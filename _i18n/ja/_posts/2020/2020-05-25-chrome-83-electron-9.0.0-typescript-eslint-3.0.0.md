---
title: "2020-05-25のJS: Chrome 83、Electron 9.0.0、typescript-eslint 3.0.0"
author: "azu"
layout: post
date : 2020-05-25T14:18:36.448Z
category: JSer
tags:
- Chrome
- Electron
- TypeScript
- ESLint

---

JSer.info #489 - Chrome 83がリリースされました。

- [New in Chrome 83  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/05/nic83)
- [What's New In DevTools (Chrome 83)  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/03/devtools)
- [Deprecations and removals in Chrome 83  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/04/chrome-83-deps-rems)
- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D83)
- [V8 release v8.3 · V8](https://v8.dev/blog/v8-release-83)

Trusted Typesのサポート、フォームコントロールUIのアップデート、COOP(Cross-Origin-Opener-Policy)とCOEP(Cross-Origin-Embedder-Policy)が実装されています。
COOPとCOEPはSite Isolationと深い関係がある仕組みなので、詳細は次の記事を参照してください。

- [Making your website "cross-origin isolated" using COOP and COEP](https://web.dev/coop-coep/)
- [Site Isolation 及び Web のセキュリティモデルの更新 | blog.jxck.io](https://blog.jxck.io/entries/2020-05-22/site-isolation.html)

また、Origin Trialとして`performance.measureMemory()`や`Scheduler.postTask()`が追加されています。
その他にはBarcode Detection APIやCSS ` prefers-color-scheme`のサポートなどが行われています。

---

Electron 9.0.0がリリースされました。

- [Electron 9.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-9-0#highlight-features)

9.0.0ではChromium 83、Node 12.14、V8 8.3へアップデートが行われています。

`enableRemoteModle`オプションを使わずに`remote`モジュールを使うことを非推奨化されています。
これは、`remote`モジュールをコアから外していく作業の一環です。

- [Deprecate the 'remote' module and move it to userland · Issue #21408 · electron/electron](https://github.com/electron/electron/issues/21408)
- [Electron’s ‘remote’ module considered harmful - Jeremy Apthorp - Medium](https://medium.com/@nornagon/electrons-remote-module-considered-harmful-70d69500f31)

その他には、`app.enableRendererProcessReuse`をデフォルトで`true`に変更、スペルチェッカーの改善、PDFビューアの有効化なども行われています。

----

TypeScript向けのESLintプラグインであるtypescript-eslint 3.0.0がリリースされました。

- [Release v3.0.0 · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v3.0.0)

[ESLint 7](https://eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0)をサポート、TypeScript 3.9で挙動が変更されたOptional ChainingとNon-Null Assertionsの変更に追従したサポートが含まれます。

- [TypeScript: Handbook - TypeScript 3.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html#parsing-differences-in-optional-chaining-and-non-null-assertions)

また、同時にNode.js 8とTypeScript 3.2のサポートを終了しています。

その他には、`@typescript-eslint/recommended`と`@typescript-eslint/recommended-requiring-typechecking`が`@typescript-eslint/eslint-recommended`を継承するように変更されています。
またルールのデフォルト値の変更、Deprecatedなルールの削除なども行われています。

具体的なrecommendedルールセットにおける設定値の変更は次のIssueにまとめられています。

- [Changes to the `eslint-recommended` ruleset for 3.0.0 · Issue #1273 · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/issues/1273)
- [Changes to the `recommended` sets for 3.0.0 · Issue #1423 · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/issues/1423)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v14.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.3.0/](https://nodejs.org/en/blog/release/v14.3.0/ "Node v14.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 14.3.0リリース。
REPLでoutput previewの改善、Top-Level Awaitのサポートなど


----

## New in Chrome 83  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/05/nic83](https://developers.google.com/web/updates/2020/05/nic83 "New in Chrome 83  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 83リリース。
Trusted Typesのサポート、フォームコントロールUIのアップデート、COOPとCOEPの実装。
Origin Trialとして`performance.measureMemory()`や`Scheduler.postTask()`の追加。
その他にはBarcode Detection APIやCSS ` prefers-color-scheme`のサポートなど

- [Chromium Blog: Chrome 83 Beta: Cross-site Scripting Protection, Improved Form Controls, and Safe Cross-origin Resource Sharing](https://blog.chromium.org/2020/04/chrome-83-beta-cross-site-scripting.html "Chromium Blog: Chrome 83 Beta: Cross-site Scripting Protection, Improved Form Controls, and Safe Cross-origin Resource Sharing")

----

## Release v3.0.0 · typescript-eslint/typescript-eslint
[github.com/typescript-eslint/typescript-eslint/releases/tag/v3.0.0](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v3.0.0 "Release v3.0.0 · typescript-eslint/typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint 3.0.0リリース。
ESLint 7をサポート、TS 3.9のサポート。 
Node.js 8とTypeScript 3.2のサポート終了。
`recommended`と`recommended-requiring-typechecking`が`eslint-recommended`を継承するように変更。
ルールのデフォルト値の変更、Deprecatedなルールの削除など。


----

## Electron 9.0.0 | Electron Blog
[www.electronjs.org/blog/electron-9-0](https://www.electronjs.org/blog/electron-9-0 "Electron 9.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 9.0.0リリース。
Chromium 83、Node 12.14、V8 8.3へアップデート。
`enableRemoteModle`オプションを使わずに`remote`モジュールを使うことを非推奨化、`app.enableRendererProcessReuse`をデフォルトで`true`に変更など。
その他には、スペルチェッカーの改善、PDFビューアの有効化など


----
<h1 class="site-genre">アーティクル</h1>

----

## Preparing for AppCache removal
[web.dev/appcache-removal/](https://web.dev/appcache-removal/ "Preparing for AppCache removal")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

ChromeのAppCache削除プラン。
Chrome 90で完全に消える予定。
Chrome on iOSではService Workerが使えないため、代用方法はない環境もある。他のブラウザでのAppCacheの削除予定についてなど


----

## Chromium Blog: The Science Behind Web Vitals
[blog.chromium.org/2020/05/the-science-behind-web-vitals.html](https://blog.chromium.org/2020/05/the-science-behind-web-vitals.html "Chromium Blog: The Science Behind Web Vitals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

Web Vitalsの背景にあるUX調査について。
LCPの2.5秒未満、CLSの0.1未満、FIDの100ミリ秒未満の推奨値の算出に関する調査についてまとめた記事


----

## Site Isolation 及び Web のセキュリティモデルの更新 | blog.jxck.io
[blog.jxck.io/entries/2020-05-22/site-isolation.html](https://blog.jxck.io/entries/2020-05-22/site-isolation.html "Site Isolation 及び Web のセキュリティモデルの更新 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

異なるサイトのコードの実行やリソースを読み込みを観測することで情報を取得できるサイドチャネル攻撃を防止する仕組みについて。
ブラウザのプロセスを分離する方法とウェブサイト側でオプトインとしてクロスオリジンリクエストを制御する仕組みについて。


----

## Introducing App Service Static Web Apps - Microsoft Tech Community - 1394451
[techcommunity.microsoft.com/t5/azure-app-service/introducing-app-service-static-web-apps/ba-p/1394451](https://techcommunity.microsoft.com/t5/azure-app-service/introducing-app-service-static-web-apps/ba-p/1394451 "Introducing App Service Static Web Apps - Microsoft Tech Community - 1394451")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">Azure</span> <span class="jser-tag">article</span></p>

Azureの静的サイトホスティングサービスのApp Service Static Web Appsについて。
ルーティングルール、GitHubアカウントなどを使った認証、Azure FunctionsでのサーバAPIの実装、GitHub Actionsを使ったデプロイなどができる


----

## module bundlerの作り方(準備編) - 技術探し
[blog.hiroppy.me/entry/create-module-bundler-preparation](https://blog.hiroppy.me/entry/create-module-bundler-preparation "module bundlerの作り方(準備編) - 技術探し")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">bundler</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

BabelのJavaScriptパーサを使って基本的なmodule bundlerを作成するチュートリアル


----

## swyx Writing | IE11 Mainstream End Of Life in Oct 2020
[www.swyx.io/writing/ie11-eol/](https://www.swyx.io/writing/ie11-eol/ "swyx Writing | IE11 Mainstream End Of Life in Oct 2020")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

IE 11の「メインストリーム」でのサポート終了についての意見/記事。
Windows 10のextended supportは2025年までだが、「メインストリーム」のサポートは2020年までのため、IE 11の「メインストリーム」サポートも2020年までではという話。
ChromiumベースのMSEdgeのリリースと、Windows Update経由での自動ロールアウトも2020年中には完了することも加味している。
また、IE 11のシェア、IE 11のサポートを終了しているサービスについてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## What's New in Lighthouse 6.0
[web.dev/lighthouse-whats-new-6.0/](https://web.dev/lighthouse-whats-new-6.0/ "What's New in Lighthouse 6.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 6.0リリース。
Web Vitalsに基づく新しいメトリクスとしてLCP/CLSの追加、Performanceスコア計算の変更。
新しいAuditsとして、Unused JavaScript、axe-coreベースのAccessibility Auditなどの追加。
Lighthouse拡張はPageSpeed Insights APIを使うように変更など

- [Release v6.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v6.0.0 "Release v6.0.0 · GoogleChrome/lighthouse")
- [Lighthouse Scoring calculator](https://googlechrome.github.io/lighthouse/scorecalc/ "Lighthouse Scoring calculator")
- [GoogleChrome/lighthouse-ci: Automate running Lighthouse for every commit, viewing the changes, and preventing regressions](https://github.com/GoogleChrome/lighthouse-ci "GoogleChrome/lighthouse-ci: Automate running Lighthouse for every commit, viewing the changes, and preventing regressions")

----

## WebGL guide (part 1/2)
[xem.github.io/articles/webgl-guide.html](https://xem.github.io/articles/webgl-guide.html "WebGL guide (part 1/2)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">tutorial</span></p>

WebGL/GLSLについてのチュートリアル


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Introduction - Nuxt Content
[content.nuxtjs.org/](https://content.nuxtjs.org/ "Introduction - Nuxt Content")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Nuxt.jsからMarkdown、JSON、CSVなどのコンテンツデータを取得して、埋め込めるNext.jsモジュール。


----

## cacjs/cac: Simple yet powerful framework for building command-line apps.
[github.com/cacjs/cac](https://github.com/cacjs/cac "cacjs/cac: Simple yet powerful framework for building command-line apps.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">console</span> <span class="jser-tag">library</span></p>

コマンドラインツール向けのライブラリ。
引数パーサ、ヘルプ表示、バージョン表示、サブコマンドの仕組みを持っている


----

## loreanvictor/rxxpress: An Experimental Mashup of RxJS and Express
[github.com/loreanvictor/rxxpress/](https://github.com/loreanvictor/rxxpress/ "loreanvictor/rxxpress: An Experimental Mashup of RxJS and Express")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

RxJSを使ったExpressライクなサーバライブラリ。
ExpressのRouterと組み合わせ利用できるように設計されている


----

## umijs/umi-request: A request tool based on fetch.
[github.com/umijs/umi-request](https://github.com/umijs/umi-request "umijs/umi-request: A request tool based on fetch.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Fetch</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Fetch APIベースのHTTPリクエストライブラリ


----
