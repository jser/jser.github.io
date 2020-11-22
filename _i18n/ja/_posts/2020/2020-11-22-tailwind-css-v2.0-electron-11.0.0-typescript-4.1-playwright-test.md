---
title: "2020-11-22のJS: Tailwind CSS v2.0、Electron 11.0.0、TypeScript 4.1、playwright-test"
author: "azu"
layout: post
date : 2020-11-22T02:57:36.494Z
category: JSer
tags:
- Chrome
- browser
- proposal
- security
- XSS

---

JSer.info #515 - [Utility-First](https://tailwindcss.com/docs/utility-first)なCSSフレームワークであるTailwind CSS 2.0がリリースされました。

- [Tailwind CSS v2.0 – Tailwind CSS](https://blog.tailwindcss.com/tailwindcss-v2)

破壊的な変更としてIE11のサポートを終了、Node 10以下のサポートを終了、一部クラス名の変更などが含まれています。
機能追加としてカラーパレットの追加、ダークモードのサポート、`2xl` breakpointの追加しています。
また、フォーム向けのプラグインとして`@tailwindcss/forms`の追加、`@apply`の対応改善、`overflow-ellipsis`と` overflow-clip`の追加などもされています。

---

Electron 10.0.0がリリースされました。

- [Electron 11.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-11-0)
- [Release electron v11.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v11.0.0)

Electron 10.0.0ではApple Siliconに対応しています。

- [Apple Silicon Support | Electron Blog](https://www.electronjs.org/blog/apple-silicon)

その他には、Chromium 87/V8 8.7/Node.js 12.18.3へのアップデートなどが含まれています。

---

TypeScript 4.1が正式にリリースされました。

- [Announcing TypeScript 4.1 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/)

大きな変更としてTemplate Literal Typesがサポートされています。
Template Literal Typesは型定義の表現をかなり強力にするため、DSLに対する型定義などに使われそうです。

- [ghoullier/awesome-template-literal-types: Curated list of awesome Template Literal Types examples](https://github.com/ghoullier/awesome-template-literal-types)

また、Mapped TypesでKeyのRemappingをサポート、再帰的なConditional Typesのサポート。 インデックスアクセス時に`undefined`となる可能性を考慮する`noUncheckedIndexedAccess`オプションの追加。
その他には、`baseUrl`なしで`paths`オプションを指定に対応、新しいJSXの変換に対応しています。
破壊的な変更として、`new Promise`における`resolve`関数の引数がOptionalではなるといった変更も含まれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Tailwind CSS v2.0 – Tailwind CSS
[blog.tailwindcss.com/tailwindcss-v2](https://blog.tailwindcss.com/tailwindcss-v2 "Tailwind CSS v2.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS 2.0リリース。
破壊的な変更としてIE11のサポートを終了、Node 10以下のサポートを終了、一部クラス名の変更など。
機能追加としてカラーパレットの追加、ダークモードのサポート、`2xl` breakpointの追加。
フォーム向けのプラグインとして`@tailwindcss/forms`の追加、`@apply`の対応改善、`overflow-ellipsis`と` overflow-clip`の追加など


----

## Firefox 83 is upon us - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/11/firefox-83-is-upon-us/](https://hacks.mozilla.org/2020/11/firefox-83-is-upon-us/ "Firefox 83 is upon us - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 83リリース。
開発者ツールで`scroll`のデバッグ改善、
CSS `conic-gradient`関数のサポート、WebRenderのサポート対象の追加など

- [Firefox 83 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/83 "Firefox 83 for developers - Mozilla | MDN")

----

## Electron 11.0.0 | Electron Blog
[www.electronjs.org/blog/electron-11-0](https://www.electronjs.org/blog/electron-11-0 "Electron 11.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 11.0.0リリース。
Chromium 87/V8 8.7/Node.js 12.18.3へアップデート。
Apple M1のサポート、`app.createThumbnailFromPath()`、`webContents.forcefullyCrashRenderer()`の追加など

- [Release electron v11.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v11.0.0 "Release electron v11.0.0 · electron/electron")

----

## New in Chrome 87  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/11/nic87](https://developers.google.com/web/updates/2020/11/nic87 "New in Chrome 87  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 87リリース。
DevToolsにWebAuthnタブを追加、カメラのpan/tilt/zoomのサポート、Service WorkerでRangeリクエストのサポート。
Cookie Store API、`Intl.Segmenter`、`isInputPending`、`postMessage`にStreamsを渡せるようになるなど。
また、FTPをデフォルトで無効化。

- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D87 "Chrome Platform Status")

----

## Announcing TypeScript 4.1 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-1/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/ "Announcing TypeScript 4.1 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.1リリース。
Template Literal Types、Mapped TypesでKeyのRemappingをサポート、再帰的なConditional Typesのサポート。 インデックスアクセス時に`undefined`となる可能性を考慮する`noUncheckedIndexedAccess`オプションの追加。
`baseUrl`なしで`paths`オプションを指定できるように、新しいJSXの変換に対応。
破壊的な変更として、`new Promise`における`resolve`関数の引数がOptionalではなくなるなど


----

## Prettier 2.2: new JavaScript parsers, TS 4.1 and ESM standalone bundles · Prettier
[prettier.io/blog/2020/11/20/2.2.0.html](https://prettier.io/blog/2020/11/20/2.2.0.html "Prettier 2.2: new JavaScript parsers, TS 4.1 and ESM standalone bundles · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.2.リリース。
JavaScriptで`espree`と`meriyah`のパーサをサポート、TypeScript 4.1サポート、standalone版を同梱するようになるなど


----

## Release Notes for Safari Technology Preview 116 | WebKit
[webkit.org/blog/11348/release-notes-for-safari-technology-preview-116/](https://webkit.org/blog/11348/release-notes-for-safari-technology-preview-116/ "Release Notes for Safari Technology Preview 116 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 116リリース。
AudioWorklet APIをデフォルトで有効化、MediaRecorderの改善、Storage Access APIをper frameからper pageに変更など


----

## ECMAScript proposal updates @ 2020-11 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/11/22/ecmascript-proposal-updat](https://ecmascript-daily.github.io/ecmascript/2020/11/22/ecmascript-proposal-updat "ECMAScript proposal updates @ 2020-11 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2020-11におけるTC39 MeetingでのECMAScript Proposalのステータ変更のまとめ


----
<h1 class="site-genre">アーティクル</h1>

----

## Back/forward cache
[web.dev/bfcache/](https://web.dev/bfcache/ "Back/forward cache")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 87(Android)からcross-siteにおけるナビゲーションでBFCacheが有効化される。
BFCacheの動作、BFCacheで表示されたかの判定方法、BFCacheされない条件とBFCacheからの処理の再開方法について。
また、Google Analyticsのアクセス解析とBFCache、パフォーマンス計測に対する影響についてなど


----

## Web 技術の調査方法 | blog.jxck.io
[blog.jxck.io/entries/2020-11-19/how-to-track-web-standards.html](https://blog.jxck.io/entries/2020-11-19/how-to-track-web-standards.html "Web 技術の調査方法 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span> <span class="jser-tag">spec</span> <span class="jser-tag">proposal</span></p>

ウェブ技術に関連する仕様、ステータス、議論内容の調べ方について。
Browser、IETF、W3C/WHAWG、TC39について


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## BlackFan/client-side-prototype-pollution: Prototype Pollution and useful Script Gadgets
[github.com/BlackFan/client-side-prototype-pollution](https://github.com/BlackFan/client-side-prototype-pollution "BlackFan/client-side-prototype-pollution: Prototype Pollution and useful Script Gadgets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">XSS</span></p>

Prototype Pollution攻撃の事例を集めたリポジトリ。
さまざまなライブラリに対してのPrototype Pollutionのコード例をまとめている


----

## PrimeFaces – Ultimate UI Framework
[www.primefaces.org/](https://www.primefaces.org/ "PrimeFaces – Ultimate UI Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span> <span class="jser-tag">Java</span></p>

Angular, React, Vue, JSFに対応したUIフレームワーク


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## 101arrowz/fflate: High performance (de)compression in an 8kB package
[github.com/101arrowz/fflate](https://github.com/101arrowz/fflate "101arrowz/fflate: High performance (de)compression in an 8kB package")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

deflate,gzip,zlibのcompress/decompressをサポートしているライブラリ。
ファイルサイズの小ささとパフォーマンスを主な目的としていて、Workerでの非同期処理にも対応している


----

## microsoft/playwright-test: Build a cross-browser end-to-end test suite with Playwright.
[github.com/microsoft/playwright-test](https://github.com/microsoft/playwright-test "microsoft/playwright-test: Build a cross-browser end-to-end test suite with Playwright.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

Playwrightを使ったE2Eテストフレームワーク。
JestライクなAssertion、PlaywrightとFolioを使ったテスト、Snapshotテストとしてビジュアルテスティングをサポートしている。

- [microsoft/folio: A customizable test framework to build your own test frameworks](https://github.com/microsoft/folio "microsoft/folio: A customizable test framework to build your own test frameworks")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mkay581/cookie-store: A polyfill for the Cookie Store API
[github.com/mkay581/cookie-store](https://github.com/mkay581/cookie-store "mkay581/cookie-store: A polyfill for the Cookie Store API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span></p>

Cookie Store API のPolyfillライブラリ


----

## microsoft/folio: A customizable test framework to build your own test frameworks
[github.com/microsoft/folio](https://github.com/microsoft/folio "microsoft/folio: A customizable test framework to build your own test frameworks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

テストフレームワークを作るためのテストフレームワーク。
Test Fixture、Annotation APIでFlaky Testsの宣言やリトライ、テストの生成などを行える


----

## kuu/hls-parser: A simple library to read/write HLS playlists
[github.com/kuu/hls-parser](https://github.com/kuu/hls-parser "kuu/hls-parser: A simple library to read/write HLS playlists")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HLS playlistのパーサ、ジェネレーターライブラリ。
Apple Low-Latency HLS形式もサポートしている


----

## ceifa/wasmoon: A real lua VM with JS bindings made with webassembly
[github.com/ceifa/wasmoon](https://github.com/ceifa/wasmoon "ceifa/wasmoon: A real lua VM with JS bindings made with webassembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Lua</span></p>

Lua VMをWebAssemblyに変換して、JavaScriptからLuaのコードを実行するライブラリ。


----
