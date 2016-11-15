---
title: "2016-11-15のJS: TypeScript 2.1RC、Node.js v7.1.0"
author: azu
layout: post
date : 2016-11-15T10:22
category: JSer
tags:
    - TypeScript
    - Node.js

---

JSer.info #305 - TypeScript 2.1 RCがリリースされました。

- [TypeScript 2.1 RC: Better Inference, Async Functions, and More | TypeScript](https://blogs.msdn.microsoft.com/typescript/2016/11/08/typescript-2-1-rc-better-inference-async-functions-and-more/ "TypeScript 2.1 RC: Better Inference, Async Functions, and More | TypeScript")
- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#21-november-2016 "Roadmap · Microsoft/TypeScript Wiki")
- [TypeScript 2.1.1 変更点 - Qiita](http://qiita.com/vvakame/items/305749d3d6dc6bf877c6 "TypeScript 2.1.1 変更点 - Qiita")

2.1ではasync/awaitがES3とES5への出力ができるようになりました。
また、tsconfig.jsonに`extends`の追加、`--target ESNext`のサポート、JSXをReact以外でも利用できるように[--jsxFactory](https://github.com/Microsoft/TypeScript/pull/12135 "--jsxFactory")の追加などが行われています。

RC時点(2.1.1)ではまだ入っていませんが、正式リリース時には[Mapped types](https://github.com/Microsoft/TypeScript/pull/12114 "Mapped types")などの追加も予定されています。

----

Node.js v7.1.0リリースされました。

- [Node v7.1.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v7.1.0/ "Node v7.1.0 (Current) | Node.js")

Node.js v7.0.0で`String(global)`に[意図しない破壊的な変更](https://github.com/nodejs/node/issues/9274 "Native class of `global` changed in Node v7 · Issue #9274 · nodejs/node")が入っていたのが修正されました。

V8の[ECMAScript仕様追従](https://tc39.github.io/ecma262/#sec-object.prototype.tostring)により、Node.js v7.0.0で`String(global)`が`"[object Object]"`を返すようになっていました。

```js
String(global);// "[object Object]"
```

そのため`global[Symbol.toStringTag]`が定義されました。これにより、今までと同じ `"[object global]"`が返されるようになっています。

```js
String(global);// "[object global]"
```

- [lib: make `String(global) === '[object global]'` by addaleax · Pull Request #9279 · nodejs/node](https://github.com/nodejs/node/pull/9279 "lib: make `String(global) === &#39;[object global]&#39;` by addaleax · Pull Request #9279 · nodejs/node")

この[パターン](https://github.com/nodejs/node/issues/9274#issuecomment-256149041)はNode.jsで実行されているかを判定するために使ってるモジュールがあったため、一度元の挙動(Node.js v6)に戻すことになりました。

- [npm grep for 'object global' on Oct 26 2016](https://gist.github.com/addaleax/01e287d8a1674eaeaaa3af725f7653ef "npm grep for &#39;object global&#39; on Oct 26 2016")
- [lib: make `String(global) === '[object global]'` by addaleax · Pull Request #9279 · nodejs/node](https://github.com/nodejs/node/pull/9279#issuecomment-257724083 "lib: make `String(global) === &#39;[object global]&#39;` by addaleax · Pull Request #9279 · nodejs/node")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## TestCafe v0.10.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-10-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-10-0-released.html "TestCafe v0.10.0 Released | TestCafe")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v0.10.0リリース。
Snapshot APIを扱いやすく、automatic waitの仕組みを改善、`speed`オプションでテストの実行速度をコントールできるようになるなど

----

## TypeScript 2.1 RC: Better Inference, Async Functions, and More | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/11/08/typescript-2-1-rc-better-inference-async-functions-and-more/](https://blogs.msdn.microsoft.com/typescript/2016/11/08/typescript-2-1-rc-better-inference-async-functions-and-more/ "TypeScript 2.1 RC: Better Inference, Async Functions, and More | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.1 RCリリース。
`any`型の改善、tsconfig.jsonの`extends`対応、async/awaitがES3/ES5へ出力できるようになるなど

- [TypeScript 2.1.1 変更点 - Qiita](http://qiita.com/vvakame/items/305749d3d6dc6bf877c6 "TypeScript 2.1.1 変更点 - Qiita")

----

## Node v7.1.0 (Current) | Node.js
[nodejs.org/en/blog/release/v7.1.0/](https://nodejs.org/en/blog/release/v7.1.0/ "Node v7.1.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v7.1.0リリース。
V8の仕様追従により意図しない破壊的な変更が起きていた。

```js
String(global);// "[object Object]"
```

そのため`global[Symbol.toStringTag]`が定義された。これにより、今までと同じ `"[object global]"`が返されるようになった。

```js
String(global);// "[object global]"
```

- [lib: make `String(global) === '[object global]'` by addaleax · Pull Request #9279 · nodejs/node](https://github.com/nodejs/node/pull/9279 "lib: make `String(global) === &#39;[object global]&#39;` by addaleax · Pull Request #9279 · nodejs/node")

----

## Release Notes for Safari Technology Preview 17 | WebKit
[webkit.org/blog/7071/release-notes-for-safari-technology-preview-17/](https://webkit.org/blog/7071/release-notes-for-safari-technology-preview-17/ "Release Notes for Safari Technology Preview 17 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 17リリース。
NPAPIプラグインのサポート終了、Custom Elementのデフォルト有効化、`rel=noopener`のサポートなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Migrating to Jest – Medium
[medium.com/@kentcdodds/migrating-to-jest-881f75366e7e](https://medium.com/@kentcdodds/migrating-to-jest-881f75366e7e "Migrating to Jest – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">testing</span></p>

AVAとMochaでのテストをJestにマイグレーションする方法とツール(codemods)について。
UI testsの時間が短縮されてる。

- [skovhus/jest-codemods: Codemods for migrating to Jest https://github.com/facebook/jest](https://github.com/skovhus/jest-codemods "skovhus/jest-codemods: Codemods for migrating to Jest https://github.com/facebook/jest")

----

## Migrating an Angular 1 App to Angular 2 - Part 1
[auth0.com/blog/migrating-an-angular-1-app-to-angular-2-part-1/](https://auth0.com/blog/migrating-an-angular-1-app-to-angular-2-part-1/ "Migrating an Angular 1 App to Angular 2 - Part 1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">tutorial</span></p>

AngularJS 1.xのアプリをAngularJS 2へマイグレーションするチュートリアル

- [auth0-blog/ng2-dinos: A sample Angular 2 application](https://github.com/auth0-blog/ng2-dinos "auth0-blog/ng2-dinos: A sample Angular 2 application")

----

## FLOCSSを使ってCSSファイルを20,000行から9,000行にした話 - Qiita
[qiita.com/Atsss/items/4f9d98fb1d0546539c09](http://qiita.com/Atsss/items/4f9d98fb1d0546539c09 "FLOCSSを使ってCSSファイルを20,000行から9,000行にした話 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">リファクタリング</span></p>

CSSのリファクタリング手法や方針について。
どのようなフローでリファクタリングを進めていったかや進捗の可視化について

----

## 2016年、Web Audio API はどう変わったのか? | g200kg Music &amp; Software
[www.g200kg.com/archives/2016/11/2016web-audio-a.html](http://www.g200kg.com/archives/2016/11/2016web-audio-a.html "2016年、Web Audio API はどう変わったのか? | g200kg Music & Software")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">API</span></p>

Web Audio APIの変更点について。
AudioWorkerがAudioWorkletにリネーム、ConstantSourceNodeの追加、コンストラクタのサポートなど

----

## Writing a JavaScript Framework - Data Binding with ES6 Proxies | @RisingStack
[blog.risingstack.com/writing-a-javascript-framework-data-binding-es6-proxy/](http://blog.risingstack.com/writing-a-javascript-framework-data-binding-es6-proxy/ "Writing a JavaScript Framework - Data Binding with ES6 Proxies | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ProxyやReflect APIを使い、値の変更を監視するObservableライブラリ。
ES5のgetter/setterを使ったアプローチとの比較

- [RisingStack/nx-observe: Next gen data observation/binding with ES6 Proxies](https://github.com/RisingStack/nx-observe "RisingStack/nx-observe: Next gen data observation/binding with ES6 Proxies")

----

## Pitfall: not all objects can be proxied transparently
[www.2ality.com/2016/11/proxying-builtins.html](http://www.2ality.com/2016/11/proxying-builtins.html "Pitfall: not all objects can be proxied transparently")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES2015のProxyでhandlerオブジェクトが空である場合に透過的な動作を期待するがそうではないという話

----

## Logging Errors in Client-Side Applications
[www.sitepoint.com/logging-errors-client-side-apps/](https://www.sitepoint.com/logging-errors-client-side-apps/ "Logging Errors in Client-Side Applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">library</span></p>

クライアントサイドのロガーやエラー収集サービスについてのまとめ

----

## Improving Perceived Performance with Multiple Background Images – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts
[csswizardry.com/2016/10/improving-perceived-performance-with-multiple-background-images/](http://csswizardry.com/2016/10/improving-perceived-performance-with-multiple-background-images/ "Improving Perceived Performance with Multiple Background Images – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">画像</span></p>

`background-image`に指定した画像が表示されるまで、`linear-gradient`を使った模様を代替表示するFallbackについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Chrome Dev Summit 2016 - YouTube
[www.youtube.com/user/ChromeDevelopers](https://www.youtube.com/user/ChromeDevelopers "Chrome Dev Summit 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Chrome Dev Summit 2016の動画まとめ

- [Chrome Dev Summit 2016](https://developer.chrome.com/devsummit/ "Chrome Dev Summit 2016")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## deck.gl
[uber.github.io/deck.gl/](https://uber.github.io/deck.gl/ "deck.gl")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">library</span></p>

Uber製のWebGLを使ったデータビジュアライゼーションライブラリ

----

## doiuse...?
[www.doiuse.com/](http://www.doiuse.com/ "doiuse...?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">tool</span></p>

CSSをペーストして指定したブラウザ(autoprefixerのフォーマット)で利用できるかをチェックできるツール

- [anandthakker/doiuse: Lint CSS for browser support against caniuse database.](https://github.com/anandthakker/doiuse "anandthakker/doiuse: Lint CSS for browser support against caniuse database.")

----

## caiogondim/logdown.js: Debug utility with markdown support that runs on browser and server
[github.com/caiogondim/logdown.js](https://github.com/caiogondim/logdown.js "caiogondim/logdown.js: Debug utility with markdown support that runs on browser and server")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">library</span></p>

ブラウザとNode.jsで動くシンプルなロガーライブラリ

----

## th0r/webpack-bundle-analyzer: Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap
[github.com/th0r/webpack-bundle-analyzer](https://github.com/th0r/webpack-bundle-analyzer "th0r/webpack-bundle-analyzer: Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

webpackのbundleの構成要素やサイズをビジュアライズできるプラグイン

----

## DJWassink/Promise-parallel-throttle: It&#x27;s like Promise.all(), but throttled!
[github.com/DJWassink/Promise-parallel-throttle](https://github.com/DJWassink/Promise-parallel-throttle "DJWassink/Promise-parallel-throttle: It's like Promise.all(), but throttled!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

一度に実行する数を指定できる`Promise.all`的なライブラリ

----

## dop251/goja: ECMAScript 5.1(+) implementation written in Go
[github.com/dop251/goja](https://github.com/dop251/goja "dop251/goja: ECMAScript 5.1(+) implementation written in Go")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">golang</span></p>

ECMAScriptのGo言語実装。
ES5.1相当の実装をしてる

----

## dhamaniasad/HeadlessBrowsers: A list of (almost) all headless web browsers in existence
[github.com/dhamaniasad/HeadlessBrowsers](https://github.com/dhamaniasad/HeadlessBrowsers "dhamaniasad/HeadlessBrowsers: A list of (almost) all headless web browsers in existence")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">まとめ</span></p>

ヘッドレスブラウザ(テストのためのライブラリも含む)のまとめ

----
