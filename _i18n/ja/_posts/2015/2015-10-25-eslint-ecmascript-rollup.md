---
title: "2015-10-25のJS: ESLint入門、ECMAScriptとは何か?、rollupとES6 modules"
author: azu
layout: post
date : 2015-10-25T20:20
category: JSer
tags:
    - ESLint
    - ECMAScript
    - Bundle
    - Browserify
    - rollup

---

JSer.info #250 - [ESLint v1.7.0](http://eslint.org/blog/2015/10/eslint-v1.7.0-released/ "ESLint v1.7.0")がリリースされました。
`.eslintrc`内に`"extends": "./foo.js"`と書くことでJavaScriptファイルを継承出来るようになっています。

また、[JavaScript - ESLint 最初の一歩 - Qiita](http://qiita.com/mysticatea/items/f523dab04a25f617c87d "JavaScript - ESLint 最初の一歩 - Qiita")という記事では、ESLintの使い方、設定方法、エディタ、ES6関連のルールについてなどが紹介されています。
初めてESLintを使う際に見てみるといいかもしれません。

----

[ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch")という記事ではECMAScriptについてQ&A形式で紹介しています。

ECMAScriptを策定してるTC39とは何か?という疑問から、ES6とES.nextの仕様策定プロセス、どのような仕様が提案されているかなどについて書かれています。

仕様策定に関して疑問が出やすい部分について一通り書かれているので、興味がある人は見てみると良いかもしれません。

-----

[rollup.js](http://rollupjs.org/ "rollup.js")はBrowserify、RequireJS、Webpackのようにモジュールの結合を行うbundleツールです。
デフォルトではES6 modulesのみを結合しますが[plugin](https://github.com/rollup/rollup/pull/207 "plugin")によってCommonJSなども対応するようです。

特徴として[サイト上](http://rollupjs.org)で試すことが出来ますが、他のbundleツールと違いそれぞれのモジュールをラップした関数などがなくキレイに結合されています。
また、モジュールを読み込んでいても使用していない関数は除去されるなどの最適化が行われています。

これはES6 modulesがCommonJSの`require`のように動的にモジュールを読み込めるものではなく、[静的に依存関係が決まる](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/)こと等を上手く活用しています。

- [Cycles · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/Cycles "Cycles · rollup/rollup Wiki")
- [ES6 modules · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/ES6-modules "ES6 modules · rollup/rollup Wiki")
- [Bindings · rollup/rollup Wiki](https://github.com/rollup/rollup/wiki/Bindings "Bindings · rollup/rollup Wiki")
- [JavaScript - ES6 Modules 間では export/import された変数（？）は同期される - Qiita](http://qiita.com/shuhei/items/f74e1f7478839e829b16 "JavaScript - ES6 Modules 間では export/import された変数（？）は同期される - Qiita")

他のbundleツールとの違いについては以下を参照してみてください。

- [Yet another module bundler · Issue #219 · rollup/rollup](https://github.com/rollup/rollup/issues/219 "Yet another module bundler · Issue #219 · rollup/rollup")

実際にbundleした結果を比較したものが[nolanlawson/rollup-comparison](https://github.com/nolanlawson/rollup-comparison "nolanlawson/rollup-comparison")で公開されています。
(Webpack 2でも[ES6 modulesを元に使用されていないコードの削除](https://github.com/webpack/webpack/pull/861#issuecomment-149997270)は予定されています。)

このようにrollupはES6 modulesに最適化されたデザインですが、ES6で書いたコードをnpmなどで公開するルールなどはまだ整備されていないのが現状です。

[The struggles of publishing a JavaScript library | Read the Tea Leaves](http://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/ "The struggles of publishing a JavaScript library | Read the Tea Leaves")では、npmやBower、jspmにライブラリをどのように公開するかという話が書かれています。

その中でも、npmでは`"main"` フィールドに指定するエントリーポイントは基本的にES5環境向けにビルドしたものとなっていますが、公開されたライブラリにES6のコードをどう含めるかについては何も決まっていません。

そのため、ES6 modulesのコード(ライブラリのコードも含む)を参照したいrollupは`jsnext:main`というフィールドにES6のエントリーポイントを指定するような規約を設けています。

[rollup.js](http://rollupjs.org/ "rollup.js")で公開されたライブラリのパッケージにもES6のコードが含まれている事によるメリットが提示されてきたので、今後npmやbundleツールでES6のコードをどう扱うかという話に何らかの進展があるかもしれません。

ちなみに、ブラウザがどのようにES6 modulesを読み込むかという仕様は[whatwg/loader](https://github.com/whatwg/loader "whatwg/loader")にて議論されています。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint v1.7.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/10/eslint-v1.7.0-released/](http://eslint.org/blog/2015/10/eslint-v1.7.0-released/ "ESLint v1.7.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.7.0リリース。
eslintrcの`extends`にJavaScriptのファイルパスそのもを書いて設定を継承出来るようになった

----

## jsdom/Changelog.md at 7.0.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/7.0.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/7.0.0/Changelog.md "jsdom/Changelog.md at 7.0.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 7.0.0リリース。
Node.js 4.0以降が必要になった。
XMLHttpRequestの再実装、`HTMLTemplateElement.prototype.content`の追加など

----

## esprima/ChangeLog at 2.7.0 · jquery/esprima
[github.com/jquery/esprima/blob/2.7.0/ChangeLog](https://github.com/jquery/esprima/blob/2.7.0/ChangeLog "esprima/ChangeLog at 2.7.0 · jquery/esprima")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

esprima 2.7.0リリース。
`esprima.tokenize`にdelegatorオプションの追加など

- [API: Token delegator · Issue #1332 · jquery/esprima](https://github.com/jquery/esprima/issues/1332 "API: Token delegator · Issue #1332 · jquery/esprima")

----
<h1 class="site-genre">アーティクル</h1>

----

## JavaScript - ESLint 最初の一歩 - Qiita
[qiita.com/mysticatea/items/f523dab04a25f617c87d](http://qiita.com/mysticatea/items/f523dab04a25f617c87d "JavaScript - ESLint 最初の一歩 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLintの使い方、設定方法、ES6関連のルールについて

----

## ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch
[efcl.info/2015/10/18/ecmascript-paper/](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">まとめ</span></p>

ECMAScriptとは何か?からES2016の策定プロセス、進捗の確認方法、コントリビュートのやり方、TranspilerやPolyfillの役割など仕様策定に関する疑問をまとめたもの

----

## ecmascript-6-destructuring-gotcha
[www.nczonline.net/blog/2015/10/ecmascript-6-destructuring-gotcha/](https://www.nczonline.net/blog/2015/10/ecmascript-6-destructuring-gotcha/ "ecmascript-6-destructuring-gotcha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

`let {} = {};` がES6でvalidであるというのは混乱を起こすのではという話。
現在、EMCAScript仕様のIssueとして修正するべきかが議論されている。

- [Destructuring declarations that bind nothing should probably be an early error · Issue #97 · tc39/ecma262](https://github.com/tc39/ecma262/issues/97 "Destructuring declarations that bind nothing should probably be an early error · Issue #97 · tc39/ecma262")

----

## EventEmitter in ES6
[www.datchley.name/es6-eventemitter/](http://www.datchley.name/es6-eventemitter/ "EventEmitter in ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6でシンプルにEventEmitterやObserverを実装しながら、ES6の機能について学ぶ話

----

## The struggles of publishing a JavaScript library | Read the Tea Leaves
[nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/](http://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/ "The struggles of publishing a JavaScript library | Read the Tea Leaves")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

bower、npm、jspmに対応したライブラリの公開方法と設定について。
Browserify、Webpack、rollupでのライブラリのビルドについてなど

- [nolanlawson/hello-javascript](https://github.com/nolanlawson/hello-javascript "nolanlawson/hello-javascript")

----

## Experimenting with Object.observe in JavaScript
[www.sitepoint.com/experimenting-object-observe-javascript-found-useful/](http://www.sitepoint.com/experimenting-object-observe-javascript-found-useful/ "Experimenting with Object.observe in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES.nextで提案されている`Object.observe`の現状について。
ブラウザのサポート状況、Polyfillについて

----

## StrongLoop | Moving toward Express 5
[strongloop.com/strongblog/moving-toward-express-5/](https://strongloop.com/strongblog/moving-toward-express-5/ "StrongLoop | Moving toward Express 5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Express 5αでの変更点についての解説

----

## TypeScript 1.6時代の.d.ts管理について意見を述べておく - Qiita
[qiita.com/vvakame/items/72d22e33632178f7db24](http://qiita.com/vvakame/items/72d22e33632178f7db24 "TypeScript 1.6時代の.d.ts管理について意見を述べておく - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">まとめ</span></p>

npmパッケージとTypeScriptのd.tsの管理について。

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## The Accessibility Project
[a11yproject.com/](http://a11yproject.com/ "The Accessibility Project")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">アクセシビリティ</span> <span class="jser-tag">まとめ</span></p>

ウェブ開発者向けにアクセシビリティについてまとめているサイト

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## rollup.js
[rollupjs.org/](http://rollupjs.org/ "rollup.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

ES6 modulesをBrowserifyなどのようにbundleするツール。
使用していない関数は無視したり、余計なラップする関数なしに結合が出来る。
デフォルトではES6のみだがプラグインでCommonJSなども対応する。

----

## Rich-Harris/magic-string
[github.com/Rich-Harris/magic-string](https://github.com/Rich-Harris/magic-string "Rich-Harris/magic-string")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

Source Mapをサポートしてるコード変換ライブラリ。
文字列の上書き、追加、削除などを文字列操作のように変更を行うことができる。

----

## .eslintrc editor
[pirosikick.github.io/eslintrc-editor/](https://pirosikick.github.io/eslintrc-editor/ ".eslintrc editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">設定</span></p>

ESLintの設定をGUIでポチポチと作成することが出来るツール

- [ESLintの設定ファイルをブラウザでポチポチして作るツールを作った - Qiita](http://qiita.com/pirosikick/items/64cb38752fa252911501 "ESLintの設定ファイルをブラウザでポチポチして作るツールを作った - Qiita")

----

## cotejp/webmidi
[github.com/cotejp/webmidi](https://github.com/cotejp/webmidi "cotejp/webmidi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">sound</span> <span class="jser-tag">library</span></p>

Web MIDI APIをラップしたライブラリ

----

## dleitee/valid.js
[github.com/dleitee/valid.js](https://github.com/dleitee/valid.js "dleitee/valid.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

String、Number、Date、Boolなどにおけるバリデーションを組み合わせたバリデーション関数を作成できるライブラリ

----

## rodrigogs/kairos
[github.com/rodrigogs/kairos](https://github.com/rodrigogs/kairos "rodrigogs/kairos")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

時間同士の四則演算や比較を行うライブラリ

----
<h1 class="site-genre">書籍関係</h1>

----

## SVG Text Layout - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920043072.do](http://shop.oreilly.com/product/0636920043072.do "SVG Text Layout - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">book</span></p>

SVGにおけるテキストのレイアウトについての書籍

----
