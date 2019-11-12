---
title: "2019-11-12のJS: TypeScript 3.7正式リリース、Babel 7.7.0、npmロードマップ、Web Almanac"
author: "azu"
layout: post
date : 2019-11-12T02:09:19.069Z
category: JSer
tags:
- TypeScript
- Babel
- npm
- book

---

JSer.info #461 - TypeScript 3.7の正式版がリリースされました。

- [Announcing TypeScript 3.7 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7/)
- [TypeScript 3.7 · TypeScript](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html)
- [TypeScript v3.7.2 変更点 - Qiita](https://qiita.com/vvakame/items/60d8d43ded0b160a99cc)

Playgroundで更新内容を確認できるようになり、新しく増えた構文などのサンプルコードが確認できるようになっています。

- <https://www.typescriptlang.org/play/index.html?#show-whatisnew>

構文として新しい増えているため、TypeScriptをサポートしているツールチェイン周りもアップデートが必要になります。
ECMASCript Proposal(Stage 3)の[Optional Chaining](https://github.com/tc39/proposal-optional-chaining)と[Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing)のサポートが追加されました。
Assertion Functionsで`asserts <expr>`を返り値の型として書けるようになっています。
これにあわせて`never`型を返す関数の型推論の改善されています。

その他の変更として、型エラーがネストさしてる際のエラー表示の改善、`@ts-nockeck`をtsファイルでサポート、`--declaration`と`--allowJs`を組みあせて利用できるようなっています。
また、ECMAScriptの仕様に準拠するために試験的な機能として`useDefineForClassFields`のフラグが追加されています。
これによってクラスフィールドの出力コードがより仕様に合わせた形なり、またクラスフィールドに`declare` modifierを利用できるようになります。

----

Babel 7.7.0がリリースされました。

- [7.7.0 Released: Error recovery and TypeScript 3.7 · Babel](https://babeljs.io/blog/2019/11/05/7.7.0)

Top-Level `await`のパースをサポート、TypeScript 3.7サポートが行われています。
また、パースエラーでも結果のASTとエラーを返せる`errorRecovery`オプションの追加、`babel.config.json`や`.babelrc.cjs`を設定ファイルとして認識するようになっています。
その他の変更として、`@babel/react`でJSX内でのSpread構文を展開せずにSpread構文のまま出力できる`useSpread`オプションの追加やメモリ消費量の改善など行われています。

----

npm 6.13.0のリリースに合わせて、今後のnpmのロードマップについて書かれた記事が公開されいます。

- [Release v6.13.0 · npm/cli](https://github.com/npm/cli/releases/tag/v6.13.0)
- [The npm Blog — Updates to Community, Docs & more...](https://blog.npmjs.org/post/188841555980/updates-to-community-docs-more)

npm 6.13.0では`package.json`に書かれた`funding`フィールドをサポートするようになっています。
これにあわせてインストール済みのパッケージの`funding`フィールドをリストできる`npm fund`コマンドが追加されています。

- [rfcs/0017-add-funding-support.md at latest · npm/rfcs](https://github.com/npm/rfcs/blob/latest/accepted/0017-add-funding-support.md)

また、npm install時にfunding通知と`--no-fund`での通知のオプトアウトが実装されています。
これまでは、各パッケージでfunding通知が実装されていたため、これの標準化をしてユーザーがコントロールできるようにする目的です。

その他にも[npmのフォーラム](https://npm.community/)はアーカイブ化しバグ関係の管理はGitHub Issuesに再び移動され、
RFCについてOpenにミーティングする場を設け、[GitHub Project](https://github.com/orgs/npm/projects/7)でのステータスの公開などの取り組みも行われいます。

- [Open RFC Meeting - Wednesday, Sept 4th @ 12:00pm EST · Issue #49 · npm/rfcs](https://github.com/npm/rfcs/issues/49)

記事ではnpm v7での変更予定についても書かれています。
npm v7の変更予定としてパフォーマンスの改善、GitHubのPRからのインストールのサポート、Node 6と8のサポート終了、peerDependenciesをデフォルトでインストールするなどの変更が予定されています。

年末ぐらいにはベータリリースして試せるようになる予定とのことです。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 3.7 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-7/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7/ "Announcing TypeScript 3.7 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.7リリース。
Playgroundで更新内容を確認できるようになった。
Optional Chainig、Nullish Coalescing、Assertion Functionsのサポート、エラーレポートの改善、`@ts-nockeck`をtsファイルでサポートなど。
`never`型のコントールフロー改善、`--declaration`と`--allowJs`を組みあせて利用できるように.
`useDefineForClassFields`のフラグ付きでクラスフィールドに`declare`を利用できるように、


----

## Prettier 1.19: Long awaited Vue option, TypeScript 3.7 and new JavaScript features · Prettier
[prettier.io/blog/2019/11/09/1.19.0.html](https://prettier.io/blog/2019/11/09/1.19.0.html "Prettier 1.19: Long awaited Vue option, TypeScript 3.7 and new JavaScript features · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 1.19リリース。
`--vue-indent-script-and-style`オプションの追加、TypeScript 3.7のサポート、ES Proposalのpartial application構文のサポートなど。


----

## 7.7.0 Released: Error recovery and TypeScript 3.7 · Babel
[babeljs.io/blog/2019/11/05/7.7.0](https://babeljs.io/blog/2019/11/05/7.7.0 "7.7.0 Released: Error recovery and TypeScript 3.7 · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7.7.0リリース。
Top-Level `await`のサポート、TypeScript 3.7サポート。
パースエラーでも結果のASTとエラーを返せる`errorRecovery`オプションの追加、`.babelrc.cjs`を設定ファイルとして認識するように、メモリ消費量の改善など


----

## Release v6.13.0 · npm/cli
[github.com/npm/cli/releases/tag/v6.13.0](https://github.com/npm/cli/releases/tag/v6.13.0 "Release v6.13.0 · npm/cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.13.0リリース。
`npm fund`で依存パッケージの`funding`フィールドをリスト表示できるように、`npm help <command> --viewer browser`で表示するヘルプをgatsbyベースに変更など


----

## Announcing Dart 2.6 with dart2native: Compile Dart to self-contained, native executables
[medium.com/dartlang/dart2native-a76c815e6baf](https://medium.com/dartlang/dart2native-a76c815e6baf "Announcing Dart 2.6 with dart2native: Compile Dart to self-contained, native executables")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart 2.6リリース。
`dart2native` compilerでmacOSやWindows、Linux向けのネイティブコードの出力をサポート、`dart:ffi`の改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## Client-Side SQL Query Parsing with ANTLR | Rockset
[rockset.com/blog/client-side-sql-query-parsing-with-antlr/](https://rockset.com/blog/client-side-sql-query-parsing-with-antlr/ "Client-Side SQL Query Parsing with ANTLR | Rockset")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SQL</span> <span class="jser-tag">article</span></p>

ANTLRを使ったSQL構文のパーサをJavaScriptで書く方法についての記事


----

## Rethinking frontend APM - LogRocket Blog
[blog.logrocket.com/rethinking-frontend-apm/](https://blog.logrocket.com/rethinking-frontend-apm/ "Rethinking frontend APM - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

LogRocketにLogRocket MetricsというFrontend向けのパフォーマンスモニタリング機能が追加された。
APM(Application Performance Management)機能で、フロントエンドに関するいろいろなメトリクスを計測し、モニタリングやアラートを設定できる


----

## The npm Blog — Updates to Community, Docs & more...
[blog.npmjs.org/post/188841555980/updates-to-community-docs-more](https://blog.npmjs.org/post/188841555980/updates-to-community-docs-more "The npm Blog — Updates to Community, Docs & more...")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span> <span class="jser-tag">news</span></p>

npmの最近の変更と今後について。
npmのフォーラム( https://npm.community/ )はアーカイブ化しバグ関係の管理はGitHub Issuesに再び移動、npm 6.13で`npm fund`のサポートなど。
またnpm v7の変更予定としてパフォーマンスの改善、GitHubのPRからのインストール、Node 6と8のサポート終了、peerDepsをデフォルトでインストールするように変更など

- [Release v6.13.0 · npm/cli](https://github.com/npm/cli/releases/tag/v6.13.0 "Release v6.13.0 · npm/cli")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## GoogleChrome/lighthouse-ci: Automate running Lighthouse for every commit, viewing the changes, and preventing regressions
[github.com/GoogleChrome/lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci "GoogleChrome/lighthouse-ci: Automate running Lighthouse for every commit, viewing the changes, and preventing regressions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">CI </span> <span class="jser-tag">testing</span></p>

継続的にlighthouseの結果を計測し、設定したbudgetに対するassertionを行うためのCIツール。
lighthouseの結果を記録して、項目ごとにAssertionsを設定でき、コミットごとにそのパフォーマンスのリグレッションが発生してないかを継続的にチェックできるツール。

- [treosh/lighthouse-ci-action: Run Lighthouse in CI using Github Actions](https://github.com/treosh/lighthouse-ci-action "treosh/lighthouse-ci-action: Run Lighthouse in CI using Github Actions")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## GoogleChromeLabs/native-url: Node's url module implemented using the built-in URL API.
[github.com/GoogleChromeLabs/native-url](https://github.com/GoogleChromeLabs/native-url "GoogleChromeLabs/native-url: Node's url module implemented using the built-in URL API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

Node.jsの`url`モジュールを`URL`オブジェクトを使って実装したpolyfillライブラリ。
ネイティブのURL APIを使うことで、ファイルサイズが小さくなる。webpackなどのaliasで差し替える方法についても書かれている


----

## pvdz/tenko: An 100% spec compliant ES2020 JavaScript parser written in JS
[github.com/pvdz/tenko](https://github.com/pvdz/tenko "pvdz/tenko: An 100% spec compliant ES2020 JavaScript parser written in JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScriptで書かれたJavaScriptパーサライブラリ。
ES2015+の構文のパースをサポート、またESTree、Acorn、Babel形式のAST出力に対応している。

- [pvdz/zeparser2: Next version of my JS (ES5) parser](https://github.com/pvdz/zeparser2 "pvdz/zeparser2: Next version of my JS (ES5) parser")
- [pvdz/zeparser3: ZeParser3 was renamed to Tenko -> https://github.com/pvdz/tenko](https://github.com/pvdz/zeparser3 "pvdz/zeparser3: ZeParser3 was renamed to Tenko -&gt; https://github.com/pvdz/tenko")

----

## manuelbieh/geolib: Zero dependency library to provide some basic geo functions
[github.com/manuelbieh/geolib](https://github.com/manuelbieh/geolib "manuelbieh/geolib: Zero dependency library to provide some basic geo functions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

地理座標系の計算を行うライブラリ


----

## lirantal/lockfile-lint: Lint an npm or yarn lockfile to analyze and detect security issues
[github.com/lirantal/lockfile-lint](https://github.com/lirantal/lockfile-lint "lirantal/lockfile-lint: Lint an npm or yarn lockfile to analyze and detect security issues")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">yarn</span> <span class="jser-tag">security</span> <span class="jser-tag">Tools</span> <span class="jser-tag">testing</span></p>

`pacage-lock.json`や`yarn.lock`のチェックツール。
ポリシーに反する依存がロックファイル含まれていないかチェックするLintツール。

- [Why npm lockfiles can be a security blindspot for injecting malicious modules | Snyk](https://snyk.io/blog/why-npm-lockfiles-can-be-a-security-blindspot-for-injecting-malicious-modules/ "Why npm lockfiles can be a security blindspot for injecting malicious modules | Snyk")

----
<h1 class="site-genre">書籍関係</h1>

----

## The 2019 Web Almanac
[almanac.httparchive.org/en/2019/](https://almanac.httparchive.org/en/2019/ "The 2019 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">book</span></p>

HTTP Archiveのレポートと解説を合わせた書籍。
ページコンテンツ、UX、Publishing,
Distributingについて


----
