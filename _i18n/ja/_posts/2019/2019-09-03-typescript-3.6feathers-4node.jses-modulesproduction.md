---
title: "2019-09-03のJS: TypeScript 3.6、Feathers 4(Node.jsフレームワーク)、ES ModulesをProductionで使う方法"
author: "azu"
layout: post
date : 2019-09-03T02:36:40.240Z
category: JSer
tags:
- TypeScript
- Feathers
- ESModule

---

JSer.info #451 - TypeScript 3.6が正式にリリースされました。

- [Announcing TypeScript 3.6 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6/)

基本的にはβ、RCからの大きな変更はありませんが、Generatorsの型チェック改善、`--downlevelIteration`フラグでArray Spreadの仕様に合わせた変換の改善、Promiseの型エラーの改善ながお行われています。
破壊的な変更としては`lib.dom.d.ts`の`globalThis`に関する変更、`GlobalFetch`の削除、`experimental-webgl`が削除され`webgl`と`webgl2`を使うように変更なども行われています。

また、[TypeScript playground](https://www.typescriptlang.org/play/)が <https://typescript-play.js.org/> ベースのものに刷新され、
TypeScriptのオプションなど細かい指定ができるようになっています。

- [agentcooper/typescript-play: Better TypeScript playground](https://github.com/agentcooper/typescript-play)

----

リアルタイムアプリやREST API向けのNode.jsフレームワークである[Feathers](https://feathersjs.com/) 4がリリースされています。

- [Introducing Feathers 4: A framework for real-time apps and REST APIs](https://blog.feathersjs.com/introducing-feathers-4-a-framework-for-real-time-apps-and-rest-apis-afff3819055b)

コアライブラリがTypeScriptで書き直され型定義ファイルを同梱するようになっています。
また認証の仕組み([Authentication](https://docs.feathersjs.com/guides/basics/authentication.html#authentication))を作り直したことで、互換性がない変更も含まれています。具体的には次のIssueにまとめられています。

- [Authentication next · Issue #1045 · feathersjs/feathers](https://github.com/feathersjs/feathers/issues/1045#issuecomment-456701800)

また、認証周りの仕組みの変更に伴うマイグレーションガイドも公開されています。

- [Migrating | FeathersJS](https://docs.feathersjs.com/guides/migrating.html)

----

[Using Native JavaScript Modules in Production Today — Philip Walton](https://philipwalton.com/articles/using-native-javascript-modules-in-production-today/)という記事では、ブラウザでES Modulesそのものを読み込んで使うための方法について紹介されています。

RollupをつかってnpmモジュールごとにES moduleのchunkを作成し、`<script module>`でのロード、`modulepreload`でのpreloadについて。
また、Dynamic Importでの動的ロードと[polyfill](https://github.com/GoogleChromeLabs/dynamic-import-polyfill)、ES moduleをサポートしてない環境への`<script nonmodule>`での読み込みについてなどについて書かれています。

デモアプリも公開されているので、興味がある人は読んでみるとよさそうです。

- [Real Modules with Rollup Demo](https://rollup-native-modules-boilerplate.glitch.me/)
- [philipwalton/rollup-native-modules-boilerplate: A demo app showcasing the use of real JavaScript modules in production—complete with cross-browser fallbacks for legacy browsers.](https://github.com/philipwalton/rollup-native-modules-boilerplate)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 3.6 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-6/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6/ "Announcing TypeScript 3.6 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.6リリース。
 Generatorsの型チェック改善、`--downlevelIteration`フラグでArray Spreadの仕様に合わせた変換の改善、Promiseの型エラーの改善。 `--target es2015`でUnicodeの変数名をサポート、Ambient ClassesとFunctionがマージできるようになるなど。
また、Playgroundが https://typescript-play.js.org ベースに更新されるなど


----

## Dojo
[dojo.io/blog/version-6-dojo](https://dojo.io/blog/version-6-dojo "Dojo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Dojo 6リリース。


----

## ESLint v6.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2019/08/eslint-v6.3.0-released](https://eslint.org/blog/2019/08/eslint-v6.3.0-released "ESLint v6.3.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v6.3.0リリース。
`eslint --init`でTypeScriptの設定のサポート、設定ファイルに`reportUnusedDisableDirectives`を指定できるように


----

## Introducing Feathers 4: A framework for real-time apps and REST APIs
[blog.feathersjs.com/introducing-feathers-4-a-framework-for-real-time-apps-and-rest-apis-afff3819055b](https://blog.feathersjs.com/introducing-feathers-4-a-framework-for-real-time-apps-and-rest-apis-afff3819055b "Introducing Feathers 4: A framework for real-time apps and REST APIs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Node.jsフレームワークのFeathers 4リリース。
コアライブラリがTypeScriptで書き直され型定義ファイルを同梱するように、認証の仕組みを作り直しプラグインで拡張できるようになるなど。
認証周りの仕組みの変更に伴うマイグレーションガイドも公開されている。

- [Feathers | A framework for real-time applications and REST APIs](https://feathersjs.com/ "Feathers | A framework for real-time applications and REST APIs")
- [Authentication | FeathersJS](https://docs.feathersjs.com/guides/basics/authentication.html#registering-a-user "Authentication | FeathersJS")
- [Migrating | FeathersJS](https://docs.feathersjs.com/guides/migrating.html "Migrating | FeathersJS")
- [Authentication next · Issue #1045 · feathersjs/feathers](https://github.com/feathersjs/feathers/issues/1045 "Authentication next · Issue #1045 · feathersjs/feathers")

----

## Release 6.0.0 · systemjs/systemjs
[github.com/systemjs/systemjs/releases/tag/6.0.0](https://github.com/systemjs/systemjs/releases/tag/6.0.0 "Release 6.0.0 · systemjs/systemjs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">module</span> <span class="jser-tag">ReleaseNote</span></p>

systemjs 6.0.0 リリース。
`System.onload`のhookを追加、`systemjs-importmap`でのImportMap定義の合成をサポート、`System.resolve`が同期処理に変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Using Native JavaScript Modules in Production Today — Philip Walton
[philipwalton.com/articles/using-native-javascript-modules-in-production-today/](https://philipwalton.com/articles/using-native-javascript-modules-in-production-today/ "Using Native JavaScript Modules in Production Today — Philip Walton")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

ES moduleをそのまま使うためのテクニックについての話。
RollupをつかってnpmモジュールごとにES moduleのchunkを作成し、`<script module>`でのロード、`modulepreload`でのpreload。
Dynamic Importでの動的ロードとpolyfill、ES moduleをサポートしてない環境への`<script nonmodule>`での読み込みについてなど。


----

## Optional chaining · V8
[v8.dev/features/optional-chaining](https://v8.dev/features/optional-chaining "Optional chaining · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

ECMAScript Proposal Stage 3であるOptional Chain(`?.`)とnullish coalescing `??` operatorについて。
`lodash.get`をどのように置き換えられるかの例など


----

## MarkdownやAsciidoc中に書いたJavaScriptのサンプルコードをdoctestするツールを書いた | Web Scratch
[efcl.info/2019/09/02/power-doctest-markdown-asciidoc/](https://efcl.info/2019/09/02/power-doctest-markdown-asciidoc/ "MarkdownやAsciidoc中に書いたJavaScriptのサンプルコードをdoctestするツールを書いた | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span> <span class="jser-tag">article</span> <span class="jser-tag">node.js</span></p>

MarkdownやAsciidocのコードブロック内のJavaScriptコードをdoctestするツールやライブラリについて。
コメントで式の期待する評価結果を書くと、assertに変換してテストできる。

- [azu/power-doctest: JavaScript Doctest for JavaScript, Markdown and Asciidoc.](https://github.com/azu/power-doctest "azu/power-doctest: JavaScript Doctest for JavaScript, Markdown and Asciidoc.")

----

## Creating an Object Validator in JavaScript the Test-Driven Development Way | Nick Scialli
[nick.scialli.me/creating-an-object-validator-the-tdd-way/](https://nick.scialli.me/creating-an-object-validator-the-tdd-way/ "Creating an Object Validator in JavaScript the Test-Driven Development Way | Nick Scialli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

オブジェクトのvalidatorをTDDで実装していく話。
テスト、実装、リファクタリングの流れについて


----

## The Baseline Interpreter: a faster JS interpreter in Firefox 70 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/08/the-baseline-interpreter-a-faster-js-interpreter-in-firefox-70/](https://hacks.mozilla.org/2019/08/the-baseline-interpreter-a-faster-js-interpreter-in-firefox-70/ "The Baseline Interpreter: a faster JS interpreter in Firefox 70 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">JavaScript</span></p>

Firefox 70に入るJavaScriptのBaseline Interpreterについて。
既存のベースラインJITのコードと上手く共有し、jitScriptと呼ばれる新しくバイトコードインタプリタを追加することでパフォーマンスの改善につながったという話


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 現代フロントエンドに欠かせないwebpackとBabelを理解しよう - Speaker Deck
[speakerdeck.com/mukai21/xian-dai-hurontoendoniqian-kasenaiwebpacktobabelwoli-jie-siyou](https://speakerdeck.com/mukai21/xian-dai-hurontoendoniqian-kasenaiwebpacktobabelwoli-jie-siyou "現代フロントエンドに欠かせないwebpackとBabelを理解しよう - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">webpack</span> <span class="jser-tag">slide</span></p>

Babelやwebpackが何をやっているのかについてのスライド。
Babelがどのようにコードを変換しているのかやwebpackがどのようにモジュールを扱っているのかについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Using with puppeteer · Jest
[jestjs.io/docs/puppeteer](https://jestjs.io/docs/puppeteer "Using with puppeteer · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

Jest内でpuppeteerを使う方法についてのドキュメント


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## finom/check-imports: Check imports in JS files and update package.json dependencies
[github.com/finom/check-imports](https://github.com/finom/check-imports "finom/check-imports: Check imports in JS files and update package.json dependencies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

コードに書かれている`import`文や`require`関数などを分析して、`package.json`の依存関係を更新するツール


----

## antoinechalifour/memento: Memento is a development-only tool that caches HTTP calls once they have been executed.
[github.com/antoinechalifour/memento](https://github.com/antoinechalifour/memento "antoinechalifour/memento: Memento is a development-only tool that caches HTTP calls once they have been executed.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

開発時にAPIへのリクエストをキャッシュして、モックサーバとして利用できるようにするツール。


----

## CONNECT-platform/connective: agent-based reactive programming library for typescript
[github.com/connect-platform/connective](https://github.com/connect-platform/connective "CONNECT-platform/connective: agent-based reactive programming library for typescript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

RxJSを使って作られたデータコントールフローライブラリ


----
