---
title: "2022-08-25のJS:  Oven: the company behind Bun、CSS `:has()`"
author: "azu"
layout: post
date : 2022-08-25T06:33:06.679Z
category: JSer
tags:
- node.js
- TypeScript
- redux
- cloudflare
- grpc

---

JSer.info #606 - [Bun](https://bun.sh/)を開発する[@jarredsumner](https://twitter.com/jarredsumner)を中心にOvenという会社が設立され、資金調達が行われました。

- [Oven: the company behind Bun](https://oven.sh/)

Ovenの今後のロードマップとして、Bunを動かすエッジサーバのホスティング、Node.js向けに書かれたフレームワークのサポートの改善、半年以内にStable版を出すことを目標にしているそうです。

----

[Using :has() as a CSS Parent Selector and much more | WebKit](https://webkit.org/blog/13096/css-has-pseudo-class/)という記事では、CSSの`:has()`擬似クラスについて紹介されています。

[:has()](https://developer.mozilla.org/ja/docs/Web/CSS/:has)はいわゆる親セレクターとしての利用方法がよく知られていますが、それ以外にもGridの利用、`>`との違い、sibling combinators(`~`と`+`)との組み合わせなどについても紹介されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.9.0-alpha.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v1.9.0-alpha.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.9.0-alpha.0 "Release v1.9.0-alpha.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v1.9.0-alpha.0リリース。
`merge` mutationの追加、`createReducer`にオブジェクトを渡すスタイルをDeprecatedへ変更、`createAsyncThunk.withTypes()`の追加など


----

## Release v2.7.0 · cloudflare/miniflare
[github.com/cloudflare/miniflare/releases/tag/v2.7.0](https://github.com/cloudflare/miniflare/releases/tag/v2.7.0 "Release v2.7.0 · cloudflare/miniflare")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

miniflare 2.7.0リリース。
`fetch`リクエストをモックするAPIの追加、Durable ObjectをflushするAPIの追加など


----

## Oven: the company behind Bun
[oven.sh/](https://oven.sh/ "Oven: the company behind Bun")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">news</span> <span class="jser-tag">company</span></p>

BunはOvenという会社を立ち上げ、資金調達をした。
今後のロードマップとして、Bunを動かすエッジサーバのホスティング、Node.js向けに書かれたフレームワークのサポートの改善、半年以内にStable版を出すことを目標にしている。


----

## Node v18.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v18.8.0/](https://nodejs.org/en/blog/release/v18.8.0/ "Node v18.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 18.8.0リリース。
ユーザーランドでのスナップショットを作成/復元できる`--build-snapshot`と`--snapshot-blob`の追加。現時点ではCJS/ESMはサポートしてないため、一つのファイルのみを扱える。


----

## Release Notes for Safari Technology Preview 152 | WebKit
[webkit.org/blog/13137/release-notes-for-safari-technology-preview-152/](https://webkit.org/blog/13137/release-notes-for-safari-technology-preview-152/ "Release Notes for Safari Technology Preview 152 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 152リリース。
ECMAScript Proposal Stage 3のSymbols as WeakMap keysの実装、Compression Streams APIの実装など


----

## Release v1.25.0 · denoland/deno
[github.com/denoland/deno/releases/tag/v1.25.0](https://github.com/denoland/deno/releases/tag/v1.25.0 "Release v1.25.0 · denoland/deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.25.0リリース。
`deno init`コマンドの追加、Unstableな機能として`npm:` prefixでnpmパッケージをロードできるようになるなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Buf | Connect-Web: It&#039;s time for Protobuf and gRPC to be your first choice in the browser
[buf.build/blog/connect-web-protobuf-grpc-in-the-browser](https://buf.build/blog/connect-web-protobuf-grpc-in-the-browser "Buf | Connect-Web: It&#039;s time for Protobuf and gRPC to be your first choice in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">grpc</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

gRPCのクライアントライブラリであるconnect-webについて。
Protocol BufferからTypeScriptのクライアントコードを生成して利用できる。

- [bufbuild/connect-web: Simple, reliable, interoperable. A better gRPC-Web.](https://github.com/bufbuild/connect-web "bufbuild/connect-web: Simple, reliable, interoperable. A better gRPC-Web.")

----

## Working with file system paths on Node.js
[2ality.com/2022/07/nodejs-path.html](https://2ality.com/2022/07/nodejs-path.html "Working with file system paths on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">URL</span> <span class="jser-tag">article</span></p>

Node.jsの`path`モジュール、minimatchでのglobについての解説。
また、URLとファイルパスの変換について


----

## Running WordPress in the Browser
[wasmlabs.dev/articles/wordpress-in-the-browser/](https://wasmlabs.dev/articles/wordpress-in-the-browser/ "Running WordPress in the Browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">wordpress</span> <span class="jser-tag">SQLite</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

WebAssemblyを使ってWordPressをブラウザで動かす話。
PHPとSQLiteをそれぞれEmscriptenを使ってWasmへとコンパイルし、WordPressを動かす。
Service Workerを使ったループバックの実装についてなど


----

## Typescipt is terrible for library developers: We spend a disproportionate amount of time on types
[erock.prose.sh/typescript-terrible-for-library-developers](https://erock.prose.sh/typescript-terrible-for-library-developers "Typescipt is terrible for library developers: We spend a disproportionate amount of time on types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

ライブラリにおけるTypeScriptの型の複雑さについて。
デバッグ、複雑さ、テスト、メンテナンスの難しさについて


----

## Using :has() as a CSS Parent Selector and much more | WebKit
[webkit.org/blog/13096/css-has-pseudo-class/](https://webkit.org/blog/13096/css-has-pseudo-class/ "Using :has() as a CSS Parent Selector and much more | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSの`:has()`擬似クラスについて。
親セレクターとしての利用、Gridの利用、`>`との違い、sibling combinators(`~`と`+`)との組み合わせなどについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Building a Typechecker from scratch | Dmitry Soshnikov | Education
[www.dmitrysoshnikov.education/p/typechecker](https://www.dmitrysoshnikov.education/p/typechecker "Building a Typechecker from scratch | Dmitry Soshnikov | Education")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">video</span> <span class="jser-tag">tutorial</span></p>

JavaScriptで型チェッカーを一から作成していく講座


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## react-pdf-viewer/react-pdf-viewer: A React component to view a PDF document
[github.com/react-pdf-viewer/react-pdf-viewer](https://github.com/react-pdf-viewer/react-pdf-viewer "react-pdf-viewer/react-pdf-viewer: A React component to view a PDF document")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">PDF</span> <span class="jser-tag">library</span></p>

pdf.jsを使ったPDFビューアReactコンポーネント


----

## rayepps/radash: Functional utility library - modern, simple, typed, powerful
[github.com/rayepps/radash](https://github.com/rayepps/radash "rayepps/radash: Functional utility library - modern, simple, typed, powerful")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

lodashのようなユーティリティコレクションライブラリ。
それぞれの関数が独立していて、シンプルなコードとして読めるように書かれている

- [Lodash is dead. Long live Radash. | by Ray Epps | Vanguards of Code | Aug, 2022 | Medium](https://medium.com/vanguards-of-code/lodash-is-dead-long-live-radash-d9d52abf428b "Lodash is dead. Long live Radash. | by Ray Epps | Vanguards of Code | Aug, 2022 | Medium")

----
