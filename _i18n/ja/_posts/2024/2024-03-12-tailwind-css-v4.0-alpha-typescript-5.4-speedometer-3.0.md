---
title: "2024-03-12のJS: Tailwind CSS v4.0 alpha、TypeScript 5.4、Speedometer 3.0"
author: "azu"
layout: post
date: 2024-03-12T02:18:32.384Z
category: JSer
tags:
- nodejs
- TypeScript
- React
- browser
- game

---

JSer.info #684 - Tailwind CSS v4.0 alphaがリリースされました。

- [Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-alpha)

OxideというRustで書かれたエンジンを追加、Lightning CSSを組み込むように変更することでパフォーマンスやビルドトインでサポートする構文が改善されています。また、記事ではv4のロードマップについても触れられています。

---

TypeScript 5.4がリリースされました。

- [Announcing TypeScript 5.4 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4/)

BetaやRCからの大きな機能的な追加などはありません。
クロージャーにおけるNarrowing結果の改善、`NoInfer` Utility Typeの追加、
`--module preserve`の追加が行われています。
また、ES2024の`Object.groupBy`/`Map.groupBy`をサポート、Import Attributesのサポートが追加されています。
5.4が`target: "ES3"`や`out`オプションなどの非推奨化されたオプションがサポートされる最後のバージョンとなる予定です。
これらのオプションは5.5で削除される予定となっています。

- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909)

---

ブラウザエンジンのパフォーマンスを測定するためのベンチマークツールであるSpeedometer 3.0がリリースされました。

- [Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit](https://webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/)

Speedometerは主にブラウザエンジンの開発者がブラウザのパフォーマンスを測定するベンチマークとして利用されています。
今回のアップデートで同期と非同期処理の実行時間をより正確に計測、HTTP Archiveやnpmのダウンロード数を元にした利用されているフレームワークの調整などが行われています。
また、今まではTodoMVCを利用していましtが、Next.js/Nuxt を使ったメディアサイトやグラフィカルなダッシュボード、CodeMirrorとTipTapを使ったエディタなどもテストに追加されています。

Speedometer 3.0のベンチマークでは次のようなフレームワークがテストに含まれています。

- [Angular](https://angular.io/)
- [Backbone](https://backbonejs.org/)
- [jQuery](https://jquery.com/)
- [Lit](https://lit.dev/)
- [Preact](https://preactjs.com/)
- [React](https://reactjs.org/)
- [React+Redux](https://react-redux.js.org/)
- [Svelte](https://svelte.dev/)
- [Vue](https://vuejs.org/)
- [Next.js](https://nextjs.org/)
- [Nuxt](https://nuxtjs.org/)
- [Observable Plot](https://observablehq.com/@observablehq/plot)
- [chart.js](https://www.chartjs.org/)
- [React stockcharts](https://github.com/rrag/react-stockcharts)
- [D3](https://d3js.org/)
- [CodeMirror](https://codemirror.net/)
- [TipTap](https://www.tiptap.dev/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v8.0.0 · pixijs/pixijs
[github.com/pixijs/pixijs/releases/tag/v8.0.0](https://github.com/pixijs/pixijs/releases/tag/v8.0.0 "Release v8.0.0 · pixijs/pixijs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

PixiJS v8.0.0リリース。
`pixi.js`の単体のパッケージに統合、初期化が非同期へと変更、Graphiscs APIの変更など

- [v8 Migration Guide | PixiJS](https://pixijs.com/guides/migrations/v8 "v8 Migration Guide | PixiJS")

----

## Node.js — Node v21.7.0 (Current)
[nodejs.org/en/blog/release/v21.7.0](https://nodejs.org/en/blog/release/v21.7.0 "Node.js — Node v21.7.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v21.7.0リリース。
`util.styleText(format, text)`関数を追加、`process.loadEnvFile(path)`と`util.parseEnv(content)`を追加。
`.env`で複数行の値をサポート、`node:sea`にAPIを追加、`node:vm`に`importModuleDynamically`オプションを追加、`crypto.hash()`の追加など


----

## Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS
[tailwindcss.com/blog/tailwindcss-v4-alpha](https://tailwindcss.com/blog/tailwindcss-v4-alpha "Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS v4 alphaリリース。
OxideというRustで書かれたエンジンを追加、Lightning CSSを組み込むように変更。
v4のロードマップについてなど


----

## WebKit Features in Safari 17.4 | WebKit
[webkit.org/blog/15063/webkit-features-in-safari-17-4/](https://webkit.org/blog/15063/webkit-features-in-safari-17-4/ "WebKit Features in Safari 17.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17.4の変更点について。
HTMLでは、`<input type="checkbox" switch>`のサポート、フォームの縦書き表示に対応、`<select>`の区切りに`<hr>`を使えるように。
CSSでは、`@scope`のサポート、`::spelling-error`と`::grammar-error`の擬似要素のサポート、`content: "foo" / "alt"`で代替テキストをサポート。
Web APIでは、`element.checkVisibility()`のサポート、`AbortSignal.any()`のサポート。
JSでは、ES2024の`Promise.withResolvers()`/`Object.groupBy()`/`Map.groupBy()`のサポート。

- [Safari 17.4 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17_4-release-notes "Safari 17.4 Release Notes | Apple Developer Documentation")

----

## Biome v1.6 | Biome
[biomejs.dev/blog/biome-v1-6/](https://biomejs.dev/blog/biome-v1-6/ "Biome v1.6 | Biome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Biome v1.6リリース。
Astro/Svelte/Vueのファイル内のJS/TS分析をサポート、`biome.jsonc`をサポート。
`atributePosition`オプションの追加、ルールの更新など


----

## Announcing TypeScript 5.4 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-4/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4/ "Announcing TypeScript 5.4 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.4リリース。
クロージャーにおけるNarrowing結果の改善、`NoInfer` Utility Typeの追加、
`--module preserve`の追加。
ES2024の`Object.groupBy`/`Map.groupBy`をサポート、Import Attributesのサポート。
`target: "ES3"`や`out`オプションなどを非推奨化されたオプションは5.5で削除される予定。


----

## WinterJS 1.0 · Blog · Wasmer
[wasmer.io/posts/winterjs-v1](https://wasmer.io/posts/winterjs-v1 "WinterJS 1.0 · Blog · Wasmer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span></p>

SpidermonkeyベースのWinterJS-compatibleなJavaScript RuntimeであるWinterJS 1.0リリース。


----

## Release v4.1.0 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.1.0](https://github.com/honojs/hono/releases/tag/v4.1.0 "Release v4.1.0 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Hono v4.1.0リリース。
WebSocket Helperの追加、Body Limit Middlewareの追加、出力ターゲットをES2022に変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## フルスクラッチして理解するOpenID Connect (1) 認可エンドポイント編 - エムスリーテックブログ
[www.m3tech.blog/entry/2024/03/05/150000](https://www.m3tech.blog/entry/2024/03/05/150000 "フルスクラッチして理解するOpenID Connect (1) 認可エンドポイント編 - エムスリーテックブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">OpenID</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

OpenID ConnectのID ProviderをTypeScriptで実装していく連載


----

## &quot;react-strict-dom&quot;, why it&#039;s so great? | Szymon Rybczak
[szymonrybczak.dev/blog/react-strict-dom](https://szymonrybczak.dev/blog/react-strict-dom "\&quot;react-strict-dom\&quot;, why it&#039;s so great? | Szymon Rybczak")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">HTML</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">article</span></p>

react-strict-domについて。
React Native for WebのアプローチではReact Nativeのプリミティブをウェブ向けに変換する互換Shimが大きかった。
react-strict-domでは逆のアプローチを採用し、DOM APIのサブセットをネイティブ側で扱う。

- [RFC: React DOM for Native (reduce API fragmentation) by necolas · Pull Request #496 · react-native-community/discussions-and-proposals](https://github.com/react-native-community/discussions-and-proposals/pull/496 "RFC: React DOM for Native (reduce API fragmentation) by necolas · Pull Request #496 · react-native-community/discussions-and-proposals")

----

## Why Should You Care About Package Metadata Interoperability? | OpenJS Foundation
[openjsf.org/blog/package-metadata-interoperability-collab-space-intro](https://openjsf.org/blog/package-metadata-interoperability-collab-space-intro "Why Should You Care About Package Metadata Interoperability? | OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

OpenJSで`package.json`のメタデータの相互運用性を向上させるためのワーキンググループが発足した。

- [openjs-foundation/package-metadata-interoperability-collab-space: The goal of the Package Metadata Interoperability Collab Space is to improve how JavaScript developers define their packages across the ecosystem. The group is currently working to better understand package.json and how developers use it to define their projects.](https://github.com/openjs-foundation/package-metadata-interoperability-collab-space "openjs-foundation/package-metadata-interoperability-collab-space: The goal of the Package Metadata Interoperability Collab Space is to improve how JavaScript developers define their packages across the ecosystem. The group is currently working to better understand package.json and how developers use it to define their projects.")
- [OpenJS Launches New Collaboration to Improve Interoperability of JavaScript Package Metadata  - Socket](https://socket.dev/blog/openjs-improve-interoperability-of-javascript-package-metadata "OpenJS Launches New Collaboration to Improve Interoperability of JavaScript Package Metadata  - Socket")

----

## Ultimate Guide to Visual Testing with Playwright
[www.browsercat.com/post/ultimate-guide-visual-testing-playwright](https://www.browsercat.com/post/ultimate-guide-visual-testing-playwright "Ultimate Guide to Visual Testing with Playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Playwrightを使ったビジュアルリグレッションテストについて


----

## Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit
[webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/](https://webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/ "Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ウェブブラウザエンジンのベンチマークとして使われるSpeedometer 3.0リリース。
同期と非同期処理の実行時間をより正確に計測、HTTP Archiveやnpmのダウンロード数を元にした利用されているフレームワークの調整。
また、今まではTodoMVCを利用していたが、Next.js/Nuxt を使ったメディアサイトやグラフィカルなダッシュボード、CodeMirrorとTipTapを使ったエディタなどもテストに追加など


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## rolldown-rs/rolldown: Fast Rust bundler for JavaScript with Rollup-compatible API.
[github.com/rolldown-rs/rolldown](https://github.com/rolldown-rs/rolldown "rolldown-rs/rolldown: Fast Rust bundler for JavaScript with Rollup-compatible API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rollup</span> <span class="jser-tag">Rust</span> <span class="jser-tag">vite</span> <span class="jser-tag">library</span></p>

Rollup互換を目指すRustでのJavaScript Bundlerの実装。


----

## edmundhung/conform: A type-safe form validation library utilizing web fundamentals to progressively enhance HTML Forms with full support for server frameworks like Remix and Next.js.
[github.com/edmundhung/conform](https://github.com/edmundhung/conform "edmundhung/conform: A type-safe form validation library utilizing web fundamentals to progressively enhance HTML Forms with full support for server frameworks like Remix and Next.js.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">Remix</span> <span class="jser-tag">library</span></p>

RemixやNext.jsでのサーバ側の処理にも対応したフォームライブラリ。
Zodなどと組み合わせてサーバ側でのバリデーションやReactの`useFormState`と組み合わせて動作する


----
<h1 class="site-genre">書籍関係</h1>

----

## Eloquent JavaScript
[eloquentjavascript.net/](https://eloquentjavascript.net/ "Eloquent JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Eloquent JavaScripの第4版(2024)が公開された


----
