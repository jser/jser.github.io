---
title: "2021-03-09のJS: Gatsby 3、Electron 12、ブラウザのライフサイクルの変化"
author: "azu"
layout: post
date : 2021-03-08T14:53:58.520Z
category: JSer
tags:
- React
- serverless
- aws
- GraphQL
- jQuery

---

JSer.info #530 - Gatsby v3がリリースされました。

- [Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby](https://www.gatsbyjs.com/blog/gatsby-v3/)
- [Gatsby v3.0 (March 2021 #1)](https://www.gatsbyjs.com/docs/reference/release-notes/v3.0/)

ローカルでは実際にアクセスされたページだけをビルドすることで、全体を再構築せずにビルドする挙動がデフォルトとなっています。これによって必要なページだけをビルドするため、開発時のビルド待ち時間を少なくしています。

破壊的変更としてNode.js 12未満のサポート終了、React 17/webpack 5/ESLint 7へアップデート、globalの`graphql`ではなくimportして使うように変更、APIの変更などが含まれています。

マイグレーション方法については、次のドキュメントに丁寧な解説が書かれています。

- [Migrating from v2 to v3 | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/migrating-from-v2-to-v3/)

---

Electron 12.0.0がリリースされました。

- [Electron 12.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-12-0)


Chromium 89、V8 8.9、Node.js 14.16(12.xからの更新)へアップデートされています。
`exposeInMainWorld`がオブジェクト以外をサポート、`webFrameMain` APIの追加など含まれています。

Electron 12.0.0では`contextIsolation`と`worldSafeExecuteJavaScript`がデフォルトで`true`に変更されています。
[Context Isolation](https://www.electronjs.org/docs/tutorial/context-isolation)は`preload`のスクリプトと`webContents`のスクリプトの実行コンテキスト分離することで、XSSなどの被害の範囲を軽減する仕組みです。

- [Electron: Context Isolationの欠如を利用した任意コード実行 / Electron: Abusing the lack of context isolation - CureCon(ja) - Speaker Deck](https://speakerdeck.com/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-ja)
- [Electron（v.12.0.0 現在）の IPC 通信入門 - よりセキュアな方法への変遷 - Qiita](https://qiita.com/hibara/items/c59fb6924610fc22a9db)

また、[段階的に廃止されている`remote`モジュール](https://github.com/electron/electron/issues/21408)が非推奨となり、[@electron/remote](https://github.com/electron/remote)という外部モジュールへと移行されています。

- [electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.](https://github.com/electron/remote)

---

ブラウザのライフサイクルが変化してきているのでいくつかのニュースをまとめて紹介します。

現在6週間ごとにリリースされているChromeですが、Q3 of 2021のChrome 94からはリリースサイクルを4週間ごとに短縮することを発表しました。

- [Chromium Blog: Speeding up Chrome's release cycle](https://blog.chromium.org/2021/03/speeding-up-release-cycle.html)
- [Chromium Dash](https://chromiumdash.appspot.com/schedule)

Microsoft Edge Legacyの廃止スケジュールが公開されています。
Microsoft Edge Legacyは2021年3月9日でサポート終了されます。また、2021年4月13に配信されるセキュリティアップデートで削除され、同時に新しいChromiumベースのMSEdgeがインストールされます。(置き換わる)

- [New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224)

Internet Explorer(IE)の廃止はEdgeとは異なるライフサイクルであるためまだまだ先ですが、
IEでアクセスしたときにMSEdgeへリダイレクトする互換リストによって移行が進められています。

- [Moving users to Microsoft Edge from Internet Explorer - Microsoft Edge Development | Microsoft Docs](https://docs.microsoft.com/en-us/microsoft-edge/web-platform/ie-to-microsoft-edge-redirection)

この[NeedEdgeの互換リスト](https://edge.microsoft.com/neededge/v1)に記載されたサイトへIEで訪問すると、MSEdgeで開き直すように促すリダイレクトポップアップが表示されるようになります。
この互換リストに[追加されているサイト](https://github.com/teppeis/history-of-ie-incompatible-sites-list/commits/master)は徐々に増えてきています。
これとは、別にIEのサポート終了を宣言しているサイトについては次のドキュメントにまとめられています。

- [IE11 サポート終了の歴史 - Google ドキュメント](https://docs.google.com/document/d/1XP58gVMyp_UCP4FFsf5ATpvRVwqi7v_EpEF3sl_Sobk/edit)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby
[www.gatsbyjs.com/blog/gatsby-v3/](https://www.gatsbyjs.com/blog/gatsby-v3/ "Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">ReleaseNote</span></p>

Gatsby 3.0リリース。
破壊的変更としてNode.js 12未満のサポート終了、webpack 5/ESLint 7へアップデート、globalの`graphql`ではなくimportして使うように変更、APIの変更など。
ローカルでは実際にアクセスされたページだけをビルドすることで、全体を再構築せずにビルドできるように

- [Migrating from v2 to v3 | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/migrating-from-v2-to-v3/ "Migrating from v2 to v3 | Gatsby")

----

## jQuery 3.6.0 Released! | Official jQuery Blog
[blog.jquery.com/2021/03/02/jquery-3-6-0-released/](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/ "jQuery 3.6.0 Released! | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">JSON</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.6.0リリース。
JSONPのリクエスト時に、エラーレスポンスがJSONを返した場合の挙動を変更。
`.force()`のバグを修正など


----

## Deno 1.8 Release Notes
[deno.land/posts/v1.8](https://deno.land/posts/v1.8 "Deno 1.8 Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.8.0リリース。
試験的にWebGPU APIのサポート。
ICUに対応しECMA i18n APIである`Intl` オブジェクトなどのサポート。`DENO_AUTH_TOKENS`でモジュールを取得する際の認証トークンをサポート、Exit sanitierを`Deno.test`に追加、`deno fmt`がJSONをサポート、TypeScript 4.2へアップデート。
Import Map、`Deno.permissions`、`Deno.link`、`Deno.symlink` APIがそれぞれStable APIとなった。


----

## New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community
[techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224](https://techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224 "New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">news</span></p>

Microsoft Edge Legacyは2021年3月9日でサポート終了される。
また、2021年4月13に削除されるセキュリティアップデートが配信され、同時に新しいChromiumベースのMSEdgeがインストールされる。


----

## Chromium Blog: Speeding up Chrome&#039;s release cycle
[blog.chromium.org/2021/03/speeding-up-release-cycle.html](https://blog.chromium.org/2021/03/speeding-up-release-cycle.html "Chromium Blog: Speeding up Chrome&#039;s release cycle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">news</span></p>

Chromeのリリースサイクルが6週間ごとから4週間ごとに短縮される。


----

## Announcing the New TypeScript Handbook | TypeScript
[devblogs.microsoft.com/typescript/announcing-the-new-typescript-handbook/](https://devblogs.microsoft.com/typescript/announcing-the-new-typescript-handbook/ "Announcing the New TypeScript Handbook | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span></p>

TypeScript Handbookが刷新された。

- [TypeScript: The starting point for learning TypeScript](https://www.typescriptlang.org/docs/ "TypeScript: The starting point for learning TypeScript")

----

## Electron 12.0.0 | Electron Blog
[www.electronjs.org/blog/electron-12-0](https://www.electronjs.org/blog/electron-12-0 "Electron 12.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 12.0.0リリース。
Chromium 89、V8 8.9、Node.js 14.16へアップデート。
`exposeInMainWorld`がオブジェクト以外をサポート、`webFrameMain` APIの追加など。
`contextIsolation`と`worldSafeExecuteJavaScript`がデフォルトで`true`に変更、`remote`モジュールが非推奨となり`@electron/remote`外部モジュール化

- [electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.](https://github.com/electron/remote "electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.")

----

## Release v6.0.0 · pixijs/pixi.js
[github.com/pixijs/pixi.js/releases/tag/v6.0.0](https://github.com/pixijs/pixi.js/releases/tag/v6.0.0 "Release v6.0.0 · pixijs/pixi.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">canvas</span> <span class="jser-tag">WebGL</span></p>

pixi.js 6.0.0リリース。
TypeScriptの型改善、DeprecatedとなっていたAPIの削除、`alpha`オプションのデフォルト値を`true`に変更、`FAIL_IF_MAJOR_PERFORMANCE_CAVEAT`のデフォルト値を`false`に変更など


----

## Google Developers Blog: Announcing Flutter 2
[developers.googleblog.com/2021/03/announcing-flutter-2.html](https://developers.googleblog.com/2021/03/announcing-flutter-2.html "Google Developers Blog: Announcing Flutter 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">ReleaseNote</span></p>

Flutter 2リリース。
WebサポートとデスクトップサポートがStableとなり、Dart 2.12をサポート。
iOSでAutocompleteとScaffoldMessengerのサポートなど

- [Dart 2.12](https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87 "Dart 2.12")
- [Flutter web support hits the stable milestone | Flutter](https://medium.com/flutter/flutter-web-support-hits-the-stable-milestone-d6b84e83b425 "Flutter web support hits the stable milestone | Flutter")
- [What’s New in Flutter 2. by Chris Sells | Mar, 2021 | Medium | Flutter | Flutter](https://medium.com/flutter/whats-new-in-flutter-2-0-fe8e95ecc65 "What’s New in Flutter 2. by Chris Sells | Mar, 2021 | Medium | Flutter | Flutter")

----
<h1 class="site-genre">アーティクル</h1>

----

## Mini apps - web.dev
[web.dev/mini-apps/](https://web.dev/mini-apps/ "Mini apps - web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span></p>

Mini appsのエコシステムの記事


----

## Hiding Content Responsibly | Kitty Giraudel
[kittygiraudel.com/2021/02/17/hiding-content-responsibly/](https://kittygiraudel.com/2021/02/17/hiding-content-responsibly/ "Hiding Content Responsibly | Kitty Giraudel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

コンテンツの非表示を意味するCSSやWAI-ARIA属性のそれぞれの動作とアクセシビリティ的な挙動についてのまとめ。
データ、ビジュアル、レイアウト、セマンティクス、コンテンツ、キーボード、ポインター、スタイルなどの状態について

- [removal techniques and implications](https://codepen.io/vincent-valentin/full/JjGmxzV "removal techniques and implications")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## serverless-stack/serverless-stack: Serverless Stack (SST) is a framework that makes it easy to build serverless apps.
[github.com/serverless-stack/serverless-stack](https://github.com/serverless-stack/serverless-stack "serverless-stack/serverless-stack: Serverless Stack (SST) is a framework that makes it easy to build serverless apps.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">serverless</span> <span class="jser-tag">aws</span></p>

AWS CDKを使ったserverless管理、開発ツール。
Lambdaの開発、デプロイ、ビルドやLintの設定、各種AWSスタックとの連携などを含む


----

## NightlyCommit/twing: First-class Twig engine for Node.js
[github.com/NightlyCommit/twing](https://github.com/NightlyCommit/twing "NightlyCommit/twing: First-class Twig engine for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">template</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

テンプレートエンジンであるTwigのJavaScript実装ライブラリ


----

## JakePartusch/serverlessui: A command-line utility for deploying serverless applications to AWS. Complete with custom domains, deploy previews, TypeScript support, and more.
[github.com/JakePartusch/serverlessui](https://github.com/JakePartusch/serverlessui "JakePartusch/serverlessui: A command-line utility for deploying serverless applications to AWS. Complete with custom domains, deploy previews, TypeScript support, and more.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">serverless</span> <span class="jser-tag">Tools</span></p>

AWSへserverlessアプリケーションをデプロイするためのツール。
CDKを使って静的なサイトとlambdaなどのデプロイを一括で行う


----

## nanojsx/nano: 🎯 SSR first, lightweight 1kB JSX library.
[github.com/nanojsx/nano](https://github.com/nanojsx/nano "nanojsx/nano: 🎯 SSR first, lightweight 1kB JSX library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

JSXを使ったSSR firstなUIライブラリ。
指定したコンポーネントのみをHydrate、Lazy Hydrateができ、ビルトインでRouterやHead周りのコンポーネントを持っている。
ReactライクなライフサイクルメソッドやHooksの処理を持っている。

- [Nano JSX • Lightweight 1kB JSX library](https://nanojsx.github.io/ "Nano JSX • Lightweight 1kB JSX library")

----
