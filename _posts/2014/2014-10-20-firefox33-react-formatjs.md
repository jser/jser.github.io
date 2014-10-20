---
title: "2014-10-20のJS: Firefox33、Reactとは何か、FormatJS"
author: azu
layout: post
date : 2014-10-19T23:31
category: JSer
tags:
    - Firefox
    - React
    - i18n
    - library

---

JSer.info #197 - [Firefox 33.0](https://www.mozilla.org/en-US/firefox/33.0/releasenotes/ "Firefox — Notes (33.0) — Mozilla")がリリースされました。

ChromeやOperaは既にデフォルトサポートになっている[&lt;picture&gt; ](https://dev.opera.com/blog/opera-25/ "&lt;picture&gt; ")要素が、フラグ付きでFirefoxにも追加されました。

また開発者ツールにCSS周りの機能や、[Developer Toolbar](https://developer.mozilla.org/en-US/docs/Tools/GCLI "Developer Toolbar")のコマンドなど色々追加されているので以下の記事を見てみるといいと思います。

- [Event listeners popup, @media sidebar, Cubic bezier editor + more – Firefox Developer Tools Episode 33 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2014/07/event-listeners-popup-media-sidebar-cubic-bezier-editor-more-firefox-developer-tools-episode-33/ "Event listeners popup, @media sidebar, Cubic bezier editor + more – Firefox Developer Tools Episode 33 ✩ Mozilla Hacks – the Web developer blog")

Firefoxの開発者ツールの開発について興味がある方は以下のスライドも見てみると面白いかもしれません。

- [Five Stages of Development - Nordic.js](http://www.slideshare.net/robnyman/five-stages-of-development-nordicjs "Five Stages of Development - Nordic.js")
- [▶ Nordic.js 2014 • Robert Nyman - Five Stages of Development - YouTube](https://www.youtube.com/watch?v=z0GZUCvfjHI "▶ Nordic.js 2014 • Robert Nyman - Five Stages of Development - YouTube")

----
[ReactJS For Stupid People](http://blog.andrewray.me/reactjs-for-stupid-people/ "ReactJS For Stupid People")という記事は最近よく見る[React](http://facebook.github.io/react/ "React")とは何かについて整理されています。

React自体はViewのみを扱うライブラリですが、[Flux](http://facebook.github.io/flux/ "Flux")アーキテクチャの話と混ざって話されてたりするため役割が大きく見えることがあります。
この記事では特徴と良い所、良くない所についてまとめられています。

[React v0.12 RC](http://facebook.github.io/react/blog/2014/10/16/react-v0.12-rc1.html "React v0.12 RC")がリリースされていますが、
[JSX](http://facebook.github.io/jsx/ "JSX")まわり変更やAPIのリネームなど整理してる感じがするのでReactがどういうものかについて知るにはいい機会なのかもしれません。

----
Yahoo社から[FormatJS](http://formatjs.io/ "FormatJS")という国際化のためJavaScriptライブラリがリリースされました。

各地域別の数値、日付、相対時間、複数形の表現などの国際化対応の仕組みを提供するモジュールとそれらを使ってローカライズした画面を作成するHandlebarsやReact、Dust等のテンプレートエンジンと一緒に使える拡張を提供しています。

このライブラリは[ECMAScript Internationalization API Specification](http://www.ecma-international.org/ecma-402/1.0/ "ECMAScript Internationalization API Specification")がベースとなっていて、まだ全てのブラウザがECMA i18n APIをサポートしてる訳ではないので、polyfillとして[Intl.js](https://github.com/andyearnshaw/Intl.js)と一緒に使うようになっています。

またECMA i18n APIでは、相対時間や複数形のローカライズについてのAPIは用意されていません。
そのため、FormatJSでは[Unicode CLDR](http://cldr.unicode.org/ "Unicode CLDR")のデータと[ICU MessageFormat](http://userguide.icu-project.org/formatparse/messages "ICU MessageFormat")で書いてローカライズするようになっていて、そのフォーマッター等はそれぞれ[モジュール](http://formatjs.io/github/ "GitHub — FormatJS")として提供されています。

ECMA i18n API 1st editiionでは、ICU MessageFormat等の書式ついては仕様がありませんが、次期バージョンでは[Message Formatting](http://wiki.ecmascript.org/doku.php?id=globalization:messageformatting "Message Formatting")が検討されているようです。
そのため、すべてがECMA標準仕様に則ったものではなく拡張もありますが、FormatJSはICU MessageFormatをASTにパースする[パーサ](https://github.com/yahoo/intl-messageformat-parser "Parser")も用意しているので次期仕様への配慮もしやすい作りになっている気がします。

またコード自体もES6 moduleを使って書かれていて、それを[grunt-bundle-jsnext-lib](grunt-bundle-jsnext-lib)でbundle化したものを配布しているようです。

JavaScriptを使った国際化については以下の話が面白いです。

- [Localize your frontend // slidr.io](http://slidr.io/klyrr/localize-your-frontend "Localize your frontend // slidr.io")
	- 動画: [https://www.youtube.com/watch?v=Lu4mholN2lA&index=3&list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw](https://www.youtube.com/watch?v=Lu4mholN2lA&index=3&list=PL37ZVnwpeshF8Sr8JZNFU6boKMmod9YBw)
	- jimdo.com の国際化対応の話
- [WEB+DB PRESS Vol.78に「フロントエンドの国際化」について書いた！ - teppeis blog](http://teppeis.hatenablog.com/entry/2013/12/webdb-press-javascript-i18n "WEB+DB PRESS Vol.78に「フロントエンドの国際化」について書いた！ - teppeis blog")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox — Notes (33.0) — Mozilla
[www.mozilla.org/en-US/firefox/33.0/releasenotes/](https://www.mozilla.org/en-US/firefox/33.0/releasenotes/ "Firefox — Notes (33.0) — Mozilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox33リリース。

OpenH264のサポート、CSPのバックエンドが新しくなりました。
また、`<picture>`をフラグ付きでサポート、[開発者ツールの機能追加](https://hacks.mozilla.org/2014/07/event-listeners-popup-media-sidebar-cubic-bezier-editor-more-firefox-developer-tools-episode-33/ "Event listeners popup, @media sidebar, Cubic bezier editor + more – Firefox Developer Tools Episode 33 ✩ Mozilla Hacks – the Web developer blog")等が行われています。

- [Firefox 33 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/33 "Firefox 33 for developers - Mozilla | MDN")
- [Firefox 33 サイト互換性情報 - Mozilla | MDN](https://developer.mozilla.org/ja/docs/Mozilla/Firefox/Releases/33/Site_Compatibility "Firefox 33 サイト互換性情報 - Mozilla | MDN")
- [Firefox 33 が正式リリース、Open H264 や @counter-style 規則のサポート、OMTC の有効化など | WWW WATCH](http://hyper-text.org/archives/2014/10/firefox_33_release.shtml "Firefox 33 が正式リリース、Open H264 や @counter-style 規則のサポート、OMTC の有効化など | WWW WATCH")
- [CSP for the web we have | Mozilla Security Blog](https://blog.mozilla.org/security/2014/10/04/csp-for-the-web-we-have/ "CSP for the web we have | Mozilla Security Blog")

----

## Release Dragon Master · sass/libsass
[github.com/sass/libsass/releases/tag/3.0](https://github.com/sass/libsass/releases/tag/3.0 "Release Dragon Master · sass/libsass")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">C++</span></p>

SassコンパイラのC++実装であるlibsass 3.0リリース。

Sass3.4の動作に近づけていく改善が中心。

`@extends`、Map、`call()`のサポート、WIndowsでの動作を改善など

----

## jQuery UI 1.11.2 | jQuery UI Blog
[blog.jqueryui.com/2014/10/jquery-ui-1-11-2/](http://blog.jqueryui.com/2014/10/jquery-ui-1-11-2/ "jQuery UI 1.11.2 | jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.11.2リリース

----

## React v0.12 RC | React
[facebook.github.io/react/blog/2014/10/16/react-v0.12-rc1.html](http://facebook.github.io/react/blog/2014/10/16/react-v0.12-rc1.html "React v0.12 RC | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.12 RCリリース。

JSXに破壊的な変更が多く含まれている。

`@jsx` pragmaは不要に、JSXタグは小文字or`-`が含まれてるならHTMLとして扱うように、Spread attributesをサポートする代わりにtransferPropsToは非推奨にする等など

----

## A new ES6 draft, Rev28
[esdiscuss.org/topic/a-new-es6-draft-rev28](https://esdiscuss.org/topic/a-new-es6-draft-rev28 "A new ES6 draft, Rev28")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 6 Draft Rev 28リリース。

- [harmony:specification\_drafts \[ES Wiki\]](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#october_14_2014_draft_rev_28 "harmony:specification\_drafts \[ES Wiki\]")

----

## Android Lollipop | Android Developers
[developer.android.com/about/versions/lollipop.html#WebView](http://developer.android.com/about/versions/lollipop.html#WebView "Android Lollipop | Android Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Android</span> <span class="jser-tag">webview</span></p>

Android5以降のChromium WebViewはGoogle Playからアップデートすることが出来るようになっている

----
<h1 class="site-genre">アーティクル</h1>

----

## Exploring Angular 1.3 - One-time bindings – Blog | thoughtram - Extend your memory
[blog.thoughtram.io//angularjs/2014/10/14/exploring-angular-1.3-one-time-bindings.html](http://blog.thoughtram.io//angularjs/2014/10/14/exploring-angular-1.3-one-time-bindings.html "Exploring Angular 1.3 - One-time bindings – Blog | thoughtram - Extend your memory")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

Angular 1.3で導入されたone-time bindingについての解説

----

## ReactJS For Stupid People
[blog.andrewray.me/reactjs-for-stupid-people/](http://blog.andrewray.me/reactjs-for-stupid-people/ "ReactJS For Stupid People")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span></p>

Reactとは何かについて。

ReactはViewのみを扱うライブラリ、DOM APIでHTML作成は大変なのでJSXというSyntaxを持つ、Reactはサーバでも使える。

良くない点としてドキュメントサイトの入り口のわかりにくさやサイズなどがあげられています。

Fluxはコンセプトであってライブラリではないという話やどういう時に使うべきかについても書かれている。

----

## platform.js ⇒ webcomponents.js
[blog.polymer-project.org/announcements/2014/10/16/platform-becomes-webcomponents/](http://blog.polymer-project.org/announcements/2014/10/16/platform-becomes-webcomponents/ "platform.js ⇒ webcomponents.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

platform.jsはwebcomponents.jsという名前にリネームされる。

bower等を利用して入れている場合は影響があるので参照するファイルを変更する必要がある

----

## 自動検出と自動修正でCSSを保守する - Qiita
[qiita.com/r7kamura/items/7addebc61d177313a29d](http://qiita.com/r7kamura/items/7addebc61d177313a29d "自動検出と自動修正でCSSを保守する - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Sass</span> <span class="jser-tag">Tools</span></p>

scss-lintとcsscombを使ってSassのLintと修正を行い保守可能なCSSを維持する事について

----

## status.modern.IEの見方 | Web Scratch
[efcl.info/2014/10/19/modern-ie/](http://efcl.info/2014/10/19/modern-ie/ "status.modern.IEの見方 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">browser</span> <span class="jser-tag">webservice</span></p>

status.modern.IEで公開されているIEの開発ステータスの読み方と、その変更を見ていく方法について

----

## Announcing key advances to JavaScript performance in Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/10/09/announcing-key-advances-to-javascript-performance-in-windows-10-technical-preview.aspx](http://blogs.msdn.com/b/ie/archive/2014/10/09/announcing-key-advances-to-javascript-performance-in-windows-10-technical-preview.aspx "Announcing key advances to JavaScript performance in Windows 10 Technical Preview - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">JavaScript</span></p>

IEのJavaScriptエンジンであるChakraの最適化について。
[Baseline コンパイラ](https://dev.mozilla.jp/2013/04/the-baseline-compiler-has-landed/ "Baseline コンパイラ")的なASTを中間層として用意してJITコンパイルする仕組みなどについて書かれている。

最適化としてやっていることについてで、
オブジェクトの同値の場合にインラインキャッシュ、コードのインライン化、Arrayアクセスの最適化、mark&sweep GCの改善等に触れている

- [Baseline コンパイラを導入しました | Mozilla Developer Street (modest)](https://dev.mozilla.jp/2013/04/the-baseline-compiler-has-landed/ "Baseline コンパイラを導入しました | Mozilla Developer Street (modest)")

----

## NPM 2.0 and how it helps avoiding global dependencies | 4waisenkinder
[4waisenkinder.de/blog/2014/10/18/npm-2-dot-0-and-the-much-better-star-npm-run-star-command/](http://4waisenkinder.de/blog/2014/10/18/npm-2-dot-0-and-the-much-better-star-npm-run-star-command/ "NPM 2.0 and how it helps avoiding global dependencies | 4waisenkinder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

npm 2.0からnpm run scriptに引数を渡せるようになった件とnpm run scriptでは自動的にnode_modules/.binのパスを解決してくれる事について

----

## mattdesl/module-best-practices
[github.com/mattdesl/module-best-practices](https://github.com/mattdesl/module-best-practices "mattdesl/module-best-practices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

Node.jsのモジュールベストプラクティス。

モジュールのファイル名、npmモジュールの作成、コンストラクタのパターン、テスト、バージョニング、package.jsonの情報、npmignore、npm run-scriptについて等

----
<h1 class="site-genre">サイト、サービス</h1>

----

## Browser Platform Status Tracker
[platformstatustracker.azurewebsites.net/](http://platformstatustracker.azurewebsites.net/ "Browser Platform Status Tracker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">まとめ</span> <span class="jser-tag">browser</span></p>

IEやChromiumのステータス情報から差分の情報をまとめてくれているページ。

どの機能がどのバージョンで入ったか、prefixが外れたか等が分かる

----

## Lapple/ErrorBoard
[github.com/Lapple/ErrorBoard](https://github.com/Lapple/ErrorBoard "Lapple/ErrorBoard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">node.js</span></p>

Node.jsで動くJavaScriptのエラーを収集して見るためのダッシュボードアプリ

----

## Functional Programming in Javascript
[jhusain.github.io/learnrx/](http://jhusain.github.io/learnrx/ "Functional Programming in Javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">関数型プログラミング</span></p>

Arrayのmapやfilter等について学べるエクササイズ。

一つのエクササイズを完了させると次の問題へ進めていって全部で40個以上ある

<a href='https://github.com/jhusain/learnrx'>https://github.com/jhusain/learnrx</a>

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## kriasoft/react-starter-kit · GitHub
[github.com/kriasoft/react-starter-kit](https://github.com/kriasoft/react-starter-kit "kriasoft/react-starter-kit · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React/Fluxパターンで全部入りな感じのStarter Kit。

シングルページアプリケーション的な構成になっている。

- [Web Starter Kit — Web Fundamentals](https://developers.google.com/web/starter-kit/ "Web Starter Kit — Web Fundamentals")

----

## FormatJS
[formatjs.io/](http://formatjs.io/ "FormatJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

数字や日付、文字列の国際化対応のためのライブラリ。

150言語以上に対応しており、HandlebarsやReact等のテンプレートの対応も用意されている。

ECMA i18n APIやUnicode CLDR、ICU Messageなどの標準の上に実装されている

- [Announcing Format.JS: Internationalize your web apps on the client &amp; server | Yahoo Engineering](http://yahooeng.tumblr.com/post/100006468771/announcing-format-js-internationalize-your-web-apps-on "Announcing Format.JS: Internationalize your web apps on the client &amp; server | Yahoo Engineering")
- [米Yahoo!が国際化のためのJavaScriptライブラリ「Format.JS」を公開 | SourceForge.JP Magazine](http://sourceforge.jp/magazine/14/10/17/151500 "米Yahoo!が国際化のためのJavaScriptライブラリ「Format.JS」を公開 | SourceForge.JP Magazine")

----

## medikoo/memoize
[github.com/medikoo/memoize](https://github.com/medikoo/memoize "medikoo/memoize")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

memorizeを行うためのライブラリ。

多彩なキャッシュするルールが用意されていて、特定の引数をキーにしたり、非同期対応、Weakなmemorizeなども用意されている

----

## No9/localstorage-down
[github.com/no9/localstorage-down](https://github.com/no9/localstorage-down "No9/localstorage-down")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

leveldownのdbとして使えるlocalStorageのバックエンド実装。

----

## uber/potter
[github.com/uber/potter](https://github.com/uber/potter "uber/potter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

uber社のNodeのプロダクションプロジェクトを作成するscaffold、CIの設定等行うpluginで拡張可能なコマンドラインツール

<a href='http://raynos.github.io/nodeconfeu2014-talk/'>http://raynos.github.io/nodeconfeu2014-talk/</a>

----

## box/leche
[github.com/box/leche](https://github.com/box/leche "box/leche")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

mockするためのオブジェクト作成やパラメタライズドテストを行うData Providerの機能が用意されているテストの補助ライブラリ。

MochaとSinonと共に使う事を想定して作られている

----

## dgs700/angular-custom-element
[github.com/dgs700/angular-custom-element](https://github.com/dgs700/angular-custom-element "dgs700/angular-custom-element")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">WebComponents</span></p>

Angular2.0ではWeb Components対応が予定されているが、1.xでもCustom Elementsを使ってディレクティブを定義出来るようにするライブラリ

----

## Knockout Secure Binding – Brian M Hunt
[brianmhunt.github.io/articles/knockout-plus-content-security-policy/](http://brianmhunt.github.io/articles/knockout-plus-content-security-policy/ "Knockout Secure Binding – Brian M Hunt")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

KnockoutのCSP対応なバインディングを出来るようにするライブラリ。

`new Function`を使わないようにすることでCSP対応している。

----

## othiym23/async-listener
[github.com/othiym23/async-listener](https://github.com/othiym23/async-listener "othiym23/async-listener")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node 0.11のasyncListener APIのpolyfillライブラリ。

----

## captainbrosset/pagerecorder
[github.com/captainbrosset/pagerecorder](https://github.com/captainbrosset/pagerecorder "captainbrosset/pagerecorder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">addon</span></p>

Firefoxの開発者ツールでページの変更を記録するアドオン。

どのようなイベントがおきて、どの要素が変更されたか等を一覧できる

----

## react-hot-loader · Pure JS live-editing for React
[gaearon.github.io/react-hot-loader/](http://gaearon.github.io/react-hot-loader/ "react-hot-loader · Pure JS live-editing for React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Reactを使ったコードのLive Reloadを行うためのWebpackのloaderに指定するプラグイン

----
<h1 class="site-genre">書籍関係</h1>

----

## Learning Ember.js by Blake Erickson [Leanpub PDF/iPad/Kindle]
[leanpub.com/learningemberjs](https://leanpub.com/learningemberjs "Learning Ember.js by Blake Erickson \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

Ember.jsとEmber CLIについての基本的な使い方から学べる書籍

----
