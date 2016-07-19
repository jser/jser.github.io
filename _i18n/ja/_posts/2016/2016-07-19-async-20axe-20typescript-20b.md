---
title: "2016-07-19のJS: async 2.0、aXe 2.0、TypeScript 2.0β"
author: azu
layout: post
date : 2016-07-19T09:50
category: JSer
tags:
    - async
    - promise
    - accessibility
    - TypeScript

---

JSer.info #288 - 非同期処理ライブラリ[Async](https://github.com/caolan/async "Async")の2.0がリリースされました。
2.0ではライブラリ内部が整理され、`require("async/series")`のように直接参照でそれぞれの機能が利用できるようになっています。また、内部的にES2015 modulesでimport/exportしている[async-es](https://www.npmjs.com/package/async-es "async-es")も合わせて公開されています。

機能的な変更点についてはCHANGELOGを参照してください。

- [async/CHANGELOG.md at v2.0.0 · caolan/async](https://github.com/caolan/async/blob/v2.0.0/CHANGELOG.md "async/CHANGELOG.md at v2.0.0 · caolan/async")

----

HTMLのアクセシビリティテストライブラリである[aXe](https://github.com/dequelabs/axe-core "aXe") 2.0がリリースされました。

aXeはHTMLにスクリプトとして読み込ませて実行し、[定義したルール](https://github.com/dequelabs/axe-core/blob/master/doc/rule-descriptions.md)にもとづきアクセシビリティのチェックをするライブラリ/ツールです。

- [Deque Launches aXe 2.0](http://www.deque.com/blog/introducing-axe-2-0/ "Deque Launches aXe 2.0")

2.0では[Plugins](https://github.com/dequelabs/axe-core/blob/master/doc/plugins.md "Plugins")の仕組みが追加されています。

----

[TypeScript 2.0 Beta](https://blogs.msdn.microsoft.com/typescript/2016/07/11/announcing-typescript-2-0-beta/ "TypeScript 2.0 Beta")が公開されました。

Non-nullable type、module定義でワイルドカード(`*`)のサポート、`never` typeなどの機能が追加されています。
また、tsconfigの`include`でglobサポート、built-inの型定義ファイルを`--lib`で指定できるように、`--skipLibCheck`の追加など

詳しくは以下を参照してください。

- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&amp;#39;s new in TypeScript · Microsoft/TypeScript Wiki")
- [TypeScript 2.0 Beta 変更点 - Qiita](http://qiita.com/vvakame/items/ae239f3d6f6f08f7c719 "TypeScript 2.0 Beta 変更点 - Qiita")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## ESLint v3.1.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/07/eslint-v3.1.0-released](http://eslint.org/blog/2016/07/eslint-v3.1.0-released "ESLint v3.1.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.1.0リリース。
ルールがエラーの開始位置のみしかレポートできなかったのが、範囲指定してエラーレポートできるようになるなど

- [ESLint v3.1.0 - Qiita](http://qiita.com/mysticatea/items/723a467a4eb47e4913e2 "ESLint v3.1.0 - Qiita")

----

## Release Zepto.js 1.2.0 · madrobby/zepto
[github.com/madrobby/zepto/releases/tag/v1.2.0](https://github.com/madrobby/zepto/releases/tag/v1.2.0 "Release Zepto.js 1.2.0 · madrobby/zepto")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Zepto.js 1.2.0リリース。
`__proto__`をコードベースから削除、`$.noop`や`$.isNumeric()`の追加ｎado

----

## async/CHANGELOG.md at v2.0.0 · caolan/async
[github.com/caolan/async/blob/v2.0.0/CHANGELOG.md](https://github.com/caolan/async/blob/v2.0.0/CHANGELOG.md "async/CHANGELOG.md at v2.0.0 · caolan/async")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

async 2.0.0リリース。
ES2015版の`async-es`の提供、`race`などの機能追加。
破壊的な変更として`waterfall`の挙動変更、`filter`や`reject`などのコールバック関数が受け取る引数を変更など

- [Async v2.0.0 リリース - Qiita](http://qiita.com/suguru03/items/b73ab97482d5394b8f43 "Async v2.0.0 リリース - Qiita")

----

## Deque Launches aXe 2.0
[www.deque.com/blog/introducing-axe-2-0/](http://www.deque.com/blog/introducing-axe-2-0/ "Deque Launches aXe 2.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">testing</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

ウェブサイトのAccessibilityテストエンジンであるaXe 2.0リリース

- [dequelabs/axe-core: Accessibility engine for automated Web UI testing](https://github.com/dequelabs/axe-core "dequelabs/axe-core: Accessibility engine for automated Web UI testing")

----

## protractor/CHANGELOG.md at 4.0.0 · angular/protractor
[github.com/angular/protractor/blob/4.0.0/CHANGELOG.md](https://github.com/angular/protractor/blob/4.0.0/CHANGELOG.md "protractor/CHANGELOG.md at 4.0.0 · angular/protractor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Protractor 4.0.0リリース。
`webdriver-manager`が個別のnpmモジュールとしてインストール可能に、TypeScriptの型定義ファイルを追加など

- [webdriver-manager](https://www.npmjs.com/package/webdriver-manager "webdriver-manager")

----

## Announcing TypeScript 2.0 Beta | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/07/11/announcing-typescript-2-0-beta/](https://blogs.msdn.microsoft.com/typescript/2016/07/11/announcing-typescript-2-0-beta/ "Announcing TypeScript 2.0 Beta | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.0βリリース。
Non-nullable Type、module定義に`*`などが使えるように。
`never` typeの追加、tsconfigでglobサポート、built-inの型定義ファイルを`--lib`で指定できるように、`--skipLibCheck`の追加など

- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&amp;#39;s new in TypeScript · Microsoft/TypeScript Wiki")
- [TypeScript 2.0 Beta 変更点 - Qiita](http://qiita.com/vvakame/items/ae239f3d6f6f08f7c719 "TypeScript 2.0 Beta 変更点 - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## 4 Types of Memory Leaks in JavaScript and How to Get Rid Of Them
[auth0.com/blog/2016/01/26/four-types-of-leaks-in-your-javascript-code-and-how-to-get-rid-of-them/](https://auth0.com/blog/2016/01/26/four-types-of-leaks-in-your-javascript-code-and-how-to-get-rid-of-them/ "4 Types of Memory Leaks in JavaScript and How to Get Rid Of Them")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

JavaScriptでよくあるメモリリークのパターンについて。
Chrome開発者ツールを使ってメモリリークを見つける方法について

----

## Node.js における Promise を使った例外処理 - from scratch
[yosuke-furukawa.hatenablog.com/entry/2016/07/12/103734](http://yosuke-furukawa.hatenablog.com/entry/2016/07/12/103734 "Node.js における Promise を使った例外処理 - from scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Promises</span></p>

Node.jsのuncaughtExceptionとPromiseを使った場合のunhandledRejectionについて。
それぞれの違いや動作について

----

## What’s inside jQuery 3.0 | jQuery 3.0 new features
[codebrahma.com/whats-new-jquery-3-0/](https://codebrahma.com/whats-new-jquery-3-0/ "What’s inside jQuery 3.0 | jQuery 3.0 new features")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span></p>

jQuery 3の細かな変更について。
strict mode、for of、`requestAnimationFrame()`、エスケープの仕組み、jqXHR、`.show()`/`hide()`の改善、`.width()`/`.height()`が整数値ではなくなるなど

----

## The Lumpy Web - Tales of a Developer Advocate
[paul.kinlan.me/the-lumpy-web/](https://paul.kinlan.me/the-lumpy-web/ "The Lumpy Web - Tales of a Developer Advocate")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">spec</span> <span class="jser-tag">browser</span></p>

Webとブラウザにおける問題は大きく分けて3つに分類できる。
ブラウザ毎の実装違い(実装のバージョン違い)、仕様と実装の齟齬、実装優先度の問題。
これらの問題に対してどこを参照すれば、どのカテゴリの問題であるかを把握できるかについて書かれてる

----

## JavaScript variables hoisting in details
[rainsoft.io/javascript-hoisting-in-details/](https://rainsoft.io/javascript-hoisting-in-details/ "JavaScript variables hoisting in details")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

`var`のhoisting(巻き上げ)についての解説。
また`let`や`const`、`class`とTDZについて

----

## Mixins Considered Harmful | React
[facebook.github.io/react/blog/2016/07/13/mixins-considered-harmful.html](https://facebook.github.io/react/blog/2016/07/13/mixins-considered-harmful.html "Mixins Considered Harmful | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

ReactのMixinでやっていることは、higher-order componentsやutilを使うなど別の方法で解決できるという話

----

## enzyme+mocha+power-assertでReactコンポーネントのフルレンダリングテスト - wadackel.me
[blog.wadackel.me/2016/react-enzyme-mocha-power-assert/](https://blog.wadackel.me/2016/react-enzyme-mocha-power-assert/ "enzyme+mocha+power-assertでReactコンポーネントのフルレンダリングテスト - wadackel.me")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">testing</span></p>

Reactコンポーネントをjsdomとenzymeでテストする話

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Redux Middleware Wars (Japanese) // Speaker Deck
[speakerdeck.com/shuhei/redux-middleware-wars-japanese](https://speakerdeck.com/shuhei/redux-middleware-wars-japanese "Redux Middleware Wars (Japanese) // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">スライド</span></p>

Reduxで非同期処理を扱うMiddlewareについてのスライド。
redux-thunk、redux-promise、redux-saga、redux-loop、redux-observableの比較

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ianstormtaylor/slate: A completely customizable framework for building rich text editors in the browser.
[github.com/ianstormtaylor/slate](https://github.com/ianstormtaylor/slate "ianstormtaylor/slate: A completely customizable framework for building rich text editors in the browser.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">editor</span></p>

リッチエディタを実装できるReact Component。
ロジックはプラグインとして実装できるためカスタマイズしやすい作り。

----

## sindresorhus/conf: Simple config handling for your app or module
[github.com/sindresorhus/conf](https://github.com/sindresorhus/conf "sindresorhus/conf: Simple config handling for your app or module")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Node.jsでシンプルな設定保存ライブラリ。

----

## carteb/carte-blanche: An isolated development space with integrated fuzz testing for your components. See them individually, explore them in different states and quickly and confidently develop them.
[github.com/carteb/carte-blanche](https://github.com/carteb/carte-blanche "carteb/carte-blanche: An isolated development space with integrated fuzz testing for your components. See them individually, explore them in different states and quickly and confidently develop them.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

React Componentのチェックができるツール。
ランダム/任意のデータを入れて描画結果がどうなるかを確認できる。
スタイルガイド的なツール

----

## ECMAScript Version Detector
[azu.github.io/ecmascript-version-detector/](https://azu.github.io/ecmascript-version-detector/ "ECMAScript Version Detector")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScriptのコードを入力すると、そのコードの構文のECMAScript versionを出してくれるツールとライブラリ。
書いてるコードがProposal段階なのかを判定できる

----

## zingchart/zingtouch: A JavaScript touch gesture detection library for the modern web
[github.com/zingchart/zingtouch](https://github.com/zingchart/zingtouch "zingchart/zingtouch: A JavaScript touch gesture detection library for the modern web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">mobile</span> <span class="jser-tag">library</span></p>

TouchとGestureの管理ライブラリ。
`ZingTouch.Region(element)`で領域を作成し、その領域に対してイベントを設定できる

----
