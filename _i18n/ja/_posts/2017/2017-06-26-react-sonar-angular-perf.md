---
title: "2017-06-26のJS: React入門、sonar - linting for web、Angularパフォーマンス改善"
author: "azu"
layout: post
date : 2017-06-26T08:55:22.360Z
category: JSer
tags:
- React
- Lint
- ESLint
- Angular

---

JSer.info #337 - [React Express](http://www.react.express/ "React Express")というサイトでは、Reactでのアプリケーション開発についてのチュートリアルが書かれています。
Reactから始める開発という形なので、npmなどの関連するツールやES2015など周辺環境についても簡単に紹介されています。
基本的に実行できるサンプルコードと共にReactについて紹介されているので、触りながら理解するのに役立ちそうです。

-----

 [sonar, a linting tool for the web](https://sonarwhal.com/ "sonar, a linting tool for the web")というウェブサイトに対するESLintのようなツールがJS Foundationの元で公開されました。

- [sonar – JS Foundation Welcomes Newest Project – JS Foundation](https://js.foundation/announcements/2017/06/22/sonar-js-foundation-welcomes-newest-project "sonar – JS Foundation Welcomes Newest Project – JS Foundation")

元々はMSEdgeのチームによって作られたもので、ESLintのようにカスタムルールを書くことができます。

- [sonar/events.md at master · sonarwhal/sonar](https://github.com/sonarwhal/sonar/blob/master/docs/developer-guide/collectors/events.md "sonar/events.md at master · sonarwhal/sonar")
   - hookできるイベント

ウェブサイトのHTML要素をトラバースしながら処理したり、リソースに対するリクエストに関する処理などをルールとして書くことができます。

[FAQ](https://sonarwhal.com/about/faq.html "FAQ")によると、[aXe](https://www.deque.com/products/axe/ "Easy Accessibility Testing with aXe")や[SSL Server Test](https://www.ssllabs.com/ssltest/ "SSL Server Test")など既存ツールやサービスと連携したLintingツールとすることを目的としているようです。(そのためルールも非同期処理に対応している)

> sonar doesn’t want to reinvent the wheel. For that reason it tries to integrate other tools and services that do a great job and contribute back where appropriate. For example, we are using axe for accessibility, SSL Server Test for checking the certificate configuration, etc.

----

[Improve SPA Performance with Angular App // Speaker Deck](https://speakerdeck.com/manakuro/improve-spa-performance-with-angular-app "Improve SPA Performance with Angular App // Speaker Deck")というスライドでは、メモリリークが起きやすいパターンやChrome開発者ツールを使った計測方法について書かれています。
また、AngularにおけるメモリリークのパターンやChange Detectionの処理を削減する方法などについて書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Dev.Opera — What’s new in Chromium 59 and Opera 46
[dev.opera.com/blog/opera-46/](https://dev.opera.com/blog/opera-46/ "Dev.Opera — What’s new in Chromium 59 and Opera 46")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 46 (based on Chromium 59)リリース。
Animation PNG、SVGファビコン、バックグラウンドタブのスロットリング、`MediaError.message`のサポートなど


----

## New Release: 2.9.5
[jshint.com/blog/2017-06-22/release-2-9-5/](http://jshint.com/blog/2017-06-22/release-2-9-5/ "New Release: 2.9.5")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.9.5リリース。
`trailingcomma`オプションの追加、バグ修正など


----

## ESLint v4.1.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/06/eslint-v4.1.0-released](http://eslint.org/blog/2017/06/eslint-v4.1.0-released "ESLint v4.1.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.1.0リリース。 globベースの`overrides`設定の追加、無視ファイルを`package.json`に定義できるように

- [ESLint v4.1.0 - Qiita](http://qiita.com/mysticatea/items/e758c9a9a7dfb8b9cdb1 "ESLint v4.1.0 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## JS scope: static, dynamic, and runtime-augmented – Dmitry Soshnikov – Medium
[medium.com/@DmitrySoshnikov/js-scope-static-dynamic-and-runtime-augmented-5abfee6223fe](https://medium.com/@DmitrySoshnikov/js-scope-static-dynamic-and-runtime-augmented-5abfee6223fe "JS scope: static, dynamic, and runtime-augmented – Dmitry Soshnikov – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScriptのスコープについて。
作ったときに参照が解決できるStatic scope、呼び出し元によって参照が決まるDynamic scope、`witH`や`eval`によるRuntime-augmented scopeについて


----

## React Express
[www.react.express/](http://www.react.express/ "React Express")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

Reactのチュートリアルサイト。
実行できるサンプルと共にReactの使い方や、npm/webpack/ES2015など関連するツールや知識について解説してる。


----

## Redux Architecture Guidelines | joeellis.la
[joeellis.la/redux-architecture/](http://joeellis.la/redux-architecture/ "Redux Architecture Guidelines | joeellis.la")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

ケースバイケースではあるけど、Reduxを使ったアーキテクチャのガイドライン。
stateのネストを避けるためにnormalizeする、stateにはsourceとなるデータを入れる、ReactのstateよりReduxのState。
Standard Action、Container componentについてなど


----

## Aligned Input Events  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/aligning-input-events](https://developers.google.com/web/updates/2017/06/aligning-input-events "Aligned Input Events  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">event</span> <span class="jser-tag">article</span> <span class="jser-tag">Android</span></p>

Pointer Eventsの`getCoalescedEvents`について。
入力デバイスは60-120Hzに対して、モニタが60Hzである場合にポインタのイベントをすべて処理するのは無駄となる。
その無駄を回避するためにイベントをまとめてくれる`getCoalescedEvents()`について


----

## Codemods: A Quick and Easy Way to Automate Code Refactoring — SitePoint
[www.sitepoint.com/getting-started-with-codemods/](https://www.sitepoint.com/getting-started-with-codemods/ "Codemods: A Quick and Easy Way to Automate Code Refactoring — SitePoint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">AST</span></p>

codemodを使ったリファクタリングツールの作り方についての記事


----

## ✨Locally Scoped CSS Variables: What, How, and Why | Una Kravets Online✨
[una.im/local-css-vars/](https://una.im/local-css-vars/ "✨Locally Scoped CSS Variables: What, How, and Why | Una Kravets Online✨")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

CSS Custom Propertiesについて。
利用方法、ローカルスコープ、サポート状況についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## High Performance JS in V8 - Google スライド
[docs.google.com/presentation/d/1KCcA-WAyhGs0SEOrfU21fjaTWTxvNxYLwmNlGIbuZFw/edit#slide&#x3D;id.p](https://docs.google.com/presentation/d/1KCcA-WAyhGs0SEOrfU21fjaTWTxvNxYLwmNlGIbuZFw/edit#slide=id.p "High Performance JS in V8 - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

V8のES2015+のパフォーマンスについてのスライド。
CrankshaftはES2015を最適化しないため遅かった。またtry-catchなどがあると最適化できなかった。
新しいpipelineのIgnition + Turbofanではその部分が改善されているという話。


----

## Improve SPA Performance with Angular App // Speaker Deck
[speakerdeck.com/manakuro/improve-spa-performance-with-angular-app](https://speakerdeck.com/manakuro/improve-spa-performance-with-angular-app "Improve SPA Performance with Angular App // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">performance</span> <span class="jser-tag">Angular</span> <span class="jser-tag">slide</span></p>

メモリリークのパターン、Chromeの開発者ツールを使っての計測方法について。
Angularにおける意図しないメモリリークを避ける方法やChange Detectionのコストを削減する方法についてなど

- [mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.](https://github.com/mgechev/angular-performance-checklist "mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.
[github.com/mgechev/angular-performance-checklist](https://github.com/mgechev/angular-performance-checklist "mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">performance</span> <span class="jser-tag">document</span></p>

Angularのパフォーマンスチェックリスト


----

## faceyspacey/redux-first-router: 🎖 seamless redux-first routing -- just dispatch actions
[github.com/faceyspacey/redux-first-router](https://github.com/faceyspacey/redux-first-router "faceyspacey/redux-first-router: 🎖 seamless redux-first routing -- just dispatch actions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Redux向けのルーターライブラリ。
URLパターンにマッチしたActionを発行することをベースにしてルーティングできるようにしている

- [Pre Release: Redux-First Router — A Step Beyond Redux-Little-Router](https://medium.com/faceyspacey/pre-release-redux-first-router-a-step-beyond-redux-little-router-cd2716576aea "Pre Release: Redux-First Router — A Step Beyond Redux-Little-Router")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## sonar, a linting tool for the web
[sonarwhal.com/](https://sonarwhal.com/ "sonar, a linting tool for the web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

ウェブサイト(URL)に対するESLintのようなLintツール。
カスタムルールを自分で定義することができ、axeやSSL Server Testなど既存のツールを簡単に統合して利用できるようにする目的。


----

## await-to-js - NMOTW
[nmotw.in//github/await-to-js/](http://nmotw.in//github/await-to-js/ "await-to-js - NMOTW")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

awaitと組み合わせて使うことで、go言語のように`[error, value]`の値を返すようにするライブラリ


----

## medikoo/date-from-timezone: Construct dates with timezone context
[github.com/medikoo/date-from-timezone](https://github.com/medikoo/date-from-timezone "medikoo/date-from-timezone: Construct dates with timezone context")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

`Intl.DateTimeFormat`を使うことで、JavaScriptでタイムゾーン情報を付与して`new Date`を行うライブラリ

- [Add timezone data to Date](https://esdiscuss.org/topic/add-timezone-data-to-date#content-6 "Add timezone data to Date")

----

## OptimalBits/redbird: A modern reverse proxy for node
[github.com/OptimalBits/redbird](https://github.com/OptimalBits/redbird "OptimalBits/redbird: A modern reverse proxy for node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proxy</span></p>

HTTPSやHTTP/2に対応したNode.jsでのリバースプロキシライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## O'Reilly Japan - アイソモーフィックJavaScript
[www.oreilly.co.jp/books/9784873118079/](https://www.oreilly.co.jp/books/9784873118079/ "O'Reilly Japan - アイソモーフィックJavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">React</span> <span class="jser-tag">Angular</span></p>

2017年7月4日発売
Isomorphic JavaScriptについての書籍。
実現する方法や各種フレームワークReact/Angular/Brisketを使った方法、ケーススタディなど


----
