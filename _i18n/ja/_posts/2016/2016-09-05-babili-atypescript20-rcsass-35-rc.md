---
title: "2016-09-05のJS: Babili α、TypeScript 2.0 RC、Sass 3.5 RC"
author: azu
layout: post
date : 2016-09-05T19:41
category: JSer
tags:
    - Sass
    - Babel
    - TypeScript

---

JSer.info #295 - TypeScript 2.0 RCがリリースされました。

- [Announcing TypeScript 2.0 RC | TypeScript](https://blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/ "Announcing TypeScript 2.0 RC | TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

`--strictNullChecks`でのnullチェックや[Tagged union types](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#tagged-union-types "Tagged union types")の、[tsconfig.jsonがglobをサポート](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#glob-support-in-tsconfigjson)など色々強化されています。


----

Babelのプラグインとしてminifyを行う[babili](https://github.com/babel/babili "babili")がαリリースされました。

- [Babili (babel-minify) · Babel](https://babeljs.io/blog/2016/08/30/babili "Babili (babel-minify) · Babel")

ES2015+のコードに対して圧縮や未使用コードの削除などを行うBabelプラグインとなっています。
Rollupやwebpackはbundleツールなので少し領域が異なりますが、[UglifyJS2](https://github.com/mishoo/UglifyJS2)のようなツールに対抗できるポジションを目指しているようです。

----
CSSメタ言語のSass 3.5RCがリリースされました。

- [Sass 3.5 Release Candidate « Sass Blog](http://blog.sass-lang.com/posts/809572-sass-35-release-candidate "Sass 3.5 Release Candidate « Sass Blog")

C++で実装しなおした[LibSass](http://sass-lang.com/libsass "LibSass")がRuby版と殆ど100％の互換性となったようです。
3.5ではCSS Custom Property、First-Class Functions、Bracketed Listsなどのサポートが追加されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## esprima/ChangeLog at 3.0.0 · jquery/esprima
[github.com/jquery/esprima/blob/3.0.0/ChangeLog](https://github.com/jquery/esprima/blob/3.0.0/ChangeLog "esprima/ChangeLog at 3.0.0 · jquery/esprima")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">ReleaseNote</span></p>

esprima 3.0.0リリース。
ES2016 `**` をサポート、JSXのサポートなど

----

## Sass 3.5 Release Candidate « Sass Blog
[blog.sass-lang.com/posts/809572-sass-35-release-candidate](http://blog.sass-lang.com/posts/809572-sass-35-release-candidate "Sass 3.5 Release Candidate « Sass Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">ReleaseNote</span></p>

Sass 3.5 RCリリース。
libsassがRuby版とほぼ100％の互換性を持つように。
CSS Custom Propertyのサポートなど

----

## jsdom/Changelog.md at 9.5.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.5.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.5.0/Changelog.md "jsdom/Changelog.md at 9.5.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.5.0リリース。
`document.scripts`、 `document.embeds`と `document.plugins`の追加。
`document.getElementsByTagName`が`HTMLCollection`を返すようになるなど

----

## Angular 2 RC6
[angularjs.blogspot.com/2016/09/angular-2-rc6\_1.html](http://angularjs.blogspot.com/2016/09/angular-2-rc6_1.html "Angular 2 RC6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2 RC6リリース
RC5以下で非推奨となっていたAPIの削除、npmパッケージにES6 modules形式のソースを含むように、TypeScript 2.0に対応など

- [Angular 2 RC.6がリリースされました · Angular2 Info](https://ng2-info.github.io/2016/09/angular-2-rc-6/ "Angular 2 RC.6がリリースされました · Angular2 Info")
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-rc6-2016-08-31 "angular/CHANGELOG.md at master · angular/angular")

----

## Release Notes for Safari Technology Preview Release 12 | WebKit
[webkit.org/blog/6928/release-notes-for-safari-technology-preview-release-12/](https://webkit.org/blog/6928/release-notes-for-safari-technology-preview-release-12/ "Release Notes for Safari Technology Preview Release 12 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 12リリース。
Fetch APIがデフォルトで有効に、Resource Timingの仕様追従など

----

## Node v6.5.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.5.0/](https://nodejs.org/en/blog/release/v6.5.0/ "Node v6.5.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.5.0リリース。
inspectorがuncaught exceptionをサポートなど

----

## Announcing TypeScript 2.0 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/](https://blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/ "Announcing TypeScript 2.0 RC | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.0 RCリリース。
Tagged Unions、numberとstringのLiteral Typeを強化、tsconfig.jsonでglobの対応など

----
<h1 class="site-genre">アーティクル</h1>

----

## Babili (babel-minify) · Babel
[babeljs.io/blog/2016/08/30/babili](https://babeljs.io/blog/2016/08/30/babili "Babili (babel-minify) · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

BabelのminifyプラグインであるBabili βリリース。
Uglifyと違って変換後のES5なコードではなく、ES2015+のコードに対して圧縮を行う。
そのためFlowなどの型情報を使った圧縮なども可能になる。

----

## The Case for Custom Elements: Part 1 – Dev Channel – Medium
[medium.com/dev-channel/the-case-for-custom-elements-part-1-65d807b4b439](https://medium.com/dev-channel/the-case-for-custom-elements-part-1-65d807b4b439 "The Case for Custom Elements: Part 1 – Dev Channel – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Custome Elementのケーススタディ

----

## 15K 行のアプリを TypeScript 1.8 から 2.0 に移行してみた - はやくプログラムになりたい
[rhysd.hatenablog.com/entry/2016/07/15/090000](http://rhysd.hatenablog.com/entry/2016/07/15/090000 "15K 行のアプリを TypeScript 1.8 から 2.0 に移行してみた - はやくプログラムになりたい")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2系への移行とオプションについて

----

## the new code – Web Developer Reading List: Maths in JavaScript
[thenewcode.com/1131/Web-Developer-Reading-List-Maths-in-JavaScript](http://thenewcode.com/1131/Web-Developer-Reading-List-Maths-in-JavaScript "the new code – Web Developer Reading List: Maths in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Mathについての学ぶチュートリアル

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Reactの最新動向とベストプラクティス // Speaker Deck
[speakerdeck.com/koba04/reactfalsezui-xin-dong-xiang-tobesutopurakuteisu](https://speakerdeck.com/koba04/reactfalsezui-xin-dong-xiang-tobesutopurakuteisu "Reactの最新動向とベストプラクティス // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">スライド</span></p>

Reactのコンポーネントの作り方やテスト、React周りで最近でてきたツールについてのスライド

----

## Service Worker Deep Dive - Google スライド
[docs.google.com/presentation/d/19x3yi7Jn-6In5igGYfEiK0tBfNI290BAclT0AiqDj4Q/pub#slide=id.p](https://docs.google.com/presentation/d/19x3yi7Jn-6In5igGYfEiK0tBfNI290BAclT0AiqDj4Q/pub#slide=id.p "Service Worker Deep Dive - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">スライド</span></p>

ここ1年ぐらいのService Worker周りの変化についてのスライド。
Push Notification、Stream、Background、Foreign Fetch、Header-based Install、Origin Trialなど

----

## Edge Web Technologies and Browser Vendors
[www.slideshare.net/dynamis/edge-web-technologies-and-browser-vendors](http://www.slideshare.net/dynamis/edge-web-technologies-and-browser-vendors "Edge Web Technologies and Browser Vendors")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">browser</span> <span class="jser-tag">スライド</span></p>

ここ最近のウェブブラウザの変化についてのスライド。
ウェブ互換性への方針、新しい機能などについてざっくりと紹介されている

----

## WAI-ARIA珍プレー好プレー
[www.slideshare.net/mlca11y/waiaria-65618928](http://www.slideshare.net/mlca11y/waiaria-65618928 "WAI-ARIA珍プレー好プレー")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">スライド</span></p>

> WAI-ARIAは表現やインタラクションを変えない

role="button"を付けてキーボードによるインタラクションを忘れているケース、メニューの例などについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## html-best-practices/README.ja.md at master · hail2u/html-best-practices
[github.com/hail2u/html-best-practices/blob/master/README.ja.md](https://github.com/hail2u/html-best-practices/blob/master/README.ja.md "html-best-practices/README.ja.md at master · hail2u/html-best-practices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">翻訳</span></p>

HTML Best Practices日本語訳

- [普通のHTMLの書き方（またはHTML Best Practices日本語版） - Weblog - Hail2u.net](https://hail2u.net/blog/webdesign/html-best-practices-in-japanese.html "普通のHTMLの書き方（またはHTML Best Practices日本語版） - Weblog - Hail2u.net")
- [HTML5のSVG要素では名前空間宣言が省略できる - 週刊SVG](http://ssvvgg.net/post/147494232850/html5%E3%81%AEsvg%E8%A6%81%E7%B4%A0%E3%81%A7%E3%81%AF%E5%90%8D%E5%89%8D%E7%A9%BA%E9%96%93%E5%AE%A3%E8%A8%80%E3%81%8C%E7%9C%81%E7%95%A5%E3%81%A7%E3%81%8D%E3%82%8B "HTML5のSVG要素では名前空間宣言が省略できる - 週刊SVG")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Top | Diff of HTMLs
[diffofhtmls.herokuapp.com/](https://diffofhtmls.herokuapp.com/ "Top | Diff of HTMLs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">HTML</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

WHATWGとW3C HTMLのdiffを見ることができるツール

----

## Async Redux Actions With RxJS - React Rally 2016
[www.slideshare.net/benlesh1/async-redux-actions-with-rxjs-react-rally-2016](http://www.slideshare.net/benlesh1/async-redux-actions-with-rxjs-react-rally-2016 "Async Redux Actions With RxJS - React Rally 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">Rx</span> <span class="jser-tag">スライド</span></p>

_redux-observable_についてのスライド。
Reduxにおいて非同期処理を行う場合に、連続性やCancelなどを表現しやすいRxJSを使うという話

- [redux-observable/redux-observable: RxJS middleware for action side effects in Redux using &amp;#34;Epics&amp;#34;](https://github.com/redux-observable/redux-observable "redux-observable/redux-observable: RxJS middleware for action side effects in Redux using &amp;#34;Epics&amp;#34;")

----

## camwiegert/in-view: Get notified when a DOM element enters or exits the viewport.
[github.com/camwiegert/in-view](https://github.com/camwiegert/in-view "camwiegert/in-view: Get notified when a DOM element enters or exits the viewport.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

ある要素がviewportに含まれているかを判定して、入った時と出た時のハンドラを書けるライブラリ。
将来的にIntersectionObserverへも対応予定

----

## dollarshaveclub/postmate: A powerful, simple, promise-based postMessage library 📭 📨 📬 📫 🚚
[github.com/dollarshaveclub/postmate](https://github.com/dollarshaveclub/postmate "dollarshaveclub/postmate: A powerful, simple, promise-based postMessage library 📭 📨 📬 📫 🚚")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

PromiseベースのpostMessageライブラリ

----

## sdkennedy/babel-preset-target: Babel preset that allows for target environments to be specified along with plugins and presets. If all environments have native support for a given plugin, it will be skipped.
[github.com/sdkennedy/babel-preset-target](https://github.com/sdkennedy/babel-preset-target "sdkennedy/babel-preset-target: Babel preset that allows for target environments to be specified along with plugins and presets. If all environments have native support for a given plugin, it will be skipped.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

サポートするブラウザを指定することで、対応したBabel pluginでの変換をしてくれるbabel preset

----
<h1 class="site-genre">書籍関係</h1>

----

## Angular 2 Router by Victor Savkin [Leanpub PDF/iPad/Kindle]
[leanpub.com/router](https://leanpub.com/router "Angular 2 Router by Victor Savkin \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

AngularJS 2のRouterについての電子書籍

----
