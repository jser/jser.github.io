---
title: "2019-03-18のJS: TypeScript 3.4 RC(readonly)、Node.js 11.12.0(`--frozen-intrinsic`)と実験的機能まとめ"
author: "azu"
layout: post
date : 2019-03-18T23:34:25.280Z
category: JSer
tags:
- TypeScript
- Node.js

---

JSer.info #427 - TypeScript 3.4 RCがリリースされました。

- [TypeScript | Announcing TypeScript 3.4 RC](https://devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/)
- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#34-march-2019 "Roadmap · Microsoft/TypeScript Wiki")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-34 "Breaking Changes · Microsoft/TypeScript Wiki")
- [TypeScript v3.4.0-rc 変更点 - Qiita](https://qiita.com/vvakame/items/7f4a55fe15fc9bbe1a63 "TypeScript v3.4.0-rc 変更点 - Qiita")

CLIでは、ビルドの情報をファイルに保存して、次回起動時にその情報を元にビルドできる`--incremental`フラグの追加されています。
`--watch`とは異なり、プロセスの起動終了をまたいだ継続的なビルドを行えます。

型周りでは、`readonly`修飾子を配列とtupleに対して適応できるようになっています。
`const` assertionの追加され、リテラルに対しても`readyonly`の適応や`"文字列"`が`string`という型に勝手に広がるの防止する構文が追加されています。

その他にも、高階関数の型推論改善や`globalThis`(Stage 3)の型定義の追加が行われています。

----

Node.js 11.12.0がリリースされました。

- [Node v11.12.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v11.12.0/)

Node.js 11.12.0では`--frozen-intrinsics`という実験的フラグが追加されています。
詳細は実装されたPRなどに書かれていますが、`--frozen-intrinsics`は`Array`などのJavaScriptのビルトインオブジェクトのデフォルトでdeep freezeする実験的フラグです。
このフラグを有効するといわゆるmonkey patchができない状態になるので、暗黙的にビルトインオブジェクトが拡張されていないという前提でコードを調査できるというセキュリティ的な利点があります。

- [Frozen intrinsics experimental flag by guybedford · Pull Request #25685 · nodejs/node](https://github.com/nodejs/node/pull/25685 "Frozen intrinsics experimental flag by guybedford · Pull Request #25685 · nodejs/node")
- [A Node.js Security Model](https://docs.google.com/document/d/1h__FmXsEWRuNrzAV_l3Iw9i_z8fCXSokGfBiW8-nDNg/edit?ts=5c1adaed#heading=h.xh66r8quma5i)

関連する話として、Secure EcmaScript(SES)やNode.js 11.8.0で実験的に実装されたPolicy機能について調べると面白いかもしれません。

- [Agoric/SES: Secure EcmaScript](https://github.com/Agoric/SES "Agoric/SES: Secure EcmaScript")
- [2019-01-29のJS: Node.js 11.8.0(Policy機能)、Nuxt.js 2.4.0(TSサポート)、Yarn v2のロードマップ](https://jser.info/2019/01/29/node.js-11.8.0policynuxt.js-2.4.0tsyarn-v2/)

----

[Update on Experimental Features in Node.js - NodeSource](https://nodesource.com/blog/experimental-features-in-node.js)という記事では、現在実装されているNode.jsの実験的な機能について紹介されています。

先程紹介したPolicy機能やWorker Threads、Performance Hooks、Diagnostic Report、ECMAScript Modulesについて書かれています。

Performance HooksはブラウザのPerformance Timing APIとも互換性が意識して作られている話やECMAScript Modulesは`.mjs`の話などが書かれています。
興味がある人は試してみるといいかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Chrome 73  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/03/nic73](https://developers.google.com/web/updates/2019/03/nic73 "New in Chrome 73  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 73リリース。
デスクトップ版でもPWAインストールの対応、Signed HTTP Exchanges、Constructable style sheetsのサポート、`String#matchAll`のサポート。
`wheel`がデフォルトでPassiveに変更など

- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D73 "Chrome Platform Status")

----

## TypeScript | Announcing TypeScript 3.4 RC
[devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/ "TypeScript | Announcing TypeScript 3.4 RC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.4 RCリリース。
ビルドの情報をファイルに保存して、次回の起動時にその情報で続けてビルドできる`--incremental`フラグの追加。
`readonly`修飾子を配列とtupleに対して適応できるように、`const` assertionの追加、高階関数の型推論改善など

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#34-march-2019 "Roadmap · Microsoft/TypeScript Wiki")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-34 "Breaking Changes · Microsoft/TypeScript Wiki")
- [TypeScript v3.4.0-rc 変更点 - Qiita](https://qiita.com/vvakame/items/7f4a55fe15fc9bbe1a63 "TypeScript v3.4.0-rc 変更点 - Qiita")

----

## Node v11.12.0 (Current) | Node.js
[nodejs.org/en/blog/release/v11.12.0/](https://nodejs.org/en/blog/release/v11.12.0/ "Node v11.12.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 11.12.0リリース。
`Array`などのビルトインオブジェクトをデフォルトでfreezeする`--frozen-intrinsics`フラグを実験的に追加など


----

## CKEditor 5 v12.0.0 with inline widgets and distraction free editor released
[ckeditor.com/blog/CKEditor-5-v12.0.0-with-inline-widgets-and-distraction-free-editor-released/](https://ckeditor.com/blog/CKEditor-5-v12.0.0-with-inline-widgets-and-distraction-free-editor-released/ "CKEditor 5 v12.0.0 with inline widgets and distraction free editor released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CKEditor 5 v12.0.0リリース。
Inline widgets、placeholderの対応、TableにMediaを埋め込めるように、inspector機能を持つデバッグモジュールの公開など


----

## Releasing React Native 0.59 · React Native
[facebook.github.io/react-native/blog/2019/03/12/releasing-react-native-059](https://facebook.github.io/react-native/blog/2019/03/12/releasing-react-native-059 "Releasing React Native 0.59 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ios</span> <span class="jser-tag">andoi</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.59リリース。
Hooksの対応、JavaScriptCoreをアップデートし、64 bitサポートなど。一部のコアコンポーネントを外部ライブラリ化など


----
<h1 class="site-genre">アーティクル</h1>

----

## 手元のコードのパフォーマンスを計測するperformance.markのスニペット | Web Scratch
[efcl.info/2019/03/14/performance-snnipet/](https://efcl.info/2019/03/14/performance-snnipet/ "手元のコードのパフォーマンスを計測するperformance.markのスニペット | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`performance.mark`を使った特定のコードの処理時間や関連データを記録するスニペットについて。
記録の計測とデータの収集を分けて行うことについて


----

## A Complete React Redux Tutorial for 2019
[daveceddia.com/redux-tutorial/](https://daveceddia.com/redux-tutorial/ "A Complete React Redux Tutorial for 2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Reduxについてのチュートリアル。
ステートの管理方法、ActionのDispatch方法やその動き、Reactと一緒に使う方法などについて


----

## Node.js and Express Tutorial: Building and Securing RESTful APIs
[auth0.com/blog/node-js-and-express-tutorial-building-and-securing-restful-apis/](https://auth0.com/blog/node-js-and-express-tutorial-building-and-securing-restful-apis/ "Node.js and Express Tutorial: Building and Securing RESTful APIs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">API</span> <span class="jser-tag">article</span></p>

Node.jsとExpressを使ってRest APIを作成するチュートリアル。
Auth0を使ったjwt対応など


----

## On the Road to WebRTC 1.0, Including VP8 | WebKit
[webkit.org/blog/8672/on-the-road-to-webrtc-1-0-including-vp8/](https://webkit.org/blog/8672/on-the-road-to-webrtc-1-0-including-vp8/ "On the Road to WebRTC 1.0, Including VP8 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">article</span> <span class="jser-tag">safari</span></p>

Safari 12.1のWebRTC対応更新について。
VP8コーデック、Simulcast、Unified Planの対応など。
Screen capture APIの実験的サポート、古いWebRTC APIの非推奨化など


----

## Update on Experimental Features in Node.js - NodeSource
[nodesource.com/blog/experimental-features-in-node.js](https://nodesource.com/blog/experimental-features-in-node.js "Update on Experimental Features in Node.js - NodeSource")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsの実験的な機能についての紹介記事。
Worker Threads、Performance Hooks、Diagnostic Report、Policy、ECMAScript Modulesについて


----

## 自社運営のWebアプリをPWA化した際にハマった話（OAuthなど） - APC 技術ブログ
[techblog.ap-com.co.jp/entry/2019/03/13/201027](https://techblog.ap-com.co.jp/entry/2019/03/13/201027 "自社運営のWebアプリをPWA化した際にハマった話（OAuthなど） - APC 技術ブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span> <span class="jser-tag">PWA</span> <span class="jser-tag">Android</span> <span class="jser-tag">Chrome</span></p>

AndroidとiOSでのPWA対応についての記事。
ホームスクリーンアプリにすると動かなくなった機能とその対処法などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Yahoo!ニュースにおけるBFFパフォーマンスチューニング事例
[www.slideshare.net/techblogyahoo/yahoobff](https://www.slideshare.net/techblogyahoo/yahoobff "Yahoo!ニュースにおけるBFFパフォーマンスチューニング事例")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

Node.jsのサーバアプリ処理のボトルネックの調査方法やベンチマークのとり方、アプローチなどについてのスライド


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## aruneko/WebUSB-MyNumberCard
[github.com/aruneko/WebUSB-MyNumberCard](https://github.com/aruneko/WebUSB-MyNumberCard "aruneko/WebUSB-MyNumberCard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

WebUSBを使ったマイナンバーカードのドライバ


----

## sindresorhus/type-fest: A collection of essential TypeScript types
[github.com/sindresorhus/type-fest](https://github.com/sindresorhus/type-fest "sindresorhus/type-fest: A collection of essential TypeScript types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScriptの型コレクションライブラリ


----
