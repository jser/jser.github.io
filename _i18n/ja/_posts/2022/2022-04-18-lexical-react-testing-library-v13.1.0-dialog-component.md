---
title: "2022-04-18のJS: Lexical、React Testing Library v13.1.0、Dialog componentの作成"
author: "azu"
layout: post
date : 2022-04-18T13:36:16.175Z
category: JSer
tags:
- React
- HTML
- JSON
- TypeScript
- polyfill

---

JSer.info #588 - Lexicalというテキストエディタを作るためのJavaScriptフレームワークが公開されました。

- [facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.](https://github.com/facebook/lexical)

エディタの状態をdouble-bufferingで管理して、状態の変更をdiff/patchで表示に反映させる仕組みを持っている。
またcontentEditableを使っているが、外部からの変更をMutationObserverで監視し、エディタの状態を更新している。

Lexicalは同じくFacebookが作成している[Draft.js](https://draftjs.org/)の後継となるライブラリで、APIの互換性はありませんが、今後マイグレーションガイドを作成していく予定とのことです。

- [Add Draft JS to Lexical migration documentation · Issue #1641 · facebook/lexical](https://github.com/facebook/lexical/issues/1641)

----

React DOMのテストライブラリであるReact Testing Library v13.1.0がリリースされました。

- [Release v13.1.0 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0)

React Testing Library v13.1.0では、`renderHook`というAPIが追加されています。
このAPIは、React Hooksのテストをするためのもので、[`@testing-library/react-hooks`](https://github.com/testing-library/react-hooks-testing-library)の実装を元にしています。

詳しい経緯は次のPRで書かれていますが、[`@testing-library/react-hooks`](https://github.com/testing-library/react-hooks-testing-library)はReact 18の対応が難しい部分があったため、`renderHook`というシンプルなAPIが`@testing-library/react`へと実装されました。

- [feat: Add `renderHook` by eps1lon · Pull Request #991 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/pull/991)

そのため、今後`@testing-library/react-hooks`は非推奨する予定となっています。

- https://github.com/testing-library/react-hooks-testing-library#a-note-about-react-18-support

----

[Building a dialog component](https://web.dev/building-a-dialog-component/)という記事では`<dialog>`要素を使ったダイアログコンポーネントの作成について書かれています。

`inert`属性、`autofocus`属性、CSSの`overscroll-behavior`プロパティなど、関連するアクセシビリティの機能などについても書かれているので、興味がある人は読んでみると良さそうです。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 3.22.0 - 2022.04.15 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.22.0](https://github.com/zloirock/core-js/releases/tag/v3.22.0 "Release 3.22.0 - 2022.04.15 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.22.0リリース。
Change Array by copy proposalの仕様追従、`atob`/`btoa`の修正、compat dataの更新など


----

## Release v1.4.0 · remix-run/remix
[github.com/remix-run/remix/releases/tag/v1.4.0](https://github.com/remix-run/remix/releases/tag/v1.4.0 "Release v1.4.0 · remix-run/remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Remix</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Remix v1.4.0リリース。
`remix`という単独のパッケージを参照させる"magic imports"という仕組みのために、`node_modules`を直接編集してたがpnpmなどで動かない問題があった。
そのため、それぞれのパッケージを参照するようにするためのマイグレーションスクリプトの公開とそれに関連する変更が含まれている。


----

## Release v8.0.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v8.0.0](https://github.com/reduxjs/react-redux/releases/tag/v8.0.0 "Release v8.0.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.0.0リリース。
コードベースをTypeScriptに書き換え、APIの互換性は維持している。
`useSyncExternalStore`を使ったReact 18の対応、TypeScriptの型定義から`DefaultRootState`を削除、`connectAdvanced`の削除など


----

## util: add parseArgs module by bcoe · Pull Request #42675 · nodejs/node
[github.com/nodejs/node/pull/42675](https://github.com/nodejs/node/pull/42675 "util: add parseArgs module by bcoe · Pull Request #42675 · nodejs/node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proposal</span> <span class="jser-tag">issue</span></p>

Node.jsにコマンドライン引数のパースをする`util.parseArgs`を追加するProposal

- [pkgjs/parseargs: Polyfill of future proposal for \`util.parseArgs()\`](https://github.com/pkgjs/parseargs "pkgjs/parseargs: Polyfill of future proposal for \&#x60;util.parseArgs()\&#x60;")

----

## Release v13.1.0 · testing-library/react-testing-library
[github.com/testing-library/react-testing-library/releases/tag/v13.1.0](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0 "Release v13.1.0 · testing-library/react-testing-library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

react-testing-library 13.1.0リリース。
React 18のHooksをテストするための`renderHook` APIを追加。

- [feat: Add \`renderHook\` by eps1lon · Pull Request #991 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/pull/991 "feat: Add \&#x60;renderHook\&#x60; by eps1lon · Pull Request #991 · testing-library/react-testing-library")
- [testing-library/react-hooks-testing-library: 🐏 Simple and complete React hooks testing utilities that encourage good testing practices.](https://github.com/testing-library/react-hooks-testing-library#a-note-about-react-18-support "testing-library/react-hooks-testing-library: 🐏 Simple and complete React hooks testing utilities that encourage good testing practices.")

----

## Release 2.0.0-beta.1 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-beta.1](https://github.com/vercel/swr/releases/tag/2.0.0-beta.1 "Release 2.0.0-beta.1 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-beta.1リリース。
`useSWR`が`isLoading`を返すように、`keepPreviousData`オプションの追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## New React 18 features and changes - Xebia
[xebia.com/new-react-18-features-and-changes/](https://xebia.com/new-react-18-features-and-changes/ "New React 18 features and changes - Xebia")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18の変更点についての解説。
Concurrent renderer、createRoot/hydrateRootとonRecoverableErrorについて。
Automatic batchingとflushSync。
新しく追加されたHooks APIであるuseTransition/useDeferredValue、useId、useSyncExternalStore、useInsertionEffectについて


----

## なぜ我々はsession.cookieを変更しなければならなかったのか - BASEプロダクトチームブログ
[devblog.thebase.in/entry/2022/04/13/114714](https://devblog.thebase.in/entry/2022/04/13/114714 "なぜ我々はsession.cookieを変更しなければならなかったのか - BASEプロダクトチームブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">privacy</span> <span class="jser-tag">article</span></p>

Public Suffix Listへの追加申請と、ブラウザに同梱されるタイミングの話。
ブラウザの復元機能によって、変更前と変更後の同名Cookieが存在してしまう問題とブラウザごとの挙動の違いについて。


----

## Building a dialog component
[web.dev/building-a-dialog-component/](https://web.dev/building-a-dialog-component/ "Building a dialog component")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">accessibility</span></p>

`<dialog>`要素を使ったダイアログの作成とアクセシビリティについての記事。
ダイアログ表示とユーザー入力を無視する`inert`属性、`autofocus`属性、ESCキーでの非表示。
`<dialog>`要素のスタイル、Header/Footerのデザイン、`overscroll-behavior`でのbody scroll lock、JavaScriptとの連携方法について


----

## Boost Resource Loading With fetchpriority, a New Priority Hint — Smashing Magazine
[www.smashingmagazine.com/2022/04/boost-resource-loading-new-priority-hint-fetchpriority/](https://www.smashingmagazine.com/2022/04/boost-resource-loading-new-priority-hint-fetchpriority/ "Boost Resource Loading With fetchpriority, a New Priority Hint — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">performance</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

リソースロードの優先度を定義する`fetchpriority`属性について。

- [WICG/priority-hints: A browser API to enable developers signal the priorities of the resources they need to download.](https://github.com/WICG/priority-hints "WICG/priority-hints: A browser API to enable developers signal the priorities of the resources they need to download.")
- [HTMLIFrameElement.fetchpriority - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/fetchpriority "HTMLIFrameElement.fetchpriority - Web APIs | MDN")

----

## 从 Turborepo 看 Monorepo 工具的任务编排能力 · Issue #13 · worldzhao/blog
[github.com/worldzhao/blog/issues/13](https://github.com/worldzhao/blog/issues/13 "从 Turborepo 看 Monorepo 工具的任务编排能力 · Issue #13 · worldzhao/blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

monorepoにおける依存関係の管理、タスクのスケジューリング、バージョン管理について。
タスクの並列実行、トポロジカルソース、TurborepoとRushのアプローチ、リモートキャッシュについての解説。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.
[github.com/facebook/lexical](https://github.com/facebook/lexical "facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

テキストエディタを作るためのJavaScriptフレームワーク。
エディタの状態をdouble-bufferingで管理している。
状態の変更をdiff/patchで表示に反映させる。
またcontentEditableを使っているが、外部からの変更をMutationObserverで監視し、エディタの状態を更新している。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ThomasAribart/json-schema-to-ts: Infer TS types from JSON schemas 📝
[github.com/ThomasAribart/json-schema-to-ts](https://github.com/ThomasAribart/json-schema-to-ts "ThomasAribart/json-schema-to-ts: Infer TS types from JSON schemas 📝")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

JSON SchemaからTypeScriptの型へ変換するライブラリ


----

## Shopify/javy: JS to WebAssembly toolchain
[github.com/Shopify/javy](https://github.com/Shopify/javy "Shopify/javy: JS to WebAssembly toolchain")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">Tools</span></p>

JavaScriptのコードを実行するWebAssembly。
JavaScriptエンジンにはQuickJSを利用している。
Shopifyで利用されている。


----

## ehmicky/wild-wild-path: 🤠 Object property paths with wildcards and regexps 🌵
[github.com/ehmicky/wild-wild-path](https://github.com/ehmicky/wild-wild-path "ehmicky/wild-wild-path: 🤠 Object property paths with wildcards and regexps 🌵")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`*`と正規表現でマッチしたオブジェクトのプロパティの取得と設定ができるライブラリ


----
