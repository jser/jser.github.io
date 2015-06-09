"use strict";
var dictionaryItems = require("technical-word-rules");
var StructuredSource = require('structured-source');
/**
 * spell check the text, then return array of result.
 * @param {string} text
 * @returns {SpellCheckResult[]}
 */
function spellCheckText(text) {
    var src = new StructuredSource(text);
    var results = [];
    for (var i = 0, length = dictionaryItems.length; i < length; i++) {
        var dictionary = dictionaryItems[i];
        var query = new RegExp(dictionary.pattern, dictionary.flag);
        var match = query.exec(text);
        if (!match) {
            continue;
        }
        var matchedString = match[0];
        // s/Web/Web/iは大文字小文字無視してWebに変換したいという意味に対応する
        if (dictionary.flag != null) {
            var strictQuery = new RegExp(dictionary.pattern);
            var isStrictMatch = strictQuery.test(match[0]);
            // /Web/i でマッチするけど、 /Web/ でマッチするならそれは除外する
            if (isStrictMatch) {
                continue;
            }
        }

        // s/ベンダ/ベンダー/ のようにexpectedがpatternを包含している場合のexpectedを除外
        var expectedQuery = new RegExp('^' + dictionary.expected);
        if (expectedQuery.test(text.slice(match.index))) {
            continue;
        }

        // [start, end]
        var expected = matchedString.replace(query, dictionary.expected);
        var position = src.indexToPosition(match.index);
        /**
         *
         * @typedef {{actual: string, expected: string, paddingLine: number, paddingColumn: number}} SpellCheckResult
         */
        var result = {
            actual: matchedString,
            expected: expected,
            paddingLine: position.line - 1,// start with 0
            paddingColumn: position.column// start with 0
        };


        results.push(result);
    }
    return results;
}

module.exports = {
    spellCheckText: spellCheckText
};
