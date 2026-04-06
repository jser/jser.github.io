---
title: "2026-04-06のJS: TypeScript 6.0、ES2026 RC、axiosサプライチェーン攻撃"
author: "azu"
layout: post
date: 2026-04-06T01:09:01.312Z
category: JSer
tags:
- TypeScript
- nodejs
- security
- Tools
- React

---

JSer.info #768 - TypeScript 6.0がリリースされました。

- [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

現在のJavaScriptコードベースによる最後のリリースで、Goで書き直されたTypeScript 7.0への移行を準備するリリースとなっています。`strict`がデフォルトで`true`に、`target`のデフォルトが`es2025`に、`module`のデフォルトが`esnext`に変更されています。`target: es5`や`--moduleResolution node`(node10)、`--outFile`などが非推奨となりエラーに変更されました。新しい機能として、`es2025`ターゲットの追加、Temporal APIの型定義、Map/WeakMapの`getOrInsert()`/`getOrInsertComputed()`メソッドの追加、TypeScript 7.0の型順序に合わせる`--stableTypeOrdering`フラグの追加などが含まれています。

---

ECMAScript 2026のRelease Candidateが公開されました。

- [Release ES2026 Candidate March 31st 2026 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31)

TC39によって2026年3月に承認され、2026年6月のEcma General Assemblyでの承認を経て正式リリースとなる予定です。ES2026には、`Array.fromAsync`、JSON.parse source text access、Iterator Sequencing、`Uint8Array`のBase64変換、`Math.sumPrecise`、`Error.isError`、Upsert(`Map.prototype.getOrInsert`)などが含まれる予定です。

---

axiosのnpmパッケージに対するサプライチェーン攻撃が発生しました。

- [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)
- [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)
- [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

ソーシャルエンジニアリングによりメンテナーアカウントが乗っ取られ、悪意のある`axios@1.14.1`と`axios@0.30.4`が公開されました。これらのバージョンには`plain-crypto-js`というマルウェアが依存関係として追加されており、postinstallフックを通じてmacOS/Windows/Linux向けのRemote Access Trojan(RAT)をインストールする仕組みになっていました。影響を受けたかどうかの確認方法は次のページにまとめられています。

- [Am I affected? - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 6.0 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-6-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/ "Announcing TypeScript 6.0 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 6.0リリース。
現在のJavaScriptコードベースによる最後のリリースで、Goで書き直されたTypeScript 7.0への移行を準備するリリースとなる。
`strict`がデフォルトで`true`に、`target`のデフォルトが`es2025`に、`module`のデフォルトが`esnext`に変更。
`target: es5`、`--moduleResolution node`(node10)、`--outFile`、`--esModuleInterop false`などが非推奨となりエラーに変更。
`es2025`ターゲットの追加、Temporal APIの型定義の追加、Map/WeakMapの`getOrInsert()`/`getOrInsertComputed()`メソッドの追加。
Node.jsのSubpath Importsの`#/`のサポート、`--moduleResolution bundler`と`--module commonjs`の組み合わせをサポート。
TypeScript 7.0の型順序に合わせる`--stableTypeOrdering`フラグの追加など


----

## WebKit Features for Safari 26.4 | WebKit
[webkit.org/blog/17862/webkit-features-for-safari-26-4/](https://webkit.org/blog/17862/webkit-features-for-safari-26-4/ "WebKit Features for Safari 26.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">CSS</span> <span class="jser-tag">WebTransport</span> <span class="jser-tag">WebAuthentication</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 26.4リリース。
CSS Grid Lanesによるmasonry/ウォーターフォールスタイルのレイアウトのサポート、名前のみの`@container`クエリのサポート。
`font-size: math`と`math-depth`プロパティのサポート。
CSS Zoomの修正、Scroll-driven Animationsのパフォーマンス改善。
WebTransportのサポート、Keyboard Lock APIのサポート、ReadableByteStreamのサポート。
Scoped Custom Element Registriesの改善、`Iterator.concat()`のサポート。
`<img>`の`sizes`属性でのmath関数(`min()`/`max()`/`clamp()`)のサポート、SVGの`lighter`合成演算子のサポート。
WebAuthnのPRF拡張のサポートなど。


----

## Release v20.0.0 · raineorshine/npm-check-updates
[github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0 "Release v20.0.0 · raineorshine/npm-check-updates")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

npm-check-updates v20.0.0リリース。
npm/yarn/pnpmの設定にあるminimum release ageの設定を自動的に読み取り、cooldownオプションとして適用するようになった。


----

## Release ES2026 Candidate March 31st 2026 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31](https://github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31 "Release ES2026 Candidate March 31st 2026 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2026のRelease Candidateが公開された。
TC39によって2026年3月に承認され、2026年6月のEcma GAでの承認を経て正式リリースとなる予定。


----

## Release v15.0.0 · sindresorhus/got
[github.com/sindresorhus/got/releases/tag/v15.0.0](https://github.com/sindresorhus/got/releases/tag/v15.0.0 "Release v15.0.0 · sindresorhus/got")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Got v15.0.0リリース。
Node.js 22未満のサポートを削除、
`promise.cancel()`を削除しAbortControllerの`signal`オプションに移行、`isStream`オプションの削除。
`responseType: 'buffer'`が`Buffer`の代わりに`Uint8Array`を返すように変更。
ネイティブのFormData APIを利用するように変更、`strictContentLength`のデフォルトを`true`に変更。
RFC 9110に準拠し300/304レスポンスの自動リダイレクトを廃止など


----

## Release 4.18.0 · lodash/lodash
[github.com/lodash/lodash/releases/tag/4.18.0](https://github.com/lodash/lodash/releases/tag/4.18.0 "Release 4.18.0 · lodash/lodash")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">lodash</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

lodash 4.18.0リリース。
`_.unset`と`_.omit`のPrototype Pollutionの脆弱性を修正、`_.template`のコードインジェクションの修正。
`lodash.unset`や`lodash.template`などの個別パッケージが古いままだったのを修正して再公開。


----

## Node.js — Node.js 25.9.0 (Current)
[nodejs.org/en/blog/release/v25.9.0](https://nodejs.org/en/blog/release/v25.9.0 "Node.js — Node.js 25.9.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v25.9.0リリース。
テストランナーのモックモジュールAPIで`defaultExport`と`namedExports`オプションを`exports`オプションに統合。
`--max-heap-size`フラグの追加、Web CryptoでTurboSHAKEとKangarooTwelveアルゴリズムのサポート。
SEA(Single Executable Applications)でESMエントリポイントのコードキャッシュをサポート、実験的な`stream/iter`モジュールの追加。
`AsyncLocalStorage`に`using`スコープの追加、REPLでのカスタムエラーハンドリングのサポートなど。


----

## Release v5.0.0 · lerna-lite/lerna-lite
[github.com/lerna-lite/lerna-lite/releases/tag/v5.0.0](https://github.com/lerna-lite/lerna-lite/releases/tag/v5.0.0 "Release v5.0.0 · lerna-lite/lerna-lite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

lerna-lite v5.0.0リリース。
Node.js 20のサポート終了、Conventional Changelogのレガシー設定ファイル読み込みの削除、`--remove-package-fields`オプションの削除。
内部依存を自前の実装に置き換えることでインストールサイズを削減など


----
<h1 class="site-genre">アーティクル</h1>

----

## Storybook MCP for React
[storybook.js.org/blog/storybook-mcp-for-react/](https://storybook.js.org/blog/storybook-mcp-for-react/ "Storybook MCP for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">MCP</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Storybook MCPサーバについて。
AIエージェントに既存のUIコンポーネントのメタデータ(ストーリー、API、ドキュメント)を提供するMCPサーバ。
複数のStorybookを組み合わせて使うCompositionにも対応している。
MCP Appsに対応して、チャットのレスポンスに直接Storyを埋め込めるようになっている。


----

## Node.js — Security Bug Bounty Program Paused Due to Loss of Funding
[nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties](https://nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties "Node.js — Security Bug Bounty Program Paused Due to Loss of Funding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Node.jsのセキュリティバグバウンティプログラムの一時停止について。
2016年からHackerOneのInternet Bug Bounty(IBB)プログラムを通じて運用されていたが、IBBプログラムの終了により資金が枯渇したため一時停止となった。
資金の80%を発見、20%を修正へ割り当てているが、AIなどによる発見の拡大によりバランスが変わった。
脆弱性の報告自体はHackerOneを通じて引き続き受け付けるが、報告者への金銭的な報酬はなくなる。専用の資金が確保できた場合にプログラムの再開を検討する予定


----

## Signals, the push-pull based algorithm — Willy Brauner
[willybrauner.com/journal/signal-the-push-pull-based-algorithm](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm "Signals, the push-pull based algorithm — Willy Brauner")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Signalにおけるpush-pullベースのリアクティブアルゴリズムについての解説記事。
Signalの基本的な仕組みとして、値の変更時にサブスクライバーへ通知するPush型と、計算値を実際にアクセスされるまで遅延評価するPull型の組み合わせについて解説している。


----

## Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA | The IntelliJ IDEA Blog
[blog.jetbrains.com/idea/2026/03/js-ts-free-support/](https://blog.jetbrains.com/idea/2026/03/js-ts-free-support/ "Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA | The IntelliJ IDEA Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JetBrains</span> <span class="jser-tag">IDE</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

IntelliJ IDEA v2026.1で、JavaScript/TypeScript/HTML/CSSのコア機能が無料で利用可能に。
これまでUltimate版のみで提供されていたWeb開発向けの機能が、Community Editionでも利用できるようになった。
JS/TSのコード補完やリファクタリング、ESLint/Prettierの統合、Viteでのプロジェクト作成、npmスクリプトの実行、依存関係の脆弱性検出などが含まれる。


----

## axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity
[www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan "axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

axiosのnpmパッケージに対するサプライチェーン攻撃について。
ソーシャルエンジニアリングによりメンテナーアカウントが乗っ取られ、悪意のある`axios@1.14.1`と`axios@0.30.4`が公開された。
これらのバージョンには`plain-crypto-js`というマルウェアが依存関係として追加されている。
postinstallフックを通じてmacOS/Windows/Linux向けのRemote Access Trojan(RAT)をインストールする仕組みになっていた。

- [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers "Attackers Are Hunting High-Impact Node.js Maintainers in a C...")
- [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise "The Hidden Blast Radius of the Axios Compromise - Socket")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Introducing EmDash — the spiritual successor to WordPress that solves plugin security
[blog.cloudflare.com/emdash-wordpress/](https://blog.cloudflare.com/emdash-wordpress/ "Introducing EmDash — the spiritual successor to WordPress that solves plugin security")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">CMS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">astro</span> <span class="jser-tag">security</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">wordpress</span></p>

CloudflareによるサーバーレスCMS。
TypeScriptで書かれ、Astro 6.0をベースにしたオープンソース(MITライセンス)のCMS。
プラグインを独立したサンドボックス環境(Dynamic Workers)で実行し、プラグイン起因のセキュリティ問題を解決するアーキテクチャを採用している。
MCPやCLIによるAIエージェント連携、x402プロトコルによる決済統合などの機能も備えている。


----

## vercel-labs/emulate: Local API emulation for CI and no-network sandboxes
[github.com/vercel-labs/emulate](https://github.com/vercel-labs/emulate "vercel-labs/emulate: Local API emulation for CI and no-network sandboxes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vercel</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">CI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">server</span></p>

Vercel/GitHub/Google/Slack/AWS(S3/SQS)などのAPIをローカルでエミュレートするツール。
外部APIのモックサーバとして利用できる。
各サービスはステートフルにデータを保持し、OAuth 2.0フローやWebhookにも対応している。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ArrowJS — The first UI framework for the agentic era
[arrow-js.com/](https://arrow-js.com/ "ArrowJS — The first UI framework for the agentic era")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">library</span></p>

ビルドステップなしで動作する軽量なUIフレームワーク。`reactive`、`html`、`component`の3つの関数で構成される。
AI向けにWebAssemblyサンドボックス内でコンポーネントロジックを分離して実行する機能を持つ。


----
<h1 class="site-genre">書籍関係</h1>

----

## React本格入門 | 技術評論社
[gihyo.jp/book/2026/978-4-297-15523-0](https://gihyo.jp/book/2026/978-4-297-15523-0 "React本格入門 | 技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2026年4月15日発売。
React 19をベースにした入門書。


----
