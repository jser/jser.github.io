---
title: "2015-06-30のJS: Ember Data Stableリリース、JavaScriptアンケート"
author: azu
layout: post
date : 2015-06-30T20:28
category: JSer
tags:
    - Ember
    - アンケート
    - JavaScript
    - ECMAScript

---

JSer.info #234 - Ember DataがついにStableリリースされました。

- [Ember.js - Ember Data v1.13 Released](http://emberjs.com/blog/2015/06/18/ember-data-1-13-released.html "Ember.js - Ember Data v1.13 Released")

2年ほど前に[Ember Data 1.0 Beta 1](http://emberjs.com/blog/2013/08/31/ember-1-0-released.html "Ember Data 1.0 Beta 1")が公開されていましたが、その後も順調に変化を重ねて、今回Ember.jsのバージョンに併せてEmber Data 1.13としてリリースされました。

リリース記事ではEmber Data 2.0に向けての変更点についても書かれています。


-----

[JavaScript Scene Tech Survey Results — JavaScript Scene — Medium](https://medium.com/javascript-scene/javascript-scene-tech-survey-d2449a529ed "JavaScript Scene Tech Survey Results — JavaScript Scene — Medium")という記事ではTwitterで[Eric Elliott](https://twitter.com/_ericelliott "Eric Elliott")さんが中心となってJavaScriptについてアンケートを取った結果が公開されています。

![es6 usage](http://monosnap.com/image/gH4VufcCf2VC8KtiXvauSawStslt7X.png)

ES6を使った事があるかや興味のあるES6の機能、興味のあるフレームワークなどについての回答がまとめられています。

若干新しいもの好き、Node.jsユーザが多めで、DailyJSが行っている[JavaScript Developer Survey](http://dailyjs.com/2014/12/16/1333-javascript-survey-results/ "JavaScript Developer Survey")とは回答者の層が少し違う感じがして面白いと思います。

-----

突然の[アンケート](https://azu.typeform.com/to/AGW5qu)です。

<!-- Change the width and height values to suit you best -->
<div class="typeform-widget" data-url="https://azu.typeform.com/to/AGW5qu" data-text="ES6" style="width:100%;height:500px;"></div>
<script>(function(){var qs,js,q,s,d=document,gi=d.getElementById,ce=d.createElement,gt=d.getElementsByTagName,id='typef_orm',b='https://s3-eu-west-1.amazonaws.com/share.typeform.com/';if(!gi.call(d,id)){js=ce.call(d,'script');js.id=id;js.src=b+'widget.js';q=gt.call(d,'script')[0];q.parentNode.insertBefore(js,q)}})()</script>
<div style="font-family: Sans-Serif;font-size: 12px;color: #999;opacity: 0.5; padding-top: 5px;">Powered by <a href="http://www.typeform.com/?utm_campaign=typeform_AGW5qu&amp;utm_source=website&amp;utm_medium=typeform&amp;utm_content=typeform-embedded&amp;utm_term=" style="color: #999" target="_blank">Typeform</a></div>


-----

<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md#550](https://github.com/tmpvar/jsdom/blob/master/Changelog.md#550 "jsdom/Changelog.md at master · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 5.5.0リリース。
postMessageのサポート、`cloneNode`と`importNode`の問題を修正など

----

## flow/Changelog.md at master · facebook/flow
[github.com/facebook/flow/blob/master/Changelog.md#v0131](https://github.com/facebook/flow/blob/master/Changelog.md#v0131 "flow/Changelog.md at master · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Flow v0.13.1リリース。
`flow ast`でESTree ASTを出力するように。class式、binary/octal integer literalのサポートなど

----

## Ember.js - Ember Data v1.13 Released
[emberjs.com/blog/2015/06/18/ember-data-1-13-released.html](http://emberjs.com/blog/2015/06/18/ember-data-1-13-released.html "Ember.js - Ember Data v1.13 Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Ember Data 1.13リリース。
Ember Data初のStableリリースで、バージョンをEmberと合わせてる

----

## ESLint 0.24.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/06/eslint-0.24.0-released](http://eslint.org/blog/2015/06/eslint-0.24.0-released "ESLint 0.24.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.24.0リリース。
ES6 Classesに関するルールの追加など

----

## Vorlon.js 0.0.15 is out ! - Etienne Margraff - Site Home - MSDN Blogs
[blogs.msdn.com/b/emargraff/archive/2015/06/24/vorlon-js-0-0-15-is-out.aspx](http://blogs.msdn.com/b/emargraff/archive/2015/06/24/vorlon-js-0-0-15-is-out.aspx "Vorlon.js 0.0.15 is out ! - Etienne Margraff - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptデバッグツールのVorlon.js 0.0.15リリース。
ネットワークパネル、DOMパネル、プラグイン機能の改善など

----

## Announcing Orion 9.0 | Orion News
[planetorion.org/news/2015/06/language-tooling-goodness-in-orion-9-0/](http://planetorion.org/news/2015/06/language-tooling-goodness-in-orion-9-0/ "Announcing Orion 9.0 | Orion News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">IDE</span> <span class="jser-tag">ReleaseNote</span></p>

Orion 9.0リリース。
Ternをベースとしたコード解析に変更し、コード補完やコードナビゲーション、リファクタリング機能の追加。

- [Eclipse、Webブラウザ上で動作する統合開発環境「Orion 9.0」をリリース：CodeZine](http://codezine.jp/article/detail/8798 "Eclipse、Webブラウザ上で動作する統合開発環境「Orion 9.0」をリリース：CodeZine")

----
<h1 class="site-genre">アーティクル</h1>

----

## ES5 + Facebook JSXで書かれたJavaScriptコードベースをTypeScriptに移行させる - VOYAGE GROUP techlog
[techlog.voyagegroup.com/entry/2015/06/24/170611](http://techlog.voyagegroup.com/entry/2015/06/24/170611 "ES5 + Facebook JSXで書かれたJavaScriptコードベースをTypeScriptに移行させる - VOYAGE GROUP techlog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">React</span></p>

TypeScriptでES6 targetなコードを吐き出し、BabelでES5へ変換するビルドチェインの形成について。
既存プロジェクトの段階的な移行ステップについて。

追記: TypeScriptのmasterブランチにJSXサポートがマージされたので、この辺ももう少し構成が代わって行く可能性はありそうです。

- [JSX and `as` operator by RyanCavanaugh · Pull Request #3564 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/pull/3564 "JSX and `as` operator by RyanCavanaugh · Pull Request #3564 · Microsoft/TypeScript")

----

## JavaScript Scene Tech Survey Results — JavaScript Scene — Medium
[medium.com/javascript-scene/javascript-scene-tech-survey-d2449a529ed](https://medium.com/javascript-scene/javascript-scene-tech-survey-d2449a529ed "JavaScript Scene Tech Survey Results — JavaScript Scene — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Twitterなどで行ったJavaScriptアンケートの結果発表。
Node.jsのユーザーが多めで、ES6を利用したことがある人が半分程度、関心のあるフレームワークなど

----

## Metaprogramming in ES6: Symbols and why they&#x27;re awesome
[blog.keithcirkel.co.uk/metaprogramming-in-es6-symbols/](http://blog.keithcirkel.co.uk/metaprogramming-in-es6-symbols/ "Metaprogramming in ES6: Symbols and why they're awesome")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6とメタプログラミング。
Symbolの使い方。Symbol.hasInstance、Symbol.iterator、Symbol.matchなどそれぞれを定義しておいた時の挙動について書かれてる

----

## JavaScript - Web Audioの新しいAPIについてざっくり解説 - Qiita
[qiita.com/mohayonao/items/ace81c01892321702687](http://qiita.com/mohayonao/items/ace81c01892321702687 "JavaScript - Web Audioの新しいAPIについてざっくり解説 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

新しく増えたWeb Audio APIとそのpolyfillについて

- [mohayonao/web-audio-api-shim](https://github.com/mohayonao/web-audio-api-shim/ "mohayonao/web-audio-api-shim")

----

## A Guide to React.js Tools and Libraries | Toptal
[www.toptal.com/react/navigating-the-react-ecosystem](http://www.toptal.com/react/navigating-the-react-ecosystem "A Guide to React.js Tools and Libraries | Toptal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Reactで見るJavaScriptのエコシステム、ツール、ES6やTranspilerなどについて。
またFluxの実装ライブラリとして[Alt](https://github.com/goatslacker/alt)の紹介やReactの関連ライブラリについてなど幅広く書かれてる

----

## The State of JS Build Tools 2015
[www.walkercoderanger.com/blog/2015/06/state-of-js-build-tools-2015/](http://www.walkercoderanger.com/blog/2015/06/state-of-js-build-tools-2015/ "The State of JS Build Tools 2015")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">まとめ</span></p>

JavaScriptのビルドツールであるGrunt、Gulp、Broccoli、Brunchについて。
それぞれの簡単な紹介と何を基準にこれらのツールを選ぶのかという話

----

## Building Backbone apps using Flux — Medium
[medium.com/@victordoss/building-backbone-apps-using-flux-f656fd8a873a](https://medium.com/@victordoss/building-backbone-apps-using-flux-f656fd8a873a "Building Backbone apps using Flux — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">backbone.js</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Backbone.jsでFlux的なデータの流れにするためにModeをラップしてDispatcherを入れるライブラリについて

----

## Sass - SCSSと付き合う上でやって(知って)よかったこと8選 - Qiita
[qiita.com/suisho/items/e996c42798bbb17add13](http://qiita.com/suisho/items/e996c42798bbb17add13 "Sass - SCSSと付き合う上でやって(知って)よかったこと8選 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Sass</span> <span class="jser-tag">Tools</span> <span class="jser-tag">まとめ</span></p>

Sassに関連するTipsやライブラリ、ツールについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Front End TV - Screencast tutorials for web developers.
[www.frontend.tv/](http://www.frontend.tv/ "Front End TV - Screencast tutorials for web developers.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">動画</span></p>

JavaScriptやCSSや関連するツールなどについて5分程度のスクリーンキャストをやっているサイト

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## HTML5test - How well does your browser support HTML5?
[html5test.com/](https://html5test.com/ "HTML5test - How well does your browser support HTML5?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">HTML5</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

ブラウザの実装してるHTMLやJavaScriptの機能をテストしてスコアを出すサービス

----

## React 0.13 日本語リファレンス | js STUDIO
[js.studio-kingdom.com/react](http://js.studio-kingdom.com/react "React 0.13 日本語リファレンス | js STUDIO")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">リファレンス</span> <span class="jser-tag">翻訳</span></p>

Reactリファレンスの日本語訳

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## timdp/es6-promise-pool
[github.com/timdp/es6-promise-pool](https://github.com/timdp/es6-promise-pool "timdp/es6-promise-pool")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promise.allのように並列に処理を行うが、一度に何個づつやるかを決めて処理できるPromiseの補助ライブラリ

----

## wavesurfer.js
[www.wavesurfer.fm/](http://www.wavesurfer.fm/ "wavesurfer.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

Web Audioの波形をCanvasで描画してくれるライブラリ

----

## karpathy/convnetjs
[github.com/karpathy/convnetjs](https://github.com/karpathy/convnetjs "karpathy/convnetjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptでニューラルネットワークの実装ライブラリ

----
