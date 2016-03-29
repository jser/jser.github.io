---
title: "2016-03-29のJS: Safari 9.1、Backbone.jsの近況、Web Performance API"
author: azu
layout: post
date : 2016-03-29T09:46
category: JSer
tags:
    - Safari
    - perf
    - backbone.js

---

JSer.info #272 - Backbone.js [1.3.2](http://backbonejs.org/#changelog "1.3.2")がリリースされていますが、
[The Sad State of the Backbone Ecosystem](http://benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/ "The Sad State of the Backbone Ecosystem")という記事では近年のBackbone.js周りのエコシステムについて書かれています。

Backbone.js本体のPulseや[Marionette.js](https://github.com/marionettejs/backbone.marionette/ "Marionette.js")、他の関連ライブラリの状況について書かれています。

[JavaScript情報ってなんだっけ?](http://azu.github.io/slide/2016/jser5years/javascript-information.html "JavaScript情報ってなんだっけ?")でもGitHubリポジトリのPulseを見ることで、状況はある程度分かるという話をしました。
Backbone.jsの場合は枯れているというのもありますが、これ以上大きな進化をするのが難しい状況にも見えます。

Backbone.jsを使っている人は状況を把握するのに読んでみると面白いかもしれません。

----

[Safari 9.1](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")がリリースされました。

- [Safari 9.1](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")
- [CSS Variables in WebKit | WebKit](https://webkit.org/blog/5989/css-variables-in-webkit/)
- [Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web](http://www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se)

Safari 9.1で使えるようになった機能について上記の記事では解説されています。
CSS Custom Properties、CSS Will-Change、`<picture>`要素、Fast Tapの対応など新しい機能も色々増えています。

----

[ブラウザのPerformance APIの話](http://www.slideshare.net/kawada_hiroshi/performance-api "ブラウザのPerformance APIの話")というスライドでは、ブラウザで利用できるパフォーマンス計測のAPIについて書かれています。

スライド内でも紹介されていますが、Timing APIについては[A Primer for Web Performance Timing APIs](https://w3c.github.io/perf-timing-primer/ "A Primer for Web Performance Timing APIs")というドキュメントによくまとめられています。

またパフォーマンス関連して、Google等が主導の[Accelerated Mobile Pages (AMP)](https://www.ampproject.org/ "Accelerated Mobile Pages (AMP)")に対抗して、[Content Performance Policy (CPP)](https://discourse.wicg.io/t/content-performance-policy/1380/1 "Content Performance Policy")の提案などがありました。

CPPはまだアイデアに近い話ですが、この話に加えてSandbox Policyという提案が[@igrigorik](https://github.com/igrigorik "igrigorik")から出されています。

- [Proposal: Sandbox Policy - HTML - WICG](https://discourse.wicg.io/t/proposal-sandbox-policy/1414 "Proposal: Sandbox Policy - HTML - WICG")

これは既存の`<iframe sandbox>`を拡張した概念(オプトイン、オプトアウトな違いはある)で、`document.write`を禁止するディレクティブの追加などが含まれています。

どの話も、開発側がある種サブセットのような制限を受け入れてより高速な表示などが出来るようにするためのルールを決めている形です。

パフォーマンスに興味がある人はこの辺も見てみると面白いかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Backbone.js
[backbonejs.org/](http://backbonejs.org/ "Backbone.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">ReleaseNote</span></p>

Backbone. 1.3.2リリース。
`findIndex`、`findLastIndex`の追加、`component.json`のサポートを終了

- [Remove component.json support? · Issue #2601 · marionettejs/backbone.marionette](https://github.com/marionettejs/backbone.marionette/issues/2601 "Remove component.json support? · Issue #2601 · marionettejs/backbone.marionette")

----

## Release v1.0.0 · mozilla/sweet.js
[github.com/mozilla/sweet.js/releases/tag/v1.0.0](https://github.com/mozilla/sweet.js/releases/tag/v1.0.0 "Release v1.0.0 · mozilla/sweet.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptにhygienic macrosを導入するsweet.js 1.0.0リリース。

- [Redesign by disnet · Pull Request #485 · mozilla/sweet.js](https://github.com/mozilla/sweet.js/pull/485 "Redesign by disnet · Pull Request #485 · mozilla/sweet.js")

----

## ESLint v2.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/03/eslint-v2.5.0-released](http://eslint.org/blog/2016/03/eslint-v2.5.0-released "ESLint v2.5.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.5.0リリース。
依存してるライブラリもESLintのパッケージに含めて配布できる`bundledDependencies`を利用するように、ルールの追加/修正など。

- [ESLint v2.5.0 - Qiita](http://qiita.com/mysticatea/items/7018ca26abfa7701debc "ESLint v2.5.0 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Safari 9.1
[developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari\_9\_1.html](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 9.1の変更点について。
`<picture>`要素のサポート、Web Inspectorの改善、Fast Tap、Canvasが`imageSmoothingQuality`プロパティ、CSS Custom Propertiesのサポートなど

----

## CSS Variables in WebKit | WebKit
[webkit.org/blog/5989/css-variables-in-webkit/](https://webkit.org/blog/5989/css-variables-in-webkit/ "CSS Variables in WebKit | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Safari 9.1でサポートされたCSS Custom Propertiesについての解説
`--name`で変数を定義し、CSS内から`var(--name)`で参照できる。
JavaScriptからも`getPropertyValue/setProperty`で読み書きができる

----

## Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web
[www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se](http://www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se "Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

iOS 9.3のSafariについて。
`<picture>`、Fast Tap、CSS Custom Properties、ダイアログの変更、`shrink-to-fit`、Remote Inspectorなど

----

## JSDocをランタイムassertに変換するBabelプラグインを書いた | Web Scratch
[efcl.info/2016/03/25/jsdoc-to-assert/](http://efcl.info/2016/03/25/jsdoc-to-assert/ "JSDocをランタイムassertに変換するBabelプラグインを書いた | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">babel</span></p>

JSDocをassertに変換するBabelプラグインについて。
JSDocの型をランタイムassertにすることで、定義されてる型と実際の値が一致しているかを検証できる

----

## Shadow DOM CSS Cheat Sheet
[robdodson.me/shadow-dom-css-cheat-sheet/](http://robdodson.me/shadow-dom-css-cheat-sheet/ "Shadow DOM CSS Cheat Sheet")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Shadown DOMのCSS(`:host`など)、CSS Custom Properties(`--var`)についてのチートシート

----

## Status of Static Typing in ECMAScript | ECMAScript Daily
[ecmascript-daily.github.io/pages/status-of-static-typing-in-ecmascript/](https://ecmascript-daily.github.io/pages/status-of-static-typing-in-ecmascript/ "Status of Static Typing in ECMAScript | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">まとめ</span></p>

ECMAScriptにおける静的型関連Proposalのステータスまとめ。

----

## Gordux.js - The redux pattern in vanilla.js
[k94n.com/gordux-js-the-redux-pattern-in-vanilla-js](https://k94n.com/gordux-js-the-redux-pattern-in-vanilla-js "Gordux.js - The redux pattern in vanilla.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span></p>

Reduxのようなデータフローを素のJavaScriptで実装してみるという話。
EventにはCustom Eventを使ってPub/Subを行っている

----

## The Sad State of the Backbone Ecosystem
[benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/](http://benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/ "The Sad State of the Backbone Ecosystem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span></p>

Backbone.jsのエコシステムのアクティビティについて。
Backbone.js本体やMarionette、関連するライブラリの状況についてまとめてる

----

## GitHub - benoitvallon/computer-science-in-javascript: Computer science reimplemented in JavaScript
[github.com/benoitvallon/computer-science-in-javascript](https://github.com/benoitvallon/computer-science-in-javascript "GitHub - benoitvallon/computer-science-in-javascript: Computer science reimplemented in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">algorithm</span></p>

JavaScriptでデータ構造やソートアルゴリズムの実装例

- [Data Structures in JavaScript posts - Ben&#x27;s Blog](http://blog.benoitvallon.com/category/data-structures-in-javascript/ "Data Structures in JavaScript posts - Ben&#x27;s Blog")

----

## Sinon Tutorial: JavaScript Testing with Mocks, Spies &amp; Stubs
[www.sitepoint.com/sinon-tutorial-javascript-testing-mocks-spies-stubs/](http://www.sitepoint.com/sinon-tutorial-javascript-testing-mocks-spies-stubs/ "Sinon Tutorial: JavaScript Testing with Mocks, Spies & Stubs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Sinon.jsを使ったテストについて。
Sinon.jsのmock, stub, spyについて

----

## Promise-based functions should not throw exceptions
[www.2ality.com/2016/03/promise-rejections-vs-exceptions.html](http://www.2ality.com/2016/03/promise-rejections-vs-exceptions.html "Promise-based functions should not throw exceptions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Promises</span></p>

Promiseをベースとしてるasync/awaitを見据えながら、Promiseを返す関数は例外を投げないで`reject`したPromiseオブジェクトを返すべきという話

- [JavaScript Promiseの本](http://azu.github.io/promises-book/#not-throw-use-reject "JavaScript Promiseの本")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ng-japan 2016 セッション資料まとめ - Qiita
[qiita.com/nyamogera/items/b83833d1e15a55d0bb66](http://qiita.com/nyamogera/items/b83833d1e15a55d0bb66 "ng-japan 2016 セッション資料まとめ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">イベント</span></p>

ng-japan 2016の動画とスライドまとめ

- [ng-japan - The Angular conference in Tokyo, Japan (2016/3/21)](http://ngjapan.org/ "ng-japan - The Angular conference in Tokyo, Japan (2016/3/21)")

----

## The Case for CSS Modules
[markdalgleish.github.io/presentation-the-case-for-css-modules/](http://markdalgleish.github.io/presentation-the-case-for-css-modules/ "The Case for CSS Modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span></p>

CSS Modulesについてのスライド

- [css-modules/css-modules: Documentation about css-modules](https://github.com/css-modules/css-modules "css-modules/css-modules: Documentation about css-modules")

----

## Fluent Conf 2016: Jeremy Fairbank - The rise of async JavaScript - YouTube
[www.youtube.com/watch?v=QtgR94Q2pt4](https://www.youtube.com/watch?v=QtgR94Q2pt4 "Fluent Conf 2016: Jeremy Fairbank - The rise of async JavaScript - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画 </span></p>

async/awaitがどのように動くのかをPromiseをベースとして解説してる。
エラーハンドリングの動作やasync functionがどのように動くのかを見ていく話

- [Fluent Conf: Rise of Async JavaScript // Speaker Deck](https://speakerdeck.com/jfairbank/fluent-conf-rise-of-async-javascript "Fluent Conf: Rise of Async JavaScript // Speaker Deck")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## A Primer for Web Performance Timing APIs
[w3c.github.io/perf-timing-primer/](https://w3c.github.io/perf-timing-primer/ "A Primer for Web Performance Timing APIs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">document</span></p>

Web Performance Timing APIの概要をまとめたドキュメント

- [ブラウザのPerformance APIの話](http://www.slideshare.net/kawada_hiroshi/performance-api "ブラウザのPerformance APIの話")

----

## WebpackBin
[www.webpackbin.com/](http://www.webpackbin.com/ "WebpackBin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webpack</span> <span class="jser-tag">webservice</span></p>

http://requirebin.com/ のwebpack版。
HTML/CSS/JavaScriptを書いて公開出来るサービス

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## GitHub - ozkxr/match: An JavaScript library to test JSON with some nice features.
[github.com/ozkxr/match](https://github.com/ozkxr/match "GitHub - ozkxr/match: An JavaScript library to test JSON with some nice features.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">JSON</span></p>

JSONなどのオブジェクトに対してpredicate関数の結果を使ったmatchライブラリ

----

## tusharmath/funjector: Dependency injection for functional paradigm
[github.com/tusharmath/funjector](https://github.com/tusharmath/funjector "tusharmath/funjector: Dependency injection for functional paradigm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

関数に対するDIライブラリ。
部分適応した関数を作り、それに対してinjectできる仕組みを提供する

----

## pmdartus/snapline: Unleash your screenshots stored in Chrome Devtool timeline files
[github.com/pmdartus/snapline](https://github.com/pmdartus/snapline "pmdartus/snapline: Unleash your screenshots stored in Chrome Devtool timeline files")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">画像</span></p>

Chrome開発者ツールのタイムラインをGIFアニメーション画像に変換出来るツール

----
<h1 class="site-genre">書籍関係</h1>

----

## Majesty Of… by Alex Kyriakidis et al. [Leanpub PDF/iPad/Kindle]
[leanpub.com/vuejs/](https://leanpub.com/vuejs/ "Majesty Of… by Alex Kyriakidis et al. \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Vue.jsについての書籍

- [hootlex/the-majesty-of-vuejs: educational](https://github.com/hootlex/the-majesty-of-vuejs "hootlex/the-majesty-of-vuejs: educational")

----
