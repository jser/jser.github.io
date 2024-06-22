---
title: "2024-06-22のJS: Nuxt 2 EOL、TypeScript 5.5、State of JavaScript 2023の結果"
author: "azu"
layout: post
date: 2024-06-22T06:10:01.531Z
category: JSer
tags:
- Vue
- ECMAScript
- nodejs
- Chrome
- proposal

---

JSer.info #697 - - [Nuxt 2 End-of-Life (EOL) · Nuxt Blog](https://nuxt.com/blog/nuxt2-eol)
- [Announcing TypeScript 5.5 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/)
- [State of JavaScript 2023](https://2023.stateofjs.com/en-US/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Nuxt 2 End-of-Life (EOL) · Nuxt Blog
[nuxt.com/blog/nuxt2-eol](https://nuxt.com/blog/nuxt2-eol "Nuxt 2 End-of-Life (EOL) · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

Nuxt 2は2024年6月30日でEnd-of-Life (EOL)となる。
Nuext 2.xの最終版となる2.18.0が6月末にリリースされる予定


----

## Nuxt 3.12 · Nuxt Blog
[nuxt.com/blog/v3-12](https://nuxt.com/blog/v3-12 "Nuxt 3.12 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.12リリース。
Nuxt 4の動作をopt-inして試せる`compatibilityVersion: 4`オプションの追加、`multiApp`オプションの追加、不要になったexprimentalオプションの削除など

- [Upgrade Guide · Get Started with Nuxt](https://nuxt.com/docs/getting-started/upgrade#testing-nuxt-4 "Upgrade Guide · Get Started with Nuxt")

----

## New in Chrome 126  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-126?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-126?hl=en "New in Chrome 126  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 126リリース。
Cross-document view transitionsのサポート、CloseWatcher APIを再有効化。
import assertionの`assert`構文を削除など

- [Chrome 126  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/126 "Chrome 126  |  Release notes  |  Chrome for Developers")

----

## Electron 31.0.0 | Electron
[www.electronjs.org/blog/electron-31-0](https://www.electronjs.org/blog/electron-31-0 "Electron 31.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 31リリース。
Chromium 125、Node.js 20.14、V8 12.6へアップデート。
WebSQLの削除、File System APIのサポートなど


----

## Release Version 8.12.0 · acornjs/acorn
[github.com/acornjs/acorn/releases/tag/8.12.0](https://github.com/acornjs/acorn/releases/tag/8.12.0 "Release Version 8.12.0 · acornjs/acorn")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

acorn 8.12.0リリース。
ES2025のduplicate capture group names in regular expressionsをサポートなど


----

## Bun v1.1.13 | Bun Blog
[bun.sh/blog/bun-v1.1.13](https://bun.sh/blog/bun-v1.1.13 "Bun v1.1.13 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.13リリース。
`worker_thread`の`eval`オプションをサポート、`URL.createObjectURL`のサポート、`expect`のカスタムメッセージをサポートなど


----

## Version 4.0 released : Node-RED
[nodered.org/blog/2024/06/20/version-4-0-released](https://nodered.org/blog/2024/06/20/version-4-0-released "Version 4.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node-RED 4.0リリース。


----

## Announcing TypeScript 5.5 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-5/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/ "Announcing TypeScript 5.5 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.5リリース。
関数からtype predicatesを推論できるようになり、`Array.prototype.filter`などでの絞り込みが簡潔に書けるように。
Stage 3のSet Methodsをサポート。
JSDocで`@import {foo} from "foo"`をサポート、正規表現の基本的な構文チェックをサポート、`isolatedDeclarations`をサポート。
設定ファイル内で`${configDir}`のテンプレート値をサポート。
`typescript`パッケージのサイズを削減、Named Importをサポート、`transpileDeclaration` APIの追加。
`transpileModule`と`transpileDeclaration`でのビルド時間を改善。
`out`や`target: ES3`などの非推奨となっていたオプションが無効化され、`ignoreDeprecations`オプションを指定しないと利用できなくなる変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## ECMAScript proposal updates @ 2024-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/06/15/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/06/15/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2024年6月のTC39 MeetingにおけるECMAScript Proposalのステータス変更のまとめ。


----

## Codemod partnering with the React team
[codemod.com/blog/react-announcement](https://codemod.com/blog/react-announcement "Codemod partnering with the React team")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 19に関するcodemod

- [codemod/packages/codemods/react/19 at main · codemod-com/codemod](https://github.com/codemod-com/codemod/tree/main/packages/codemods/react/19 "codemod/packages/codemods/react/19 at main · codemod-com/codemod")

----

## Build Stunning Responsive Card Tables with CSS4 &amp; CSS5 - DEV Community
[dev.to/subu\_hunter/build-stunning-responsive-card-tables-with-css4-css5-1fai](https://dev.to/subu_hunter/build-stunning-responsive-card-tables-with-css4-css5-1fai "Build Stunning Responsive Card Tables with CSS4 &amp; CSS5 - DEV Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Tableとscroll-snapを使ったカヌーセル的なカード型のテーブルデザインについて


----

## Node.js Security Progress Report: Redefining Security Processes and Key Initiatives | OpenJS Foundation
[openjsf.org/blog/nodejs-security-progress-report-may-2024?utm\_content&#x3D;297186945&amp;utm\_medium&#x3D;social&amp;utm\_source&#x3D;twitter&amp;hss\_channel&#x3D;tw-91985735](https://openjsf.org/blog/nodejs-security-progress-report-may-2024?utm_content=297186945&utm_medium=social&utm_source=twitter&hss_channel=tw-91985735 "Node.js Security Progress Report: Redefining Security Processes and Key Initiatives | OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.jsのセキュリティについてのレポート。
`--experimental-policy`の削除、Permission ModelのInitiative phaseの完了など


----

## State of JavaScript 2023
[2023.stateofjs.com/en-US/](https://2023.stateofjs.com/en-US/ "State of JavaScript 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span></p>

State of JavaScript 2023の結果が公開された。
JavaScriptの言語機能、フレームワーク、ツール、テスト、TypeScriptなどについてのアンケート


----
