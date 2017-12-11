---
title: "2017-12-11のJS: Parcel、webpack 4.0.0α、Node.js Performance改善ガイド"
author: "azu"
layout: post
date : 2017-12-11T00:06:46.000Z
category: JSer
tags:
- bundler
- webpack
- node.js
- performance

---

JSer.info #361 - [設定より規約](https://ja.wikipedia.org/wiki/%E8%A8%AD%E5%AE%9A%E3%82%88%E3%82%8A%E8%A6%8F%E7%B4%84 "設定より規約")([Convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration "Convention over configuration"))なbundlerである[Parcel](https://parceljs.org/ "Parcel")がリリースされました。

- [🚀 Announcing Parcel: A blazing fast, zero configuration web application bundler 📦](https://hackernoon.com/announcing-parcel-a-blazing-fast-zero-configuration-web-application-bundler-feac43aac0f1 "🚀 Announcing Parcel: A blazing fast, zero configuration web application bundler 📦")

[webpack](https://webpack.js.org/ "webpack")や[FuseBox](http://fuse-box.org/ "FuseBox")は詳細を設定ファイルで扱いますが、[Parcel](https://parceljs.org/ "Parcel")には現時点では設定ファイルがありません。
代わりにビルトインのプラグインと`pacakge.json`に書かれた`parcel-plugin-`から始まる名前のパッケージで[Plugins](https://parceljs.org/plugins.html#plugin-api "Plugins")を読み込むことで、対応するファイル([Assets](https://parceljs.org/assets.html "Assets"))などを拡張します。
（Assetの内部処理として、それぞれのAssetsに対応する設定ファイルを使う仕組み。たとえば[JSAsset](https://github.com/parcel-bundler/parcel/blob/cf6902a30a4acc49a5b4572be42781ebf3ed356a/src/assets/JSAsset.js "JSAsset")ならば内部的にBabelが利用され、`.babelrc`を読み込んで処理される)

JavaScriptだけではなくHTMLファイルをEntry pointとして扱うことができるため、典型的にはHTMLを起点にそこから読み込まれているAsset(CSSやJavaScriptなど)の依存を集めてビルドします。

```
$ parcel build src/index.html
# dist/ へAssets毎{js,css,htmlなど}のパッケージ結果が出力される
```

また、[FuseBoxのような](https://github.com/fuse-box/fuse-box/blob/93b5daca3fb1f91989983cf088b546a6f3672083/docs/internal-process.md)Asset単位のビルドキャッシュをしていて、デフォルトでは2度目のビルドからはキャッシュが利用されます。
一方、[公式サイトに掲載されているBenchmark](https://github.com/parcel-bundler/parcel/tree/cf6902a30a4acc49a5b4572be42781ebf3ed356a#benchmarks)の[詳細は明らかにされていない](https://github.com/parcel-bundler/parcel/issues/9)ため、キャッシュなしにおける優位性は不明です。
(parcelでは[source map support](https://github.com/parcel-bundler/parcel/issues/68 "source map support")がまだサポートされていないなど、同等の設定での計測かは明確にはなっていない。)

----

webpackの次のメジャーアップデートであるwebpack 4.0.0-alpha.0が公開されています。

- [webpack 4.0.0-alpha.0 feedback · Issue #6064 · webpack/webpack](https://github.com/webpack/webpack/issues/6064 "webpack 4.0.0-alpha.0 feedback · Issue #6064 · webpack/webpack")

BREAKING CHANGEとしてはNode.js 4のサポート終了、新しいプラグインシステムの追加と既存プラグインの変更などが中心です。既存のプラグインも基本的には互換性を持ちますが、一部プラグインではWorkaroundが必要になるようです。

- [The new plugin system (week 22–23) – webpack – Medium](https://medium.com/webpack/the-new-plugin-system-week-22-23-c24e3b22e95 "The new plugin system (week 22–23) – webpack – Medium")

新しく`--mode`オプション（"devevelop" or "production")の追加が行われています。
これは現在の`-d`や`-p`を整理して、webpackコア側の設定を"devevelop" or "production"にするものです。

- `-d` = `--mode development --devtool cheap-module-eval-source-map`
- `-p` = `--mode production --plugin uglifyjs-webpack-plugin`
- [Webpack 4: include UglifyJsPlugin under the production mode · Issue #6075 · webpack/webpack](https://github.com/webpack/webpack/issues/6075 "Webpack 4: include UglifyJsPlugin under the production mode · Issue #6075 · webpack/webpack")

また、module typeとしてesm(`.mjs`)とwebassembly(`.wasm`)をデフォルトで探すようになり、`sideEffects`設定のサポートなどが追加されています。

[Parcel](https://parceljs.org/ "Parcel")のリリースを受けて、webpackの今後のロードマップに投票できる[Vote](https://webpack.js.org/vote/ "Vote")にZero Config Modeが追加されています。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Alright <a href="https://twitter.com/hashtag/JavaScript?src=hash&amp;ref_src=twsrc%5Etfw">#JavaScript</a> <a href="https://twitter.com/hashtag/webpack?src=hash&amp;ref_src=twsrc%5Etfw">#webpack</a> folks, I&#39;ve created the voting item! <br><br>If you _really_ want a Zero Configuration (aka your configs live in .postcss, .babel, .everythingelse), we can do this. It seems like theres folks who want this.) Thanks <a href="https://twitter.com/parceljs?ref_src=twsrc%5Etfw">@parceljs</a> 4 ideas! <a href="https://t.co/y57ALM28fB">https://t.co/y57ALM28fB</a> <a href="https://t.co/m5RYhR4s3N">pic.twitter.com/m5RYhR4s3N</a></p>&mdash; Sean Thomas Larkin (@TheLarkInn) <a href="https://twitter.com/TheLarkInn/status/938928029044170752?ref_src=twsrc%5Etfw">December 8, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

----

[Node.js Performance 改善ガイド - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2017/12/05/125517 "Node.js Performance 改善ガイド - from scratch")という記事ではNode.jsアプリケーションのパフォーマンス改善方法について書かれています。

メモリ、CPU、ファイルI/O、ネットワークそれぞれにおける典型的なボトルネックの調べ方や改善方法について。
また、JavaScriptの最適化の問題や、クラスタやNative Addonなどの代替手法についてなどについてかかれています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release 1.9.0: JSX Fragments, EditorConfig and Arrow Parens · prettier/prettier
[github.com/prettier/prettier/releases/tag/1.9.0](https://github.com/prettier/prettier/releases/tag/1.9.0 "Release 1.9.0: JSX Fragments, EditorConfig and Arrow Parens · prettier/prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 1.9.0リリース。
JSXのFragment(`<></>`)ｗｐサポート、EditorConfigのサポート、Markdownのサポート改善。


----

## 📦 Parcel
[parceljs.org/](https://parceljs.org/ "📦 Parcel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

HTML,JS,CSSなどをまとめてbundleできるツール。
設定不要で使えること、高速にビルドできることが目的のツール。
ファイルタイプに対する処理をプラグインとして追加できる。

- [🚀 Announcing Parcel: A blazing fast, zero configuration web application bundler 📦](https://medium.com/@devongovett/announcing-parcel-a-blazing-fast-zero-configuration-web-application-bundler-feac43aac0f1 "🚀 Announcing Parcel: A blazing fast, zero configuration web application bundler 📦")

----

## GoogleChromeLabs/jsvu: JavaScript (engine) Version Updater
[github.com/GoogleChromeLabs/jsvu](https://github.com/GoogleChromeLabs/jsvu "GoogleChromeLabs/jsvu: JavaScript (engine) Version Updater")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

各種JavaScriptエンジンをダウンロード、インストールできるツール。
eshost-cliと組み合わせることでChakra、JavaScriptCore、SpiderMonkey、V8でのJavaScript実行結果を同時に得られる。

- [bterlson/eshost-cli: Run ECMAScript code uniformly across any ECMAScript host](https://github.com/bterlson/eshost-cli "bterlson/eshost-cli: Run ECMAScript code uniformly across any ECMAScript host")

----

## Release Notes for Safari Technology Preview 45 | WebKit
[webkit.org/blog/8039/release-notes-for-safari-technology-preview-45/](https://webkit.org/blog/8039/release-notes-for-safari-technology-preview-45/ "Release Notes for Safari Technology Preview 45 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 45リリース。
SVGフィルターの最適化、`display:contents`をデフォルトで有効化、`OffscreenCanvas.getContext("webgl")`を実装など


----

## mochify.js/CHANGES.md at v5.0.0 · mantoni/mochify.js
[github.com/mantoni/mochify.js/blob/v5.0.0/CHANGES.md](https://github.com/mantoni/mochify.js/blob/v5.0.0/CHANGES.md "mochify.js/CHANGES.md at v5.0.0 · mantoni/mochify.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Mochaを使ったテストをブラウザで動かすMchify 5.0.0リリース。
PhantomJSからHeadless Chromeに変更、`--url`オプションの追加など


----

## Angular 5.1 & More Now Available – Angular Blog
[blog.angular.io/angular-5-1-more-now-available-27d372f5eb4e](https://blog.angular.io/angular-5-1-more-now-available-27d372f5eb4e "Angular 5.1 & More Now Available – Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 5.1リリース。
CLIがService Workerオプション、App Shellオプションサポート、TypeScript 2.5サポートなど


----

## webpack 4.0.0-alpha.0 feedback · Issue #6064 · webpack/webpack
[github.com/webpack/webpack/issues/6064](https://github.com/webpack/webpack/issues/6064 "webpack 4.0.0-alpha.0 feedback · Issue #6064 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">issue</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 4.0.0-alpha.0リリース。
Node.js 4のサポート終了、`--mode`（dev/prod)の追加。
module typeとしてesm、webassemblyのサポート、`sideEffects`設定のサポート。
新しいプラグインシステムの追加と既存プラグインの変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Qiita の新記事ページのレイアウト実装 - Qiita
[qiita.com/morishitter/items/c4aa500929f2de441bfd](https://qiita.com/morishitter/items/c4aa500929f2de441bfd "Qiita の新記事ページのレイアウト実装 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Grid Layoutと`position: sticky`でのレイアウトについて


----

## PuppeteerでWebページからメインコンテンツっぽいところを抽出してみる - Qiita
[qiita.com/ukyo/items/287169de85576dfed608](https://qiita.com/ukyo/items/287169de85576dfed608 "PuppeteerでWebページからメインコンテンツっぽいところを抽出してみる - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">Chrome</span></p>

PuppeteerでスクレイピングしたDOM要素のスコアリングして、メインコンテンツを抽出する仕組みについて


----

## await vs return vs return await - JakeArchibald.com
[jakearchibald.com/2017/await-vs-return-vs-return-await/](https://jakearchibald.com/2017/await-vs-return-vs-return-await/ "await vs return vs return await - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

async functionの中で`await`と`return`、`return await`の違いについてを解説した記事


----

## New in Chrome 63  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/12/nic63](https://developers.google.com/web/updates/2017/12/nic63 "New in Chrome 63  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 63リリース。
Dynamic imports、Async iterator、`Promise#finally`、`Intl.PluralRules`、CSS `overscroll-behavior`プロパティのサポートなど


----

## Node.js Performance 改善ガイド - from scratch
[yosuke-furukawa.hatenablog.com/entry/2017/12/05/125517](http://yosuke-furukawa.hatenablog.com/entry/2017/12/05/125517 "Node.js Performance 改善ガイド - from scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Node.jsのパフォーマンスの調査や測定をする方法について。
メモリリーク、CPUの処理時間、ファイルI/O、ネットワークのボトルネック調査について。
またJavaScriptのdeoptが起きてないか、クラスタやNative Addonなどの代替手法についてなど


----

## Vanilla JSで学ぶRedux - Qiita
[qiita.com/ryota-murakami/items/2ed6b12943214ecfeeaf](https://qiita.com/ryota-murakami/items/2ed6b12943214ecfeeaf "Vanilla JSで学ぶRedux - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Reduxのコードを見ながらReduxの仕組みについて解説している記事。


----

## Prototype Tree · TryCatch
[zhirzh.github.io/2017/12/06/prototype-tree/](https://zhirzh.github.io/2017/12/06/prototype-tree/ "Prototype Tree · TryCatch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">図</span> <span class="jser-tag">article</span> <span class="jser-tag">d3.js</span></p>

JavaScriptオブジェクトのprototypeツリーをD3.jsを使って可視化する話

- [zhirzh/prototype-tree](https://github.com/zhirzh/prototype-tree "zhirzh/prototype-tree")

----

## 歴史的遺物callback interfaceの紹介 - Qiita
[qiita.com/yuki3/items/ab20985e70247c80d19c](https://qiita.com/yuki3/items/ab20985e70247c80d19c "歴史的遺物callback interfaceの紹介 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebPlatformAPI</span></p>

`addEventListener`のcallback interfaceと`requestAnimationFrame`などのcallback functionという仕様の違いついて。
イベントハンドラにおける`handleEvent`の動作について


----

## Using Headless Mode in Firefox – Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/ "Using Headless Mode in Firefox – Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">Selenium</span> <span class="jser-tag">article</span></p>

SeleniumをFirefoxのHeadlessモードで動かす方法、Debugging Protocolについてなど


----

## Fast Source Map Generation for React Native – David Aurelio – Medium
[medium.com/@david.aurelio/medium-fast-source-map-generation-for-react-native-ea5549007c18](https://medium.com/@david.aurelio/medium-fast-source-map-generation-for-react-native-ea5549007c18 "Fast Source Map Generation for React Native – David Aurelio – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">sourcemap</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

React Native(Metro)が利用するSource Mapの高速な実装について
https://github.com/facebook/metro/tree/master/packages/metro-source-map


----

## React Performance Fixes on Airbnb Listing Pages – Airbnb Engineering & Data Science – Medium
[medium.com/airbnb-engineering/recent-web-performance-fixes-on-airbnb-listing-pages-6cd8d93df6f4](https://medium.com/airbnb-engineering/recent-web-performance-fixes-on-airbnb-listing-pages-6cd8d93df6f4 "React Performance Fixes on Airbnb Listing Pages – Airbnb Engineering & Data Science – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Reactを使ったアプリケーションのパフォーマンスを測定し、それをどのように修正していったかについての記事。
`PureComponent`での無駄な描画を防止、スクロール時の処理、入力欄などについて


----

## Performance Calendar » Clearing cache in the browser
[calendar.perfplanet.com/2017/clearing-cache-in-the-browser/](https://calendar.perfplanet.com/2017/clearing-cache-in-the-browser/ "Performance Calendar » Clearing cache in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

ウェブアプリ側からブラウザのキャッシュをクリアするさまざまな手法のまとめ。
`location.reload(true)`、Vary、fetch、iframe、Clear-SIte-Dataなどの手法毎にブラウザの対応についてまとめている。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf Budapest 2017 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshH9ztZfHqvQhF1\_Zm4VcCTD](http://www.youtube.com/playlist?list=PL37ZVnwpeshH9ztZfHqvQhF1_Zm4VcCTD "JSConf Budapest 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

JSConf Budapest 2017の動画まとめ

- [JSConf Budapest 2017](http://jsconfbp.com/ "JSConf Budapest 2017")

----

## Eirik Vullum: JavaScript Metaprogramming - ES6 Proxy Use and Abuse | JSConf Budapest 2017 - YouTube
[www.youtube.com/watch?v&#x3D;\_5X2aB\_mNp4](https://www.youtube.com/watch?v=_5X2aB_mNp4 "Eirik Vullum: JavaScript Metaprogramming - ES6 Proxy Use and Abuse | JSConf Budapest 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

ES Proxyを活用したメタプログラミングについての発表動画

- [JSBP - JavaScript Metaprogramming with Proxies by Eirik Langholm Vullum](http://slides.com/eiriklv/javascript-metaprogramming-with-proxies-41#/ "JSBP - JavaScript Metaprogramming with Proxies by Eirik Langholm Vullum")

----

## MakeYouAReact - Google スライド
[docs.google.com/presentation/d/1qh5ZCMI2e45Z4YZBcI62NMDt-1H2Uwx0sZ3T8ScNStk/pub?start&#x3D;false&amp;loop&#x3D;false&amp;delayms&#x3D;60000#slide&#x3D;id.g18b78f925cfb8077\_17](https://docs.google.com/presentation/d/1qh5ZCMI2e45Z4YZBcI62NMDt-1H2Uwx0sZ3T8ScNStk/pub?start=false&loop=false&delayms=60000#slide=id.g18b78f925cfb8077_17 "MakeYouAReact - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span> <span class="jser-tag">DOM</span></p>

ReactのようなViewライブラリを自作するために必要な技術について解説してるスライド。
実際に実装を作りながら、DOMのdiff/patchなどについて解説している。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Three.js入門サイト - ICS MEDIA
[ics.media/tutorial-three/index.html](https://ics.media/tutorial-three/index.html "Three.js入門サイト - ICS MEDIA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">tutorial</span></p>

Three.jsについてのチュートリアルサイト。
Three.jsの使い方やWebGLについて


----

## i0natan/nodebestpractices: The largest Node.JS best practices list. Curated from the top ranked articles and always updated
[github.com/i0natan/nodebestpractices](https://github.com/i0natan/nodebestpractices "i0natan/nodebestpractices: The largest Node.JS best practices list. Curated from the top ranked articles and always updated")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">document</span></p>

Node.jsとexpressについてのプラクティスガイド。


----

## WasmFiddle
[wasdk.github.io/WasmFiddle/](https://wasdk.github.io/WasmFiddle/ "WasmFiddle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">editor</span> <span class="jser-tag">Tools</span></p>

WebAssemblyのjsfiddle的なサービス。
Wasmのコンパイルと実行、wast/wasmのダウンロードができる。


----

## jsdom/whatwg-mimetype: Parses, serializes, and manipulates MIME types, according to the WHATWG MIME Sniffing Standard
[github.com/jsdom/whatwg-mimetype](https://github.com/jsdom/whatwg-mimetype "jsdom/whatwg-mimetype: Parses, serializes, and manipulates MIME types, according to the WHATWG MIME Sniffing Standard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

MIME typesのパーサ、シリアライズライブラリ


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## deeplearn.js
[deeplearnjs.org/](https://deeplearnjs.org/ "deeplearn.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">機械学習</span> <span class="jser-tag">WebGL</span></p>

WebGLを使った機械学習向けのライブラリ。
同期的な(NumPyのような)計算実行と遅延的な(TensorFlowのような)計算実行をサポートしている。


----
