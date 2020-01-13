---
title: "2020-01-13のJS: Firefox 72、Node.js 13.6.0、TypeScript 3.8 Beta(Private Fields)"
author: "azu"
layout: post
date : 2020-01-13T02:31:20.234Z
category: JSer
tags:
- Firefox
- Node.js
- TypeScript

---

JSer.info #470 - Firefox 72がリリースされました

- [Firefox 72 — our first song of 2020 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/01/firefox-72-our-first-song-of-2020/)
- [Firefox 72 for Developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/72)
- [Firefox 72.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/72.0/releasenotes/)

Firefox 72では開発者ツールの改善が行われ、デバッガーでプロパティにset/getに対するBreak Pointを設定できるようになっています。
また、コンソールでの非同期処理に対するスタックトレースが[Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)で有効化されています。

その他には、ES2020に入る予定の[Nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator)のサポート、CSSのShadow Parts(`::part()`)、CSS Motion Pathの対応なども含まれています。

またFirefox 72からは通知許可の求めるにはユーザーインタラクションのイベント内で行う必要があるように変更されています。
詳細は次の記事で紹介されています。

- [Upcoming notification permission changes in Firefox 72 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/11/upcoming-notification-permission-changes-in-firefox-72/)
- [Restricting Notification Permission Prompts in Firefox - Future Releases](https://blog.mozilla.org/futurereleases/2019/11/04/restricting-notification-permission-prompts-in-firefox/)

少しアプローチは異なりますが、Chrome 80からopt-inでQuiet UIという新しい通知許可のUIが実装されています。

- [Chromium Blog: Introducing quieter permission UI for notifications](https://blog.chromium.org/2020/01/introducing-quieter-permission-ui-for.html)

こちらはまだデフォルトでは入っていませんが、通知許可をより静かにする実験的なUIとなっています。
今後、[Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)に基づいて許可率の低いサイトではデフォルトをQuiet UIにするといった変更を予定しているようです。

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Chrome 80+ Quiet UI(opt-in) for Notifications<a href="https://t.co/YTCp4ny0Hv">https://t.co/YTCp4ny0Hv</a> <a href="https://t.co/HEqsxyWTkh">pic.twitter.com/HEqsxyWTkh</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/1216549874348384257?ref_src=twsrc%5Etfw">January 13, 2020</a></blockquote>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


----

Node.jsの開発版であるv13.6.0がリリースされました。

- [Node v13.6.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v13.6.0/)

正規表現にマッチするかをテストできる`assert.match()`と`assert.doesNotMatch()`が`assert`モジュールに追加されています。
また、`EventEmitter.on`のAsync Iterator対応、Streamに対する`fs`の実装を指定できるオプションの追加、`error`イベントを副作用なしに監視できる`EventEmitter.errorMonitor` Symbolを追加なども行われています。

ブラウザの[User Timing API](https://developer.mozilla.org/docs/Web/API/User_Timing_API)や[PerformanceObserver](https://developer.mozilla.org/docs/Web/API/PerformanceObserver)に相当するAPIを提供する[`perf_hooks`](https://nodejs.org/api/perf_hooks.html)モジュールがStable APIになるといった変更も含まれています。

----

TypeScript 3.8 Betaがリリースされました

- [Announcing TypeScript 3.8 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8-beta/)

Flowにもあった`import type`/`export type`で型定義だけをimport/exportできるようになっています。

- [Module Types | Flow](https://flow.org/en/docs/types/modules/)

新しい構文のサポートとしてES Proposal Stage 3の[ECMAScript Private Fields](https://github.com/tc39/proposal-private-fields)に対応、同じくStage 3の[Top-Level `await`](https://github.com/tc39/proposal-top-level-await)に対応しています。
TypeScriptには元々soft privateとしての`private`修飾子がありましたが、今回実装されたhard privateであるPrivate Fieldsの違いについても解説されています。

その他として`target`と`module`が`es2020`のサポートが追加され、`tsconfig.json`に`watchOptions`オプションが追加されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release throw new Preact('10.2.0') · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.2.0](https://github.com/preactjs/preact/releases/tag/10.2.0 "Release throw new Preact('10.2.0') · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.2.0リリース。
`useErrorBoundary` hookのサポート、`lazy()`がnamed exportsに対応など


----

## Firefox 72 — our first song of 2020 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/01/firefox-72-our-first-song-of-2020/](https://hacks.mozilla.org/2020/01/firefox-72-our-first-song-of-2020/ "Firefox 72 — our first song of 2020 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 72リリース。
フラグ付きでコンソールのAsync Stack Traceの対応、CSSのShadow Parts(`::part()`)、CSS Motion Pathの対応。
通知許可の求めるにはユーザーインタラクションのイベント内で行う必要があるように変更、Nullish coalescing operator、`formdata`イベントの対応など

- [Firefox 72 for Developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/72 "Firefox 72 for Developers - Mozilla | MDN")
- [Firefox 72.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/72.0/releasenotes/ "Firefox 72.0, See All New Features, Updates and Fixes")
- [Firefox 72 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/en-CA/versions/72/ "Firefox 72 Site Compatibility | Firefox Site Compatibility")

----

## Node v12.14.1 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.14.1/](https://nodejs.org/en/blog/release/v12.14.1/ "Node v12.14.1 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.14.1リリース。
`v8.serialize`と`v8.deserialize`がStable APIとなるなど


----

## Node v13.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v13.6.0/](https://nodejs.org/en/blog/release/v13.6.0/ "Node v13.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 13.6.0リリース。
正規表現にマッチするかをテストできる`assert.match()`と`assert.doesNotMatch()`の実装、
`EventEmitter.on`のAsync Iterator対応。
Streamに対する`fs`の実装を指定できるオプションの追加、`error`イベントを副作用なしに監視できる`EventEmitter.errorMonitor` Symbolを追加。
`perf_hooks`モジュールがStable APIになるなど


----

## Release Notes for Safari Technology Preview 98 | WebKit
[webkit.org/blog/9689/release-notes-for-safari-technology-preview-98/](https://webkit.org/blog/9689/release-notes-for-safari-technology-preview-98/ "Release Notes for Safari Technology Preview 98 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 98 リリース。
`OffscreenCanvas.convertToBlob`のサポート、CSSの`clamp()`のサポート。
`beforeunload`や`unload`時の同期XHRが禁止される変更など


----

## Announcing TypeScript 3.8 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-8-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8-beta/ "Announcing TypeScript 3.8 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.8 Betaリリース。
`import type`/`export type`で型定義だけをimport/exportできるように、Stage 3のECMAScript Private Fieldsに対応。
Top-Level `await`に対応、`target`と`module`が`es2020`をサポート、`watchOptions`の追加など


----

## Release v2.9.0 · date-fns/date-fns
[github.com/date-fns/date-fns/releases/tag/v2.9.0](https://github.com/date-fns/date-fns/releases/tag/v2.9.0 "Release v2.9.0 · date-fns/date-fns")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

date-fns 2.9.0リリース。
`eachYearInterval`、`eachMonthInterval`、`isExists`の追加。
オブジェクトでまとめてDateを操作する`add`と`sub`の追加など


----

## 7.8.0 Released: ECMAScript 2020, .mjs configuration files and @babel/cli improvements · Babel
[babeljs.io/blog/2020/01/11/7.8.0](https://babeljs.io/blog/2020/01/11/7.8.0 "7.8.0 Released: ECMAScript 2020, .mjs configuration files and @babel/cli improvements · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7.8.0リリース。
ES2020のサポートをデフォルト化、`babel.config.mjs`など設定ファイルの対応を整理、`--copy-ignored`と`--out-file-extension`のサポートなど。
また 8.0.0に向けた準備などについて書かれている

- [Babel 8 Release Plan · Issue #10746 · babel/babel](https://github.com/babel/babel/issues/10746 "Babel 8 Release Plan · Issue #10746 · babel/babel")

----

## Release Version 16.0.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/16.0.0](https://github.com/jsdom/jsdom/releases/tag/16.0.0 "Release Version 16.0.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

jsdom 16.0.0リリース。
Node.js 10未満のサポート終了、`dom.runVMScript()`の廃止、`prototype`使った`Window`間のプロパティ共有の廃止など。`window.getSelection()`のサポート、Timerのメモリリークを修正など


----

## Release V1 RELEASE! @pika/web is now Snowpack · pikapkg/snowpack
[github.com/pikapkg/snowpack/releases/tag/v1.0.1](https://github.com/pikapkg/snowpack/releases/tag/v1.0.1 "Release V1 RELEASE! @pika/web is now Snowpack · pikapkg/snowpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span></p>

Snowpack 1.0.0リリース。
インストール時にES Modulesとして読み込めるモジュールを配置することで、変更ごとにビルドしないでアプリケーション開発できることを目的にしている。
`@pika/web`からSnowpackにリネーム、`--optimize`でのtree-shakingサポート等。

- [Snowpack](https://www.snowpack.dev/ "Snowpack")

----
<h1 class="site-genre">アーティクル</h1>

----

## Guide to Web Authentication
[webauthn.guide/](https://webauthn.guide/ "Guide to Web Authentication")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAuthentication</span> <span class="jser-tag">article</span></p>

Web Authenticationの基本的な目的や使い方について書かれた記事


----

## Chromium Blog: Introducing quieter permission UI for notifications
[blog.chromium.org/2020/01/introducing-quieter-permission-ui-for.html](https://blog.chromium.org/2020/01/introducing-quieter-permission-ui-for.html "Chromium Blog: Introducing quieter permission UI for notifications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 80で入る通知などのパーミッションデザインの変更について。
Quiet UIと呼ばれる新しい許可UIの追加と設定方法について。
またChrome UX Reportのデータをもとに、通知の受け入れ率が低いサイトは自動的にquieter promptsにする変更などが追加される予定。


----

## Advancing the web framework ecosystem
[web.dev/advancing-framework-ecosystem-cds-2019/](https://web.dev/advancing-framework-ecosystem-cds-2019/ "Advancing the web framework ecosystem")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">google</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

Chromeチームが最近取り組んでいるいウェブフレームワークの最適化ついて。
Angular、Next.js、Nuxt.js、Babelについてのパフォーマンス最適化などの取り組みを紹介している


----

## Raw WebGPU
[alain.xyz/blog/raw-webgpu](https://alain.xyz/blog/raw-webgpu "Raw WebGPU")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">safari</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">WebPlatformAPI</span></p>

WebKitやChromiumに試験的に実装されているWebGPUについてのチュートリアル。Vulkan、DirectX 12、Metalを扱うことを目的としたWeb API、基本的な使い方について解説している

- [WebGPU](https://gpuweb.github.io/gpuweb/ "WebGPU")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## qawolf/qawolf: 🐺Create browser tests 10x faster
[github.com/qawolf/qawolf](https://github.com/qawolf/qawolf "qawolf/qawolf: 🐺Create browser tests 10x faster")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

PupeteerとJestを使ったテストフレームワーク。
操作を記憶してテストケースとSelectorを作成でき、CIに実行結果の動画をアップロードのサポートなどをしている。
Automatic waiting、Keyboard eventsなどをサポートしている

- [QA Wolf](https://docs.qawolf.com/ "QA Wolf")

----

## babel/preset-modules: A Babel preset that targets modern browsers by fixing engine bugs (will be merged into preset-env eventually)
[github.com/babel/preset-modules](https://github.com/babel/preset-modules "babel/preset-modules: A Babel preset that targets modern browsers by fixing engine bugs (will be merged into preset-env eventually)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

@babel/preset-envにマージされる予定の、Modern Browser向けの最適化を目的にしたBabel Preset。
MSEdgeなどのES Modulesをサポートしているが一部構文にバグがあるケースなどにも対応している。


----
