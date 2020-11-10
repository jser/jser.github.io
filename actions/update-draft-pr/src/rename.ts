import path from "path";
import slug from "slug";
import { Octokit } from "@octokit/rest"

const slugTitle = (title: string) => {
    const tenTitle = title.replace(/、/g, "-");
    return slug(tenTitle, {
        remove: null,
        lower: true
    });
};

interface EmbedHeadlineParams {
    content: string;
    headline?: string;
}

const embedHeadline = ({ content, headline }: EmbedHeadlineParams): string => {
    if (!headline) {
        return content;
    }
    return content.replace(/---\s+JSer.info #\d+\s+----/, `---

JSer.info #512 - ${headline}

----`);
}
/**
 *
 * @param {*} robot
 * @param octokit
 * @param {string} owner
 * @param {string} repo
 * @param {string} branch
 * @returns {Promise<void>}
 *
 * https://medium.com/@obodley/renaming-a-file-using-the-git-api-fed1e6f04188
 * http://www.levibotelho.com/development/commit-a-file-with-the-github-api/
 */
const renameCommit = async (octokit: Octokit, { ref, sha, owner, repo, branch, originalFileName, renameFn }: {
    ref: string, sha: string; owner: string, repo: string, branch: string, originalFileName: string,
    renameFn: (oldFileName: string, content: string) => { newFileName: string, newContent: string }
}) => {
    console.log("start rename(delete and create)", {
        ref,
        owner,
        repo,
        branch,
        originalFileName
    });
    // get content
    // http://octokit.github.io/rest.js/#api-Repos-getContent
    const { data: getContentResponse } = await octokit.repos.getContent({
        owner,
        repo,
        path: originalFileName,
        ref
    });
    if (!("content" in getContentResponse)) {
        throw new Error("no content: " + getContentResponse);
    }
    if (!getContentResponse.content) {
        throw new Error("no content: " + getContentResponse);
    }
    const decodedContent = Buffer.from(getContentResponse.content, "base64").toString();
    const { newFileName, newContent } = renameFn(originalFileName, decodedContent);
    if (originalFileName === newFileName && decodedContent === newContent) {
        console.log(`No need to commit: ${originalFileName}`);
        return;
    }
    if (originalFileName === newFileName) {
        console.log("Update Content");
        // Update Content
        const { data: createOrUpdateResponse } = await octokit.repos.createOrUpdateFileContents({
            owner,
            repo,
            path: newFileName,
            message: `Update ${newFileName}`,
            content: Buffer.from(newContent).toString("base64"),
            branch,
            sha
        });
        console.log("createOrUpdateResponse", createOrUpdateResponse)
    } else {
        console.log(`Rename: ${originalFileName} -> ${newFileName}`);
        // update file
        // https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#create-or-update-file-contents
        const { data: createFileResponse } = await octokit.repos.createOrUpdateFileContents({
            owner,
            repo,
            path: newFileName,
            message: `Move ${originalFileName} to ${newFileName}`,
            content: Buffer.from(newContent).toString("base64"),
            branch
        });
        console.log("createFileResponse", createFileResponse);
        // remove original file
        const { data: deleteFileResponse } = await octokit.repos.deleteFile({
            owner,
            repo,
            path: originalFileName,
            message: `Remove ${originalFileName}`,
            sha: getContentResponse.sha,
            branch
        });
        console.log("deleteFileResponse", deleteFileResponse);
    }
    return {
        status: "ok"
    };
};

const RENAME_TARGET = /(_i18n\/ja\/_posts\/\d+)\/(.*?\.md$)/;
const canRename = (originalFilePath: string) => {
    return RENAME_TARGET.test(originalFilePath);
};
/**
 * PR title -> content:title
 * replace content:title to newTitle
 * @returns {*}
 */
const replaceContentTitle = (content: string, newTitle: string) => {
    const titlePattern = /title: "(\d{4})-(\d{2})-(\d{2})のJS:(.*)"/;
    if (!titlePattern.test(content)) {
        return content;
    }
    return content.replace(titlePattern, `title: "${newTitle}"`);
};

/**
 * PR title -> file newm
 * @returns {*}
 */
const renameFilePathWithNewTitle = (originalFilePath: string, newTitle: string) => {
    if (!RENAME_TARGET.test(originalFilePath)) {
        return originalFilePath;
    }
    const titlePattern = /^(\d{4})-(\d{2})-(\d{2})のJS:(.*)/;
    if (!titlePattern.test(newTitle)) {
        return originalFilePath;
    }
    // @ts-ignore
    const [_, year, month, day, keyword] = newTitle.match(titlePattern);
    const trimmedKeyword = keyword.trim();
    // Title is empty
    if (trimmedKeyword.length === 0) {
        return originalFilePath;
    }
    const newSlug = slugTitle(trimmedKeyword);
    const ext = path.extname(originalFilePath);
    return originalFilePath.replace(RENAME_TARGET, (_all, pathname) => {
        return `${pathname}/${year}-${month}-${day}-${newSlug}${ext}`;
    });
};

/**
 * title: ** -> file name
 * content's title to file name
 * @param originalFilePath
 * @param content https://developer.github.com/v3/repos/contents/#get-contents
 * @returns {*}
 */
const renamePattern = (originalFilePath: string, content: string) => {
    if (!RENAME_TARGET.test(originalFilePath)) {
        return originalFilePath;
    }
    const titlePattern = /title: "(\d{4})-(\d{2})-(\d{2})のJS:(.*)"/;
    if (!titlePattern.test(content)) {
        return originalFilePath;
    }
    // @ts-ignore
    const [_, year, month, day, keyword] = content.match(titlePattern);
    const trimmedKeyword = keyword.trim();
    // Title is empty
    if (trimmedKeyword.length === 0) {
        return originalFilePath;
    }
    const newSlug = slugTitle(trimmedKeyword);
    const ext = path.extname(originalFilePath);
    return originalFilePath.replace(RENAME_TARGET, (_all, pathname) => {
        return `${pathname}/${year}-${month}-${day}-${newSlug}${ext}`;
    });
};

export const rename = async (octokit: Octokit, payload: {
    owner: string;
    repo: string;
    // if exits, title based rename
    forceFitToTitle?: string
    // headline from body
    headline?: string;
    head: {
        ref: string;
        sha: string;
    }
    base: {
        ref: string;
        sha: string
    }
}) => {
    const newTitle = payload.forceFitToTitle;
    const compare = await octokit.repos.compareCommits(
        {
            owner: payload.owner,
            repo: payload.repo,
            base: payload.base.sha,
            head: payload.head.sha
        }
    );
    const branch = payload.head.ref.replace("refs/heads/", "");
    const promises = compare.data.files
        .filter(file => {
            return file.status === "added" || file.status === "modified";
        })
        .filter(file => {
            const originalFileName = file.filename;
            return canRename(originalFileName);
        })
        .map(file => {
            return renameCommit(octokit, {
                owner: payload.owner,
                repo: payload.repo,
                ref: payload.head.ref,
                sha: payload.head.sha,
                branch,
                originalFileName: file.filename,
                renameFn: (fileName, content) => {
                    // Update Pull Request title
                    // if newTitle exists, replace fileName and content:title with newTtile
                    const newContent = newTitle
                        ? replaceContentTitle(content, newTitle)
                        : content;
                    return {
                        newFileName: newTitle
                            ? renameFilePathWithNewTitle(fileName, newTitle)
                            : renamePattern(fileName, content),
                        newContent: embedHeadline({ content: newContent, headline: payload.headline })
                    };
                }
            });
        });
    return Promise.all(promises);
};
