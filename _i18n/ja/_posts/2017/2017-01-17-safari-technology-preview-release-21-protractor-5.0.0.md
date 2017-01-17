---
title: "2017-01-17のJS: Safari Technology Preview Release 21、Protractor 5.0.0"
author: azu
layout: post
date : 2017-01-17T09:49
category: JSer
tags:
    - Safari
    - testing
    - E2E

---

JSer.info #314 - [Safari Technology Preview Release 21](https://webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/ "Safari Technology Preview Release 21")がリリースされました。

`<script type="module">`をサポートし、ECMAScript modulesが利用できるようになりました。
 ECMAScript modulesについては次の記事にSafariでの設定も書かれているので合わせて見てみると良いです。

- [Native ECMAScript modules - the first overview](https://blog.hospodarets.com/native-ecmascript-modules-the-first-overview "Native ECMAScript modules - the first overview")

----

E2Eテストフレームワークの[Protractor](http://www.protractortest.org/ "Protractor") [5.0.0](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "5.0.0")がリリースされました。

- [protractor/CHANGELOG.md at 5.0.0 · angular/protractor](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "protractor/CHANGELOG.md at 5.0.0 · angular/protractor")

[selenium-webdriver v3.x](https://github.com/SeleniumHQ/selenium/blob/master/javascript/node/selenium-webdriver/CHANGES.md#v300 "selenium-webdriver")にアップデートされたため、APIの変更などが含まれています。
また、動作に必要なNode.jsのバージョンが v6.9.x となっています。

----

## お知らせ

1月15日にJSer.info 6周年記念イベントを開催しました。
当日に発表されたスライドや議事録などは次のページにまとまっているので、よろしければ見てみてください。

- [JSer.info 6周年記念イベントを開催しました - JSer.info](https://jser.info/2017/01/15/jser-info-6years/ "JSer.info 6周年記念イベントを開催しました - JSer.info")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.4.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v1.4.0](https://github.com/karma-runner/karma/releases/tag/v1.4.0 "Release v1.4.0 · karma-runner/karma")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma v1.4.0リリース。
HTTP moduleを設定することで`node-http2`などを利用できるように、定数を`karma.constants`としてexportするようになるなど

----

## mobx/CHANGELOG.md at 3.0.0 · mobxjs/mobx
[github.com/mobxjs/mobx/blob/3.0.0/CHANGELOG.md](https://github.com/mobxjs/mobx/blob/3.0.0/CHANGELOG.md "mobx/CHANGELOG.md at 3.0.0 · mobxjs/mobx")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MobX 3リリース。
`observable`が各type毎にファクトリメソッドを追加、受け取ったオブジェクトをcloneするように、エラーハンドリングの改善など

- [MobX 3.0.0 の変更点について - console.lealog();](http://lealog.hateblo.jp/entry/2017/01/11/140607 "MobX 3.0.0 の変更点について - console.lealog();")
- [MobX 3 released: Unpeeling the onion – Medium](https://medium.com/@mweststrate/mobx-3-released-unpeeling-the-onion-ca877382f443 "MobX 3 released: Unpeeling the onion – Medium")

----

## Release Notes for Safari Technology Preview 21 | WebKit
[webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/](https://webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/ "Release Notes for Safari Technology Preview 21 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">webkit</span> <span class="jser-tag">safari</span></p>

Safari Technology Preview Release 21リリース。
Concurrent GCの有効化、`<script type="module">`の有効化、`global`のサポートされたがbreak the webのためbackoutなど

- [チェンジセット 210570 – WebKit](https://trac.webkit.org/changeset/210570 "チェンジセット 210570 – WebKit")
- [global breaks flickr.com · Issue #20 · tc39/proposal-global](https://github.com/tc39/proposal-global/issues/20 "global breaks flickr.com · Issue #20 · tc39/proposal-global")
- [Native ECMAScript modules - the first overview](https://blog.hospodarets.com/native-ecmascript-modules-the-first-overview "Native ECMAScript modules - the first overview")

----

## protractor/CHANGELOG.md at 5.0.0 · angular/protractor
[github.com/angular/protractor/blob/5.0.0/CHANGELOG.md](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "protractor/CHANGELOG.md at 5.0.0 · angular/protractor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

Protractor 5.0.0リリース。
`selenium-webdriver` 3.0.xへのアップデートに伴う破壊的変更、未知のフラグはエラーを投げるようになるなど

----
<h1 class="site-genre">アーティクル</h1>

----

## TypeScript: the missing introduction
[toddmotto.com/typescript-the-missing-introduction](https://toddmotto.com/typescript-the-missing-introduction "TypeScript: the missing introduction")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

TypeScriptという言語がどのような仕組みで動いているのか、JavaScriptに対してどのような役割をもっているのかという言語入門以前の話を丁寧にかかれている。

----

## Practical Redux · Mark&#x27;s Dev Blog
[blog.isquaredsoftware.com/series/practical-redux/](http://blog.isquaredsoftware.com/series/practical-redux/ "Practical Redux · Mark's Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

ゲームの管理ツールを題材にしたReduxについての連載。
`Redux-ORM`を使ったモデルの作成、Semantic-UIでのUI作成、ディレクトリ構造、デバッグ方法、コンポーネントのリファクタリングなどについて扱っている

----

## Side Effects in JS Promise chains – Medium
[medium.com/@gabrielcatalin/side-effects-in-js-promise-chains-7db50b6302f3](https://medium.com/@gabrielcatalin/side-effects-in-js-promise-chains-7db50b6302f3 "Side Effects in JS Promise chains – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promise chainに副作用がある処理を含める際に処理が途切れてしまう問題について。
`passThrough()`のような高階関数を用意し副作用を扱うことで、明示しつつバグを減らす方法について

----

## TypedArray or DataView: Understanding byte order ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/01/typedarray-or-dataview-understanding-byte-order/](https://hacks.mozilla.org/2017/01/typedarray-or-dataview-understanding-byte-order/ "TypedArray or DataView: Understanding byte order ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

`ArrayBuffer`、`TypedArray`、`DataView`についての解説。
`ArrayBuffer`がバイナリのデータ構造であり、*view*として`TypedArray`と`DataView`があるという話

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Components v1 - the next generation  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/01/webcomponents-org](https://developers.google.com/web/updates/2017/01/webcomponents-org "Web Components v1 - the next generation  |  Web  |  Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Web Components v1に伴い、
webcomponents.org がアップデートされた

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## arqex/freezer: A tree data structure that emits events on updates, even if the modification is triggered by one of the leaves, making it easier to think in a reactive way.
[github.com/arqex/freezer](https://github.com/arqex/freezer "arqex/freezer: A tree data structure that emits events on updates, even if the modification is triggered by one of the leaves, making it easier to think in a reactive way.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable.jsのようなImmutableなデータ構造を扱うライブラリ。
変更を通知するイベントやImmutable.jsよりもファイルサイズが小さい。

----

## Siema - Lightweight and simple carousel with no dependencies
[pawelgrzybek.com/siema/](https://pawelgrzybek.com/siema/ "Siema - Lightweight and simple carousel with no dependencies")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存がないカヌーセルライブラリ

----

## angus-c/just: A library of dependency-free utilities that do just do one thing.
[github.com/angus-c/just](https://github.com/angus-c/just "angus-c/just: A library of dependency-free utilities that do just do one thing.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存がない小さなユーティリティライブラリ集。
それぞれの機能を個別のモジュールとしてインストールして利用できる。
それぞれの`just-*`モジュール間でも依存関係がない作りとなっている。

- [Why I wrote Just. – Medium](https://medium.com/@angustweets/just-a12d54221f65 "Why I wrote Just. – Medium")
- [Just vs lodash · Issue #4 · angus-c/just](https://github.com/angus-c/just/issues/4 "Just vs lodash · Issue #4 · angus-c/just")

----

## yamafaktory/shrimpit: Shrimpit is a small CLI analysis tool for checking unused JavaScript, JSX &amp; Vue templates ES6 exports in your project.
[github.com/yamafaktory/shrimpit](https://github.com/yamafaktory/shrimpit "yamafaktory/shrimpit: Shrimpit is a small CLI analysis tool for checking unused JavaScript, JSX & Vue templates ES6 exports in your project.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

各モジュールのimport/exportを一覧し、未使用なモジュールを表示出来るCLI

----

## katat/vbot: JSON based visual regression testing tool, particularly useful for SPA or complicated web app
[github.com/katat/vbot](https://github.com/katat/vbot "katat/vbot: JSON based visual regression testing tool, particularly useful for SPA or complicated web app")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span></p>

JSONベースのリグレッションテストツール。
JSONでシナリオを作成して、スクリーンショットの画像比較ができる

- [vbot - JSON based visual regression tester - Kata Tech Life](http://katat.github.io/2017/01/09/vbot/ "vbot - JSON based visual regression tester - Kata Tech Life")

----

## Landmarks browser extension
[matatk.agrip.org.uk/landmarks/](http://matatk.agrip.org.uk/landmarks/ "Landmarks browser extension")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">Extension</span></p>

WAI-ARIAのlandmarkナビゲーションを有効化するブラウザ拡張

----

## tsayen/dom-to-image: Generates an image from a DOM node using HTML5 canvas
[github.com/tsayen/dom-to-image](https://github.com/tsayen/dom-to-image "tsayen/dom-to-image: Generates an image from a DOM node using HTML5 canvas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">canvas</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span></p>

SVGの`<foreignObject>`を使いHTMLを描画したものをCanvas経由で画像として取得するライブラリ

- [DOM オブジェクトを Canvas に描画する - HTML | MDN](https://developer.mozilla.org/ja/docs/Web/HTML/Canvas/Drawing_DOM_objects_into_a_canvas "DOM オブジェクトを Canvas に描画する - HTML | MDN")

----

## ModClean/modclean: Remove unwanted files and directories from your node_modules folder
[github.com/ModClean/modclean](https://github.com/ModClean/modclean "ModClean/modclean: Remove unwanted files and directories from your node\_modules folder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

node_modulesから不要なファイルを削除することができるツール

----
