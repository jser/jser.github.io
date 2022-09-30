---
title: "2022-09-29のJS: TypeScript 4.9 Beta、workerd(Cloudflare Workers runtime)、Web Almanac 2022"
author: "azu"
layout: post
date : 2022-09-29T03:01:10.645Z
category: JSer
tags:
- node.js
- TypeScript
- security
- book
- browser

---

JSer.info #611 - TypeScript 4.9 betaがリリースされました。

- [Announcing TypeScript 4.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/)

型キャストはせずに型の一致をチェックできる`satisfies`演算子の追加、`in`演算子での型の絞り込みの改善、`== NaN`をコンパイルエラーに変更などが行われています。

`satisfies`演算子については次の記事が詳しいです。

- [Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium](https://medium.com/@cefn/typescript-satisfies-6ba52e74cb2f)

また、`--watch`でのファイル監視のデフォルトを`useFsEvents`に変更、`exports`フィールドの`typeVersions`の優先度を修正なども含まれています。

----

Cloudflare Workersのruntimeであるworkerdがオープンソースとして公開されました。

- [Introducing workerd: the Open Source Workers runtime](https://blog.cloudflare.com/workerd-open-source-workers-runtime/)
- [cloudflare/workerd](https://github.com/cloudflare/workerd)

これに合わせて、Miniflare 3.0.0がαリリースされ、JSを使って実装していた部分もworkerdを使うものになっています。

- [Release v3.0.0-next.1 · cloudflare/miniflare](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0-next.1)

これによってローカルでの開発時と本番の動作が異なるケースが少なくなっていきそうです。

----

HTTP Archiveのデータを元にしたウェブのステータスをまとめたレポートであるWeb Almanacの2022年版が公開されました。

- [The 2022 Web Almanac](https://almanac.httparchive.org/en/2022/)

HTML/CSS/JSなどやアクセシビリティ/セキュリティ/サードパーティなど幅広いデータについて書かれています。

2021年版は日本語にも翻訳されており、電子書籍として読むこともできます。

- [2021 Web Almanac](https://almanac.httparchive.org/ja/2021/)
- <https://cdn.httparchive.org/almanac/ebooks/web_almanac_2021_ja.pdf>

----

<h1 class="site-genre">ヘッドライン</h1>

----

## September 22nd 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/september-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/september-2022-security-releases/ "September 22nd 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.jsのセキュリティ修正としてv14.20.1 (LTS)、v16.17.1 (LTS)、v18.9.1 (Current)がリリースされた。
`--inspect`におけるDNS rebinding、HTTP Request Smuggling、WebCryptoのWeak randomnessの問題の修正など


----

## Announcing TypeScript 4.9 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/ "Announcing TypeScript 4.9 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.9 betaリリース。
型キャストはせずに型の一致をチェックできる`satisfies`演算子の追加、`in`演算子での型の絞り込みの改善、`== NaN`をコンパイルエラーに変更など。
`--watch`でのファイル監視のデフォルトを`useFsEvents`に変更、`exports`フィールドの`typeVersions`の優先度を修正など

- [Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium](https://medium.com/@cefn/typescript-satisfies-6ba52e74cb2f "Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium")

----

## Introducing workerd: the Open Source Workers runtime
[blog.cloudflare.com/workerd-open-source-workers-runtime/](https://blog.cloudflare.com/workerd-open-source-workers-runtime/ "Introducing workerd: the Open Source Workers runtime")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">C++</span></p>

Cloudflare WorkersのJavaScript/WebAssembly runtimeであるworkerdが公開された。
MiniflareでJSを使って実装していた部分もworkerdを使うものが公開されている。
workerd自体はSandboxではないが、SSRF防止するためのBindingとFetchの仕組みなども持っている。

- [Release v3.0.0-next.1 · cloudflare/miniflare](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0-next.1 "Release v3.0.0-next.1 · cloudflare/miniflare")
- [cloudflare/workerd](https://github.com/cloudflare/workerd "cloudflare/workerd")

----

## Release Add support for engines.node and Volta · actions/setup-node
[github.com/actions/setup-node/releases/tag/v3.5.0](https://github.com/actions/setup-node/releases/tag/v3.5.0 "Release Add support for engines.node and Volta · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Github</span></p>

GitHub Actionsのsetup-node 3.5.0リリース。
`package.json`の`engines.node`とVoltaで指定したNode.jsのバージョンをサポート


----

## Release Notes for Safari Technology Preview 154 | WebKit
[webkit.org/blog/13207/release-notes-for-safari-technology-preview-154/](https://webkit.org/blog/13207/release-notes-for-safari-technology-preview-154/ "Release Notes for Safari Technology Preview 154 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">serverless</span></p>

Safari Technology Preview 154リリース。
CSS `:dir`の有効化、`InputEvent.isComposing`のサポート、Scroll To Text Fragmentの有効化など


----

## Release v0.5.0 · facebook/lexical
[github.com/facebook/lexical/releases/tag/v0.5.0](https://github.com/facebook/lexical/releases/tag/v0.5.0 "Release v0.5.0 · facebook/lexical")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

lexical v0.5.0リリース。
NotionライクなDraggable Blocksのサポート、LexicalTablePluginの安定化、Shadow Rootの対応など。
一部のAPIには破壊的な変更も含まれている


----
<h1 class="site-genre">アーティクル</h1>

----

## Next.js Layouts RFC in 5 minutes – Vercel
[vercel.com/blog/next-js-layouts-rfc-in-5-minutes](https://vercel.com/blog/next-js-layouts-rfc-in-5-minutes "Next.js Layouts RFC in 5 minutes – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.jsのLayouts RFCについての解説記事


----

## The Anatomy of an Isolate Cloud
[deno.com/blog/anatomy-isolate-cloud](https://deno.com/blog/anatomy-isolate-cloud "The Anatomy of an Isolate Cloud")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

Deno DeployのIsolationのアプローチについて。
V8のプロセスが独立していて、Runnerがリクエストに対して起動中のプロセス or プロセスを起動して実行する。
基本的にはV8 Sandboxに依存していて、fsやnetの制限を設けている


----

## Introducing Ezno
[kaleidawave.github.io/posts/introducing-ezno/](https://kaleidawave.github.io/posts/introducing-ezno/ "Introducing Ezno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Rustで実装しているTypeScript互換の型チェッカーとコンパイラであるEnzoについて。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Zod Tutorial | Total TypeScript
[www.totaltypescript.com/tutorials/zod](https://www.totaltypescript.com/tutorials/zod "Zod Tutorial | Total TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">video</span></p>

TypeScriptを使ったスキーマバリデーションライブラリのzodのチュートリアル動画。
それぞれ練習問題を見ながら進めていくないようになっている


----

## SPAセキュリティ超入門 | ドクセル
[www.docswell.com/s/ockeghem/K2PPNK-phpconf2022](https://www.docswell.com/s/ockeghem/K2PPNK-phpconf2022 "SPAセキュリティ超入門 | ドクセル")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">XSS</span> <span class="jser-tag">SQL</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

SPAにおいてよく起きるセキュリティの問題についてのスライド。
クライアントサイドでのみバリデーションしている場合の認可制御不備、任意のHTMLを描画してしまうことによるXSS、CSRFについてなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## gioboa/vite-module-federation: Module Federation with Vite now is possible
[github.com/gioboa/vite-module-federation](https://github.com/gioboa/vite-module-federation "gioboa/vite-module-federation: Module Federation with Vite now is possible")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">plugin</span></p>

Module FederationをするVite Plugin


----

## Japa - A simple yet powerful testing framework for Node.js
[japa.dev/docs](https://japa.dev/docs "Japa - A simple yet powerful testing framework for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Node.js向けのテストフレームワーク。
`node`コマンドでテストが実行できる。
基本的なテスト機能に加え、パラメタライズドテスト、テストへのタグ付けとフィルタリングなどをもつ。
またプラグインの仕組みをサポートしており、失敗したテストのみを再実行やTypeScriptの型チェックのテストなどをプラグインでサポートしている。


----
<h1 class="site-genre">書籍関係</h1>

----

## The 2022 Web Almanac
[almanac.httparchive.org/en/2022/](https://almanac.httparchive.org/en/2022/ "The 2022 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">book</span> <span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span></p>

Web Almanacの2022年版が公開された。
HTTP Archiveのデータを元にしたウェブのステータスをまとめたレポート。
HTML/CSS/JSなどやアクセシビリティ/セキュリティ/サードパーティなど幅広いデータを扱ってる


----

## Shell scripting with Node.js
[exploringjs.com/nodejs-shell-scripting/](https://exploringjs.com/nodejs-shell-scripting/ "Shell scripting with Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">book</span> <span class="jser-tag">ShellScript</span></p>

Node.jsでshell scriptingを扱う書籍


----
