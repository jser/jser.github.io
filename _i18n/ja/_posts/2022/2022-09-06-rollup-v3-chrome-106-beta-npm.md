---
title: "2022-09-06のJS: Rollup v3の変更点、 Chrome 106 Beta、npmベストプラクティス"
author: "azu"
layout: post
date : 2022-09-05T15:01:32.595Z
category: JSer
tags:
- node.js
- browser
- testing
- document
- CSS

---

JSer.info #608 - Rollup 3.0のプレリリース版が公開されています。

- [[v3.0 Release branch] by lukastaegert · Pull Request #4549 · rollup/rollup](https://github.com/rollup/rollup/pull/4549)


Rollup 3.0では、Node.js 12のサポート終了、ブラウザ向けのパッケージを`@rollup/browser`に分離、非推奨のメソッドの削除。 `output.interop`に`compat`を追加、`--bundleConfigAsCjs`フラグの追加などが予定されています。

----

Chrome 106 Betaが公開されました。

- [Chromium Blog: Chrome 106 Beta: New CSS Features, WebCodecs and WebXR Improvements, and More](https://blog.chromium.org/2022/09/chrome-106-beta-new-css-features.html)

Origin Trialsとしてiframeの`anonymous`属性、Pop-Up APIの追加されています。
Android WebViewでのClient Hintsをサポート、CSSの単位として`ic`をサポート、`Intl.NumberFormat` v3 APIをサポート、`WebCodecs`の`dequeue`イベントのサポートなども含まれています。
また、破壊的な変更としてCookieのドメイン属性の非ASCII文字を削除、HTTP/2 Pushのサポートの削除なども含まれています。

----

[Open Source Security Foundation](https://openssf.org/blog/2022/09/01/npm-best-practices-for-the-supply-chain/)からnpmでのパッケージ公開のセキュリティについてのベストプラクティスのドキュメントが公開されています。

- [package-manager-best-practices/npm.md at main · ossf/package-manager-best-practices](https://github.com/ossf/package-manager-best-practices/blob/main/published/npm.md)

また、JavaScriptのライブラリをnpmへパッケージとして公開に関するガイドが公開されています。

- [frehner/modern-guide-to-packaging-js-library: A guide to help ensure your JavaScript library is the most compatible, fast, and efficient library you can make.](https://github.com/frehner/modern-guide-to-packaging-js-library)

こちらも合わせて読んでみると良いかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v6.0.0 beta 1 · styled-components/styled-components
[github.com/styled-components/styled-components/releases/tag/v6.0.0-beta.1](https://github.com/styled-components/styled-components/releases/tag/v6.0.0-beta.1 "Release v6.0.0 beta 1 · styled-components/styled-components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

styled-components v6.0.0-beta.1リリース。
TypeScriptでの書き直し、stylis v4へのアップデート、Node.js 12のサポート終了などが含まれる


----

## Release v5.5.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v5.5.0](https://github.com/lerna/lerna/releases/tag/v5.5.0 "Release v5.5.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

lerna v5.5.0リリース。
pnpm workspacesのサポート


----

## \[v3.0 Release branch\] by lukastaegert · Pull Request #4549 · rollup/rollup
[github.com/rollup/rollup/pull/4549](https://github.com/rollup/rollup/pull/4549 "\[v3.0 Release branch\] by lukastaegert · Pull Request #4549 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rollup</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup 3.0の変更点について。
Node.js 12のサポート終了、ブラウザ向けのパッケージを`@rollup/browser`に分離、非推奨のメソッドの削除。
`output.interop`に`compat`を追加、`--bundleConfigAsCjs`フラグの追加など


----

## Release v0.23.0 · vitest-dev/vitest
[github.com/vitest-dev/vitest/releases/tag/v0.23.0](https://github.com/vitest-dev/vitest/releases/tag/v0.23.0 "Release v0.23.0 · vitest-dev/vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

vitest v0.23.0リリース。
CJSとの互換性の改善、`retry`オプションの追加、`vitest bench`コマンドの追加、coverageのjson reporterの追加など


----

## Release v7.10.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v7.10.0](https://github.com/pnpm/pnpm/releases/tag/v7.10.0 "Release v7.10.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v7.10.0リリース。
`resolution-mode`に`time-based`の追加、`pnpm env remove`の追加など


----

## Release v5.0.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v5.0.0](https://github.com/avajs/ava/releases/tag/v5.0.0 "Release v5.0.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA v5.0.0 preリリース。
Node.js 12以下のサポート終了、TypeScript 4.7未満のサポート終了など


----

## TestCafe v2.0.0 Released | Framework | Release Notes
[testcafe.io/404018/release-notes/framework/2022-8-31-testcafe-v2-0-0-released](https://testcafe.io/404018/release-notes/framework/2022-8-31-testcafe-v2-0-0-released "TestCafe v2.0.0 Released | Framework | Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe 2.0.0リリース。
TypeScriptのアップデート、JavaScriptのエラーを無視するオプションの追加など


----

## Chromium Blog: Chrome 106 Beta: New CSS Features, WebCodecs and WebXR Improvements, and More
[blog.chromium.org/2022/09/chrome-106-beta-new-css-features.html](https://blog.chromium.org/2022/09/chrome-106-beta-new-css-features.html "Chromium Blog: Chrome 106 Beta: New CSS Features, WebCodecs and WebXR Improvements, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 106 Betaリリース。
Origin Trialsとしてiframeの`anonymous`属性、Pop-Up APIの追加。
Android WebViewでのClient Hintsをサポート、CSSの単位として`ic`をサポート、`Intl.NumberFormat` v3 APIをサポート、`WebCodecs`の`dequeue`イベントのサポートなど。
Cookieのドメイン属性の非ASCII文字を削除、HTTP/2 Pushのサポートの削除など


----
<h1 class="site-genre">アーティクル</h1>

----

## Modern alternatives to BEM - daverupert.com
[daverupert.com/2022/08/modern-alternatives-to-bem/](https://daverupert.com/2022/08/modern-alternatives-to-bem/ "Modern alternatives to BEM - daverupert.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">architecture</span> <span class="jser-tag">article</span></p>

CSSに`@layer`やWeb Componentsなどの新しい概念が増えたことで、CSSの設計がどのように変わっていくかについて。


----

## Anonymous iframe origin trial: Easily embed iframes in COEP environments - Chrome Developers
[developer.chrome.com/blog/anonymous-iframe-origin-trial/](https://developer.chrome.com/blog/anonymous-iframe-origin-trial/ "Anonymous iframe origin trial: Easily embed iframes in COEP environments - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

`Cross-Origin-Embedder-Policy: require-corp`と`Cross-Origin-Opener-Policy: same-origin`のレスポンスヘッダを返すサイトではないと、クロスオリジン分離してiframeとして埋め込めない。
この問題を解決するために、iframe要素に`anonymous`属性について


----

## Things not available when someone blocks all cookies
[blog.tomayac.com/2022/08/30/things-not-available-when-someone-blocks-all-cookies/](https://blog.tomayac.com/2022/08/30/things-not-available-when-someone-blocks-all-cookies/ "Things not available when someone blocks all cookies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

Cookieをブロックした状態で呼び出すと例外が発生するAPIについて
localStorage、IndexedDB、Service Workers、Cookie APIなどについて


----

## Implementing Promisable setTimeout | yield code(); - Dmitry Kudryavtsev
[yieldcode.blog/post/implementing-promisable-set-timeout](https://yieldcode.blog/post/implementing-promisable-set-timeout "Implementing Promisable setTimeout | yield code(); - Dmitry Kudryavtsev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`setTimeout`のPromise版の実装とAbortControllerを使ったキャンセルについて。
また、Node.jsの`timers/promises`について。


----

## 実践 Node.js Native ESM — Wantedlyでのアプリケーション移行事例 | Wantedly Engineer Blog
[www.wantedly.com/companies/wantedly/post\_articles/410531](https://www.wantedly.com/companies/wantedly/post_articles/410531 "実践 Node.js Native ESM — Wantedlyでのアプリケーション移行事例 | Wantedly Engineer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

Node.jsのNative ESM対応について。
ESMとCJSの非互換性の問題と対処についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## layerhub-io/react-design-editor: Image, Presentation and Video editor. React design editor using fabric.js. Canva clone
[github.com/layerhub-io/react-design-editor](https://github.com/layerhub-io/react-design-editor "layerhub-io/react-design-editor: Image, Presentation and Video editor. React design editor using fabric.js. Canva clone")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

Reactで書かれたプレゼン、動画編集のエディタライブラリ。Canvaクローン。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## package-manager-best-practices/npm.md at main · ossf/package-manager-best-practices
[github.com/ossf/package-manager-best-practices/blob/main/published/npm.md](https://github.com/ossf/package-manager-best-practices/blob/main/published/npm.md "package-manager-best-practices/npm.md at main · ossf/package-manager-best-practices")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

npmのセキュリティに関するベストプラクティスについてのドキュメント。
CIの構成、依存関係の管理、ロックファイル、パッケージのリリース、レジストリについてなど

- [npm Best Practices for the Supply-Chain - Open Source Security Foundation](https://openssf.org/blog/2022/09/01/npm-best-practices-for-the-supply-chain/ "npm Best Practices for the Supply-Chain - Open Source Security Foundation")

----

## flomesh-io/pipy: Pipy is a programmable proxy for the cloud, edge and IoT.
[github.com/flomesh-io/pipy](https://github.com/flomesh-io/pipy "flomesh-io/pipy: Pipy is a programmable proxy for the cloud, edge and IoT.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">proxy</span> <span class="jser-tag">C++</span> <span class="jser-tag">software</span></p>

C++で書かれたプログラマブルなProxy。
スクリプティング言語としてJavaScriptで記述できる


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## frehner/modern-guide-to-packaging-js-library
[github.com/frehner/modern-guide-to-packaging-js-library](https://github.com/frehner/modern-guide-to-packaging-js-library "frehner/modern-guide-to-packaging-js-library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">document</span></p>

JavaScriptライブラリを公開するときのガイド。
ESM/CJS/UMD形式の公開、Tree Shakingに対応する、minifyをしない、Source Mapをつける、外部ライブラリをコピーして含めないなど。
またpackage.jsonのフィールドについての解説など


----

## bluwy/whyframe: Develop components in isolation
[github.com/bluwy/whyframe](https://github.com/bluwy/whyframe "bluwy/whyframe: Develop components in isolation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

iframe内にマークアップを描画するコンポーネントライブラリ。
Svelte、Vue、Reactなど各種UIフレームワークに対応している


----

## tinylibs/tinyspy: 🕵🏻‍♂️ minimal fork of nanospy, with more features
[github.com/tinylibs/tinyspy](https://github.com/tinylibs/tinyspy "tinylibs/tinyspy: 🕵🏻‍♂️ minimal fork of nanospy, with more features")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

依存のないspyライブラリ


----

## BetterTyped/hyper-fetch: ⚡ Backend agnostic fetching framework for any javascript environment - queues, caching, persistence, builders, commands, offline and more!
[github.com/BetterTyped/hyper-fetch](https://github.com/BetterTyped/hyper-fetch "BetterTyped/hyper-fetch: ⚡ Backend agnostic fetching framework for any javascript environment - queues, caching, persistence, builders, commands, offline and more!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Fetch</span></p>

UniversalなFetchライブラリ。
Builder APIで特定のエンドポイントを叩くコマンドを作成して利用する。
キャッシュ、キュー管理、キャンセル、Prefetchingなどをサポートしている。


----
