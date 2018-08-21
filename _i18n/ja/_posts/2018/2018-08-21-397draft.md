---
title: "2018-08-21のJS: webpack 4のマイナーな変更、スクロールの歴史、Puppeteer Recorder"
author: "azu"
layout: post
date : 2018-08-21T01:39:48.415Z
category: JSer
tags:
- webpack
- history
- Puppeteer

---

JSer.info #397 - [webpack 4.0 to 4.16: Did you know? – webpack – Medium](https://medium.com/webpack/webpack-4-0-to-4-16-did-you-know-71e25a57fa6b)という記事では、webpackのマイナー(4.0 ~ 4.16)の変更に関してまとめて解説されています。

[webpack 4](https://medium.com/webpack/webpack-4-released-today-6cdb994702d4)では`CommonsChunkPlugin`が削除され、代わりに`optimization.splitChunks`というオプションが追加されています。

- [webpack 4: Code Splitting, chunk graph and the splitChunks optimization](https://medium.com/webpack/webpack-4-code-splitting-chunk-graph-and-the-splitchunks-optimization-be739a861366)

その後のマイナーアップデートでも`automaticNameDelimiter`、`maxSize`オプションの追加などが行われています。
また、[Code Splitting](https://webpack.js.org/guides/code-splitting/)する際には[Dynamic Imports](https://webpack.js.org/guides/code-splitting/#dynamic-imports)に対して`import(/* webpackChunkName: "lodash" */ 'lodash')`のような特殊なコメントでモジュールごとの挙動を指定できるようになっています。
この挙動の指定に関しても、マイナーの変更としてpreloadなどを指定できる`webpackPrefetch`や、そのまま`import()`として出力するための`webpackIgnore`コメントなどが追加されています。

- [`<link rel=”prefetch/preload”>` in webpack – webpack – Medium](https://medium.com/webpack/link-rel-prefetch-preload-in-webpack-51a52358f84c)

その他にもwebpack 4のマイナーの変更が紹介されているので、興味がある人は見てみると良さそうです。

----

[Puppeteer Recorder - Chrome ウェブストア](https://chrome.google.com/webstore/detail/puppeteer-recorder/djeegiggegleadkkbgopoonhjimgehda/reviews)というChrome拡張が公開されています。
この拡張は[Selenium IDE](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)のように、Chromeでの操作を記録し、それを再現するコードを[Puppeteer](https://github.com/GoogleChrome/puppeteer)向けのスクリプトとして出力します。

- [checkly/puppeteer-recorder: Puppeteer recorder is a Chrome extension that records your browser interactions and generates a Puppeteer script.](https://github.com/checkly/puppeteer-recorder)

また、[Creating a Chrome extension in 2018: The good, the bad and the meh | Checkly](https://checklyhq.com/blog/2018/08/creating-a-chrome-extension-in-2018-the-good-the-bad-and-the-meh/)という記事では、このChrome拡張に関する解説が行われています。

[Puppeteer](https://github.com/GoogleChrome/puppeteer)はHeadless Chromeを扱うHigh LevelなAPIをまとめたライブラリですが、[foxr](https://github.com/deepsweet/foxr)というFirefox(headless)をPuppeteerライクなAPIで操作するライブラリも公開されています。

- [deepsweet/foxr: 🦊 Node.js API to control Firefox](https://github.com/deepsweet/foxr)

[foxr](https://github.com/deepsweet/foxr)はまだ開発段階ですが、Puppeteer APIのサブセットとして互換性のあるAPIを提供することを目的としています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release: npm@6.4.0 - 📣 announcements - npm forum
[npm.community/t/release-npm-6-4-0/1417](https://npm.community/t/release-npm-6-4-0/1417 "Release: npm@6.4.0 - 📣 announcements - npm forum")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.4.0リリース。
IPv6が使える場合はIPv6を使うように、`npm audit`に`--audit-level`を追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Variable Scope in Modern JavaScript with var, let and const | Andy Carter
[andy-carter.com/blog/variable-scope-in-modern-javascript](https://andy-carter.com/blog/variable-scope-in-modern-javascript "Variable Scope in Modern JavaScript with var, let and const | Andy Carter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`var`、`let`、`const`の変数のスコープについて解説している記事。

- [関数とスコープ · JavaScriptの入門書 #jsprimer](https://asciidwango.github.io/js-primer/basic/function-scope/ "関数とスコープ · JavaScriptの入門書 #jsprimer")

----

## Better tree shaking with deep scope analysis – webpack – Medium
[medium.com/webpack/better-tree-shaking-with-deep-scope-analysis-a0b788c0ce77](https://medium.com/webpack/better-tree-shaking-with-deep-scope-analysis-a0b788c0ce77 "Better tree shaking with deep scope analysis – webpack – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

webpackのTree Shakingではモジュール間同士の依存に関するDead Code Eliminationに動かないケースがあった。
そのパターンを解決するプラグインとその動作の解説について

- [vincentdchan/webpack-deep-scope-analysis-plugin: A webpack plugin for deep scope analysis](https://github.com/vincentdchan/webpack-deep-scope-analysis-plugin "vincentdchan/webpack-deep-scope-analysis-plugin: A webpack plugin for deep scope analysis")
- [Unexpected code after tree-shake · Issue #6264 · webpack/webpack](https://github.com/webpack/webpack/issues/6264 "Unexpected code after tree-shake · Issue #6264 · webpack/webpack")

----

## webpack 4.0 to 4.16: Did you know? – webpack – Medium
[medium.com/webpack/webpack-4-0-to-4-16-did-you-know-71e25a57fa6b](https://medium.com/webpack/webpack-4-0-to-4-16-did-you-know-71e25a57fa6b "webpack 4.0 to 4.16: Did you know? – webpack – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack 4以降の変更点について。
`optimization`に`automaticNameDelimiter`、`maxSize`オプションの追加。
Dynamic Importでpreloadなどを指定できる`webpackPrefetch`や、そのまま`import()`として出力するための`webpackIgnore`コメントのサポートなど。


----

## Scroll to the future — Martian Chronicles, Evil Martians’ team blog
[evilmartians.com/chronicles/scroll-to-the-future-modern-javascript-css-scrolling-implementations](https://evilmartians.com/chronicles/scroll-to-the-future-modern-javascript-css-scrolling-implementations "Scroll to the future — Martian Chronicles, Evil Martians’ team blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">UI</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span></p>

ブラウザとスクロールについての歴史や変更についてをまとめた記事。
スクロールバーのOSやブラウザでの表示の違い、`Element#scrollIntoView`やCSS `scroll-behavior`でのスクロールの挙動。
またstickyやIntersection Observer、`overscroll-behavior`プロパティなどについて


----

## Cross-tab Synchronization with the Web Locks API - Blog | SitePen
[www.sitepen.com/blog/2018/08/14/cross-tab-synchronization-with-the-web-locks-api/](https://www.sitepen.com/blog/2018/08/14/cross-tab-synchronization-with-the-web-locks-api/ "Cross-tab Synchronization with the Web Locks API - Blog | SitePen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Web Locks APIを使ったタブ間同士のコミュニケーションについて。
Web Locks APIのユースケースや使い方について

- [WICG/web-locks: Cross-tab resource coordination API](https://github.com/WICG/web-locks/ "WICG/web-locks: Cross-tab resource coordination API")

----

## JavaScript engine fundamentals: optimizing prototypes · Mathias Bynens
[mathiasbynens.be/notes/prototypes](https://mathiasbynens.be/notes/prototypes "JavaScript engine fundamentals: optimizing prototypes · Mathias Bynens")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span></p>

JavaScriptエンジン(V8)の`prototype`の最適化の仕組みについての解説


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Tangled World of Web Technology ― Are we safe? - Speaker Deck
[speakerdeck.com/lmt\_swallow/tangled-world-of-web-technology-are-we-safe](https://speakerdeck.com/lmt_swallow/tangled-world-of-web-technology-are-we-safe "Tangled World of Web Technology ― Are we safe? - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">XSS</span> <span class="jser-tag">slide</span> <span class="jser-tag">security</span></p>

ブラウザでの新しい技術と今まである技術が絡んだ脆弱性についてのスライド。
ReactやVueといったデフォルトエスケープされるライブラリにおいてもXSSは起こるケースがあること。
また、Service WorkerやCSPなど新しい技術と今まである技術が絡み合うことで発生する問題などの紹介。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Puppeteer Recorder - Chrome ウェブストア
[chrome.google.com/webstore/detail/puppeteer-recorder/djeegiggegleadkkbgopoonhjimgehda](https://chrome.google.com/webstore/detail/puppeteer-recorder/djeegiggegleadkkbgopoonhjimgehda "Puppeteer Recorder - Chrome ウェブストア")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span> <span class="jser-tag">testing</span></p>

Chromeの操作を記録してPuppeteerで再生できるスクリプトを出力できるブラウザ拡張。


----

## deepsweet/foxr: 🦊 Node.js API to control Firefox
[github.com/deepsweet/foxr](https://github.com/deepsweet/foxr "deepsweet/foxr: 🦊 Node.js API to control Firefox")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">API</span> <span class="jser-tag">node.js</span></p>

Firefoxをremote protocol経由で操作するNode.jsライブラリ。
Headlessモードにも対応し、APIはPuppeteerのサブセット互換のものを提供することを目的としている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Angular Console
[angularconsole.com/](https://angularconsole.com/ "Angular Console")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">console</span> <span class="jser-tag">GUI</span> <span class="jser-tag">software</span></p>

Angular CLIのUIを提供することを目的にしたアプリ。
Angular CLIでできる操作をGUIから行えるようにすることが目的。

- [Angular Console — The UI for the Angular CLI – nrwl](https://blog.nrwl.io/angular-console-the-ui-for-the-angular-cli-a5d0924240b7 "Angular Console — The UI for the Angular CLI – nrwl")

----

## flowchart.js
[flowchart.js.org/](http://flowchart.js.org/ "flowchart.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span> <span class="jser-tag">グラフ</span></p>

テキストからSVGのフローチャートを作成するJavaScriptライブラリ。


----

## Tonejs/Tone.js: A Web Audio framework for making interactive music in the browser.
[github.com/Tonejs/Tone.js](https://github.com/Tonejs/Tone.js "Tonejs/Tone.js: A Web Audio framework for making interactive music in the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">API</span> <span class="jser-tag">library</span></p>

Web Audio APIを使ったインタラクティブミュージックを作成するためのフレームワーク。
Max/MSPインスパイアなシグナルプロセッシング向けの処理やモジュールを提供するのが目的


----

## arguiot/TheoremJS: A Math library for computation in JavaScript
[github.com/arguiot/TheoremJS](https://github.com/arguiot/TheoremJS "arguiot/TheoremJS: A Math library for computation in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

MathやNumber、代数、統計などに関する関数を集めたmathematicalフレームワーク


----

## spencermountain/spacetime: A lightweight javascript timezone library
[github.com/spencermountain/spacetime](https://github.com/spencermountain/spacetime "spencermountain/spacetime: A lightweight javascript timezone library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

他のライブラリに依存していないタイムゾーンライブラリ。また、i18n APIには直接依存していない。歴史的なタイムゾーンの扱いを省略することでファイルサイズを小さくしている。

- [Home · spencermountain/spacetime Wiki](https://github.com/spencermountain/spacetime/wiki "Home · spencermountain/spacetime Wiki")

----
<h1 class="site-genre">書籍関係</h1>

----

## Vue.js入門 基礎から実践アプリケーション開発まで | 川口 和也, 手島 拓也, 野田 陽平, 喜多 啓介, 片山 真也 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4297100916/](https://www.amazon.co.jp/dp/4297100916/ "Vue.js入門 基礎から実践アプリケーション開発まで | 川口 和也, 手島 拓也, 野田 陽平, 喜多 啓介, 片山 真也 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">book</span></p>

2018年9月22日発売
Vue.jsについての書籍


----

## JavaScript Data Structures and Algorithms: An Introduction to Understanding and Implementing Core Data Structure and Algorithm Fundamentals: Sammie Bae: 9781484239872: Amazon.com: Books
[www.amazon.com/dp/1484239873/](https://www.amazon.com/dp/1484239873/ "JavaScript Data Structures and Algorithms: An Introduction to Understanding and Implementing Core Data Structure and Algorithm Fundamentals: Sammie Bae: 9781484239872: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2019年3月11日発売
JavaScriptでのデータ構造やアルゴリズムについての書籍


----

## JavaScript逆引きレシピ 第2版 達人が選んだ珠玉の現場ワザ（山田祥寛）｜翔泳社の本
[www.shoeisha.co.jp/book/detail/9784798157573](https://www.shoeisha.co.jp/book/detail/9784798157573 "JavaScript逆引きレシピ 第2版 達人が選んだ珠玉の現場ワザ（山田祥寛）｜翔泳社の本")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2018年10月15日発売
JavaScriptの逆引きリファレンス本


----
