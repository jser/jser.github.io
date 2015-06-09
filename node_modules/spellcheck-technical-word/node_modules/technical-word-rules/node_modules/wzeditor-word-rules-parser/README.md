# wzeditor-word-rules-parser [![Build Status](https://travis-ci.org/azu/wzeditor-word-rules-parser.svg?branch=master)](https://travis-ci.org/azu/wzeditor-word-rules-parser)

[WZ EDITOR](http://www.wzsoft.jp/wz8/index.html "WZ EDITOR")の用語統一辞書のパーサーです。

[WEB+DB PRESS用語統一ルール](https://gist.github.com/inao/f55e8232e150aee918b9 "WEB+DB PRESS用語統一ルール")をパースできることを目的としています。

> \1\2ほう\3	([^使])([いくすたつのる])方([ぁ-んァ-ヶ])	,,RE<★い方が★☆使い方☆>

のような行ごとの辞書をJSONに変換します。

### 調査レポート

辞書の形式の仕様は公開されてないので、実行結果から推測して正規表現に落としています。

* [WZ Editor 用語統一ヘルプと分析](doc/wzeditor-rule.md)

## Installation

```sh
npm install wzeditor-word-rules-parser
```

## Usage

### Module

`wzeditor-rules-parser` をテキストコンテンツを渡す事でパースした結果を返してくれる。

``` js
var parser = require("wzeditor-rules-parser");
var content = fs.readFileSync(__dirname + "/../dictionary/WEB+DB PRESS用語統一ルール", "utf-8");
var result = parser.parse(content);
/*
[ { pattern: 'クッキー|\\bCOOKIE\\b|\\bcookie\\b',
    expected: 'Cookie' },
  { pattern: 'Web Socket', expected: 'WebSocket' },
  { pattern: '(?:([^/])ウェブ)|(?:ウェブ([^/\\+]))',
    expected: '$1Web$2' },
  { pattern: '(?:([^/])\\bWEB)|(?:WEB\\b([^/\\+]))',
    expected: '$1Web$2' },
  { pattern: '(?:([^/])ウェッブ)|(?:ウェッブ([^/\\+]))',
    expected: '$1Web$2' },
  { pattern: '\\bEmacs\\b', flag: 'i', expected: 'Emacs' },
  { pattern: 'Emacs([0-9])', expected: 'Emacs $1' },
  { pattern: '\\bEmacs Lisp\\b',
    flag: 'i',
    expected: 'Emacs Lisp' }
]
*/
```

それぞれのオブジェクトは以下のような意味を持つ

- `pattern` {String} : マッチする文字列
- `flag` {String} : マッチする文字列の正規表現で指定するフラグ
- `expected` {String} : マッチする文字列に対応している置換する文字列(正規表現のプレースホルダを含む)


```js
{
    "pattern" : "string",
    "flag" : "string | null",
    "expected": "string"
}
```

つまり、JavaScriptでは以下のようにすることで置換が可能になる。

```js
var matchWord = new Regexp(pattern, flag);
"置換対象の文字列".replace(matchWord, expected);
```


### CLI

```sh
wzeditor-word-rules-parser "dictionary/WEB+DB PRESS用語統一ルール"
```

とすることでパースしたJSONを返す事も出来ます。

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

MIT