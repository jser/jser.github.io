---
title: "2016-06-13のJS: jQuery 3.0、Firefox 47.0、Web Audio API入門"
author: azu
layout: post
date : 2016-06-13T15:30
category: JSer
tags:
    - Firefox
    - jQuery
    - WebAudioAPI

---

JSer.info #283 - [jQuery 3.0](http://blog.jquery.com/2016/06/09/jquery-3-0-final-released/ "jQuery 3.0")が正式にリリースされました。

幾つかの非互換性が含まれていますが、jQuery 1.xや2.xからアップグレードする場合のドキュメントも公開されています。
基本的には[jQuery Migrate](https://github.com/jquery/jquery-migrate "jQuery Migrate")という移行用のプラグインを入れて、警告を修正したら本体をアップグレードする流れになっています。

- [jQuery Core 3.0 Upgrade Guide | jQuery](http://jquery.com/upgrade-guide/3.0/ "jQuery Core 3.0 Upgrade Guide | jQuery")
- [【翻訳まとめ】jQuery 3.0 アップグレードガイド - Qiita](http://qiita.com/fmy/items/345a264a1cf2e2a73f62)

また、今回のjQuery 3リリースと同時に、`ajax`と`effect`を取り除いたslimビルドが公開されています。

----

[Firefox 47](https://www.mozilla.jp/firefox/47.0/releasenotes/ "Firefox 47")がリリースされました。

Widevine CDM(DMRなストリーミング)のサポート、Service Worker/Push APIのデバッグ機能の改善、 `about:debugging`の追加、ES2017の` Object.values()`と`Object.entries()`の実装など

開発者ツール周りは次の記事で解説されています。

- [Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/ "Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog")

----

[web audio lesson](http://mohayonao.github.io/web-audio-lesson/ "web audio lesson")では、Web Audio APIについて基本的な話から応用な話までをレッスン方式で解説されています。

- [web-audio-lesson : Web Audio API初学者向けのテキストを書きました - 音の鳴るブログ](http://mohayonao.hatenablog.com/entry/2016/06/12/154735 "web-audio-lesson : Web Audio API初学者向けのテキストを書きました - 音の鳴るブログ")

オンライン上でコードをそのまま実行できるようになっていて、それぞれのレッスンごとに課題が設定されています。
Web Audio APIに興味がある人は見てみるといいかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## jQuery 3.0 Final Released! | Official jQuery Blog
[blog.jquery.com/2016/06/09/jquery-3-0-final-released/](http://blog.jquery.com/2016/06/09/jquery-3-0-final-released/ "jQuery 3.0 Final Released! | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.0リリース。
ajaxとeffectを取り除いたslimビルドの公開。
`jQuery.Deferred`がPromise A/+互換に、非推奨イベントの削除、再度`requestAnimationFrame`を利用するように変更など

- [jQuery Core 3.0 Upgrade Guide | jQuery](http://jquery.com/upgrade-guide/3.0/ "jQuery Core 3.0 Upgrade Guide | jQuery")
- [jquery/jquery-migrate: APIs and features removed from jQuery core](https://github.com/jquery/jquery-migrate#migrate-older-jquery-code-to-jquery-30 "jquery/jquery-migrate: APIs and features removed from jQuery core")
- [【翻訳まとめ】jQuery 3.0 アップグレードガイド - Qiita](http://qiita.com/fmy/items/345a264a1cf2e2a73f62 "【翻訳まとめ】jQuery 3.0 アップグレードガイド - Qiita")

----

## Firefox 47.0 リリースノート
[www.mozilla.jp/firefox/47.0/releasenotes/](https://www.mozilla.jp/firefox/47.0/releasenotes/ "Firefox 47.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 47リリース。
Widevine CDM(DMRなストリーミング)のサポート、Service Worker/Push APIのデバッグ機能の改善、 `about:debugging`の追加、ES2017の` Object.values()`と`Object.entries()`の実装など

- [Mozilla To Test Widevine CDM in Firefox Nightly | Future Releases](https://blog.mozilla.org/futurereleases/2016/04/08/mozilla-to-test-widevine-cdm-in-firefox-nightly/ "Mozilla To Test Widevine CDM in Firefox Nightly | Future Releases")
- [Firefox 47 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/47 "Firefox 47 for developers - Mozilla | MDN")
- [Firefox 47 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/47/ "Firefox 47 サイト互換性情報 | Firefox サイト互換性情報")
- [Firefox 47 がリリース、CSS Mask Image プロパティへの対応やVP9サポートの有効化など | WWW WATCH](https://hyper-text.org/archives/2016/06/firefox_47_release.shtml "Firefox 47 がリリース、CSS Mask Image プロパティへの対応やVP9サポートの有効化など | WWW WATCH")

----

## Release v6.10.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.10.0](https://github.com/babel/babel/releases/tag/v6.10.0 "Release v6.10.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.10.0リリース。
`--watch`時に、初回はビルドしない`--skip-initial-build`オプションの追加、バグ修正など

----

## ESLint v2.12.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/06/eslint-v2.12.0-released](http://eslint.org/blog/2016/06/eslint-v2.12.0-released "ESLint v2.12.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.12.0リリース。
JSCS互換のルールの追加、全てのビルトインルールを読み込む`eslint:all`の追加、パフォーマンスの改善など

- [Utilize glob ignore option for massive perf win by samccone · Pull Request #6215 · eslint/eslint](https://github.com/eslint/eslint/pull/6215 "Utilize glob ignore option for massive perf win by samccone · Pull Request #6215 · eslint/eslint")
- [ESLint v2.12.0 - Qiita](http://qiita.com/mysticatea/items/7bf844b32f8295eeb061 "ESLint v2.12.0 - Qiita")

----

## Release Notes for Safari Technology Preview 6 | WebKit
[webkit.org/blog/6531/release-notes-for-safari-technology-preview-6/](https://webkit.org/blog/6531/release-notes-for-safari-technology-preview-6/ "Release Notes for Safari Technology Preview 6 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 6リリース。
関数の引数におけるtrailing commasのドラフトをサポート、CSSの`normal`値をサポートなど

- [Trailing Commas in Function Param Lists](https://jeffmo.github.io/es-trailing-function-commas/ "Trailing Commas in Function Param Lists")

----

## Dev.Opera — What’s new in Chromium 51 and Opera 38
[dev.opera.com/blog/opera-38/](https://dev.opera.com/blog/opera-38/ "Dev.Opera — What’s new in Chromium 51 and Opera 38")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 38(based on Chromium 51)リリース。
ES6 `Symbol.hasInstance`、`Symbol.species`、関数式の`fn.name`対応、`querySelector`の返り値がiterableに、`KeyboardEvent#key`のサポートなど

----

## Chromium Blog: Chrome 52 Beta: CSS containment, simpler performance measurement, streamable responses from service workers, and more options for web push
[blog.chromium.org/2016/06/chrome-52-beta-css-containment-simpler.html](http://blog.chromium.org/2016/06/chrome-52-beta-css-containment-simpler.html "Chromium Blog: Chrome 52 Beta: CSS containment, simpler performance measurement, streamable responses from service workers, and more options for web push")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 52 Betaリリース。
CSS `contain`プロパティ、`PerformanceObserver`のサポート。
Fetch APIがreferrer policyをサポート。
metaタグでの`X-Frame-Option`が無効となるなど

- [CSS Containment in Chrome 52 | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/06/css-containment "CSS Containment in Chrome 52 | Web Updates - Google Developers")
- [Fetch Referrer Policy Sample](https://googlechrome.github.io/samples/fetch-api/fetch-referrer-policy.html "Fetch Referrer Policy Sample")
- [CSS Containment Module Level 3 （日本語訳）](https://triple-underscore.github.io/css-containment-ja.html "CSS Containment Module Level 3 （日本語訳）")

----
<h1 class="site-genre">アーティクル</h1>

----

## Open Sourcing CloudFlare’s UI Framework
[blog.cloudflare.com/cf-ui/](http://blog.cloudflare.com/cf-ui/ "Open Sourcing CloudFlare’s UI Framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

小さなReact Componentをmonorepoで管理して公開する話。
コンポーネントの粒度、テスト方法、デバッグ、アクセシビリティなどについて

----

## DOM Features You Didn’t Know Existed (Video &amp; Slides) | Impressive Webs
[www.impressivewebs.com/dom-features-you-didnt-know-existed-video-slides/](https://www.impressivewebs.com/dom-features-you-didnt-know-existed-video-slides/ "DOM Features You Didn’t Know Existed (Video & Slides) | Impressive Webs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

いろんなDOM APIについて紹介してる記事

----

## Passive Event Listeners によるスクロールの改善 | blog.jxck.io
[blog.jxck.io/entries/2016-06-09/passive-event-listeners.html](https://blog.jxck.io/entries/2016-06-09/passive-event-listeners.html "Passive Event Listeners によるスクロールの改善 | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

`addEventListener(type, handler, options)`の第三引数として追加されてた `passive`オプションについて。
`passive: true` とした場合の効果、Feature detectの方法についてなど

- [addEventListener()の第３引数の意味とかをちゃんと理解する為のメモ - 今日もスミマセン。](http://d.hatena.ne.jp/snaka72/20100925/1285404467 "addEventListener()の第３引数の意味とかをちゃんと理解する為のメモ - 今日もスミマセン。")
- [Add feature test for passive event listener support · Issue #1894 · Modernizr/Modernizr](https://github.com/Modernizr/Modernizr/issues/1894 "Add feature test for passive event listener support · Issue #1894 · Modernizr/Modernizr")

----

## Performance Observer - Efficient Access to Performance Data | Web Updates - Google Developers
[developers.google.com/web/updates/2016/06/performance-observer](https://developers.google.com/web/updates/2016/06/performance-observer "Performance Observer - Efficient Access to Performance Data | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">API</span> <span class="jser-tag">performance</span></p>

`PerformanceObserver`についての解説記事。
ブラウザがアイドル時に、非同期でTiming情報を取る事ができる。

----

## Memory Debugging with Web Inspector | WebKit
[webkit.org/blog/6425/memory-debugging-with-web-inspector/](https://webkit.org/blog/6425/memory-debugging-with-web-inspector/ "Memory Debugging with Web Inspector | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">debug</span></p>

Safari TPの新しいメモリプロファイラについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Practical React with MobX - YouTube
[www.youtube.com/watch?v=XGwuM\_u7UeQ](https://www.youtube.com/watch?v=XGwuM_u7UeQ "Practical React with MobX - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span> <span class="jser-tag">library</span></p>

MobXについてのスクリーンキャスト。
MobXを使ってどのようにStateを管理するのか、どのようなサイクルで状態の変更を描画するのかについて

- [mobxjs/mobx: Simple, scalable state management.](https://github.com/mobxjs/mobx "mobxjs/mobx: Simple, scalable state management.")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## web audio lesson
[mohayonao.github.io/web-audio-lesson/](http://mohayonao.github.io/web-audio-lesson/ "web audio lesson")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

Web Audio APIの基礎から応用までの課題付きチュートリアル。
コードをその場で実行できるようになっている。

- [web-audio-lesson : Web Audio API初学者向けのテキストを書きました - 音の鳴るブログ](http://mohayonao.hatenablog.com/entry/2016/06/12/154735 "web-audio-lesson : Web Audio API初学者向けのテキストを書きました - 音の鳴るブログ")

----

## npms
[npms.io/](https://npms.io/ "npms")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">検索</span></p>

バックエンドにElasticsearchを使ったnpm検索サービス。
Quality、Maintenance、Popularity、Personalities(未実装)という指標も一緒に表示してくれる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## airbnb/hypernova: A service for server-side rendering your JavaScript views
[github.com/airbnb/hypernova](https://github.com/airbnb/hypernova "airbnb/hypernova: A service for server-side rendering your JavaScript views")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">rails</span></p>

AirbnbのReactサーバサイドレンダリングモジュール。
Railsとの統合する設定も公開されている

----

## Kakapo.js
[devlucky.github.io/kakapo-js](http://devlucky.github.io/kakapo-js "Kakapo.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

HTTPモックライブラリ。
モックデータ入りの開発サーバを作れるライブラリ。

----

## rill-js/rill: Isomorphic web application framework.
[github.com/rill-js/rill](https://github.com/rill-js/rill "rill-js/rill: Isomorphic web application framework.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

Browser、Node.jsで動くisomorphicなHTTPミドルウェアライブラリ。

----

## benjamn/reify: Enable ECMAScript 2015 modules in Node today. No caveats. Full stop.
[github.com/benjamn/reify](https://github.com/benjamn/reify "benjamn/reify: Enable ECMAScript 2015 modules in Node today. No caveats. Full stop.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

ECMAScript moduleをNode.jsに変換/ランタイム変換するツール。

----
<h1 class="site-genre">書籍関係</h1>

----

## CSSシークレット ―ウェブデザイナーが知るべき47のキーポイント : Lea Verou, 牧野 聡 : 本 : Amazon.co.jp
[www.amazon.co.jp/CSS%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88-%E2%80%95%E3%82%A6%E3%82%A7%E3%83%96%E3%83%87%E3%82%B6%E3%82%A4%E3%83%8A%E3%83%BC%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D47%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-Lea-Verou/dp/4873117666](http://www.amazon.co.jp/CSS%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88-%E2%80%95%E3%82%A6%E3%82%A7%E3%83%96%E3%83%87%E3%82%B6%E3%82%A4%E3%83%8A%E3%83%BC%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D47%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-Lea-Verou/dp/4873117666 "CSSシークレット ―ウェブデザイナーが知るべき47のキーポイント : Lea Verou, 牧野 聡 : 本 : Amazon.co.jp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2016年6月25日発売
CSS Secretsの翻訳

- [CSS Secrets - O&amp;#39;Reilly Media](http://shop.oreilly.com/product/0636920031123.do "CSS Secrets - O&amp;#39;Reilly Media")

----
