---
title: "2019-06-17のJS: react-redux 7.1.0(Hooksサポート)、Pika CDN、State of CSS 2019"
author: "azu"
layout: post
date : 2019-06-17T01:22:37.368Z
category: JSer
tags:
- Redux
- React
- ESModules
- CSS

---

JSer.info #440 - ReactのRedux向けバインディングのreact-redux 7.1.0がリリースされました。

- [Release v7.1.0 · reduxjs/react-redux](https://github.com/reduxjs/react-redux/releases/tag/v7.1.0)

7.1.0ではReact Hooksに対応しています。
React Hooksで扱える`ueSelector`というAPIが追加されています。

```js
import React from 'react'
import { useSelector } from 'react-redux'

export const CounterComponent = () => {
  const counter = useSelector(state => state.counter)
  return <div>{counter}</div>
}
```

詳しくは次のドキュメントで解説されています。

- [Hooks · React Redux](https://react-redux.js.org/next/api/hooks)

----

[Pika CDN](https://www.pika.dev/cdn)というnpmに公開されているES Module形式のパッケージをURLから読み込めるウェブサービスが公開されています。

Pika CDNで読み込めるのは`package.json`の`module`フィールドに対応したパッケージのみとなっています。
パッケージの`module`フィールドへの対応は、このサービス自身が出している[@pika/web](https://github.com/pikapkg/web)や[pkg.module](https://github.com/rollup/rollup/wiki/pkg.module)などを参照すると良さそうです。

また、読み込むパッケージはブラウザのUserAgentを元に最適化されたものが配布されるようになっているようです。

----

[The State of CSS 2019](https://2019.stateofcss.com/)のアンケート結果が公開されています。

- [機能](https://2019.stateofcss.com/features/)
- [単位、CSSセレクタ](https://2019.stateofcss.com/units-and-selectors/)
- [プリプロセッサ、フレームワーク、CSS in JS](https://2019.stateofcss.com/technologies/)

などについてのアンケート結果が公開されています。
主にアメリカ、イギリス、ドイツ、フランス、カナダあたりの回答で半分を占めていますが、CSSに興味がある人は見てみると面白いかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v2.5.0 · fastify/fastify
[github.com/fastify/fastify/releases/tag/v2.5.0](https://github.com/fastify/fastify/releases/tag/v2.5.0 "Release v2.5.0 · fastify/fastify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Node.jsウェブフレームワークのfastify 2.5.0リリース。
レスポンスタイムを取得できる`Reply#getResponseTime`の追加など


----

## Release v7.1.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v7.1.0](https://github.com/reduxjs/react-redux/releases/tag/v7.1.0 "Release v7.1.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux 7.1.0リリース。
React Hooksに正式対応、`useSelector`の第2引数に`deps`オプションの追加など

- [Hooks · React Redux](https://react-redux.js.org/next/api/hooks "Hooks · React Redux")

----

## Release v0.101.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.101.0](https://github.com/facebook/flow/releases/tag/v0.101.0 "Release v0.101.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType v0.101.0リリース。
inexact object syntaxである`...`のlintに対応、関数の型パラメータのデフォルト型を指定可能になるなど

- [On the Roadmap: Exact Objects by Default – Flow – Medium](https://medium.com/flow-type/on-the-roadmap-exact-objects-by-default-16b72933c5cf "On the Roadmap: Exact Objects by Default – Flow – Medium")
- [flow - allow type parameter defaults in function declarations by tanhauhau · Pull Request #10084 · babel/babel](https://github.com/babel/babel/pull/10084 "flow - allow type parameter defaults in function declarations by tanhauhau · Pull Request #10084 · babel/babel")

----

## Release Notes for Safari Technology Preview 85 | WebKit
[webkit.org/blog/9281/release-notes-for-safari-technology-preview-85/](https://webkit.org/blog/9281/release-notes-for-safari-technology-preview-85/ "Release Notes for Safari Technology Preview 85 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 85リリース。
Pointer Eventsの対応改善、`Promise.allSettled`の実装、ES PropoaslのNumeric Separatorを実装など


----

## New in Chrome 75  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/06/nic75](https://developers.google.com/web/updates/2019/06/nic75 "New in Chrome 75  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 75リリース。
低遅延Canvasを利用できる`desynchronized`オプションのサポート、Web Share APIがファイルをサポート、ES ProposalのNumeric separatorのサポート。
また、`playsInline`のサポート、HTTPヘッダの`stale-while-revalidate`レスポンスディレティブのサポート、CSPで`script-src-attr`ディレクティブなどを追加など

- [Google Developers Japan: Chrome 75: 低遅延キャンバス コンテキスト、ファイル共有、数値セパレータ](https://developers-jp.googleblog.com/2019/06/chrome-75.html "Google Developers Japan: Chrome 75: 低遅延キャンバス コンテキスト、ファイル共有、数値セパレータ")

----

## TypeScript Playground | The unofficial playground for advanced TypeScript users
[playground.type-puzzle.org/](https://playground.type-puzzle.org/ "TypeScript Playground | The unofficial playground for advanced TypeScript users")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

`@types/*`モジュールの型も解決できるTypeScript  Playground

- [「外部パッケージの型定義もインストールし推論できるTypeScript playgroundを作った」という題で登壇してきました＋スライドの補足 | WEB EGG](https://blog.leko.jp/post/introduce-the-new-typescript-playground-for-advanced-use/ "「外部パッケージの型定義もインストールし推論できるTypeScript playgroundを作った」という題で登壇してきました＋スライドの補足 | WEB EGG")

----
<h1 class="site-genre">アーティクル</h1>

----

## How to Use the Web Share API | CSS-Tricks
[css-tricks.com/how-to-use-the-web-share-api/](https://css-tricks.com/how-to-use-the-web-share-api/ "How to Use the Web Share API | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Web Share APIの使い方についての記事。サポートブラウザやFeature Detect、APIの使い方について。
またサポートしていない場合のFallbackについて


----

## Unpacking hoisting
[2ality.com/2019/05/unpacking-hoisting.html](http://2ality.com/2019/05/unpacking-hoisting.html "Unpacking hoisting")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`var`や`function`などのHoistingの動作を別の角度から解説した記事。
ES2015からはスコープのTopに移動するという説明になっているという話。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## The modern PWA Cheat Sheet by Maximiliano Firtman | JSConf EU 2019 - YouTube
[www.youtube.com/watch?v&#x3D;cybhV88KLfI](https://www.youtube.com/watch?v=cybhV88KLfI "The modern PWA Cheat Sheet by Maximiliano Firtman | JSConf EU 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">video</span></p>

PWAについての発表動画。
ライフサイクル、Web API、iOS、Web APKsやアプリとしての配布についてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Pika CDN - Pika
[www.pika.dev/cdn](https://www.pika.dev/cdn "Pika CDN - Pika")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">webservice</span></p>

ES Moduleに対応したnpmモジュールCDNサービス。
UA別に最適化したビルド結果のパッケージを返すことができる。


----

## The State of CSS 2019
[2019.stateofcss.com/](https://2019.stateofcss.com/ "The State of CSS 2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">アンケート</span></p>

State of CSS 2019のアンケート結果。
FlexboxやGridなどのレイアウト、単位、Pre & Post Processors、エディタやツールなどの利用についてのアンケート結果


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## tradingview/lightweight-charts: Financial lightweight charts built with HTML5 canvas
[github.com/tradingview/lightweight-charts](https://github.com/tradingview/lightweight-charts "tradingview/lightweight-charts: Financial lightweight charts built with HTML5 canvas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">グラフ</span> <span class="jser-tag">library</span></p>

Financial Chartライブラリ


----

## nikersify/jay: 😎 Supercharged JavaScript REPL
[github.com/nikersify/jay](https://github.com/nikersify/jay "nikersify/jay: 😎 Supercharged JavaScript REPL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

`require`で外部npmモジュールの自動インストール、`require`キャッシュの破棄などの機能を含んだNode REPL。


----

## josdejong/workerpool: Offload tasks to a pool of workers on node.js and in the browser
[github.com/josdejong/workerpool](https://github.com/josdejong/workerpool "josdejong/workerpool: Offload tasks to a pool of workers on node.js and in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ブラウザのWeb WorkerやNode.jsの`worker_threads`に対応したWorker Poolライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## 仕事ですぐに使えるTypeScript — 仕事ですぐに使えるTypeScript ドキュメント
[future-architect.github.io/typescript-guide/index.html](https://future-architect.github.io/typescript-guide/index.html "仕事ですぐに使えるTypeScript — 仕事ですぐに使えるTypeScript ドキュメント")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span> <span class="jser-tag">tutorial</span></p>

TypeScriptについて学ぶためのドキュメント。
基本的なJavaScriptの書き方、型の書き方、アプリケーションの作成についてなど

- [TypeScript教育用コンテンツ公開のお知らせ | Future Tech Blog - フューチャーアーキテクト](https://future-architect.github.io/articles/20190612/ "TypeScript教育用コンテンツ公開のお知らせ | Future Tech Blog - フューチャーアーキテクト")

----
