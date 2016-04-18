---
title: "2016-04-18のJS: JSCS 3.0とESLintへのマージ、SVG アイコン"
author: azu
layout: post
date : 2016-04-18T19:42
category: JSer
tags:
    - JSCS
    - ESLint
    - SVG
    - CSS

---

JSer.info #275 - JavaScriptのコードスタイルチェッカーであるJSCS 3.0がリリースされました。

- [Release 3.0.0 · jscs-dev/node-jscs](https://github.com/jscs-dev/node-jscs/releases/tag/v3.0.0 "Release 3.0.0 · jscs-dev/node-jscs")

プラグイン開発者向けの非互換性がありますが、他は`yandex` presetの削除、ルールの追加となっています。

また、JSCSは3.xで新規開発が終了し、JSCSチームはESLintチームに入るようです。

- [JSCS — end of the line — Medium](https://medium.com/@markelog/jscs-end-of-the-line-bc9bf0b3fdb2)
- [Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")

今後三ヶ月を目処にJSCSのバグ修正なども終了し、その間に、[ESLintにはJSCS互換/移行のサポート](https://github.com/eslint/eslint/milestones/JSCS%20Compatibility)を用意していく予定となっています。
(そのため、JSCSからESLintに移行する場合は少し待ったほうがいいかもしれません)

JSCSチームがESLintに入った理由として、コミュニティ/Issueの管理コストや[CST](https://github.com/cst/cst "CST")の開発に注力したかったなどが挙げられています。

- [JSCS, CST и новое начало / Хабрахабр](https://habrahabr.ru/post/281635/ "JSCS, CST и новое начало / Хабрахабр")

また、同じ問題を解決するツールであったり、ESLintが今後AutoFix機能を改善していきたいというのも一つの理由なのかもしれません。

- [Fixing autofix · Issue #5329 · eslint/eslint](https://github.com/eslint/eslint/issues/5329 "Fixing autofix · Issue #5329 · eslint/eslint")


-----

[How to work with SVG icons](http://fvsch.com/code/svg-icons/how-to/ "How to work with SVG icons")という記事ではSVGアイコンについてかなり詳しく解説されています。

SVG spriteの仕組みや作り方、ブラウザ間の動作の違い、CSSからSVGのスタイルを変更する方法など実践的な内容が書かれていて面白いです。
また、インラインSVGと外部リソースのSVGの動作の違いやブラウザの挙動など、実際に使うとハマるであろう部分も補完されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 2 | WebKit
[webkit.org/blog/6098/release-notes-for-safari-technology-preview-release-2/](https://webkit.org/blog/6098/release-notes-for-safari-technology-preview-release-2/ "Release Notes for Safari Technology Preview 2 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 2リリース。
`String#padStart`/`String#padEnd`/の追加、`for (var i = 20 in b){ }`がエラーとなるように。
CSS media queryで`color-gamut`の対応、TP1で間違って公開されてたFetch APIをデフォルトでは無効に、Web Inspectorの改善など

----

## ESLint v2.8.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/04/eslint-v2.8.0-released](http://eslint.org/blog/2016/04/eslint-v2.8.0-released "ESLint v2.8.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.8.0リリース。

- [ESLint v2.8.0 - Qiita](http://qiita.com/mysticatea/items/8e7ca6f6ae402a494a6b "ESLint v2.8.0 - Qiita")

----

## Release 3.0.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v3.0.0](https://github.com/jscs-dev/node-jscs/releases/tag/v3.0.0 "Release 3.0.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS 3.0.0リリース。

----

## Jest 11.0 · Jest
[facebook.github.io/jest/blog/2016/04/12/jest-11.html](http://facebook.github.io/jest/blog/2016/04/12/jest-11.html "Jest 11.0 · Jest")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 11.0リリース。
0.10から11.0へのメジャーアップデート

----

## Release v0.23.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.23.0](https://github.com/facebook/flow/releases/tag/v0.23.0 "Release v0.23.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow v0.23.0リリース。
`flow init`で`.flowconfig`を作る時のオプション追加やコメントを書けるようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/04/welcoming-jscs-to-eslint](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ESLint</span></p>

JSCS 3.0.0で新規開発は終了し、3ヶ月を目処にサポートも終了する。
JSCSチームはESLintに入り、ESLintのAutofixを動かすためにも必要なCSTの開発を行う。
ESLint側はJSCSからの移行/互換のサポートを予定している。

- [Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")
- [JSCS, CST и новое начало / Хабрахабр](https://habrahabr.ru/post/281635/ "JSCS, CST и новое начало / Хабрахабр")

----

## How to work with SVG icons
[fvsch.com/code/svg-icons/how-to/](http://fvsch.com/code/svg-icons/how-to/ "How to work with SVG icons")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">画像</span></p>

SVGアイコンについての実践的な解説。
CSSスプライトのようにSVGスプライトを使う方法、インラインSVGと外部SVGを読み込み違いや対応ブラウザ/polyfillについてなど。
またCSSからSVGのスタイルを変更する方法やSafariの問題などかなり詳細にまとまっている

----

## CSS @apply rule (native CSS mixins)
[blog.gospodarets.com/css\_apply\_rule](https://blog.gospodarets.com/css_apply_rule "CSS @apply rule (native CSS mixins)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSSの`@aaply` Proposalについての解説

----

## power-assert + babel as a development tool | Web Scratch
[efcl.info/2016/04/14/espower-babel-is-deprecated/](http://efcl.info/2016/04/14/espower-babel-is-deprecated/ "power-assert + babel as a development tool | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

power-assert+babel+mochaの構成について。
デバッグビルド時は情報量の多いassert、プロダクションビルド時はassertを取り除き、JSDocからランタイムassertをしてチェックする話

----

## christianalfoni - RxJs the smartest dumbest tool ever
[www.christianalfoni.com/articles/2016\_03\_31\_RxJs-the-smartest-dumbest-tool-ever](http://www.christianalfoni.com/articles/2016_03_31_RxJs-the-smartest-dumbest-tool-ever "christianalfoni - RxJs the smartest dumbest tool ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">tutorial</span></p>

RxJSはどのような問題を解決するのかという話

----

## Scalable Single-Page Application Architecture – Minko Gechev&#x27;s blog
[blog.mgechev.com/2016/04/10/scalable-javascript-single-page-app-angular2-application-architecture/](http://blog.mgechev.com/2016/04/10/scalable-javascript-single-page-app-angular2-application-architecture/ "Scalable Single-Page Application Architecture – Minko Gechev's blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

AngularJS2 + RxJSでCQRS+EventSourcing的なアプローチ。 DIでの依存解決、レイヤー間の隔離やasync serviceの動きが面白い。

----

## Immutability is not enough
[codewords.recurse.com/issues/six/immutability-is-not-enough](https://codewords.recurse.com/issues/six/immutability-is-not-enough "Immutability is not enough")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

Immutable.jsを使ったStateの更新について。
単純にStateをimmutableにして、単純に関数を逐次的に適応すると、前のStateを参照しない問題が起こりえる。
また“lost update”の問題について

----

## react-storybookを用いたReactコンポーネント開発 - Hatena Developer Blog
[developer.hatenastaff.com/entry/2016/04/14/150000](http://developer.hatenastaff.com/entry/2016/04/14/150000 "react-storybookを用いたReactコンポーネント開発 - Hatena Developer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

React Componentをストーリーにもとづき確認できるスタイルガイド的なreact-storybookについて

----

## Leveling Up with React: Redux | CSS-Tricks
[css-tricks.com/learning-react-redux/](https://css-tricks.com/learning-react-redux/ "Leveling Up with React: Redux | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Reduxにおけるデータフローなどをわかりやすく解説したチュートリアル

----

## CoffeeScriptからES2015(ES6)へ移行しました - ペパボテックブログ
[tech.pepabo.com/2016/04/13/coffeescript-transpiled-es/](http://tech.pepabo.com/2016/04/13/coffeescript-transpiled-es/ "CoffeeScriptからES2015(ES6)へ移行しました - ペパボテックブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

CoffeeScriptをdecafを使って変換し、JavaScriptに移行する話。

----

## 【意訳】Webpackの混乱ポイント - Qiita
[qiita.com/chuck0523/items/caacbf4137642cb175ec](http://qiita.com/chuck0523/items/caacbf4137642cb175ec "【意訳】Webpackの混乱ポイント - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">翻訳</span></p>

"Webpack — The Confusing Parts"の翻訳。
webpackの設定において混乱しやすいことについてまとめられている。

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Let&#x27;s Learn ES6
[letslearnes6.com/](http://letslearnes6.com/ "Let's Learn ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">動画 </span></p>

ES6について学ぶ動画シリーズのサイト

- [Let&#x27;s Learn ES6 - YouTube](https://www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX "Let&#x27;s Learn ES6 - YouTube")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Makeitopen.com - Open Source Learning
[makeitopen.com/](http://makeitopen.com/ "Makeitopen.com - Open Source Learning")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React NativeでF8のアプリをどのように作っていったかの話

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Rich Harris / buble · GitLab
[gitlab.com/Rich-Harris/buble](https://gitlab.com/Rich-Harris/buble "Rich Harris / buble · GitLab")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

BabelのようなES2015のコードをES5に変換するツール。
Babelのような拡張性や仕様への準拠よりも、変換速度を重視した作りになっている

----

## thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.
[github.com/thejameskyle/babel-react-optimize](https://github.com/thejameskyle/babel-react-optimize "thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

React(JSX)の最適化をするBabelプラグイン

----

## Our Justified Layout Goes Open Source | code.flickr.com
[code.flickr.net/2016/04/05/our-justified-layout-goes-open-source/](http://code.flickr.net/2016/04/05/our-justified-layout-goes-open-source/ "Our Justified Layout Goes Open Source | code.flickr.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

Flickerの画像を敷きつけるUIライブラリ

----
