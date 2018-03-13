---
title: "2018-03-13のJS: MobX 4.0.0、PreactとGlimmerのパフォーマンス比較実験"
author: "azu"
layout: post
date : 2018-03-13T01:26:18.731Z
category: JSer
tags:
- MobX
- Preact
- glimmer

---

JSer.info #374 - [MobX](https://github.com/mobxjs/mobx "MobX") 4.0.0がリリースされました。

- [MobX 4: Better, simpler, faster, smaller – Michel Weststrate – Medium](https://medium.com/@mweststrate/mobx-4-better-simpler-faster-smaller-c1fbc08008da)
- [mobx/CHANGELOG.md at master · mobxjs/mobx](https://github.com/mobxjs/mobx/blob/master/CHANGELOG.md#400)


Decorator proposal(`@decorator`)を使わずにObservableオブジェクトを作成する`decorate`関数の追加、[Object api](https://mobx.js.org/refguide/object-api.html "Object api | MobX")の追加、`when`や`flow`のような非同期サポートの補助する関数の追加などが行われています。

破壊的な変更として`shareGlobalState`の削除、observable mapに`Map`を使うように、`extras`関係のAPIのリネーム、`mobx`モジュールがdefault exportをしなくなるなどが行われています。
次のページにマイグレーションガイドが公開されています。

- [Migrating from mobx 3 to mobx 4 · mobxjs/mobx Wiki](https://github.com/mobxjs/mobx/wiki/Migrating-from-mobx-3-to-mobx-4 "Migrating from mobx 3 to mobx 4 · mobxjs/mobx Wiki")

また、現在開発中の[MobX 5(15?)](https://github.com/mobxjs/mobx/pull/1380)ではObservableにES Proxyを使ったものを予定しているようです。

- [Road to MobX 5 · Issue #1390 · mobxjs/mobx](https://github.com/mobxjs/mobx/issues/1390 "Road to MobX 5 · Issue #1390 · mobxjs/mobx")

----

[Lighter than Lightweight: How We Built the Same App Twice with Preact and Glimmer.js | LinkedIn Engineering](https://engineering.linkedin.com/blog/2018/03/how-we-built-the-same-app-twice-with-preact-and-glimmerjs "Lighter than Lightweight: How We Built the Same App Twice with Preact and Glimmer.js | LinkedIn Engineering")という記事では、同じアプリをPreactとGlimmer.jsで実装し、ページロードに関するパフォーマンスの比較実験をした結果について書かれています。
それぞれのアプリでページ表示に関する値を指標として比較した時に、極端な差はでませんでした。

- [Web クライアントサイドのパフォーマンスメトリクス — Speed Index、Paint Timing、TTI etc... ::ハブろぐ](https://havelog.ayumusato.com/develop/performance/e744-performance_metrics.html "Web クライアントサイドのパフォーマンスメトリクス — Speed Index、Paint Timing、TTI etc... ::ハブろぐ")
  - First Meaningful PaintやTime to Interactiveについての解説

Preact(3kb)とGlimmer.js(30kb)ではファイルサイズに差がありますが、その差がそのままページの表示時間に出てないことについて書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## DoneJS 2.0 Released
[www.bitovi.com/blog/donejs-2.0](https://www.bitovi.com/blog/donejs-2.0 "DoneJS 2.0 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

DoneJS 2.0リリース。
CanJS 4.0に対応、CIやデプロイの設定を`donejs add`で行えるように、`donejs upgrade`でマイグレーションができるようになっている。
HTTP/2 pushを使ったインクリメンタルレンダリングの対応改善など

- [Create Streamable, High-Performance Web Applications](https://www.bitovi.com/streamable "Create Streamable, High-Performance Web Applications")

----

## We have released version 3.0 of OpenPGPjs, an open source OpenPGP library - ProtonMail Blog
[protonmail.com/blog/openpgpjs-3-release/](https://protonmail.com/blog/openpgpjs-3-release/ "We have released version 3.0 of OpenPGPjs, an open source OpenPGP library - ProtonMail Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

OpenPGPの実装であるOpenPGP.js 3.0リリース


----

## New in Chrome 65  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/nic65](https://developers.google.com/web/updates/2018/03/nic65 "New in Chrome 65  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 65の変更点について。
CSS Paint API、Server Tming API、`display: contents`の対応、Feature Policyの対応など。
また`document.all`が上書きできなくなるようになるなど

- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D65 "Chrome Platform Status")
- [Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API](https://blog.chromium.org/2018/02/chrome-65-beta-css-paint-api-and.html "Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API")

----

## MobX 4: Better, simpler, faster, smaller – Michel Weststrate – Medium
[medium.com/@mweststrate/mobx-4-better-simpler-faster-smaller-c1fbc08008da](https://medium.com/@mweststrate/mobx-4-better-simpler-faster-smaller-c1fbc08008da "MobX 4: Better, simpler, faster, smaller – Michel Weststrate – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MobX 4リリース。
Decorator proposal(`@decorator`)を使わずに同じことをする`decorate`関数の追加、コレクション向けのUtility APIを追加、`when`の追加など。
また`shareGlobalState`の削除、APIのリネーム、default exportをしないようにするなどの破壊的変更が行われている。

- [Migrating from mobx 3 to mobx 4 · mobxjs/mobx Wiki](https://github.com/mobxjs/mobx/wiki/Migrating-from-mobx-3-to-mobx-4 "Migrating from mobx 3 to mobx 4 · mobxjs/mobx Wiki")
- [mobx/CHANGELOG.md at master · mobxjs/mobx](https://github.com/mobxjs/mobx/blob/master/CHANGELOG.md#400 "mobx/CHANGELOG.md at master · mobxjs/mobx")

----

## Release Futura · sass/libsass
[github.com/sass/libsass/releases/tag/3.5.0](https://github.com/sass/libsass/releases/tag/3.5.0 "Release Futura · sass/libsass")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Sass</span> <span class="jser-tag">library</span></p>

libsass 3.5リリース。 引数のtrailing commasサポート、`content-exists`関数のサポート、CSSのCustom Property、`var()`のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## An imperative guide to forms in React – LogRocket
[blog.logrocket.com/an-imperative-guide-to-forms-in-react-927d9670170a](https://blog.logrocket.com/an-imperative-guide-to-forms-in-react-927d9670170a "An imperative guide to forms in React – LogRocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

Reactを使ったフォームの扱いについての記事。
Formikを使ったフォームの作成などについて


----

## Emscripting a C library to Wasm  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/emscripting-a-c-library](https://developers.google.com/web/updates/2018/03/emscripting-a-c-library "Emscripting a C library to Wasm  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Emscriptenを使いCのコードをWebAssemblyにして実行するチュートリアル。
libwebpをwasmにコンパイルする話


----

## Feature Policy による Permission Delegation | blog.jxck.io
[blog.jxck.io/entries/2018-03-08/feature-policy-permission-delegation.html](https://blog.jxck.io/entries/2018-03-08/feature-policy-permission-delegation.html "Feature Policy による Permission Delegation | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

iframe sandbox、CSP、Feature Policyの役割について。
`sandbox`はホワイリトストでの機能制限、CSPはブラックリストでの機能制限、Feature Policyは権限の設定をオリジンに対して行う。
また`sandbox`とFeature Policyの機能重複はしないことについて


----

## Web Workers to the rescue – Rastislav Svarba – Medium
[rast.io/web-workers-rescue](https://rast.io/web-workers-rescue "Web Workers to the rescue – Rastislav Svarba – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">article</span></p>

Web Workerを使った処理の移譲のコストと効果についての記事。
データの取得と処理をWorkerに移動した場合の処理時間とWorkerへのデータ受け渡しのコストについて


----

## The npm Blog — Introducing \`npm ci\` for faster, more reliable...
[blog.npmjs.org/post/171556855892/introducing-npm-ci-for-faster-more-reliable](http://blog.npmjs.org/post/171556855892/introducing-npm-ci-for-faster-more-reliable "The npm Blog — Introducing \`npm ci\` for faster, more reliable...")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">npm</span></p>

`pacakge-lock.json`から常にクリーンインストールする`npm ci`について。 現在の存在する`node_modules`ディレクトリを削除し、`pacakge-lock.json`を元にインストールする。 キャッシュを使わないCI環境向けのインストールコマンド。

- [npm ciを使おう あるいはより速く - Qiita](https://qiita.com/mstssk/items/8759c71f328cab802670 "npm ciを使おう あるいはより速く - Qiita")

----

## Lighter than Lightweight: How We Built the Same App Twice with Preact and Glimmer.js | LinkedIn Engineering
[engineering.linkedin.com/blog/2018/03/how-we-built-the-same-app-twice-with-preact-and-glimmerjs](https://engineering.linkedin.com/blog/2018/03/how-we-built-the-same-app-twice-with-preact-and-glimmerjs "Lighter than Lightweight: How We Built the Same App Twice with Preact and Glimmer.js | LinkedIn Engineering")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

同じアプリをPreactとGlimmer.jsで実装し、ページロードに関するパフォーマンスの比較実験をした結果について。
ファイルサイズは重要であるが、ファイルサイズがすべてを決めるわけではないという点について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## andrew--r/frontend-case-studies: 💼 A curated list of technical talks and articles about real-world enterprise frontend development
[github.com/andrew--r/frontend-case-studies](https://github.com/andrew--r/frontend-case-studies "andrew--r/frontend-case-studies: 💼 A curated list of technical talks and articles about real-world enterprise frontend development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">企業</span> <span class="jser-tag">まとめ</span></p>

フロントエンドのケーススタディのまとめ。
色々な企業の事例が書かれている。


----

## 30 Seconds of CSS
[atomiks.github.io/30-seconds-of-css/](https://atomiks.github.io/30-seconds-of-css/ "30 Seconds of CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span></p>

CSSのスニペットとその解説をまとめたもの。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Boxy SVG Editor
[boxy-svg.com/](https://boxy-svg.com/ "Boxy SVG Editor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">editor</span> <span class="jser-tag">software</span></p>

SVGエディタアプリ


----

## pshihn/workly: A really simple way to move a stand-alone function/class to a web worker. 🏋️‍♀️→ 😄
[github.com/pshihn/workly](https://github.com/pshihn/workly "pshihn/workly: A really simple way to move a stand-alone function/class to a web worker. 🏋️‍♀️→ 😄")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ProxyとWebWorkerを使い既存の関数やクラスをWorkerで処理するライブラリ


----

## midwayjs/pandora: A Manageable, Measurable and Traceable Node.js Application Manager represented by Alibaba powered by TypeScript
[github.com/midwayjs/pandora](https://github.com/midwayjs/pandora "midwayjs/pandora: A Manageable, Measurable and Traceable Node.js Application Manager represented by Alibaba powered by TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

Alibaba製のNode.jsアプリケーションの管理ツール。
アプリケーションプロセスの管理、計測、監視、トラブルシューティングのためのデバッグの仕組みなどが持っている。


----

## Run
[run.tools/](https://run.tools/ "Run")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Node.js製のデプロイツール。
"Resource"という単位で設定を行い、S3へデプロイといったことを行える。
Resourceは自分で作成することができ、どのようなオプションを受け取るかやオプションを受け取って処理を記述できる。

- [Resources](https://run.tools/docs/reference/resources "Resources")

----

## zipson | JSON parse and stringify with compression
[jgranstrom.github.io/zipson/](https://jgranstrom.github.io/zipson/ "zipson | JSON parse and stringify with compression")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

`JSON.stringify`/`JSON.parse`の代替ライブラリ。
データの圧縮やStreamingのサポートを目的にしている


----

## Rough.js
[roughjs.com/](http://roughjs.com/ "Rough.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

手書き風の線を描くCanvasライブラリ


----
