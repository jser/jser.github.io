---
title: "2024-08-25のJS: WebdriverIO v9、Node v22.7.0(TS `enum`と`namespace`の対応)、Deno 1.46(Last 1.x)"
author: "azu"
layout: post
date: 2024-08-25T01:34:12.084Z
category: JSer
tags:
- nodejs
- Vue
- TypeScript
- webdriver
- Bun

---

JSer.info #704 - WebdriverIO v9がリリースされました。

- [WebdriverIO v9 Released | WebdriverIO](https://webdriver.io/blog/2024/08/15/webdriverio-v9-release/)

新しい機能として、WebDriver BiDiのサポート、`url`コマンドの追加、`addInitScript`コマンドの追加、`setViewport`コマンドの追加、ShadowRootのサポートなどがあります。

また、`emulate`コマンドでClockのエミュレーションサポートや、要素がinteractiveになるまで自動的に待機する変更も含まれています。

---

Node.js v22.7.0がリリースされました。

- [Node.js — Node v22.7.0 (Current)](https://nodejs.org/en/blog/release/v22.7.0)

新しい機能として、`--experimental-transform-types`フラグによるTypeScriptの`enum`と`namespace`の変換をサポートしました。
また、あいまいなJSをCommonJSかES Modulesかを判定して実行する`--experimental-detect-module`フラグをデフォルトで有効化、Bufferのパフォーマンス改善なども含まれています。

---

Deno v1.46がリリースされました。

- [Deno 1.46: The Last 1.x Release](https://deno.com/blog/v1.46)

Deno 1.xの最終リリースとなる予定です。

`deno run main.ts`の`run`を省略できるように、`deno task`を`deno run`でも呼べるように、`--allow-*`/`--deny-*`の省略形を追加、`--env`を`--env-file`に名前を変更、`deno fmt`がHTML/CSS/YAMLなどをサポート、`deno remove`/`deno clean`コマンドの追加、`deno compile`がCode Signに対応しています。

その他にもstdパッケージの大部分がStableとなりました。

- [The Road to Stabilizing the Standard Library · Issue #4600 · denoland/std](https://github.com/denoland/std/issues/4600)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v11.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v11.0.0](https://github.com/vueuse/vueuse/releases/tag/v11.0.0 "Release v11.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v11.0.0リリース。
依存のmajorアップデート、オプションの追加など


----

## WebdriverIO v9 Released | WebdriverIO
[webdriver.io/blog/2024/08/15/webdriverio-v9-release/](https://webdriver.io/blog/2024/08/15/webdriverio-v9-release/ "WebdriverIO v9 Released | WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v9.リリース。
WebDriver BiDiをサポート、`url`コマンドの追加、`addInitScript`コマンドの追加、`setViewport`コマンドの追加、ShadowRootのサポート。
`emulate`コマンドでClockのエミュレーションサポート、要素がinteractiveになるまで自動的に待機する変更など。


----

## Node.js — Node v20.17.0 (LTS)
[nodejs.org/en/blog/release/v20.17.0](https://nodejs.org/en/blog/release/v20.17.0 "Node.js — Node v20.17.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.17.0リリース。
ESMを`require()`でロードできる`--experimental-require-module`フラグを追加,
Globパターンの判定ができる`path.matchesGlob`を追加。
DuplexPair APIの公開など


----

## Bun v1.1.25 | Bun Blog
[bun.sh/blog/bun-v1.1.25](https://bun.sh/blog/bun-v1.1.25 "Bun v1.1.25 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.25リリース。
`node:cluster`のサポート、V8のinteral APIを部分的にサポート、`bun build --compile`で指定したファイルをバイナリ内にファイルを埋め込めるようになるなど


----

## stackblitz-labs/pkg.pr.new: Continuous (Preview) Releases for your libraries!
[github.com/stackblitz-labs/pkg.pr.new](https://github.com/stackblitz-labs/pkg.pr.new "stackblitz-labs/pkg.pr.new: Continuous (Preview) Releases for your libraries!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">github</span> <span class="jser-tag">CI</span></p>

CIからコミットごとにnpmパッケージを公開できるツールとサービス。


----

## Release v15.0.0 · capricorn86/happy-dom
[github.com/capricorn86/happy-dom/releases/tag/v15.0.0](https://github.com/capricorn86/happy-dom/releases/tag/v15.0.0 "Release v15.0.0 · capricorn86/happy-dom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Happy DOM v15.0.0リリース。
Node.js 18未満のサポート終了、`HTML*Element`のサポートの追加など


----

## Announcing TypeScript 5.6 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/ "Announcing TypeScript 5.6 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.6 RCリリース。
ESLintの`no-constant-binary-expression`と似た常にtrue/nullishとなる間違った書き方をエラーにする変更、Iterator Helperのサポート。
ES2022のArbitrary module namespace identifier namesをサポート、`--noUncheckedSideEffectImports`フラグの追加。
型チェックせずにファイルを出力できる`--noCheck`フラグの追加、`--stopOnBuildErrors`フラグの追加など


----

## Node.js — Node v22.7.0 (Current)
[nodejs.org/en/blog/release/v22.7.0](https://nodejs.org/en/blog/release/v22.7.0 "Node.js — Node v22.7.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.7.0リリース。
TypeScriptの`enum`と`namaspace`の変換を行う`--experimental-transform-types`フラグの追加。
あいまいなJSをCommonJSかES Modulesかを判定して実行する`--experimental-detect-module`フラグをデフォルトで有効化、Bufferのパフォーマンス改善など


----

## Release v1.0.0-rc.0 · web-infra-dev/rspack
[github.com/web-infra-dev/rspack/releases/tag/v1.0.0-rc.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0-rc.0 "Release v1.0.0-rc.0 · web-infra-dev/rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

rspack v1.0.0-rc.0リリース。
eval-source-mapのパフォーマンス改善、`HtmlRspackPlugin`がエスケープ構文をサポートなど


----

## Nuxt 3.13 · Nuxt Blog
[nuxt.com/blog/v3-13](https://nuxt.com/blog/v3-13 "Nuxt 3.13 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Nuxt</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.13リリース。
Route Groupsのサポート、`NuxtLink`に`prefetchOn`を追加、`@vue/runtime-core`の型を拡張しないように変更など


----

## Electron 32.0.0 | Electron
[www.electronjs.org/blog/electron-32-0](https://www.electronjs.org/blog/electron-32-0 "Electron 32.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 32リリース。
Chromium 128/Node.js 20.16.0/V8 12.8にアップデート、`webcontents.navigationHistory` APIの追加、`zstd`に対応など。
`File`オブジェクトから非標準な`path`プロパティを削除といった破壊的な変更も含まれている


----

## Deno 1.46: The Last 1.x Release
[deno.com/blog/v1.46](https://deno.com/blog/v1.46 "Deno 1.46: The Last 1.x Release")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.46リリース。
Denov 1.xの最終リリース。
`deno run`の`run`を省略できるように、`deno task`を`deno run`でも呼べるように、`--allow-*`/`--deny-*`の省略形を追加。
`--env`を`--env-file`に名前を変更、`deno fmt`がHTML/CSS/YAMLなどをサポート、`deno remove`/`deno clean`コマンドの追加。
`deno compile`がCode Signに対応、stdをStable変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## blocking=render: Why would you do that?! – Harry Roberts – Web Performance Consultant
[csswizardry.com/2024/08/blocking-render-why-whould-you-do-that/](https://csswizardry.com/2024/08/blocking-render-why-whould-you-do-that/ "blocking=render: Why would you do that?! – Harry Roberts – Web Performance Consultant")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

`blocking=render`について。
アンチフリッカースニペットのような意図的にページを非表示状態にしたい場合のユースケースについて


----

## Node.jsで型安全な環境変数を扱うスニペット | Web Scratch
[efcl.info/2024/08/24/type-safe-env/](https://efcl.info/2024/08/24/type-safe-env/ "Node.jsで型安全な環境変数を扱うスニペット | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.jsで環境変数をTypeScript定義、コマンドに対して環境変数のセットを型安全に渡す方法について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## vitest-dev/eslint-plugin-vitest: eslint plugin for vitest
[github.com/vitest-dev/eslint-plugin-vitest?tab&#x3D;readme-ov-file](https://github.com/vitest-dev/eslint-plugin-vitest?tab=readme-ov-file "vitest-dev/eslint-plugin-vitest: eslint plugin for vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">plugin</span></p>

vitest向けのESLintプラグイン

- [Vitest公式になったeslint-plugin-vitestを導入して、適切なVitestのお作法を学んでみる](https://zenn.dev/bs_kansai/articles/8ff70404804f60)

----
<h1 class="site-genre">書籍関係</h1>

----

## Tailwind CSSフロントエンド開発の教科書 | 仮 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4798070971/](https://www.amazon.co.jp/dp/4798070971/ "Tailwind CSSフロントエンド開発の教科書 | 仮 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css </span> <span class="jser-tag">book</span></p>

2024年12月31日発売
Tailwind CSSについての書籍


----
