// LICENSE : MIT
"use strict";
var fs = require("fs");
var glob = require("glob");
var path = require("path");
var fm = require('front-matter');
var targetDir = path.join(__dirname, "..", "_i18n");
var files = glob.sync(targetDir + "/**/*.md");

function Checker(file) {
    this.file = file;
    this.parsedTree = fm(fs.readFileSync(file, "utf-8"));
}
Checker.prototype.getCategories = function () {
    var cats = [];
    if (this.parsedTree.attributes["categories"]) {
        cats.concat(this.parsedTree.attributes["categories"].fileter(function (name) {
            return name.length > 0;
        }));
    }
    if (this.parsedTree.attributes["category"] && this.parsedTree.attributes["category"].length > 0) {
        cats.push(this.parsedTree.attributes["category"]);
    }
    return cats;
};

function isEmptyCategory(categories) {
    return categories.length === 0;
}


// <MAIN>
var warningFiles = files.map(function (filePath) {
    return new Checker(filePath);
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
