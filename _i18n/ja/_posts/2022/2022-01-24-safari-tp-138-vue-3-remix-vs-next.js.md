---
title: "2022-01-24のJS: Safari TP 138、Vue 3のデフォルト化、Remix vs Next.js"
author: "azu"
layout: post
date : 2022-01-24T11:20:56.215Z
category: JSer
tags:
- node.js
- React
- npm
- HTTP
- GraphQL

---

JSer.info #576

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v0.25.0 · axios/axios
[github.com/axios/axios/releases/tag/v0.25.0](https://github.com/axios/axios/releases/tag/v0.25.0 "Release v0.25.0 · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

axios 0.25.0リリース。


----

## Node v17.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.4.0/](https://nodejs.org/en/blog/release/v17.4.0/ "Node v17.4.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.4.0リリース。
EventEmitterとAsyncResourceを連携する`EventEmitterAsyncResource`を追加、ReadableStreamに`map`と`filter`を追加など

- [addaleax/eventemitter-asyncresource: AsyncResource integration for EventEmitter](https://github.com/addaleax/eventemitter-asyncresource "addaleax/eventemitter-asyncresource: AsyncResource integration for EventEmitter")

----

## Announcing React Native 0.67 · React Native
[reactnative.dev/blog/2022/01/19/version-067](https://reactnative.dev/blog/2022/01/19/version-067 "Announcing React Native 0.67 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.67リリース。
`DatePickerAndroid`の削除、Hermes 0.9.0へアップデートなど


----

## Deno 1.18 Release Notes
[deno.com/blog/v1.18](https://deno.com/blog/v1.18 "Deno 1.18 Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.18リリース。
Web Cryptography APIの実装、`deno.json`を自動で参照するように、Error Causeをスタックトレースに反映。
`Deno.test`のstep APIがstableに、FFI APIの改善、V8 snapshotsの圧縮方法をV8 zlibからlzとzstdに変更して起動速度の改善など


----

## Release Notes for Safari Technology Preview 138 | WebKit
[webkit.org/blog/12176/release-notes-for-safari-technology-preview-138/](https://webkit.org/blog/12176/release-notes-for-safari-technology-preview-138/ "Release Notes for Safari Technology Preview 138 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 138リリース。
`:focus-visible`、Media Queryの`resolution`、CSS Containmentをデフォルトで有効化。
Service Workerの`NavigationPreloadManager`を有効化、Service Workerを経由したファイルダウンロードをサポートなど


----

## Vue 3 as the New Default | The Vue Point
[blog.vuejs.org/posts/vue-3-as-the-new-default.html](https://blog.vuejs.org/posts/vue-3-as-the-new-default.html "Vue 3 as the New Default | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

2022年2月7日にVue 3が`vue@next`から`vue@latest`へと変更され、`vue`パッケージのStableバージョンとなる。
この変更に合わせてCDNでのlastestの参照先、ドキュメント、GitHubリポジトリも変更される。


----

## Release v5.67.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.67.0](https://github.com/webpack/webpack/releases/tag/v5.67.0 "Release v5.67.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5.67.0リリース。
AssertModuleに`outputPath`オプションの追加。
`output.trustedTypes: true`の場合は`eval-source-map`でもTrusted Typesに対応したコードを出力するようになど


----

## Announcing TypeScript 4.6 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6-beta/ "Announcing TypeScript 4.6 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.6 Betaリリース。
型推論の改善がメインとなっている。再帰型、インターフェースへのインデックスアクセス、関数の引数における型推論の改善。
`checkJs`が有効時に、JavaScriptの構文エラーのチェックを改善。
`--generateTrace`で出力できるビルドのトレースデータを分析するための`@typescript/analyze-trace`パッケージの公開など

- [@typescript/analyze-trace - npm](https://www.npmjs.com/package/@typescript/analyze-trace "@typescript/analyze-trace - npm")

----
<h1 class="site-genre">アーティクル</h1>

----

## npm: A Free Guide for Beginners | CSS-Tricks - CSS-Tricks
[css-tricks.com/a-complete-beginners-guide-to-npm/](https://css-tricks.com/a-complete-beginners-guide-to-npm/ "npm: A Free Guide for Beginners | CSS-Tricks - CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">tutorial</span></p>

npmとは何か、基本的な使い方についての連載記事


----

## Remix vs Next.js | Remix
[remix.run/blog/remix-vs-next](https://remix.run/blog/remix-vs-next "Remix vs Next.js | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Next.jsのEコマースを例に、RemixとNext.jsを比較した記事。
アーキテクチャの違い、CDN Edgeでの実行、データの更新についての比較など


----

## Mocking With Undici Like a Pro
[fusebit.io/blog/undici-mocking/](https://fusebit.io/blog/undici-mocking/ "Mocking With Undici Like a Pro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js向けのHTTPクライアントのUndiciのモックサポートについての記事。
`MockAgent`使ったモックについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## WebAppPentestGuidelines/graphQLGuideLine
[github.com/WebAppPentestGuidelines/graphQLGuideLine](https://github.com/WebAppPentestGuidelines/graphQLGuideLine "WebAppPentestGuidelines/graphQLGuideLine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

GraphQLにおける脆弱性の診断ガイド。
よくある問題としてIntrospection Queryが有効となっているケース、DoSとなるクエリ、レースコンディションなどについて解説している。
また診断や調査に使えるツールの紹介など


----

## Vanilla List • The Vanilla JavaScript Repository
[vanillalist.top/](https://vanillalist.top/ "Vanilla List • The Vanilla JavaScript Repository")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

依存がないライブラリのまとめサイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mo.js
[mojs.github.io/](https://mojs.github.io/ "mo.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

図形の描画とアニメーションのライブラリ


----

## tinyplex/tinybase: A tiny, reactive JavaScript library for structured state and tabular data.
[github.com/tinyplex/tinybase](https://github.com/tinyplex/tinybase "tinyplex/tinybase: A tiny, reactive JavaScript library for structured state and tabular data.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">database</span> <span class="jser-tag">library</span></p>

テーブル的なデータ構造の状態管理ライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Structure and Interpretation of Computer Programs | The MIT Press
[mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1](https://mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1 "Structure and Interpretation of Computer Programs | The MIT Press")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">book</span></p>

2022年4月 発売
SICPのJavaScript版

- [sicp.comp.nus.edu.sg/](https://sicp.comp.nus.edu.sg/ "sicp.comp.nus.edu.sg/")

----
