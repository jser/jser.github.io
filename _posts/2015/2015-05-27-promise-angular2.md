---
title: "2015-05-27のJS: Promiseのありがちな間違い、AngularJS 2に向けて、Plain JS"
author: azu
layout: post
date : 2015-05-27T22:12
category: JSer
tags:
    - Promise
    - AngularJS
    - DOM
    - jQuery

---

JSer.info #229 - [We have a problem with promises](http://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html "We have a problem with promises")という記事では、Promiseでのありがちな間違いなどについてまとめて紹介されています。

Promiseの動作フローの解説、おかしな書き方とそれを修正した書き方を並べて紹介されていてよくまとまっていると思います。

[JavaScript Promiseの本](http://azu.github.io/promises-book/ "JavaScript Promiseの本")でも大部分で同様の話をしているので、一緒に見てみるといいかもしれません。

----

[JavaScript - AngularJSモダンプラクティス - Qiita](http://qiita.com/armorik83/items/5542daed0c408cb9f605 "JavaScript - AngularJSモダンプラクティス - Qiita")という記事では、既にAngularJS 1.xを使っている人が[AngularJS 2](https://angular.io/ "Angular")に向けてどのように1.xで書いておくとよいかについてまとめられています。

[AngularJS 2](https://angular.io/ "Angular")ではどのように書けるようになるのか、2.xでは廃止される機能、また関連するライブラリやツールについても書かれていて、AngularJSを使ってるいる人は読んでみるといいかもしれません。

----

[Plain JavaScript - Functions and Helpers](http://plainjs.com/javascript/ "Plain JavaScript - Functions and Helpers")というサイトでは、jQueryのメソッドに対応する事をPure JavaScriptで行うにはどうするかについて逆引きリファレンス的に書かれています。

[You Might Not Need jQuery](http://youmightnotneedjquery.com/ "You Might Not Need jQuery")と似たような感じですが、DOM APIの使い方の確認等に使えそうな感じがします。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## async/CHANGELOG.md at master · caolan/async
[github.com/caolan/async/blob/master/CHANGELOG.md#v100](https://github.com/caolan/async/blob/master/CHANGELOG.md#v100 "async/CHANGELOG.md at master · caolan/async")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

非同期処理を管理するライブラリであるasync 1.0.0リリース。

----
<h1 class="site-genre">アーティクル</h1>

----

## We have a problem with promises
[pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html](http://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html "We have a problem with promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">まとめ</span></p>

Promiseの色々な落とし穴やアンチパターンについてよくまとまってる

- [JavaScript Promiseの本](http://azu.github.io/promises-book/ "JavaScript Promiseの本")

----

## JavaScript - AngularJSモダンプラクティス - Qiita
[qiita.com/armorik83/items/5542daed0c408cb9f605](http://qiita.com/armorik83/items/5542daed0c408cb9f605 "JavaScript - AngularJSモダンプラクティス - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

AngularJS 2に移行しやすくするにはどうするかというチュートリアル。
1.xでもES6 classesを使った書き方をするためのリファクタリング方法。
Angular 2でのdirective、モジュール、関連ライブラリやツール、FAQなど

----

## Moving to ES6 from CoffeeScript
[gist.github.com/danielgtaylor/0b60c2ed1f069f118562](https://gist.github.com/danielgtaylor/0b60c2ed1f069f118562 "Moving to ES6 from CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CoffeeScript</span></p>

CoffeScriptからES6への移行するにおいて文法の比較やES6の構文や機能の紹介

----

## ES6 — classes and inheritance — Medium
[medium.com/@mrzepinski/es6-classes-and-inheritance-607804080906](https://medium.com/@mrzepinski/es6-classes-and-inheritance-607804080906 "ES6 — classes and inheritance — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 ClassesとES5との書き方比較。
getterやsetter、細かいショートハンドとともに紹介してる

----

## Why Backbone.js? - Roost Austin
[roost.bocoup.com/2015/austin/blog/why-backbone/](https://roost.bocoup.com/2015/austin/blog/why-backbone/ "Why Backbone.js? - Roost Austin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">MVC</span></p>

JavaScriptライブラリをどのような基準で比較して選択するかについて。
メジャーなライブラリの統計を比較した図や学習曲線、欠点などについて書かれていて、どのような見方があるかについての話が興味深い

----

## Notifying you of Changes to Notifications
[updates.html5rocks.com/2015/05/Notifying-you-of-notificiation-changes](http://updates.html5rocks.com/2015/05/Notifying-you-of-notificiation-changes "Notifying you of Changes to Notifications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Chrome 44でService Workerを使ったプッシュ通知で任意のオブジェクトを渡せるようになり、また`getNotifications()`で特定のtagがついたNotificationのみを取り出せるようになった

----

## graphite, grafana, sitespeed.io, diamond で継続 Web パフォーマンスモニタリング - Qiita
[qiita.com/Jxck\_/items/abfa9f3dd15c5572cbfd](http://qiita.com/Jxck_/items/abfa9f3dd15c5572cbfd "graphite, grafana, sitespeed.io, diamond で継続 Web パフォーマンスモニタリング - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

sitespeed.ioを使い実際のブラウザを動かしてTiming API等のクライアントサイドでのメトリクス情報を継続的に取得したデータをgraphiteに保存し可視化する方法について

----

## ここ最近のWeb地図周辺の動向をまとめてみた | #GUNMAGISGEEK
[shimz.me/blog/map/4268](http://shimz.me/blog/map/4268 "ここ最近のWeb地図周辺の動向をまとめてみた | #GUNMAGISGEEK")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">GEO</span> <span class="jser-tag">まとめ</span></p>

GeoJSONを始めウェブの地図周りの技術についての変化について

----

## Testing JavaScript — Medium
[medium.com/@nickheiner/testing-javascript-8c8efe8434e](https://medium.com/@nickheiner/testing-javascript-8c8efe8434e "Testing JavaScript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

proxyquireを使ったテスト、E2Eとモック、tapeを使ったテストについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ウェブクリエイターの為の情報サイト | Web Programming Primer
[wp-p.info/](http://wp-p.info/ "ウェブクリエイターの為の情報サイト | Web Programming Primer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span></p>

HTML/CSS/JavaScriptの入門的な内容のチュートリアル集

----

## Plain JavaScript - Functions and Helpers
[plainjs.com/javascript/](http://plainjs.com/javascript/ "Plain JavaScript - Functions and Helpers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">リファレンス</span></p>

Pure JavaScriptでDOM操作などについての逆引きリファレンス

----

## EmberWeekend
[emberweekend.com/episodes](https://emberweekend.com/episodes "EmberWeekend")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">podcast</span></p>

EmberJSについてのpodcast

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## sebastian-lenz/typedoc
[github.com/sebastian-lenz/typedoc](https://github.com/sebastian-lenz/typedoc "sebastian-lenz/typedoc")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">API</span> <span class="jser-tag">document</span></p>

TypeScriptのAPIドキュメント生成ツール

----

## WebdriverIO - Selenium 2.0 javascript bindings for nodejs
[webdriver.io/](http://webdriver.io/ "WebdriverIO - Selenium 2.0 javascript bindings for nodejs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Selenium</span> <span class="jser-tag">webdriver</span></p>

Node.jsのSelenium/WebDriver APIのバインディング。
モバイルのフリックやタブの切替等色々なAPIが用意されてる

----

## symdiff
[symdiff.github.io/](https://symdiff.github.io/ "symdiff")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

HTMLとCSSを渡して使われてないCSSを検索するツール

----

## padolsey/operative
[github.com/padolsey/operative](https://github.com/padolsey/operative "padolsey/operative")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

直接関数を渡してそれをWeb Workerで動かせるライブラリ。
古いブラウザ向けのfallbackやPromiseのサポートなど、できるだけシームレスに書けるようにしてる

- [operativeでWebWorkersを手軽に扱う - 四角革命前夜](http://blog.sasaplus1.com/2015/05/23/01/ "operativeでWebWorkersを手軽に扱う - 四角革命前夜")

----

## High-performance javascript library for animations &amp; interfaces | Famous.org
[famous.org/](http://famous.org/ "High-performance javascript library for animations &amp; interfaces | Famous.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span></p>

アニメーションライブラリであるFamousがリニューアル公開された

----

## Easily testing React components with react-test-tree — Qubit Engineering — Medium
[medium.com/qubit-engineering/easily-testing-react-components-with-react-test-tree-f9e1668b1c2d](https://medium.com/qubit-engineering/easily-testing-react-components-with-react-test-tree-f9e1668b1c2d "Easily testing React components with react-test-tree — Qubit Engineering — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">DOM</span></p>

React component向けのテストライブラリ。
対象のReact componentに`ref`属性を追加しておくことで、clickなどのイベントのシミュレートや子componentをstubすることができる

- [QubitProducts/react-test-tree](https://github.com/QubitProducts/react-test-tree "QubitProducts/react-test-tree")

----