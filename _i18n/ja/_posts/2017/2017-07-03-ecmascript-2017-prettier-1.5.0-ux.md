---
title: "2017-07-03のJS: ECMAScript 2017、Prettier 1.5.0、UXのパフォーマンスメトリクス"
author: "azu"
layout: post
date : 2017-07-03T05:14:08.123Z
category: JSer
tags:
- ECMAScript
- Prettier
- performance
- browser

---

JSer.info #338 - ECMAScript 2017が正式リリースされました。

> ECMA-262 8th edition - ECMAScript® 2017 Language Specification
> -- [Ecma latest news](http://ecma-international.org/news/index.html "Ecma latest news")

- [Standard ECMA-262](http://ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")

ES2017ではasync/await、shared memory and atomic、`Object.entires`/`Object.values`、`String#padStart`/`String#padEnd`、`Object.getOwnPropertyDescriptors()`や関数内での末尾カンマの許容などが追加されています。

詳細は次のサイトを見るといいかもしれません。

- [III ECMAScript 2017](http://exploringjs.com/es2016-es2017/pt_es2017.html "III ECMAScript 2017")

今後(ES2018~)で策定していくProposalについては次のページにまとめられています。

- [tc39/proposals: Tracking ECMAScript Proposals](https://github.com/tc39/proposals "tc39/proposals: Tracking ECMAScript Proposals")
- [babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals](https://github.com/babel/proposals "babel/proposals: (WIP) Tracking the status of Babel&#39;s implementation of TC39 proposals")
  - Babelの対応

----

整形ツールのPrettier 1.5.0がリリースされました。

- [Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier](https://github.com/prettier/prettier/releases/tag/1.5.0 "Release 1.5.0: GraphQL, CSS-in-JS &amp; JSON · prettier/prettier")

GraphQL、CSS in JS、JSONの対応、CSSやTypeScript、JSX周りバグ修正などが行われています。


----

[Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics)という記事では、ユーザー体験への影響を見るパフォーマンスのメトリクスについて書かれています。

単純に`DOMContentLoaded`や`load`の時間を見るだけでは体験を計測できないという問題があります。
そのため、First Paint/First Meaningful Paing/Time to Interactive(TTI)/Longtasksなどの指標やその意味についてかかれています。

記事の元は、Google I/Oでの発表となっているので併せて動画の方も見るといいかもしれません。

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Ljq-Jn-EgU?ecver=1" frameborder="0" allowfullscreen></iframe>


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier
[github.com/prettier/prettier/releases/tag/1.5.0](https://github.com/prettier/prettier/releases/tag/1.5.0 "Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

prettier 1.5.0リリース。
GraphQL、CSS in JS、JSONの対応、CSSやTypeScript、JSX周りバグ修正など

- [Adding a new layout strategy to Prettier – Geckoboard: Under-the-Hood – Medium](https://medium.com/geckoboard-under-the-hood/adding-a-new-layout-strategy-to-prettier-8d33084c0f99 "Adding a new layout strategy to Prettier – Geckoboard: Under-the-Hood – Medium")

----

## Release v7.0.0-beta.16 · babel/babylon
[github.com/babel/babylon/releases/tag/v7.0.0-beta.16](https://github.com/babel/babylon/releases/tag/v7.0.0-beta.16 "Release v7.0.0-beta.16 · babel/babylon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">AST</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Babylon 7.0.0 beta16リリース。
TypeScriptパーサの追加、BigInt(Stage 2)のサポートなど

- [TypeScript parser by andy-ms · Pull Request #523 · babel/babylon](https://github.com/babel/babylon/pull/523 "TypeScript parser by andy-ms · Pull Request #523 · babel/babylon")

----

## Ecma latest news
[ecma-international.org/news/index.html](http://ecma-international.org/news/index.html "Ecma latest news")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

"ECMA-262 8th edition - ECMAScript® 2017 Language Specification" ES2017がGAで承認されて正式リリースされた。

- [Standard ECMA-262](http://ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")

----

## Release Notes for Safari Technology Preview 34 | WebKit
[webkit.org/blog/7760/release-notes-for-safari-technology-preview-34/](https://webkit.org/blog/7760/release-notes-for-safari-technology-preview-34/ "Release Notes for Safari Technology Preview 34 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 34リリース。
`RTCRtpTransceiver#addTransceiver`をサポートしトラック単位での片方向通信を使えるように、W3C Secure Contextsの実装、SRIを試験的にサポートなど

- [Safari TP 34では新しい片方向WebRTCの手順が使えるようになったので、試してみた - Qiita](http://qiita.com/tomoyukilabs/items/59267f25c9dbd43d5ecb "Safari TP 34では新しい片方向WebRTCの手順が使えるようになったので、試してみた - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/user-centric-performance-metrics](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics "Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

ユーザー体験への影響を見るパフォーマンスのメトリクスについて。
ロード時間だけでは体験を計測できないため。
そのため、First Paint/First Meaningful Paing/Time to Interactive/Longtasksを指標にそれぞれ何を意味するかや計測方法について

- [You Need to know SSR // Speaker Deck](https://speakerdeck.com/yosuke_furukawa/you-need-to-know-ssr "You Need to know SSR // Speaker Deck")

----

## Chrome 60 DevTools の新機能/変更点 - Qiita
[qiita.com/kyoshidajp/items/e3f9be02a7ccd00aa7d7](http://qiita.com/kyoshidajp/items/e3f9be02a7ccd00aa7d7 "Chrome 60 DevTools の新機能/変更点 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome 60の開発者ツールの変更点について


----

## NYTimes/kyt: Starting a new JS app? Build, test and run advanced apps with kyt 🔥
[github.com/nytimes/kyt](https://github.com/nytimes/kyt "NYTimes/kyt: Starting a new JS app? Build, test and run advanced apps with kyt 🔥")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptアプリのツールキット。
Babel/webpack/Jest/Stylelint/ESlint/protoなどのセットアップをまとめて行うツール


----

## Supercharged Live Stream Blog: Code Splitting  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/supercharged-codesplit](https://developers.google.com/web/updates/2017/06/supercharged-codesplit "Supercharged Live Stream Blog: Code Splitting  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span> <span class="jser-tag">plugin</span> <span class="jser-tag">video</span></p>

Code Splittingを行うBabelプラグインを作成するスクリーンキャスト


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Building m.uber: Engineering a High-Performance Web App for the Global Market - Uber Engineering Blog
[eng.uber.com/m-uber/](https://eng.uber.com/m-uber/ "Building m.uber: Engineering a High-Performance Web App for the Global Market - Uber Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">mobile</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

Uberのモバイル向けの最適化について。
Reactを使っているが、mobileではPreactに置き換えて利用している。
また、サーバサイドレンダリングや、初期bundleサイズを小さくするためのcode split、依存が小さなJustの利用、SWやIndexedDBを使ったキャッシュなどについて。
問題を見つけるためのエラーハンドリングについて。

- [angus-c/just: A library of dependency-free utilities that do just do one thing.](https://github.com/angus-c/just "angus-c/just: A library of dependency-free utilities that do just do one thing.")

----

## GraphQL Network Communication Framework
[graphql-io.com/](http://graphql-io.com/ "GraphQL Network Communication Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

クライアント <-> サーバのコミュニケーションを行うGraphQLフレームワーク。
Apollo/WebSocketベース


----

## HTML Standard
[html.spec.whatwg.org/dev/](https://html.spec.whatwg.org/dev/ "HTML Standard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span></p>

WHATWG HTML仕様のDeveloper's Edition。
ブラウザベンダー向けの情報は削除し、ウェブ開発者向けの情報に絞ったHTML仕様。

- [HTML Standard 日本語訳](https://momdo.github.io/html/dev/ "HTML Standard 日本語訳")
- [Review on utilization of \`w-nodev\` annotation · Issue #1488 · whatwg/html](https://github.com/whatwg/html/issues/1488#issuecomment-310450737 "Review on utilization of \&#x60;w-nodev\&#x60; annotation · Issue #1488 · whatwg/html")
- [WHATWG HTML Standard Developer Editionの話 - 水底の血](http://momdo.hatenablog.jp/entry/20170702/1498999477 "WHATWG HTML Standard Developer Editionの話 - 水底の血")
- [HTML5 for Web Developers | HTML5 Doctor](http://html5doctor.com/html5-for-web-developers/ "HTML5 for Web Developers | HTML5 Doctor")

----

## babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals
[github.com/babel/proposals](https://github.com/babel/proposals "babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

ECMAScript proposalとBabelの実装の対応をまとめたもの


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## roman01la/js-memory-usage: Data Structures Memory Usage in JavaScript
[github.com/roman01la/js-memory-usage](https://github.com/roman01la/js-memory-usage "roman01la/js-memory-usage: Data Structures Memory Usage in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">performance</span></p>

JavaScriptのデータ構造別/ライブラリごとのメモリ消費量をまとめたもの。List/Array/Map/SetをJavaScript/ImmutableJS/ClojureScript/GopherJS/Reasonなど色々な実装ごと比較


----

## pinterest/esprint: Fast eslint runner
[github.com/pinterest/esprint](https://github.com/pinterest/esprint "pinterest/esprint: Fast eslint runner")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

ESLintをparallelで実行できるツール


----

## anvilresearch/webcrypto: W3C Web Cryptography API for Node.js
[github.com/anvilresearch/webcrypto](https://github.com/anvilresearch/webcrypto "anvilresearch/webcrypto: W3C Web Cryptography API for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

Node.jsでWeb Cryptography APIに対応するpolyfill(ponyfill)ライブラリ


----

## coast-team/netflux: JavaScript client and server side transport API based on WebRTC & WebSocket
[github.com/coast-team/netflux](https://github.com/coast-team/netflux "coast-team/netflux: JavaScript client and server side transport API based on WebRTC & WebSocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">browser</span></p>

WebRTC、WebSocketを使ったP2Pライブラリ。
ブラウザ、Node.jsでデータのやり取りを行える


----

## OnetapInc/chromy: Chromy is a library for operating headless chrome. 🍺🍺🍺
[github.com/OnetapInc/chromy](https://github.com/OnetapInc/chromy "OnetapInc/chromy: Chromy is a library for operating headless chrome. 🍺🍺🍺")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Headless ChromeをNightmare.jsのように操作するAPIを提供するライブラリ。
Chrome DevTools Protocolを使って処理をやり取りしている。


----

## dollarshaveclub/study: A Simple, progressive, client/server AB testing library ⚡️
[github.com/dollarshaveclub/study](https://github.com/dollarshaveclub/study "dollarshaveclub/study: A Simple, progressive, client/server AB testing library ⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

A/Bテストティングライブラリ。
universalで動き、storage driverでデータの保存先を指定できる。


----

## egoist/dom-dom: JSX to actual DOM.
[github.com/egoist/dom-dom](https://github.com/egoist/dom-dom "egoist/dom-dom: JSX to actual DOM.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jsx</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

JSXを`document` APIを使ってDOMオブジェクトにするライブラリ


----

## yahoo/mendel: Build toolchain for experimentation on isomorphic web applications with tree-inheritance and multivariate support.
[github.com/yahoo/mendel](https://github.com/yahoo/mendel "yahoo/mendel: Build toolchain for experimentation on isomorphic web applications with tree-inheritance and multivariate support.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">設計</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

コードのフラグではなくルールファイルベースでプロジェクト構造を管理できるツール。
試験的な機能を取り入れたA/Bテストを管理しやすくするためのフレームワーク。
フラグ管理は技術的負債となりやすく、持続可能性をYahooで調査した結果作成されたデザイン。

- [mendel/Design.md at master · yahoo/mendel](https://github.com/yahoo/mendel/blob/master/docs/Design.md "mendel/Design.md at master · yahoo/mendel")

----

## jaredpalmer/formik: Forms in React, without tears
[github.com/jaredpalmer/formik](https://github.com/jaredpalmer/formik "jaredpalmer/formik: Forms in React, without tears")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React向けのフォームライブラリ


----
