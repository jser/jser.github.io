---
title: "2020-05-18のJS: TypeScript 3.9、Deno 1.0、Playwright 1.0"
author: "azu"
layout: post
date : 2020-05-18T12:14:18.906Z
category: JSer
tags:
- TypeScript
- Deno
- Testing

---

JSer.info #488 - TypeScript 3.9がリリースされました。

- [Announcing TypeScript 3.9 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9/)

`Promise.all`の型推論がされています。
また3.9 β時点では導入される予定だった[`awaited`](https://github.com/microsoft/TypeScript/pull/35998)は[問題が見つかった](https://github.com/microsoft/TypeScript/issues/37897)ため、3.9時点では導入されないことになりました。

その他にはビルドパフォーマンスの改善、Type Errorとなることを期待する`// @ts-expect-error`コメントの追加などが行われています。
JSへとコード変換における非互換な変更として、クラスのGetter/Setterを`enumerable: true`に変換するのではなく、`enumerable: false`に変換する変更が含まれています。
これは、ECMAScriptの仕様で定義されているのと同じ挙動で、Babelも同様の挙動です。

- [TypeSctipt 3.9](https://www.typescriptlang.org/play?target=1&ts=3.9.2#code/MYGwhgzhAEDC0G8BQ1XQOYFMAu0wAoBKRaAJxwFdSA7aAImADow7oBfJDoA)
- [TypeSctipt 3.8](https://www.typescriptlang.org/play?target=1&ts=3.8.3#code/MYGwhgzhAEDC0G8BQ1XQOYFMAu0wAoBKRaAJxwFdSA7aAImADow7oBfJDoA)
- [Babel](https://babeljs.io/repl#?browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=MYGwhgzhAEDC0G8BQ1XQOYFMAu0wAoBKRaAJxwFdSA7aAImADow7oBfJDoA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=es2015&prettier=false&targets=&version=7.9.6&externalPlugins=)

----

V8を使ったJavaScript/TypeScriptランタイムであるDeno 1.0.0がリリースされました。

- [Deno 1.0](https://deno.land/v1)

Node.jsの作者でもある[Ryan Dahl](https://github.com/ry)が中心となっていって作成されており、次の動画でもコンセプトが話されています。
DenoはNode.jsのForkではなく、一から新しく実装されています。

- [10 Things I Regret About Node.js - Ryan Dahl - JSConf EU - YouTube](https://www.youtube.com/watch?v=M3BM9TB-8yA)

Denoはデフォルトでサンドボックス上でコードが実行されます。
ネットワークやファイルアクセスなどの機能はオプトインで有効化できるようになっています。

また、TypeScriptをサポートとしており、コード実行以外にも[Formatter](https://deno.land/manual/tools/formatter)、[Bundler](https://deno.land/manual/tools/bundler)などの機能も持っています。

npmのようなパッケージの仕組みとは別にURLからES Modulesをロードできる仕組みを持ち、
Go言語ライクな[Standard library](https://deno.land/manual/standard_library)も提供しています。

----

PuppeteerライクなAPIを持つクラスブラウザテストフレームワークの[Playwright](https://github.com/microsoft/playwright) 1.0がリリースされました。

- [Fast and reliable cross-browser testing with Playwright 🎭](https://medium.com/@arjunattam/fast-and-reliable-cross-browser-testing-with-playwright-155c0e8a821f)

PlaywrightはChromium、WebKit、Firefoxを一部[Patch](https://github.com/microsoft/playwright/tree/master/browser_patches)をあててつつサポートしています。
PuppeteerもChromium、Firefoxをサポートしていますが、[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)(CDP)に基づいたサポートとなっています。そのため、CDPそのものを扱っていないWebKitはPuppeteerではサポートされていません。

Playwrightは、Puppeteerをforkしてこの辺の違いもカバーしクロスブラウザのテストフレームワークとして使うのに適したAPI/エミュレーション機能を持つことを目的としています。

- [\[Question\] How does Puppeteer's new Firefox support affect Playwright? · Issue #1765 · microsoft/playwright](https://github.com/microsoft/playwright/issues/1765)

Playwrightでは、`waitForTime`のような時間ではなく、`waitForEvent`のようなイベントの発生を待つ仕組み持ちflaky testsを回避しやすくなっています。
複数の独立したコンテキストを定義して並列実行の安定性を向上、ネットワークルーティングなどさまざまなAPIをもっています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 3.9 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-9/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9/ "Announcing TypeScript 3.9 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.9リリース。`Promise.all`の型改善、ビルドパフォーマンスの改善、Type Errorとなることを期待する`// @ts-expect-error`コメントの追加など。 また、ECMAScript仕様にあわせてGetter/Setterをトランスパイルするように変更など


----

## Release Notes for Safari Technology Preview 106 | WebKit
[webkit.org/blog/10580/release-notes-for-safari-technology-preview-106/](https://webkit.org/blog/10580/release-notes-for-safari-technology-preview-106/ "Release Notes for Safari Technology Preview 106 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 106リリース。
CSSの`:where()` pseudo-classのサポート、ES2020のBigIntをサポート、`Intl.RelativeTimeFormat`のサポートなど


----

## Deno 1.0
[deno.land/v1](https://deno.land/v1 "Deno 1.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">node.js</span></p>

Deno 1.0リリース。
V8を使ったJavaScript/TypeScriptランタイム。
オプトインで機能を有効化でき、formatterなどを同梱していて、Go言語ライクなStandard libraryを持っている。


----

## Fast and reliable cross-browser testing with Playwright 🎭
[medium.com/@arjunattam/fast-and-reliable-cross-browser-testing-with-playwright-155c0e8a821f](https://medium.com/@arjunattam/fast-and-reliable-cross-browser-testing-with-playwright-155c0e8a821f "Fast and reliable cross-browser testing with Playwright 🎭")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Playwright 1.0.0リリース。
Chrome、Firefox、SafariをサポートしたPuppeteer-likeなAPIを持つクスブラウザテストフレームワーク。
時間ではなくイベントに対して待機できる仕組み、複数の独立したコンテキストの定義、さまざまなブラウザAPIに対応している


----
<h1 class="site-genre">アーティクル</h1>

----

## How to use prefers-reduced-motion in React · Josh W Comeau
[joshwcomeau.com/react/prefers-reduced-motion/](https://joshwcomeau.com/react/prefers-reduced-motion/ "How to use prefers-reduced-motion in React · Josh W Comeau")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Reactで`prefers-reduced-motion`を利用したアニメーションの削減を実装する方法について。
React hooksを使った実装、SSRを考慮したパターンについて


----

## What's New In DevTools (Chrome 84)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/05/devtools](https://developers.google.com/web/updates/2020/05/devtools "What's New In DevTools (Chrome 84)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 84の開発者ツールの変更点について。
パフォーマンスパネルにWeb Vitalsを反映した項目の追加、PromiseオブジェクトのStatusをコンソールに表示するように、CSS `revert` プロパティのサポートなど


----

## Kite Launches AI-Powered JavaScript Completions - Code Faster with Kite
[www.kite.com/blog/product/kite-launches-ai-powered-javascript-completions/](https://www.kite.com/blog/product/kite-launches-ai-powered-javascript-completions/ "Kite Launches AI-Powered JavaScript Completions - Code Faster with Kite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">article</span></p>

機械学習ベースのコード補完ツールであるKiteがJavaScriptの補完に対応したという話


----

## How an anti ad-blocker works: Reverse-engineering BlockAdBlock
[xy2.dev/article/re-bab/](https://xy2.dev/article/re-bab/ "How an anti ad-blocker works: Reverse-engineering BlockAdBlock")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ad </span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

AdBlockのBlockerの実装を見ていく話。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Production Ready State Management for React | Kea 2.0
[kea.js.org/](https://kea.js.org/ "Production Ready State Management for React | Kea 2.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

React向けのステート管理ライブラリ。
Actions、Reducers、Listeners、Loaders、Selectors、Valuesを扱う


----

## ReactEurope 2020 - YouTube
[www.youtube.com/playlist?list&#x3D;PLCC436JpVnK0Q4WHoB85ZYBwcCyTaMgAl](https://www.youtube.com/playlist?list=PLCC436JpVnK0Q4WHoB85ZYBwcCyTaMgAl "ReactEurope 2020 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

React Europe 2020の動画一覧

- [ReactEurope - The original European React.js &amp; Native conference on May 14-15th, 2020 in Paris, France](https://www.react-europe.org/ "ReactEurope - The original European React.js &amp;amp; Native conference on May 14-15th, 2020 in Paris, France")

----

## Focused Session: Performance profiling for Web Applications with Sam Saccone - YouTube
[www.youtube.com/watch?v&#x3D;j9LW94EN7n4](https://www.youtube.com/watch?v=j9LW94EN7n4 "Focused Session: Performance profiling for Web Applications with Sam Saccone - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">video</span> <span class="jser-tag">debug</span> <span class="jser-tag">browser</span></p>

ウェブアプリケーションのボトルネックの見つけ方について動画。
初期ロードのネットワークにおけるクリティカルパスの問題とpreload、
操作中のパフォーマンスのボトルネックの見つけ方についてのケーススタディ

- [nodeschool April 18 2020 - webperf - Google スライド](https://docs.google.com/presentation/d/1K9QKmQdZ51OU4DKGmXL_8R4KS4N-WVtZZEqZA9g4STA/edit#slide=id.p "nodeschool April 18 2020 - webperf - Google スライド")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## addyosmani/puppeteer-webperf: Automating Web Performance testing with Puppeteer 🎪
[github.com/addyosmani/puppeteer-webperf](https://github.com/addyosmani/puppeteer-webperf "addyosmani/puppeteer-webperf: Automating Web Performance testing with Puppeteer 🎪")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">example</span></p>

Puppeteerを使ったパフォーマンス計測のメトリクス取得などのスニペットリポジトリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Raynos/npm-bin-deps: NPR allows you to run your CLI dependencies without having a copy in node\_modules.
[github.com/Raynos/npm-bin-deps](https://github.com/Raynos/npm-bin-deps "Raynos/npm-bin-deps: NPR allows you to run your CLI dependencies without having a copy in node\_modules.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

npm run-scriptからコマンドとして利用するパッケージを`package.json`に`binDependencies`として定義して、利用するツール


----

## sandersn/downlevel-dts: Convert a new d.ts to one that works with older versions of Typescript
[github.com/sandersn/downlevel-dts](https://github.com/sandersn/downlevel-dts "sandersn/downlevel-dts: Convert a new d.ts to one that works with older versions of Typescript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TypeScriptの型定義のダウングレードを行うツール。
TypeScriptの古い機能を使って新しい機能を再現するように型定義を変換するツール


----

## facebookexperimental/Recoil: Recoil is an experimental state management library for React apps. It provides several capabilities that are difficult to achieve with React alone, while being compatible with the newest features of React.
[github.com/facebookexperimental/Recoil](https://github.com/facebookexperimental/Recoil "facebookexperimental/Recoil: Recoil is an experimental state management library for React apps. It provides several capabilities that are difficult to achieve with React alone, while being compatible with the newest features of React.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

React向けのステート管理ライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript: The Definitive Guide, 7th Edition - O'Reilly Media
[shop.oreilly.com/product/0636920048633.do](http://shop.oreilly.com/product/0636920048633.do "JavaScript: The Definitive Guide, 7th Edition - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptについての書籍。
サイ本 第7版


----
