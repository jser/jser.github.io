---
title: "2015-09-25のJS: Firefox 41.0、npm 3.x stableリリース、XRegExp 3.0.0"
author: azu
layout: post
date : 2015-09-25T15:18
category: JSer
tags:
    - Firefox
    - npm
    - node
    - regexp
    - library

---


JSer.info #246 - Firefox 41.0がリリースされました。

- [Firefox 41.0 リリースノート](http://www.mozilla.jp/firefox/41.0/releasenotes/ "Firefox 41.0 リリースノート")
- [Firefox 41 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/41 "Firefox 41 for developers - Mozilla | MDN")

CSSの縦書き文章のレイアウト機能([writing-mode](https://developer.mozilla.org/ja/docs/Web/CSS/writing-mode "writing-mode"))がデフォルトで有効となりました。
ES6の対応として`Symbol.species`、`new.target`のサポート、 destructuringやlet式の仕様追従が行われています。

また、`Navigator.onLine`がWindowsとMacでまともな動作をするようになり、Notifications APIなどがWeb Worker内で利用できるようになっています。


----
npm v3.xがstableリリースされています。

- [The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...](http://blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the "The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...")

v3.3.2まではβとしてリリースされているため、`npm install npm`ではインストールされてませんでしたが、v3.3.3からβでなくなったためstableとしてインストールされます。

Node.jsにバンドルされるのは次のメジャーアップデート時になると思いますが、npm v3.xの変更点については以下を読むといいと思います。

- [npm3 ❓ // Speaker Deck](https://speakerdeck.com/watilde/npm3)
- [NPM 3 Betaは、Windowsユーザーによいニュースをもたらす](http://www.infoq.com/jp/news/2015/07/npm)

依存関係のディレクトリ構造がフラットになり、またpeerDependenciesがデフォルトでインストールされなくなる等が、より安全なインストールが出来るような変更が行わなわれています。

動かなくなるケースは少ないと思いますが、`npm install`に時間がかかるというIssueが挙げられています。

- [npm@3 wants to be faster · Issue #8826 · npm/npm](https://github.com/npm/npm/issues/8826 "npm@3 wants to be faster · Issue #8826 · npm/npm")

-----

拡張した正規表現を扱える[XRegExp](http://xregexp.com/ "XRegExp") 3.0.0がリリースされました。

- [Flagrant Badassery » XRegExp 3.0.0!](http://blog.stevenlevithan.com/archives/xregexp-3-0-0 "Flagrant Badassery » XRegExp 3.0.0!")
- [Version history :: XRegExp](http://xregexp.com/history/ "Version history :: XRegExp")

3.0.0ではES6に追従するような変更、Unicodeのサポート、速度の改善などが行われています。

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 41.0 リリースノート
[www.mozilla.jp/firefox/41.0/releasenotes/](http://www.mozilla.jp/firefox/41.0/releasenotes/ "Firefox 41.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 41.0リリース。
縦書きレイアウトの機能がデフォルトで有効に、`Symbol.species`、`new.target`のサポート、Web Workerの中でNotification APIなどが利用できるようになるなど

- [Firefox 41 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/41 "Firefox 41 for developers - Mozilla | MDN")

----

## Node v4.1.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v4.1.0/](https://nodejs.org/en/blog/release/v4.1.0/ "Node v4.1.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v4.1.0リリース。
Buffer作成の改善、fs.WriteStreamの書き込み速度の改善など

----

## The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...
[blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the](http://blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the "The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 3.xがlatestとしてリリースされた。
`npm install -g npm` でnpm 3.xがインストールされるようになった

- [Release v3.0.0 · npm/npm](https://github.com/npm/npm/releases/tag/v3.0.0 "Release v3.0.0 · npm/npm")

----

## Announcing TypeScript 1.6 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/09/16/announcing-typescript-1-6.aspx](http://blogs.msdn.com/b/typescript/archive/2015/09/16/announcing-typescript-1-6.aspx "Announcing TypeScript 1.6 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.6リリース。
JSX(TSX)、Class expressions、User defined type guards、Intersection types、Abstract classes、モジュール解決アルゴリズムの改善など

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-16 "Breaking Changes · Microsoft/TypeScript Wiki")

----

## Release 1.0 · bosonic/bosonic
[github.com/bosonic/bosonic/releases/tag/v1.0](https://github.com/bosonic/bosonic/releases/tag/v1.0 "Release 1.0 · bosonic/bosonic")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Web Componentsを扱うライブラリであるBosonic 1.0リリース

- [Bosonic Web Component](http://bosonic.github.io/ "Bosonic Web Component")

----

## Flagrant Badassery » XRegExp 3.0.0!
[blog.stevenlevithan.com/archives/xregexp-3-0-0](http://blog.stevenlevithan.com/archives/xregexp-3-0-0 "Flagrant Badassery » XRegExp 3.0.0!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span></p>

正規表現の拡張ライブラリであるXRegExp 3.0.0リリース。
Unicode周りのサポート改善、`A`(astral)フラグの追加、ES6に追従した変更など

----

## RxJS/CHANGELOG.md at 5.0.0-alpha.1 · ReactiveX/RxJS
[github.com/ReactiveX/RxJS/blob/5.0.0-alpha.1/CHANGELOG.md](https://github.com/ReactiveX/RxJS/blob/5.0.0-alpha.1/CHANGELOG.md "RxJS/CHANGELOG.md at 5.0.0-alpha.1 · ReactiveX/RxJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ReactiveX/RxJS 5.0.0αリリース

----

## リリース バージョン 10547 : Microsoft Edge Dev
[dev.modern.ie/platform/changelog/desktop/10547/](https://dev.modern.ie/platform/changelog/desktop/10547/ "リリース バージョン 10547 : Microsoft Edge Dev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge Build 10547リリース。
`<template>`、`<picture>`の追加、`<a download>`の対応、SVGで外部コンテンツのロード、フラグ付きでAsync Function、`**`演算子の対応など

- [Microsoft Edge の変更ログ - Windows 10 Insider Preview Build 10547 - Browser](http://browser.hatenablog.com/entry/2015/09/21/180947 "Microsoft Edge の変更ログ - Windows 10 Insider Preview Build 10547 - Browser")

----

## ESLint v1.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/09/eslint-v1.5.0-released/](http://eslint.org/blog/2015/09/eslint-v1.5.0-released/ "ESLint v1.5.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.5.0リリース。
`--fix`に対応するルールの追加、`--debug`フラグの追加など

----

## Release ES2016 Draft 1 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-1](https://github.com/tc39/ecma262/releases/tag/es2016-draft-1 "Release ES2016 Draft 1 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 1リリース。
仕様書がWordからEcmarkupで書かれるようになり、GitHubでリリースされた。

- [New in ECMAScript 2016, JavaScript&#x27;s First Yearly Release](http://www.infoq.com/presentations/ecmascript-2016 "New in ECMAScript 2016, JavaScript&#x27;s First Yearly Release")

----
<h1 class="site-genre">アーティクル</h1>


----

## React.js v0.14 changes - blog.koba04.com
[blog.koba04.com/post/2015/09/22/react-js-v014-changes/](http://blog.koba04.com/post/2015/09/22/react-js-v014-changes/ "React.js v0.14 changes - blog.koba04.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 0.14の変更点について

----

## Pointer Events Will Make Cross-Browser Touch Support Easy
[www.sitepoint.com/pointer-events-will-make-cross-browsers-touch-support-easy/](http://www.sitepoint.com/pointer-events-will-make-cross-browsers-touch-support-easy/ "Pointer Events Will Make Cross-Browser Touch Support Easy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Pointer Eventsのコンセプト、実際にどう使うかについての解説記事。
feature detectionの方法、ジェスチャーを扱うMSGesture objectについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ESDoc Hosting Service - hosts documentation for JavaScript(ES6) with ESDoc
[doc.esdoc.org/](https://doc.esdoc.org/ "ESDoc Hosting Service - hosts documentation for JavaScript(ES6) with ESDoc")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSDoc</span> <span class="jser-tag">document</span></p>

[ESDoc](https://esdoc.org)で書かれたドキュメントをホスティングするサービス。
GitHubリポジトリのURLを登録するとESDocによるドキュメントが生成される。`esdoc.json`の設定ファイルがない場合も自動的に`src/`のコードを元に生成される。

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mantoni/eslint_d.js
[github.com/mantoni/eslint\_d.js](https://github.com/mantoni/eslint_d.js "mantoni/eslint\_d.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">サーバー</span></p>

ESLintをサーバとして立ててLintを行うツール。
初回起動のオーバーヘッドがなくなるので高速に実行出来る

----

## ConquestArrow/dtsmake · GitHub
[github.com/ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake "ConquestArrow/dtsmake · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptを与えるとd.tsを生成するツール

- [TypeScript型定義ファイルのコツと生成ツール dtsmake - Qiita](http://qiita.com/ConquestArrow/items/450f961c3d54bc932cf3 "TypeScript型定義ファイルのコツと生成ツール dtsmake - Qiita")

----

## fireball-x/editor-framework
[github.com/fireball-x/editor-framework](https://github.com/fireball-x/editor-framework "fireball-x/editor-framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span></p>

ElectronとPolymerをベースとしたエディタ向けのフレームワーク

----

## Release the docs!
[sassdoc.com/](http://sassdoc.com/ "Release the docs!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JSDoc</span></p>

コメントでアノテーションを書いたSassのコードからドキュメントを生成するツール

----
<h1 class="site-genre">書籍関係</h1>

----

## Amazon: 速習ECMAScript6: 次世代の標準JavaScriptを今すぐマスター！ [Kindle版]: 山田祥寛
[www.amazon.co.jp/dp/B014MS5XWK?tag=amazon0abac-22](http://www.amazon.co.jp/dp/B014MS5XWK?tag=amazon0abac-22 "Amazon: 速習ECMAScript6: 次世代の標準JavaScriptを今すぐマスター！ \[Kindle版\]: 山田祥寛")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

ES6についてのKindle本

- [【新刊紹介】『速習 ECMAScript 6』発売、次期JavaScript仕様を短期間でキャッチアップ！：CodeZine（コードジン）](http://codezine.jp/article/detail/8963 "【新刊紹介】『速習 ECMAScript 6』発売、次期JavaScript仕様を短期間でキャッチアップ！：CodeZine（コードジン）")

----

## Building Isomorphic JavaScript Apps: From Concept to Implementation to Real-World Solutions: Jason Strimpel, Maxime Najim: 9781491932933: Amazon.com: Books
[www.amazon.com/dp/1491932937/](http://www.amazon.com/dp/1491932937/ "Building Isomorphic JavaScript Apps: From Concept to Implementation to Real-World Solutions: Jason Strimpel, Maxime Najim: 9781491932933: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016年4月30日発売
IsomorphicについてのOreilly本

----
