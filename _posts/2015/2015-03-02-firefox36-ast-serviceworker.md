---
title: "2015-03-02のJS: Firefox 36.0、ASTのコミュニティ標準、Service Worker"
author: azu
layout: post
date : 2015-03-02T21:15
category: JSer
tags:
    - JavaScript
    - Firefox
    - AST
    - ServiceWorker

---

JSer.info #217 - [Firefox 36.0](https://www.mozilla.org/en-US/firefox/36.0/releasenotes/ "Firefox — Notes (36.0) — Mozilla")がリリースされました。

CSSの機能追加として[will-changeプロパティ](https://dev.opera.com/articles/ja/css-will-change-property/ "will-changeプロパティ")、[@font-face unicode-range](http://teppeis.hatenablog.com/entry/2014/09/safari-backslash-yen-sign "@font-face unicode-range")などが入り、ES6の仕様への追従も`Symbol`を始めとして、[Temporal Dead Zone (TDZ)](http://es6rocks.com/2015/01/temporal-dead-zone-tdz-demystified/ "Temporal Dead Zone (TDZ)")の挙動への対応が行われていて、WebGL 2.0やWeb Animationsの実験的なサポートが追加されています。

詳しい更新内容は以下にまとめられています。

- [Firefox 36 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/36/Site_Compatibility "Firefox 36 サイト互換性情報 - Mozilla | MDN")
- [Firefox 36 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/36 "Firefox 36 for developers - Mozilla | MDN")

ES6の細かい挙動について気になる人は以下のクイズもやってみるといいかもしれません。

- [ES6 Quiz - hogehoge @teramako](http://d.hatena.ne.jp/teramako/20150301/p1 "ES6 Quiz - hogehoge @teramako")

-----

[[2015-02] 最近のJavaScript AST標準化の動き | Web Scratch](http://efcl.info/2015/02/26/recent-js-ast/ "[2015-02] 最近のJavaScript AST標準化の動き | Web Scratch") という記事では、JavaScriptのAST(抽象木)についての最近の変化について詳しく書かれています。

今までは[SpiderMonkey parser](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API "SpiderMonkey parser")によって定義されたASTを元にツールのエコシステムが回っていましたが、ES6の対応が進んでいなかったため各パーサが試行錯誤したり、[Shift AST Specification](https://github.com/shapesecurity/shift-spec "Shift AST Specification")という仕様が登場したりしました。

しかし、最近になって[EsprimaがjQuery Foundationに移管](http://blog.jquery.com/2015/01/26/jquery-foundation-adopts-esprima/ "jQuery Foundation adopts Esprima | Official jQuery Blog")されたのを契機に[ESTree](https://github.com/estree/estree "ESTree")という実質後継となるASTの仕様策定がコミュニティドリブンで進んでいることについて書かれています。

----

[Service worker が拓く mobile web の新しいかたち](http://www.slideshare.net/kinukox/service-worker-mobile-web "Service worker が拓く mobile web の新しいかたち") というスライドでは、Chromeに実装が入っているServiceWorkerがどのような事が出来るのかについてまとまっています。

ServiceWorkerはデバッグやスコープなどで少しはまりやすい部分がありますが、[ServiceWorker のスコープとページコントロールについて - Qiita](http://qiita.com/nhiroki/items/eb16b802101153352bba "ServiceWorker のスコープとページコントロールについて - Qiita")も一緒に読むとServiceWorkerの動きが理解しやすくなると思います。


-----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint 0.15.1 released - ESLint
[eslint.org/blog/2015/02/eslint-0.15.1-released/](http://eslint.org/blog/2015/02/eslint-0.15.1-released/ "ESLint 0.15.1 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.15.1リリース

----

## New AngularJS Releases 1.4.0-beta.5 and 1.3.14
[angularjs.blogspot.com/2015/02/new-angularjs-releases-140-beta5-and.html](http://angularjs.blogspot.com/2015/02/new-angularjs-releases-140-beta5-and.html "New AngularJS Releases 1.4.0-beta.5 and 1.3.14")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

AngularJS 1.4.0-betaと1.3.14 リリース。
CommonJS supportの改善

----

## Firefox — Notes (36.0) — Mozilla
[www.mozilla.org/en-US/firefox/36.0/releasenotes/](https://www.mozilla.org/en-US/firefox/36.0/releasenotes/ "Firefox — Notes (36.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 36.0リリース。
HTTP/2のフルサポート、ES6 Symbolサポート、CSSの`object-fit`と`object-position`、`will-change`、`isolation`の実装、promiseオブジェクトのデバッグ対応など

- [Firefox 36 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/36 "Firefox 36 for developers - Mozilla | MDN")

----

## React v0.13 RC | React
[facebook.github.io/react/blog/2015/02/24/react-v0.13-rc1.html](http://facebook.github.io/react/blog/2015/02/24/react-v0.13-rc1.html "React v0.13 RC | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.13 RCリリース

----

## Pointer Events is a W3C Recommendation | W3C News
[www.w3.org/blog/news/archives/4430](http://www.w3.org/blog/news/archives/4430 "Pointer Events is a W3C Recommendation | W3C News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">event</span> <span class="jser-tag">spec</span></p>

Pointer EventsがW3C Recommendationになった。

- [Pointer Events advance to W3C Recommendation | The Paciello Group – Your Accessibility Partner (WCAG 2.0/508 audits, VPAT, usability and accessible user experience)](http://www.paciellogroup.com/blog/2015/02/pointer-events-advance-to-w3c-recommendation/ "Pointer Events advance to W3C Recommendation | The Paciello Group – Your Accessibility Partner (WCAG 2.0/508 audits, VPAT, usability and accessible user experience)")
- [Pointer Events W3C Recommendation, Interoperable Touch, and Removing the Dreaded 300ms Tap Delay - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2015/02/24/pointer-events-w3c-recommendation-interoperable-touch-and-removing-the-dreaded-300ms-tap-delay.aspx "Pointer Events W3C Recommendation, Interoperable Touch, and Removing the Dreaded 300ms Tap Delay - IEBlog - Site Home - MSDN Blogs")
- [Getting on Point | Official jQuery Blog](http://blog.jquery.com/2015/02/24/getting-on-point/ "Getting on Point | Official jQuery Blog")

----

## Release v2.4.0 · marionettejs/backbone.marionette
[github.com/marionettejs/backbone.marionette/releases/tag/v2.4.0](https://github.com/marionettejs/backbone.marionette/releases/tag/v2.4.0 "Release v2.4.0 · marionettejs/backbone.marionette")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Marionette 2.4.0リリース。
CollectionViewとCompositeViewのパフォーマンスや機能強化が中心。
`Marionette.Controller`が非推奨となり`Marionette.Object`を利用するようになった

----

## WebStorm 10 EAP, 140.2753: V8 profiling, TypeScript 1.4 and built-in TypeScript compiler | JetBrains WebStorm Blog
[blog.jetbrains.com/webstorm/2015/02/webstorm-10-eap-140-2753/](http://blog.jetbrains.com/webstorm/2015/02/webstorm-10-eap-140-2753/ "WebStorm 10 EAP, 140.2753: V8 profiling, TypeScript 1.4 and built-in TypeScript compiler | JetBrains WebStorm Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">ReleaseNote</span></p>

WebStorm 10 EAPリリース。
V8のプロファイリングツール連携、TypeScript 1.4サポート、Scratch filesの改善など

----
<h1 class="site-genre">アーティクル</h1>

----

## [2015-02] 最近のJavaScript AST標準化の動き | Web Scratch
[efcl.info/2015/02/26/recent-js-ast/](http://efcl.info/2015/02/26/recent-js-ast/ "\[2015-02\] 最近のJavaScript AST標準化の動き | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">まとめ</span></p>

EspreeやShift AST、esprimaがjQuery Foundationに移管された事により活発化したAST周りの動きについて。
ESTreeというASTのコミュニティスタンダードについてなどの話

----

## ServiceWorker のスコープとページコントロールについて - Qiita
[qiita.com/nhiroki/items/eb16b802101153352bba](http://qiita.com/nhiroki/items/eb16b802101153352bba "ServiceWorker のスコープとページコントロールについて - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">JavaScript</span></p>

ServiceWorkerのスコープとコントール出来るようになるタイミングなどのライフサイクルについての解説

----

## ES6 Quiz - hogehoge @teramako
[d.hatena.ne.jp/teramako/20150301/p1](http://d.hatena.ne.jp/teramako/20150301/p1 "ES6 Quiz - hogehoge @teramako")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span></p>

ECMAScript 6 クイズ

----

## Exploring ES6 Classes In AngularJS 1.x
[www.michaelbromley.co.uk/blog/350/exploring-es6-classes-in-angularjs-1-x](http://www.michaelbromley.co.uk/blog/350/exploring-es6-classes-in-angularjs-1-x "Exploring ES6 Classes In AngularJS 1.x")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

Angular 1.xでES6 classを使って記述する方法についての記事

----

## Iterables and iterators in ECMAScript 6
[www.2ality.com/2015/02/es6-iteration.html](http://www.2ality.com/2015/02/es6-iteration.html "Iterables and iterators in ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6のIteratorについての詳しい解説。
for..ofでのイテレート、spread演算子での展開、`Symbol.iterator`でのIterableの実装などについて

----

## JavaScript - web-animations-jsで策定中のAPIを先取りする - Qiita
[qiita.com/haribote/items/a8fc84d6cc2fd4abbf72](http://qiita.com/haribote/items/a8fc84d6cc2fd4abbf72 "JavaScript - web-animations-jsで策定中のAPIを先取りする - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

Web Animations APIのpolyfillの基本的な使い方について

----

## ECMAScript7を見据えた、JavaScript(TypeScript)で使えるFRPライブラリの比較調査 - Qiita
[qiita.com/kondei/items/17e5d4867a0652911e52](http://qiita.com/kondei/items/17e5d4867a0652911e52 "ECMAScript7を見据えた、JavaScript(TypeScript)で使えるFRPライブラリの比較調査 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span></p>

RxJS、Bacon.js、Kefire.jsの比較

----

## よろしくESLint - Weblog - Hail2u.net
[hail2u.net/blog/coding/come-into-eslint.html](http://hail2u.net/blog/coding/come-into-eslint.html "よろしくESLint - Weblog - Hail2u.net")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLintの設定について。
packge.jsonにも設定を書くことができる点やJSHintからの移行について

----

## JavaScript入門用のコンソールプログラムjavascriptingを翻訳しました - @ledsun blog
[ledsun.hatenablog.com/entry/2015/02/26/085717](http://ledsun.hatenablog.com/entry/2015/02/26/085717 "JavaScript入門用のコンソールプログラムjavascriptingを翻訳しました - @ledsun blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">翻訳</span></p>

nodeschool.ioで使われてるJavaScriptの文法を学ぶコンソールアプリの翻訳

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## CSS 4 - What&#x27;s coming up // Speaker Deck
[speakerdeck.com/diegoeis/css-4-whats-coming-up](https://speakerdeck.com/diegoeis/css-4-whats-coming-up "CSS 4 - What&#x27;s coming up // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span></p>

CSS Selector、Media Queries Lv4についてのスライド

----

## Service worker が拓く mobile web の新しいかたち
[www.slideshare.net/kinukox/service-worker-mobile-web](http://www.slideshare.net/kinukox/service-worker-mobile-web "Service worker が拓く mobile web の新しいかたち")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">スライド</span></p>

ServiceWorkerについてのスライド。
どういうことができるのか、Fetch API、Fetch APIのResponse、デバッグ方法、セキュリティポリシーについて。
Chromeでの実装者によるスライド

----

## hello world » AngularJS 도입 선택 가이드 공개합니다.
[helloworld.naver.com/helloworld/1172239](http://helloworld.naver.com/helloworld/1172239 "hello world » AngularJS 도입 선택 가이드 공개합니다.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">PDF</span> <span class="jser-tag">資料</span> <span class="jser-tag">韓国</span></p>

AngularJS導入ガイド

----

## mattpodwysocki/applicative-2015
[github.com/mattpodwysocki/applicative-2015](https://github.com/mattpodwysocki/applicative-2015 "mattpodwysocki/applicative-2015")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">スライド</span></p>

RxJSについてのスライド。
First class async value、RxのonNext, onError, onComplete、どういう流れで処理を書けるかについてなど

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Vue.js資料まとめ
[gist.github.com/hashrock/f575928d0e109ace9ad0](https://gist.github.com/hashrock/f575928d0e109ace9ad0 "Vue.js資料まとめ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">links</span></p>

Vue.jsについてのリソースまとめ

----

## diafygi/webcrypto-examples
[github.com/diafygi/webcrypto-examples](https://github.com/diafygi/webcrypto-examples "diafygi/webcrypto-examples")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">セキュリティ</span> <span class="jser-tag">サンプル</span></p>

Web Cryptography APIのサンプル集

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jxcore·io
[jxcore.io/](http://jxcore.io/ "jxcore·io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span></p>

Node.jsを拡張したフレームワーク。
SpiderMonkeyとV8のエンジンの切り替え、マルチスレッドサポート、モバイルアプリへの組み込みなどをサポートしてる

- [Node.jsを拡張した「JXCore」、オープンソースでソースコードを公開 | SourceForge.JP Magazine](http://sourceforge.jp/magazine/15/02/24/164700 "Node.jsを拡張した「JXCore」、オープンソースでソースコードを公開 | SourceForge.JP Magazine")

----

## olahol/eselement
[github.com/olahol/eselement](https://github.com/olahol/eselement "olahol/eselement")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

ASTをDOMライクなAPIで操作出来るライブラリ。
querySelector、childNodes、removeChild、createElementのようなAPIが用意されてる

----

## Validate.js
[validatejs.org/](http://validatejs.org/ "Validate.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存がするライブラリがないバリデーションライブラリ。

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon.co.jp： ブレイクスルーJavaScript フロントエンドエンジニアとして越えるべき5つの壁―オブジェクト指向からシングルページアプリケーションまで: 太田 智彬, 田辺 丈士, 新井 智士, 大江 遼, 株式会社アイ・エム・ジェイ: 本
[www.amazon.co.jp/dp/479813905X/](http://www.amazon.co.jp/dp/479813905X/ "Amazon.co.jp： ブレイクスルーJavaScript フロントエンドエンジニアとして越えるべき5つの壁―オブジェクト指向からシングルページアプリケーションまで: 太田 智彬, 田辺 丈士, 新井 智士, 大江 遼, 株式会社アイ・エム・ジェイ: 本")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2015年4月17日 発売
オブジェクト指向、イベント、Canvas、Ajax、シングルページアプリケーションについての書籍

----
