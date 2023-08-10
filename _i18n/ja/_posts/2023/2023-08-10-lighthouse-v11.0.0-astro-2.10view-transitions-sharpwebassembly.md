---
title: "2023-08-10のJS: Lighthouse v11.0.0、Astro 2.10(View Transitions)、SharpのWebAssemblyビルド"
author: "azu"
layout: post
date : 2023-08-10T13:11:24.885Z
category: JSer
tags:
- Bun
- Tools
- Chrome
- performance
- deno

---

JSer.info #655 - Lighthouse v11.0.0がリリースされました。

- [Release v11.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0)

Node.js 16のサポート終了、デフォルトでは使われてなかった`resource-summary`/`service-worker`/`first-contentful-paint-3g`のAuditを削除などの変更が含まれます。
また、[INP](https://web.dev/inp/)のAuditがStableへと移行されています。

---

Astro 2.10がリリースされました。

- [Astro 2.10: Persistent State in View Transitions | Astro](https://astro.build/blog/astro-2100/)

[Astro 2.9で実験的にサポートされたView Transitions](https://astro.build/blog/astro-290/)に加える形で、指定した要素を永続的にする`transition:persist`ディレクティブが追加されています。

また、Astro 3.0がベータリリースされています。

- [astro/packages/astro/CHANGELOG.md at refs/heads/next · withastro/astro](https://github.com/withastro/astro/blob/refs/heads/next/packages/astro/CHANGELOG.md#300-beta0)

----

[Bringing Sharp to WebAssembly and WebContainers](https://blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/)という記事では、Native Addonである画像処理ライブラリの[sharp](https://sharp.pixelplumbing.com/)をWebAssemblyへどのようにビルドしたかについて書かれています。

emnapiを使ったNode APIの移植、libvipsをWasmへコンパイル、起動時の処理を同期的にするためにEmscriptenをどのように修正したかについて書かれています。

次のPull Requestでsharpの変更が確認できます。

- [WebAssembly build by RReverser · Pull Request #3522 · lovell/sharp](https://github.com/lovell/sharp/pull/3522)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bun v0.7.2 | Bun Blog
[bun.sh/blog/bun-v0.7.2](https://bun.sh/blog/bun-v0.7.2 "Bun v0.7.2 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.7.2リリース。
`node:worker_threads`、`node:diagnostics_channel`のサポート。
`BroadcastChannel` APIのサポート、`Error`オブジェクトを`structuredClone`でcloneできるように修正。
メモリリークの修正など


----

## Release v11.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0 "Release v11.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse v11.0.0リリース。
Node.js 16のサポート終了、`resource-summary`/`service-worker`/`first-contentful-paint-3g`のAuditを削除。
INPのAuditをStableへと移行など


----

## Deno 1.36: More flexible security and expanded testing APIs
[deno.com/blog/v1.36](https://deno.com/blog/v1.36 "Deno 1.36: More flexible security and expanded testing APIs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.36リリース。
`--deny-*`の拒否フラグをサポート、`deno test`がJUnitレポーターをサポート、`node:test`のサポート。
Node.jsとの互換性改善、モジュールのダウンロードにリトライを追加など


----

## Astro 2.10: Persistent State in View Transitions | Astro
[astro.build/blog/astro-2100/](https://astro.build/blog/astro-2100/ "Astro 2.10: Persistent State in View Transitions | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 2.10リリース。
View Transition APIを使って指定した要素を永続的にする`transition:persist`ディレクティブの追加。
また合わせてAstro 3.0がベータリリースされている。


----

## Bun v0.7.3 | Bun Blog
[bun.sh/blog/bun-v0.7.3](https://bun.sh/blog/bun-v0.7.3 "Bun v0.7.3 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.7.3リリース。
`bun test --coverage`のサポート、`bun test -t /pattern/`のサポート。
`bun:sqlite`、`fs`のクラッシュの修正など


----

## 1.0.0: Milestone for API stability · vanjs-org/van · Discussion #72
[github.com/vanjs-org/van/discussions/72](https://github.com/vanjs-org/van/discussions/72 "1.0.0: Milestone for API stability · vanjs-org/van · Discussion #72")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Reactive UIフレームワークのVanJS 1.0リリース。

- [Release 1.0.0: Milestone for API stability · vanjs-org/van](https://github.com/vanjs-org/van/releases/tag/1.0.0 "Release 1.0.0: Milestone for API stability · vanjs-org/van")

----

## Release v0.19.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.19.0](https://github.com/evanw/esbuild/releases/tag/v0.19.0 "Release v0.19.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.19.0リリース。
エントリーポイントにワイルドカードを指定できるように、Dynamic Importで変数を含めたパスをbundleできるように。
`--packages=external`と`tsconfig.json`の`paths`の問題の修正、`.module.css`のデフォルトローダを`local-css`へ変更


----

## Wednesday August 9th 2023 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/august-2023-security-releases](https://nodejs.org/en/blog/vulnerability/august-2023-security-releases "Wednesday August 9th 2023 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.jsのセキュリティリリースとして次のバージョンが公開されている。

- Node v20.5.1 (Current)
- Node v18.17.1 (LTS)
- Node v16.20.2 (LTS)

実験的な機能であるPermissions policiesの修正とOpenSSLのアップデートが主な修正


----

## Announcing TypeScript 5.2 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-2-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-rc/ "Announcing TypeScript 5.2 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.2 RCリリース。
Stage 3 ProposalのExplicit Resource Management(`using`宣言)のサポート、Decorator Metadataのサポート。
Tupleにおけるラベルありなしの組み合わせの制限を削除、配列のUnion型の扱いの改善。
`import type`では`.ts`ファイルをimportできるように修正、`module`オプションと`moduleResolution`オプションの間違った組み合わせのチェックを追加など


----

## Release Notes for Safari Technology Preview 176 | WebKit
[webkit.org/blog/14401/release-notes-for-safari-technology-preview-176/](https://webkit.org/blog/14401/release-notes-for-safari-technology-preview-176/ "Release Notes for Safari Technology Preview 176 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 176リリース。
CSSの`contain-intrinsic-size: inherit`のサポート、`liner(...)` timing functionのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Bringing Sharp to WebAssembly and WebContainers
[blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/](https://blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/ "Bringing Sharp to WebAssembly and WebContainers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">Image</span> <span class="jser-tag">article</span></p>

C++で書かれたNative Addonの画像処理ライブラリであるsharpをWebContainersで利用できるようにWebAssemblyへコンパイルする話。
emnapiを使ったNode APIの移植、libvipsをWasmへコンパイル、起動時の処理を同期的にするためにEmscriptenをどのように修正したかについて。


----

## A compilation of outstanding testing articles (with JavaScript) | Practica.js
[practica.dev/blog/a-compilation-of-outstanding-testing-articles-with-javaScript/](https://practica.dev/blog/a-compilation-of-outstanding-testing-articles-with-javaScript/ "A compilation of outstanding testing articles (with JavaScript) | Practica.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

テストに関する優れた記事/動画の概要を紹介している記事。


----

## Puppeteer in Node.js: Common Mistakes to Avoid | AppSignal Blog
[blog.appsignal.com/2023/02/08/puppeteer-in-nodejs-common-mistakes-to-avoid.html](https://blog.appsignal.com/2023/02/08/puppeteer-in-nodejs-common-mistakes-to-avoid.html "Puppeteer in Node.js: Common Mistakes to Avoid | AppSignal Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">article</span></p>

Puppeteerでのよくある間違いについての連載記事


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Vue.jsエコシステム動向2023 - Speaker Deck
[speakerdeck.com/kazupon/vue-dot-jsekosisutemudong-xiang-2023](https://speakerdeck.com/kazupon/vue-dot-jsekosisutemudong-xiang-2023 "Vue.jsエコシステム動向2023 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">slide</span></p>

Vue周りのエコシステムについてのスライド。
Vue 3.3の改善内容やReactivity Transformが非推奨となった理由について。
VueのLSP、Nuxt 3とNitroについてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## npmgraph -
[npmgraph.js.org/](https://npmgraph.js.org/ "npmgraph -")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

npmパッケージの依存関係を可視化できるWebサービス。
指定したパッケージまたは`package.json`から解析できる


----
<h1 class="site-genre">書籍関係</h1>

----

## 実践 Svelte入門：書籍案内｜技術評論社
[gihyo.jp/book/2023/978-4-297-13495-2](https://gihyo.jp/book/2023/978-4-297-13495-2 "実践 Svelte入門：書籍案内｜技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">book</span></p>

Svelteの入門書


----
