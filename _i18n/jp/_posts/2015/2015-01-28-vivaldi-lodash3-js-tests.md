---
title: "2015-01-28のJS: Vivaldi、lodash 3.0.0、JavaScriptテスト概要"
author: azu
layout: post
date : 2015-01-28T00:14
category: JSer
tags:
    - Browser
    - Opera
    - library
    - Testing

---


JSer.info #212 - 元OperaのCEOによるChromiumベースのブラウザである[Vivaldi](https://vivaldi.com/)のTechinial Preview版が公開されました。

- [Meet Vivaldi, A New Browser From the Former CEO of Opera](http://thenextweb.com/apps/2015/01/27/meet-vivaldi-new-browser-former-ceo-opera/)
- [Former Opera CEO Launches Vivaldi, A New Browser For Power Users | TechCrunch](http://techcrunch.com/2015/01/27/vivaldi-the-four-browsers/)

Opera 12ユーザーに向けての機能が多く搭載されている感じで、Chroniumをベースとしているのでレンダリングエンジンは現在のOperaと同じくBlinkが使われているようです。

----

[lodash v3.0.0](https://github.com/lodash/lodash/releases/tag/3.0.0 "lodash v3.0.0")がリリースされました。

String関係のメソッドの追加、関数型スタイルで使うためのメソッドの追加などがされました。

また`npm instal lodash.foreach`というように個々のモジュールとして入れることは以前から可能でしたが、この時の依存関係のツリーがシンプルになるように改善されました。

加えてパフォーマンス面でもlazy chainingの導入やES6のSet & WeakMapを利用することで大きく改善されたようです。

----

[A Journey Through Client-Side Testing with JavaScript -Telerik Developer Network](http://developer.telerik.com/featured/journey-client-side-testing-javascript/ "A Journey Through Client-Side Testing with JavaScript -Telerik Developer Network")ではJavaScriptテストについて幅広く書かれています。

JavaScriptのテストと言っても色々な役割を持つ組み合わせで動いてることが多く、AssertionやTest Runnerとはどういうものがあるかについて書かれています


<iframe src="//www.slideshare.net/slideshow/embed_code/20015155?startSlide=33" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/teppeis/javascript-testwhywhathow" title="JavaScript Unit Test Why? What? How?" target="_blank">JavaScript Unit Test Why? What? How?</a> </strong> from <strong><a href="//www.slideshare.net/teppeis" target="_blank">teppeis </a></strong> </div>

またTodoMVCを例にテストの実行についても紹介していて、ユニットテストというよりIntegration Testsという感じの話となっています。

最近、Integration Testsの話として[Testium](https://github.com/groupon-testium/testium "Testium")について書いたのでこちらも合わせてみるといいかもしれません。

- [テストできないコードをE2Eテストを使ってリファクタリングしよう | Web Scratch](http://efcl.info/2015/01/24/testium-e2e-refactoring/ "テストできないコードをE2Eテストを使ってリファクタリングしよう | Web Scratch")


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Vivaldi - A new browser for our friends
[vivaldi.com/](https://vivaldi.com/ "Vivaldi - A new browser for our friends")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Opera</span> <span class="jser-tag">blink</span></p>

元Opera CEOが始めたブラウザ。
Chromium(Blink)をベースにしていて、UIにReact等ウェブの技術を使用している。

----

## Chromium Blog: Chrome 41 Beta: New ES6 Features and Improved DevTools for Service Workers and Web Animations
[blog.chromium.org/2015/01/chrome-41-beta-new-es6-features-and.html](http://blog.chromium.org/2015/01/chrome-41-beta-new-es6-features-and.html "Chromium Blog: Chrome 41 Beta: New ES6 Features and Improved DevTools for Service Workers and Web Animations")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 41βリリース。
ES6 Template Literals、Web Animationsのデバッグ機能、image-rendering: pixelatedのサポート等

----

## Release 2.5.0 · groupon-testium/testium
[github.com/groupon-testium/testium/releases/tag/v2.5.0](https://github.com/groupon-testium/testium/releases/tag/v2.5.0 "Release 2.5.0 · groupon-testium/testium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Integration Testフレームワークのtestium 2.5.0リリース。
日本語などの入力ができない問題の修正やエラー表示の改善、`Element.prototype.getElement`の実装など

----

## Release 3.0.0 · lodash/lodash
[github.com/lodash/lodash/releases/tag/3.0.0](https://github.com/lodash/lodash/releases/tag/3.0.0 "Release 3.0.0 · lodash/lodash")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

lodash v3.0.0リリース。
String関係のメソッドの追加、関数型スタイルで使いやすいメソッドの追加、個々のモジュールとして入れた時の依存関係をシンプルに、パフォーマンスの改善、lazy chainingの導入等

- [Changelog · lodash/lodash Wiki](https://github.com/lodash/lodash/wiki/Changelog#compatibility-warnings "Changelog · lodash/lodash Wiki")
- [How to Speed Up Lo-Dash ×100? Introducing Lazy Evaluation. | Filip Zawada](http://filimanjaro.com/blog/2014/introducing-lazy-evaluation/ "How to Speed Up Lo-Dash ×100? Introducing Lazy Evaluation. | Filip Zawada")

----

## Release JSHint 2.6.0 · jshint/jshint
[github.com/jshint/jshint/releases/tag/2.6.0](https://github.com/jshint/jshint/releases/tag/2.6.0 "Release JSHint 2.6.0 · jshint/jshint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.6.0リリース。

----

## ESLint 0.13.0 released - ESLint
[eslint.org/blog/2015/01/eslint-0.13.0-released/](http://eslint.org/blog/2015/01/eslint-0.13.0-released/ "ESLint 0.13.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.13.0リリース。
Template strings、デフォルトパラメータ等のES6サポート改善、ブロックスコープの挙動を修正等

----
<h1 class="site-genre">アーティクル</h1>

----

## テストできないコードをE2Eテストを使ってリファクタリングしよう | Web Scratch
[efcl.info/2015/01/24/testium-e2e-refactoring/](http://efcl.info/2015/01/24/testium-e2e-refactoring/ "テストできないコードをE2Eテストを使ってリファクタリングしよう | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">browser</span></p>

E2EテストフレームワークのTestiumの紹介とリファクタリングについて。
Mocha+Testium+power-assertでユニットテストと同じようにE2Eテストを書くための設定やサンプル

----

## Fetch API in action
[blog.gospodarets.com/fetch\_in\_action](http://blog.gospodarets.com/fetch_in_action "Fetch API in action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">API</span> <span class="jser-tag">XHR</span></p>

Fetch APIについての紹介。
レスポンスのステータスコード、レスポンスのJSONパース、タイムアウトの問題、使い方、polyfillについて

----

## Destructuring and parameter handling in ECMAScript 6
[www.2ality.com/2015/01/es6-destructuring.html](http://www.2ality.com/2015/01/es6-destructuring.html "Destructuring and parameter handling in ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6のDestructuring(分割代入、構造化代入)と引数時の扱いについて。
またSpread operatorを使った値の展開についても書かれてる

----

## Strange JavaScript Errors and How to Fix Them
[davidwalsh.name/fix-javascript-errors](http://davidwalsh.name/fix-javascript-errors "Strange JavaScript Errors and How to Fix Them")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

JavaScriptのエラーメッセージとそれがどのようなときに起きてるエラーなのか、また修正方法について

----

## addyosmani/es6-equivalents-in-es5
[github.com/addyosmani/es6-equivalents-in-es5](https://github.com/addyosmani/es6-equivalents-in-es5 "addyosmani/es6-equivalents-in-es5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

ES6で書かれたものとES5で同等の事を行うコードを並べて、ES6の機能について紹介

----

## Getting Literal With ES6 Template Strings
[updates.html5rocks.com/2015/01/ES6-Template-Strings](http://updates.html5rocks.com/2015/01/ES6-Template-Strings "Getting Literal With ES6 Template Strings")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Template Stringsについての解説

- [TemplateStrings.md](https://gist.github.com/kuu/b7eb679a3ad48d980ed3 "TemplateStrings.md")

----

## 5分でわかる正しい Web サイト常時 SSL 化のための基礎知識 | WWW WATCH
[hyper-text.org/archives/2015/01/full\_time\_ssl\_website\_quick\_start.shtml](http://hyper-text.org/archives/2015/01/full_time_ssl_website_quick_start.shtml "5分でわかる正しい Web サイト常時 SSL 化のための基礎知識 | WWW WATCH")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">SSL</span> <span class="jser-tag">まとめ</span></p>

SSLの効果 - メリットとデメリット、SSL証明書の種類と取得方法、外部リソースの読み込みとMixed Content、HTTPSに接続を強制する方法 - HSTS、リダイレクト、CookieのSecure属性などについて

----

## ES6 Module Gotchas | geedew
[www.geedew.com/2014/12/26/es6-module-gotchas/](http://www.geedew.com/2014/12/26/es6-module-gotchas/ "ES6 Module Gotchas | geedew")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6 modulesのアンチパターンについて。
静的なものを扱うデザインであるという話、オブジェクトをexportした場合の問題、副作用を目的としたモジュールの読込方法、export defaultを出来るだけ使うべき等

----

## New animation controls in Chrome Canary | Val Head - Designer
[www.valhead.com/2015/01/06/quick-tip-chrome-animation-controls/](http://www.valhead.com/2015/01/06/quick-tip-chrome-animation-controls/ "New animation controls in Chrome Canary | Val Head - Designer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

ChromeのCSS animationのデバッグ機能についての紹介

- [New animation inspector panel in Firefox 37 - YouTube](https://www.youtube.com/watch?v=3UZdsbmYduQ "New animation inspector panel in Firefox 37 - YouTube")

----

## What the Virtual Viewport?
[updates.html5rocks.com/2015/01/virtual-viewport](http://updates.html5rocks.com/2015/01/virtual-viewport "What the Virtual Viewport?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span></p>

Chrome 39と40でviewportの仕組みが変わった。
40からLayout ViewportとVisual Viewportに分かれて処理されるようになった。(IEと同様)
ズーム時にposition: fixedな要素等の動作の違いがでる。

- [Chrome Viewports - Google スライド](https://docs.google.com/presentation/d/1nJvJqL2dw5STi5FFpR6tP371vSpDWWs5Beksbfitpzc/present "Chrome Viewports - Google スライド")
- [A tale of two viewports — part two](http://www.quirksmode.org/mobile/viewports2.html "A tale of two viewports — part two")

----

## A Journey Through Client-Side Testing with JavaScript -Telerik Developer Network
[developer.telerik.com/featured/journey-client-side-testing-javascript/](http://developer.telerik.com/featured/journey-client-side-testing-javascript/ "A Journey Through Client-Side Testing with JavaScript -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

JavaScriptのテスト全体について書かれた記事。
テストフレームワーク、Assertionライブラリ、Test Runnerなどテストを構成する要素。
mocha-phantom、karma、DalekJS、Atomusでの実行方法について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Functional programming in javascript (intro) // Speaker Deck
[speakerdeck.com/geekingfrog/functional-programming-in-javascript-intro](https://speakerdeck.com/geekingfrog/functional-programming-in-javascript-intro "Functional programming in javascript (intro) // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptと関数型プログラミングについてのスライド。

----

## Web Componentsのアクセシビリティ
[www.slideshare.net/mlca11y/web-components-43883982](http://www.slideshare.net/mlca11y/web-components-43883982 "Web Componentsのアクセシビリティ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">スライド</span></p>

Web Componentsとアクセシビリティについてのスライド。
既存要素があるケースと独自要素の場合はWAI-ARIAを使うことについて

----
<h1 class="site-genre">サイト、サービス</h1>

----

## CSS Flexbox Please!
[demo.agektmr.com/flexbox/](http://demo.agektmr.com/flexbox/ "CSS Flexbox Please!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">demo</span></p>

CSS Flexboxのプロパティをその場で変更したりして動作を試せるデモページ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Diet.js
[dietjs.com/](http://dietjs.com/ "Diet.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsのウェブアプリケーションフレームワーク

----

## yoshuawuyts/promise-each
[github.com/yoshuawuyts/promise-each](https://github.com/yoshuawuyts/promise-each "yoshuawuyts/promise-each")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promiseと組み合わせて使えるeach、every、filter、map、reduce、some等の関数をそれぞれモジュール化したもの

----

## Home | Aurelia
[aurelia.io/](http://aurelia.io/ "Home | Aurelia")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Durandalの次世代となるJavaScriptフレームワーク。 ES6(or AltJS) + jspm、two-way binding、DI、ルーティング等を盛り込んだフレームワーク。
元AngularJSチームの人が開発してる

- [Introducing Aurelia](http://blog.durandal.io/2015/01/26/introducing-aurelia/ "Introducing Aurelia")

----

## shiwano/typhen
[github.com/shiwano/typhen](https://github.com/shiwano/typhen "shiwano/typhen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

d.tsからJSON Schemaを作ったり、Handlebarsを使ったテンプレートでコードやドキュメントを出力できるツール

- [TypeScript の型定義からコードを自動生成するツールを作った - Qiita](http://qiita.com/shiwano/items/dd769ead84e0da2d349a "TypeScript の型定義からコードを自動生成するツールを作った - Qiita")

----

## Wallaby - intelligent test runner for JavaScript
[wallabyjs.com/](http://wallabyjs.com/ "Wallaby - intelligent test runner for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JetBrains</span> <span class="jser-tag">IDE</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

JetBrains IDE等と統合して使えるTest Runner。
Mocha、QUnit、Jasmine等が使えて、コードカバレッジをエディタ上に表示、テストケースを一部だけ実行などが出来る。
spy-jsの人が作ってる

----
