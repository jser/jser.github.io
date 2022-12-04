---
title: "2015-07-28のJS: Chrome 45β、ES6チュートリアル、Chrome開発者ツール本"
author: azu
layout: post
date : 2015-07-28T23:11
category: JSer
tags:
    - Chrome
    - ES6
    - debug

---
JSer.info #238 - [Chrome 45 Beta](http://blog.chromium.org/2015/07/chrome-45-beta-new-es2015-features.html "Chrome 45 Beta")がリリースされました。

[Chromium Blog: Chrome 45 Beta: New ES2015 features, service worker improvements, and media controls](http://blog.chromium.org/2015/07/chrome-45-beta-new-es2015-features.html "Chromium Blog: Chrome 45 Beta: New ES2015 features, service worker improvements, and media controls")

Chrome 45ではArrow Functionや`Array.of`や`Array.from`、`Object.assign`等のES6の実装やService Workerの改善などが行われています。

またSMILやMediaStreamのlabel属性など古い仕様のものがdeprecatedとなったりしています。

- [MediaStream Deprecations — Web Updates](https://developers.google.com/web/updates/2015/07/mediastream-deprecations "MediaStream Deprecations — Web Updates")


----

[ECMAScript 6 Tutorial](http://ccoenraets.github.io/es6-tutorial/index.html "ECMAScript 6 Tutorial")というサイトでは、名前の通りES6をチュートリアルで機能別に学べるように作られています。

また別の[ECMAScript 6 Features - ALPROSYS](http://www.alprosys.com/es6/es6_features_ol.html "ECMAScript 6 Features - ALPROSYS")というスライドでは、ES6の機能毎の紹介やES5ではどのように書けるかなどがまとまっているので見てみるといいかもしれません。

-----

[Introduction | Down and Dirty with Chrome Developer Tools](http://blittle.github.io/chrome-dev-tools/ "Introduction | Down and Dirty with Chrome Developer Tools")というGitBookでできた電子書籍ではChromeの開発者ツールについて書かれています。

実際にChromeを使って開発者ツールを動かし機能を学べるような作りになっていて、細かい機能についても画像豊富に紹介しているため一度見てみると何か発見があるかもしれません。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 1.0.0 - 2015.07.22 · zloirock/core-js · GitHub
[github.com/zloirock/core-js/releases/tag/v1.0.0](https://github.com/zloirock/core-js/releases/tag/v1.0.0 "Release 1.0.0 - 2015.07.22 · zloirock/core-js · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Babelにも同梱されてるES5、ES6、ES.nextのpolyfillであるcore-js 1.0.0リリース。

- [Polyfill · Babel](https://babeljs.io/docs/usage/polyfill/ "Polyfill · Babel")

----

## Chromium Blog: Chrome 45 Beta: New ES2015 features, service worker improvements, and media controls
[blog.chromium.org/2015/07/chrome-45-beta-new-es2015-features.html](http://blog.chromium.org/2015/07/chrome-45-beta-new-es2015-features.html "Chromium Blog: Chrome 45 Beta: New ES2015 features, service worker improvements, and media controls")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 45 Betaリリース。
Arrow FunctionやObject.assignなどのサポート、Subresource Integrityのサポート、SVGアニメーションを行うSMILを非推奨に、Service WorkerからページへpostMessageしたときのメッセージ配送先オブジェクトの変更など

- [Subresource Integrity Sample](https://googlechrome.github.io/samples/subresource-integrity/index.html "Subresource Integrity Sample")

----

## Introducing TypeScript npm nightlies - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/07/27/introducing-typescript-nightlies.aspx](http://blogs.msdn.com/b/typescript/archive/2015/07/27/introducing-typescript-nightlies.aspx "Introducing TypeScript npm nightlies - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScriptのnightly buildが公開された。

`npm install -g typescript@next`

でインストールできるようになっている。

- [Create a 'publish-nightly' task in our Jakefile by DanielRosenwasser · Pull Request #3875 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/pull/3875 "Create a 'publish-nightly' task in our Jakefile by DanielRosenwasser · Pull Request #3875 · Microsoft/TypeScript")

----

## Release v0.9.0 · airportyh/testem
[github.com/airportyh/testem/releases/tag/v0.9.0](https://github.com/airportyh/testem/releases/tag/v0.9.0 "Release v0.9.0 · airportyh/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Test Runnerツールのtestem 0.9.0リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## Bringing automated testing to Microsoft Edge through WebDriver | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2015/07/23/bringing-automated-testing-to-microsoft-edge-through-webdriver/](http://blogs.windows.com/msedgedev/2015/07/23/bringing-automated-testing-to-microsoft-edge-through-webdriver/ "Bringing automated testing to Microsoft Edge through WebDriver | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">webdriver</span></p>

MSEdgeがWebDriverをサポート。
MicrosoftWebDriver serverが公開された。

----

## channikhabra/yarr
[github.com/channikhabra/yarr](https://github.com/channikhabra/yarr "channikhabra/yarr")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rss</span> <span class="jser-tag">tutorial</span></p>

クライアントのみで動くRSSリーダーを題材としたJavaScriptアプリのチュートリアル。
Babel、dexie、jQuery、Rx、virtual-domで作られている。
また、どういう手順で作成するのかというのをGit tagでバージョン毎に見られるようにして、それぞれのバージョン毎に解説が書かれている。

----

## jdalton/polyfill-guide
[github.com/jdalton/polyfill-guide](https://github.com/jdalton/polyfill-guide "jdalton/polyfill-guide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

polyfillの書き方のガイド

----

## Building Plugins for React Apps
[nylas.com/blog/react-plugins](https://nylas.com/blog/react-plugins "Building Plugins for React Apps")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">tutorial</span></p>

React Componentの独立性を保つにはどうするかという話
Store同士に複雑な依存があると大変なので中央で管理するOmniStoreという概念の導入、Componentがただのデータであることを利用したDIする仕組み、Componentの独立性を確保するパターンについて等

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ECMAScript 6 Features - ALPROSYS
[www.alprosys.com/es6/es6\_features\_ol.html](http://www.alprosys.com/es6/es6_features_ol.html "ECMAScript 6 Features - ALPROSYS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">チートシート</span></p>

ES6の新しい構文についてES3、5ではどのように書くことができたのかを比較しながら見られるチートシート的なスライド

----

## Chrome Tech Talk Night #8 レポート | 株式会社サイバーエージェント
[www.cyberagent.co.jp/techinfo_detail/id=10782](https://www.cyberagent.co.jp/techinfo_detail/id=10782 "Chrome Tech Talk Night #8 レポート | 株式会社サイバーエージェント")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">動画</span> <span class="jser-tag">イベント</span></p>

Chrome Tech Talk Night #8の動画とスライドまとめ

- [Chrome Tech Talk Night #8 - connpass](http://connpass.com/event/17312/ "Chrome Tech Talk Night #8 - connpass")

----

## ▶ TXJS 2015 Livestream - YouTube
[www.youtube.com/watch?v=6lEbk7xdlsQ](https://www.youtube.com/watch?v=6lEbk7xdlsQ "▶ TXJS 2015 Livestream - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span></p>

TXJS 2015の動画

- [Texas JavaScript Conference 2015 | TXJS](https://2015.texasjavascript.com/ "Texas JavaScript Conference 2015 | TXJS")
- [Texas JavaScript 2015 | Chris Missal&#x27;s Blog](https://lostechies.com/chrismissal/2015/07/27/texas-javascript-2015/ "Texas JavaScript 2015 | Chris Missal's Blog")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ECMAScript 6 Tutorial
[ccoenraets.github.io/es6-tutorial/index.html](http://ccoenraets.github.io/es6-tutorial/index.html "ECMAScript 6 Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

ES6について学ぶチュートリアルサイト。
それぞれの機能毎に学ぶ形式になってる。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## schteppe/p2.js
[github.com/schteppe/p2.js](https://github.com/schteppe/p2.js "schteppe/p2.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

2D物理エンジンライブラリ

----

## JavaScript engine for Internet of Things
[samsung.github.io/jerryscript/](http://samsung.github.io/jerryscript/ "JavaScript engine for Internet of Things")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

サムスンの組み込み向けJavaScriptエンジン。ファイルサイズが小さめでIoT向け。iotjsというNode.js的なフレームワークも作ってる。

- JerryScript : V8
- iotjs : Node.js

のような関係

- [Platform for Internet of Things with JavaScript](http://samsung.github.io/iotjs/ "Platform for Internet of Things with JavaScript")

----

## s-a/iron-node
[github.com/s-a/iron-node](https://github.com/s-a/iron-node "s-a/iron-node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

Node.js向けのJavaScriptデバッガ。
Chrome開発者ツールを使ってNode.jsのコードをデバッグ出来るツール

----

## horsey
[bevacqua.github.io/horsey/](http://bevacqua.github.io/horsey/ "horsey")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

テキスト入力時に候補データからサジェストするUIライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Introduction | Down and Dirty with Chrome Developer Tools
[blittle.github.io/chrome-dev-tools/](http://blittle.github.io/chrome-dev-tools/ "Introduction | Down and Dirty with Chrome Developer Tools")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">book</span></p>

Chrome開発者ツールのそれぞれの機能について解説してる電子書籍。
実際に動かして確認できるサンプルやGIFでの分かりやすい解説をされてる

----
