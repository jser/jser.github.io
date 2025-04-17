---
title: "2025-04-17のJS: Zod 4 beta、Next.js 15.3とRspack、LLMを使ったテストのマイグレーション"
author: "azu"
layout: post
date: 2025-04-17T14:36:16.916Z
category: JSer
tags:
- Next.js
- React
- TypeScript
- test
- css

---

JSer.info #732 - Zod 4 betaがリリースされました。

- [Introducing Zod 4 beta | Zod Docs](https://v4.zod.dev/v4)

パフォーマンスとBundle Sizeの改善が行われ、Tree Shaking可能なAPIを提供する`@zod/mini`と`@zod/core`パッケージが公開されています。また、再帰も可能なオブジェクトの定義をする`z.interface()` API、メタデータを管理する`z.registry()` API、JSONスキーマ変換のための`toJSONSchema()` APIなどが追加されています。その他にも文字列のTop Level APIの追加や変更、エラーメッセージを`message`から`error`パラメータへ変更など多くの変更が含まれています。

----

Next.js 15.3がリリースされ、Rspackをビルドツールとしてサポートするようになりました。

- [Next.js 15.3 | Next.js](https://nextjs.org/blog/next-15-3)
- [Rspack joins the Next.js ecosystem - Rspack](https://rspack.dev/blog/rspack-next-partner)

Next.js 15.3では、Turbopackを`next build`でも利用可能になったほか、Rspackのサポート、クライアントサイドの計測を行う`instrumentation-client.{js,ts}`のサポート、Navigation Hooksのサポートなどが追加されています。また、`useLinkStatus`の追加やTypeScript LSPのパフォーマンス改善も行われました。実験的な機能として`<Link unstable_dynamicOnHovertrue>`のサポートなども含まれています。

----

AirbnbがEnzymeからReact Testing Libraryへの大規模なテスト移行をLLMを活用して行った事例について紹介されています。

- [Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

移行プロセスをステップ化し、再試行ループの導入、関連するテストや移行ガイドラインをコンテキストとして追加することで、当初は75%のテストが自動的に移行できました。さらに、失敗したファイルにどのステップでうまくいかなかったかをコメントとして残し、それらのファイルを使って学習することで、最終的には97%まで自動的に移行できるようになったとのことです。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bun v1.2.9 | Bun Blog
[bun.sh/blog/bun-v1.2.9](https://bun.sh/blog/bun-v1.2.9 "Bun v1.2.9 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.9リリース。
Redisクライアントである`Bub.redis`の追加、`require.extensions`のサポート、`require.resolve`の`paths`オプションのサポートなど


----

## Introducing Zod 4 | Zod Docs
[v4.zod.dev/v4](https://v4.zod.dev/v4 "Introducing Zod 4 | Zod Docs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Zod 4 betaリリース。
パフォーマンスの改善、Bundle Sizeの改善、Tree Shaking可能なAPIを提供する`@zod/mini`と`@zod/core`パッケージを公開。
再帰も可能なオブジェクトの定義をする`z.interface()` APIの追加、メタデータを管理数ｒ`z.registry()` API、`toJSONSchema()` APIの追加。
文字列のTop Level APIの追加や変更、エラーメッセージを`message`から`error`パラメータへ変更など


----

## Next.js 15.3 | Next.js
[nextjs.org/blog/next-15-3](https://nextjs.org/blog/next-15-3 "Next.js 15.3 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 15.3リリース。
Turbopackを`next build`でも利用可能に、Rspackのサポート、`instrumentation-client.{js,ts}`のサポート、Navigation Hooksのサポート。
`useLinkStatus`の追加、TypeScript LSPのパフォーマンス改善。
実験的な機能として`<Link unstable_dynamicOnHovertrue>`のサポートなど


----

## Release 0.12.0 | StyleX
[stylexjs.com/blog/v0.12.0](https://stylexjs.com/blog/v0.12.0 "Release 0.12.0 | StyleX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

StyleX v0.12.0リリース。
パフォーマンスの改善、ESLintプラグインに`no-legacy-media-queries`を追加。
`@stylexjs/esbuild-plugin`/`@stylexjs/nextjs-plugin`/`@stylexjs/webpack-plugin`などを非推奨に変更など


----

## Shipping Temporal | SpiderMonkey JavaScript/WebAssembly Engine
[spidermonkey.dev/blog/2025/04/11/shipping-temporal.html](https://spidermonkey.dev/blog/2025/04/11/shipping-temporal.html "Shipping Temporal | SpiderMonkey JavaScript/WebAssembly Engine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

SpinderMonkeyがECMAScript Proposal Stage 3のTemporalの実装がFirefox 139でリリースされる。


----

## Astro 5.7 | Astro
[astro.build/blog/astro-570/](https://astro.build/blog/astro-570/ "Astro 5.7 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 5.7リリース。
実験的なFont APIの追加、Sessions APIがStableに変更、SVGファイルをコンポーネントとして読み込めるように、`astro:config`がStableへ変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium
[medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b "Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">test</span> <span class="jser-tag">LanguageModel</span> <span class="jser-tag">article</span></p>

EnzymeからReact Testing Libraryへの移行をLLMを活用してマイグレーションした話。
移行のプロセスのステップ化、再試行ループ、コンテキストに関連するテスト/移行ガイドラインの追加することで75%は移行できた。
そこからどのステップでうまくいっていないかをコメントに残して、そのファイルを使った学習をすることで97%まで自動的に移行ができたという話


----

## Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext
[blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/ "Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">article</span></p>

Cloudflare WorkersでNext.jsを動かすOpenNextについて。


----

## WebAssembly の歩き方
[zenn.dev/canary\_techblog/articles/47af6331b4ecfb](https://zenn.dev/canary_techblog/articles/47af6331b4ecfb "WebAssembly の歩き方")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

WebAssemblyとはどういうものかについて。
WebAssemblyが定義しているもの、バイトコード表現とテキスト表現、仕様の実装であるEmbedderについて


----

## Rspack joins the Next.js ecosystem - Rspack
[rspack.dev/blog/rspack-next-partner](https://rspack.dev/blog/rspack-next-partner "Rspack joins the Next.js ecosystem - Rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

Next.jsのRspackサポートについて


----

## Advanced React in the Wild
[largeapps.dev/case-studies/advanced/](https://largeapps.dev/case-studies/advanced/ "Advanced React in the Wild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Reactで書かれたアプリケーションのパフォーマンス改善の事例集


----

## Default styles for h1 elements are changing | MDN Blog
[developer.mozilla.org/en-US/blog/h1-element-styles/](https://developer.mozilla.org/en-US/blog/h1-element-styles/ "Default styles for h1 elements are changing | MDN Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">browser</span> <span class="jser-tag">css</span></p>

セクションに基づいた暗黙的な`<h1>`要素のデフォルトのスタイル(UAのスタイル)が変更される。
Firefox 138、Chrome 136以降にこの変更が含まれる


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)
[github.com/goldbergyoni/nodejs-testing-best-practices](https://github.com/goldbergyoni/nodejs-testing-best-practices "goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">test</span> <span class="jser-tag">document</span></p>

Node.jsでのテストについてのドキュメント


----

## lightpanda-io/browser: Lightpanda: the headless browser designed for AI and automation
[github.com/lightpanda-io/browser](https://github.com/lightpanda-io/browser "lightpanda-io/browser: Lightpanda: the headless browser designed for AI and automation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">zig</span> <span class="jser-tag">browser</span> <span class="jser-tag">software</span></p>

ZigとV8を使って書かれたヘッドレスブラウザ


----

## Ray-D-Song/lexe: Package your Node.js application into a single executable file, but only 10MB.🔥
[github.com/Ray-D-Song/lexe?tab&#x3D;readme-ov-file](https://github.com/Ray-D-Song/lexe?tab=readme-ov-file "Ray-D-Song/lexe: Package your Node.js application into a single executable file, but only 10MB.🔥")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

LLRTをRuntimeとして使ったSingle Executable Binaryを作成するツール。
Node.jsの一部に互換のあるAPIを提供し、バイナリサイズが小さいという特徴がある


----
<h1 class="site-genre">書籍関係</h1>

----

## 「型システムのしくみ」発売のお知らせ - まめめも
[mametter.hatenablog.com/entry/2025/04/10/063009](https://mametter.hatenablog.com/entry/2025/04/10/063009 "「型システムのしくみ」発売のお知らせ - まめめも")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span> <span class="jser-tag">program</span></p>

TypeScriptのサブセットの型チェッカを実装していく型システムについての書籍


----
