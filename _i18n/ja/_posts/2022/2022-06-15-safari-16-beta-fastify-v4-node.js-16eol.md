---
title: "2022-06-15のJS: Safari 16 Beta、Fastify v4、Node.js 16のEOLの予定日の変更"
author: "azu"
layout: post
date : 2022-06-15T03:43:11.216Z
category: JSer
tags:
- Tools
- node.js
- npm
- browser
- React

---

JSer.info #596 - Safari 16 betaのリリースノートと変更点についての記事が公開されています。

- [Safari 16 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-16-release-notes)
- [News from WWDC22: WebKit Features in Safari 16 Beta | WebKit](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/)

プッシュ通知をPush APIがサポートされます。

- [Meet Web Push | WebKit](https://webkit.org/blog/12945/meet-web-push/)

CSSのContainer Queries、Subgrid、`overscroll-behavior`プロパティのサポートが追加されています。
また、Shared Workerのサポート、Formの`requestSubmit()`メソッドをサポートも追加されています。

----

Node.jsのウェブアプリケーションフレームワークであるFastify v4がリリースされました。

- [Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium](https://medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e)
- [Release v4.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v4.0.0)

Fastify  4.0.0では挙動の一貫性がなかった部分が破壊的な変更として修正されています。
また、Fastify 3.xは2023年6月30日にEOL(End Of Life)となることが発表されています。

----

Node.js 16 LTSのEOLは2024年4月の予定でしたが、2023年9月11日へと短縮されています。

- [Bringing forward the End-of-Life Date for Node.js 16 | Node.js](https://nodejs.org/en/blog/announcements/nodejs16-eol/)

これは、Node.js 16が利用するOpenSSL1.1.1のEOLが2023年9月11日となっているためです。
そのため、Node.js 16のEOLは7ヶ月短縮され、2023年9月11日までとなる予定です。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v11.9.0 · sverweij/dependency-cruiser
[github.com/sverweij/dependency-cruiser/releases/tag/v11.9.0](https://github.com/sverweij/dependency-cruiser/releases/tag/v11.9.0 "Release v11.9.0 · sverweij/dependency-cruiser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

dependency-cruiser 11.9.0リリース。
Markdownレポートをサポート


----

## News from WWDC22: WebKit Features in Safari 16 Beta | WebKit
[webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/ "News from WWDC22: WebKit Features in Safari 16 Beta | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 16 Betaの変更点について。
Container Queries、Push API、Subgridのサポート。
CSSの`overscroll-behavior`のサポート、Shared Workerのサポート、Formの`requestSubmit()`メソッドをサポートなど

- [Safari 16 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-16-release-notes "Safari 16 Beta Release Notes | Apple Developer Documentation")

----

## Release v1.5.0 · ghiscoding/lerna-lite
[github.com/ghiscoding/lerna-lite/releases/tag/v1.5.0](https://github.com/ghiscoding/lerna-lite/releases/tag/v1.5.0 "Release v1.5.0 · ghiscoding/lerna-lite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

lerna-lite 1.5.0リリース。
ロックファイルを更新する`--sync-workspace-lock`フラグを追加など


----

## Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium
[medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e](https://medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e "Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Fastify 4.0.0リリース。
`reply.send`を呼び出すの必須に、`setErrorHandler`の処理順の一貫性を改善、Pino v8へアップデート、`fastify.listen`の可変長引数を非推奨化など

- [Release v4.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v4.0.0 "Release v4.0.0 · fastify/fastify")

----

## Bringing forward the End-of-Life Date for Node.js 16 | Node.js
[nodejs.org/en/blog/announcements/nodejs16-eol/](https://nodejs.org/en/blog/announcements/nodejs16-eol/ "Bringing forward the End-of-Life Date for Node.js 16 | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

Node.js 16のEOLがOpenSSL 1.1.1のEOLと同日の2023年9月11日までに繰り上げられた。


----

## PlasmoHQ/plasmo: The browser extension framework
[github.com/PlasmoHQ/plasmo](https://github.com/PlasmoHQ/plasmo "PlasmoHQ/plasmo: The browser extension framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">library</span></p>

ブラウザ拡張向けのフレームワーク。
ReactとTypeScriptのサポート、Manifest V3、Live Reloading、`.env`のサポート、各拡張Storeへのデプロイの対応など


----

## ECMAScript proposal updates @ 2022-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2022/06/13/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2022/06/13/ecmascript-proposal-update "ECMAScript proposal updates @ 2022-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2022年6月のTC39ミーティングにおけるECMAScript Proposalのステータス変更のまとめ


----

## Release 3.23.0 - 2022.06.14 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.23.0](https://github.com/zloirock/core-js/releases/tag/v3.23.0 "Release 3.23.0 - 2022.06.14 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.23.0リリース。
`Array.prototype.findLast`をstableに移動、`Array.prototype.groupBy`を`Array.prototype.group`にリネームなど


----

## Prettier 2.7: new --cache CLI option and TypeScript 4.7 syntax! · Prettier
[prettier.io/blog/2022/06/14/2.7.0.html](https://prettier.io/blog/2022/06/14/2.7.0.html "Prettier 2.7: new --cache CLI option and TypeScript 4.7 syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.7リリース。
`--cache`フラグの追加、TypeScript 4.7のサポートなど


----

## Release 10.8.0 · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.8.0](https://github.com/preactjs/preact/releases/tag/10.8.0 "Release 10.8.0 · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.8.0リリース。
Vitestとの互換性のためにSubpackagesへ`exports`フィールドを追加、`createRoot`/`hydrateRoot` APIのReactとの互換性を改善など


----

## Release v1.6.0 · remix-run/remix
[github.com/remix-run/remix/releases/tag/v1.6.0](https://github.com/remix-run/remix/releases/tag/v1.6.0 "Release v1.6.0 · remix-run/remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Remix</span></p>

Remix v1.6.0リリース。
`remix`パッケージをDeprecatedとして、`@remix-run/*`の個別のパッケージからImportすることを推奨するように。


----

## Release 7.0.0 · google/zx
[github.com/google/zx/releases/tag/7.0.0](https://github.com/google/zx/releases/tag/7.0.0 "Release 7.0.0 · google/zx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">shell</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

zx 7.0.0リリース。
TypeScriptでの書き直し、`within()`、`echo()` APIの追加。
`--eval`フラグのサポート、REPLのサポートなど


----

## Release 18.2.0 (June 14, 2022) · facebook/react
[github.com/facebook/react/releases/tag/v18.2.0](https://github.com/facebook/react/releases/tag/v18.2.0 "Release 18.2.0 (June 14, 2022) · facebook/react")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React v18.2.0リリース。
`onRecoverableError`の第二引数にcomponent stackの情報を渡すように。
Hydrate時にブラウザの拡張機能などによってHTMLが変更されているとレンダリングが壊れる問題を修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## First-party cookie recipes
[web.dev/first-party-cookie-recipes/](https://web.dev/first-party-cookie-recipes/ "First-party cookie recipes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

First-Party Cookieを設定する際のCookieの属性の指定について。
通常のFirst-Party Cookieとサブドメインを持つサイトのパターンについてそれぞれ解説が書かれている。
`__Host` prefix、`Secure`属性、`Domain`属性を指定しないこと、`Path`属性、`HttpOnly`属性、`SameSite`属性についてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## fastify/fastify-dx: A Full Stack Framework based on Fastify and Vite. Built for great developer experience without compromising on performance and stability.
[github.com/fastify/fastify-dx](https://github.com/fastify/fastify-dx "fastify/fastify-dx: A Full Stack Framework based on Fastify and Vite. Built for great developer experience without compromising on performance and stability.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

FastifyとViteを使ったフレームワーク。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ranyitz/qnm: cli utility for querying the node\_modules directory
[github.com/ranyitz/qnm](https://github.com/ranyitz/qnm "ranyitz/qnm: cli utility for querying the node\_modules directory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

node_modulesにインストールされているパッケージのバージョンや最新のバージョンや公開日などの情報を表示できるコマンドラインツール。
また、パッケージのサイズや依存している個数なども表示できる


----
