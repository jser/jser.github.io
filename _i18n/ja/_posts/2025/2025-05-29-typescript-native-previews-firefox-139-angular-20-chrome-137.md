---
title: "2025-05-29のJS: TypeScript Native Previews、Firefox 139、Angular 20、Chrome 137"
author: "azu"
layout: post
date: 2025-05-29T01:31:32.863Z
category: JSer
tags:
- TypeScript
- Bun
- nodejs
- ESLint
- golang

---

JSer.info #736 - TypeSciptのGo言語でのネイティブ実装である`@typescript/native-preview`が公開されました。

- [Announcing TypeScript Native Previews - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

TypeScriptをGo言語に移植した実装で、コンパイラである`tsgo`と合わせてVSCode拡張などもリリースされています。

- [TypeScriptネイティブ移植観察レポート TSKaigi 2025 - Speaker Deck](https://speakerdeck.com/berlysia/typescript-native-porting-observation-tskaigi-2025)


---

Firefox 139がリリースされました。

- [Firefox 139.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/139.0/releasenotes/)
- [Firefox 139 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/139)

`hidden=until-found`属性のサポートとTemporal APIの実装が含まれています。実験的機能として、Prioritized Task Scheduling API、View Transition API、HTMLの属性における`<`と`>`の自動エスケープ機能が追加されています。

---

Angular v20がリリースされました。

- [Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301)

`effect`、`linkedSignal`、`toSignal`、Incremental hydrationとroute-level render mode configがStableに変更されました。ZonelessはDeveloper Previewに移行し、実験的機能として`httpResource`とvitestサポートが追加されています。また、Chrome DevToolsでのAngular固有のパフォーマンス情報を扱う`ng.enableProfiling()` APIが追加されています。
また、`*ngIf`/`*ngFor`/`*ngSwitch`の非推奨化も含まれています。

---

Chrome 137がリリースされました。

- [New in Chrome 137  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-137)
- [Chrome 137  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/137)

CSS関連では条件付き値を表現する`if()`関数と、フォーカスナビゲーション順序を制御する`reading-flow`/`reading-order`プロパティが追加されました。Web API関連では、Selection APIに`getComposedRanges()`と`direction`プロパティ、Web CryptographyでのEd25519サポートが追加されています。WebAssemblyでは、JavaScript Promise Integration（JSPI）の正式サポートが含まれています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node.js — Node v24.1.0 (Current)
[nodejs.org/en/blog/release/v24.1.0](https://nodejs.org/en/blog/release/v24.1.0 "Node.js — Node v24.1.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.1.0リリース。
`node:fs`の`glob`がStableとなり、experimentalのwarningが出ないようになった


----

## Announcing TypeScript Native Previews - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-native-previews/](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/ "Announcing TypeScript Native Previews - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">golang</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScriptのGo言語のネイティブ実装である`@typescript/native-preview`が公開された


----

## Bun v1.2.14 | Bun Blog
[bun.sh/blog/bun-v1.2.14](https://bun.sh/blog/bun-v1.2.14 "Bun v1.2.14 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.14リリース。
`bun install`が`catalog:`をサポート、Fetch APIがzstdをサポート、`"module": "Preserve"`をデフォルト値に変更など


----

## Release v9.0.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v9.0.0](https://github.com/storybookjs/storybook/releases/tag/v9.0.0 "Release v9.0.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook v9.0.0リリース。


----

## Firefox 139.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/139.0/releasenotes/](https://www.mozilla.org/en-US/firefox/139.0/releasenotes/ "Firefox 139.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 139リリース。
`hidden=until-found`のサポート、Temporarl APIをサポート。
実験的な機能として、Prioritized Task Scheduling API/View Transition API/属性における`<`と`>`を自動エスケープなど

- [Firefox 139 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/139 "Firefox 139 for developers - Mozilla | MDN")

----

## Bun v1.2.15 | Bun Blog
[bun.sh/blog/bun-v1.2.15](https://bun.sh/blog/bun-v1.2.15 "Bun v1.2.15 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.15リリース。
`bun audit`の追加、`BUN_OPTIONS`の環境変数を追加、`vm.SourceTextModule`をサポート、`perf_hooks.createHistogram()`をサポートなど


----

## Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog
[blog.angular.dev/announcing-angular-v20-b5c9c06cf301](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301 "Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v20.リリース。
`effect`/`linkedSignal`/`toSignal`、Incremental hydrationとroute-level render mode configがStableに変更。
ZonelessがDeveloper Previewに変更。
実験的な機能として`httpResource`を追加、vitestのサポート。
Chrome DevToolsでAngular特有のパフォーマンス情報を扱う`ng.enableProfiling()` APIを追加。
template expressionで`**`と`in`演算子。
`*ngIf`/`*ngFor`/`*ngSwitch`の非推奨化など


----

## New in Chrome 137  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-137?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-137?hl=en "New in Chrome 137  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 137リリース。
CSS関連では、条件付き値を表現する `if()` 関数が追加。
フォーカスナビゲーション順序を制御する `reading-flow`/`reading-order`プロパティを追加。筆記体での文字間隔を無視する改善、`accent-color` プロパティでのシステムアクセントカラー対応を実装。`offset-path: shape()` サポート。

Web API関連では、Selection APIに `getComposedRanges()` と `direction` プロパティが追加。Blob URLのパーティショニング（fetch/navigation）が実装。
Web Cryptographyでの `Ed25519` サポートが追加。HSTSキャッシュを使ったトラッキングを防止する機能を実装。応答しないWebページのクラッシュレポートをReporting APIでサポート。

WebAssemblyでは、JavaScript Promise Integration（JSPI）の正式サポートが追加。
branch hintのサポートなど

- [Chrome 137  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/137 "Chrome 137  |  Release notes  |  Chrome for Developers")

----
<h1 class="site-genre">アーティクル</h1>

----

## ESLint v9.0.0: A retrospective - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/](https://eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/ "ESLint v9.0.0: A retrospective - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint v9.0.0のretrospective。
うまくいった点とうまくいかなかった点について。
サポートバージョンのポリシーとv8.x/v9.xの共存とバックポートはうまく行った。
一方で破壊的な変更が多すぎた問題と、ツールが足りなくてアップデートが大変になっていた問題やエコシステムとの協調性が不足していた点について


----

## TSKaigi資料まとめ
[zenn.dev/m\_n/articles/a1189e28e43313](https://zenn.dev/m_n/articles/a1189e28e43313 "TSKaigi資料まとめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">document</span></p>

TSKaigi 2025のスライドまとめ

- [TSKaigi 2025](https://2025.tskaigi.org/ "TSKaigi 2025")

----

## Wake up, Remix! | Remix
[remix.run/blog/wake-up-remix](https://remix.run/blog/wake-up-remix "Wake up, Remix! | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

Remixの今後の方向性について。
Remix v2はReact Routerの薄いラッパーとなった。
Remix v3ではDBや組み込みコンポーネントを含むフレームワークとなり、またReactではなくPreactのforkをベースにしたものを組み込む予定。
Remixの基本的な方針について書かれている


----

## A brief history of JavaScript | Deno
[deno.com/blog/history-of-javascript](https://deno.com/blog/history-of-javascript "A brief history of JavaScript | Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">history</span></p>

ブラウザ/JavaScript/ライブラリの歴史をタイムラインでまとめたもの


----

## Introducing \`jsr:\` Support
[blog.vlt.sh/blog/jsr-support](https://blog.vlt.sh/blog/jsr-support "Introducing \`jsr:\` Support")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

vltが`jsr:` prefixでJSRパッケージのインストールをサポート


----

## React, visualized – react.gg
[react.gg/visualized](https://react.gg/visualized "React, visualized – react.gg")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

Reactの動作をビジュアライズして紹介しているサイト


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 2025-05-23 SignalとObservable ― 新たなデータモデルを解きほぐす (TSKaigi 2025) - Google スライド
[docs.google.com/presentation/d/1c7fYqn7-v3hnbKtmwXHbvwuCs6cNq\_ThLKVDZ7rvbA0/preview#slide&#x3D;id.g260298bad6d\_0\_77](https://docs.google.com/presentation/d/1c7fYqn7-v3hnbKtmwXHbvwuCs6cNq_ThLKVDZ7rvbA0/preview#slide=id.g260298bad6d_0_77 "2025-05-23 SignalとObservable ― 新たなデータモデルを解きほぐす (TSKaigi 2025) - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

ECMAScript Stage 1のSignalsとWCIG Observableについてのスライド。
Pull/Pushベースの連続する値の扱いについて


----
