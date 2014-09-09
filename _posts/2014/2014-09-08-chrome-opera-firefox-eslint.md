---
title: "2014-09-08のJS: Chrome 37/Opera 24、Firefox 32、ESLint 0.8.0"
author: azu
layout: post
date : 2014-09-08T21:38
category: JSer
tags:
    - Chrome
    - Opera
    - Firefox
    - AST
    - ECMAScript
---

JSer.info #191 - [Chrome 37](http://googlechromereleases.blogspot.jp/2014/08/stable-channel-update_26.html "Chrome 37")と[Opera 24](https://dev.opera.com/blog/opera-24/ "Opera 24")(Chromium 37がベース)がリリースされました。

共通の変更内容が多いですが[Dev.Opera — Opera 24 released](https://dev.opera.com/blog/opera-24/ "Dev.Opera — Opera 24 released")に分かりやすくまとめられています。
CSS ShapesやCSSの`all`プロパティが利用できるようになったこと、`showModalDialog()`が廃止され代わりに[`<dialog>`](http://updates.html5rocks.com/2013/09/dialog-element-Modals-made-easy "dialog element")要素が利用できるようになりました。

CSS Shapesに興味がある人は以下も参照するといいと思います。

- [CSS Shapes now available in Chrome 37 release | Web Platform Team Blog](http://blogs.adobe.com/webplatform/2014/08/28/css-shapes-now-in-chrome-37/ "CSS Shapes now available in Chrome 37 release | Web Platform Team Blog")
- [CSS Shapes Editor Extension – Brackets Blog](http://blog.brackets.io/2014/04/17/css-shapes-editor/ "CSS Shapes Editor Extension – Brackets Blog")


他の詳しい変更内容は以下を参照して下さい。

- [Chromium Blog: Chrome 37 Beta: DirectWrite on Windows and the &lt;dialog&gt; element](http://blog.chromium.org/2014/07/chrome-37-beta-directwrite-on-windows.html "Chromium Blog: Chrome 37 Beta: DirectWrite on Windows and the &lt;dialog&gt; element")
- [Dev.Opera — Opera 24 released](https://dev.opera.com/blog/opera-24/ "Dev.Opera — Opera 24 released")

----

[Firefox 32.0](https://www.mozilla.org/en-US/firefox/32.0/releasenotes/ "32.0")がリリースされました。

Web Audio Editorの追加、`<img>`の`srcset`属性がフラグ付きで実装されたことや、ES6の`Array.from()`等が実装されています。
また、フラグ付きで実装されていた`position: sticky;`がデフォルトで有効になりました。

- [Web Audio Editor - 開発ツール | MDN](https://developer.mozilla.org/ja/docs/Tools/Web_Audio_Editor "Web Audio Editor - 開発ツール | MDN")
- [Web Audio Editor の紹介 | Mozilla Developer Street (modest)](https://dev.mozilla.jp/2014/06/introducing-the-web-audio-editor-in-firefox-developer-tools/ "Web Audio Editor の紹介 | Mozilla Developer Street (modest)")
- [Firefox 32 が正式リリース、position: sticky; や srcset 属性への対応、開発ツールの機能追加など | WWW WATCH](http://hyper-text.org/archives/2014/09/firefox_32_release.shtml "Firefox 32 が正式リリース、position: sticky; や srcset 属性への対応、開発ツールの機能追加など | WWW WATCH")
- [Firefox 32 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/32 "Firefox 32 for developers - Mozilla | MDN")


----

PlugableなLintツールである[ESLint 0.8.0](http://eslint.org/blog/2014/09/eslint-0.8.0-released/ "ESLint 0.8.0")がリリースされました。

根幹とも言える[Plugins](http://eslint.org/docs/developer-guide/working-with-plugins.html "Plugins")の仕様が固まり、プラグインの作成方法や[eslint-tester](https://github.com/eslint/eslint-tester "eslint-tester")を使ったテスト、プラグインの公開方法等についてのドキュメントも書かれています。

- [Working with Plugins](http://eslint.org/docs/developer-guide/working-with-plugins.html "ESLint")

----

## お知らせ

それぞれの記事にTwitterへのTweetボタンを表示するようにしました。

パフォーマンス的な問題やデメリットが多そうならrevertするので、ご意見のある方は[Twitterボタンを各リンクに表示する · Issue #8 · jser/jser.github.io](https://github.com/jser/jser.github.io/issues/8 "Twitterボタンを各リンクに表示する · Issue #8 · jser/jser.github.io")や[@jser_info](https://twitter.com/jser_info "@jser_info")などへ適当に投げてください。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Dev.Opera — Opera 24 released
[dev.opera.com/blog/opera-24/](https://dev.opera.com/blog/opera-24/ "Dev.Opera — Opera 24 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 24リリース。

Windowsでのフォントレンダリングの改善、CSSの`all`プロパティのサポート、`navigator.hardwareConcurrency`でCPUコア数の取得、Web Cryptography APIのサポート等

----

## Firefox — Notes (32.0) — Mozilla
[www.mozilla.org/en-US/firefox/32.0/releasenotes/](http://www.mozilla.org/en-US/firefox/32.0/releasenotes/ "Firefox — Notes (32.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">セキュリティ</span></p>

Firefox 32リリース。

position:stickyがデフォルト有効に、imgのsrcset属性を試験サポート、`Array.from()`、Public Key Pinningの対応

- [Firefox 32 が正式リリース、position: sticky; や srcset 属性への対応、開発ツールの機能追加など | WWW WATCH](http://hyper-text.org/archives/2014/09/firefox_32_release.shtml "Firefox 32 が正式リリース、position: sticky; や srcset 属性への対応、開発ツールの機能追加など | WWW WATCH")
- [Firefox 32 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/32 "Firefox 32 for developers - Mozilla | MDN")

----

## Release SCSS-Lint 0.28.0 · causes/scss-lint
[github.com/causes/scss-lint/releases/tag/v0.28.0](https://github.com/causes/scss-lint/releases/tag/v0.28.0 "Release SCSS-Lint 0.28.0 · causes/scss-lint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">ReleaseNote</span></p>

SCSS-Lint 0.28.0リリース。

Sass 3.4に対応

----

## Brackets 0.43 Release – Brackets Blog
[blog.brackets.io/2014/09/04/brackets-0-43-release/](http://blog.brackets.io/2014/09/04/brackets-0-43-release/ "Brackets 0.43 Release – Brackets Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">editor</span> <span class="jser-tag">ReleaseNote</span></p>

Brackets 0.43リリース。

Sass/Lessのサポート、検索UIの改善、シンタックスの言語切替ができるように

----

## mathjs/HISTORY.md at v1.0.0 · josdejong/mathjs
[github.com/josdejong/mathjs/blob/v1.0.0/HISTORY.md](https://github.com/josdejong/mathjs/blob/v1.0.0/HISTORY.md "mathjs/HISTORY.md at v1.0.0 · josdejong/mathjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

既存のMathと互換性のある関数や数値演算、数式のパーサを持つライブラリであるmath.js 1.0.0リリース

----

## ESLint 0.8.0 released - ESLint
[eslint.org/blog/2014/09/eslint-0.8.0-released/](http://eslint.org/blog/2014/09/eslint-0.8.0-released/ "ESLint 0.8.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.8.0リリース。

プラグインの仕組みがstableになって、作り方、テスト方法、命名ルール等が公開された。

ignorefileの`node_modules/`と書いた時の挙動を変更、パフォーマンスの改善等

- [Working with Plugins](http://eslint.org/docs/developer-guide/working-with-plugins.html "Working with Plugins")

----

## Release v0.9.0: Release 0.9.0 (2014-09-02) multi-stage sourcemaps · twada/power-assert
[github.com/twada/power-assert/releases/tag/v0.9.0](https://github.com/twada/power-assert/releases/tag/v0.9.0 "Release v0.9.0: Release 0.9.0 (2014-09-02) multi-stage sourcemaps · twada/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 0.9.0リリース。

AltJS等を使っている時に、元ファイルの正しいエラー行数を表示するために多段SourceMapに対応

- [多段SourceMapの対応方法とライブラリ | Web Scratch](http://efcl.info/2014/09/03/multi-stage-sourcemap/ "多段SourceMapの対応方法とライブラリ | Web Scratch")

----

## Socket.IO — Socket.IO 1.1.0
[socket.io/blog/socket-io-1-1-0/](http://socket.io/blog/socket-io-1-1-0/ "Socket.IO — Socket.IO 1.1.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Socket.IO 1.1.0リリース。

namespaceの指定が`/`から始まるかどうかはどちらでも良くなった。バグ修正等

----
<h1 class="site-genre">アーティクル</h1>

----

## A Fond Farewell to YUI | Blog | Sencha
[www.sencha.com/blog/a-fond-farewell-to-yui/](http://www.sencha.com/blog/a-fond-farewell-to-yui/ "A Fond Farewell to YUI | Blog | Sencha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">歴史</span> <span class="jser-tag">library</span></p>

Ext JS 1.0より前はYUIに依存してて、その後は3.0までアダプタ的なものを提供していた。

またエンタープライズウェブアプリの今後についてや、AngularJS等とExt JSがカバーしてる範囲の違いと用途への適正等の話

- [YUI との別れを惜しむ | 株式会社ゼノフィ](https://www.xenophy.com/sencha-blog/11463 "YUI との別れを惜しむ | 株式会社ゼノフィ")
- [Enterprise Web Development: From Desktop to Mobile](http://enterprisewebbook.com/ "Enterprise Web Development: From Desktop to Mobile")

----

## 多段SourceMapの対応方法とライブラリ | Web Scratch
[efcl.info/2014/09/03/multi-stage-sourcemap/](http://efcl.info/2014/09/03/multi-stage-sourcemap/ "多段SourceMapの対応方法とライブラリ | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

多段SourceMapといわれてるものについての問題と、それをマッピングし直すことでその問題を解決するモジュールについて

----

## Making the web “just work” with any input: Mouse, Touch, and Pointer Events - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/09/05/making-the-web-just-work-with-any-input.aspx](http://blogs.msdn.com/b/ie/archive/2014/09/05/making-the-web-just-work-with-any-input.aspx "Making the web “just work” with any input: Mouse, Touch, and Pointer Events - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">browser</span> <span class="jser-tag">mobile</span></p>

IE 11のアップデートでTouch Eventsのサポートが入り、Mouse/Touch/Pointerの3つのモデルが存在するようになった。

それらのモデルの比較とfeature detectによる互換性のない実装がよくみられる事について等

- [The Mobile Web should just work for everyone - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/07/31/the-mobile-web-should-just-work-for-everyone.aspx "The Mobile Web should just work for everyone - IEBlog - Site Home - MSDN Blogs")
- [IE11: 現在そして将来の Web に対応するタッチ ブラウジング - IEBlog 日本語 - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie_ja/archive/2013/08/06/ie11-touch-browsing-for-todays-web-and-beyond.aspx "IE11: 現在そして将来の Web に対応するタッチ ブラウジング - IEBlog 日本語 - Site Home - MSDN Blogs")
- [Issue 162757 - chromium - Implement pointer events in Chrome behind experimental flag - An open-source project to help move the web forward. - Google Project Hosting](https://code.google.com/p/chromium/issues/detail?id=162757#c64 "Issue 162757 - chromium - Implement pointer events in Chrome behind experimental flag - An open-source project to help move the web forward. - Google Project Hosting")

----

## From AngularJS to React: the isomorphic way
[blog.risingstack.com/from-angularjs-to-react-the-isomorphic-way/](http://blog.risingstack.com/from-angularjs-to-react-the-isomorphic-way/ "From AngularJS to React: the isomorphic way")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AngularJS</span></p>

SEO的な視点からAngularJSからReactにした話。

Angularではkoa-prerenderでプリレンダリングをしていた。

Reactを使うことでクライアントもサーバも同じコード(Isomorphic JavaScript)を使ってViewができるようになった

----

## ECMAScript 6 modules: the final syntax
[www.2ality.com/2014/09/es6-modules-final.html](http://www.2ality.com/2014/09/es6-modules-final.html "ECMAScript 6 modules: the final syntax")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 modulesの構文について。

構文の仕様は固まり、CommonJSのような同期的な形とAMDのような非同期的な呼び出しどちらでも使える。

ES6 modulesの構文、基本的な使い方、default exportやSystem.importについて等まとまってる

----

## An Introduction to WebDriver Using the JavaScript Bindings - Tuts+ Code Tutorial
[code.tutsplus.com/tutorials/an-introduction-to-webdriver-using-the-javascript-bindings--cms-21855](http://code.tutsplus.com/tutorials/an-introduction-to-webdriver-using-the-javascript-bindings--cms-21855 "An Introduction to WebDriver Using the JavaScript Bindings - Tuts+ Code Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Selenium</span> <span class="jser-tag">webdriver</span> <span class="jser-tag">node.js</span></p>

WebDriverJSのバインディングについて。

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Supersonic JavaScript // Speaker Deck
[speakerdeck.com/ariya/supersonic-javascript](https://speakerdeck.com/ariya/supersonic-javascript "Supersonic JavaScript // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

JavaScriptエンジンの最適化についてのスライド。

コンストラクタ関数の最適化(Shape、Hidden class)を妨げない書き方、短絡評価、段階的なアプローチ、GCについてなど

- [JavaScript Memory Management Masterclass // Speaker Deck](https://speakerdeck.com/addyosmani/javascript-memory-management-masterclass "JavaScript Memory Management Masterclass // Speaker Deck")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## コーディングガイド by @mdo
[kia-king.com/code-guide/](http://kia-king.com/code-guide/ "コーディングガイド by @mdo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">翻訳</span></p>

<a href='http://codeguide.co/'>http://codeguide.co/</a> の訳

HTMLやCSSやJavaScriptそれぞれを書く時のルールの統一感を持つためのガイドライン

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## macbre/phantomas
[github.com/macbre/phantomas](https://github.com/macbre/phantomas "macbre/phantomas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

PhantomJSを使ったパフォーマンスメトリクス、モニタリングツール

----

## TimBeyer/html-to-vdom
[github.com/TimBeyer/html-to-vdom](https://github.com/TimBeyer/html-to-vdom "TimBeyer/html-to-vdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

HTML文字列をVirtual DOM(vTree)に変換するライブラリ。

----

## btwael/locallydb
[github.com/btwael/locallydb](https://github.com/btwael/locallydb "btwael/locallydb")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

node、node-webkitで使えるNoSQLなデータベースライブラリ。

JSONファイルベース

----

## zendesk/cross-storage
[github.com/zendesk/cross-storage](https://github.com/zendesk/cross-storage "zendesk/cross-storage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

postMessageを使ったクロスドメインでデータを共有出来るlocalStorageラッパライブラリ。

ES6 Promisesを使ったPromiseベースのAPIになってる

- [DailyJS: Cross-Storage: Share Local Data Across Domains](http://dailyjs.com/2014/09/05/cross-storage/ "DailyJS: Cross-Storage: Share Local Data Across Domains")

----

## RReverser/acorn-csp
[github.com/RReverser/acorn-csp](https://github.com/RReverser/acorn-csp "RReverser/acorn-csp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AST</span></p>

acornのCSP対応版を生成するツール。

`new Function`を使っている所に対して、AST変換を使ったインライン展開的な事をして対応していて興味深い

- [Acorn-cspのできた流れ - efcl’s blog](http://efcl.hatenablog.com/entry/2014/09/07/022914 "Acorn-cspのできた流れ - efcl’s blog")

----

## pioneer.js - javascript integration testing
[pioneerjs.com/](http://pioneerjs.com/ "pioneer.js - javascript integration testing")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Selenium</span> <span class="jser-tag">webdriver</span> <span class="jser-tag">library</span></p>

Cucumber的なDSLと、そのDSLに対応した処理をJavaScriptで書けるStep、どこをテストするのかのDOMをラップしたWidgetsの3層構造のテストフレームワーク。

WebDriverを使ってブラウザ自動テストが出来る

- [Pioneerのお試しステップ - efcl’s blog](http://efcl.hatenablog.com/entry/2014/09/08/212101 "Pioneerのお試しステップ - efcl’s blog")

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: AngularJSリファレンス
[www.amazon.co.jp/dp/4844336681?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4844336681?tag=amazon0abac-22 "Amazon: AngularJSリファレンス")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

2014年9月5日発売

AngularJSの脱初心者〜中級者向けの書籍

<a href='http://zoetrope.hatenablog.jp/entry/2014/09/01/201056'>http://zoetrope.hatenablog.jp/entry/2014/09/01/201056</a>

----

## O&#x27;Reilly Japan - 実践 Selenium WebDriver
[www.oreilly.co.jp/books/9784873116952/](http://www.oreilly.co.jp/books/9784873116952/ "O&#x27;Reilly Japan - 実践 Selenium WebDriver")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Selenium</span> <span class="jser-tag">book</span> <span class="jser-tag">ios</span> <span class="jser-tag">Android</span></p>

2014年9月18日発売

Seleniumについての書籍。

ブラウザやiOS/Androidのテストについて扱う

----
