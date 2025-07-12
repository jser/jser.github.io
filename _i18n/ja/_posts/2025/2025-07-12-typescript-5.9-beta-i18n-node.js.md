---
title: "2025-07-12のJS: TypeScript 5.9 Beta、i18nとローカライズ、Node.jsのモダンな機能"
author: "azu"
layout: post
date: 2025-07-12T07:46:02.849Z
category: JSer
tags:
- TypeScript
- nodejs
- MCP
- Vue
- vercel

---

JSer.info #741 - TypeScript 5.9 Betaがリリースされました。

- [Announcing TypeScript 5.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/)

`tsc --init`で生成する設定の変更、`import defer`構文のサポート、`--module node20`オプションの追加などが含まれています。また、型チェックの改善やパフォーマンスの向上も行われています。

---

Patreonの国際化とローカライズの実装についての記事が公開されています。

- [4 Untranslatable Words Behind Patreon's Internationalization Overhaul](https://www.patreon.com/posts/133137028)

条件式で文を分ける際の注意点、数値表現でのIntl APIの活用、複数形表現のローカライズなど、実践的なベストプラクティスが紹介されています。ローカライズシステム移行時に起きた問題と解決方法についても書かれています。

---

次の記事では、2025年に向けたNode.jsのモダンな機能とパターンについてまとめられています。

- [Modern Node.js Patterns for 2025](https://kashw1n.com/blog/nodejs-2025/)

ESM、built-in fetch API、Worker threadsによる並列処理、AbortControllerによるキャンセル処理など、最新のNode.js機能の活用方法が説明されています。Permission modelやSingle Executable Applicationsなどの新機能についても触れられています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 5.9 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/ "Announcing TypeScript 5.9 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.9 Betaリリース。
`tsc --init`で生成する設定を変更、`import defer`のサポート、`--module node20`のサポートなど


----

## The future of Nuxt​ · nuxt/nuxt · Discussion #32559
[github.com/nuxt/nuxt/discussions/32559](https://github.com/nuxt/nuxt/discussions/32559 "The future of Nuxt​ · nuxt/nuxt · Discussion #32559")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">vercel</span> <span class="jser-tag">news</span></p>

Nuxt.jsを開発してるNuxtLabsがVercelに買収された

- [NuxtLabs joins Vercel - Vercel](https://vercel.com/blog/nuxtlabs-joins-vercel "NuxtLabs joins Vercel - Vercel")

----

## Node.js — Node v24.4.0 (Current)
[nodejs.org/en/blog/release/v24.4.0](https://nodejs.org/en/blog/release/v24.4.0 "Node.js — Node v24.4.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.4.0リリース。
`fs.mkdtempDisposableSync`の追加、`--watch-kill-signal`フラグの追加など


----

## Release v5.100.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.100.0](https://github.com/webpack/webpack/releases/tag/v5.100.0 "Release v5.100.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack v5.100.0リリース。
HMRのES Modules outputのサポート、`using`のサポート、Defer Module Evaluationのサポート。
`virtual:`スキーマをサポートするVirtualUrlPluginを追加など


----

## Release v1.54.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.54.0](https://github.com/microsoft/playwright/releases/tag/v1.54.0 "Release v1.54.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.54.0リリース。
`partitionKey`オプションの追加、html reporterに`noSnippets`オプションを追加。
`--user-data-dir`フラグでユーザーデータディレクトリを指定できるようになるなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog
[blog.nginx.org/blog/quickjs-engine-support-for-njs](https://blog.nginx.org/blog/quickjs-engine-support-for-njs "Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nginx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

NGINXのnjsはQuickJSのエンジンを選択して利用できるようになった


----

## JavaScript scope hoisting is broken
[devongovett.me/blog/scope-hoisting.html](https://devongovett.me/blog/scope-hoisting.html "JavaScript scope hoisting is broken")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">article</span></p>

Rollupなどが行うScope Hoistingは、Code splittingと概念が反発しあっているという問題について。
モジュールの実行順序の問題やモジュールを関数でラップした時の最適化の問題についてなど


----

## 4 Untranslatable Words Behind Patreon's Internationalization Overhaul
[www.patreon.com/posts/133137028](https://www.patreon.com/posts/133137028 "4 Untranslatable Words Behind Patreon's Internationalization Overhaul")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">i18n</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ローカライズされるコンテンツを作成するときにきをつけることについて。

- 条件式で文を分けるときは、完全な文として分ける
- 数値表現は常にIntlを利用する
- 複数系の表現もローカライズする

ローカライズシステム移行時に起きた問題や解決方法についてなど


----

## Modern Node.js Patterns for 2025
[kashw1n.com/blog/nodejs-2025/](https://kashw1n.com/blog/nodejs-2025/ "Modern Node.js Patterns for 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

最近のNode.jsで利用できる機能について。
ESM、`node:` prefix、built-in fetch APIやtesting frameworkの使用、top-level await。
Worker threadsによる並列処理、AbortControllerによるキャンセル処理、async iteratorsによるイベント処理。
Permission model、import mapsによるモジュール解決、Single Executable Applicationsによる単一実行可能ファイルの作成などについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## xmcp — The TypeScript MCP framework
[xmcp.dev/](https://xmcp.dev/ "xmcp — The TypeScript MCP framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">MCP</span> <span class="jser-tag">library</span></p>

TypeScriptのMCPサーバフレームワーク


----

## typescript-eslint/tsgolint: ✨ Experimental proof-of-concept typescript-go powered JS/TS linter written in Go
[github.com/typescript-eslint/tsgolint](https://github.com/typescript-eslint/tsgolint "typescript-eslint/tsgolint: ✨ Experimental proof-of-concept typescript-go powered JS/TS linter written in Go")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">library</span></p>

TSLintの ルールをtsgoで動くようにしてどれぐらい早くなるかの試験的な実装。
ESLintのASTへの変換をせずにTS ASTをそのまま扱うようにする変更も行なっていて、20-40倍程度早くチェックできている


----

## josdejong/jsonrepair: Repair invalid JSON documents
[github.com/josdejong/jsonrepair](https://github.com/josdejong/jsonrepair "josdejong/jsonrepair: Repair invalid JSON documents")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

InvalidなJSON文字列をJSONに修復するツール


----
