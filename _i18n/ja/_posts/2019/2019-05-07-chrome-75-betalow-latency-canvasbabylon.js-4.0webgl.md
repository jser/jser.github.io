---
title: "2019-05-07のJS: Chrome 75 Beta(Low Latency Canvas)、Babylon.js 4.0(WebGL)"
author: "azu"
layout: post
date : 2019-05-07T01:19:40.127Z
category: JSer
tags:
- Chrome
- WebGL
- gulp

---

JSer.info #434 - Chrome 75のベータ版がリリースされました。

- [Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators](https://blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html)
- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D75)

Canvas Contextに低遅延レンダリングのための`desynchronized`オプションを追加されています。
`desynchronized`オプションについては次の記事で解説されています。

- [Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/05/desynchronized) 
- [Add a low latency mode for OffscreenCanvas · Issue #2659 · whatwg/html](https://github.com/whatwg/html/issues/2659)

Web Share APIでファイルをサポート、ES Proposalの[Numeric separators](https://github.com/tc39/proposal-numeric-separator)をサポートしています。
また、CSPの `script-src-attr`, `script-src-elem`, `style-src-attr`, `style-src-elem`ディレクティブのサポートが追加され、
[HTMLVideoElement.playsInline](https://www.chromestatus.com/feature/Discussion%20to%20add%20it%20to%20spec:%20https://github.com/whatwg/html/issues/1237)やCache-Controlの`stale-while-revalidate`のサポートなども含まれています。

`stale-while-revalidate`については次の記事がわかりやすいと思います。

- [What stale-while-revalidate provides is a grace period (defined by us) in which the browser is permitted to use an out of date (stale) asset while we’re checking for a newer version.](https://csswizardry.com/2019/03/cache-control-for-civilians/)

----

WebGLベースの3D games向けフレームワークであるBabylon.js 4.0がリリースされました。

- [Babylon.js 4.0 Is Here! – Babylon.js – Medium](https://medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b)
- [Release 4.0.0 · BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js/releases/tag/v4.0.0)

Visual Scene Inspectorが追加され[inspector](https://doc.babylonjs.com/features/playground_debuglayer)のデバッグ機能が強化されています。
また、不要なモジュールなどをbundle時にeliminateできるようにファイルサイズが改善されています。

- [ES6 - Babylon.js Documentation](https://doc.babylonjs.com/features/es6_support)

またパフォーマンスの改善や物理エンジンとして[ammo.js](https://github.com/kripken/ammo.js/)をサポートなどが行われています。

- [Use a Physics Engine - Babylon.js Documentation](https://doc.babylonjs.com/how_to/using_the_physics_engine)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## jQuery 3.4.1: triggering focus events in IE and finding root elements in iOS 10 | Official jQuery Blog
[blog.jquery.com/2019/05/01/jquery-3-4-1-triggering-focus-events-in-ie-and-finding-root-elements-in-ios-10/](http://blog.jquery.com/2019/05/01/jquery-3-4-1-triggering-focus-events-in-ie-and-finding-root-elements-in-ios-10/ "jQuery 3.4.1: triggering focus events in IE and finding root elements in iOS 10 | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.4.1リリース。
IE10-IE11で`trigger`の問題を修正、iOS 10.0-10.2でのclickの問題を修正、AMDとしてロードしたときの問題を修正など


----

## Release Notes for Safari Technology Preview 81 | WebKit
[webkit.org/blog/8834/release-notes-for-safari-technology-preview-81/](https://webkit.org/blog/8834/release-notes-for-safari-technology-preview-81/ "Release Notes for Safari Technology Preview 81 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 81リリース。
印刷時のスタイルで`@page`によるmarginのサポート、`frame-ancestors` CSPを`X-Frame-Options`ヘッダより優先するように。
`requestAnimationFrame`の実行タイミングの問題を修正など

- [177484 – requestAnimationFrame should execute before the next frame](https://bugs.webkit.org/show_bug.cgi?id=177484 "177484 – requestAnimationFrame should execute before the next frame")

----

## Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators
[blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html](https://blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html "Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 75 Betaリリース。
Canvasに低遅延レンダリングのための`desynchronized`オプションを追加、Web Shareでファイルをサポート、ES ProposalのNumeric separatorsをサポート。
CSPの`script-src-attr`ディレクティブのサポート、Cache-Controlの`stale-while-revalidate`のサポートなど

- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D75 "Chrome Platform Status")
- [Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/05/desynchronized "Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers")

----

## Release 7.0.0 · websockets/ws
[github.com/websockets/ws/releases/tag/7.0.0](https://github.com/websockets/ws/releases/tag/7.0.0 "Release 7.0.0 · websockets/ws")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebSocketクライアント & サーバの`ws` 7.0.0リリース。
Node.js 6のサポート終了、コンストラクタでNode.jsの`url`オブジェクトではなく`URL`オブジェクトを受け取るように変更。
`readyState`が`OPEN`ではないときの`ping`、`pong`の挙動変更など


----

## Release v4.0.0 · facebook/relay
[github.com/facebook/relay/releases/tag/v4.0.0](https://github.com/facebook/relay/releases/tag/v4.0.0 "Release v4.0.0 · facebook/relay")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

GraphQLとReact向けのフレームワークであるRelay 4.0.0リリース。
Containerの引数に`graphql` tagを渡すのではなくオブジェクトを受け付けるように変更、client schema extensionsのフルサポートなど

- [Building the New facebook.com with React, GraphQL and Relay](https://developers.facebook.com/videos/2019/building-the-new-facebookcom-with-react-graphql-and-relay/ "Building the New facebook.com with React, GraphQL and Relay")

----

## Microsoft Edge – All the news from Build 2019 - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/05/06/edge-chromium-build-2019-pwa-ie-mode-devtools/](https://blogs.windows.com/msedgedev/2019/05/06/edge-chromium-build-2019-pwa-ie-mode-devtools/ "Microsoft Edge – All the news from Build 2019 - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">IE</span> <span class="jser-tag">news</span></p>

ChromiumベースのMSEdgeにはサードパーティトラッキングのブロックができるPrivacy Tools、表示しているサイトをIE互換するIE modeが搭載される予定


----

## Babylon.js 4.0 Is Here! – Babylon.js – Medium
[medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b](https://medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b "Babylon.js 4.0 Is Here! – Babylon.js – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebGLベースの3Dゲーム向けフレームワークのBabylon.js 4.0.0リリース。 Visual Scene Inspectorの導入、ファイルサイズやパフォーマンスの改善、物理エンジンとしてAmmo.jsをサポートなど


----

## Hyper Blog
[hyper.is/blog](https://hyper.is/blog "Hyper Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">console</span> <span class="jser-tag">software</span> <span class="jser-tag">ReleaseNote</span></p>

Electron製のターミナルであるHyper 3リリース。 `hterm`から`xterm.js`に変更してWebGL Rendererを使うように、IPCのバッチ処理でパフォーマンス改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## Stub navigator API in end-to-end tests | Better world by better software
[glebbahmutov.com/blog/stub-navigator-api/](https://glebbahmutov.com/blog/stub-navigator-api/ "Stub navigator API in end-to-end tests | Better world by better software")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Cypressを使いBattery status APIのStubをしながらテストをするチュートリアル。
`navigator`をどのようにstubしてテストするかについて


----

## The CSS Handbook: a handy guide to CSS for developers
[medium.freecodecamp.org/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11](https://medium.freecodecamp.org/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11 "The CSS Handbook: a handy guide to CSS for developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSについてのガイド。
基本的なCSSのプロパティの解説からunit、レイアウト、アニメーションなど幅広く書かれている


----

## Revisiting prefers-reduced-motion, the reduced motion media query | CSS-Tricks
[css-tricks.com/revisiting-prefers-reduced-motion-the-reduced-motion-media-query/](https://css-tricks.com/revisiting-prefers-reduced-motion-the-reduced-motion-media-query/ "Revisiting prefers-reduced-motion, the reduced motion media query | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">animation</span> <span class="jser-tag">article</span> <span class="jser-tag">accessibility</span></p>

CSSの`prefers-reduced-motion`の解説と使い方についての記事。
アクセシビリティ、プログレッシブ・エンハンスメントの考え、CSS Variablesと組み合わせた実装について


----

## Optimizing Performance With Resource Hints — Smashing Magazine
[www.smashingmagazine.com/2019/04/optimization-performance-resource-hints/](https://www.smashingmagazine.com/2019/04/optimization-performance-resource-hints/ "Optimizing Performance With Resource Hints — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

Resource Hintsについての記事。
`dns-prefetch`、`preconnect`、`prefetch`、`prerender`をそれぞれどのような場合に利用するかについて。`as`属性についてなど


----

## gulp4再入門 gulpfileの分割とnodeモジュールの利用 - Qiita
[qiita.com/masato\_makino/items/ad11058e1a8a009abbdf](https://qiita.com/masato_makino/items/ad11058e1a8a009abbdf "gulp4再入門 gulpfileの分割とnodeモジュールの利用 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">article</span></p>

gulp4ベースの入門記事。
gulp taskの定義方法、タスクファイルの分割、gulpプラグインとNodeモジュールについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## oclif/cli-ux: CLI IO utilities
[github.com/oclif/cli-ux](https://github.com/oclif/cli-ux "oclif/cli-ux: CLI IO utilities")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

ターミナルのCLIを提供するNode.jsライブラリ。
promptやconfirmなどの対話操作、URLのリンク表示、spinner、アノテーション、table表示など


----

## Laconia · Create well-crafted serverless applications, effortlessly
[laconiajs.io/](https://laconiajs.io/ "Laconia · Create well-crafted serverless applications, effortlessly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Node.jsのserverlsssフレームワーク。Hexagonal Architectureで依存を外から渡せるような構造にしてテストしやすくしている。
Long Task向けのbatch処理を行うモジュールも提供されている。


----

## microsoft/react-native-windows: A framework for building native Windows apps with React.
[github.com/Microsoft/react-native-windows](https://github.com/Microsoft/react-native-windows "microsoft/react-native-windows: A framework for building native Windows apps with React.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">windows</span> <span class="jser-tag">library</span></p>

React Native for Windows。
React NativeでネイティブなWindowsアプリ(UWP)を作成するフレームワーク。


----
