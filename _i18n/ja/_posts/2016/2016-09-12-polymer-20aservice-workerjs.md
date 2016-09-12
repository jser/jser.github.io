---
title: "2016-09-12のJS: Polymer 2.0 Preview、Service Worker入門、JSから型定義ファイルの生成"
author: azu
layout: post
date : 2016-09-12T20:19
category: JSer
tags:
    - Polymer
    - WebComponent
    - ServiceWorker
    - Flow
    - TypeScript

---

JSer.info #296 - [Polymer 2.0 Preview](https://www.polymer-project.org/1.0/blog/2016-09-09-polymer-2.0 "Polymer 2.0 Preview")がリリースされました。

Polymer 2.0ではWebComponent v1([Shadow DOM v1](http://hayato.io/2016/shadowdomv1/ "Shadow DOM v1")や[Custom Elements v1](https://developers.google.com/web/fundamentals/primers/customelements/ "Custom Elements v1"))の上に形成されています。
そのため、v1の仕様に準拠した変更やクラスベースのコンポーネントが作成できるようになっています。

- [Polymer/polymer at 2.0-preview](https://github.com/Polymer/polymer/tree/2.0-preview "Polymer/polymer at 2.0-preview")

----

Flow 0.32.0がリリースされました。

- [Release v0.32.0 · facebook/flow](https://github.com/facebook/flow/releases/tag/v0.32.0 "Release v0.32.0 · facebook/flow")

0.32.0では、アノテーション付きのJavaScriptファイルからFlowの型定義ファイルを生成する`gen-flow-files`コマンドが追加されています。

- [flowtype v0.32.0 changes - Please Drive Faster](http://joe-re.hatenablog.com/entry/2016/09/06/101529 "flowtype v0.32.0 changes - Please Drive Faster")

また、TypeScriptの方では素のJavaScriptファイルからTypeScriptの型定義ファイルを生成する[dts-gen](https://github.com/Microsoft/dts-gen "dts-gen")というツールが公開されています。

- [Microsoft/dts-gen: dts-gen creates starter TypeScript definition files for any module or library.](https://github.com/Microsoft/dts-gen "Microsoft/dts-gen: dts-gen creates starter TypeScript definition files for any module or library.")

どちらもα版といった感じですが、気になる方はためしてみると良いかもしれません。

追記: [dts-gen(1) でJavaScripファイルからdtsを生成する - Islands in the byte stream](http://gfx.hatenablog.com/entry/2016/09/12/232554 "dts-gen(1) でJavaScripファイルからdtsを生成する - Islands in the byte stream")

----

[Service Workerの基本とそれを使ってできること - Qiita](http://qiita.com/y_fujieda/items/f9e765ac9d89ba241154)という記事では、Service Workerの基本的なライフサイクルやキャッシュ、Pushの実現について紹介されています。

また、Googleの[Introduction to Service Worker | Web Fundamentals - Google Developers](https://developers.google.com/web/fundamentals/primers/service-worker/?hl=en "Introduction to Service Worker | Web Fundamentals - Google Developers")の[翻訳](https://developers.google.com/web/fundamentals/primers/service-worker/)も公開されているので、合わせて読んでみるといいかもしれません。

> Promise を多用する

とあるようにService WorkerはPromiseがネストするので、それに対するアプローチを紹介している[Untangling Deeply-Nested Promise Chains — Philip Walton](https://philipwalton.com/articles/untangling-deeply-nested-promise-chains/ "Untangling Deeply-Nested Promise Chains — Philip Walton")も読んでみると面白いかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Polymer 2.0 Preview - Polymer Project
[www.polymer-project.org/1.0/blog/2016-09-09-polymer-2.0](https://www.polymer-project.org/1.0/blog/2016-09-09-polymer-2.0 "Polymer 2.0 Preview - Polymer Project")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

Polymer 2.0 Previewリリース。
Shadow DOM v1、クラスベースで書けるようになるなど

----

## V8 JavaScript Engine: V8 Release 5.4
[v8project.blogspot.com/2016/09/v8-release-54.html](http://v8project.blogspot.com/2016/09/v8-release-54.html "V8 JavaScript Engine: V8 Release 5.4")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.4リリース。
メモリが少ない端末でのメモリ消費量の改善、起動速度の改善など

----

## Ember.js - Ember.js 2.8 and 2.9 Beta Released
[emberjs.com/blog/2016/09/08/ember-2-8-and-2-9-beta-released.html](http://emberjs.com/blog/2016/09/08/ember-2-8-and-2-9-beta-released.html "Ember.js - Ember.js 2.8 and 2.9 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 2.8と2.9βリリース
2.8で`Ember.Engine` APIを追加など

----

## Jest 15.0: New Defaults for Jest · Jest
[facebook.github.io/jest/blog/2016/09/01/jest-15.html](http://facebook.github.io/jest/blog/2016/09/01/jest-15.html "Jest 15.0: New Defaults for Jest · Jest")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 15.0リリース。
CLIの表示を改善、Watchコマンドを追加、jest-react-nativeの改善など

----

## Release v0.32.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.32.0](https://github.com/facebook/flow/releases/tag/v0.32.0 "Release v0.32.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.32.0リリース
`{|`と`|}`を使ったexact object typeの追加、`flow gen-flow-files`コマンドの追加など

----

## ESLint v3.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/09/eslint-v3.5.0-released](http://eslint.org/blog/2016/09/eslint-v3.5.0-released "ESLint v3.5.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.5.0リリース。
新しいルールの追加、`--fix`の対応ルールの追加など

- [ESLint v3.5.0 - Qiita](http://qiita.com/mysticatea/items/875c801362f337bc4ce9 "ESLint v3.5.0 - Qiita")

----

## Release Release 4.0.0 · ternjs/acorn
[github.com/ternjs/acorn/releases/tag/4.0.0](https://github.com/ternjs/acorn/releases/tag/4.0.0 "Release Release 4.0.0 · ternjs/acorn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AST</span> <span class="jser-tag">ReleaseNote</span></p>

acorn 4.0.0リリース。
デフォルトの`ecmaVersion`が`7`となり、async/awaitの構文をサポートなど

----
<h1 class="site-genre">アーティクル</h1>

----

## ES2015で始めるJavaScript入門 - Qiita
[qiita.com/ABCanG1015/items/824681cb88676da4f9a8](http://qiita.com/ABCanG1015/items/824681cb88676da4f9a8 "ES2015で始めるJavaScript入門 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

ES2015ベースでJavaScriptについて学ぶレッスン式のチュートリアル

----

## わぁいアリア（WAI-ARIA）大好き | れいぶろぐ
[labe.wp.xdomain.jp/post/567](http://labe.wp.xdomain.jp/post/567 "わぁいアリア（WAI-ARIA）大好き | れいぶろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WAI-ARIA</span></p>

WAI-ARIAはどんなもので何のためにあるのかを分かりやすく解説してる

----

## Service Worker の紹介 | Web Fundamentals - Google Developers
[developers.google.com/web/fundamentals/primers/service-worker/](https://developers.google.com/web/fundamentals/primers/service-worker/ "Service Worker の紹介 | Web Fundamentals - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">翻訳</span></p>

Service Workerについての紹介記事翻訳

----

## Service Workerの基本とそれを使ってできること - Qiita
[qiita.com/y\_fujieda/items/f9e765ac9d89ba241154](http://qiita.com/y_fujieda/items/f9e765ac9d89ba241154 "Service Workerの基本とそれを使ってできること - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span></p>

Service Workerのライフサイクルやどのような事ができるかの紹介記事。
Cache、Pushについて

----

## flowtype v0.32.0 changes - Please Drive Faster
[joe-re.hatenablog.com/entry/2016/09/06/101529](http://joe-re.hatenablog.com/entry/2016/09/06/101529 "flowtype v0.32.0 changes - Please Drive Faster")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">Tools</span></p>

JavaScriptファイルからFlowの型定義ファイルを生成する`gen-flow-files`コマンドについて

----

## Untangling Deeply-Nested Promise Chains — Philip Walton
[philipwalton.com/articles/untangling-deeply-nested-promise-chains/](https://philipwalton.com/articles/untangling-deeply-nested-promise-chains/ "Untangling Deeply-Nested Promise Chains — Philip Walton")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span></p>

Promiseでネストが深くなったものを、関数へ分割やasync/awaitを使いネストを浅くリファクタリングする話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Remark
[iros.github.io/d3-v4-whats-new/#1](https://iros.github.io/d3-v4-whats-new/#1 "Remark")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">d3.js</span> <span class="jser-tag">スライド</span></p>

D3.js v4についてのスライド。
モジュール分割、Canvasへの書き出し、分割されたモジュール毎の解説

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## DevTools Timeline Viewer
[chromedevtools.github.io/timeline-viewer/](https://chromedevtools.github.io/timeline-viewer/ "DevTools Timeline Viewer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chromeの開発者ツールのTimelineデータを読み込ませて表示できるサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Microsoft/dts-gen: dts-gen creates starter TypeScript definition files for any module or library.
[github.com/Microsoft/dts-gen](https://github.com/Microsoft/dts-gen "Microsoft/dts-gen: dts-gen creates starter TypeScript definition files for any module or library.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

npmパッケージやコードからd.tsを自動生成してくれるツール

----

## Fuse.js - JavaScript fuzzy-search library
[fusejs.io/](http://fusejs.io/ "Fuse.js - JavaScript fuzzy-search library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">検索</span></p>

データからあいまい検索を行えるJavaScriptライブラリ

----

## ebidel/appmetrics.js: A small (1.1kb) library for measuring things in your web app and reporting the results to Google Analytics.
[github.com/ebidel/appmetrics.js](https://github.com/ebidel/appmetrics.js "ebidel/appmetrics.js: A small (1.1kb) library for measuring things in your web app and reporting the results to Google Analytics.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">アクセス解析</span> <span class="jser-tag">library</span></p>

User Timing APIを使って計測したデータをGoogle Analyticsにレポートできるライブラリ

----

## jgornick/asyncp: Port of the Async.js API to use Promises
[github.com/jgornick/asyncp](https://github.com/jgornick/asyncp "jgornick/asyncp: Port of the Async.js API to use Promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Promises</span></p>

async.jsのAPIをPromiseを使って実装したライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript: The New Toys: T. J. Crowder: 9781119367956: Amazon.com: Books
[www.amazon.com/JavaScript-Toys-T-J-Crowder/dp/1119367956](https://www.amazon.com/JavaScript-Toys-T-J-Crowder/dp/1119367956 "JavaScript: The New Toys: T. J. Crowder: 9781119367956: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年4月10日発売
ES2015+についての書籍

----

## 改訂新版JavaScript本格入門　～モダンスタイルによる基礎から現場での応用まで：書籍案内｜技術評論社
[gihyo.jp/book/2016/978-4-7741-8411-1](http://gihyo.jp/book/2016/978-4-7741-8411-1 "改訂新版JavaScript本格入門　～モダンスタイルによる基礎から現場での応用まで：書籍案内｜技術評論社")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016年9月30日発売
JavaScript本格入門の改訂版

- [JavaScript本格入門　～モダンスタイルによる基礎からAjax・jQueryまで：書籍案内｜技術評論社](http://gihyo.jp/book/2010/978-4-7741-4466-5 "JavaScript本格入門　～モダンスタイルによる基礎からAjax・jQueryまで：書籍案内｜技術評論社")

----
