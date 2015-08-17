---
title: "2015-08-17のJS: redux 1.0.0、flux-utils、Firefox 40"
author: azu
layout: post
date : 2015-08-17T20:21
category: JSer
tags:
    - flux
    - library
    - firefox

---

JSer.info #241 - Fluxのように単方向データの流れを行うフレームワークである[Redux](https://github.com/rackt/redux "Redux") 1.0.0がリリースされました。

- [Release v1.0.0 · rackt/redux](https://github.com/rackt/redux/releases/tag/v1.0.0 "Release v1.0.0 · rackt/redux")

Reduxのコンセプトについては作者が以前[The Evolution of Flux Frameworks — Medium](https://medium.com/@dan_abramov/the-evolution-of-flux-frameworks-6c16ad26bb31 "The Evolution of Flux Frameworks — Medium")という記事で書いています。

ざっくり書くと、Stateを管理するコンテナ(reduxオブジェクト)を提供することでFluxのActionCreatorとStoreにあたるものをただの関数として書けるようにして、状態の変化が予測できるようにすることを目的としています。

ドキュメントや[人気のFluxフレームワークReduxをさわってみた - マルシテイアは月の上](http://amagitakayosi.hatenablog.com/entry/2015/07/30/000000 "人気のFluxフレームワークReduxをさわってみた - マルシテイアは月の上")などを見てみると特徴や、どういう制約を元に作られているかのが分かるかもしれません。

- [Read Me | Redux](http://rackt.github.io/redux/ "Read Me | Redux")
- [Three Principles | Redux](http://rackt.github.io/redux/docs/introduction/ThreePrinciples.html "Three Principles | Redux")

また同時期に、今まで他のFluxフレームワークのようにStoreやActionCreatorに関する機能を提供してなかった[facebook/flux](https://github.com/facebook/flux "facebook/flux")に[Flux Utils](https://github.com/facebook/flux/blob/master/docs/Flux-Utils.md "Flux Utils")という形でそれらの機能が提供されるようになりました。

以下に簡単にどういう機能が提供されているかについてまとめてあります。

- [flux-utilsについて](https://gist.github.com/azu/e0274b703ef97226b0db "flux-utilsについて")

[Immutable.js](https://facebook.github.io/immutable-js/ "Immutable.js")を使っているなどの特徴もありますが、その中でも`ReduceStore`のstateを受け取り変更したstateを返す`reduce`メソッドが副作用のないただの関数であるべきと書かれているように、reduxと似た概念を提供していることがわかります。

> This method should be pure and have no side-effects.

これらは互いに影響受けているようなきがするので、[redux作者](https://twitter.com/dan_abramov)と[flux作者](https://twitter.com/fisherwebdev)の会話を見てみると面白いかもしれません。

- [Combining Stateless Stores](https://gist.github.com/gaearon/d77ca812015c0356654f "Combining Stateless Stores")

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/fisherwebdev">@fisherwebdev</a> <a href="https://twitter.com/goatslacker">@goatslacker</a> <a href="https://twitter.com/alexeyraspopov">@alexeyraspopov</a> Also, with Store-is-function pattern, you can easily keep modularity by delegating to &quot;substores&quot;</p>&mdash; Dan Abramov (@dan_abramov) <a href="https://twitter.com/dan_abramov/status/606155287024795648">June 3, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


----

[Firefox 40](http://www.mozilla.jp/firefox/40.0/releasenotes/ "Firefox 40")がリリースされました。

開発者ツールのPerformanceツールが改善され、[Waterfall](https://developer.mozilla.org/en-US/docs/Tools/Performance/Waterfall) view、[Call Tree](https://developer.mozilla.org/en-US/docs/Tools/Performance/Call_Tree) view、[Flame Chart](https://developer.mozilla.org/en-US/docs/Tools/Performance/Flame_Chart) viewなどに対応しています。

- [New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/ "New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog")
- [Firefox 40 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/40 "Firefox 40 for developers - Mozilla | MDN")

また同時に[延長サポート版 (ESR)](http://www.mozilla.jp/firefox/38.2.0/releasenotes/ "延長サポート版 (ESR)")としてFirefox 38.2.0がリリースされています

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.0.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v1.0.0](https://github.com/rackt/redux/releases/tag/v1.0.0 "Release v1.0.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 1.0.0リリース。
Stateを管理するコンテナを提供することでFluxのActionCreatorとStoreにあたるものをただの関数として書けるようにし、単方向データの流れを行うライブラリ。

----

## 1.1 Release
[blog.polymer-project.org/announcements/2015/08/13/1.1-release/](http://blog.polymer-project.org/announcements/2015/08/13/1.1-release/ "1.1 Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 1.1リリース。
コンポーネントとグローバルスコープでStyleを共有する仕組みの追加など

- [Polymer 1.1 リリース - Qiita](http://qiita.com/laco0416/items/51a3f7863602c1d35e8a "Polymer 1.1 リリース - Qiita")

----

## MozillaZine.jp » Blog Archive » Firefox 40 がリリースされた
[mozillazine.jp/?p=4868](http://mozillazine.jp/?p=4868 "MozillaZine.jp » Blog Archive » Firefox 40 がリリースされた")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 40リリース。
`return`に書かれた到達できないコードへの警告がコンソールへ出るように開発者ツールの改善、Web Audio APIの仕様追従、Web Animations APIの仕様追従など

- [Firefox 40 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/40/Site_Compatibility "Firefox 40 サイト互換性情報 - Mozilla | MDN")
- [Firefox 40 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/40 "Firefox 40 for developers - Mozilla | MDN")

----
<h1 class="site-genre">アーティクル</h1>

----

## 4.0 is the new 1.0 — Node &amp; JavaScript — Medium
[medium.com/node-js-javascript/4-0-is-the-new-1-0-386597a3436d](https://medium.com/node-js-javascript/4-0-is-the-new-1-0-386597a3436d "4.0 is the new 1.0 — Node & JavaScript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">歴史</span></p>

Node.js 4.0がio.jsとのマージが完了したバージョンとしてリリースされる予定。

----

## Browserify dependencies in depth! | TEJI TECH BLOG
[www.tejitak.com/blog/?p=1468](http://www.tejitak.com/blog/?p=1468 "Browserify dependencies in depth! | TEJI TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span></p>

Browserifyでの依存関係の解決パターンについて。
依存するモジュールのバージョンが複数ある場合の問題についての色々なアプローチ

----

## ES6 In Depth: Modules ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/08/es6-in-depth-modules/](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/ "ES6 In Depth: Modules ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 modulesのimport/exportの多様な構文のそれぞれの動作についての解説。
Moduleの仕様を分解してみた時にLoadingについてはECMAScriptでは未定義であること、構文的にstaticであることなどについて書かれている

----

## es6-coding-style/es6-coding-style-en.md at master · gf-web/es6-coding-style
[github.com/gf-web/es6-coding-style/blob/master/es6-coding-style-en.md](https://github.com/gf-web/es6-coding-style/blob/master/es6-coding-style-en.md "es6-coding-style/es6-coding-style-en.md at master · gf-web/es6-coding-style")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6コーディングスタイルガイド。
Destructuringの使いすぎへの注意、ES5での書き方をES6の機能でキレイに書けるケースについて比較、moduleの`*`や`as`について書かれている。

----

## flux-utilsについて
[gist.github.com/azu/e0274b703ef97226b0db](https://gist.github.com/azu/e0274b703ef97226b0db "flux-utilsについて")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

Facebookのfluxモジュールに追加されたutilsについて。
今まではDispatcherのみだったがStoreやReact Componentと連携するためのContainerなどが提供されたことについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## フロントエンドMVCとFlux // Speaker Deck
[speakerdeck.com/sangotaro/hurontoendomvctoflux](https://speakerdeck.com/sangotaro/hurontoendomvctoflux "フロントエンドMVCとFlux // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">スライド</span></p>

Fluxとはどういうものなのかについてのスライド。
MVCと何が違って何が違わないのかがわかりやすく書かれている。

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## mdast - markdown processor powered by plug-ins
[mdast.js.org/](http://mdast.js.org/ "mdast - markdown processor powered by plug-ins")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Markdownパーサであるmdastのサイト。
プラグインを使ってMarkdownからHTMLへの変換、Lintなど様々なことができる

----

## Perf.Rocks
[perf.rocks/](http://perf.rocks/ "Perf.Rocks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">まとめ</span></p>

ウェブパフォーマンスについての記事やツール、人、スライド、動画、書籍などについてのまとめ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Relay | A JavaScript framework for building data-driven React applications
[facebook.github.io/relay/](https://facebook.github.io/relay/ "Relay | A JavaScript framework for building data-driven React applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">facebook</span></p>

GraphQLを使ったデータのやりとりをするフレームワーク。
Relay.QLなどES6 template literalが前提になった作りになっていて面白い。

- [Relay Technical Preview | React](https://facebook.github.io/react/blog/2015/08/11/relay-technical-preview.html "Relay Technical Preview | React")

----

## patrick-steele-idem/morphdom
[github.com/patrick-steele-idem/morphdom](https://github.com/patrick-steele-idem/morphdom "patrick-steele-idem/morphdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

Virutal DOMではなくDOMを使ってdiff/patchをしてDOM Nodeを置き換えるライブラリ。
`virtual-dom`と比較したベンチマークも書かれている。

----

## jamesshore/quixote
[github.com/jamesshore/quixote](https://github.com/jamesshore/quixote "jamesshore/quixote")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

mochaなどと組み合わせて使えるCSSのユニットテスト向けのassertionライブラリ

----

## scottcorgan/immu
[github.com/scottcorgan/immu](https://github.com/scottcorgan/immu "scottcorgan/immu")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable Objectを扱うライブラリ。
Object.definePropertyやObject.freezeを使ってArrayやObjectの変更を防止したオブジェクトを作成する

----
<h1 class="site-genre">書籍関係</h1>

----

## Designing for Performance by Lara Callender Hogan
[designingforperformance.com/](http://designingforperformance.com/ "Designing for Performance by Lara Callender Hogan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

ブラウザのパフォーマンスについての書籍。

----
