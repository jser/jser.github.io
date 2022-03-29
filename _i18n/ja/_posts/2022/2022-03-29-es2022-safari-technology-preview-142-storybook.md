---
title: "2022-03-29のJS: ES2022リリース候補版、Safari Technology Preview 142、Storybookの代替実装"
author: "azu"
layout: post
date : 2022-03-29T03:02:54.858Z
category: JSer
tags:
- ECMAScript
- React
- debug
- Tools
- vite

---

JSer.info #585 - ECMAScript 2022のリリース候補版となる仕様書のドラフトが公開されました。
合わせて、ECMAScript Internationalization APIのES2022のリリース候補版が公開されています。

- [Release ES2022 Candidate March 2022 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03)
- [Release ES Intl 2022 Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/es2022-candidate)

6月のEcma InternationalでのGA(総会)で承認されたタイミングで、ES2022が正式にリリースされる予定です。
Normative(仕様の変更、Proposalを仕様にマージ)な変更は次のページにまとめてあります。

- [ES2021...ES2022 Normative changes: https://github.com/tc39/ecma262/compare/es2021...es2022-candidate-2022-03](https://gist.github.com/azu/a33211926e3de8bff8de83d6783c55eb)

次のProposalが、それぞれES2022に含まれる予定です。

- Class Fields
    - [tc39/proposal-class-fields](https://github.com/tc39/proposal-class-fields) private/public
    - [Ergonomic brand checks for Private Fields](https://github.com/tc39/proposal-private-fields-in-in)
- [Class static initialization blocks](https://github.com/tc39/proposal-class-static-block)
- [Error Cause](https://github.com/tc39/proposal-error-cause)
- [RegExp Match Indices](https://github.com/tc39/proposal-regexp-match-indices)
- [Top-level `await` proposal](https://github.com/tc39/proposal-top-level-await)
- [Object.hasOwn](https://github.com/tc39/proposal-accessible-object-hasownproperty)
- [String/Array.at()](https://github.com/tc39/proposal-relative-indexing-method)

ES2022に対応するツールだと、[Babel](https://babeljs.io/docs/en/plugins-list#es2022)、[TypeScript 4.6](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/)、[ESLint v8.9.0](https://eslint.org/blog/2022/02/eslint-v8.9.0-released)、[esbuild v0.14.24](https://github.com/evanw/esbuild/releases/v0.14.24)などが対応済みです。

ES2022に対応する書籍だと、[JavaScript for impatient programmers](https://exploringjs.com/impatient-js/index.html)が[既に対応済み](https://exploringjs.com/impatient-js/ch_new-javascript-features.html#new-in-es2022)で、[JavaScript Primer](https://jsprimer.net/)が[対応中](https://github.com/asciidwango/js-primer/issues/1337)となっています。

---

Safari Technology Preview 142がリリースされました。

- [Release Notes for Safari Technology Preview 142 | WebKit](https://webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/)

CSS Subgrid/CSS Container Queries/CSS Motion Pathがデフォルトで有効化されています。
ECMAScript Proposal Stage3の[ShadowRealm](https://github.com/tc39/proposal-shadowrealm)をデフォルトで有効化されています。
また、以前実装がありましたがその後削除された[SharedWorker](https://developer.mozilla.org/ja/docs/Web/API/SharedWorker)の実装が再度進められています。
そのほかには、WebKitがProposalを出している3Dコンテンツを表示する`<model>`要素の実験的な実装が含まれています。

- [explainers/README.md at main · WebKit/explainers](https://github.com/WebKit/explainers/blob/main/model/README.md)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release ES2022 Candidate March 2022 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03](https://github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03 "Release ES2022 Candidate March 2022 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2022 リリース候補版のリリース


----

## Release ES Intl 2022 Candidate · tc39/ecma402
[github.com/tc39/ecma402/releases/tag/es2022-candidate](https://github.com/tc39/ecma402/releases/tag/es2022-candidate "Release ES Intl 2022 Candidate · tc39/ecma402")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2022 Internationalizatio APIのリリース候補版のリリース。


----

## Release Notes for Safari Technology Preview 142 | WebKit
[webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/](https://webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/ "Release Notes for Safari Technology Preview 142 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 142リリース。
CSS Subgrid/CSS Container Queries/CSS Motion Pathをデフォルトで有効化。
ES Proposal Stage3のShadow Realmsをデフォルトで有効化、Shared Workersの実装。
実験的な`<model>`要素の実装など

- [explainers/README.md at main · WebKit/explainers](https://github.com/WebKit/explainers/blob/main/model/README.md "explainers/README.md at main · WebKit/explainers")

----

## Decorators (sans metadata) to stage 3, per 2022.03.28 TC39 · tc39/proposals@eced71d
[github.com/tc39/proposals/commit/eced71d59d7c34e0f173fdec6b6fb477fc2e0371](https://github.com/tc39/proposals/commit/eced71d59d7c34e0f173fdec6b6fb477fc2e0371 "Decorators (sans metadata) to stage 3, per 2022.03.28 TC39 · tc39/proposals@eced71d")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

ECMAScript ProposalのDecoratorがStage 3となった。


----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing Ladle | Ladle
[www.ladle.dev/blog/introducing-ladle/](https://www.ladle.dev/blog/introducing-ladle/ "Introducing Ladle | Ladle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">debug</span> <span class="jser-tag">vite</span></p>

ViteベースのStorybook代替実装であるLadleについて。
ビルド時間の短縮といったパフォーマンスの改善などが主な目的で作られている

- [tajo/ladle: 🥄 Develop, test and document your React components faster.](https://github.com/tajo/ladle "tajo/ladle: 🥄 Develop, test and document your React components faster.")

----

## Introducing MDN Plus: Make MDN your own - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2022/03/introducing-mdn-plus-make-mdn-your-own/](https://hacks.mozilla.org/2022/03/introducing-mdn-plus-make-mdn-your-own/ "Introducing MDN Plus: Make MDN your own - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">article</span></p>

MDN Plusについて。
ページの変更通知、ページのお気に入り機能、オフライン機能などが利用できるサブスクリプションの有料機能。
現在はUSとCanadaで利用できる。


----

## Remixing React Router | Remix
[remix.run/blog/remixing-react-router](https://remix.run/blog/remixing-react-router "Remixing React Router | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

RemixとReact Routerのリポジトリをマージする方針について。
RemixをReact Routerのリポジトリへマージし、Remixというリポジトリ名に変更する予定について。


----

## npm-scripts を書く時の手癖 - mizdra&#039;s blog
[www.mizdra.net/entry/2022/03/24/093000](https://www.mizdra.net/entry/2022/03/24/093000 "npm-scripts を書く時の手癖 - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

npm-scriptsの基本的なパターン、npm-run-allを使った複数のコマンドを実行するパターン、コードを使ったscriptを扱うパターンなどについての記事。


----

## Tao of Node - Design, Architecture &amp; Best Practices | Alex Kondov - Software Engineer
[alexkondov.com/tao-of-node/](https://alexkondov.com/tao-of-node/ "Tao of Node - Design, Architecture &amp; Best Practices | Alex Kondov - Software Engineer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsでのウェブアプリケーション開発おけるプラクティスについての記事


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ブラウザ自動操作技術の深層へ、直接触れて学ぶ WebDriver と Chrome DevTools Protocol - Speaker Deck
[speakerdeck.com/hgsgtk/webdriver-cdp-using-php](https://speakerdeck.com/hgsgtk/webdriver-cdp-using-php "ブラウザ自動操作技術の深層へ、直接触れて学ぶ WebDriver と Chrome DevTools Protocol - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">webdriver</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">slide</span> <span class="jser-tag">php</span></p>

WebDriver APIとChrome DevTools Protocol(CDP)についてのスライド。
それぞれのAPIを使ってブラウザ操作を自動化する処理をどのように書くのかについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## tajo/ladle: 🥄 Develop, test and document your React components faster.
[github.com/tajo/ladle](https://github.com/tajo/ladle "tajo/ladle: 🥄 Develop, test and document your React components faster.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">vite</span></p>

ViteベースのStorybookの代替実装

- [Introducing Ladle | Ladle](https://www.ladle.dev/blog/introducing-ladle/ "Introducing Ladle | Ladle")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## MattiasBuelens/web-streams-polyfill: Web Streams, based on the WHATWG spec reference implementation
[github.com/MattiasBuelens/web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill "MattiasBuelens/web-streams-polyfill: Web Streams, based on the WHATWG spec reference implementation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">stream</span> <span class="jser-tag">polyfill</span></p>

Web Streamのpolyfillライブラリ


----
