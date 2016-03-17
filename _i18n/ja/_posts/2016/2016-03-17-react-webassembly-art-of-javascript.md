---
title: "2016-03-17のJS: React.js v15.0 RC、WebAssembly、最近JavaScript"
author: azu
layout: post
date : 2016-03-17T22:03
category: JSer
tags:
    - React
    - WebAssembly
    - JavaScript


---

JSer.info #270 - 

----
<h1 class="site-genre">ヘッドライン</h1>

----

## V8 JavaScript Engine: V8 Release 5.0
[v8project.blogspot.com/2016/03/v8-release-50.html](http://v8project.blogspot.com/2016/03/v8-release-50.html "V8 JavaScript Engine: V8 Release 5.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.0リリース。
RegExp Unicode flagのサポート、RegExpのwell-known symbolsをサポート、`Object.keys()`やrest parameterの速度改善など

----

## Release v6.7.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.7.0](https://github.com/babel/babel/releases/tag/v6.7.0 "Release v6.7.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.7.0リリース。
async/await周りのバグ修正、内部的な変更してAST上に存在したキャッシュをWeakMapベースで保存するように変更。

----

## node/CHANGELOG.md at v5.8.0 · nodejs/node
[github.com/nodejs/node/blob/v5.8.0/CHANGELOG.md](https://github.com/nodejs/node/blob/v5.8.0/CHANGELOG.md "node/CHANGELOG.md at v5.8.0 · nodejs/node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.8.0リリース。
`path.normalize`のレグレッションを修正、`util.format`のパフォーマンス改善。

- [Node 5.7.1 path.normalize broken · Issue #5585 · nodejs/node](https://github.com/nodejs/node/issues/5585 "Node 5.7.1 path.normalize broken · Issue #5585 · nodejs/node")
- [util: improve util.format performance by evanlucas · Pull Request #5360 · nodejs/node](https://github.com/nodejs/node/pull/5360 "util: improve util.format performance by evanlucas · Pull Request #5360 · nodejs/node")

----

## Node v5.9.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.9.0/](https://nodejs.org/en/blog/release/v5.9.0/ "Node v5.9.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.9.0リリース。
`vm`モジュールのメモリ使用量の削減、`zlib`モジュールがconcatenated archivesをサポート

----

## Release v1.5.0 · testem/testem
[github.com/testem/testem/releases/tag/v1.5.0](https://github.com/testem/testem/releases/tag/v1.5.0 "Release v1.5.0 · testem/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

testem v1.5.0リリース。
複数のTest Pageを指定するとparallel実行できるように、Mochaのテストにかかった時間を表示できるようになるなど

----

## React.js v15.0 changes - blog.koba04.com
[blog.koba04.com/post/2016/03/09/react-js-v15-changes/](http://blog.koba04.com/post/2016/03/09/react-js-v15-changes/ "React.js v15.0 changes - blog.koba04.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React.js v15.0 RCの変更点まとめ

----
<h1 class="site-genre">アーティクル</h1>

----

## A WebAssembly Milestone: Experimental Support in Multiple Browsers ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/03/a-webassembly-milestone/](https://hacks.mozilla.org/2016/03/a-webassembly-milestone/ "A WebAssembly Milestone: Experimental Support in Multiple Browsers ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">status</span></p>

WebAssemblyの仕様、ブラウザの実装のステータスについて。
最初のbinary formatドラフト仕様がでており、Firefox、Chrome、ChackraCoreのNightlyで試験的な実装がされている。

- [V8 JavaScript Engine: Experimental support for WebAssembly in V8](http://v8project.blogspot.jp/2016/03/experimental-support-for-webassembly.html "V8 JavaScript Engine: Experimental support for WebAssembly in V8")
- [Previewing WebAssembly experiments in Microsoft Edge | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/03/15/previewing-webassembly-experiments/ "Previewing WebAssembly experiments in Microsoft Edge | Microsoft Edge Dev Blog")

----

## Firefox 開発ツールを使った Service Workers と Push のデバッグ | Mozilla Developer Street (modest)
[dev.mozilla.jp/2016/03/debugging-service-workers-and-push-with-firefox-devtools/](https://dev.mozilla.jp/2016/03/debugging-service-workers-and-push-with-firefox-devtools/ "Firefox 開発ツールを使った Service Workers と Push のデバッグ | Mozilla Developer Street (modest)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">ServiceWorker</span></p>

FirefoxでのService WorkerとPush Notificationsのデバッグについて。
`about:debugging`というデバッグのダッシュボード画面についても書かれている

----

## State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium
[medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b](https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b "State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

最近のJavaScriptにおける主流となったライブラリやツールについて。
React、Redux、Babel、ESLint、npm、webpack、mochaなどのテストツールなどや人について

> If you don’t need it, don’t use it

と書かれているように全てに対するベストではないという話も書かれている

----

## Learning React Without Using React Part 1 — JavaScript Inside — Medium
[medium.com/javascript-inside/learn-the-concepts-part-1-418952d968cb](https://medium.com/javascript-inside/learn-the-concepts-part-1-418952d968cb "Learning React Without Using React Part 1 — JavaScript Inside — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

ツールなどは使わないで学ぶReactのチュートリアル。

----

## Webpack FTW!!!!
[k94n.com/webpack-ftw](https://k94n.com/webpack-ftw "Webpack FTW!!!!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpackはどんなことができるのかというのをわかりやすく簡単に紹介してる

- [Webpack FTW // Speaker Deck](https://speakerdeck.com/k9ordon/webpack-ftw "Webpack FTW // Speaker Deck")

----

## 特集：C#×JavaScript：ECMAScriptの最新情報を得るには (1/2) - ＠IT
[www.atmarkit.co.jp/ait/articles/1603/11/news042.html](http://www.atmarkit.co.jp/ait/articles/1603/11/news042.html "特集：C#×JavaScript：ECMAScriptの最新情報を得るには (1/2) - ＠IT")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span></p>

ECMAScriptの仕様策定のプロセスやリソースがどこにあるかがまとまってる記事

----

## Jest | &quot;JavaScript Unit Testing Performance&quot;
[facebook.github.io/jest/blog/2016/03/11/javascript-unit-testing-performance.html](http://facebook.github.io/jest/blog/2016/03/11/javascript-unit-testing-performance.html "Jest | "JavaScript Unit Testing Performance"")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

テストフレームワークのJestが実行時間を改善するためにやっていることについて

----

## JavaScript Proposal for weak references: WeakRef
[ponyfoo.com/articles/weakref](https://ponyfoo.com/articles/weakref "JavaScript Proposal for weak references: WeakRef")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">proposal</span></p>

`WeakRef` Proposalについての解説。
WeakMapと同じようにWeakな扱いだが、WeakMapと違いGCで回収された時に呼ばれる`executor`を指定できる。(WeakMap/Setは回収されたタイミングを知ることができない)

- [proposal-weakrefs/weakrefs.md at master · tc39/proposal-weakrefs](https://github.com/tc39/proposal-weakrefs/blob/master/specs/weakrefs.md "proposal-weakrefs/weakrefs.md at master · tc39/proposal-weakrefs")

----

## Node.js Buffer API Changes — Medium
[medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97](https://medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97 "Node.js Buffer API Changes — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span></p>

Node.js v6で予定されているBuffer APIの変更についての解説

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Fluent Conference 2016 (San Francisco, CA) - YouTube
[www.youtube.com/watch?v=9UYoKyuFXrM&amp;list=PL055Epbe6d5bQubu5EWf\_kUNA3ef\_qbmL](https://www.youtube.com/watch?v=9UYoKyuFXrM&amp;list=PL055Epbe6d5bQubu5EWf_kUNA3ef_qbmL "Fluent Conference 2016 (San Francisco, CA) - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画 </span></p>

Fluent Conference 2016の動画が公開された

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## PostCSS.parts | A searchable catalog of PostCSS plugins
[postcss.parts/](http://postcss.parts/ "PostCSS.parts | A searchable catalog of PostCSS plugins")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span> <span class="jser-tag">検索</span></p>

PostCSSのカタログサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Introducing InversifyJS 2.0
[blog.wolksoftware.com/introducing-inversify-2](http://blog.wolksoftware.com/introducing-inversify-2 "Introducing InversifyJS 2.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Inversion of control (IoC)コンテナーのTypeScript向けライブラリ

----

## rajasegar/compack: An awesome bundler for Web Components
[github.com/rajasegar/compack](https://github.com/rajasegar/compack "rajasegar/compack: An awesome bundler for Web Components")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">Tools</span></p>

Web Componentsのscaffoldingとbundleするツール

----

## eanplatter/enclave: A simpler way to compile React applications http://enclave.js.org
[github.com/eanplatter/enclave](https://github.com/eanplatter/enclave "eanplatter/enclave: A simpler way to compile React applications http://enclave.js.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">Tools</span></p>

`npm install`して`npm start`するだけで、React+Babelな環境を動かせるブートストラップ的なツール

----
