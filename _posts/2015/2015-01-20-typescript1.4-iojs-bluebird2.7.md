---
title: "2015-01-20のJS: TypeScript 1.4、io.js 1.0、bluebird 2.7のglobal rejection events"
author: azu
layout: post
date : 2015-01-20T22:24
category: JSer
tags:
    - TypeScript
    - Node.js
    - io.js
    - Promise
    - library

---

JSer.info #211 - [TypeScript 1.4](http://blogs.msdn.com/b/typescript/archive/2015/01/16/announcing-typescript-1-4.aspx "TypeScript 1.4")がリリースされました。

以前[TypeScript and the Road to 2.0 - TypeScript - Site Home - MSDN Blogs](http://blogs.msdn.com/b/typescript/archive/2014/10/22/typescript-and-the-road-to-2-0.aspx "TypeScript and the Road to 2.0 - TypeScript - Site Home - MSDN Blogs")のロードマップで書かれていたように、Union Types、Type Aliases、Const Enumsの追加など機能が追加されています。

ES6の構文サポートの改善、ES6のコードを出力するモードも追加されていて詳しくは以下を見るといいです。

- [TypeScript 1.4.1 変更点 - Qiita](http://qiita.com/vvakame/items/69efc1c6a3b91876330d "TypeScript 1.4.1 変更点 - Qiita")

また、TypeScriptの[Compiler API](https://github.com/Microsoft/TypeScript/wiki/Using-the-Compiler-API "Compiler API")についてのドキュメントが加筆されています。

----

Node.jsのforkである[io.js](https://iojs.org/ "io.js")の1.0.0がリリースされました。

[io.js - FAQ](https://iojs.org/faq.html "io.js - FAQ")にも書かれていますが、semverなのでNode.jsからのメジャーアップデートという意味で1.0なので、production-readyだから1.0という意味ではないです。

[JSer.info 4周年 - JSer.info](http://jser.info/2015/01/16/4-years/ "JSer.info 4周年 - JSer.info")でも少し書いていましたが、オープンガバナンスモデルを元に予測可能なリリースサイクルの提供を目的としていて、これにより新しい技術([ES6](https://iojs.org/es6.html "ES6")への対応)などを取り入れやすく等が主な目的としてあります。

----

Promiseの実装ライブラリである[bluebird](https://github.com/petkaantonov/bluebird "bluebird") [v2.7.0](https://github.com/petkaantonov/bluebird/releases/tag/v2.7.0 "v2.7.0")がリリースされました。([v2.8.0](https://github.com/petkaantonov/bluebird/releases/tag/v2.8.0 "v2.8.0")まででています)

大きな機能として[Global rejection events](https://github.com/petkaantonov/bluebird/blob/master/API.md#global-rejection-events "Global rejection events")が追加されました。

これは、グローバルにイベントを登録しておくと[unhandled rejection](http://azu.github.io/promises-book/#promise-done "unhandled rejection")(`.catch`等でエラー処理を行わない場合にエラーが握りつぶされてしまう現象)をキャッチすることができるようになっています。

```js
process.on("unhandledRejection", function(reason, promise) {
    // See Promise.onPossiblyUnhandledRejection for parameter documentation
});

process.on("rejectionHandled", function(promise) {
    // See Promise.onUnhandledRejectionHandled for parameter documentation
});
```

これに類似する機能は仕様としても議論されていて、以下にまとめられています。

- [[whatwg] An API for unhandled promise rejections from Domenic Denicola on 2014-09-12 (public-whatwg-archive@w3.org from September 2014)](https://lists.w3.org/Archives/Public/public-whatwg-archive/2014Sep/0024.html "[whatwg] An API for unhandled promise rejections from Domenic Denicola on 2014-09-12 (public-whatwg-archive@w3.org from September 2014)")
- [Promise unhandled rejection tracking global handler hook](https://gist.github.com/benjamingr/0237932cee84712951a2 "Promise unhandled rejection tracking global handler hook")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Socket.IO — Socket.IO 1.3.0
[socket.io/blog/socket-io-1-3-0/](http://socket.io/blog/socket-io-1-3-0/ "Socket.IO — Socket.IO 1.3.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Socket.IO 1.3.0リリース。

----

## harmony:specification_drafts [ES Wiki]
[wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#january_15_2015_draft_rev_31](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#january_15_2015_draft_rev_31 "harmony:specification\_drafts \[ES Wiki\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 6のDraft Rev 31リリース。
議論検討する`super()`についての記述の変更が中心

- [ecma262/ES6-super-construct=proposal.md at master · tc39/ecma262](https://github.com/tc39/ecma262/blob/master/workingdocs/ES6-super-construct%3Dproposal.md "ecma262/ES6-super-construct=proposal.md at master · tc39/ecma262")

----

## ESLint 0.12.0 released - ESLint
[eslint.org/blog/2015/01/eslint-0.12.0-released/](http://eslint.org/blog/2015/01/eslint-0.12.0-released/ "ESLint 0.12.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint  0.12.0リリース。
ES6の一部をサポート、JSXのフルサポート。
それに併せてルールがJSXでも動くように修正等

----

## Release 1.17.0 · jquery/qunit
[github.com/jquery/qunit/releases/tag/1.17.0](https://github.com/jquery/qunit/releases/tag/1.17.0 "Release 1.17.0 · jquery/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 1.17.0リリース。
HTMLレポータの改善。

----

## Announcing TypeScript 1.4 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/01/16/announcing-typescript-1-4.aspx](http://blogs.msdn.com/b/typescript/archive/2015/01/16/announcing-typescript-1-4.aspx "Announcing TypeScript 1.4 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.4リリース。
Union Types、Type Aliases、Const Enumsの追加。
ES6の構文サポートの改善、ES6のコードを出力するモードの追加等

- [TypeScript 1.4.1 変更点 - Qiita](http://qiita.com/vvakame/items/69efc1c6a3b91876330d "TypeScript 1.4.1 変更点 - Qiita")

----

## io.js/CHANGELOG.md at v1.x · iojs/io.js
[github.com/iojs/io.js/blob/v1.x/CHANGELOG.md#2015-01-14-version-101](https://github.com/iojs/io.js/blob/v1.x/CHANGELOG.md#2015-01-14-version-101 "io.js/CHANGELOG.md at v1.x · iojs/io.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのforkであるio.js 1.0リリース。

- [IO.js Overview](http://blog.risingstack.com/iojs-overview/ "IO.js Overview")
- [io.js-v1.0.0のリリースによせて - ぼちぼち日記](http://d.hatena.ne.jp/jovi0608/20150115/1421312947 "io.js-v1.0.0のリリースによせて - ぼちぼち日記")
- [io.jsについて知っていること - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2014/12/25/104300 "io.jsについて知っていること - from scratch")

----

## Release v2.7.0 · petkaantonov/bluebird
[github.com/petkaantonov/bluebird/releases/tag/v2.7.0](https://github.com/petkaantonov/bluebird/releases/tag/v2.7.0 "Release v2.7.0 · petkaantonov/bluebird")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

bluebird 2.7.0リリース。
`process.on("unhandledRejection", fn)` という感じでグローバルにunhandled Rejectionをキャッチ出来るイベントを登録できるように。

- [Promise unhandled rejection tracking global handler hook](https://gist.github.com/benjamingr/0237932cee84712951a2 "Promise unhandled rejection tracking global handler hook")
- [\[whatwg\] An API for unhandled promise rejections from Domenic Denicola on 2014-09-12 (public-whatwg-archive@w3.org from September 2014)](http://lists.w3.org/Archives/Public/public-whatwg-archive/2014Sep/0024.html "\[whatwg\] An API for unhandled promise rejections from Domenic Denicola on 2014-09-12 (public-whatwg-archive@w3.org from September 2014)")

----

## Release v1.10.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v1.10.0](https://github.com/jscs-dev/node-jscs/releases/tag/v1.10.0 "Release v1.10.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptコードスタイルチェックツール jscs 1.10.0リリース。

----

## Release 5.0 “Pravda vítězí” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/5.0.0](https://github.com/postcss/autoprefixer/releases/tag/5.0.0 "Release 5.0 “Pravda vítězí” · postcss/autoprefixer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

autoprefixer 5.0リリース。
PostCSS 4.0とBrowserslistを使用するように、`object-fit`やCSS Shapesなどの新しいプロパティに対応

----
<h1 class="site-genre">アーティクル</h1>

----

## ServiceWorker を使った XHR のモックテスト - Block Rockin’ Codes
[jxck.hatenablog.com/entry/response-injection](http://jxck.hatenablog.com/entry/response-injection "ServiceWorker を使った XHR のモックテスト - Block Rockin’ Codes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ServiceWorker</span></p>

ServiceWorkerを使ったXHRのモック。
`onfetch`に登録すれば、XHR等のリクエストに対してhookができるので、事前に定義しておいたレスポンスを返すようにする。
ServiceWorkerの登録プロセスについて

----

## What&#x27;s new in CSS Selectors 4 | grack
[grack.com/blog/2015/01/11/css-selectors-4/](https://grack.com/blog/2015/01/11/css-selectors-4/ "What&#x27;s new in CSS Selectors 4 | grack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSS Selectors Level 4で追加された要素についての紹介

----

## embona – ブラウザで動くBonanzaを作ってみた(その1) » nmi.jp
[nmi.jp/archives/763](http://nmi.jp/archives/763 "embona – ブラウザで動くBonanzaを作ってみた(その1) » nmi.jp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Emscriptenを使って将棋プログラムを移植するまでの流れ。
ヒープメモリ不足、ファイルの読み込み、デバッグ方法、標準入出力の扱い、Asyncifyでのメインループ処理など

----
<h1 class="site-genre">サイト、サービス</h1>

----

## VersionEye - Notification System for Software Packages
[www.versioneye.com/](https://www.versioneye.com/ "VersionEye - Notification System for Software Packages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">package</span> <span class="jser-tag">webservice</span></p>

npmやgem等色々な言語のライブラリの更新チェック、依存関係のチェック等が出来るサービス。
ファイルアップロードとかAPI等もある。
パッケージをフォローしてRSSで見たりできる

- [Continuous Updating // Speaker Deck](https://speakerdeck.com/reiz/continuous-updating "Continuous Updating // Speaker Deck")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Esperanto demo
[esperantojs.org/](http://esperantojs.org/ "Esperanto demo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

ES6 modulesのコードをCommonJS、AMD、UMDに変換するコマンドラインツール。Nodeモジュールとしても利用できる。

----

## fdecampredon/rx-flux
[github.com/fdecampredon/rx-flux](https://github.com/fdecampredon/rx-flux "fdecampredon/rx-flux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

RxJSベースのFluxアーキテクチャの実装ライブラリ

----

## RubaXa/Sortable
[github.com/RubaXa/Sortable](https://github.com/RubaXa/Sortable "RubaXa/Sortable")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

D&Dで要素を動かせるsortableライブラリ。
jQuery等の依存がないライブラリ

----

## ECharts · Home
[ecomfe.github.io/echarts/index-en.html](http://ecomfe.github.io/echarts/index-en.html "ECharts · Home")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">library</span></p>

Baidu EFEのグラフライブラリ。
種類が豊富に用意されていて、Canvasを管理するのにZRenderというライブラリを使っている

- [ZRender](http://ecomfe.github.io/zrender/ "ZRender")

----

## winterbe/streamjs
[github.com/winterbe/streamjs](https://github.com/winterbe/streamjs "winterbe/streamjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Java</span> <span class="jser-tag">library</span></p>

Java 8 Streams APIをインスパイアなStreamライブラリ

----

## eventualbuddha/decaffeinate
[github.com/eventualbuddha/decaffeinate](https://github.com/eventualbuddha/decaffeinate "eventualbuddha/decaffeinate")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

CoffeeScript to ES6に変換するツール

----

## gobblejs/gobble
[github.com/gobblejs/gobble](https://github.com/gobblejs/gobble "gobblejs/gobble")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Grunt</span></p>

JavaScriptビルドツール。
Gruntはビルドツールではないため、Gruntと共存する形でも使える。
またデバッガビリティを優先して開発していて、pluginも変に複雑化しないように役割をシンプルにしてる

----

## ForbesLindesay/sync-request
[github.com/ForbesLindesay/sync-request](https://github.com/ForbesLindesay/sync-request "ForbesLindesay/sync-request")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span></p>

同期的なHTTPリクエストを行うライブラリ

----