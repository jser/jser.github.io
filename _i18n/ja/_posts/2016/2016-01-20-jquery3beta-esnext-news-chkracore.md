---
title: "2016-01-20のJS: jQuery 3.0β、ES.next News、ChakraCore OSS"
author: azu
layout: post
date : 2016-01-20T22:57
category: 
tags:
    - 

---

JSer.info #262

----
<h1 class="site-genre">ヘッドライン</h1>

----

## jQuery 3.0 Beta Released | Official jQuery Blog
[blog.jquery.com/2016/01/14/jquery-3-0-beta-released/](http://blog.jquery.com/2016/01/14/jquery-3-0-beta-released/ "jQuery 3.0 Beta Released | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.0βリリース。
jQuery10周年を記念してのリリース

----

## Ember.js - Ember.js 2.3 and 2.4 Beta Released
[emberjs.com/blog/2016/01/15/ember-2-3-released.html](http://emberjs.com/blog/2016/01/15/ember-2-3-released.html "Ember.js - Ember.js 2.3 and 2.4 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 2.3リリース。
FastBootに`visit`メソッドの追加

----

## Release 6.3 “Pro rege et lege” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/6.3.0](https://github.com/postcss/autoprefixer/releases/tag/6.3.0 "Release 6.3 “Pro rege et lege” · postcss/autoprefixer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

Autoprefixer 6.3リリース。
Grid Layoutのサポート、自前で用意したUA別のデータからブラウザの種類を決められる機能の追加

----

## axios/CHANGELOG.md at v0.9.0 · mzabriskie/axios
[github.com/mzabriskie/axios/blob/v0.9.0/CHANGELOG.md](https://github.com/mzabriskie/axios/blob/v0.9.0/CHANGELOG.md "axios/CHANGELOG.md at v0.9.0 · mzabriskie/axios")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">XHR</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

axios 0.9.0リリース。
XDomainRequestの対応改善、`adapter`プロパティの追加など

----

## MooTools Blog: 1.6.0 is out!
[mootools.net/blog/2016/01/14/mootools-1-6-0-release](http://mootools.net/blog/2016/01/14/mootools-1-6-0-release "MooTools Blog: 1.6.0 is out!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MooTools 1.6.0リリース。
Promises/A+互換の`Class.Thenable`を追加。
次回のメジャーアップデートではIE11+のみのサポートとなる。
また`Array.from`はES6と名前が被っているためリネームされる

----

## ES.next News: The 5 best ECMAScript links of the week
[esnextnews.com/](http://esnextnews.com/ "ES.next News: The 5 best ECMAScript links of the week")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">mail</span></p>

ES.nextについての週刊メルマガ。
JavaScriptの補完的な感じ。
by Dr.Axel Rauschmayer and Johannes Weber.

- [ES.next News: The 5 best ECMAScript links of the week](http://esnextnews.com/ "ES.next News: The 5 best ECMAScript links of the week")

----

## ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/01/13/chakracore-now-open/](https://blogs.windows.com/msedgedev/2016/01/13/chakracore-now-open/ "ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">JavaScript</span></p>

MSEdgeのJavaScriptエンジンであるChakraのCore部分がオープンソースとして公開された。

- [Microsoft/ChakraCore](https://github.com/Microsoft/Chakracore "Microsoft/ChakraCore")

----

## Enable Node.js to run with Microsoft&#x27;s ChakraCore engine by kunalspathak · Pull Request #4765 · nodejs/node
[github.com/nodejs/node/pull/4765](https://github.com/nodejs/node/pull/4765 "Enable Node.js to run with Microsoft's ChakraCore engine by kunalspathak · Pull Request #4765 · nodejs/node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">issue</span></p>

Node.jsにChakraCoreビルドを追加するPull Request

- [Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/01/19/nodejs-chakracore-mainline/ "Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog")

----

## Renaming jade -&gt; pug · Issue #2184 · pugjs/jade
[github.com/pugjs/jade/issues/2184](https://github.com/pugjs/jade/issues/2184 "Renaming jade -> pug · Issue #2184 · pugjs/jade")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span> <span class="jser-tag">node.js</span></p>

Jadeはpugにリネームされる

----
<h1 class="site-genre">アーティクル</h1>

----

## babel-plugin-typecheck を使って flowtype 文法で書かれたJSをランタイムチェックする - Qiita
[qiita.com/mizchi/items/30a5f9560e86e0d5ab31](http://qiita.com/mizchi/items/30a5f9560e86e0d5ab31 "babel-plugin-typecheck を使って flowtype 文法で書かれたJSをランタイムチェックする - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

FlowTypeの型定義構文を使ってランタイムチェックを行うBabelプラグインについて

----

## Browserify VS Webpack - JS Drama
[blog.namangoel.com/browserify-vs-webpack-js-drama](http://blog.namangoel.com/browserify-vs-webpack-js-drama "Browserify VS Webpack - JS Drama")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span></p>

Browserifyとwebpackの思想の違い、静的リソースの扱い、どちらをどういう理由で選ぶべきかについて

----

## React.js Best Practices for 2016 | @RisingStack
[blog.risingstack.com/react-js-best-practices-for-2016/](https://blog.risingstack.com/react-js-best-practices-for-2016/ "React.js Best Practices for 2016 | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

Reactの使い方、データの持ち方、テストなどのプラクティス

----

## JSといえばjQueryだったWebデザイナーが、Reactを1年間使って感じたメリット | dwango creators&#x27; blog（ドワンゴクリエイターズブログ）
[creator.dwango.co.jp/3413.html](http://creator.dwango.co.jp/3413.html "JSといえばjQueryだったWebデザイナーが、Reactを1年間使って感じたメリット | dwango creators' blog（ドワンゴクリエイターズブログ）")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">design</span></p>

デザイナーから見たReactについて

----

## Enumify: better enums for JavaScript
[www.2ality.com/2016/01/enumify.html](http://www.2ality.com/2016/01/enumify.html "Enumify: better enums for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

classを使ったEnumのライブラリについて

- [rauschma/enumify](https://github.com/rauschma/enumify "rauschma/enumify")


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## MicheleBertoli/css-in-js - JavaScript
[github.com/MicheleBertoli/css-in-js](https://github.com/MicheleBertoli/css-in-js "MicheleBertoli/css-in-js - JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span></p>

React系のCSS in JSライブラリの比較まとめ

----

## cheeaun/javascript-error-logging
[github.com/cheeaun/javascript-error-logging](https://github.com/cheeaun/javascript-error-logging "cheeaun/javascript-error-logging")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webservice</span> <span class="jser-tag">debug</span></p>

JavaScriptのerror loggingサービスのまとめ

----

## Progressive Web Apps | Web Fundamentals - Google Developers
[developers.google.com/web/progressive-web-apps](https://developers.google.com/web/progressive-web-apps "Progressive Web Apps | Web Fundamentals - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span></p>

Progressive Web AppについてのGoogleのまとめページ。
Progressive Web Appとは何かについて書かれている。

----

## thejameskyle/babel-handbook
[github.com/thejameskyle/babel-handbook](https://github.com/thejameskyle/babel-handbook "thejameskyle/babel-handbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">tutorial</span></p>

Babelのセットアップ方法やプラグイン開発について書かれたハンドブック

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ariporad/pirates
[github.com/ariporad/pirates](https://github.com/ariporad/pirates "ariporad/pirates")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">babel</span></p>

`require.extensions`のhookを扱うライブラリ。
一つの拡張子に複数のhookを行う部分を管理する。

----

## kolodny/deact - JavaScript
[github.com/kolodny/deact](https://github.com/kolodny/deact "kolodny/deact - JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

TemplateStringを使ってJSXライクな書き方ができるテンプレートエンジン。

----

## Jotted — Showcase self-hosted HTML, CSS and JavaScript demos, with editable source
[ghinda.net/jotted/](https://ghinda.net/jotted/ "Jotted — Showcase self-hosted HTML, CSS and JavaScript demos, with editable source")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JSBinとかJSFiddleのような形式でHTML/CSS/JSを埋め込み表示出来るライブラリ

----

