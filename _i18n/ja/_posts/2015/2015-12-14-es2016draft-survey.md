---
title: "2015-12-14のJS: ES2016 Draft、JavaScript開発者アンケート、JSer.infoイベント開催予定"
author: azu
layout: post
date : 2015-12-14T19:51
category: JSer
tags:
    - ECMAScript
    - アンケート
    - JSer
    - イベント

---

JSer.info #257 - 次期ECMAScriptの仕様のドラフト版となる[ES2016 Draft 2015-12-10](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20151210 "ES2016 Draft 2015-12-10")がリリースされました。

このドラフト版では新しい機能として`Array.prototype.includes`と`TypedArray.prototype.includes`が追加されています。
この機能は新しく採用されている[TC39 Process](https://tc39.github.io/process-document/ "TC39 Process")に則った方式で追加された初めての機能となります。

`Array#includes`は`Array#contains`として元々ES6で入る予定でしたが、Break the Webだったため延期されていました。

- [Having a non-enumerable Array.prototype.contains may not be web-compatible](https://esdiscuss.org/topic/having-a-non-enumerable-array-prototype-contains-may-not-be-web-compatible)
- [Introducing Break the Web: Array extra methods case // Speaker Deck](https://speakerdeck.com/constellation/introducing-break-the-web-array-extra-methods-case)

ES2016では機能ごとにプロポーザルを公開し、機能ごとに進めていきます。
詳しい策定プロセスやプロポーザルとして公開されているものについては下記を参照してください。

- [Introduction | ECMAScriptとは何か？](http://azu.github.io/slide-what-is-ecmascript/ "Introduction | ECMAScriptとは何か？")
- [tc39/ecma262](https://github.com/tc39/ecma262 "tc39/ecma262")

----

[JavaScript Developer Survey Results](https://ponyfoo.com/articles/javascript-developer-survey-results "JavaScript Developer Survey Results")にてJavaScriptの開発者アンケート結果が公開されています。

毎年12月に[DailyJS](http://dailyjs.com)が行っていたアンケートを継承した形になっているようです。

- [JavaScript Developer Survey 2014: Results](http://dailyjs.com/2014/12/16/1333-javascript-survey-results/ "JavaScript Developer Survey 2014: Results")

アンケート結果を見ていくと、ついに、テストを書くと回答した人の割合が50％を超えています。

![testing](https://i.imgur.com/0C944YL.png)

またLintツールとしてはESLintがJSHintを抜いたり

![linting](https://i.imgur.com/RC8ePwr.png)

利用しているフレームワークではReactが一番使われるようになるなどの変化が起きています。

![framework](https://i.imgur.com/zpSAISK.png)

ES6を使ったことがあるかについてでは8割の人が何らかの形で使ったことがあると回答しています。

![ES6](https://i.imgur.com/hAnbtfN.png)

これは7月にJSer.info上のアンケートデータで、"ES6でコードを書いたことがありますか?"という質問に対して74％がYESと答えていたので、数値的にも結構近いところがあります。

- [2015-07-06のJS: React v0.14 Beta 1、Firefox 39、ES6アンケート結果 - JSer.info](http://jser.info/2015/07/06/react-0.14-firefox39-es6/ "2015-07-06のJS: React v0.14 Beta 1、Firefox 39、ES6アンケート結果 - JSer.info")

最後にES2016で何が来るのか知ってる?という質問に対して半分がYESとなっています。

![ES2016](https://i.imgur.com/DxxOnco.png)

まだ何が入るかは最終決定してないので誰も知らないが解だと思います。
ECMAScriptのプロポーザルに[あった](https://github.com/mindeavor/es-pipeline-operator)からといってその仕様が[入るとは限らない](https://esdiscuss.org/topic/an-update-on-object-observe)ので、策定プロセスについてはプロポーザルを読む前に把握しておくといいかもしれません。

- [What’s in ECMAScript 2016 (ES7)?](http://www.2ality.com/2015/11/tc39-process.html "What’s in ECMAScript 2016 (ES7)?")


----

## お知らせ

[2011年01月16日](http://jser.info/post/2774561807/ "2011年01月16日")にJSer.infoを[開始](http://www.slideshare.net/efcl/javascript-6580879)してから、後ちょっとで丸5年になります。

それを記念してピッタリ五年となる2016年01月16日(土)に[JSer.info 5周年記念イベント](http://jser.connpass.com/event/24202/ "JSer.info 5周年記念イベント - connpass")をやろうと思います!

詳細は以下に書いてありますので、興味がある方はどうぞ。

- [JSer.info 5周年記念イベントを1/16(土)に開催します - JSer.info](http://jser.info/2015/12/14/jser-info-announce-5-years/ "JSer.info 5周年記念イベントを1/16(土)に開催します - JSer.info")

受付開始は**2015年12月16日(水) 21:00**からになります。

- [JSer.info 5周年記念イベント - connpass](http://jser.connpass.com/event/24202/ "JSer.info 5周年記念イベント - connpass")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Node v5.2.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.2.0/](https://nodejs.org/en/blog/release/v5.2.0/ "Node v5.2.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v5.2.0リリース。

----

## Dev.Opera — Opera 34 released
[dev.opera.com/blog/opera-34/](https://dev.opera.com/blog/opera-34/ "Dev.Opera — Opera 34 released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 34(based on Chromium 47)リリース。
`Array.prototype.includes`、rest parameters、`requestIdleCallback`の追加など

----

## Release ES2016 Draft 2015-12-10 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20151210](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20151210 "Release ES2016 Draft 2015-12-10 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2015-12-10リリース。
`Array.prototype.includes`が追加された。
ES2016から採用された仕様策定プロセスに則った形のものとして、初めて追加された新しい機能となる。

- [The TC39 Process](https://tc39.github.io/process-document/ "The TC39 Process")
- [ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScriptの仕様策定に関するカンニングペーパー | Web Scratch")

----
<h1 class="site-genre">アーティクル</h1>

----

## JavaScript Developer Survey Results
[ponyfoo.com/articles/javascript-developer-survey-results](https://ponyfoo.com/articles/javascript-developer-survey-results "JavaScript Developer Survey Results")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">まとめ</span></p>

JavaScript開発者アンケート結果が公開された。毎年DailyJSがやっていたものと同様のもの。
テストを書く人が半数を上回り、フレームワークではReactがもっとも使われるようになり、ES6を全く使ったことのない人は20％以下となるなど

- [JavaScript Developer Survey 2014: Results](http://dailyjs.com/2014/12/16/1333-javascript-survey-results/ "JavaScript Developer Survey 2014: Results")

----

## ESLint のカスタムルールを作ろう! (その1) - Qiita
[qiita.com/mysticatea/items/cc3f648e11368799e66c](http://qiita.com/mysticatea/items/cc3f648e11368799e66c "ESLint のカスタムルールを作ろう! (その1) - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span></p>

ESLintのルールの作り方

----

## Proxyについて - JS.next
[js-next.hatenablog.com/entry/2015/12/03/045720](http://js-next.hatenablog.com/entry/2015/12/03/045720 "Proxyについて - JS.next")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6 Proxyについての解説

----

## Universal React ◆ 24 ways
[24ways.org/2015/universal-react/](https://24ways.org/2015/universal-react/ "Universal React ◆ 24 ways")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">tutorial</span></p>

Reactをサーバサイドで扱う方法について

----

## webpack+babel-loader+power-assert+jsdomでフロントエンド開発環境を作る - yutaponのブログ
[yutapon.hatenablog.com/entry/webpack%2Bbabel-loader%2Bpower-assert%2Bjsdom-skeleton](http://yutapon.hatenablog.com/entry/webpack%2Bbabel-loader%2Bpower-assert%2Bjsdom-skeleton "webpack+babel-loader+power-assert+jsdomでフロントエンド開発環境を作る - yutaponのブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設定</span></p>

BabelによるビルドとMochaでのテスト構成についての記事。
Webpackの設定、jsdomを使ったユニットテストについて

----

## How do Promises Work? - Quils in Space
[robotlolita.me/2015/11/15/how-do-promises-work.html](http://robotlolita.me/2015/11/15/how-do-promises-work.html "How do Promises Work? - Quils in Space")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promiseの小さな実装を書きながらPromiseについて学ぶ話

----

## notes/Do-not-underestimate-credentials-leaks.md at master · ChALkeR/notes
[github.com/ChALkeR/notes/blob/master/Do-not-underestimate-credentials-leaks.md](https://github.com/ChALkeR/notes/blob/master/Do-not-underestimate-credentials-leaks.md "notes/Do-not-underestimate-credentials-leaks.md at master · ChALkeR/notes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">セキュリティ</span></p>

主にNode.js関連のプロジェクトでのトークンやパスワードなど漏れが起きるパターンについて。
もし漏らしていた場合の影響や変更方法について書かれている

----

## Performance Calendar » WebPageTest: Year in Review
[calendar.perfplanet.com/2015/webpagetest-year-in-review/](http://calendar.perfplanet.com/2015/webpagetest-year-in-review/ "Performance Calendar » WebPageTest: Year in Review")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">まとめ</span></p>

今年WebPageTestに追加された機能や連携サービスについて。

- [WebPagetest - Website Performance and Optimization Test](http://www.webpagetest.org/ "WebPagetest - Website Performance and Optimization Test")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Chrome Dev Summit 2015 Notes
[danoc.me/blog/chrome-dev-summit-2015-notes/](https://danoc.me/blog/chrome-dev-summit-2015-notes/ "Chrome Dev Summit 2015 Notes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

Chrome Dev Summit 2015の動画とそれぞれの要点メモ。
サマリがまとまってるのでどの動画を見るかの参考になる

----

## JSConf US LastCall - Track B - YouTube
[www.youtube.com/playlist?list=PL37ZVnwpeshG7ThPHHHRvPFTeU1\_F\_tcP](https://www.youtube.com/playlist?list=PL37ZVnwpeshG7ThPHHHRvPFTeU1_F_tcP "JSConf US LastCall - Track B - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">動画</span></p>

JSConf US 2015の動画一覧

- [JSConf US Last Call - jsconf.micDrop()](http://lastcall.jsconf.us/ "JSConf US Last Call - jsconf.micDrop()")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## oneuijs/You-Dont-Need-jQuery
[github.com/oneuijs/You-Dont-Need-jQuery](https://github.com/oneuijs/You-Dont-Need-jQuery "oneuijs/You-Dont-Need-jQuery")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">JavaScript</span></p>

jQuery使わなくてもDOM APIを使って大体同じ事が出来るというまとめ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Jam3/web-audio-player
[github.com/Jam3/web-audio-player](https://github.com/Jam3/web-audio-player "Jam3/web-audio-player")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

後方互換性の問題やバージョン毎のバグが多いWeb Audio APIをラップしてクロスブラウザで再生をサポートするライブラリ

----

## peerigon/updtr
[github.com/peerigon/updtr](https://github.com/peerigon/updtr "peerigon/updtr")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

`npm outdated`ベースで、それぞれのモジュールをupdateしてnpm testを行うことで、テストが通ったモジュールのみをアップデート出来るツール

----

## Khaos - Easily generate oft-used project templates.
[khaos.io/](http://khaos.io/ "Khaos - Easily generate oft-used project templates.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

対話式のテンプレートジェネレーターツール。
テンプレートに使った変数を対話形式で埋められるプロジェクト設定のテンプレートを作れる

----

## embed.js
[riteshkr.com/embed.js/](http://riteshkr.com/embed.js/ "embed.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Twitter、gistやYouTube、絵文字など色々なものを埋め込み出来るライブラリ

----
