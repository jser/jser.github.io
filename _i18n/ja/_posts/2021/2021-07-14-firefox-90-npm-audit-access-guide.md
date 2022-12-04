---
title: "2021-07-14のJS: Firefox 90、npm auditの問題、Access Guide"
author: "azu"
layout: post
date : 2021-07-14T03:24:13.966Z
category: JSer
tags:
- node.js
- Next.js
- npm
- TypeScript
- Tools

---

JSer.info #548 - Firefox 90がリリースされました。

- [Firefox 90.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/90.0/releasenotes/)
- [Firefox 90 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/90)

Firefox 90ではECMAScript Proposal Stage 4のPrivate class fieldsをデフォルトでサポート、Stage 3のString/Arrayの`at()`をサポートしています。FTPサポートの削除、WheelEventの互換性を改善なども含まれています。

また、Chromeでも実装されていた[Fetch metadata request headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#fetch_metadata_request_headers)が実装されています。
`Sec-Fetch-Site`、`Sec-Fetch-Mode`、`Sec-Fetch-User`、`Sec-Fetch-Dest`のリクエストヘッダがそれぞれのリクエストに追加され、サーバ側でのチェックに利用できます。

- [Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/)
- [Protect your resources from web attacks with Fetch Metadata](https://web.dev/fetch-metadata/)

Fetch metadata request headersはSafariとIE以外のブラウザで実装されています。

---

[npm audit: Broken by Design — Overreacted](https://overreacted.io/npm-audit-broken-by-design/)という記事では、[create-react-app](https://github.com/facebook/create-react-app/issues/11174)を例に `npm audit` で報告される脆弱性の問題について書かれています。

報告される脆弱性の殆どはReDOSとなっていて、`devDependencies`として扱うツールにおいてはfalse positiveに近いものとなっている点やエコシステムとして対応が難しくなっている点について書かれています。

GitHubから公開されている GitHub’s Advisory Database のデータにおいても2021年はCWE-400であるDoSが一番多く報告されていて、ReDOSの報告が増えてることもわかります。

- [Our shared common weaknesses | GitHub Security Lab](https://securitylab.github.com/research/CWE-Overview/)

ツールが過剰する報告する問題の中に実際の問題が混ざって無視されてしまう懸念、どのような対応が考えられるか、[npm audit and audit-resolve.json](https://github.com/npm/rfcs/pull/18)といったRFCなどについても書かれています。

---

[Access Guide](https://accessguide.io/)というサイトでは、 WCAG 2.1のアクセシビリティガイドの解説が書かれています。
それぞれのトピックごとに解説や実装方法、テスト方法などについてのリソースがまとめられています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## html2canvas/CHANGELOG.md at master · niklasvh/html2canvas
[github.com/niklasvh/html2canvas/blob/master/CHANGELOG.md#100-2021-07-04](https://github.com/niklasvh/html2canvas/blob/master/CHANGELOG.md#100-2021-07-04 "html2canvas/CHANGELOG.md at master · niklasvh/html2canvas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

HTMLをCanvasにしてスクリーンショットを取るhtml2canvas 1.0.0リリース


----

## Release v8.0.0 · nestjs/nest
[github.com/nestjs/nest/releases/tag/v8.0.0](https://github.com/nestjs/nest/releases/tag/v8.0.0 "Release v8.0.0 · nestjs/nest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nest.js 8.0.0リリース。
Loggerクラスの改善、API Versioningのサポートなど


----

## Release 8.9.2 · mermaid-js/mermaid
[github.com/mermaid-js/mermaid/releases/tag/8.9.2](https://github.com/mermaid-js/mermaid/releases/tag/8.9.2 "Release 8.9.2 · mermaid-js/mermaid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">diagram</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

mermaid 8.9.2で `%%{init: {<JSON_OBJECT>}}%%` の設定記法を使ったXSS脆弱性とPrototype pollutionの脆弱性が修正されている。

- [#1106238 Client-Side DOS via Mermaid Prototype Pollution vulnerability](https://hackerone.com/reports/1106238 "#1106238 Client-Side DOS via Mermaid Prototype Pollution vulnerability")

----

## Firefox 90.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/90.0/releasenotes/](https://www.mozilla.org/en-US/firefox/90.0/releasenotes/ "Firefox 90.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 90リリース。
ES Proposal Stage 4のPrivate class fieldsをデフォルトでサポート、Stage 3のString/Arrayの`at()`をサポート。
FTPサポートの削除、WheelEventの互換性を改善など

- [Firefox 90 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/90 "Firefox 90 for developers - Mozilla | MDN")
- [tc39/proposal-relative-indexing-method: A TC39 proposal to add an .at() method to all the basic indexable classes (Array, String, TypedArray)](https://github.com/tc39/proposal-relative-indexing-method "tc39/proposal-relative-indexing-method: A TC39 proposal to add an .at() method to all the basic indexable classes (Array, String, TypedArray)")

----

## Release 2.27.0 · prisma/prisma
[github.com/prisma/prisma/releases/tag/2.27.0](https://github.com/prisma/prisma/releases/tag/2.27.0 "Release 2.27.0 · prisma/prisma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">MongoDB</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js向けのORMであるPrisma 2.27.0リリース。
MongoDBをプレビューサポート、M1 Macのサポート、pnpmでインストールできない問題を修正など

- [Start from scratch with MongoDB (15 min) | Prisma Docs](https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/mongodb-typescript-mongodb "Start from scratch with MongoDB (15 min) | Prisma Docs")

----
<h1 class="site-genre">アーティクル</h1>

----

## How does Node.js load its built-in/native modules? | Joyee Cheung&#039;s Blog
[joyeecheung.github.io/blog/2021/07/06/how-does-node-js-load-its-builtins-native-modules/](https://joyeecheung.github.io/blog/2021/07/06/how-does-node-js-load-its-builtins-native-modules/ "How does Node.js load its built-in/native modules? | Joyee Cheung&#039;s Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js内のJavaScriptで書かれたビルトインモジュールは、Node.jsバイナリにどのように保存されて読み込まれているかについて。
バイナリファイルの読み取り専用のデータセクションに保存されており、bootstrapでV8を使ってコンパイルやSnapshotsを扱う仕組みをもっている。


----

## Resource inlining in JavaScript frameworks
[web.dev/aurora-resource-inlining/](https://web.dev/aurora-resource-inlining/ "Resource inlining in JavaScript frameworks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">Angular</span> <span class="jser-tag">CSS</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Next.jsとAngularのGoogle FontsのCritical CSSのインライン化について。
FontをロードするCSSをインライン化することでCLSの最適化ができるという話


----

## npm audit: Broken by Design — Overreacted
[overreacted.io/npm-audit-broken-by-design/](https://overreacted.io/npm-audit-broken-by-design/ "npm audit: Broken by Design — Overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

devDependenciesとして使うツールにおけるnpm auditの報告のほとんどがReDoSの脆弱性になってしまっている問題について。
本番で動くdependenciesのみをチェックする`npm audit --production`、公開するパッケージをインライン化する方法とその問題、エコシステムへの問題提起的な記事


----

## TypeScript and native ESM on Node.js
[2ality.com/2021/06/typescript-esm-nodejs.html](https://2ality.com/2021/06/typescript-esm-nodejs.html "TypeScript and native ESM on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

TypeScriptでのESMの対応方法について。
`package.json`の`"type": "module"`設定、`exports`フィールドと`typesVersions`フィールド、`import`するファイルの拡張子設定などについて


----

## jQueryからTypeScript・Reactまで - Viteで始めるモダンで高速な開発環境構築 - ICS MEDIA
[ics.media/entry/210708/](https://ics.media/entry/210708/ "jQueryからTypeScript・Reactまで - Viteで始めるモダンで高速な開発環境構築 - ICS MEDIA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Viteの基本的な使い方についての記事。
ライブラリ、TypeScript、画像などのアセットの利用、設定ファイル、IE11対応についてなど


----

## Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog
[blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/ "Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox 90でFetch Metadata Request Headersをサポート。
`Sec-Fetch-Site`などの`Sec-Fetch-*`のリクエストヘッダをサポートしている

- [Protect your resources from web attacks with Fetch Metadata](https://web.dev/fetch-metadata/ "Protect your resources from web attacks with Fetch Metadata")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Access Guide
[accessguide.io/](https://accessguide.io/ "Access Guide")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">document</span></p>

WCAG 2.1の解説サイト。
どのように実装するか、どのようにテストするか、実際の例について


----

## Javascript Decorators
[javascriptdecorators.org/](https://javascriptdecorators.org/ "Javascript Decorators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">Tools</span> <span class="jser-tag">debug</span></p>

ECMAScript ProposalのDecoratorsを試せるPlaygroundツール

- [tc39/proposal-decorators: Decorators for ES6 classes](https://github.com/tc39/proposal-decorators "tc39/proposal-decorators: Decorators for ES6 classes")


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## FrontLabsOfficial/vue-tiny-validate: 💯 Tiny (2.5KB minified) Vue Validate Composition
[github.com/FrontLabsOfficial/vue-tiny-validate](https://github.com/FrontLabsOfficial/vue-tiny-validate "FrontLabsOfficial/vue-tiny-validate: 💯 Tiny (2.5KB minified) Vue Validate Composition")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Vue Composition API向けのバリデーションライブラリ


----

## lucacasonato/dext.ts: The Preact Framework for Deno
[github.com/lucacasonato/dext.ts](https://github.com/lucacasonato/dext.ts "lucacasonato/dext.ts: The Preact Framework for Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">Next.js</span></p>

Deno向けのNext.jsをインスパイアしたPreactを使ったウェブフレームワーク。


----
<h1 class="site-genre">書籍関係</h1>

----

## O&#039;Reilly Japan - 初めてのWebGL 2 第2版
[www.oreilly.co.jp/books/9784873119373/](https://www.oreilly.co.jp/books/9784873119373/ "O&#039;Reilly Japan - 初めてのWebGL 2 第2版")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2021年07月21日発売
WebGLの入門書


----
