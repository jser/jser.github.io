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
let resultJSON = [];
mdFiles.forEach(mdFilePath => {
    const content = fs.readFileSync(mdFilePath, "utf-8");
    const maps = parse(content);
    resultJSON = resultJSON.concat(maps);
});

fs.writeFileSync(outputFilePath, JSON.stringify(resultJSON), "utf-8");