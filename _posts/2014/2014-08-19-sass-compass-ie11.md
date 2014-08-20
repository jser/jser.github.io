---
title: "2014-08-19のJS: Sass 3.4、Compass 1.0、IE11/F12開発者ツール"
author: azu
layout: post
tags:
    - JavaScript
    - Sass
    - Compass
    - IE
    - debug

---

JSer.info #188 - [Sass 3.4](http://blog.sass-lang.com/posts/221239-sass-34-is-released "Sass 3.4")がリリースされました。

parent selector `&` の扱いの改善や、sourcemapの生成がデフォルトに(無効にする場合は`--sourcemap=none`とする)、`@error`ディレクティブのサポート等が入っています。

- [File: SASS_CHANGELOG — Sass Documentation](http://sass-lang.com/documentation/file.SASS_CHANGELOG.html#340_18_august_2014 "File: SASS_CHANGELOG — Sass Documentation")

----

Sassを使ったフレームワークである[Compass](http://compass-style.org/ "Compass")の1.0がついにリリースされました。
(前回のstableは2012年06月24日)

- [Compass 1.0 is Released! | Compass Documentation](http://compass-style.org/blog/2014/08/15/omg-compass-1-0/ "Compass 1.0 is Released! | Compass Documentation")

[autoprefixer](https://github.com/ai/autoprefixer "autoprefixer")と同じようにvendor prefixは[Can I use](http://caniuse.com/ "Can I use")のデータを使って生成するようになったことや、CompassのCoreライブラリをCompassコマンドなしで利用出来るようになっています。

またSassのsourcemapのサポートや[Compass-blueprint](http://compass-blueprint.org/ "Compass-blueprint")はCoreからはずされてpluginとして利用するようになっています。

その他の変更点についてはChangelogを参照して下さい。

- [Compass History | Compass Documentation](http://compass-style.org/CHANGELOG/ "Compass History | Compass Documentation")

----

- [August updates for Internet Explorer - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/08/13/august-updates-for-internet-explorer.aspx "August updates for Internet Explorer - IEBlog - Site Home - MSDN Blogs")
- [Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/08/14/announcing-new-f12-dev-tools-features-in-august-update.aspx "Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs")

上記の記事ではIE11の8月度のアップデートについて書かれています。
IE11でのWebDriverのサポートや開発者ツールのアップデートがされています。

[Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/08/14/announcing-new-f12-dev-tools-features-in-august-update.aspx "Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs") の方に開発者ツールの変更点が書かれていますが、表示周りが幅広く更新されています。

カラーピッカーの追加、watchでの補完、ブレーク時に関数がreturnしてる値の表示、UI Responsiveness tool/Memory toolのデザイン改善、セッションをimport/export出来るようになる等、結構変わっている部分が多いです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Sass 3.4 is Released « Sass Blog
[blog.sass-lang.com/posts/221239-sass-34-is-released](http://blog.sass-lang.com/posts/221239-sass-34-is-released "Sass 3.4 is Released « Sass Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">ReleaseNote</span></p>

Sass 3.4 リリース。

parent selector `&`の扱いを改善、Selector Functionsで`&`を使えるように。`@error` ディレクティブの追加、sourcemapの生成がデフォルトになるなど

- [File: SASS\_CHANGELOG — Sass Documentation](http://sass-lang.com/documentation/file.SASS_CHANGELOG.html "File: SASS\_CHANGELOG — Sass Documentation")
- [@error directive · Issue \#747 · sass/sass](https://github.com/sass/sass/issues/747 "@error directive · Issue \#747 · sass/sass")

----

## Compass 1.0 is Released! | Compass Documentation
[compass-style.org/blog/2014/08/15/omg-compass-1-0/](http://compass-style.org/blog/2014/08/15/omg-compass-1-0/ "Compass 1.0 is Released\! \| Compass Documentation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Compass 1.0リリース。

ベンダーprefixはcaniuseを利用、コマンドラインツールなしにライブラリとして利用可能に、sourcemapサポート、import-onceでのパフォーマンス改善等

----

## Release JSHint 2.5.4 · jshint/jshint
[github.com/jshint/jshint/releases/tag/2.5.4](https://github.com/jshint/jshint/releases/tag/2.5.4 "Release JSHint 2.5.4 · jshint/jshint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.5.4リリース。

----

## August updates for Internet Explorer - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/08/13/august-updates-for-internet-explorer.aspx](http://blogs.msdn.com/b/ie/archive/2014/08/13/august-updates-for-internet-explorer.aspx "August updates for Internet Explorer - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">ReleaseNote</span></p>

2014年8月のIE11のアップデートについて。

F12開発者ツールの改善、WebGLの改善、WebDriverのサポート

- [Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs](http://blogs.msdn.com/b/ie/archive/2014/08/14/announcing-new-f12-dev-tools-features-in-august-update.aspx "Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs")

----

## jQuery UI 1.11.1 | jQuery UI Blog
[blog.jqueryui.com/2014/08/jquery-ui-1-11-1/](http://blog.jqueryui.com/2014/08/jquery-ui-1-11-1/ "jQuery UI 1.11.1 \| jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.11.1リリース

----

## Knockout 3.2.0 released - Steve Sanderson’s blog - As seen on YouTube™
[blog.stevensanderson.com/2014/08/18/knockout-3-2-0-released/](http://blog.stevensanderson.com/2014/08/18/knockout-3-2-0-released/ "Knockout 3.2.0 released - Steve Sanderson’s blog - As seen on YouTube™")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout 3.2.0リリース。

Components、Custom Elements、textInputのバインディングなどの追加。

IE6のサポートは維持

----

## Release v0.8.0: Release 0.8.0 (2014-08-12) · twada/power-assert
[github.com/twada/power-assert/releases/tag/v0.8.0](https://github.com/twada/power-assert/releases/tag/v0.8.0 "Release v0.8.0: Release 0.8.0 (2014-08-12) · twada/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 0.8.0リリース。

espowerのオプションでアサーションの指定がescallmatchを使ったパターンを渡す方法に変更。デフォルト設定を使っている場合はそのまま維持される。

- [twada/escallmatch](https://github.com/twada/escallmatch "twada/escallmatch")

----
<h1 class="site-genre">アーティクル</h1>

----

## 長期かつ修正頻度の高いPJでのCSSメンテ - ワザノバ | wazanova
[wazanova.jp/items/1484](http://wazanova.jp/items/1484 "長期かつ修正頻度の高いPJでのCSSメンテ - ワザノバ \| wazanova")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">設計</span> <span class="jser-tag">翻訳</span></p>

大規模プロジェクトでのCSSのメンテナンスビリティについて。

- DRYより修正する時に迷わず消せるような疎結合なコンポーネントである方が長期的にはよかった
- プロジェクトにおける命名ルールを持つことはいいこと
- コンポーネントに名前空間をもたせると分かりやすいこと
- ファイルの管理について
- ライブラリmixinの問題について

等、実践的な事について書かれていて参考になります。

- [Enduring CSS: writing style sheets for rapidly changing, long-lived projects - Author and responsive web developer Ben Frain](http://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/ "Enduring CSS: writing style sheets for rapidly changing, long-lived projects - Author and responsive web developer Ben Frain")

----

## Opinionated Rundown of JS Frameworks | Blog
[blog.andyet.com/2014/08/13/opinionated-rundown-of-js-frameworks](http://blog.andyet.com/2014/08/13/opinionated-rundown-of-js-frameworks "Opinionated Rundown of JS Frameworks \| Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MVC</span> <span class="jser-tag">まとめ</span></p>

HumanJSの人によるJavaScript MV*のまとめ

Angular/Ember/React/Polymer/Backbone.js/Vanilla/Ampersand.js

- [シングルページアプリづくりのJavaScriptフレームワーク比較 - ワザノバ \| wazanova](http://wazanova.jp/items/1474 "シングルページアプリづくりのJavaScriptフレームワーク比較 - ワザノバ \| wazanova")

----

## Web Reflection: PointerEvents No More
[webreflection.blogspot.com/2014/08/pointerevents-no-more.html](http://webreflection.blogspot.com/2014/08/pointerevents-no-more.html "Web Reflection: PointerEvents No More")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">event</span></p>

BlinkはPointerEventsを実装しないことにした事について。

- touch eventsが既にある
- hit-testモデルがパフォーマンス的に不利
- 複雑すぎる

等が主な理由。

- [Issue 162757 - chromium - Implement pointer events in Chrome behind experimental flag - An open-source project to help move the web forward. - Google Project Hosting](https://code.google.com/p/chromium/issues/detail?id=162757#c64 "Issue 162757 - chromium - Implement pointer events in Chrome behind experimental flag - An open-source project to help move the web forward. - Google Project Hosting")
- [PSA: PointerEvents and PointerGestures are being replaced by polymer-gestures, breaking changes for pointer\* events - Google グループ](https://groups.google.com/forum/#!topic/polymer-dev/ba4aDyOozm8 "PSA: PointerEvents and PointerGestures are being replaced by polymer-gestures, breaking changes for pointer\* events - Google グループ")

----

## Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs
[blogs.msdn.com/b/ie/archive/2014/08/14/announcing-new-f12-dev-tools-features-in-august-update.aspx](http://blogs.msdn.com/b/ie/archive/2014/08/14/announcing-new-f12-dev-tools-features-in-august-update.aspx "Announcing new F12 dev tools features in August update - IEBlog - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">debug</span></p>

IE11のF12開発者ツールの変更点について。

カラーピッカー、sourcemapの選択機能、補完の強化、Asyncコールスタック、パフォーマンス、メモリパネルでセッションをimport/exportが可能になる等

- [米MS、8月のIE11更新で強化された「F12開発者ツール」の新機能を紹介：CodeZine](http://codezine.jp/article/detail/8034 "米MS、8月のIE11更新で強化された「F12開発者ツール」の新機能を紹介：CodeZine")


----

## 古めかしいCGを描くためのライブラリ gretro です - 音の鳴るブログ
[mohayonao.hatenablog.com/entry/2014/08/12/111859](http://mohayonao.hatenablog.com/entry/2014/08/12/111859 "古めかしいCGを描くためのライブラリ gretro です - 音の鳴るブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

Canvasで描くとどうしてもモダンな感じになってしまうという問題を解決するライブラリ。

色やパターンを絞ってレトロな感じのCanvasを描画出来る

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## ESNext for humans - LvivJS 16 August 2014
[www.slideshare.net/janjongboom/esnext-for-humans-lvivjs-16-august-2014](http://www.slideshare.net/janjongboom/esnext-for-humans-lvivjs-16-august-2014 "ESNext for humans - LvivJS 16 August 2014")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">スライド</span></p>

ES6についてのスライド。

新しい構文についての紹介がメインでGeneratorについて詳しく説明してる

----

## JavaScript Test-Driven Development with Jasmine 2.0 and Karma
[www.slideshare.net/cebartling/javascript-38057372](http://www.slideshare.net/cebartling/javascript-38057372 "JavaScript Test-Driven Development with Jasmine 2.0 and Karma")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Jasmine2.0とKarmaについてのスライド。

jasmine spyについて紹介されてる

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## arian/partition-bundle
[github.com/arian/partition-bundle](https://github.com/arian/partition-bundle "arian/partition-bundle")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">plugin</span> <span class="jser-tag">library</span></p>

Browserify内にAMD的な動的ロードを持ち込むplugin。

動的に読み込みたいjsファイルを定義した設定ファイルを作り、動的に読み込むようにrequireではなく`loadjs`関数を使って読み込む。

----

## Rome
[bevacqua.github.io/rome/](http://bevacqua.github.io/rome/ "Rome")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

依存がないDate/Time Picker UIライブラリ。

----

## gwendall/way.js
[github.com/gwendall/way.js](https://github.com/gwendall/way.js "gwendall/way.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HTML formで入力した内容をStorageに保存したり、JSONにしたり、監視や値のやり取りが出来るライブラリ。

フォームに属性を指定しておくだけで、フォーム内容の保存的な事が出来る

----

## thlorenz/browserify-devdupe · GitHub
[github.com/thlorenz/browserify-devdupe](https://github.com/thlorenz/browserify-devdupe "thlorenz/browserify-devdupe · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">npm</span> <span class="jser-tag">library</span></p>

browserify bundleを作るときにnpm dedupeみたいな事をするモジュール

----

## mizchi/bower-build
[github.com/mizchi/bower-build](https://github.com/mizchi/bower-build "mizchi/bower-build")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

bowerの`main`で指定されているファイルをconcatしたものを生成するツール

- [bower-buildでbowerで入れたファイルを一つにconcatする - Qiita](http://qiita.com/mizchi/items/67fcaf92ef3e8e5ac393 "bower-buildでbowerで入れたファイルを一つにconcatする - Qiita")

----
