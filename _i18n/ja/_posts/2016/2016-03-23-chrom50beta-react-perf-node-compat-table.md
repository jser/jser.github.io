---
title: "2016-03-23のJS: Chrome 50β、Reactのパフォーマンス調査改善、Node.js compat table"
author: azu
layout: post
date : 2016-03-23T23:26
category: JSer
tags:
    - Chrome
    - React
    - perf
    - Node.js

---

JSer.info #271 - 

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing Marko v3: From HTML to HTML-JS | Marko
[markojs.com/blog/announcing-marko-v3/](http://markojs.com/blog/announcing-marko-v3/ "Announcing Marko v3: From HTML to HTML-JS | Marko")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">template</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

テンプレートエンジンのMarko v3リリース。
HTML-JS syntaxというJavaScriptのように書けるテンプレート表現のサポート、コンパイル時最適化の対応など

----

## Chromium Blog: Chrome 50 Beta: Push notification improvements and declarative preload
[blog.chromium.org/2016/03/chrome-50-beta-push-notification.html](http://blog.chromium.org/2016/03/chrome-50-beta-push-notification.html "Chromium Blog: Chrome 50 Beta: Push notification improvements and declarative preload")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 50 Betaリリース。
`<link rel='preload'>`、`HTMLCanvasElement.toBlob()`のサポート、iframeのsandbox属性値がサポートされているかを判定出来るように、`Document.defaultCharset`を削除など

- [DOMTokenList Validation Added in Chrome 50 | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/03/domtokenlist-validation-added-in-chrome-50?hl=en "DOMTokenList Validation Added in Chrome 50 | Web Updates - Google Developers")
- [Preload: What Is It Good For? – Smashing Magazine](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "Preload: What Is It Good For? – Smashing Magazine")

----

## protractor/CHANGELOG.md at 3.2.0 · angular/protractor
[github.com/angular/protractor/blob/3.2.0/CHANGELOG.md](https://github.com/angular/protractor/blob/3.2.0/CHANGELOG.md "protractor/CHANGELOG.md at 3.2.0 · angular/protractor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Protractor 3.2.0リリース。
TypeScriptサポートのための変更追加、任意のバージョンのWebDriverを指定できるようになるなど

- [Typescript support · Issue #1203 · angular/protractor](https://github.com/angular/protractor/issues/1203#issuecomment-168777170 "Typescript support · Issue #1203 · angular/protractor")

----

## Google Cloud Platform Blog: Node.js on Google App Engine goes beta
[cloudplatform.googleblog.com/2016/03/Node.js-on-Google-App-Engine-goes-beta.html](https://cloudplatform.googleblog.com/2016/03/Node.js-on-Google-App-Engine-goes-beta.html "Google Cloud Platform Blog: Node.js on Google App Engine goes beta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">google</span></p>

GAEでNode.jsがβサポートされた

----
<h1 class="site-genre">アーティクル</h1>

----

## Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/](https://hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/ "Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

Firefox 47の開発者ツールの新しい機能について。
どういう流れでオブジェクトが保持されているのかを可視化、コンソールへ複数行入力出来るように、Storage Insperatorでcacheをサポートなど

----

## Debugging with Node
[krasimirtsonev.com/blog/article/debugging-with-node](http://krasimirtsonev.com/blog/article/debugging-with-node "Debugging with Node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">tutorial</span></p>

Node.jsに元々入っている`node debug`コマンドの使い方について

----

## reBEM: React ♥ BEM — Medium
[medium.com/@mistadikay/rebem-react-bem-20d875157017](https://medium.com/@mistadikay/rebem-react-bem-20d875157017 "reBEM: React ♥ BEM — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">CSS</span></p>

ReactとBEMの組み合わせについて。
reBEM layersという考え方について

----

## An Introduction to jQuery&#x27;s Deferred Objects
[www.sitepoint.com/introduction-jquery-deferred-objects/](http://www.sitepoint.com/introduction-jquery-deferred-objects/ "An Introduction to jQuery's Deferred Objects")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span></p>

jQuery Deferredの歴史や使い方について
1.x、2.x、3.xそれぞれでの違いについて書かれている

----

## Animating with React, Redux, and d3 | A geek with a hat
[swizec.com/blog/animating-with-react-redux-and-d3/swizec/6775](http://swizec.com/blog/animating-with-react-redux-and-d3/swizec/6775 "Animating with React, Redux, and d3 | A geek with a hat")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">d3.js</span> <span class="jser-tag">SVG</span></p>

ReactとD3.jsを組み合わせてアニメーションするComponentを作る話。
Container ComponentにStateが出てくるためReduxで管理している。
パーティクルを表示するなかでどこにボトルネックがあるかについて

----

## Reactを使ったプロダクトのパフォーマンスを改善した話 | GMOメディア エンジニアブログ
[tech.gmo-media.jp/post/141458071484/react-perf-tuning](http://tech.gmo-media.jp/post/141458071484/react-perf-tuning "Reactを使ったプロダクトのパフォーマンスを改善した話 | GMOメディア エンジニアブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">debug</span></p>

React Componentで作成したアプリにのボトルネックの調査方法や改善手法について。
react-addons-perfを使ってプロファイルを見ながらやっていく話

----

## Redux Middleware in Depth - Qiita
[qiita.com/kuy/items/c6784fe443f1d5c7bbdc](http://qiita.com/kuy/items/c6784fe443f1d5c7bbdc "Redux Middleware in Depth - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span></p>

Reduxのmiddlewareについて。
middlewareの適応順や実行順により起きる問題や解決方法について詳しく書かれている。

----

## Why I Write Plain JavaScript Modules
[ponyfoo.com/articles/why-i-write-plain-javascript-modules](https://ponyfoo.com/articles/why-i-write-plain-javascript-modules "Why I Write Plain JavaScript Modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

なぜDOMのライブラリをReact/AngularJSなど特定のフレームワーク向けではなく、PureなDOMライブラリとして書くのかについて

----

## The State of Browser APIs - 1
[hwclass.in/2016/03/09/the-next-generation-of-browser-apis/](http://hwclass.in/2016/03/09/the-next-generation-of-browser-apis/ "The State of Browser APIs - 1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

現在ブラウザで使える色々な新しいAPIについての紹介

- [AurelioDeRosa/HTML5-API-demos: A repository where you can find information about many JavaScript and HTML5 APIs.](https://github.com/AurelioDeRosa/HTML5-API-demos "AurelioDeRosa/HTML5-API-demos: A repository where you can find information about many JavaScript and HTML5 APIs.")

----

## JavaScriptのPromiseオブジェクトについて調べた事 | QUARTETCOM TECH BLOG
[tech.quartetcom.co.jp/2016/03/22/javascript-promise/](http://tech.quartetcom.co.jp/2016/03/22/javascript-promise/ "JavaScriptのPromiseオブジェクトについて調べた事 | QUARTETCOM TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span></p>

Promiseについて簡潔にまとまった内容。
AngularJSの`$q`についても扱われてる

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Node.js ES2015/ES6 support
[node.green/](http://node.green/ "Node.js ES2015/ES6 support")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">まとめ</span></p>

Node.js版 ECMAScript compat-table

----

## Your first Progressive Web App
[codelabs.developers.google.com/codelabs/your-first-pwapp/](https://codelabs.developers.google.com/codelabs/your-first-pwapp/ "Your first Progressive Web App")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">tutorial</span></p>

Progressive Web Appについて学ぶワークショップ資料

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## gravmatt/force-js: The easy way to scroll and animate your page
[github.com/gravmatt/force-js](https://github.com/gravmatt/force-js "gravmatt/force-js: The easy way to scroll and animate your page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

要素をアニメーションする依存のないライブラリ

----

## danigb/tonal: Music tonal elements —pitches, chords, scales, keys— in Javascript
[github.com/danigb/tonal](https://github.com/danigb/tonal "danigb/tonal: Music tonal elements —pitches, chords, scales, keys— in Javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web MIDI、Web Audio APIを扱う小さなライブラリを集めたmono repo。

----

## GoogleChrome/proxy-polyfill: Proxy object polyfill
[github.com/GoogleChrome/proxy-polyfill](https://github.com/GoogleChrome/proxy-polyfill "GoogleChrome/proxy-polyfill: Proxy object polyfill")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

ES6 Proxyのpolyfillライブラリ。
get/set/apply/constructなど一部のtrapのみをサポートしている

----
