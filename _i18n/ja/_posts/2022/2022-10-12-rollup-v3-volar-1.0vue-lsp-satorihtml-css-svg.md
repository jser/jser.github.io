---
title: "2022-10-12のJS: Rollup v3、Volar 1.0(Vue LSP)、Satori(HTML + CSS = SVG)"
author: "azu"
layout: post
date : 2022-10-12T07:49:16.919Z
category: JSer
tags:
- React
- Ember
- audio
- ESLint
- ECMAScript

---

JSer.info #613 - Rollup 3.0.0がリリースされました。

- [Release v3.0.0 · rollup/rollup](https://github.com/rollup/rollup/releases/tag/v3.0.0)
- [rollup.js#migration](https://rollupjs.org/guide/en/#migration)

破壊的な変更として、プラグインのAPIの変更、オプションの変更が行われています。
また、デフォルトで`import()`を維持するように変更、chunkのアルゴリズムの変更なども含まれています。
そのほかには、デフォルトでNode.jsのESMサポートとの相互運用性を改善するために`output.interop`/`output.exports`/`output.esModule`オプションのデフォルト値が変更されています。

基本的には`__esModule`というNode.jsが考慮しない(ESMとCJSの総合運用性のために使われていた)プロパティを減らす方向になっています。詳しい変更内容は次のPRを参照すると良さそうです。

- [[v3.0] Improve interop defaults by lukastaegert · Pull Request #4611 · rollup/rollup](https://github.com/rollup/rollup/pull/4611)

加えて、ECMAScript Proposal Stage 3の[Import Assertions](https://github.com/tc39/proposal-import-assertions)のサポートも追加されています。

---

VueテンプレートのIDEサポートなどを提供するVolar 1.0がリリースされました。

- [Volar 1.0 "Nika" Released! | The Vue Point](https://blog.vuejs.org/posts/volar-1.0.html)

`<template lang="pug">`のbuilt-inサポートを終了しプラグイン化されています。
`vue-tsc`が`--watch`と`--declaration --emitDeclarationOnly`をサポートしています。
また、コアモジュールがVueなどのフレームワークに依存しなくなるなり、サンプルとして[Svelte Langauge Server Example](https://github.com/johnsoncodehk/volar/tree/master/examples)が公開されています。

---

HTMLとCSSで書いたコードをSVG画像へと変換するSatoriというライブラリが公開されています。

- [vercel/satori: Enlightened library to convert HTML and CSS to SVG](https://github.com/vercel/satori)

OGP(OG)イメージのために、コンテンツに基づいた画像を生成することが増えています。
Puppeteerなどを利用すればHTMLとCSSで書いたデザインから画像(スクリーンショット)を再生することはできました。
しかし、ブラウザプロセスを立ち上げると時間がかかったりリソースの消費も大きいです。

そのため、SatoriではFlexboxのレイアウトエンジンを実装として知られる[Yoga](https://yogalayout.com/)のWasmビルド版を使い、HTMLとCSSのサブセットを実装しSVGを生成しています。

次の記事で詳しい解説が書かれています。

- [Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 2.0.0-rc.0 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-rc.0](https://github.com/vercel/swr/releases/tag/2.0.0-rc.0 "Release 2.0.0-rc.0 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-rc.0リリース。
破壊的変更としてmutationにおけるエラーが他のmutationやuseSWRに反映されないように変更。また、mutationがエラーをthrowするかを抑制できる`throwOnError`オプションを追加など


----

## ESLint v8.25.0 released - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2022/10/eslint-v8.25.0-released/](https://eslint.org/blog/2022/10/eslint-v8.25.0-released/ "ESLint v8.25.0 released - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.25.0リリース。
新しい設定ファイルでは、`.eslintignore`ファイルはサポートしなくなり、設定ファイル内の`ignores`フィールドで無視するファイルを指定するようになる変更。


----

## Chrome 107 beta - Chrome Developers
[developer.chrome.com/blog/chrome-107-beta/](https://developer.chrome.com/blog/chrome-107-beta/ "Chrome 107 beta - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 107 betaリリース。
`grid-template`でのtransitionのサポート、Screen Capture APIの改善、Resource Timingに`renderBlockingStatus`を追加。
Permissions policyのorigin指定に`*`を利用可能に、`<form>`要素が`rel`属性のサポートなど。
Origin TrialsとしてDeclarative PendingBeacon API、Permissions policyのunloadのサポートなど。
また`Expect-CT` HTTPヘッダを非推奨化など

- [resource-timing/Render\_Blocking\_Status.md at render-blocking-status-explainer · abinpaul1/resource-timing](https://github.com/abinpaul1/resource-timing/blob/render-blocking-status-explainer/Explainer/Render_Blocking_Status.md "resource-timing/Render\_Blocking\_Status.md at render-blocking-status-explainer · abinpaul1/resource-timing")

----

## Release v7.0.0 · capricorn86/happy-dom
[github.com/capricorn86/happy-dom/releases/tag/v7.0.0](https://github.com/capricorn86/happy-dom/releases/tag/v7.0.0 "Release v7.0.0 · capricorn86/happy-dom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Happy DOM v7.0.0リリース。
`CSSStyleDeclaration`のサポート改善、`Window.getComputedStyle()`のサポート改善、`CSSStyleSheet`のサポート改善など


----

## Release v3.0.0 · rollup/rollup
[github.com/rollup/rollup/releases/tag/v3.0.0](https://github.com/rollup/rollup/releases/tag/v3.0.0 "Release v3.0.0 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rollup</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup v3.0.0リリース。
破壊的な変更として、プラグインのAPIの変更、オプションの変更、デフォルトで`import()`を維持するように変更、chunkのアルゴリズムの変更など。
また、デフォルトでNode.jsのESMサポートとの相互運用性を改善、import assertionsのサポート、など

- [rollup.js migration](https://rollupjs.org/guide/en/#migration "rollup.js migration")

----
<h1 class="site-genre">アーティクル</h1>

----

## Evolving Ember’s Major Version Process
[blog.emberjs.com/evolving-embers-major-version-process/](https://blog.emberjs.com/evolving-embers-major-version-process/ "Evolving Ember’s Major Version Process")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">article</span></p>

Emberはメジャーリリース(破壊的変更)を少なくするという方針であったため、メジャーリリースの間隔が長くなっていた。この間隔が長くなると非推奨の機能に取り除くタイミングがわかりにくくなるなどの弊害があった。
そのため、予測可能なリズムとして6周ごとにマイナーリリース、18ヶ月ごとにメジャーリリースとする。
また`X.10`以降にはDeprecationを増やさない、メジャーリリースはDeprecationを削除するのみというルールと取り入れ、開発者がDeprecationにいつ対応するべきかを明確にする。


----

## Intl.Segmenter で和文の改行をいい感じにしてみる
[zenn.dev/notfounds/articles/58c465d4029dc1](https://zenn.dev/notfounds/articles/58c465d4029dc1 "Intl.Segmenter で和文の改行をいい感じにしてみる")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">article</span></p>

`Intl.Segmenter`を使った分かち書きを考慮した改行の実装について。
また、JavaScriptエンジンの実装による違いとHydrationでの差異を無視する方法について


----

## 10 best practices to containerize Node.js web applications with Docker | Snyk Blog
[snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/](https://snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/ "10 best practices to containerize Node.js web applications with Docker | Snyk Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Docker</span> <span class="jser-tag">article</span></p>

DockerベースのNode.jsのウェブアプリケーションのプラクティスについて。
Docker Imageの作成、Gracefull Shutdownの対応、不要な情報の削除などについて


----

## Volar 1.0 &quot;Nika&quot; Released! | The Vue Point
[blog.vuejs.org/posts/volar-1.0.html](https://blog.vuejs.org/posts/volar-1.0.html "Volar 1.0 \&quot;Nika\&quot; Released! | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span></p>

Volar 1.0リリース。
`<template lang="pug">`のbuilt-inサポートを終了しプラグイン化。
`vue-tsc`が`--watch`と`--declaration --emitDeclarationOnly`をサポート。
コアモジュールがVueなどのフレームワークに依存しなくなるなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## slash9494/react-modern-audio-player: 🔊 Simple, accessible and flexible audio player
[github.com/slash9494/react-modern-audio-player](https://github.com/slash9494/react-modern-audio-player "slash9494/react-modern-audio-player: 🔊 Simple, accessible and flexible audio player")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Reactで書かれた音楽プレイヤーコンポーネント


----

## leeoniya/uFuzzy: A tiny, efficient fuzzy search that doesn&#039;t suck
[github.com/leeoniya/uFuzzy](https://github.com/leeoniya/uFuzzy "leeoniya/uFuzzy: A tiny, efficient fuzzy search that doesn&#039;t suck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search </span> <span class="jser-tag">library</span></p>

ファイルサイズが小さなあいまい検索ライブラリ


----

## vercel/satori: Enlightened library to convert HTML and CSS to SVG
[github.com/vercel/satori](https://github.com/vercel/satori "vercel/satori: Enlightened library to convert HTML and CSS to SVG")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">SVG</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HTMLとCSSからSVGを生成するライブラリ。
yoga-layoutを使いCSSのサブセットを実装していて、ブラウザのレンダリングエンジンを使わずにSVGへと変換できる

- [Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images "Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel")

----

## fp-ts/core
[github.com/fp-ts/core](https://github.com/fp-ts/core "fp-ts/core")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">functional</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

関数型プログラミング向けのTypeScriptライブラリ。


----

## stepci/stepci: API Testing and Monitoring made simple
[github.com/stepci/stepci](https://github.com/stepci/stepci "stepci/stepci: API Testing and Monitoring made simple")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

言語に依存しないWeb APIのテストツール。
yamlでAPIのテストの定義を書き、テストを実行できる。


----
