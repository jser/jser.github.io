---
title: "2015-09-02のJS: MSEdgeとasm.js、単方向データフローのアーキテクチャ、CSS仕様書の読み方"
author: azu
layout: post
date : 2015-09-02T21:38
category: JSer
tags:
    - Flux
    - MVC
    - MSEdge
    - CSS
    - Spec

---

JSer.info #243 - Windows 10 [Build 10532](https://blogs.windows.com/bloggingwindows/2015/08/27/windows-10-insider-preview-build-10532-for-pc/ "Build 10532")が公開され付属するMSEdgeもアップデートされました。

Pointer Lock、Canvasの[blend modes](http://blogs.adobe.com/webplatform/2014/02/24/using-blend-modes-in-html-canvas/ "blend modes")の追加、ES6 Classes、asm.jsがデフォルト有効となり、DestructuringやES.nextの[Async Functions](https://github.com/tc39/ecmascript-asyncawait "Async Functions")が実験フラグ付きでサポートされました。

- [Microsoft Edge 10532](http://dev.modern.ie/platform/changelog/10532-pc/ "Microsoft Edge 10532")
- [Windows 10 Insider Preview Build 10532 for PC | Blogging Windows](https://blogs.windows.com/bloggingwindows/2015/08/27/windows-10-insider-preview-build-10532-for-pc/ "Windows 10 Insider Preview Build 10532 for PC | Blogging Windows")

また、オープンなメディアフォーマットを開発する[Alliance for Open Media](http://aomedia.org/ "Alliance for Open Media")にもMicrosoftが参加しているのと関係がありそうですが、MSEdgeにWebM/Opus/VP9を実装を予定しているようです。

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Oh, hai there open media formats! <a href="http://t.co/mdUgKyFvV0">http://t.co/mdUgKyFvV0</a> <a href="http://t.co/PT7srf6J4J">http://t.co/PT7srf6J4J</a> <a href="http://t.co/0tjhZipHaV">http://t.co/0tjhZipHaV</a></p>&mdash; Jacob Rossi (@jacobrossi) <a href="https://twitter.com/jacobrossi/status/638785221593288704">September 1, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

[André Staltz - Unidirectional User Interface Architectures](http://staltz.com/unidirectional-user-interface-architectures.html "André Staltz - Unidirectional User Interface Architectures")という記事では、Flux, Redux, Famous, Elm, Cycle.js それぞれのアーキテクチャについて簡潔にまとめられています。

それぞれがどういう構成要素で、単方向のデータフローを回しているかについて図と共に書かれているのでおすすめです。

Backbone.jsなどについて書かれた以下の記事も合わせてみると面白いかもしれません。

- [サバクラ両方で動く JavaScript の大規模開発を行うために](https://gist.github.com/tily/1362110 "サバクラ両方で動く JavaScript の大規模開発を行うために")

----

[基本の前の基礎知識 - Back to Basics CSS 2015-08-30](http://unformedbuilding.com/slide/back-to-basics-2015-08-30/#/ "基本の前の基礎知識 - Back to Basics CSS 2015-08-30")というスライドでは、CSSの仕様の読み方について解説されています。

仕様書はどこにあるのか、仕様書に出てくるCSSの基本構文の読み方、記号などの意味などについて詳しく書かれています。

CSSの仕様書を参照するときに合わせて読むと良さそうです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint v1.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/08/eslint-v1.3.0-released](http://eslint.org/blog/2015/08/eslint-v1.3.0-released "ESLint v1.3.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.3.0リリース。
`SourceCode`オブジェクトのAPIを追加、HTMLフォーマッターを追加、ルールの修正など

----

## V8 JavaScript Engine: V8 Release 4.6
[v8project.blogspot.com/2015/08/v8-release-46.html](http://v8project.blogspot.com/2015/08/v8-release-46.html "V8 JavaScript Engine: V8 Release 4.6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.6 リリース。
ES6の Spread operator、`new.target`の対応、TypedArrayの改善など

----

## Release v2.0.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v2.0.0](https://github.com/rackt/redux/releases/tag/v2.0.0 "Release v2.0.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Redux 2.0.0リリース。
Hot Reloadingのためだけにあった`getReducer()`を削除、`compose()`の動作を修正するなど

----

## mocha/HISTORY.md at master · mochajs/mocha
[github.com/mochajs/mocha/blob/master/HISTORY.md#230--2015-08-30](https://github.com/mochajs/mocha/blob/master/HISTORY.md#230--2015-08-30 "mocha/HISTORY.md at master · mochajs/mocha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 2.3.0リリース。 テストのエラーが起きた時に自動的にキャッチしないでスルーできる`--allowUncaught`の追加、非同期のテストのみ許可する`--async-only`でのPromiseの動作を修正

- [Added option to allow unhandled exceptions to propagate in the browser by amsul · Pull Request #1659 · mochajs/mocha](https://github.com/mochajs/mocha/pull/1659 "Added option to allow unhandled exceptions to propagate in the browser by amsul · Pull Request #1659 · mochajs/mocha")

----

## Release version 10532 [PC] : Microsoft Edge Dev
[dev.modern.ie/platform/changelog/10532-pc/](http://dev.modern.ie/platform/changelog/10532-pc/ "Release version 10532 \[PC\] : Microsoft Edge Dev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

Microsoft Edge 10532リリース。
Pointer Lock、Canvas blending modesのサポート、asm.jsとES6 Classesがデフォルトで有効に。
またAsync Function、Destructuringがフラグ付きで導入された

----

## jsdom/Changelog.md at 6.2.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/6.2.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/6.2.0/Changelog.md "jsdom/Changelog.md at 6.2.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 6.2.0リリース。
`Element.prototype.classList`のサポートやバグ修正

----

## Release v1.0.0: The first stable release (2015-08-26) · power-assert-js/power-assert
[github.com/power-assert-js/power-assert/releases/tag/v1.0.0](https://github.com/power-assert-js/power-assert/releases/tag/v1.0.0 "Release v1.0.0: The first stable release (2015-08-26) · power-assert-js/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

assertが失敗した時に表示する情報量を増やすpower-assert 1.0.0リリース。

----
<h1 class="site-genre">アーティクル</h1>

----

## André Staltz - Unidirectional User Interface Architectures
[staltz.com/unidirectional-user-interface-architectures.html](http://staltz.com/unidirectional-user-interface-architectures.html "André Staltz - Unidirectional User Interface Architectures")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

Flux, Redux, Famous, Elm, Cycle.js それぞれのアーキテクチャについてまとめた記事。
構成要素、データーフロー、特徴について簡潔にまとめられている

----

## Using requestIdleCallback — Google Web Updates
[developers.google.com/web/updates/2015/08/27/using-requestidlecallback](https://developers.google.com/web/updates/2015/08/27/using-requestidlecallback "Using requestIdleCallback — Google Web Updates")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span></p>

requestIdleCallbackについての解説。
Idleな期間に非同期でコールバックを呼び出す事ができ、第二引数で一定時間内には必ず呼び出す`timeout`を指定できる

----

## fizzbuzz
[ditam.github.io/posts/fizzbuzz.html](http://ditam.github.io/posts/fizzbuzz.html "fizzbuzz")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アルゴリズム</span></p>

JavaScriptで20種類のFizzBuzzの実装

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 基本の前の基礎知識 - Back to Basics CSS 2015-08-30
[unformedbuilding.com/slide/back-to-basics-2015-08-30/#/](http://unformedbuilding.com/slide/back-to-basics-2015-08-30/#/ "基本の前の基礎知識 - Back to Basics CSS 2015-08-30")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">spec</span> <span class="jser-tag">スライド</span></p>

CSSの仕様の読み方についてのスライド。
仕様に出てくる構文の読み方や単位についてまとめられている

----

## npm3 ❓ // Speaker Deck
[speakerdeck.com/watilde/npm3](https://speakerdeck.com/watilde/npm3 "npm3 ❓ // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">スライド</span></p>

npm3で追加された機能や変更点などについてのスライド

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Thimble by Mozilla - An online code editor for learners &amp; educators.
[thimble.mozilla.org/](https://thimble.mozilla.org/ "Thimble by Mozilla - An online code editor for learners & educators.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Mozilla</span> <span class="jser-tag">webservice</span> <span class="jser-tag">editor</span></p>

オンラインでウェブサイトを作れるサービス。
JSFiddle的なエディタ&プレビューとファイルツリー。
また、任意のファイルをアップロードできるのでHTMLで公開するのに便利そう

----

## mattdesl/promise-cookbook
[github.com/mattdesl/promise-cookbook](https://github.com/mattdesl/promise-cookbook "mattdesl/promise-cookbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">book</span></p>

Promiseの基本的な使い方、メソッドについて解説したCookbook

----

## JS.ORG | NEWS
[news.js.org/](http://news.js.org/ "JS.ORG | NEWS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

ユーザー投稿のJavaScriptニュースを扱うサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Izzimach/react-pixi
[github.com/Izzimach/react-pixi](https://github.com/Izzimach/react-pixi "Izzimach/react-pixi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

Reactを使ってPixi.jsのCanvasを操作するライブラリ

----

## mysticatea/npm-run-all
[github.com/mysticatea/npm-run-all](https://github.com/mysticatea/npm-run-all "mysticatea/npm-run-all")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm run-scriptで定義したものの並列実行や逐次実行等の補助を行うコマンドラインツール。
Nodeモジュールとしても利用できる

- [npm-run-all と concurrently を試す | アカベコマイリ](http://akabeko.me/blog/2015/08/npm-run-all-and-concurrently/ "npm-run-all と concurrently を試す | アカベコマイリ")

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: Reactive Programming with Rxjs: Untangle Your Asynchronous JavaScript Code: Sergi Mansilla
[www.amazon.com/dp/1680501291?tag=amazon0abac-22](http://www.amazon.com/dp/1680501291?tag=amazon0abac-22 "Amazon: Reactive Programming with Rxjs: Untangle Your Asynchronous JavaScript Code: Sergi Mansilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

2016年3月25日発売
RxJSでのリアクティブプログラミングについての書籍

----

## SurviveJS - Webpack and React
[survivejs.com/](http://survivejs.com/ "SurviveJS - Webpack and React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

WebpackとReactについての書籍

----
