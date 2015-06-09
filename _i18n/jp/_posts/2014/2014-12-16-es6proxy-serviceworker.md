---
title: "2014-12-16のJS: ES6 Proxy、Web Components、Service Worker"
author: azu
layout: post
date : 2014-12-16T22:00
category: JSer
tags:
    - ES6
    - WebComponents
    - ServiceWorker

---

JSer.info #206 - [Meta programming with ECMAScript 6 proxies](http://www.2ality.com/2014/12/es6-proxies.html "Meta programming with ECMAScript 6 proxies")([日本語訳](http://panda.node.ws/?p=1371 "ECMAScript 6 proxyによるメタプログラミング(1/11) | JSお散歩"))という記事では、ECMAScript 6のProxyについて詳しく解説されています。

ES6 Proxyを使うことでどういう事ができるのかというユースケースやReflect APIについても解説されていて、メタプログラミング的に面白い部分が多いので見ておくといいかもしれません。

----

[Web Componentsの基本的な使い方・まとめ](http://www.h2.dion.ne.jp/%7Edefghi/webc/webc.htm "Web Componentsの基本的な使い方・まとめ")ではWeb Componentsについて詳しく書かれています。

template要素、HTML Imports、Shadow DOM、Custom Elementsといった構成要素毎に書かれているので、興味があるところから読んでみるといいかもしれません。

----

[JavaScript - Chrome 40 で今すぐ ServiceWorker を試す - Qiita](http://qiita.com/kinu/items/2abd61b4390f9bbaffc9 "JavaScript - Chrome 40 で今すぐ ServiceWorker を試す - Qiita")という記事ではChrome 40から利用できるService Workerについて紹介されています。

以下の動画と合わせて読むと分かりやすいかもしれません。

- [▶ Service workersで遊んでみた - YouTube](https://www.youtube.com/watch?v=SmdhzKp0JYM&feature=youtu.be "▶ Service workersで遊んでみた - YouTube")


----

<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at 1.5.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/1.5.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/1.5.0/Changelog.md "jsdom/Changelog.md at 1.5.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

jsdom 1.5.0リリース。

console APIの定義を追加

----

## Ember.js - Ember.js 1.9.0 and 1.10 Beta Released
[emberjs.com/blog/2014/12/08/ember-1-9-0-released.html](http://emberjs.com/blog/2014/12/08/ember-1-9-0-released.html "Ember.js - Ember.js 1.9.0 and 1.10 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 1.9.0と1.10βリリース。

Ember 2.0に向けて1.9では非推奨となった機能があることについて書かれている。

Handlebars 2.0へのアップデート、streams observationパターンの導入等

- [Ember.js - Deprecations: Deprecations](http://emberjs.com/guides/deprecations/ "Ember.js - Deprecations: Deprecations")

----

## Release 3.5 “Mount Sharp” · mbostock/d3
[github.com/mbostock/d3/releases/tag/v3.5.0](https://github.com/mbostock/d3/releases/tag/v3.5.0 "Release 3.5 “Mount Sharp” · mbostock/d3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

D3.js 3.5リリース

- [D3 バージョン 3.5 がリリースされました。 | Daily D3](http://daily.d3js.info/?p=775 "D3 バージョン 3.5 がリリースされました。 | Daily D3")

----

## Release 0.4 · sdesalas/trifleJS
[github.com/sdesalas/trifleJS/releases/tag/v0.4](https://github.com/sdesalas/trifleJS/releases/tag/v0.4 "Release 0.4 · sdesalas/trifleJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">ReleaseNote</span></p>

PhantomJSのIE版的なヘッドレスブラウザであるtrifleJS 0.4リリース。

----

## harmony:specification_drafts [ES Wiki]
[wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#december_6_2014_draft_rev_29](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#december_6_2014_draft_rev_29 "harmony:specification\_drafts \[ES Wiki\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAscript 6 Draft Rev 29リリース。

`RegExp.prototype.flags`の追加、WeakMap/WeakSetから`clear`メソッドの削除、`String.prototype.contains`が`includes`にリネーム

- [TC39 MTG Notes 第43回 報告会](http://azu.github.io/slide/chatwork/tc39-mtg-notes.html "TC39 MTG Notes 第43回 報告会")
- [RegExp.prototype.flags - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/flags "RegExp.prototype.flags - JavaScript | MDN")

----

## Dynatrace AJAX Edition 4.5 is here
[apmblog.compuware.com/2014/12/11/dynatrace-ajax-edition-4-5-last-page-chapter-yet-story-continues/](http://apmblog.compuware.com/2014/12/11/dynatrace-ajax-edition-4-5-last-page-chapter-yet-story-continues/ "Dynatrace AJAX Edition 4.5 is here")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">software</span> <span class="jser-tag">browser</span></p>

Dynatrace AJAX Edition 4.5リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## JavaScript Application Architecture On The Road To 2015 — Medium
[medium.com/@addyosmani/javascript-application-architecture-on-the-road-to-2015-d8125811101b](https://medium.com/@addyosmani/javascript-application-architecture-on-the-road-to-2015-d8125811101b "JavaScript Application Architecture On The Road To 2015 — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

2014年のJavaScript全体のアーキテクチャを振り返り今後どうなるかについての話。

データバインディング、Immutable、Virtual DOM、Web Components、Component同士のメッセージング、ES6とBrowserify、オフラインファースト等

----

## [JavaScript Advent Calendar 2014 No.6] navigator.onLine in Blink
[blog.oimou.com/javascript-advent-calendar-2014-6ri-mu-navigator-onlinemaniatukusu2589ed73/](http://blog.oimou.com/javascript-advent-calendar-2014-6ri-mu-navigator-onlinemaniatukusu2589ed73/ "\[JavaScript Advent Calendar 2014 No.6\] navigator.onLine in Blink")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">blink</span> <span class="jser-tag">コードリーディング</span></p>

navigator.onLineがどのように実装されているかをBlink/Chromeのソースコードから追っていく話。

ブラウザのソースコードを見ていく方法について実例での参考になりそう

----

## How to Use npm as a Build Tool
[blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/](http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/ "How to Use npm as a Build Tool")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span></p>

npm run-scriptをビルドツールとして使う話

クロスプラットフォーム向けにrmの代わりにrimrafモジュールを使ったり、タスクのグループ化やhookについて書かれている。

----

## Meta programming with ECMAScript 6 proxies
[www.2ality.com/2014/12/es6-proxies.html](http://www.2ality.com/2014/12/es6-proxies.html "Meta programming with ECMAScript 6 proxies")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">リファレンス</span> <span class="jser-tag">まとめ</span></p>

ES6のProxyについて詳しい解説。

メタプログラミングとは何か、Proxyはどのように動くのか、ユースケース、Proxyかどうかの判定方法、PropertyDescriptorとあわせた場合の挙動、Reflect APIについて

- [ECMAScript 6 proxyによるメタプログラミング(1/11) | JSお散歩](http://panda.node.ws/?p=1371 "ECMAScript 6 proxyによるメタプログラミング(1/11) | JSお散歩")

----

## Snap.svgの使い方まとめ
[www.h2.dion.ne.jp/~defghi/snapsvg/snapsvg.xhtml](http://www.h2.dion.ne.jp/~defghi/snapsvg/snapsvg.xhtml "Snap.svgの使い方まとめ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">まとめ</span></p>

Snap.svgについての詳しい解説、チュートリアル。

目的や基本的な使い方から応用、Raphaël.jsとの違いなどよくまとまってる

----

## SVGOを使ったSVGの軽量化方法（アニメーションさせるときの注意とか）｜2.IDEA
[2ndidea.com/svg/optimize-svg-with-svgo/](http://2ndidea.com/svg/optimize-svg-with-svgo/ "SVGOを使ったSVGの軽量化方法（アニメーションさせるときの注意とか）｜2.IDEA")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">Tools</span></p>

SVGの最適化を行うSVGOの使い方について。

それぞれのプラグインについて解説されてる

----

## Polyfilling Doesn&#x27;t Have to be Difficult -Telerik Developer Network
[developer.telerik.com/featured/polyfilling-doesnt-difficult/](http://developer.telerik.com/featured/polyfilling-doesnt-difficult/ "Polyfilling Doesn&#x27;t Have to be Difficult -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span></p>

polyfillとはどういうものか、実際に`Number.isInteger()`や`placeholder`属性を実装しながら学ぶチュートリアル

----

## Web Componentsの基本的な使い方・まとめ
[www.h2.dion.ne.jp/~defghi/webc/webc.htm](http://www.h2.dion.ne.jp/~defghi/webc/webc.htm "Web Componentsの基本的な使い方・まとめ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">まとめ</span></p>

Web Componentsの構成要素、それぞれの機能について詳しく解説されてる。

template要素、HTML Imports、Shadow DOM、Custom Elementsについて

----

## 実践入門 Ember.js：連載｜gihyo.jp … 技術評論社
[gihyo.jp/dev/serial/01/emberjs](http://gihyo.jp/dev/serial/01/emberjs "実践入門 Ember.js：連載｜gihyo.jp … 技術評論社")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span></p>

Ember.jsについての連載

----

## Ractive.js の紹介 — KaoriYa
[www.kaoriya.net/blog/2014/12/13/](http://www.kaoriya.net/blog/2014/12/13/ "Ractive.js の紹介 — KaoriYa")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span></p>

簡単なTODOアプリを使ったRactive.jsの紹介。

mustache拡張なテンプレートとイベント、データバインディングについて

----

## JavaScript - Chrome 40 で今すぐ ServiceWorker を試す - Qiita
[qiita.com/kinu/items/2abd61b4390f9bbaffc9](http://qiita.com/kinu/items/2abd61b4390f9bbaffc9 "JavaScript - Chrome 40 で今すぐ ServiceWorker を試す - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">JavaScript</span></p>

Service Workerを使ったオフライン処理、スクリプトの登録、更新方法、FetchやCache APIについて

----

## The offline cookbook - JakeArchibald.com
[jakearchibald.com/2014/offline-cookbook/](http://jakearchibald.com/2014/offline-cookbook/ "The offline cookbook - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">JavaScript</span></p>

Service Workerを使った典型的なパターンの紹介。

----

## On Third-Party JavaScript - In Production Case-Study
[blog.risingstack.com/on-third-party-javascript-in-production/](http://blog.risingstack.com/on-third-party-javascript-in-production/ "On Third-Party JavaScript - In Production Case-Study")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">セキュリティ</span></p>

サードパーティJavaScriptのケーススタディから学べる事について。

Mixpanel、Disqusからサイズやキャッシュ、どういう初期化経路を踏むかなどについて書かれている

----

## Introducing the JavaScript Internationalization API ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2014/12/introducing-the-javascript-internationalization-api/](https://hacks.mozilla.org/2014/12/introducing-the-javascript-internationalization-api/ "Introducing the JavaScript Internationalization API ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">API</span></p>

ECMA i18n APIの使い方について。

元々localeCompareやtoLocaleStringといったものがあったがローカライズには不十分であり、その部分にECMA i18n APIを使える。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Papa Parse - Powerful CSV parser for Javascript
[papaparse.com/](http://papaparse.com/ "Papa Parse - Powerful CSV parser for Javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

CSVパーサーライブラリ。

CSVをJSONに変換、WebWorkerを使っての並列処理、ダウンロードしながらのパース等

----

## gcanti/uvdom
[github.com/gcanti/uvdom](https://github.com/gcanti/uvdom "gcanti/uvdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirualDOM</span> <span class="jser-tag">library</span></p>

Virtual DOMを持っているライブラリ(React、virtual-dom等)向けに、それぞれ変換出来る抽象レイヤーの実装。

----

## Offline.js – Handle your users losing their internet connection like a pro
[github.hubspot.com/offline/docs/welcome/](http://github.hubspot.com/offline/docs/welcome/ "Offline.js – Handle your users losing their internet connection like a pro")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

オフラインかどうかを検知して通知出来るライブラリ

----

## decimal.js API
[mikemcl.github.io/decimal.js/](http://mikemcl.github.io/decimal.js/ "decimal.js API")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Decimalを扱うライブラリ。

小数点同士の演算、丸め込みの挙動の指定等、フォーマットを指定しての出力等が出来る

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: TypeScript実践プログラミング (Programmer&#x27;s SELECTION): スティーブ・フェントン, 鈴木 幸敏, 株式会社クイープ
[www.amazon.co.jp/dp/4798139807?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4798139807?tag=amazon0abac-22 "Amazon: TypeScript実践プログラミング (Programmer&#x27;s SELECTION): スティーブ・フェントン, 鈴木 幸敏, 株式会社クイープ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span> <span class="jser-tag">翻訳</span></p>

2015年1月23日 発売

Pro TypeScriptの翻訳本

http://www.apress.com/9781430267911

----

## WebSocket - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920030485.do](http://shop.oreilly.com/product/0636920030485.do "WebSocket - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">book</span></p>

WebSocketについての書籍

----
