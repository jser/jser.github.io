---
title: "2018-10-02のJS: Cypress正式リリース、TypeScript 3.1、Parcel 1.10.0、Vue 3.0のロードマップ"
author: "azu"
layout: post
date : 2018-10-02T00:53:18.850Z
category: JSer
tags:
- cypress
- TypeSript
- parcel
- Vue

---

JSer.info #403 - E2Eテストフレームワーク/サービスの[Cypress](https://www.cypress.io/)が正式リリースされました

- [We're officially out of beta!](https://www.cypress.io/blog/2018/09/20/cypress-is-officially-out-of-beta/#)

Public Betaのときと同じく[Test Runner](https://github.com/cypress-io/cypress)はOSSのMITライセンスで、[Dashboardサービス](https://www.cypress.io/dashboard/)はOSSや公開プロジェクトなら無料、プライベートプロジェクトは有料となっています。

現在はChromeまたはElectronのみでテストが実行されますが、今後はIE11を含むクロスプラウザでのテストやGitHub連携、ネットワークProxyなどをサポートする予定です。

----

TypeScript 3.1がリリースされました。

- [Announcing TypeScript 3.1 | TypeScript](https://blogs.msdn.microsoft.com/typescript/announcing-typescript-3-1/)
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-31)

Mapped Typeの挙動がTupleにおいて変更され、Tuple Typeがより型付けしやすくなっています。

- [TypeScript 3.1 の Mapped Tuple Typeについて - Qiita](https://qiita.com/Quramy/items/c596b1bacf591da545b2)

`namespace`を使わずに関数へプロパティ追加できるように、TypeScriptのバージョンごとに型定義ファイルを指定して配布できる`typesVersions`フィールドのサポートが追加されています。

またLanguage Serviceでは`then`をAsync/Awaitへリファクタリングできるようになるといった変更が追加されています。

----

Vueの次のメジャーアップデートであるVue 3.0のロードマップが公開されました。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Just announced plans for Vue 3.0 at <a href="https://twitter.com/vue_london?ref_src=twsrc%5Etfw">@vue_london</a> - sorry the slides were a bit rough, full writeup coming next week.</p>&mdash; Evan You (@youyuxi) <a href="https://twitter.com/youyuxi/status/1043188361073176576?ref_src=twsrc%5Etfw">September 21, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

- [Plans for the Next Iteration of Vue.js – The Vue Point – Medium](https://medium.com/the-vue-point/plans-for-the-next-iteration-of-vue-js-777ffea6fabf)
- [\[和訳\] 次期 Vue (v3.0) の計画 / Plans for the Next Iteration of Vue.js - Qiita](https://qiita.com/unecochan/items/ac206365745257d68926)

この記事ではVue 3で行われる変更予定や追加機能などについてかかれています。
Vue自体のコードベースをTypeSriptに書き直し、クラスベースコンポーネントの導入、[Functional Component](https://jp.vuejs.org/v2/guide/render-function.html#%E9%96%A2%E6%95%B0%E5%9E%8B%E3%82%B3%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%8D%E3%83%B3%E3%83%88)がただの関数として書けるようになり、Observer/Schedulerの分離、ES Proxyベースのobserverの導入などについて書かれています。

またProxyを使えないIE11も制限ありでサポートする予定ですが、`Object.defineProperty`を使った2.xと同じ仕組みであるため、他のブラウザと完全な互換性を提供することが難しい点についても書かれています。

注釈: `Object.defineProperty`でgetter/setterを使い変更を検知する仕組みでは、オブジェクト作成時にないプロパティの変更を検知できない問題があります。一方Proxyはオブジェクト作成時にないプロパティ名に対する代入なども検知できます。
この点はMobX 4.xと5.xに類似する話だと思います。

- [mobx/CHANGELOG.md at 5.0.0 · mobxjs/mobx](https://github.com/mobxjs/mobx/blob/5.0.0/CHANGELOG.md)
- [MobX 5.0.0 について - console.lealog();](https://lealog.hateblo.jp/entry/2018/06/08/105219)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## We're officially out of beta!
[www.cypress.io/blog/2018/09/20/cypress-is-officially-out-of-beta/](https://www.cypress.io/blog/2018/09/20/cypress-is-officially-out-of-beta/ "We're officially out of beta!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cypressが正式リリース。
今後のロードマップとして、IE11を含むクロスブラウザ、Flakyテストを見つけるためのリトライと分析、GitHub連携などを予定している


----

## 📦 Parcel v1.10.0 — Babel 7, Flow, Elm, and more! 🚀
[medium.com/@devongovett/parcel-v1-10-0-babel-7-flow-elm-and-more-c20736553573](https://medium.com/@devongovett/parcel-v1-10-0-babel-7-flow-elm-and-more-c20736553573 "📦 Parcel v1.10.0 — Babel 7, Flow, Elm, and more! 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel 1.10.0リリース。
Babel 7、Flowの自動検出、Elm対応、インライン`<script>`と`<style>`の対応、HTMLのimportに対応など


----

## husky/CHANGELOG.md at master · typicode/husky
[github.com/typicode/husky/blob/master/CHANGELOG.md#100](https://github.com/typicode/husky/blob/master/CHANGELOG.md#100 "husky/CHANGELOG.md at master · typicode/husky")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Git Hook管理ツールであるHusky 1.0.0リリース。
Node.js 4のサポート終了、`scripts`フィールドから`husky`フィールドへ設定を移行、`.huskyrc`のサポートなど。
マイグレーションは`husky-upgrade`コマンドで行える


----

## Release Notes for Safari Technology Preview 66 | WebKit
[webkit.org/blog/8414/release-notes-for-safari-technology-preview-66/](https://webkit.org/blog/8414/release-notes-for-safari-technology-preview-66/ "Release Notes for Safari Technology Preview 66 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 66リリース。
Web Share API、CSS Conic Gradientsのサポート。
実験的にWebRTC Unified Plan、Media Capabilities APIをサポートなど


----

## SystemJS 2.0.0 Release
[guybedford.com/systemjs-2.0](https://guybedford.com/systemjs-2.0 "SystemJS 2.0.0 Release")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span> <span class="jser-tag">module</span></p>

SystemJS 2.0.0リリース。 `s.js`でレガシーブラウザのサポート、`system.js`で新しいProposalや仕様などをサポートする方針。 Package Name MapsやWeb Assembly Integrationなどの実装など


----

## Release Inferno v6.0.0-rc.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v6.0.0-rc.0](https://github.com/infernojs/inferno/releases/tag/v6.0.0-rc.0 "Release Inferno v6.0.0-rc.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v6.0.0-rc.0リリース。
Fragmentsのサポート、`getDerivedStateFromProps`と`getSnapshotBeforeUpdate`のライフサイクルイベントをサポートなど


----

## ECMAScript proposal updates @ 2018-09 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2018/10/01/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2018/10/01/ecmascript-proposal-updates "ECMAScript proposal updates @ 2018-09 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2018年9月に行われたTC39ミーティングで変更があったECMAScriptのProposalのまとめ。
`JSON.parse`の拡張Proposalの追加、Temporal(Dates and Times)がStage 2になるなど


----

## Release 1.0.0 · basecamp/trix
[github.com/basecamp/trix/releases/tag/1.0.0](https://github.com/basecamp/trix/releases/tag/1.0.0 "Release 1.0.0 · basecamp/trix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Basecampが作成しているリッチエディタのtrix 1.0.0がリリースされた。

- [Trix: A rich text editor for everyday writing](https://trix-editor.org/ "Trix: A rich text editor for everyday writing")

----

## Announcing TypeScript 3.1 | TypeScript
[blogs.msdn.microsoft.com/typescript/announcing-typescript-3-1/](https://blogs.msdn.microsoft.com/typescript/announcing-typescript-3-1/ "Announcing TypeScript 3.1 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.1リリース。
Mapped Tuple Type、namespaceを使わずに関数へプロパティ追加できるように、TypeScriptのバージョンごとに型を配布できる`typesVersions`フィールドをサポート。
`then`をAsync/Awaitへリファクタリングできるようになるなど

- [TypeScript 3.1 の Mapped Tuple Typeについて - Qiita](https://qiita.com/Quramy/items/c596b1bacf591da545b2 "TypeScript 3.1 の Mapped Tuple Typeについて - Qiita")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-31 "Breaking Changes · Microsoft/TypeScript Wiki")

----

## nw/node-release-lines: API for Node.js release metadata
[github.com/nw/node-release-lines](https://github.com/nw/node-release-lines "nw/node-release-lines: API for Node.js release metadata")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsのリリース情報を取得できるライブラリ。
LTSのバージョンやEOLなバージョンの取得、バージョンごとの状態を取得などができる


----

## Release Notes for Safari Technology Preview 66 | WebKit
[webkit.org/blog/8414/release-notes-for-safari-technology-preview-66/](https://webkit.org/blog/8414/release-notes-for-safari-technology-preview-66/ "Release Notes for Safari Technology Preview 66 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">safari</span></p>

Safari Technology Preview 66リリース。 Web Share API、CSS Conic Gradientsのサポート。 試験的にWebRTC Unified Plan、Media Capabilities APIをサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## What's New in Vue Devtools 5.0 Beta
[www.telerik.com/blogs/whats-new-in-vue-devtools-5-beta](https://www.telerik.com/blogs/whats-new-in-vue-devtools-5-beta "What's New in Vue Devtools 5.0 Beta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">debug</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span></p>

Vue DevTools 5.0βについて。
Routing Tab、Performance Tab、Settings Tab、VuexのStateの編集機能について

- [Release v5.0.0-beta.1 · vuejs/vue-devtools](https://github.com/vuejs/vue-devtools/releases/tag/v5.0.0-beta.1 "Release v5.0.0-beta.1 · vuejs/vue-devtools")

----

## Payment Request API: 統合ガイド  |  Web  |  Google Developers
[developers.google.com/web/fundamentals/payments/](https://developers.google.com/web/fundamentals/payments/ "Payment Request API: 統合ガイド  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

Payment Request APIについての記事。
Payment Request APIを使った取引のプロセス、APIの使い方、Feature Detectの方法などについて


----

## Node.jsでのイベントループの仕組みとタイマーについて - 技術探し
[blog.hiroppy.me/entry/nodejs-event-loop](https://blog.hiroppy.me/entry/nodejs-event-loop "Node.jsでのイベントループの仕組みとタイマーについて - 技術探し")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsのイベントループのフェーズについての解説。
Node.js/V8 ではどのようにイベントループを回しているかについて


----

## JavaScript typeof – LogRocket
[blog.logrocket.com/javascript-typeof-2511d53a1a62](https://blog.logrocket.com/javascript-typeof-2511d53a1a62 "JavaScript typeof – LogRocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptの`typeof`を使ったデータ型のチェックについて。
またプリミティブ型とWrapper objectについて


----

## The Importance Of Manual Accessibility Testing — Smashing Magazine
[www.smashingmagazine.com/2018/09/importance-manual-accessibility-testing/](https://www.smashingmagazine.com/2018/09/importance-manual-accessibility-testing/ "The Importance Of Manual Accessibility Testing — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

アクセシビリティの手動テストや自動テスト関するリソースを紹介している記事


----

## turtleDB: A JavaScript Framework for building offline-first, collaborative web apps
[hackernoon.com/turtledb-a-javascript-framework-for-building-offline-first-collaborative-web-apps-7183cd787163](https://hackernoon.com/turtledb-a-javascript-framework-for-building-offline-first-collaborative-web-apps-7183cd787163 "turtleDB: A JavaScript Framework for building offline-first, collaborative web apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">データベース</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

Offline-FirstなデータベースライブラリのturtleDBについて。
クライアント側はIndexedDBでローカルに保存でき、サーバ側はMongoDBなどのアダプタとして動作する。オフラインではクライアントに保存でき、オンラインでは同期ができるような仕組み

- [turtle-DB/turtleDB: Official turtleDB project](https://github.com/turtle-DB/turtleDB "turtle-DB/turtleDB: Official turtleDB project")

----

## Plans for the Next Iteration of Vue.js – The Vue Point – Medium
[medium.com/the-vue-point/plans-for-the-next-iteration-of-vue-js-777ffea6fabf](https://medium.com/the-vue-point/plans-for-the-next-iteration-of-vue-js-777ffea6fabf "Plans for the Next Iteration of Vue.js – The Vue Point – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

Vue 3.0のロードマップについて。 クラスベースコンポーネント、Functional Component、コードベースをTypeSript化、Observer/Schedulerの分離、ES Proxyベースのobserverについて。 またProxyを使えないIE11も制限ありでサポート予定。

- [\[和訳\] 次期 Vue (v3.0) の計画 / Plans for the Next Iteration of Vue.js - Qiita](https://qiita.com/unecochan/items/ac206365745257d68926 "\[和訳\] 次期 Vue (v3.0) の計画 / Plans for the Next Iteration of Vue.js - Qiita")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Array - 30 seconds of code
[30secondsofcode.org/](https://30secondsofcode.org/ "Array - 30 seconds of code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

JavaScriptのコードスニペット集。
典型的な処理のスニペットをまとめている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Leko/hothouse: Continuous dependency update for Node.js project
[github.com/Leko/hothouse](https://github.com/Leko/hothouse "Leko/hothouse: Continuous dependency update for Node.js project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">yarn</span> <span class="jser-tag">github</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npmtとyarnに対応しているGreenkeeperのような依存パッケージの更新PRを出してくれるツール


----
