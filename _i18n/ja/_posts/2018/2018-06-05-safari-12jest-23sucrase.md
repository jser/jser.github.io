---
title: "2018-06-05のJS: Safari 12の変更予定、Jest 23、sucrase"
author: "azu"
layout: post
date : 2018-06-05T00:34:04.007Z
category: JSer
tags:
- safari
- jest
- babel
- transpiler

---

JSer.info #386 - iOS 12、macOS 10.14に搭載予定のSafari 12の変更予定のリリースノートが公開されています。

- [What’s New in Safari - Apple Developer](https://developer.apple.com/safari/whats-new/)

`font-display`のサポート、[Intelligent Tracking Prevention 2.0](https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/)、[Cross-Origin Read Blocking (CORB)](https://chromium.googlesource.com/chromium/src/+/master/services/network/cross_origin_read_blocking_explainer.md)の一部をサポート、またPassword AutoFillに関する機能が追加されています。

少し前にリリースされた[Safari Technology Preview 57](https://webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/)でも`Cross-Origin-Options` HTTP response headerというクロスオリジンに関するセキュリティヘッダが試験的に実装されています。

- [Safari TP 57のCross-Origin-Options HTTP response headerについて](https://gist.github.com/azu/842e5d8d9fe1767dfbbd4238e7a19fad)

----

JavaScriptテストフレームワークのJest 23がリリースされました。

- [Jest 23: 🔥 Blazing Fast Delightful Testing · Jest](https://facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html)

Interactive Snapshot Modeの追加、非同期なカスタムmatcherを作成できるように、`jest-each`がコアに同梱、`toStrictEqual`などのmatcherの追加が行われています。

また、テストがハングした際のデバッグを補助する[--detectOpenHandles](https://facebook.github.io/jest/docs/en/cli.html#detectopenhandles)オプションが追加されています。

----

[sucrase](https://github.com/alangpierce/sucrase)というTypeScript、Flow、JSXと一部のES.nextの機能の変換に限定したTranspilerが公開されています。Babelとは異なりES2015+をES5へ変換するのではなく、ES2015+がそのまま実行できる環境向けにモジュールやTypeScript、Flow、JSXなどを高速にJavaScriptへ変換することが目的となっています。

- website: <https://sucrase.io/>

Babelのパーサをforkしたものを利用していて、TypeScriptなども[@babel/preset-typescript](https://github.com/babel/babel/tree/master/packages/babel-preset-typescript)のように型情報を外してJavaScriptに変換できます。
（型チェックはおこないません）

[Motivation](https://github.com/alangpierce/sucrase#motivation)にも書かれているように、Babelとは異なりASTまでは生成せずtokenレベルでのコード変換を行います。
そのため、BabelのようなASTプラグインはサポートしていませんが、変換ステップが少なくなるため高速な変換を行えます。

- Babel: Source -> Token -> AST -> Transform -> AST -> Source
- sucrase: Source -> Token -> Transform -> Source

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Chrome 67  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/nic67](https://developers.google.com/web/updates/2018/05/nic67 "New in Chrome 67  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 67リリース。
Desktop PWA、Generic Sensor API、`BigInt`のサポート、開発者ツールの更新など


----

## Announcing TypeScript 2.9 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/05/31/announcing-typescript-2-9/](https://blogs.msdn.microsoft.com/typescript/2018/05/31/announcing-typescript-2-9/ "Announcing TypeScript 2.9 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.9リリース。
`import()` typeの追加、JSONファイルをimportしたときに型推論がされるように、Tagged Template Stringの型改善など

- [TypeScript 2.9 変更点 - Qiita](https://qiita.com/utatti/items/9f6c60f11620f7df50c0 "TypeScript 2.9 変更点 - Qiita")
- [TypeScript 2.9.1 変更点 - Qiita](https://qiita.com/vvakame/items/0b22e5e34023e4c5d074 "TypeScript 2.9.1 変更点 - Qiita")

----

## Release 1.0.0-beta.5 · avajs/ava
[github.com/avajs/ava/releases/tag/v1.0.0-beta.5](https://github.com/avajs/ava/releases/tag/v1.0.0-beta.5 "Release 1.0.0-beta.5 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 1.0.0-beta.5リリース。
`ava.config.js`の設定ファイルのサポート、`t.throws`で`code`プロパティをサポートなど


----

## Release 8.6 “Follow Reason” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/8.6.0](https://github.com/postcss/autoprefixer/releases/tag/8.6.0 "Release 8.6 “Follow Reason” · postcss/autoprefixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Autoprefixer 8.6リリース。
CSS Gridの`gap`をサポートなど


----

## Release Notes for Safari Technology Preview 57 | WebKit
[webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/](https://webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/ "Release Notes for Safari Technology Preview 57 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 57リリース。
クロスオリジンWindow間でのアクセスを制限できる`Cross-Origin-Options` HTTPヘッダの試験的サポート、modern EME APIをデフォルトで有効化など。


----

## Jest 23: 🔥 Blazing Fast Delightful Testing · Jest
[facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html](https://facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html "Jest 23: 🔥 Blazing Fast Delightful Testing · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 23リリース。
Interactive Snapshot Modeの追加、非同期なカスタムmatcherを作成できるように、`jest-each`がコアに同梱、`toStrictEqual`などのmatcherの追加


----

## What’s New in Safari - Apple Developer
[developer.apple.com/safari/whats-new/](https://developer.apple.com/safari/whats-new/ "What’s New in Safari - Apple Developer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 12の変更予定。
watchOSで動作するように、`font-display`のサポート、ITP 2.0、CORBの一部をサポート、`.safariextz`スタイルのSafari拡張を非推奨化など


----
<h1 class="site-genre">アーティクル</h1>

----

## Simplify Web Worker code with Comlink
[davidea.st/articles/comlink-simple-web-worker](https://davidea.st/articles/comlink-simple-web-worker "Simplify Web Worker code with Comlink")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">article</span></p>

Web Workerの動作についての解説やComlinkを使ったWeb Workerの利用方法について

- [GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.](https://github.com/GoogleChromeLabs/comlink "GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.")

----

## Beyond SPAs: alternative architectures for your PWA  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/beyond-spa](https://developers.google.com/web/updates/2018/05/beyond-spa "Beyond SPAs: alternative architectures for your PWA  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">server</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

Service WorkerとExpressを使ったページ単位の(SPAではない)ウェブアプリのためのアーキテクチャと実装サンプルについて。
ルーティングをクライアントとサーバで共有し、パーシャルなViewをStream APIで取得しレンダリングする。また動的なメタ情報の渡し方についてなど

- [GoogleChromeLabs/so-pwa: A progressive web app to read Stack Overflow content.](https://github.com/GoogleChromeLabs/so-pwa "GoogleChromeLabs/so-pwa: A progressive web app to read Stack Overflow content.")

----

## Getting Started With CSS Layout — Smashing Magazine
[www.smashingmagazine.com/2018/05/guide-css-layout/](https://www.smashingmagazine.com/2018/05/guide-css-layout/ "Getting Started With CSS Layout — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSのレイアウトについての記事。
Float、Flex、Gridなどのレイアウトの仕組み。
BoxとContents、Alignmentなどについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JavaScript engines: The Good Parts™ // slidr.io
[slidr.io/mathiasbynens/javascript-engines-the-good-parts#1](https://slidr.io/mathiasbynens/javascript-engines-the-good-parts#1 "JavaScript engines: The Good Parts™ // slidr.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

JavaScriptエンジンの最適化パスについてのスライド。
V8、Spidermonkey、Chackra、JavaScriptCoreそれぞれの最適化パスの流れやShapeと最適化が崩れるパターンについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## GoogleChromeLabs/critters: 🦔 A Webpack plugin to inline your critical CSS and lazy-load the rest.
[github.com/GoogleChromeLabs/critters](https://github.com/GoogleChromeLabs/critters "GoogleChromeLabs/critters: 🦔 A Webpack plugin to inline your critical CSS and lazy-load the rest.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span> <span class="jser-tag">performance</span></p>

クリティカルCSSのインライン化、外部ファイルのlazy loadとprefetchの対応を行うwebpack plugin。


----

## Reach Router - Overview
[reach.tech/router](https://reach.tech/router "Reach Router - Overview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span></p>

React向けのルーターライブラリ。
React Routerの元々の作者が作成していて、Focus Mangementなどのアクセシビリティが考慮されている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## alangpierce/sucrase: Super-fast alternative to Babel for when you can target modern JS runtimes
[github.com/alangpierce/sucrase](https://github.com/alangpierce/sucrase "alangpierce/sucrase: Super-fast alternative to Babel for when you can target modern JS runtimes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">jsx</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

BabelのParserをforkして作られたJSX/Flow/TypeScriptなどをJSに変換するツール。
ES2015+が動く実行環境向けへコードを変換する際に、それ以外(JSX/Flow/TypeScript)の変換を高速に行うことが目的。
Babelとは異なりプラグインのステップを省くことで変換速度を向上させている。


----

## hybridsjs/hybrids: UI library for creating Web Components with simple and functional API
[github.com/hybridsjs/hybrids/](https://github.com/hybridsjs/hybrids/ "hybridsjs/hybrids: UI library for creating Web Components with simple and functional API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

`lit-html`のようにCustom Elementを作成できる`html`や`define`などを提供するライブラリ。


----

## Alex1990/tiny-cookie: A tiny cookie manipulation plugin for the browser.
[github.com/Alex1990/tiny-cookie](https://github.com/Alex1990/tiny-cookie "Alex1990/tiny-cookie: A tiny cookie manipulation plugin for the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

小さなクッキー操作ライブラリ


----

## GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.
[github.com/GoogleChromeLabs/comlink](https://github.com/GoogleChromeLabs/comlink "GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webworker</span></p>

Proxyを使ったWeb Workerライブラリ。
Worker内での実装をProxyして`postMessage`などのメッセージングを隠蔽してくれる


----

## marblejs/marble: Marble.js - functional reactive HTTP middleware framework built on top of Node.js platform, TypeScript and RxJS library.
[github.com/marblejs/marble](https://github.com/marblejs/marble "marblejs/marble: Marble.js - functional reactive HTTP middleware framework built on top of Node.js platform, TypeScript and RxJS library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">server</span> <span class="jser-tag">HTTP</span></p>

Rxjsを使ったHTTPミドルウェアフレームワーク。
Node.jsにおいてリクエスト、レスポンスに対する処理を書ける。


----

## Keyframes.app
[keyframes.app/](https://keyframes.app/ "Keyframes.app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">editor</span></p>

CSS animationのGUIエディタ。 CSS animationのプロパティを設定して、実際にアニメーションとして再生しながら変化するプロパティを決めたCSSを出力できる


----
<h1 class="site-genre">書籍関係</h1>

----

## Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books
[www.amazon.com/dp/1617295248/](https://www.amazon.com/dp/1617295248/ "Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span> <span class="jser-tag">JavaScript</span></p>

2018年8月31日発売。
Vue.jsのテスト本。


----
