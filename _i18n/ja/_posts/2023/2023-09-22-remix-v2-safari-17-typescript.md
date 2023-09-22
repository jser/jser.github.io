---
title: "2023-09-22のJS: Remix v2、Safari 17、TypeScriptドキュメンタリー"
author: "azu"
layout: post
date : 2023-09-22T11:20:43.678Z
category: JSer
tags:
- Tools
- nodejs
- UI
- Chrome
- debug

---

JSer.info #661 - - [Remix v2 | Remix](https://remix.run/blog/remix-v2)
- [Upgrading to v2 | Remix](https://remix.run/docs/en/main/start/v2)

---

- [WebKit Features in Safari 17.0 | WebKit](https://webkit.org/blog/14445/webkit-features-in-safari-17-0/)
- [Safari 17 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes)

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/U6s2pdxebSo?si=X3RsrXXWRZQbyT9K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bun v1.0.2 | Bun Blog
[bun.sh/blog/bun-v1.0.2](https://bun.sh/blog/bun-v1.0.2 "Bun v1.0.2 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.2リリース。
`bunx <pkg>@latest`で最新のパッケージが取得できないバグを修正、`bun --watch`のパフォーマンス改善。
DateのパースにV8の実装を使雨ように、`URL.canParse`/`URLSearchParams.prototype.size`の実装など。


----

## Release v2.0.0 · remix-run/remix
[github.com/remix-run/remix/releases/tag/remix%402.0.0](https://github.com/remix-run/remix/releases/tag/remix%402.0.0 "Release v2.0.0 · remix-run/remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">ReleaseNote</span></p>

Remix 2.0.0リリース。
React 17のサポート終了、Node.js 14/16のサポート終了。
V1からの移行は`v2_*`フラグを使うことで機能を一つずつ有効化して移行できる。
2.0.0では`v2_*`フラグの削除、`remix.config.js`の設定やコマンドの変更などが含まれる。

- [Remix v2 | Remix](https://remix.run/blog/remix-v2 "Remix v2 | Remix")
- [Upgrading to v2 | Remix](https://remix.run/docs/en/main/start/v2 "Upgrading to v2 | Remix")

----

## Node v18.18.0 (LTS) | Node.js
[nodejs.org/ja/blog/release/v18.18.0](https://nodejs.org/ja/blog/release/v18.18.0 "Node v18.18.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.18.0リリース。
`node --import`フラグの追加、`node:fs`と`node:stream`でExplicit Resource Managementのサポートなど


----

## Node v20.7.0 (Current) | Node.js
[nodejs.org/ja/blog/release/v20.7.0](https://nodejs.org/ja/blog/release/v20.7.0 "Node v20.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.7.0リリース。
複数の`--env-file`指定をサポート、npm 10.xへのアップデート、`process.sourceMapsEnabled` APIの追加など


----

## Next.js 13.5 | Next.js
[nextjs.org/blog/next-13-5](https://nextjs.org/blog/next-13-5 "Next.js 13.5 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 13.5リリース。
パフォーマンスの改善、re-exportsするパッケージを最適化する`optimizePackageImports`オプションの追加。
実験的な機能として、`next/image`に`unstable_getImgProps`を追加、`next dev --experimental-https`の追加。
また、`create-next-app`がBunをサポートなど


----

## eslint-stylistic/eslint-stylistic: Monorepo for ESLint Stylistic plugins and configs
[github.com/eslint-stylistic/eslint-stylistic](https://github.com/eslint-stylistic/eslint-stylistic "eslint-stylistic/eslint-stylistic: Monorepo for ESLint Stylistic plugins and configs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">plugin</span></p>

ESLintのスタイル関連のルールを管理するプロジェクト


----

## Ladle v3 | Ladle
[ladle.dev/blog/ladle-v3](https://ladle.dev/blog/ladle-v3 "Ladle v3 | Ladle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybookの代替ツールであるLadle v3リリース。
SWCをデフォルトのTranspilerに変更、Node.js 16のサポート終了、CSS in JSライブラリを追加の設定なしで動作するように


----

## WebKit Features in Safari 17.0 | WebKit
[webkit.org/blog/14445/webkit-features-in-safari-17-0/](https://webkit.org/blog/14445/webkit-features-in-safari-17-0/ "WebKit Features in Safari 17.0 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17リリース。
HTMLでは、`<search>`要素の対応、`popover`属性の対応。
CSSでは、`font-size-adjust`、`text-transform`、`@counter-style`、`image-set()`の対応。
JavaScriptでは、Storage API、正規表現の`v`フラグ(ES2024)、Stage 3のSet Operationsの対応。
画像では、JPEG XL/HEIC/AV1コーデックのサポート。
実験的なフラグの管理方法や開発者ツールの変更なども含まれる

- [Safari 17 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes "Safari 17 Release Notes | Apple Developer Documentation")

----

## Deno 1.37: Modern JavaScript in Jupyter Notebooks
[deno.com/blog/v1.37](https://deno.com/blog/v1.37 "Deno 1.37: Modern JavaScript in Jupyter Notebooks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">denoe</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.37リリース。
`deno jupyter --unstable`の追加、`deno test`に`--reporter=tap`レポーターを追加、Node.jsとの互換性改善。
ロックファイルの形式をversion 3にアップデート、`std/url`の追加、`std/ulid`の追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## How to Find the Exact Line of an Infinite Loop Bug in the code | by Abdu Tawfik | Medium
[abduvik.medium.com/how-to-find-infinite-loops-in-javascript-using-devtools-ea5fc84aec73](https://abduvik.medium.com/how-to-find-infinite-loops-in-javascript-using-devtools-ea5fc84aec73 "How to Find the Exact Line of an Infinite Loop Bug in the code | by Abdu Tawfik | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chromeで無限ループが起きてる時にパフォーマンスのプロファイルを取る方法について。
無限ループが起きるとProfile自体も完了しないため、記録を開始してタブのプロセスを強制的に停止すると取得できるという方法について。
また同期的な無限ループと非同期的な無限ループについて


----

## From WebGL to WebGPU - Chrome for Developers
[developer.chrome.com/en/blog/from-webgl-to-webgpu/](https://developer.chrome.com/en/blog/from-webgl-to-webgpu/ "From WebGL to WebGPU - Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">WebGPU</span> <span class="jser-tag">article</span></p>

WebGLとWebGPUの違いについて


----

## Introducing runes
[svelte.dev/blog/runes](https://svelte.dev/blog/runes "Introducing runes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">article</span></p>

Svelte 5はrunesという`$state`/`$derived`/`$effect`といったマクロを使いreactiveなステート管理を実現するという話。
`$:`のラベルでのReactiveではアプリケーションが複雑になるとどれがReactiveなのかがわからなくなる問題があったため。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## TypeScript Origins: The Documentary - YouTube
[www.youtube.com/watch?v&#x3D;U6s2pdxebSo](https://www.youtube.com/watch?v=U6s2pdxebSo "TypeScript Origins: The Documentary - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">video</span></p>

TypeScriptのドキュメンタリー動画


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## nuejs/nuejs: Build user interfaces with 10x less code. Alternative to React, Vue, and Svelte
[github.com/nuejs/nuejs/tree/master](https://github.com/nuejs/nuejs/tree/master "nuejs/nuejs: Build user interfaces with 10x less code. Alternative to React, Vue, and Svelte")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

少ないコード量で書けることが目的のVue/Riot的なUIフレームワーク。


----
