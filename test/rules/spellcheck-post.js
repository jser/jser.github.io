// LICENSE : MIT
"use strict";
var RuleHelper = require("textlint-rule-helper").RuleHelper;
var spellCheck = require("spellcheck-technical-word").spellCheckText;
/**
 * @param {RuleContext} context
 */
module.exports = function (context) {
    var helper = new RuleHelper(context);
    var exports = {};
    var Syntax = context.Syntax;
    // HTMLの中身は無視する
    var isCurrentHTMLBlock = false;
    exports[context.Syntax.Html] = function (node) {
        isCurrentHTMLBlock = true;
    };
    // ---- <h1 class="site-genre">ヘッドライン</h1> きたらリセット
    exports[context.Syntax.HorizontalRule] = function (node) {
        isCurrentHTMLBlock = false;
    };
    // 次のParagraphがきたらHTMLブロックは終わった事にする
    exports[context.Syntax.Paragraph] = function (node) {
        isCurrentHTMLBlock = false;
    };
    exports[context.Syntax.Str] = function (node) {
        if (isCurrentHTMLBlock) {
            return;
        }
        // Headerは自動でサイトのタイトルを使うので無視する
        if (helper.isChildNode(node, [Syntax.Link, Syntax.Image, Syntax.BlockQuote, Syntax.Header])) {
            return;
        }
        var text = context.getSource(node);
        var results = spellCheck(text);
        results.forEach(function (/*SpellCheckResult*/result) {
            // line, column
            context.report(node, new context.RuleError(result.actual + " => " + result.expected, {
                line: result.paddingLine,
                column: result.paddingColumn
            }));
        });
    };
    return exports;
};
