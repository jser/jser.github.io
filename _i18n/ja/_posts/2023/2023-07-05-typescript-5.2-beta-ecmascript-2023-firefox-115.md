---
title: "2023-07-05のJS: TypeScript 5.2 Beta、ECMAScript 2023、Firefox 115"
author: "azu"
layout: post
date : 2023-07-05T06:01:57.428Z
category: JSer
tags:
- TypeScript
- ECMAScript
- browser
- node.js
- game

---

JSer.info #650 - TypeScript 5.2 Betaがリリースされました。

- [Announcing TypeScript 5.2 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/)

Stage 3 ProposalのExplicit Resource Management(`using`宣言)のサポート、同じくStage 3のDecorator Metadataのサポートされています。
また、Tupleにおけるラベルありなしの組み合わせの制限を削除、配列のUnion型の扱いの改善なども含まれています。

---

ECMAScript 2023がecma GAで承認されたため、正式にリリースされました。

- [Ecma International approves new standards - Ecma International](https://www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/)
- [Release ES2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023)

主な変更点は次のとおりです。

- Proposal: [Hashbang Grammar](https://github.com/tc39/proposal-hashbang)
- 対応ブラウザ: [モダンブラウザ全部](https://caniuse.com/mdn-javascript_grammar_hashbang_comments)

```js
#!test
// #! as single line comment
```


- Proposal: [Change Array by copy](https://github.com/tc39/proposal-change-array-by-copy)
- 対応ブラウザ: モダンブラウザ全部
  - Firefox 115でサポート

```js
const sequence = [1, 2, 3];
sequence.toReversed(); // => [3, 2, 1]
sequence; // => [1, 2, 3]

const outOfOrder = new Uint8Array([3, 1, 2]);
outOfOrder.toSorted(); // => Uint8Array [1, 2, 3]
outOfOrder; // => Uint8Array [3, 1, 2]

const correctionNeeded = [1, 1, 3];
correctionNeeded.with(1, 2); // => [1, 2, 3]
correctionNeeded; // => [1, 1, 3]
```

- Proposal: [Array.prototype.findLast and Array.prototype.findLastIndex](https://github.com/tc39/proposal-array-find-from-last)
- 対応ブラウザ: [モダンブラウザ全部](https://caniuse.com/?search=Array.prototype.findLast)

```js
const array = [{ value: 1 }, { value: 2 }, { value: 3 }, { value: 4 }];
array.findLastIndex(n => n.value % 2 === 1); // => 2
array.findLast(n => n.value % 2 === 1); // => { value: 3 }
```

- Proposal: [Symbols as WeakMap keys](https://github.com/tc39/proposal-symbols-as-weakmap-keys)
- 対応ブラウザ: [Firefox以外](https://caniuse.com/mdn-javascript_builtins_weakmap_symbol_as_keys)


```js
const map = new WeakMap();
const s = Symbol("desc");
map.set(s, {})
map.get(s); // => {}
```

---

Firefox 115がリリースされました。

- [Firefox 115.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/115.0/releasenotes/)

macOS 10.12/10.13/10.14、Windows7/8/8.1がサポートされる最後のバージョンとなります
`contenteditable`におけるノード分割と結合の挙動を他のブラウザと揃えるように変更。
`Array.fromAsync()`のサポート、ES2023の`Array.toReversed()`/`.toSorted()`/`.toSpliced()`/`.with()`のサポート。
`Response.json()`、`URL.canParse()`のサポートなどが追加されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v8.0.0-alpha.0 · pixijs/pixijs
[github.com/pixijs/pixijs/releases/tag/v8.0.0-alpha.0](https://github.com/pixijs/pixijs/releases/tag/v8.0.0-alpha.0 "Release v8.0.0-alpha.0 · pixijs/pixijs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

PixiJS v8.0.0-alpha.0リリース。
WebGPUレンダラーとWebGLレンダラーの書き直し、変更されたものだけ更新するリアクティブレンダラー、高度なBlendモードをの追加など。
初期化方法を非同期に変更、Graphics APIの刷新など


----

## ESLint v8.44.0 released - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2023/06/eslint-v8.44.0-released/](https://eslint.org/blog/2023/06/eslint-v8.44.0-released/ "ESLint v8.44.0 released - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.44.0リリース。
`eslint.config.js`でPromiseを受け入れることで設定ファイル(CJS)からESMをロードできるように、espreeがRegExpの`v`フラグをサポート。
`context.parserServices`プロパティを非推奨化など


----

## Announcing TypeScript 5.2 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/ "Announcing TypeScript 5.2 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.2 Betaリリース。
Stage 3 ProposalのExplicit Resource Management(`using`宣言)のサポート、Decorator Metadataのサポート。
Tupleにおけるラベルありなしの組み合わせの制限を削除、配列のUnion型の扱いの改善など


----

## Ecma International approves new standards - Ecma International
[www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/](https://www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/ "Ecma International approves new standards - Ecma International")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2023がecma GAで承認されたため、正式にリリース。

- [Release ES2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023 "Release ES2023 · tc39/ecma262")

----

## Release v4.0.0 · lquixada/cross-fetch
[github.com/lquixada/cross-fetch/releases/tag/v4.0.0](https://github.com/lquixada/cross-fetch/releases/tag/v4.0.0 "Release v4.0.0 · lquixada/cross-fetch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

cross-fetch 4.0.0リリース。
Node.js 10と12のサポート終了、Node.js 18と20のサポート、Service WorkerとCloudflare Workersのサポートなど


----

## Release v8.6.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v8.6.6](https://github.com/pnpm/pnpm/releases/tag/v8.6.6 "Release v8.6.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">performance</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v8.6.6リリース。
パフォーマンスの改善など


----

## Release v29.6.0 · jestjs/jest
[github.com/jestjs/jest/releases/tag/v29.6.0](https://github.com/jestjs/jest/releases/tag/v29.6.0 "Release v29.6.0 · jestjs/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Jest 29.6.0リリース。
Current Testでのsnapshotテストのサポート、非同期でエラーがthrowされた場合の問題を`rejectionHandled`イベントを使うことで修正など


----

## Release 0.2.5 · web-infra-dev/rspack
[github.com/web-infra-dev/rspack/releases/tag/0.2.5](https://github.com/web-infra-dev/rspack/releases/tag/0.2.5 "Release 0.2.5 · web-infra-dev/rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span></p>

rspack 0.2.5リリース。
Web Workerのサポート、entryの`filename`オプションのサポート、HMRでCJSとESMが混在している場合にwarningを出すようになるなど


----

## Firefox 115.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/115.0/releasenotes/](https://www.mozilla.org/en-US/firefox/115.0/releasenotes/ "Firefox 115.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 115リリース。
macOS 10.14以下、Windows7/8/8.1がサポートされる最後のバージョンとなる。
`contenteditable`におけるノード分割と結合の挙動を他のブラウザと揃えるように変更。
` Array.fromAsync()`のサポート、ES2023の`Array.toReversed()`/`.toSorted()`/`.toSpliced()`/`.with()`のサポート。
`Response.json()`、`URL.canParse()`のサポートなど。

- [Firefox users on macOS 10.12, 10.13 and 10.14 moving to Extended Support Release | Firefox ヘルプ](https://support.mozilla.org/ja/kb/firefox-users-macos-1012-1013-1014-moving-to-extended-support "Firefox users on macOS 10.12, 10.13 and 10.14 moving to Extended Support Release | Firefox ヘルプ")
- [Firefox users on Windows 7, 8 and 8.1 moving to Extended Support Release | Firefox ヘルプ](https://support.mozilla.org/ja/kb/firefox-users-windows-7-8-and-81-moving-extended-support "Firefox users on Windows 7, 8 and 8.1 moving to Extended Support Release | Firefox ヘルプ")
- [Firefox 115 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/115 "Firefox 115 for developers - Mozilla | MDN")
- [Intent to Ship: Compatible join and split node direction in HTML editor](https://groups.google.com/a/mozilla.org/g/dev-platform/c/Ob-T1HSe-4I?pli=1 "Intent to Ship: Compatible join and split node direction in HTML editor")

----
<h1 class="site-genre">アーティクル</h1>

----

## CommonJS is not going away | Bun Blog
[bun.sh/blog/commonjs-is-not-going-away](https://bun.sh/blog/commonjs-is-not-going-away "CommonJS is not going away | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">article</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span></p>

BunがCommonJSをサポートするのはなぜかについて。
CommonJSとECMAScript Moduleを比べると同期と非同期の違いがあるため起動時のロード時間が異なることや、すでに多くのCommonJSモジュールがあるため

- [CommonJS is hurting JavaScript](https://deno.com/blog/commonjs-is-hurting-javascript "CommonJS is hurting JavaScript")

----

## Useful DevTools Tips and Tricks — Smashing Magazine
[www.smashingmagazine.com/2023/06/popular-devtools-tips/](https://www.smashingmagazine.com/2023/06/popular-devtools-tips/ "Useful DevTools Tips and Tricks — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

ブラウザの開発者ツールのTipsをまとめた記事


----

## Architecture of an early stage SAAS | Feelback Blog
[www.feelback.dev/blog/feelback-saas-launch-architecture/](https://www.feelback.dev/blog/feelback-saas-launch-architecture/ "Architecture of an early stage SAAS | Feelback Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">article</span> <span class="jser-tag">node.js</span></p>

fly.io と Node.jsを使ったSaaSのアーキテクチャ解説。
fly.ioを使った低コストなインフラの構成。
クライアントとサーバどちらもNode.jsで、型付きRPCとしてhttpcを利用。
管理画面はCloudflare Pagesにありhttpcを使って通信、ホームページやドキュメントにはAstroを利用している。
また、利用している外部サービスやmonorepoの構造についてなど

- [httpc: function-based API made easy](https://httpc.dev/ "httpc: function-based API made easy")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## giuseppelt/httpc: Build function-based API with minimal code and end-to-end type safety
[github.com/giuseppelt/httpc](https://github.com/giuseppelt/httpc "giuseppelt/httpc: Build function-based API with minimal code and end-to-end type safety")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

TypeScriptで書いたサーバの関数をクライアントから同じように呼び出せるRPCツールキット。
サーバで関数をexportしたコードからクライアントコードを生成する仕組みによって、サーバの関数と同じ関数と引数でAPIコールができる。


----
