// LICENSE : MIT
"use strict";
var glob = require("glob");
var path = require("path");
var koDir = path.join(__dirname, "..", "_i18n", "ko");
var translatedFiles = glob.sync(koDir + "/**/*.md");
var MDFileParser = require("./lib/MDFileParser");

/**
 * validate translator, then return array of errors.
 * @returns {Error[]}
 */
module.exports = function validateTranslator() {
    var parsedFiles = translatedFiles.map(function (filePath) {
        return new MDFileParser(filePath);
    });
    var translatorWarningFiles = parsedFiles.filter(function (parser) {
        var translator = parser.getTranslator();
        return translator == null || translator.length === 0;
    }).map(function (checker) {
        return checker.file;
    });
    return translatorWarningFiles.map(function (filePath) {
        return new Error('Error : "Not found `translator` meta field" @ ' + filePath + '\n' +
            'Add "translator: <Your Name>" to yaml header.');
    });
};
