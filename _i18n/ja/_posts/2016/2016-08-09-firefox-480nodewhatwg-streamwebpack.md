---
title: "2016-08-09のJS: Firefox 48.0、Node/WHATWG Stream、webpackチュートリアル"
author: azu
layout: post
date : 2016-08-09T09:19
category: JSer
tags:
    - Firefo
    - Node.js
    - Stream
    - webpack

---

JSer.info #291

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox — Notes (48.0) — Mozilla
[www.mozilla.org/en-US/firefox/48.0/releasenotes/](https://www.mozilla.org/en-US/firefox/48.0/releasenotes/ "Firefox — Notes (48.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 48.0リリース。
WebWorkerでWeb Crypto APIが動くように、CSS `calc()`の入れ子をサポート。
`Element.animate()`がデフォルトで有効に、`insertAdjacentText()`の実装など

- [Firefox 48 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/48 "Firefox 48 for developers - Mozilla | MDN")
- [Firefox 48 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/48/ "Firefox 48 サイト互換性情報 | Firefox サイト互換性情報")

----

## Release Notes for Safari Technology Preview Release 10 | WebKit
[webkit.org/blog/6823/release-notes-for-safari-technology-preview-release-10/](https://webkit.org/blog/6823/release-notes-for-safari-technology-preview-release-10/ "Release Notes for Safari Technology Preview Release 10 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 10リリース。
`**`のサポート、"use strict"の挙動を仕様へ追従、DOMTokenListがiterableに、nullを空文字として扱うように色々なAPIを修正など

- [ECMAScript® 2017 Language Specification](https://tc39.github.io/ecma262/#sec-arrow-function-definitions-static-semantics-early-errors "ECMAScript® 2017 Language Specification")

----
<h1 class="site-genre">アーティクル</h1>

----

## Flow: Mapping an object — Medium
[medium.com/@thejameskyle/flow-mapping-an-object-373d64c44592](https://medium.com/@thejameskyle/flow-mapping-an-object-373d64c44592 "Flow: Mapping an object — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">JavaScript</span></p>

map-objというライブラリを例に、FlowTypeでどのように型定義をしていくかというチュートリアル

- [sindresorhus/map-obj: Map object keys and values into a new object](https://github.com/sindresorhus/map-obj "sindresorhus/map-obj: Map object keys and values into a new object")

----

## step by stepで始めるwebpack - Qiita
[qiita.com/howdy39/items/48d85c430f90a21075cd](http://qiita.com/howdy39/items/48d85c430f90a21075cd "step by stepで始めるwebpack - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpackの導入方法についてステップバイステップなチュートリアル

----

## From Mixins to Object Composition
[raganwald.com/2016/07/20/prefer-composition-to-inheritance.html](http://raganwald.com/2016/07/20/prefer-composition-to-inheritance.html "From Mixins to Object Composition")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

mixinではなく、objectのcompositionで機能拡張をする方法について

----

## JavaScript and Functional Programming – Beth Allchurch | Developer
[bethallchurch.github.io/JavaScript-and-Functional-Programming/](https://bethallchurch.github.io/JavaScript-and-Functional-Programming/ "JavaScript and Functional Programming – Beth Allchurch | Developer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptで関数型プログラミングをする場合に気をつけることやパターンについて。

----

## package.json の browser field 実践編 - Qiita
[qiita.com/shinout/items/911e024368e2cb29fd3d](http://qiita.com/shinout/items/911e024368e2cb29fd3d "package.json の browser field 実践編 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span> <span class="jser-tag">npm</span></p>

package.jsonの"browser" fieldの解釈の違いについて。
Browserify、webpack、React Native Packagerの比較

----

## project毎のnpmコマンドをいい感じにするnpmrc &amp; config達 - Qiita
[qiita.com/inuscript/items/86dbfd26abe6905756c0](http://qiita.com/inuscript/items/86dbfd26abe6905756c0 "project毎のnpmコマンドをいい感じにするnpmrc & config達 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">設定</span></p>

npmrc(npm-config)の設定について

----

## Introducing EdgeHTML 14 with the Windows 10 Anniversary Update | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/08/04/introducing-edgehtml-14/](https://blogs.windows.com/msedgedev/2016/08/04/introducing-edgehtml-14/ "Introducing EdgeHTML 14 with the Windows 10 Anniversary Update | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span></p>

Windows 10 Anniversary UpdateのEdgeHTML 14で入った機能のまとめ

----

## Animating like you just don’t care with Element.animate ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/08/animating-like-you-just-dont-care-with-element-animate/](https://hacks.mozilla.org/2016/08/animating-like-you-just-dont-care-with-element-animate/ "Animating like you just don’t care with Element.animate ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span></p>

Firefox 48で実装された`Element#animate()` APIについての解説

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Introducing A11ycasts! -- A11ycasts #01 - YouTube
[www.youtube.com/watch?v=HtTyRajRuyY](https://www.youtube.com/watch?v=HtTyRajRuyY "Introducing A11ycasts! -- A11ycasts #01 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">動画</span></p>

アクセシビリティについての動画シリーズ

- [Chrome Developers on Twitter: &amp;#34;Just launched ~ A11ycasts! A new series dedicated to teaching web accessibility. Tune in every 2 weeks! https://t.co/yZphrjpGPz&amp;#34;](https://twitter.com/ChromiumDev/status/760555781603360768 "Chrome Developers on Twitter: &amp;#34;Just launched ~ A11ycasts! A new series dedicated to teaching web accessibility. Tune in every 2 weeks! https://t.co/yZphrjpGPz&amp;#34;")

----

## stream between nodejs and whatwg // Speaker Deck
[speakerdeck.com/jxck/stream-between-nodejs-and-whatwg](https://speakerdeck.com/jxck/stream-between-nodejs-and-whatwg "stream between nodejs and whatwg // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">stream</span> <span class="jser-tag">スライド</span></p>

Node.js StreamとWHATWG Streamの違いについて。
目的が異なるため、作りも異なるという話

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Is Houdini Ready Yet?
[ishoudinireadyyet.com/](https://ishoudinireadyyet.com/ "Is Houdini Ready Yet?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">browser</span> <span class="jser-tag">まとめ</span></p>

CSS Houdiniのそれぞれの仕様とブラウザの実装状況についてまとめられたサイト

- [w3c/css-houdini-drafts: Mirror of https://hg.css-houdini.org/drafts](https://github.com/w3c/css-houdini-drafts "w3c/css-houdini-drafts: Mirror of https://hg.css-houdini.org/drafts")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Introduction · Almin.js
[almin.js.org/](https://almin.js.org/ "Introduction · Almin.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">DDD</span></p>

Flux/CQRSなライブラリであるAlminの公式サイト。
GitBookで書かれたドキュメントが置かれてる。

----

## jumpsuit/jumpsuit: Jump in. Zip up. Build great apps.
[github.com/jumpsuit/jumpsuit](https://github.com/jumpsuit/jumpsuit "jumpsuit/jumpsuit: Jump in. Zip up. Build great apps.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

View(React)、State管理なライブラリ + CLIなども含んだワンセットなライブラリ

----

## How to stub promises using Sinon.JS – Temple Coding
[templecoding.com/blog/2016/02/29/how-to-stub-promises-using-sinonjs/](https://templecoding.com/blog/2016/02/29/how-to-stub-promises-using-sinonjs/ "How to stub promises using Sinon.JS – Temple Coding")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Promises</span></p>

PromiseのstubをするSinon.jsの拡張ライブラリ

- [substantial/sinon-stub-promise: Synchronous Promise stubbing for Sinon.JS](https://github.com/substantial/sinon-stub-promise "substantial/sinon-stub-promise: Synchronous Promise stubbing for Sinon.JS")

----

## jvilk/BrowserFS: BrowserFS is an in-browser filesystem that emulates the Node JS filesystem API and supports storing and retrieving files from various backends.
[github.com/jvilk/BrowserFS](https://github.com/jvilk/BrowserFS "jvilk/BrowserFS: BrowserFS is an in-browser filesystem that emulates the Node JS filesystem API and supports storing and retrieving files from various backends.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

ブラウザ上でfs的なファイルシステムのエミュレートを行うライブラリ。
memory、localStorage、Dropboxなど色々なバックエンドを持っている

----
<h1 class="site-genre">書籍関係</h1>

----

## Test-Driving JavaScript Applications - O&#x27;Reilly Media
[shop.oreilly.com/product/9781680501742.do](http://shop.oreilly.com/product/9781680501742.do "Test-Driving JavaScript Applications - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span></p>

TDDについてのJavaScript本

----

## Understanding ECMAScript 6 - O&#x27;Reilly Media
[shop.oreilly.com/product/9781593277574.do](http://shop.oreilly.com/product/9781593277574.do "Understanding ECMAScript 6 - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

ES6について解説している書籍。
Understanding ECMAScript 6 の書籍版

- [Understanding… by Nicholas C. Zakas \[Leanpub PDF/iPad/Kindle\]](https://leanpub.com/understandinges6 "Understanding… by Nicholas C. Zakas \[Leanpub PDF/iPad/Kindle\]")

----
