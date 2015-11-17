---
title: "2015-11-16のJS: ECMAScript 2016(ES7)って何、WindowsでのNode.js入門"
author: azu
layout: post
date : 2015-11-16T22:49
category: JSer
tags:
    - ECMAScript
    - ES.next
    - MS
    - Node.js
  
---


JSer.info #253 - [What’s in ECMAScript 2016 (ES7)?](http://www.2ality.com/2015/11/tc39-process.html "What’s in ECMAScript 2016 (ES7)?")という記事では、最近よく見るECMAScript 2016 (ES7)というのは実際には何の事を言ってるのかについて書かれています。

TC39とは何か?、今後(ES7から)は機能ごとのProposalとなってること、どのように策定が進んでいくかといったことについて書かれています。

以前自分が書いた[Introduction | ECMAScriptとは何か？](http://azu.github.io/slide-what-is-ecmascript/ "Introduction | ECMAScriptとは何か？")や[記事](http://efcl.info/2015/10/18/ecmascript-paper/)と扱ってる内容はかなり近いです。

合わせてES6のエディタであるAllenさんのインタビューも読むと、今後どのようになっていくかが分かりやすいです。

- [ECMAScript 2015はなぜ策定まで時間がかかったか？ 仕様策定のリーダー、アレン・ワーフスブラック氏に聞く：CodeZine（コードジン）](http://codezine.jp/article/detail/9071 "ECMAScript 2015はなぜ策定まで時間がかかったか？ 仕様策定のリーダー、アレン・ワーフスブラック氏に聞く：CodeZine（コードジン）")

上記の記事と同時期に[ES6 in Practice](http://www.slideshare.net/teppeis/es6-in-practice "ES6 in Practice")というスライドが公開されています。
こちらのスライドでも同様に仕様策定のプロセスや現状のES6 Modulesの問題点についてなどが書かれています。
ES6 Modulesは構文とセマンティクスのみが仕様化されていて、どのようにパスを解決してどうやって読み込むのかはまだ安定した仕様はありません。
そのため、BabelなどのTranspilerはある種の独自解釈をしてES6 Modulesを扱っています。
そこから生まれるCommonJSとの相互運用性の問題などについて問題提起がされています。

どのスライドも[ES7 XXX言うな問題](http://www.slideshare.net/teppeis/es6-in-practice/22)について触れています。
"ES7 Decorator"というようにProposal段階の機能が、まるでES7の機能であるような言い方は誤解を生むことがあります。
そのため、仕様として提案中の機能であることやStage 1の機能であることなどもう少し正確な言い回しをしようという話となっています。

----

[Microsoft/nodejs-guidelines](https://github.com/Microsoft/nodejs-guidelines "Microsoft/nodejs-guidelines")というリポジトリでMicrosoftによるNode.js入門ガイドラインが公開されています。

Windows上でのNode.jsの利用方法について、npmの使い方、開発ツールやエディタなどについて書かれています。


-----

## お知らせ

ウェブ上で記事の方を見ると分かりますが、それぞれの記事に"▼関連記事の表示"というボタンが増えていると思います。

これは、その記事に関連する記事一覧を[jser-stat](https://github.com/jser/stat-js "jser-stat")を使って出しています。

![関連記事](https://monosnap.com/file/svl7DJLuVANCIuhLpd0Z54ioBIypK1.png)

取得から探索まで全部ブラウザ上で処理してるので、そこまで正確というものではないですが、気になる記事の関連記事を探してみると面白いかもしれません。

## お知らせ2

以前お知らせしていた[JSer.info 5周年イベント](https://github.com/jser/jser.info/issues/54 "JSer.info 5周年イベント")ですが、2016年1月16日(土) 午後あたりに開催する予定となりました。

まだ、何をするかが決まっていないので、興味がある人は以下のIssueにコメントを書いて頂けると参考にします。

- [JSer.info 5周年イベント · Issue #54 · jser/jser.info](https://github.com/jser/jser.info/issues/54 "JSer.info 5周年イベント · Issue #54 · jser/jser.info")


----
<h1 class="site-genre">ヘッドライン</h1>

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#614](https://github.com/babel/babel/blob/master/CHANGELOG.md#614 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.1.4リリース。
`babel/register`が`babel-register`というパッケージに分離、ブラウザ向けの`babel-browser`パッケージの追加、バグ修正など

----
<h1 class="site-genre">アーティクル</h1>

----

## What’s in ECMAScript 2016 (ES7)?
[www.2ality.com/2015/11/tc39-process.html](http://www.2ality.com/2015/11/tc39-process.html "What’s in ECMAScript 2016 (ES7)?")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

ECMAScriptに関する用語解説やES.nextにおける策定プロセスの解説。
また“ES7 features”のような紹介は間違っているかもしれないという話や現状の策定状況についてなど

- [Introduction | ECMAScriptとは何か？](http://azu.github.io/slide-what-is-ecmascript/ "Introduction | ECMAScriptとは何か？")

----

## Haskell in ES6: Part 1- casual javascript
[casualjavascript.com/javascript/es6/haskell/native/implementation/2015/11/12/haskell-in-es6-part-1.html](http://casualjavascript.com/javascript/es6/haskell/native/implementation/2015/11/12/haskell-in-es6-part-1.html "Haskell in ES6: Part 1- casual javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

JavaScriptでHaskellの関数を実装していく話

----

## Anatomy of a large Angular application — Medium
[medium.com/@bojzi/anatomy-of-a-large-angular-application-f098e5e36994](https://medium.com/@bojzi/anatomy-of-a-large-angular-application-f098e5e36994 "Anatomy of a large Angular application — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

大きなAngularJSアプリの構造について。
TypeScriptで書いてBrowserifyでビルド、コードの構造のレイヤー分けやデータフローなどの設計について

----

## Microsoft/nodejs-guidelines
[github.com/Microsoft/nodejs-guidelines](https://github.com/Microsoft/nodejs-guidelines "Microsoft/nodejs-guidelines")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">node.js</span> <span class="jser-tag">windows</span> <span class="jser-tag">tutorial</span></p>

Windows向けのNode.js入門的なガイドライン

----

## KeitaMoromizato/js-study-front-test
[github.com/KeitaMoromizato/js-study-front-test](https://github.com/KeitaMoromizato/js-study-front-test "KeitaMoromizato/js-study-front-test")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">tutorial</span></p>

Node.jsでのテストとKarmaなどを使ったブラウザテストの違いや仕組みについて。
実際に試せるサンプルと共に紹介されているので分かりやすい。

- [社内JavaScript勉強会で作ったコンテンツまとめ - Qiita](http://qiita.com/KeitaMoromizato/items/82679e98add1345646c6 "社内JavaScript勉強会で作ったコンテンツまとめ - Qiita")

----

## Kinoma now shipping JavaScript 6th Edition (ES6) support | Kinoma Notes - Blog of Kinoma team
[blog.kinoma.com/2015/10/es6\_support/](http://blog.kinoma.com/2015/10/es6_support/ "Kinoma now shipping JavaScript 6th Edition (ES6) support | Kinoma Notes - Blog of Kinoma team")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

KinomaのIoTデバイス向けのJavaScriptエンジンXS6がES6 Compat tableで96％の実装率を持っているという話

- [ECMAScript 6 compatibility table](http://kangax.github.io/compat-table/es6/ "ECMAScript 6 compatibility table")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ES6 in Practice
[www.slideshare.net/teppeis/es6-in-practice](http://www.slideshare.net/teppeis/es6-in-practice "ES6 in Practice")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">スライド</span></p>

ECMAScriptの策定プロセスやES6 Modulesについてのスライド。
ES6 Modulesのメリット、現状の問題について書かれている。
現状では構文とセマンティクスのみが決定している。
読み込み方などについて、BabelなどのTranspilerは独自の解釈があることについての問題提起

----

## BlinkOn 5 One Pager - Google ドキュメント
[docs.google.com/document/d/1BtfsTBVt7KZekH69dCXK0nOCn-W\_kkv23lqjqTJ\_sYY/edit#heading=h.rx77pwie3tnj](https://docs.google.com/document/d/1BtfsTBVt7KZekH69dCXK0nOCn-W_kkv23lqjqTJ_sYY/edit#heading=h.rx77pwie3tnj "BlinkOn 5 One Pager - Google ドキュメント")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">blink</span> <span class="jser-tag">イベント</span> <span class="jser-tag">まとめ</span></p>

BlinkOn 5のスライドと動画まとめ

----

## Porting C/C++ to Web - Google スライド
[docs.google.com/presentation/d/1liKVavDBbcg0w8izutvVopCWKGu5M7EJPvst1JlpN\_s/present#slide=id.p](https://docs.google.com/presentation/d/1liKVavDBbcg0w8izutvVopCWKGu5M7EJPvst1JlpN_s/present#slide=id.p "Porting C/C++ to Web - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">C言語</span> <span class="jser-tag">C++</span> <span class="jser-tag">スライド</span></p>

ブラウザのプラグイン(ネイティブコード)とJavaScriptについてのスライド。
C/C++をemscriptenで変換する方法やasm.js、wasmについての解説。
またそれぞれの現段階での実行速度について

- [Web Assembly BlinkOn 5 - Google スライド](https://docs.google.com/presentation/d/19gdTwicIb-tkZ1bg8117pKVJ5oLnBbf1FsRUfDuFSQg/present#slide=id.g40421410250356b_1 "Web Assembly BlinkOn 5 - Google スライド")
- [ハイパフォーマンスなWebを実現するasm.js／WebAssemblyとは――Mozillaのルーク・ワグナー氏に聞く：CodeZine（コードジン）](http://codezine.jp/article/detail/9072 "ハイパフォーマンスなWebを実現するasm.js／WebAssemblyとは――Mozillaのルーク・ワグナー氏に聞く：CodeZine（コードジン）")

----

## 鉄腕アニメーション
[people.mozilla.org/~bbirtles/pres/201511-astro-animation/#/title-screen](http://people.mozilla.org/~bbirtles/pres/201511-astro-animation/#/title-screen "鉄腕アニメーション")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">animation</span> <span class="jser-tag">スライド</span></p>

Web Animationについてのスライド

----

## Schedule - View Source
[viewsourceconf.org/schedule/](https://viewsourceconf.org/schedule/ "Schedule - View Source")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">イベント</span> <span class="jser-tag">スライド</span> <span class="jser-tag">まとめ</span></p>

ViewSource Conferenceの動画とスライドまとめ

----

## Jeff Morrison - Flow or how I learned to stop worrying and typecheck my React code - YouTube
[www.youtube.com/watch?v=9U4\_hlnaFEE](https://www.youtube.com/watch?v=9U4_hlnaFEE "Jeff Morrison - Flow or how I learned to stop worrying and typecheck my React code - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">動画</span></p>

ReactとFlowTypeを使った開発についての動画

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jaredreich/notie.js
[github.com/jaredreich/notie.js](https://github.com/jaredreich/notie.js "jaredreich/notie.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

依存がないNotification UIライブラリ。
画面上部に被さる形の通知UI

----

## danvk/source-map-explorer · GitHub
[github.com/danvk/source-map-explorer](https://github.com/danvk/source-map-explorer "danvk/source-map-explorer · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">debug</span></p>

Source Mapから利用情報を可視化してファイルサイズやサイズの割合などを調べるツール

----

## mweststrate/mobservable
[github.com/mweststrate/mobservable](https://github.com/mweststrate/mobservable "mweststrate/mobservable")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

配列やオブジェクトなどをラップして変更監視が出来るライブラリ。
getterとsetterを使い変更を監視するためプロパティの代入による変更を通知出来る

- [Object.observe is dead. Long live Mobservable.observe — Medium](https://medium.com/@mweststrate/object-observe-is-dead-long-live-mobservable-observe-ad96930140c5 "Object.observe is dead. Long live Mobservable.observe — Medium")

----
<h1 class="site-genre">書籍関係</h1>

----

## Client-Side Data Storage - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920043676.do](http://shop.oreilly.com/product/0636920043676.do "Client-Side Data Storage - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016年1月発売
クライアントサイドのストレージについての書籍

----
