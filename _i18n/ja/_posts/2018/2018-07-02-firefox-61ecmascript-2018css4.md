---
title: "2018-07-02のJS: Firefox 61、ECMAScript 2018リリース、CSS4はどこにある？"
author: "azu"
layout: post
date : 2018-07-02T22:40:14.980Z
category: JSer
tags:
- firefox
- ECMAScript
- CSS

---

JSer.info #390 - Firefox 61がリリースされました。

- [Firefox — Notes (61.0) — Mozilla](https://www.mozilla.org/en-US/firefox/61.0/releasenotes/ "Firefox — Notes (61.0) — Mozilla")
- [Firefox 61 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/61 "Firefox 61 for developers - Mozilla | MDN")
- [Firefox 61 サイト互換性情報 | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/versions/61/ "Firefox 61 サイト互換性情報 | Firefox サイト互換性情報")


TLS 1.3のサポートをデフォルトで有効化、アクセシビリティインスペクタの実装、
`PerformanceServerTiming`のサポートなどが行われています。

AvastやAVGを使っている場合にTLS 1.3での接続に問題が出るケースもあるようです。

- [1468892 - SSL_ERROR_RX_RECORD_TOO_LONG with Avast intercepting TLS 1.3 connections](https://bugzilla.mozilla.org/show_bug.cgi?id=1468892)

またFetch APIの`credentials`のデフォルト値を`omit`から`same-origin`に変更する仕様への追従が行われています。

- [Make fetch() use "same-origin" credentials by default by annevk · Pull Request #585 · whatwg/fetch](https://github.com/whatwg/fetch/pull/585)

same-originに対するXHRのデフォルトの挙動とFetch APIのデフォルトの挙動が異なったため（Fetchではクッキーを渡さないなど）、XHRからFetch APIにシームレスな切り替えができないという混乱を生んでいたため、仕様が変更されました。

その他では、Touch系のイベントがChromeと同様にデフォルトで`passive`となるように変更されています。

- [モバイル上のスクロールを高速化するため、タッチイベントリスナーが標準でパッシブとなりました | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2018/touch-event-listeners-are-now-passive-by-default-making-scrolling-faster-on-mobile/)
- [Making touch scrolling fast by default  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/01/scrolling-intervention)

----

[2018年6月27日のEcma GA（総会）](http://www.ecma-international.org/news/index.html)でECMAScript 2018が正式に承認されリリースされました。

- [Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm)

ECMAScriptはLiving Standardであるため最新版は[GitHub](https://tc39.github.io/ecma262/)に公開されており、[ES2018のスナップショット](https://tc39.github.io/ecma262/2018/)も公開されています。

- [ECMAScript · JavaScriptの入門書 #jsprimer](https://asciidwango.github.io/js-primer/basic/ecmascript/ "ECMAScript · JavaScriptの入門書 #jsprimer")
- [ECMAScriptの仕様/プロポーザルの調べ方を知る | Web Scratch](https://efcl.info/2018/03/07/ecmascript-usage/)

ES2018で入ったプロポーザルについては次の記事などで紹介されています。
Object Rest/Spread Properties、Async Iteration、`Promise#finally`、正規表現の拡張などが含まれています。

- [JavaScript: What’s new in ECMAScript 2018 (ES2018)?](https://medium.com/front-end-hacking/javascript-whats-new-in-ecmascript-2018-es2018-17ede97f36d5)
- [Exploring ES2018 and ES2019](http://exploringjs.com/es2018-es2019/index.html)

----

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jtmkk6odggs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

[Where is CSS4? When is it coming out?](https://www.youtube.com/watch?v=Jtmkk6odggs)という動画でCSS4はなぜないのかについてをわかりやすく解説しています。


CSS3のときに仕様がModuleへ分解され、それぞれのModuleはLevel 3となりました。（全体をCSS3と呼んでいました）
その後のCSSの仕様はModuleごとにLevelをあげる(CSS Selectors Level 4になるなど)、また新しく追加されたModuleはLevel 1から開始するという形になっています。
そのため、CSS4という全体を表すものはないという話がされています。

次の記事も合わせて読むと良さそうです。

- [Why there is no CSS4 - explaining CSS Levels](https://rachelandrew.co.uk/archives/2016/09/13/why-there-is-no-css4-explaining-css-levels/)
- [Levels, snapshots, modules…](https://www.w3.org/Style/2011/CSS-process)

現在のCSS moduleのLevelやステータスについては次のページにまとめられています。

- [CSS current work & how to participate](https://www.w3.org/Style/CSS/current-work)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox — Notes (61.0) — Mozilla
[www.mozilla.org/en-US/firefox/61.0/releasenotes/](https://www.mozilla.org/en-US/firefox/61.0/releasenotes/ "Firefox — Notes (61.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 61.0リリース。
TLS 1.3のドラフトサポートをデフォルトで有効化、アクセシビリティインスペクタの実装。
`PerformanceServerTiming`のサポート、Fetch APIの`credentials`のデフォルト値を`same-origin`に変更、WebVRがmacOSで有効化など

- [Firefox 61 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/61 "Firefox 61 for developers - Mozilla | MDN")

----

## Dev.Opera — What’s new in Chromium 67 and Opera 54
[dev.opera.com/blog/opera-54/](https://dev.opera.com/blog/opera-54/ "Dev.Opera — What’s new in Chromium 67 and Opera 54")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 54 (based on Chromium 67)リリース。
Generic Sensors、Custom Elementが既存のHTML Elementを拡張できるように、Stream APIがtransformをサポートなど


----

## lighthouse/changelog.md at v3.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/blob/v3.0.0/changelog.md](https://github.com/GoogleChrome/lighthouse/blob/v3.0.0/changelog.md "lighthouse/changelog.md at v3.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 3.0リリース。
レポートUIの変更、それぞれのスコアのWeightの変更、First Contentful Paintの追加、RTTのコスト表示の追加など。

- [Announcing Lighthouse 3.0  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/05/lighthouse3 "Announcing Lighthouse 3.0  |  Web  |  Google Developers")

----

## Ecma latest news
[www.ecma-international.org/news/index.html](http://www.ecma-international.org/news/index.html "Ecma latest news")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

ECMA-262 9th edition - ECMAScript® 2018リリース

- [ECMAScript® 2018 Language Specification](https://www.ecma-international.org/ecma-262/9.0/ "ECMAScript® 2018 Language Specification")

----
<h1 class="site-genre">アーティクル</h1>

----

## E2EテストをPhantomJSから、Puppeteer + Headless Chromeへ移行しました - LCL Engineers' Blog
[techblog.lclco.com/entry/2018/06/28/080000](http://techblog.lclco.com/entry/2018/06/28/080000 "E2EテストをPhantomJSから、Puppeteer + Headless Chromeへ移行しました - LCL Engineers' Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Capybara + PhantomJSで行っていたテストを、Puppeteer + Headless Chromeに移行していくという話。
Puppeteerの機能紹介やデバッグ方法について。


----

## Web Performance Checklist – ITNEXT
[itnext.io/web-performance-checklist-6b616f3c6f0d](https://itnext.io/web-performance-checklist-6b616f3c6f0d "Web Performance Checklist – ITNEXT")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ウェブアプリにおけるパフォーマンスのチェック項目のまとめ。
最適化のアプローチについての概要まとめ


----

## Making Web Components Work | Mixpanel Engineering
[engineering.mixpanel.com/2018/06/12/making-web-components-work/](https://engineering.mixpanel.com/2018/06/12/making-web-components-work/ "Making Web Components Work | Mixpanel Engineering")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span></p>

Web Componentsを使って作ったパネルコンポーネントについての記事。
snabbdomを使ったVirtual DOMを使い描画し、Web Conponentsでのステート管理についてなど。


----

## AudioWorklet Design Pattern  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/06/audio-worklet-design-pattern](https://developers.google.com/web/updates/2018/06/audio-worklet-design-pattern "AudioWorklet Design Pattern  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">article</span></p>

AudioWorkletのデザインパターンについて。
WebAssembly、SharedArrayBufferとの組み合わせての利用についてなど


----

## Introduction to Feature Policy  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/06/feature-policy](https://developers.google.com/web/updates/2018/06/feature-policy "Introduction to Feature Policy  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">CSP</span></p>

Feature Policyについて。
CSPはセキュリティのコントールをし、Feature Policyは機能に対してのコントールをする点について。
Feature Policyの指定方法やどのようなときに使うべきかについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Where is CSS4? When is it coming out? - YouTube
[www.youtube.com/watch?v&#x3D;Jtmkk6odggs](https://www.youtube.com/watch?v=Jtmkk6odggs "Where is CSS4? When is it coming out? - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">spec</span> <span class="jser-tag">video</span></p>

CSS4はどこにあるのという問いに対する説明の動画。
CSS3のときに仕様がmoduleに分解され、それぞれのModuleはLevel 3となった。
その後のSpecはModuleごとにLevelをあげ、また新しく追加されたModuleはLevel 1から開始する。
そのためCSS4という全体を表すものはないという話。


----

## Vue.js プロジェクトの爆発させかた #ichigayageek / How to explosion Vue.js project - Speaker Deck
[speakerdeck.com/potato4d/how-to-explosion-vue-dot-js-project](https://speakerdeck.com/potato4d/how-to-explosion-vue-dot-js-project "Vue.js プロジェクトの爆発させかた #ichigayageek / How to explosion Vue.js project - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">slide</span></p>

Vueを使ったプロジェクトで遭遇する問題についてのスライド。
規模が大きくなってきたときのステートの管理方法、デザイナーとの協業、既存のウェブアプリへの部分的な適応、別のテンプレートエンジンとの組み合わせなどについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## wg-effectiveness/process\_jp.md at master · w3c/wg-effectiveness
[github.com/w3c/wg-effectiveness/blob/master/process\_jp.md](https://github.com/w3c/wg-effectiveness/blob/master/process_jp.md "wg-effectiveness/process\_jp.md at master · w3c/wg-effectiveness")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">spec</span> <span class="jser-tag">翻訳</span></p>

"忙しい人のためのW3Cプロセス入門"
W3C Process for Busy Peopleの日本語訳


----

## kay-is/react-from-zero: A simple (99% ES2015 less) tutorial for React
[github.com/kay-is/react-from-zero](https://github.com/kay-is/react-from-zero "kay-is/react-from-zero: A simple (99% ES2015 less) tutorial for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

Reactを一から学ぶチュートリアル。
ブラウザだけで動くReactのコードを見ながら、Reactについてを解説している。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Swiip/compo: 🎼Compo·sing Web Compo·nents
[github.com/Swiip/compo](https://github.com/Swiip/compo "Swiip/compo: 🎼Compo·sing Web Compo·nents")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

WebComponentでUIを作成するための関数を提供するライブラリ。

- [Announcing: compo – Matthieu Lux (@Swiip) – Medium](https://medium.com/@Swiip_51904/announcing-compo-3ba9e15890a7 "Announcing: compo – Matthieu Lux (@Swiip) – Medium")

----

## mizchi/trans-loader: webpack-less frontend with service-worker
[github.com/mizchi/trans-loader](https://github.com/mizchi/trans-loader "mizchi/trans-loader: webpack-less frontend with service-worker")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">babel</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Service Workerを使ってBabelやTypeScriptでの変換を行うスクリプト。
npmのモジュールをjspm.ioを使ってロードできる。

- [trans-loader: node/webpack なしではじめるフロントエンドプロジェクト - Qiita](https://qiita.com/mizchi/items/796a5c392d306a44a918 "trans-loader: node/webpack なしではじめるフロントエンドプロジェクト - Qiita")
- [jspm.io - Native ES Modules CDN](https://jspm.io/ "jspm.io - Native ES Modules CDN")

----

## kitze/JSUI: A powerful UI toolkit for managing JavaScript apps
[github.com/kitze/JSUI](https://github.com/kitze/JSUI "kitze/JSUI: A powerful UI toolkit for managing JavaScript apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">GUI</span> <span class="jser-tag">project</span></p>

JavaScriptのプロジェクト管理GUI。
GUIでアプリの作成、プロジェクトのダッシュボード、タスクの実行などができる


----
