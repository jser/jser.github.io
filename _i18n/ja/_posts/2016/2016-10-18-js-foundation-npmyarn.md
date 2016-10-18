---
title: "2016-10-18のJS: JS Foundation、npmクライアントのyarn"
author: azu
layout: post
date : 2016-10-18T09:39
category: JSer
tags:
    - jQuery
    - JS
    - Yarn
    - npm

---

JSer.info #301 - Linux Foundationの一つとして[JS Foundation](https://js.foundation/ "JS Foundation")ができたそうです。

- [The Linux Foundation Unites JavaScript Community for Open Web Development | The JS Foundation](https://js.foundation/announcements/2016/10/17/Linux-Foundation-Unites-JavaScript-Community-Open-Web-Development/ "The Linux Foundation Unites JavaScript Community for Open Web Development | The JS Foundation")

元は[jQuery Foundation](https://jquery.org/ "jQuery Foundation")なので、JavaScriptのオープンソースプロジェクトの開発支援などが目的で設立されたようです。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">The jQuery Foundation is now the JS Foundation, you can follow the Foundation on <a href="https://twitter.com/the_jsf">@the_jsf</a> and the jQuery project here on <a href="https://twitter.com/jquery">@jquery</a>!</p>&mdash; jquery (@jquery) <a href="https://twitter.com/jquery/status/788012682494423040">October 17, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

[Yarn](https://yarnpkg.com/ "Yarn")というnpmクライアントがリリースされました。

- [Yarn: A new package manager for JavaScript | Engineering Blog | Facebook Code](https://code.facebook.com/posts/1840075619545360 "Yarn: A new package manager for JavaScript | Engineering Blog | Facebook Code")

[npm](https://www.npmjs.com/ "npm")のモジュールを管理するコマンドラインツールとして同名の[npm](https://www.npmjs.com/package/npm "npm")がありますが、yarnは後者のコマンドラインツールの実装です。

`package.json`の扱いは既存のnpmと[互換性](https://github.com/yarnpkg/yarn/labels/compatibility "compatibility discussion")を持つためJavaScriptのエコシステム自体は同様です。(Bowerはこれを分割してしまった)
特徴としてキャッシュや並列処理を行い高速なインストール、また`yarn.lock`を使った依存バージョン固定をデフォルトで行います。

コマンドラインのインタフェースの互換性は目的ではないですが、以下にコマンドの比較がまとめられています。

- [NPM vs Yarn Cheat Sheet](https://shift.infinite.red/npm-vs-yarn-cheat-sheet-8755b092e5cc "NPM vs Yarn Cheat Sheet")
- [Migrating from npm | Yarn](https://yarnpkg.com/en/docs/migrating-from-npm "Migrating from npm | Yarn")


----
<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at 9.7.1 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.7.1/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.7.1/Changelog.md "jsdom/Changelog.md at 9.7.1 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.7.0リリース。
EventListenerOptionsのサポート、`document.hasFocus()`のサポートなど

----

## ESLint v3.8.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/10/eslint-v3.8.0-released](http://eslint.org/blog/2016/10/eslint-v3.8.0-released "ESLint v3.8.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.8.0リリース。
`executeOnFiles()`の結果の`source`プロパティにソースコードを含められるように、新しいルールの追加や修正など

- [ESLint v3.8.0 - Qiita](http://qiita.com/mysticatea/items/6f037c15057c57982453 "ESLint v3.8.0 - Qiita")

----

## Angular 2.1.0 Now Available
[angularjs.blogspot.com/2016/10/angular-210-now-available.html](http://angularjs.blogspot.com/2016/10/angular-210-now-available.html "Angular 2.1.0 Now Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2.1.0リリース。
Routerがpreloadingのサポートなど

----

## Release Notes for Safari Technology Preview 15 | WebKit
[webkit.org/blog/6987/release-notes-for-safari-technology-preview-15/](https://webkit.org/blog/6987/release-notes-for-safari-technology-preview-15/ "Release Notes for Safari Technology Preview 15 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 15リリース。
El Capitan向けの最後のリリース、Fetch APIの改善、`download`属性のサポート、`DOMTokenList.prototype.supports()`のサポートなど

----

## The Linux Foundation Unites JavaScript Community for Open Web Development | The JS Foundation
[js.foundation/announcements/2016/10/17/Linux-Foundation-Unites-JavaScript-Community-Open-Web-Development/](https://js.foundation/announcements/2016/10/17/Linux-Foundation-Unites-JavaScript-Community-Open-Web-Development/ "The Linux Foundation Unites JavaScript Community for Open Web Development | The JS Foundation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jQuery</span></p>

jQuery FoundationはJS Foundationになった。

- [JS Foundation (@the\_jsf) | Twitter](https://twitter.com/the_jsf "JS Foundation (@the\_jsf) | Twitter")
- [jquery on Twitter: The jQuery Foundation is now the JS Foundation, you can follow the Foundation on @the\_jsf and the jQuery project here on @jquery!](https://twitter.com/jquery/status/788012682494423040 "jquery on Twitter: &amp;#34;The jQuery Foundation is now the JS Foundation, you can follow the Foundation on @the\_jsf and the jQuery project here on @jquery!&amp;#34;")

----

## Node v6.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.8.0/](https://nodejs.org/en/blog/release/v6.8.0/ "Node v6.8.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.8.0リリース。
`fs.existsSync`がdeprecatedではなくなった。`http.request`が`timeout`オプションを受け取れるようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Exploring JavaScript: Typed Arrays
[codingbox.io/exploring-javascript-typed-arrays-c8fd4f8bd24f](https://codingbox.io/exploring-javascript-typed-arrays-c8fd4f8bd24f "Exploring JavaScript: Typed Arrays")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Typed Arraysについての入門的な解説

----

## Introduction to HTTP/2  |  Web  |  Google Developers
[developers.google.com/web/fundamentals/performance/http2/](https://developers.google.com/web/fundamentals/performance/http2/ "Introduction to HTTP/2  |  Web  |  Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP2</span> <span class="jser-tag">tutorial</span></p>

HTTP/2入門記事。 HTTP/2の概要が簡潔にまとまっている

----

## JavaScriptの配列のパターン | Web Scratch
[efcl.info/2016/10/11/array-patterns/](http://efcl.info/2016/10/11/array-patterns/ "JavaScriptの配列のパターン | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES2015+をベースにした配列のパターンについて。 `indexOf(x) === -1`とか使わなくていいパターンや代替となる方法などについてサンプルコードを中心にかかれている

----

## AbemaTV の番組表リニューアルに伴うパフォーマンス改善 - Qiita
[qiita.com/keyi8773/items/f435f062afa7c5dc8e13](http://qiita.com/keyi8773/items/f435f062afa7c5dc8e13 "AbemaTV の番組表リニューアルに伴うパフォーマンス改善 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">React</span></p>

無限スクロール系のUIパフォーマンスの改善について。
レンダリングの改善、`position: relative`による意図しないレイヤーが作成される問題、スロットリングなどの低減策についてなど

- [GPUアクセラレーションとposition: relativeによるレイヤー生成について ::ハブろぐ](https://havelog.ayumusato.com/develop/performance/e556-compositing_border_and_layer.html "GPUアクセラレーションとposition: relativeによるレイヤー生成について ::ハブろぐ")

----

## アメブロ2016 ~ React/ReduxでつくるIsomorphic web app ~ | CyberAgent Developers Blog | サイバーエージェント デベロッパーズブログ
[developers.cyberagent.co.jp/blog/archives/636/](https://developers.cyberagent.co.jp/blog/archives/636/ "アメブロ2016 ~ React/ReduxでつくるIsomorphic web app ~ | CyberAgent Developers Blog | サイバーエージェント デベロッパーズブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span></p>

アメブロをReact/Reduxでサーバサイドレンダリングの構造に移行するまでの話。
ツール環境、CSS、アクセシビリティ、レンダリングについてなど

----

## Undo Functionality with the Command Pattern in JavaScript — Pyred
[pyred.net/coding/2016/10/12/undo-functionality-with-the-command-pattern-in-javascript](http://pyred.net/coding/2016/10/12/undo-functionality-with-the-command-pattern-in-javascript "Undo Functionality with the Command Pattern in JavaScript — Pyred")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">デザインパターン</span></p>

JavaScriptでのコマンドパターンについて

----

## Vue.js入門 ―最速で作るシンプルなWebアプリケーション：連載｜gihyo.jp … 技術評論社
[gihyo.jp/dev/serial/01/vuejs](http://gihyo.jp/dev/serial/01/vuejs "Vue.js入門 ―最速で作るシンプルなWebアプリケーション：連載｜gihyo.jp … 技術評論社")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Vue.jsについての連載

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## モダン日本語フォント指定 // Speaker Deck
[speakerdeck.com/tacamy/modanri-ben-yu-huontozhi-ding](https://speakerdeck.com/tacamy/modanri-ben-yu-huontozhi-ding "モダン日本語フォント指定 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span></p>

CSSのfont-familyについてのスライド。
OSやブラウザでfontの情報が異なるため、@font-faceを使い定義するという話

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## JSPerf - Community Driven JavaScript Performance Benchmarks
[jsperf.co/](http://jsperf.co/ "JSPerf - Community Driven JavaScript Performance Benchmarks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

JavaScriptのコードのパフォーマンス計測サイト。
jsperf.com と似たような感じのサイト。
データはGitHubへ自動的にコミットされ、Jekyllを使った静的サイトとして配信されてる。

- [hasharray/jsperf: JavaScript Performance Benchmarks](https://github.com/hasharray/jsperf "hasharray/jsperf: JavaScript Performance Benchmarks")

----

## emartech/angular2-phonecat: Angular 2 port of the original Angular Phonecat application with Webpack
[github.com/emartech/angular2-phonecat](https://github.com/emartech/angular2-phonecat "emartech/angular2-phonecat: Angular 2 port of the original Angular Phonecat application with Webpack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AngularJS 2にPhonecatを移植したもの

----

## pauliusuza/node-v7-async-await-demo: Node.js 7.x async / await support demonstration
[github.com/pauliusuza/node-v7-async-await-demo](https://github.com/pauliusuza/node-v7-async-await-demo "pauliusuza/node-v7-async-await-demo: Node.js 7.x async / await support demonstration")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span></p>

Node.js 7.xでasync/awaitを有効にするデモ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Yarn
[yarnpkg.com/](https://yarnpkg.com/ "Yarn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

npmクライアントツール。
`package.json`の扱いは既存のnpmと互換を持つ。
キャッシュや並列処理を行い高速なインストール、`yarn.lock`を使った依存バージョン固定を正確に行える。

- [Yarn: A new package manager for JavaScript | Engineering Blog | Facebook Code](https://code.facebook.com/posts/1840075619545360 "Yarn: A new package manager for JavaScript | Engineering Blog | Facebook Code")
- [The npm Blog — Hello, Yarn!](http://blog.npmjs.org/post/151660845210/hello-yarn "The npm Blog — Hello, Yarn!")
- [Migrating from npm | Yarn](https://yarnpkg.com/en/docs/migrating-from-npm "Migrating from npm | Yarn")

----

## naptha/tesseract.js: Pure Javascript OCR for 62 Languages
[github.com/naptha/tesseract.js](https://github.com/naptha/tesseract.js "naptha/tesseract.js: Pure Javascript OCR for 62 Languages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">OCR</span> <span class="jser-tag">library</span></p>

tesseract OCRのJavaScript port。
ブラウザやNodeでOCRできるライブラリ

- [Compile to EMScripten/asm.js · Issue #75 · tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract/issues/75 "Compile to EMScripten/asm.js · Issue #75 · tesseract-ocr/tesseract")
- [tesseract-ocr/tesseract: Tesseract Open Source OCR Engine (main repository)](https://github.com/tesseract-ocr/tesseract "tesseract-ocr/tesseract: Tesseract Open Source OCR Engine (main repository)")

----
<h1 class="site-genre">書籍関係</h1>

----

## getify/Functional-Light-JS: A book about functional programming in JavaScript.
[github.com/getify/Functional-Light-JS](https://github.com/getify/Functional-Light-JS "getify/Functional-Light-JS: A book about functional programming in JavaScript.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">ebook</span></p>

関数型JavaScriptについての無料の書籍

----
