---
title: "2017-05-22のJS: Safari TP 30、Polymer 2.0とBower、Create React App 1.0.0"
author: "azu"
layout: post
date : 2017-05-22T10:59:03.315Z
category: JSer
tags:
- Safari
- Polymer
- Bower
- React

---

JSer.info #332 - [Safari Technology Preview Release 30](https://webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/ "Safari Technology Preview Release 30")がリリースされました。

[Subresource Integrity](https://www.w3.org/TR/SRI/ "Subresource Integrity")(SRI)のサポート、`X-Content-Type-Options:nosniff`がサポートされました。

- [How to implement SRI in your build process ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/04/how-to-implement-sri-into-your-build-process/ "How to implement SRI in your build process ★ Mozilla Hacks – the Web developer blog")
- [X-Content-Type-Options: nosniff · Issue #2758 · Fyrd/caniuse](https://github.com/Fyrd/caniuse/issues/2758 "X-Content-Type-Options: nosniff · Issue #2758 · Fyrd/caniuse")
  - Firefoxも[50でサポート](http://mozsec-jp.hatenablog.jp/entry/2016/08/29/222740)したので主要ブラウザの`nosniff`サポートが揃った

また、Promiseの`rejectionhandled`と`unhandledrejection`のイベントサポートされています。

----

[Polymer 2.0.0](https://github.com/Polymer/polymer/releases/tag/v2.0.0 "2.0.0")と[polymer-cli 1.0.0](https://github.com/Polymer/polymer-cli "polymer-cli")がリリースされました。
ES2015のクラスベースで書けるようになり、Dirty checkingをopt-outする手段が用意され、1.xとの互換レイヤーなども提供されています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/tKvNeNGmOtU" frameborder="0" allowfullscreen></iframe>

- [Time for 2.0 - Polymer Project](https://www.polymer-project.org/blog/2017-05-15-time-for-two "Time for 2.0 - Polymer Project")
- [What's new in 2.0 - Polymer Project](https://www.polymer-project.org/2.0/docs/about_20 "What&#39;s new in 2.0 - Polymer Project")

1.xからのマイグレーションについては次のドキュメントにまとめられています。

- [Polymer 2.0 upgrade guide - Polymer Project](https://www.polymer-project.org/2.0/docs/upgrade "Polymer 2.0 upgrade guide - Polymer Project")

また、Polymerをインストールする方法として[Bower](https://bower.io/ "Bower")を使う方法が公式となっています。
([polymer-cli](https://github.com/Polymer/polymer-cli "polymer-cli")もBowerをベースにしている)

- [Install Polymer 2.x - Polymer Project](https://www.polymer-project.org/2.0/start/install-2-0 "Install Polymer 2.x - Polymer Project")

しかし、数日前にBowerは正式に非推奨となりました。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Bower is deprecated. <a href="https://t.co/XkIxOKhfBc">pic.twitter.com/XkIxOKhfBc</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/866085257052798976">May 21, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

- [Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower](https://github.com/bower/bower/pull/2458 "Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower")

そのため、Polymerもnpm/yarnサポートへと移行中です。

```
philipahlberg 5:52 PM
Hi everyone, with Bower being depreciated and pointing to Yarn now, should an issue be filed for the Polymer CLI to make the switch at some point in the future?

fresnizky 7:47 PM
@philipahlberg I think they're​ already working on it.
 https://github.com/Polymer/polymer/issues/3903#issuecomment-279180914
```

- Polymerのslackより <https://polymer.slack.com/archives/C03PF4L4L/p1495270338490522>

次のIssueでnpmサポートについて議論されていて、現在[@polymer/polymer](https://www.npmjs.com/package/@polymer/polymer "@polymer/polymer")がα版として公開されています。

- [Polymer on NPM stuck on version 1.2.5 · Issue #3903 · Polymer/polymer](https://github.com/Polymer/polymer/issues/3903#issuecomment-279180914 "Polymer on NPM stuck on version 1.2.5 · Issue #3903 · Polymer/polymer")

----

ReactのScaffoldingツールであるCreate React App 1.0がリリースされました。

webpack 2、ランタイムエラーの表示、Service Workerの対応、Jest 20、Dynamic importを使ったコード分割などさまざまな変更が含まれています。

- [What's New in Create React App - React Blog](https://facebook.github.io/react/blog/2017/05/18/whats-new-in-create-react-app.html "What&#39;s New in Create React App - React Blog")

0.9.5からのマイグレーション方法については次のリリースノートに書かれています。

- [Release v1.0.0 · facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app/releases/tag/v1.0.0 "Release v1.0.0 · facebookincubator/create-react-app")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 30 | WebKit
[webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/](https://webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/ "Release Notes for Safari Technology Preview 30 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 30リリース。
Subresource Integrity(SRI)、`X-Content-Type-Options:nosniff`に対応、PromiseのUnhandled rejectionのイベントをサポート。
`document.cookie`のアクセスを厳密化、WAI-ARIA周りの修正など


----

## Time for 2.0 - Polymer Project
[www.polymer-project.org/blog/2017-05-15-time-for-two](https://www.polymer-project.org/blog/2017-05-15-time-for-two "Time for 2.0 - Polymer Project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 2.0リリース。
クラスベースで書けるように、Polymer CLIも併せてメジャーアップデートされた

- [Release Stable Release 2.0.0 · Polymer/polymer](https://github.com/Polymer/polymer/releases/tag/v2.0.0 "Release Stable Release 2.0.0 · Polymer/polymer")
- [What&#39;s new in 2.0 - Polymer Project](https://www.polymer-project.org/2.0/docs/about_20 "What&amp;#39;s new in 2.0 - Polymer Project")

----

## Release 7.0 “Coelestem adspicit lucem” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/7.0.0](https://github.com/postcss/autoprefixer/releases/tag/7.0.0 "Release 7.0 “Coelestem adspicit lucem” · postcss/autoprefixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Autoprefixer 7.0リリース。
PostCSS 6.0、Browserslist 2.0、caniuse-liteを利用するように。
Node.js 0.12のサポート終了、Grid Layoutのサポートをデフォルトではオフに、コードベースがCoffeeScriptからBabelへ移行など

- [Autoprefixer 7.0 and Browserslist 2.0 — Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/autoprefixer-7-browserslist-2-released "Autoprefixer 7.0 and Browserslist 2.0 — Martian Chronicles, Evil Martians’ team blog")

----

## ESLint v4.0.0-beta.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/05/eslint-v4.0.0-beta.0-released](http://eslint.org/blog/2017/05/eslint-v4.0.0-beta.0-released "ESLint v4.0.0-beta.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.0.0βリリース。

- [ESLint v4.0.0 の変更点まとめ - Qiita](http://qiita.com/mysticatea/items/3d01452d76ea6c943793 "ESLint v4.0.0 の変更点まとめ - Qiita")

----

## Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower
[github.com/bower/bower/pull/2458](https://github.com/bower/bower/pull/2458 "Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span></p>

Bowerが`npm deprecate`となり正式に非推奨となった。
メンテナンスは続けられるが、Bowerの将来に興味がある人はメールで連絡をくださいとのこと。

- [Consider deprecating Bower. · Issue #2298 · bower/bower](https://github.com/bower/bower/issues/2298#issuecomment-302792690 "Consider deprecating Bower. · Issue #2298 · bower/bower")

----

## Release v1.0.0 · facebookincubator/create-react-app
[github.com/facebookincubator/create-react-app/releases/tag/v1.0.0](https://github.com/facebookincubator/create-react-app/releases/tag/v1.0.0 "Release v1.0.0 · facebookincubator/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app v1.0.0リリース。
webpack 2、ランタイムエラーの表示、Service Workerの対応、Jest 20、Dynamic importを使ったコード分割など

- [What&#39;s New in Create React App - React Blog](https://facebook.github.io/react/blog/2017/05/18/whats-new-in-create-react-app.html "What&amp;#39;s New in Create React App - React Blog")

----
<h1 class="site-genre">アーティクル</h1>

----

## ZEIT – Next 3.0 Preview
[zeit.co/blog/next3-preview](https://zeit.co/blog/next3-preview "ZEIT – Next 3.0 Preview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">サーバー</span> <span class="jser-tag">ReleaseNote</span></p>

Next 3.0 プレビューリリース。
`next export`で静的なHTMLとして出力できるように、コンポーネントのdynamic importをサポートなど


----

## Developer Edition 54: New inspector and debugger features, MDN help in the netmonitor, and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/03/developer-edition-54-new-inspector-and-debugger-features/](https://hacks.mozilla.org/2017/03/developer-edition-54-new-inspector-and-debugger-features/ "Developer Edition 54: New inspector and debugger features, MDN help in the netmonitor, and more ★ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Firefox 54の開発者ツールの変更点紹介。
CSS Inspectの改善、Debuggerパネルで整形版が別タブで開けたり、ツールチップで変数の表示、Network PanelでMore Infoからヘルプへの移動、JSON Viewなど


----

## JavaScript のもう一つの「関数名」 —— name プロパティ - Qiita
[qiita.com/8x9/items/34272b59b5aa68e33256](http://qiita.com/8x9/items/34272b59b5aa68e33256 "JavaScript のもう一つの「関数名」 —— name プロパティ - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptのFunctionの`name`プロパティについて。
ES2015から無名関数やArrow Functionなど関数自体が名前を持ってなくても、変数宣言側の名前が`name`プロパティで参照できることや、`writable`属性の仕様についてなど


----

## The Many Faces of Functions in JavaScript - Bocoup
[bocoup.com/blog/the-many-faces-of-functions-in-javascript](https://bocoup.com/blog/the-many-faces-of-functions-in-javascript "The Many Faces of Functions in JavaScript - Bocoup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

JavaScriptの色々な"関数"についての解説


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## A Modern Front-End Workflow – Umar Hansa | Render 2017 - YouTube
[www.youtube.com/watch?v&#x3D;v5r\_n6Tq0uk](https://www.youtube.com/watch?v&#x3D;v5r_n6Tq0uk "A Modern Front-End Workflow – Umar Hansa | Render 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">video</span></p>

Chrome開発者ツールのTipsやデバッグワークフローについての発表動画


----

## The Future of Audio and Video on the Web (Google I/O '17) - YouTube
[www.youtube.com/watch?v&#x3D;z9unKFzAj1w](https://www.youtube.com/watch?v&#x3D;z9unKFzAj1w "The Future of Audio and Video on the Web (Google I/O '17) - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ProgressiveWebApp</span></p>

ウェブサイトにおける動画や音楽のPWA対応についての発表動画。
ServiceWorkerを使ったオフライン対応、回転とフルスクリーン、 Media Capabilitiesを使った再生判定、MediaSession APIでのカバー表示など

- [GoogleChrome/sample-media-pwa: A sample video-on-demand media Progressive Web App](https://github.com/GoogleChrome/sample-media-pwa "GoogleChrome/sample-media-pwa: A sample video-on-demand media Progressive Web App")
- [Customize Media Notifications and Handle Playlists  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/02/media-session "Customize Media Notifications and Handle Playlists  |  Web  |  Google Developers")
- [google/shaka-player: JavaScript player library / DASH client / MSE-EME player](https://github.com/google/shaka-player "google/shaka-player: JavaScript player library / DASH client / MSE-EME player")

----

## Web Performance: Leveraging the Metrics that Most Affect User Experience (Google I/O '17) - YouTube
[www.youtube.com/watch?v&#x3D;6Ljq-Jn-EgU&amp;index&#x3D;71&amp;list&#x3D;PLOU2XLYxmsIKC8eODk\_RNCWv3fBcLvMMy](https://www.youtube.com/watch?v&#x3D;6Ljq-Jn-EgU&amp;index&#x3D;71&amp;list&#x3D;PLOU2XLYxmsIKC8eODk_RNCWv3fBcLvMMy "Web Performance: Leveraging the Metrics that Most Affect User Experience (Google I/O '17) - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">video</span></p>

パフォーマンスとメトリクスについての発表動画。
ロード完了ではなくインタラクティブになった時間(TTI)を計測、Hero Elements。UXとメトリクス
Long Tasks(50ms)をPerformanceObserverで検出、操作の遅延の計測、改善のパターンについて

- [GoogleChrome/tti-polyfill: TTI polyfill](https://github.com/GoogleChrome/tti-polyfill "GoogleChrome/tti-polyfill: TTI polyfill")

----

## CSS Houdini- the bridge between CSS, JavaScript and the browser by Serg Hospodarets
[slides.com/malyw/houdini-codemotion#/](http://slides.com/malyw/houdini-codemotion#/ "CSS Houdini- the bridge between CSS, JavaScript and the browser by Serg Hospodarets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">slide</span></p>

CSS Houdiniについてのスライド。
CSS/JavaScript/ブラウザの連携、Workletについて


----

##  Google I/O 2017 - All Sessions - YouTube
[www.youtube.com/playlist?list&#x3D;PLOU2XLYxmsIKC8eODk\_RNCWv3fBcLvMMy](http://www.youtube.com/playlist?list&#x3D;PLOU2XLYxmsIKC8eODk_RNCWv3fBcLvMMy " Google I/O 2017 - All Sessions - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Google I/O 2017の動画まとめ


----

##  JSConf EU 2017 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshFmAPr65sU2O5WMs7\_CGjs\_](https://www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshFmAPr65sU2O5WMs7_CGjs_ " JSConf EU 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span> <span class="jser-tag">video</span></p>

JSConf EU 2017の動画一覧


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Don't Overcomplicate Javascript – Bits from Nikola Ristic ∞ ƒront-end ∆eveloper
[bits.ristic.io/dont-overcomplicate-javascript-0](https://bits.ristic.io/dont-overcomplicate-javascript-0 "Don't Overcomplicate Javascript – Bits from Nikola Ristic ∞ ƒront-end ∆eveloper")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">opinion</span></p>

JavaScriptにおけるカーゴカルトについての連載。よく理解しないでコードの習慣を持ち込むことは技術的負債や複雑性を持ち込む可能性があることについて。
ReduxにおけるActionの定数のパターンについて。`import * as Constants from "./constants"`の問題点についてなど


----

## HN PWA - Hacker News readers as Progressive Web Apps
[hnpwa.com/](https://hnpwa.com/ "HN PWA - Hacker News readers as Progressive Web Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">example</span></p>

Hacker Newsを色々なViewフレームワークで実装したまとめ。

- [Hacker News APIがTodoMVC的な場所になってる | Web Scratch](http://efcl.info/2014/10/11/hackernews-api/ "Hacker News APIがTodoMVC的な場所になってる | Web Scratch")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## diegomura/react-pdf: Create PDF files using React
[github.com/diegomura/react-pdf](https://github.com/diegomura/react-pdf "diegomura/react-pdf: Create PDF files using React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">PDF</span> <span class="jser-tag">library</span></p>

Reactコンポーネントとしてレイアウトなどを書きPDFを生成するライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Complete Redux Book by Ilya Gelman et al. \[PDF/iPad/Kindle\]
[leanpub.com/redux-book](https://leanpub.com/redux-book "Complete Redux Book by Ilya Gelman et al. \[PDF/iPad/Kindle\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">book</span></p>

Reduxについての電子書籍


----
