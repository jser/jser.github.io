---
title: "2017-11-28のJS: Firefox 58の変更点、Emscripten/WebAssembly/Rust"
author: "azu"
layout: post
date : 2017-11-28T00:43:49.054Z
category: JSer
tags:
- firefox
- webassembly
- emscripten

---

JSer.info #359 - [New in Firefox 58: Developer Edition – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/11/new-in-firefox-58-developer-edition/ "New in Firefox 58: Developer Edition – Mozilla Hacks – the Web developer blog")ではFirefox 58(開発版)での変更点について紹介しています。

CSSの`clip-path`を編集できる[CSS shapes highlighter](https://developer.mozilla.org/ja/docs/Tools/Page_Inspector/How_to/Edit_CSS_shapes "CSS shapes highlighter")の追加、デバッガーで著名なフレームワークのスタックトレースが簡潔な表示にでき、また`console.groups`が折りたためるようになるなど。
また、macOSでのWebVRをデフォルトで有効化、FLACのサポート環境の追加、`PerformanceNavigationTiming `のサポート、Budgetベースのバックグラウンドにおける処理の制限追加などが行われています。

----

[WebAssemblyをNodeJS Native Addonの配布形式として使う - Islands in the byte stream](http://gfx.hatenablog.com/entry/2017/11/16/231950 "WebAssemblyをNodeJS Native Addonの配布形式として使う - Islands in the byte stream")という記事では[Emscripten](https://kripken.github.io/emscripten-site/)経由でWebAssemblyを利用する方法について書かれています。

Node.jsではNative addonの仕組みがあるためバインディングを書けばCやC++などで書かれたものも利用できますが、node-gypによるビルドは環境によって問題を起こすことがあります。
ネイティブコードをwasmにビルド済みのものを配布し、各環境でwasmを読み込んで実行することでこの問題を回避するという話を`zopfli`を例にして紹介しています。

----

[dcodeIO/webassembly](https://github.com/dcodeIO/webassembly "dcodeIO/webassembly")は、C/C++で書かれたコードをWebAssemblyに変換して実行できるコンパイラ、ランタイムをもつツールキットです。
[Emscripten](https://kripken.github.io/emscripten-site/)などを使ってC/C++を`.wasm`へビルドできる環境を[自分で設定](https://github.com/azu/emscripten-example)するよりも、最小構成のビルド環境を簡単に作れるようにする目的のツールキットです。

`npm`でインストールすると`.wasm`のビルドに必要なツールも同時にダウンロードしてくれます。

```
# Install
npm install webassembly
# Compile
npx wa compile -o program.wasm program.c
```

Node.jsで`.wasm`ファイルを読み込んで実行できるランタイムも含まれているので、次のように読み込んで実行できます。

```js
// program.js
require("webassembly")
  .load("program.wasm")
  .then(module => {
    console.log("1 + 2 = " + module.exports.add(1, 2));
  });
```

`git clone`して`npm install`するだけで動くサンプルコードは次のリポジトリに用意してあります。

- [azu/webassembly-example: Test https://github.com/dcodeIO/webassembly](https://github.com/azu/webassembly-example "azu/webassembly-example: Test https://github.com/dcodeIO/webassembly")

また、少し話は異なりますがRustがEmscriptenを使わずにWebAssembly(`wasm32-unknown-unknown
`)の出力に対応しました。

- [std: Add a new wasm32-unknown-unknown target by alexcrichton · Pull Request #45905 · rust-lang/rust](https://github.com/rust-lang/rust/pull/45905)
- [rustbuild: Enable WebAssembly backend by default by alexcrichton · Pull Request #46115 · rust-lang/rust](https://github.com/rust-lang/rust/pull/46115)
- [Rust単体でWebAssemblyをコンパイルする（Emscripten無し）](https://sbfl.net/blog/2017/11/27/rust-webassembly-standalone/ "Rust単体でWebAssemblyをコンパイルする（Emscripten無し）")

[Emscripten](https://kripken.github.io/emscripten-site/)を使わずに`.wasm`を扱うことができる環境は増えてきているので、興味がある人は調べてみるといいかもしれません。
WebAssemblyについては次のサイトがWeeklyでニュースレターを更新しています。

- [WebAssembly Weekly · A community-driven weekly newsletter about WebAssembly](http://wasmweekly.news/ "WebAssembly Weekly · A community-driven weekly newsletter about WebAssembly")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md#1140](https://github.com/tmpvar/jsdom/blob/master/Changelog.md#1140 "jsdom/Changelog.md at master · tmpvar/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 11.4.0リリース。
基本的なSVGのサポート、`pretendToBeVisual`オプションの追加、`prepend()/append()/before()/after()/replaceWith()`の追加、`<applet>`要素の削除など


----

## New in Firefox 58: Developer Edition – Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/11/new-in-firefox-58-developer-edition/](https://hacks.mozilla.org/2017/11/new-in-firefox-58-developer-edition/ "New in Firefox 58: Developer Edition – Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 58について。
デバッガーでフレームワークのスタックトレースが簡潔化、`console.groups`が折りたためるように。
また、WebVR(macOS)、FLACのサポート環境の追加、`PerformanceNavigationTiming `のサポート、Budgetベースのバックグラウンドにおける処理の制限追加など

- [budget-based background timeout throttling](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API#Policies_in_place_to_aid_background_page_performance)

----

## Learn Svelte
[svelte.technology/guide#state-management](https://svelte.technology/guide#state-management "Learn Svelte")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

コンパイルできるUIフレームワークのSvelteにStoreが追加された。
ReduxやMobXなどのように`Store`でStateを管理し、変更の監視やcompuate propertyの管理ができる


----
<h1 class="site-genre">アーティクル</h1>

----

## Dynamic import()  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/11/dynamic-import](https://developers.google.com/web/updates/2017/11/dynamic-import "Dynamic import()  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Chrome 63から利用できるDynamic `import()`についての解説


----

## Web Frameworks: Conclusions - Blog | SitePen
[www.sitepen.com/blog/2017/11/10/web-frameworks-conclusions/](https://www.sitepen.com/blog/2017/11/10/web-frameworks-conclusions/ "Web Frameworks: Conclusions - Blog | SitePen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

JavaScriptフレームワークの比較。
強み、弱み、将来性、選ぶ理由について


----

## WebAssemblyをNodeJS Native Addonの配布形式として使う - Islands in the byte stream
[gfx.hatenablog.com/entry/2017/11/16/231950](http://gfx.hatenablog.com/entry/2017/11/16/231950 "WebAssemblyをNodeJS Native Addonの配布形式として使う - Islands in the byte stream")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">WebAssembly</span></p>

Emscriptenを使ってWebAssembl形式にしたNodeモジュールを配布する方法について


----

## Bankai, the friendly web compiler – choo – Medium
[medium.com/choojs/bankai-the-friendly-web-compiler-35f1916679cc](https://medium.com/choojs/bankai-the-friendly-web-compiler-35f1916679cc "Bankai, the friendly web compiler – choo – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Browserifyを使った開発ツールキットについて

- [choojs/bankai: - friendly web compiler](https://github.com/choojs/bankai "choojs/bankai: - friendly web compiler")

----

## JavaScriptのWebGL 2.0でGPGPU - Qiita
[qiita.com/teatime77/items/e867d7d462cb553b373d](https://qiita.com/teatime77/items/e867d7d462cb553b373d "JavaScriptのWebGL 2.0でGPGPU - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">article</span></p>

WebGL 2.0を使ったGPGPUについての解説記事。
WebGL 2.0を使った行列計算や他の実装との比較など


----

## ReactNative 本体のバージョンのアップグレードを行う - Qiita
[qiita.com/hotchpotch/items/5617caccd8749f410631](https://qiita.com/hotchpotch/items/5617caccd8749f410631 "ReactNative 本体のバージョンのアップグレードを行う - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

ReactNativeの0.44.xから0.49.xへのアップグレードについて。
`rn-diff`を使った変更内容のチェック、Xcode関係のアップデート、モジュールのマイグレーション、FlowとReactの型変更の対応などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Introduction to Node.js | edX
[www.edx.org/course/introduction-node-js-microsoft-dev283x](https://www.edx.org/course/introduction-node-js-microsoft-dev283x "Introduction to Node.js | edX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">MS</span> <span class="jser-tag">video</span> <span class="jser-tag">tutorial</span></p>

MicrosoftのNode.js入門講座


----

## Source to Binary - journey of V8 javascript engine // Speaker Deck
[speakerdeck.com/brn/source-to-binary-journey-of-v8-javascript-engine](https://speakerdeck.com/brn/source-to-binary-journey-of-v8-javascript-engine "Source to Binary - journey of V8 javascript engine // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">slide</span></p>

V8がJavaScriptのコードをを実行するフロー、コンパイルパイプラインについてのスライド


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## JSBench.me - JavaScript performance benchmarking playground
[jsbench.me/](https://jsbench.me/ "JSBench.me - JavaScript performance benchmarking playground")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">Tools</span> <span class="jser-tag">webservice</span></p>

JavaScriptのスニペットベンチマークサイト。
jsperfのようにJavaScriptのコードのマイクロベンチマークを取って比較できる


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## y-js/yjs: A framework for real-time p2p shared editing on any data
[github.com/y-js/yjs](https://github.com/y-js/yjs "y-js/yjs: A framework for real-time p2p shared editing on any data")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">p2p</span> <span class="jser-tag">library</span></p>

WebRTC/WebSocktes/XMPPを使ったP2Pでデータのやり取りやテキストの同時編集ができるライブラリ


----

## MikeMcl/big.js: A small, fast JavaScript library for arbitrary-precision decimal arithmetic.
[github.com/MikeMcl/big.js/](https://github.com/MikeMcl/big.js/ "MikeMcl/big.js: A small, fast JavaScript library for arbitrary-precision decimal arithmetic.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Javaの`BigDecimal`のJavaScript実装ライブラリ


----

## asfktz/autodll-webpack-plugin: Webpack's DllPlugin without the boilerplate
[github.com/asfktz/autodll-webpack-plugin](https://github.com/asfktz/autodll-webpack-plugin "asfktz/autodll-webpack-plugin: Webpack's DllPlugin without the boilerplate")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span></p>

webpackのDLLを簡単に扱えるようにするDLLプラグイン。
パッケージの追加や設定の変更をトリガーに再ビルドできる。


----

## aws/aws-amplify: A declarative library for application development using Cloud services with JavaScript
[github.com/aws/aws-amplify](https://github.com/aws/aws-amplify "aws/aws-amplify: A declarative library for application development using Cloud services with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span></p>

AWSとの連携を簡単に行えるライブラリ。認証、Analytics、API、Storageなど。
またReact/React Nativeと連携できるライブラリも公開されている。

- [Announcing AWS Amplify and the AWS Mobile CLI | AWS Mobile Blog](https://aws.amazon.com/jp/blogs/mobile/announcing-aws-amplify-and-the-aws-mobile-cli/ "Announcing AWS Amplify and the AWS Mobile CLI | AWS Mobile Blog")
- [Get Started - AWS Mobile](http://docs.aws.amazon.com/aws-mobile/latest/developerguide/web-getting-started.html "Get Started - AWS Mobile")

----

## z-pattern-matching/z: native pattern matching for javascript
[github.com/z-pattern-matching/z](https://github.com/z-pattern-matching/z "z-pattern-matching/z: native pattern matching for javascript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

パターンマッチライブラリ


----

## imsnif/synp: Convert yarn.lock to package-lock.json and vice versa
[github.com/imsnif/synp](https://github.com/imsnif/synp "imsnif/synp: Convert yarn.lock to package-lock.json and vice versa")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

`yarn.lock`ファイルと`package-lock.json`ファイルを相互変換できるツール。


----

## google/ts-style: ☂️ TypeScript style guide, formatter, and linter.
[github.com/google/ts-style](https://github.com/google/ts-style "google/ts-style: ☂️ TypeScript style guide, formatter, and linter.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">console</span> <span class="jser-tag">google</span></p>

設定不要なコンパイル、コードフォーマット、Lintを行うTypeScript向けのツール。 clang-format、TSLintを利用している。


----

## naver/billboard.js: Re-usable, easy interface JavaScript chart library based on D3 v4+
[github.com/naver/billboard.js](https://github.com/naver/billboard.js "naver/billboard.js: Re-usable, easy interface JavaScript chart library based on D3 v4+")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">d3.js</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">library</span></p>

D3.jsを使ったC3.jsのようなグラフライブラリ。
C3.jsをforkしたライブラリで、D3.js v4を使いC3.jsとの互換性を持っている


----

## dcodeIO/webassembly: A minimal toolkit and runtime to produce and run WebAssembly modules.
[github.com/dcodeIO/webassembly](https://github.com/dcodeIO/webassembly "dcodeIO/webassembly: A minimal toolkit and runtime to produce and run WebAssembly modules.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

WebAssemblyのツールキットとランタイム。 wasmへのコンパイルに必要な依存の自動ダウンロードやコンパイルができる。 またwasm向けの`console`や`Mtch`などのバインディングを提供するランタイムも含まれている。


----
<h1 class="site-genre">書籍関係</h1>

----

## ちゃんと使える力を身につける　JavaScriptのきほんのきほん | 大澤 文孝 | 工学 | Kindleストア | Amazon
[www.amazon.co.jp/%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E4%BD%BF%E3%81%88%E3%82%8B%E5%8A%9B%E3%82%92%E8%BA%AB%E3%81%AB%E3%81%A4%E3%81%91%E3%82%8B-JavaScript%E3%81%AE%E3%81%8D%E3%81%BB%E3%82%93%E3%81%AE%E3%81%8D%E3%81%BB%E3%82%93-%E5%A4%A7%E6%BE%A4-%E6%96%87%E5%AD%9D-ebook/dp/B0779R1R3P](https://www.amazon.co.jp/%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E4%BD%BF%E3%81%88%E3%82%8B%E5%8A%9B%E3%82%92%E8%BA%AB%E3%81%AB%E3%81%A4%E3%81%91%E3%82%8B-JavaScript%E3%81%AE%E3%81%8D%E3%81%BB%E3%82%93%E3%81%AE%E3%81%8D%E3%81%BB%E3%82%93-%E5%A4%A7%E6%BE%A4-%E6%96%87%E5%AD%9D-ebook/dp/B0779R1R3P "ちゃんと使える力を身につける　JavaScriptのきほんのきほん | 大澤 文孝 | 工学 | Kindleストア | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

プログラミング入門者向けのJavaScript入門書


----
