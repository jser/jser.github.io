// LICENSE : MIT
"use strict";
var rulePrh = require("textlint-rule-prh");
module.exports = function (context, options) {
    var rule = rulePrh(context, options);
    // overwrite
    var isCurrentHTMLBlock = false;
    var originalStr = rule[context.Syntax.Str];
    rule[context.Syntax.Html] = function () {
        isCurrentHTMLBlock = true;
    };
    // ---- <h1 class="site-genre">ヘッドライン</h1> きたらリセット
    rule[context.Syntax.HorizontalRule] = function () {
        isCurrentHTMLBlock = false;
    };
    // 次のParagraphがきたらHTMLブロックは終わった事にする
    rule[context.Syntax.Paragraph] = function () {
        isCurrentHTMLBlock = false;
    };
    rule[context.Syntax.Str] = function (node) {
        if (isCurrentHTMLBlock) {
            return;
        }
        originalStr(node);
    };
    return rule;
};

