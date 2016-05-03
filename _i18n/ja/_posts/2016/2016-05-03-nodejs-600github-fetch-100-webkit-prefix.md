---
title: "2016-05-03のJS: Node.js 6.0.0、GitHub Fetch 1.0.0、-webkit- prefixのポリシー"
author: azu
layout: post
date : 2016-05-03T22:50
category: 
tags:
    - Node.js
    - Fetch
    - webkit 

---


JSer.info #277 - 

- [Node v6.0.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v6.0.0/)
- [Release Fetch 1.0.0 · github/fetch](https://github.com/github/fetch/releases/tag/v1.0.0)
- [Updating Our Prefixing Policy | WebKit](https://webkit.org/blog/6131/updating-our-prefixing-policy/)


----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v6.0.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.0.0/](https://nodejs.org/en/blog/release/v6.0.0/ "Node v6.0.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 6.0.0(LTS)リリース。
v8のアップデートを含むため、Native addonは`npm rebuid`での再ビルドが必要。
Buffer APIが新しくなり、古いAPIは非推奨へ、`worker.suicide`は`worker.exitedAfterDisconnect`に変更、`querystring.parse()`が返すオブジェクトは`Object.prototype`を継承しないようになるなど

- [Node.js v6.0 (Current) がリリースされました。 - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2016/04/27/110027 "Node.js v6.0 (Current) がリリースされました。 - from scratch")

----

## Chromium Blog: Chrome 51 Beta: Credential Management API and reducing the overhead of offscreen rendering
[blog.chromium.org/2016/04/chrome-51-beta-credential-management.html](http://blog.chromium.org/2016/04/chrome-51-beta-credential-management.html "Chromium Blog: Chrome 51 Beta: Credential Management API and reducing the overhead of offscreen rendering")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 51 Betaリリース。
Credential Management APIのサポート。
offscreenの場合、crosss originのframeにおいては`requestAnimationFrame()`が呼ばれないように、Intersection Observer 、`passive`イベントオプション、V8 5.1へのアップデートなど。

- [V8 JavaScript Engine: V8 Release 5.1](http://v8project.blogspot.jp/2016/04/v8-release-51.html "V8 JavaScript Engine: V8 Release 5.1")
- [IntersectionObserver/explainer.md at gh-pages · WICG/IntersectionObserver](https://github.com/WICG/IntersectionObserver/blob/gh-pages/explainer.md "IntersectionObserver/explainer.md at gh-pages · WICG/IntersectionObserver")
- [Throttling Blink&#x27;s rendering pipeline for hidden content](https://docs.google.com/document/d/1Dd4qi1b_iX-OCZpelvXxizjq6dDJ76XNtk37SZEoTYQ/pub "Throttling Blink&#x27;s rendering pipeline for hidden content")
- [Power usage impact of render pipeline throttling - Google ドキュメント](https://docs.google.com/document/d/1jMuvRYWptZfP5zpvWmPJPRL-iowtgBVX45rSvew0VH4/edit "Power usage impact of render pipeline throttling - Google ドキュメント")

----

## Release v6.8.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.8.0](https://github.com/babel/babel/releases/tag/v6.8.0 "Release v6.8.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.8.0リリース。
Babel自体がBabel 6でTranspileするようになり、runtimeが5に依存していた問題が修正された

----

## Release Fetch 1.0.0 · github/fetch
[github.com/github/fetch/releases/tag/v1.0.0](https://github.com/github/fetch/releases/tag/v1.0.0 "Release Fetch 1.0.0 · github/fetch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">htto</span> <span class="jser-tag">library</span></p>

Fetch APIのpolyfillであるGitHub Fetch 1.0.0リリース。
IE9のサポートを終了、`timeout`イベントをハンドルするように、`URLSearchParams`のサポートなど

----

## ESLint v2.9.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/04/eslint-v2.9.0-released](http://eslint.org/blog/2016/04/eslint-v2.9.0-released "ESLint v2.9.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.9.0リリース。
Autofix `--fix` オプションの改善。
今までは一度のパスで適応できないものは諦めていたが、複数回のパスで修正を適応を試みるようになった。

- [ESLint v2.9.0 - Qiita](http://qiita.com/mysticatea/items/1d377b67465664009ad5 "ESLint v2.9.0 - Qiita")

----

## Release SlimerJS 0.10.0 · laurentj/slimerjs
[github.com/laurentj/slimerjs/releases/tag/0.10.0](https://github.com/laurentj/slimerjs/releases/tag/0.10.0 "Release SlimerJS 0.10.0 · laurentj/slimerjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox版のPhantomJS APIの互換実装であるSlimerJS 0.10.0リリース。

----

## Release Notes for Safari Technology Preview 3 | WebKit
[webkit.org/blog/6143/release-notes-for-safari-technology-preview-3/](https://webkit.org/blog/6143/release-notes-for-safari-technology-preview-3/ "Release Notes for Safari Technology Preview 3 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 3リリース。
`Symbol.isConcatSpreadable`などのwell-known Symbol実装の追加、
`:host()`擬似クラス、IndexedDBが`Blob`をサポート、`Crypto`、CSP周りの仕様準拠度の向上など

----
<h1 class="site-genre">アーティクル</h1>

----

## Scroll-linked effects - Mozilla | MDN
[developer.mozilla.org/en-US/docs/Mozilla/Performance/Scroll-linked\_effects](https://developer.mozilla.org/en-US/docs/Mozilla/Performance/Scroll-linked_effects "Scroll-linked effects - Mozilla | MDN")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

`onscroll`にhookして同期的に位置を変更する処理に対しては警告メッセージが出るようになった。
その場合の対処法についてのドキュメント

- [スクロール連動位置合わせは非同期スクロールと相性が悪い場合があり、コンソールに警告が表示されます | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2016/scroll-linked-positioning-effects-may-not-work-well-with-async-scrolling-console-warns/ "スクロール連動位置合わせは非同期スクロールと相性が悪い場合があり、コンソールに警告が表示されます | Firefox サイト互換性情報")

----

## Announcing Vue.js 2.0 — The Vue Point — Medium
[medium.com/the-vue-point/announcing-vue-js-2-0-8af1bde7ab9](https://medium.com/the-vue-point/announcing-vue-js-2-0-8af1bde7ab9 "Announcing Vue.js 2.0 — The Vue Point — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

Vue.js 2.0のパブリックプレビュー版リリース。
SnabbdomベースのVirtua lDOM実装の追加など

- [paldepind/snabbdom: A virtual DOM library with focus on simplicity, modularity, powerful features and performance.](https://github.com/paldepind/snabbdom "paldepind/snabbdom: A virtual DOM library with focus on simplicity, modularity, powerful features and performance.")

----

## Updating Our Prefixing Policy | WebKit
[webkit.org/blog/6131/updating-our-prefixing-policy/](https://webkit.org/blog/6131/updating-our-prefixing-policy/ "Updating Our Prefixing Policy | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span></p>

Safari/WebKitは新しい機能などは今後Vendor prefixではなく、フラグのON/OFFを追加していくようにするポリシーの変更について。
`-webkit-` prefixがあまりに使われてしまい、後方互換性のためにprefixが標準仕様となってしまった歴史などもあるため

- [Feature Policy | WebKit](https://webkit.org/feature-policy/ "Feature Policy | WebKit")

----

## How to Make Your React Apps 15x Faster – ReactJS News
[reactjsnews.com/how-to-make-your-react-apps-10x-faster](https://reactjsnews.com/how-to-make-your-react-apps-10x-faster "How to Make Your React Apps 15x Faster – ReactJS News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">設定</span></p>

Reactはデバッグ向けのコードが大量に入っているため、production(`NODE_ENV=production`)ビルドや機械的に最適化できるBabelプラグインを導入するだけでも速度が大分変わるという話

- [thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.](https://github.com/thejameskyle/babel-react-optimize "thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.")

----

## V8 JavaScript Engine: ES6, ES7, and beyond
[v8project.blogspot.com/2016/04/es6-es7-and-beyond.html](http://v8project.blogspot.com/2016/04/es6-es7-and-beyond.html "V8 JavaScript Engine: ES6, ES7, and beyond")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8が既存のウェブとの互換性を持ちつつ次期ECMAScriptの仕様を実装しているかのプロセスについて。
ES6の実装が完了する前にドラフトバージョンを実装することで見つけられる後方互換性の問題がある話。
またECMAScriptという複雑な言語仕様のtest suiteであるtest262について。

----

## npmで同じライブラリの複数バージョンをインストールして使う方法 | Web Scratch
[efcl.info/2016/05/02/npm-package-mixed-multiple-versions-demo/](http://efcl.info/2016/05/02/npm-package-mixed-multiple-versions-demo/ "npmで同じライブラリの複数バージョンをインストールして使う方法 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tips</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>

一つのプロジェクト内に同名ライブラリの複数バージョンをインストールして扱う方法について

----

## A look at ES6 Maps - Barbarian Meets Coding
[www.barbarianmeetscoding.com/blog/2016/04/27/a-look-at-es6-maps](http://www.barbarianmeetscoding.com/blog/2016/04/27/a-look-at-es6-maps "A look at ES6 Maps - Barbarian Meets Coding")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Mapについての解説。
データ構造としてのMap、Iterableについて

----

## Turbocharged JavaScript refactoring with codemods — Airbnb Engineering &amp; Data Science — Medium
[medium.com/airbnb-engineering/turbocharged-javascript-refactoring-with-codemods-b0cae8b326b9](https://medium.com/airbnb-engineering/turbocharged-javascript-refactoring-with-codemods-b0cae8b326b9 "Turbocharged JavaScript refactoring with codemods — Airbnb Engineering & Data Science — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

codemodを使ったリファクタリングについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Almin.js | JavaScriptアーキテクチャ
[azu.github.io/slide/2016/child\_process\_sushi/almin-javascript-architecture.html](http://azu.github.io/slide/2016/child_process_sushi/almin-javascript-architecture.html "Almin.js | JavaScriptアーキテクチャ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

[Almin.js](https://github.com/almin/almin "Almin.js")の設計の概念的な話やパターンについて。
FluxやCQRSといったパターンにおいて、ドメインモデルをどうやったら考えて実装できるようになるかという話。

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Diffee Checker
[una.im/diffee/](http://una.im/diffee/ "Diffee Checker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS </span></p>

CSS blend modesを使いiframe同士の描画結果の差分を表示するデモ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Galooshi/import-js: A tool to simplify importing JS modules
[github.com/Galooshi/import-js](https://github.com/Galooshi/import-js "Galooshi/import-js: A tool to simplify importing JS modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">editor</span></p>

指定した関数名から、該当するモジュールのimport文を自動的に探索して追加できるツール。
各種エディタ連携などもある

----

## ericholiveira/studio: A nodejs framework to create decoupled and scalable applications
[github.com/ericholiveira/studio](https://github.com/ericholiveira/studio "ericholiveira/studio: A nodejs framework to create decoupled and scalable applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span></p>

ActorモデルインスパイアなNode.jsのフレームワーク

----

## flickr/yakbak: Record and playback HTTP responses
[github.com/flickr/yakbak](https://github.com/flickr/yakbak "flickr/yakbak: Record and playback HTTP responses")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

ProxyとしてHTTPリクエストとレスポンスを記録し、リプレイしたレスポンスを返すことができるNode.jsライブラリ

- [Introducing yakbak: Record and playback HTTP interactions in NodeJS | code.flickr.com](http://code.flickr.net/2016/04/25/introducing-yakbak-record-and-playback-http-interactions-in-nodejs/ "Introducing yakbak: Record and playback HTTP interactions in NodeJS | code.flickr.com")

----

## jeromeetienne/babel-plugin-jsdoced: babel plugin which use jsdoc to implement strong typing in javascript
[github.com/jeromeetienne/babel-plugin-jsdoced](https://github.com/jeromeetienne/babel-plugin-jsdoced "jeromeetienne/babel-plugin-jsdoced: babel plugin which use jsdoc to implement strong typing in javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JSDoc</span> <span class="jser-tag">plugin</span></p>

jsdoced.jsを使いJSDocからランタイムassertを追加するBabelプラグイン。
jsdoc-to-assertと似てるが、返り値のチェックやProxy APIを使ってプロパティの代入もチェックしている

- [jsdoced.js - test your code with jsdoc](http://jsdocedjs.org/ "jsdoced.js - test your code with jsdoc")
- [JSDocをランタイムassertに変換するBabelプラグインを書いた | Web Scratch](http://efcl.info/2016/03/25/jsdoc-to-assert/ "JSDocをランタイムassertに変換するBabelプラグインを書いた | Web Scratch")

----
