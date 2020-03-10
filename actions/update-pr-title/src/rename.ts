import path from "path";
import slug from "slug";
import { Octokit } from "@octokit/rest"

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
const renameCommit = async (octokit: Octokit, {ref, owner, repo, branch, originalFileName, renameFn}: {
    ref: string, owner: string, repo: string, branch: string, originalFileName: string,
    renameFn: (oldFileName: string, content: string) => string
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
    const {data: getContentResponse} = await octokit.repos.getContents({
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
    const decodedContent = new Buffer(getContentResponse.content, "base64").toString();
    const newFileName = renameFn(originalFileName, decodedContent);
    if (originalFileName === newFileName) {
        console.log(`No need to rename: ${originalFileName}`);
        return;
    }
    console.log(`Rename: ${originalFileName} -> ${newFileName}`);
    // create new file
    // https://developer.github.com/v3/repos/contents/#create-a-file
    const {data: createFileResponse} = await octokit.repos.createFile({
        owner,
        repo,
        path: newFileName,
        message: `Move ${originalFileName} to ${newFileName}`,
        content: getContentResponse.content,
        branch
    });
    console.log("createFileResponse", createFileResponse);
    // remove original file
    const {data: deleteFileResponse} = await octokit.repos.deleteFile({
        owner,
        repo,
        path: originalFileName,
        message: `Remove ${originalFileName}`,
        sha: getContentResponse.sha,
        branch
    });
    console.log("deleteFileResponse", deleteFileResponse);
    return {
        status: "ok"
    };
};

const RENAME_TARGET = /(_i18n\/ja\/_posts\/\d+)\/(.*?\.md$)/;
const canRename = (originalFilePath: string) => {
    return RENAME_TARGET.test(originalFilePath);
};
/**
 *
 * @param originalFilePath
 * @param content https://developer.github.com/v3/repos/contents/#get-contents
 * @returns {*}
 */
const renamePattern = (originalFilePath: string, content: any) => {
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
    const newSlug = slug(trimmedKeyword, {
        remove: null,
        lower: true
    });
    const ext = path.extname(originalFilePath);
    return originalFilePath.replace(RENAME_TARGET, (_all, pathname) => {
        return `${pathname}/${year}-${month}-${day}-${newSlug}${ext}`;
    });
};

export const rename = async (octokit: Octokit, payload: {
    owner: string;
    repo: string;
    head: {
        ref: string;
        sha: string;
    }
    base: {
        ref: string;
        sha: string
    }
}) => {
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
                branch,
                originalFileName: file.filename,
                renameFn: (fileName, content) => {
                    return renamePattern(fileName, content);
                }
            });
        });
    return Promise.all(promises);
};
