---
title: "2016-05-30のJS: 初めてのnpm publish、Node.jsでのメモリリークデバッグ"
author: azu
layout: post
date : 2016-05-30T20:41
category: JSer
tags:
    - npm
    - V8
    - Node.js
    - memory
    - debug

---

JSer.info #281　[Publishing Your First Package to npm](https://eladnava.com/publishing-your-first-package-to-npm/)という記事では、npmにパッケージを公開する流れが紹介されています。

まだ`npm publish`したことがない人はチュートリアルを見ながらやってみるといいかもしれません。
グローバルな名前空間を使うのに気が引ける場合はScoped Modulesとして公開してみるといいかもしれません。
(`package.json`の`name`を`@<npmユーザ名>/<パッケージ名`とするだけです)

- [npmで名前空間を持ったモジュールを公開する方法(scoped modules) | Web Scratch](http://efcl.info/2015/04/30/npm-namespace/)

-----

[Node.jsでのJavaScriptメモリリークを発見するための簡単ガイド | プログラミング | POSTD](http://postd.cc/simple-guide-to-finding-a-javascript-memory-leak-in-node-js/)は[Simple Guide to Finding a JavaScript Memory Leak in Node.js](http://www.alexkras.com/simple-guide-to-finding-a-javascript-memory-leak-in-node-js/ "Simple Guide to Finding a JavaScript Memory Leak in Node.js")の翻訳記事ですが、Node.jsでのメモリリークの見つけ方や確認方法についてです。

JavaScriptライブラリはブラウザ向けでもNode.jsで動くように書くことが多い(テスト楽)ので、
Node.js向けの方法ですが適応できる範囲は結構広いので知っておくといいことが多いです。

- 最近まさに`global.gc()`と`process.memoryUsage()`を使ってメモリリークのテストをブラウザ向けのライブラリでやりました
- [perf(test): add memory leak testing by azu · Pull Request #33 · almin/almin](https://github.com/almin/almin/pull/33 "perf(test): add memory leak testing by azu · Pull Request #33 · almin/almin")

GCとHeapダンプの取り方はブラウザの開発者ツールでも同様の事ができます。
また、Node.jsをChromeの開発者ツールでリモートデバッグする機能がPull Requestされています。

- [Add v8_inspector support by ofrobots · Pull Request #6792 · nodejs/node](https://github.com/nodejs/node/pull/6792)
- [V8, modern JavaScript, and beyond - Google I/O 2016 - YouTube](https://www.youtube.com/watch?v=N1swY14jiKc)

----


----
<h1 class="site-genre">ヘッドライン</h1>

----

## Deco - React Native IDE
[www.decosoftware.com/may-2016-update](https://www.decosoftware.com/may-2016-update "Deco - React Native IDE")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">editor</span> <span class="jser-tag">ReleaseNote</span></p>

React Native IDEであるDecoがオープンソースとしてリリースされた

----

## ESLint v2.11.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/05/eslint-v2.11.0-released](http://eslint.org/blog/2016/05/eslint-v2.11.0-released "ESLint v2.11.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.11.0リリース。
JSCS互換のルールの追加、`obj.hasOwnProperty`の利用に関するルールの追加など

- [ESLint v2.11.0 - Qiita](http://qiita.com/mysticatea/items/979bee6cd462f135f217 "ESLint v2.11.0 - Qiita")
- [Suggestion: Object.hasOwnProperty](https://esdiscuss.org/topic/suggestion-object-hasownproperty "Suggestion: Object.hasOwnProperty")

----

## Release Notes for Safari Technology Preview 5 | WebKit
[webkit.org/blog/6415/release-notes-for-safari-technology-preview-5/](https://webkit.org/blog/6415/release-notes-for-safari-technology-preview-5/ "Release Notes for Safari Technology Preview 5 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 5リリース。
`NodeList`がiterableに、`window.scroll`が`ScrollToOptions`をサポート、sourceMappingURLが相対パスを扱えない問題を修正など

----
<h1 class="site-genre">アーティクル</h1>

----

## Publishing Your First Package to npm
[eladnava.com/publishing-your-first-package-to-npm/](https://eladnava.com/publishing-your-first-package-to-npm/ "Publishing Your First Package to npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">tutorial</span></p>

npmでパッケージを公開するまでの流れを書いたチュートリアル

----

## Fullstack React : React Tutorial: Cloning Yelp
[www.fullstackreact.com/articles/react-tutorial-cloning-yelp/](https://www.fullstackreact.com/articles/react-tutorial-cloning-yelp/ "Fullstack React : React Tutorial: Cloning Yelp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

YelpのクローンをReactで作るチュートリアル

----

## IntersectionObserverを使ってlazyload-imageを書き直した - 1000ch.net
[1000ch.net/posts/2016/intersection-observer-lazyload.html](https://1000ch.net/posts/2016/intersection-observer-lazyload.html "IntersectionObserverを使ってlazyload-imageを書き直した - 1000ch.net")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span></p>

`IntersectionObserver`を使った画像の遅延ロードの実装について。
fallbackはただの`<img>`として動作する

----

## [翻訳] Airbnb React/JSX Style Guide - Qiita
[qiita.com/koukun/items/e64762e407b8dd5e0247](http://qiita.com/koukun/items/e64762e407b8dd5e0247 "\[翻訳\] Airbnb React/JSX Style Guide - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">翻訳</span></p>

Airbnb React/JSXのコーディングスタイルガイドの翻訳

----

## RxJS の代わりに xstream を使う - Qiita
[qiita.com/masakielastic/items/f34f5b297abee0e80ddc](http://qiita.com/masakielastic/items/f34f5b297abee0e80ddc "RxJS の代わりに xstream を使う - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span></p>

RxライクなStreamライブラリであるxstreamについて

- [staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript](https://github.com/staltz/xstream "staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript")

----

## React/Redux Introduction // Speaker Deck
[speakerdeck.com/adwd/redux-introduction](https://speakerdeck.com/adwd/redux-introduction "React/Redux Introduction // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">スライド</span></p>

React/ReduxでTodo的アプリを作る話。
チュートリアル的な内容のスライド

----

## Implementing a Stepping Debugger in JavaScript
[jlongster.com/Implementing-Stepping-Debugger-JavaScript](http://jlongster.com/Implementing-Stepping-Debugger-JavaScript "Implementing a Stepping Debugger in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span></p>

JavaScriptをステップ実行できるエディタをどうやって実装するか。
regeneratorとステートマシーン、コールスタックの実装、ブレークポイントの対応など

- [jlongster/unwinder: An implementation of continuations in JavaScript](https://github.com/jlongster/unwinder "jlongster/unwinder: An implementation of continuations in JavaScript")

----

## Testing Your Style With ESLint and Mocha
[robots.thoughtbot.com/testing-your-style-with-eslint-and-mocha](https://robots.thoughtbot.com/testing-your-style-with-eslint-and-mocha "Testing Your Style With ESLint and Mocha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span></p>

ESLintをMochaのテストとして動かす話

----

## npm-scripts でクロスプラットフォームに環境変数を参照するための npm を作成してみた – アカベコマイリ
[akabeko.me/blog/2016/05/cross-conf-env-1-0-release/](http://akabeko.me/blog/2016/05/cross-conf-env-1-0-release/ "npm-scripts でクロスプラットフォームに環境変数を参照するための npm を作成してみた – アカベコマイリ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

`packge.json`の`config` fieldに環境変数を定義して、それをクロスプラットフォームで利用できるようにするツール

----

## Understanding ASTs by Building Your Own Babel Plugin
[www.sitepoint.com/understanding-asts-building-babel-plugin/](https://www.sitepoint.com/understanding-asts-building-babel-plugin/ "Understanding ASTs by Building Your Own Babel Plugin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">AST</span></p>

Babelプラグインを書きながらASTについて学ぶチュートリアル

----

## Announcing React Server - @Redfin
[www.redfin.com/blog/2016/05/announcing-react-server.html](https://www.redfin.com/blog/2016/05/announcing-react-server.html "Announcing React Server - @Redfin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サーバー</span></p>

Reactのサーバサイドレンダリングを行うためのフレームワーク

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Node Conf London 2016 - YouTube
[www.youtube.com/playlist?list=PL0CdgOSSGlBYnHAl\_DZoy9BWvdVQjNKE2](https://www.youtube.com/playlist?list=PL0CdgOSSGlBYnHAl_DZoy9BWvdVQjNKE2 "Node Conf London 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

Node Conf London 2016 の動画まとめ

- [NodeConf London 2016](http://london.nodeconf.com/ "NodeConf London 2016")

----

## JSConfUY 2016 - YouTube
[www.youtube.com/user/jsconfuy](https://www.youtube.com/user/jsconfuy "JSConfUY 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

JSConf Uruguay 2016の動画まとめ

- [JSConf Uruguay 2016 - Montevideo, April 15th-16th](https://jsconf.uy/ "JSConf Uruguay 2016 - Montevideo, April 15th-16th")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## tonyganch/gonzales-pe: CSS parser with support of preprocessors
[github.com/tonyganch/gonzales-pe](https://github.com/tonyganch/gonzales-pe "tonyganch/gonzales-pe: CSS parser with support of preprocessors")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

CSS Parserライブラリ。
CSS/less/Sassをサポートしてる

----

## QuorraJS
[quorrajs.org/](https://quorrajs.org/ "QuorraJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

LaravelインスパイアなNode.jsフレームワーク

- [Introducing QuorraJS — Medium](https://medium.com/@quorrajs/we-are-just-getting-started-f6593e4ae06b "Introducing QuorraJS — Medium")

----

## ALM Tools for TypeScript
[alm.tools/](http://alm.tools/ "ALM Tools for TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">editor</span></p>

ブラウザで動くTypeScriptエディタ

----
<h1 class="site-genre">書籍関係</h1>

----

## 初めてのThree.js 第2版 : Jos Dirksen, あんどうやすし : 本 : Amazon.co.jp
[www.amazon.co.jp/%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AEThree-js-%E7%AC%AC2%E7%89%88-Jos-Dirksen/dp/4873117704](http://www.amazon.co.jp/%E5%88%9D%E3%82%81%E3%81%A6%E3%81%AEThree-js-%E7%AC%AC2%E7%89%88-Jos-Dirksen/dp/4873117704 "初めてのThree.js 第2版 : Jos Dirksen, あんどうやすし : 本 : Amazon.co.jp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">翻訳</span></p>

2016年7月25日発売
Three.js本

----
