---
title: "2016-03-03のJS: Ember.js LTS、ECMA i18n API 3rd Edition RC、jQuery 3での変更点"
author: azu
layout: post
date : 2016-03-03T21:53
category: JSer
tags:
    - Ember
    - i18n
    - ECMAScript
    - jQuery

---

JSer.info #268 - [Ember.js - Announcing Ember's First LTS Release](http://emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html "Ember.js - Announcing Ember&#39;s First LTS Release")ではEmber.jsのLTS(Long Term Support)について書かれています。

[Ember.js 2.4](http://emberjs.com/blog/2016/02/29/ember-2-4-released.html "Ember.js 2.4")が最初のLTSリリースとなります。

![LTS](http://emberjs.com/images/blog/2016-02/Releases@3x.svg)

LTSでは36週の間バグ修正のリリースが行われ、60週間はセキュリティパッチのリリースが行われるリリースサイクルになります。
つまりEmber.js 2.4は2016年11月までバグ修正が行われ、2017年4月までセキュリティリリースが継続される形になります。

----

ECMA-402ことECMAScript i18n APIの3rd EditionがRCリリースされました。

- [ECMAScript® 2016 Internationalization API Specification (3rd Edition)](http://tc39.github.io/ecma402/ "ECMAScript® 2016 Internationalization API Specification (3rd Edition)")
- [Release 3rd Edition - Release Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402")

[Intl オブジェクト](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Intl "Intl オブジェクト")と呼ばれる国際化関連のAPIを定めている仕様です。

2nd Editionからのユーザーにとっての違いは[`Intl.getCanonicalLocales (locales)`](http://tc39.github.io/ecma402/#sec-intl.getcanonicallocales "Intl.getCanonicalLocales (locales)")のAPIが増えただけぐらいになっています。

- [tc39-notes/nov-19.md at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/blob/master/es7/2015-11/nov-19.md#abstract-locale-operations)
- [Exposing `CanonicalizeLocaleList()` abstract operation via `Intl.getCanonicalLocales()` by caridy · Pull Request #78 · tc39/ecma402](https://github.com/tc39/ecma402/pull/78)

ECMA-402もECMAScript(ECMA-262)と同じく[The TC39 Process](https://tc39.github.io/process-document/ "The TC39 Process")を採用しています。
そのため毎年リリース + StageでのProposal管理が[tc39/ecma402: Status, process, and documents for ECMA 402](https://github.com/tc39/ecma402 "tc39/ecma402: Status, process, and documents for ECMA 402")で行われています。

- [Introduction | ECMAScriptとは何か？](http://azu.github.io/slide-what-is-ecmascript/ "Introduction | ECMAScriptとは何か？")

----

[What's New in jQuery 3 - Telerik Developer Network](http://developer.telerik.com/featured/whats-new-in-jquery-3/ "What&#39;s New in jQuery 3 - Telerik Developer Network")という記事では、現在[Beta](https://blog.jquery.com/2016/01/14/jquery-3-0-beta-released/ "Beta")リリースされているjQuery 3について詳しく解説されています。

細かな変更点について書かれているので、jQueryに興味がある人は見てみるといいです。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v6.6.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.6.0](https://github.com/babel/babel/releases/tag/v6.6.0 "Release v6.6.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.6.0リリース。
transform-es3-member-expression-literalsが再度組み合わせて利用できるように、Babel 6で削除されたオプションに関するエラーをわかりやすく表示されるようになるなど

----

## Ember.js - Announcing Ember&#x27;s First LTS Release
[emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html](http://emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html "Ember.js - Announcing Ember's First LTS Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.jsがLTS(Long Term Support)リリースを行う予定。
Ember.js 2.4が最初のLTSリリースとなる

----

## Ember.js - Ember.js 2.4 and 2.5 Beta Released
[emberjs.com/blog/2016/02/29/ember-2-4-released.html](http://emberjs.com/blog/2016/02/29/ember-2-4-released.html "Ember.js - Ember.js 2.4 and 2.5 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 2.4と2.5 Betaリリース。
2.5では`Object.assign`のpolyfillである`Ember.assign`の追加、イベントのテストヘルパーの追加

----

## Release 3rd Edition - Release Candidate · tc39/ecma402 · GitHub
[github.com/tc39/ecma402/releases/tag/3.0-rc-1](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402 · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript Internationalization API 3rd Edition RCリリース。 i18n APIについて定義されてる仕様書

----
<h1 class="site-genre">アーティクル</h1>

----

## What&#x27;s New in jQuery 3 - Telerik Developer Network
[developer.telerik.com/featured/whats-new-in-jquery-3/](http://developer.telerik.com/featured/whats-new-in-jquery-3/ "What's New in jQuery 3 - Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span></p>

jQuery 3についての解説。
for/ofでの列挙、`$.get`/`$.post`のシグネチャ追加、requestAnimationFrameの対応、`data()`の動作変更、DeferredがPromise/A+互換に、SVGのサポートなど

----

## Step by Step Guide To Building React Redux Apps — Medium
[medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a "Step by Step Guide To Building React Redux Apps — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

React+Reduxをステップバイステップで学ぶチュートリアル

----

## Design by Contract with Flow, React, and ESLint · Jeff Winkler
[react.rocks/blog/post/propTypes\_React\_Flow/](https://react.rocks/blog/post/propTypes_React_Flow/ "Design by Contract with Flow, React, and ESLint · Jeff Winkler")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">flowtype</span></p>

ReactのコードをESLint + FlowTypeでチェックする仕組みについての記事

----

## Preload: What Is It Good For? – Smashing Magazine
[www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "Preload: What Is It Good For? – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span></p>

`<link rel="preload">`でのpreloadについての詳しい解説。
ブラウザがちゃんと優先度を扱える、CSPと同居できる、`as`属性を使い適切な形でリソースを読み込めるなどの特徴について書かれている。

----

## Building command line tools with Node.js - Atlassian Developers
[developer.atlassian.com/blog/2015/11/scripting-with-node/?categories=node.js](https://developer.atlassian.com/blog/2015/11/scripting-with-node/?categories=node.js "Building command line tools with Node.js - Atlassian Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">tutorial</span></p>

Node.jsでCLI作るチュートリアル

----

## Falcor入門 1日目 Falcorとは何者か - Qiita
[qiita.com/Quramy/items/5cf4f112d715c2e2d300](http://qiita.com/Quramy/items/5cf4f112d715c2e2d300 "Falcor入門 1日目 Falcorとは何者か - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">API</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Falcorとはどういうものなのかについての解説。
データの透過性と一貫性について

> Falcorを利用する大きなメリットの1つは「データがサーバにあるのか、クライアントにあるのか意識することなく扱えるようになること」

----

## TypeScriptの型定義管理ツールTypingsについて - Qiita
[qiita.com/literalice/items/d83249a5646abcb0bec6](http://qiita.com/literalice/items/d83249a5646abcb0bec6 "TypeScriptの型定義管理ツールTypingsについて - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

typingsの使い方について

----

## async/await: It’s Good and Bad — Medium
[medium.com/@benlesh/async-await-it-s-good-and-bad-15cf121ade40](https://medium.com/@benlesh/async-await-it-s-good-and-bad-15cf121ade40 "async/await: It’s Good and Bad — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

async/awaitのメリット/デメリットについて。

----

## gaearon/react-makes-you-sad: Here’s a flowchart to make you happy again!
[github.com/gaearon/react-makes-you-sad](https://github.com/gaearon/react-makes-you-sad "gaearon/react-makes-you-sad: Here’s a flowchart to make you happy again!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">画像</span></p>

Reactの学ぶ手順やエコシステムについてのアドバイス的な図

- [日本語訳](http://qiita.com/kuy/items/bfe5975205c9237ebd26)

----

## Examples of name clashes in JavaScript’s standard library
[www.2ality.com/2016/02/js-name-clashes.html](http://www.2ality.com/2016/02/js-name-clashes.html "Examples of name clashes in JavaScript’s standard library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

新たに追加するメソッド名が衝突したBreak the webの例とSymbolについて。
`Symbol.unscopables`が導入された経緯について

----

## Elmish: Functional Programming in Javascript — Medium
[medium.com/@chetcorcos/elmish-functional-programming-in-javascript-50995f1d4b9e](https://medium.com/@chetcorcos/elmish-functional-programming-in-javascript-50995f1d4b9e "Elmish: Functional Programming in Javascript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

Elm的なアーキテクチャをJavaScriptで実装しながら学んでみたという話

- [ccorcos/elmish: A Javascript UI library inspired by Elm](https://github.com/ccorcos/elmish "ccorcos/elmish: A Javascript UI library inspired by Elm")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ConFoo: Measuring SPA Performance // Speaker Deck
[speakerdeck.com/bluesmoon/confoo-measuring-spa-performance](https://speakerdeck.com/bluesmoon/confoo-measuring-spa-performance "ConFoo: Measuring SPA Performance // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

SPAでパフォーマンスをどう計測するについてのスライド。
XHRのhook、MutationObserver、FetchObserverについて

----

## React.js Conf 2016 - YouTube
[www.youtube.com/playlist?list=PLb0IAmt7-GS0M8Q95RIc2lOM6nc77q1IY](https://www.youtube.com/playlist?list=PLb0IAmt7-GS0M8Q95RIc2lOM6nc77q1IY "React.js Conf 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画 </span></p>

React.js Conf 2016の動画まとめ

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Doclets
[www.doclets.io/](https://www.doclets.io/ "Doclets")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">webservice</span></p>

JSDocとMarkdownのドキュメントホスティングサイト。
ymlにソースとMarkdownファイルを指定すれば、ドキュメントを作ってくれる

----

## HTML Standard 日本語訳
[momdo.github.io/html/](https://momdo.github.io/html/ "HTML Standard 日本語訳")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">HTML</span> <span class="jser-tag">翻訳</span></p>

WHATWG Living Standardの日本語訳

- [HTML Living Standard訳はじめました - 水底の血](http://momdo.hatenablog.jp/entry/20160301/1456833788 "HTML Living Standard訳はじめました - 水底の血")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## rtsao/csjs: Modular, scoped CSS with ES6
[github.com/rtsao/csjs](https://github.com/rtsao/csjs "rtsao/csjs: Modular, scoped CSS with ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

Template Stringsを使ったCSSのカプセル化を行うライブラリ

----

## mohayonao/web-audio-mock-api: mock API which implements the Web Audio API&#x27;s interfaces only
[github.com/mohayonao/web-audio-mock-api](https://github.com/mohayonao/web-audio-mock-api "mohayonao/web-audio-mock-api: mock API which implements the Web Audio API's interfaces only")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Web Audio APIのモックライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Introduction | React Webpack cookbook
[christianalfoni.github.io/react-webpack-cookbook/](https://christianalfoni.github.io/react-webpack-cookbook/ "Introduction | React Webpack cookbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span> <span class="jser-tag">webpack</span></p>

webpackとReactでのビルド環境構築系のGitBook

----

## Amazon.co.jp： ブラウザハック Webブラウザからの攻撃手法とその防御法総覧: Wade Alcorn, Christian Frichot, Michele Orru, 園田 道夫, はせがわ ようすけ, 西村 宗晃, 株式会社プロシステムエルオーシー: 本
[www.amazon.co.jp/%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%8F%E3%83%83%E3%82%AF-Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%8B%E3%82%89%E3%81%AE%E6%94%BB%E6%92%83%E6%89%8B%E6%B3%95%E3%81%A8%E3%81%9D%E3%81%AE%E9%98%B2%E5%BE%A1%E6%B3%95%E7%B7%8F%E8%A6%A7-Wade-Alcorn/dp/479814343X](http://www.amazon.co.jp/%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%8F%E3%83%83%E3%82%AF-Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%8B%E3%82%89%E3%81%AE%E6%94%BB%E6%92%83%E6%89%8B%E6%B3%95%E3%81%A8%E3%81%9D%E3%81%AE%E9%98%B2%E5%BE%A1%E6%B3%95%E7%B7%8F%E8%A6%A7-Wade-Alcorn/dp/479814343X "Amazon.co.jp： ブラウザハック Webブラウザからの攻撃手法とその防御法総覧: Wade Alcorn, Christian Frichot, Michele Orru, 園田 道夫, はせがわ ようすけ, 西村 宗晃, 株式会社プロシステムエルオーシー: 本")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">book</span></p>

2016年3月16日発売
攻撃者目線から学ぶブラウザ/ウェブのセキュリティについての書籍

----
