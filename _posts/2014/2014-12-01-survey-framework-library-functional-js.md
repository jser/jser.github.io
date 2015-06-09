---
title: "2014-12-02のJS: JavaScript開発者アンケート、フレームワーク or ライブラリ、関数型プログラミング"
author: azu
layout: post
date : 2014-12-02T09:47
category: JSer
tags:
    - アンケート
    - Angular
    - JavaScript
    - library

---

JSer.info #204 - 今年も[DailyJSによるJavaScript開発者向けアンケート](http://dailyjs.com/2014/12/01/javascript-survey/ "DailyJS: JavaScript Developer Survey 2014")の受付が開始されました。

[DailyJS: JavaScript Developer Survey 2014](http://dailyjs.com/2014/12/01/javascript-survey/ "DailyJS: JavaScript Developer Survey 2014")からどんなターゲット向けにJavaScriptを書いてるか、使ってるライブラリやテストについて等のアンケートをやっています。

[2010年](http://dailyjs.com/2010/11/29/javascript-survey/ "DailyJS: JavaScript Developer Survey")から継続的に行われているアンケートなので、是非参加しましょう。

----

[The State of JavaScript in 2015 - Jimmy Breck-McKye](http://www.breck-mckye.com/blog/2014/12/the-state-of-javascript-in-2015/ "The State of JavaScript in 2015 - Jimmy Breck-McKye")という記事では、ライブラリとテクノロジーの変化にどう対応していくべきかについて書かれています。

AngularJSやEmberのようなモノリシックなフレームワークではなく、専門の役割を持ったライブラリを使うことで、
レガシーになったプロジェクトに新しいテクノロジーを導入するときも全てを書き換えないでインクリメンタルに変更していける事や、
新しいライブラリやテクノロジーを採用する際に気をつける3つの教訓などの考えが書かれています。

こういうアーキテクチャの再考が最近多いのは、ReactのようなVirtual DOMを持つViewを専門的に扱うライブラリなどがでてきて、
今まではコスト的にひっかかっていたやり方も上手く行くケースが見えてきたのもあるかもしれません。

>  なぜVirtual DOMか -「設計と速度が両立する」
>  via [VirtualDom - なぜ仮想DOMという概念が俺達の魂を震えさせるのか - Qiita](http://qiita.com/mizchi/items/4d25bc26def1719d52e6 "VirtualDom - なぜ仮想DOMという概念が俺達の魂を震えさせるのか - Qiita")

----

[Functional Programming](http://scott.sauyet.com/Javascript/Talk/2014/01/FuncProgTalk/ "Functional Programming")というスライドではJavaScriptにおける関数型プログラミングについて書かれています。

オブジェクト指向的に書いた場合と、関数型的に書いた場合を比較しながら紹介しているため考え方が分かりやすいです。

また、JavaScriptでは末尾呼出し最適化が実装されてない事やパターンマッチ、遅延評価、同図像性（Homoiconicity）など言語的に難しい部分はありますが、関数型プログラミングのアプローチを知る分にはよくまとまっていると思います。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 0.11.1 · yyx990803/vue
[github.com/yyx990803/vue/releases/tag/0.11.1](https://github.com/yyx990803/vue/releases/tag/0.11.1 "Release 0.11.1 · yyx990803/vue")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 0.11.1リリース。

v-componentのスコープの変更、`wait-for`属性で特定のeventがemitされるまで待てるように、`v-style`にdataとしてCSSオブジェクトを渡してスタイルを適応出来るようになるなど

----

## ESLint 0.10.0 released - ESLint
[eslint.org/blog/2014/11/eslint-0.10.0-released/](http://eslint.org/blog/2014/11/eslint-0.10.0-released/ "ESLint 0.10.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.10.0リリース。

CLIがデフォルトでnode_modulesを無視するように、拡張子なしのファイル名のみの指定が可能になり、別途オプションとして拡張子のデフォルト値を設定出来るようになる等

----

## IE Web Development Support Moving to Stack Overflow
[social.msdn.microsoft.com/Forums/ie/en-US/8ba70824-dba2-4425-bc75-247c2c29bde1/action?threadDisplayName=ie&amp;forum=iewebdevelopment](https://social.msdn.microsoft.com/Forums/ie/en-US/8ba70824-dba2-4425-bc75-247c2c29bde1/action?threadDisplayName=ie&amp;forum=iewebdevelopment "IE Web Development Support Moving to Stack Overflow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">IE</span></p>

IEの開発に関する質問サポートはStack Overflowに移行するとの話

----

## DailyJS: JavaScript Developer Survey 2014
[dailyjs.com/2014/12/01/javascript-survey/](http://dailyjs.com/2014/12/01/javascript-survey/ "DailyJS: JavaScript Developer Survey 2014")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

DailyJSのJavaScript開発者アンケート 2014の受付が開始された

----
<h1 class="site-genre">アーティクル</h1>

----

## The State of Flux
[reactjsnews.com/the-state-of-flux/](http://reactjsnews.com/the-state-of-flux/ "The State of Flux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">library</span> <span class="jser-tag">まとめ</span></p>

Fluxアーキテクチャ関連のライブラリのまとめ、それぞれの実装的な特徴

----

## Getting Started with React and JSX
[www.sitepoint.com/getting-started-react-jsx/](http://www.sitepoint.com/getting-started-react-jsx/ "Getting Started with React and JSX")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

Reactのチュートリアル。

props、state、eventと順に紹介してる

----

## フロントエンドエンジニアになってから11ヶ月間で覚えたちょっと捗るChromeの使い方 - Qiita
[qiita.com/dayoshix/items/0d4043bf7dbaa1dc9184](http://qiita.com/dayoshix/items/0d4043bf7dbaa1dc9184 "フロントエンドエンジニアになってから11ヶ月間で覚えたちょっと捗るChromeの使い方 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">tools</span></p>

Chrome開発者ツールのTips。

gifと共に機能を紹介してて分かりやすい

- [Chrome DevTools Overview - Google Chrome](https://developer.chrome.com/devtools "Chrome DevTools Overview - Google Chrome")

----

## The State of JavaScript in 2015 - Jimmy Breck-McKye
[www.breck-mckye.com/blog/2014/12/the-state-of-javascript-in-2015](http://www.breck-mckye.com/blog/2014/12/the-state-of-javascript-in-2015 "The State of JavaScript in 2015 - Jimmy Breck-McKye")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AngularJS</span> <span class="jser-tag">library</span> <span class="jser-tag">thought</span></p>

AngularJS 2.0の発表でJavaScriptについて再考する話。

新しいテクノロジーを扱う時はちゃんと疑問を持って接する事、企業製だからといって信用するのは別問題、モノリシックなフルスタックフレームワークよりも役割が分けられたライブラリを選ぶ。

役割が分けられたライブラリを使う事でレガシーなプロジェクトに新しいテクノロジーを導入するときも全てを書き換えないでインクリメンタルに変更していける。

著名なライブラリがフルスタックなのか、特定の役割だけを持っているかや、
今後どのようにライブラリを選び開発していくかについて。


----

## What&#x27;s in a Function Name? - Bocoup
[bocoup.com/weblog/whats-in-a-function-name/](http://bocoup.com/weblog/whats-in-a-function-name/ "What&#x27;s in a Function Name? - Bocoup")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScriptの関数名について。

関数定義や関数式、即時実行、newの場合、ES6のletやexportなどのそれぞれの場合に"関数名"がどうなるか。

またJSHintによるチェックやデバッグに役立つ`displayName`プロパティについて

----

## Custom Elements - Web Components を構成する技術: Tender Surrender
[blog.agektmr.com/2014/11/custom-elements-web-components.html](http://blog.agektmr.com/2014/11/custom-elements-web-components.html "Custom Elements - Web Components を構成する技術: Tender Surrender")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">動画</span></p>

Custom Elementsについての解説。

Custom Elementsの作り方、仕組み、ライフサイクルコールバック、ユースケースについて

----

## Goodbye, Layout Invalidation: Animating SVGs With CSS Transforms | Charlie Marsh
[www.princeton.edu/~crmarsh/svg-performance/](http://www.princeton.edu/~crmarsh/svg-performance/ "Goodbye, Layout Invalidation: Animating SVGs With CSS Transforms | Charlie Marsh")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">performance</span></p>

動かすSVG要素を分けてCSS transform等を使ってGPUで処理が出来るようにチューニングすることで、60FPSが出るようにパフォーマンス改善をする話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## React Through the Ages // Speaker Deck
[speakerdeck.com/zpao/react-through-the-ages](https://speakerdeck.com/zpao/react-through-the-ages "React Through the Ages // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

Reactの今後についてのスライド。

Reusable ComponentsがFacebookの中には既に10000個ある。

1.0に向けてAPIの安定化/修正、ES6 Classesへの対応、CSS in JS、Web Worker対応、レイアウトやアニメーション等をあげている

- [React: CSS in JS // Speaker Deck](https://speakerdeck.com/vjeux/react-css-in-js "React: CSS in JS // Speaker Deck")

----

## ReactJS: Keep Simple. Everything can be a component! // Speaker Deck
[speakerdeck.com/pedronauck/reactjs-keep-simple-everything-can-be-a-component](https://speakerdeck.com/pedronauck/reactjs-keep-simple-everything-can-be-a-component "ReactJS: Keep Simple. Everything can be a component! // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

Reactの特徴について分かりやすくまとめられているスライド。

Immutable、Virtual DOM、PropとState、DRYにするためのMixin、Isomorphicについて

----

## Functional Programming
[scott.sauyet.com/Javascript/Talk/2014/01/FuncProgTalk/](http://scott.sauyet.com/Javascript/Talk/2014/01/FuncProgTalk/ "Functional Programming")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">スライド</span></p>

関数型プログラミングについてのスライド。

オブジェクト指向との考え方の違い、DeclarativeとImperative、まだJSでは扱えない部分について(末尾最適化等)、具体的にOOPからFPへどう書き換えるかの例等

----
<h1 class="site-genre">サイト、サービス</h1>

----

## ペパボのフロントエンドスタンダード
[pepabo.github.io/docs/frontend/standard.html](http://pepabo.github.io/docs/frontend/standard.html "ペパボのフロントエンドスタンダード")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

ペパボによるエンジニア、デザイナが「最低限これだけはおさえておこう」というスタンダードを文書化したもの。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## decadecity/css-specificity-map
[github.com/decadecity/css-specificity-map](https://github.com/decadecity/css-specificity-map "decadecity/css-specificity-map")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tools</span></p>

CSSの詳細度グラフのデータを作るライブラリ

- [The Specificity Graph – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts](http://csswizardry.com/2014/10/the-specificity-graph/ "The Specificity Graph – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts")
- [CSS specificity graphs | Blog | Decade City](https://decadecity.net/blog/2014/11/26/css-specificity-graphs "CSS specificity graphs | Blog | Decade City")

----

## knsv/mermaid
[github.com/knsv/mermaid](https://github.com/knsv/mermaid "knsv/mermaid")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">図</span> <span class="jser-tag">JavaScript</span></p>

テキストからD3を使ったフローチャートやダイアグラム等の図を作成してくれるライブラリ

----

## krasimir/atomus
[github.com/krasimir/atomus](https://github.com/krasimir/atomus "krasimir/atomus")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Node.js環境でDOMを含めたクライアントサイドのコードをテストするライブラリ。

jsdomを使っていて、テストを実行する場所となるHTMLを渡して、クリックなどのイベントを起こしてテスト出来る

----

## serratus/quaggaJS
[github.com/serratus/quaggaJS](https://github.com/serratus/quaggaJS "serratus/quaggaJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptで書かれたバーコードリーダライブラリ。getUserMediaを使ってリアルタイムに処理したり、画像から検出したりできる

----

## Handsontable - JavaScript data grid editor. Excel-like grid editing with HTML &amp; JavaScript
[handsontable.com/](http://handsontable.com/ "Handsontable - JavaScript data grid editor. Excel-like grid editing with HTML &amp; JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Excelライクなデータグリッドエディタ。

依存するライブラリなしで利用できる

----
<h1 class="site-genre">書籍関係</h1>

----

## Introduction | Full Stack JavaScript Engineering
[fsje.codefellows.org/](http://fsje.codefellows.org/ "Introduction | Full Stack JavaScript Engineering")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">Sass</span></p>

フロントエンド全般についての知識について書かれたGitBookを使った電子書籍

----

## Amazon: 改訂版 Webデザイナーのための jQuery入門: 髙津戸 壮, 小原 司
[www.amazon.co.jp/dp/4774169447?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4774169447?tag=amazon0abac-22 "Amazon: 改訂版 Webデザイナーのための jQuery入門: 髙津戸 壮, 小原 司")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">book</span></p>

「WebデザイナーのためのjQuery入門」の改訂版

- [改訂版 WebデザイナーのためのjQuery入門 - Takazudo hamalog](http://hamalog.tumblr.com/post/104081966956/web-jquery "改訂版 WebデザイナーのためのjQuery入門 - Takazudo hamalog")

----

