---
title: "2015-06-10のJS: ブラウザとES6の状況、Web Audio APIチュートリアル"
author: azu
layout: post
date : 2015-06-10T12:45
category: JSer
tags:
    - WebAudio
    - ES6
    - Safari
    - Chrome
    - MSEdge

---

JSer.info #231 - [Safari 9.0](https://developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html "Safari 9.0")の変更点が公開されています。

JavaScriptにおいてはES6のClasses、Template Strings、Symbol、Computed Propertiesといった機能などのサポートが入っています。
またCSSにおいては、`-webkit-` prefixが外されたものも多いですが、逆に`-webkit-` prefix付きで`-webkit-scroll-snap-type`などのサポートが追加されています。

WebkitのES6やCSSなどに関する実装状況は以下のステータスページに公開されているので、気になる人は見てみるといいと思います。

- [The WebKit Open Source Project - Web Platform Status](http://www.webkit.org/status.html "The WebKit Open Source Project - Web Platform Status")

また、Microsoftの新しいブラウザであるMSEdgeがサポートしているES6の機能については[JavaScript の新機能](https://msdn.microsoft.com/library/br212465(v=vs.94).aspx "JavaScript の新機能")というページでリファレンスが公開されています。
実装状況をまとめたステータスページも[Developer Resources : MSEdge Dev](http://dev.modern.ie/platform/status/ "Developer Resources : MSEdge Dev")にて公開されています。

同時期に[Chrome 44 Beta](http://blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html "Chrome 44 Beta")も公開され、こちらでもComputed Propertiesやユニコードエスケープリテラルなどのサポートが追加され、実装状況については[Chromium Dashboard](https://www.chromestatus.com/features "Chromium Dashboard")にて公開されています。

Firefoxは実況状況をまとめたページがまだないですが、[ECMAScript 6 compatibility table](http://kangax.github.io/compat-table/es6/ "ECMAScript 6 compatibility table")を見ると各ブラウザの実装状況が一覧できるようになっています。

----

[Web Audio School](http://mmckegg.github.io/web-audio-school/ "Web Audio School")というサイトでは、[Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API "Web Audio API")について学ぶことができるチュートリアルが公開されています。

以前[JavaScriptとWeb Audio事始め](http://azu.github.io/slide/webaudioapi/web-audio.html "JavaScriptとWeb Audio事始め")というスライドで簡単にWeb Audioについて紹介していますが、Web Audio APIで音を処理する場合は、音量を調整するGainNodeを作ってそれをつなげるというようなAudioNodeと呼ばれるものを扱ってフィルターなどをかけていきます。

![AudioNode](http://monosnap.com/image/aFVeydGv2X32wTXrWCSpHfMYYBIOhd.png)

[Web Audio School](http://mmckegg.github.io/web-audio-school/ "Web Audio School")というサイトでは、Web Audio APIの基本的な使い方から、色々なAudioNodeの扱いなどについて書かれています。

Web Audio APIのコードを書いて、想定した挙動になるように合わせていく問題形式になっていますが、答えがあってるかどうかを視覚的にわかるようになっているのが面白いです。

<div class="kwout" style="text-align: center;"><img src="http://kwout.com/cutout/6/j6/7q/s2u_bor.jpg" alt="http://mmckegg.github.io/web-audio-school/" title="Web Audio School" width="600" height="339" style="border: none;" usemap="#map_6j67qs2u" /><p><a href="http://mmckegg.github.io/web-audio-school/">Web Audio School</a></p></div>

----

## お知らせ

以前から@[UYEONG](https://github.com/UYEONG "UYEONG")さんが[JSer.infoの韓国語訳](http://wit.nts-corp.com/)をやって頂いていましたが、韓国語訳も[http://jser.info/ko/](http://jser.info/ko/)という感じで同じサイトで公開するようになりました。

![header](http://monosnap.com/image/whz0nvwzXYcZfhtIwxyhL0aowGyOZD.png) 

そのため、サイトのヘッダ部分に言語切り替えのリンクを追加しました。

----


<h1 class="site-genre">ヘッドライン</h1>

----

## Node v0.12.4 (Stable)
[blog.nodejs.org/2015/05/22/node-v0-12-4-stable/](http://blog.nodejs.org/2015/05/22/node-v0-12-4-stable/ "Node v0.12.4 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.4リリース

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#550](https://github.com/babel/babel/blob/master/CHANGELOG.md#550 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Babel 5.5.0リリース。
バグ修正が中心。

----

## What’s new in Babylon.js v2.1 - Eternal Coding - HTML5 / JavaScript / 3D development - Site Home - MSDN Blogs
[blogs.msdn.com/b/eternalcoding/archive/2015/06/08/what-s-new-in-babylon-js-v2-1.aspx](http://blogs.msdn.com/b/eternalcoding/archive/2015/06/08/what-s-new-in-babylon-js-v2-1.aspx "What’s new in Babylon.js v2.1 - Eternal Coding - HTML5 / JavaScript / 3D development - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">ReleaseNote</span></p>

Babylon.js v2.1リリース。

----

## Chromium Blog: Chrome 44 Beta: Improvements to Notifications API and promoted add to homescreen
[blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html](http://blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html "Chromium Blog: Chrome 44 Beta: Improvements to Notifications API and promoted add to homescreen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 44 Betaリリース。
プッシュ通知の改善、`\u{1F302}`のような[Unicodeエスケープのリテラル](https://googlechrome.github.io/samples/extended-unicode-escapes/index.html)、ES6 Computed Properties、`document.scrollingElement`のサポートなど

----

## Safari 9.0
[developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html](https://developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html "Safari 9.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 9.0での変更点としてTemplate strings、Classes、WeakSet、SymbolなどのES6サポート、開発者ツールのデザインや機能追加などが行われている

- [Safari 9.0の新機能の概要 - console.lealog();](http://lealog.hateblo.jp/entry/2015/06/09/115905 "Safari 9.0の新機能の概要 - console.lealog();")
- [iOS9_changes · uupaa/WebKitChangeLog Wiki](https://github.com/uupaa/WebKitChangeLog/wiki/iOS9_changes "iOS9_changes · uupaa/WebKitChangeLog Wiki")

----

## Changelog · winjs/winjs Wiki
[github.com/winjs/winjs/wiki/Changelog#v40](https://github.com/winjs/winjs/wiki/Changelog#v40 "Changelog · winjs/winjs Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WinJS 4.0リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/](https://hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/ "New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

Firefox 40の開発者ツールについて。
パフォーマンスツールの改善、ネットワークモニタでPostデータのコピー、CSSドキュメントの表示連携など

----

## Polymer エレメントの開発ツールと CI - 詩と創作・思索のひろば
[motemen.hatenablog.com/entry/2015/06/polymer-tools-and-ci](http://motemen.hatenablog.com/entry/2015/06/polymer-tools-and-ci "Polymer エレメントの開発ツールと CI - 詩と創作・思索のひろば")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

Polymerに関連するツールやライブラリの消化。
コンポーネントのドキュメント作り方、開発時の補助ツール、配布向けのビルド作成、CIでのテストについてなど

----

## React/dekuコンポーネントとthisのパターン | Web Scratch
[efcl.info/2015/06/05/this-component/](http://efcl.info/2015/06/05/this-component/ "React/dekuコンポーネントとthisのパターン | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span></p>

ReactのコンポーネントをES6 Classesで書くと`this`が多くなる問題とイベントハンドラの登録/解除の例。
また、関数的なアプローチを持つdekuのコンポーネントとの違いについて

----

## React: 保守しやすいハイパフォーマンスの UI コンポーネントを作成する
[www.ibm.com/developerworks/jp/web/library/wa-react-intro/index.html](http://www.ibm.com/developerworks/jp/web/library/wa-react-intro/index.html "React: 保守しやすいハイパフォーマンスの UI コンポーネントを作成する")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React、Component、Flux、デバッグツール、GraphQLとReactNative等の関連するプロジェクトなどReactに全般についてまとまってる記事

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## BlinkOn 4 One-Pager - http://bit.ly/blinkon4onepager - Google ドキュメント
[docs.google.com/document/d/1ga5lPyCxQ0G7deJWDZPSbVvewG7cRdT6Qi-pHXUDgkg/edit#heading=h.rx77pwie3tnj](https://docs.google.com/document/d/1ga5lPyCxQ0G7deJWDZPSbVvewG7cRdT6Qi-pHXUDgkg/edit#heading=h.rx77pwie3tnj "BlinkOn 4 One-Pager - http://bit.ly/blinkon4onepager - Google ドキュメント")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">blink</span> <span class="jser-tag">イベント</span></p>

BlinkについてのイベントであるBlinkOn  4の動画とスライドまとめ

----

## Integrity protection for third-party JavaScript // Speaker Deck
[speakerdeck.com/fmarier/integrity-protection-for-third-party-javascript-1](https://speakerdeck.com/fmarier/integrity-protection-for-third-party-javascript-1 "Integrity protection for third-party JavaScript // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">セキュリティ</span></p>

ブラウザの実装してるサードパーティスクリプトに対するセキュリティについてのスライド。
CSP、HSTS、SRIについて

----

## ▶ Asynchronous JavaScript at Netflix by Matthew Podwysowski at JSConf Budapest 2015 - YouTube
[www.youtube.com/watch?v=a8W5VVGO-jA](https://www.youtube.com/watch?v=a8W5VVGO-jA "▶ Asynchronous JavaScript at Netflix by Matthew Podwysowski at JSConf Budapest 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span> <span class="jser-tag">スライド</span></p>

RxやObservableについての発表。
非同期においてはPromiseがあるがCancelができない問題があり、またNode Streamは最適ではないとして、そこを扱うAPIデザインとしてのObservable、Rxについて紹介している

- [mattpodwysocki/jsconfbp-2015](https://github.com/mattpodwysocki/jsconfbp-2015 "mattpodwysocki/jsconfbp-2015")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Audio School
[mmckegg.github.io/web-audio-school/](http://mmckegg.github.io/web-audio-school/ "Web Audio School")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span></p>

Web Audio APIについてのチュートリアルサイト。
それぞれのAudio Nodeについての解説や実行結果を視覚的に分かるようにしているので分かりやすい

----

## What&#x27;s New in JavaScript
[msdn.microsoft.com/en-us/library/ie/br212465(v=vs.94).aspx](https://msdn.microsoft.com/en-us/library/ie/br212465(v=vs.94).aspx "What&#x27;s New in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MSEdge</span></p>

MSEdgeでのJavaScriptの新しい機能についてのページ

----

## The Accessibility Cheatsheet - bitsofco.de
[bitsofco.de/2015/the-accessibility-cheatsheet](http://bitsofco.de/2015/the-accessibility-cheatsheet "The Accessibility Cheatsheet - bitsofco.de")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">チートシート</span></p>

ウェブアクセシビリティチートシート

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## cssnext
[cssnext.io/](http://cssnext.io/ "cssnext")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSSの新しい構文等を現在のCSSに変換するTranspilerツール。
一部仕様などにない拡張構文も含まれている

- [cssnextでみる次世代CSSとPostCSS | Yucchiy&#x27;s blog](http://blog.yucchiy.com/2015/04/22/cssnext-postcss-for-nextgeneration-of-css/ "cssnextでみる次世代CSSとPostCSS | Yucchiy&#x27;s blog")

----

## TechnologyAdvice/Vers
[github.com/TechnologyAdvice/Vers](https://github.com/TechnologyAdvice/Vers "TechnologyAdvice/Vers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

バージョニングを持ったモデルライブラリ

----

## Verify.js - A powerful, customizable, asynchronous form validation library
[verifyjs.com/](http://verifyjs.com/ "Verify.js - A powerful, customizable, asynchronous form validation library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

非同期でバリデーション出来るライブラリ

----

## Performance Tools | CSS-Tricks
[css-tricks.com/performance-tools/](https://css-tricks.com/performance-tools/ "Performance Tools | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

ウェブサイトパフォーマンス計測に関連するツールやサービスのまとめ

----
<h1 class="site-genre">書籍関係</h1>

----

## ECMAScript 2015… by Maciej Rzepiński [Leanpub PDF/iPad/Kindle]
[leanpub.com/ecmascript2015es6guide](https://leanpub.com/ecmascript2015es6guide "ECMAScript 2015… by Maciej Rzepiński \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">電子書籍</span></p>

ES6についての電子書籍

- [Maciej Rzepiński — Medium](https://medium.com/@mrzepinski "Maciej Rzepiński — Medium")

----
