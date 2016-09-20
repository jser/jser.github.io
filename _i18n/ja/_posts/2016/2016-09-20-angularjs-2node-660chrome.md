---
title: "2016-09-20のJS: AngularJS 2、Node 6.6.0、Chrome 54の開発者ツール"
author: azu
layout: post
date : 2016-09-20T09:48
category: JSer
tags:
    - Angular
    - Node
    - Chrome
    - debug

---

JSer.info #297 - Angular [2.0.0](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-2016-09-14 "2.0.0")がリリースされました。

- [Angular, version 2: proprioception-reinforcement](http://angularjs.blogspot.jp/2016/09/angular2-final.html)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-2016-09-14)
- [🎉✨ Angular 2.0.0がリリースされました 🎉✨ · Angular2 Info](https://ng2-info.github.io/2016/09/angular-2-final/)

----

Node.js 6.6.0がリリースされました

- [Node v6.6.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v6.6.0/)


6.6.0ではEventEmitterのmemory leak警告と
PromiseのUnhandled rejectionの警告を次のように書くことで受け取れるようになっています。

```js
process.on('warning', (warning) => {
	console.log(warning); //
})
```

- [process | Node.js v6.6.0 Documentation](https://nodejs.org/dist/latest-v6.x/docs/api/process.html#process_event_warning)
- [node/test-promises-warning-on-unhandled-rejection.js at 995d504d396d9a7137b11a4c1abebaafd97c3061 · jasnell/node](https://github.com/jasnell/node/blob/995d504d396d9a7137b11a4c1abebaafd97c3061/test/parallel/test-promises-warning-on-unhandled-rejection.js)
- [events: make memory leak warning more programatically accessible by addaleax · Pull Request #8298 · nodejs/node](https://github.com/nodejs/node/pull/8298/files)

ブラウザでは自動でコンソールに[Unhandled Rejection](http://azu.github.io/slide/error-handling/promise-error-handling.html)の警告ができます。
Node.js 6.6.0でも同様にデフォルトで警告がでるようになりました。

```js
const p = Promise.reject('This was rejected');
// UnhandledPromiseRejectionWarning: Unhandled promise rejection (rejection id: 1): This was rejected
```

また、これらの警告は`"warning"`イベントとしてキャッチすることができるようになっています。

今まで、EventEmitterのメモリリーク警告は`stderr`にログを出すだけでテストも難しいものでしたが、同じように`warning`イベントで取得できるようになりました。

```js
const events = require("events");
const event = new events.EventEmitter();
event.setMaxListeners(1);
process.on('warning', (warning) => {
    console.warn(warning.message);
    // Warning: Possible EventEmitter memory leak detected. 2 test listeners added. Use emitter.setMaxListeners() to increase limit
});

event.on("test", () => {});
event.on("test", () => {});
```

- [azu/node6.6-warning-demo](https://github.com/azu/node6.6-warning-demo "azu/node6.6-warning-demo")

----

[Chrome 54 Beta](http://blog.chromium.org/2016/09/chrome-54-beta-custom-elements-v1.html "Chrome 54 Beta")がリリースされましたが、開発者ツールも同様に更新されています。

- [DevTools Digest, September 2016: Perf Roundup | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/09/devtools-digest "DevTools Digest, September 2016: Perf Roundup | Web Updates - Google Developers")

CPU Throttling、TimelineにNetwork viewの表示、スクロールパフォーマンスのProfile、SourceパネルにTimelineのデータ表示などのボトルネックを見つける機能が追加されています。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Angular, version 2: proprioception-reinforcement
[angularjs.blogspot.com/2016/09/angular2-final.html](http://angularjs.blogspot.com/2016/09/angular2-final.html "Angular, version 2: proprioception-reinforcement")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

AngularJS 2リリース

- [🎉✨ Angular 2.0.0がリリースされました 🎉✨ · Angular2 Info](https://ng2-info.github.io/2016/09/angular-2-final/ "🎉✨ Angular 2.0.0がリリースされました 🎉✨ · Angular2 Info")

----

## Node v6.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.6.0/](https://nodejs.org/en/blog/release/v6.6.0/ "Node v6.6.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.6.0リリース。
EventEmitterのmemory leak警告、
PromiseのUnhandled rejectionの警告が、`process.on('warning', (warning) => { })`でキャッチできるように

----

## jQuery UI 1.12.1 | jQuery UI Blog
[blog.jqueryui.com/2016/09/jquery-ui-1-12-1/](http://blog.jqueryui.com/2016/09/jquery-ui-1-12-1/ "jQuery UI 1.12.1 | jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.12.1リリース。
新しいテーマの追加、`Checkboxradio　widget`の追加、`classes`オプションの追加など

----

## Release Notes for Safari Technology Preview Release 13 | WebKit
[webkit.org/blog/6937/release-notes-for-safari-technology-preview-release-13/](https://webkit.org/blog/6937/release-notes-for-safari-technology-preview-release-13/ "Release Notes for Safari Technology Preview Release 13 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 13 リリース。
`adoptedCallback`のサポート、`CSS.escape`の実装、クロスオリジンのチェック強化など

----

## Chromium Blog: Chrome 54 Beta: Custom Elements V1, BroadcastChannel, and media platform improvements
[blog.chromium.org/2016/09/chrome-54-beta-custom-elements-v1.html](http://blog.chromium.org/2016/09/chrome-54-beta-custom-elements-v1.html "Chromium Blog: Chrome 54 Beta: Custom Elements V1, BroadcastChannel, and media platform improvements")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 54βリリース。
Custom Element v1、BroadcastChannelのサポート。
Resource Timing API のtransferやencoded/decodedのサポート、`initTouchEvent`の削除など

----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing debugger.html ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/09/introducing-debugger-html/](https://hacks.mozilla.org/2016/09/introducing-debugger-html/ "Introducing debugger.html ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

debugger.htmlというソースパネルライクな新しいデバッガーについて。
Firefox、Chrome、Node.jsに対応し、Remote Debug Protocolでデータをやり取りする。
Firefoxの開発者ツールに統合される予定

- [debugger.html のご紹介 | Mozilla Developer Street (modest)](https://dev.mozilla.jp/2016/09/introducing-debugger-html/ "debugger.html のご紹介 | Mozilla Developer Street (modest)")

----

## DevTools Digest, September 2016: Perf Roundup | Web Updates - Google Developers
[developers.google.com/web/updates/2016/09/devtools-digest](https://developers.google.com/web/updates/2016/09/devtools-digest "DevTools Digest, September 2016: Perf Roundup | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">Chrome</span></p>

Chrome 54での開発者ツールについて。
CPU Throttling、TimelineにNetwork viewの表示、スクロールパフォーマンスのProfile、SourceパネルにTimelineのデータ表示など

----

## JS web frameworks benchmark – Round 4 | Stefan_Krause.blog()
[www.stefankrause.net/wp/?p=316](http://www.stefankrause.net/wp/?p=316 "JS web frameworks benchmark – Round 4 | Stefan\_Krause.blog()")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

AngularやReactなどのライブラリやフレームワークのベンチマーク比較

- [Table Report](http://stefankrause.net/js-frameworks-benchmark4/webdriver-ts/table.html "Table Report")

----

## How Developers use Node.js - Survey Results | @RisingStack
[blog.risingstack.com/node-js-developer-survey-results-2016/](http://blog.risingstack.com/node-js-developer-survey-results-2016/ "How Developers use Node.js - Survey Results | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">アンケート</span></p>

Node.jsを使ったサーバサイド開発についてのアンケート結果

----

## Why Use Flow? · Aria
[blog.aria.ai/post/why-use-flow/](https://blog.aria.ai/post/why-use-flow/ "Why Use Flow? · Aria")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span></p>

FlowによるStatic typeについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## The future of ES6 (Jafar Husain) - Full Stack Fest 2016 - YouTube
[www.youtube.com/watch?v=3pKNRgResq0](https://www.youtube.com/watch?v=3pKNRgResq0 "The future of ES6 (Jafar Husain) - Full Stack Fest 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span></p>

現在策定中の仕様も含めて非同期処理について。
Promise、Async/Await。
PullなAPIとしてGenerator(同期)、AsyncGenerator(Stage 2)。
PushなAPIとしてObservable(Stage 1)について

----

## Пользовательские свойства как основа архитектуры CSS (FrontTalks) // Speaker Deck
[speakerdeck.com/lautsevich/pol-zovatiel-skiie-svoistva-kak-osnova-arkhitiektury-css-fronttalks](https://speakerdeck.com/lautsevich/pol-zovatiel-skiie-svoistva-kak-osnova-arkhitiektury-css-fronttalks "Пользовательские свойства как основа архитектуры CSS (FrontTalks) // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">スライド</span></p>

CSS Custom Propertiesについてのスライド。
Fallback、i18n、CSS Custom Propertiesとcalc、JavaScriptからの利用、@supportsについてなど

----

## Testing JavaScript with Jest - Lesson Playlist @eggheadio
[egghead.io/playlists/testing-javascript-with-jest-a36c4074](https://egghead.io/playlists/testing-javascript-with-jest-a36c4074 "Testing JavaScript with Jest - Lesson Playlist @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">video</span></p>

Jestを学ぶスクリーンキャスト

----

## Building Applications with React and Redux in ES6 | Zombie Code Kill
[zombiecodekill.com/2016/05/21/building-applications-with-react-and-redux-in-es6/](https://zombiecodekill.com/2016/05/21/building-applications-with-react-and-redux-in-es6/ "Building Applications with React and Redux in ES6 | Zombie Code Kill")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span></p>

ReactとReduxの入門講座

- [Building Applications with React and Redux in ES6 | Pluralsight](https://www.pluralsight.com/courses/react-redux-react-router-es6 "Building Applications with React and Redux in ES6 | Pluralsight")

----

## Developer&#x27;s guide to accessibility mechanics — Developer&#x27;s guide to accessibility mechanics
[ljwatson.github.io/decks/2016/fromthefront/index.html#cover](https://ljwatson.github.io/decks/2016/fromthefront/index.html#cover "Developer's guide to accessibility mechanics — Developer's guide to accessibility mechanics")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">スライド</span></p>

デフォルトの`<a>`はどういうサポートがあるからaccessibleであるかについてを独自のリンク実装で見ていく話。
またデフォルトではaccessibleでないツールチップ、タブパネルなどをどうじっそうするか。
実際にスクリーンリーダーの音を聞きながら確認できる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## avocode/combokeys: Web browser keyboard shortcuts. CommonJS, NPM.
[github.com/avocode/combokeys](https://github.com/avocode/combokeys "avocode/combokeys: Web browser keyboard shortcuts. CommonJS, NPM.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">キーボード</span> <span class="jser-tag">library</span></p>

Mousetrapをforkしたキーボードショートカットライブラリ。
リファクタリングとdocumentへのlistenがデフォルトではないように変更されている

- [Handle keyboard shortcuts in the browser with Combokeys](https://blog.avocode.com/blog/handle-keyboard-shortcuts-in-the-browser-with-combokeys "Handle keyboard shortcuts in the browser with Combokeys")

----

## kentcdodds/match-sorter: Simple, expected, and deterministic best-match sorting of an array in JavaScript
[github.com/kentcdodds/match-sorter](https://github.com/kentcdodds/match-sorter "kentcdodds/match-sorter: Simple, expected, and deterministic best-match sorting of an array in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

オブジェクトの配列から検索するライブラリ。
指定したキーのみを対象にしたり、検索方法などを指定できる

----
<h1 class="site-genre">書籍関係</h1>

----

## BUILD PACMAN by Jeffrey Biles [Leanpub PDF/iPad/Kindle]
[leanpub.com/buildpacman](https://leanpub.com/buildpacman "BUILD PACMAN by Jeffrey Biles \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">book</span></p>

JavaScriptでパックマンを作る書籍。

----
