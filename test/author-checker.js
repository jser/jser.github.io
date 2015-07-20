// LICENSE : MIT
"use strict";
var glob = require("glob");
var path = require("path");
var targetDir = path.join(__dirname, "..", "_i18n");
var files = glob.sync(targetDir + "/**/*.md");
var MDFileParser = require("./lib/MDFileParser");

/**
 * validate translator, then return array of errors.
 * @returns {Error[]}
 */
module.exports = function validateTranslator() {
    var parsedFiles = files.map(function (filePath) {
        return new MDFileParser(filePath);
    });
    var translatorWarningFiles = parsedFiles.filter(function (parser) {
        var author = parser.getAuthor();
        return author == null || author.length === 0;
    }).map(function (checker) {
        return checker.file;
    });
    return translatorWarningFiles.map(function (filePath) {
        return new Error('Error : "Not found `author` meta field" @ ' + filePath + '\n' +
            'Add "author: <Your Name>" to yaml header.');
    });
};
