---
title: "2015-08-03のJS: ESLint 1.0.0、JSCS 2.0.0、esprima 2.5.0"
author: azu
layout: post
date : 2015-08-03T09:13
category: JSer
tags:
    - Lint
    - Tool
    - AST
    - ES6
    - JavaScript

---

JSer.info #239 - JavaScript Lintツールである[ESLint](http://eslint.org/) 1.0.0がリリースされました。

`--reset`のオプションがデフォルトとなり[全てのルールがデフォルトOFF](http://eslint.org/docs/user-guide/migrating-to-1.0.0#all-rules-off-by-default "All Rules Off by Default")となりました。今までのデフォルトは `"eslint:recommended"` という設定を使うことでできるようです。

```
{
    "extends": "eslint:recommended"
}
```

- [ESLint 1.0.0 released - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2015/07/eslint-1.0.0-released/ "ESLint 1.0.0 released - ESLint - Pluggable JavaScript linter")
- [Migrating to v1.0.0](http://eslint.org/docs/user-guide/migrating-to-1.0.0 "Migrating to v1.0.0")


----

JavaScriptのスタイルチェックツールである[JSCS](https://github.com/jscs-dev/node-jscs) 2.0.0がリリースされました。

- [Release 2.0.0 · jscs-dev/node-jscs](https://github.com/jscs-dev/node-jscs/releases/tag/v2.0.0 "Release 2.0.0 · jscs-dev/node-jscs")

`esnext`というオプションでES6(とJSX)のサポート、スタイルの自動修正機能を改善、ES6関連のルールの追加、`//`コメントでチェックを無効化などがサポートされました。

```
if (x) y(); // jscs:ignore requireCurlyBraces
```

----

JavaScriptのパーサライブラリである[esprima](http://esprima.org/ "Esprima") 2.5.0がリリースされました。

- [esprima/ChangeLog at 2.5.0 · jquery/esprima](https://github.com/jquery/esprima/blob/2.5.0/ChangeLog "esprima/ChangeLog at 2.5.0 · jquery/esprima")

2.5.0で[ES6の機能をフルサポート](https://github.com/jquery/esprima/issues/1099)したため、ES6のコードを全てパースできるようになりました。

先ほど出てきた[JSCS](https://github.com/jscs-dev/node-jscs)はesprimaを、[ESLint](http://eslint.org/)はesprimaをforkした[Espree](https://github.com/eslint/espree "Espree")をパーサとして利用しています。

また[@hzoo](https://github.com/hzoo)さんによりどちらも[babel-jscs](https://github.com/jscs-dev/babel-jscs "babel-jscs")と[babel-eslint](https://github.com/babel/babel-eslint "babel-eslint")という形で、BabelがサポートするexperimentalなES.nextのコードもサポートしています。

このbabel-*の仕組みとしては、Babelが内蔵するacornベースのパーサを使いパースした結果を、esprima互換のAST/CSTに変換することで、ES.nextのコードもJSCSとESLintで使えるようにしています。

JavaScriptのASTについては[ESTree](https://github.com/estree/estree "ESTree")というデファクトスタンダードがありますが、CST(Concrete Syntax Tree)についてはまだ標準的なものはありません。

- [Abstract vs. Concrete Syntax Trees - Eli Bendersky's website](http://eli.thegreenplace.net/2009/02/16/abstract-vs-concrete-syntax-trees/ "Abstract vs. Concrete Syntax Trees - Eli Bendersky&#39;s website")

ESLint、JSCSどちらも、ESTreeのAST仕様では定義されていない"スペース"や";"(セミコロン)といった文字列などもチェックに利用しています。

JSCSでは[CST](https://github.com/mdevils/cst "CST")というConcrete Syntax Treeの実装を作り使うようになっていて、ESLintもesprima由来のtokenを利用しています。

長くなりましたが、何が書きたかったかというと土台となるesprimaなどのJavaScriptパーサはES6に対応し、それらを使うESLintやJSCSなどもES6へ対応したため、こういったツールがまとめて一段落したように見えます。

そのため、次はCSTなどよりツールを便利するために一歩踏み出し始めた感じなので、この辺はまだまだ色々な進化がありそうな気がします。

[#19 ES7 | mozaic.fm](http://mozaic.fm/post/125673651143/19-es7 "#19 ES7 | mozaic.fm")でもこういったASTツールチェインの話をしているので聞いてみるといいかもしれません。

-----

## お知らせ

[Realtime JSer.info](http://realtime.jser.info/ "Realtime JSer.info") β始めました。
JSer.infoは週一ですが、[realtime.jser.info](realtime.jser.info/)は名前の通りその場その場で更新されます。

何かご意見あったら以下のIssueとかに下さい。
(hugoで作り直すPRとかも募集してます)

- [realtime.jser.info · Issue #47 · jser/jser.info](https://github.com/jser/jser.info/issues/47 "realtime.jser.info · Issue #47 · jser/jser.info")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint 1.0.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/07/eslint-1.0.0-released](http://eslint.org/blog/2015/07/eslint-1.0.0-released "ESLint 1.0.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 1.0.0リリース。
ES6の対応改善、`--reset`がデフォルトの挙動となり設定なしではルールを持たないようになった。
"eslint:recommended"の設定を継承することで今までと同じデフォルト設定が得られる。

- [Documentation - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/user-guide/migrating-to-1.0.0 "Documentation - ESLint - Pluggable JavaScript linter")
- [ESLint 1.0.0新ルールまとめ - Qiita](http://qiita.com/armorik83/items/228b97bee25aa33c9850 "ESLint 1.0.0新ルールまとめ - Qiita")

----

## Release 2.0.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v2.0.0](https://github.com/jscs-dev/node-jscs/releases/tag/v2.0.0 "Release 2.0.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptスタイルチェックツールjscs 2.0.0リリース。
ES.nextをサポートする`--esnext`フラグの追加、CSTを実装しAutofixingに利用するように、ES6に対応したルールの追加、コメントによるルールの無効化のサポートなど

- [mdevils/cst](https://github.com/mdevils/cst "mdevils/cst")

----


## Release 2.5.0 · jquery/esprima
[github.com/jquery/esprima/releases/tag/2.5.0](https://github.com/jquery/esprima/releases/tag/2.5.0 "Release 2.5.0 · jquery/esprima")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

esprima 2.5.0リリース。
ES6の全ての機能をパースできるように

- [esprima/ChangeLog at 2.5.0 · jquery/esprima](https://github.com/jquery/esprima/blob/2.5.0/ChangeLog "esprima/ChangeLog at 2.5.0 · jquery/esprima")
- [ES6 Main Tracking Issue · Issue #1099 · jquery/esprima](https://github.com/jquery/esprima/issues/1099 "ES6 Main Tracking Issue · Issue #1099 · jquery/esprima")
- [Esprima Meeting Agenda - Google ドキュメント](https://docs.google.com/document/d/1l02VT94tdphwUUZfPJorRYOY0Q_v41R_TyYhKayiP9M/edit "Esprima Meeting Agenda - Google ドキュメント")

----

## Flow | Version 0.14.0
[flowtype.org/blog/2015/07/29/Version-0.14.0.html](http://flowtype.org/blog/2015/07/29/Version-0.14.0.html "Flow | Version 0.14.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.14.0リリース。
型指定してないパラメータを`any`と扱うように、Flowコメント構文をブロックコメント内で使えるようになるなど

----

## | Intern 3 is here! | Blog | SitePen
[www.sitepen.com/blog/2015/07/30/intern-3-is-here/](https://www.sitepen.com/blog/2015/07/30/intern-3-is-here/ "| Intern 3 is here! | Blog | SitePen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScriptテストフレームワークのIntern 3リリース。
IE8のサポート終了、ES6の対応改善、d.tsを追加、QUnit互換のサポートなど

- [Release 3.0.0 · theintern/intern](https://github.com/theintern/intern/releases/3.0.0 "Release 3.0.0 · theintern/intern")

----
<h1 class="site-genre">アーティクル</h1>

----

## Linting JavaScript in 2015
[blog.lauritz.me/linting-javascript-in-2015/](http://blog.lauritz.me/linting-javascript-in-2015/ "Linting JavaScript in 2015")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ESLintを使ってJavaScriptのコードをLintする方法についての紹介

----

## New regular expression features in ECMAScript 6
[www.2ality.com/2015/07/regexp-es6.html](http://www.2ality.com/2015/07/regexp-es6.html "New regular expression features in ECMAScript 6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">正規表現</span></p>

ES6で追加された正規表現の要素について。
sticky flag、Unicode flag、`\u{...}`によるEscape sequencesについて

----

## Flux inside Web Workers — Medium
[medium.com/@nsisodiya/flux-inside-web-workers-cc51fb463882](https://medium.com/@nsisodiya/flux-inside-web-workers-cc51fb463882 "Flux inside Web Workers — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">DOM</span></p>

DOM lessな実装をしてればWeb Workerでも動かせる。
FluxをベースにStore->View、View->ActionをpostMessageでやりとりすることで、View以外をWeb Worker上で処理できるという話

----

## Isomorphic Architecture を実装してるときの細かいアレコレ ::ハブろぐ
[havelog.ayumusato.com/develop/javascript/e682-universal_architecture_tips.html](http://havelog.ayumusato.com/develop/javascript/e682-universal_architecture_tips.html "Isomorphic Architecture を実装してるときの細かいアレコレ ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">isomorphic</span> <span class="jser-tag">JavaScript</span></p>

シングルページアプリケーションとサーバサイドレンダリングを扱う際に起こる問題と解決策について。
設定の共有をするか、UAの評価、React Componentの`<head>`への適応方法、ライフサイクルの管理などについて

----

## Non-blocking Asynchronous JSON.parse Using The Fetch API
[azimi.me/2015/07/30/non-blocking-async-json-parse.html](http://azimi.me/2015/07/30/non-blocking-async-json-parse.html "Non-blocking Asynchronous JSON.parse Using The Fetch API")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span></p>

Fetch APIで提供されてる`Response`オブジェクトを使い`(new Response(string)).json()`を非同期JSON.parseとして利用する方法について

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Learning RiotJS - Video Tutorial Playlist @eggheadio
[egghead.io/playlists/learning-riotjs](https://egghead.io/playlists/learning-riotjs "Learning RiotJS - Video Tutorial Playlist @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">動画</span> <span class="jser-tag">library</span></p>

Riot.JSについてのスクリーンキャストシリーズ

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Mithril
[mithril-ja.js.org/](http://mithril-ja.js.org/ "Mithril")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">翻訳</span></p>

Mithrilの日本語訳ページ

----

## WebRTCセキュリティレポート · A Study of WebRTC Security
[webrtc-security.github.io/report_ja/](http://webrtc-security.github.io/report_ja/ "WebRTCセキュリティレポート · A Study of WebRTC Security")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebRTC</span> <span class="jser-tag">セキュリティ</span></p>

WebRTCのセキュリティについての文章。
WebRTCがどういう仕組みで動いているのか、信頼性が何をベースとして構築されているか、暗号のメカニズム、安全に扱う方法についてなど

- [WebRTC入門+最新動向](http://www.slideshare.net/rotsuya/intro-webrtcppt "WebRTC入門+最新動向")

----
<h1 class="site-genre">書籍関係</h1>

----

## Front-End Architecture - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920040156.do](http://shop.oreilly.com/product/0636920040156.do "Front-End Architecture - O&#x27;Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2015年12月発売
CSSプリプロセス、開発ワークフローツール、JavaScriptのライブラリなどフロントエンドについての書籍

----
