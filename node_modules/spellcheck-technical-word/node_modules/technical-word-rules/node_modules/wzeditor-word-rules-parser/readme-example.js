/**
 * Created by azu on 2014/10/12.
 * LICENSE : MIT
 */
"use strict";
var fs = require("fs");
var parser = require("./lib/wzeditor-rules-parser");
var content = fs.readFileSync(__dirname + "/dictionary/WEB+DB PRESS用語統一ルール", "utf-8");
var result = parser.parse(content);
console.log(result);