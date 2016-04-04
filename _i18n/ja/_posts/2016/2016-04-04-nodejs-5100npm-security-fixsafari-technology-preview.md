---
title: "2016-04-04のJS: Node.js 5.10.0、npm security fix、Safari Technology Preview"
author: azu
layout: post
date : 2016-04-04T19:46
category: JSer
tags:
    - Node.js
    - npm
    - security
    - safari

---

JSer.info #273 - [Node v5.10.0 (Stable)](https://nodejs.org/en/blog/release/v5.10.0/ "Node v5.10.0 (Stable)")がリリースされました。

後述する[npm](https://www.npmjs.com/ "npm")のセキュリティ的な問題の修正がされたバージョンも含まれています。

[2016-03-17のJS](http://jser.info/2016/03/17/react-webassembly-art-of-javascript/ "2016-03-17のJS")でも紹介していましたが、Node.js v6ではBuffer APIの変更が予定されています。

- [Node.js Buffer API Changes — Medium](https://medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97#.qk7fmic6y "Node.js Buffer API Changes — Medium")

このAPIの変更と`--zero-fill-buffers`コマンドラインオプションが、Node.js 5.10.0にもバックポートされています。

また、主にNW.jsやElectron環境向けだと思いますが、`--no-browser-globals`フラグで、
以下のようなブラウザにグローバルとの互換APIを露出させないオプションが追加されいます。

    setTimeout, clearTimeout, setInterval, clearInterval, setImmediate, clearImmediate
    console

----

[The npm Blog — fixing a bearer token vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")では`npm < 2.15.1` or `npm < 3.8.3`にあった脆弱性について解説されています。

npmのCLIで発生したリクエストにて、registry以外にもtoken情報を送信していたという問題で、[既存のtokenはこちらから取り消せます](https://www.npmjs.com/settings/tokens)。

- [npm security updates v2.15.1 and v3.8.3 | Node.js](http://nodejs.org/en/blog/vulnerability/npm-tokens-leak-march-2016/ "npm security updates v2.15.1 and v3.8.3 | Node.js")
- 該当コミット: [config: only send token to registry hosts · npm/npm@f67ecad](https://github.com/npm/npm/commit/f67ecad59e99a03e5aad8e93cd1a086ae087cb29 "config: only send token to registry hosts · npm/npm@f67ecad")

npm 2.xと3.x それぞれアップデートされています。
Node.js自体のアップデート または `npm i -g npm`でアップデートする必要があります。

Windowsの場合は[npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade "npm-windows-upgrade")を使うことで`npm i -g npm`と同様のことが行えます。

npmは[AzerのKik問題](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm "Azer")を受けて、色々な変更や改善を最近行っているので合わせてチェックするとよいかと思います。

簡単にまとめると

- [npm registry is now fully HTTPS!](http://blog.npmjs.org/post/142077474335/npm-registry-is-now-fully-https "The npm Blog — npm registry is now fully HTTPS!")
  - registryの完全HTTPS化
- [changes to npm’s unpublish policy](http://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy "The npm Blog — changes to npm’s unpublish policy")
  - `npm unpublish`ポリシーの変更
  - publishして24時間以内なら、今まで通り`npm unpublish`できる。
  - それ以降は`support@npmjs.com`へ連絡が必要
- 完全にunpublish(remove)されたモジュールは[Security holding package](https://github.com/npm/security-holder "Security holding package")に置き換えるように変更
  - パッケージの名前空間の乗っとり防止の対策
- [Package install scripts vulnerability](http://blog.npmjs.org/post/141702881055/package-install-scripts-vulnerability "The npm Blog — Package install scripts vulnerability")
  - `npm install <module>`した際に`postinstall`で任意のスクリプトが実行できる問題と対策
  - [npm install scriptの脆弱性とオープンソースと信頼 - teppeis blog](http://teppeis.hatenablog.com/entry/2016/03/npm-vulnerability-and-open-source-trust "npm install scriptの脆弱性とオープンソースと信頼 - teppeis blog")

----

Safari Technology Previewが公開されています。
2週間ごとに更新される開発者向けのバージョンで、[Firefox Developer Edition](https://www.mozilla.org/ja/firefox/developer/ "Firefox Developer Edition — Mozilla")やChromeのDev Channelのような感じです。

- [Introducing Safari Technology Preview | WebKit](https://webkit.org/blog/6017/introducing-safari-technology-preview/ "Introducing Safari Technology Preview | WebKit")

Safari Technology Previewで問題を見つけたら、BugzillaやBug Reporterを使ってバグ報告することができます。

- [Fetch polyfill not working with Safari Technology Preview · Issue #303 · github/fetch](https://github.com/github/fetch/issues/303 "Fetch polyfill not working with Safari Technology Preview · Issue #303 · github/fetch")
- [azu/browser-javascript-resource: Browser JavaScript Resource.](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource: Browser JavaScript Resource.")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v5.10.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.10.0/](https://nodejs.org/en/blog/release/v5.10.0/ "Node v5.10.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.10.0リリース。
npmのセキュリティアップデートしたバージョンが含まれている。
また、`Buffer(size)`のallocation問題に対して`Buffer.alloc`/`Buffer.allocUnsafe`/`Buffer.from`と`--zero-fill-buffers`コマンドライン引数の追加など

- [The npm Blog — fixing a bearer token vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")
- [Node.js Buffer API Changes | Linux.com](https://www.linux.com/news/software/applications/893109-nodejs-buffer-api-changes "Node.js Buffer API Changes | Linux.com")

----

## Introducing Safari Technology Preview | WebKit
[webkit.org/blog/6017/introducing-safari-technology-preview/](https://webkit.org/blog/6017/introducing-safari-technology-preview/ "Introducing Safari Technology Preview | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span></p>

Safariの開発者プレビュー版が公開された

----

## Pixi.JS v4 Arrives - Goodboy™ — Goodboy™
[www.goodboydigital.com/pixi-js-v4/](http://www.goodboydigital.com/pixi-js-v4/ "Pixi.JS v4 Arrives - Goodboy™ — Goodboy™")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">game</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

PixiJS v4 RCリリース。
pixi-gl-coreというWebGL部分のコア実装を分離、RenderTextureのGCを任意のタイミングで走らせることが出来るように

- [pixijs/pixi-gl-core: A set of tidy little pixi objects that make working with webGL simpler (WIP, will be moved to pixi group when ready)](https://github.com/pixijs/pixi-gl-core "pixijs/pixi-gl-core: A set of tidy little pixi objects that make working with webGL simpler (WIP, will be moved to pixi group when ready)")

----
<h1 class="site-genre">アーティクル</h1>

----

## The npm Blog — fixing a bearer token vulnerability
[blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

npmにMITMできる脆弱性があったため2.xと3.xそれぞれセキュリティアップデートされている。
`npm i -g`または`npm-windows-upgrade`を使うことで`npm`自体をアップデートできる

- [felixrieseberg/npm-windows-upgrade: Upgrade npm on Windows](https://github.com/felixrieseberg/npm-windows-upgrade "felixrieseberg/npm-windows-upgrade: Upgrade npm on Windows")

----

## Webpack 2 Tree Shaking Configuration — Modus Create: Front End Development — Medium
[medium.com/modus-create-front-end-development/webpack-2-tree-shaking-configuration-9f1de90f3233](https://medium.com/modus-create-front-end-development/webpack-2-tree-shaking-configuration-9f1de90f3233 "Webpack 2 Tree Shaking Configuration — Modus Create: Front End Development — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack 1から2へのマイグレーションについて

----

## React vs Angular2: The fight rages on – Evojam Technology Blog
[tech.evojam.com/2016/03/31/react-vs-angular2-the-fight-rages-on/](http://tech.evojam.com/2016/03/31/react-vs-angular2-the-fight-rages-on/ "React vs Angular2: The fight rages on – Evojam Technology Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">AngularJS</span></p>

ReactとAngularJS 2の比較

----

## Houdini: Maybe The Most Exciting Development In CSS You&#x27;ve Never Heard Of – Smashing Magazine
[www.smashingmagazine.com/2016/03/houdini-maybe-the-most-exciting-development-in-css-youve-never-heard-of/](https://www.smashingmagazine.com/2016/03/houdini-maybe-the-most-exciting-development-in-css-youve-never-heard-of/ "Houdini: Maybe The Most Exciting Development In CSS You've Never Heard Of – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

W3C task forceのHoudiniは何を解決するのが目的でどういうものなのかについての解説。

----

## The JavaScript Event Loop: Explained
[blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/](http://blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/ "The JavaScript Event Loop: Explained")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScriptのイベントループについての解説、図解。
DOM EventやWebWorkerについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## What&#x27;s New in TypeScript? | Build 2016 | Channel 9
[channel9.msdn.com/Events/Build/2016/B881](https://channel9.msdn.com/Events/Build/2016/B881 "What's New in TypeScript? | Build 2016 | Channel 9")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">動画 </span></p>

近年のTypeScriptのリリースについて。
またnon-nullable typeやnpmとd.tsについてなど

----

## Let&#x27;s Learn ES6 - YouTube
[www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX](https://www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX "Let's Learn ES6 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">動画 </span></p>

ES6について学ぶスクリーンキャストの連載

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## buzinas/tslint-eslint-rules: Improve your TSLint with the missing ESLint rules
[github.com/buzinas/tslint-eslint-rules](https://github.com/buzinas/tslint-eslint-rules "buzinas/tslint-eslint-rules: Improve your TSLint with the missing ESLint rules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

TSLint向けのESLintルール

----

## aadsm/jschardet: Character encoding auto-detection in JavaScript (port of python&#x27;s chardet)
[github.com/aadsm/jschardet](https://github.com/aadsm/jschardet "aadsm/jschardet: Character encoding auto-detection in JavaScript (port of python's chardet)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">文字コード</span></p>

JavaScriptで文字コード判定をするライブラリ

----

## rbuckton/prex: Async coordination primitives and extensions on top of ES6 Promises
[github.com/rbuckton/prex](https://github.com/rbuckton/prex "rbuckton/prex: Async coordination primitives and extensions on top of ES6 Promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promise周りの補助ライブラリ。
Cancellation、Semaphore、SchedulingのAPIを提供してる

----

## LiquidLabsGmbH/retractor: Expose react internals for E2E testing
[github.com/LiquidLabsGmbH/retractor](https://github.com/LiquidLabsGmbH/retractor "LiquidLabsGmbH/retractor: Expose react internals for E2E testing")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">React</span></p>

selenium-webderiverにReact Elementoを受け取れる`findElement`を拡張するライブラリ

----

## bfred-it/object-fit-images: Adds support to object-fit to images on IE9, IE10, IE11, Edge and other old browsers.
[github.com/bfred-it/object-fit-images](https://github.com/bfred-it/object-fit-images "bfred-it/object-fit-images: Adds support to object-fit to images on IE9, IE10, IE11, Edge and other old browsers.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

`object-fit`をIEでも動かすJavaScriptライブラリ

----

## thejameskyle/the-super-tiny-compiler: Possibly the smallest compiler ever
[github.com/thejameskyle/the-super-tiny-compiler](https://github.com/thejameskyle/the-super-tiny-compiler "thejameskyle/the-super-tiny-compiler: Possibly the smallest compiler ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

JavaScriptで書かれた小さなCompiler/Transpilerの実装。
コメントがしっかり付けられているのでコンパイルの作りについての学習する向け

----

## gajus/create-index: Creates ES6 ./index.js file in target directories that imports and exports all sibling files and directories.
[github.com/gajus/create-index](https://github.com/gajus/create-index "gajus/create-index: Creates ES6 ./index.js file in target directories that imports and exports all sibling files and directories.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

ディレクトリを指定すると、そこにあるモジュールを`import`した`index.js`を作成してくれるツール

----

## Babel Starter Kit ∙ A project template for authoring and publishing JavaScript libraries
[www.kriasoft.com/babel-starter-kit/](https://www.kriasoft.com/babel-starter-kit/ "Babel Starter Kit ∙ A project template for authoring and publishing JavaScript libraries")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Babelを使ったStarter Kit

----
<h1 class="site-genre">書籍関係</h1>

----

## ECSS: Home Page
[ecss.io/](http://ecss.io/ "ECSS: Home Page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

ECSS(Enduring CSS)についての書籍
CSSの設計、考え方について扱ってる

- [Enduring CSS: writing style sheets for rapidly changing, long-lived projects – Ben Frain](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/ "Enduring CSS: writing style sheets for rapidly changing, long-lived projects – Ben Frain")

----
