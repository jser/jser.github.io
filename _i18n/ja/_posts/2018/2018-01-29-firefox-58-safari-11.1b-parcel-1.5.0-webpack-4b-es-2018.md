---
title: "2018-01-29のJS: Firefox 58、Safari 11.1(β)、Parcel 1.5.0、webpack 4(β)、ES 2018の機能が決定"
author: "azu"
layout: post
date : 2018-01-29T21:51:02.933Z
category: JSer
tags:
- firefox
- Safari
- Bundler
- webpack
- parcel

---

JSer.info #368 - Firefox 58.0がリリースされました。

- [Firefox — Notes (58.0) — Mozilla](https://www.mozilla.org/en-US/firefox/58.0/releasenotes/)
- [Firefox 58 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/58 "Firefox 58 for developers - Mozilla | MDN")
- [Firefox 58 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/58/ "Firefox 58 サイト互換性情報 | Firefox サイト互換性情報")


[バッググラウンドタブにおけるスロットリングの強化](https://developer.mozilla.org/ja/docs/Web/Guide/User_experience/Using_the_Page_Visibility_API#Policies_in_place_to_aid_background_page_performance)、WebAssembly Streaming Compilerの導入。
CSS Font Displayのサポート、`Promise#finally`の追加、`PerformanceNavigationTiming` APIの実装など

詳しくは次の記事で解説されています。

- [Firefox 58: The Quantum Era Continues – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/01/firefox-58-the-quantum-era-continues/ "Firefox 58: The Quantum Era Continues – Mozilla Hacks – the Web developer blog")
- [Making WebAssembly even faster: Firefox’s new streaming and tiering compiler – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/01/making-webassembly-even-faster-firefoxs-new-streaming-and-tiering-compiler/ "Making WebAssembly even faster: Firefox’s new streaming and tiering compiler – Mozilla Hacks – the Web developer blog")

----

[Safari 11.1](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_11_1.html "Safari 11.1")(β)が開発者向けに公開されています。

Safari 11.1ではService Worker、Payment Request API、`HTMLImageElement.decode()`、Beacon APIのサポート。
Subresource Integrity、Storage Access API、Intelligent Tracking Preventionの挙動の変更などが行われています。

----

BundlerであるParcel 1.5.0がリリースされました。
Source Mapsの対応や、WebAssemblyなどAssertsの対応が追加されています。

- [📦 Parcel v1.5.0 released: Source Maps, WebAssembly, Rust, and more! 🚀](https://medium.com/@devongovett/parcel-v1-5-0-released-source-maps-webassembly-rust-and-more-3a6385e43b95 "📦 Parcel v1.5.0 released: Source Maps, WebAssembly, Rust, and more! 🚀")

また、webpack 4(β)もリリースされています。
`--mode`オプションが必須となり、典型的な設定は`mode: development`または`mode: production`で行われてるようになっています。デフォルトでは`src`をソースディレクトリにし、`dist`ディレクトリに出力するといった設定ファイルなしでの利用改善が図られています。

- [🚀webpack 4 beta — try it today!🚀 – webpack – Medium](https://medium.com/webpack/webpack-4-beta-try-it-today-6b1d27d7d7e2)
- [Release v4.0.0-beta.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v4.0.0-beta.0)

また`CommonsChunkPlugin`などの一部プラグインを削除され、代わりに`optimization`のオプションで設定できるようになるといった変更なども含まれています。

- [RIP CommonsChunkPlugin.md](https://gist.github.com/sokra/1522d586b8e5c0f5072d7565c2bee693 "RIP CommonsChunkPlugin.md")

----

[62nd meeting of Ecma TC39](https://github.com/tc39/agendas/blob/master/2018/01.md "62nd meeting of Ecma TC39")が行われ、ECMAScript 2018に最終的に入るProposalが決定しました。
ECMAScriptは毎年6月ごろにリリースされるため、これから新しい機能(Proposal)を入れると間に合わなくなります。
そのため、1月ごろに機能(Proposal)の追加はフリーズされ、この時期からStage 4となったProposalは[ECMAScript仕様本体](https://github.com/tc39/ecma262 "ECMAScript")へマージされます。

- [is:pr label:"pending stage 4"](https://github.com/tc39/ecma262/pulls?utf8=%E2%9C%93&q=is%3Apr+label%3A%22pending+stage+4%22+)で実際にマージの様子が確認できます。

[Finished Proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "Finished Proposals")にまとめられていますが、ES2018には次の8つのProposalがマージされます。

- [tc39/proposal-template-literal-revision](https://github.com/tc39/proposal-template-literal-revision)
  - テンプレートリテラルの改善
- [tc39/proposal-regexp-dotall-flag: Proposal to add the `s` (`dotAll`) flag to regular expressions in ECMAScript.](https://github.com/tc39/proposal-regexp-dotall-flag)
  - `/./s`が改行や絵文字などにもマッチできるようにする`s`フラグの追加
- [tc39/proposal-regexp-named-groups: Named capture groups for JavaScript RegExps](https://github.com/tc39/proposal-regexp-named-groups)
  - 正規表現の名前付きキャプチャ
- [tc39/proposal-regexp-lookbehind: RegExp lookbehind assertions](https://github.com/tc39/proposal-regexp-lookbehind)
  - 正規表現の後読みのサポート
- [tc39/proposal-regexp-unicode-property-escapes: Proposal to add Unicode property escapes `\p{…}` and `\P{…}` to regular expressions in ECMAScript.](https://github.com/tc39/proposal-regexp-unicode-property-escapes)
  - `/^\p{White_Space}+$/u` Unicode character propertiesのサポート
- [tc39/proposal-object-rest-spread: Rest/Spread Properties for ECMAScript](https://github.com/tc39/proposal-object-rest-spread)
  - `{ ...obj }` オブジェクト版のRest/Spreadプロパティ(配列はES2015から利用できる)
- [tc39/proposal-promise-finally: ECMAScript Proposal, specs, and reference implementation for Promise.prototype.finally](https://github.com/tc39/proposal-promise-finally)
  - Promiseチェーンの最後に必ず実行されるコールバックを指定できる`Promise.prototype.finally`のサポート
- [tc39/proposal-async-iteration: Asynchronous iteration for JavaScript](https://github.com/tc39/proposal-async-iteration)
  - IteratorのAsync版

Proposalの詳しい解説は次の記事にまとめられています。

- [ECMAScript 2018: the final feature set](http://2ality.com/2017/02/ecmascript-2018.html)

今回のTC39ミーティングで変化があったProposalは次のページにまとめてあります。

- [ECMAScript proposal updates at 2018-01 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2018/01/28/ecmascript-proposal-updates)
- [ECMAScript 2018: the final feature set](http://2ality.com/2017/02/ecmascript-2018.html)



----

<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at 11.6.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/11.6.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/11.6.0/Changelog.md "jsdom/Changelog.md at 11.6.0 · tmpvar/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 11.6.0リリース。
`WebSocket`の実装、`performance`の実装、`window.devicePixelRatio`の追加など


----

## Firefox — Notes (58.0) — Mozilla
[www.mozilla.org/en-US/firefox/58.0/releasenotes/](https://www.mozilla.org/en-US/firefox/58.0/releasenotes/ "Firefox — Notes (58.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 58リリース。
バッググラウンドタブにおけるスロットリングの強化、WebAssembly Streaming Compilerの導入。
CSS Font Displayのサポート、`Promise#finally`の追加、`PerformanceNavigationTiming` APIの実装など

- [Firefox 58: The Quantum Era Continues – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/01/firefox-58-the-quantum-era-continues/ "Firefox 58: The Quantum Era Continues – Mozilla Hacks – the Web developer blog")
- [Firefox 58 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/58 "Firefox 58 for developers - Mozilla | MDN")
- [Firefox 58 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/58/ "Firefox 58 サイト互換性情報 | Firefox サイト互換性情報")

----

## 📦 Parcel v1.5.0 released: Source Maps, WebAssembly, Rust, and more! 🚀
[medium.com/@devongovett/parcel-v1-5-0-released-source-maps-webassembly-rust-and-more-3a6385e43b95](https://medium.com/@devongovett/parcel-v1-5-0-released-source-maps-webassembly-rust-and-more-3a6385e43b95 "📦 Parcel v1.5.0 released: Source Maps, WebAssembly, Rust, and more! 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v1.5.0リリース。
Source Mapのサポート、WebAssemblyのサポート、`.env`ファイルに対応。
また、コンフィグファイルが追加されたときにキャッシュを削除するようになるなど


----

## Release v4.0.0-beta.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v4.0.0-beta.0](https://github.com/webpack/webpack/releases/tag/v4.0.0-beta.0 "Release v4.0.0-beta.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 4.0.0βリリース。
Node.js 4のサポート終了、`mode`が必須のオプションに、`import()`は常に名前空間オブジェクトを返すように。
また、`CommonsChunkPlugin`などの一部プラグインを削除し代わりに`optimization`のオプションで設定できるように変更など

- [RIP CommonsChunkPlugin.md](https://gist.github.com/sokra/1522d586b8e5c0f5072d7565c2bee693 "RIP CommonsChunkPlugin.md")
- [🚀webpack 4 beta — try it today!🚀 – webpack – Medium](https://medium.com/webpack/webpack-4-beta-try-it-today-6b1d27d7d7e2 "🚀webpack 4 beta — try it today!🚀 – webpack – Medium")

----

## Release Notes for Safari Technology Preview 48 | WebKit
[webkit.org/blog/8084/release-notes-for-safari-technology-preview-48/](https://webkit.org/blog/8084/release-notes-for-safari-technology-preview-48/ "Release Notes for Safari Technology Preview 48 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 48リリース。
Storage Access APIをデフォルトで有効化、Service Workerの対応改善、`createImageBitmap(ImageBitmap)`の実装など


----

## Safari 11.1
[developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari\_11\_1.html](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_11_1.html "Safari 11.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

現在β公開中のSafari 11.1の変更点について。
Service Worker、Payment Request、`HTMLImageElement.decode()`、Beacon APIのサポート。
Subresource Integrity、Storage Access API、Intelligent Tracking Preventionの挙動の変更など


----

## Stable AngularJS and Long Term Support – Angular Blog
[blog.angular.io/stable-angularjs-and-long-term-support-7e077635ee9c](https://blog.angular.io/stable-angularjs-and-long-term-support-7e077635ee9c "Stable AngularJS and Long Term Support – Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">news</span></p>

AngularJS(1.x)のLTSスケジュールについて。
現在開発中のAngularJS 1.7は2018年7月にリリースされ、そこから3年間メンテされるLTSとなる。
1.7.x以降はAngularJSに新しい機能などは追加しない予定。


----
<h1 class="site-genre">アーティクル</h1>

----

## Improvements to the DevTools Console in the Windows 10 Fall Creators Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2018/01/17/devtools-console-improvements-edgehtml-16/](https://blogs.windows.com/msedgedev/2018/01/17/devtools-console-improvements-edgehtml-16/ "Improvements to the DevTools Console in the Windows 10 Fall Creators Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

EdgeHTML16の開発者ツールの改善について


----

## 🚀webpack 4 beta — try it today!🚀 – webpack – Medium
[medium.com/webpack/webpack-4-beta-try-it-today-6b1d27d7d7e2](https://medium.com/webpack/webpack-4-beta-try-it-today-6b1d27d7d7e2 "🚀webpack 4 beta — try it today!🚀 – webpack – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack 4βについての解説記事。
パフォーマンス、設定、ファイルサイズ、ファイルタイプのサポート、最適化オプションなどについて


----

## ECMAScript proposal updates at 2018-01 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2018/01/28/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2018/01/28/ecmascript-proposal-updates "ECMAScript proposal updates at 2018-01 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">proposal</span></p>

2018年1月のTC39のミーティング結果を反映したECMAScript Proposalのステータスまとめ。


----

## New in Chrome 64  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/01/nic64](https://developers.google.com/web/updates/2018/01/nic64 "New in Chrome 64  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 64の変更点について
`ResizeObservers`、RegExpのNamed Capture、`import.meta`のサポート。`<video>`や`<audio>`の`preload`属性のデフォルト値が`metadata`へと変更など

- [New in Chrome 64: ResizeObservers, Named Captures, import.meta and more! - YouTube](https://www.youtube.com/watch?v=y5sb-icqOyg "New in Chrome 64: ResizeObservers, Named Captures, import.meta and more! - YouTube")

----

## Top 10 JavaScript errors from 1000+ projects (and how to avoid them)
[rollbar.com/blog/top-10-javascript-errors/](https://rollbar.com/blog/top-10-javascript-errors/ "Top 10 JavaScript errors from 1000+ projects (and how to avoid them)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

エラー収集サービスのRollbarにおいて報告されたJavaScriptのエラーランキング。
どのようなエラーメッセージか、またどのような状況で発生するかなどを解説している。

- [JavaScript エラーリファレンス - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Errors "JavaScript エラーリファレンス - JavaScript | MDN")

----

## ECMAScript 2018: the final feature set
[2ality.com/2017/02/ecmascript-2018.html](http://2ality.com/2017/02/ecmascript-2018.html "ECMAScript 2018: the final feature set")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">spec</span></p>

2018年1月でECMAScript 2018に入るProposalが決まったため、そのProposalをまとめた記事


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## JavaScript Object Explorer
[sdras.github.io/object-explorer/](https://sdras.github.io/object-explorer/ "JavaScript Object Explorer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">Tools</span></p>

JavaScriptのオブジェクトに関する操作方法(作成、削除、更新など)を対話的に選択してコードを出してくれるサイト。
配列版もあり、翻訳も募集している。

- [JavaScript Array Explorer](https://sdras.github.io/array-explorer/ "JavaScript Array Explorer")
- [Translations needed! · Issue #1 · sdras/object-explorer](https://github.com/sdras/object-explorer/issues/1 "Translations needed! · Issue #1 · sdras/object-explorer")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## 0x00A/scratches: A scratchpad. Read, Evaluate, Print, Loop, but with a nicer editor.
[github.com/0x00A/scratches](https://github.com/0x00A/scratches "0x00A/scratches: A scratchpad. Read, Evaluate, Print, Loop, but with a nicer editor.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Electron</span> <span class="jser-tag">software</span> <span class="jser-tag">mac </span></p>

Electron製のJavaScriptスクラッチパッド。
JavaScriptのコードを実行して評価結果を並べて表示するアプリ


----

## fastpack/fastpack: Pack JS code fast & easy
[github.com/fastpack/fastpack](https://github.com/fastpack/fastpack "fastpack/fastpack: Pack JS code fast & easy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">flowtype</span></p>

OCaml製のJavaScript Bundlerツール。
Flowをパーサとして使い、コードのbundleを行う。postprocessとして他のツールを呼びだすことができる。
高速なインクリメンタルビルドを行うことが目的。


----
<h1 class="site-genre">書籍関係</h1>

----

## Webサイトパフォーマンス実践入門 高速なWebページを作りたいあなたに（JeremyL.Wagner 武舎広幸 阿部和也 上西昌弘）｜翔泳社の本
[www.shoeisha.co.jp/book/detail/9784798155098](http://www.shoeisha.co.jp/book/detail/9784798155098 "Webサイトパフォーマンス実践入門 高速なWebページを作りたいあなたに（JeremyL.Wagner 武舎広幸 阿部和也 上西昌弘）｜翔泳社の本")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">翻訳</span> <span class="jser-tag">book</span></p>

2018年03月19日発売。
Web Performance in Actionの翻訳本


----
