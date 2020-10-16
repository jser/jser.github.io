---
title: "2020-10-13のJS: Chrome 86、webpack 5、Browserify 17"
author: "azu"
layout: post
date : 2020-10-13T01:08:50.516Z
category: JSer
tags:
- Chrome
- webpack
- browserify

---

JSer.info #509 - Chrome 86がリリースされました。

- [New in Chrome 86  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/10/nic86)
- <https://www.chromestatus.com/features#milestone%3D86>
- [Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More](https://blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html)

File System Access API、CSS 擬似クラスの`:focus-visible`、Document-Policyヘッダなどのサポートなどが行われています。
Origin TrialとしてWebHID API、Multi-Screen Window Placement APIなどのサポートが追加されています。

また、Web Components v0の削除、FTPサポートの非推奨化が始まっています。

- [Deprecations and removals in Chrome 86  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/09/chrome-86-deps-rems)

----

webpack 5がリリースされました。

- [Webpack 5 release (2020-10-10) | webpack](https://webpack.js.org/blog/2020-10-10-webpack-5-release/)

破壊的な変更と機能追加などかなり幅広い変更を含むメジャーアップデートとなっています。

破壊的な変更として、自動的なNode.jsのpolyfillの削除、デフォルトの出力コードにES2015が含まれるように、非推奨のオプションの削除やオプション名の変更などが含まれています。
機能追加として、filesystem cache、Asset modules、JSON Modules、`import.meta`、Worker script、Module Federation、Async modulesのサポートされています。
また、`target`オプションが`browserslist`をサポート、CommonJSのTree Shakingをサポート、コード生成とTree Shakingの改善なども行われています。

スケジュール通りのリリースのため、まだ既知のバグやloader側の対応がリリースされていない場合もあります。

- [Issues · webpack/webpack](https://github.com/webpack/webpack/labels/webpack-5)

4.xから5.xへのアップグレードガイドは次のページで公開されています。

- [To v5 from v4 | webpack](https://webpack.js.org/migrate/5/)

また、[webpack CLI](https://github.com/webpack/webpack-cli) 4.0.0もリリースされています。

- <https://github.com/webpack/webpack-cli/blob/master/CHANGELOG.md#400-2020-10-10>

webpack 5に対応、[Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)を実行する`--analyze`フラグの追加、`--env`フラグの追加、`init`コマンドの追加などが行われています。

webpack 5のオプションそれぞれに対応したCLIのフラグが追加されています。

- [webpack-cli](https://github.com/webpack/webpack-cli/tree/master/packages/webpack-cli)

----

Browserify 17.0.0がリリースされました。

- [Release v17.0.0 · browserify/browserify](https://github.com/browserify/browserify/releases/tag/v17.0.0)

shimライブラリの`events`、`path`、`stream`、`util`をNode.js 10+互換となるようにアップデートされています。
また`.json`ファイルをrequireする際に、JSONかどうかのバリデーションを行うように修正されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v12.19.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.19.0/](https://nodejs.org/en/blog/release/v12.19.0/ "Node v12.19.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v12.19.0リリース。
`import`フィールドのサポート、cryptoモジュールに`randomInt`関数の追加。
`module.parent`の非推奨化など


----

## New in Chrome 86  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/10/nic86](https://developers.google.com/web/updates/2020/10/nic86 "New in Chrome 86  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 86リリース。
File System Access API、CSS 擬似クラスの`:focus-visible`、Document-Policyヘッダなどのサポート。
Origin TrialとしてWebHID API、Multi-Screen Window Placement APIなどのサポート。
Web Components v0の削除、FTPサポートの非推奨化。


----

## Release v9.5.4 · vercel/next.js
[github.com/vercel/next.js/releases/tag/v9.5.4](https://github.com/vercel/next.js/releases/tag/v9.5.4 "Release v9.5.4 · vercel/next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 9.5.4リリース。
オープンリダイレクト脆弱性のセキュリティ修正


----

## Release Notes for Safari Technology Preview 114 | WebKit
[webkit.org/blog/11300/release-notes-for-safari-technology-preview-114/](https://webkit.org/blog/11300/release-notes-for-safari-technology-preview-114/ "Release Notes for Safari Technology Preview 114 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 114リリース。
`Intl.DateTimeFormat`の`dateStyle`/`timeStyle`/`dayPeriod`のサポート、`Intl.Segmenter`のサポート。
Paint Timingの有効化、WebGL2の有効化、`loading=lazy`の実装など


----

## Release v17.0.0 · browserify/browserify
[github.com/browserify/browserify/releases/tag/v17.0.0](https://github.com/browserify/browserify/releases/tag/v17.0.0 "Release v17.0.0 · browserify/browserify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 17.0.0リリース。
shimライブラリの`events`、`path`、`stream`、`util`をNode.js 10+互換となるようにアップデート。
`.json`ファイルのrequire時にJSONのバリデーションを行うように


----

## Webpack 5 release (2020-10-10) | webpack
[webpack.js.org/blog/2020-10-10-webpack-5-release/](https://webpack.js.org/blog/2020-10-10-webpack-5-release/ "Webpack 5 release (2020-10-10) | webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5リリース。
破壊的な変更として、自動的なNode.jsのpolyfillの削除、デフォルトの出力コードにES2015が含まれるように、非推奨のオプションの削除やオプション名の変更など。
機能追加として、filesystem cache、Asset modules、JSON Modules、`import.meta`、Worker script、Module Federation、Async modulesのサポート。
また、`target`オプションが`browserslist`をサポート、CommonJSのTree Shakingをサポート、コード生成とTree Shakingの改善など

- [To v5 from v4 | webpack](https://webpack.js.org/migrate/5/ "To v5 from v4 | webpack")
- [webpack@5の主な変更点まとめ - 技術探し](https://blog.hiroppy.me/entry/webpack5 "webpack@5の主な変更点まとめ - 技術探し")

----

## webpack-cli/CHANGELOG.md at master · webpack/webpack-cli
[github.com/webpack/webpack-cli/blob/master/CHANGELOG.md#400-2020-10-10](https://github.com/webpack/webpack-cli/blob/master/CHANGELOG.md#400-2020-10-10 "webpack-cli/CHANGELOG.md at master · webpack/webpack-cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

webpack-cli 4.0.0リリース。
webpack 5に対応、Webpack Bundle Analyzerを実行する`--analyze`フラグの追加、`--env`フラグの追加、`init`コマンドの追加など

- [webpack-cli/packages/webpack-cli at master · webpack/webpack-cli](https://github.com/webpack/webpack-cli/tree/master/packages/webpack-cli "webpack-cli/packages/webpack-cli at master · webpack/webpack-cli")
- [webpack-contrib/webpack-bundle-analyzer: Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap](https://github.com/webpack-contrib/webpack-bundle-analyzer "webpack-contrib/webpack-bundle-analyzer: Webpack plugin and CLI utility that represents bundle content as convenient interactive zoomable treemap")

----

## Release v5.9.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v5.9.0](https://github.com/pnpm/pnpm/releases/tag/v5.9.0 "Release v5.9.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 5.9.0リリース。
YarnのPlug'n'Playをサポート、`symlink`を無効化できる設定の追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Gaining security and privacy by partitioning the cache  |  Web
[developers.google.com/web/updates/2020/10/http-cache-partitioning](https://developers.google.com/web/updates/2020/10/http-cache-partitioning "Gaining security and privacy by partitioning the cache  |  Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">article</span></p>

Chrome 86でのCache partitioningについて。
今まではアクセスするリソースのURLのみでCache Keyを構成していたが、今後はアクセス元のサイトなどもCache Keyに利用されるという話。
アクセス元のサイトとアクセスするリソースのURLのDouble-keying、アクセス元のサイトとiframeのサイトとアクセスするリソースのURLのTriple-keyingのキャッシュについて

- [shivanigithub/http-cache-partitioning](https://github.com/shivanigithub/http-cache-partitioning/ "shivanigithub/http-cache-partitioning")

----

## Bringing the browser developer tools to Visual Studio Code - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2020/10/01/microsoft-edge-tools-vscode/](https://blogs.windows.com/msedgedev/2020/10/01/microsoft-edge-tools-vscode/ "Bringing the browser developer tools to Visual Studio Code - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">plugin</span></p>

Microsoft Edge Tools for VS Code extensionリリース。
VSCode内でMSEdgeを使ったプレビュー、デバッグができる。
ヘッドレスモードの対応、Networkパネルの対応などをしている


----

## Understanding TypeScript Generics — Smashing Magazine
[www.smashingmagazine.com/2020/10/understanding-typescript-generics/](https://www.smashingmagazine.com/2020/10/understanding-typescript-generics/ "Understanding TypeScript Generics — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

TypeScriptのGenericsについての記事。
Genericsの使い方、ユースケースについて


----

## Using WebXR With Babylon.js — Smashing Magazine
[www.smashingmagazine.com/2020/10/using-webxr-with-babylonjs/](https://www.smashingmagazine.com/2020/10/using-webxr-with-babylonjs/ "Using WebXR With Babylon.js — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebXR</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

WebXRについてのチュートリアル。
WebXR、3DoF、6DoFの解説。
babylon.jsを使ったWebXRのシーンの作成、デバッグ方法について


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## doc22940/browserslist-user-agent-regexp
[github.com/doc22940/browserslist-user-agent-regexp](https://github.com/doc22940/browserslist-user-agent-regexp "doc22940/browserslist-user-agent-regexp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

`browserslist`の定義からサポートするブラウザのUser Agentにマッチする正規表現を出力するツール


----

## boa-dev/boa: Boa is an embeddable and experimental Javascript engine written in Rust. Currently, it has support for some of the language.
[github.com/boa-dev/boa](https://github.com/boa-dev/boa "boa-dev/boa: Boa is an embeddable and experimental Javascript engine written in Rust. Currently, it has support for some of the language.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">library</span></p>

Rustで書かれたJavaScriptエンジン。
Rustのプロジェクトに組み込んだり、JavaScriptインタープリタをWebAssemblyとして動かすことができる


----

## awslabs/diagram-maker: A library to display an interactive editor for any graph-like data.
[github.com/awslabs/diagram-maker](https://github.com/awslabs/diagram-maker "awslabs/diagram-maker: A library to display an interactive editor for any graph-like data.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">JavaScript</span></p>

AWSのダイアグラムエディタ。
ライブラリとして利用でき、プラグインで拡張可能になっていて、UIはPreactとReduxを使って書かれている。

- [Diagram Maker: Open sourcing IoT visualization | AWS Open Source Blog](https://aws.amazon.com/jp/blogs/opensource/diagram-maker-open-sourcing-iot-visualization/ "Diagram Maker: Open sourcing IoT visualization | AWS Open Source Blog")

----

## tuananh/camaro: camaro is an utility to transform XML to JSON, using Node.js binding to native XML parser pugixml, one of the fastest XML parser around.
[github.com/tuananh/camaro](https://github.com/tuananh/camaro "tuananh/camaro: camaro is an utility to transform XML to JSON, using Node.js binding to native XML parser pugixml, one of the fastest XML parser around.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">XML</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span> <span class="jser-tag">WebAssembly</span></p>

XMLをJSONに変換するライブラリ。
C++で書かれていてWebAssemblyにコンパイルしたものを利用するライブラリ


----

## RDambrosio016/RSLint: A (WIP) Extremely fast JavaScript linter and Rust crate
[github.com/RDambrosio016/RSLint](https://github.com/RDambrosio016/RSLint "RDambrosio016/RSLint: A (WIP) Extremely fast JavaScript linter and Rust crate")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">eslinn</span></p>

Rustで書かれたJavaScript Lintツール。


----

## RocktimSaikia/meta-fetcher: 🔎 Tiny URL meta-data fetcher(scrapper) for Node.js
[github.com/RocktimSaikia/meta-fetcher](https://github.com/RocktimSaikia/meta-fetcher "RocktimSaikia/meta-fetcher: 🔎 Tiny URL meta-data fetcher(scrapper) for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

ウェブサイトのメタ情報を取得するすnode-fetchベースのスクレイピングライブラリ


----

## mljs/ml: Machine learning tools in JavaScript
[github.com/mljs/ml](https://github.com/mljs/ml "mljs/ml: Machine learning tools in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

機械学習向けのツールを集めたライブラリ


----

## Schniz/fnm: 🚀 Fast and simple Node.js version manager, built in Rust
[github.com/Schniz/fnm](https://github.com/Schniz/fnm "Schniz/fnm: 🚀 Fast and simple Node.js version manager, built in Rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Rust</span></p>

Rustで書かれたNode.jsのバージョン管理ツール。


----
