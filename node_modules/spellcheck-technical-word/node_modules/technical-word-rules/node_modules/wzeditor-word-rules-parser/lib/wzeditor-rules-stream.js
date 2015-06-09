/**
 * Created by azu on 2014/06/04.
 * LICENSE : MIT
 */
"use strict";
var parser = require("./wzeditor-rules-parser");
var es = require('event-stream');

function parseStream() {
    return es.map(function (line, callback) {
        try {
            var object = parser.lineParse(line);
            callback(null, object)
        } catch (error) {
            callback(error);
        }
    })
}
module.exports = parseStream;