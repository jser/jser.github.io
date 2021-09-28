---
title: "2021-09-28のJS: Lit 2、Gatsby 4 beta、Partytown(Third-Party Script into Worker)"
author: "azu"
layout: post
date : 2021-09-27T14:10:06.442Z
category: JSer
tags:
- React
- WebComponents
- node.js
- Tools
- Chrome

---

JSer.info #559 - Web Componentsを扱うライブラリであるLit 2がリリースされました。

- [Announcing Lit 2 stable release – Lit](https://lit.dev/blog/2021-09-21-announcing-lit-2/)
- [Lit 2.0 Release Livestream - YouTube](https://www.youtube.com/watch?v=nfb779XIhsU)

Lit 2は今までLitElement 2.xとlit-html 1.xという別々のパッケージになったものを統合していて、`lit`という新しいパッケージ担っています。

classベースのDirectives API、非同期Directives、Reactive Controllersの追加されています。
要素全体に対して影響を与えられるElement expressions、タグ名などに変数を使えるStatic expressionsなども追加されています。
また、実験的にSSRのサポートなども追加されています。

LitElement 2.xとlit-html 1.xからアップグレードガイドも公開されています。

- [Upgrade guide – Lit](https://lit.dev/docs/releases/upgrade/)

----

Gatsby 4のベータ版がリリースされています。

- [Introducing Gatsby 4 | Gatsby](https://www.gatsbyjs.com/gatsby-4/)

[rendering mode](https://v4.gatsbyjs.com/docs/conceptual/rendering-options/)として、HTMLの生成を実際にアクセスするときまで遅延するDeferred Static Generation(DSG)のサポート、SSRのサポートが追加されています。

[Deferred Static Generation](https://v4.gatsbyjs.com/docs/reference/rendering-options/deferred-static-generation/)(DSG)はNext.jsの[Incremental Static Regeneration](https://nextjs.org/docs/basic-features/data-fetching#incremental-static-regeneration)(ISR)と似ていて、初回のリクエストがきた段階で始めてビルドを開始することで、めったにアクセスされないコンテンツを含むようなサイトでのデプロイにかかるビルド時間を短縮する仕組みです。
DSGではデプロイ時にデータのスナップショットを作り、リクエスト時にスナップショットからコンテンツであるHTMLを生成して返します。そのため、DSGはISRとは、リクエスト時に異なりサーバから外部リソースを再取得するのではなく、あくまでデプロイ時に作成されたスナップショットを参照してビルドするようになっています。

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">While DSG may look similar on the surface, what Gatsby does is that it takes a snapshot of the data at initial build time and creates lightweight render engines that are capable of building a page on demand. However, all data was already sourced at initial build time!</p>&mdash; Sid (@chatsidhartha) <a href="https://twitter.com/chatsidhartha/status/1442352346441281540?ref_src=twsrc%5Etfw">September 27, 2021</a></blockquote>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

その他にはparallel queryでのビルド時間の改善なども含まれています。
あわせてv3からのマイグレーションガイドも公開されています。

- [Migrating from v3 to v4 | Gatsby](https://v4.gatsbyjs.com/docs/reference/release-notes/migrating-from-v3-to-v4/)

----

PartytownはサードパーティスクリプトをWebWorkerで動かし、サードパーティスクリプトによるメインスレッドのブロッキングを避ける目的のライブラリです。

- [BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉](https://github.com/BuilderIO/partytown)

WebWorkerにはDOM APIなどがないため、そのままサードパーティスクリプトをWorkerで動かすとエラーとなります。
そのため、次のような仕組みでDOM APIなどを含むサードパーティスクリプトをWorker内で雨後しています。

1. Worker内でのDOM操作を[Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)する
2. DOM操作をコマンドにして同期XHRで通信([Worker内では同期XHRが利用](https://developer.mozilla.org/docs/Web/API/XMLHttpRequest/Synchronous_and_Asynchronous_Requests#example_synchronous_http_request_from_a_worker)できます)
3. この通信をService Workerでインターセプトしてコマンドを取得
4. コマンドを元にService Workerとメインスレッドで非同期にやりとりしてDOM操作の結果を取得
5. DOM操作の結果を元のWorkerに返す

これによって、Worker内で動作しているサードパーティスクリプトから見れば同期的にAPIを使えているように見えるため、コードの変更なしに動作しています。

詳しい仕組みについては記事も公開されているので、こちらを参照してください。

- [Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻](https://dev.to/adamdbradley/introducing-partytown-run-third-party-scripts-from-a-web-worker-2cnp)



----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Lit 2 stable release – Lit
[lit.dev/blog/2021-09-21-announcing-lit-2/](https://lit.dev/blog/2021-09-21-announcing-lit-2/ "Announcing Lit 2 stable release – Lit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Lit 2リリース。
classベースのDirectives API、非同期Directives、Reactive Controllersの追加。
要素全体に対して影響を与えられるElement expressions、タグ名などに変数を使えるStatic expressionsの追加。
また、実験的にSSRのサポートなど


----

## Node v16.10.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.10.0/](https://nodejs.org/en/blog/release/v16.10.0/ "Node v16.10.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.10.0リリース。
コネクションごとに最大のリクエスト数を制限する`server.maxRequestsPerSocket`オプションの追加。
`$HOME/.node_modules`などを探索しない`--no-global-search-paths`フラグの追加など


----

## Electron 15.0.0 | Electron
[www.electronjs.org/blog/electron-15-0/](https://www.electronjs.org/blog/electron-15-0/ "Electron 15.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 15.0.0リリース。
Electron 15から8週間ごとのメジャーアップデートとなる。
Chromium 94、Node.js 16.5.0、V8 9.4へアップデート、`nativeWindowOpen`のデフォルト値を`true`へ変更、`safeStorage` APIの追加など

- [Release electron v15.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v15.0.0 "Release electron v15.0.0 · electron/electron")
- [safeStorage | Electron](https://www.electronjs.org/docs/latest/api/safe-storage/ "safeStorage | Electron")

----

## Chromium Blog: Chrome 95 Beta: Secure Payment Confirmation, WebAssembly Exception Handling and More
[blog.chromium.org/2021/09/chrome-95-beta-secure-payment.html](https://blog.chromium.org/2021/09/chrome-95-beta-secure-payment.html "Chromium Blog: Chrome 95 Beta: Secure Payment Confirmation, WebAssembly Exception Handling and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 95 betaリリース。
Origin TrialとしてAccess HandleをFile System Access APIに追加。
Performance Observerに`droppedEntriesCount`の追加、EyeDropper APIの追加、`self.reportError()`の追加、`URLPattern`の追加など。
また、FTP URLのサポート終了、数字で終わるIPv4アドレスではないホスト名のサポートを廃止など


----

## Miniflare is now an official part of the Workers ecosystem 🎉 · cloudflare/miniflare@e1cb97f
[github.com/cloudflare/miniflare/commit/e1cb97f9891b2818f4be5715ee467668a39f7f80](https://github.com/cloudflare/miniflare/commit/e1cb97f9891b2818f4be5715ee467668a39f7f80 "Miniflare is now an official part of the Workers ecosystem 🎉 · cloudflare/miniflare@e1cb97f")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span> <span class="jser-tag">testing</span></p>

Cloudflare WorkersのsimulatorであるMiniflareがCloudflare公式となった


----

## es-module-shims/CHANGELOG.md at 1.0.0 · guybedford/es-module-shims
[github.com/guybedford/es-module-shims/blob/1.0.0/CHANGELOG.md](https://github.com/guybedford/es-module-shims/blob/1.0.0/CHANGELOG.md "es-module-shims/CHANGELOG.md at 1.0.0 · guybedford/es-module-shims")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

ES Module Shims 1.0.0リリース。
lexerがWasmを利用していたため`unsafe-eval`のCSP設定が必要となっていたが、asm.jsビルドを使いデフォルトでCSPに対応した。
また、パフォーマンスについてはほぼ同等で、Safariに関してはasm.js版の方が早くなっている。

- [feat: make the CSP asm.js build the main entry by guybedford · Pull Request #193 · guybedford/es-module-shims](https://github.com/guybedford/es-module-shims/pull/193 "feat: make the CSP asm.js build the main entry by guybedford · Pull Request #193 · guybedford/es-module-shims")
- [feat: asm.js build by guybedford · Pull Request #86 · guybedford/es-module-lexer](https://github.com/guybedford/es-module-lexer/pull/86 "feat: asm.js build by guybedford · Pull Request #86 · guybedford/es-module-lexer")
- [content-security-policy/CSP.md at master · WebAssembly/content-security-policy](https://github.com/WebAssembly/content-security-policy/blob/master/proposals/CSP.md "content-security-policy/CSP.md at master · WebAssembly/content-security-policy")

----

## Manifest V2 support timeline - Chrome Developers
[developer.chrome.com/docs/extensions/mv3/mv2-sunset/](https://developer.chrome.com/docs/extensions/mv3/mv2-sunset/ "Manifest V2 support timeline - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span> <span class="jser-tag">news</span></p>

Chrome拡張のmanifest v3のロードマップ。
2022年1月17日に新しくmanifest v2の拡張は申請できなくなる。
2023年1月に既存のv2拡張は更新もできなくなる。


----

## ESLint v8.0.0-rc.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2021/09/eslint-v8.0.0-rc.0-released](https://eslint.org/blog/2021/09/eslint-v8.0.0-rc.0-released "ESLint v8.0.0-rc.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.0.0-rc.0リリース。

- [Migrating to v8.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/docs/8.0.0/user-guide/migrating-to-8.0.0 "Migrating to v8.0.0 - ESLint - Pluggable JavaScript linter")

----

## Stimulus 3
[world.hey.com/hotwired/stimulus-3-c438d432](https://world.hey.com/hotwired/stimulus-3-c438d432 "Stimulus 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rails</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Stimulus 3 リリース。
パッケージ名が`stimulus`から`@hotwired/stimulus`へと変更された。
Action Parametersのサポート、デフォルト値のサポート、`debug`オプションの追加など

- [Comparing v2.0.0...v3.0.0 · hotwired/stimulus](https://github.com/hotwired/stimulus/compare/v2.0.0...v3.0.0 "Comparing v2.0.0...v3.0.0 · hotwired/stimulus")

----

## Introducing Gatsby 4 | Gatsby
[www.gatsbyjs.com/gatsby-4/](https://www.gatsbyjs.com/gatsby-4/ "Introducing Gatsby 4 | Gatsby")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Gatsby 4ベータリリース。
HTMLの生成を実際にアクセスするときまで遅延するDeferred Static Generation(DSG)のサポート、SSRのサポート、parallel queryでのビルド時間の改善など

- [Matteo Frana on Twitter: &amp;quot;@chatsidhartha Can you explain me briefly the differences between Gatsby DSG and ISR? Thank you! I&#039;m looking forward to testing Gatsby 4.&amp;quot; / Twitter](https://twitter.com/matfrana/status/1442225069158248449 "Matteo Frana on Twitter: &amp;amp;quot;@chatsidhartha Can you explain me briefly the differences between Gatsby DSG and ISR? Thank you! I&amp;#039;m looking forward to testing Gatsby 4.&amp;amp;quot; / Twitter")
- [Run Gatsby 4 with DSG and SSR on Netlify today | Netlify](https://www.netlify.com/blog/2021/09/16/run-gatsby-4-with-dsg-and-ssr-on-netlify-today/ "Run Gatsby 4 with DSG and SSR on Netlify today | Netlify")

----
<h1 class="site-genre">アーティクル</h1>

----

## Blazor Developers Can Now Create Custom Elements, Render Components from JavaScript -- Visual Studio Magazine
[visualstudiomagazine.com/articles/2021/09/16/aspnet-core-updates.aspx](https://visualstudiomagazine.com/articles/2021/09/16/aspnet-core-updates.aspx "Blazor Developers Can Now Create Custom Elements, Render Components from JavaScript -- Visual Studio Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">.net</span> <span class="jser-tag">C#</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span></p>

.NET 6 RC1でBlazorがCustom Elementをサポートし、BlazorコンポーネントをCustom Elementとして利用できるようになった。

- [Announcing .NET 6 Release Candidate 1 - .NET Blog](https://devblogs.microsoft.com/dotnet/announcing-net-6-release-candidate-1/ "Announcing .NET 6 Release Candidate 1 - .NET Blog")
- [AspLabs/src/BlazorCustomElements at main · aspnet/AspLabs](https://github.com/aspnet/AspLabs/tree/main/src/BlazorCustomElements "AspLabs/src/BlazorCustomElements at main · aspnet/AspLabs")

----

## Fullstack app with TypeScript, Next.js, Prisma &amp; GraphQL
[www.prisma.io/blog/fullstack-nextjs-graphql-prisma-oklidw1rhw](https://www.prisma.io/blog/fullstack-nextjs-graphql-prisma-oklidw1rhw "Fullstack app with TypeScript, Next.js, Prisma &amp; GraphQL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span> <span class="jser-tag">prisma</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">GraphQL</span></p>

Next.js/Prisma/GraphQLを使ったアプリケーション開発についてのチュートリアル。


----

## What&#039;s new in React 18? | Yagmur Cetin Tas
[yagmurcetintas.com/journal/whats-new-in-react-18](https://yagmurcetintas.com/journal/whats-new-in-react-18 "What&#039;s new in React 18? | Yagmur Cetin Tas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18で予定されている変更の概要をまとめた記事


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Get Your Head Straight - Speaker Deck
[speakerdeck.com/csswizardry/get-your-head-straight](https://speakerdeck.com/csswizardry/get-your-head-straight "Get Your Head Straight - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">slide</span> <span class="jser-tag">CSS</span></p>

パフォーマンスの問題を見つけるために`<head>`の中身を表示するct.cssについてのスライド。
`<script>`や`<style>`について3rd partyであるかやブロッキングしてるかなどを可視化してくれる

- [🧠 ct.css – Let’s take a look inside your &lt;head&gt;](https://csswizardry.com/ct/ "🧠 ct.css – Let’s take a look inside your &amp;lt;head&amp;gt;")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## vite/packages/plugin-react at main · vitejs/vite
[github.com/vitejs/vite/tree/main/packages/plugin-react](https://github.com/vitejs/vite/tree/main/packages/plugin-react "vite/packages/plugin-react at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">vite</span> <span class="jser-tag">plugin</span></p>

ViteのReact Plugin。
`@vitejs/plugin-react-refresh`を置き換えるプラグイン


----

## BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉
[github.com/BuilderIO/partytown](https://github.com/BuilderIO/partytown "BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

サードパーティスクリプトをWorker内で動かしてメインスレッドのブロッキングを防ぐライブラリ。
Worker内でのDOM操作をProxyして、同期XHRで通信し、その通信をService Workerでインターセプトしてメインスレッドと非同期でやり取りした結果をWorkerに返している。

- [Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻](https://dev.to/adamdbradley/introducing-partytown-run-third-party-scripts-from-a-web-worker-2cnp "Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## gvergnaud/ts-pattern: 🎨 The exhaustive Pattern Matching library for TypeScript, with smart type inference.
[github.com/gvergnaud/ts-pattern](https://github.com/gvergnaud/ts-pattern "gvergnaud/ts-pattern: 🎨 The exhaustive Pattern Matching library for TypeScript, with smart type inference.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScriptでのパターンマッチライブラリ


----

## cesanta/elk: A low footprint JavaScript engine for embedded systems
[github.com/cesanta/elk](https://github.com/cesanta/elk "cesanta/elk: A low footprint JavaScript engine for embedded systems")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

組み込み向けの小さなJavaScriptエンジン


----
