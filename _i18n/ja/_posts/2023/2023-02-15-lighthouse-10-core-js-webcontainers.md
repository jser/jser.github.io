---
title: "2023-02-15のJS: Lighthouse 10、core-js、WebContainers"
author: "azu"
layout: post
date : 2023-02-15T04:33:33.465Z
category: JSer
tags:
- performance
- TypeScript
- browser
- Tools
- node.js

---

JSer.info #631 - LightHouse 10がリリースされました。

- [What's new in Lighthouse 10 - Chrome Developers](https://developer.chrome.com/blog/lighthouse-10-0/)
- [Release v10.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v10.0.0)

LightHouse 10では、スコアからTTIが削除され、CLSにスコアが移行されています。
また、AuditとしてBFCacheの検証、ペースト禁止の検証の追加されています。
その他には、LightHouseのJSON出力の構造が変更されています。

関連する内容として、[CrUX History API](https://developer.chrome.com/docs/crux/history-api/)というChrome User Experience Report (CrUX) の履歴データを取得するAPIがリリースされています。
特定のページのWeb Vitalsの値のデータを1週間単位で取得できます。

- [Introducing historical web performance data via the CrUX History API - Chrome Developers](https://developer.chrome.com/en/blog/chrome-ux-report-history-api/)

---

core-js 3.28.0がリリースされました。

- [Release 3.28.0 - 2023.02.14 · zloirock/core-js](https://github.com/zloirock/core-js/releases/tag/v3.28.0)

core-js 3.28.0では、[2023-01のTC 39 Meetingsの結果](https://ecmascript-daily.github.io/ecmascript/2023/02/03/ecmascript-proposal-update)を反映した変更が含まれています。

- Stage4となったChange Array by copy proposalをStableに移動
- Stage3の`JSON.parse` source text access、`ArrayBuffer.prototype.transfer`、Explicit Resource Managementを追加
- Stage 2のSymbol Predicatesを実装
- Stage 1の`Number.range`を`Iterator.range`に変更

また、core-jsの歴史、財政的な支援の募集や今後の方針についての記事も公開されています。

- [core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub](https://github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md)

オープンソースのメンテナンスと財政的な話については[Working in Public](https://press.stripe.com/working-in-public)という書籍がよくまとまっています。
Babelやcore-jsのように少人数のメンテナーと多くのユーザーというように比率が大きく異なるプロジェクトは、スタジアムモデルという形に分類されて紹介されています。

また、ソフトウェアはほぼ無料で配布できるため、利用者の数は増え続け、メンテナンスにかかる費用が高くなるという問題が知られています。
（オープンソース）ソフトウェアを購入する動機は減っている一方で、その社会的価値は劇的に上昇していて、多くの人やサイトはオープンソースソフトウェアに依存しています。
そのため、オープンソースコードはメンテナンスが必要な公共インフラストラクチャの一種であるという話もされています。

オープンソースへ財政的な支援をする個人や企業は増えています。
一方でソフトウェアの依存関係は膨大になっているため、どのように支援すればいいかわからない問題も指摘されています。

📝 依存関係から自動的に分配するサービスもあります。

- [thanks.dev – open source funding platform](https://thanks.dev/home)
- [StackAid - Fund all your open source dependencies](https://www.stackaid.us/)

また、特定の人へのSponsorは「寄付」の概念と混同されやすいですが、どちらかというそのクリエイターの将来の仕事に対する期待、関心に紐づくので、サブスクリプションのようなものという話もあります。
そのため、特定のプロジェクトに対するSponsorではなく、特定の人に対するSponsorという文化的な変化も起きているという話が紹介されていました。
（これは、プロジェクトが成長段階に入るとコードを書く開発者以外にも、モデレートやドキュメントなどを中心にする人の重要度が高くなっていくという話とも関係しています）

この本の出版後なので含まれていませんが、Babelでも同様の話がされていたので、興味があるひとは読むと良いかもしれません。

- [Babel is used by millions, so why are we running out of money? · Babel](https://babeljs.io/blog/2021/05/10/funding-update)


---

- [WebContainers - Dev environments. In your web app. | WebContainers](https://webcontainers.io/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 163 | WebKit
[webkit.org/blog/13839/release-notes-for-safari-technology-preview-163/](https://webkit.org/blog/13839/release-notes-for-safari-technology-preview-163/ "Release Notes for Safari Technology Preview 163 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 163リリース。
CSS GridのMasonry layoutをデフォルトで有効化、`StorageManager.estimate()`のサポート、Web Crypto APIがEd25519をサポート。
非標準な`HTMLHeadElement.profile`や`HTMLFrameElement.location`などを削除


----

## Release v3.2.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.2.0](https://github.com/nuxt/nuxt/releases/tag/v3.2.0 "Release v3.2.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Nuxt.js v3.2.0リリース。
Nuxt DevToolsの追加、`useFetch`でのリクエストに自動的にCookieが付くように。
サーバのコードからclient-only componentを取り除く`treeshakeClientOnly`がデフォルトで`true`へと変更など。


----

## What&#039;s new in Lighthouse 10 - Chrome Developers
[developer.chrome.com/blog/lighthouse-10-0/](https://developer.chrome.com/blog/lighthouse-10-0/ "What&#039;s new in Lighthouse 10 - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 10リリース。
スコアからTTIが削除され、CLSにスコアが移行する。
AuditとしてBFCacheの検証、ペースト禁止の検証の追加。
Lighthouseの結果であるJSONの構造の変更など

- [Release v10.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v10.0.0 "Release v10.0.0 · GoogleChrome/lighthouse")

----

## Electron 23.0.0 | Electron
[www.electronjs.org/blog/electron-23-0](https://www.electronjs.org/blog/electron-23-0 "Electron 23.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 23.0.0リリース。
Chromium 110、Node.js 18.12.1、V8 11.0へのアップデート。
Windows 7/8/8.1のサポートを終了、`scroll-touch-*`イベントの削除。
機能追加としてWebUSB APIのサポートなど


----

## Release v1 Because I finally got around to it · jquense/yup
[github.com/jquense/yup/releases/tag/v1.0.0](https://github.com/jquense/yup/releases/tag/v1.0.0 "Release v1 Because I finally got around to it · jquense/yup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

スキーマを組み上げてバリデーションできるyup 1.0.0リリース。
`tuple`の追加、bundleしたファイルを配布するように、`when` APIの変更、emailバリデーションをWHATWGの定義と同じものへ変更。
`cast`に`ignore-optionality`オプションを追加、型処理のパフォーマンス改善と`Objectschema`クラスの追加など

- [How do I migrate to v1 · Issue #1906 · jquense/yup](https://github.com/jquense/yup/issues/1906 "How do I migrate to v1 · Issue #1906 · jquense/yup")

----

## Release DOMPurify 3.0.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/3.0.0](https://github.com/cure53/DOMPurify/releases/tag/3.0.0 "Release DOMPurify 3.0.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

DOMpurify 3.0.0リリース。
IEのサポートを終了、`ALLOW_SELF_CLOSE_IN_ATTRP`オプションの追加など


----

## Release 3.28.0 - 2023.02.14 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.28.0](https://github.com/zloirock/core-js/releases/tag/v3.28.0 "Release 3.28.0 - 2023.02.14 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.28.0リリース。
Stage4となったChange Array by copy proposalをStableに移動。
Stage3の`JSON.parse` source text access、`ArrayBuffer.prototype.transfer`、Explicit Resource Managementを追加。
Stage 2のSymbol Predicatesを実装、Stage 1の`Number.range`を`Iterator.range`に変更など


----

## Nextra 2 – Next.js Static Site Generator – The Guild
[the-guild.dev/blog/nextra-2](https://the-guild.dev/blog/nextra-2 "Nextra 2 – Next.js Static Site Generator – The Guild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.jsベースの静的サイトジェネレータであるNextra 2リリース。
MDX2のサポート、Markdownのインポート、Next 13に対応、リモートのMarkdownファイルを読み込んでレンダリングできるように、FlexSearchを使った全文検索のサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Bringing Javascript to WebAssembly for Shopify Functions (2023)
[shopify.engineering/javascript-in-webassembly-for-shopify-functions](https://shopify.engineering/javascript-in-webassembly-for-shopify-functions "Bringing Javascript to WebAssembly for Shopify Functions (2023)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptをWasmにして実行する仕組みについて。
QuickJSを使いJavaScriptをByteCodeにした`script.wasm`を作成し、`QuickJS.wasm`と動的にリンクして大部分を共有している。

Shopify Functionで利用されるが、非同期処理の制限や5ms未満での実行制限がある。現在はRustで作成したWasmより3枚ていど遅いが、今後はSpiderMonkeyの利用やJITについてやっていく。

- [Shopify/javy: JS to WebAssembly toolchain](https://github.com/Shopify/javy "Shopify/javy: JS to WebAssembly toolchain")

----

## Speculation Rules API によるプリレンダリングのためのメトリクス設計
[nhiroki.jp/2023/02/13/metrics-for-prerendering](https://nhiroki.jp/2023/02/13/metrics-for-prerendering "Speculation Rules API によるプリレンダリングのためのメトリクス設計")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Speculation Rules APIのPreRenderingについて。
Prerenderした場合の`navigationStart`は事前実行のタイミングとなるため、`activationStart`というメトリクスが追加された点。
また、Predenderが実際に利用されているかの判定方法について


----

## Improved type safety in Storybook 7
[storybook.js.org/blog/improved-type-safety-in-storybook-7/](https://storybook.js.org/blog/improved-type-safety-in-storybook-7/ "Improved type safety in Storybook 7")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Storybook 7でのTypeScriptの型について。
`StroyObj`タイプや`satisfies`演算子を使ってexportするコンポーネントの定義に型を付ける話


----

## Understanding App Directory Architecture In Next.js — Smashing Magazine
[www.smashingmagazine.com/2023/02/understanding-app-directory-architecture-next-js/](https://www.smashingmagazine.com/2023/02/understanding-app-directory-architecture-next-js/ "Understanding App Directory Architecture In Next.js — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.jsの`app`ディレクトリについての記事


----

## A Historical Reference of React Criticism—zachleat.com
[www.zachleat.com/web/react-criticism/](https://www.zachleat.com/web/react-criticism/ "A Historical Reference of React Criticism—zachleat.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">history</span></p>

Reactに対する批判の歴史についての記事


----

## core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub
[github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md](https://github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md "core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">article</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">opinion</span></p>

core-jsの歴史、財政的な問題、ロードマップについて。
また、多くのウェブサイトが複数のバージョンの`core-js`を同じページに読み込んでいるパッケージの依存関係の問題について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## WebContainers - Dev environments. In your web app. | WebContainers
[webcontainers.io/](https://webcontainers.io/ "WebContainers - Dev environments. In your web app. | WebContainers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

Node.jsをWebブラウザ上で動作させて、Playgroundなどに利用できるWebContainersのAPIとパッケージが公開された


----

## Introducing historical web performance data via the CrUX History API - Chrome Developers
[developer.chrome.com/en/blog/chrome-ux-report-history-api/](https://developer.chrome.com/en/blog/chrome-ux-report-history-api/ "Introducing historical web performance data via the CrUX History API - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

CrUX History APIで1週間間隔のデータを6ヶ月間分の履歴が確認できるようになった。
WebVitalsのデータを各ページレベルでも取得できるようになっている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## upgradejs/depngn: A CLI tool to find out if your dependencies support a given version of node.
[github.com/upgradejs/depngn](https://github.com/upgradejs/depngn "upgradejs/depngn: A CLI tool to find out if your dependencies support a given version of node.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

インストールされている依存関係の`engines`フィールドを見て、指定したNode.jsバージョンが条件を満たすかを一覧できるツール


----

## slashd-analytics/run: Run user-provided code in a Web Worker
[github.com/slashd-analytics/run](https://github.com/slashd-analytics/run "slashd-analytics/run: Run user-provided code in a Web Worker")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span></p>

Web Workerを一種のSandboxとして使い、任意のJSコードを実行するライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Design Patterns in TypeScript
[refactoring.guru/design-patterns/typescript](https://refactoring.guru/design-patterns/typescript "Design Patterns in TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span> <span class="jser-tag">book</span></p>

TypeScriptでのデザインパターンについてまとめたサイト


----
