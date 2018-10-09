---
title: "2018-10-09のJS: Create React App 2.0、EdgeHTML 18、Node.jsフレームワークアンケート"
author: "azu"
layout: post
date : 2018-10-09T02:30:12.103Z
category: JSer
tags:
- reactjs
- msedge
- nodejs

---

JSer.info #404 - Reactを使った開発環境ツールであるCreate React App 2.0がリリースされました。

- [Create React App 2.0: Babel 7, Sass, and More – React Blog](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html "Create React App 2.0: Babel 7, Sass, and More – React Blog")
- [Release v2.0.3 · facebook/create-react-app](https://github.com/facebook/create-react-app/releases/tag/v2.0.3 "Release v2.0.3 · facebook/create-react-app")

Babel 7、webpack 4、Jest 23と依存モジュールがメジャーアップデートされています。
またNode.js 6のサポート終了、IE11のサポートを行うため最低限のpolyfillが[react-app-polyfill](https://github.com/facebook/create-react-app/tree/master/packages/react-app-polyfill)というパッケージで導入できるようになっています。

[Proxyの設定方法変更](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#configuring-the-proxy-manually)、Service Workerをオプトインになるといった変更が行われています。

----

Windows 10 October 2018 Updateに含まれているEdgeHTML 18の変更内容が公開されています。

- [What’s new in Microsoft Edge in the Windows 10 October 2018 Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2018/10/04/edgehtml-18-october-2018-update/#KO7TAJrEFfU4x13A.97)
- [EdgeHTML 18](https://docs.microsoft.com/en-us/microsoft-edge/dev-guide?WT.mc_id=windowsdocs-twitter#new-apis-in-edgehtml-18)

Web Authenticationの実装、Media autoplay policy、CSS masking、background blend、Web Notificationでbadgeプロパティなどをサポートが追加されています。

またXSSフィルターが廃止されContent Security Policy (CSP)を代わりに使うことが推奨されています。

- [Announcing Windows 10 Insider Preview Build 17723 and Build 18204 - Windows Experience BlogWindows Experience Blog](https://blogs.windows.com/windowsexperience/2018/07/25/announcing-windows-10-insider-preview-build-17723-and-build-18204/)

----

[On Node Framework Popularity – hueniverse](https://hueniverse.com/on-node-framework-popularity-355fbde5cbe4)という記事ではNode.jsのウェブアプリケーションフレームワークについてのアンケート結果が公開されています。

Express、Hapi、Koaなどの利用率や好み、使い続けるかについてのアンケート結果がまとめられています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Create React App 2.0: Babel 7, Sass, and More – React Blog
[reactjs.org/blog/2018/10/01/create-react-app-v2.html](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html "Create React App 2.0: Babel 7, Sass, and More – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 2.0リリース。
Babel 7、webpack 4、Jest 23に更新。
Node.js 6のサポート終了、IE11のサポートを行うpolyfillを分離、Proxyの設定方法変更、Service Workerをオプトインに変更など


----

## Release v1.9.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.9.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.9.0 "Release v1.9.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v1.9.0リリース。
Chromium 71.0に更新、async stack tracesのサポート、Browserifyでbundleできるようになりブラウザ上でも実行できるように。
`frame.goto`や`frame.waitForNavigation`の追加など


----

## What’s new in Microsoft Edge in the Windows 10 October 2018 Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2018/10/04/edgehtml-18-october-2018-update/](https://blogs.windows.com/msedgedev/2018/10/04/edgehtml-18-october-2018-update/ "What’s new in Microsoft Edge in the Windows 10 October 2018 Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

Windows 10 October 2018 Updateに含まれるEdgeHTML 18の変更点について。
Web Authenticationの実装、Media autoplay policyの導入、CSS masking、background blendのサポート。
Web Notificationでbadgeをサポート、XSSフィルターの廃止など

- [What's new in EdgeHTML 18 - Microsoft Edge Development | Microsoft Docs](https://docs.microsoft.com/en-us/microsoft-edge/dev-guide?WT.mc_id=windowsdocs-twitter#new-apis-in-edgehtml-18 "What&#x27;s new in EdgeHTML 18 - Microsoft Edge Development | Microsoft Docs")

----

## Ember.js - Ember 3.4 Released
[emberjs.com/blog/2018/10/07/ember-3-4-released.html](https://emberjs.com/blog/2018/10/07/ember-3-4-released.html "Ember.js - Ember 3.4 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 3.4リリース。
`<Tag />`のようにかぎ括弧で書けるように、Custom Component Managerの機能追加、`component#sendAction`を非推奨化など

- [Release v3.4.0 · emberjs/ember.js](https://github.com/emberjs/ember.js/releases/tag/v3.4.0 "Release v3.4.0 · emberjs/ember.js")

----

## jsdom/Changelog.md at master · jsdom/jsdom
[github.com/jsdom/jsdom/blob/master/Changelog.md#1220](https://github.com/jsdom/jsdom/blob/master/Changelog.md#1220 "jsdom/Changelog.md at master · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JSDOM 12.2.0リリース。
Shadow DOMのサポート、`Element#toggleAttribute`メソッドのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Content Security Policy Level 3におけるXSS対策 - pixiv inside
[inside.pixiv.blog/kobo/5137](https://inside.pixiv.blog/kobo/5137 "Content Security Policy Level 3におけるXSS対策 - pixiv inside")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

CSPのscript-srcとstrict-dynamicについて。
ドメインホワイトリストの問題とnonceによる実行制限について


----

## ライブラリをES2015(ES6)で書いて公開する所から始めよう | Web Scratch
[efcl.info/2015/01/09/write-es6/](https://efcl.info/2015/01/09/write-es6/ "ライブラリをES2015(ES6)で書いて公開する所から始めよう | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

Babelを使ったES2015以降のコードで書くプロジェクトのセットアップやnpmでライブラリ公開の準備などについてのチュートリアル。
よくあるJavaScriptライブラリのディレクトリ構造などについて。
Babel 7に対応する更新が行われた


----

## WebAssembly on Cloudflare Workers
[blog.cloudflare.com/webassembly-on-cloudflare-workers/](https://blog.cloudflare.com/webassembly-on-cloudflare-workers/ "WebAssembly on Cloudflare Workers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Cloudflare Worker内でWebAssemblyが動作するようになった


----

## Working with Babel 7 and Webpack | The Basement
[www.thebasement.be/working-with-babel-7-and-webpack/](https://www.thebasement.be/working-with-babel-7-and-webpack/ "Working with Babel 7 and Webpack | The Basement")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

Babel7とwebpackを使った設定方法についての解説記事。
`@babel/preset-env`の`useBuiltIns`オプションやデバッグ方法についてなど


----

## On Node Framework Popularity – hueniverse
[hueniverse.com/on-node-framework-popularity-355fbde5cbe4](https://hueniverse.com/on-node-framework-popularity-355fbde5cbe4 "On Node Framework Popularity – hueniverse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

Node.jsのサーバフレームワークアンケート結果について。
Express、Hapi、Koaなどの利用率や好み、使い続けるかについてのアンケート結果がまとめられている


----

## Calls between JavaScript and WebAssembly are finally fast 🎉 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2018/10/calls-between-javascript-and-webassembly-are-finally-fast-%F0%9F%8E%89/](https://hacks.mozilla.org/2018/10/calls-between-javascript-and-webassembly-are-finally-fast-%F0%9F%8E%89/ "Calls between JavaScript and WebAssembly are finally fast 🎉 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

Firefox WebAssemblyで関数呼び出しが改善された話とその仕組みについて。
WebAssemblyとJITの関係、WebAssemblyで最適化した関数とビルドイン関数の呼び出しの比較など


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## 本書の対象読者及び目的 - Sound for Javascripters
[ongaku-daisukikko-club.gitbook.io/music-for-javascripter/](https://ongaku-daisukikko-club.gitbook.io/music-for-javascripter/ "本書の対象読者及び目的 - Sound for Javascripters")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">book</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

Web Audio APIとMIDI Keyboardを使ってシンセサイザーを作る内容の書籍。
Codesandboxを使いながらウェブブラウザ上でコードを書いてテストを行い実行していく。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jamesseanwright/wax: An experimental, JSX-compatible renderer for the Web Audio API
[github.com/jamesseanwright/wax](https://github.com/jamesseanwright/wax "jamesseanwright/wax: An experimental, JSX-compatible renderer for the Web Audio API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web Audio APIをJSXを使って宣言的に記述できるライブラリ


----

## simov/request-compose: Composable HTTP Client
[github.com/simov/request-compose](https://github.com/simov/request-compose "simov/request-compose: Composable HTTP Client")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.js向けのComposeできるHTTPライブラリ。
関数をcomposeしてHTTPリクエストやレスポンスの処理を行える。

- [Composable HTTP Client for NodeJS - DEV Community 👩‍💻👨‍💻](https://dev.to/simov/composable-http-client-for-nodejs-83f "Composable HTTP Client for NodeJS - DEV Community 👩‍💻👨‍💻")

----

## terser-js/terser: JavaScript parser, mangler, optimizer and beautifier toolkit for ES6+
[github.com/terser-js/terser](https://github.com/terser-js/terser "terser-js/terser: JavaScript parser, mangler, optimizer and beautifier toolkit for ES6+")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

uglify-esをforkしたminifyツール。
uglify-esがメンテナンスされていないため(uglify-js自体は開発されている)、ES2015+に対応することを目的に開発されている。


----
