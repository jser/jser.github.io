---
title: "2015-05-19のJS: Firefox 38、Backebone 1.2.0、マイクロベンチマークの問題"
author: azu
layout: post
date : 2015-05-19T23:03
category: JSer
tags: 
    - Firefox
    - Backbone
    - MVC
    - V8
    - ベンチマーク

---


JSer.info #228 - [Firefox 38.0](https://www.mozilla.org/en-US/firefox/38.0/releasenotes/ "Firefox — Notes (38.0) — Mozilla")がリリースされました。

タブやウィンドウ間でデータのやり取りができる[BroadcastChannel API](https://hacks.mozilla.org/2015/02/broadcastchannel-api-in-firefox-38/ "BroadcastChannel API")や[HTML5 ruby tags](https://hacks.mozilla.org/2015/03/ruby-support-in-firefox-developer-edition-38/ "HTML5 ruby tags")、` <picture>`や`<img srcset>`のサポートなどが追加されています。

また、[performance.measure](http://www.sitepoint.com/discovering-user-timing-api/ "performance.measure")やFirefoxの開発者ツールで[`copy()`](https://developer.mozilla.org/ja/docs/Tools/Web_Console#Helper_commands "copy()")メソッドのサポート、[JavaScript エンジンの最適化により削除されている変数を表示](https://developer.mozilla.org/ja/docs/Tools/Debugger/How_to/Examine,_modify,_and_watch_variables)する機能など開発者ツールにも色々機能が増えています。

詳細は以下から確認できます。

- [Trainspotting: Firefox 38 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/05/trainspotting-firefox-38/ "Trainspotting: Firefox 38 ✩ Mozilla Hacks – the Web developer blog")
- [Firefox 38 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/38)
- [Firefox 38 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/38/Site_Compatibility)


----

[Backbone.js](http://backbonejs.org/ "Backbone.js") 1.2.0がリリースされました。
1年ぶりのアップデートになりますが、コミット数が多いので内部コードレベルでは結構変化しています。

- [Comparing 1.1.2...1.2.0 · jashkenas/backbone](https://github.com/jashkenas/backbone/compare/1.1.2...1.2.0 "Comparing 1.1.2...1.2.0 · jashkenas/backbone")

Viewの作成などをhookする機能の追加、モデルの"update"イベントの追加、ユニークidとなるmodeldの追加、Strict modeだと動かない問題の修正などがされています。

一部互換性のない変更も含まれているようです。

- [listenTo change in behavior, 1.2.0? · Issue #3611 · jashkenas/backbone](https://github.com/jashkenas/backbone/issues/3611 "listenTo change in behavior, 1.2.0? · Issue #3611 · jashkenas/backbone")

----

V8について色々な記事を書いてる[@mraleph](https://twitter.com/mraleph "@mraleph")さんによる[Do not Measure the Weather](http://mrale.ph/talks/goto2015/#/ "Do not Measure the Weather")というスライドでは、JavaScriptエンジンの最適化によってマイクロベンチマークが意図したものを計測できていない事がある点について実例と共に解説しています。

よくあるのがループの中で計測した処理を書いていてその結果を使っていないため、ループの中身が最適化によって空になってしまう問題などが起きています。(dead code elimination)

以下のような原則で最適化によって無意味なベンチマークにならないような方法について書かれています。

1. verify results
2. no constants
3. no loop invariants
4. no dead code
- [http://mrale.ph/talks/goto2015/#/74](http://mrale.ph/talks/goto2015/#/74)

しかし、最近のJavaScriptエンジンはホントに賢いので、それでも最適化により意図とは異なるものを計測してる場合があり、
実際にどういう事が起きているのかを[IRHydra2](http://mrale.ph/irhydra/2/# "IRHydra2")を使って見ていく方法についても書かれています。

IRHydra2については以前[V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch")という記事を書いたのでこちらも見てみるといいかもしれません。

> algorithms first, µbenchmarks last

とも書かれています。

- [The Black Cat of Microbenchmarks](http://mrale.ph/blog/2014/02/23/the-black-cat-of-microbenchmarks.html "The Black Cat of Microbenchmarks")

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Node v0.12.3 (Stable)
[blog.nodejs.org/2015/05/13/node-v0-12-3-0.12.3/](http://blog.nodejs.org/2015/05/13/node-v0-12-3-0.12.3/ "Node v0.12.3 (Stable)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>
Node v0.12.3リリース

----

## 0.9 released!
[blog.polymer-project.org/announcements/2015/05/14/0.9-release/](http://blog.polymer-project.org/announcements/2015/05/14/0.9-release/ "0.9 released!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>
polymer 0.9リリース。
0.8でexperimentalだった機能がデフォルトサポートされている。
`:root`セレクタ、Gesture、CSPのサポートやUtilの追加など。
Breaking Changeもあり、Migration guideが用意されている


- [Release notes - Polymer](https://www.polymer-project.org/0.9/docs/release-notes.html "Release notes - Polymer")
- [Migration guide - Polymer](https://www.polymer-project.org/0.9/docs/migration.html "Migration guide - Polymer")
    
----

## Ember.js - Ember.js 1.12 and 1.13 Beta (Glimmer!) Released
[emberjs.com/blog/2015/05/13/ember-1-12-released.html](http://emberjs.com/blog/2015/05/13/ember-1-12-released.html "Ember.js - Ember.js 1.12 and 1.13 Beta (Glimmer!) Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>
Ember.js 1.12と1.13 Betaリリース。
computeにgetter/setterを使った方法を追加、併せてDecoratorsを使った方法サポート予定

----

## Backbone.js
[backbonejs.org](http://backbonejs.org "Backbone.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>
Backbone.js 1.2.0リリース
Viewの作成などをhookする機能の追加、モデルの"update"イベントの追加、ユニークidとなる`modeld`の追加、ES6 modulesとして読み込んでも使えるように修正

- [Use Function(&quot;return this&quot;) to get global? · Issue #2152 · jashkenas/underscore](https://github.com/jashkenas/underscore/issues/2152 "Use Function(&quot;return this&quot;) to get global? · Issue #2152 · jashkenas/underscore")
- [ES6 moduleのtop levelにある`this`の値は何になるのか? | Web Scratch](http://efcl.info/2015/05/06/this-is-es6-module/ "ES6 moduleのtop levelにある\&#x60;this\&#x60;の値は何になるのか? | Web Scratch")
    
----

## Firefox — Notes (38.0) — Mozilla
[www.mozilla.org/en-US/firefox/38.0/releasenotes/](https://www.mozilla.org/en-US/firefox/38.0/releasenotes/ "Firefox — Notes (38.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>
Firefox 38.0リリース。
Ruby要素のサポート、WebSocketがWeb Workerで動作するように、BroadcastChannel API、`srcset`属性とpicture要素のサポート、開発者ツールで`copy`関数のサポートなど

- [Ruby support in Firefox Developer Edition 38 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/03/ruby-support-in-firefox-developer-edition-38/ "Ruby support in Firefox Developer Edition 38 ✩ Mozilla Hacks – the Web developer blog")
- [Trainspotting: Firefox 38 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/05/trainspotting-firefox-38/ "Trainspotting: Firefox 38 ✩ Mozilla Hacks – the Web developer blog")
- [Firefox 38の性能を検証 ゲーム・プラットフォームとしての優秀さを示す - Mozilla Flux](http://rockridge.hatenablog.com/entry/2015/05/13/003218 "Firefox 38の性能を検証 ゲーム・プラットフォームとしての優秀さを示す - Mozilla Flux")
- [Firefox 38 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/38 "Firefox 38 for developers - Mozilla | MDN")
- [Firefox 38 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/38/Site_Compatibility "Firefox 38 サイト互換性情報 - Mozilla | MDN")
    
----

## babel/CHANGELOG.md at v5.3.0 · babel/babel
[github.com/babel/babel/blob/v5.3.0/CHANGELOG.md#530](https://github.com/babel/babel/blob/v5.3.0/CHANGELOG.md#530 "babel/CHANGELOG.md at v5.3.0 · babel/babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>
Babel 5.3.0リリース。
5.2.0からの主な変更点としては`es7.trailingCommas` transformerの仕様追従、`retainLines`のオプション追加など

- [retainLines](http://babeljs.io/docs/usage/options/ "retainLines")
    
----

<h1 class="site-genre">アーティクル</h1>

----

## Why Babel Matters
[codemix.com/blog/why-babel-matters](http://codemix.com/blog/why-babel-matters "Why Babel Matters")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>
Babelの基本的な機能の紹介、ES.nextと言われるようなまだ標準化されてない仕様の対応、Babel pluginでのコードの最適化や型チェック、マクロなどASTを扱うプラットフォームとして見るBabelについて

----

## Function Bind Syntax · Babel
[babeljs.io/blog/2015/05/14/function-bind](https://babeljs.io/blog/2015/05/14/function-bind "Function Bind Syntax · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>
Babel 5.4でES.nextで提案されているStage 0の`::`によるBind構文の変換をサポート。
[Function Bind Syntax](https://github.com/zenparsing/es-function-bind "Function Bind Syntax")の挙動についての解説

----

## We Tested How Googlebot Crawls Javascript And Here&#x27;s What We Learned
[searchengineland.com/tested-googlebot-crawls-javascript-heres-learned-220157](http://searchengineland.com/tested-googlebot-crawls-javascript-heres-learned-220157 "We Tested How Googlebot Crawls Javascript And Here&#x27;s What We Learned")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">google</span> <span class="jser-tag">検索</span></p>
Google検索botがどこまでJavaScript等を解釈してクロールしているかの調査

----

## ES6 In Depth: Template strings ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/05/es6-in-depth-template-strings-2/](https://hacks.mozilla.org/2015/05/es6-in-depth-template-strings-2/ "ES6 In Depth: Template strings ✩ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>
Template stringsについて。
Backtickから始まるtemplate literalやtagged templateについて

----

## Dev.Opera — The State of Web Type
[dev.opera.com/articles/state-of-web-type/](https://dev.opera.com/articles/state-of-web-type/ "Dev.Opera — The State of Web Type")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">fonts</span> <span class="jser-tag">まとめ</span></p>
OpenTypeフォントに関する機能のブラウザサポートの状況についてのまとめ。
JustificationとHyphenation、Font Loadingについてなど

- [State of Web Type](http://stateofwebtype.com/ "State of Web Type")
    
----

## ブラウザでビジュアルテストをするreftest-runnerを作った | Web Scratch
[efcl.info/2015/05/14/reftest-runner/](http://efcl.info/2015/05/14/reftest-runner/ "ブラウザでビジュアルテストをするreftest-runnerを作った | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">canvas</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webdriver</span></p>
ブラウザの描画結果を比較する自動テストライブラリとコマンドラインツール。
2つのHTMLを用意して表示結果が一致するかどうかテストをするので、Canvasのテストなどに利用できる

----

## A Complete Guide to SVG Fallbacks | CSS-Tricks
[css-tricks.com/a-complete-guide-to-svg-fallbacks/](https://css-tricks.com/a-complete-guide-to-svg-fallbacks/ "A Complete Guide to SVG Fallbacks | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">まとめ</span></p>
SVG Fallbackのまとめ

----

## Bringing Node.js to Windows 10 IoT Core
[blogs.windows.com/buildingapps/2015/05/12/bringing-node-js-to-windows-10-iot-core/](http://blogs.windows.com/buildingapps/2015/05/12/bringing-node-js-to-windows-10-iot-core/ "Bringing Node.js to Windows 10 IoT Core")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>
Chakra JavaScriptエンジンを使ったNode.jsのforkが公開された。

- [Microsoft/node](https://github.com/Microsoft/node "Microsoft/node")
    
----

## BroadcastChannel API in Firefox 38 ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/02/broadcastchannel-api-in-firefox-38/](https://hacks.mozilla.org/2015/02/broadcastchannel-api-in-firefox-38/ "BroadcastChannel API in Firefox 38 ✩ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>
Firefox38でBroadcastChannel APIが実装された。
同じchannelを指定すれば、異なるタブやウィンドウ間でもメッセージのやり取りができるようになるAPI。
Blobデータのやりとりも可能

- [Broadcast Channel API - Web API Interfaces | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API "Broadcast Channel API - Web API Interfaces | MDN")
    
----

<h1 class="site-genre">スライド、動画関係</h1>

----

## Do not Measure the Weather
[mrale.ph/talks/goto2015/#/](http://mrale.ph/talks/goto2015/#/ "Do not Measure the Weather")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>
計測と最適化の問題についてのスライド。
JSエンジンはJITコンパイルするため計測結果は未最適化+最適化になる。
場合によっては計測対象がdead codeとなり最適化によって消えているかもしれないので、計測できていないケースも存在する。
そのことを実際にIRHydra2を使って検証する話

- [V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch")
- [IRHydra2](http://mrale.ph/irhydra/2/ "IRHydra2")
- [Javaの理論と実践: 欠陥マイクロベンチマークを分析する](http://www.ibm.com/developerworks/jp/java/library/j-jtp02225/ "Javaの理論と実践: 欠陥マイクロベンチマークを分析する")


----

## Making a Silky Smooth Web // Speaker Deck
[speakerdeck.com/paullewis/making-a-silky-smooth-web](https://speakerdeck.com/paullewis/making-a-silky-smooth-web "Making a Silky Smooth Web // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>
JavaScript->Style->Layout->Paint->Compositeという表示までの流れをきれいに行う方法や開発者ツールの使い方について。 requestAnimationFrameの活用

----

<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## State of Web Type
[stateofwebtype.com/](http://stateofwebtype.com/ "State of Web Type")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">検索</span></p>
ウェブフォントとtypographic機能別のブラウザサポート状況をまとめているサイト

----

<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## codemix/babel-plugin-typecheck · GitHub
[github.com/codemix/babel-plugin-typecheck](https://github.com/codemix/babel-plugin-typecheck "codemix/babel-plugin-typecheck · GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">flowtype</span></p>
flowtypeアノテーションからランタイム型チェックのコードへ変換するBabel plugin

----

## hit9/ntt
[github.com/hit9/ntt](https://github.com/hit9/ntt "hit9/ntt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>
小さなテストモジュール。
テストコードそのもので実行できるので、Mochaなどのようにrunnerにあたる部分は不要となってる

----

## watermark.js - watermarks in the browser
[brianium.github.io/watermarkjs/](http://brianium.github.io/watermarkjs/ "watermark.js - watermarks in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span> <span class="jser-tag">library</span></p>
画像のwatermarkを付けるライブラリ

----

## Quench: The Gulp file generator.
[quenchjs.com/](http://quenchjs.com/ "Quench: The Gulp file generator.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>
CSS、JavaScript、Imageについての項目を入力してgulpfileを生成してくれるツール。

----

## leebyron/testcheck-js
[github.com/leebyron/testcheck-js](https://github.com/leebyron/testcheck-js "leebyron/testcheck-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>
QuickCheckライブラリ。
JasmineとMochaの拡張が用意されてる

----