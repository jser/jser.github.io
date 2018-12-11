---
title: "2018-12-11のJS: gulp 4が正式リリース、MSEdgeがChromiumベースに移行"
author: "azu"
layout: post
date : 2018-12-11T00:22:12.068Z
category: JSer
tags:
- gulpjs
- MSEdge
- Chromium

---

JSer.info #413 - gulp 4.0が正式にリリースされました。

- [🎉 Version 4.0 Now Default 🎉 – gulpjs – Medium](https://medium.com/gulpjs/version-4-now-default-92c6cd4beb45)

今まではプレリリース扱いだったので`npm install gulp@next`でないとインストールされませんでしたが、現在は`npm install gulp`で4.0がインストールされるようになっています。

`gulp.series`、`gulp.parallel`、`gulp.lastRun`、`gulp.symlink`などのAPIが追加されています。
sourcemapsのデフォルトサポート、gulpfileからのmodule exportをタスクとして扱えるようなっています。

または破壊的な変更として、`gulp`と`gulp-cli`の分離、`gulp.task`や`gulp.watch`の引数の変更などが行われています。

3.xからの公式なマイグレーションガイドはまだありませんが、すでにいくつか記事が書かれているのでそれらを見てみるとよいかもしれません。

- [\[Docs\] Migration Guide · Issue #861 · gulpjs/gulp](https://github.com/gulpjs/gulp/issues/861)
- [gulp v4.0.0がプレリリース！ 移行方法と変更点まとめ - satoyan419.com](https://satoyan419.com/gulp-v4/ "gulp v4.0.0がプレリリース！ 移行方法と変更点まとめ - satoyan419.com")
- [How do I update to Gulp 4? - Liquid Light](https://www.liquidlight.co.uk/blog/article/how-do-i-update-to-gulp-4/ "How do I update to Gulp 4? - Liquid Light")
- [The Complete-Ish Guide to Upgrading to Gulp 4 | Joe Zim's JavaScript Corner](https://www.joezimjs.com/javascript/complete-guide-upgrading-gulp-4/ "The Complete-Ish Guide to Upgrading to Gulp 4 | Joe Zim's JavaScript Corner")

----

Microsoftは、[Microsoft Edge](https://www.microsoft.com/windows/microsoft-edge)(MSEdge)を[Chromium](https://www.chromium.org/Home)ベースへと移行することを発表しました。
現在のMSEdgeはレンダリングエンジンであるEdgeHTMLとJavaScriptエンジンである[ChakraCore](https://github.com/Microsoft/ChakraCore)を利用しています。
これをChromiumのレンダリングエンジンである[Blink](https://www.chromium.org/blink)とJavaScriptエンジンである[V8](https://v8.dev/)へ移行することを表明しています。

- [Microsoft Edge: Making the web better through more open source collaboration - Windows Experience BlogWindows Experience Blog](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/#5yeIh988gX4mFiRU.97)
- [MicrosoftEdge/MSEdge: Microsoft Edge](https://github.com/MicrosoftEdge/MSEdge "MicrosoftEdge/MSEdge: Microsoft Edge")
- [MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team](https://github.com/MicrosoftEdge/MSEdgeExplainers "MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team")

MSEdgeというブラウザ自体(ブランド)は維持されますが、中身がChromeと同じ[Chromium](https://www.chromium.org/Home)ベースへ移行されます。
この移行によってWindows7, 8を含めたすべてのサポートバージョンのWindowsとmacOSなどの他のプラットフォームをサポートする予定です。

新しいMSEdgeはChakraCoreは利用しない予定ですが、ChakraCore自体はブラウザ以外でも利用されているためサポートを継続するとの発表もしています。

- [Chromium adoption in Microsoft Edge and future of ChakraCore · Issue #5865 · Microsoft/ChakraCore](https://github.com/Microsoft/ChakraCore/issues/5865)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## New in Chrome 71  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/12/nic71](https://developers.google.com/web/updates/2018/12/nic71 "New in Chrome 71  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 71の変更点について。
`Intl.RelativeTimeFormat()`のサポート、`text-underline-position`のサポート。
Fetch APIのcredentials-modeのデフォルト値が`omit`から`same-origin`へと変更など


----

## 7.2.0 Released: Private Instance Methods · Babel
[babeljs.io/blog/2018/12/03/7.2.0.html](https://babeljs.io/blog/2018/12/03/7.2.0.html "7.2.0 Released: Private Instance Methods · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7.2.0リリース。
Private methods proposalのサポート、pipeline operator proposalのパースをサポート、replで変換過程を見られるタイムトラベルをサポートなど


----

## Release Notes for Safari Technology Preview 71 | WebKit
[webkit.org/blog/8517/release-notes-for-safari-technology-preview-71/](https://webkit.org/blog/8517/release-notes-for-safari-technology-preview-71/ "Release Notes for Safari Technology Preview 71 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 71リリース。
`supported-color-schemes`のサポート、Intersection Observerの有効化、Web Authenticationの試験的サポートなど


----

## Release 8.4.0 · developit/preact
[github.com/developit/preact/releases/tag/8.4.0](https://github.com/developit/preact/releases/tag/8.4.0 "Release 8.4.0 · developit/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 8.4.0リリース。
TypeScriptの型定義を改善、パフォーマンスの改善など。
また次期メジャーバージョンのPreact Xについて書かれている


----

## Microsoft Edge: Making the web better through more open source collaboration - Windows Experience BlogWindows Experience Blog
[blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/ "Microsoft Edge: Making the web better through more open source collaboration - Windows Experience BlogWindows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">news</span></p>

デスクトップMSEdgeはChromiumベース(Blink+V8)に移行し、すべてのWindowsバージョンやmacOS向けなどへ提供予定。
JavaScriptエンジンのChakraCoreはEdge以外の利用のためサポートを続ける。

- [MicrosoftEdge/MSEdge: Microsoft Edge](https://github.com/MicrosoftEdge/MSEdge "MicrosoftEdge/MSEdge: Microsoft Edge")
- [Chromium adoption in Microsoft Edge and future of ChakraCore · Issue #5865 · Microsoft/ChakraCore](https://github.com/Microsoft/ChakraCore/issues/5865 "Chromium adoption in Microsoft Edge and future of ChakraCore · Issue #5865 · Microsoft/ChakraCore")
- [MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team](https://github.com/MicrosoftEdge/MSEdgeExplainers "MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team")

----

## puppeteer/experimental/puppeteer-firefox at master · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/tree/master/experimental/puppeteer-firefox](https://github.com/GoogleChrome/puppeteer/tree/master/experimental/puppeteer-firefox "puppeteer/experimental/puppeteer-firefox at master · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

PuppeteerのFirefox版


----

## Google Developers Blog: Flutter 1.0: Google’s Portable UI Toolkit
[developers.googleblog.com/2018/12/flutter-10-googles-portable-ui-toolkit.html](https://developers.googleblog.com/2018/12/flutter-10-googles-portable-ui-toolkit.html "Google Developers Blog: Flutter 1.0: Google’s Portable UI Toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">ReleaseNote</span></p>

Flutter 1.0リリース。
Hummingbirdというウェブ向けの出力対応予定について

- [Hummingbird: Building Flutter for the Web – Flutter – Medium](https://medium.com/flutter-io/hummingbird-building-flutter-for-the-web-e687c2a023a8 "Hummingbird: Building Flutter for the Web – Flutter – Medium")

----

## Processing.js 2008-2018
[blog.humphd.org/processing-js-2008/](https://blog.humphd.org/processing-js-2008/ "Processing.js 2008-2018")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

メンテンナンスモードであったProcessing.jsのリポジトリがアーカイブ化された。
またProcessing.jsの歴史について。後継ライブラリとしてはp5jsが開発されている。

- [processing-js/processing-js: A port of the Processing visualization language to JavaScript.](https://github.com/processing-js/processing-js/ "processing-js/processing-js: A port of the Processing visualization language to JavaScript.")

----

## Release v0.88.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.88.0](https://github.com/facebook/flow/releases/tag/v0.88.0 "Release v0.88.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.88.0リリース。
`Function`と`Object`を`any`のaliasとして扱うように。
`flow start --lazy-mode watchman`の追加、`flow config check`コマンドの追加など


----

## ESLint v5.10.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/12/eslint-v5.10.0-released](https://eslint.org/blog/2018/12/eslint-v5.10.0-released "ESLint v5.10.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 5.10.0リリース。
`padding-line-between-statements`にオプションの追加、
JSDoc関係のルールである`require-jsdoc`と`valid-jsdoc`が非推奨になるなど

- [ESLint v5.10.0 - Qiita](https://qiita.com/mysticatea/items/64a09c3bea4c06d84a2e "ESLint v5.10.0 - Qiita")

----

## 🎉 Version 4.0 Now Default 🎉 – gulpjs – Medium
[medium.com/gulpjs/version-4-now-default-92c6cd4beb45](https://medium.com/gulpjs/version-4-now-default-92c6cd4beb45 "🎉 Version 4.0 Now Default 🎉 – gulpjs – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">ReleaseNote</span></p>

gulp 4.0が正式リリース。
`gulp.series`と`gulp.parallel`を追加。
sourcemapsのデフォルトサポート、gulpfileからのexportをタスクとして扱えるように、`gulp`と`gulp-cli`の分離など

- [Release v4.0.0 · gulpjs/gulp](https://github.com/gulpjs/gulp/releases/tag/v4.0.0 "Release v4.0.0 · gulpjs/gulp")

----
<h1 class="site-genre">アーティクル</h1>

----

## jQueryへの依存を外す方法 - dely engineering blog
[tech.dely.jp/entry/2018/12/08/160000](https://tech.dely.jp/entry/2018/12/08/160000 "jQueryへの依存を外す方法 - dely engineering blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CoffeeScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">リファクタリング</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">article</span></p>

jQueryの依存を外すまでのフローについて。
polyfill.io の利用、CoffeeScriptからTypeScriptへの移行。
jQueryをVanillaJS + polyfillで動くように書き直し、BackstopJSでビジュアルリグレッションテストする方法について。


----

## Node.js Everywhere with Environment Variables! – Node.js Collection – Medium
[medium.com/the-node-js-collection/making-your-node-js-work-everywhere-with-environment-variables-2da8cdf6e786](https://medium.com/the-node-js-collection/making-your-node-js-work-everywhere-with-environment-variables-2da8cdf6e786 "Node.js Everywhere with Environment Variables! – Node.js Collection – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsでの環境変数の使い方、`.env`を使った環境変数の定義と読み込み方法についてなど


----

## Yahoo! JAPANでの生体認証の取り組み（FIDO2サーバーの仕組みについて） - Yahoo! JAPAN Tech Blog
[techblog.yahoo.co.jp/advent-calendar-2018/webauthn/](https://techblog.yahoo.co.jp/advent-calendar-2018/webauthn/ "Yahoo! JAPANでの生体認証の取り組み（FIDO2サーバーの仕組みについて） - Yahoo! JAPAN Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

WebAuthn（Web Authentication）を使った生体認証でのログインフローについての解説


----

## ヤフー株式会社におけるWebフロントエンドの技術選定 - Yahoo! JAPAN Tech Blog
[techblog.yahoo.co.jp/advent-calendar-2018/yahoo-frontend/](https://techblog.yahoo.co.jp/advent-calendar-2018/yahoo-frontend/ "ヤフー株式会社におけるWebフロントエンドの技術選定 - Yahoo! JAPAN Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">company</span> <span class="jser-tag">opinion</span></p>

ヤフー株式会社における各サービスごとのフロントエンドに利用しているフレームワークやライブラリなどについて。
それぞれの技術を選定した理由などについてもまとめられている。


----

## Performance Calendar » data-s(h)aver strategies
[calendar.perfplanet.com/2018/data-shaver-strategies/](https://calendar.perfplanet.com/2018/data-shaver-strategies/ "Performance Calendar » data-s(h)aver strategies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ブラウザのデータセーバーが有効かを判定し、それに対してどのようなコンテンツを返すかについて。
コンテンツ数の削減、自動再生の防止、解像度の低い画像の配信、データセーバーが有効になっていることの通知などについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Compare HAR files
[compare.sitespeed.io/](https://compare.sitespeed.io/ "Compare HAR files")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span></p>

HARファイル同士を比較できるウェブサービス。
それぞれのリソースロードのタイムライン比較、動画、ファイルサイズのDiffなどを出してくれる

- [Performance Calendar » Sharing is caring: What’s new with comparing HAR files?](https://calendar.perfplanet.com/2018/sharing-comparing-har-files/ "Performance Calendar » Sharing is caring: What’s new with comparing HAR files?")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## rowanmanning/proclaim: A simple assertion library for server and client side JavaScript.
[github.com/rowanmanning/proclaim](https://github.com/rowanmanning/proclaim "rowanmanning/proclaim: A simple assertion library for server and client side JavaScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

古いブラウザや古いNode.jsでも動作するように書かれたassert系ライブラリ。
chaiのようにassertの拡張メソッドも実装されている


----
