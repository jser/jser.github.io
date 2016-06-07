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

JSer.info #282 - [What's New in Shadow DOM v1 (by examples) — hayato.io](http://hayato.io/2016/shadowdomv1/ "What&#39;s New in Shadow DOM v1 (by examples) — hayato.io")という記事では、Shadow DOM仕様の策定者でもある[@shadow_hayato](https://twitter.com/shadow_hayato "@shadow_hayato")さんよるShadow DOM v0とv1の違いについて解説されています。

closed shadow rootという概念の追加や、v1では`/deep/`や`::shadow`は利用できなくなり、
slot(`::slotted`)を利用する点など色々な違いがあります。

- [webcomponents/Shadow-DOM-Cascade-Order-in-v1.md at gh-pages · w3c/webcomponents](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/Shadow-DOM-Cascade-Order-in-v1.md "webcomponents/Shadow-DOM-Cascade-Order-in-v1.md at gh-pages · w3c/webcomponents")

コード例を中心に解説されているので、Shadow DOMに興味がある人は見ておくといいです。

-----

[ReactEurope](https://www.react-europe.org/ "ReactEurope")が開催され、その動画が公開されています。

- [ReactEurope - YouTube](https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A/feed "ReactEurope - YouTube")

また、[The state of React.js 2016 // Speaker Deck](https://speakerdeck.com/koba04/the-state-of-react-dot-js-2016 "The state of React.js 2016 // Speaker Deck")というスライドではここ半年ぐらいのReactの変化などについてまとめられています。

Reactの動向はReact Coreチームのミーティングノートが公開されているので、こちらも合わせて参照するといいです。

- [reactjs/core-notes: Weekly meeting notes from the React core team](https://github.com/reactjs/core-notes "reactjs/core-notes: Weekly meeting notes from the React core team")

----

[JavaScript Plugin Architecture](https://github.com/azu/JavaScript-Plugin-Architecture "JavaScript Plugin Architecture")という電子書籍では、JavaScriptのライブラリやツールにおけるプラグイン設計について書かれています。

- [JavaScript Plugin Architectureというプラグイン設計について学ぶ無料の電子書籍を書いた | Web Scratch](http://efcl.info/2016/06/06/JavaScript-Plugin-Architecture/ "JavaScript Plugin Architectureというプラグイン設計について学ぶ無料の電子書籍を書いた | Web Scratch")

現時点では、[jQuery](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/jQuery/README.md)、[ESLint](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/ESLint/README.md)、[Connect](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/connect/README.md)、[gulp](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/gulp/README.md)、[Redux](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/Redux/README.md)のプラグインについてそれぞれプラグインの仕組み自体を実装しつつ解説した内容が書かれています。

全部まとめて読むというよりは気になったものをパッと見るリファレンス的な感じになっています。

----
<h1 class="site-genre">ECMAScript便り〆</h1>

5月に行われた[TC39 Meeting](https://github.com/rwaldron/tc39-notes "TC39 Meeting")の記録が公開されたので、主要なできごとを簡単に書いておきます。
詳しくは[ミーティングノート](https://github.com/rwaldron/tc39-notes/tree/master/es7/2016-05 "tc39-notes/es7/2016-05 at master · rwaldron/tc39-notes")を読んでください

- [tc39/proposals: Tracking ECMAScript Proposals | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/13/tc39-proposals-tracking-ecmascript-proposals)
  - 今までProposalは[tc39/ecma262](https://github.com/tc39/ecma262 "tc39/ecma262")にまとめがありましたが、単独のリポジトリに移動しました
- [Arrive TC39 meeting notes for 2016-05 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/06/07/arrive-tc39-meeting-notes-for-2016-05)
  - 2016年5月のミーティングノートが公開されました
  - 6月中旬にはECMAScript 2016の正式リリースが控えています。
- [[Stage 0] ljharb/proposal-promise-finally: ECMAScript Proposal, specs, and reference implementation for Promise.prototype.finally | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-0-ljharb-proposal-promise-finally-ecmascript-proposal-specs-and-reference-implementation-for-promise-prototype-finally)
  - `Promise#finally` のProposalがStage 0になりました
- [[Stage 4] Per May 2016 TC39 consensus, String#{padStart,padEnd} is now stage 4! by ljharb · Pull Request #581 · tc39/ecma262 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-4-per-may-2016-tc39-consensus-string-padstart-padend-is-now-stage-4-by-ljharb-pull-request-581-tc39-ecma262)
- [[Stage 4] Per May 2016 TC39 consensus, Object.getOwnPropertyDescriptors is now stage 4! by ljharb · Pull Request #582 · tc39/ecma262 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-4-per-may-2016-tc39-consensus-object-getownpropertydescriptors-is-now-stage-4-by-ljharb-pull-request-582-tc39-ecma262)
  - `String#{padStart,padEnd}`と`Object.getOwnPropertyDescriptors`がStage 4となりES2017に入る
- [Cancelable promises | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/26/cancelable-promises)
  - Promiseのキャンセル方法としてCancelTokenと`Promise#cancel`の2種類が提案され、議論が開始された
  - [zenparsing/es-cancel-token: Cancel Tokens for ECMAScript](https://github.com/zenparsing/es-cancel-token)
    - ES Observableにも関わってくるので、[Remove forEach and add "subscribe" overload by zenparsing · Pull Request #97 · zenparsing/es-observable](https://github.com/zenparsing/es-observable/pull/97 "Remove forEach and add &#34;subscribe&#34; overload by zenparsing · Pull Request #97 · zenparsing/es-observable")も参照。
  - [domenic/cancelable-promise: Cancelable promises proposal for JavaScript](https://github.com/domenic/cancelable-promise)

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
- [Issues · w3c/webcomponents](https://github.com/w3c/webcomponents/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Av1+label%3Ashadow-dom "Issues · w3c/webcomponents")


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
