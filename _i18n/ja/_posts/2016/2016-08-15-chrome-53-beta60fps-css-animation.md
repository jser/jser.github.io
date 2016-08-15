---
title: "2016-08-15のJS: Chrome 53 Beta、使わなくて良いイディオム、60FPS CSS Animation"
author: azu
layout: post
date : 2016-08-15T10:17
category: JSer
tags:
    - Chrome
    - ES5
    - CSS
    - animation

---

JSer.info #292

----
<h1 class="site-genre">ヘッドライン</h1>

----

## The State of Vue — The Vue Point — Medium
[medium.com/the-vue-point/the-state-of-vue-1655e10a340a](https://medium.com/the-vue-point/the-state-of-vue-1655e10a340a "The State of Vue — The Vue Point — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.0.0 RC1リリース。
APIはフリーズされたため、正式リリースまでにAPIはもう変更しないとのこと

- [Release v2.0.0-rc.1 · vuejs/vue](https://github.com/vuejs/vue/releases/tag/v2.0.0-rc.1 "Release v2.0.0-rc.1 · vuejs/vue")

----

## ESLint v3.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/08/eslint-v3.3.0-released](http://eslint.org/blog/2016/08/eslint-v3.3.0-released "ESLint v3.3.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.3.0リリース。
実体と名前が合ってないルールをリネーム(元ルールは非推奨)、新しいルールとして`no-template-curly-in-string`と`sort-keys`の追加など

- [ESLint v3.3.0 - Qiita](http://qiita.com/mysticatea/items/adf6ef3c63b35c01fc05 "ESLint v3.3.0 - Qiita")

----

## Chromium Blog: Chrome 53 Beta: Shadow DOM, PaymentRequest, and Android autoplay
[blog.chromium.org/2016/08/chrome-53-beta-shadow-dom.html](http://blog.chromium.org/2016/08/chrome-53-beta-shadow-dom.html "Chromium Blog: Chrome 53 Beta: Shadow DOM, PaymentRequest, and Android autoplay")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 53βリリース。
Shadow DOM v1、PaymentRequest APIのサポート、Video要素は`muted`なら`autoplay`で自動再生が可能に、`allow-presentation`の対応。
HTTP/0.9が非推奨に、TextEncoderは常にutf-8を使うようなるなど

- [Payment Request APIを試す - mmag](http://joe-noh.hatenablog.com/entry/2016/08/08/213159 "Payment Request APIを試す - mmag")
- [Muted autoplay on mobile: say goodbye to &amp;lt;canvas&amp;gt; hacks and animated GIFs! | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/07/autoplay "Muted autoplay on mobile: say goodbye to &amp;lt;canvas&amp;gt; hacks and animated GIFs! | Web Updates - Google Developers")

----

## Google Chrome Blog: Flash and Chrome
[chrome.googleblog.com/2016/08/flash-and-chrome.html](https://chrome.googleblog.com/2016/08/flash-and-chrome.html "Google Chrome Blog: Flash and Chrome")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chrome 53でトラッキング用の小さなFlashをブロック。
Chrome 55で全てのFlashがデフォルトブロックとなり、初回アクセス時に許可を求めるダイアログがでる形

----

## Angular 2 RC5 - NgModules, Lazy Loading and AoT compilation
[angularjs.blogspot.com/2016/08/angular-2-rc5-ngmodules-lazy-loading.html](http://angularjs.blogspot.com/2016/08/angular-2-rc5-ngmodules-lazy-loading.html "Angular 2 RC5 - NgModules, Lazy Loading and AoT compilation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2 RC5リリース。
`@NgModule`のサポートなど

- [RC4 to RC5 Migration - ts](https://angular.io/docs/ts/latest/cookbook/rc4-to-rc5.html)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md)


----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing #EdgeBug: File web platform bugs with a Tweet | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/08/11/edgebug-twitter/](https://blogs.windows.com/msedgedev/2016/08/11/edgebug-twitter/ "Introducing #EdgeBug: File web platform bugs with a Tweet | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">issue</span></p>

Twitterで #EdgeBug のハッシュタグ経由でIssueを作成できるように

----

## API Deprecations and Removals in Chrome 53 | Web Updates - Google Developers
[developers.google.com/web/updates/2016/08/chrome-53-deprecations](https://developers.google.com/web/updates/2016/08/chrome-53-deprecations "API Deprecations and Removals in Chrome 53 | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 53で非推奨/削除されたAPIについて。
また非推奨となるプロセスとポリシーについて

----

## Make your JavaScript code shine: knockout old ES5 hacks
[rainsoft.io/make-your-javascript-code-shide-knockout-old-es5-hack/](https://rainsoft.io/make-your-javascript-code-shide-knockout-old-es5-hack/ "Make your JavaScript code shine: knockout old ES5 hacks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

ES2015で導入された機能や構文で代替できるため、既に使わなくても良くなったES5のイディオムについて

----

## Developer Edition 50: Console, Memory Tool, Net Monitor and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/08/developer-edition-50-console-memory-tool-net-monitor-and-more/](https://hacks.mozilla.org/2016/08/developer-edition-50-console-memory-tool-net-monitor-and-more/ "Developer Edition 50: Console, Memory Tool, Net Monitor and more ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firefox 50の開発者ツールについて。
コンソールにSource Mapを適応した行数の表示、HTTPログのコールスタックに対応、メモリツールがデフォルトで有効に、WebAssemblyのシンタックスハイライトに対応など

----

## 従来のWebアプリの常識を変える! Service WorkerがもたらすWebの未来 | PLAID Engineer Blog
[tech.plaid.co.jp/cong-lai-nowebapurinochang-shi-wobian-eru-service-workergamotarasuwebnowei-lai/](http://tech.plaid.co.jp/cong-lai-nowebapurinochang-shi-wobian-eru-service-workergamotarasuwebnowei-lai/ "従来のWebアプリの常識を変える! Service WorkerがもたらすWebの未来 | PLAID Engineer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">JavaScript</span></p>

ServiceWorkerがどういうものかという概要的な話。

----

## Offline Google Analytics Made Easy | Web Updates - Google Developers
[developers.google.com/web/updates/2016/07/offline-google-analytics](https://developers.google.com/web/updates/2016/07/offline-google-analytics "Offline Google Analytics Made Easy | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">google</span> <span class="jser-tag">アクセス解析</span> <span class="jser-tag">ServiceWorker</span></p>

Service Workerを使ったGoogle Analyticsのオフライン対応について

- [GoogleChrome/sw-helpers: Service Worker helper libraries](https://github.com/googlechrome/sw-helpers "GoogleChrome/sw-helpers: Service Worker helper libraries")

----

## SVG 2 new features · w3c/svgwg Wiki
[github.com/w3c/svgwg/wiki/SVG-2-new-features](https://github.com/w3c/svgwg/wiki/SVG-2-new-features "SVG 2 new features · w3c/svgwg Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span></p>

SVG 2の新しい機能や変更点について

----

## Smooth as Butter: Achieving 60 FPS Animations with CSS3 — OutSystems Experts — Medium
[medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-css3-db7b98610108](https://medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-css3-db7b98610108 "Smooth as Butter: Achieving 60 FPS Animations with CSS3 — OutSystems Experts — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">performance</span></p>

CSSアニメーションの60FPS出すまでをステップバイステップで見ていく話。
スライドメニューを、position、transform、will-change、クラスの付け外しでそれぞれFPSにどのような変化があるかを見る

----

## flexboxのバグに立ち向かう（flexboxバグまとめ） - Qiita
[qiita.com/hashrock/items/189db03021b0f565ae27](http://qiita.com/hashrock/items/189db03021b0f565ae27 "flexboxのバグに立ち向かう（flexboxバグまとめ） - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">issue</span></p>

CSS flexboxのバグについてスクリーンショットと共に紹介してる

- [luisrudge/postcss-flexbugs-fixes: PostCSS plugin that tries to fix all of flexbug&amp;#39;s issues](https://github.com/luisrudge/postcss-flexbugs-fixes "luisrudge/postcss-flexbugs-fixes: PostCSS plugin that tries to fix all of flexbug&amp;#39;s issues")
- [philipwalton/flexbugs: A community-curated list of flexbox issues and cross-browser workarounds for them.](https://github.com/philipwalton/flexbugs "philipwalton/flexbugs: A community-curated list of flexbox issues and cross-browser workarounds for them.")

----

## What is Promise.try, and why does it matter? - joepie91&#x27;s Ramblings
[cryto.net/%7Ejoepie91/blog/2016/05/11/what-is-promise-try-and-why-does-it-matter/](http://cryto.net/%7Ejoepie91/blog/2016/05/11/what-is-promise-try-and-why-does-it-matter/ "What is Promise.try, and why does it matter? - joepie91's Ramblings")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

`Promise.try`のユースケースについて。
ECMAScript標準ではないが、`Promise.try`があることで同期的なエラーが扱いやすくなるという話

- [ljharb/proposal-promise-try: ECMAScript Proposal, specs, and reference implementation for Promise.try](https://github.com/ljharb/proposal-promise-try "ljharb/proposal-promise-try: ECMAScript Proposal, specs, and reference implementation for Promise.try")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## permission.site
[permission.site/](https://permission.site/ "permission.site")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span></p>

HTTPSやパーミッションが必要なブラウザのAPIを試せるサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## zalando/tailor: A streaming layout service for front-end microservices
[github.com/zalando/tailor](https://github.com/zalando/tailor "zalando/tailor: A streaming layout service for front-end microservices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTML</span></p>

layout service libray for front-end

- [Better streaming layouts for front-end microservices with Tailor - O&amp;#39;Reilly Media](https://www.oreilly.com/ideas/better-streaming-layouts-for-frontend-microservices-with-tailor "Better streaming layouts for front-end microservices with Tailor - O&amp;#39;Reilly Media")

----

## js-joda/js-joda: :clock2: Immutable date and time library for javascript
[github.com/js-joda/js-joda](https://github.com/js-joda/js-joda "js-joda/js-joda: :clock2: Immutable date and time library for javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JSR-310/Joda timeのAPIをインスパイアした日付ライブラリ。

----
<h1 class="site-genre">書籍関係</h1>

----

## Introduction · React Enlightenment [DRAFT]
[www.reactenlightenment.com/](http://www.reactenlightenment.com/ "Introduction · React Enlightenment \[DRAFT\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Reactについての電子書籍
開眼JavaScriptのシリーズ。

- [FrontendMasters/react-enlightenment: A thoughtful and complete introduction to React.](https://github.com/FrontendMasters/react-enlightenment "FrontendMasters/react-enlightenment: A thoughtful and complete introduction to React.")

----

## Manning | RxJS in Action
[www.manning.com/books/rxjs-in-action](https://www.manning.com/books/rxjs-in-action "Manning | RxJS in Action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

2017年3月31日発売
RxJSについての書籍

----
