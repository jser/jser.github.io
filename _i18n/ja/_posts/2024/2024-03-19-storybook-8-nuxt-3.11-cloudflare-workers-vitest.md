---
title: "2024-03-19のJS: Storybook 8、Nuxt 3.11、Cloudflare Workers + Vitest"
author: "azu"
layout: post
date: 2024-03-19T03:24:43.652Z
category: JSer
tags:
- React
- test
- CSS
- vite
- Tools

---

JSer.info #685 - Storybook 8.0がリリースされました。

- [Storybook 8](https://storybook.js.org/blog/storybook-8/)
- [Storybook: UI component explorer for frontend developers](https://storybook.js.org/releases/8.0)

破壊的な変更として、`storiesOf` APIの削除、`*.stories.mdx`の削除、StoryShots addonの削除、Yarn v1のサポート終了などが行われています。
詳細はマイグレーションガイドを参照してください。

- [Migration guide for Storybook 8.0 • Storybook docs](https://storybook.js.org/docs/migration-guide?ref=storybookblog.ghost.io)

機能追加として、Chromaticとの連携機能の実装、MSWを使ったReact Server Component(RSC)のサポート。
そのほかには、SWCを使うことでビルドパフォーマンスの改善、`react-docgen`がデフォルトとなるように変更、`react`をpeerDependenciesから除外するなどの変更が行われています。

---

Nuxt 3.11がリリースされました。

- [Nuxt 3.11 · Nuxt Blog](https://nuxt.com/blog/v3-11)

ログ表示の改善、`usePreviewMode`の追加、`appMiddleware`の追加が行われています。
また、サーバ専用の`.server.vue`とクライアント専用の`.client.vue`というファイル名による定義がページコンポーネントでもサポートされています。

----

次の記事では、Vitestを使ったCloudflare Workersのテストについて紹介されています。

- [Improved Cloudflare Workers testing via Vitest and workerd](https://blog.cloudflare.com/workers-vitest-integration/)
- [Vitest integration · Cloudflare Workers docs](https://developers.cloudflare.com/workers/testing/vitest-integration/)

Vitestはテストを分離したWorkerなどで実行できますが、[Custom Pool](https://vitest.dev/advanced/pool.html)を使うことでテストを実行する環境を独自に定義することができます。
[@cloudflare/vitest-pool-workers](https://www.npmjs.com/package/@cloudflare/vitest-pool-workers)では、Miniflareでテストコードを実行できるCustom Poolが実装されています。
これによって、ローカルでもCloudflre Workersのテストを実行することができるようになったという話が紹介されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 5.11.0 · prisma/prisma
[github.com/prisma/prisma/releases/tag/5.11.0](https://github.com/prisma/prisma/releases/tag/5.11.0 "Release 5.11.0 · prisma/prisma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">prisma</span> <span class="jser-tag">ReleaseNote</span></p>

Prisma 5.11.0リリース。
Cloudflare Workers(Vercel Edge)などのEdge functionがプレビューサポートされた。

- [Prisma ORM support for Edge functions is now in Preview](https://www.prisma.io/blog/prisma-orm-support-for-edge-functions-is-now-in-preview "Prisma ORM support for Edge functions is now in Preview")

----

## Storybook 8
[storybook.js.org/blog/storybook-8/](https://storybook.js.org/blog/storybook-8/ "Storybook 8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Design</span> <span class="jser-tag">debug</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 8リリース。
破壊的な変更として、`storiesOf` APIの削除、`*.stories.mdx`の削除、StoryShots addonの削除、Yarn v1のサポート終了。
機能追加として、Chromaticとの連携機能の実装、MSWを使ったReact Server Component(RSC)のサポート。
そのほかには、SWCを使うことでビルドパフォーマンスの改善、`react-docgen`がデフォルトとなるように変更、`react`をpeerDependenciesから除外するなど

- [Storybook: UI component explorer for frontend developers](https://storybook.js.org/releases/8.0 "Storybook: UI component explorer for frontend developers")
- [storybook/MIGRATION.md at next · storybookjs/storybook](https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#from-version-7x-to-800 "storybook/MIGRATION.md at next · storybookjs/storybook")

----

## Bun v1.0.31 | Bun Blog
[bun.sh/blog/bun-v1.0.31](https://bun.sh/blog/bun-v1.0.31 "Bun v1.0.31 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.31リリース。
`bun --print`の追加、Stdinからコードを実行できるように、`bun add --trust <pkg>`の追加、`bun pm trust`/`bun pm untrusted`の追加。
`fetch()`に`unix`オプションを追加しUnix Socketsをサポート。
Node.js 21.7.0で追加された`util.styleText`のサポートなど

- [Node.js — Node v21.7.0 (Current)](https://nodejs.org/en/blog/release/v21.7.0 "Node.js — Node v21.7.0 (Current)")

----

## Nuxt 3.11 · Nuxt Blog
[nuxt.com/blog/v3-11](https://nuxt.com/blog/v3-11 "Nuxt 3.11 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.11リリース。
ログ表示の改善、`usePreviewMode`の追加、`appMiddleware`の追加。
サーバ専用の`.server.vue`とクライアント専用の`.client.vue`をページコンポーネントでもサポートなど


----

## Elysia 1.0 - Lament of the Fallen | ElysiaJS
[elysiajs.com/blog/elysia-10](https://elysiajs.com/blog/elysia-10 "Elysia 1.0 - Lament of the Fallen | ElysiaJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">server</span> <span class="jser-tag">ReleaseNote</span></p>

Bun向けのHTTPサーバフレームワークのElysia 1.0リリース。
起動時間の改善、Type Checkのパフォーマンス改善、`onBeforeHandle`などに`as`オプションを追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Server Actions時代のformライブラリconform
[zenn.dev/akfm/articles/server-actions-with-conform](https://zenn.dev/akfm/articles/server-actions-with-conform "Server Actions時代のformライブラリconform")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Server Actionsに対応したフォームライブラリであるConformについて

- [Conform / Overview](https://conform.guide/ "Conform / Overview")

----

## Improved Cloudflare Workers testing via Vitest and workerd
[blog.cloudflare.com/workers-vitest-integration/](https://blog.cloudflare.com/workers-vitest-integration/ "Improved Cloudflare Workers testing via Vitest and workerd")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">vite</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

VitestでCloudflare Workersのテストを行う方法について。
`@cloudflare/vitest-pool-workers`を使うことで、Workerに対するUnit Testができる仕組みについて。
VitestのCustom Poolを使うことで、テストをworkerdのプロセス内で実行している。

- [Vitest integration · Cloudflare Workers docs](https://developers.cloudflare.com/workers/testing/vitest-integration/ "Vitest integration · Cloudflare Workers docs")

----

## Best Practices for Writing Tests with React Testing Library | ClarityDev blog
[claritydev.net/blog/improving-react-testing-library-tests](https://claritydev.net/blog/improving-react-testing-library-tests "Best Practices for Writing Tests with React Testing Library | ClarityDev blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

React Testing LibraryでのReactコンポーネントのテストについて。
コンポーネントをRoleでselectする方法やデバッグ方法、`userEvent`、"not wrapped in act(...)"の警告についてなど


----

## Implementing Vertical Form Controls | WebKit
[www.webkit.org/blog/15190/implementing-vertical-form-controls/](https://www.webkit.org/blog/15190/implementing-vertical-form-controls/ "Implementing Vertical Form Controls | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">CSS</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

WebKitでのCSS `writing-mode`による縦書きフォームのサポートについて。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## エディター付きのReact開発環境を ブラウザーだけで実装した話 - Speaker Deck
[speakerdeck.com/steelydylan/edeitafu-kinoreactkai-fa-huan-jing-wo-burauzadakedeshi-zhuang-sitahua](https://speakerdeck.com/steelydylan/edeitafu-kinoreactkai-fa-huan-jing-wo-burauzadakedeshi-zhuang-sitahua "エディター付きのReact開発環境を ブラウザーだけで実装した話 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">slide</span></p>

プレビュー機能付きのエディタの実装についてのスライド。
エディタ上の重たい処理をWeb Worker上に逃す方法、Service Worker内でTypeScriptのトランスパイルの実装などについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ECSS — Simple Rules for efficient CSS
[ecss.info/en/](https://ecss.info/en/ "ECSS — Simple Rules for efficient CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

予測可能なCSSを書くためのデザインガイドとstylelintのルール


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## guidepup/virtual-screen-reader: Virtual Screen Reader is a screen reader simulator for unit tests.
[github.com/guidepup/virtual-screen-reader](https://github.com/guidepup/virtual-screen-reader "guidepup/virtual-screen-reader: Virtual Screen Reader is a screen reader simulator for unit tests.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

Unit Testに利用できるスクリーンリーダのシミュレータライブラリ

- [Simple setup: Virtual Screen Reader in Storybook - DEV Community](https://dev.to/scottnath/simple-setup-virtual-screen-reader-in-storybook-2efo "Simple setup: Virtual Screen Reader in Storybook - DEV Community")

----

## MistCSS
[typicode.github.io/mistcss/](https://typicode.github.io/mistcss/ "MistCSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

CSSからReactコンポーネントを作成するツール。
CSSを書いて、そのCSSからRectコンポーネントを生成する仕組みになっている。
data属性をPropsとして扱う、`@scope`でスコープを扱うなど

----

## devongovett/unplugin-parcel-macros
[github.com/devongovett/unplugin-parcel-macros](https://github.com/devongovett/unplugin-parcel-macros "devongovett/unplugin-parcel-macros")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">parcel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">webpack</span> <span class="jser-tag">rollup</span> <span class="jser-tag">vite</span> <span class="jser-tag">esbuild</span></p>

Parcelのmacroと同じものをwebpack/rollup/Vite/esbuildで利用できるようにするプラグイン。
import attributesの構文を使いビルド時にマクロ的な処理を行う仕組み
