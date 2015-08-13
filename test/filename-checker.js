// LICENSE : MIT
"use strict";
var glob = require("glob");
var path = require("path");
var targetDir = path.join(__dirname, "..", "_i18n");
var files = glob.sync(targetDir + "/**/*.md");
function postFileNameChecker() {
    var validFileNameRegExp = /\d{4}-\d{2}-\d{2}-([\w\.\-]*?)\.md/i;
    var wrongSlugRegExp = /(^title$)/i;
    var warningFiles = files.filter(function (filePath) {
        var fileName = path.basename(filePath);
        var match = fileName.match(validFileNameRegExp);
        if (match) {
            var postSlug = match[1];
            if (wrongSlugRegExp.test(postSlug)) {
                // wrong
                return true;
            }
        } else {
            // wrong
            return true;
        }
        // valid file
        return false;
    });
    return warningFiles.map(function (filePath) {
        return new Error('Error : "Wrong file name @ ' + filePath + '\n');
    });
}
/**
 * validate filename, then return array of errors.
 * @returns {Error[]}
 */
module.exports = postFileNameChecker;