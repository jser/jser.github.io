---
title: "2024-10-16のJS: Deno v2、TypeScript 5.7 Beta、ES2025に入る5つのProposal"
author: "azu"
layout: post
date: 2024-10-15T15:41:43.168Z
category: JSer
tags:
- deno
- Tools
- Bun
- css
- ESLint

---

JSer.info #711 - Deno v2.0.0がリリースされました

- [Announcing Deno 2](https://deno.com/blog/v2.0)
- [Deno 2.0 Release Candidate](https://deno.com/blog/v2.0-release-candidate)

Node.jsとの互換性の改善、JSRのサポート改善、Workspaceのサポートなどが行われています。
Deno 1.xから2.xへのマイグレーションガイドも公開されています。

- [Deno 1.x to 2.x Migration Guide](https://docs.deno.com/runtime/reference/migration_guide/)

---

TypeScript 5.7 Betaがリリースされました

- [Announcing TypeScript 5.7 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/)

初期化されてない変数のチェック、相対パスの`.ts`を出力時に`.js`へと書き換える`--rewriteRelativeImportExtensions`フラグの追加されています。
また、`--target es2024`のサポート、Node.js 22のV8 Compile Cacheをサポートして実行速度の改善なども行われています。。

---

2024年10月のTC39のミーティングで5つのProposalがStage 4になりました。

- [ECMAScript proposal updates @ 2024-10 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update)

[Promise.try](https://github.com/tc39/proposal-promise-try)/[Import Attributes](https://github.com/tc39/proposal-import-attributes)/[RegExp Modifiers](https://github.com/tc39/proposal-regexp-modifiers)/[Sync Iterator helpers](https://github.com/tc39/proposal-iterator-helpers)/[JSON Modules](https://github.com/tc39/proposal-json-modules)がそれぞれStage 4になりました。
そのため、これらの機能はES2025に含まれることになります。

それ以外にもすでにStage 4になっているProposalは次のページで確認できます。

- [proposals/finished-proposals.md at main · tc39/proposals](https://github.com/tc39/proposals/blob/main/finished-proposals.md)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bun v1.1.30 | Bun Blog
[bun.sh/blog/bun-v1.1.30](https://bun.sh/blog/bun-v1.1.30 "Bun v1.1.30 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">css</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.30リリース。
CSSのparseとbundleのサポート、`bun publish`コマンドの追加、`bun build --bytecode --compile`のパフォーマンス改善。
`--compile`フラグなしの`--bytecode`フラグをサポート、`bun build --format=cjs`のサポートなど


----

## Announcing Deno 2
[deno.com/blog/v2.0](https://deno.com/blog/v2.0 "Announcing Deno 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.0リリース。
グローバルな`window`を削除/`process`を追加、`deno add`で`jsr:`と`npm:`の識別子を指定して追加に対応、パーミッションの指定に関する挙動の変更、`deno bundle`コマンドの削除など

- [Deno 2.0 Release Candidate](https://deno.com/blog/v2.0-release-candidate "Deno 2.0 Release Candidate")
- [Deno 1.x to 2.x Migration Guide](https://docs.deno.com/runtime/reference/migration_guide/ "Deno 1.x to 2.x Migration Guide")

----

## Release eslint-plugin-react-hooks@5.0.0 (Oct 11, 2024) · facebook/react
[github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0](https://github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0 "Release eslint-plugin-react-hooks@5.0.0 (Oct 11, 2024) · facebook/react")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

eslint-plugin-react-hooks 5.0.0リリース。
ESLint v9のサポート、コンポーネント名は大文字で開始するルールを追加、React 19の対応、`useEffect(fn, undefined)`を許可するように変更など


----

## Release v1.48.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.48.0](https://github.com/microsoft/playwright/releases/tag/v1.48.0 "Release v1.48.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.48.0リリース。
`page.routeWebSocket()` APIを追加、`page.requestGC()`メソッドの追加、`location`オプションの追加など


----

## Release Notes for Safari Technology Preview 205 | WebKit
[webkit.org/blog/15999/release-notes-for-safari-technology-preview-205/](https://webkit.org/blog/15999/release-notes-for-safari-technology-preview-205/ "Release Notes for Safari Technology Preview 205 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 205リリース。
`Math.sumPrecise`、`Iterator.prototype.reduce`のサポート。
WebAssemblyの例外処理をサポート


----

## Announcing TypeScript 5.7 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/ "Announcing TypeScript 5.7 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.7 Betaリリース。
初期化されてない変数のチェック、相対パスの`.ts`を出力時に`.js`へと書き換える`--rewriteRelativeImportExtensions`フラグの追加。
`--target es2024`のサポート、Node.js 22のV8 Compile Cacheをサポートして実行速度の改善など


----

## Release v0.81.0 · facebook/metro
[github.com/facebook/metro/releases/tag/v0.81.0](https://github.com/facebook/metro/releases/tag/v0.81.0 "Release v0.81.0 · facebook/metro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">bundler</span></p>

metro 0.81.0リリース。
Node.js 18未満のサポート終了、`#`から開始するパスは将来のsubpath importサポートのため予約されるようになるなど


----

## Release v2.3.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v2.3.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.3.0 "Release v2.3.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v2.3.0リリース。
`upsertQueryEntries`を追加、`prepareHeaders`オプションの改善など


----

## ECMAScript proposal updates @ 2024-10 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-10 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2024年10月のTC39 MeetingでのECMAScript ProposalのStatus変更のまとめ。
`Promise.try`/Import attributes/RegExp Modifiers/Iterator helpers/JSON modulesがStage 4となりES2025に入る


----
<h1 class="site-genre">アーティクル</h1>

----

## The Popover API: Your New Best Friend for Tooltips
[www.voorhoede.nl/en/blog/the-popover-api-your-new-best-friend-for-tooltips/](https://www.voorhoede.nl/en/blog/the-popover-api-your-new-best-friend-for-tooltips/ "The Popover API: Your New Best Friend for Tooltips")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">PostCSS</span> <span class="jser-tag">article</span></p>

Popover APIを使ったツールチップの表示について


----

## Deno v2がリリース🎉 - Deno v1.0.0の頃からの変化と現在のプラクティスについて
[zenn.dev/uki00a/articles/deno-v2-what-has-changed-from-v1](https://zenn.dev/uki00a/articles/deno-v2-what-has-changed-from-v1 "Deno v2がリリース🎉 - Deno v1.0.0の頃からの変化と現在のプラクティスについて")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">article</span></p>

Deno v1からv2への変化について


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## trynova/nova: JS engine lolz
[github.com/trynova/nova](https://github.com/trynova/nova "trynova/nova: JS engine lolz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span></p>

Rustで書かれたJavaScriptエンジン。
データ指向なデザインで実装されている


----
