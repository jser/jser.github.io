---
title: "2014-12-23のJS: 開発者アンケート結果、Protractorの仕組み、パフォーマンスチューニング"
author: azu
layout: post
date : 2014-12-23T18:26
category: JSer
tags:
    - アンケート
    - E2E
    - Performance
    - JavaScript
    - Angular

---

JSer.info #207 - [DailyJS](http://dailyjs.com/ "DailyJS: A JavaScript Blog")が毎年この時期にやっているアンケートである[JavaScript Developer Survey 2014](http://dailyjs.com/2014/12/16/javascript-survey-results/ "DailyJS: JavaScript Developer Survey 2014: Results")([翻訳](http://panda.node.ws/?p=1620 "翻訳"))の結果が公開されました。

毎年微妙に質問や回答方法(複数可となってたり)が異なるため、単純に比較はしにくい設問もありますが、
[去年](http://dailyjs.com/2013/12/12/javascript-survey-results/ "DailyJS: JavaScript Developer Survey 2013: Results")はGrunt一強だったビルドツールについてがGulpが35%、Gruntは47%となっていたり見ていて面白い変化も多いです。

----

[JavaScript - こわくない Protractor - Qiita](http://qiita.com/shuhei/items/6973fe694d29a193f224 "JavaScript - こわくない Protractor - Qiita")という記事では、[Protractor](https://github.com/angular/protractor "Protractor")というE2Eテストツールがどのようにして[WebDriverJS](https://code.google.com/p/selenium/wiki/WebDriverJs "WebDriverJS")を扱ってテストしているのかについて詳しく書かれています。

テスト時にSeleniumでブラウザを操作しているため、操作から実際の結果までに間があったり、その結果をassertするタイミングが難しかったり、非同期とした場合コードが複雑になったりしやすいです。

そのため[色々なライブラリ](https://github.com/groupon-testium/testium "groupon-testium/testium")がこの[WebDriver protocolのラッパ](https://theintern.github.io/leadfoot/ "Leadfoot docs: Index")を作ったり、それらのラッパを使って直感的に[テストを書けるような記法](http://nightwatchjs.org/ "Nightwatch.js | Node.js powered End-to-End testing framework")を考えたりしています。

Protractorも同じように[WebDriverJS](https://code.google.com/p/selenium/wiki/WebDriverJs "WebDriverJS")というラッパを使い、`ElementFinder`という概念を導入したり、Promiseで非同期に処理されつつ直感的に書けるようにしているという話が書かれています。

----

[Effective web performance tuning for smartphone](http://www.slideshare.net/dena_study/effective-web-performance-tuning-for-smartphone "Effective web performance tuning for smartphone")というスライドではスマートフォン向けウェブアプリのパフォーマンス改善について実践的な内容が紹介されています。

実際にどうやって問題を見つけて、計測して、何を指標にして改善していったかが書かれていて、
どうやってパフォーマンス改善に取り組んでいけばいいのかの参考になる点も多いと思います。

以下もあわせて

- [2014年のWebパフォーマンスふりかえり - 来年以降の期待etc ::ハブろぐ](http://havelog.ayumusato.com/develop/performance/e637-web_performance_2014.html "2014年のWebパフォーマンスふりかえり - 来年以降の期待etc ::ハブろぐ")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v0.10.34 (Stable)
[blog.nodejs.org/2014/12/17/node-v0-10-34-stable](http://blog.nodejs.org/2014/12/17/node-v0-10-34-stable "Node v0.10.34 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.10.34 リリース。

v0.11.15がv0.12RCとなるので、次のStableで0.12がリリースされる予定(が[ルート証明書のトラブル](http://d.hatena.ne.jp/jovi0608/20141222/1419265270 "Node-v0.10.34がはまったクロスルート証明書とOpenSSLの落とし穴 - ぼちぼち日記")により多少ずれそう)

- [node js on Twitter: &quot;Node v0.10.34 (Stable) http://t.co/VimTZXc1VK tomorrow is v0.11.15 (the release candidate for v0.12)&quot;](https://twitter.com/nodejs/status/545349270241435648 "node js on Twitter: &quot;Node v0.10.34 (Stable) http://t.co/VimTZXc1VK tomorrow is v0.11.15 (the release candidate for v0.12)&quot;")
- [node v0.10.34 で CERT_UNTRUSTED のエラーが発生する - Qiita](http://qiita.com/ken880guchi/items/bb72846fb785b01ced0b "node v0.10.34 で CERT_UNTRUSTED のエラーが発生する - Qiita")
- [Node-v0.10.34がはまったクロスルート証明書とOpenSSLの落とし穴 - ぼちぼち日記](http://d.hatena.ne.jp/jovi0608/20141222/1419265270 "Node-v0.10.34がはまったクロスルート証明書とOpenSSLの落とし穴 - ぼちぼち日記")

----

## jQuery 1.11.2 and 2.1.3 Released – Safari Fail-Safe Edition | Official jQuery Blog
[blog.jquery.com/2014/12/18/jquery-1-11-2-and-2-1-3-released-safari-fail-safe-edition/](http://blog.jquery.com/2014/12/18/jquery-1-11-2-and-2-1-3-released-safari-fail-safe-edition/ "jQuery 1.11.2 and 2.1.3 Released – Safari Fail-Safe Edition | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 1.11.2 と 2.1.3リリース。

iOS7と8のquerySelectorバグの対処(Workaound)

----

## Improving the Pointer Events Polyfill | Official jQuery Blog
[blog.jquery.com/2014/12/17/improving-the-pointer-events-polyfill/](http://blog.jquery.com/2014/12/17/improving-the-pointer-events-polyfill/ "Improving the Pointer Events Polyfill | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

GoogleからjQuery FoundationがPointerEventsのpolyfillの管理を引き継いだ

----
<h1 class="site-genre">アーティクル</h1>

----

## DailyJS: JavaScript Developer Survey 2014: Results
[dailyjs.com/2014/12/16/javascript-survey-results/](http://dailyjs.com/2014/12/16/javascript-survey-results/ "DailyJS: JavaScript Developer Survey 2014: Results")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span></p>

JavaScript開発者アンケート 2014年の結果が公開された。

- [DailyJS | JavaScript デベロッパー・サーベイ 2014 結果 | JSお散歩](http://panda.node.ws/?p=1620 "DailyJS | JavaScript デベロッパー・サーベイ 2014 結果 | JSお散歩")

----

## HTML Best Practices - Weblog - Hail2u.net
[hail2u.net/blog/webdesign/html-best-practices.html](http://hail2u.net/blog/webdesign/html-best-practices.html "HTML Best Practices - Weblog - Hail2u.net")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span></p>

HTMLベストプラクティス。

HTMLの書き方について良い例と悪い例が書かれている

- [hail2u/html-best-practices](https://github.com/hail2u/html-best-practices "hail2u/html-best-practices")

----

## IE10 以下を切る場合の JavaScript チェックリスト - Qiita
[qiita.com/Jxck_/items/fe8a1c49cac717e52ae3](http://qiita.com/Jxck_/items/fe8a1c49cac717e52ae3 "IE10 以下を切る場合の JavaScript チェックリスト - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">まとめ</span></p>

モダンブラウザでは利用できるJavaScriptやDOM APIについて。

また使いどころが難しい機能についても触れている

----

## ソーシャルメディアの読み込みはDNSプリフェッチのまとめ設定がお得 | ゆっくりと…
[tokkono.cute.coocan.jp/blog/slow/index.php/programming/boostup-socials-with-dns-prefetch/](http://tokkono.cute.coocan.jp/blog/slow/index.php/programming/boostup-socials-with-dns-prefetch/ "ソーシャルメディアの読み込みはDNSプリフェッチのまとめ設定がお得 | ゆっくりと…")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

`<link rel="dns-prefetch" />`のブラウザサポート状況、同時に指定できる数の制限が無いこと、meta要素を置く場所について。

----

## Maintaining JavaScript Code Quality with ESLint | PayPal Engineering Blog
[www.paypal-engineering.com/2014/12/12/maintaining-javascript-code-quality-with-eslint/](https://www.paypal-engineering.com/2014/12/12/maintaining-javascript-code-quality-with-eslint/ "Maintaining JavaScript Code Quality with ESLint | PayPal Engineering Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">AST</span></p>

自分でルールを拡張出来るESLintの紹介。簡単なルールの書き方、設定方法について

----

## Unit Testing Polymer Elements - Polymer
[www.polymer-project.org/articles/unit-testing-elements.html](https://www.polymer-project.org/articles/unit-testing-elements.html "Unit Testing Polymer Elements - Polymer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">testing</span> <span class="jser-tag">tutorial</span></p>

Polymerを使ったElementのテストのチュートリアル。

Web Componentsのテストの参考になりそう

----

## JavaScript - こわくない Protractor - Qiita
[qiita.com/shuhei/items/6973fe694d29a193f224](http://qiita.com/shuhei/items/6973fe694d29a193f224 "JavaScript - こわくない Protractor - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">protractor</span> <span class="jser-tag">E2E</span> <span class="jser-tag">testing</span></p>

ProtractorというE2Eテストツールの仕組みについての解説。

element() は DOM 要素を選択してる訳ではない、ブラウザの操作をするメソッドはPromiseを返している、書いた順番で実行されるようになっている点などどのような仕組みで動いているかについてまとめられている

----

## 私のJavaScript情報の集め方 - Qiita
[qiita.com/koba04/items/ba2381776d394633de72](http://qiita.com/koba04/items/ba2381776d394633de72 "私のJavaScript情報の集め方 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rss</span> <span class="jser-tag">twitter</span> <span class="jser-tag">github</span></p>

JavaScriptに関連する情報収集について

- [Frontrend in Kanazawaのスライドを公開しましたというご連絡と情報収集についての補足など - Life goes on](http://layzie.hatenablog.com/entry/20141104/1415076724 "Frontrend in Kanazawaのスライドを公開しましたというご連絡と情報収集についての補足など - Life goes on")
- [世界のJavaScriptを読もう @ 2014](http://azu.github.io/slide/jser200/javascript-2014.html "世界のJavaScriptを読もう @ 2014")

----

## TypeScript - dtsmのご紹介 - Qiita
[qiita.com/vvakame/items/38b953ab0f4de63cce8b](http://qiita.com/vvakame/items/38b953ab0f4de63cce8b "TypeScript - dtsmのご紹介 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">package</span> <span class="jser-tag">Tools</span></p>

npmライクなコマンドラインインタフェースを持ったd.ts管理ツール

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## React.js + Flux入門 #scripty02
[www.slideshare.net/techblogyahoo/reactjs-flux-scripty02](http://www.slideshare.net/techblogyahoo/reactjs-flux-scripty02 "React.js + Flux入門 #scripty02")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">Flux</span></p>

React, Virtual DOM, Flux(Fluxxor) を全体的に眺めた感じのスライド。 Reactが持つ機能やライフサイクル、Fluxのフローについて

----

## Backbone Conf III - 2014 - YouTube
[www.youtube.com/playlist?list=PLlgxAbM67lYIGw8DnANC7VgREbzJRQged&amp;app=desktop](https://www.youtube.com/playlist?list=PLlgxAbM67lYIGw8DnANC7VgREbzJRQged&amp;app=desktop "Backbone Conf III - 2014 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">動画</span> <span class="jser-tag">イベント</span> <span class="jser-tag">まとめ</span></p>

http://backboneconf.com/ の動画が公開された

- [BACKBONECONF 2014, by Bocoup](http://backboneconf.com/ "BACKBONECONF 2014, by Bocoup")

----

## Effective web performance tuning for smartphone
[www.slideshare.net/dena_study/effective-web-performance-tuning-for-smartphone](http://www.slideshare.net/dena_study/effective-web-performance-tuning-for-smartphone "Effective web performance tuning for smartphone")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">mobile</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

スマフォのパフォーマンスチューニングについてのスライド。

どうやって調査するか、改善のワークフロー、何を指標に改善するか。

改善すべき目安やポイントとして
処理時間が20ms超、一定間隔で同一処理、描画の負荷が高いイベント、5MB超のGC、メモリリーク、意図しないレイヤーの合成
などについて書かれている。

- [第三回DeNAゲーム開発勉強会 : ATND](https://atnd.org/events/59594 "第三回DeNAゲーム開発勉強会 : ATND")
- [2014年のWebパフォーマンスふりかえり - 来年以降の期待etc ::ハブろぐ](http://havelog.ayumusato.com/develop/performance/e637-web_performance_2014.html "2014年のWebパフォーマンスふりかえり - 来年以降の期待etc ::ハブろぐ")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Libscore
[libscore.com/](http://libscore.com/ "Libscore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">検索</span></p>

世界中のサイトでどのJavaScriptライブラリがどれくらい使われているかを表示するサービス

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## domenic/html-as-custom-elements
[github.com/domenic/html-as-custom-elements](https://github.com/domenic/html-as-custom-elements "domenic/html-as-custom-elements")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WebComponents</span></p>

HTML要素をCustom Elementで実装し直すプロジェクト。

----

## foss-haas/fynx
[github.com/foss-haas/fynx](https://github.com/foss-haas/fynx "foss-haas/fynx")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Fluxアーキテクチャ的な実装ライブラリ。

Ajax的な操作を行うServicesという場所を明示的に用意している。

----
<h1 class="site-genre">書籍関係</h1>

----

## CUTT System:TypeScriptネットワークプログラミング
[www.cutt.co.jp/book/978-4-87783-354-1.html](http://www.cutt.co.jp/book/978-4-87783-354-1.html "CUTT System:TypeScriptネットワークプログラミング")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2014年1月10日 発売

WebSocketやWebRTC等を使ったアプリをTypeScriptで書いて学んで行く書籍

----