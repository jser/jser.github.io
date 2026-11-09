---
title: "2026-11-09のJS: TypeScript 7.1 Beta、Node.js 26 LTS/27 Alpha、Safari 27.1"
author: "azu"
layout: post
date: 2026-11-09T00:23:07.548Z
category: JSer
tags:
- TypeScript
- nodejs
- safari
- browser
- css
- WebAPI

---

JSer.info #782 - TypeScript 7.1 Betaがリリースされました。

- [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

Ambient ModulesでのImport Attributes、`import source`/`import.source()`に対応しています。
`--target es2026`/`--lib es2026`が追加され、`Promise.allKeyed`などの型定義も追加されています。
また、`typescript/sync`/`typescript/async`などの新しいAPI、埋め込みコードを扱うContent Mappersが追加されています。

---

Node.js 26.13.0がリリースされ、Node.js 26系がコードネームLithiumとしてLTSに移行しました。

- [Node.js — Node.js 26.13.0 (LTS)](https://nodejs.org/en/blog/release/v26.13.0)

Node.js 26系は2029年4月末までサポートされます。
Node.js 25以降のLinux公式バイナリは`libatomic`にリンクされており、古いLTSからの更新時には別途インストールが必要になる場合があります。

また、Node.js 27 Alphaがリリースされました。

- [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

V8 15.6へアップデートされ、`Math.sumPrecise()`/`Iterator.zip()`などに対応しています。
破壊的変更として、ヒープ上限の既定値が変更されています。
`Buffer`/`ArrayBuffer`のメモリもヒープ上限に算入されます。
`v8.serialize()`の出力形式が変更され、旧バージョンでは読み込めなくなっています。
このほか、`node:vfs`のフラグが不要になり、環境変数へのアクセスを制御する`--allow-env`、実験的な`net/promises` APIが追加されています。

---

Safari 27.1がリリースされました。

- [WebKit Features for Safari 27.1 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

iPhone Duo向けにDevice Posture APIとViewport Segments APIを、機能フラグ付きで試験的にサポートしています。
`device-posture`メディアクエリや`navigator.devicePosture`で折りたたみ状態を取得できます。
また、`window.viewport.segments`やCSS環境変数で画面の分割領域を取得できます。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 7.1 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/ "Announcing TypeScript 7.1 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 7.1 Betaリリース。
Ambient ModulesにおけるImport Attributesをサポート、`import source`/`import.source()`に対応。
`--target es2026`/`--lib es2026`を追加、`Promise.allKeyed`などの型定義を追加。
`typescript/sync`/`typescript/async`などの新しいAPI、埋め込みコードを扱うContent Mappersを追加など


----

## Nuxt 4.6 · Nuxt Blog
[nuxt.com/blog/v4-6](https://nuxt.com/blog/v4-6 "Nuxt 4.6 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v4.6.0リリース。
同梱のNuxt CLI v4で`nuxt init`を削除し、`npm create nuxt@latest`に統一。
サーバー処理の共通APIとなる`nuxt/server`、`runtimeConfig.appSecret`とセッション管理APIを追加。
`experimental.routeTypedFetch`で`$fetch`/`useFetch`の型推論を刷新し、型チェックのパフォーマンスを改善。
Vue Vaporとの相互運用、`createUseFetch`/`createUseAsyncData`の`addons`、実験的な`@nuxt/vite-server`を追加。
`my-bad`による開発時のエラー表示、`nuxt dev`の対話パネル、`nuxt curl`/`nuxt task`コマンドを追加など


----

## Node.js — 2026年10月21日（水）セキュリティリリース
[nodejs.org/en/blog/vulnerability/october-2026-security-releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases "Node.js — 2026年10月21日（水）セキュリティリリース")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 22.23.4/24.22.1/26.12.1のセキュリティリリース。
重要度Highを含む10件の脆弱性を修正。
`dns.resolve`でのNUL文字による名前の切り詰め、TLS証明書のホスト名検証の回避、Brotliデコーダーの領域外書き込みを修正。
`crypto.randomUUID()`と`crypto.randomInt()`の乱数キャッシュがスナップショットに保存される問題を修正。
`fs.realpathSync`によるPermission Modelの回避などを修正。
また、c-ares/Undici/OpenSSL/SQLiteなどの依存関係を更新。


----

## WebKit Features for Safari 27.1 | WebKit
[webkit.org/blog/18486/webkit-features-for-safari-27-1/](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/ "WebKit Features for Safari 27.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">css</span> <span class="jser-tag">WebAPI</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 27.1リリース。
iPhone Duo向けにDevice Posture APIとViewport Segments APIを機能フラグ付きで試験的にサポート。
`device-posture`メディアクエリや`navigator.devicePosture`で折りたたみ状態を取得できる。
`window.viewport.segments`やCSS環境変数で画面の分割領域を取得できる。


----

## Release v10.0.0-beta.0 · TypeStrong/ts-loader
[github.com/TypeStrong/ts-loader/releases/tag/v10.0.0-beta.0](https://github.com/TypeStrong/ts-loader/releases/tag/v10.0.0-beta.0 "Release v10.0.0-beta.0 · TypeStrong/ts-loader")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

ts-loader v10.0.0-beta.0リリース。
TypeScript 7.1以上/Node.js 22以上を必須とし、コンパイル処理を`typescript/sync` APIへ移行。
`compilerOptions`/`context`/`happyPackMode`などのローダーオプションを削除している。


----

## Release vite-plus v1.4.0 · voidzero-dev/vite-plus
[github.com/voidzero-dev/vite-plus/releases/tag/v1.4.0](https://github.com/voidzero-dev/vite-plus/releases/tag/v1.4.0 "Release vite-plus v1.4.0 · voidzero-dev/vite-plus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">CLI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vite+ 1.4.0リリース。
`vpx`でTypeScript/JavaScriptファイルの実行と`--watch`による監視に対応、`vp migrate`でtsxからの移行をサポート。
`vp check --deny-warnings`、レジストリのチームを管理する`vp pm team`を追加。
グローバルCLIの依存関係をリリースごとのロックファイルからインストールするように変更など


----

## Node.js — Node.js 26.13.0 (LTS)
[nodejs.org/en/blog/release/v26.13.0](https://nodejs.org/en/blog/release/v26.13.0 "Node.js — Node.js 26.13.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v26.13.0リリース。
Node.js 26系がコードネームLithiumとしてLTSに移行し、2029年4月末までサポートされる。
Node.js 25以降のLinux公式バイナリは`libatomic`にリンクされており、古いLTSからの更新時には別途インストールを必要とする場合がある。


----

## Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)
[nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0 "Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v27.0.0-alpha.0.0.0リリース。
破壊的変更として、ヒープ上限の既定値を変更し、`Buffer`/`ArrayBuffer`のメモリも上限に算入するように変更。
`v8.serialize()`の出力形式を変更し、旧バージョンでの読み込みに非対応となる。
V8 15.6へアップデートと`Math.sumPrecise()`/`Iterator.zip()`などをサポート。
`node:vfs`のフラグなしに変更、環境変数へのアクセスを制御する`--allow-env`を追加、実験的な`net/promises` APIの追加など


----

## Release v1.0.0 · dy/jz
[github.com/dy/jz/releases/tag/v1.0.0](https://github.com/dy/jz/releases/tag/v1.0.0 "Release v1.0.0 · dy/jz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">compiler</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptをWebAssemblyにコンパイルするJZ v1.0.0リリース。


----

## Release v1.65.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.65.0](https://github.com/microsoft/playwright/releases/tag/v1.65.0 "Release v1.65.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Playwright v1.65.0リリース。
破壊的変更として、TypeScriptのクラスフィールドが`useDefineForClassFields`に従うように変更、クリックなどの操作で`inert`の解除を待つように変更。
Cookieの照合をRFC 6265に合わせ、`APIRequestContext`の`params`を既存のクエリに追記するように変更。
`bunx --bun playwright test`でBun上でのテスト実行に対応、`failures`レポーターと`onlyFailures`オプションを追加。
テストを単独で実行する`lock: '-exclusive-'`、`cdpSession.send()`の`timeout`/`signal`オプションを追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Unload event deprecated in Chrome  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/unload-deprecated-in-chrome](https://developer.chrome.com/blog/unload-deprecated-in-chrome "Unload event deprecated in Chrome  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Chrome 155で`unload`イベントの非推奨化が完了し、デフォルトでは発火しなくなった。
イベントの信頼性やBFCacheへの影響、段階的な適用の経緯について解説している。
Permissions PolicyやChrome Enterpriseの設定によるオプトアウトは引き続き利用できる。


----

## Rebuilding the global town square from scratch
[blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch "Rebuilding the global town square from scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">SSR</span> <span class="jser-tag">performance</span> <span class="jser-tag">AI</span> <span class="jser-tag">article</span></p>

X.comのWebアプリを再構築した背景と移行方法について。
React/Relay/Fastifyなどを使い、利用者/検索クローラー/リンクプレビュー向けに分かれていた3つのサーバーを統合。
Streaming HTML、GraphQLレスポンスの再利用、JavaScriptの分割や読み込み順序の調整によるパフォーマンス改善。
AIコーディングエージェントを使った開発と、既存サーバーを仕様として利用するテスト、国ごとの段階的な移行についても解説している。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Add streaming HTML insertion methods by noamr · Pull Request #12758 · whatwg/html
[github.com/whatwg/html/pull/12758?overview&#x3D;true](https://github.com/whatwg/html/pull/12758?overview=true "Add streaming HTML insertion methods by noamr · Pull Request #12758 · whatwg/html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebAPI</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span></p>

HTMLをストリーミングで解析し、DOMへ段階的に挿入するAPIをHTML仕様に。
`Element.streamHTML()`/`streamAppendHTML()`などが`WritableStream`を返し、Streamへ書き込まれたHTML文字列をHTMLとして挿入する。
危険な要素や属性を除去するメソッドと、除去を既定で行わない`Unsafe`版を用意する。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## vercel-labs/tsc-ts: TypeScript written in TypeScript
[github.com/vercel-labs/tsc-ts](https://github.com/vercel-labs/tsc-ts "vercel-labs/tsc-ts: TypeScript written in TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">compiler</span> <span class="jser-tag">Tools</span></p>

TypeScript-Go（tsgo）をTypeScriptに移植した実験的なコンパイラ。
scriptcを使ってネイティブコードにコンパイルし、npmパッケージとして配布している。
`tsc-ts -p tsconfig.json`でプロジェクトをコンパイルでき、`--api`で標準入出力を使うAPIサーバーとしても動作する。


----

## obsidianmd/pele: Renders Mermaid diagrams faster than you&#039;d run from a volcano! 🌋
[github.com/obsidianmd/pele](https://github.com/obsidianmd/pele "obsidianmd/pele: Renders Mermaid diagrams faster than you&#039;d run from a volcano! 🌋")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">diagram</span> <span class="jser-tag">SVG</span></p>

MermaidのダイアグラムをSVGに変換するライブラリ。依存がなく、CSS変数による色やフォントの変更、図の種類ごとの読み込みや遅延読み込みに対応している。
`mount()`でブラウザの要素に描画し、コンテナの幅に合わせてレイアウトを調整できる。


----
