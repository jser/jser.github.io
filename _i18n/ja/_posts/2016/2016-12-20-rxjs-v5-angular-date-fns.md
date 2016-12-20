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

JSer.info #310 - [RxJS 5](https://github.com/ReactiveX/rxjs "RxJS 5")がリリースされました。
Microsoftがメンテナンスしていた[Reactive-Extensions/RxJS](https://github.com/Reactive-Extensions/RxJS "Reactive-Extensions/RxJS")(RxJS 4)を書き直したバージョンで、互換性がある部分はありますがAPIも色々変更されています。

- [rxjs/CHANGELOG.md at master · ReactiveX/rxjs](https://github.com/ReactiveX/rxjs/blob/master/CHANGELOG.md#500-2016-12-13 "rxjs/CHANGELOG.md at master · ReactiveX/rxjs")

v4からv5へのマイグレーションは次のドキュメントにまとめられています。

- [Migrating from RxJS 4 to 5](https://github.com/ReactiveX/rxjs/blob/master/MIGRATION.md "Migrating from RxJS 4 to 5")

RxJS v5は現在Stage 1の[ECMAScript Observable](https://github.com/tc39/proposal-observable "ECMAScript Observable") Proposalに準拠した実装です。
([Stage 1](https://thefeedbackloop.xyz/tc39-a-process-sketch-stages-0-and-1/ "Stage 1")なので仕様自体が変わる可能性はあります)

また、デバッグのしやすさやパフォーマンスなどが改善され、Rxの特徴と言えるOperatorが整理されています。

----

AngularJS 1.xの最新版である[AngularJS 1.6.0](http://angularjs.blogspot.jp/2016/12/angular-160-released.html "AngularJS 1.6.0")がリリースされました。

- [Angular: Angular 1.6.0 released](http://angularjs.blogspot.jp/2016/12/angular-160-released.html "Angular: Angular 1.6.0 released")
- [1.6.0 rainbow-tsunami (2016-12-08)](https://github.com/angular/angular.js/blob/master/CHANGELOG.md#160-rainbow-tsunami-2016-12-08 "1.6.0 rainbow-tsunami (2016-12-08)")

詳しい変更点は[CHANGELOG](https://github.com/angular/angular.js/blob/master/CHANGELOG.md#160-rainbow-tsunami-2016-12-08)にかかれています。
jqLiteをjQuery 3の挙動に合わせるように変更、[Expression Sandboxを削除](http://angularjs.blogspot.jp/2016/09/angular-16-expression-sandbox-removal.html)。
また、JSONPリクエストはホワイトリストがデフォルトになるなど多數のBreaking Changeが含まれています。

AngularJS 1.xはsemverではありませんが、2.0からはsemverに沿う方針へ変更されています。
加えて2.0はタイムラインベースのアップデートも行うため、Angaular 2からは半年ごとのmajorアップデートを行います。
また、3.xは`@angular/router`がすでにv3を使っていて、バージョンがずれてしまうため、次のメジャーバージョンはv4となるそうです。

詳しくは、次の記事で解説されています。

- [Angular: Ok... let me explain: it's going to be Angular 4.0, or just Angular](http://angularjs.blogspot.jp/2016/12/ok-let-me-explain-its-going-to-be.html "Angular: Ok... let me explain: it&#39;s going to be Angular 4.0, or just Angular")
- [Angularの次バージョンは「Angular 4」に、2017年3月リリース。今後は単に「Angular」と呼んでほしいと － Publickey](http://www.publickey1.jp/blog/16/angularangular_420173angular.html "Angularの次バージョンは「Angular 4」に、2017年3月リリース。今後は単に「Angular」と呼んでほしいと － Publickey")

AngularのLTSについては特に決まっていないようです。

- [Angular LTS version · Issue #12331 · angular/angular](https://github.com/angular/angular/issues/12331 "Angular LTS version · Issue #12331 · angular/angular")

----

[date-fns - modern JavaScript date utility library](https://date-fns.org/ "date-fns - modern JavaScript date utility library")というライブラリは[Moment.js](http://momentjs.com/ "Moment.js")のように日付周りを扱うutilityライブラリです。
[Lodash](https://lodash.com/ "Lodash")のように、それぞれの操作を独立した関数として扱えるようにすることが目的の一つとなっています。
そのため、必要なものだけを読み込んで使うことができます。

また、Moment.jsは基本的にMutableなAPIとなっていますが、date-fnsはImmutableなAPIとなっています。

- Moment.jsでもImmutableに扱うAPIの提案がでています
- [Support a pseudo-immutable API (first-party Frozen Moment) by butterflyhug · Pull Request #2 · moment/moment-rfcs](https://github.com/moment/moment-rfcs/pull/2 "Support a pseudo-immutable API (first-party Frozen Moment) by butterflyhug · Pull Request #2 · moment/moment-rfcs")

また、開発中の部分もありますが現在のステータスは次にまとめられています。

- [Add a brief comparison with Moment.js? · Issue #275 · date-fns/date-fns](https://github.com/date-fns/date-fns/issues/275#issuecomment-264934189 "Add a brief comparison with Moment.js? · Issue #275 · date-fns/date-fns")


----

## お知らせ

[JSer.info 6周年と300回記念イベント - connpass](https://jser.connpass.com/event/46997/ "JSer.info 6周年と300回記念イベント - connpass")の抽選結果が発表されています。
まだ、発表枠があるので何か話したい事がある人は申し込んで見てください。

- [2017年1月15日(日)に JSer.info 6周年 && 300回目記念イベント を開催します - JSer.info](https://jser.info/2016/12/13/announcement-jser-info-6years-event/ "2017年1月15日(日)に JSer.info 6周年 &amp;&amp; 300回目記念イベント を開催します - JSer.info")

また、当日JavaScript Discussionというコーナーで次の質問ボードを元に議論する時間が設けています。
質問、聞きたいこと、話したいこと、主張を書き込むことができます。
当日も時間を取りますが、事前に書いてもらっても問題ありません。

- [JSer.info 6周年 - JavaScript Discussion](https://app.sli.do/event/bkry5ojl/ask "JSer.info 6周年 - JavaScript Discussion")

気になる質問は :+1: で投票すると上に来るのでテーマとして取り上げやすくなります。

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
