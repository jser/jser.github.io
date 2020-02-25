---
title: "2020-02-25のJS: TypeScript 3.8 正式リリース、ESLint 7.0.0の変更予定"
author: "azu"
layout: post
date : 2020-02-25T02:30:48.221Z
category: JSer
tags:
- TypeScript
- ESLint

---

JSer.info #476 - TypeScript 3.8が正式にリリースされました。

- [Announcing TypeScript 3.8 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8/)

型定義だけをインポート/エクスポートできる`import type`/`export type`の追加、ECMASCript Proposal Stage 3の[ECMAScript Private Fields](https://github.com/tc39/proposal-private-fields)、[Top-Level `await`](https://github.com/tc39/proposal-top-level-await)のサポートが追加されています。

また、`tsconfig.json`の`tartet`と`module`オプションに`es2020`を追加、`watchOptions`で`--watch`時の挙動の設定の追加、`assumeChangesOnlyAffectDirectDependencies`オプションで"Fast and Loose"なインクリメンタルビルドをサポートしています。

----

現在[v7.0.0-alpha.1](https://github.com/eslint/eslint/releases/tag/v7.0.0-alpha.1)が公開されているESLint 7の変更予定がまとめられたドキュメントが公開されています。

- [What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0)

このドキュメントでは主に破壊的な変更についてまとめられています。

Node.js 8.xのサポートを終了し、`CLIEngine`クラスは非推奨となり新しく`ESLint`クラスが導入される予定です。
`ESLint`クラスについては次のRFCにまとめられていますが、既存の`CLIEngine`クラスは同期処理だったのに対して`ESLint`クラスは非同期処理に対応するものとなります。

- [New: `ESLint` Class Replacing `CLIEngine` by mysticatea · Pull Request #40 · eslint/rfcs](https://github.com/eslint/rfcs/pull/40)

また、ESLint本体に含まれていたNode.jsやCommonJS関係のルールは[`eslint-plugin-node`](https://github.com/mysticatea/eslint-plugin-node)に移行される予定です。
その他には、directive commentsにコメントを書けるように、ホームディレクトリにある`~/.eslintrc`の利用に警告がでるように、デフォルトのignore patternsの更新などが含まれる予定です。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 3.8 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-8/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8/ "Announcing TypeScript 3.8 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.8リリース。
`import type`/`export type`の追加、Stage 3のES Private Fields、Top-Level `await`のサポート。
`tartet`と`module`オプションに`es2020`を追加、`watchOptions`で`--watch`時の挙動を設定できるようになるなど


----

## Node v13.9.0 (Current) | Node.js
[nodejs.org/en/blog/release/v13.9.0/](https://nodejs.org/en/blog/release/v13.9.0/ "Node v13.9.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Node v13.9.0リリース。
`async_hooks`モジュールに`executionAsyncResource`を追加、`crypto`モジュールに`diffieHellman`を追加。
Diagnostic Reportがworker_thredsをサポート

- [Diagnostic Report | Node.js v13.9.0 Documentation](https://nodejs.org/api/report.html "Diagnostic Report | Node.js v13.9.0 Documentation")

----

## Release Initial Release: 1.0.0 · reduxjs/cra-template-redux
[github.com/reduxjs/cra-template-redux/releases/tag/v1.0.0](https://github.com/reduxjs/cra-template-redux/releases/tag/v1.0.0 "Release Initial Release: 1.0.0 · reduxjs/cra-template-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">Tools</span></p>

create-react-app向けのReduxテンプレート。
`npx create-react-app my-app --template redux` でセットアップできる。
Redux Toolkitを利用している

- [Redux Toolkit | Redux Toolkit](https://redux-toolkit.js.org/ "Redux Toolkit | Redux Toolkit")

----

## Release 3.4.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.4.0](https://github.com/avajs/ava/releases/tag/v3.4.0 "Release 3.4.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3.4.0リリース。
テストを失敗させずにAssertionを試せる`t.try()`のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Understanding the “Initial”, “Inherit” and “Unset” CSS Keywords
[medium.com/@elad/understanding-the-initial-inherit-and-unset-css-keywords-2d70b7121695](https://medium.com/@elad/understanding-the-initial-inherit-and-unset-css-keywords-2d70b7121695 "Understanding the “Initial”, “Inherit” and “Unset” CSS Keywords")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSの`initial`、`inherit`、`unset`、`revert`について。
CSS プロパティの初期値の違いやそれぞれの意味について


----

## The Circuit Breaker Pattern
[blog.bearer.sh/circuit-breaker-design-pattern/](https://blog.bearer.sh/circuit-breaker-design-pattern/ "The Circuit Breaker Pattern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">article</span></p>

Node.jsでCircuit Breakerパターンをしながら学んでいくチュートリアル

- [Building a Circuit Breaker in Node.js (Part 1)](https://blog.bearer.sh/build-a-circuit-breaker-in-node-js/ "Building a Circuit Breaker in Node.js (Part 1)")

----

## 仮想DOMは本当に“速い”のか？ DOM操作の新しい考え方を、フレームワークを実装して理解しよう - エンジニアHub｜若手Webエンジニアのキャリアを考える！
[employment.en-japan.com/engineerhub/entry/2020/02/18/103000](https://employment.en-japan.com/engineerhub/entry/2020/02/18/103000 "仮想DOMは本当に“速い”のか？ DOM操作の新しい考え方を、フレームワークを実装して理解しよう - エンジニアHub｜若手Webエンジニアのキャリアを考える！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VirtualDOM</span> <span class="jser-tag">article</span></p>

Virtual DOMとは何かやどのように実装されているかについて。
なぜVirtual DOMではレンダリングが遅くなりにくいかについて


----

## Aborting a fetch request
[meetguns.com/blog/aborting-a-fetch-request/](https://meetguns.com/blog/aborting-a-fetch-request/ "Aborting a fetch request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

`AbortController`を使ってFetchのキャンセルを行う方法について


----

## Angular 9: What’s New?
[auth0.com/blog/angular-9-whats-new/](https://auth0.com/blog/angular-9-whats-new/ "Angular 9: What’s New?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 9の変更点についての解説


----

## What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0](https://eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0 "What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint 7.0.0での変更予定について。
`CLIEngine`クラスは非推奨となり新しく`ESLint`クラスが導入される、Node.jsやCommonJS関係のルールは`eslint-plugin-node`に移行される。
directive commentsにコメントを書けるように、`~/.eslintrc`の利用に警告がでるように、デフォルトのignore patternsの更新など


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## benawad/destiny: Prettier for File Structures
[github.com/benawad/destiny](https://github.com/benawad/destiny "benawad/destiny: Prettier for File Structures")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

プロジェクトのファイル構造をコンポーネントごとに分けるように編集するツール


----

## suchipi/hex-engine: A modern 2D game engine for the browser.
[github.com/suchipi/hex-engine](https://github.com/suchipi/hex-engine "suchipi/hex-engine: A modern 2D game engine for the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">canvas</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Canvasを使った2Dゲームエンジンライブラリ。ReactインスパイアなAPIを持つ。
音声同期、スプライトシートやアニメーション、物理エンジンなどのサポート。
またAseprite、Tiled、BMFontなどのオーサリングツールもサポートしている。

- [Aseprite - Animated sprite editor & pixel art tool](https://www.aseprite.org/ "Aseprite - Animated sprite editor &amp; pixel art tool")
- [Tiled Map Editor | A flexible level editor](https://www.mapeditor.org/ "Tiled Map Editor | A flexible level editor")
- [BMFont - AngelCode.com](https://www.angelcode.com/products/bmfont/ "BMFont - AngelCode.com")

----
