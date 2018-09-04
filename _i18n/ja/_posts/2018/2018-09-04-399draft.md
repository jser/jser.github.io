---
title: "2018-09-04のJS: Browser Interoperability、Mobile Form Design、400回記念イベントページ公開"
author: "azu"
layout: post
date : 2018-09-04T02:19:41.829Z
category: JSer
tags:
- browser
- Mobile
- form

---

JSer.info #399 - [Chromium Blog: Charting Browser Interoperability](https://blog.chromium.org/2018/08/charting-browser-interoperability.html)という記事では、ブラウザのWeb APIの相互運用性などについて見られる[Web API Confluence Dashboard](https://web-confluence.appspot.com/#!/)についての紹介がされています。

それぞれのブラウザ固有のAPIの数やその固有のAPIがどの程度削除されているか。
またブラウザごとにAPIが実装されているかを一覧するといった、ウェブブラウザの相互運用性をチェックできるダッシュボードについて紹介されています。

またそれらのAPIをどのような仕組みで収集しているかのアルゴリズムについても解説されているので、クロスブラウザに興味がある人は見てみると面白いかもしれません。

- [confluence/CatalogDataCollection.md at master · GoogleChromeLabs/confluence](https://github.com/GoogleChromeLabs/confluence/blob/master/CatalogDataCollection.md#detailed-algorithm)

----

[Best Practices For Mobile Form Design — Smashing Magazine](https://www.smashingmagazine.com/2018/08/best-practices-for-mobile-form-design/)という記事では、モバイルのブラウザにおいてのフォームデザインについて幅広いプラクティスがまとめられています。

フォームの複雜さや入力のコストについて書かれていて、それぞれのフィールドの種類ごとによくないやり方とよいやり方についてを紹介しています。
Touchに考慮したデザインや具体的な事例、バリデーション、アクセシビリティなど幅広い項目について書かれています。


----

## お知らせ

[2018年9月22日(土)に JSer.info 400回目記念イベントを開催します - JSer.info](https://jser.info/2018/08/31/jser-400-event-announce/)で紹介しましたが、イベント参加の募集を開始しています。

次のページから参加、発表などで申し込みできます。

- [JSer.info 400回記念イベント - connpass](https://jser.connpass.com/event/100092/)

発表枠がまだまだありそうなので、JavaScriptに関して(ウェブでもOK)の発表したい方を募集しています。すごい抽象的なテーマなので、前々から話したかったけど普段のイベントだとテーマが合わないから保留していたというようなものも歓迎しています。
（毎年発表内容はJavaScriptに関係しそうというぐらいであとはバラバラです）

また、参加する人もJavaScript Discussionという質問をベースにしたDiscussionを行うコーナーで聞きたいことなどについての質問を事前に用意しておくといいです。
YES/NOの答えがあるものから、答えがないものまで質問は自由です。（大体いいね順で上から進めていくので、意図が分かりやすい質問文を考えておくとよいです）

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 64 | WebKit
[webkit.org/blog/8406/release-notes-for-safari-technology-preview-64/](https://webkit.org/blog/8406/release-notes-for-safari-technology-preview-64/ "Release Notes for Safari Technology Preview 64 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 64リリース。
WebWorkerの`name`オプションをサポート、Safari Push Notificationsでパーミッションを要求するのはユーザージェスチャ起因じゃないとできなくなるなど


----

## Chromium Blog: Charting Browser Interoperability
[blog.chromium.org/2018/08/charting-browser-interoperability.html](https://blog.chromium.org/2018/08/charting-browser-interoperability.html "Chromium Blog: Charting Browser Interoperability")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

ブラウザのAPIに関するinteroperabilityについての記事
ブラウザ固有のAPIの数、削除されているAPIの数などのデータの見方。
またそれらのAPIをどのように集めているかについてなど

- [Web API Confluence Dashboard](https://web-confluence.appspot.com/#!/ "Web API Confluence Dashboard")

----

## Release v3.5.0 · fuse-box/fuse-box
[github.com/fuse-box/fuse-box/releases/tag/v3.5.0](https://github.com/fuse-box/fuse-box/releases/tag/v3.5.0 "Release v3.5.0 · fuse-box/fuse-box")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

FuseBox 3.5.0リリース。
targetに`npm-server`, `npm-browser`, `npm-universal`を追加など


----

## Release v0.80.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.80.0](https://github.com/facebook/flow/releases/tag/v0.80.0 "Release v0.80.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.80.0リリース。
Flow lintのseverity算出の仕組みの変更、いつくかのlibdefの型を変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## What's New In DevTools (Chrome 70)  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/08/devtools](https://developers.google.com/web/updates/2018/08/devtools "What's New In DevTools (Chrome 70)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 70の開発者ツールの変更点について。
Live Expressions、ネットワークスロットリングをコマンドメニューから選択できるように、AudioContextに関するEvent Listener BreakPointのサポートなど


----

## Best Practices For Mobile Form Design — Smashing Magazine
[www.smashingmagazine.com/2018/08/best-practices-for-mobile-form-design/](https://www.smashingmagazine.com/2018/08/best-practices-for-mobile-form-design/ "Best Practices For Mobile Form Design — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mobile</span> <span class="jser-tag">design</span> <span class="jser-tag">article</span></p>

モバイルでのフォームのデザインについての記事。
ラベルの置き方、フィールドのサイズ、確認項目、パスワードの表示、フィールドの分割、選択肢の置き方、アクセシビリティについてなど


----

## Introducing F2 – Sima – Medium
[medium.com/@SimaZwx/https-medium-com-simazwx-introducing-f2-c44fb4e74c2d](https://medium.com/@SimaZwx/https-medium-com-simazwx-introducing-f2-c44fb4e74c2d "Introducing F2 – Sima – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">グラフ</span> <span class="jser-tag">library</span> <span class="jser-tag">mobile</span> <span class="jser-tag">article</span></p>

モバイル向けに作られたインタラクティブグラフライブラリのF2について。

- [antvis/f2: 📱📈An elegant, interactive and flexible charting library for mobile.](https://github.com/antvis/f2/ "antvis/f2: 📱📈An elegant, interactive and flexible charting library for mobile.")

----

## Using the React DevTools Profiler to Diagnose React App Performance Issues | Netlify
[www.netlify.com/blog/2018/08/29/using-the-react-devtools-profiler-to-diagnose-react-app-performance-issues/](https://www.netlify.com/blog/2018/08/29/using-the-react-devtools-profiler-to-diagnose-react-app-performance-issues/ "Using the React DevTools Profiler to Diagnose React App Performance Issues | Netlify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Reactの新しい開発者ツールのProfierを使ったパフォーマンスの問題の見つけ方について。
React Renderのcommits回数が多い問題を見つけて、debounceでcommitを減らすようにした話


----

## マイクロサービス/API時代のフロントエンド開発 - ＠IT
[www.atmarkit.co.jp/ait/series/9324/](http://www.atmarkit.co.jp/ait/series/9324/ "マイクロサービス/API時代のフロントエンド開発 - ＠IT")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">BFF</span> <span class="jser-tag">server</span> <span class="jser-tag">API</span> <span class="jser-tag">article</span></p>

BFF（Backends For Frontends）についての連載記事。
UIのためAPIサーバであるBFFの役割、ユースケース、アンチパターンについてなど


----

## Array.prototype.sort について | メモログ
[memolog.org/2018/about-array-prototype-sort.html](https://memolog.org/2018/about-array-prototype-sort.html "Array.prototype.sort について | メモログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

各ブラウザのJavaScriptエンジンのsotの実装について。 仕様では安定ソートを保証しないが、大体が安定ソートになっていっている。
V8はV8 7.0/Chrome 70でTimesortになる。

- [Mathias Bynens on Twitter: &quot;Array.prototype.sort is now stable in @v8js v7.0 / Chrome 70! 🎉 Previously, V8 used an unstable QuickSort for arrays with more than 10 elements. Now, we use the stable TimSort algorithm. Demo: https://t.co/X3Y1psd7IM… https://t.co/LhPEE15hA0&quot;](https://twitter.com/mathias/status/1036626116654637057 "Mathias Bynens on Twitter: &amp;quot;Array.prototype.sort is now stable in @v8js v7.0 / Chrome 70! 🎉 Previously, V8 used an unstable QuickSort for arrays with more than 10 elements. Now, we use the stable TimSort algorithm. Demo: https://t.co/X3Y1psd7IM… https://t.co/LhPEE15hA0&amp;quot;")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## TypeScript導入で得られる「変えていく勇気」 / The courage to change by TypeScript - Speaker Deck
[speakerdeck.com/okunokentaro/the-courage-to-change-by-typescript](https://speakerdeck.com/okunokentaro/the-courage-to-change-by-typescript "TypeScript導入で得られる「変えていく勇気」 / The courage to change by TypeScript - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">slide</span></p>

TypeScriptを使ったアプリケーション開発についてのスライド。
今のTypeScriptでは型定義ファイルの管理方法、途中から導入するための手段などが整備されている点について。
また型を活用したリファクタリングを行いやすいアーキテクチャについてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## dy/font-measure: Compute font metrics such as x-height, cap height, ascent, descent and tittle for any web font.
[github.com/dy/font-measure](https://github.com/dy/font-measure "dy/font-measure: Compute font metrics such as x-height, cap height, ascent, descent and tittle for any web font.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

font familyを指定すると、そのfontのメトリクス情報を返してくれるライブラリ。 Canvasを使い計測している


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## UpperCod/Atomico: 🔥 A small library to work with web components
[github.com/uppercod/atomico](https://github.com/uppercod/atomico "UpperCod/Atomico: 🔥 A small library to work with web components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">jsx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JSXをサポートしたWebComponentを作成するライブラリ。
Custom ElementにReactライクなライフサイクルイベントを追加している


----
<h1 class="site-genre">書籍関係</h1>

----

## WebGL Insights 日本語版 - アスキードワンゴ
[asciidwango.jp/post/176833750840/webgl-insights-%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88](https://asciidwango.jp/post/176833750840/webgl-insights-%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88 "WebGL Insights 日本語版 - アスキードワンゴ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">book</span></p>

2018年8月24日発売
WebGL Insightsの翻訳本

- [ WebGL Insights ](http://www.webglinsights.com/ " WebGL Insights ")

----
