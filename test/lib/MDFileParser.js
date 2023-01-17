// LICENSE : MIT
"use strict";
const fs = require("fs");
const assert = require("assert");
const fm = require('front-matter');

class MDFileParser {
    constructor(file) {
        this.file = file;
        const fileContent = fs.readFileSync(file, "utf-8");
        assert(fileContent.startsWith("---"), "should start front matter, but this file does not start with --- " + file);
        this.parsedTree = fm(fileContent);
    }
    
    getCategories() {
        const cats = [];
        if (this.parsedTree.attributes["categories"]) {
            cats.concat(this.parsedTree.attributes["categories"].fileter(function (name) {
                return name.length > 0;
            }));
        }
        if (this.parsedTree.attributes["category"] && this.parsedTree.attributes["category"].length > 0) {
            cats.push(this.parsedTree.attributes["category"]);
        }
        return cats;
    }
    
    getAuthor() {
        return this.parsedTree.attributes["author"];
    }
    
    getTranslator() {
gi        return this.parsedTree.attributes["translator"];
    }
    
    getTitle() {
        return this.parsedTree.attributes["title"];
    }
}

module.exports = MDFileParser;
