---
title: "2016-04-26のJS: core-js 2.3.0、addEventListenerの第3引数、ウェブ関連仕様の翻訳"
author: azu
layout: post
date : 2016-04-26T20:25
category: JSer
tags:
    - ECMAScript
    - DOM
    - W3C
    - WHATWG
    - Spec
    - Translation

---


JSer.info #276 - 

----
<h1 class="site-genre">ヘッドライン</h1>

----

## New Release: 2.9.2
[jshint.com/blog/2016-04-19/release-2-9-2/](http://jshint.com/blog/2016-04-19/release-2-9-2/ "New Release: 2.9.2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.9.2リリース

----

## Release v3.5.0 · reactjs/redux
[github.com/reactjs/redux/releases/tag/v3.5.0](https://github.com/reactjs/redux/releases/tag/v3.5.0 "Release v3.5.0 · reactjs/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 3.5.0リリース
ES.nextのStage 1 Proposalであるes obvervableに対応。
`Symbol.observable`を実装を追加

----

## Release 2.3.0 - 2016.04.24 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v2.3.0](https://github.com/zloirock/core-js/releases/tag/v2.3.0 "Release 2.3.0 - 2016.04.24 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 2.3.0リリース。
`global.asap`、`Symbol.asyncIterator`、`Symbol.observable`の追加。
`Map#toJSON`、`Set#toJSON`、`Error.isError`の削除など。TC39ミーティング内容の反映が中心

- [tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/tree/master/es7/2016-03 "tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes")

----

## V8 JavaScript Engine: V8 Release 5.1
[v8project.blogspot.com/2016/04/v8-release-51.html](http://v8project.blogspot.com/2016/04/v8-release-51.html "V8 JavaScript Engine: V8 Release 5.1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.1リリース。
`Symbol.species`、`Symbol.hasInstance`、 Function nameの仕様追従、パフォーマンス/メモリ使用量の改善など

----

## Release Version 2.0.0 · chartjs/Chart.js
[github.com/chartjs/Chart.js/releases/tag/v2.0.0](https://github.com/chartjs/Chart.js/releases/tag/v2.0.0 "Release Version 2.0.0 · chartjs/Chart.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">canvas</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">library</span></p>

Canvasを使ったグラフライブラリのChart.js 2.0.0リリース。

----
<h1 class="site-genre">アーティクル</h1>

----

## DOM Listener: capture, passive, and once
[www.webreflection.co.uk/blog/2016/04/17/new-dom4-standards](https://www.webreflection.co.uk/blog/2016/04/17/new-dom4-standards "DOM Listener: capture, passive, and once")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span></p>

`node.addEventListener(type, handler, EventListenerOptions)` 第三引数に追加された`EventListenerOptions`について。
`passive`と`capture`の解説

----

## How do I update to Gulp 4? - Liquid Light
[www.liquidlight.co.uk/blog/article/how-do-i-update-to-gulp-4/](https://www.liquidlight.co.uk/blog/article/how-do-i-update-to-gulp-4/ "How do I update to Gulp 4? - Liquid Light")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span></p>

まだリリースはされてないが、gulp 4へのアップデートについて
どのようにアップデートすればいいかが書かれている

----

## Stylelint | CSS-Tricks
[css-tricks.com/stylelint/](https://css-tricks.com/stylelint/ "Stylelint | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSSのLintツールであるStylelintについて。
エディタとの連携、PostCSS、stylefmtについて

----

## emilbjorklund/svg-weirdness: A repository of bugs and plain weird behavior in SVG
[github.com/emilbjorklund/svg-weirdness](https://github.com/emilbjorklund/svg-weirdness "emilbjorklund/svg-weirdness: A repository of bugs and plain weird behavior in SVG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">browser</span> <span class="jser-tag">issue</span></p>

SVGのバグを集めたリポジトリ

----

## 中級者向け Service Worker Tutorial | blog.jxck.io
[blog.jxck.io/entries/2016-04-24/service-worker-tutorial.html](https://blog.jxck.io/entries/2016-04-24/service-worker-tutorial.html "中級者向け Service Worker Tutorial | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">動画 </span></p>

ServiceWorkerを使って開発する際に出てくる問題や挙動について解説しているスクリーンキャスト


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## EmberConf 2016 - YouTube
[www.youtube.com/playlist?list=PL4eq2DPpyBblc8aQAd516-jGMdAhEeUiW](https://www.youtube.com/playlist?list=PL4eq2DPpyBblc8aQAd516-jGMdAhEeUiW "EmberConf 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画 </span></p>

EmberConf 2016の動画まとめ

- [EmberConf 2016 - March 29 &amp; 30, Portland, OR.](http://emberconf.com/ "EmberConf 2016 - March 29 &amp; 30, Portland, OR.")

----

## Dev.Opera — Front-End Performance: The Dark Side
[dev.opera.com/blog/timing-attacks/](https://dev.opera.com/blog/timing-attacks/ "Dev.Opera — Front-End Performance: The Dark Side")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">動画 </span></p>

フロントエンドのパフォーマンスについての動画

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Flexbox Patterns
[www.flexboxpatterns.com/home](http://www.flexboxpatterns.com/home "Flexbox Patterns")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Flexboxのパターン集

----

## ウェブ関連仕様 日本語訳
[triple-underscore.github.io/](https://triple-underscore.github.io/ "ウェブ関連仕様 日本語訳")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">spec</span> <span class="jser-tag">翻訳</span></p>

WHATWGやW3Cなどの仕様書を翻訳しているサイト

----

## はじめてのプログレッシブ ウェブアプリ
[codelabs.developers.google.com/codelabs/your-first-pwapp-ja/](https://codelabs.developers.google.com/codelabs/your-first-pwapp-ja/ "はじめてのプログレッシブ ウェブアプリ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span></p>

プログレッシブウェブアプリについて学ぶチュートリアル

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## evcohen/eslint-plugin-jsx-a11y: Static AST checker for a11y rules on JSX elements.
[github.com/evcohen/eslint-plugin-jsx-a11y](https://github.com/evcohen/eslint-plugin-jsx-a11y "evcohen/eslint-plugin-jsx-a11y: Static AST checker for a11y rules on JSX elements.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">ESLint</span></p>

JSX要素のアクセシビリティをチェックするESLintルール

----

## VictorBjelkholm/autochecker: Test your JavaScript modules simultaneously in 32 different versions of NodeJS
[github.com/VictorBjelkholm/autochecker](https://github.com/VictorBjelkholm/autochecker "VictorBjelkholm/autochecker: Test your JavaScript modules simultaneously in 32 different versions of NodeJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span></p>

Node.jsの複数のバージョンでテストするツール。 matrix test

----

## staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript
[github.com/staltz/xstream](https://github.com/staltz/xstream "staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span></p>

Hot onlyなRxJSライクなStreamライブラリ。

- [André Staltz - Why we built xstream](http://staltz.com/why-we-built-xstream.html "André Staltz - Why we built xstream")

----

## jonathanewerner/webpack-validator: Validates your webpack config with Joi
[github.com/jonathanewerner/webpack-validator](https://github.com/jonathanewerner/webpack-validator "jonathanewerner/webpack-validator: Validates your webpack config with Joi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

webpackの設定ファイルのバリデーションツール

----

## webpack/memory-fs: A simple in-memory filesystem. Holds data in a javascript object.
[github.com/webpack/memory-fs](https://github.com/webpack/memory-fs "webpack/memory-fs: A simple in-memory filesystem. Holds data in a javascript object.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

memory上で読み書きするfsモジュール

----
