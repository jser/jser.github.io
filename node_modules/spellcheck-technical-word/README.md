# spellcheck-technical-word [![Build Status](https://travis-ci.org/azu/spellcheck-technical-word.svg?branch=master)](https://travis-ci.org/azu/spellcheck-technical-word)

This library provide check function of [azu/technical-word-rules](https://github.com/azu/technical-word-rules "azu/technical-word-rules").

## Installation

    npm install spellcheck-technical-word

## Usage

```js
var spellcheck = require("spellcheck-technical-word").spellCheckText;
var results = spellcheck("git");
assert(results.length > 0);
var result = results.pop();
/*
{ actual: 'git', expected: 'Git', paddingLine: 0, paddingColumn:0 }
*/
```

**Result data structure**

```js
/**
 *
 * @typedef {{actual: string, expected: string, paddingLine: number, paddingColumn: number}} SpellCheckResult
 */
var result = {
    actual: "string",
    expected: "string,
    paddingLine: 0,// start with 0
    paddingColumn: 0// start with 0
};
```


Use case: [azu/textlint-rule-helper](https://github.com/azu/textlint-rule-helper "azu/textlint-rule-helper")

## Tests

    npm test

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

MIT