---
title: "2022-06-28のJS: ECMAScript 2022、TypeScript 4.8 Beta、CodeMirror 6"
author: "azu"
layout: post
date : 2022-06-28T03:46:30.520Z
category: JSer
tags:
- React
- ECMAScript
- ESLint
- Angular
- TypeScript

---

JSer.info #598 - ECMAScript 2022が、2022-06のEcma International GA(総会)で承認され、正式にリリースあれました。

- [Ecma International approves new standards - Ecma International](https://www.ecma-international.org/news/ecma-international-approves-new-standards-6/)

ES2022では、クラスにPublic/Privateクラスフィールド、Top-Level await、StringとArrayに`at()`、Error Causeなどが追加されています。追加された機能については、次の記事で解説されています。

- [Ecma International approves ECMAScript 2022: What’s new?](https://2ality.com/2022/06/ecmascript-2022.html)
- [正式仕様リリース！ JavaScriptの最新仕様ES2022で追加された「全」新機能](https://zenn.dev/tonkotsuboy_com/articles/es2022-whats-new)

また、同じくJavaScriptの入門書である[jsprimer](https://jsprimer.net/)もES2022に対応しています。

- [JavaScript Primer 4.0.0: ECMAScript 2022に対応したJS本 | Web Scratch](https://efcl.info/2022/06/19/jsprimer-4/)
- [Release v4.0.0: ES2022 · asciidwango/js-primer](https://github.com/asciidwango/js-primer/releases/tag/v4.0.0)

----

TypeScript 4.8 Betaがリリースされました。

- [Announcing TypeScript 4.8 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-8-beta/)

`unknown`などに関係するコントロールフロー分析の改善、Template String Typesでの`infer`の改善が行われています。
また、`--build`/`-watch`/`--incremental`におけるビルドパフォーマンスの改善、オブジェクトリテラルや配列リテラルを`==`や`===`で比較した場合にエラーとなるように変更されています。
そのほかには、Binding patternの型推論の改善、`--watch`の安定性の改善などが含まれます。

---

[CodeMirror](https://codemirror.net/) 6は、`@codemirror/next`として開発されていましたが、6が`codemirror`のStableバージョンへと変更されました。

- [CodeMirror 6.0](https://marijnhaverbeke.nl/blog/codemirror-6.html)

これによって、`npm install codemirror`で6がインストールされるようになります。
CodeMirror 6は、CodeMirrorを一から書き直しているため、CodeMirror 5以前とは互換性はありません。
CodeMirror 5からのマイグレーションガイドは次のページで公開されています。

- [CodeMirror 5 to 6 Migration Guide](https://codemirror.net/docs/migration/)

また、CodeMirror 6はコアがパッケージとして分かれているため、`codemirror/codemirror`というリポジトリはありません。今までのCodeMirror 5以前が`codemirror/codemirror`というリポジトリでしたが、今回の6がStableとなったことで`codemirror/codemirror5`というリポジトリ名にリネームされました。

- [codemirror/codemirror5: In-browser code editor (version 5, legacy)](https://github.com/codemirror/codemirror5)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Ecma International approves new standards - Ecma International
[www.ecma-international.org/news/ecma-international-approves-new-standards-5/](https://www.ecma-international.org/news/ecma-international-approves-new-standards-5/ "Ecma International approves new standards - Ecma International")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2022、ECMAScript 2022 Internationalization APIが正式にリリースされた。


----

## \[webkit-dev\] WebKit is now on GitHub
[lists.webkit.org/pipermail/webkit-dev/2022-June/032312.html](https://lists.webkit.org/pipermail/webkit-dev/2022-June/032312.html "\[webkit-dev\] WebKit is now on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">Github</span> <span class="jser-tag">news</span></p>

WebKitのリポジトリがGitHubへ移行する

- [WebKit/WebKit: Home of the WebKit project, the browser engine used by Safari, Mail, App Store and many other applications on macOS, iOS and Linux.](https://github.com/WebKit/WebKit "WebKit/WebKit: Home of the WebKit project, the browser engine used by Safari, Mail, App Store and many other applications on macOS, iOS and Linux.")

----

## Announcing React Native 0.69 · React Native
[reactnative.dev/blog/2022/06/21/version-069](https://reactnative.dev/blog/2022/06/21/version-069 "Announcing React Native 0.69 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.69リリース。
React 18のサポート、HermesとReact Native一緒にリリースする方針へ変更など


----

## CodeMirror 6.0
[marijnhaverbeke.nl/blog/codemirror-6.html](https://marijnhaverbeke.nl/blog/codemirror-6.html "CodeMirror 6.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CodeMirror 6がStableリリースされた。
`codemirror`パッケージのStableが6となり、CodeMirror 5のリポジトリはLegacyとなった。

- [codemirror/codemirror5: In-browser code editor (version 5, legacy)](https://github.com/codemirror/codemirror5 "codemirror/codemirror5: In-browser code editor (version 5, legacy)")
- [CodeMirror](https://codemirror.net/ "CodeMirror")

----

## Release 2.5.0 · socketio/socket.io
[github.com/socketio/socket.io/releases/tag/2.5.0](https://github.com/socketio/socket.io/releases/tag/2.5.0 "Release 2.5.0 · socketio/socket.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Socket.IO 2.5.0リリース。
セキュリティ修正として`maxHttpBufferSize`のデフォルト値を100MBから1MBに変更など


----

## Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter
[eslint.org/](https://eslint.org/ "Find and fix problems in your JavaScript code - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">news</span></p>

ESLintのウェブサイトがリニューアルされた


----

## Release Version 14.0.0 · open-source-labs/reactime
[github.com/open-source-labs/reactime/releases/tag/v14.0.0](https://github.com/open-source-labs/reactime/releases/tag/v14.0.0 "Release Version 14.0.0 · open-source-labs/reactime")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">debug</span></p>

State管理のタイムトラベルデバッグツールのReactime v14.0.0リリース。
React Routerのステートをサポートなど


----

## Release v2.0.0 · foliojs/fontkit
[github.com/foliojs/fontkit/releases/tag/v2.0.0](https://github.com/foliojs/fontkit/releases/tag/v2.0.0 "Release v2.0.0 · foliojs/fontkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">browser</span></p>

fontkit v2.0.0リリース。
Node.js特有の機能に対する依存を削除し、ブラウザでも利用できるよう変更。
Bufferの代わりにUint8Array/TextEncoder/TextDecoderを利用するなど


----

## Release v14.0.0 · angular-eslint/angular-eslint
[github.com/angular-eslint/angular-eslint/releases/tag/v14.0.0](https://github.com/angular-eslint/angular-eslint/releases/tag/v14.0.0 "Release v14.0.0 · angular-eslint/angular-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

Angular ESLint v14.0.0リリース。
Angular 14のサポート、Node.js 12のサポート終了、インラインテンプレートをLintする際のVirtual filenameの変更など


----

## Announcing TypeScript 4.8 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-8-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-8-beta/ "Announcing TypeScript 4.8 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.8 Betaリリース。
`unknown`は`{} | null | undefined`と同様になり関連するコントロールフロー分析の改善、Template String Typesでの`infer`の改善。
`--build`/`-watch`/`--incremental`におけるビルドパフォーマンスの改善、オブジェクトリテラルや配列リテラルを`==`や`===`で比較した場合にエラーとなるように。
Binding patternの型推論の改善、`--watch`の安定性の改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## When You Should Prefer Map Over Object In JavaScript
[www.zhenghao.io/posts/object-vs-map](https://www.zhenghao.io/posts/object-vs-map "When You Should Prefer Map Over Object In JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

MapとObjectの使い分けについての記事。
Objectを使うときとObjectの問題、Mapの使い方とMapのベンチマーク。


----

## Sensemaking: Angular without SSR is faster than Next.js with SSR. I have the data.
[alexkrupp.typepad.com/sensemaking/2022/06/angular-without-ssr-is-faster-than-nextjs-with-ssr-i-have-the-data.html](https://alexkrupp.typepad.com/sensemaking/2022/06/angular-without-ssr-is-faster-than-nextjs-with-ssr-i-have-the-data.html "Sensemaking: Angular without SSR is faster than Next.js with SSR. I have the data.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Angular(SSRあり/なし)とNext.jsのショーケースに掲載されているサイトのパフォーマンス計測をして比較した記事。
両方フレームワークのパフォーマンススコアの平均と中央値は大体同じ傾向となったという話


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## astoilkov/main-thread-scheduling: Fast and consistently responsive apps using a single function call
[github.com/astoilkov/main-thread-scheduling](https://github.com/astoilkov/main-thread-scheduling "astoilkov/main-thread-scheduling: Fast and consistently responsive apps using a single function call")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Main Threadでの処理をUIの表示や操作をブロックせずに行うためのスケジューリングライブラリ。
Scheduling APIを意識したAPIとなっている。
`requestIdleCallback()`や`postMessage()`などを使いキューを管理する。
また、`navigator.scheduling.isInputPending()`を使いユーザー入力をブロックしないようにタスクを実行できる。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## timocov/dts-bundle-generator: Tool to generate a single bundle of dts
[github.com/timocov/dts-bundle-generator](https://github.com/timocov/dts-bundle-generator "timocov/dts-bundle-generator: Tool to generate a single bundle of dts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TypeScriptの型定義をbundleするツール


----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript Primer 4.0.0: ECMAScript 2022に対応したJS本 | Web Scratch
[efcl.info/2022/06/19/jsprimer-4/](https://efcl.info/2022/06/19/jsprimer-4/ "JavaScript Primer 4.0.0: ECMAScript 2022に対応したJS本 | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript Primer 4.0.0リリース。
ES2022の対応とSandpackを使ったエディタが組み込まれた。

- [Release v4.0.0: ES2022 · asciidwango/js-primer](https://github.com/asciidwango/js-primer/releases/tag/v4.0.0 "Release v4.0.0: ES2022 · asciidwango/js-primer")

----
