---
title: "2014-09-15のJS: JavaScriptエンジンの最適化、ビルドツールBroccoli"
author: azu
layout: post
date : 2014-09-15T21:24
category: JavaScript
tags:
    - 

---
JSer.info #192 - 今週は[nodeconfeu](http://nodeconfeu.com/ "Nodeland Conference 2014")があったのと、自分でも[V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch")という記事を書いた影響でV8の最適化に関するものが多いです。

[V8 Installation and d8 shell usage](https://gist.github.com/kevincennis/0cd2138c78a07412ef21 "V8 Installation and d8 shell usage") では、V8をビルドして起動オプションを使って最適化やトレースをする方法について分かりやすく紹介されています。

[V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch") では、Hidden Class等の著名な最適化がどうなると効かなくなるかを[IRHydra2](http://mrale.ph/irhydra/2/# "IRHydra2")を使って見る方法等について書かれています。

V8の仕組みやプロファイリングについては[thlorenz/v8-perf](https://github.com/thlorenz/v8-perf "thlorenz/v8-perf")に参考となる資料がまとめられていて、また同作者による[Demystifying v8 and JavaScript Performance](http://thlorenz.github.io/talks/demystifying-v8/talk.pdf "talk.key - talk.pdf")というスライドが公開されています。
(内容的にはv8-perfの一部)

---

[Intro to Broccoli](http://aexmachina.info/assets/talks/intro-to-broccoli/#1 "Intro to Broccoli") というスライドでは、ビルドツールである[Broccoli](https://github.com/broccolijs/broccoli "Broccoli")とは何かについて書かれています。

> In Rails speak Broccoli is the asset pipeline, and Grunt and Gulp are rake

というように、Railsでいうasset piplineのような効率的なビルドを目的にしています。

ビルド対象はファイル単位ではなくTreeで扱うようになっていて、その仕組みについては[Broccoli: First Beta Release](http://www.solitr.com/blog/2014/02/broccoli-first-release/ "Broccoli: First Beta Release")や[No more `grunt watch`: Modern build workflows with Broccoli - Ember Fest!](https://emberfest.eu/talks/talks_12C5ADD371A9A5D4 "Talk talks_12C5ADD371A9A5D4 - Ember Fest!")にて紹介されています。

See also : [nodeca/mincer](https://github.com/nodeca/mincer "nodeca/mincer")

---

## お知らせ

今回で192回目の更新ですが、このままのペースだと11月10日(月)に200回目となるので、
それを記念して勉強会的なイベントをやろうかと思ってます。

詳細は(まだ詳細は決まってない)以下に書いてありますが、2014年11月09日(日)を予定しています。

- [JSer.info 200回記念イベント · Issue #31 · jser/jser.info](https://github.com/jser/jser.info/issues/31 "JSer.info 200回記念イベント · Issue #31 · jser/jser.info")

まだ、参加人数とか会場も決まってないので(会場を募集しています!)、イベントページを作って詳細が決まったらもう一度お知らせします。

参加人数の参考にしたいので、参加するかもという人は [![Vote](http://voting-badge.herokuapp.com/img?url=https://github.com/jser/jser.info/issues/31)](http://voting-badge.herokuapp.com/vote?url=https://github.com/jser/jser.info/issues/31) を押しておいてもらえると助かります。

---

<h1 class="site-genre">ヘッドライン</h1>

----

## Intern 2.1 released | Blog | SitePen
[www.sitepen.com/blog/2014/09/12/intern-2-1-released/](http://www.sitepen.com/blog/2014/09/12/intern-2-1-released/ "Intern 2.1 released | Blog | SitePen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Intern 2.1リリース。

HTMLレポーター/JUnit XMLレポーターの追加。

----

## Release 3.1 “Satyameva Jayate” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/3.1.0](https://github.com/postcss/autoprefixer/releases/tag/3.1.0 "Release 3.1 “Satyameva Jayate” · postcss/autoprefixer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

autoprefixer 3.1リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## V8 Installation and d8 shell usage
[gist.github.com/kevincennis/0cd2138c78a07412ef21](https://gist.github.com/kevincennis/0cd2138c78a07412ef21 "V8 Installation and d8 shell usage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">tutorial</span></p>

d8コマンドをインストールして、最適化/非最適化、プロファイリング、GCのトレース、hidden class等のチェック方法などについてまとまってるチュートリアル

----

## V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch
[efcl.info/2014/09/13/v8-optimization-memo/](http://efcl.info/2014/09/13/v8-optimization-memo/ "V8の最適化とIRHydraでの可視化とベンチマークについてのメモ | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">まとめ</span></p>

V8のHidden Class等のJavaScriptの最適化やhot codeについて。

IRHydra2を使った最適化されてない事の可視化や参考リソースについて。

----

## 「for やめろ」またはイベントループと nextTick() - Block Rockin’ Codes
[jxck.hatenablog.com/entry/for-with-eventloop](http://jxck.hatenablog.com/entry/for-with-eventloop "「for やめろ」またはイベントループと nextTick() - Block Rockin’ Codes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span></p>

node.jsにおけるイベントループとブロッグについて。

setTimeout、process.nextTick、setImmediateの意味の違い。

I/Oイベントとそれぞれの実行タイミングについて分かりやすく解説してる。

----

## Integrating D3.js visualizations in a React app - Nicolas Hery
[nicolashery.com/integrating-d3js-visualizations-in-a-react-app/](http://nicolashery.com/integrating-d3js-visualizations-in-a-react-app/ "Integrating D3.js visualizations in a React app - Nicolas Hery")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">d3.js</span> <span class="jser-tag">DOM</span></p>

D3.jsのデータ・ドリブンのデータ更新とReactのVirtual DOMを組み合わせた話

- [D3.js の Data-Driven な DOM 操作がおもしろい - てっく煮ブログ](http://tech.nitoyon.com/ja/blog/2013/10/24/d3js/ "D3.js の Data-Driven な DOM 操作がおもしろい - てっく煮ブログ")

----

## Firefox Add-on Enables Web Development Across Browsers and Devices ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2014/09/firefox-tools-adapter/](https://hacks.mozilla.org/2014/09/firefox-tools-adapter/ "Firefox Add-on Enables Web Development Across Browsers and Devices ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">addon</span></p>

Firefoxの開発者ツールを使ってChromeやSafariで表示してるページをデバッグするアダプタのアドオン。

remotedebug.org と似ているが、共有のプロトコルの提供ではなく、Firefoxのプロトコルをベースとしてる

- [Firefox Tools Adapter - Firefox Developer Tools | MDN](https://developer.mozilla.org/en-US/docs/Tools/Firefox_Tools_Adapter "Firefox Tools Adapter - Firefox Developer Tools | MDN")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Intro to Broccoli
[aexmachina.info/assets/talks/intro-to-broccoli/#1](http://aexmachina.info/assets/talks/intro-to-broccoli/#1 "Intro to Broccoli")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">スライド</span></p>

ビルドツールであるBroccoliについてのスライド。 Railsで言えばBroccoliはasset pipelineで、GruntやGulpはrakeに当たるツール。

ビルドに焦点をおいているという特徴がある

----

## Talk talks_12C5ADD371A9A5D4 - Ember Fest!
[emberfest.eu/talks/talks_12C5ADD371A9A5D4](https://emberfest.eu/talks/talks_12C5ADD371A9A5D4 "Talk talks\_12C5ADD371A9A5D4 - Ember Fest!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">動画</span></p>

JavaScriptベースのビルドツールであるBroccoliについての動画

<a href='https://github.com/broccolijs/broccoli'>https://github.com/broccolijs/broccoli</a>

Broccoliがどのようなプロセスでファイルを処理するかについて話されてる

----

## 9 anti-patterns for node.js teams
[www.slideshare.net/jeharrell/9-antipatterns-for-nodejs-teams](http://www.slideshare.net/jeharrell/9-antipatterns-for-nodejs-teams "9 anti-patterns for node.js teams")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">スライド</span></p>

node.jsにおける9つのアンチパターンについてのスライド <a href='http://efcl.hatenablog.com/entry/2014/09/11/212846'>http://efcl.hatenablog.com/entry/2014/09/11/212846</a>

----

## 2014-09-09-performance-in-css-hikalab-yuya-saito.pdf • Droplr
[d.pr/f/sP4H](http://d.pr/f/sP4H "2014-09-09-performance-in-css-hikalab-yuya-saito.pdf • Droplr")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

CSSとパフォーマンスについてのスライド。CSSのスタイル変更がどのようなレンダリングツリーの変更/再描画を起こしてるか、それを計測する方法、回避する方法について詳しく書かれてる

----

## OSCON - React Architecture // Speaker Deck
[speakerdeck.com/vjeux/oscon-react-architecture](https://speakerdeck.com/vjeux/oscon-react-architecture "OSCON - React Architecture // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">スライド</span></p>

Reactの歴史とReactのDOM Diffについてのスライド

<a href='https://www.youtube.com/watch?v=eCf5CquV_Bw'>https://www.youtube.com/watch?v=eCf5CquV_Bw</a>

DOMのバージョン管理に擬えて、Virtual DOMのdiffの仕組みについて解説されてる

- [JavaScript’s History and How it Led To ReactJS | The New Stack](http://thenewstack.io/javascripts-history-and-how-it-led-to-reactjs/ "JavaScript’s History and How it Led To ReactJS | The New Stack")

----

## Building high quality services at Uber
[raynos.github.io/nodeconfeu2014-talk/#/](http://raynos.github.io/nodeconfeu2014-talk/#/ "Building high quality services at Uber")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">スライド</span></p>

Uber社のnode.jsを使ったプロダクションを運用するにあたってのスライド。

ログ、モニター、設定の管理、例外のログ、プロファイル、初期設定のscaffolding等のツールについて。

----

## Asynchronous JavaScript &amp; Promises
[www.innoarchitech.com/asynchronous-javascript-promises/](http://www.innoarchitech.com/asynchronous-javascript-promises/ "Asynchronous JavaScript &amp; Promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">スライド</span> <span class="jser-tag">動画</span></p>

JavaScriptの非同期処理、Promiseについての動画とスライド。

Promiseとはどういうものかについて

- [Asynchronous JavaScript &amp; Promises by Alex Castrounis](http://slides.com/alexcastrounis/async-js-promises#/ "Asynchronous JavaScript &amp; Promises by Alex Castrounis")

----

## BSidesLA Managing Content Security Policy // Speaker Deck
[speakerdeck.com/oreoshake/bsidesla-managing-content-security-policy](https://speakerdeck.com/oreoshake/bsidesla-managing-content-security-policy "BSidesLA Managing Content Security Policy // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">セキュリティ</span> <span class="jser-tag">CSP</span> <span class="jser-tag">browser</span> <span class="jser-tag">スライド</span></p>

CSPについてのスライド。

CSPとは何か、どうやって適応するか、どうやって管理するか。

CSP Lv2のhashについてやCSPレポート解析と <a href='http://caspr.io/'>http://caspr.io/</a> ついて

- [Caspr](http://caspr.io/#/ "Caspr")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Polyfill service
[cdn.polyfill.io/v1/](https://cdn.polyfill.io/v1/ "Polyfill service")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

polyfillライブラリを配信してくれるCDNサービス。

クエリでfeaturesやuaを指定してそれに対するpolyfillをまとめくれたものを配信してくれる

- [Polyfills as a service | FT Labs](http://labs.ft.com/2014/09/polyfills-as-a-service/ "Polyfills as a service | FT Labs")

----

## srcset と sizes
[terkel.github.io/srcset-sizes/](http://terkel.github.io/srcset-sizes/ "srcset と sizes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">画像</span> <span class="jser-tag">CSS</span> <span class="jser-tag">翻訳</span></p>

srcset と sizes 属性の入門の翻訳

<a href='http://ericportis.com/posts/2014/srcset-sizes/'>http://ericportis.com/posts/2014/srcset-sizes/</a>

- [Srcset and sizes の日本語訳 · terkel.jp](http://terkel.jp/archives/2014/09/srcset-sizes/ "Srcset and sizes の日本語訳 · terkel.jp")

----

## thlorenz/v8-perf
[github.com/thlorenz/v8-perf](https://github.com/thlorenz/v8-perf "thlorenz/v8-perf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">まとめ</span></p>

V8のパフォーマンスに関するレポートや資料のまとめ。

Data type、コンパイラ、最適化、GC、メモリ、CPUプロファイリング。

またfast objectであるかどうかの確認方法やプロファイルの取り方などについて

----

## Speed Hall of Fame - The Chromium Projects
[www.chromium.org/developers/speed-hall-of-fame](http://www.chromium.org/developers/speed-hall-of-fame "Speed Hall of Fame - The Chromium Projects")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">まとめ</span></p>

ChromiumやV8のパフォーマンスの最適化/向上のIssue(内容)とその結果についてまとめられてるページ

----

## DartLanguageSpecification_Japanese.pdf
[www.cresc.co.jp/tech/java/Google_Dart/DartLanguageSpecification_Japanese.pdf](http://www.cresc.co.jp/tech/java/Google_Dart/DartLanguageSpecification_Japanese.pdf "DartLanguageSpecification\_Japanese.pdf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">spec</span> <span class="jser-tag">翻訳</span></p>

Dartの仕様書日本語訳

ECMA-408版

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ES6 right now
[johnkpaul.github.io/presentations/jqcon/2014/es6-now/#/](http://johnkpaul.github.io/presentations/jqcon/2014/es6-now/#/ "ES6 right now")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

ES6の動かせるサンプルと共に機能紹介と今スグ使う設定についてのスライド

traceur(+grunt/gulp/broccoli/browserify)やes6-shimの紹介

----

## davidmarkclements/decofun
[github.com/davidmarkclements/decofun](https://github.com/davidmarkclements/decofun "davidmarkclements/decofun")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

無名関数を自動的にそのコンテキストに応じた名前を付けるデバッグツール。

----

## GraftJS/jschan · GitHub
[github.com/GraftJS/jschan](https://github.com/GraftJS/jschan "GraftJS/jschan · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

libchanのJavaScriptポート。

ネットワークを超えてChannel同士でやり取りをする。

WebSocketsとSPDYをサポートしていて、msgpackを使う

----

## uupaa/WMCache.js
[github.com/uupaa/WMCache.js](https://github.com/uupaa/WMCache.js "uupaa/WMCache.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">safari</span></p>

FileSystem, IndexedDB, Quota Management APIを使って100MB超えのテンポラリなストレージを管理するライブラリ

- [WMCache · uupaa/WMCache.js Wiki](https://github.com/uupaa/WMCache.js/wiki/WMCache "WMCache · uupaa/WMCache.js Wiki")

----

## hello.js - Javascript API for OAuth2 authentication and REST services
[adodson.com/hello.js/](http://adodson.com/hello.js/ "hello.js - Javascript API for OAuth2 authentication and REST services")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">OAuth</span> <span class="jser-tag">library</span></p>

OAuth 2対応のアプリの認証やAPIを叩く機能を持ったライブラリ。

<a href='https://auth-server.herokuapp.com/'>https://auth-server.herokuapp.com/</a> という認証のサーバを使っていて、クライアントサイトを書くだけでGitHubやFacebook等のAPIを利用できる

----

## BlackDice/lill
[github.com/BlackDice/lill](https://github.com/BlackDice/lill "BlackDice/lill")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

es6-symbolを使った linked-listの実装ライブラリ

----

## ブラウザ内で安全に文字列からDOMを組み立てるためのRickDOMというライブラリを書いた - 葉っぱ日記
[d.hatena.ne.jp/hasegawayosuke/20140912/p1](http://d.hatena.ne.jp/hasegawayosuke/20140912/p1 "ブラウザ内で安全に文字列からDOMを組み立てるためのRickDOMというライブラリを書いた - 葉っぱ日記")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

DOMParserやcreateHTMLDocumentを使って文字列から安全にDOMを組み立てるライブラリ

- [hasegawayosuke/rickdom](https://github.com/hasegawayosuke/rickdom "hasegawayosuke/rickdom")

----

## thlorenz/proxyquireify
[github.com/thlorenz/proxyquireify](https://github.com/thlorenz/proxyquireify "thlorenz/proxyquireify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">plugin</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

`require`をラップして読み込んだモジュールのメソッドのstubを行えるbrowserify plugin。

変換によってDIが行われるので元モジュールに特殊な仕組みが必要ない

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript: Novice to Ninja - O&#x27;Reilly Media
[shop.oreilly.com/product/9780992461225.do](http://shop.oreilly.com/product/9780992461225.do "JavaScript: Novice to Ninja - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2014年10月 発売

基礎から学ぶJavaScript

----