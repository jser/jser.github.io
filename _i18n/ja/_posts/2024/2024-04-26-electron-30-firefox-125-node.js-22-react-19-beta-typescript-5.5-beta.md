---
title: "2024-04-26のJS: Electron 30、Firefox 125、Node.js 22、React 19 Beta、TypeScript 5.5 Beta"
author: "azu"
layout: post
date: 2024-04-26T02:30:50.846Z
category: JSer
tags:
- React
- Electron
- Firefox
- JSON
- Tools

---

JSer.info #690 - Electron 30.0.0がリリースされました。

- [Electron 30.0.0 | Electron](https://www.electronjs.org/blog/electron-30-0)

V8 12.4、Chromium 124、Node.js 20.11.1へアップデート。
File System APIをサポート、Cross Origin iframeにPermission Policyを使うように変更、`WebContentsView`/`BaseWindow`の廃止などの変更が含まれています。

---

Firefox 125がリリースされました。

- [Firefox 125.0.1, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/125.0.1/releasenotes/)
- [Firefox 125 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/125)

`Intl.Segmenter`のサポート、Popover APIのサポート、AV1コーデックのサポート、WasmのMulti Memoryをサポートなどが追加されています。

---

Node.js 22がリリースされました。

- [Node.js — Node.js 22 is now available!](https://nodejs.org/en/blog/announcements/v22-release-announce)

Node.js 22.x は2024-10-29に[LTS](https://github.com/nodejs/release#release-schedule)となる予定のメジャーバージョンです。

V8 12.4へアップデート、`require()`でのESMモジュールのロードをサポートする`--experimental-require-module`フラグの追加が含まれています。
また、npm run-scriptを実行する`node --run <script>`を追加、`node --watch`フラグを追加、WebSocketをデフォルトで有効化、`node:fs`に`glob`の追加などが行われています。
そのほかには、StreamのHigh Water Markのデフォルト値を16KiBから64KiBへ変更なども行われています。

---

React 19 Betaがリリースされました。

- [React 19 Beta – React](https://react.dev/blog/2024/04/25/react-19)

Actionという概念の導入と`useActionState`/`useFormStatus`の追加されています。
楽観的な更新を扱う`useOptimistic`、Promiseをunwrapする`use`の追加されています。
Server Component/Server Actionのサポート、`fowardRef`が不要となるように変更なども行われています。

---

TypeScript 5.5 Betaがリリースされました。

- [Announcing TypeScript 5.5 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/)

関数からtype predicatesを推論できるようになり、`Array.prototype.filter`などでの絞り込みが簡潔に書けるようになっています。

- [The Making of a TypeScript Feature: Inferring Type Predicates](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/)

JSDocで`@import {foo} from "foo"`をサポート、正規表現の基本的な構文チェックをサポート、`isolatedDeclarations`をサポートが追加されています。
また、`out`や`target: ES3`などの非推奨となっていたオプションが無効化され、`ignoreDeprecations`オプションを指定しないと利用できなくなっています。



----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Electron 30.0.0 | Electron
[www.electronjs.org/blog/electron-30-0](https://www.electronjs.org/blog/electron-30-0 "Electron 30.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 30リリース。
V8 12.4、Chromium 124、Node.js 20.11.1へアップデート。
File System APIをサポート、Cross Origin iframeにPermission Policyを使うように変更、`WebContentsView`/`BaseWindow`の廃止など


----

## Firefox 125.0.1, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/125.0.1/releasenotes/](https://www.mozilla.org/en-US/firefox/125.0.1/releasenotes/ "Firefox 125.0.1, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 125リリース。
`Intl.Segmenter`のサポート、Popover APIのサポート、AV1コーデックのサポート、WasmのMulti Memoryをサポートなど

- [Firefox 125 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/125 "Firefox 125 for developers - Mozilla | MDN")
- [WebAssembly/multi-memory: Multiple per-module memories for Wasm](https://github.com/WebAssembly/multi-memory "WebAssembly/multi-memory: Multiple per-module memories for Wasm")

----

## Node.js — Node.js 22 is now available!
[nodejs.org/en/blog/announcements/v22-release-announce](https://nodejs.org/en/blog/announcements/v22-release-announce "Node.js — Node.js 22 is now available!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 22リリース。
V8 12.4へアップデート、`require()`でのESMモジュールのロードをサポートする`--experimental-require-module`フラグの追加。
npm run-scriptを実行する`node --run <script>`を追加、`node --watch`フラグを追加、WebSocketをデフォルトで有効化、`node:fs`に`glob`を追加。
StreamのHigh Water Markのデフォルト値を16KiBから64KiBへ変更。


----

## React Native 0.74 - Yoga 3.0, Bridgeless New Architecture, and more · React Native
[reactnative.dev/blog/2024/04/22/release-0.74](https://reactnative.dev/blog/2024/04/22/release-0.74 "React Native 0.74 - Yoga 3.0, Bridgeless New Architecture, and more · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.74リリース。
レイアウトエンジンであるYoga 3.0へアップグレート、Bridgelessがデフォルトに変更、`onLayout`でのStateの更新がバッチ化されるように。
Androidの最小SDKバージョンを23 (Android 6.0)に変更、PropTypesの削除など


----

## React 19 Beta – React
[react.dev/blog/2024/04/25/react-19](https://react.dev/blog/2024/04/25/react-19 "React 19 Beta – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 19 Betaリリース。
Actionという概念の導入と`useActionState`/`useFormStatus`の追加。
楽観的な更新を扱う`useOptimistic`、Promiseをunwrapする`use`の追加。
Server Component/Server Actionのサポート、`fowardRef`が不要となるように変更。
Hydrationのエラーの表示の改善、`<Context>`自体が`<Context.Provider>`としての機能を持つように変更、`ref`のcleanup処理を定義できるように。
`useDeferredValue`の第二引数に初期値をサポート、`<title>`などのメタデータタグのサポート、`<link ref=stylesheet>`でのスタイルシートのサポート。
`<script async={true}>`のサポート、`preload`などの`<link rel=preload>`を扱う関数を追加。
React 18ではサードパーティによってHTMLが改変されたときはHydration時にレンダリングし直すことで消えていたが、残るように変更、Custme Elementのサポートなど。


----

## Release Version 2.0.0 · quilljs/quill
[github.com/quilljs/quill/releases/tag/v2.0.0](https://github.com/quilljs/quill/releases/tag/v2.0.0 "Release Version 2.0.0 · quilljs/quill")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Quill 2.0リリース。
TypeScriptのビルトインサポート、`registry`の追加、ドキュメントモデルとの同期にInputEventを使うように変更。

- [Announcing Quill 2.0 - Knock Down Silos by Slab](https://slab.com/blog/announcing-quill-2-0/ "Announcing Quill 2.0 - Knock Down Silos by Slab")

----

## What’s new in Apollo Client 3.10 | Apollo GraphQL Blog
[www.apollographql.com/blog/whats-new-in-apollo-client-3-10](https://www.apollographql.com/blog/whats-new-in-apollo-client-3-10 "What’s new in Apollo Client 3.10 | Apollo GraphQL Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Apollo Client 3.10リリース。
`@apollo/client/testing/experimental`にMSWと連携してスキーマ駆動テストをする`createTestSchema`の追加、`client.watchFragment`の追加。
`createQueryPreloader`をStableに変更など

- [Release v3.10.0 · apollographql/apollo-client](https://github.com/apollographql/apollo-client/releases/tag/v3.10.0 "Release v3.10.0 · apollographql/apollo-client")

----

## Announcing TypeScript 5.5 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/ "Announcing TypeScript 5.5 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.5リリース。
関数からtype predicatesを推論できるようになり、`Array.prototype.filter`などでの絞り込みが簡潔に書けるように。
JSDocで`@import {foo} from "foo"`をサポート、正規表現の基本的な構文チェックをサポート、`isolatedDeclarations`をサポート。
設定ファイル内で`${configDir}`のテンプレート値をサポート。
`typescript`パッケージのサイズを削減、Named Importをサポート、`transpileDeclaration` APIの追加。
`out`や`target: ES3`などの非推奨となっていたオプションを削除など

- [The Making of a TypeScript Feature: Inferring Type Predicates](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/ "The Making of a TypeScript Feature: Inferring Type Predicates")

----
<h1 class="site-genre">アーティクル</h1>

----

## Rspack v1.0 Release Plan · web-infra-dev/rspack · Discussion #6315
[github.com/web-infra-dev/rspack/discussions/6315](https://github.com/web-infra-dev/rspack/discussions/6315 "Rspack v1.0 Release Plan · web-infra-dev/rspack · Discussion #6315")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

Rspackのロードマップ。
2024年7月にRspack 1.0をリリースする予定


----

## HTML attributes vs DOM properties - JakeArchibald.com
[jakearchibald.com/2024/attributes-vs-properties/](https://jakearchibald.com/2024/attributes-vs-properties/ "HTML attributes vs DOM properties - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

HTMLの属性とDOMプロパティの違いについて。
属性とプロパティの型の違い、大文字小文字の区別、Reflectionについて。
また、Preact/VueやReactなどのUIフレームワークでの扱いについてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## LavaMoat/LavaDome: Secure DOM trees isolation and encapsulation leveraging ShadowDOM
[github.com/LavaMoat/LavaDome](https://github.com/LavaMoat/LavaDome "LavaMoat/LavaDome: Secure DOM trees isolation and encapsulation leveraging ShadowDOM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

Shadow DOMを使い同じOriginで実行されているJavaScriptからもアクセスできないDOMを扱うライブラリ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## React のルール – React
[ja.react.dev/reference/rules](https://ja.react.dev/reference/rules "React のルール – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">docue</span> <span class="jser-tag">translate</span></p>

Rules of Reactの翻訳。
Reactでアプリケーションを書く時のルールについて書かれている

- [Rules of React – React](https://react.dev/reference/rules "Rules of React – React")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## JSON Fixer
[jsonfixer.com/](https://jsonfixer.com/ "JSON Fixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">Tools</span></p>

JSONっぽいものをJSONに修正してくれるツール


----
