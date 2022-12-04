---
title: "2018-02-27のJS: webpack 4、プロファイルとパフォーマンス改善、KeyboardEvent.keyCodeの問題"
author: "azu"
layout: post
date : 2018-02-27T02:15:36.179Z
category: JSer
tags:
- webpack
- performance
- keyboard

---

JSer.info #372 - webpack 4が正式リリースされました。

- [🎼webpack 4: released today!!✨ – webpack – Medium](https://medium.com/webpack/webpack-4-released-today-6cdb994702d4)
- [Release v4.0.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v4.0.0)

ビルドパフォーマンスの改善、`mode`オプションの追加、`CommonsChunkPlugin`を廃止し代わりに`optimize`オプションの追加、`.wasm`、`.mjs`などをEntry Pointとしてサポートなどが行われています。

新しいプラグインシステムが導入され、plugin/loader周りに破壊的な変更が行われています。
まだ、いくつかのplugin/loaderは4.xには対応していないものもあります。

plugin/loader作者向けのマイグレーションガイドは次の記事で公開されています。

- [webpack 4: migration guide for plugins/loaders – webpack – Medium](https://medium.com/webpack/webpack-4-migration-guide-for-plugins-loaders-20a79b927202 "webpack 4: migration guide for plugins/loaders – webpack – Medium")

----

[Maybe you don't need Rust and WASM to speed up your JS](https://mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-to-speed-up-your-js.html "Maybe you don&#39;t need Rust and WASM to speed up your JS")という記事では、[@mraleph](https://twitter.com/mraleph "@mraleph")さんがプロファイルを取りながらパフォーマンス改善を行うことについてを[mozilla/source-map](https://github.com/mozilla/source-map "mozilla/source-map")を例に解説しています。

最近、[mozilla/source-map](https://github.com/mozilla/source-map "mozilla/source-map")は作者である[@fitzgen](https://twitter.com/fitzgen "@fitzgen")さんによってWebAssembly + Rustに書き換えられパフォーマンスが改善されました。これについては次の記事で解説されています。

- [Oxidizing Source Maps with Rust and WebAssembly – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/01/oxidizing-source-maps-with-rust-and-webassembly/ "Oxidizing Source Maps with Rust and WebAssembly – Mozilla Hacks – the Web developer blog")

しかし[@mraleph](https://twitter.com/mraleph "@mraleph")さんは、元となったJavaScript版での改善の余地について分析し、JavaScript版を元に改善のアプローチを3つのグループに分けて解説しています。
この記事では`d8`(V8)や`perf`を使ったプロファイルを取りながら、言語やV8の実装など深いところまで見ていく形になっています。

また、この記事に対して[@fitzgen](https://twitter.com/fitzgen "@fitzgen")さんが[Speed Without Wizardry](http://fitzgeraldnick.com/2018/02/26/speed-without-wizardry.html "Speed Without Wizardry")というレスポンス記事を書いているので併せて読むと良さそうです。

----

[KeyboardEvent.keyCodeとは何か - WebStudio](https://d-toybox.com/studio/lib/what_is_keyCode.html "KeyboardEvent.keyCodeとは何か - WebStudio")という記事では`KeyboardEvent.keyCode`の歴史や問題点について書かれています。

`KeyboardEvent.keyCode`はブラウザやOS間で互換性の問題があり、また標準仕様がない問題について書かれています。
`keyCode`の代わりに[KeyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key "KeyboardEvent.key")や[KeyboardEvent.code](https://developer.mozilla.org/ja/docs/Web/API/KeyboardEvent/code "KeyboardEvent.code")など仕様化されたものがあります。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## jest/CHANGELOG.md at v22.4.0 · facebook/jest
[github.com/facebook/jest/blob/v22.4.0/CHANGELOG.md](https://github.com/facebook/jest/blob/v22.4.0/CHANGELOG.md "jest/CHANGELOG.md at v22.4.0 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 22.4.0リリース。


----

## nohoist in Workspaces | Yarn Blog
[yarnpkg.com/blog/2018/02/15/nohoist/](https://yarnpkg.com/blog/2018/02/15/nohoist/ "nohoist in Workspaces | Yarn Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span></p>

yarn workspaceの`nohoist`オプションについての解説


----

## Release v1.1.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.1.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.1.0 "Release v1.1.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 1.1.0リリース。
Chromium 66.0.3348.0に更新、`BrowserFetcher`、`page.waitForXPath`のサポート。
`frame`周りのイベントサポートの追加など


----

## Release electron v2.0.0-beta.1 · electron/electron
[github.com/electron/electron/releases/tag/v2.0.0-beta.1](https://github.com/electron/electron/releases/tag/v2.0.0-beta.1 "Release electron v2.0.0-beta.1 · electron/electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron v2.0.0-beta.1リリース。
Chrome 61.0.3163.10、Node 8.9.3に更新。
非推奨のAPIの削除、`window.loadFile`のサポート、Macでin-app purchaseのサポートなど


----

## Node v9.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v9.6.0/](https://nodejs.org/en/blog/release/v9.6.0/ "Node v9.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v9.6.0リリース。
`asyncResource.emit{Before,After}`が非推奨となり`asyncResource.runInAsyncScope`を代わりに追加。
Dynamic Importのサポート、`vm`モジュールがES Moduleをサポート、


----

## Release almin@0.16.0 · almin/almin
[github.com/almin/almin/releases/tag/almin%400.16.0](https://github.com/almin/almin/releases/tag/almin%400.16.0 "Release almin@0.16.0 · almin/almin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">almin</span> <span class="jser-tag">ReleaseNote</span></p>

almin 0.16.0リリース。
`Context`の`dispatcher`がオプショナルな引数に変更、`almin-react-container`のバグ修正など


----

## 🎼webpack 4: released today!!✨ – webpack – Medium
[medium.com/webpack/webpack-4-released-today-6cdb994702d4](https://medium.com/webpack/webpack-4-released-today-6cdb994702d4 "🎼webpack 4: released today!!✨ – webpack – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">opinion</span></p>

webpack 4リリース。
ビルドパフォーマンスの改善、`mode`オプションの追加、`CommonsChunkPlugin`の代わりに`optimize`オプションの追加、`.wasm`、`.mjs`のサポートなど。
新しいプラグインシステムが導入され、plugin/loader周りに破壊的な変更が行われている。

- [Release v4.0.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v4.0.0 "Release v4.0.0 · webpack/webpack")
- [webpack 4: mode and optimization – webpack – Medium](https://medium.com/webpack/webpack-4-mode-and-optimization-5423a6bc597a "webpack 4: mode and optimization – webpack – Medium")
- [webpack 4: migration guide for plugins/loaders – webpack – Medium](https://medium.com/webpack/webpack-4-migration-guide-for-plugins-loaders-20a79b927202 "webpack 4: migration guide for plugins/loaders – webpack – Medium")
- [Webpack 4.0 Release: What&#39;s New?](https://auth0.com/blog/webpack-4-release-what-is-new/ "Webpack 4.0 Release: What&amp;#39;s New?")

----

## Release v5.7.0 · npm/npm
[github.com/npm/npm/releases/tag/v5.7.0](https://github.com/npm/npm/releases/tag/v5.7.0 "Release v5.7.0 · npm/npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 5.7プレリリース。
package-lockのgit merge conflictを解決する`npm-merge-driver`の公開、
常にlock-fileのみを参照する`npm ci`コマンドの追加など。
5.7.0には`sudo`利用時に問題があるため、5.7.1がリリースされている。

- [npm-merge-driver](https://www.npmjs.com/package/npm-merge-driver "npm-merge-driver")

----
<h1 class="site-genre">アーティクル</h1>

----

## Using Promise.prototype.finally in Node.js | www.thecodebarbarian.com
[thecodebarbarian.com/using-promise-finally-in-node-js.html](http://thecodebarbarian.com/using-promise-finally-in-node-js.html "Using Promise.prototype.finally in Node.js | www.thecodebarbarian.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

`Promise#finally`についての記事。
Promiseの状態遷移や`finally`の動作について。また`finally`のハンドラでエラーが起きた際の動作について


----

## Measuring the Impact of 3rd-Party Tags with WebPageTest - Andy Davies
[andydavies.me/blog/2018/02/19/using-webpagetest-to-measure-the-impact-of-3rd-party-tags/](http://andydavies.me/blog/2018/02/19/using-webpagetest-to-measure-the-impact-of-3rd-party-tags/ "Measuring the Impact of 3rd-Party Tags with WebPageTest - Andy Davies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

WebPageTestを使ってサードパーティスクリプトがロードパフォーマンスにどのような影響を与えているかを比較する方法について。
特定のリクエストをブロックした結果と比較する方法について


----

## KeyboardEvent.keyCodeとは何か - WebStudio
[d-toybox.com/studio/lib/what\_is\_keyCode.html](https://d-toybox.com/studio/lib/what_is_keyCode.html "KeyboardEvent.keyCodeとは何か - WebStudio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">キーボード</span> <span class="jser-tag">article</span></p>

`KeyboardEvent.keyCode`の歴史や実装について。 `keyCode`はOSやブラウザ間で問題があり標準化もされていないため、`key`や`code`を代わりに使うべきという話。


----

## Maybe you don't need Rust and WASM to speed up your JS
[mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-to-speed-up-your-js.html](https://mrale.ph/blog/2018/02/03/maybe-you-dont-need-rust-to-speed-up-your-js.html "Maybe you don't need Rust and WASM to speed up your JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

プロファイルを取りながらパフォーマンスを改善していく話。 Rust + wasmで書き直されたSource Mapライブラリを例に、JS版でのボトルネックを調べ改善していく話。 アルゴリズムの改善、言語に依存する問題、実装に依存する問題について


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ECMAScriptの使い方
[azu.github.io/slide/2018/node/ecmascript39.html](http://azu.github.io/slide/2018/node/ecmascript39.html "ECMAScriptの使い方")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

ECMAScriptのバージョンの歴史、なぜES2016以降の策定プロセスを変更したのかについて。
各ブラウザ実装の比較、仕様やプロポーザルの調べ方や利用方法について


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Wedgetail
[wedgetail.js.org/index.html](https://wedgetail.js.org/index.html "Wedgetail")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">testing</span></p>

コードの実行時間が期待値かをテストするライブラリ。 low、hight、averageを指定しコードの実行時間のテストを行える。 またパーセンタイルに対応している。


----

## theia-ide/theia: Theia is a cloud & desktop IDE framework implemented in TypeScript.
[github.com/theia-ide/theia](https://github.com/theia-ide/theia "theia-ide/theia: Theia is a cloud & desktop IDE framework implemented in TypeScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">editor</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Electron</span></p>

monaco-editorベースのCould IDE、Desktop IDE。

- [Microsoft/monaco-editor: A browser based code editor](https://github.com/Microsoft/monaco-editor "Microsoft/monaco-editor: A browser based code editor")

----
<h1 class="site-genre">書籍関係</h1>

----

## Exploring ES2018 and ES2019
[exploringjs.com/es2018-es2019/](http://exploringjs.com/es2018-es2019/ "Exploring ES2018 and ES2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

Exploring ES2018 and ES2019が公開された


----
