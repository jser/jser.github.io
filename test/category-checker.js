// LICENSE : MIT
"use strict";
var glob = require("glob");
var path = require("path");
var targetDir = path.join(__dirname, "..", "_i18n");
var files = glob.sync(targetDir + "/**/*.md");
var MDFileParser = require("./lib/MDFileParser");
function isEmptyCategory(categories) {
    return categories.length === 0;
}
/**
 * validate category, then return array of errors.
 * @returns {Error[]}
 */
module.exports = function validateCategory() {
    var warningFiles = files.map(function (filePath) {
        return new MDFileParser(filePath);
    }).filter(function (checker) {
        return isEmptyCategory(checker.getCategories());
    }).map(function (checker) {
        return checker.file;
    });

    return warningFiles.map(function (filePath) {
        return new Error('Error : "Not found category" @ ' + filePath);
    });
};