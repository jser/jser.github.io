---
title: "2018-05-22のJS: Firefox 61の開発者ツール、Next.js 6、Data-Forge"
author: "azu"
layout: post
date : 2018-05-21T23:42:56.258Z
category: JSer
tags:
- firefox
- Next.js
- data

---

JSer.info #384 - [New in Firefox 61: Developer Edition – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/05/new-in-firefox-61-developer-edition/)という記事ではFirefox 61の変更点について紹介されています。

Source Mapの対応改善、HARファイルのimport/export、パネルの入れ替えのサポート、アクセシビリティインスペクタの追加などが行われています。

Source Mapの対応改善について詳しくは次の記事で紹介されています。

- [Debugging Modern Web Applications – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/05/debugging-modern-web-applications/)

----

Reactを使ったフレームワークであるNext.js 6がリリースされました。

- [ZEIT – Next.js 6 and Nextjs.org](https://zeit.co/blog/next6)
- [Release 6.0.0 · zeit/next.js](https://github.com/zeit/next.js/releases/tag/6.0.0)


`_app.js`でデフォルトの`App`の挙動を拡張できるようになりました。
Babel 7(RC)にアップデートされ、これにより[`@babel/preset-typescript`](https://github.com/babel/babel/tree/master/packages/babel-preset-typescript)を使ってTypeScriptをサポートする例などが紹介されています。

Babelがアップデートされたことにより`.babelrc`で拡張している場合は[babel-upgrade](https://github.com/babel/babel-upgrade)などを使いBabel関係のアップデートも必要となる場合があります。

- [migration from 5 to 6 · Issue #4239 · zeit/next.js](https://github.com/zeit/next.js/issues/4239)

また、<https://learnnextjs.com>のドキュメントが[Getting Started - Learn Next.js](https://nextjs.org/learn/)にマージされています。

----

データ処理ライブラリの[Data-Forge](http://www.data-forge-js.com/)が公開されました。

[Data-Forge](http://www.data-forge-js.com/)はCSVやJSONなどのデータの読み込み、加工、集約、整形などを行えます。
読み込んだデータは一度[DataFrame](https://github.com/data-forge/data-forge-ts/blob/master/docs/concepts.md#dataframe)に変換され、DataFrameに対してデータ処理を行う形になっていて[pandas](https://github.com/pandas-dev/pandas)をインスパイアしています。

また、これらのデータ処理をメソッドチェーンで書くようになっていて、内部的には[Iterable / Iterator](https://github.com/data-forge/data-forge-ts/blob/master/docs/concepts.md#iterable--iterator)で処理されます。

```js
dataForge.readFileSync('input.csv')     // Read input file.
    .parseCSV()                         // Parse CSV data to a dataframe.
    .parseInts("Column2", "Column3")    // Parse from strings to integers.
    .parseDates("Column4")              // Parse from strings to date objects.
    .dropSeries("Column5")              // Don't want column 5.
    .where(row => predicate(row))       // Filter out rows that you don't want.
    .select(row => transform(row))      // Apply transformation to each row.
    .asCSV()                            // Write out data file in CSV (or other) format.
    .writeFileSync('output.csv');       // Write output file.
```

同じ作者によってJavaScriptによるデータラングリングについての書籍も書かれているようです。

- [Manning | Data Wrangling with JavaScript](https://www.manning.com/books/data-wrangling-with-javascript?a_aid=datawranglingwithjavascript&a_bid=acc654f9)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Firefox 61: Developer Edition – Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2018/05/new-in-firefox-61-developer-edition/](https://hacks.mozilla.org/2018/05/new-in-firefox-61-developer-edition/ "New in Firefox 61: Developer Edition – Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 61 Developer Editionの変更点について。
開発者ツールの改善、Source Mapの対応改善、HARファイルのimport/export、アクセシビリティインスペクタの追加など。


----

## TestCafe v0.20.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-20-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-20-0-released.html "TestCafe v0.20.0 Released | TestCafe")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v0.20.0リリース。
HTTPリクエスト、レスポンスのhookを行えるように。
proxyを無視できるパターンを指定できるようになるなど


----

## Announcing TypeScript 2.9 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/05/16/announcing-typescript-2-9-rc/](https://blogs.msdn.microsoft.com/typescript/2018/05/16/announcing-typescript-2-9-rc/ "Announcing TypeScript 2.9 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.9 RCリリース。
`keyof`がSymbolとnumberに対応、`import(path)` typeのサポート、`import.meta`のサポート、JSXのgenericsをサポートなど


----

## saadq/lynt: ✨ A zero config JavaScript linter with support for Typescript, Flow, and React.
[github.com/saadq/lynt](https://github.com/saadq/lynt "saadq/lynt: ✨ A zero config JavaScript linter with support for Typescript, Flow, and React.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span> <span class="jser-tag">flowtype</span></p>

設定なしに使えることを目的としたLintツール。
ESLintやTSLintを使いopinionatedなLintを行う。
スタイルに関するルールは含めずにエラーに関するものだけに限定している。


----

## ZEIT – Next.js 6 and Nextjs.org
[zeit.co/blog/next6](https://zeit.co/blog/next6 "ZEIT – Next.js 6 and Nextjs.org")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 6リリース。
`_app.js`でアプリのライフサイクルなどに対して拡張できるように、Babel 7(RC)にアップデート、`@babel/preset-typescript`を使ってTypeScriptをサポートなど


----

## Release v5.2.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v5.2.0](https://github.com/mochajs/mocha/releases/tag/v5.2.0 "Release v5.2.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 5.2.0リリース。
`mocha.opts`にコメントがかけるように、APIドキュメントの更新など

- [Home - Documentation](https://mochajs.org/api/ "Home - Documentation")

----

## Release 3.0.0-beta.1 - 2018.05.20 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.0.0-beta.1](https://github.com/zloirock/core-js/releases/tag/v3.0.0-beta.1 "Release 3.0.0-beta.1 - 2018.05.20 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 3.0.0 β1リリース。
Proposalである`Object.fromEntries`、`Map`や`Set`のコレクションメソッドの実装など。
あわせてwithdrawされたProposalの実装を削除。
またいくつかのブラウザバージョンでのバグに対処など

- [core-js@3 by zloirock · Pull Request #325 · zloirock/core-js](https://github.com/zloirock/core-js/pull/325 "core-js@3 by zloirock · Pull Request #325 · zloirock/core-js")

----

## Chromium Blog: Evolving Chrome's security indicators
[blog.chromium.org/2018/05/evolving-chromes-security-indicators.html](https://blog.chromium.org/2018/05/evolving-chromes-security-indicators.html "Chromium Blog: Evolving Chrome's security indicators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">HTTPS</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">security</span></p>

ChromeのHTTPSとHTTPのURLバーの表示の変更予定について。
HTTPSはデフォルトになっていくため"Secure"ラベルを外していき、
HTTPの方が例外的なものとして"Not Secure"というラベルをつけるという方針について。


----
<h1 class="site-genre">アーティクル</h1>

----

## Storybook vs Styleguidist – Chroma
[blog.hichroma.com/storybook-vs-styleguidist-2bd93d6dcc06](https://blog.hichroma.com/storybook-vs-styleguidist-2bd93d6dcc06 "Storybook vs Styleguidist – Chroma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

StorybookとStyleguidistの違い、どのようなときに使うのかについて


----

## Type-Safe Object Merging in TypeScript 2.8
[spin.atomicobject.com/2018/05/14/type-safe-object-merging-2-8/](https://spin.atomicobject.com/2018/05/14/type-safe-object-merging-2-8/ "Type-Safe Object Merging in TypeScript 2.8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 2.8のConditional Typeを使ったType Safeなオブジェクトマージについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Native JavaScript modules by Serg Hospodarets
[slides.com/malyw/native-js-modules#/](https://slides.com/malyw/native-js-modules#/ "Native JavaScript modules by Serg Hospodarets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">slide</span></p>

ES modulesについてのスライド。
AMD、CommonJSなどとの比較、`<script type=module>`がDeferred by defaultであることやmoduleの動作について。
また循環参照の対応、パスの扱い、Dynamic import、パフォーマンスやテストなどについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## sloria/local-repl: 🐚 Project-specific configuration for the Node.js REPL
[github.com/sloria/local-repl](https://github.com/sloria/local-repl "sloria/local-repl: 🐚 Project-specific configuration for the Node.js REPL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Node.jsでプロジェクト毎にaliasや依存などを指定できるREPL


----

## home
[layerjs.org/](https://layerjs.org/ "home")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">HTML</span> <span class="jser-tag">animation</span></p>

`Stage`と`Frame`の属性を付けた要素を元にレイヤーを作り、トランジションなどの遷移アニメーションを表現するライブラリ。


----

## planttheidea/fast-copy: A blazing fast deep object copier
[github.com/planttheidea/fast-copy](https://github.com/planttheidea/fast-copy "planttheidea/fast-copy: A blazing fast deep object copier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

オブジェクトのdeep copyを行うライブラリ。


----

## Data-Forge
[www.data-forge-js.com/](http://www.data-forge-js.com/ "Data-Forge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

CSVやJSONなどのデータの読み込み、加工、集約、整形などを行うライブラリ。
LINQとPandasをインスパイアして作成されていて、メソッドチェーン(内部的にIterator)で処理を書ける。

- [Manning | Data Wrangling with JavaScript](https://www.manning.com/books/data-wrangling-with-javascript?a_aid=datawranglingwithjavascript&a_bid=acc654f9 "Manning | Data Wrangling with JavaScript")

----

## rsuite/rsuite: A suite of React components .
[github.com/rsuite/rsuite](https://github.com/rsuite/rsuite "rsuite/rsuite: A suite of React components .")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Reactを使ったUIコンポーネント集ライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Manning | Data Wrangling with JavaScript
[www.manning.com/books/data-wrangling-with-javascript?a\_aid&#x3D;datawranglingwithjavascript&amp;a\_bid&#x3D;acc654f9](https://www.manning.com/books/data-wrangling-with-javascript?a_aid=datawranglingwithjavascript&a_bid=acc654f9 "Manning | Data Wrangling with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptを使ったデータラングリング(データ処理)についての書籍


----

## Pro Vue.js 2: Adam Freeman: 9781484238042: Amazon.com: Books
[www.amazon.com/dp/1484238044/](https://www.amazon.com/dp/1484238044/ "Pro Vue.js 2: Adam Freeman: 9781484238042: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2019年1月17日発売
Vueについての書籍


----
