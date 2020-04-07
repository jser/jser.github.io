---
title: "2020-04-07のJS: ES2020 Candidate、WebdriverIO v6、ブラウザのリリース情報の追い方"
author: "azu"
layout: post
date : 2020-04-07T01:38:40.312Z
category: JSer
tags:
- ECMAScript
- WebDriver
- Browser

---

JSer.info #482 - ECMAScript 2020のリリース候補が公開されました。

- [Release ES2020 Candidate · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2020)

[ES2020 Candidate](https://tc39.es/ecma262/2020/)はTC39での承認が通った形で、2020年6月にあるEcmaの[General Assembly](https://www.ecma-international.org/memento/ga.htm)で承認されると正式にECMAScript 2020としてリリースされます。

また、今回3月から4月にかけて行われたTC39ミーティングで`import.meta`がStage 4となっています。

- [ECMAScript proposal updates @ 2020-04 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update)

そのため、`import.meta`もギリギリES2020に含まれることになっています。
ES2020に含まれるProposalは次のページにまとめられています。

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md)
- [ECMAScript 2020: the final feature set](https://2ality.com/2019/12/ecmascript-2020.html)

----

WebdriverIO v6がリリースされました。

- [WebdriverIO v6 Released · WebdriverIO](https://webdriver.io/blog/2020/03/26/webdriverio-v6-released.html)

WebdriverIO v6では`devtools`がデフォルト化されています。
WebdriverIOはWebdriver APIを使いますが、現状のWebdriver APIでは、接続したブラウザの開発者ツールを使うことができません。
そのため`devtools`ではPuppeteerを統合することでこの問題を回避しています。

- [Chrome DevTools as Automation Protocol · WebdriverIO](https://webdriver.io/blog/2019/09/16/devtools.html)

Webdriver APIの方もMSEdge Teamが双方向通信のProposalを公開しています。

- [MSEdgeExplainers/WebDriverRPC at master · MicrosoftEdge/MSEdgeExplainers](https://github.com/MicrosoftEdge/MSEdgeExplainers/tree/master/WebDriverRPC)

その他には、非推奨となった[request](https://github.com/request/request)の代わりに[got](https://github.com/sindresorhus/got)を使うことでパフォーマンスの改善やTypeScriptサポートなどが追加されています。

----

JSer.infoでもブラウザのリリース情報を追っていますが、ブラウザのリリース情報などの追い方をまとめたリンク集を公開しました。

- [ブラウザ/セキュリティ/プライバシー周りの一次情報に近い二次情報の情報源をまとめたもの](https://gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511)

実際にはもっと大量のリソースをベースに見てみていますが、情報源に近いところをまとめています。

これに合わせてブラウザの公式ブログやIssue、SNSなどをまとめたbrowser-resourcesも更新しています。

- [azu/browser-resources: A Collection of official Resources/Status/Issues for browsers.](https://github.com/azu/browser-resources)

その他のものとしては、ブラウザ周りのRSSなどをまとめた次のサイトが追いやすいかもしれません。

- [Web Browser Eng](https://topicdeck.com/web-dev/browser-eng/chromium/)
- [PaulKinlan/topicdeck: An NPM module that hosts and aggregates collections of RSS feeds.](https://github.com/PaulKinlan/topicdeck)
    - Chromeチームの[Paul Kinlan](https://github.com/PaulKinlan)が管理している

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release ES2020 Candidate · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2020](https://github.com/tc39/ecma262/releases/tag/es2020 "Release ES2020 Candidate · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ES2020のリリース候補が公開された。
`import.meta`もES2020に含まれている。


----

## WebdriverIO v6 Released · WebdriverIO
[webdriver.io/blog/2020/03/26/webdriverio-v6-released.html](https://webdriver.io/blog/2020/03/26/webdriverio-v6-released.html "WebdriverIO v6 Released · WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

WebdriverIO v6リリース。
Node 8のサポート終了、Puppeteerの統合と`devtools`パッケージのデフォルト化、`request`から`got`への移行によるパフォーマンスの改善、TypeScriptサポートなど


----

## Chromium Blog: Temporarily rolling back SameSite Cookie Changes
[blog.chromium.org/2020/04/temporarily-rolling-back-samesite.html](https://blog.chromium.org/2020/04/temporarily-rolling-back-samesite.html "Chromium Blog: Temporarily rolling back SameSite Cookie Changes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">news</span> <span class="jser-tag">security</span></p>

Chrome 80で段階的にロールアウトされていたデフォルトをSameSite=Laxとする変更を、一時的にロールバックしてデフォルトを変更しないようにするとのこと。
再展開は夏を目標にしている。

- [SameSite Updates - The Chromium Projects](https://www.chromium.org/updates/same-site "SameSite Updates - The Chromium Projects")

----

## New WebKit Features in Safari 13.1 | WebKit
[webkit.org/blog/10247/new-webkit-features-in-safari-13-1/](https://webkit.org/blog/10247/new-webkit-features-in-safari-13-1/ "New WebKit Features in Safari 13.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 13.1の変更点について。
iPadOS 13.4でのPointer Eventsの対応。Web Animations API、Async Clipboard API、ResizeObserver、Picture-in-Pictureのサポート。
ES ProposalのNullish coalesing operator(`??`)のサポート、CSS Shadow Partsのサポート、ITPのアップデートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## ブラウザ/セキュリティ/プライバシー周りの一次情報に近い二次情報の情報源をまとめたもの
[gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511](https://gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511 "ブラウザ/セキュリティ/プライバシー周りの一次情報に近い二次情報の情報源をまとめたもの")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span> <span class="jser-tag">MSEdge</span> <span class="jser-tag">Firefox</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">safari</span> <span class="jser-tag">webkit</span></p>

ブラウザの新しいAPIやリリースなどの追い方や参考リソースのまとめ


----

## ECMAScript proposal updates @ 2020-04 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update "ECMAScript proposal updates @ 2020-04 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2020-03から2020-04にかけて行われたTC39MTGで変更があったProposalのまとめ。
`import.meta`がStage 4となり、ECMAScript 2020に含まれる。

- [Release ES2020 Candidate · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2020 "Release ES2020 Candidate · tc39/ecma262")

----

## LCH colors in CSS: what, why, and how? | Lea Verou
[lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/](http://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/ "LCH colors in CSS: what, why, and how? | Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Color Modules Level 4で定義されているLCHカラーについて。
LCHとは何かやなぜ導入されているのかについて。RGBと比較してより多くの色にアクセスできる点などについて解説している


----

## フロントエンド x RTC界隈の最近とこれから - console.lealog();
[lealog.hateblo.jp/entry/2020/04/02/094225](https://lealog.hateblo.jp/entry/2020/04/02/094225 "フロントエンド x RTC界隈の最近とこれから - console.lealog();")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

WebRTC周りのWeb Platform APIのステータスやProposalについて。
WebTransport、WebRTC-QUIC、WebCodecs、WebSocketStreamなどの関連するAPIについて


----

## A QUIC Update for Node.js
[www.nearform.com/blog/a-quic-update-for-node-js/](https://www.nearform.com/blog/a-quic-update-for-node-js/ "A QUIC Update for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span> <span class="jser-tag">QUIC</span></p>

Node.jsでのQUICプロトコルの実装について。
QUICの概要や、Node.js Coreに追加する目的で実装している `quic` モジュールについて

- [nodejs/quic: Exploring a QUIC implementation for Node.js core](https://github.com/nodejs/quic "nodejs/quic: Exploring a QUIC implementation for Node.js core")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## engine262/engine262: An implementation of ECMA-262 in JavaScript
[github.com/engine262/engine262](https://github.com/engine262/engine262 "engine262/engine262: An implementation of ECMA-262 in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

JavaScriptによるECMAScript実装。
JavaScript開発者が新しい言語機能のプロトタイピングを簡単にできるようにするのが目的


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Lezer
[lezer.codemirror.net/](https://lezer.codemirror.net/ "Lezer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AST</span></p>

インクリメンタルなパースを行うパーサシステムライブラリ。
文法を定義し、パースをインクリメンタルに行いエラー復帰なども対応したASTを生成するパーサジェネレータ。
エディタのシンタックスハイライトのような用途で利用でき、CodeMirrorチームによって開発されている。


----

## lirantal/npq: 🎖safely\* install packages with npm or yarn by auditing them as part of your install process
[github.com/lirantal/npq](https://github.com/lirantal/npq "lirantal/npq: 🎖safely\* install packages with npm or yarn by auditing them as part of your install process")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npmやyarnでパッケージをインストールする際に、パッケージのダウンロード数、READMEのうむ、インストールスクリプト、Snykでのチェックを行うCLI


----

## Keyboard Event Viewer
[w3c.github.io/uievents/tools/key-event-viewer.html](https://w3c.github.io/uievents/tools/key-event-viewer.html "Keyboard Event Viewer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Keyboard</span> <span class="jser-tag">Tools</span> <span class="jser-tag">DOM</span></p>

JavaScriptのKeyboard Eventビューア


----

## caroso1222/notyf: 👻 A minimalistic, responsive, vanilla JavaScript library to show toast notifications.
[github.com/caroso1222/notyf](https://github.com/caroso1222/notyf "caroso1222/notyf: 👻 A minimalistic, responsive, vanilla JavaScript library to show toast notifications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

依存がないToast通知を行うUIライブラリ。


----
