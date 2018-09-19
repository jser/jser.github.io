---
title: "2018-09-18のJS: Chrome 70 beta、縦書きの実装、Vue Patterns"
author: "azu"
layout: post
date : 2018-09-18T01:52:53.161Z
category: JSer
tags:
- chrome
- vue
- css

---

JSer.info #401 - Chrome 70βがリリースされました。

- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html)


Shape Detection APIの[origin trial](https://blog.jxck.io/entries/2016-09-29/vender-prefix-to-origin-trials.html)の開始、Credential Management APIで指紋認証をサポート、Web Workerで`name`オプションをサポート、TLS 1.3のサポートなどが行われています。

Web Components v0(Custom Elements v0、HTML Imports、Shadow DOM v0)が非推奨(deprecated)となりました。
Deprecatedから削除までのスケジュールは次のMLにかかれていますが、origin trialsで利用範囲を狭めていき最終的に2020年Q2で削除の予定です。

- [Intent to Deprecate and Remove: Shadow DOM V0, Custom Elements V0, HTML Imports - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/h-JwMiPUnuU/sl79aLoLBQAJ)

このDeprecatedのためにOrigin Trialを使うという珍しい手法については次のPodcastでも話されています。

- [ep40 Monthly Web 201807 | mozaic.fm](https://mozaic.fm/episodes/40/monthly-web-201807.html) 0:29:00~

----

[カクヨムでの縦組み表示の実装と、縦書きWebの将来に向けて (builderscon tokyo 2018) - Hatena Developer Blog](http://developer.hatenastaff.com/entry/2018/09/11/152905)という記事では縦組み表示のサイトを作成ためのウェブ標準や現在の実装の問題と回避方法について書かれています。
CSSを使った縦組みの実装について書かれています。ブラウザ固有の問題などもあり、それらの問題に対してどのように対処したのかについても書かれています。

また縦組みに関するCSSの仕様として[CSS3 module: text](https://www.w3.org/TR/2001/WD-css3-text-20010517/)と[CSS Writing Modes Module Level 3](https://www.w3.org/TR/2010/WD-css3-writing-modes-20101202/)などがありますが、これらの仕様策定に関する[@fantasai](https://twitter.com/fantasai)のインタビューも最近公開されたので合わせてみるといいかもしれません。

- [私のゴールは世界中の言語でCSSを使えるようにすること EPUB3で縦書きを実現した、fantasai（エリカ・エテマッド）に聞く](https://www.aplab.jp/fantasai)

----

[Vue Patterns](https://learn-vuejs.github.io/vue-patterns/)というドキュメントでは、Vueのコンポーネントに関するパターンなどについて紹介されています。

基本的なコンポーネントの宣言方法や使い方、エラーハンドリング、 Composition、HOCやRender Propsなどのパターンについてなどコンポーネントの記述周りについてがまとまっています。

----

## お知らせ

[JSer.info 400回記念イベント](https://jser.connpass.com/event/100092/)は今週の土曜日にサイボウズ株式会社(東京オフィス)で開催予定です。

- [2018年9月22日(土)に JSer.info 400回目記念イベントを開催します - JSer.info](https://jser.info/2018/08/31/jser-400-event-announce/)

参加枠はギリギリオーバーしていますが、当日のキャンセルなどもありますので、参加したい人はできるだけ事前に申し込んでおいてください。当日の入場に必要な**ID**をconnpassのメッセージで送るため、事前に補欠でも登録しておいたほうが安全です。

当日必要なものは次のとおりです。

- ConnpassからのメールにかかれているID(7Fの入館端末でIDを入力して入館証を発行するの利用)
- JavaScript Discussionで聞きたいこと
  - 事前に書いておきたい人は[事前質問用のSpreadSheet](https://docs.google.com/spreadsheets/d/1pk1Nw4B5eo5mwOcQUo3ipVdwBOAeTkWCWbwW8I5e8Iw/edit#gid=0)にかいておいてください
- 参加枠の人は1000円
- LTをしたい人はLTの準備

他になにか聞きたいことがある人は[JSer.info 400回記念イベント · Issue #102 · jser/jser.info](https://github.com/jser/jser.info/issues/102)などを参照してください。

それでは、当日会えることを楽しみにしています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 3.1 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/09/13/announcing-typescript-3-1-rc/](https://blogs.msdn.microsoft.com/typescript/2018/09/13/announcing-typescript-3-1-rc/ "Announcing TypeScript 3.1 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.1 RCリリース。
Mapped TypeでTupleやArrayの扱いを改善、関数にプロパティを定義できるように。
また破壊的な変更点として`lib.d.ts`をWeb IDLから生成するためベンダー独自の型が削除される。`typeof foo === "function"`でのtype gurdeの挙動の変更など

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes "Breaking Changes · Microsoft/TypeScript Wiki")

----

## Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more
[blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 70リリース。
Shape Detection APIのorigin trialの開始、 Web Authenticationで指紋認証をサポート、Web Workerで`name`オプション、TLS 1.3のサポート。
Web Components v0を非推奨化など


----

## Acorn 6.0.0 released - Acorn - discuss.Tern
[discuss.ternjs.net/t/acorn-6-0-0-released/230](https://discuss.ternjs.net/t/acorn-6-0-0-released/230 "Acorn 6.0.0 released - Acorn - discuss.Tern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptパーサのAcorn 6.0.0リリース。
TypeScriptの型定義を同梱、`ecmaVersion`のデフォルト値を`9`に変更、いくつかの内部処理を別パッケージに分離など。


----

## neonious/lowjs: A port of Node.JS with far lower system requirements. Community version for POSIX systems such as Linux, uClinux or Mac OS X.
[github.com/neonious/lowjs](https://github.com/neonious/lowjs "neonious/lowjs: A port of Node.JS with far lower system requirements. Community version for POSIX systems such as Linux, uClinux or Mac OS X.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

組み込み向けのファイルサイズが2MB程度のNode.jsポート。 V8の代わりにDuktapeを使っている。


----

## Release v3.0.0 · janl/mustache.js
[github.com/janl/mustache.js/releases/tag/v3.0.0](https://github.com/janl/mustache.js/releases/tag/v3.0.0 "Release v3.0.0 · janl/mustache.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

mustache.js 3.0.0リリース。
プリミティブ型のプロパティのレンダリングに対応、`render`の第４引数にdelimiterを指定できるようにしキャッシュの問題を修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## カクヨムでの縦組み表示の実装と、縦書きWebの将来に向けて (builderscon tokyo 2018) - Hatena Developer Blog
[developer.hatenastaff.com/entry/2018/09/11/152905](http://developer.hatenastaff.com/entry/2018/09/11/152905 "カクヨムでの縦組み表示の実装と、縦書きWebの将来に向けて (builderscon tokyo 2018) - Hatena Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

縦書き表示を行った際のブラウザのバグや問題への対象方法について


----

## Introducing the React Profiler – React Blog
[reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html](https://reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html "Introducing the React Profiler – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React 16.5でサポートされたプロファイルと開発者ツールについて。
開発者ツールでの計測方法(dev/prod)、使い方などについて


----

## Why React16 is a blessing to React developers – freeCodeCamp.org
[medium.freecodecamp.org/why-react16-is-a-blessing-to-react-developers-31433bfc210a](https://medium.freecodecamp.org/why-react16-is-a-blessing-to-react-developers-31433bfc210a "Why React16 is a blessing to React developers – freeCodeCamp.org")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16で追加された機能の紹介。
`componentDidCatch`のエラーハンドリング、Fragments、Portal、Custom DOM Attributesについて。
Ref周りのAPIやContext APIの追加、ライフサイクルの変更についてなど


----

## Operational Introduction to Algebraic Effects and Continuations
[gist.github.com/yelouafi/57825fdd223e5337ba0cd2b6ed757f53](https://gist.github.com/yelouafi/57825fdd223e5337ba0cd2b6ed757f53 "Operational Introduction to Algebraic Effects and Continuations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

redux-sagaの作者によるJavaScriptでのAlgebraic Effectsについての連載。
Continuation Passing Style (CPS)について


----

## Vue conference and meetup videos from 2018 (Q1 digest) - MeetupFeed
[blog.meetupfeed.com/vue-conference-and-meetup-videos-from-2018-q1-digest/](https://blog.meetupfeed.com/vue-conference-and-meetup-videos-from-2018-q1-digest/ "Vue conference and meetup videos from 2018 (Q1 digest) - MeetupFeed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">video</span> <span class="jser-tag">Vue</span></p>

Vueに関するカンファレンスやイベントなどの発表、動画をまとめた記事。
各発表の概要とリンクが紹介されている


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Webフロントエンド パフォーマンス改善ハンドブックを公開しました - dwango on GitHub
[dwango.github.io/articles/web-frontend-performance-handbook/](https://dwango.github.io/articles/web-frontend-performance-handbook/ "Webフロントエンド パフォーマンス改善ハンドブックを公開しました - dwango on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">performance</span></p>

ウェブサイトのパフォーマンス改善についてのドキュメント。ランタイムとページロードタイムにおける問題の見つけ方や改善の事例についてまとめられたもの。

- [Introduction · Webフロントエンド パフォーマンス改善ハンドブック](https://dwango-js.github.io/performance-handbook/ "Introduction · Webフロントエンド パフォーマンス改善ハンドブック")

----

## Vue Patterns
[learn-vuejs.github.io/vue-patterns/](https://learn-vuejs.github.io/vue-patterns/ "Vue Patterns")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

Vueにおけるパターンについてまとめたドキュメント。
基本的なコンポーネントの宣言方法や使い方、エラーハンドリング、 Composition、HOCやRender Propsなどのパターンについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## UmiJS
[umijs.org/](https://umijs.org/ "UmiJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

Next.jsライクなJavaScriptフレームワーク。
webpackを使ったビルド、開発サーバ、Nuxt.jsのようなルーティング、プラグインでの拡張などをサポートしている。


----

## axa-group/nlp.js: An NLP library built in node over Natural, with entity extraction, sentiment analysis, automatic language identify, and so more
[github.com/axa-group/nlp.js](https://github.com/axa-group/nlp.js "axa-group/nlp.js: An NLP library built in node over Natural, with entity extraction, sentiment analysis, automatic language identify, and so more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">nlp</span></p>

いろいろな自然言語に対応してるNLPライブラリ。
言語の推定、Classifier、levenshtein距離など自然言語処理で使ういろいろな処理を実装している


----

## getgauge/taiko: A node.js library to automate chrome/chromium browser
[github.com/getgauge/taiko](https://github.com/getgauge/taiko "getgauge/taiko: A node.js library to automate chrome/chromium browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">console</span></p>

REPLでChromeを操作するコードを実行していき、その操作内容をコードで出力できるツール。
出力されたコードを使って操作を再現することができる。


----

## intoli/user-agents: A JavaScript library for generating random user agents with data that's updated daily.
[github.com/intoli/user-agents](https://github.com/intoli/user-agents "intoli/user-agents: A JavaScript library for generating random user agents with data that's updated daily.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

任意のUA(User Agent)を生成するライブラリ。
モバイルや特定の範囲のUAなどを指定して生成もできる。


----

## SamVerschueren/tsd-check: Check TypeScript type definitions
[github.com/SamVerschueren/tsd-check](https://github.com/SamVerschueren/tsd-check "SamVerschueren/tsd-check: Check TypeScript type definitions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

TypeScriptの型定義チェックライブラリ。 Genericsを使ったassertionのように利用できる。


----
