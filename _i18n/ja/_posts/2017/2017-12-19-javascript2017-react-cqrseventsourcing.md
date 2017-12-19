---
title: "2017-12-19のJS: JavaScript開発者アンケート2017、Reactのインフラ、CQRS/EventSourcing"
author: "azu"
layout: post
date : 2017-12-19T01:21:14.517Z
category: JSer
tags:
- JavaScript
- react
- cqrs
- EventSourcing

---

JSer.info #362 - [The State of JavaScript 2017: Introduction](https://stateofjs.com/2017/introduction/ "The State of JavaScript 2017: Introduction")にてJavaScriptを使う開発者向けアンケートの結果が公開されています。

JavaScriptのフロントエンドからバックエンド、ツール、言語、ライブラリ、CSSなど幅広く扱った内容になっています。
またそれらの結果と給料や経験年数などを組み合わせた結果を見れます。

たとえば、[#StateOfJS 2017 Results: Front-end Frameworks](http://stateofjs.com/2017/front-end/results/)ではフロントエンドのフレームワークとして何を使っているかという質問の結果が掲載されています。
結果としてはReact、何も使ってない、Angularとなっていて、それらのフレームワークをまた使いたいかどうかや組み合わせて使っているのかといった内容になっています。

去年の結果も<http://2016.stateofjs.com/>で見れるため、比べて見ると思い白いかもしれません。

----

[Behind the Scenes: Improving the Repository Infrastructure - React Blog](https://reactjs.org/blog/2017/12/15/improving-the-repository-infrastructure.html#using-public-api-in-tests "Behind the Scenes: Improving the Repository Infrastructure - React Blog")という記事では
[facebook/react](https://github.com/facebook/react/ "facebook/react")リポジトリの開発インフラ整備について書かれています。

かなり幅広く(ライブラリにおける)プロジェクト管理や改善方法について書かれています。

Prettierでのコード整形、monorepoとyarn workspace、モジュール構造といった買付環境の整備。
rollupでのflat bundle、Closure Compilerでの圧縮、加えてそれらのproductionビルドに対するテストについて。
また、Public APIに対するテストの重要性や`npm pack`でのpublish状況再現してのテストなど。

Internalにおけるビルドシステムの改善やそれらのモジュールをリリースする仕組みの整備など、大きくなったライブラリ/フレームワークにおけるインフラを細かく紹介しています。

----

[Patterns for designing flexible architecture in node.js (CQRS/ES/Onion)](https://medium.com/@domagojk/patterns-for-designing-flexible-architecture-in-node-js-cqrs-es-onion-7eb10bbefe17 "Patterns for designing flexible architecture in node.js (CQRS/ES/Onion)")という記事では、TypeScriptを使ってCQRS/EventSourcing(ES)パターンでNode.jsアプリを実装する話が書かれています。

記事中に出てくるサンプルアプリは[domagojk/beenion: Online adaptation of a scientific journal publishing and peer reviewing](https://github.com/domagojk/beenion "domagojk/beenion: Online adaptation of a scientific journal publishing and peer reviewing")で公開されています。

かなりしっかりとCQRS/ESパターンについて書かれているのでFluxやRedux(redux-saga)に興味がある人は読んでみると面白いかもしれません。

- Write side(Command side)
- Command
- Command handler
- domain model
- Repository
- Event
- Read side(Query side)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v9.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v9.3.0/](https://nodejs.org/en/blog/release/v9.3.0/ "Node v9.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 9.3.0リリース
`--trace-event-categories`に`node.async_hooks`を追加、`module.builtinModules`でビルトインモジュールの一覧を取得できるようになるなど


----

## moment/CHANGELOG.md at 2.20.0 · moment/moment
[github.com/moment/moment/blob/2.20.0/CHANGELOG.md](https://github.com/moment/moment/blob/2.20.0/CHANGELOG.md "moment/CHANGELOG.md at 2.20.0 · moment/moment")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

moment 2.20.0リリース。
HTML5 inputに対応するフォーマットの追加、`UTC`への変換しないオプションが`toISOString`に追加された

- [moment-2.20.0.md](https://gist.github.com/marwahaha/e0d4135fbf8bb75fa85c4aa2bddc5031 "moment-2.20.0.md")

----

## Introducing Docusaurus · Docusaurus
[docusaurus.io/blog/2017/12/14/introducing-docusaurus.html](https://docusaurus.io/blog/2017/12/14/introducing-docusaurus.html "Introducing Docusaurus · Docusaurus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">document</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

OSSのドキュメントサイト生成ツールであるdocusaurusが正式公開された。
docusaurusが作られた理由や使い方について


----

## Release "Fast" By Default · TypeStrong/ts-node
[github.com/TypeStrong/ts-node/releases/tag/v4.0.0](https://github.com/TypeStrong/ts-node/releases/tag/v4.0.0 "Release \"Fast\" By Default · TypeStrong/ts-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">node.js</span></p>

ts-node 4.0.0リリース。
`--fast`がデフォルトとなった。
`--type-check`を使うことで型チェックを合わせて行うように変更。
`transformers`オプションのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Enter AudioWorklet  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/12/audio-worklet](https://developers.google.com/web/updates/2017/12/audio-worklet "Enter AudioWorklet  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">audio</span> <span class="jser-tag">webworker</span> <span class="jser-tag">JavaScript</span></p>

Chrome 64でフラグ付きの実装が入るAudioWorkletについての解説


----

## The State of JavaScript 2017: Introduction
[stateofjs.com/2017/introduction/](https://stateofjs.com/2017/introduction/ "The State of JavaScript 2017: Introduction")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アンケート</span> <span class="jser-tag">まとめ</span></p>

JavaScriptの開発者アンケートの結果が公開された。
JavaScriptのフロントエンドからバックエンドまで幅広くツールや言語、ライブラリ、CSSなどについて扱っている


----

## モバイル開発に役立つJSデバッグ術 - Mercari Engineering Blog
[tech.mercari.com/entry/2017/12/13/103000](http://tech.mercari.com/entry/2017/12/13/103000 "モバイル開発に役立つJSデバッグ術 - Mercari Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome開発者ツールの機能紹介をしている記事。
Responsive表示、ネットワークスロットリング、CPUスロットリング、全ファイル検索など


----

## The Current State of Implementation and Planning for ESModules
[medium.com/the-node-js-collection/the-current-state-of-implementation-and-planning-for-esmodules-a4ecb2aac07a](https://medium.com/the-node-js-collection/the-current-state-of-implementation-and-planning-for-esmodules-a4ecb2aac07a "The Current State of Implementation and Planning for ESModules")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

Node.jsのES Modulesの実装状況や優先度についての説明。
CommonJSとの相互運用性、mjsのサポート、hook apiのサポート、コアモジュールの対応、`import.meta`についてなど


----

## Behind the Scenes: Improving the Repository Infrastructure - React Blog
[reactjs.org/blog/2017/12/15/improving-the-repository-infrastructure.html](https://reactjs.org/blog/2017/12/15/improving-the-repository-infrastructure.html "Behind the Scenes: Improving the Repository Infrastructure - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Reactのリポジトリのインフラ改善について。
Prettierでのコード整形、monorepoとyarn workspace、モジュール構造、rollupでのflat bundle、Closure Compilerでの圧縮。
productionビルドに対するテスト、Public APIに対するテスト、`npm pack`でのpublish状況再現。
カスタムビルドの対応、リリースフロー整備など


----

## The global \`Reflect\` object, its use cases and things to watch out for
[www.stefanjudis.com/today-i-learned/the-global-reflect-object-its-use-cases-and-things-to-watch-out-for/](https://www.stefanjudis.com/today-i-learned/the-global-reflect-object-its-use-cases-and-things-to-watch-out-for/ "The global \`Reflect\` object, its use cases and things to watch out for")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`Reflect`の使い方について。
`Proxy`と合わせて使うものでオブジェクトの変更のloggingを例解説している。


----

## How to debug front-end: Elements – Pragmatists
[blog.pragmatists.com/how-to-debug-front-end-elements-d97da4cbc3ea](https://blog.pragmatists.com/how-to-debug-front-end-elements-d97da4cbc3ea "How to debug front-end: Elements – Pragmatists")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chromeの開発者ツールの使い方について。
デバッガー、Element inspector、Source、スタイルなどについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## nitin42/react-perf-devtool: A Chrome developer tool extension to inspect performance of React components.
[github.com/nitin42/react-perf-devtool](https://github.com/nitin42/react-perf-devtool "nitin42/react-perf-devtool: A Chrome developer tool extension to inspect performance of React components.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">browser</span> <span class="jser-tag">Extension</span></p>

Reactコンポーネントのパフォーマンス計測ツール。
Reactの`performance.measure`の結果を使い、`react-addons-perf`のような計測結果を表示できるブラウザ拡張とツール


----

## Polymer 2 and Googlebot – Dev Channel – Medium
[medium.com/dev-channel/polymer-2-and-googlebot-2ad50c5727dd](https://medium.com/dev-channel/polymer-2-and-googlebot-2ad50c5727dd "Polymer 2 and Googlebot – Dev Channel – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span></p>

PolymerとGoogle Botへの対応について。
Google BotはChrome 41相当であるため、TranspilerやPolyfill、確認方法などについて


----

## calirojas506/vue-inspector: Vue.js Inspector for Mobile Devices
[github.com/calirojas506/vue-inspector](https://github.com/calirojas506/vue-inspector "calirojas506/vue-inspector: Vue.js Inspector for Mobile Devices")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">debug</span> <span class="jser-tag">mobile</span> <span class="jser-tag">library</span></p>

VueのInspectorライブラリ。
モバイルデバイス上でVueコンポーネントのデバッグをする目的のツール


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## nik-garmash/hyntax: Straightforward HTML parser
[github.com/nik-garmash/hyntax](https://github.com/nik-garmash/hyntax "nik-garmash/hyntax: Straightforward HTML parser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">library</span></p>

HTMLパーサライブラリ


----

## developit/microbundle: 📦 Zero-configuration bundler for tiny modules.
[github.com/developit/microbundle](https://github.com/developit/microbundle "developit/microbundle: 📦 Zero-configuration bundler for tiny modules.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

設定ファイルなしでbundleする目的のRollupのラッパーツール。


----

## xtuc/js-webassembly-interpreter: WebAssembly interpreter
[github.com/xtuc/js-webassembly-interpreter](https://github.com/xtuc/js-webassembly-interpreter "xtuc/js-webassembly-interpreter: WebAssembly interpreter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

WebAssemblyインタープリタ


----

## Popmotion - A functional JavaScript motion library
[popmotion.io/](https://popmotion.io/ "Popmotion - A functional JavaScript motion library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

関数でモーションを扱うアニメーションライブラリ


----

## ballercat/walt: Walt is a JavaScript-like syntax for WebAssembly text format WIP
[github.com/ballercat/walt](https://github.com/ballercat/walt "ballercat/walt: Walt is a JavaScript-like syntax for WebAssembly text format WIP")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">Tools</span></p>

JavaScript/Flowのサブセットのように書けて、WebAssemblyにコンパイルできる言語とツール


----

## franciscop/state: State management tool using Proxy()
[github.com/franciscop/state](https://github.com/franciscop/state "franciscop/state: State management tool using Proxy()")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`Proxy`を使ったステート管理ライブラリ。


----

## sveltejs/sapper: Combat-ready apps, engineered by Svelte
[github.com/sveltejs/sapper](https://github.com/sveltejs/sapper "sveltejs/sapper: Combat-ready apps, engineered by Svelte")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

SvelteをつかったNext.jsのようなフレームワーク

- [What is Sapper?](https://sapper-template.now.sh/blog/what-is-sapper "What is Sapper?")

----
<h1 class="site-genre">書籍関係</h1>

----

## Manning | Electron in Action
[www.manning.com/books/electron-in-action](https://www.manning.com/books/electron-in-action "Manning | Electron in Action")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">book</span></p>

2018年5月1日発売
Electronについての書籍


----

## Patterns for designing flexible architecture in node.js (CQRS/ES/Onion)
[medium.com/@domagojk/patterns-for-designing-flexible-architecture-in-node-js-cqrs-es-onion-7eb10bbefe17](https://medium.com/@domagojk/patterns-for-designing-flexible-architecture-in-node-js-cqrs-es-onion-7eb10bbefe17 "Patterns for designing flexible architecture in node.js (CQRS/ES/Onion)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">CQRS</span> <span class="jser-tag">EventSourcing</span> <span class="jser-tag">DDD</span> <span class="jser-tag">JavaScript</span></p>

TypeScriptを使ってCQRS+EventSourcingのパターンでNode.jsアプリを実装する記事。
サンプルプロジェクトと共にコマンドからイベントを作りそれをRepositoryに保存する流れを紹介してる。

- [domagojk/beenion: Online adaptation of a scientific journal publishing and peer reviewing](https://github.com/domagojk/beenion "domagojk/beenion: Online adaptation of a scientific journal publishing and peer reviewing")

----
