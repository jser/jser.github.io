---
title: "2022-03-15のJS:  React 18 RC、playwright v1.20.0、Safari 15.4の変更点"
author: "azu"
layout: post
date : 2022-03-15T03:48:47.857Z
category: JSer
tags:
- React
- node.js
- TypeScript
- ECMAScript
- book

---

JSer.info #583 - React 18 RCがリリースされました。

- [How to Upgrade to the React 18 Release Candidate – React Blog](https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html)

React 18 RCではIEのサポートが終了しています。

ReactDOMの`render` APIをDeprecatedとし、`createRoot` APIの利用が推奨となっています。
SSR APIの`renderToNodeStream`を非推奨化し、Suspenseをサポートした`renderToPipeableStream`と`renderToReadableStream`が追加されています。

setStateなどのステート更新を自動的にバッジ処理するようにし、React 17の挙動を再現するための`flushSync`APIが追加されています。
また、ReduxなどのReact外でステート管理するライブラリ向けに`userId`/`useSyncExternalStore`/`useInsertionEffect` APIを追加。

その他には、開発時の`<StrictMode>`ではunmountとmountでの再マウントをテストするように挙動を変更されています。`global.IS_REACT_ACT_ENVIRONMENT`でテスト環境かどうかを判定するように変更されています。

---

playwright 1.20.0がリリースされました。

- [Release v1.20.0 · microsoft/playwright](https://github.com/microsoft/playwright/releases/tag/v1.20.0)

playwright 1.20.0では、スクリーンショットAPIにアニメーションの無効化、特定の箇所を隠す`mask`オプションの追加されています。
`expect().toMatchSnapshot()`がanomymouse snapshotsのサポート、`maxDiffPixels`と`maxDiffPixelRatio`オプションの追加されています。
また、テストファイルのテストケースごとに並列化をする`fullyParallel`モードのオプションが追加されています。

----

[New WebKit Features in Safari 15.4 | WebKit](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/)では、Safari 15.4の変更点についてまとめられています。

かなり色々な機能追加がありますが、主に次のような変更が含まれています。

- `<dialog>`要素のサポート
- CSSの`:has()`擬似クラス
- Cascade Layers
- CSS Containmentのサポート。
- Viewport Unitsとして`lvh`や`svh`などのサポート
- `:focus-visible`擬似クラスのサポート
- `calc()`でのmath functionのサポート
- 非標準な`-webkit-` prefixをいくつかのCSSプロパティから削除
- BroadcastChannelのサポート
- `window.scroll`の`scroll-behavior`プロパティのサポート
- `structuredClone` APIのサポート
- File System Access APIのサポート
- ES2022の`at()`メソッドと`Object.hasOwn()`メソッドのサポート
- Stage 3のProposalである`findLast()`メソッドのサポート
- `Intl`の実装を仕様に準拠するように更新
- Web App Manifestの対応改善
- `navigationPreload`のサポートなど
- `requestVideoFrameCallback()`のサポート
- CSP Lv3のサポート改善
- XSS Auditorの削除


----

<h1 class="site-genre">ヘッドライン</h1>

----

## How to Upgrade to the React 18 Release Candidate – React Blog
[reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html](https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html "How to Upgrade to the React 18 Release Candidate – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 18 RCリリース。
IEのサポートを終了。
ReactDOMの`render` APIをDeprecatedとし、`createRoot` APIの利用を推奨するように。
SSR APIの`renderToNodeStream`を非推奨化し、Suspenseをサポートした`renderToPipeableStream`と`renderToReadableStream`を追加。
`setState`のステート更新を自動的にバッジ処理するようにし、オプトアウト用の`flushSync`APIを追加。
また、ReduxなどのReact外でステート管理するライブラリ向けに`userId`/`useSyncExternalStore`/`useInsertionEffect` APIを追加。
開発時は`<StrictMode>`でunmountとmountでの再マウントをテストするように挙動を変更。
`global.IS_REACT_ACT_ENVIRONMENT`でテスト環境かどうかを設定できるように。


----

## Node v17.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.7.0/](https://nodejs.org/en/blog/release/v17.7.0/ "Node v17.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v17.7.0リリース。
`net.Socket`と`net.Server`に`noDelay`/`keepAlive`/`keepAliveInitialDelay`オプションの追加など


----

## Release v8.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v8.0.0](https://github.com/vueuse/vueuse/releases/tag/v8.0.0 "Release v8.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v8.0.0リリース。
`@vueuse/core/nuxt`を削除し、代わりに`@vueuse/nuxt`を公開。
`useTimeoutPoll`/`useDateFormat`/`useGamepad`/`useFileSystemAccess`/`useChangeCase`の追加など


----

## Release v8.0.0 · breejs/bree
[github.com/breejs/bree/releases/tag/v8.0.0](https://github.com/breejs/bree/releases/tag/v8.0.0 "Release v8.0.0 · breejs/bree")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JobスケジューラーのBree 8.0.0リリース。


----

## Release v1.20.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.20.0](https://github.com/microsoft/playwright/releases/tag/v1.20.0 "Release v1.20.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.20.0リリース。
スクリーンショットAPIにアニメーションの無効化、特定の箇所を隠す`mask`オプションの追加。
`expect().toMatchSnapshot()`がanomymouse snapshotsのサポート、`maxDiffPixels`と`maxDiffPixelRatio`オプションの追加。
テストの設定に`fullyParallel`モートを追加など


----

## New WebKit Features in Safari 15.4 | WebKit
[webkit.org/blog/12445/new-webkit-features-in-safari-15-4/](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/ "New WebKit Features in Safari 15.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 15.4の変更点について。
`<dialog>`要素のサポート、CSSの`:has()`擬似クラス、Cascade Layers、CSS Containmentのサポート。
Viewport Unitsとして`lvh`や`svh`などのサポート、`:focus-visible`擬似クラスのサポート、`calc()`でのmath functionのサポート。
非標準な`-webkit-` prefixをいくつかのCSSプロパティから削除。
BroadcastChannel、`window.scroll`の`scroll-behavior`プロパティ、`structuredClone`、File System Access APIのサポート。
ES2022の`at()`メソッドと`Object.hasOwn()`メソッド、Stage 3のProposalである`findLast()`メソッドのサポートなど。
`Intl`の実装を仕様に準拠するように更新、Web App Manifestの対応改善、`navigationPreload`のサポートなど。
`requestVideoFrameCallback()`のサポート、CSP Lv3のサポート改善、XSS Auditorの削除など


----
<h1 class="site-genre">アーティクル</h1>

----

## Learn PWA
[web.dev/learn/pwa/](https://web.dev/learn/pwa/ "Learn PWA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">tutorial</span></p>

PWAについて学べるチュートリアル。


----

## Typed Ember is now the Ember TypeScript Core Team!
[blog.emberjs.com/typed-ember-is-now-the-ember-type-script-core-team/](https://blog.emberjs.com/typed-ember-is-now-the-ember-type-script-core-team/ "Typed Ember is now the Ember TypeScript Core Team!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

EmberのTypeScriptサポートをコアのサブチームとして進めるという話。
Ember CLIへの統合、Glintでのテンレプーと型チェック、Ember自体の型定義の改善、RFCのTypeScriptへの影響調査などを行うチーム

- [0724-road-to-typescript](https://emberjs.github.io/rfcs/0724-road-to-typescript.html "0724-road-to-typescript")
- [typed-ember/glint: TypeScript powered tooling for Glimmer templates](https://github.com/typed-ember/glint "typed-ember/glint: TypeScript powered tooling for Glimmer templates")

----

## A Proposal For Type Syntax in JavaScript - TypeScript
[devblogs.microsoft.com/typescript/a-proposal-for-type-syntax-in-javascript/](https://devblogs.microsoft.com/typescript/a-proposal-for-type-syntax-in-javascript/ "A Proposal For Type Syntax in JavaScript - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

TypeScriptチームが、実行時には消去可能なコメントとしての型構文をECMAScriptのProposalとして提案するという話

- [giltayar/proposal-types-as-comments: ECMAScript proposal for type syntax that is erased - Stage 0](https://github.com/giltayar/proposal-types-as-comments "giltayar/proposal-types-as-comments: ECMAScript proposal for type syntax that is erased - Stage 0")

----

## JavaScript naming conflicts: How existing code can force proposed features to be renamed
[2ality.com/2022/03/naming-conflicts.html](https://2ality.com/2022/03/naming-conflicts.html "JavaScript naming conflicts: How existing code can force proposed features to be renamed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">issue</span></p>

ECMAScriptの新しいProposalが既存のWebを壊すbreak the webがどのように起きるかについての解説記事。
ビルトインのprototoypeの変更、プロパティ名の競合、グローバル名の衝突、withによる衝突など


----

## WebGPU — All of the cores, none of the canvas — surma.dev
[surma.dev/things/webgpu/](https://surma.dev/things/webgpu/ "WebGPU — All of the cores, none of the canvas — surma.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGPU</span> <span class="jser-tag">article</span></p>

WebGPUについて解説記事。
WebGLはOpenGLのラッパーであるが、WebGPUは独自の抽象化レイヤーを持っている、またWGSLというWebGPUのシェーディング言語について


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## daisyUI — Tailwind CSS Components
[daisyui.com/](https://daisyui.com/ "daisyUI — Tailwind CSS Components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

UIコンポーネントの見た目を提供するTailwindプラグイン。
クラス名にコンポーネントの指定することでUIを定義し、カスタムはクラス名にTailwindのUtilityを指定することで行う


----
<h1 class="site-genre">書籍関係</h1>

----

## Micro State Management with React Hooks | Packt
[www.packtpub.com/product/micro-state-management-with-react-hooks/9781801812375](https://www.packtpub.com/product/micro-state-management-with-react-hooks/9781801812375 "Micro State Management with React Hooks | Packt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

Reactでのステート管理について書籍


----
