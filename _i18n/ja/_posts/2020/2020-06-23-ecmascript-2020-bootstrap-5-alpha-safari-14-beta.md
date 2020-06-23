---
title: "2020-06-23のJS: ECMAScript 2020リリース、Bootstrap 5 alpha、Safari 14 Beta"
author: "azu"
layout: post
date : 2020-06-23T02:59:04.220Z
category: JSer
tags:
- ECMAScript
- Bootstrap
- CSS
- Safari

---

JSer.info #493 - ECMAScript 2020がEcma internationalの119th General Assemblyで承認され、正式にリリースされました。

- [Ecma latest news](https://www.ecma-international.org/news/index.html)
- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md)

ECMAScript 2020では次のような変更が含まれています。

- for-in mechanics - for...inやObject.keysの順番が仕様で定義された
- `export * as ns from "mod"` - 構文の追加
- `String.prototype.matchAll` - マッチしたすべての文字列をイテレータで返す
- `globalThis` - ブラウザの`window`、Node.jsの`global`へのProxy
- BigInt - 巨大な整数/7番目のプリミティブ型
- Optional chaining - `obj?.prop`
- Nullish coalescing Operator - `??`
- `Promise.allSettled` - `Promise.all`とは異なりRejectedも含まれてすべての完了を待つ
- `import()` - Dynamic Import
- `import.meta` - `import.meta.url`などが定義されるオブジェクト

ECMAScriptの策定プロセス/リリースプロセスについては次を参照してください。

- [ECMAScript · JavaScript Primer #jsprimer](https://jsprimer.net/basic/ecmascript/)

Releated:

- [ECMAScript 2020の対応 · Issue #1145 · asciidwango/js-primer](https://github.com/asciidwango/js-primer/issues/1145)
- [ECMAScript 2020: the final feature set](https://2ality.com/2019/12/ecmascript-2020.html)

----

Bootstrap 5 alphaがリリースされました。

- [Bootstrap 5 alpha! | Bootstrap Blog](https://blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/)

破壊的な変更としてjQueryの依存削除、IEのサポートが終了されています。
CSS Custom Propertiesでのカスタマイズの対応、formやgridの対応改善、Utilities APIの追加なども含まれています。

----

Safari 14 Betaのリリースノートが公開されています。

- [Safari 14 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes)

WebExtensionsの拡張に対応、HTTP/3のサポート、Flashのサポート終了が含まれています。
JavaScriptでは、BigInt、EventTargetの継承、Public class fieldのサポート。
CSSでは、`is()`、`:where()`、image-orientationのサポート。
その他にはWebP、Picture in Pictureのサポートなども行われています。

詳しくはWWDC20での動画で発表される予定です。

- [Safari and Web - Discover - Apple Developer](https://developer.apple.com/news/?id=e4u1mtfu)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Ecma latest news
[www.ecma-international.org/news/index.html](https://www.ecma-international.org/news/index.html "Ecma latest news")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2020とECMAScript 2020 Internationalization APIが正式リリース


----

## Bootstrap 5 alpha! | Bootstrap Blog
[blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/](https://blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/ "Bootstrap 5 alpha! | Bootstrap Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 5αリリース。
jQueryの依存削除、IEのサポート終了、CSS Custom Propertiesでのカスタマイズの対応、formやgridの対応改善、Utilities APIの追加など


----

## Release v2.13.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.13.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.13.0 "Release v2.13.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js 2.13.0リリース。
`target: static`の追加、`.env`をビルトインサポート、`@nuxt/components`でのAuto Discoryオプションの追加など。
また、Nuxt.jsの利用情報を送信するようになり、オプトアウトのためのオプションの追加など

- [nuxt/telemetry: Nuxt Telemetry](https://github.com/nuxt/telemetry#opting-out "nuxt/telemetry: Nuxt Telemetry")
- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components "nuxt/components: Scan and auto import components for Nuxt.js 2.13+")

----

## 📦 Parcel 2 beta 1: improved stability, tree shaking, source map performance, and more! 🚀
[medium.com/@devongovett/parcel-2-beta-1-improved-stability-tree-shaking-source-map-performance-and-more-78179779e8b7](https://medium.com/@devongovett/parcel-2-beta-1-improved-stability-tree-shaking-source-map-performance-and-more-78179779e8b7 "📦 Parcel 2 beta 1: improved stability, tree shaking, source map performance, and more! 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel 2 beta 1リリース。
Tree shakingのデフォルト有効化、Source Mapのパフォーマンス改善Content hashingの改善、モジュール解決エラーの改善など。
非互換な変更としてはConfigの変更、サーバモードでも`dist`ディレクトリに出力するように変更、Plugin APIの変更なども含まれている


----

## jspm.dev Release - jspm.org
[jspm.org/jspm-dev-release](https://jspm.org/jspm-dev-release "jspm.dev Release - jspm.org")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">news</span> <span class="jser-tag">cdn</span></p>

jspmのCDNとしてdev.jspm.ioの代わりとなるjspm.devが公開された。
ES Modulesに対して最適化されたCDNで、Rollupを使ってレスポンス時間が短くなるように事前に最適化している。
パッケージのSubpathに対応、Node.jsの`export`フィールドなどに対応している


----

## Dojo 7 Has Arrived
[dojo.io/blog/version-7-dojo](https://dojo.io/blog/version-7-dojo "Dojo 7 Has Arrived")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Dojo 7リリース。
WidgetsをTSXで書けるように、Custom Elements の対応改善、データとWidgetsを切り離して扱えるDojo Resourcesの追加、i18nの対応改善など

- [Announcing Dojo 7 Widgets](https://dojo.io/blog/version-7-dojo-widgets "Announcing Dojo 7 Widgets")

----

## ESLint v7.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/06/eslint-v7.3.0-released](https://eslint.org/blog/2020/06/eslint-v7.3.0-released "ESLint v7.3.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 7.3.0リリース。
新しいルールとして`no-promise-executor-return`と`no-unreachable-loop`の追加。
設定値にJSONで扱えない値を入れると正しく動作しなくなるリグレッションが含まれるため修正バージョンもリリースされる予定。

- [ESLint v7.3.0 - Qiita](https://qiita.com/mysticatea/items/e155bd2fee35c22ee423 "ESLint v7.3.0 - Qiita")

----

## vitejs/vite: Native-ESM powered web dev build tool. It's fast.
[github.com/vitejs/vite](https://github.com/vitejs/vite "vitejs/vite: Native-ESM powered web dev build tool. It's fast.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Tools</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 1.0.0βリリース


----

## Safari 14 Beta Release Notes | Apple Developer Documentation
[developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes "Safari 14 Beta Release Notes | Apple Developer Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 14ベータの変更点。
WebExtensionsの拡張に対応、HTTP/3のサポート、Flashのサポート終了。
JavaScriptでは、BigInt、EventTargetの継承、Public class fieldのサポート。
CSSでは、`is()`、`:where()`、image-orientationのサポート。
その他にはWebP、Picture in Pictureのサポートなど

- [Safari Web Extensions | Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari_web_extensions "Safari Web Extensions | Apple Developer Documentation")
- [Browser support for JavaScript APIs - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs "Browser support for JavaScript APIs - Mozilla | MDN")

----
<h1 class="site-genre">アーティクル</h1>

----

## JavaScriptライブラリを読むときのコツ | blog.ojisan.io
[blog.ojisan.io/how-to-read-js](https://blog.ojisan.io/how-to-read-js "JavaScriptライブラリを読むときのコツ | blog.ojisan.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptライブラリのコードリーディングについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## WebAssembly and the Elusive Universal Binary
[kripken.github.io/talks/2020/universal.html#/](https://kripken.github.io/talks/2020/universal.html#/ "WebAssembly and the Elusive Universal Binary")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">slide</span></p>

WebAssemblyでのCross PlatformなUniversal Binaryについてのスライド。
ネイティブバイナリに比べて28%程度の速度低下でUniversal Binaryが実現できているという話


----

## slides/ModuleFederationWebpack5.md at master · sokra/slides
[github.com/sokra/slides/blob/master/content/ModuleFederationWebpack5.md](https://github.com/sokra/slides/blob/master/content/ModuleFederationWebpack5.md "slides/ModuleFederationWebpack5.md at master · sokra/slides")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">slide</span></p>

webpack 5で導入予定のModule Federationについてのスライド。
Federationでの最適化や動作、既存のDLLやExternalsとの違いについて話されている

- [Module Federation | webpack](https://webpack.js.org/concepts/module-federation/ "Module Federation | webpack")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## milesj/interweave: 🌀 React library to safely render HTML, filter attributes, autowrap text with matchers, render emoji characters, and much more.
[github.com/milesj/interweave](https://github.com/milesj/interweave "milesj/interweave: 🌀 React library to safely render HTML, filter attributes, autowrap text with matchers, render emoji characters, and much more.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">HTML</span> <span class="jser-tag">library</span></p>

HTML文字列をレンダリングできるReactコンポーネント。
指定したタグのみを許可したり、自動リンク、絵文字の対応、SSRなどに対応している


----

## marcello3d/lascaux-sketch: Lascaux Sketch 2 is an open source web-based digital painting tool
[github.com/marcello3d/lascaux-sketch](https://github.com/marcello3d/lascaux-sketch "marcello3d/lascaux-sketch: Lascaux Sketch 2 is an open source web-based digital painting tool")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">Tools</span></p>

WebGLを使ったお絵かきツール。
Java AppletのLascaux SketchをWebGLベースに移植したもの


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mswjs/msw: Seamless REST/GraphQL API mocking library for browser and Node.
[github.com/mswjs/msw](https://github.com/mswjs/msw "mswjs/msw: Seamless REST/GraphQL API mocking library for browser and Node.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

HTTPモックライブラリ。
Service Workerを使う方法、Fetch、XHR、`http`モジュールをinterceptする方法を提供している。
リクエストに対するレスポンスを定義して、ブラウザとNode.jsでそれぞれHTTPリクエストのテストができるライブラリ


----

## JSSpec | jsspec.github.io
[jsspec.github.io/](https://jsspec.github.io/ "JSSpec | jsspec.github.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

RSpecライクなContextを持ったテストフレームワーク。
`subject`というグローバル変数に対してテストのコンテキストを割り当ててテストコードを書けるようになっている。


----
