---
title: "2023-06-21のJS: React-Redux v8.1.0、Fresh 1.2、Modern CSS"
author: "azu"
layout: post
date : 2023-06-20T22:57:46.724Z
category: JSer
tags:
- React
- node.js
- WebAssembly
- webservice
- TypeScript

---

JSer.info #648 - React-Redux v8.1.0リリースされました。
開発モードでは`useSelector`が同じ入力に対して同じ結果を返すかをチェックする仕組みが追加されています。
selectorを同じ入力で2回呼び出し、異なる参照の場合は警告を出す仕組みになっています。
[React v18.0](https://react.dev/blog/2022/03/29/react-v18#new-strict-mode-behaviors)で追加されたStrict modeとよく似た挙動になっています。

- [Release v8.1.0 · reduxjs/react-redux](https://github.com/reduxjs/react-redux/releases/tag/v8.1.0)

---

Deno向けのウェブフレームワークであるFresh 1.2がリリースされました。

- [Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more](https://deno.com/blog/fresh-1.2)

メインメンテナーがPreactの[Marvin Hagemeister](https://github.com/marvinhagemeister)となりフルタイムでメンテナンスするようになるそうです。
Sigalsをhydrateできるように、`npm:`識別子の対応、HEADハンドラーの追加されています。
また、`islands/`のサブディレクトリのサポート、プラグインが非同期処理に対応なども行われています。

---

[Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions](https://moderncss.dev/modern-css-for-dynamic-component-based-architecture/)という記事では、モダンなCSSを使ったコンポーネントベースのアーキテクチャについて紹介されています。

`@layer`を使ったLayout、`:has()`やCustom Propertiesを使ったVariantsの実装、
`@container style()`を使ったスタイルの条件分岐、Container QueryとMedia Queryによるブレークポイントでのデバイスサイズ出し分けの違いについてなど書かれています。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 3.31.0 - 2023.06.12 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.31.0](https://github.com/zloirock/core-js/releases/tag/v3.31.0 "Release 3.31.0 - 2023.06.12 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.31.0リリース。
Proposal Stageの変更への対応。
Array GroupingはStage 2へ降格し、静的メソッドである`Object.groupBy`を追加。
`Promise.withResolvers`の追加など


----

## Turborepo 1.10 – Turbo
[turbo.build/blog/turbo-1-10-0](https://turbo.build/blog/turbo-1-10-0 "Turborepo 1.10 – Turbo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepo 1.10リリース。
Plopを使った`turbo gen`の追加、`.env`のサポート、`--env-mode`がStableに変更など

- [Consistency Made Simple : PLOP](https://plopjs.com/ "Consistency Made Simple : PLOP")

----

## Release v8.1.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v8.1.0](https://github.com/reduxjs/react-redux/releases/tag/v8.1.0 "Release v8.1.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.1.0リリース。
開発モードでは`useSelector`が同じ入力に対して同じ結果を返すかをチェックする仕組みが追加された。
selectorを同じ入力で2回呼び出し、異なる参照の場合は警告を出す仕組み


----

## Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more
[deno.com/blog/fresh-1.2](https://deno.com/blog/fresh-1.2 "Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">React</span></p>

Deno向けのWeb FrameworkであるFresh 1.2リリース。
メインメンテナーをPreactのMarvin Hagemeisterに交代。
Sigalsをhydrateできるように、`npm:`識別子の対応、HEADハンドラーの追加。
`islands/`のサブディレクトリのサポート、プラグインが非同期処理に対応など


----

## Release v10.0.0 · nestjs/nest
[github.com/nestjs/nest/releases/tag/v10.0.0](https://github.com/nestjs/nest/releases/tag/v10.0.0 "Release v10.0.0 · nestjs/nest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

NestJS v10.0.0リリース。
Node.js 12, 14のサポート終了、`@nestjs/common`から`CacheModule`を削除など

- [Migration guide - FAQ | NestJS - A progressive Node.js framework](https://docs.nestjs.com/migration-guide "Migration guide - FAQ | NestJS - A progressive Node.js framework")

----

## Release v5.0.0 ❤️ · gvergnaud/ts-pattern
[github.com/gvergnaud/ts-pattern/releases/tag/v5.0.0](https://github.com/gvergnaud/ts-pattern/releases/tag/v5.0.0 "Release v5.0.0 ❤️ · gvergnaud/ts-pattern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

TypeScript向けのパターンマッチングライブラリであるts-pattern 5.0.0リリース。
`.with`の動作変更、method chainのサポートなど


----

## Tuesday June 20 2023 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/june-2023-security-releases](https://nodejs.org/en/blog/vulnerability/june-2023-security-releases "Tuesday June 20 2023 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.jsのセキュリティアップデートとして、16.x/18.x/20.xがそれぞれ公開された。

- Node.js v16.20.1 (LTS)
- Node.js v18.16.1 (LTS)
- Node.js v20.3.1 (Current)


----
<h1 class="site-genre">アーティクル</h1>

----

## The Cloud is dead, long live the Cloud! Announcing Wasmer Edge
[wasmer.io/posts/announcing-wasmer-edge](https://wasmer.io/posts/announcing-wasmer-edge "The Cloud is dead, long live the Cloud! Announcing Wasmer Edge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span> <span class="jser-tag">article</span></p>

Wasmer Edgeのリリース。
WebAssemblyのアプリケーションをWasmtimeで動かすプラットフォーム。
Shared nothingのアーキテクチャを採用した分散モノリスのアプローチ。


----

## Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions
[moderncss.dev/modern-css-for-dynamic-component-based-architecture/](https://moderncss.dev/modern-css-for-dynamic-component-based-architecture/ "Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

モダンなCSSを使ったコンポーネントベースのアーキテクチャについて。
`@layer`を使ったLayout、`:has()`やCustom Propertiesを使ったVariants。
`@container style()`を使ったスタイルの条件分岐、Container QueryとMedia Queryによるブレークポイントでのデバイスサイズ出し分けの違いについてなど


----

## TypeScript 5.2&#039;s New Keyword: &#039;using&#039; | Total TypeScript
[www.totaltypescript.com/typescript-5-2-new-keyword-using](https://www.totaltypescript.com/typescript-5-2-new-keyword-using "TypeScript 5.2&#039;s New Keyword: &#039;using&#039; | Total TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

TypeScript 5.2で実装予定のECMAScript Proposal Stage 3の`using`について。
リソース解放のパターンを`using`構文としてサポートする

- [tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management "tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management")
- [ECMAScript Explicit Resource Management &amp; \`using\` Declarations · Issue #52955 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/52955 "ECMAScript Explicit Resource Management &amp;amp; \&#x60;using\&#x60; Declarations · Issue #52955 · microsoft/TypeScript")

----

## Introducing HTTP/3 Prioritization
[blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/ "Introducing HTTP/3 Prioritization")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP3</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">cloudflare</span></p>

HTTP/3 Extensible Prioritiesをサポートすることで、Webページの読み込みがどれぐらい改善されるかについて


----

## Web Apps on macOS Sonoma 14 Beta
[blog.tomayac.com/2023/06/07/web-apps-on-macos-sonoma-14-beta/](https://blog.tomayac.com/2023/06/07/web-apps-on-macos-sonoma-14-beta/ "Web Apps on macOS Sonoma 14 Beta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">macOS</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

macOS Sonomaのインストール可能なウェブアプリの動作について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Fermyon • Experience the next wave of cloud computing. | Fermyon • Experience the next wave of cloud computing.
[www.fermyon.com/](https://www.fermyon.com/ "Fermyon • Experience the next wave of cloud computing. | Fermyon • Experience the next wave of cloud computing.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span></p>

Spinというツールキットで作成したWebAssemblyアプリケーションをデプロイ、実行できるサーバレスプラットフォーム

- [The Next Generation of Serverless is Happening | Fermyon • Experience the next wave of cloud computing.](https://www.fermyon.com/blog/next-generation-of-serverless-is-happening "The Next Generation of Serverless is Happening | Fermyon • Experience the next wave of cloud computing.")

----
