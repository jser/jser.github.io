---
title: "2016-11-08のJS: sitespeed.io 4.0、webpack 2 beta入門、JavaScriptスタックチュートリアル"
author: azu
layout: post
date : 2016-11-08T10:44
category: JSer
tags:
    - performance
    - webpack
    - JavaScript
    - framework

---

JSer.info #304 - ウェブサイトのパフォーマンス計測ツールである[sitespeed.io](https://www.sitespeed.io/ "sitespeed.io") v4.0がリリースされました。

- [Welcome sitespeed.io 4.0](https://www.sitespeed.io/sitespeed.io-4.0-is-released/)

4.0ではGraphite/Grafanaと組み合わせた[Performance Dashboard](https://www.sitespeed.io/documentation/sitespeed.io/performance-dasboard/ "Performance Dashboard")がセットアップできるDockerの設定も公開されています。

```
curl -O https://raw.githubusercontent.com/sitespeedio/sitespeed.io/master/docker/docker-compose.yml
docker-compose up
```

関連(v4より前の設定)

- [graphite, grafana, sitespeed.io, diamond で継続 Web パフォーマンスモニタリング - Qiita](http://qiita.com/Jxck_/items/abfa9f3dd15c5572cbfd)
- [続・パフォーマンス計測実験で Graphite も Docker に置き換えた ::ハブろぐ](https://havelog.ayumusato.com/develop/performance/e670-use_docker_instead_of_hosted_graphite.html)

またv4.0では、Pre/Postスクリプトでログインに対応、プラグインの仕組み、HTTP/2、HARファイルの対応改善、モバイル対応などの改善が含まれています。

単純に[sitespeed.io](https://www.sitespeed.io/ "sitespeed.io")でチェックするだけなら、npmで簡単に入るので試してみると面白いかもしれません。

```
npm install -g sitespeed.io
sitespeed.io https://jser.info
```

----

[Getting Started with Webpack 2](https://blog.madewithenvy.com/getting-started-with-webpack-2-ed2b86c68783)という記事では、webpack 2(beta)を元にしたチュートリアルが紹介されています。

[webpack#1545](https://github.com/webpack/webpack/issues/1545#issuecomment-255614222)に作者である@[sokra](https://github.com/sokra "sokra")によるwebpack 2のステータスについて書かれています。

「今年中にはリリースしたいが、まだドキュメント周りにまだ問題があるためContributionを歓迎しています」とのことです。

------

[JavaScript Stack from Scratch](https://github.com/verekia/js-stack-from-scratch "JavaScript Stack from Scratch")([翻訳: ゼロから始めるJavaScript生活](https://github.com/takahashim/js-stack-from-scratch))では、JavaScriptのエコシステムを活用するチュートリアルが公開されています。

> これら全てのツールを一緒につなぎ合わせることにフォーカスしており、各ツールについて可能な限りシンプルな例を提供します。

とあるようにツールを組み合わせて利用することを主軸としているので、一度見てみると面白いかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Welcome sitespeed.io 4.0
[www.sitespeed.io/sitespeed.io-4.0-is-released/](https://www.sitespeed.io/sitespeed.io-4.0-is-released/ "Welcome sitespeed.io 4.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Sitespeed.io 4.0リリース。
Dockerでgrafanaのダッシュボードを含んだセットアップが用意された、Pre/Postスクリプトでログインに対応、プラグイン、HTTP/2、HARファイルの対応改善、モバイル対応など

----

## Release v0.34.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.34.0](https://github.com/facebook/flow/releases/tag/v0.34.0 "Release v0.34.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType v0.34.0リリース。
`empty` typeの追加、AsyncIterationの対応など

----

## async/await support in Firefox | Firefox Nightly News
[blog.nightly.mozilla.org/2016/11/01/async-await-support-in-firefox/](https://blog.nightly.mozilla.org/2016/11/01/async-await-support-in-firefox/ "async/await support in Firefox | Firefox Nightly News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span></p>

Firefox Nightlyにasync/awaitが実装された。

----
<h1 class="site-genre">アーティクル</h1>

----

## Getting Started with Webpack 2
[blog.madewithenvy.com/getting-started-with-webpack-2-ed2b86c68783](https://blog.madewithenvy.com/getting-started-with-webpack-2-ed2b86c68783 "Getting Started with Webpack 2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpack 2を使ったビルドの設定について。
multiple entry、loader、bundleの分割などについて

----

## What&#x27;s New and What&#x27;s Changed in Bootstrap 4 -Telerik Developer Network
[developer.telerik.com/featured/whats-new-whats-changed-bootstrap-4/](http://developer.telerik.com/featured/whats-new-whats-changed-bootstrap-4/ "What's New and What's Changed in Bootstrap 4 -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Bootstrap 4αでの変更点について

----

## Vue.js 1.x から 2.0 への移行のポイント | d.sunnyone.org
[d.sunnyone.org/2016/11/vuejs-1x-20.html](http://d.sunnyone.org/2016/11/vuejs-1x-20.html "Vue.js 1.x から 2.0 への移行のポイント | d.sunnyone.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Vue 1.xから2.0へのマイグレーションについて。
テンプレートが事前コンパイルされるようになったことでの違いや移行方法、気をつけるポイントについて

----

## TypeScript 2.0: Read-Only Properties | Marius Schulz
[blog.mariusschulz.com/2016/10/31/typescript-2-0-read-only-properties](https://blog.mariusschulz.com/2016/10/31/typescript-2-0-read-only-properties "TypeScript 2.0: Read-Only Properties | Marius Schulz")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2.0の`readonly`について

----

## Cooperative Scheduling with requestIdleCallback ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/11/cooperative-scheduling-with-requestidlecallback/](https://hacks.mozilla.org/2016/11/cooperative-scheduling-with-requestidlecallback/ "Cooperative Scheduling with requestIdleCallback ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

Firefox 52で実装される`requestIdleCallback`についての解説。
`timeRemaining()`、`timeout`オプションやキャンセルした場合についてなど。

- [Cooperative Scheduling of Background Tasks（日本語訳）](https://triple-underscore.github.io/requestidlecallback-ja.html "Cooperative Scheduling of Background Tasks（日本語訳）")
- [Using requestIdleCallback  |  Web  |  Google Developers](https://developers.google.com/web/updates/2015/08/using-requestidlecallback "Using requestIdleCallback  |  Web  |  Google Developers")

----

## Pointing the Way Forward  |  Web  |  Google Developers
[developers.google.com/web/updates/2016/10/pointer-events](https://developers.google.com/web/updates/2016/10/pointer-events "Pointing the Way Forward  |  Web  |  Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Pointer eventsについて。
PenやTouchなどのイベントモデルを抽象化したもの。
`pointerType`でイベントの種類ごと扱う方法、`pointercancel`や`touch-action`について

----

## Build a Universal JavaScript App with Next.js
[auth0.com/blog/building-universal-apps-with-nextjs/](https://auth0.com/blog/building-universal-apps-with-nextjs/ "Build a Universal JavaScript App with Next.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span></p>

Next.jsを使ったアプリケーションを作るチュートリアル。

----

## takahashim/js-stack-from-scratch: Step-by-step tutorial to build a modern JavaScript stack from scratch
[github.com/takahashim/js-stack-from-scratch](https://github.com/takahashim/js-stack-from-scratch "takahashim/js-stack-from-scratch: Step-by-step tutorial to build a modern JavaScript stack from scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">翻訳</span></p>

JavaScriptのエコシステムや著名なライブラリを使ったチュートリアルの翻訳。
色々なツールをあわせ使うことを前提に書かれたガイド

----

## jareware/css-architecture: 8 simple rules for a robust, scalable CSS architecture
[github.com/jareware/css-architecture](https://github.com/jareware/css-architecture "jareware/css-architecture: 8 simple rules for a robust, scalable CSS architecture")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">設計</span></p>

8つのルールを元にしたCSSのアーキテクチャ。
コンポーネントとCSSの関係についてが中心

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## vhf/v8-bailout-reasons: A list of Crankshaft bailout reasons with examples
[github.com/vhf/v8-bailout-reasons](https://github.com/vhf/v8-bailout-reasons "vhf/v8-bailout-reasons: A list of Crankshaft bailout reasons with examples")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8のdeoptimizationがなぜ起きるのかについて"Bailout reasons"と共に理由を解説してるリポジトリ

- [V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## turbo.js - Easy GPGPU
[turbo.github.io/](https://turbo.github.io/ "turbo.js - Easy GPGPU")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span></p>

GLSLを使って演算処理を行うライブラリ

----

## tfennelly/browserify-tree: Generate a Browserify bundle dependency tree for bundled modules
[github.com/tfennelly/browserify-tree](https://github.com/tfennelly/browserify-tree "tfennelly/browserify-tree: Generate a Browserify bundle dependency tree for bundled modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Tools</span></p>

Browserifyでbundleしたファイルの依存ツリーを見ることができるツール

----

## naver/egjs: Set of UI interactions, effects and utility components library using jQuery.
[github.com/naver/egjs](https://github.com/naver/egjs "naver/egjs: Set of UI interactions, effects and utility components library using jQuery.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

jQueryベースのUIインタラクション、エフェクトライブラリ

----

## Grimoire.js
[grimoire.gl/](https://grimoire.gl/ "Grimoire.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">library</span></p>

GOMLというHTMLライクなXMLシンタックスで記述して、WebGLを使った3D表現を行うライブラリ。
`<scene>`や`<camera>`といったノードを組み合わせることで表現する。

----
<h1 class="site-genre">書籍関係</h1>

----

## Securing Third-Party Code - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920051695.do](http://shop.oreilly.com/product/0636920051695.do "Securing Third-Party Code - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">OSS</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

2017年1月発売
JavaScriptのサードパーティのコードを安全に使う方法についての書籍

----

## Developing SPAs - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920046349.do](http://shop.oreilly.com/product/0636920046349.do "Developing SPAs - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年1月発売
.NET開発者向けのSPA本

----

## Pro Angular 2: ADAM FREEMAN: 9781484223062: Amazon.com: Books
[www.amazon.com/Pro-Angular-2-ADAM-FREEMAN/dp/1484223063](https://www.amazon.com/Pro-Angular-2-ADAM-FREEMAN/dp/1484223063 "Pro Angular 2: ADAM FREEMAN: 9781484223062: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

2017年5月8日発売
AngularJS 2についての書籍

----

## WebデベロッパーのためのReact開発入門 JavaScript UI ライブラリの基本と活用 | 柴田 文彦 |本 | 通販 | Amazon
[www.amazon.co.jp/Web%E3%83%87%E3%83%99%E3%83%AD%E3%83%83%E3%83%91%E3%83%BC%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AEReact%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80-JavaScript-UI-%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A8%E6%B4%BB%E7%94%A8-%E6%9F%B4%E7%94%B0/dp/4295000337](https://www.amazon.co.jp/Web%E3%83%87%E3%83%99%E3%83%AD%E3%83%83%E3%83%91%E3%83%BC%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AEReact%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80-JavaScript-UI-%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A8%E6%B4%BB%E7%94%A8-%E6%9F%B4%E7%94%B0/dp/4295000337 "WebデベロッパーのためのReact開発入門 JavaScript UI ライブラリの基本と活用 | 柴田 文彦 |本 | 通販 | Amazon")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2016年11月25日発売
Reactの入門本

- [WebデベロッパーのためのReact開発入門 JavaScript UIライブラリの基本と活用 - インプレスブックス](http://book.impress.co.jp/books/1116101049 "WebデベロッパーのためのReact開発入門 JavaScript UIライブラリの基本と活用 - インプレスブックス")

----
