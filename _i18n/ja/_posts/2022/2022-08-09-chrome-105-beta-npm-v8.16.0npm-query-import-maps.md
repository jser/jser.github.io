---
title: "2022-08-09のJS: Chrome 105 Beta、npm v8.16.0(npm query)、Import Maps"
author: "azu"
layout: post
date : 2022-08-09T04:04:13.003Z
category: JSer
tags:
- React
- mail
- performance
- DOM
- puppeteer

---

JSer.info #604 - Chrome 105 Betaがリリースされました。

- [Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More](https://blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html)

Chrome 105 betaでは、Custom Highlight APIの実装、Container Queryの実装、`:has`擬似クラスの実装、Fetch Upload Streamingの実装などが追加されています。
また、`navigator.mediaDevices.getDisplayMedia`に`systemAudio`オプションの追加、HTML Sanitizer APIの追加、`import.meta.resolve()`メソッドの追加、`Response.json()`メソッドの追加なども行われています。

非推奨だったWebSQLがSecure Context以外では利用できなくなるようになり、Cookieのドメイン属性に非Ascii文字のサポートが非推奨となるといった変更も行われています。

----

npm 8.16.0がリリースされました。

- [Release v8.16.0 · npm/cli](https://github.com/npm/cli/releases/tag/v8.16.0)

npm 8.16.0では`npm query`というCSSセレクタライクなクエリで依存関係を検索できるコマンドが追加されています。

たとえば、次のコマンドでは`license`フィールドが`MIT`のパッケージを一覧できます。

```
npm query "[license=MIT]"
```

詳細は次の記事やRFCを参照してください。

- [Introducing the new npm Dependency Selector Syntax | GitHub Changelog](https://github.blog/changelog/2022-08-03-introducing-the-new-npm-dependency-selector-syntax/)
- [rfcs/0000-dependency-selector-syntax.md at 3d5b2130504139bdc8a3b599923aa07d2ff79c96 · npm/rfcs](https://github.com/npm/rfcs/blob/3d5b2130504139bdc8a3b599923aa07d2ff79c96/accepted/0000-dependency-selector-syntax.md)

----

[Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog](https://www.honeybadger.io/blog/import-maps/)という記事では、Import Mapsについて解説されています。

Import Mapsの使い方、動的なImport Mapsの作り方、ファイル名のハッシュとキャッシュ、同じモジュールの複数バージョンの利用、CDNの利用などについて紹介されています。


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v7.0.0 · riot/riot
[github.com/riot/riot/releases/tag/v7.0.0](https://github.com/riot/riot/releases/tag/v7.0.0 "Release v7.0.0 · riot/riot")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Riot.js v7.0.0リリース。
ESM bundleの改善、runtime `slots`の追加、bundleサイズの改善など


----

## Release Inferno v8.0.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v8.0.0](https://github.com/infernojs/inferno/releases/tag/v8.0.0 "Release Inferno v8.0.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v8.0.0リリース。
コンポーネントのライフサイクルメソッドに`componentWillMove`/`componentDidAppear`/`componentWillDisappear`を追加、`javascript:`へのリンクに対して警告を追加、TypeScriptの型定義の改善など


----

## Release v16.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v16.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v16.0.0 "Release v16.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v16.0.0リリース。
CDP(Chrome DevTools Protocol)のauto-attachメカニズムを使うことで、PageやFrameへの接続の安定性を改善するなど


----

## Release v2.7.0 · parcel-bundler/parcel
[github.com/parcel-bundler/parcel/releases/tag/v2.7.0](https://github.com/parcel-bundler/parcel/releases/tag/v2.7.0 "Release v2.7.0 · parcel-bundler/parcel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v2.7.0リリース。
プラグイン設定ファイルの拡張子`.cjs`が利用できるように、React Freshで`@emotion/react`をサポートなど


----

## Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More
[blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html](https://blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html "Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 105 betaリリース。
Custom Highlight APIの実装、Container Queryの実装、`:has`擬似クラスの実装、Fetch Upload Streamingの実装など。
`navigator.mediaDevices.getDisplayMedia`に`systemAudio`オプションの追加、HTML Sanitizer APIの追加、`import.meta.resolve()`メソッドの追加、`Response.json()`メソッドの追加。
WebSQLがSecure Context以外では利用できなくなるように、Cookieのドメイン属性に非Ascii文字のサポートの廃止など


----

## Release bun v0.1.7 · oven-sh/bun
[github.com/oven-sh/bun/releases/tag/bun-v0.1.7](https://github.com/oven-sh/bun/releases/tag/bun-v0.1.7 "Release bun v0.1.7 · oven-sh/bun")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Bun 0.1.7リリース。
`bun init`コマンドの追加、`bun install`がprivate npm registryのサポート、`bun installl`がプロジェクトルートの`prepare`などのlifecycle hookに対応など


----

## Release v8.16.0 · npm/cli
[github.com/npm/cli/releases/tag/v8.16.0](https://github.com/npm/cli/releases/tag/v8.16.0 "Release v8.16.0 · npm/cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm v8.16.0リリース。
CSSセレクタライクなクエリで依存関係を検索できる`npm query`コマンドの追加など

- [Introducing the new npm Dependency Selector Syntax | GitHub Changelog](https://github.blog/changelog/2022-08-03-introducing-the-new-npm-dependency-selector-syntax/ "Introducing the new npm Dependency Selector Syntax | GitHub Changelog")

----
<h1 class="site-genre">アーティクル</h1>

----

## Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog
[www.honeybadger.io/blog/import-maps/](https://www.honeybadger.io/blog/import-maps/ "Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Import Mapsについての記事。
Import Mapsの使い方、動的なImport Mapsの作り方、ファイル名のハッシュとキャッシュ、同じモジュールの複数バージョンの利用、CDNの利用など


----

## 500ms to 1.7ms In React: A Journey And A Checklist | Orizens
[orizens.com/blog/500ms-to-1-7ms-in-react-a-journey-and-a%20checklist/](https://orizens.com/blog/500ms-to-1-7ms-in-react-a-journey-and-a%20checklist/ "500ms to 1.7ms In React: A Journey And A Checklist | Orizens")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Reactアプリのパフォーマンスをどう改善していくかについて。
コンポーネントの分割、メモ化、プロファイラーを使ったCustom Hooksの問題の追い方について


----

## Parsing command line arguments with \`util.parseArgs()\` in Node.js
[2ality.com/2022/08/node-util-parseargs.html](https://2ality.com/2022/08/node-util-parseargs.html "Parsing command line arguments with \`util.parseArgs()\` in Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 18.3.0で追加された`utils`モジュールの`parseArgs`関数について

- [Util | Node.js v18.7.0 Documentation](https://nodejs.org/api/util.html#utilparseargsconfig "Util | Node.js v18.7.0 Documentation")

----

## Checking if a JavaScript native function is monkey patched · mmazzarolo.com
[mmazzarolo.com/blog/2022-07-30-checking-if-a-javascript-native-function-was-monkey-patched/](https://mmazzarolo.com/blog/2022-07-30-checking-if-a-javascript-native-function-was-monkey-patched/ "Checking if a JavaScript native function is monkey patched · mmazzarolo.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptでネイティブ関数がmonkey patchによって上書きされているかを判定する方法について。


----

## LINE MUSIC のパフォーマンスを向上させた Vue3 マイグレーション
[engineering.linecorp.com/ja/blog/vue3-migration-with-improved-line-music-performance/](https://engineering.linecorp.com/ja/blog/vue3-migration-with-improved-line-music-performance/ "LINE MUSIC のパフォーマンスを向上させた Vue3 マイグレーション")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">refactoring</span></p>

Vue 2.xからVue 3へのアップグレード方法とbundle sizeの変化についての記事。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## sofn-xyz/mailing: Build, test, send emails with React
[github.com/sofn-xyz/mailing](https://github.com/sofn-xyz/mailing "sofn-xyz/mailing: Build, test, send emails with React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">mail</span> <span class="jser-tag">library</span></p>

Reactコンポーネントを使ってメールコンテンツの開発ができるツールキット。
MJMLをベースにしていて、ローカルでメールのレンダリング結果を見ながらコンポーネントベースでメールコンテンツを作成できる

- [MJML - The Responsive Email Framework](https://mjml.io/ "MJML - The Responsive Email Framework")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mjmlio/mjml: MJML: the only framework that makes responsive-email easy
[github.com/mjmlio/mjml](https://github.com/mjmlio/mjml "mjmlio/mjml: MJML: the only framework that makes responsive-email easy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mail</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

MJMLマークアップ言語を元にレスポンシブなメールを作成できるフレームワーク


----
