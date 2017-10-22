#!/usr/bin/env node
"use strict";
const glob = require("glob-all");
const parse = require("jser-item-category-parser").parse;
const fs = require("fs");
const path = require("path");
const jaDir = path.join(__dirname, "..", "_i18n/ja");
const outputFilePath = path.join(__dirname, "..", "public", "build/item-category.json");
const mdFiles = glob.sync([
    `${jaDir}/**/*.md`,
    `!${jaDir}/events/*.md`,
    `!${jaDir}/support/*.md`,
    `!${jaDir}/tumblr/*.md`,
    `!${jaDir}/about/*.md`,
]);
/* urlとカテゴリ(記事中の分類)を関連付けたJSONを作る
    [{
        category: "ヘッドライン",
        url: "http://example.com"
    }]
 */
let resultJSON = [];
mdFiles.forEach(mdFilePath => {
    const content = fs.readFileSync(mdFilePath, "utf-8");
    try {
        const maps = parse(content);
        resultJSON = resultJSON.concat(maps);
    } catch (error) {
        console.log(mdFilePath);
        console.error(error);
    }
});

fs.writeFileSync(outputFilePath, JSON.stringify(resultJSON), "utf-8");