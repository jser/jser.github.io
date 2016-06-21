---
title: "2016-06-21のJS: ECMAScript 2016リリース、QUnit 2.0"
author: azu
layout: post
date : 2016-06-21T09:26
category: JSer
tags:
    - ECMAScript
    - Spec
    - i18n
    - QUnit

---

JSer.info #284 - ECMAScript 2016が正式にリリースされました :tada:

- [ECMAScript® 2016 Language Specification](http://www.ecma-international.org/ecma-262/7.0/ "ECMAScript® 2016 Language Specification")

どのような変更があったのかは以前簡単にまとめています。

- [ECMAScript 2016 features & changes - JSer.info](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features &amp; changes - JSer.info")
- [ECMAScript 2015 - 2016 diff points](https://gist.github.com/azu/3dc9295e97aee9a2706068caf65f0348 "ECMAScript 2015 - 2016 diff points")

機能的に追加されたのは、`Array.prototype.includes`と[`**`演算子](https://github.com/rwaldron/exponentiation-operator)ぐらいなので大きな変化ありません。
(Proxyの`[[enumerate]]` trapと`Reflect.enumerate`が削除されたりもしています)

一番大きな変化として仕様策定プロセスの変更で、毎年スナップショット的にリリースする形になっています。
ちょっと古いですが次の記事で解説しています。

- [ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch")

HTMLの仕様と同じく仕様を読むという意味で参照する場合は、[スナップショット](http://www.ecma-international.org/publications/standards/Ecma-262.htm)よりもGitHubにあるLiving Standardな仕様を参照した方が良いと思います。

- [ECMAScript® 2017 Language Specification](https://tc39.github.io/ecma262/ "ECMAScript® 2017 Language Specification")

また、ECMAScript 2016と同じく[ECMAScript® 2016 Internationalization API Specification](http://www.ecma-international.org/ecma-402/3.0/ "ECMAScript® 2016 Internationalization API Specification")もリリースされています。
`Intl`オブジェクトなどを決めている[ECMAScriptの国際化API](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Intl "ECMAScriptの国際化API")の仕様です。
こちらも毎年リリースの策定プロセスへ変更されています。

- [Release 3rd Edition - Release Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402")

ECMAScriptの最新情報については[ECMAScript Daily](https://ecmascript-daily.github.io/ "ECMAScript Daily")の方に書いているので、興味がある人は見てみるといいかもしれません。

- [ecmascript-daily.github.io](https://ecmascript-daily.github.io/ "ECMAScript Daily")

----

JavaScriptのテストフレームワークQunit 2.0がリリースされています。

- [Release 2.0.0 · jquery/qunit](https://github.com/jquery/qunit/releases/tag/2.0.0 "Release 2.0.0 · jquery/qunit")

基本的に非推奨となっていたグローバル関数を削除、メソッドのリネームなど破壊的な変更が中心です

- `module()`、`test()`はそれぞれ`QUnit.*`以下に移動
- `start()`、`stop()`の代わりに`assert.async()`を利用
- `setup`/`teardown`は`beforeEach`/`afterEach`にリネーム
- `QUnit.init`と`QUnit.reset`の削除

アップグレードガイドも公開されているので合わせて参照してください

- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")


----
<h1 class="site-genre">ヘッドライン</h1>

----

## ECMAScript® 2016 Language Specification
[www.ecma-international.org/ecma-262/7.0/](http://www.ecma-international.org/ecma-262/7.0/ "ECMAScript® 2016 Language Specification")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

ECMAScript 2016リリース。
毎年リリース体制になってから初リリース

- [Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")
- [tc39/ecma262: Status, process, and documents for ECMA262](https://github.com/tc39/ecma262 "tc39/ecma262: Status, process, and documents for ECMA262")
- [ECMAScript 2016 features &amp;amp; changes - JSer.info](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features &amp;amp; changes - JSer.info")

----

## ECMAScript® 2016 Internationalization API Specification
[www.ecma-international.org/ecma-402/3.0/](http://www.ecma-international.org/ecma-402/3.0/ "ECMAScript® 2016 Internationalization API Specification")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">spec</span></p>

ECMAScript 2016 Internationalization API仕様リリース。
Unicode 8.0を必要とするようになり、`Intl.getCanonicalLocales()`の追加。

----

## Release v1.9.0 · testem/testem
[github.com/testem/testem/releases/tag/v1.9.0](https://github.com/testem/testem/releases/tag/v1.9.0 "Release v1.9.0 · testem/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

testem 1.9.0リリース。
カスタムレポーターがmetaデータを受け取る事ができるようになった

----

## Release 2.0.0 · jquery/qunit
[github.com/jquery/qunit/releases/tag/2.0.0](https://github.com/jquery/qunit/releases/tag/2.0.0 "Release 2.0.0 · jquery/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.0.0リリース。
非推奨のグローバル関数を削除、メソッドのリネームなど破壊的な変更が含まれれる

- `module()`、`test()`はそれぞれ`QUnit.*`以下に移動
- `start()`、`stop()`の代わりに`assert.async()`
- `setup`/`teardown`は`beforeEach`/`afterEach`に
- `QUnit.init`と`QUnit.reset`の削除

アップグレードガイドは以下を参照

- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")

----

## ESLint v2.13.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/06/eslint-v2.13.0-released](http://eslint.org/blog/2016/06/eslint-v2.13.0-released "ESLint v2.13.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.13.0リリース。
2.x系では最後になり、次は3.0.0が予定されている

- [Proposal for 3.0.0 · Issue #6356 · eslint/eslint](https://github.com/eslint/eslint/issues/6356 "Proposal for 3.0.0 · Issue #6356 · eslint/eslint")

----

## RC2 Now Available
[angularjs.blogspot.com/2016/06/rc2-now-available.html](http://angularjs.blogspot.com/2016/06/rc2-now-available.html "RC2 Now Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular2 RC2リリース

- [Angular 2 RC.2がリリースされました | Angular2 Info](http://ng2-info.github.io/2016/06/16/angular-2-rc-2/ "Angular 2 RC.2がリリースされました | Angular2 Info")

----

## Safari 10.0
[developer.apple.com/library/prerelease/content/releasenotes/General/WhatsNewInSafari/Articles/Safari\_10\_0.html](https://developer.apple.com/library/prerelease/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_10_0.html "Safari 10.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 10のリリースノート。
IndexedDB、CSP、Shadow DOM v1、ES6、ECMA i18n APIなど

----
<h1 class="site-genre">アーティクル</h1>

----

## ReactでTDD（テスト駆動開発）を始めよう : 環境構築からテスト作成、機能実装までの詳解ガイド | プログラミング | POSTD
[postd.cc/getting-started-with-tdd-in-react/](http://postd.cc/getting-started-with-tdd-in-react/ "ReactでTDD（テスト駆動開発）を始めよう : 環境構築からテスト作成、機能実装までの詳解ガイド | プログラミング | POSTD")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">翻訳</span></p>

React ComponentをTDDする話

----

## A Quick Introduction To Polymer — WebComponents.org
[webcomponents.org/articles/a-quick-polymer-introduction/](http://webcomponents.org/articles/a-quick-polymer-introduction/ "A Quick Introduction To Polymer — WebComponents.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span></p>

Polymer入門向けの概要を説明した文章

----

## 実例とともに学ぶECMAScript 2015 〜Generator〜 – NET BIZ DIV. TECH BLOG
[tech.recruit-mp.co.jp/front-end/post-10358/](https://tech.recruit-mp.co.jp/front-end/post-10358/ "実例とともに学ぶECMAScript 2015 〜Generator〜 – NET BIZ DIV. TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

Generator、Iteratorについて。
Iterableを扱うfor of、`Array.from`、spread operatorについて。
「GeneratorはIteratorを返す関数」に至るまでを丁寧に解説してる記事

----

## The SoundCloud Client in React + Redux - RWieruch
[www.robinwieruch.de/the-soundcloud-client-in-react-redux/](http://www.robinwieruch.de/the-soundcloud-client-in-react-redux/ "The SoundCloud Client in React + Redux - RWieruch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

React+ReduxでSoundcloudのクライアントを作るチュートリアル

----

## The Future of Declaration Files | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/](https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/ "The Future of Declaration Files | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">TypeScript</span></p>

npmからTypeScriptの型定義ファイルをインストールして使えるようになるという話。

`npm install --save @types/lodash` のような形で他にツールを必要としない

- [TypeScript Types Search](http://microsoft.github.io/TypeSearch/ "TypeScript Types Search")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Tips &amp; Tricks in Front-End Development // Speaker Deck
[speakerdeck.com/forloop/tips-and-tricks-in-front-end-development](https://speakerdeck.com/forloop/tips-and-tricks-in-front-end-development "Tips & Tricks in Front-End Development // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span> <span class="jser-tag">Tips</span></p>

`object-fit`、Viewport unit、既読リンクの扱い、壊れた`<img />`の表示、要素内が空の場合の表示、postMessage、SVGなどのフロントエンド向けのTips

----

## CSS Animations, Orchestrated by David Khourshid
[slides.com/davidkhourshid/deck-17#/](http://slides.com/davidkhourshid/deck-17#/ "CSS Animations, Orchestrated by David Khourshid")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span></p>

CSSアニメーションのまとめかたについてのスライド

----

## Resource (pre)loading
[yoavweiss.github.io/link\_htmlspecial\_16/](http://yoavweiss.github.io/link_htmlspecial_16/ "Resource (pre)loading")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">スライド</span></p>

`<link rel>`についてのスライド
prefetch、resource loading、feature detectionについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## mgiuca/web-share: Web API proposal for sharing data from a web page
[github.com/mgiuca/web-share](https://github.com/mgiuca/web-share "mgiuca/web-share: Web API proposal for sharing data from a web page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">spec</span></p>

`navigator.share`のAPIについてのドキュメント。
Androidのintents、iOSのUIActivityViewControllerのような共有するためのAPI。
Chromeで実装検討中

- [Web Share - Chrome Platform Status](https://www.chromestatus.com/feature/5668769141620736 "Web Share - Chrome Platform Status")
- [Web Share API for sharing content to arbitrary destination - APIs - WICG](https://discourse.wicg.io/t/web-share-api-for-sharing-content-to-arbitrary-destination/1561/4 "Web Share API for sharing content to arbitrary destination - APIs - WICG")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## fed135/Kalm: Node socket wrapper and optimizer
[github.com/fed135/Kalm](https://github.com/fed135/Kalm "fed135/Kalm: Node socket wrapper and optimizer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">WebRTC</span> <span class="jser-tag">library</span></p>

WebSocketやWebRTCなど双方向の通信を行うライブラリ。
Nagleアルゴリズムの実装など効率よくパケットを送れるような仕組みを持っている。
Adapterで利用するプロトコルを変更できるようになっている

----

## af/envalid: Environment variable validation for Node.js
[github.com/af/envalid](https://github.com/af/envalid "af/envalid: Environment variable validation for Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Node.jsの`process.env`の値をバリデーションするライブラリ

----

## headless - chromium/src - Git at Google
[chromium.googlesource.com/chromium/src/+/master/headless/](https://chromium.googlesource.com/chromium/src/+/master/headless/ "headless - chromium/src - Git at Google")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chromiumヘッドレスブラウザのリポジトリ

----

## alexreardon/raf-stub: Accurate and predictable testing of requestAnimationFrame and cancelAnimationFrame
[github.com/alexreardon/raf-stub](https://github.com/alexreardon/raf-stub "alexreardon/raf-stub: Accurate and predictable testing of requestAnimationFrame and cancelAnimationFrame")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

`requestAnimationFrame`のstubライブラリ。
ステップごとにframeを進めることができる

----
<h1 class="site-genre">書籍関係</h1>

----

## Manning | Angular 2 in Action
[www.manning.com/books/angular-2-in-action](https://www.manning.com/books/angular-2-in-action "Manning | Angular 2 in Action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

Angular 2についての書籍

- [Angular 2 in Action](https://github.com/angular-in-action/ "Angular 2 in Action")

----
