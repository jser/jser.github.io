---
title: "2015-02-23のJS: Underscore.js 1.8.0、CodeMirror 5.0、Web Audio入門"
author: azu
layout: post
date : 2015-02-23T22:21
category: JSer
tags:
    - JavaScript
    - library
    - Editor
    - WebAudio

---

JSer.info #216 - [Underscore.js](http://underscorejs.org/#changelog "Underscore.js") 1.8.0がリリースされています。

ユーザー

1.8.0ではファイルサイズの削減を目的としたコミットによりIE8の互換性がなくなる問題がありましたが、1.8.1と1.8.2で一部修正されています。また1.8.0では`_.isError`や`_.mapObject`などいくつかメソッドが追加されています。

- [http://underscorejs.org/#changelog](http://underscorejs.org/#changelog)
- [Go on a Diet · Issue #2060 · jashkenas/underscore](https://github.com/jashkenas/underscore/issues/2060 "Go on a Diet · Issue #2060 · jashkenas/underscore")

リリース直前に1.8.0に入る予定だったメソッド名の一部が変更されているので、masterを直接使っていた場合には注意が必要です。

- [Discuss latest changes to master before releasing · Issue #2061 · jashkenas/underscore](https://github.com/jashkenas/underscore/issues/2061 "Discuss latest changes to master before releasing · Issue #2061 · jashkenas/underscore")

1.8.0のリリースにおいて[色々](https://twitter.com/jdalton/status/568568521602412546)と[問題](https://github.com/jashkenas/underscore/issues/2061)が[あり](https://gitter.im/jashkenas/underscore)ま[した](https://github.com/jashkenas/underscore/issues/2062)が、とりあえず普通のユーザーに与える影響は`_.matches`のリネーム以外は大体修正されたように見えます。

[2014-09-01のJS: Underscore 1.7.0、Browserify入門、Gravit - JSer.info](http://jser.info/2014/09/01/underscore-browserify-Gravit/ "2014-09-01のJS: Underscore 1.7.0、Browserify入門、Gravit - JSer.info")で書いていましたがunderscore.jsをアップデートする際には気をつけたほうがいいと思います。

-----

CodeMirror 4.13と5.0がリリースされました。

- [New releases 4.13 and 5.0 - discuss.CodeMirror](http://discuss.codemirror.net/t/new-releases-4-13-and-5-0/163 "New releases 4.13 and 5.0 - discuss.CodeMirror")

CodeMirror 5.0では`contentEditable`を使って、iOSなど今まで表示のみに近かったモバイル端末等のサポートを開始しました。

<blockquote class="twitter-tweet" lang="en"><p>CodeMirror 5.0のモバイル対応すげー… <a href="http://t.co/4VnAoESxVM">pic.twitter.com/4VnAoESxVM</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/569852054367129601">February 23, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

まだ状況によって上手く行ってない気がしますが、[JavaScript Promiseの本](http://azu.github.io/promises-book/ "JavaScript Promiseの本")のCodeMirrorを5.0にアップデートしてあるので、試してみるといいかもしれません。


-----

[HTML5で音を扱う3つの方法](http://150217-html5sound.fnobi.com/ "HTML5で音を扱う3つの方法")というスライドでは、JavaScriptから音を扱う方法としてAudio要素、Web Audio API、MediaStream Processing APIについて簡単に紹介されています。

また、音を扱う場合に中心となるWeb Audio APIについては[音を扱うJavaScriptライブラリや記事 - Qiita](http://qiita.com/mohayonao/items/d79e9fc56b4e9c157be1 "音を扱うJavaScriptライブラリや記事 - Qiita")という記事でどこを参照したらいいかがまとまっていて、これから始めるにあたってアタリが付けやすいと思います。

自分も[JavaScriptとWeb Audio事始め](http://azu.github.io/slide/webaudioapi/web-audio.html "JavaScriptとWeb Audio事始め")という簡単に触ってみて引っかかりそうな点などについてまとめてたスライドを作りました。

<div class="kwout" style="text-align: center;"><a href="http://azu.github.io/slide/webaudioapi/web-audio.html"><img src="http://kwout.com/cutout/s/a8/48/pmv_bor.jpg" alt="http://azu.github.io/slide/webaudioapi/web-audio.html" title="JavaScriptとWeb Audio事始め" width="600" height="232" style="border: none;" /></a><p style="margin-top: 10px; text-align: center;"><a href="http://azu.github.io/slide/webaudioapi/web-audio.html">JavaScriptとWeb Audio事始め</a> via <a href="http://kwout.com/quote/sa848pmv">kwout</a></p></div>

Web Audio APIはAudioNodeが基本的に使い捨てであったり、`setTimeout`などより[正確なスケジューリング](http://www.html5rocks.com/ja/tutorials/audio/scheduling/ "正確なスケジューリング")を行う方法が用意されていたりして、DOM TreeのAPIなどとは少し違うパラダイムを持っていて一度触ってみると面白いと思います。


-----

<h1 class="site-genre">ヘッドライン</h1>

----

## Underscore.js
[underscorejs.org/](http://underscorejs.org/ "Underscore.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Underscore.js 1.8.0(現在1.8.2まで出てる)リリース。
ファイルサイズの削減、エイリアスとして使われていたメソッド名を一部変更、削除などのBreaking Changeを含んでいる。
詳しくは下記のIssueを参照。
1.8.0はIE8との互換性がないので、1.8.1と1.8.2で互換性の修正が行われている。

- [Discuss latest changes to master before releasing · Issue #2061 · jashkenas/underscore](https://github.com/jashkenas/underscore/issues/2061 "Discuss latest changes to master before releasing · Issue #2061 · jashkenas/underscore")

----

## ESLint 0.15.0 released - ESLint
[eslint.org/blog/2015/02/eslint-0.15.0-released/](http://eslint.org/blog/2015/02/eslint-0.15.0-released/ "ESLint 0.15.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

ESLint 0.15.0リリース。
Spread operator、Rest parameters、Destructuringのサポート。
ES6についてはESTreeでASTの仕様の議論をしてるので、それに従う形で実装を進めて行く

- [estree/estree](https://github.com/estree/estree/ "estree/estree")

----

## node-browserify/changelog.markdown at 9.0.3 · substack/node-browserify
[github.com/substack/node-browserify/blob/9.0.3/changelog.markdown](https://github.com/substack/node-browserify/blob/9.0.3/changelog.markdown "node-browserify/changelog.markdown at 9.0.3 · substack/node-browserify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 9.0.0リリース。
umd 3.0.0へのアップデート。`$`や`_`もモジュール名として利用できるようになったため`--standalone $foo_bar`のような指定をした時の挙動がBreaking Changeとなる

- [umd/HISTORY.md at 3.0.0 · ForbesLindesay/umd](https://github.com/ForbesLindesay/umd/blob/3.0.0/HISTORY.md "umd/HISTORY.md at 3.0.0 · ForbesLindesay/umd")

----

## jsdom/Changelog.md at 4.0.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/4.0.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/4.0.0/Changelog.md "jsdom/Changelog.md at 4.0.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

jsdom 4.0.0リリース。
io.jsの新しいvmモジュールに依存するため、4.xはio.jsでの動作のみで、Node.jsの場合は3.xを使うように推奨されてる。

----

## Wallaby.js hits version 1.0 · Artem Govorov
[dm.gl/2015/02/23/wallaby-version-one/](http://dm.gl/2015/02/23/wallaby-version-one/ "Wallaby.js hits version 1.0 · Artem Govorov")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">plugin</span> <span class="jser-tag">testing</span></p>

JetBrains IDEのpluginとして動作するテストフレームワークwallaby.js 1.0リリース。
今後は他のエディタサポートやAPIの公開、AltJSのサポートなどを予定している。

----

## New releases 4.13 and 5.0 - discuss.CodeMirror
[discuss.codemirror.net/t/new-releases-4-13-and-5-0/163](http://discuss.codemirror.net/t/new-releases-4-13-and-5-0/163 "New releases 4.13 and 5.0 - discuss.CodeMirror")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CodeMirror 4.13と5.0リリース。
5.0ではcontentEditableを使ったモバイルブラウザのサポートが追加されてる

----

## Knockout.js 3.3 Released - Knock Me Out
[www.knockmeout.net/2015/02/knockout-3-3-released.html](http://www.knockmeout.net/2015/02/knockout-3-3-released.html "Knockout.js 3.3 Released - Knock Me Out")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout.js 3.3リリース。
Componentsの値を変更した時のレンダリングを同期か非同期の設定が可能に、`$component`の追加、computesが"awake"と"sleep"のイベントを通知するように

- [Release Version 3.3.0 · knockout/knockout](https://github.com/knockout/knockout/releases/tag/v3.3.0 "Release Version 3.3.0 · knockout/knockout")

----

## rev9-ecma-402-draft-now-available
[esdiscuss.org/topic/rev9-ecma-402-draft-now-available](https://esdiscuss.org/topic/rev9-ecma-402-draft-now-available "rev9-ecma-402-draft-now-available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ecma</span> <span class="jser-tag">spec</span> <span class="jser-tag">i18n</span></p>

ECMA-402(ECMA i18n API) 2.0ドラフト Rev 9リリース

----

## harmony:specification_drafts [ES Wiki]
[wiki.ecmascript.org/doku.php?id=harmony:specification\_drafts#february\_20\_2015\_rev\_34\_release\_candidate\_1](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#february_20_2015_rev_34_release_candidate_1 "harmony:specification_drafts [ES Wiki]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ES6 Draft RC1リリース(Rev 34)

----

## Release 0.7.0 · airportyh/testem
[github.com/airportyh/testem/releases/tag/v0.7.0](https://github.com/airportyh/testem/releases/tag/v0.7.0 "Release 0.7.0 · airportyh/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

testem 0.7.0リリース。
io.jsやNode.js 0.12のサポート、Windowsでもci-modeが動くように修正、実行ページをよりisolateに

----
<h1 class="site-genre">アーティクル</h1>

----

## Flow | Flow Comments
[flowtype.org/blog/2015/02/20/Flow-Comments.html](http://flowtype.org/blog/2015/02/20/Flow-Comments.html "Flow | Flow Comments")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.4.0でコメントによる型指定が追加された。
https://github.com/jareware/flotate のプロジェクトのシンタックスがマージされた形

----

## Classes in ECMAScript 6 (final semantics)
[www.2ality.com/2015/02/es6-classes-final.html](http://www.2ality.com/2015/02/es6-classes-final.html "Classes in ECMAScript 6 (final semantics)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Classesについての詳しい解説。
Classの挙動、使い方、Iterator、継承、`super()`、`new.target`の値、ES5では無理だったビルトインコンストラクタのサブクラスが可能になる点などについて

----

## 音を扱うJavaScriptライブラリや記事 - Qiita
[qiita.com/mohayonao/items/d79e9fc56b4e9c157be1](http://qiita.com/mohayonao/items/d79e9fc56b4e9c157be1 "音を扱うJavaScriptライブラリや記事 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span> <span class="jser-tag">まとめ</span></p>

Web Audio API関連のライブラリやpolyfill、fallback実装などのリソースまとめ

----

## React Tips and Best Practices - ÆFLASH
[aeflash.com/2015-02/react-tips-and-best-practices.html](http://aeflash.com/2015-02/react-tips-and-best-practices.html "React Tips and Best Practices - ÆFLASH")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tips</span></p>

ReactのTips。
`shouldComponentUpdate`とMixin、propTypesとプロダクション、component内のstateを避けて全体のデータフローを一方通行にする話など

----

## The npm Blog — Welcome, jQuery developers!
[blog.npmjs.org/post/111385956875/welcome-jquery-developers](http://blog.npmjs.org/post/111385956875/welcome-jquery-developers "The npm Blog — Welcome, jQuery developers!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">npm</span></p>

jQuery plugin registryはread onlyモードとなり、pluginの公開にnpmを推奨してるのを受けて、jQuery pluginをnpmで公開する方法についてのサポートをしていくとの事

- [【翻訳】Welcome, jQuery developers! — Medium](https://medium.com/@watilde/%E7%BF%BB%E8%A8%B3-welcome-jquery-developers-3ae0075c19f6 "【翻訳】Welcome, jQuery developers! — Medium")
- [【翻訳】Publishing your jQuery plugin to npm, the quick and dirty way — Medium](https://medium.com/@watilde/%E7%BF%BB%E8%A8%B3-publishing-your-jquery-plugin-to-npm-the-quick-and-dirty-way-8487344e2b3f "【翻訳】Publishing your jQuery plugin to npm, the quick and dirty way — Medium")

----

## JSX - ESLintについての細かいあれこれ - Qiita
[qiita.com/suisho/items/8610d3806a3f94d7d1d0](http://qiita.com/suisho/items/8610d3806a3f94d7d1d0 "JSX - ESLintについての細かいあれこれ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLintの設定について

----

## JavaScript - ぼくのかんがえたさいきょうのES6プロジェクトテンプレート - Qiita
[qiita.com/mohayonao/items/9b0655b8b4979bffda31](http://qiita.com/mohayonao/items/9b0655b8b4979bffda31 "JavaScript - ぼくのかんがえたさいきょうのES6プロジェクトテンプレート - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6でのプロジェクト構成について。
ビルド、npm run-script、Browserify、テスト、Lint、コードカバレッジなどの設定について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## HTML5で音を扱う3つの方法
[150217-html5sound.fnobi.com/](http://150217-html5sound.fnobi.com/ "HTML5で音を扱う3つの方法")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">audio</span> <span class="jser-tag">API</span> <span class="jser-tag">スライド</span></p>

Audioタグ、Web Audio API、MediaStream Processing APIについてのスライド。
それぞれがどのような用途や機能を持っているかについて書かれている

----

## Reactive Programming in JavaScript
[ahomu.github.io/s/150221-frontrend_conference/index.html#1](http://ahomu.github.io/s/150221-frontrend_conference/index.html#1 "Reactive Programming in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">スライド</span></p>

Reactiveプログラミングについてのスライド。"Reactive = 片方の変化を他方に自動で伝播する仕組み"
Actor、FRP等Reactiveは色々あるがFRPについて詳しく書かれている。
RxJSやBacon.jsを使ったサンプルについて

- [Reactive Programming in JavaScript - Frontrend Final Conference 資料 ::ハブろぐ](http://havelog.ayumusato.com/develop/javascript/e657-reactive_programming_in_javascript.html "Reactive Programming in JavaScript - Frontrend Final Conference 資料 ::ハブろぐ")

----

## Introduction to Service Worker // Speaker Deck
[speakerdeck.com/1000ch/introduction-to-service-worker](https://speakerdeck.com/1000ch/introduction-to-service-worker "Introduction to Service Worker // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">スライド</span></p>

オフラインを実現するために関連するAPI、主にService Workerについてのスライド。
Cache API、Push APIについて解説されている。

----

## Introduction To React // Speaker Deck
[speakerdeck.com/hokaccha/introduction-to-react](https://speakerdeck.com/hokaccha/introduction-to-react "Introduction To React // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

既存のDOMの再描画の流れとReactでのUI再描画の仕組みの違いについて。
再描画のコストの違いや設計への影響、Fluxアーキテクチャへの流れが分かりやすく書かれているスライド

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Eric Elliott’s essential JavaScript links or The way of the parrot, not · Super-Script
[super-script.us/2015/essential-js-links.html](http://super-script.us/2015/essential-js-links.html "Eric Elliott’s essential JavaScript links or The way of the parrot, not · Super-Script")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">links</span></p>

JavaScriptについてのリソースリンク集。
スクリーンショット付きで紹介してる

----

## mking/react-hn
[github.com/mking/react-hn](https://github.com/mking/react-hn "mking/react-hn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サンプル</span> <span class="jser-tag">tutorial</span></p>

Reactを使ったHackerNewsのクローン。
どういうComponentの粒度になってるかや構造についての解説が書かれている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mzabriskie/axios
[github.com/mzabriskie/axios](https://github.com/mzabriskie/axios "mzabriskie/axios")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">XHR</span></p>

Node.js/ブラウザどちらでも動くPromiseベースのHTTPリクエストライブラリ。
リクエスト/レスポンスに対してコールバックを呼ばれる前に処理を挟んだりすることも出来る

----

## yahoo/preceptor
[github.com/yahoo/preceptor](https://github.com/yahoo/preceptor "yahoo/preceptor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Mocha、Cucumberなどに対応したTest Runner。
設定によりレポーターやテスト対象などを細かく設定することができ、何をテストするかはTaskという塊で定義でき、Taskを並列で動かすこともできる。

----

## yahoo/kobold
[github.com/yahoo/kobold](https://github.com/yahoo/kobold "yahoo/kobold")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">testing</span></p>

スクリーンショットを比較して視覚的なレグレッションがないかをテストするコマンドラインツール

----

## hughsk/disc
[github.com/hughsk/disc](https://github.com/hughsk/disc "hughsk/disc")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">Tools</span> <span class="jser-tag">gurai</span></p>

Browserifyでビルドしたコードから、ディレクトリ別(モジュール別)でファイルサイズやファイル数をグラフで可視化してくれるツール

----

## gabelerner/canvg
[github.com/gabelerner/canvg](https://github.com/gabelerner/canvg "gabelerner/canvg")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">canvas</span></p>

SVGをCanvasでレンダリングするライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: コーディングWebアクセシビリティ - WAI-ARIAで実現するマルチデバイス環境のWebアプリケーション: ヘイドン・ピカリング, Heydon Pickering, 伊原力也, 太田良典, 株式会社Bスプラウト
[www.amazon.co.jp/dp/4862462669?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4862462669?tag=amazon0abac-22 "Amazon: コーディングWebアクセシビリティ - WAI-ARIAで実現するマルチデバイス環境のWebアプリケーション: ヘイドン・ピカリング, Heydon Pickering, 伊原力也, 太田良典, 株式会社Bスプラウト")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">book</span> <span class="jser-tag">翻訳</span></p>

2015年3月30日発売
"Apps For All - Coding Accessible Web Applications"の日本語版

----

## The Pragmatic Bookshelf | CoffeeScript
[pragprog.com/book/tbcoffee2/coffeescript](https://pragprog.com/book/tbcoffee2/coffeescript "The Pragmatic Bookshelf | CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">book</span></p>

CoffeeScriptについての書籍

----
