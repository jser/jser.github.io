---
title: "2022-11-29のJS: ESMeta、Wasmer 3.0、tRPC v10"
author: "azu"
layout: post
date : 2022-11-29T14:34:25.485Z
category: JSer
tags:
- TypeScript
- Tools
- node.js
- WebAssembly
- Rust

---

JSer.info #620 - [ESMeta](https://github.com/es-meta/esmeta)というECMAScript Specification Metalanguageツールが公開されています。

- [es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage](https://github.com/es-meta/esmeta)

主に[ECMAScriptの仕様](https://tc39.es/ecma262/)を扱う人向けのツールです。
ECMAScriptの言語/仕様書のパーサとインタープリタを実装することで、仕様書から自動的にECMAScriptの処理系を生成するメタ的なツールです。
仕様書のアルゴリズムをステップ実行したり、デバッガーでBreak Pointを貼ったり、仕様書における内部状態を可視化できるデバッグ機能が実装されています。

----

WebAssemblyの処理系であるWasmer 3.0がリリースされました。

- [Announcing Wasmer 3.0](https://wasmer.io/posts/announcing-wasmer-3.0)
- [wasmer/migration_to_3.0.0.md at master · wasmerio/wasmer · GitHub](https://github.com/wasmerio/wasmer/blob/master/docs/migration_to_3.0.0.md)

Wasmer 3.0では、WAPMパッケージを実行できる`wasmer run`コマンドの追加、`MemoryView`の追加。
Zigのクロスコンパイル機能を使ってWindow/Linux/macOSの実行ファイルを作成できるようになっています。

----

TypeScriptを使ったAPIレイヤーを定義する tRPC v10 がリリースされました。

- [Announcing tRPC v10 | tRPC](https://trpc.io/blog/announcing-trpc-10)

主に型の利用方法を改善する目的でRouterの定義方法、`inferRouterInputs`と`inferRouterOutputs`の型定義を追加、Middlewareのシグネチャの変更などが行われています。

マイグレーションガイドとマイグレーションツールも併せて公開されています。

- [Migrate from v9 to v10 | tRPC](https://trpc.io/docs/migrate-from-v9-to-v10)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Prettier 2.8: improve --cache CLI option and TypeScript 4.9 satisfies operator! · Prettier
[prettier.io/blog/2022/11/23/2.8.0.html](https://prettier.io/blog/2022/11/23/2.8.0.html "Prettier 2.8: improve --cache CLI option and TypeScript 4.9 satisfies operator! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.8リリース。
TypeScript 4.9 `satisfies` operatorのサポート、`--cache-location`オプションの追加など


----

## es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage
[github.com/es-meta/esmeta](https://github.com/es-meta/esmeta "es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ECMAScript仕様書のメタ言語ツール。
ECMAScriptの言語/仕様書のパーサとインタープリタを実装したメタツール。
仕様書のアルゴリズムをステップ実行したり、デバッガーでBreak Pointを貼ったり、仕様書における内部状態を可視化できる。


----

## Announcing Wasmer 3.0
[wasmer.io/posts/announcing-wasmer-3.0](https://wasmer.io/posts/announcing-wasmer-3.0 "Announcing Wasmer 3.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span></p>

Wasmer 3.0リリース。
WAPMパッケージを実行できる`wasmer run`コマンドの追加、`MemoryView`の追加。
Zigのクロスコンパイル機能を使ってWindow/Linux/macOSの実行ファイルを作成できるように

- [wasmer/migration\_to\_3.0.0.md at master · wasmerio/wasmer · GitHub](https://github.com/wasmerio/wasmer/blob/master/docs/migration_to_3.0.0.md "wasmer/migration\_to\_3.0.0.md at master · wasmerio/wasmer · GitHub")

----

## Announcing tRPC v10 | tRPC
[trpc.io/blog/announcing-trpc-10](https://trpc.io/blog/announcing-trpc-10 "Announcing tRPC v10 | tRPC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

tRPC v10リリース。
Routerの定義方法、`inferRouterInputs`と`inferRouterOutputs`の型定義を追加、Middlewareのシグネチャの変更など

- [Migrate from v9 to v10 | tRPC](https://trpc.io/docs/migrate-from-v9-to-v10 "Migrate from v9 to v10 | tRPC")

----

## Node.js 18.x runtime now available in AWS Lambda | AWS Compute Blog
[aws.amazon.com/jp/blogs/compute/node-js-18-x-runtime-now-available-in-aws-lambda/](https://aws.amazon.com/jp/blogs/compute/node-js-18-x-runtime-now-available-in-aws-lambda/ "Node.js 18.x runtime now available in AWS Lambda | AWS Compute Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">Lambda</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

AWS LambdaでNode.js 18をサポート


----
<h1 class="site-genre">アーティクル</h1>

----

## Wasmはなぜセキュアなのか？
[zenn.dev/0kate/articles/83e48c177ff709](https://zenn.dev/0kate/articles/83e48c177ff709 "Wasmはなぜセキュアなのか？")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

Wasmerの実装を読みながら、WebAssemblyのセキュリティ機能がどのように実現されているについて


----

## Prerender2 という機能について | blog.bokken.io
[blog.bokken.io/articles/2022-11-24/about-prerender2.html](https://blog.bokken.io/articles/2022-11-24/about-prerender2.html "Prerender2 という機能について | blog.bokken.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chromeで実装中のPrerender2について。
Speculation Rulesでプリレンダリングする対象を指定する新しい仕組みについて


----

## デザインシステム開発優先度の「難しさ」と「対策」｜hikaru-takase /Loglass｜note
[note.com/99997373/n/n7dcb9092a90b](https://note.com/99997373/n/n7dcb9092a90b "デザインシステム開発優先度の「難しさ」と「対策」｜hikaru-takase /Loglass｜note")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Design</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

マルチプロダクト化していく中で複数のプロダクトから参照できるデザインが必要となり、それを解決するためにデザインシステムをどのように進めていくかについて。
デザイントークンの分離、コンポーネントの集中管理、小さく作り始めて広げていくなど


----

## TypeScript and native ESM on Node.js
[2ality.com/2021/06/typescript-esm-nodejs.html](https://2ality.com/2021/06/typescript-esm-nodejs.html "TypeScript and native ESM on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.jsでのESMと`exports`フィールドについての解説


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf JP 2022 公開資料・Twitterリンクまとめ
[zenn.dev/yumemi\_inc/articles/2022-11-27-jsconf-jp-2022](https://zenn.dev/yumemi_inc/articles/2022-11-27-jsconf-jp-2022 "JSConf JP 2022 公開資料・Twitterリンクまとめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

JSConf JP 2022の動画とスライドのまとめ

- [JSConf JP](https://jsconf.jp/2022/ "JSConf JP")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## 1Password/typeshare: Typeshare is the ultimate tool for synchronizing your type definitions between Rust and other languages for seamless FFI.
[github.com/1Password/typeshare](https://github.com/1Password/typeshare "1Password/typeshare: Typeshare is the ultimate tool for synchronizing your type definitions between Rust and other languages for seamless FFI.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">kotlin</span> <span class="jser-tag">swift</span> <span class="jser-tag">golang</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

アノテーションしたRustのコードからTypeScript/Swift/Kotlinの型定義を生成できるツール

----


## hyperstackjs · Hyperstack is a modern full-stack Node.js web framework for the pragmatic programmer
[hyperstackjs.io/](https://hyperstackjs.io/ "hyperstackjs · Hyperstack is a modern full-stack Node.js web framework for the pragmatic programmer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

Node.jsのウェブアプリケーションフレームワーク

----
<h1 class="site-genre">書籍関係</h1>

----

## A Skeptic’s Guide to Functional Programming with JavaScript
[jrsinclair.com/skeptics-guide](https://jrsinclair.com/skeptics-guide "A Skeptic’s Guide to Functional Programming with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">functional</span> <span class="jser-tag">book</span></p>

JavaScriptでの関数型プログラミングについての書籍


----
