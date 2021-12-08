---
title: "2021-12-08のJS: Rust + Node-APIのパッケージの公開、 #WebSpeedHackathon 、The 2021 Web Almanac"
author: "azu"
layout: post
date : 2021-12-08T03:54:12.200Z
category: JSer
tags:
- Svelte
- node.js
- Tools
- book
- HTTP

---

JSer.info #569 - [Rust + Node-APIでクロスプラットフォーム向けnpmパッケージを公開する - 別にしんどくないブログ](https://shisama.hatenablog.com/entry/2021/12/03/054437)という記事では、Rustでnapi-rsを使って書いたコードをNode.jsから利用する方法について書かれています。

パッケージとして公開する場合、Node.jsのNode-APIを使うためネイティブモジュールとしてインストール必要があります。
その場合に、インストール後に`postinstall`でバイナリをダウンロード/ビルドするのではなく、`optionalDependencies`を使ってアーキテクチャごとのパッケージをインストールできるようにする方法についても紹介されています。

---

[#WebSpeedHackathon](https://twitter.com/search?f=realtime&q=%0A%23WebSpeedHackathon)の2021年版が開催されています。

- [重いサイトを軽くしろ！年末年始は #WebSpeedHackathon 2021 に挑戦しよう | CyberAgent Developers Blog](https://developers.cyberagent.co.jp/blog/archives/32747/)
- [CyberAgentHack/web-speed-hackathon-2021](https://github.com/CyberAgentHack/web-speed-hackathon-2021)

重たいウェブサイトのパフォーマンスを改善するハッカソン教材として作られたアプリケーションです。
2022/1/3まで開催されていて、スコアはGitHub Actionsで計測する仕組みも公開されています。
ウェブサイトのパフォーマンス改善に興味がある人は触ってみると面白いかもしれません。

---

HTTP Archiveのデータをもとにウェブの状態をまとめたWeb Almanacの2021年版が公開されています。

- [The 2021 Web Almanac](https://almanac.httparchive.org/en/2021/)

ブラウザのテクノロジーやウェブの状態を確認できるレポートで、全24章から構成されています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v17.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.2.0/](https://nodejs.org/en/blog/release/v17.2.0/ "Node v17.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.2.0リリース。
`async_hooks`モジュールに`asyncWrapProviders`を追加、AbortSignalに`reason`を追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Rust + Node-APIでクロスプラットフォーム向けnpmパッケージを公開する - 別にしんどくないブログ
[shisama.hatenablog.com/entry/2021/12/03/054437](https://shisama.hatenablog.com/entry/2021/12/03/054437 "Rust + Node-APIでクロスプラットフォーム向けnpmパッケージを公開する - 別にしんどくないブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

napi-rsを使ったRustで書いたコードをNode.jsのnative modulesとして利用する方法について。
アーキテクチャごとのバイナリをpublishしoptionalDependenciesとして定義することで、`postinstall`を不要にする方法について。


----

## react-router 作り方
[zenn.dev/stin/articles/how-to-develop-react-router](https://zenn.dev/stin/articles/how-to-develop-react-router "react-router 作り方")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">history</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

react-routerが内部的に利用している`history`ライブラリを使ったルータの作り方についての記事


----

## 重いサイトを軽くしろ！年末年始は #WebSpeedHackathon 2021 に挑戦しよう | CyberAgent Developers Blog
[developers.cyberagent.co.jp/blog/archives/32747/](https://developers.cyberagent.co.jp/blog/archives/32747/ "重いサイトを軽くしろ！年末年始は #WebSpeedHackathon 2021 に挑戦しよう | CyberAgent Developers Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">example</span> <span class="jser-tag">article</span></p>

ウェブパフォーマンスを改善するハッカソン教材

- [CyberAgentHack/web-speed-hackathon-2021](https://github.com/CyberAgentHack/web-speed-hackathon-2021 "CyberAgentHack/web-speed-hackathon-2021")

----

## Web Performance Calendar » HTTP compression
[calendar.perfplanet.com/2021/http-compression/](https://calendar.perfplanet.com/2021/http-compression/ "Web Performance Calendar » HTTP compression")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ロスレスデータ圧縮の圧縮レベルと速度のバランスについて。
gzip、brotli、zstd、圧縮レベルのトレードオフについて。
また、バイナリコンテンツの2重圧縮の問題などについて


----

## WebAssembly and Back Again: Fine-Grained Sandboxing in Firefox 95 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/](https://hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/ "WebAssembly and Back Again: Fine-Grained Sandboxing in Firefox 95 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox 95に含まれるRLBoxというWebAssemblyを使ったSandboxの仕組みについて。
プロセスの分離はオーバヘッドが大きくなりやすい。分離したいコードをWasmに変換し、Wasmをwasm2cでC言語に変換してネイティブコードへ変換し利用する。
Wasmを経由することで指定外のメモリ空間にアクセスできないことを保証している。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf JP 2021 Track A - YouTube
[www.youtube.com/playlist?list&#x3D;PL42hYWKFRfN7cg6c3uM4\_tAxbybVzG3ao](https://www.youtube.com/playlist?list=PL42hYWKFRfN7cg6c3uM4_tAxbybVzG3ao "JSConf JP 2021 Track A - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JSConf JP 2021の動画一覧

- [JSConf JP 2021 Track B - YouTube](https://www.youtube.com/playlist?list=PL42hYWKFRfN7XWswj9wcC0j4191KNJuO3 "JSConf JP 2021 Track B - YouTube")
- [JSConf JP 2021 Track C - YouTube](https://www.youtube.com/playlist?list=PL42hYWKFRfN4l-KXE-2xzy95dRKPtCg0V "JSConf JP 2021 Track C - YouTube")
- [JSConf JP](https://jsconf.jp/2021/ "JSConf JP")

----

## Svelte Summit Fall 2021 - YouTube
[www.youtube.com/playlist?list&#x3D;PL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt](https://www.youtube.com/playlist?list=PL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt "Svelte Summit Fall 2021 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Svelte Summit Fall 2021の動画まとめ

- [Svelte Summit Fall 2021](https://card.zenn.dev/?url=https%3A%2F%2Fwww.youtube.com%2Fplaylist%3Flist%3DPL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt "Svelte Summit Fall 2021")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## primo-af/primo: a simpler, all-in-one way to develop and manage websites
[github.com/primo-af/primo](https://github.com/primo-af/primo "primo-af/primo: a simpler, all-in-one way to develop and manage websites")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">CMS</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">software</span></p>

静的なサイトを管理、開発するためのCMSアプリ。
Svelteベースで作られていて、デスクトップアプリでサイトを編集ができ、バックエンドはSupabaseベースのものが公開されている。


----

## Online CSS Analyzer - Project Wallace
[www.projectwallace.com/analyze-css](https://www.projectwallace.com/analyze-css "Online CSS Analyzer - Project Wallace")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">webservice</span></p>

URLを指定してサイトが利用しているCSSを解析するツール。
サイズ、セレクタ数、詳細度、色、フォントの指定などについての分析結果を表示する


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## denoland/dnt: Deno to npm package build tool.
[github.com/denoland/dnt](https://github.com/denoland/dnt "denoland/dnt: Deno to npm package build tool.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Deno向けに書かれたモジュールをNode.jsで利用できるように変換するツール。

- [dnt というツールについて - Qiita](https://qiita.com/kt3k/items/8947fddc9f580ba32307 "dnt というツールについて - Qiita")

----

## Open Props: sub-atomic styles
[open-props.style/](https://open-props.style/ "Open Props: sub-atomic styles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

CSS custom propertiesを使ったライブラリ。


----

## BuilderIO/mitosis: Write components once, run everywhere. Compiles to Vue, React, Solid, Angular, Svelte, and more.
[github.com/BuilderIO/mitosis](https://github.com/BuilderIO/mitosis "BuilderIO/mitosis: Write components once, run everywhere. Compiles to Vue, React, Solid, Angular, Svelte, and more.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JSXベースコンポーネントを定義し、それをReact/Angular/Vue/Solid/Svelteなどの各種フレームワークを使ったコードへと変換できるツール。
UIフレームワークの中間言語


----

## plentico/plenti: Static Site Generator with Go backend and Svelte frontend
[github.com/plentico/plenti](https://github.com/plentico/plenti "plentico/plenti: Static Site Generator with Go backend and Svelte frontend")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">Tools</span> <span class="jser-tag">golang</span></p>

SvelteとGo言語を使った静的サイトジェネレータ


----
<h1 class="site-genre">書籍関係</h1>

----

## The 2021 Web Almanac
[almanac.httparchive.org/en/2021/](https://almanac.httparchive.org/en/2021/ "The 2021 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">book</span> <span class="jser-tag">browser</span> <span class="jser-tag">HTTP</span></p>

HTTP Archiveのデータ元にしたレポートであるWeb Almanacの2021年版。
ブラウザのテクノロジーやウェブの状態を確認できるレポート


----

## The Jamstack Book
[www.manning.com/books/the-jamstack-book](https://www.manning.com/books/the-jamstack-book "The Jamstack Book")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Jamstack</span> <span class="jser-tag">book</span></p>

2022年4月26日発売予定
Jamstackについての書籍


----
