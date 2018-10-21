---
title: "2018-10-21のJS: Chrome 70、Angular 7、LoopBack 4 GA"
author: "azu"
layout: post
date : 2018-10-21T14:10:58.305Z
category: JSer
tags:
- chrome
- angular
- LoopBack


---

JSer.info #406 - Chrome 70がリリースされました。

- [New in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/10/nic70 "New in Chrome 70  |  Web  |  Google Developers")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D70 "Chrome Platform Status")
- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
- [Deprecations and removals in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/09/chrome-70-deps-rems "Deprecations and removals in Chrome 70  |  Web  |  Google Developers")

[Desktop PWA](https://developers.google.com/web/progressive-web-apps/desktop)でWindowsとLinuxのサポートが追加されました。macOSはChrome 72でサポートされる予定です。

Credential Management APIで指紋認証をサポート、Web Workerで`name`オプション、TLS 1.3のサポート。 Web Components v0を非推奨化などが行われています。
また、Chrome 70から`http://`なサイトフォームなどに入力した際に赤色の"Not Secure"警告がでるようになりました。

- [Chromium Blog: Evolving Chrome's security indicators](https://blog.chromium.org/2018/05/evolving-chromes-security-indicators.html)

----

Angular 7がリリースされました。

- [Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more](https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#700-2018-10-18)

TypeScript 3.1のサポート、Virtual Scrollingの対応、CDKでDrag and Dropのサポートされています。また開発時だけに必要な`reflect-metadata`はproductionビルドから自動的に取り除かれるようになっています。

----

Node.jsのAPIフレームワークの[LoopBack 4](https://v4.loopback.io/) GA (General Availability)がリリースされています。

- [StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!](https://strongloop.com/strongblog/loopback-4-ga)

コアがTypeScriptで書き直されているため型周りが全体的に改善されています。

- [strongloop/loopback-next: LoopBack makes it easy to build modern API applications that require complex integrations.](https://github.com/strongloop/loopback-next)

`lb4 openapi`コマンドでOpenAPI形式への出力対応しています。
またLTSポリシーも合わせて更新され、LoopBack 4は2021年4月までサポートされる予定となっています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Chrome 70  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/10/nic70](https://developers.google.com/web/updates/2018/10/nic70 "New in Chrome 70  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 70リリース。
Desktop PWA(Windows)のサポート、Credential Management APIで指紋認証をサポート、Web Workerで`name`オプション、TLS 1.3のサポート。 Web Components v0を非推奨化など

- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D70 "Chrome Platform Status")
- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
- [Deprecations and removals in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/09/chrome-70-deps-rems "Deprecations and removals in Chrome 70  |  Web  |  Google Developers")

----

## Release 7.0.2 · zeit/next.js
[github.com/zeit/next.js/releases/tag/7.0.2](https://github.com/zeit/next.js/releases/tag/7.0.2 "Release 7.0.2 · zeit/next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 7.0.2リリース。
7.0.0と7.0.1にあったエラー画面でのXSSが修正された。


----

## Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more
[blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c](https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c "Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 7リリース。
TypeScript 3.1のサポート、Virtual Scrollingの対応、CDKでDrag and Dropのサポート。
`reflect-metadata`がproductionビルドに誤って含まれるケースを防止する改善など

- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#700-2018-10-18 "angular/CHANGELOG.md at master · angular/angular")
- [Angular 7リリースノート – Angular Blog日本語訳 | maesblog](https://mae.chab.in/archives/60226 "Angular 7リリースノート – Angular Blog日本語訳 | maesblog")

----

## StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!
[strongloop.com/strongblog/loopback-4-ga](https://strongloop.com/strongblog/loopback-4-ga "StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js APIフレームワークのLoopBack 4GAリリース。
コアがTypeScriptで書き直され、OpenAPI形式への出力対応。
LTSポリシーも合わせて更新され、LoopBack 4は2021年4月までサポートされる予定。

- [LoopBack 4](https://v4.loopback.io/ "LoopBack 4")

----
<h1 class="site-genre">アーティクル</h1>

----

## Node.jsにおけるプロトタイプ汚染攻撃とは何か - ぼちぼち日記
[jovi0608.hatenablog.com/entry/2018/10/19/083725](https://jovi0608.hatenablog.com/entry/2018/10/19/083725 "Node.jsにおけるプロトタイプ汚染攻撃とは何か - ぼちぼち日記")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Prototype pollutionについて。
オブジェクトをマージする際などに`__proto__`プロパティによって意図しない書き換えが行われる問題について


----

## Angular 4アプリケーションをAngular 6に移行する | 株式会社カブク
[www.kabuku.co.jp/developers/migration-from-ng4-to-ng6](https://www.kabuku.co.jp/developers/migration-from-ng4-to-ng6 "Angular 4アプリケーションをAngular 6に移行する | 株式会社カブク")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 4.xから6.xへの移行方法について。
Angular 4のLTSが2018年9月で終了するため、6.xへどのように移行するかについて。
移行した結果ビルド時間やファイルサイズが改善されたことについて


----

## On the Roadmap: Exact Objects by Default – Flow – Medium
[medium.com/flow-type/on-the-roadmap-exact-objects-by-default-16b72933c5cf](https://medium.com/flow-type/on-the-roadmap-exact-objects-by-default-16b72933c5cf "On the Roadmap: Exact Objects by Default – Flow – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">flowtype</span></p>

Flow 0.84.0からExact Objects（`{| |}`相当）がデフォルトになる変更予定について。 その他のプロパティを許可する新しい構文として`{foo: number, ...}`を導入し、どのようにマイグレーションしていくかについて


----

## Re-ducksパターン：React + Redux のディレクトリ構成ベストプラクティス
[noah.plus/blog/021/](https://noah.plus/blog/021/ "Re-ducksパターン：React + Redux のディレクトリ構成ベストプラクティス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">redux</span></p>

Reduxの文脈で見るDucksパターンとRe-ducksパターンについて。 ファイルディレクトリ構造をどのようなルールにするかやそれによって解決できることについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## マークアップをパワーアップするWAI-ARIA
[masup9.github.io/dist23/#/](https://masup9.github.io/dist23/#/ "マークアップをパワーアップするWAI-ARIA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">slide</span></p>

WAI-AIRAの目的、使い方、ユースケースについて解説しているスライド。
role、ステート、プロパティを付与したときにウェブブラウザやアクセシビリティの支援技術に伝わるかについて。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Gridsome - Build blazing fast websites with Vue.js and GraphQL
[gridsome.org/](https://gridsome.org/ "Gridsome - Build blazing fast websites with Vue.js and GraphQL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

VueとGraphQLを使った静的サイトツール/フレームワーク。
Gatsby.jsインスパイアなフレームワークでGraphQL経由レイヤーを経由してデータソースにアクセスする。


----

## perf-tools/timekeeper at master · artifact-project/perf-tools
[github.com/artifact-project/perf-tools/tree/master/timekeeper](https://github.com/artifact-project/perf-tools/tree/master/timekeeper "perf-tools/timekeeper at master · artifact-project/perf-tools")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

指定区間の時間計測結果をコンソールやパフォーマンスタブ(Performance Timing API)に出力できるライブラリ


----

## nico3333fr/CSP-useful: Collection of scripts, thoughts about CSP (Content Security Policy)
[github.com/nico3333fr/CSP-useful](https://github.com/nico3333fr/CSP-useful "nico3333fr/CSP-useful: Collection of scripts, thoughts about CSP (Content Security Policy)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

CSPレポートのサンプルやノイズになってるCSPレポートなどについてまとめてるリポジトリ。またCSPのTipsやユースケースについて書かれている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## terkelg/zet: Set() as it should be
[github.com/terkelg/zet](https://github.com/terkelg/zet "terkelg/zet: Set() as it should be")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`Set`を使った和集合、積集合などの演算をサポートしたライブラリ。
`Set`同士の集合演算を行う`Set`のサブクラスライブラリ


----

## f/graphql.js: A Simple and Isomorphic GraphQL Client for JavaScript
[github.com/f/graphql.js](https://github.com/f/graphql.js "f/graphql.js: A Simple and Isomorphic GraphQL Client for JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

IsomorphicなGraphQLクライアントライブラリ


----

## segmentio/evergreen: 🌲 Evergreen React UI Framework by Segment
[github.com/segmentio/evergreen/](https://github.com/segmentio/evergreen/ "segmentio/evergreen: 🌲 Evergreen React UI Framework by Segment")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

SegmentによるReact UIフレームワーク


----

## Tencent/omi: Next generation web framework in 4kb JavaScript (Web Components + JSX + Proxy + Store + Path Updating)
[github.com/Tencent/omi](https://github.com/Tencent/omi "Tencent/omi: Next generation web framework in 4kb JavaScript (Web Components + JSX + Proxy + Store + Path Updating)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Web Componentsをベースにしたフレームワーク。
JSXのサポート、ES Proxyを使った変更検知、Shadow DOMを使ったScoped CSSなど持っている


----
