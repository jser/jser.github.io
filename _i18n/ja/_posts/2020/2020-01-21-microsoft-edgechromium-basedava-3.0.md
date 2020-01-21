---
title: "2020-01-21のJS: 新しいMicrosoft Edge(Chromium-based)、AVA 3.0リリース"
author: "azu"
layout: post
date : 2020-01-21T02:07:39.513Z
category: JSer
tags:
- MSEdge
- AVA
- Testing

---

JSer.info #471 - Chromiumベースの新しいMicrosoft Edgeが正式リリースされました。

- [Download New Microsoft Edge Browser | Microsoft](https://www.microsoft.com/en-us/edge)
- [New year, new browser - The new Microsoft Edge is out of preview and now available for download | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2020/01/15/new-year-new-browser-the-new-microsoft-edge-is-out-of-preview-and-now-available-for-download/)
- [Upgrading to the new Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2020/01/15/upgrading-new-microsoft-edge-79-chromium/)

Windows 7+、macOSに対応していて、当初から発表されていたようにChromiumベースにしています。

- [Microsoft Edge: Making the web better through more open source collaboration | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/)

エンジンは基本的にはChromeと同じとなりますが、ブラウザのUIやTracking Preventionなど機能的には異なる部分があります。

- <https://microsoftedgewelcome.microsoft.com/privacy>
- [Improving Tracking Prevention in Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/12/03/improving-tracking-prevention-microsoft-edge-79/)

レンダリングエンジンがEdgeHTMLであった従来のMSEdgeの方はEdge Legacyと呼ぶようです。

- [Dev channel update to 80.0.361.5 is live - Microsoft Tech Community - 1070730](https://techcommunity.microsoft.com/t5/discussions/dev-channel-update-to-80-0-361-5-is-live/m-p/1070730)


----

Node.jsのテストフレームワークであるAVA 3.0がリリースされました。

- [Release 3.0.0 · avajs/ava](https://github.com/avajs/ava/releases/tag/v3.0.0)

[node --inspect](https://nodejs.org/de/docs/guides/debugging-getting-started/)と連携する`ava debug`コマンドの追加、Node.jsに対して引数を渡す`--node-arguments`オプションの追加などが行われています。

破壊的な変更としてはNode 10未満のサポート終了、Babelが同梱ではなくなり別パッケージとしてインストールする形に変更されています。

- [avajs/babel: Babel provider for AVA.](https://github.com/avajs/babel)

また、ES Modulesのサポートをしていくために`.cjs`と`.mjs`をテストファイルとして認識するようになっています。

ES Modules対応については次のProject Boardで追跡できます。

- [ESM support](https://github.com/orgs/avajs/projects/2)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v7.0.0-esm1 (experimental) · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v7.0.0-esm1](https://github.com/mochajs/mocha/releases/tag/v7.0.0-esm1 "Release v7.0.0-esm1 (experimental) · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MochaのES Modules対応のExperimental版がリリースされた


----

## New year, new browser - The new Microsoft Edge is out of preview and now available for download | Windows Experience Blog
[blogs.windows.com/windowsexperience/2020/01/15/new-year-new-browser-the-new-microsoft-edge-is-out-of-preview-and-now-available-for-download/](https://blogs.windows.com/windowsexperience/2020/01/15/new-year-new-browser-the-new-microsoft-edge-is-out-of-preview-and-now-available-for-download/ "New year, new browser - The new Microsoft Edge is out of preview and now available for download | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

ChromiumベースのMicrosoft Edgeが公開された。
Windows 7+、macOSに対応したバージョンが配布されている。

- [Upgrading to the new Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2020/01/15/upgrading-new-microsoft-edge-79-chromium/ "Upgrading to the new Microsoft Edge - Microsoft Edge Blog")
- [Download New Microsoft Edge Browser | Microsoft](https://www.microsoft.com/en-us/edge "Download New Microsoft Edge Browser | Microsoft")

----

## mustache.js/CHANGELOG.md at master · janl/mustache.js
[github.com/janl/mustache.js/blob/master/CHANGELOG.md#400--16-january-2020](https://github.com/janl/mustache.js/blob/master/CHANGELOG.md#400--16-january-2020 "mustache.js/CHANGELOG.md at master · janl/mustache.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

テンプレートエンジンであるmustache 4.0.0リリース。
`.to_html()`メソッドの削除、テンプレートのキャッシュの仕組みをカスタマイズできるようになるなど。


----

## TestCafe v1.8.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v1-8-0-released.html](https://devexpress.github.io/testcafe/blog/testcafe-v1-8-0-released.html "TestCafe v1.8.0 Released | TestCafe")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v1.8.0リリース。
Chromium版MSEdgeをサポートなど


----

## ECMAScript Archives
[www.ecma-international.org/archive/ecmascript/](https://www.ecma-international.org/archive/ecmascript/ "ECMAScript Archives")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

ECMAScript Archives Page。
過去のECMAScript仕様に関するTC39MTGのミーティングログのアーカイブやドキュメント。
1996年から2015年までのアーカイブ


----

## Blog - Next.js 9.2 | Next.js
[nextjs.org/blog/next-9-2](https://nextjs.org/blog/next-9-2 "Blog - Next.js 9.2 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 9.2リリース。
ビルトインでCSSファイルをimportできるように、`.module.css`でCSS Modulesとしてimportできるように。
Code Splittingに関するwebpackの設定を変更し、chunks作成時の戦略を変更など


----

## Release 3.0.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.0.0](https://github.com/avajs/ava/releases/tag/v3.0.0 "Release 3.0.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3リリース。
`ava debug`コマンドの追加、`--node-arguments`オプションの追加。
Node 10未満のサポート終了、Babelが同梱ではなくなり別パッケージとしてインストールする形に変更、ES Modulesのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## ブラウザで何が起こっているのかを知る Reporting API と ReportingObserver | blog.jxck.io
[blog.jxck.io/entries/2020-01-18/reporting.html](https://blog.jxck.io/entries/2020-01-18/reporting.html "ブラウザで何が起こっているのかを知る Reporting API と ReportingObserver | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

ブラウザで起きたエラーレポートなどを送信、監視するReporting APIとReportingObserverについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## GoogleCloudPlatform/wombat-dressing-room: proxy designed to reduce the attack surface of npm publish
[github.com/GoogleCloudPlatform/wombat-dressing-room](https://github.com/GoogleCloudPlatform/wombat-dressing-room "GoogleCloudPlatform/wombat-dressing-room: proxy designed to reduce the attack surface of npm publish")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Github</span> <span class="jser-tag">security</span></p>

GitHubリポジトリに紐付いたnpm publishをするための認証トークンを発行するシステム。npm registryに対する2FA Proxy。
トークンと該当するGitHubのタグがある場合にのみpublishでき、トークンはパッケージごとに異なるため流出しても特定のパッケージのみに影響を抑える目的。

- [Wombat Dressing Room, an npm publication proxy on GCP | Google Open Source Blog](https://opensource.googleblog.com/2020/01/wombat-dressing-room-npm-publication_10.html "Wombat Dressing Room, an npm publication proxy on GCP | Google Open Source Blog")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## wasm3/wasm3: 🚀 The fastest WebAssembly interpreter
[github.com/wasm3/wasm3](https://github.com/wasm3/wasm3 "wasm3/wasm3: 🚀 The fastest WebAssembly interpreter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span></p>

WebAssemblyのインタープリター


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## logaretm/villus: A tiny and fast GraphQL client for Vue.js
[github.com/logaretm/villus](https://github.com/logaretm/villus "logaretm/villus: A tiny and fast GraphQL client for Vue.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span></p>

Vue.js向けのGraphQLクライアントライブラリ。

- [Announcing Villus - A tiny and fast GraphQL Client for Vue.js - Abdelrahman' Blog](https://logaretm.com/blog/2020-01-11-announcing-villus/ "Announcing Villus - A tiny and fast GraphQL Client for Vue.js - Abdelrahman&#x27; Blog")

----

## gjtorikian/isBinaryFile: Detects if a file is binary in Node.js. Similar to Perl's -B
[github.com/gjtorikian/isBinaryFile](https://github.com/gjtorikian/isBinaryFile "gjtorikian/isBinaryFile: Detects if a file is binary in Node.js. Similar to Perl's -B")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">library</span></p>

ファイルがバイナリかどうかを判定するNode.jsライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Cookie 概説 - 30歳からのプログラミング
[numb86-tech.hatenablog.com/entry/2020/01/19/004420](https://numb86-tech.hatenablog.com/entry/2020/01/19/004420 "Cookie 概説 - 30歳からのプログラミング")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag"> node</span> <span class="jser-tag">security</span></p>

ブラウザとexpressを使ったCookieの設定と属性などのCookieの仕組みについての解説記事。
Expires、Max-Age、Domain、Path，Secure属性、HttpOnly属性、SameSite属性についての解説


----
