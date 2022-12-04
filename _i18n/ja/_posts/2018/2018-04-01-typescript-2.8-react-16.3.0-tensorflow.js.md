---
title: "2018-04-01のJS: TypeScript 2.8、React 16.3.0、TensorFlow.js"
author: "azu"
layout: post
date : 2018-04-01T05:56:39.824Z
category: JSer
tags:
- TypeScript
- react
- ML

---

JSer.info #377 - TypeScript 2.8が正式リリースされました。

- [Announcing TypeScript 2.8 | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/)
- [TypeScript 2.8.1 変更点 - Qiita](https://qiita.com/vvakame/items/2e32aeded05997f77dfa)

Conditional Typesのサポートされ、またConditional Typesを使ったビルトインの型として`Exclude<T, U>`, `Extract<T, U>`, `NonNullable<T>`, `ReturnType<T>`, `InstanceType<T>`が追加されています。
mapped type modifierの`+`、`-`のサポート、`.d.ts`ファイルだけを出力できる`emitDeclarationOnly`オプションの追加、`@jsx`プラグマコメントのサポートなどが行われています。

----

React 16.3.0がリリースされました。

- [React v16.3.0: New lifecycles and context API - React Blog](https://reactjs.org/blog/2018/03/29/react-v-16-3.html "React v16.3.0: New lifecycles and context API - React Blog")
- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")

今後に向けた大きな変更が追加されています。
新しい[Context](https://reactjs.org/docs/context.html "Context") APIの追加、`createRef`メソッドの追加、`forwardRef`メソッドの追加、`StrictMode`コンポーネントの追加などが行われています。

また非同期レンダリングのサポートのためなどにReactコンポーネントのライフサイクルイベントの変更が行われています。
`componentWillMount`、`componentWillReceiveProps`、`componentWillUpdate`は今後削除されていく方向になり、代わりに`getDerivedStateFromProps`と`getSnapshotBeforeUpdate`が追加されています。

次のようなタイムラインで上記のライフサイクルイベントのAPIの削除が行われていくようです。

- 16.3: それぞれaliasとなる`UNSAFE_componentWillMount`, `UNSAFE_componentWillReceiveProps`, ` UNSAFE_componentWillUpdate`の追加
  - `UNSAFE_` prefixへのマイグレーションスクリプトとして[rename-unsafe-lifecycles](https://github.com/reactjs/react-codemod#rename-unsafe-lifecycles "rename-unsafe-lifecycles")が公開されている
- A future 16.x release: `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate`は非推奨となり警告を表示
- 17.0: `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate`を削除
  - ただし緩やかなマイグレーションのために`UNSAFE_`版は17.xでも動作を維持する

そのため、古いAPIが完全に削除されるのは18.0となる予定です。(`UNSAFE_`版は17.xでも残るため)
詳しくは次の記事で解説されています。

- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")

----

[TensorFlow.js](https://js.tensorflow.org/ "TensorFlow.js")はブラウザでTensorFlowのモデルを使った機械学習を行えるライブラリです。
元々Googleが開発していた[deeplearn.js](https://deeplearnjs.org/index.html "deeplearn.js")の後継バージョンとして公開されています。

JavaScriptとhigh-level layers APIで機械学習を行えるため、初めて機械学習を学ぶJavaScript開発者をターゲットについていることなどについてが次の記事で書かれています。

- [Introducing TensorFlow.js: Machine Learning in JavaScript](https://medium.com/tensorflow/introducing-tensorflow-js-machine-learning-in-javascript-bf3eab376db "Introducing TensorFlow.js: Machine Learning in JavaScript")

また、既存のTensorFlowやKerasのモデルを変換してインポートできブラウザ上で再学習なども行えます。
現在はWebGLに依存しているためブラウザのみで動作し、Node.jsのサポートについては検討中であることなどがFAQにかかれています。

- [FAQ – TensorFlow.js](https://js.tensorflow.org/faq/)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## React v16.3.0: New lifecycles and context API - React Blog
[reactjs.org/blog/2018/03/29/react-v-16-3.html](https://reactjs.org/blog/2018/03/29/react-v-16-3.html "React v16.3.0: New lifecycles and context API - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v16.3.0リリース。
新しいContext APIの追加、`createRef`メソッドの追加、`forwardRef`メソッドの追加。
コンポーネントライフサイクルイベントの変更と追加、`StrictMode`コンポーネントの追加など

- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")
- [React v16.3.0: New lifecycles and context API【日本語翻訳】 | maesblog](https://mae.chab.in/archives/60040 "React v16.3.0: New lifecycles and context API【日本語翻訳】 | maesblog")

----

## March 2018 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/march-2018-security-releases/](https://nodejs.org/en/blog/vulnerability/march-2018-security-releases/ "March 2018 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.jsのセキュリティアップデートとして、それぞれのLTSと開発バージョンのアップデートが公開された

- Node.js 9.10.0
- Node.js 8.11.0 (LTS "Carbon")
- Node.js 6.14.0 (LTS "Boron")
- Node.js 4.9.0 (LTS "Argon")


----

## V8 JavaScript Engine: V8 release v6.6
[v8project.blogspot.com/2018/03/v8-release-66.html](https://v8project.blogspot.com/2018/03/v8-release-66.html "V8 JavaScript Engine: V8 release v6.6")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.6(Chrome 66)リリース。
ECMAScript Proposalの対応として`Function#toString()`の仕様追従、JSがJSONのsupersetとなる仕様追従。
また`catch`構文のパラメータを省略に対応、`String#trimStart`や`String#trimEnd`の実装など。
Background compilationの対応やAsync、Arrayのパフォーマンス改善など

- [Function.prototype.toString revision](https://tc39.github.io/Function-prototype-toString-revision/ "Function.prototype.toString revision")
- [tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262](https://github.com/tc39/proposal-json-superset "tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262")
- [tc39/proposal-string-left-right-trim: A proposal to the ECMAScript standard for including left and right trim of whitespace to strings](https://github.com/tc39/proposal-string-left-right-trim "tc39/proposal-string-left-right-trim: A proposal to the ECMAScript standard for including left and right trim of whitespace to strings")

----

## ZEIT – Next.js 5.1: Faster Page Resolution, Environment Config & More
[zeit.co/blog/next5-1](https://zeit.co/blog/next5-1 "ZEIT – Next.js 5.1: Faster Page Resolution, Environment Config & More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 5.1リリース。
ページロードの速度改善、設定を定義できる`publicRuntimeConfig`と`serverRuntimeConfig`を追加、エラーハンドリングの改善など


----

## Release v3.4.0 · storybooks/storybook
[github.com/storybooks/storybook/releases/tag/v3.4.0](https://github.com/storybooks/storybook/releases/tag/v3.4.0 "Release v3.4.0 · storybooks/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ui </span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

Storybook 3.4.0リリース。
Polymer 2サポート、AngularとVueのstoryshotサポートなど


----

## power-assert/CHANGELOG.md at v1.5.0 · power-assert-js/power-assert
[github.com/power-assert-js/power-assert/blob/v1.5.0/CHANGELOG.md](https://github.com/power-assert-js/power-assert/blob/v1.5.0/CHANGELOG.md "power-assert/CHANGELOG.md at v1.5.0 · power-assert-js/power-assert")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 1.5.0リリース。
Node.js 9.9.0で追加された`assert`のstrict modeをサポート

- [Node v9.9.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v9.9.0/ "Node v9.9.0 (Current) | Node.js")
- [Assert | Node.js v9.10.1 Documentation](https://nodejs.org/api/assert.html#assert_strict_mode "Assert | Node.js v9.10.1 Documentation")

----

## 📦 Parcel v1.7.0: – devongovett – Medium
[medium.com/@devongovett/parcel-v1-7-0-9aac0c505837](https://medium.com/@devongovett/parcel-v1-7-0-9aac0c505837 "📦 Parcel v1.7.0: – devongovett – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v1.7.0リリース。
`.vue`とPugのサポート、出力するファイルにハッシュ値を付与するように、absolute pathとtilde(`~`) pathのサポート、必要な依存を自動的にインストールするようになるなど


----

## Dart Sass 1.0.0 is Released « Sass Blog
[sass.logdown.com/posts/7045860-dart-sass-100-is-released](http://sass.logdown.com/posts/7045860-dart-sass-100-is-released "Dart Sass 1.0.0 is Released « Sass Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart Sass 1.0リリース。
Ruby Sassについてはメンテナンスモードとなる。


----

## ESLint v5.0.0-alpha.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/03/eslint-v5.0.0-alpha.0-released](https://eslint.org/blog/2018/03/eslint-v5.0.0-alpha.0-released "ESLint v5.0.0-alpha.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">serverless</span></p>

ESLint 5.0.0αリリース。
予定される破壊的な変更についてはマイグレーションガイドで解説されている。

- [ESLint v5.0.0 変更点まとめ (随時更新) - Qiita](https://qiita.com/mysticatea/items/f34097961bf2827b675d "ESLint v5.0.0 変更点まとめ (随時更新) - Qiita")
- [Migrating to v5.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/docs/5.0.0/user-guide/migrating-to-5.0.0 "Migrating to v5.0.0 - ESLint - Pluggable JavaScript linter")

----

## Announcing TypeScript 2.8 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/](https://blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/ "Announcing TypeScript 2.8 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">TypeScript</span></p>

TypeScript 2.8リリース。 Conditional Types、d.tsのみの出力に対応、`@jsx` pragmaコメントのサポート、mapped type modifierの`+`、`-`のサポートなど

- [TypeScript 2.8.1 変更点 - Qiita](https://qiita.com/vvakame/items/2e32aeded05997f77dfa "TypeScript 2.8.1 変更点 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Server Timing APIを使ってサーバーサイドのベンチマークを手軽にやる | ブログ :: Web notes.log
[blog.wnotes.net/blog/article/server-side-benchmark-using-server-timing-api](http://blog.wnotes.net/blog/article/server-side-benchmark-using-server-timing-api "Server Timing APIを使ってサーバーサイドのベンチマークを手軽にやる | ブログ :: Web notes.log")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

Server Timinig APIを使いサーバサイドのリクエストごとのベンチマークをとり、Chromeの開発者ツールに表示するライブラリについて


----

## Update on Async Rendering - React Blog
[reactjs.org/blog/2018/03/27/update-on-async-rendering.html](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

非同期レンダリングのためのライフサイクルイベントの追加と変更について。
16.3でイベントの追加、16.xで古いイベントに警告を表示、17.0で古いイベントを廃止。
また追加された`getDerivedStateFromProps`と`getSnapshotBeforeUpdate`についての解説


----

## Working with the new CSS Typed Object Model  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/cssom](https://developers.google.com/web/updates/2018/03/cssom "Working with the new CSS Typed Object Model  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

CSS Typed OMについての解説。
すでにある`style`プロパティと新しく追加された`attributeStyleMap`の違いや、CSS Typed OMで追加されたAPIのメリットや実際の使い方について


----

## WebAssembly/esm-integration: ECMAScript module integration
[github.com/WebAssembly/esm-integration](https://github.com/WebAssembly/esm-integration "WebAssembly/esm-integration: ECMAScript module integration")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">module</span> <span class="jser-tag">ECMAScript</span></p>

ES Module Integration Proposal for WebAssembly


----

## How display: contents; Works
[bitsofco.de/how-display-contents-works/](https://bitsofco.de/how-display-contents-works/ "How display: contents; Works")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

`display: contents;` の解説


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## CondeNast/perf-timeline-cli: Generate Chrome Performance Timelines via a command line interface
[github.com/CondeNast/perf-timeline-cli](https://github.com/CondeNast/perf-timeline-cli "CondeNast/perf-timeline-cli: Generate Chrome Performance Timelines via a command line interface")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Chrome開発者ツールのPerformanceパネルの情報を取得するCLIツール。
Puppeteerを使ってアクセスした結果を取得する


----

## JavaScript in 14 minutes by Jeremy Thomas
[jgthms.com/javascript-in-14-minutes/](https://jgthms.com/javascript-in-14-minutes/ "JavaScript in 14 minutes by Jeremy Thomas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

ブラウザの開発者ツールで実行しながら学べるJavaScriptチュートリアル


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## cmseaton42/task-easy: A simple, customizable, and lightweight priority queue for promises.
[github.com/cmseaton42/task-easy](https://github.com/cmseaton42/task-easy "cmseaton42/task-easy: A simple, customizable, and lightweight priority queue for promises.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promiseスケジュールライブラリ


----

## asfktz/Awaity.js: A functional, lightweight alternative to bluebird.js, built with async / await in mind.
[github.com/asfktz/Awaity.js](https://github.com/asfktz/Awaity.js "asfktz/Awaity.js: A functional, lightweight alternative to bluebird.js, built with async / await in mind.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

async/awaitベースのコレクション系ライブラリ
map、filter、reduceなどのPromiseに対するコレクション操作を提供するライブラリ


----

## jacobbogers/libRmath.js: Javascript Pure Implementation of Statistical R "core" numerical libRmath.so
[github.com/jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js "jacobbogers/libRmath.js: Javascript Pure Implementation of Statistical R \"core\" numerical libRmath.so")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">R </span> <span class="jser-tag">library</span></p>

Rの`math`をJavaScriptにポートしたライブラリ


----

## TensorFlow.js
[js.tensorflow.org/](https://js.tensorflow.org/ "TensorFlow.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span></p>

tensorflowのJavaScript版。
WebGLを使った機械学習を行え、既存の学習モデルはconverterで変換し利用できる。

- [tensorflow/tfjs-converter: Convert TensorFlow SavedModel and Keras models to TensorFlow.js](https://github.com/tensorflow/tfjs-converter "tensorflow/tfjs-converter: Convert TensorFlow SavedModel and Keras models to TensorFlow.js")

----

## jaywcjlove/hotkeys: ➷ A robust Javascript library for capturing keyboard input. It has no dependencies.
[github.com/jaywcjlove/hotkeys](https://github.com/jaywcjlove/hotkeys "jaywcjlove/hotkeys: ➷ A robust Javascript library for capturing keyboard input. It has no dependencies.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">キーボード</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

ショートカットキー管理ライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## React開発　現場の教科書 | マイナビブックス
[book.mynavi.jp/ec/products/detail/id&#x3D;88735](https://book.mynavi.jp/ec/products/detail/id=88735 "React開発　現場の教科書 | マイナビブックス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

ReactとAtomic Designについての書籍


----

## CSS Pocket Reference, 5th Edition - O'Reilly Media
[shop.oreilly.com/product/0636920146353.do](http://shop.oreilly.com/product/0636920146353.do "CSS Pocket Reference, 5th Edition - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2018年4月発売。
CSSリファレンス本


----
