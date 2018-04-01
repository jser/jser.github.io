#!/usr/bin/env node
"use strict";
const glob = require("glob-all");
const parseDetails = require("jser-item-category-parser").parseDetails;
const fs = require("fs");
const path = require("path");
const makeDir = require('make-dir');
const jaDir = path.normalize(path.join(__dirname, "..", "_i18n/ja/"));
const ampDir = path.normalize(path.join(__dirname, "..", "amp"));
const mdFiles = glob.sync([
    `${jaDir}/**/*.md`,
    `!${jaDir}/_posts/events/*.md`,
    `!${jaDir}/_posts/support/*.md`,
    `!${jaDir}/_posts/tumblr/*.md`,
    `!${jaDir}/_posts/about/*.md`,
]);
const template = (result) => {


};
/* urlとカテゴリ(記事中の分類)を関連付けたJSONを作る
    [{
        category: "ヘッドライン",
        url: "http://example.com"
    }]
 */
mdFiles.forEach(mdFilePath => {
    const content = fs.readFileSync(mdFilePath, "utf-8");
    const pathname = mdFilePath.replace(`${jaDir}_posts/`, "");
    const ampPath = path.join(ampDir, pathname);
    try {
        const result = parseDetails(content, {
            filePath: mdFilePath
        });
        let dirname = path.dirname(ampPath);
        makeDir.sync(dirname);
        fs.writeFileSync(ampPath, JSON.stringify(result), "utf-8");
    } catch (error) {
        console.log(mdFilePath);
        console.error(error);
    }
});
