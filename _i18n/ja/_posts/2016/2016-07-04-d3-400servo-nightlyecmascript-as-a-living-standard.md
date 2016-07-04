---
title: "2016-07-04のJS: D3 4.0.0、Servo Nightly、ECMAScript as a Living Standard"
author: azu
layout: post
date : 2016-07-04T22:32
category: JSer
tags:
    - D3
    - SVG
    - Servo
    - browser
    - ECMAScript

---

JSer.info #286 - D3.js 4.0.0がリリースされました。

- [Release v4.0.0 · d3/d3](https://github.com/d3/d3/releases/tag/v4.0.0 "Release v4.0.0 · d3/d3")
- [d3/CHANGES.md at master · d3/d3](https://github.com/d3/d3/blob/master/CHANGES.md "d3/CHANGES.md at master · d3/d3")

大幅に書き直され、それぞれの機能が個別のモジュールとして分けられています。
詳細は[CHANGES.md](https://github.com/d3/d3/blob/master/CHANGES.md)にかかれています。

----

Mozillaが開発しているレンダリングエンジンの[Servo](https://servo.org/ "Servo")のNightlyビルドが公開されるようになりました。

- [Servo Nightly Builds Available](https://blog.servo.org/2016/06/30/servo-nightlies/ "Servo Nightly Builds Available")

ブラウザのUIとしてはHTMLベースの[browserhtml](https://github.com/browserhtml/browserhtml "browserhtml")が使われていて、
ブラウザアプリとして試すことができます。

----

[ECMAScript as a Living Standard](http://azu.github.io/slide/2016/node-es/ecmascript.html "ECMAScript as a Living Standard")というスライドでは、ECMAScriptの策定プロセスがソフトウェア一般のプロセスと大きく変わらないものであるという話が書かれています。
ES2015からは多くの議論やコミットがGitHub上で行われているため、OSSを見ていくのとあまり変わらないフローを取る事ができます。

なぜ毎年リリースするというプロセスの変更を取り入れたのかなどについて書かれています。

- [Node学園 21時限目でECMAScript as a Living Standardという発表をした | Web Scratch](http://efcl.info/2016/06/29/node-ecmascript/ "Node学園 21時限目でECMAScript as a Living Standardという発表をした | Web Scratch")

後、このような早いプロセスへの変更に対応できるようなJavaScript入門書があると良さそうなので今書いています。

- [asciidwango/js-primer: JavaScriptの入門書](https://github.com/asciidwango/js-primer "asciidwango/js-primer: JavaScriptの入門書")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release Cycle Diversity · cyclejs/core
[github.com/cyclejs/core/releases/tag/v7.0.0](https://github.com/cyclejs/core/releases/tag/v7.0.0 "Release Cycle Diversity · cyclejs/core")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cycle.js 7.0.0リリース。
RxJS、most.js、xstreamを選んで使えるように、TypeScriptで書き直し、vDOMとしてsnabbdomを使うようになるなど

- [snabbdom](https://github.com/paldepind/snabbdom/ "snabbdom")

----

## Release v15.2.0 · facebook/react
[github.com/facebook/react/releases/tag/v15.2.0](https://github.com/facebook/react/releases/tag/v15.2.0 "Release v15.2.0 · facebook/react")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 15.2.0リリース。
エラーコードが追加されURLから詳細が見られるように、warningメッセージにコンポーネントスタック情報を追加、`React.PropTypes.symbol`の追加など

----

## Release 2.0.0 · sweet-js/sweet.js
[github.com/sweet-js/sweet.js/releases/tag/v2.0.0](https://github.com/sweet-js/sweet.js/releases/tag/v2.0.0 "Release 2.0.0 · sweet-js/sweet.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptでマクロを扱うsweet.js 2.0.0リリース。
context APIが変更された

----

## Release v4.0.0 · d3/d3
[github.com/d3/d3/releases/tag/v4.0.0](https://github.com/d3/d3/releases/tag/v4.0.0 "Release v4.0.0 · d3/d3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span></p>

D3.js 4.0.0リリース。
`d3-scale`や`d3-time`のようにそれぞれの機能がモジュールに分割され、npmパッケージとして個別にインストールできる。
合わせて機能追加や修正が行われている

- [d3/CHANGES.md at master · d3/d3](https://github.com/d3/d3/blob/master/CHANGES.md "d3/CHANGES.md at master · d3/d3")

----

## ESLint v3.0.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/07/eslint-v3.0.0-released](http://eslint.org/blog/2016/07/eslint-v3.0.0-released "ESLint v3.0.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.0.0リリース。
`eslint:recommended`のアップデート、設定ファイル/設定が指定されてない場合は警告がでるように、Node.js 0.12のサポート終了など

- [ESLint v3.0.0 - Qiita](http://qiita.com/mysticatea/items/9c8a8b1219d5f94441e8 "ESLint v3.0.0 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Servo Nightly Builds Available
[blog.servo.org/2016/06/30/servo-nightlies/](https://blog.servo.org/2016/06/30/servo-nightlies/ "Servo Nightly Builds Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Mozilla</span></p>

Mozillaの開発するレンダリングエンジンのServoのDeveloper Preview版が公開された

----

## How to Upgrade a Node Module The Right Way - Jama Software
[www.jamasoftware.com/blog/upgrade-node-module-right-way/](http://www.jamasoftware.com/blog/upgrade-node-module-right-way/ "How to Upgrade a Node Module The Right Way - Jama Software")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">webpack</span></p>

依存モジュールの非互換性なアップデートをどうやってアップグレードしていくかについて。react-routerを例に紹介してる。
webpackのaliasを使ってFeature Flagを作り、フラグ切り替えで新旧の実装を並べて書いていく。

----

## Intersection Observer を用いた要素出現検出の最適化 | blog.jxck.io
[blog.jxck.io/entries/2016-06-25/intersection-observer.html](https://blog.jxck.io/entries/2016-06-25/intersection-observer.html "Intersection Observer を用いた要素出現検出の最適化 | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span></p>

Intersection Observerの使い方や従来の方法との違いについて。
スクロール量や要素の表示に応じた処理

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ECMAScript as a Living Standard
[azu.github.io/slide/2016/node-es/ecmascript.html](http://azu.github.io/slide/2016/node-es/ecmascript.html "ECMAScript as a Living Standard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">スライド</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

ECMAScript仕様策定のプロセスを理解することで、ECMAScriptに関する情報を見る方法がわかるという話。
ES2015は毎年リリースに向けてのベースとなるような仕様であるため、これから足りない部分については議論が進んで行く

- [Node学園 21時限目でECMAScript as a Living Standardという発表をした | Web Scratch](http://efcl.info/2016/06/29/node-ecmascript/ "Node学園 21時限目でECMAScript as a Living Standardという発表をした | Web Scratch")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## holyjs/holyjs: HolyJS - NodeJS Server Project Starter
[github.com/holyjs/holyjs](https://github.com/holyjs/holyjs "holyjs/holyjs: HolyJS - NodeJS Server Project Starter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">template</span></p>

Node.jsでサーバサイドのプロジェクトテンプレート

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## juliangarnier/anime: Javascript Animation Engine
[github.com/juliangarnier/anime](https://github.com/juliangarnier/anime "juliangarnier/anime: Javascript Animation Engine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

CSSアニメーション管理ライブラリ

----

## planttheidea/vidz: A zero-dependency, framework-agnostic video implementation
[github.com/planttheidea/vidz](https://github.com/planttheidea/vidz "planttheidea/vidz: A zero-dependency, framework-agnostic video implementation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span> <span class="jser-tag">library</span></p>

Video要素でのロードやイベントハンドリングなどを扱うライブラリ

----

## planttheidea/crio: Immutable objects and arrays in a natural way
[github.com/planttheidea/crio](https://github.com/planttheidea/crio "planttheidea/crio: Immutable objects and arrays in a natural way")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ArrayとObjectのImmutable版を提供するライブラリ。
Mutableとして操作したい場合は、ネイティブのもので操作してラップするか、`.mutable(array => {})`を利用できる。

----

## leebyron/iterall: Minimal zero-dependency utilities for using Iterables in all JavaScript environments.
[github.com/leebyron/iterall](https://github.com/leebyron/iterall "leebyron/iterall: Minimal zero-dependency utilities for using Iterables in all JavaScript environments.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ArrayやArray-likeなどをiterableとして扱う`forEach`の処理を書くためのライブラリ

----

## ejs - Readable JavaScript Errors
[i-break-codes.github.io/ejs/](https://i-break-codes.github.io/ejs/ "ejs - Readable JavaScript Errors")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">debug</span></p>

`window.onerror`でJavaScriptのエラーを整形してコンソールに表示してくれるライブラリ

----

## caiogondim/fast-memoize.js: Fastest possible memoization library
[github.com/caiogondim/fast-memoize.js](https://github.com/caiogondim/fast-memoize.js "caiogondim/fast-memoize.js: Fastest possible memoization library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

メモ化ライブラリ

----

## gcanti/babel-plugin-tcomb: Babel plugin for static and runtime type checking using Flow and tcomb
[github.com/gcanti/babel-plugin-tcomb](https://github.com/gcanti/babel-plugin-tcomb "gcanti/babel-plugin-tcomb: Babel plugin for static and runtime type checking using Flow and tcomb")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

FlowTypeの型をtcombを使いランタイムassertに変換するBabelプラグイン

----
<h1 class="site-genre">書籍関係</h1>

----

## Modular JS: Practical ES6 - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920047124.do](http://shop.oreilly.com/product/0636920047124.do "Modular JS: Practical ES6 - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

2016年8月発売
ES6についての書籍

----
