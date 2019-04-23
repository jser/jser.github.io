---
title: "2019-04-23のJS: Svelte 3(Change Everything)、GoogleでのCSP(Content Security Policy)導入ステップ"
author: "azu"
layout: post
date : 2019-04-23T01:35:41.198Z
category: JSer
tags:
- Svelte
- CSP
- security
​
---
​
JSer.info #432 - コンパイル前提のUIコンポーネントフレームワークであるSvelte 3リリースされました。

- [Svelte 3: Rethinking reactivity](https://svelte.dev/blog/svelte-3-rethinking-reactivity)

3.0.0の[CHANGELOGには"Everything"](https://github.com/sveltejs/svelte/blob/master/CHANGELOG.md#300)として書かれていませんが、
今までの仕組みを大幅に書き換えたバージョンとなっています。

テンプレートの構文、コンポーネントで利用できるAPI、ステートを変更したときにUIを更新するために変更検知の仕組み(Reactiveな仕組み)が変更されています。
今までは、コンポーネントのステーを`set` APIなどで変更して、この変更がUIに反映されています。

```js
<p>{count} doubled is {double}</p>
<button on:click="set({ count: count + 1 })">+1</button>

<script>
	export default {
		data() {
			return {
				count: 0
			};
		},
        computed: {
			doubled: ({ count }) => count * 2
		}
	};
</script>
```

Svelte 3からは、次のように変更を検知したい文を`$`ラベル([JavaScriptのラベル](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label))でアノテーションします。このラベルで指定した変数などの値が変更されるとUIが更新されるコードがコンパイル時に生成されます。
(`$$invalidate`という更新を通知する処理が生成コードには含まれるようになります。)

```html
<p>{count} doubled is {doubled}</p>
<button on:click="{() => count += 1}">+1</button>
<script>
	let count = 0;
	$: doubled = count * 2;

	function handleClick() {
		count += 1;
	}
</script>
```

この宣言的なReactivityについては次のドキュメントやRFCを見るのが良さそうです。

- [Reactivity / Declarations • Svelte Tutorial](https://svelte.dev/tutorial/reactive-declarations)
- [rfcs/0003-reactive-declarations.md at master · sveltejs/rfcs](https://github.com/sveltejs/rfcs/blob/master/text/0003-reactive-declarations.md)

ものすごく簡単にまとめると、`@observable`のような[​まだ策定中のDecorator構文](https://github.com/tc39/proposal-decorators)ではなく、既にある[label文](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)と`$`というラベルを使って、コンパイル時に変数などをObservableを作り出すという手法のようです。

この他にも[Write less code](https://svelte.dev/blog/write-less-code)に寄せた変更などが多く含まれているため詳細は公式サイトを読むのがよさそうです。

- [Svelte • Cybernetically enhanced web apps](https://svelte.dev/)


----

[Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck](https://speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation)というスライドでは、Googleの主要なドメインにおけるCSP(Content Security Policy)の導入状態などについて書かれています。

Google domainでCSPがどの程度導入されているかのカバレッジや60%以上のXSSはCSPでブロックできている点について。
また、CSP導入の4つのLevelと導入ステップ、ホワイリストの問題とnonce-based CSP、CSPとデプロイのトレードオフについてなど。
CSPのディレクティブ(設定)によってはevalやinline codeなどが利用できないため、CSP対応のリファクタリング手法やステップについて書かれています。

このスライドでも紹介されているホワイリストの問題とnonce-based CSPについては次の記事も参照するとよさそうです。

- [Content Security Policy Level 3におけるXSS対策 - pixiv inside](https://inside.pixiv.blog/kobo/5137 "Content Security Policy Level 3におけるXSS対策 - pixiv inside")

----

<h1 class="site-genre">ヘッドライン</h1>

----

## alibaba/rax: \[ v1.0 released\] The fastest way to build universal application.
[github.com/alibaba/rax](https://github.com/alibaba/rax "alibaba/rax: \[ v1.0 released\] The fastest way to build universal application.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

ReactライクなAPIを持つUniversalなViewライブラリであるRax 1.0.0リリース。
Hooks APIにも対応している。


----

## Release v5.0.0 · sindresorhus/np
[github.com/sindresorhus/np/releases/tag/v5.0.0](https://github.com/sindresorhus/np/releases/tag/v5.0.0 "Release v5.0.0 · sindresorhus/np")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm publishするnp 5.0.0リリース。
2要素認証を新しく公開するパッケージに関しては自動で有効化、公開に失敗したときのロールバック処理の改善など


----

## Release Notes for Safari Technology Preview 80 | WebKit
[webkit.org/blog/8825/release-notes-for-safari-technology-preview-80/](https://webkit.org/blog/8825/release-notes-for-safari-technology-preview-80/ "Release Notes for Safari Technology Preview 80 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 80リリース。
ResizeObserverのサポート、`window.open`の第二引数で`noreferrer`のサポート、`contentWindow`のサポートなど。
またLegacy Safari Extensionsのサポート終了など


----

## Blog - Next.js 8.1 | Next.js
[nextjs.org/blog/next-8-1](https://nextjs.org/blog/next-8-1 "Blog - Next.js 8.1 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">AMP</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 8.1リリース。
AMPサポートが追加された。
コンポーネント内でAMPとの処理分岐でのhybrid対応、`next export`でAMPでの出力とバリデーション


----

## Release 10.0.0-beta.0 Reconcilertron · developit/preact
[github.com/developit/preact/releases/tag/10.0.0-beta.0](https://github.com/developit/preact/releases/tag/10.0.0-beta.0 "Release 10.0.0-beta.0 Reconcilertron · developit/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.0.0-beta.0リリース。
`Fragments`の安定化、条件分岐を含む描画のパフォーマンス改善、コンポーネントの上下関係を考慮した更新処理を行うように修正など


----

## Svelte 3: Rethinking reactivity
[svelte.dev/blog/svelte-3-rethinking-reactivity](https://svelte.dev/blog/svelte-3-rethinking-reactivity "Svelte 3: Rethinking reactivity")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

コンパイル前提のUIフレームワークであるSvelte 3リリース。
今までの仕組みを書き直したため、テンプレート構文、API、ウェブサイトが変更されている。
変更検知の仕組みが大きく変わり、`set` APIではなく、reactiveな変数を`$:`で宣言しコンパイル時に変更を追跡するコードを生成する方法に変更された


----
<h1 class="site-genre">アーティクル</h1>

----

## TypeScript再入門「がんばらないTypeScript」で、JavaScriptを“柔らかい”静的型付き言語に（gfx執筆） - エンジニアHub｜若手Webエンジニアのキャリアを考える！
[employment.en-japan.com/engineerhub/entry/2019/04/16/103000](https://employment.en-japan.com/engineerhub/entry/2019/04/16/103000 "TypeScript再入門「がんばらないTypeScript」で、JavaScriptを“柔らかい”静的型付き言語に（gfx執筆） - エンジニアHub｜若手Webエンジニアのキャリアを考える！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

ゆるい型付けの設定で始めるTypeScriptについて。


----

## A horrifying globalThis polyfill in universal JavaScript · Mathias Bynens
[mathiasbynens.be/notes/globalthis](https://mathiasbynens.be/notes/globalthis "A horrifying globalThis polyfill in universal JavaScript · Mathias Bynens")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">article</span></p>

`globalThis`のpolyfillとその動作原理についての解説。


----

## Experimental Node.js: testing the new performance hooks
[blog.logrocket.com/experimental-node-js-testing-the-new-performance-hooks-31fcdd2a747e](https://blog.logrocket.com/experimental-node-js-testing-the-new-performance-hooks-31fcdd2a747e "Experimental Node.js: testing the new performance hooks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Node.jsの`perf_hooks`の使い方についての記事。
モジュールのロード時間やURLへのリクエスト時間を計測を例に紹介している


----

## The perfect unit test
[javascriptplayground.com/the-perfect-javascript-unit-test/](https://javascriptplayground.com/the-perfect-javascript-unit-test/ "The perfect unit test")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Unit Testの書き方について。
テストケース名の書き方、テストをSetup、コード実行、Assertの3つのステップに分解して書くことについて


----

## A RealWorld Comparison of Front-End Frameworks with Benchmarks (2019 update)
[medium.freecodecamp.org/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075](https://medium.freecodecamp.org/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075 "A RealWorld Comparison of Front-End Frameworks with Benchmarks (2019 update)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span> <span class="jser-tag">benchmark</span></p>

"RealWorld"というベンチマークアプリの各JavaScriptフレームワークなどの実装を比較した記事。
パフォーマンス、出力されたコードのファイルサイズ、Line of Code(LOC)でそれぞれを比較した結果をまとめている

- [gothinkster/realworld: &quot;The mother of all demo apps&quot; — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more 🏅](https://github.com/gothinkster/realworld "gothinkster/realworld: &amp;quot;The mother of all demo apps&amp;quot; — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more 🏅")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck
[speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation](https://speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation "Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

GoogleにおけるCSPについてのスライド。Google domainのCSPのカバレッジや60%以上のXSSはCSPでブロックできている。
CSP導入の4つのLevelと導入ステップ、ホワイリストの問題とnonce-based CSP、CSPとデプロイのトレードオフについてなど。
CSP対応のリファクタリング手法などについて

- [Content Security Policy Level 3におけるXSS対策 - pixiv inside](https://inside.pixiv.blog/kobo/5137 "Content Security Policy Level 3におけるXSS対策 - pixiv inside")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## isInputPending: Facebook's first browser API contribution - Facebook Code
[code.fb.com/developer-tools/isinputpending-api/](https://code.fb.com/developer-tools/isinputpending-api/ "isInputPending: Facebook's first browser API contribution - Facebook Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

`navigator.scheduling.isInputPending()`を使いユーザーの操作中は、キューにためた処理を実行しないように制御する方法について。
ロード処理が完了するまでユーザーが操作できない時間であるFirst Input Delay (FID) を軽減する手法について

- [First Input Delay  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/05/first-input-delay "First Input Delay  |  Web  |  Google Developers")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Do you really know how a lockfile works for yarn and npm packages? | Snyk
[snyk.io/blog/making-sense-of-package-lock-files-in-the-npm-ecosystem/](https://snyk.io/blog/making-sense-of-package-lock-files-in-the-npm-ecosystem/ "Do you really know how a lockfile works for yarn and npm packages? | Snyk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">yarn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

yarnの`yarn.lock`、npmの`package-lock.json`が実際にどのように動いているのかについて。
アプリケーションとライブラリのロックファイルについて


----

## stryker-mutator/stryker: Mutation testing for JavaScript and friends
[github.com/stryker-mutator/stryker](https://github.com/stryker-mutator/stryker "stryker-mutator/stryker: Mutation testing for JavaScript and friends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">C#</span> <span class="jser-tag">scala</span></p>

Mutation testingライブラリ。
テストコードをテストするためのフレームワーク。
mochaやjestなど各種テストフレームワークと連携して動作する。

- [stryker-mutator/stryker-handbook: A comprehensive guide to the stryker ecosystem](https://github.com/stryker-mutator/stryker-handbook#readme "stryker-mutator/stryker-handbook: A comprehensive guide to the stryker ecosystem")
- [stryker/packages/core at master · stryker-mutator/stryker](https://github.com/stryker-mutator/stryker/tree/master/packages/core#readme "stryker/packages/core at master · stryker-mutator/stryker")
- [Blog - Stryker Mutator](https://stryker-mutator.io/blog/2017-01-17/introduction-to-mutation-testing "Blog - Stryker Mutator")

----

## lancedikson/bowser: a browser detector
[github.com/lancedikson/bowser](https://github.com/lancedikson/bowser "lancedikson/bowser: a browser detector")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span></p>

User-Agentを元にブラウザ名やバージョンなどを構造的なデータとして取得できるライブラリ


----

## sindresorhus/file-type: Detect the file type of a Buffer/Uint8Array/ArrayBuffer
[github.com/sindresorhus/file-type](https://github.com/sindresorhus/file-type "sindresorhus/file-type: Detect the file type of a Buffer/Uint8Array/ArrayBuffer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Content sniffingをしてファイルの種類を判定するNode.jsライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Front-end Developer Handbook 2019 - Learn the entire JavaScript, CSS and HTML development practice!
[frontendmasters.com/books/front-end-handbook/2019/](https://frontendmasters.com/books/front-end-handbook/2019/ "Front-end Developer Handbook 2019 - Learn the entire JavaScript, CSS and HTML development practice!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">links</span></p>

フロントエンド開発についての概要や技術項目ごとのリソースをまとめた電子書籍の2019年版


----
