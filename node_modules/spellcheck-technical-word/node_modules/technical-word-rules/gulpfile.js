"use strict";
var gulp = require("gulp");
var source = require('vinyl-source-stream');
var fs = require("fs");
var concat = require('gulp-concat');
var parse = require("wzeditor-word-rules-parser").parse;
var es = require("event-stream");
function string_src(filename, string) {
    var src = require('stream').Readable({objectMode: true});
    src._read = function () {
        this.push(new gutil.File({cwd: "", base: "", path: "index.json", contents: new Buffer(string)}));
        this.push(null)
    };
    return src
}
gulp.task("build", function () {
    var writeStream = fs.createWriteStream('./all.json');
    return gulp.src("dict/*.txt")
        .pipe(concat("all.txt"))
        // -> gulp -> file stream
        .pipe(es.map(function (file, cb) {
            try {
                var result = parse(String(file.contents));
                fs.writeFile("./all.json", JSON.stringify(result), cb);
            } catch (e) {
                cb(e);
            }
        }))
});
gulp.task('default', ['build']);