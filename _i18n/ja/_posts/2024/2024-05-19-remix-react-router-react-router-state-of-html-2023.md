---
title: "2024-05-19のJS: Remix + React Router = React Router、State of HTML 2023"
author: "azu"
layout: post
date: 2024-05-19T14:15:49.809Z
category: JSer
tags:
- React
- Angular
- nodejs
- Next.js
- safari

---

JSer.info #693 - 次の記事では、Remix v3はReact Router v7としてリリースする予定という話が紹介されています。

- [Merging Remix and React Router | Remix](https://remix.run/blog/merging-remix-and-react-router)

RemixとReact Routerは、Viteとサーバ以外はほぼ同等の機能になってきています。
そのため、React RouterをRemixにマイグレーションするのではなく、React RouterをアップデートするだけでRemixの機能を使えるようにしたいという話が書かれています。
既存のRemixアプリは、import先のパッケージを`react-router`に変更するだけで動く予定とのことです。

この意思決定の詳細は、Xでも書かれています。

- https://x.com/ryanflorence/status/1791479313939976313

React Routerの安定化のために、Remix自体の開発は少しの間止まるとのことですが、
今後Remixプロジェクトとしての予定があるそうです。

---

State of HTML 2023の結果が公開されました。

- [State of HTML 2023](https://2023.stateofhtml.com/en-US/)

HTMLの要素や属性、Web Components、アクセシビリティ、課題や欲しい機能についてのアンケート結果がまとめられています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## WebKit Features in Safari 17.5 | WebKit
[webkit.org/blog/15383/webkit-features-in-safari-17-5/](https://webkit.org/blog/15383/webkit-features-in-safari-17-5/ "WebKit Features in Safari 17.5 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17.5の変更点について。
CSSの`text-wrap: balance`、`light-dark()`、`@starting-style`、`@import <url> supports(<feature>)`のサポート。
AV1 for WebCodecsのサポートなど


----

## Firefox 126.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/126.0/releasenotes/](https://www.mozilla.org/en-US/firefox/126.0/releasenotes/ "Firefox 126.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 126リリース。
zstdをサポート、CSSの`zoom`プロパティをサポート、`URL.parse()`をサポート、 Screen Wake Lock APIをサポート。
Custom ElementのCustomStateSetと`:state()`擬似クラスをサポートなど

- [Firefox 126 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/126 "Firefox 126 for developers - Mozilla | MDN")

----

## Node.js — Node v22.2.0 (Current)
[nodejs.org/en/blog/release/v22.2.0](https://nodejs.org/en/blog/release/v22.2.0 "Node.js — Node v22.2.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.2.0リリース。
fs.globが`withFileTypes`をサポート、`--inspect-wait=host:port`をサポート、`--experimental-policy`を削除。
`node:test`に`test.plan`メソッドの追加など


----

## Release 8.1.0 · google/zx
[github.com/google/zx/releases/tag/8.1.0](https://github.com/google/zx/releases/tag/8.1.0 "Release 8.1.0 · google/zx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ShellScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

zx 8.1.0リリース。
ESMとCJSの両方をサポート、Node.js 12から22までサポート、Deno 1.xとの互換性のサポート。
`usePwsh()`の追加、`$.timeout`のサポート、`--cwd`フラグの追加など


----

## Release v0.21.3 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.21.3](https://github.com/evanw/esbuild/releases/tag/v0.21.3 "Release v0.21.3 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.21.3リリース。
decorator metadata proposalのサポート


----
<h1 class="site-genre">アーティクル</h1>

----

## Merging Remix and React Router | Remix
[remix.run/blog/merging-remix-and-react-router](https://remix.run/blog/merging-remix-and-react-router "Merging Remix and React Router | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

RemixはReact Router v7としてリリースする予定という話。
RemixとReact Routerは、Viteとサーバ以外はほぼ同等の機能になってきている。
そのため、React RouterをRemixにマイグレーションするのではなく、React RouterをアップデートするだけでRemixの機能を使えるようにしたいという話。
既存のRemixアプリは、import先のパッケージを`react-router`に変更するだけで動く予定という話。


----

## Angular 17 Update: Control Flow &amp; App Builder Migration - ANGULARarchitects
[www.angulararchitects.io/blog/angular-17-update-control-flow-app-builder-migration/](https://www.angulararchitects.io/blog/angular-17-update-control-flow-app-builder-migration/ "Angular 17 Update: Control Flow &amp; App Builder Migration - ANGULARarchitects")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 18が2024-05-20にリリースされるため、その前にAngular 17へアップデートしようという記事。
Angular 17では新しい制御フローやViteへの変更なども含まれていて、アップデート方法について。


----

## Introducing Firebase App Hosting
[firebase.blog/posts/2024/05/introducing-app-hosting/](https://firebase.blog/posts/2024/05/introducing-app-hosting/ "Introducing Firebase App Hosting")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firebase</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Firebase App Hostingについて。
設定なしでAngularとNext.jsをサポートするCloud Runベースのホスティングサービス


----

## State of HTML 2023
[2023.stateofhtml.com/en-US/](https://2023.stateofhtml.com/en-US/ "State of HTML 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">Survey</span></p>

State of HTML 2023の結果が公開された。
HTMLの要素や属性、Web Components、アクセシビリティ、課題や欲しい機能についてのアンケート


----

## Digging for SSRF in NextJS apps
[www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps](https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps "Digging for SSRF in NextJS apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Next.js 14.1.1で修正されたSSRFの脆弱性について。
Server Actionsで`redirect()`を使ったパスリダイレクトをしてるAPIがある場合に、Next.jsから任意のURLに対してGETリクエストした内容を取得できるSSRF脆弱性について

- [Next.js Server-Side Request Forgery in Server Actions · CVE-2024-34351 · GitHub Advisory Database](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g "Next.js Server-Side Request Forgery in Server Actions · CVE-2024-34351 · GitHub Advisory Database")
- [azu/nextjs-CVE-2024-34351: poc](https://github.com/azu/nextjs-CVE-2024-34351 "azu/nextjs-CVE-2024-34351: poc")

----

## Introducing the CSS anchor positioning API  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/anchor-positioning-api](https://developer.chrome.com/blog/anchor-positioning-api "Introducing the CSS anchor positioning API  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Anchor Positioning APIについて。
コンセプト、基本的な使い方、popover属性や`<dialog>`との組み合わせ、`@position-try`での代替の位置指定、スクロールとの組み合わせなど


----

## React Compiler – React
[react.dev/learn/react-compiler](https://react.dev/learn/react-compiler "React Compiler – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">document</span></p>

React Compilerが実験的に公開された。
Babelプラグインとして実装されていて、opt-inでの導入方法や`react-compiler-healthcheck`での互換性のチェック、ESLintプラグインについて書かれている


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Platform Status
[webstatus.dev/](https://webstatus.dev/ "Web Platform Status")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">webservice</span></p>

ウェブプラットフォームのブラウザのステータスをまとめてるページ。
機能ごとのブラウザサポートの表示、検索などができる


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## farzher/fuzzysort: Fast SublimeText-like fuzzy search for JavaScript.
[github.com/farzher/fuzzysort](https://github.com/farzher/fuzzysort "farzher/fuzzysort: Fast SublimeText-like fuzzy search for JavaScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search</span> <span class="jser-tag">library</span></p>

fuzzy searchライブラリ


----
