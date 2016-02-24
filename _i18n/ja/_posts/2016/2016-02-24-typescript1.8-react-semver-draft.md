---
title: "2016-02-24のJS: TypeScript 1.8、Reactのバージョニング、Draft.js"
author: azu
layout: post
date : 2016-02-24T10:11
category: JSer
tags:
    - TypeScript
    - React

---

JSer.info #267 - [TypeScript 1.8](https://blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/ "TypeScript 1.8")が正式リリースされました。

- [Release v1.8.2 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/releases/tag/v1.8.2 "Release v1.8.2 · Microsoft/TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-18 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

JavaScriptファイルをTypeScriptプロジェクトに含めやすくする[--allowJs](https://github.com/Microsoft/TypeScript/wiki/What's-new-in-TypeScript#including-js-files-with---allowjs "--allowJs")オプションやTypeScriptファイルをそのまま1つのJavaScriptにbundleする機能が追加されています。

また、String Literal Typesの対応やフローコントロールを解析して到達できていないコードの検知などの機能も追加されています。

----

[New Versioning Scheme | React](http://facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html "New Versioning Scheme | React")ではReactの次期バージョンはv15.0.0となることについて書かれています。

いわゆる[Semantic Versioning](http://semver.org/ "Semantic Versioning")の1.0.0以降の方式でアップデートしていくという方針について書かれています。

また、Reactに依存したライブラリにおけるReactバージョンに指定方法についても書かれているので、
React Componentのライブラリを作っている人は参照するといいかもしれません。

![react versioning](http://facebook.github.io/react/img/blog/versioning-6.png)

----

FacebookのNoteやMessengerで使われているReactベースのリッチテキストエディタフレームワークである[Draft.js](https://facebook.github.io/draft-js/ "Draft.js")が公開されています。

Reactでコンポーネントを作る際に、テキストエディタのような仕組みは色々悩みどころが出てくるので、
その辺の仕組みを見てみると面白いかもしれません。

- [Issues and Pitfalls](https://facebook.github.io/draft-js/docs/advanced-topics-issues-and-pitfalls.html#content "Issues and Pitfalls")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v5.7.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.7.0/](https://nodejs.org/en/blog/release/v5.7.0/ "Node v5.7.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.7.0リリース。
`Buffer#fill`が`encoding`引数をサポート、`spawn()`が`shell`オプションをサポートするなど

----

## jQuery 1.12.1 and 2.2.1 Released | Official jQuery Blog
[blog.jquery.com/2016/02/22/jquery-1-12-1-and-2-2-1-released/](http://blog.jquery.com/2016/02/22/jquery-1-12-1-and-2-2-1-released/ "jQuery 1.12.1 and 2.2.1 Released | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 1.12.1と2.2.1リリース
`.position()`のバグを修正

----

## Announcing TypeScript 1.8 | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/](https://blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/ "Announcing TypeScript 1.8 | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.8リリース。
String Literal Typesのサポート、コントロールフローを解析しUnreachableなコードを検出するなど

----

## ESLint v2.2.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/02/eslint-v2.2.0-released](http://eslint.org/blog/2016/02/eslint-v2.2.0-released "ESLint v2.2.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.2.0リリース
`// eslint-disable-next-line`のサポート

----

## Release ES2016 Draft 2016-02-15 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20160215](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20160215 "Release ES2016 Draft 2016-02-15 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2016-02-15リリース。
exponentiation operatorの追加、`Object.prototype`はimmutableに、Unicode 8.0へアップデート、`[[Enumerate]]`と`Reflect.enumerate`の削除など

----

## Release v2.10.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v2.10.0](https://github.com/jscs-dev/node-jscs/releases/tag/v2.10.0 "Release v2.10.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS 2.10.0リリース。
`disallowSpacesInsideTemplateStringPlaceholders`、`requireImportsAlphabetized`の追加

----

## New Versioning Scheme | React
[facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html](http://facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html "New Versioning Scheme | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

Reactの次期バージョンは15.0.0としてリリース予定。
Semver的なバージョニングに合わせるため。また、React ComponentにおけるReactの依存バージョンの書き方についても解説されてる

----
<h1 class="site-genre">アーティクル</h1>

----

## Why using &#x60;_.chain&#x60; is a mistake. — Making Internets — Medium
[medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba "Why using \`\_.chain\` is a mistake. — Making Internets — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

lodashの`_.chanin`は拡張が難しい、lodashに含めることでbundleサイズが大きいという問題がある。
4.1から`lodash/fp`にfunctionalな関数が用意されており、同等の表現はより小さなbundleサイズで実現できるという話

----

## DevTools へのセキュリティ パネル導入について - Google Developers Japan
[googledevjp.blogspot.com/2016/02/draft-devtools.html](http://googledevjp.blogspot.com/2016/02/draft-devtools.html "DevTools へのセキュリティ パネル導入について - Google Developers Japan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome開発者ツールに"Security"パネルが追加された。
TLS証明書、Mixed Contentなどを確認出来る

----

## JavaScript Safe Navigation
[gist.github.com/dakaraphi/6a87168db66fd8f032d2](https://gist.github.com/dakaraphi/6a87168db66fd8f032d2 "JavaScript Safe Navigation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">proxy</span></p>

ProxyとSymbolを使って `?.` 的なプロパティチェインを繋げるように書く実装。
`safe(o).isNull.next.next.$` のように書ける

----

## Aerotwist - The Hack is Back!
[aerotwist.com/blog/the-hack-is-back/](https://aerotwist.com/blog/the-hack-is-back/ "Aerotwist - The Hack is Back!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span></p>

`createImageBitmap`とWebWorkerを使うことで、画像のデコード処理を別スレッドで行う方法について

----

## Delivering Octicons with SVG
[github.com/blog/2112-delivering-octicons-with-svg](https://github.com/blog/2112-delivering-octicons-with-svg "Delivering Octicons with SVG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">SVG</span></p>

GitHubはアイコンフォントをやめて、SVGを使ったアイコンを利用するように切り替えた。
SVGをアイコンとして埋め込む方法、パフォーマンス、欠点や落とし穴について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## talk/webtalk_2016-02-20.pdf at master · momdo/talk
[github.com/momdo/talk/blob/master/webtalk\_2016-02-20.pdf](https://github.com/momdo/talk/blob/master/webtalk_2016-02-20.pdf "talk/webtalk\_2016-02-20.pdf at master · momdo/talk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span> <span class="jser-tag">スライド</span></p>

ウェブの仕様は継続的に更新されているという話。
WHATWG HTMLから見るW3C HTML、CSS SnapshotはCSS WGが安定していると認識したものを記述しているという話について

----

## Google と Udacity による JavaScript Promise オンライン コースのご紹介 - Google Developers Japan
[googledevjp.blogspot.com/2016/02/google-udacity-javascript-promise.html](http://googledevjp.blogspot.com/2016/02/google-udacity-javascript-promise.html "Google と Udacity による JavaScript Promise オンライン コースのご紹介 - Google Developers Japan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promiseに関するオンラインコース

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## npm Discover · see what everyone else is using
[www.npmdiscover.com/](http://www.npmdiscover.com/ "npm Discover · see what everyone else is using")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span> <span class="jser-tag">検索</span></p>

特定のnpmパッケージとよく一緒に使われているものを一覧表示してくれるサイト。
「`react`と一緒に使われているツールやライブラリが何か」という事を検索できる。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## trueadm/inferno: An extremely fast, isomorphic JavaScript library for building modern user interfaces
[github.com/trueadm/inferno](https://github.com/trueadm/inferno "trueadm/inferno: An extremely fast, isomorphic JavaScript library for building modern user interfaces")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

ReactライクなVirtual DOMライブラリ。
テンプレートからVirtual DOM Elementを作る段階で、静的/動的なのかを調べている。
これにより実行時にはdiff/patchを行わないフラグメントを作ることでパフォーマンスの向上を狙っている。

- [What&#x27;s the difference from virtual dom libraries? · Issue #21 · trueadm/inferno](https://github.com/trueadm/inferno/issues/21 "What&#x27;s the difference from virtual dom libraries? · Issue #21 · trueadm/inferno")

----

## ziyasal/scientist.js: A JavaScript interpretation of the Ruby library Scientist, a library for carefully refactoring critical paths.
[github.com/ziyasal/scientist.js](https://github.com/ziyasal/scientist.js "ziyasal/scientist.js: A JavaScript interpretation of the Ruby library Scientist, a library for carefully refactoring critical paths.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

リファクタリングを補助するRubyライブラリであるscienceのJavaScript版

- [trello/scientist: A Node.js library for carefully refactoring critical paths in production](https://github.com/trello/scientist "trello/scientist: A Node.js library for carefully refactoring critical paths in production")
- [github/scientist: A Ruby library for carefully refactoring critical paths.](https://github.com/github/scientist "github/scientist: A Ruby library for carefully refactoring critical paths.")

----

## dthree/cash: Cross-platform Linux commands in pure ES6
[github.com/dthree/cash](https://github.com/dthree/cash "dthree/cash: Cross-platform Linux commands in pure ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

JavaScriptで書かれたLinuxコマンド集。
クロスプラットフォームで動く`mv`や`cp`といった単体のコマンドとしてもインストールできる

----

## Draft.js | Rich Text Editor Framework for React
[facebook.github.io/draft-js/](https://facebook.github.io/draft-js/ "Draft.js | Rich Text Editor Framework for React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">editor</span> <span class="jser-tag">facebook</span> <span class="jser-tag">library</span></p>

Facebook Notesやmessengerで使われてるReactのリッチエディタフレームワーク。
immutable-jsを利用している

----

## ProjectSeptemberInc/gl-react: OpenGL / WebGL bindings for React to implement complex effects over images and content, in the descriptive VDOM paradigm
[github.com/ProjectSeptemberInc/gl-react](https://github.com/ProjectSeptemberInc/gl-react "ProjectSeptemberInc/gl-react: OpenGL / WebGL bindings for React to implement complex effects over images and content, in the descriptive VDOM paradigm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

OpenGL / WebGLを使ったReact Componentライブラリ。

----
<h1 class="site-genre">書籍関係</h1>

----

## Happy Learn JavaScript Tutorial
[www.happylearnjavascripttutorial.com/](http://www.happylearnjavascripttutorial.com/ "Happy Learn JavaScript Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScript楽しく学ぶ目的の書籍

----

## JavaScript-mancy by Jaime González García [PDF/iPad/Kindle]
[leanpub.com/javascriptmancy-mastering-arcane-art-of-writing-awesome-javascript-for-csharp-developers](https://leanpub.com/javascriptmancy-mastering-arcane-art-of-writing-awesome-javascript-for-csharp-developers "JavaScript-mancy by Jaime González García \[PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

C#開発者向けJavaScript本

----
