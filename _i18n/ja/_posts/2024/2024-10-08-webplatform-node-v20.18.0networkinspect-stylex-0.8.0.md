---
title: "2024-10-08のJS: WebPlatformの新機能リリースノート、Node v20.18.0(networkのinspect)、StyleX 0.8.0"
author: "azu"
layout: post
date: 2024-10-08T11:06:46.767Z
category: JSer
tags:
- webservice
- nodejs
- React
- WebPlatformAPI
- npm

---

JSer.info #710 - - [Web features explorer - Web platform release notes](https://web-platform-dx.github.io/web-features-explorer/release-notes/)
- [Node.js — Node v20.18.0 (LTS)](https://nodejs.org/en/blog/release/v20.18.0)
- [Release 0.8.0 | StyleX](https://stylexjs.com/blog/v0.8.0)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Web features explorer - Web platform release notes
[web-platform-dx.github.io/web-features-explorer/release-notes/](https://web-platform-dx.github.io/web-features-explorer/release-notes/ "Web features explorer - Web platform release notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">news</span> <span class="jser-tag">webservice</span></p>

web-featuresやbrowser-compat-dataを元にしたブラウザの新しい機能をリリースノート形式でまとめたサイト


----

## Release v10.9.0 · npm/cli
[github.com/npm/cli/releases/tag/v10.9.0](https://github.com/npm/cli/releases/tag/v10.9.0 "Release v10.9.0 · npm/cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm v10.9.0リリース。
開発時のランタイム情報を定義できる`devEngines`フィールドのサポートなど


----

## Node.js — Node v20.18.0 (LTS)
[nodejs.org/en/blog/release/v20.18.0](https://nodejs.org/en/blog/release/v20.18.0 "Node.js — Node v20.18.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.18.0リリース。
`--experimental-network-inspection`フラグでNetwork Inspectionをサポート。
`vm`内の`globalThis`をfreezeする`vm.constants.DONT_CONTEXTIFY`を追加など


----

## Tauri 2.0 Stable Release | Tauri
[v2.tauri.app/blog/tauri-20/](https://v2.tauri.app/blog/tauri-20/ "Tauri 2.0 Stable Release | Tauri")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">GUI</span> <span class="jser-tag">ReleaseNote</span></p>

Tauri 2.0リリース。
iOS/Androidのサポート、モバイルアプリのシミューレーターでもHMRが有効に、プラグインシステムの刷新、アクセス制御の仕組みを刷新など


----

## September 30, 2024 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2024-09-30.html](https://react-spectrum.adobe.com/releases/2024-09-30.html "September 30, 2024 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria September 30, 2024リリース。
ColorPicker/ColorArea/ColorField/ColorSlider/ColorSwatch/ColorSwatchPicker/ ColorWheelの追加。
ButtonにPendingのstateを追加。
実験的なコンポーネントして、`Tree`/`TreeView`と`Disclosure`/`DisclosureGroup`を追加など


----

## Release 20.0.0 · nrwl/nx
[github.com/nrwl/nx/releases/tag/20.0.0](https://github.com/nrwl/nx/releases/tag/20.0.0 "Release 20.0.0 · nrwl/nx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Nx 20.0.0リリース。
rspackプラグインの追加など


----

## Release 0.8.0 | StyleX
[stylexjs.com/blog/v0.8.0](https://stylexjs.com/blog/v0.8.0 "Release 0.8.0 | StyleX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css </span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

StyleX 0.8.0リリース。
shorthandを禁止する`valid-shorthands`ルールの追加、`enforce-extension`ルールの追加。
lightningcssを使ったminifyやautoprefixのpost-processを行うように


----
<h1 class="site-genre">アーティクル</h1>

----

## ESLint now officially supports linting of JSON and Markdown - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2024/10/eslint-json-markdown-support/](https://eslint.org/blog/2024/10/eslint-json-markdown-support/ "ESLint now officially supports linting of JSON and Markdown - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">JSON</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">article</span></p>

ESLintのJSONとMarkdownのサポートについて


----

## How Bun supports V8 APIs without using V8 (part 1) | Bun Blog
[bun.sh/blog/how-bun-supports-v8-apis-without-using-v8-part-1](https://bun.sh/blog/how-bun-supports-v8-apis-without-using-v8-part-1 "How Bun supports V8 APIs without using V8 (part 1) | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">V8</span> <span class="jser-tag">webkit</span> <span class="jser-tag">C++</span> <span class="jser-tag">article</span></p>

BunがどのようにV8 APIをJSC上に実装しているかについて。
C++のポインタ、レイアウトの互換性のレイヤー、V8とJSCの値の表現の違い、NaNボクシング、GC、メモリレイアウトについて


----

## Web Components are not Framework Components — and That’s Okay • Lea Verou
[lea.verou.me/blog/2024/wcs-vs-frameworks/](https://lea.verou.me/blog/2024/wcs-vs-frameworks/ "Web Components are not Framework Components — and That’s Okay • Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Web ComponentsはHTMLの拡張とリアクティブテンプレートという2つのカテゴリを使っているという話


----

## webpack to Rspack ~ Rspack移行の結果と注意点 ~
[zenn.dev/ryo\_kawamata/articles/b2df9989fe2c6e](https://zenn.dev/ryo_kawamata/articles/b2df9989fe2c6e "webpack to Rspack ~ Rspack移行の結果と注意点 ~")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

webpackからRspackへのマイグレーションについて。
productionビルドでの問題と対応について


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ViteConf 2024 - YouTube
[www.youtube.com/playlist?list&#x3D;PLqGQbXn\_GDmnObDzgjUF4Krsfl6OUKxtp](https://www.youtube.com/playlist?list=PLqGQbXn_GDmnObDzgjUF4Krsfl6OUKxtp "ViteConf 2024 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

ViteConf 2024の動画一覧


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## CrUX Vis
[cruxvis.withgoogle.com/](https://cruxvis.withgoogle.com/ "CrUX Vis")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span></p>

CrUXのデータを使って指定したサイトのWeb Vitalなどのパフォーマンスメトリクスの傾向をビジュアライズしてみれるサイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## dimdenGD/ultimate-express: The Ultimate Express. Fastest http server with full Express compatibility, based on µWebSockets.
[github.com/dimdenGD/ultimate-express](https://github.com/dimdenGD/ultimate-express "dimdenGD/ultimate-express: The Ultimate Express. Fastest http server with full Express compatibility, based on µWebSockets.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">express</span> <span class="jser-tag">library</span></p>

µWebSocketsベースのexpress互換のAPIを持つライブラリ


----
