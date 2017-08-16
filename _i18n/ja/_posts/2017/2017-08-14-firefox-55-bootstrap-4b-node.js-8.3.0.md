---
title: "2017-08-14のJS: Firefox 55、BootStrap 4β、Node.js 8.3.0"
author: "azu"
layout: post
date : 2017-08-14T23:21:14.903Z
category: JSer
tags:
- Firefox
- BootStrap
- Node.js

---

JSer.info #344 - [Firefox 55.0](https://www.mozilla.jp/firefox/55.0/releasenotes/ "Firefox 55.0")がリリースされました。

- [Firefox 55 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/55)
- [Firefox 55: first desktop browser to support WebVR ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/08/firefox-55-supports-webvr/)

ECMAScriptにおいてはES2017の`SharedArrayBuffer`、現在Stage 3の[Object rest/spread properties](https://github.com/tc39/proposal-object-rest-spread)のサポートが行われています。
加えて`requestIdleCallback`、[WebVR API](https://developer.mozilla.org/en-US/docs/Web/API/WebVR_API "WebVR API")、[Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API "Intersection Observer API")がサポートされています。

また、既存の挙動の変更としてスクロール位置の値を浮動小数点数として返すように変更、[Selection API](https://developer.mozilla.org/en-US/docs/Web/API/Selection#Behavior_of_Selection_API_in_terms_of_editing_host_focus_changes)の仕様追従、WebRTC APIの仕様追従が行われています。

- [scrollX、scrollY、pageXOffset、pageYOffset が整数の代わりに浮動小数点数を返すようになりました | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2017/scrollx-scrolly-pagexoffset-pageyoffset-now-return-double-instead-of-integer/ "scrollX、scrollY、pageXOffset、pageYOffset が整数の代わりに浮動小数点数を返すようになりました | Firefox サイト互換性情報")

既に[Chrome(11~)](https://developers.google.com/web/updates/2017/03/background_tabs)やFireox(50~)でも行われているバックグラウンドタブにおける`setTimeout`などのスロットルについてですが、[トラッキングスクリプト](https://wiki.mozilla.org/Security/Tracking_protection#Lists)に対してはさらに強い制約がかかるようになりました。

- [Throttling of tracking timeout scripts](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout#Throttling_of_tracking_timeout_scripts "Throttling of tracking timeout scripts")

Geolocation APIと[Storage API](https://developer.mozilla.org/ja/docs/Web/API/Storage_API)(ストレージの容量を確認するAPI)は[Secure Contexts](https://developer.mozilla.org/ja/docs/Web/Security/Secure_Contexts "Secure Contexts")(つまりHTTPS)でのみ有効となりました。
既にChrome(50~)において、Geolocation APIはSecure Contextのみとなっています。

- [Geolocation API Removed from Unsecured Origins in Chrome 50  |  Web  |  Google Developers](https://developers.google.com/web/updates/2016/04/geolocation-on-secure-contexts-only "Geolocation API Removed from Unsecured Origins in Chrome 50  |  Web  |  Google Developers")
- [Deprecating Powerful Features on Insecure Origins - The Chromium Projects](https://www.chromium.org/Home/chromium-security/deprecating-powerful-features-on-insecure-origins "Deprecating Powerful Features on Insecure Origins - The Chromium Projects")

----

[Bootstrap 4 Beta · Bootstrap](http://blog.getbootstrap.com/2017/08/10/bootstrap-4-beta/ "Bootstrap 4 Beta · Bootstrap")が公開されました。[Bootstrap 4 alpha](http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/ "Bootstrap 4 alpha")から2年弱程度経っています。

3.xからの変更点として、LessからSassへ移行、FlexboxとGridシステムの改善、IE8/9のサポート終了、JavaScriptプラグインの書き直しなどが行われています。
詳細な変更点については次のIssueを見るとよさそうです。

- [Beta 1 ship list · Issue #21568 · twbs/bootstrap](https://github.com/twbs/bootstrap/issues/21568 "Beta 1 ship list · Issue #21568 · twbs/bootstrap")

----

Node.js 8.3.0がリリースされました。

- [Node v8.3.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v8.3.0/ "Node v8.3.0 (Current) | Node.js")

このバージョンから[V8 6.0](https://v8project.blogspot.jp/2017/06/v8-release-60.html "V8 6.0")が使われるようになり、新しい最適化コンパイラのTurbofanが有効化されています。
そのため、既存の最適化とは異なる傾向が出るようになっています。

たとえば今までは`try/catch`を含む関数は最適化が行われませんでしたが、Turbofanでは最適化されるようになっています。また、`Function#bind`も今まではArrow Functionでラップした関数に比べて遅いものでしたが、ほぼ同等の速度がでるようになっています。
コードの最適化がどのように変わっているかについては、次の記事でコード例と共に紹介されています。

- [GET READY: A NEW V8 IS COMING, NODE.JS PERFORMANCE IS CHANGING.](https://medium.com/the-node-js-collection/get-ready-a-new-v8-is-coming-node-js-performance-is-changing-46a63d6da4de "GET READY: A NEW V8 IS COMING, NODE.JS PERFORMANCE IS CHANGING.")
- [Get ready: A new V8 is coming, Node.js performance is changing. | nearForm](https://www.nearform.com/blog/node-js-is-getting-a-new-v8-with-turbofan/ "Get ready: A new V8 is coming, Node.js performance is changing. | nearForm")

そのため、[Optimization killers · petkaantonov/bluebird Wiki](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers "Optimization killers · petkaantonov/bluebird Wiki")で紹介されているような「最適化を妨げるコード」はTurboFanが使われているかで大きく変わっています。(Wikiの内容も更新されています)
興味がある人は読んでみるといいと思います。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v3.1.0 · sinonjs/sinon
[github.com/sinonjs/sinon/releases/tag/v3.1.0](https://github.com/sinonjs/sinon/releases/tag/v3.1.0 "Release v3.1.0 · sinonjs/sinon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Sinon.js 3.1.0リリース
sandboxにファクトリメソッドの追加、
`sandbox.stub`のリグレッションの修正など


----

## Release v3.5.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v3.5.0](https://github.com/webpack/webpack/releases/tag/v3.5.0 "Release v3.5.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack v3.5.0リリース。
Dynamic Importに`webpackMode`のオプションを追加、`require.context`にcontext modeの第4引数を追加など

- [Module API - Methods](https://webpack.js.org/api/module-methods/ "Module API - Methods")

----

## Microsoft/napajs: Napa.js: Multi-threaded JavaScript runtime
[github.com/Microsoft/napajs](https://github.com/Microsoft/napajs "Microsoft/napajs: Napa.js: Multi-threaded JavaScript runtime")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span></p>

Node.jsで動くマルチスレッドライブラリ。元々BingでCPU-boundな処理を扱うために作られたもの。
スレッド(Worker)をまとめたZoneがあり、Zoneに対して値を渡してそれぞれのスレッドで処理が行える


----

## Release Notes for Safari Technology Preview Release 37 | WebKit
[webkit.org/blog/7862/release-notes-for-safari-technology-preview-release-37/](https://webkit.org/blog/7862/release-notes-for-safari-technology-preview-release-37/ "Release Notes for Safari Technology Preview Release 37 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 37リリース。
`navigator.sendBeacon`、`document.elementsFromPoint`のサポート。
`Promise#finally`、optional `catch` bindingのサポートなど

- [tc39/proposal-optional-catch-binding: proposal for ECMAScript to allow omission of the catch binding](https://github.com/tc39/proposal-optional-catch-binding "tc39/proposal-optional-catch-binding: proposal for ECMAScript to allow omission of the catch binding")

----

## Node v8.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v8.3.0/](https://nodejs.org/en/blog/release/v8.3.0/ "Node v8.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v8.3.0リリース。
Turbofanが有効化されたV8 6.0へのアップグレード、WHATWG Encodingのサポートなど

- [GET READY: A NEW V8 IS COMING, NODE.JS PERFORMANCE IS CHANGING.](https://medium.com/the-node-js-collection/get-ready-a-new-v8-is-coming-node-js-performance-is-changing-46a63d6da4de "GET READY: A NEW V8 IS COMING, NODE.JS PERFORMANCE IS CHANGING.")

----

## Bootstrap 4 Beta · Bootstrap
[blog.getbootstrap.com/2017/08/10/bootstrap-4-beta/](http://blog.getbootstrap.com/2017/08/10/bootstrap-4-beta/ "Bootstrap 4 Beta · Bootstrap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 4βリリース。
LessからSassへ、FlexboxとGridシステムの改善、IE8/9のサポート終了、JavaScriptプラグインの書き直しなど


----

## Firefox 55 for developers - Mozilla | MDN
[developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/55](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/55 "Firefox 55 for developers - Mozilla | MDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 55リリース。
Object spread/rest operator、SharedArrayBufferに対応。
WebVR、requestIdleCallback、Intersection Observer API対応。
またSelection APIの仕様追従、Geo APIなどがSecure Contextのみで利用可能になるなど

- [Firefox 55.0 リリースノート](https://www.mozilla.jp/firefox/55.0/releasenotes/ "Firefox 55.0 リリースノート")
- [Firefox 55: first desktop browser to support WebVR ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/08/firefox-55-supports-webvr/ "Firefox 55: first desktop browser to support WebVR ★ Mozilla Hacks – the Web developer blog")
- [Dummy](http://example.com/ "Dummy")

----
<h1 class="site-genre">アーティクル</h1>

----

## ZEIT – Next.js 3.0
[zeit.co/blog/next3](https://zeit.co/blog/next3 "ZEIT – Next.js 3.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">library</span></p>

Next.js 3.0リリース。
Static Exportのサポート、Dynamic Importのサポート、HMRの対応改善など


----

## ES Modules in Node Today! – Web Dev @ Microsoft – Medium
[medium.com/web-on-the-edge/es-modules-in-node-today-32cff914e4b](https://medium.com/web-on-the-edge/es-modules-in-node-today-32cff914e4b "ES Modules in Node Today! – Web Dev @ Microsoft – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span></p>

Node.jsで今後サポートが予定されているES modulesを扱えるようにするrequire extension hookライブラリ。
`.mjs`対応やCommonJSとの相互運用性に考慮したオプションなどを持つ

- [standard-things/esm: ES modules in Node today!](https://github.com/standard-things/esm "standard-things/esm: ES modules in Node today!")
- [node-eps/002-es-modules.md at master · nodejs/node-eps](https://github.com/nodejs/node-eps/blob/master/002-es-modules.md "node-eps/002-es-modules.md at master · nodejs/node-eps")

----

## Passing data between Promise callbacks
[2ality.com/2017/08/promise-callback-data-flow.html](http://2ality.com/2017/08/promise-callback-data-flow.html "Passing data between Promise callbacks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span></p>

Promiseチェイン間における値のやり取りのパターンについて


----

## The Modern Javascript Tutorial
[javascript.info/](https://javascript.info/ "The Modern Javascript Tutorial")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">tutorial</span></p>

JavaScript/DOM APIのチュートリアルサイト。
それぞれの項目ごとに解説やサンプル、演習問題がある。


----

## Introduction to Preact — a smaller, faster React alternative
[blog.logrocket.com/introduction-to-preact-a-smaller-faster-react-alternative-ad5532eb6d79](https://blog.logrocket.com/introduction-to-preact-a-smaller-faster-react-alternative-ad5532eb6d79 "Introduction to Preact — a smaller, faster React alternative")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Preactについての記事。
Preactとは何か、Reactとの違いや互換性(preact-compat)について。
またPreactの基本的な使い方、preact-cliを使っての開発についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Javascript Performance by mikesherov
[slides.com/mikesherov/javascript-performance](http://slides.com/mikesherov/javascript-performance "Javascript Performance by mikesherov")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

パフォーマンス最適化についてのスライド。
`O(n^2)`なアルゴリズムを避ける、キャッシュとメモ化、GCを避ける。
不必要なImmutableを避ける、必要ないことはしない、パフォーマンス計測の仕方などについて。
npmやwebpackなど実際のプロジェクトの例などについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Investigating Performance of Object#toString in ES2015
[ponyfoo.com/articles/investigating-performance-object-prototype-to-string-es2015](https://ponyfoo.com/articles/investigating-performance-object-prototype-to-string-es2015 "Investigating Performance of Object#toString in ES2015")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">firefox</span></p>

V8の`Object.prototype.toString()`の最適化について。
ES2015で`Symbol.toStringTag`が追加され、toStringはこの実装を考慮する必要がある。(toString自体はオブジェクトの型判定によく使われている)
オブジェクトが`Symbol.toStringTag`を実装しているかのフラグをMapで持っておき、持ってない場合は余計なlookupを省くようにしたという話。
元々はSpiderMonkeyでデザインされていた方法をportした内容についての解説。

- [1369042 - Optimize the @@toStringTag and @@toPrimitive lookups](https://bugzilla.mozilla.org/show_bug.cgi?id=1369042#c0 "1369042 - Optimize the @@toStringTag and @@toPrimitive lookups")
- [Interesting Symbols - Google ドキュメント](https://docs.google.com/document/d/1q_Y2YM8S055RF1R6qvDe65kOEVO99tdviI1vaDcbnmc/edit# "Interesting Symbols - Google ドキュメント")

----

## zeeshanu/learn-regex: Learn regex the easy way
[github.com/zeeshanu/learn-regex](https://github.com/zeeshanu/learn-regex "zeeshanu/learn-regex: Learn regex the easy way")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">正規表現</span> <span class="jser-tag">tutorial</span></p>

正規表現について簡単にまとめられたドキュメント。
基本的な使い方やメタ文字、フラグなどについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## masakazu-yanai/char-canvas: Draw Tool for Ascii Art.
[github.com/masakazu-yanai/char-canvas](https://github.com/masakazu-yanai/char-canvas "masakazu-yanai/char-canvas: Draw Tool for Ascii Art.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

CanvasライクなAPIでアスキーアートを扱うライブラリ。


----

## darcyclarke/rawkit: 🦊 Immediately Open Chrome DevTools when debugging Node.js apps
[github.com/darcyclarke/rawkit](https://github.com/darcyclarke/rawkit "darcyclarke/rawkit: 🦊 Immediately Open Chrome DevTools when debugging Node.js apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

Chromeの立ち上げと`node --inspect`のデバッガーへの接続を自動的に行うことができるツール


----

## JSON to TypeScript interfaces and runtime type-checkers – quicktype
[ts.quicktype.io/](https://ts.quicktype.io/ "JSON to TypeScript interfaces and runtime type-checkers – quicktype")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">webservice</span></p>

JSONからTypeScript/JSON Schema/Go/C#/Elmなどの型定義/interfaceを生成することができるツール


----

## ream/ream: 🚀 Framework for building universal Vue.js app
[github.com/ream/ream](https://github.com/ream/ream "ream/ream: 🚀 Framework for building universal Vue.js app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

UniversalなVueアプリのフレームワーク。
Next.jsやNuxt.jsのディレクトリ構造などの暗黙的な規約ではなく、明示的な設定/コードによりアプリケーションを作れるようにする目的


----
