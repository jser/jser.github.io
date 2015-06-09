---
title: "2015-04-06のJS: Babel 5.0.0と次期ECMAScript、Bower 1.4.0、JSCSと自動整形"
author: azu
layout: post
date : 2015-04-06T22:53
category: 
tags:
    - JavaScript
    - ECMAScript
    - Bower
    - tool

---

JSer.info #222 - ES6+のコードをES5相当に変換するツールである[Babel](http://babeljs.io/ "Babel")の5.0.0がリリースされました。
変更内容について詳しくは以下を見るといいと思います。

- [5.0.0 Released · Babel](http://babeljs.io/blog/2015/03/31/5.0.0/ "5.0.0 Released · Babel")
- [babel/CHANGELOG.md at master · babel/babel](https://github.com/babel/babel/blob/master/CHANGELOG.md#500 "babel/CHANGELOG.md at master · babel/babel")

大きな変更点としてはブログ記事にも書かれていますが、今までES7以降の機能は`experimental`オプションで有効化して使えるようになっていました。
5.0.0からは`experimental`オプションを削除して、代わりにTC39 Processに沿った`--stage 0`というようにstage別のオプションを指定して使うようになります。

ECMAScriptを策定するプロセスであるTC39 Processでは、Stage 0からStage 4の5段階に分かれていて、Stage 4は次期仕様に含まれるという感じになっています。

Stage 2 - Draftぐらいになると、大きな反論がなければ次の仕様に入るというレベルなので、BabelではStage 2の仕様の実装がデフォルトで有効化されています。(またStage 3 - Candidateでは仕様のドラフトに対するフィードバックをどんどん行う段階なので、Babelを使うことでフィードバックがしやすくなると思います)

[明日には使えなくなるES7トーク](http://azu.github.io/slide/es6talks/ "明日には使えなくなるES7トーク")のスライドで簡単に紹介してるので、こちらも見てみるといいかもしれません。

つまり、これはどういう事かというと今まで次期ECMAScriptに入るかもしれないという実験的という意味で仕様と若干の距離がありました。
しかし、今後は次期ECMAScriptのどのStageの仕様の実装という事が明確になって、ユーザーはBabelを使って挙動をイメージしやすくなるので、仕様に対してもフィードバックしやすくなって仕様と実装の距離が近くなると思います。

[世界のJavaScriptを読もう @ 2014](http://azu.github.io/slide/jser200/javascript-2014.html "世界のJavaScriptを読もう @ 2014")でも書いていましたが仕様策定者は仕様へのフィードバックを求めているけど、仕様のリリース速度が早くなったり幅広くなることで、ユーザーはそれに気づかないでフィードバックする機会を失う問題というのが起こりやすくなっていると思います。

Babelがその隙間を少しでも埋めることを期待する変更だと思います。

他の変更点としては[babelrc](http://babeljs.io/docs/usage/babelrc/ "babelrc")というドキュメント化されていなかった設定ファイルのドキュメントを追加、[Plugins](http://babeljs.io/docs/usage/plugins/ "Plugins · Babel")のサポート、ES6 Classesで`constructor()`時に`super()`を呼んでいない場合にエラーとするように変更されています。

- [Classes in ECMAScript 6](http://www.2ality.com/2015/02/es6-classes-final.html) 

----

パッケージ管理ツールである[Bower](http://bower.io/ "Bower") [v1.4.0](https://github.com/bower/bower/releases/tag/v1.4.0 "Release v1.4.0 · bower/bower")がリリースされました。
何故か今まで出来なかった`login`と`unregister`コマンドがサポートされました。

またpacakge.jsonにBowerの設定を書けるように、`--save-exact`のサポート等がされています。

- [Release v1.4.0 · bower/bower](https://github.com/bower/bower/releases/tag/v1.4.0 "Release v1.4.0 · bower/bower")

-----
JavaScriptコードスタイルチェックツールである[JSCS v1.12.0](https://github.com/jscs-dev/node-jscs/releases/tag/v1.12.0 "Release v1.12.0 · jscs-dev/node-jscs")がリリースされました。

このバージョンでは一部自動整形機能がサポートされて、`-x`オプションを付けることで既存のコードに対してルールを用いた整形を行う事が出来ます。
(現時点ではスペースや改行などのみで、構造的な変更が必要な整形はされない)

```
jscs -x
```

JSCSでは`jscs --auto-configure path`とすることで、既存のコードからそれに近いコードスタイルセットを選んだり、インタラクティブに個別のルールを設定できたりするので、途中からでも導入しやすいような作りになってきています。

- [JSCS - Overview](http://jscs.info/overview.html "JSCS - Overview")

[実際にJSCSを導入](https://github.com/azu/textlint/commit/d261a7c648c31d888d3fa6e71b89b1fee07bb342)してみましたが、`--auto-configure`でコードスタイルセットを作成して、`-x`でスペース等が自動で整えられて、構造的な部分もWebStormのQuickFixで自動的に書き換え出来るようなものだったので意外と導入はすんなりできた感じがします。

gofmtのようにリポジトリに設定が入っていれば細かいコードスタイルはツールが自動で揃えてくれるようになると便利になりそうな感じはしました。(現時点ではそこまでパワフルではないですが)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing TypeScript 1.5 Alpha - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/03/27/announcing-typescript-1-5-alpha.aspx](http://blogs.msdn.com/b/typescript/archive/2015/03/27/announcing-typescript-1-5-alpha.aspx "Announcing TypeScript 1.5 Alpha - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.5αリリース。
ES6 modulesなどの対応、デコレータのサポート、Sublime Textプラグインの追加など

----

## Firefox — Notes (37.0) — Mozilla
[www.mozilla.org/en-US/firefox/37.0/releasenotes/](https://www.mozilla.org/en-US/firefox/37.0/releasenotes/ "Firefox — Notes (37.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 37リリース。
Typed ArrayにもArrayメソッドの追加、Web Audio APIを最新の仕様に追従、Web Worker内でIndexedDBを使えるようになる等

- [Firefox 37 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/37 "Firefox 37 for developers - Mozilla | MDN")
- [Firefox 37 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/37/Site_Compatibility "Firefox 37 サイト互換性情報 - Mozilla | MDN")

----

## Release v2.0.0 · eslint/espree
[github.com/eslint/espree/releases/tag/v2.0.0](https://github.com/eslint/espree/releases/tag/v2.0.0 "Release v2.0.0 · eslint/espree")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">ReleaseNote</span></p>

ESLintが使うASTパーサであるespree 2.0.0リリース。
ESTree仕様への追従のためにBreaking Change、`super`の対応、RestElementへの対応など

----

## less.js/CHANGELOG.md at v2.5.0 · less/less.js
[github.com/less/less.js/blob/v2.5.0/CHANGELOG.md](https://github.com/less/less.js/blob/v2.5.0/CHANGELOG.md "less.js/CHANGELOG.md at v2.5.0 · less/less.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

less.js 2.5.0リリース。
スコープ内でも`@plugin`が動作するように、パーサのパフォーマンス改善や細かい警告の修正など

- [Fix `@plugin` scoping rules by rjgotten · Pull Request #2522 · less/less.js](https://github.com/less/less.js/pull/2522 "Fix `@plugin` scoping rules by rjgotten · Pull Request #2522 · less/less.js")

----

## 5.0.0 Released · Babel
[babeljs.io/blog/2015/03/31/5.0.0](https://babeljs.io/blog/2015/03/31/5.0.0 "5.0.0 Released · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 5.0.0リリース。
`--experimental`を廃止して、ECMAScriptを策定してるTC39のプロセスを元にしたStageベースのフラグを導入。またES7のDecoratorsなどの実装を追加、class継承でのsuper()の呼び出しチェックを追加するなど

----

## flow/Changelog at v0.8.0 · facebook/flow
[github.com/facebook/flow/blob/v0.8.0/Changelog](https://github.com/facebook/flow/blob/v0.8.0/Changelog "flow/Changelog at v0.8.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.8.0リリース。

----

## Release v1.4.0 · bower/bower
[github.com/bower/bower/releases/tag/v1.4.0](https://github.com/bower/bower/releases/tag/v1.4.0 "Release v1.4.0 · bower/bower")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">package</span> <span class="jser-tag">ReleaseNote</span></p>

Bower 1.4.0リリース。
loginとunregisterコマンドをサポート、pacakge.jsonにBowerの設定を書けるように、`--save-exact`のサポートなど

- [Unregister and login commands (rebased) by sheerun · Pull Request #1719 · bower/bower](https://github.com/bower/bower/pull/1719 "Unregister and login commands (rebased) by sheerun · Pull Request #1719 · bower/bower")
- [Accept npm&#x27;s config variables in package.json · Issue #1711 · bower/bower](https://github.com/bower/bower/issues/1711 "Accept npm&#x27;s config variables in package.json · Issue #1711 · bower/bower")

----

## Release v1.12.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v1.12.0](https://github.com/jscs-dev/node-jscs/releases/tag/v1.12.0 "Release v1.12.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS 1.12.0リリース。
自動整形機能のサポート(`-x`オプション)、ルールの追加、Auto-configurationのエラー表示の改善など

----

## Node v0.12.2 (Stable)
[blog.nodejs.org/2015/03/31/node-v0-12-2-stable/](http://blog.nodejs.org/2015/03/31/node-v0-12-2-stable/ "Node v0.12.2 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.2リリース。

----

## harmony:specification_drafts [ES Wiki]
[`wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_3_2015_rev_37_release_candidate_4`](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_3_2015_rev_37_release_candidate_4)

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2015(ES6) RC4リリース。
TC39で承認されたバージョン、"Edition 6"という記述を"ECMAScript 2015"に置換するなど

- [Allen Wirfs-Brock on Twitter: &quot;@rwaldron @SlexAxton RC4 replaced a lot of &quot;Edition 6&quot; with &quot;ECMAScript 2015&quot;. Will help with ISO version aka ISO/IEC-16262 Edition 4&quot;](https://twitter.com/awbjs/status/584093254045413376 "Allen Wirfs-Brock on Twitter: &quot;@rwaldron @SlexAxton RC4 replaced a lot of &quot;Edition 6&quot; with &quot;ECMAScript 2015&quot;. Will help with ISO version aka ISO/IEC-16262 Edition 4&quot;")
- [Allen Wirfs-Brock on Twitter: &quot;The final ES6 draft will be RC4 which I will finalize and forward to Ecma next week.&quot;](https://twitter.com/awbjs/status/580326814826020864 "Allen Wirfs-Brock on Twitter: &quot;The final ES6 draft will be RC4 which I will finalize and forward to Ecma next week.&quot;")

----

## WebStorm 10 released: improved JavaScript support, TypeScript 1.4, V8 profiling, and more | JetBrains WebStorm Blog
[blog.jetbrains.com/webstorm/2015/03/webstorm-10-released/](http://blog.jetbrains.com/webstorm/2015/03/webstorm-10-released/ "WebStorm 10 released: improved JavaScript support, TypeScript 1.4, V8 profiling, and more | JetBrains WebStorm Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">ReleaseNote</span></p>

WebStorm 10リリース。
ES6のサポート改善、TypeScript 1.4のサポート、spy-jsで依存関係の表示、多段SourceMapに対応、V8のプロファイリングのサポートなど

- [What&#x27;s new in WebStorm 10](https://www.jetbrains.com/webstorm/whatsnew/ "What&#x27;s new in WebStorm 10")

----
<h1 class="site-genre">アーティクル</h1>

----

## Live Editing JavaScript with Webpack (Part III)
[jlongster.com/Backend-Apps-with-Webpack--Part-III](http://jlongster.com/Backend-Apps-with-Webpack--Part-III "Live Editing JavaScript with Webpack (Part III)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

webpackのhot module replacementの仕組みについての解説。
リロードなしでモジュールの変更をする仕組みについて

- [hot module replacement with webpack](http://webpack.github.io/docs/hot-module-replacement-with-webpack.html "hot module replacement with webpack")

----

## Auto-formatting JavaScript Code Style — Medium
[medium.com/@addyosmani/auto-formatting-javascript-code-style-fe0f98a923b8](https://medium.com/@addyosmani/auto-formatting-javascript-code-style-fe0f98a923b8 "Auto-formatting JavaScript Code Style — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JSCS 1.12.0で自動整形機能が入り、JSCSを使ってSublime Textで自動整形を行う方法について。

- [Release v1.12.0 · jscs-dev/node-jscs](https://github.com/jscs-dev/node-jscs/releases/tag/v1.12.0 "Release v1.12.0 · jscs-dev/node-jscs")

----

## CSS Font LoadingとFont Face Observer、Web Font Loader - Weblog - Hail2u.net
[hail2u.net/blog/webdesign/css-font-loading-font-face-observer-and-web-font-loader.html](http://hail2u.net/blog/webdesign/css-font-loading-font-face-observer-and-web-font-loader.html "CSS Font LoadingとFont Face Observer、Web Font Loader - Weblog - Hail2u.net")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

CSS Font Loadingと同様の機能を提供するshim的なライブラリの比較

----

## Jam3/jam3-lesson-module-basics
[github.com/Jam3/jam3-lesson-module-basics](https://github.com/Jam3/jam3-lesson-module-basics "Jam3/jam3-lesson-module-basics")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

小さいnpmのモジュールを使ってクライアントサイドの開発をしようという紹介記事。
実際にBrowserifyなどを使ってどうやって開発するかについて紹介している

----

## the-offline-cookbook-ja/ja.md at master · kuu/the-offline-cookbook-ja
[github.com/kuu/the-offline-cookbook-ja/blob/master/ja.md](https://github.com/kuu/the-offline-cookbook-ja/blob/master/ja.md "the-offline-cookbook-ja/ja.md at master · kuu/the-offline-cookbook-ja")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">翻訳</span> <span class="jser-tag">JavaScript</span></p>

The offline cookbookの翻訳。
Service Workerのパターンについて書かれている

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Service Workerハッカソン資料まとめ - dackdive&#x27;s blog
[dackdive.hateblo.jp/entry/2015/04/04/163234](http://dackdive.hateblo.jp/entry/2015/04/04/163234 "Service Workerハッカソン資料まとめ - dackdive&#x27;s blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">スライド</span> <span class="jser-tag">動画</span> <span class="jser-tag">まとめ</span></p>

Service Workerハッカソンのスライドや動画のまとめ

----
<h1 class="site-genre">サイト、サービス</h1>

----

## SemVer checker
[semver.npmjs.com/](http://semver.npmjs.com/ "SemVer checker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

npmのsemver計算機
バージョン文字列からどのバージョンにマッチするかを確認できる

----

## ECMAScript 6: Feature Overview and Comparison
[es6-features.org/](http://es6-features.org/ "ECMAScript 6: Feature Overview and Comparison")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

ES6とES5の書き方を項目毎に比較紹介してるサイト

----

## sorting algorithms in javascript
[h3manth.com/javascript-sorting/](http://h3manth.com/javascript-sorting/ "sorting algorithms in javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">アルゴリズム</span></p>

JavaScriptでソートアルゴリズムの実装

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## azu/wait-for-element.js
[github.com/azu/wait-for-element.js](https://github.com/azu/wait-for-element.js "azu/wait-for-element.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">DOM</span></p>

CSSセレクタにマッチする要素が表示されるまで待つライブラリ。
MutationObserverを使った実装とsetTimeoutを使った実装を持ってる

- [ある要素が表示されるまで待つJSライブラリを書いた(MutationObserver) | Web Scratch](http://efcl.info/2015/04/06/wait-for-element/ "ある要素が表示されるまで待つJSライブラリを書いた(MutationObserver) | Web Scratch")

----

## mohebifar/xto6
[github.com/mohebifar/xto6](https://github.com/mohebifar/xto6 "mohebifar/xto6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

ES5のコードをES6へ変換するTranspiler

----
