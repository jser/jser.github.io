---
title: "2020-05-07のJS: Firefox 76、Jest 26、Web Vitals"
author: "azu"
layout: post
date : 2020-05-07T04:42:34.756Z
category: JSer
tags:
- Firefox
- Jest
- Chrome
- Performance

---

JSer.info #486 - Firefox 76がリリースされました。

- [Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/)
- [Firefox 76 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/76)
- [Firefox 76 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/en-CA/releases/76/)
- [Firefox 76.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/76.0/releasenotes/)

Firefox 76では開発者ツールに多くの改善が含まれています。
特定のディレクトリをDebuggerの対象から除外できるように、"Copy stack trace"の追加、Action CableのWebScoket Inspectionのサポートなどが追加されています。

機能追加としてAudio workletsのサポート、CSS System Colorsのサポートが行われています。
その他には未知のプロトコルへのNavigation移動をブロックするように変更なども含まれています。

----

JavaScriptテストフレームワークのJest 26がリリースされました。

- [Jest 26: Tick Tock · Jest](https://jestjs.io/blog/2020/05/05/jest-26)

[@sinonjs/fake-timers](https://github.com/sinonjs/fake-timers)ベースの新しいFake Timerの追加、`it`や`describe`などをexportする`@jest/globals`の追加、Native ESMのサポートなどが含まれています。
破壊的な変更として、Node.js 8未満のサポートを終了しいくつかのコアモジュールでES5のビルドを提供しないように変更しています。
今後の変更予定として、Jest 27でデフォルトのtestRunnerを["jest-circus"](https://github.com/facebook/jest/tree/master/packages/jest-circus)に変更しenvironmentを"node"に変更する予定です。
また、Jest 28で"jest-jasmine2"と"jest-environment-jsdom"をコアから別のパッケージへと分離する予定となっています。

まとめると次のような変更が予定されています。

- [testRunner](https://jestjs.io/docs/ja/configuration#testrunner-string): [jasmine2](https://github.com/facebook/jest/tree/master/packages/jest-jasmine2) → ["circus"](https://github.com/facebook/jest/tree/master/packages/jest-circus)
- [testEnvironment](https://jestjs.io/docs/ja/configuration#testenvironment-string): [jsdom](https://github.com/facebook/jest/tree/master/packages/jest-environment-jsdom) → [node](https://github.com/facebook/jest/tree/master/packages/jest-environment-node)

----

[Web Vitals](https://web.dev/vitals/)という記事では、ウェブサイトのパフォーマンスに関する重要な指標をCore Web Vitalsという概念にまとめて、Google/Chrome系のプロダクトで利用できるようにする話が書かれています。

現在のCore Web Vitalsは次の3つの指標で構成されています。

- [Largest Contentful Paint (LCP)](https://web.dev/lcp/): ロードに関する指標
- [First Input Delay (FID)](https://web.dev/fid/): インタラクションに関する指標
- [Cumulative Layout Shift (CLS)](https://web.dev/cls/): 描画に関する指標

これらの指標を取得できる[web-vitals](https://github.com/GoogleChrome/web-vitals)というJavaScriptライブラリの提供([Performance Observer](Performance Observer)の値を利用するため[Chromeでしか取れない指標](https://github.com/GoogleChrome/web-vitals#browser-support)もある)や[ブラウザ拡張機能](https://github.com/GoogleChrome/web-vitals-extension)の提供なども行っています。

今後は[Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)(既に対応済み)、[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)、Search Console などのツールでもこの指標を利用できるようにしていくとのことです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/](https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/ "Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 76リリース。
開発者ツールの改善、Audio workletsのサポート、CSS System Colorsのサポート、未知のプロトコルへのNavigation移動をブロックするように変更など

- [Firefox 76 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/76 "Firefox 76 for developers - Mozilla | MDN")
- [Firefox 76 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/en-CA/releases/76/ "Firefox 76 Site Compatibility | Firefox Site Compatibility")
- [Firefox 76.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/76.0/releasenotes/ "Firefox 76.0, See All New Features, Updates and Fixes")

----

## Node v12.16.3 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.16.3/](https://nodejs.org/en/blog/release/v12.16.3/ "Node v12.16.3 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.16.3リリース。
Experimentalで実装されているconditional exportsに関するwarningメッセージが削除された


----

## Announcing TypeScript 3.9 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-9-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9-rc/ "Announcing TypeScript 3.9 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.9 RCリリース。
`Promise.all`の型改善、ビルドパフォーマンスの改善、Type Errorとなることを期待する`// @ts-expect-error`コメントの追加など。 また、ECMAScript仕様にあわせてGetter/Setterをトランスパイルするように変更など
`awaited` typeは延期


----

## jQuery 3.5.1 Released: Fixing a Regression | Official jQuery Blog
[blog.jquery.com/2020/05/04/jquery-3-5-1-released-fixing-a-regression/](http://blog.jquery.com/2020/05/04/jquery-3-5-1-released-fixing-a-regression/ "jQuery 3.5.1 Released: Fixing a Regression | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.5.1リリース。
jQuery 3.5.0でのリグレッションを修正。3.5ではXSSに対するセキュリティ修正のため、意図的に後方互換性がない部分も含まれる


----

## Jest 26: Tick Tock · Jest
[jestjs.io/blog/2020/05/05/jest-26](https://jestjs.io/blog/2020/05/05/jest-26 "Jest 26: Tick Tock · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 26リリース。
`@sinonjs/fake-timers`ベースの新しいFake Timerの追加、`it`や`describe`などをexportする`@jest/globals`の追加、Native ESMのサポートなど。
いくつかのコアモジュールでES5のビルドを提供しないように変更し、Node.js 8未満のサポートを終了。
今後の変更として、Jest 27でデフォルトのtestRunnerを"jest-circus"に変更しenvironmentを"node"に変更する。
また、Jest 28で"jest-jasmine2"と"jest-environment-jsdom"をコアから別のパッケージへと分離する予定。


----

## Release v1.6.0 · mdx-js/mdx
[github.com/mdx-js/mdx/releases/tag/v1.6.0](https://github.com/mdx-js/mdx/releases/tag/v1.6.0 "Release v1.6.0 · mdx-js/mdx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">ReleaseNote</span></p>

MarkdownにJSXを拡張するMDX 1.6.0リリース。
Vueをベータサポート


----
<h1 class="site-genre">アーティクル</h1>

----

## What’s in that .wasm? Introducing: wasm-decompile · V8
[v8.dev/blog/wasm-decompile](https://v8.dev/blog/wasm-decompile "What’s in that .wasm? Introducing: wasm-decompile · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

`wasm-decompile`でのWebAssemblyのデコンパイルについて

- [wabt/decompiler.md at master · WebAssembly/wabt](https://github.com/WebAssembly/wabt/blob/master/docs/decompiler.md "wabt/decompiler.md at master · WebAssembly/wabt")

----

## window.location Cheatsheet - DEV Community 👩‍💻👨‍💻
[dev.to/samanthaming/window-location-cheatsheet-4edl](https://dev.to/samanthaming/window-location-cheatsheet-4edl "window.location Cheatsheet - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">チートシート</span> <span class="jser-tag">article</span></p>

`window.location`オブジェクトのプロパティやメソッドの挙動を解説している記事


----

## Improved Next.js and Gatsby page load performance with granular chunking
[web.dev/granular-chunking-nextjs/](https://web.dev/granular-chunking-nextjs/ "Improved Next.js and Gatsby page load performance with granular chunking")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpackの`SplitChunksPlugin`を行うことでNext.js 9.2やGatsbyのページ間でのCommon chunkを分けた話。
HTTP/2における`maxInitialRequests`の設定によるcリクエスト数の増加の影響調査、ルーティングとchunkの分離についてなど

- [feat(gatsby): enable granular chunks by wardpeet · Pull Request #22253 · gatsbyjs/gatsby](https://github.com/gatsbyjs/gatsby/pull/22253 "feat(gatsby): enable granular chunks by wardpeet · Pull Request #22253 · gatsbyjs/gatsby")

----

## Web Vitals
[web.dev/vitals/](https://web.dev/vitals/ "Web Vitals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

ウェブページのパフォーマンス計測の重なメトリクスをCore Web Vitalsとしてまとめたという話。
Core Web VitalsはLargest Contentful Paint(LCP)、First Input Delay(FID)、Cumulative Layout Shift(CLS)。
同時に`web-vitals`というそれぞれのメトリクスを計測できるライブラリも提供し、 PageSpeed InsightsやSearch Consoleなどもそれぞれ対応していく予定

- [GoogleChrome/web-vitals: Essential metrics for a healthy site.](https://github.com/GoogleChrome/web-vitals "GoogleChrome/web-vitals: Essential metrics for a healthy site.")
- [GoogleChrome/web-vitals-extension: A Chrome extension to measure essential metrics for a healthy site](https://github.com/GoogleChrome/web-vitals-extension "GoogleChrome/web-vitals-extension: A Chrome extension to measure essential metrics for a healthy site")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## rinsuki/play-flv-in-browser: Play FLV in Browser!
[github.com/rinsuki/play-flv-in-browser](https://github.com/rinsuki/play-flv-in-browser "rinsuki/play-flv-in-browser: Play FLV in Browser!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flash</span> <span class="jser-tag">video</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

ffmepgをWebAssemblyにコンパイルしたものを使ってflv/mp4をブラウザで再生するデモ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## antfu/i18n-ally: 🌍 All in one i18n extension for VS Code
[github.com/antfu/i18n-ally](https://github.com/antfu/i18n-ally "antfu/i18n-ally: 🌍 All in one i18n extension for VS Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">i18n</span> <span class="jser-tag">Extension</span> <span class="jser-tag">EmEditor</span></p>

VSCode上に作られたi18n編集システム。
エディタ上で翻訳キーの代わりに翻訳結果の表示などローカライズの支援をする拡張機能。
さまざまなフレームワークに対応している


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## addaleax/gen-esm-wrapper: Generate ESM wrapper files for CommonJS modules
[github.com/addaleax/gen-esm-wrapper](https://github.com/addaleax/gen-esm-wrapper "addaleax/gen-esm-wrapper: Generate ESM wrapper files for CommonJS modules")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span></p>

CommonJSからESM Wrapperを生成するツール


----

## jesseduffield/lazynpm: terminal UI for npm
[github.com/jesseduffield/lazynpm](https://github.com/jesseduffield/lazynpm "jesseduffield/lazynpm: terminal UI for npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">UI</span></p>

lazygit, lazydockerライクなnpmのターミナルUIツール。
パッケージの情報表示、パッケージの管理、スクリプトの実行など


----

## Quantum JavaScript (Q.js)
[quantumjavascript.app/](https://quantumjavascript.app/ "Quantum JavaScript (Q.js)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

量子回路シミュレーターライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Tackling TypeScript: Upgrading from JavaScript
[exploringjs.com/tackling-ts/](https://exploringjs.com/tackling-ts/ "Tackling TypeScript: Upgrading from JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

Dr. AxelによるTypeScriptの入門書


----
