---
title: "2016-04-11のJS: Grunt 1.0.0、React 15.0、ツールで学ぶJavaScript"
author: azu
layout: post
date : 2016-04-11T20:00
category: JSer
tags:
    - Grunt
    - React
    - Tutorial

---

JSer.info #274 - Grunt 1.0.0が正式リリースされました。

- [Grunt 1.0.0 released - Grunt: The JavaScript Task Runner](http://gruntjs.com/blog/2016-04-04-grunt-1.0.0-released "Grunt 1.0.0 released - Grunt: The JavaScript Task Runner")
- [JavaScript作業自動化ツール「Grunt 1.0.0」が登場。約2年もの開発停滞から復活 － Publickey](http://www.publickey1.jp/blog/16/javascriptgrunt_1002.html "JavaScript作業自動化ツール「Grunt 1.0.0」が登場。約2年もの開発停滞から復活 － Publickey")

1.0.0 RC1からは依存パッケージのアップデートがされていますが、`grunt.util._`で参照できるlodashが4.3.0に更新されています。
`grunt.util._`自体が非推奨であるため、以下のように自分でlodashをインストールして使うことが推奨されています。


```js
var _ = require('lodash');
```

----

[React v15.0](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")がリリースされました。

幾つか問題があったため、既に[React v15.0.1](https://facebook.github.io/react/blog/2016/04/08/react-v15.0.1.html "React v15.0.1")がリリースされていますが、基本的には0.14.xからは非推奨の警告メッセージがなければそのままアップグレードできるようです。

0.14.xからの変更点は以下にまとめられています。

- [React v15.0 | React](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")
- [React.js v15.0 changes - blog.koba04.com](http://blog.koba04.com/post/2016/03/09/react-js-v15-changes/ "React.js v15.0 changes - blog.koba04.com")

また、Reactのコアチームのミーティングノートが公開されるようになっているので、今後どのような方針でやっていくのかなどが書かれているので気になる人は見るといいかもしれません。

- [reactjs/core-notes: Weekly meeting notes from the React core team](https://github.com/reactjs/core-notes "reactjs/core-notes: Weekly meeting notes from the React core team")

----

[Tools to Learn JavaScript By Doing -Telerik Developer Network](http://developer.telerik.com/featured/tools-learn-javascript/ "Tools to Learn JavaScript By Doing -Telerik Developer Network")という記事ではツールで学ぶJavaScriptについて書かれています。

[NodeSchool](http://nodeschool.io/ja/ "NodeSchool")や[js-assessment](https://github.com/rmurphey/js-assessment "js-assessment")、[Advent of Code](http://adventofcode.com/ "Advent of Code")などの問題を解きながら学べるサイトやツールについて書かれています。

ものすごく前に[テストで学ぶJavaScriptについて](http://efcl.info/2012/0414/res3059/ "テストで学ぶJavaScriptについて | Web Scratch")というのを書いてましたが、実際に解きながら学ぶと結構色々発見があり面白いと思います。

この中だと[NodeSchool](http://nodeschool.io/ja/ "NodeSchool")の[workshopper](http://nodeschool.io/ja/#workshopper-list)は、ただのJavaScript文法だけではなく色々なライブラリやツールごとにあるので、見てみるとおもしろいかもしれません。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Grunt 1.0.0 released - Grunt: The JavaScript Task Runner
[gruntjs.com/blog/2016-04-04-grunt-1.0.0-released](http://gruntjs.com/blog/2016-04-04-grunt-1.0.0-released "Grunt 1.0.0 released - Grunt: The JavaScript Task Runner")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Grunt</span> <span class="jser-tag">ReleaseNote</span></p>

Grunt 1.0.0リリース。
Gruntプラグインの`peerDependencies`には`"grunt": ">=0.4.0"`を入れることを推奨してる。

----

## Release v1.0.0 - Rosebud · SBoudrias/Inquirer.js
[github.com/SBoudrias/Inquirer.js/releases/tag/v1.0.0](https://github.com/SBoudrias/Inquirer.js/releases/tag/v1.0.0 "Release v1.0.0 - Rosebud · SBoudrias/Inquirer.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">library</span></p>

ターミナルで選択肢などインタラクティブな動作を行うInquirer.js 1.0.0リリース。
PromiseベースのAPIへ変更

----

## normalize.css/CHANGELOG.md at 4.0.0 · necolas/normalize.css
[github.com/necolas/normalize.css/blob/4.0.0/CHANGELOG.md](https://github.com/necolas/normalize.css/blob/4.0.0/CHANGELOG.md "normalize.css/CHANGELOG.md at 4.0.0 · necolas/normalize.css")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

normalize.css 4.0.0リリース。

- [Normalize.scss v4 - Weblog - Hail2u.net](https://hail2u.net/blog/webdesign/modularized-normalize-scss-v4.0.0.html "Normalize.scss v4 - Weblog - Hail2u.net")

----

## AWS Lambda Supports Node.js 4.3
[aws.amazon.com/about-aws/whats-new/2016/04/aws-lambda-supports-node-js-4-3/](https://aws.amazon.com/about-aws/whats-new/2016/04/aws-lambda-supports-node-js-4-3/ "AWS Lambda Supports Node.js 4.3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

AWS LambdaでNode.js 4.3をサポート

----

## jsdom/Changelog.md at 8.3.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/8.3.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/8.3.0/Changelog.md "jsdom/Changelog.md at 8.3.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 8.3.0リリース。
Node Canvasを使った外部リソースを使った`img`の処理を追加(optional)。
`img.naturalWidth`などの実データに基づく値を取れるようになっています。

また、Page Visibility APIの基本的な実装を追加するなど

----

## React v15.0 | React
[facebook.github.io/react/blog/2016/04/07/react-v15.html](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v15.0リリース。
IE8のサポート終了、semverに準拠してアップデートするように変更。
0.14で非推奨なメッセージがでてなければ、そのままアップデートして動作する。

----
<h1 class="site-genre">アーティクル</h1>


----

## Tools to Learn JavaScript By Doing -Telerik Developer Network
[developer.telerik.com/featured/tools-learn-javascript/](http://developer.telerik.com/featured/tools-learn-javascript/ "Tools to Learn JavaScript By Doing -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">tutorial</span></p>

js-assessment、NodeSchool、Advent of CodeなどJavaScriptを学べるインタラクティブ性のあるツールについて

----

## Introducing the Microsoft Edge Platform Issue Tracker | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/04/06/edgehtml-issue-tracker/](https://blogs.windows.com/msedgedev/2016/04/06/edgehtml-issue-tracker/ "Introducing the Microsoft Edge Platform Issue Tracker | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">issue</span></p>

MS EdgeのIssue Trackerがアップデートされた。

- [azu/browser-javascript-resource: Browser JavaScript Resource.](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource: Browser JavaScript Resource.")

----

## WebdriverIOで始めるE2EテストとPageObject - Qiita
[qiita.com/derui@github/items/9ee72c7533c9a57aa8d2](http://qiita.com/derui@github/items/9ee72c7533c9a57aa8d2 "WebdriverIOで始めるE2EテストとPageObject - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span></p>

WebdriverIOを使ったE2EテストをPageObjectパターンで実装する話

----

## Reactコンポーネントをnpmパッケージとして開発する - Hatena Developer Blog
[developer.hatenastaff.com/entry/2016/04/09/180000](http://developer.hatenastaff.com/entry/2016/04/09/180000 "Reactコンポーネントをnpmパッケージとして開発する - Hatena Developer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Reactコンポーネントをnpmでライブラリとして公開する方法とメリット/デメリットについて。

----

## Streaming template literals - JakeArchibald.com
[jakearchibald.com/2016/streaming-template-literals/](https://jakearchibald.com/2016/streaming-template-literals/ "Streaming template literals - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

Template LiteralとWHATWG Streamをあわせる方法について

----

## Angular 2 — Unit Testing recipes — Google Developer Experts — Medium
[medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584](https://medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584 "Angular 2 — Unit Testing recipes — Google Developer Experts — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AnguarJS2でのテストパターン

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Introduction to flux-util // Speaker Deck
[speakerdeck.com/joere/introduction-to-flux-util](https://speakerdeck.com/joere/introduction-to-flux-util "Introduction to flux-util // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Facebookのflux utilについてのスライド。
flux utilの機能や担当する役割について

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## React.run - Beta
[www.react.run/](http://www.react.run/ "React.run - Beta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">webservice</span></p>

React Componentのコードを実行/共有できるJSFiddle的なサービス

----

## Microsoft Edge Developer Resources
[dev.windows.com/en-us/microsoft-edge/platform/data/](https://dev.windows.com/en-us/microsoft-edge/platform/data/ "Microsoft Edge Developer Resources")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">webservice</span> <span class="jser-tag">統計</span></p>

MSEdgeのウェブサイトでのCSSプロパティの使用率やブラウザのAPIサポート率などのデータ。

- [Chrome Platform Status](https://www.chromestatus.com/features "Chrome Platform Status")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jdonaghue/es-search: Search ECMAScript structurally
[github.com/jdonaghue/es-search](https://github.com/jdonaghue/es-search "jdonaghue/es-search: Search ECMAScript structurally")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AST</span> <span class="jser-tag">検索</span> <span class="jser-tag">JavaScript</span></p>

ASTベースでJavaScriptのコードから構造に一致する部分を検索するツール

----

## redfin/react-server: React server monorepo
[github.com/redfin/react-server](https://github.com/redfin/react-server "redfin/react-server: React server monorepo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サーバー</span></p>

Reactを使ったexpress middlewareなどのサーバ関連の実装

----

## mohayonao/web-audio-engine: Pure JS implementation of the Web Audio API
[github.com/mohayonao/web-audio-engine](https://github.com/mohayonao/web-audio-engine "mohayonao/web-audio-engine: Pure JS implementation of the Web Audio API")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web Audio APIのPure JavaScript実装。
PCM audioをNode Streamに吐くことができる

----

## kenwheeler/cash: An absurdly small jQuery alternative for modern browsers
[github.com/kenwheeler/cash](https://github.com/kenwheeler/cash "kenwheeler/cash: An absurdly small jQuery alternative for modern browsers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

jQuery Alternativeなライブラリ。
jQueryのDOM周りのメソッドを集めた感じ

----

## brigand/babel-plugin-flow-react-proptypes: A babel plugin to generate React PropTypes definitions from Flow type declarations.
[github.com/brigand/babel-plugin-flow-react-proptypes](https://github.com/brigand/babel-plugin-flow-react-proptypes "brigand/babel-plugin-flow-react-proptypes: A babel plugin to generate React PropTypes definitions from Flow type declarations.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">React</span></p>

FlowTypeでReactのpropTypesを書くと、JavaScriptのpropTypesに変換してくれるBabelプラグイン

----

## c58/marsdb: MarsDB is a Promise based lightweight database with MongoDB query syntax, written on ES6
[github.com/c58/marsdb](https://github.com/c58/marsdb "c58/marsdb: MarsDB is a Promise based lightweight database with MongoDB query syntax, written on ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

minimongoのようなクライアントサイド向けのデータベースライブラリ。
Adpterでバックエンドとなる保存方法を変更できるため、BrowserやElectron、Node.jsなどで動作する

----

## PlasmaPower/assert-request: Assert responses to HTTP requests in Node.JS
[github.com/PlasmaPower/assert-request](https://github.com/PlasmaPower/assert-request "PlasmaPower/assert-request: Assert responses to HTTP requests in Node.JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span></p>

Node.jsでrequestに対してresponseのassertを行うライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon.com: Isomorphic Application Development with JavaScrip eBook: Konstantin Tarkus: Kindle Store
[www.amazon.com/Isomorphic-Application-Development-JavaScrip-Konstantin-ebook/dp/B01DWFRFVG](http://www.amazon.com/Isomorphic-Application-Development-JavaScrip-Konstantin-ebook/dp/B01DWFRFVG "Amazon.com: Isomorphic Application Development with JavaScrip eBook: Konstantin Tarkus: Kindle Store")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017年2月4日発売
Isomorphic JavaScriptについての書籍

----
