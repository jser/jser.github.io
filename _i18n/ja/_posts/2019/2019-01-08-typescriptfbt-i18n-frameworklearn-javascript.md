---
title: "2019-01-08のJS: TypeScriptのロードマップ、FBT i18n Framework、Learn JavaScript"
author: "azu"
layout: post
date : 2019-01-08T02:22:36.982Z
category: JSer
tags:
- TypeScript
- i18n
- JavaScript

---

JSer.info #417 - TypeScriptの2019年前半のロードマップが、次のIssueで公開されています。

- [TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/29288)

`allowJs`や`checkJS`などでJavaScriptも扱うようになったため、さらにJS/JSDocの扱いの改善してTypeScriptへのマイグレーションがスムーズにできるようにすること。
またLintへの取り組みでは、TSLintはルールの仕組み上パフォーマンスに問題がありそれを改善するには既存のルールにも影響を与えるため、TSLintではなくESLintでのTypeScriptのLint改善をしていく方針について書かれています。

また、TypeScript Compilerのパフォーマンス改善や整形などをCLIから行えるようにするといったCLIの改善、ドキュメントの改善、Playgroundで`tsconfig.json`の設定できるようにするといった改善などに取り組んでいく方針について書かれています。

このロードマップに対してのフィードバックも募集しています。
意見がある人は書いてみるとよいかもしれません。

機能的なロードマップについては、次のページで公開されているので合わせてみるとよさそうです。

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap)

----

[Learn JavaScript](https://learnjavascript.online/)というJavaScriptの学習サイトが公開されています。

ES2015なども含めた基本的なJavaScriptの書き方について練習問題を解いていきながら学べるサイトとなっています。
すべての問題にテストが書かれており、そのテストを通るようにJavaScriptを書いていく[code kata](https://en.wikipedia.org/wiki/Kata_(programming%29)です。

復習用にFlashcardsも用意されているので、JavaScriptを書いて学びたい人は触ってみると良さそうです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 2.9.0 · qunitjs/qunit
[github.com/qunitjs/qunit/releases/tag/2.9.0](https://github.com/qunitjs/qunit/releases/tag/2.9.0 "Release 2.9.0 · qunitjs/qunit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.9.0リリース


----

## Release v2.1.3 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v2.1.3](https://github.com/facebook/create-react-app/releases/tag/v2.1.3 "Release v2.1.3 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">react</span> <span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 2.1.3リリース。
`webpack-dev-server@3.1.10`以下にあった脆弱性を修正したバージョンを取り込んでいる

- [Sniffing Codes in Hot Module Reloading Messages - crblog](https://blog.cal1.cn/post/Sniffing%20Codes%20in%20Hot%20Module%20Reloading%20Messages "Sniffing Codes in Hot Module Reloading Messages - crblog")
- [Release v3.1.11 · webpack/webpack-dev-server](https://github.com/webpack/webpack-dev-server/releases/tag/v3.1.11 "Release v3.1.11 · webpack/webpack-dev-server")
- [npm](https://www.npmjs.com/advisories/725 "npm")

----
<h1 class="site-genre">アーティクル</h1>

----

## Page Object pattern in JavaScript | LinkedIn
[www.linkedin.com/pulse/page-object-pattern-javascript-vladim%C3%ADr-gorej/](https://www.linkedin.com/pulse/page-object-pattern-javascript-vladim%C3%ADr-gorej/ "Page Object pattern in JavaScript | LinkedIn")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Selenium WebDriverを使ったページオブジェクトパターンについて。
ページオブジェクトとはどのようなものか、要素の抽象化、遅延処理、ページオブジェクトにAssertを含めないことについてなど


----

## Odi - server-side framework - DEV Community 👩‍💻👨‍💻
[dev.to/dantsk/odi---server-side-framework-2ep7](https://dev.to/dantsk/odi---server-side-framework-2ep7 "Odi - server-side framework - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.js向けのサーバサイドフレームワーク。Decoratorを使った宣言的な定義やTypeScriptの`emitDecoratorMetadata`を使ったDTOなどを持つ。
類似するコンセプトを持つNestjsとの違いについてなど

- [Odi-ts/odi: 🌪🌌 Opinionated, Declarative, Idiomatic framework for building scalable, supportable, enterprise applications and servers.](https://github.com/Odi-ts/odi "Odi-ts/odi: 🌪🌌 Opinionated, Declarative, Idiomatic framework for building scalable, supportable, enterprise applications and servers.")

----

## Neural networks in JavaScript | Scrimba.com
[scrimba.com/g/gneuralnetworks](https://scrimba.com/g/gneuralnetworks "Neural networks in JavaScript | Scrimba.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">library</span></p>

ニューラルネットワークライブラリであるBrain.jsのインタラクティブなチュートリアル

- [BrainJS/brain.js: 🤖 Neural networks in JavaScript](https://github.com/BrainJS/brain.js "BrainJS/brain.js: 🤖 Neural networks in JavaScript")

----

## TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript
[github.com/Microsoft/TypeScript/issues/29288](https://github.com/Microsoft/TypeScript/issues/29288 "TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span> <span class="jser-tag">article</span></p>

TypeScriptのロードマップ。
JS/JSDocの扱いの改善、TSLintではなくESLintでのTSのLint改善、パフォーマンス改善、CLIの改善、ドキュメントの改善、Playgroundの改善などに取り組んでいく


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Learn JavaScript
[learnjavascript.online/](https://learnjavascript.online/ "Learn JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">webservice</span></p>

JavaScriptについてテストを通るようにコードを書いて学べるサイト。
それぞれの項目に対して大量の練習問題があり、復習用にFlashcardsが用意されている。


----

## GoogleChromeLabs/webm-wasm: webm-wasm lets you create webm videos in JavaScript via WebAssembly.
[github.com/GoogleChromeLabs/webm-wasm](https://github.com/GoogleChromeLabs/webm-wasm "GoogleChromeLabs/webm-wasm: webm-wasm lets you create webm videos in JavaScript via WebAssembly.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">C++</span></p>

webmをエンコードするWebAssemblyライブラリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## facebookincubator/fbt: A JavaScript Internationalization Framework
[github.com/facebookincubator/fbt](https://github.com/facebookincubator/fbt "facebookincubator/fbt: A JavaScript Internationalization Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">u18</span> <span class="jser-tag">library</span> <span class="jser-tag">babel</span></p>

Facebookのi18n JavaScriptフレームワーク。
ソースコードからフレーズの収集、翻訳ファイルの管理、関数やJSXでの翻訳表示、babelプラグインなどを持ったi18nフレームワーク


----

## RunJS - Write and run JavaScript instantly
[projects.lukehaas.me/runjs/](https://projects.lukehaas.me/runjs/ "RunJS - Write and run JavaScript instantly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mac</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">software</span> <span class="jser-tag">node.js</span></p>

JavaScriptを実行した結果をside by sideで表示できるmacOS向けのアプリ


----
