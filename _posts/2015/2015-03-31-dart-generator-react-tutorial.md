---
title: "2015-03-31のJS: Dart to JS、ES6 Generator、Reactでシングルページアプリケーション作成"
author: azu
layout: post
date : 2015-03-31T22:04
category: JSer
tags:
    - Dart
    - ES6
    - React
    - tutorial

---

JSer.info #221 - DartをChromeに載せることは諦めて、DartをJavaScriptに変換する部分に注力することが発表されました。

- [Dart News &amp; Updates: Dart for the Entire Web](http://news.dartlang.org/2015/03/dart-for-entire-web.html "Dart News &amp; Updates: Dart for the Entire Web")

またほぼ同時に[Dart 1.9](http://news.dartlang.org/2015/03/dart-19-release-youve-been-await-ing-for.html)がリリースされています。

Dartは[ECMA-408](http://www.ecma-international.org/publications/standards/Ecma-408.htm "ECMA-408")として標準化されていますが、Dart 1.9では[Dart Programming Language Specification, 2nd Edition](https://www.dartlang.org/docs/spec/ "Dart Programming Language Specification, 2nd Edition")([翻訳](http://www.cresc.co.jp/tech/java/Google_Dart/DartLanguageSpecification_Japanese.pdf "DartLanguageSpecification_Japanese.pdf"))で追加定義されたasync/awaitやenumなどのサポートが入っています。

詳しくは以下を見るといいです。

- [Dart News & Updates: Dart 1.9: The release you’ve been await-ing for](http://news.dartlang.org/2015/03/dart-19-release-youve-been-await-ing-for.html)
- [Dart 1.9.1リリースノート - Qiita](http://qiita.com/laco0416/items/cd6685ab3cd115613d37)

----

[ES6 generators in depth](http://www.2ality.com/2015/03/es6-generators.html "ES6 generators in depth")という記事ではES6のGeneratorについてを掘り下げて解説されています。
[Iterables and iterators in ECMAScript 6](http://www.2ality.com/2015/02/es6-iteration.html "Iterables and iterators in ECMAScript 6")の続編的な記事なので、こちらを先に見ておくと良いです。

Generatorの役割を3種類に分けて紹介していて、それぞれについて例とともに詳しく解説されています。

1. Iterators (data producers)
2. Observers (data consumers)
3. Coroutines (data producers and consumers)

----

[mikechau/react-primer-draft](https://github.com/mikechau/react-primer-draft "mikechau/react-primer-draft")というReactを使ってシングルページアプリケーションを作るチュートリアルが公開されいます。

Reactを使ったアプリの作成について丁寧に書かれていて、参考リンクも多く含まれているので一度見てみると良さそうです。
まだ未完成ですがES6についてやルータ、Fluxといったライブラリについても書いていくようです。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint 0.18.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/03/eslint-0.18.0-released](http://eslint.org/blog/2015/03/eslint-0.18.0-released "ESLint 0.18.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.18.0 リリース。
JSXの構文についての処理はESLintから完全に削除され、[eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react "eslint-plugin-react")へ移植された。

----

## Ember.js - Ember.js 1.11.0 and 1.12 Beta Released
[emberjs.com/blog/2015/03/27/ember-1-11-0-released.html](http://emberjs.com/blog/2015/03/27/ember-1-11-0-released.html "Ember.js - Ember.js 1.11.0 and 1.12 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 1.11リリース。
HTMLBarsの構文強化やその構文の解説がされている。

----

## Node v0.12.1 (Stable)
[blog.nodejs.org/2015/03/23/node-v0-12-1-stable/](http://blog.nodejs.org/2015/03/23/node-v0-12-1-stable/ "Node v0.12.1 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.1リリース。
OpenSSLのアップデート

----
<h1 class="site-genre">アーティクル</h1>

----

## Dart News &amp; Updates: Dart for the Entire Web
[news.dartlang.org/2015/03/dart-for-entire-web.html](http://news.dartlang.org/2015/03/dart-for-entire-web.html "Dart News &amp; Updates: Dart for the Entire Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

DartはDartVMをChromiumに載せることは諦めて、Dart2jsに集中するとのこと。
また、Dart 1.9がリリースされている。

- [Dart News & Updates: Dart 1.9: The release you’ve been await-ing for](http://news.dartlang.org/2015/03/dart-19-release-youve-been-await-ing-for.html)
- [Dart 1.9.1リリースノート - Qiita](http://qiita.com/laco0416/items/cd6685ab3cd115613d37)

----

## A Preview of WinJS 4.0
[blogs.windows.com/buildingapps/2015/03/27/a-preview-of-winjs-4-0/](http://blogs.windows.com/buildingapps/2015/03/27/a-preview-of-winjs-4-0/ "A Preview of WinJS 4.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">windows</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WinJS 4.0のプレビュー版が公開された

----

## &quot;Project Spartan&quot; in the Windows Technical Preview build 10049 - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2015/03/30/quot-project-spartan-quot-in-the-windows-technical-preview-build-10049.aspx](http://blogs.msdn.com/b/ie/archive/2015/03/30/quot-project-spartan-quot-in-the-windows-technical-preview-build-10049.aspx "&quot;Project Spartan&quot; in the Windows Technical Preview build 10049 - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">windows</span> <span class="jser-tag">IE</span> <span class="jser-tag">ReleaseNote</span></p>

Project Spartanが入ったWindows 10のプレビュー版が公開された
UserVoiceでアイデアへの投票を募集している。

- [Project Spartan: Hot (33 ideas) – Feature Suggestions for Windows](https://windows.uservoice.com/forums/285214-project-spartan "Project Spartan: Hot (33 ideas) – Feature Suggestions for Windows")

----

## Node.js Tools 1.0 for Visual Studio - The Visual Studio Blog - Site Home - MSDN Blogs
[blogs.msdn.com/b/visualstudio/archive/2015/03/25/node-js-tools-1-0-for-visual-studio.aspx](http://blogs.msdn.com/b/visualstudio/archive/2015/03/25/node-js-tools-1-0-for-visual-studio.aspx "Node.js Tools 1.0 for Visual Studio - The Visual Studio Blog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">IDE</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js Tools 1.0 for Visual Studioリリース。
またリポジトリがGitHubに移行した

- [Microsoft/nodejstools](https://github.com/Microsoft/nodejstools "Microsoft/nodejstools")

----

## ES6 generators in depth
[www.2ality.com/2015/03/es6-generators.html](http://www.2ality.com/2015/03/es6-generators.html "ES6 generators in depth")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6のGeneratorについての詳しい解説。
Generatorとは何か、構成要素、Iterator、Generatorの使い方、CSPなど幅広く書かれてる

----

## mikechau/react-primer-draft
[github.com/mikechau/react-primer-draft](https://github.com/mikechau/react-primer-draft "mikechau/react-primer-draft")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">book</span></p>

Reactでシングルページアプリケーションを作るチュートリアル的な文章。
React.Component について詳しく書かれている

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Reusable Component UI Design // Speaker Deck
[speakerdeck.com/tyshgc/reusable-component-ui-design](https://speakerdeck.com/tyshgc/reusable-component-ui-design "Reusable Component UI Design // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

再利用できるReact Componentについてのスライド

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Package Quality
[packagequality.com/](http://packagequality.com/ "Package Quality")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span></p>

npmのパッケージのクオリティチェック。
issueの数やバージョンなどの情報を元に数値化してる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Microsoft/IEDiagnosticsAdapter
[github.com/Microsoft/IEDiagnosticsAdapter](https://github.com/Microsoft/IEDiagnosticsAdapter "Microsoft/IEDiagnosticsAdapter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">IE</span> <span class="jser-tag">debug</span> <span class="jser-tag">proxy</span> <span class="jser-tag">software</span></p>

Chrome remote debug protocolを使ってIEをデバッグできるプロキシ。
ChromeでIEで見てるサイトをデバッグ出来る

----

## operasoftware/operachromiumdriver
[github.com/operasoftware/operachromiumdriver](https://github.com/operasoftware/operachromiumdriver "operasoftware/operachromiumdriver")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">webdriver</span></p>

OperaのWebDriver実装

----

## bloomberg/brisket
[github.com/bloomberg/brisket](https://github.com/bloomberg/brisket "bloomberg/brisket")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">backbone.js</span> <span class="jser-tag">library</span></p>

Bloombergのisomorphic JavaScriptフレームワーク。
Rendrと同じくBackboneをベースとしたサーバサイドレンダリングの仕組みを持つ。

- [At Bloomberg We’ve Made Brisket. And It Can Make Anything. | Bloomberg L.P.](http://www.bloomberg.com/company/2015-03-24/bloomberg-weve-made-brisket-can-make-anything/ "At Bloomberg We’ve Made Brisket. And It Can Make Anything. | Bloomberg L.P.")

----

## cssnext/cssnext
[github.com/cssnext/cssnext](https://github.com/cssnext/cssnext "cssnext/cssnext")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

CSS4などの仕様をCSS3相当に変換するツールとライブラリ。

- [Myth - CSS the way it was imagined.](http://www.myth.io/ "Myth - CSS the way it was imagined.")

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: Front-End Architecture: A Modern Blueprint for Scalable and Sustainable Design Systems: Micah Godbolt
[www.amazon.com/dp/1491926783](http://www.amazon.com/dp/1491926783 "Amazon: Front-End Architecture: A Modern Blueprint for Scalable and Sustainable Design Systems: Micah Godbolt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">book</span></p>

2015年10月25日発売
フロントエンドアーキテクチャ。
JavaScriptやツール、CSSなど幅広く扱ってる

----
