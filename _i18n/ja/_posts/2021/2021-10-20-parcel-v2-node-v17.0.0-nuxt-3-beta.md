---
title: "2021-10-20のJS: Parcel v2、Node v17.0.0、Nuxt 3 beta"
author: "azu"
layout: post
date : 2021-10-20T03:47:20.958Z
category: JSer
tags:
- React
- node.js
- video
- bundler
- browser

---

JSer.info #562 - ビルドツールのParcel v2がリリースされました。

- [Announcing Parcel v2!](https://parceljs.org/blog/v2/)

Parcelは設定なしで動作することを目的にしているため、v1ではプラグインの仕組みは薄い形になっていました。
Parcel v2ではプラグインの仕組みを刷新し、様々なケースに対応できるようになっています。

- [Plugins](https://parceljs.org/features/plugins/)

また、Tree Shakingをデフォルト化、[SWC](https://github.com/swc-project/swc)ベースのJavaScriptコンパイラに変更、ModernとLegacyビルドの出し分け、Image optimizerの追加されています。
その他にも、bundleのインライン化、ライブラリ向けのビルドのサポート、C++やRustでコアモジュールの一部を書き直し、ビルドパフォーマンスの改善なども含まれています。

Parcel v1からマイグレーションについてのドキュメントも公開されています。

- [Migration](https://parceljs.org/getting-started/migration/)

----

Node.js 17.0.0がリリースされました。

- [Node v17.0.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v17.0.0/)
- [Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium](https://medium.com/the-node-js-collection/node-js-17-is-here-8dba1e14e382)

Nodeの奇数バージョンはLTSとはなりませんが、`Current`バージョンが17.xとなります。
現在のNodeのLTSは12と14ですが、2021-10-26にNode 16がLTSに追加されます。

- [Releases | Node.js](https://nodejs.org/en/about/releases/)

Node.js 17では、`readline`モジュールのPromise対応、OpenSSL 3.0へのアップデート、V8 9.5へアップデート、npm 8.0.0へのアップデート、スタックトレースにNodeバージョンを表示などの変更が含まれています。
またウェブ標準の`strcturedClone()`と`DOMException`をサポートが追加されています。

[structuredClone()](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)は`postMessage`などで内部的に使われていた(DOMを含む)オブジェクトの複製のメカニズムを関数として公開したメソッドです。
最近、WHATWG HTMLの仕様に追加され、[Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=1722576)や[Deno](https://deno.com/blog/v1.13#support-for-self.structuredclone())で実装され、[Chrome](https://bugs.chromium.org/p/chromium/issues/detail?id=1233571)、[Safari](https://bugs.webkit.org/show_bug.cgi?id=228331)、[core-js](https://github.com/zloirock/core-js/issues/969)で実装が進められています。

- [Expose structuredClone by surma · Pull Request #3414 · whatwg/html](https://github.com/whatwg/html/pull/3414)

この`structuredClone()`は`JSON.parse`/`JSON.strinfigy`がサポートしていないオブジェクト(MapやRegExpなど)もサポートしていため、DOM以外の部分でも有用です。

- [構造化複製アルゴリズムを使ったオブジェクトのディープコピー](https://zenn.dev/petamoriken/articles/ad1e943d8d113c)

`structuredClone()`で複製ができない場合は`DOMException`を例外として投げる仕様であるため、`DOMException`も合わせて実装されています。

Node 17にはNode 16の変更点も含まれるので、その他の変更は次の記事を参照してください。

- [2021-04-27のJS: Node.js 16.0.0、Chrome 91 beta、Prisma(Ready for production) - JSer.info](https://jser.info/2021/04/27/node.js-16.0.0-chrome-91-beta-prismaready-for-production/)
- [Node.js v17 の主な変更点 - 別にしんどくないブログ](https://shisama.hatenablog.com/entry/2021/10/20/114721)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Parcel v2!
[parceljs.org/blog/v2/](https://parceljs.org/blog/v2/ "Announcing Parcel v2!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v2リリース。
プラグインの仕組みを刷新、Tree Shakingをデフォルト化、SWCベースのJavaScriptコンパイラに変更、ModernとLegacyビルドの出し分け、Image optimizerの追加。
bundleのインライン化、ライブラリ向けのビルドのサポート、開発時はリクエストされたタイミングで遅延ビルドできるようになるなど。
その他にもSource MapライブラリをRustで書き直してパフォーマンス改善やファイル監視の仕組みの改善などが含まれている

- [Migration](https://parceljs.org/getting-started/migration/ "Migration")

----

## Deno 1.15 Release Notes | Deno Blog
[deno.com/blog/v1.15](https://deno.com/blog/v1.15 "Deno 1.15 Release Notes | Deno Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.15リリース。
Web Crypto APIの更新、FFIの改善、`deno uninstall`コマンドの追加、`deno lint --watch`の追加。
`Deno.test`がネストしたテストケースをサポート、V8 9.5へアップデート、Node.js互換のモジュールを利用できる`--compat`フラグの追加など

- [Deno v1.15で導入されたNode.js互換モードについて](https://zenn.dev/uki00a/articles/node-compat-mode-introduced-in-deno-v1-15 "Deno v1.15で導入されたNode.js互換モードについて")

----

## Nuxt - Introducing Nuxt 3 Beta
[nuxtjs.org/announcements/nuxt3-beta/](https://nuxtjs.org/announcements/nuxt3-beta/ "Nuxt - Introducing Nuxt 3 Beta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt 3 betaリリース。
Vue 3とViteへの対応。
新しいサーバエンジンのNitro Engineを導入することで、通常のNode.jsサーバ、Serverless、Service Workerなど様々な形でデプロイできるようになっている。


----

## GitHub Advisory Database now powers npm audit | The GitHub Blog
[github.blog/2021-10-07-github-advisory-database-now-powers-npm-audit/](https://github.blog/2021-10-07-github-advisory-database-now-powers-npm-audit/ "GitHub Advisory Database now powers npm audit | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Github</span> <span class="jser-tag">news</span></p>

`npm audit`がGitHub Advisory Databaseをみるようになった


----

## Release v7.0.0 · pinojs/pino
[github.com/pinojs/pino/releases/tag/v7.0.0](https://github.com/pinojs/pino/releases/tag/v7.0.0 "Release v7.0.0 · pinojs/pino")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

pino 7.0.0リリース。
ログの処理を別Threadなどに渡せる`pino.transport()`の追加、`pino.multistream()`の追加、TypeScriptの型を同梱するようになるなど

- [Welcome to pino@7.0.0 - and the era of worker\_thread transport - NearForm](https://www.nearform.com/blog/pino7-0-0-pino-transport-worker_thread-transport/ "Welcome to pino@7.0.0 - and the era of worker\_thread transport - NearForm")

----

## Node v17.0.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.0.0/](https://nodejs.org/en/blog/release/v17.0.0/ "Node v17.0.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v17.0.0リリース。
`readline`モジュールのPromise対応、OpenSSL 3.0へのアップデート、V8 9.5へアップデート、npm 8.0.0へのアップデート、スタックトレースにNodeバージョンを表示など。
またウェブ標準の`strcturedClone()`と`DOMException`をサポート

- [Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium](https://medium.com/the-node-js-collection/node-js-17-is-here-8dba1e14e382 "Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium")
- [Release v8.0.0 · npm/cli](https://github.com/npm/cli/releases/tag/v8.0.0 "Release v8.0.0 · npm/cli")

----
<h1 class="site-genre">アーティクル</h1>

----

## A Visual Guide to React Rendering - Cheat Sheet | Alex Sidorenko
[alexsidorenko.com/blog/react-render-cheat-sheet/](https://alexsidorenko.com/blog/react-render-cheat-sheet/ "A Visual Guide to React Rendering - Cheat Sheet | Alex Sidorenko")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">cheatsheet</span> <span class="jser-tag">article</span></p>

Reactのレンダリングのビジュアライズ


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## RF21 – Naman Goel – Rethinking CSS - Introducing Stylex - YouTube
[www.youtube.com/watch?v&#x3D;ur-sGzUWId4](https://www.youtube.com/watch?v=ur-sGzUWId4 "RF21 – Naman Goel – Rethinking CSS - Introducing Stylex - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">facebook</span> <span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">video</span></p>

FacebookのAtomic CSSの実装であるStylexについての動画。
StylexはReact-Nativeライクなスタイルの書き方をするツールキット、Atomic CSSによって線形的に増えるCSSの量を非線形にできる。
2021年末にベータ版をリリースする予定。

- [Facebook CSS-in-JS Solution Stylex Introduced at React Finland 2021](https://www.infoq.com/news/2021/10/facebook-css-js-stylex/ "Facebook CSS-in-JS Solution Stylex Introduced at React Finland 2021")

----

## React Finland 2021 - Talks - YouTube
[www.youtube.com/playlist?list&#x3D;PL-a9lBflNu2opNHeISTnlHgGVlI7oGLXi](https://www.youtube.com/playlist?list=PL-a9lBflNu2opNHeISTnlHgGVlI7oGLXi "React Finland 2021 - Talks - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Finland 2021の動画一覧

- [React Finland 2021 - Sessions - YouTube](https://www.youtube.com/playlist?list=PL-a9lBflNu2rhk1vr3yr4mdRzzUb_nj5P "React Finland 2021 - Sessions - YouTube")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## PrivacyTests.org: open-source tests of web browser privacy
[privacytests.org/](https://privacytests.org/ "PrivacyTests.org: open-source tests of web browser privacy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">privacy</span></p>

ブラウザごとのFinger PrintingやTracking対策などのPrivacy機能をまとめたサイト。


----

## oslabs-beta/sapling: Sapling - A convenient way to traverse your React app in VS Code
[github.com/oslabs-beta/sapling](https://github.com/oslabs-beta/sapling "oslabs-beta/sapling: Sapling - A convenient way to traverse your React app in VS Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">React</span> <span class="jser-tag">Extension</span></p>

Reactのコンポーネントツリーをエディタのサイドパネルに表示するVSCode拡張。
Rootとなるコンポーネントを含むファイルを選ぶと、そのコンポーネントが含むコンポーネントをツリーとして表示してくれる

- [Sapling - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=team-sapling.sapling "Sapling - Visual Studio Marketplace")
- [Introducing Sapling: a VS Code Extension for Traversing React Component Hierarchy | by Team Sapling | Oct, 2021 | JavaScript in Plain English](https://javascript.plainenglish.io/introducing-sapling-a-vs-code-extension-for-traversing-your-react-component-hierarchy-3ac94d95887e "Introducing Sapling: a VS Code Extension for Traversing React Component Hierarchy | by Team Sapling | Oct, 2021 | JavaScript in Plain English")

----
<h1 class="site-genre">書籍関係</h1>

----

## Practical Svelte - Create Performant Applications with the Svelte Component Framework | Alex Libby | Apress
[www.apress.com/gp/book/9781484273739](https://www.apress.com/gp/book/9781484273739 "Practical Svelte - Create Performant Applications with the Svelte Component Framework | Alex Libby | Apress")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">book</span></p>

Svelteを使ったウェブアプリケーション開発の入門書


----

## Sairyss/domain-driven-hexagon: Guide on Domain-Driven Design, Hexagonal architecture, best practices etc.
[github.com/Sairyss/domain-driven-hexagon](https://github.com/Sairyss/domain-driven-hexagon "Sairyss/domain-driven-hexagon: Guide on Domain-Driven Design, Hexagonal architecture, best practices etc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DDD</span> <span class="jser-tag">document</span> <span class="jser-tag">TypeScript</span></p>

ドメイン駆動設計(DDD)についてのガイド。
主にDDDに関係する用語、設計、TypeScriptでのサンプルを用いた技術的な戦術についての解説をまとめたもの。


----
