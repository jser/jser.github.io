---
title: "2016-02-15のJS; Grunt 1.0.0 RC1、ESLint 2.0.0、Underscore/Lodash"
author: azu
layout: post
date : 2016-02-15T20:07
category: JSer
tags:
    - JavaScript
    - Grunt
    - ESLint
    - underscore
    - lodash
    - Vanilla

---


JSer.info #266

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release 2.1.0 - 2016.02.09 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v2.1.0](https://github.com/zloirock/core-js/releases/tag/v2.1.0 "Release 2.1.0 - 2016.02.09 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 2.1.0リリース。
ES5 polyfillの分離。
`Reflect.enumerate`の削除、Metadata Reflection APIの追加など

- [decorators/metadata.md at master · jonathandturner/decorators](https://github.com/jonathandturner/decorators/blob/master/specs/metadata.md "decorators/metadata.md at master · jonathandturner/decorators")

----

## February 2016 Security Release Summary | Node.js
[nodejs.org/en/blog/vulnerability/february-2016-security-releases/](https://nodejs.org/en/blog/vulnerability/february-2016-security-releases/ "February 2016 Security Release Summary | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">セキュリティ</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのセキュリティアップデート。
0.1x、4.x、5.xのアップデートがそれぞれ公開されている。

----

## Grunt 1.0.0 rc1 released - Grunt: The JavaScript Task Runner
[gruntjs.com/blog/2016-02-11-grunt-1.0.0-rc1-released](http://gruntjs.com/blog/2016-02-11-grunt-1.0.0-rc1-released "Grunt 1.0.0 rc1 released - Grunt: The JavaScript Task Runner")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Grunt</span> <span class="jser-tag">ReleaseNote</span></p>

Grunt 1.0.0 RC1リリース。
メジャーアップデートとなるため`peerDependencies`についての注意、`grant`モジュールにCLIが含まれるように、依存モジュールのアップデートなど

----

## ESLint v2.0.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/02/eslint-v2.0.0-released](http://eslint.org/blog/2016/02/eslint-v2.0.0-released "ESLint v2.0.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.0.0リリース。
`eslint --init`で既存コードから判定して利用するルールの設定を作為する機能の追加、`eslint:recommended`のアップデート、既存ルールの挙動変更やオプションの非互換な変更など

- [ESLint v2.0.0 の変更点まとめ - Qiita](http://qiita.com/mysticatea/items/8bcecd821cca9e849078 "ESLint v2.0.0 の変更点まとめ - Qiita")
- [Documentation - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/user-guide/migrating-to-2.0.0 "Documentation - ESLint - Pluggable JavaScript linter")

----

## StrongLoop | A New Day for Express!
[strongloop.com/strongblog/a-new-day-for-express/](https://strongloop.com/strongblog/a-new-day-for-express/ "StrongLoop | A New Day for Express!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">community</span></p>

expressがNode.js FoundationのTop-Level Projectとなり、strongloop(IBM)から  https://github.com/expressjs へ移管された。

- [TSC/Express.md at master · nodejs/TSC](https://github.com/nodejs/TSC/blob/master/Applications/Express.md "TSC/Express.md at master · nodejs/TSC")

----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing the Accessible Modal Dialog
[dev.edenspiekermann.com/2016/02/11/introducing-accessible-modal-dialog/](http://dev.edenspiekermann.com/2016/02/11/introducing-accessible-modal-dialog/ "Introducing the Accessible Modal Dialog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">library</span> <span class="jser-tag">WAI-ARIA</span></p>

AccessibleなモーダルUIライブラリ

----

## timaschew/postcss-compare-packs: compare most popular postcss packs like cssnext, rucksack and precss
[github.com/timaschew/postcss-compare-packs](https://github.com/timaschew/postcss-compare-packs "timaschew/postcss-compare-packs: compare most popular postcss packs like cssnext, rucksack and precss")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">PostCSS</span> <span class="jser-tag">まとめ</span></p>

cssnext、rucksack、precssなどのPostCSSパックの比較

----

## ECMAScript, TC39 Meeting Notesの読み方と修正方法 | Web Scratch
[efcl.info/2016/02/12/tc39-meeting-notes/](http://efcl.info/2016/02/12/tc39-meeting-notes/ "ECMAScript, TC39 Meeting Notesの読み方と修正方法 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ECMA TC39ミーティングノートの読み方とこのミーティングノートにはどういうことが書かれているのかについて

----

## cht8687/You-Dont-Need-Lodash-Underscore: Lists of Javascript methods which you can use natively
[github.com/cht8687/You-Dont-Need-Lodash-Underscore](https://github.com/cht8687/You-Dont-Need-Lodash-Underscore "cht8687/You-Dont-Need-Lodash-Underscore: Lists of Javascript methods which you can use natively")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

underscore/lodashのメソッドをネイティブで同じ表現をする書き方について

- [stevemao/You-Dont-Know-About-Lodash-Underscore: In response to You-Dont-Need-Lodash-Underscore](https://github.com/stevemao/You-Dont-Know-About-Lodash-Underscore "stevemao/You-Dont-Know-About-Lodash-Underscore: In response to You-Dont-Need-Lodash-Underscore")

----

## An update on strong mode - Google グループ
[groups.google.com/forum/#!msg/strengthen-js/ojj3TDxbHpQ/5ENNAiUzEgAJ](https://groups.google.com/forum/#!msg/strengthen-js/ojj3TDxbHpQ/5ENNAiUzEgAJ "An update on strong mode - Google グループ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8のstrong modeの実装ステータスや結果について。
性能が想定よりでなかった、ES6の仕様に性能のブロッカーがある。複雑になりすぎるなど。
そのため次期V8ではstrong modeのサポートは削除予定

----

## web-perf/react-worker-dom: Experiments to see the advantages of using Web Workers to Render React Virtual DOM
[github.com/web-perf/react-worker-dom](https://github.com/web-perf/react-worker-dom "web-perf/react-worker-dom: Experiments to see the advantages of using Web Workers to Render React Virtual DOM")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">React</span></p>

ReactをWebWorkerで動かす実装とデモ

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## AriaFallah/WebpackTutorial: A simple webpack tutorial
[github.com/AriaFallah/WebpackTutorial](https://github.com/AriaFallah/WebpackTutorial "AriaFallah/WebpackTutorial: A simple webpack tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpackのチュートリアル。
色々なパターンについて設定やなぜそう書くのかについて書かれてる

----

## React Newsletter
[reactjsnewsletter.com/](http://reactjsnewsletter.com/ "React Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">mail</span></p>

ReactのWeeklyメールマガジン

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## marten-de-vries/kneden: Transpile ES7 async/await to vanilla ES6 Promise chains: a Babel plugin
[github.com/marten-de-vries/kneden](https://github.com/marten-de-vries/kneden "marten-de-vries/kneden: Transpile ES7 async/await to vanilla ES6 Promise chains: a Babel plugin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">JavaScript</span></p>

async/awaitをPromiseを使ったreadableなコードへ変換する目的のBabelプラグイン

----

## ruyadorno/ntl: Npm Task List: Interactive cli menu to list/run npm tasks
[github.com/ruyadorno/ntl](https://github.com/ruyadorno/ntl "ruyadorno/ntl: Npm Task List: Interactive cli menu to list/run npm tasks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm run-scriptをインタラクティブに選択肢て実行出来るツール

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript glossary… by Andrea Giammarchi [PDF/iPad/Kindle]
[leanpub.com/jsglossary](https://leanpub.com/jsglossary "JavaScript glossary… by Andrea Giammarchi \[PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptを使った開発に出てくる用語を解説することを目的とした書籍

- [My new JavaScript book](https://www.webreflection.co.uk/blog/2016/02/08/jsglossary "My new JavaScript book")

----
