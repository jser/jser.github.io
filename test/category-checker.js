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

// <MAIN>
var warningFiles = files.map(function (filePath) {
    return new MDFileParser(filePath);
}).filter(function (checker) {
    return isEmptyCategory(checker.getCategories());
}).map(function (checker) {
    return checker.file;
});

warningFiles.forEach(function (filePath) {
    console.error('Error : "Not found category" @ ' + filePath);
});

if (warningFiles.length > 0) {
    process.exit(1);
}
