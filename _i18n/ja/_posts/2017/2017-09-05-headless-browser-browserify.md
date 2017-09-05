---
title: "2017-09-05のJS: Headless Browserの対応、Browserifyの再開"
author: "azu"
layout: post
date : 2017-09-05T01:20:45.284Z
category: JSer
tags:
- browser
- firefox
- Chrome
- headless
- browserify

---

JSer.info #347 - FirefoxのHeadlessモードについてのドキュメントが公開されています。

- [Headless mode - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Headless_mode "Headless mode - Mozilla | MDN")

FirefoxのHeadlessモードはLinuxではFirefox 55から、Mac/Windowsは56(現在のNightly)から動作します。

ChromeもMac/LinuxはChrome 59から、WindowsはChrome 60からHeadlessモードをが利用できるようになっています。

以前[2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules - JSer.info](https://jser.info/2017/05/03/headless-chromefirefoxphantomjsslimerjs-es-modules/ "2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules - JSer.info")でまとめた現在のHeadless対応状況をまとめると次のような感じです。

<script src="https://gist.github.com/azu/c4206d94f18f35f6fe2fe303f988e7d5.js"></script>

Firefoxは[selenium-webdriver](https://www.npmjs.com/package/selenium-webdriver "selenium-webdriver")を使った例が紹介されています。
Chromeは、Chromeチームが公開している[Puppeteer](https://github.com/GoogleChrome/puppeteer "Puppeteer")をはじめ、[Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD](https://medium.com/@kensoh/chromeless-chrominator-chromy-navalia-lambdium-ghostjs-autogcd-ef34bcd26907 "Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD")などさまざまなライブラリが公開されています。

[NickJS](https://nickjs.org/ "NickJS | The Modern Headless Browser Library")のようにPhantomJSからHeadless Chromeへ移行しているツールも出てきています。

- [Web Scraping in 2017: Advanced Headless Chrome Tips & Tricks](https://blog.phantombuster.com/web-scraping-in-2017-headless-chrome-tips-tricks-4d6521d695e8 "Web Scraping in 2017: Advanced Headless Chrome Tips &amp; Tricks")

----

Browserifyが`substack/node-browserify`から[browserify/browserify](https://github.com/browserify/browserify "browserify/browserify")のorganizationへ移行するとともに、次のようなIssueを立てて協力を求めています。

- [help wanted · Issue #5 · browserify/discuss](https://github.com/browserify/discuss/issues/5 "help wanted · Issue #5 · browserify/discuss")

[JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info](https://jser.info/2017/01/31/bundler-testing-framework-report/ "JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info")で伝えていたようにBrowserifyの開発は停滞していました。
今のBrowserifyはCommonJSをベースとしたBundlerであるため、今後[.mjs](https://blog.jxck.io/entries/2017-08-15/universal-mjs-ecosystem.html ".mjs")などがくることに備えた対応が必要であるなどを踏まえて現在のエコシステムを整理し始めています。

このIssueを始め、[browserify/admin: administrative procedures for the browserify org](https://github.com/browserify/admin "browserify/admin: administrative procedures for the browserify org")といったコミュニティ向けのドキュメント公開や今まで各自のリポジトリにあった`*fy`パッケージを <https://github.com/browserify> に集約しています。

Browserifyに意見がある人はこのIssueに書くとよさそうです。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">if you want to help out the browserify ecosystem, there&#39;s a new help wanted thread <a href="https://t.co/nB98TS5Cls">https://t.co/nB98TS5Cls</a></p>&mdash; substack (@substack) <a href="https://twitter.com/substack/status/902644080445874177">August 29, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 2.5 | TypeScript
[blogs.msdn.microsoft.com/typescript/2017/08/31/announcing-typescript-2-5/](https://blogs.msdn.microsoft.com/typescript/2017/08/31/announcing-typescript-2-5/ "Announcing TypeScript 2.5 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.5リリース。
Optinal-catch-bindingのサポート、エディタ連携の改善、重複/aliasなパッケージの扱いを改善、`--preserveSymlinks`のサポートなど

- [Typescript 2.5 リリース - abcdefGets](http://abcdef.gets.b6n.ch/entry/2017/09/01/143601 "Typescript 2.5 リリース - abcdefGets")

----

## Ember.js - Ember 2.15 and 2.16 Beta Released
[emberjs.com/blog/2017/09/01/ember-2-15-released.html](https://emberjs.com/blog/2017/09/01/ember-2-15-released.html "Ember.js - Ember 2.15 and 2.16 Beta Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 2.15リリース。
`Ember.Router`のスーパーセットである`router` serviceの公開など


----

## Concurrent JavaScript: It can work! | WebKit
[webkit.org/blog/7846/concurrent-javascript-it-can-work/](https://webkit.org/blog/7846/concurrent-javascript-it-can-work/ "Concurrent JavaScript: It can work! | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webkit</span></p>

`SharedArrayBuffer`が追加されるため、JavaScriptでThreadをサポートした場合にどうなるのかという思考実験についての記事。
現在のJavaScript VMはシングルスレッドであることを利用しているので、マルチスレッドの場合のVMのパフォーマンスなどについて。


----

## 🏁 Release: Iteration 10 – 10th developer preview · Issue #177 · ckeditor/ckeditor5-design
[github.com/ckeditor/ckeditor5-design/issues/177](https://github.com/ckeditor/ckeditor5-design/issues/177 "🏁 Release: Iteration 10 – 10th developer preview · Issue #177 · ckeditor/ckeditor5-design")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CKEditor 5 v0.10.0リリース。
MSEdgeのサポート、ツールチップメニューの改善、クリップボードの改善など

- [CKEditor 5 Developer Preview (v0.10.0)](https://ckeditor5.github.io/ "CKEditor 5 Developer Preview (v0.10.0)")
- [CKEditor 5 – Roadmap to 1.0.0 and beyond · Issue #172 · ckeditor/ckeditor5-design](https://github.com/ckeditor/ckeditor5-design/issues/172 "CKEditor 5 – Roadmap to 1.0.0 and beyond · Issue #172 · ckeditor/ckeditor5-design")

----
<h1 class="site-genre">アーティクル</h1>

----

## What's New In DevTools (Chrome 62)  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/08/devtools-release-notes](https://developers.google.com/web/updates/2017/08/devtools-release-notes "What's New In DevTools (Chrome 62)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 62の開発者ツールの更新点について。
Top-level `await`がコンソールで利用可能に、特定のnodeのスクリーンショットを取れるように、CSS Gridのハイライト、コンソールフィルタの改善。
またHARをインポートできるようになり、キャッシュデータの閲覧ができるように


----

## Form Validation with Web Audio | CSS-Tricks
[css-tricks.com/form-validation-web-audio/](https://css-tricks.com/form-validation-web-audio/ "Form Validation with Web Audio | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

Web Audio APIとフォームバリデーションを組み合わせる話。


----

## Measuring performance gains — AngularJS to React (with Redux or Mobx)
[medium.com/@guptagaruda/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455](https://medium.com/@guptagaruda/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455 "Measuring performance gains — AngularJS to React (with Redux or Mobx)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Angular</span></p>

3つのベンチマークアプリを元にAngular 1.xとReact/Redux/Mobxを比較した記事。
現在も多くのエンタープライズアプリがAngular 1.xで動いているため、Reactに移ることでどのようなメリットがあるのかを計測する目的


----

## Decaffeinating a Large CoffeeScript Codebase Without Losing Sleep · DataFox Tech Blog
[eng.datafox.com/javascript/2017/07/18/decaffeinating-large-coffeescript-codebase/](http://eng.datafox.com/javascript/2017/07/18/decaffeinating-large-coffeescript-codebase/ "Decaffeinating a Large CoffeeScript Codebase Without Losing Sleep · DataFox Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

bulk-decaffeinateを使ったCoffeeScriptからJavaScriptへの移行手順についての記事。


----

## React + RxJSで始める状態管理 - VOYAGE GROUP techlog
[techlog.voyagegroup.com/entry/2017/08/31/102915](http://techlog.voyagegroup.com/entry/2017/08/31/102915 "React + RxJSで始める状態管理 - VOYAGE GROUP techlog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">almin</span> <span class="jser-tag">設計</span></p>

Write層とRead層を分けることでのメリットとデメリットについて。 
複雑さに対する責務の分離と依存局所化について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Headless mode - Mozilla | MDN
[developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless\_mode](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode "Headless mode - Mozilla | MDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">document</span></p>

Firefoxのheadless modeについてのドキュメント


----

## Rendering on Google Search  |  Search  |  Google Developers
[developers.google.com/search/docs/guides/rendering](https://developers.google.com/search/docs/guides/rendering "Rendering on Google Search  |  Search  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">browser</span></p>

Google Search Botのレンダリングサブシステムで利用してるChromeのバージョンやサポートしてない(無効化されている)機能について書かれてる。
2017年9月4日現在はChrome 41をベースにしている

- [来日したGoogleゲイリーに何でも聞いてみた――プロジェクトOWL、検索アナリティクス、PWA etc. #inhouseseo | 海外SEO情報ブログ](https://www.suzukikenichi.com/blog/ama-with-gary/amp/ "来日したGoogleゲイリーに何でも聞いてみた――プロジェクトOWL、検索アナリティクス、PWA etc. #inhouseseo | 海外SEO情報ブログ")

----

## Kea vs setState, Redux, Mobx, Dva, JumpState, Apollo, etc.
[medium.com/@mariusandra/kea-vs-setstate-redux-mobx-dva-jumpstate-apollo-etc-4aa26ea11d02](https://medium.com/@mariusandra/kea-vs-setstate-redux-mobx-dva-jumpstate-apollo-etc-4aa26ea11d02 "Kea vs setState, Redux, Mobx, Dva, JumpState, Apollo, etc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">redux</span></p>

React向けのステート管理ライブラリのKeaについての記事。

- [Kea](https://kea.js.org/ "Kea")

----

## help wanted · Issue #5 · browserify/discuss
[github.com/browserify/discuss/issues/5](https://github.com/browserify/discuss/issues/5 "help wanted · Issue #5 · browserify/discuss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">issue</span></p>

browserifyのissueと今後(ES Moduleやhmrなど)について。
browserify organizationにそれぞれのパッケージが移されまとめて管理されるようになった


----

## phantombuster/nickjs: Web scraping library made by the Phantombuster team. Modern, simple & works on all websites.
[github.com/phantombuster/nickjs](https://github.com/phantombuster/nickjs "phantombuster/nickjs: Web scraping library made by the Phantombuster team. Modern, simple & works on all websites.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span></p>

Headless ChromeとPhantomJSをサポートしてるスクレイピングライブラリ

- [Phantombuster: API-fy the Web](https://phantombuster.com/ "Phantombuster: API-fy the Web")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## react-tools/react-move: React Move 🌀 Beautiful, data-driven animations for React
[github.com/react-tools/react-move](https://github.com/react-tools/react-move "react-tools/react-move: React Move 🌀 Beautiful, data-driven animations for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

Reactでデータドリブンなアニメーションを行うライブラリ


----

## lukechilds/keyv: Simple key-value store with support for multiple backends
[github.com/lukechilds/keyv](https://github.com/lukechilds/keyv "lukechilds/keyv: Simple key-value store with support for multiple backends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Redis、MySQLなどさまざまなバックエンドに対応してるシンプルなKVSライブラリ。
Map的なAPIを実装したadpterを使うことでバックエンドを変更できる


----
<h1 class="site-genre">書籍関係</h1>

----

## React for Real - O'Reilly Media
[shop.oreilly.com/product/9781680502633.do](http://shop.oreilly.com/product/9781680502633.do "React for Real - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

Reactについての書籍


----

## New Javascript Books
[newjavascriptbooks.com/](https://newjavascriptbooks.com/ "New Javascript Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptについての新書をまとめてるサイト


----
