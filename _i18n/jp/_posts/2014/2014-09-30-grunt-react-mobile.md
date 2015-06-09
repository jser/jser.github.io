---
title: "2014-09-30のJS: Gruntの現在と未来、React.js、The Mobile Web Handbook"
author: azu
layout: post
date : 2014-09-30T22:36
category: JSer
tags:
    - JavaScript
    - Grunt
    - React
    - Flux

---

JSer.info #194 - [The State of Grunt](http://cowboy.github.io/state-of-grunt-fe-summit-2014-talk/ "The State of Grunt")というスライドでは、Gruntの現状と将来について書かれています。

GulpやBroccoliのpluginを[optional adapter](http://cowboy.github.io/state-of-grunt-fe-summit-2014-talk/#59 "plugins via optional adapter")を使ったサポート、GulpのようなStreamやPromiseベースのタスクのサポート等を予定しているそうです。

また、[最後のページ](http://cowboy.github.io/state-of-grunt-fe-summit-2014-talk/#66 "The State of Grunt")ではGruntとGulpとBroccoliのそれぞれの目的の違いについて書かれています。

----

[Get Started React.js // Speaker Deck](https://speakerdeck.com/koba04/get-started-react-dot-js "Get Started React.js // Speaker Deck")というスライドでは[React](http://facebook.github.io/react/ "React")の基本的な使い方からComponent、Prop、State等の構成要素などについて詳しく書かれています。

最近、[色々](http://maketea.co.uk/2014/06/30/building-robust-web-apps-with-react-part-4.html "Building robust web apps with React: Part 4, server-side rendering | Matt Hinchliffe, Front-End Developer")な[ところ](http://www.princeton.edu/~crmarsh/react-ssr/ "Rendering React Components on the Server | Charlie Marsh")で[SEO等の視点などから](http://blog.risingstack.com/from-angularjs-to-react-the-isomorphic-way/ "From AngularJS to React: The Isomorphic Way")もみかけるようになったReactの[Server-Side Rendering](http://reactjs.net/guides/server-side-rendering.html "Server-Side Rendering")についても触れられています。

Reactのpropとstateを使ったUIのアプローチについては[From Backbone To React: Our Experience Scaling a Web Application](http://techsonian.net/2014/09/from-backbone-to-react-our-experience-scaling-a-web-application/ "From Backbone To React: Our Experience Scaling a Web Application")も見てみると面白いかもしれません。

----

PPK([Peter-Paul Koch](http://www.quirksmode.org/about/ "Peter-Paul Koch"))さんによるWebKitやAndroidなどのモバイルブラウザにおける問題や解決方法などについて書かれた[The Mobile Web Handbook](http://www.smashingmagazine.com/2014/09/30/mobile-web-handbook-release/ "“There Are More Bugs In Mobile Than... Particles In The Universe!” | Smashing Magazine")という書籍がリリースされました。

モバイルサイトのややこしい問題などについて色々とかかれていて、viewportやTouch Eventに一章使ったりかなり特化した内容になってるようです。

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Release 0.11.0-rc · yyx990803/vue
[github.com/yyx990803/vue/releases/tag/0.11.0-rc](https://github.com/yyx990803/vue/releases/tag/0.11.0-rc "Release 0.11.0-rc · yyx990803/vue")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 0.11.0-rcリリース。

Breakingな変更も含め多数の変更が予定されてる

----
<h1 class="site-genre">アーティクル</h1>

----

## Virtual DOMのアルゴリズムが知りたくてvirtual-domのコードを読んだ話 - snyk_s log
[saneyukis.hatenablog.com/entry/2014/09/03/134858](http://saneyukis.hatenablog.com/entry/2014/09/03/134858 "Virtual DOMのアルゴリズムが知りたくてvirtual-domのコードを読んだ話 - snyk\_s log")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">VirualDOM</span> <span class="jser-tag">アルゴリズム</span> <span class="jser-tag">JavaScript</span></p>

VirtualDOMの構成要素やdiffのアルゴリズムについて

----

## JavaScript - BrowserifyからWebpackへの移行時の注意点 - Qiita
[qiita.com/derui@github/items/5233b4ef8fbde1e80d33](http://qiita.com/derui@github/items/5233b4ef8fbde1e80d33 "JavaScript - BrowserifyからWebpackへの移行時の注意点 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span></p>

Browserifyから見たWebpackのメリットについて。 Browserifyはデフォルトでは1ビルドに1ファイル出力、一方Webpackは最初から複数のファイルを吐き出せる。
(Browserifyは[factor-bundle](https://github.com/substack/factor-bundle "factor-bundle")などが必要)

また、Webpackはデフォルトで賢いビルドをするため高速にビルド出来る。
(BrowserifyはAdvanced Optionsなどで細かい指定やビルドの工夫が必要)

どちらもビルド時間の多くをSourceMap出力が占めている傾向がある。

----

## Get Started React.js // Speaker Deck
[speakerdeck.com/koba04/get-started-react-dot-js](https://speakerdeck.com/koba04/get-started-react-dot-js "Get Started React.js // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirualDOM</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

React.jsについて詳しく書かれたスライド。

JSXの使い方、Viewの構成、ImmutableなPropと状態を表すState、Component同士のやり取りやライフサイクル、CSSやアニメーション、Fluxアーキテクチャ、サーバサイドレンダリングなど

- [Fluxアーキテクチャの覚え書きを書いた - snyk\_s log](http://saneyukis.hatenablog.com/entry/2014/09/26/174750 "Fluxアーキテクチャの覚え書きを書いた - snyk\_s log")

----

## Testing Flux Applications | React
[facebook.github.io/react/blog/2014/09/24/testing-flux-applications.html](http://facebook.github.io/react/blog/2014/09/24/testing-flux-applications.html "Testing Flux Applications | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

FluxアーキテクチャをJestでテストする話。

- [Flux | Application Architecture for Building User Interfaces](http://facebook.github.io/flux/ "Flux | Application Architecture for Building User Interfaces")
- [Jest | Painless JavaScript Unit Testing](http://facebook.github.io/jest/ "Jest | Painless JavaScript Unit Testing")

----

## ECMAScript 6 promises (1/2): foundations
[www.2ality.com/2014/09/es6-promises-foundations.html](http://www.2ality.com/2014/09/es6-promises-foundations.html "ECMAScript 6 promises (1/2): foundations")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

ES6 Promiseについての連載。

JavaScriptにおける非同期処理に関連するコールスタック、イベントループ、コールバックについての解説がされている

----

## Preparing for ECMAScript 6: New String Methods
[www.sitepoint.com/preparing-ecmascript-6-new-string-methods/](http://www.sitepoint.com/preparing-ecmascript-6-new-string-methods/ "Preparing for ECMAScript 6: New String Methods")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6で入るString周りのメソッドについての解説

----

## async vs defer attributes - Growing with the Web
[www.growingwiththeweb.com/2014/02/async-vs-defer-attributes.html](http://www.growingwiththeweb.com/2014/02/async-vs-defer-attributes.html "async vs defer attributes - Growing with the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span></p>

script要素のasync属性とdefer属性の動作の違いを図解にしたもの

- [サイトに適したリソース配置とasync/defer完全マスター – レンダリング優先のグッド・プラクティス | ゆっくりと…](http://tokkono.cute.coocan.jp/blog/slow/index.php/xhtmlcss/resource-potitioning-best-practice/ "サイトに適したリソース配置とasync/defer完全マスター – レンダリング優先のグッド・プラクティス | ゆっくりと…")

----

## Dev.Opera — Better @font-face with Font Load Events
[dev.opera.com/articles/better-font-face/](https://dev.opera.com/articles/better-font-face/ "Dev.Opera — Better @font-face with Font Load Events")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">Promises</span> <span class="jser-tag">CSS</span></p>

CSS Font Loadingを使ってウェブフォントを読み込んでから適応して、FOUTを回避する事について

- [CSS Font Loading Module Level 3を試してみた - console.blog(self);](http://sadah.hatenablog.com/entry/2014/06/30/211944 "CSS Font Loading Module Level 3を試してみた - console.blog(self);")

----

## Using ServiceWorker in Chrome today - JakeArchibald.com
[jakearchibald.com/2014/using-serviceworker-today/](http://jakearchibald.com/2014/using-serviceworker-today/ "Using ServiceWorker in Chrome today - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chromeでフラグ付きで実装されたService Workerを動かす方法やオフラインキャッシュのデモ

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## The State of Grunt
[cowboy.github.io/state-of-grunt-fe-summit-2014-talk/#1](http://cowboy.github.io/state-of-grunt-fe-summit-2014-talk/#1 "The State of Grunt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Grunt</span> <span class="jser-tag">スライド</span></p>

Gruntの現状と未来についてのスライド。

Grunt 0.4ではGulpやBroccoliのプラグインも使えるようにすることやstream/promiseベースのTaskのパイプラインのサポート。

Grunt/Gulp/Broccoliの目的の違いについてまとめられてる

----

## Dropbox - guiding-through-the-javascript-frameworks.pdf
[www.dropbox.com/s/hjl3cfs36b31jja/guiding-through-the-javascript-frameworks.pdf?dl=0](https://www.dropbox.com/s/hjl3cfs36b31jja/guiding-through-the-javascript-frameworks.pdf?dl=0 "Dropbox - guiding-through-the-javascript-frameworks.pdf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

JavaScriptのAngular、Ember、Backbone、React、Ampersand.jsなどのライブラリの特徴、またそれらを使って何を解決するのかというガイドラインを示すスライド

----

## ▶ Tale of npm, css and html - YouTube
[www.youtube.com/watch?v=27GYm6nRv6E](https://www.youtube.com/watch?v=27GYm6nRv6E "▶ Tale of npm, css and html - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">browserify</span> <span class="jser-tag">CSS</span> <span class="jser-tag">動画</span></p>

Browserifyとnpmを使った開発、またBrowserifyのcss版と言えるparcelifyについてのスクリーンキャスト

<a href='https://github.com/rotundasoftware/parcelify'>https://github.com/rotundasoftware/parcelify</a>

----
<h1 class="site-genre">サイト、サービス</h1>

----

## JavaScriptが実行できるリアルタイムオンラインエディタ作ってみました | 圧縮電子どうのこうの
[polygon-planet-log.blogspot.com/2014/09/javascript-online-synchronize-editor.html](http://polygon-planet-log.blogspot.com/2014/09/javascript-online-synchronize-editor.html "JavaScriptが実行できるリアルタイムオンラインエディタ作ってみました | 圧縮電子どうのこうの")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">webservice</span></p>

コラボレーション出来るjsfiddle的なウェブサービス。

複数人で編集できカーソル位置の可視化、JavaScriptコンソールやHTMLのプレビューなどがある

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mohayonao/neume.js · GitHub
[github.com/mohayonao/neume.js](https://github.com/mohayonao/neume.js "mohayonao/neume.js · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web Audio APIを扱うライブラリ。

パフォーマンスや試行錯誤がしやすいインタフェースを目的にしている

<a href='http://mohayonao.hatenablog.com/entry/2014/09/29/123242'>http://mohayonao.hatenablog.com/entry/2014/09/29/123242</a>

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon.co.jp： JavaScriptエンジニア養成読本 [Webアプリ開発の定番構成Backbone.js+CoffeeScript+Gruntを1冊で習得! ] （Software Design plus）: 吾郷 協, 山田 順久, 竹馬 光太郎, 和智 大二郎: 本
[amazon.co.jp/dp/4774167975/](http://www.amazon.co.jp/dp/4774167975/ "この商品をチェックした人はこんな商品もチェックしています")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2014年10月18日 発売

JavaScript開発のムック本

----

## Developing a React.js Edge - O&#x27;Reilly Media
[shop.oreilly.com/product/9781939902122.do](http://shop.oreilly.com/product/9781939902122.do "Developing a React.js Edge - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">VirualDOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

React.jsについての書籍

<a href='https://github.com/rtfeldman/bleeding-edge-sample-app'>https://github.com/rtfeldman/bleeding-edge-sample-app</a>

----

## “There Are More Bugs In Mobile Than... Particles In The Universe!” | Smashing Magazine
[www.smashingmagazine.com/2014/09/30/mobile-web-handbook-release/](http://www.smashingmagazine.com/2014/09/30/mobile-web-handbook-release/ "“There Are More Bugs In Mobile Than... Particles In The Universe!” | Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">Android</span> <span class="jser-tag">mobile</span> <span class="jser-tag">web</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

PPKによるモバイル周りのJSやCSSのバグや混乱する挙動などについてのガイドラインを提供する本。

viewportや300msの遅延、ズームの動作、Touch Event、Androidなどのハマりどころについて書かれてる

----
