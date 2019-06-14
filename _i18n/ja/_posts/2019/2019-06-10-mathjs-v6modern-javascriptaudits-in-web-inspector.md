---
title: "2019-06-10のJS: mathjs v6、Modern JavaScriptパッケージの配布、Audits in Web Inspector"
author: "azu"
layout: post
date : 2019-06-10T16:21:33.839Z
category: JSer
tags:
- mathjs
- Safari
- npm

---

JSer.info #439 - 数値計算ライブラリの[Math.js](https://mathjs.org/) v6がリリースされました。

- [mathjs v6: a monolith turned modular - Jos de Jong](https://josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/)

Math.jsは全体で200個以上の機能がありファイルサイズが137kB(gzip)もありました。
そのため、v6では必要なものだけをモジュールとして使えるようにするための構造的な変更が含まれています。
次のように書いた場合に、必要なもの以外を削除したりTree Shakingができるように[`"module"` field](https://github.com/rollup/rollup/wiki/pkg.module)に対応しています。

```js
import { log } from "mathjs";

console.log(log(10))
``` 

また、グローバルな設定ではなく`create`関数で依存と設定から特定の機能を作れるようになっています。
その他にも、BigNumberの対応などを取り除いた軽量版の`mathjs/number`も利用できるようになっています。

併せてパッケージ配布について書かれた[Enabling Modern JavaScript on npm](https://jasonformat.com/enabling-modern-js-on-npm/)という記事も読むと良さそうです。Modern JavaScriptは「ES2015以降の構文を使った書かれたコード」ぐらいの意味ですが、npmパッケージとして配布されている多くのコードはES5に変換(Transpile)されたものが公開されています。そのため、パッケージの利用者はES5に変換されたコードを利用することになって、Modernを選択できなくなる問題について書かれています。

これを解決するために、WebpackやRollupでは`package.json`の`"module"` fieldなどをサポートし、パッケージ利用者が選択できるようになっています。
また、[Microbundle](https://github.com/developit/microbundle)や[@pika/pack](https://www.pikapkg.com/blog/introducing-pika-pack/)などのModern JavaScriptをパッケージとして配布を補助するツールも出てきいますが、まだエコシステム全体としての固まりきっていない部分があるという話も書かれています。

----


次の記事では[Safari Technology Preview 75](https://webkit.org/blog/8594/release-notes-for-safari-technology-preview-75/)から追加されたSafariのAudit Tabについて解説されています。

- [Audits in Web Inspector | WebKit](https://webkit.org/blog/8935/audits-in-web-inspector/)

デフォルトではアクセシビリティに関するAuditルールが定義されていて、アクセシビリティのチェックができます。

また、このAuditタブではTest Case Formatに従ったJSONを読み込むことで任意のチェックツールを定義できます。
次の記事では、ESLintをつかった`*.js`ファイルのチェックを行うルールを定義してAuditタブでチェックする方法を紹介しています。
 
- [Creating Web Inspector Audits | WebKit](https://webkit.org/blog/8937/creating-web-inspector-audits/)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v12.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.4.0/](https://nodejs.org/en/blog/release/v12.4.0/ "Node v12.4.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.4.0リリース。
`import`文でJSONを読み込める` --experimental-json-modules`フラグの削除、V8 heap profilerを扱う`--heap-prof`フラグの追加など


----

## mathjs v6: a monolith turned modular - Jos de Jong
[josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/](https://josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/ "mathjs v6: a monolith turned modular - Jos de Jong")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

matchjs v6リリース。
モジューラーなアプローチで利用できるように変更。
グローバルな設定ではなく`create`関数で依存と設定から特定の機能を作れるように、ES moduleでimportした際にtree-shakingができるように。
また`number`のみをサポートしたバージョンも同梱されている。

- [mathjs/HISTORY.md at develop · josdejong/mathjs](https://github.com/josdejong/mathjs/blob/develop/HISTORY.md#2019-06-08-version-600 "mathjs/HISTORY.md at develop · josdejong/mathjs")

----

## Storybook 5.1
[medium.com/storybookjs/storybook-5-1-50afd02b5bbb](https://medium.com/storybookjs/storybook-5-1-50afd02b5bbb "Storybook 5.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">開発環境</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Stroybook 5.1リリース。
React Nativeの再対応、A11y addonの改善、Context addonの追加、TypeScrip向けのpresetを追加など

- [Real-time accessibility testing with Storybook](https://medium.com/storybookjs/instant-accessibility-qa-linting-in-storybook-4a474b0f5347 "Real-time accessibility testing with Storybook")
- [Intro to Presets](https://storybook.js.org/docs/presets/introduction/ "Intro to Presets")

----

## Release v3.0.0 · mqttjs/MQTT.js
[github.com/mqttjs/MQTT.js/releases/tag/v3.0.0](https://github.com/mqttjs/MQTT.js/releases/tag/v3.0.0 "Release v3.0.0 · mqttjs/MQTT.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MQTT.js 3.0.0リリース。
MQTT 5.0をサポート。


----
<h1 class="site-genre">アーティクル</h1>

----

## Audits in Web Inspector | WebKit
[webkit.org/blog/8935/audits-in-web-inspector/](https://webkit.org/blog/8935/audits-in-web-inspector/ "Audits in Web Inspector | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Safariの開発者ツールに追加されたAudit Tabについて。
デフォルトではアクセシビリティについてのAuditが含まれていて、自分でAuditのルールを定義して追加できるようになっている。
例としてESLintを`*.js`に対して実行するAuditルールが挙げられている。

- [Creating Web Inspector Audits | WebKit](https://webkit.org/blog/8937/creating-web-inspector-audits/ "Creating Web Inspector Audits | WebKit")

----

## An introduction to the MediaRecorder API - Twilio
[www.twilio.com/blog/mediastream-recording-api](https://www.twilio.com/blog/mediastream-recording-api "An introduction to the MediaRecorder API - Twilio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

MediaRecorder APIで音声の録音とダウンロードを行うチュートリアル


----

## ECMAScript proposal updates @ 2019-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2019/06/09/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2019/06/09/ecmascript-proposal-updates "ECMAScript proposal updates @ 2019-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2019年6月のTC39ミーティングでStage変更があったECMAScript Proposalのまとめ。
Dynamic ImportがついにStage 4となった。


----

## Dive into IndexedDB
[flaviocopes.com/indexeddb/](https://flaviocopes.com/indexeddb/ "Dive into IndexedDB")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

PromiseベースのIndexedDBラッパーである`idb`を使ったIndexedDBについてのチュートリアル。
データの追加、削除、マイグレーションについて

- [jakearchibald/idb: IndexedDB, but with promises](https://github.com/jakearchibald/idb "jakearchibald/idb: IndexedDB, but with promises")

----

## Enabling Modern JavaScript on npm
[jasonformat.com/enabling-modern-js-on-npm/](https://jasonformat.com/enabling-modern-js-on-npm/ "Enabling Modern JavaScript on npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">npm</span></p>

npmにパッケージとして公開するモジュールについて。
Bundleツールなどの変化によって、Transpile済みのファイルのみを配布すると利用者は最適化ができない問題について。
`package.json`の`"main"`、`"module"`、`"unpkg"`フィールドと配布するモジュールの形式やパッケージ作者が配布時に気をつける点。
またmicrobundleや`@pika/pack`などのパッケージ配布の補助ツールについてなど


----

## CSS Grid Level 2 - subgrid is coming to Firefox - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/06/css-grid-level-2-subgrid-is-coming-to-firefox/](https://hacks.mozilla.org/2019/06/css-grid-level-2-subgrid-is-coming-to-firefox/ "CSS Grid Level 2 - subgrid is coming to Firefox - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Grid Level 2のサブグリッドについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Inside Frontend #3 - YouTube
[www.youtube.com/playlist?list&#x3D;PLZFhK-XSlb82hef6Sxyqcc-6e8xVTbaIE&amp;app&#x3D;desktop](https://www.youtube.com/playlist?list=PLZFhK-XSlb82hef6Sxyqcc-6e8xVTbaIE&app=desktop "Inside Frontend #3 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Inside Frontend #3 の動画一覧

- [Inside Frontend | 2019年5月18日 Frontendカンファレンスを渋谷Abema Towersで開催](https://inside-frontend.com/ "Inside Frontend | 2019年5月18日 Frontendカンファレンスを渋谷Abema Towersで開催")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## npmfs - home
[npmfs.com/](https://npmfs.com/ "npmfs - home")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span></p>

npmに公開されているパッケージのソースコードビューアサービス。
特定のバージョンのコードを参照したり、バージョン間のDiffを見られるようになっている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## urql
[formidable.com/open-source/urql/](https://formidable.com/open-source/urql/ "urql")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React Hooksに対応したGraphQLを扱うReact向けライブラリ。
Queryの取得状態や取得結果を使ったコンポーネントを扱える

- [Urql, Grown Up](https://formidable.com/open-source/urql/ "Urql, Grown Up")

----

## lukeed/tinydate: A tiny (340B) reusable date formatter. Extremely fast!
[github.com/lukeed/tinydate](https://github.com/lukeed/tinydate "lukeed/tinydate: A tiny (340B) reusable date formatter. Extremely fast!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ファイルサイズが小さなDate Formatterライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## 実践TypeScript ~ BFFとNext.js&Nuxt.jsの型定義~ | 吉井 健文 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/483996937X/](https://www.amazon.co.jp/dp/483996937X/ "実践TypeScript ~ BFFとNext.js&Nuxt.jsの型定義~ | 吉井 健文 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2019年6月26日発売
TypeSctiptとNext.js、Nuxt.jsについての書籍


----
