---
title: "2015-06-23のJS: ECMAScript 6公開、SVGガイド、JSConf US 2015"
author: azu
layout: post
date : 2015-06-23T21:06
category: 
tags:
    - ES6
    - Promise
    - SVG
    - 動画

---

JSer.info #233 - ECMAScript 2015(aka. ES6)がEcma標準として承認されました！ :tada:

- [ECMAScript 2015 is now an Ecma Standard](https://esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard "ECMAScript 2015 is now an Ecma Standard")

[Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")にPDFとHTMLでES6の仕様書が公開されています。
正式な仕様として公開されたのでこれからブラウザの実装も進んだり、学ぶためのリソースも増えてくると思います。

今だと、[WEB+DB PRESS Vol.87](http://teppeis.hatenablog.com/entry/2015/06/webdb-press-es6-and-yapc-asia "WEB+DB PRESS Vol.87")で概要を把握して、
[http://es6-features.org/](http://es6-features.org/)で簡単にどんな機能が増えたのかを見て、[tower-of-babel](https://github.com/yosuke-furukawa/tower-of-babel "tower-of-babel")で実際に書いてみたり、
もっと深く知りたい場合は[Exploring ES6](http://exploringjs.com/ "Exploring ES6")を読むなどするのが良い気がします。

以前書いた、Promise本もアップデートしているので、Promiseについてはこっちを見てみるといいかもしれません。

- [ES6がリリースされたのでPromiseについて学びましょう | Web Scratch](http://efcl.info/2015/06/23/promises-book-v1.5/ "ES6がリリースされたのでPromiseについて学びましょう | Web Scratch")

----

[A Practical Guide to SVGs on the web](https://svgontheweb.com/ "A Practical Guide to SVGs on the web")というサイトでは、現在[殆どのブラウザでサポートされている](http://caniuse.com/#feat=svg)SVGについて書かれています。

ファイルサイズの最適化や表示方法、JavaScriptやCSSとの連携方法などについて分かりやすくまとまっています。

----

[JSConf US 2015](http://2015.jsconf.us/ "JSConf US 2015 - The best conference for JS and the Web. Period")の動画が一部公開され始めています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq" frameborder="0" allowfullscreen></iframe>

それぞれの動画に字幕もついているので、気になる発表を探してみるといいかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ECMAScript 2015 is now an Ecma Standard
[esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard](https://esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard "ECMAScript 2015 is now an Ecma Standard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2015(ES6)正式リリース。

- [ECMAScript 2015 Language Specification – ECMA-262 6th Edition](http://www.ecma-international.org/ecma-262/6.0/ "ECMAScript 2015 Language Specification – ECMA-262 6th Edition")

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#560](https://github.com/babel/babel/blob/master/CHANGELOG.md#560 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 5.6.0リリース。
`--watch`開始時にパースエラーが起きてもCLIを停止しないように、transformerの一部をpluginとして分離するなど

- [transformers](https://github.com/babel/babel/commit/3247851019dd350504689ad57c42ef45eb2381c7 "transformers")
- [Babel Plugins](https://github.com/babel-plugins "Babel Plugins")

----

## qooxdoo 5.0 released | qooxdoo News
[news.qooxdoo.org/qooxdoo-5-0-released](http://news.qooxdoo.org/qooxdoo-5-0-released "qooxdoo 5.0 released | qooxdoo News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

JavaScriptのRIAフレームワークであるqooxdoo 5.0リリース。
qx.Website widgetsの追加、MSEdgeの対応、Pointer Eventsなどの対応、SVG、Fullscreen APIの対応、WebDriverを使ってテストの導入など

----

## Node v0.12.5 (Stable)
[blog.nodejs.org/2015/06/22/node-v0-12-5-stable/](http://blog.nodejs.org/2015/06/22/node-v0-12-5-stable/ "Node v0.12.5 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">セキュリティ</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.5リリース。

----

## Release JSHint 2.8.0 · jshint/jshint
[github.com/jshint/jshint/releases/tag/2.8.0](https://github.com/jshint/jshint/releases/tag/2.8.0 "Release JSHint 2.8.0 · jshint/jshint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.8.0リリース。
`module`でコードをES6 moduleとみなしてチェック出来るように、バグ修正など

----

## Node.js Foundation Advances Community Collaboration, Announces New Members and Ratified Technical Governance | The Linux Foundation
[www.linuxfoundation.org/news-media/announcements/2015/06/nodejs-foundation-advances-community-collaboration-announces-new](http://www.linuxfoundation.org/news-media/announcements/2015/06/nodejs-foundation-advances-community-collaboration-announces-new "Node.js Foundation Advances Community Collaboration, Announces New Members and Ratified Technical Governance | The Linux Foundation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js Foundationについての公式アナウンス。
Node.jsとio.jsのマージやガバナンスモデルについての同意がとれて、Linux FoundationのコラボレーションプロジェクトとしてNode.js Foundationが誕生した。

- [Node.js Foundation がコミュニティのコラボレーションを進化: 新メンバーと運用指針となる技術ガバナンスを発表 | The Linux Foundation](http://www.linuxfoundation.jp/news-media/announcements/2015/06/jp_nodejs-foundation-advances-community-collaboration-announces-new "Node.js Foundation がコミュニティのコラボレーションを進化: 新メンバーと運用指針となる技術ガバナンスを発表 | The Linux Foundation")

----
<h1 class="site-genre">アーティクル</h1>

----

## Brendan Eich » Blog Archive » From ASM.JS to WebAssembly
[brendaneich.com/2015/06/from-asm-js-to-webassembly/](https://brendaneich.com/2015/06/from-asm-js-to-webassembly/ "Brendan Eich » Blog Archive » From ASM.JS to WebAssembly")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">asm.js</span> <span class="jser-tag">JavaScript</span></p>

ブラウザ向けのバイナリフォーマットの標準化プロジェクトとしてWebAssemblyが公開された。
サイズやデコードの効率化を目的としたバイナリフォーマットで、第一段階の目標としてはasm.jsのバイナリ版相当の機能を予定している。

JavaScriptを置き換えるものではなく、JavaScriptが苦手な部分を補完できるような立ち位置であることなどが[FAQ](https://github.com/WebAssembly/design/blob/master/FAQ.md "FAQ")にかかれています。

- [主要ブラウザで実行可能なバイナリ形式「WebAssembly」の開発がスタート。Chrome、WebKit、Firefox、Microsoft Edge、LLVM、Unityらがサポートを相次いで表明 － Publickey](http://www.publickey1.jp/blog/15/webassembly.html "主要ブラウザで実行可能なバイナリ形式「WebAssembly」の開発がスタート。Chrome、WebKit、Firefox、Microsoft Edge、LLVM、Unityらがサポートを相次いで表明 － Publickey")
- [design/HighLevelGoals.md at master · WebAssembly/design](https://github.com/WebAssembly/design/blob/master/HighLevelGoals.md "design/HighLevelGoals.md at master · WebAssembly/design")
- [design/FAQ.md at master · WebAssembly/design](https://github.com/WebAssembly/design/blob/master/FAQ.md "design/FAQ.md at master · WebAssembly/design")
- [Rebuild: 97: Minimum Viable Standard (omo)](http://rebuild.fm/97/ "Rebuild: 97: Minimum Viable Standard (omo)")

----

## WebAssembly: a binary format for the web
[www.2ality.com/2015/06/web-assembly.html](http://www.2ality.com/2015/06/web-assembly.html "WebAssembly: a binary format for the web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span></p>

WebAssemblyの概要解説

----

## ES6 In Depth: Collections ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/06/es6-in-depth-collections/](https://hacks.mozilla.org/2015/06/es6-in-depth-collections/ "ES6 In Depth: Collections ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

SetとMapについて。
それぞれのメソッドの解説、JSと他の言語でのMapの特性の違い、列挙の順序問題、WeakSet、WeakMapが何故必要になるのかについてなど

----

## A Practical Guide to SVGs on the web
[svgontheweb.com/](https://svgontheweb.com/ "A Practical Guide to SVGs on the web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">browser</span></p>

SVGの使い方ガイドライン。
最適化、使い方、表示方法のまとめ、CSSやJavaScriptからの操作方法、レスポンシブ、アニメーションなどSVGについてまとまってる

----

## MIDI,JavaScript - JavaScriptでMIDIファイルを解析してみる 1 - Qiita
[qiita.com/PianoScoreJP/items/2f03ae61d91db0334d45](http://qiita.com/PianoScoreJP/items/2f03ae61d91db0334d45 "MIDI,JavaScript - JavaScriptでMIDIファイルを解析してみる 1 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span></p>

JavaScriptでMIDIファイル(SMF)を解析してヘッダ情報やトラックを取り出すチュートリアル

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf US 2015 - YouTube
[www.youtube.com/playlist?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq](https://www.youtube.com/playlist?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq "JSConf US 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

JSConf US 2015の動画が公開された。
それぞれの動画の文字起こしをしたGistも公開されている

- [JSConf US 2015 - The best conference for JS and the Web. Period](http://2015.jsconf.us/ "JSConf US 2015 - The best conference for JS and the Web. Period")
- [una/js-conf-notes](https://github.com/una/js-conf-notes "una/js-conf-notes")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## JavaScript Live
[jslive.com/](https://jslive.com/ "JavaScript Live")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

RubyFlowみたいなJavaScriptのコミュニティニュースサイト

----

## JavaScript.com
[www.javascript.com/](https://www.javascript.com/ "JavaScript.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

CodeSchoolによるJavaScript初心者向けの学習リソースの紹介、コミュニティによる記事紹介などをしているサイト

----

## Custom Elements - Explore the world of Web Components
[customelements.io/](https://customelements.io/ "Custom Elements - Explore the world of Web Components")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">検索</span></p>

Bowerかnpmのキーワードにweb-componentsがついてるものを検索出来るサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## oceanhouse21/dokker
[github.com/oceanhouse21/dokker](https://github.com/oceanhouse21/dokker "oceanhouse21/dokker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

JSDocのコメントからlodashのようなドキュメントページ/Markdownを生成してくれるツール

----

## trueadm/t7
[github.com/trueadm/t7](https://github.com/trueadm/t7 "trueadm/t7")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">VirtualDOM</span></p>

Template Stringsを使ったテンプレートライブラリ。
結果をReactやその他のvirtual-domライブラリを使ってるもの向けへ出力できる

----

## sighjs/sigh
[github.com/sighjs/sigh](https://github.com/sighjs/sigh "sighjs/sigh")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">gulp</span> <span class="jser-tag">Tools</span></p>

JavaScriptビルドツール。
gulp pluginをサポートしていて、デフォルトで並列タスク、インクリメンタルリビルド、Source Mapの対応など他のビルドツールの特徴も持たせてる
http://sighjs.github.io/

----

## eorroe/NodeList-Prototype-Extension
[github.com/eorroe/NodeList-Prototype-Extension](https://github.com/eorroe/NodeList-Prototype-Extension "eorroe/NodeList-Prototype-Extension")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

DOM NodeのCollectionに対して操作出来るライブラリ

----
