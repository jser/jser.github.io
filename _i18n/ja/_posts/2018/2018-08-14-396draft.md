---
title: "2018-08-13のJS: sonarwhal to webhint、Dart 2、Vue CLI 3"
author: "azu"
layout: post
date : 2018-08-13T12:22:03.816Z
category: JSer
tags:
- webhint
- dart
- vue

---

JSer.info #396 - sonarはESLintのようにプラグインで拡張できるウェブサイトのLintツールでした。

- [sonar - JS Foundation Welcomes Newest Project - JS Foundation](https://js.foundation/announcements/2017/06/22/sonar-js-foundation-welcomes-newest-project)

[名前の競合するツール](https://code.fb.com/android/open-sourcing-sonar-a-new-extensible-debugging-tool-2/)や[サービス](https://www.sonarsource.com/)もあり、`webhint`へ名前を変更することを決定しました。
(今もウェブサイトは名前の移行中なので古いドキュメントが残っています)

- [webhint: a hinting engine for the web – webhint – Medium](https://medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9)
- [webhintio/hint: 💡 A hinting engine for the web](https://github.com/webhintio/hint)

名前の変更と合わせてwebhint 3.0がリリースされ、パフォーマンス改善や`npm create hintrc`で設定ファイルを作成できるようになるなどの機能が追加されています。

----

Dart 2の安定版が公開されました。

- [Dart 2 | Dart](https://www.dartlang.org/dart-2)
- [Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium](https://medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7)

[Flutter](https://flutter.io/)ではすでにDart 2のプレリリースバージョンが使われていましたが、Dart 2にあわせて[AngularDart 5.0](https://webdev.dartlang.org/angular)もリリースされています。

----

[Vue CLI](https://cli.vuejs.org/) 3.0がリリースされています。

- [Vue CLI 3.0 is here! – The Vue Point – Medium](https://medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb)

Vue CLI 3.0はこれまでのScaffolding ToolであったCLIが書き直されたバージョンでリッチな機能を多くもっています。
webpackを使ったビルドや[Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/)の対応、プラグインシステム、GUIで操作できるダッシュボード、開発サーバ、ビルドをES2015対応ブラウザ向けに最適化するModern Modeなど機能を持っています。

また、デフォルトではwebpackは設定済みですが、ejectしなくてもwebpackなどの設定を変更できるように[webpack-chain](https://github.com/mozilla-neutrino/webpack-chain)などの仕組みが取り入れられています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## webhint: a hinting engine for the web – webhint – Medium
[medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9](https://medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9 "webhint: a hinting engine for the web – webhint – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

webhint(sonarwhal)のリリース。
sonarwhalからwebhintへ名前の変更、起動時間の改善、`npm create hintrc`で設定ファイルを作成できるようになるなど


----

## V8 JavaScript Engine: V8 release v6.9
[v8project.blogspot.com/2018/08/v8-release-69.html](https://v8project.blogspot.com/2018/08/v8-release-69.html "V8 JavaScript Engine: V8 release v6.9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.9リリース。
メモリ使用量の削減、WebAssemblyコンパイラの起動速度などの改善、DataViewの速度改善など


----

## Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium
[medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7](https://medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7 "Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart 2リリース。

- [Dart 2 | Dart](https://www.dartlang.org/dart-2 "Dart 2 | Dart")

----

## Release v3.0.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v3.0.0](https://github.com/lerna/lerna/releases/tag/v3.0.0 "Release v3.0.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

monorepo管理ツールのlerna 3.0.0リリース。
`lerna publish`と`lerna version`コマンドに分離、`lerna changed`の追加。
`lerna publish`時に自動的にGitへ`--no-verify`を渡すのをやめ`--commit-hook`オプションを追加、lerna自身をmonorepoで管理するようになるなど


----

## Release v3.0.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v3.0.0](https://github.com/karma-runner/karma/releases/tag/v3.0.0 "Release v3.0.0 · karma-runner/karma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma 3.0.0リリース。
デフォルトのタイムアウト時間の変更、`karma init`で`ChromeHeadless`を選択できるようになるなど


----

## Vue CLI 3.0 is here! – The Vue Point – Medium
[medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb](https://medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb "Vue CLI 3.0 is here! – The Vue Point – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vue CLI 3.0リリース。
CLIが書き直されたバージョンでリッチな機能を多くもつ。
ejectしなくてもwebpackなどをカスタマイズできるように、プラグインシステム、ダッシュボードのGUI、開発サーバ、ビルドやModern Modeについてなど

- [mozilla-neutrino/webpack-chain: A chaining API to generate and simplify the modification of Webpack configurations.](https://github.com/mozilla-neutrino/webpack-chain "mozilla-neutrino/webpack-chain: A chaining API to generate and simplify the modification of Webpack configurations.")

----

## Release v7.0.0-rc.0 · babel/babel
[github.com/babel/babel/releases/tag/v7.0.0-rc.0](https://github.com/babel/babel/releases/tag/v7.0.0-rc.0 "Release v7.0.0-rc.0 · babel/babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7 RCリリース。


----
<h1 class="site-genre">アーティクル</h1>

----

## AngularJSのリプレースにAngularを選んだ話 - BizReach Tech Blog
[tech.bizreach.co.jp/posts/51/angular-upgrade/](https://tech.bizreach.co.jp/posts/51/angular-upgrade/ "AngularJSのリプレースにAngularを選んだ話 - BizReach Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

AngularJS(1.x)で書かれたページをパフォーマンスと将来性の問題からAngular(2以降)に移行した話。
複数のアプリに対応できるようにUIコンポーネントをライブラリ化、Atomic Components、standard-versionを使ったバージョン管理についてなど

- [大規模Angular SPA開発に立ち向かうためにアプリとUIを切り分けた話 - BizReach Tech Blog](https://tech.bizreach.co.jp/posts/204/angular-upgrade-second/ "大規模Angular SPA開発に立ち向かうためにアプリとUIを切り分けた話 - BizReach Tech Blog")

----

## Introducing Electron Fiddle – Felix Rieseberg – Medium
[medium.com/@felixrieseberg/introducing-electron-fiddle-1de2be1ba6e7](https://medium.com/@felixrieseberg/introducing-electron-fiddle-1de2be1ba6e7 "Introducing Electron Fiddle – Felix Rieseberg – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">article</span> <span class="jser-tag">software</span> <span class="jser-tag">editor</span></p>

ElectronアプリをJSFiddleのようなプレイグラウンドで開発できるアプリ。
エディタにコードを書いてElectronアプリを実行したり、コードをgistに共有したり、アプリのパッケージ化できる

- [electron/fiddle: 🚀 The easiest way to get started with Electron](https://github.com/electron/fiddle "electron/fiddle: 🚀 The easiest way to get started with Electron")


----

## Variable Scope in Modern JavaScript with var, let and const | Andy Carter
[andy-carter.com/blog/variable-scope-in-modern-javascript](https://andy-carter.com/blog/variable-scope-in-modern-javascript "Variable Scope in Modern JavaScript with var, let and const | Andy Carter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`var`、`let`、`const`の変数のスコープについて解説している記事。

- [関数とスコープ · JavaScriptの入門書 #jsprimer](https://asciidwango.github.io/js-primer/basic/function-scope/ "関数とスコープ · JavaScriptの入門書 #jsprimer")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## NaturalIntelligence/fast-xml-parser: Validate XML, Parse XML to JS/JSON and vise versa, or parse XML to Nimn rapidly without C/C++ based libraries and no callback
[github.com/NaturalIntelligence/fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser "NaturalIntelligence/fast-xml-parser: Validate XML, Parse XML to JS/JSON and vise versa, or parse XML to Nimn rapidly without C/C++ based libraries and no callback")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">XML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Pure JavaScriptなXML to JSON、JSON to XMLの変換ライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## Introduction · Human Redux
[read.reduxbook.com/](https://read.reduxbook.com/ "Introduction · Human Redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">book</span></p>

Reduxについての書籍。
Reduxの使い方、Selector、ルーティング、非同期処理やエラー処理、Redux Bundlerなどについて


----

## JavaScript for impatient programmers
[exploringjs.com/impatient-js/](http://exploringjs.com/impatient-js/ "JavaScript for impatient programmers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptの文法や機能についてのJavaScript初心者向けの書籍。
各章ごとにエクササイズが用意されており、ES2018を含む主要な機能を一覧的に学べる書籍。


----

## React Native+Expoではじめるスマホアプリ開発 ~JavaScriptによるアプリ構築の実際~ | 松澤 太郎 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4839966648/](https://www.amazon.co.jp/dp/4839966648/ "React Native+Expoではじめるスマホアプリ開発 ~JavaScriptによるアプリ構築の実際~ | 松澤 太郎 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span> <span class="jser-tag">ios</span> <span class="jser-tag">Android</span></p>

2018年8月29日発売
React Nativeでのアプリ開発についての書籍。


----
