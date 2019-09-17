---
title: "2019-09-17のJS: Chrome 77、TypeScript 3.7のロードマップ、Can I use and MDN"
author: "azu"
layout: post
date : 2019-09-17T00:03:38.654Z
category: JSer
tags:
- Chrome
- TypeScript
- MDN

---

JSer.info #453 - Chrome 77がリリースされました。

- [New in Chrome 77  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/09/nic77)

Chrome 77では、`PerformanceObserver`の中でページ内の大きな要素の変更があったことを関しするLargest Contentful Paint(LCP)がサポートされました。

- [Largest Contentful Paint  |  web.dev](https://web.dev/largest-contentful-paint/)

その他にも`formdata`イベント、`formAssociated`プロパティのサポートなどが含まれています。
また、アドレスバーに表示されていたEV証明書の情報が詳細パネルの方に移動しています。

- [Troy Hunt: Extended Validation Certificates are (Really, Really) Dead](https://www.troyhunt.com/extended-validation-certificates-are-really-really-dead/)
- [Upcoming Change to Chrome's Identity Indicators - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/h1bTcoTpfeI/jUTk1z7VAAAJ)

----

[TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352)というIssueでTypeScript 3.7のロードマップが公開されています。

ECMAScript Private Fields、Optional Chaining、Nullish Coalescing、Top-Level awaitなど現在Stage3のProposalに対応していく予定です。
また、今までは制限されていた`--declaration`と`--allowJs`の組合せや`--declaration`と`--isolatedModules`のの組み合わせに対応していく予定です。
その他として、`typescript`パッケージサイズの削減、`@types`パッケージをGitHub Package Registryにもpublishするようにし、ハンドブックの更新なども予定されています。

----

[Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/)という記事では、[MDN compat data](https://github.com/mdn/browser-compat-data)と[Can I use...](https://caniuse.com/)のコラボレーションについて書かれています。

どちらも機能などに対するブラウザのサポート状況をまとめたデータですが、目的が異なるためデータの特性が若干異なっています。
MDNはあらゆる機能に関する網羅性を持ったデータに対して、Can I use...はブラウザがサポートしているかに注目したデータとなっています。
そのため、Can I use...のデータには入っていない項目も多くありました。

今回のコラボレーションで、[Can I use...](https://caniuse.com/)が[MDN compat data](https://github.com/mdn/browser-compat-data)のデータを使って機能に関するブラウザのサポート状況を表示できるようになっています。（現在は両方のデータを検索した結果がそれぞれ表示される）
 
また、類似するサイトとしてメールクライアント別に利用できるHTMLやCSSなどのサポート状況をまとめたCan I email...というサイトも別の作者によって公開されています。

- [Can I email… Support tables for HTML and CSS in emails](https://www.caniemail.com/)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript
[github.com/microsoft/TypeScript/issues/33352](https://github.com/microsoft/TypeScript/issues/33352 "TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span></p>

TypeScript 3.7のロードマップ。
ECMAScript Private Fields、Optional Chaining、Nullish Coalescingへの対応、`--declaration`と`--allowJs`の組合せに対応など。
また`typescript`パッケージサイズの削減、`@types`パッケージをGitHub Package Registryにもpublishするようにし、ハンドブックの更新なども予定されている。


----

## Release DOMPurify 2.0.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/2.0.0](https://github.com/cure53/DOMPurify/releases/tag/2.0.0 "Release DOMPurify 2.0.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

DOMpurify 2.0.0リリース。
Trusted Typesが利用できる場合でも`RETURN_TRUSTED_TYPE`オプションを渡したときのみ、Trusted Typesを使うように変更


----

## Google Developers Blog: Flutter news from GDD China: uniting Flutter on web and mobile, and introducing Flutter 1.9
[developers.googleblog.com/2019/09/flutter-news-from-gdd-china-flutter1.9.html?m&#x3D;1](https://developers.googleblog.com/2019/09/flutter-news-from-gdd-china-flutter1.9.html?m=1 "Google Developers Blog: Flutter news from GDD China: uniting Flutter on web and mobile, and introducing Flutter 1.9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">ReleaseNote</span></p>

Flutter 1.9 リリース。
Webサポートがメインリポジトリにマージされた。


----

## ESLint v6.4.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2019/09/eslint-v6.4.0-released](https://eslint.org/blog/2019/09/eslint-v6.4.0-released "ESLint v6.4.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 6.4.0リリース。
`no-import-assign`、`prefer-regex-literals`、`default-param-last`のルールを追加。
一部ルールが`enforceForClassMembers`オプションでクラス構文をサポートするようになるなど

- [ESLint v6.4.0 - Qiita](https://qiita.com/mysticatea/items/4164b162fb37dcc443a1 "ESLint v6.4.0 - Qiita")

----

## Release v4.0.0 · immerjs/immer
[github.com/immerjs/immer/releases/tag/v4.0.0](https://github.com/immerjs/immer/releases/tag/v4.0.0 "Release v4.0.0 · immerjs/immer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Immer 4.0.0リリース。
development modeでは、すべての値はdeep frozenされた状態で保存されるようになった。
またウェブサイトのドキュメント更新など

- [Introduction to Immer · Immer](https://immerjs.github.io/immer/docs/introduction "Introduction to Immer · Immer")

----

## Release 2.4.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v2.4.0](https://github.com/avajs/ava/releases/tag/v2.4.0 "Release 2.4.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 2.4.0リリース。
`t.try()`をフラグ付きでサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## How to build a plugin system on the web and also sleep well at night
[www.figma.com/blog/how-we-built-the-figma-plugin-system/](https://www.figma.com/blog/how-we-built-the-figma-plugin-system/ "How to build a plugin system on the web and also sleep well at night")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">plugin</span></p>

プラグインとして追加されるサードパーティコードを安全にウェブブラウザで実行するための仕組みについて。
`<inline-iframe>`、JavaScriptインタプリタの利用、ProposalのRealms(shim)を使ったサンドボックスについて

- [tc39/proposal-realms: ECMAScript Proposal, specs, and reference implementation for Realms](https://github.com/tc39/proposal-realms "tc39/proposal-realms: ECMAScript Proposal, specs, and reference implementation for Realms")
- [Agoric/realms-shim: Spec-compliant shim for Realms TC39 Proposal](https://github.com/Agoric/realms-shim "Agoric/realms-shim: Spec-compliant shim for Realms TC39 Proposal")

----

## Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/](https://hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/ "Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

MDN Compat DataをCan I Useのウェブサイトにマージ。
Can I Use上でMDNのデータを元にした機能やサポートブラウザが見られるようになった。


----

## A lighter V8 · V8
[v8.dev/blog/v8-lite](https://v8.dev/blog/v8-lite "A lighter V8 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

V8のLite modeについて。
メモリが少ないデバイス向けのモードで、消費メモリの削減を目的としている。


----

## WebGPU and WSL in Safari | WebKit
[webkit.org/blog/9528/webgpu-and-wsl-in-safari/](https://webkit.org/blog/9528/webgpu-and-wsl-in-safari/ "WebGPU and WSL in Safari | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari Technology Preview 91からベータサポートされているWebGPU APIとWSLについて。
WebGPUのパイプライン処理の最適化、ランタイムのパフォーマンス、Web Shading Language(WSL)について紹介されている


----

## X3D: Declarative 3D for the Modern Web
[blog.scottlogic.com/2019/08/27/declarative-3d-for-the-modern-web.html](https://blog.scottlogic.com/2019/08/27/declarative-3d-for-the-modern-web.html "X3D: Declarative 3D for the Modern Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">3D</span> <span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

宣言的な3D表現を行うX3Dという仕様とX3DOMという実装について。
SVGのようにHTML中にタグを書くことで3D表示を行う


----

## New in Chrome 77  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/09/nic77](https://developers.google.com/web/updates/2019/09/nic77 "New in Chrome 77  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 77リリース。
Largest Contentful Paint(LCP)、`formdata`イベント、`formAssociated`プロパティのサポートなど

- [More capable form controls  |  web.dev](https://web.dev/more-capable-form-controls/ "More capable form controls  |  web.dev")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Can I email… Support tables for HTML and CSS in emails
[www.caniemail.com/](https://www.caniemail.com/ "Can I email… Support tables for HTML and CSS in emails")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mail</span> <span class="jser-tag">HTML</span> <span class="jser-tag">webservice</span></p>

メール内で特定のHTMLタグやCSSが利用できるかをメールクライアントのサポート状態を検索できるサービス。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## nanoSQL 2
[nanosql.io/](https://nanosql.io/ "nanoSQL 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SQL</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

SQL builderライブラリ。
インメモリ、ブラウザのIndexedDBやLocalstorage、Node.jsからMySQLやRedixなどさまざまなデータべースに対して動作する


----
<h1 class="site-genre">書籍関係</h1>

----

## Web Development with Node and Express, 2nd Edition - O'Reilly Media
[shop.oreilly.com/product/0636920261216.do](http://shop.oreilly.com/product/0636920261216.do "Web Development with Node and Express, 2nd Edition - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">book</span></p>

2019年10月発売
Node.jsとExpressについての書籍


----

## daumann/ECMAScript-new-features-list: A comprehensive list of new ES features, including ES2015 (ES6), ES2016 (ES7), ES2017 (ES8), ES2018 (ES9), ES2019 (ES10)
[github.com/daumann/ECMAScript-new-features-list](https://github.com/daumann/ECMAScript-new-features-list "daumann/ECMAScript-new-features-list: A comprehensive list of new ES features, including ES2015 (ES6), ES2016 (ES7), ES2017 (ES8), ES2018 (ES9), ES2019 (ES10)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

ECMAScriptのバージョンごとに追加された機能/構文とサンプルコードをまとめたリポジトリ


----
