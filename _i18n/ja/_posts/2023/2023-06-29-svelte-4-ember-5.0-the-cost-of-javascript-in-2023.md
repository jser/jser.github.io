---
title: "2023-06-29のJS: Svelte 4、Ember 5.0、The Cost Of JavaScript in 2023"
author: "azu"
layout: post
date : 2023-06-29T00:45:08.079Z
category: JSer
tags:
- CSS
- Tools
- React
- TypeScript
- editor

---

JSer.info #649 - Svelte 4がリリースされました。

- [Announcing Svelte 4](https://svelte.dev/blog/svelte-4)
- [Release svelte@4.0.0 · sveltejs/svelte](https://github.com/sveltejs/svelte/releases/tag/svelte%404.0.0)

Node.js 14のサポート終了、CJSの出力は廃止しESMのみをサポートするように、Custom Elementsの対応を`tag`オプションから`customElement`オプションに変更といった変更が含まれている。
また、生成するファイルサイズの削減、ウェブサイトのドキュメントを刷新なども行われています。

マイグレーションガイドと`npx svelte-migrate@latest svelte-4`というマイグレーションツールが公開されています。

- [Svelte 4 migration guide • Docs • Svelte](https://svelte.dev/docs/v4-migration-guide)

---

Ember 5.0リリースされました。

- [Ember 5.0 Released](https://blog.emberjs.com/ember-5-0-released/)

Emberではメジャーアップデートで機能追加をせず、破壊的変更のみを行うため、機能追加はありません。
非推奨となっていた`AutoLocation`の削除、`@ember/error`パッケージの削除、`Ember.String`の削除など行われています。

---

The Cost Of JavaScriptの2023年版の動画とスライドが公開されています。

- [The Cost Of JavaScript - 2023 - YouTube](https://www.youtube.com/watch?v=ZKH3DLT4BKw)
- [The Cost Of JavaScript in 2023 - Speaker Deck](https://speakerdeck.com/addyosmani/the-cost-of-javascript-in-2023)

JavaScriptのダウンロード、実行のコストについて話されていて、Code SplittingやDynamic Importなどの最適化について紹介されています。
また、最近発展してきたIslands ArchitectureのPartial Hydration、QwikのResumalable Hydration、ReactのSelective Hydationについても紹介されています。

過去のThe Cost Of JavaScriptについては、次のページを参照してください。

- [The Cost Of JavaScript In 2018. Update: The Cost Of JavaScript In 2019… | by Addy Osmani | Medium](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4)
- [The cost of JavaScript in 2019 · V8](https://v8.dev/blog/cost-of-javascript-2019)

また、実際のウェブサイトの統計的なデータに関しては[Web Almanac](https://almanac.httparchive.org/ja/2022/)の[JavaScript](https://almanac.httparchive.org/en/2022/javascript)の章などを参照すると良いと思います。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Svelte 4
[svelte.dev/blog/svelte-4](https://svelte.dev/blog/svelte-4 "Announcing Svelte 4")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">ReleaseNote</span></p>

Svelte 4リリース。
Node.js 14のサポート終了、CJSの出力は廃止しESMのみをサポートするように、Custom Elementsの対応を`tag`オプションから`customElement`オプションに変更。
生成するファイルサイズの削減、ウェブサイトのドキュメントを刷新など

- [Svelte 4 migration guide • Docs • Svelte](https://svelte.dev/docs/v4-migration-guide "Svelte 4 migration guide • Docs • Svelte")
- [Release svelte@4.0.0 · sveltejs/svelte](https://github.com/sveltejs/svelte/releases/tag/svelte%404.0.0 "Release svelte@4.0.0 · sveltejs/svelte")

----

## Ember 5.0 Released
[blog.emberjs.com/ember-5-0-released/](https://blog.emberjs.com/ember-5-0-released/ "Ember 5.0 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 5.0リリース。
Emberではメジャーアップデートは機能追加をせず、破壊的変更のみを行う。
`AutoLocation`の削除、`@ember/error`パッケージの削除、`Ember.String`の削除など


----

## Release v6.14.0 · remix-run/react-router
[github.com/remix-run/react-router/releases/tag/react-router%406.14.0](https://github.com/remix-run/react-router/releases/tag/react-router%406.14.0 "Release v6.14.0 · remix-run/react-router")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Router 6.14.0リリース。
`useSubmit`がJSONとTextをサポート。


----

## Release v0.18.9 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.9](https://github.com/evanw/esbuild/releases/tag/v0.18.9 "Release v0.18.9 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.9リリース。
`await using`の対応漏れの修正、autoprefixer的のようにCSSのprefixを自動で追加できるようになるなど


----

## Bun v0.6.10 | Bun Blog
[bun.sh/blog/bun-v0.6.10](https://bun.sh/blog/bun-v0.6.10 "Bun v0.6.10 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.6.10リリース。
CommonJSの互換性を改善しwebpack動作するように、`require.main`のサポート、`__esModule`フラグを解釈するように。
`fs.watch`の実装、V8の`Error.captureStackTrace`の実装。
`bun install`時にライフサイクルスクリプトの実行を許可するパッケージを定義する`trustedDependencies`フィールドのサポートなど


----

## Release Notes for Safari Technology Preview 173 | WebKit
[webkit.org/blog/14378/release-notes-for-safari-technology-preview-173/](https://webkit.org/blog/14378/release-notes-for-safari-technology-preview-173/ "Release Notes for Safari Technology Preview 173 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 173リリース。
Safari 17で導入予定の機能が利用できるTechnology Preview。
Web Inspectorの再設計、ウェブアプリをDockに追加、JPEG XLのサポート、HEICのサポートなど


----

## Release v3.0.0 · cloudflare/miniflare
[github.com/cloudflare/miniflare/releases/tag/v3.0.0](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0 "Release v3.0.0 · cloudflare/miniflare")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

miniflare v3.0.0リリース。
workerdを利用するのようになった。
CLIが同梱されなくなり`wrangler`を経由してCLIとして利用できる。
またいくつかのAPIが削除や変更されている。

- [⬆️ Migrating from Version 2 · Miniflare](https://miniflare.dev/get-started/migrating "⬆️ Migrating from Version 2 · Miniflare")

----
<h1 class="site-genre">アーティクル</h1>

----

## Cyclic Dependency Space Toggles
[kizu.dev/cyclic-toggles/](https://kizu.dev/cyclic-toggles/ "Cyclic Dependency Space Toggles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Variablesを使ってロジックゲートを実装する方法について。
循環参照するVariablesは無効となる仕様を利用し、Variablesにif文的な切り替えを実装する方法について。またなぜこのような仕様と実装になったのかについて


----

## Next.js App Router Update | Next.js
[nextjs.org/blog/june-2023-update](https://nextjs.org/blog/june-2023-update "Next.js App Router Update | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.jsの最近の取り組みについて。
App RouterのStable化、巨大なアプリケーションでのパフォーマンスの改善、ドキュメントの改善。
ReactのServer Side Componentへの対応やServer Actionsについてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 2023-06-24 DOMのテストがどんどん書きたくなるTesting Libraryの世界への招待 (#phpconfuk) - Google スライド
[docs.google.com/presentation/d/1j6sEAs0LF5jPXs\_mHxvPreqK-lxEL3OxvQAFyXmxbZc/view#slide&#x3D;id.g24bcedd6665\_0\_0](https://docs.google.com/presentation/d/1j6sEAs0LF5jPXs_mHxvPreqK-lxEL3OxvQAFyXmxbZc/view#slide=id.g24bcedd6665_0_0 "2023-06-24 DOMのテストがどんどん書きたくなるTesting Libraryの世界への招待 (#phpconfuk) - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">slide</span></p>

DOMのテストライブラリであるTesting Libraryの考え方について。
DOMを生成し、テスト対象をクエリで検索し、アサーションでテストする。
クエリにはWAI-ARIA Roleやラベル、Test Idなどを指定するメソッドがあるがその優先度について。

- [About Queries | Testing Library](https://testing-library.com/docs/queries/about/ "About Queries | Testing Library")

----

## The Cost Of JavaScript - 2023 - YouTube
[www.youtube.com/watch?v&#x3D;ZKH3DLT4BKw](https://www.youtube.com/watch?v=ZKH3DLT4BKw "The Cost Of JavaScript - 2023 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">performance</span></p>

JavaScriptのコストについての動画とスライド。
JavaScriptのダウンロード、実行のコスト。
Code SplittingやDynamic Importなどの最適化。
Islands ArchitectureのPartial Hydration、QwikのResumalable Hydration、ReactのSelective Hydationについて。

- [The Cost Of JavaScript in 2023 - Speaker Deck](https://speakerdeck.com/addyosmani/the-cost-of-javascript-in-2023?slide=31 "The Cost Of JavaScript in 2023 - Speaker Deck")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Module Federation: streamline your microfrontends
[module-federation.io/](https://module-federation.io/ "Module Federation: streamline your microfrontends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MicroFrontend</span> <span class="jser-tag">document</span></p>

Microforntendsの開発を補助するModule Federationについてのウェブサイトが公開された。
ドキュメントやユースケース、使い方やサンプルプロジェクトなどが公開されている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Panda CSS - Build modern websites using build time and type-safe CSS-in-JS
[panda-css.com/](https://panda-css.com/ "Panda CSS - Build modern websites using build time and type-safe CSS-in-JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

CSS in JSフレームワーク。
TypeScriptでType Safeにスタイルを書くことができ、ツールを通してCSSファイルとして出力することで、実行時にはJSが不要になっている。


----

## Codux | Visual IDE for React
[www.codux.com/](https://www.codux.com/ "Codux | Visual IDE for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">editor</span> <span class="jser-tag">Tools</span></p>

Reactのビジュアルエディタ。
GUIでコンポーネントを編集でき、コードも並べて編集できるエディタ。

- [Meet Codux: The React Visual Editor That Improves Developer Experience — Smashing Magazine](https://www.smashingmagazine.com/2023/06/codux-react-visual-editor-improves-developer-experience/ "Meet Codux: The React Visual Editor That Improves Developer Experience — Smashing Magazine")

----
