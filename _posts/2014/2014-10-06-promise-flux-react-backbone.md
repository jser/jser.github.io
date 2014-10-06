---
title: "2014-10-06のJS: localForage 1.0.0、Promises API、FluxとReact.jsとBackbone.js"
author: azu
layout: post
date : 2014-10-06T19:59
category: JSer
tags:
    - JavaScript
    - Promise
    - localstorage
    - Flux
    - React.js
    - Backbone.js

---

JSer.info #195 - IndexedDBやWebSQLやlocalStorage等をラップしたAPIを提供する[localForage](https://github.com/mozilla/localForage "localForage") 1.0.0がリリースされました。

localForageやPromiseベースのAPIとコールバックのAPIどちらでも利用でき、ストレージとしてどのバックエンドを使うかを選択出来る形をとっています。

IEに関する多くのバグ修正や古いブラウザ(Firefox4やChrome31以下)のサポートを終了したり、細かい改善が多く入っています。

詳しくは[CHANGELOG](https://github.com/mozilla/localForage/blob/1.0.1/CHANGELOG.md "CHANGELOG")を参照して下さい。

----

[ECMAScript 6 promises (2/2): the API](http://www.2ality.com/2014/10/es6-promises-api.html "ECMAScript 6 promises (2/2): the API")ではES6 Promisesについて詳しく解説されています。

[Part 1](http://www.2ality.com/2014/09/es6-promises-foundations.html "1")ではPromiseについては殆ど出ていませんでしたが(前置き的な非同期処理についてが主)、Part 2ではPromiseの大分部の機能や仕組みについて書かれています。

[JavaScript Promiseの本](http://azu.github.io/promises-book/ "JavaScript Promiseの本")は内容的に似ている部分も多いですが、Qの`done`や`finally`やブラウザのデバッガの対応等についても書かれているので、一緒に読むといい気がします。

----

[React Apps Using Flux and Backbone | Toptal](http://www.toptal.com/front-end/simple-data-flow-in-react-applications-using-flux-and-backbone "React Apps Using Flux and Backbone | Toptal") という記事では、[Fluxアーキテクチャ](http://facebook.github.io/react/docs/flux-overview.html "Flux Application Architecture ")について分かりやすく解説されています。。

[facebook/flux](https://github.com/facebook/flux "facebook/flux")と[React](http://facebook.github.io/react/ "React")を使った基本的な流れの紹介とBackbone.jsを組み合わせてやるにはどうするかという話が書かれています。

Fluxアーキテクチャの`Dispatcher -> Store -> View -> ...`という流れの要点がまとまっていて分かりやすい気がします。

## お知らせ

既に[JSer.info 200回記念イベントを11月1日に行います - JSer.info](http://0.0.0.0:4000/events/jser200/ "JSer.info 200回記念イベントを11月1日に行います - JSer.info")という記事でお知らせしていますが、
11月1日に[JSer.info 200回記念イベント - connpass](http://connpass.com/event/9067/ "JSer.info 200回記念イベント - connpass")をやります。

既に参加枠はいっぱいになってますが、「発表枠」はまだ募集しています。

- [JSer.info 200回記念イベント · Issue #31 · jser/jser.info](https://github.com/jser/jser.info/issues/31 "JSer.info 200回記念イベント · Issue #31 · jser/jser.info")
- [jser/jser.info - Gitter](https://gitter.im/jser/jser.info "jser/jser.info - Gitter")
- [#jserinfo](https://twitter.com/search?q=%23jserinfo "#jserinfo - Twitter Search")

とかにこんなネタどうだろとか投げれば拾いに行くので、気軽にご応募下さい。

### パネルディスカッションについて

パネルディスカッションでは、[JSer.info 200回記念イベント - Google モデレーター](http://www.google.com/moderator/?hl=ja#16/e=213da7 "JSer.info 200回記念イベント - Google モデレーター")に投稿されたものなどからテーマを決めて話したいと思っています。

なので、パネラーの人や参加者に聞きたい事を好き勝手書いておくといいと思います。

パネル参加者(予定)

- @azu
    - JSer.info の人
- @yosuke_furukawa
    - 日本Node.jsユーザグループ代表
- @saneyuki_s
    - Mozilla contributor. ECMAScript/Rust/Gecko/Servo.
- @Constellation
    - WebKit committer. ECMAScript/browsers/JIT/GPU.
- @t_wada
    - TDD 実践者. Testing/JavaScript/AST.

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 0.9.0 · marijnh/acorn
[github.com/marijnh/acorn/releases/tag/0.9.0](https://github.com/marijnh/acorn/releases/tag/0.9.0 "Release 0.9.0 · marijnh/acorn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptパーサのacorn 0.9.0リリース。

----

## node-browserify/changelog.markdown at 6.0.0 · substack/node-browserify
[github.com/substack/node-browserify/blob/6.0.0/changelog.markdown](https://github.com/substack/node-browserify/blob/6.0.0/changelog.markdown "node-browserify/changelog.markdown at 6.0.0 · substack/node-browserify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">sourcemap</span></p>

browserify 6.0.0リリース。

SourceMapのファイルパスがベースURLからの相対パスとなった。

----

## Release v1.3.0 - UI Improvements · yeoman/yo
[github.com/yeoman/yo/releases/tag/v1.3.0](https://github.com/yeoman/yo/releases/tag/v1.3.0 "Release v1.3.0 - UI Improvements · yeoman/yo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

yo v1.3.0リリース。

コマンドラインUIの改善

----

## Google Developers Blog: Promises in the Google APIs JavaScript Client Library
[googledevelopers.blogspot.com/2014/10/promises-in-google-apis-javascript.html](http://googledevelopers.blogspot.com/2014/10/promises-in-google-apis-javascript.html "Google Developers Blog: Promises in the Google APIs JavaScript Client Library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Google APIのクライアントライブラリがPromise/A+ベースのものとなった

----

## Release Stable API · mozilla/localForage
[github.com/mozilla/localForage/releases/tag/1.0.0](https://github.com/mozilla/localForage/releases/tag/1.0.0 "Release Stable API · mozilla/localForage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

IndexedDB, WebSQL, localStorageを同じインタフェースで使えるlocalForage 1.0.0リリース。

----
<h1 class="site-genre">アーティクル</h1>

----


## 【JavaScript】 MutationObserverの使い方 個人的まとめ - はりをきば
[blog.gutyan.jp/entry/2014/09/06/MutationObserver](http://blog.gutyan.jp/entry/2014/09/06/MutationObserver "【JavaScript】 MutationObserverの使い方 個人的まとめ - はりをきば")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

MutationObserverの使い方、オプションについての解説

----

## Node.js Security Tips
[blog.risingstack.com/node-js-security-tips/](http://blog.risingstack.com/node-js-security-tips/ "Node.js Security Tips")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">セキュリティ</span></p>

Node.jsとセキュリティについて

eval、strict mode、sudoしない、シェルを叩いてコマンドを実行しない、一時ファイル、XSS、HttpOnly、CSP等の扱いについて書かれている

----

## npm 2.0.0でローカルモジュールを使ってrequire(&#x27;../../../&#x27;)を回避する | Web Scratch
[efcl.info/2014/10/04/npm2-local-module/](http://efcl.info/2014/10/04/npm2-local-module/ "npm 2.0.0でローカルモジュールを使ってrequire(&#x27;../../../&#x27;)を回避する | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>

npm 2.0.0からdependenciesにローカルパスを指定出来るようになり、プロジェクトだけで使うUitlsを読み込みやすくなった話

----

## HTML5Rocks の日本語記事まとめ - Google Developer Relations Japan Blog
[googledevjp.blogspot.com/2014/10/html5rocks.html](http://googledevjp.blogspot.com/2014/10/html5rocks.html "HTML5Rocks の日本語記事まとめ - Google Developer Relations Japan Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">翻訳</span> <span class="jser-tag">まとめ</span></p>

HTML5Rockに現在公開されている翻訳記事のまとめ

----

## レスポンシブイメージのネイティブサポート - HTML5 Rocks
[www.html5rocks.com/ja/tutorials/responsive/picture-element/](http://www.html5rocks.com/ja/tutorials/responsive/picture-element/ "レスポンシブイメージのネイティブサポート - HTML5 Rocks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">画像</span></p>

レスポンシブに画像を扱うpicture要素について。

media queryでの分岐、srcset属性での解像度対応、読み込む画像の種類によるfailback

----

## viljamis/Molten-Leading
[github.com/viljamis/Molten-Leading](https://github.com/viljamis/Molten-Leading "viljamis/Molten-Leading")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

jQueryで実装されてたMolten Leadingのpure JavaScript版。

line-heightを要素の幅に併せて変更してくれるライブラリ

----

## React Apps Using Flux and Backbone | Toptal
[www.toptal.com/front-end/simple-data-flow-in-react-applications-using-flux-and-backbone](http://www.toptal.com/front-end/simple-data-flow-in-react-applications-using-flux-and-backbone "React Apps Using Flux and Backbone | Toptal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">backbone.js</span> <span class="jser-tag">JavaScript</span></p>

Fluxアーキテクチャのフローについて。

DispatcherでイベントとState管理、Store(EventEmitter)がブロードキャストしたイベントをキャッチしてViewをレンダリングするという流れ。

これをBackbone.jsとReactを使った実装について

----

## ECMAScript 6 promises (2/2): the API
[www.2ality.com/2014/10/es6-promises-api.html](http://www.2ality.com/2014/10/es6-promises-api.html "ECMAScript 6 promises (2/2): the API")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">tutorial</span></p>

ES6 Promiseについて詳しい解説。基本的な使い方やどのようなフローで動くか、エラーハンドリング、メリット/デメリット、デバッグ、Promiseラッパの書き方、他の機能と強調した書き方についてなど

----

## まだmechanizeで消耗してるの? WebDriverで銀行をスクレイピング（ProtractorとWebdriverIOを例に） - 詩と創作・思索のひろば (Poetry, Writing and Contemplation)
[motemen.hatenablog.com/entry/2014/10/01/scrape-by-protractor-webdriverio](http://motemen.hatenablog.com/entry/2014/10/01/scrape-by-protractor-webdriverio "まだmechanizeで消耗してるの? WebDriverで銀行をスクレイピング（ProtractorとWebdriverIOを例に） - 詩と創作・思索のひろば (Poetry, Writing and Contemplation)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

AngularJS向けのE2EテストフレームワークであるProtractorを使ったスクレイピングについて。

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## A primer on Content Security Policy // Speaker Deck
[speakerdeck.com/polarblau/a-primer-on-content-security-policy](https://speakerdeck.com/polarblau/a-primer-on-content-security-policy "A primer on Content Security Policy // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">スライド</span></p>

XSSの動く仕組み、そのXSSを防止するためのエスケープや必要な事の多さとその一つとしてのCSPについてのスライド。

CSPのルールについての紹介

----

## React - A JavaScript library for building user interfaces // Speaker Deck
[speakerdeck.com/helielson/react-a-javascript-library-for-building-user-interfaces](https://speakerdeck.com/helielson/react-a-javascript-library-for-building-user-interfaces "React - A JavaScript library for building user interfaces // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

React.js入門的なスライド。

render、state、componentのライフサイクル、テストについて

----

## Ampersand.js – Minimalistic Approach to not so minimalistic Problems // Speaker Deck
[speakerdeck.com/kamilogorek/ampersand-dot-js-minimalistic-approach-to-not-so-minimalistic-problems](https://speakerdeck.com/kamilogorek/ampersand-dot-js-minimalistic-approach-to-not-so-minimalistic-problems "Ampersand.js – Minimalistic Approach to not so minimalistic Problems // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Ampersand.js の紹介スライド

- [▶ Kamil Ogórek – Ampersand.js – Minimalistic Approach to not so minimalistic Problems \[Reject.JS 2014\] - YouTube](https://www.youtube.com/watch?v=2Rzxn-xaFkg&amp;index=5&amp;list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw "▶ Kamil Ogórek – Ampersand.js – Minimalistic Approach to not so minimalistic Problems \[Reject.JS 2014\] - YouTube")

----

## ES6: the future is now // Speaker Deck
[speakerdeck.com/jsist/es6-the-future-is-now](https://speakerdeck.com/jsist/es6-the-future-is-now "ES6: the future is now // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">スライド</span></p>

ECMAScriptのタイムライン、ES6の機能紹介のスライド

----

## TypeScript: coding JavaScript without the pain
[www.slideshare.net/SanderMak/typescript-coding-javascript-without-the-pain](http://www.slideshare.net/SanderMak/typescript-coding-javascript-without-the-pain "TypeScript: coding JavaScript without the pain")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">スライド</span></p>

TypeScriptの特徴について紹介しているスライド

- [sandermak/typescript-presentation](https://github.com/sandermak/typescript-presentation "sandermak/typescript-presentation")

----

## Localize your frontend // slidr.io
[slidr.io/klyrr/localize-your-frontend##1](http://slidr.io/klyrr/localize-your-frontend##1 "Localize your frontend // slidr.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span> <span class="jser-tag">AngularJS</span></p>

jimdo.com のローカライズについてのスライド。数字フォーマットの問題に対してAngularJS、Closure LibraryやECMA i18n API(とpolyfill)等について

- [▶ Tina Umlandt – Localize your frontend! \[Reject.JS 2014\] - YouTube](https://www.youtube.com/watch?v=Lu4mholN2lA&amp;index=3&amp;list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw "▶ Tina Umlandt – Localize your frontend! \[Reject.JS 2014\] - YouTube")

----

## Reject.JS 2014 - YouTube
[www.youtube.com/playlist?list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw](https://www.youtube.com/playlist?list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw "Reject.JS 2014 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span> <span class="jser-tag">まとめ</span></p>

Reject.JS 2014 の動画が公開された

<a href='http://rejectjs.org/speakers/'>http://rejectjs.org/speakers/</a>

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Steady.js
[lafikl.github.io/steady.js/](http://lafikl.github.io/steady.js/ "Steady.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

scrollイベントを扱うライブラリ。

onscrollをthrottleしたり、topからの位置で反応するイベントをつけたりスクロール周りの処理を扱いやすくしてくれる

----

## JavaScript Promises Essentials | Packt
[www.packtpub.com/application-development/javascript-promises-essentials](https://www.packtpub.com/application-development/javascript-promises-essentials "JavaScript Promises Essentials | Packt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">電子書籍</span></p>

JavaScript Promiseについての書籍。

WinJSのPromiseについても扱ってる

----

## verb - A CAD Library for the Web
[verbnurbs.com/](http://verbnurbs.com/ "verb - A CAD Library for the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

CADライブラリ

----

## yahoo/gifshot
[github.com/yahoo/gifshot](https://github.com/yahoo/gifshot "yahoo/gifshot")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span> <span class="jser-tag">library</span></p>

複数枚の画像や動画からgifを作成する JavaScriptライブラリ

----

## Mozilla Brick
[brick.mozilla.io/](http://brick.mozilla.io/ "Mozilla Brick")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Mozilla</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

WebComponentを使ったUIコンポーネントライブラリ

----

## shakiba/svgexport
[github.com/shakiba/svgexport](https://github.com/shakiba/svgexport "shakiba/svgexport")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">SVG</span> <span class="jser-tag">画像</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

PhantomJSを使ってSVGをPNG/JPEG/PDFなどに変換出来るコマンドラインツール。

----

## SweetAlert
[tristanedwards.me/sweetalert](http://tristanedwards.me/sweetalert "SweetAlert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

ダイアログUIライブラリ

----
<h1 class="site-genre">書籍関係</h1>


----

## Developing a Gulp.js Edge - O&#x27;Reilly Media
[shop.oreilly.com/product/9781939902146.do](http://shop.oreilly.com/product/9781939902146.do "Developing a Gulp.js Edge - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">book</span></p>

JavaScriptのStreamベースのビルドシステムであるGulpについての書籍

- [gulp.js - the streaming build system](http://gulpjs.com/ "gulp.js - the streaming build system")

----

## Amazon.co.jp: Webアプリ構築のためのAngularJS 電子書籍: 外村 和仁, CodeGrid: Kindleストア
[www.amazon.co.jp/dp/B00O4RMZ4O/](http://www.amazon.co.jp/dp/B00O4RMZ4O/ "Amazon.co.jp: Webアプリ構築のためのAngularJS 電子書籍: 外村 和仁, CodeGrid: Kindleストア")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span> <span class="jser-tag">kindle</span></p>

2014年10月6日発売

<a href='https://app.codegrid.net/'>https://app.codegrid.net/</a> の攻略！AngularJSの連載を元にした書籍

----
