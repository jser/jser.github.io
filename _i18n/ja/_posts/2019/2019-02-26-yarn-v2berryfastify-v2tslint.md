---
title: "2019-02-26のJS: yarn v2候補(berry)、Fastify v2、TSLintの今後"
author: "azu"
layout: post
date : 2019-02-26T02:02:23.716Z
category: JSer
tags:
- yarn
- node
- typescript
- eslint
- tslint

---

JSer.info #424 - [yarn](https://yarnpkg.com/) v2のソースコードとなりリポジトリが公開されています。

- [yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization](https://github.com/yarnpkg/berry)

次のIssueでも書かれているように、v1とは別のリポジトリにしているのはIssueのtriageをしやすくするためだそうです。

> The codename for these changes is Berry
> -- https://github.com/yarnpkg/yarn/issues/6953

"Berry"という名前はv2に向けた変更のコードネームです。

- [👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry](https://github.com/yarnpkg/berry/issues/1 "👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry")
- [Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn](https://github.com/yarnpkg/yarn/issues/6953#issuecomment-466589196 "Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn")

v2(berry)では[Yarn's Future - v2 and beyond](https://github.com/yarnpkg/yarn/issues/6953)で予定されていたものが実装されている段階のようです。

コードベースがTypeScriptで書き直されていて、monorepoになっています。
lockファイルをymlサブセットとなるような[syml](https://github.com/yarnpkg/berry/blob/master/packages/berry-parsers/sources/syml.ts)というフォーマットを作り実装しています。また、プラグインの仕組みが追加され、PnPやnpm(`package-lock.json`を扱う)などの処理はプラグインとして実装されています。
また、ワークスペースの改善として[Constraints](https://github.com/yarnpkg/berry/blob/master/docs/workspaces-constraints.md)というProlog(実際には[tau-prolog](https://github.com/jariazavalverde/tau-prolog))を使った制約を扱う[プラグイン](https://github.com/yarnpkg/berry/tree/master/packages/plugin-constraints)が追加されています。ワークスペース間の依存などのルールをPrologを使って記述して、より効率的に扱えるようにするのが目的のようです。

興味がある人は[Install](https://github.com/yarnpkg/berry#install)して試したり、[Issue](https://github.com/yarnpkg/berry/issues)を見てみると良いかもしれません。

----

[TypeScriptの2019 Juneロードマップ](https://github.com/Microsoft/TypeScript/issues/29288)でTSLintではなくESLintのサポートを強化していくという話が行われ、[typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)というプロジェクトが作成され[ESLintチームと協力](https://eslint.org/blog/2019/01/future-typescript-eslint)していくことが発表されていました。

このような背景もあり、TSLintのメンテナーからTSLintの今後について記事が公開されています。

- [TSLint in 2019 – Palantir Blog – Medium](https://medium.com/palantir/tslint-in-2019-1a144c2317a9 "TSLint in 2019 – Palantir Blog – Medium")
- [Roadmap: TSLint -> ESLint · Issue #4534 · palantir/tslint](https://github.com/palantir/tslint/issues/4534 "Roadmap: TSLint -> ESLint · Issue #4534 · palantir/tslint")

TSLintは2019年中には非推奨となり(今すぐではないです)、今後はESLintへの移行パスを整備していくという話が書かれています。
[typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)(ESLintのTypeScript対応)は開発途中であるため、TSLintとの互換となるようなルールがない部分もあります。そのため、TSLint自体はまだしばらくはメンテンスを続けていくという方針についても書かれています。

現状の[typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)の動作については、次の記事も参照して見てください。

- [@typescript-eslint ことはじめ - teppeis blog](https://teppeis.hatenablog.com/entry/2019/02/typescript-eslint)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Version 3.5.0 · knockout/knockout
[github.com/knockout/knockout/releases/tag/v3.5.0](https://github.com/knockout/knockout/releases/tag/v3.5.0 "Release Version 3.5.0 · knockout/knockout")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout 3.5.0リリース。
`foreach`バインディングの挙動の変更とパフォーマンスの改善、`ko.when`がPromiseを返すようになるなど


----

## Release: npm@6.9.0-next.0 - 📣 announcements - npm forum
[npm.community/t/release-npm-6-9-0-next-0/5553](https://npm.community/t/release-npm-6-9-0-next-0/5553 "Release: npm@6.9.0-next.0 - 📣 announcements - npm forum")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.9.0-next.0リリース。
パッケージに別名をつけることができるpackage alias機能をサポート、`--before`オプションをサポートなど

- [install: add support for package aliases by zkat · Pull Request #3 · npm/cli](https://github.com/npm/cli/pull/3 "install: add support for package aliases by zkat · Pull Request #3 · npm/cli")

----

## The npm Blog — Managing JavaScript in the Enterprise
[blog.npmjs.org/post/182958759735/managing-javascript-in-the-enterprise](https://blog.npmjs.org/post/182958759735/managing-javascript-in-the-enterprise "The npm Blog — Managing JavaScript in the Enterprise")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">news</span></p>

npm Enterpriseの正式リリース。
SSO認証の対応やprivate registryのサポートなど

- [npm | Enterprise](https://www.npmjs.com/products/enterprise "npm | Enterprise")

----

## dsherret/conditional-type-checks: Types for testing TypeScript types.
[github.com/dsherret/conditional-type-checks](https://github.com/dsherret/conditional-type-checks "dsherret/conditional-type-checks: Types for testing TypeScript types.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

Conditional Typeを使いTypeScriptの型Assertionを行うライブラリ


----

## Fastify v2.0.0 is here – Fastify – Medium
[medium.com/@fastifyjs/fastify-v2-0-0-is-here-8275d613fba4](https://medium.com/@fastifyjs/fastify-v2-0-0-is-here-8275d613fba4 "Fastify v2.0.0 is here – Fastify – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">server</span></p>

Node.jsフレームワークのFastify 2.0.0リリース。
`onError`、`preParsing`、`preSerialization`、`preValidation` hookの追加。
pluginのロードのタイムアウトを設定、シグネチャの一貫性の修正など

- [Release v2.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v2.0.0 "Release v2.0.0 · fastify/fastify")

----

## yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization
[github.com/yarnpkg/berry](https://github.com/yarnpkg/berry "yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">news</span></p>

yarn v2となるソースコードのリポジトリが公開された。
v1のリポジトリと分けているのは、issueをハンドリングしやすくするため。
現在はロードマップに予定した機能はある程度実装された状態で、一部の機能やドキュメントが足りていない状況。

- [Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn](https://github.com/yarnpkg/yarn/issues/6953#issuecomment-466589196 "Yarn&#x27;s Future - v2 and beyond · Issue #6953 · yarnpkg/yarn")
- [👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry](https://github.com/yarnpkg/berry/issues/1 "👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry")

----
<h1 class="site-genre">アーティクル</h1>

----

## AddyOsmani.com - JavaScript Loading Priorities in Chrome
[addyosmani.com/blog/script-priorities/](https://addyosmani.com/blog/script-priorities/ "AddyOsmani.com - JavaScript Loading Priorities in Chrome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

link rel=preloadとscript要素の defer/async属性を組み合わせ際のLoadingやExecution Priorityについてまとめた記事


----

## How @supports Works | CSS-Tricks
[css-tricks.com/how-supports-works/](https://css-tricks.com/how-supports-works/ "How @supports Works | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSの`@supports`の使い方やユースケースについて。
また、JavaScriptからのCSS Supportsを使ったFeature Detectについて


----

## Intelligent Tracking Prevention 2.1 | WebKit
[webkit.org/blog/8613/intelligent-tracking-prevention-2-1/](https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/ "Intelligent Tracking Prevention 2.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Safari 12.1で導入されるITP 2.1について。 Partitioned Cookiesのサポート終了、document.cookieで作成したクッキーは生存期間が7日間のcapがつくように、DNTの削除など


----

## TSLint in 2019 – Palantir Blog – Medium
[medium.com/palantir/tslint-in-2019-1a144c2317a9](https://medium.com/palantir/tslint-in-2019-1a144c2317a9 "TSLint in 2019 – Palantir Blog – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">Tools</span></p>

TSLintの今後について。
今後TSLintは非推奨となり、TSLintからESLintへの移行パスを整備していくという話


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## React – A JavaScript library for building user interfaces
[ja.reactjs.org/](https://ja.reactjs.org/ "React – A JavaScript library for building user interfaces")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">翻訳</span></p>

Reactサイトの日本語訳

- [Is React Translated Yet? ¡Sí! Sim! はい！ – React Blog](https://reactjs.org/blog/2019/02/23/is-react-translated-yet.html "Is React Translated Yet? ¡Sí! Sim! はい！ – React Blog")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## patr0nus/DeskGap: A cross-platform desktop app framework based on Node.js and the system webview
[github.com/patr0nus/DeskGap/](https://github.com/patr0nus/DeskGap/ "patr0nus/DeskGap: A cross-platform desktop app framework based on Node.js and the system webview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">mac</span> <span class="jser-tag">windows</span> <span class="jser-tag">Electron</span></p>

OSのWebViewの仕組みを利用したElectronライクなデスクトップアプリ作成フレームワーク。
Chromiumなどをbundleしないが、Node.jsをbundleしている。
フレームワーク上では制限されたElectronライクなAPIとNode.jsの機能が利用できる。


----

## klaussinani/qoa: 💬 Minimal interactive command-line prompts
[github.com/klaussinani/qoa](https://github.com/klaussinani/qoa "klaussinani/qoa: 💬 Minimal interactive command-line prompts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span> <span class="jser-tag">UI</span></p>

ターミナルで対話的なインタフェースを提供するNode.jsライブラリ。
Confirm、Quiz、Secure Promptなど


----

## jariazavalverde/tau-prolog: An open source Prolog interpreter in JavaScript
[github.com/jariazavalverde/tau-prolog](https://github.com/jariazavalverde/tau-prolog "jariazavalverde/tau-prolog: An open source Prolog interpreter in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">library</span></p>

PrologインタプリタのJavaScript実装


----

## fagbokforlaget/simple-fs: Handles files on indexeddb like you would do in node.js (promise)
[github.com/fagbokforlaget/simple-fs](https://github.com/fagbokforlaget/simple-fs "fagbokforlaget/simple-fs: Handles files on indexeddb like you would do in node.js (promise)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

IndexedDBを使ったファイルシステムライクなAPIを持ったブラウザ向けライブラリ


----

## namics/webpack-config-plugins: Provide best practices for webpack loader configurations
[github.com/namics/webpack-config-plugins](https://github.com/namics/webpack-config-plugins "namics/webpack-config-plugins: Provide best practices for webpack loader configurations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">設定</span></p>

webpackのloader設定をまとめたプラグイン。
Babel、TypeScript、Sass、Font、Imageなどのビルドを行うプラグインが用意されている


----
