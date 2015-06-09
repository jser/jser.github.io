// LICENSE : MIT
"use strict";
var assert = require("power-assert");
var fs = require("fs"),
    path = require("path");
var textlint = require("textlint").textlint;

// ✘ HTML Import
// ✔ HTML Imports
describe("spellcheck-tech-word.js", function () {
    beforeEach(function () {
        textlint.setupRules({
            // rule-key : rule
            "spellcheck-tech-word": require("../spellcheck-tech-word")
        });
    });
    afterEach(function () {
        textlint.resetRules();
    });
    it("should lint wrong tech words", function () {
        var filePath = path.join(__dirname, "/fixtures/wrong.md");
        var result = textlint.lintFile(filePath);
        assert(result.filePath === filePath);
        assert(result.messages.length > 0);
        var message = result.messages[0].message;
        assert.equal(message, "HTML Import => HTML Imports");
    });
    context("expect Link, Image and block", function () {
        it("should not lint wrong tech words", function () {
            var filePath = path.join(__dirname, "/fixtures/no-error.md");
            var result = textlint.lintFile(filePath);
            assert(result.filePath === filePath);
            assert(result.messages.length == 0);
        });
    });
});