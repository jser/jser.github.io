---
title: "2021-08-31のJS: TypeScript 4.4、PageSpeed InsightsのLab/Field data、Packemon(ライブラリ向けビルドツール)"
author: "azu"
layout: post
date : 2021-08-30T22:46:59.689Z
category: JSer
tags:
- node.js
- Chrome
- TypeScript
- browser
- React

---

JSer.info #555 - TypeScript 4.4が正式にリリースされました。

- [Announcing TypeScript 4.4 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/)

Control Flow Analysisの改善、Index SignaturesにSymbolやTemplate Stringを利用できるようになっています。
また、Catch節のデフォルトを`unknown`型にする`useUnknownInCatchVariables`オプションと
optionalと`undefined`値の区別をする`exactOptionalPropertyTypes`オプションの追加されています。

`useUnknownInCatchVariables`は`strict`オプションが有効の場合は自動的にONとなります。
一方で、`exactOptionalPropertyTypes`は`strict`オプションとは別途設定が必要になります。

また、ES Proposal Stage 3の[class static block](https://github.com/tc39/proposal-class-static-block#ecmascript-class-static-initialization-blocks)がサポートされています。
その他には、`tsc --help`の表示を改善、ビルドパフォーマンスの改善も含まれています。

----

[Why lab and field data can be different (and what to do about it)](https://web.dev/lab-and-field-data-differences/)という記事では、[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)などに表示される"lab data"と"field data"の違いについて解説しています。

Lab dataは、ネットワークは実行環境を固定したSynthetic モニタリングのデータとなっています。
一方のField dataは、[Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)で収集されたChromeユーザーのRUMデータを元にしています。

この2つのデータの違い、どのようなケースで値に違いがでるかなどを解説しています。
実際のユーザーの体験に近いのはField dataであるため、まずはField dataをみることや、2つのデータに違いがある場合には最適化の余地があることを示していることなどについて書かれています。

---

[Packemon](https://packemon.dev/)はnpmで公開するパッケージ向けのビルドツールです。

Node.js(mjs,cjs)、ブラウザ(ESM、UMD)向けのビルドを一括でできるようになっています。

Node.js 12+からサポートされたECMAScript Modules(ESM)では、利用できないNode.jsのAPIやimport時のファイル拡張子が必須となるなどのCommonJSとの違いがあります。ビルド時に、[Babelを使ったESM向けのコード変換](https://github.com/milesj/packemon/tree/master/packages/babel-plugin-cjs-esm-interop)やESMで利用できない機能をビルド時にチェックなども行います。

- [Node.jsライブラリ/ツールをESMに移行する[Node.js 12+]](https://zenn.dev/azu/scraps/8251dab75562c8)
- [Pure ESM package](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c)

その他には`packemon validate`といったパッケージのメタデータのバリデーションなどができるコマンドなども持っています。
似たツールとしては[Microbundle](https://github.com/developit/microbundle)がありますが、packemonはパッケージ公開を補助するツールも持つといった違いがあります。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v16.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.8.0/](https://nodejs.org/en/blog/release/v16.8.0/ "Node v16.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 16.8.0リリース。
`stream.Duplex.from`、 `stream.Readable.isDisturbed(stream)`の追加。
`util`モジュールに`toUSVString`の追加など


----

## Announcing TypeScript 4.4 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-4/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/ "Announcing TypeScript 4.4 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.4リリース。
Control Flow Analysisの改善、Index SignaturesにSymbolやTemplate Stringを利用できるように。
Catch節のデフォルトを`unknown`型にする`useUnknownInCatchVariables`オプションの追加。
optionalと`undefined`値の区別をする`exactOptionalPropertyTypes`オプションの追加。
また、ES Proposal Stage 3のclass static blockをサポート。
`tsc --help`の表示を改善、ビルドパフォーマンスの改善も含まれている


----

## Chromium Blog: Chrome 94 Beta: WebCodecs, WebGPU, Scheduling, and More
[blog.chromium.org/2021/08/chrome-94-beta-webcodecs-webgpu.html](https://blog.chromium.org/2021/08/chrome-94-beta-webcodecs-webgpu.html "Chromium Blog: Chrome 94 Beta: WebCodecs, WebGPU, Scheduling, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 94 Betaリリース。
Origin Trialとして、HTTP status code 103 Early Hintsを実験的にサポート。
WebCodecs、`scheduler.postTask()`、`MediaStreamTrackGenerator`/`MediaStreamTrackProcessor`のサポート。
Self Profiling APIのサポートなど。
また、WebSQLがサードパーティコンテキストでは非推奨となり、`navigator.plugins`/ `navigator.mimeTypes`は固定された値を返すように変更されるなど


----

## Announcing SWR 1.0 – SWR
[swr.vercel.app/blog/swr-v1](https://swr.vercel.app/blog/swr-v1 "Announcing SWR 1.0 – SWR")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

データ取得するReact HooksライブラリのSWR 1.0リリース。
`fallback`オプションの追加、Immutable Modeの追加、`provider`オプションの追加、`useSWRConfig`の追加。
また、Middlewareの対応、一部APIの変更、デフォルトの`fetcher`を定義しなくなるなど


----

## Release 27.1.0 · facebook/jest
[github.com/facebook/jest/releases/tag/v27.1.0](https://github.com/facebook/jest/releases/tag/v27.1.0 "Release 27.1.0 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 27.1.0リリース。
`snapshotFormat`オプションの追加、Node.js 16で追加された`node:` prefixのモジュールをサポートなど

- [Modules: CommonJS modules | Node.js v16.8.0 Documentation](https://nodejs.org/api/modules.html#modules_core_modules "Modules: CommonJS modules | Node.js v16.8.0 Documentation")

----

## mongoose/CHANGELOG.md at master · Automattic/mongoose
[github.com/Automattic/mongoose/blob/master/CHANGELOG.md#600--2021-08-24](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#600--2021-08-24 "mongoose/CHANGELOG.md at master · Automattic/mongoose")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MongoDB</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

mongoose 6.0リリース。
MongoDB Driver 4.0サポート、`sanitizeFilter`と`Trusted()`メソッドの追加、`default`に関数を渡せるように、Documentの変更をProxyで検知できるように。
破壊的な変更として、`createConnection(uri)`がthenableではなくなる、同じQueryを再実行はエラーにになる,`strictQuery`オプションを`strict`にリネーム。
また、デフォルトの挙動を変更に関連して不要となったオプションの削除やTypeScriptの型定義の変更など

- [Mongoose v6.0.2: Migrating to Mongoose 6](https://mongoosejs.com/docs/migrating_to_6.html "Mongoose v6.0.2: Migrating to Mongoose 6")
- [Introducing Mongoose 6.0.0 | www.thecodebarbarian.com](https://thecodebarbarian.com/introducing-mongoose-6.html "Introducing Mongoose 6.0.0 | www.thecodebarbarian.com")

----
<h1 class="site-genre">アーティクル</h1>

----

## Private Network Access update: Introducing a deprecation trial - Chrome Developers
[developer.chrome.com/blog/private-network-access-update/](https://developer.chrome.com/blog/private-network-access-update/ "Private Network Access update: Introducing a deprecation trial - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Chromeでのnon-secureなウェブサイトからPrivate Network Accessを制限するロードマップについて。
Chrome 94でnon-secureなPublicウェブサイトからPrivate Networkへのリクエストを送れなくなり、逆Origin Trialを開始している。
Chrome 102で逆Origin Trialを終了し、完全に制限される。


----

## Introducing Portal Windows for Electron
[blog.tandem.chat/portal-windows/](https://blog.tandem.chat/portal-windows/ "Introducing Portal Windows for Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Electron</span> <span class="jser-tag">article</span></p>

Tandemで利用しているElectronで他のウィンドウをミラーリングするライブラリについて。
他のアプリのウィンドウをReactコンポーネントとして描画、スクリーンシェアなどに利用できる。

- [cryptagon/portal-windows: Render and position native windows as simply as you render and position tooltips in your React app.](https://github.com/cryptagon/portal-windows "cryptagon/portal-windows: Render and position native windows as simply as you render and position tooltips in your React app.")

----

## Why lab and field data can be different (and what to do about it)
[web.dev/lab-and-field-data-differences/](https://web.dev/lab-and-field-data-differences/ "Why lab and field data can be different (and what to do about it)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

PageSpeed Insightsなどに表示されている定点観測データであるLab dataとRUMであるField dataについて。
それぞれのデータの違い、計測方法、キャッシュの状態、AMP/SXG、BFCacheなどの影響について。
LabとFieldがどちらもある場合は、Field dataがよりユーザーの体験に近いことについて。


----

## Modern client-side routing: the App History API
[web.dev/app-history-api/](https://web.dev/app-history-api/ "Modern client-side routing: the App History API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

Chrome 95にてフラグ付きで実装されたApp History APIについて。
問題のあるHistory APIを置き換えるAPI。
`navigation`イベントでのナビゲーションの検知、`transitionWhile(promise)`での遷移中/成功/失敗の表現、ナビゲーションエラー時のロールバックなどの具体例について。
また、Historyの管理、状態の管理、FormのSubmitにおけるナビゲーションを扱える点についてなど

- [WICG/app-history: The app history API provides a web application-focused way of managing same-origin same-frame history entries and navigations.](https://github.com/WICG/app-history "WICG/app-history: The app history API provides a web application-focused way of managing same-origin same-frame history entries and navigations.")

----

## NAN to Node-API Migration: A Short Story - NodeSource
[nodesource.com/blog/NAN-to-Node-API-migration-a-short-story](https://nodesource.com/blog/NAN-to-Node-API-migration-a-short-story "NAN to Node-API Migration: A Short Story - NodeSource")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">C++</span> <span class="jser-tag">article</span></p>

Node.jsのnative addonを開発時に利用するNANとNode-API(N-API)について。
Node-APIはV8に依存しないnative addon開発のために追加され、NANからNode-APIに移行しながら、Node-APIの使い方について見ていく記事。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## GoogleChromeLabs/ProjectVisBug: FireBug for designers › Edit any webpage, in any state https://a.nerdy.dev/gimme-visbug
[github.com/GoogleChromeLabs/ProjectVisBug](https://github.com/GoogleChromeLabs/ProjectVisBug "GoogleChromeLabs/ProjectVisBug: FireBug for designers › Edit any webpage, in any state https://a.nerdy.dev/gimme-visbug")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">debug</span> <span class="jser-tag">Design</span></p>

デザイナー向けのDevTools

- [VisBug](https://visbug.web.app/ "VisBug")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Gotta pack &#039;em all! | Packemon
[packemon.dev/](https://packemon.dev/ "Gotta pack &#039;em all! | Packemon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

ライブラリ向けのビルドツール。
Node.js(mjs,cjs)、ブラウザ(ESM、UMD)向けのビルドを一括でできる。
また、設定に応じたpackage.jsonの書き換え、Babelを使ったESM向けのコード変換、mjsで利用できない機能をビルド時にチェック、パッケージのメタデータのバリデーションなどができる。

- [azu/packemon-demo: Packemon demo package](https://github.com/azu/packemon-demo "azu/packemon-demo: Packemon demo package")

----

## 5alidz/tiny-schema-validator: JSON schema validator
[github.com/5alidz/tiny-schema-validator](https://github.com/5alidz/tiny-schema-validator "5alidz/tiny-schema-validator: JSON schema validator")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Schemaを定義してバリデーションができるbuilderライブラリ。
作成したSchemaオブジェクトはTypeScriptの型としても利用できる。

----

## unjs/unplugin: Unified plugin system for Vite, Rollup, and Webpack
[github.com/unjs/unplugin](https://github.com/unjs/unplugin "unjs/unplugin: Unified plugin system for Vite, Rollup, and Webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">rollup</span> <span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span> <span class="jser-tag">library</span></p>

Vite/Rollup/webpack pluginを同じコードから作成するライブラリ


----
