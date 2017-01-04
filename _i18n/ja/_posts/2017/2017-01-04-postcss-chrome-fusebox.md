---
title: "2017-01-04のJS: PostCSS概要、Chrome開発者ツール、FuseBox"
author: azu
layout: post
date : 2017-01-04T17:28
category: JSer
tags:
    - bundler
    - Tools
    - Chrome
    - PostCSS

---

JSer.info #312 - [PostCSS まとめ - Qiita](http://qiita.com/morishitter/items/4a04eb144abf49f41d7d "PostCSS まとめ - Qiita")という記事では、[PostCSS](https://github.com/postcss/postcss "PostCSS")とはどのようなものなのかについて書かれています。

PostCSSはCSSのツール基盤となるフレームワークで、CSSパーサやジェネレータなどを含んでいるもので、プラグインとしてCSSに対する様々な処理を扱えるようになっています(パーサ自体もプラグインで拡張できるのでSassなども一部扱えます。)

この記事では、PostCSSを使って動くプリプロセッサやLinterといったツールなどについて紹介されています。

----

[Optimise your web development workflow 2016](https://umaar.github.io/devtools-optimise-your-web-development-workflow-2016/#/ "Optimise your web development workflow 2016")というスライドでは、Chromeの開発者ツールの機能について紹介されています。
開発者ツールには大量の機能がありますが、GIF画像とともにそれらの機能を紹介しています。

Elements、Timeline、Networks、Auditsパネルにある機能やそれに関連する仕様やツールなども紹介しているので、
一度見てみると面白いかもしれません。

また、1Tips/1ページ形式で開発者ツールのTipsを紹介しているので合わせてみると良いかもしれません。

- [Dev Tips - Developer Tips by Umar Hansa](https://umaar.com/dev-tips/ "Dev Tips - Developer Tips by Umar Hansa")

----

[Fusebox](http://fuse-box.org/ "Fusebox")というbundler/module loaderツールが公開されています。
webpackなどが近いツールで、プラグインで変換レイヤーを追加でき、その結果を一つのファイルにまとめるbundlerです。
また、`FuseBox.import`というLoader APIも合わせて利用でき、webpackやSystemJSなどに近い機能を持っています。

高速な変換がウリの一つで、モジュールの依存関係と変換済みファイルをキャッシュすることで、再変換時の処理時間が短くできるようになっています。

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">FuseBox cache and deps.json <a href="https://t.co/4EjS62HY28">pic.twitter.com/4EjS62HY28</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/816568272736788480">January 4, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[fuse-box/fuse-box](https://github.com/fuse-box/fuse-box "fuse-box/fuse-box")のソースコードはTypeScriptで書かれていて、
まだでたばかりなのでソースコードを見てみるのも面白いかもしれません。

----

## お知らせ

- [jser/ping](https://github.com/jser/ping "jser/ping")にPingのIssueを立てると[@jser_info](https://twitter.com/jser_info "@jser_info")のTwitterに流れるようになりました
- データ分析用に[JSer.info Data Dashboard](https://jser.info/data-dashboard/ "JSer.info Data Dashboard")を作りました
    - JSer.infoの記事や紹介URLに関するデータを色々な形でみることを目的にしたページです
    - 面白そうなデータの読み方があるなら[jser/data-dashboard: JSer.info Data Dashboard.](https://github.com/jser/data-dashboard "jser/data-dashboard: JSer.info Data Dashboard.")にIssue/PRを立てると良さそうです。
    
----
<h1 class="site-genre">ヘッドライン</h1>

----

## StealJS 1.0 Release
[www.bitovi.com/blog/stealjs-1.0-release](https://www.bitovi.com/blog/stealjs-1.0-release "StealJS 1.0 Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

開発時は動的なモジュールローダで、本番時はsteal-toolsでのproduction buildでbundleできるStealJS 1.0リリース

- [Easy ES6 with StealJS - YouTube](https://www.youtube.com/watch?v=VKydmxRm6w8 "Easy ES6 with StealJS - YouTube")

----
<h1 class="site-genre">アーティクル</h1>

----

## Optimizing Page Speeds With Lazyloading | Jscrambler Blog
[blog.jscrambler.com/optimizing-page-speeds-with-lazyloading/](https://blog.jscrambler.com/optimizing-page-speeds-with-lazyloading/ "Optimizing Page Speeds With Lazyloading | Jscrambler Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AngularのルーティングとコンポーネントのLazyLoadについて

----

## Lazy Loading - React
[webpack.js.org/guides/lazy-load-react/](https://webpack.js.org/guides/lazy-load-react/ "Lazy Loading - React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span></p>

webpack2を使ったReactコンポーネントのLazyLoad方法についてのドキュメント

----

## FlowtypeでFluxアーキテクチャに型付けをするという発表をした - Please Drive Faster
[joe-re.hatenablog.com/entry/2016/12/29/204917](http://joe-re.hatenablog.com/entry/2016/12/29/204917 "FlowtypeでFluxアーキテクチャに型付けをするという発表をした - Please Drive Faster")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">Flux</span></p>

FlowTypeを使ってFluxアーキテクチャのパターンに型を付ける話

- [flowtypeによりFluxにおいて型安全を手に入れる - Qiita](http://qiita.com/joe-re/items/d6fd262a8c6017f41e22 "flowtypeによりFluxにおいて型安全を手に入れる - Qiita")

----

## Node.js Interview Questions and Answers (2017 Edition) | @RisingStack
[blog.risingstack.com/node-js-interview-questions-and-answers-2017/](http://blog.risingstack.com/node-js-interview-questions-and-answers-2017/ "Node.js Interview Questions and Answers (2017 Edition) | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span></p>

Node.jsにおいて良くある質問とその答えについてをQ&A形式で書かれたもの。
コーディングスタイル、よくある書き間違い、セキュリティ、タイミング攻撃などについて

----

## React Interview Questions
[tylermcginnis.com/react-interview-questions/](https://tylermcginnis.com/react-interview-questions/ "React Interview Questions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span></p>

Reactについての疑問をQ&A形式で書かれた記事。
Classで書くコンポーネントと関数として書くコンポーネントの違い、`refs`とは何か、`key`属性はなぜ大事なのか、コンポーネントパターンなど

----

## Writing HTML with accessibility in mind – Medium
[medium.com/@matuzo/writing-html-with-accessibility-in-mind-a62026493412](https://medium.com/@matuzo/writing-html-with-accessibility-in-mind-a62026493412 "Writing HTML with accessibility in mind – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span></p>

HTMLとアクセシビリティ(スクリーンリーダー)について
`lang`属性、`alt`属性、`<buton>`要素、landmarksについて

----

## PostCSS まとめ - Qiita
[qiita.com/morishitter/items/4a04eb144abf49f41d7d](http://qiita.com/morishitter/items/4a04eb144abf49f41d7d "PostCSS まとめ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span></p>

PostCSSの概要と特徴、作られたモチベーションについて

----

## Front-End Performance Checklist 2017 (PDF, Apple Pages) – Smashing Magazine
[www.smashingmagazine.com/2016/12/front-end-performance-checklist-2017-pdf-pages/](https://www.smashingmagazine.com/2016/12/front-end-performance-checklist-2017-pdf-pages/ "Front-End Performance Checklist 2017 (PDF, Apple Pages) – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

ウェブフロントエンドのパフォーマンスチェックリスト。
ファイルサイズ、配信方法、レンダリング、モニタリング、テスト方法などについて

----

## The Reflect API of ES6 – Zsolt Nagy
[www.zsoltnagy.eu/the-reflect-api-of-es6/](http://www.zsoltnagy.eu/the-reflect-api-of-es6/ "The Reflect API of ES6 – Zsolt Nagy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Reflect APIについての紹介記事

----

## MozAnime in 2016 | Nothing new
[birtles.wordpress.com/2016/12/27/mozanime-in-2016/](https://birtles.wordpress.com/2016/12/27/mozanime-in-2016/ "MozAnime in 2016 | Nothing new")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">animation</span></p>

2016年におけるFirefoxのWeb Animations対応やデバッグ機能の更新点について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Optimise your web development workflow 2016
[umaar.github.io/devtools-optimise-your-web-development-workflow-2016/](https://umaar.github.io/devtools-optimise-your-web-development-workflow-2016/ "Optimise your web development workflow 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">CSS</span> <span class="jser-tag">debug</span> <span class="jser-tag">slide</span> <span class="jser-tag">accessibility</span></p>

Chromeの開発者ツールについてのスライド。
主にCSS、アクセシビリティ、パフォーマンスについて豊富なGIFアニメーションと共に紹介している。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Fuse-Box bundler / API Reference
[fuse-box.org/](http://fuse-box.org/ "Fuse-Box bundler / API Reference")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

webpack/Browserifyのようなbundler、JSPM/SystemJSのようなloaderを機能を持つツール。
変換結果の依存関係とキャッシュをすることで高速な変換ができる。
プラグインで対応する変換を拡張できる

- [FuseBox — bundle your project within a fraction of a second](https://medium.com/@ivanorlov/fusebox-bundle-your-project-within-a-fraction-of-a-second-f2360ba95727 "FuseBox — bundle your project within a fraction of a second")

----

## Gothdo/range: A JavaScript implementation of the Python&#x27;s range() function.
[github.com/Gothdo/range](https://github.com/Gothdo/range "Gothdo/range: A JavaScript implementation of the Python's range() function.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Pythonの`range()`のJavaScript実装ライブラリ

----

## andywer/leakage: 🐛 Memory leak testing for node.
[github.com/andywer/leakage](https://github.com/andywer/leakage "andywer/leakage: 🐛 Memory leak testing for node.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">test</span> <span class="jser-tag">libn</span></p>

Node.jsでメモリリークのテストを書くことができるライブラリ。

----

## nolanlawson/marky: High-resolution JavaScript timer based on performance.mark() and measure()
[github.com/nolanlawson/marky](https://github.com/nolanlawson/marky "nolanlawson/marky: High-resolution JavaScript timer based on performance.mark() and measure()")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">libn</span></p>

User Timing API(`performance.mark`と`performance.measure`)ベースの処理時間計測ライブラリ

----

## maniart/diffyjs: A dependency-free motion detection library for the browser
[github.com/maniart/diffyjs](https://github.com/maniart/diffyjs "maniart/diffyjs: A dependency-free motion detection library for the browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span></p>

`MediaDevices.getUserMedia()`を使って取得した画像から、フレームごとの動きのdiffを取得できるライブラリ。
motion detectionライブラリ

----
