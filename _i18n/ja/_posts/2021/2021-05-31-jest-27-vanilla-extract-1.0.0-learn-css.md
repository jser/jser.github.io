---
title: "2021-05-31のJS: Jest 27、vanilla-extract 1.0.0、Learn CSS"
author: "azu"
layout: post
date : 2021-05-31T14:26:57.997Z
category: JSer
tags:
- TypeScript
- CSS
- Tools
- testing
- node.js

---

JSer.info #542 - - [Release 27.0.0 · facebook/jest](https://github.com/facebook/jest/releases/tag/v27.0.0)
- [Release 27.0.0 · facebook/jest](https://github.com/facebook/jest/releases/tag/v27.0.0)
----

- [vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.](https://vanilla-extract.style/)
- [🧁🍨 Mark Dalgleish on Twitter: "🧁🎉 Announcing vanilla-extract v1.0! 💪 Locally scoped, type-safe styles, variables + themes. 🦄 Minimal abstraction over CSS. 🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack. ✅ Now stable + production ready. 🙇‍♂️ Enjoy! https://t.co/Ejaf4anfbj" / Twitter](https://twitter.com/markdalgleish/status/1398158090294292482)

----

- [Learn CSS](https://web.dev/learn/css/)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## sinon/CHANGELOG.md at master · sinonjs/sinon
[github.com/sinonjs/sinon/blob/master/CHANGELOG.md#1110--2021-05-25](https://github.com/sinonjs/sinon/blob/master/CHANGELOG.md#1110--2021-05-25 "sinon/CHANGELOG.md at master · sinonjs/sinon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

sinon.js 11.1.0リリース。
PromiseをFakeする`sinon.promise()`の実装など


----

## Jest 27: New Defaults for Jest, 2021 edition ⏩ · Jest
[jestjs.io/blog/2021/05/25/jest-27](https://jestjs.io/blog/2021/05/25/jest-27 "Jest 27: New Defaults for Jest, 2021 edition ⏩ · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 27リリース。
デフォルトが大きく変わるリリースとなっていて、`jest-circus`のデフォルト化、fake timersのデフォルトを`@sinonjs/fake-timers`ベースの`modern`に変更している。
機能追加として、失敗したテストをインタラクティブに実行できるように、inline snapshotsをprettierの依存なく実行できるようになど。
また、`done`の複数回呼び出しをエラーとしたり、Promiseを返すのと`done`の混在を禁止したり、TypeScriptの型を厳密化するといった変更も含まれる

- [Release 27.0.0 · facebook/jest](https://github.com/facebook/jest/releases/tag/v27.0.0 "Release 27.0.0 · facebook/jest")

----

## Announcing TypeScript 4.3 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-3/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-3/ "Announcing TypeScript 4.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.3リリース
setterにgetterとは異なる型を指定できるように、`override`キーワードの追加、Template String Typeの改善。
Private Class Elements(fields/methods/accessors)のサポート、`static` Index Signatureのサポート。
`ConstructorParameters`がAbstract classをサポート、Genericsにおける型の絞り込みの改善、Promiseオブジェクトを条件式に渡してしまうミスのチェックを追加。
その他には、`.tsbuildinfo`のサイズ改善、watch時の初回ビルドの改善など。


----

## Announcing Vendure v1.0 | Vendure E-commerce
[www.vendure.io/blog/2021/05/announcing-vendure-v1.0/](https://www.vendure.io/blog/2021/05/announcing-vendure-v1.0/ "Announcing Vendure v1.0 | Vendure E-commerce")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">GraphQL</span></p>

GraphQL/TypeScriptベースのeコマースフレームワークであるVendure v1.0リリース。

- [vendure-ecommerce/vendure: A headless GraphQL ecommerce framework for the modern web](https://github.com/vendure-ecommerce/vendure "vendure-ecommerce/vendure: A headless GraphQL ecommerce framework for the modern web")

----

## Optimized images for Nuxt
[image.nuxtjs.org/](https://image.nuxtjs.org/ "Optimized images for Nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Nuxt.js向けの画像最適化モジュール


----

## ECMAScript proposal updates @ 2021-05 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2021/05/29/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2021/05/29/ecmascript-proposal-update "ECMAScript proposal updates @ 2021-05 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2021年5月のTC39ミーティングでStageの変更があったProposalのまとめ。
Top-Level awaitとRegExp Match IndicesがStage 4となりES2022に含まれることが決まった


----

## New Release: 2.13.0
[jshint.com/blog/2021-05-30/release-2-13-0/](https://jshint.com/blog/2021-05-30/release-2-13-0/ "New Release: 2.13.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.13.0リリース。
`export * as ns from`、`import.meta`、Dynamic `import()`、Optional Chaining、Nullish Coalescingのサポートなど


----

## Lit 2.0: Meet Lit, all over again! – Lit
[lit.dev/blog/2021-04-21-lit-2.0-meet-lit-all-over-again/](https://lit.dev/blog/2021-04-21-lit-2.0-meet-lit-all-over-again/ "Lit 2.0: Meet Lit, all over again! – Lit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Lit 2.0 RCリリース。
`lit-html`と`LitELement`を一つにまとめて`lit`パッケージの公開、ウェブサイトの刷新がおコン割れている。
ファイルサイズやパフォーマンスの改善、SSRの対応などが含まれている

- [Lit Launch Event - YouTube](https://www.youtube.com/watch?v=f1j7b696L-E "Lit Launch Event - YouTube")
- [Introducing &amp;quot;Lit&amp;quot; for Web Components](https://zenn.dev/takanorip/articles/640f9fe9c6c8ca "Introducing &amp;amp;quot;Lit&amp;amp;quot; for Web Components")

----
<h1 class="site-genre">アーティクル</h1>

----

## 5 steps to faster web fonts /// Iain Bean
[iainbean.com/posts/2021/5-steps-to-faster-web-fonts/](https://iainbean.com/posts/2021/5-steps-to-faster-web-fonts/ "5 steps to faster web fonts /// Iain Bean")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span> <span class="jser-tag">article</span></p>

Web Fontsのローディングについての連載。
`font-display`でのテキストの表示と切り替わるタイミングのまとめ


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## xqq/mpegts.js: HTML5 MPEG2-TS Stream Player
[github.com/xqq/mpegts.js](https://github.com/xqq/mpegts.js "xqq/mpegts.js: HTML5 MPEG2-TS Stream Player")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">library</span></p>

flv.jsをベースにしたMPEG-2 TS steram playerライブラリ。
HTTPとWebSocketを使ったMPEG-2 TS streamの再生、低遅延、低スペックマシンでも再生できることを目的にしている。
flv.jsベースであるため、FLV containerもサポートしている。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Learn CSS
[web.dev/learn/css/](https://web.dev/learn/css/ "Learn CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span></p>

CSSについて一通り扱うチュートリアル講座。
Box Model、セレクタ、詳細度、CSSの単位などの基本的な概念から、GridやFlexboxなどのレイアウト、ColorやmarginなどのCSSプロパティの解説、擬似クラスや疑似要素などを扱う


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## wwwtyro/candygraph: Fast by default, flexible 2D plotting library.
[github.com/wwwtyro/candygraph](https://github.com/wwwtyro/candygraph "wwwtyro/candygraph: Fast by default, flexible 2D plotting library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">graphic</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

パフォーマンスに目的を置いた2Dグラフ描画ライブラリ


----

## lume/autolayout: Apple&#039;s Auto Layout and Visual Format Language for JavaScript (using cassowary constraints)
[github.com/lume/autolayout](https://github.com/lume/autolayout "lume/autolayout: Apple&#039;s Auto Layout and Visual Format Language for JavaScript (using cassowary constraints)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Auto LayoutとVisual Format Languageの実装ライブラリ


----

## plantain-00/type-coverage: A CLI tool to check type coverage for typescript code
[github.com/plantain-00/type-coverage](https://github.com/plantain-00/type-coverage "plantain-00/type-coverage: A CLI tool to check type coverage for typescript code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TypeScriptの型カバレッジを出すツール


----

## vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.
[vanilla-extract.style/](https://vanilla-extract.style/ "vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

vanilla-extract v1.0リリース。
TypeScriptでスタイルをJSとして`.css.ts`に書いて`class`属性に指定したものをコンパイルすると、CSSファイルを生成するフレームワークに依存しないツールキット。
ビルド時に静的に展開されるAPIと実行時に動作するDynamic API、webpackやViteなどの各種ツールに対応したプラグインが用意されている。

- [🧁🍨 Mark Dalgleish on Twitter: &amp;quot;🧁🎉 Announcing vanilla-extract v1.0! 💪 Locally scoped, type-safe styles, variables + themes. 🦄 Minimal abstraction over CSS. 🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack. ✅ Now stable + production ready. 🙇‍♂️ Enjoy! https://t.co/Ejaf4anfbj&amp;quot; / Twitter](https://twitter.com/markdalgleish/status/1398158090294292482 "🧁🍨 Mark Dalgleish on Twitter: &amp;amp;quot;🧁🎉 Announcing vanilla-extract v1.0! 💪 Locally scoped, type-safe styles, variables + themes. 🦄 Minimal abstraction over CSS. 🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack. ✅ Now stable + production ready. 🙇‍♂️ Enjoy! https://t.co/Ejaf4anfbj&amp;amp;quot; / Twitter")

----
<h1 class="site-genre">書籍関係</h1>

----

## WebAssembly: The Definitive Guide
[learning.oreilly.com/library/view/webassembly-the-definitive/9781492089834/](https://learning.oreilly.com/library/view/webassembly-the-definitive/9781492089834/ "WebAssembly: The Definitive Guide")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">book</span></p>

2021年12月発売予定
WebAsseblyについての書籍


----
