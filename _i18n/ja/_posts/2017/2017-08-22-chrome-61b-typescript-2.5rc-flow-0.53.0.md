---
title: "2017-08-22のJS:  Chrome 61β、TypeScript 2.5RC、Flow 0.53.0"
author: "azu"
layout: post
date : 2017-08-22T02:00:59.401Z
category: JSer
tags:
- Chrome
- TypeScript
- Flow

---

JSer.info #345 - Chrome 61βがリリースされました。

- [Chromium Blog: Chrome 61 Beta: JavaScript modules, Payment Request API on desktop, Web Share API, and WebUSB](https://blog.chromium.org/2017/08/chrome-61-beta-javascript-modules.html "Chromium Blog: Chrome 61 Beta: JavaScript modules, Payment Request API on desktop, Web Share API, and WebUSB")

`<script type=module>`でES modulesを扱えるようになりました。
加えてPayment Request API](https://developers.google.com/web/fundamentals/discovery-and-monetization/payment-request/ "Payment Request API")や[Network Information API](https://googlechrome.github.io/samples/network-information/index.html "Network Information API")がデスクトップのChromeでも利用できるようになっています。
また、[Web Share API](https://developers.google.com/web/updates/2016/10/navigator-share "Web Share API")や[WebUSB API](https://developers.google.com/web/updates/2016/03/access-usb-devices-on-the-web "WebUSB API")、[Visual Viewport API](https://github.com/WICG/ViewportAPI "Visual Viewport API")、[Device Memory](https://github.com/WICG/device-memory "Device Memory")のサポートが追加されています。

既存の挙動の破壊的な変更としては、SEを使った動画はバックグラウンド時にVideo Trackが無効化されるようになっています。
セキュリティ対策として`\n`と`<`をそのまま含むHTTP(S)のURLへのリクエストがブロックされるようになっています。

- [Media Updates in Chrome 61  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/07/chrome-61-media-updates "Media Updates in Chrome 61  |  Web  |  Google Developers")
- [Prevent requests to HTTP(S) URLs containing raw `\n` and `<`. · Issue #546 · whatwg/fetch](https://github.com/whatwg/fetch/issues/546 "Prevent requests to HTTP(S) URLs containing raw `\n` and `&lt;`. · Issue #546 · whatwg/fetch")

----

[TypeScript 2.5 RC](https://blogs.msdn.microsoft.com/typescript/2017/08/17/announcing-typescript-2-5-rc/ "TypeScript 2.5 RC")がリリースされました。

現在ECMAScript ProposalでStage 3の[Optional catch binding](https://tc39.github.io/proposal-optional-catch-binding/ "Optional catch binding")がサポートされています。

```js
try {
   throw new Error("throw");
} catch {
   // errorを省略できる
}
```

- [ES proposal: optional catch binding](http://2ality.com/2017/08/optional-catch-binding.html "ES proposal: optional catch binding")

また今まではTypeScriptで書かれたモジュールを`npm link`すると定義が重複するという問題がありました。
[Workaround](https://github.com/Microsoft/TypeScript/issues/11107#issuecomment-254003380)はありますが、2.5Rではこの問題が修正されています。

- [Duplicate type declarations with npm link · Issue #6496 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/6496 "Duplicate type declarations with npm link · Issue #6496 · Microsoft/TypeScript")

----

Flow 0.53.0がリリースされました。

- [flow/Changelog.md at v0.53.0 · facebook/flow](https://github.com/facebook/flow/blob/v0.53.0/Changelog.md "flow/Changelog.md at v0.53.0 · facebook/flow")

Reactに対するFlowのモデルに破壊的な変更があるため、ReactでFlowを利用している場合はマイグレーションが必要です。
[flow-upgrade](https://yarnpkg.com/en/package/flow-upgrade "flow-upgrade")を使うことでマイグレーションが行えます。

また、Reactに対するutility typesが追加されています。

- [Type Reference | Flow](https://flow.org/en/docs/react/types/ "Type Reference | Flow")

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Node v8.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v8.4.0/](https://nodejs.org/en/blog/release/v8.4.0/ "Node v8.4.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v8.4.0リリース。
フラグ付きで`http2`をサポート、`util.format`がオブジェクトを扱う`%o`と`%O`をサポートなど


----

## Release 0.22.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v0.22.0](https://github.com/avajs/ava/releases/tag/v0.22.0 "Release 0.22.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 0.22.0リリース。
デフォルトのconcurrencyをCPUコア数に合わせるように、`t.log`の追加など


----

## Chromium Blog: Chrome 61 Beta: JavaScript modules, Payment Request API on desktop, Web Share API, and WebUSB
[blog.chromium.org/2017/08/chrome-61-beta-javascript-modules.html](https://blog.chromium.org/2017/08/chrome-61-beta-javascript-modules.html "Chromium Blog: Chrome 61 Beta: JavaScript modules, Payment Request API on desktop, Web Share API, and WebUSB")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrom 61βリリース。
`<script type=module>`のサポート、Payment Request API、Web Share API、WebUSB APIのサポート。
Expect-CT HTTP headerのサポート、HTTPリクエストURLに`>`や`\n`が含まれている場合にブロックするように

- [Expect-CT Extension for HTTP](http://httpwg.org/http-extensions/expect-ct.html "Expect-CT Extension for HTTP")
- [Prevent requests to HTTP(S) URLs containing raw \`
\` and \`&lt;\`. · Issue #546 · whatwg/fetch](https://github.com/whatwg/fetch/issues/546 "Prevent requests to HTTP(S) URLs containing raw \&#x60;
\&#x60; and \&#x60;&amp;lt;\&#x60;. · Issue #546 · whatwg/fetch")

----

## flow/Changelog.md at v0.53.0 · facebook/flow
[github.com/facebook/flow/blob/v0.53.0/Changelog.md](https://github.com/facebook/flow/blob/v0.53.0/Changelog.md "flow/Changelog.md at v0.53.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.53.0リリース。
Reactのモデルに対する型の改善。互換性のない変更も含まれるため`flow-upgrade`コマンドでマイグレーションできるようになっている

- [flow-upgrade | Yarn](https://yarnpkg.com/en/package/flow-upgrade "flow-upgrade | Yarn")

----

## Announcing TypeScript 2.5 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2017/08/17/announcing-typescript-2-5-rc/](https://blogs.msdn.microsoft.com/typescript/2017/08/17/announcing-typescript-2-5-rc/ "Announcing TypeScript 2.5 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.5 RCリリース。
現在ProposalのOptional catchのサポート、`npm link`などで定義が重複した場合にコンパイルエラーとなる問題を修正、`--preserveSymlinks`のサポートなど

- [Duplicate type declarations with npm link · Issue #6496 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/6496 "Duplicate type declarations with npm link · Issue #6496 · Microsoft/TypeScript")

----

## Release v6.0.0 · h5bp/html5-boilerplate
[github.com/h5bp/html5-boilerplate/releases/tag/6.0.0](https://github.com/h5bp/html5-boilerplate/releases/tag/6.0.0 "Release v6.0.0 · h5bp/html5-boilerplate")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">ReleaseNote</span></p>

html5-boilerplate 6.0.0リリース


----

## Release DOMPurify 1.0.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/1.0.0](https://github.com/cure53/DOMPurify/releases/tag/1.0.0 "Release DOMPurify 1.0.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

XSSサニタイズライブラリのDMOPurify 1.0.0リリース。
コードベースをES2015にし、rollupしたものを配布するように。バグ修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## Accessibility Testing with pa11y
[bitsofco.de/pa11y/](https://bitsofco.de/pa11y/ "Accessibility Testing with pa11y")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">article</span> <span class="jser-tag">Tools</span></p>

アクセシビリティテストツールのpa11yについての記事。
基本的な使い方について


----

## Rethinking drag and drop – Alex Reardon – Medium
[medium.com/@alexandereardon/rethinking-drag-and-drop-d9f5770b4e6b](https://medium.com/@alexandereardon/rethinking-drag-and-drop-d9f5770b4e6b "Rethinking drag and drop – Alex Reardon – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

React向けの縦横リストのD&Dライブラリであるreact-beautiful-dndについて。
どのようにアクセシビリティやパフォーマンスに気をつけて実装しているかについて書かれている

- [atlassian/react-beautiful-dnd: Beautiful, accessible drag and drop for lists with React.js](https://github.com/atlassian/react-beautiful-dnd "atlassian/react-beautiful-dnd: Beautiful, accessible drag and drop for lists with React.js")

----

## The State of CSS in Angular – Angular Blog
[blog.angular.io/the-state-of-css-in-angular-4a52d4bd2700](https://blog.angular.io/the-state-of-css-in-angular-4a52d4bd2700 "The State of CSS in Angular – Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

AngularのCSSについて。
コンポーネントのカプセルCSS、Shadow DOMを使ったnativeのカプセル化、非推奨となった`/deep/`や`:ng-deep`について

- [The New Angular ::ng-deep and the Shadow-Piercing Combinators Drop](https://hackernoon.com/the-new-angular-ng-deep-and-the-shadow-piercing-combinators-deep-and-drop-4b088dbe459 "The New Angular ::ng-deep and the Shadow-Piercing Combinators Drop")

----

## HTTP/2 Server Push with Node.js | @RisingStack
[blog.risingstack.com/node-js-http-2-push/](http://blog.risingstack.com/node-js-http-2-push/ "HTTP/2 Server Push with Node.js | @RisingStack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP2</span> <span class="jser-tag">article</span></p>

`--expose-http2`フラグで有効化できるNode.jsのHTTP/2でサーバプッシュを行う方法についてのサンプル


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Ava Test Runner - A Fresh Take On JavaScript Testing and Growing an Open-Source Project - Sessions by Pusher
[pusher.com/sessions/meetup/the-js-roundabout/ava-test-runner-a-fresh-take-on-javascript-testing-and-growing-an-open-source-project](https://pusher.com/sessions/meetup/the-js-roundabout/ava-test-runner-a-fresh-take-on-javascript-testing-and-growing-an-open-source-project "Ava Test Runner - A Fresh Take On JavaScript Testing and Growing an Open-Source Project - Sessions by Pusher")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">video</span></p>

Node.jsのテストフレームワークであるAVAについてを紹介する発表動画。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## plouc/nivo: Make dataviz fun again
[github.com/plouc/nivo](https://github.com/plouc/nivo "plouc/nivo: Make dataviz fun again")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">d3.js</span> <span class="jser-tag">library</span> <span class="jser-tag">グラフ</span></p>

D3.jsとReactを使ったデータビジュアライズコンポーネント。 SVGの出力の対応やサーバサイドレンダリングをしてSVGを取得するHTTP APIなども用意されている。


----

## jiayihu/pretty-algorithms: 🌊 Pretty, common and useful algorithms with modern JS and beautiful tests
[github.com/jiayihu/pretty-algorithms](https://github.com/jiayihu/pretty-algorithms "jiayihu/pretty-algorithms: 🌊 Pretty, common and useful algorithms with modern JS and beautiful tests")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アルゴリズム</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

検索、ソート、カウントなどのよくあるアルゴリズムを実装したライブラリ


----

## GoogleChrome/puppeteer: Headless Chrome Node API
[github.com/GoogleChrome/puppeteer](https://github.com/GoogleChrome/puppeteer "GoogleChrome/puppeteer: Headless Chrome Node API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Headless Chromeを扱うライブラリ。
Chromeチームが開発している。


----

## google/songbird: Spatial Audio Encoding on the Web
[github.com/google/songbird](https://github.com/google/songbird "google/songbird: Spatial Audio Encoding on the Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">audio</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Web Audio APIを使ったSpatial Audio Encodingライブラリ


----

## shellscape/mocha-chrome: Run Mocha tests using headless Google Chrome
[github.com/shellscape/mocha-chrome](https://github.com/shellscape/mocha-chrome "shellscape/mocha-chrome: Run Mocha tests using headless Google Chrome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Tools</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span></p>

MochaをHeadless chromeで動かすツール


----

## streamich/memfs: In-memory filesystem with Node's API
[github.com/streamich/memfs](https://github.com/streamich/memfs "streamich/memfs: In-memory filesystem with Node's API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Node.jsの`fs`モジュール互換のメモリファイルシステムライブラリ。
ブラウザでも動作する


----
