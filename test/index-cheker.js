// LICENSE : MIT
"use strict";
var SUCCESS_STATUS = 0;
var FAIL_STATUS = 1;
var categoryChecker = require("./category-checker");
var translatorChecker = require("./translator-checker");
var authorChecker = require("./author-checker");

function check(checker) {
    var resultsError = checker();
    if (resultsError.length > 0) {
        console.log("Found Error on " + checker.name);
    }
    resultsError.forEach(function (error) {
        console.error(error.message);
    });
    if (resultsError.length > 0) {
        console.log("----------------------------------------\n");
    }
    return resultsError.length > 0 ? FAIL_STATUS : SUCCESS_STATUS;
}

[categoryChecker, translatorChecker, authorChecker].map(check).forEach(function (status) {
    if (status === FAIL_STATUS) {
        process.exit(FAIL_STATUS);
    }
});