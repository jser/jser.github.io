---
title: "2015-07-21のJS: TypeScript 1.5、Web Compoents概要、ブラウザの情報源"
author: azu
layout: post
date : 2015-07-21T22:54
category: JSer
tags:
    - TypeScript
    - WebCompoents
    - Browser

---

JSer.info #237 -  [TypeScript 1.5](https://github.com/Microsoft/TypeScript/releases/tag/v1.5.3 "TypeScript 1.5")がリリースされました。

- [Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs](http://blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx "Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs")

新しい機能については[What's new in TypeScript](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-15 "What's new in TypeScript")でまとめられていますが、ES6周りでは modules、destructuring、spread、for/of、symbols、computed properties、let、constなどがサポートされています。

またTypeScriptとしては`--module umd`や`--module system`での出力する種類の追加、`--inlineSourceMap`でインラインSourceMapのサポート、`--experimentalDecorators`のフラグでDecoratorのサポートなどが追加されています。

既存の構文やCompiler APIでの破壊的な変更について以下にまとめられています。

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-15 "Breaking Changes · Microsoft/TypeScript Wiki")
- [API Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/API-Breaking-Changes#typescript-15 "API Breaking Changes · Microsoft/TypeScript Wiki")

-----

[Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog](http://blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/ "Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog")という記事ではWeb Componentsによって何が変わるのかについて詳しく書かれています。

Web Componentsがどういう事を解決してくれるのか、既存の類似実装などの歴史、既存の実装では何を解決出来なかったか、今現在のWeb Componentsの状況などについて書かれています。

また、[Microsoft Edge and Web Components | Microsoft Edge Dev Blog](http://blogs.windows.com/msedgedev/2015/07/15/microsoft-edge-and-web-components/ "Microsoft Edge and Web Components | Microsoft Edge Dev Blog")という記事ではMSEdgeでのWeb Componentsの実装方針について書かれています。

----

先ほどのMSEdgeの話もそうですが、最近ではブラウザベンダーが色々な情報を発信しています。

公式の情報だけに絞っても、色々な場所に書かれているのでどこを探せばいいのかは結構難しいです。

そういった公式の情報源についてを[azu/browser-javascript-resource](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource")にまとめてみました。

- [ブラウザ毎のリリースノートや実装状況はどこを見ればいいかをまとめました | Web Scratch](http://efcl.info/2015/07/21/browser-javascript-resource/ "ブラウザ毎のリリースノートや実装状況はどこを見ればいいかをまとめました | Web Scratch")

[変化を作ってる人が集まる場所には情報が集まる](http://azu.github.io/slide/jser200/javascript-2014.html)ので、ブラウザベンダーが発信してる情報だけ見ても、かなり幅広いことが分かると思います。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## V8 JavaScript Engine: V8 4.5 release
[v8project.blogspot.com/2015/07/v8-45-release.html](http://v8project.blogspot.com/2015/07/v8-45-release.html "V8 JavaScript Engine: V8 4.5 release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.5(Chrome 45)リリース。
Array Function、Array/TypedArrayのメソッド追加、Object.assign、最適化コンパイラのTurboFan、V8 APIの変更など

----

## ESLint 1.0.0-rc-1 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/07/eslint-1.0.0-rc-1-released](http://eslint.org/blog/2015/07/eslint-1.0.0-rc-1-released "ESLint 1.0.0-rc-1 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 1.0.0-rc-1リリース。
`--reset`がデフォルトになり、ES6の対応改善、新しいルールの追加など

- [Documentation - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/1.0.0/user-guide/migrating-to-1.0.0 "Documentation - ESLint - Pluggable JavaScript linter")

----

## Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx](http://blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx "Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.5リリース。
modulesやdestructuring等ES6の対応改善、tsconfig.jsonによるプロジェクト設定、Decoratorを`--experimentalDecorators`フラグで試験的サポートなど

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#15 "Roadmap · Microsoft/TypeScript Wiki")

----

## node-browserify/changelog.markdown at master · substack/node-browserify
[github.com/substack/node-browserify/blob/master/changelog.markdown#1100](https://github.com/substack/node-browserify/blob/master/changelog.markdown#1100 "node-browserify/changelog.markdown at master · substack/node-browserify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 11.0.0リリース。
ブラウザ向けの`stream`として使うreadable-streamをアップデートしStreams3ベースに変更。
ブラウザ向け`http`モジュールをFetch APIをベースとしたstream-httpへ変更しstreamをサポートできるように

- [nodejs/readable-stream](https://github.com/nodejs/readable-stream "nodejs/readable-stream")
- [jhiesey/stream-http](https://github.com/jhiesey/stream-http "jhiesey/stream-http")

----
<h1 class="site-genre">アーティクル</h1>

----

## Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/](http://blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/ "Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">MSEdge</span> <span class="jser-tag">browser</span></p>

WebComponentsについての詳しい解説。
何を目的にしているか、関連するコンポーネント実装の歴史。
CSSスタイルのisolation、スタイルのスコープ、Global object isolation、iframeには欠けている部分についてなど

----

## Socket.IO — Socket.IO P2P
[socket.io/blog/socket.io-p2p/#](http://socket.io/blog/socket.io-p2p/# "Socket.IO — Socket.IO P2P")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">p2p</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Socket.IOからWebRTCを利用してP2Pでの通信を行えるように

----

## Comprehensive Beginner&#x27;s Guide To ReactJS - AntJanus
[antjanus.com/blog/web-development-tutorials/front-end-development/comprehensive-beginners-guide-to-reactjs/](http://antjanus.com/blog/web-development-tutorials/front-end-development/comprehensive-beginners-guide-to-reactjs/ "Comprehensive Beginner&#x27;s Guide To ReactJS - AntJanus")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">React</span></p>

AngularJSユーザ向けのReact入門ガイド

----

## How to Debug JavaScript Remotely With Vorlon.js - Tuts+ Code Tutorial
[code.tutsplus.com/tutorials/how-to-debug-javascript-remotely-with-vorlonjs--cms-24343](http://code.tutsplus.com/tutorials/how-to-debug-javascript-remotely-with-vorlonjs--cms-24343 "How to Debug JavaScript Remotely With Vorlon.js - Tuts+ Code Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">tutorial</span></p>

Vorlon.jsを使ったJavaScriptのリモートデバッグについて

----

## ES6 In Depth: Proxies ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/07/es6-in-depth-proxies-and-reflect/](https://hacks.mozilla.org/2015/07/es6-in-depth-proxies-and-reflect/ "ES6 In Depth: Proxies ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Proxy APIについての解説。
Proxyで扱える14コのhandler、Proxyの使いどころ、Revocable proxiesについてなど。
"オブジェクトはプロパティのコレクションである"といえるかどうかの話

----

## StrongLoop | An Introduction to JavaScript ES6 Iterators
[strongloop.com/strongblog/introduction-to-es6-iterators/](https://strongloop.com/strongblog/introduction-to-es6-iterators/ "StrongLoop | An Introduction to JavaScript ES6 Iterators")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Iteratorについての解説。
for-ofとfor-inの違い、Symbol.iteratorを使って定義する方法とそれを利用する方法について

----

## azu/browser-javascript-resource
[github.com/azu/browser-javascript-resource](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">blog</span> <span class="jser-tag">まとめ</span></p>

IEやFirefoxなどブラウザごとのリリースノートや更新履歴、実装状況、バグレポートの方法などをまとめたもの

- [ブラウザ毎のリリースノートや実装状況はどこを見ればいいかをまとめました | Web Scratch](http://efcl.info/2015/07/21/browser-javascript-resource/ "ブラウザ毎のリリースノートや実装状況はどこを見ればいいかをまとめました | Web Scratch")

----

## 知らないと損するSassの組み込み関数徹底解剖 | Yuhiisk
[blog.yuhiisk.com/archive/2015/07/14/sass-built-in-functions.html](http://blog.yuhiisk.com/archive/2015/07/14/sass-built-in-functions.html "知らないと損するSassの組み込み関数徹底解剖 | Yuhiisk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">リファレンス</span></p>

Sassの関数まとめ

----

## Flux in Depth. Store and Network Communication. – Minko Gechev&#x27;s blog
[blog.mgechev.com/2015/07/18/flux-in-depth-store-network-communication-services](http://blog.mgechev.com/2015/07/18/flux-in-depth-store-network-communication-services "Flux in Depth. Store and Network Communication. – Minko Gechev&#x27;s blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

Fluxからネットワークを含めたデータフローについて。
Store -> View、View -> Storeまでの流れ、モデルとStateの分離。
Network -> UI、UI -> Networkのパターンについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## An Introduction to Browser Rendering - YouTube
[www.youtube.com/watch?v=n1cKlKM3jYI](https://www.youtube.com/watch?v=n1cKlKM3jYI "An Introduction to Browser Rendering - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">動画</span></p>

ブラウザのレンダリングフローについてのスクリーンキャスト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## nikgraf/belle
[github.com/nikgraf/belle/](https://github.com/nikgraf/belle/ "nikgraf/belle")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

React Componentとして使えるUI集。
外からJSを経由してコンポーネントに対してスタイルを設定出来るようになっている。

----

## ipselon/react-ui-builder
[github.com/ipselon/react-ui-builder](https://github.com/ipselon/react-ui-builder "ipselon/react-ui-builder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span></p>

React ComponentをGUIで配置したり、配置したものからReactのコードを吐き出したりして、GUIでコードを編集、プレビューなど出来るツール。
ツール自体がReactとProxyからできていて面白い

----
<h1 class="site-genre">書籍関係</h1>

----

## DrBoolean/mostly-adequate-guide
[github.com/DrBoolean/mostly-adequate-guide](https://github.com/DrBoolean/mostly-adequate-guide "DrBoolean/mostly-adequate-guide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptでの関数型プログラミングについての無料の書籍

----

## JavaScript Regular Expressions - O&#x27;Reilly Media
[shop.oreilly.com/product/9781783282258.do](http://shop.oreilly.com/product/9781783282258.do "JavaScript Regular Expressions - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span> <span class="jser-tag">book</span></p>

JavaScriptの正規表現についての書籍

----
