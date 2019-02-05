---
title: "2019-02-05のJS: Firefox 65(WebP)、Safari 12.1(リリース候補)、ECMAScript 2019の機能決定"
author: "azu"
layout: post
date : 2019-02-05T00:35:02.073Z
category: JSer
tags:
- firefox
- safari
- ECMAScript

---

JSer.info #421 - Firefox 65がリリースされました。

- [Firefox 65.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/65.0/releasenotes/ "Firefox 65.0, See All New Features, Updates and Fixes")
- [Firefox 65 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/65 "Firefox 65 for developers - Mozilla | MDN")
- [Firefox 65 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/65/ "Firefox 65 サイト互換性情報 | Firefox サイト互換性情報")
- [Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/01/firefox-65-webp-flexbox-inspector-new-tooling/ "Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog")

Firefox 65では[CSS Flexbox Inspector](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Examine_Flexbox_layouts)の追加といった開発者ツールの改善、CSS `env()`のサポート、`Intl.RelativeTimeFormat`や`globalThis`の実装がされています。
また、今までフラグ付きであったStorage Access APIとReadable Streamsがデフォルトで有効化されています。

[RFC 8441 - Bootstrapping WebSockets with HTTP/2](https://tools.ietf.org/html/rfc8441)として標準化されたWebSocketsのHTTP/2対応、画像形式のWebPのサポートなどが追加されています。

----

iOS 12.2/macOS 10.14.4と合わせて公開予定のSafari 12.1のリリースノートが公開されています。(まだ正式リリースはされていません)

- [Safari 12.1 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari_release_notes/safari_12_1_release_notes)

Safari 12.1は[Safari Technology Preview 62](https://webkit.org/blog/8384/release-notes-for-safari-technology-preview-62/)からの変更が含まれているようです。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Safari Technology Preview 62 is out!<br><br>A small note: STP 62 bumps its Safari version number from 12.0 to 12.1. That is, STP is now tracking a release after Safari 12.<br><br>Release Notes: <a href="https://t.co/vt8myfz7NO">https://t.co/vt8myfz7NO</a> <a href="https://t.co/yrgHQyUpSa">pic.twitter.com/yrgHQyUpSa</a></p>&mdash; Ricky Mondello (@rmondello) <a href="https://twitter.com/rmondello/status/1024708391396995072?ref_src=twsrc%5Etfw">August 1, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Safari 12.1ではITP(Intelligent Tracking Prevention)の強化、ダークモードサポートのためのcolor scheme系APIのサポート、Intersection Observer API、Web Share API、`<datalist>`のサポートが追加されています。
また、WebRTC Unified PlanとVP8サポートがサポートが追加されています。

- [Safari 12.1 で VP8 と Unified Plan が入る – V – Medium](https://medium.com/@voluntas/safari-12-1-%E3%81%A7-vp8-%E3%81%A8-unified-plan-%E3%81%8C%E5%85%A5%E3%82%8B-47c3aa0cb9eb)

----

2019年1月にTC39のミーティングが行われECMAScript 2019に入る機能が決定されました。
ECMAScript 2019は2019年6月ごろにリリース予定のため、1月の段階で入る機能が決定されます。

- [agendas/11.md at master · tc39/agendas](https://github.com/tc39/agendas/blob/master/2018/11.md)
- [ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch](https://efcl.info/2015/10/18/ecmascript-paper/)

1月のミーティングでは`Object.fromEntries`、Well-formed `JSON.stringify`、`String.prototype.{trimStart,trimEnd}`、`Array.prototype.{flat,flatMap}`がStage 4となりES 2019に入ります。

- [\[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates)

最終的にES2019へと入る機能は次のページでまとめられています。

- [ECMAScript 2019: the final feature set](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")
- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

メソッドの追加などが中心で、DecoratorやPrivate fieldなどの構文的な大きなProposalはまだStage 4ではないため、ES2019には入りません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 65.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/65.0/releasenotes/](https://www.mozilla.org/en-US/firefox/65.0/releasenotes/ "Firefox 65.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 65.0リリース。
CSS `env()`のサポート、`Intl.RelativeTimeFormat`/`globalThis`の実装、Storage Access API/Readable Streamsをデフォルトで有効化。
WebSocketsのHTTP/2対応、WebP画像のサポートなど

- [Firefox 65 for developers | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/65 "Firefox 65 for developers | MDN")
- [Firefox 65 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/65/ "Firefox 65 サイト互換性情報 | Firefox サイト互換性情報")
- [Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/01/firefox-65-webp-flexbox-inspector-new-tooling/ "Firefox 65: WebP support, Flexbox Inspector, new tooling &amp; platform updates - Mozilla Hacks - the Web developer blog")

----

## Release v2.0.0 · facebook/relay
[github.com/facebook/relay/releases/tag/v2.0.0](https://github.com/facebook/relay/releases/tag/v2.0.0 "Release v2.0.0 · facebook/relay")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

GraphQL + ReactライブラリのRepay v2.0.0リリース。
Reactの新しいContext APIに対応、依存の更新、`replay-compiler`がPersisted Queriesのサポートなど

- [Persisted Queries · Relay](https://facebook.github.io/relay/docs/en/persisted-queries.html "Persisted Queries · Relay")

----

## New in Chrome 72  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/01/nic72](https://developers.google.com/web/updates/2019/01/nic72 "New in Chrome 72  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 72リリース。
Public class fields、User Activation API、`Intl.format`のサポートなど。
またHPKPの削除、TLS 1.0と1.1を非推奨化など

- [Chromium Blog: Chrome 72 Beta: Public class fields, user activation and more](https://blog.chromium.org/2018/12/chrome-72-beta-public-class-fields-user.html "Chromium Blog: Chrome 72 Beta: Public class fields, user activation and more")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D72 "Chrome Platform Status")
- [Deprecations and removals in Chrome 72  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/12/chrome-72-deps-rems "Deprecations and removals in Chrome 72  |  Web  |  Google Developers")

----

## Safari 12.1 Release Notes | Apple Developer Documentation
[developer.apple.com/documentation/safari\_release\_notes/safari\_12\_1\_release\_notes](https://developer.apple.com/documentation/safari_release_notes/safari_12_1_release_notes "Safari 12.1 Release Notes | Apple Developer Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 12.1のリリースノート(iOS 12.2/macOS 10.14.4の予定)。
ITPの強化、color schemeのサポート、Intersection Observer API、Web Share API、`<datalist>`のサポート。
WebRTC Unified PlanとVP8サポートなど

- [Ricky Mondelloによる解説](https://twitter.com/rmondello/status/1091073294202269696 "Ricky Mondelloによる解説")

----

## Announcing TypeScript 3.3 | TypeScript
[blogs.msdn.microsoft.com/typescript/2019/01/31/announcing-typescript-3-3/](https://blogs.msdn.microsoft.com/typescript/2019/01/31/announcing-typescript-3-3/ "Announcing TypeScript 3.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.3リリース。
関数呼び出しにおけるUnion Typeの扱いを改善、`--build`の`--watch`でインクリメンタルビルドをサポートなど

- [TypeScript v3.3.0-rc 変更点 - Qiita](https://qiita.com/vvakame/items/dadc91f0be6fc00085ae "TypeScript v3.3.0-rc 変更点 - Qiita")

----

## Type Safe JavaScript with JSDoc – TruckJS – Medium
[medium.com/@trukrs/type-safe-javascript-with-jsdoc-7a2a63209b76](https://medium.com/@trukrs/type-safe-javascript-with-jsdoc-7a2a63209b76 "Type Safe JavaScript with JSDoc – TruckJS – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSDoc</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">VSCode</span></p>

JSDocと`jsconfig.json`での型チェックについて。
`tsc`の`checkJS`機能を使ってJavaScriptのままJSDocの型チェック行う話


----

## \[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates "\[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2019年1月のTC39ミーティングでのECMAScript Proposalの更新まとめ。
今回のミーティングまでにStage 4となったものがES2019となる。

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")
- [ECMAScript 2019: the final feature set](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")

----
<h1 class="site-genre">アーティクル</h1>

----

## Code-splitting for libraries—bundling for npm with Rollup 1.0
[levelup.gitconnected.com/code-splitting-for-libraries-bundling-for-npm-with-rollup-1-0-2522c7437697](https://levelup.gitconnected.com/code-splitting-for-libraries-bundling-for-npm-with-rollup-1-0-2522c7437697 "Code-splitting for libraries—bundling for npm with Rollup 1.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

Rollupを使ってどのようにライブラリをbundleするかやnpmに公開するかについて。
umd、esm、cjs形式での配布について


----

## ECMAScript 2019: the final feature set
[2ality.com/2018/02/ecmascript-2019.html](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript 2019の入る機能が1月のTC39ミーティングで最終決定された。

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

----

## RTCQuicTransport Coming to an Origin Trial Near You (Chrome 73)  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/01/rtcquictransport-api](https://developers.google.com/web/updates/2019/01/rtcquictransport-api "RTCQuicTransport Coming to an Origin Trial Near You (Chrome 73)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">QUIC</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 73でQUICでの接続してデータのやりとりをするAPIである`RTCQuicTransport`のOrigin Trialが開始された。
WebRTC NV(Next Version)への取り組みとして、UDP上のQUICを使ったLow Level APIの策定が目的。

- [shampson/RTCQuicTransport-Origin-Trial-Documentation: Documentation and demos for developers using the RTCQuicTransport in Chrome's origin trial.](https://github.com/shampson/RTCQuicTransport-Origin-Trial-Documentation "shampson/RTCQuicTransport-Origin-Trial-Documentation: Documentation and demos for developers using the RTCQuicTransport in Chrome&#x27;s origin trial.")
- [WebRTC over QUIC – V – Medium](https://medium.com/@voluntas/webrtc-over-quic-d65425230ef "WebRTC over QUIC – V – Medium")

----

## Severe Security Vulnerability in Bower’s Zip Archive Extraction | Snyk
[snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction/](https://snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction/ "Severe Security Vulnerability in Bower’s Zip Archive Extraction | Snyk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">ReleaseNote</span></p>

Bowerのzip/tarの解凍処理に脆弱性があり修正バージョンとしてBower 1.8.8がリリースされた。

- [Release v1.8.8 · bower/bower](https://github.com/bower/bower/releases/tag/v1.8.8 "Release v1.8.8 · bower/bower")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Chrome University 2018 - YouTube
[www.youtube.com/playlist?list&#x3D;PL9ioqAuyl6UIFAdsM5KU6P-hRJdh-BPmm](https://www.youtube.com/playlist?list=PL9ioqAuyl6UIFAdsM5KU6P-hRJdh-BPmm "Chrome University 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">video</span></p>

ChromeとChrome OSのアーキテクチャについての発表動画まとめ。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ungap
[ungap.github.io/](https://ungap.github.io/ "ungap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span></p>

ECMAScriptやDOM APIに関するES5互換なPolyfillをまとめるプロジェクト。
それぞれのpolyfillがモジュールとして利用でき、1つのOrganizationとして管理するのが目的


----

## nextapps-de/flexsearch: Next-Generation full text search library for Browser and Node.js
[github.com/nextapps-de/flexsearch](https://github.com/nextapps-de/flexsearch "nextapps-de/flexsearch: Next-Generation full text search library for Browser and Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search </span> <span class="jser-tag">library</span></p>

ブラウザとNode.jsで動く全文検索エンジンライブラリ。
WebWorkerの対応や検索モードのオプションが用意されている


----

## lukeed/httpie: A Node.js HTTP client as easy as pie! 🥧
[github.com/lukeed/httpie](https://github.com/lukeed/httpie "lukeed/httpie: A Node.js HTTP client as easy as pie! 🥧")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Node.js向けのシンプルなPromise HTTPライブラリ。
Nodeコアモジュールのみを利用している。


----
<h1 class="site-genre">書籍関係</h1>

----

## Chrome Developer Tools 入門 | 電子書籍とプリントオンデマンド（POD） | NextPublishing（ネクストパブリッシング）
[nextpublishing.jp/book/10430.html](https://nextpublishing.jp/book/10430.html "Chrome Developer Tools 入門 | 電子書籍とプリントオンデマンド（POD） | NextPublishing（ネクストパブリッシング）")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">book</span></p>

2019年2月1日発売
Chrome Developer Toolsについての書籍


----
