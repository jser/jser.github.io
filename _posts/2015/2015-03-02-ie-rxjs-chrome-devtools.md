---
title: "2015-03-23のJS: IEのアップデート、RxJS入門、Chrome DevToolsの新機能と計測の仕方"
author: azu
layout: post
date : 2015-03-23T22:49
category: JSer
tags:
    - IE
    - Chrome
    - debug
    - performance

---

JSer.info #220 - Windows 10 Technical Previewがアップデートされ、IEのレンダリングエンジンもアップデートされています。
[Rendering engine updates in March for the Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2015/03/18/rendering-engine-updates-in-march-for-the-windows-10-technical-preview.aspx "Rendering engine updates in March for the Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs")では Web Audio APIやTouch Eventsなど最近サポートされた機能についてまとめられています。


-----

[「RxJS」初心者入門 - JavaScriptの非同期処理の常識を変えるライブラリ | 株式会社LIG](http://liginc.co.jp/web/js/151272 "「RxJS」初心者入門 - JavaScriptの非同期処理の常識を変えるライブラリ | 株式会社LIG")という記事ではReactive ExtensionsのJavaScript実装である[RxJS](https://github.com/Reactive-Extensions/RxJS "RxJS")について書かれています。

Rxとはどういう概念やパターンを持っているか、ObserverとObservable、オペレーターといったRxJSを構成する要素について色々なサンプルコード共に解説されています。

- [Learn Reactive Extensions](http://wilfrem.github.io/learn_rx/ "Learn Reactive Extensions")

----

- 動画: [jQuery UK Conference - Oxford 2015](http://jqueryuk.com/2015/videos.php?s=devtools-state-of-the-union "jQuery UK Conference - Oxford 2015")
- スライド: [DevTools: State Of The Union 2015 // Speaker Deck](https://speakerdeck.com/addyosmani/devtools-state-of-the-union-2015 "DevTools: State Of The Union 2015 // Speaker Deck")

Addy Osmani氏によるChrome開発者ツールの新しい機能の紹介がされている発表の動画です。
以前話題となった[WikipediaとjQueryのユースケース](https://github.com/jquery/jquery.com/issues/88 "Don&#39;t advertise .show() on the front page · Issue #88 · jquery/jquery.com")を例にどうやってパフォーマンスの問題を計測していくかなど実践的なツールの使い方について話されています。

動画は時間内に終わらなかったためスライドの最後まで話されてないですが、どういう所が描画のボトルネックになっているのかを見ていく話としても面白いので見ておくといいかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Rendering engine updates in March for the Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2015/03/18/rendering-engine-updates-in-march-for-the-windows-10-technical-preview.aspx](http://blogs.msdn.com/b/ie/archive/2015/03/18/rendering-engine-updates-in-march-for-the-windows-10-technical-preview.aspx "Rendering engine updates in March for the Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">ReleaseNote</span></p>

Windows 10 Technical Previewのアップデートが行われて、ブラウザのレンダリングエンジンもアップデートされている。
WAI-ARIA Landmark Roles、Web Audio API、Touch Events、Fullscreen APIなどのサポートなど

----

## flow/Changelog at v0.7.0 · facebook/flow
[github.com/facebook/flow/blob/v0.7.0/Changelog](https://github.com/facebook/flow/blob/v0.7.0/Changelog "flow/Changelog at v0.7.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.7.0リリース。
ES6 modulesのサポート開始、null/undefinedとの比較するケースの対応改善、`hasOwnProperty`を呼び出してるケースの対応改善

----

## React v0.13.1 | React
[facebook.github.io/react/blog/2015/03/16/react-v0.13.1.html](http://facebook.github.io/react/blog/2015/03/16/react-v0.13.1.html "React v0.13.1 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.13.1リリース

----

## harmony:specification_drafts [ES Wiki]
[`wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#march_17_2015_rev_36_release_candidate_3`](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#march_17_2015_rev_36_release_candidate_3)

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES6仕様書RC3リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## Explore React
[x-team.github.io/explore-react/](http://x-team.github.io/explore-react/ "Explore React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">コードリーディング</span></p>

Reactのコードリーディングをしながら内部的な仕組みを見ていく話

----

## Moving Codecademy to ECMAScript 6, Webpack, and React
[artur.co/articles/moving-codecademy-to-es6-webpack-and-react/](http://artur.co/articles/moving-codecademy-to-es6-webpack-and-react/ "Moving Codecademy to ECMAScript 6, Webpack, and React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">React</span></p>

Codecademyのクライアントサイドのアーキテクチャの変遷について

----

## Chromium Blog: New JavaScript techniques for rapid page loads
[blog.chromium.org/2015/03/new-javascript-techniques-for-rapid.html](http://blog.chromium.org/2015/03/new-javascript-techniques-for-rapid.html "Chromium Blog: New JavaScript techniques for rapid page loads")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span></p>

Chrome 41で`async`属性をつけたスクリプトはダウンロードが始まった瞬間にパーサ用の別スレッドでパースされるためより高速になるとの話

- [レンダリングを妨げる JavaScript を削除する - PageSpeed Insights — Google Developers](https://developers.google.com/speed/docs/insights/BlockingJS "レンダリングを妨げる JavaScript を削除する - PageSpeed Insights — Google Developers")

----

## 「RxJS」初心者入門 - JavaScriptの非同期処理の常識を変えるライブラリ | 株式会社LIG
[liginc.co.jp/web/js/151272](http://liginc.co.jp/web/js/151272 "「RxJS」初心者入門 - JavaScriptの非同期処理の常識を変えるライブラリ | 株式会社LIG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span></p>

RxJSの入門記事。
Rxのパラダイム的な話やサンプルなどがまとまってる

----

## ES5の範囲でOption型を表すライブラリ、option-t を作った - snyk_s log
[saneyukis.hatenablog.com/entry/2015/03/20/191424](http://saneyukis.hatenablog.com/entry/2015/03/20/191424 "ES5の範囲でOption型を表すライブラリ、option-t を作った - snyk\_s log")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Promises</span></p>

(初期状態)未選択を状態として保存したい時に使うOption typeの実装ライブラリ(like Rust)

- [saneyuki/option-t.js](https://github.com/saneyuki/option-t.js "saneyuki/option-t.js")
- [「値が無い」ということをどう表現するか、あるいはOption型について - Line 1: Error: Invalid Blog(&#x27;by Esehara&#x27; )](http://bugrammer.hateblo.jp/entry/2013/07/30/134120 "「値が無い」ということをどう表現するか、あるいはOption型について - Line 1: Error: Invalid Blog(&#x27;by Esehara&#x27; )")

----

## JavaScript - 4パターンのWebWorker生成方法とインラインワーカーの技法 - Qiita
[qiita.com/mohayonao/items/872166cf364e007cf83d](http://qiita.com/mohayonao/items/872166cf364e007cf83d "JavaScript - 4パターンのWebWorker生成方法とインラインワーカーの技法 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span></p>

WebWorkerの生成方法についてのまとめ

----

## material-fluxというFluxライブラリをREADME駆動で開発した | Web Scratch
[efcl.info/2015/03/17/material-flux/](http://efcl.info/2015/03/17/material-flux/ "material-fluxというFluxライブラリをREADME駆動で開発した | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Flux</span> <span class="jser-tag">ECMAScript</span></p>

特殊なハックをできるだけ排除したFluxライブラリを作った話とREADME駆動について。
またES6 ClassesをベースとしたAPIについて

----

## RemoteDebug and cross-browser DevTools. One year later. — Kenneth Auchenberg
[kenneth.io/blog/2015/03/12/remotedebug-one-year-later](https://kenneth.io/blog/2015/03/12/remotedebug-one-year-later "RemoteDebug and cross-browser DevTools. One year later. — Kenneth Auchenberg")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span></p>

ブラウザ間の共通デバッグプロトコルを作るプロジェクトであるRemoteDebugを公開して1年経ってどのような変化があったかについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## DevTools: State Of The Union 2015 // Speaker Deck
[speakerdeck.com/addyosmani/devtools-state-of-the-union-2015](https://speakerdeck.com/addyosmani/devtools-state-of-the-union-2015 "DevTools: State Of The Union 2015 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">スライド</span></p>

Chromeの開発者ツールの新しい機能や実際のパフォーマンス計測、問題の見つけ方について。
WikipediaとjQueryの例、一つの処理が100ms以上取ってるなら危険、`hide()`のボトルネック、まずは計測することから始めるという話

- [jQuery UK Conference - Oxford 2015](http://jqueryuk.com/2015/videos.php?s=devtools-state-of-the-union "jQuery UK Conference - Oxford 2015")

----

## Using npm link to use node modules that are &quot;in progress&quot; - Node.js Video Tutorial #free @eggheadio
[egghead.io/lessons/node-js-using-npm-link-to-use-node-modules-that-are-in-progress](https://egghead.io/lessons/node-js-using-npm-link-to-use-node-modules-that-are-in-progress "Using npm link to use node modules that are &quot;in progress&quot; - Node.js Video Tutorial #free @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">動画</span></p>

npm linkを使った開発についてのスクリーンキャスト

----

## jQuery UK Conference - Oxford 2015
[jqueryuk.com/2015/videos.php](http://jqueryuk.com/2015/videos.php "jQuery UK Conference - Oxford 2015")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">動画</span> <span class="jser-tag">まとめ</span></p>

jQuery UK 2015の動画が公開された

- [Coverage of jQuery UK 2015 | Lanyrd](http://lanyrd.com/2015/jquery-uk/coverage/ "Coverage of jQuery UK 2015 | Lanyrd")

----

## ウェブパフォーマンスの基礎とこれから
[www.slideshare.net/kawada_hiroshi/ss-46149727](http://www.slideshare.net/kawada_hiroshi/ss-46149727 "ウェブパフォーマンスの基礎とこれから")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

通信についてを中心に扱うパフォーマンスについてのスライド
ウェブサイトの表示までにどういう通信が起きてるか、ブラウザ上でどうやって計測するかやPerformance Timelineなどの仕様について、HTTP/2での戦略の違いなど

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Jank Free: Let&#x27;s Make the Web Silky Smooth!
[jankfree.org/](http://jankfree.org/ "Jank Free: Let&#x27;s Make the Web Silky Smooth!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">動画</span> <span class="jser-tag">まとめ</span></p>

ウェブサイトで60FPSの描画をするためのパフォーマンスチューニング等についてのスライド、動画や記事のまとめサイト。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## eatcodeplay/Konsole.js
[github.com/eatcodeplay/Konsole.js](https://github.com/eatcodeplay/Konsole.js "eatcodeplay/Konsole.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">library</span></p>

画面内にコンソールを表示できるFirebug Lite的なライブラリ。
console APIの上書き、DOMのインスペクト、CSSの操作、FPSの表示など

----

## Hamsa
[gethamsa.com/](http://gethamsa.com/ "Hamsa")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`Object.observe()`(又はpolyfill)を使ったモデルライブラリ。
スキーマ的なプロパティの型やデフォルト値の定義、class継承、` Object.observe()`を使った変更監視、find系の探査メソッドを持つ

----
<h1 class="site-genre">書籍関係</h1>

----

## O&#x27;Reilly Japan - 入門 React
[www.oreilly.co.jp/books/9784873117195/](http://www.oreilly.co.jp/books/9784873117195/ "O&#x27;Reilly Japan - 入門 React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2015年03月27日発売
Developing a React Edgeの翻訳本。

----

## HTML5 &amp; CSS3 For The Real World, 2nd Edition - O&#x27;Reilly Media
[shop.oreilly.com/product/9780987467485.do](http://shop.oreilly.com/product/9780987467485.do "HTML5 &amp; CSS3 For The Real World, 2nd Edition - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

広義のHTMLとCSSの新しいAPIなどを見ていく書籍

----

## Functional Programming in JavaScript - O&#x27;Reilly Media
[shop.oreilly.com/product/9781784398224.do](http://shop.oreilly.com/product/9781784398224.do "Functional Programming in JavaScript - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2015年3月発売。
関数型JavaScriptについての書籍

----

## React+d3.js by Swizec Teller [Leanpub PDF/iPad/Kindle]
[leanpub.com/reactd3js](https://leanpub.com/reactd3js "React+d3.js by Swizec Teller \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">d3.js</span> <span class="jser-tag">book</span></p>

ReactとD3.jsについての書籍

----
