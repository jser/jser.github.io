---
title: "2018-04-10のJS: PWA on iOS & Windows Store、dom-testing-library"
author: "azu"
layout: post
date : 2018-04-10T01:35:23.636Z
category: JSer
tags:
- PWA
- iOS
- windows
- dom
- tests

---

JSer.info #378 - [Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7)という記事では、iOS 11.3/Safari 11.1でサポートされたService Workerなどいわゆる[Progressive Web Apps ](https://developers.google.com/web/progressive-web-apps/)(PWA)の対応について書かれています。

ホームスクリーンアプリとしての動作や[Safari Technology Preview](https://developer.apple.com/safari/technology-preview/)を使ったService Workerのデバッグ方法について紹介しています。加えて、iOSのネイティブアプリと違いやAndroid/ChromeのPWAとの違いなどについても書かれています。

また[First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Central](https://www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here)という記事では、Windows 10 Spring Creators Update(Windows 10 build 1803)のプレビュー版のWindows StoreにPWAなアプリケーションが掲載されるようになったことが書かれています。

Windows StoreでのPWAについては次の記事で解説されています。

- [Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/#0eVsoxrHYlso6vcS.97)

----

[kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.](https://github.com/kentcdodds/dom-testing-library)というDOM要素をテストするためのライブラリが公開されています。
テストの際によく利用するテキストを含む要素を選択する`getByText`関数や`data-testid`属性を元に要素を選択する`getByTestId`関数などを提供するライブラリとなっています。

著名なViewライブラリ向けのバインディングも用意されていて[react-testing-library
](https://github.com/kentcdodds/react-testing-library)、[vue-testing-library
](https://github.com/dfcook/vue-testing-library)などがあります。

詳しくは作者により次の記事で解説されています。

- [Introducing the react-testing-library 🐐 – kentcdodds](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Axe 3.0 has arrived — here’s what you need to know - Deque
[www.deque.com/blog/axe-3-0-has-arrived/](https://www.deque.com/blog/axe-3-0-has-arrived/ "Axe 3.0 has arrived — here’s what you need to know - Deque")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">ReleaseNote</span></p>

Axe 3.0リリース。
Shadow DOMのサポートなど

- [Release 3.0.0 · dequelabs/axe-core](https://github.com/dequelabs/axe-core/releases/tag/v3.0.0 "Release 3.0.0 · dequelabs/axe-core")

----

## First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Central
[www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here](https://www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here "First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Central")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">PWA</span> <span class="jser-tag">news</span></p>

Microsoft StoreにPWAアプリが公開されるようになった


----

## sails/CHANGELOG.md at v1.0.0 · balderdashy/sails
[github.com/balderdashy/sails/blob/v1.0.0/CHANGELOG.md](https://github.com/balderdashy/sails/blob/v1.0.0/CHANGELOG.md "sails/CHANGELOG.md at v1.0.0 · balderdashy/sails")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのウェブアプリケーションフレームワークであるSails.js 1.0リリース。


----
<h1 class="site-genre">アーティクル</h1>

----

## React v16.3 changes - blog.koba04.com
[blog.koba04.com/post/2018/04/04/react-v163-changes/](http://blog.koba04.com/post/2018/04/04/react-v163-changes/ "React v16.3 changes - blog.koba04.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16.3の変更点について


----

## Lazy Loading Images and Video  |  Web Fundamentals  |  Google Developers
[developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/ "Lazy Loading Images and Video  |  Web Fundamentals  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

画像や動画の遅延ロードについて。
画像の遅延ロードとしてIntersection Observerを使った方法、CSSを使った方法について。
動画とGIFのロード、遅延ロードを補助するライブラリ、ロードに失敗した時のFallbackなどについて


----

## Headless Chrome: an answer to server-side rendering JS sites  |  Tools for Web Developers  |  Google Developers
[developers.google.com/web/tools/puppeteer/articles/ssr](https://developers.google.com/web/tools/puppeteer/articles/ssr "Headless Chrome: an answer to server-side rendering JS sites  |  Tools for Web Developers  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">server</span> <span class="jser-tag">article</span></p>

Headless Chromeを使ったサーバーサイドレンダリングについてのチュートリアル。
どのように実装するか、最適化について


----

## GoDaddy Open Source Center - Isomorphic Asset System for React and React-Native
[godaddy.github.io/2018/04/04/isomorphic-asset-system-for-react-and-react-native/](https://godaddy.github.io/2018/04/04/isomorphic-asset-system-for-react-and-react-native/ "GoDaddy Open Source Center - Isomorphic Asset System for React and React-Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

SVGのアセットを管理するツール、React/React Nativeコンポーネント、webpack loaderなどについて


----

## Strategies for Service Worker Caching for Progressive Web Apps
[blog.hasura.io/strategies-for-service-worker-caching-d66f3c828433](https://blog.hasura.io/strategies-for-service-worker-caching-d66f3c828433 "Strategies for Service Worker Caching for Progressive Web Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Service Workerのキャッシュの仕組みとキャッシュの問題があるケースについて。
壊れたデプロイを行った時の問題、`service-worker.js`ファイル自体をキャッシュした時の問題、キャッシュすべきでないレスポンスなどについて。
また`create-react-app`の事例や`Clear-Site-Data`ヘッダについて


----

## Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium
[medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7 "Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">PWA</span></p>

iOS 11.3でサポートされたService WorkerなどのPWAに関する機能について。
ネイティブアプリと比較した場合の制限やChrome/Androidとの違いなどについて


----

## Transform your codebase using codemods | nec.is
[nec.is/writing/transform-your-codebase-using-codemods/](https://nec.is/writing/transform-your-codebase-using-codemods/ "Transform your codebase using codemods | nec.is")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">AST</span></p>

jscodeshiftを使ったJavaScriptのコード変換についての記事。
どのようにJavaScriptのコードを扱うのか、ASTについて、jscodeshiftのAPIについて紹介している


----

## Introducing the Payment Request API for Apple Pay | WebKit
[webkit.org/blog/8182/introducing-the-payment-request-api-for-apple-pay/](https://webkit.org/blog/8182/introducing-the-payment-request-api-for-apple-pay/ "Introducing the Payment Request API for Apple Pay | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 11.1のPayment Request APIでApple Payを利用する方法についての解説記事。
`-webkit-appearance: -apple-pay-button;"`のスタイルを指定するだけでAppley Payボタンを表示できる。
またPayment Request APIの使い方について。


----

## Understanding JavaScript Proxies by Examining on-change Library
[codeburst.io/understanding-javascript-proxies-by-examining-on-change-library-f252eddf76c2](https://codeburst.io/understanding-javascript-proxies-by-examining-on-change-library-f252eddf76c2 "Understanding JavaScript Proxies by Examining on-change Library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">proxy</span> <span class="jser-tag">article</span></p>

プロパティの変更検知をES Proxyで実装しながら、Proxyについて紹介している記事


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Browser Automated Tests // Speaker Deck
[speakerdeck.com/derekb/browser-automated-tests](https://speakerdeck.com/derekb/browser-automated-tests "Browser Automated Tests // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">slide</span></p>

puppeteerとmochaを使った自動テストについてのスライド。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## React lifecycle methods diagram
[projects.wojtekmaj.pl/react-lifecycle-methods-diagram/](http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/ "React lifecycle methods diagram")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span></p>

React 16.3以降を含むReactのライフサイクルの図


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.
[github.com/kentcdodds/dom-testing-library](https://github.com/kentcdodds/dom-testing-library "kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

DOM要素をテストするMatcherライブラリ

- [Introducing the react-testing-library 🐐 – kentcdodds](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65 "Introducing the react-testing-library 🐐 – kentcdodds")

----

## kwolfy/webworker-promise: Promise based wrapper for webworkers
[github.com/kwolfy/webworker-promise](https://github.com/kwolfy/webworker-promise "kwolfy/webworker-promise: Promise based wrapper for webworkers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span></p>

WebWorkerを扱うライブラリ。
EventEmitterライクなイベントの仕組みとPromiseを使った非同期処理、Worker poolの仕組みなどを持っている


----

## avwo/whistle: HTTP, HTTPS, WebSocket debugging proxy
[github.com/avwo/whistle](https://github.com/avwo/whistle "avwo/whistle: HTTP, HTTPS, WebSocket debugging proxy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">proxy</span> <span class="jser-tag">debug</span> <span class="jser-tag">node.js</span></p>

Node.jsで書かれたHTTP/HTTPS/WebSocketsのデバッグProxy


----
