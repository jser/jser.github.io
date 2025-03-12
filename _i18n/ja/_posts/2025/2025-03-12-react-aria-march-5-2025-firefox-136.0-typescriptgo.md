---
title: "2025-03-12のJS: React Aria March 5, 2025、Firefox 136.0、TypeScriptコンパイラをGoに移植"
author: "azu"
layout: post
date: 2025-03-12T03:35:33.452Z
category: JSer
tags:
- React
- TypeScript
- Vue
- Electron
- pnpm

---

JSer.info #728 - React Aria March 5, 2025リリースされました

- [March 5, 2025 Release – React Spectrum Releases](https://react-spectrum.adobe.com/releases/2025-03-05.html)

Toast/Tree/Virtualizerコンポーネントを追加、AutocompleteをMenu/Selectなどと組み合わせて利用できるようになりました。
また、`<Pressable>`/`<Focusable>`の追加、`usePress`のリファクタリングなどが含まれています。
その他には、ドキュメントをTailwind v4に対応など

---

Firefox 136.0リリースされました

- [Firefox 136.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/136.0/releasenotes/)
- [Firefox 136 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/136)

HTMLの`autocorrect`属性をサポート、`Intl.DurationFormat`のサポート、Data URLsの最大サイズを32MBからChromeと同じ512MBに変更されています。
Cookie Storage APIのサポート、HTTPS-Firstに変更されています。
実験的な機能として、`Error.captureStackTrace()`のサポート、`Clear-Site-Data`ヘッダのサポート、SVGの`<discard>`要素のサポートなどが含まれています。

----

TypeScriptコンパイラのGo言語へのポートの計画が公開されました。

- [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScriptの型チェックやLSPのパフォーマンスを改善するために、TypeScriptコンパイルやLSPなどのツールをGo言語へポートするという計画が公開されました。
移植したnative版をTypeScript 7としてリリースする予定で、native版が安定するまではJS版もメンテナンスしていく予定となっています。
TypeScript 7が出たあとも、移行の問題がなくなるまでJS版をメンテして、99.99%はそのまま移行できることを目指しているようです。

- https://github.com/microsoft/typescript-go

> "Why a port instead of a rewrite? What's the difference? · microsoft/typescript-go · Discussion #410"
> https://github.com/microsoft/typescript-go/discussions/411

なぜ書き直しではなく移植を選んだのかについては、TypeScriptのコードベースのサイズの大きさや、TypeScriptは仕様があるわけではなくリファレンス実装のみであるという理由などが挙げらています。

> Why Go? #411 
> https://github.com/microsoft/typescript-go/discussions/411

Goを選んだ理由として、GCがあることやセマンティクスとコードの構造がJSと似ているため、移植性が高いという理由が挙げられています。

- [TypeScript is being ported to Go | interview with Anders Hejlsberg - YouTube](https://www.youtube.com/watch?v=10qowKUW82U)

C#はOOP言語なので、既存のTypeScriptコンパイラのコードを移植するには、構造を変更する必要があるため選択肢にするのが難しかったという話がされています。
また、TypeScriptコンパイラはGCなどに依存しているため、Rustなどの言語は選択肢にするのが難しかったという話もされています。
書き直しであれば、最初からGC/循環参照グラフに依存しないような構造にしていたなどの話もされています。

まだ、具体的なリリーススケジュールは未定ですが、基本的には移行がスムーズに行えるようにすることを目指しているようです。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## March 5, 2025 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2025-03-05.html](https://react-spectrum.adobe.com/releases/2025-03-05.html "March 5, 2025 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria March 5, 2025リリース。
Toast/Tree/Virtualizerコンポーネントを追加、AutocompleteをMenu/Selectなどと組み合わせて利用できるように。
`<Pressable>`/`<Focusable>`の追加、
`usePress`のリファクタリング。
ドキュメントをTailwind v4に対応など


----

## Electron 35.0.0 | Electron
[www.electronjs.org/blog/electron-35-0](https://www.electronjs.org/blog/electron-35-0 "Electron 35.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 35.0.0リリース。
Chromium 134/Node.js 22.14.0/V8 13.5へアップデート、Service Worker Preload Scriptsのサポートなど


----

## Release v3.16.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.16.0](https://github.com/nuxt/nuxt/releases/tag/v3.16.0 "Release v3.16.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v3.16.0リリース。
`create-nuxt`パッケージの追加、パフォーマンスの改善、delayed/lazy hydrationのサポートなど


----

## Release pnpm 10.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.6.0](https://github.com/pnpm/pnpm/releases/tag/v10.6.0 "Release pnpm 10.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.6.0リリース。
`.npmrc`の設定を全て`pnpm-workspace.yaml`に記述できるように


----

## Release v1.51.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.51.0](https://github.com/microsoft/playwright/releases/tag/v1.51.0 "Release v1.51.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.51.0リリース。
`browserContext.storageState()`がIndexedDBをサポート、`filter({ visible })`を追加、`expect(page).toHaveURL(fn)`をサポート。
LLM向けのCopy promptをレポーターに追加など


----

## Release @ark-ui/react@5.0.0 · chakra-ui/ark
[github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%405.0.0](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%405.0.0 "Release @ark-ui/react@5.0.0 · chakra-ui/ark")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Solid</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ark UI v5リリース。
パフォーマンスとBundle Sizeの改善、コンポーネントにデフォルト値を指定するオプションの追加など


----

## Firefox 136.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/136.0/releasenotes/](https://www.mozilla.org/en-US/firefox/136.0/releasenotes/ "Firefox 136.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 136リリース。
HTMLの`autocorrect`属性をサポート、`Intl.DurationFormat`のサポート、Data URLsの最大サイズを32MBからChromeと同じ512MBに変更。
Cookie Storage APIのサポート、HTTPS-Firstに変更。
実験的な機能として、`Error.captureStackTrace()`のサポート、`Clear-Site-Data`ヘッダのサポート、SVGの`<discard>`要素のサポートなど

- [Firefox 136 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/136 "Firefox 136 for developers - Mozilla | MDN")

----

## Bun v1.2.5 | Bun Blog
[bun.sh/blog/bun-v1.2.5](https://bun.sh/blog/bun-v1.2.5 "Bun v1.2.5 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.5リリース。
Node-APIとの互換性の改善、`node:timers`の追加、`Bun.CSRF`の追加。
dev serverがsvelteをサポート、CSS modulesのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## A 10x Faster TypeScript - TypeScript
[devblogs.microsoft.com/typescript/typescript-native-port/](https://devblogs.microsoft.com/typescript/typescript-native-port/ "A 10x Faster TypeScript - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

TypeScriptの型チェックやLSPのパフォーマンスを改善するために、TypeScriptコンパイルやLSPなどのツールをGo言語へポートするという話。
移植したnative版をTypeScript 7としてリリースする予定で、native版が安定するまではJS版もメンテナンスしていく予定。


----

## Split Route Modules | Remix
[remix.run/blog/split-route-modules](https://remix.run/blog/split-route-modules "Split Route Modules | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Router v7.2.0で追加されたSplit Route Modulesについて。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## microsoft/typescript-go: Staging repo for development of native port of TypeScript
[github.com/microsoft/typescript-go](https://github.com/microsoft/typescript-go "microsoft/typescript-go: Staging repo for development of native port of TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">golang</span> <span class="jser-tag">Tools</span></p>

TypeScriptをGo言語にポートした実装。
型チェック以外は並行に処理できる。型チェックはいくつかのブロックに分けて処理するようになっている。

- [A 10x faster TypeScript - YouTube](https://www.youtube.com/embed/pNlq-EVld70?si=OaEgTg6ROtfYDYLt "A 10x faster TypeScript - YouTube")

----

## Pikku - A Function-First Framework for Node.js | Pikku
[pikku.dev/](https://pikku.dev/ "Pikku - A Function-First Framework for Node.js | Pikku")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

TypeScriptで書かれたウェブフレームワーク。
ただの関数としてハンドラーなどを定義できる。TypeScriptのコードからJSONスキーマを生成してバリデーションを行え、クライアントコードも自動的に生成される


----
