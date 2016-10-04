---
title: "2016-10-03のJS: Vue.js 2.0、Babel 6.17.0、複雑なJavaScript"
author: azu
layout: post
date : 2016-10-03T09:49
category: JSer
tags:
    - Vue
    - Babel
    - JavaScript
    - DDD

---

JSer.info #299 Vue.js 2.0がリリースされました。

- [Vue 2.0 is Here! – The Vue Point – Medium](https://medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8)

2.0では[snabbdom](https://github.com/snabbdom/snabbdom "snabbdom")をforkしたVirtual DOMを導入しているため、要素の更新やライフサイクル周りが変更されています。
(一方、[snabbdom](https://github.com/snabbdom/snabbdom "snabbdom")自体は[cycle.jsの人達がcollaborator](https://github.com/snabbdom/snabbdom/issues/164#issuecomment-248549455)になりました)

- [2.0 Changes · Issue #2873 · vuejs/vue](https://github.com/vuejs/vue/issues/2873)
- [Vue.js 2.0のFeaturesを訳してみる - Qiita](http://qiita.com/prismrism/items/66a9dfc31139326911d8)
- [Vue1.0からVue2.0でハマったこととか - Qiita](http://qiita.com/tanshio/items/88e29877671d5d9f1067 "Vue1.0からVue2.0でハマったこととか - Qiita")

また、1.xからのマイグレーションヘルパーとガイドが公開されています。

- [vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0](https://github.com/vuejs/vue-migration-helper "vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0")
- [Migration from Vue 1.x - vue.js](http://vuejs.org/guide/migration.html "Migration from Vue 1.x - vue.js")

----

Babel [6.17.0](https://github.com/babel/babel/releases/tag/v6.17.0 "6.17.0")がリリースされました。

[optimize-js](https://github.com/nolanlawson/optimize-js "optimize-js")関連の変更やECMAScript ProposalのStage変更を各presetに反映しています。

9月に行われたTC39 MTGによるStageの変更は次のページでまとめてあります。

- [ECMAScript proposal updates @ 2016-10 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

----

[複雑なJavaScriptアプリケーションを考えながら作る話](http://azu.github.io/slide/2016/react-meetup/large-scale-javascript.html)というスライドでは、数万行以上になる規模のJavaScriptアプリケーションにおける設計について書かれています。

FluxとCQRSについてや、1つのものが2つの役割をもつことから生まれる複雑さの掛け算を回避するアーキテクチャなどについて書かれています。

そこから生まれた実装である[Almin](https://github.com/almin/almin "Almin")を使った開発内容などのドキュメントは次のリポジトリにまとめられています。

- [azu/large-scale-javascript: 複雑なJavaScriptアプリケーションを作るために考えること](https://github.com/azu/large-scale-javascript)

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v6.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.7.0/](https://nodejs.org/en/blog/release/v6.7.0/ "Node v6.7.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.7.0リリース。
セキュリティアップデートが含まれる更新

----

## Vue 2.0 is Here! – The Vue Point – Medium
[medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8](https://medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8 "Vue 2.0 is Here! – The Vue Point – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.0リリース。
1.xからのマイグレーションヘルパーも公開されている。

- [vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0](https://github.com/vuejs/vue-migration-helper "vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0")
- [Migration from Vue 1.x - vue.js](http://vuejs.org/guide/migration.html "Migration from Vue 1.x - vue.js")

----

## 6.16.0 Released · Babel
[babeljs.io/blog/2016/09/28/6.16.0](https://babeljs.io/blog/2016/09/28/6.16.0 "6.16.0 Released · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.16.0リリース。
babel-coreが`parserOpts`と`generatorOpts`をサポートするなど

----

## Release v6.17.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.17.0](https://github.com/babel/babel/releases/tag/v6.17.0 "Release v6.17.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.17.0リリース。
ProposalのStage変更を反映、async generatorとobject rest-spreadをstage3へ、optimize-js関連の変更など

- [ECMAScript proposal updates @ 2016-10 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

----

## ESLint v3.7.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/09/eslint-v3.7.0-released](http://eslint.org/blog/2016/09/eslint-v3.7.0-released "ESLint v3.7.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v3.7.0リリース。
`--fix`対応のルールの追加など

- [ESLint v3.7.0 - Qiita](http://qiita.com/mysticatea/items/dd90aff81eeb92683c5d "ESLint v3.7.0 - Qiita")

----

## RE:DOM is now 1.0! – RE:DOM – Medium
[medium.com/re-dom/re-dom-is-now-1-0-58ec0328a59d](https://medium.com/re-dom/re-dom-is-now-1-0-58ec0328a59d "RE:DOM is now 1.0! – RE:DOM – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

RE:DOM 1.0リリース
合わせてRE:DOM向けのfake domであるNO:DOMも公開されてる

- [pakastin/redom: Tiny, but super fast DOM library with 100 % test coverage!](https://github.com/pakastin/redom "pakastin/redom: Tiny, but super fast DOM library with 100 % test coverage!")
- [pakastin/nodom: fake DOM for RE:DOM](https://github.com/pakastin/nodom "pakastin/nodom: fake DOM for RE:DOM")

----

## Release v0.33.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.33.0](https://github.com/facebook/flow/releases/tag/v0.33.0 "Release v0.33.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.33.0リリース。

----

## Release Notes for Safari Technology Preview Release 14 | WebKit
[webkit.org/blog/6969/release-notes-for-safari-technology-preview-release-14/](https://webkit.org/blog/6969/release-notes-for-safari-technology-preview-release-14/ "Release Notes for Safari Technology Preview Release 14 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 14リリース。
`URLSearchParams`の実装、safaridriverも含むようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Node.js debugging with Chrome DevTools (in parallel with browser JavaScript)
[blog.hospodarets.com/nodejs-debugging-in-chrome-devtools](https://blog.hospodarets.com/nodejs-debugging-in-chrome-devtools "Node.js debugging with Chrome DevTools (in parallel with browser JavaScript)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">node.js</span></p>

Node.jsをChromeの開発者ツールでデバッグする方法について。
設定を有効にする手順

----

## Master the DOM – Medium
[medium.com/@pakastin/master-the-dom-bc1a2a06089b](https://medium.com/@pakastin/master-the-dom-bc1a2a06089b "Master the DOM – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">tutorial</span></p>

DOM APIでのDOM Treeの基本的な操作を見ていく話。

----

## Common CSS Mistakes (And How To Fix Them)
[blog.mariano.io/common-css-mistakes-and-how-to-fix-them-8ee0f5e88d64](https://blog.mariano.io/common-css-mistakes-and-how-to-fix-them-8ee0f5e88d64 "Common CSS Mistakes (And How To Fix Them)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSSのよくある間違いと修正方法

----

## requestAnimationFrame とタイマーの今更な比較とデモ ::ハブろぐ
[havelog.ayumusato.com/develop/javascript/e725-timer\_vs\_raf.html](https://havelog.ayumusato.com/develop/javascript/e725-timer_vs_raf.html "requestAnimationFrame とタイマーの今更な比較とデモ ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

`requestAnimationFrame`と`setTimeout`の比較。
`setTimeout`は細かい処理でも影響を受けやすいという話

----

## hemanth/es-next: stage-0 to stage-4 ECMAscript proposals.
[github.com/hemanth/es-next](https://github.com/hemanth/es-next "hemanth/es-next: stage-0 to stage-4 ECMAscript proposals.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

ECMAScript proposalsのStage別まとめ。
それぞれに小さなサンプルコードが書かれている。

----

## Loading Polyfills Only When Needed — Philip Walton
[philipwalton.com/articles/loading-polyfills-only-when-needed/](https://philipwalton.com/articles/loading-polyfills-only-when-needed/ "Loading Polyfills Only When Needed — Philip Walton")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

polyfillをサポートしてない環境だけで動的に読み込みたいという話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 複雑なJavaScriptアプリケーションを考えながら作る話
[azu.github.io/slide/2016/react-meetup/large-scale-javascript.html](http://azu.github.io/slide/2016/react-meetup/large-scale-javascript.html "複雑なJavaScriptアプリケーションを考えながら作る話")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span> <span class="jser-tag">CQRS</span> <span class="jser-tag">DDD</span></p>

JavaScriptで複雑なアプリケーションを作る場合にどのように考えるかというスライド。
ドメインモデルをどのように考えて作っていくかについて。 Babel、React、Almin、PostCSSがベース。

- [azu/large-scale-javascript: 複雑なJavaScriptアプリケーションを作るために考えること](https://github.com/azu/large-scale-javascript "azu/large-scale-javascript: 複雑なJavaScriptアプリケーションを作るために考えること")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## CodePen - React ES6 lifecycles
[codepen.io/netsi1964/full/NRgyZX/](http://codepen.io/netsi1964/full/NRgyZX/ "CodePen - React ES6 lifecycles")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span></p>

Reactのライフサイクルのまとめ。
実際に動くコードがドキュメントになっていて、動作をさせながらライフサイクルメソッドの実行順について見ることができる

----

## Web Platform Feature Availability
[paulirish.github.io/web-feature-availability/](https://paulirish.github.io/web-feature-availability/ "Web Platform Feature Availability")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">browser</span></p>

CanIUseとStatCounterを使いある機能がどれぐらいのプラットフォームで利用できるかを一覧できるサイト

----

## React Status: A Free, Weekly Email Newsletter
[react.statuscode.com/](http://react.statuscode.com/ "React Status: A Free, Weekly Email Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">news</span> <span class="jser-tag">mail</span></p>

Reactについてを扱うWeeklyメールマガジン

----

## Fix and prevent known vulnerabilities in Node.js apps | Snyk
[snyk.io/](https://snyk.io/ "Fix and prevent known vulnerabilities in Node.js apps | Snyk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">webservice</span></p>

Node.js appの既知の脆弱性などを通知、修正などを行うサービス。
CIで自動的にチェックできる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mkwtys/bundle-size: Show bundle file size of npm packages
[github.com/mkwtys/bundle-size](https://github.com/mkwtys/bundle-size "mkwtys/bundle-size: Show bundle file size of npm packages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

指定したパッケージのファイルサイズを出力できるCLI。
Environmentを指定できるのでdevelopmentとproductionのファイルサイズをminify、gzip済みで比較できる

----

## krasimir/navigo: A simple vanilla JavaScript router with a fallback for older browsers
[github.com/krasimir/navigo](https://github.com/krasimir/navigo "krasimir/navigo: A simple vanilla JavaScript router with a fallback for older browsers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

シンプルなルーターライブラリ。
マッピングに正規表現も利用できる

----
<h1 class="site-genre">書籍関係</h1>

----

## TypeScript Design Patterns - O&#x27;Reilly Media
[shop.oreilly.com/product/9781785280832.do](http://shop.oreilly.com/product/9781785280832.do "TypeScript Design Patterns - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">デザインパターン</span> <span class="jser-tag">book</span></p>

TypeScriptでのデザインパターン本

----
