---
title: "2018-01-09のJS: Spectre/Meltdownのブラウザへの影響、FuseBox 3.0、Nuxt.js 1.0"
author: "azu"
layout: post
date : 2018-01-09T23:13:18.624Z
category: JSer
tags:
- Security
- browser
- fusebox
- vue

---

JSer.info #365 - Googleの[Project Zero](https://googleprojectzero.blogspot.jp/2014/07/announcing-project-zero.html "Project Zero")チームより、投機的実行を利用したサイドチャネル攻撃に関する脆弱性として[Meltdown and Spectre](https://spectreattack.com/ "Meltdown and Spectre")が公開されました。


ブラウザは任意のJavaScriptを実行でき、かつ`SharedArrayBuffer`や`performance.now()`など精度の高いタイマーをもつためこのサイドチャネル攻撃の影響受けます。本来は、ブラウザは一種Sandbox内で任意のJavaScriptを独立して実行する仕組みを持ちSandbox外の状態は観測できません。しかし、[Spectre](https://spectreattack.com/ "Spectre")によってSandbox外の状態を観測できる可能性がでてきたためです。

そのためChrome、Firefox、MSEdge、Safariではそれぞれ一時的に[SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer "SharedArrayBuffer - JavaScript | MDN")の無効化、`performance.now()`の精度を下げる軽減策が導入されています。
([fantastictimers.pdf](https://gruss.cc/files/fantastictimers.pdf#page=10 "fantastictimers.pdf")では`SharedArrayBuffer`を高精度のタイマーとして使えることについて書かれています）

- [Actions required to mitigate Speculative Side-Channel Attack techniques - The Chromium Projects](https://sites.google.com/a/chromium.org/dev/Home/chromium-security/ssca)
- [Mitigations landing for new class of timing attack | Mozilla Security Blog](https://blog.mozilla.org/security/2018/01/03/mitigations-landing-new-class-timing-attack/)
- [Mitigating speculative execution side-channel attacks in Microsoft Edge and Internet Explorer - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2018/01/03/speculative-execution-mitigations-microsoft-edge-internet-explorer/#dvXo8lGoraWMULYx.97)
- [What Spectre and Meltdown Mean For WebKit | WebKit](https://webkit.org/blog/8048/what-spectre-and-meltdown-mean-for-webkit/)

どのブラウザも今回の変更は一時的な対策であるとして、`SharedArrayBuffer`については再度有効化する目標について書かれています。

関連: 高精度のタイマーを使ってのサイドチャネル攻撃について。

- [IAIK/ChromeZero: Google Chrome extension implementing JavaScript Zero](https://github.com/IAIK/ChromeZero)
- [jszero.pdf](https://misc0110.net/web/files/jszero.pdf)
- [fantastictimers.pdf](https://gruss.cc/files/fantastictimers.pdf#page=10)
- [ecmascript_sharedmem/TimingAttack.md at master · tc39/ecmascript_sharedmem](https://github.com/tc39/ecmascript_sharedmem/blob/master/issues/TimingAttack.md "ecmascript_sharedmem/TimingAttack.md at master · tc39/ecmascript_sharedmem")
- [Flush+Reload](https://eprint.iacr.org/2013/448.pdf "Flush+Reload")
- [sec15-paper-gruss.pdf](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-gruss.pdf "sec15-paper-gruss.pdf")


----

BundlerかつTask Runnerである[FuseBox](https://github.com/fuse-box/fuse-box "FuseBox") 3.0がリリースされました。

- [FuseBox 3.0 — faster than ever – fusebox – Medium](https://medium.com/fusebox/fusebox-3-0-faster-than-ever-5fae4254556c "FuseBox 3.0 — faster than ever – fusebox – Medium")
- [fuse-box/version3changelog.md at master · fuse-box/fuse-box](https://github.com/fuse-box/fuse-box/blob/master/docs/version3changelog.md "fuse-box/version3changelog.md at master · fuse-box/fuse-box")


Code Splittingをデフォルトでサポート、TypeScriptをソースにTree Shakingをサポートするために`ts:main`のサポート。
パフォーマンスの改善、ウェブサイトのデザイン更新などが行われています。

----

Vue版Next.jsであるNuxt.js 1.0がリリースされました。

- [Nuxt.js 1.0 is out 🎉 – Nuxt.js – Medium](https://medium.com/@nuxt_js/nuxt-js-1-0-is-out-bab1af459972 "Nuxt.js 1.0 is out 🎉 – Nuxt.js – Medium")

Node.js 8.0.0未満のサポートを終了。
今後はドキュメンテーション、パフォーマンス、TypeScriptサポートの改善などを行っていくロードマップについて書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v8.9.4 (LTS) | Node.js
[nodejs.org/en/blog/release/v8.9.4/](https://nodejs.org/en/blog/release/v8.9.4/ "Node v8.9.4 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 8.9.4リリース。
npm 5.6.0の同梱など

- [The npm Blog — v5.6.0 (2017-11-27)](http://blog.npmjs.org/post/167963735925/v560-2017-11-27 "The npm Blog — v5.6.0 (2017-11-27)")

----

## Actions Required to Mitigate Speculative Side-Channel Attack Techniques - The Chromium Projects
[sites.google.com/a/chromium.org/dev/Home/chromium-security/ssca](https://sites.google.com/a/chromium.org/dev/Home/chromium-security/ssca "Actions Required to Mitigate Speculative Side-Channel Attack Techniques - The Chromium Projects")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">news</span> <span class="jser-tag">browser</span></p>

Chrome、Firefox、MSEdge、SafariなどのブラウザはMeltdown/Spectre(CPUプロセッサに関する脆弱性)を受ける。
そのためSharedArrayBufferの無効化や軽減策として`performance.now()`などの挙動を変更する

- [Mitigations landing for new class of timing attack | Mozilla Security Blog](https://blog.mozilla.org/security/2018/01/03/mitigations-landing-new-class-timing-attack/ "Mitigations landing for new class of timing attack | Mozilla Security Blog")
- [Meltdown and Spectre](https://spectreattack.com/ "Meltdown and Spectre")
- [Mitigating speculative execution side-channel attacks in Microsoft Edge and Internet Explorer - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2018/01/03/speculative-execution-mitigations-microsoft-edge-internet-explorer/#m2GyZlsjAzq0Do6K.97 "Mitigating speculative execution side-channel attacks in Microsoft Edge and Internet Explorer - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
- [What Spectre and Meltdown Mean For WebKit | WebKit](https://webkit.org/blog/8048/what-spectre-and-meltdown-mean-for-webkit/ "What Spectre and Meltdown Mean For WebKit | WebKit")

----

## browserify/changelog.markdown at v15.0.0 · browserify/browserify
[github.com/browserify/browserify/blob/v15.0.0/changelog.markdown](https://github.com/browserify/browserify/blob/v15.0.0/changelog.markdown "browserify/changelog.markdown at v15.0.0 · browserify/browserify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 15.0.0リリース。
Node.js 4未満のサポート終了、`module-deps`の依存を更新、`browserify` organizationに移動など

- [Release v5.0.0 · browserify/module-deps](https://github.com/browserify/module-deps/releases/tag/v5.0.0 "Release v5.0.0 · browserify/module-deps")

----

## Dev.Opera — What’s new in Chromium 63 and Opera 50
[dev.opera.com/blog/opera-50/](https://dev.opera.com/blog/opera-50/ "Dev.Opera — What’s new in Chromium 63 and Opera 50")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 50 (based on Chromium 63)リリース。
Dynamic import、Async Iterator/Generator、`Promise#finally`、`Intl.PluralRules`のサポートなど


----

## ESLint v4.15.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/01/eslint-v4.15.0-released](https://eslint.org/blog/2018/01/eslint-v4.15.0-released "ESLint v4.15.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.15.0リリース。
`CLIEngine#getRules()`で設定されたルールの取得、`messageId`の追加など開発者向けの機能追加など

- [ESLint v4.15.0 - Qiita](https://qiita.com/mysticatea/items/c6c10d4749e7d69d321e "ESLint v4.15.0 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## ECMAScript 2015以降のJavaScriptの\`this\`を理解する | Web Scratch
[efcl.info/2018/01/04/what-is-this/](http://efcl.info/2018/01/04/what-is-this/ "ECMAScript 2015以降のJavaScriptの\`this\`を理解する | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

JavaScriptの`this`についての解説記事。
状況によって異なる値を参照する`this`は、どのような仕組みでその値を決まっているかについて。
関数やArrow Functionでの仕組みの違いなどについて

- [asciidwango/js-primer: JavaScriptの入門書](https://github.com/asciidwango/js-primer "asciidwango/js-primer: JavaScriptの入門書")

----

## FuseBox 3.0 — faster than ever – fusebox – Medium
[medium.com/fusebox/fusebox-3-0-faster-than-ever-5fae4254556c](https://medium.com/fusebox/fusebox-3-0-faster-than-ever-5fae4254556c "FuseBox 3.0 — faster than ever – fusebox – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

FuseBox 3.0リリース。
Code Splittingをデフォルトでサポート、TypeScriptをソースにTree Shakingをサポートするために`ts:main`のサポート。
パフォーマンスの改善、ウェブサイトのデザイン更新など

- [Release 3.0.2 · fuse-box/fuse-box](https://github.com/fuse-box/fuse-box/releases/tag/3.0.2 "Release 3.0.2 · fuse-box/fuse-box")
- [fuse-box/version3changelog.md at master · fuse-box/fuse-box](https://github.com/fuse-box/fuse-box/blob/master/docs/version3changelog.md "fuse-box/version3changelog.md at master · fuse-box/fuse-box")

----

## New flexbox guides on MDN – Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2018/01/new-flexbox-guides-on-mdn/](https://hacks.mozilla.org/2018/01/new-flexbox-guides-on-mdn/ "New flexbox guides on MDN – Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">document</span></p>

FlexboxのガイドがMDNに追加された


----

## 🐛🔨 The Contributors Guide to webpack — Part 1 🎨 🖼
[medium.com/webpack/the-contributors-guide-to-webpack-part-1-a0410cc82ca4](https://medium.com/webpack/the-contributors-guide-to-webpack-part-1-a0410cc82ca4 "🐛🔨 The Contributors Guide to webpack — Part 1 🎨 🖼")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

webpackのアーキテクチャの解説をする連載。
webpack関係のツール、プラグインのエコシステムや動作の仕組み、モジュール依存関係グラフの構築などについて

- [TheLarkInn/artsy-webpack-tour: Annotations on webpack source code in a pseudo-guided fashion.](https://github.com/TheLarkInn/artsy-webpack-tour "TheLarkInn/artsy-webpack-tour: Annotations on webpack source code in a pseudo-guided fashion.")

----

## Using React Fragments for the first time
[javascriptplayground.com/react-fragments/](https://javascriptplayground.com/react-fragments/ "Using React Fragments for the first time")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16で導入されたFragmentについての記事。
どのような問題を解決するのかや気をつけるべき点、ユースケースについて


----

## What’s New in HTML 5.2?
[bitsofco.de/whats-new-in-html-5-2/](https://bitsofco.de/whats-new-in-html-5-2/ "What’s New in HTML 5.2?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">HTML</span> <span class="jser-tag">spec</span> <span class="jser-tag">article</span></p>

W3C HTML 5.2の変更点まとめ。
`<dialog>`要素、iframeに`allowpaymentrequest`属性の追加、`<main>`要素の複数配置の許容。
また`keygen`、`menu`、`menuitem`の削除、HTML4 XHTML1 strict doctypeの削除など

- [HTML 5.2: Changes](https://www.w3.org/TR/html52/changes.html#changes "HTML 5.2: Changes")
- [main要素、二つの定義 | フロントエンドBlog | ミツエーリンクス](https://www.mitsue.co.jp/knowledge/blog/frontend/201412/02_1454.html "main要素、二つの定義 | フロントエンドBlog | ミツエーリンクス")
- [メモ：両HTMLにおけるmain要素の説明、ついに一定の収束の気配か。 - 水底の血](http://momdo.hatenablog.jp/entry/20180105/1515161004 "メモ：両HTMLにおけるmain要素の説明、ついに一定の収束の気配か。 - 水底の血")

----

## JavaScript Start-up Optimization  |  Web Fundamentals  |  Google Developers
[developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/javascript-startup-optimization/](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/javascript-startup-optimization/ "JavaScript Start-up Optimization  |  Web Fundamentals  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ウェブサイトの起動速度周りの改善ポイントについてまとめた記事。
ネットワーク、ファイルサイズ、パース、コンパイル、実行コストについてを簡単にまとめたもの

- [JavaScript Start-up Performance – reloading – Medium](https://medium.com/reloading/javascript-start-up-performance-69200f43b201 "JavaScript Start-up Performance – reloading – Medium")

----

## Nuxt.js 1.0 is out 🎉 – Nuxt.js – Medium
[medium.com/@nuxt\_js/nuxt-js-1-0-is-out-bab1af459972](https://medium.com/@nuxt_js/nuxt-js-1-0-is-out-bab1af459972 "Nuxt.js 1.0 is out 🎉 – Nuxt.js – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">server</span> <span class="jser-tag">ReleaseNote</span></p>

Vue版Next.jsであるNuxt.js 1.0リリース。
Node.js 8.0.0未満のサポートを終了。
今後はドキュメンテーション、パフォーマンス、TypeScriptサポートの改善などを行っていく

- [Release v1.0.0 · nuxt/nuxt.js](https://github.com/nuxt/nuxt.js/releases/tag/v1.0.0 "Release v1.0.0 · nuxt/nuxt.js")

----

## Sapper: Towards the ideal web app framework
[svelte.technology/blog/sapper-towards-the-ideal-web-app-framework](https://svelte.technology/blog/sapper-towards-the-ideal-web-app-framework "Sapper: Towards the ideal web app framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

SvelteベースのNext.js的なフレームワークであるSapperについて。
それぞれのページがSvelteのコンポーネントとなる。
元々フレームワークからではなくコンパイラとして始まったSvelteと他のフレームワークとの違いについて

- [Sapper • Military-grade progressive web apps, powered by Svelte](https://sapper.svelte.technology/ "Sapper • Military-grade progressive web apps, powered by Svelte")

----

## The State of JavaScript Frameworks, 2017 | Part 1: Front-End Frameworks
[www.npmjs.com/npm/state-of-javascript-frameworks-2017-part-1](https://www.npmjs.com/npm/state-of-javascript-frameworks-2017-part-1 "The State of JavaScript Frameworks, 2017 | Part 1: Front-End Frameworks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

npmのダウンロード数から見るJavaScriptのエコシステムについての連載記事。
フロントエンドとバックエンドのフレームワーク、Reactに関するエコシステムについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Chrome DevTools 101: Debugging JavaScript - YouTube
[www.youtube.com/watch?v&#x3D;H0XScE08hy8](https://www.youtube.com/watch?v=H0XScE08hy8 "Chrome DevTools 101: Debugging JavaScript - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">video</span></p>

Chrome開発者ツールでのデバッガーの使い方についての動画。
ブレークポイントの種類や貼り方、ステップ実行などについて

- [Pause Your Code With Breakpoints  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/javascript/breakpoints "Pause Your Code With Breakpoints  |  Tools for Web Developers  |  Google Developers")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Roadmap of Web Applications on Mobile
[www.w3.org/2018/01/web-roadmaps/mobile/](https://www.w3.org/2018/01/web-roadmaps/mobile/ "Roadmap of Web Applications on Mobile")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">spec</span> <span class="jser-tag">document</span></p>

W3Cのモバイルのウェブアプリに関する仕様のロードマップ。
それぞれの仕様のジャンルごとのまとめ、ステータス、実装状況について


----

## Lighthouse 2.7 Updates  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/01/lighthouse](https://developers.google.com/web/updates/2018/01/lighthouse "Lighthouse 2.7 Updates  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Lighthouse 2.7リリース。
SEO auditの追加、手動のアクセシビリティチェックリストの追加、WebP auditの更新など


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mweststrate/immer: Create the next immutable state by mutating the current one
[github.com/mweststrate/immer](https://github.com/mweststrate/immer "mweststrate/immer: Create the next immutable state by mutating the current one")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

MutableなAPIでImmutableにオブジェクトや配列を変更できるライブラリ。


----
