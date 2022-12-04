---
title: "2022-03-01のJS: Redux Toolkit 1.8.0、Node.js 17.6.0、CSS Cascade Layers"
author: "azu"
layout: post
date : 2022-02-28T12:49:04.690Z
category: JSer
tags:
- node.js
- TypeScript
- Tools
- pnpm
- Chrome

---

JSer.info #581 - Redux Toolkit 1.8.0がリリースされました。

- [Release v1.8.0 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.8.0)

1.8.0では、新しい非同期Middlewareとして`createListenerMiddleware`が追加されています。

- [createListenerMiddleware | Redux Toolkit](https://redux-toolkit.js.org/api/createListenerMiddleware)

`createListenerMiddleware`は[redux-saga](https://github.com/redux-saga/redux-saga)や[redux-observable](https://redux-observable.js.org/)など同じく非同期処理を扱うためのMiddlewareです。
シンプルな`dispatch`や`getState`などのAPIや、redux-sagaをインスパイアした`take`や[Temporal](https://docs.temporal.io/docs/typescript/workflows#condition)をインスパイアした`condition`など複雑なタスクを扱うAPIも持っています。

次の動画で、この`createListenerMiddleware`がどのように作られたのかを紹介しています。

- [Redux Insights: the Redux Toolkit &quot;action listener&quot; middleware - YouTube](https://www.youtube.com/watch?v=D5WOry6gw9c)
- [New experimental &quot;action listener middleware&quot; package available · Discussion #1648 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/discussions/1648)

---

Node.js 17.6.0がリリースされました。

- [Node v17.6.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v17.6.0/)

[Node v17.5.0](https://nodejs.org/en/blog/release/v17.5.0/)でStreaｍに対して現在Stage 2のECMAScript Proposalである[Iterator Helpers](https://github.com/tc39/proposal-iterator-helpers)が実装されていました。
しかし、仕様に準拠した実装をした場合に[mongoose](https://github.com/Automattic/mongoose/issues/11377)などのモジュールが動かなくなるリグレッションが発生したため、[仕様への準拠を一部revert](https://github.com/nodejs/node/pull/41931)しています。

- [Regression in Node 17.5, Assigning a function to prototype of an Object results in a TypeError: Cannot assign to read only property 'x' of object 'y' at Object.<anonymous> · Issue #41926 · nodejs/node](https://github.com/nodejs/node/issues/41926)

具体的にはIterator Helperの仕様では、`map`などのメソッドは[`{ [[Writable]]: false, [[Enumerable]]: false, [[Configurable]]: false }`](https://tc39.es/proposal-iterator-helpers/#sec-iterator.prototype)で実装されることなっています。

この場合、次のようにStreamの`prototype.map`を上書きしようとする、`Writable`が`false`であるため、例外が発生してできません。

```js
// [Writable]]: falseでは書き込めない
ReadableStream.prototype.map = function(fn) { // 例外が発生する
  // ..
};
```

mongooseなどで、このような代入が存在したため、[`[[Writable]]: false`を`[[Writable]]: true`にする変更(revert)](https://github.com/nodejs/node/pull/41931)がNode.js 17.6.0に含まれています。(BREAKING CHANGEとなってしまったため)

- [fix Node.js 17.5 compatibility by benjamingr · Pull Request #11381 · Automattic/mongoose](https://github.com/Automattic/mongoose/pull/11381)
  - mongoose側での修正

----

[A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks](https://css-tricks.com/css-cascade-layers/)という記事では、Chrome/Edge 99+、Firefox 97+、Safari Technology Preview 133で実装されている CSS Cascade Layers について紹介されています。

CSSでは、UA、`!important`、[詳細度](https://developer.mozilla.org/ja/docs/Web/CSS/Specificity)などによってどのスタイルが当たるかの[Cascadingの仕様](https://drafts.csswg.org/css-cascade/#cascading)があります。
この仕様に[Cascade Layers](https://www.w3.org/TR/css-cascade-5/#layering)というものが追加され、各ブラウザでの実装が進んでいます。

この記事では、Cascade Layersの基本的な使い方、Important layers、Layerの優先度、sub layerについてなど書かれています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v6.32.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v6.32.0](https://github.com/pnpm/pnpm/releases/tag/v6.32.0 "Release v6.32.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 6.32.0リリース。
インストールスクリプトを実行できるパッケージを指定する`onlyBuiltDependencies`の追加、`overrides`フィールドが`pnpm add`に対して反映されるようになるなど


----

## Astro 0.23 Release Notes | Astro
[astro.build/blog/astro-023/](https://astro.build/blog/astro-023/ "Astro 0.23 Release Notes | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 0.23リリース。
HTML以外のビルドに対応、`set:html`と`set:text`ディレクティブの追加、`PUBLIC_` prefixの環境変数はフロントエンドへ公開するように変更。
また、次のバージョンではコンポーネント内のテキストを自動的にHTMLエスケープするよう変更予定。


----

## Node v17.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.6.0/](https://nodejs.org/en/blog/release/v17.6.0/ "Node v17.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.6.0リリース。
StreamにIterator helperの`map`などをメソッドを追加すると壊れるモジュールがあったため、仕様への準拠を一時的にrevert。
`--experimental-https-modules`のフラグ付きでHTTP URLをESMモジュールとしてロードできるように。
また`process.on("multipleResolves", ...)`がDeprecatedとなった。

- [stream: add map method to Readable: by benjamingr · Pull Request #40815 · nodejs/node](https://github.com/nodejs/node/pull/40815 "stream: add map method to Readable: by benjamingr · Pull Request #40815 · nodejs/node")

----

## Release v1.8.0 · reduxjs/redux-toolkit
[reduxjs/redux-toolkit/releases/tag/v1.8.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.8.0)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v1.8.0-rc.0リリース。
新しい非同期Middlewareとして`createListenerMiddleware`を追加、`configureStore`の型定義の改善など

- [New experimental &amp;quot;action listener middleware&amp;quot; package available · Discussion #1648 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/discussions/1648 "New experimental &amp;amp;quot;action listener middleware&amp;amp;quot; package available · Discussion #1648 · reduxjs/redux-toolkit")

----
<h1 class="site-genre">アーティクル</h1>

----

## What&#039;s New In DevTools (Chrome 99) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-99/](https://developer.chrome.com/blog/new-in-devtools-99/ "What&#039;s New In DevTools (Chrome 99) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Chrome 99の開発者ツールの変更点について。
WebSocketsのThrottilingに対応、Reporting APIのパネルを追加、ANSI escape codeを使ったコンソールログのスタイリングをサポートなど


----

## How to publish Deno modules to NPM
[deno.com/blog/dnt-oak](https://deno.com/blog/dnt-oak "How to publish Deno modules to NPM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

Denoで書かれたライブラリをNode.js向けにnpmへ公開する方法について。
HTTPフレームワークであるoakをdntを使ってNode.jsでも動かすように変換して公開した方法について

- [denoland/dnt: Deno to npm package build tool.](https://github.com/denoland/dnt/ "denoland/dnt: Deno to npm package build tool.")
- [feat: add experimental support for Node.js by kitsonk · Pull Request #479 · oakserver/oak](https://github.com/oakserver/oak/pull/479 "feat: add experimental support for Node.js by kitsonk · Pull Request #479 · oakserver/oak")

----

## A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks
[css-tricks.com/css-cascade-layers/](https://css-tricks.com/css-cascade-layers/ "A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Cascade Layersの解説記事。
Cascade Layersの基本的な使い方、Important layers、Layerの優先度、sub layerについてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## microsoft/TypeScript-Compiler-Notes: A repo containing notes about the TypeScript Compiler codebase
[github.com/microsoft/TypeScript-Compiler-Notes](https://github.com/microsoft/TypeScript-Compiler-Notes "microsoft/TypeScript-Compiler-Notes: A repo containing notes about the TypeScript Compiler codebase")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span></p>

TypeScriptのコンパイラーについてのメモをまとめたリポジトリ。
重要な変更のPRのまとめ、コンパイルプロセスの解説やContributeする方法ついてなど書かれている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## JoshuaKGoldberg/TypeStat: Converts JavaScript to TypeScript and TypeScript to better TypeScript.
[github.com/JoshuaKGoldberg/TypeStat](https://github.com/JoshuaKGoldberg/TypeStat "JoshuaKGoldberg/TypeStat: Converts JavaScript to TypeScript and TypeScript to better TypeScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのコードにTypeScriptの型をつけてTypeScriptのコードベースに変換するツール


----

## xataio/screenshot: A zero-dependency browser-native way to take screenshots powered by the native web MediaDevices API.
[github.com/xataio/screenshot](https://github.com/xataio/screenshot "xataio/screenshot: A zero-dependency browser-native way to take screenshots powered by the native web MediaDevices API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Image</span> <span class="jser-tag">browser</span></p>

`MediaDevices.getDisplayMedia`を使ったスクリーンショットライブラリ。
画面の表示そのものをキャプチャ画像として取得できる

- [Xata | New Open Source Library: Announcing @xata.io/screenshot](https://www.xata.io/blog/introducing-screenshot/ "Xata | New Open Source Library: Announcing @xata.io/screenshot")

----

## leafac/caxa: 📦 Package Node.js applications into executable binaries 📦
[github.com/leafac/caxa](https://github.com/leafac/caxa "leafac/caxa: 📦 Package Node.js applications into executable binaries 📦")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Node.jsアプリケーションを単一の実行バイナリにパッケージングするツール。
Node.jsとアプリを含む自己解凍型アーカイブとして扱うことで、`fs`などへのpatchをせずにパッケージングしている


----
<h1 class="site-genre">書籍関係</h1>

----

## vinodotdev/node-to-rust
[github.com/vinodotdev/node-to-rust/](https://github.com/vinodotdev/node-to-rust/ "vinodotdev/node-to-rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">book</span></p>

JavaScriptユーザ向けのRust入門書


----
