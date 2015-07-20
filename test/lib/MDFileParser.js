// LICENSE : MIT
"use strict";
var fs = require("fs");
var fm = require('front-matter');
function MDFileParser(file) {
    this.file = file;
    this.parsedTree = fm(fs.readFileSync(file, "utf-8"));
}
MDFileParser.prototype.getCategories = function () {
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
MDFileParser.prototype.getAuthor = function () {
    return this.parsedTree.attributes["author"];
};
MDFileParser.prototype.getTranslator = function () {
    return this.parsedTree.attributes["translator"];
};
module.exports = MDFileParser;