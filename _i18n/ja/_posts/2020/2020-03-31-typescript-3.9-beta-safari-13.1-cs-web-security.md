---
title: "2020-03-31のJS: TypeScript 3.9 Beta、Safari 13.1、CS Web Securityコース"
author: "azu"
layout: post
date : 2020-03-30T14:02:02.940Z
category: JSer
tags:
- TypeScript
- Safari
- ITP
- Security

---

JSer.info #481 - TypeScript 3.9 Betaがリリースされました。

- [Announcing TypeScript 3.9 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9-beta/)

`Promise.all`の型改善、`awaited` typeの追加、ビルドパフォーマンスの改善などが行われています。
また`// @ts-ignore`のように型チェックを無視するのではなく、Type Errorとなることを期待する`// @ts-expect-error`コメントディレクティブの追加が行われています。

その他には、`class`のGetter/Setterをトランスパイルした際に`enumrable: true`となっているのを、ECMAScript仕様に合わせて`enumerable: false`に変更されています。

----

iOS13.4/iPadOS13.4/macOSでそれぞれSafari 13.1がリリースされました。

- [Safari 13.1 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari_release_notes/safari_13_1_beta_release_notes)
- [Safari 13.1 のセキュリティコンテンツについて - Apple サポート](https://support.apple.com/ja-jp/HT211104)

Safari 13.1ではNullish coalescing operator(`??`)や`String.prototype.replaceAll`がサポートされています。
また、Web Animations、Async Clipboard API、Resize Observer、Picture-in-Picture APIなどのAPIも追加されています。

その他には、新しいIntelligent Tracking Prevention(ITP)の仕組みが導入されています。

- [Full Third-Party Cookie Blocking and More | WebKit](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/)

過去のITPでは条件に基づくサードパーティクッキーのブロックでしたが、[ITPの挙動を利用したトラッキングも可能であった](https://arxiv.org/abs/2001.07421)ため、
Safari 13.1からサードパーティクッキーを完全にブロックする仕組みに変更されています。

また、`document.cookie`、LocalStorage、Service Workerなどスクリプトから書き込めるストレージに7日間の上限が追加されました。
スクリプトからストレージに書き込み、そのサイトで[ユーザー操作](https://twitter.com/johnwilander/status/1242840752138248192)がなくなってから7日間たつと、そのサイトのストレージを削除する仕組みとなっています。
この7-Day Capの制限もすべてのサイトに適用されますが、いくつかの例外があるようです。

- ホーム画面に追加されたウェブアプリケーションはこの制限がない
- WKWebViewなどのWebViewではこの制限がない
- Safariを起動していない日は日付をカウントしない

参考: [iOS 13.4 and Safari 13.1 persistent storage · Issue #943 · localForage/localForage](https://github.com/localForage/localForage/issues/943)

----

スタンフォード大学のウェブセキュリティコースの動画とスライドなど資料が公開されています。

- [CS253 - Web Security](https://web.stanford.edu/class/cs253/)

[Feross](https://github.com/feross)によるウェブセキュリティに関するコースで、ブラウザ/サーバ/ネットワークなどのセキュリティに関する講義となっています。
幅広くウェブのセキュリティについて扱っているので興味がある人は見てみるとよさそうです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.3.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v1.3.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.3.0 "Release v1.3.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit 1.3.0リリース。
ステートの正規化を管理を手助けする`createEntityAdapter`、非同期処理のパターンを提供する`createAsyncThunk`の追加。
Storeのmutationを検知してエラー通知する仕組みの追加など


----

## Chrome Releases: Chrome and Chrome OS release updates
[chromereleases.googleblog.com/2020/03/chrome-and-chrome-os-release-updates.html](https://chromereleases.googleblog.com/2020/03/chrome-and-chrome-os-release-updates.html "Chrome Releases: Chrome and Chrome OS release updates")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">news</span></p>

延期していたChromeのリリーススケジュールについて。Chrome 82はキャンセルされ83に統合される予定。

- Chrome 81: 2020-04-07
- Chrome 82: キャンセル
- Chrome 83: 2020-05-19


----

## Node v13.12.0 (Current) | Node.js
[nodejs.org/en/blog/release/v13.12.0/](https://nodejs.org/en/blog/release/v13.12.0/ "Node v13.12.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">rlee</span></p>

Node.js 13.12.0リリース。
npm 6.14.4へのアップデート、`Object.prototype.__proto__`の書き込みを無効化する`--disable-proto`オプションの追加など

- [Disable \_\_proto\_\_ · Issue #31951 · nodejs/node](https://github.com/nodejs/node/issues/31951 "Disable \_\_proto\_\_ · Issue #31951 · nodejs/node")

----

## Announcing TypeScript 3.9 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-9-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9-beta/ "Announcing TypeScript 3.9 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScritp 3.9βリリース。
`Promise.all`の型改善、`awaited` typeの追加、ビルドパフォーマンスの改善、Type Errorとなることを期待する`// @ts-expect-error`コメントの追加など。
また、ECMAScript仕様にあわせてGetter/Setterをトランスパイルするとenumerableだったのをnon-enumerableに変更するなど


----

## Version 9.1 of Angular Now Available — TypeScript 3.8, faster builds, and more
[blog.angular.io/version-9-1-of-angular-now-available-typescript-3-8-faster-builds-and-more-eb292f989428](https://blog.angular.io/version-9-1-of-angular-now-available-typescript-3-8-faster-builds-and-more-eb292f989428 "Version 9.1 of Angular Now Available — TypeScript 3.8, faster builds, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 9.1リリース。
TypeScript 3.8サポート、ビルドパフォーマンスの改善、`ng e2e`が`grep`オプションをサポート、rtlのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## SecretlintでAPIトークンや秘密鍵などのコミットを防止する | Web Scratch
[efcl.info/2020/03/24/secretlint/](https://efcl.info/2020/03/24/secretlint/ "SecretlintでAPIトークンや秘密鍵などのコミットを防止する | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Docker</span> <span class="jser-tag">article</span></p>

ファイル内にAWSやGCPなどのCredentialsを含んでいないかチェックできるLintツール。
DockerやNode.jsから利用できる。プロジェクトや個人環境にpre-commit hookで組み込んだり、CIでうっかり秘匿情報が入ってないかをチェックできる。
ルールはNode.jsで自作して追加できる。

- [secretlint/secretlint: Pluggable linting tool to prevent committing credential.](https://github.com/secretlint/secretlint "secretlint/secretlint: Pluggable linting tool to prevent committing credential.")

----

## Full Third-Party Cookie Blocking and More | WebKit
[webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/ "Full Third-Party Cookie Blocking and More | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">security</span> <span class="jser-tag">privacy</span> <span class="jser-tag">article</span></p>

iOS 13.4、Safari 13.1のITPについて。
3rd-party cookieは基本的にブロック、LocalStorageを含むストレージは最後のインタラクションから7日後に削除され、`document.referrer`はoriginのみとなった。
ストレージ削除のカウントのルールについてはホームに追加したアプリやSafariを起動していない日はカウントしないなどの例外がある


----

## 🐛よくハマったFlexboxのバグまとめ｜たかもそ｜note
[note.com/takamoso/n/n32c4e6904cf7](https://note.com/takamoso/n/n32c4e6904cf7 "🐛よくハマったFlexboxのバグまとめ｜たかもそ｜note")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Flexboxのブラウザの挙動の違いや仕様についてなど


----

## What’s new in react-query v1.0 - LogRocket Blog
[blog.logrocket.com/whats-new-in-react-query-v1-0/](https://blog.logrocket.com/whats-new-in-react-query-v1-0/ "What’s new in react-query v1.0 - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

React Hooksで非同期処理を扱うreact-query 1.0の変更点について

- [tannerlinsley/react-query: ⚛️ Hooks for fetching, caching and updating asynchronous data in React](https://github.com/tannerlinsley/react-query "tannerlinsley/react-query: ⚛️ Hooks for fetching, caching and updating asynchronous data in React")

----

## UI Fabric is evolving into Fluent UI - Microsoft 365 Developer Blog
[developer.microsoft.com/en-us/office/blogs/ui-fabric-is-evolving-into-fluent-ui/](https://developer.microsoft.com/en-us/office/blogs/ui-fabric-is-evolving-into-fluent-ui/ "UI Fabric is evolving into Fluent UI - Microsoft 365 Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

MSのUIフレームワークであるUI FabricがFluent UIにリネームした。
パッケージネームも`@fluentui`のscopeで公開されるが、互換性のために`@uifabric`も公開され続ける。
また、今後のロードマップについて

- [microsoft/fluentui: We've moved! UI Fabric is now Fluent UI - A set of React components for building Microsoft web experiences.](https://github.com/microsoft/fluentui "microsoft/fluentui: We&#x27;ve moved! UI Fabric is now Fluent UI - A set of React components for building Microsoft web experiences.")

----

## HTML DOM - Common tasks of managing HTML DOM with vanilla JavaScript
[htmldom.dev/](https://htmldom.dev/ "HTML DOM - Common tasks of managing HTML DOM with vanilla JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">document</span></p>

ライブラリを使わずにDOM API使ってできることを逆引きリファレンス的に紹介しているサイト


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## CS253 - Web Security
[web.stanford.edu/class/cs253/](https://web.stanford.edu/class/cs253/ "CS253 - Web Security")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">web </span> <span class="jser-tag">server</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

スタンフォード大学のWeb Securityコースのスライドと動画。
ブラウザからサーバまで攻撃/防御視点でのセキュリティについて学ぶ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Chrome DevTools // slidr.io
[slidr.io/bmeurer/chrome-devtools#1](https://slidr.io/bmeurer/chrome-devtools#1 "Chrome DevTools // slidr.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">ESLint</span></p>

Chrome DevToolsについてのスライド。
DevToolsのアーキテクチャ、機能の紹介など


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## chrvadala/node-ble: Bluetooth Low Energy (BLE) library written with pure Node.js (no bindings) - baked by Bluez via DBus
[github.com/chrvadala/node-ble](https://github.com/chrvadala/node-ble "chrvadala/node-ble: Bluetooth Low Energy (BLE) library written with pure Node.js (no bindings) - baked by Bluez via DBus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Bluetooth</span> <span class="jser-tag">library</span></p>

Pure Node.jsなBLEライブラリ


----

## kriasoft/node-sqlite at v4
[github.com/kriasoft/node-sqlite/tree/v4](https://github.com/kriasoft/node-sqlite/tree/v4 "kriasoft/node-sqlite at v4")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SQLite</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsのSQLiteクライアントライブラリ


----

## heremaps/harp.gl: harp.gl - web map rendering engine
[github.com/heremaps/harp.gl](https://github.com/heremaps/harp.gl "heremaps/harp.gl: harp.gl - web map rendering engine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">library</span></p>

three.jsを使った3Dマップレンダリングエンジンライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## TypeScript Weekly
[www.typescript-weekly.com/](https://www.typescript-weekly.com/ "TypeScript Weekly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">mail</span></p>

TypeScriptについてのWeeklyメールマガジン


----

## 初心者からちゃんとしたプロになる　JavaScript基礎入門 | 西畑 一馬, 須郷 晋也, 岡島 美咲, 扇 克至, 岩本 大樹 | 工学 | Kindleストア | Amazon
[www.amazon.co.jp/dp/B0863LYNQQ/](https://www.amazon.co.jp/dp/B0863LYNQQ/ "初心者からちゃんとしたプロになる　JavaScript基礎入門 | 西畑 一馬, 須郷 晋也, 岡島 美咲, 扇 克至, 岩本 大樹 | 工学 | Kindleストア | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">book</span></p>

2020年3月25日発売
JavaScriptとVueについての書籍


----
