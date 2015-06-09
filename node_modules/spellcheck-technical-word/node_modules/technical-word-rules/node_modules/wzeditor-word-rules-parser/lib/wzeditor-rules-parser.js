"use strict";
var alphabetRegExp = /^[a-zA-Z\s]+$/;
function escapeRegExp(string) {
    if (!string) {
        return;
    }
    return string.replace(/([.*+?^=!:${}()|[\]\/\\])/g, "\\$1");
}

function wrapAsPlaceHolder(string) {
    return "(" + string + ")";
}
// \1 -> $1
function replaceMatchedValue(string) {
    return string.replace(/\\/g, "$");
}
// line -> object
function patternForBeforeFieldOnly(lineObject) {
    return {
        "pattern": "\\b" + lineObject.afterField + "\\b",
        "flag": "i",
        "expected": replaceMatchedValue(lineObject.afterField)
    }
}

function stringPatternForField(fields, builder) {
    var pattens = fields.map(builder);
    return pattens.join("|");
}
function wordBuilder(predicate, string) {
    if (predicate(string)) {
        return string;
    } else {
        return escapeRegExp(string);
    }
}

function patternForBothField(lineObject) {
    var representWord = wordBuilder.bind(this, function () {
        return lineObject.hasRegExpOption;
    });
    var beforeStringPattern = stringPatternForField(lineObject.beforeFieldWords, function (word) {
        if (alphabetRegExp.test(word)) {
            return "\\b" + representWord(word) + "\\b";
        } else {
            return representWord(word);
        }
    });
    return {
        "pattern": beforeStringPattern,
        "expected": replaceMatchedValue(lineObject.afterField)
    }
}
function patternForRatherChar(lineObject) {
    var representWord = wordBuilder.bind(this, function () {
        return lineObject.hasRegExpOption;
    });
    var beforeStringPattern = stringPatternForField(lineObject.beforeFieldWords, function (word) {
        var place = [];
        // charが空の場合でも\bを入れるため空文字を追加する
        place.push(lineObject.beforeChar ? wrapAsPlaceHolder(lineObject.beforeChar) : "");
        place.push(representWord(word));
        place.push(lineObject.afterChar ? wrapAsPlaceHolder(lineObject.afterChar) : "");
        // alphabet or not
        if (alphabetRegExp.test(word)) {
            return place.join("\\b");
        } else {
            return place.join("");
        }
    });

    if (lineObject.beforeChar) {
        return {
            "pattern": beforeStringPattern,
            "expected": "$1" + replaceMatchedValue(lineObject.afterField)
        };
    }
    if (lineObject.afterChar) {
        return {
            "pattern": beforeStringPattern,
            "expected": replaceMatchedValue(lineObject.afterField) + "$1"
        };
    }
}
function patternForBothChar(lineObject) {
    var representWord = wordBuilder.bind(this, function () {
        return lineObject.hasRegExpOption;
    });
    var beforeStringPattern = lineObject.beforeFieldWords.map(function (word) {
        if (alphabetRegExp.test(word)) {
            return "(?:" + wrapAsPlaceHolder(lineObject.beforeChar) + "\\b" + representWord(word) + ")"
                + "|"
                + "(?:" + representWord(word) + "\\b" + wrapAsPlaceHolder(lineObject.afterChar) + ")"
        } else {
            return "(?:" + wrapAsPlaceHolder(lineObject.beforeChar) + representWord(word) + ")"
                + "|"
                + "(?:" + representWord(word) + wrapAsPlaceHolder(lineObject.afterChar) + ")"
        }
    });

    return beforeStringPattern.map(function (pattern) {
        return {
            "pattern": pattern,
            "expected": "$1" + replaceMatchedValue(lineObject.afterField) + "$2"
        }
    });
}
function lineParse(line) {
    if (line.length === 0) {
        return;
    }
    // コメントアウトされている場合は無視する
    if (line[0] === "#") {
        return;
    }
    /*
    コメントがある場合
     */
    var commentRegexp = /<(.*?)>\s*?$/;
    var commentField = null;
    var removedComment = line.replace(commentRegexp, function (all, comment) {
        commentField = comment;
        return "";
    });
    var fields = removedComment.split("\t");
    /*
    前置文字,後置文字,オプション
     */
    var optionalFields = [];
    if (fields[2] != null) {
        if (fields[2].indexOf(",") === -1) {
            optionalFields = [fields[2]];
        } else {
            optionalFields = fields[2].split(",");
        }
    }
    var beforeChar = (function () {
        var withoutSpace = /\S/;
        var field = optionalFields[0];
        if (field != null && withoutSpace.test(field)) {
            return field.trim()
        } else {
            return null;
        }
    })();
    var afterChar = (function () {
        var withoutSpace = /\S/;
        var field = optionalFields[1];
        if (field != null && withoutSpace.test(field)) {
            return field.trim()
        } else {
            return null;
        }
    })();
    var hasRegExpOption = optionalFields[2] === "RE";
    var beforeField = fields[1] ? fields[1].trim() : null;
    var afterField = fields[0] ? fields[0].trim() : null;
    var lineObject = {
        // 変更前単語
        beforeField: beforeField,
        // | で区切った文字列
        beforeFieldWords: beforeField && beforeField.split("|"),
        // 変更後単語
        afterField: afterField,
        // 前置文字
        beforeChar: beforeChar,
        // 後置文字
        afterChar: afterChar,
        // RE オプションがついてるかどうか
        hasRegExpOption: hasRegExpOption,
        // コメント
        commentField: commentField
    };
    /*
    # なお、正解パターンだけ置く場合、WZ6以降ではそれ以外の記述があると機能しなくなる（コメントもだめ）
    # 「CakePHP<★cakephp★>」ではWZ6以降は機能しない
    => iオプションの正規表現を作成する
     */
    // 大文字小文字を補正するパターン
    if (beforeField === null && afterField) {
        return patternForBeforeFieldOnly(lineObject);
    }
    // 変更前単語 + 変更後単語
    if (beforeChar === null && afterChar === null) {
        return patternForBothField(lineObject);
    }
    // 前置文字 + 後置文字があるパターン
    if (beforeChar !== null && afterChar !== null) {
        return patternForBothChar(lineObject);
    } else {
        // 前置文字 or 後置文字のパターン
        return patternForRatherChar(lineObject);
    }

}
function isNotEmpty(object) {
    return object != null;
}
function flatten(array) {
    return Array.prototype.concat.apply([], array);
}
function parse(content) {
    var contentByLine = content.split("\n");
    return flatten(contentByLine.map(function (line) {
        try {
            return lineParse(line);
        } catch (error) {
            console.error(error);
        }
    }).filter(isNotEmpty));
}

module.exports.parse = parse;
module.exports.lineParse = lineParse;