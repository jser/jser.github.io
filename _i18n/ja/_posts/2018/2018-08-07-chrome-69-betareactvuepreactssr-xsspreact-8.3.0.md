---
title: "2018-08-07のJS: Chrome 69 Beta、React/Vue/PreactのSSR XSSの修正、Preact 8.3.0"
author: "azu"
layout: post
date : 2018-08-07T00:52:37.711Z
category: JSer
tags:
- chrome
- react
- vue
- preact

---

JSer.info #395 - Chrome 69 Betaがリリースされました。

- [Chromium Blog: Chrome 69 Beta: CSS tricks, and more](https://blog.chromium.org/2018/08/chrome-69-beta-av1-video-decoder-css.html)
- [Audio/Video Updates in Chrome 69  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/chrome-69-media-updates "Audio/Video Updates in Chrome 69  |  Web  |  Google Developers")
- [Deprecations and removals in Chrome 69  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/chrome-69-deps-rems "Deprecations and removals in Chrome 69  |  Web  |  Google Developers")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D69 "Chrome Platform Status")

CSS conic gradients、CSS scroll snap、CSS `env()` functionのサポートなどCSSの変更が多く行われています。
またOffscreenCanvasや
[ReportingObserver API](https://developers.google.com/web/updates/2018/07/reportingobserver)、[Keyboard Map API](https://github.com/WICG/keyboard-map)のサポートなどが行われています。

メディア系のアップデートは[Audio/Video Updates in Chrome 69  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/chrome-69-media-updates "Audio/Video Updates in Chrome 69  |  Web  |  Google Developers")にまとめられています。

---

React 16.4.2でSSR（サーバサイドレンダリング）時に発生するXSSが修正されています。

- [React v16.4.2: Server-side vulnerability fix - React Blog](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html)

あまりないパターンだと思いますが、タグ文字列を含む任意の値を属性値として使っている場合に、SSR時にその属性値がタグとして出力されてしまう問題が修正されています。

```js
let userProvidedData = '></div><script>alert("hi")</script>';
let props = {};
props[userProvidedData] = "hello";
let element = <div {...props} />;
let html = ReactDOMServer.renderToString(element);
// <div ></div><script>alert("hi")</script>
```

VueとPreactの同様の問題が[Reactチームによって報告](https://github.com/facebook/react/pull/13302)されており、同時に修正がリリースされています。

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">This issue affected Preact (-compat &amp; -render-to-string) as well. It&#39;s been patched in versions 3.18.1 / 3.7.1 of those libraries. Cheers to the React folks for the easy disclosure process. <a href="https://t.co/pN9nnMBDEC">https://t.co/pN9nnMBDEC</a></p>&mdash; Jason Miller 🦊⚛ (@_developit) <a href="https://twitter.com/_developit/status/1024748991458762756?ref_src=twsrc%5Etfw">August 1, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Fix for the same issue has been released in Vue 2.5.17. (only affects SSR). Thanks to the React team for coordinating this with us! <a href="https://t.co/WnKS79FjfW">https://t.co/WnKS79FjfW</a></p>&mdash; Vue.js (@vuejs) <a href="https://twitter.com/vuejs/status/1024754536877973504?ref_src=twsrc%5Etfw">August 1, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

----

Preact 8.3.0がリリースされました。

- [Release 8.3.0 · developit/preact](https://github.com/developit/preact/releases/tag/8.3.0)

[React v16.3.0](https://reactjs.org/blog/2018/03/29/react-v-16-3.html)で追加された
`getDerivedStateFromProps`と`getSnapshotBeforeUpdate`に対応しています。
またmoduleを`.mjs`で出力するように、`setState`の挙動をReactに近づけるように修正などが行われています。


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v10.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v10.8.0/](https://nodejs.org/en/blog/release/v10.8.0/ "Node v10.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

Node v10.8.0リリース。
npm 6.2.0が同梱されるようになった。


----

## React v16.4.2: Server-side vulnerability fix - React Blog
[reactjs.org/blog/2018/08/01/react-v-16-4-2.html](https://reactjs.org/blog/2018/08/01/react-v-16-4-2.html "React v16.4.2: Server-side vulnerability fix - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

React 16.4.2リリース。
SSRにおいてユーザー入力をコンポーネントの属性名に渡せるとXSSが発生する問題を修正。
minorごとに同様のpatchリリースが公開されている。
VueとPreactも同様の問題があり、合わせてsecurity fixがリリースされた。


----

## Release Notes for Safari Technology Preview 62 | WebKit
[webkit.org/blog/8384/release-notes-for-safari-technology-preview-62/](https://webkit.org/blog/8384/release-notes-for-safari-technology-preview-62/ "Release Notes for Safari Technology Preview 62 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 62リリース。
ITPデバッグモードの試験的追加、`JSON.stringify`の修正、HLSストリームのキャッシュを無効化、CSS Gridの`gap`プロパティにおける`calc`が動くように修正など


----

## TestCafe v0.21.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-21-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-21-0-released.html "TestCafe v0.21.0 Released | TestCafe")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">ReleaseNote</span></p>

TestCafe v0.21.0リリース。
テストページをHTTPSでアクセスできるように、スクリーンショットのパスに変数を使えるようになるなど


----

## Dojo Version 3.0 | Dojo
[dojo.io/blog/2018/07/27/2018-07-27-Dojo-version-3-release/](https://dojo.io/blog/2018/07/27/2018-07-27-Dojo-version-3-release/ "Dojo Version 3.0 | Dojo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Dojo 3.0リリース。
パッケージが細かく別れていたものを`@dojo/framework`に統合して利用できるように変更。マイグレーションスクリプトも公開されている。

- [framework/V3-Migration-Guide.md at master · dojo/framework](https://github.com/dojo/framework/blob/master/docs/V3-Migration-Guide.md "framework/V3-Migration-Guide.md at master · dojo/framework")

----

## ESLint v5.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/08/eslint-v5.3.0-released](https://eslint.org/blog/2018/08/eslint-v5.3.0-released "ESLint v5.3.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 5.3.0リリース。
正規表現に関するルールが2つ、Async Functionに関するルールが2つ追加された。

- [ESLint v5.3.0 - Qiita](https://qiita.com/mysticatea/items/eb99e18d6cc7c3bf9317 "ESLint v5.3.0 - Qiita")
- [Promise のコンストラクタに渡した async function 内で throw しても rejected な Promise は作られない（常に fulfilled になる） - Humanity](http://tyru.hatenablog.com/entry/2018/08/04/220530 "Promise のコンストラクタに渡した async function 内で throw しても rejected な Promise は作られない（常に fulfilled になる） - Humanity")

----

## Release 8.3.0 · developit/preact
[github.com/developit/preact/releases/tag/8.3.0](https://github.com/developit/preact/releases/tag/8.3.0 "Release 8.3.0 · developit/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 8.3.0リリース。
`getDerivedStateFromProps`と`getSnapshotBeforeUpdate`に対応。moduleを`.mjs`で出力するように、`setState`の挙動をReactに近づけるように修正など


----

## Chromium Blog: Chrome 69 Beta: CSS tricks, and more
[blog.chromium.org/2018/08/chrome-69-beta-av1-video-decoder-css.html](https://blog.chromium.org/2018/08/chrome-69-beta-av1-video-decoder-css.html "Chromium Blog: Chrome 69 Beta: CSS tricks, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 69βリリース。 CSS conic gradients、CSS scroll snap、CSS `env()` functionのサポート。
ReportingObserver API、Keyboard Map APIのサポートなど

- [Audio/Video Updates in Chrome 69  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/chrome-69-media-updates "Audio/Video Updates in Chrome 69  |  Web  |  Google Developers")
- [Deprecations and removals in Chrome 69  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/08/chrome-69-deps-rems "Deprecations and removals in Chrome 69  |  Web  |  Google Developers")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D69 "Chrome Platform Status")

----
<h1 class="site-genre">アーティクル</h1>

----

## Vue.js で XSS を作り込まないために気を付けること - SSTエンジニアブログ
[techblog.securesky-tech.com/entry/2018/08/01/110000](https://techblog.securesky-tech.com/entry/2018/08/01/110000 "Vue.js で XSS を作り込まないために気を付けること - SSTエンジニアブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">XSS</span></p>

Vue.jsでXSSが発生するポイントについての解説。
`v-html`、`href`のバインディグ、サーバサイドのテンプレートとCSRでのエスケープ漏れなどについて


----

## JSDocで型チェックする - Qiita
[qiita.com/shisama/items/016288d38165d542fffd](https://qiita.com/shisama/items/016288d38165d542fffd "JSDocで型チェックする - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの`allowJs`と`checkJs`を使ったJavaScriptでの型チェックについて。
JSDocで書いた型アノテーションや型定義ファイルを元に型チェックを行う方法について


----

## The Cost Of JavaScript In 2018 – Addy Osmani – Medium
[medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4 "The Cost Of JavaScript In 2018 – Addy Osmani – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

JavaScriptのパフォーマンスコストについての記事。
ファイルサイズ、ロード時間、インタラクティブになるまでの時間、モバイルや低スペックマシンでのコスト。
またパフォーマンスを改善するパターンなどについて


----

## I created the exact same app in React and Vue. Here are the differences.
[medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-e9a1ae8077fd](https://medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-e9a1ae8077fd "I created the exact same app in React and Vue. Here are the differences.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

VueとReactで同じTodoアプリを作って比較する記事。
処理ごとにそれぞれのやり方を比較して紹介している。


----

## ちゃんと理解するCode Splitting - Qiita
[qiita.com/seya/items/06b160adb7801ae9e66f](https://qiita.com/seya/items/06b160adb7801ae9e66f "ちゃんと理解するCode Splitting - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

webpackにおけるCode Splittingの動作の解説。Code Splittingのメリットとデメリット。
Code SplittingするUIのパターンやDynamic Import、`webpackPrefetch`オプション、VueやReactでの対応についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Storybook Tutorial
[www.learnstorybook.com/](https://www.learnstorybook.com/ "Storybook Tutorial")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Angular</span> <span class="jser-tag">Vue</span> <span class="jser-tag">tutorial</span></p>

Storybookのチュートリアル。
React、Angular、Vueに対応したStirybookでのコンポーネント開発やChromaticを使ったビジュアルテストなどについて書かれている

- [Chromatic visual testing for React](https://www.chromaticqa.com/ "Chromatic visual testing for React")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Frontend News
[frontendnews.io/](https://frontendnews.io/ "Frontend News")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">mail</span> <span class="jser-tag">web</span></p>

フロントエンドに関する1週間に1つのTipsについてを更新するサイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Fusion.js Documentation
[fusionjs.com/](https://fusionjs.com/ "Fusion.js Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">plugin</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

UberのプラグインベースなBrowser/Node.jsウェブフレームワーク。コアにプラグインの仕組みとDIの仕組みを持ち、ReactやRedux、KoaなどUberがよく利用しているものをプラグインとして導入できる。
webpackやbabelなどをラップするcliがあり、create-react-appのように設定ファイルを触らずに開発ができる。

- [Introducing Fusion.js: A Plugin-based Universal Web Framework](https://eng.uber.com/fusionjs/ "Introducing Fusion.js: A Plugin-based Universal Web Framework")

----

## sasha240100/between.js: Lightweight JavaScript (ES6) tweening engine
[github.com/sasha240100/between.js](https://github.com/sasha240100/between.js "sasha240100/between.js: Lightweight JavaScript (ES6) tweening engine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

AからBへ値の変化を扱えるライブラリ。
Tweening animationのような特定のイージングやループでの値の変化を扱う。


----
