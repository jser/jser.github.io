---
title: "2018-07-24のJS: Monthly Webの作り方、普通のHTMLの書き方"
author: "azu"
layout: post
date : 2018-07-24T00:40:57.119Z
category: JSer
tags:
- Web
- HTML

---

JSer.info #393 - [Monthly Web の作り方 2018 年版 | blog.jxck.io](https://blog.jxck.io/entries/2018-07-18/how-to-logging-monthly-web.html)という記事では、[mozaic.fm](https://mozaic.fm/)というPodcastにおいて毎月公開しているウェブ標準や実装の動向についてどうやって情報を集めるかについて書かれています。

ブラウザ、WHATWG/W3C、TC39、IETFに関してどのようなスタイルで情報が公開されているかについてまとめられています。
仕様や試験的な実装の動きについて興味がある人は見てみると良さそうです。

----

[普通のHTMLの書き方](https://hail2u.net/documents/html-best-practices.html)というドキュメントでは、HTMLの現代的な書き方について書かれています。

HTMLをメンテナンスしやすい簡潔な書き方、セマンティック、アクセシビリティを考慮した書き方などについてのドキュメントです。
XHTMLやHTML4.01など古い仕様からくる非推奨な書き方をどのように避けるべきかについても書かれています。
それぞれの項目に悪い例と良い例つきで解説されていて、よくある記述の仕様的な解説なども書かれています。

以前公開されたドキュメントに解説がついたものとなっています。

- [hail2u/html-best-practices: For writing maintainable and scalable HTML documents](https://github.com/hail2u/html-best-practices)

----

## お知らせ

以前お知らせしたJSer.info 400回記念イベントの日付が2018年9月22日(土)に決まりました。
2018年8月中にはイベントページを作ると思います。

また、何かしたい/聞きたいことがある場合は次のIssueに書いてください。

- [JSer.info 400回記念イベント · Issue #102 · jser/jser.info](https://github.com/jser/jser.info/issues/102)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 61 | WebKit
[webkit.org/blog/8365/release-notes-for-safari-technology-preview-61/](https://webkit.org/blog/8365/release-notes-for-safari-technology-preview-61/ "Release Notes for Safari Technology Preview 61 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 61リリース。
`Element.toggleAttribute`のサポート、`fetch`の`credentials`のデフォルト値を`same-origin`へ変更など

- [Element.toggleAttribute | blog.jxck.io](https://blog.jxck.io/entries/2018-07-20/toggle-attribute.html "Element.toggleAttribute | blog.jxck.io")

----

## Node v10.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v10.7.0/](https://nodejs.org/en/blog/release/v10.7.0/ "Node v10.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 10.7.0リリース。
`console.timeLog()`の実装、`process.hrtime.bigint()`の実装、`--title`コマンドライン引数でプロセスのタイトルを指定できるようになるなど


----

## Ember.js - Ember 3.3 Released
[emberjs.com/blog/2018/07/16/ember-3-3-released.html](https://emberjs.com/blog/2018/07/16/ember-3-3-released.html "Ember.js - Ember 3.3 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 3.3リリース。
jQueryの依存をオプショナルにできるように

- [Release v3.3.0 · emberjs/ember.js](https://github.com/emberjs/ember.js/releases/tag/v3.3.0 "Release v3.3.0 · emberjs/ember.js")

----

## Support the native graal packages by ChadKillingsworth · Pull Request #90 · google/closure-compiler-npm
[github.com/google/closure-compiler-npm/pull/90](https://github.com/google/closure-compiler-npm/pull/90 "Support the native graal packages by ChadKillingsworth · Pull Request #90 · google/closure-compiler-npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Java</span> <span class="jser-tag">news</span> <span class="jser-tag">Tools</span></p>

Closure Compilerにネイティブバイナリが同梱された(macOSとLinux)

- [Release 20180716.0.0 · google/closure-compiler-npm](https://github.com/google/closure-compiler-npm/releases/tag/20180716.0.0 "Release 20180716.0.0 · google/closure-compiler-npm")

----

## CanJS 5.0
[www.bitovi.com/blog/canjs-5](https://www.bitovi.com/blog/canjs-5 "CanJS 5.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CanJS 5.0リリース。


----
<h1 class="site-genre">アーティクル</h1>

----

## Connection-Aware Components | Max Böck - Frontend Web Developer
[mxb.at/blog/connection-aware-components/](https://mxb.at/blog/connection-aware-components/ "Connection-Aware Components | Max Böck - Frontend Web Developer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">React</span></p>

Network Information APIや`navigator.onLine`などを使った接続情報を考慮したReactコンポーネントの作り方について


----

## Compiler in JavaScript using ANTLR – DailyJS – Medium
[medium.com/dailyjs/compiler-in-javascript-using-antlr-9ec53fd2780f](https://medium.com/dailyjs/compiler-in-javascript-using-antlr-9ec53fd2780f "Compiler in JavaScript using ANTLR – DailyJS – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">AST</span></p>

ANTLRを使ってコンパイラを作る話。
ECMAScriptを入力にしてPythonのコードを出力するコンパイラをどうのように作るかについて

- [antlr4 - npm](https://www.npmjs.com/package/antlr4 "antlr4 - npm")

----

## Element.toggleAttribute | blog.jxck.io
[blog.jxck.io/entries/2018-07-20/toggle-attribute.html](https://blog.jxck.io/entries/2018-07-20/toggle-attribute.html "Element.toggleAttribute | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span></p>

属性の値をトグルをする`Element.prototype.toggleAttribute`について


----

## PWACompat: the Web App Manifest for all browsers  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/07/pwacompat](https://developers.google.com/web/updates/2018/07/pwacompat "PWACompat: the Web App Manifest for all browsers  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">polyfill</span></p>

Web App Manifestから古いSafariやレガシーブラウザ向けにメタ要素を追加するライブラリ。

- [GoogleChromeLabs/pwacompat: PWACompat to bring Web App Manifest to older browsers](https://github.com/GoogleChromeLabs/pwacompat "GoogleChromeLabs/pwacompat: PWACompat to bring Web App Manifest to older browsers")

----

## Operationalizing Node.js for Server Side Rendering – Airbnb Engineering & Data Science – Medium
[medium.com/airbnb-engineering/operationalizing-node-js-for-server-side-rendering-c5ba718acfc9](https://medium.com/airbnb-engineering/operationalizing-node-js-for-server-side-rendering-c5ba718acfc9 "Operationalizing Node.js for Server Side Rendering – Airbnb Engineering & Data Science – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

AirbnbにおけるReactのサーバサイドレンダリングのパフォーマンスについての記事。JavaScriptがどのように非同期処理をしているかやボトルネックとなる場所についてなど


----

## Monthly Web の作り方 2018 年版 | blog.jxck.io
[blog.jxck.io/entries/2018-07-18/how-to-logging-monthly-web.html](https://blog.jxck.io/entries/2018-07-18/how-to-logging-monthly-web.html "Monthly Web の作り方 2018 年版 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">spec</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ウェブ標準に関する仕様や実装の一次情報について。
ブラウザ、WHATWG/W3C、TC39、IETFに関して、それぞれどのような形で情報が公開されているかについてまとめられている。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## GoogleChromeLabs/ndb: ndb is an improved debugging experience for Node.js, enabled by Chrome DevTools
[github.com/GoogleChromeLabs/ndb](https://github.com/GoogleChromeLabs/ndb "GoogleChromeLabs/ndb: ndb is an improved debugging experience for Node.js, enabled by Chrome DevTools")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Puppeteerを使ったNode.jsのデバッガーツール。
Node.jsのアプリに対してChrome開発者ツールでデバッグできる。
`node --inspect`に比べてコンソールパネルでの実行、ブレークポイントの対応、プロファイル周りなどが追加されている。


----

## 普通のHTMLの書き方
[hail2u.net/documents/html-best-practices.html](https://hail2u.net/documents/html-best-practices.html "普通のHTMLの書き方")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">HTML5</span> <span class="jser-tag">document</span> <span class="jser-tag">spec</span></p>

HTMLの避けるべき非推奨な書き方、簡潔な書き方、セマンティック、アクセシビリティを考慮した書き方などについてのドキュメント。
それぞれの項目に悪い例と良い例つきで解説されている。よくある記述の仕様的な解説なども書かれている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## nathan/pax: The fastest JavaScript bundler in the galaxy.
[github.com/nathan/pax](https://github.com/nathan/pax "nathan/pax: The fastest JavaScript bundler in the galaxy.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span></p>

Rust製のJavaScript Bundler


----

## ramhejazi/draxt: draxt.js – NodeList-like/jQuery-like package for File System (node.js)
[github.com/ramhejazi/draxt](https://github.com/ramhejazi/draxt "ramhejazi/draxt: draxt.js – NodeList-like/jQuery-like package for File System (node.js)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsの`fs`を配列などのようにメソッドチェーンで操作できるライブラリ


----

## imbrn/v8n: JavaScript fluent validation library.
[github.com/imbrn/v8n](https://github.com/imbrn/v8n "imbrn/v8n: JavaScript fluent validation library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

メソッドチェーンでバリデーションルールを書けるライブラリ


----
