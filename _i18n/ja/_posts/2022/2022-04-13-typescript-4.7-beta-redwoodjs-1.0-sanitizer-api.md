---
title: "2022-04-13のJS: TypeScript 4.7 Beta、RedwoodJS 1.0、Sanitizer API"
author: "azu"
layout: post
date : 2022-04-12T22:59:47.573Z
category: JSer
tags:
- Tools
- TypeScript
- React
- testing
- book

---

JSer.info #587 - TypeScript 4.7 Betaがリリースされました。

- [Announcing TypeScript 4.7 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/)

TypeScript 4.5 Betaで導入されNightlyでテストされていた、Node.jsのECMAScript Moduleサポートを再び有効化されています。
これに関連して`package.json`の`exports`フィールドのサポート、`"module": "nodenext"`、`.mts`/`cts`の拡張子のサポートが追加されています。
また、Node.jsではファイルがモジュールかどうかは`package.json`の`module`フィールドなどによって暗黙的に異なります。
そのため、ファイルがモジュールかどうかを判定方法を制御できる`moduleDetection`オプションも追加して、強制的(`force`)にモジュールとして認識させることもできるようになっています。

- [Add moduleDetection compiler flag to allow for changing how modules are parsed by weswigham · Pull Request #47495 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/47495)

型推論の改善として、Compuatedプロパティに対するコントロールフロー解析の改善、オブジェクトにおける関数の型推論の改善が含まれています。

Genericsの型を指定したaliasを定義できる Instantiation Expressionsをサポート。

```ts
const ErrorMap = Map<string, Error>;
```

- [Add moduleDetection compiler flag to allow for changing how modules are parsed by weswigham · Pull Request #47495 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/47495)

`infer`に対する`extends`での推論条件の追加をサポート、型が共変(`in`)/反変(`out`)/不変(`in out`)なのかを指定できるアノテーションを追加されています。

- [Optional variance annotations by ahejlsberg · Pull Request #48240 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/48240)

モジュール解決持の探索方法をカスタマイズする`moduleSuffixes`オプションの追加、`import type`とReference Commentで`resolution-mode`を指定できるようになっています。

----

[Making of: The Sanitizer API (Nullcon 2022) - Google スライド](https://docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM_ASFHH8Z5fMyfeoSbSH-k/view#slide=id.g82761e80df_0_1948)というスライドでは、[HTML Sanitizer API](https://wicg.github.io/sanitizer-api/)という策定中/実装中のウェブ標準について紹介されています。

信頼できないHTML文字列のインジェクトするときに、そのHTML文字列をサニタイズしてXSSを防止するためのAPIです。
最初は、HTML文字列をサニタイズしてHTML文字列を返すAPIとして進められていました、HTMLのパースモードの違いなどからパイパスする方法があることが発見されました。(HTML文字列という文字列のフラグメントに対するサニタイズは安全にはできないと分かった)

そのため、`innerHTML`とよく似た`setHTML`という新しいAPIが策定され、このAPIにsanitizerを渡す形に変更された話が書かれています。

- [Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api](https://github.com/WICG/sanitizer-api/issues/42)
- [1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc](https://bugzilla.mozilla.org/show_bug.cgi?id=1669945)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Astro 1.0 Beta Release | Astro
[astro.build/blog/astro-1-beta-release/](https://astro.build/blog/astro-1-beta-release/ "Astro 1.0 Beta Release | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 1.0 betaリリース。
2022年6月8日に正式リリースの予定。


----

## Announcing Rome Formatter
[rome.tools/blog/2022/04/05/rome-formatter-release](https://rome.tools/blog/2022/04/05/rome-formatter-release "Announcing Rome Formatter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rustに書き直されたRomeのFormatterがリリースされた。
Prettierの挙動をベースにしていて、opt-inで構文エラーのコードに対する整形も対応している。


----

## Release v8.0.0 · cucumber/cucumber-js
[github.com/cucumber/cucumber-js/releases/tag/v8.0.0](https://github.com/cucumber/cucumber-js/releases/tag/v8.0.0 "Release v8.0.0 · cucumber/cucumber-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Cucumber.js 8.0.0リリース。


----

## Announcing RedwoodJS 1.0 and $1M Funding
[tom.preston-werner.com/2022/04/04/redwood-v1-and-funding.html](https://tom.preston-werner.com/2022/04/04/redwood-v1-and-funding.html "Announcing RedwoodJS 1.0 and $1M Funding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">React</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">prisma</span> <span class="jser-tag">jest</span></p>

React/GraphQL/Prisma/Jest/Storybookを組み合わせたアプリケーションフレームワークであるRedwoodJS 1.0リリース。

- [Redwood 1.0.0-rc.final is Available 🚀 - Announcements / Releases and Upgrade Guides - RedwoodJS Community](https://community.redwoodjs.com/t/redwood-1-0-0-rc-final-is-available/2902 "Redwood 1.0.0-rc.final is Available 🚀 - Announcements / Releases and Upgrade Guides - RedwoodJS Community")

----

## Announcing TypeScript 4.7 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/ "Announcing TypeScript 4.7 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.7 betaリリース。
Node.jsのECMAScript Moduleサポートを再び有効化、`moduleDetection`オプションの追加。
Compuatedプロパティに対するコントロールフロー解析の改善、オブジェクトにおける関数の型推論の改善。Genericsの型を指定したaliasを定義できる Instantiation Expressionsをサポート。
`infer`に対する`extends`での推論条件の追加をサポート、型が共変(`in`)/反変(`out`)/不変(`in out`)なのかを指定できるアノテーションを追加。
モジュール解決持の探索方法をカスタマイズする`moduleSuffixes`オプションの追加、`import type`とReference Commentで`resolution-mode`を指定できるように。


----

## Release Notes for Safari Technology Preview 143 | WebKit
[webkit.org/blog/12563/release-notes-for-safari-technology-preview-143/](https://webkit.org/blog/12563/release-notes-for-safari-technology-preview-143/ "Release Notes for Safari Technology Preview 143 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 143リリース。
CSS Container Queriesの改善、CSS Cascade Layersの改善。Web Animation APIの改善。
Permissions APIをデフォルトで有効化、`inert`属性をデフォルトで有効化。

- [HTMLElement.inert - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/HTMLElement/inert "HTMLElement.inert - Web API | MDN")

----

## Turborepo 1.2 | Turborepo
[turborepo.org/blog/turbo-1-2-0](https://turborepo.org/blog/turbo-1-2-0 "Turborepo 1.2 | Turborepo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepot 1.2リリース。
対象をフィルターできる`--filter`フラグの追加、`--dry-run`フラグの追加。
パフォーマンスの改善、キャッシュの整合性をHMACで検証できる`signature`オプションの追加など


----

## Release v8.0.0-rc.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v8.0.0-rc.0](https://github.com/reduxjs/react-redux/releases/tag/v8.0.0-rc.0 "Release v8.0.0-rc.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.0.0-rc.0リリース。
`@types/react-readux`に存在した`DefaultRootState`の型定義を削除など


----

## goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript &amp; Node.js testing best practices (April 2022)
[github.com/goldbergyoni/javascript-testing-best-practices](https://github.com/goldbergyoni/javascript-testing-best-practices "goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript &amp; Node.js testing best practices (April 2022)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">news</span></p>

JavaScriptのテストについてのドキュメント。 テストの構造、バックエンド、フロントエンド、CIなどについて書かれているjavascript-testing-best-practicesがアップデートされた


----

## Release 2.0.0-beta.0 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-beta.0](https://github.com/vercel/swr/releases/tag/2.0.0-beta.0 "Release 2.0.0-beta.0 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-beta.0リリース。
リモートの副作用のあるリクエストを扱う`useSWRMutation`の追加。
破壊的な変更としてFetcherには複数の引数として展開しないように変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## 04.01.2022 - TypeScript/How the compiler compiles
[www.huy.rocks/everyday/04-01-2022-typescript-how-the-compiler-compiles](https://www.huy.rocks/everyday/04-01-2022-typescript-how-the-compiler-compiles "04.01.2022 - TypeScript/How the compiler compiles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript CompilerがどうやってTypeScritのコードをコンパイル、エラーを報告しているかについての解説記事


----

## ECMAScript proposal “Change Array by copy”: four new non-destructive Array methods
[2ality.com/2022/04/change-array-by-copy.html](https://2ality.com/2022/04/change-array-by-copy.html "ECMAScript proposal “Change Array by copy”: four new non-destructive Array methods")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3のChange Array by copyについて。
Arrayのメソッドには破壊的なメソッドが混ざっていたが、それに対応する非破壊的なメソッドを追加するProposal


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Making of: The Sanitizer API (Nullcon 2022) - Google スライド
[docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM\_ASFHH8Z5fMyfeoSbSH-k/view#slide&#x3D;id.g82761e80df\_0\_1948](https://docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM_ASFHH8Z5fMyfeoSbSH-k/view#slide=id.g82761e80df_0_1948 "Making of: The Sanitizer API (Nullcon 2022) - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">API</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

Sanitizer APIについてのスライド。 
DOM XSSを防ぐSanitizer APIがサニタイズしたHTML文字列を返すAPIではない理由、`setHTML` APIについて

- [Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api](https://github.com/WICG/sanitizer-api/issues/42 "Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api")
- [1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc](https://bugzilla.mozilla.org/show_bug.cgi?id=1669945 "1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## antfu/vue-starport: 🛰 Shared component across routes with animations
[github.com/antfu/vue-starport](https://github.com/antfu/vue-starport "antfu/vue-starport: 🛰 Shared component across routes with animations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

ページをまたいでで同じコンポーネントを表示、遷移アニメーションを行うVueコンポーネント。
共有するコンポーネントをRootに引き上げることで、ページ間で同じコンポーネントのインスタンスを維持している。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## AgnosticUI/agnosticui: AgnosticUI is a set of UI primitives that start their lives in clean HTML and CSS. These standards compliant components are then copied to our framework implementations in: React, Vue 3, Angular, and Svelte.
[github.com/agnosticui/agnosticui](https://github.com/agnosticui/agnosticui "AgnosticUI/agnosticui: AgnosticUI is a set of UI primitives that start their lives in clean HTML and CSS. These standards compliant components are then copied to our framework implementations in: React, Vue 3, Angular, and Svelte.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

UIコンポーネントフレームワーク。
プレーンなJSからも利用でき、React/Angular/Svelte/Vueなどの各種UIフレームワーク向けのパッケージも公開されている。


----
<h1 class="site-genre">書籍関係</h1>

----

## プロを目指す人のためのTypeScript入門　安全なコードの書き方から高度な型の使い方まで：書籍案内｜技術評論社
[gihyo.jp/book/2022/978-4-297-12747-3](https://gihyo.jp/book/2022/978-4-297-12747-3 "プロを目指す人のためのTypeScript入門　安全なコードの書き方から高度な型の使い方まで：書籍案内｜技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2022年4月22日発売
TypeScriptの入門書


----
