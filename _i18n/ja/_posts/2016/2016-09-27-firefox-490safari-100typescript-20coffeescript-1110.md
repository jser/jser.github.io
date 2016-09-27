---
title: "2016-09-27のJS: Firefox 49.0、Safari 10.0、TypeScript 2.0、CoffeeScript 1.11.0"
author: azu
layout: post
date : 2016-09-27T08:34
category: JSer
tags:
    - Firefox
    - Safari
    - TypeScript
    - CoffeeScript

---

JSer.info #298 - [Firefox 49](https://www.mozilla.jp/firefox/49.0/releasenotes/ "Firefox 49")がリリースされました。

- [Firefox 49 for developers](https://developer.mozilla.org/ja/Firefox/Releases/49 "Firefox 49 for developers")
- [Firefox 49 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/49/ "Firefox 49 サイト互換性情報 | Firefox サイト互換性情報")
- [Firefox 49 fixes sites designed with WebKit in mind, and more ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/09/firefox-49-fixes-sites-designed-with-webkit-in-mind-and-more/ "Firefox 49 fixes sites designed with WebKit in mind, and more ★ Mozilla Hacks – the Web developer blog")

Web Speech APIの音声合成をサポートや[Window.isSecureContext](https://developer.mozilla.org/ja/docs/Web/API/Window/isSecureContext "Window.isSecureContext")のサポート、
既存のサイトとの互換性のために`-webkit` prefixのサポートが追加されています。

- [Webkit! RESOLVED FIXED - otsukare](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")

----

[Safari 10.0](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_10_0.html "Safari 10.0")がリリースされました。

IndexedDB、CSP 2.0、Shadow DOM v1、ES2015、Font Loading、ECMAScript i18n APIのサポートなどが行われています。
また、WebDriverや開発者ツールの改善なども行われています。

----

[TypeScript 2.0](https://blogs.msdn.microsoft.com/typescript/2016/09/22/announcing-typescript-2-0/ "TypeScript 2.0")がリリースされました。

DefinitelyTypedの型定義ファイルをnpmモジュール(`@type`)としてインストールできるように、non-nullable、read only modifierのサポートなどが追加されています。

破壊的な変更や具体的な変更はWikiにまとまっているので下記を参照してください。

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-20 "Breaking Changes · Microsoft/TypeScript Wiki")
- [What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki")

----

CoffeeScript [1.11.0](http://coffeescript.org/#1.11.0 "1.11.0")がリリースされました。

- [http://coffeescript.org/#1.11.0](http://coffeescript.org/#1.11.0)

`import`/`export`の構文をサポート、`--inline-map`コマンドラインオプションのサポートなどが行われています。

最近になって[coffeescript6/discuss: A place to discuss the future of CoffeeScript](https://github.com/coffeescript6/discuss "coffeescript6/discuss: A place to discuss the future of CoffeeScript")というリポジトリで、今後のCoffeeScriptをどうするかという議論が活発化しています。

今回のリリースは、[アクティブなメンテナー](https://github.com/lydell)と[アクティブなコミッター](https://github.com/GeoffreyBooth)により行われました。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Dev.Opera — What’s new in Chromium 53 and Opera 40
[dev.opera.com/blog/opera-40/](https://dev.opera.com/blog/opera-40/ "Dev.Opera — What’s new in Chromium 53 and Opera 40")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

input patternのRegExpが`u`フラグ扱いに、Shadow DOM v1、MediaStreamTrack Constraints APIの追加など

----

## Firefox 49.0 リリースノート
[www.mozilla.jp/firefox/49.0/releasenotes/](https://www.mozilla.jp/firefox/49.0/releasenotes/ "Firefox 49.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 49リリース。
既存コンテンツの互換性のために`-webkit-` prefixのプロパティをサポート、`<a>`要素の`referrerpolicy`属性のサポート、Web Speech APIの音声合成をサポートなど

- [Firefox 49 for developers](https://developer.mozilla.org/ja/Firefox/Releases/49 "Firefox 49 for developers")
- [Firefox 49 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/49/ "Firefox 49 サイト互換性情報 | Firefox サイト互換性情報")
- [Firefox 49 fixes sites designed with WebKit in mind, and more ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/09/firefox-49-fixes-sites-designed-with-webkit-in-mind-and-more/ "Firefox 49 fixes sites designed with WebKit in mind, and more ★ Mozilla Hacks – the Web developer blog")

----

## Safari 10.0
[developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari\_10\_0.html](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_10_0.html "Safari 10.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">apple</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 10.0リリース。
IndexedDB、CSP 2.0、Shadow DOM v1、ES2015、Font Loading、ES i18n APIのサポートなど

----

## PM2 v2 - Bradbury
[keymetrics.io/2016/08/24/pm2-v2-released/](https://keymetrics.io/2016/08/24/pm2-v2-released/ "PM2 v2 - Bradbury")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Docker</span> <span class="jser-tag">ReleaseNote</span></p>

PM2 V2リリース。
pm2-docker、transpilerサポートなど

----

## TypeScript 2.0 is now available! | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/09/22/announcing-typescript-2-0/](https://blogs.msdn.microsoft.com/typescript/2016/09/22/announcing-typescript-2-0/ "TypeScript 2.0 is now available! | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.0リリース。
DefinitelyTypedの型定義ファイルをnpmモジュールとしてインストールできるように、non-nullable、read only modifierなど

- [| TypeScript 2.0 Awesomeness | Blog | SitePen](https://www.sitepen.com/blog/2016/09/01/typescript-2-0-awesomeness/ "| TypeScript 2.0 Awesomeness | Blog | SitePen")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-20 "Breaking Changes · Microsoft/TypeScript Wiki")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki")

----

## CoffeeScript
[coffeescript.org/#1.11.0](http://coffeescript.org/#1.11.0 "CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">ReleaseNote</span></p>

CoffeeScript 1.11.0リリース。
`import`/`export`の構文をサポート、`--inline-map`コマンドラインオプションのサポートなど

- [treat Infinity and NaN as reserved words · Issue #4218 · jashkenas/coffeescript](https://github.com/jashkenas/coffeescript/issues/4218 "treat Infinity and NaN as reserved words · Issue #4218 · jashkenas/coffeescript")
- [Support import and export of ES2015 modules by GeoffreyBooth · Pull Request #4300 · jashkenas/coffeescript](https://github.com/jashkenas/coffeescript/pull/4300 "Support import and export of ES2015 modules by GeoffreyBooth · Pull Request #4300 · jashkenas/coffeescript")
- [Opt-in ESNext features in 1.x · Issue #40 · coffeescript6/discuss](https://github.com/coffeescript6/discuss/issues/40 "Opt-in ESNext features in 1.x · Issue #40 · coffeescript6/discuss")

----

## ESLint v3.6.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/09/eslint-v3.6.0-released](http://eslint.org/blog/2016/09/eslint-v3.6.0-released "ESLint v3.6.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.6.0リリース。
async/awaitの対応と既存ルールの修正、`--fix`対応ルールの追加など

- [ESLint v3.6.0 - Qiita](http://qiita.com/mysticatea/items/9fd48f9ac3faac578c62 "ESLint v3.6.0 - Qiita")

----

## jQuery 3.1.1 Released! | Official jQuery Blog
[blog.jquery.com/2016/09/22/jquery-3-1-1-released/](http://blog.jquery.com/2016/09/22/jquery-3-1-1-released/ "jQuery 3.1.1 Released! | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.1.1リリース
`:disabled`セレクタのバグ修正、AMDとして読み込んだときに`noConflict`を公開するようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Ahead-of-Time Compilation in Angular 2 – Minko Gechev&#x27;s blog
[blog.mgechev.com/2016/08/14/ahead-of-time-compilation-angular-offline-precompilation/](http://blog.mgechev.com/2016/08/14/ahead-of-time-compilation-angular-offline-precompilation/ "Ahead-of-Time Compilation in Angular 2 – Minko Gechev's blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AnguarJS 2のAhead-of-Time (AOT)について

----

## Welcome to HTML 5.2!Telerik Developer Network
[developer.telerik.com/featured/welcome-to-html-5-2/](http://developer.telerik.com/featured/welcome-to-html-5-2/ "Welcome to HTML 5.2!Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">HTML</span></p>

W3C HTML5.2について。
5.1からの差分について

----

## Snapshot Testing in React Storybook
[voice.kadira.io/snapshot-testing-in-react-storybook-43b3b71cec4f](https://voice.kadira.io/snapshot-testing-in-react-storybook-43b3b71cec4f "Snapshot Testing in React Storybook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span></p>

React Storybookを使ったスナップショットテストについて

- [kadirahq/storyshots: Snapshot testing for React Storybook](https://github.com/kadirahq/storyshots "kadirahq/storyshots: Snapshot testing for React Storybook")
- [kadirahq/react-storybook: UI Component Dev Environment for React](https://github.com/kadirahq/react-storybook "kadirahq/react-storybook: UI Component Dev Environment for React")

----

## Testing Components in Angular 2 with Jasmine - Semaphore
[semaphoreci.com/community/tutorials/testing-components-in-angular-2-with-jasmine](https://semaphoreci.com/community/tutorials/testing-components-in-angular-2-with-jasmine "Testing Components in Angular 2 with Jasmine - Semaphore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AngularJS 2のコンポーネントをjasmineでテストする話

----

## Use Easy-Fix to Run Integration Tests Like Unit Tests – WalmartLabs – Medium
[medium.com/walmartlabs/use-easy-fix-to-run-integration-tests-like-unit-tests-834288ec446d](https://medium.com/walmartlabs/use-easy-fix-to-run-integration-tests-like-unit-tests-834288ec446d "Use Easy-Fix to Run Integration Tests Like Unit Tests – WalmartLabs – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

vcr系のテストライブラリ。
実行結果を記録/リプレイするライブラリ。
他のVCR系とは異なり非同期処理を記録することで、HTTPのみ限定していないという話

- [walmartlabs/easy-fix: easy-fix: run integration tests like unit tests](https://github.com/walmartlabs/easy-fix "walmartlabs/easy-fix: easy-fix: run integration tests like unit tests")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## WebAssembly: birth of a virtual ISA (Ben Smith) - Full Stack Fest 2016 - YouTube
[www.youtube.com/watch?v=vmzz17JGPHI](https://www.youtube.com/watch?v=vmzz17JGPHI "WebAssembly: birth of a virtual ISA (Ben Smith) - Full Stack Fest 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">video</span></p>

WebAssemblyが何であって、何でないか。
歴史、asm.jsとの関係、コンパイル結果がどのような構造になってるかについての解説など

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Browser Bug Searcher
[browser-issue-tracker-search.appspot.com/](https://browser-issue-tracker-search.appspot.com/ "Browser Bug Searcher")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">issue</span> <span class="jser-tag">検索</span></p>

MSEdge、Firefox、Chrome、Opera、WebKitのIssue Trackerをまとめて検索できるサイト。
ブラウザのバグ検索エンジン

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## CSP Evaluator
[csp-evaluator.withgoogle.com/](https://csp-evaluator.withgoogle.com/ "CSP Evaluator")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">Tools</span></p>

CSPのポリシーディレクティブのチェックツール。
ポリシーの設定の構文エラー、設定の問題などを見つけてくれるツール

----

## jumpinjackie/jsdoc-typescript-plugin: JSDoc plugin to generate TypeScript definition files (.d.ts) from JSDoc-annotated source
[github.com/jumpinjackie/jsdoc-typescript-plugin](https://github.com/jumpinjackie/jsdoc-typescript-plugin "jumpinjackie/jsdoc-typescript-plugin: JSDoc plugin to generate TypeScript definition files (.d.ts) from JSDoc-annotated source")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSDoc</span> <span class="jser-tag">TypeScript</span></p>

JSDocからTypeScriptの型定義ファイルを生成するJSDoc plugin

----
<h1 class="site-genre">書籍関係</h1>

----

## Refactoring JavaScript - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920053262.do](http://shop.oreilly.com/product/0636920053262.do "Refactoring JavaScript - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年1月発売
JavaScriptのリファクタリングについての書籍

----
