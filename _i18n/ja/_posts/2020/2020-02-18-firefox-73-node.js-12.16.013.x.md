---
title: "2020-02-18のJS: Firefox 73、Node.js 12.16.0(13.xからのバックポート)"
author: "azu"
layout: post
date : 2020-02-18T01:52:14.927Z
category: JSer
tags:
- Firefox
- Node.js

---

JSer.info #475 - Firefox 73がリリースされました。

- [Firefox 73 is upon us - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/02/firefox-73-is-upon-us/)
- [Firefox 73.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/73.0/releasenotes/ "Firefox 73.0, See All New Features, Updates and Fixes")
- [Firefox 73 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/73 "Firefox 73 for developers - Mozilla | MDN")
- [Firefox 73 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/versions/73/ "Firefox 73 Site Compatibility | Firefox Site Compatibility")

Formのvalidationを行ってからsubmitする[HTMLFormElement.requestSubmit()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit)をフラグ付きでサポート、CSSの[overscroll-behavior-block](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior-block)と[overscroll-behavior-inline](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior-inline)をサポート。

開発者ツールのコンソールで、次のように`%c`でのスタイル指定にbackground imageを指定できるようになりました。

```js
console.log('%c Firefox',`
color: red; padding: 2px 2px 2px 20px; background: no-repeat  url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAARCAMAAADjcdz2AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAHRUExURQAAADQT0/+iBf9KEgCC/v0mLf04JuU+Lv8tK/8yJv90BP4rK8wMZv/NHtIQX9gZT/QgN+IbTf6XBf5QHv+tAPmnFvpuGv/mP//bOP7pSv3tVv/0FQCO/NopOsMGbvJPMscLaMUAaO0dQfk2J/giNd0WVLsDev9yD8QIbroDd9sVVP11HuceP/5fFughPv6ND//nPv+4G//ZM/+8JP+zCv/PLf/eOdZAY//qAP7hQ/3sMf7vRgA9yEdc3ABp+hKA/ZS2zv+MAACF/8aKqcPOo/9XGf89I/8hQPgfO/98CP+tAP+WAP60AP7MAOISZe4YWe0gQ/+BAP/AAv9SAItCav/8T//kLwBF1Px/H//vBwBf7fhTLv9PHf8oMvYdRv+ZDP9cAP9PFs1TTeFSQf/FEP/uPv/SJ/G3J/VJIbFpX6hEXF1Dif/pQ5+Lg1xyuvu8AAAAu85oYJlOYuRHKgAAlP+RAL1aowBX4U4rmFt/1EhBnZBzlf/1WSoYhv/8Otx9eXN/8piPwwBk8QA8uX5jojBUy/OOHjyO/7rSx1ly5gCX/wCS8Chx8ftvOip79pF4q16T5SGL++5uUtyOkPPUSwBz/+vaW513wp+7vgBO421lv+OTuBwAAABFdFJOUwAF/gv+/P0C/f785uEFxX37M/z9VP3+7Pf7/f79Pn9hYBbHsub0Vq+gXJ6kqf588IjiFPC2rl7fGPp4sKYkaI13/or6+26KYjUAAAESSURBVBjTY2BgZ2BnZAABKwsgmwGMGWzt7J0c6qyZwRxBPUab8ob2rg7pGgkRBl4GBv4A87J6ZxYZF2mpUHFmoAodjmAux04WmRmRUpKhBkAdHpzCERG9kyd2T4uUzBE3YtByZ3P1LJ00nYVlwpQwy1QzBj53TlextllRPX1TG30lwkwZeDw4M4ormsNnRjVV5gelGTPwxXGwBRdWtfS3huf5+qQYMmj4s7oBDfHyqS7I9RUNMmHQ9BPgSEzOKqotyU73YfISYWDkCQAqSQoJyRT1YmLSB7pMzU+A1S2BK7DUW0goXhvkOTl/Dw42YV0xrkBPdV6wdxVU3WM53WJco+UZoAGgyK+kws2tLMvAzs4AAPERO0Rc4hCeAAAAAElFTkSuQmCC')`);
```

その他の利用できるスタイルについては次のドキュメントにまとめられています。

- https://developer.mozilla.org/en-US/docs/Web/API/Console#Styling_console_output

----

Node.js 12.16.0がリリースされました。

- [Node v12.16.0 (LTS) | Node.js](https://nodejs.org/en/blog/release/v12.16.0/)

このLTSバージョンの更新では、開発版であるNode 13.xからのバックポートが色々と含まれています。
次の機能がExperimental APIとしてNode.js 12.16.0にバックポートされています。

- [Node v13.6.0](https://nodejs.org/en/blog/release/v13.6.0/)で実装された[`assert.match()`](https://nodejs.org/api/assert.html#assert_assert_match_string_regexp_message)と[`assert.doesNotMatch()`](https://nodejs.org/api/assert.html#assert_assert_doesnotmatch_string_regexp_message)
- [Node v13.4.0](https://nodejs.org/en/blog/release/v13.4.0/)で実装された`EventEmitter`の[`captureRejections`](https://nodejs.org/api/events.html#events_events_capturerejections)オプション
- [Node v13.3.0](https://nodejs.org/en/blog/release/v13.3.0/)で実装された`wasi`コアモジュール

また、同じようにNode 13.xから次のAPIがStable APIとしてNode.js 12.16.0にバックポートされています

- [`EventEmitter.on`](https://nodejs.org/api/events.html#events_events_on_emitter_eventname)
- [`EventEmitter.errorMonitor`](https://nodejs.org/api/events.html#events_eventemitter_errormonitor)
- [`--trace-exit`](https://nodejs.org/api/cli.html#cli_trace_exit) CLIフラグ
- [`--trace-uncaught`](https://nodejs.org/api/cli.html#cli_trace_uncaught) CLIフラグ
- `child_process`と`cluster`の[`{ serialization: "advanced" }`](https://nodejs.org/api/child_process.html#child_process_advanced_serialization)オプション

その他では[perf_hooks](https://nodejs.org/api/perf_hooks.html)モジュールがStable APIとなっています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v12.16.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.16.0/](https://nodejs.org/en/blog/release/v12.16.0/ "Node v12.16.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Node 12.16.0リリース。
実験的な機能として`assert.match`と`assert.doesNotMatch`の追加。
`child_process`が`serialization`オプションをサポート、`--trace-exit`、`--trace-uncaught`の追加、`perf_hooks`がStable APIとなるなど。


----

## Chromium Blog: Chrome 81: Near Field Communications, Augmented Reality, and More
[blog.chromium.org/2020/02/chrome-81-near-field-communications.html](https://blog.chromium.org/2020/02/chrome-81-near-field-communications.html "Chromium Blog: Chrome 81: Near Field Communications, Augmented Reality, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 81 ベータリリース。
Original Trialとしてモバイル向けのWeb NFC、`scheduler.postTask`のサポート、Mixed Contentの自動アップグレード、TLS 1.0と1.1の削除など


----

## Announcing Ionic 5! | The Ionic Blog
[ionicframework.com/blog/announcing-ionic-5/](https://ionicframework.com/blog/announcing-ionic-5/ "Announcing Ionic 5! | The Ionic Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ionic 5リリース。
iOS 13に合わせたデザインの更新、Ionic Animationsの追加、Ioniconsの更新、Angular 9のIvyへの対応

- [Introducing Ionic Animations | The Ionic Blog](https://blog.ionicframework.com/introducing-ionic-animations/ "Introducing Ionic Animations | The Ionic Blog")

----

## Release v2.0 · FullHuman/purgecss
[github.com/FullHuman/purgecss/releases/tag/v2.0.5](https://github.com/FullHuman/purgecss/releases/tag/v2.0.5 "Release v2.0 · FullHuman/purgecss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

使われてないCSSを削除するPurgeCSS 2.0.0リリース。
非同期化、CSS Variablesの対応、Node.js 8以下のサポート終了

- [PurgeCSS 2.0 - Full Human - Medium](https://medium.com/full-human/purgecss-2-0-c0e812e6c4f6 "PurgeCSS 2.0 - Full Human - Medium")

----
<h1 class="site-genre">アーティクル</h1>

----

## Firefox 73 is upon us - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/02/firefox-73-is-upon-us/](https://hacks.mozilla.org/2020/02/firefox-73-is-upon-us/ "Firefox 73 is upon us - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 73リリース。
フラグ付きでHTMLFormElementに`requestSubmit`メソッドの追加、開発者ツールのコンソールのスタイルでbackground imageをサポート、DNS over HTTPSのプロバイダーにNextDNSを追加

- [Firefox 73.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/73.0/releasenotes/ "Firefox 73.0, See All New Features, Updates and Fixes")
- [Firefox 73 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/73 "Firefox 73 for developers - Mozilla | MDN")
- [Firefox 73 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/versions/73/ "Firefox 73 Site Compatibility | Firefox Site Compatibility")

----

## Adding notification permission data to the Chrome User Experience Report
[developers.google.com/web/updates/2020/02/notification-permission-data-in-crux](https://developers.google.com/web/updates/2020/02/notification-permission-data-in-crux "Adding notification permission data to the Chrome User Experience Report")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome User Experience Reportに通知許諾ダイアログのデータが追加された


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 最新のブラウザで変わるCookieの取り扱いやPrivacyの考え方 - Speaker Deck
[speakerdeck.com/yosuke\_furukawa/zui-xin-falseburauzadebian-warucookiefalsequ-rixi-iyaprivacyfalsekao-efang](https://speakerdeck.com/yosuke_furukawa/zui-xin-falseburauzadebian-warucookiefalsequ-rixi-iyaprivacyfalsekao-efang "最新のブラウザで変わるCookieの取り扱いやPrivacyの考え方 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">privacy</span> <span class="jser-tag">slide</span></p>

ブラウザのサードパーティクッキーやトラッキング防止周りの機能についてのスライド。
SafariのITP、FIrefoxのETP、SameSite Cookie。
CNAME CloakingやSafariの提案しているAd click attribution、ChromeのPrivacy Sandboxについてなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## OpenChakra
[openchakra.app/](https://openchakra.app/ "OpenChakra")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">GUI</span> <span class="jser-tag">editor</span></p>

Chakra UIを使ったサイトを構築できるビジュアルエディタ。D&Dでコンポーネントを組み立てでき、その結果をCodeSandboxにコードとして出力できる。

- [Chakra UI | Design System built with React](https://chakra-ui.com/ "Chakra UI | Design System built with React")

----

## Chakra UI | Design System built with React
[chakra-ui.com/](https://chakra-ui.com/ "Chakra UI | Design System built with React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">WAI-ARIA</span></p>

Reactを使ったUIコンポーネントライブラリ。
一貫性のある組み合わせが可能なコンポーネントを作ることを目的としていて、WAI-ARIAの対応、テーマ機能などを持っている。


----

## evanw/esbuild: An extremely fast JavaScript bundler and minifier
[github.com/evanw/esbuild](https://github.com/evanw/esbuild "evanw/esbuild: An extremely fast JavaScript bundler and minifier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">golang</span> <span class="jser-tag">bundler</span></p>

Go言語製のJavaScript Bundler。
CommonJS/ES Modules、Source Map、Minifier、JSXなどに対応している


----

## volument/baretest: An extremely fast and simple JavaScript test runner.
[github.com/volument/baretest](https://github.com/volument/baretest "volument/baretest: An extremely fast and simple JavaScript test runner.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

自己実行可能なテストフレームワーク。
`test`関数といくつかのライフサイクルを提供する小さなテストフレームワーク。

- [Baretest — An extremely minimalistic alternative to Jest](https://volument.com/baretest "Baretest — An extremely minimalistic alternative to Jest")

----

## Mirage JS • An API mocking library for frontend developers
[miragejs.com/](https://miragejs.com/ "Mirage JS • An API mocking library for frontend developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

APIモッキングライブラリ。
ブラウザで動くサーバを実装し、リクエストに対するレスポンスを定義できる。
`fetch`や`XMLHttpRequest`をインターセプトすることで実装している。


----

## FullCalendar - JavaScript Event Calendar
[fullcalendar.io/](https://fullcalendar.io/ "FullCalendar - JavaScript Event Calendar")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

カレンダーUIライブラリ。


----
