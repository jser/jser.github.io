---
title: "2016-02-02のJS: Firefox 44.0、ES2016の追加機能、webpack2β"
author: azu
layout: post
date : 2016-02-02T19:57
category: JSer
tags:
    - Firefox
    - ECMAScript
    - webpack

---

JSer.info #264 - [Firefox 44.0](https://www.mozilla.jp/firefox/44.0/releasenotes/ "Firefox 44.0")がリリースされました。

`let`と`const`は[Spidermonkey独自の動作](https://www.fxsitecompat.com/ja/docs/2015/variables-defined-with-const-and-let-are-no-longer-properties-on-window-redeclaration-with-let-will-throw/)が含まれていましたが、今回ES6準拠となるように変更されました。

HTTP通信において[Brotli](https://en.wikipedia.org/wiki/Brotli "Brotli")の圧縮アルゴリズムがサポートされています。

- [Content negotiation - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#The_Accept-Encoding_header "Content negotiation - HTTP | MDN")

Chromeでも49で実装されています。(HTTPSのみ有効)

- [Intent to Ship: Brotli (Accept-encoding: br on HTTPS connection) - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/JufzX024oy0/WEOGbN43AwAJ "Intent to Ship: Brotli (Accept-encoding: br on HTTPS connection) - Google グループ")

----

ECMAScript 2016(ES2016)で追加される機能が確定しました。

ES2016からはProposal(≒機能ごと)に仕様の検討を行い、最終的に合意を得られたProposalがECMAScriptの仕様へマージされます。
この新しい策定プロセスを通り、以下の2つのProposalがES2016の仕様に入ります。

- [Array.prototype.includes](https://github.com/tc39/Array.prototype.includes/ "Array.prototype.includes")
- [Exponentiation Operator](https://github.com/rwaldron/exponentiation-operator "Exponentiation Operator")

Proposalから仕様となったものがこの2つという意味なので、ES2016における変更点は他にも色々あります。

詳しくは別途記事を書いたので以下を参照してください。

- [ECMAScript 2016 features & changes - JSer.info](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features &amp; changes - JSer.info")

----

[What's new in webpack 2](https://gist.github.com/sokra/27b24881210b56bbaff7 "What&#39;s new in webpack 2")ではwebpack 2での追加機能や変更点について書かれています。

[Rollup](https://github.com/rollup/rollup "Rollup")ようにES6 Modulesを解析し、使われているもの以外を削除することが出来るようになっています。

また、`System.import`をモジュールの分割ポイントとして扱うことができるようになるようです。

その他の変更はIssueを見るのがいいと思います。

- [Scheduled small breaking changes for 2.0 · Issue #729 · webpack/webpack](https://github.com/webpack/webpack/issues/729 "Scheduled small breaking changes for 2.0 · Issue #729 · webpack/webpack")
- [Issues · webpack/webpack](https://github.com/webpack/webpack/labels/webpack-2 "Issues · webpack/webpack")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## V8 JavaScript Engine: V8 Release 4.9
[v8project.blogspot.com/2016/01/v8-release-49.html](http://v8project.blogspot.com/2016/01/v8-release-49.html "V8 JavaScript Engine: V8 Release 4.9")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.9リリース。
Destructuring、Proxy、Reflect、デフォルトパラメータなどES6の仕様追従。
`Math.random()`のアルゴリズム改善など

- [メジャーブラウザのMath.random()のアルゴリズムがXorShift128+になった - JSer.info](http://jser.info/2016/01/27/math.random-xsfhit/ "メジャーブラウザのMath.random()のアルゴリズムがXorShift128+になった - JSer.info")

----

## jQuery UI 1.12.0 Beta 1 | jQuery UI Blog
[blog.jqueryui.com/2016/01/jquery-ui-1-12-0-beta-1/](http://blog.jqueryui.com/2016/01/jquery-ui-1-12-0-beta-1/ "jQuery UI 1.12.0 Beta 1 | jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.12.0 Beta 1リリース。
controlgroupとcheckboxradioの追加、npmサポート、IE7サポート終了など

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md](https://github.com/tmpvar/jsdom/blob/master/Changelog.md "jsdom/Changelog.md at master · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 8.0.0リリース。
IDLからコードを生成することで仕様との互換性の向上、`Element#insertAdjacentHTML`と`Node#adoptNode`の実装など

----

## Firefox 44.0 リリースノート
[www.mozilla.jp/firefox/44.0/releasenotes/](http://www.mozilla.jp/firefox/44.0/releasenotes/ "Firefox 44.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 44.0リリース。
`Symbol.toPrimitive`の実装、letやconstがES6の仕様に追従、OffscreenCanvas APIをフラグ付きで追加、WebRTCから接頭辞の削除など

- [Firefox 44 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/44 "Firefox 44 for developers - Mozilla | MDN")
- [Firefox 44 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/44/ "Firefox 44 サイト互換性情報 | Firefox サイト互換性情報")
- [const や let で定義された変数は window 上のプロパティとならなくなり、let による再宣言は例外が投げられます | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2015/variables-defined-with-const-and-let-are-no-longer-properties-on-window-redeclaration-with-let-will-throw/ "const や let で定義された変数は window 上のプロパティとならなくなり、let による再宣言は例外が投げられます | Firefox サイト互換性情報")

----

## Announcing TypeScript 1.8 Beta - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2016/01/28/announcing-typescript-1-8-beta.aspx](http://blogs.msdn.com/b/typescript/archive/2016/01/28/announcing-typescript-1-8-beta.aspx "Announcing TypeScript 1.8 Beta - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.8βリリース。
tscにJavaScriptファイルを扱う `--allowJs` が追加された。
ES6 to ES5をTypeScript Compilerで変換、d.tsがないライブラリとかをtscが直接扱えるようになる。
Unreachable codeの検出、String literal typesの追加、JSXの対応改善など

- [What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-18-upcoming "What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki")

----

## PhantomJS 2.1 Release Notes | PhantomJS
[phantomjs.org/release-2.1.html](http://phantomjs.org/release-2.1.html "PhantomJS 2.1 Release Notes | PhantomJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">software</span> <span class="jser-tag">ReleaseNote</span></p>

PhantomJS 2.1リリース。
SSL Client Authentication、context menuイベントのサポート

----

## Release v3.1.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v3.1.0](https://github.com/rackt/redux/releases/tag/v3.1.0 "Release v3.1.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 3.1.0リリース。
`createStore()`が`applyMiddleware()`をオプションとして受け入れられるようになった。

----

## Deprecate TSD · Issue #269 · DefinitelyTyped/tsd
[github.com/DefinitelyTyped/tsd/issues/269](https://github.com/DefinitelyTyped/tsd/issues/269 "Deprecate TSD · Issue #269 · DefinitelyTyped/tsd")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span></p>

TypeScriptの型定義ファイルを管理するツールであるtsdが非推奨となり、代わりにtypingsを利用することが推奨されている。

- [typings/typings - TypeScript](https://github.com/typings/typings "typings/typings - TypeScript")
- [vvakame/dtsm - TypeScript](https://github.com/vvakame/dtsm "vvakame/dtsm - TypeScript")

----
<h1 class="site-genre">アーティクル</h1>

----

## ECMAScript 2016 features &amp; changes - JSer.info
[jser.info/2016/02/01/es2016/](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features & changes - JSer.info")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

ES2016で追加される機能が確定したことについて。
また新機能以外の変更点やどこを見れば仕様の変更が分かるかなどについて

----

## What&#x27;s new in webpack 2
[gist.github.com/sokra/27b24881210b56bbaff7](https://gist.github.com/sokra/27b24881210b56bbaff7 "What's new in webpack 2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack 2での変更点について。
ES6 modulesをベースとした最適化、`System.import`を使った動的ロード向けのモジュール分離に対応するなど

----

## Front-end Application Libraries and Component Architectures - Telerik Developer Network
[developer.telerik.com/featured/front-end-application-frameworks-component-architectures/](http://developer.telerik.com/featured/front-end-application-frameworks-component-architectures/ "Front-end Application Libraries and Component Architectures - Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">まとめ</span></p>

コンポーネントを扱うライブラリの仕組みや構成、ルーター、サポートブラウザなどについての比較まとめ。
Polymer、React、Riot.js、Vue.js、Aurelia、Angular2について

----

## Spencer Dixon - Test Driven React Tutorial
[spencerdixon.com/blog/test-driven-react-tutorial.html](http://spencerdixon.com/blog/test-driven-react-tutorial.html "Spencer Dixon - Test Driven React Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span></p>

Reactのテストについてのチュートリアル

----

## Adding ESLint to Your Project is Now Easier than Ever
[devnull.guru/adding-eslint-to-your-project-is-easier-than-ever/](http://devnull.guru/adding-eslint-to-your-project-is-easier-than-ever/ "Adding ESLint to Your Project is Now Easier than Ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Bluetooth</span></p>

ESLint 2.xで導入されてる`--init`によるAutomatic Configurationについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## CreateJS入門 - ICS MEDIA
[ics.media/tutorial-createjs/index.html](https://ics.media/tutorial-createjs/index.html "CreateJS入門 - ICS MEDIA")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">tutorial</span></p>

CreateJS入門サイト

----

## Styleguide: Accessibility · edx/ux-pattern-library Wiki
[github.com/edx/ux-pattern-library/wiki/Styleguide:-Accessibility](https://github.com/edx/ux-pattern-library/wiki/Styleguide:-Accessibility "Styleguide: Accessibility · edx/ux-pattern-library Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">WAI-ARIA</span></p>

アクセシビリティについてスタイルガイド

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## naomiaro/waveform-playlist: Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Project inspired by Audacity.
[github.com/naomiaro/waveform-playlist](https://github.com/naomiaro/waveform-playlist "naomiaro/waveform-playlist: Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Project inspired by Audacity.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">editor</span></p>

AudacityインスパイアなWeb Audioを使った音声エディタ

----

## sinsoku/clairvoyance
[github.com/sinsoku/clairvoyance](https://github.com/sinsoku/clairvoyance "sinsoku/clairvoyance")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

CSSのカバレッジ計測ツール。
CSSファイルに書かれたスタイルがHTMLの中でどのくらい使われてるかを計測できるツール

- [CSS のカバレッジを計測する Clairvoyance というツールを作りました - アジャイルSEの憂鬱](http://sinsoku.hatenablog.com/entry/2016/01/31/174155 "CSS のカバレッジを計測する Clairvoyance というツールを作りました - アジャイルSEの憂鬱")

----

## juliankrispel/decaf: Coffeescript to ES.next transpiler
[github.com/juliankrispel/decaf](https://github.com/juliankrispel/decaf "juliankrispel/decaf: Coffeescript to ES.next transpiler")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

CoffeeScriptのコードをJavaScriptに変換するツール。

- [Issues · decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate "Issues · decaffeinate/decaffeinate")

----

## dfilatov/vidom: Library to build UI based on virtual DOM
[github.com/dfilatov/vidom](https://github.com/dfilatov/vidom "dfilatov/vidom: Library to build UI based on virtual DOM")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

ReactインスパイアなVirtual DOMを持つUIライブラリ。
Reactより小さく早いものを目的としている

----

## developit/preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.
[github.com/developit/preact](https://github.com/developit/preact "developit/preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Reactのコアを再実装することを目的としたライブラリ。
ContextやPropTypesなどを削除している。
preact-compatというReactの互換レイヤーを別モジュールとして持っている。

- [Differences to React · developit/preact Wiki](https://github.com/developit/preact/wiki/Differences-to-React "Differences to React · developit/preact Wiki")
- [developit/preact-compat - JavaScript](https://github.com/developit/preact-compat "developit/preact-compat - JavaScript")

----

## zeithq/micro: Micro — Async HTTP microservices
[github.com/zeithq/micro](https://github.com/zeithq/micro "zeithq/micro: Micro — Async HTTP microservices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">node.js</span></p>

小さなHTTPサーバライブラリ。
リクエストを受け取りレスポンスを返すというシンプルなもの。
async/awaitをデフォルトで使えるようになっている。

----

## sindresorhus/got: Simplified HTTP/HTTPS requests
[github.com/sindresorhus/got](https://github.com/sindresorhus/got "sindresorhus/got: Simplified HTTP/HTTPS requests")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">Promises</span></p>

Node.js向けのHTTPクライアントライブラリ。`request`と同じ立ち位置のライブラリ

----

## Viewer.js
[fengyuanchen.github.io/viewerjs/](http://fengyuanchen.github.io/viewerjs/ "Viewer.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span> <span class="jser-tag">library</span></p>

多機能な画像ビューアライブラリ。

----

## stylelint/stylelint
[github.com/stylelint/stylelint](https://github.com/stylelint/stylelint "stylelint/stylelint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

ルールやプラグインで拡張できるCSSのスタイルLintツール

----
