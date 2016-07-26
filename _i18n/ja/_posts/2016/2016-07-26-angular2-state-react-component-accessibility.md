---
title: "2016-07-26のJS: AngularJS 2でのState管理、React Componentパターン、アクセシビリティガイドライン"
author: azu
layout: post
date : 2016-07-26T09:43
category: JSer
tags:
    - Angular2
    - React
    - Accessibility

---

JSer.info #289 - [Tackling State — angular2](https://vsavkin.com/managing-state-in-angular-2-applications-caf78d123d02)という記事ではAngular 2のアプリケーションにおけるState管理について書かれています。

作り的にはReduxなどと似ていますが、次のような事をAngular 2 + RxJSで効率的に実装するにはどうするかが書かれています。

- Immutable Stateである
- ActionによってのみStateは変更される
- ApplicationはObservableを受け取りObservableを返すもの
- ApplicationとViewは分離される

----

[React.js in patterns](http://krasimirtsonev.com/blog/article/react-js-in-design-patterns)という記事ではReact Component + JSXの色々なパターンについて書かれています。

コンポーネント同士を組み合わせて使う方法や、`this.props.children`を使ったやり方、高階関数を使う方法など色々なパターンについて書かれています。

高階関数を使ったコンポーネントについては以下の記事も見てみると良いです。

- [Mixins Considered Harmful | React](https://facebook.github.io/react/blog/2016/07/13/mixins-considered-harmful.html "Mixins Considered Harmful | React")

-----

[Vox Product Accessibility Guidelines](http://accessibility.voxmedia.com/)というサイトではアクセシビリティのガイドラインが公開されています。

職種ごとのチェックリストが書かれていて、また根拠となるドキュメントへのリンクがまとまっているためそちらを参照してみるといいかもしれません。

- Designers
- Engineers
- Project Managers
- QA
- Editorial

チェックリスト自体は結構ざっくりとした内容が多いですが、一度見てみると面白いかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Dojo Recap – June, 2016 | The Dojo Toolkit Blog
[dojotoolkit.org/blog/dojo-recap-june-2016](http://dojotoolkit.org/blog/dojo-recap-june-2016 "Dojo Recap – June, 2016 | The Dojo Toolkit Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Dojo 1.11.2リリース。
またDojo 2の進捗について

----

## Release 2.0.1 · jquery/qunit
[github.com/jquery/qunit/releases/tag/2.0.1](https://github.com/jquery/qunit/releases/tag/2.0.1 "Release 2.0.1 · jquery/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.0.1リリース。
Symbolのダンプができるように

----

## Qt WebBrowser 1.0 - Qt Blog
[blog.qt.io/blog/2016/07/18/qt-webbrowser-1-0/](http://blog.qt.io/blog/2016/07/18/qt-webbrowser-1-0/ "Qt WebBrowser 1.0 - Qt Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span></p>

Qt WebBrowser 1.0リリース。
Qt WebEngine(Chromium)を使ったブラウザ。

----

## Release Notes for Safari Technology Preview Release 9 | WebKit
[webkit.org/blog/6800/release-notes-for-safari-technology-preview-release-9/](https://webkit.org/blog/6800/release-notes-for-safari-technology-preview-release-9/ "Release Notes for Safari Technology Preview Release 9 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 9リリース。

----

## V8 JavaScript Engine: V8 Release 5.3
[v8project.blogspot.com/2016/07/v8-release-53.html](http://v8project.blogspot.com/2016/07/v8-release-53.html "V8 JavaScript Engine: V8 Release 5.3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.3リリース。
Ignition Interpreterの追加、Promiseのパフォーマンス改善、V8 APIの変更など

- [Ignition: An Interpreter for V8 \[BlinkOn\] - Google スライド](https://docs.google.com/presentation/d/1OqjVqRhtwlKeKfvMdX6HaCIu9wpZsrzqpIVIwQSuiXQ/edit#slide=id.ge4ef702cb_2_20 "Ignition: An Interpreter for V8 \[BlinkOn\] - Google スライド")

----
<h1 class="site-genre">アーティクル</h1>

----

## Why object literals in JavaScript are cool
[rainsoft.io/why-object-literals-in-javascript-are-cool/](https://rainsoft.io/why-object-literals-in-javascript-are-cool/ "Why object literals in JavaScript are cool")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScriptのオブジェクトリテラルについて。
プロパティの定義やES2015のshorthandやcomputed property nameについて

----

## The Most In-Depth Yet Understandable ES6 Destructuring Tutorial (complete with Assembled Avengers) | Untangled
[untangled.io/in-depth-es6-destructuring-with-assembled-avengers/](http://untangled.io/in-depth-es6-destructuring-with-assembled-avengers/ "The Most In-Depth Yet Understandable ES6 Destructuring Tutorial (complete with Assembled Avengers) | Untangled")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES2015のDestructuringの挙動についての記事。
大量のサンプルと共に複雑なパターンのDestructuringについてを解説してる。
またDestructuringを応用した使い方についてなど

- [Advanced ES6 Destructuring Techniques | Untangled](http://untangled.io/advanced-es6-destructuring-techniques/ "Advanced ES6 Destructuring Techniques | Untangled")

----

## 6 compelling use cases for ES6 proxies
[devbryce.com/use-cases-for-es6-proxies/](http://devbryce.com/use-cases-for-es6-proxies/ "6 compelling use cases for ES6 proxies")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">proxy</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Proxy APIのユースケースについて。
バリデーション、private、ログ、変更禁止、`Proxy.revocable`について

----

## Tackling State — angular2
[vsavkin.com/managing-state-in-angular-2-applications-caf78d123d02](https://vsavkin.com/managing-state-in-angular-2-applications-caf78d123d02 "Tackling State — angular2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">AngularJS</span></p>

AngularJS 2とRxJSでのstate管理について。

Immutable State、ActionによってStateは変更される。
ApplicationはObservableを受け取りObservableを返す、ApplicationとViewは分離される。
これらのコンセプトをどのように実現するかについてかかれている。

----

## React.js in patterns
[krasimirtsonev.com/blog/article/react-js-in-design-patterns](http://krasimirtsonev.com/blog/article/react-js-in-design-patterns "React.js in patterns")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React Componentのパターン。
コンポーネントの入れ子や`this.props.children`、propsのやり取り、コンポーネント間のstate管理、DIについてなど

----

## Debugging the Production Web — Medium
[medium.com/@jrullmann/debugging-the-production-web-d36373b9440](https://medium.com/@jrullmann/debugging-the-production-web-d36373b9440 "Debugging the Production Web — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

本番のウェブアプリケーションのログについて。
ブラウザからどのようなログをどのように集めるか、手順をどのように再現するか、DevToolsについて

----

## Create Apps with No Configuration | React
[facebook.github.io/react/blog/2016/07/22/create-apps-with-no-configuration.html](https://facebook.github.io/react/blog/2016/07/22/create-apps-with-no-configuration.html "Create Apps with No Configuration | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">console</span></p>

設定なしでReactアプリを書き始められるツール。
`npm start`でサーバを立てて、`npm run build`でビルドできる。
`npm run eject`でロックインから外れる事ができる。

- [facebookincubator/create-react-app: Create React apps with no build configuration.](https://github.com/facebookincubator/create-react-app "facebookincubator/create-react-app: Create React apps with no build configuration.")

----

## The Service Worker Lifecycle
[bitsofco.de/the-service-worker-lifecycle/](https://bitsofco.de/the-service-worker-lifecycle/ "The Service Worker Lifecycle")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span></p>

ServiceWorkerのライフサイクルについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Vox Product Accessibility Guidelines
[accessibility.voxmedia.com/](http://accessibility.voxmedia.com/ "Vox Product Accessibility Guidelines")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span></p>

Vox Mediaのアクセシビリティガイドライン。
職種ごとにチェックリストが書かれている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Object Model
[objectmodel.js.org/](http://objectmodel.js.org/ "Object Model")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

プロパティの型定義したモデルクラスを作れるライブラリ

----

## nodeca/pica: Resize image in browser with high quality and high speed
[github.com/nodeca/pica](https://github.com/nodeca/pica "nodeca/pica: Resize image in browser with high quality and high speed")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span> <span class="jser-tag">library</span></p>

TypedArray、WebWorker、WebGLを使った画像リサイズライブラリ。

----

## stefanjudis/forrest: An npm scripts desktop client
[github.com/stefanjudis/forrest](https://github.com/stefanjudis/forrest "stefanjudis/forrest: An npm scripts desktop client")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">software</span></p>

npm run-scriptのGUIクライアント

----

## diegomura/react-log: React for the Console
[github.com/diegomura/react-log](https://github.com/diegomura/react-log "diegomura/react-log: React for the Console")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

console.logへの出力をJSXで書くことができるReact Component

----

## Download Blisk - a browser for web developers
[blisk.io/](https://blisk.io/ "Download Blisk - a browser for web developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

開発者向けの機能を持ったChromeベースのブラウザ。
モバイル向けの機能、自動更新、パフォーマンス やエラーの可視化など

----
<h1 class="site-genre">書籍関係</h1>

----

## Manning | Web Performance in Action
[www.manning.com/books/web-performance-in-action](https://www.manning.com/books/web-performance-in-action "Manning | Web Performance in Action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

2017年 春発売。
ウェブパフォーマンスについての書籍。
ブラウザでのレンダリング、HTTP/2などについて

----
