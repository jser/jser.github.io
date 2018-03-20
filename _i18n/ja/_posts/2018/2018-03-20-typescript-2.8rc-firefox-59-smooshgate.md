---
title: "2018-03-20のJS: TypeScript 2.8RC、Firefox 59、#SmooshGate"
author: "azu"
layout: post
date : 2018-03-20T01:23:07.818Z
category: JSer
tags:
- TypeScript
- firefox
- ECMAScript

---

JSer.info #375　- TypeScript 2.8 RCがリリースされました。

- [Announcing TypeScript 2.8 RC | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/ "Announcing TypeScript 2.8 RC | TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-28 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

Conditional Typesのサポート、Mapped Type Modifierの`-`、`+`ができるようになりNonNullableへの変換が扱えるようになりました。
また、JSX Pragmasをコメントで指定できるようなり、`.d.ts`だけを出力する`--emitDeclarationsOnly`のサポートなどが行われています。

Conditional Typesで型の表現の幅が広がりますが、詳細はリリースノートや次の記事を参照してください。

- [TypeScript 2.8 の Conditional Types について - Qiita](https://qiita.com/Quramy/items/b45711789605ef9f96de)
- [Strongly Typed Event Emitters with Conditional Types](https://medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8)

----

Firefox 59がリリースされました。

- [Firefox — Notes (59.0) — Mozilla](https://www.mozilla.org/en-US/firefox/59.0/releasenotes/ "Firefox — Notes (59.0) — Mozilla")
- [Firefox 59 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Releases/59 "Firefox 59 for developers - Mozilla | MDN")

[PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent "PointerEvent")がデフォルトで有効化され、[`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior "overscroll-behavior")の実装、`EventTarget`コンストラクタの実装がされています。

[EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget "EventTarget")はNode.jsのEventEmitterのように継承して利用できるpub/subなクラスとして利用できます。

- [EventTarget の継承可能化による EventEmitter の代替 | blog.jxck.io](https://blog.jxck.io/entries/2017-07-10/subclassible-eventtarget.html "EventTarget の継承可能化による EventEmitter の代替 | blog.jxck.io")

----

[#SmooshGate FAQ  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/03/smooshgate "#SmooshGate FAQ  |  Web  |  Google Developers")という記事では、最近話題となった[#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")についてよくある質問を解説しています。

[#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")とは現在Stage 3のProposalである[Array.prototype.flatMap & Array.prototype.flatten](https://tc39.github.io/proposal-flatMap/ "Array.prototype.flatMap &amp; Array.prototype.flatten")とbreak the webについての問題です。
Firefox Nightlyに`Array.prototype.flatten`が実験的に実装されてた所、MooToolsの`Array.prototype.flatten`の実装と衝突し動作しないサイトがあることとわかりました。
その回避案の１つとして`Array.prototype.flatten`を`Array.prototype.smoosh`にリネームするPRが出された一連の流れを[#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")と呼んでいます。

- [rename flatten to smoosh by michaelficarra · Pull Request #56 · tc39/proposal-flatMap](https://github.com/tc39/proposal-flatMap/pull/56 "rename flatten to smoosh by michaelficarra · Pull Request #56 · tc39/proposal-flatMap")
- [SmooshGate: The ongoing struggle between progress and stability in JavaScript](https://medium.com/@jacobdfriedmann/smooshgate-the-ongoing-struggle-between-progress-and-stability-in-javascript-2a971c1162dd "SmooshGate: The ongoing struggle between progress and stability in JavaScript")

実際に判定ツールを書いたので[Can I Standardize?](https://azu.github.io/can-i-standardize/ "Can I Standardize?")試すことができますが、`Array.prototype.flatten`はMooToolsやprototype.js、sugar.jsなどで実装されています。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Can I Standardize?<a href="https://t.co/Q1hA7MnHqB">https://t.co/Q1hA7MnHqB</a><br><br>`Array.prototype.flatten`:<br>- prototype.js define: true<br>- MooTools define: true<br>- Suger.js define: true<br><br>`Array.prototype.smoosh`:<br>prototype.js define: false<br>MooTools define: false<br>Suger.js define: false<br><br> <a href="https://twitter.com/hashtag/smooshgate?src=hash&amp;ref_src=twsrc%5Etfw">#smooshgate</a> <a href="https://twitter.com/hashtag/ecmascript?src=hash&amp;ref_src=twsrc%5Etfw">#ecmascript</a> <a href="https://t.co/JQluGQLU4N">pic.twitter.com/JQluGQLU4N</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/971958777485312000?ref_src=twsrc%5Etfw">March 9, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

この記事ではなぜprototype拡張によってbreak the webが起きるのか、なぜMooToolsを直しただけでは解決しないのか、TC39はこれからこの問題をどう修正していくかなどについて書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 2.8 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/](https://blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/ "Announcing TypeScript 2.8 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.8 RCリリース。
Conditional Types、Mapped Type Modifierの`-`、`+`ができるように、JSX Pragmasをコメントで指定できるようなるなど


----

## Release v1.2.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.2.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.2.0 "Release v1.2.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 1.2.0リリース。
`elementHandle.contentFrame()`の追加、リダイレクト回数を返す`request.redirectChain()`の追加など


----

## Firefox — Notes (59.0) — Mozilla
[www.mozilla.org/en-US/firefox/59.0/releasenotes/](https://www.mozilla.org/en-US/firefox/59.0/releasenotes/ "Firefox — Notes (59.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 59リリース。
開発者ツールの改善、[PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent "PointerEvent")をデフォルトで有効化、[`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior "overscroll-behavior")の実装、[`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget)コンストラクタの実装など

- [Firefox 59 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Releases/59 "Firefox 59 for developers - Mozilla | MDN")

----

## Release Inferno v5.0.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v5.0.0](https://github.com/infernojs/inferno/releases/tag/v5.0.0 "Release Inferno v5.0.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Inferno v5.0.0 リリース。 `.mjs`で配布していたのを`.js`に変更、 IE9のサポート終了、TypeScriptのサポート改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## とあるLPの制作現場 - Qiita
[qiita.com/noplan1989/items/a52a957546ddb9efeca3](https://qiita.com/noplan1989/items/a52a957546ddb9efeca3 "とあるLPの制作現場 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">design</span></p>

実際にウェブサイトのランディングページ(LP)の作る際にどのように作成したかについて。


----

## How to Build Password Generator with Electron & React Pt.1 - Setting the Stage - Alex Devero Blog
[blog.alexdevero.com/password-generator-pt1/](https://blog.alexdevero.com/password-generator-pt1/ "How to Build Password Generator with Electron & React Pt.1 - Setting the Stage - Alex Devero Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">JavaScript</span></p>

Electronを使ったパスワードジェネレータアプリのチュートリアル


----

## Unblocking Clipboard Access  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/clipboardapi](https://developers.google.com/web/updates/2018/03/clipboardapi "Unblocking Clipboard Access  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">clipboard</span> <span class="jser-tag">WebPlatformAPI</span></p>

Async Clipboard APIについての紹介。
今まで`document.execCommand`でやっていたものをちゃんとしたPermissionモデルと共に扱えるAPIについて


----

## Data visualization with react-vis – DailyJS – Medium
[medium.com/dailyjs/data-visualization-with-react-vis-bd2587fe1660](https://medium.com/dailyjs/data-visualization-with-react-vis-bd2587fe1660 "Data visualization with react-vis – DailyJS – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

react-visを使ったグラフの描画について


----

## webpack 4 の optimization.splitChunks（廃止されたCommonsChunkPluginの代わり） の使い方、使い所 - Qiita
[qiita.com/soarflat/items/1b5aa7163c087a91877d](https://qiita.com/soarflat/items/1b5aa7163c087a91877d "webpack 4 の optimization.splitChunks（廃止されたCommonsChunkPluginの代わり） の使い方、使い所 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack 4の`optimization`オプションについて。
`optimization.*`の設定とそれぞれの出力結果について


----

## Say Hello to Houdini and the CSS Paint API / Coder's Block
[codersblock.com/blog/say-hello-to-houdini-and-the-css-paint-api/](https://codersblock.com/blog/say-hello-to-houdini-and-the-css-paint-api/ "Say Hello to Houdini and the CSS Paint API / Coder's Block")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Paint APIについての記事。
Paint Workletを使ったスタイルの拡張の書き方やスタイルの適応方法について。
また現時点でのCSS Paint APIを含めたHoudiniについて


----

## Redruco: Truco para aprender Redux (Parte 1) – Javier Fernandes – Medium
[medium.com/@javierfernandes/redruco-truco-para-aprender-redux-parte-1-c72d052576b0](https://medium.com/@javierfernandes/redruco-truco-para-aprender-redux-parte-1-c72d052576b0 "Redruco: Truco para aprender Redux (Parte 1) – Javier Fernandes – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React/Reduxを使ったアプリケーション開発についての連載。
Reduxが必要となる状態はどのようなケースか、また開発においてもアプリの状態とUIの詳細は独立して考えられることについて。
Storybookでコンポーネントを確認しながら開発し、アプリを作るチュートリアル。


----

## #SmooshGate FAQ  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/smooshgate](https://developers.google.com/web/updates/2018/03/smooshgate "#SmooshGate FAQ  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TC39</span></p>

ECMAScriptで`Array.prototype.flatten` Proposalが既存のMooToolsなどのライブラリと名前がバッティングするためbreak the webとなる問題について。
標準化する実装と異なる点だけではなく、prototypeを列挙している点にも問題がある。
また、なぜ既存の実装を変更しても解決にならないかや今後について。


----

## Strongly Typed Event Emitters – Brian Terlson – Medium
[medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8](https://medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8 "Strongly Typed Event Emitters – Brian Terlson – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 2.8(RC)のConditional Typeを使ったEventEmitterの型付けについて

- [bterlson/strict-event-emitter-types: A type-only library for strongly typing any event emitter](https://github.com/bterlson/strict-event-emitter-types "bterlson/strict-event-emitter-types: A type-only library for strongly typing any event emitter")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## nucleartide/emberconf-2018: EmberConf 2018 notes.
[github.com/nucleartide/emberconf-2018](https://github.com/nucleartide/emberconf-2018 "nucleartide/emberconf-2018: EmberConf 2018 notes.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

EmberConf 2018の動画や発表のまとめ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Everyone can now run JavaScript on Cloudflare with Workers
[blog.cloudflare.com/cloudflare-workers-unleashed/](https://blog.cloudflare.com/cloudflare-workers-unleashed/ "Everyone can now run JavaScript on Cloudflare with Workers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cdn</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">webservice</span></p>

Cloudflare Workersが一般公開された。
CDN上でService Workerと同じようなAPIで処理を書くことができるサービス。


----

## FromJS - Understand JavaScript Apps
[www.fromjs.com/](http://www.fromjs.com/ "FromJS - Understand JavaScript Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">DOM</span> <span class="jser-tag">Extension</span> <span class="jser-tag">babel</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

DOMをインスペクトし、表示されている文字列がコードのどこで生成されているかを検索できるChrome拡張。 既存のHTMLを生成するDOM APIを上書きしトレースしている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## vuex-orm/vuex-orm: The Vuex plugin to enable Object-Relational Mapping access to the Vuex Store.
[github.com/vuex-orm/vuex-orm](https://github.com/vuex-orm/vuex-orm "vuex-orm/vuex-orm: The Vuex plugin to enable Object-Relational Mapping access to the Vuex Store.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Vuex</span> <span class="jser-tag">ORM</span></p>

複雑なデータ構造を扱うためのVuexプラグイン。リレーションを持ったデータをノーマライズし、RailsやLaravelのようなORMライクなAPIでデータの検索、取得ができる。複雑にネストしたデータ構造をノーマライズすることで、データを扱うコストを一定に保つことが目的。

- [Vuexでリレーションを持った複雑なデータ構造を上手く扱うには - Qiita](https://qiita.com/kiaking/items/bcd5360fb3106cf22a81 "Vuexでリレーションを持った複雑なデータ構造を上手く扱うには - Qiita")
- [paularmstrong/normalizr: Normalizes nested JSON according to a schema](https://github.com/paularmstrong/normalizr "paularmstrong/normalizr: Normalizes nested JSON according to a schema")

----

## maticzav/emma-cli: 📦 Terminal assistant to find and install node packages.
[github.com/maticzav/emma-cli](https://github.com/maticzav/emma-cli "maticzav/emma-cli: 📦 Terminal assistant to find and install node packages.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">検索</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npmモジュールの検索とインストールを行うツール


----

## terkelg/prompts: Lightweight, beautiful and user-friendly interactive prompts
[github.com/terkelg/prompts](https://github.com/terkelg/prompts "terkelg/prompts: Lightweight, beautiful and user-friendly interactive prompts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span></p>

Node.jsでインタラクティブなプロンプトを表示するライブラリ


----
