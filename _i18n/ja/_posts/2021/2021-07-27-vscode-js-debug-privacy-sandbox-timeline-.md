---
title: "2021-07-27のJS: vscode-js-debug、 Privacy Sandbox Timeline、小さなブラウザの作り方"
author: "azu"
layout: post
date : 2021-07-27T12:52:36.749Z
category: JSer
tags:
- node.js
- browser
- security
- Tools
- Chrome

---

JSer.info #550 - - [Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/)
- [microsoft/vscode-js-debug: The VS Code JavaScript debugger](https://github.com/microsoft/vscode-js-debug)
  - [Official page for Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/)

----

- [Privacy Sandbox Timeline](https://privacysandbox.com/timeline/)
  - [Google releases a timeline for Privacy Sandbox rollout in Chrome](https://www.xda-developers.com/google-chrome-privacy-sandbox-floc-timeline/)


---

- [ブラウザの作り方 - Speaker Deck](https://speakerdeck.com/keiya01/burauzafalsezuo-rifang?slide=23)
- [Let's build a browser engine! Part 1: Getting started](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
- [ちいさな Web ブラウザを作ってみよう](https://browserbook.shift-js.info/)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Version 2.0 released : Node-RED
[nodered.org/blog/2021/07/20/version-2-0-released](https://nodered.org/blog/2021/07/20/version-2-0-released "Version 2.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

IoTデバイスなどを扱うビジュアルプログラミング環境のNode-RED 2.0.0リリース。

- [Release 2.0.0: Milestone Release · node-red/node-red](https://github.com/node-red/node-red/releases/tag/2.0.0 "Release 2.0.0: Milestone Release · node-red/node-red")

----
<h1 class="site-genre">アーティクル</h1>

----

## URLPattern brings routing to the web platform
[web.dev/urlpattern/](https://web.dev/urlpattern/ "URLPattern brings routing to the web platform")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

path-to-regexpのようにURLのパターンマッチを扱う`URLPattern`オブジェクトについて。
基本的な使い方、キャプチャ、ブラウザサポートとPolyfillについて


----

## Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/](https://blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/ "Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

VSCodeからChromeとMSEdgeのDebuggerに接続するvscode-js-debug拡張について。
DAP(Debug Adapter Protocol)のProtocol Adapterを使い、VScodeからブラウザのデバッグに接続している。

- [microsoft/vscode-js-debug: The VS Code JavaScript debugger](https://github.com/microsoft/vscode-js-debug "microsoft/vscode-js-debug: The VS Code JavaScript debugger")

----

## Fastly Launches New Era of Highly-Secure Serverless JavaScript With Zero Cold Starts | Fastly
[www.fastly.com/press/press-releases/fastly-launches-new-era-of-highly-secure-serverless-javascript-with-zero](https://www.fastly.com/press/press-releases/fastly-launches-new-era-of-highly-secure-serverless-javascript-with-zero "Fastly Launches New Era of Highly-Secure Serverless JavaScript With Zero Cold Starts | Fastly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">cdn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

FastlyのCompute@EdgeがJavaScriptをサポート

- [JS on Wasm with Nick Fitzgerald (JS Party #183) |&gt; Changelog](https://changelog.com/jsparty/183 "JS on Wasm with Nick Fitzgerald (JS Party #183) |&amp;gt; Changelog")

----

## How to Eliminate Render-Blocking Resources: a Deep Dive
[sia.codes/posts/render-blocking-resources/](https://sia.codes/posts/render-blocking-resources/ "How to Eliminate Render-Blocking Resources: a Deep Dive")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

レンダリングブロッキングの要素となるJavaScriptとCSSについて。
レンダリングブロックされるとどのようにパフォーマンスへ影響があるのか、WebPageTestを使った確認方法、レンダリングブロッキングの削除方法についてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Privacy Sandbox Timeline
[privacysandbox.com/timeline/](https://privacysandbox.com/timeline/ "Privacy Sandbox Timeline")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">document</span></p>

Privacy Sandboxのロードマップとタイムライン


----

## nicoespeon/abracadabra: Automated refactorings for VS Code (JS &amp; TS) ✨ It&#039;s magic ✨
[github.com/nicoespeon/abracadabra](https://github.com/nicoespeon/abracadabra "nicoespeon/abracadabra: Automated refactorings for VS Code (JS &amp; TS) ✨ It&#039;s magic ✨")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">refacoring</span> <span class="jser-tag">plugin</span> <span class="jser-tag">JavaScript</span></p>

JavaScriptとTypeScriptのリファクタリングを補助するVSCode拡張。
WebStormのようにコードのQuick Fixを提供している


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Tak-Iwamoto/ptera: Ptera is DateTime library for Deno
[github.com/Tak-Iwamoto/ptera](https://github.com/Tak-Iwamoto/ptera "Tak-Iwamoto/ptera: Ptera is DateTime library for Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Deno向けの日付操作ライブラリ

- [DenoのDateTimeライブラリPteraをリリースしました](https://zenn.dev/tak_iwamoto/articles/8b32b27bd577b1 "DenoのDateTimeライブラリPteraをリリースしました")

----

## ajitid/fzf-for-js: Do fuzzy matching using FZF algorithm in JavaScript
[github.com/ajitid/fzf-for-js](https://github.com/ajitid/fzf-for-js "ajitid/fzf-for-js: Do fuzzy matching using FZF algorithm in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">search</span></p>

コマンドラインツール向けの曖昧(あいまい)検索であるFZFのアルゴリズムをJavaScriptに移植したライブラリ


----

## ES-Community/nsecure: Node.js security CLI / API that allow you to deeply analyze the dependency tree of a given package / directory
[github.com/ES-Community/nsecure](https://github.com/ES-Community/nsecure "ES-Community/nsecure: Node.js security CLI / API that allow you to deeply analyze the dependency tree of a given package / directory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Tools</span></p>

ディレクトリや特定のパッケージのnpmパッケージへの依存を分析するツール。
コードをパースして、利用しているnpmパッケージのメタデータ、ライセンス、セキュリティ情報などの一覧を取得する


----

## tangramxyz/tangram: Tangram is an all-in-one automated machine learning framework.
[github.com/tangramxyz/tangram](https://github.com/tangramxyz/tangram "tangramxyz/tangram: Tangram is an all-in-one automated machine learning framework.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">library</span> <span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ruby </span> <span class="jser-tag">python</span> <span class="jser-tag">golang</span></p>

機械学習フレームワーク。
コマンドラインで学習したモデルを作成し、各種言語のFFIなライブラリから予測ができる。
JavaScriptにWasmビルドを公開している。
またモデルのパフォーマンスダッシュボードをブラウザで見れるようになっている。


----

## udecode/plate: A plugin framework for building rich text editors with slate.
[github.com/udecode/plate](https://github.com/udecode/plate "udecode/plate: A plugin framework for building rich text editors with slate.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

slateベースのリッチテキストエディタライブラリ。
プラグインで機能を追加できるようになっていて、さまざまなプラグインが用意されている。


----

## actuallyakash/spacers: 🔳 when you need more \_\_space\_\_
[github.com/actuallyakash/spacers](https://github.com/actuallyakash/spacers "actuallyakash/spacers: 🔳 when you need more \_\_space\_\_")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

D&Dで要素に対してpaddingやmarginなどのスペースを設定できるライブラリ


----

## davewasmer/devcert: Local HTTPS development made easy
[github.com/davewasmer/devcert](https://github.com/davewasmer/devcert "davewasmer/devcert: Local HTTPS development made easy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">SSL</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

ローカルで開発用のHTTPSサーバの作成を補助するライブラリ。
任意のドメインに対する証明書の作成、マシンへのルート証明書のインストールなどローカルでHTTPSサーバを起動するのを補助するツール。


----
<h1 class="site-genre">書籍関係</h1>

----

## ちいさな Web ブラウザを作ってみよう
[browserbook.shift-js.info/](https://browserbook.shift-js.info/ "ちいさな Web ブラウザを作ってみよう")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">book</span> <span class="jser-tag">Rust</span> <span class="jser-tag">security</span></p>

Rustでウェブブラウザを作りつつ、ブラウザのレンダリングの仕組み、全体の流れ、セキュリティについて学習する教材。


----
