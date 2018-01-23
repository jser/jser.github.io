---
title: "2018-01-23のJS: 2018-01-23のJS: Bootstrap 4、create-react-app 1.1.0と2.0、kuker"
author: "azu"
layout: post
date : 2018-01-23T03:05:24.055Z
category: JSer
tags:
- CSS
- React
- debug
- browser

---

JSer.info #367 - CSSフレームワークのBootstrap 4が正式リリースされました。
[Bootstrap 3.3.0](http://blog.getbootstrap.com/2014/10/29/bootstrap-3-3-0-released/ "Bootstrap 3.3.0")から約3年ぶりのメジャーアップデートとなります。

- [Bootstrap 4 · Bootstrap](https://blog.getbootstrap.com/2018/01/18/bootstrap-4/)

4.0では実装をLessからSassへ変更、GridシステムにFlexboxを利用、Panelsやthumbnailsを廃止しCardsへの移行などの変更が行なわれています。そのため、コンポーネントへ指定するクラス名のリネームも行われています。
詳しい変更点とv3からの違いについてはマイグレーションガイドを参照してください。

- [Migrating to v4 · Bootstrap](https://getbootstrap.com/docs/4.0/migration/)

また、IE 8、9のサポート終了し、v4からはIE10+、iOS 7+、Android 5.0+が対象となっています。

- [Browsers and devices · Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/browsers-devices/ "Browsers and devices · Bootstrap")

----

Reactの開発ツールである[create-react-app](https://github.com/facebook/create-react-app "create-react-app") 1.1.0がリリースされました。

- [Release v1.1.0 · facebook/create-react-app](https://github.com/facebook/create-react-app/releases/tag/v1.1.0 "Release v1.1.0 · facebook/create-react-app")

`--use-npm`の追加、`--scripts-version`で`.tar.gz`や`file:`のサポートなどが行われています。
また、このリリースが1.1.x系の最後となり、次のメジャーアップデート候補である2.0に含める機能についての議論が行われています。

- [Roadmap for react-scripts@2.0 · Issue #3815 · facebook/create-react-app](https://github.com/facebook/create-react-app/issues/3815 "Roadmap for react-scripts@2.0 · Issue #3815 · facebook/create-react-app")

----

[kuker](https://github.com/krasimir/kuker "kuker")というReact、Angular、Vue、Redux、MobX、HTMLなどに対応したデバッグツールが公開されています。
kukerは、ライブラリの状態やイベントのログを`postMessage`で送り、そのログを表示できるブラウザ拡張となっています。

たとえば、Reduxならばコンポーネントのライフサイクルログを表示し、ReduxならReduxからdispatchされたActionとその時点でのStateを表示できるようになります。

同じ系統のデバッグブラウザ拡張として[Redux DevTools](https://github.com/gaearon/redux-devtools "Redux DevTools")があります。
[Almin](https://almin.js.org/ "Almin")というライブラリ向けに、[Redux DevToolsに対応したもの](https://github.com/almin/almin-devtools)と[kukerに対応したもの](https://github.com/almin/almin-kuker-devtools)をそれぞれ書いてみました。
どちらも任意のデータを送る仕組みを持っていますが、kukerは単純に`postMessage`でイベントやStateを送るだけなので特別な仕組みは必要ありません。

```js
const sendToDevTools = ({ type, state }) => {
    window.postMessage({
        kuker: true,
        type: type,
        origin: 'Almin',
        label: type,
        time: (new Date()).getTime(),
        state: { state },
        icon: 'fa-money',
        color: '#bada55'
    }, '*');
};
```

詳しくは作者のブログで必要となった理由や仕組みについて書かれているので見てみると良さそうです。

- [Debugging your front-end like it's 2019](http://krasimirtsonev.com/blog/article/debugging-your-front-end-like-is-2019 "Debugging your front-end like it&#39;s 2019")

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.0.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.0.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.0.0 "Release v1.0.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer 1.0.0リリース。
コードカバレッジAPIのサポート、PDFのカスタマイズ、XPathのサポートなど

- [Puppeteer  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/puppeteer/ "Puppeteer  |  Tools for Web Developers  |  Google Developers")

----

## Announcing TypeScript 2.7 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/01/17/announcing-typescript-2-7-rc/](https://blogs.msdn.microsoft.com/typescript/2018/01/17/announcing-typescript-2-7-rc/ "Announcing TypeScript 2.7 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.7RCリリース

クラスプロパティへの代入忘れをチェックする`--strictPropertyInitialization`の追加、Tupleの扱いの変更、`in`と`instanceof`の改善など


----

## Bootstrap 4 · Bootstrap
[blog.getbootstrap.com/2018/01/18/bootstrap-4/](https://blog.getbootstrap.com/2018/01/18/bootstrap-4/ "Bootstrap 4 · Bootstrap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 4リリース。
4.0ではLessからSassへ、Flexboxの利用、Cardsへの移行、IE 8、9などのサポート終了など。
β3からの変更として、printのスタイルの更新サンプル、ドキュメントの追加など

- [Bootstrap 4 Beta · Bootstrap](https://blog.getbootstrap.com/2017/08/10/bootstrap-4-beta/ "Bootstrap 4 Beta · Bootstrap")
- [Migrating to v4 · Bootstrap](https://getbootstrap.com/docs/4.0/migration/ "Migrating to v4 · Bootstrap")

----

## Release v5.0.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v5.0.0](https://github.com/mochajs/mocha/releases/tag/v5.0.0 "Release v5.0.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 5.0.0リリース。
IE 9、10のサポート終了、テストファイルを追加指定する`--file`オプションの追加など


----

## Polymer 3.0: New Year, New Preview - Polymer Project
[www.polymer-project.org/blog/2018-01-18-polymer-3-new-preview](https://www.polymer-project.org/blog/2018-01-18-polymer-3-new-preview "Polymer 3.0: New Year, New Preview - Polymer Project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 3.0-pre.4リリース。
`PropertiesMixin`の追加、`html`タグ関数の改善。
Stableリリースは2018年Q1末を予定


----

## jQuery 3.3.0 – A fragrant bouquet of deprecations and…is that a new feature? | Official jQuery Blog
[blog.jquery.com/2018/01/19/jquery-3-3-0-a-fragrant-bouquet-of-deprecations-and-is-that-a-new-feature/](http://blog.jquery.com/2018/01/19/jquery-3-3-0-a-fragrant-bouquet-of-deprecations-and-is-that-a-new-feature/ "jQuery 3.3.0 – A fragrant bouquet of deprecations and…is that a new feature? | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.3.0リリース。
`.addClass()`、`.removeClass()`、`.toggleClass()`が配列を受け取れるように。
`jQuery.now`や`jQuery.isFunction`などが非推奨になるなど


----

## Release v1.1.0 · facebookincubator/create-react-app
[github.com/facebookincubator/create-react-app/releases/tag/v1.1.0](https://github.com/facebookincubator/create-react-app/releases/tag/v1.1.0 "Release v1.1.0 · facebookincubator/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 1.1.0リリース。
`--use-npm`の追加、`--scripts-version`で`.tar.gz`や`file:`のサポートなど。
2.0のα版もリリースされ、2.0に含める機能についてはIssueで議論している。

- [Roadmap for react-scripts@2.0 · Issue #3815 · facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app/issues/3815 "Roadmap for react-scripts@2.0 · Issue #3815 · facebookincubator/create-react-app")

----
<h1 class="site-genre">アーティクル</h1>

----

## Understanding SVG Coordinate Systems and Transformations (Part 1) — The viewport, viewBox, and preserveAspectRatio
[www.sarasoueidan.com/blog/svg-coordinate-systems/](https://www.sarasoueidan.com/blog/svg-coordinate-systems/ "Understanding SVG Coordinate Systems and Transformations (Part 1) — The viewport, viewBox, and preserveAspectRatio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">article</span></p>

SVGのviewport、viewBox、preserveAspectRatioについての詳しい解説


----

## Oxidizing Source Maps with Rust and WebAssembly – Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2018/01/oxidizing-source-maps-with-rust-and-webassembly/](https://hacks.mozilla.org/2018/01/oxidizing-source-maps-with-rust-and-webassembly/ "Oxidizing Source Maps with Rust and WebAssembly – Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Rust</span></p>

Source Mapパーサ、ジェネレーターをRust + WebAssemblyに書き換えた話。
Rustで書いてwasmに変換して使うことで、JavaScriptの実装に比べて処理時間や処理の安定性が向上したという話

- [Use WebAssembly to speed up SourceMapConsumer by fitzgen · Pull Request #306 · mozilla/source-map](https://github.com/mozilla/source-map/pull/306 "Use WebAssembly to speed up SourceMapConsumer by fitzgen · Pull Request #306 · mozilla/source-map")

----

## What's New In DevTools (Chrome 65)  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/01/devtools](https://developers.google.com/web/updates/2018/01/devtools "What's New In DevTools (Chrome 65)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Chrome 65での開発者ツールの変更点について。
Local Overrides、アクセシビリティツール、カラーピッカーにコンストラスト情報の表示、ステップ実行でWorkerやsetTimeoutなどの非同期処理のサポート。
パフォーマンスパネルで複数の記録を保存できるようになるなど


----

## Debugging your front-end like it's 2019
[krasimirtsonev.com/blog/article/debugging-your-front-end-like-is-2019](http://krasimirtsonev.com/blog/article/debugging-your-front-end-like-is-2019 "Debugging your front-end like it's 2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Flux</span> <span class="jser-tag">redux</span> <span class="jser-tag">Angular</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span></p>

kukerという開発者ツールについて。
redux-devtoolsのようにブラウザに拡張をインストールし、ReduxやReact、Angularなどライブラリのログを見ることができる。
ログを投げる側は`postMessage`を送ることで記録できる。

- [krasimir/kuker: Kick-ass browser extension to debug your apps](https://github.com/krasimir/kuker "krasimir/kuker: Kick-ass browser extension to debug your apps")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## CSS Grid — Learn all about CSS Grid with Wes Bos in this free video series!
[cssgrid.io/](https://cssgrid.io/ "CSS Grid — Learn all about CSS Grid with Wes Bos in this free video series!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">video</span></p>

CSS Grid講座


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Render Props - React
[reactjs.org/docs/render-props.html](https://reactjs.org/docs/render-props.html "Render Props - React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span></p>

ReactのRender Propsのパターンについてのドキュメント


----

## Introduction · A Roadmap for Node.js Security
[nodesecroadmap.fyi/](https://nodesecroadmap.fyi/ "Introduction · A Roadmap for Node.js Security")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

Node.jsのセキュリティに関するドキュメント。Node.jsにおけてセキュリティ的な問題が起きる項目について。
またDynamic requireなどコードレ別の問題などについて


----

## krasimir/kuker: Kick-ass browser extension to debug your apps
[github.com/krasimir/kuker](https://github.com/krasimir/kuker "krasimir/kuker: Kick-ass browser extension to debug your apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span></p>

クライアントから`postMessage`で投げたログとStateを表示できるビューアのブラウザ拡張。
React、Redux、Angular、Vue、HTMLなどに対応したデバッグツール。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## skerit/json-dry: JSON-dry allows you to serialize & revive objects containing circular references, dates, regexes, class instances,...
[github.com/skerit/json-dry](https://github.com/skerit/json-dry "skerit/json-dry: JSON-dry allows you to serialize & revive objects containing circular references, dates, regexes, class instances,...")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

正規表現や循環参照に対応したJSONシリアライズ/デシリアライズライブラリ。
オブジェクトのクローンも行える。


----

## boltpkg/bolt: ⚡️ Super-powered JavaScript project management
[github.com/boltpkg/bolt](https://github.com/boltpkg/bolt "boltpkg/bolt: ⚡️ Super-powered JavaScript project management")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

lerna/yarn workspaceのようなmonorepo管理ツール。
buildやtestなどにデフォルト設定があり、monorepoの環境構築を簡単にできるようにすることが目的


----
<h1 class="site-genre">書籍関係</h1>

----

## Functional-Light… by Kyle Simpson \[Leanpub PDF/iPad/Kindle\]
[leanpub.com/fljs](https://leanpub.com/fljs "Functional-Light… by Kyle Simpson \[Leanpub PDF/iPad/Kindle\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">book</span></p>

Functional programming (FP)のアプローチをJavaScriptに適応してFPについて学ぶ書籍


----

## Simplifying JavaScript: Writing Modern JavaScript with ES5, ES6, and Beyond by Joe Morgan | The Pragmatic Bookshelf
[pragprog.com/book/es6tips/simplifying-javascript](https://pragprog.com/book/es6tips/simplifying-javascript "Simplifying JavaScript: Writing Modern JavaScript with ES5, ES6, and Beyond by Joe Morgan | The Pragmatic Bookshelf")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

2018年5月10日発売
ES2015以降の新しい構文を学び、読みやすく拡張し易いコードを書く方法についてを学ぶ書籍。


----

## Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books
[www.amazon.com/Testing-Vue-Js-Applications/dp/1617295248](https://www.amazon.com/Testing-Vue-Js-Applications/dp/1617295248 "Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span></p>

2017年7月30日発売
Vueアプリケーションのテストについての書籍


----
