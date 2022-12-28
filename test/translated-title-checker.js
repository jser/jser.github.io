// LICENSE : MIT
"use strict";
const glob = require("glob");
const path = require("path");
const koDir = path.join(__dirname, "..", "_i18n", "ko");
const translatedFiles = glob.sync(koDir + "/**/*.md");
const MDFileParser = require("./lib/MDFileParser");

/**
 * validate translator, then return array of errors.
 * @returns {Error[]}
 */
module.exports = function validateTranslator() {
    const parsedFiles = translatedFiles.map(function (filePath) {
        return new MDFileParser(filePath);
    });
    const translatedWarningFiles = parsedFiles.flatMap(function (parser) {
        const title = parser.getTitle();
        if (/のJS/.test(title)) {
            return [new Error("should strip 'のJS' from title: " + title + " in " + parser.file)];
        }
        // if (/、/.test(title)) {
        //     return [new Error("should replace '、' with ',': " + title + " in " + parser.file + "\n\n" + title.replaceAll("、", ","))];
        // }
        return []
    })
    return translatedWarningFiles;
};
