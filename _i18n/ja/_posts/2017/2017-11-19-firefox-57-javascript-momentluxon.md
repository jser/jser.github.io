---
title: "2017-11-19のJS: Firefox 57、JavaScriptのコスト、momentとLuxon"
author: "azu"
layout: post
date : 2017-11-19T10:51:22.569Z
category: JSer
tags:
- Firefox
- Performance
- Date
- Moment
- i18n

---

JSer.info #358 - Firefox 57がリリースされました。

- [Firefox — Notes (57.0) — Mozilla](https://www.mozilla.org/en-US/firefox/57.0/releasenotes/)
- [Introducing the New Firefox: Firefox Quantum - The Mozilla Blog](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/)

[Project Quantum](https://medium.com/mozilla-tech/a-quantum-leap-for-the-web-a3b7174b3c12 "Project Quantum")と呼ばれていたFirefoxの大規模書き換えの初回のリリースとなっています。
新たに書き直されたQuantum CSS(Stylo)と呼ばれるCSSエンジンが含まれるリリースであるため、既存のCSSとの挙動にさまざまな違い(バグ修正も含む)があります。

詳しくは次の記事を読むと良さそうです。

- [Inside a super fast CSS engine: Quantum CSS (aka Stylo) – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/08/inside-a-super-fast-css-engine-quantum-css-aka-stylo/ "Inside a super fast CSS engine: Quantum CSS (aka Stylo) – Mozilla Hacks – the Web developer blog")
- [Firefox Quantum 57 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/57 "Firefox Quantum 57 for developers - Mozilla | MDN")

`PerformanceObserver`の有効化、Fetchのabortを行える[AbortController](https://developer.mozilla.org/ja/docs/Web/API/AbortController "AbortController")に対応しています。
また、WindowsのFirefoxにおいてデフォルトのフォントが変更されています。

- [日本語の既定フォントが変更されました | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2017/japanese-default-fonts-have-been-changed/ "日本語の既定フォントが変更されました | Firefox サイト互換性情報")

----

[The Cost Of JavaScript – Dev Channel – Medium](https://medium.com/dev-channel/the-cost-of-javascript-84009f51e99e "The Cost Of JavaScript – Dev Channel – Medium")という記事ではJavaScriptのコストについて書かれています。

JavaScriptのコストとはネットワークからのロード、パース、コンパイル、実行から構成されています。
このパースとコンパイルが低スペックのデバイスでは大きな割合となることがあります。
そのため、同じサイズのJavaScriptと画像ファイルでは、実行 or 描画までの時間は異なります。

これらのコストについての解説や対策方法の一つとしてのPRPLパターンやPerformance Budgetについて書かれています。

----

[moment/luxon: A library for working with dates and times in JS](https://github.com/moment/luxon "moment/luxon: A library for working with dates and times in JS")という日付周りのライブラリがαリリースされています。

元々、[moment](https://github.com/moment/moment "moment")-labプロジェクトから始まったライブラリで、momentの問題点である[mutable](https://github.com/moment/moment-rfcs/pull/2)である点などを解決しています。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Wondering about the future of Moment, modularization, etc? We have what we&#39;ll call a &#39;moment-labs&#39; project here: <a href="https://t.co/tFxIq9lEjm">https://t.co/tFxIq9lEjm</a></p>&mdash; moment.js (@momentjs) <a href="https://twitter.com/momentjs/status/918264220663214081?ref_src=twsrc%5Etfw">October 11, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Want a smaller, immutable date library for modern browsers? Luxon has officially joined the family! <a href="https://t.co/HSjRuRuZG1">https://t.co/HSjRuRuZG1</a></p>&mdash; moment.js (@momentjs) <a href="https://twitter.com/momentjs/status/923982141704192000?ref_src=twsrc%5Etfw">October 27, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

[For Moment users](https://moment.github.io/luxon/docs/manual/faq/moment.html "For Moment users")にも書かれていますが、MomentとAPIの互換性はありません。

特徴としては、日付/時間/インターバルの操作/パース/フォーマットを行うことができ、momentとは異なりImmutableなAPIとなっています。また、ECMA i18n APIを使ったTimeZoneやIntlを使った国際化に対応しています。

そして、LuxonはネイティブのDate、Moment、Date-fnsとは異なりmonthを`1-indexed`な値として扱います。

```js
// 2017-01-01
const date20170101 = new Date("2017-01-01T00:00:00.000Z");
// Luxon - 1-index
const { DateTime }  = require('luxon');
console.log("Luxon:get:" + DateTime.fromJSDate(date20170101).month); // => 1
console.log("Luxon:set:" + DateTime.fromJSDate(date20170101).set({ month: 1 }).month); // => 1
// date-fns - 0-indexed
const {getMonth, setMonth} = require('date-fns');
console.log("date-fns:get:"+ getMonth(date20170101)); // => 0
console.log("date-fns:set:"+ getMonth(setMonth(new Date(2017, 1, 1), 0))); // => 0
// moment - 0-indexed
const moment = require('moment');
console.log("moment:get:"+ moment(date20170101).month()); // => 0
console.log("moment:set:"+ moment(date20170101).month(0).month()); // => 0
```

- [Luxon - data-fns - moment | RunKit](https://runkit.com/azu/5a117a65dcefad0012187983 "Luxon - data-fns - moment | RunKit")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v0.59.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.59.0](https://github.com/facebook/flow/releases/tag/v0.59.0 "Release v0.59.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.59.0リリース。
`$ReadOnly<T>` utility typeの追加、パフォーマンスの改善、`/* flowlint sketchy-null:error */`のようなコメントでLintを有効化できるように


----

## Node v9.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v9.2.0/](https://nodejs.org/en/blog/release/v9.2.0/ "Node v9.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 9.2.0リリース。
`fs.realpathSync.native`、`fs.realpath.native`、`process.ppid`がexposeされた


----

## Release Notes for Safari Technology Preview 44 | WebKit
[webkit.org/blog/8035/release-notes-for-safari-technology-preview-44/](https://webkit.org/blog/8035/release-notes-for-safari-technology-preview-44/ "Release Notes for Safari Technology Preview 44 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 44リリース。
Payment Requestがデフォルトで有効化、`createImageBitmap()`の実装、OffscreenCanvasのIDLを追加など


----

## Introducing security alerts on GitHub
[github.com/blog/2470-introducing-security-alerts-on-github](https://github.com/blog/2470-introducing-security-alerts-on-github "Introducing security alerts on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">github</span> <span class="jser-tag">security</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ruby</span> <span class="jser-tag">news</span></p>

GitHubリポジトリにnpmやgemのセキュリティアラート機能が追加された。


----

## Release v4.0.0-beta.1 · reactjs/redux
[github.com/reactjs/redux/releases/tag/v4.0.0-beta.1](https://github.com/reactjs/redux/releases/tag/v4.0.0-beta.1 "Release v4.0.0-beta.1 · reactjs/redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Redux v4.0.0-beta.1リリース。
TypeScriptの更新、`INIT`をランダムな値に変更、IE11未満のサポートを終了、Dispatchのパフォーマンス改善など

- [Redux 4 breaking changes · Issue #1342 · reactjs/redux](https://github.com/reactjs/redux/issues/1342 "Redux 4 breaking changes · Issue #1342 · reactjs/redux")

----

## Firefox — Notes (57.0) — Mozilla
[www.mozilla.org/en-US/firefox/57.0/releasenotes/](https://www.mozilla.org/en-US/firefox/57.0/releasenotes/ "Firefox — Notes (57.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 57リリース。
CSSエンジンの書き直しが行われ挙動の変更とパフォーマンスの改善、`watch`/`unwatch`メソッドが非推奨化、`PerformanceObserver`の有効化、Fetchのabortに対応。
WebRTCの`RTCDataChannel`のメッセージファイルサイズを指定できるように

- [Introducing the New Firefox: Firefox Quantum - The Mozilla Blog](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/ "Introducing the New Firefox: Firefox Quantum - The Mozilla Blog")
- [Firefox Quantum 57 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/57 "Firefox Quantum 57 for developers - Mozilla | MDN")
- [Firefox 57 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/57/ "Firefox 57 サイト互換性情報 | Firefox サイト互換性情報")
- [Using WebRTC data channels - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels#Understanding_message_size_limits "Using WebRTC data channels - Web APIs | MDN")

----

## Release 2.6.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v2.6.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v2.6.0 "Release 2.6.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">ReleaseNote</span></p>

lighthouse 2.6.0リリース。
`redirects`などのチェックツールの追加。
各スクリプトの起動時間を計測する`bootup-time`、ページの実行時間を計測する`mainthread-work-breakdown`などのAuditを追加


----
<h1 class="site-genre">アーティクル</h1>

----

## Refactoring React Components with Jest’s Snapshot – Michael Romani – Medium
[medium.com/@mr4227/refactoring-react-components-with-jests-snapshot-7ed1b9d332cc](https://medium.com/@mr4227/refactoring-react-components-with-jests-snapshot-7ed1b9d332cc "Refactoring React Components with Jest’s Snapshot – Michael Romani – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jestのsnapshotテストを使ったReactコンポーネントのリファクタリングについての記事。
スナップショットを取ってから、でかいコンポーネントの細分化をテストしながら行う話


----

## How Redux Works: A Counter-Example
[daveceddia.com/how-does-redux-work/](https://daveceddia.com/how-does-redux-work/ "How Redux Works: A Counter-Example")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

Reduxでカウンターアプリを作りながらReduxの使い方や仕組みについてを学ぶチュートリアル。


----

## The Cost Of JavaScript – Dev Channel – Medium
[medium.com/dev-channel/the-cost-of-javascript-84009f51e99e](https://medium.com/dev-channel/the-cost-of-javascript-84009f51e99e "The Cost Of JavaScript – Dev Channel – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScriptの実行までのコストについてを解説した記事。
ダウンロード、パース、実行のステップを踏む。同じサイズのJSと画像のコストは異なる点。
PRPLパターン、Performance Budgetについて。


----

## JavaScript. The Core: 2nd Edition – ds.laboratory
[dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition/](http://dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition/ "JavaScript. The Core: 2nd Edition – ds.laboratory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript/JavaScriptにおける用語の定義やその概念の解説。
ECMAScriptの仕様に近いコアな内容。


----

## Clean Code vs. Dirty Code: React Best Practices - American Express Engineering Blog
[americanexpress.io/clean-code-dirty-code/](http://americanexpress.io/clean-code-dirty-code/ "Clean Code vs. Dirty Code: React Best Practices - American Express Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

Reactを題材にしたクリーンなコードについて。
ネーミングやコンポーネントの分割、デフォルト値の扱いなど良くない例とそれを改善した例を元に解説している。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## React Redux を用いた SPA 新規サービスを運用して得た知見と実装例 - ランサーズ（Lancers）エンジニアブログ
[engineer.blog.lancers.jp/2017/11/react-redux-spa-manage-tips/](https://engineer.blog.lancers.jp/2017/11/react-redux-spa-manage-tips/ "React Redux を用いた SPA 新規サービスを運用して得た知見と実装例 - ランサーズ（Lancers）エンジニアブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">slide</span> <span class="jser-tag">JavaScript</span></p>

React+Redux+Sagaを使ったプロジェクトについてのスライド。
ディレクトリ構成や基本的な処理の流れ、HOCを使ったコンポーネントの拡張、ダイアログやストレージへの保存などユースケース毎の実装方法について。
またテスト、Sentryを使ったエラー解析、SEO、APIの管理についてなどについて


----

## JS Kongress 2017 - YouTube
[www.youtube.com/playlist?list&#x3D;PL8ajgHZ7PoCt3l5RXoyqVu\_r7gYJU0dMx](http://www.youtube.com/playlist?list=PL8ajgHZ7PoCt3l5RXoyqVu_r7gYJU0dMx "JS Kongress 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

JS Kongress 2017の動画一覧

- [JS Kongress 2017 💻 - The Future of JavaScript, Nov 13-14 2017, Munich](https://2017.js-kongress.de/ "JS Kongress 2017 💻 - The Future of JavaScript, Nov 13-14 2017, Munich")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## What Web Can Do Today
[whatwebcando.today/](https://whatwebcando.today/ "What Web Can Do Today")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">browser</span></p>

アクセスしているブラウザでさまざまなWeb Platform APIが利用できるかを表示してくれるサイト


----

## \`performance.mark\` with metadata is useful for Real user monitoring
[dev.to/ben/we-welcome-a-wonderful-influx-of-new-members-from-japan-1k0](https://dev.to/ben/we-welcome-a-wonderful-influx-of-new-members-from-japan-1k0 "\`performance.mark\` with metadata is useful for Real user monitoring")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

`performance.mark`にメタデータとしてFPSを付加して計測して、ボトルネックになっている行動をログから解析、可視化する方法について

- [azu/performance-mark-metadata: \`performance.mark\` with custom meta data.](https://github.com/azu/performance-mark-metadata "azu/performance-mark-metadata: \&#x60;performance.mark\&#x60; with custom meta data.")
- [performance.markにメタデータを紐付けできるライブラリを書いた | Web Scratch](http://efcl.info/2017/11/15/performance.mark-metadata/ "performance.markにメタデータを紐付けできるライブラリを書いた | Web Scratch")

----

## stereobooster/react-snap: A zero-configuration static pre-renderer for Single Page Applications
[github.com/stereobooster/react-snap](https://github.com/stereobooster/react-snap "stereobooster/react-snap: A zero-configuration static pre-renderer for Single Page Applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

Reactをprerenderして静的なHTMLにできるライブラリ。
設定なしでcreate-react-appと協調して動作することを目標にしている。SSRで扱うことが難しい3rdパーティスクリプトやWebGLなどがオプションで対処できる。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## moment/luxon: A library for working with dates and times in JS
[github.com/moment/luxon](https://github.com/moment/luxon "moment/luxon: A library for working with dates and times in JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

日付や時間、インターバルを扱うライブラリ。 日付操作やパース、フォーマットを行える。Immutableであり、TimeZoneやIntlを使った国際化に対応している。 Momentとの違いをまとめたドキュメントも公開されている。


----

## jaredpalmer/react-fns: Browser API's turned into declarative React components and HoC's
[github.com/jaredpalmer/react-fns](https://github.com/jaredpalmer/react-fns "jaredpalmer/react-fns: Browser API's turned into declarative React components and HoC's")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

ReactのHigh Order Componentのコレクションライブラリ。
デバイスの回転や動作、オンライン/オフライン、Geo、メディアクエリー、スクロール、ロケールを扱えるコンポーネントなどが用意されている


----

## goto-bus-stop/tinyify: a browserify plugin that runs various optimizations, so you don't have to install them all manually. makes your bundles tiny!
[github.com/goto-bus-stop/tinyify](https://github.com/goto-bus-stop/tinyify "goto-bus-stop/tinyify: a browserify plugin that runs various optimizations, so you don't have to install them all manually. makes your bundles tiny!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">plugin</span> <span class="jser-tag">Tools</span></p>

Browserifyでフラットbundle、unassert、productionビルド、minifyなどをまとめて行うプラグイン


----

## jaredpalmer/razzle: ✨ Create server-rendered universal JavaScript applications with no configuration
[github.com/jaredpalmer/razzle](https://github.com/jaredpalmer/razzle "jaredpalmer/razzle: ✨ Create server-rendered universal JavaScript applications with no configuration")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">isomorphic</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

UniversalなJavaScriptアプリケーションを設定なしで書き始められる開発環境ツール。
`create-react-app`のようなツールだが、React以外でも利用できる。


----
<h1 class="site-genre">書籍関係</h1>

----

## Pure React
[daveceddia.com/pure-react/](https://daveceddia.com/pure-react/ "Pure React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

Reactについてステップバイステップで学べるサンプルを中心にした書籍。


----

## Manning | Vue.js in Action
[www.manning.com/books/vue-js-in-action](https://www.manning.com/books/vue-js-in-action "Manning | Vue.js in Action")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">book</span></p>

2018年5月30日発売
Vueについての書籍


----

## 超速！ Webページ速度改善ガイド ── 使いやすさは「速さ」から始まる（WEB+DB PRESS plusシリーズ）｜gihyo.jp … 技術評論社
[gihyo.jp/magazine/wdpress/plus/978-4-7741-9400-4](http://gihyo.jp/magazine/wdpress/plus/978-4-7741-9400-4 "超速！ Webページ速度改善ガイド ── 使いやすさは「速さ」から始まる（WEB+DB PRESS plusシリーズ）｜gihyo.jp … 技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

2017年11月23日発売
ウェブページのパフォーマンス改善についての書籍。
ネットワーク、レンダリング、スクリプトの項目ごとに測定方法や改善方法についてを解説する


----

## Manning | React Native in Action
[www.manning.com/books/react-native-in-action](https://www.manning.com/books/react-native-in-action "Manning | React Native in Action")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2018年4月30日発売
React Nativeについての書籍


----
