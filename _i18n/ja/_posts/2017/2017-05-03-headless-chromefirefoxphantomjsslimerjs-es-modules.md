---
title: "2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules"
author: "azu"
layout: post
date : 2017-05-03T02:03:59.837Z
category: JSer
tags:
- Firefox
- Chrome
- Headless
- PhantomJS
- SlimerJS
- modules
- ECMAScript

---

JSer.info #329 - Chrome 59βがリリースされました。

- [Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload](https://blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html "Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload")

Service Workerの[navigation preloads](https://developers.google.com/web/updates/2017/02/navigation-preload)のサポート、`MediaError.message`のサポート、Image Capture APIの試験的サポートなどが行われています。

また、[Headless Chromium](https://chromium.googlesource.com/chromium/src/+/master/headless/ "Headless Chromium")が追加されています。

詳しくは次の記事で解説されていますが、PhantomJSのようにXvfbなどが不要なChromeを動かすことができるモードです。

- [Getting Started with Headless Chrome  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/04/headless-chrome "Getting Started with Headless Chrome  |  Web  |  Google Developers")

また、このHeadless Chromeのリリースをうけて、PhantomJSのコアメンテナー(唯一のアクティブメンテナー)が開発の終了を宣言しています。

- [[Announcement] Stepping down as maintainer - Google グループ](https://groups.google.com/forum/#!topic/phantomjs/9aI5d-LDuNE "[Announcement] Stepping down as maintainer - Google グループ")
- [[Release] PhantomJS 2.5.0 Beta - Google グループ](https://groups.google.com/forum/#!topic/phantomjs/AefOuwkgBh0 "[Release] PhantomJS 2.5.0 Beta - Google グループ")
  - 少し前に公開されたα版(QtWebKitのアップデートが含まれている)

PhantomJSはQtWebKitを利用しており、QtWebKitは一度削除され最近また復活しています。
QtWebKitのAlternativeとしてChromiumベースの[QtWebEngine](https://wiki.qt.io/QtWebEngine "QtWebEngine")が提供されています。

- [New Features in Qt 5.6 - Qt Wiki](https://wiki.qt.io/New_Features_in_Qt_5.6 "New Features in Qt 5.6 - Qt Wiki")
- [QtWebKit Developer Journal: QtWebKit: I'm back!](http://qtwebkit.blogspot.jp/2016/08/qtwebkit-im-back.html "QtWebKit Developer Journal: QtWebKit: I&#39;m back!")

どちらを利用した場合もPhantomJSには大量の修正が必要となり、サポートコストが高いためPhantomJSのメンテナンスを終了するとのことです。

別方向の話としては、PhantomJSをHeadless Chromeベースで動かすことについてのIssueが立てられています。

- [Support headless Chromium · Issue #14954 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/14954 "Support headless Chromium · Issue #14954 · ariya/phantomjs")

PhantomJSとHeadless Chromeの違いについては次の記事でも書かれています。
レンダリングエンジン以外の違いとして、[PhantomJSの持つAPI](http://phantomjs.org/api/ "API | PhantomJS")とHeadless Chromeの操作に使う[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/ "Chrome DevTools Protocol")の違いがあります。

> Headless Chrome is similar to tools like PhantomJS. Both can be used for automated testing in a headless environment. The main difference between the two is that Phantom uses an older version of WebKit as its rendering engine while Headless Chrome uses the latest version of Blink.
> -- <https://developers.google.com/web/updates/2017/04/headless-chrome>

----

[Headless SlimerJS with Firefox – Coding](https://adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/ "Headless SlimerJS with Firefox – Coding")の記事では、Firefox NightlyでHeadlessサポートに向けて開発されている点について書かれています。

また、FirefoxベースのPhantomJSといえる[SlimerJS](http://slimerjs.org/ "SlimerJS")が、このHeadless Firefoxをサポートする方向について書かれています。
([SlimerJS](http://slimerjs.org/ "SlimerJS")は[PhantomJSの持つAPI](http://phantomjs.org/api/ "API | PhantomJS")とよく似ているAPIを持つ)

- [Turn SlimerJS into an headless browser · Issue #80 · laurentj/slimerjs](https://github.com/laurentj/slimerjs/issues/80#issuecomment-280813674 "Turn SlimerJS into an headless browser · Issue #80 · laurentj/slimerjs")

**まとめ**: Headless Browser

<script src="https://gist.github.com/azu/c4206d94f18f35f6fe2fe303f988e7d5.js"></script>

----

[ECMAScript modules in browsers - JakeArchibald.com](https://jakearchibald.com/2017/es-modules-in-browsers/ "ECMAScript modules in browsers - JakeArchibald.com")という記事では、ブラウザのES modulesのサポート状況と挙動について書かれています。

Node.jsで扱うモジュールとは異なる点や、`<script type="module">`のデフォルトの挙動などについて書かれています。
次の記事も併せてみると良さそうです。

- [Native ECMAScript modules: the new features and differences from Webpack modules](https://blog.hospodarets.com/native-ecmascript-modules-new-features "Native ECMAScript modules: the new features and differences from Webpack modules")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Headless SlimerJS with Firefox – Coding
[adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/](https://adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/ "Headless SlimerJS with Firefox – Coding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">E2E</span> <span class="jser-tag">webdriver</span></p>

Firefox Nightlyでheadlessサポートが行われたため、SlimerJSでヘッドレスなテストをおこなえるようになったという話


----

## TestCafe v0.15.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-15-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-15-0-released.html "TestCafe v0.15.0 Released | TestCafe")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

TestCafe 0.15.0リリース。
`Selector()#withText`の仕様を変更、ReactとVue向けのSelector拡張のサポート、セットアップ済みのDocker imageの提供。
`--proxy`と`--debug-mode`の追加、`Role`に`preserveUrl`オプションの追加など


----

## Angular: Angular 4.1.0 Now Available
[angularjs.blogspot.com/2017/04/angular-410-now-available.html](http://angularjs.blogspot.com/2017/04/angular-410-now-available.html "Angular: Angular 4.1.0 Now Available")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 4.1.0リリース。
StrictNullChecksを有効化したTypeScript 2.2/2.3のサポート。


----

## Release v2.3.0 JoJo's Bizarre Adventure · vuejs/vue
[github.com/vuejs/vue/releases/tag/v2.3.0](https://github.com/vuejs/vue/releases/tag/v2.3.0 "Release v2.3.0 JoJo's Bizarre Adventure · vuejs/vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.3.0リリース。
サーバサイドレンダリングの改善、コンポーネントの非同期ローディングの改善、passive event listenerのサポートなど


----

## Release v0.45.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.45.0](https://github.com/facebook/flow/releases/tag/v0.45.0 "Release v0.45.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.45.0リリース。
Unicodeサポートの改善、Dynamic Importのサポート、`export type * from ...`に対応など


----

## Announcing TypeScript 2.3 | TypeScript
[blogs.msdn.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/](https://blogs.msdn.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/ "Announcing TypeScript 2.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.3リリース。
`--checkJs`で`// @ts-check`と書かれたJavaScriptのJSDocをtype checkできるように。
Default type argumentsのサポート、`--downlevelIteration`の追加、`tsc  --init`で生成される`tsconfig.json`の整理など

- [JSDoc support in JavaScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript "JSDoc support in JavaScript · Microsoft/TypeScript Wiki")

----

## Ember.js - Ember 2.13 and 2.14 Beta Released
[emberjs.com/blog/2017/04/29/ember-2-13-released.html](https://emberjs.com/blog/2017/04/29/ember-2-13-released.html "Ember.js - Ember 2.13 and 2.14 Beta Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 2.14リリース。
Ember CLIでyarnのサポート、BabelやAutoprefixerで利用できる`targets`を指定する`config/target.js`が生成されるようになるなど

- [Ember CLI Targets 🎯](http://rwjblue.com/2017/04/21/ember-cli-targets/ "Ember CLI Targets 🎯")

----

## Netflix/unleash: Professionally publish your JavaScript modules in one keystroke
[github.com/Netflix/unleash](https://github.com/Netflix/unleash "Netflix/unleash: Professionally publish your JavaScript modules in one keystroke")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

npm publishバージョン管理ツール。
semverでのバージョン付け、テストの実行、CHANGELOGの生成、publish時のpreview、gh-pagesへのドキュメントのデプロイなどpublish周りの処理をまとめたツール


----

## Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload
[blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html](https://blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html "Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 59 Betaリリース。
Headless Chrome、SWのnavigation preloadsのサポート、`MediaError.message`のサポート、Image Capture APIの試験的サポートなど

- [mediacapture-image/implementation-status.md at gh-pages · w3c/mediacapture-image](https://github.com/w3c/mediacapture-image/blob/gh-pages/implementation-status.md "mediacapture-image/implementation-status.md at gh-pages · w3c/mediacapture-image")

----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing a faster BBC News front page | Wildly Inaccurate
[wildlyinaccurate.com/introducing-a-faster-bbc-news-front-page](https://wildlyinaccurate.com/introducing-a-faster-bbc-news-front-page "Introducing a faster BBC News front page | Wildly Inaccurate")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

BBC Newsのパフォーマンス改善について。 SpeedCurveを使って計測を行い、画像遅延ロード、Reactをサーバサイドレンダリングのみに利用してる。 まだ改善の1段階で、Reactをブラウザ側で動かしたときにモバイルだと重たい問題


----

## Internationalize your keyboard controls ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/03/internationalize-your-keyboard-controls/](https://hacks.mozilla.org/2017/03/internationalize-your-keyboard-controls/ "Internationalize your keyboard controls ★ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">キーボード</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

キーボードイベントについて。
`keyCode`/`charCode`/`which`を置き換える`key`と`code`プロパティについて。
また、その他のKeyboardEvent周りのTipsについて。

- [KeyboardEvent.key mapping of each browser - Google スプレッドシート](https://docs.google.com/spreadsheets/d/1YB4M5Y5BWSn-7FX7pXFNbLtDDGzQ0noUTIo-YSqyRzc/edit#gid&#x3D;0 "KeyboardEvent.key mapping of each browser - Google スプレッドシート")
- [cvan/keyboardevent-key-polyfill: polyfill for \`KeyboardEvent.prototype.key\`](https://github.com/cvan/keyboardevent-key-polyfill "cvan/keyboardevent-key-polyfill: polyfill for \&#x60;KeyboardEvent.prototype.key\&#x60;")
- [UI Events](https://w3c.github.io/uievents/#code-examples "UI Events")

----

## Everything you need to know about BabelJS
[kleopetrov.me/2016/03/18/everything-about-babel/](http://kleopetrov.me/2016/03/18/everything-about-babel/ "Everything you need to know about BabelJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babelの設定やCLIについての概要解説


----

## Functional pattern: flatMap
[2ality.com/2017/04/flatmap.html](http://2ality.com/2017/04/flatmap.html "Functional pattern: flatMap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

`flatMap`と呼ばれるものはどのようなものを言っているのかについて。
またそれに関連するECMAScriptのStage 1のProposalについて

- [bterlson/proposal-flatMap: Proposal for flatten and flatMap](https://github.com/bterlson/proposal-flatMap "bterlson/proposal-flatMap: Proposal for flatten and flatMap")

----

## Getting Started with Headless Chrome  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/04/headless-chrome](https://developers.google.com/web/updates/2017/04/headless-chrome "Getting Started with Headless Chrome  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Headless Chromeの使い方について。
コマンドラインからDOMのダンプ、PDFの作成、スクリーンショット、remote debuggingの方法などについて


----

## ECMAScript modules in browsers - JakeArchibald.com
[jakearchibald.com/2017/es-modules-in-browsers/](https://jakearchibald.com/2017/es-modules-in-browsers/ "ECMAScript modules in browsers - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span></p>

ES modulesのブラウザサポートとNode.jsのモジュールと異なる点などについて。
また、モジュールが未サポート環境へのfallbackとしての`nonmodule`、デフォルトが`defer`である点や実行順、CORSやMIME typeなどについて


----

## Node.js 8.0.0 has been delayed and will ship on or around May 30th
[medium.com/the-node-js-collection/node-js-8-0-0-has-been-delayed-and-will-ship-on-or-around-may-30th-cd38ba96980d](https://medium.com/the-node-js-collection/node-js-8-0-0-has-been-delayed-and-will-ship-on-or-around-may-30th-cd38ba96980d "Node.js 8.0.0 has been delayed and will ship on or around May 30th")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodev</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

Node.js 8.0.0のリリース日が5月30日になった件について。
V8のTurboFan + Ignition pipelineのデフォルト化リリースを待ってからにする点について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## bevacqua/prop-tc39: Scraping microservice for TC39 proposals 😸
[github.com/bevacqua/prop-tc39](https://github.com/bevacqua/prop-tc39 "bevacqua/prop-tc39: Scraping microservice for TC39 proposals 😸")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">API</span></p>

ECMAScriptのProposalsの一覧とそれをJSONとして取得できるAPIとパッケージ


----

## Performance best practices for Firefox front-end engineers - Mozilla | MDN
[developer.mozilla.org/en-US/docs/Mozilla/Firefox/Performance\_best\_practices\_for\_Firefox\_fe\_engineers](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Performance_best_practices_for_Firefox_fe_engineers "Performance best practices for Firefox front-end engineers - Mozilla | MDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span></p>

Firefoxのフロントエンド向けに書かれたパフォーマンスガイド。
requestIdleCallback、reflow、repaint、パフォーマンス計測などについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Introduction · react-sketchapp
[airbnb.io/react-sketchapp/](http://airbnb.io/react-sketchapp/ "Introduction · react-sketchapp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Sketch</span> <span class="jser-tag">library</span></p>

React ComponentをSketchへレンダリングするrenderer


----

## Create Next App
[open.segment.com/create-next-app](https://open.segment.com/create-next-app "Create Next App")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">React</span></p>

Next.js版create react app


----

## ktsn/houl: Gulp compatible build tool for huge static sites
[github.com/ktsn/houl](https://github.com/ktsn/houl "ktsn/houl: Gulp compatible build tool for huge static sites")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">gulp</span> <span class="jser-tag">debug</span></p>

gulp pluginを利用できるビルド/dev serverツール

- [大規模静的サイトのためのビルドツール // Speaker Deck](https://speakerdeck.com/ktsn/da-gui-mo-jing-de-saitofalsetamefalsebirudoturu "大規模静的サイトのためのビルドツール // Speaker Deck")

----
<h1 class="site-genre">書籍関係</h1>

----

## わか(った気にな)るWebRTC 紙＋電子版セット - Route 312 - BOOTH（同人誌通販・ダウンロード）
[booth.pm/ja/items/504677](https://booth.pm/ja/items/504677 "わか(った気にな)るWebRTC 紙＋電子版セット - Route 312 - BOOTH（同人誌通販・ダウンロード）")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">book</span></p>

WebRTCの入門書


----

## Webフロントエンド ハイパフォーマンス チューニング | 久保田 光則 |本 | 通販 | Amazon
[www.amazon.co.jp/Web%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9-%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E4%B9%85%E4%BF%9D%E7%94%B0-%E5%85%89%E5%89%87/dp/4774189677](https://www.amazon.co.jp/Web%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9-%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E4%B9%85%E4%BF%9D%E7%94%B0-%E5%85%89%E5%89%87/dp/4774189677 "Webフロントエンド ハイパフォーマンス チューニング | 久保田 光則 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

2017年5月26日発売
ウェブサイトのフロントエンドのパフォーマンスについての書籍


----
