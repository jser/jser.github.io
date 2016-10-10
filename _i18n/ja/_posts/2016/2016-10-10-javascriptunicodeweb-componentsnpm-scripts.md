---
title: "2016-10-10: JavaScriptとUnicode、Web Components、npm-scripts"
author: azu
layout: post
date : 2016-10-10T23:11
category: JSer
tags:
    - Unicode
    - WebComponents
    - npm

---

JSer.info #300 - JSer.info 300回目です。
次の記事で、JSer.infoに最近追加した機能や変更点などをまとめてあります。

- [JSer.info 300回目 && https化 && ユーザー投稿機能](https://jser.info/2016/10/10/300posts/)

----

[What every JavaScript developer should know about Unicode](https://rainsoft.io/what-every-javascript-developer-should-know-about-unicode/ "What every JavaScript developer should know about Unicode")という記事では、JavaScriptとUnicodeに関する網羅的な解説がされています。

Unicodeにおける用語、Character、Code point、Plane、BMP、Code unit、サロゲートペア、Combing marks、エスケープシーケンス、文字列比較、Normalize、lengthの返す値、正規表現についてなど幅広い内容を扱っています。
また、ES2015から`String#normalize`メソッドや`String.fromCodePoint`と`String#codePointAt`の追加、IterableなどAPI的にも色々増えているので一度見てみるといいかもしれません。

----

[Web Components 2016 & Polymer v2](https://1000ch.github.io/slide/webcomponents-2016/ "Web Components 2016 &amp; Polymer v2")というスライドでは、ChromeやSafariなどに実装されているShadow DOM v1、Custom Elements v1について書かれています。
Web Componentsのライブラリとして有名なPolymer v2のロードマップや`is`属性についてなど最近のWeb Components周りの事情についてまとまっています。


----

[npm-scripts で Web フロントエンド開発を管理する – アカベコマイリ](http://akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/ "npm-scripts で Web フロントエンド開発を管理する – アカベコマイリ")という記事では、npm scripts(npm run-scripts)を使ったタスク処理について書かれています。
gulpなどのTask Runnerで行う処理をnpm run-scriptsで行う方法や利用するCLI、クロスプラットフォームに対応したタスクの書き方など幅広く書かれています。

また、npm run-scriptsで問題となる変数の扱いについても[cross-conf-env](http://akabeko.me/blog/2016/05/cross-conf-env-1-0-release/ "cross-conf-env")を使った方法などについても書かれています。


----
<h1 class="site-genre">ヘッドライン</h1>

----

## ECMAScript proposal updates @ 2016-10 | ECMAScript Daily
[ecmascript-daily.github.io/2016/10/02/proposals-updates](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2016年10月時点での、ECMAScript Proposalのステータスまとめ。 9月のミーティングで変更されたStageのまとめ

----

## jsdom/Changelog.md at 9.6.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.6.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.6.0/Changelog.md "jsdom/Changelog.md at 9.6.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.6.0リリース。
HTMLCollectionがiterableに対応など

----
<h1 class="site-genre">アーティクル</h1>

----

## What every JavaScript developer should know about Unicode
[rainsoft.io/what-every-javascript-developer-should-know-about-unicode/](https://rainsoft.io/what-every-javascript-developer-should-know-about-unicode/ "What every JavaScript developer should know about Unicode")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Unicode</span></p>

JavaScriptの文字列とUnicodeについて網羅的な解説。
Unicodeにおける用語、Character、Code point、Plane、BMP、Code unit、サロゲートペア、Combing marks、エスケープシーケンス、文字列比較、Normalize、length、正規表現について

----

## Progressive Web Apps with React.js: Part 2 — Page Load Performance – Medium
[medium.com/@addyosmani/progressive-web-apps-with-react-js-part-2-page-load-performance-33b932d97cf2](https://medium.com/@addyosmani/progressive-web-apps-with-react-js-part-2-page-load-performance-33b932d97cf2 "Progressive Web Apps with React.js: Part 2 — Page Load Performance – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span></p>

初期表示を早くするために、Routingごとにファイルとして分けて動的にロードする話。
webpackを使っての分割と読み込み、link preloadを使っての先読み、キャッシュについて

----

## JavaScriptライブラリ/プロジェクトのファイルサイズの問題点を見つける方法 - Qiita
[qiita.com/azu/items/7b54d614dc816780034a](http://qiita.com/azu/items/7b54d614dc816780034a "JavaScriptライブラリ/プロジェクトのファイルサイズの問題点を見つける方法 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Browserifyやwebpackなどでbundleしたファイルのサイズや依存モジュールのサイズなどを確認する方法について

----

## npm-scripts で Web フロントエンド開発を管理する – アカベコマイリ
[akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/](http://akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/ "npm-scripts で Web フロントエンド開発を管理する – アカベコマイリ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span></p>

npm run-scriptについて詳しく書かれた記事。
gulpなどのTask Runnerで行う典型的なユースケースをnpm run-scriptでやった場合にどうなるかや、クロスプラットフォームで動くツールについて書かれている。

----

## event.offsetX,Yの罠...どこが原点の座標値なのかを理解する (currentTargetとtarget) - Qiita
[qiita.com/yukiB/items/cc533fbbf3bb8372a924](http://qiita.com/yukiB/items/cc533fbbf3bb8372a924 "event.offsetX,Yの罠...どこが原点の座標値なのかを理解する (currentTargetとtarget) - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

targetとcurrentTargetの違い、offsetX/Y、screenX/Y、getBoundingClientRect()などについて

- [マウスイベントで取得されるカーソル座標パラメータの整理(offset, page, screen, client) - Qiita](http://qiita.com/yukiB/items/31a9e9e600dfb1f34f76 "マウスイベントで取得されるカーソル座標パラメータの整理(offset, page, screen, client) - Qiita")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Proper Error Handling // Speaker Deck
[speakerdeck.com/michelebertoli/proper-error-handling](https://speakerdeck.com/michelebertoli/proper-error-handling "Proper Error Handling // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

エラーハンドリング周りについてスライド。
何のためにするのか、手法やReactなどにおけるエラーハンドリングについて

----

## create-react-app-introduction // Speaker Deck
[speakerdeck.com/adwd/create-react-app-introduction](https://speakerdeck.com/adwd/create-react-app-introduction "create-react-app-introduction // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">スライド</span></p>

ReactのStarterKit的な`create-react-app`についての紹介

- [facebookincubator/create-react-app: Create React apps with no build configuration.](https://github.com/facebookincubator/create-react-app "facebookincubator/create-react-app: Create React apps with no build configuration.")

----

## Web Components 2016 &amp; Polymer v2
[1000ch.github.io/slide/webcomponents-2016/](https://1000ch.github.io/slide/webcomponents-2016/ "Web Components 2016 & Polymer v2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Web Componentsについてのスライド。
Shadow DOM v1、Custom Elements v1それぞれの変更点。
Polymer v2や`is`属性についてなど

----

## WebVR - virtual reality in your browsers // Speaker Deck
[speakerdeck.com/casarock/webvr-virtual-reality-in-your-browsers](https://speakerdeck.com/casarock/webvr-virtual-reality-in-your-browsers "WebVR - virtual reality in your browsers // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">VR</span></p>

VRの歴史やWebVR APIについてのスライド。
またWebVR APIを使ったユースケースの紹介

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## はてな教科書 JavaScript 編 · GitBook
[hatena.github.io/Hatena-Textbook-JavaScript/](https://hatena.github.io/Hatena-Textbook-JavaScript/ "はてな教科書 JavaScript 編 · GitBook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ebook</span></p>

JavaScriptの基本文法やDOM、Node.js、jQueryについてをざっと見ていく内容

- [はてなサマーインターン2016を終え、「はてな教科書」をアップデートしました - Hatena Developer Blog](http://developer.hatenastaff.com/entry/2016/10/05/160000 "はてなサマーインターン2016を終え、「はてな教科書」をアップデートしました - Hatena Developer Blog")
- [hatena/Hatena-Textbook-JavaScript: はてな研修用JavaScript教科書](https://github.com/hatena/Hatena-Textbook-JavaScript "hatena/Hatena-Textbook-JavaScript: はてな研修用JavaScript教科書")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## babel/babel-preset-env: WIP: Autoprefixer for Babel: target specific environments (browser, node, etc)
[github.com/babel/babel-preset-env](https://github.com/babel/babel-preset-env "babel/babel-preset-env: WIP: Autoprefixer for Babel: target specific environments (browser, node, etc)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

targetでブラウザやNode.jsのバージョンを指定することで、それに対応した最小限の変換を行うbabel preset

----

## DeNADev/wahid: A CreateJS-compatible library for games
[github.com/DeNADev/wahid](https://github.com/DeNADev/wahid "DeNADev/wahid: A CreateJS-compatible library for games")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

CreateJS互換の(モバイル)ゲーム向けライブラリ

- [CreateJS 互換ライブラリ wahid の開発 — Mobage Developers Blog](http://developers.mobage.jp/blog/createjs-wahid "CreateJS 互換ライブラリ wahid の開発 — Mobage Developers Blog")

----

## UI-Router
[ui-router.github.io/](https://ui-router.github.io/ "UI-Router")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

AngularとReactに対応したルータライブラリ

----

## Office UI Fabric
[dev.office.com/fabric](http://dev.office.com/fabric "Office UI Fabric")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">UI</span> <span class="jser-tag">React</span> <span class="jser-tag">AngularJS</span></p>

Office 365とかのUIコンポーネントを提供するライブラリ。
Vanilla JS、React、Angular、iOS版がある。

----
<h1 class="site-genre">書籍関係</h1>

----

## React Components - O&#x27;Reilly Media
[shop.oreilly.com/product/9781785889288.do](http://shop.oreilly.com/product/9781785889288.do "React Components - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React Componentについての書籍

----

## Manning | Functional Programming in JavaScript
[www.manning.com/books/functional-programming-in-javascript](https://www.manning.com/books/functional-programming-in-javascript "Manning | Functional Programming in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">book</span></p>

関数型プログラミングについての書籍
サンプルコードがES2015ベースで書かれている。

----

## JavaScript : Functional Programming for JavaScript Developers | PACKT Books
[www.packtpub.com/web-development/javascript-functional-programming-javascript-developers](https://www.packtpub.com/web-development/javascript-functional-programming-javascript-developers "JavaScript : Functional Programming for JavaScript Developers | PACKT Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptでの関数型プログラミングのパターン本

----
