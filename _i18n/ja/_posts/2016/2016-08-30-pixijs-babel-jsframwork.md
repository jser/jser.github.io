---
title: "2016-08-30のJS: pixi.js 4.0.0、Babel 6.14.0、JSフレームワークアンケート"
author: azu
layout: post
date : 2016-08-30T09:40
category: JSer
tags:
    - Canvas
    - WebGL
    - game
    - Babel
    - framwork
    - survery

---

JSer.info #294 - WebGLやCanvasを使った2Dレンダリングエンジンのpixi.js 4.0.0がリリースされました。

- [Release v4.0.0 · pixijs/pixi.js](https://github.com/pixijs/pixi.js/releases/tag/v4.0.0 "Release v4.0.0 · pixijs/pixi.js")

[RCリリース時の記事](http://www.goodboydigital.com/pixi-js-v4/)でも紹介されていますが、
Multi texture rendereringのサポート、GPU GC管理、WebGLレンダーの改善などが行われています。
また、コア部分が[pixi-gl-core](https://github.com/pixijs/pixi-gl-core "pixi-gl-core")として公開されたり、
npm周りの整備がされています。

バグ修正も行われていますが4.0になって増えたバグもあるので、それらの修正を含めた4.1のリリースが予定されています。

- [Issues · pixijs/pixi.js](https://github.com/pixijs/pixi.js/issues?q=is%3Aopen+is%3Aissue+milestone%3Av4.1 "Issues · pixijs/pixi.js")

----

Babel [6.14.0](https://github.com/babel/babel/releases/tag/v6.14.0 "6.14.0")がリリースされました。

- [6.14.0 Released · Babel](http://babeljs.io/blog/2016/08/24/6.14.0 "6.14.0 Released · Babel")

新しく `latest` と `es2017` のpresetが追加されています。
`latest` presetはES2015+ (ES2015, ES2016, ES2017)のものが含まれていて、ECMAScriptの新しいバージョンが追加されている方式となっています。

----

[The State Of JavaScript: Front-End Frameworks – Medium](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")という記事ではJavaScriptのフレームワークについてのアンケート結果が公開されています。
[The State Of JavaScript](http://stateofjs.com/ "The State Of JavaScript")にて行われたもので、著名なフレームワーク/ライブラリごとに興味や満足度について調べたものです。

対象となっていたフレームワーク/ライブラリは次の6つとなっています。

- React
- Angular
- Angular 2
- Ember
- Vue
- Backbone

この記事ではそのアンケート結果が公開されています。

候補となったものでVue以外は殆どの人が知っていて、

- 学びたいもの: React -> Vue -> Angular2
- 満足度: React -> Vue -> Angular2

という結果になっています。

詳しくは、[The State Of JavaScript: Front-End Frameworks – Medium](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")を参照してください。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v4.0.0 · pixijs/pixi.js
[github.com/pixijs/pixi.js/releases/tag/v4.0.0](https://github.com/pixijs/pixi.js/releases/tag/v4.0.0 "Release v4.0.0 · pixijs/pixi.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

pixi.js 4.0.0リリース
Multi texture rendereringのサポート、GPU GC管理、WebGLレンダーの改善、npmでパッケージの公開など

- [PixiJS v4 Arrives - Goodboy™ — Goodboy™](http://www.goodboydigital.com/pixi-js-v4/ "PixiJS v4 Arrives - Goodboy™ — Goodboy™")

----

## Release v6.14.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.14.0](https://github.com/babel/babel/releases/tag/v6.14.0 "Release v6.14.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.14.0リリース。
`es2017` presetと、ES2015+を扱う`latest` presetが追加された。

----
<h1 class="site-genre">アーティクル</h1>

----

## The State Of JavaScript: Front-End Frameworks – Medium
[medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptのフレームワークについてアンケート結果。
認知度はVue以外大体同じ。
学びたいもの: React -> Vue -> Angular2
満足度: React -> Vue -> Angular2

- [The State Of JavaScript](http://stateofjs.com/ "The State Of JavaScript")

----

## Enable Chrome Accessibility Experiment
[gist.github.com/marcysutton/0a42f815878c159517a55e6652e3b23a](https://gist.github.com/marcysutton/0a42f815878c159517a55e6652e3b23a "Enable Chrome Accessibility Experiment")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">debug</span></p>

Chromeの試験的なAccessibility inspectorを有効にする方法。
要素に対するWAI-ARIAの情報をElementsパネルで見ることができる

----

## Demythstifying Web Components – Back Alley Coder
[www.backalleycoder.com/2016/08/26/demythstifying-web-components/](http://www.backalleycoder.com/2016/08/26/demythstifying-web-components/ "Demythstifying Web Components – Back Alley Coder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Web Componentsに関するよくある誤解について書かれたもの

----

## How To Use WebPageTest and its API | CSS-Tricks
[css-tricks.com/use-webpagetest-api/](https://css-tricks.com/use-webpagetest-api/ "How To Use WebPageTest and its API | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">API</span></p>

WebPageTest APIを使ったメトリクスについて

----

## Three Ways to Test Angular 2 Components – Angular 2
[vsavkin.com/three-ways-to-test-angular-2-components-dcea8e90bd8d](https://vsavkin.com/three-ways-to-test-angular-2-components-dcea8e90bd8d "Three Ways to Test Angular 2 Components – Angular 2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AngularJS 2のコンポーネントをテストする方法について

----

## You SHOULD Learn Vanilla JavaScript Before JS Frameworks - Snipcart
[snipcart.com/blog/learn-vanilla-javascript-before-using-js-frameworks](https://snipcart.com/blog/learn-vanilla-javascript-before-using-js-frameworks "You SHOULD Learn Vanilla JavaScript Before JS Frameworks - Snipcart")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">thought</span></p>

フレームワークを学ぶ前にJavaScriptを学ぼうという話

----

## jsdoc-to-assert を試す – アカベコマイリ
[akabeko.me/blog/2016/08/jsdoc-to-assert/](http://akabeko.me/blog/2016/08/jsdoc-to-assert/ "jsdoc-to-assert を試す – アカベコマイリ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

jsdoc-to-assertでのランタイムassertの導入について

----

## 型定義ベースのアサーションライブラリ types-assert を書いた - Qiita
[qiita.com/KeitaMoromizato/items/e49185a0cd03c6cb8b3a](http://qiita.com/KeitaMoromizato/items/e49185a0cd03c6cb8b3a "型定義ベースのアサーションライブラリ types-assert を書いた - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

TypeScriptの型定義ファイルを使ったassertionライブラリ

- [KeitaMoromizato/types-assert: type-assert is dynamic type assertion library](https://github.com/KeitaMoromizato/types-assert "KeitaMoromizato/types-assert: type-assert is dynamic type assertion library")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## From MVC to Flux - JS Monthly London - YouTube
[www.youtube.com/watch?v=p8tqhf5qKOI](https://www.youtube.com/watch?v=p8tqhf5qKOI "From MVC to Flux - JS Monthly London - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span></p>

改めてFluxとはどういうコンセプトなのか、同様のコアコンセプトを持つReduxについての紹介

- [From MVC to Flux - Pusher Blog](https://blog.pusher.com/from-mvc-to-flux/ "From MVC to Flux - Pusher Blog")

----

## thejameskyle/itsy-bitsy-data-structures: All the things you didn&#x27;t know you wanted to know about data structures
[github.com/thejameskyle/itsy-bitsy-data-structures](https://github.com/thejameskyle/itsy-bitsy-data-structures "thejameskyle/itsy-bitsy-data-structures: All the things you didn't know you wanted to know about data structures")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アルゴリズム</span> <span class="jser-tag">document</span></p>

JavaScriptでリスト、ハッシュテーブル、スタックなどのデータ構造についての実装と解説リポジトリ。
それぞれの探索のコストや特徴などの解説がコメントに書かれている

- [React Rally Day 2 - YouTube](https://www.youtube.com/watch?v=nI0cQ-2YR1I "React Rally Day 2 - YouTube")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## SAM - State | Action | Model
[sam.js.org/](http://sam.js.org/ "SAM - State | Action | Model")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span> <span class="jser-tag">デザインパターン</span></p>

SAM (State-Action-Model)についてのドキュメントサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## babel/babel-minify: Babel preset for minification (Alpha)
[github.com/babel/babel-minify](https://github.com/babel/babel-minify "babel/babel-minify: Babel preset for minification (Alpha)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

Babelのminify plugin preset

----

## google/closure-compiler-js: Package for the JS version of closure-compiler for use via npm
[github.com/google/closure-compiler-js](https://github.com/google/closure-compiler-js "google/closure-compiler-js: Package for the JS version of closure-compiler for use via npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Closure Compilerの一部機能を使えるツール。JavaScriptへのコンパイル済みファイルを含んでいるので、Javaを必要としない。

----

## reactjs/react-docgen: A CLI and toolbox to extract information from React component files for documentation generation purposes.
[github.com/reactjs/react-docgen](https://github.com/reactjs/react-docgen "reactjs/react-docgen: A CLI and toolbox to extract information from React component files for documentation generation purposes.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

ReactのpropTypesなどをパースしてASTとして取得できるライブラリ/CLI

----

## pakastin/redom: Tiny DOM library
[github.com/pakastin/redom](https://github.com/pakastin/redom "pakastin/redom: Tiny DOM library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

DOM APIを使った小さなコンポーネントライブラリ

----

## nolanlawson/slow-deps: 🐌 Measure which dependencies in a project are slowest to npm install
[github.com/nolanlawson/slow-deps](https://github.com/nolanlawson/slow-deps "nolanlawson/slow-deps: 🐌 Measure which dependencies in a project are slowest to npm install")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

npmの依存モジュールがそれぞれどれくらいのインストール時間やサイズなのかを計測出来るツール

----
<h1 class="site-genre">書籍関係</h1>

----

## Fluent JavaScript | PACKT Books
[www.packtpub.com/web-development/fluent-javascript](https://www.packtpub.com/web-development/fluent-javascript "Fluent JavaScript | PACKT Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年4月6日発売

- [Amazon | Fluent JavaScript \[Kindle edition\] by Callum Rimmer, Lucian Lature | Languages &amp;amp; Tools | Kindleストア](https://www.amazon.co.jp/dp/B01F7HCB0C/ "Amazon | Fluent JavaScript \[Kindle edition\] by Callum Rimmer, Lucian Lature | Languages &amp;amp; Tools | Kindleストア")

----
