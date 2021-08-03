---
title: "2021-08-03のJS: Yarn 3.0、Chrome 93 beta、cross origin iframeでのalert/prompt/confirmを削除"
author: "azu"
layout: post
date : 2021-08-03T03:38:52.177Z
category: JSer
tags:
- React
- node.js
- Chrome
- DOM
- browser

---

JSer.info #551 - Yarn 3.0がリリースされました。

- [Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻](https://dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07)
- [berry/CHANGELOG.md at master · yarnpkg/berry](https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md#300)

Node.js 10のサポート終了、`.pnp.cjs`にリネーム、`@yarnpkg/pnpify`を3つのパッケージに分解などの変更を含んでいます。

- `@yarnpkg/sdks`: [Editor SDKs](https://yarnpkg.com/getting-started/editor-sdks)
- `@yarnpkg/pnpify`: PnPと互換性のないツールを実行するツール
- `@yarnpkg/nm`: `node_modules` linker

また、 `exports`フィールドのサポート、[pnpm](https://pnpm.io/)ライクなハードリンクのサポート、シェル構文のサポート改善、 ESBuildでのbundleをサポートする`@yarnpkg/esbuild-plugin-pnp`の追加なども含まれています。


----

Chrome 93 betaがリリースされました。

- [Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More](https://blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html)

Origin TrialとしてCOEPの導入をより手軽にするための[`Cross-Origin-Embedder-Policy：credentialless`](https://github.com/WICG/credentiallessness)、[URL Handlers](https://web.dev/pwa-url-handler/)の追加などが含まれています。
また、 `AbortSignal.abort()`メソッドのサポート、Stage 3のError causeと`Object.hasOwn`のサポートも含まれています。

ダークモード対応などではCSSの`prefers-color-scheme` media queryを使い、ユーザーエージェントがどのcolor schemeを優先するかを判定していました。しかし、CSSではページロード後となるため、ページロード時にその判定ができるようにClient Hint Headerの`Sec-CH-Prefers-Color-Scheme`が追加されています。
また、`navigator.userAgent`や`User-Agent`ヘッダの後継となる、User-Agent Client Hintsに関するAPIやヘッダの変更も含まれています。

- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)

---

Chrome 92では、cross originのiframe内から`window.{alert, prompt, confirm}`が利用できなくなりました。

- [1065085 - Implement window.{alert, prompt, confirm} removal from cross-origin iframes - chromium](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085)
- [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576)

この問題への対処方法として、次のような方法があげられています。

- Chrome 96(12月)まで有効な[Reverse Origin Trial](https://developer.chrome.com/origintrials/#/view_trial/2541156089743802369)を有効化する
- ダイアログUIを自作する方法
- [postMessageを使って親ドキュメントでダイアログを出す方法](https://stackoverflow.com/questions/68492434/javascript-dialogs-alert-confirm-and-prompt-in-cross-origin-iframe-does-n)

この影響で、CodePenなどのiframeを使ってコードを実行する環境、Google Apps Scriptをウェブサイトとして公開しているケース、Salesforceの一部機能などが動かなくなるなどの影響が出ています。
いくつかのウェブサイトで影響があったため、Chromeでは[2021年8月15日まで無効化](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085#c41)されています。(Reverse Origin Trialのための猶予期間)

他のブラウザもこの仕様に追従する予定となっています。

- [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576)
- [Proposal: Disallow cross-origin iframes usage of window.{alert, confirm, prompt} · Issue #5407 · whatwg/html](https://github.com/whatwg/html/issues/5407)

詳しくは次のページも参照してください。

- [Cross Origin iframe からの alert/confirm/prompt 呼び出しの無効化 | blog.jxck.io](https://blog.jxck.io/entries/2021-08-02/3rd-party-iframe-dialog.html)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Headless UI v1.4: The One With Tabs – Tailwind CSS
[blog.tailwindcss.com/headless-ui-v1-4](https://blog.tailwindcss.com/headless-ui-v1-4 "Headless UI v1.4: The One With Tabs – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Headless UI 1.4リリース。
Tagコンポーネントの追加、`Disclosures`と`Popover`のPanel内に`Button`を置くとPanelを閉じれるように


----

## Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻
[dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07](https://dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07 "Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">ReleaseNote</span></p>

Yarn 3.0リリース。
Node.js 10のサポート終了、`.pnp.cjs`にリネーム、`@yarnpkg/pnpify`を3つのパッケージに分解など。
`exports`フィールドのサポート、pnpmライクなハードリンクのサポート、シェル構文のサポート改善、 ESBuildのサポートなど

- [berry/CHANGELOG.md at master · yarnpkg/berry](https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md#300 "berry/CHANGELOG.md at master · yarnpkg/berry")

----

## Release 3.16.0 - 2021.07.30 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.16.0](https://github.com/zloirock/core-js/releases/tag/v3.16.0 "Release 3.16.0 - 2021.07.30 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core.js 3.16.0リリース。
Stage 3の`Array#findLast`、Stage 1の`Array#filterOut`と`Array#groupBy`のサポート。
Denoのサポートなど


----

## Node v16.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.6.0/](https://nodejs.org/en/blog/release/v16.6.0/ "Node v16.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 16.6.0リリース。
V8 9.2へアップデート、`http2`のセキュリティ修正など

- [V8 release v9.2 · V8](https://v8.dev/blog/v8-release-92 "V8 release v9.2 · V8")

----

## Recoil 0.4 | Recoil
[recoiljs.org/blog/2021/07/30/0.4.0-release/](https://recoiljs.org/blog/2021/07/30/0.4.0-release/ "Recoil 0.4 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.4リリース。
キャッシュポリシーを`cachePolicy_UNSTABLE`で設定できるように、トランザクションをする`useRecoilTransaction_UNSTABLE`で利用できるように。
TypeScriptの型改善など


----

## Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More
[blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html](https://blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html "Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 93 betaリリース。
Origin Trialとして`Cross-Origin-Embedder-Policy：credentialless`、URL Handlersの追加など。
`AbortSignal.abort()`メソッドのサポート、Stage 3のError causeと`Object.hasOwn`のサポート。
Client Hint Headerの`Sec-CH-Prefers-Color-Scheme`の追加やUA Client Hintの更新など


----

## 1065085 - Implement window.\{alert, prompt, confirm\} removal from cross-origin iframes - chromium
[bugs.chromium.org/p/chromium/issues/detail?id&#x3D;1065085](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085 "1065085 - Implement window.\{alert, prompt, confirm\} removal from cross-origin iframes - chromium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">DOM</span> <span class="jser-tag">news</span></p>

Chrome 92でcross origin iframeからのalert/dialog/promptが無効化された。
回避方法として、Chrome 96まで有効なReverse Origin Trial、ダイアログUIを自作する方法、postMessageを使って親ドキュメントでダイアログを出す方法など。

- [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576 "Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status")
- [Proposal: Disallow cross-origin iframes usage of window.\{alert, confirm, prompt\} · Issue #5407 · whatwg/html](https://github.com/whatwg/html/issues/5407 "Proposal: Disallow cross-origin iframes usage of window.\{alert, confirm, prompt\} · Issue #5407 · whatwg/html")
- [google chrome - JavaScript dialogs alert(), confirm() and prompt() in cross origin iframe does not work any longer - Stack Overflow](https://stackoverflow.com/questions/68492434/javascript-dialogs-alert-confirm-and-prompt-in-cross-origin-iframe-does-n "google chrome - JavaScript dialogs alert(), confirm() and prompt() in cross origin iframe does not work any longer - Stack Overflow")
- [Chrome Enterprise release notes - Google Chrome Enterprise Help](https://support.google.com/chrome/a/answer/7679408#92&zippy=%2Cchrome "Chrome Enterprise release notes - Google Chrome Enterprise Help")
- [Intent to Remove: Cross origin subframe JS Dialogs](https://groups.google.com/a/chromium.org/g/blink-dev/c/hTOXiBj3D6A/m/gFXmgIz9AwAJ "Intent to Remove: Cross origin subframe JS Dialogs")
- [Cross Origin iframe からの alert/confirm/prompt 呼び出しの無効化 | blog.jxck.io](https://blog.jxck.io/entries/2021-08-02/3rd-party-iframe-dialog.html "Cross Origin iframe からの alert/confirm/prompt 呼び出しの無効化 | blog.jxck.io")

----

## Release Version 16.7.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/16.7.0](https://github.com/jsdom/jsdom/releases/tag/16.7.0 "Release Version 16.7.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 16.7.0リリース。
`AbortSignal.abort()`のサポート、`getBoundingClientRect()`の返り値に`x`と`y`を追加。
`<textarea>`の改行コードのノーマライゼーションを仕様に準拠するように変更など

- [The WHATWG Blog — Newline normalizations in form submission](https://blog.whatwg.org/newline-normalizations-in-form-submission "The WHATWG Blog — Newline normalizations in form submission")

----
<h1 class="site-genre">アーティクル</h1>

----

## How do Chrome extensions impact browser performance?
[www.debugbear.com/blog/chrome-extension-performance-2021](https://www.debugbear.com/blog/chrome-extension-performance-2021 "How do Chrome extensions impact browser performance?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ブラウザ拡張がウェブサイトのパフォーマンスにどのように影響を与えているかについての記事。
CPU負荷、初回のレンダリングへの影響、バックグラウンでのCPU処理、、メモリ消費量。
またAdBlocker系とデータ量やメモリ消費量の削減について


----

## WebView2 and Electron | Electron Blog
[www.electronjs.org/blog/webview2](https://www.electronjs.org/blog/webview2 "WebView2 and Electron | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">windows</span> <span class="jser-tag">article</span></p>

ElectronとWindowsのWebView2のアーキテクチャ的な違いについて。


----

## GraphQLクライアントにurqlをおすすめしたい
[zenn.dev/adwd/articles/f4c5c5120467bb](https://zenn.dev/adwd/articles/f4c5c5120467bb "GraphQLクライアントにurqlをおすすめしたい")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">article</span></p>

GraphQLクライアントライブラリのurqlについて。
レスポンスをキャッシュの仕組みとキャッシュを履きする仕組みについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## BlueBlazin/thislang: An implementation of a subset of javascript in that subset of javascript.
[github.com/BlueBlazin/thislang](https://github.com/BlueBlazin/thislang "BlueBlazin/thislang: An implementation of a subset of javascript in that subset of javascript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">language</span></p>

JavaScriptでのJavaScript subsetの実装。


----

## arcanis/clipanion: Type-safe CLI library with no runtime dependencies
[github.com/arcanis/clipanion](https://github.com/arcanis/clipanion "arcanis/clipanion: Type-safe CLI library with no runtime dependencies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

CLI向けのコマンドライン引数パーサライブラリ。
ネストされたコマンドのサポート、typanionと連携したバリデーション、ヘルプのサポートなど。
Yarnで利用されている。


----

## crcn/sift.js: Use Mongodb queries in JavaScript
[github.com/crcn/sift.js](https://github.com/crcn/sift.js "crcn/sift.js: Use Mongodb queries in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptのオブジェクトに対してMongoDB Queryライクな構文や演算子で検索できるライブラリ


----
