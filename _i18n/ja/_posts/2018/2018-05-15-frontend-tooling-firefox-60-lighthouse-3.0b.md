---
title: "2018-05-15のJS: フロントエンドツールアンケート結果、Firefox 60、Lighthouse 3.0β"
author: "azu"
layout: post
date : 2018-05-15T01:33:11.228Z
category: JSer
tags:
- frontend
- firefox
- Lighthouse

---

JSer.info #383 - フロントエンドツールアンケート2018の結果が公開されています。

- [The Front-End Tooling Survey 2018 - Results - AshleyNolan.co.uk - Blog and Portfolio for Ashley Nolan](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results)

JavaScriptやCSSに関するツールやライブラリなどについてのアンケート結果をまとめたもので、[前回の結果](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2016-results)からの変化などについても掲載されています。

利用言語、ライブラリ、Lint、テスト、bundlerなどについて項目ごとのアンケート結果が公開されているので見てみると良さそうです。

----

Firefox 60.0がリリースされました。

- [Firefox — Notes (60.0) — Mozilla](https://www.mozilla.org/en-US/firefox/60.0/releasenotes/)
- [Firefox 60 – Modules and More – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/05/firefox-60-modules-and-more/ "Firefox 60 – Modules and More – Mozilla Hacks – the Web developer blog")
- [Firefox 60 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/60 "Firefox 60 for developers - Mozilla | MDN")

ES Modulesの有効化、[Same-Site Cookies](https://blog.mozilla.org/security/2018/04/24/same-site-cookies-in-firefox-60/)のサポート、`Array#values`の有効化、Web Authentication APIのサポート、WebVR APIがmacOSで有効化などが行われています。

ES ModulesはこれでIEを除くメジャーブラウザでサポートされたことになりました。

- [JavaScript modules via script tag](https://caniuse.com/#feat=es6-module)

また、[Firefox Quantum for Enterprise](https://www.mozilla.org/en-US/firefox/enterprise/)と名がついたエンタープライズ向けのESR(Extended Support Release)版もFirefox 60がベースとなっています。

- [Open for business: Firefox Quantum is ready for IT – Mozilla Tech – Medium](https://medium.com/mozilla-tech/open-for-business-firefox-quantum-is-ready-for-it-622c74fe13fe)

----

Lighthouse 3.0がプレリリースされ新しい機能について解説されています。

- [Announcing Lighthouse 3.0  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/05/lighthouse3)

レポートUIの変更、First Contentful Paintの追加、RTTのコスト表示の追加など。
その他の変更点として、スコアのWeightの変更、First InteractiveをFirst CPU Idleに名前の変更など指標が変更されています。

また、LightHouseの記録下内容をPerformanceタブで見るView Traceなどといった機能も追加されています。
この機能については次の発表動画でデモがおこなわれています。

- [What's new in Chrome DevTools (Google I/O '18) - YouTube](https://www.youtube.com/watch?v=mfuE53x4b3k)

Google I/Oの発表でもLighthouseを扱った内容は多いのであわせて見るとよさそうです。

- [Chrome and Web at Google I/O 2018 - YouTube - YouTube](https://www.youtube.com/playlist?list=PLNYkxOF6rcIC4NQeXpdAy0RbOACI66Hvf)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v10.1.0 (Current) | Node.js
[nodejs.org/en/blog/release/v10.1.0/](https://nodejs.org/en/blog/release/v10.1.0/ "Node v10.1.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v10.1.0リリース。
`require("fs/promises")`が`require("fs").promises`に変更、`request.aborted`プロパティの追加など


----

## Firefox — Notes (60.0) — Mozilla
[www.mozilla.org/en-US/firefox/60.0/releasenotes/](https://www.mozilla.org/en-US/firefox/60.0/releasenotes/ "Firefox — Notes (60.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 60.0リリース。
ES Modulesの有効化、`Array#values`の有効化、Web Authentication APIのサポート、WebVR APIがmacOSで有効化。
またESRのバージョンが60へ更新など。

- [Firefox 60 – Modules and More – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2018/05/firefox-60-modules-and-more/ "Firefox 60 – Modules and More – Mozilla Hacks – the Web developer blog")
- [Firefox 60 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/60 "Firefox 60 for developers - Mozilla | MDN")

----

## Video.js 7 is here! 🎉 | Video.js Blog
[blog.videojs.com/video-js-7-is-here/](http://blog.videojs.com/video-js-7-is-here/ "Video.js 7 is here! 🎉 | Video.js Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Video.js 7リリース。
Video.js HTTP Streaming (VHS)プラグインでHLSとDASHを試験的にサポート。
古いブラウザサポートのコードを削除、オプトアウトだったGoogle ANalyticsの収集を終了など


----

## Release v1.0.0 · webpack-contrib/webpack-serve
[github.com/webpack-contrib/webpack-serve/releases/tag/v1.0.0](https://github.com/webpack-contrib/webpack-serve/releases/tag/v1.0.0 "Release v1.0.0 · webpack-contrib/webpack-serve")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">debug</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

webpack-serve 1.0.0リリース。
`webpack-dev-server`の後継となるwebpack向けの開発サーバ


----

## Release v0.72.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.72.0](https://github.com/facebook/flow/releases/tag/v0.72.0 "Release v0.72.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

flow 0.72.0リリース。
`$Either<T>`, `$All<T>`, `$Type<T>`の廃止。
Language Server Protocolの改善、Stage 1のnullish coalescingをサポートなど


----

## The Front-End Tooling Survey 2018 - Results - AshleyNolan.co.uk - Blog and Portfolio for Ashley Nolan
[ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results "The Front-End Tooling Survey 2018 - Results - AshleyNolan.co.uk - Blog and Portfolio for Ashley Nolan")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">アンケート</span> <span class="jser-tag">news</span></p>

JavaScript、CSS、ツールなどについての開発者アンケート。 利用言語、ライブラリ、Lint、テスト、bundlerなどについて項目ごとのアンケート結果が公開されている


----
<h1 class="site-genre">アーティクル</h1>

----

## Using Lighthouse To Improve Page Load Performance  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/lighthouse](https://developers.google.com/web/updates/2018/05/lighthouse "Using Lighthouse To Improve Page Load Performance  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Lighthouseによって検出できるページロードパフォーマンスの問題について。
preloadした方がいいリソースの表示、JavaScriptのパースと実装の時間表示、リダイレクト検出、利用してないコード量の表示、preconnectによるRTTのコストの削減予測など


----

## The npm Blog — \`npm audit\`: identify and fix insecure...
[blog.npmjs.org/post/173719309445/npm-audit-identify-and-fix-insecure](https://blog.npmjs.org/post/173719309445/npm-audit-identify-and-fix-insecure "The npm Blog — \`npm audit\`: identify and fix insecure...")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

npm 6で入ったセキュリティチェックをする`npm audit`コマンドについての解説


----

## Introducing the Microsoft Edge DevTools Protocol - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2018/05/11/introducing-edge-devtools-protocol/#0b7zCRAl1ApIqZ6D.97](https://blogs.windows.com/msedgedev/2018/05/11/introducing-edge-devtools-protocol/#0b7zCRAl1ApIqZ6D.97 "Introducing the Microsoft Edge DevTools Protocol - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

リモートデバッグができるMicrosoft Edge DevTools Protocolの解説。


----

## 実践PWA：光る電卓「Llumino PWA」の開発と技術解説 - ここぽんのーと
[cocopon.me/blog/2018/05/pwa-llumino-dev/](https://cocopon.me/blog/2018/05/pwa-llumino-dev/ "実践PWA：光る電卓「Llumino PWA」の開発と技術解説 - ここぽんのーと")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ネイティブアプリだったものをPWAで再現する話。
CSSアニメーション、Service Worker、Web App Manifest、インタラクションについて


----

## Announcing Lighthouse 3.0  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/lighthouse3](https://developers.google.com/web/updates/2018/05/lighthouse3 "Announcing Lighthouse 3.0  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span> <span class="jser-tag">performance</span></p>

Lighthouse 3.0プレリリース。 レポートUIの変更、それぞれのスコアのWeightの変更、First Contentful Paintの追加、RTTのコスト表示の追加など。 その他の変更点としてFirst InteractiveをFirst CPU Idleに名前の変更など


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Google I/O 2018 - All Sessions - YouTube - YouTube
[www.youtube.com/playlist?list&#x3D;PLOU2XLYxmsIInFRc3M44HUTQc3b\_YJ4-Y](http://www.youtube.com/playlist?list=PLOU2XLYxmsIInFRc3M44HUTQc3b_YJ4-Y "Google I/O 2018 - All Sessions - YouTube - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span></p>

Google I/O 2018の動画まとめ


----

## TSConf 2018 - YouTube - YouTube
[www.youtube.com/playlist?list&#x3D;PL2z7rCjEG2ksF0rJ8Qwp1y5eTjqiPIRfT](https://www.youtube.com/playlist?list=PL2z7rCjEG2ksF0rJ8Qwp1y5eTjqiPIRfT "TSConf 2018 - YouTube - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

TSCong 2018の動画まとめ

- [TSConf 2018 | Seattle](https://tsconf.io/ "TSConf 2018 | Seattle")

----

## What's new in Chrome DevTools (Google I/O '18) - YouTube
[www.youtube.com/watch?v&#x3D;mfuE53x4b3k&amp;feature&#x3D;youtu.be](https://www.youtube.com/watch?v=mfuE53x4b3k&feature=youtu.be "What's new in Chrome DevTools (Google I/O '18) - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">video</span></p>

Chromeの開発者ツールの新しい機能について。
非同期処理やWorkerでのブレークポイントの改善、検索機能の改善、LightHouseのアップデートとView Traceのデモ、コンソールのEaget Evaluationのデモなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jspm.io - Native ES Modules CDN
[jspm.io/](https://jspm.io/ "jspm.io - Native ES Modules CDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

npmモジュールをES moduleとしてロードできるようにしてくれるCDNサービス。
CommonJSなモジュールはES moduleとして読み込めるように変換される。


----

## isomorphic-git/isomorphic-git: A pure JavaScript implementation of git for node and browsers!
[github.com/isomorphic-git/isomorphic-git](https://github.com/isomorphic-git/isomorphic-git "isomorphic-git/isomorphic-git: A pure JavaScript implementation of git for node and browsers!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">git</span> <span class="jser-tag">library</span></p>

Pure JavaScriptなGitの実装ライブラリ。
Node.jsとブラウザで動作する


----

## Nest - A progressive Node.js web framework
[nestjs.com/](https://nestjs.com/ "Nest - A progressive Node.js web framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

Node.jsのウェブフレームワーク。
TypeScriptで書かれていて、AngularのようにDecoratorを使った宣言的な記述を行う。


----

## jorgebucaran/classcat: JavaScript function for conditionally concatenating CSS classes.
[github.com/jorgebucaran/classcat](https://github.com/jorgebucaran/classcat "jorgebucaran/classcat: JavaScript function for conditionally concatenating CSS classes.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

CSSのクラス名文字列を結合したり、条件付きで消したりするライブラリ。


----
