---
title: "2020-07-21のJS: Chrome 84(SameSite Cookie)、Vue 3 RC、React Spectrum"
author: "azu"
layout: post
date : 2020-07-21T02:20:24.850Z
category: JSer
tags:
- Chrome
- Vue
- React

---

JSer.info #497 - Chrome 84がリリースされました。

- [New in Chrome 84  |  Web  |  Google Developers](https://developers.google.com/web/updates/2020/07/nic84)
- [Chromium Blog: Chrome 84 Beta: Web OTP, Web Animations, New Origin Trials and More](https://blog.chromium.org/2020/05/chrome-84-beta-web-otp-web-animations.html)
- [Chrome Platform Status: milestone=84](https://www.chromestatus.com/features#milestone%3D84)


Web animations APIの対応改善、Content Indexing API、Wake lock API、`WeakRef`のサポートなどが含まれています。
また、Origin trialsとしてIdle detection、Web Assembly SIMDのサポートされています。

- [Fast, parallel applications with WebAssembly SIMD · V8](https://v8.dev/features/simd)

元々Chrome 80でロールアウト予定だったSame Site Cookieのロールアウトの再開がされています。

- [Chromium Blog: Resuming SameSite Cookie Changes in July](https://blog.chromium.org/2020/05/resuming-samesite-cookie-changes-in-july.html)

その他にはTLS 1.0と1.1のサポートの削除されています。
実際にTLS 1.0や1.1での接続を確認するには[badssl\.com](https://badssl.com/)などが利用できます。

この変更はFirefoxとSafariでも予定されています。

- [Release Notes for Safari Technology Preview 91 | WebKit](https://webkit.org/blog/9526/release-notes-for-safari-technology-preview-91/)
- [TLS 1.0/1.1 対応が初期設定で無効化されました (影響あり) | Firefox サイト互換性情報](https://www.fxsitecompat.dev/ja/docs/2020/tls-1-0-1-1-support-has-been-disabled-by-default/)

----

Vue 3 RCがリリースされています。

- [Vue 3 is now in RC! · Issue #189 · vuejs/rfcs](https://github.com/vuejs/rfcs/issues/189)

Vue 3の正式リリースは8月の予定です。
RCのリリースに合わせて、マイグレーションガイドが公開されています。

- [Introduction | Vue.js](https://v3.vuejs.org/guide/migration/introduction.html)

RCではまだIE11サポートが完了していないため、正式リリースまでには対応していく予定とのことです。

----

Adobeからデザインシステム向けのReactフレームワークが公開されています。

- [adobe/react-spectrum: A collection of libraries and tools that help you build adaptive, accessible, and robust user experiences.](https://github.com/adobe/react-spectrum)
- [React Spectrum Libraries](https://react-spectrum.adobe.com/index.html)

[React Aria](https://react-spectrum.adobe.com/react-aria/getting-started.html)はWAI-ARIAに対応する機能を提供するReact Hooks、[React Stately](https://react-spectrum.adobe.com/react-stately/getting-started.html)は一般的なコンポーネントの状態管理をするReact Hooksです。
これらはWAI-ARIAやキーボード操作などのアクセシビリティ、i18の仕組みなどを提供することが目的で、他のデザインシステムでも利用できるような作りになっています。

また、これらを利用したAdobeのデザインシステムのReactコンポーネントの実装のライブラリとして[React Spectrum](https://react-spectrum.adobe.com/react-spectrum/getting-started.html)が公開されています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Chrome 84  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/07/nic84](https://developers.google.com/web/updates/2020/07/nic84 "New in Chrome 84  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 84リリース。
Content Indexing API、Wake lock API、`WeakRef`のサポート。
Origin trialsとしてIdle detection、Web Assembly SIMDのサポート。
Same Site Cookieのロールアウトの再開、TLS 1.0と1.1のサポートの削除など

- [V8 release v8.4 · V8](https://v8.dev/blog/v8-release-84 "V8 release v8.4 · V8")
- [Chromium Blog: Chrome 84 Beta: Web OTP, Web Animations, New Origin Trials and More](https://blog.chromium.org/2020/05/chrome-84-beta-web-otp-web-animations.html "Chromium Blog: Chrome 84 Beta: Web OTP, Web Animations, New Origin Trials and More")

----

## Vue 3 is now in RC! · Issue #189 · vuejs/rfcs
[github.com/vuejs/rfcs/issues/189](https://github.com/vuejs/rfcs/issues/189 "Vue 3 is now in RC! · Issue #189 · vuejs/rfcs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 3 RCリリース。
マイグレーションガイドも合わせて公開されている。

- [Introduction | Vue.js](https://v3.vuejs.org/guide/migration/introduction.html "Introduction | Vue.js")

----

## Release 2.0.0 · naver/billboard.js
[github.com/naver/billboard.js/releases/tag/2.0.0](https://github.com/naver/billboard.js/releases/tag/2.0.0 "Release 2.0.0 · naver/billboard.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

D3.jsベースのチャートライブラリであるbillboard.js 2.0.0リリース。
TypeScriptでの書き直し、ファイルサイズとパフォーマンスの改善、一部オプションのシグネチャーの変更、`.transform()`の非推奨化など

- [📊 billboard.js 2.0 is out! 🎉🎊, more smaller and faster. | by Jae Sung Park | Jul, 2020 | Medium](https://medium.com/@alberto.park/billboard-js-2-0-is-out-15e84b52ab11 "📊 billboard.js 2.0 is out! 🎉🎊, more smaller and faster. | by Jae Sung Park | Jul, 2020 | Medium")
- [CHANGELOG v2 · naver/billboard.js Wiki](https://github.com/naver/billboard.js/wiki/CHANGELOG-v2 "CHANGELOG v2 · naver/billboard.js Wiki")

----

## ESLint v7.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/07/eslint-v7.5.0-released](https://eslint.org/blog/2020/07/eslint-v7.5.0-released "ESLint v7.5.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 7.5.0リリース。
Optional Chainingのサポート、`id-blacklist`を非推奨化し`id-denylist`に変更など


----

## Announcing the Release of Apollo Client 3.0 - Apollo Blog
[www.apollographql.com/blog/announcing-the-release-of-apollo-client-3-0/](https://www.apollographql.com/blog/announcing-the-release-of-apollo-client-3-0/ "Announcing the Release of Apollo Client 3.0 - Apollo Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

GraphQL ClientのApollo Client 3.0リリース。
`InMemoryCache`に`evict()`や`gc()`などを追加、`makeVar`によるReactive variablesの追加など。

- [Release 3.0.0 · apollographql/apollo-client](https://github.com/apollographql/apollo-client/releases/tag/v3.0.0 "Release 3.0.0 · apollographql/apollo-client")

----
<h1 class="site-genre">アーティクル</h1>

----

## Generating UUIDs at scale on the Web | by Matthieu Wipliez | Teads Engineering | Jul, 2020 | Medium
[medium.com/teads-engineering/generating-uuids-at-scale-on-the-web-2877f529d2a2](https://medium.com/teads-engineering/generating-uuids-at-scale-on-the-web-2877f529d2a2 "Generating UUIDs at scale on the Web | by Matthieu Wipliez | Teads Engineering | Jul, 2020 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

クライアントサイトでのUUID生成について。
`URL.createObjectURL`と`crypto.getRandomValues`を使ったランダムなUUIDの生成とcollisionについて


----

## Dynamic CSS Components Without JavaScript: Every Layout
[every-layout.dev/blog/css-components/](https://every-layout.dev/blog/css-components/ "Dynamic CSS Components Without JavaScript: Every Layout")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

style属性でCSS Custom Propertyを指定することで、CSSに対して値を渡す方法について。

- [なぜ私たちはCSSフレームワークを使わないのか - Scott Tolinksi氏、Reactive Conf](https://www.infoq.com/jp/news/2020/07/css-variables-design-systems/ "なぜ私たちはCSSフレームワークを使わないのか - Scott Tolinksi氏、Reactive Conf")

----

## eslint-plugin-vue で来たる Vue.js 3 のリリースに備えよう - BASE開発チームブログ
[devblog.thebase.in/entry/2020/07/16/141446](https://devblog.thebase.in/entry/2020/07/16/141446 "eslint-plugin-vue で来たる Vue.js 3 のリリースに備えよう - BASE開発チームブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

ESLintを使ったVue 3の対応チェックについて。
Vueで非推奨となった機能やVue3で廃止される機能をESLintでチェックする話


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## adobe/react-spectrum: A collection of libraries and tools that help you build adaptive, accessible, and robust user experiences.
[github.com/adobe/react-spectrum](https://github.com/adobe/react-spectrum "adobe/react-spectrum: A collection of libraries and tools that help you build adaptive, accessible, and robust user experiences.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">i18n</span> <span class="jser-tag">Keyboard</span></p>

WAI-ARIAとコンポーネントの状態管理をするReact Hooks、AdobeのデザインシステムのReactコンポーネントの実装のライブラリ。
WAI-ARIAやキーボード操作などのアクセシビリティ、i18の仕組みなどを提供することが目的

- [React Spectrum](https://react-spectrum.adobe.com/index.html "React Spectrum")

----

## richardanaya/tour\_of\_rust: A tour of rust's language features
[github.com/richardanaya/tour\_of\_rust](https://github.com/richardanaya/tour_of_rust "richardanaya/tour\_of\_rust: A tour of rust's language features")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">tutorial</span></p>

WebAssemblyのツアー式チュートリアル


----

## iamakulov/awesome-webpack-perf: A curated list of webpack tools for web performance
[github.com/iamakulov/awesome-webpack-perf](https://github.com/iamakulov/awesome-webpack-perf "iamakulov/awesome-webpack-perf: A curated list of webpack tools for web performance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span> <span class="jser-tag">performance</span></p>

webpackのパフォーマンス関係のプラグイン、Loaderのまとめ。
最適化を行うloaderやbundleの分析を行うプラグインなどをまとめたもの


----

## Zizzamia/perfume.js: Web performance library for measuring all User-centric performance metrics
[github.com/zizzamia/perfume.js](https://github.com/zizzamia/perfume.js "Zizzamia/perfume.js: Web performance library for measuring all User-centric performance metrics")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span></p>

ブラウザのさまざまなパフォーマンスメトリクスを取得できるJavaScriptライブラリ。
Navigation Timing、Element Timing、Web Vitalsなどに対応している


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## breejs/bree: Bree is the best job scheduler for Node.js with support for cron, dates, ms, later, and human-friendly strings. Uses workers and spawns sandboxed processes. Supports async/await, retries, throttling, concurrency, and cancelable jobs (graceful shutdown). Simple, fast, and the most lightweight tool for the job. Made for Forward Email and Lad.
[github.com/breejs/bree](https://github.com/breejs/bree "breejs/bree: Bree is the best job scheduler for Node.js with support for cron, dates, ms, later, and human-friendly strings. Uses workers and spawns sandboxed processes. Supports async/await, retries, throttling, concurrency, and cancelable jobs (graceful shutdown). Simple, fast, and the most lightweight tool for the job. Made for Forward Email and Lad.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsのjob scheduler/cron処理ライブラリ


----

## getify/moduloze: Convert CommonJS (CJS) modules to UMD and ESM formats
[github.com/getify/moduloze](https://github.com/getify/moduloze "getify/moduloze: Convert CommonJS (CJS) modules to UMD and ESM formats")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">module</span> <span class="jser-tag">Bluetooth</span></p>

CommonJSをUMDとES Modulesに変換するツール


----

## lukeed/dequal: A tiny (305B) utility for check for deep equality
[github.com/lukeed/dequal](https://github.com/lukeed/dequal "lukeed/dequal: A tiny (305B) utility for check for deep equality")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

deep-equalライブラリ


----

## lukeed/klona: A tiny (423B) and fast utility to "deep clone" Objects, Arrays, Dates, RegExps, and more!
[github.com/lukeed/klona](https://github.com/lukeed/klona "lukeed/klona: A tiny (423B) and fast utility to \"deep clone\" Objects, Arrays, Dates, RegExps, and more!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

deep-cloneライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Building Micro-Frontends: the book - Building Micro-Frontends
[www.buildingmicrofrontends.com/](https://www.buildingmicrofrontends.com/ "Building Micro-Frontends: the book - Building Micro-Frontends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MicroFrontend</span> <span class="jser-tag">book</span></p>

MicroFrontendについての書籍。
DAZNでのMicroFrontendアーキテクチャについて


----
