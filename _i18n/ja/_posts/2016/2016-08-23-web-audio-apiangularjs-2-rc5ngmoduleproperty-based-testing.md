---
title: "2016-08-23のJS: Web Audio APIの変更点、AngularJS 2 RC5のNgModule、Property-based Testing"
author: azu
layout: post
date : 2016-08-23T09:38
category: 
tags:
    - WebAudioAPI
    - Angular2
    - Testing

---

JSer.info #293

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v6.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.4.0/](https://nodejs.org/en/blog/release/v6.4.0/ "Node v6.4.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.4.0リリース

----

## Release v0.31.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.31.0](https://github.com/facebook/flow/releases/tag/v0.31.0 "Release v0.31.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.31.0リリース。

----

## Release Notes for Safari Technology Preview Release 11 | WebKit
[webkit.org/blog/6883/release-notes-for-safari-technology-preview-release-11/](https://webkit.org/blog/6883/release-notes-for-safari-technology-preview-release-11/ "Release Notes for Safari Technology Preview Release 11 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 11リリース。
`class extends null`の挙動をES2016準拠に、`DOMTokenList.replace()`のサポートなど

----

## WebVR 1.0 available in Firefox Nightly
[blog.mozvr.com/webvr-1-0-available-in-firefox-nightly/](https://blog.mozvr.com/webvr-1-0-available-in-firefox-nightly/ "WebVR 1.0 available in Firefox Nightly")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">VR</span></p>

WebVR 1.0 APIがFirefoxのNightlyで利用できるように

----
<h1 class="site-genre">アーティクル</h1>

----

## What’s new in Web Audio? ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/08/whats-new-in-web-audio-2/](https://hacks.mozilla.org/2016/08/whats-new-in-web-audio-2/ "What’s new in Web Audio? ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span></p>

ここ1年のWeb Audio APIの変更点について

- [What’s new in Web Audio? | Mozilla Developer Street (modest)](https://dev.mozilla.jp/2016/08/whats-new-in-web-audio-2/ "What’s new in Web Audio? | Mozilla Developer Street (modest)")

----

## Generative Testing in JavaScript — JavaScript Inside — Medium
[medium.com/javascript-inside/generative-testing-in-javascript-f91432247c27](https://medium.com/javascript-inside/generative-testing-in-javascript-f91432247c27 "Generative Testing in JavaScript — JavaScript Inside — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

JavaScriptでのProperty-based Testingについて。
そもそもどのようなアプローチのテスト手法なのかやtestcheck-jsなどの既存のライブラリについて

- [testcheck-js](https://github.com/leebyron/testcheck-js "testcheck-js")
- [jsverify/jsverify: Property-based testing for JavaScript. Like QuickCheck.](https://github.com/jsverify/jsverify "jsverify/jsverify: Property-based testing for JavaScript. Like QuickCheck.")
- [unexpected-check](http://unexpected.js.org/unexpected-check/ "unexpected-check")

----

## performance.markでパフォーマンス計測する | Web Scratch
[efcl.info/2016/08/15/performance.mark/](http://efcl.info/2016/08/15/performance.mark/ "performance.markでパフォーマンス計測する | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

`performance.mark`などのAPIを使ってある区間の処理時間を計測する方法や、パフォーマンスロガーの作り方などについて

----

## Angular2 RC5への更新とステート管理の変更、power-assertによるテストまで試す - undefined
[blog.bokuweb.me/entry/angular2\_rc5](http://blog.bokuweb.me/entry/angular2_rc5 "Angular2 RC5への更新とステート管理の変更、power-assertによるテストまで試す - undefined")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AngularJS 2 RC5で導入されたNgModuleについてや、ステート管理について。
また、`NgModule`を使ったテストについて

- [Angular 2 RC.5がリリースされました · Angular2 Info](https://ng2-info.github.io/2016/08/angular-2-rc-5/ "Angular 2 RC.5がリリースされました · Angular2 Info")
- [NgModule導入について · Angular2 Info](http://ng2-info.github.io/2016/07/preparing-for-ngmodule/ "NgModule導入について · Angular2 Info")

----

## Vue.js 2.0のFeaturesを訳してみる - Qiita
[qiita.com/prismrism/items/66a9dfc31139326911d8](http://qiita.com/prismrism/items/66a9dfc31139326911d8 "Vue.js 2.0のFeaturesを訳してみる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">翻訳</span></p>

Vue.js 2.0の変更点についての訳

----

## Writing a JavaScript Framework - Execution timing, beyond setTimeout | @RisingStack
[blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/](http://blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/ "Writing a JavaScript Framework - Execution timing, beyond setTimeout | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScriptの非同期実行に関する記事。
ECMAScript、HTML、Node.jsそれぞれのjob queueの仕組みについて。
それらを使ってどのようにレンダリングのイベントループを実装するかについて

----

## The cost of small modules | Read the Tea Leaves
[nolanlawson.com/2016/08/15/the-cost-of-small-modules/](https://nolanlawson.com/2016/08/15/the-cost-of-small-modules/ "The cost of small modules | Read the Tea Leaves")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span></p>

Browserifyやwebpack、rollupなどのモジュール数とロード時間の相関関係について。 browserifyはrequireをエミュレート、rollupなどはインライン化するなどの特徴が現れてる

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## CSS for Software Engineers for CSS Developers // Speaker Deck
[speakerdeck.com/csswizardry/css-for-software-engineers-for-css-developers](https://speakerdeck.com/csswizardry/css-for-software-engineers-for-css-developers "CSS for Software Engineers for CSS Developers // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">設計</span> <span class="jser-tag">thought</span></p>

CSSにおけるSOLIDの原則のような開発指針についてのスライド。
DRY、単一責任の原則、関心の分離、Immutability、Open/Closed、直交性など

- [Harry Roberts | CSS for Software Engineers for CSS Developers | CSS Day 2016 on Vimeo](https://vimeo.com/177216958 "Harry Roberts | CSS for Software Engineers for CSS Developers | CSS Day 2016 on Vimeo")

----

## The Progressive Framework - Google スライド
[docs.google.com/presentation/d/1WnYsxRMiNEArT3xz7xXHdKeH1C-jT92VxmptghJb5Es/present#slide=id.p](https://docs.google.com/presentation/d/1WnYsxRMiNEArT3xz7xXHdKeH1C-jT92VxmptghJb5Es/present#slide=id.p "The Progressive Framework - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Vue.js 2.0についてのスライド
規模や状況に応じてツール/フレームワークを選ぶべきという話。
Vue.js 2.0は段階を踏んで使えるよという話

----

## Keynote
[henryzoo.com/babel-plugin-slides/assets/player/KeynoteDHTMLPlayer.html#0](http://henryzoo.com/babel-plugin-slides/assets/player/KeynoteDHTMLPlayer.html#0 "Keynote")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">スライド</span></p>

Babel pluginについてのスライド。
どのような仕組みで変換されているのかをDOM APIとの対比しながら見ていく話

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## siddharthkp/auto-install: Install dependencies as you code
[github.com/siddharthkp/auto-install](https://github.com/siddharthkp/auto-install "siddharthkp/auto-install: Install dependencies as you code")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span></p>

コードの変更を監視して自動的に`npm install`してくれるツール

----

## waud/waud: Web Audio Library
[github.com/waud/waud](https://github.com/waud/waud "waud/waud: Web Audio Library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web Audio APIを使った音を再生するライブラリ。
Audio Spriteやbase64、iOSなどの再生にインタラクションが必要な物への対応など

----

## andywer/npm-launch: 🚀 Minimalistic task runner on steroids!
[github.com/andywer/npm-launch](https://github.com/andywer/npm-launch "andywer/npm-launch: 🚀 Minimalistic task runner on steroids!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

npm run-scriptの表記と互換性があるTask Runnerツール。
コメントが書けるJSONまたはNode.jsスクリプトで書ける

----
<h1 class="site-genre">書籍関係</h1>

----

## A Book Apart, Practical SVG
[abookapart.com/products/practical-svg](https://abookapart.com/products/practical-svg "A Book Apart, Practical SVG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">book</span></p>

SVGについての書籍

----

## 書籍情報―JavaScriptとWebGLによる 画像処理プログラミング
[www.kohgakusha.co.jp/books/detail/978-4-7775-1958-3](http://www.kohgakusha.co.jp/books/detail/978-4-7775-1958-3 "書籍情報―JavaScriptとWebGLによる 画像処理プログラミング")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">book</span></p>

WebGLでの画像処理についての書籍

----
