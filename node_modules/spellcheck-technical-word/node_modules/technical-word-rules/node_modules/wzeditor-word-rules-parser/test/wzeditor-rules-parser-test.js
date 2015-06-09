"use strict";
var assert = require("power-assert");
var fs = require("fs");
var parser = require("../lib/wzeditor-rules-parser");
function assertRegExp(actual, expect) {
    assert.equal(String(new RegExp(actual)), String(expect));
}
describe("wzeditor-rules-parser", function () {
    var file = fs.readFileSync(__dirname + "/../dictionary/WEB+DB PRESS用語統一ルール", "utf-8");

    context(".pattern", function () {

        context("When 前置文字だけの場合", function () {
            var content = "Git";
            it("大文字を無視する変換の正規表現を生成", function () {
                var result = parser.parse(content);
                assertRegExp(result[0].pattern, /\bGit\b/);
                assert.equal(result[0].flag, "i");
            });
        });
        context("単純な文字列置換において", function () {
            context("変更前単語がアルファベットの場合", function () {
                var content = "AFTER\tabc";
                it("境界値を含めた変換する正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /\babc\b/);
                    assert(result[0].flag == null);
                });
            });
            context("変更前単語が日本語の場合", function () {
                var content = "変換後\t日本語";
                it("完全一致で変換する正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /日本語/);
                });
            });
        });
        context("変更前単語 + 前置文字のみの場合で", function () {
            context("変更前単語が日本語の時", function () {
                var content = "変換後\t日本語\t[\\d]";
                it("前置文字 + 変更前単語 の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /([\d])日本語/);
                });
            });
            context("変更前単語がアルファベットの時", function () {
                var content = "変換後\tABC\t[\\d]";
                it("変更前単語 \b 前置文字 の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /([\d])\bABC\b/);
                });
            });
        });
        context("変更前単語 + 後置文字のみの場合で", function () {
            context("変更前単語が日本語の時", function () {
                var content = "変換後\t日本語\t,[\\d]";
                it("変更前単語 + 後置文字 の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /日本語([\d])/);
                });
            });
            context("変更前単語がアルファベットの時", function () {
                var content = "変換後\tABC\t,[\\d]";
                it("変更前単語 \b 後置文字 の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /\bABC\b([\d])/);
                });
            });
            context("変更前単語がアルファベット+スペースの時", function () {
                var content = "変換後\tA B C\t,[\\d]";
                it("変更前単語 \b 後置文字 の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /\bA B C\b([\d])/);
                });
            });
        });
        context("前置文字、後置文字両方ある場合で", function () {
            context("変更前単語が日本語の時", function () {
                var content = "変換後\t日本語\t[\\w],[\\d]";
                it("(前置文字 + 変更前単語) or (変更前単語 + 後置文字)の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /(?:([\w])日本語)|(?:日本語([\d]))/);
                    assert.equal(result[0].expected, "$1変換後$2");
                });
            });
            context("変更前単語がアルファベットの時", function () {
                var content = "変換後\tABC\t[\\w],[\\d]";
                it("(前置文字 \b 変更前単語) or (変更前単語 b 後置文字)の正規表現を生成", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /(?:([\w])\bABC)|(?:ABC\b([\d]))/);
                    assert.equal(result[0].expected, "$1変換後$2");
                });
            });
        });
        context("変更前単語に|があるケースについて", function () {
            context("指定されてるのが変更前単語のみの時", function () {
                it("|で区切られたORの正規表現が作成される", function () {
                    var enContent = "変換後\tABC|EFG";
                    var result_en = parser.parse(enContent);
                    assertRegExp(result_en[0].pattern, /\bABC\b|\bEFG\b/);

                    var jaContent = "変換後\t日本語|EFG";
                    var result_ja = parser.parse(jaContent);
                    assertRegExp(result_ja[0].pattern, /日本語|\bEFG\b/);
                });
            });
            context("前置、後置文字がある時", function () {
                var content = "変換後\tABC|EFG\t[\\w],[\\d]";
                it("|でそれぞれ別々のオブジェクトが組み立てられる", function () {
                    var result = parser.parse(content);
                    assert(result.length == "ABC|EFG".split("|").length);
                });
                it("|で区切られたオブジェクトはそれぞれ前置文字、後置文字があるケースとして処理される", function () {
                    var result = parser.parse(content);
                    assertRegExp(result[0].pattern, /(?:([\w])\bABC)|(?:ABC\b([\d]))/);
                    assertRegExp(result[1].pattern, /(?:([\w])\bEFG)|(?:EFG\b([\d]))/);
                });
            });
        });
        context("正規表現オプション RE について", function () {
            context("オプションREが指定されていない場合", function () {
                it("変更前単語は文字列として扱われる", function () {
                    var content = "変換後\t単語[\\d]";
                    var results = parser.parse(content);
                    assertRegExp(results[0].pattern, /単語\[\\d\]/);
                });
                it("前置との組み合わせ時も変更前単語は文字列として扱われる", function () {
                    var content = "変換後\t単語[\\d]\t[\\d]";
                    var results = parser.parse(content);
                    assertRegExp(results[0].pattern, /([\d])単語\[\\d\]/);
                });
            });
            context("オプションREが指定されている場合", function () {
                var content = "変換後\t単語[\\d]\t,,RE";
                it("変更前単語は正規表現として扱われる", function () {
                    var results = parser.parse(content);
                    assertRegExp(results[0].pattern, /単語[\d]/);
                });

                it("前置との組み合わせ時も変更前単語は正規表現として扱われる", function () {
                    var content = "変換後\t単語[\\d]\t[\\d],,RE";
                    var results = parser.parse(content);
                    assertRegExp(results[0].pattern, /([\d])単語[\d]/);
                });
            });
        });
    });
    context(".afterRegexp", function () {
        context("when contain \1\2", function () {
            var content = "変換後\\1\\2\t(単語)";
            it("should replace to $1$2", function () {
                var results = parser.parse(content);
                assert.equal(results[0].expected, "変換後$1$2");
            });
        });
        context("when contain \2", function () {
            var content = "変換後\\2\t(単語)";
            it("should replace to $2", function () {
                var results = parser.parse(content);
                assert.equal(results[0].expected, "変換後$2");
            });
        });
    });
});