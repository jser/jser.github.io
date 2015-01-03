---
title: "2014-12-30のJS: jsdom 2.0.0、6to5 2.0.0、HTMLBars"
author: azu
layout: post
date : 2014-12-30T22:54
category: JSer
tags:
    - JavaScript
    - DOM
    - ECMAScript
    - テンプレート

---

JSer.info #208 - DOMのJavaScript実装(Node.jsでも動くDOMの実装)である[jsdom 2.0.0](https://github.com/tmpvar/jsdom/blob/2.0.0/Changelog.md "jsdom/Changelog.md at 2.0.0 · tmpvar/jsdom")がリリースされました。

機能的な追加ではないですが、2.0.0となったのは今までDOM Level{1,2,3}別で実装されていたが、今後は[Living Standard](https://wiki.whatwg.org/wiki/FAQ#What_does_.22Living_Standard.22_mean.3F "Living Standard")モデルで実装していくという方針を示すためだそうです。

[バージョン番号をつけるのはメリットよりもデメリットのほうが多いという過去の経験](https://plus.google.com/+HayatoIto/posts/axVAUzFEu4L "バージョン番号をつけるのはメリットよりもデメリットのほうが多いという過去の経験")やjsdom内部でも[level別だと辛い感じ](https://github.com/tmpvar/jsdom/pull/933#issuecomment-61679063 "Living standard: Add support fot NodeFilter constants by fhemberger · Pull Request #933 · tmpvar/jsdom")になってきたので、Living Standardモデルへと変えていくことになったようです。

公開APIについては殆ど変更はありませんが、内部的にかなり構造を変更していくリファクタリングをして行くようです。

----

ES6のコードをES5へ変換するツールである[6to5](https://6to5.org/ "6to5") [2.0.0](https://github.com/6to5/6to5/blob/master/CHANGELOG.md#200 "2.0.0")(現時点で2.2.0まで出ていますが)がリリースされました。

詳しくはCHANGELOGを参照してもらうといいですが、[Flow](http://flowtype.org/ "Flow")の型アノテーションがあってもパースして取り除けるように、ES5,6のpolyfillとして使用するライブラリを[Core.js](https://github.com/zloirock/core-js "Core.js")に変更、パフォーマンスの改善等が行われています。

- [6to5/CHANGELOG.md at master · 6to5/6to5](https://github.com/6to5/6to5/blob/master/CHANGELOG.md#200 "6to5/CHANGELOG.md at master · 6to5/6to5")


----

[HTMLBars - A Feature-by-Feature Review | colintoh.com](http://colintoh.com/blog/htmlbars "HTMLBars - A Feature-by-Feature Review | colintoh.com")という記事では次期Emberが採用する[HTMLBars](https://github.com/tildeio/htmlbars "htmlbars")というテンプレートエンジンの仕組みについて書かれています。

現在のEmberは[Handlebars](http://handlebarsjs.com/ "Handlebars")をそのまま使っていて、レンダリングまでに以下のようなフローが発生します。

> テンプレート -> AST -> HTML String -> DOM

[HTMLBars](https://github.com/tildeio/htmlbars "htmlbars")ではHandlebarsのSyntax自体はほぼ同じですが、レンダリングまでのフローが以下のように変更されます。

> テンプレート (HTMLBarsがコンパイル)-> JavaScript関数 -> DOM

これは、今の[React](http://facebook.github.io/react/ "React")がJSX(テンプレート)から`React.createElement`のような関数に変換するのと似ていると思います。

これにより"HTML String"をパースしなおす必要がないため、パフォーマンスが改善できるという話が書かれています。

同じような話を[#13 Virtual DOM | mozaic.fm](http://mozaic.fm/post/106264251221/13-virtual-dom "#13 Virtual DOM | mozaic.fm")で[@mizchi](https://twitter.com/mizchi "@mizchi")さんが話していたと思うので、一緒に聞くといいのかもしれません。(28:00ごろ)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v0.10.35 (Stable)
[blog.nodejs.org/2014/12/23/node-v0-10-35-stable/](http://blog.nodejs.org/2014/12/23/node-v0-10-35-stable/ "Node v0.10.35 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.10.35リリース。

http://d.hatena.ne.jp/jovi0608/20141222/1419265270 の修正が入った

----

## Ember.js - Ember.js 1.9.1 Released
[emberjs.com/blog/2014/12/23/ember-1-9-1-released.html](http://emberjs.com/blog/2014/12/23/ember-1-9-1-released.html "Ember.js - Ember.js 1.9.1 Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">XSS</span></p>

Ember.js 1.9.1 リリース。

Handlebarsテンプレートはタグのエスケープは自動でやるが、属性値にjavascript:等を指定した場合にXSSとなる可能性があったため自動的にエスケープされるように変更された

----

## Release v1.5.0 · eslint/espree
[github.com/eslint/espree/releases/tag/v1.5.0](https://github.com/eslint/espree/releases/tag/v1.5.0 "Release v1.5.0 · eslint/espree")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

esprima forkのespree 1.5.0リリース。

JSXのパースをサポート

----

## jsdom/Changelog.md at 2.0.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/2.0.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/2.0.0/Changelog.md "jsdom/Changelog.md at 2.0.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

jsdom 2.0.0リリース。

リファクタリング、内部構造を大きく変えていくリリース。

`levels`という概念を捨ててLiving Standard Modelに従うように。

非標準なAPIを標準化されたものへ変更など

----

## 6to5/CHANGELOG.md at master · 6to5/6to5
[github.com/6to5/6to5/blob/master/CHANGELOG.md#200](https://github.com/6to5/6to5/blob/master/CHANGELOG.md#200 "6to5/CHANGELOG.md at master · 6to5/6to5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ES6のコードをES5に変換する6to5 2.0.0リリース。

FlowTypeのサポート、polyfill等をcore-jsに変更、Performanceの改善、`6to5/register`に`cache`オプションの追加等

- [Flow types · Issue #260 · 6to5/6to5](https://github.com/6to5/6to5/issues/260 "Flow types · Issue #260 · 6to5/6to5")
- [zloirock/core-js](https://github.com/zloirock/core-js "zloirock/core-js")
- [Slow compilation · Issue #341 · 6to5/6to5](https://github.com/6to5/6to5/issues/341 "Slow compilation · Issue #341 · 6to5/6to5")

----

## Brackets Blog - The Free, Open Source Code Editor for the Web
[blog.brackets.io/2014/12/18/brackets-1-1-and-extract-for-brackets-0-6-now-available/](http://blog.brackets.io/2014/12/18/brackets-1-1-and-extract-for-brackets-0-6-now-available/ "Brackets Blog - The Free, Open Source Code Editor for the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">editor</span> <span class="jser-tag">ReleaseNote</span></p>

Brackets 1.1リリース。

クロスブラウザのLive Previewを実験的にサポート。

----
<h1 class="site-genre">アーティクル</h1>

----

## Shape Security Labs: Announcing the Shift JavaScript AST Specification
[engineering.shapesecurity.com/2014/12/announcing-shift-javascript-ast.html](http://engineering.shapesecurity.com/2014/12/announcing-shift-javascript-ast.html "Shape Security Labs: Announcing the Shift JavaScript AST Specification")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">spec</span></p>

SpiderMonkey ASTは内部表現として始まったので、ツールから扱いにくい部分やES6のサポートの問題がでてきた。 "Shift"プロジェクトではそのASTの仕様策定、パーサ、ジェネレータ、バリデータ、SpiderMonkey ASTからの変換ツール、Javaの実装などが公開されている。

- [Shape Security](https://github.com/shapesecurity "Shape Security")

----

## Performance Calendar » Fast-Forward Performance – The Future Looks Bright
[calendar.perfplanet.com/2014/fast-forward-performance-the-future-looks-bright/](http://calendar.perfplanet.com/2014/fast-forward-performance-the-future-looks-bright/ "Performance Calendar » Fast-Forward Performance – The Future Looks Bright")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">API</span> <span class="jser-tag">performance</span></p>

パフォーマンス改善に役立つAPI、測定をするためのAPIのまとめ。

ブラウザのサポート状態について

----

## HTMLBars - A Feature-by-Feature Review | colintoh.com
[colintoh.com/blog/htmlbars](http://colintoh.com/blog/htmlbars "HTMLBars - A Feature-by-Feature Review | colintoh.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Emberが採用する[HTMLBars](https://github.com/tildeio/htmlbars "htmlbars")について。

以前のEmberのレンダリングは[Handlebars](http://handlebarsjs.com/ "Handlebars")をそのまま使っていたため

> テンプレート -> AST -> HTML String -> DOM

というレンダリングのフローとなっていて遅かった。

HTMLBarsはHandlebarsのテンプレート記法を使うのは同様だが、上記のフローを以下のように行える。

> テンプレート (HTMLBarsがコンパイル)-> JavaScript関数(DOM API) -> DOM

このようなフローとなった理由や仕組みについて書かれている。

内部的にはHTMLBars ASTというものがあるが、レンダリングのフローではコンパイル結果の関数を使うので、HTML Stringのパースがなくなる点が大きな違い。

- [htmlbars/ARCHITECTURE.md at master · tildeio/htmlbars](https://github.com/tildeio/htmlbars/blob/master/ARCHITECTURE.md "htmlbars/ARCHITECTURE.md at master · tildeio/htmlbars")

----

## Symbols in ECMAScript 6
[www.2ality.com/2014/12/es6-symbols.html](http://www.2ality.com/2014/12/es6-symbols.html "Symbols in ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6のSymbolsについて。

Symbolの使い方、const Symbol()でのユニーク値としての利用、WeakMapと合わせてのプライベート値、メタ値との利用、iframe、なぜ文字列じゃなくてSymbolなのかについて

----

## Smashing Magazineのパフォーマンス改善ケースが凄まじい件 — MOL
[t32k.me/mol/log/style-class-conference/](http://t32k.me/mol/log/style-class-conference/ "Smashing Magazineのパフォーマンス改善ケースが凄まじい件 — MOL")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">performance</span></p>

Smashing Magazineのパフォーマンス改善について。

Critical Rendering Pathの最適化、パフォーマンス改善の指標をSpeed Index <= 1000としている点について等

- [Improving Smashing Magazine&#x27;s Performance: A Case Study - Smashing Magazine](http://www.smashingmagazine.com/2014/09/08/improving-smashing-magazine-performance-case-study/ "Improving Smashing Magazine&#x27;s Performance: A Case Study - Smashing Magazine")

----

## Functional Reactive Programming with the Power of Node.js Streams
[blog.risingstack.com/functional-reactive-programming-with-the-power-of-nodejs-streams/](http://blog.risingstack.com/functional-reactive-programming-with-the-power-of-nodejs-streams/ "Functional Reactive Programming with the Power of Node.js Streams")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">stream</span> <span class="jser-tag">関数型プログラミング</span></p>

NodeのStreamとFRPの導入的な記事。

リアクティブプログラミングはどのようなケースで有用なのか、FRPのライブラリとしてRxJSやBacon等が既にある。

またNodeのStreamとの互換性を高めたHighland.jsというライブラリの紹介記事

----

## The state of the Web Notifications API - Aurelio De Rosa blog
[aurelio.audero.it/blog/2014/10/18/state-web-notifications-api/](http://aurelio.audero.it/blog/2014/10/18/state-web-notifications-api/ "The state of the Web Notifications API - Aurelio De Rosa blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

Web Notifications APIの`events`周りの仕様がW3CとWHATWGで異なるが、それぞれのブラウザの実装はどうなっているかについて。

- [W3C vs. WhatWG HTML5 Specs - Differences Documented -Telerik Developer Network](http://developer.telerik.com/featured/w3c-vs-whatwg-html5-specs-differences-documented/ "W3C vs. WhatWG HTML5 Specs - Differences Documented -Telerik Developer Network")

----

## Javascript-globalization by rxaviers
[rxaviers.github.io/javascript-globalization/](http://rxaviers.github.io/javascript-globalization/ "Javascript-globalization by rxaviers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span> <span class="jser-tag">まとめ</span></p>

ECMA i18n APIやFormatJS等の国際化ライブラリなどの特徴や機能比較のまとめ

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Flux react現状確認会
[www.slideshare.net/VOYAGE_GROUP/flux-react](http://www.slideshare.net/VOYAGE_GROUP/flux-react "Flux react現状確認会")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">スライド</span></p>

FluxとReactについてのスライド。

アーキテクチャ = オブザーバパターン、データの一方通行性、メリット・デメリット、ViewライブラリとしてReactを選んだ理由について。

実際にFlux的にやっての本家との違いについて

- [Fluxとはなんだったのか + misc at 2014 - snyk\_s log](http://saneyukis.hatenablog.com/entry/2014/12/24/014421 "Fluxとはなんだったのか + misc at 2014 - snyk\_s log")

----

## Chrome 関連の動画に日本語字幕が付きました - Google Developer Japan Blog
[googledevjp.blogspot.com/2014/12/chrome.html](http://googledevjp.blogspot.com/2014/12/chrome.html "Chrome 関連の動画に日本語字幕が付きました - Google Developer Japan Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">翻訳</span></p>

I/O Bytes 2014のChrome関係の動画に日本語字幕がついた

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## JSVerify — property based testing for JavaScript. Like QuickCheck.
[jsverify.github.io/#jsverify](http://jsverify.github.io/#jsverify "JSVerify — property based testing for JavaScript. Like QuickCheck.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

QuickCheckを行うライブラリ。

MochaやJasmineとの連携も用意されている

----

## azu/textlint
[github.com/azu/textlint](https://github.com/azu/textlint "azu/textlint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

テキストやMarkdownをLintするツール。

ESLintのようにルールをJavaScriptで書いて拡張出来る。

- [JavaScriptでルールを書けるテキスト/Markdownの校正ツール textlint を作った | Web Scratch](http://efcl.info/2014/12/30/textlint/ "JavaScriptでルールを書けるテキスト/Markdownの校正ツール textlint を作った | Web Scratch")

----

## mapbox/pbf
[github.com/mapbox/pbf](https://github.com/mapbox/pbf "mapbox/pbf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ファイルサイズの小さいprotocol buffersの実装ライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Knockout.js - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920035367.do](http://shop.oreilly.com/product/0636920035367.do "Knockout.js - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

Knockout.jsについての書籍

----
