---
title: "2021-11-09のJS: React Router v6、Angular v13、ChromeのRecord and Replay、TypeScriptへの段階的な移行"
author: "azu"
layout: post
date : 2021-11-09T02:39:44.474Z
category: JSer
tags:
- React
- TypeScript
- Chrome
- performance
- node.js

---

JSer.info #565 - React Router v6がリリースされました。

- [React Router v6 | Remix](https://remix.run/blog/react-router-v6)

React Hooksベースで再実装、`<Route>`のネストの扱いを改善、`<Link to>`の値に相対パスの解釈を`<Route path>`を基準にする変更などが含まれています。

合わせてReact Router v5からのマイグレーションガイドも公開されています。

- [React Router | Upgrading from v5](https://reactrouter.com/docs/en/v6/upgrading/v5)

----

Angular 13がリリースされました。

- [Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog](https://blog.angular.io/angular-v13-is-now-available-cce66f7bc296)

IvyがデフォルトとなったためView Engineを削除されています。
Angular Package Format(APF)が`exports`フィールドのサポートが追加されています。
また、IE 11のサポートが終了されています。
AngularでのIEサポートはAngular 12までとなり、Angular 12は2022年11月12日までサポートされます。

- [Angular - Angular versioning and releases](https://angular.io/guide/releases#support-policy-and-schedule)

その他には、Angular CLIが永続ビルドキャッシュをサポート、テスト時にDOMのクリーンアップがデフォルト化されています。

----

[Record, replay and measure user flows - Chrome Developers](https://developer.chrome.com/docs/devtools/recorder/)という記事では、Chrome 97の開発者ツールにプレビュー実装されたRecorder panelについて紹介されています。

ユーザー操作を記録し再生でき、またユーザーフローとPerformance計測を組み合わせて利用できます。
また、記録した内容は編集したり、Puppeteerスクリプトとして出力できるようになっています。

----

以下の記事はどちらもJavaScriptからTypeScriptへの段階的な移行について書かれています。

- [インクリメンタルに新しい技術を取り入れる方法。TypeScriptへの移行を例にしたプロセス](https://tech.plaid.co.jp/karte-blocks-incremental-development/)
- [Etsy’s Journey to TypeScript - Code as Craft](https://codeascraft.com/2021/11/08/etsys-journey-to-typescript/)

ゆるい型をつけてから段階的に厳しくしていくアプローチと最初から厳密な型をつけていくというアプローチをそれぞれ扱っているので、合わせて読んでみると面白いと思います。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v11.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v11.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v11.0.0 "Release v11.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 11.0.0リリース。
Out of Processなiframeのwaitをサポートする`Page.waitForFrame()`と`frame.isOOPFrame()`の追加。
HTTP Requestのinitiatorを取得できるようになるなど


----

## Recoil 0.5 | Recoil
[recoiljs.org/blog/2021/11/03/0.5.0-release](https://recoiljs.org/blog/2021/11/03/0.5.0-release "Recoil 0.5 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.5リリース。
キャッシュをクリアできる`useRecoilRefresher_UNSTABLE()`の追加。
`onSet`のコールバックに`isReset`を追加、`getLoadable()`/`getPromise()`/`getInfo_UNSTABLE()`の追加など


----

## React Router v6 | Remix
[remix.run/blog/react-router-v6](https://remix.run/blog/react-router-v6 "React Router v6 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Router v6リリース。
React Hooksベースで再実装、`<Route>`のネストの改善、`<Link to>`の値に相対パスの解釈を`<Route path>`を基準にするように変更など

- [React Router v6 | Remix](https://remix.run/blog/react-router-v6#upgrading-to-react-router-v6 "React Router v6 | Remix")
- [React Router | Upgrading from v5](https://reactrouter.com/docs/en/v6/upgrading/v5 "React Router | Upgrading from v5")

----

## Announcing TypeScript 4.5 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/ "Announcing TypeScript 4.5 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.5 RCリリース。
4.5 betaで導入されていたESM対応の`module: node12`はリリースが延期となった。


----

## Nightwatch v2 is Now in Beta | Nightwatch.js Blog
[nightwatchjs.org/blog/nightwatch-v2-beta-is-available.html](https://nightwatchjs.org/blog/nightwatch-v2-beta-is-available.html "Nightwatch v2 is Now in Beta | Nightwatch.js Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nightwatch v2リリース。
Chrome DevTools ProtocolとWebDriver BiDIのサポート、CucumberJSのサポートなど


----

## V8 release v9.7 · V8
[v8.dev/blog/v8-release-97](https://v8.dev/blog/v8-release-97 "V8 release v9.7 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v9.7リリース。
ArrayとTypedArrayに`findLast`と`findLastIndex`の実装。


----

## Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog
[blog.angular.io/angular-v13-is-now-available-cce66f7bc296](https://blog.angular.io/angular-v13-is-now-available-cce66f7bc296 "Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 13リリース。
IvyがデフォルトとなったためView Engineを削除、Angular Package Format(APF)が`exports`フィールドのサポート、IE 11のサポート終了。
Angular CLIが永続ビルドキャッシュをサポート、テスト時にDOMのクリーンアップがデフォルト化など


----

## Release v4.0.0 · markedjs/marked
[github.com/markedjs/marked/releases/tag/v4.0.0](https://github.com/markedjs/marked/releases/tag/v4.0.0 "Release v4.0.0 · markedjs/marked")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

markded 4.0.0リリース。
ESMの対応、default exportを削除したため`import { markded } from "marked"`のnamed importを利用するに変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## What&#039;s new in PageSpeed Insights
[web.dev/whats-new-pagespeed-insights/](https://web.dev/whats-new-pagespeed-insights/ "What&#039;s new in PageSpeed Insights")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

新しいPageSpeed Insightsの画面解説。
計測データとCrUXデータ(Lab)が混在していたが、CrUXのデータはOrigin Summaryというタブに分離された。
Core Web Vitalsのスコア表示などが含まれる予定


----

## Malware found in coa and rc, two npm packages with 23M weekly downloads - The Record by Recorded Future
[therecord.media/malware-found-in-coa-and-rc-two-npm-packages-with-23m-weekly-downloads/](https://therecord.media/malware-found-in-coa-and-rc-two-npm-packages-with-23m-weekly-downloads/ "Malware found in coa and rc, two npm packages with 23M weekly downloads - The Record by Recorded Future")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

`coa`と`rc`パッケージにマルウェアが含まれていたバージョンがpublishされていた問題について。
現在は無効化されているが、それぞれ次のバージョンが問題となっている。

- coa: 2.0.3, 2.0.4, 2.1.1, 2.1.3, 3.0.1, 3.1.3
- rc: 1.2.9, 1.3.9, 2.3.9

- [Embedded malware in coa · GHSA-73qr-pfmq-6rp8 · GitHub Advisory Database](https://github.com/advisories/GHSA-73qr-pfmq-6rp8 "Embedded malware in coa · GHSA-73qr-pfmq-6rp8 · GitHub Advisory Database")
- [Embedded malware in rc · GHSA-g2q5-5433-rhrf · GitHub Advisory Database](https://github.com/advisories/GHSA-g2q5-5433-rhrf "Embedded malware in rc · GHSA-g2q5-5433-rhrf · GitHub Advisory Database")

----

## Record, replay and measure user flows - Chrome Developers
[developer.chrome.com/docs/devtools/recorder/](https://developer.chrome.com/docs/devtools/recorder/ "Record, replay and measure user flows - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Chrome 97の開発者ツールにプレビュー実装されたRecorder panelについて。
ユーザー操作を記録し再生できる。またユーザーフローとPerformance計測を組み合わせられる。
記録した内容は編集したり、Puppeteerスクリプトとして出力できる。


----

## TypeScriptのJSDocサポートでできること、できないこと
[zenn.dev/qnighy/articles/56917d9bf9077b](https://zenn.dev/qnighy/articles/56917d9bf9077b "TypeScriptのJSDocサポートでできること、できないこと")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

TypeScriptのJSDocによる型アノテーションについての解説。
TypeScriptとJSDocの型アノテーションでの表現力の違い、JSDocでの型アノテーションの書き方について


----

## A Comprehensive Guide To Error Handling In Node.js - Honeybadger Developer Blog
[www.honeybadger.io/blog/errors-nodejs/](https://www.honeybadger.io/blog/errors-nodejs/ "A Comprehensive Guide To Error Handling In Node.js - Honeybadger Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsのエラーハンドリングについての記事。
例外、コールバック、Promise、EventEmitterそれぞれにおけるエラーのハンドリング。
カスタムエラーでの分類、Operational ErrorとProgrammer Errorの違い。
またOperation Errorが発生したときの対処方法とProgrammer Errorの防止策について


----

## インクリメンタルに新しい技術を取り入れる方法。TypeScriptへの移行を例にしたプロセス
[tech.plaid.co.jp/karte-blocks-incremental-development/](https://tech.plaid.co.jp/karte-blocks-incremental-development/ "インクリメンタルに新しい技術を取り入れる方法。TypeScriptへの移行を例にしたプロセス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

JavaScriptをTypeScriptを段階的に移行する方法について。
最初からしっかりとした型をつける方法とゆるい型に変換してから型をつける方法の比較、マイグレーションの順番、型を使ったAPIバリデーション、VueからReactへの段階的な移行など。
インクリメンタルな移行するときのポイントについて。


----

## Etsy’s Journey to TypeScript - Code as Craft
[codeascraft.com/2021/11/08/etsys-journey-to-typescript/](https://codeascraft.com/2021/11/08/etsys-journey-to-typescript/ "Etsy’s Journey to TypeScript - Code as Craft")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

TypeScriptの採用戦略についての記事。
厳密な型付けへの移行方法、typescript-eslintを使った一部の汎用型と構文の禁止、APIへの型付けについて。
TypeScriptの型チェックのパフォーマンス問題のデバッグ、教育について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Web Performance Metrics Cheatsheet
[bitsofco.de/web-performance-metrics-cheatsheet/](https://bitsofco.de/web-performance-metrics-cheatsheet/ "Web Performance Metrics Cheatsheet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">cheatsheet</span></p>

ウェブパフォーマンスのメトリクスチートシート。
4つのステージにグループ分けし、それぞれに関連するメトリクスをまとめている


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## urin/qrono: 🕥 Just right date time library
[github.com/urin/qrono](https://github.com/urin/qrono "urin/qrono: 🕥 Just right date time library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutableな日付操作ライブラリ。
UTCとローカル時間のみを扱うことで、夏時間のあいまいな時間を正確に扱う。

- [こういうのでいいんだよ、な JavaScript日付時刻ライブラリ Qrono](https://zenn.dev/urin/articles/6ca9cf8174fd92 "こういうのでいいんだよ、な JavaScript日付時刻ライブラリ Qrono")

----

## Shopify/hydrogen: React-based framework for building dynamic, Shopify-powered custom storefronts.
[github.com/Shopify/hydrogen](https://github.com/Shopify/hydrogen "Shopify/hydrogen: React-based framework for building dynamic, Shopify-powered custom storefronts.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">vite</span> <span class="jser-tag">library</span></p>

Shopifyのストアフロントを作成するReactベースのフレームワーク。
ViteとReactをベースにしていて、React ServerSide Componentsを利用している。

- [Meet Hydrogen: A React Framework For Dynamic, Contextual And Personalized E-Commerce — Smashing Magazine](https://www.smashingmagazine.com/2021/11/hydrogen-react-framework-dynamic-contextual-personalized-ecommerce/ "Meet Hydrogen: A React Framework For Dynamic, Contextual And Personalized E-Commerce — Smashing Magazine")

----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript（第7版） | Ohmsha
[www.ohmsha.co.jp/book/9784873119700/](https://www.ohmsha.co.jp/book/9784873119700/ "JavaScript（第7版） | Ohmsha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2021年12月2日発売
サイ本 7版の翻訳本


----
