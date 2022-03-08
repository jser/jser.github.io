---
title: "2022-03-08のJS: TypeScript 4.6、Chrome 100 beta、新しいMDN"
author: "azu"
layout: post
date : 2022-03-08T03:17:40.310Z
category: JSer
tags:
- TypeScript
- React
- node.js
- webpack
- bundler

---

JSer.info #582 - TypeScript 4.6がリリースされました。

- [Announcing TypeScript 4.6 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/)

TypeScript 4.6では型推論の改善が行われています。
また、`--target es2022`のサポート、`checkJs`が有効時のJavaScriptの構文エラーのチェックが改善されています。

次の4.7では、[TypeScript 4.5](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/)で保留となっていたNode.js ESMの対応を進める予定となっています。

- [TypeScript 4.7 Iteration Plan · Issue #48027 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/48027)

---

Chrome 100 betaがリリースされました。

- [Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More](https://blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html)

バージョンが`100`と3桁となるため、ChromeとFirefoxで問題が起きるサイトがあることが予想されています。

- [Version 100 in Chrome and Firefox - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/02/version-100-in-chrome-and-firefox/)

また、Chrome 100 betaではUser-Agent文字列を削減していくフェーズ3に入りました。
Chrome 100がUA文字列を削減する前の最後のバージョンとなり、101から段階的にUA文字列を削減していくフェーズになります。

- [Chromium Blog: User-Agent Reduction Origin Trial and Dates](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html)
- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)

その他には、マルチスクリーン時にどこにWindowを表示するかを指定d系るMulti-Screen Window Placement APIの追加などが行われています。

- [Managing several displays with the Multi-Screen Window Placement API](https://web.dev/multi-screen-window-placement/)

---

[MDN Web Docs](https://developer.mozilla.org)(MDN)のデザインやロゴなどが刷新されています。
また、MDN Plusというサブスクリプションで通知や追加コンテンツなどを得られる有料機能を公開することが予定されています。

詳細は次の記事で解説されています。

- [A new year, a new MDN - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v5.70.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.70.0](https://github.com/webpack/webpack/releases/tag/v5.70.0 "Release v5.70.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack v5.70.0リリース。
ESMにおける`require.context`相当の機能として`import.meta.webpackContext`を追加。
ESMサポートの対象にNode.js 12を追加など


----

## Release v0.14.24 · evanw/esbuild
[github.com/evanw/esbuild/releases/v0.14.24](https://github.com/evanw/esbuild/releases/v0.14.24 "Release v0.14.24 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.14.24リリース。
targetに`es2022`をサポート、`define`オプションインデックス指定の場合も置換できるように、`--mangle-quoted`の追加など


----

## Release Notes for Safari Technology Preview 141 | WebKit
[webkit.org/blog/12434/release-notes-for-safari-technology-preview-141/](https://webkit.org/blog/12434/release-notes-for-safari-technology-preview-141/ "Release Notes for Safari Technology Preview 141 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 141リリース。
CSS `overflow: clip`の有効化、import assertion構文をフラグ付きで実装、CSPの`wasm-unsafe-eval`を実装など


----

## Announcing TypeScript 4.6 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-6/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/ "Announcing TypeScript 4.6 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.6リリース。
DestructuringとUnionの組み合わせ、再帰型、インターフェースへのインデックスアクセス、関数の引数における型推論の改善。
`--target es2022`のサポート、`checkJs`が有効時のJavaScriptの構文エラーのチェックを改善。


----

## Release v28.0.0-alpha.7 · facebook/jest
[github.com/facebook/jest/releases/tag/v28.0.0-alpha.7](https://github.com/facebook/jest/releases/tag/v28.0.0-alpha.7 "Release v28.0.0-alpha.7 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">ReleaseNote</span></p>

Jest v28.0.0-alpha.7リリース。
複数のマシンでテストを分割して実行できる`--shared`フラグの実装など

- [feat: implement \`--shard\` option by marionebl · Pull Request #12546 · facebook/jest](https://github.com/facebook/jest/pull/12546 "feat: implement \&#x60;--shard\&#x60; option by marionebl · Pull Request #12546 · facebook/jest")

----

## Release v6.0.0-alpha.0 · styled-components/styled-components
[github.com/styled-components/styled-components/releases/tag/v6.0.0-alpha.0](https://github.com/styled-components/styled-components/releases/tag/v6.0.0-alpha.0 "Release v6.0.0-alpha.0 · styled-components/styled-components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

styled-components v6.0.0-alpha.0リリース。
TypeScriptでの書き直し、stylis v4へのアップデート、Node.js 14未満のサポート終了など

- [\[breaking\] stylis v4 by probablyup · Pull Request #3241 · styled-components/styled-components](https://github.com/styled-components/styled-components/pull/3241 "\[breaking\] stylis v4 by probablyup · Pull Request #3241 · styled-components/styled-components")

----

## Release v10.7.0 · TypeStrong/ts-node
[github.com/TypeStrong/ts-node/releases/tag/v10.7.0](https://github.com/TypeStrong/ts-node/releases/tag/v10.7.0 "Release v10.7.0 · TypeStrong/ts-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">node.js</span></p>

ts-node v10.7.0リリース。
`--esm`フラグと`ts-node-esm`バイナリを追加など


----

## Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More
[blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html](https://blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html "Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 100 betaリリース。
Chrome 100がUA文字列を削減する前の最後のバージョン隣、101から段階的にUA文字列を削減していく。
Multi-Screen Window Placement APIの追加、
Origin TrialとしてMedia Source ExtensionsをWorkerで動かせるように。
`AbortSignal.prototype.throwIfAborted()`の追加、`HIDDevice forget()`の追加など。

- [Chromium Blog: User-Agent Reduction Origin Trial and Dates](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html "Chromium Blog: User-Agent Reduction Origin Trial and Dates")

----
<h1 class="site-genre">アーティクル</h1>

----

## A new year, a new MDN - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/ "A new year, a new MDN - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">article</span></p>

MDNのデザインとロゴの更新について。
また、追加機能や追加コンテンツを提供する予定のMDN Plusというサブスクリプションサービスについて

- [MDN Web Docs](https://developer.mozilla.org/ "MDN Web Docs")

----

## Working together on Interop 2022 | WebKit
[webkit.org/blog/12288/working-together-on-interop-2022/](https://webkit.org/blog/12288/working-together-on-interop-2022/ "Working together on Interop 2022 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span> <span class="jser-tag">testing</span> <span class="jser-tag">WebPlatformAPI</span></p>

ブラウザの相互運用性に取り組むInterop 2022について。
Apple/Google/Microsoft/Mozilla/Bocoup/Igaliaなどが協力して、ウェブプラットフォームでフォーカスしているエリアについての相互運用性の取り組みについて。
WPTを使った計測やフォーカスしたエリアについての紹介など

- [web-platform-tests dashboard](https://wpt.fyi/interop-2022 "web-platform-tests dashboard")
- [Interop 2022: browsers working together to improve the web for developers](https://web.dev/interop-2022/ "Interop 2022: browsers working together to improve the web for developers")
- [Microsoft Edge and Interop 2022 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2022/03/03/microsoft-edge-and-interop-2022/ "Microsoft Edge and Interop 2022 - Microsoft Edge Blog")
- [Announcing Interop 2022 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/03/interop-2022/ "Announcing Interop 2022 - Mozilla Hacks - the Web developer blog")
- [Bocoup and Interop 2022 - web standards - Bocoup](https://bocoup.com/blog/interop-2022 "Bocoup and Interop 2022 - web standards - Bocoup")
- [Igalia and Interop 2022 | Igalia](https://www.igalia.com/news/interop2022.html "Igalia and Interop 2022 | Igalia")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## nodeshift/nodejs-reference-architecture: The Red Hat and IBM Node.js Reference architecture. The teams &#039;opinion&#039; on what components our customers and internal teams should use when building Node.js applications and guidance for how to be successful in production with those components.
[github.com/nodeshift/nodejs-reference-architecture](https://github.com/nodeshift/nodejs-reference-architecture "nodeshift/nodejs-reference-architecture: The Red Hat and IBM Node.js Reference architecture. The teams &#039;opinion&#039; on what components our customers and internal teams should use when building Node.js applications and guidance for how to be successful in production with those components.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">document</span> <span class="jser-tag">Docker</span></p>

Node.jsプロジェクトのアーキテクチャやライブラリの選定などについてのリファレンスをまとめたガイドライン。
Dockerやnpm周りの設定、ジャンルごとのライブラリやフレームワーク、運用回りのロギングやトレースなど一通りの内容がまとめられている

- [Node.js Reference Architecture | Node.JS Reference Architecture](https://nodeshift.dev/nodejs-reference-architecture/ "Node.js Reference Architecture | Node.JS Reference Architecture")

----
<h1 class="site-genre">書籍関係</h1>

----

## フロントエンドのデザインパターン
[zenn.dev/morinokami/books/learning-patterns-1](https://zenn.dev/morinokami/books/learning-patterns-1 "フロントエンドのデザインパターン")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">architecture</span> <span class="jser-tag">book</span> <span class="jser-tag">React</span></p>

patterns.dev の翻訳本。
ReactやJavaScriptにおけるデザインパターンの解説

- [Patterns.dev - Modern Web App Design Patterns](https://www.patterns.dev/ "Patterns.dev - Modern Web App Design Patterns")

----
