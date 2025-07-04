---
title: "2025-07-04のJS: ECMAScript 2025、Rspack 1.4、Deno 2.4、Bundle Sizeの改善"
author: "azu"
layout: post
date: 2025-07-04T01:25:12.237Z
category: JSer
tags:
  - React
  - css
  - rspack
  - Chrome
  - ECMAScript
---

JSer.info #740 - ECMAScript 2025 が正式にリリースされました。

- [Ecma International approves new standards - Ecma International](https://ecma-international.org/news/ecma-international-approves-new-standards-11/)
- [Release ES2025 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2025)

ECMAScript 2025 が Ecma International の General Assembly で承認され、正式にリリースされました。
ECMAScript 2025 では、次のような仕様が追加されています。

- Iterator helpers: iterator に対する map、filter、reduce などのメソッド
- Set.prototype メソッド: Set に対する集合演算を行うためのメソッド
- JSON modules インポート: JSON モジュールをインポートする機能と import attributes の仕様
- RegExp.escape メソッド: 正規表現をエスケープするためのメソッド
- 正規表現修飾子フラグ: 正規表現内でインラインで modifier flags を有効/無効にする構文を追加
- Promise.try メソッド: Promise を返すかどうか不明な関数を呼び出し、結果を常に Promise にするメソッド
- Float16Array: Float16 を扱う TypedArray 型

---

Rspack 1.4 がリリースされました。

- [Announcing Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

Wasm を利用したブラウザ環境での実行サポートが追加され、bundle size の改善も行われています。デフォルトで Incremental build が有効化され、実験的な CssChunkingPlugin の追加、MultiCompiler での lazy compilation サポートなどの機能強化が含まれています。また、Perfetto ベースのパフォーマンス分析ツールも追加されました。

---

Deno 2.4 がリリースされ、`deno bundle`コマンドが復活しました。

- [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4)

以前に廃止された`deno bundle`コマンドが復活し、テキストの`byte`インポート機能や OpenTelemetry の安定化が行われています。`--preload`フラグの追加、`deno update`コマンドの追加、package.json の conditional exports サポートなど、開発体験の向上を図る多くの機能が追加されています。

---

{% include inline-support.html %}

---

<h1 class="site-genre">ヘッドライン</h1>

---

## Announcing Rspack 1.4 - Rspack

[rspack.rs/blog/announcing-1-4](https://rspack.rs/blog/announcing-1-4 "Announcing Rspack 1.4 - Rspack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">ReleaseNote</span></p>

Rspack 1.4 リリース。
Wasm を利用してブラウザ環境での実行サポート、bundle size の改善。
デフォルトで Incremental build を有効化。
実験的な CssChunkingPlugin の追加、MultiCompiler で lazy compilation をサポート、`useInputFileSystem`オプションをサポート。
Perfetto ベースのパフォーマンス分析ツール、Zod v4 への更新など

---

## Chrome 139 beta  |  Blog  |  Chrome for Developers

[developer.chrome.com/blog/chrome-139-beta?hl&#x3D;en](https://developer.chrome.com/blog/chrome-139-beta?hl=en "Chrome 139 beta  |  Blog  |  Chrome for Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 139 beta リリース。
CSS では、`var()`/`attr()`の短絡評価のサポート、`caret-animation`/`corner-shape`/CSS Custom Functions のサポート。
WHATWG の仕様に合わせて`+json`の JSON MIME typ をサポート。
Origin trials で Prompt API、WebGPU Compatibility mode の追加。
macOS 11 サポート終了、ISO-2022-JP の自動検出の削除など

- [Intent to Ship: Spec-compliant JSON MIME type detection](https://groups.google.com/a/chromium.org/g/blink-dev/c/-lZFLXH7_Y8/m/ZzgLXc91AQAJ "Intent to Ship: Spec-compliant JSON MIME type detection")

---

## Ecma International approves new standards - Ecma International

[ecma-international.org/news/ecma-international-approves-new-standards-11/](https://ecma-international.org/news/ecma-international-approves-new-standards-11/ "Ecma International approves new standards - Ecma International")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

ECMAScript 2025 が Ecma の GA で承認され正式にリリースされた。

- [Release ES2025 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2025 "Release ES2025 · tc39/ecma262")

---

## Release 0.14.0 | StyleX

[stylexjs.com/blog/v0.14.0](https://stylexjs.com/blog/v0.14.0 "Release 0.14.0 | StyleX")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">library</span></p>

StyleX v0.14.0 リリース。
`viewTransitionClass` API を追加、lint に`validImports`オプションを追加。
破壊的な変更としてスタイルをマージするときの戦略を設定する`styleResolution`オプションのデフォルト値を`application-order`から`property-specificity`に変更

---

## Electron 37.0.0 | Electron

[www.electronjs.org/blog/electron-37-0](https://www.electronjs.org/blog/electron-37-0 "Electron 37.0.0 | Electron")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 37.0 リリース。
Chromium 138.0.7204.35/Node 22.16.0/V8 13.8 にアップデート。
`window.open`で`innerWidth`と`innerHeight`オプションをサポート、Node.js の`--experimental-network-inspection`をサポート。
unhandled rejection 動作変更、WebUSB/WebSerial API の blocklist サポートなど。

---

## Deno 2.4: deno bundle is back | Deno

[deno.com/blog/v2.4](https://deno.com/blog/v2.4 "Deno 2.4: deno bundle is back | Deno")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.4 リリース。
`deno bundle`コマンドの復活/テキストの`byte`インポート機能/OpenTelemetry の安定化。  
`--preload`フラグの追加/`deno update`コマンドの追加/`DENO_COMPAT`環境変数の追加、package.json の conditional exports をサポートなど

---

## Release v3.0.0 · recharts/recharts

[github.com/recharts/recharts/releases/tag/v3.0.0](https://github.com/recharts/recharts/releases/tag/v3.0.0 "Release v3.0.0 · recharts/recharts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">graphic</span> <span class="jser-tag">library</span></p>

Recharts 3 リリース。
Custom components のサポート、デフォルトで`accessibilityLayera11y`を有効に変更など

- [3.0 migration guide · recharts/recharts Wiki](https://github.com/recharts/recharts/wiki/3.0-migration-guide#breaking-code-changes "3.0 migration guide · recharts/recharts Wiki")

---

## dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions

[github.com/dahlia/logtape?tab&#x3D;readme-ov-file](https://github.com/dahlia/logtape?tab=readme-ov-file "dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ロガーライブラリ。
ライブラリとアプリケーションの利用を想定していて、Node.js/Deno/Browser などで動作し、構造化ログをサポートしている。
また、pino や winston などの別のロガーとの Integration を行う Adapter を提供している

---

<h1 class="site-genre">アーティクル</h1>

---

## CSS conditionals with the new if() function  |  Blog  |  Chrome for Developers

[developer.chrome.com/blog/if-article?hl&#x3D;en](https://developer.chrome.com/blog/if-article?hl=en "CSS conditionals with the new if() function  |  Blog  |  Chrome for Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">article</span></p>

CSS の`if()`関数について。
プロパティの値に対して`if()`と`style()`/`media()`/`suports()`を使った条件分岐を書く方法について

---

## How We Reduced CKEditor’s Bundle Size by 40% | CKEditor

[ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/](https://ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/ "How We Reduced CKEditor’s Bundle Size by 40% | CKEditor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">article</span></p>

CKEditor 5 の bundle size 最適化について。
バージョンずれの対策として re-export でパッケージをまとめたパッケージを公開していたが tree-shakin が効かずに bundle サイズの問題が起きた。
`/* #__PURE__ */`コメントの活用、ES2022 への target 変更、`sideEffects`フラグの設定などを行う tree shaking の問題を解決していった話。
また、Sonda を使った bundle 分析について

- [Sonda](https://sonda.dev/ "Sonda")

---

## \`useOptimistic\` to Make Your App Feel Instant | Epic React by Kent C. Dodds

[www.epicreact.dev/use-optimistic-to-make-your-app-feel-instant-zvyuv](https://www.epicreact.dev/use-optimistic-to-make-your-app-feel-instant-zvyuv "`useOptimistic` to Make Your App Feel Instant | Epic React by Kent C. Dodds")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React の`useOptimistic` hooks の使い方や`setState`との違いについて

---

<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

---

## photostructure/tz-lookup: JavaScript Library for Timezone Lookup by Location

[github.com/photostructure/tz-lookup](https://github.com/photostructure/tz-lookup "photostructure/tz-lookup: JavaScript Library for Timezone Lookup by Location")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

緯度経度から地名を検索するライブラリ

---
