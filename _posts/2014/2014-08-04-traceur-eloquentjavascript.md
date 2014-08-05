---
title: "2014-08-04のJS: traceur-compiler入門、Eloquent JavaScript第二版"
author: azu
layout: post
tags:
    - ES6
    - traceur
    - book
    - JSer.info

---

JSer.info #186 - [traceur-compiler 入門 - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2014/07/31/093041 "traceur-compiler 入門 - from scratch") という記事では、ES6をES5(要runtime)に変換するツールである[Traceur](https://github.com/google/traceur-compiler "Traceur")について詳しく書かれています。
Traceur Compilerの基本的な使い方からES6のコード例などについて書かれています。

ES6のサンプルコードは[es6features](https://github.com/lukehoban/es6features "es6features")がよくまとまっていますが、以前試した時もTraceurで結構扱えていたのでこの辺も試してみるといいかもしれません。

* [ECMAScript6についてes6featuresで学んだ \| Web Scratch](http://efcl.info/2014/0323/res3750/ "ECMAScript6についてes6featuresで学んだ \| Web Scratch")

また、[Using ECMAScript 6 today](http://www.2ality.com/2014/08/es6-today.html "Using ECMAScript 6 today")という記事ではES6で入った機能の概要や関連リソースの紹介がされています。

[es6-tools](https://github.com/addyosmani/es6-tools "es6-tools")にES6関係のツールはまとまっていますが最初にみても迷うと思います。
上記の記事では主要なツールについてがまとまっているので興味をもった人は見ておくといいかもしれません。

---

英語圏では著名な無料で読めるJavaScript書籍である[Eloquent JavaScript](http://eloquentjavascript.net/ "Eloquent JavaScript")の第二版がリリースされました。

CC-BY-NCでリリースされていてソースコードも[marijnh/Eloquent-JavaScript](https://github.com/marijnh/Eloquent-JavaScript "marijnh/Eloquent-JavaScript")で公開されています。

- [プログラミング入門書『Eloquent JavaScript, 2nd Edition』のオンライン版が無料で公開：CodeZine](http://codezine.jp/article/detail/7971 "プログラミング入門書『Eloquent JavaScript, 2nd Edition』のオンライン版が無料で公開：CodeZine")

自分も[JavaScript Promiseの本](http://azu.github.io/promises-book/ "JavaScript Promiseの本")で同じような仕組みを実装しましたが、[Eloquent JavaScript](http://eloquentjavascript.net/ "Eloquent JavaScript")のオンライン版ではコードがその場で実行して見られるようになっています。

![interactive](http://gyazo.com/8df4fdd8333d98bfa91ea786ca1cd7ca.gif)

同じく無料でオンライン版を読むことができる[Speaking JavaScript](http://speakingjs.com/es5/ "Speaking JavaScript")と共にオススメです。

---

# お知らせ

今サイト上で見てる人は気づいてると思いますが、JSer.infoがTumblrからGitHub Pagesに移行しました。

技術的な背景など詳しくは[JSer.infoをTumblrからGitHub Pagesに移行しました - JSer.info](http://jser.info/2014/08/03/renewal/ "JSer.infoをTumblrからGitHub Pagesに移行しました - JSer.info")に書いてあります。

GitHub上にソースがそのままあるため、記事の修正等が[jser/jser.github.io](https://github.com/jser/jser.github.io "jser/jser.github.io")へ直接送れるようになっています。

今後ともよろしくお願いします。

---

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Scala.js 0.5.3
[www.scala-js.org/news/2014/07/30/announcing-scalajs-0.5.3/](http://www.scala-js.org/news/2014/07/30/announcing-scalajs-0.5.3/ "Announcing Scala.js 0.5.3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">scala</span> <span class="jser-tag">ReleaseNote</span></p>

Scala.js 0.5.3 リリース。

パフォーマンスの改善

----

## V8 Memory Corruption and Stack Overflow (fixed in Node v0.8.28 and v0.10.30)
[blog.nodejs.org/2014/07/31/v8-memory-corruption-stack-overflow/](http://blog.nodejs.org/2014/07/31/v8-memory-corruption-stack-overflow/ "V8 Memory Corruption and Stack Overflow (fixed in Node v0.8.28 and v0.10.30)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">セキュリティ</span></p>

Node 0.10.xと0.8.xのsecurity fix.

----

## Vue.js 0.10.6, and what&#x27;s next - vue.js
[vuejs.org/2014/07/29/vue-next/](http://vuejs.org/2014/07/29/vue-next/ "Vue.js 0.10.6, and what&#x27;s next - vue.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Vue.js 0.10.6リリース。

Vue-nextについても書かれている。

スクラッチで書きなおしている理由として、デザインの問題とコードの質の改善を上げてる。

----

## Brackets 0.42 Release (Themes!) – Brackets Blog
[blog.brackets.io/2014/08/01/brackets-0-42-release-themes/](http://blog.brackets.io/2014/08/01/brackets-0-42-release-themes/ "Brackets 0.42 Release (Themes\!) – Brackets Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">IDE</span> <span class="jser-tag">ReleaseNote</span></p>

Brackets 0.42リリース。

言語切替とテーマのサポート

----
<h1 class="site-genre">アーティクル</h1>

----

## JavaScript and V8 TurboFan
[ariya.ofilabs.com/2014/08/javascript-and-v8-turbofan.html](http://ariya.ofilabs.com/2014/08/javascript-and-v8-turbofan.html "JavaScript and V8 TurboFan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span></p>

V8にlandedしたばかりの新しいOptimizing compilerであるTurboFanについての解説。

Crankshaftの後任的なものでまだ開発が始まったばかり

- [\[v8\] r22709 committed - Land the Fan (disabled)... - Google グループ](https://groups.google.com/forum/#!msg/v8-dev/ab8V5Z58_70/5-05DvysCt8J "\[v8\] r22709 committed - Land the Fan (disabled)... - Google グループ")

----

## 3 New JavaScript APIs You May Want to Follow
[www.sitepoint.com/3-new-javascript-apis-may-want-follow/](http://www.sitepoint.com/3-new-javascript-apis-may-want-follow/ "3 New JavaScript APIs You May Want to Follow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">JavaScript</span></p>

最近ドラフトがリリースされたWeb Alarms API, Presentation API, Standby APIについて

----

## Event listeners popup, @media sidebar, Cubic bezier editor + more – Firefox Developer Tools Episode 33 ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2014/07/event-listeners-popup-media-sidebar-cubic-bezier-editor-more-firefox-developer-tools-episode-33/](https://hacks.mozilla.org/2014/07/event-listeners-popup-media-sidebar-cubic-bezier-editor-more-firefox-developer-tools-episode-33/ "Event listeners popup, @media sidebar, Cubic bezier editor + more – Firefox Developer Tools Episode 33 ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">tools</span></p>

Firefox33に入る開発者ツールの機能紹介。

DOMから関連するイベントリスナーの表示、media queryのルール表示、イージングエディタ、コマンドの追加、min.jsをデバッグの対象外にする機能等

----

## Using ECMAScript 6 today
[www.2ality.com/2014/08/es6-today.html](http://www.2ality.com/2014/08/es6-today.html "Using ECMAScript 6 today")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

今日から使えるES6について。

ES6の機能のハイライトやライブラリやツール、Traceur等のTranspilerについて。

----


## traceur-compiler 入門 - from scratch
[yosuke-furukawa.hatenablog.com/entry/2014/07/31/093041](http://yosuke-furukawa.hatenablog.com/entry/2014/07/31/093041 "traceur-compiler 入門 - from scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tools</span> <span class="jser-tag">google</span></p>

traceur-compilerについての解説。

ES6のコードをES5で実行出来るように変換(要runtime)、対応してるES6の構文、ExperimentalなES7の機能、メリット・デメリット、類似ツールについて。

----

## Atom Shell vs Node-Webkit - 牛角堂
[blog.iwege.com/posts/atom-shell-vs-node-webkit.html](http://blog.iwege.com/posts/atom-shell-vs-node-webkit.html "Atom Shell vs Node-Webkit - 牛角堂")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">atom</span> <span class="jser-tag">node-webkit</span></p>

Atom Shellとnode-webkitの比較(中国語)

entry-pointの違い、Chromiumアップデートの対応(ビルドシステム)、マルチコンテキスト、プロセス分離とコミュニケーション、パッケージ管理などについてよくまとまってる。

----

## EcmaScript 6 Template Strings | mozintern
[mozintern.wordpress.com/2014/07/31/ecmascript-6-template-strings-2/](http://mozintern.wordpress.com/2014/07/31/ecmascript-6-template-strings-2/ "EcmaScript 6 Template Strings \| mozintern")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span></p>

Firefox34あたりで入るTemplate Stringsについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## AngularJS入門の巻
[www.slideshare.net/itokami1123/angularjs-34533999](http://www.slideshare.net/itokami1123/angularjs-34533999 "AngularJS入門の巻")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">スライド</span></p>

AngularJSのデータバインディング、モジュール、スコープとデータの反映についてのスライド。

----
<h1 class="site-genre">サイト、サービス</h1>

----

## CSS Triggers...
[csstriggers.com/](http://csstriggers.com/ "CSS Triggers...")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">検索</span> <span class="jser-tag">まとめ</span></p>

CSSプロパティ別にreflowやrepaintの発生、Compositeが可能かどうかが一覧出来る。

Chrome DevToolsで調べた結果を元にしてる。

- [Aerotwist - CSS Triggers](http://aerotwist.com/blog/css-triggers/ "Aerotwist - CSS Triggers")

----

## Opinionated AngularJS styleguide for teams
[toddmotto.com/opinionated-angular-js-styleguide-for-teams/](http://toddmotto.com/opinionated-angular-js-styleguide-for-teams/ "Opinionated AngularJS styleguide for teams")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span></p>

AngularJSのコーディングスタイルガイド。

- [AngularJS styleguide 日本語訳 - AngularJS Ninja](http://angularjsninja.com/blog/2014/07/29/angularjs-styleguide-in-Japanese/ "AngularJS styleguide 日本語訳 - AngularJS Ninja")

----

## Highlights from recent Chromium, Blink, Skia and v8 commits
[commits.peter.sh/](http://commits.peter.sh/ "Highlights from recent Chromium, Blink, Skia and v8 commits")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">blink</span> <span class="jser-tag">V8</span> <span class="jser-tag">git</span></p>

Chromium,Blink,Skia,V8のコミットハイライトをまとめてるpeterさんのサイト。

RSSも追加された

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## flerro/jop
[github.com/flerro/jop](https://github.com/flerro/jop "flerro/jop")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

Node.js製のJSONを扱うコマンドラインツール。

整形表示、データのフィルタリング、カウント、グループング、変換等。jq的なツール

----

## facebook/immutable-js
[github.com/facebook/immutable-js](https://github.com/facebook/immutable-js "facebook/immutable-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">library</span></p>

immutableなVector、Map、Set等を提供してくれるライブラリ。

それぞれ同名のオブジェクトと同じメソッドを提供してくれるのと、遅延シーケンスに対応してる。

ES6で書かれていて、変換したものを配布している。

----

## DOM Event Delegation without jQuery | Matt Andrews
[mattandre.ws/2014/08/small-beautiful-dom-delegation/](https://mattandre.ws/2014/08/small-beautiful-dom-delegation/ "DOM Event Delegation without jQuery \| Matt Andrews")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存がないシンプルなDOM delegateライブラリ。

elementを取って、そこに対してイベントを設定出来る

- [ftlabs/ftdomdelegate](https://github.com/ftlabs/ftdomdelegate "ftlabs/ftdomdelegate")

----
<h1 class="site-genre">書籍関係</h1>

----

## Eloquent JavaScript
[eloquentjavascript.net/](http://eloquentjavascript.net/ "Eloquent JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Eloquent JavaScript第二版がリリースされた

----

## Amazon: 入門Backbone.js (Programmer&#x27;s SELECTION): James Sugrue
[www.amazon.co.jp/dp/479813712X?tag=amazon0abac-22](http://www.amazon.co.jp/dp/479813712X?tag=amazon0abac-22 "Amazon: 入門Backbone.js (Programmer&#x27;s SELECTION): James Sugrue")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">翻訳</span> <span class="jser-tag">book</span></p>

2014年8月29日発売

<a href='http://www.apress.com/9781430263340'>http://www.apress.com/9781430263340</a> の翻訳本

----
