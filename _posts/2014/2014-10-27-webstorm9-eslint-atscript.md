---
title: "2014-10-27のJS: WebStorm 9、ESLint 0.9.0、AngularJS 2.0とAtScript"
author: azu
layout: post
date : 2014-10-27T19:41
category: JSer
tags:
    - WebStorm
    - IDE
    - Lint
    - Tools
    - TypeScript
    - AngularJS

---

JSer.info #198 - [WebStorm 9](http://blog.jetbrains.com/webstorm/2014/10/webstorm-9-released-meteor-support-react-and-jsx-gulp-integration-and-more/ "WebStorm 9")がリリースされました。

新たに[Meteor](http://blog.jetbrains.com/webstorm/2014/09/meteor-support-in-webstorm-9/ "Meteor")、[React](http://facebook.github.io/react/ "React")、[Polymer](https://www.polymer-project.org/ "Polymer")、[gulp](http://gulpjs.com/ "gulp")のサポート等が追加されています。

また、ファイルの種類毎にタブ/スペースのインデント等を指定出来る[EditorConfig](http://editorconfig.org/ "EditorConfig")や[ESLint](http://eslint.org/ "ESLint")、[JSCS](https://github.com/jscs-dev/node-jscs "JSCS")等のサポートもされています。

他にも色々機能追加されていて、詳しくは以下で解説されています。

- [WebStorm 9 released: Meteor support, React and JSX, Gulp integration, and more | JetBrains WebStorm Blog](http://blog.jetbrains.com/webstorm/2014/10/webstorm-9-released-meteor-support-react-and-jsx-gulp-integration-and-more/ "WebStorm 9 released: Meteor support, React and JSX, Gulp integration, and more | JetBrains WebStorm Blog")
- [What&#39;s new in WebStorm 9](https://www.jetbrains.com/webstorm/whatsnew/ "What&#39;s new in WebStorm 9")

----

PluginでLintのルールを拡張可能な[ESLint 0.9.0](http://eslint.org/blog/2014/10/eslint-0.9.0-released/ "ESLint 0.9.0")がリリースされました。

Pluginの使用がstableとなり、ESLintの[Governance Model](http://eslint.org/docs/developer-guide/governance.html "Governance")やContributors向けの[Contributingドキュメント](http://eslint.org/docs/developer-guide/contributing.html "Contributing")が整備されています。
(具体的にはCLIへのサイン、コミットメッセージの書式などルールが書かれています)

今後はES6サポートやよりpluginを扱いやすくする仕組みなどが[Upcoming](https://github.com/eslint/eslint/wiki/Release-goals#upcoming "Upcoming")にあげられています。(ES6サポートはパーサ側がサポートしてないとできないので、それを待っている感じだと思います)

----

[ng-europe](http://ngeurope.org/ "ng-europe - The first AngularJS European conference in Paris, France.")にてAngularJS 2.0について色々な発表がありました。(またライブラリ自体は公開されてないですが)

- [AngularJS カンファレンス（ng-europe 2014）のスライドまとめ - AngularJS Ninja](http://angularjsninja.com/blog/2014/10/24/slides-at-ngeurope-2014/ "AngularJS カンファレンス（ng-europe 2014）のスライドまとめ - AngularJS Ninja")

以前2.0の構想について書かれた[AngularJS: AngularJS 2.0](https://blog.angularjs.org/2014/03/angular-20.html "AngularJS: AngularJS 2.0")でも出てきていましたが、AngularJS 2.0ではAtScriptというES6にAnnotationsを加えたもので作られていることが[Keynote: AtScript](https://docs.google.com/presentation/d/1hr2IM-8G-0RzpB-WY8pLHvxqNggKPzUO0KvEv1IKPws/edit#slide=id.p "Keynote: AtScript - Google スライド")で語られています。

このAtScript(ES6+Annotaions)は[traceur-compiler 入門](http://yosuke-furukawa.hatenablog.com/entry/2014/07/31/093041 "traceur-compiler 入門 - from scratch")で書かれているように[Traceur](https://github.com/google/traceur-compiler "Traceur")によってTranspileして使うようになっています。

またソース自体が公開されてないのであまり深い追いしてもしょうがないですが、
[ES6+カジュアルトーク](http://connpass.com/event/9113/ "ES6+カジュアルトーク")で発表する[スライド](http://azu.github.io/slide/es6talks/ "明日には使えなくなるES7トーク")にもう少し詳しくまとめてありますので、興味がある人はそちらを見ておくといいのかもしれません。

- [slide/es7.md at gh-pages · azu/slide](https://github.com/azu/slide/blob/gh-pages/es6talks/es7.md "slide/es7.md at gh-pages · azu/slide")

----

## お知らせ

今週末の土曜日に[JSer.info 200回記念イベント](http://connpass.com/event/9067/ "JSer.info 200回記念イベント")を行います。

[JSer.info 200回記念イベントの質問](http://www.google.com/moderator/?hl=ja#16/e=213da7 "JSer.info 200回記念イベントの質問")等まだ募集しているので、`#jserinfo` をつけて適当つぶやくとかでも募集しています。

<a href="https://twitter.com/intent/tweet?button_hashtag=jserinfo&text=%E8%81%9E%E3%81%8D%E3%81%9F%E3%81%84%E3%81%93%E3%81%A8%3A%20" class="twitter-hashtag-button">Tweet #jserinfo</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>


----

<h1 class="site-genre">ヘッドライン</h1>

----

## WebStorm 9 released: Meteor support, React and JSX, Gulp integration, and more | JetBrains WebStorm Blog
[blog.jetbrains.com/webstorm/2014/10/webstorm-9-released-meteor-support-react-and-jsx-gulp-integration-and-more/](http://blog.jetbrains.com/webstorm/2014/10/webstorm-9-released-meteor-support-react-and-jsx-gulp-integration-and-more/ "WebStorm 9 released: Meteor support, React and JSX, Gulp integration, and more | JetBrains WebStorm Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebStorm</span> <span class="jser-tag">ReleaseNote</span></p>

WebStorm 9リリース。

主に以下の様な機能追加等が中心です。

- Meteor、React/JSX、Polymerのサポート
- PhoneGap、Gulp統合
- spy-js/LiveEditがNode.jsアプリケーションに対応
- ESLint/JSCS/EditorConfigのサポート
- [What&#x27;s new in WebStorm 9](https://www.jetbrains.com/webstorm/whatsnew/ "What&#x27;s new in WebStorm 9")

----

## Release Custom Driver Support · mozilla/localForage
[github.com/mozilla/localForage/releases/tag/1.1.1](https://github.com/mozilla/localForage/releases/tag/1.1.1 "Release Custom Driver Support · mozilla/localForage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

localForage 1.1.1リリース。

`defineDriver()`メソッドが追加され、任意のCustom Driverを作成して適応出来るようになった。

任意のストレージをバックエンドに実装出来る

----

## mocha/History.md at 2.0.0 · mochajs/mocha
[github.com/mochajs/mocha/blob/2.0.0/History.md](https://github.com/mochajs/mocha/blob/2.0.0/History.md "mocha/History.md at 2.0.0 · mochajs/mocha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

mocha 2.0.0リリース。

リポジトリのオーナーがmochajsになった。

Node.js 0.4と0.6のサポート終了

----

## Node v0.10.33 (Stable)
[blog.nodejs.org/2014/10/23/node-v0-10-33-stable/](http://blog.nodejs.org/2014/10/23/node-v0-10-33-stable/ "Node v0.10.33 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">セキュリティ</span></p>

Node v0.10.33リリース

POODLE対策

----

## ESLint 0.9.0 released - ESLint
[eslint.org/blog/2014/10/eslint-0.9.0-released/](http://eslint.org/blog/2014/10/eslint-0.9.0-released/ "ESLint 0.9.0 released - ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 0.9.0リリース。

pluginはstableに、 Governance Modelを追加、ルールの追加や修正など

----

## CodeMirror release 4.7.0 - Google グループ
[groups.google.com/forum/#!msg/codemirror/Ry_Mx8BGcQU/NFqd0odfYHQJ](https://groups.google.com/forum/#!msg/codemirror/Ry_Mx8BGcQU/NFqd0odfYHQJ "CodeMirror release 4.7.0 - Google グループ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

CodeMirror 4.7.0リリース

CoffeeScriptやScala、PHP等のmodeを改善。Textileのサポート、ロゴが新しくなった

----
<h1 class="site-genre">アーティクル</h1>

----

## TypeScript and the Road to 2.0 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2014/10/22/typescript-and-the-road-to-2-0.aspx](http://blogs.msdn.com/b/typescript/archive/2014/10/22/typescript-and-the-road-to-2-0.aspx "TypeScript and the Road to 2.0 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2.0のロードマップ。

1.4で union types のサポート、1.5からES6の親和性の向上などを目指す。

またFacebookのFlowやAngular2.0で使われてるAtScriptのチームと一緒にType AnnotaionsをECMAScriptへの提案を進めていく方針

----

## Community Round-up #23 | React
[facebook.github.io/react/blog/2014/10/17/community-roundup-23.html](http://facebook.github.io/react/blog/2014/10/17/community-roundup-23.html "Community Round-up #23 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span></p>

Fluxアーキテクチャのサンプルや解説やライブラリ等のまとめ

----

## 写真サービス機能のブラウザ内実装 | 株式会社サイバーエージェント
[www.cyberagent.co.jp/recruit/techreport/report/id=8548](https://www.cyberagent.co.jp/recruit/techreport/report/id=8548 "写真サービス機能のブラウザ内実装 | 株式会社サイバーエージェント")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">Android</span> <span class="jser-tag">画像</span> <span class="jser-tag">canvas</span> <span class="jser-tag">browser</span></p>

iOS6.0~、Android4.0~に対応した画像を扱う時に起きる問題と対処について。

iOS6のファイルサイズの問題、AndroidのtoDataURLがJPEGをサポートしてない問題、フィルタ処理やリサイズについてなどハマりどころをまとめられている

----

## スマートフォンWebのフロントエンドを高速化する取り組み - クックパッド開発者ブログ
[techlife.cookpad.com/entry/2014/10/23/095814](http://techlife.cookpad.com/entry/2014/10/23/095814 "スマートフォンWebのフロントエンドを高速化する取り組み - クックパッド開発者ブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Android</span> <span class="jser-tag">webkit</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">mobile</span></p>

モバイル向けの一部ページをシングルページアプリケーションとして作るのに適した条件やメリットについて書かれている。

クライアントサイドでの画像リサイズとアップロードやTouchイベント対応などについて

----

## ECMAScript 6 returns JavaScript to original intent | InfoWorld
[www.infoworld.com/article/2837425/javascript/ecmascript-6-returns-javascript-to-original-intent.html](http://www.infoworld.com/article/2837425/javascript/ecmascript-6-returns-javascript-to-original-intent.html "ECMAScript 6 returns JavaScript to original intent | InfoWorld")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">インタビュー</span></p>

ES6,7についてJafar Husainさん(Async Generatorの人)へのインタビュー。

何故ES6,7を同時進行しているのか、Async functionとAsync Generatorについて、大きなアプリケーションと型の必要性について。

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## AngularJS カンファレンス（ng-europe 2014）のスライドまとめ - AngularJS Ninja
[angularjsninja.com/blog/2014/10/24/slides-at-ngeurope-2014/](http://angularjsninja.com/blog/2014/10/24/slides-at-ngeurope-2014/ "AngularJS カンファレンス（ng-europe 2014）のスライドまとめ - AngularJS Ninja")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">スライド</span> <span class="jser-tag">まとめ</span></p>

ng-europeのスライドまとめ

- [ng-europe - The first AngularJS European conference in Paris, France.](http://ngeurope.org/ "ng-europe - The first AngularJS European conference in Paris, France.")

----

## Keynote: AtScript - Google スライド
[docs.google.com/presentation/d/1hr2IM-8G-0RzpB-WY8pLHvxqNggKPzUO0KvEv1IKPws/present#slide=id.p](https://docs.google.com/presentation/d/1hr2IM-8G-0RzpB-WY8pLHvxqNggKPzUO0KvEv1IKPws/present#slide=id.p "Keynote: AtScript - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">スライド</span></p>

AtScriptについてのスライド。

AtScriptは新しい言語ではなくES6にTypesとAnnotationsとIntrospectionを追加したもの。

AtScriptのロードマップについても書かれている。

----

## AtScript Primer - Google ドキュメント
[docs.google.com/document/d/11YUzC-1d0V1-Q3V0fQ7KSit97HnZoKVygDxpWzEYW0U/preview#](https://docs.google.com/document/d/11YUzC-1d0V1-Q3V0fQ7KSit97HnZoKVygDxpWzEYW0U/preview# "AtScript Primer - Google ドキュメント")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span> <span class="jser-tag">spec</span></p>

Angular2.0で使われているES6に型定義を拡張したもの。

assert.jsを使ったES6 validなものへTraceurで変換が出来る。 
またDI等に利用できるMetadata Annotationsがある。

こちらもECMAScript標準への提案を行っていく方針。

- [Assert.js](http://angular.github.io/assert/ "Assert.js")
- [The Extensible Web Manifesto](http://extensiblewebmanifesto.org/ "The Extensible Web Manifesto")

----

## ES6 &amp; Traceur
[arv.github.io/ngeurope/#/](http://arv.github.io/ngeurope/#/ "ES6 &amp; Traceur")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

ES6の機能についてのスライド。

機能ごとにいつ、どんな時に使うべきかも書かれている。

またTraceurがどのように動いているかやAngularで使われてるAtScriptの拡張について

----

## Yahoo! JAPAN Creative Blog — 「SCRIPTY#1 」の資料を公開します #scripty01
[yj-creative.tumblr.com/post/100569738942/scripty-1-scripty01](http://yj-creative.tumblr.com/post/100569738942/scripty-1-scripty01 "Yahoo! JAPAN Creative Blog — 「SCRIPTY#1 」の資料を公開します #scripty01")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">イベント</span></p>

SCRIPTYのスライドまとめ。

CSS/BEM、Backbone/Marionette、Angular/Three.js、Polymer、Yahoo!ニュースのブラウザサポート、grunt、ライブコーディング、アクセシビリティなど

----

## In the DOM, no one will hear you scream
[www.slideshare.net/x00mario/in-the-dom-no-one-will-hear-you-scream](http://www.slideshare.net/x00mario/in-the-dom-no-one-will-hear-you-scream "In the DOM, no one will hear you scream")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">XSS</span> <span class="jser-tag">スライド</span></p>

DOM Based XSSとjQueryによるXSSについてのスライド。

DOM Level、文字列からコードとして実行するメソッド一覧、上書きによる破壊、DOMPurifyによる防止について

- [cure53/DOMPurify](https://github.com/cure53/DOMPurify "cure53/DOMPurify")
- [cure53/jPurify](https://github.com/cure53/jPurify "cure53/jPurify")

----

## christianalfoni WebApp Enthusiast
[christianalfoni.github.io/javascript/2014/08/20/react-js-and-flux.html](http://christianalfoni.github.io/javascript/2014/08/20/react-js-and-flux.html "christianalfoni WebApp Enthusiast")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span></p>

Backbone/Angular/Flux+Reactでそれぞれ実装した場合の違いを見ながら、Fluxアーキテクチャの特徴について紹介。 



[Ractive.js](<a href='http://www.ractivejs.org/'>http://www.ractivejs.org/</a> &quot;Ractive.js&quot;)と[vue.js](<a href='http://vuejs.org/'>http://vuejs.org/</a> &quot;vue.js&quot;)とFluxアーキテクチャを使って同様のサンプルを作ってあります。

- [azu/Flux-Checkbox-Example](https://github.com/azu/Flux-Checkbox-Example "azu/Flux-Checkbox-Example")

----

## ブラウザのパフォーマンスを限界まで高める HTMLコーディングの考え方
[ja.slideshare.net/kawada_hiroshi/html-40678123](http://ja.slideshare.net/kawada_hiroshi/html-40678123 "ブラウザのパフォーマンスを限界まで高める HTMLコーディングの考え方")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">スライド</span></p>

ブラウザのパフォーマンス最適化の戦略についてのスライド。

極端な例外を除いたパーセンタイルを見てパフォーマンスを調整。

レンダリングの開始時間、Speed Index、Critical Redering Pathを目安にする。

標準化やNavigation Timingについて

- [Google I/O 2014 - Mobile Web performance auditing](https://www.google.com/events/io/schedule/session/c8300366-03ed-e311-903f-00155d5066d7 "Google I/O 2014 - Mobile Web performance auditing")

----
<h1 class="site-genre">サイト、サービス</h1>

----

## AurelioDeRosa/HTML5-API-demos
[github.com/AurelioDeRosa/HTML5-API-demos](https://github.com/AurelioDeRosa/HTML5-API-demos "AurelioDeRosa/HTML5-API-demos")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">サンプル</span></p>

Battery Status API等の広義のHTML5 APIについての仕様とサンプルと記事をまとめたリポジトリ

----

## JS Compatibility Checker
[jscc.info/](http://jscc.info/ "JS Compatibility Checker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ブラウザ間で互換性のあるコードかをチェックするツール。

ECMAScript5 APIやcaniuseのデータを元にチェックする

----

## Content Security Policy Playground
[www.cspplayground.com/](http://www.cspplayground.com/ "Content Security Policy Playground")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">webservice</span> <span class="jser-tag">まとめ</span></p>

CSPについて実際に任意の設定を適応して試しながら学べるサイト。

CSP Policyのバリデーションや関連リソースについてもまとめられている

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## wooorm/mdast
[github.com/wooorm/mdast](https://github.com/wooorm/mdast "wooorm/mdast")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">node.js</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScriptのMarkdownパーサライブラリ。パースした結果をJSON的なASTとして出力する。

gfmやpandoc風の解釈も対応していて、Parser API ライクなドキュメントもあって良さそう

----

## Khan/structuredjs
[github.com/Khan/structuredjs](https://github.com/Khan/structuredjs "Khan/structuredjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScriptのコードをプレースホルダー的に書いておいて、入力されたコードがプレースホルダーと一致するかをチェックできるライブラリ。

不一致の場合のエラー情報等も定義でき、学習サイト等で使われる感じ

----

## dameleon/paw.js
[github.com/dameleon/paw.js](https://github.com/dameleon/paw.js "dameleon/paw.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">mobile</span> <span class="jser-tag">library</span></p>

TouchEventやPointerEventをハンドリングして、シンプルに扱える`tap`イベント等のカスタムイベントを発行してくれるライブラリ。

- [Paw.jsというのを書いたのと今から始めるマルチタッチイベント処理 - damelog](http://dameleon.hatenablog.com/entry/2014/10/21/171448 "Paw.jsというのを書いたのと今から始めるマルチタッチイベント処理 - damelog")

----

## hughsk/district
[github.com/hughsk/district](https://github.com/hughsk/district "hughsk/district")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

指定したディレクトリをnode_modules以下にエイリアスを貼るツール。

モジュールを特定のディレクトリに名前空間的にまとめることができる

----
