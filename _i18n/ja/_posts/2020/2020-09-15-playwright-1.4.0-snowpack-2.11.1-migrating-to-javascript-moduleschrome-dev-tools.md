---
title: "2020-09-15のJS: playwright 1.4.0、snowpack 2.11.1、Migrating to JavaScript modules(Chrome Dev Tools)"
author: "azu"
layout: post
date : 2020-09-15T02:59:01.892Z
category: JSer
tags:
- playwright
- snowpack
- modules

---

JSer.info #505 - クロスブラウザの自動化ライブラリであるplaywright 1.4.0がリリースされました。

- [Release v1.4.0 · microsoft/playwright](https://github.com/microsoft/playwright/releases/tag/v1.4.0)

playwright 1.4では依存するブラウザをそれぞれChromium 86/Firefox 80/WebKit 14ベースにアップデートしています。
APIとして`elementHandle.waitForElementState()`と`elementHandle.waitForSelector()`の追加なども行われています。
その他には、実験的な機能として動画の録画機能が追加されています。

また、同時に[Playwright CLI](https://github.com/microsoft/playwright-cli)が正式リリースされています。

[Playwright CLI](https://github.com/microsoft/playwright-cli)では、操作を記録して再生するコードの生成、要素のInspect、スクリーンショット、PDFの生成などができるコマンドラインツールとなっています。

----

フロントエンド向けのビルドツールであるSnowpack 2.11.1がリリースされました。

- [Release snowpack@2.11.1 · pikapkg/snowpack](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1)

[@snowpack/plugin-optimize](https://github.com/pikapkg/snowpack/tree/master/plugins/plugin-optimize)という最適化プラグインが追加されています。
[@snowpack/plugin-optimize](https://github.com/pikapkg/snowpack/tree/master/plugins/plugin-optimize)は、[esbuild](https://github.com/evanw/esbuild)でJS、[CSSO](https://github.com/css/csso)でCSS、[HTMLMinifier](https://github.com/kangax/html-minifier)でHTMLをそれぞれ圧縮します。これに加えて[`<link rel="modulepreload">`](https://developers.google.com/web/updates/2017/12/modulepreload)を使ったプリロードに対応しています。

その他には、`build --watch`でHMR/Livereloadの対応、`@snowpack/plugin-webpack`でもHTMLのminifyする変更がされています。

----

[DevTools architecture refresh: Migrating to JavaScript modules  |  Web](https://developers.google.com/web/updates/2020/09/migrating-to-js-modules)という記事では、Chrome Dev ToolsのコードベースをES Modulesに移行した話が書かれています。

Chrome Dev Tools(元はWebKit)は、ES Modulesが策定される前から書かれているため、独自のモジュールの仕組みを持っていました。
標準化されたES Modulesのメリットなどを考慮して、どのように独自の仕組みからES Modulesへ移行していったかについて書かれています。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v14.10.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.10.0/](https://nodejs.org/en/blog/release/v14.10.0/ "Node v14.10.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 14.10.0リリース。
ランダムなintegerを返す`crypto.randomInt()`の追加、`performance.eventLoopUtilization()`の追加など


----

## Release 2.0.0 (2020-09-10) · serverless/serverless
[github.com/serverless/serverless/releases/tag/v2.0.0](https://github.com/serverless/serverless/releases/tag/v2.0.0 "Release 2.0.0 (2020-09-10) · serverless/serverless")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">serverless</span></p>

Serverless Frameworkのserverless 2.0リリース。
Node.js 10未満のサポート終了、`slss`のaliasを削除、AWSの`httoApi`の`timeout`設定の削除など


----

## Release v1.4.0 · denoland/deno
[github.com/denoland/deno/releases/tag/v1.4.0](https://github.com/denoland/deno/releases/tag/v1.4.0 "Release v1.4.0 · denoland/deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.4.0リリース。
WebSocket APIの実装、`Deno.systemMemoryInfo()`の追加。
また、unstableな機能として`deno run --watch`、`deno test --coverage`の追加など


----

## Release snowpack@2.11.1 · pikapkg/snowpack
[github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1 "Release snowpack@2.11.1 · pikapkg/snowpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

snowpack 2.11.1リリース。
esbuildなどをベースにした`@snowpack/plugin-optimize`の追加、`build --watch`でHMR/Livereloadの対応。
また、`@snowpack/plugin-webpack`でもHTMLのminifyをするようになるなど。


----

## ten1seven/what-input: A global utility for tracking the current input method (mouse/pointer, keyboard or touch).
[github.com/ten1seven/what-input](https://github.com/ten1seven/what-input "ten1seven/what-input: A global utility for tracking the current input method (mouse/pointer, keyboard or touch).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">browser</span> <span class="jser-tag">DOM</span></p>

ユーザーの入力状態をトラッキングするライブラリ。
現在の入力状態がmouse, keyboard, touchなのかを判定できる


----

## Release v1.4.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.4.0](https://github.com/microsoft/playwright/releases/tag/v1.4.0 "Release v1.4.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

playwright 1.4.0リリース。
playwright-cliを正式リリース、Chromium 86/Firefox 80/WebKit 14へアップデート。
`elementHandle.waitForElementState()`と`elementHandle.waitForSelector()`の追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## AVIF has landed - JakeArchibald.com
[jakearchibald.com/2020/avif-has-landed/](https://jakearchibald.com/2020/avif-has-landed/ "AVIF has landed - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Image</span> <span class="jser-tag">article</span></p>

AV1 video由来の画像フォーマットであるAVIFについて。
jpeg、WebP、AVIFのサイズや画質の比較。
AVIFのエンコード、デコード時間、プログレッシブ表示できないといった特徴についてなど

- [How to Use AVIF: The New Next-Gen Image Compression Format — Lightspeed](https://reachlightspeed.com/blog/using-the-new-high-performance-avif-image-format-on-the-web-today/ "How to Use AVIF: The New Next-Gen Image Compression Format — Lightspeed")

----

## DevTools architecture refresh: Migrating to JavaScript modules  |  Web
[developers.google.com/web/updates/2020/09/migrating-to-js-modules](https://developers.google.com/web/updates/2020/09/migrating-to-js-modules "DevTools architecture refresh: Migrating to JavaScript modules  |  Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">refacoring</span></p>

Chrome Dev Toolsのコードベースを独自モジュールシステムからES Modulesに移行した話。
標準であるES Modulesの利点、移行戦略、exportの変更/importの変更の段階的な移行について。
また技術的な負債により初期の見積もり(数週間)よりも大きく時間(数ヶ月)かかったことについてなど


----

## Leading-Trim: The Future of Digital Typesetting | by Ethan Wang | Microsoft Design | Aug, 2020 | Medium
[medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202](https://medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202 "Leading-Trim: The Future of Digital Typesetting | by Ethan Wang | Microsoft Design | Aug, 2020 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS `leading-trim`プロパティについて


----

## A Practical Guide to the Web Cryptography API - DEV Community 👩‍💻👨‍💻
[dev.to/voraciousdev/a-practical-guide-to-the-web-cryptography-api-4o8n](https://dev.to/voraciousdev/a-practical-guide-to-the-web-cryptography-api-4o8n "A Practical Guide to the Web Cryptography API - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Web Cryptography APIの基本的な使い方。
Encryption、Decryption、転送や保存について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## type-challenges/type-challenges: Collection of TypeScript type challenges with online judge
[github.com/type-challenges/type-challenges](https://github.com/type-challenges/type-challenges "type-challenges/type-challenges: Collection of TypeScript type challenges with online judge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tutorial</span></p>

TypeScriptの型定義の問題に挑戦できる問題集


----

## microsoft/FluidFramework: Library for building distributed, real-time collaborative web applications
[github.com/microsoft/FluidFramework](https://github.com/microsoft/FluidFramework "microsoft/FluidFramework: Library for building distributed, real-time collaborative web applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

分散型リアルタイムコラボレーションのためのウェブアプリケーションフレームワーク。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## brahmosjs/brahmos: Super charged JavaScript library with modern React API and native templates.
[github.com/brahmosjs/brahmos](https://github.com/brahmosjs/brahmos "brahmosjs/brahmos: Super charged JavaScript library with modern React API and native templates.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">jsx</span> <span class="jser-tag">library</span> <span class="jser-tag">babel</span></p>

ReactのようなAPIとJSXで記述できるUIライブラリ。
Babel pluginでJSXをTagged Template Literalに変換し、lit-htmlのような形でレンダリングする


----

## cookie-universal/packages/cookie-universal at master · microcipcip/cookie-universal
[github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal](https://github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal "cookie-universal/packages/cookie-universal at master · microcipcip/cookie-universal")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

ブラウザとNode.jsで動くCookieを扱うライブラリ。


----

## microsoft/playwright-cli: CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots.
[github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli "microsoft/playwright-cli: CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">browser</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

PlaywrightのCLI。
操作を記録して再生するコードの生成、要素のInspect、スクリーンショット、PDFの生成などの機能をもっている


----

## ngneat/edit-in-place: A flexible and unopinionated edit in place library for Angular applications
[github.com/ngneat/edit-in-place](https://github.com/ngneat/edit-in-place "ngneat/edit-in-place: A flexible and unopinionated edit in place library for Angular applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Angular</span></p>

クリックしたらその場で編集できるedit in placeを提供するAngular向けのライブラリ


----

## sabljakovich/mongoose-execution-time: Mongoose plugin for measuring and logging query execution time
[github.com/sabljakovich/mongoose-execution-time](https://github.com/sabljakovich/mongoose-execution-time "sabljakovich/mongoose-execution-time: Mongoose plugin for measuring and logging query execution time")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MongoDB</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

mongooseでqueryの実行時間をログ出力するライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript for Data Science
[js4ds.org/](https://js4ds.org/ "JavaScript for Data Science")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

データサイエンティスト向けのJavaScriptの入門書


----
