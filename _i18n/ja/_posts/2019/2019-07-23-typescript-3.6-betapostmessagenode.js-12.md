---
title: "2019-07-23のJS: TypeScript 3.6 Beta、postMessageとパフォーマンス、Node.js 12の変更点"
author: "azu"
layout: post
date : 2019-07-23T01:11:39.658Z
category: JSer
tags:
- TypeScript
- performance
- Node.js

---

JSer.info #445 - TypeScript 3.6 Betaがリリースされました。

- [Announcing TypeScript 3.6 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/)
- [Roadmap · microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/issues/202)

Generator/Iteratorの型改善、 次のようなArray Spreadの変換においてエッジケースで仕様との挙動の違いがあった問題が修正されています。

```ts
[...Array(5)]
```

また、Promiseの`await`忘れなどから起きる型の不一致に関するエラー表示改善なども含まれています。

----

[Is postMessage slow? — DasSur.ma](https://dassur.ma/things/is-postmessage-slow/)という記事では`postMessage`で送信するペイロードのパフォーマンスについて書かれています。

`postMessage`の仕様ではオブジェクトを送る際にStructured Clone algorithmでのシリアライズの仕組みが含まれています。
Structured Clone algorithmと`JSON.stringify`/`JSON.parse`とのパフォーマンスの比較やImmerJSを使って送るオブジェクト自体を小さくする方法に紹介されています。

また、`ArrayBuffer`などはTransferable型であるため、シリアライズのコストがなく送ることができるためサイズが大きな場合は優位な点や
WebAssembly、SharedArrayBufferについても触れています。

`postMessage`で送るペイロードとしてオブジェクトとバイナリをどちらを使うかの基準や計測したデータについても書かれています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Ember.js - Ember 3.11 Released
[blog.emberjs.com/2019/07/15/ember-3-11-released.html](https://blog.emberjs.com/2019/07/15/ember-3-11-released.html "Ember.js - Ember 3.11 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 3.11リリース。
`...attributes`構文のサポート、`{{fn}}` helper、`{{on}}` modifierの追加。
`Function.prototype.observes`の非推奨化など


----

## Recommended security update | Yarn Blog
[yarnpkg.com/blog/2019/07/12/recommended-security-update/](https://yarnpkg.com/blog/2019/07/12/recommended-security-update/ "Recommended security update | Yarn Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Yarn 1.17.3リリース。
`*.yarnpkg.com`、`*.npmjs.org`, `*.npmjs.com`のレジストリに対する通信は自動的にhttpsで通信するようにする修正


----

## Announcing TypeScript 3.6 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/ "Announcing TypeScript 3.6 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.6 ベータリリース。
Generator/Iteratorの型改善、 Array Spreadの変換の改善、Promiseの`await`忘れなどのエラー表示改善など


----

## laverdet/isolated-vm: Secure & isolated JS environments for nodejs
[github.com/laverdet/isolated-vm](https://github.com/laverdet/isolated-vm "laverdet/isolated-vm: Secure & isolated JS environments for nodejs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8 Isolateを使ってNode.jsからJavaScriptを隔離した環境で実行するライブラリ


----
<h1 class="site-genre">アーティクル</h1>

----

## Use React.memo() wisely
[dmitripavlutin.com/use-react-memo-wisely/](https://dmitripavlutin.com/use-react-memo-wisely/ "Use React.memo() wisely")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`React.memo()`の役割と使い方について


----

## Google deprecates XSS Auditor for Chrome | The Daily Swig
[portswigger.net/daily-swig/google-deprecates-xss-auditor-for-chrome](https://portswigger.net/daily-swig/google-deprecates-xss-auditor-for-chrome "Google deprecates XSS Auditor for Chrome | The Daily Swig")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">XSS</span> <span class="jser-tag">article</span></p>

MSEdgeに続いてChromeのXSS Auditorも非推奨となることについて。


----

## ES proposal: private class fields
[2ality.com/2019/07/private-class-fields.html](https://2ality.com/2019/07/private-class-fields.html "ES proposal: private class fields")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript Proposalのprivate class fieldsについて


----

## Is postMessage slow? — DasSur.ma
[dassur.ma/things/is-postmessage-slow/](https://dassur.ma/things/is-postmessage-slow/ "Is postMessage slow? — DasSur.ma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`postMessage`のパフォーマンスについての記事。Structured Clone algorithmとJSONシリアライズでのパフォーマンス比較。
ImmerJSを使った送信するオブジェクトの最小化、ArrayBufferのtransferableなバイナリフォーマットのパフォーマンス。
100kbまではオブジェクト、それ以上のサイズならバイナリを検討することについて。


----

## Datadog と Lighthouse を利用した WebPerf の継続的計測 | mediba Creator × Engineer Blog
[ceblog.mediba.jp/post/186341145447/webperf-measuring-with-lighthouse-and-datadog](https://ceblog.mediba.jp/post/186341145447/webperf-measuring-with-lighthouse-and-datadog "Datadog と Lighthouse を利用した WebPerf の継続的計測 | mediba Creator × Engineer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Lighthouseで計測した値をDatadogに保存してメトリクスの可視化を行う方法について


----

## Weak references and finalizers · V8
[v8.dev/features/weak-references](https://v8.dev/features/weak-references "Weak references and finalizers · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

`WeakMap`、`WeakSet`のweakの動作について。
またECMAScript Proposalである`WeakRef`と`FinalizationGroup`について。

- [tc39/proposal-weakrefs: WeakRefs](https://github.com/tc39/proposal-weakrefs "tc39/proposal-weakrefs: WeakRefs")

----

## Node.js 12: The future of server-side JavaScript - LogRocket Blog
[blog.logrocket.com/node-js-12/](https://blog.logrocket.com/node-js-12/ "Node.js 12: The future of server-side JavaScript - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 12の主な変更点について。
V8の更新によるパフォーマンス改善、TLS 1.3の対応、ヒープサイズがメモリサイズによって決まるように、HTTPパーサの改善、Diagnostic reportsやheap dumpの同梱など。
また`worker_thread`のexperimentalフラグが外れ、試験的な機能としてES modulesの対応など


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Introduction - Content Security Policy
[csp.withgoogle.com/docs/index.html](https://csp.withgoogle.com/docs/index.html "Introduction - Content Security Policy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">XSS</span></p>

CSP(Content Security Policy)についての解説サイト。
CSPとはどのようにXSSを防ぐのか、使う理由/使わない理由、CSPの設定、FAQなどが書かれている


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## IntrinsicLabs/osgood: Osgood is a secure, fast, and simple platform for running JavaScript HTTP servers.
[github.com/IntrinsicLabs/osgood](https://github.com/IntrinsicLabs/osgood "IntrinsicLabs/osgood: Osgood is a secure, fast, and simple platform for running JavaScript HTTP servers.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">server</span> <span class="jser-tag">Rust</span></p>

Rustで書かれたV8ベースのHTTPサーバ。ルーティングのハンドラはWorkerとして実行され、リクエストに対するレスポンスを返す

- [Introducing Osgood - DEV Community 👩‍💻👨‍💻](https://dev.to/tlhunter/introducing-osgood-4k1m "Introducing Osgood - DEV Community 👩‍💻👨‍💻")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## zerobias/effector: The state manager ☄️
[github.com/zerobias/effector](https://github.com/zerobias/effector "zerobias/effector: The state manager ☄️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

ステート管理ライブラリ。
EventsやEffectsを使い、StoreのStateを更新という一連の流れの名前空間を管理するDomainのAPIを提供しています。
VueやReactなどUIフレームワーク向けのアダプターも提供しています。


----

## gajus/lightship: Abstracts readiness/ liveness checks and graceful shutdown of Node.js services running in Kubernetes.
[github.com/gajus/lightship](https://github.com/gajus/lightship "gajus/lightship: Abstracts readiness/ liveness checks and graceful shutdown of Node.js services running in Kubernetes.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Kubernetes</span> <span class="jser-tag">node.js</span></p>

Kubernetesのヘルスチェックなどに対する抽象層を提供するNode.jsライブラリ


----

## ehmicky/test-each: 🤖 Repeat tests. Repeat tests. Repeat tests.
[github.com/ehmicky/test-each](https://github.com/ehmicky/test-each "ehmicky/test-each: 🤖 Repeat tests. Repeat tests. Repeat tests.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

Data Driven Testingを行うためのヘルパーライブラリ。
データからテストケースを作成するためのイテレートやSeed値を元にしたランダムな値を生成してテストできる


----
