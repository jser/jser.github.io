// LICENSE : MIT
"use strict";
var fs = require("fs");
var http = require("http");
http.get("http://azu.github.io/technical-word-rules/all.json", function (res) {
    var body = '';
    res.setEncoding('utf8');

    res.on('data', function (chunk) {
        body += chunk;
    });
    res.on('end', function (res) {
        fs.writeFileSync(require("path").join(__dirname, "all.json"), body, "utf-8");
    });
}).on('error', function (e) {
    console.log("Got error: " + e.message);
});