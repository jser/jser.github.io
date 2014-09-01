---
title: "2014-09-01のJS: Underscore1.7.0、Browserify入門、Gravit"
author: azu
layout: post
date : 2014-09-01T08:19
category: JSer
tags:
    - JavaScript
    - Broserify
    - Design
    - software
    - node-webkit

---

JSer.info #190 - [Underscore](http://underscorejs.org/ "Underscore") 1.7.0がリリースされました。

破壊的な変更も多いですが、主な変更内容はChangeLogに、掲載されてない変更内容は以下のコメントにまとめられています。

- [Change Log](http://underscorejs.org/#changelog "Change Log")
- [Release Underscore 1.7.0 by akre54 · Pull Request #1799 · jashkenas/underscore](https://github.com/jashkenas/underscore/pull/1799#issuecomment-53577944 "Release Underscore 1.7.0 by akre54 · Pull Request #1799 · jashkenas/underscore")

大きな変更としては、` _.template`が[初期化時にdataを受け取らなくなり、常に関数を返すように](https://github.com/jashkenas/underscore/issues/1736 "_.template should not accept data argument · Issue #1736 · jashkenas/underscore")なったこと、`_.extend`の[挙動](https://github.com/jashkenas/underscore/pull/1770)がES6 Object.assignに近いものに変わったことや、ネイティブの`Array.prototype.*`を使わなくなった事による高速化や(疎の配列における)挙動の違い等が含まれています。

今後のリリース方針については以下を参照するといいかと思います。

- [Fix the versioning · Issue #1805 · jashkenas/underscore](https://github.com/jashkenas/underscore/issues/1805 "Fix the versioning · Issue #1805 · jashkenas/underscore")

----

[A Gentle Browserify Walkthrough - Pony Foo](http://blog.ponyfoo.com/2014/08/25/a-gentle-browserify-walkthrough "A Gentle Browserify Walkthrough - Pony Foo")という記事はBrowserifyの入門的な内容について書かれています。

CommonJSとは何かという所からbrowserifyの基本的な使い方、CommonJSを扱えることのメリット等が分かりやすく書かれています。

より詳しくBrowserifyについて知りたい方は[substack/browserify-handbook](https://github.com/substack/browserify-handbook "substack/browserify-handbook")も参照するといいと思います。

----

[Gravit](http://hub.gravit.io/browser/ "Gravit") というnode-webkit製のデザインツールのβ版が公開されています。

[ブラウザで動くバージョン](http://hub.gravit.io/browser/ "Gravit")やソースコードも[quasado/gravit](https://github.com/quasado/gravit "quasado/gravit")にて公開されています。

<div class="kwout" style="text-align: center;"><a href="http://gravit.io/"><img src="http://kwout.com/cutout/8/4r/pz/8pm_bor.jpg" alt="http://gravit.io/" title="Gravit – unlock your design potential." width="579" height="600" style="border: none;" /></a><p style="margin-top: 10px; text-align: center;"><a href="http://gravit.io/">Gravit – unlock your design potential.</a> via <a href="http://kwout.com/quote/84rpz8pm">kwout</a></p></div>

ウェブ技術で作られていて、プロジェクトの構造もキレイにまとまってるのでソースコードを見てみると面白いかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Sencha Touch 2.4 | Blog | Sencha
[www.sencha.com/blog/announcing-sencha-touch-2-4/](http://www.sencha.com/blog/announcing-sencha-touch-2-4/ "Announcing Sencha Touch 2.4 | Blog | Sencha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sencha</span> <span class="jser-tag">ReleaseNote</span></p>

Sencha Touch 2.4リリース。

BlackBerry 10のサポート強化とtoast コンポーネントの追加

----

## Underscore.js
[underscorejs.org/](http://underscorejs.org/ "Underscore.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Underscore 1.7.0 リリース。

Arrayのネイティブ関数では無く独自の実装を使うように変更し高速化、`_.iteratee`がカスタマイズ可能に`_.before`のメソッド追加、`_.extend`の挙動がES6 `Object.assign`にあわせた形へ変更するなど。

&quot;Sparse&quot; arrays、extend、union、template等破壊的な変更も多く含まれている。

- [Release Underscore 1.7.0 by akre54 · Pull Request #1799 · jashkenas/underscore](https://github.com/jashkenas/underscore/pull/1799#issuecomment-53577944 "Release Underscore 1.7.0 by akre54 · Pull Request #1799 · jashkenas/underscore")

----

## CoffeeScript
[coffeescript.org](http://coffeescript.org "CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">ReleaseNote</span></p>

CoffeeScript 1.8.0リリース。

sourcemapのファイル名が.js.mapに変更、CLIの改善、`require("coffee-script/repl")`をrequire出来るように

----

## harmony:specification_drafts [ES Wiki]
[wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#august_24_2014_draft_rev_27](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#august_24_2014_draft_rev_27 "harmony:specification\_drafts \[ES Wiki\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 6 Draft Rev 27リリース。

Array/generator comprehensionsの削除、Array.prototype.sortの実装依存についての明文化等

----

## Dart News &amp; Updates: Dart 1.6 adds support for deferred loading
[news.dartlang.org/2014/08/dart-16-adds-support-for-deferred.html](http://news.dartlang.org/2014/08/dart-16-adds-support-for-deferred.html "Dart News &amp; Updates: Dart 1.6 adds support for deferred loading")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart 1.6リリース。

loadLibraryというDeferred loadingを提供するlibraryが入った。

- [Deferred Loading in Dart | Dart: Structured web apps](https://www.dartlang.org/docs/spec/deferred-loading.html "Deferred Loading in Dart | Dart: Structured web apps")

----

## MooTools - 1.5.1 is out!
[mootools.net/blog/2014/08/29/mootools-1-5-1-release/](http://mootools.net/blog/2014/08/29/mootools-1-5-1-release/ "MooTools - 1.5.1 is out!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

MooTools 1.5.1リリース・

パッケージ周りの改善

----

## Release 1.6.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v1.6.0](https://github.com/jscs-dev/node-jscs/releases/tag/v1.6.0 "Release 1.6.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

コードスタイルチェックツールのjscs 1.6.0リリース。

Googleプリセットの改善やバグ修正等

----

## Ember.js - Ember 1.7.0 and 1.8 Beta Released
[emberjs.com/blog/2014/08/23/ember-1-7-0-released.html](http://emberjs.com/blog/2014/08/23/ember-1-7-0-released.html "Ember.js - Ember 1.7.0 and 1.8 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 1.7.0 と 1.8 Betaリリース

----

## Chromium Blog: Chrome 38 Beta: New primitives for the next-generation web
[blog.chromium.org/2014/08/chrome-38-beta-new-primitives-for-next.html](http://blog.chromium.org/2014/08/chrome-38-beta-new-primitives-for-next.html "Chromium Blog: Chrome 38 Beta: New primitives for the next-generation web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 38βリリース。

picture要素、Map/Set、`for...of`、Symbol、Math周りの追加。

[Network Information API](http://w3c.github.io/netinfo/ "Network Information API")、 [Screen Orientation API](http://www.w3.org/TR/screen-orientation/ "Screen Orientation API")、[Encoding API](http://updates.html5rocks.com/2014/08/Easier-ArrayBuffer---String-conversion-with-the-Encoding-API "Encoding API")でXHRでバイナリを取得しながらデコードが出来るようになるなど。

- [Collecting and Iterating, the ES6 Way - HTML5Rocks Updates](http://updates.html5rocks.com/2014/08/Collecting-and-Iterating-the-ES6-Way "Collecting and Iterating, the ES6 Way - HTML5Rocks Updates")
- [Easier ArrayBuffer &lt;-&gt; String conversion with the Encoding API - HTML5Rocks Updates](http://updates.html5rocks.com/2014/08/Easier-ArrayBuffer---String-conversion-with-the-Encoding-API "Easier ArrayBuffer &lt;-&gt; String conversion with the Encoding API - HTML5Rocks Updates")

----

## Introducing Meteor 0.9.0 and the official Meteor packaging system
[www.meteor.com/blog/2014/08/26/meteor-090-new-packaging-system](https://www.meteor.com/blog/2014/08/26/meteor-090-new-packaging-system "The Meteor blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Meteor 0.9.0リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## Important Announcement Regarding YUI | Yahoo Engineering
[yahooeng.tumblr.com/post/96098168666/important-announcement-regarding-yui](http://yahooeng.tumblr.com/post/96098168666/important-announcement-regarding-yui "Important Announcement Regarding YUI | Yahoo Engineering")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">YUI</span> <span class="jser-tag">ReleaseNote</span></p>

YUIは新規開発終了し、今後はYahoo内部向けの修正に留めるとの事。

- [Yahoo stopping all new development of YUI | Hacker News](https://news.ycombinator.com/item?id=8243523 "Yahoo stopping all new development of YUI | Hacker News")

----

## Unicode-aware regular expressions in ES6 · Mathias Bynens
[mathiasbynens.be/notes/es6-unicode-regex](https://mathiasbynens.be/notes/es6-unicode-regex "Unicode-aware regular expressions in ES6 · Mathias Bynens")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span></p>

ES6で導入された正規表現の`u`フラグについての解説とES5でも使えるようにするtranspilerについて。

正規表現でユニコード文字を正しく扱うためのフラグ。

ES5やES6でのユニコード文字の扱いについては以下のスライドと動画で詳しく解説されてる。

- [Hacking with Unicode // Speaker Deck](https://speakerdeck.com/mathiasbynens/hacking-with-unicode "Hacking with Unicode // Speaker Deck")

----

## Virtual DOMを持つMV*ライブラリのmercuryについて | Web Scratch
[efcl.info/2014/08/28/mercury/](http://efcl.info/2014/08/28/mercury/ "Virtual DOMを持つMV\*ライブラリのmercuryについて | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">MVC</span></p>

mercuryのModel(State)、View(Virtual DOM)、Controller(Event)について。

モジュールを組み合わせた構造と関数型プログラミング的なアプローチがベースのライブラリ

----

## A Gentle Browserify Walkthrough - Pony Foo
[blog.ponyfoo.com/2014/08/25/a-gentle-browserify-walkthrough](http://blog.ponyfoo.com/2014/08/25/a-gentle-browserify-walkthrough "A Gentle Browserify Walkthrough - Pony Foo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">tutorial</span></p>

Browserifyについての丁寧なチュートリアル。

CommonJSとは何か、browserifyの基本的な使い方、利点としてnpmのモジュールが使える点やCJS以外のモジュールをbrowserify-shimで扱う事について等

- [Browserify All The Things // Speaker Deck](https://speakerdeck.com/bevacqua/browserify-all-the-things "Browserify All The Things // Speaker Deck")
- [substack/browserify-handbook](https://github.com/substack/browserify-handbook "substack/browserify-handbook")

----

## Journey from browserify to webpack — Medium
[medium.com/@tomchentw/why-webpack-is-awesome-9691044b6b8e](https://medium.com/@tomchentw/why-webpack-is-awesome-9691044b6b8e "Journey from browserify to webpack — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

webpackを使ったビルドについて。 browserifyとの比較

webpackがデフォルトで webpack-dev-serverや差分コンパイル、bower統合、js以外を読み込めるloaderを持ってる点について書かれている

----

## aster
[rreverser.com/aster-ast-based-code-builder/](http://rreverser.com/aster-ast-based-code-builder/ "aster")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScript ASTを処理するビルドツール。

GruntやGulp等はtaskごとにパースと生成を繰り返すため非効率な部分がある。

asterはASTに対して変換の処理をパイプラインで行うため無駄な処理が減る。

- [asterjs/aster](https://github.com/asterjs/aster "asterjs/aster")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Forward JS
[forwardjs.com/](http://forwardjs.com/ "Forward JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

Forward JSの動画が公開されている

----

## JavaScript Memory Management Masterclass // Speaker Deck
[speakerdeck.com/addyosmani/javascript-memory-management-masterclass](https://speakerdeck.com/addyosmani/javascript-memory-management-masterclass "JavaScript Memory Management Masterclass // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">スライド</span></p>

JavaScriptでのメモリリークとそもそも何故起きるのかについてのスライド。 

DOM leakやV8のメモリ管理の方法、世代別GC、DevToolsを使っての見つけ方、Performance Toolsの使い方についてなどかなり詳しく紹介されている。

- [JavaScript Memory Management Masterclass のメモ | wIssue Note](http://efcl.wordpress.com/2014/08/31/javascript-memory-management-masterclass-%e3%81%ae%e3%83%a1%e3%83%a2/ "JavaScript Memory Management Masterclass のメモ | wIssue Note")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Run CasperJS scripts online - CasperBox
[www.casperbox.com/](https://www.casperbox.com/ "Run CasperJS scripts online - CasperBox")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">webservice</span> <span class="jser-tag">library</span></p>

CaperJSのコードをオンラインで書いて実行、REST APIとAPIを使って実行出来るライブラリを提供してるサービス

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mathiasbynens/regexpu
[github.com/mathiasbynens/regexpu](https://github.com/mathiasbynens/regexpu "mathiasbynens/regexpu")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span> <span class="jser-tag">Tools</span></p>

ES6の正規表現の`u`フラグをES5でも使えるように変換するtranspiler

----

## Chartist - Simple responsive charts
[gionkunz.github.io/chartist-js/](http://gionkunz.github.io/chartist-js/ "Chartist - Simple responsive charts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">library</span></p>

SVGベースのレスポンシブなグラフライブラリ。

media queriesを使って指定

----

## twistdigital/es6-promisify
[github.com/twistdigital/es6-promisify](https://github.com/twistdigital/es6-promisify "twistdigital/es6-promisify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

nodeスタイルのコールバックを受け取る関数のPromiseラッパーを作るモジュール。

----

## Gravit – unlock your design potential.
[gravit.io/](http://gravit.io/ "Gravit – unlock your design potential.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">illust</span> <span class="jser-tag">software</span></p>

Illustratorライクなデザインツール。

ドローやレイヤー等の機能を持ってる

ブラウザで動かすこともできるオープンソースなアプリ。

<a href='https://github.com/quasado/gravit'>https://github.com/quasado/gravit</a>

----

## Cheerp homepage
[leaningtech.com/cheerp/](http://leaningtech.com/cheerp/ "Cheerp homepage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">C++</span> <span class="jser-tag">JavaScript</span></p>

C++からJavaScriptへコードへのコードコンパイラ。

LLVMを使用、DOM等扱うC++のラッパライブラリ的なのを持っている

----
<h1 class="site-genre">書籍関係</h1>

----

## O&#x27;Reilly Japan - モダンWeb
[www.oreilly.co.jp/books/9784873116921/](http://www.oreilly.co.jp/books/9784873116921/ "O&#x27;Reilly Japan - モダンWeb")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">book</span></p>

2014年09月10日 発売

----

## 大規模開発でも小規模開発でも使える TypeScript実践入門：書籍案内｜技術評論社
[gihyo.jp/book/2014/978-4-7741-6711-4](http://gihyo.jp/book/2014/978-4-7741-6711-4 "大規模開発でも小規模開発でも使える TypeScript実践入門：書籍案内｜技術評論社")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span> <span class="jser-tag">windows</span></p>

2014年9月12日発売

TypeScriptについての書籍

----

## The Pragmatic Bookshelf | Dart 1 for Everyone
[www.pragprog.com/book/csdart1/dart-1-for-everyone](https://www.pragprog.com/book/csdart1/dart-1-for-everyone "The Pragmatic Bookshelf | Dart 1 for Everyone")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">book</span></p>

2014年10月10日発売

Google Dartについての書籍

----

## Manning: Firefox OS in Action
[www.manning.com/jongboom/](http://www.manning.com/jongboom/ "Manning: Firefox OS in Action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">OS</span> <span class="jser-tag">book</span></p>

2015年春発売

Firefox OS本

----

## Amazon: JavaScript逆引きレシピ jQuery対応
[www.amazon.co.jp/dp/4798135461?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4798135461?tag=amazon0abac-22 "Amazon: JavaScript逆引きレシピ jQuery対応")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2014年8月29日発売

電子版も同時リリース

- [JavaScript逆引きレシピ jQuery対応（9784798139470）：翔泳社の電子書籍](http://www.shoeisha.co.jp/ebooks/detail/9784798139470 "JavaScript逆引きレシピ jQuery対応（9784798139470）：翔泳社の電子書籍")

----