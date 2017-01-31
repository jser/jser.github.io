---
title: "JSerレポート #1 Next Bundler、テスティングフレームワーク"
author: azu
layout: report
date : 2017-01-31T10:12
category: report
tags:
    - webpack
    - bundler
    - testing
    - report

---

# [Bundler #1](https://github.com/jser/report/issues/1 "Next Bundler #1")

JavaScriptのコードはモジュールに分けて開発することが一般的です。
ブラウザにおいて、一つずつ`<script>`タグでモジュールをロードするのはラウンドトリップやコネクションの問題が発生します。

そのため、多くの場合ブラウザ向けのコードはモジュールをまとめた(bundleした)ファイルを作成して配信します。

- [ES6 ModulesはHTTP/2によってconcat無しで使えるようになるのか - teppeis blog](http://teppeis.hatenablog.com/entry/2015/05/es6-modules-and-http2 "ES6 ModulesはHTTP/2によってconcat無しで使えるようになるのか - teppeis blog")
- [レトロエンジニアのための近代Webフロントエンド事情 - Qiita](http://qiita.com/uctakeoff/items/ce8da368d020273c6064 "レトロエンジニアのための近代Webフロントエンド事情 - Qiita")


その際にモジュールの依存関係などを解決しながらファイルをまとめる"bundler"と呼ばれるツールの動きについてのレポートです。

## webpack 2

- [Release v2.2.0 · webpack/webpack](https://github.com/webpack/webpack/releases/tag/v2.2.0 "Release v2.2.0 · webpack/webpack")

webpack 2が正式にリリースされています。

- [2017-01-24のJS: webpack 2正式リリース、JavaScriptの開発環境設定、2016 JS Stars - JSer.info](https://jser.info/2017/01/24/webpack-2-javascript-2016-js-star/ "2017-01-24のJS: webpack 2正式リリース、JavaScriptの開発環境設定、2016 JS Stars - JSer.info")で紹介しました。

webpack 2のドキュメントは [webpack.js.org/](https://webpack.js.org/) の新しいサイトの方にまとめられています。

[Migrating from v1 to v2](https://webpack.js.org/guides/migrating/ "Migrating from v1 to v2")にマイグレーションガイドがあります。

一部設定の名前が変更されていたり、`json-loader`がデフォルトとなっていたり既存のconfigを変更する参考になると思います。

また多くの人は次のパフォーマンス警告にかかると思うので、次の記事を読むと良いかもしれません。

- [Webpack2のパフォーマンス警告を制御する - Qiita](http://qiita.com/inuscript/items/f840b5ccff0c0be7420a "Webpack2のパフォーマンス警告を制御する - Qiita")

## [Fusebox](http://fuse-box.org/ "Fusebox")

[Fusebox](http://fuse-box.org/ "Fusebox")という新しいBundlerツールが登場しました。
実際に試してみると、初回のビルドと再ビルド(`.fusebox`のキャッシュあり)どちらも高速です。

- [2017-01-04のJS: PostCSS概要、Chrome開発者ツール、FuseBox - JSer.info](https://jser.info/2017/01/04/postcss-chrome-fusebox/ "2017-01-04のJS: PostCSS概要、Chrome開発者ツール、FuseBox - JSer.info") で紹介しました。

基本的に設定はJavaScriptのコードとして書くようになっていて、`node`で実行するだけです。

また、webpackのように設定としてentryポイントを設定するのではなく、ビルドの設定をする`FuseBox.init`と実際にbudnleするものを決める`fuse.bundle`メソッドで分かれています。

```js
const FuseBox = require("fusebox").FuseBox
let fuse = FuseBox.init({
    homeDir: "src/",
    globals: { default: "myLib"},
    outFile: "./out.js"
});

fuse.bundle(">index.js");
```

そのためコードとして設定を書くgulpとは相性がいいため、公式のサンプルでもgulp内に書いている例を見かけます。

- [angular2-example/gulpfile.js at master · fuse-box/angular2-example](https://github.com/fuse-box/angular2-example/blob/master/gulpfile.js "angular2-example/gulpfile.js at master · fuse-box/angular2-example")

## [Rollup](https://github.com/rollup/rollup "Rollup")

Rollupは順調に開発中です。
## [browserify](https://github.com/substack/node-browserify "browserify")

browserify自体を機能追加/改善するアップデートはあまり積極的に行われていません。
substack以外にPRをマージするOwnerがいないことに起因しています。

[![node-browserify 2017-01-31 19-47-37](https://cloud.githubusercontent.com/assets/19714/22461846/515bb70a-e7ee-11e6-9651-648f65a2a8c8.png)](https://github.com/substack/node-browserify/graphs/contributors)

元々本体に多くの機能があるわけではなく依存するパッケージに機能が分散しています。
しかし、その依存のアップデートが滞りがちであるため、
Issue/PRにはNode.js v6>=で追加されたDeprecated Warningや依存するパッケージのDeprecated Warningを解消する些細なものが多く並んでいます。

- [https://github.com/substack/node-browserify/pulls](https://github.com/substack/node-browserify/pulls)
- [buffer: discuss future direction of Buffer constructor API · Issue #9531 · nodejs/node](https://github.com/nodejs/node/issues/9531 "buffer: discuss future direction of Buffer constructor API · Issue #9531 · nodejs/node")

先日、[14.0.0](https://github.com/substack/node-browserify/blob/master/changelog.markdown#1400 "14.0.0")がリリースされました。
このリリースでは、browserifyが利用する`buffer`のpolyfillである[feross/buffer](https://github.com/feross/buffer "feross/buffer")がアップデートされています。
`TypedArray`を使う実装になったため、bufferを含んだコードを変換した場合に、IE10以下では動かなくなります。

IE10以下でも動くようにしたい場合は、古い[feross/buffer](https://github.com/feross/buffer "feross/buffer")を利用する必要があります。

```sh
$ npm install buffer@4 --save
$ browserify -r buffer/:buffer main.js > bundle.js
```

## ES modules

MSEdgeと[WebKit](https://lists.webkit.org/pipermail/webkit-dev/2016-December/028564.html)にES modules(`<script type="module">`)が実装されています。

- [Release Notes for Safari Technology Preview 21 | WebKit](https://webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/ "Release Notes for Safari Technology Preview 21 | WebKit")

ES modulesとNode.js modulesについては細かな挙動の違いなどが存在します。
詳しくは次の記事を読むと良いです。

- [Native ECMAScript modules: the new features and differences from Webpack modules](https://blog.hospodarets.com/native-ecmascript-modules-new-features)
- [Native ECMAScript modules - the first overview](https://blog.hospodarets.com/native-ecmascript-modules-the-first-overview#browsers-support)

webpack 2やrollupなどはES modulesのコードを直接扱うようになっています。
ES modulesのブラウザ実装が進むにつれ、ES modulesを扱うツールなども増えてくることが予想されます。
Bundlerはそこへ直接関係するツールであるため、今後の動きに注目していく必要があります。

----

# [Testing Framework #3](https://github.com/jser/report/issues/3 "Testing Framework #3")

JavaScriptのテスティングフレームワーク周りのレポートです。

## [Mocha](https://github.com/mochajs/mocha)がContributorを募集

> Mocha needs YOU!
> -- [https://github.com/mochajs/mocha#mocha-needs-you](https://github.com/mochajs/mocha#mocha-needs-you)

Mochaのメンテナンスリソースが足りていないため協力を募集する内容がREADMEにかかれています。
IssueやPull Requestのレビューをしてくれる人やMochaへのテストの追加などをコントリビューションを募集しています。

詳しくは[Projects](https://github.com/mochajs/mocha/projects "Projects · mochajs/mocha")を見るかGitterでやり取りすると良さそうです。

- [mochajs/mocha - Gitter](https://gitter.im/mochajs/mocha "mochajs/mocha - Gitter")

## Sinon.js 2.0へ向けて

[Sinon.JS](http://sinonjs.org/ "Sinon.JS") が2.0向けての作業が進められています。
タスクについては次のIssueで管理されています。

- [Sinon 2.0 Release · Issue #966 · sinonjs/sinon](https://github.com/sinonjs/sinon/issues/966 "Sinon 2.0 Release · Issue #966 · sinonjs/sinon")

> The much fabled 2.0 release, that will split Sinon.JS into more modules, tidy up the api, simplify all the dependency boilerplate by using Browserify. 
> -- [2.0 Milestone](https://github.com/sinonjs/sinon/milestone/5 "2.0 Milestone")

とあるように、(CommonJS)モジュールとして管理されていなかったのを大きくリファクタリングし、それぞれがモジュール化されています。
残りのタスクにはドキュメント系となっているため、そこまで遠くない日に2.0がリリースされるかもしれません。
プレリリース版は既に公開されています。

- [Releases · sinonjs/sinon](https://github.com/sinonjs/sinon/releases "Releases · sinonjs/sinon")

## [2016 JavaScript Rising Stars](https://risingstars2016.js.org/ "2016 JavaScript Rising Stars")

JavaScriptに関するツールやライブラリのStar増加率をまとめたサイトにおいて、[Testing Frameworks](https://risingstars2016.js.org/#test-framework "#8Testing Frameworks")についてもまとめられています。
2016年は[AVA](https://github.com/avajs/ava "AVA")と[Jest](http://facebook.github.io/jest/ "Jest")のStar数が伸びているようです。

## AVA will introduce Magic assert

テストフレームワークの[AVA](https://github.com/avajs/ava "AVA")は[power-assert](https://github.com/power-assert-js/power-assert "power-assert")を内部的に利用しテスト結果を表示することができます。
現在、そのテスト結果の表示をより分かりやすくしようと`magic-assert`という名前で開発がされています。

- [Magic assert · Issue #1155 · avajs/ava](https://github.com/avajs/ava/issues/1155 "Magic assert · Issue #1155 · avajs/ava")

![magic-assert](https://cloud.githubusercontent.com/assets/697676/21117268/9459421a-c0c1-11e6-80e6-bb2ce6be7c76.png)


----

JSer.infoでは不定期でレポートという形で、特定のテーマに関する状況をまとめています。

- [jser/report](https://github.com/jser/report "jser/report")

レポートなどの更新情報を知りたい方は[RSS](https://jser.info/rss/)や[Twitter@jser_info](https://twitter.com/jser_info)をフォローしてみてください。

<a href="https://twitter.com/jser_info" class="twitter-follow-button" data-show-count="false" data-size="large">Follow @jser_info</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

<a href='http://cloud.feedly.com/#subscription%2Ffeed%2Fhttps://jser.info/rss/' target='blank'><img id='feedlyFollow' src='https://s3.feedly.com/img/follows/feedly-follow-rectangle-flat-medium_2x.png' alt='follow us in feedly' width='71' height='28'></a>