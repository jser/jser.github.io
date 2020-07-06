---
title: "2020-07-06のJS: Firefox 78、Vue 3 Statusとリリーススケジュール"
author: "azu"
layout: post
date : 2020-07-06T13:25:56.945Z
category: JSer
tags:
- Firefox
- Vue

---

JSer.info #495 - Firefox 78がリリースされました。

- [New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/06/new-in-firefox-78/)
- [Firefox 78.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/)
- [Firefox 78 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/78)

Firefox 78は[Firefox Extended Support Release](https://support.mozilla.org/kb/choosing-firefox-update-channel)(ESR)のアップデートとなるバージョンです。また、前回のESR(Firefox 68相当)ではService Workerは無効化されていましたが、Firefox 78 ESRではサポートされています。

- <https://support.mozilla.org/ja/kb/firefox-enterprise-78-release-notes>

Firefox 78では開発者ツールが改善されています。
コンソールにPromiseのエラーをより詳細に表示、ネットワークパネルでリクエストの失敗理由の表示するなどの変更が含まれています。

CSSでは`:is`と`:where`のサポート、`:read-only`と`:read-write`のprefixなしをサポートしています。
また正規表現エンジンを新しくしたことでES2018のNamed Cature Groupsなどをサポートしています。

- [A New RegExp Engine in SpiderMonkey - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/06/a-new-regexp-engine-in-spidermonkey/)

その他にはTLS 1.0と1.1がデフォルトで無効化される変更が含まれています。

- [TLS 1.0/1.1 対応が初期設定で無効化されました (影響あり) | Firefox サイト互換性情報](https://www.fxsitecompat.dev/ja/docs/2020/tls-1-0-1-1-support-has-been-disabled-by-default/)

----

Vue 3のリリーススケジュールや提案されているRFCなどのステータスが公開されています。

- [Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs](https://github.com/vuejs/rfcs/issues/183)

元々は2020年前半のリリース予定でしたが、Vue 3 RCを7月中旬に、Vue 3を8月上旬に出す予定とのことです。
ロードマップについては次のProject boardでも管理されています。

- [Roadmap](https://github.com/vuejs/vue/projects/6)

このIssueでは、関連するパッケージのステータスや[JSXサポートに関する議論](https://github.com/vuejs/jsx/issues/141)について紹介されています。

関連する話として、Vue 2向けのVue3 Composition APIを提供する[@vue/composition-api](https://github.com/vuejs/composition-api) [v1.0.0-beta.1](https://github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1)がリリースされています。
また、Vue 2とVue 3どちらにも対応するライブラリを作るためのツールキットであるvue-demiが公開されています。

- [antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3](https://github.com/antfu/vue-demi)
- [Make Libraries Working with Vue 2 and 3 - Anthony Fu](https://antfu.me/posts/make-libraries-working-with-vue-2-and-3/)

その他にも、Vue 3リリース以降に入るかもしれないRFCなども出ているので、次のURLも参照してみてください。

- [SFC Improvements by yyx990803 · Pull Request #182 · vuejs/rfcs](https://github.com/vuejs/rfcs/pull/182)
- [Weekly Vue 2020-07-05 - DEV Community 👩‍💻👨‍💻](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-style-variables.md)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.0.0-beta.1 · vuejs/composition-api
[github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1](https://github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1 "Release v1.0.0-beta.1 · vuejs/composition-api")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 2向けのComposition API実装である@vue/composition-api 1.0.0 beta  1リリース


----

## New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/06/new-in-firefox-78/](https://hacks.mozilla.org/2020/06/new-in-firefox-78/ "New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 78リリース。ESRの更新バージョン。
コンソールにPromiseのエラーをより詳細に表示、ネットワークパネルでリクエストの失敗理由の表示などの開発者ツールの改善。
CSSの`:is`と`:where`のサポート、`:read-only`と`:read-write`のprefixなしをサポート。
正規表現のNamed Cature Groupsをサポート、`ParentNode.replaceChildren`のサポート。
TLS 1.0と1.1をデフォルトで無効化など

- [Firefox 78.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/ "Firefox 78.0, See All New Features, Updates and Fixes")
- [Firefox 78 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/78 "Firefox 78 for developers - Mozilla | MDN")

----

## Release v0.14.0 · video-dev/hls.js
[github.com/video-dev/hls.js/releases/tag/v0.14.0](https://github.com/video-dev/hls.js/releases/tag/v0.14.0 "Release v0.14.0 · video-dev/hls.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hls.js 0.14.0リリース。


----

## Node v14.5.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.5.0/](https://nodejs.org/en/blog/release/v14.5.0/ "Node v14.5.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v14.5.0リリース。
V8 8.3へアップデート、`EventTarget`を試験的に実装など


----

## V8 release v8.4 · V8
[v8.dev/blog/v8-release-84](https://v8.dev/blog/v8-release-84 "V8 release v8.4 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 8.4(Chrome 84)リリース。
WebAssembly SIMD APIがOrigin Trialで利用できるように、`WeakRef`のサポート、Private methodsとaccessorsのサポートなど


----

## Release v5.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v5.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v5.0.0 "Release v5.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v5.0.0リリース。
`page.emulateMedia`を `page.emulateMediaType`に変更。
Direct requireを削除し、オブジェクトとして読み込むように変更など


----

## Release Version 6.0.0 · react-hook-form/react-hook-form
[github.com/react-hook-form/react-hook-form/releases/tag/v6.0.0](https://github.com/react-hook-form/react-hook-form/releases/tag/v6.0.0 "Release Version 6.0.0 · react-hook-form/react-hook-form")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Hook Form 6.0.0リリース。


----

## Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs
[github.com/vuejs/rfcs/issues/183](https://github.com/vuejs/rfcs/issues/183 "Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

Vue 3のステータスについて。
7月にRC、8月に正式リリースの予定。


----

## Release 3.10.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.10.0](https://github.com/avajs/ava/releases/tag/v3.10.0 "Release 3.10.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3.10.0リリース。
`.only()`を利用中にスナップショットをアップデートしないように、`t.timeout`にメッセージオプションを追加、`t.try()`や`t.snapshot()`がhook中に実行できないように修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## Sign-in form best practices
[web.dev/sign-in-form-best-practices/](https://web.dev/sign-in-form-best-practices/ "Sign-in form best practices")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

`<form>`/`<input>`/`<label>`/`<button>`を使ったフォーム作成についてチェックリスト的な記事


----

## Creating an Application Performance Monitor Using Node 14 New and Experimental Features | Medium
[medium.com/@erickwendel/node-v14-x-is-up-deep-diving-into-new-features-ace6dd89ac0b](https://medium.com/@erickwendel/node-v14-x-is-up-deep-diving-into-new-features-ace6dd89ac0b "Creating an Application Performance Monitor Using Node 14 New and Experimental Features | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 14で利用できるExperimentalな機能を使ってアプリケーションのモニタリングをするAgentを作るという話。
Async Local Storage、Diagnostic Reportsについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## web.dev LIVE
[web.dev/live/](https://web.dev/live/ "web.dev LIVE")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Conference</span> <span class="jser-tag">video</span> <span class="jser-tag">google</span> <span class="jser-tag">Chrome</span></p>

web.devのセッション動画まとめ。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Overview | Tooling.Report
[bundlers.tooling.report/](https://bundlers.tooling.report/ "Overview | Tooling.Report")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">document</span></p>

browserify, parcel, rollup, webpackなどのbundlerの機能比較サイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## preactjs/compressed-size-action: GitHub Action that adds compressed size changes to your PRs.
[github.com/preactjs/compressed-size-action](https://github.com/preactjs/compressed-size-action "preactjs/compressed-size-action: GitHub Action that adds compressed size changes to your PRs.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

JavaScriptファイルのビルドサイズの変更を通知するGitHub Actions。


----

## tom-sherman/immurl: 🔗 A tiny immutable URL library, backed by the native whatwg URL.
[github.com/tom-sherman/immurl](https://github.com/tom-sherman/immurl "tom-sherman/immurl: 🔗 A tiny immutable URL library, backed by the native whatwg URL.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">library</span></p>

`URL`のimmutable版


----

## antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3
[github.com/antfu/vue-demi](https://github.com/antfu/vue-demi "antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Vue2と3に対応したライブラリを作成するためのライブラリ。
Vue2と3に互換性がないためどちらにも対応したライブラリを作るためのツールキット的なライブラリ

- [Make Libraries Working with Vue 2 and 3 - Anthony Fu](https://antfu.me/posts/make-libraries-working-with-vue-2-and-3/ "Make Libraries Working with Vue 2 and 3 - Anthony Fu")
- [Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs](https://github.com/vuejs/rfcs/issues/183#issuecomment-651944231 "Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs")

----
<h1 class="site-genre">書籍関係</h1>

----

## はじめに - サバイバルTypeScript
[book.yyts.org/](https://book.yyts.org/ "はじめに - サバイバルTypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span> <span class="jser-tag">ebook</span></p>

プログラミング経験のある人がTypeScriptを学ぶことを目的とした書籍


----
