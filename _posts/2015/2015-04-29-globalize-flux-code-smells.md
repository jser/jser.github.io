---
title: "2015-04-29のJS: Globalize 1.0、Flux実装、Code Smellsの検出"
author: azu
layout: post
date : 2015-04-29T23:17
category: JSer
tags:
    - i18n
    - Flux
    - JavaScript

---

JSer.info #225 - [CLDR](http://cldr.unicode.org/ "CLDR - Unicode Common Locale Data Repository")ベースの国際化対応ライブラリである[jquery/globalize](https://github.com/jquery/globalize "jquery/globalize") 1.0がリリースされました。

- [Announcing Globalize 1.0 | Official jQuery Blog](http://blog.jquery.com/2015/04/23/announcing-globalize-1-0/ "Announcing Globalize 1.0 | Official jQuery Blog")

日付や数値、通貨の国際化対応やICU message formatのサポートがされています。
類似するライブラリとしては[FormatJS](http://formatjs.io/ "FormatJS")などがあります。

----

[React.js meetup #1](http://reactjs-meetup.connpass.com/event/11232/ "React.js meetup #1 - connpass")や[O&#39;Reilly Fluent](http://fluentconf.com/javascript-html-2015 "O&#39;Reilly Fluent")などのイベントがありFluxについての話が色々でていたのでまとめて紹介。

- [10分で実装するFlux](http://azu.github.io/slide/react-meetup/flux.html "10分で実装するFlux")
	- Fluxを一から実装してみて、データがホントに一方通行に流れてるのかを確認するという趣旨のスライド
	- EventEmitterから実装してみてますが、Viewを除くと50行程度で書けるものであるという話
	- 実装: [azu/mini-flux](https://github.com/azu/mini-flux "azu/mini-flux")
- [ReactとFluxのこと // Speaker Deck](https://speakerdeck.com/geta6/reacttofluxfalsekoto "ReactとFluxのこと // Speaker Deck")
	- ReactとFluxがどういう仕組みだったり、実際どう動いてるのかを具体的に解説してるスライド
- [react-flux-fluent-2015 // Speaker Deck](https://speakerdeck.com/fisherwebdev/react-flux-fluent-2015 "react-flux-fluent-2015 // Speaker Deck")
	- [facebook/flux](https://github.com/facebook/flux "facebook/flux")のメンテナーである[Bill Fisher](https://github.com/fisherwebdev "Bill Fisher")によるFluxについてのスライド
	- Fluxの構成する要素の役割を順を追って解説したりアンチパターンについても書かれている

他にも実践してみた系の記事がでてるので好みのアプローチで見てみるといいかもしれません。

- [React+FluxでTodoMVCを作ってFluxについて学んでみた - yutaponのブログ](http://yutapon.hatenablog.com/entry/2015/04/27/150000)
- [橋本商会 » React+Fluxxor+socket.ioでfluxなチャットを作った](http://shokai.org/blog/archives/9929)

----

[Eliminate JavaScript Code Smells](http://elijahmanor.github.io/talks/js-smells/#/ "Eliminate JavaScript Code Smells") というスライドでは、いわゆるCode Smells(何かの問題になる兆候)を発見する方法について書かれています。

- [コードの臭い - Wikipedia](http://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E8%87%AD%E3%81%84 "コードの臭い - Wikipedia")

[ESLint](http://eslint.org/ "ESLint")や[danielstjules/jsinspect](https://github.com/danielstjules/jsinspect "danielstjules/jsinspect")などのツールを使った方法や色々なパターンのCode Smellsについて書かれていて面白い内容になっています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Pixi.js v3 - Goodboy™ — Goodboy™
[www.goodboydigital.com/pixi-js-v3/](http://www.goodboydigital.com/pixi-js-v3/ "Pixi.js v3 - Goodboy™ — Goodboy™")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">game</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptゲームエンジンのpixi.js v3リリース。 WebGL Renderer、Particle Containerの追加、Interaction、Resolution管理の改善など

----

## jQuery 1.11.3 and 2.1.4 Released – iOS Fail-Safe Edition | Official jQuery Blog
[blog.jquery.com/2015/04/28/jquery-1-11-3-and-2-1-4-released-ios-fail-safe-edition/](http://blog.jquery.com/2015/04/28/jquery-1-11-3-and-2-1-4-released-ios-fail-safe-edition/ "jQuery 1.11.3 and 2.1.4 Released – iOS Fail-Safe Edition | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 1.11.3 と 2.1.4リリース。
iOS8.2と8.3向けのワークアラウンドの追加

- [Prevent iOS from improperly JIT-ing isArrayLike by jridgewell · Pull Request #2094 · jashkenas/underscore](https://github.com/jashkenas/underscore/pull/2094 "Prevent iOS from improperly JIT-ing isArrayLike by jridgewell · Pull Request #2094 · jashkenas/underscore")
- [Bug 142792 – Objects with numeric properties intermittently get a phantom &#x27;length&#x27; property](https://bugs.webkit.org/show_bug.cgi?id=142792 "Bug 142792 – Objects with numeric properties intermittently get a phantom &#x27;length&#x27; property")

----

## Dev.Opera — Opera 29 released
[dev.opera.com/blog/opera-29/](https://dev.opera.com/blog/opera-29/ "Dev.Opera — Opera 29 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 29 (based on Chromium 42) リリース。
ES6 classes、object literalsの拡張サポート、Fetch APIがwindowコンテキストでも利用できるように、Web Audio APIの仕様追従など

----

## Announcing PEP 0.3.0 | Official jQuery Blog
[blog.jquery.com/2015/04/21/announcing-pep-0-3-0/](http://blog.jquery.com/2015/04/21/announcing-pep-0-3-0/ "Announcing PEP 0.3.0 | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

PEP(Pointer Events Polyfill) 0.3.0リリース

----

## Announcing Globalize 1.0 | Official jQuery Blog
[blog.jquery.com/2015/04/23/announcing-globalize-1-0/](http://blog.jquery.com/2015/04/23/announcing-globalize-1-0/ "Announcing Globalize 1.0 | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Unicode CLDRベースの国際化対応ライブラリであるGlobalize 1.0リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## ES6 を学べる tower-of-babel を作りました。 (workshopper の作り方) - from scratch
[yosuke-furukawa.hatenablog.com/entry/2015/04/26/104521](http://yosuke-furukawa.hatenablog.com/entry/2015/04/26/104521 "ES6 を学べる tower-of-babel を作りました。 (workshopper の作り方) - from scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

workshopper / workshopper-exerciseを使ったエクササイズの作り方について

----

## JavaScriptでパーサコンビネータのコンセプトを理解する(「正規表現だけに頼ってはいけない」の続き) - id:anatooのブログ
[blog.anatoo.jp/entry/2015/04/26/220026](http://blog.anatoo.jp/entry/2015/04/26/220026 "JavaScriptでパーサコンビネータのコンセプトを理解する(「正規表現だけに頼ってはいけない」の続き) - id:anatooのブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span></p>

JavaScriptでパーサコンビネータを実装して、パーサコンビネータについて学ぶ話

----

## 【翻訳】ReactをjQueryの数行に要約する | POSTD
[postd.cc/boiling-react-down-to-a-few-lines-in-jquery/](http://postd.cc/boiling-react-down-to-a-few-lines-in-jquery/ "【翻訳】ReactをjQueryの数行に要約する | POSTD")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">翻訳</span></p>

jQueryで書いたコードにReactのアイデアを適応して、状態の変更とDOMへの反映へと処理を分けていく話。
Virtual DOMやimmutabilityについても触れている

----

## SinonJs Spies – Zsolt Nagy – Development of Maintainable Web-Applications
[zsolt-nagy.github.io/SinonJs-Spies/](http://zsolt-nagy.github.io/SinonJs-Spies/ "SinonJs Spies – Zsolt Nagy – Development of Maintainable Web-Applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

Sinon.JSのspyを使ったテストについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 10分で実装するFlux
[azu.github.io/slide/react-meetup/flux.html](http://azu.github.io/slide/react-meetup/flux.html "10分で実装するFlux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

一からFluxアーキテクチャを実装してみてFluxがどういう仕組みで回ってるのかを確認していくスライド。
Fluxの特徴であるデータの一方通行に流れているかをスタックトレースで確認する

- [橋本商会 » flux.DispatcherのwaitForの実装](http://shokai.org/blog/archives/9905 "橋本商会 » flux.DispatcherのwaitForの実装")
- [React+FluxでTodoMVCを作ってFluxについて学んでみた - yutaponのブログ](http://yutapon.hatenablog.com/entry/2015/04/27/150000 "React+FluxでTodoMVCを作ってFluxについて学んでみた - yutaponのブログ")

----

## ReactとFluxのこと // Speaker Deck
[speakerdeck.com/geta6/reacttofluxfalsekoto](https://speakerdeck.com/geta6/reacttofluxfalsekoto "ReactとFluxのこと // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">スライド</span></p>

Reactによって富豪的なViewの描画が現実的なレベルに落とせる話やFluxアーキテクチャがどういう形でデータを一方通行に回すかについて書かれているスライド

- [社内勉強会でReactとFluxについて喋った - pixiv engineering blog](http://inside.pixiv.net/entry/2015/04/27/170944 "社内勉強会でReactとFluxについて喋った - pixiv engineering blog")

----

## react-flux-fluent-2015 // Speaker Deck
[speakerdeck.com/fisherwebdev/react-flux-fluent-2015](https://speakerdeck.com/fisherwebdev/react-flux-fluent-2015 "react-flux-fluent-2015 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">スライド</span></p>

[facebook/flux](https://github.com/facebook/flux "facebook/flux")モジュール作者によるFluxについてのスライド。
Fluxの構成要素、Dispatcher、Storeがシングルトンであること、React、Fluxのアンチパターンについて書かれてる

----

## Video: JavaScript, HTML5, CSS3 Conference - O&#x27;Reilly Fluent, April 20 - 22, 2015, San Francisco, CA
[fluentconf.com/javascript-html-2015/public/content/video](http://fluentconf.com/javascript-html-2015/public/content/video "Video: JavaScript, HTML5, CSS3 Conference - O&#x27;Reilly Fluent, April 20 - 22, 2015, San Francisco, CA")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

Fluent Conf 2015の動画が公開されている

----

## ES6 in Production // Speaker Deck
[speakerdeck.com/pazguille/es6-in-production](https://speakerdeck.com/pazguille/es6-in-production "ES6 in Production // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">スライド</span></p>

ES6を使っていくためのスライド。 node_modules以下もBrowserify(Babelify)で変換するには、`global`オプションを利用する。ES6で書いたモジュールをES5から使えるように公開する方法、ES6 classesやBabelのlooseモードについてなど

----

## Eliminate JavaScript Code Smells
[elijahmanor.github.io/talks/js-smells/#/](http://elijahmanor.github.io/talks/js-smells/#/ "Eliminate JavaScript Code Smells")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">スライド</span></p>

JSHintやESLintを使って複雑なコードの検出、jsinspectやjscpdを使ってコピー&ペーストを検出、色々なあやしいコードの検出するeslint pluginや特定のライブラリをサポートするeslint pluginについて

- [elijahmanor/eslint-plugin-smells](https://github.com/elijahmanor/eslint-plugin-smells "elijahmanor/eslint-plugin-smells")

----

## Solar System of JS
[shaunlebron.github.io/solar-system-of-js/#0](http://shaunlebron.github.io/solar-system-of-js/#0 "Solar System of JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">歴史</span> <span class="jser-tag">スライド</span></p>

今のJavaScript、今後のJavaScriptに関係ある要素や言語などをビジュアライズしてるスライド。

- [▶ ECMAScript Harmony: Rise of the Compilers - Brendan Eich keynote - YouTube](https://www.youtube.com/watch?v=PlmsweSNhTw "▶ ECMAScript Harmony: Rise of the Compilers - Brendan Eich keynote - YouTube")
- [shaunlebron/solar-system-of-js](https://github.com/shaunlebron/solar-system-of-js "shaunlebron/solar-system-of-js")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## The WebKit Open Source Project - Web Platform Status
[www.webkit.org/status.html](http://www.webkit.org/status.html "The WebKit Open Source Project - Web Platform Status")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span></p>

WebkitのStatusダッシュボード。 新しい機能等の実装状況について書かれてる。

- [Browser Platform Status Tracker](http://platformstatustracker.azurewebsites.net/ "Browser Platform Status Tracker") もWebkitのStatusに対応

----

## Loupe
[latentflip.com/loupe/](http://latentflip.com/loupe/ "Loupe")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">動画</span></p>

JavaScriptのコールスタック、イベントループ、コールバックキューについて学べるサイトと動画

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## HerringtonDarkholme/typescript-repl
[github.com/HerringtonDarkholme/typescript-repl](https://github.com/HerringtonDarkholme/typescript-repl "HerringtonDarkholme/typescript-repl")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

コード補完もできるTypeScript REPL

----

## angus-c/es6-react-mixins
[github.com/angus-c/es6-react-mixins](https://github.com/angus-c/es6-react-mixins "angus-c/es6-react-mixins")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React ComponentのmixinをES6 Classesを使って行うライブラリ

----

## rambler-digital-solutions/es6-class-mixin
[github.com/rambler-digital-solutions/es6-class-mixin](https://github.com/rambler-digital-solutions/es6-class-mixin "rambler-digital-solutions/es6-class-mixin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ES6 classesでのmixinを行うライブラリ。
`class Input extends mixin(BaseClass. mixin) {}` という感じでBaseClassを拡張したクラスをその場で作成する

----

## mohayonao/tickable-timer
[github.com/mohayonao/tickable-timer](https://github.com/mohayonao/tickable-timer "mohayonao/tickable-timer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

setTimeout/setInterval互換のAPIを持ち、任意の間隔で進めたり、イベント通知の機能を持つテスト向けのタイマーライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Security for Web Developers: Using JavaScript, HTML, and CSS: John Paul Mueller: 9781491928646: Amazon.com: Books
[www.amazon.com/Security-Web-Developers-Using-JavaScript/dp/1491928646](http://www.amazon.com/Security-Web-Developers-Using-JavaScript/dp/1491928646 "Security for Web Developers: Using JavaScript, HTML, and CSS: John Paul Mueller: 9781491928646: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">セキュリティ</span> <span class="jser-tag">book</span></p>

2015年9月25日発売 ウェブ開発者向けのセキュリティについての書籍

----