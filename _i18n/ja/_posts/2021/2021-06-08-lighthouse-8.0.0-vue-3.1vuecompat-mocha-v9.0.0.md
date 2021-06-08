---
title: "2021-06-08のJS: Lighthouse 8.0.0(スコア計算の変更)、Vue 3.1(@vue/compat)、 Mocha v9.0.0"
author: "azu"
layout: post
date : 2021-06-08T02:48:58.962Z
category: JSer
tags:
- Chrome
- node.js
- TypeScript
- browser
- WebAssembly

---

JSer.info #543 - Lighthouse 8.0.0がリリースされました。

- [Release v8.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0)

Lighthouse 8.0.0ではパフォーマンススコアの計算式が変更されています。
詳細は次のドキュメントにかかれていますが、今まで実験的だったCumulative Layout Shift (CLS)の比重が5%から15%へと増加しています。それにあわせて他のスコアの比重も変化しています。

- [lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/v8-perf-faq.md)

機能追加として、レポートをメトリクス別にフィルターできるように、`csp-xss`のAuditの追加なども含まれています。

----

Vue 3.1.0がリリースされました。

- [Release v3.1.0 Pluto · vuejs/vue-next](https://github.com/vuejs/vue-next/releases/tag/v3.1.0)

Vue 3.1.0では`@vue/compat`というVue 2の互換APIを実装したパッケージが公開されています。
既存のVue 2.xで書かれたアプリケーションをVue 3上で動かすためのMigration Buildとなっています。

詳細は次のドキュメントで解説されていますが、Vue 2.xの時点での公開APIのみを実装した互換ビルドであるため、
一部ライブラリは動かないことなどが書かれています。

- [Migration Build | Vue.js](https://v3.vuejs.org/guide/migration/migration-build.html)

また、今後の予定では、Vue 3で実装されたComposition APIなどをVue 2.xへとバックポートしたVue 2.7がリリースされる予定となっています。

----

JavaScriptテストフレームワークのMocha 9.0.0がリリースされました。

- [Release v9.0.0 · mochajs/mocha](https://github.com/mochajs/mocha/releases/tag/v9.0.0)

Mocha 9ではNode.js 10のサポート終了し、ESM(ECMAScript Modules)をネイティブサポートしています。
ESMでの読み込みを試してみてから、読み込めなかった場合はCJS(CommonJS)で読み込むようなfallbackとなっています。

- [import-first loading of test files by giltayar · Pull Request #4635 · mochajs/mocha](https://github.com/mochajs/mocha/pull/4635)

その他には、`--dry-run`オプションのサポート、非推奨だった`utils.lookupFiles()`の削除などが含まれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v10.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v10.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v10.0.0 "Release v10.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

puppeteer 10.0.0リリース。
Node.js 10のサポート終了、起動してから最初のページのロード待ちをするかどうかを決める`waitForInitialPage`オプションの追加など


----

## Release v8.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0 "Release v8.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 8.0.0リリース。
パフォーマンススコアの計算式の変更、レポートをメトリクス別にフィルターできるように、`csp-xss`のAuditの追加など。

- [lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/v8-perf-faq.md "lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse")

----

## Electron 13.0.0 | Electron Blog
[www.electronjs.org/blog/electron-13-0](https://www.electronjs.org/blog/electron-13-0 "Electron 13.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 13.0.0リリース。
Chrome 91、Node.js 14.16.0、V8 9.1へアップデート。
`process.contextIsolated`、`session.storagePat`、`process.contextId`の追加。
WebContentsの`new-window`イベントがDeprecatedとなり`webContents.setWindowOpenHandler()`を推奨するようになるなど


----

## Looking fine with Firefox 89 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/06/looking-fine-with-firefox-89/](https://hacks.mozilla.org/2021/06/looking-fine-with-firefox-89/ "Looking fine with Firefox 89 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 89リリース。
Media Queryの`forced-colors`、フォントロード時の視差を調整する`line-gap-override`/`ascent-override`/`descent-override`の実装。
Top-level `await`をデフォルトで有効化、64bitマシンでArrayBufferが2GB以上のサイズを扱えるように、`PerformanceEventTiming`のサポートなど。

- [Firefox 89 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/89 "Firefox 89 for developers - Mozilla | MDN")
- [Firefox 89.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/89.0/releasenotes/ "Firefox 89.0, See All New Features, Updates and Fixes")

----

## Chromium Blog: Chrome 92: Web Apps as File Handlers, New JavaScript Features, and More
[blog.chromium.org/2021/06/chrome-92-web-apps-as-file-handlers-new.html](https://blog.chromium.org/2021/06/chrome-92-web-apps-as-file-handlers-new.html "Chromium Blog: Chrome 92: Web Apps as File Handlers, New JavaScript Features, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 92 betaリリース。
Origin TrialとしてFile Handling API、Shared Element Transitions。
`@font-face`の`size-adjust`、V8 9.2へのアップデート、SharedArrayBuffersがCross Origin Isolateされたページに限定されるなど


----

## Release v9.0.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v9.0.0](https://github.com/mochajs/mocha/releases/tag/v9.0.0 "Release v9.0.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 9.0.0リリース。
Node.js 10のサポート終了、ESMサポート、`--dry-run`オプションのサポート。
非推奨だった`utils.lookupFiles()`の削除など


----

## Node v16.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.3.0/](https://nodejs.org/en/blog/release/v16.3.0/ "Node v16.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.3.0リリース。
npm 7.15.1へのアップデートでnpmのworkspaceコマンドが色々追加された


----

## Release v3.1.0 Pluto · vuejs/vue-next
[github.com/vuejs/vue-next/releases/tag/v3.1.0](https://github.com/vuejs/vue-next/releases/tag/v3.1.0 "Release v3.1.0 Pluto · vuejs/vue-next")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 3.1.0リリース。
Vue 2からのMigration Buildとして`@vue/compat`の追加。
`app.config.isCustomElement`とコンポーネントの`delimiters`オプションを非推奨化してコンポーネントの`compilerOptions`オプションをサポート。
`v-is`を非推奨化して`is="vue:xxx"`のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## What&#039;s New In DevTools (Chrome 92) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-92/](https://developer.chrome.com/blog/new-in-devtools-92/ "What&#039;s New In DevTools (Chrome 92) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 92のDevToolsの変更点について。
CSS gridエディタ、REPL内で`const`の再定義ができるように、Source order viewerの追加。
CORSのエラーメッセージの改善、NetworkのフィルターにWasm typeを追加、UA Client Hintの対応。
ExperimentsとしてChrome DevTools Protocolを見るProtocol Monitor、Puppeteer Recorderの追加など


----

## UI Security - Thinking Outside the Viewport | Microsoft Browser Vulnerability Research
[microsoftedge.github.io/edgevr/posts/ui-security-thinking-outside-the-viewport/](https://microsoftedge.github.io/edgevr/posts/ui-security-thinking-outside-the-viewport/ "UI Security - Thinking Outside the Viewport | Microsoft Browser Vulnerability Research")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

ブラウザUIのセキュリティバグを例に、UIにおけるセキュリティバグをどのようにチェックするかについて解説している記事


----

## Making JavaScript run fast on WebAssembly | Bytecode Alliance
[bytecodealliance.org/articles/making-javascript-run-fast-on-webassembly](https://bytecodealliance.org/articles/making-javascript-run-fast-on-webassembly "Making JavaScript run fast on WebAssembly | Bytecode Alliance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Wasmで動くJavaScriptエンジンを作る話。
WasmをサンドボックスとしてJavaScriptを実行できる点と、JavaScriptエンジンの初期化とRuntimeの高速化の手法について書かれている。

- [bytecodealliance/wizer: The WebAssembly Pre-Initializer](https://github.com/bytecodealliance/wizer "bytecodealliance/wizer: The WebAssembly Pre-Initializer")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## An introduction to WebAssembly for JavaScript Developers
[pascalpares.appspot.ovh/webassembly-for-javascript-developers/](https://pascalpares.appspot.ovh/webassembly-for-javascript-developers/ "An introduction to WebAssembly for JavaScript Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

WebAssemblyのJavaScript APIについての解説記事。
Wasmファイルのロード、コンパイル、WasmからJSのコールバック関数の呼び出し、Dynamic Link、グローバル変数、文字列の渡し方、Shared Memory Bufferなどについて


----

## progfay/benefit-from-end-of-ie: List of APIs that will be available due to IE termination
[github.com/progfay/benefit-from-end-of-ie](https://github.com/progfay/benefit-from-end-of-ie "progfay/benefit-from-end-of-ie: List of APIs that will be available due to IE termination")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">document</span></p>

IEのみがサポートしていないAPIをまとめたもの。
MDNのデータをベースにHTML、JS、CSS、SVGのAPIを一覧できる

----


## Node.js API Table
[nodejs-api-table.netlify.app/](https://nodejs-api-table.netlify.app/ "Node.js API Table")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">API</span> <span class="jser-tag">document</span></p>

Node.jsのモジュールやAPIがどのバージョンで追加されたのかを一覧できるサイト。

- [Next.js で Node.js の API がいつ入ったのかわかる表を作る](https://zenn.dev/sosukesuzuki/articles/f00bc24600f2d8 "Next.js で Node.js の API がいつ入ったのかわかる表を作る")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## devongovett/dprint-node: A node API for the dprint TypeScript and JavaScript code formatter
[github.com/devongovett/dprint-node](https://github.com/devongovett/dprint-node "devongovett/dprint-node: A node API for the dprint TypeScript and JavaScript code formatter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">library</span></p>

Rustで書かれたdprintを使ったコードフォーマッター


----

## htmlplus/core: HTMLPLUS is a native, framework-less, and lightweight library that is purely developed with Javascript. All HTMLPLUS components are customizable and configurable.
[github.com/htmlplus/core](https://github.com/htmlplus/core "htmlplus/core: HTMLPLUS is a native, framework-less, and lightweight library that is purely developed with Javascript. All HTMLPLUS components are customizable and configurable.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Web Componentsで作られたUIライブラリ。
ReactとVue向けのバインディングも提供している


----

## kawmra/typist-json: A simple runtime JSON type checker.
[github.com/kawmra/typist-json](https://github.com/kawmra/typist-json "kawmra/typist-json: A simple runtime JSON type checker.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

スキーマを定義するビルダー関数とチェッカーライブラリ。
定義したスキーマをTypeScriptの型として利用できる。

- [TypeScript 向けの軽量ランタイム JSON 型チェッカーを作った](https://zenn.dev/kawmra/articles/0aad8dca56f1da "TypeScript 向けの軽量ランタイム JSON 型チェッカーを作った")

----

## EvandroLG/ts-audio: ts-audio is an agnostic library that makes it easy to work with AudioContext and create audio playlists in the browser
[github.com/EvandroLG/ts-audio](https://github.com/EvandroLG/ts-audio "EvandroLG/ts-audio: ts-audio is an agnostic library that makes it easy to work with AudioContext and create audio playlists in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">audio</span> <span class="jser-tag">TypeScript</span></p>

AudioContext APIを使った音楽再生ライブラリ。
複数の音声の連続再生などをサポートしている


----

## Testy/TestyTs: ✔️ Modern TypeScript testing framework.
[github.com/Testy/TestyTs](https://github.com/Testy/TestyTs "Testy/TestyTs: ✔️ Modern TypeScript testing framework.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Decoratorを使ったTypeScriptテストフレームワーク


----
