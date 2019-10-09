---
title: "2019-10-09のJS: Preact X(10)、webhint browser extension v1、TypeScript 3.7β"
author: "azu"
layout: post
date : 2019-10-09T00:17:09.603Z
category: JSer
tags:
- Preact
- webhint
- typescript

---

JSer.info #456 - React互換のAPIを持つPreact X(10.0.0)がリリースされました。
Preact 9.xはスキップしてPreact 10.xになっています。

- [Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact](https://github.com/preactjs/preact/releases/tag/10.0.0)
- [What's new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/whats-new/)

Preact Xでは、Fragments、componentDidCatch、Hooks(`preact/hooks`)、createContext、CSS Custom Propertiesの対応などが含まれています。
[Hooks](https://preactjs.com/guide/v10/hooks/)はPreactのコアには含まれていませんが、`preact/hooks`または`preact/compat`をインポートすることで対応しています。

また、いままでは別モジュールとなっていた`preact-compat`が[`preact/compat`](https://preactjs.com/guide/v10/switching-to-preact)という形でインポートするように変更されています。

```js
// Preact 8.x
import React from "preact-compat";

// Preact X
import React from "preact/compat";
```

また、preact本体はdefault exportをやめたため、named importをして使う形に変更されています。

```
// Preact 8.x
import Preact from "preact";

// Preact X
import * as preact from "preact";

// Preferred: Named exports (works in 8.x and Preact X)
import { h, Component } from "preact";
```

Preact 8.xから10.xへのマイグレーションガイドも公開されているので、合わせて見てください。

- [Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/upgrade-guide/)

----

ウェブサイト向けのLintツールである[webhint](https://webhint.io/)のブラウザ拡張版がv1となりました。

- [Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/#U2qsHqfdpdTkuKGc.97)

[beta版](https://medium.com/webhint/announcing-the-webhint-browser-extension-abb22f4cfeb)からの追加点として、
MDN browser compat dataを使ったクロスブラウザの互換情報の表示、カラーコントラストについてのHintの追加などが含まれています。

Chrome(lighthouse)のAuditとの違いとして、webhintはクロスブラウザに関するチェックをあげています。

> The webhint extension doesn’t replace the existing audits tab you’ll find in the developer tools for Chrome and the new Chromium-based Edge browser. While there is a little overlap in the information provided, webhint and Lighthouse serve different purposes, and you may find yourself using both. One distinguishing feature of webhint that it’s meant to provide cross-browser insights, including compatibility with Safari, IE, Opera, and so on.
> -- https://medium.com/webhint/announcing-the-webhint-browser-extension-abb22f4cfeb

----


TypeScript 3.7 Betaがリリースされました。

- [Announcing TypeScript 3.7 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/)
- [TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352)

ECMAScriptのStage 3 Proposalである[Optional Chaining](https://github.com/tc39/proposal-optional-chaining)と[Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing)がサポートされています。
また、`asserts`によるコントールフロー制御を行うAssertion Functionsがサポートされています。
その他には、`--declaration`と`--allowJs`の組み合わせのサポートが含まれています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.0.0](https://github.com/preactjs/preact/releases/tag/10.0.0 "Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact X(10.0.0)リリース。
`Fragments`、`componentDidCatch`、`createContext`のサポート、Hooks APIのサポートなど

- [What's new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/whats-new/ "What&#x27;s new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.")
- [Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/upgrade-guide/ "Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.")

----

## Release v3.2.0 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v3.2.0](https://github.com/facebook/create-react-app/releases/tag/v3.2.0 "Release v3.2.0 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 3.2.0リリース。
`yarn build --profile`でproduction buildでのプロファイル対応、`TSC_COMPILE_ON_ERROR`のサポートなど


----

## vuejs/vue-next
[github.com/vuejs/vue-next](https://github.com/vuejs/vue-next "vuejs/vue-next")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Github</span> <span class="jser-tag">news</span></p>

Vue 3候補のソースコードが公開された

----

## Announcing TypeScript 3.7 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/ "Announcing TypeScript 3.7 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.7 Betaリリース。
Optional Chaining、Nullish Coalescing、Assertion Functionsのサポート。
`--declaration`と`--allowJs`の組み合わせのサポート、TypeScriptファイル内で`// @ts-nocheck`の追加など

- [TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352 "TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript")

----

## Release v5.5.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v5.5.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.5.0 "Release v5.5.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Chrome</span></p>

Lighthouse 5.5.0リリース。
Largest Contentful Paint(LCP)のサポート


----

## Version 1.0 released : Node-RED
[nodered.org/blog/2019/09/30/version-1-0-released](https://nodered.org/blog/2019/09/30/version-1-0-released "Version 1.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">IoT</span> <span class="jser-tag">ReleaseNote</span></p>

フローベースのビジュアルエディタを使って、Node.jsで動くプログラムを作成できるツールキットであるNode-RED 1.0リリース。


----

## Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/](https://blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/ "Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Extension</span> <span class="jser-tag">accessibility</span></p>

webhint browser extension 1.0.0リリース。
プラグインでカスタマイズできるウェブサイト向けのLintツールのブラウザ拡張版。
MDN browser compat dataを使ったクロスブラウザの互換情報の表示、カラーコントラストについてのHintの追加など

- [webhint, the hinting engine for web best practices](https://webhint.io/ "webhint, the hinting engine for web best practices")
- [webhint browser extension](https://medium.com/webhint/the-webhint-browser-extension-v1-release-df9044ddaf69)

----
<h1 class="site-genre">アーティクル</h1>

----

## I created the exact same app in React and Vue. Here are the differences. \[2019 Edition\]
[medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-2019-edition-42ba2cab9e56](https://medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-2019-edition-42ba2cab9e56 "I created the exact same app in React and Vue. Here are the differences. \[2019 Edition\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ReactとVueでのTodoアプリを例にした比較。
React Hooksに対応したバージョン


----

## Fixing layout instability  |  web.dev
[web.dev/fixing-layout-instability/](https://web.dev/fixing-layout-instability/ "Fixing layout instability  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`PerformanceObserver`でCumulative Layout Shift (CLS)を計測し、どのようなレイアウトの変化が起きてるのかをWebPageTestで確認する方法について。
また、実際にプレースホルダーデータを使ってlayout instabilityを修正する方法について。

- [Measuring Cumulative Layout Shift (CLS) in WebPageTest - DEV Community 👩‍💻👨‍💻](https://dev.to/chromiumdev/measuring-cumulative-layout-shift-cls-in-webpagetest-5cle "Measuring Cumulative Layout Shift (CLS) in WebPageTest - DEV Community 👩‍💻👨‍💻")

----

## How to read a Web Page Test waterfall chart - Frontend Web Developer, Oxfordshire, UK - Matt Hobbs
[nooshu.github.io/blog/2019/10/02/how-to-read-a-wpt-waterfall-chart/](https://nooshu.github.io/blog/2019/10/02/how-to-read-a-wpt-waterfall-chart/ "How to read a Web Page Test waterfall chart - Frontend Web Developer, Oxfordshire, UK - Matt Hobbs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

WebPageTestのウォーターフォールチャートの読み方について。
図の要素ごとに解説やHTTP/1.1とHTTP/2での流れの違いなどについて書かれている


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Accessibility Support
[a11ysupport.io/](https://a11ysupport.io/ "Accessibility Support")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">webservice</span> <span class="jser-tag">WAI-ARIA</span></p>

スクリーンリーダごとのWAI-ARIAなどのアクセシビリティサポート状況についてまとめているサイト。
Can I Use...のアクセシビリティ版


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## cevek/ttypescript: Over TypeScript tool to use custom transformers in the tsconfig.json
[github.com/cevek/ttypescript](https://github.com/cevek/ttypescript "cevek/ttypescript: Over TypeScript tool to use custom transformers in the tsconfig.json")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">plugin</span></p>

TypeScriptでのコンパイル処理に対して、プラグインで変換処理を追加できるコンパイラーの実装

----

## algolia/shipjs: Take control of what is going to be your next release.
[github.com/algolia/shipjs](https://github.com/algolia/shipjs "algolia/shipjs: Take control of what is going to be your next release.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">CI </span></p>

リリースの準備とリリースを行うツール。
semantic-releaseとは異なりすべてを自動で行うのではなく、Pull Requestを作成して、手動で確認やCHANGELOGの更新をしてからリリースを行うといったプロセスが取れる。

----

## fengyuanchen/cropperjs: JavaScript image cropper.
[github.com/fengyuanchen/cropperjs](https://github.com/fengyuanchen/cropperjs "fengyuanchen/cropperjs: JavaScript image cropper.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Image Cropperライブラリ。
画像の切り抜き、回転、移動などができる画像加工を行うライブラリ


----

## Bin-Huang/prray: "Promisified" Array, comes with async method supports(such as mapAsync). And it is compatible with normal array.
[github.com/Bin-Huang/prray](https://github.com/Bin-Huang/prray "Bin-Huang/prray: \"Promisified\" Array, comes with async method supports(such as mapAsync). And it is compatible with normal array.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

コールバック関数にAsync Functionを取るArrayの実装ライブラリ


----
