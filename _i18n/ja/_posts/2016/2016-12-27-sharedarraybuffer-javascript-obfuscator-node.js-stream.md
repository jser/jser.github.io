---
title: "2016-12-27のJS: SharedArrayBufferとAtomics API、Node.js Stream、JavaScript obfuscator"
author: azu
layout: post
date : 2016-12-27T09:58
category: JSer
tags:
    - browser
    - ECMAScript
    - Node.js
    - Tools

---

JSer.info #311 - Safari Technology Preview Release 20とMSEdgeのJavaScriptエンジンである[ChakraCore 1.4.0](https://github.com/Microsoft/ChakraCore/wiki/Release-Notes#v140 "ChakraCore 1.4.0")が公開されています。

- [Release Notes · Microsoft/ChakraCore Wiki](https://github.com/Microsoft/ChakraCore/wiki/Release-Notes#v140)
- [Release Notes for Safari Technology Preview 20 | WebKit](https://webkit.org/blog/7120/release-notes-for-safari-technology-preview-20/)

どちらも[SharedArrayBuffer](http://tc39.github.io/ecmascript_sharedmem/shmem.html#GlobalObject.ConstructorProps.SharedArrayBuffer "SharedArrayBuffer")が実装されています。
SharedArrayBufferは、WebWorkerとの間でもデータを共有できる[Stage 3のProposal](https://github.com/tc39/proposals)仕様です。

データをコピーや[Transfer](https://developer.mozilla.org/ja/docs/Web/API/Transferable)ではなく、メモリで共有する仕様です。(いわゆる共有メモリ)
複数のスレッドがメモリ内の同じデータを読み書きするため、スレッドセーフなAPIが必要になります。
そのため、[tc39/ecmascript_sharedmem](https://github.com/tc39/ecmascript_sharedmem "tc39/ecmascript_sharedmem: Shared memory and atomics for ECMAscript")の仕様では不可分操作を提供する`Atomics` APIが合わせて定義されています。

SharedArrayBufferとAtomics APIについて、詳しくは次のURLを見るのが良いと思います。

- [tc39/ecmascript_sharedmem: Shared memory and atomics for ECMAscript](https://github.com/tc39/ecmascript_sharedmem "tc39/ecmascript_sharedmem: Shared memory and atomics for ECMAscript")
- [A Taste of JavaScript’s New Parallel Primitives ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/05/a-taste-of-javascripts-new-parallel-primitives/)([翻訳](https://dev.mozilla.jp/2016/05/a-taste-of-javascripts-new-parallel-primitives/))
- [JavaScriptでの並列プログラミング: 共有メモリーと不可分操作、ロック // Speaker Deck](https://speakerdeck.com/chikoski/20161113-nodefest)
- [SharedArrayBufferとAtomics APIについて - JS.next](http://js-next.hatenablog.com/entry/2015/09/30/225251 "SharedArrayBufferとAtomics APIについて - JS.next")

Stage 3の仕様ですが、既に2つ以上の実装があるため、次のTC39 Meeting(2017年1月)でStage 4となる予定です。
そのため、ES2017として公開される可能性があります。

- [tc39-notes/nov-30.md at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/blob/master/es7/2016-11/nov-30.md#13iia-sharedarraybuffer "tc39-notes/nov-30.md at master · rwaldron/tc39-notes")

この仕様に先んじて、ECMAScriptに"Agent"という概念が既に追加されています。

- [Add language to define Agents by lars-t-hansen · Pull Request #522 · tc39/ecma262](https://github.com/tc39/ecma262/pull/522 "Add language to define Agents by lars-t-hansen · Pull Request #522 · tc39/ecma262")

また、2016年11月のTC39 MeetingでStageが変わったProposalは次の記事にまとめてあります。

- [ECMAScript proposal updates @ 2016-11 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2016/12/22/ecmascript-proposals "ECMAScript proposal updates @ 2016-11 | ECMAScript Daily")

----

[Stream API入門 - Qiita](http://qiita.com/Mizunashi_Mana/items/872354cd7bf25090932f "Stream API入門 - Qiita")では、Node.jsのStream APIについて解説されています。他のコールバックやPromise、Generator、async/awaitなどの非同期処理についても触れています。

Node.js Streamの特徴の一つでもあるバッファリングとバックプレッシャーについては合わせて次の記事を見てみるといいかもしれません。

- [highWaterMarkから探るNode.jsのStreamの仕組み - Yahoo! JAPAN Tech Blog](https://techblog.yahoo.co.jp/advent-calendar-2016/node-stream-highwatermark/ "highWaterMarkから探るNode.jsのStreamの仕組み - Yahoo! JAPAN Tech Blog")

これとは別で、WHATWGが提案している[Streams Standard](https://streams.spec.whatwg.org/ "Streams Standard")(Fetch APIなどと連携する)も合わせて見ると面白いかもしれません。

- [streams/FAQ.md at master · whatwg/streams](https://github.com/whatwg/streams/blob/master/FAQ.md "streams/FAQ.md at master · whatwg/streams")

また、データのストリーム処理はJavaScriptという言語にかぎらずあるものなので、次の記事も見てみるとストリーム処理の特徴が分かりやすいかもしれません。

- [ストリーム処理とは何か？＋2016年の出来事 - Qiita](http://qiita.com/kimutansk/items/60e48ec15e954fa95e1c "ストリーム処理とは何か？＋2016年の出来事 - Qiita")

----
<h1 class="site-genre">ヘッドライン</h1>

----

## Say allo&#x27; to yeoman-generator 1.0 | Yeoman
[yeoman.io/blog/hello-generator-1.0.html](http://yeoman.io/blog/hello-generator-1.0.html "Say allo' to yeoman-generator 1.0 | Yeoman")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ジェネレーター</span> <span class="jser-tag">Tools</span></p>

Yeoman-generator 1.0リリース。
`composeWith`のAPIを簡略化、Yarnサポート、deprecatedなAPIを削除など

- [Release v1.0.0 🎉 · yeoman/generator](https://github.com/yeoman/generator/releases/tag/v1.0.0 "Release v1.0.0 🎉 · yeoman/generator")

----

## Release Notes · Microsoft/ChakraCore Wiki
[github.com/Microsoft/ChakraCore/wiki/Release-Notes#v140](https://github.com/Microsoft/ChakraCore/wiki/Release-Notes#v140 "Release Notes · Microsoft/ChakraCore Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

ChakraCore 1.4リリース。
JITがLinuxやmacOSでも有効化、async/awaitをデフォルトで有効化、SharedArrayBufferを実験的にサポート、wasmの実験的サポートなど

----

## Release Notes for Safari Technology Preview 20 | WebKit
[webkit.org/blog/7120/release-notes-for-safari-technology-preview-20/](https://webkit.org/blog/7120/release-notes-for-safari-technology-preview-20/ "Release Notes for Safari Technology Preview 20 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 20リリース。
Visual Viewport、SharedArrayBufferを有効化、`block-all-mixed-content`の追加、BlinkからportしたCSSパーサを使うようになるなど

- [What the Virtual Viewport?  |  Web  |  Google Developers](https://developers.google.com/web/updates/2015/01/What-the-Viewport "What the Virtual Viewport?  |  Web  |  Google Developers")
- [lars-t-hansen/ecmascript\_sharedmem: Placeholder for old shared memory spec](https://github.com/lars-t-hansen/ecmascript_sharedmem "lars-t-hansen/ecmascript\_sharedmem: Placeholder for old shared memory spec")

----

## Release 3rd Mutation · canjs/canjs
[github.com/canjs/canjs/releases/tag/v3.0.0](https://github.com/canjs/canjs/releases/tag/v3.0.0 "Release 3rd Mutation · canjs/canjs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CanJS 3.0リリース
コードは`can-*`からなるモジュールに分割され、`.attr()`の代わりに`DefineMap`の導入など

- [JavaScriptフレームワーク「CanJS 3.0」リリース | OSDN Magazine](https://mag.osdn.jp/16/12/22/160000 "JavaScriptフレームワーク「CanJS 3.0」リリース | OSDN Magazine")
- [donejs - donejs](http://donejs.com/ "donejs - donejs")

----
<h1 class="site-genre">アーティクル</h1>

----

## ECMAScript proposal updates @ 2016-11 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2016/12/22/ecmascript-proposals](https://ecmascript-daily.github.io/ecmascript/2016/12/22/ecmascript-proposals "ECMAScript proposal updates @ 2016-11 | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2016年11月のTC39ミーティングでのProposalのStage変動をまとめたもの

----

## Stream API入門 - Qiita
[qiita.com/Mizunashi\_Mana/items/872354cd7bf25090932f](http://qiita.com/Mizunashi_Mana/items/872354cd7bf25090932f "Stream API入門 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">stream</span></p>

Node.jsのStream APIについて。
非同期処理のコールバック、Promise、async/await、generatorを踏まえてのStreamについての解説。
Write/Read/Duplex、Stream処理が得意とすること、`objectMode`についてなど幅広く解説されてる

----

## CSS Writing Modes ◆ 24 ways
[24ways.org/2016/css-writing-modes/](https://24ways.org/2016/css-writing-modes/ "CSS Writing Modes ◆ 24 ways")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSSの`writing-mode`プロパティについての解説

----

## かずぽんブログ • Vue.js 2016年まとめ &amp; 今後
[blog.kazupon.jp/post/154903508388/vuejs-2016-closing-and-future](http://blog.kazupon.jp/post/154903508388/vuejs-2016-closing-and-future "かずぽんブログ • Vue.js 2016年まとめ & 今後")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

2016年のVue.jsの変化について。
Vue.js 2.0、コミュニティ、エコシステム、利用範囲や今後について

----

## Firebug lives on in Firefox DevTools ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/12/firebug-lives-on-in-firefox-devtools/](https://hacks.mozilla.org/2016/12/firebug-lives-on-in-firefox-devtools/ "Firebug lives on in Firefox DevTools ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firebug</span> <span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

Firebugは開発終了したが、多くの機能はFirefoxの開発者ツールに引き継がれている/引き継ぐ予定があるという話。

またFirebugはマルチプロセス対応を念頭に開発されたものではなかったため、Firebugを拡張するよりも、Firefoxの開発者ツールを拡張していく方が良いという決定がされた。

----

## Web アクセシビリティ向け Node.js 製の自動チェックツールや DevTools 用の拡張機能など ::ハブろぐ
[havelog.ayumusato.com/develop/a11y/e732-a11y\_checking\_automate.html](https://havelog.ayumusato.com/develop/a11y/e732-a11y_checking_automate.html "Web アクセシビリティ向け Node.js 製の自動チェックツールや DevTools 用の拡張機能など ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">test</span></p>

Webアクセシビリティの自動チェックツールや補助ツールの紹介。

----

## JavaScriptのUIライブラリはどうあるべきかという話とOnsen UIのアーキテクチャ - id:anatooのブログ
[blog.anatoo.jp/entry/2016/12/09/201511](http://blog.anatoo.jp/entry/2016/12/09/201511 "JavaScriptのUIライブラリはどうあるべきかという話とOnsen UIのアーキテクチャ - id:anatooのブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span></p>

特定のUIフレームワークに依存されないUIフレームワークの基盤をどのように作るかという話。
CSS Components層、Web Components層、フレームワークバインディング層のレイヤー分けについて

----

## ServiceWorker内にExpressサーバーを立てる - Qiita
[qiita.com/narirou/items/738a0fe6656d0f905e28](http://qiita.com/narirou/items/738a0fe6656d0f905e28 "ServiceWorker内にExpressサーバーを立てる - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">node.js</span></p>

express-serviceがどのようにして実際のNode.jsで動くExpressのコードをServideWorkerの中でも擬似的に動かしているのかについての解説

- [express-service](https://www.npmjs.com/package/express-service "express-service")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Accessibility - Learn web development | MDN
[developer.mozilla.org/en-US/docs/Learn/Accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility "Accessibility - Learn web development | MDN")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">web </span></p>

アクセシビリティについてのガイド

----

## SpeedTracker
[speedtracker.org/](https://speedtracker.org/ "SpeedTracker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

個人向けに使うCalibreやSpeedCurveのような継続的なパフォーマンス計測サービス。
WebPageTestで取った結果をGitHubリポジトリにJekyllで動くようにデータをpushしてくれる。

- [Performance Calendar » Introducing SpeedTracker](http://calendar.perfplanet.com/2016/introducing-speedtracker/ "Performance Calendar » Introducing SpeedTracker")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Mithril、Vue.jsの仮想DOM用のi18nライブラリ作った - Qiita
[qiita.com/shibukawa/items/c2298b21b4629941b230](http://qiita.com/shibukawa/items/c2298b21b4629941b230 "Mithril、Vue.jsの仮想DOM用のi18nライブラリ作った - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Node.jsでもブラウザでも動作するi18nライブラリ。
プレースホルダ、複数形、コンテキスト、`data-i18n`属性に対する翻訳する機能を持つ

- [i18n for Virtual DOM (i18n4v) — i18n for virtual dom 0.1.5 documentation](https://i18n4v.js.org/ "i18n for Virtual DOM (i18n4v) — i18n for virtual dom 0.1.5 documentation")

----

## devongovett/regexgen: Generate regular expressions that match a set of strings
[github.com/devongovett/regexgen](https://github.com/devongovett/regexgen "devongovett/regexgen: Generate regular expressions that match a set of strings")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span></p>

複数の文字列を渡して、それにマッチする正規表現を作るライブラリ

----

## javascript-obfuscator/javascript-obfuscator: JavaScript obfuscator for Node.js
[github.com/javascript-obfuscator/javascript-obfuscator](https://github.com/javascript-obfuscator/javascript-obfuscator "javascript-obfuscator/javascript-obfuscator: JavaScript obfuscator for Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

JavaScriptの難読化ツール/ライブラリ。
ES2015+のコードを扱うことができ、Source Mapにも対応している

----

## amilajack/eslint-plugin-compat: Browser and ES spec compatibility assertion with ESLint
[github.com/amilajack/eslint-plugin-compat](https://github.com/amilajack/eslint-plugin-compat "amilajack/eslint-plugin-compat: Browser and ES spec compatibility assertion with ESLint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ESLint</span></p>

AutoPrefixerのように想定ブラウザを記述し、そのブラウザで動かないAPIを使ってないかをチェックするESLintルール。
caniuseやcompat tableのデータを使う

----
