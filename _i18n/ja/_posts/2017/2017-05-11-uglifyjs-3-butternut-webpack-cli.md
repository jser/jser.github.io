---
title: "2017-05-11のJS: UglifyJS 3、butternut、webpack-cli"
author: "azu"
layout: post
date : 2017-05-10T14:19:19.703Z
category: JSer
tags:
- UglifyJS
- webpack-cli
- webpack

---

JSer.info #330 - [UglifyJS](https://github.com/mishoo/UglifyJS2 "UglifyJS") [v3.0.0](https://github.com/mishoo/UglifyJS2/releases/tag/v3.0.0 "v3.0.0")がリリースされました。

> uglify-js@3.x has a new API and CLI and is not backwards compatible with uglify-js@2.x.
> -- https://github.com/mishoo/UglifyJS2

2.x系のAPIやオプションとは互換性のない変更が多く含まれています。
また、2.xではES2015+をサポートしていませんでしたが(パースができなかった)、[uglify-es](https://www.npmjs.com/package/uglify-es "uglify-es")というUglifyJS 3.x系と互換性のES2015をサポートしたバージョンが公開されています。

> @kzc: it's also alpha quality and chock-full-o-bugs. But it's an official package!
> -- https://github.com/Rich-Harris/butternut/issues/2

2.xから3への変更点やマイグレーションガイドが公開されてないことによりトラブルになっていますが、
[Change Log](https://gist.github.com/azu/80d9b2e5f6ee42b2e78b73610c9c6967 "Change Log")を簡単にまとめると次のような変更が含まれています。

- `--prefix`/`--lint`などの代替方法があるコマンドライン引数の削除
- `angular`オプション(`/* @ngInject /*`の対応)の削除
- オプションの`screw_ie8`が`ie8`へのリネームなど
- `minify()`から`fs`依存が取り除かれ、結果をASTとして吐き出せるように

など様々な変更が含まれています。

- [unify CLI & API under `minify()` by alexlamsl · Pull Request #1811 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/pull/1811 "unify CLI &amp; API under `minify()` by alexlamsl · Pull Request #1811 · mishoo/UglifyJS2")
- [drop `angular` by alexlamsl · Pull Request #1812 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/pull/1812 "drop `angular` by alexlamsl · Pull Request #1812 · mishoo/UglifyJS2")

詳細は次のIssueを参照してください。

- [What is backwards incompatible in 3.0? · Issue #1875 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/issues/1875 "What is backwards incompatible in 3.0? · Issue #1875 · mishoo/UglifyJS2")
- [Is there a migration guide, from version 2.x to 3.x? · Issue #1881 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/issues/1881 "Is there a migration guide, from version 2.x to 3.x? · Issue #1881 · mishoo/UglifyJS2")

----

[butternut](https://github.com/Rich-Harris/butternut "butternut")というminifierがα公開されました。
[rollup](https://github.com/rollup/rollup "rollup")や[svelte](https://github.com/sveltejs/svelte "svelte")の作者である@[Rich-Harris (Rich Harris)](https://github.com/Rich-Harris "Rich-Harris (Rich Harris)")によるもので、[buble](https://www.npmjs.com/package/buble "buble")と同じ高速なminifyが目的のツールです。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/mjackson">@mjackson</a> <a href="https://twitter.com/AdamRackis">@AdamRackis</a> it&#39;s fast for the same reason Bublé is fast — it doesn&#39;t manipulate AST and generate code, it edits code in place. Much less costly</p>&mdash; Rich Harris (@Rich_Harris) <a href="https://twitter.com/Rich_Harris/status/862067505774428160">May 9, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

コードをパースしてASTにし、そこからは[magic-string](https://github.com/Rich-Harris/magic-string "magic-string")を使い、直接圧縮したコードを吐いています。

> The traditional approach to minification is this: parse your source code into an abstract syntax tree (AST) using something like Acorn, manipulate the AST, and finally generate code from it.
> Butternut takes a different approach. It uses Acorn to generate an AST, but instead of steps 2 and 3 it then edits the code in place using magic-string — which is much less costly than AST manipulation and code generation.
> -- https://github.com/Rich-Harris/butternut#how

----

[Webpack CLI](https://github.com/webpack/webpack-cli "Webpack CLI")というwebpackのCLIツールが公開されました。

- [Announcing the new webpack CLI – webpack – Medium](https://medium.com/webpack/announcing-the-new-webpack-cli-75ce1d9b8663 "Announcing the new webpack CLI – webpack – Medium")

webpackのCLIを作り変えているもので、`init`や`migrate`などのサブコマンドが追加されています。
`migrate`サブコマンドではv1からv2への設定ファイルのマイグレーションができ、
`init`コマンドでは[Yeoman](http://yeoman.io/ "Yeoman")をベースにしたテンプレ生成を行うことができます。

- [webpack-cli/SCAFFOLDING.md at master · webpack/webpack-cli](https://github.com/webpack/webpack-cli/blob/master/SCAFFOLDING.md "webpack-cli/SCAFFOLDING.md at master · webpack/webpack-cli")

今後の予定として`webpack`のパッケージに統合されるため、将来的には`webpack`コマンドとして扱えます。

> The CLI is getting integrated into webpack soon, which means you will be using webpack init instead of webpack-cli init.

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 29 | WebKit
[webkit.org/blog/7532/release-notes-for-safari-technology-preview-29/](https://webkit.org/blog/7532/release-notes-for-safari-technology-preview-29/ "Release Notes for Safari Technology Preview 29 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">i18n</span></p>

Safari Technology Preview Release 29リリース。
`Intl.DateTimeFormat.prototype.formatToParts`の実装、Web InspectorのBreak Pointの改善、読み込める画像リソースのホワイトリスト化(psdファイルは不可)など


----

## Prepack · Partial evaluator for JavaScript
[prepack.io/](https://prepack.io/ "Prepack · Partial evaluator for JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのAOTコンパイラ。
BabylonでパースしたASTを元に実行できるinterpreterを持ち、その結果を用いてコードの最適化を行う目的のツール。


----

## Release v3.0.1 · mishoo/UglifyJS2
[github.com/mishoo/UglifyJS2/releases/tag/v3.0.1](https://github.com/mishoo/UglifyJS2/releases/tag/v3.0.1 "Release v3.0.1 · mishoo/UglifyJS2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

UglifyJS 3.0リリース。
`--prefix`や`angular`オプションなどの削除、`screw_ie8`が`ie8`にリネームなど様々な破壊的変更が含まれている。
`minify()`から`fs`依存が取り除かれ、結果をASTとして吐き出せるようになるなど

- [unify CLI &amp; API under \`minify()\` by alexlamsl · Pull Request #1811 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/pull/1811 "unify CLI &amp;amp; API under \&#x60;minify()\&#x60; by alexlamsl · Pull Request #1811 · mishoo/UglifyJS2")
- [drop \`angular\` by alexlamsl · Pull Request #1812 · mishoo/UglifyJS2](https://github.com/mishoo/UglifyJS2/pull/1812 "drop \&#x60;angular\&#x60; by alexlamsl · Pull Request #1812 · mishoo/UglifyJS2")
- [maybe https://github.com/mishoo/UglifyJS2/releases](https://gist.github.com/azu/80d9b2e5f6ee42b2e78b73610c9c6967 "maybe https://github.com/mishoo/UglifyJS2/releases")

----

## Jest 20: 💖 Delightful Testing & 🏃🏽 Multi-Project-Runner · Jest
[facebook.github.io/jest/blog/2017/05/06/jest-20-delightful-testing-multi-project-runner.html](https://facebook.github.io/jest/blog/2017/05/06/jest-20-delightful-testing-multi-project-runner.html "Jest 20: 💖 Delightful Testing & 🏃🏽 Multi-Project-Runner · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 20リリース。
プロジェクトをまたいでテストを実行できるように、`expect`でPromiseのサポートを改善、`expect.assertions(n)`の追加、Jasmineをforkして使うように、CIではSnapshotを自動的に保存しないようになるなど


----

## Announcing the new webpack CLI – webpack – Medium
[medium.com/webpack/announcing-the-new-webpack-cli-75ce1d9b8663](https://medium.com/webpack/announcing-the-new-webpack-cli-75ce1d9b8663 "Announcing the new webpack CLI – webpack – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

webpack-cliがリリースされた。
`init`と`migrate`サブコマンドがあり、v1からv2へのマイグレーションやscaffolding toolとして利用できる

- [webpack/webpack-cli: webpack CLI](https://github.com/webpack/webpack-cli "webpack/webpack-cli: webpack CLI")

----

## | TypeScript 2.3: The Sexy Default Type Argument | Blog | SitePen
[www.sitepen.com/blog/2017/05/09/typescript-2-3-the-sexy-default-type-argument/](https://www.sitepen.com/blog/2017/05/09/typescript-2-3-the-sexy-default-type-argument/ "| TypeScript 2.3: The Sexy Default Type Argument | Blog | SitePen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2.3で入ったDefault type argumentsとcheckJSについて


----

## Release 2.0.0 · socketio/socket.io
[github.com/socketio/socket.io/releases/tag/2.0.0](https://github.com/socketio/socket.io/releases/tag/2.0.0 "Release 2.0.0 · socketio/socket.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Socket.IO 2.0.0リリース。
uWebSocketsがデフォルトのwebsocketエンジンに、カスタムパーサを指定できるように、Engine.IOとSocket.IOのhandshakeをマージしてroundtripの削減など

- [uWebSockets/uWebSockets: Tiny WebSockets](https://github.com/uWebSockets/uWebSockets "uWebSockets/uWebSockets: Tiny WebSockets")
- [Try to load uws by default, fall back to ws by kapouer · Pull Request #459 · socketio/engine.io](https://github.com/socketio/engine.io/pull/459 "Try to load uws by default, fall back to ws by kapouer · Pull Request #459 · socketio/engine.io")

----

## Release Almin 0.12 · almin/almin
[github.com/almin/almin/releases/tag/almin%400.12.3](https://github.com/almin/almin/releases/tag/almin%400.12.3 "Release Almin 0.12 · almin/almin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Almin 0.12リリース。
デフォルトの`StoreGroup`を変更しType Safeとなるように、`Store#receivePayload`のライフサイクルの追加など。
マイグレーションツールで0.11から移行できる。

- [almin/migration-tools: Migration scripts for Almin.](https://github.com/almin/migration-tools "almin/migration-tools: Migration scripts for Almin.")

----

## Nest FINAL release is here! Node.js framework built on top of TypeScript | Kamil Mysliwiec
[kamilmysliwiec.com/nest-final-release-is-here-node-js-framework-built-top-of-typescript/](https://kamilmysliwiec.com/nest-final-release-is-here-node-js-framework-built-top-of-typescript/ "Nest FINAL release is here! Node.js framework built on top of TypeScript | Kamil Mysliwiec")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsのサーバフレームワークであるNest.jsについて


----

## Release v0.46.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.46.0](https://github.com/facebook/flow/releases/tag/v0.46.0 "Release v0.46.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow v0.46.0リリース。
strict arity checkの試験的実装など
`experimental.strict_call_arity=true`

- [Flow: A Static Type Checker for JavaScript](https://flow.org/blog/2017/05/07/Strict-Function-Call-Arity/ "Flow: A Static Type Checker for JavaScript")

----
<h1 class="site-genre">アーティクル</h1>

----

## CSS Variables — No, really! – Dev Channel – Medium
[medium.com/dev-channel/css-variables-no-really-76f8c91bd34e](https://medium.com/dev-channel/css-variables-no-really-76f8c91bd34e "CSS Variables — No, really! – Dev Channel – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

CSS Variableについての解説記事。
基本的な使い方やよくある質問について。
また、色や複数値の例、スコープやcalcとの組み合わせ、JavaScriptとの連携などについて書かれている。


----

## Build Yourself a Redux - The Zapier Engineering Blog - Zapier
[zapier.com/engineering/how-to-build-redux/](https://zapier.com/engineering/how-to-build-redux/ "Build Yourself a Redux - The Zapier Engineering Blog - Zapier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

Reduxを実装しながらReduxについて学ぶ記事。
Redux/middleware/React Reduxを実装している


----

## util.promisify が追加された - from scratch
[yosuke-furukawa.hatenablog.com/entry/2017/05/10/101752](http://yosuke-furukawa.hatenablog.com/entry/2017/05/10/101752 "util.promisify が追加された - from scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Promises</span></p>

Node.jsの`util.promisify`について。
コールバック関数を受け取るNode.jsのコアメソッドをPromiseを返すように変換するUtilメソッド。


----

## Refer to the spec: What is all that stuff at the top of the spec?
[rachelandrew.co.uk/archives/2017/04/24/refer-to-the-spec-what-is-all-that-stuff-at-the-top-of-the-spec/](https://rachelandrew.co.uk/archives/2017/04/24/refer-to-the-spec-what-is-all-that-stuff-at-the-top-of-the-spec/ "Refer to the spec: What is all that stuff at the top of the spec?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">spec</span> <span class="jser-tag">article</span></p>

CSSの仕様の読み方についての連載

- [Refer to the spec](https://rachelandrew.co.uk/archives/2017/04/11/refer-to-the-spec/ "Refer to the spec")

----

## ES6 Modules in Chrome Canary (M60+) – Dev Channel – Medium
[medium.com/dev-channel/es6-modules-in-chrome-canary-m60-ba588dfb8ab7](https://medium.com/dev-channel/es6-modules-in-chrome-canary-m60-ba588dfb8ab7 "ES6 Modules in Chrome Canary (M60+) – Dev Channel – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span></p>

ES modulesについて。 nonmodule属性とrollupを使って、未対応のブラウザと対応ブラウザでの配布方法の分岐について


----

## The :focus-within pseudo class | Ian Devlin
[www.iandevlin.com/blog/2017/04/css/the-focus-within-pseudo-class](https://www.iandevlin.com/blog/2017/04/css/the-focus-within-pseudo-class "The :focus-within pseudo class | Ian Devlin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

`:focus-within`擬似クラスについて。


----

## FuseBox 2.0 — The beast reborn – fusebox – Medium
[medium.com/fusebox/fusebox-2-0-the-beast-reborn-e4ec0443b782](https://medium.com/fusebox/fusebox-2-0-the-beast-reborn-e4ec0443b782 "FuseBox 2.0 — The beast reborn – fusebox – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">serverless</span></p>

FuseBox 2.0リリース。
Configuration APIの変更、メソッドチェインでAPIを書けるように、Code Splitting  APIを追加、プラグインの追加、ドキュメントの更新など


----

## Idiomatic Redux · Mark's Dev Blog
[blog.isquaredsoftware.com/series/idiomatic-redux/](http://blog.isquaredsoftware.com/series/idiomatic-redux/ "Idiomatic Redux · Mark's Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">article</span></p>

Reduxのパターンについての連載


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## An Introduction to Glimmer - Sessions by Pusher
[pusher.com/sessions/meetup/ember-london/an-introduction-to-glimmer](https://pusher.com/sessions/meetup/ember-london/an-introduction-to-glimmer "An Introduction to Glimmer - Sessions by Pusher")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

Glimmerの基本的な使い方について発表


----

## Asynchronous JavaScript with async/await - Course by @mariusschulz @eggheadio
[egghead.io/courses/asynchronous-javascript-with-async-await](https://egghead.io/courses/asynchronous-javascript-with-async-await "Asynchronous JavaScript with async/await - Course by @mariusschulz @eggheadio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">video</span> <span class="jser-tag">tutorial</span></p>

async/awaitについてのスクリーンキャスト。
基本的な使い方、Sequntially/Concurrently、エラーハンドリング/Proposalのasync iteratorについて


----

## Parsing JavaScript - better lazy than eager? - Google スライド
[docs.google.com/presentation/d/1b-ALt6W01nIxutFVFmXMOyd\_6ou\_6qqP6S0Prmb1iDs/present#slide&#x3D;id.p](https://docs.google.com/presentation/d/1b-ALt6W01nIxutFVFmXMOyd_6ou_6qqP6S0Prmb1iDs/present#slide&#x3D;id.p "Parsing JavaScript - better lazy than eager? - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">slide</span></p>

JavaScriptのパースについてのスライド。
パースとは何か、V8はどうやってパースしてるのか。
またウェブページのJavaScriptパースは全体の15-20％を占めるため、パース速度を改善するために開発者はどうするべきかについて。
開発者ツールや`chrome://tracing`でのパース時間の読み方について


----

## Testing Made Easy: Better, Faster, Stronger Unit Tests and Integration Tests - Sessions by Pusher
[pusher.com/sessions/meetup/js-monthly-london/testing-made-easy-better-faster-stronger-unit-tests-and-integration-tests](https://pusher.com/sessions/meetup/js-monthly-london/testing-made-easy-better-faster-stronger-unit-tests-and-integration-tests "Testing Made Easy: Better, Faster, Stronger Unit Tests and Integration Tests - Sessions by Pusher")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">video</span></p>

JavaScriptのテストについて。
JestやCypress、StoryBookなどのユニットテスト/E2Eテストについての動画


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## SpectorJS - Explore and Troubleshoot your WebGL scenes with ease
[spector.babylonjs.com/](http://spector.babylonjs.com/ "SpectorJS - Explore and Troubleshoot your WebGL scenes with ease")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">debug</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span></p>

WebGLのデバッグツール。


----

## ESBench
[esbench.com/](https://esbench.com/ "ESBench")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">webservice</span></p>

Babelで変換した結果を元にbenchmark.jsでマイクロベンチを取るサービス


----

## Web Hypertext Application Technology Working Group Working Mode
[whatwg.org/working-mode](https://whatwg.org/working-mode "Web Hypertext Application Technology Working Group Working Mode")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">document</span> <span class="jser-tag">spec</span></p>

WHATWG仕様の用語や仕様の追加/変更/削除のProcessについて書かれたドキュメント


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## pmq20/node-compiler: Compiling your Node.js application into a single executable with dynamic require and all fs.\* API support.
[github.com/pmq20/node-compiler](https://github.com/pmq20/node-compiler "pmq20/node-compiler: Compiling your Node.js application into a single executable with dynamic require and all fs.\* API support.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Node.jsのアプリを1つの実行バイナリにするツール。

- [Node.js Compiler: compiling your Node.js application into a single executable // Speaker Deck](https://speakerdeck.com/pmq20/node-dot-js-compiler-compiling-your-node-dot-js-application-into-a-single-executable "Node.js Compiler: compiling your Node.js application into a single executable // Speaker Deck")

----

## Rich-Harris/butternut: The fast, future-friendly minifier
[github.com/Rich-Harris/butternut](https://github.com/Rich-Harris/butternut "Rich-Harris/butternut: The fast, future-friendly minifier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

高速である程度良い圧縮を目的にしたminifyツール


----

## hshoff/vx: react + d3 = vx | visualization components
[github.com/hshoff/vx](https://github.com/hshoff/vx "hshoff/vx: react + d3 = vx | visualization components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">d3.js</span> <span class="jser-tag">library</span></p>

React + D3.jsのビジュアライズコンポーネントライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## 01alchemist/TurboScript: Super charged JavaScript / TypeScript for parallel programming which compiles to asm.js and WebAssembly
[github.com/01alchemist/TurboScript](https://github.com/01alchemist/TurboScript "01alchemist/TurboScript: Super charged JavaScript / TypeScript for parallel programming which compiles to asm.js and WebAssembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">asm.js</span> <span class="jser-tag">WebAssembly</span></p>

asm.js、wasmへの変換を目的にしたプログラミング言語。
TypeScriptに似たSyntaxで型情報を扱う。


----

## O'Reilly Japan - SVGエッセンシャルズ 第2版
[www.oreilly.co.jp/books/9784873117973/](https://www.oreilly.co.jp/books/9784873117973/ "O'Reilly Japan - SVGエッセンシャルズ 第2版")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">book</span></p>

2017年5月17日発売
SVG Essentials, 2nd Editionの翻訳本


----
