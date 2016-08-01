---
title: "2016-08-02のJS: Mocha 3.0、React 15.3.0、ECMAScript Proposalの進捗"
author: azu
layout: post
date : 2016-08-01T23:28
category: JSer
tags:
    - testing
    - React
    - ECMAScript

---


JSer.info #290

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Aurelia 1.0 is Here!!!
[blog.durandal.io/2016/07/27/aurelia-1-0-is-here/](http://blog.durandal.io/2016/07/27/aurelia-1-0-is-here/ "Aurelia 1.0 is Here!!!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Aurelia 1.0リリース

----

## Ember.js - Ember.js 2.7 and 2.8 Beta Released
[emberjs.com/blog/2016/07/25/ember-2-7-and-2-8-beta-released.html](http://emberjs.com/blog/2016/07/25/ember-2-7-and-2-8-beta-released.html "Ember.js - Ember.js 2.7 and 2.8 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Ember.js 2.7と2.8 Betaリリース。
Ember 2.8では`Ember.Engine`、`Array#includes`のpolyfill、`Ember.String.isHTMLSafe`などが追加される

----

## mocha/CHANGELOG.md at master · mochajs/mocha
[github.com/mochajs/mocha/blob/master/CHANGELOG.md](https://github.com/mochajs/mocha/blob/master/CHANGELOG.md "mocha/CHANGELOG.md at master · mochajs/mocha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 3.0.0リリース。 非同期テスト時に`done()`の実装とPromiseを返すとエラーになる、`--grep`で正規表現リテラル的な文字列が指定可能に、`describe.only`の動作を改善など

----

## Jest 14.0: React Tree Snapshot Testing · Jest
[facebook.github.io/jest/blog/2016/07/27/jest-14.html](http://facebook.github.io/jest/blog/2016/07/27/jest-14.html "Jest 14.0: React Tree Snapshot Testing · Jest")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Jest 14.0リリース。
React Componentのsnapshot testing、React Nativeサポートなど

----

## Release v15.3.0 · facebook/react
[github.com/facebook/react/releases/tag/v15.3.0](https://github.com/facebook/react/releases/tag/v15.3.0 "Release v15.3.0 · facebook/react")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 15.3.0リリース。
`React.PureComponent`の追加、propTypesのバリデーション改善、テスト向けの`react-test-renderer`を公開など

----

## ESLint v3.2.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/07/eslint-v3.2.0-released](http://eslint.org/blog/2016/07/eslint-v3.2.0-released "ESLint v3.2.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v3.2.0リリース。
`no-tab`ルールの追加など

- [ESLint v3.2.0 - Qiita](http://qiita.com/mysticatea/items/706f4bb024d7ceb78f1d "ESLint v3.2.0 - Qiita")

----

## Release v6.12.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.12.0](https://github.com/babel/babel/releases/tag/v6.12.0 "Release v6.12.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.12.0リリース。
`babel-plugin-transform-runtime`に`helpers: false`を追加。
` babel-plugin-transform-es2015-modules-umd `に`exactGlobals`オプションを追加など

----
<h1 class="site-genre">アーティクル</h1>

----

## ECMAScript proposal updates @ 2016-07 | ECMAScript Daily
[ecmascript-daily.github.io/2016/07/30/last-minutes-proposals-changes](https://ecmascript-daily.github.io/2016/07/30/last-minutes-proposals-changes "ECMAScript proposal updates @ 2016-07 | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2016年7月のミーティングのProposal statusの変化まとめ。
Async/Awaitとtrailing function commasがstage 4になった

----

## A Comprehensive Guide to Font Loading Strategies—zachleat.com
[www.zachleat.com/web/comprehensive-webfonts/](https://www.zachleat.com/web/comprehensive-webfonts/ "A Comprehensive Guide to Font Loading Strategies—zachleat.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span></p>

Font Loadingの手法やそれぞれの良いところ、良くないところについてのまとめ

----

## A step-by-step TDD approach on testing React components using Enzyme
[thereignn.ghost.io/a-step-by-step-tdd-approach-on-testing-react-components-using-enzyme/](http://thereignn.ghost.io/a-step-by-step-tdd-approach-on-testing-react-components-using-enzyme/ "A step-by-step TDD approach on testing React components using Enzyme")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">jsx</span> <span class="jser-tag">testing</span></p>

Enzymeを使ったReact ComponentのTDDについて。
React Componentをテスト駆動で開発するチュートリアル

----

## Taming requestAnimationFrame and requestIdleCallback
[www.webreflection.co.uk/blog/2016/07/31/taming-raf-and-rick](https://www.webreflection.co.uk/blog/2016/07/31/taming-raf-and-rick "Taming requestAnimationFrame and requestIdleCallback")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

requestAnimationFrame/requestIdleCallbackなどのスケジューリングを行うライブラリについて

- [WebReflection/sob: Schedule on Browser](https://github.com/WebReflection/sob "WebReflection/sob: Schedule on Browser")

----

## CSS: will-change指定時の挙動, パフォーマンスへの影響と考察 - Qiita
[qiita.com/damele0n/items/71352757d0e6fdf5b184](http://qiita.com/damele0n/items/71352757d0e6fdf5b184 "CSS: will-change指定時の挙動, パフォーマンスへの影響と考察 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

CSSの`will-change`の効果の検証とブラウザの実装(ソースコード)について。
指定した値毎の挙動についてなど

----

## React v0.14.x から v15.2.x へのアップデート録 ::ハブろぐ
[havelog.ayumusato.com/develop/javascript/e717-react\_v15\_upgrade.html](https://havelog.ayumusato.com/develop/javascript/e717-react_v15_upgrade.html "React v0.14.x から v15.2.x へのアップデート録 ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React 0.14.xから15.2へのアップデートした際に出る警告と対処法について

----

## JavaScript Systems Music
[teropa.info/blog/2016/07/28/javascript-systems-music.html](http://teropa.info/blog/2016/07/28/javascript-systems-music.html "JavaScript Systems Music")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">music</span></p>

JavaScriptでSystems Music

- [Systems music - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Systems_music "Systems music - Wikipedia, the free encyclopedia")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Vue.js @ Laracon - Google スライド
[docs.google.com/presentation/d/16MpK3I2LZz47QdLg3uMNkCC3PqmM0znXF3-FdCEpics/mobilepresent#slide=id.p](https://docs.google.com/presentation/d/16MpK3I2LZz47QdLg3uMNkCC3PqmM0znXF3-FdCEpics/mobilepresent#slide=id.p "Vue.js @ Laracon - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Vue.js 2.0のコンセプトについてのスライド

----

## Async Redux Module 1 // Speaker Deck
[speakerdeck.com/freddyrangel/async-redux-module-1](https://speakerdeck.com/freddyrangel/async-redux-module-1 "Async Redux Module 1 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">スライド</span></p>

Reduxでの非同期についてのスライド集。
そもそも動きから、middleware、thunk、sagaについて

- [Async Redux Module 2 // Speaker Deck](https://speakerdeck.com/freddyrangel/async-redux-module-2 "Async Redux Module 2 // Speaker Deck")
- [Async Redux Module 3 // Speaker Deck](https://speakerdeck.com/freddyrangel/async-redux-module-3 "Async Redux Module 3 // Speaker Deck")
- [Async Redux Module 4 // Speaker Deck](https://speakerdeck.com/freddyrangel/async-redux-module-4 "Async Redux Module 4 // Speaker Deck")
- [Async Redux Module 5 // Speaker Deck](https://speakerdeck.com/freddyrangel/async-redux-module-5 "Async Redux Module 5 // Speaker Deck")

----

## Modern Javascript | AngularClass
[courses.angularclass.com/courses/modern-javascript](http://courses.angularclass.com/courses/modern-javascript "Modern Javascript | AngularClass")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span></p>

JavaScriptについての動画講座。
ES5の復習からES6の新しい機能、TypeScript、npm、webpackについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## はじめに | 目次
[vuex.vuejs.org/ja/](http://vuex.vuejs.org/ja/ "はじめに | 目次")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">document</span> <span class="jser-tag">翻訳</span></p>

Vuexについてのドキュメント訳

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## CodeceptJS
[codecept.io/](http://codecept.io/ "CodeceptJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">php</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

PHPのCodeceptionインスパイアなJavaScriptテストフレームワーク。
シナリオテストのハイレベルAPIで、Protractorなど他のtest runnerの中でも動かせる。

- [Codeception](http://codeception.com/ "Codeception")

----

## rkendall/reffix: The Reference Fixer for analyzing and fixing broken path references in files.
[github.com/rkendall/reffix](https://github.com/rkendall/reffix "rkendall/reffix: The Reference Fixer for analyzing and fixing broken path references in files.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのrequireやimportのパス、HTMLのimgやscriptのパスのチェックと修正ができるツール

----

## mgol/check-dependencies: Checks if currently installed npm dependencies are installed in the exact same versions that are specified in package.json
[github.com/mgol/check-dependencies](https://github.com/mgol/check-dependencies "mgol/check-dependencies: Checks if currently installed npm dependencies are installed in the exact same versions that are specified in package.json")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npmでインストールしているバージョンとpacakge.jsonのバージョンが同一なのかをチェックできるライブラリとCLI

----
<h1 class="site-genre">書籍関係</h1>

----

## Front-End Web Development: The Big Nerd Ranch Guide: Chris Aquino, Todd Gandee: 9780134433943: Amazon.com: Books
[www.amazon.com/Front-End-Web-Development-Ranch-Guide/dp/0134433947](https://www.amazon.com/Front-End-Web-Development-Ranch-Guide/dp/0134433947 "Front-End Web Development: The Big Nerd Ranch Guide: Chris Aquino, Todd Gandee: 9780134433943: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2016年8月11日発売
Ember.jsを使ったウェブアプリについての書籍

----
