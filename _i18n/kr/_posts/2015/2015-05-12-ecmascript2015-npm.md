---
title: "2015-05-12 자바스크립트 소식: ECMAScript 2015(ES6) 입문、npm의 최신 변경 사항을 살펴보다"
author: azu
layout: post
date : 2015-05-12T19:21
category: JSer
tags:
    - ES6
    - ECMAScript
    - npm
    - Node.js

---
JSer.info #227 - [Rubyist Magazine - 2015 年の JavaScript と babel の話](http://magazine.rubyist.net/?0050-ECMAScript2015 "Rubyist Magazine - 2015 年の JavaScript と babel の話")という記事では、[Babel](http://babeljs.io/ "Babel")によるtranspileを利用しながらES6で追加された機能や構文について紹介しています。

記事中にも書かれていますが[tower-of-babel](https://github.com/yosuke-furukawa/tower-of-babel "tower-of-babel")というインタラクティブに学べるツールも公開されていて、ES6は[最終ドラフト](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts)がでていて現在進行形で[ブラウザ等で実装が進んでいる](http://kangax.github.io/compat-table/es6/)ので、この機会に学んでみるのもいいと思います。

また、[Hello, ES6 ~これから迎えるJSのミライ~ - @yoshiko_pg](http://yoshiko-pg.github.io/slides/20150425-jsfes/ "Hello, ES6 ~これから迎えるJSのミライ~ - @yoshiko_pg")というスライドでも書かれていますが、最近はES6で書かれた(公開時にBabel等の変換したコードを使う)ライブラリ等も増えてきていてそのサンプルコード等もES6で書かれているケースが増えて来ていると思います。

構文だけではなくて仕様的な話などもっと深く見て行きたい場合は[You Don&#39;t Know JS: ES6 &amp; Beyond](https://github.com/getify/You-Dont-Know-JS/tree/master/es6%20%26%20beyond "You Don&#39;t Know JS: ES6 &amp; Beyond")や[②ality – JavaScript and more](http://www.2ality.com/search/label/esnext "②ality – JavaScript and more")等を見ることをオススメします。


----
[npm update -g npm // Speaker Deck](https://speakerdeck.com/watilde/npm-update-g-npm "npm update -g npm // Speaker Deck")というスライドでは、パッケージ管理ツールであるnpmの最近の変更点や追加された機能などについて紹介されています。

npmは`npm install -g npm`することでNode.jsやio.jsのバージョンとは別でアップデート可能ですが、現在のNode.jsにバンドルされているのはnpm v2.5.1なので、そこからどのような変更があったかについて書かれています。

npmの変更点については[The npm Blog](http://blog.npmjs.org/ "The npm Blog")([翻訳](https://medium.com/@watilde/ "Daijiro Wachi — Medium"))、[GitHubのReleasesページ](https://github.com/npm/npm/releases "Releases · npm/npm")を見ることで細かく見ていくことができると思います。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint 0.21.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/05/eslint-0.21.0-released](http://eslint.org/blog/2015/05/eslint-0.21.0-released "ESLint 0.21.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.21.0リリース。
`eslint --init`で設定ファイルの作成をインタラクティブに行えるように、外部の設定ファイルを継承出来るようになり、また[Shareable Configs](http://eslint.org/docs/developer-guide/shareable-configs "Shareable Configs")というドキュメントが追加された

----

## React v0.13.3 | React
[facebook.github.io/react/blog/2015/05/08/react-v0.13.3.html](https://facebook.github.io/react/blog/2015/05/08/react-v0.13.3.html "React v0.13.3 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.13.3リリース。
ES6 Classesを使った時に非推奨メソッドの警告を改善、
`dangerouslySetInnerHTML`で値がundefinedの時に例外を投げないようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Rubyist Magazine - 2015 年の JavaScript と babel の話
[magazine.rubyist.net/?0050-ECMAScript2015](http://magazine.rubyist.net/?0050-ECMAScript2015 "Rubyist Magazine - 2015 年の JavaScript と babel の話")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6の概要を紹介する記事

- [Hello, ES6 ~これから迎えるJSのミライ~ - @yoshiko_pg](http://yoshiko-pg.github.io/slides/20150425-jsfes/ "Hello, ES6 ~これから迎えるJSのミライ~ - @yoshiko_pg")

----

## Deku: How we built our functional alternative to React
[segment.com/blog/deku-our-functional-alternative-to-react/](https://segment.com/blog/deku-our-functional-alternative-to-react/ "Deku: How we built our functional alternative to React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Virtual DOMを持ち、Reactのようなライフサイクルを持つコンポーネントライブラリ。
ES6 Classesではなくライフサイクルに対応する関数をexportする形式となっていて`this`を気にせず書くことができる。
Babelのオプションを使いJSXで書くこともでき、Node.js上でも動作するためサーバサイドレンダリングが行える。
ファイルサイズが10kb程度。

- [segmentio/deku](https://github.com/segmentio/deku "segmentio/deku")

----

## Milliseconds Matter Modern JavaScript libraries: the isomorphic way
[blog.algolia.com/modern-javascript-libraries-the-isomorphic-way/](https://blog.algolia.com/modern-javascript-libraries-the-isomorphic-way/ "Milliseconds Matter Modern JavaScript libraries: the isomorphic way")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Node.jsとブラウザどちらでも動くライブラリを書いていく記事。
faux-jaxを使ったXHRのテストをzuulで動かす。コールバックとPromiseのサポートについてやBrowserify等を使ったモジュールの変換、後方互換ガイドの書き方についてなど

- [algolia/faux-jax](https://github.com/algolia/faux-jax "algolia/faux-jax")

----

## Immutability in JavaScript
[www.sitepoint.com/immutability-javascript/](http://www.sitepoint.com/immutability-javascript/ "Immutability in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

immutable.jsを使ったJavaScriptでのImmutabilityの実現について。
実行コストはどうなのか、逆にどういう点でコストが小さくなるのか

----

## The Core Concepts of Angular 2 | Victor Savkin
[victorsavkin.com/post/118372404541/the-core-concepts-of-angular-2](http://victorsavkin.com/post/118372404541/the-core-concepts-of-angular-2 "The Core Concepts of Angular 2 | Victor Savkin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">設計</span></p>

AngularJS 2のコアコンセプトについて。
テンプレート、ライフサイクル、DI、コンポーネントなどの構成要素について。

- [angular/zone.js](https://github.com/angular/zone.js "angular/zone.js")

----

## A break from the past, part 2: Saying goodbye to ActiveX, VBScript, attachEvent…
[blogs.windows.com/msedgedev/2015/05/06/a-break-from-the-past-part-2-saying-goodbye-to-activex-vbscript-attachevent/](https://blogs.windows.com/msedgedev/2015/05/06/a-break-from-the-past-part-2-saying-goodbye-to-activex-vbscript-attachevent/ "A break from the past, part 2: Saying goodbye to ActiveX, VBScript, attachEvent…")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">IE</span></p>

MSEdgeで削除されたIE特有の機能などについて。(IEから引き継がなかった機能)
逆に`-webkit-border-radius`のようなものを既存のウェブサイトの互換性のためにサポートしている

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## npm update -g npm // Speaker Deck
[speakerdeck.com/watilde/npm-update-g-npm](https://speakerdeck.com/watilde/npm-update-g-npm "npm update -g npm // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">スライド</span></p>

npmの最近の変更点についてのスライド

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Front-end Dev Weekly JP
[front-end-dev-weekly-jp.github.io/](http://front-end-dev-weekly-jp.github.io/ "Front-end Dev Weekly JP")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">翻訳</span> <span class="jser-tag">blog</span></p>

Front-end Dev Weeklyの翻訳

- [Front-end Dev Weekly](https://frontenddevweekly.curated.co/ "Front-end Dev Weekly")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jQuery - The Write Less, Do More, JavaScript Library
[cyokodog.github.io/JS_STUDY/web-audio/presen/](http://cyokodog.github.io/JS_STUDY/web-audio/presen/ "jQuery - The Write Less, Do More, JavaScript Library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span> <span class="jser-tag">動画</span> <span class="jser-tag">スライド</span></p>

Web Audio API、MediaStream Processing API、Web Speech API、Speech Recognition APIの紹介的なスライド

----

## getify/es-feature-tests
[github.com/getify/es-feature-tests](https://github.com/getify/es-feature-tests "getify/es-feature-tests")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

ECMAScript 6以降の機能についてfeature detectを実行して結果を取得するライブラリ

----

## Challenger.js
[rileyjshaw.com/challenger/](http://rileyjshaw.com/challenger/ "Challenger.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AST</span></p>

練習問題などを作るライブラリ。
期待する結果をコードで書いて検証でき、また入力されるコードをASTのNode名などを使ったwhitelist、blacklist方式で制限できる

----

## nkzawa/hyperd
[github.com/nkzawa/hyperd](https://github.com/nkzawa/hyperd "nkzawa/hyperd")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

virtual-domを使ったUIコンポーネントライブラリ。
html-to-domでHTMLからvirtual-domへの変換をすることで任意のテンプレートエンジンを使える。
また、コンポーネント自体がEventEmitterを継承している。

----
