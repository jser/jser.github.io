---
title: "2021-02-16のJS: TypeScript 4.2 RC、WebdriverIO v7、Nuxt.js 2.15.0"
author: "azu"
layout: post
date : 2021-02-16T03:07:05.874Z
category: JSer
tags:
- TypeScript
- Vue
- HTML
- node.js
- Fetch

---

JSer.info #527 - TypeScript 4.2 RCがリリースされています。

- [Announcing TypeScript 4.2 RC | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/)

Tuple TypesでRest Elementをサポート、Type Aliasの型追跡の仕組みを改善して表示される型が分かりやすくなるように。
また、オブジェクトではないオペランドに対して`in`演算子を利用した場合に、コンパイルエラーとなるように変更。
その他には、`noPropertyAccessFromIndexSignature`オプションの追加、`abstract new`のサポート、`--explainFiles`フラグが追加されています。

[TypeScript 4.2 Beta](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-beta/)の時点では、Template Literal式をデフォルトでTemplate Literal Typeとして扱うように変更されていました。
しかし、この挙動は[望ましくないケース](https://github.com/microsoft/TypeScript/issues/42589)もあることがわかり、revertしてデフォルトでは`string`として扱うようになっています。
4.2 RCでは、Template Literal式に `as const` をつけた場合のみ、Template Literal Typeとして扱うようになっています。

```ts
declare const yourName: string;

// 'bar' has type '`hello ${string}`'.
const bar = `hello ${yourName}` as const;
//                              ^^^^^^^^

// 'baz' has type 'string'.
const baz = `hello ${yourName}`;
```

---

WebdriverIO v7がリリースされました。

- [WebdriverIO v7 Released | WebdriverIO](https://webdriver.io/blog/2021/02/09/webdriverio-v7-released/)


Node.js 10のサポート終了、TypeScriptでの書き直し、Cucumber v7へアップデート、Lightouse連携の改善が含まれています。
`browser.checkPWA()`の追加、`@babel/register`や`ts-node`がインストールされている場合に自動的にコンパイルする[`autoCompileOpts`](https://webdriver.io/docs/configurationfile)オプションの追加などが含まれています。

---

Nuxt.js 2.15.0がリリースされています。

- [Release v2.15.0 · nuxt/nuxt.js](https://github.com/nuxt/nuxt.js/releases/tag/v2.15.0)
- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide)
- [nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js](https://github.com/nuxt-contrib/jiti)

破壊的な変更としてNode.js 10のサポート終了、`@nuxt/components` v2へのアップデートが含まれています。
`@nuxt/components` v2へのアップデートするマイグレーションガイドも公開されています。

- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide "nuxt/components: Scan and auto import components for Nuxt.js 2.13+")

その他にはYarnのPlug'n'Playのサポート、PostCSS 8をopt-inでサポートしています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v4.0.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v4.0.0](https://github.com/lerna/lerna/releases/tag/v4.0.0 "Release v4.0.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span></p>

lerna 4.0.0リリース。
Node.js 10未満のサポート終了、依存のアップデートなど


----

## Announcing TypeScript 4.2 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/ "Announcing TypeScript 4.2 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.2 RCリリース。
Tuple TypesでRest Elementをサポート、Type Aliasの型追跡の改善、オブジェクトではないオペランドに対する`in`演算子のチェックを追加。`noPropertyAccessFromIndexSignature`オプションの追加、`abstract new`のサポート、`--explainFiles`フラグの追加など


----

## Release v2.0.0 · markedjs/marked
[github.com/markedjs/marked/releases/tag/v2.0.0](https://github.com/markedjs/marked/releases/tag/v2.0.0 "Release v2.0.0 · markedjs/marked")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

marked 2.0.0リリース


----

## eBay Launches Marko 5
[tech.ebayinc.com/engineering/ebay-launches-marko-5/](https://tech.ebayinc.com/engineering/ebay-launches-marko-5/ "eBay Launches Marko 5")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">template</span> <span class="jser-tag">ReleaseNote</span></p>

Marko 5リリース。
コンパイラにBabelを使うように、webpackとRollupでのbundleに対応、`@marko/testing-library`の追加、VScodeなどのエディタ拡張のサポートなど。

- [Upgrading to Marko 5](https://markojs.com/docs/marko-5-upgrade/ "Upgrading to Marko 5")

----

## WebdriverIO v7 Released | WebdriverIO
[webdriver.io/blog/2021/02/09/webdriverio-v7-released/](https://webdriver.io/blog/2021/02/09/webdriverio-v7-released/ "WebdriverIO v7 Released | WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v7リリース。
Node.js 10のサポート終了、TypeScriptでの書き直し、Cucumber v7へアップデート、Lightouse連携の改善。
`browser.checkPWA()`の追加、`@babel/register`や`ts-node`がインストールされている場合に自動的にコンパイルする`autoCompileOpts`の追加など


----

## Release v2.15.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.15.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.15.0 "Release v2.15.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxtjs 2.15.0リリース。
Node.js 10のサポート終了、YarnのPlug'n'Playのサポート、`@nuxt/components` v2へのアップデートなど

- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide "nuxt/components: Scan and auto import components for Nuxt.js 2.13+")
- [nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js](https://github.com/nuxt-contrib/jiti "nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js")

----
<h1 class="site-genre">アーティクル</h1>

----

## Dynamic Static Typing In TypeScript — Smashing Magazine
[www.smashingmagazine.com/2021/01/dynamic-static-typing-typescript/](https://www.smashingmagazine.com/2021/01/dynamic-static-typing-typescript/ "Dynamic Static Typing In TypeScript — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">express</span></p>

expressのルーティングの型を書きながら、TypeScriptの高度な型について見ていくチュートリアル


----

## Generators in Javascript: How to use them - DEV Community 👩‍💻👨‍💻
[dev.to/karimelghamry/generators-in-javascript-how-to-use-them-372d](https://dev.to/karimelghamry/generators-in-javascript-how-to-use-them-372d "Generators in Javascript: How to use them - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

generator関数の使い方とユースケースについて


----

## Lazy Load Routes in Vue with webpack Dynamic Comments | CSS-Tricks
[css-tricks.com/lazy-load-routes-in-vue-with-webpack-dynamic-comments/](https://css-tricks.com/lazy-load-routes-in-vue-with-webpack-dynamic-comments/ "Lazy Load Routes in Vue with webpack Dynamic Comments | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

Vue Routerを使った遅延ロードについての解説記事。
webpackでのchunkの分離、`webpackChunkName`でのchunkのファイル名の指定についてなど


----

## Just(js): On Javascript Performance
[just.billywhizz.io/blog/on-javascript-performance-01/](https://just.billywhizz.io/blog/on-javascript-performance-01/ "Just(js): On Javascript Performance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">C++</span></p>

Just(js)はどのような最適化をしてTechempowerのベンチマークのスコアをあげていったかについての記事

- [Introduction - TechEmpower Framework Benchmarks](https://www.techempower.com/benchmarks/#section=intro "Introduction - TechEmpower Framework Benchmarks")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Write videos in React | Remotion
[www.remotion.dev/](https://www.remotion.dev/ "Write videos in React | Remotion")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span> <span class="jser-tag">library</span></p>

Reactを使って動画を作るための開発環境とライブラリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## tildeio/simple-html-tokenizer: A lightweight JavaScript library for tokenizing non-\`<script>\` HTML expected to be found in the \`<body>\` of a document
[github.com/tildeio/simple-html-tokenizer](https://github.com/tildeio/simple-html-tokenizer "tildeio/simple-html-tokenizer: A lightweight JavaScript library for tokenizing non-\`<script>\` HTML expected to be found in the \`<body>\` of a document")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">library</span></p>

HTMLをパースしてトークナイズするライブラリ


----

## Ethan-Arrowood/undici-fetch: A WHATWG Fetch implementation based on @nodejs/undici
[github.com/Ethan-Arrowood/undici-fetch](https://github.com/Ethan-Arrowood/undici-fetch "Ethan-Arrowood/undici-fetch: A WHATWG Fetch implementation based on @nodejs/undici")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">library</span></p>

Node.js向けのFetch APIの実装ライブラリ。
undiciをベースに実装している。

- [nodejs/undici: An HTTP/1.1 client, written from scratch for Node.js](https://github.com/nodejs/undici "nodejs/undici: An HTTP/1.1 client, written from scratch for Node.js")

----

## vercel/nft: Node.js dependency tracing utility
[github.com/vercel/nft](https://github.com/vercel/nft "vercel/nft: Node.js dependency tracing utility")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">library</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">TypeScript</span></p>

JavaScriptファイルの依存関係をトレースするライブラリ。
`node_modules`などを含むモジュールが依存するファイルパスを取得できる


----

## gzuidhof/sunder: A minimal framework for Service Workers (such as Cloudflare Workers).
[github.com/gzuidhof/sunder](https://github.com/gzuidhof/sunder "gzuidhof/sunder: A minimal framework for Service Workers (such as Cloudflare Workers).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Service WorkerやCloudflare Worker向けのルーティングライブラリ


----

## zeroturnaround/sql-formatter: A whitespace formatter for different query languages
[github.com/zeroturnaround/sql-formatter](https://github.com/zeroturnaround/sql-formatter "zeroturnaround/sql-formatter: A whitespace formatter for different query languages")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SQL</span> <span class="jser-tag">library</span></p>

JavaScriptで書かれたSQLのフォーマッター


----

## mizdra/eslint-interactive
[github.com/mizdra/eslint-interactive](https://github.com/mizdra/eslint-interactive "mizdra/eslint-interactive")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

ESLintをルールごとにチェックして、ルールごとに`--fix`での修正をインタラクティブにできるコマンドラインツール

- [rule ごとに高速に eslint --fix できるツールを作った - mizdra's blog](https://www.mizdra.net/entry/2021/02/11/211856 "rule ごとに高速に eslint --fix できるツールを作った - mizdra&#x27;s blog")

----
