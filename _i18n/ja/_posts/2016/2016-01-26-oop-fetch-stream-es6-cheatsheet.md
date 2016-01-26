---
title: "2016-01-26のJS: JavaScriptとOOP、Fetch with Stream、ES6チートシート"
author: azu
layout: post
date : 2016-01-26T18:18
category: JSer
tags:
    - OOP
    - Fetch
    - JavaScript
    - ES6

---

JSer.info #263 - [OO Relationships — Medium](https://medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162 "OO Relationships — Medium")ではJavaScriptとオブジェクト指向プログラミングについて書かれています。

[Allen Wirfs-Brock](https://twitter.com/awbjs "Allen Wirfs-Brock")さんの以下の発言が発端です(今も続いてる)

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">JS devs: do you use abstraction? What word do you use for “an open set of objects that share a common interface and implementation”?</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/689506114807857152">January 19, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">JS Devs: What  do you call “an open set of objects that share a common interface and implementation”?</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/689513929546928128">January 19, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ES6で追加された`class`を踏まえprototype-basedであるJavaScriptにおけるオブジェクト同士の関係性について書かれています。
実践的な話というよりは概念的な話ですが興味深い内容になっています。

----

[2016 - the year of web streams - JakeArchibald.com](https://jakearchibald.com/2016/streams-ftw/ "2016 - the year of web streams - JakeArchibald.com")ではChromeでフラグ付きの[WHATWG Stream](https://streams.spec.whatwg.org/ "Streams")について紹介されています。

また[Fetch API](https://fetch.spec.whatwg.org/ "Fetch")とStream APIを組み合わせて使うことで、
データを取得しながら処理をすることで、表示までの動作がどのように変わるのかについて紹介されています。

----

[ECMAScript 2015 by David Leonard](http://slides.com/drksephy/ecmascript-2015#/ "ECMAScript 2015 by David Leonard")では[DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")のチートシートを元にしたES6について紹介されています。

ES6とES5を[比較](http://es6-features.org/)した内容で、具体的にどの部分が異なるのかが紹介されています。

----

:information_source:

Podcastやサイト紹介などをやっている[The Changelog](https://changelog.com/ "The Changelog - Open source moves fast. Keep up.")に[Ping](https://github.com/thechangelog/ping "Ping")というリポジトリがあり、
これと同じものがJSer.infoにもあったら利用したいかの意見を募集中です。

[Ping](https://github.com/thechangelog/ping "Ping")は紹介して欲しい記事を書いたり、意見を書いたり、Changelogだとこの人をpodcastに呼んでほしいなどの要望を書くGitHub Issueです。
これに関する意見などありましたらGitterに書いてください。

[![Gitter chat](https://badges.gitter.im/jser/jser.info.png)](https://gitter.im/jser/jser.info)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v2.9.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v2.9.0](https://github.com/jscs-dev/node-jscs/releases/tag/v2.9.0 "Release v2.9.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS v2.9.0リリース。
`requireCapitalizedConstructors`ルールの追加、ルールの更新、バグ修正など


----

## Node v5.5.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.5.0/](https://nodejs.org/en/blog/release/v5.5.0/ "Node v5.5.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v5.5.0リリース。
REPLでも`--require`が動作するように、`fs.createWriteStream`で`autoClose`オプションをサポートするなど

----

## Release ES2016 Draft 2016-01-20 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20160120](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20160120 "Release ES2016 Draft 2016-01-20 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2016-01-20リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## Simulating Website Thumbnails using Iframes — Medium
[medium.com/@jamesfuthey/simulating-the-creation-of-website-thumbnail-screenshots-using-iframes-7145269891db](https://medium.com/@jamesfuthey/simulating-the-creation-of-website-thumbnail-screenshots-using-iframes-7145269891db "Simulating Website Thumbnails using Iframes — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span></p>

iframeを使ってサイトのサムネイル的な表示をする方法について

----

## Understand promises before you start using async/await — Medium
[medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8](https://medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8 "Understand promises before you start using async/await — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

async/awaitを使う前にPromiseについて理解しようという話

----

## OO Relationships — Medium
[medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162](https://medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162 "OO Relationships — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">OOP</span></p>

JavaScriptとオブジェクト指向プログラミングについて。
static/dynamic dispatch、prototypeベース、縦/横の継承、
class、mixin、traits、ダックタイピング、compositionなどについて

----

## 2016 - the year of web streams - JakeArchibald.com
[jakearchibald.com/2016/streams-ftw/](https://jakearchibald.com/2016/streams-ftw/ "2016 - the year of web streams - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Fetch with Streamについて。
readable stream、transform streamを使ったMPEG to GIFの例

----

## JavaScriptのコードを分解してよく使われてる機能を分析する | Web Scratch
[efcl.info/2016/01/22/es-usage-rate/](http://efcl.info/2016/01/22/es-usage-rate/ "JavaScriptのコードを分解してよく使われてる機能を分析する | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

コードをパースして機能ごとの出現回数を調べるツールを書いたという話

----

## rollup.js - Rollupがちょうどいい感じ - Qiita
[qiita.com/cognitom/items/e3ac0da00241f427dad6](http://qiita.com/cognitom/items/e3ac0da00241f427dad6 "rollup.js - Rollupがちょうどいい感じ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span></p>

Bundlerであるrollup.jsについて。
x to ES6をしてから変換する話、Tree Shaking、基本的な使い方や設定について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Cycle.js Fundamentals - Course by @andrestaltz @eggheadio
[egghead.io/series/cycle-js-fundamentals](https://egghead.io/series/cycle-js-fundamentals "Cycle.js Fundamentals - Course by @andrestaltz @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">動画</span></p>

Cycle.js作者によるCycle.jsとRxJSについてのスクリーンキャスト。

----

## ECMAScript 2015 by David Leonard
[slides.com/drksephy/ecmascript-2015#/](http://slides.com/drksephy/ecmascript-2015#/ "ECMAScript 2015 by David Leonard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">スライド</span></p>

ES5でのややこしい書き方、それをES6で書いた場合にどうなるかなどについて書かれたスライド。
アノテーションでどの部分が違うのかがわかりやすく表示されている。

- [DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## DrkSephy/es6-cheatsheet
[github.com/DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6チートシート。
ES5での書き方とES6での書き方を比較してる形

----

## Pa11y - Your automated accessibility testing pal
[pa11y.org/](http://pa11y.org/ "Pa11y - Your automated accessibility testing pal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">Tools</span></p>

アクセシビリティチェック as a Service。
毎日実行し結果を集計し、ダッシュボードで見ることが出来る。
またCLIからチェックすることも出来る

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Umbrella JS
[umbrellajs.com/](http://umbrellajs.com/ "Umbrella JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

jQueryのようなDOM操作やAjax周りの機能を提供する小さなライブラリ

----

## stomita/clipboard-hook
[github.com/stomita/clipboard-hook](https://github.com/stomita/clipboard-hook "stomita/clipboard-hook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">クリップボード</span></p>

要素ごとのイベントを移譲することで、全体としての`cut`/`copy`/`paste`イベントに対するhookを書けるライブラリ

----

## Jam3/devtool: runs Node.js programs through Chromium DevTools
[github.com/Jam3/devtool](https://github.com/Jam3/devtool "Jam3/devtool: runs Node.js programs through Chromium DevTools")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">Electron</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

Electron上でNode.jsを実行し開発者ツールでデバッグ出来るツール。
コマンドラインでNode.jsのファイルを指定するだけで実行できる。

----

## skerit/janeway: A curses-based console for node.js
[github.com/skerit/janeway](https://github.com/skerit/janeway "skerit/janeway: A curses-based console for node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">debug</span></p>

curses/blessedベースのJavaScript REPL。
ブラウザの開発者ツールのようにインタラクティブな動作を目的としている

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript Master - O&#x27;Reilly Media
[shop.oreilly.com/product/9780994346933.do](http://shop.oreilly.com/product/9780994346933.do "JavaScript Master - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016年3月発売

----
