---
title: "2020-08-25のJS: TypeScript 4.0、Cypress 5.0、Electron 10.0"
author: "azu"
layout: post
date : 2020-08-25T02:59:14.022Z
category: JSer
tags:
- TypeScript
- Testing
- Electron

---

JSer.info #502 - TypeScript 4.0が正式にリリースされました。

- [Announcing TypeScript 4.0 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/)

Variadic Tuple Types、Labeled Tuple Elements、Class Propertyの型がConstructorから推論されるようになるなどの型機能の改善がされています。
また、ES2021で入る予定の[Logical Operators and Assignment Expressions](https://github.com/tc39/proposal-logical-assignment)がサポートされています。
その他には`catch`節のデフォルトが`unknown`となるように変更され、`jsxFragmentFactory`オプションのサポート、`--incremental`と`--noEmit`の組み合わせをサポートが追加されています。

Babel、PreitterはTypeScript 4.0に対応したバージョンがそれぞれリリースされています。

- [7.11.0 Released: ECMAScript 2021 support in preset-env, TypeScript 4.0 support, printing config and the future of `babel-eslint` · Babel](https://babeljs.io/blog/2020/07/30/7.11.0)
- [Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier](https://prettier.io/blog/2019/04/12/1.17.0.html)

TypeScript-ESLintについては次のIssueを参照してください。

- [TypeScript 4.0 Syntax Support · Issue #2260 · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/issues/2260#issuecomment-677853883)

----

E2EテストフレームワークのCypress 5.0がリリースされました。

- [Release 5.0.0 · cypress-io/cypress](https://github.com/cypress-io/cypress/releases/tag/v5.0.0)


`cypress-plugin-retries`が非推奨化され、Cypress自体でリトライの設定できるようになっています。
詳しくは次の記事で解説されています。

- [Introducing Test Retries in Cypress 5.0](https://www.cypress.io/blog/2020/08/19/introducing-test-retries-in-cypress-5-0/)

サポート対象をTypeScript 3.4+、Node.js 10+に変更、テストファイル内に書かれた`__dirname`と`__filename`の末尾に`/`が含まれなくなるなどの変更も含まれています。

----

Electron 10.0がリリースされました。

[Release electron v10.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v10.0.0)

Chromium 85、V8 8.5、Node.js 12.16へアップデートされています。
また`enableRemoteModule`を`false`に変更、`app.allowRendererProcessReuse`を`true`に変更されています。

`remote`モジュールはユーザーランドに移行するため、そのための段階的な変更として`enableRemoteModule`オプションが導入され、デフォルト値が`false`(無効)となりました。
詳しくは次のIssueや予定されている破壊的変更のドキュメントを参照してください。

- [Deprecate the 'remote' module and move it to userland · Issue #21408 · electron/electron](https://github.com/electron/electron/issues/21408)
- [Electron 9.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-9-0)
- [electron/breaking-changes.md at master · electron/electron](https://github.com/electron/electron/blob/master/docs/breaking-changes.md)

その他には、`contents.backgroundThrottling`プロパティの追加、`sameSite`情報を取得できるように、`worldSafeExecuteJavaScript`オプションが追加されています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 2.8.0 · pikapkg/snowpack
[github.com/pikapkg/snowpack/releases/tag/snowpack%402.8.0](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.8.0 "Release 2.8.0 · pikapkg/snowpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

snowpack 2.8.0リリース。
`snowpack build --watch`の追加、`--polyfill-node`でNodeコアモジュールのpolyfillを追加できるようになるなど


----

## Release v1.3.0 · Polymer/lit-html
[github.com/Polymer/lit-html/releases/tag/v1.3.0](https://github.com/Polymer/lit-html/releases/tag/v1.3.0 "Release v1.3.0 · Polymer/lit-html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

lit-html 1.3.0リリース。
Trusted Typesのサポートなど


----

## Announcing TypeScript 4.0 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/ "Announcing TypeScript 4.0 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.0リリース。
Variadic Tuple Types、Labeled Tuple Elements、Class Propertyの型がConstructorから推論されるように。
ES2021で入る予定のLogical Operators and Assignment Expressionsのサポート。
`catch`節のデフォルトが`unknown`となるように、`jsxFragmentFactory`オプションのサポート、`--incremental`と`--noEmit`の組み合わせをサポート


----

## axios/CHANGELOG.md at master · axios/axios
[github.com/axios/axios/blob/master/CHANGELOG.md#0200-august-20-2020](https://github.com/axios/axios/blob/master/CHANGELOG.md#0200-august-20-2020 "axios/CHANGELOG.md at master · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Axios 0.20.0リリース。
BOMを含むJSONに対応、`maxBodyLength`オプションの追加、`decompress`オプションの追加など


----

## Release 5.0.0 · cypress-io/cypress
[github.com/cypress-io/cypress/releases/tag/v5.0.0](https://github.com/cypress-io/cypress/releases/tag/v5.0.0 "Release 5.0.0 · cypress-io/cypress")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">testing</span></p>

Cypress 5.0.0リリース。
`cypress-plugin-retries`が非推奨化され、Cypress自体でリトライの設定できるように。
サポート対象をTypeScript 3.4+、Node.js 10+に変更、`__dirname`と`__filename`の末尾に`/`が含まれなくなるなど

- [Release 5.0.0 · cypress-io/cypress](https://github.com/cypress-io/cypress/releases/tag/v5.0.0 "Release 5.0.0 · cypress-io/cypress")

----

## Release electron v10.0.0 · electron/electron
[github.com/electron/electron/releases/tag/v10.0.0](https://github.com/electron/electron/releases/tag/v10.0.0 "Release electron v10.0.0 · electron/electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 10.0.0リリース。
Chromium 85、V8 8.5、Node.js 12.16へアップデート。
`enableRemoteModule`を`false`に変更、`app.allowRendererProcessReuse`を`true`に変更。
`contents.backgroundThrottling`プロパティの追加、`sameSite`情報を取得できるように、`worldSafeExecuteJavaScript`オプションの追加など


----

## Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier
[prettier.io/blog/2020/08/24/2.1.0.html](https://prettier.io/blog/2020/08/24/2.1.0.html "Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.1リリース。
`--embedded-language-formatting`フラグの追加、`--ignore-unknown`フラグの追加、TypeScript 4.0のサポート。
ES ProposalのPipeline operator、Record and Tuple構文のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## ts-migrate: A Tool for Migrating to TypeScript at Scale | by Sergii Rudenko | Airbnb Engineering & Data Science | Aug, 2020 | Medium
[medium.com/airbnb-engineering/ts-migrate-a-tool-for-migrating-to-typescript-at-scale-cd23bfeb5cc](https://medium.com/airbnb-engineering/ts-migrate-a-tool-for-migrating-to-typescript-at-scale-cd23bfeb5cc "ts-migrate: A Tool for Migrating to TypeScript at Scale | by Sergii Rudenko | Airbnb Engineering & Data Science | Aug, 2020 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

JavaScriptからTypeScriptへのマイグレーションを補助する`ts-migrate`について。
`.js`を`.ts`にリネーム、codemodベースでの`any`などの型付け、コンパイルエラーになる部分を`// @ts-expect-error`コメントで抑制していきマイグレーションする。

- [airbnb/ts-migrate: A tool to help migrate JavaScript code quickly and conveniently to TypeScript](https://github.com/airbnb/ts-migrate "airbnb/ts-migrate: A tool to help migrate JavaScript code quickly and conveniently to TypeScript")

----

## What's New In DevTools (Chrome 86)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/08/devtools](https://developers.google.com/web/updates/2020/08/devtools "What's New In DevTools (Chrome 86)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 86のDevToolsの変更点について。
Mediaパネルの追加、コンテキストメニューから要素のスクリーンショットを撮影できるように。
WebFontで`local()`がない場合をエミュレート、Idle Detectionのエミュレート、`prefers-reduced-data`のエミュレート機能の追加。
Lighthouse 6.2へアップデート、ApplicationパネルにFrameの情報を追加、`X-Client-Data`のデコードをサポートなど


----

## Protect your resources from web attacks with Fetch Metadata
[web.dev/fetch-metadata/](https://web.dev/fetch-metadata/ "Protect your resources from web attacks with Fetch Metadata")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

Fetch Metadataの`Sec-Fetch-*`ヘッダの解説。
Same-OriginとCross-Siteの区別、それぞれの`Sec-Fetch-*`ヘッダの解説、クロスサイトリクエストを使った攻撃の判定と対策などについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## HexEd.it - Browser-based Online and Offline Hex Editing
[hexed.it/](https://hexed.it/ "HexEd.it - Browser-based Online and Offline Hex Editing")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">editor</span> <span class="jser-tag">Tools</span></p>

ブラウザベースのバイナリエディタ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## azu/kvs: Key-Value storage library for Browser, Node.js, and In-Memory.
[github.com/azu/kvs](https://github.com/azu/kvs "azu/kvs: Key-Value storage library for Browser, Node.js, and In-Memory.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ブラウザとNode.jsで動作するUniversalなKey-ValueなStorageライブラリ。
同じインターフェイスをもつIndexedDBやファイルベースなどの実装があり、マイグレーションをサポートしている。
それぞれの実装は個別に分かれていて、それぞれのパッケージは1kb(gzip)程度のサイズとなっている。


----

## Elderjs/elderjs: Elder.js is an opinionated static site generator and web framework for Svelte built with SEO in mind.
[github.com/elderjs/elderjs](https://github.com/elderjs/elderjs "Elderjs/elderjs: Elder.js is an opinionated static site generator and web framework for Svelte built with SEO in mind.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Svelte</span> <span class="jser-tag">library</span></p>

Svelteを使った静的サイトジェネレーター。
規約ではなく`route.js`による柔軟なパーマネントリンクの生成、`data.js`でビルドに必要なものをまとめて取得して、静的なサイトを生成するためのツール。


----

## keiya01/react-performance-testing: A library to test runtime performance in React
[github.com/keiya01/react-performance-testing](https://github.com/keiya01/react-performance-testing "keiya01/react-performance-testing: A library to test runtime performance in React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Reactコンポーネントのレンダリング回数やレンダリング時間を計測できるライブラリ。
Reactにmonkey patchを当てて計測している。

- [Reactでレンダリング回数やレンダリングにかかる時間をユニットテストでテストできるライブラリを開発しました - Qiita](https://qiita.com/keiya01/items/93d83911fb44170717c2 "Reactでレンダリング回数やレンダリングにかかる時間をユニットテストでテストできるライブラリを開発しました - Qiita")

----
