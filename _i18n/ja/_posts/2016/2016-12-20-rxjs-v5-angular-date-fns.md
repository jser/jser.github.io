---
title: "2016-12-20のJS: RxJS v5、Angular、date-fns"
author: azu
layout: post
date : 2016-12-20T10:38
category: JSer
tags:
    - Rx
    - Angular
    - Date
    - library

---

JSer.info #310 - 

----
<h1 class="site-genre">ヘッドライン</h1>

----

## rxjs/CHANGELOG.md at master · ReactiveX/rxjs
[github.com/ReactiveX/rxjs/blob/master/CHANGELOG.md](https://github.com/ReactiveX/rxjs/blob/master/CHANGELOG.md "rxjs/CHANGELOG.md at master · ReactiveX/rxjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

RxJS 5.0.0リリース

----

## jsdom/Changelog.md at 9.9.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.9.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.9.0/Changelog.md "jsdom/Changelog.md at 9.9.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.9.0リリース。
`document.createCDATASection`、`node.wholeText`のサポート、バグ修正など

----

## Release v5.0.0 · reactjs/react-redux
[github.com/reactjs/react-redux/releases/tag/v5.0.0](https://github.com/reactjs/react-redux/releases/tag/v5.0.0 "Release v5.0.0 · reactjs/react-redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v5.0.0リリース。
後方互換性はあるけどメジャーアップデート、`connect()`のオプションを追加、`connectAdvanced()`を追加など

----

## webpack 2.2: The Release Candidate – webpack – Medium
[medium.com/webpack/webpack-2-2-the-release-candidate-2e614d05d75f](https://medium.com/webpack/webpack-2-2-the-release-candidate-2e614d05d75f "webpack 2.2: The Release Candidate – webpack – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack 2.2.0 RCリリース。
2.x系初のRCリリースとなってる

- [Release v2.2.0-rc.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v2.2.0-rc.0 "Release v2.2.0-rc.0 · webpack/webpack")

----

## Release v0.37.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.37.0](https://github.com/facebook/flow/releases/tag/v0.37.0 "Release v0.37.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow v0.37.0 リリース。
built-in libの定義を更新、`declare module`内で`import type`と`import typeof`を使えるようになるなど

----

## Angular: Angular 1.6.0 released
[angularjs.blogspot.com/2016/12/angular-160-released.html](http://angularjs.blogspot.com/2016/12/angular-160-released.html "Angular: Angular 1.6.0 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

AngularJS 1.6.0リリース。
jqLiteをjQuery 3の挙動に合わせるように、expression sandboxを削除。
また、JSONPリクエストはホワイトリストがデフォルトになるなど多數のBreaking Changeが含まれている

- [angular.js/CHANGELOG.md at master · angular/angular.js](https://github.com/angular/angular.js/blob/master/CHANGELOG.md#160-rainbow-tsunami-2016-12-08 "angular.js/CHANGELOG.md at master · angular/angular.js")
- [AngularJS: Developer Guide: Migrating from Previous Versions](https://docs.angularjs.org/guide/migration#migrating-from-1-5-to-1-6 "AngularJS: Developer Guide: Migrating from Previous Versions")
- [Angular: Angular 1.6 - Expression Sandbox Removal](http://angularjs.blogspot.jp/2016/09/angular-16-expression-sandbox-removal.html "Angular: Angular 1.6 - Expression Sandbox Removal")

----
<h1 class="site-genre">アーティクル</h1>

----

## Angular: Ok... let me explain: it&#x27;s going to be Angular 4.0, or just Angular
[angularjs.blogspot.com/2016/12/ok-let-me-explain-its-going-to-be.html](http://angularjs.blogspot.com/2016/12/ok-let-me-explain-its-going-to-be.html "Angular: Ok... let me explain: it's going to be Angular 4.0, or just Angular")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AngularJSの次のメジャーバージョンは4を予定している話。
既に`@angular/router`がv3であるため、合わせるためにv4へあげる。
2017年3月にリリースする予定

----

## Performance Calendar » Prefer DEFER Over ASYNC
[calendar.perfplanet.com/2016/prefer-defer-over-async/](http://calendar.perfplanet.com/2016/prefer-defer-over-async/ "Performance Calendar » Prefer DEFER Over ASYNC")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

deferとasync属性について。 どちらもHTMLパースのブロックはしないが、レンダリングのブロックは発生する。 
deferは常にdomInteractiveが起きてから実行するため一定、しかしasyncはダウンロード速度によってはメインと被ることもある。
メインコンテンツに関係ないレンダリングを行うスクリプトはdefer属性を試すことで、メインのレンダリングが邪魔されずに進むかを確認した方が良いという話。

----

## JavaScript Clean Coding Best Practices | @RisingStack
[blog.risingstack.com/javascript-clean-coding-best-practices-node-js-at-scale/](http://blog.risingstack.com/javascript-clean-coding-best-practices-node-js-at-scale/ "JavaScript Clean Coding Best Practices | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

読みやすいJavaScriptのコードを書くためのプラクティス

----

## Writing Declaration Files for @types | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/12/14/writing-dts-files-for-types/](https://blogs.msdn.microsoft.com/typescript/2016/12/14/writing-dts-files-for-types/ "Writing Declaration Files for @types | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeSriptのDefinitelyTyped向けに型定義ファイルを書く方法について
手で書く方法とdts-genを使う方法について

----

## 実況中継シリーズ Vue.jsで実現するMVVMパターン Fluxアーキテクチャとの距離 - Re.Ra.Ku アドベントカレンダー day 13 - Re.Ra.Ku tech blog
[techblog.reraku.co.jp/entry/2016/12/13/080000](http://techblog.reraku.co.jp/entry/2016/12/13/080000 "実況中継シリーズ Vue.jsで実現するMVVMパターン Fluxアーキテクチャとの距離 - Re.Ra.Ku アドベントカレンダー day 13 - Re.Ra.Ku tech blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MVC</span> <span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

MVVMとFluxのアーキテクチャに似ている部分と異なる部分について

----

## SurviveJS - Inferno - Blazing fast, React-like UI library - Interview with Dominic Gannaway
[survivejs.com/blog/inferno-interview/](http://survivejs.com/blog/inferno-interview/ "SurviveJS - Inferno - Blazing fast, React-like UI library - Interview with Dominic Gannaway")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span></p>

ReactライクなVirtual DOMを使ったUIライブラリであるInfernoの特徴について。
どのような仕組みで動いているのか、Reactなどとの違いについて

----

## The Inner Workings Of Virtual DOM – Medium
[medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf "The Inner Workings Of Virtual DOM – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">VirtualDOM</span> <span class="jser-tag">React</span></p>

(Preactの)Virtual DOMがどのような処理を経てレンダリングされているのかを追った記事。
Virtual DOMの最適化処理についてなど

----

## Cross-Browser HTML5 Form Validation is Finally Here! Now What? -Telerik Developer Network
[developer.telerik.com/topics/web-development/cross-browser-html5-form-validation-finally-now/](http://developer.telerik.com/topics/web-development/cross-browser-html5-form-validation-finally-now/ "Cross-Browser HTML5 Form Validation is Finally Here! Now What? -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">JavaScript</span></p>

HTML5 Form Validation APIについて。
WebKitもサポートしたので、すべてのブラウザで利用できるようになった

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Professor Frisby Introduces Composable Functional JavaScript - Course by @drboolean @eggheadio
[egghead.io/courses/professor-frisby-introduces-function-composition](https://egghead.io/courses/professor-frisby-introduces-function-composition "Professor Frisby Introduces Composable Functional JavaScript - Course by @drboolean @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptでのFunctionalプログラミングについてのスクリーンキャスト。
Either的な実装やカリー化などについて解説してる

----

## Vue.js Fundamentals - YouTube
[www.youtube.com/playlist?list=PLwAKR305CRO\_1yAao-8aZiQnBqJeyng4O](https://www.youtube.com/playlist?list=PLwAKR305CRO_1yAao-8aZiQnBqJeyng4O "Vue.js Fundamentals - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">video</span></p>

Vue.js 2.0のチュートリアル動画

----

## ECMAScript: latest and upcoming features // Speaker Deck
[speakerdeck.com/rauschma/ecmascript-latest-and-upcoming-features](https://speakerdeck.com/rauschma/ecmascript-latest-and-upcoming-features "ECMAScript: latest and upcoming features // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">slide</span></p>

ES2016/ES2017と今Stage 3であるProposalについての紹介スライド

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Npm Desktop Manager
[720kb.github.io/ndm/](https://720kb.github.io/ndm/ "Npm Desktop Manager")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">GUI</span></p>

npmのパッケージを管理するGUIアプリケーション

----

## date-fns/date-fns: ⏳ Modern JavaScript date utility library ⌛️
[github.com/date-fns/date-fns](https://github.com/date-fns/date-fns "date-fns/date-fns: ⏳ Modern JavaScript date utility library ⌛️")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Date周りの操作を提供するライブラリ。
lodashのように利用する関数だけを取り出して使えるようにするのが目的となってる

- [Add a brief comparison with Moment.js? · Issue #275 · date-fns/date-fns](https://github.com/date-fns/date-fns/issues/275#issuecomment-264934189 "Add a brief comparison with Moment.js? · Issue #275 · date-fns/date-fns")

----

## simple-statistics/simple-statistics: simple statistics for node &amp; browser javascript
[github.com/simple-statistics/simple-statistics](https://github.com/simple-statistics/simple-statistics "simple-statistics/simple-statistics: simple statistics for node & browser javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">統計</span></p>

統計的な関数のコレクションライブラリ。
Pythonのsimplestatisticsのport。

- [sheriferson/simplestatistics: Simple statistical functions implemented in readable Python.](https://github.com/sheriferson/simplestatistics "sheriferson/simplestatistics: Simple statistical functions implemented in readable Python.")

----
