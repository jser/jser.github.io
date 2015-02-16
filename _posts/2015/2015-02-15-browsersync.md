---
title: "2015-02-16のJS: Babel(6to5)、BrowserSync 2.0"
author: azu
layout: post
date : 2015-02-15T22:46
category: JSer
tags:
    - Tools

---
JSer.info #215 - ES6+のコードをES5に変換するツールである [6to5](https://6to5.org/) が [Babel](https://babeljs.io/ "Babel · The transpiler for writing next generation JavaScript") にリネームされてリリースされました。

- [Not Born to Die · Babel](http://babeljs.io/blog/2015/02/15/not-born-to-die/ "Not Born to Die · Babel")

また、BabelはAcornをベースにしたパーサーを利用していて、そのASTの元になっている[SpiderMonkey parser](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API "SpiderMonkey parser")のASTはES6以降についての仕様が曖昧になっていてその部分を各パーサがそれぞれ実装していました。

最近になってjQuery FoundationにEsprimaが移管されたのが契機となって、Esprima、Acorn、Mozilla、Shift ASTの人たちが中心となってASTの仕様を定義していく[ESTree](https://github.com/estree/estree "ESTree")が始まりました。(基本的には現行のASTと互換性を重視しています)

Babelとしても[@sebmck](https://github.com/sebmck "sebmck")氏が[ESTree](https://github.com/estree/estree "ESTree")でのASTの策定に関わっていくようです。

-----

LiveReload的な機能を持っている開発用のローカルサーバを立ててくれる[BrowserSync 2.0](http://www.wearejh.com/news/browsersync-2-0/ "BrowserSync 2.0 - JH")がリリースされました。

元々多機能でしたが、[Pesticide](http://pesticide.io/ "Pesticide - Kill Your Css Layout Bugs")を使ったCSSアウトラインのデバッグ機能やレイテンシーのシミュレート等Remote debug機能が強化されています。

-----


-----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.11.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v1.11.0](https://github.com/jscs-dev/node-jscs/releases/tag/v1.11.0 "Release v1.11.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

jscs v1.11.0リリース。
既存のファイルの用意されてるプリセットでチェックして、自動で設定ファイルを作成出来る`--auto-configure`のオプションの追加、ルールの追加修正など。

----

## jQuery UI 1.11.3 | jQuery UI Blog
[blog.jqueryui.com/2015/02/jquery-ui-1-11-3/](http://blog.jqueryui.com/2015/02/jquery-ui-1-11-3/ "jQuery UI 1.11.3 | jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.11.3リリース。

----

## Changelog · lodash/lodash Wiki
[github.com/lodash/lodash/wiki/Changelog#v320](https://github.com/lodash/lodash/wiki/Changelog#v320 "Changelog · lodash/lodash Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

lodash v3.2.0リリース。
`_.fill`や`_.spread`等の追加、lazyサポートの修正や対応メソッドの追加

----

## BrowserSync 2.0 - JH
[www.wearejh.com/news/browsersync-2-0/](http://www.wearejh.com/news/browsersync-2-0/ "BrowserSync 2.0 - JH")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

LiveReloadなどが入った開発用サーバであるBrowserSync 2.0リリース。
デバッグのUI画面が追加され、履歴、接続してる端末一覧、CSSでデバッグ用にアウトライン表示などの機能が追加されている

----

## Download RequireJS
[requirejs.org/docs/download.html#2-1-16](http://requirejs.org/docs/download.html#2-1-16 "Download RequireJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AMD</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

RequireJS 2.1.16リリース。
依存関係のパースをするのにEsprima 2.0を使うように、r.jsがNashornをサポート、UMDサポートのアップデート

----

## Release Pure 0.6.0-rc-1 – New Pure Menus · yahoo/pure
[github.com/yahoo/pure/releases/tag/v0.6.0-rc-1](https://github.com/yahoo/pure/releases/tag/v0.6.0-rc-1 "Release Pure 0.6.0-rc-1 – New Pure Menus · yahoo/pure")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Pure 0.6.0-rc-1リリース。
Menusの書き直し、Normalizeのアップデート(IE 7以下はサポート廃止)など

----

## js2coffee/New_in_2.0.md at master · js2coffee/js2coffee
[github.com/js2coffee/js2coffee/blob/master/notes/New_in_2.0.md](https://github.com/js2coffee/js2coffee/blob/master/notes/New_in_2.0.md "js2coffee/New\_in\_2.0.md at master · js2coffee/js2coffee")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CoffeeScript</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptをCoffeeScriptに変換するJs2coffee 2.0リリース。
エディタや警告の表示、ASTの表示、SourceMap対応など

----

## harmony:specification_drafts [ES Wiki]
[wiki.ecmascript.org/doku.php?id=harmony:specification_drafts](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts "harmony:specification\_drafts \[ES Wiki\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2015 (ES6)  Draft Rev 33リリース。
`super()`に関する制約の記述の追加、module周りのリファクタリング

----
<h1 class="site-genre">アーティクル</h1>

----

## Not Born to Die · Babel
[babeljs.io/blog/2015/02/15/not-born-to-die](https://babeljs.io/blog/2015/02/15/not-born-to-die "Not Born to Die · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

6to5が"Babel"にリネームされた。
多くのツールがparsersとtranspilersに依存しているため、Babelプロジェクトではこの部分を解決していく。
ESTreeというASTの仕様の標準化作業にも協力していくとのこと

- [Project scope and future · Issue #568 · babel/babel](https://github.com/babel/babel/issues/568 "Project scope and future · Issue #568 · babel/babel")
- [estree/estree](https://github.com/estree/estree "estree/estree")
- [Name suggestions · Issue #596 · babel/babel](https://github.com/babel/babel/issues/596 "Name suggestions · Issue #596 · babel/babel")

----

## estree/estree · GitHub
[github.com/estree/estree](https://github.com/estree/estree "estree/estree · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span></p>

SpiderMonkey Parser APIのASTのドキュメントがGitHubに移行し、ES6についてのドキュメント化が開始された。
現行の多くのツールがこれに依存していて、明文化されてないASTについてを仕様に落とすのが目的。

----

## JSCS in use
[varya.me/en/posts/jscs-in-use/](http://varya.me/en/posts/jscs-in-use/ "JSCS in use")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのコードスタイルチェックツールであるJSCSの使い方について

- [JavaScript CodeStyle. Automatically!](http://varya.me/jscs-talk/ "JavaScript CodeStyle. Automatically!")
- [JSCS: JavaScript Code Style — Frontend Babel](http://frontendbabel.info/articles/jscs-javascript-code-style/ "JSCS: JavaScript Code Style — Frontend Babel")

----

## Extensible Web を支える低レベル API 群 - Block Rockin’ Codes
[jxck.hatenablog.com/entry/extensible-lowlevel-api](http://jxck.hatenablog.com/entry/extensible-lowlevel-api "Extensible Web を支える低レベル API 群 - Block Rockin’ Codes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

現在策定や実装が進んでいる低レベルなAPIとしてどのようなものがあるかについてのまとめ

- [Extensible web](http://www.slideshare.net/Jxck/extensible-web "Extensible web")

----

## Change Detection in Angular 2 | Victor Savkin
[victorsavkin.com/post/110170125256/change-detection-in-angular-2](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2 "Change Detection in Angular 2 | Victor Savkin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">アルゴリズム</span></p>

Angular 2の変更検知の仕組みについての解説。
基本的にはComponentツリーを上から走査して変更を検知するが、Reactの`shouldComponentUpdate()`のように子への探索を減らす仕組みが導入されている

- [リアルな DOM はなぜ遅いのか - steps to phantasien](http://steps.dodgson.org/b/2014/12/11/why-is-real-dom-slow/ "リアルな DOM はなぜ遅いのか - steps to phantasien")

----

## Year in review: Spidermonkey part 1 | H4writer
[h4writer.com/?p=14](http://h4writer.com/?p=14 "Year in review: Spidermonkey part 1 | H4writer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">歴史</span></p>

2014年のFirefoxに入ったAPI、機能や改善点等の振り返り

- [Year in review: Spidermonkey in 2014 part 2 | H4writer](http://h4writer.com/?p=40 "Year in review: Spidermonkey in 2014 part 2 | H4writer")

----

## TouchDevelop - TouchDevelop goes open-source
[www.touchdevelop.com/blog/touchdevelopgoesopensource](https://www.touchdevelop.com/blog/touchdevelopgoesopensource "TouchDevelop - TouchDevelop goes open-source")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">MS</span> <span class="jser-tag">オープンソース</span></p>

タッチ操作でアプリを開発出来るウェブアプリである TouchDevelopがオープンソースとして公開された。
TypeScriptで書かれている

- [TouchDevelop](https://github.com/Microsoft/TouchDevelop "TouchDevelop")

----

## A Guide To ES6 Classes - I Like Kill Nerds
[ilikekillnerds.com/2015/02/a-guide-to-es6-classes/](http://ilikekillnerds.com/2015/02/a-guide-to-es6-classes/ "A Guide To ES6 Classes - I Like Kill Nerds")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Classについて。
ES5ではどのように"クラス"を書いてたかと、ES6ではどのように書けるかについて。
継承や`surper()`についても触れている

----

## Flux solutions compared by example - Pixelhunter.me | Dmitri Voronianski&#x27;s blog
[pixelhunter.me/post/110248593059/flux-solutions-compared-by-example](http://pixelhunter.me/post/110248593059/flux-solutions-compared-by-example "Flux solutions compared by example - Pixelhunter.me | Dmitri Voronianski&#x27;s blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">サンプル</span> <span class="jser-tag">JavaScript</span></p>

Flux実装のライブラリは多種多様で、小さなサンプルをそれぞれのライブラリを使って分かった事について。
通信でデータ取得はどこですべきか、
Isomorphicとシングルトン、ComponentをラップしたContainerのレイヤーを設ける事についてなど

----

## 60fps on the mobile web — Flipboard Engineering
[engineering.flipboard.com/2015/02/mobile-web/](http://engineering.flipboard.com/2015/02/mobile-web/ "60fps on the mobile web — Flipboard Engineering")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">React</span> <span class="jser-tag">DOM</span></p>

React Canvas について。
Cavnas要素でUIを作ることで60FPSのスクロールを実現する。
宣言的にUIを作れるためDOM的な抽象レイヤーとしてReactを使い、内部的にCanvasでレンダリングするReact Canvasを開発した話

- [Flipboard/react-canvas](https://github.com/flipboard/react-canvas "Flipboard/react-canvas")
- [Flipboard – React Canvas Accessibility | The Paciello Group – Your Accessibility Partner (WCAG 2.0/508 audits, VPAT, usability and accessible user experience)](http://www.paciellogroup.com/blog/2015/02/flipboard-react-canvas-accessibility/ "Flipboard – React Canvas Accessibility | The Paciello Group – Your Accessibility Partner (WCAG 2.0/508 audits, VPAT, usability and accessible user experience)")

----

## maxogden/maintenance-modules
[github.com/maxogden/maintenance-modules](https://github.com/maxogden/maintenance-modules "maxogden/maintenance-modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

npmでモジュールを公開するのを補助する色々なツールの紹介。
TravisCIの設定、gh-pagesへのデプロイスクリプト、package.jsonの整形、npm release、依存パッケージのチェックなど

----

## Detect JavaScript Problems with ESLint
[davidwalsh.name/eslint](http://davidwalsh.name/eslint "Detect JavaScript Problems with ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLintを使ったJavaScriptのLintについて。
オプションの設定方法

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ES6 at PayPal
[www.slideshare.net/JamundFerguson/es6-at-paypal](http://www.slideshare.net/JamundFerguson/es6-at-paypal "ES6 at PayPal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

ES6を使ってみようという感じのスライド

----

## Asynchronous Programming: The End of The Loop - Video Tutorial Series @eggheadio
[egghead.io/series/mastering-asynchronous-programming-the-end-of-the-loop](https://egghead.io/series/mastering-asynchronous-programming-the-end-of-the-loop "Asynchronous Programming: The End of The Loop - Video Tutorial Series @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">動画</span></p>

NetflixのJafar HusainさんよるJavaScriptの非同期プログラミングについてのスクリーンキャスト。
聞きやすくて、分かりやすくて、書き起こしもある

----

## Tagtree course: Expert ES6
[tagtree.io/courses/expert-es6/](http://tagtree.io/courses/expert-es6/ "Tagtree course: Expert ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

ES6について学べる講座。
ES6の新しい機能についての解説と練習問題を解いて学べる

----

## nodefest 2014 - YouTube
[www.youtube.com/playlist?list=PL42hYWKFRfN689rx3pVReAkYjs2F05Kum](https://www.youtube.com/playlist?list=PL42hYWKFRfN689rx3pVReAkYjs2F05Kum "nodefest 2014 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

東京Node学園祭2014 http://nodefest.jp/2014/ の動画が公開された

----
<h1 class="site-genre">サイト、サービス</h1>

----

## npm/how-to-npm
[github.com/npm/how-to-npm](https://github.com/npm/how-to-npm "npm/how-to-npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">tutorial</span></p>

npmについてコマンドラインで学べるインタラクティブな教材

----

## css2scss - from css to scss
[sebastianpontow.de/css2compass](http://sebastianpontow.de/css2compass "css2scss - from css to scss")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Sass</span> <span class="jser-tag">webservice</span></p>

CSSからSCSSの機能を使ったもの変換したり、色見本を作ってくれるサービス。

- [汚いcssを整形するWebアプリ「css2scss」でリファクタリングした際、「ヤバい」と感じた３つの機能と３つの点 - Qiita](http://qiita.com/koh-taka@github/items/bf638dd64c7c09e93557 "汚いcssを整形するWebアプリ「css2scss」でリファクタリングした際、「ヤバい」と感じた３つの機能と３つの点 - Qiita")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## wooorm/eslint-md
[github.com/wooorm/eslint-md](https://github.com/wooorm/eslint-md "wooorm/eslint-md")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">Tools</span></p>

Markdownの中にあるCodeBlockのJavaScriptをESLintでチェックできるツール

----

## Phoenixmatrix/phoenixmatrix-proxy
[github.com/Phoenixmatrix/phoenixmatrix-proxy](https://github.com/Phoenixmatrix/phoenixmatrix-proxy "Phoenixmatrix/phoenixmatrix-proxy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node-webkit</span> <span class="jser-tag">proxy</span> <span class="jser-tag">app</span></p>

node-webkit(nw.js)で書かれたプロキシアプリ。
SSLにもCharlesみたいに証明書を使ってプロキシ出来る。Fiddlerとかみたいにスクリプタブルなデバッグプロキシとなるのが目的

----

## wix/react-templates
[github.com/wix/react-templates](https://github.com/wix/react-templates "wix/react-templates")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">template</span> <span class="jser-tag">library</span></p>

ReactのJSXへ変換できるテンプレートとコンパイラ。
JetBrains IDEで動くプラグインが用意されている
https://github.com/idok/react-templates-plugin

----

## Flipboard/react-canvas
[github.com/flipboard/react-canvas](https://github.com/flipboard/react-canvas "Flipboard/react-canvas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

CavasのレンダリングをするReact components。
基本的な要素、Events、Text sizing、css-layout(パフォーマンス優先なのでなくなるかも?)、Accessibilityへの配慮が予定されてる

- [60fps on the mobile web — Flipboard Engineering](http://engineering.flipboard.com/2015/02/mobile-web/ "60fps on the mobile web — Flipboard Engineering")

----

## Reapp - Hybrid apps, fast
[reapp.io/](http://reapp.io/ "Reapp - Hybrid apps, fast")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">mobile</span> <span class="jser-tag">library</span></p>

ReactベースのモバイルUIフレームワーク

----

## maxogden/wzrd
[github.com/maxogden/wzrd](https://github.com/maxogden/wzrd "maxogden/wzrd")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">debug</span> <span class="jser-tag">library</span></p>

beefyみたいなBrowserifyを使ったローカルサーバを立てるコマンドラインツール

----

## typicode/jsop
[github.com/typicode/jsop](https://github.com/typicode/jsop "typicode/jsop")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Object.observe を使って読み込んだJSONを書き換えたら自動的に保存するNodeモジュール

----

## acdlite/flummox
[github.com/acdlite/flummox](https://github.com/acdlite/flummox "acdlite/flummox")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Flux実装ライブラリ。
コアとなるFlummoxクラスをを継承して、そこにStoreとActionを登録することでシングルトンを避ける作りになっている。ES6 classやasync/awaitを使った書き方等が考慮されている。

----

## fdecampredon/jsx-typescript
[github.com/fdecampredon/jsx-typescript](https://github.com/fdecampredon/jsx-typescript "fdecampredon/jsx-typescript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span></p>

TypeScript + React(JSX)なTypeScript fork.

----
<h1 class="site-genre">書籍関係</h1>

----

## Exploring ES6: Upgrade to the next version of JavaScript
[exploringjs.com/](http://exploringjs.com/ "Exploring ES6: Upgrade to the next version of JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Speaking JavaScriptの著者でもあるDr. AxelによるES6についての書籍

- [First details of my upcoming book on ES6](http://www.2ality.com/2015/02/es6-book.html "First details of my upcoming book on ES6")

----
