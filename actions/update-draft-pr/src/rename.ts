import path from "path";
import slug from "slug";
import { Octokit } from "@octokit/rest"
import { createKoreFile, createGitHubAdaptor, KoreFile } from "korefile"

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
        console.log("headline is not defined");
        return content;
    }
    console.log("# headline")
    console.log(headline);
    console.log("# content")
    console.log(content);
    const replacedContent = content.replace(/---\s+JSer\.info #(\d+)[\s\S]+\n\n----\n\n<h1/, `---

JSer.info #$1 - ${headline}

----

<h1`);
    console.log("# replaced");
    console.log(replacedContent);
    return replacedContent;
}
/**
 *
 * @param {*} robot
 * @param koreFile
 * @param {string} owner
 * @param {string} repo
 * @param {string} branch
 * @returns {Promise<void>}
 *
 * https://medium.com/@obodley/renaming-a-file-using-the-git-api-fed1e6f04188
 * http://www.levibotelho.com/development/commit-a-file-with-the-github-api/
 */
const renameCommit = async (koreFile: KoreFile, { originalFileName, renameFn }: {
    originalFileName: string,
    renameFn: (oldFileName: string, content: string) => { newFileName: string, newContent: string }
}) => {
    console.log("start rename(delete and create)", originalFileName);
    // get content
    // http://octokit.github.io/rest.js/#api-Repos-getContent
    const originalContent = await koreFile.readFile(originalFileName);
    const { newFileName, newContent } = renameFn(originalFileName, originalContent);
    if (originalFileName === newFileName && originalContent === newContent) {
        console.log(`No need to commit: ${originalFileName}`);
        return;
    }
    if (originalFileName === newFileName) {
        console.log("Update Content");
        // Update Content
        // https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#create-or-update-file-contents
        await koreFile.writeFile(originalFileName, newContent);
        console.log("Updated ", originalFileName)
    } else {
        console.log(`Rename: ${originalFileName} -> ${newFileName}`);
        // update file
        // https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#create-or-update-file-contents
        await koreFile.writeFile(newFileName, newContent);
        console.log("Create", newContent);
        // remove original file
        await koreFile.deleteFile(originalFileName);
        console.log("Delete", originalFileName);
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

export const rename = async (payload: {
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
    },
    GITHUB_TOKEN: string
}) => {
    const koreFile = createKoreFile({
        adaptor: createGitHubAdaptor({
            owner: payload.owner,
            repo: payload.repo,
            ref: `heads/${payload.head.ref}`,
            token: payload.GITHUB_TOKEN
        })
    });
    const octokit = new Octokit({
        auth: payload.GITHUB_TOKEN
    });
    const newTitle = payload.forceFitToTitle;
    const compare = await octokit.repos.compareCommits(
        {
            owner: payload.owner,
            repo: payload.repo,
            base: payload.base.sha,
            head: payload.head.sha
        }
    );
    const promises = compare.data.files
        .filter(file => {
            return file.status === "added" || file.status === "modified";
        })
        .filter(file => {
            const originalFileName = file.filename;
            return canRename(originalFileName);
        })
        .map(file => {
            return renameCommit(koreFile, {
                originalFileName: file.filename,
                renameFn: (fileName, content) => {
                    // Update Pull Request title
                    // if newTitle exists, replace fileName and content:title with newTitle
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
