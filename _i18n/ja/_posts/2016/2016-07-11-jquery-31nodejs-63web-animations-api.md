---
title: "2016-07-11のJS: jQuery 3.1、Node.js 6.3、Web Animations API入門"
author: azu
layout: post
date : 2016-07-11T20:19
category: JSer
tags:
    - jQuery
    - Node.js
    - animation

---

JSer.info #287 - jQuery 3.1.0がリリースされました。

- [jQuery 3.1.0 Released – No More Silent Errors | Official jQuery Blog](http://blog.jquery.com/2016/07/07/jquery-3-1-0-released-no-more-silent-errors/)

jQuery 3.0では`jQuery.ready`はPromise A/+互換の[Deferred Object](https://api.jquery.com/category/deferred-object/ "Deferred Object")を使うようになっています。
そのため、次のようなコードは何もコンソールにエラーが表示されない状態になっていました。

```js
$(function() {
  throw new Error("This is Error");
});
// ≒
jQuery.ready.then(function() {
  throw new Error("This is Error");
});
```

いわゆる[unhandled rejection](http://azu.github.io/promises-book/#_%E6%B2%88%E9%BB%99%E3%81%97%E3%81%9F%E3%82%A8%E3%83%A9%E3%83%BC)となってしまうため、次のように`.catch`でエラーハンドリングを行う必要がありました。

```js
jQuery.ready.then(function() {
  throw new Error("This is Error");
}).catch(error => {
  console.error(error);
});
```

しかし、 `$()`はjQueryオブジェクトを返すため、エラーハンドリングを書くことができないという問題があります。

この問題についての詳細は [Bugsnag Blog - A Warning About jQuery 3](http://blog.bugsnag.com/a-warning-about-jquery-3 "Bugsnag Blog - A Warning About jQuery 3") で解説されています。

jQuery 3.1では今までと同じように`jQuery.ready`内で起きたエラーをコンソールに表示します。
(自動的に`.catch`してre-throwしています)

また、[jQuery.readyException()](http://api.jquery.com/jquery.readyexception/ "jQuery.readyException()")という専用のエラーを受け取るメソッドを定義できるようになっています。

- [Core: Re-throw errors that happened in callbacks wrapped in jQuery ready by mgol · Pull Request #3210 · jquery/jquery](https://github.com/jquery/jquery/pull/3210 "Core: Re-throw errors that happened in callbacks wrapped in jQuery ready by mgol · Pull Request #3210 · jquery/jquery")

ついでにJavaScript Promiseの本もjQuery 3.xに対応した更新をしています。

- [Release 1.6.0 · azu/promises-book](https://github.com/azu/promises-book/releases/tag/1.6.0 "Release 1.6.0 · azu/promises-book")

-----
[Node v6.3.0](https://nodejs.org/en/blog/release/v6.3.0/)がリリースされました。

`--inspect`のコマンドライン引数をつけてNode.jsを起動することで、Node.jsアプリに対してChromeの開発者ツールでリモートデバッグできるようになります。
CLIなどは一瞬で終わってしまうので、`--debug-brk`オプションを付けるとブレークした状態で開始できます。

```
node --inspect --debug-brk
```

以下の記事も参考になります。

- [Debugging Node.js Nightlies with Chrome DevTools — Medium](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27#.6hsm7r89v "Debugging Node.js Nightlies with Chrome DevTools — Medium")

----

[Web Animations APIの基本的な使い方・まとめ](http://www.h2.dion.ne.jp/%7Edefghi/webanim/webanim.htm)というサイトでは、[Web Animations](https://w3c.github.io/web-animations/ "Web Animations") APIについて機能や挙動について学ぶ事ができます。

大量のサンプルと共に見ることができるので、興味がある人は見てみると良いです。

既にCSSアニメーションなどがあるのに、Web Animationsという仕様がでてきたのは以下のスライドを見てみるのが分かりやすいかもしれません。

- [真面目なアニメーション (html5j 2013, Web Animations)](http://www.slideshare.net/brianskold/html5j-2013 "真面目なアニメーション (html5j 2013, Web Animations)")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## jQuery 3.1.0 Released – No More Silent Errors | Official jQuery Blog
[blog.jquery.com/2016/07/07/jquery-3-1-0-released-no-more-silent-errors/](http://blog.jquery.com/2016/07/07/jquery-3-1-0-released-no-more-silent-errors/ "jQuery 3.1.0 Released – No More Silent Errors | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.1.0リリース。
`jQuery.readyException`で`ready`時に起きたエラーのログを取れるように

- [Bugsnag Blog - A Warning About jQuery 3](http://blog.bugsnag.com/a-warning-about-jquery-3 "Bugsnag Blog - A Warning About jQuery 3")

----

## angular/CHANGELOG.md at 2.0.0-rc.4 · angular/angular
[github.com/angular/angular/blob/2.0.0-rc.4/CHANGELOG.md](https://github.com/angular/angular/blob/2.0.0-rc.4/CHANGELOG.md "angular/CHANGELOG.md at 2.0.0-rc.4 · angular/angular")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2 RC4リリース。
テスト周りの構造が大きく変化し、JasmineではなくMochaでもテストを実行できるようになるなど

- [Angular 2 RC.4の変更点 | Angular2 Info](http://ng2-info.github.io/2016/07/08/angular-2-rc-4/ "Angular 2 RC.4の変更点 | Angular2 Info")
- [Cannot use Mocha to write angular2 tests · Issue #5395 · angular/angular](https://github.com/angular/angular/issues/5395 "Cannot use Mocha to write angular2 tests · Issue #5395 · angular/angular")

----

## Node v6.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.3.0/](https://nodejs.org/en/blog/release/v6.3.0/ "Node v6.3.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.3.0リリース。
`buffer.swap64()`の追加、shared libraryとしてNode.jsを使えるようにビルドオプションの追加、`setImmediate()`のパフォーマンス改善、V8 inspectorを実験的にサポートしChromeの開発者ツールでデバッグできるようになるなど

- [Debugging Node.js Nightlies with Chrome DevTools — Medium](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27 "Debugging Node.js Nightlies with Chrome DevTools — Medium")

----

## Release Notes for Safari Technology Preview Release 8 | WebKit
[webkit.org/blog/6744/release-notes-for-safari-technology-preview-release-8/](https://webkit.org/blog/6744/release-notes-for-safari-technology-preview-release-8/ "Release Notes for Safari Technology Preview Release 8 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 8リリース。
ES6の実装完了、Apple Payのコードをリポジトリに移動、`:focus-within`のサポートなど

----
<h1 class="site-genre">アーティクル</h1>

----

## Teach Access Portal
[teachaccess.github.io/tutorial/](https://teachaccess.github.io/tutorial/ "Teach Access Portal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">tutorial</span></p>

WAI-ARIAなどのaccessibleなHTMLの書き方のチュートリアル。
実際に書きながら試す事ができる

----

## Accessible SVGs | CSS-Tricks
[css-tricks.com/accessible-svgs/](https://css-tricks.com/accessible-svgs/ "Accessible SVGs | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">WAI-ARIA</span></p>

AccessibleなSVGの作り方について

----

## metagrover/ES6-for-humans: A kickstarter guide to writing ES6.
[github.com/metagrover/ES6-for-humans](https://github.com/metagrover/ES6-for-humans "metagrover/ES6-for-humans: A kickstarter guide to writing ES6.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

ES6で増えた構文や機能の簡単な紹介

----

## How well do you know CSS display?
[www.chenhuijing.com/blog/how-well-do-you-know-display/](https://www.chenhuijing.com/blog/how-well-do-you-know-display/ "How well do you know CSS display?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSSのdisplayプロパティに指定できる値とそれぞれの挙動についての解説

----

## Backbone.jsにReduxを導入してみる - Qiita
[qiita.com/takeshy/items/2bca340ffa157841a482](http://qiita.com/takeshy/items/2bca340ffa157841a482 "Backbone.jsにReduxを導入してみる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">redux</span></p>

Backbone.jsのみで管理していたStateをReduxを使い管理するようにしてみた話。
redux-devtools-extensionを使ってStateの変化を確認する方法について

- [Mihail Diordiev - Debugging flux applications in production at react-europe 2016 - YouTube](https://www.youtube.com/watch?v=cbXLohVbzNI "Mihail Diordiev - Debugging flux applications in production at react-europe 2016 - YouTube")
- [redux-devtools-extension](https://github.com/zalmoxisus/redux-devtools-extension "redux-devtools-extension")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## BlinkOn 6 - Munich, Germany - YouTube
[www.youtube.com/watch?v=iCSAUHpPbiU](https://www.youtube.com/watch?v=iCSAUHpPbiU "BlinkOn 6 - Munich, Germany - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">動画</span></p>

BlinkOn 6の動画一覧

- [BlinkOn6 One Pager - Google ドキュメント](https://docs.google.com/document/d/1eYSF1eUAJefn2mRyY6saUzQc4JWQE3tZZhwgLjohvDY/preview "BlinkOn6 One Pager - Google ドキュメント")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Animations APIの基本的な使い方・まとめ
[www.h2.dion.ne.jp/~defghi/webanim/webanim.htm](http://www.h2.dion.ne.jp/~defghi/webanim/webanim.htm "Web Animations APIの基本的な使い方・まとめ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">animation</span> <span class="jser-tag">API</span> <span class="jser-tag">JavaScript</span></p>

Web Animations APIについての解説サイト。
実際に動かしながらアニメーションの作成方法について学ぶことができる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## paulirish/devtools-timeline-model: Parse raw trace data into the Chrome DevTools&#x27; structured profiling data models
[github.com/paulirish/devtools-timeline-model](https://github.com/paulirish/devtools-timeline-model "paulirish/devtools-timeline-model: Parse raw trace data into the Chrome DevTools' structured profiling data models")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

Chrome開発者ツールのTimelineデータの処理ライブラリ

----

## boopathi/babel-minify: Some babel plugins and tools to minify ES6+ code
[github.com/boopathi/babel-minify](https://github.com/boopathi/babel-minify "boopathi/babel-minify: Some babel plugins and tools to minify ES6+ code")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">library</span></p>

Babelでminifyをするプラグインのpreset。
使ってないコードの削除、インライン化、mangleなどを行う

----

## filipelinhares/ress: A modern CSS reset
[github.com/filipelinhares/ress](https://github.com/filipelinhares/ress "filipelinhares/ress: A modern CSS reset")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

normalize.cssにいくつかデフォルト値やresetを追加したもの

----

## thejameskyle/assert-equal-jsx: assertEqualJSX
[github.com/thejameskyle/assert-equal-jsx](https://github.com/thejameskyle/assert-equal-jsx "thejameskyle/assert-equal-jsx: assertEqualJSX")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

JSXのタグ同士の比較を行うassertionライブラリ

----

## declandewet/common-tags: Useful template literal tags for dealing with strings in ES2015+
[github.com/declandewet/common-tags](https://github.com/declandewet/common-tags "declandewet/common-tags: Useful template literal tags for dealing with strings in ES2015+")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

Tagged Templateとして使える関数ライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript Functions… by Amin Meyghani [PDF/iPad/Kindle]
[leanpub.com/javascript-closure](https://leanpub.com/javascript-closure "JavaScript Functions… by Amin Meyghani \[PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScriptの関数やクロージャー、prototypeなどについて扱う書籍。
$0から購入できる

----

## Practical… by Daniel Schmitz et al. [Leanpub PDF/iPad/Kindle]
[leanpub.com/vue](https://leanpub.com/vue "Practical… by Daniel Schmitz et al. \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Vue.jsについて書籍

----
