---
title: "2019-01-01のJS: WebdriverIO v5、Rollup 1.0、Rust + WebAssembly + WebWorker"
author: "azu"
layout: post
date : 2018-12-31T13:38:01.421Z
category: JSer
tags:
- Selenium
- rollup
- WebAssembly
- Rust

---

JSer.info #416 - WebDriverを扱うテストフレームワークであるWebdriverIO v5がリリースされました。

- [WebdriverIO v5 Released · WebdriverIO](https://webdriver.io/blog/2018/12/19/webdriverio-v5-released.html)
- [webdriverio/CHANGELOG.md at master · webdriverio/webdriverio](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20)

パッケージ構造やAPI周りの変更が行われています。

基本的なパッケージが[`@wdio`](https://www.npmjs.com/org/@wdio/)に移動され、同梱されていたCLIが`@wdio/cli`に移動しています。

API周りではコマンドがselectorを受け取らないようになり、メソッドチェーンではなくasync/awaitベースに変更されています。

```js
// v4ではセレクタを渡せた
browser.click('#elem')
// v5からはelementを取得してから操作する
const elem = $('#elem')
elem.click()
```

その他にも`isVisible`が`isDisplayed`にリネームされるなど多くのコマンドのリネームが行われています。
詳しくは[CHANGELOG.md](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20)に掲載されています。

----

モジュールBundlerであるRollup v1.0.0がリリースされました。

- [Release v1.0.0 · rollup/rollup](https://github.com/rollup/rollup/releases/tag/v1.0.0)

破壊的な変更として、非推奨となっていたオプションやオプションのリネームが含まれています。
`bundle.generate`と`bundle.write`の返す値のフォーマットの変更、`acorn@6`へアップデートなどが行われています。

- [1.0 changes by guybedford · Pull Request #2293 · rollup/rollup](https://github.com/rollup/rollup/pull/2293)

----

[Comlink + Rust で言語とスレッドの垣根を越えた WebAssembly 開発 - Qiita](https://qiita.com/3846masa/items/92d24e16ebb5151b08ba)という記事では、Zip展開アプリの例にしたRustとWebAssemblyを使った開発について書かれています。

Rustや[wasm-pack](https://rustwasm.github.io/wasm-pack/book/)を使った開発環境の設定から、[wasm-bindgen](https://rustwasm.github.io/wasm-bindgen/)でRust
とJavaScriptのバインディングの作成、webpackでの読み込みとブラウザでの実行についてまで書かれています。
また、メインスレッドで重たい処理を行うのを避けるために、WebAssemblyの処理をWebWorker上で行い、そのメッセージのやり取りに[Comlink](https://github.com/GoogleChromeLabs/comlink)を使う方法などについても紹介されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## WebdriverIO v5 Released · WebdriverIO
[webdriver.io/blog/2018/12/19/webdriverio-v5-released.html](https://webdriver.io/blog/2018/12/19/webdriverio-v5-released.html "WebdriverIO v5 Released · WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Selenium</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v5リリース。
`wdio` CLIは`@wdio/cli`に移動、コマンドがselectorを受け取らないように、メソッドチェーンではなくasync/awaitベースに変更。
その他にもコマンドのリネームなどの破壊的な変更を多く含む

- [webdriverio/CHANGELOG.md at master · webdriverio/webdriverio](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20 "webdriverio/CHANGELOG.md at master · webdriverio/webdriverio")

----

## Release v1.0.0 · rollup/rollup
[github.com/rollup/rollup/releases/tag/v1.0.0](https://github.com/rollup/rollup/releases/tag/v1.0.0 "Release v1.0.0 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup 1.0.0リリース。
破壊的な変更としてオプションのリネーム、`bundle.generate`の返す値のフォーマットの変更、`acorn@6`へアップデートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## 「GraphQL」徹底入門 ─ RESTとの比較、API・フロント双方の実装から学ぶ - エンジニアHub｜若手Webエンジニアのキャリアを考える！
[employment.en-japan.com/engineerhub/entry/2018/12/26/103000](https://employment.en-japan.com/engineerhub/entry/2018/12/26/103000 "「GraphQL」徹底入門 ─ RESTとの比較、API・フロント双方の実装から学ぶ - エンジニアHub｜若手Webエンジニアのキャリアを考える！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

GraphQLの入門記事。
GraphQLの利点、欠点、スキーマ/クエリの書き方、VariableやFragmentの使い方について。
またRelayの拡張や実際にGraphQLを使った実装例についてなど


----

## Understanding Throttling and Debouncing – Bits and Pieces
[blog.bitsrc.io/understanding-throttling-and-debouncing-973131c1ba07](https://blog.bitsrc.io/understanding-throttling-and-debouncing-973131c1ba07 "Understanding Throttling and Debouncing – Bits and Pieces")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ThrottlingとDebouncingについてそれぞれを実装しながら挙動を理解していく記事


----

## Comlink + Rust で言語とスレッドの垣根を越えた WebAssembly 開発 - Qiita
[qiita.com/3846masa/items/92d24e16ebb5151b08ba](https://qiita.com/3846masa/items/92d24e16ebb5151b08ba "Comlink + Rust で言語とスレッドの垣根を越えた WebAssembly 開発 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webworker</span> <span class="jser-tag">Rust</span> <span class="jser-tag">article</span></p>

Rustを使ったWebAssemblyライブラリの開発について。
Rustを使ったwasmのバインディングの作成、webpackを使ったロード方法について。
また、処理をメインスレッド外のWebWorkerで行いComlinkでのデータのやり取りする方法について


----

## Babel 7 の主な変更点まとめ - Qiita
[qiita.com/soarflat/items/21b8955f992bf7d38581](https://qiita.com/soarflat/items/21b8955f992bf7d38581 "Babel 7 の主な変更点まとめ - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babel 7の主な変更点やマイグレーション方法について


----

## 基礎からはじめるReact Native入門連載一覧：CodeZine（コードジン）
[codezine.jp/article/corner/772](https://codezine.jp/article/corner/772 "基礎からはじめるReact Native入門連載一覧：CodeZine（コードジン）")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">tutorial</span></p>

React Nativeについての連載記事。


----

## ECMAScript modules in Node.js: the new plan
[2ality.com/2018/12/nodejs-esm-phases.html](http://2ality.com/2018/12/nodejs-esm-phases.html "ECMAScript modules in Node.js: the new plan")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span> <span class="jser-tag">module</span></p>

Node.jsにおけるES Modulesの扱いについてのまとめ記事。
`.mjs`のサポートについてやCommonJSとの相互運用性の問題、今後どのような方針が予定されているのかについて


----

## JavaScriptとWeb開発に関するInfoQトレンドレポート
[www.infoq.com/jp/articles/javascript-web-development-trends](https://www.infoq.com/jp/articles/javascript-web-development-trends "JavaScriptとWeb開発に関するInfoQトレンドレポート")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

InfoQのJavaScriptに関するトレンドレポート。
イノベーター、アーリーアダプター、アーリーマジョリティ、レイトマジョリティ、ラガードに分けて関連するライブラリ/フレームワーク/ツールについて紹介している。


----

## TypeScriptで実現する型安全な多言語対応（Angularを例に） | 株式会社カブク
[www.kabuku.co.jp/software\_engineer/typescript-angular-i18n/](https://www.kabuku.co.jp/software_engineer/typescript-angular-i18n/ "TypeScriptで実現する型安全な多言語対応（Angularを例に） | 株式会社カブク")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">i18n</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

翻訳ファイルをTypeScriptのコードとして表現することで型安全な翻訳定義を作成する方法について。
翻訳ファイルをコードにするメリットとデメリットについてなど


----

## takefumi-yoshii/react-hooks-ogiri: Advent calendar of 2018. This is a showreel using a reaction hook.
[github.com/takefumi-yoshii/react-hooks-ogiri](https://github.com/takefumi-yoshii/react-hooks-ogiri "takefumi-yoshii/react-hooks-ogiri: Advent calendar of 2018. This is a showreel using a reaction hook.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">example</span> <span class="jser-tag">document</span></p>

React Hooks APIを使ったUIコンポーネントのサンプル実装集

- [React Hooks 大喜利 Advent Calendar 2018 - Qiita](https://qiita.com/advent-calendar/2018/react-hooks-ogiri "React Hooks 大喜利 Advent Calendar 2018 - Qiita")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## FontoXML/fontoxpath: A minimalistic XPath 3.1 implementation in pure JavaScript
[github.com/FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath "FontoXML/fontoxpath: A minimalistic XPath 3.1 implementation in pure JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">xpath</span> <span class="jser-tag">library</span></p>

XPath 3.1、XQuery 3.1の実装ライブラリ


----

## jsincss | A JS-in-CSS stylesheet loader
[jsincss.com/](https://jsincss.com/ "jsincss | A JS-in-CSS stylesheet loader")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

JavaScriptからテンプレートでCSSを生成でき、イベントによってリアクティブにCSSを変更できるライブラリ。
プラグインで拡張できるようになっている。

- [tomhodgins/jsincss: A JS-in-CSS stylesheet loader](https://github.com/tomhodgins/jsincss "tomhodgins/jsincss: A JS-in-CSS stylesheet loader")
- [What is a JIC Stylesheet? - Responsive Style](https://responsive.style/theory/what-is-a-jic-stylesheet.html "What is a JIC Stylesheet? - Responsive Style")

----

## BabelEdit - Editor for JSON translation files for Angular & React
[www.codeandweb.com/babeledit](https://www.codeandweb.com/babeledit "BabelEdit - Editor for JSON translation files for Angular & React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">i18n</span> <span class="jser-tag">React</span> <span class="jser-tag">Angular</span> <span class="jser-tag">software</span></p>

JSONベースの翻訳ファイルエディタ。
AngularやReactとの連携としたワークフローが紹介されている


----
