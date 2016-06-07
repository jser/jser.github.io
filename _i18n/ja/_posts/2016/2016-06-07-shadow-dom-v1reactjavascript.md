---
title: "2016-06-07のJS: Shadow DOM v1、React近況、JavaScriptのプラグイン設計本"
author: azu
layout: post
date : 2016-06-07T09:40
category: JSer
tags:
    - WebComponent
    - React
    - JavaScript
    - plguin
    - book

---



JSer.info #282 - 

----
<h1 class="site-genre">ヘッドライン</h1>

----

## V8 JavaScript Engine: Release 5.2
[v8project.blogspot.com/2016/06/release-52.html](http://v8project.blogspot.com/2016/06/release-52.html "V8 JavaScript Engine: Release 5.2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.2リリース。
 Exponentiation operator `**`のサポート、`Array.isArray`、`in` operator、`Function#bind`のパフォーマンス改善など

----
<h1 class="site-genre">アーティクル</h1>

----

## Getting Started with TDD in React - Semaphore
[semaphoreci.com/community/tutorials/getting-started-with-tdd-in-react](https://semaphoreci.com/community/tutorials/getting-started-with-tdd-in-react "Getting Started with TDD in React - Semaphore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

Enzymeを使ったReact Componentのテストについて

----

## What&#x27;s New in Shadow DOM v1 (by examples) — hayato.io
[hayato.io/2016/shadowdomv1/](http://hayato.io/2016/shadowdomv1/ "What's New in Shadow DOM v1 (by examples) — hayato.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Shadow DOM v0とv1の違いについて。
[@shadow_hayato](https://twitter.com/shadow_hayato "@shadow_hayato")さん(仕様作庭者)によるコード例を元にした解説。

- [Shadow DOM v1: Status updates - Google グループ](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/BUGxw_Yx5Lo "Shadow DOM v1: Status updates - Google グループ")

----

## Chromeのヘッドレスブラウザがやってくる。というわけで試してみた。 - Qiita
[qiita.com/devneko/items/51f2e114a7e0b3389435](http://qiita.com/devneko/items/51f2e114a7e0b3389435 "Chromeのヘッドレスブラウザがやってくる。というわけで試してみた。 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chromeのヘッドレスブラウザについて

- [Issues - chromium - An open-source project to help move the web forward. - Monorail](https://bugs.chromium.org/p/chromium/issues/list?q=label:Proj-Headless "Issues - chromium - An open-source project to help move the web forward. - Monorail")

----

## Infinite collections with ES6 generators - Advanced Web Machinery
[advancedweb.hu/2016/05/31/infinite-collections-with-es6-generators/](https://advancedweb.hu/2016/05/31/infinite-collections-with-es6-generators/ "Infinite collections with ES6 generators - Advanced Web Machinery")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Iteratorを使った無限リストについて

- [sashee/gentoo: Tools for ES6 generators](https://github.com/sashee/gentoo "sashee/gentoo: Tools for ES6 generators")

----

## Why we chose MobX over Redux for Spectacle Editor
[formidable.com/blog/2016/06/02/why-we-chose-mobx-over-redux-for-spectacle-editor/](http://formidable.com/blog/2016/06/02/why-we-chose-mobx-over-redux-for-spectacle-editor/ "Why we chose MobX over Redux for Spectacle Editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span></p>

Reduxとかと同じくアプリケーションのStateを管理するMobXの特徴についての紹介

- [mobxjs/mobx: Simple, scalable state management.](https://github.com/mobxjs/mobx "mobxjs/mobx: Simple, scalable state management.")

----

## Creating A Living Style Guide: A Case Study – Smashing Magazine
[www.smashingmagazine.com/2016/05/creating-a-living-style-guide-case-study/](https://www.smashingmagazine.com/2016/05/creating-a-living-style-guide-case-study/ "Creating A Living Style Guide: A Case Study – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

スタイルガイドのケーススタディ

----

## Improving Your CSS with Parker – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts
[csswizardry.com/2016/06/improving-your-css-with-parker/](http://csswizardry.com/2016/06/improving-your-css-with-parker/ "Improving Your CSS with Parker – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSSの解析ツールであるParkerについて

- [katiefenn/parker: Stylesheet analysis tool.](https://github.com/katiefenn/parker/ "katiefenn/parker: Stylesheet analysis tool.")

----

## webpackのDLLバンドルを使ってビルドを速くする - Qiita
[qiita.com/pirosikick/items/c77db84dbed4c447a6fe](http://qiita.com/pirosikick/items/c77db84dbed4c447a6fe "webpackのDLLバンドルを使ってビルドを速くする - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">performance</span></p>

webpackのビルド速度の改善について。
vendarライブラリだけ別にビルドし読み込んで使うDLLバンドル、`cacheDirectory`、`externals`との違いについてなど

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## The state of React.js 2016 // Speaker Deck
[speakerdeck.com/koba04/the-state-of-react-dot-js-2016](https://speakerdeck.com/koba04/the-state-of-react-dot-js-2016 "The state of React.js 2016 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

Reactの最近の変更や今後の変更、非推奨になる予定の機能についてなど

- [第65回 HTML5とか勉強会 ー React最新情報 - YouTube](https://www.youtube.com/watch?v=C8bMahvTkHA "第65回 HTML5とか勉強会 ー React最新情報 - YouTube")

----

## ReactEurope 2016 - Day 1 - YouTube
[www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A](https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A "ReactEurope 2016 - Day 1 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">動画</span></p>

ReactEurope 2016の動画まとめ

----

## Building React Applications with Idiomatic Redux - Course by @dan_abramov @eggheadio
[egghead.io/courses/building-react-applications-with-idiomatic-redux](https://egghead.io/courses/building-react-applications-with-idiomatic-redux "Building React Applications with Idiomatic Redux - Course by @dan\_abramov @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">動画</span> <span class="jser-tag">tutorial</span></p>

Redux作者によるReduxでアプリケーションを作るスクリーンキャスト

- [Dan Abramov - The Redux Journey at react-europe 2016 - YouTube](https://www.youtube.com/watch?v=uvAXVMwHJXU "Dan Abramov - The Redux Journey at react-europe 2016 - YouTube")


----

## Next Vue.js 2.0 // Speaker Deck
[speakerdeck.com/kazupon/next-vue-dot-js-2-dot-0](https://speakerdeck.com/kazupon/next-vue-dot-js-2-dot-0 "Next Vue.js 2.0 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

Vue.js 2.0のレンダリングフローについて

----

## Flow vs TypeScript
[djcordhose.github.io/flow-vs-typescript/2016\_hhjs.html#/](http://djcordhose.github.io/flow-vs-typescript/2016_hhjs.html#/ "Flow vs TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">flowtype</span></p>

TypeScriptとFlowTypeの型指定の比較についてのスライド

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## HyperDev
[hyperdev.com/](https://hyperdev.com/ "HyperDev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>

サーバも書けるJSFiddle的なサービス。
Node.jsでサーバ側、HTML/CSS/JSなフロントも一緒に書けるエディタサービス

----

## Front-end Hyperpolyglot
[jeffcarp.github.io/frontend-hyperpolyglot/](http://jeffcarp.github.io/frontend-hyperpolyglot/ "Front-end Hyperpolyglot")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

React/Angular1,2/Ember/Polymer/Vueのテンプレートの書き方比較

- [Programming Languages - Hyperpolyglot](http://hyperpolyglot.org/ "Programming Languages - Hyperpolyglot")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## epoberezkin/ajv: The fastest JSON schema Validator. Supports v5 proposals
[github.com/epoberezkin/ajv](https://github.com/epoberezkin/ajv "epoberezkin/ajv: The fastest JSON schema Validator. Supports v5 proposals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

JSON Schema validatorライブラリ

----

## MJB-code6/SkyPort: Add offline functionality to your web app
[github.com/MJB-code6/SkyPort](https://github.com/MJB-code6/SkyPort "MJB-code6/SkyPort: Add offline functionality to your web app")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">library</span></p>

Service Workerを使ったオフラインモードを実現するライブラリ。

----

## Frend — A collection of accessible, modern front-end components.
[frend.co/](http://frend.co/ "Frend — A collection of accessible, modern front-end components.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">WAI-ARIA</span></p>

AccessibleなDOM UIを実現するためのJavaScriptライブラリ。CSSフレームワークのように特定のクラスを付けた要素にWAI-ARIAの属性を付加していく。

----

## GoogleChrome/lighthouse: auditing and performance metrics for Progressive Web Apps
[github.com/GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse "GoogleChrome/lighthouse: auditing and performance metrics for Progressive Web Apps")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Service Workerを使ってのオフライン対応の有無、Speed IndexなどのロードパフォーマンスなどProgressive Web Appsに関する計測ツール

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript Plugin Architectureというプラグイン設計について学ぶ無料の電子書籍を書いた | Web Scratch
[efcl.info/2016/06/06/JavaScript-Plugin-Architecture/](http://efcl.info/2016/06/06/JavaScript-Plugin-Architecture/ "JavaScript Plugin Architectureというプラグイン設計について学ぶ無料の電子書籍を書いた | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ebook</span></p>

JavaScriptのプラグイン設計のケーススタディ本。
jQuery、ESLint、Connect、gulp、Reduxなどのプラグインの仕組みを実装しながら学ぶ電子書籍

- [azu/JavaScript-Plugin-Architecture: JavaScriptプラグインアーキテクチャの本](https://github.com/azu/JavaScript-Plugin-Architecture "azu/JavaScript-Plugin-Architecture: JavaScriptプラグインアーキテクチャの本")

----
