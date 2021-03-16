---
title: "2021-03-16のJS: Safari Technology Preview 122、React Native 0.64、SvelteKit"
author: "azu"
layout: post
date : 2021-03-15T23:42:20.954Z
category: JSer
tags:
- Tools
- debug
- Chrome
- CSS
- React

---

JSer.info #531 - Safari Technology Preview 122がリリースされました。

- [Release Notes for Safari Technology Preview 122 | WebKit](https://webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/)

Safari Technology Preview 122では色々な機能が実装されています。
実験フラグ付きでCSS `:focus-visible`とCSS Color 5の`color-mix()`/`color-contrast()`/[Relative color syntax](https://drafts.csswg.org/css-color-5/#relative-colors)が実装されています。
ES Proposal Stage 3の[Private method](https://github.com/tc39/proposal-private-methods)、[Static private methods](https://github.com/tc39/proposal-static-class-features)、[Top-Level await](https://github.com/tc39/proposal-top-level-await)、[RegExp Match Indices](https://github.com/tc39/proposal-regexp-match-indices)のサポート。
Web WorkerとService Workerで`type: module`をサポート、Paint Timingの(再)有効化なども含まれます。

- [Threading the web with module workers](https://web.dev/module-workers/)
- [Chrome 80 から Web Worker (Dedicated Worker) で ES Modules が使えます](https://nhiroki.jp/2019/12/05/es-modules-for-dedicated-workers)

Safariとは直接関係しませんが、2021年6月ごろにリリースされる予定のECMAScript 2021のリリース候補も公開されています。

- [Release ES2021 Candidate March 2021 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03)
- [ECMAScript 2021: the final feature set](https://2ality.com/2020/09/ecmascript-2021.html)

---

SveleteKitのソースコードが公開されています。
SveleteKitはSvelteベースのNext.jsライクなフレームワークであった[Sapper](https://sapper.svelte.dev/)を置き換える目的で作られています。

- [sveltejs/kit: A monorepo for SvelteKit and friends](https://github.com/sveltejs/kit)

まだソースコードの公開だけでリリースはされていません。
[What is SvelteKit? | SK Incognito](https://sk-incognito.vercel.app/learn/what-is-sveltekit)というチュートリアルサイトでは、SvelteKitがどのようなものか紹介されているので、興味がある人は見てみるといいかもしれません。

---

React Native 0.64がリリースされました。

- [Announcing React Native 0.64 with Hermes on iOS · React Native](https://reactnative.dev/blog/2021/03/12/version-0.64)

AOTによる事前コンパイルでfootprintを最適化してアプリの起動速度などを改善する目的である[Hermes JS Engine](https://github.com/facebook/hermes)がiOSでも利用可能になっています。
また、HermesにES2015の[Proxy object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)のサポートが追加されています。
その他には、MetroでInline Requiresがデフォルトで有効化、[React 17](https://reactjs.org/blog/2020/10/20/react-v17.html)へアップデートなどが含まれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v0.9.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.9.0](https://github.com/evanw/esbuild/releases/tag/v0.9.0 "Release v0.9.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">relre</span></p>

esbuild 0.9.0リリース。
package.jsonの`exports`フィールドのサポート、`esbuild.startService()` APIの削除、bannerとfooterを言語ごとに指定できるように


----

## Release Notes for Safari Technology Preview 122 | WebKit
[webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/](https://webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/ "Release Notes for Safari Technology Preview 122 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 122リリース。
実験フラグ付きでCSS `:focus-visible`とCSS Color 5の実装を追加。
ES ProposalのPrivate method、Top-Level await、RegExp Match Indicesのサポート。
Workerで`type: module`をサポート、Paint Timingの有効化など


----

## Chromium Blog: Chrome 90 Beta: AV1 Encoder for WebRTC, New Origin Trials, and More
[blog.chromium.org/2021/03/chrome-90-beta-av1-encoder-for-webrtc.html](https://blog.chromium.org/2021/03/chrome-90-beta-av1-encoder-for-webrtc.html "Chromium Blog: Chrome 90 Beta: AV1 Encoder for WebRTC, New Origin Trials, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 90 Betaリリース。
AV1 Encoderのサポート。
Origin Trialとして`getCurrentBrowsingContextMedia()`、Breakout Box、WebAssembly Exception Handlingのサポート。
CSSの`aspect-ratio`とwidthかheightが指定されているときに推論されるように、`:state`、`overflow: clip`のサポート。
Feature-Policyに代わるPermissions-Policy、`StaticRange`のサポートなど。
`navigator.plugins`と`navigator.mimeTypes`が空要素を返すようになるなど


----

## Announcing React Native 0.64 with Hermes on iOS · React Native
[reactnative.dev/blog/2021/03/12/version-0.64](https://reactnative.dev/blog/2021/03/12/version-0.64 "Announcing React Native 0.64 with Hermes on iOS · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.64リリース。
iOSでもJSエンジンのHermesを利用可能に、MetroでInline Requiresがデフォルトで有効化、HermesがES Proxyのサポート、React 17へアップデートなど


----

## sveltejs/kit: A monorepo for SvelteKit and friends
[github.com/sveltejs/kit](https://github.com/sveltejs/kit "sveltejs/kit: A monorepo for SvelteKit and friends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span></p>

SvelteKitのソースコードが公開された


----

## Release ES2021 Candidate March 2021 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03](https://github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03 "Release ES2021 Candidate March 2021 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2021のリリース候補が公開された。ECMAScript 2021に入る予定の機能は決定され仕様もフリーズされたため、masterブランチはES 2022となった

- [ECMAScript 2021: the final feature set](https://2ality.com/2020/09/ecmascript-2021.html "ECMAScript 2021: the final feature set")
- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

----

## Socket.IO 4.0.0 | Socket.IO
[socket.io/blog/socket-io-4-release/](https://socket.io/blog/socket-io-4-release/ "Socket.IO 4.0.0 | Socket.IO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Socket.IO 4.0.0リリース。
破壊的な変更としてサーバ側の`io.to()`がimmutableに変更、protocolは互換性を維持している。
`pingTimeout`のデフォルト値を5秒から20秒へ変更、Utilityメソッドの追加、`autoUnref`オプションの追加など

- [Migrating from 3.x to 4.0 | Socket.IO](https://socket.io/docs/v3/migrating-from-3-x-to-4-0/ "Migrating from 3.x to 4.0 | Socket.IO")
- [fix: set default protocol version to 3 to allow backward compatibilit… by simonemazzoni · Pull Request #616 · socketio/engine.io](https://github.com/socketio/engine.io/pull/616 "fix: set default protocol version to 3 to allow backward compatibilit… by simonemazzoni · Pull Request #616 · socketio/engine.io")

----
<h1 class="site-genre">アーティクル</h1>

----

## Debugging layout shifts
[web.dev/debugging-layout-shifts/](https://web.dev/debugging-layout-shifts/ "Debugging layout shifts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Layout Instability APIでのCumulative Layout Shift (CLS)の計測とCLSの特定とデバッグ方法について


----

## Digging Into CSS Logical Properties
[ishadeed.com/article/css-logical-properties/](https://ishadeed.com/article/css-logical-properties/ "Digging Into CSS Logical Properties")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

RTLに対応したCSSの書き方と`margin-inline-end`について。


----

## レシピサービスのフロントエンドに CSS in JS を採用した話 - クックパッド開発者ブログ
[techlife.cookpad.com/entry/2021/03/15/090000](https://techlife.cookpad.com/entry/2021/03/15/090000 "レシピサービスのフロントエンドに CSS in JS を採用した話 - クックパッド開発者ブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

emotionを使ったCSS-in-JSについて。
styled-componentsの記法ではなくString Stylesを採用した理由、stylelintを使ったLint、Jestを使ったスナップショットテストについてなど


----

## JavaScript: What is the meaning of this?
[web.dev/javascript-this/](https://web.dev/javascript-this/ "JavaScript: What is the meaning of this?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

いろいろなケースの`this`の意味について解説している記事

- [関数とthis · JavaScript Primer #jsprimer](https://jsprimer.net/basic/function-this/ "関数とthis · JavaScript Primer #jsprimer")

----

## Beyond Console.log() – Level up Your Debugging Skills - SitePoint
[www.sitepoint.com/beyond-console-log-level-up-your-debugging-skills/](https://www.sitepoint.com/beyond-console-log-level-up-your-debugging-skills/ "Beyond Console.log() – Level up Your Debugging Skills - SitePoint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">console</span> <span class="jser-tag">debug</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">Chrome</span></p>

Console APIやChrome DevToolsを使ったデバッグについての記事。
ログフォーマット、Console APIの紹介、Dev Tools上で使える関数、Overrides、VScodeとの連携についてなど


----

## The Death of a Node.js Process - Thomas Hunter II
[thomashunter.name/posts/2021-03-08-the-death-of-a-nodejs-process](https://thomashunter.name/posts/2021-03-08-the-death-of-a-nodejs-process "The Death of a Node.js Process - Thomas Hunter II")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsにおけるプロセス終了とエラーについて。
uncaughtException、unhandledRejectionでのエラーのキャッチと`process.exit`でのプロセス終了方法。
また、Signalとそれをハンドリングできるかどうかについてのまとめ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Post-Spectre Web Development
[w3c.github.io/webappsec-post-spectre-webdev/](https://w3c.github.io/webappsec-post-spectre-webdev/ "Post-Spectre Web Development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

Spectre以後のウェブ開発における脅威モデルと戦略についてのドキュメント。
Isolation、サブリソース、クロスオリジンを意図した操作についてなど


----

## What is SvelteKit? | SK Incognito
[sk-incognito.vercel.app/learn/what-is-sveltekit](https://sk-incognito.vercel.app/learn/what-is-sveltekit "What is SvelteKit? | SK Incognito")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">tutorial</span></p>

SvelteKitのチュートリアルサイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Cloud9c/taro: A lightweight 3D game engine for the web.
[github.com/Cloud9c/taro](https://github.com/Cloud9c/taro "Cloud9c/taro: A lightweight 3D game engine for the web.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">3D</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

three.jsとcannon-esを使った3Dゲームエンジンライブラリ


----

## rsms/estrella: Lightweight and versatile build tool based on the esbuild compiler
[github.com/rsms/estrella](https://github.com/rsms/estrella "rsms/estrella: Lightweight and versatile build tool based on the esbuild compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">bundler</span></p>

esbuildとtscのラッパーツール。
esbuildでビルドしながら、tscでの型チェックを同時に実行できるビルドツール

- [Through the pipeline: An exploration of front-end bundlers - DEV Community 👩‍💻👨‍💻](https://dev.to/walpolea/through-the-pipeline-an-exploration-of-front-end-bundlers-ea1 "Through the pipeline: An exploration of front-end bundlers - DEV Community 👩‍💻👨‍💻")

----
