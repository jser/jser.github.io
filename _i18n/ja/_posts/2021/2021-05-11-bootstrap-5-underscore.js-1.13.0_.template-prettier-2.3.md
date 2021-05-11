---
title: "2021-05-11のJS: Bootstrap 5、 Underscore.js 1.13.0(`_.template`のセキュリティ修正)、Prettier 2.3"
author: "azu"
layout: post
date : 2021-05-11T02:01:52.181Z
category: JSer
tags:
- CSS
- Tools
- node.js
- book
- WebComponents

---

JSer.info #539 - - [Bootstrap 5 | Bootstrap Blog](https://blog.getbootstrap.com/2021/05/05/bootstrap-5/)
- [Migrating to v5 · Bootstrap v5.0](https://getbootstrap.com/docs/5.0/migration/)

----

- [Underscore.js 1.13.0](https://underscorejs.org/#1.13.0)

----

- [Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier](https://prettier.io/blog/2021/05/09/2.3.0.html)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bootstrap 5 | Bootstrap Blog
[blog.getbootstrap.com/2021/05/05/bootstrap-5/](https://blog.getbootstrap.com/2021/05/05/bootstrap-5/ "Bootstrap 5 | Bootstrap Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

Bootstrap 5リリース。
IEのサポート終了、jQueryの削除。
offcanvasコンポーネント、cardの代替えとなるaccordionコンポーネントの追加。
FormとLayoutの変更、RTLのサポート、SassのUtility APIの追加など。

- [Migrating to v5 · Bootstrap v5.0](https://getbootstrap.com/docs/5.0/migration/ "Migrating to v5 · Bootstrap v5.0")

----

## Underscore.js
[underscorejs.org/#1.13.0](https://underscorejs.org/#1.13.0 "Underscore.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

underscore 1.13.0リリース。
ECMAScript Modulesのサポート。
1.12.1では`_.template`の`variable`オプション経由でのCode Injectionができる脆弱性も修正されている。


----

## Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier
[prettier.io/blog/2021/05/09/2.3.0.html](https://prettier.io/blog/2021/05/09/2.3.0.html "Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.3リリース。
JavaScriptのフォーマットの大きめな変更、Handlebarsサポートをalphaからreleaseに変更、JSON5/JSONのフォーマットの修正など


----

## google/zx: A tool for writing better scripts
[github.com/google/zx](https://github.com/google/zx "google/zx: A tool for writing better scripts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ShellScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

シェルスクリプトのような処理をJavaScriptで書けるNode.js製のツール。
Top-Level awaitを使ってシェルコマンドをそのまま使える`$`やHTTP通信するfetchなどが同梱されている。


----
<h1 class="site-genre">アーティクル</h1>

----

## How we use Web Components at GitHub - The GitHub Blog
[github.blog/2021-05-04-how-we-use-web-components-at-github/](https://github.blog/2021-05-04-how-we-use-web-components-at-github/ "How we use Web Components at GitHub - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">Github</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

GitHubでのWeb Componentsについて。
Rails ViewComponentとCatalystを使ったWeb Componentsの組み込み、GitHub Elementsの公開についてなど

- [github/github-elements: GitHub&#039;s Web Component collection.](https://github.com/github/github-elements "github/github-elements: GitHub&amp;#039;s Web Component collection.")

----

## リソースの読み込みを助けるウェブブラウザ API の世界
[nhiroki.jp/2021/05/06/resource-loading-apis](https://nhiroki.jp/2021/05/06/resource-loading-apis "リソースの読み込みを助けるウェブブラウザ API の世界")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

先読みや読み込みの優先度などウェブブラウザにおけるリソースロードのHintとなるAPIや仕組みについてのまとめ


----

## Hello, Modules!. JavaScript Modules, also known as ESM… | by Sindre Sorhus | May, 2021 | 🦄 Sindre Sorhus’ blog
[blog.sindresorhus.com/hello-modules-d1010b4e777b](https://blog.sindresorhus.com/hello-modules-d1010b4e777b "Hello, Modules!. JavaScript Modules, also known as ESM… | by Sindre Sorhus | May, 2021 | 🦄 Sindre Sorhus’ blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 10のサポートが終了したことで、ESMへの移行をどのようにするかについての記事。
ESMのメリット、パッケージのメンテナ向けの移行ガイドについて


----

## A Guide To Newly Supported, Modern CSS Pseudo-Class Selectors — Smashing Magazine
[www.smashingmagazine.com/2021/04/guide-supported-modern-css-pseudo-class-selectors/](https://www.smashingmagazine.com/2021/04/guide-supported-modern-css-pseudo-class-selectors/ "A Guide To Newly Supported, Modern CSS Pseudo-Class Selectors — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

最近のCSSで扱える擬似クラスの紹介記事。
任意の`a`にマッチする`:any-link`、フォーカスしてる要素を扱う`:focus-visible`と`:focus-within`、セレクタを扱う`:is()`と`where()`と`:has()`、`:empty`など


----

## Chapter 8: CSS | CSS-Tricks
[css-tricks.com/chapter-8-css/](https://css-tricks.com/chapter-8-css/ "Chapter 8: CSS | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">history</span> <span class="jser-tag">article</span></p>

CSSの歴史についての記事。
Lie、IE3のCSS実装、W3CのCSS WG、NetscapeのJSSS。
doctype宣言でのスイッチと後方互換性、fantasai、CSS3でのモジューラアプローチについてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Svelte Summit Spring 2021 簡易まとめ
[zenn.dev/tomoam/articles/889618f2e6e62f](https://zenn.dev/tomoam/articles/889618f2e6e62f "Svelte Summit Spring 2021 簡易まとめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Svelte Summit Springの動画と概要のまとめ

- [Svelte Summit is a FREE whole-day online event.](https://sveltesummit.com/ "Svelte Summit is a FREE whole-day online event.")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## sinclairzx81/hammer: Build Tool for Browser and Node Applications
[github.com/sinclairzx81/hammer](https://github.com/sinclairzx81/hammer "sinclairzx81/hammer: Build Tool for Browser and Node Applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">Tools</span></p>

esbuildをベースにしたparcelのようにHTMLをエントリポイントにしたビルド/開発ツール


----

## jsxtools/cqfill: Polyfill for CSS Container Queries
[github.com/jsxtools/cqfill](https://github.com/jsxtools/cqfill "jsxtools/cqfill: Polyfill for CSS Container Queries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span></p>

CSS Container Queriesのpolyfill。
PostCSSと組み合わせて利用できる


----
<h1 class="site-genre">書籍関係</h1>

----

## プロフェッショナルWebプログラミング　JavaScript | 柳井 政和 | 工学 | Kindleストア | Amazon
[www.amazon.co.jp/dp/B092QQJQF4/](https://www.amazon.co.jp/dp/B092QQJQF4/ "プロフェッショナルWebプログラミング　JavaScript | 柳井 政和 | 工学 | Kindleストア | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

ウェブページを動作させることに絞ったJavaScriptの入門書


----

## React と Vue に関する XSS アンチパターン
[zenn.dev/yuuhu04/books/xss-anti-pattern-of-react-and-vue](https://zenn.dev/yuuhu04/books/xss-anti-pattern-of-react-and-vue "React と Vue に関する XSS アンチパターン")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">XSS</span> <span class="jser-tag">document</span></p>

ReactとVueにおけるXSSのパターンについて書かれた文章。
ReactとVueのエスケープの仕組み、フレームワークが保護しないケースとXSSが発生するパターンについて書かれている


----
