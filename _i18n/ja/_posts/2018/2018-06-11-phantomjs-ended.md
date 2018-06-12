---
title: "PhantomJSの開発が終了しリポジトリがアーカイブ化された"
author: azu
layout: post
date : 2018-06-11T22:31
category: 雑記
tags:
    - PhantomJS
    - JavaScript

---

QtWebKitをベースにしたヘッドレスブラウザである[PhantomJS][]の開発が終了され、2018年6月2日にリポジトリもアーカイブされました。

[![ariya/phantomjs](https://jser.info/uploads/media/2018/06/11-1528724137.png)](https://github.com/ariya/phantomjs)

以前にもお伝えしていましたが、PhantomJSはQtWebKitをベースにしていて安定版が利用しているバージョンも古いままでした。
また、[QtWebKitの新しいバージョンへアップデートを行うベータ版](https://groups.google.com/forum/#!topic/phantomjs/AefOuwkgBh0)も開発されていましたが、[Headless Chromium](https://chromium.googlesource.com/chromium/src/+/master/headless/README.md)が公開されたことや[個人でPhantomJSのメンテナンスを続けていくの難しい](https://groups.google.com/forum/#!topic/phantomjs/9aI5d-LDuNE)という問題もあり開発は停止していました。

- [2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules - JSer.info](https://jser.info/2017/05/03/headless-chromefirefoxphantomjsslimerjs-es-modules/ "2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules - JSer.info")
- [2017-09-05のJS: Headless Browserの対応、Browserifyの再開 - JSer.info](https://jser.info/2017/09/05/headless-browser-browserify/ "2017-09-05のJS: Headless Browserの対応、Browserifyの再開 - JSer.info")

そのまま非アクティブな状態が続いたためリポジトリもアーカイブする提案がされ、2018年6月2日にリポジトリがアーカイブされました。

- [Archiving the project: suspending the development · Issue #15344 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/15344)

---

[PhantomJS][]は2011年1月23日に公開されました。

- [don't code today what you can't debug tomorrow: PhantomJS: minimalistic headless WebKit-based JavaScript-driven tool](http://ariya.blogspot.com/2011/01/phantomjs-minimalistic-headless-webkit.html)

JSer.infoではPhantomJSがリリースされた日にPhantomJSを紹介する記事を書いていました。

- [WebkitベースのJavaScriptコマンドラインツール「PhantomJS」 - JSer.info](https://jser.info/post/2888913234)

現在ではChromeとFirefoxそれぞれでヘッドレスモードが公式にサポートされています。

<script src="https://gist.github.com/azu/c4206d94f18f35f6fe2fe303f988e7d5.js"></script>

ブラウザに同様の機能が実装され開発を終了したものとしては、開発者ツールの元となったFirebugがあります。

- [Saying Goodbye to Firebug – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/10/saying-goodbye-to-firebug/)

PhantomJSは[Selenium](https://www.seleniumhq.org/)のような自動テストをはじめ、[スクレイピング](https://github.com/phantombuster/nickjs)、[Prerender](https://github.com/prerender/prerender)、[キャプチャやPDF化](http://phantomjs.org/screen-capture.html)、[パフォーマンス分析](http://yslow.org/)などさまざまな用途で利用されていました。

PhantomJSはバイナリ1つでヘッドレスなブラウザを動かせることから、CIなどいろいろな環境で手軽にブラウザを実行できるツールとして使われ、また自動テストにおいては実際のブラウザよりも自動化がしやすかったため大きな意味をもっていたと思います。

今回のリポジトリのアーカイブ化でPhantomJSは1つの役目を終えたと言えます。

Thanks to [PhantomJS and contributors](https://github.com/ariya/phantomjs/graphs/contributors)!

[PhantomJS]: http://phantomjs.org/
