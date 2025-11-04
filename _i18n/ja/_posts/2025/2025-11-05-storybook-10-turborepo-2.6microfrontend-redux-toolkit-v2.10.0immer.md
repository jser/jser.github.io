---
title: "2025-11-05のJS: Storybook 10、Turborepo 2.6(Microfrontend)、 redux-toolkit v2.10.0とImmerのパフォーマンス改善"
author: "azu"
layout: post
date: 2025-11-04T23:50:03.534Z
category: JSer
tags:
- Tools
- rspack
- performance
- nodejs
- storybook

---

JSer.info #754 - Storybook v10.0.0がリリースされました。

- [Release v10.0.0 · storybookjs/storybook](https://github.com/storybookjs/storybook/releases/tag/v10.0.0)

ESM-onlyに変更してインストールサイズを29%削減し、distコードをunminify化しています。新しい機能として、Module automockingのサポート、TypesafeなCSF factories、タグフィルター機能の改善が含まれています。
また、Next 16、Vitest 4、Svelte非同期コンポーネントへの対応なども追加されています。

---

Turborepo 2.6がリリースされました。

- [Turborepo 2.6 | Turborepo](https://turborepo.com/blog/turbo-2-6)

Microfrontendサポートとして、ローカル開発用のパスレベルのルーティングを定義できる`microfrontends.json`が追加されました。
Vercelの[Microfrontends](https://vercel.com/docs/microfrontends)サポートの一環として提供されています。また、Bunのサポート、TUIの改善なども含まれています。

---

Redux Toolkit v2.10.0がリリースされました。

- [Release v2.10.0 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0)

ReduxのメンテナーがImmerのパフォーマンス改善を行い、Immer 10.2.0にアップデートしています。
次のIssueでImmerのパフォーマンス問題について調査されています。

- [Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer](https://github.com/immerjs/immer/issues/1152)

このアップデートにより、Immerのパフォーマンス問題が改善されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v10.0.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v10.0.0](https://github.com/storybookjs/storybook/releases/tag/v10.0.0 "Release v10.0.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook v10.0.0リリース。
ESM-onlyに変更してインストールサイズを29%削減、distコードをunminify化。
Module automockingのサポート、TypesafeなCSF factories、タグフィルター機能の改善。
Next 16/Vitest 4/Svelte非同期コンポーネント対応など


----

## Turborepo 2.6 | Turborepo
[turborepo.com/blog/turbo-2-6](https://turborepo.com/blog/turbo-2-6 "Turborepo 2.6 | Turborepo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepo 2.6リリース。
Microfroendサポートとして、ローカル開発用のパスレベルのルーティングを定義できる`microfrontends.json`を追加。
Bunのサポート、TUIの改善など


----

## Electron 39.0.0 | Electron
[www.electronjs.org/blog/electron-39-0](https://www.electronjs.org/blog/electron-39-0 "Electron 39.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 39.0.0リリース。
Chromium 142/Node.js 22.20/V8 14.2へアップグレード。
ASAR integrityがStableに、`window.open`のポップアップは常にサイズが変更可能になるなど


----

## New in Chrome 142  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-142?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-142?hl=en "New in Chrome 142  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 142リリース。
`:target-before`/`:target-after`疑似クラスの追加、Style Container Queriesと`if()`関数でのレンジ構文のサポート。
`interestfor`属性の追加、`document.activeViewTransition`プロパティの追加。
WebGPUの`primitive_index`機能とテクスチャ形式tier1/tier2のサポート。
ローカルネットワークへのリクエストに許可　プロンプトが表示されるようになるなど

- [Chrome 142  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/142 "Chrome 142  |  Release notes  |  Chrome for Developers")

----

## Release v2.10.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0 "Release v2.10.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v2.10.0リリース。
Immerのパフォーマンス改善を行いImmer 10.2.0にアップデートなど

- [Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer](https://github.com/immerjs/immer/issues/1152 "Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer")

----

## Announcing Rspack 1.6 - Rspack
[rspack.rs/blog/announcing-1-6](https://rspack.rs/blog/announcing-1-6 "Announcing Rspack 1.6 - Rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">ReleaseNote</span></p>

Rspack 1.6リリース。
Dynamic importのTree Shakingを改善、import deferのサポート。
ESM出力の改善する`EsmLibraryPlugin`を追加、Barrelファイルの最適化をデフォルト有効化、layer機能の安定化。
ビルド時にJSX構文を保持オプションを追加、Source Mapを抽出する`extractSourceMap`オプションを追加。
Rsbuild 1.6では、ブラウザのエラーログをターミナル転送できるように、Rslib 1.6ではtypescript-goベースの型宣言ファイルの生成をサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing TanStack Start Middleware – Frontend Masters Blog
[frontendmasters.com/blog/introducing-tanstack-start-middleware/](https://frontendmasters.com/blog/introducing-tanstack-start-middleware/ "Introducing TanStack Start Middleware – Frontend Masters Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

TanStack Startのmiddlewareについて


----

## I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance | Loren Stewart
[www.lorenstew.art/blog/10-kanban-boards/](https://www.lorenstew.art/blog/10-kanban-boards/ "I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance | Loren Stewart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

10個のフレームワークで同じカンバンアプリを作成してモバイルパフォーマンスを比較した記事。
バンドルサイズ。モバイル環境でのパフォーマンス、MPAとSPA、React以外の選択肢についてなど


----

## Node.js — Node.js v22 to v24
[nodejs.org/en/blog/migrations/v22-to-v24](https://nodejs.org/en/blog/migrations/v22-to-v24 "Node.js — Node.js v22 to v24")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js v22からv24の変更とマイグレーションツールについて


----

## The Inner Workings of JavaScript Source Maps
[www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals "The Inner Workings of JavaScript Source Maps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">article</span></p>

Source Maoの仕組みについて。
Source Mapの形式やVLQエンコーディングの仕組みにについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## TanCN - Form and Table Builder
[tancn.dev/](https://tancn.dev/ "TanCN - Form and Table Builder")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">UI</span></p>

TanStackを使ったフォームビルダー


----


## Triplex Goes Open Source and Moves to Poimandres • Triplex
[triplex.dev/blog/triplex-moves-to-pmndrs](https://triplex.dev/blog/triplex-moves-to-pmndrs "Triplex Goes Open Source and Moves to Poimandres • Triplex")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">3D</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

Reactで3Dコンポーネントを作成するツール

- [pmndrs/triplex: The open source visual workspace for React / Three Fiber. Build the 2D and 3D web.](https://github.com/pmndrs/triplex "pmndrs/triplex: The open source visual workspace for React / Three Fiber. Build the 2D and 3D web.")

----

## @remix-run/node-fetch-server - npm
[www.npmjs.com/package/@remix-run/node-fetch-server](https://www.npmjs.com/package/@remix-run/node-fetch-server "@remix-run/node-fetch-server - npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Fetch APIの`Request`/`Response`を使ったHTTPサーバライブラリ。

