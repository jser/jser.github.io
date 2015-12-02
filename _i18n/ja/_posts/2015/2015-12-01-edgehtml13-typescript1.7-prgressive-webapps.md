---
title: "2015-12-01のJS: EdgeHTML 13、TypeScript 1.7、Progressive Web Apps"
author: azu
layout: post
date : 2015-12-01T21:05
category: JSer
tags:
    - TypeScript
    - MSEdge
    - Progressive

---

JSer.info #255 - [Introducing EdgeHTML 13, our first platform update for Microsoft Edge | Microsoft Edge Dev Blog](http://blogs.windows.com/msedgedev/2015/11/16/introducing-edgehtml-13-our-first-platform-update-for-microsoft-edge/)ではMSEdgeのレンダリングエンジンであるEdgeHTML 13での変更点について書かれています。

- [Release version 10586 : Microsoft Edge Dev](https://dev.windows.com/en-us/microsoft-edge/platform/changelog/desktop/10586/?compareWith=10240 "Release version 10586 : Microsoft Edge Dev")

HTMLとCSSについてはCSS `initial`と`unset`、`a[download]`、`input[type=time]`、`<picture>`、ORTC、`<template>`などのサポートが追加されています。

また、MSEdgeのJavaScriptエンジンであるChakraもアップデートされています。
ES6 Classesとasm.jsをデフォルトサポートし、
フラグ付きでasync/await、Exponentiation operator、Destructuringのサポートが追加されています。

-----

TypeScript 1.7がリリースされています。

-  [Announcing TypeScript 1.7 - TypeScript - Site Home - MSDN Blogs](http://blogs.msdn.com/b/typescript/archive/2015/11/30/announcing-typescript-1-7.aspx)

async/awaitが`--experimentalAsyncFunctions`のフラグなしで利用可能になりました(現状では`--target es6`のみ対応)。
型として[`this`が利用できる](https://github.com/Microsoft/TypeScript/wiki/What's-new-in-TypeScript#this-typing)ようになり、`--target es6 --module`という組み合わせが利用できるようになっています。

詳しくは以下の記事を読んでみるといいです。

- [TypeScript 1.7.3 変更点 - Qiita](http://qiita.com/vvakame/items/0441f248b349eba9e267 "TypeScript 1.7.3 変更点 - Qiita")

-----

[Introducing Pokedex.org: a progressive webapp for Pokémon fans — Pocket JavaScript](http://www.pocketjavascript.com/blog/2015/11/23/introducing-pokedex-org)では[Progressive Web Apps](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/ "Progressive Web Apps")という考え方においてウェブアプリを開発した話が書かれています。

> アプリに「なっていく」とは何かなんだけど、Webアプリが「使ってるうちにネイティブアプリと同じような体験を備える」ってところなのかな。なので基本的にWebアプリというのは変わらない。
> また、「Web」というのもポイント。「『Web技術』を使ったアプリ」ではなくて、サーバにホストされURLを持つ、「Web上にあるアプリ」というのが重要。
> -- [Progressive Web Appsとは - fragmentary](http://myakura.hatenablog.com/entry/2015/11/18/053939 "Progressive Web Appsとは - fragmentary")

Progressive Web Apps自体は新しい機能や仕組みというものではなくて、そういう概念に名前をつけたものでしかないです。

細かい事は今後どこかで話題になると思うのでスルーして、[Introducing Pokedex.org: a progressive webapp for Pokémon fans](http://www.pocketjavascript.com/blog/2015/11/23/introducing-pokedex-org "Introducing Pokedex.org: a progressive webapp for Pokémon fans")の記事では、
ウェブアプリでありながらオフラインでも動作したり、60FPSのスクロールや滑らかなアニメーションを実現するための工夫について詳細に書かれています。

また[nolanlawson/pokedex.org](https://github.com/nolanlawson/pokedex.org/ "nolanlawson/pokedex.org")にソースコードが公開されているので興味がある人は読んでみるといいです。

上記の記事で参照されている[Chrome Dev Summit](https://developer.chrome.com/devsummit "Chrome Dev Summit")の発表は以下から見ることが出来ます。

- [Progressive Web Apps (Chrome Dev Summit 2015) - YouTube](https://www.youtube.com/watch?v=MyQ8mtR9WxI&list=PLNYkxOF6rcICcHeQY02XLvoGL34rZFWZn&index=9 "Progressive Web Apps (Chrome Dev Summit 2015) - YouTube")

----

## お知らせ

JSer.infoのサイト右下を見るとGitterのボタンがあります。ここから直接チャット画面を開けるようになっています。

Issueを立てるようなことでもないちょっとしたことやオススメ記事とかそういうの書く場所として適当にご利用下さい。

また、[リアルタイム版](http://realtime.jser.info/)、[Pull Requestツール](http://jser.info/contributing/ "JSer.info Pull Request Form")、[統計処理ライブラリ](https://github.com/jser/stat-js "jser/stat-js")、[トレンドビューア](http://jser.info/trends/ "JSer.info トレンド")、[画像素材](https://github.com/jser/media "jser/media")など、JSer.info関連のサイトやリポジトリが増えてきたのでREADMEで整理してあります。

記事を修正したい場合や記事を紹介してもらいたい場合など、目的別にまとめてあるので迷ったら以下を見てください。

- [jser/jser.info](https://github.com/jser/jser.info "jser/jser.info")


-----

<h1 class="site-genre">ヘッドライン</h1>

----

## AngularJS 1.5.0-beta.2 and 1.4.8 have been released
[angularjs.blogspot.jp/2015/11/angularjs-15-beta2-and-14-releases.html](http://angularjs.blogspot.jp/2015/11/angularjs-15-beta2-and-14-releases.html "AngularJS 1.5.0-beta.2 and 1.4.8 have been released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

AngularJS 1.5.0-beta.2と1.4.8リリース。

----

## V8 JavaScript Engine: V8 Release 4.8
[v8project.blogspot.jp/2015/11/v8-release-48.html](http://v8project.blogspot.jp/2015/11/v8-release-48.html "V8 JavaScript Engine: V8 Release 4.8")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.8リリース(Chrome 48で搭載)。
well-known symbolsの追加、 ArrayメソッドがArray-likeなオブジェクトを扱う際にES6の仕様へ準拠するように

- [Issue 3087 - v8 - ES6: Array.prototype.slice and friends should use ToLength instead of ToUint32 - V8 JavaScript Engine - Google Project Hosting](https://code.google.com/p/v8/issues/detail?id=3087 "Issue 3087 - v8 - ES6: Array.prototype.slice and friends should use ToLength instead of ToUint32 - V8 JavaScript Engine - Google Project Hosting")

----

## Introducing EdgeHTML 13, our first platform update for Microsoft Edge | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2015/11/16/introducing-edgehtml-13-our-first-platform-update-for-microsoft-edge/](http://blogs.windows.com/msedgedev/2015/11/16/introducing-edgehtml-13-our-first-platform-update-for-microsoft-edge/ "Introducing EdgeHTML 13, our first platform update for Microsoft Edge | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

EdgeHTML 13の変更点について。
HTMLやCSS関連では、
CSS `initial`と`unset`、`a[download]`、`input[type=time]`、`<picture>`、ORTC、`<template>`のサポート。

JavaScript関連では、ES6 Classesとasm.jsをデフォルトサポート。
フラグ付きでasync/await、Exponentiation operator、Destructuringのサポート。

- [Release version 10586 : Microsoft Edge Dev](https://dev.windows.com/en-us/microsoft-edge/platform/changelog/desktop/10586/?compareWith=10240 "Release version 10586 : Microsoft Edge Dev")

----

## Announcing TypeScript 1.7 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/11/30/announcing-typescript-1-7.aspx](http://blogs.msdn.com/b/typescript/archive/2015/11/30/announcing-typescript-1-7.aspx "Announcing TypeScript 1.7 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.7リリース。
async/awaitはフラグなしで利用できるように、Exponentiation operatorをサポート、`--target ES6`と`--module`が併用可能になるなど

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#17 "Roadmap · Microsoft/TypeScript Wiki")
- [What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-17 "What's new in TypeScript · Microsoft/TypeScript Wiki")
- [TypeScript 1.7.3 変更点 - Qiita](http://qiita.com/vvakame/items/0441f248b349eba9e267 "TypeScript 1.7.3 変更点 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing Pokedex.org: a progressive webapp for Pokémon fans — Pocket JavaScript
[www.pocketjavascript.com/blog/2015/11/23/introducing-pokedex-org](http://www.pocketjavascript.com/blog/2015/11/23/introducing-pokedex-org "Introducing Pokedex.org: a progressive webapp for Pokémon fans — Pocket JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

Progressive Web Apps(アプリになっていくウェブ)を実現する色々。
オフラインでも動作するようにしたり、
60FPSスクロールを実現するためにVirtual DOMのdiff/patchをWeb WorkerでUIから重たい処理を省き、CSSアニメーションを活用するなど

- [Progressive Web Apps: Escaping Tabs Without Losing Our Soul – Infrequently Noted](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/ "Progressive Web Apps: Escaping Tabs Without Losing Our Soul – Infrequently Noted")
- [Progressive Web Appsとは - fragmentary](http://myakura.hatenablog.com/entry/2015/11/18/053939 "Progressive Web Appsとは - fragmentary")

----

## Don't lose user and app state, use Page Visibility - igvita.com
[www.igvita.com/2015/11/20/dont-lose-user-and-app-state-use-page-visibility/](https://www.igvita.com/2015/11/20/dont-lose-user-and-app-state-use-page-visibility/ "Don't lose user and app state, use Page Visibility - igvita.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">event</span></p>

pagehideやvisibilityChangeなどの画面表示関連のイベント対応表。
各ブラウザでのサポート状況について

----

## From Karma to Mocha, with a taste of jsdom — Podio Engineering Blog — Medium
[medium.com/podio-engineering-blog/from-karma-to-mocha-with-a-taste-of-jsdom-c9c703a06b21](https://medium.com/podio-engineering-blog/from-karma-to-mocha-with-a-taste-of-jsdom-c9c703a06b21 "From Karma to Mocha, with a taste of jsdom — Podio Engineering Blog — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

KarmaからMocha+jsdomへテストを移行した話。
Isolationの仕組み、全テストの実行時間、単独のテストケース実行、監視などそれぞれの項目における比較が書かれている

----

## Configuring Babel 6
[www.2ality.com/2015/11/configuring-babel6.html](http://www.2ality.com/2015/11/configuring-babel6.html "Configuring Babel 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">設定</span></p>

Babel 6で細分化されたパッケージと基本的な使い方について

----

## RailsのAsset PipelineとPrecompileをNode.jsのみで処理できるgulp-sprocketsを作った - yo_waka&#x27;s blog
[waka.github.io/2015/11/25/gulp\_sprockets.html](http://waka.github.io/2015/11/25/gulp_sprockets.html "RailsのAsset PipelineとPrecompileをNode.jsのみで処理できるgulp-sprocketsを作った - yo_waka's blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">rails</span></p>

Sprocketsの独自ディレクティブもパースして、gulp上でビルド出来るようにするgulpプラグイン

----

## Chrome 47 WebRTC: media recording, secure origins &amp; proxy handling | Web Updates - Google Developers
[developers.google.com/web/updates/2015/10/chrome-47-webrtc](https://developers.google.com/web/updates/2015/10/chrome-47-webrtc "Chrome 47 WebRTC: media recording, secure origins & proxy handling | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 47のWebRTC関連のアップデートについて。
MediaStreamRecorderをフラグ付きで実装、`getUserMedia()`がHTTPSのみで利用可能となるなど

----

## Node.js へのcontributeの仕方 - from scratch
[yosuke-furukawa.hatenablog.com/entry/2015/12/01/093433](http://yosuke-furukawa.hatenablog.com/entry/2015/12/01/093433 "Node.js へのcontributeの仕方 - from scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">community</span> <span class="jser-tag">OSS</span></p>

Node.jsへコントリビュートする場合のポイントについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Chrome Dev Summit 2015 - YouTube
[www.youtube.com/playlist?list=PLNYkxOF6rcICcHeQY02XLvoGL34rZFWZn](https://www.youtube.com/playlist?list=PLNYkxOF6rcICcHeQY02XLvoGL34rZFWZn "Chrome Dev Summit 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">動画</span> <span class="jser-tag">イベント</span> <span class="jser-tag">まとめ</span></p>

Chrome Dev Summit 2015の動画一覧

- [Chrome Dev Summit 2015](https://developer.chrome.com/devsummit "Chrome Dev Summit 2015")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## React.js Conf | February 22 &amp; 23 2016
[conf.reactjs.com/](http://conf.reactjs.com/ "React.js Conf | February 22 & 23 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">イベント</span></p>

2016年2月22-23日にReact.js Confが開催

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## OrKoN/jsperf
[github.com/OrKoN/jsperf](https://github.com/OrKoN/jsperf "OrKoN/jsperf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">node.js</span></p>

jsperf.comのコードをNode.jsで実行できるツール

----

## kdzwinel/betwixt
[github.com/kdzwinel/betwixt](https://github.com/kdzwinel/betwixt "kdzwinel/betwixt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">proxy</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">node.js</span></p>

通信内容をキャプチャしてデバッグに利用できるローカルプロキシ。
Chrome開発者ツールのネットワークパネル風UIで通信内容を見ることが出来る。

----

## What are the best JavaScript IDEs? - Slant
[www.slant.co/topics/1686/~javascript-ides](http://www.slant.co/topics/1686/~javascript-ides "What are the best JavaScript IDEs? - Slant")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">まとめ</span></p>

JavaScriptのエディタ/IDEまとめ

----

## mweststrate/ts-npm-lint
[github.com/mweststrate/ts-npm-lint](https://github.com/mweststrate/ts-npm-lint "mweststrate/ts-npm-lint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

TypeScriptで書かれたモジュールを公開するときに`package.json`の内容などをチェック、修正するツール

----

## Home | phina.js
[phinajs.com/](http://phinajs.com/ "Home | phina.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

tmlib.jsの後継となるゲームライブラリ。
Canvasを使った描画、サウンド、入力系などゲーム作成に必要なものをサポートしてる

- [本日 JavaScript ゲームライブラリ『phina.js』をリリースしました! | phiary](http://phiary.me/phinajs-release/ "本日 JavaScript ゲームライブラリ『phina.js』をリリースしました! | phiary")

----

## mo · js - Motion Graphics For The Web
[mojs.io/](http://mojs.io/ "mo · js - Motion Graphics For The Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span></p>

モーショングラフィックライブラリ。
SVGとCSS animationを使ったアニメーションライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: What Every JavaScript Developer Should Know About ECMAScript 2015 (OdeToCode Programming Series): K. Scott Allen
[www.amazon.com/dp/B018D12X0C?tag=amazon0abac-22](http://www.amazon.com/dp/B018D12X0C?tag=amazon0abac-22 "Amazon: What Every JavaScript Developer Should Know About ECMAScript 2015 (OdeToCode Programming Series): K. Scott Allen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">kindle</span></p>

ES6についてのKindle本
100ページ程で追加された構文やオブジェクト、メソッドについて解説されてる。

----
