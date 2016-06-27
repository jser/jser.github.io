---
title: "2016-06-27のJS: Babel 6.11.0、Safari TP7、Firefox 49の開発者ツール"
author: azu
layout: post
date : 2016-06-27T20:03
category: JSer
tags:
    - Babel
    - Safari
    - Firefox
    - debug

---

JSer.info #285 - Babel 6.11.0がリリースされました。

- [Release v6.11.0 · babel/babel](https://github.com/babel/babel/releases/tag/v6.11.0 "Release v6.11.0 · babel/babel")

[ES2016がリリース](http://jser.info/2016/06/21/ecmascript2016-unit2.0/)されたため、


----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v6.11.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.11.0](https://github.com/babel/babel/releases/tag/v6.11.0 "Release v6.11.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.11.0リリース。
`es2016` presetを追加、その他のProposalも現在のStageに追従。

- [tc39/proposals: Tracking ECMAScript Proposals](https://github.com/tc39/proposals "tc39/proposals: Tracking ECMAScript Proposals")

----

## Release v1.0.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v1.0.0](https://github.com/karma-runner/karma/releases/tag/v1.0.0 "Release v1.0.0 · karma-runner/karma")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Karma 1.0.0リリース。
preprocessorの実行順序をファイル種別で制御できるようになるなど

----

## jsdom/Changelog.md at 9.3.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.3.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.3.0/Changelog.md "jsdom/Changelog.md at 9.3.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.3.0リリース。
`Audio`コンストラクタのサポート、`Image`の挙動を仕様準拠となるように修正など

----

## Release Notes for Safari Technology Preview Release 7 | WebKit
[webkit.org/blog/6640/release-notes-for-safari-technology-preview-release-7/](https://webkit.org/blog/6640/release-notes-for-safari-technology-preview-release-7/ "Release Notes for Safari Technology Preview Release 7 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 7リリース。
`addEventListener`がEventListenerOptionsをサポート、`window.onerror`で`error`オブジェクトを受け取れるように。
[関数の引数における末尾カンマ](http://jeffmo.github.io/es-trailing-function-commas/)のサポート、`::placeholder`のprefixが外れるなど

- [jeffmo/es-trailing-function-commas](https://github.com/jeffmo/es-trailing-function-commas "jeffmo/es-trailing-function-commas")

----
<h1 class="site-genre">アーティクル</h1>

----

## ESLint Part 1: Exploration | Scott Nonnenberg
[blog.scottnonnenberg.com/eslint-part-1-exploration/](https://blog.scottnonnenberg.com/eslint-part-1-exploration/ "ESLint Part 1: Exploration | Scott Nonnenberg")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">tutorial</span></p>

ESLintの導入から設定についてのチュートリアル

----

## Developer Edition 49: Network Request Stack Traces and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/06/developer-edition-49-network-request-stack-traces-and-more/](https://hacks.mozilla.org/2016/06/developer-edition-49-network-request-stack-traces-and-more/ "Developer Edition 49: Network Request Stack Traces and more ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firefox 49の開発者ツールについて。
ネットワークパネルでどこから通信が発生したのかスタックトレースできるように、エラーメッセージの詳細をMDNで見られるように、アクセシビリティの改善など

- [David Baron&#x27;s weblog: Running animations on the compositor thread](http://dbaron.org/log/20150916-compositor-animations "David Baron&#x27;s weblog: Running animations on the compositor thread")
- [Developer Edition 49：ネットワークモニタでのスタックトレース表示、など | Mozilla Developer Street (modest)](https://dev.mozilla.jp/2016/06/developer-edition-49-network-request-stack-traces-and-more/ "Developer Edition 49：ネットワークモニタでのスタックトレース表示、など | Mozilla Developer Street (modest)")

----

## A 𝝺-calculus interpreter
[tadeuzagallo.com/blog/writing-a-lambda-calculus-interpreter-in-javascript/](http://tadeuzagallo.com/blog/writing-a-lambda-calculus-interpreter-in-javascript/ "A 𝝺-calculus interpreter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

JavaScriptで小さなλ言語のパーサとインタプリタを実装するチュートリアル。

----

## 15 Ways to Write Self-documenting JavaScript
[www.sitepoint.com/self-documenting-javascript/](https://www.sitepoint.com/self-documenting-javascript/ "15 Ways to Write Self-documenting JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Self-documentingなコードを書く方法について

----

## Debugging Node.js Nightlies with Chrome DevTools — Medium
[medium.com/@paul\_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27 "Debugging Node.js Nightlies with Chrome DevTools — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">V8</span></p>

Node.jsのnightlyに入ったChromeの開発者ツールでのデバッグの方法について

----

## Autoprefixer on Twitter: &quot;To clean CSS from prefixes run Autoprefixer with browsers: [] https://t.co/5CVdedVFMV&quot;
[twitter.com/autoprefixer/status/745762946626764804](https://twitter.com/autoprefixer/status/745762946626764804 "Autoprefixer on Twitter: "To clean CSS from prefixes run Autoprefixer with browsers: \[\] https://t.co/5CVdedVFMV"")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">設定</span></p>

CSSからprefixを外すには対象ブラウザの設定無しにしたAutoPrefixerを実行すれば良いというTips

----

## RxJS(5.x)で行うテストファーストな機能開発 | MMMブログ
[blog.mmmcorp.co.jp/blog/2016/06/25/testing-rxjs-5/](http://blog.mmmcorp.co.jp/blog/2016/06/25/testing-rxjs-5/ "RxJS(5.x)で行うテストファーストな機能開発 | MMMブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">testing</span></p>

RxJS 5のObservableをマーブル記法というDSLで書いてテストする方法について

----

## TypeScript の型定義ファイルと仲良くなろう - Hatena Developer Blog
[developer.hatenastaff.com/entry/2016/06/27/140931](http://developer.hatenastaff.com/entry/2016/06/27/140931 "TypeScript の型定義ファイルと仲良くなろう - Hatena Developer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScriptの型定義でのハマりどころや、方定義ファイルを読み書きに必要な知識について

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## JavaScript error reference - JavaScript | MDN
[developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors "JavaScript error reference - JavaScript | MDN")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">document</span> <span class="jser-tag">リファレンス</span></p>

JavaScriptのよくあるエラーメッセージのリファレンス。
何が問題で起きてるのか、実際に起きるサンプルコードがまとめられている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Monaco Editor
[microsoft.github.io/monaco-editor/](https://microsoft.github.io/monaco-editor/ "Monaco Editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

VS Codeのエディタ部分であるMonaco Editorが個別のパッケージとして公開された

----

## tmanderson/babelconf: Conveniently create a .babelrc configuration
[github.com/tmanderson/babelconf](https://github.com/tmanderson/babelconf "tmanderson/babelconf: Conveniently create a .babelrc configuration")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">設定</span> <span class="jser-tag">Tools</span></p>

`.babelrc` の設定を選択式で作成できるCLI

----

## thoov/mock-socket: Javascript mocking library for websockets and socket.io
[github.com/thoov/mock-socket](https://github.com/thoov/mock-socket "thoov/mock-socket: Javascript mocking library for websockets and socket.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">library</span></p>

WebSocketsとSocket.IOのモックライブラリ

----

## davidmarkclements/0x: Flame Graph Profiling with a Single Command
[github.com/davidmarkclements/0x](https://github.com/davidmarkclements/0x "davidmarkclements/0x: Flame Graph Profiling with a Single Command")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

インタラクティブなフレームグラフを作成できるツール。

Node.jsで実行したアプリのスタックトレースをフレームグラフで可視化できる

----

## markerikson/redux-ecosystem-links: A categorized list of Redux-related addons, libraries, and utilities
[github.com/markerikson/redux-ecosystem-links](https://github.com/markerikson/redux-ecosystem-links "markerikson/redux-ecosystem-links: A categorized list of Redux-related addons, libraries, and utilities")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">まとめ</span></p>

Redux関連のライブラリなどについてのまとめ

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon.co.jp： Js.next: Ecmascript 6: Aaron Frost: 洋書
[www.amazon.co.jp/Js-next-Ecmascript-6-Aaron-Frost/dp/1449336361](https://www.amazon.co.jp/Js-next-Ecmascript-6-Aaron-Frost/dp/1449336361 "Amazon.co.jp： Js.next: Ecmascript 6: Aaron Frost: 洋書")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年4月25日発売
ES6についての書籍

- [JS.Next - O&amp;#39;Reilly Media](http://shop.oreilly.com/product/0636920026396.do "JS.Next - O&amp;#39;Reilly Media")

----

## SVG Animations: From Common UX Implementations to Complex Responsive Animation: Sarah Drasner: 9781491939703: Amazon.com: Books
[www.amazon.com/SVG-Animations-Implementations-Responsive-Animation/dp/1491939702](https://www.amazon.com/SVG-Animations-Implementations-Responsive-Animation/dp/1491939702 "SVG Animations: From Common UX Implementations to Complex Responsive Animation: Sarah Drasner: 9781491939703: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">book</span></p>

2017年1月25日発売
SVGアニメーションについての書籍

----
