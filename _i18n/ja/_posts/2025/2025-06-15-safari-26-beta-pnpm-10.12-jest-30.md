---
title: "2025-06-15のJS: Safari 26 Beta、pnpm 10.12、Jest 30"
author: "azu"
layout: post
date: 2025-06-15T11:32:35.162Z
category: JSer
tags:
- test
- Tools
- rspack
- ESLint
- polyfill

---

JSer.info #738 - Safari 26 betaがリリースされました。

- [News from WWDC25: WebKit in Safari 26 beta | WebKit](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/)

このバージョンからmacOSと同じく、西暦の下2桁がSafariのバージョンとなるようです。

CSSでは、Anchor Positioning、Scroll-driven Animations、`text-wrap:pretty`、`contrast-color()`、`progress()`をサポートしています。
Web APIでは、WebGPU、HDR Images、Digital Credentials API、Trusted Types API、URL Patternを新たにサポートしています。
Web InspectorではService Workerや非同期処理のデバッグが改善されています。
その他、SVGファビコンの対応やWebAssemblyのインタープリタ対応による実行開始速度の改善なども含まれています。

---

pnpm v10.12.1がリリースされました。

- [Release pnpm 10.12.1 · pnpm/pnpm](https://github.com/pnpm/pnpm/releases/tag/v10.12.1)
- [pnpm 10.12 Introduces Global Virtual Store and Expanded Version Catalogs](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs)

実験的な機能として`enableGlobalVirtualStore`オプションでグローバル仮想ストアをサポートし、依存関係のキャッシュがある時のインストール速度が高速化されています。また、`pnpm update`がcatalogをサポートし、`catalogMode`オプションや`--save-catalog`フラグが追加されています。

---

Jest 30がリリースされました。

- [Jest 30: Faster, Leaner, Better · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

Node.js 14/16/19/21のサポートを終了し、TypeScript 5.4+、jsdom 26へアップデートされています。
[unrs-resolver](https://github.com/unrs/unrs-resolver)を使ったパフォーマンスとメモリの改善、設定ファイルのTypeScriptサポート、`import.meta`のサポート、`using`を使ったspyの自動復元などが追加されています。
また、`expect.arrayOf`、`jest.advanceTimersToNextFrame()`、`jest.unstable_unmockModule()`などの新しいAPIも追加されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Oxlint v1.0 Stable | The JavaScript Oxidation Compiler
[oxc.rs/blog/2025-06-10-oxlint-stable](https://oxc.rs/blog/2025-06-10-oxlint-stable "Oxlint v1.0 Stable | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

Oxlint 1.0リリース。


----

## Release 3.43.0 - 2025.06.09 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.43.0](https://github.com/zloirock/core-js/releases/tag/v3.43.0 "Release 3.43.0 - 2025.06.09 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.43.0リリース。
Explicit Resource Management/Array.fromAsync/Error.isErrorがStableに移行。
Joint iteration/Iterator chunkingのStage 2 proposalを追加、`Math.clamp`から`Number.prototype.clamp`への変更など


----

## Node.js — Node v24.2.0 (Current)
[nodejs.org/en/blog/release/v24.2.0](https://nodejs.org/en/blog/release/v24.2.0 "Node.js — Node v24.2.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.2.0リリース。
HTTP/2 priority signalingの削除、`import.meta.main`のサポートなど


----

## Release pnpm 10.12.1 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.12.1](https://github.com/pnpm/pnpm/releases/tag/v10.12.1 "Release pnpm 10.12.1 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.12.1リリース。
実験的な機能として`enableGlobalVirtualStore`オプションでグローバル仮想ストアをサポート。
依存関係グラフのハッシュを名前とするグローバルなストアへハードリンクするためキャッシュがある時のインストール速度が高速になる。
`pnpm update`がcatalogをサポート、`catalogMode`オプションの追加、`--save-catalog`の追加など

- [pnpm 10.12 Introduces Global Virtual Store and Expanded Vers...](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs "pnpm 10.12 Introduces Global Virtual Store and Expanded Vers...")

----

## Jest 30: Faster, Leaner, Better · Jest
[jestjs.io/blog/2025/06/04/jest-30](https://jestjs.io/blog/2025/06/04/jest-30 "Jest 30: Faster, Leaner, Better · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 30リリース。
Node.js 14/16/19/21のサポート終了、TypeScript 5.4+、jsdom 26へアップデート。  
`expect`のエイリアスメソッド削除、`--testPathPattern`を`--testPathPatterns`にリネーム。  
unrs-resolverを使ったパフォーマンスとメモリの改善、設定ファイルのTSサポート、`import.meta`のサポート、`using`を使ったspyの自動復元。
`expect.arrayOf`の追加、`jest.advanceTimersToNextFrame()`の追加、`jest.unstable_unmockModule()`の追加など


----

## News from WWDC25: WebKit in Safari 26 beta | WebKit
[webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/ "News from WWDC25: WebKit in Safari 26 beta | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 26 betaの変更点について。
CSSでは、Anchor Positioning/Scroll-driven Animations/`text-wrap:pretty`/`contrast-color()`/`progress()`をサポート。
Web APIでは、WebGPU/HDR Images/Digital Credentials API/Trusted Types API/URL Patternをサポート。
Web InspectorでService Workerや非同期処理のデバッグの改善。
その他、SVGファビコンの対応、WebAssemblyをインタープリタ対応し実行開始速度の改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## State of CSS 2025
[survey.devographics.com/en-US/survey/state-of-css/2025](https://survey.devographics.com/en-US/survey/state-of-css/2025 "State of CSS 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">Survey</span></p>

CSSの開発者アンケートであるState of CSS 2025の募集が始まった


----

## WebStatus.dev: Now with more data, deeper insights, and a clearer path to Baseline  |  Blog  |  web.dev
[web.dev/blog/web-platform-dashboard-evolution?hl&#x3D;en](https://web.dev/blog/web-platform-dashboard-evolution?hl=en "WebStatus.dev: Now with more data, deeper insights, and a clearer path to Baseline  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

ウェブプラットフォームのBaselineの実装状態などを可視化するダッシュボードである WebStatus.dev について

- [Web Platform Status](https://webstatus.dev/ "Web Platform Status")

----

## We shipped FinalizationRegistry in Workers: why you should never use it
[blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/](https://blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/ "We shipped FinalizationRegistry in Workers: why you should never use it")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Cloudflare Workersの`FinalizationRegistry` APIのサポートについて。
WebAssemblyと連携する際のメモリ管理で、JavaScriptオブジェクトがガベージコレクションされる際にコールバックを実行するAPI。  
非決定的な実行タイミングのため使用を推奨せず、代わりにExplicit Resource Managementの使用を推奨。I/O操作を無効化するなどの安全対策を実装して提供している


----

## Storybook 9
[storybook.js.org/blog/storybook-9/](https://storybook.js.org/blog/storybook-9/ "Storybook 9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Storybook 9の変更点について。
破壊的な変更として、`@storybook/addon-essentials`を削除してcoreに統合、パッケージ構造の変更。
VitestとPlaywrightを使ったStorybookテスト機能をStableに変更、パッケージサイズを48%削減。
Interaction/Accessibility/Visualテスト機能の統合、Story生成機能、Tags-basedの管理機能の追加。
Vite-powered Next.js、Svelte 5、React Nativeの改善など

- [Migration guide for Storybook 9.0 | Storybook docs](https://storybook.js.org/docs/migration-guide?ref=storybookblog.ghost.io "Migration guide for Storybook 9.0 | Storybook docs")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## web-infra-dev/rstest: The testing framework powered by Rspack (WIP).
[github.com/web-infra-dev/rstest](https://github.com/web-infra-dev/rstest "web-infra-dev/rstest: The testing framework powered by Rspack (WIP).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">rspack</span></p>

Rspackを使ったVitestのようなテストフレームワーク


----

## aymericzip/intlayer: Internationalisation solution for JS application focusing on scalability. Make your JavaScript / TypeScript application multilingue.
[github.com/aymericzip/intlayer](https://github.com/aymericzip/intlayer "aymericzip/intlayer: Internationalisation solution for JS application focusing on scalability. Make your JavaScript / TypeScript application multilingue.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

React/Next.js/Vue などに対応したi18nフレームワーク。
コード生成とロケールファイルを使った翻訳、ビジュアルエディタ、middlewareの提供、Markdownのサポートなど


----

## Nergie/no-barrel-file
[github.com/Nergie/no-barrel-file](https://github.com/Nergie/no-barrel-file "Nergie/no-barrel-file")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

barrel importsを検知して修正できるツール


----
