---
title: "2018-11-27のJS: Web Components入門、React-Reduxの歴史と実装、 HTTP/3 explained"
author: "azu"
layout: post
date : 2018-11-27T02:18:42.009Z
category: JSer
tags:
- WebComponents
- react
- redux
- HTTP3

---

JSer.info #411 - "Lets Build Web Components!"というWeb Componentsについての連載記事が公開されています。

* [Lets Build Web Components! Part 1: The Standards - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-1-the-standards-3e85 "Lets Build Web Components! Part 1: The Standards - DEV Community 👩‍💻👨‍💻")
* [Lets Build Web Components! Part 2: The Polyfills - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-2-the-polyfills-dkh "Lets Build Web Components! Part 2: The Polyfills - DEV Community 👩‍💻👨‍💻")
* [Lets Build Web Components! Part 3: Vanilla Components - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-3-vanilla-components-4on3 "Lets Build Web Components! Part 3: Vanilla Components - DEV Community 👩‍💻👨‍💻")
* [Lets Build Web Components! Part 4: Polymer Library - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-4-polymer-library-4dk2 "Lets Build Web Components! Part 4: Polymer Library - DEV Community 👩‍💻👨‍💻")
* [Let's Build Web Components! Part 5: LitElement - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-5-litelement-906 "Let's Build Web Components! Part 5: LitElement - DEV Community 👩‍💻👨‍💻")
* [Let's Build Web Components! Part 6: Gluon - DEV Community 👩‍💻👨‍💻](https://dev.to/bennypowers/lets-build-web-components-part-6-gluon-27ll "Let's Build Web Components! Part 6: Gluon - DEV Community 👩‍💻👨‍💻")

Web Componentsの基本的な使い方、Polyfill、ライフサイクル、スタイルなどについて解説しています。
また、[Polymer](https://www.polymer-project.org/)や[Gluonjs](https://github.com/ruphin/gluonjs)といったフレームワークを使ったコンポーネント開発などについても書かれているためかなり幅広い内容になっています。

----

[Idiomatic Redux: The History and Implementation of React-Redux · Mark's Dev Blog](https://blog.isquaredsoftware.com/2018/11/react-redux-history-implementation/)という記事では、Reduxのメンテナーの[Mark Erikson](https://github.com/markerikson)が[React Redux](https://github.com/reduxjs/react-redux)の歴史と実装について紹介しています。

v5までのReact Reduxの実装とv6 β実装された[Context API](https://reactjs.org/docs/context.html)ベースの実装やパフォーマンスの問題についても書かれています。
また今後の話として、Reactの[Hooks API](https://reactjs.org/docs/hooks-reference.html)を使った実装の提案などについても書かれています。

----

[HTTP/2 explained](https://daniel.haxx.se/http2/)の著者でもある[Daniel Stenberg](https://daniel.haxx.se/)によるHTTP/3 explainedが公開されています。

- [HTTP/3 explained - The book](https://daniel.haxx.se/http3-explained/)
- [HTTP/3 Explained | daniel.haxx.se](https://daniel.haxx.se/blog/2018/11/26/http3-explained/)

この書籍ではHTTP/3について解説されています。
HTTP/3自体がまだ策定中であるため、この書籍もまだ更新が予定されています。

また、ソースコードもGitHubで公開されています。

- [bagder/http3-explained: A document describing the HTTP/3 and QUIC protocols](https://github.com/bagder/http3-explained)

----

<h1 class="site-genre">アーティクル</h1>

----

## Lets Build Web Components! Part 1: The Standards - DEV Community 👩‍💻👨‍💻
[dev.to/bennypowers/lets-build-web-components-part-1-the-standards-3e85](https://dev.to/bennypowers/lets-build-web-components-part-1-the-standards-3e85 "Lets Build Web Components! Part 1: The Standards - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span></p>

Web Componentsについての連載。
Web Componentsの構成要素、polyfill、読み込み方法、ライフサイクル、非同期ロード。
また`:host`や`<slot>`、スタイル、アクセシビリティ、Polymerなどのフレームワークについて


----

## WebSockets - A Conceptual Deep-Dive | Ably Realtime
[www.ably.io/concepts/websockets](https://www.ably.io/concepts/websockets "WebSockets - A Conceptual Deep-Dive | Ably Realtime")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">article</span> <span class="jser-tag">library</span></p>

WebSocketについての記事。 Cometのようなポーリングによる通信、WebSocketによるハンドシェイクについて。 `WebSocket`を使っての接続方法や著名なライブラリの紹介など


----

## Idiomatic Redux: The History and Implementation of React-Redux · Mark's Dev Blog
[blog.isquaredsoftware.com/2018/11/react-redux-history-implementation/](https://blog.isquaredsoftware.com/2018/11/react-redux-history-implementation/ "Idiomatic Redux: The History and Implementation of React-Redux · Mark's Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">article</span></p>

react-reduxの歴史と今後について
今までのreact-reduxの実装とv6 β実装されたContext APIベースの実装。
また、React Hooksを使った実装のProposalについてなど


----

## ZEIT – ncc: Node.js Compiler Collection
[zeit.co/blog/ncc](https://zeit.co/blog/ncc "ZEIT – ncc: Node.js Compiler Collection")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Node.jsのプログラムを依存含めて1つのファイルにするnccについて。
ファイル1つにまとめることで配布性や実行時の起動時間のI/Oオーバヘッドの改善を目的としている。

- [zeit/ncc: Node.js Compiler Collection](https://github.com/zeit/ncc "zeit/ncc: Node.js Compiler Collection")

----

## Malicious code found in npm package event-stream downloaded 8 million times in the past 2.5 months | Snyk
[snyk.io/blog/malicious-code-found-in-npm-package-event-stream](https://snyk.io/blog/malicious-code-found-in-npm-package-event-stream "Malicious code found in npm package event-stream downloaded 8 million times in the past 2.5 months | Snyk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

`event-stream@3.3.6`と`flatmap-stream`の問題について。
`flatmap-stream`にwalletsからbitcoinを盗むコードが含まれており、`event-stream@3.3.6`がこのパッケージに依存していた問題について。
現在`flatmap-stream`はnpmからunpublishされている

- [I don't know what to say. · Issue #116 · dominictarr/event-stream](https://github.com/dominictarr/event-stream/issues/116 "I don&#x27;t know what to say. · Issue #116 · dominictarr/event-stream")
- [statement on event-stream compromise](https://gist.github.com/dominictarr/9fd9c1024c94592bc7268d36b8d83b3a "statement on event-stream compromise")

----

## How we made Carousell’s mobile web experience 3x faster
[medium.com/carousell-insider/how-we-made-carousells-mobile-web-experience-3x-faster-bbb3be93e006](https://medium.com/carousell-insider/how-we-made-carousells-mobile-web-experience-3x-faster-bbb3be93e006 "How we made Carousell’s mobile web experience 3x faster")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

carousellにおけるパフォーマンス改善について。
PRPLパターン、Critical CSS、Lazy LOading、画像の圧縮とCDN、Service Workerの導入などについて


----

## フロントエンド向けvalidator: favalidの紹介 - asterisc
[akito0107.hatenablog.com/entry/2018/11/23/195538](http://akito0107.hatenablog.com/entry/2018/11/23/195538 "フロントエンド向けvalidator: favalidの紹介 - asterisc")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

バリデーターを関数で書いてcombineできるライブラリのfavalidについて

- [akito0107/favalid: make your favorite validators.](https://github.com/akito0107/favalid "akito0107/favalid: make your favorite validators.")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## seo\_for\_spa.pdf - Speaker Deck
[speakerdeck.com/kazuyaseki/seo-for-spa-cfb3706f-ae1d-4c6f-a83f-96dc2452f32b](https://speakerdeck.com/kazuyaseki/seo-for-spa-cfb3706f-ae1d-4c6f-a83f-96dc2452f32b "seo\_for\_spa.pdf - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">SEO</span> <span class="jser-tag">google</span> <span class="jser-tag">slide</span></p>

Google botに適切に解釈されるようにするための手法についてのスライド。
Google botがChrome 41相当であることによる制限、タイムアウトの検証、Dynamic Rendering(prerender)やSSRなどの対策についてなど


----

## Angular Webアプリケーションの最新設計手法.pdf - Speaker Deck
[speakerdeck.com/koumatsumot0/angular-webahurikesiyonfalsezui-xin-she-ji-shou-fa](https://speakerdeck.com/koumatsumot0/angular-webahurikesiyonfalsezui-xin-she-ji-shou-fa "Angular Webアプリケーションの最新設計手法.pdf - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">slide</span></p>

Angularのコンポーネント設計やステート管理についてのスライド


----

## PWA導入の成果と課題 / nikkei-pwa-html5conf2018 - Speaker Deck
[speakerdeck.com/sisidovski/nikkei-pwa-html5conf2018](https://speakerdeck.com/sisidovski/nikkei-pwa-html5conf2018 "PWA導入の成果と課題 / nikkei-pwa-html5conf2018 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

PWAの導入と運用しての課題についてのスライド。
Service Workerによるパフォーマンスの改善、Add to HomeScreenのハンドリング、Performance Budgetの設定方法とパフォーマンス監視などについて


----

## HTTP and 5G (fixed1)
[www.slideshare.net/dynamis/httpp-and-5g-fixed1](https://www.slideshare.net/dynamis/httpp-and-5g-fixed1 "HTTP and 5G (fixed1)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">QUIC</span> <span class="jser-tag">browser</span> <span class="jser-tag">network</span> <span class="jser-tag">slide</span></p>

5G環境での通信試験についてのスライド。
5Gの試験環境における輻輳制御方法CUBICとBBRの比較、HTTP/1、HTTP/2、QUICの比較などについて


----

## Class features in NodeFest Japan - Google スライド
[docs.google.com/presentation/d/1nsR7QnPlyhlPj1ff4cYyARwcWrYM1j\_fM7dpbFZM3K8/mobilepresent#slide&#x3D;id.p](https://docs.google.com/presentation/d/1nsR7QnPlyhlPj1ff4cYyARwcWrYM1j_fM7dpbFZM3K8/mobilepresent#slide=id.p "Class features in NodeFest Japan - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">slide</span></p>

ECMAScript ProposalのPrivate fieldsについてのスライド。
privateを実現するための構文として`#variable`を使う理由や経緯、構文、現在のStageについてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## google/js-green-licenses: JavaScript package.json License Checker
[github.com/google/js-green-licenses](https://github.com/google/js-green-licenses "google/js-green-licenses: JavaScript package.json License Checker")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">npm</span> <span class="jser-tag">ライセンス</span></p>

`package.json`にかかれている依存ライブラリのライセンスチェックツール。
Pull Reuqest対するチェックなども対応している


----

## KidkArolis/jetpack: 🚀 Jetpack – a more convenient webpack dev server.
[github.com/KidkArolis/jetpack](https://github.com/KidkArolis/jetpack "KidkArolis/jetpack: 🚀 Jetpack – a more convenient webpack dev server.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

webpackベースの開発サーバ、ビルドツール。
Parcelのようにデフォルトの設定があり、設定なしで利用できることを目的としている。


----

## wasmerio/wasmer: High-Performance WebAssembly JIT interpreter
[github.com/wasmerio/wasmer](https://github.com/wasmerio/wasmer "wasmerio/wasmer: High-Performance WebAssembly JIT interpreter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Rust</span></p>

WebAssemblyファイル(`.wasm`と`.wat`)を実行できるスタンドアローンなツール。


----

## Introduction · HTTP/3 explained
[http3-explained.haxx.se/en/](https://http3-explained.haxx.se/en/ "Introduction · HTTP/3 explained")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">http3</span> <span class="jser-tag">document</span></p>

HTTP/3とQUICについての解説ドキュメント。
TCPとUDP、HTTP/2との違い、QUICの仕組みなどについて

- [http2 explained · GitBook (Legacy)](https://legacy.gitbook.com/book/bagder/http2-explained/details "http2 explained · GitBook (Legacy)")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.
[github.com/developit/htm](https://github.com/developit/htm "developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">babal</span> <span class="jser-tag">jsx</span> <span class="jser-tag">library</span></p>

JSXライクなTagged Templatesライブラリ。babelプラグインでコンパイルも可能になっている。


----

## areknawo/Rex: Your RegEx companion.
[github.com/areknawo/rex](https://github.com/areknawo/rex "areknawo/Rex: Your RegEx companion.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

メソッドチェーンで正規表現を作成したり、マッチング、置換するライブラリ


----

## boneskull/create-yo: Use any Yeoman generator with "npm init"
[github.com/boneskull/create-yo](https://github.com/boneskull/create-yo "boneskull/create-yo: Use any Yeoman generator with \"npm init\"")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">library</span></p>

`npm init yo <generator>`できるYoeman向けのツール


----
