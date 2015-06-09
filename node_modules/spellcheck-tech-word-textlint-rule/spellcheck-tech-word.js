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
    exports[context.Syntax.Str] = function (node) {
        if (helper.isChildNode(node, [Syntax.Link, Syntax.Image, Syntax.BlockQuote])) {
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
