---
title: "2016-12-12のJS: Chrome 56β、Babelの過去と現在と未来"
author: azu
layout: post
date : 2016-12-12T10:14
category: JSer
tags:
    - Chrome
    - Firefox
    - Babel

---

JSer.info #309 - Chrome 56βがリリースされました。

- [Chromium Blog: Chrome 56 Beta: “Not Secure” warning, Web Bluetooth, and CSS position: sticky](https://blog.chromium.org/2016/12/chrome-56-beta-not-secure-warning-web.html "Chromium Blog: Chrome 56 Beta: “Not Secure” warning, Web Bluetooth, and CSS position: sticky")

CSS `position: sticky`の有効化、WebGL 2.0のサポート、FlashのClick to Playがデフォルト化、CSS Fontsの`system-ui`をサポート、SHA-1の対応終了などが含まれています。

HTML5 by default(いわゆるFlashのClick to playのデフォルト化)はChrome55で予定されていましたが、56からに変更されました。

- [Chromium Blog: Roll-out plan for HTML5 by Default](https://blog.chromium.org/2016/12/roll-out-plan-for-html5-by-default.html "Chromium Blog: Roll-out plan for HTML5 by Default")
- [Flash Roadmap - The Chromium Projects](https://sites.google.com/a/chromium.org/dev/flash-roadmap#TOC-HTML5-By-Default-Target:-Chrome-55---Dec-2016- "Flash Roadmap - The Chromium Projects")

同様の変更がFirefoxでも2017年中に行われる予定です。

- [Flash コンテンツは 2017 年中に「クリックして有効化」となります | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2016/flash-content-will-be-click-to-activate-in-2017/ "Flash コンテンツは 2017 年中に「クリックして有効化」となります | Firefox サイト互換性情報")

また、SHA-1証明書についてChromeは56で、Firefox 51(2017年1月リリース)、IE11とMSEdgeは2017年2月のリリースでそれぞれ無効化されます。

- [公的認証局によって発行された SHA-1 証明書は受け入れられなくなります (影響あり) | Firefox サイト互換性情報](https://www.fxsitecompat.com/ja/docs/2016/sha-1-certificates-issued-by-public-ca-will-no-longer-be-accepted/)
- [FAQ: SHA-1 廃止/SHA-2 移行に関するマイクロソフトのポリシー – 日本のセキュリティチーム](https://blogs.technet.microsoft.com/jpsecurity/2015/11/02/faq-sha-1-sha-2/)
- [Windows Enforcement of SHA1 Certificates - TechNet Articles - United States (English) - TechNet Wiki](http://social.technet.microsoft.com/wiki/contents/articles/32288.windows-enforcement-of-sha1-certificates.aspx)
- [Google Developers Japan: Chrome の SHA-1 証明書](https://googledevjp.blogspot.jp/2016/11/sha-1-certificates-in-chrome.html?m=1 "Google Developers Japan: Chrome の SHA-1 証明書")
- [MacOS & Safari SHA-1 deprecation policy ? | Apple Developer Forums](https://forums.developer.apple.com/thread/65399 "MacOS &amp; Safari SHA-1 deprecation policy ? | Apple Developer Forums")

SHA-1証明書のサポートが終了するとどうなるのかは、次のサイトがよくまとまっています。

- [SSLサーバー証明書 : SHA-1 証明書の受付終了と SHA-2 証明書への移行について｜Cybertrust.ne.jp](https://www.cybertrust.ne.jp/sureserver/productinfo/sha1ms.html "SSLサーバー証明書 : SHA-1 証明書の受付終了と SHA-2 証明書への移行について｜Cybertrust.ne.jp")

----

[The State of Babel · Babel](https://babeljs.io/blog/2016/12/07/the-state-of-babel "The State of Babel · Babel")では、Babelの歴史や現在、また今後のロードマップについて書かれています。

Babel版Autoprefixerである[babel-preset-env](https://github.com/babel/babel-preset-env "babel-preset-env")や、[babili](https://github.com/babel/babili "babili")のリリース。
プラグインエコシステムやドキュメントの整備や課題などについて書かれています。

また、今後のロードマップやBabelのコミュニティについて書かれています。

----

## お知らせ

JSer.infoの6周年イベントのイベントページを公開しました。
募集開始は2016/12/15(木) 21:00 〜 からとなっています(抽選)。

- [JSer.info 6周年と300回記念イベント - connpass](https://jser.connpass.com/event/46997/ "JSer.info 6周年と300回記念イベント - connpass")

また、5-20分の発表枠を設けています。
JavaScriptについて発表したいことがある人は「発表枠」で申し込んでください。
発表枠以外でも自由に発表できる時間はあるので、スライドを隠し持っていると良いです。

書記枠という変な枠もあります。
自分がいつもやっているような[アウトラインメモ](http://efcl.info/tags/?q=%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88)を[Etherpad](http://etherpad.org/ "Etherpad")などを使って書くのを手伝ってくれる人の枠です。
(司会業やってないときは自分もやります)
当日リアルタイムで見れるようにして、文書ベースのデータがあると議論/質疑がしやすくなるかを試したいので作りました。

募集開始は2016/12/15(木)からですが、気になる人は申し込んでみてください。

詳細は[2017年1月15日(日)に JSer.info 6周年 && 300回目記念イベント を開催します - JSer.info](https://jser.info/2016/12/13/announcement-jser-info-6years-event/ "2017年1月15日(日)に JSer.info 6周年 &amp;&amp; 300回目記念イベント を開催します - JSer.info")を見てください。
----
<h1 class="site-genre">ヘッドライン</h1>

----

## Chromium Blog: Chrome 56 Beta: “Not Secure” warning, Web Bluetooth, and CSS position: sticky
[blog.chromium.org/2016/12/chrome-56-beta-not-secure-warning-web.html](https://blog.chromium.org/2016/12/chrome-56-beta-not-secure-warning-web.html "Chromium Blog: Chrome 56 Beta: “Not Secure” warning, Web Bluetooth, and CSS position: sticky")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 56βリリース。
Web Bluetooth APIがデフォルトで有効化、CSS `position: sticky`の有効化、WebGL 2.0、FlashのClick to Playがデフォルト化、CSS Fontsの`system-ui`をサポート、SHA-1の対応終了など

- [Chromium Blog: Roll-out plan for HTML5 by Default](https://blog.chromium.org/2016/12/roll-out-plan-for-html5-by-default.html "Chromium Blog: Roll-out plan for HTML5 by Default")
- [Flash Roadmap - The Chromium Projects](https://sites.google.com/a/chromium.org/dev/flash-roadmap#TOC-HTML5-By-Default-Target:-Chrome-55---Dec-2016- "Flash Roadmap - The Chromium Projects")
- [Intent to Implement and Ship: The “system-ui” generic font family - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/hvN9YVvIb5c/5DrcunKSCAAJ "Intent to Implement and Ship: The “system-ui” generic font family - Google グループ")
- [SSLサーバー証明書 : SHA-1 証明書の受付終了と SHA-2 証明書への移行について｜Cybertrust.ne.jp](https://www.cybertrust.ne.jp/sureserver/productinfo/sha1ms.html "SSLサーバー証明書 : SHA-1 証明書の受付終了と SHA-2 証明書への移行について｜Cybertrust.ne.jp")

----

## Microsoft Edge build 14986 changelog - Microsoft Edge Development
[developer.microsoft.com/en-us/microsoft-edge/platform/changelog/desktop/14986/](https://developer.microsoft.com/en-us/microsoft-edge/platform/changelog/desktop/14986/ "Microsoft Edge build 14986 changelog - Microsoft Edge Development")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge build 14986リリース。
CSS Custom Property、IntersectionObserverのサポート。
Fetchをフラグ付きでサポート、async/awaitをデフォルトで有効に

----

## Release Notes for Safari Technology Preview 19 | WebKit
[webkit.org/blog/7093/release-notes-for-safari-technology-preview-19/](https://webkit.org/blog/7093/release-notes-for-safari-technology-preview-19/ "Release Notes for Safari Technology Preview 19 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 19リリース。
ES6 modulesのサポート、Touch Barのサポート、Pointer Lock APIの有効化、WebDriver時は`navigator.webdriver`が触れるようになるなど

----

## Announcing TypeScript 2.1 | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/12/07/announcing-typescript-2-1/](https://blogs.msdn.microsoft.com/typescript/2016/12/07/announcing-typescript-2-1/ "Announcing TypeScript 2.1 | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.1リリース。
async/await、Object Rest & Spread、`keyof` type、Mapped Typeのサポートなど

- [TypeScript 2.1.4 変更点 - Qiita](http://qiita.com/vvakame/items/fc7e37d0296c63f41f4f "TypeScript 2.1.4 変更点 - Qiita")

----

## Angular 2.3.0 Now Available
[angularjs.blogspot.com/2016/12/angular-230-now-available.html](http://angularjs.blogspot.com/2016/12/angular-230-now-available.html "Angular 2.3.0 Now Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2.3.0リリース。
IDEなどと連携する向けにAngular Language Serviceをリリース、zone.jsのスタックトレースが分かりやすくなるように改善されるなど

----

## TestCafe v0.11.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-11-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-11-0-released.html "TestCafe v0.11.0 Released | TestCafe")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v0.11.0リリース。
Selectorの仕組みを変更、built-in assertionの追加、ブラウザに起動引数をわたせるように

----

## Release 7.1.0 · developit/preact
[github.com/developit/preact/releases/tag/7.1.0](https://github.com/developit/preact/releases/tag/7.1.0 "Release 7.1.0 · developit/preact")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

小さなReactライクなライブラリであるPreact 7.1.0リリース。
初期レンダリングの高速化など

----

## parse5
[inikulin.github.io/parse5/#3-0-0](http://inikulin.github.io/parse5/#3-0-0 "parse5")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">ReleaseNote</span></p>

HTMLパーサであるparse5 3.0.0リリース。

----

## Release 2.1.0 · qunitjs/qunit
[github.com/qunitjs/qunit/releases/tag/2.1.0](https://github.com/qunitjs/qunit/releases/tag/2.1.0 "Release 2.1.0 · qunitjs/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.1.0リリース。

----

## Release KITT · sass/libsass
[github.com/sass/libsass/releases/tag/3.4.0](https://github.com/sass/libsass/releases/tag/3.4.0 "Release KITT · sass/libsass")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">ReleaseNote</span></p>

LibSass 3.4リリース

----
<h1 class="site-genre">アーティクル</h1>

----

## The State of Babel · Babel
[babeljs.io/blog/2016/12/07/the-state-of-babel](https://babeljs.io/blog/2016/12/07/the-state-of-babel "The State of Babel · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span></p>

Babelの現状について。
babel-preset-env、babili、コードカバレッジやプラグインエコシステム、ドキュメント、今後のロードマップについて

----

## 今年のうちに対応したい、Node.jsのBufferに潜む危険性 - Yahoo! JAPAN Tech Blog
[techblog.yahoo.co.jp/advent-calendar-2016/node\_new\_buffer/](https://techblog.yahoo.co.jp/advent-calendar-2016/node_new_buffer/ "今年のうちに対応したい、Node.jsのBufferに潜む危険性 - Yahoo! JAPAN Tech Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span></p>

Node.jsの`new Buffer`のセキュリティ的な問題点についての解説。
非推奨となった`new Buffer`の代わりとなる`Buffer.from`/`Buffer.alloc`/`Buffer.allocUnsafe`について

- [notes/Lets-fix-Buffer-API.md at master · ChALkeR/notes](https://github.com/ChALkeR/notes/blob/master/Lets-fix-Buffer-API.md "notes/Lets-fix-Buffer-API.md at master · ChALkeR/notes")

----

## Node.js v7 has updated V8 to 5.4 | Node.js
[nodejs.org/en/blog/community/update-v8-5.4/](https://nodejs.org/en/blog/community/update-v8-5.4/ "Node.js v7 has updated V8 to 5.4 | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>

Node.js v7で使えるようになったECMAScriptの機能や改善点について

----

## Variable Fontについて - console.blog(self);
[sadah.hatenablog.com/entry/variablefont](http://sadah.hatenablog.com/entry/variablefont "Variable Fontについて - console.blog(self);")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span></p>

Variable Fontの確認方法や仕様について。
どのようにフォントの設定をCSSから変更するかについて。

----

## Vue.js Vueコンポーネントのユニットテストを書いてみよう - Qiita
[qiita.com/potato4d/items/8215941b84c11b845886](http://qiita.com/potato4d/items/8215941b84c11b845886 "Vue.js Vueコンポーネントのユニットテストを書いてみよう - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Vueコンポーネントのユニットテストの方法について

----

## How to Snapshot Test Everything in Your Redux App With Jest – Medium
[medium.com/@jondot/how-to-snapshot-test-everything-in-your-redux-app-with-jest-fde305ebedea](https://medium.com/@jondot/how-to-snapshot-test-everything-in-your-redux-app-with-jest-fde305ebedea "How to Snapshot Test Everything in Your Redux App With Jest – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">testing</span></p>

Jestを使ったReactコンポーネントのsnapshotテスト、enzymeを使ったインタラクションテスト、Reduxのreducerのテスト手法について

----

## Promise の all と race だけで書ける待ち合わせ、書けない待ち合わせ - Qiita
[qiita.com/Kuniwak/items/9ea447598b7652db78b9](http://qiita.com/Kuniwak/items/9ea447598b7652db78b9 "Promise の all と race だけで書ける待ち合わせ、書けない待ち合わせ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

`Promise.all`と`Promise.race`を使った待ちわせのパターンについて

----

## On Webpack and Source Map integration | Code.Art.Web
[lorefnon.me/2016/12/03/on-webpack-and-source-map-integration.html](http://lorefnon.me/2016/12/03/on-webpack-and-source-map-integration.html "On Webpack and Source Map integration | Code.Art.Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpackの`devtool`で指定できるSource Mapオプションについて

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## prigara/javascript-conferences: List of conferences for frontend and Node.js developers in 2016
[github.com/prigara/javascript-conferences](https://github.com/prigara/javascript-conferences "prigara/javascript-conferences: List of conferences for frontend and Node.js developers in 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">イベント</span></p>

JavaScriptのカンファレンスをまとめているリポジトリ

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## andywer/webpack-blocks: 📦 Configure webpack using functional feature blocks.
[github.com/andywer/webpack-blocks](https://github.com/andywer/webpack-blocks "andywer/webpack-blocks: 📦 Configure webpack using functional feature blocks.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">config</span> <span class="jser-tag">library</span></p>

webpackの設定を関数で書くことができるモジュール

----
