---
title: "2017-01-24のJS: webpack 2正式リリース、JavaScriptの開発環境設定、2016 JS :star:"
author: azu
layout: post
date : 2017-01-24T10:33
category: JSer
tags:
    - webpack
    - JavaScript
---

JSer.info #315 - webpack 2.xの正式版としてwebpack v2.2.0がリリースされました。

- [Release v2.2.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v2.2.0 "Release v2.2.0 · webpack/webpack")
- [🎉 webpack 2.2: The Final Release 🎉 – webpack – Medium](https://medium.com/webpack/webpack-2-2-the-final-release-76c3d43bf144 "🎉 webpack 2.2: The Final Release 🎉 – webpack – Medium")

[公式サイト](https://webpack.js.org/ "webpack")も2.xに対応したものとなっています。
設定ファイル周りの細かい変更が多いですが、v1からv2への移行ガイドも公開されているので合わせて見ると良いです。

- [Migrating from v1 to v2](https://webpack.js.org/guides/migrating/ "Migrating from v1 to v2")

また、webpack 2では、TreeShakingと呼ばれる機能が追加されています。

- [Demystifying webpack2 tree shaking - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2017/01/24/110152 "Demystifying webpack2 tree shaking - from scratch")

今後の機能追加や改善については、投票ツールを通じて決定していくようです。
(投票の重み付けに利用されている[Open Collectiveについてのスライド](http://azu.github.io/slide/2017/t_wada_sushi/OpenCollective.html "Open Collective")を書いたので、併せてみるといいかもしれません)

- [https://webpack.js.org/vote/](https://webpack.js.org/vote/)

投票のサイトを見ると今のところ次の開発候補としてはScope Hoisting(Rollupインスパイアな最適化)、Typescript周りの改善などが上がっているようです。

----

[Modern JavaScript概観、そしてElectronへ](http://blog.satotaichi.info/modern-javascript_201701/)という記事では、JavaScriptの開発環境設定について書かれています。

型、Babelのエコシステム、Lint、テスト、UIフレームワーク、CSS、アーキテクチャ、ビルドなど幅広い内容を扱っています。
また、どのような選択肢からなぜそのツール/ライブラリを選んだのかという点について詳しく書かれています。

----

[2016 JavaScript Rising Stars](https://risingstars2016.js.org/ "2016 JavaScript Rising Stars")というサイトでは、2016年においてGitHub Starの増加率でランキングした結果が書かれています。

右側にそれぞれの結果に登場したもの対する説明が書かれているので、一度見てみると良いかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v2.2.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v2.2.0](https://github.com/webpack/webpack/releases/tag/v2.2.0 "Release v2.2.0 · webpack/webpack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 2.2.0正式版リリース。

- [Migrating from v1 to v2](https://webpack.js.org/guides/migrating/ "Migrating from v1 to v2")
- [🎉 webpack 2.2: The Final Release 🎉 – webpack – Medium](https://medium.com/webpack/webpack-2-2-the-final-release-76c3d43bf144#.ibgliase6 "🎉 webpack 2.2: The Final Release 🎉 – webpack – Medium")

----

## TestCafe v0.12.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-12-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-12-0-released.html "TestCafe v0.12.0 Released | TestCafe")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v0.12.0リリース。
ベーシック認証/NTLM認証のサポート、CIでの動作改善、テストのスキップ、`test.before`と`test.after`の追加、ESLintプラグインの追加など

----
<h1 class="site-genre">アーティクル</h1>

----

## Modern JavaScript概観、そしてElectronへ
[blog.satotaichi.info/modern-javascript\_201701/](http://blog.satotaichi.info/modern-javascript_201701/ "Modern JavaScript概観、そしてElectronへ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Electron</span> <span class="jser-tag">babel</span></p>

JavaScriptの環境設定をめぐる試行について。
TypeScriptやFlowなどの型システム、Babelのエコシステム、Lint、テストフレームワーク、UIフレームワーク、CSS、アーキテクチャ、ビルドなど。
幅広いツール/ライブラリの中で、どのような考えで何を選んだかについて書かれている。

----

## アメブロ2016 ~ Isomorphic JavaScriptの詳しい話 | CyberAgent Developers Blog | サイバーエージェント デベロッパーズブログ
[developers.cyberagent.co.jp/blog/archives/3513/](https://developers.cyberagent.co.jp/blog/archives/3513/ "アメブロ2016 ~ Isomorphic JavaScriptの詳しい話 | CyberAgent Developers Blog | サイバーエージェント デベロッパーズブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">isomorphic</span></p>

クライアントサイドとサーバサイドのどちらでも動くIsomorphicなJavaScriptを書くために気をつける点について。
Reactコンポーネント、Fetch、スタイルシート、環境変数、ルーティング、表示領域の扱い，パフォーマンス計測についてなど

----

## Making transpiled ES modules more spec-compliant
[www.2ality.com/2017/01/babel-esm-spec-mode.html](http://www.2ality.com/2017/01/babel-esm-spec-mode.html "Making transpiled ES modules more spec-compliant")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">node.js</span></p>

ES Modulesを仕様と現在のTranspilerの挙動について。
ECMAScriptとNode.jsのモジュールのInteroperabilityについて

----

## Module Bundling and Webpack in Simple Terms
[arianv.com/post/Module-Bundling-and-Webpack-in-Simple-Terms/](http://arianv.com/post/Module-Bundling-and-Webpack-in-Simple-Terms/ "Module Bundling and Webpack in Simple Terms")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpackがどのようにモジュールをbundleしているかを丁寧に解説した記事

----

## TypeScript 2.1: Mapped Types | Marius Schulz
[blog.mariusschulz.com/2017/01/20/typescript-2-1-mapped-types](https://blog.mariusschulz.com/2017/01/20/typescript-2-1-mapped-types "TypeScript 2.1: Mapped Types | Marius Schulz")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2.1で入ったMapped Typesについて。
`Object.freeze`などを例にMapped Typesの使い方を解説している

----

## Dragons when upgrading from Angular 2.1.x to 2.4.x – Medium
[medium.com/@abookone/dragons-when-upgrading-from-angular-2-1-x-to-2-4-x-530de5a763cb](https://medium.com/@abookone/dragons-when-upgrading-from-angular-2-1-x-to-2-4-x-530de5a763cb "Dragons when upgrading from Angular 2.1.x to 2.4.x – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

Angular 2.1から2.4へのアップデートにおけるハマりどころについて

----

## Vue + Vuex — Getting started – Medium
[medium.com/@bradfmd/vue-vuex-getting-started-f78c03d9f65](https://medium.com/@bradfmd/vue-vuex-getting-started-f78c03d9f65 "Vue + Vuex — Getting started – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">tutorial</span></p>

Vuexについての導入チュートリアル

----

## Server-side Rendering Shootout with Marko, Preact, Rax, React and Vue
[hackernoon.com/server-side-rendering-shootout-with-marko-preact-rax-react-and-vue-25e1ae17800f](https://hackernoon.com/server-side-rendering-shootout-with-marko-preact-rax-react-and-vue-25e1ae17800f "Server-side Rendering Shootout with Marko, Preact, Rax, React and Vue")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">template</span></p>

UIライブラリ/テンプレートエンジンであるMarkoのサーバサイドレンダリングの高速化手法について。
Marko v4ではブラウザとサーバで出力方式を変えている。
クライアントサイドではVirtual DOMを使い、サーバサイドでは文字列結合をベースとした出力を使い分けている。

- [Marko v4 Multiple Compilation Targets](https://gist.github.com/mlrawlings/8b67bee58df45709e232f689b873e1d1 "Marko v4 Multiple Compilation Targets")
- [feat: add marko by mlrawlings · Pull Request #11 · taobaofed/server-side-rendering-comparison](https://github.com/taobaofed/server-side-rendering-comparison/pull/11 "feat: add marko by mlrawlings · Pull Request #11 · taobaofed/server-side-rendering-comparison")
- [marko/ROADMAP.md at master · marko-js/marko](https://github.com/marko-js/marko/blob/master/ROADMAP.md "marko/ROADMAP.md at master · marko-js/marko")

----

## 3 New CSS Features to Learn in 2017
[bitsofco.de/3-new-css-features-to-learn-in-2017/](https://bitsofco.de/3-new-css-features-to-learn-in-2017/ "3 New CSS Features to Learn in 2017")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

最近のブラウザで利用できる新しいCSSの機能について。
Feature Queries、Grid Layout、CSS Variables

----

## ES2016 / ES2017の最新動向を追ってみた - Qiita
[qiita.com/yuyake0084/items/3c901f37ed7333d4da16](http://qiita.com/yuyake0084/items/3c901f37ed7333d4da16 "ES2016 / ES2017の最新動向を追ってみた - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES2016、2017で追加された構文や機能について

----

## Introduction to WebAssembly — Rasmus Andersson
[rsms.me/wasm-intro](https://rsms.me/wasm-intro "Introduction to WebAssembly — Rasmus Andersson")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span></p>

WebAssemblyの中身を見ていく話。
セマンティクス、type section、メモリアドレス、JavaScriptのAPIについて

----

## Functional Programing in Javascript | Lifelong Learning
[vmayakumar.wordpress.com/2017/01/17/functional-programing-in-javascript/](https://vmayakumar.wordpress.com/2017/01/17/functional-programing-in-javascript/ "Functional Programing in Javascript | Lifelong Learning")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptでの関数型プログラミングについて。
Adequate/mostly-adequate-guideを元にしている

- [MostlyAdequate/mostly-adequate-guide: Mostly adequate guide to FP (in javascript)](https://github.com/MostlyAdequate/mostly-adequate-guide "MostlyAdequate/mostly-adequate-guide: Mostly adequate guide to FP (in javascript)")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## 2016 JavaScript Rising Stars
[risingstars2016.js.org/](https://risingstars2016.js.org/ "2016 JavaScript Rising Stars")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">github</span></p>

2016年にGitHubのstarの増加率でランキングをつけた結果について。
それぞれのライブラリやツールについても簡単に解説されている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Voca: The JavaScript string library
[vocajs.com/](https://vocajs.com/ "Voca: The JavaScript string library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

文字列操作系のUtils集ライブラリ

----

## lorenzofox3/zora: A less than 200 lines of code javascript test harness for nodejs and the browser
[github.com/lorenzofox3/zora](https://github.com/lorenzofox3/zora "lorenzofox3/zora: A less than 200 lines of code javascript test harness for nodejs and the browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Generatorを使った小さなテストフレームワーク

----

## alibaba/rax: A universal React-compatible render engine.
[github.com/alibaba/rax](https://github.com/alibaba/rax "alibaba/rax: A universal React-compatible render engine.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

ReactライクなAPIを持つUniversalなViewライブラリ。
ブラウザだけではなく、アプリ(Weex)やサーバでも動作させることが目的。

- [rax/difference-with-react.md at master · alibaba/rax](https://github.com/alibaba/rax/blob/master/docs/difference-with-react.md "rax/difference-with-react.md at master · alibaba/rax")
- [Weex](https://weex-project.io/ "Weex")
- [(question) Inferno/Preact comparison · Issue #81 · alibaba/rax](https://github.com/alibaba/rax/issues/81 "(question) Inferno/Preact comparison · Issue #81 · alibaba/rax")

----
