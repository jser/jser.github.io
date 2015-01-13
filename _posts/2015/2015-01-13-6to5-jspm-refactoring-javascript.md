
---
title: "2015-01-13のJS: 6to5、ES6とjspm、リファクタリングJavaScript"
author: azu
layout: post
date : 2015-01-13T21:44
category: JSer
tags:
    - ES6
    - リファクタリング
    - JavaScript
    - modules

---

JSer.info #210 - ES6+のコードをES5に変換するツールである[6to5](http://6to5.org/ "6to5 · Turn ES6+ code into readable vanilla ES5")の公式サイトがリニューアルされました。

また、同じくES6のコードを変換するツールである[esnext](https://github.com/esnext/esnext "esnext")が6to5に合流して、移行していくようです。

- [6to5 + esnext · 6to5](http://6to5.org/blog/2015/01/12/6to5-esnext/ "6to5 + esnext · 6to5")

ちょうど[ライブラリをES6で書いて公開する所から始めよう | Web Scratch](http://efcl.info/2015/01/09/write-es6/ "ライブラリをES6で書いて公開する所から始めよう | Web Scratch")という、6to5を使いES6で書いたライブラリを公開する流れについての記事も公開したので6to5を試してみるといいかもしれません。

----

[JavaScript in 2015 - Glen Maddern: Internet Pro](http://glenmaddern.com/articles/javascript-in-2015 "JavaScript in 2015 - Glen Maddern: Internet Pro") という記事では、[jspm](http://jspm.io/ "jspm")というパッケージ管理ツールについて紹介しています。

[jspm](http://jspm.io/ "jspm")はnpmやGitHubからライブラリをインストールするコマンドラインツールと[SystemJS](https://github.com/systemjs/systemjs "SystemJS")を使ったモジュールローダから成っています。

<iframe width="420" height="315" src="//www.youtube.com/embed/iukBMY4apvI?rel=0" frameborder="0" allowfullscreen></iframe>

上記の動画では、redditからgifを抽出して表示するという流れを[jspm](http://jspm.io/ "jspm")で行っていて、とてもテンポよく紹介しています。

開発中はRequireJSのように動的にES6 modulesやCommonJS、AMD等を読み込み、最後に[Production Workflows](https://github.com/jspm/jspm-cli/wiki/Production-Workflows "Production Workflows")にあるように一つのファイルにバンドルする流れで紹介されています。

----

[The Refactoring Tales](http://javascriptplayground.com/the-refactoring-tales/refactoring-tales.html "The Refactoring Tales")という電子書籍ではJavaScriptのリファクタリングについて書かれています。

まだ未完成ですが、jQueryでかかれたテストがしにくいレガシーコードをどうやって修正していくのかなどについて紹介されています。

簡単な概要は[The Refactoring Tales - JavaScriptのリファクタリング本を読んだ | Web Scratch](http://efcl.info/2015/01/11/refactoring-tales/ "The Refactoring Tales - JavaScriptのリファクタリング本を読んだ | Web Scratch")にて紹介しています。

----


<h1 class="site-genre">ヘッドライン</h1>

----

## 6to5 · Turn ES6+ code into readable vanilla ES5
[6to5.org/](https://6to5.org/ "6to5 · Turn ES6+ code into readable vanilla ES5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

包含的にES6のコードをES5に変換する6to5の公式サイトリニューアル。
 JSXやFlowとか多くの部分を対応、polyfill出来るところは外部のpolyfillを読み込み対応、可読性が高いコードを吐くようになっている。

----
<h1 class="site-genre">アーティクル</h1>

----

## ライブラリをES6で書いて公開する所から始めよう | Web Scratch
[efcl.info/2015/01/09/write-es6/](http://efcl.info/2015/01/09/write-es6/ "ライブラリをES6で書いて公開する所から始めよう | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

ES6でライブラリを書いて、テストしてnpmに公開するまでの流れ。
6to5+power-assert+mochaの組み合わせを設定ファイルレスで行う話

----

## Shape Security Labs: A Technical Comparison of the Shift and SpiderMonkey AST Formats
[engineering.shapesecurity.com/2015/01/a-technical-comparison-of-shift-and.html](http://engineering.shapesecurity.com/2015/01/a-technical-comparison-of-shift-and.html "Shape Security Labs: A Technical Comparison of the Shift and SpiderMonkey AST Formats")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">spec</span></p>

Shift ASTとSpiderMonkey ASTの違いについて。
改善点、拡張された点、まだ議論すべき点について

----

## A Good Front-End Architecture
[www.sitepoint.com/good-front-end-architecture/](http://www.sitepoint.com/good-front-end-architecture/ "A Good Front-End Architecture")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

フロントエンド(HTML、JavaScript、CSS、リソース)のディレクトリ構造について

----

## Modularizing Underscore.js | &amp;yet Blog
[blog.andyet.com/2015/01/07/modularizing-underscorejs](http://blog.andyet.com/2015/01/07/modularizing-underscorejs "Modularizing Underscore.js | &amp;yet Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">document</span> <span class="jser-tag">library</span></p>

小さいモジュールを大量に作って公開する場合にも問題となる点がある事について。
Amp.jsという小さなモジュールの組み合わせでUnderscoreライクなものを作り、それぞれのモジュールがどのような構造になっているかについて

- [Amp.js](http://amp.ampersandjs.com/ "Amp.js")
- [HenrikJoreteg/fixpack](https://github.com/henrikjoreteg/fixpack "HenrikJoreteg/fixpack")

----

## What&#x27;s New in QUnit 1.16
[www.sitepoint.com/whats-new-qunit-1-16/](http://www.sitepoint.com/whats-new-qunit-1-16/ "What&#x27;s New in QUnit 1.16")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

QUnit 1.16について。
2.0に向けて変更、非同期のテストの新しい方法の追加、Promiseのサポート、`QUnit.skip()`などについて

----

## Cross-tab Communication
[ponyfoo.com/articles/cross-tab-communication](http://ponyfoo.com/articles/cross-tab-communication "Cross-tab Communication")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

localStorageを使ったタブ間のやり取りする方法。
より簡単に行う`local-storage`というライブラリについて

- [bevacqua/local-storage](https://github.com/bevacqua/local-storage "bevacqua/local-storage")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JavaScript in 2015 - Glen Maddern: Internet Pro
[glenmaddern.com/articles/javascript-in-2015](http://glenmaddern.com/articles/javascript-in-2015 "JavaScript in 2015 - Glen Maddern: Internet Pro")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">動画</span></p>

jspmの紹介記事 + 動画。
redditのAPIを使いGIFを表示する画面をjspm+npm+ES6をつかって書く動画。
テンポ良く紹介されている動画で、開発中はビルド等不要でローダで読み込み、プロダクションでは一つのファイルにbundle出来るという特徴を紹介してる。

- [jspm.io - Frictionless Browser Package Management](http://jspm.io/ "jspm.io - Frictionless Browser Package Management")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Essential JavaScript Links
[gist.github.com/ericelliott/d576f72441fc1b27dace](https://gist.github.com/ericelliott/d576f72441fc1b27dace "Essential JavaScript Links")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">links</span></p>

JavaScriptに関するリソースリンク集

----

## Internet ExplorerのどのバージョンからどのHTML/CSS/JSに対応しているかの一覧｜Web制作 W3G
[w3g.jp/blog/ie_supportlist](https://w3g.jp/blog/ie_supportlist "Internet ExplorerのどのバージョンからどのHTML/CSS/JSに対応しているかの一覧｜Web制作 W3G")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">WebPlatformAPI</span></p>

IEバージョン別のサポート終了日、対応したHTML/CSS/JSの機能のまとめ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## azu/espower-6to5 · GitHub
[github.com/azu/espower-6to5](https://github.com/azu/espower-6to5 "azu/espower-6to5 · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

power-assert + 6to5 ES6でpower-assertのテストを書ける。
使用例: https://github.com/azu/textlint-rule-helper

----

## conceptsandtraining/modernie_selenium
[github.com/conceptsandtraining/modernie_selenium](https://github.com/conceptsandtraining/modernie_selenium "conceptsandtraining/modernie\_selenium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">Selenium</span></p>

modern.ieを使ったSeleniumの設定ツール。
自動で必要なものをインストール + Windowsの余計な設定をオフにしてくれる

----

## es-shims/es7-shim
[github.com/es-shims/es7-shim](https://github.com/es-shims/es7-shim "es-shims/es7-shim")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

ES7のpolyfillライブラリ

----

## bevacqua/local-storage
[github.com/bevacqua/local-storage](https://github.com/bevacqua/local-storage "bevacqua/local-storage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

localStorageのAPIをシンプルにしたライブラリ
タブ間のコミュニケーションに使うような監視機能も持ってる

----

## Zhouzi/TheaterJS
[github.com/Zhouzi/TheaterJS](https://github.com/Zhouzi/TheaterJS "Zhouzi/TheaterJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

タイプライター的な文字表示効果等を行えるライブラリ

----

## mirek/node-unused-deps
[github.com/mirek/node-unused-deps](https://github.com/mirek/node-unused-deps "mirek/node-unused-deps")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">module</span> <span class="jser-tag">Tools</span> <span class="jser-tag">console</span></p>

使用してないNodeモジュールがあるかどうかをチェックするコマンドラインツール

----

## tejasmanohar/npm-algos
[github.com/tejasmanohar/npm-algos](https://github.com/tejasmanohar/npm-algos "tejasmanohar/npm-algos")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">アルゴリズム</span></p>

コンピュータサイエンス、アルゴリズムの実装ライブラリのまとめ

----

## Headless Browser Testing With Xvfb
[tobyho.com/2015/01/09/headless-browser-testing-xvfb/](http://tobyho.com/2015/01/09/headless-browser-testing-xvfb/ "Headless Browser Testing With Xvfb")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">console</span> <span class="jser-tag">firefox</span> <span class="jser-tag">browser</span></p>

Firefoxなどヘッドレスで動かすのにXvfbが必要なアプリをxvfb-run firefoxという感じで起動できるコマンドラインツール

----

## Amp.js
[amp.ampersandjs.com/](http://amp.ampersandjs.com/ "Amp.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Underscore.js的なユーティリティ関数のコレクションライブラリ。
それぞれの機能をちゃんと個別のnpmモジュールとしてインストール出来る

- [Modularizing Underscore.js | &amp;yet Blog](http://blog.andyet.com/2015/01/07/modularizing-underscorejs "Modularizing Underscore.js | &amp;yet Blog")

----
<h1 class="site-genre">書籍関係</h1>

----

## Node.js Design Patterns | Packt
[www.packtpub.com/web-development/nodejs-design-patterns](https://www.packtpub.com/web-development/nodejs-design-patterns "Node.js Design Patterns | Packt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">デザインパターン</span> <span class="jser-tag">book</span></p>

Node.jsのデザインパターンについての書籍

----

## The Refactoring Tales
[javascriptplayground.com/the-refactoring-tales/refactoring-tales.html](http://javascriptplayground.com/the-refactoring-tales/refactoring-tales.html "The Refactoring Tales -")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">jQuery</span></p>

JavaScriptのリファクタリングについてのウェブで公開されてる書籍。(まだ執筆中)
1,2章はjQueryべったりな書き方のリファクタリング、3章は不必要な複雑性を分離、4章はデザインパターン、5章はFat Controller等

- [The Refactoring Tales](http://javascriptplayground.com/the-refactoring-tales/ "The Refactoring Tales")
- [The Refactoring Tales - JavaScriptのリファクタリング本を読んだ | Web Scratch](http://efcl.info/2015/01/11/refactoring-tales/ "The Refactoring Tales - JavaScriptのリファクタリング本を読んだ | Web Scratch")

----