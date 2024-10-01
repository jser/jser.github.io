---
title: "2024-10-01のJS: Oxc Transformer Alpha、Node.jsの9つの柱、Expres.js 5.0 pre-release"
author: "azu"
layout: post
date: 2024-10-01T01:37:42.326Z
category: JSer
tags:
- nodejs
- TypeScript
- Tools
- Rust
- React

---

JSer.info #709 - TypeScriptのTranspilerであるoxc-transformのαリリースされました。

- [Oxc Transformer Alpha | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2024-09-29-transformer-alpha.html)

Rustで書かれたTypeScript to JavaScriptのtranspilerで、isolatedDeclarationsに対応した型定義ファイルの生成にも対応しています。

---

[The Nine Node Pillars](https://www.platformatichq.com/node-principles)は、Node.jsアプリケーションの9つのプラクティスについて書かれたドキュメントです。

次のような項目について、Node.jsでのアプリケーション開発について書かれています。

- イベントループをブロックしない
- メトリクスを監視して行動する
- Node.js LTSを使う
- テスト、レビューなどの自動化
- 依存関係の管理、monorepo
- 依存関係のリスクとアップデート
- グローバルを避ける
- エラーハンドリング、意味あるログを出す
- API Specとクライアントの自動生成

---

express v5.0.0のpre-releaseが行われています。

- [Release 5.0.0 · expressjs/express](https://github.com/expressjs/express/releases/tag/v5.0.0)
- [Migrating to Express 5](https://expressjs.com/en/guide/migrating-5.html)


[What's New in Express.js v5.0](https://www.trevorlasn.com/blog/whats-new-in-express-5)という記事では、
Express 5.0(pre-release)の変更点についてまとめられています。
`app.del()`/`app.param(fn)`/`req.param(name)`の削除、Path Routeのマッチングが正規表現としてStrictなものへと変更されています。
また、RouterのHandlerがasync awaitをサポート、Node.js 18未満のサポートを終了などの変更が含まれています。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.9.0 - LGTM! · solidjs/solid
[github.com/solidjs/solid/releases/tag/v1.9.0](https://github.com/solidjs/solid/releases/tag/v1.9.0 "Release v1.9.0 - LGTM! · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Solid</span> <span class="jser-tag">ReleaseNote</span></p>

Solid v1.9.0リリース。
JSXの検証の改善、Custom Elementのサポート改善、`handleEvent`のサポート


----

## Release v2.0.0 · unjs/jiti
[github.com/unjs/jiti/releases/tag/v2.0.0](https://github.com/unjs/jiti/releases/tag/v2.0.0 "Release v2.0.0 · unjs/jiti")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

jiti v2.0.0リリース。
JSXのサポート、CJS/ESMのdual pacakgeとして公開するように、`jiti/native`の追加、`jiti/register`の追加など。


----

## OpenNext - OpenNext
[opennext.js.org/](https://opennext.js.org/ "OpenNext - OpenNext")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">aws</span> <span class="jser-tag">library</span></p>

Next.jsをVercel以外でセルフホストできるようにするため、アーキテクチャの設計やアダプターの実装。
AWSとCloudflare向けのアダプターが開発されている


----

## End of life for Actions Node16 - GitHub Changelog
[github.blog/changelog/2024-09-25-end-of-life-for-actions-node16/](https://github.blog/changelog/2024-09-25-end-of-life-for-actions-node16/ "End of life for Actions Node16 - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">news</span></p>

2024年10月15日にGitHub ActionsでのNode.js 16のサポートが終了する。


----

## helmet/CHANGELOG.md at main · helmetjs/helmet
[github.com/helmetjs/helmet/blob/main/CHANGELOG.md#800](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#800 "helmet/CHANGELOG.md at main · helmetjs/helmet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

helmet v8.0.0リリース。
Node.js 18未満のサポートを終了、
`Strict-Transport-Security`のmax-ageがデフォルトで365日に変更など


----

## Oxc Transformer Alpha | The JavaScript Oxidation Compiler
[oxc.rs/blog/2024-09-29-transformer-alpha.html](https://oxc.rs/blog/2024-09-29-transformer-alpha.html "Oxc Transformer Alpha | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Rust</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScriptのTranspilerであるoxc-transformのαリリース。


----

## The Nine Node Pillars
[www.platformatichq.com/node-principles](https://www.platformatichq.com/node-principles "The Nine Node Pillars")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">document</span></p>

Node.jsアプリケーションの9つのプラクティスについて書かれたドキュメント。
- イベントループをブロックしない
- メトリクスを監視して行動する
- Node.js LTSを使う
- テスト、レビューなどの自動化
- 依存関係の管理、monorepo
- 依存関係のリスクとアップデート
- グローバルを避ける
- エラーハンドリング、意味あるログを出す
- API Specとクライアントの自動生成


----

## Release @ark-ui/react@4.0.0 · chakra-ui/ark
[github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%404.0.0](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%404.0.0 "Release @ark-ui/react@4.0.0 · chakra-ui/ark")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Ark UI v4.0.0リリース。
ColorPicker/Select/Combobox/DatePickerの値の渡し方の変更など

- [Release @ark-ui/solid@4.0.0 · chakra-ui/ark](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Fsolid%404.0.0 "Release @ark-ui/solid@4.0.0 · chakra-ui/ark")
- [Release @ark-ui/vue@4.0.0 · chakra-ui/ark](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Fvue%404.0.0 "Release @ark-ui/vue@4.0.0 · chakra-ui/ark")

----

## Release Notes for Safari Technology Preview 204 | WebKit
[webkit.org/blog/15978/release-notes-for-safari-technology-preview-204/](https://webkit.org/blog/15978/release-notes-for-safari-technology-preview-204/ "Release Notes for Safari Technology Preview 204 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 204リリース。
CSSの`line-clamp`をpreviewサポート、Cookie Store APIのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## What&#039;s New in Express.js v5.0
[www.trevorlasn.com/blog/whats-new-in-express-5](https://www.trevorlasn.com/blog/whats-new-in-express-5 "What&#039;s New in Express.js v5.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">express</span> <span class="jser-tag">article</span></p>

Express 5.0(pre-release)の変更点について。
`app.del()`/`app.param(fn)`/`req.param(name)`の削除、Path Routeのマッチングが正規表現としてStrictなものへと変更。
RouterのHandlerがasync awaitをサポート、Node.js 18未満のサポートを終了など

- [Migrating to Express 5](https://expressjs.com/en/guide/migrating-5.html "Migrating to Express 5")

----

## Jotaiのatomを自由にテストしたいときに見る記事
[zenn.dev/yuneco/articles/jotai-atom-testing](https://zenn.dev/yuneco/articles/jotai-atom-testing "Jotaiのatomを自由にテストしたいときに見る記事")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Jotaiのテスト方法について


----

## Node.js 20 upgrade: a journey through unexpected HEAP issues with Kubernetes | by Ztec | Sep, 2024 | Deezer I/O
[deezer.io/node-js-20-upgrade-a-journey-through-unexpected-heap-issues-with-kubernetes-27ae3d325646](https://deezer.io/node-js-20-upgrade-a-journey-through-unexpected-heap-issues-with-kubernetes-27ae3d325646 "Node.js 20 upgrade: a journey through unexpected HEAP issues with Kubernetes | by Ztec | Sep, 2024 | Deezer I/O")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js 18から20へアップデートすると平均応答時間やCPUの使用率がわずかに増加し、その原因を探索していく記事。
HeapとGCのメトリクスを見ていくと、GCが頻繁に起きるようになっており、リリースノートを探すとV8のHeapスペースのデフォルト値が変更されていることを発見するまでの話


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mieszkosabo/tartak: Tartak is a functional programming language that compiles to TypeScript types.
[github.com/mieszkosabo/tartak](https://github.com/mieszkosabo/tartak "mieszkosabo/tartak: Tartak is a functional programming language that compiles to TypeScript types.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">language</span> <span class="jser-tag">Tools</span></p>

TypeScriptの型へとコンパイルできる関数型言語


----
<h1 class="site-genre">書籍関係</h1>

----

## ［作って学ぶ］ブラウザのしくみ──HTTP、HTML、CSS、JavaScriptの裏側 | 土井 麻未 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4297145464/](https://www.amazon.co.jp/dp/4297145464/ "［作って学ぶ］ブラウザのしくみ──HTTP、HTML、CSS、JavaScriptの裏側 | 土井 麻未 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">book</span> <span class="jser-tag">Rust</span></p>

2024年11月9日 発売
Rustでシンプルなブラウザを作成しながら仕組みについて学ぶ書籍


----
