---
title: "2017-09-26のJS: Chrome 62 Beta、Safari 11.0、モダンブラウザのレンダリングパイプライン"
author: "azu"
layout: post
date : 2017-09-26T00:37:50.814Z
category: JSer
tags:
- Chrome
- Safari
- browser

---

JSer.info #350 - Chrome 62betaがリリースされました。

- [Chromium Blog: Chrome 62 Beta: Network Quality Estimator API, OpenType variable fonts, and media capture from DOM elements](https://blog.chromium.org/2017/09/chrome-62-beta-network-quality.html "Chromium Blog: Chrome 62 Beta: Network Quality Estimator API, OpenType variable fonts, and media capture from DOM elements")

Network Quality Estimator API、OpenType Variable Fonts、DOM要素をキャプチャできる`captureStream()`のサポートなどが行われています。

また、62からHTTPのページでのフォーム入力時に"Not secure"と表示されてるようになっています。

- [Chromium Blog: Next steps toward more connection security](https://blog.chromium.org/2017/04/next-steps-toward-more-connection.html "Chromium Blog: Next steps toward more connection security")
- [Chrome62から、http://でのフォームに入力すると警告が出るようになる - ASnoKaze blog](http://asnokaze.hatenablog.com/entry/2017/08/18/122808 "Chrome62から、http://でのフォームに入力すると警告が出るようになる - ASnoKaze blog")

----

Safari 11が正式リリースされました。

- [New WebKit Features in Safari 11 | WebKit](https://webkit.org/blog/7956/new-webkit-features-in-safari-11/)
- [Safari 11.0](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Safari_11_0/Safari_11_0.html)

[WebRTCとMedia Capture](https://webkit.org/blog/7763/a-closer-look-into-webrtc/ "WebRTC and media capture")、[WebAssembly](https://webkit.org/blog/7691/webassembly/ "WebAssembly")、[OpenType Variable Font](https://webkit.org/blog/7051/variable-fonts-on-the-web/ "Variable Font")のサポートが行われています。
また、[Web Cryptography API](https://webkit.org/blog/7790/update-on-web-cryptography/ "Web Cryptography API")の更新や動画などのメディアの自動再生がデフォルトブロックする変更などが含まれています。

- [Auto-Play Policy Changes for macOS | WebKit](https://webkit.org/blog/7734/auto-play-policy-changes-for-macos/ "Auto-Play Policy Changes for macOS | WebKit")

またiPhone Xに関する`viewport-fit=cover`とCSSの`constants()`（`env()`にリネーム予定）とsafe-areaについての解説もかかれているので併せて読むと良さそうです。

- [Designing Websites for iPhone X | WebKit](https://webkit.org/blog/7929/designing-websites-for-iphone-x/ "Designing Websites for iPhone X | WebKit")

----

[Introduction to WebRender – Part 1 – Browsers today – Mozilla Gfx Team Blog](https://mozillagfx.wordpress.com/2017/09/21/introduction-to-webrender-part-1-browsers-today/ "Introduction to WebRender – Part 1 – Browsers today – Mozilla Gfx Team Blog")という記事では、現在のメジャーなモダンブラウザにおけるレンダリングプロセスについて書かれています。

ServoのWebRenderを例に、現在のレンダリングパイプラインについて書かれています。

1. Layout
    1. DOMツリー: DOMパースしてDOMツリーを作る
    2. Frameツリー: 各DOMツリーのレイアウト結果
2. Painting
    1. Display List: Frameツリーごとに描画コマンドへ
    2. Layerツリー: レイヤーに描画
3. Compositor
    1. LayerツリーのCompositing: レイヤー同士を合成


各ブラウザに差異はありますが、描画までのプロセス(Layout -> Painting)と合成のプロセス(Compositing)を分けるという手法は、現在のモダンウェブブラウザでは取り入れられています。

他のブラウザのレンダリングプロセスについても最近発表があったので併せてみるとよいかもしれません。

- Chrome:
  - [Next Gen Rendering Engine (BlinkOn 8) - Google スSlide](https://docs.google.com/presentation/d/11rr_vo7UNS6icihnWZMx45O4y5JiSegZKYLQKA1LAdo/edit?ts=599d038f&pli=1#slide=id.g2627e5dc61_1_27)
  - [LayoutNG - Google Documents](https://docs.google.com/document/d/1uxbDh4uONFQOiGuiumlJBLGgO4KDWB8ZEkp7Rd47fw4/edit#heading=h.guvbepjyp0oj)
- MSEdge: [Building a faster browser: Behind the scenes improvements in Microsoft Edge | Microsoft Edge Web Summit 2017 | Channel 9](https://channel9.msdn.com/Events/WebPlatformSummit/Microsoft-Edge-Web-Summit-2017/ES14 "Building a faster browser: Behind the scenes improvements in Microsoft Edge | Microsoft Edge Web Summit 2017 | Channel 9")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Chromium Blog: Chrome 62 Beta: Network Quality Estimator API, OpenType variable fonts, and media capture from DOM elements
[blog.chromium.org/2017/09/chrome-62-beta-network-quality.html](https://blog.chromium.org/2017/09/chrome-62-beta-network-quality.html "Chromium Blog: Chrome 62 Beta: Network Quality Estimator API, OpenType variable fonts, and media capture from DOM elements")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 62βリリース。
Network Quality Estimator API、OpenType Variable Fontsのサポート。
CSS color parserが`#RRGGBBAA`のような形式もサポート、MSEがFLACをサポートなど


----

## Safari 11.0
[developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Safari\_11\_0/Safari\_11\_0.html](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Safari_11_0/Safari_11_0.html "Safari 11.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">safari</span></p>

Safari 11.0リリース。 WebRTC、WebAssermbly、Media Capture API、WebCrypto APIのアルゴリズム追加、Resource timing APIのサポート。 CSSではVariable fonts、CSS strokeのサポート。 ホームスクリーンアプリでWebKitの機能をサポート、追跡クッキーの防止など

- [New WebKit Features in Safari 11 | WebKit](https://webkit.org/blog/7956/new-webkit-features-in-safari-11/ "New WebKit Features in Safari 11 | WebKit")

----

## Relicensing React, Jest, Flow, and Immutable.js | Engineering Blog | Facebook Code
[code.facebook.com/posts/300798627056246/relicensing-react-jest-flow-and-immutable-js/](https://code.facebook.com/posts/300798627056246/relicensing-react-jest-flow-and-immutable-js/ "Relicensing React, Jest, Flow, and Immutable.js | Engineering Blog | Facebook Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">license</span> <span class="jser-tag">news</span></p>

React、Jest、Flow、Immutable.jsはBSD + PatentライセンスからMITライセンスへ変更される。
技術的要因以外で停滞するのは好ましくないため、エコシステムの基盤となるライブラリ/ツールのライセンス変更を決定した。


----

## Release Dexie v2.0.0 · dfahlander/Dexie.js
[github.com/dfahlander/Dexie.js/releases/tag/v2.0.0](https://github.com/dfahlander/Dexie.js/releases/tag/v2.0.0 "Release Dexie v2.0.0 · dfahlander/Dexie.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

IndexedDBラッパーのDexie v2.0.0リリース。
IndexedDB 2.0のサポート、Safariのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Almin + React/Vue.jsのパフォーマンスプロファイルをタイムライン表示できるように | Web Scratch
[efcl.info/2017/09/20/almin-performance-profile-0.14.0/](http://efcl.info/2017/09/20/almin-performance-profile-0.14.0/ "Almin + React/Vue.jsのパフォーマンスプロファイルをタイムライン表示できるように | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">almin</span> <span class="jser-tag">debug</span> <span class="jser-tag">performance</span></p>

Almin/React/Vueのパフォーマンスオプションについて。
開発者ツールのタイムラインでそれぞれの処理時間を可視化できる。


----

## asm.js: 仕様と実装の今 - Qiita
[qiita.com/mod\_poppo/items/de5c6f2f4604b84b1bc1](http://qiita.com/mod_poppo/items/de5c6f2f4604b84b1bc1 "asm.js: 仕様と実装の今 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">asm.js</span></p>

asm.jsの仕様と各ブラウザ(Firefox、MSEdge、Chrome)の実装の差異について

- [dherman/asm.js: A low-level, extraordinarily optimizable subset of JavaScript.](https://github.com/dherman/asm.js "dherman/asm.js: A low-level, extraordinarily optimizable subset of JavaScript.")

----

## Upcoming TypeScript Changes in Vue 2.5 – The Vue Point – Medium
[medium.com/the-vue-point/upcoming-typescript-changes-in-vue-2-5-e9bd7e2ecf08](https://medium.com/the-vue-point/upcoming-typescript-changes-in-vue-2-5-e9bd7e2ecf08 "Upcoming TypeScript Changes in Vue 2.5 – The Vue Point – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Vue</span></p>

Vue 2.5でTypeScriptの型定義周りが改善されることについて。
また、Vueのlanuguage-serverも併せて更新されているため、JavaScriptを使った場合もエディタでの補完などが改善される。

- [vetur/server at master · vuejs/vetur](https://github.com/vuejs/vetur/tree/master/server "vetur/server at master · vuejs/vetur")

----

## To type or not to type: quantifying detectable bugs in JavaScript | the morning paper
[blog.acolyer.org/2017/09/19/to-type-or-not-to-type-quantifying-detectable-bugs-in-javascript/](https://blog.acolyer.org/2017/09/19/to-type-or-not-to-type-quantifying-detectable-bugs-in-javascript/ "To type or not to type: quantifying detectable bugs in JavaScript | the morning paper")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">論文</span> <span class="jser-tag">article</span></p>

JavaScriptに型注釈を加えることでどの程度バグを検出できるかという論文の紹介記事。
GitHubで実際の修正コミットを元に、TSとFlowで型付けし、修正されたバグが検出できるかをテストした。
型注釈をつけることで大体15%のバグは発見できた。

- [Type or Not to Type:Quantifying Detectable Bugs in JavaScript](http://ttendency.cs.ucl.ac.uk/projects/type_study/documents/type_study.pdf "Type or Not to Type:Quantifying Detectable Bugs in JavaScript")

----

## Lifecycle Simulators
[reactarmory.com/guides/lifecycle-simulators](https://reactarmory.com/guides/lifecycle-simulators "Lifecycle Simulators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

Reactコンポーネントのライフサイクルをシミュレートできるツール。
初期化、Stateの更新、Propsの更新をそれぞれ試すことができる


----

## Introduction to WebRender – Part 1 – Browsers today – Mozilla Gfx Team Blog
[mozillagfx.wordpress.com/2017/09/21/introduction-to-webrender-part-1-browsers-today/](https://mozillagfx.wordpress.com/2017/09/21/introduction-to-webrender-part-1-browsers-today/ "Introduction to WebRender – Part 1 – Browsers today – Mozilla Gfx Team Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">firefox</span> <span class="jser-tag">servo</span> <span class="jser-tag">article</span></p>

ServoのWebRenderを例にしてメジャーブラウザのレンダリングの仕組みについて解説している。
`frame tree`と呼ばれる各要素ツリーのレイアウト結果から、`display list`と呼ばれるフラットな描画コマンドを作成する。その描画結果を`layer`に乗せ、最後に`layer`を`compositing`で合成する。
各ブラウザに差異はあるが描画と合成を分けるという手法は、現在のウェブブラウザでは取り入れられている。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Debugging in 2017 with Node.js - YouTube
[www.youtube.com/watch?v&#x3D;Xb\_0awoShR8](https://www.youtube.com/watch?v=Xb_0awoShR8 "Debugging in 2017 with Node.js - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">video</span></p>

Node.jsなアプリをChromeの開発者ツールでデバッグする方法についての発表。
`process._debugProcess(pid)`での既存プロセスのデバッグ、開発者ツールをコードから扱う方法、`chrome://tracing`との連携などについて


----

## Microsoft Edge Web Summit 2017 | Channel 9
[channel9.msdn.com/Events/WebPlatformSummit/Microsoft-Edge-Web-Summit-2017](https://channel9.msdn.com/Events/WebPlatformSummit/Microsoft-Edge-Web-Summit-2017 "Microsoft Edge Web Summit 2017 | Channel 9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

MSEdge Web Summit 2017の動画一覧


----

## HTML5 Conference 2017 - YouTube
[www.youtube.com/user/html5j](https://www.youtube.com/user/html5j "HTML5 Conference 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">イベント</span></p>

HTML5 Conference 2017の動画一覧

- [HTML5 Conference](http://events.html5j.org/conference/2017/9/ "HTML5 Conference")

----

## React v16 and beyond React Fiber // Speaker Deck
[speakerdeck.com/koba04/react-v16-and-beyond-react-fiber](https://speakerdeck.com/koba04/react-v16-and-beyond-react-fiber "React v16 and beyond React Fiber // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">slide</span></p>

React 16の変更点と16以降に導入されるReact Fiberの仕組みについてのスライド


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## cure53/browser-sec-whitepaper
[github.com/cure53/browser-sec-whitepaper/](https://github.com/cure53/browser-sec-whitepaper/ "cure53/browser-sec-whitepaper")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PDF</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span></p>

ブラウザセキュリティに関する文章。 各ブラウザ/色々なケースでの攻撃方法や脆弱性について書かれている


----

## mbeaudru/modern-js-cheatsheet: Cheatsheet for the JavaScript knowledge you will frequently encounter in modern projects.
[github.com/mbeaudru/modern-js-cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet "mbeaudru/modern-js-cheatsheet: Cheatsheet for the JavaScript knowledge you will frequently encounter in modern projects.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">チートシート</span></p>

ES2015の構文などを中心に紹介するチートシート


----

## Performance metrics. What’s this all about? – codeburst
[codeburst.io/performance-metrics-whats-this-all-about-1128461ad6b](https://codeburst.io/performance-metrics-whats-this-all-about-1128461ad6b "Performance metrics. What’s this all about? – codeburst")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

ウェブブラウザのパフォーマンスのメトリクスについての解説。
またそれらを計測できるツールについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Vue.js 2 Material Component Framework | Vuetify.js
[vuetifyjs.com/](https://vuetifyjs.com/ "Vue.js 2 Material Component Framework | Vuetify.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Vueを使ったMaterialデザインのUIフレームワーク


----

## uber/luma.gl: A JavaScript WebGL Framework for Data Visualization
[github.com/uber/luma.gl](https://github.com/uber/luma.gl "uber/luma.gl: A JavaScript WebGL Framework for Data Visualization")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">JavaScript</span></p>

WebGLを使ったデータビジュアライゼーションフレームワーク。
WebGL2にも対応していて、過度な抽象化を避けたAPIを提供する目的


----
<h1 class="site-genre">書籍関係</h1>

----

## Building Progressive Web Apps: Bringing the Power of Native to the Browser: Tal Ater: 9781491961650: Amazon.com: Books
[www.amazon.com/Building-Progressive-Web-Apps-Bringing/dp/1491961651](https://www.amazon.com/Building-Progressive-Web-Apps-Bringing/dp/1491961651 "Building Progressive Web Apps: Bringing the Power of Native to the Browser: Tal Ater: 9781491961650: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

PWAについての書籍


----

## mjavascript/practical-modern-javascript: 🏊 Dive into ES6 and the future of JavaScript
[github.com/mjavascript/practical-modern-javascript](https://github.com/mjavascript/practical-modern-javascript "mjavascript/practical-modern-javascript: 🏊 Dive into ES6 and the future of JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

ES2015以降のJavaScriptについて書かれた電子書籍。CC by-nc-saで公開されている。


----
