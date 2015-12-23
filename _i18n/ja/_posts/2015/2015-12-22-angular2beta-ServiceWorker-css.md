---
title: "2015-12-22のJS: AngularJS 2β、ServiceWorker Cookbook、非標準CSSの修正"
author: azu
layout: post
date : 2015-12-22T21:06
category: JSer
tags:
    - Angular
    - ServiceWorker
    - CSS
    - webkit

---

JSer.info #258 - [AngularJS 2 Beta](http://angularjs.blogspot.jp/2015/12/angular-2-beta.html "Angular 2 Beta")がリリースされました。

まだbetaではありますが、1.xからのアップグレード方法として以下の2つのアプローチが紹介されています。

- ngUpgrade
  - 1.xと2.xを共存させながらアップグレードしていく手法
  - [Upgrading apps to Angular 2 using ngUpgrade](http://blog.thoughtram.io/angular/2015/10/24/upgrading-apps-to-angular-2-using-ngupgrade.html "Upgrading apps to Angular 2 using ngUpgrade")
  - [Upgrading from 1.x - ts](https://angular.io/docs/ts/latest/guide/upgrade.html "Upgrading from 1.x - ts")
- ngForward
  - AngularJS 2.xのスタイルで1.xのコードを書く手法
  - [ngUpgraders/ng-forward](https://github.com/ngUpgraders/ng-forward "ngUpgraders/ng-forward")

今後はファイルサイズの削減、CLIの改善、i18nのサポートなどをやっていくそうです。
以下でマイルストーンのチケット消化率を見ることが出来ます。

- [Angular 2 Beta Burndown](http://juristr.com/apps/ng2beta/ "Angular 2 Beta Burndown")

----

[Beyond Offline ★ Mozilla Hacks](https://hacks.mozilla.org/2015/12/beyond-offline/ "Beyond Offline ★ Mozilla Hacks")という記事では、Service Workerのオフライン対応以外の使い道について書かれています。

具体的なパターンやコード例については以下のサイトにまとめられています。

- [ServiceWorker Cookbook](https://serviceworke.rs/ "ServiceWorker Cookbook")

Service Workerの典型的なユースケースとして紹介されるオフライン対応については以下にまとめられています。

- [Offline Recipes for Service Workers ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/11/offline-service-workers/ "Offline Recipes for Service Workers ★ Mozilla Hacks – the Web developer blog")
- [The offline cookbook - JakeArchibald.com](https://jakearchibald.com/2014/offline-cookbook/ "The offline cookbook - JakeArchibald.com") ([翻訳](https://github.com/kuu/the-offline-cookbook-ja/blob/master/ja.md))

----

[総行数57,000の巨大CSS群をLessに書き換えた軌跡 - mixi Engineers' Blog](http://alpha.mixi.co.jp/entry/2015/12/20/000000 "総行数57,000の巨大CSS群をLessに書き換えた軌跡")という記事ではモバイルのWebKitブラウザのみの対応を目的としたCSSをどうやって修正したかについて書かれています。

`-webkit-` prefixや標準でない書き方のCSSを[css-fixme](https://github.com/Kuniwak/css-fixme "css-fixme")などで標準的なCSSへと修正し、それを[Autoprefixer](https://github.com/postcss/autoprefixer "Autoprefixer")で変換するという手法について解説されています。

vendor prefixに対する取り組みなどは下記を参照するといいかもしれません。

- [CSS vendor prefixes considered harmful - QuirksBlog](http://www.quirksmode.org/blog/archives/2010/03/css_vendor_pref.html)
- [WebCompat](http://wontfix.blogspot.jp/2015/08/webcompat.html)
- [A break from the past, part 2: Saying goodbye to ActiveX, VBScript, attachEvent… | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2015/05/06/a-break-from-the-past-part-2-saying-goodbye-to-activex-vbscript-attachevent/)



----
<h1 class="site-genre">ヘッドライン</h1>

----

## Angular 2 Beta
[angularjs.blogspot.jp/2015/12/angular-2-beta.html](http://angularjs.blogspot.jp/2015/12/angular-2-beta.html "Angular 2 Beta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

AngularJS 2βリリース。
AngularJS 1からのアップグレードガイドも公開されている

- [Upgrading from 1.x - ts](https://angular.io/docs/ts/latest/guide/upgrade.html "Upgrading from 1.x - ts")

----

## RxJS/CHANGELOG.md at 5.0.0-beta.0 · ReactiveX/RxJS
[github.com/ReactiveX/RxJS/blob/5.0.0-beta.0/CHANGELOG.md](https://github.com/ReactiveX/RxJS/blob/5.0.0-beta.0/CHANGELOG.md "RxJS/CHANGELOG.md at 5.0.0-beta.0 · ReactiveX/RxJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

RxJS 5.0.0-beta.0リリース

----

## Firefox 43.0 リリースノート
[www.mozilla.jp/firefox/43.0/releasenotes/](http://www.mozilla.jp/firefox/43.0/releasenotes/ "Firefox 43.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 43リリース。
ES2016の`Array.prototype.includes`がデフォルトで有効、Subresource integrityの対応など

- [Firefox 43 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/43 "Firefox 43 for developers - Mozilla | MDN")
- [Firefox 43 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/43/ "Firefox 43 サイト互換性情報 | Firefox サイト互換性情報")

----

## Node v5.3.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.3.0/](https://nodejs.org/en/blog/release/v5.3.0/ "Node v5.3.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v5.3.0リリース。
`Buffer.prototype.includes()`の追加、REPLで外部モジュールを`require`できないバグを修正など

----

## flow/Changelog.md at master · facebook/flow
[github.com/facebook/flow/blob/master/Changelog.md#v0200](https://github.com/facebook/flow/blob/master/Changelog.md#v0200 "flow/Changelog.md at master · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.20.0リリース。
`this`型のサポート、`.json`ファイルロードの解釈に対応、エラーメッセージの改善など

----

## Release ES2016 Draft 2015-12-20 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20151220](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20151220 "Release ES2016 Draft 2015-12-20 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2015-12-20リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## 総行数57,000の巨大CSS群をLessに書き換えた軌跡 - mixi Engineers&#x27; Blog
[alpha.mixi.co.jp/entry/2015/12/20/000000](http://alpha.mixi.co.jp/entry/2015/12/20/000000 "総行数57,000の巨大CSS群をLessに書き換えた軌跡 - mixi Engineers' Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">LESS</span> <span class="jser-tag">webkit</span></p>

-webkit- prefixから標準への書き換えを行った話。
CSS:fixmeで標準記法へ直し、Autoprefixerでプレフィックス対応し、Lessを使い構造的に管理しやすくしていく

- [マルチブラウザやりました (DMM.Study Night)](http://www.slideshare.net/sugibigmuff/dmmstudy-night "マルチブラウザやりました (DMM.Study Night)")

----

## An Intro To Using npm and ES6 Modules for Front End Development | Wes Bos
[wesbos.com/javascript-modules/](http://wesbos.com/javascript-modules/ "An Intro To Using npm and ES6 Modules for Front End Development | Wes Bos")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 modulesの使い方についてまとまっている。
どのようにパスを解決したりするかはECMAScriptで定義されていないため、今のところbundlerの機能でしかないという点についても触れている。

----

## HTTP/2のNode.js実装node-http2を読む - Qiita
[qiita.com/takaaki7/items/70898443050ca260e94c](http://qiita.com/takaaki7/items/70898443050ca260e94c "HTTP/2のNode.js実装node-http2を読む - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP2</span> <span class="jser-tag">stream</span></p>

node-http2の実装について。
Node Streamを使い、それをフロー制御している

----

## Beyond Offline ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/12/beyond-offline/](https://hacks.mozilla.org/2015/12/beyond-offline/ "Beyond Offline ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span></p>

Service Workerをオフライン対応以外の用途で使う方法について。
クックブック形式で色々なパターンを紹介している

- [ServiceWorker Cookbook](https://serviceworke.rs/ "ServiceWorker Cookbook")
- [the-offline-cookbook-ja/ja.md at master · kuu/the-offline-cookbook-ja](https://github.com/kuu/the-offline-cookbook-ja/blob/master/ja.md "the-offline-cookbook-ja/ja.md at master · kuu/the-offline-cookbook-ja")

----

## FluxのActionとStoreをちゃんと分ける話 - pixiv inside
[inside.pixiv.net/entry/2015/12/19/113746](http://inside.pixiv.net/entry/2015/12/19/113746 "FluxのActionとStoreをちゃんと分ける話 - pixiv inside")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

Actionでデータを構築し、StoreへDispatchする。
またDispatchするデータは`Entity`にすることで、役割を分けるという話

----

## deku で Virtual DOM を使う | スマホ神 – JavaScript 受託開発 –
[smart.ataglance.jp/2015-12-17-use-virtual-dom-with-deku/](http://smart.ataglance.jp/2015-12-17-use-virtual-dom-with-deku/ "deku で Virtual DOM を使う | スマホ神 – JavaScript 受託開発 –")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">library</span></p>

dekuの使い方について。
JSXで書いてBabelで変換する方法

----

## More Responsive Tapping on iOS | WebKit
[webkit.org/blog/5610/more-responsive-tapping-on-ios/](https://webkit.org/blog/5610/more-responsive-tapping-on-ios/ "More Responsive Tapping on iOS | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ios</span></p>

iOSのWebKitでもタップの350ms遅延が解消される。
viewportのwidthなど特定の条件では遅延がなくなる。

- [300ms tap delay, gone away | Web Updates - Google Developers](https://developers.google.com/web/updates/2013/12/300ms-tap-delay-gone-away "300ms tap delay, gone away | Web Updates - Google Developers")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ServiceWorker Cookbook
[serviceworke.rs/](https://serviceworke.rs/ "ServiceWorker Cookbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">document</span></p>

Service Workerのパターンを集めたクックブック。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## A-Frame – Building Blocks for the VR Web
[aframe.io/](https://aframe.io/ "A-Frame – Building Blocks for the VR Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">VR</span> <span class="jser-tag">HTML</span> <span class="jser-tag">WebComponents</span></p>

WebVRをCustom Elementのタグを書くだけで出来るライブラリ

----

## jaredly/treed
[github.com/jaredly/treed](https://github.com/jaredly/treed "jaredly/treed")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

ツリーエディタライブラリ

----

## pzavolinsky/react-unit
[github.com/pzavolinsky/react-unit](https://github.com/pzavolinsky/react-unit "pzavolinsky/react-unit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

React Componentをテストするためのライブラリ

----

## paldepind/snabbdom
[github.com/paldepind/snabbdom](https://github.com/paldepind/snabbdom "paldepind/snabbdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">library</span></p>

Virtual DOMライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: ゲームで学ぶJavaScript入門 HTML5&amp;CSSも身に付く!: 田中 賢一郎
[www.amazon.co.jp/dp/4844339788](http://www.amazon.co.jp/dp/4844339788 "Amazon: ゲームで学ぶJavaScript入門 HTML5&CSSも身に付く!: 田中 賢一郎")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">book</span></p>

ゲームを作りながらJavaScriptについて学ぶ書籍

----

## Learning React Native - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920041511.do](http://shop.oreilly.com/product/0636920041511.do "Learning React Native - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React Nativeについての書籍

----
