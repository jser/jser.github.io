---
title: "2023-01-06のJS:  Vue 2のEOLは2023年末、NextAuthはAuth.jsに、React NativeのFirst-class Support for TypeScript"
author: "azu"
layout: post
date : 2023-01-06T03:37:03.041Z
category: JSer
tags:
- node.js
- React
- Tools
- browser
- book

---

JSer.info #625 - [2022 Year In Review | The Vue Point](https://blog.vuejs.org/posts/2022-year-in-review.html)という記事では、Vue 2のEnd of Life (EOL)が改めて周知されています。

- [Vue.js - Vue 2 LTS, EOL & Extended Support](https://v2.vuejs.org/lts/)

Vue.js 2は2023年12月31日にEOLとなり、サポートが終了されます。
サポート終了後はセキュリティリリースも行われなくなる予定です。

---

[NextAuth.js](https://next-auth.js.org/)が[Auth.js](https://authjs.dev/)の一部という扱いに変更されました。
これによって、SvelteKitやSolidStartでもNextAuthが実装していた認証、認可の仕組みが利用できるようになっています。

---

React NativeがTypeScriptをFirst-classとしてサポートすることが発表されました。

- [First-class Support for TypeScript · React Native](https://reactnative.dev/blog/2023/01/03/typescript-first)

型定義ファイルの同梱やテンプレートもTypeScriptがデフォルトとなるようです。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Prototype Pollution in JSON5 via Parse Method · CVE-2022-46175 · GitHub Advisory Database
[github.com/advisories/GHSA-9c47-m6qq-7p4h](https://github.com/advisories/GHSA-9c47-m6qq-7p4h "Prototype Pollution in JSON5 via Parse Method · CVE-2022-46175 · GitHub Advisory Database")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

JSON5にprototype pollutionの脆弱性があり、2.2.2と1.0.2で修正された。

- [Release v2.2.2 · json5/json5](https://github.com/json5/json5/releases/tag/v2.2.2 "Release v2.2.2 · json5/json5")
- [Release v1.0.2 · json5/json5](https://github.com/json5/json5/releases/tag/v1.0.2 "Release v1.0.2 · json5/json5")

----

## Tamagui 1.0 🎉 — Tamagui
[tamagui.dev/blog/version-one](https://tamagui.dev/blog/version-one "Tamagui 1.0 🎉 — Tamagui")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React向けのUIフレームワークであるTamagui 1.0リリース。
React NativeとWebどちらも対応し、スタイリングライブラリも含む。1.0ではNativeとWebの互換性の向上やバンドルサイズの改善などが行われている。


----

## Vue.js
[v2.vuejs.org/lts/](https://v2.vuejs.org/lts/ "Vue.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">document</span></p>

Vue 2のサポート終了は2023年12月31日。
サポート終了後はセキュリティ修正を提供しない、拡張LTSはAngularJSと同じく外部企業に依頼する形となる予定

- [2022 Year In Review | The Vue Point](https://blog.vuejs.org/posts/2022-year-in-review.html "2022 Year In Review | The Vue Point")

----

## Release v0.16.13 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.16.13](https://github.com/evanw/esbuild/releases/tag/v0.16.13 "Release v0.16.13 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.16.13リリース。
`--metafile`でbundle時のメタデータを出力し、メタデータを可視化できるビューアサイトの実装など


----

## First-class Support for TypeScript · React Native
[reactnative.dev/blog/2023/01/03/typescript-first](https://reactnative.dev/blog/2023/01/03/typescript-first "First-class Support for TypeScript · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.71でTypeScriptの型定義が同梱され、新しいテンプレートもデフォルトでTypeScriptを利用するようになった


----

## Node v18.13.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v18.13.0/](https://nodejs.org/en/blog/release/v18.13.0/ "Node v18.13.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.13.0リリース。
`File` APIの実装、`node:test`モジュールに`mock` APIの追加、v8 snapshot compressionを無効化して起動速度の向上など


----

## Release v6.4.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v6.4.0](https://github.com/lerna/lerna/releases/tag/v6.4.0 "Release v6.4.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span></p>

lerna v6.4.0リリース。
`lerna watch`コマンドの追加など

----

## Auth.js
[authjs.dev/](https://authjs.dev/ "Auth.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAuthentication</span> <span class="jser-tag">OAuth</span> <span class="jser-tag">library</span></p>

NextAuthはAuth.jsとなり、Next.js以外にもSvelteKitやSolidStartなどをサポートするようになった。


----

## Gluon
[gluonjs.org/](https://gluonjs.org/ "Gluon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">deno</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

ChromeとFirefoxをWebViewの代わりにデスクトップアプリを作るフレームワーク。
デスクトップブラウザの起動オプションで単独のアプリらしく起動させる。
バックエンドにはNode.jsとDenoが利用でき、アプリと連携できるAPIが用意されている。


----
<h1 class="site-genre">アーティクル</h1>

----

## そろそろカスケードレイヤー(@layer)と向き合う
[zenn.dev/yend724/articles/20221227-fcz1jh70bhnqof2v](https://zenn.dev/yend724/articles/20221227-fcz1jh70bhnqof2v "そろそろカスケードレイヤー(@layer)と向き合う")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSの@layerについての解説記事


----

## Interop 2022: end of year update
[web.dev/interop-2022-wrapup/](https://web.dev/interop-2022-wrapup/ "Interop 2022: end of year update")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

ウェブブラウザの相互運用性の取り組みであるInterop 2022の結果のまとめ


----

## Miško HeveryのQwik記事シリーズ | POSTD
[postd.cc/series-qwik/](https://postd.cc/series-qwik/ "Miško HeveryのQwik記事シリーズ | POSTD")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Qwikシリーズの翻訳記事


----
<h1 class="site-genre">書籍関係</h1>

----

## 実践Node.js入門 | 伊藤 康太 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4297129566/](https://www.amazon.co.jp/dp/4297129566/ "実践Node.js入門 | 伊藤 康太 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">book</span></p>

2023年1月26日 発売。
Node.jsでのCLIやアプリケーション開発についての書籍


----
