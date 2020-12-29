---
title: "2020-12-29のJS: CSS Snapshot 2020、100万のサイトをクロールした調査結果、FlowからTypeScriptへの移行"
author: "azu"
layout: post
date : 2020-12-29T03:05:18.915Z
category: JSer
tags:
- browser
- node.js
- Tools
- performance
- Rust

---

JSer.info #520 - CSSの各仕様の現在のステータスを一覧する目的であるCSS Snapshot 2020が公開されています。

- [CSS Snapshot 2020](https://www.w3.org/TR/2020/NOTE-css-2020-20201222/)
- [CSS Snapshot 2020 日本語訳](https://momdo.github.io/css-2020/)
- [CSS Snapshot 2020が発行されました | フロントエンドBlog | ミツエーリンクス](https://www.mitsue.co.jp/knowledge/blog/frontend/202012/23_1049.html)

スナップショットとしてCSSモジュール(ここではCSSの各仕様のこと)のステータスとサマリがまとまとめられています。
CSSの仕様の全体像が分かりやすいので、興味がある人は見てみると良いかもしれません。

また、最新のステータスは[CSS current work & how to participate](https://www.w3.org/Style/CSS/current-work)で確認できます。

----

[JavaScript Performance in the Wild 2020 | CatchJS](https://catchjs.com/Blog/PerformanceInTheWild)という記事では、[Tranco](https://tranco-list.eu/)のデータを元にした100万サイトをPuppeteerでクロールした調査結果についてまとめられています。

どのような要因がウェブサイトのパフォーマンスに影響を与えているかを調査するために集めたデータとなっていて、ライブラリとメトリクスへの影響などについて書かれています。
集められたデータはKaggleで公開されています。

- [Web Performance Metrics | Kaggle](https://www.kaggle.com/indexhtml/web-performance-metrics)

また、類似するデータは[HTTP Archive](https://httparchive.org/)でも公開されているので興味がある人は調べてみると良いかもしれません。

CatchJSの記事では、同様の調査からウェブサイトのエラーについて書かれています。

- [JavaScript Errors in the Wild 2020 | CatchJS](https://catchjs.com/Blog/ErrorsInTheWild)

----

[War stories: The move from Flow to TypeScript](https://react.christmas/2020/2)という記事ではFlowからTypeScriptへの移行について書かれています。

 js-unused-exportsをForkして使われてないファイルの削除、flow-to-tsを使った変換、ESLintを使ったフォーマットの修正といったどのようにコードを移行していったかについて書かれています。
また移行期間中のコードのフリーズした話やマイグレーションの目標設定と目標の計測についても書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Volta 1.0.0 | Volta
[blog.volta.sh/2020/12/21/announcing-volta-100/](https://blog.volta.sh/2020/12/21/announcing-volta-100/ "Announcing Volta 1.0.0 | Volta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Nodeやnpmのバージョン管理ツールであるVolta 1.0.0リリース。


----

## Node v15.5.0 (Current) | Node.js
[nodejs.org/en/blog/release/v15.5.0/](https://nodejs.org/en/blog/release/v15.5.0/ "Node v15.5.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v15.5.0リリース。
`child_process`と`stream`がAbortSignalをサポート、`querystring.stringify()`がBigIntをサポートなど


----

## Release 4.0.0 · fuse-box/fuse-box
[github.com/fuse-box/fuse-box/releases/tag/v4.0.0](https://github.com/fuse-box/fuse-box/releases/tag/v4.0.0 "Release 4.0.0 · fuse-box/fuse-box")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

FuseBox 4.0リリース。
破壊的な変更として`homeDir`、`output`、`useSigleBundle`の削除。
`watch`オプションを`watcher`にリネーム、
`output`オプションの代わりに`bundles.distRoot`を使うように変更など

- [Changelog fuse 3 to 4 · FuseBox](https://fuse-box.org/docs/development/changelog-fuse-compiler "Changelog fuse 3 to 4 · FuseBox")

----

## CSS Snapshot 2020
[www.w3.org/TR/2020/NOTE-css-2020-20201222/](https://www.w3.org/TR/2020/NOTE-css-2020-20201222/ "CSS Snapshot 2020")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

CSS Snapshot 2020リリース

- [CSS Snapshot 2020 日本語訳](https://momdo.github.io/css-2020/ "CSS Snapshot 2020 日本語訳")
- [CSS Snapshot 2020が発行されました | フロントエンドBlog | ミツエーリンクス](https://www.mitsue.co.jp/knowledge/blog/frontend/202012/23_1049.html "CSS Snapshot 2020が発行されました | フロントエンドBlog | ミツエーリンクス")
- [Working Group Note: CSS Snapshot 2020 | W3C News](https://www.w3.org/blog/news/archives/8820 "Working Group Note: CSS Snapshot 2020 | W3C News")

----

## cross-env is "finished" (now in maintenance mode) · Issue #257 · kentcdodds/cross-env
[github.com/kentcdodds/cross-env/issues/257](https://github.com/kentcdodds/cross-env/issues/257 "cross-env is \"finished\" (now in maintenance mode) · Issue #257 · kentcdodds/cross-env")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

cross-envがメンテナンスモードとなりアーカイブされた。
機能として完成しているため、これ以上機能追加することはないため。セキュリティアップデートと新しいNode.jsへの対応は続けるメンテナンスモードとなった


----
<h1 class="site-genre">アーティクル</h1>

----

## CSS Containment によるパフォーマンス改善 — HACK The Nikkei
[hack.nikkei.com/blog/advent20201219/](https://hack.nikkei.com/blog/advent20201219/ "CSS Containment によるパフォーマンス改善 — HACK The Nikkei")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

CSS Containmentの`contain: content`によるPaint Timeの改善について。


----

## Web Performance Calendar » Strategies for Telemetry Exfiltration (aka Beaconing In Practice)
[calendar.perfplanet.com/2020/beaconing-in-practice/](https://calendar.perfplanet.com/2020/beaconing-in-practice/ "Web Performance Calendar » Strategies for Telemetry Exfiltration (aka Beaconing In Practice)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

ブラウザからメトリクスデータを送信するときの戦略について。
`navigator.sendBeacon`/Fetch/XHR/pixel imageでの送信、どのタイミングで送信するかのライフサイクルイベントの到達信頼性についての調査。
ローカルストレージでの再送やService Workerでのバッファ、Reporting APIについてなど。


----

## Maximally optimizing image loading for the web in 2021
[www.industrialempathy.com/posts/image-optimizations/](https://www.industrialempathy.com/posts/image-optimizations/ "Maximally optimizing image loading for the web in 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

画像の読み込みの最適化についてまとめた記事。
widthとheightでのCLSの回避、`content-visibility`、AVIF、`srcset`と`size`属性、Cache-Controlヘッダ、`loading`属性と`decoding`属性。
プレースホルダー画像を使う方法についてなど


----

## War stories: The move from Flow to TypeScript
[react.christmas/2020/2](https://react.christmas/2020/2 "War stories: The move from Flow to TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

約15日でFlowからTypeScriptのマイグレーションした話。
js-unused-exportsを使った使われてないファイルの削除、flow-to-tsを使った変換、ESLintを使ったフォーマットの修正。
コードのフリーズとマイグレーションの目標について


----

## JavaScript Performance in the Wild 2020 | CatchJS
[catchjs.com/Blog/PerformanceInTheWild](https://catchjs.com/Blog/PerformanceInTheWild "JavaScript Performance in the Wild 2020 | CatchJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

https://tranco-list.eu/ のデータを元にサイトをPuppeteerでクロールして集めたパフォーマンスに関するデータセットについて。
Kaggleでデータセットを公開している。
HTTPのプロトコルバージョン、サードパーティリソース、ライブラリとそれぞれのメトリクスの関係性などについて。
2.2%のサイトでjQueryのロードをしていないためにエラーが発生していることなどについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## msn0/mdn-polyfills: MDN polyfills - from, forEach, filter, find, findIndex, assign, includes, create, entries, of, repeat, startsWith, endsWith, toggleAttribute, bind, MouseEvent, CustomEvent, padEnd, padStart
[github.com/msn0/mdn-polyfills](https://github.com/msn0/mdn-polyfills "msn0/mdn-polyfills: MDN polyfills - from, forEach, filter, find, findIndex, assign, includes, create, entries, of, repeat, startsWith, endsWith, toggleAttribute, bind, MouseEvent, CustomEvent, padEnd, padStart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">mdn</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span></p>

MDNに載っているJavaScriptやDOM APIのpolyfillをまとめたパッケージ


----

## jsDocs.io
[www.jsdocs.io/](https://www.jsdocs.io/ "jsDocs.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

npmパッケージに含まれるTypeScriptの型定義ファイルをベースに自動的にドキュメントを生成して表示できるサービス


----

## jameslittle230/stork: 🔎 Impossibly fast web search, made for static sites.
[github.com/jameslittle230/stork](https://github.com/jameslittle230/stork "jameslittle230/stork: 🔎 Impossibly fast web search, made for static sites.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">WebAssembly</span></p>

Rustで書かれたindexerとWebAssemblyを使った検索ライブラリ。
検索対象のファイルからインデックスファイルを作り、それを元にした検索機能/UIを提供するライブラリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## devbridge/js-unused-exports
[github.com/devbridge/js-unused-exports](https://github.com/devbridge/js-unused-exports "devbridge/js-unused-exports")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのファイルから使われてない関数、ファイルを抽出するツール。
細かい無視オプションやaliasの対応などのオプションをもっている。


----
<h1 class="site-genre">書籍関係</h1>

----

## Webブラウザセキュリティ ― Webアプリケーションの安全性を支える仕組みを整理する – 技術書出版と販売のラムダノート
[www.lambdanote.com/collections/frontpage/products/wbs](https://www.lambdanote.com/collections/frontpage/products/wbs "Webブラウザセキュリティ ― Webアプリケーションの安全性を支える仕組みを整理する – 技術書出版と販売のラムダノート")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">book</span></p>

2021年1月5日 発売
ウェブセキュリティについての書籍。
SOP、CORS、CSPなどのOriginを境界にしたセキュリティ機構、ブラウザのプロセス分離モデル、Cookieについてなど


----
