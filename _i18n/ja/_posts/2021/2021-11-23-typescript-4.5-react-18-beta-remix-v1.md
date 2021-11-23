---
title: "2021-11-23のJS: TypeScript 4.5、React 18 beta、Remix v1"
author: "azu"
layout: post
date : 2021-11-23T14:07:26.950Z
category: JSer
tags:
- Tools
- TypeScript
- React
- Chrome
- debug

---

JSer.info #567 - TypeScript 4.5が正式リリースされました。

- [Announcing TypeScript 4.5 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5/)

TypeScriptがビルトインで持つ`lib`の型定義を`package.json`の`dependencies`を使ってロックできるようになっています。
`Awaited`型の追加、Top-Level awaitに対応した`module: es2022`のサポート、Condition Typesにおいて一部末尾最適化するようになる変更も含まれています。
import名に対する`type` modifierのサポート、ES ProposalのPrivate Field Presence Checks、Import Assertionsのサポートなども追加されています。

[TypeScript 4.5 Beta](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-beta/)で追加されていたNode.jsのESMサポートについては4.6以降に延期となっています。

---

React 18のbetaがリリースされています。

- [React 18 is now in beta · Discussion #112 · reactwg/react-18](https://github.com/reactwg/react-18/discussions/112)
- [The Plan for React 18 – React Blog](https://reactjs.org/blog/2021/06/08/the-plan-for-react-18.html)

[useSyncExternalStore](https://github.com/reactwg/react-18/discussions/86)/[useId](https://github.com/reactwg/react-18/discussions/111)/[useInsertionEffect](https://github.com/reactwg/react-18/discussions/110)のAPIがそれぞれ追加されています。
React 18の機能開発はこれで完了として、正式版のリリースに向けて残りはドキュメントやエラーの改善などを行うようです。

----

ReactベースのウェブフレームワークであるRemix v1リリースされています。

- [Remix v1 | Remix](https://remix.run/blog/remix-v1)

Next.jsなどのようにReactをベースにしたフレームワークになっていて、CLI、ルーティング、ライフサイクルメソッド、React Hooksなどを提供します。
他のものとの違いとしてSSR(Server Side Rendering)やSSG(Static Site Generator)ではなく、クライアントサーバモデルを基本としています。
サーバが返すデータをフィルターし、クライアントに転送するデータを最小化する目的の`loader`関数などを持っています。
どのような目的を持って作られているかについては次のページにまとめられています。

- [Remix | Philosophy](https://remix.run/docs/en/v1/guides/philosophy)

また、このサーバ側をfly.ioやCloudflare WorkersなどのEdgeで動かせるようになっています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 4.5 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-5/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5/ "Announcing TypeScript 4.5 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.5リリース。
TypeScriptがビルトインで持つ`lib`の型定義を`dependencies`としてロックできるように。
`Awaited`型の追加、Top-Level awaitに対応した`module: es2022`のサポート、Condition Typesにおいて一部末尾最適化するように。
import名に対する`type` modifierのサポート、ES ProposalのPrivate Field Presence Checks、Import Assertionsのサポートなど


----

## React 18 is now in beta · Discussion #112 · reactwg/react-18
[github.com/reactwg/react-18/discussions/112](https://github.com/reactwg/react-18/discussions/112 "React 18 is now in beta · Discussion #112 · reactwg/react-18")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 18 betaリリース。
`useSyncExternalStore`(`useMutableSource`をリネーム)、`useId`、`useInsertionEffect`の追加など


----

## Remix v1 | Remix
[remix.run/blog/remix-v1](https://remix.run/blog/remix-v1 "Remix v1 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ReactベースのウェブフレームワークであるRemix v1リリース。
CLI、ルーティング、ライフサイクルメソッド、React Hooksなどを提供する。
クライアントサーバモデルで、サーバが返すデータをフィルターし、最小限のデータにすることを目的にした`loader`関数などを持つ。
fly.ioやCloudflare Workersなどサーバ側をEdgeで動かすことを目的にしている。


----

## Release v6.0.0 · sindresorhus/execa
[github.com/sindresorhus/execa/releases/tag/v6.0.0](https://github.com/sindresorhus/execa/releases/tag/v6.0.0 "Release v6.0.0 · sindresorhus/execa")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

execa 6.0.0リリース。
ESMのみのサポートに変更、default exportを削除しnamed exportに変更など


----

## Release v4.0.0 · emberjs/ember.js
[github.com/emberjs/ember.js/releases/tag/v4.0.0](https://github.com/emberjs/ember.js/releases/tag/v4.0.0 "Release v4.0.0 · emberjs/ember.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 4.0.0リリース

- [Ember 3.28 and 4.0 Beta Released](https://blog.emberjs.com/ember-3-28-released "Ember 3.28 and 4.0 Beta Released")

----
<h1 class="site-genre">アーティクル</h1>

----

## Chrome Devtools による フロントエンドパフォーマンスの計測
[zenn.dev/koki\_tech/articles/9deb70d0a9befb](https://zenn.dev/koki_tech/articles/9deb70d0a9befb "Chrome Devtools による フロントエンドパフォーマンスの計測")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chromeの開発者ツールのパフォーマンスタブの読み方の図解


----

## Reimagine Atomic CSS
[antfu.me/posts/reimagine-atomic-css](https://antfu.me/posts/reimagine-atomic-css "Reimagine Atomic CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Atomic CSSについて。
事前生成 + PruneのTaildinwのアプローチ、オンデマンド生成のTailwindCSSについて。
また、Atomic CSSエンジンのUnoCSSを作っているという話。


----

## What&#039;s New In DevTools (Chrome 96) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-96/](https://developer.chrome.com/blog/new-in-devtools-96/ "What&#039;s New In DevTools (Chrome 96) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome96の開発者ツールの変更点について。
CSS Overviewパネルの追加、`prefers-contrast`とAuto Dark Themeのエミュレート機能の追加。
NetworkパネルにPayloadタブの追加、試験的にReporting APIパネルを追加など


----

## Migrating from Puppeteer to Playwright | Checkly
[www.checklyhq.com/guides/puppeteer-to-playwright/](https://www.checklyhq.com/guides/puppeteer-to-playwright/ "Migrating from Puppeteer to Playwright | Checkly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

PuppeteerからPlaywrightの移行方法についての記事。
APIの対応表、マイグレーション方法、Playwrightのauto-waiting、二つの違いについてなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## divriots/browser-vite: Vite in the browser.
[github.com/divriots/browser-vite](https://github.com/divriots/browser-vite "divriots/browser-vite: Vite in the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">Tools</span></p>

ViteをブラウザのService Workersで動かすプロジェクト


----

## Bun - fast JavaScript &amp; CSS bundler
[bun.sh/](https://bun.sh/ "Bun - fast JavaScript &amp; CSS bundler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

Zigで書かれたJavaScript/TypeScript/CSSに対応したTranspiler/Bundlerツール


----

## d-kimuson/type-predicates-generator: generating predicates and assertion function by type definitions.
[github.com/d-kimuson/type-predicates-generator](https://github.com/d-kimuson/type-predicates-generator "d-kimuson/type-predicates-generator: generating predicates and assertion function by type definitions.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

TypeScriptのコードからtype predicatesをするassertion関数を生成するツール

- [TypeScriptの型定義から型ガードを自動生成する type-predicates-generator の紹介](https://zenn.dev/kimuson/articles/type_predicates_generator "TypeScriptの型定義から型ガードを自動生成する type-predicates-generator の紹介")

----
<h1 class="site-genre">書籍関係</h1>

----

## クリエイティブコーディングの教科書
[zenn.dev/baroqueengine/books/a19140f2d9fc1a](https://zenn.dev/baroqueengine/books/a19140f2d9fc1a "クリエイティブコーディングの教科書")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">book</span></p>

JavaScriptとCanvasを使ったクリエティブコーディングについての電子書籍。
Canvasでの描画、画像処理、探索アルゴリズム、アニメーション表現についてなど


----
