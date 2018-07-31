---
title: "2018-07-31のJS: TypeScript 3.0、Chrome 68、Vueの内部技術"
author: "azu"
layout: post
date : 2018-07-31T00:34:34.373Z
category: JSer
tags:
- typescript
- chrome
- Vue

---

JSer.info #394 - TypeScript 3.0が正式にリリースされました。

- [Announcing TypeScript 3.0 | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/07/30/announcing-typescript-3-0/)
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What's-new-in-TypeScript#typescript-30)
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-30)

monorepoなどで複数パッケージ間のビルド関係などを扱うProject referencesの追加、Generic rest parametersのサポート、Tuple型の改善、`unknown`型の追加、Reactの`defaultProps`の型のサポートなどが行われています。

次の記事でも具体的な動作について説明されているので合わせてみてみるといいかもしれません。

- [TypeScript 3.0.0-RC 変更点 - Qiita](https://qiita.com/vvakame/items/57a0559c45b88b2ae168)

----

Chrome 68がリリースされました。

- [New in Chrome 68  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/07/nic68)
- [Chrome Releases: Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2018/07/stable-channel-update-for-desktop.html "Chrome Releases: Stable Channel Update for Desktop")
- [Chromium Blog: Chrome 68 Beta: add to home screen, payment handler, page lifecycle](https://blog.chromium.org/2018/06/chrome-68-beta-add-to-home-screen.html "Chromium Blog: Chrome 68 Beta: add to home screen, payment handler, page lifecycle")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D68 "Chrome Platform Status")

Chrome 68から`http://`なサイトの場合にアドレスバーには"Not Secure"（保護されていない通信）の表示がでるようになりました。
逆に`https://`のアドレスバーの表示が控えめになっていくなど、徐々にHTTPSがデフォルトとなるような表示に変化していく予定です。

- [Google Online Security Blog: A secure web is here to stay](https://security.googleblog.com/2018/02/a-secure-web-is-here-to-stay.html)
- [Chromium Blog: Evolving Chrome's security indicators](https://blog.chromium.org/2018/05/evolving-chromes-security-indicators.html)

また、Chrome 68ではPage Lifecycle APIのサポート、`customElements.upgrade()`のサポート、Service WorkerにおけるHTTPキャッシュのデフォルトの挙動を変更などが行われています。

Page Lifecycle API、`fetch` APIの[`keepalive`](https://fetch.spec.whatwg.org/#keep-alive-flag)オプション、`navigator.sendBeacon`などが揃ってきたこともあり、将来的にChromeではページを閉じる際に同期的なXHR（ログ送信などに利用されていた）を使えなくする予定があります。

- [Intent to Implement & Ship: Disallow Sync XHR in Page Dismissal - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/LnqwTCiT9Gs/tO0IBO4PAwAJ)
- [Page Lifecycle API  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/07/page-lifecycle-api)
- [Logging Activity With The Web Beacon API — Smashing Magazine](https://www.smashingmagazine.com/2018/07/logging-activity-web-beacon-api/)

----

[Vue技术内幕](http://hcysun.me/vue-design/)というサイトではVue.js本体のコード解説をしています。
中国語で書かれていてまだ書き途中の部分もありますが、ディレクトリ構造、オプションや初期化処理、リアクティブシステムの実装、テンプレートのパースとコンパイルの仕組み、Virtual DOMについてなどに書かれています。

コード解説なのでコードの動きを中心に解説されていて、特にテンプレートの処理周りの解説はかなり細かい印象です。
Vue.jsのコード自体に興味がある人は読んでみると面白いかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Prettier 1.14: YAML Support · Prettier
[prettier.io/blog/2018/07/29/1.14.0.html](https://prettier.io/blog/2018/07/29/1.14.0.html "Prettier 1.14: YAML Support · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 1.14リリース。
YAMLのサポート、Front matterをサポート、`requirePragma`と`requirePragma`を各言語でサポート、CJK処理を改善してパフォーマンスの改善など


----

## Angular v6.1 Now Available — TypeScript 2.9, Scroll Positioning, and more
[blog.angular.io/angular-v6-1-now-available-typescript-2-9-scroll-positioning-and-more-9f1c03007bb6](https://blog.angular.io/angular-v6-1-now-available-typescript-2-9-scroll-positioning-and-more-9f1c03007bb6 "Angular v6.1 Now Available — TypeScript 2.9, Scroll Positioning, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v6.1リリース。
ルーターの`scrollPositionRestoration`オプションでスクロール位置の保存に対応、TypeScript 2.9サポートなど


----

## Announcing the Ionic 4 Beta | The Official Ionic Blog
[blog.ionicframework.com/announcing-ionic-4-beta/](https://blog.ionicframework.com/announcing-ionic-4-beta/ "Announcing the Ionic 4 Beta | The Official Ionic Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

クロスプラットフォームアプリ開発フレームワークのIonic 4 Betaリリース。


----

## Announcing TypeScript 3.0 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/07/30/announcing-typescript-3-0/](https://blogs.msdn.microsoft.com/typescript/2018/07/30/announcing-typescript-3-0/ "Announcing TypeScript 3.0 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.0リリース。
Project references、可変長引数にGenerics型パラメータを適応できるように、Tuple型の改善、`unknown`型の追加、Reactの`defaultProps`の型のサポートなど

- [TypeScript 3.0.0-RC 変更点 - Qiita](https://qiita.com/vvakame/items/57a0559c45b88b2ae168 "TypeScript 3.0.0-RC 変更点 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## New in Chrome 68  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/07/nic68](https://developers.google.com/web/updates/2018/07/nic68 "New in Chrome 68  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 68リリース。
HTTPなサイトにはNot Secureの表示がでるように。
Page Lifecycle APIのサポート、`customElements.upgrade()`のサポート、Service WorkerにおけるHTTPキャッシュのデフォルトの挙動を変更など

- [Chrome Releases: Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2018/07/stable-channel-update-for-desktop.html "Chrome Releases: Stable Channel Update for Desktop")
- [Chromium Blog: Chrome 68 Beta: add to home screen, payment handler, page lifecycle](https://blog.chromium.org/2018/06/chrome-68-beta-add-to-home-screen.html "Chromium Blog: Chrome 68 Beta: add to home screen, payment handler, page lifecycle")
- [Fresher service workers, by default  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/06/fresher-sw "Fresher service workers, by default  |  Web  |  Google Developers")

----

## Page Lifecycle API  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/07/page-lifecycle-api](https://developers.google.com/web/updates/2018/07/page-lifecycle-api "Page Lifecycle API  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">WebPlatformAPI</span></p>

Page Lifecycle APIについての解説。
ウェブページにライフサイクルの概念を導入する。`visibilitychange`など既存のイベントや新しく追加された`freeze`、`resume`などイベントの紹介、ライフサイクルにおけるStateについてを解説している。


----

## A one year PWA retrospective – Pinterest Engineering – Medium
[medium.com/@Pinterest\_Engineering/a-one-year-pwa-retrospective-f4a2f4129e05](https://medium.com/@Pinterest_Engineering/a-one-year-pwa-retrospective-f4a2f4129e05 "A one year PWA retrospective – Pinterest Engineering – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">article</span></p>

PinterestのモバイルサイトのPWA化についてのタイムライン。
ログインユーザーからログアウトユーザーへの適応、GestaltとUIレイアウト、bundleサイズについてなど


----

## time-travel.md
[gist.github.com/jasonLaster/1e220992c294a571dd9b59abd084ccf2](https://gist.github.com/jasonLaster/1e220992c294a571dd9b59abd084ccf2 "time-travel.md")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">firefox</span> <span class="jser-tag">article</span></p>

FirefoxのNightlyに入ったWebReplayの使い方や機能について。 一連の操作や状態を保存してブレークポイントからの状態をもどしていったり、リプレイできるデバッグ機能。バグの再現とデバッグなどに利用できる。


----

## Redux vs. The React Context API
[daveceddia.com/context-api-vs-redux/](https://daveceddia.com/context-api-vs-redux/ "Redux vs. The React Context API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Contextの使い方や動作についての解説。Reduxでのステート管理との違いやContextはReduxを置き換えるものではない点についてなど


----

## Removing Babel's Stage Presets · Babel
[babeljs.io/blog/2018/07/27/removing-babels-stage-presets](https://babeljs.io/blog/2018/07/27/removing-babels-stage-presets "Removing Babel's Stage Presets · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babel 7では`babel-preset-stage-0`のようなStage Presetを公開しないことについて。
Stage Presetを削除することにした背景やProposalへのフィードバックについて。


----

## Logging Activity With The Web Beacon API — Smashing Magazine
[www.smashingmagazine.com/2018/07/logging-activity-web-beacon-api/](https://www.smashingmagazine.com/2018/07/logging-activity-web-beacon-api/ "Logging Activity With The Web Beacon API — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`navigator.sendBeacon`を使ってページを離脱する前にログを送信する方法について。
またGDPRやDNTの対応について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## thedaviddias/Front-End-Performance-Checklist: 🎮 The only Front-End Performance Checklist that runs faster than the others
[github.com/thedaviddias/Front-End-Performance-Checklist](https://github.com/thedaviddias/Front-End-Performance-Checklist "thedaviddias/Front-End-Performance-Checklist: 🎮 The only Front-End Performance Checklist that runs faster than the others")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">document</span></p>

フロントエンドのパフォーマンスチェックリスト


----

## perf-tools/performance at master · artifact-project/perf-tools
[github.com/artifact-project/perf-tools/tree/master/performance](https://github.com/artifact-project/perf-tools/tree/master/performance "perf-tools/performance at master · artifact-project/perf-tools")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span></p>

User Timing APIのpolyfillライブラリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## cozmo/jsQR: A pure javascript QR code reading library. This library takes in raw images and will locate, extract and parse any QR code found within.
[github.com/cozmo/jsQR](https://github.com/cozmo/jsQR "cozmo/jsQR: A pure javascript QR code reading library. This library takes in raw images and will locate, extract and parse any QR code found within.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存がないQRコードリーダライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Vue技术内幕
[hcysun.me/vue-design/](http://hcysun.me/vue-design/ "Vue技术内幕")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ebook</span></p>

Vue.jsのソースコードを解説する電子書籍。
ディレクトリ構造、オプションや初期化処理、リアクティブシステムの実装、テンプレートのパースとジェネレートの仕組み、Virtual DOMについてなど


----
