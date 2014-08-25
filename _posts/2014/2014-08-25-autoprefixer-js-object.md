---
title: "2014-08-25のJS: Autoprefixer 3.0、JavaScriptのオブジェクト、Next Component"
author: azu
layout: post
date : 2014-08-25T22:09
category: 
tags:
    - CSS
    - JavaScript
    - パッケージ管理
    - Components

---

JSer.info #189 - CSSファイルに対してvendor prefixを付加できる[Autoprefixer 3.0](https://github.com/postcss/autoprefixer/releases/tag/3.0.0 "Autoprefixer 3.0")がリリースされました。

Sass等がプリプロセスと呼ばれるのに対して、プリプロセスされた後のCSSに対して処理をするので[PostCSS](https://github.com/postcss "PostCSS")とか言われるジャンルのツールです。
([ポストプロセスという用語が適切なのか](http://morishitter.hatenablog.com/entry/2014/07/09/024347 "CSSポストプロセッサーの必要性 - morishitter blog")という話もありますが)

[Autoprefixer 3.0](https://github.com/postcss/autoprefixer/releases/tag/3.0.0 "Autoprefixer 3.0")では、CoffeeScriptで書かれていたものがES6ベースに書きなおされました。またそれに伴ってコードから使う場合のAPIも変わっています。

----

[Advanced objects in JavaScript](http://bjorn.tipling.com/advanced-objects-in-javascript "Advanced objects in JavaScript") という記事ではJavaScriptのオブジェクトについて幅広く解説されています。

単純なprototypeから、getter/setter、また同じgetter/setterでもdefinePropertyを使った方法とPropertyDescriptorについて順を追ってサンプルコードと共に解説されていて読みやすいと思います。

そこからalternative `new`としてのObject.create、valueOfとtoStringについてまで触れられていて、最新のES6のProxyとSymbol(ここが本題っぽいですが)について書かれています。

幅広い内容なのでちょっと長いですがコード例も多いので読みやすいため、全体的に見て知らない部分を別途詳しく調べる等してみるといいかもしれません。

----

[Duo](http://duojs.org/ "Duo") という[component](https://github.com/component/component "component")の後継となるパッケージ管理ツールが公開されています。
([component/component](https://github.com/component/component "component/component")にもDuoが後継であることが明記されている)

まだ出たばかりであるため、動作の安定性、ドキュメント不足など評価するフェーズではない気がします。

新たに追加された機能として、Go言語のように`require('matthewmueller/uid');`と指定する事で直接GitHubリポジトリからパッケージを取得する機能等が追加されています。
(`component.json`によるcomponentはそのまま使えます。)

また、Duoとは違いこちらはComponentに対して後方互換性はありませんが、[normalize.io](https://normalize.github.io/ "normalize.io - an ES6 module, Web Component, and SPDY/HTTP2 Push frontend development worfklow")というパッケージ管理もβ公開されているのでコンセプトとして面白いので見てみるといいかもしれません。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 3.0 “Liberté, Égalité, Fraternité” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/3.0.0](https://github.com/postcss/autoprefixer/releases/tag/3.0.0 "Release 3.0 “Liberté, Égalité, Fraternité” · postcss/autoprefixer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Autoprefixer 3.0リリース。

`autoprefixer()`のAPIの変更、coreは分離、CoffeeからES6で書き直し、リポジトリがpostcssに移動した

----

## Node v0.10.31 (Stable)
[blog.nodejs.org/2014/08/19/node-v0-10-31-stable/](http://blog.nodejs.org/2014/08/19/node-v0-10-31-stable/ "Node v0.10.31 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.10.31 リリース。

----
<h1 class="site-genre">アーティクル</h1>

----

## Sass 3.4 is Out!
[www.sitepoint.com/sass-3-4-is-out/](http://www.sitepoint.com/sass-3-4-is-out/ "Sass 3.4 is Out!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span></p>

Sass3.4の更新内容について。

parent selector 、selector function、 `@error` ディレクティブなどについて

----

## Advanced objects in JavaScript
[bjorn.tipling.com/advanced-objects-in-javascript](http://bjorn.tipling.com/advanced-objects-in-javascript "Advanced objects in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

JSのオブジェクトについて幅広く解説されてる。

getter/setter、definePropertyとPropertyDescriptor、Object.create、valueOfとtoString、ES6のProxyとSymbolについて

- [Web Reflection: What Books Didn&#x27;t Tell You About ES5 Descriptors - Part 1](http://webreflection.blogspot.jp/2014/03/what-books-wont-tell-you-about-es5.html "Web Reflection: What Books Didn&#x27;t Tell You About ES5 Descriptors - Part 1")
- [ES5, Property Descriptor解説 - 枕を欹てて聴く](http://constellation.hatenablog.com/entry/20101205/1291564928 "ES5, Property Descriptor解説 - 枕を欹てて聴く")
- [Revisiting JavaScript Objects | LakTEK (Lakshan Perera)](http://www.laktek.com/2012/12/29/revisiting-javascript-objects/ "Revisiting JavaScript Objects | LakTEK (Lakshan Perera)")

----

## ストリーム表現とその変換 - ✘╹◡╹✘
[r7kamura.hatenablog.com/entry/2014/08/21/113654](http://r7kamura.hatenablog.com/entry/2014/08/21/113654 "ストリーム表現とその変換 - ✘╹◡╹✘")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

リアクティブプログラミングにおけるストリームの実装ライブラリと、ストリームについての解説。

ストリームの作成、ストリームを変換するmap、filter、scanについて

- [【翻訳】あなたが求めていたリアクティブプログラミング入門 - ninjinkun&#x27;s diary](http://ninjinkun.hatenablog.com/entry/introrxja "【翻訳】あなたが求めていたリアクティブプログラミング入門 - ninjinkun&#x27;s diary")

----

## WebStorm+Spy-jsの使い方 - Qiita
[qiita.com/laco0416/items/985044f0019ebef6cb2c](http://qiita.com/laco0416/items/985044f0019ebef6cb2c "WebStorm+Spy-jsの使い方 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">Tools</span></p>

WebStormから使えるspy-jsの機能や使い方について

- [WebStorm - Node.jsでもSpy-jsを使ってみる - Qiita](http://qiita.com/laco0416/items/6a45b08da45385dda746 "WebStorm - Node.jsでもSpy-jsを使ってみる - Qiita")

----

## WebRTC で動く Chord DHT の実装 webrtc-chord を公開しました - tsujio’s blog
[ntsujio.hatenablog.com/entry/2014/07/03/221023](http://ntsujio.hatenablog.com/entry/2014/07/03/221023 "WebRTC で動く Chord DHT の実装 webrtc-chord を公開しました - tsujio’s blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebRTC</span></p>

WebRTCを使った分散ハッシュテーブル (DHT: Distributed Hash Table) の実装

- [tsujio/webrtc-chord](https://github.com/tsujio/webrtc-chord "tsujio/webrtc-chord")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## bevacqua/js
[github.com/bevacqua/js/](https://github.com/bevacqua/js/ "bevacqua/js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

&quot;JavaScript Quality Guide&quot;

JavaScriptコーディングスタイルガイド。

----

## ECMAScript 6 support in Mozilla - JavaScript | MDN
[developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_6_support_in_Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_6_support_in_Mozilla "ECMAScript 6 support in Mozilla - JavaScript | MDN")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

FirefoxのES6サポート状況についてまとまってるページ

----

## 5 Minutes of JavaScript - The latest news in the JavaScript community
[five-js.envylabs.com/episodes/42-episode-41-august-21st-2014](http://five-js.envylabs.com/episodes/42-episode-41-august-21st-2014 "5 Minutes of JavaScript - The latest news in the JavaScript community")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">podcast</span> <span class="jser-tag">JavaScript</span></p>

週間JavaScriptなPodcast

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## slap-editor/slap
[github.com/slap-editor/slap](https://github.com/slap-editor/slap "slap-editor/slap")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">editor</span></p>

node.js製のターミナル上で動くテキストエディタ。

SublimeText的なファイルリスト、マウス対応、キーバインドの対応などデフォルトでもそのまま使えるような感じで面白い

----

## Duo
[duojs.org/](http://duojs.org/ "Duo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">GoLang</span> <span class="jser-tag">browserify</span></p>

Componentライクなパッケージ管理ツール。component.jsonでまとめられたコンポーネントからビルドしたjsやcssを生成出来る。またGo言語のようにrequireに直接GitHubのレポジトリを指定して使うことも出来る

- [the future of component? · Issue #594 · component/component](https://github.com/component/component/issues/594 "the future of component? · Issue #594 · component/component")
- [duo? · Issue #27 · normalize/discussions](https://github.com/normalize/discussions/issues/27 "duo? · Issue #27 · normalize/discussions")

----

## normalize.io - an ES6 module, Web Component, and SPDY/HTTP2 Push frontend development worfklow
[normalize.github.io/](https://normalize.github.io/ "normalize.io - an ES6 module, Web Component, and SPDY/HTTP2 Push frontend development worfklow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ES6 moudle/HTML Import/CSS importで書いてimportしたものをビルド出来るパッケージ管理ツール。

npm、URL、components等に対応してて、パッケージをURLで指定するという原則を持ってる

----

## Ment.io examples
[jeff-collins.github.io/ment.io/#/](http://jeff-collins.github.io/ment.io/#/ "Ment.io examples")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AngularJS</span></p>

Content Editableとかテキストエリアにおいて、GitHubのような@によるmentionの補完が出来るライブラリ

----

## styledown/styledown · GitHub
[github.com/styledown/styledown](https://github.com/styledown/styledown "styledown/styledown · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">document</span></p>

CSSスタイルガイド生成ツール。 

コメントにmarkdownで書いてスタイルガイドを生成する事が出来る。

----

## hail2u/node-csswring
[github.com/hail2u/node-csswring/](https://github.com/hail2u/node-csswring/ "hail2u/node-csswring")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSSから余分な記述を取り除いたり、書き換える事で圧縮するツール。

SourceMapに対応してる

- [CSSWring v1.1.0 - Weblog - Hail2u.net](http://hail2u.net/blog/webdesign/node-csswring-v1.1.0.html "CSSWring v1.1.0 - Weblog - Hail2u.net")

----

## soliton4/nodeMirror
[github.com/soliton4/nodeMirror](https://github.com/soliton4/nodeMirror "soliton4/nodeMirror")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">editor</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

node.js + CodeMirrorなブラウザで動くIDE。

ローカルサーバを立ち上げて、ブラウザで使う。hexエディタ、ターミナル、HTMLの表示などが出来る

----

## joyent/node-vstream
[github.com/joyent/node-vstream](https://github.com/joyent/node-vstream "joyent/node-vstream")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">stream</span> <span class="jser-tag">library</span></p>

node streamをラップして、データのダンプやチェック機能等を付けられるモジュール。

----

## browserify-loader 介绍 - 寸志 - SegmentFault
[blog.segmentfault.com/zhicun/1190000000640242](http://blog.segmentfault.com/zhicun/1190000000640242 "browserify-loader 介绍 - 寸志 - SegmentFault")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">AMD</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">library</span></p>

<a href='https://github.com/island205/browserify-loader'>https://github.com/island205/browserify-loader</a> についての紹介記事。

requrejsのように`main`属性で読み込むものを指定して使うローダーライブラリ

----