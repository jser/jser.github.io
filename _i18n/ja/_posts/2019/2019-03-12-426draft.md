---
title: "2019-03-12のJS: TensorFlow.js 1.0、詳細Cache-Control、`JSON.stringify(-0)`"
author: "azu"
layout: post
date : 2019-03-12T00:20:50.340Z
category: JSer
tags:
- TensorFlow
- HTTP
- JSON

---

JSer.info #426 - TensorFlowのモデルをブラウザやNode.jsでも利用できるTensorFlow.js 1.0がリリースされました。

- [Release 1.0.0 · tensorflow/tfjs](https://github.com/tensorflow/tfjs/releases/tag/v1.0.0)

1.0では`Tensor.array()`と`Tensor.arraySync()`の追加、またAPIの細かなリネームといった破壊的な変更が含まれています。
また、リリースしたばかりの頃にくらべてパフォーマンスが改善されています。


----

[Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts](https://csswizardry.com/2019/03/cache-control-for-civilians/ "Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts")という記事では、`Cache-Control` HTTPヘッダについて詳しく解説されています。

`public`、`private`、`max-age`、`no-store`、`no-cache`、`immutable`、`stale-while-revalidate`といった各プロパティの動作やユースケースについての解説がされています。
またCache Bustingの手法などや`Clear-Site-Data`ヘッダ、ライブ配信向けのページの設定など幅広い内容を扱っています。

----

## 今週のIssue

ECMAScript仕様のIssueに`JSON.stringify(-0)`の処理についてのIssueが作られています。

- [Normative: Make `JSON.stringify(-0)` preserve the sign by mathiasbynens · Pull Request #1466 · tc39/ecma262](https://github.com/tc39/ecma262/pull/1466)

現在の仕様では`JSON.stringify(-0)`した場合の結果は`String(-0)`した場合と同じロジックであるため、`-`を無視した`"0"`という文字列になります。
一方で、`JSON.parse("-0")`は`-`を考慮するため`-0`という結果になります。

そのため、parseしてstringifyした結果が元の値とは`Object.is`で一致しないケースがあります。
この仕様は、JSONを発見した[douglascrockford/JSON-js](https://github.com/douglascrockford)に基づいたものです。

```js
// 今の仕様
Object.is(JSON.parse(JSON.stringify(-0)), -0); // => false
```

この仕様を修正して`JSON.stringify(-0)`が`"-0"`となるようなPRが出されました。

```js
// PRで出されていた仕様
Object.is(JSON.parse(JSON.stringify(-0)), -0); // => true
```

しかし、`===`での比較なら`-0`と`0`の違いは無視されることや`String()`の挙動と合わせている点など、
現実ではあまり問題となるケースがないという話もあり、一旦PRが取り下げられています。

```js
// 今の仕様
JSON.parse(JSON.stringify(-0)) === -0; // => true
```

興味がある人は仕様のIssueを読んでみると面白いかもしれません。
`===`と`Object.is`の比較については次のページがわかりすいと思います。

- [等価性の比較と同一性 - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Equality_comparisons_and_sameness)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 1.0.0 · tensorflow/tfjs
[github.com/tensorflow/tfjs/releases/tag/v1.0.0](https://github.com/tensorflow/tfjs/releases/tag/v1.0.0 "Release 1.0.0 · tensorflow/tfjs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

TensorFlow.js 1.0リリース。
パフォーマンスの改善、`Tensor.array()`と `Tensor.arraySync()`の追加など


----

## Release: npm@6.9.0 - 📣 announcements - npm forum
[npm.community/t/release-npm-6-9-0/5911](https://npm.community/t/release-npm-6-9-0/5911 "Release: npm@6.9.0 - 📣 announcements - npm forum")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.9.0リリース。
指定した日付より前のバージョンをインストールする`--before`オプションの追加、パッケージ名をaliasしてインストールするpackage aliasのサポートなど


----

## rmdm/rmgr: Release resources gracefully
[github.com/rmdm/rmgr](https://github.com/rmdm/rmgr "rmdm/rmgr: Release resources gracefully")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

リソースを管理するライブラリ。
リソースごとにinitializeとdispose時の処理を定義し、リソースの解放などを行うヘルパーライブラリ


----

## Marble.js 2.0 🔥 — reactive, better, functional, stronger
[medium.com/@jflakus/marble-2-reactive-better-functional-stronger-5924119d3098](https://medium.com/@jflakus/marble-2-reactive-better-functional-stronger-5924119d3098 "Marble.js 2.0 🔥 — reactive, better, functional, stronger")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

RxJSを使ったNode.js向けのHTTPフレームワークであるMarble.js 2.0リリース。 WebSocketsの対応、Contextを使ったDIの対応、io-tsを使ったバリデーションの対応など


----

## jsdom/Changelog.md at master · jsdom/jsdom
[github.com/jsdom/jsdom/blob/master/Changelog.md#1400](https://github.com/jsdom/jsdom/blob/master/Changelog.md#1400 "jsdom/Changelog.md at master · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JSDOM 14.0.0リリース。
`JSDOM.fragment()`がbrowsing contextを持たないframentsを作成するように変更、`element.blur()`のリグレッションの修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts
[csswizardry.com/2019/03/cache-control-for-civilians/](https://csswizardry.com/2019/03/cache-control-for-civilians/ "Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">article</span></p>

`Cache-Control` HTTPヘッダについての解説記事。
`public`、`private`、`max-age`、`no-store`、`no-cache`、`immutable`、`stale-while-revalidate`などそれぞれの項目の解説。
またCache Bustingの手法などについても書かれている


----

## JavaScript loose comparison (==) step by step
[felix-kling.de/js-loose-comparison/](https://felix-kling.de/js-loose-comparison/ "JavaScript loose comparison (==) step by step")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">spec</span></p>

`==`がどのように値を比較するかをECMAScript仕様に定義されているアルゴリズムのステップごとにチェックするツール。


----

## What's New In DevTools (Chrome 74)  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/03/devtools](https://developers.google.com/web/updates/2019/03/devtools "What's New In DevTools (Chrome 74)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 74の開発者ツールの変更点について。 CSS propertyの影響をハイライト、Lighthouse v4へアップデート、WebSocketのバイナリメッセージの表示対応。パフォーマンスパネルでLong taskを記録できるようになるなど。


----

## A Complete Guide to useEffect — Overreacted
[overreacted.io/a-complete-guide-to-useeffect/](https://overreacted.io/a-complete-guide-to-useeffect/ "A Complete Guide to useEffect — Overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Hooksの`useEffect`の動作や使い方、よくある質問について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Request Map Generator
[requestmap.webperf.tools/](http://requestmap.webperf.tools/ "Request Map Generator")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

指定したURLのリクエストの関係をマップ表示して可視化するツール。
WebPageTestの結果を利用している


----

## twbs/rfs: Automated responsive font sizes
[github.com/twbs/rfs](https://github.com/twbs/rfs "twbs/rfs: Automated responsive font sizes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">PostCSS</span></p>

レスポンシブなフォントサイズを指定するCSS。
Sass、PostCSS、less、stylus版が用意されている


----

## Feature policy
[featurepolicy.info/](https://featurepolicy.info/ "Feature policy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">example</span> <span class="jser-tag">document</span></p>

Feature Policyのデモサイト。 それぞれのポリシーのサポート状況やドキュメント、サンプルなどがまとめられている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## dyatko/arkit: Visualises JavaScript, TypeScript and Flow codebases as meaningful and committable architecture diagrams
[github.com/dyatko/arkit](https://github.com/dyatko/arkit "dyatko/arkit: Visualises JavaScript, TypeScript and Flow codebases as meaningful and committable architecture diagrams")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">SVG</span> <span class="jser-tag">UML</span></p>

アーキテクチャのダイアグラムをファイルから生成するツール。 コードベースのファイルを指定して、その構造をPlant UMLやSVGなどの図に変換してくれるツール


----

## Introduction · AnyProxy
[anyproxy.io/en/](http://anyproxy.io/en/ "Introduction · AnyProxy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proxy</span> <span class="jser-tag">Tools</span></p>

HTTPSやWebSocketなどに対応したローカルProxyツール。
Proxyしたログを閲覧するGUIもついている。


----

## jaames/iro.js: 🎨 Color wheel widget for JavaScript - with zero dependencies and a lovely SVG-based UI
[github.com/jaames/iro.js](https://github.com/jaames/iro.js "jaames/iro.js: 🎨 Color wheel widget for JavaScript - with zero dependencies and a lovely SVG-based UI")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">color</span> <span class="jser-tag">library</span></p>

依存がないカラーピッカーライブラリ。SVGをベースにしたカラーピッカーUIを作成するライブラリ


----

## vladocar/femtoJS: femtoJS - Really small JavaScript (ES6) library for DOM manipulation.
[github.com/vladocar/femtoJS](https://github.com/vladocar/femtoJS "vladocar/femtoJS: femtoJS - Really small JavaScript (ES6) library for DOM manipulation.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

一部のjQueryライクなDOM APIを提供するライブラリ。
ES2015+に対応したブラウザのみを対象にしている。

- [vladocar/nanoJS: Minimal standalone JS library for DOM manipulation](https://github.com/vladocar/nanoJS "vladocar/nanoJS: Minimal standalone JS library for DOM manipulation")

----
