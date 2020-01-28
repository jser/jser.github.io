---
title: "2020-01-27のJS: Safari TP 99(Remove Flash)、AVA 3.1.0(TypeScript) playwright"
author: "azu"
layout: post
date : 2020-01-27T14:40:00.229Z
category: JSer
tags:
- safari
- node
- puppeteer

---

JSer.info #472 - Safari Technology Preview 99リリース。

- [Release Notes for Safari Technology Preview 99 | WebKit](https://webkit.org/blog/9992/release-notes-for-safari-technology-preview-99/)

Safari Technology Preview 99ではAdobe Flashのサポートが削除されています。
また、今までは`-webkit-` prefixがついていましたが、CSSの[image-set()](https://developer.mozilla.org/ja/docs/Web/CSS/image-set)構文がサポートされました。

----

AVA 3.1.0がリリースされました。

- [Release 3.1.0 · avajs/ava](https://github.com/avajs/ava/releases/tag/v3.1.0)

TypeScriptをサポートするために[@ava/typescript](https://github.com/avajs/typescript)というパッケージが追加されています。
仕組み的には、内部的にTypeScriptファイルをコンパイルするのではなく、コンパイル済みのファイルを読み込むようにパスを変更する仕組み的になっています。

----

Puppeteerのクラスブラウザ版を目指すplaywrightが公開されています。

- [microsoft/playwright: Node library to automate Chromium, Firefox and WebKit with a single API](https://github.com/microsoft/playwright)

基本的にはPuppeteerをベースにしていて、ChromiumだけではなくWebKitとFirefoxもサポートしています。
類似するものとしてはWebDriverですが、WebDriverよりも機能的なDriver、分かりやすいAPI、setTimeout-freeな自動化ができることを目的にしています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 🎉 HTM 3 is here! · developit/htm
[github.com/developit/htm/releases/tag/3.0.0](https://github.com/developit/htm/releases/tag/3.0.0 "Release 🎉 HTM 3 is here! · developit/htm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

HTM 3リリース。
StaticなTreeを判別してキャッシュ出来るように、Preact Xに対応、`babel-plugin-htm`に自動importのオプションを追加など


----

## Node v13.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v13.7.0/](https://nodejs.org/en/blog/release/v13.7.0/ "Node v13.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">sourcemap</span></p>

Node v13.7.0リリース。
`module`モジュールにSource Mapを扱うAPIを追加、`process`に`uncaughtExceptionMonitor`リスナーの追加など


----

## Release Notes for Safari Technology Preview 99 | WebKit
[webkit.org/blog/9992/release-notes-for-safari-technology-preview-99/](https://webkit.org/blog/9992/release-notes-for-safari-technology-preview-99/ "Release Notes for Safari Technology Preview 99 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 99リリース。
Flashのサポートを削除、CSSの`image-set()`をサポートなど


----

## ResizeObserver in WebKit | WebKit
[webkit.org/blog/9997/resizeobserver-in-webkit/](https://webkit.org/blog/9997/resizeobserver-in-webkit/ "ResizeObserver in WebKit | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebPlatformAPI</span></p>

Safari Technology Preview 80で実装されたResizeObserverについて。
ResizeObserverによる要素に対するリサイズの監視などの使い方、イベントが発生する流れについての解説、利用例などについて

- [Release Notes for Safari Technology Preview 80 | WebKit](https://webkit.org/blog/8825/release-notes-for-safari-technology-preview-80/ "Release Notes for Safari Technology Preview 80 | WebKit")

----

## Release v4.8.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v4.8.0](https://github.com/pnpm/pnpm/releases/tag/v4.8.0 "Release v4.8.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

パッケージ管理ツールのpnpm 4.8.0リリース。
モジュールのインタラクティブアップデートを行う`pnpm update --interactive`の追加など


----

## Release v1.30.0 · rollup/rollup
[github.com/rollup/rollup/releases/tag/v1.30.0](https://github.com/rollup/rollup/releases/tag/v1.30.0 "Release v1.30.0 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup 1.30.0リリース。
dynamic importsのsplit chunksのロジックの改善。
Code Splitting時にentry chunksで空importを行う最適化のためをON/OFFできるようにする`hoistTransitiveImports`オプションの追加など


----

## Release 3.1.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.1.0](https://github.com/avajs/ava/releases/tag/v3.1.0 "Release 3.1.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3.1.0リリース。
`@ava/typescript`パッケージでTypeScriptサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Debug z-index stacking content with 3D View in the Microsoft Edge DevTools - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2020/01/23/debug-z-index-3d-view-edge-devtools/](https://blogs.windows.com/msedgedev/2020/01/23/debug-z-index-3d-view-edge-devtools/ "Debug z-index stacking content with 3D View in the Microsoft Edge DevTools - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">debug</span></p>

MSEdgeの開発者ツールに、`z-index`のスタックコンテキストをビジュアライズする3D Views機能が実験的に実装された


----

## 💡🎁 JavaScript Visualized: Generators and Iterators - DEV Community 👩‍💻👨‍💻
[dev.to/lydiahallie/javascript-visualized-generators-and-iterators-e36](https://dev.to/lydiahallie/javascript-visualized-generators-and-iterators-e36 "💡🎁 JavaScript Visualized: Generators and Iterators - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Generators、Iteratorsの動きをコードとコンソールの表示をあわせて見られるようにして解説している記事


----

## Replacing Mocha with Jest
[akoskm.com/2020/01/22/mocha-jest-react-testing.html](https://akoskm.com/2020/01/22/mocha-jest-react-testing.html "Replacing Mocha with Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

MochaからJestへのマイグレーション方法について。
Mochaの機能のJestでの代用方法について紹介されている。


----

## Inside node: What happens when we execute a script?
[blog.s1h.org/inside-node-executing-a-script/](https://blog.s1h.org/inside-node-executing-a-script/ "Inside node: What happens when we execute a script?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">article</span></p>

Node.jsでスクリプトを実行するまでにどのような処理が行われているのかをコードから見ていく記事。
`node`のコマンドライン引数の処理、ファイルのロード、`module`でのスクリプトをのコンパイル、libuvを使ったイベントループでのコード実行の流れについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## microsoft/playwright: Node library to automate Chromium, Firefox and WebKit browsers
[github.com/microsoft/playwright](https://github.com/microsoft/playwright "microsoft/playwright: Node library to automate Chromium, Firefox and WebKit browsers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">Firefox</span> <span class="jser-tag">webkit</span> <span class="jser-tag">library</span> <span class="jser-tag">Selenium</span> <span class="jser-tag">webdriver</span></p>

Chromium、WebKit、Firefoxを操作できるNode.jsライブラリ。
Puppeteerと同じチームが開発していて、クロスブラウザ向けの抽象化されたAPIを提供する目的。
WebDriverよりも機能的なDriver、分かりやすいAPI、setTimeout-freeな自動化を目的としている


----

## Puppeteer Sandbox | Headless Chrome Playground
[puppeteersandbox.com/](https://puppeteersandbox.com/ "Puppeteer Sandbox | Headless Chrome Playground")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">Tools</span></p>

ブラウザからPuppeteerを扱うコードを書いて実行結果を取得できるSandboxツール


----

## All questions | TypeOfNaN JavaScript Quizzes
[quiz.typeofnan.dev/](https://quiz.typeofnan.dev/ "All questions | TypeOfNaN JavaScript Quizzes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webservice</span></p>

JavaScriptに関するクイズサイト。
JavaScriptについてのクイズとその解説が掲載されている


----
