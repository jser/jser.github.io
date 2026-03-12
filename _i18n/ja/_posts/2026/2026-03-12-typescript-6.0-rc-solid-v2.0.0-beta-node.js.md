---
title: "2026-03-12のJS: TypeScript 6.0 RC、Solid v2.0.0 Beta、Node.jsリリーススケジュールの変更"
author: "azu"
layout: post
date: 2026-03-12T11:45:51.325Z
category: JSer
tags:
- npm
- nodejs
- TypeScript
- React
- Tools

---

JSer.info #766 - TypeScript 6.0 RCがリリースされました。

- [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

TypeScript 7(Go言語ベース)への移行を見据えたリリースで、多くのデフォルト設定の変更や非推奨化が含まれています。
`strict`がデフォルトで`true`に変更、`module`のデフォルトが`esnext`に変更、`target`のデフォルトが`es2025`に変更など、既存のプロジェクトへの影響が大きい変更が含まれています。
また、`target: es5`/`--moduleResolution node10`/`--module amd|umd|system`/`--outFile`などが非推奨化されています。

---

Solid v2.0.0 Betaがリリースされました。

- [Release v2.0.0 Beta - The <Suspense> is Over · solidjs/solid](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0)

非同期処理がファーストクラスとして扱われ、computationsがPromiseやasync iterablesを返せるようになっています。
`<Loading>`コンポーネントや`isPending`によるPending状態の追跡、`action()`と`createOptimistic`によるOptimistic Updateの仕組みが追加されました。
`<Index>`を`<For keyed={false}>`へ変更、`createEffect`のcompute/applyフェーズの分離、`use:`ディレクティブの削除など破壊的変更も含まれています。

---

Node.jsのリリースモデルが2026年10月から変更されることが発表されました。

- [Node.js — Evolving the Node.js Release Schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

現在の年2回のメジャーリリースから年1回に変更され、すべてのメジャーリリースがLTSとなります。
新しいリリースサイクルでは、Alpha Phase(10月〜3月)でBreaking Changesを許容し、Current Phase(4月〜10月)で安定化、その後30ヶ月のLTSフェーズとなります。
奇数/偶数バージョンの区別がなくなり、Node.js 26(2026年4月)が現行モデルの最後のリリースとなります。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v6.3.0 · actions/setup-node
[github.com/actions/setup-node/releases/tag/v6.3.0](https://github.com/actions/setup-node/releases/tag/v6.3.0 "Release v6.3.0 · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GitHub</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

setup-node v6.3.0リリース。
`devEngines`フィールドのサポート


----

## Release v2.0.0 Beta - The &lt;Suspense&gt; is Over · solidjs/solid
[github.com/solidjs/solid/releases/tag/v2.0.0-beta.0](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0 "Release v2.0.0 Beta - The &lt;Suspense&gt; is Over · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Solid</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Solid v2.0.0 Betaリリース。
非同期処理はファーストクラスとして、computationsがPromiseやasync iterablesを返せるようになった。
`<Loading>`コンポーネントや`isPending`によるPending状態の追跡、`action()`と`createOptimistic`によるOptimistic Updateの仕組みを追加。
`<Index>`を`<For keyed={false}>`へ変更、`createEffect`のcompute/applyフェーズの分離、`use:`ディレクティブの削除など。


----

## Announcing TypeScript 6.0 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/ "Announcing TypeScript 6.0 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 6.0 RCリリース。
TypeScript 7(Go言語ベース)への移行を見据えたリリースで、多くのデフォルト設定の変更や非推奨化が含まれる。
Betaからの変更として `import ... assert {...}`の廃止が延期された。
`strict`がデフォルトで`true`に変更、`module`のデフォルトが`esnext`に変更、`target`のデフォルトが`es2025`に変更、`types`のデフォルトが`[]`に変更。
`target: es5`/`--moduleResolution node10`/`--module amd|umd|system`/`--outFile`などを非推奨化。
ES2025の`RegExp.escape`やTemporalの型定義を追加、`lib.dom`に`dom.iterable`と`dom.asynciterable`を統合。
`this`を使わない関数のcontext sensitivityの改善、`#/`で始まるsubpath importsのサポートを追加。
`--moduleResolution bundler`と`--module commonjs`の組み合わせが可能に。
TypeScript 7への移行を補助する`--stableTypeOrdering`フラグの追加など。


----

## Astro 6.0 | Astro
[astro.build/blog/astro-6/](https://astro.build/blog/astro-6/ "Astro 6.0 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Vite</span></p>

Astro 6.0リリース。
ViteのEnvironment APIを使った開発サーバーの刷新により、開発時にもCloudflare WorkersやBun/Denoなどの本番ランタイムで実行可能に。
フォント管理を自動化するFonts APIの追加、リクエスト時にCMSやAPIのデータを取得できるLive Content Collectionsの追加。
CSPのサポートが安定版に。
Node.js 22以上が必須に変更、Vite 7/Shiki 4/Zod 4へのアップグレード。
Experimentalとして、GoからRustベースに書き換えたコンパイラ、Queued Rendering、Route Caching APIの追加など。


----

## Node.js — Evolving the Node.js Release Schedule
[nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule "Node.js — Evolving the Node.js Release Schedule")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">news</span></p>

Node.jsのリリースモデルを2026年10月から変更される。
現在の年2回のメジャーリリースから年1回に変更し、すべてのリリースがLTSとなる。
新しいリリースサイクルでは、Alpha Phase(10月〜3月)でBreaking Changesを許容し、Current Phase(4月〜10月)で安定化、その後30ヶ月のLTSフェーズとなる。
奇数/偶数バージョンの区別がなくなり、バージョン番号がカレンダー年と対応する(Node.js 27は2027年など)。
Node.js 26(2026年4月)が現行モデルの最後のリリースとなり、Node.js 27(2027年4月)から新しいスケジュールが適用される。


----

## Chrome 146  |  Release notes  |  Chrome for Developers
[developer.chrome.com/release-notes/146](https://developer.chrome.com/release-notes/146 "Chrome 146  |  Release notes  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 146リリース。
CSSのスクロール駆動アニメーション、`trigger-scope`プロパティのサポート。
`meta name="text-scale"`によるOS/ブラウザのテキストスケーリング設定の反映、Scoped Custom Element Registryのサポート。
`Iterator.concat()`のサポート、Sanitizer APIの追加、WebAudioのPlayback Statistics APIの追加。
WebGPUのCompatibility modeのサポート。


----

## Get features faster with Chrome&#039;s two-week release cycle  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/chrome-two-week-release?hl&#x3D;en](https://developer.chrome.com/blog/chrome-two-week-release?hl=en "Get features faster with Chrome&#039;s two-week release cycle  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">news</span></p>

Chromeのリリースサイクルを2026年9月(Chrome 153)から、4週間サイクルから2週間サイクルへ変更する。
デスクトップ、Android、iOSが対象で、DevチャネルとCanaryチャネルは変更なし。
Extended Stableチャネルは8週間サイクルのまま維持される。


----

## RedwoodSDK 1.0: Getting Out of the Weeds | Blog | RedwoodSDK
[rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds](https://rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds "RedwoodSDK 1.0: Getting Out of the Weeds | Blog | RedwoodSDK")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cloudflare Workers向けのReactフレームワークであるRedwoodSDK 1.0リリース。
旧RedwoodJSから方針を転換し、コード生成や暗黙的な規約に依存しない設計となっている。
Web標準API(fetch, Request, Response)をそのまま利用し、設定より合成(Composability)を重視するアーキテクチャを採用している。

- [Release v1.0.0 · redwoodjs/sdk](https://github.com/redwoodjs/sdk/releases/tag/v1.0.0 "Release v1.0.0 · redwoodjs/sdk")

----
<h1 class="site-genre">アーティクル</h1>

----

## Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog
[bloomberg.github.io/js-blog/post/temporal/](https://bloomberg.github.io/js-blog/post/temporal/ "Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TC39</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ECMAScript ProposalのTemporalがStage 4となりES2026に含まれることが決定するまでの経緯についての記事。
JavaScriptの`Date`オブジェクトが抱えるミュータブルな設計、タイムゾーン対応の不足、曖昧なパースなどの問題と、それを解決するためにTemporalがどのように設計されたかを解説している。
Temporalはイミュータブルな設計、タイムゾーンとカレンダーのネイティブサポート、ナノ秒精度などの特徴を持つ。
`ZonedDateTime`/`Instant`/`PlainDate`/`PlainTime`などの型。`temporal_rs`やBloomberg/Google/Microsoft/Igaliaなど複数の組織による協力についても紹介されている。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Announcing npmx: a fast, modern browser for the npm registry
[npmx.dev/blog/alpha-release](https://npmx.dev/blog/alpha-release "Announcing npmx: a fast, modern browser for the npm registry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">search</span></p>

npmパッケージ検索サービスnpmx αリリース
パッケージのダウンロード統計、依存関係の古さの警告、ESM/CJSのモジュール形式の検出、インストールサイズの分析などの機能を持つ。


----

## flatt-security/setup-takumi-guard-npm: GitHub Action to configure npm with Takumi Guard registry auth via OIDC
[github.com/flatt-security/setup-takumi-guard-npm](https://github.com/flatt-security/setup-takumi-guard-npm "flatt-security/setup-takumi-guard-npm: GitHub Action to configure npm with Takumi Guard registry auth via OIDC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Actions</span></p>

npmのパッケージインストールをセキュリティプロキシ経由にすることで、悪意あるパッケージをブロックするGitHub Action。
npm/pnpm/yarnに対応し、レジストリを`https://npm.flatt.tech/`に設定することでインストール時にパッケージをチェックする。
GitHub OIDCを使った認証に対応し、Bot IDを設定することで監査ログやダッシュボードでの可視化が利用できる。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## aidenybai/react-grab: Select context for coding agents directly from your website
[github.com/aidenybai/react-grab/tree/main](https://github.com/aidenybai/react-grab/tree/main "aidenybai/react-grab: Select context for coding agents directly from your website")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">AI</span> <span class="jser-tag">library</span></p>

Webサイト上のUI要素をInspectしてReactコンポーネント名やファイルパス、HTMLソースコードなどのコンテキスト情報をコピーできるツール。
コピーした情報をCursorやClaude CodeなどのAIコーディングエージェントに渡して利用できる。
Next.js/Vite/webpackに対応し、プラグインによるカスタマイズやPrimitives APIによる独自UIの構築にも対応している。


----

## dupontcyborg/numpy-ts: Full NumPy, in TypeScript/JavaScript (94% coverage)
[github.com/dupontcyborg/numpy-ts](https://github.com/dupontcyborg/numpy-ts "dupontcyborg/numpy-ts: Full NumPy, in TypeScript/JavaScript (94% coverage)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">math</span></p>

PythonのNumPyをTypeScript/JavaScriptで再実装したライブラリ。
NumPyの507関数のうち476関数をカバーしている。dtype指定、ブロードキャスト、線形代数演算、NumPyスタイルのスライス記法などをサポートする。
Tree-shakeableなモジュール構成で、Node.jsとブラウザの両方で動作する。


----

## pbakaus/impeccable: The design language that makes your AI harness better at design.
[github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable "pbakaus/impeccable: The design language that makes your AI harness better at design.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">AI</span> <span class="jser-tag">Design</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

AIコーディングエージェント向けのフロントエンドデザインのスキルとコマンドのセット。
タイポグラフィ、色彩、空間設計、モーション、インタラクション、レスポンシブデザイン、UXライティングなどのスキルを定義している。
AIが生成するUI/UXデザインにおけるアンチパターンのガイダンスも含まれている。
Claude Code、Cursor、Gemini CLIなどのAIツールに対応している。


----
