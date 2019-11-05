---
title: "2019-11-05のJS: MSEdge on Chromium RC、Immer 5.0.0、Speed Report on Search Console"
author: "azu"
layout: post
date : 2019-11-05T00:09:40.841Z
category: JSer
tags:
- MSEdge
- Google
- Library

---

JSer.info #460 - Microsoft EdgeのChromium版がRCリリースされました。

- [Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/)

ロゴがあたらしくなりましたが、Microsoft Edge on Chromiumは既に公開されているMicrosoft Edge Insider ChannelsのCanary、Dev、Betaでテストできます。
RCリリースの記事では、自動テストに使えるWebDriver、Puppeteer、IEDriverServer使ったMSEdgeのIEモードでの起動方法についてなどについても書かれています。

また、今後の開発予定についてはステータスページやExplainerページを参照してください。

- [Microsoft Edge web platform features status and roadmap - Microsoft Edge Development](https://developer.microsoft.com/en-us/microsoft-edge/platform/status/crossdomainfontloading/)
- [MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team](https://github.com/MicrosoftEdge/MSEdgeExplainers)

----

オブジェクトをImmutableに変更するライブラリであるImmer.js 5.0.0がリリースされました。

- [Release v5.0.0 · immerjs/immer](https://github.com/immerjs/immer/releases/tag/v5.0.0)

5.0.0では`Map`と`Set`のオブジェクトがサポートされています。
詳しくは次のドキュメントを参照するとよさそうです。

- [Working with classes · Immer](https://immerjs.github.io/immer/docs/complex-objects)
- [Support for Set and Map · Issue #146 · immerjs/immer](https://github.com/immerjs/immer/issues/146)

----

Google Search ConsoleにSpeed Reportが試験的に追加されました。

- [Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console](https://webmasters.googleblog.com/2019/11/search-console-speed-report.html)

[Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)のデータを元にした速度に関するLow、Middle、Fastのグループ分けを行い、問題の指摘などをしてくれます。
問題の改善方法についての詳細は、[Lighthouse](https://github.com/GoogleChrome/lighthouse)ベースとなった[PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)に誘導される形になっています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## OpenJS Foundation launches new professional certification program to support the future of Node.js development - OpenJS Foundation
[openjsf.org/blog/2019/10/22/openjs-foundation-launches-new-professional-certification-program-to-support-the-future-of-node-js-development/](https://openjsf.org/blog/2019/10/22/openjs-foundation-launches-new-professional-certification-program-to-support-the-future-of-node-js-development/ "OpenJS Foundation launches new professional certification program to support the future of Node.js development - OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

OpenJS Foundation(Node.js Foundation)がNode.jsのアプリケーション開発とサービス開発における2種類の認定プログラムを開始した


----

## Release v0.111.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.111.0](https://github.com/facebook/flow/releases/tag/v0.111.0 "Release v0.111.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.111.0リリース。
Object spread構文によるオブジェクトのマージにおける型推論の改善。
パフォーマンス改善に向けた試験的なフラグとして`experimental.minimal_merge`の追加など

- [Now you can spread disjoint unions without getting errors!](https://medium.com/flow-type/spreads-common-errors-fixes-9701012e9d58 "Now you can spread disjoint unions without getting errors!")

----

## The npm Blog — Release: 6.12.1
[blog.npmjs.org/post/188679949625/release-6121](https://blog.npmjs.org/post/188679949625/release-6121 "The npm Blog — Release: 6.12.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.12.1リリース。
Node.js 13のサポートなど


----

## Release v5.0.0 · immerjs/immer
[github.com/immerjs/immer/releases/tag/v5.0.0](https://github.com/immerjs/immer/releases/tag/v5.0.0 "Release v5.0.0 · immerjs/immer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Immer 5.0.0リリース。
MapとSetのサポート


----

## Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/](https://blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/ "Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge on ChromiumのRCリリース。
WebDriverの対応、Puppeteerの対応、IEDriverServer使ったMSEdgeのIEモードでの起動方法についてなど


----
<h1 class="site-genre">アーティクル</h1>

----

## Hands-on guide: developing & deploying Node.js apps in Kubernetes
[learnk8s.io/nodejs-kubernetes-guide/](https://learnk8s.io/nodejs-kubernetes-guide/ "Hands-on guide: developing & deploying Node.js apps in Kubernetes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Docker</span> <span class="jser-tag">kubernetes</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

Express+MongoなNode.jsアプリをDockerで動かして、それをminikubeを使ってローカルのKubernatesクラスタで動かし、スケーリングをテストするチュートリアル記事


----

## 5 TypeScript tips to improve your applications
[nehalist.io/5-typescript-tips-to-improve-your-architecture/](https://nehalist.io/5-typescript-tips-to-improve-your-architecture/ "5 TypeScript tips to improve your applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの型Tips。
Utility types、`unknown`型の利用、Lookup Types、ライブラリの型の拡張、ビルトインオブジェクトの型についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## React Conf 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLPxbbTqCLbGHPxZpw4xj\_Wwg8-fdNxJRh](https://www.youtube.com/playlist?list=PLPxbbTqCLbGHPxZpw4xj_Wwg8-fdNxJRh "React Conf 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Conf 2019の動画一覧

- [React Conf 2019 - Fall 2019 in Lake Las Vegas, Nevada](https://conf.reactjs.org/ "React Conf 2019 - Fall 2019 in Lake Las Vegas, Nevada")

----

## ReactHooksでvideoを乗りこなす - Speaker Deck
[speakerdeck.com/narirou/reacthookstevideowocheng-rikonasu](https://speakerdeck.com/narirou/reacthookstevideowocheng-rikonasu "ReactHooksでvideoを乗りこなす - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span> <span class="jser-tag">slide</span></p>

React Hooksを使ってVideoプレイヤーを作成することについてのスライド。
`<video>`要素の持つ複雑なステート管理、更新頻度に合わせたステートの分離、React Hooksの利用についてなど


----

## Building (And Re-Building) the Airbnb Design System | Maja Wichrowska & Tae Kim - YouTube
[www.youtube.com/watch?v&#x3D;fHQ1WSx41CA&amp;list&#x3D;PLPxbbTqCLbGHPxZpw4xj\_Wwg8-fdNxJRh&amp;index&#x3D;10&amp;t&#x3D;0s](https://www.youtube.com/watch?v=fHQ1WSx41CA&list=PLPxbbTqCLbGHPxZpw4xj_Wwg8-fdNxJRh&index=10&t=0s "Building (And Re-Building) the Airbnb Design System | Maja Wichrowska & Tae Kim - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Design</span> <span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

Airbnbのデザインシステムの過去、現在、未来についての発表。
最初はフラグメンテーションが問題になり、CSS-in-JSを使ってデザインをDSLに寄せたら複雑化しパフォーマンスが問題になった。
柔軟性とパフォーマンスをちょうどよく取れるモジューラなアーキテクチャを目指し再構築しているという話


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## SameSite cookie recipes
[web.dev/samesite-cookie-recipes/](https://web.dev/samesite-cookie-recipes/ "SameSite cookie recipes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span></p>

SameSite Cookiesへの対応方法について。
SameSite=Noneに対応していないUAの対策として、LegacyなCookieととSameSite属性をつけたCookieを両方渡すパターンについてなど


----

## Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console
[webmasters.googleblog.com/2019/11/search-console-speed-report.html](https://webmasters.googleblog.com/2019/11/search-console-speed-report.html "Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">performance</span></p>

Google Search ConsoleにChrome UX Reportを使った速度に関するレポートが一般公開された。
PC、モバイルごとに速度がLow、Middle、Fastの分類をして、その原因や改善方法の情報を提供する画面が追加された


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## mciastek/sal: 🚀 Performance focused, lightweight scroll animation library 🚀
[github.com/mciastek/sal](https://github.com/mciastek/sal "mciastek/sal: 🚀 Performance focused, lightweight scroll animation library 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">animation</span></p>

Intersection Observerを使ったスクロールアニメーションライブラリ。


----

## mikro-orm/mikro-orm: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Supports MongoDB, MySQL, MariaDB, PostgreSQL and SQLite databases.
[github.com/mikro-orm/mikro-orm](https://github.com/mikro-orm/mikro-orm "mikro-orm/mikro-orm: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Supports MongoDB, MySQL, MariaDB, PostgreSQL and SQLite databases.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">rnode</span> <span class="jser-tag">library</span> <span class="jser-tag">MySQL</span> <span class="jser-tag">MongoDB</span></p>

TypeScriptで書かれたMongoDB、MySQL、PostgreSQLなどのORMマッパーライブラリ


----

## kroitor/asciichart: Nice-looking lightweight console ASCII line charts ╭┈╯ for NodeJS, browsers and terminal, no dependencies
[github.com/kroitor/asciichart](https://github.com/kroitor/asciichart "kroitor/asciichart: Nice-looking lightweight console ASCII line charts ╭┈╯ for NodeJS, browsers and terminal, no dependencies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">graphic</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span></p>

コンソールでAscii線グラフを描画するライブラリ


----
