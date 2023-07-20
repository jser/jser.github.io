---
title: "2023-07-20のJS: vm2の開発終了、Storybook 7.1、Fresh 1.3"
author: "azu"
layout: post
date : 2023-07-20T12:49:40.487Z
category: JSer
tags:
- node.js
- security
- Tools
- ECMAScript
- proposal

---

JSer.info #652 - Node.jsの[node:vm](https://nodejs.org/api/vm.html)モジュールはSandbox(信用できないコードの実行環境)としては[利用できません](https://snyk.io/blog/security-concerns-javascript-sandbox-node-js-vm-module/)が、[vm2](https://github.com/patriksimek/vm2)は`node:vm`をラップしてSandboxを提供するモジュールでした。

今回、`vm2`の仕組み的に修正できないSandboxに関する脆弱性が発見されたため、メンテナンスを終了することが宣言されています。脆弱性の詳細はまだ公開されていませんが、Sandboxを破ることができる脆弱性で、[PoCは8月ごろ](https://github.com/patriksimek/vm2/issues/533#issuecomment-1632482080)に公開される予定です。

- [Discontinued · Issue #533 · patriksimek/vm2](https://github.com/patriksimek/vm2/issues/533)
- [vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database](https://github.com/advisories/GHSA-cchq-frgv-rjh5)

Sandbox機能が欲しい場合は、QuickJSをWebAssemblyにコンパイルした[quickjs-emscripten](https://github.com/justjake/quickjs-emscripten)やV8のIsolateを使った[isolated-vm](https://github.com/laverdet/isolated-vm)への移行を推奨しています。
[proxy-agents](https://github.com/TooTallNate/proxy-agents)(PACファイルを評価するためにvm2を利用していた)は`quickjs-emscripten`へ移行したようです。

- [Use `quickjs-emscripten` instead of `vm2` to execute PAC file code by TooTallNate · Pull Request #224 · TooTallNate/proxy-agents](https://github.com/TooTallNate/proxy-agents/pull/224)

`vm2`は`node:vm`上で実行するコードからホスト環境を参照できないようにパッチで塞いでいくアプローチをとっていました。(📝 `node:vm`を使ったことがある人向けの話。contextとして渡すオブジェクトにProxyを使い、特定のプロパティを参照できなくするなど)
これは軽量ですが、塞げない穴が出てきたり抜け漏れが出やすいアプローチです。

こういったSandboxにはどのようなアプローチがあるかは、次の記事が面白いと思います。

- [How to build a plugin system on the web and also sleep well at night | Figma Blog](https://www.figma.com/ja/blog/how-we-built-the-figma-plugin-system/)
- [Sandboxing and Workload Isolation · Fly](https://fly.io/blog/sandboxing-and-workload-isolation/)

---

Storybook 7.1がリリースされました。

- [Storybook 7.1](https://storybook.js.org/blog/storybook-7-1/)

Storybook上でオンボーディングの追加、Emotionなどのスタイリングライブラリのセットアップを自動化、Vueのサポートの改善などが含まれています。
また今までコミュニティ開発であったFigma design addonをコアのAddonとして管理するようになっています。

----

Deno向けのウェブアプリケーションフレームワークであるFresh 1.3がリリースされました。

- [Fresh 1.3 – Simplified Route Components and More](https://deno.com/blog/fresh-1.3)

非同期のルートコンポーネントをサポート、プラグインがルーティングやミドルウェアを定義できるように、`_500.tsx`でのエラーページのサポート、ErrorBoundaryのサポートなどが追加されています。
また、1ファイルから複数のislandsをexportできるように、`Deno.serve`のサポートなども追加されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ECMAScript proposal updates @ 2023-07 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2023/07/14/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2023/07/14/ecmascript-proposal-update "ECMAScript proposal updates @ 2023-07 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2023年7月のTC39 MeetingでのECMAScript Proposalのステータス変更のまとめ


----

## Discontinued · Issue #533 · patriksimek/vm2
[github.com/patriksimek/vm2/issues/533](https://github.com/patriksimek/vm2/issues/533 "Discontinued · Issue #533 · patriksimek/vm2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span></p>

Node.jsの`vm`モジュールを使ったSandboxを実現する目的の`vm2`に構造的なSandbox Escapeの脆弱性があるため、メンテナンスを終了するというアナウンス。
脆弱性のPoCは2023年8月ごろに公開されるため、isolated-vmのようなモジュールへ移行を推奨している。

- [vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database](https://github.com/advisories/GHSA-cchq-frgv-rjh5 "vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database")
- [laverdet/isolated-vm: Secure &amp; isolated JS environments for nodejs](https://github.com/laverdet/isolated-vm "laverdet/isolated-vm: Secure &amp;amp; isolated JS environments for nodejs")

----

## Release v0.18.13 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.13](https://github.com/evanw/esbuild/releases/tag/v0.18.13 "Release v0.18.13 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.13リリース。
`DEV: doAnExpensiveCheck()`のようなラベル指定した処理を、`--drop-label`で削除できるように。


----

## Release Notes for Safari Technology Preview 174 | WebKit
[webkit.org/blog/14390/release-notes-for-safari-technology-preview-174/](https://webkit.org/blog/14390/release-notes-for-safari-technology-preview-174/ "Release Notes for Safari Technology Preview 174 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 174リリース。
Canvas自体に設定された合計メモリ使用量の制限を削除など

- [Total Canvas Memory Use Exceeds The Maximum Limit - PQINA](https://pqina.nl/blog/total-canvas-memory-use-exceeds-the-maximum-limit/ "Total Canvas Memory Use Exceeds The Maximum Limit - PQINA")

----

## Node v18.17.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v18.17.0](https://nodejs.org/en/blog/release/v18.17.0 "Node v18.17.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.17.0リリース。
URLパーサのAda 2.0にアップデート、`URL.canParse`のサポート、Web Crypto APIの仕様との互換性の向上など


----

## Release 1.0.3 · kamranahmedse/driver.js
[github.com/kamranahmedse/driver.js/releases/tag/1.0.3](https://github.com/kamranahmedse/driver.js/releases/tag/1.0.3 "Release 1.0.3 · kamranahmedse/driver.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

サイトツアー表示をするDriver.js 1.0リリース。
TypeScriptで書き直し、SVGをページ上に載せてハイライト表示をするように実装を変更、ドキュメントを刷新など


----

## Storybook 7.1
[storybook.js.org/blog/storybook-7-1/](https://storybook.js.org/blog/storybook-7-1/ "Storybook 7.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 7.1リリース。
オンボーディングの追加、Emotionなどのスタイリングライブラリのセットアップを自動化、Vueのサポートの改善。
Figma design addonをコアに取り込むなど


----

## Chrome 116 beta - Chrome Developers
[developer.chrome.com/en/blog/chrome-116-beta/](https://developer.chrome.com/en/blog/chrome-116-beta/ "Chrome 116 beta - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 116 betaリリース。
CSS Motion Path、`display`と`content-visibility`に対してキーフレームアニメーションをサポート。
`AbortSignal.any()`のサポート、Fetch APIの`getReader({mode: 'byob'})`をサポート、Document Picture-in-Pictureのサポート。
Permissions Policy Originsに`*` wildcardの指定をサポート。
Origin TrialとしてCOOPの`restrict-properties`をサポート、EditContext APIのサポートなど

- [Use a ReadableStream with byte source (formerly called ReadableByteStream) for .body · Issue #267 · whatwg/fetch](https://github.com/whatwg/fetch/issues/267 "Use a ReadableStream with byte source (formerly called ReadableByteStream) for .body · Issue #267 · whatwg/fetch")
- [ReadableStream.getReader() - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/ReadableStream/getReader "ReadableStream.getReader() - Web API | MDN")
- [Wildcards in Permissions Policy Origins by arichiv · Pull Request #516 · w3c/webappsec-permissions-policy](https://github.com/w3c/webappsec-permissions-policy/pull/516 "Wildcards in Permissions Policy Origins by arichiv · Pull Request #516 · w3c/webappsec-permissions-policy")
- [w3c/edit-context: EditContext API](https://github.com/w3c/edit-context "w3c/edit-context: EditContext API")

----

## Fresh 1.3 – Simplified Route Components and More
[deno.com/blog/fresh-1.3](https://deno.com/blog/fresh-1.3 "Fresh 1.3 – Simplified Route Components and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Fresh 1.3リリース。
非同期のルートコンポーネントをサポート、プラグインがルーティングやミドルウェアを定義できるように、`_500.tsx`でのエラーページのサポート、ErrorBoundaryのサポート。
1ファイルから複数のislandsをexportできるように、`Deno.serve`のサポートなど

- [feat: support async route components by marvinhagemeister · Pull Request #1388 · denoland/fresh](https://github.com/denoland/fresh/pull/1388 "feat: support async route components by marvinhagemeister · Pull Request #1388 · denoland/fresh")
- [feat(server): plugins can add middlewares and routes by deer · Pull Request #1455 · denoland/fresh](https://github.com/denoland/fresh/pull/1455 "feat(server): plugins can add middlewares and routes by deer · Pull Request #1455 · denoland/fresh")

----

## Release v0.18.14 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.14](https://github.com/evanw/esbuild/releases/tag/v0.18.14 "Release v0.18.14 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.14リリース。
CSS Modulesサポートの一貫として、`global-css` loaderと`local-css` loaderを追加し、CSSで`:local()`と`:global()`をサポートなど。


----
<h1 class="site-genre">アーティクル</h1>

----

## URL.canParse
[davidwalsh.name/url-canparse](https://davidwalsh.name/url-canparse "URL.canParse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">article</span></p>

URLがパースできるかを判定する`URL.canParse`メソッドについて

- [URL: canParse() static method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URL/canParse_static "URL: canParse() static method - Web APIs | MDN")

----

## How React 18 Improves Application Performance – Vercel
[vercel.com/blog/how-react-18-improves-application-performance](https://vercel.com/blog/how-react-18-improves-application-performance "How React 18 Improves Application Performance – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18のTransitions、Suspense、Server Componentsについて


----

## Security alert: social engineering campaign targets technology industry employees - The GitHub Blog
[github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/](https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/ "Security alert: social engineering campaign targets technology industry employees - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">security</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

採用担当者や開発者になりすまし、プライベートリポジトリに招待、そのリポジトリをcloneしてインストールすると感染するマルウェアが仕込まれているという攻撃が増えている話。
マルウェアはnpm install時に、ダウンロードして実行される仕組みになっているという話

- [Phylum Discovers Sophisticated Ongoing Attack on NPM](https://blog.phylum.io/sophisticated-ongoing-attack-discovered-on-npm/ "Phylum Discovers Sophisticated Ongoing Attack on NPM")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## coderaiser/putout: 🐊 Pluggable and configurable JavaScript Linter and code transformer with built-in ESLint and Babel support for js, jsx typescript, flow, markdown, yaml and json. Write declarative codemods in a simplest possible way 😏
[github.com/coderaiser/putout](https://github.com/coderaiser/putout "coderaiser/putout: 🐊 Pluggable and configurable JavaScript Linter and code transformer with built-in ESLint and Babel support for js, jsx typescript, flow, markdown, yaml and json. Write declarative codemods in a simplest possible way 😏")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">Tools</span></p>

BabelとESLintをベースにしたcodemodのツールキット。
ビルトインルールとしてCommonJS to ESMなど多数の変換ルールを持っているが、それらを管理するツールとプラグインの仕組みを提供する。


----
