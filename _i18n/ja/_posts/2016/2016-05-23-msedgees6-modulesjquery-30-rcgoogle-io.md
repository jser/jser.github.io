---
title: "2016-05-23のJS: MSEdgeがES6 Modulesをサポート、jQuery 3.0 RCリリース"
author: azu
layout: post
date : 2016-05-23T19:45
category: JSer
tags:
    - MSEdge
    - modules
    - jQuery
    - Google
    - 動画

---


JSer.info #280 - MSEdgeの新しいビルドが公開され、`<script type="module">`でのES6 modulesをフラグ付きでサポートしています。

- [Previewing ES6 Modules and more from ES2015, ES2016 and beyond | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/05/17/es6-modules-and-beyond/)

[Microsoft Edge で Modules を使ってみる - Browser](http://browser.hatenablog.com/entry/2016/05/22/220131 "Microsoft Edge で Modules を使ってみる - Browser")でも書かれていますが、まだサポートは限定的です。

他のブラウザも実装中で、[仕様もまだ議論中](https://github.com/whatwg/loader)なところは多いですが、Moduleが一歩進んだ感じです。

- [Modules (ES6) - Chrome Platform Status](https://www.chromestatus.com/feature/5365692190687232 "Modules (ES6) - Chrome Platform Status")

また、MSEdgeはES2016で入る `**` と `Array.prototype.includes`のサポート、ES2017で入る予定の`Object.values`や`Object.entries`などの実装を開始しています。

ECMAScriptの部分に関してはオープンソースのChakraCoreリポジトリの方で実装されるので、以下のリポジトリを見ておくと実装状況がわかると思います。

- [Microsoft/ChakraCore: ChakraCore is the core part of the Chakra Javascript engine that powers Microsoft Edge](https://github.com/Microsoft/ChakraCore "Microsoft/ChakraCore: ChakraCore is the core part of the Chakra Javascript engine that powers Microsoft Edge")

ECMAScriptのProposalの場所は以下に変更されたので合わせて参照するといいかもしれません。

- [tc39/proposals: Tracking ECMAScript Proposals](https://github.com/tc39/proposals "tc39/proposals: Tracking ECMAScript Proposals")

> TC39, the standards body that works on the ECMAScript language, has a new GitHub-driven process and yearly release cadence.

記事中でGitHub-drivenとありますが、ChakraCoreのIssueに[WebKitの人](https://github.com/Microsoft/ChakraCore/issues/796)がいたり、[Proposal仕様を書いた人](https://github.com/Microsoft/ChakraCore/pull/475)がいたり、それらに対して[ECMAScriptのリポジトリからリンク](https://github.com/tc39/proposal-ptc-syntax/issues/7)があってリファレンスリンクが見えたりするので面白いです。

V8チームが書いた記事も合わせてみると、仕様策定から実装プロセスへの変化が見られるかもしれません。

- [V8 JavaScript Engine: ES6, ES7, and beyond](http://v8project.blogspot.jp/2016/04/es6-es7-and-beyond.html "V8 JavaScript Engine: ES6, ES7, and beyond")

-----


[jQuery 3.0 RC](http://blog.jquery.com/2016/05/20/jquery-3-0-release-candidate-released/)がリリースされました。

jQuery 3.xはIE9+サポートとなり、1.xと2.xから3.xに一本化されます。
過去のバージョンからのアップグレード方法については以下のドキュメントにまとめられています。

- [jQuery Core 3.0 Upgrade Guide | jQuery](https://jquery.com/upgrade-guide/3.0/ "jQuery Core 3.0 Upgrade Guide | jQuery")


----
<h1 class="site-genre">ヘッドライン</h1>

----

## Previewing ES6 Modules and more from ES2015, ES2016 and beyond | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/05/17/es6-modules-and-beyond/](https://blogs.windows.com/msedgedev/2016/05/17/es6-modules-and-beyond/ "Previewing ES6 Modules and more from ES2015, ES2016 and beyond | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge build 14342リリース。
ES6 modulesを扱える`<script type="module">`をフラグ付きでサポート、ES2016/2017の新しい機能である`**`、`Object.values`、`Object.entries`、`String#pad*`のサポートなど

- [Microsoft Edge で Modules を使ってみる - Browser](http://browser.hatenablog.com/entry/2016/05/22/220131 "Microsoft Edge で Modules を使ってみる - Browser")

----

## Release v15.1.0 · facebook/react
[github.com/facebook/react/releases/tag/v15.1.0](https://github.com/facebook/react/releases/tag/v15.1.0 "Release v15.1.0 · facebook/react")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v15.1.0リリース。
Chromeの`Object.assign`に順序バグがあるため対応するpolyfillをアップデート、react-addons-perfが書き直された。

- [Add new ReactPerf by gaearon · Pull Request #6046 · facebook/react](https://github.com/facebook/react/pull/6046 "Add new ReactPerf by gaearon · Pull Request #6046 · facebook/react")
- [Add feature test against buggy V8 versions by spicyj · Pull Request #32 · sindresorhus/object-assign](https://github.com/sindresorhus/object-assign/pull/32 "Add feature test against buggy V8 versions by spicyj · Pull Request #32 · sindresorhus/object-assign")

----

## Node v6.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.2.0/](https://nodejs.org/en/blog/release/v6.2.0/ "Node v6.2.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.2.0リリース。
`--no-deprecation`をランタイムに設定できる `process.noDeprecation = true;` が用意されるなど

----

## Release v6.9.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.9.0](https://github.com/babel/babel/releases/tag/v6.9.0 "Release v6.9.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.9.0リリース。
core-jsのアップデート、`systemGlobal`オプションの追加など

- [Releases · zloirock/core-js](https://github.com/zloirock/core-js/releases "Releases · zloirock/core-js")

----

## jQuery 3.0 Release Candidate…Released! | Official jQuery Blog
[blog.jquery.com/2016/05/20/jquery-3-0-release-candidate-released/](http://blog.jquery.com/2016/05/20/jquery-3-0-release-candidate-released/ "jQuery 3.0 Release Candidate…Released! | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.0 RCリリース

----
<h1 class="site-genre">アーティクル</h1>

----

## Refactoring a javascript video store
[martinfowler.com/articles/refactoring-video-store-js/](http://martinfowler.com/articles/refactoring-video-store-js/ "Refactoring a javascript video store")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">リファクタリング</span></p>

マーティン・ファウラーによるJavaScript(ES2015)のリファクタリング

----

## Iterators and Generators in Javascript | Kenneth Truyers
[www.kenneth-truyers.net/2016/05/20/iterators-and-generators-in-javascript/](https://www.kenneth-truyers.net/2016/05/20/iterators-and-generators-in-javascript/ "Iterators and Generators in Javascript | Kenneth Truyers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Iterator/Iterable/Generatorについての簡潔なまとめ

----

## How to Make Accessible Web Components — a Brief Guide
[www.sitepoint.com/accessible-web-components/](https://www.sitepoint.com/accessible-web-components/ "How to Make Accessible Web Components — a Brief Guide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">HTML</span> <span class="jser-tag">WebComponents</span></p>

Custom Elementで作った要素をAccessibleに実装するチュートリアル。
キーボード対応、WAI-ARIA、ハイコントラストモードでの確認など

----

## The 7 Cross-Browser Testing Tools You Need in 2016
[www.sitepoint.com/the-7-cross-browser-testing-tools-you-need-in-2016/](https://www.sitepoint.com/the-7-cross-browser-testing-tools-you-need-in-2016/ "The 7 Cross-Browser Testing Tools You Need in 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">webservice</span></p>

テスト用のクロスブラウザを扱えるサービスのまとめ

----

## ここがすごいぞ！ stylelint！ - Qiita
[qiita.com/inuscript/items/ff4f6972c988afbec3a8](http://qiita.com/inuscript/items/ff4f6972c988afbec3a8 "ここがすごいぞ！ stylelint！ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSSのLintをするstylelintについて

----

## step by stepで始めるKarma - Qiita
[qiita.com/howdy39/items/b9d704e7f84053924da3](http://qiita.com/howdy39/items/b9d704e7f84053924da3 "step by stepで始めるKarma - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">browser</span></p>

karmaの導入チュートリアル

----

## Six nifty ES6 tricks
[www.2ality.com/2016/05/six-nifty-es6-tricks.html](http://www.2ality.com/2016/05/six-nifty-es6-tricks.html "Six nifty ES6 tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6の少しテクニカルな使い方
デフォルト引数を使った必須引数のチェック、for of + `Object.entries`、サロゲートペア、配列の入れ方、template literal、mixinなどについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Learn Redux Video Tutorial Course
[learnredux.com/](https://learnredux.com/ "Learn Redux Video Tutorial Course")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">動画</span></p>

Reduxを使ったウェブアプリ開発に関するスクリーンキャスト

----

## Web and Chrome at Google I/O 2016 - YouTube
[www.youtube.com/user/ChromeDevelopers](https://www.youtube.com/user/ChromeDevelopers "Web and Chrome at Google I/O 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">動画</span></p>

Google I/O 2016の動画まとめ

- [Google I/O 2016](https://events.google.com/io2016/ "Google I/O 2016")

----

## Web Performance Tooling - Google I/O 2016 - YouTube
[www.youtube.com/watch?v=iMqi55rcR00](https://www.youtube.com/watch?v=iMqi55rcR00 "Web Performance Tooling - Google I/O 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome開発者ツールのパフォーマンス周りの使い方や見かたについて。
ケーススタディ毎にどの部分が遅いのかを見つけて、開発者ツールで本当にそれが原因なのかを確認したり、俯瞰の仕方についてなど

----

## Instant Loading: Building offline-first Progressive Web Apps - Google I/O 2016 - YouTube
[www.youtube.com/watch?v=cmGr0RszHc8](https://www.youtube.com/watch?v=cmGr0RszHc8 "Instant Loading: Building offline-first Progressive Web Apps - Google I/O 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">JavaScript</span></p>

ServiceWorkerを使ったオフラインファーストについての発表。
電波状態が悪いケースを想定した動作、IndexedDBを使ったデータの保存など

- [pazguille/offline-first: Everything you need to know to create offline-first web apps.](https://github.com/pazguille/offline-first "pazguille/offline-first: Everything you need to know to create offline-first web apps.")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Lerna · A tool for managing JavaScript projects with multiple packages.
[lernajs.io/](https://lernajs.io/ "Lerna · A tool for managing JavaScript projects with multiple packages.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">npm</span></p>

Babelで使われてるmonorepoを管理するツールであるLernaの公式サイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## brigand/react-mixin: mixins in react with es6 style classes
[github.com/brigand/react-mixin](https://github.com/brigand/react-mixin "brigand/react-mixin: mixins in react with es6 style classes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

React Componentに対してES6 Classesでmixinをするライブラリ

----

## yoshuawuyts/choo: - framework for creating sturdy web applications
[github.com/yoshuawuyts/choo](https://github.com/yoshuawuyts/choo "yoshuawuyts/choo: - framework for creating sturdy web applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span></p>

小さなモジュールを組み合わせたReduxライクな仕組みを持つフレームワーク。

----

## maxogden/yo-yo: A tiny library for building modular UI components using DOM diffing and ES6 tagged template literals
[github.com/maxogden/yo-yo](https://github.com/maxogden/yo-yo "maxogden/yo-yo: A tiny library for building modular UI components using DOM diffing and ES6 tagged template literals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

https://www.npmjs.com/package/morphdom をベースにtagged template literalsを使ったViewライブラリ

----

## wssgcg1213/babel-plugin-inline-replace-varibles: babel plugin to inline replace varibles
[github.com/wssgcg1213/babel-plugin-inline-replace-varibles](https://github.com/wssgcg1213/babel-plugin-inline-replace-varibles "wssgcg1213/babel-plugin-inline-replace-varibles: babel plugin to inline replace varibles")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

Babelで文字列に値をインライン展開するプラグイン

----
<h1 class="site-genre">書籍関係</h1>

----

## Exploring ES2016… by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]
[leanpub.com/exploring-es2016-es2017](https://leanpub.com/exploring-es2016-es2017 "Exploring ES2016… by Axel Rauschmayer \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span> <span class="jser-tag">JavaScript</span></p>

Exploring ES6のES2016/2017対応版

----
