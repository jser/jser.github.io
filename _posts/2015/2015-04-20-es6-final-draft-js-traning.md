---
title: "2015-04-20のJS: ECMAScript6最終ドラフト、JavaScriptトレーニング"
author: azu
layout: post
date : 2015-04-20T22:12
category: JSer
tags:
    - ECMAScript
    - JavaScript
    - tutorial

---

JSer.info #224 - 次期ECMAScriptのいわゆるES6の[Rev 38 Final Draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_14_2015_rev_38_final_draft "Rev 38 Final Draft")がリリースされました。

最終ドラフトなので、これがECMAへ提出されて2015年の6月のECMAのミーティングにて承認されれば、ECMA標準として公開される予定になっています。

[2014-06-09のJS](http://jser.info/post/88276341744/2014-06-09-js-bluebird/ "2014-06-09のJS")の際にES6のリリース次期が変更されていましたが、この変更した通りに進んでいるようです。
(図は2014-06-09時点のもの)

<p><a href="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" title="ES6 timeline" target="_blank"><img width="100%" src="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" alt="ES6 Release Schedule"/></a></p>

<p><a href="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" title="ES6 timeline" target="_blank">＊画像が横に長いのでクリック</a></p>

ECMA標準として承認された後、ECMAScriptは[ISO/IEC 16262](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=55755 "ISO/IEC 16262")としても標準化されているためこちらにも提出される予定です。

ISO/IECではECMAScript5を[ISO/IEC 16262:2011](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=55755 "ISO/IEC 16262:2011")として標準化されているように年号が使われています。
このような対応関係が分かりにくくなる問題あり、ES6の仕様書ではECMAScript 2015という表記へ変更されています。

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/rwaldron">@rwaldron</a> <a href="https://twitter.com/SlexAxton">@SlexAxton</a> RC4 replaced a lot of &quot;Edition 6&quot; with &quot;ECMAScript 2015&quot;. Will help with ISO version aka ISO/IEC-16262 Edition 4</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/584093254045413376">April 3, 2015</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

- [Web Reflection: JavaScript and the living ECMAScript Standard](http://webreflection.blogspot.jp/2015/01/javascript-and-living-ecmascript.html "Web Reflection: JavaScript and the living ECMAScript Standard")

----

[mixi-inc/JavaScriptTraining](https://github.com/mixi-inc/JavaScriptTraining "mixi-inc/JavaScriptTraining")というリポジトリではJavaScriptの入門トレーニング用の資料が公開されています。

- [2日でできる！JavaScript トレーニング - mixi Engineers&#39; Blog](http://alpha.mixi.co.jp/entry/2015/04/17/155003 "2日でできる！JavaScript トレーニング - mixi Engineers&#39; Blog")

![screenshot](http://monosnap.com/image/7wFTczUbicOXK4BuMYYz03sa5s1sbl.png)

[JS Assessment](http://efcl.info/2012/0414/res3059/ "JS Assessment")やいわゆる[Koan](http://el.jibun.atmarkit.co.jp/rails/2011/01/koan-3c38.html "Koan")のような形式となっていて、テストが通るように問題を解いていく方式になっています。

DOM操作、DOMイベント、非同期処理、PromiseとFetch API、bowerを使ったパッケージ管理などについてを扱っていて、生のDOM APIについて学ぶ機会も少なくなってきてるのでこういうトレーニングをやってみるのも面白いかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## April 14, 2015 Rev 38 Final Draft - Draft Specification for ES.next (Ecma-262 Edition 6)
[wiki.ecmascript.org/doku.php?id=harmony:specification\_drafts#april\_14\_2015\_rev\_38\_final\_draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_14_2015_rev_38_final_draft)

ECMAScript 2015(ES6)の最終ドラフトがリリース。

<blockquote class="twitter-tweet" lang="en"><p>Final Draft of the ECMAScript 2015 Language Specification (ES6) is now available at <a href="http://t.co/pcHkz1muWu">http://t.co/pcHkz1muWu</a> Next step: Ecma GA approval vote</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/588811606236106755">April 16, 2015</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## React v0.13.2 | React
[facebook.github.io/react/blog/2015/04/18/react-v0.13.2.html](http://facebook.github.io/react/blog/2015/04/18/react-v0.13.2.html "React v0.13.2 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.13.2リリース。
react toolsに`--es6module`のオプションを追加など

- [Document new es6module flag in react-tools README by TimeBomb · Pull Request #3618 · facebook/react](https://github.com/facebook/react/pull/3618 "Document new es6module flag in react-tools README by TimeBomb · Pull Request #3618 · facebook/react")

----

## Release electron v0.24.0 · atom/electron
[github.com/atom/electron/releases/tag/v0.24.0](https://github.com/atom/electron/releases/tag/v0.24.0 "Release electron v0.24.0 · atom/electron")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">atom</span> <span class="jser-tag">ReleaseNote</span></p>

Atom Shell 0.24.0リリース。
Atom ShellはElectronにリネームされた

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md#500](https://github.com/tmpvar/jsdom/blob/master/Changelog.md#500 "jsdom/Changelog.md at master · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 5.0.0リリース。
`document.cookie`周りの修正が中心

----

## Release v0.8.0 · airportyh/testem
[github.com/airportyh/testem/releases/tag/v0.8.0](https://github.com/airportyh/testem/releases/tag/v0.8.0 "Release v0.8.0 · airportyh/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Testem 0.8.0リリース。
SauceLabsのようにリモートとつないで実行する場合の挙動を改善

----

## Release v0.11.0: ES6 support (2015-04-18) · twada/power-assert
[github.com/twada/power-assert/releases/tag/v0.11.0](https://github.com/twada/power-assert/releases/tag/v0.11.0 "Release v0.11.0: ES6 support (2015-04-18) · twada/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 0.11.0リリース。
ES6の構文をサポート

- [ES6 support by twada · Pull Request #17 · twada/power-assert](https://github.com/twada/power-assert/pull/17 "ES6 support by twada · Pull Request #17 · twada/power-assert")
- [twada/babel-plugin-espower](https://github.com/twada/babel-plugin-espower "twada/babel-plugin-espower")

----

## Chromium Blog: Chrome 43 Beta: Web MIDI and upgrading legacy sites to HTTPS
[blog.chromium.org/2015/04/chrome-43-beta-web-midi-and-upgrading.html](http://blog.chromium.org/2015/04/chrome-43-beta-web-midi-and-upgrading.html "Chromium Blog: Chrome 43 Beta: Web MIDI and upgrading legacy sites to HTTPS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 43 Betaリリース。
Web MIDI APIがデフォルトで有効に、
Permissions APIのサポート、DOM属性がprototype chainに移動、Flashなしでもクリップボードへのコピーが出来るように、Fetchでレスポンスをストリーミング出来るようになるなど

- [Permissions API for the Web](http://updates.html5rocks.com/2015/04/permissions-api-for-the-web "Permissions API for the Web")
- [DOM Attributes now on the prototype chain](http://updates.html5rocks.com/2015/04/DOM-attributes-now-on-the-prototype "DOM Attributes now on the prototype chain")
- [Cut and Copy Commands](http://updates.html5rocks.com/2015/04/cut-and-copy-commands "Cut and Copy Commands")
- [yutakahirano/fetch-with-streams](https://github.com/yutakahirano/fetch-with-streams/ "yutakahirano/fetch-with-streams")

----
<h1 class="site-genre">アーティクル</h1>

----

## Getting started with Node.js and Mocha - Semaphore
[semaphoreci.com/community/tutorials/getting-started-with-node-js-and-mocha](https://semaphoreci.com/community/tutorials/getting-started-with-node-js-and-mocha "Getting started with Node.js and Mocha - Semaphore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Mochaを使ったテストについて。
Mochaの基本的な使い方やexpressを使って実装したウェブサーバのテストについて簡潔にまとめられている

----

## Fullscreen API と 闇 - Browser
[browser.hatenablog.com/entry/2015/04/18/121248](http://browser.hatenablog.com/entry/2015/04/18/121248 "Fullscreen API と 闇 - Browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

ブラウザ間のFullscreen APIの挙動の違いについて

----

## Permissions API for the Web
[updates.html5rocks.com/2015/04/permissions-api-for-the-web](http://updates.html5rocks.com/2015/04/permissions-api-for-the-web "Permissions API for the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

パーミッションを確認するAPI。
`navigator.permissions`について

----

## JavaScriptでフルスクラッチゲーム開発しよう 第1回 準備編 - Qiita
[qiita.com/zukkun/items/4ea9542a6dde45c6a9fd](http://qiita.com/zukkun/items/4ea9542a6dde45c6a9fd "JavaScriptでフルスクラッチゲーム開発しよう 第1回 準備編 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">game</span> <span class="jser-tag">JavaScript</span></p>

一からJavaScriptでゲーム(ゲームエンジン)を作る連載。
フレームごとの更新、Canvasを使った描画、画像の読み込みなどゲームフレームワークは使わずに書いていく話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Controllable React Components // Speaker Deck
[speakerdeck.com/lettertwo/controllable-react-components](https://speakerdeck.com/lettertwo/controllable-react-components "Controllable React Components // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

ReactでES6 classesを使ったComponentを作るスライド。
Component内では常にstateじゃなくpropsを使いたい、FormのControlled Componentでもpropsを使うための高階関数について

- [Forms | React](http://facebook.github.io/react/docs/forms.html#controlled-components "Forms | React")
- [matthewwithanm/react-controllables](https://github.com/matthewwithanm/react-controllables "matthewwithanm/react-controllables")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ES Weekly Newsletter
[esweekly.com/](http://esweekly.com/ "ES Weekly Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">mail</span></p>

ECMAScriptについての週刊のメールマガジン

----

## mixi-inc/JavaScriptTraining
[github.com/mixi-inc/JavaScriptTraining](https://github.com/mixi-inc/JavaScriptTraining "mixi-inc/JavaScriptTraining")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

mixi社のJavaScript研修資料。
テストを通すことで進んでいけるような内容になっている。
DOM操作、DOMイベント、非同期処理、PromiseとFetch API、bowerを使ったパッケージ管理などについて

- [2日でできる！JavaScript トレーニング - mixi Engineers&#39; Blog](http://alpha.mixi.co.jp/entry/2015/04/17/155003 "2日でできる！JavaScript トレーニング - mixi Engineers&#39; Blog")

----

## ARIA in HTML 日本語訳
[momdo.github.io/html-aria/](http://momdo.github.io/html-aria/ "ARIA in HTML 日本語訳")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">spec</span></p>

HTMLとWAI-ARIAの属性についての要件をまとめた仕様。
ある要素のデフォルトのARIAセマンティクスと使用してもよいARIAロールについて簡潔にまとめられている

- [ARIA in HTML 日本語訳を公開した - 水底の血](http://momdo.hatenablog.jp/entry/20150418/1429345964 "ARIA in HTML 日本語訳を公開した - 水底の血")

----

## Hacklone/private-bower
[github.com/Hacklone/private-bower](https://github.com/Hacklone/private-bower "Hacklone/private-bower")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">オープンソース</span></p>

Private bower registry

----

## HAR Resources | A community curated list of resources, tools, projects and applications that support HTTP Archive (HAR)
[ahmadnassri.github.io/har-resources](https://ahmadnassri.github.io/har-resources "HAR Resources | A community curated list of resources, tools, projects and applications that support HTTP Archive (HAR)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">まとめ</span></p>

HTTP Archive (HAR)を扱うツールやリソースのまとめ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## acornejo/jjv
[github.com/acornejo/jjv](https://github.com/acornejo/jjv "acornejo/jjv")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

JSON Schemaの定義とバリデーションを行うライブラリ

----

## caiogondim/logdown
[github.com/caiogondim/logdown](https://github.com/caiogondim/logdown "caiogondim/logdown")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

ロガー + Markdownなライブラリ。
ブラウザ、Node.jsどちらでも動作する

----

## T3 JavaScript Framework - T3 JavaScript Framework
[t3js.org/](http://t3js.org/ "T3 JavaScript Framework - T3 JavaScript Framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Box社のJavaScriptフレームワーク。
Angular 1.x系みたいなモジュールの仕組みだが、基本はコンパクトでコールスタックもかなり浅くなるように作られている。`debug`オプションを有効にすることでエラーが取りやすいように設計されている

----

## vdemedes/interaptor
[github.com/vdemedes/interaptor](https://github.com/vdemedes/interaptor "vdemedes/interaptor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

mitmを使ったHTTP stubライブラリ。
特定のリクエストに対して任意のレスポンスを定義して返せる

----