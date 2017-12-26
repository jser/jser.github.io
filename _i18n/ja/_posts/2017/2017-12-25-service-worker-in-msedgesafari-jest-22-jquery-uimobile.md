---
title: "2017-12-26のJS: Service Worker in MSEdge/Safari、Jest 22、jQuery UIとMobileの統合"
author: "azu"
layout: post
date : 2017-12-26T09:55:06.473Z
category: JSer
tags:
- ServiceWorker
- jest
- jQuery

---

JSer.info #363 - MSEdge(Insider build)とSafari(Technology Preview)でそれぞれService Workerが実装されたことについてのブログが公開されました。

- [Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/)
- [Release Notes for Safari Technology Preview 46 | WebKit](https://webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/)

これによりモダンブラウザにはService Workerが実装されることになります。

<p class="ciu_embed" data-feature="serviceworkers" data-periods="future_1,current,past_1,past_2">
  <a href="http://caniuse.com/#feat=serviceworkers">Can I Use serviceworkers?</a> Data on support for the serviceworkers feature across the major browsers from caniuse.com.
</p>

MSEdgeとSafariどちらもまだ実験的なビルドでの公開なので、正常に動かないケースもあるようです。
その場合はそれぞれのIssue Trackerに報告することが推奨されています。

- MSEdge: [Microsoft Edge issue tracker - Microsoft Edge Development](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/?page=1&q=Service%20Worker "Microsoft Edge issue tracker - Microsoft Edge Development")
- Safari: [Bug List](https://bugs.webkit.org/buglist.cgi?quicksearch=Service%20Worker "Bug List")

----

Jest 22がリリースされました。

- [Jest 22: Refinements & Custom Runners · Jest](http://facebook.github.io/jest/blog/2017/12/18/jest-22.html "Jest 22: Refinements &amp; Custom Runners · Jest")


Node.js 4のサポート終了、Custom Runnerのコアとなる[jest-worker](https://github.com/facebook/jest/tree/master/packages/jest-worker "jest-worker")が公開されました。
Jestは元々[node-worker-farm](https://github.com/rvagg/node-worker-farm "node-worker-farm")を使い、テストの並列実行を行っていましたが、その役目を[jest-worker](https://github.com/facebook/jest/tree/master/packages/jest-worker "jest-worker")に置き換えていました。

- [Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest](https://github.com/facebook/jest/pull/4497 "Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest")

そして、Jestを並列実行処理の基盤として使えるCustom RunnerがJest 22で正式に公開されています。
これにより、Jestの上で[jest-runner-mocha](https://github.com/rogeliog/jest-runner-mocha "jest-runner-mocha")や[jest-runner-eslint](https://github.com/jest-community/jest-runner-eslint "jest-runner-eslint")のように別のテストフレームワークやLint処理などを並列実行できるようになっています。

詳しくは次の動画を見てください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/NtjyeojAOBs" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>

またテスト結果のフォーマッタの変更、`--detectLeaks`の追加、Babel 7のサポートなどが行われています。

----

[The Future of jQuery UI and jQuery Mobile | jQuery UI Blog](http://blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/ "The Future of jQuery UI and jQuery Mobile | jQuery UI Blog")では、jQuery UIとjQuery Mobileのプロジェクト統合について書かれています。

[jquery-mobile](https://github.com/jquery/jquery-mobile "jquery-mobile")は[jquery-ui](https://github.com/jquery/jquery-ui "jquery-ui")に依存していますが、今までチームやリポジトリは別々にありました。
今回、[@scottgonzalez](https://github.com/scottgonzalez "scottgonzalez")がjQuery UIプロジェクトのリーダを辞めることになり、現在jQuery Mobileのプロジェクトリーダである[@arschmitz](https://github.com/arschmitz "arschmitz")がjQuery UIプロジェクトも見ることになりました。
jQuery MobileはUIに依存しているため、重複や無駄を避けるために2つのプロジェクトを統合したチームにしていく方針について書かれています。

また合わせて協力者を募集するため<https://jqueryui-dev.slack.com/>のslackチームを作り、意見を募集しています。
(<http://bit.ly/2Btf6pu>からslackチームにjoinできる)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Notes for Safari Technology Preview 46 | WebKit
[webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/](https://webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/ "Release Notes for Safari Technology Preview 46 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">ServiceWorker</span></p>

Safari Technology Preview Release 46リリース。
Service Workerがデフォルトで有効化、`--useBigInt`フラグつきBigIntの実装、`img`要素の`decoding`属性のサポートなど


----

## V8 JavaScript Engine: V8 release v6.4
[v8project.blogspot.com/2017/12/v8-release-64.html](https://v8project.blogspot.com/2017/12/v8-release-64.html "V8 JavaScript Engine: V8 release v6.4")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.4リリース。
パフォーマンス、メモリ使用量の改善。named captureなどの正規表現Proposalの実装と有効化、`import.meta.url`のサポートなど


----

## Release Webpack-CLI V.2.0.0 · webpack/webpack-cli
[github.com/webpack/webpack-cli/releases/tag/v.2.0.0](https://github.com/webpack/webpack-cli/releases/tag/v.2.0.0 "Release Webpack-CLI V.2.0.0 · webpack/webpack-cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack-cli 2.0.0リリース。
`add`コマンド、`serve`コマンドの追加など


----

## Release v2.0.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v2.0.0](https://github.com/karma-runner/karma/releases/tag/v2.0.0 "Release v2.0.0 · karma-runner/karma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma v2.0.0リリース。
Node.js 4未満のサポート終了、エラー表示の改善など


----

## ESLint v4.14.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/12/eslint-v4.14.0-released](https://eslint.org/blog/2017/12/eslint-v4.14.0-released "ESLint v4.14.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.14.0リリース。
パーサ向けにScope解析のhookポイントが追加された。


----

## Jest 22: Refinements & Custom Runners · Jest
[facebook.github.io/jest/blog/2017/12/18/jest-22.html](http://facebook.github.io/jest/blog/2017/12/18/jest-22.html "Jest 22: Refinements & Custom Runners · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 22リリース。
Node.js 4のサポート終了、カスタムRunnerのコアとなる`jest-worker`の公開。
テスト結果のフォーマッタの変更、`--detectLeaks`の追加、Babel 7のサポート、MITライセンスに変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## 【連載記事】JavaScriptでプログラミングを学ぶ　その1：基礎と文法
[sbfl.net/blog/2017/12/14/javascript-programming-1/](https://sbfl.net/blog/2017/12/14/javascript-programming-1/ "【連載記事】JavaScriptでプログラミングを学ぶ　その1：基礎と文法")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

プログラミングを学んだことない人向けのJavaScript入門連載。


----

## Use a Render Prop! – componentDidBlog
[cdb.reacttraining.com/use-a-render-prop-50de598f11ce](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce "Use a Render Prop! – componentDidBlog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Reactの子コンポーネントと値やロジックを共有するパターンとしてのrender propsについて

- [Add doc about Render Props by mjackson · Pull Request #355 · reactjs/reactjs.org](https://github.com/reactjs/reactjs.org/pull/355 "Add doc about Render Props by mjackson · Pull Request #355 · reactjs/reactjs.org")

----

## React 🎄
[react.holiday/](https://react.holiday/ "React 🎄")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

アドベントカレンダー形式のReactチュートリアル


----

## Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/](https://blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/ "Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

MSEdgeのService Workerが実装された。
Service Workerの基本的な使い方やService Workerの制限について書かれている。


----

## The Future of jQuery UI and jQuery Mobile | jQuery UI Blog
[blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/](http://blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/ "The Future of jQuery UI and jQuery Mobile | jQuery UI Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">mobile</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

jQuery MobileはjQuery UIに依存しているが、今までは別々のチーム/リポジトリとなっていた。
重複などの無駄があるため、チームを統合し、停滞しているプロジェクトを改善していく指針が公開された。
あわせてSlackチャンネルを開設して協力者を募集している。


----

## Preloading modules  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/12/modulepreload](https://developers.google.com/web/updates/2017/12/modulepreload "Preloading modules  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

`<link rel="modulepreload">`について。
`<link rel="preload">`との違い、モジュールの依存関係はフラットにすべてのファイルを定義するべきかについて


----

## Idiomatic Redux: Using Reselect Selectors for Encapsulation and Performance · Mark's Dev Blog
[blog.isquaredsoftware.com/2017/12/idiomatic-redux-using-reselect-selectors/](http://blog.isquaredsoftware.com/2017/12/idiomatic-redux-using-reselect-selectors/ "Idiomatic Redux: Using Reselect Selectors for Encapsulation and Performance · Mark's Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">React</span></p>

reselectを使ったパフォーマンスの最適化について。
reselectはstateからstateを作るライブラリで、入力に対してメモ化が行われている。
これを使いReduxのstateからアプリケーションに適切な形へstateを変換させる例について紹介している


----

## ES6 Modules のエラー処理を決定的(deterministic)にした話 - Google ドキュメント
[docs.google.com/document/d/1Wuc2LVLb2Ii-itnA4sKw\_KndJGvZ4mvdfw0POm5qcs4/edit#](https://docs.google.com/document/d/1Wuc2LVLb2Ii-itnA4sKw_KndJGvZ4mvdfw0POm5qcs4/edit# "ES6 Modules のエラー処理を決定的(deterministic)にした話 - Google ドキュメント")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">module</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">article</span> <span class="jser-tag">ECMAScript</span></p>

ES Modules(仕様)のエラーがネットワークに依存したものとなっていて、毎回異なるエラーになる問題があった。
エラーが毎回同じ結果となるように、仕様をどのように修正していったかについて。


----

## ブラウザのしくみ: データ構造とアルゴリズムと雰囲気で理解する DOM と Shadow DOM — hayato.io
[hayato.io/2017/dom/](https://hayato.io/2017/dom/ "ブラウザのしくみ: データ構造とアルゴリズムと雰囲気で理解する DOM と Shadow DOM — hayato.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">WebComponents</span></p>

DOMやShadow DOMの構造や実装についての解説記事。
Shadow DOMの登場によってDOMはツリーのツリー(Super Tree)となっている。
その場合におけるCSSセレクタのマッチングやイベントパスについてなどをChromeの実装と合わせて解説している。


----

## Lint the Web Forward With Sonarwhal ◆ 24 ways
[24ways.org/2017/lint-the-web-forward-with-sonarwhal/](https://24ways.org/2017/lint-the-web-forward-with-sonarwhal/ "Lint the Web Forward With Sonarwhal ◆ 24 ways")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">web </span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Sonarwhalを使ったウェブサイトのLintについての記事。
Sonarwhalの基本的な使い方や設定について解説している


----

## Testing Angular 2 and Continuous Integration with Jest - Semaphore
[semaphoreci.com/community/tutorials/testing-angular-2-and-continuous-integration-with-jest](https://semaphoreci.com/community/tutorials/testing-angular-2-and-continuous-integration-with-jest "Testing Angular 2 and Continuous Integration with Jest - Semaphore")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Angular</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jestを使ったAngularのテストについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## 日経電子版 サイト高速化とPWA対応 / nikkei-high-performance-pwa // Speaker Deck
[speakerdeck.com/sisidovski/nikkei-high-performance-pwa](https://speakerdeck.com/sisidovski/nikkei-high-performance-pwa "日経電子版 サイト高速化とPWA対応 / nikkei-high-performance-pwa // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">slide</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

ウェブサイトのパフォーマンス改善についてのスライド。
アセットの配信の最適化、Resource Hintsでのpreload。
SpeedCurveを使ってのモニタリングやファイルサイズのチェック。
Service Workerでのキャッシュやデバッグなどについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## amsul/react-performance: Helpers to debug and record component render performance 🚀
[github.com/amsul/react-performance](https://github.com/amsul/react-performance "amsul/react-performance: Helpers to debug and record component render performance 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

React 16で動く`react-addons-perf`のようなものを目指すライブラリ。
Reactコンポーネントのプロファイルを取れるライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## Responsively Retrofitting: Retrofitting Web Sites with HTML5 and CSS3: Christopher Schmitt: 9781449364205: Amazon.com: Books
[www.amazon.com/Responsively-Retrofitting-Sites-HTML5-CSS3/dp/1449364209](https://www.amazon.com/Responsively-Retrofitting-Sites-HTML5-CSS3/dp/1449364209 "Responsively Retrofitting: Retrofitting Web Sites with HTML5 and CSS3: Christopher Schmitt: 9781449364205: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">book</span></p>

2018年8月25日発売
既存のレガシーなウェブサイトをモバイル向けにリニューアルする方法についてを扱う書籍


----
