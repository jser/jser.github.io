---
title: "2021-11-30のJS: Lighthouse 9.1.0、Storybook 6.4.0、DenoのNode.js互換モード"
author: "azu"
layout: post
date : 2021-11-30T03:18:08.366Z
category: JSer
tags:
- Tools
- node.js
- CSS
- Chrome
- performance

---

JSer.info #568 - Lighthouse 9.1.0がリリースされました。

- [Release v9.1.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0)

Next.js向けのStack Packが追加されたため、Next.jsのアプリに対するAuditが追加されています。

- [feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs](https://github.com/GoogleChrome/lighthouse-stack-packs/pull/66)

----

Storybook 6.4.0がリリースされました。

- [Release v6.4.0 · storybookjs/storybook](https://github.com/storybookjs/storybook/releases/tag/v6.4.0)

[Storybook Addon Interactions](https://github.com/storybookjs/storybook/tree/next/addons/interactions)でInteractionsタブが追加され、インタラクション操作のシミュレートとデバッグができるようになっています。
また、Storybook向けのESLintプラグインである[storybookjs/eslint-plugin-storybook](https://github.com/storybookjs/eslint-plugin-storybook)が公開されています。

----

Denoでは、現在[Node.js compability mode](https://deno.land/manual@v1.16.3/npm_nodejs/compatibility_mode)が開発されており、今後この互換性を上げていく方針となっています。

- [Improve Node Compat Mode · Issue #12577 · denoland/deno](https://github.com/denoland/deno/issues/12577)

[Deno のこれまでとこれから JSConf JP 2021](https://kt3k.github.io/talk_jsconfjp2021/#1)という発表では、このNode.js互換モードの開発がなぜ進められているのかについて話されています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/fC4oZJmvfI0?start=9735" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 3.0.0 · emscripten-core/emscripten
[github.com/emscripten-core/emscripten/releases/tag/3.0.0](https://github.com/emscripten-core/emscripten/releases/tag/3.0.0 "Release 3.0.0 · emscripten-core/emscripten")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">LLVM</span></p>

Emscripten 3.0.0リリース


----

## Prettier 2.5: TypeScript 4.5 and MDX v2 comment syntax! · Prettier
[prettier.io/blog/2021/11/25/2.5.0.html](https://prettier.io/blog/2021/11/25/2.5.0.html "Prettier 2.5: TypeScript 4.5 and MDX v2 comment syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.5リリース。
TypeScript 4.5のサポート、MDX v2のコメント構文をサポート、HTMLの`class`属性を複数行に整形していたのを1行に戻す変更など


----

## Release 8.4 “President Camio” · postcss/postcss
[github.com/postcss/postcss/releases/tag/8.4.0](https://github.com/postcss/postcss/releases/tag/8.4.0 "Release 8.4 “President Camio” · postcss/postcss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

PostCSS 8.4リリース。
WarningとErrorにRangeを指定できるように、プラグインが指定されていない場合にパース処理を実際にアクセスするまで遅延させるように。
パッケージサイズの削減など


----

## Release v9.1.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0 "Release v9.1.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse v9.1.0リリース。
Next.js向けのauditを追加など

- [feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs](https://github.com/GoogleChrome/lighthouse-stack-packs/pull/66 "feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs")

----

## Release 12.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v12.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v12.0.0 "Release 12.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Firefox</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer 12.0.0リリース。
Chromium 97.0.4692.0へアップデート、Firefoxで`userDataDir`の指定をサポートなど


----

## Release v6.4.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v6.4.0](https://github.com/storybookjs/storybook/releases/tag/v6.4.0 "Release v6.4.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 6.4.0リリース。
Interactions stories、ESLintプラグインの追加など

- [storybook/addons/interactions at next · storybookjs/storybook](https://github.com/storybookjs/storybook/tree/next/addons/interactions "storybook/addons/interactions at next · storybookjs/storybook")
- [storybookjs/eslint-plugin-storybook: Official ESLint plugin for Storybook](https://github.com/storybookjs/eslint-plugin-storybook "storybookjs/eslint-plugin-storybook: Official ESLint plugin for Storybook")

----

## Release v5.0.0 · chalk/chalk
[github.com/chalk/chalk/releases/tag/v5.0.0](https://github.com/chalk/chalk/releases/tag/v5.0.0 "Release v5.0.0 · chalk/chalk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Chalk 5.0.0リリース。
pure ESMに変更、default exportからnamed exportへ変更。
また、`keyword()`/`hsl()`/`hsv()`/`hwb()`/`ansi()`を削除、Template Literalを`chalk-template`パッケージに移行など


----

## berstend/node-safe: 🤠 Make using Node.js safe again with Deno-like permissions
[github.com/berstend/node-safe](https://github.com/berstend/node-safe "berstend/node-safe: 🤠 Make using Node.js safe again with Deno-like permissions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">macOS</span> <span class="jser-tag">security</span> <span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

macOSのsandbox機能を利用してDenoライクなSandboxの仕組みを実装したNodeの実行ツール。
`--allow-read`、`--allow-net`など許可リストを指定してスクリプト実行やnpm/yarn/npxにも対応している。


----
<h1 class="site-genre">アーティクル</h1>

----

## CI 環境でのユニットテストの実行時間を2倍速くした話 (Jest + Mongo DB + Circle CI) - ミツモア Tech blog
[engineering.meetsmore.com/entry/2021/01/21/134930](https://engineering.meetsmore.com/entry/2021/01/21/134930 "CI 環境でのユニットテストの実行時間を2倍速くした話 (Jest + Mongo DB + Circle CI) - ミツモア Tech blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">jest</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jestでのユニットテストの実行時間の削減についての記事。
テストの並列化、変更したファイルのみをテスト、Worker単位でのDBの初期化、CIでキャッシュについて


----

## Publish ESM and CJS in a single package
[antfu.me/posts/publish-esm-and-cjs](https://antfu.me/posts/publish-esm-and-cjs "Publish ESM and CJS in a single package")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

CommonJSとESMのデュアルフォーマットでのパッケージ公開について。
`package.json`の`exports`フィールドでの使い分け、tsupとunbuildのビルドについて。
ESMでは利用できないCommonJSの`__dirname`などの補完方法について


----

## New – Real-User Monitoring for Amazon CloudWatch | AWS News Blog
[aws.amazon.com/jp/blogs/aws/cloudwatch-rum/](https://aws.amazon.com/jp/blogs/aws/cloudwatch-rum/ "New – Real-User Monitoring for Amazon CloudWatch | AWS News Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

CloudWatchでRUMを取得できるサービスがリリースされた。
JavaScriptのタグを埋め込むことで、Web Vitalsなどのメトリクスデータなどを取得できる。

- [aws-observability/aws-rum-web: Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web "aws-observability/aws-rum-web: Amazon CloudWatch RUM Web Client")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Deno のこれまでとこれから JSConf JP 2021
[kt3k.github.io/talk\_jsconfjp2021/#1](https://kt3k.github.io/talk_jsconfjp2021/#1 "Deno のこれまでとこれから JSConf JP 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">slide</span></p>

Denoの設計や採用事例についてのスライド。
また現在進めているNode.js互換モードについて。

- [Improve Node Compat Mode · Issue #12577 · denoland/deno](https://github.com/denoland/deno/issues/12577 "Improve Node Compat Mode · Issue #12577 · denoland/deno")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## postcss-rs/postcss-rs: 🚀 Fast and 100% API compatible postcss replacer, built in Rust
[github.com/postcss-rs/postcss-rs](https://github.com/postcss-rs/postcss-rs "postcss-rs/postcss-rs: 🚀 Fast and 100% API compatible postcss replacer, built in Rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span> <span class="jser-tag">Rust</span></p>

PostCSSのRust実装


----

## Tamagui — React Native + Web UI kit
[tamagui.dev/](https://tamagui.dev/ "Tamagui — React Native + Web UI kit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Design</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

React NativeとWebに対応したスタイリングライブラリ。
Propsでスタイルを渡し、コンパイル時にはAtomic CSSが生成されて、コンポーネントにはクラス名が指定される。


----
