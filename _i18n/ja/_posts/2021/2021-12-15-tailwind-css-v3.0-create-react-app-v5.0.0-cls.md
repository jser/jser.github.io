---
title: "2021-12-15のJS: Tailwind CSS v3.0、create-react-app v5.0.0、CLSの改善"
author: "azu"
layout: post
date : 2021-12-15T00:08:41.159Z
category: JSer
tags:
- node.js
- CSS
- safari
- Tools
- DOM

---

JSer.info #570 - - [Tailwind CSS v3.0 – Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v3)

----

- [Release v5.0.0 · facebook/create-react-app](https://github.com/facebook/create-react-app/releases/tag/v5.0.0)

----


- [Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd)
- [Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-2-2a846adeb097)
- [Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-3-3a36240861e4)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Tailwind CSS v3.0 – Tailwind CSS
[tailwindcss.com/blog/tailwindcss-v3](https://tailwindcss.com/blog/tailwindcss-v3 "Tailwind CSS v3.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS v3.0リリース。
Just-in-Time Modeのエンジンを刷新、Box Shadow Colorの追加、CSS Scroll Snapのサポート、Multi-column layoutのサポートなど。


----

## Release 13.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v13.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v13.0.0 "Release 13.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 13.0.0リリース。
`already-handled`のtypoを修正


----

## Release Notes for Safari Technology Preview 136 | WebKit
[webkit.org/blog/12137/release-notes-for-safari-technology-preview-136/](https://webkit.org/blog/12137/release-notes-for-safari-technology-preview-136/ "Release Notes for Safari Technology Preview 136 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">WebExtension</span></p>

Safari Technology Preview 136リリース。
`contain: paint`、`revert-layer`、`flex-basis: content`のサポート。
`Temporal.Instant`の実装、WebExtensionのManigest V3をサポートなど


----

## GitHub Actions: GitHub-hosted runners now run Node.js 16 by default | GitHub Changelog
[github.blog/changelog/2021-12-10-github-actions-github-hosted-runners-now-run-node-js-16-by-default/](https://github.blog/changelog/2021-12-10-github-actions-github-hosted-runners-now-run-node-js-16-by-default/ "GitHub Actions: GitHub-hosted runners now run Node.js 16 by default | GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

GitHub ActionsのNode.jsのデフォルトがNode.js 16に変更


----

## Release v5.0.0 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v5.0.0](https://github.com/facebook/create-react-app/releases/tag/v5.0.0 "Release v5.0.0 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app v5.0.0リリース。
webpack 5、Jest 27、ESLint 8、PostCSS 8へのアップデート。
tailwind.config.jsのサポート、依存のバージョン固定を削除、Node 10と12のサポート終了など


----

## New WebKit Features in Safari 15.2 | WebKit
[webkit.org/blog/12140/new-webkit-features-in-safari-15-2/](https://webkit.org/blog/12140/new-webkit-features-in-safari-15-2/ "New WebKit Features in Safari 15.2 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">WebAssembly</span></p>

Safari 15.2の変更点について。
Wasmで利用可能なメモリが4GBに拡張、COOP/COEP HTTPヘッダをサポートし、crossOriginIsolated時はSharedArrayBuffer/Wasmスレッドが利用可能に。
Canvasで`colorSpace: "display-p3"`をサポートなど


----

## Release 5.0.0 – ESM support, CSS Selectors Level 4 · css/csso
[github.com/css/csso/releases/tag/v5.0.0](https://github.com/css/csso/releases/tag/v5.0.0 "Release 5.0.0 – ESM support, CSS Selectors Level 4 · css/csso")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

CSS minifyのCSSO 5.0.0リリース。
CSS Selectors Level 4のサポート、ESMとCJSでのdual moduleに変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech
[tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd "Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

BuzzFeedでのWeb Vitalsの計測と改善についての連載記事。
RUMとSynthetic MonitingでのCLSスコアのモニタリング、RUMのログからCLSを発生させている要素の特定と修正、サードパーティの埋め込みコンテンツによるCLSの改善など

- [Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-2-2a846adeb097 "Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech")
- [Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-3-3a36240861e4 "Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech")

----

## New in Node.js: \`node:\` protocol imports
[2ality.com/2021/12/node-protocol-imports.html](https://2ality.com/2021/12/node-protocol-imports.html "New in Node.js: \`node:\` protocol imports")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

`node:` protocolでのNode.jsのビルトインモジュールの参照について。


----

## Debug memory leaks with the Microsoft Edge Detached Elements tool - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/](https://blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/ "Debug memory leaks with the Microsoft Edge Detached Elements tool - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

MSEdgeの開発者ツールのDetached Elementsについて。
DOMツリーから切り離された要素を一覧でき、DOMのメモリリークをデバッグできる機能。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## capricorn86/happy-dom: A jsdom alternative with support for server side rendering of web components.
[github.com/capricorn86/happy-dom](https://github.com/capricorn86/happy-dom "capricorn86/happy-dom: A jsdom alternative with support for server side rendering of web components.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

JSDOMのようにNode.jsでDOM APIを利用できるようにする目的のライブラリ。
サーバサイドレンダリング向けのパッケージも公開されている。


----

## Akryum/peeky: Test framework for curious minds 🐈️ Powered by Vite ⚡️
[github.com/Akryum/peeky](https://github.com/Akryum/peeky "Akryum/peeky: Test framework for curious minds 🐈️ Powered by Vite ⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Viteを使ったテストフレームワーク。
テスト開発用のGUIをもっている


----
