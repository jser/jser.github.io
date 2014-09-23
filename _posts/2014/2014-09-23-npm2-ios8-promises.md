---
title: "2014-09-23のJS: "
author: azu
layout: post
date : 2014-09-23T16:58
category: JSer
tags:
    - node.js
    - npm
    - iOS
    - Promises

---

JSer.info #193 - node.jsのパッケージ管理ツールであるnpm 2.0.0がリリースされました。

[npm run-scriptに引数を渡せるように](https://github.com/npm/npm/pull/5518 "Passing args into run-scripts by bcoe · Pull Request #5518 · npm/npm")なったことや、npmの[リリースプロセスがドキュメント化](https://github.com/npm/npm/wiki/Release-Process "Release Process · npm/npm Wiki")されたこと、[Scoped packages](https://www.npmjs.org/doc/misc/npm-scope.html "Scoped packages")という機能が追加された点等結構色々変更があります。

[Scoped packages](https://www.npmjs.org/doc/misc/npm-scope.html "Scoped packages")は企業利用などで使うときにpublicじゃなくて社内でモジュールを管理するためのスコープ機能を提供する仕組みです。

詳細は以下の記事に書かれています。

- [The npm Blog — npm@2.0.0](http://blog.npmjs.org/post/98131109725/npm-2-0-0 "The npm Blog — npm@2.0.0")

---

iOS8がリリースされ内蔵されているSafariのアップデートと新しいWebViewが入りました。

以下の記事ではどのような機能が入ったかや、今までのWebView(UIWebView)と新しいWebView(WKWebView)のパフォーマンスや制限の違い等について書かれています。

- [iOS 8 and iPhone 6 for web developers and designers: next evolution for Safari and native webapps | Breaking the Mobile Web](http://www.mobilexweb.com/blog/safari-ios8-iphone6-web-developers-designers "iOS 8 and iPhone 6 for web developers and designers: next evolution for Safari and native webapps | Breaking the Mobile Web")
- [Apple Shows Love for HTML5 with iOS 8 | Blog | Sencha](http://www.sencha.com/blog/apple-shows-love-for-html5-with-ios-8 "Apple Shows Love for HTML5 with iOS 8 | Blog | Sencha")

まだ、バグ等も多いですが、新しいWKWebViewでは今までのWebViewのような制限がないので、アプリ内でもSafariと同じように動くものができるかもしれません。

---

[Node.jsエンジニアなら2014年内に知っておきたいPromise入門 | Tokyo Otaku Mode Tech Blog](http://blog.otakumode.com/2014/09/17/nodejs-promise/ "Node.jsエンジニアなら2014年内に知っておきたいPromise入門 | Tokyo Otaku Mode Tech Blog") という記事では、Promiseの基本的な使い方やNodeで[よく使われているasync.js](http://blog.futurice.com/npm-registry-in-numbers "NPM registry in numbers | Futurice blog")モジュールからの切り替えについて詳しく書かれています。

まだ、Node.jsのstableであるv0.10にはネイティブでPromiseが入っていないため、[Bluebird](https://github.com/petkaantonov/bluebird "Bluebird")を使った例で書かれています。
[次期安定版 v0.12](http://d.hatena.ne.jp/jovi0608/20140319/1395199285 "次期安定版 v0.12")ではネイティブでPromiseが入ることや、Node以外でもPromiseを使ったAPIは増えていくため、Promiseについて分かりやすくまとまっていていいと思います。

- [JavaScript Promiseを使うウェブの仕様を調べてみた | Web Scratch](http://efcl.info/2014/09/16/promises-spec-ref-list/ "JavaScript Promiseを使うウェブの仕様を調べてみた | Web Scratch")

---

<h1 class="site-genre">ヘッドライン</h1>

----

## The npm Blog — npm@2.0.0
[blog.npmjs.org/post/98131109725/npm-2-0-0](http://blog.npmjs.org/post/98131109725/npm-2-0-0 "The npm Blog — npm@2.0.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 2.0.0リリース。

リリースプロセスのドキュメント化、semverの挙動の変更、企業など社内モジュールの管理等に使えるscopeという機能を追加、npm runが引数を取れるようになるなど

- [Release Process · npm/npm Wiki](https://github.com/npm/npm/wiki/Release-Process "Release Process · npm/npm Wiki")
- [npm-scope](https://www.npmjs.org/doc/misc/npm-scope.html "npm-scope")

----

## WinJS Everywhere
[blogs.windows.com/buildingapps/2014/09/17/winjs-everywhere/](http://blogs.windows.com/buildingapps/2014/09/17/winjs-everywhere/ "WinJS Everywhere")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WinJS 3.0リリース。

クロスプラットフォームのデザイン互換性周りの修正が中心

- [WinJS3.0 がリリースされました。 - monoe&#x27;s blog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/osamum/archive/2014/09/19/winjs3-0.aspx "WinJS3.0 がリリースされました。 - monoe&#x27;s blog - Site Home - MSDN Blogs")

----

## Node v0.10.32 (Stable)
[blog.nodejs.org/2014/09/16/node-v0-10-32-stable/](http://blog.nodejs.org/2014/09/16/node-v0-10-32-stable/ "Node v0.10.32 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.10.32 リリース。

----

## React v0.11.2 | React
[facebook.github.io/react/blog/2014/09/16/react-v0.11.2.html](http://facebook.github.io/react/blog/2014/09/16/react-v0.11.2.html "React v0.11.2 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">facebook</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.11.2リリース。

dialogとpicture要素のサポート、flowの型チェックツール用のアノテーションを取り除くフラグをjsxコマンドに追加

----

## Polymer 0.4.1 Released!
[blog.polymer-project.org/releases/2014/09/18/release-0.4.1/](http://blog.polymer-project.org/releases/2014/09/18/release-0.4.1/ "Polymer 0.4.1 Released!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 0.4.1リリース。

WAI-ARIAについての`core-a11y-keys`要素を追加、

iOS8のバグに対するworkaroundを追加

----
<h1 class="site-genre">アーティクル</h1>

----

## Updates to our platform roadmap - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/09/18/updates-to-our-platform-roadmap.aspx](http://blogs.msdn.com/b/ie/archive/2014/09/18/updates-to-our-platform-roadmap.aspx "Updates to our platform roadmap - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

IEの開発中、検討中の機能について

- [Internet Explorer Web Platform Status and Roadmap - status.modern.IE](http://status.modern.ie/ "Internet Explorer Web Platform Status and Roadmap - status.modern.IE")

----

## iOS 8 and iPhone 6 for web developers and designers: next evolution for Safari and native webapps | Breaking the Mobile Web
[www.mobilexweb.com/blog/safari-ios8-iphone6-web-developers-designers](http://www.mobilexweb.com/blog/safari-ios8-iphone6-web-developers-designers "iOS 8 and iPhone 6 for web developers and designers: next evolution for Safari and native webapps | Breaking the Mobile Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

iPhone6とplusの仕様やviewportまわりの違い、iOS8 safariでサポートされたAPIやCSSサポート、minimal-uiの廃止、safariの追加機能、UIWebViewとWKWebVIewの違い、バグについて詳しくまとめられている

- [iOS8 presents serious issues that prevent file uploading | Blog](http://blog.fineuploader.com/2014/09/10/ios8-presents-serious-issues-that-prevent-file-uploading/ "iOS8 presents serious issues that prevent file uploading | Blog")

----

## Apple Shows Love for HTML5 with iOS 8 | Blog | Sencha
[www.sencha.com/blog/apple-shows-love-for-html5-with-ios-8](http://www.sencha.com/blog/apple-shows-love-for-html5-with-ios-8 "Apple Shows Love for HTML5 with iOS 8 | Blog | Sencha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">performance</span></p>

iOS8のSafariでサポートされた新しい機能について。

また今までのWebViewと新しく追加されたWebKitの機能がちゃんと使えるWKWerbViewのパフォーマンスの比較。

既知のバグについても書かれてる

- [iOS 8 に Apple の HTML5 への愛を見た | 株式会社ゼノフィ](https://www.xenophy.com/sencha-blog/11578 "iOS 8 に Apple の HTML5 への愛を見た | 株式会社ゼノフィ")

----

## Node.jsエンジニアなら2014年内に知っておきたいPromise入門 | Tokyo Otaku Mode Tech Blog
[blog.otakumode.com/2014/09/17/nodejs-promise/](http://blog.otakumode.com/2014/09/17/nodejs-promise/ "Node.jsエンジニアなら2014年内に知っておきたいPromise入門 | Tokyo Otaku Mode Tech Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Promises</span> <span class="jser-tag">tutorial</span></p>

JavaScript Promiseの基本的な使い方、async.jsを使っていた場合にそれをPromiseに書き換える実装方法について。

Promiseについてよくまとまってるチュートリアル

----

## JavaScript Promiseを使うウェブの仕様を調べてみた | Web Scratch
[efcl.info/2014/09/16/promises-spec-ref-list/](http://efcl.info/2014/09/16/promises-spec-ref-list/ "JavaScript Promiseを使うウェブの仕様を調べてみた | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">spec</span> <span class="jser-tag">検索</span></p>

Promisesの仕様を前提にしてる仕様の一覧。また、仕様をどうやって調べるかについて。W3CやWHATWGの仕様をまとめてダウンロードして検索する方法について書かれてる

----

## Node.js Best Practices
[blog.risingstack.com/node-js-best-practices/](http://blog.risingstack.com/node-js-best-practices/ "Node.js Best Practices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">開発環境</span></p>

Node.jsにおけるコーディングルール的なのとエラーについて。

callbackのerrorはチェックする事と早期return、Operational errorとProgrammer errorsの違いと対処、npmを使ったWorkflowについて書かれてる

- [Error Handling in Nodejs - Developer Center - Joyent](http://www.joyent.com/developers/node/design/errors "Error Handling in Nodejs - Developer Center - Joyent")

----

## Traceur, Gulp, Browserify and ES6 - Matt Greer
[www.mattgreer.org/articles/traceur-gulp-browserify-es6/](http://www.mattgreer.org/articles/traceur-gulp-browserify-es6/ "Traceur, Gulp, Browserify and ES6 - Matt Greer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">gulp</span> <span class="jser-tag">browserify</span></p>

Gulp+TraceurでES6のコードを使う方法と、Browserify + es6ifyでTraceurを使う方法について。

----

## 透過PNGをSVGを利用して軽くするテクニック - Weblog - Hail2u.net
[hail2u.net/blog/webdesign/with-svg.html](http://hail2u.net/blog/webdesign/with-svg.html "透過PNGをSVGを利用して軽くするテクニック - Weblog - Hail2u.net")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">画像</span></p>

JPG画像とマスクとなるPNG画像をsvgのmask要素を合わせる事で擬似アルファチャネルをやる事について。

単体の透過pngよりサイズサイズが軽量に出来る話。

<a href='http://blog.jackadam.net/2010/alpha-jpegs/'>http://blog.jackadam.net/2010/alpha-jpegs/</a>

----

## CSSセレクターマッチングのコスト - Unreviewed
[takenspc.hatenablog.com/entry/2014/09/16/152157](http://takenspc.hatenablog.com/entry/2014/09/16/152157 "CSSセレクターマッチングのコスト - Unreviewed")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">webkit</span></p>

CSSセレクタは要素とセレクタの数だけ判定を行う回数が増えるため、そのコストを減らすアプローチについて。

また、CSSセレクタのマッチ判定の手順について結合子別に詳しく解説してる。

- [WebKit CSS JIT Internals - Constellation Scorpius](http://constellation.github.io/blog/2014/07/14/webkit-css-jit-internals/ "WebKit CSS JIT Internals - Constellation Scorpius")

----

## WebStorm 9 EAP, 138.2406: spy-js code completion, CSS3 enhancements, Scratch files and… JSX | JetBrains WebStorm Blog
[blog.jetbrains.com/webstorm/2014/09/webstorm-9-eap-138-2406/](http://blog.jetbrains.com/webstorm/2014/09/webstorm-9-eap-138-2406/ "WebStorm 9 EAP, 138.2406: spy-js code completion, CSS3 enhancements, Scratch files and… JSX | JetBrains WebStorm Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">node.js</span></p>

spy.jsを実行した結果を使ったコード補完が行えるように。また、今までは引数や返り値のみだったか、式にも対応した。

emacsみたいなScratchファイルの機能を追加、indexingの範囲をデフォルトではnode_moduleまでに限定、JSX(React)のサポート改善等

----

## WebIDE、ストレージインスペクタ、jQuery イベント、iframe 切り替えなど – Firefox 開発ツール エピソード 34 | Mozilla Developer Street (modest)
[dev.mozilla.jp/2014/09/webide-storage-inspector-jquery-events-iframe-switcher-more-firefox-developer-tools-episode-34/](https://dev.mozilla.jp/2014/09/webide-storage-inspector-jquery-events-iframe-switcher-more-firefox-developer-tools-episode-34/ "WebIDE、ストレージインスペクタ、jQuery イベント、iframe 切り替えなど – Firefox 開発ツール エピソード 34 | Mozilla Developer Street (modest)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

Firefox 34 で追加されてる開発ツールの機能について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Slide decks of JSConf 2014
[gist.github.com/nikcorg/1fe60d2da6e22653806c](https://gist.github.com/nikcorg/1fe60d2da6e22653806c "Slide decks of JSConf 2014")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">event</span> <span class="jser-tag">スライド</span></p>

JSConf.eu 2014のスライドまとめ

<a href='http://2014.jsconf.eu/'>http://2014.jsconf.eu/</a>

<a href='https://www.youtube.com/user/jsconfeu/'>https://www.youtube.com/user/jsconfeu/</a>

----

## A Quick Introduction to BrowserSync - Tuts+ Web Design Tutorial
[webdesign.tutsplus.com/tutorials/a-quick-introduction-to-browsersync--cms-22135](http://webdesign.tutsplus.com/tutorials/a-quick-introduction-to-browsersync--cms-22135 "A Quick Introduction to BrowserSync - Tuts+ Web Design Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">動画</span> <span class="jser-tag">Tools</span></p>

BrowserSyncについて紹介するスクリーンキャスト

----

## Syncing Async
[www.slideshare.net/fitc_slideshare/syncingasync](http://www.slideshare.net/fitc_slideshare/syncingasync "Syncing Async")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">スライド</span></p>

非同期処理とPromiseについてのスライド。

コールバックのネストの問題、PromiseやGeneratorで考える非同期で逐次的な処理について。

----

## CORS для тестирования и для жизни. Константин Якушев. MoscowJS 14
[www.slideshare.net/moscowjs/cors-moscowjs-14](http://www.slideshare.net/moscowjs/cors-moscowjs-14 "CORS для тестирования и для жизни. Константин Якушев. MoscowJS 14")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">XHR</span> <span class="jser-tag">スライド</span></p>

CORSのHTTPヘッダの設定と動作について分かりやすくまとめられてる。 

指定する値の書き方についてが分かりやすい

CORS in Actionの人。

----

## Componentization for Reality
[ja.slideshare.net/ygoto3q/componentization-for-reality](http://ja.slideshare.net/ygoto3q/componentization-for-reality "Componentization for Reality")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

コンポーネントベースで考えるウェブ開発についてスライド。

ディレクトリ単位だとバラけてしまうのでコンポーネント単位でまとめる。

ジェネレータ、webpack、insertCSS、Angular

- [俺の話を聞け、5分だけでもいい　ーJavaScriptだいすきな男たちとJavaScriptを学ぼう！【JSオジサン#3】 JSオジサン 先生 - 無料動画学習｜schoo（スクー）](https://schoo.jp/class/1190 "俺の話を聞け、5分だけでもいい　ーJavaScriptだいすきな男たちとJavaScriptを学ぼう！【JSオジサン#3】 JSオジサン 先生 - 無料動画学習｜schoo（スクー）")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## wingify/dom-comparator
[github.com/wingify/dom-comparator](https://github.com/wingify/dom-comparator "wingify/dom-comparator")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

2つのDOM文字列を比較した結果を取得するライブラリ。

CSSやNodeにどういう操作が行われたかの情報が取れる

----

## ConradIrwin/async-profile
[github.com/ConradIrwin/async-profile](https://github.com/ConradIrwin/async-profile "ConradIrwin/async-profile")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span></p>

node.jsで非同期処理のプロファイルを取るためのライブラリ。callback待ちにどれくらいの時間を使ってるかの表示、

非同期処理の結果をネスト表示も出来る

- [A CPU Profiler for Node.js - Bugsnag](https://bugsnag.com/blog/async-profile "A CPU Profiler for Node.js - Bugsnag")

----

## matthew-andrews/denodeify
[github.com/matthew-andrews/denodeify/](https://github.com/matthew-andrews/denodeify/ "matthew-andrews/denodeify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

nodeスタイルで書かれた関数(error, response)をPromiseラッパにするライブラリ

----

## deloreanjs/delorean
[github.com/deloreanjs/delorean](https://github.com/deloreanjs/delorean "deloreanjs/delorean")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Flux patternの実装ライブラリ

dispatcherとstore、ComponentとしてReactやFlight、Ractiveなどと組み合わせて使うことができる

- [Fluxxor - Home](http://fluxxor.com/ "Fluxxor - Home")

----

## fat/bean
[github.com/fat/bean](https://github.com/fat/bean "fat/bean")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">event</span></p>

JavaScriptのDOMイベントを簡単に扱える小さなライブラリ。

on/off/fire/one/cloneが用意されている。cloneではNodeと共にeventをコピーすることができる

----

## inikulin/dmn
[github.com/inikulin/dmn](https://github.com/inikulin/dmn "inikulin/dmn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

プロジェクトで使ってるファイルからら.npmignoreを生成するコマンドラインツール。

また、インストール済みのnode_modulesから不要なファイルを削除する事も出来る。

----