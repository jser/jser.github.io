---
title: "2016-05-16のJS: Electron 1.0、ブレークポイントの使い方、Bublé"
author: azu
layout: post
date : 2016-05-16T19:36
category: JSer
tags:
    - Electron
    - Chrome
    - debug
    - Babel
    - ES2015

---

JSer.info #279 - ChromiumとNode.jsをベースとしたデスクトップアプリ開発環境である[Electron 1.0](http://electron.atom.io/blog/2016/05/11/electron-1-0 "Electron 1.0")がリリースされました。

本体は非推奨なメソッドの削除が中心となっています。
合わせて開発者ツールの強化やデモ、テストツールが公開されています。

- [Devtron](http://electron.atom.io/devtron/)
- [electron/electron-api-demos: Explore the Electron APIs](https://github.com/electron/electron-api-demos)
- [Spectron](http://electron.atom.io/spectron/)

----

[ブレークポイントを使ったJavaScriptデバッグを整理してみた【再入門】 - Qiita](http://qiita.com/nekoneko-wanwan/items/02aed17773833c3ad3b2 "ブレークポイントを使ったJavaScriptデバッグを整理してみた【再入門】 - Qiita")という記事ではChrome開発者ツールでのブレークポイントの使い方について解説されています。

コードに対するブレークポイントからDOM、XHRなど色々なブレーク方法をスクリーンショット共に解説されているので分かりやすいです。

公式サイトも合わせて見るといいかもしれません

- [Chrome DevTools Overview - Google Chrome](https://developer.chrome.com/devtools "Chrome DevTools Overview - Google Chrome")

----

[Bublé – the blazing fast, batteries-included ES2015 compiler](https://buble.surge.sh/guide/ "Bublé – the blazing fast, batteries-included ES2015 compiler")は、ES2015のコードをES5へ変換することを目的としたTranspilerツールです。

[Babel](https://babeljs.io/ "Babel")とは異なる点としては以下のような点があります。

- [AST](http://efcl.info/2016/03/06/ast-first-step/ "AST")を変換してASTを生成するわけではなく、ASTから[magic-string](https://github.com/Rich-Harris/magic-string "magic-string")を使い直接コードを生成しています
  - ASTから直接コードを吐き出すので高速な変換ができます
  - 一方、中間フォーマットがないためプラグインのような拡張は難しいです
- Babel 6.xのようにプラグイン式ではなく、ビルトインで変換するパターンが入っています
- ECMAScriptの仕様準拠が目的ではない点
  - [Babel](https://babeljs.io/ "Babel")はECMAScriptへのできるだけ準拠した挙動になるように変換します
  - `loose`オプションを指定することで、ラフな変換をするようにできますがBubléはこちらがデフォルトとなります
- 変換できる機能が意図的に限定されています
  - `import/export`やComputed propertiesなどの変換はできません
  - 恐らく同作者の[rollup](https://github.com/rollup/rollup "rollup")と合わせ使うようなデザインになっています

Babelとは構造や目的も異なるので、興味がある人はためしてみるといいかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Electron 1.0
[electron.atom.io/blog/2016/05/11/electron-1-0](http://electron.atom.io/blog/2016/05/11/electron-1-0 "Electron 1.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 1.0リリース。

----

## ESLint v2.10.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/05/eslint-v2.10.0-released](http://eslint.org/blog/2016/05/eslint-v2.10.0-released "ESLint v2.10.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.10.0リリース。

- [ESLint v2.10.0 - Qiita](http://qiita.com/mysticatea/items/5df2d679283d0a84b296 "ESLint v2.10.0 - Qiita")

----

## Release Notes for Safari Technology Preview 4 | WebKit
[webkit.org/blog/6210/release-notes-for-safari-technology-preview-4/](https://webkit.org/blog/6210/release-notes-for-safari-technology-preview-4/ "Release Notes for Safari Technology Preview 4 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 4リリース。
`String.prototype.localeCompare`の実装、object literarlでも`super()`が呼べるように、`var log = console.log`が可能になるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## ブレークポイントを使ったJavaScriptデバッグを整理してみた【再入門】 - Qiita
[qiita.com/nekoneko-wanwan/items/02aed17773833c3ad3b2](http://qiita.com/nekoneko-wanwan/items/02aed17773833c3ad3b2 "ブレークポイントを使ったJavaScriptデバッグを整理してみた【再入門】 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

Chrome開発者ツールのブレークポイントの使い方や各種ブレークポイントについて。
画像と共に項目が解説されているので分かりやすい。

----

## するするさせたい：サイボウズ採用情報のアニメーション（その1） - fragmentary
[myakura.hatenablog.com/entry/2016/05/12/083000](http://myakura.hatenablog.com/entry/2016/05/12/083000 "するするさせたい：サイボウズ採用情報のアニメーション（その1） - fragmentary")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span></p>

CSSアニメーションのパフォーマンス問題を見つけ方と解決方法について

----

## An Ultimate Guide To CSS Pseudo-Classes And Pseudo-Elements – Smashing Magazine
[www.smashingmagazine.com/2016/05/an-ultimate-guide-to-css-pseudo-classes-and-pseudo-elements/](https://www.smashingmagazine.com/2016/05/an-ultimate-guide-to-css-pseudo-classes-and-pseudo-elements/ "An Ultimate Guide To CSS Pseudo-Classes And Pseudo-Elements – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSSの擬似要素と擬似クラスの網羅的な解説

----

## Get to Know the Page Visibility API | Scotch
[scotch.io/tutorials/get-to-know-the-page-visibility-api](https://scotch.io/tutorials/get-to-know-the-page-visibility-api "Get to Know the Page Visibility API | Scotch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

Page Visibility APIの使い所や使い方について

----

## ちゃんと使い分けてる? dependenciesいろいろ。 - Qiita
[qiita.com/cognitom/items/acc3ffcbca4c56cf2b95](http://qiita.com/cognitom/items/acc3ffcbca4c56cf2b95 "ちゃんと使い分けてる? dependenciesいろいろ。 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span></p>

npmのdependenciesの種類についての解説。
- dependencies
- devDependencies
- peerDependencies
- optionalDependencies
- bundledDependencies

----

## runtastic/flow-guide: Our definitive guide for using Flow static JavaScript type checker (https://flowtype.org)
[github.com/runtastic/flow-guide](https://github.com/runtastic/flow-guide "runtastic/flow-guide: Our definitive guide for using Flow static JavaScript type checker (https://flowtype.org)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">tutorial</span></p>

Flowの導入チュートリアル

----

## redux-observable — Medium
[medium.com/@benlesh/redux-observable-ec0b00d2eb52](https://medium.com/@benlesh/redux-observable-ec0b00d2eb52 "redux-observable — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span> <span class="jser-tag">Rx</span></p>

Netflixで使ってる`redux-observable`について。
なぜ`redux-`なのか? - ReduxはReact周りでよく知られているパターンであり、既に様々なRedux関連ツールが存在するからであるという話

- [blesh/redux-observable: RxJS middleware for Redux](https://github.com/blesh/redux-observable "blesh/redux-observable: RxJS middleware for Redux")

----

## Streamlining the Sign-in Flow Using Credential Management API | Web Updates - Google Developers
[developers.google.com/web/updates/2016/04/credential-management-api](https://developers.google.com/web/updates/2016/04/credential-management-api "Streamlining the Sign-in Flow Using Credential Management API | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">Chrome</span></p>

Credential Management APIについて。
自動サインインを実装しながら使い方について学ぶチュートリアル

- [Credential Management API を使ったサインインフローの効率化 | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/04/credential-management-api?hl=ja "Credential Management API を使ったサインインフローの効率化 | Web Updates - Google Developers")

----

## About document.ready
[www.webreflection.co.uk/blog/2016/05/10/document.ready](https://www.webreflection.co.uk/blog/2016/05/10/document.ready "About document.ready")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promiseを返す`document.ready`をどう実装するかという話。
`document.readyState`と`DOMContentLoaded`について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ng-conf 2016 - YouTube
[www.youtube.com/playlist?list=PLOETEcp3DkCq788xapkP\_OU-78jhTf68j](https://www.youtube.com/playlist?list=PLOETEcp3DkCq788xapkP_OU-78jhTf68j "ng-conf 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">動画 </span></p>

ng-conf 2016の動画一覧

- [ng-conf May 4th - 6th 2016 - The World&#x27;s Original Angular Conference](https://www.ng-conf.org/#/ "ng-conf May 4th - 6th 2016 - The World&#x27;s Original Angular Conference")

----

## How to make your Webpack builds 10x faster
[www.slideshare.net/trueter/how-to-make-your-webpack-builds-10x-faster](http://www.slideshare.net/trueter/how-to-make-your-webpack-builds-10x-faster "How to make your Webpack builds 10x faster")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">スライド</span> <span class="jser-tag">performance</span></p>

webpackのビルド速度改善についてのスライド

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## tc39/proposals: Tracking ECMAScript Proposals
[github.com/tc39/proposals](https://github.com/tc39/proposals "tc39/proposals: Tracking ECMAScript Proposals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

ECMAScriptのProposalまとめリポジトリ。
Active/InActive/Finished/Stage 0のProposalが一覧できる。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Bublé – the blazing fast, batteries-included ES2015 compiler
[buble.surge.sh/guide/](https://buble.surge.sh/guide/ "Bublé – the blazing fast, batteries-included ES2015 compiler")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">babel</span></p>

BabelのようにES2015のコードをES5に変換するツール。
設定なしで動作し、サポートしたいブラウザバージョンを指定することで変換内容を選択できる。

----

## garbles/why-did-you-update: Puts your console on blast when React is making unnecessary updates.
[github.com/garbles/why-did-you-update](https://github.com/garbles/why-did-you-update "garbles/why-did-you-update: Puts your console on blast when React is making unnecessary updates.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span></p>

Reactで`props`の中身が一致する場合にも、renderが呼ばれている事を検知してコンソールに表示するライブラリ

----

## leo/args: Minimal toolkit for building CLIs
[github.com/leo/args](https://github.com/leo/args "leo/args: Minimal toolkit for building CLIs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

minimistを使った引数処理、ヘルプ表示、サブコマンドなどに対応したライブラリ

----

## florian/x18n: A sane JavaScript internationalisation library
[github.com/florian/x18n](https://github.com/florian/x18n "florian/x18n: A sane JavaScript internationalisation library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">i18n</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

r18n gem互換記法が使えるi18nライブラリ

----

## documentationjs/globals-docs: Documentation URIs for JavaScript globals.
[github.com/documentationjs/globals-docs](https://github.com/documentationjs/globals-docs "documentationjs/globals-docs: Documentation URIs for JavaScript globals.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Mozilla</span></p>

JavaScriptの型やオブジェクトを渡すと、対応するMDNのドキュメントURLを返してくれるライブラリ

----
