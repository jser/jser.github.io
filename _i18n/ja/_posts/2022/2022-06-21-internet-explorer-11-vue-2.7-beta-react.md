---
title: "2022-06-21のJS: Internet Explorer 11のサポート終了、Vue 2.7 Beta、社内のReactコンポーネントのメンテナンス"
author: "azu"
layout: post
date : 2022-06-21T03:02:39.168Z
category: JSer
tags:
- Tools
- bundler
- node.js
- monorepo
- React

---

JSer.info #597 - エンタープライズやWindows Serverなどの特定のOSを除いて、Internet Explorer 11のサポートが2022年6月15日で終了されました。

- [Internet Explorer 11 has retired and is officially out of support—what you need to know | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2022/06/15/internet-explorer-11-has-retired-and-is-officially-out-of-support-what-you-need-to-know/)

サポート終了となったOSでIEのアプリケーションを開くと、MSEdgeにリダイレクトされるようになっていきます。
また、MSEdgeのIEモード(下位互換モード)は、2029 年までサポートされる予定となっています。

- [ライフサイクルに関する FAQ - Internet Explorer および Microsoft Edge | Microsoft Docs](https://docs.microsoft.com/lifecycle/faq/internet-explorer-microsoft-edge)

----

Vue 2系の最終マイナーバージョンとなるVue 2.7のbeta版がリリースされました。

- [Vue 2.7 is Now in Beta! | The Vue Point](https://blog.vuejs.org/posts/vue-2-7-beta.html)

Vue 3からのバックポートとして`defineComponent()`、`h()`、`useSlot()`、`useAttrs()`、`useCssModules()`のサポートが追加されています。
またESMビルドにはnamed exportとして提供されることについてや、Vue 3との動作の違いについてなども書かれています。

Vue 2.7の正式リリースは、6月末を予定していて、リリースされてから18ヶ月後の2023年末にサポートが終了される予定となっています。

----

[Notes on maintaining an internal React component library | Gabe's blog](https://www.gabe.pizza/notes-on-component-libraries/)という記事では、社内でのReactコンポーネントライブラリを作成する場合について書かれています。

どのようにコンポーネントを設計すれば、正しく使われるコンポーネントが作れるのかについて書かれています。
間違った使われ方をしないような設計やメジャーアップデート時にcodemodでのマイグレーション、ビジュアルリグレッションテストなどについて書かれています。

また、PublicなStorybookを検索できるコンポーネント百科事典がStorybookによって公開されています。
これもあわせてみてみると良いかもしれません。

- [Component Encyclopedia | Storybook](https://storybook.js.org/showcase)
- [Component Encyclopedia](https://storybook.js.org/blog/component-encyclopedia/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v0.14.44 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.14.44](https://github.com/evanw/esbuild/releases/tag/v0.14.44 "Release v0.14.44 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild 0.14.44リリース。
`copy` loaderのサポート、package.jsonで定義したself-referencesのサポート。
`tsconfig.json`の`alwaysStrict`がある場合に`"use strcit"`を追加するようになるなど


----

## Deno 1.23 Release Notes
[deno.com/blog/v1.23](https://deno.com/blog/v1.23 "Deno 1.23 Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.23.0リリース。
`deno run`などでデフォルトでタイプチェックをしないように変更、`Deno.sleepSync`を削除、`deno task`が`--cwd`フラグをサポート。
`deno task`がcat/xargs/redirectをサポート、CompressionStreamとDecompressionStreamが`"deflate-raw"`をサポート。
TypeScript 4.7をサポートなど

- [Release v1.23.0 · denoland/deno](https://github.com/denoland/deno/releases/tag/v1.23.0 "Release v1.23.0 · denoland/deno")

----

## Release v2.0.0 · redwoodjs/redwood
[github.com/redwoodjs/redwood/releases/tag/v2.0.0](https://github.com/redwoodjs/redwood/releases/tag/v2.0.0 "Release v2.0.0 · redwoodjs/redwood")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redwood 2.0.0リリース。
`import/order`のLintルールの変更、独自のインフラにデプロイする場合の設定の変更、`useRequireAuth`の挙動を変更など


----

## Release 2.0.0-beta.4 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-beta.4](https://github.com/vercel/swr/releases/tag/2.0.0-beta.4 "Release 2.0.0-beta.4 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-beta.4リリース。
`preload`関数の追加、`SWRConfig`で設定をoverrideできるようになるなど


----

## Release Inferno v8.0.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v8.0.0](https://github.com/infernojs/inferno/releases/tag/v8.0.0 "Release Inferno v8.0.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v8.0.0リリース。
`componentDidAppear`と`componentWillDisappear`の追加、`href=javascript:`に警告を表示するように。
破棄的な変更としてIEのサポート終了、`inferno-component`パッケージの削除、`inferno-devtools`パッケージの削除など


----

## Release Version 20.0.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/20.0.0](https://github.com/jsdom/jsdom/releases/tag/20.0.0 "Release Version 20.0.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 20.0.0リリース。
Node.js 14未満のサポート終了、`crypto.getRandomValues()`の実装、`addEventListener`が`signal`オプションのサポートなど


----

## Release v0.14.46 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.14.46](https://github.com/evanw/esbuild/releases/tag/v0.14.46 "Release v0.14.46 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.14.46リリース。
構文ごとに機能のサポートを無効化するかを指定できるように、TypeScript 4.7のサポート、`--define`がoptional chianingをサポートなど


----

## Release v1.0.0 · sindresorhus/ow
[github.com/sindresorhus/ow/releases/tag/v1.0.0](https://github.com/sindresorhus/ow/releases/tag/v1.0.0 "Release v1.0.0 · sindresorhus/ow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

関数でスキーマを定義してバリデーションするow 1.0.0リリース。
Node.js 12のサポート終了、TypeScript 4.7が必須に、Pure ESM化など。


----

## Internet Explorer 11 has retired and is officially out of support—what you need to know | Windows Experience Blog
[blogs.windows.com/windowsexperience/2022/06/15/internet-explorer-11-has-retired-and-is-officially-out-of-support-what-you-need-to-know/](https://blogs.windows.com/windowsexperience/2022/06/15/internet-explorer-11-has-retired-and-is-officially-out-of-support-what-you-need-to-know/ "Internet Explorer 11 has retired and is officially out of support—what you need to know | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">news</span></p>

Internet Explorerが2022年6月15日をもってサポートを終了となった。
今後はIEを開くとMSEdgeへリダイレクトされるようになる。


----

## Vue 2.7 is Now in Beta! | The Vue Point
[blog.vuejs.org/posts/vue-2-7-beta.html](https://blog.vuejs.org/posts/vue-2-7-beta.html "Vue 2.7 is Now in Beta! | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 2.7 Betaリリース。
Vue 3からのバックポートとして`defineComponent()`、`h()`、`useSlot()`、`useAttrs()`、`useCssModules()`のサポート。
またESMビルドにはnamed exportとして提供されることについてや、Vue 3との動作の違いについてなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Notes on maintaining an internal React component library | Gabe&#039;s blog
[www.gabe.pizza/notes-on-component-libraries/](https://www.gabe.pizza/notes-on-component-libraries/ "Notes on maintaining an internal React component library | Gabe&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

社内でReactコンポーネントライブラリを作るときのプラクティスについての記事。
間違った状態を受け入れる型を避ける、子となるコンポーネント自体にmarginを持たせない、コンポーネントのwidthは幅全体を占めるようにする。
コンポーネントのPropsとして`className`や`style`は公開しないようにする、ElementのPropsを継承しないようにする。
相互依存するコンポーネントにはReact Contextを使う、一緒に利用するコンポーネントはオブジェクトとしてまとめてexportする。
メジャーアップデートと共にcodemodを提供する、開発者がどのように使ってるかを分析、ビジュアルリグレッションテストを設定するなど


----

## Using web streams on Node.js
[2ality.com/2022/06/web-streams-nodejs.html](https://2ality.com/2022/06/web-streams-nodejs.html "Using web streams on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">stream</span> <span class="jser-tag">article</span></p>

Node.jsでのWeb Streamについての記事。
基本的な使い方、Asynchronous Iterationとの組み合わせ、Streamへの変換、ReadableStream/WritableStream/TranformStream。
Streamのbackpressure、バイナリを扱うByte Stream、`node:stream`が公開するヘルパー関数についてなど


----

## Lerna 5.1 — New website, new guides, new Lerna example repo, distributed caching support and speed! | by Juri Strumpflohner | Jun, 2022 | Nrwl
[blog.nrwl.io/lerna-5-1-new-website-new-guides-new-lerna-example-repo-distributed-caching-support-and-speed-64d66410bec7](https://blog.nrwl.io/lerna-5-1-new-website-new-guides-new-lerna-example-repo-distributed-caching-support-and-speed-64d66410bec7 "Lerna 5.1 — New website, new guides, new Lerna example repo, distributed caching support and speed! | by Juri Strumpflohner | Jun, 2022 | Nrwl")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">article</span></p>

Lerna 5.1について。
Nxコマンドと連携できる仕組みの追加、ドキュメントサイトの刷新など。
また今後のロードマップについて

- [Release v5.1.0 · lerna/lerna](https://github.com/lerna/lerna/releases/tag/v5.1.0 "Release v5.1.0 · lerna/lerna")
- [Running Tasks | Lerna](https://lerna.js.org/docs/core-concepts/running-tasks "Running Tasks | Lerna")
- [Lerna 2022 Plans · Discussion #3140 · lerna/lerna](https://github.com/lerna/lerna/discussions/3140 "Lerna 2022 Plans · Discussion #3140 · lerna/lerna")

----

## AbortController is your friend
[whistlr.info/2022/abortcontroller-is-your-friend/](https://whistlr.info/2022/abortcontroller-is-your-friend/ "AbortController is your friend")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

AbortControllerについての記事。
AbortControllerとAbortSignalの使い方について。
`addEventListner`との組み合わせ、複雑な処理の停止、React Hooksでの利用、AbortSignalのヘルパー処理についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf Budapest 2022 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshGuMZrOZzEo8QLBjjpbtBGm#budapest2022](https://www.youtube.com/playlist?list=PL37ZVnwpeshGuMZrOZzEo8QLBjjpbtBGm#budapest2022 "JSConf Budapest 2022 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JSConf Budapest 2022の動画一覧

- [JSConf Budapest 2022](https://jsconfbp.com/ "JSConf Budapest 2022")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## A build system for the JavaScript ecosystem | moon
[moonrepo.dev/](https://moonrepo.dev/ "A build system for the JavaScript ecosystem | moon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span></p>

Rustで書かれたJavaScriptなmonorepo向けのプロジェクト管理ツール。
パッケージの依存グラフに基づいたタスクの実行、
キャッシュ、リモートキャッシュ、インクリメンタルビルドなどの機能を提供する


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## taozhi8833998/node-sql-parser: Parse simple SQL statements into an abstract syntax tree (AST) with the visited tableList and convert it back to SQL
[github.com/taozhi8833998/node-sql-parser](https://github.com/taozhi8833998/node-sql-parser "taozhi8833998/node-sql-parser: Parse simple SQL statements into an abstract syntax tree (AST) with the visited tableList and convert it back to SQL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SQL</span> <span class="jser-tag">library</span></p>

SQLパーサ/ジェネレータライブラリ。
BigQuery、DB2、Hive、MariaDB、MySQL、PostgresQL、SQLiteなどのSQLに対応している


----

## coder-mike/microvium: A compact, embeddable scripting engine for applications and microcontrollers for executing programs written in a subset of the JavaScript language.
[github.com/coder-mike/microvium](https://github.com/coder-mike/microvium "coder-mike/microvium: A compact, embeddable scripting engine for applications and microcontrollers for executing programs written in a subset of the JavaScript language.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

組み込み向けのJavaScriptエンジン。
64kBのメモリ制限やJavaScriptの機能も制限されているが、小さなメモリフットプリントで動かすのを目的としている


----
