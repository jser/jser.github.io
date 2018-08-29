---
title: "2018-08-28のJS: Babel 7、BabelとTypeScript、継続的なパフォーマンス改善と計測"
author: "azu"
layout: post
date : 2018-08-28T02:02:42.367Z
category: JSer
tags:
- babel
- TypeScript
- performance

---

JSer.info #398 - Babel 7が正式にリリースされました。

- [Babel 7 Released · Babel](https://babeljs.io/blog/2018/08/27/7.0.0)

Node.js 4のサポート終了し、`@babel`スコープへモジュールを移動、`es2015`のような年号プリセットを廃止し`@babel/preset-env`に移行、Stageプリセットを廃止などが行われています。

- 年号プリセット(`babel-preset-es2015`) -> 廃止([@babel/preset-env](https://babeljs.io/docs/en/next/babel-preset-env.html)へ移行)
- Stageプリセット -> 廃止(個別の`@babel/plugin-proposal-*`プラグインを使う)
- `babel-preset-env` -> `@babel/preset-env`へ移行

またJavaScriptで設定を書ける`babel.config.js`での設定をサポート、パフォーマンスの改善などが行われています。

マイグレーションは[babel-upgrade](https://github.com/babel/babel-upgrade)というツールで行え、マイグレーションガイドも合わせて公開されています。

- [Upgrade to Babel 7 · Babel](http://babeljs.io/docs/en/next/v7-migration)

[TypeScript and Babel 7 | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/08/27/typescript-and-babel-7/)という記事では、Babel 7でTypeScriptのコードをJavaScriptに変換できる(型情報を取り除ける)ことについて紹介されています。

Babel 7では[TypeScriptのコードをパース](https://github.com/babel/babylon/pull/523)できるようになり、[@babel/preset-typescript](https://babeljs.io/docs/en/next/babel-preset-typescript.html)を利用してFlowと同じように型情報を取り除いてJavaScriptに変換できます。

制限として、Babel自体は型チェックを行なわないことや`enum`/`namespace`のようなTypeScript独自の構文はサポートしてない点についても紹介されています。

----

[Webpagetestから始める継続的パフォーマンス改善](http://azu.github.io/slide/2018/roppongijs/webpagetest-performance.html)というスライドでは、継続的パフォーマンスを行うために継続的にパフォーマンス計測を行うことについてかかれています。

パフォーマンス改善と指標、それを測るための[WebPagetest](https://www.webpagetest.org/)といったサービスの紹介。
また、計測した可視化する方法や改善した結果を確認したり、実際にどのように問題を見つけるかやパフォーマンスリグレッションを防ぐ方法などについて書かれています。

[WebPagetest](https://www.webpagetest.org/)のUIの使い方については[A brief guide to using WebpageTest - Frontend News #5](https://frontendnews.io/editions/2018-08-22-a-brief-guide-to-webpagetest)という記事が公開されていたので合わせて読むと良さそうです。

またパフォーマンス改善方法については[Web Performance Made Easy: Google I/O 2018 edition  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/web-performance-made-easy)というリファインされた記事が公開されているので合わせて読むと良さそうです。

----

## お知らせ

2018年9月22日(土)に開催予定の[JSer.info 400回記念イベント](https://github.com/jser/jser.info/issues/102)ですが、今週中にconnpassでイベントページを公開予定です。
次のグループのメンバーになっておくと、イベントページが公開された時に通知が飛ぶと思います。（抽選にすると思うので、ゆっくり登録できると思います）

- [JSer.info - connpass](https://jser.connpass.com/)

[以前](https://github.com/jser/jser.info/issues/89)と[同じ](https://github.com/jser/jser.info/issues/31)[ように](https://github.com/jser/jser.info/issues/54)、数人の発表者とメモを書いてくれる人と質問を管理してくれるモデレータ(具体的には[http://sli.do/](http://sli.do/)周りの管理)を募集する予定です。

テーマは「憶測せずに議論しよう」です。

会場には大体自分より何かしら詳しい人がいると思います。そのため、発表者であっても憶測でしゃべるよりはその場で詳しい人に聞いて議論することを重要視しています。

発表途中でも発表者に質問することや逆に会場の人に質問することを推奨する感じのイベントです（これは会場に「XXXを使ってる人」と聞くのではなく、疑問を解決する話）

発表者は深く考えずに質問時間が長く取れるJavaScriptに関連する発表という感じで応募していただけると幸いです。
(発表に集中してもらえるように細かい補助とかは自分がやります。)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## jsdom/Changelog.md at master · jsdom/jsdom
[github.com/jsdom/jsdom/blob/master/Changelog.md#1200](https://github.com/jsdom/jsdom/blob/master/Changelog.md#1200 "jsdom/Changelog.md at master · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 12.0.0リリース。
Node.js 8以降が必要になるように、`ResourceLoader`の追加、依存の更新など


----

## Johnny-Five.io: Johnny-Five v1.0
[johnny-five.io/news/v1\_0/](http://johnny-five.io/news/v1_0/ "Johnny-Five.io: Johnny-Five v1.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Robotics Programming Frameworkの Johnny-Five v1.0リリース


----

## Release v1.1.0 · stimulusjs/stimulus
[github.com/stimulusjs/stimulus/releases/tag/v1.1.0](https://github.com/stimulusjs/stimulus/releases/tag/v1.1.0 "Release v1.1.0 · stimulusjs/stimulus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Turbolinksと連携できるJavaScriptフレームワークのStimulus 1.1.0リリース。
`@stimulus/polyfills`の追加、`data-action`属性で複数のactionを指定時にその順序を尊重するように、`DOMContentLoaded`で処理を開始するようになるなど


----

## Almin v0.18 – React Native compatible · Almin
[almin.js.org/blog/2018/08/27/almin-0.18.html](https://almin.js.org/blog/2018/08/27/almin-0.18.html "Almin v0.18 – React Native compatible · Almin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">almin</span></p>

ステート管理ライブラリのAlmin 0.18.0リリース。
TypeScript 3.0に対応、React Nativeとの互換性の向上、ファイルサイズの削減など


----

## Babel 7 Released · Babel
[babeljs.io/blog/2018/08/27/7.0.0](https://babeljs.io/blog/2018/08/27/7.0.0 "Babel 7 Released · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7リリース。
Node.js 4以下のサポート終了、`@babel`スコープへモジュールを移動、`es2015`のような年号プリセットを廃止し`preset-env`に移行、Stageプリセットを廃止。
`babel.config.js`での設定をサポート、パフォーマンスの改善など。
マイグレーションは`babel-upgrade`で行える。

- [babel/babel-upgrade: ⬆️ A tool for upgrading Babel versions (to v7): \`npx babel-upgrade\`](https://github.com/babel/babel-upgrade "babel/babel-upgrade: ⬆️ A tool for upgrading Babel versions (to v7): \&#x60;npx babel-upgrade\&#x60;")

----
<h1 class="site-genre">アーティクル</h1>

----

## dep: a little Node.js dependency installer – Daijiro Wachi – Medium
[medium.com/@watilde/dep-a-little-node-js-dependency-installer-b8fead7596d3](https://medium.com/@watilde/dep-a-little-node-js-dependency-installer-b8fead7596d3 "dep: a little Node.js dependency installer – Daijiro Wachi – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span> <span class="jser-tag">npm</span></p>

`package.json`の依存をインストールできる`dep`について。
`npm`のコマンドと違って`install`、`lock`、`run`のみを扱う


----

## WorkerDOM: Concurrency for JavaScript programming with the DOM – Accelerated Mobile Pages Project
[amphtml.wordpress.com/2018/08/21/workerdom/](https://amphtml.wordpress.com/2018/08/21/workerdom/ "WorkerDOM: Concurrency for JavaScript programming with the DOM – Accelerated Mobile Pages Project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">webworker</span> <span class="jser-tag">article</span> <span class="jser-tag">AMP</span> <span class="jser-tag">JavaScript</span></p>

WebWorkerの中で動くDOMの実装のアルファ版を公開したという話。
メインスレッドでの処理が重なるとjankとなるため、WorkerスレッドでDOM APIの処理を行う実験的実装。
HydrateしたデータでWorkerとの間をやりとりし、変更はMutationObserverで監視する

- [WorkerDOM: JavaScript Concurrency and the DOM - Speaker Deck](https://speakerdeck.com/cramforce/workerdom-javascript-concurrency-and-the-dom "WorkerDOM: JavaScript Concurrency and the DOM - Speaker Deck")
- [ampproject/worker-dom: The same DOM API and Frameworks you know, but in a Web Worker.](https://github.com/ampproject/worker-dom "ampproject/worker-dom: The same DOM API and Frameworks you know, but in a Web Worker.")

----

## Why GraphQL: Advantages, Disadvantages & Alternatives - RWieruch
[www.robinwieruch.de/why-graphql-advantages-disadvantages-alternatives/](https://www.robinwieruch.de/why-graphql-advantages-disadvantages-alternatives/ "Why GraphQL: Advantages, Disadvantages & Alternatives - RWieruch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">graphic</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

GraphQLに関する連載記事。
GraphQLの特徴、メリット、デメリット、Apolloについて。またApollo Serverとexpressを使ってGraphQLサーバを作成するチュートリアルなど

- [GraphQL Server Tutorial with Apollo Server and Express - RWieruch](https://www.robinwieruch.de/graphql-apollo-server-tutorial/ "GraphQL Server Tutorial with Apollo Server and Express - RWieruch")

----

## Web Performance Made Easy: Google I/O 2018 edition  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/08/web-performance-made-easy](https://developers.google.com/web/updates/2018/08/web-performance-made-easy "Web Performance Made Easy: Google I/O 2018 edition  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

ウェブサイトのパフォーマンスについての概要的な記事の。
LightHouseやChromeの開発者ツールを使った不必要なリソースの把握。
JavaScriptのサイズが起動速度に与える影響やファイルサイズの削減、レンダリングのボトルネックの取り除く方法などについて


----

## TypeScript and Babel 7 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/08/27/typescript-and-babel-7/](https://blogs.msdn.microsoft.com/typescript/2018/08/27/typescript-and-babel-7/ "TypeScript and Babel 7 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babel 7の`@babel/typescript`について。
BabelでTypeScriptのコードをJavaScriptへ変換(型情報を除去)できる。
型チェックやいくつかのTS独自の構文をサポートしないという制限はあるが、Babelのエコシステム上でTSのコードを扱える。


----

## Service Worker Caching Strategies Based on Request Types
[medium.com/dev-channel/service-worker-caching-strategies-based-on-request-types-57411dd7652c](https://medium.com/dev-channel/service-worker-caching-strategies-based-on-request-types-57411dd7652c "Service Worker Caching Strategies Based on Request Types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Fetch</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

どの種類に対するリクエストかを判定できる`Request.destination`について。 `Request.destination`を使いキャッシュの戦略を変えるという話。注意点として、一部リクエストは空文字列となり判定できないという話。
また`Request.mode`や`Request.url`などとの組み合わせについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Webpagetestから始める継続的パフォーマンス改善
[azu.github.io/slide/2018/roppongijs/webpagetest-performance.html](http://azu.github.io/slide/2018/roppongijs/webpagetest-performance.html "Webpagetestから始める継続的パフォーマンス改善")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">webservice</span> <span class="jser-tag">slide</span></p>

ウェブアプリの継続的なパフォーマンス改善についてのスライド。
パフォーマンス改善と指標、それを測るための継続的な計測とサービスについて。
WebPagetestを中心にどのように計測して可視化し、改善した結果を確認したりリグレッションを防ぐかについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## A brief guide to using WebpageTest - Frontend News #5
[frontendnews.io/editions/2018-08-22-a-brief-guide-to-webpagetest](https://frontendnews.io/editions/2018-08-22-a-brief-guide-to-webpagetest "A brief guide to using WebpageTest - Frontend News #5")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">webservice</span></p>

ウェブサイトのパフォーマンス計測サービスであるWebPagetestの使い方を解説した記事。
それぞれのビューの読み方や指標となる値などについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## rikschennink/fitty: ✨ Makes text fit perfectly
[github.com/rikschennink/fitty](https://github.com/rikschennink/fitty "rikschennink/fitty: ✨ Makes text fit perfectly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

指定した要素に対してテキストのサイズを合わせるライブラリ。
カスタムフォントなどにも対応している


----
