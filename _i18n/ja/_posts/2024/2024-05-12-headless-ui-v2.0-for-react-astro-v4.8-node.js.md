---
title: "2024-05-12のJS: Headless UI v2.0 for React、Astro v4.8、外部パッケージに依存せずにNode.jsで使えるようになった機能"
author: "azu"
layout: post
date: 2024-05-12T06:47:28.714Z
category: JSer
tags:
- test
- nodejs
- bundler
- vite
- Hono

---

JSer.info #692 - Headless UI v2.0 for Reactがリリースされました。

- [Headless UI v2.0 for React - Tailwind CSS](https://tailwindcss.com/blog/headless-ui-v2)

Floating UIのanchor指定をサポート、Checkboxコンポーネント、Fieldsetコンポーネント、Comboboxが`virtual` propsをサポートなどの変更が含まれています。

---

Astro 4.8がリリースされました。

- [Astro 4.8 | Astro](https://astro.build/blog/astro-480/)

実験的な機能としてAstro Actions、Request Rewritingの追加が行われています。
また、パフォーマンスの改善や`injectRoute`のバグ修正などの変更が含まれています。

---

[Node.js の進化に伴い不要となったかもしれないパッケージたち](https://zenn.dev/morinokami/articles/npm-uninstall)という記事では、外部パッケージで提供されていた機能の一部がNode.jsにも実装されていることについて紹介されています。

- Fetch API
- `.env`ファイルの読み込み
- `util.styleText`
- `node:test`
- `--watch`フラグ
- `glob`
- `util.parseArgs`

などについて紹介されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v0.21.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.21.0](https://github.com/evanw/esbuild/releases/tag/v0.21.0 "Release v0.21.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.21.0リリース。
Stage 3のDecorator Proposalのサポート、プライベートメソッドの最適化、バグ修正など


----

## Release v1.6.0 · vitest-dev/vitest
[github.com/vitest-dev/vitest/releases/tag/v1.6.0](https://github.com/vitest-dev/vitest/releases/tag/v1.6.0 "Release v1.6.0 · vitest-dev/vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

vitest v1.6.0リリース。
`--standalone`グラフのサポート、Snapshotをカスタマイズできる`snapshotEnvironment` オプションの追加。
`browser.testerScripts`と`browser.indexScripts`オプションの追加。


----

## Release v4.3.0 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.3.0](https://github.com/honojs/hono/releases/tag/v4.3.0 "Release v4.3.0 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">ReleaseNote</span></p>

Hono v4.3.0リリース。
Responseに対するクライアント側での型推論の改善、`hono/jsx`のReactとの互換性改善、`createFactory`の追加など


----

## Astro 4.8 | Astro
[astro.build/blog/astro-480/](https://astro.build/blog/astro-480/ "Astro 4.8 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 4.8リリース。
実験的な機能としてAstro Action、Request Rewritingの追加。
パフォーマンスの改善や`injectRoute`のバグ修正など


----

## Node.js — Node v20.13.0 (LTS)
[nodejs.org/en/blog/release/v20.13.0](https://nodejs.org/en/blog/release/v20.13.0 "Node.js — Node v20.13.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.13.0リリース。
Bufferの`base64`と`base64url`のパフォーマンス改善、`CustomEvent`と`node --watch`をStableに変更、`fs/promises`のスタックトレースの追加など


----

## Release v1.44.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.44.0](https://github.com/microsoft/playwright/releases/tag/v1.44.0 "Release v1.44.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.44.0リリース。
アクセシビリティ用のAssertionを追加、`page.addLocatorHandler`に`noWaitAfter`オプションを追加、`page.removeLocatorHandler`メソッドを追加。
前回失敗したテストだけを実行する`--last-failed`フラグの追加など


----

## Release v2.3.0 · mswjs/msw
[github.com/mswjs/msw/releases/tag/v2.3.0](https://github.com/mswjs/msw/releases/tag/v2.3.0 "Release v2.3.0 · mswjs/msw")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

msw 2.3.0リリース。
ハンドラー内でのnhandled exceptionは500エラーとなるように変更、`unhandledException`イベントを追加など


----

## Release v9.0.0 · sindresorhus/execa
[github.com/sindresorhus/execa/releases/tag/v9.0.0](https://github.com/sindresorhus/execa/releases/tag/v9.0.0 "Release v9.0.0 · sindresorhus/execa")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

execa v9.0.0リリース。
zx的なTemplate Literalでのコマンド実行をサポート、行ごとに出力を処理できるように、入力や出力のフィルター、`verbose`モードの改善など

- [Execa 9: our biggest release. Execa runs commands in your scripts. | by ehmicky | Medium](https://medium.com/@ehmicky/execa-9-release-d0d5daaa097f "Execa 9: our biggest release. Execa runs commands in your scripts. | by ehmicky | Medium")

----

## Bun v1.1.8 | Bun Blog
[bun.sh/blog/bun-v1.1.8](https://bun.sh/blog/bun-v1.1.8 "Bun v1.1.8 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.8リリース。
`process.on("uncaughtException")`と`process.on("unhandledRejection")`のサポート。
`node:zlib`でBrotli APIをサポート、Bun APIがExplicit Resource Managementをサポートなど


----

## Headless UI v2.0 for React - Tailwind CSS
[tailwindcss.com/blog/headless-ui-v2](https://tailwindcss.com/blog/headless-ui-v2 "Headless UI v2.0 for React - Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Headless UI v2.0リリース。
Floating UIのanchor指定をサポート、Checkboxコンポーネント、Fieldsetコンポーネント、Comboboxが`virtual` propsをサポートなど


----

## Release 7.0.0 · jasonkuhrt/graphql-request
[github.com/jasonkuhrt/graphql-request/releases/tag/7.0.0](https://github.com/jasonkuhrt/graphql-request/releases/tag/7.0.0 "Release 7.0.0 · jasonkuhrt/graphql-request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

graphql-request 7.0リリース。
cross-fetchのpolyfillを削除、Pure ESMに変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Node.js の進化に伴い不要となったかもしれないパッケージたち
[zenn.dev/morinokami/articles/npm-uninstall](https://zenn.dev/morinokami/articles/npm-uninstall "Node.js の進化に伴い不要となったかもしれないパッケージたち")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.jsのコアモジュールなどに実装されたパッケージの機能紹介。
Fetch API、`.env`のロード、`util.styleText`、`node:test`、`--watch`フラグ、`glob`、`util.parseArgs`などについて


----

## TypeScript の型検査にかかる時間を短縮した話
[zenn.dev/knowledgework/articles/speedup-typecheck](https://zenn.dev/knowledgework/articles/speedup-typecheck "TypeScript の型検査にかかる時間を短縮した話")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの型チェックのパフォーマンスチェックと改善について


----

## Misconceptions about CSS Specificity – Bram.us
[www.bram.us/2024/05/05/misconceptions-about-css-specificity/](https://www.bram.us/2024/05/05/misconceptions-about-css-specificity/ "Misconceptions about CSS Specificity – Bram.us")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSのSpecificityについて


----

## Monitor Third-Party Resources that Impact UX with Playwright
[www.checklyhq.com/blog/how-playwright-can-monitor-third-party-resources/](https://www.checklyhq.com/blog/how-playwright-can-monitor-third-party-resources/ "Monitor Third-Party Resources that Impact UX with Playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

PlaywrightのRequest Block/Delayを使ってユーザー影響のあるサードパーティスクリプトを特定する方法について


----

## Why Patching Globals Is Harmful - kettanaito.com
[kettanaito.com/blog/why-patching-globals-is-harmful](https://kettanaito.com/blog/why-patching-globals-is-harmful "Why Patching Globals Is Harmful - kettanaito.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Fetch</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Global APIにmonkey patchする弊害について。
Fetch APIの仕様を各種上書きしているReact/Next.js/Bunについて


----
