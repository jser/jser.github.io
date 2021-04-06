---
title: "2021-04-06のJS: TypeScript 4.3 Beta、hls.js v1.0.0(Apple Low-Latency HLS)、Storybook 6.2"
author: "azu"
layout: post
date : 2021-04-05T22:08:25.064Z
category: JSer
tags:
- Tools
- node.js
- TypeScript
- Vue
- license

---

JSer.info #534 - TypeScript 4.3 Betaがリリースされました。

- [Announcing TypeScript 4.3 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-3-beta/)

今までは、getterとsetterは同じ型であることが強制されていましたが、setterにgetterより幅広い型を指定できるようになっています。また、継承したメソッドをoverrideしていることを意味する`override`キーワードの追加し、`--noImplicitOverride`でチェックできるようになっています。

その他には、Template String Typeの改善、一部不完全だったPrivate Class Elements(fields/methods/accessors)のサポートが改善されています。
Private Class ElementsのサポートはRuntimeの変更も含まれるため、これに合わせてruntimeのライブラリであるtslib 2.2.0がリリースされています。

- [Release tslib 2.2.0 · microsoft/tslib](https://github.com/microsoft/tslib/releases/2.2.0)

また、Promiseオブジェクトを条件式に渡してしまうミスのチェックできるようになり、`static` Index Signaturesのサポートも追加されています。

----

HLS(HTTP Live Streaming)を扱うライブラリであるhls.js 1.0.0がリリースされました。

- [Release v1.0.0 · video-dev/hls.js](https://github.com/video-dev/hls.js/releases/tag/v1.0.0)

1.0.0では低遅延の動画を扱うApple Low-Latency HLSがサポートされています。
また、fmp4 streamのサポート改善、コードベースをTypeScriptに書きなおしなども含まれています。
破壊的な変更として`backBufferLength`のデフォルト値の変更、イベントのシグネチャの変更なども含まれています。

リリースに合わせてマイグレーションガイドも公開されています。

- [hls.js/MIGRATING.md at master · video-dev/hls.js](https://github.com/video-dev/hls.js/blob/master/MIGRATING.md#migrating-from-hlsjs-0x-to-1x)

----

Storybook 6.2がリリースされました。

- [Storybook 6.2](https://storybook.js.org/blog/storybook-6-2/)

Storybook 6.2ではVue 3とSvelteのサポートが追加されいます。

- [Storybook for Vue 3](https://storybook.js.org/blog/storybook-vue3/)
- [Storybook for Svelte](https://storybook.js.org/blog/storybook-for-svelte/)

Yarn 2のPnP/npm 7/ESMのサポート、webpack 5をopt-inでサポートしています。

- [Storybook for Webpack 5](https://storybook.js.org/blog/storybook-for-webpack-5/)

また、Controls addonが改善され、JSON editorやcolor pickerなどの機能が追加されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v12.22.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.22.0/](https://nodejs.org/en/blog/release/v12.22.0/ "Node v12.22.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.22.0リリース。
`--http-parser=legacy`を非推奨化、ES ModulesをStable化、`NAPI_VERSION`を`8`に変更。
`v8.takeCoverage()`、`v8.stopCoverage()`、`worker.performance.eventLoopUtilization()`の追加など


----

## Release v6.0.0 · typicode/husky
[github.com/typicode/husky/releases/tag/v6.0.0](https://github.com/typicode/husky/releases/tag/v6.0.0 "Release v6.0.0 · typicode/husky")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">license</span> <span class="jser-tag">ReleaseNote</span></p>

husky 6.0.0リリース。
5.0.0はParity Publicライセンスとしてリリースされ、30日経過したので6.0.0ではMITライセンスとなった。


----

## Node v15.13.0 (Current) | Node.js
[nodejs.org/en/blog/release/v15.13.0/](https://nodejs.org/en/blog/release/v15.13.0/ "Node v15.13.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 15.13.0リリース。
ウェブとの互換性を目的として`buffer`モジュールに`btoa`と`atob`メソッドを実装など


----

## Announcing TypeScript 4.3 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-3-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-3-beta/ "Announcing TypeScript 4.3 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.3 Betaリリース。
setterにgetterとは異なる型を指定できるように、`override`キーワードの追加、Template String Typeの改善。
Private Class Elements(fields/methods/accessors)のサポート、Promiseオブジェクトを条件式に渡してしまうミスのチェックを追加。
その他には、`static` Index Signatureのサポートなど


----

## Release v5.30.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.30.0](https://github.com/webpack/webpack/releases/tag/v5.30.0 "Release v5.30.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5.30.0リリース。
`cache.type: "memory"`でwatch中に`[contenthash]`などを使うと、ファイル変更ごとにゴミがメモリに貯まる問題の改善。
`cache.maxGenerations`と`cache.maxAge`で不要となったキャッシュを削除できるように

- [SourceMapDevTool plugin leaks memory in watch mode · Issue #12947 · webpack/webpack](https://github.com/webpack/webpack/issues/12947 "SourceMapDevTool plugin leaks memory in watch mode · Issue #12947 · webpack/webpack")
- [memory usage improvements, add GC support for memory cache, persistent cache only mode by sokra · Pull Request #12990 · webpack/webpack](https://github.com/webpack/webpack/pull/12990 "memory usage improvements, add GC support for memory cache, persistent cache only mode by sokra · Pull Request #12990 · webpack/webpack")

----

## Release v1.0.0 · video-dev/hls.js
[github.com/video-dev/hls.js/releases/tag/v1.0.0](https://github.com/video-dev/hls.js/releases/tag/v1.0.0 "Release v1.0.0 · video-dev/hls.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HLS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

HLS.js 1.0.0リリース。
Apple Low-Latency HLSのサポート、fmp4 streamのサポート改善、コードベースをTypeScriptに書きなおしなど。
破壊的な変更として`backBufferLength`のデフォルト値の変更、イベントのシグネチャの変更など

- [hls.js/MIGRATING.md at master · video-dev/hls.js](https://github.com/video-dev/hls.js/blob/master/MIGRATING.md#migrating-from-hlsjs-0x-to-1x "hls.js/MIGRATING.md at master · video-dev/hls.js")

----

## Proposal for dropping ie11 support in Vue 3 · Discussion #296 · vuejs/rfcs
[github.com/vuejs/rfcs/discussions/296](https://github.com/vuejs/rfcs/discussions/296 "Proposal for dropping ie11 support in Vue 3 · Discussion #296 · vuejs/rfcs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">IE</span> <span class="jser-tag">proposal</span></p>

Vue 3ではIE 11のサポートをしないというRFC。
代わりにVue 2.xへ3.xの機能をバックポートすることに注力するというProposal。


----

## Release v2.0.0 · js-reporters/js-reporters
[github.com/js-reporters/js-reporters/releases/tag/v2.0.0](https://github.com/js-reporters/js-reporters/releases/tag/v2.0.0 "Release v2.0.0 · js-reporters/js-reporters")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">spec</span></p>

JavaScriptのテストフレームワークのレポートの共通インターフェイスを定義する目的のjs-reporters 2.0.0リリース。
`SummaryReporter`の実装、Proposalの更新など


----

## Storybook 6.2
[storybook.js.org/blog/storybook-6-2/](https://storybook.js.org/blog/storybook-6-2/ "Storybook 6.2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 6.2リリース。
Vue 3とSvelteサポート、Yarn 2のPnp/npm 7/ESMのサポート、webpack 5をopt-inでサポート。
Controls addonにJSON editorやcolor pickerの追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## React Hooksのみでドラッグ＆ドロップの並び替えを実装する
[zenn.dev/uttk/articles/b90454baec68c8](https://zenn.dev/uttk/articles/b90454baec68c8 "React Hooksのみでドラッグ＆ドロップの並び替えを実装する")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

Reactで要素の並び替えをD&Dする実装についての記事。
マウスイベントとCSSを使ったD&D、要素の重なりの判定、要素の入れ替えのアニメーションなどを実装しながら見ていく記事


----

## 特定の端末のみで起こる WebView プチフリーズを Tracing を利用して追った話 - SmartNews Engineering Blog
[developer.smartnews.com/blog/2021/03/chrome\_tracing/](https://developer.smartnews.com/blog/2021/03/chrome_tracing/ "特定の端末のみで起こる WebView プチフリーズを Tracing を利用して追った話 - SmartNews Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">webview</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

WebViewのパフォーマンスデバッグについての記事。
ChromeのRemote Inspectを使ってデバイスに接続し、プロファイルやTracingを使ったボトルネックの調査方法について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Organize Kubernetes manifests in JavaScript | Kosko
[kosko.dev/](https://kosko.dev/ "Organize Kubernetes manifests in JavaScript | Kosko")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">kubernetes</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

kubernetesのmanifestをJavaScript/TypeScriptで書けるツール。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mistlog/typetype: A programming language designed for typescript type generation
[github.com/mistlog/typetype](https://github.com/mistlog/typetype "mistlog/typetype: A programming language designed for typescript type generation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScriptの型書くDSLのパーサとジェネレーター。
Conditional Typeを表現する`if`、Mapped Typesを表現する`for`などを使って型定義を書ける。
パーサはreact-pegを使い、パースしたASTからBabelを通してTSのコードを出力している

- [mistlog/react-peg: A react style parser generator based on PEG.js](https://github.com/mistlog/react-peg "mistlog/react-peg: A react style parser generator based on PEG.js")

----

## egoist/esbuild-register: Transpile JSX, TypeScript and esnext features on the fly with esbuild
[github.com/egoist/esbuild-register](https://github.com/egoist/esbuild-register "egoist/esbuild-register: Transpile JSX, TypeScript and esnext features on the fly with esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span></p>

esbuildを使ったruntimeでの変換ツール。
@babel/registerやts-node/registerのように`--require`に指定して変換処理をする


----

## FicusJS - a set of lightweight functions for developing applications using web components
[docs.ficusjs.org/](https://docs.ficusjs.org/ "FicusJS - a set of lightweight functions for developing applications using web components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

Web Componentsでアプリケーションを開発する目的のライブラリセット。
コンポーネントの作成、`uhtml`/`lit-html`/`htm`などを使ったレンダリング、Storeでのステート管理などの機能を提供する

- [Developing Without a Build (1): Introduction - DEV Community 👩‍💻👨‍💻](https://dev.to/open-wc/developing-without-a-build-1-introduction-26ao "Developing Without a Build (1): Introduction - DEV Community 👩‍💻👨‍💻")

----
<h1 class="site-genre">書籍関係</h1>

----

## Accessible Vue – The Why and How of building inclusive apps in Vue.js
[accessible-vue.com/](https://accessible-vue.com/ "Accessible Vue – The Why and How of building inclusive apps in Vue.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">book</span></p>

ウェブアクセシビリティとVueでの実装についての書籍

- [Accessible Vue by Marcus Herrmann \[Leanpub PDF/iPad/Kindle\]](https://leanpub.com/accessible-vue "Accessible Vue by Marcus Herrmann \[Leanpub PDF/iPad/Kindle\]")

----
