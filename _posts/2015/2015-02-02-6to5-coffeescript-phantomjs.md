---
title: "2015-02-02のJS: 6to5 Ver3.0、CoffeeScript 1.9.0、PhantomJS 2.0"
author: azu
layout: post
date : 2015-02-02T20:09
category: JSer
tags:
    - ES6
    - CoffeeScript
    - webkit

---

JSer.info #213 - ES6+αのコードをES5へ変換するツールである6to5のVer3.0がリリースされました。(現在[3.3.4](https://github.com/6to5/6to5/blob/v3.3.4/CHANGELOG.md "3.3.4")まででています)

- [2to3 · 6to5](http://6to5.org/blog/2015/01/27/2to3/ "2to3 · 6to5")

オプションを削除やリネームし整理していて、また[Transformers](http://6to5.org/docs/usage/transformers/ "Transformers")について互換性のない変更が含まれています。

また6to5プロジェクトとして、ES6とES5に限定してるように見える名前の変更や、今後フォーカスを当てていく箇所についての意見を募集しているようです。

- [Name suggestions · Issue #596 · 6to5/6to5](https://github.com/6to5/6to5/issues/596)
- [Project scope and future · Issue #568 · 6to5/6to5](https://github.com/6to5/6to5/issues/568 "Project scope and future · Issue #568 · 6to5/6to5")

----

[CoffeeScript](http://coffeescript.org/#1.9.0 "CoffeeScript") 1.9.0がリリースされました。

Generatorの構文をサポートやパースエラー等のエラーメッセージが改善されました。

- [CoffeeScriptが1.9でgenerator構文をサポート - Qiita](http://qiita.com/mizchi/items/39906871bc0a532b6e71 "CoffeeScriptが1.9でgenerator構文をサポート - Qiita")

----

ヘッドレスブラウザの[PhantomJS 2.0](http://phantomjs.org/release-2.0.html "PhantomJS 2.0")がリリースされました。

またダウンロード出来る一部バイナリがおかしいですが、Qt5へのアップデートをしたためQtWebKitも更新されています。

- [Release of PhantomJS 2.0 · Issue #12897 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/12897#issuecomment-71651159 "Release of PhantomJS 2.0 · Issue #12897 · ariya/phantomjs")

Qtでは[QtWebEngine](http://qt-project.org/wiki/QtWebEngine "QtWebEngine")というChroniumベースのがあるため、今後のアップデートでここも変わるかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## React v0.13.0 Beta 1 | React
[facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html](http://facebook.github.io/react/blog/2015/01/27/react-v0.13.0-beta-1.html "React v0.13.0 Beta 1 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 0.13 β1リリース。
ES6 ClassでReact.Componentを書けるように

----

## 2to3 · 6to5
[6to5.org/blog/2015/01/27/2to3](https://6to5.org/blog/2015/01/27/2to3 "2to3 · 6to5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

6to5 3.0リリース。
コマンドラインオプションに`--blacklist`と`--whitelist`の追加、パフォーマンス改善、細かいオプションの変更等。

- [Name suggestions · Issue #596 · 6to5/6to5](https://github.com/6to5/6to5/issues/596 "Name suggestions · Issue #596 · 6to5/6to5")

----

## CoffeeScript
[coffeescript.org](http://coffeescript.org "CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">ReleaseNote</span></p>

CoffeeScript 1.9.0リリース。
ES6 generatorsのサポート

----

## Node v0.10.36 (Stable)
[blog.nodejs.org/2015/01/26/node-v0-10-36-stable/](http://blog.nodejs.org/2015/01/26/node-v0-10-36-stable/ "Node v0.10.36 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.10.36リリース。

----

## Dev.Opera — Opera 27 released
[dev.opera.com/blog/opera-27/](https://dev.opera.com/blog/opera-27/ "Dev.Opera — Opera 27 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 27 (based on Chromium 40) リリース。
minlength属性、form要素の`reportValidity()`の実装、CSP Lv2の実装、Service Workers等

----

## PhantomJS 2.0 Release Notes | PhantomJS
[phantomjs.org/release-2.0.html](http://phantomjs.org/release-2.0.html "PhantomJS 2.0 Release Notes | PhantomJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

ヘッドレスブラウザのPhantomJS 2.0リリース。 QtとWebkitのアップデート、CoffeeScriptのデフォルトサポートを廃止


----
<h1 class="site-genre">アーティクル</h1>

----

## Replace CoffeeScript with ES6
[robots.thoughtbot.com/replace-coffeescript-with-es6](http://robots.thoughtbot.com/replace-coffeescript-with-es6 "Replace CoffeeScript with ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

CoffeeScriptのSyntaxをES6に書き換える方法について
[eventualbuddha/decaffeinate](https://github.com/eventualbuddha/decaffeinate "eventualbuddha/decaffeinate") のようなツールではなくて、どういう対応のコードを示しながら解説している。

----

## New string features in ECMAScript 6
[www.2ality.com/2015/01/es6-strings.html](http://www.2ality.com/2015/01/es6-strings.html "New string features in ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6で追加されるString系のメソッドについて。
Template strings、ユニコードコードポイントを正しく扱う方法、追加された便利メソッドについて

----

## Surfin&#x27; Safari - Blog Archive » Building WebKit for iOS Simulator
[www.webkit.org/blog/3457/building-webkit-for-ios-simulator/](https://www.webkit.org/blog/3457/building-webkit-for-ios-simulator/ "Surfin&#x27; Safari - Blog Archive » Building WebKit for iOS Simulator")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span></p>

iOSシミュレータ向けにWebKitをビルド出来るように

----

## Canvas 2D: New docs, Path2D objects, hit regions ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/01/canvas-2d-new-docs-path2d-hit-regions/](http://hacks.mozilla.org/2015/01/canvas-2d-new-docs-path2d-hit-regions/ "Canvas 2D: New docs, Path2D objects, hit regions ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">canvas</span></p>

Canvas 2Dの機能として追加されたPath2Dについて

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 最近のASTパーサの動き
[azu.github.io/slide/crosushi/shift-ast.html](http://azu.github.io/slide/crosushi/shift-ast.html "最近のASTパーサの動き")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">スライド</span></p>

Esprima/Esprima-FB/espree、Shift AST、acorn/acorn-6to5とかのJS ASTパーサの近況についてのスライド。
EsprimaがjQuery Fundationに移管した話についてなど

----

## React.js Conf | January 28 &amp; 29 2015
[conf.reactjs.com/schedule.html](http://conf.reactjs.com/schedule.html "React.js Conf | January 28 &amp; 29 2015")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

React.js Confの動画まとめ

----

## React in 7 Minutes - React Video Tutorial #free @eggheadio
[egghead.io/lessons/react-react-in-7-minutes](https://egghead.io/lessons/react-react-in-7-minutes "React in 7 Minutes - React Video Tutorial #free @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">動画</span></p>

7分で分かるReact Componentのスクリーンキャスト。
JSX、Componentのネスト、stateとprops、イベントハンドラについて

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## MaxArt2501/object-observe
[github.com/MaxArt2501/object-observe](https://github.com/MaxArt2501/object-observe "MaxArt2501/object-observe")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Object.observeの限定的なpolyfill

----

## Contracts.js
[www.contractsjs.org/](http://www.contractsjs.org/ "Contracts.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">sweet.js</span> <span class="jser-tag">JavaScript</span></p>

sweet.jsを使った実行時型チェック的な機能を提供するマクロ

----

## is.js - micro check library
[arasatasaygin.github.io/is.js/](http://arasatasaygin.github.io/is.js/ "is.js - micro check library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`is.*`というメソッドで色々な種類の値をチェック出来るライブラリ。
型や正規表現、環境、時間等

----

## Fluxible | A Pluggable Container for Isomorphic Flux Applications | Fluxible
[www.fluxible.io/](http://www.fluxible.io/ "Fluxible | A Pluggable Container for Isomorphic Flux Applications | Fluxible")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Yahoo製のFlux実装ライブラリ。

----

## Ramda Documentation
[ramdajs.com/](http://ramdajs.com/ "Ramda Documentation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span> <span class="jser-tag">library</span></p>

undrescoreやlodashよりも関数型スタイル向けに沿った作りとする事を目的としたライブラリ。
Immutable、副作用の排除、関数同士を組み合わせしやすいようなインターフェースにしているのが特徴。

----

## Home | marty.js
[martyjs.org/](http://martyjs.org/ "Home | marty.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Fluxアーキテクチャ実装のライブラリ。
基本的なStore、Dispatcher、Actionがあり、追加でConstant値の作成、Storageを指定して管理出来るStateが用意されてる。
Chromeのデバッグで流れを見られるようになってる

----

## israelidanny/ie8linter
[github.com/israelidanny/ie8linter](https://github.com/israelidanny/ie8linter "israelidanny/ie8linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">Tools</span> <span class="jser-tag">browser</span></p>

IE8でサポートしてないタグやCSSプロパティ等を検出するツール。

----

## douglasduteil/isparta
[github.com/douglasduteil/isparta](https://github.com/douglasduteil/isparta "douglasduteil/isparta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

istanbulと6to5を使ったES6のコードカバレッジツール。

----

## timoxley/pkgfiles
[github.com/timoxley/pkgfiles](https://github.com/timoxley/pkgfiles "timoxley/pkgfiles")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

npm publishでどのファイルが公開されるのかをチェック出来るツール

----
