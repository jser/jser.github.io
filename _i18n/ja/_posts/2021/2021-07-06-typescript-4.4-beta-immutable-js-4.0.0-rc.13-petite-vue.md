---
title: "2021-07-06のJS: TypeScript 4.4 Beta、immutable-js 4.0.0-rc.13、petite-vue"
author: "azu"
layout: post
date : 2021-07-05T22:36:05.800Z
category: JSer
tags:
- node.js
- Chrome
- WebAssembly
- アンケート
- Markdown

---

JSer.info #547 - TypeScript 4.4 betaがリリースされました。

- [Announcing TypeScript 4.4 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/)

Control Flow Analysisの改善され、Type Gurdeの結果を変数に入れてから扱うようなAliasのケースも正しく推論されるようになっています。
また、Index SignaturesにSymbolやTemplate Stringを利用できるようになっています。
Catch節のデフォルトを`unknown`型にする`useUnknownInCatchVariables`オプションの追加と
optionalと`undefined`値の区別をする`exactOptionalPropertyTypes`オプションの追加されています。

その他には、declarationの生成や`strict`モードでのビルドパフォーマンスの改善も含まれています。

----

immutable-js 4.0.0-rc.13がリリースされています。

- [Release 4.0.0-rc.13 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13)

immutable-jsは[v4.0.0-rc.12](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.12)でメンテナンスが停止して、[immutable-oss](https://github.com/immutable-js-oss) organiztionにてforkとしてメンテナンスがされていました。

今回のリリースでは、`immutable-js` organizationに`immutable-oss`のメンテナが追加され、`immutable-oss`の変更内容もimmutable-js 4.0.0-rc.13へとマージされています。
改めて`immutable-js`としてメンテナンスを再開するリリースとなっています。

- [Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/issues/1689)
- [Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/pull/1833)

----

Vueのサブセットとしてファイルサイズが小さなpetite-vueが公開されています。

- [vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement](https://github.com/vuejs/petite-vue)

Vue互換のテンプレート構文とサブセットのAPIをもつライブラリです。
ES Modulesとしてimportして利用できるようになっていて、Vueにはない`v-scope`や`v-effect`などの仕組みも持っています。
[Alpine.js](https://alpinejs.dev/)のように既存のレンダリングされたHTMLに対して動作を追加する小さなライブラリを目的としています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Support caching dependencies and LTS aliases · actions/setup-node
[github.com/actions/setup-node/releases/tag/v2.2.0](https://github.com/actions/setup-node/releases/tag/v2.2.0 "Release Support caching dependencies and LTS aliases · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

`actions/setup-node` 2.2.0リリース。 `lts/*`などのLTS構文のサポート、`cache`オプションで`npm`と`yarn`での依存キャッシュをサポートなど


----

## Announcing TypeScript 4.4 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/ "Announcing TypeScript 4.4 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Prototype.js</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.4 Betaリリース。 Control Flow Analysisの改善、Index SignaturesにSymbolやTemplate Stringを利用できるように。
Catch節のデフォルトを`unknown`型にする`useUnknownInCatchVariables`オプションの追加。
optionalと`undefined`値の区別をする`exactOptionalPropertyTypes`オプションの追加。
declarationの生成や`strict`モードでのビルドパフォーマンスの改善も含まれている


----

## Release 4.0.0-rc.13 · immutable-js/immutable-js
[github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13 "Release 4.0.0-rc.13 · immutable-js/immutable-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

imutable-js 4.0.0 RC12リリース。
forkであった`immutable-js-oss`の変更内容をマージし、コミュニティによるメンテナンスを再開するリリース。

- [Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/issues/1689 "Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js")
- [Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/pull/1833 "Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js")

----

## vite/CHANGELOG.md at main · vitejs/vite
[github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#240-2021-07-05](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#240-2021-07-05 "vite/CHANGELOG.md at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 2.4.0リリース。
`new URL(url, import.meta.url)`のサポート、`server.fsServe`を`server.fs`にリネーム、`server.fs.strict`オプションの追加など

- [Static Asset Handling | Vite](https://vitejs.dev/guide/assets.html#the-public-directory "Static Asset Handling | Vite")

----
<h1 class="site-genre">アーティクル</h1>

----

## The State of WebAssembly 2021
[blog.scottlogic.com/2021/06/21/state-of-wasm.html](https://blog.scottlogic.com/2021/06/21/state-of-wasm.html "The State of WebAssembly 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">アンケート</span></p>

WebAssemblyについての開発者アンケート。
どの言語を使っているか、どの用途に利用しているか、求める機能などについて


----

## RenderingNG - Chrome Developers
[developer.chrome.com/blog/renderingng/](https://developer.chrome.com/blog/renderingng/ "RenderingNG - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">blink</span> <span class="jser-tag">article</span></p>

ChromeのレンダリングエンジンであるBlinkの新しいアーキテクチャであるRenderingNGの主要プロジェクトのまとめ記事。
CompositeAfterPaint、LayoutNG、BlinkNG、Viz、OffscreenCanvas、VideoNGなどについて


----

## Migrating from Capybara to Puppeteer - Engineering Blog - Wealthfront
[eng.wealthfront.com/2021/06/25/migrating-from-capybara-to-puppeteer/](https://eng.wealthfront.com/2021/06/25/migrating-from-capybara-to-puppeteer/ "Migrating from Capybara to Puppeteer - Engineering Blog - Wealthfront")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

E2EテストをCapybaraからPuppeteerに移行した話。
E2Eテストフレームワークの選択と、移行する目的であった実行時間の短縮について


----

## Designing a Dataflow Editor With TypeScript and React | Protocol Labs Research
[research.protocol.ai/blog/2021/designing-a-dataflow-editor-with-typescript-and-react/](https://research.protocol.ai/blog/2021/designing-a-dataflow-editor-with-typescript-and-react/ "Designing a Dataflow Editor With TypeScript and React | Protocol Labs Research")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">ElasticSearch</span></p>

ReactとTypeScriptでデータフローエディタを作る際の設計についての記事。
データフローの状態の設計、スキーマオブジェクトから各Nodeの型定義を取り出す仕組みをGenericsを使って扱う方法について。

- [joeltg/react-dataflow-editor](https://github.com/joeltg/react-dataflow-editor "joeltg/react-dataflow-editor")

----

## Encoding data for POST requests - JakeArchibald.com
[jakearchibald.com/2021/encoding-data-for-post-requests/](https://jakearchibald.com/2021/encoding-data-for-post-requests/ "Encoding data for POST requests - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Fetchのbodyに安全にエンコードしたデータを渡す方法について。
`URLSearchParams`、`FormData`、`blob`、JSONを使った方法について紹介している


----

## Image To Text Conversion With React And Tesseract.js (OCR) — Smashing Magazine
[www.smashingmagazine.com/2021/06/image-text-conversion-react-tesseract-js-ocr/](https://www.smashingmagazine.com/2021/06/image-text-conversion-react-tesseract-js-ocr/ "Image To Text Conversion With React And Tesseract.js (OCR) — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Tesseract.jsを使った画像のOCRとCanvasを使った下処理についての記事。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement
[github.com/vuejs/petite-vue](https://github.com/vuejs/petite-vue "vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

VueサブセットのAPIとテンプレートをもったライブラリ。
ファイルサイズを小さくすることを目的にしている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Saul-Mirone/milkdown: 🍼 Plugin driven WYSIWYG markdown editor.
[github.com/saul-mirone/milkdown/](https://github.com/saul-mirone/milkdown/ "Saul-Mirone/milkdown: 🍼 Plugin driven WYSIWYG markdown editor.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

ProsemirrorとremarkベースのWYSIWYG markdownエディタライブラリ


----

## niksy/promise-any-ponyfill: \`Promise.any\` ponyfill.
[github.com/niksy/promise-any-ponyfill](https://github.com/niksy/promise-any-ponyfill "niksy/promise-any-ponyfill: \`Promise.any\` ponyfill.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">polyfill</span></p>

`Promise.any`のpolyfillライブラリ


----

## tinyhttp/malibu: 🏄 Framework-agnostic CSRF middleware for modern Node.js
[github.com/tinyhttp/malibu](https://github.com/tinyhttp/malibu "tinyhttp/malibu: 🏄 Framework-agnostic CSRF middleware for modern Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

CSRF対策のexpress middleware。


----
