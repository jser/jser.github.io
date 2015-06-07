---
title: "2014-11-10のJS: Less 2.0、Vue.js 0.11、Model-View-Intent"
author: azu
layout: post
date : 2014-11-10T20:46
category: JSer
tags:
    - Less
    - CSS
    - Vue.js
    - VirtualDOM

---

JSer.info #201 - CSSプリプロセッサである[Less 2.0](https://github.com/less/less.js/releases/tag/v2.0.0 "Release v2.0.0.0 · less/less.js")がリリースされました。

V2へのアップグレードについては[V2 Upgrade Guide](http://lesscss.org/usage/#v2-upgrade-guide "V2 Upgrade Guide")に詳しく書かれています。

----

[Vue.js 0.11](http://vuejs.org/2014/11/09/vue-011-release/ "Vue.js 0.11")がリリースされました。

- [Release 0.11.0: Cowboy Bebop · yyx990803/vue](https://github.com/yyx990803/vue/releases/tag/0.11.0 "Release 0.11.0: Cowboy Bebop · yyx990803/vue")

一から書きなおされているため、コードベースが結構変わっています。
APIの破壊的な変更や、追加されたオプション、機能については以下にまとめられています。

- [vue/changes.md at master · yyx990803/vue](https://github.com/yyx990803/vue/blob/master/changes.md "vue/changes.md at master · yyx990803/vue")

![vue](http://monosnap.com/image/nsEWKGQcP0aGgqMJ2eYAdH1RQi38X0.png)

以前のバージョンであるv0.10.6のドキュメントは[legacy.vuejs.org](http://legacy.vuejs.org/)に置かれています。

追記: 作者である[Evan You](https://github.com/yyx990803 "Evan You")さんはGoogleから[Meteor](https://www.meteor.com/ "Meteor")社の人になったそうです。

----

[Reactive MVC and the Virtual DOM — Futurice](http://futurice.com/blog/reactive-mvc-and-the-virtual-dom "Reactive MVC and the Virtual DOM — Futurice")という記事では、リアクティブなパターンについて書かれています。

以下のスライドの記事版という感じです。

- [Model-View-Intent and the Virtual DOM](http://staltz.com/mvi-freaklies/#/ "Model-View-Intent and the Virtual DOM")

React/Flux(要素的には別々ですが)はリアクティブプログラミングな所もありますが、インタラクティブな部分も混ざった感じになっているのを、よりリアクティブに実装するにはどうするかという感じの内容になっています。

既存のMVCとの役割の対比や、著者が提唱するModel-View-Intentはどういう構成なのか、またReact/Fluxを使った時との違いについて書かれています。

アーキテクチャ的には[Flux](https://github.com/facebook/flux "Flux")のように一方向のデータフローに近いところはあるので、Fluxに興味がある人も見てみると面白いと思います。

また、React/Fluxについては[Components, React and Flux (WIP) by Dan Abramov](http://slides.com/danabramov/components-react-flux-wip#/ "Components, React and Flux (WIP) by Dan Abramov")というスライドがよくまとまっているので一緒に見てみるといいかもしれません。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Ember.js - Ember.js 1.8.0 and 1.9 Beta Released
[emberjs.com/blog/2014/10/26/ember-1-8-0-released.html](http://emberjs.com/blog/2014/10/26/ember-1-8-0-released.html "Ember.js - Ember.js 1.8.0 and 1.9 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 1.8.0と1.9βリリース。

またEmber 2.0についても話し合われている

- [The Road to Ember 2.0 RFC by tomdale · Pull Request #15 · emberjs/rfcs](https://github.com/emberjs/rfcs/pull/15 "The Road to Ember 2.0 RFC by tomdale · Pull Request #15 · emberjs/rfcs")
- [Contribute to Ember.js 2.0. No coding required. :: madhatted.com](http://madhatted.com/2014/11/5/contribute-to-ember-js-2-0-no-coding-required "Contribute to Ember.js 2.0. No coding required. :: madhatted.com")

----

## Release v2.0.0.0 · less/less.js
[github.com/less/less.js/releases/tag/v2.0.0](https://github.com/less/less.js/releases/tag/v2.0.0 "Release v2.0.0.0 · less/less.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Less 2.0リリース

----

## Release 0.11.0: Cowboy Bebop · yyx990803/vue
[github.com/yyx990803/vue/releases/tag/0.11.0](https://github.com/yyx990803/vue/releases/tag/0.11.0 "Release 0.11.0: Cowboy Bebop · yyx990803/vue")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 0.11.0リリース。

一から書きなおされているため、挙動の変更やオプションの削除等破壊的な変更も多くあり、追加された機能やオプションも多い。

- [vue/changes.md at master · yyx990803/vue](https://github.com/yyx990803/vue/blob/master/changes.md "vue/changes.md at master · yyx990803/vue")
- [Vue.js v0.11の変更点(予定)まとめ - blog.koba04.com](http://blog.koba04.com/post/2014/10/07/vue-js-v011-changes/ "Vue.js v0.11の変更点(予定)まとめ - blog.koba04.com")

----

## Brackets Blog - The Free, Open Source Code Editor for the Web
[blog.brackets.io/2014/11/04/brackets-1-0-and-extract-for-brackets-preview-now-available/](http://blog.brackets.io/2014/11/04/brackets-1-0-and-extract-for-brackets-preview-now-available/ "Brackets Blog - The Free, Open Source Code Editor for the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">ReleaseNote</span></p>

Brackets 1.0リリース。

同時にExtract for BracketsというPSDファイルからテキストや色などの情報が取得出来るプラグインのα版が公開されている

- [Adobe、オープンソースのWeb開発向けテキストエディター「Brackets」v1.0をリリース - 窓の杜](http://www.forest.impress.co.jp/docs/news/20141105_674571.html "Adobe、オープンソースのWeb開発向けテキストエディター「Brackets」v1.0をリリース - 窓の杜")

----
<h1 class="site-genre">アーティクル</h1>

----

## Stream API がブラウザにやってくる - Block Rockin’ Codes
[jxck.hatenablog.com/entry/whatwg-stream](http://jxck.hatenablog.com/entry/whatwg-stream "Stream API がブラウザにやってくる - Block Rockin’ Codes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">stream</span> <span class="jser-tag">API</span> <span class="jser-tag">JavaScript</span></p>

WHATWGのStream APIについて。

連続したイベントを表現するStreamの流れ、ReadableとWritableの処理待ちのバランスが悪くなった時に調整するBack Pressureについても書かれている

- [Streams Standard](https://streams.spec.whatwg.org/ "Streams Standard")

----

## React.jsとBackbone.jsを組み合わせて実践してみた結果 - Qiita
[qiita.com/derui@github/items/864113f694b77eca685d](http://qiita.com/derui@github/items/864113f694b77eca685d "React.jsとBackbone.jsを組み合わせて実践してみた結果 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">backbone.js</span></p>

ReactとBackboneの組み合わせについて実践的な話が書かれている。

Viewの部分をReactにするアプローチ、Viewをテストする際に使えるTestUtilsやReactを導入する際の注意点など

----

## An easier way of using polyfills ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2014/11/an-easier-way-of-using-polyfills/](https://hacks.mozilla.org/2014/11/an-easier-way-of-using-polyfills/ "An easier way of using polyfills ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptの必要な機能のpolyfillをCDN的に使えるPolyfill.ioについて

----

## browserify をはじめてみる - Please Sleep
[please-sleep.cou929.nu/trying-browserify.html](http://please-sleep.cou929.nu/trying-browserify.html "browserify をはじめてみる - Please Sleep")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span></p>

埋め込み配布を目的としてJavaScriptをBrowserifyでビルドするにあたっての話。

bowerでインストールしたjQueryの依存関係の解決、browserify-shimを使ってCommonJSに対応してないライブラリを使う方法について

----

## AngularJS についての所感 ::ハブろぐ
[havelog.ayumusato.com/develop/javascript/e628-angularjs_thought.html](http://havelog.ayumusato.com/develop/javascript/e628-angularjs_thought.html "AngularJS についての所感 ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span></p>

AngularJSの扱い方を間違えるとハマってしまう所。

$scope、DIとProviderと依存の数、ルールの抑制とexpression、Controllerの肥大化。

他のライブラリに応用がしにくい世界観などについて

- [AngularJS: The Bad Parts | Lars Eidnes&#39; blog](http://larseidnes.com/2014/11/05/angularjs-the-bad-parts/ "AngularJS: The Bad Parts | Lars Eidnes&#39; blog")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Reactive MVC and the Virtual DOM — Futurice
[futurice.com/blog/reactive-mvc-and-the-virtual-dom](http://futurice.com/blog/reactive-mvc-and-the-virtual-dom "Reactive MVC and the Virtual DOM — Futurice")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">VirualDOM</span> <span class="jser-tag">デザインパターン</span> <span class="jser-tag">JavaScript</span></p>

MVIというReactiveなデザインパターンについて。

MV*と違いControllerを取り除き、代わりにIntentというユーザイベントを扱う仕組みを入れる。
一方通行にする点などFluxに似ている所はあるが、RxJS等を意識した話。
また、Virtual DOMを使い、テストしやすくするためにViewと実際の表示を作るRendererに分けている。

最後にReact/Fluxとどのような点が違うのかについて書かれている

- [Reactive MVC and the Virtual DOMのメモ | GH Issue Note](http://efcl.wordpress.com/2014/11/03/reactive-mvc-and-the-virtual-dom%e3%81%ae%e3%83%a1%e3%83%a2/ "Reactive MVC and the Virtual DOMのメモ | GH Issue Note")
- [Model-View-Intent and the Virtual DOM](http://staltz.com/mvi-freaklies/#/ "Model-View-Intent and the Virtual DOM")

----

## zertosh/ssr-demo-kit
[github.com/zertosh/ssr-demo-kit](https://github.com/zertosh/ssr-demo-kit "zertosh/ssr-demo-kit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">スライド</span> <span class="jser-tag">動画</span></p>

SoundCloudの人のReactによるサーバーサイドレンダリングのスライドと動画とサンプル

----

## Protractor for AngularJS: writing end-to-end tests has never been so fun
[ramonvictor.github.io/protractor/slides/](http://ramonvictor.github.io/protractor/slides/ "Protractor for AngularJS: writing end-to-end tests has never been so fun")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">protractor</span> <span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span> <span class="jser-tag">スライド</span></p>

Protractorについてよく書かれたスライド。

Protractorの仕組み、インストール方法、設定、API、Page Objectsを使ったテストのパターン、デバッグ方法等幅広くまとまってる

----

## Components, React and Flux (WIP) by Dan Abramov
[slides.com/danabramov/components-react-flux-wip#/](http://slides.com/danabramov/components-react-flux-wip#/ "Components, React and Flux (WIP) by Dan Abramov")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Flux</span> <span class="jser-tag">スライド</span> <span class="jser-tag">サンプル</span></p>

Reactに関する事が幅広く書かれているスライド。

jQuery、Backbone、Reactそれぞれで実装した場合について。
Reactの特徴である再利用性、コンポーネントのネスト、ステートフルやreact-router等について。

また開発ツールとしてhot-reload、一方向のデータフローを実現するFluxアーキテクチャについてもそれぞれの役割が詳しく書かれている。

- [gaearon/flux-react-router-example](https://github.com/gaearon/flux-react-router-example "gaearon/flux-react-router-example")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## ReactJS News
[reactjsnews.com/](http://reactjsnews.com/ "ReactJS News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

ReactのWeeklyニュースサイト

----

## Announcing RemoteIE: Test the latest IE on Windows, Mac OS X, iOS and Android - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/11/02/announcing-remoteie-test-the-latest-ie-on-windows-mac-os-x-ios-and-android.aspx](http://blogs.msdn.com/b/ie/archive/2014/11/02/announcing-remoteie-test-the-latest-ie-on-windows-mac-os-x-ios-and-android.aspx "Announcing RemoteIE: Test the latest IE on Windows, Mac OS X, iOS and Android - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">debug</span> <span class="jser-tag">MS</span></p>

確認用のIEをOS XやAndroid、iOS等でVPNで簡単に利用できるRemoteIEを公開した

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## uxebu/kommando
[github.com/uxebu/kommando](https://github.com/uxebu/kommando "uxebu/kommando")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

WebDriverを使ったE2Eテストを行うライブラリ。

wd.jsやleadfootなどのクライアントライブラリはオプションで指定できる。

----

## ibm-js/ecma402 · GitHub
[github.com/ibm-js/ecma402](https://github.com/ibm-js/ecma402 "ibm-js/ecma402 · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span> <span class="jser-tag">AMD</span></p>

ECMA-402 JavaScript  Internationalization APIのshimライブラリ

----

## substack/html-inline
[github.com/substack/html-inline](https://github.com/substack/html-inline "substack/html-inline")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">画像</span> <span class="jser-tag">Tools</span></p>

HTMLで読み込み指定されてるJavaScriptやCSS、画像をインライン化するコマンドラインツール

----

## rtfeldman/seamless-immutable
[github.com/rtfeldman/seamless-immutable](https://github.com/rtfeldman/seamless-immutable "rtfeldman/seamless-immutable")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ES5の機能を使ってImmutableな配列やオブジェクトを作成するライブラリ。

それぞれのオブジェクトは`Object.freeze`された状態になり、幾つか補助するメソッドが追加で用意されている

----

## travishorn/npm-package-store
[github.com/travishorn/npm-package-store](https://github.com/travishorn/npm-package-store "travishorn/npm-package-store")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

App Storeみたいにnpmモジュールの更新一覧を見られるツール

- [NPM Package Store](http://travishorn.com/npm-package-store/ "NPM Package Store")

----

## Paperclip.js - fast template engine for the DOM
[paperclipjs.com/](http://paperclipjs.com/ "Paperclip.js - fast template engine for the DOM")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">template</span> <span class="jser-tag">library</span></p>

JavaScriptテンプレートライブラリ。

データバインディングについての方向をテンプレート内に`<~>`演算子を使って指定する事ができるのが特徴的

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: WebRTC ブラウザベースのP2P技術: Alan B. Johnston, Daniel C. Burnett, 日本電信電話株式会社 内田直樹(監訳)
[www.amazon.co.jp/dp/4897979587?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4897979587?tag=amazon0abac-22 "Amazon: WebRTC ブラウザベースのP2P技術: Alan B. Johnston, Daniel C. Burnett, 日本電信電話株式会社 内田直樹(監訳)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">p2p</span> <span class="jser-tag">book</span></p>

2014年12月12日 発売

WebRTC: APIs and RTCWEB Protocols of the HTML5 Real-Time Webの翻訳本

----

## Amazon: デザイニングWebアクセシビリティ - アクセシブルな設計やコンテンツのための実践Q&amp;A: 太田良典, 伊原力也
[www.amazon.co.jp/dp/4862671756?tag=amazon0abac-22](http://www.amazon.co.jp/dp/4862671756?tag=amazon0abac-22 "Amazon: デザイニングWebアクセシビリティ - アクセシブルな設計やコンテンツのための実践Q&amp;A: 太田良典, 伊原力也")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">book</span></p>

2015年1月31日 発売

Webアクセシビリティについての書籍

----
