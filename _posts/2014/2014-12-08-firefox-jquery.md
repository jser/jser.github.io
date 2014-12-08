---
title: "2014-12-08のJS: Firefox34、QUnit 1.16、ES7 Async Generator"
author: azu
layout: post
date : 2014-12-08T19:47
category: JSer
tags:
    - Firefox
    - testing
    - webpack
    - ES7
    - 非同期

---

JSer.info #205 - [Firefo 34.0](https://www.mozilla.org/en-US/firefox/34.0/releasenotes/ "Firefox — Notes (34.0) — Mozilla")がリリースされました。

Firefox開発者ツールにlocalStorageの編集機能、jQuery eventsに対応、`console.table()`のサポート、[パフォーマンスツール](https://developer.mozilla.org/ja/docs/Tools/Performance "パフォーマンスツール")等が入っていて、詳しくは以下の記事を参照して下さい。

- [WebIDE, Storage inspector, jQuery events, iframe switcher + more – Firefox Developer Tools Episode 34 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2014/09/webide-storage-inspector-jquery-events-iframe-switcher-more-firefox-developer-tools-episode-34/ "WebIDE, Storage inspector, jQuery events, iframe switcher + more – Firefox Developer Tools Episode 34 ✩ Mozilla Hacks – the Web developer blog")

CSS Fonts Level 3の実験的サポート、template stringsなど[色々なES6の機能](https://developer.mozilla.org/ja/Firefox/Releases/34#JavaScript "JavaScript")が実装されています。

- [Firefox 34 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/34 "Firefox 34 for developers - Mozilla | MDN")


----

JavaScriptテストライブラリの[QUnit 1.16.0](https://github.com/jquery/qunit/blob/1.16.0/History.md "1.16.0")がリリースされました。

メソッドのリファクタリング、`done()`スタイルの非同期テストサポート、Promiseテストのサポートなど[QUnit 2.x](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x")に向けての色々な変更が入っています。
どのような部分が2.0で変わっていくのかについては[QUnit 2.xで変わること](http://azu.github.io/slide/chatwork/qunit2.html "QUnit 2.xで変わること")というスライドを書いたのでこちらを見るといいかもしれません。

----

[▶ Netflix JavaScript Talks - Version 7: The Evolution of JavaScript - YouTube](https://www.youtube.com/watch?v=DqMFX91ToLw "▶ Netflix JavaScript Talks - Version 7: The Evolution of JavaScript - YouTube") という発表では[ES7のAsynchronous Generators](https://github.com/jhusain/asyncgenerator "Asynchronous Generators for ES7")について仕様策定者でもある[@jhusain](https://twitter.com/jhusain "@jhusain")さんが話されています。

本題はAsync Generatorですが、JavaScriptにおける非同期処理全体について話されています。
単純な同期的な処理からコールバック、Promise、Generator、ES7 async/awaitと順を追って話を進めています。

同期的なプログラミングで値を取り出すのはBlocking/pulling、コールバックスタイルのように受け取る関数を渡すのはWaiting/pushingといったような表現を使っていて 分かりやすくまとめられていると思います。

1時間程あって長いですが、よくできてる発表なのでJavaScriptにおける非同期処理について考えたい人は見ておくといいかもしれません。

自分が見ながら書いたメモは以下にまとめてあります。

<a class="twitter-timeline" data-dnt="true" href="/azu_re/timelines/541204375696191488" data-widget-id="541931115376689154">ES7 Async Generator</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
          

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Intern 2.2 released | Blog | SitePen
[www.sitepen.com/blog/2014/12/05/intern-2-2-released/](http://www.sitepen.com/blog/2014/12/05/intern-2-2-released/ "Intern 2.2 released | Blog | SitePen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Intern 2.2リリース。

コンソールレポーターの表示改善、テストが失敗した時にオブジェクトのDiff表示が出来るようになるなど

----

## Chromium Blog: Chrome 40 Beta: Powerful Offline and Lightspeed Loading with Service Workers
[blog.chromium.org/2014/12/chrome-40-beta-powerful-offline-and.html](http://blog.chromium.org/2014/12/chrome-40-beta-powerful-offline-and.html "Chromium Blog: Chrome 40 Beta: Powerful Offline and Lightspeed Loading with Service Workers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 40β リリース。

Service WorkersとCSP Lv2の部分的サポート、`element.closest()`のサポート等

----

## Firefox — Notes (34.0) — Mozilla
[www.mozilla.org/en-US/firefox/34.0/releasenotes/](https://www.mozilla.org/en-US/firefox/34.0/releasenotes/ "Firefox — Notes (34.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 34リリース。

CSS Fonts Level 3 の実験的な実装、ES6のObject.assign()やTemplate String、メソッド定義の短縮記法等の実装、開発者ツールの改善等

- [Firefox 34 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/34 "Firefox 34 for developers - Mozilla | MDN")
- [WebIDE, Storage inspector, jQuery events, iframe switcher + more – Firefox Developer Tools Episode 34 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2014/09/webide-storage-inspector-jquery-events-iframe-switcher-more-firefox-developer-tools-episode-34/ "WebIDE, Storage inspector, jQuery events, iframe switcher + more – Firefox Developer Tools Episode 34 ✩ Mozilla Hacks – the Web developer blog")

----

## Dev.Opera — Opera 26 released
[dev.opera.com/blog/opera-26/](https://dev.opera.com/blog/opera-26/ "Dev.Opera — Opera 26 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 26 (based on Chromium 39)リリース

----

## qunit/History.md at 1.16.0 · jquery/qunit
[github.com/jquery/qunit/blob/1.16.0/History.md](https://github.com/jquery/qunit/blob/1.16.0/History.md "qunit/History.md at 1.16.0 · jquery/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 1.16.0リリース。

`done()`呼び出しでの非同期テストを行う`assert.async`の追加、Promiseのサポート、setup/teardownをbeforeEach/afterEachにリネーム、HTML Reporterの改善等

- [async() | QUnit API Documentation](http://api.qunitjs.com/async/ "async() | QUnit API Documentation")
- [Async: Make tests Promise-aware by JamesMGreene · Pull Request #634 · jquery/qunit](https://github.com/jquery/qunit/pull/634 "Async: Make tests Promise-aware by JamesMGreene · Pull Request #634 · jquery/qunit")
- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")

----
<h1 class="site-genre">アーティクル</h1>

----

## Introduction to Service Worker: How to use Service Worker - HTML5 Rocks
[www.html5rocks.com/en/tutorials/service-worker/introduction/](http://www.html5rocks.com/en/tutorials/service-worker/introduction/ "Introduction to Service Worker: How to use Service Worker - HTML5 Rocks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Service Workerのライフサイクル、Service Workerへのスクリプトの登録方法や基本的な使い方、どうやってキャッシュを更新するか、注意点について

----

## Top 10 Mistakes Node.js Developers Make
[www.airpair.com/node.js/posts/top-10-mistakes-node-developers-make](https://www.airpair.com/node.js/posts/top-10-mistakes-node-developers-make "Top 10 Mistakes Node.js Developers Make")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">まとめ</span></p>

Nodeで開発時にやってしまう間違いとそれを改善する方法や参考リソース。

半分以上JavaScriptで同様の事が当てはまりそう

----

## bassistance.de » jQuery Foundation 2014 roundup
[bassistance.de/2014/12/01/jquery-foundation-2014-roundup/](http://bassistance.de/2014/12/01/jquery-foundation-2014-roundup/ "bassistance.de » jQuery Foundation 2014 roundup")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">まとめ</span></p>

2014年のjQueryの活動についてのまとめ。

- jQuery Coreの3.0の方針やPromises等の標準へ合わせる変更について
- jQuery UIのUIレイヤーの標準化活動、パフォーマンステストの実施。
- QUnitを始めとするテストフレームワークのレポーターの標準化活動。
- 国際化に使うCLDRのJSON版の管理など

などjQuery Fundationとしての活動がまとめられています。

- [Roadmap · jquery/jquery Wiki](https://github.com/jquery/jquery/wiki/Roadmap "Roadmap · jquery/jquery Wiki")
- [jquery/css-framework](https://github.com/jquery/css-framework "jquery/css-framework")
- [js-reporters/js-reporters](https://github.com/js-reporters/js-reporters/ "js-reporters/js-reporters")
- [jquery/globalize](https://github.com/jquery/globalize/ "jquery/globalize")

----

## Moving from PhantomJS to node-webkit - Todd Wolfson
[twolfson.com/2014-11-22-moving-from-phantomjs-to-node-webkit](http://twolfson.com/2014-11-22-moving-from-phantomjs-to-node-webkit "Moving from PhantomJS to node-webkit - Todd Wolfson")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">node-webkit</span> <span class="jser-tag">testing</span></p>

node-webkitを使いスクリーンショットを取って画像diffのレグレッションテストを行う話。

----

## 生WebGL入門:初音ミクの美麗3Dモデルを表示する(前編) » nmi.jp
[nmi.jp/archives/582](http://nmi.jp/archives/582 "生WebGL入門:初音ミクの美麗3Dモデルを表示する(前編) » nmi.jp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">JavaScript</span></p>

WebGLを使ってMMDの3Dモデルを表示するまでを丁寧に解説している

WebGLでのポリゴンの表示、3Dで必須な行列や座標、モデルデータの読み込みについて等

- [tkihira/webgl-miku-sample](https://github.com/tkihira/webgl-miku-sample "tkihira/webgl-miku-sample")

----

## JavaScript - Direct Proxiesでmethod missing的なことをやる - Qiita
[qiita.com/hokaccha/items/3a3ea6180e94e70bc335](http://qiita.com/hokaccha/items/3a3ea6180e94e70bc335 "JavaScript - Direct Proxiesでmethod missing的なことをやる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Direct Proxiesを使ったmethod missingの実装について

----

## webpackを使い倒す - Thujikun blog
[thujikun.github.io/blog/2014/12/07/webpack](http://thujikun.github.io/blog/2014/12/07/webpack "webpackを使い倒す - Thujikun blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpackのloader紹介、`resolve`フィールドの指定による`require`のパス解決、pluginsの紹介、Webpack Deb Server、非同期読み込みについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## QUnit 2.xで変わること
[azu.github.io/slide/chatwork/qunit2.html](http://azu.github.io/slide/chatwork/qunit2.html "QUnit 2.xで変わること")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">スライド</span></p>

QUnit 2.xでの変更点についてのスライド。

モジュール化、`done`スタイルの非同期テストサポート、スマートなPromiseテストサポート、レポーターの標準化活動など

- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")

----

## The npm Blog — Getting Started with npm
[blog.npmjs.org/post/104272486560/getting-started-with-npm](http://blog.npmjs.org/post/104272486560/getting-started-with-npm "The npm Blog — Getting Started with npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">動画</span></p>

npmのサイトのGetting Startedに動画チュートリアルが追加された

- [Getting Started](https://docs.npmjs.com/getting-started/what-is-npm "Getting Started")

----

## Netflix JavaScript Talks - Version 7: The Evolution of JavaScript - YouTube
[www.youtube.com/watch?v=DqMFX91ToLw](https://www.youtube.com/watch?v=DqMFX91ToLw "▶ Netflix JavaScript Talks - Version 7: The Evolution of JavaScript - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">動画</span> <span class="jser-tag">スライド</span></p>

ES7についてのAsync Generatorに紹介する発表。

Object.observeの変更通知とイベントループの話から始まり、
Promises、Generator、またES7のasync/await、さらに発展してObservableを返すAsync Generatorについて話されている。

発表内容は[jhusain/asyncgenerator](https://github.com/jhusain/asyncgenerator "jhusain/asyncgenerator")にも一部同様の事が書かれている

- [ES7 Async Generator from azu on Twitter](https://twitter.com/azu_re/timelines/541204375696191488 "ES7 Async Generator from azu on Twitter")
- [jhusain/asyncgenerator](https://github.com/jhusain/asyncgenerator "jhusain/asyncgenerator")
- [Version 7: The Evolution of JavaScript- Eventbrite](https://www.eventbrite.com/e/version-7-the-evolution-of-javascript-tickets-14284664817#m_1_100 "Version 7: The Evolution of JavaScript- Eventbrite")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## js-reporters/js-reporters
[github.com/js-reporters/js-reporters](https://github.com/js-reporters/js-reporters "js-reporters/js-reporters")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">issue</span></p>

JavaScriptテストフレームワーク/Runnerのレポーターの共通フォーマットについて議論してるコミュニティ

----

## Understanding JSON Schema — Understanding JSON Schema 1.0 documentation
[spacetelescope.github.io/understanding-json-schema/](http://spacetelescope.github.io/understanding-json-schema/ "Understanding JSON Schema — Understanding JSON Schema 1.0 documentation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">book</span> <span class="jser-tag">tutorial</span></p>

JSON Schema draft 4について解説しているサイト。

JSON Schemaの書き方やリファレンス等が用意されている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Tweene :: JavaScript Animation Proxy
[tweene.com/](http://tweene.com/ "Tweene :: JavaScript Animation Proxy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

JavaScriptアニメーションプロキシライブラリ。

既にアニメーション機能を実装してるGSAP、 Velocity.js、 Transit、 jQuery等のライブラリを共通のAPIで利用できるようにするラッパライブラリ

----

## lafikl/RWDPerf
[github.com/lafikl/RWDPerf](https://github.com/lafikl/RWDPerf "lafikl/RWDPerf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">design</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

画面サイズやUA等のシミュレートして、あるURLで使ってない要素や画像の検出、通信量などのデータを一覧出来るパフォーマンス測定ツール

----

## a11y.css by Gaël Poupard
[ffoodd.github.io/a11y.css/](http://ffoodd.github.io/a11y.css/ "a11y.css by Gaël Poupard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">HTML</span> <span class="jser-tag">ブックマークレット</span></p>

CSSを使ったHTMLのビジュアルLintツール。

HTML要素における記述のミスなどへの警告やエラーを表示する事ができる

----

## rejs – Vanilla JS Module Builderの紹介 | GREE Engineers&#x27; Blog
[labs.gree.jp/blog/2014/12/12311/](http://labs.gree.jp/blog/2014/12/12311/ "rejs – Vanilla JS Module Builderの紹介 | GREE Engineers&#x27; Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

名前空間オブジェクトを使うJavaScriptファイルを、名前空間のプロパティにアクセスできるようにソートして結合出来るコマンドラインツール

- [Moncader/rejs](https://github.com/Moncader/rejs "Moncader/rejs")

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript Cookbook, 2nd Edition - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920033455.do](http://shop.oreilly.com/product/0636920033455.do "JavaScript Cookbook, 2nd Edition - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2015年2月 発売

JavaScript Cookbookの第二版

----

## Learn JavaScript &amp; jQuery - a book about interactive front-end web development
[www.javascriptbook.com/](http://www.javascriptbook.com/ "Learn JavaScript &amp; jQuery - a book about interactive front-end web development")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">book</span></p>

HTML & CSS: Design and Build WebsitesのJavaScript編

----