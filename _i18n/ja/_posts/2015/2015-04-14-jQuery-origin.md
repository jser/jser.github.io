---
title: "2015-04-14のJS: 初代jQueryをコードリーディング、npmのエコシステムとプロトタイピング"
author: azu
layout: post
date : 2015-04-14T23:06
category: JSer
tags:
    - jQuery
    - コードリーディング
    - npm
    - GitHub

---

browserify


JSer.info #223 - [John Resig - Annotated Version of the Original jQuery Release](http://ejohn.org/blog/annotated-version-of-the-original-jquery-release/ "John Resig - Annotated Version of the Original jQuery Release")ではjQueryの作者であるJohn ResigによるjQueryの初期バージョンのアノテーション付きソースコードが公開されています。

- [Genius | Annotate the world](http://genius.it/ejohn.org/files/jquery-original.html "Genius | Annotate the world")

<div class="kwout" style="text-align: center;"><a href="http://genius.it/5088390/ejohn.org/files/jquery-original.html"><img src="http://kwout.com/cutout/f/b5/rb/qs2_bor.jpg" alt="http://genius.it/5088390/ejohn.org/files/jquery-original.html" title="Genius | Annotate the world" width="600" height="482" style="border: none;" /></a><p style="margin-top: 10px; text-align: center;"><a href="http://genius.it/5088390/ejohn.org/files/jquery-original.html">Genius | Annotate the world</a> via <a href="http://kwout.com/quote/fb5rbqs2">kwout</a></p></div>


上記のページで公開されていて、jQueryの名前の由来、prototype.jsからインスパイアした`$`、メソッドチェーンの仕組み、CSS Selectorsの原点の話、タグ文字列からのDOM要素作成などjQueryの特徴的な機能がどういう意図で実装されていたのかを振り返る内容になっていてとても面白いと思います。

jQueryがJavaScriptに与えた影響は大きいので、2006年前後のブラウザやJavaScriptの歴史を振り返るような内容にもなっています。

ECMA標準では

----

[Rapid Prototyping in JavaScript](http://mattdesl.svbtle.com/rapid-prototyping "Rapid Prototyping in JavaScript")という記事では、[Browserify](http://browserify.org/ "Browserify")やnpmのエコシステムを使ってGitHubにウェブサイトを公開するまでの流れを紹介しています。

- [wtch](https://www.npmjs.com/package/wtch)
- [budo](https://www.npmjs.com/package/budo)
- [garnish](https://www.npmjs.com/package/garnish)
- [wzrd](https://www.npmjs.com/package/wzrd)

など目的別に小さなツールを組み合わせて、Live Reloadやプロトタイピングをしていく内容になっています。
また、プロジェクトのディレクトリ構成、リポジトリを作成する[ghrepo](https://github.com/mattdesl/ghrepo "ghrepo")やgh-pagesへのデプロイなどについて書かれているので、出てきたツールを使わない場合でも参考になる所はあると思います。

さっと使えてさっと公開できるのがJavaScriptやnpmのいいところでもあるので、こういうプロトタイピングを効率的に行う方法を模索してみるのも楽しいかもしれません。

----


<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint 0.19.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/04/eslint-0.19.0-released](http://eslint.org/blog/2015/04/eslint-0.19.0-released "ESLint 0.19.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.19.0リリース。
ASTのコミュニティ標準であるESTreeの仕様への追従が中心。

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#510](https://github.com/babel/babel/blob/master/CHANGELOG.md#510 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 5.1.0リリース。
trailing-function-commasのサポート、オブジェクトリテラルのメソッドに対するdecoratorsのサポートなど

- [Decorators in object literals trigger SyntaxError · Issue #1154 · babel/babel](https://github.com/babel/babel/issues/1154 "Decorators in object literals trigger SyntaxError · Issue #1154 · babel/babel")

関連してBabelを使ったコードもESLintでチェックできるプラグインbabel-eslintがBabel 5.xに対応。

- [babel/babel-eslint](https://github.com/babel/babel-eslint "babel/babel-eslint")

----

## The npm Blog — npm private modules are here!
[blog.npmjs.org/post/116379479775/npm-private-modules-are-here](http://blog.npmjs.org/post/116379479775/npm-private-modules-are-here "The npm Blog — npm private modules are here!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span></p>

npmのprivate modulesがオープン。
npmjsにscoped modulesをpublishすることが出来るようになり、それらのモジュールをprivateで利用できる$7/monthのサービス

----
<h1 class="site-genre">アーティクル</h1>

----

## Rapid Prototyping in JavaScript
[mattdesl.svbtle.com/rapid-prototyping](http://mattdesl.svbtle.com/rapid-prototyping "Rapid Prototyping in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">開発環境</span></p>

Browserify、wzrd、budoを使ったプロトタイピングについて。
ブラウザのリロードなしで変更を反映出来るHot Reloadingが出来るbudoをローカルサーバにして開発する流れ

- [mattdesl/budo](https://github.com/mattdesl/budo "mattdesl/budo")

----

## eval ソースをデバッグする - 開発ツール | MDN
[developer.mozilla.org/ja/docs/Tools/Debugger/How\_to/Debug\_eval\_sources](https://developer.mozilla.org/ja/docs/Tools/Debugger/How_to/Debug_eval_sources "eval ソースをデバッグする - 開発ツール | MDN")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">sourcemap</span> <span class="jser-tag">debug</span></p>

FirefoxやChromeの開発者ツールはevalやnew Function経由で実行されるコードに//# sourceURL=my-foo.js のような識別子があると通常のスクリプトと同等に扱えるので、ブレークポイントなどが可能になる。

----

## John Resig - Annotated Version of the Original jQuery Release
[ejohn.org/blog/annotated-version-of-the-original-jquery-release/](http://ejohn.org/blog/annotated-version-of-the-original-jquery-release/ "John Resig - Annotated Version of the Original jQuery Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">歴史</span> <span class="jser-tag">JavaScript</span></p>

jQuery作者によるjQueryの初期バージョンのコードにコメントをしたものが公開されてる。
メソッドチェインの仕組み、CSSセレクタとなるもの、文字列からのDOM要素作成など多くのライブラリに影響を与えたものがどういう考えで作られたのかが書かれていて面白い

- [Genius | Annotate the world](http://genius.it/ejohn.org/files/jquery-original.html "Genius | Annotate the world")

----

## Measuring Performance
[davidwalsh.name/measuring-performance](http://davidwalsh.name/measuring-performance "Measuring Performance")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

Navigation Timing API、Resource Timing APIといったパフォーマンス測定のためのブラウザAPIやWebPageTestなどの計測ツールやネットワーク環境のテストについての紹介

----

## Deploying ECMAScript 6
[www.2ality.com/2015/04/deploying-es6.html](http://www.2ality.com/2015/04/deploying-es6.html "Deploying ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">まとめ</span></p>

ES6関係のツール、試し方の簡潔なまとめ

----

## Timer APIs(Date.getTime, Date.now, performance.now, setTimeout, setInterval, requestAnimationFrame, setImmediate) with Canvas Animation - Qiita
[qiita.com/TypoScript/items/ae07b7fe5d5d8d526110](http://qiita.com/TypoScript/items/ae07b7fe5d5d8d526110 "Timer APIs(Date.getTime, Date.now, performance.now, setTimeout, setInterval, requestAnimationFrame, setImmediate) with Canvas Animation - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span></p>

JavaScriptの時刻を取得するAPIについて詳しい記事。
タイマーの分解能やベースクロックという考え方について

----

## A Detailed Explanation of JavaScript Game Loops and Timing | Isaac Sukin
[www.isaacsukin.com/news/2015/01/detailed-explanation-javascript-game-loops-and-timing](http://www.isaacsukin.com/news/2015/01/detailed-explanation-javascript-game-loops-and-timing "A Detailed Explanation of JavaScript Game Loops and Timing | Isaac Sukin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

JavaScriptで正しいメインループを実装するにはどうするかについて。

- [IceCreamYou/MainLoop.js](https://github.com/IceCreamYou/MainLoop.js "IceCreamYou/MainLoop.js")

----

## 関数型なAltJS、PureScriptの入門書を邦訳しました。 - Qiita
[qiita.com/hiruberuto/items/f1e048fc9a8ca51eddb2](http://qiita.com/hiruberuto/items/f1e048fc9a8ca51eddb2 "関数型なAltJS、PureScriptの入門書を邦訳しました。 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">翻訳</span></p>

PureScriptの入門書の翻訳

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Browser
[browser.hatenablog.com/](http://browser.hatenablog.com/ "Browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">blog</span> <span class="jser-tag">browser</span></p>

IEやSpartan等の情報を追ってるブログ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## alfredkam/yakojs
[github.com/alfredkam/yakojs](https://github.com/alfredkam/yakojs "alfredkam/yakojs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">SVG</span></p>

DOM-lessなグラフライブラリ。
SVGグラフを吐き出せるようにすることでサーバサイドでも同じ出力結果を出せるようにする目的

----

## MUI - Material Design CSS Framework
[www.muicss.com/](https://www.muicss.com/ "MUI - Material Design CSS Framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Material Design guidelinesに則ったデザインをするためのフレームワーク

----

## yahoo/blink-diff
[github.com/yahoo/blink-diff](https://github.com/yahoo/blink-diff "yahoo/blink-diff")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">画像</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span></p>

画像を比較してその差を出したり、一致するかをテストできるJavaScriptライブラリ。
どれくらいの差を許すか等も設定できる

----

## cburgmer/csscritic
[github.com/cburgmer/csscritic](https://github.com/cburgmer/csscritic "cburgmer/csscritic")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

CSSのレグレッションテストフレームワーク

----

## mojo-js/obj-stream
[github.com/mojo-js/obj-stream](https://github.com/mojo-js/obj-stream "mojo-js/obj-stream")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">browser</span></p>

Stream的なAPIを持ったライブラリ。
オブジェクトをStreamに流すことができ、EventEmitterを使ったStream的なものなのでブラウザでも動作する

----

## WebRx - Dynamic JavaScript User-Interfaces with ReactiveX
[webrxjs.org/](http://webrxjs.org/ "WebRx - Dynamic JavaScript User-Interfaces with ReactiveX")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span></p>

RxJSを使ったMVVMフレームワーク。
AngularやKnockoutJSからインスパイアしている部分がある。TypeScriptで書かれている

----

## mattdesl/budo
[github.com/mattdesl/budo](https://github.com/mattdesl/budo "mattdesl/budo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">開発環境</span> <span class="jser-tag">Tools</span></p>

Live Reloadする開発用のローカルサーバ。
https://github.com/caspervonb/amok のように、ブラウザの更新なしで変更を反映するHot Reloadingを行う拡張も持っている。

----

## RQ
[www.rq.crockford.com/](http://www.rq.crockford.com/ "RQ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Douglas Crockford製のPromiseハンドリングライブラリ。
sequence、parallel、race、fallbackなどの複数のPromiseの流れを扱うライブラリ

----
