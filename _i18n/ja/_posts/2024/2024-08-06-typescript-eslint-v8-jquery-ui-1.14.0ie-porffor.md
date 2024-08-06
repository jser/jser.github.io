---
title: "2024-08-06のJS: typescript-eslint v8、jQuery UI 1.14.0(IEサポートの終了)、Porffor"
author: "azu"
layout: post
date: 2024-08-06T00:28:21.073Z
category: JSer
tags:
- TypeScript
- browser
- ESLint
- React
- Extension

---

JSer.info #702 - typescript-eslint v8がリリースされました。

- [Announcing typescript-eslint v8 | typescript-eslint](https://typescript-eslint.io/blog/announcing-typescript-eslint-v8/)

ESLint 9のサポート、`projectService`をStableに変更、プリセットのルール変更などが行われています。

---

jQuery UI 1.14.0がリリースされました。

- [jQuery UI 1.14.0 released | jQuery UI Blog](https://blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/)

jQuery UIはすでに[メンテナンスモード](https://blog.jqueryui.com/2021/10/jquery-maintainers-update-and-transition-jquery-ui-as-part-of-overall-modernization-efforts/)となっていますが、このリリースでは今後のメンテナンスのしやすさに向けた変更が行われています。

- [Plans for jQuery UI 1.14, dropping support for UI <1.12 in the Download Builder | jQuery UI Blog](https://blog.jqueryui.com/2024/04/plans-for-jquery-ui-1-14-dropping-support-for-ui-1-12-in-the-download-builder/)

jQuery UI 1.14.0では、IEのサポートが削除され、Chrome/Firefox/Safari/Edgeの最新バージョンのみがサポートされるようになりました。
また、`jQuery.uiBackCompat`というjQuery UI 1.13との互換性を保つためのオプションが追加され、デフォルトは`false`となっています。

また、jQuery UI 1.14.0へのアップグレードガイドも公開されています。

- [jQuery UI 1.14 Upgrade Guide | jQuery UI](https://jqueryui.com/upgrade-guide/1.14/)

---

[Porffor](https://porffor.dev/)は、JavaScript/TypeScriptのコードをWebAssemblyにコンパイルするためのJavaScriptエンジン/コンパイラー/ランタイムです。
porffor自体もJavaScriptで書かれており、AOT(Ahead-Of-Time)でJS/TSをWebAssemblyにコンパイルしています。
これによって、[Javy](https://github.com/bytecodealliance/javy)のように既存のJavaScriptエンジン([QuickJS](https://bellard.org/quickjs/))をWasmに組み込んで実行するよりも、ファイルサイズやメモリ使用量を削減することを目標にしています。

- [CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS](https://github.com/CanadaHonk/porffor)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing typescript-eslint v8 | typescript-eslint
[typescript-eslint.io/blog/announcing-typescript-eslint-v8/](https://typescript-eslint.io/blog/announcing-typescript-eslint-v8/ "Announcing typescript-eslint v8 | typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint v8リリース。
ESLint 9のサポート、`projectService`をStableに変更、プリセットのルール変更など

----

## jQuery UI 1.14.0 released | jQuery UI Blog
[blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/](https://blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/ "jQuery UI 1.14.0 released | jQuery UI Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.14.0リリース。
IEのサポート終了、1.11のAPIとの互換性を有効にする`jQuery.uiBackCompat`オプションの追加など


----

## Release 3.38.0 - 2024.08.05 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.38.0](https://github.com/zloirock/core-js/releases/tag/v3.38.0 "Release 3.38.0 - 2024.08.05 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">polyfill</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.38.0リリース。
`RegExp.escape`/`Promise.try`/Uint8Array to/from base64 and hexをそれぞれのStage 3に移動。
Node.js 22.3.0で追加された`process.getBuiltinModule`を利用するように


----

## ECMAScript proposal updates @ 2024-07 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/08/06/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/08/06/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-07 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2024年7月のTC39ミーティングでのECMAScript Proposalのステータス変更まとめ。
`RegExp.escape`がStage 3となった


----
<h1 class="site-genre">アーティクル</h1>

----

## tsconfig.json の include オプションには何を指定すべきか - mizdra&#039;s blog
[www.mizdra.net/entry/2024/07/27/193815](https://www.mizdra.net/entry/2024/07/27/193815 "tsconfig.json の include オプションには何を指定すべきか - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

tsconfig.jsonの`includes`オプションについて


----

## 【2024年夏】ブラウザ拡張機能開発を加速するフレームワーク・ツール3選をコードベース付きで紹介！
[zenn.dev/cybozu\_frontend/articles/introduction-browser-extensions-tools](https://zenn.dev/cybozu_frontend/articles/introduction-browser-extensions-tools "【2024年夏】ブラウザ拡張機能開発を加速するフレームワーク・ツール3選をコードベース付きで紹介！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span> <span class="jser-tag">library</span></p>

ブラウザ拡張を開発するツールであるWXT/Plasmo/Extension.jsについて


----

## Patterns for Memory Efficient DOM Manipulation with Modern Vanilla JavaScript – Frontend Masters Boost
[frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/](https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/ "Patterns for Memory Efficient DOM Manipulation with Modern Vanilla JavaScript – Frontend Masters Boost")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

DOM APIでのDOMの変更を効率的に行う方法について。
`textContent`と`innerText`、`insertAdjacentHTML`と`innerHTML`、DOM Nodeの削除とGC、イベントリスナーのクリーンアップなどについて


----

## Migrate to ESLint 9.x • ~/Z
[tduyng.com/blog/migrating-to-eslint9x/](https://tduyng.com/blog/migrating-to-eslint9x/ "Migrate to ESLint 9.x • ~/Z")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint 9のFlat Configへの移行方法について。


----

## How Airbnb Smoothly Upgrades React | by Andre Wiggins | The Airbnb Tech Blog | Jul, 2024 | Medium
[medium.com/airbnb-engineering/how-airbnb-smoothly-upgrades-react-b1d772a565fd](https://medium.com/airbnb-engineering/how-airbnb-smoothly-upgrades-react-b1d772a565fd "How Airbnb Smoothly Upgrades React | by Andre Wiggins | The Airbnb Tech Blog | Jul, 2024 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

AirbnbでのReactのアップデートについて。
パッケージのalias機能を使い複数のReactバージョンを利用、SSRを行うサーバもあるため環境変数で使うバージョンを指定。
同じコードから2つのReactバージョンで動くようにして、テストしながら段階的に移行していったという話。


----

## How Google handles JavaScript throughout the indexing process – Vercel
[vercel.com/blog/how-google-handles-javascript-throughout-the-indexing-process](https://vercel.com/blog/how-google-handles-javascript-throughout-the-indexing-process "How Google handles JavaScript throughout the indexing process – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Google BotsによるインデックスとJavaScript/CSSのレンダリングの影響についての調査


----

## フロントエンド開発に役立つ Datadog 活用法 - LegalOn Technologies Engineering Blog
[tech.legalforce.co.jp/entry/2024/08/05/154617](https://tech.legalforce.co.jp/entry/2024/08/05/154617 "フロントエンド開発に役立つ Datadog 活用法 - LegalOn Technologies Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Datadog</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

Datadog RUMを使ったフロントエンドのモニタリングについて。
ユーザーアクションのトラッキングの設定や可視化について

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Porffor
[porffor.dev/](https://porffor.dev/ "Porffor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">Tools</span></p>

WasmにコンパイルできるJavaScriptエンジン/コンパイラー/ランタイム。
JavaScript/TypeScriptのコードをAOTコンパイルしてWasmにできるため、Wasmのファイルサイズが小さく効率的に動かせる。
Wasm to Cへのコンパイラなども実装している

- [CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS](https://github.com/CanadaHonk/porffor "CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS")


----
<h1 class="site-genre">スライド、動画関係</h1>


----

## React Conf 2024 Talks
[conf.react.dev/talks](https://conf.react.dev/talks "React Conf 2024 Talks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Conf 2024の動画まとめ


----
