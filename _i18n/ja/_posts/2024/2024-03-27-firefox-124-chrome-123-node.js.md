---
title: "2024-03-27のJS: Firefox 124、Chrome 123、Node.jsドキュメンタリー"
author: "azu"
layout: post
date: 2024-03-27T02:56:05.492Z
category: JSer
tags:
- nodejs
- Tools
- Chrome
- document
- rspack

---

JSer.info #686 - Firefox 124がリリースされました。

- [Firefox 124.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/124.0/releasenotes/)
- [Firefox 124 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/124)

 `AbortSignal.any()`のサポート、WebDriver BiDiの対応改善が含まれています。
また、フラグ付きで`SharedArrayBuffer.prototype.grow()`と` ArrayBuffer.prototype.resize()`のサポートなども行われています。


---

Chrome 123がリリースされました。

- [New in Chrome 123  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-123?hl=en)

CSSの`light-dark()`のサポート、Service worker Static Routing APIのサポート、Content-Encoding: zstdをサポートなどが含まれています。
また、BFCacheが利用できなかった理由を取得できる`notRestoredReasons`のサポート、ES Proposal Stage 3のImport Attributesをサポートなども行われています。

---

Node.jsのドキュメンタリー動画が公開されています。

- [Node.js: The Documentary | An origin story - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

Node.jsの誕生からRyan→Isaac→TJへのオーナーの移譲、Joyentでの停滞、io.jsのForkからの統合、Node.js Foundationの設立までの話をまとめた動画になっています。

同じタイミングで、Node.jsのウェブサイトがNext.jsでリデザインされたことが発表されています。

- [Node.js — Diving into the Node.js Website Redesign](https://nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign)

Node.jsの作者でもありDenoの作者でもあるRyan Dahl氏が、[X](https://twitter.com/rough__sea)に復帰したり、次のPodcastでは[JSR: the JavaScript Registry](https://jsr.io/)について話されています。

- [Why the creator of Node.js® created a new JavaScript runtime - Stack Overflow](https://stackoverflow.blog/2024/03/19/why-the-creator-of-node-js-r-created-a-new-javascript-runtime/)

また、2代目のNode.jsのオーナーでもあるIsaacが、JavaScriptパッケージマネージャーの開発を行う[vlt](https://www.vlt.sh/)に参加したことも発表されています。

- [Introducing our team, investors & more...](https://blog.vlt.sh/blog/the-team)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Rsbuild v0.5 - Rsbuild
[rsbuild.dev/community/releases/v0-5](https://rsbuild.dev/community/releases/v0-5 "Announcing Rsbuild v0.5 - Rsbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rsbuild v0.5リリース。
Lightning CSSをopt-inでサポート、Custom Serverをサポート、SVGRプラグインの改善など


----

## Firefox 124.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/124.0/releasenotes/](https://www.mozilla.org/en-US/firefox/124.0/releasenotes/ "Firefox 124.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 124リリース。
 `AbortSignal.any()`のサポート、WebDriver BiDiの対応改善。
フラグ付きで`SharedArrayBuffer.prototype.grow()`と` ArrayBuffer.prototype.resize()`のサポートなど

- [Firefox 124 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/124 "Firefox 124 for developers - Mozilla | MDN")

----

## Announcing VitePress 1.0 | The Vue Point
[blog.vuejs.org/posts/vitepress-1.0](https://blog.vuejs.org/posts/vitepress-1.0 "Announcing VitePress 1.0 | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

VitePress 1.0リリース


----

## New in Chrome 123  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-123?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-123?hl=en "New in Chrome 123  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 123リリース。
CSSの`light-dark()`のサポート、
Service worker Static Routing APIのサポート、Content-Encoding: zstdをサポート。
BFCacheが利用できなかった理由を取得できる`notRestoredReasons`のサポート、ES Proposal Stage 3のImport Attributesをサポートなど


----

## Node.js — Node v18.20.0 (LTS)
[nodejs.org/en/blog/release/v18.20.0](https://nodejs.org/en/blog/release/v18.20.0 "Node.js — Node v18.20.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.20.0リリース。
Import Attributesのサポート、`vm.Script`とDynamic Importに関するパフォーマンス改善をbackport(Jestでメモリリークする問題の改善)


----

## Node.js — Node v20.12.0 (LTS)
[nodejs.org/en/blog/release/v20.12.0](https://nodejs.org/en/blog/release/v20.12.0 "Node.js — Node v20.12.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.12.0リリース。
`crypto.hash()`の追加、`.env`を扱う`process.loadEnvFile(path)`と`util.parseEnv(content)`を追加。
`net.createConnection`に接続試行に関するイベントを追加、`util.styleText(format, text)`を追加など


----

## Release v10.4.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v10.4.0](https://github.com/mochajs/mocha/releases/tag/v10.4.0 "Release v10.4.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha v10.4.0リリース。
Error Causeの表示に対応


----

## Release v9.0.0-beta.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v9.0.0-beta.0](https://github.com/pnpm/pnpm/releases/tag/v9.0.0-beta.0 "Release v9.0.0-beta.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v9.0.0-beta.0リリース。
Node.js 16のサポート終了、Lockfileバージョンをv7に変更、`dedupe-injected-deps`を`true`に変更、`link-workspace-packages`を`false`に変更。
pre/post-scriptを実行する`enable-pre-post-scripts`を`true`に変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Optimizing Javascript for fun and for profit
[romgrk.com/posts/optimizing-javascript](https://romgrk.com/posts/optimizing-javascript "Optimizing Javascript for fun and for profit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span></p>

JavaScriptのパフォーマンスの最適化について。パフォーマンスと可読性のトレードオフ。
文字列の比較を避ける、異なる形状を避ける、配列やオブジェクトのメソッドを避けるといった実行時のコストを減らす工夫について


----

## Performance tooling in 2024 and beyond  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/perf-tooling-2024](https://developer.chrome.com/blog/perf-tooling-2024 "Performance tooling in 2024 and beyond  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Chrome DevToolsに試験的に実装されていた"Performance Insights"パネルは2024年後半に削除される予定。
"Performance Insights"は情報密度を減らすことを目的にしていたが、"Performance"パネルの方が使われていたという話


----

## Node.js — Diving into the Node.js Website Redesign
[nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign](https://nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign "Node.js — Diving into the Node.js Website Redesign")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.jsのウェブサイトがNext.jsで新しく書き直された話。
nextraでの静的サイトとして始めたがカスタム設定が多くなり、Next.jsをVercelで動かす形に変更した。
このリニューアルで既存の翻訳はリセットされたため、現時点では404となっており、今後Crowdinを使った翻訳の仕組みを導入予定。

- [Node.js — Run JavaScript Everywhere](https://nodejs.org/en "Node.js — Run JavaScript Everywhere")

----

## Flow Nodes: How Type Inference Is Implemented
[effectivetypescript.com/2024/03/24/flownodes/](https://effectivetypescript.com/2024/03/24/flownodes/ "Flow Nodes: How Type Inference Is Implemented")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptのnarrowingがどのように動作しているかについて。
上から下に型を絞り込んでいるのではなく、シンボルが参照されてるポイントから制御フローグラフを逆にたどることで型を絞り込む実装になっている話


----

## Chrome で text-spacing-trim プロパティがサポートされたぞ！！
[zenn.dev/inaniwaudon/articles/3ff8761773178c](https://zenn.dev/inaniwaudon/articles/3ff8761773178c "Chrome で text-spacing-trim プロパティがサポートされたぞ！！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chrome 123でサポートされたCSSのtext-spacing-trimプロパティについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Node.js: The Documentary | An origin story - YouTube
[www.youtube.com/watch?v&#x3D;LB8KwiiUGy0](https://www.youtube.com/watch?v=LB8KwiiUGy0 "Node.js: The Documentary | An origin story - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">history</span> <span class="jser-tag">video</span></p>

Node.jsについてのドキュメンタリー動画。
Node.jsが作成された理由や初期の開発、Windowの対応とlibuv。
Ryan→Isaac→TJへのオーナーの移譲、Joyentでの停滞とio.jsのfork、io.jsとNode.jsがマージされるまでの話


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Runtime compatibility across JavaScript runtimes
[runtime-compat.unjs.io/](https://runtime-compat.unjs.io/ "Runtime compatibility across JavaScript runtimes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

Bun/Deno/Vercel/LLRT/Node.js/wasmer/workerdなどのJavaScript RuntimeのWinterCG API互換性をまとめたテーブル


----

## Rsdoctor
[rsdoctor.dev/](https://rsdoctor.dev/ "Rsdoctor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">rspack</span> <span class="jser-tag">Tools</span></p>

webpackやRspackのbundle結果を分析できるツール。
bunde結果のサマリ、コンパイル/minifyの時間、loaderごとの処理時間やタイムライン、モジュールの依存関係の分析など


----
