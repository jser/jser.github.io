---
title: "2019-09-10のJS: Firefox 69、Babel 7.6.0(class private)、 Full Stackコースの教材"
author: "azu"
layout: post
date : 2019-09-10T02:39:56.538Z
category: JSer
tags:
- Firefox
- Babel
- Node.js

---

JSer.info #452 - Firefox 69がリリースされました。

- [Firefox 69.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/69.0/releasenotes/)
- [Firefox 69 — a tale of Resize Observer, microtasks, CSS, and DevTools - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/09/firefox-69-a-tale-of-resize-observer-microtasks-css-and-devtools/)
- [Firefox 69 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/69)
- [Firefox 69 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.dev/versions/69/)

Enhanced Tracking Protection (ETP)というanti-trackingの仕組みがデフォルトで有効化されました。
[Disconnect](https://disconnect.me/)のリストをベースにしたサードパーティトラッキングCookieのブロックが行われます。

- [Firefox Now Available with Enhanced Tracking Protection by Default Plus Updates to Facebook Container, Firefox Monitor and Lockwise - The Mozilla Blog](https://blog.mozilla.org/blog/2019/06/04/firefox-now-available-with-enhanced-tracking-protection-by-default/)
- [Security/Anti tracking policy - MozillaWiki](https://wiki.mozilla.org/Security/Anti_tracking_policy)

CSSの`@supports`がセレクタをサポートされ、ECMAScript ProposalのPublic class fieldのサポート、Resize Observerのサポート、`queueMicrotask`のサポートが含まれています。
また、`<keygen>`要素の削除やCSS `user-select`のprefixなしに対応しています。

開発者ツールでは、ネットワークパネルにCSPでブロックされた理由の表示されるようになり、リモートデバッグ用の`about:debugging`ページの改善、類似するコンソールメッセージのグループ化など行われるようになりました。

またこれはStableではなくNightlyでの変更ですが、コンソールに複数行のエディタモードが追加される予定です。

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Multi-line editor mode in <a href="https://twitter.com/FirefoxDevTools?ref_src=twsrc%5Etfw">@FirefoxDevTools</a> console. ❤️💡🥁 with a play/Run button. <a href="https://t.co/u36GyxO2Dx">pic.twitter.com/u36GyxO2Dx</a></p>&mdash; Mozilla WebCompat (@MozWebCompat) <a href="https://twitter.com/MozWebCompat/status/1170889728171753473?ref_src=twsrc%5Etfw">September 9, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

---

Babel 7.6.0がリリースされました。

- [7.6.0 Released: Private static accessors and V8 intrinsic syntax · Babel](https://babeljs.io/blog/2019/09/05/7.6.0)

現在Stage 3のPrivate static accessorsの変換もサポートされたため、これでClass Private Fieldに関するSyntaxをすべてサポートしたことになります。

- [tc39/proposal-class-fields: Orthogonally-informed combination of public and private fields proposals](https://github.com/tc39/proposal-class-fields#private-fields)
- [Public and private class fields · V8](https://v8.dev/features/class-fields)

その他にも、現在Stage 3のNullish coalescing operator (`??`)のエッジケースの対応改善なども含まれています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 69.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/69.0/releasenotes/](https://www.mozilla.org/en-US/firefox/69.0/releasenotes/ "Firefox 69.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 69.0リリース。
Enhanced Tracking Protection (ETP)の有効化。
CSSの`@supports`がセレクタをサポート.
またECMAScript ProposalのPublic class fieldのサポート、Resize Observerのサポート、`queueMicrotask`のサポートなど。
`<keygen>`要素の削除やCSS `user-select`のprefixなしに対応、ネットワークパネルにCSPでブロックされた理由の表示など

- [Firefox 69 — a tale of Resize Observer, microtasks, CSS, and DevTools - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/09/firefox-69-a-tale-of-resize-observer-microtasks-css-and-devtools/ "Firefox 69 — a tale of Resize Observer, microtasks, CSS, and DevTools - Mozilla Hacks - the Web developer blog")
- [Firefox 69 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/69 "Firefox 69 for developers - Mozilla | MDN")
- [Firefox 69 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/versions/69/ "Firefox 69 Site Compatibility | Firefox Site Compatibility")

----

## Node v12.10.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.10.0/](https://nodejs.org/en/blog/release/v12.10.0/ "Node v12.10.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.ja 12.10.0リリース。
`fs.rmdir`に`recursive`オプションの追加、`fs.createWriteStrea`に`emitClose`オプションの追加など


----

## Release Notes for Safari Technology Preview 91 | WebKit
[webkit.org/blog/9526/release-notes-for-safari-technology-preview-91/](https://webkit.org/blog/9526/release-notes-for-safari-technology-preview-91/ "Release Notes for Safari Technology Preview 91 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 91リリース。
TLS 1.0、1.1の無効化、`unhandledrejection`のサポート。
ES Proposalのhashbang、Optional Chainingのサポート


----

## 7.6.0 Released: Private static accessors and V8 intrinsic syntax · Babel
[babeljs.io/blog/2019/09/05/7.6.0](https://babeljs.io/blog/2019/09/05/7.6.0 "7.6.0 Released: Private static accessors and V8 intrinsic syntax · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

Babel 7.6.0リリース。
Private static Accessorsのサポート、Nullish coalescing operator (`??`)。
またV8の内部処理を呼び出すintrinsic runtime functions(`%`)のパースをサポートなど


----

## Release v0.6.1 · pikapkg/web
[github.com/pikapkg/web/releases/tag/v0.6.1](https://github.com/pikapkg/web/releases/tag/v0.6.1 "Release v0.6.1 · pikapkg/web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">module</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Module Bundlerの@pika/web 0.6リリース。
JavaScriptではない静的なアセットのサポート、monorepoサポート、Babelを使った最適化のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## What's New In DevTools (Chrome 78)  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/09/devtools](https://developers.google.com/web/updates/2019/09/devtools "What's New In DevTools (Chrome 78)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 78の開発者ツールの変更点について。
AuditがRequest Blockingなどと連携するように、Lighthouse 5.2へアップデートしLargest Contentful Paintのサポートなど


----

## Debugging WebAssembly Outside of the Browser - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/09/debugging-webassembly-outside-of-the-browser/](https://hacks.mozilla.org/2019/09/debugging-webassembly-outside-of-the-browser/ "Debugging WebAssembly Outside of the Browser - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span> <span class="jser-tag">video</span></p>

wasmtimeとGDB/LLDBを使ったWebAssemblyのデバッグ方法について。
LLDBでブレークポイントを貼ったり、変数をinspectしたりするデモ


----

## An Introduction to D3.js
[wattenberger.com/blog/d3](https://wattenberger.com/blog/d3 "An Introduction to D3.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">d3.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

D3.jsのモジュールについての紹介記事。
モジュールごとの機能や使い方について


----

## A simple homemade JavaScript obfuscator
[antoinevastel.com/javascript/2019/09/04/home-made-obfuscator.html](https://antoinevastel.com/javascript/2019/09/04/home-made-obfuscator.html "A simple homemade JavaScript obfuscator")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">article</span></p>

Shift-ASTを使ったコードの難読化スクリプトの作り方について。
ASTを使ったコード変換、terserを使った圧縮と変数名のリネーム、難読化したコードのテストについてなど


----

## 5 Handy Applications of JavaScript Array.from()
[dmitripavlutin.com/javascript-array-from-applications/](https://dmitripavlutin.com/javascript-array-from-applications/ "5 Handy Applications of JavaScript Array.from()")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`Array.from`の使い方やユースケースについて。
配列のコピー、指定要素でfillした配列の作成、配列の要素のユニーク化など


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Full Stack Open 2019
[fullstackopen.com/en/](https://fullstackopen.com/en/ "Full Stack Open 2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React, Redux, Node.js, MongoDB, GraphQLを使ってウェブアプリを作成しながら学べるコース。
ヘルシンキ大学の教材。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jhwohlgemuth/tomo-cli: A friendly command line tool designed to help create sustainable software using web technology
[github.com/jhwohlgemuth/tomo-cli](https://github.com/jhwohlgemuth/tomo-cli "jhwohlgemuth/tomo-cli: A friendly command line tool designed to help create sustainable software using web technology")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

開発環境のジェネレータツール。
特定のライブラリやツールに対するセットアップをコマンドでインストール、アンインストールできる。


----

## malijs/mali: A minimalistic gRPC microservice framework for Node.js
[github.com/malijs/mali](https://github.com/malijs/mali "malijs/mali: A minimalistic gRPC microservice framework for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

gRPCを使ったNode.jsフレームワーク。
koaライクなmiddlewareのサポートや、gRPCのMetadataサポートなどをしている。


----
<h1 class="site-genre">書籍関係</h1>

----

## これからはじめるVue.js実践入門 | 山田 祥寛 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4815601828/](https://www.amazon.co.jp/dp/4815601828/ "これからはじめるVue.js実践入門 | 山田 祥寛 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">book</span></p>

2019年8月22日発売
Vue.jsの入門書


----
