---
title: "2020-09-08のJS: Chrome 86ベータ、Underscore 1.11.0(ESM)、JavaScript Primer v2"
author: "azu"
layout: post
date : 2020-09-08T03:28:31.282Z
category: JSer
tags:
- Chrome
- Underscore
- book

---

JSer.info #504 - Chrome 86ベータがリリースされました。

- [Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More](https://blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html)

CSS 擬似クラスの`:focus-visible`、擬似要素の`::marker`をサポートされています。
Document Policy、`FetchEvent.handled`、Shadow DOM Distribution API、`ParentNode.replaceChildren()`のサポートなどのサポートも追加されています。
また、Origin TrialとしてWebHID API、Window placement API、`<meta name="battery-savings">`などの試験的に利用できるようになっています。

その他にはFTPのサポートの段階的な廃止が導入されていて、Chrome 86ではFTPが非推奨となりました。
Chrome 87でデフォルトで無効となり、Chrome 88でコードベースから削除される予定です。

- [Deprecate FTP support - Chrome Platform Status](https://www.chromestatus.com/feature/6246151319715840)

----

Underscore 1.11.0がリリースされています。

- [Underscore.js 1.11.0](https://underscorejs.org/#1.11.0)

このリリースでは、ECMAScript Modules(ESM)に対応した形式でパッケージを公開する変更が含まれています。この変更のために、Underscoreのコードベースがそれぞれの関数ごとにモジュール化されています。

また、この変更行った[Julian Gonggrijp](https://github.com/jgonggrijp)によるUndescoreのモジュール版の利用方法について解説記事が公開されています。

- [Introducing Modular Underscore—Julian Gonggrijp](https://juliangonggrijp.com/article/introducing-modular-underscore.html)

記事では、既存(モノリシック)の使い方とES Modulesの使い方、ビルドサイズの最適化、Underscore 2.0などについて書かれています。

----

JavaScriptの入門書である[JavaScript Primer](https://jsprimer.net/) 2.0がリリースされました。

- [Release 2.0.0: ECMAScript 2020対応 · asciidwango/js-primer](https://github.com/asciidwango/js-primer/releases/tag/v2.0.0)
- [JavaScript Primer 2.0 - ECMAScript 2020に対応した入門書を公開しました | Web Scratch](https://efcl.info/2020/09/01/jsprimer-2.0/)

JavaScript Primer 2.0では、ES2020で追加された`String.prototype.matchAll`、`globalThis`、BigInt、Nullish coalescing(`??`)、Optional chainin（`?.`）に対応した変更が含まれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 13.7.0 · stylelint/stylelint
[github.com/stylelint/stylelint/releases/tag/13.7.0](https://github.com/stylelint/stylelint/releases/tag/13.7.0 "Release 13.7.0 · stylelint/stylelint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

stylelint 13.7.0リリース。
`*-blacklist`、`*-requirelist`, `*-whitelist`を非推奨化し、` *-disallowed-list`, `*-required-list`にリネーム。
`stylelint-disable`コメントに説明を書けるように


----

## ESLint v7.8.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/08/eslint-v7.8.0-released](https://eslint.org/blog/2020/08/eslint-v7.8.0-released "ESLint v7.8.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 7.8.0リリース。
`ecmaScript`オプションが`2021`に対応しLogical assignment operators、numeric separatorsに対応。


----

## Release v4.0.0 · typescript-eslint/typescript-eslint
[github.com/typescript-eslint/typescript-eslint/releases/tag/v4.0.0](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v4.0.0 "Release v4.0.0 · typescript-eslint/typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript-ESLint 4.0.0リリース。
Optional ChainingとdecoratorsのASTを変更、Scope解析を改善して`no-unused-vars`などのルールを改善、`ban-ts-comment`のデフォルト値を変更など。
またTypeScript 4.0にはTypeScript-ESLint 3.10.0で対応している。


----

## webpack 5 release plan · Issue #11406 · webpack/webpack
[github.com/webpack/webpack/issues/11406](https://github.com/webpack/webpack/issues/11406 "webpack 5 release plan · Issue #11406 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">news</span> <span class="jser-tag">issue</span></p>

webpack 5リリースまで予定について。
webpack 5は2020年10月10日リリース予定で、RCは9月にリリースする予定。
細かいバグはwebpack 5リリース後に修正する予定とのこと。


----

## Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More
[blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html](https://blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html "Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 86ベータリリース。
CSS 擬似クラスの`:focus-visible`、擬似要素の`::marker`をサポート。
Document Policy、`FetchEvent.handled`、Shadow DOM Distribution API、`ParentNode.replaceChildren()`のサポートなど。
またOrigin TrialとしてWebHID API、Window placement API、`<meta name="battery-savings">`などのサポート。
その他にはFTPのサポートが非推奨となるなど

- [window-placement/EXPLAINER.md at master · webscreens/window-placement](https://github.com/webscreens/window-placement/blob/master/EXPLAINER.md "window-placement/EXPLAINER.md at master · webscreens/window-placement")
- [battery-savings/explainer.md at master · chrishtr/battery-savings](https://github.com/chrishtr/battery-savings/blob/master/explainer.md "battery-savings/explainer.md at master · chrishtr/battery-savings")

----

## Underscore.js
[underscorejs.org/#1.11.0](https://underscorejs.org/#1.11.0 "Underscore.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

underscore 1.10.0リリース。
それぞれの関数を個別のES Modulesにし、ES Modulesのエントリーポイントとして`underscore-esm.js`を追加。
`_.isArrayBuffer`、`_.isDataView`、`_.isTypedArray`の追加、`_.flatten`がdepthを指定する第2引数をサポートなど


----

## Update on Adobe Flash Player End of Support - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2020/09/04/update-adobe-flash-end-support/](https://blogs.windows.com/msedgedev/2020/09/04/update-adobe-flash-end-support/ "Update on Adobe Flash Player End of Support - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">flash</span> <span class="jser-tag">news</span></p>

MSEdgeではFlash Playerを2021年1月のEdge 88で削除する予定。
この削除スケジュールはChromiumにあわせたもの

- [Flash Roadmap - The Chromium Projects](https://www.chromium.org/flash-roadmap#TOC-Flash-Support-Removed-from-Chromium-Target:-Chrome-88---Jan-2021- "Flash Roadmap - The Chromium Projects")

----
<h1 class="site-genre">アーティクル</h1>

----

## Minimal React: getting started with the frontend library
[2ality.com/2020/08/minimal-react.html](https://2ality.com/2020/08/minimal-react.html "Minimal React: getting started with the frontend library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

snowpack、react、htm、immerを使ったReactのチュートリアル


----

## Introducing: Modern Web
[modern-web.dev/blog/introducing-modern-web/](https://modern-web.dev/blog/introducing-modern-web/ "Introducing: Modern Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span> <span class="jser-tag">testing</span></p>

ウェブ開発の汎用ツールとガイドに取り組むModern Webというプロジェクトについて。
まずはWeb Test Runnerというブラウザを使ったテストツールをリリースしている。
今後Web Dev Serverのような開発用サーバや開発ガイドなどに取り組んでいく予定とのこと

- [modernweb-dev/web: Guides, tools and libraries for modern web development.](https://github.com/modernweb-dev/web "modernweb-dev/web: Guides, tools and libraries for modern web development.")

----

## Introducing Modular Underscore—Julian Gonggrijp
[juliangonggrijp.com/article/introducing-modular-underscore.html](https://juliangonggrijp.com/article/introducing-modular-underscore.html "Introducing Modular Underscore—Julian Gonggrijp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

underscore 1.11.0でのES Modulesへの移行とその利用方法についての記事。
既存(モノリシック)の使い方とES Modulesの使い方、ビルドサイズの最適化、Underscore 2.0についてなど


----

## Browsers may throttle requestAnimationFrame
[mattperry.is/writing-code/browsers-may-throttle-requestanimationframe-to-30fps](https://mattperry.is/writing-code/browsers-may-throttle-requestanimationframe-to-30fps "Browsers may throttle requestAnimationFrame")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">article</span></p>

`requestAnimationFrame`のフレームレートがブラウザによって抑制される条件について。
iOSのlow-power mode、Safariのcross-origin iframesの条件下では抑制される点について。
また、Firefoxにおいて`performance.now()`の精度の抑制されていることとcross-origin isolateについて。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## andnp/SimplyTyped: yet another Typescript type library for advanced types
[github.com/andnp/SimplyTyped](https://github.com/andnp/SimplyTyped "andnp/SimplyTyped: yet another Typescript type library for advanced types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScriptの型ユーティリティライブラリ。
型定義の補助やランタイムでの補助関数などを提供する


----

## mizchi/minlink: Minimum(> 1kb) and isomorphic worker wrapper with comlink like rpc.
[github.com/mizchi/minlink](https://github.com/mizchi/minlink "mizchi/minlink: Minimum(> 1kb) and isomorphic worker wrapper with comlink like rpc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Web Worker/Node.jsの`worker_thread`でRPCをするためのライブラリ。
comlinkのように関数呼び出しで`postMessage`のやりとりをする

- [minlink - browser/node で使える Worker ラッパー - mizdev](https://mizchi.dev/202009061729-minlink-and-minify-tech "minlink - browser/node で使える Worker ラッパー - mizdev")

----
<h1 class="site-genre">書籍関係</h1>

----

## この書籍について · JavaScript Plugin Architecture
[azu.github.io/JavaScript-Plugin-Architecture/](https://azu.github.io/JavaScript-Plugin-Architecture/ "この書籍について · JavaScript Plugin Architecture")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">plugin</span> <span class="jser-tag">book</span></p>

JavaScriptのプラグインアーキテクチャについて扱う小さな書籍。
jQuery、ESLint、Connect、gulp、Reduxのプラグインの仕組みを実装しながら紹介している。

- [Release v2.0.0 · azu/JavaScript-Plugin-Architecture](https://github.com/azu/JavaScript-Plugin-Architecture/releases/tag/v2.0.0 "Release v2.0.0 · azu/JavaScript-Plugin-Architecture")

----

## Release 2.0.0: ECMAScript 2020対応 · asciidwango/js-primer
[github.com/asciidwango/js-primer/releases/tag/v2.0.0](https://github.com/asciidwango/js-primer/releases/tag/v2.0.0 "Release 2.0.0: ECMAScript 2020対応 · asciidwango/js-primer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript入門書のJavaScript Primer 2.0.0リリース。
ES2020の`String.prototype.matchAll`、`globalThis`、BigInt、Nullish coalescing(`??`)、Optional chainin（`?.`）に対応など

- [JavaScript Primer 2.0 - ECMAScript 2020に対応した入門書を公開しました | Web Scratch](https://efcl.info/2020/09/01/jsprimer-2.0/ "JavaScript Primer 2.0 - ECMAScript 2020に対応した入門書を公開しました | Web Scratch")

----
