---
title: "2014-08-11のJS: WebStorm 9 EAP、Server Sent Events、IEのサポートサイクル"
author: azu
layout: post
categories:
    - JSer
tags:
    - JavaScript
    - WebStorm
    - SSE
    - IE
    - Windows

---

JSer.info #187 - [WebStorm 9 EAP](http://blog.jetbrains.com/webstorm/2014/08/webstorm-9-eap/ "WebStorm 9 EAP is Open! \| JetBrains WebStorm Blog")(Early Access Program いわゆるβ版)がリリースされました。

Live EditがNode.jsアプリにも対応したり、JavaScriptのトレーシングが行えるSpy-jsもNode.jsに対応しています。

- [Live Edit Updates in WebStorm 9 — What’s New? \| JetBrains WebStorm Blog](http://blog.jetbrains.com/webstorm/2014/08/live-edit-updates-in-webstorm-9/ "Live Edit Updates in WebStorm 9 — What’s New? | JetBrains WebStorm Blog")

spy-js for node.jsについては以下の動画で詳しく解説されていますが、Node.jsに対してそれぞれの関数などの処理時間や変数の値、returnした値などが実行後に見ることが出来ます。(実行された値が入った状態で見られるので、コードを読むのにも便利)

<iframe width="560" height="315" src="//www.youtube.com/embed/kzw8GmakYGY" frameborder="0" allowfullscreen></iframe>

Java(IntelliJ)の方ではすでに入っていましたが、新しい補完方法として**Postfix completion**がサポートされました。
これは以下のように、式の末尾に`.return<TAB>`としてスニペット的な補完をする方式です。

![gif](http://gyazo.com/095afae3db42318dfb0a1ea3f00d47d1.gif)

- [Postfix Code Completion in IntelliJ IDEA 13.1 EAP \| JetBrains IntelliJ IDEA Blog](http://blog.jetbrains.com/idea/2014/03/postfix-completion/ "Postfix Code Completion in IntelliJ IDEA 13.1 EAP | JetBrains IntelliJ IDEA Blog")
- [おもしろプラグイン：Postfix Completionプラグイン - marsのメモ](http://d.hatena.ne.jp/masanobuimai/20131218/1387292674 "おもしろプラグイン：Postfix Completionプラグイン - marsのメモ")

また、[EditorConfig](http://editorconfig.org/ "EditorConfig")、[Web Components](http://plugins.jetbrains.com/plugin/7312?pr=webStorm "Web Components")のプラグイン対応などが含まれています。

----

[Server Sent Events(SSE)の使いどころと使い方 \| GREE Engineers&#39; Blog](http://labs.gree.jp/blog/2014/08/11070/ "Server Sent Events(SSE)の使いどころと使い方 | GREE Engineers&#39; Blog") という記事では、Server Sent Eventsについて解説されています。

Server Sent Eventsは名前の通り、既存のHTTP上でサーバからのPush通信を行うW3Cで定義されてる仕様です。

昔からある手法としてのCometや、WebSocketとの違い、使ってみての長所や短所について書かれています。

現状ではサポートするブラウザによって、どの手法を使うか取捨選択するという感じだと思います。

<iframe src="http://caniuse.com/eventsource/embed/agents=desktop" width="100%" height="350px"></iframe>

----

[Stay up-to-date with Internet Explorer - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/08/07/stay-up-to-date-with-internet-explorer.aspx "Stay up-to-date with Internet Explorer - IEBlog - Site Home - MSDN Blogs") では今後(2016年1月以降)のIEのサポートライフサイクルが変更される件について書かれています。

[Internet Explorer のサポートライフサイクルが変更されます \| Hebikuzure&#39;s Tech Memo](http://hebikuzure.wordpress.com/2014/08/08/lifecycle-change-on-internet-explorer/ "Internet Explorer のサポートライフサイクルが変更されます | Hebikuzure&#39;s Tech Memo") でも解説されていますが、該当Windowsバージョンでインストール可能な最新版のIEのみをサポートというポリシーに変更されています。

このライフサイクルの変更や、開発者向けの[Internet Explorer Developer Channel](http://devchannel.modern.ie/ "Internet Explorer Developer Channel")のリリースなど、IEも他のブラウザのようにリリースサイクルが少し変わってきています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## wu.js 2.0
[fitzgeraldnick.com/weblog/58/](http://fitzgeraldnick.com/weblog/58/ "wu.js 2.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

mapやreduceのような高階関数を提供するwu.js2.0リリース。

ES6に対応してGenrator関数なども受け取って処理することが出来るようになった。

- [wu.js 2.0](http://fitzgeraldnick.com/weblog/58/ "wu.js 2.0")

----

## WebStorm 9 EAP is Open! | JetBrains WebStorm Blog
[blog.jetbrains.com/webstorm/2014/08/webstorm-9-eap/](http://blog.jetbrains.com/webstorm/2014/08/webstorm-9-eap/ "WebStorm 9 EAP is Open\! \| JetBrains WebStorm Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">ReleaseNote</span></p>

WebStorm 9EAPリリース。

Live Editの強化、JavaScriptのトレーシングを行うSpy-jsがNode.jsに対応、PhoneGap対応、`.if`などを末尾から補完出来る、Postfix templates の追加、EditorConfig、Web componentsの対応

----
<h1 class="site-genre">アーティクル</h1>

----

## Server Sent Events(SSE)の使いどころと使い方 | GREE Engineers&#x27; Blog
[labs.gree.jp/blog/2014/08/11070/](http://labs.gree.jp/blog/2014/08/11070/ "Server Sent Events(SSE)の使いどころと使い方 \| GREE Engineers&#x27; Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">W3C</span> <span class="jser-tag">XHR</span> <span class="jser-tag">WebSocket</span></p>

Server Sent Eventsについての解説。

Cometと違い標準仕様が定義されている点や、WebSocketと違いHTTPを使うため通信的な互換性が高いあり、Polyfillが作れる事や現状の問題点について書かれている

- [Server Side Events](http://www.slideshare.net/thepilif/server-side-events "Server Side Events")
- [リアルタイムWebの栄光を願い\!\! これから死に行くせめてものこの間に\!\! SSEの戦術的価値を説きます\!\!](http://0-9.sakura.ne.jp/pub/HTML5han/start.html "リアルタイムWebの栄光を願い\!\! これから死に行くせめてものこの間に\!\! SSEの戦術的価値を説きます\!\!")
- [Fanout Blog » You might not need a WebSocket](http://blog.fanout.io/2014/06/24/you-might-not-need-a-websocket/ "Fanout Blog » You might not need a WebSocket") (翻訳: [【翻訳】WebSocketはもう必要ないかも \| POSTD](http://postd.cc/you-might-not-need-a-websocket/ "【翻訳】WebSocketはもう必要ないかも | POSTD"))

----

## The State of the Componentised Web - Blog - Events, News, and Videos for Web Designers and Developers
[www.futureinsights.com/home/the-state-of-the-componentised-web.html](http://www.futureinsights.com/home/the-state-of-the-componentised-web.html "The State of the Componentised Web - Blog - Events, News, and Videos for Web Designers and Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">WebComponents</span></p>

ウェブにおけるコンポーネントの流れについて。

AngularやEmberなどがもつコンポーネントを作る機能の紹介とWeb componentsについて簡単にまとまってる

----

## Why Web Components Are Ready For Production -Telerik Developer Network
[developer.telerik.com/featured/web-components-ready-production/](http://developer.telerik.com/featured/web-components-ready-production/ "Why Web Components Are Ready For Production -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Web componentsは複雑で現時点ではpolyfillは難しいが、Custom Elementに関してはシンプルなAPIであるためPolyfillが簡単で、現実に使うことができるという話

----

## Best Practices for Building Angular.js Apps with BrowerifyModern Web
[medium.com/@dickeyxxx/best-practices-for-building-angular-js-apps-266c1a4a6917](http://medium.com/@dickeyxxx/best-practices-for-building-angular-js-apps-266c1a4a6917 "Best Practices for Building Angular.js Apps with BrowerifyModern Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">browserify</span></p>

Angular.JSにはmodule機能があるため、BrowserifyやRequire.JSのようなビルドを使わなくてもconcatするだけでも問題ないという話。

concatでもsourcemapは対応できて、何よりシンプル。

----

## Stay up-to-date with Internet Explorer - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/08/07/stay-up-to-date-with-internet-explorer.aspx](http://blogs.msdn.com/b/ie/archive/2014/08/07/stay-up-to-date-with-internet-explorer.aspx "Stay up-to-date with Internet Explorer - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">ReleaseNote</span></p>

2016年1月12日からWindows OSとIEのバージョンのサポートサイクルが変更される。

OSごとの最新版のIEのみをサポート対象として、後方互換性はエンタープライズモードを使えという方針になった

- [Internet Explorer のサポートライフサイクルが変更されます \| Hebikuzure&#x27;s Tech Memo](http://hebikuzure.wordpress.com/2014/08/08/lifecycle-change-on-internet-explorer/ "Internet Explorer のサポートライフサイクルが変更されます \| Hebikuzure&#x27;s Tech Memo")

----

## Speeding up AngularJS apps with simple optimizations - Tutorial - Binpress
[www.binpress.com/tutorial/speeding-up-angular-js-with-simple-optimizations/135](http://www.binpress.com/tutorial/speeding-up-angular-js-with-simple-optimizations/135 "Speeding up AngularJS apps with simple optimizations - Tutorial - Binpress")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">performance</span></p>

AngularJSパフォーマンス改善Tips.

`{{ ::title }}` 一度きりのバインディング、$scope.$apply() と $scope.$digest()の違い、ng-repeat、ディレクティブ内でのDOM操作について

----

## Using PDF.js web worker cross domain (CORS) | ColonelPanic
[colonelpanic.net/2014/08/using-pdf-js-web-worker-cross-domain-cors/](http://colonelpanic.net/2014/08/using-pdf-js-web-worker-cross-domain-cors/ "Using PDF.js web worker cross domain (CORS) \| ColonelPanic")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span></p>

WebWorker内でXHRをして取得したリソースを、`URL.createObjectURL`でblob URLにして、blob URLを受け取って使うという話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## tc39-notes/es6/2014-07 at master · rwaldron/tc39-notes
[github.com/rwaldron/tc39-notes/tree/master/es6/2014-07](https://github.com/rwaldron/tc39-notes/tree/master/es6/2014-07 "tc39-notes/es6/2014-07 at master · rwaldron/tc39-notes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">資料</span></p>

2014年7月度のECMAScriptの仕様策定に関するTC39 Meeting Notesが公開された。

test262の大幅な改善、SIMD-128、指数演算子についてなど

- [bterlson/test262-harness](https://github.com/bterlson/test262-harness "bterlson/test262-harness")
- [simd-128-tc39.pdf](http://esdiscuss.org/notes/2014-07/simd-128-tc39.pdf "simd-128-tc39.pdf")
- [Exponentiation Operator: \*\*](https://gist.github.com/rwaldron/ebe0f4d2d267370be882 "Exponentiation Operator: \*\*")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## trek/pretender
[github.com/trek/pretender](https://github.com/trek/pretender "trek/pretender")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span></p>

HTTPモックライブラリ。

XHRをFakeXHRにすり替えておき、リクエストに対するレスポンスの定義して、任意のリソースへのリクエストをテストするモックライブラリ。

- [trek/FakeXMLHttpRequest](https://github.com/trek/FakeXMLHttpRequest "trek/FakeXMLHttpRequest")

----

## github/time-elements
[github.com/github/time-elements](https://github.com/github/time-elements "github/time-elements")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">github</span> <span class="jser-tag">WebComponents</span></p>

GitHubで使われている`<time>`のCustom Elementsライブラリ

----

## Wisembly/basil.js
[github.com/Wisembly/basil.js](https://github.com/Wisembly/basil.js "Wisembly/basil.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

localstorage, cookie ,session storage , in memoryにおいて統一的なAPIで扱えるメソッドを提供してくれるライブラリ。

----

## rakuten-nlp/rakutenma
[github.com/rakuten-nlp/rakutenma](https://github.com/rakuten-nlp/rakutenma "rakuten-nlp/rakutenma")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

形態素解析器ライブラリ。

日本語と中国語の文から単語単位に分割し、品詞を付与出来る

- [Twitter / rakuten\_tech: 楽天技術研究所は本日、JavaScript版・形態素解析器R ...](https://twitter.com/rakuten_tech/status/496913434668064768 "Twitter / rakuten\_tech: 楽天技術研究所は本日、JavaScript版・形態素解析器R ...")

----
