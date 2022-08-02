---
title: "2022-08-02のJS: Privacy Sandboxのロードマップ更新、Docusaurus 2.0、Electron v20.0.0"
author: "azu"
layout: post
date : 2022-08-02T00:23:15.529Z
category: JSer
tags:
- Tools
- CSS
- serverless
- TypeScript
- Vue

---

JSer.info #603 - Google Chromeでのサードパーティクッキー廃止に代わるAPIとしてPrivacy Sandboxという一連のAPIが提案されています。
元々は2023年半ばからサードパーティクッキー廃止を段階的に進める予定でしたが、今回このロードマップが更新されています。

- [Expanding testing for the Privacy Sandbox for the Web](https://blog.google/products/chrome/update-testing-privacy-sandbox-web/)

Privacy Sandbox APIのリリースは2023年Q3まで延期され、サードパーティクッキーの段階的な廃止は2024年後半まで延期されています。
詳しいロードマップは次のサイトで公開されています。

- [How We’re Protecting Your Online Privacy - The Privacy Sandbox](https://privacysandbox.com/intl/en_us/open-web/)

---

静的サイトジェネレータのDocusaurus v2リリースされました。

- [Announcing Docusaurus 2.0 | Docusaurus](https://docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0)

MDXのサポート、サイドバーの自動生成、プラグインシステム刷新、テーマの再構築などの変更が行われています。

Docusaurus 1から2がリリースされるまで4年ほど経っていますが、今後のメジャーアップデートは数ヶ月単位でより頻繁にアップデートしていく方針のようです。

---

Electron v20.0.0リリースされました。

- [Release electron v20.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v20.0.0)

Chromium 104、[Node v16.15.0](https://nodejs.org/en/blog/release/v16.15.0/)、V8 v10.4へと依存がアップデートされています。
また、`nodeIntegration: true`と`sandbox: false`の組み合わせを設定しない限り、RenderersがデフォルトでSandbox化されるように変更されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v9.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v9.0.0](https://github.com/vueuse/vueuse/releases/tag/v9.0.0 "Release v9.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v9.0.0リリース。
`isSupported`を`Ref<boolean>`に変更、型名を`Use` prefixに統一。
多くのUse関数の引数に関数を渡せるように、`@vueuse/math`パッケージの追加など


----

## Node v18.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v18.7.0/](https://nodejs.org/en/blog/release/v18.7.0/ "Node v18.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">serverless</span></p>

Node.js 18.7.0リリース。
`process.exit(code)`の`code`に数値以外を渡すケースをDeprecatedに変更、`CustomEvent`の実装、http serverに`dropRequest`イベントを実装など


----

## Release v1.2.0 · video-dev/hls.js
[github.com/video-dev/hls.js/releases/tag/v1.2.0](https://github.com/video-dev/hls.js/releases/tag/v1.2.0 "Release v1.2.0 · video-dev/hls.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hls.js v1.2.0リリース。
IE 11のサポート終了、CMAF CCのサポート、バグ修正や安定性の向上など


----

## Expanding testing for the Privacy Sandbox for the Web
[blog.google/products/chrome/update-testing-privacy-sandbox-web/](https://blog.google/products/chrome/update-testing-privacy-sandbox-web/ "Expanding testing for the Privacy Sandbox for the Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">news</span></p>

Privacy Sandboxのロードマップの更新について。
Privacy Sandbox APIのリリースは2023年Q3まで延期され、サードパーティクッキーの段階的な廃止は2024年後半まで延期された。


----

## losfair/blueboat: All-in-one, multi-tenant serverless JavaScript runtime.
[github.com/losfair/blueboat](https://github.com/losfair/blueboat "losfair/blueboat: All-in-one, multi-tenant serverless JavaScript runtime.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">serverless</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">Tools</span></p>

Cloudflare WorkersのようなV8 Isolatesでマルチテナント実行できるJavaScript実行環境。
エンジンはRustで書かれていて、実行するJSスクリプトはFetch APIやRequest/Responseのようなウェブ標準互換のAPIが一部利用できる。


----

## Announcing Docusaurus 2.0 | Docusaurus
[docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0](https://docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0 "Announcing Docusaurus 2.0 | Docusaurus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">ReleaseNote</span></p>

静的サイトジェネレータのDocusaurus v2リリース。
MDXのサポート、サイドバーの自動生成、プラグインシステム刷新、テーマの再構築など


----

## Release electron v20.0.0 · electron/electron
[github.com/electron/electron/releases/tag/v20.0.0](https://github.com/electron/electron/releases/tag/v20.0.0 "Release electron v20.0.0 · electron/electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron v20.0.0リリース。
`nodeIntegration: true`と`sandbox: false`の組み合わせを設定しない限り、RenderersがデフォルトSandbox化されるように変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## 新しいビューポートの単位（sv\*、lv\*、dv\*） | フロントエンドBlog | ミツエーリンクス
[www.mitsue.co.jp/knowledge/blog/frontend/202207/28\_0755.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202207/28_0755.html "新しいビューポートの単位（sv\*、lv\*、dv\*） | フロントエンドBlog | ミツエーリンクス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSのview portのunitについての記事


----

## Help pick a syntax for CSS nesting - Chrome Developers
[developer.chrome.com/blog/help-css-nesting/](https://developer.chrome.com/blog/help-css-nesting/ "Help pick a syntax for CSS nesting - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">アンケート</span></p>

CSSのネスト構文についてのアンケート。
SCSS/Less/Stylusのようにネストをするケース、`@nest`を使うケース、ブラケットを使うケースについての意見を募集している


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 🌕 moonでのmonorepo管理とpackemonでのCJS/ESMのdual package
[azu.github.io/slide/2022/moa/moon-packemon.html](https://azu.github.io/slide/2022/moa/moon-packemon.html "🌕 moonでのmonorepo管理とpackemonでのCJS/ESMのdual package")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">slide</span> <span class="jser-tag">JavaScript</span></p>

monorepo管理ツールのmoonとCJS/MJS対応のライブラリビルドツールのpackemonについてのスライド


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ronami/HypeScript: 🐬 A simplified implementation of TypeScript&#039;s type system written in TypeScript&#039;s own type system
[github.com/ronami/HypeScript](https://github.com/ronami/HypeScript "ronami/HypeScript: 🐬 A simplified implementation of TypeScript&#039;s type system written in TypeScript&#039;s own type system")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TypeScriptの型システムをTypeScriptの型で実装したもの。


----

## ehmicky/safe-json-value: ⛑️ JSON serialization should never fail
[github.com/ehmicky/safe-json-value](https://github.com/ehmicky/safe-json-value "ehmicky/safe-json-value: ⛑️ JSON serialization should never fail")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">JSON</span></p>

例外を投げないJSONのシリアライズを提供するライブラリ。
シリアライズできないときは`error`プロパティにエラーを入れ、例外となる値は結果から除外するなどしている。


----

## Skeleton
[skeleton.brainandbonesllc.com/](https://skeleton.brainandbonesllc.com/ "Skeleton")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

SvelteとTailwindを使ったUIコンポーネントライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## TypeScriptとReact/Next.jsでつくる 実践Webアプリケーション開発：書籍案内｜技術評論社
[gihyo.jp/book/2022/978-4-297-12916-3](https://gihyo.jp/book/2022/978-4-297-12916-3 "TypeScriptとReact/Next.jsでつくる 実践Webアプリケーション開発：書籍案内｜技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2022年7月22日 発売。
Next.jsの入門本


----
