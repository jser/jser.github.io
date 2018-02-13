---
title: "2018-02-13のJS: Inferno v4、SafariでのService Worker、Eloquent JavaScript第三版"
author: "azu"
layout: post
date : 2018-02-13T02:04:48.927Z
category: JSer
tags:
- React
- inferno
- Safari
- book

---

JSer.info #370 - ReactライクなAPIをもつInferno v4がリリースされました。

- [Release Inferno v4 · infernojs/inferno](https://github.com/infernojs/inferno/releases/tag/v4.0.2 "Release Inferno v4 · infernojs/inferno")

`Inferno.createPortal`の追加、[inferno-router](https://github.com/infernojs/inferno/tree/master/packages/inferno-router "inferno-router")がReact Router v4相当に、MobxやReduxとの連携の更新などが行われています。
主にモジュール分割の破壊的な変更もあり、その詳細は次のマイグレーションガイドにまとめられています。

- [inferno/v4-migration.md at master · infernojs/inferno](https://github.com/infernojs/inferno/blob/master/docs/v4-migration.md "inferno/v4-migration.md at master · infernojs/inferno")

----

[Workers at Your Service | WebKit](https://webkit.org/blog/8090/workers-at-your-service/ "Workers at Your Service | WebKit")という記事では、[Safari 11.1](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_11_1.html "Safari 11.1")(beta)に実装されたService Workerについて解説されています。

仕様的な面やSafariでの実装、キャッシュの保存場所や削除方法について書かれています。
Safari 11.1では数週間利用されていないService Workerやキャッシュが自動的に削除される、キャッシュサイズは50MB/partitionに制限されている点などについても書かれています。

また、[PWAs are coming to iOS 11.3: Cupertino, we have a problem](https://medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea "PWAs are coming to iOS 11.3: Cupertino, we have a problem")という別の記事では、Safariと他のブラウザとの実装が異なる点や、ホームスクリーンアプリとした時のWeb App Manifestの対応、注意点についても書かれています。

----

[Eloquent JavaScript](https://eloquentjavascript.net/3rd_edition/ "Eloquent JavaScript")の第三版のドラフト版が公開されました。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">You&#39;re all invited to read the full draft of Eloquent JavaScript&#39;s 3rd edition: <a href="https://t.co/8M5hp5awU2">https://t.co/8M5hp5awU2</a><br><br>Finishing touches are still ongoing, but this should be a readable text.</p>&mdash; Marijn Haverbeke (@MarijnJH) <a href="https://twitter.com/MarijnJH/status/958665332448784384?ref_src=twsrc%5Etfw">January 31, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

JavaScriptやプログラミングについてを学ぶ書籍です。
間違いやtypoを見つけた場合は[Issue](https://github.com/marijnh/Eloquent-JavaScript/issues)から報告できます。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## jest/CHANGELOG.md at v22.2.0 · facebook/jest
[github.com/facebook/jest/blob/v22.2.0/CHANGELOG.md](https://github.com/facebook/jest/blob/v22.2.0/CHANGELOG.md "jest/CHANGELOG.md at v22.2.0 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 22.2.0リリース。


----

## browserify/changelog.markdown at v16.0.0 · browserify/browserify
[github.com/browserify/browserify/blob/v16.0.0/changelog.markdown](https://github.com/browserify/browserify/blob/v16.0.0/changelog.markdown "browserify/changelog.markdown at v16.0.0 · browserify/browserify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 16.0.0リリース。
`--preserve-symlinks`のサポート、`events`のshimを更新、`--node`オプションを渡したときに`__dirname`と`__filename`を動的に設定するようになるなど


----

## Dev.Opera — What’s new in Chromium 64 and Opera 51
[dev.opera.com/blog/opera-51/](https://dev.opera.com/blog/opera-51/ "Dev.Opera — What’s new in Chromium 64 and Opera 51")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 51 (based on Chromium 64)リリース。
Resize Observer、`import.meta`、ES2018の正規表現の実装、AudioWorkletのフラグ付き実装など


----

## Release Notes for Safari Technology Preview 49 | WebKit
[webkit.org/blog/8088/release-notes-for-safari-technology-preview-49/](https://webkit.org/blog/8088/release-notes-for-safari-technology-preview-49/ "Release Notes for Safari Technology Preview 49 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 49リリース。
Service Worker、Fetchのバグ修正、ITPにデバッグモードを試験的に追加、Media Queryで`calc()`をサポート。
`String#trimStart`、json superset proposalの実装など

- [tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262](https://github.com/tc39/proposal-json-superset "tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262")

----

## Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API
[blog.chromium.org/2018/02/chrome-65-beta-css-paint-api-and.html](https://blog.chromium.org/2018/02/chrome-65-beta-css-paint-api-and.html "Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 65 Betaリリース。
CSS Paint API、Server Timing API、Feature-Policyの`sync-xhr`をサポート、TLS 1.3(draft-23)のサポートなど


----

## Eloquent JavaScript
[eloquentjavascript.net/3rd\_edition/](https://eloquentjavascript.net/3rd_edition/ "Eloquent JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">news</span></p>

Eloquent JavaScripの第3版が公開された


----

## CanJS 4.0
[www.bitovi.com/blog/canjs-4.0](https://www.bitovi.com/blog/canjs-4.0 "CanJS 4.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CanJS 4.0リリース。
デバッグツールの追加、テンプレートの記法を統一、ProxyとクラスベースのObservableオブジェクトの追加など


----

## Release Inferno v4 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v4.0.2](https://github.com/infernojs/inferno/releases/tag/v4.0.2 "Release Inferno v4 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v4リリース。
`Inferno.Component`は`inferno`パッケージに移動、`findDOMNode`は`inferno-compat`パッケージに移動。
`createPortal`のサポート、RouterがReact Router v4と同じAPIに変更、Mobx、Redux連携の更新、IE9+のサポートなど

- [inferno/v4-migration.md at master · infernojs/inferno](https://github.com/infernojs/inferno/blob/master/docs/v4-migration.md "inferno/v4-migration.md at master · infernojs/inferno")

----

## Echo JS on Twitter: "Echo JS, 2011-2018 - https://t.co/vEiEFdntF8"
[twitter.com/echojs/status/962996800738258945](https://twitter.com/echojs/status/962996800738258945 "Echo JS on Twitter: \"Echo JS, 2011-2018 - https://t.co/vEiEFdntF8\"")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

echojs.com が閉鎖された


----
<h1 class="site-genre">アーティクル</h1>

----

## なぜプロダクトに Vue.js を採用したのか? 運用してみてどうっだった? という話 | Nagisaのすゝめ
[blog.nagisa-inc.jp/archives/2980](https://blog.nagisa-inc.jp/archives/2980 "なぜプロダクトに Vue.js を採用したのか? 運用してみてどうっだった? という話 | Nagisaのすゝめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

Riotで作られていたサイトをVueでリニューアルした話。
Vueの特徴、ルータ、ステート管理、メリット、デメリットについて


----

## Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/](https://blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/ "Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">MS</span></p>

Microsoft StoreにPWAアプリを登録できるようになる。
また、BingでPWAアプリのクロールを行い一定の条件を満たしたものを表示する。

- [PWABuilder](https://www.pwabuilder.com/generator "PWABuilder")

----

## PWAs are coming to iOS 11.3: Cupertino, we have a problem
[medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea](https://medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea "PWAs are coming to iOS 11.3: Cupertino, we have a problem")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Safari 11.1で実装されたService Workerについて。
数週間使わてないService Workerは自動的に削除される点やWeb App Manifestのサポート、ホームスクリーンアプリとしての動作で注意する点などについて書かれている

- [Workers at Your Service | WebKit](https://webkit.org/blog/8090/workers-at-your-service/ "Workers at Your Service | WebKit")

----

## Introduction  |  Web Fundamentals  |  Google Developers
[developers.google.com/web/fundamentals/performance/webpack/](https://developers.google.com/web/fundamentals/performance/webpack/ "Introduction  |  Web Fundamentals  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpackを使った場合に置けるコードの最適化についての記事。
コード分割やキャッシュ、分析や計測などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Hygen
[www.hygen.io/](http://www.hygen.io/ "Hygen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

コードジェネレートツール。
テンプレートからコードを生成できる。
YAML Frontmatterでメタデータの定義、ejsでテンプレートの記述、特定の依存がある場合に動作するhook処理などを書ける


----

## Jake Archibald: In The Loop - JSConf.Asia 2018 - YouTube
[www.youtube.com/watch?v&#x3D;cCOL7MC4Pl0](https://www.youtube.com/watch?v=cCOL7MC4Pl0 "Jake Archibald: In The Loop - JSConf.Asia 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

ブラウザのイベントループについての発表。
`setTimeout`、`requestAnimationFrame`の違い。
イベントループとスタイルの変更の反映のタイミングについて。それぞれを可視化しながら解説している。
また、PromiseなどのMicroTaskとの処理順について


----

## JSConf.Asia 2018 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshFqN5dcZ704lxI3F5iHDYkl](http://www.youtube.com/playlist?list=PL37ZVnwpeshFqN5dcZ704lxI3F5iHDYkl "JSConf.Asia 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

JSConf.Asia 2018の動画が公開された

- [JSConf.Asia Singapore 2018](https://2018.jsconf.asia/ "JSConf.Asia Singapore 2018")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Assembly Studio
[webassembly.studio/](https://webassembly.studio/ "Web Assembly Studio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">editor</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

CなどでWebAssembly向けのコードを書いて、コンパイル実行できるエディタツール


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## thejameskyle/unstated: State that goes without saying
[github.com/thejameskyle/unstated](https://github.com/thejameskyle/unstated "thejameskyle/unstated: State that goes without saying")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

Reactの新しいContext APIを使ったステート管理ライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## VimeoSmashing Magazine
[vimeo.com/smashingmagazine](https://vimeo.com/smashingmagazine "VimeoSmashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span></p>

SmashingConf London 2018の動画が公開された


----
