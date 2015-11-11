---
title: "2015-11-09のJS: 巨大なJavaScriptのリファクタリング、Firefox 44の開発者ツール"
author: azu
layout: post
date : 2015-11-09T22:03
category: JSer
tags:
    - JavaScript
    - Firefox
    - debug

---

JSer.info #252 - [フロントエンドに秩序を取り戻す方法 // Speaker Deck](https://speakerdeck.com/fand/hurontoendonizhi-xu-woqu-rili-sufang-fa "フロントエンドに秩序を取り戻す方法 // Speaker Deck")というスライドでは、はてなブログの編集画面をどのようにリファクタリングしていっているかという話が書かれています。

<script async class="speakerdeck-embed" data-id="8175ffced95e4d1699c0e5f73357e8fd" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

名前空間風のオブジェクトで管理されていたものを、CommonJSのモジュール管理に変えていくリファクタリングの流れ、Viewのライブラリ導入の議論、Lintやテストの方針などについて書かれています。

JavaScriptにモジュール的な概念が根付いたのはここ数年なので、このように一つの巨大な名前空間オブジェクトで管理されているものを移行していくケーススタディとして見てみると面白いかもしれません。


----

[Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/11/developer-edition-44-creative-tools-and-more/ "Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog")([翻訳](http://www.mozilla.jp/blog/entry/10510/))という記事ではFirefox 44での開発者ツールの機能について紹介されています。

アニメーションツール、 CSSフィルタツール、カラーインスペクタツールなどのビジュアル的なツールの追加がされており、これらの機能については[DevTools Challenger](http://devtoolschallenger.com/ "DevTools Challenger")というサイトで実際に使い方を試しながら学ぶ事ができます。

また、メモリのスナップショットやWebSocketのframeを確認するデバッグ機能などが追加されています。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v3.4.0 · npm/npm
[github.com/npm/npm/releases/tag/v3.4.0](https://github.com/npm/npm/releases/tag/v3.4.0 "Release v3.4.0 · npm/npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 3.4.0で`npm install && npm test`を行う`npm install-test`というコマンドが追加された。
`--dry-run`などと組み合わせて、依存モジュールのアップデートテストに活用出来る

----

## PEP 0.4.0 | Official jQuery Blog
[blog.jquery.com/2015/11/05/pep-0-4-0/](http://blog.jquery.com/2015/11/05/pep-0-4-0/ "PEP 0.4.0 | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Pointer Events Polyfill 0.4.0リリース

----

## Release ES2016 Draft 2015-11-03 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20151103](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20151103 "Release ES2016 Draft 2015-11-03 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2015-11-03リリース。
abstract operationであるReturnIfAbruptのシンタックスシュガーである`?`の導入。
仕様書のバグ修正や実在する実装に合わせて`__proto__`がstrict modeでも許可されるようになるなど

----

## ESLint v1.9.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/11/eslint-v1.9.0-released/](http://eslint.org/blog/2015/11/eslint-v1.9.0-released/ "ESLint v1.9.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.9.0リリース。
npm 3の対応改善など

----
<h1 class="site-genre">アーティクル</h1>

----

## 7 Things You Should Know About WebAssembly
[auth0.com/blog/2015/10/14/7-things-you-should-know-about-web-assembly/](https://auth0.com/blog/2015/10/14/7-things-you-should-know-about-web-assembly/ "7 Things You Should Know About WebAssembly")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span></p>

WebAssemblyについてよくある疑問に対する分かりやすい解説

----

## Javascript quiz. ES6 edition. — Perfection Kills
[perfectionkills.com/javascript-quiz-es6/](http://perfectionkills.com/javascript-quiz-es6/ "Javascript quiz. ES6 edition. — Perfection Kills")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6についてのJavaScriptクイズ

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## フロントエンドに秩序を取り戻す方法 // Speaker Deck
[speakerdeck.com/fand/hurontoendonizhi-xu-woqu-rili-sufang-fa](https://speakerdeck.com/fand/hurontoendonizhi-xu-woqu-rili-sufang-fa "フロントエンドに秩序を取り戻す方法 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

昔ながらの名前空間風で管理されconcatして扱うJavaScriptをどうやってモジュール管理出来るようにリファクタリングしていくかという話。
また、Reactなどのライブラリ導入における議論やリファクタリングとE2E/ユニットテストについて

----

## Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/11/developer-edition-44-creative-tools-and-more/](https://hacks.mozilla.org/2015/11/developer-edition-44-creative-tools-and-more/ "Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firefox 44での開発者ツールについて。
アニメーションパネル、 pixel rulers、メモリ消費量のスナップショット、WebSocketのデバッグ機能の追加など

- [Developer Edition 44：新しいスタイル調整機能とメモリー管理ツール | Mozilla Japan ブログ](http://www.mozilla.jp/blog/entry/10510/ "Developer Edition 44：新しいスタイル調整機能とメモリー管理ツール | Mozilla Japan ブログ")

----

## What&#x27;s new in Chrome DevTools? // Speaker Deck
[speakerdeck.com/addyosmani/whats-new-in-chrome-devtools](https://speakerdeck.com/addyosmani/whats-new-in-chrome-devtools "What's new in Chrome DevTools? // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome開発者ツールの新しい機能についてのスライド

----

## Javascript Unit Testing - Early Release - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920042594.do](http://shop.oreilly.com/product/0636920042594.do "Javascript Unit Testing - Early Release - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span></p>

ユニットテストについてのスクリーンキャスト

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## npmcdn
[npmcdn.com/](https://npmcdn.com/ "npmcdn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

npmにあるものをブラウザで読み込めるように配信するCDN的なサービス

----

## DevTools Challenger
[devtoolschallenger.com/](http://devtoolschallenger.com/ "DevTools Challenger")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firefoxの開発者ツールの使い方についてを学べるサイト。
アニメーション制御やカラーピッカーなどのFirefox 44で新しく追加された機能について扱ってる。

- [Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/11/developer-edition-44-creative-tools-and-more/ "Developer Edition 44: New visual editing and memory management tools ★ Mozilla Hacks – the Web developer blog")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## lepture/vui · GitHub
[github.com/lepture/vui](https://github.com/lepture/vui "lepture/vui · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Vue.jsベースのUIフレームワーク

----

## neal-react - Declarative landing pages for react.js
[www.nealjs.com/](http://www.nealjs.com/ "neal-react - Declarative landing pages for react.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Reactを使ったランディングページでよく使われるUIをまとめたComponent集

----

## Scooter - Welcome to Scooter
[dropbox.github.io/scooter/](http://dropbox.github.io/scooter/ "Scooter - Welcome to Scooter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">dropbox</span> <span class="jser-tag">Sass</span> <span class="jser-tag">library</span></p>

DropboxのSassフレームワーク

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: 確かな力が身につくJavaScript「超」入門 (Informatics &amp; IDEA): 狩野 祐東
[www.amazon.co.jp/dp/4797383585](http://www.amazon.co.jp/dp/4797383585 "Amazon: 確かな力が身につくJavaScript「超」入門 (Informatics & IDEA): 狩野 祐東")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">初心者</span> <span class="jser-tag">book</span></p>

プログラミング初心者向けのJavaScriptについての書籍

- [確かな力が身につくJavaScript「超」入門 | 狩野祐東の本 solidpanda.com](http://www.solidpanda.com/book/title/js-beginner/ "確かな力が身につくJavaScript「超」入門 | 狩野祐東の本 solidpanda.com")

----

## Selenium - O'Reilly Media
[shop.oreilly.com/product/0636920042853.do](http://shop.oreilly.com/product/0636920042853.do "Selenium - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Selenium</span> <span class="jser-tag">book</span></p>

2016年1月発売
Seleniumについての書籍

----
