---
title: "2014-11-25のJS: Chrome 39 Beta、デバッグTips、Facebook Flow"
author: azu
layout: post
date : 2014-11-25T08:12
category: Jser
tags:
    - Chrome
    - debug
    - Flow
    - Type

---

JSer.info #203 - [Chrome 39 Beta](http://blog.chromium.org/2014/10/chrome-39-beta-js-generators-animation.html "Chrome 39 Beta")がリリースされました。

ES6 Generatorがデフォルトで有効になったり、Web Animationsの実装が進められています。
また Web Application Manifestの対応や[Beacon API](http://updates.html5rocks.com/2014/10/Send-beacon-data-in-Chrome-39 "Beacon API")が実装されています。

通常のXHRを使った非同期通信ではページを閉じてしまうとそのデータを送ることが保証出来ませんが、 [Beacon API](http://updates.html5rocks.com/2014/10/Send-beacon-data-in-Chrome-39 "Beacon API")を使うことでUIをブロックすることなくちゃんとデータを送れるようになります(ビーコンというぐらいなので大きなデータは送れません)

例えば、リンクがクリックされた計測データを画面が遷移する前に送ろうとした時にXHRでは一度Clickをキャンセル->XHRでデータを送る->遷移し直すという事(もしくは同期XHR)をしていましたが、 Beacon APIを使えば単純にデータを`navigator.sendBeacon`で送ればよくなります。


----

[Modern Debugging Experience: Part 2 - Tuts+ Code Tutorial](http://code.tutsplus.com/tutorials/modern-debugging-experience-part-2--cms-22584 "Modern Debugging Experience: Part 2 - Tuts+ Code Tutorial") という連載では(Chromeの)開発者ツールを使ったJavaScriptのデバッグテクニックについて色々な手法が書かれています。

- [Modern Debugging Experience](http://code.tutsplus.com/series/modern-debugging-experience--cms-698 "Modern Debugging Experience") 連載シリーズページ

`debugger`ステートメントを使った単純なbreakだけではなく、`Object.observe`やgetter/setterなどと組み合わせて使う方法等新しい方法も紹介しています。

また、条件付きのBreakpoints(コード、DOM、Event)やコールスタックの読み方、Node.jsのデバッグツールについても書かれています。

----

FacebookからJavaScriptの型チェックである[Flow](http://flowtype.org/ "Flow")がリリースされました。

- [Flow, a new static type checker for JavaScript | Engineering Blog | Facebook Code](https://code.facebook.com/posts/1505962329687926/flow-a-new-static-type-checker-for-javascript/ "Flow, a new static type checker for JavaScript | Engineering Blog | Facebook Code")

Flowは同じくFacebookが公開してる[Hack](https://code.facebook.com/posts/264544830379293/hack-a-new-programming-language-for-hhvm/ "Hack")と似た部分があり、並列に処理する事で高速でインクリメンタルな型チェックを行う事を目的としています。

`/* @flow */` というコメントで宣言した箇所についてのみ型チェックを行うため、段階的に型付けをしていけるようになっています。

まだバージョンが[v0.1.1](https://github.com/facebook/flow/releases/tag/v0.1.1 "Release v0.1.1: Added changelog for 0.1.1 release · facebook/flow")なので、[標準の型定義に足りないもの](https://github.com/facebook/flow/pull/115 "Some more node std libs by jeffmo · Pull Request #115 · facebook/flow")があったり、Windowsで動かすには[非公式のビルド](http://www.ocamlpro.com/pub/ocpwin/flow-builds/ "")のみだったりしますが色々期待できるツールとなりそうです。

今後の方針については[Flow | Future Plans](http://flowtype.org/docs/coming-soon.html#_ "Flow | Future Plans")に書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Chromium Blog: Chrome 39 Beta: JS Generators, Animation Playback Control, and the WebApp Manifest
[blog.chromium.org/2014/10/chrome-39-beta-js-generators-animation.html](http://blog.chromium.org/2014/10/chrome-39-beta-js-generators-animation.html "Chromium Blog: Chrome 39 Beta: JS Generators, Animation Playback Control, and the WebApp Manifest")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 39βリリース。

Generatorがデフォルトで有効、Web Animationの`play()`や`pause()`のサポート、 Web Application Manifest、 Beacon API のサポート

- [ジェネレータについて - JS.next](http://js-next.hatenablog.com/entry/2014/08/07/174147 "ジェネレータについて - JS.next")
- [Send beacon data in Chrome 39](http://updates.html5rocks.com/2014/10/Send-beacon-data-in-Chrome-39 "Send beacon data in Chrome 39")

----
<h1 class="site-genre">アーティクル</h1>

----

## Send beacon data in Chrome 39
[updates.html5rocks.com/2014/10/Send-beacon-data-in-Chrome-39](http://updates.html5rocks.com/2014/10/Send-beacon-data-in-Chrome-39 "Send beacon data in Chrome 39")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アクセス解析</span> <span class="jser-tag">Chrome</span></p>

Chrome 39でBeacon APIが入った。

Beacon APIを使えばクリックしてページ移動するときのクリックのログも非同期でちゃんと送ることが出来る。(単純なXHRだと送り終わる前に遷移してしまう)

----

## Modern Debugging Experience: Part 2 - Tuts+ Code Tutorial
[code.tutsplus.com/tutorials/modern-debugging-experience-part-2--cms-22584](http://code.tutsplus.com/tutorials/modern-debugging-experience-part-2--cms-22584 "Modern Debugging Experience: Part 2 - Tuts+ Code Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

開発者ツールを使ったデバッグ方法のTips。

debuggerステートメント、コールスタック、getter/setter/Object.observe等を使ったアクセス時にBreakさせる方法やWatch Expression、イベントリスナーのデバッグ等について書かれている

----

## My five promise patterns
[remysharp.com/2014/11/19/my-five-promise-patterns](https://remysharp.com/2014/11/19/my-five-promise-patterns "My five promise patterns")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promiseパターンについて

Nodeスタイルの高階関数をPromiseを返すようにするdenodeify、`bind`による引数の固定、コールバックとの併用、`reject`ではなく常にthrowする、処理の終わりでいつも`catch`する

----

## Property testing in JavaScript with quick_check.js - RightScale Engineering Blog
[eng.rightscale.com/2014/07/18/quick-check-js.html](http://eng.rightscale.com/2014/07/18/quick-check-js.html "Property testing in JavaScript with quick\_check.js - RightScale Engineering Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

JavaScriptのQuickChek実装である [quick_check.js](https://github.com/gampleman/quick_check.js/) について

----

## uxebu/mocha-sinon-traceur-example
[github.com/uxebu/mocha-sinon-traceur-example](https://github.com/uxebu/mocha-sinon-traceur-example "uxebu/mocha-sinon-traceur-example")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

ES6でテストを書いてTDDするサンプルプロジェクト

- [ES6 and TDD at work, with traceur, mocha and sinon - uxebu](http://www.uxebu.com/blog/2014/11/es6-tdd-work-traceur-mocha-sinon/ "ES6 and TDD at work, with traceur, mocha and sinon - uxebu")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Nodevember - YouTube
[www.youtube.com/user/nodevember/feed](https://www.youtube.com/user/nodevember/feed "Nodevember - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">動画</span></p>

http://nodevember.org/ の動画が公開されている

----

## Real World React - YouTube
[www.youtube.com/watch?v=uZgAq1CZ1N8](https://www.youtube.com/watch?v=uZgAq1CZ1N8 "Real World React - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span> <span class="jser-tag">動画</span></p>

ReactのComponentの作り方やテストについて詳しい発表

- http://presentboldly.com/bejonbee/real-world-react-v012

----

## DOM Performance (JSNext Bulgaria)
[www.slideshare.net/ickatanet/dom-performance-jsnext-bulgaria](http://www.slideshare.net/ickatanet/dom-performance-jsnext-bulgaria "DOM Performance (JSNext Bulgaria)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

DOM操作のパフォーマンスTips的なスライド。

Event Delegate、Style操作、DOM Nodeの作成(clone、DocumentFragment)、DOM Nodeの削除について。

----

## KnowThen – Screencasts For Developers
[knowthen.com/](http://knowthen.com/ "KnowThen – Screencasts For Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">動画</span></p>

JavaScriptについてのスクリーンキャストをするサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## newton-software/devil
[github.com/newton-software/devil](https://github.com/newton-software/devil "newton-software/devil")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">node-webkit</span> <span class="jser-tag">debug</span></p>

node-inspectorのようにGUIでNode.jsアプリのデバッグを行う事が出来るツール。

----

## Flow | A static type checker for JavaScript
[flowtype.org/](http://flowtype.org/ "Flow | A static type checker for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">facebook</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Facebookの静的型チェックツール。

Ocamlで書かれていて、TypeScriptと大体互換性が型定義を行える。

サーバとして動かす事もできる。HHVM/Hackみたいなインクリメンタルな型付けを行える

----

## axemclion/protractor-perf
[github.com/axemclion/protractor-perf](https://github.com/axemclion/protractor-perf "axemclion/protractor-perf")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">protractor</span> <span class="jser-tag">testing</span> <span class="jser-tag">performance</span></p>

Protractorのパフォーマンス測定版のようなツール

----

## inikulin/ineed
[github.com/inikulin/ineed](https://github.com/inikulin/ineed "inikulin/ineed")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HTMLのスクレイピング、変換処理(Reprocessing)を行えるNodeモジュール

----

## jas-/secStore.js
[github.com/jas-/secStore.js](https://github.com/jas-/secStore.js "jas-/secStore.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

localStorage/sessionStorage/Cookieで暗号化をサポートするラッパーライブラリ

----

## janmonschke/Web-Audio-Editor
[github.com/janmonschke/Web-Audio-Editor](https://github.com/janmonschke/Web-Audio-Editor "janmonschke/Web-Audio-Editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">Tools</span></p>

ウェブベースのWeb Audio Editor

----

## SpoonX/useuses
[github.com/SpoonX/useuses](https://github.com/SpoonX/useuses "SpoonX/useuses")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

`@uses`アノテーションコメントでそのJSファイルが依存するファイルパスを記述して使うモジュール管理ルール、ビルドツール

concatする程度にはシンプルで、CommonJSのような強い依存関係ではなく、単純にコメントを追加するだけなので余計にファイルは必要ない。

- [javascript dependency management « Php « SpoonX Blog](http://blog.spoonx.nl/javascript-dependency-management/ "javascript dependency management « Php « SpoonX Blog")

----

## techlayer/espresso.js
[github.com/techlayer/espresso.js](https://github.com/techlayer/espresso.js "techlayer/espresso.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">backbone.js</span> <span class="jser-tag">Flux</span></p>

BackboneとReactをインスパイアしたMV*ライブラリ。

Fluxのデータフローを一方向にするアイデアをBackboneに持ってきた感じのライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Discover AngularJS by Adam Burak [Leanpub PDF/iPad/Kindle]
[leanpub.com/discoverangularjs](https://leanpub.com/discoverangularjs "Discover AngularJS by Adam Burak \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

AngularJSチュートリアル本

----