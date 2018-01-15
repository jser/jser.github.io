---
title: "JSer.infoを開始してから7年が経ちました"
author: azu
layout: post
date : 2018-01-15T09:00
category: 雑記
tags:
    - JSer

---

2011年1月15日にJSer.infoを開始してから今日でちょうど7年となりました。
今年は特にイベントもないので簡単にJSer.infoの振り返りを書いてみます。

## 去年の紹介記事

去年一年間に紹介したサイト数は1074でした。

[![今年のJSer.info紹介記事数](http://jser.info/uploads/media/2018/01/15-1515943367.png)](https://jser.info/data-dashboard/)

また、今までのすべての紹介したサイト数の合計は7691でした。

[![合計](http://jser.info/uploads/media/2018/01/15-1515984870.png)](https://jser.info/data-dashboard/)

JSer.infoの紹介したサイトデータはすべてデータ化されているので次のページから見れます。

- [jser/jser.info](https://github.com/jser/jser.info "jser/jser.info")
- [JSer.info Data Dashboard](https://jser.info/data-dashboard/ "JSer.info Data Dashboard")

## JSer.infoのゴール

あらためて振り返るとJSer.infoのゴールは次のようなものです。

- 「JavaScriptに興味がある人にもっとJavaScriptを知ってもらう」
- 「JavaScriptの情報を整理して正確に伝える」
- 「更新コストを小さくして、継続できる形を作る」

<!-- textlint-disable -->

毎年この時期になるとゴールを振り返って、そもそも情報とはなんだっけ?ということを考えています。

<!-- textlint-enable -->

以前[JavaScript情報ってなんだっけ?](http://azu.github.io/slide/2016/jser5years/javascript-information.html "JavaScript情報ってなんだっけ?")という発表でも話していましたが、情報とは誰かの主観が入ったデータだと思います。

[![JavaScript情報ってなんだっけ?](http://jser.info/uploads/media/2018/01/15-1515977359.png)](http://azu.github.io/slide/2016/jser5years/javascript-information.html)

JSer.infoのゴールには情報を整理(データを加工して)して正確に伝えるというものが含まれています。
そのため、主観によって誤った情報が伝わることを避けるために、更新までに次のようなプロセスを辿っています。

## JSer.infoのプロセス

JSer.infoの記事が更新されるまでのワークフローについては[JSer.infoの作り方](http://azu.github.io/slide/2017/jser_info/how_to_make_jser_info.html "JSer.infoの作り方")というスライドで詳しく扱っています。

![JSer.infoのワークフロー](https://azu.github.io/slide/2017/jser_info/resources/workflow-jser.png)

> <http://azu.github.io/slide/2017/jser_info/how_to_make_jser_info.html>より

情報を見て調べるプロセスについて書いていますが、見る方法に関しては大きくは変わっていません。
[LDR](http://reader.livedoor.com/)が終了したので[Irodr](https://github.com/azu/irodr "Irodr")を作ったりしましたが、
見る対象が変わっても見る方法にはあまり変化はない気がしています。

![見る–調べる](https://azu.github.io/slide/2017/jser_info/resources/workflow_watch_search.png)

> <http://azu.github.io/slide/2017/jser_info/how_to_make_jser_info.html>より

しかし、個人サイトからQiitaやMediumへ主軸が移行していった流れやGitHubに集約されていくなど情報の流れ方は変わってきています。
[JavaScript情報ってなんだっけ?](http://azu.github.io/slide/2016/jser5years/javascript-information.html "JavaScript情報ってなんだっけ?")でも触れていますが、情報にも「仕様」といった比較的破壊的な変更が行われないものから、作者の意向によって破壊的な変更が入る「ライブラリ」など粒度はさまざまです。(ここでの壊れやすいというのは一度知った情報の意味が時間などで変化してしまうこと)

![こわれやすい–こわれにくい](https://azu.github.io/slide/2016/jser5years/img/library-browser-spec.png)

> [JavaScript情報ってなんだっけ?](http://azu.github.io/slide/2016/jser5years/javascript-information.html "JavaScript情報ってなんだっけ?")より

最近はライブラリもRFCプロセスやLTSによって、壊れにくいプロセスを導入していっていくなどの傾向があります。
そのため、ライブラリであっても著名で組織的に動いているものは壊れにくくなっています。

- [emberjs/rfcs: RFCs for changes to Ember](https://github.com/emberjs/rfcs)
- [reactjs/rfcs: RFCs for changes to React](https://github.com/reactjs/rfcs)
- [angular/RELEASE_SCHEDULE.md at master · angular/angular](https://github.com/angular/angular/blob/master/docs/RELEASE_SCHEDULE.md)

また今まではライブラリの生死が、単純に作者のモチベーションで決まっていたことが多かったようにも思えます。
しかし、近年は企業がバックにいるケース、[OpenCollective](https://opencollective.com/ "OpenCollective - A New Form of Association, Transparent by Design")や[Patreon](https://www.patreon.com/ "Patreon")などによる支援、[JS Foundation](https://github.com/JSFoundation/TAC "JS Foundation")による組織的なサポートなど色々な形が増えています。

- [Projects - JS Foundation](https://js.foundation/community/projects "Projects - JS Foundation")

また単純なStar数やGitHub Pluseなどのリポジトリとしての情報だけではなく、コミュニティや組織と言った関連情報も見ないとそのライブラリを正しく評価できないと思います。

ライブラリを取り巻く状況は複雑化しているので、情報を伝える場合はこれを意識する必要があります。

## 検証と説明

単純に情報を紹介するだけなら、そのサイト/リポジトリの情報をコピペすればよいのですが、JSer.infoの目的には「JavaScriptの情報を整理して正確に伝える」が含まれています。(元の言語が英語の場合、そもそもコピペできないですが…)

そのため、できるだけ「正確に」説明するには「検証」する必要になってきます。

![検証 - 説明](https://azu.github.io/slide/2017/jser_info/resources/workflow_verify_explain.png)

> [JSer.infoの作り方](http://azu.github.io/slide/2017/jser_info/how_to_make_jser_info.html "JSer.infoの作り方")

JSer.infoでは、単純にまとめるならば嘘を書いてないか軸に検証しています。

この問題は難しいですが、色々なパターンの嘘があります。
完全な事実誤認から誇張表現、言葉（解釈）の問題などさまざまです。

JSer.infoでは主張が中心のものはあまり取り上げない(コードがでてこない記事など)ので、
完全な事実誤認かどうかは実際に動かすなどして技術的に検証することで大体解決します。

- [JavaScriptのトレンドを素振りして確認する方法 - Qiita](https://qiita.com/azu/items/bacd146ed2e26980b9b0 "JavaScriptのトレンドを素振りして確認する方法 - Qiita")

難しいのは誇張表現などの言葉の問題です。

誇張表現もさまざまで、紹介候補のサイトが必要ではない強い言葉を使っている場合は誤解を生む可能性が高いため慎重になります。
たとえば、強い言葉としては次のようなものがあります。（いわゆるFUDや過度な誇張表現は避けましょうというハナシです）

- Blazing fast
- is Dead
- 最速
- 最強
- 熱い
- 常識
- 終了
- これだけ知って(おけ|れば)
- これがベスト/もっとも優れた
- xxx時代の終わり
- yyy時代のはじまり
- 消耗
- ベストプラクティス
- カオス

また、誇張表現になりやすいものの一種として「〜互換」という言葉があります。

「React-compatible API」のように作者が主張している場合も、実際には完全な互換ではなく雰囲気的な互換性であることが多いです。
この場合は、ちゃんとテストケースもforkしてあるかなど、どこまで本当に互換性を担保しているかは技術的に検証します。
その結果、完全な互換ではないとわかった場合は「〜ライクなAPI」や「〜総合のAPI」、「〜との互換を目指す」といった表現にしています。

たとえば、React-compatibleと説明に書いてある[Nerv](https://github.com/NervJS/nerv "Nerv")を例にすると、
現時点ではReactのテストをパスするわけではないため完全互換ではありません。
しかし、[作者のコメント](https://github.com/NervJS/nerv/issues/10#issuecomment-356913486)も考慮すると、Reactとの互換性が目的の１つとなります。

- [NervJS/nerv: A blazing fast React alternative, compatible with IE8 and React 16.](https://github.com/NervJS/nerv "NervJS/nerv: A blazing fast React alternative, compatible with IE8 and React 16.")
- [What's the tradeoff? · Issue #10 · NervJS/nerv](https://github.com/NervJS/nerv/issues/10#issuecomment-356913486 "What&#39;s the tradeoff? · Issue #10 · NervJS/nerv")

そのため、JSer.infoでの説明文は次のようになっています。

> ReactライクなAPIをもつライブラリ。ファイルサイズや小さくしつつReactとの互換性をもつことを目的にしている。

また、自分自身が知らない分野を扱うときにも色々と注意が必要です。

最近ではJavaScriptといっても、[WebAssembly](http://webassembly.org/ "WebAssembly")や[WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL "WebGL")、[WebRTC](https://webrtc.org/ "WebRTC")といったその領域だけで専門分野が成立するものなどさまざまです。
今年の始めにあった[Meltdown and Spectre](https://spectreattack.com/ "Meltdown and Spectre")などセキュリティなども専門知識がないと正確な現状は把握することが難しいです。
JSer.infoではできる限り元をたどって把握しようとしますが、不確実性が含まれるなら無理に解釈して伝えることよりも伝えないことを選びます。
(代わりに元のデータがあるならば、そこへのリンクを貼る)

- [2018-01-09のJS: Spectre/Meltdownのブラウザへの影響、FuseBox 3.0、Nuxt.js 1.0 - JSer.info](https://jser.info/2018/01/10/spectremeltdown-fusebox-3.0-nuxt.js-1.0/ "2018-01-09のJS: Spectre/Meltdownのブラウザへの影響、FuseBox 3.0、Nuxt.js 1.0 - JSer.info")

現在のJavaScriptをすべて知っている人などいないため、すべてを正確に伝えることは難しいと思います。

### 説明する

また、JSer.infoでの説明文にも言葉を使っているので、この言葉のチェックも必要です。
誤った説明をして間違って伝わるのは自明ですが、正しいことを言っても正しくは伝わないことがあるためです。

たとえば、npmの[The npm Blog — v5.6.0 (2017-11-27)](http://blog.npmjs.org/post/167963735925/v560-2017-11-27 "The npm Blog — v5.6.0 (2017-11-27)")のようにまだStableでリリースしていないのにリリース記事を公開する場合があります。
この記事を紹介するのに、"npm 5.6.0リリース"と書いてしまうとStableで公開されたようにも見えてしまいます。(**pre**リリースはされているのでリリース自体はあっているが、Stableではないので誤解を生みそう)

そのため、このような場合は元の記事には書いてないですが"npm 5.6.0(beta)が公開された"のように補足を追加しています。

- [2017-12-05のJS: npm 5.6.0(beta)、React 16.2.0、New ECMAScript Proposals - JSer.info](https://jser.info/2017/12/05/npm-5.6.0beta-react-16.2.0-new-ecmascript-proposals/ "2017-12-05のJS: npm 5.6.0(beta)、React 16.2.0、New ECMAScript Proposals - JSer.info")

[textlint](https://github.com/textlint/textlint)という自然言語のLintツールを作ったのも、元をたどればJSer.infoの紹介文をチェックする辞書を作るためです。(現在は自作の[proofdict](https://proofdict.github.io/ "proofdict")を辞書として使っています)

[postem](https://github.com/azu/postem "postem")という投稿ツールでリアルタイムチェックや[jser/jser.github.io](https://github.com/jser/jser.github.io "jser/jser.github.io")のCIでLintなどが走っています。

[![postem](https://azu.github.io/slide/2017/jser_info/resources/postem.png)](https://github.com/azu/postem)

### 正確さに協力する

紹介したいサイトの一部が間違っているからとそこで止まっていてはもったないです。
何かおかしなところがあるなら聞いてみたり修正PRを出してみたりすれば解決することもあります。

そのため、ここが何か変だなーというところは修正Pull Requestを出したりしています。
些細なことだと記事内のリンク切れや間違っている部分の訂正などをしています。
新しくでてきたプロジェクトなら簡単な修正を送ってみて、どのようなコミュニティなのかという雰囲気をつかむことも紹介文を書くのに役立ちます。
（たとえば単純に社内のものをオープンソースにしてみただけなのか、コントビュートは歓迎されるのか、どのようなスピード感かなど）

## 記事を投稿する

紹介記事ごとにこれを繰り返してある程度数が溜まったら記事にしています。
目安はBotが教えてくれます。

![bot](http://jser.info/uploads/media/2018/01/15-1515972040.png)

<blockquote class="twitter-tweet" data-lang="en"><p lang="ja" dir="ltr"><a href="https://twitter.com/azu_re?ref_src=twsrc%5Etfw">@azu_re</a> 今の投稿ステータスです！<br>平均値: 21.03013698630137<br>中央値: 21<br>現在値: 15</p>&mdash; JSer.info (@jser_info) <a href="https://twitter.com/jser_info/status/952681063968485377?ref_src=twsrc%5Etfw">January 14, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

また、紹介記事を1つ追加するたびにCI/CD経由で公開する記事のベースとなるブランチを更新するようになっています。

----

**Note:** 今の週刊ではなく、紹介記事を1つ追加するたびにそれを見たい人は[Realtime版](https://realtime.jser.info/)がみれます。
CI/CD経由のブランチ更新と同じデータを使っているので、同じタイミングで更新されています。

- [Realtime JSer.info](https://realtime.jser.info/ "Realtime JSer.info")

----

実際に記事を公開するときは[github.com/jser/jser.github.io/compare/jser-week-366?expand=1](https://github.com/jser/jser.github.io/compare/jser-week-366?expand=1)のような作っておいたブランチからPull Requestを出す形になるので、基本的にGitHub Web UIだけで記事公開までできるようになっています。

![記事がたまったブランチ](http://jser.info/uploads/media/2018/01/15-1515972306.png)

> 記事がたまったブランチ – これをPRにして直接Webで編集してマージする

JSer.infoとして紹介する際にはカテゴリ(_アーティクル_とか)で分けていますが、[過去のデータ](https://github.com/jser/jser.info "jser/jser.info")を元にカテゴリを[ベイズ推定するライブラリ](https://github.com/jser/classifier-item-category)とかを書いたので、カテゴリ分類なども今は自動化されています。
そのため、現在はヘッドラインの説明を追加するだけになっています。

JSer.infoの記事が更新されるまでにはこのようなサイクルを辿っています。

![1サイクル](https://azu.github.io/slide/2017/jser_info/resources/workflow_around_jser.png)

## イテレーション

これらのイテレーションは、1週間程度の短いサイクルで行えるようにしています。
一度に遠くのゴールを目指すより、短い目標をちょっとづつクリアした方が継続できるためです。
(失敗した時に立て直しがしやすいという理由もあります)

![イテレーション](https://azu.github.io/slide/2017/jser_info/resources/workflow-week.png)

> [JSer.infoの作り方](http://azu.github.io/slide/2017/jser_info/how_to_make_jser_info.html "JSer.infoの作り方")

1紹介記事 = 1コミットというように小さく分散して更新していくのは、更新のコストを小さくするための一種の工夫です。

このようなサイクルを繰り返し大体ほど1週間に1度更新して、今365週間(7年)が経ちました。

## 今後

個人でやっているので情報に偏りがでやすいのは課題です。

そのため、他の人がJSer.info上で記事を投稿できるようにしたい。
現時点でもPull Requestを送ればできますが、あまりに広範囲に「寄稿募集しています」といっても成立するわけではないと思います。

先ほども書いたようにJavaScriptといっても分野はさまざまです。
何か特定の分野(ライブラリや技術、コミュニティなど)の状況についての記事を投稿してみたい人がいたら、そのようなところに限定してみるのが良さそうなです。JSer.infoに載せる場合は客観的な評価と主観的な感想の分離は必要なので、その辺の体裁は整える必要があると思いますが。

雰囲気的にはレポート系の記事とか、ロードマップに関連するIssueの状況のまとめなど、ちょっと踏み込まないと分かりにくい部分についてをまとめたい。

- [JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info](https://jser.info/2017/01/31/bundler-testing-framework-report/ "JSerレポート #1 Bundlerの未来、テスティングフレームワークの現状 - JSer.info")

たとえば、Babel 7の進捗についてまとめてみたり、ReactやAngularのIssueやロードマップの状況（定期的な状態）、[Meltdown and Spectre](https://spectreattack.com/ "Meltdown and Spectre")の各ブラウザの対応と方針など色々です。
最近ならばやっとすべてのモダンブラウザで有効化されそうなModuleの状況をまとめるなども面白そうです。

少なくてもPull Requestされた記事は自分がレビューするので、ダブルチェックがあることでより正確になるはずです。

また、この考えの背景には、◯◯の最新情報をまとめるブログやサイトは大体数ヶ月から2年ぐらいで途切れてしまってることがあります。
[Meta Weekly](http://azu.github.io/Meta-Weekly/ "Meta Weekly")にあるサイトが半分ぐらいは更新が止まっていると思います。

コミュニティベースのEchoJSや企業としてやっている[JavaScript Weekly](http://javascriptweekly.com/ "JavaScript Weekly")などはちゃんと継続していますが、個人でやっている場合には一度止まると再開はされにくい気がします。
個人で最新情報を継続的にまとめるには恐らくコストが高く、一度止まると復帰が難しい問題という問題があるのだと思います。

JSer.infoはその辺を徹底的に仕組化やイテレーションコストを小さくすることで対処しています。
また止まることは想定し、再開のしやすさに重きをおいています。

その辺を協力してやっていけるとJSer.infoとしても情報の偏りがバラけて、
かつ情報サイトをやりたい人はすでにあるJSer.infoに乗っかれる双方のメリットがあっていいのかなと思いました。

何かやってみたいことがある人は[![Gitter](https://badges.gitter.im/jser/jser.info.svg)](https://gitter.im/jser/jser.info)や[#jserinfo](https://twitter.com/search?f=tweets&vertical=default&q=%23jserinfo&src=typd "#jserinfo")、[@azu_re](https://twitter.com/azu_re "@azu_re")にお知らせください。

- [jser/jser.info - Gitter](https://gitter.im/jser/jser.info "jser/jser.info - Gitter")

## おわりに

先週が[#jserinfo 365回目](https://jser.info/2018/01/10/spectremeltdown-fusebox-3.0-nuxt.js-1.0/ "JSer.info #365")なので、
週一回の更新が7年間継続できているのだと思います。(`7 * 365 / 7; // => 365`)

JSer.info が何かの助けになっていれば幸いです。

意見や感想などがありましたら、[#jserinfo](https://twitter.com/search?f=tweets&vertical=default&q=%23jserinfo&src=typd "#jserinfo")のハッシュタグに投稿してください。