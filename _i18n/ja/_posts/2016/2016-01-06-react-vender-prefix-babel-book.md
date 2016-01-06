---
title: "2016-01-06のJS: Reactエコシステム入門、ベンダープリフィックスとウェブ標準、Babelセットアップ本"
author: azu
layout: post
date : 2016-01-06T18:22
category: JSer
tags:
    - React
    - WebKit
    - CSS
    - Babel
    - Book

---

JSer.info #260

----
<h1 class="site-genre">アーティクル</h1>

----

## petehunt/react-howto
[github.com/petehunt/react-howto](https://github.com/petehunt/react-howto "petehunt/react-howto")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

React作者によるReactのエコシステム入門のガイドライン

----

## Revisiting Firefox’s DevTools – Smashing Magazine
[www.smashingmagazine.com/2015/12/revisiting-firefox-devtools/](http://www.smashingmagazine.com/2015/12/revisiting-firefox-devtools/ "Revisiting Firefox’s DevTools – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firefox開発者ツールを改めて紹介している記事。
最近色々な機能が追加されている。

----

## Angular 2 versus React: There Will Be Blood — Medium
[medium.com/@housecor/angular-2-versus-react-there-will-be-blood-66595faafd51](https://medium.com/@housecor/angular-2-versus-react-there-will-be-blood-66595faafd51 "Angular 2 versus React: There Will Be Blood — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">React</span></p>

AngularJSとReactの対比。

> Angular 2 continues to put “JS” into HTML. React puts “HTML” into JS.

----

## Well, I&#x27;m Back: innerText: Cleaning A Dark Corner Of the Web
[robert.ocallahan.org/2016/01/innertext.html](http://robert.ocallahan.org/2016/01/innertext.html "Well, I'm Back: innerText: Cleaning A Dark Corner Of the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">DOM</span></p>

IEやWebKitにも存在する`innerText`は仕様と相互互換性がなかった。
WebKitを前提とするモバイルサイトで多く使われているため、Firefoxでも実装することとなった。
同時に仕様とテストケースを書いたという話

- [The poor, misunderstood innerText — Perfection Kills](http://perfectionkills.com/the-poor-misunderstood-innerText/ "The poor, misunderstood innerText — Perfection Kills")
- [Webkit! RESOLVED FIXED - otsukare](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")

----

## Webkit! RESOLVED FIXED - otsukare
[www.otsukare.info/2016/01/04/webkit-resolved-fixed](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">webkit</span></p>

FirefoxでCSSの`-webkit-` prefixを解釈するオプションがデフォルトで有効となった。
-webkit- prefixしか書かれてないサイトも表示できるようにするのが目的

- [1213126 – Enable layout.css.prefixes.webkit by default](https://bugzilla.mozilla.org/show_bug.cgi?id=1213126 "1213126 – Enable layout.css.prefixes.webkit by default")
- [総行数57,000の巨大CSS群をLessに書き換えた軌跡 - mixi Engineers&#x27; Blog](http://alpha.mixi.co.jp/entry/2015/12/20/000000 "総行数57,000の巨大CSS群をLessに書き換えた軌跡 - mixi Engineers&#x27; Blog")

----

## ChromeDevTool - Chrome Developer Toolsでパフォーマンス計測・改善 - Qiita
[qiita.com/y\_fujieda/items/a0a69151cf7307039f74](http://qiita.com/y_fujieda/items/a0a69151cf7307039f74 "ChromeDevTool - Chrome Developer Toolsでパフォーマンス計測・改善 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome開発者ツールのそれぞれのパネルの図解。
操作方法や項目の意味などについて書かれてる。

----

## JavaScript - AudioWorker を試してみる - Qiita
[qiita.com/mohayonao/items/ce357230946cfa2303c2](http://qiita.com/mohayonao/items/ce357230946cfa2303c2 "JavaScript - AudioWorker を試してみる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">audo</span> <span class="jser-tag">JavaScript</span></p>

Web Audio APIのAudioWorkerについて。

- [mohayonao/audio-worker-shim](https://github.com/mohayonao/audio-worker-shim "mohayonao/audio-worker-shim")

----

## Managing the private data of ES6 classes
[www.2ality.com/2016/01/private-data-classes.html](http://www.2ality.com/2016/01/private-data-classes.html "Managing the private data of ES6 classes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6 Classesでプライベート風味なデータ保持パターン

----

## Lerna を使って、 Babel や React が採用している monorepo を試してみる - Qiita
[qiita.com/kimamula/items/0b4dff363933bfe74506](http://qiita.com/kimamula/items/0b4dff363933bfe74506 "Lerna を使って、 Babel や React が採用している monorepo を試してみる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Babelのようなmonorepoをlernaを使って管理する方法について

----

## Flux explained for newbies – Part 1 | DevButze
[devbutze.com/p/216](https://devbutze.com/p/216 "Flux explained for newbies – Part 1 | DevButze")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">tutorial</span></p>

コンポーネントベースでUIを考えていった時になぜFluxのようなアーキテクチャが必要となっていくかについての連載

----

## Day 2: Testing React Applications – 12 Devs of Xmas
[12devsofxmas.co.uk/2015/12/day-2-testing-react-applications/](http://12devsofxmas.co.uk/2015/12/day-2-testing-react-applications/ "Day 2: Testing React Applications – 12 Devs of Xmas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

React Componentのテストについて。
jsdom、Enzymeを使ったテスト方法など

----

## AddyOsmani.com - Offline installation of npm packages
[addyosmani.com/blog/using-npm-offline/](https://addyosmani.com/blog/using-npm-offline/ "AddyOsmani.com - Offline installation of npm packages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span></p>

npm installをオフラインでも出来るようにするためのTips。
`--cache-min`、local-npm、npm_lazyについて

----

## the new code – Create Fullscreen HTML5 Page Background Video
[thenewcode.com/777/Create-Fullscreen-HTML5-Page-Background-Video](http://thenewcode.com/777/Create-Fullscreen-HTML5-Page-Background-Video "the new code – Create Fullscreen HTML5 Page Background Video")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span></p>

HTML5 Videoを背景に使う方法や注意点について

- [Should I use a video as a background? | CSS-Tricks](https://css-tricks.com/should-i-use-a-video-as-a-background/ "Should I use a video as a background? | CSS-Tricks")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Getting Started with Redux - Course by @dan_abramov @eggheadio
[egghead.io/series/getting-started-with-redux](https://egghead.io/series/getting-started-with-redux "Getting Started with Redux - Course by @dan\_abramov @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span></p>

Redux作者によるRedux入門のスクリーンキャスト

- [tayiorbeii/egghead.io\_redux\_course\_notes](https://github.com/tayiorbeii/egghead.io_redux_course_notes "tayiorbeii/egghead.io\_redux\_course\_notes")

----

## Node.js Interactive 2015 - YouTube
[www.youtube.com/playlist?list=PLfMzBWSH11xYjL8oFumSfzOf6-kr8\_t-o](https://www.youtube.com/playlist?list=PLfMzBWSH11xYjL8oFumSfzOf6-kr8_t-o "Node.js Interactive 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">動画</span> <span class="jser-tag">まとめ</span></p>

Node.js Interactive 2015の動画まとめ

- [Node.js Interactive 2015 | Linux Conferences and Linux Events | The Linux Foundation](http://events.linuxfoundation.org/events/node-interactive "Node.js Interactive 2015 | Linux Conferences and Linux Events | The Linux Foundation")
- [duffn/nodeinteractive-2015](https://github.com/duffn/nodeinteractive-2015 "duffn/nodeinteractive-2015")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## orizens/angular-es2015-styleguide
[github.com/orizens/angular-es2015-styleguide](https://github.com/orizens/angular-es2015-styleguide "orizens/angular-es2015-styleguide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AngularJS 1.xとES2015を組み合わせたスタイルガイド

----

## HTML 5 Canvas Cheat Sheet - WebsiteSetup.org
[websitesetup.org/html-5-canvas-cheat-sheet/](http://websitesetup.org/html-5-canvas-cheat-sheet/ "HTML 5 Canvas Cheat Sheet - WebsiteSetup.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">canvas</span> <span class="jser-tag">チートシート</span></p>

Canvasのチートシート

----

## WPO Stats
[wpostats.com/](https://wpostats.com/ "WPO Stats")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">まとめ</span></p>

ウェブパフォーマンスの最適化について書かれた記事などのまとめ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Lucifier129/react-lite
[github.com/Lucifier129/react-lite](https://github.com/Lucifier129/react-lite "Lucifier129/react-lite")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

ReactのCore APIに関しての互換実装ライブラリ。
サーバサイドレンダリング、`React.PropTypes`、addonsなどを取り除いて、より小さなファイルサイズとすることを目的としている。

----

## substack/hyperx
[github.com/substack/hyperx](https://github.com/substack/hyperx "substack/hyperx")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">library</span></p>

virtual-dom、React、hyperscriptに対応したTemplate Stringsを使ったビルダーライブラリ。

----

## narirou/jconv
[github.com/narirou/jconv](https://github.com/narirou/jconv "narirou/jconv")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">文字コード</span> <span class="jser-tag">library</span></p>

Pure JavaScriptで書かれたShift_JIS(CP932)、ISO-2022-JP(-1)、EUC-JP、UTF-8、UNICODE の相互変換を行うライブラリ

----

## unit-coverage/unit-coverage
[github.com/unit-coverage/unit-coverage](https://github.com/unit-coverage/unit-coverage "unit-coverage/unit-coverage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

コードカバレッジツール。
コード同士の関係もカバレッジのレポートに含める事が出来る。
JSCSなどで利用されている

- [Coverage report](http://jscs.info/jscs/coverage.html "Coverage report")

----
<h1 class="site-genre">書籍関係</h1>

----

## Setting up ES6 by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]
[leanpub.com/setting-up-es6](https://leanpub.com/setting-up-es6 "Setting up ES6 by Axel Rauschmayer \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ebook</span></p>

Dr.AxelのBabelを使ったES6の導入についての電子書籍。
loaderの仕組みがtranspilerやCommonJSに依存している中で、モジュール周りの挙動の誤解を解く内容が書かれてる

----
