---
title: "2015-10-16のJS: Node.js 4.2.0 LTS、ES6、CSS.next"
author: azu
layout: post
date : 2015-10-16T22:22
category: JSer
tags:
    - Node.js
    - ES6
    - CSS
    - JavaScript

---

JSer.info #249 - [Node v4.2.0](https://nodejs.org/en/blog/release/v4.2.0/ "Node v4.2.0")がリリースされました。

このバージョンは"Argon"というコードネームが付いていますが、Node.jsの[LTS](https://github.com/nodejs/LTS "LTS")(Long-term Support)版としてリリースされています。

- [Node.js、初のLong Term Support対象となる「Node.js 4.2」コード名“Argon”がリリース。リリースから2年半はメンテナンス － Publickey](http://www.publickey1.jp/blog/15/nodejs_long_term_support_argon.html "Node.js、初のLong Term Support対象となる「Node.js 4.2」コード名“Argon”がリリース。リリースから2年半はメンテナンス － Publickey")

名前の通りリリースから 18ヶ月アクティブ + 12ヶ月メンテナンスモード で合計30ヶ月のサポートが行われる予定のバージョンです。

加えてコードから実行されているNode.jsがLTSなのかどうかを返す`process.release.lts`などが追加されています。

----

[ES6 Overview in 350 Bullet Points](https://ponyfoo.com/articles/es6 "ES6 Overview in 350 Bullet Points")という記事では同作者が書いた[es6-in-depth](https://ponyfoo.com/articles/tagged/es6-in-depth "es6-in-depth")シリーズを元にES6の機能について箇条書きで紹介されています。

機能別にリスト化されているので、気になったものを見つけたら詳細を見てみるという取っ掛かりとして読むと良いかもしれません。

----

[JavaScript/CSS 2015 Autumn](http://www.slideshare.net/t32k/javascriptcss-2015-autumn "JavaScript/CSS 2015 Autumn")というスライドでは、JavaScriptとCSSの現状について書かれています。

- JavaScriptについてでは、 ES6とBabel
- CSSについてでは、cssnext、PostCSS、Sass
- ビルドツールについてでは、Grunt/gulpとnpm

フロントエンド周りでのツールなどについて広くまとめられているので、導入として全体を見て、気になったものは詳細を調べてみると良さそうです。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v4.2.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v4.2.0/](https://nodejs.org/en/blog/release/v4.2.0/ "Node v4.2.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 4.2.0リリース。
"Argon"というコードネームでLTS版(長期間サポート)を初リリース、コマンドラインオプションにシンタックスチェックだけを行う`--check`を追加

- [add CLI option to syntax check script by bahamas10 · Pull Request #2411 · nodejs/node](https://github.com/nodejs/node/pull/2411 "add CLI option to syntax check script by bahamas10 · Pull Request #2411 · nodejs/node")

----

## Release 3.4.0 Release Candidate · knockout/knockout
[github.com/knockout/knockout/releases/tag/v3.4.0rc](https://github.com/knockout/knockout/releases/tag/v3.4.0rc "Release 3.4.0 Release Candidate · knockout/knockout")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout 3.4.0RCリリース。
`ko.isPureComputed`、`ko.onError`の追加、Observableのパフォーマンス改善など

----

## V8 JavaScript Engine: V8 Release 4.7
[v8project.blogspot.jp/2015/10/v8-release-47.html](http://v8project.blogspot.jp/2015/10/v8-release-47.html "V8 JavaScript Engine: V8 Release 4.7")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.7リリース。
Rest operator、Array#includesの追加など

- [V8 API changes - Google ドキュメント](https://docs.google.com/document/d/1g8JFi8T_oAE_7uAri7Njtig7fKaPDfotU6huOa1alds/edit "V8 API changes - Google ドキュメント")

----

## Release Fetch 0.10.0 · github/fetch
[github.com/github/fetch/releases/tag/v0.10.0](https://github.com/github/fetch/releases/tag/v0.10.0 "Release Fetch 0.10.0 · github/fetch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Fetch APIのpolyfillであるFetch 0.10.0リリース。
`Requst`/`Response`へのメソッドの追加

----
<h1 class="site-genre">アーティクル</h1>

----

## 難読化されたJavaScriptコードを読む : document
[imaya.blog.jp/archives/8183160.html](http://imaya.blog.jp/archives/8183160.html "難読化されたJavaScriptコードを読む : document")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

難読化されたコードを読むためのツールやリファクタリング方法について

----

## ES2015 — Web Fundamentals
[developers.google.com/web/shows/ttt/series-2/es2015](https://developers.google.com/web/shows/ttt/series-2/es2015 "ES2015 — Web Fundamentals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ES6を学ぶためのリソースやツールについて

----

## ES6 Overview in 350 Bullet Points
[ponyfoo.com/articles/es6](https://ponyfoo.com/articles/es6 "ES6 Overview in 350 Bullet Points")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

ES6の機能やポイントについて箇条書きでまとめたもの

----

## Surfin&Safari - Blog Archive » ES6 in WebKit
[www.webkit.org/blog/4054/es6-in-webkit/](https://www.webkit.org/blog/4054/es6-in-webkit/ "Surfin' Safari - Blog Archive » ES6 in WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ECMAScript</span></p>

Safari 9とWebkit nightlyに入ってるES6周りの機能について

----

## A Gentle Introduction to Ember 2.0 — Medium
[medium.com/@jamesfuthey/a-gentle-introduction-to-ember-2-0-8ef1f378ee4](https://medium.com/@jamesfuthey/a-gentle-introduction-to-ember-2-0-8ef1f378ee4 "A Gentle Introduction to Ember 2.0 — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

FirebaseとEmberを使ってブログを作リながら、Emberについて学ぶチュートリアル

----

## Lazy, composable, and modular JavaScript
[codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript](https://codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript "Lazy, composable, and modular JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

JavaScriptでの高階関数、関数合成、遅延評価。
Generator/iteratorを使った関数の組み合わせ方について

----

## Not Angularな環境でProtractorを使ってES2015(ES6), ES7なE2Eテストコードを書いてみた - Qiita
[qiita.com/nana4gonta/items/fabf1ab30ef16050c1e8](http://qiita.com/nana4gonta/items/fabf1ab30ef16050c1e8 "Not Angularな環境でProtractorを使ってES2015(ES6), ES7なE2Eテストコードを書いてみた - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">protractor</span> <span class="jser-tag">Selenium</span></p>

async/awaitを使ったProtractorのE2Eテスト。
非同期処理となる部分をasync/awaitを使うことで直列に書けるようにする話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JavaScript/CSS 2015 Autumn
[www.slideshare.net/t32k/javascriptcss-2015-autumn](http://www.slideshare.net/t32k/javascriptcss-2015-autumn "JavaScript/CSS 2015 Autumn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span></p>

JavaScriptやCSS、ビルドツール周りについて幅広くまとめられているスライド

----

## AngularJSの$watch登録数が60,000だった - @yoshiko_pg
[yoshiko-pg.github.io/slides/20151015-gp-meetup/](http://yoshiko-pg.github.io/slides/20151015-gp-meetup/ "AngularJSの$watch登録数が60,000だった - @yoshiko\_pg")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">スライド</span></p>

AngularJSのパフォーマンスチューニングについてのスライド。
$watchの数の調べ方と改善方法について

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## All of the javascript features.
[jsfeatures.in/](http://jsfeatures.in/ "All of the javascript features.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

ES5、ES6やES.nextの機能別のサンプルコードがまとめられているサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## gabrielbull/react-desktop
[github.com/gabrielbull/react-desktop](https://github.com/gabrielbull/react-desktop "gabrielbull/react-desktop")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">mac</span> <span class="jser-tag">windows</span></p>

OS X(やWindows)風のUIを作成するReact Component

----

## ryanbahniuk/sassaby
[github.com/ryanbahniuk/sassaby](https://github.com/ryanbahniuk/sassaby "ryanbahniuk/sassaby")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span></p>

MochaやJasmineなどと合わせて使えるSassのテストライブラリ。
Sassの関数やmixinなどのテストを行える

----

## Mancy NodeJs Repl
[www.mancy-re.pl/](http://www.mancy-re.pl/ "Mancy NodeJs Repl")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">software</span> <span class="jser-tag">Electron</span></p>

Electronを使ったJavaScript REPLアプリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Front-end Handbook - GitBook
[www.gitbook.com/book/frontendmasters/front-end-handbook/details](https://www.gitbook.com/book/frontendmasters/front-end-handbook/details "Front-end Handbook - GitBook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

フロントエンドについての電子書籍

----
