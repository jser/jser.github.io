---
title: "2021-02-16: TypeScript 4.2 RC, WebdriverIO v7, Nuxt.js 2.15.0"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-02-16T03:07:05.874Z
category: JSer
tags:
- TypeScript
- Vue
- HTML
- node.js
- Fetch

---

JSer.info #527 - TypeScript 4.2 RC 릴리스.

- [Announcing TypeScript 4.2 RC | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/)

Tuple Types에서 Rest Element 지원, Type Alias의 타입 추론 구조를 개선하여 표시되는 타입이 알기 쉽도록 수정.
또, 오브젝트가 아닌 오퍼랜드에 대해서 `in` 연산자를 사용한 경우 컴파일 에러 나도록 변경.
그 외로는 `noPropertyAccessFromIndexSignature` 옵션 추가, `abstract new` 지원, `--explainFiles` 플러그가 추가됐다.

[TypeScript 4.2 Beta](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-beta/) 시점에 Template Literal 식을 기본적으로 Template Literal Type으로서 다루도록 변경되었으나 이 동작이 [의도한대로 작동하지 않는 경우](https://github.com/microsoft/TypeScript/issues/42589)가 있어 revert하여 기본적으로는 `string`으로서 다루도록 한다. 
4.2 RC에서는 Template Literal 식에 `as const`를 붙힌 경우에만 Template Literal Type으로서 다루도록 변경됐다.

```ts
declare const yourName: string;

// 'bar' has type '`hello ${string}`'.
const bar = `hello ${yourName}` as const;
//                              ^^^^^^^^

// 'baz' has type 'string'.
const baz = `hello ${yourName}`;
```

---

WebdriverIO v7 릴리스.

- [WebdriverIO v7 Released | WebdriverIO](https://webdriver.io/blog/2021/02/09/webdriverio-v7-released/)


Node.js 10 지원 종료, TypeScript로 재작성, Cucumber v7으로 갱신, Lightouse 연동 개선.
`browser.checkPWA()` 추가, `@babel/register`나 `ts-node`가 설치돼 있는 경우에 자동으로 컴파일하는 [`autoCompileOpts`](https://webdriver.io/docs/configurationfile) 옵션 추가.

---

Nuxt.js 2.15.0 릴리스.

- [Release v2.15.0 · nuxt/nuxt.js](https://github.com/nuxt/nuxt.js/releases/tag/v2.15.0)
- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide)
- [nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js](https://github.com/nuxt-contrib/jiti)

비호환 변경 사항으로 Node.js 10 지원 종료, `@nuxt/components` v2으로 갱신 됐다.
이와 함께 `@nuxt/components` v2으로 갱신하는 마이그레이션 가이드도 공개됐다.

- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide "nuxt/components: Scan and auto import components for Nuxt.js 2.13+")

그 외로는 Yarn의 Plug'n'Play 지원, PostCSS 8을 opt-in으로 지원한다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v4.0.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v4.0.0](https://github.com/lerna/lerna/releases/tag/v4.0.0 "Release v4.0.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span></p>

lerna 4.0.0 릴리스.
Node.js 10 미만 지원 종료, 의존 모듈 갱신.


----

## Announcing TypeScript 4.2 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-2-rc/ "Announcing TypeScript 4.2 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.2 RC 릴리스.
Tuple Types에서 Rest Element 지원, Type Alias의 타입 추론 개선, 오브젝트가 아닌 오퍼랜드에 대해서 `in` 연산자를 사용하는지 검사, `noPropertyAccessFromIndexSignature` 옵션 추가, `abstract new` 지원, `--explainFiles` 플래그 추가.


----

## Release v2.0.0 · markedjs/marked
[github.com/markedjs/marked/releases/tag/v2.0.0](https://github.com/markedjs/marked/releases/tag/v2.0.0 "Release v2.0.0 · markedjs/marked")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

marked 2.0.0 릴리스.


----

## eBay Launches Marko 5
[tech.ebayinc.com/engineering/ebay-launches-marko-5/](https://tech.ebayinc.com/engineering/ebay-launches-marko-5/ "eBay Launches Marko 5")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">template</span> <span class="jser-tag">ReleaseNote</span></p>

Marko 5 릴리스.
컴파일러로 바벨을 사용할 수 있도록, webpack 및 Rollup 환경 번들 대응, `@marko/testing-library` 추가, VScode 등 에디터 확장 프로그램 지원.

- [Upgrading to Marko 5](https://markojs.com/docs/marko-5-upgrade/ "Upgrading to Marko 5")

----

## WebdriverIO v7 Released | WebdriverIO
[webdriver.io/blog/2021/02/09/webdriverio-v7-released/](https://webdriver.io/blog/2021/02/09/webdriverio-v7-released/ "WebdriverIO v7 Released | WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v7 릴리스.
Node.js 10 지원 종료, TypeScript로 재작성, Cucumber v7으로 갱신, Lightouse 연동 개선.
`browser.checkPWA()` 추가, `@babel/register`이나 `ts-node`가 선치돼 있는 경우 자동으로 컴파일 하는 `autoCompileOpts` 추가.


----

## Release v2.15.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.15.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.15.0 "Release v2.15.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxtjs 2.15.0 릴리스.
Node.js 10 지원 종료, Yarn의 Plug'n'Play 지원, `@nuxt/components` v2으로 갱신.

- [nuxt/components: Scan and auto import components for Nuxt.js 2.13+](https://github.com/nuxt/components#migration-guide "nuxt/components: Scan and auto import components for Nuxt.js 2.13+")
- [nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js](https://github.com/nuxt-contrib/jiti "nuxt-contrib/jiti: Runtime Typescript and ESM support for Node.js")

----
<h1 class="site-genre">아티클</h1>

----

## Dynamic Static Typing In TypeScript — Smashing Magazine
[www.smashingmagazine.com/2021/01/dynamic-static-typing-typescript/](https://www.smashingmagazine.com/2021/01/dynamic-static-typing-typescript/ "Dynamic Static Typing In TypeScript — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">express</span></p>

express 라우팅 타입을 작성해 가면서 TypeScript 고급 타입에 대해서 살펴볼 수 있는 튜토리얼.


----

## Generators in Javascript: How to use them - DEV Community 👩‍💻👨‍💻
[dev.to/karimelghamry/generators-in-javascript-how-to-use-them-372d](https://dev.to/karimelghamry/generators-in-javascript-how-to-use-them-372d "Generators in Javascript: How to use them - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

generator 함수의 사용 방법과 유스케이스에 대해 소개.


----

## Lazy Load Routes in Vue with webpack Dynamic Comments | CSS-Tricks
[css-tricks.com/lazy-load-routes-in-vue-with-webpack-dynamic-comments/](https://css-tricks.com/lazy-load-routes-in-vue-with-webpack-dynamic-comments/ "Lazy Load Routes in Vue with webpack Dynamic Comments | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

Vue Router를 사용한 지연 로드에 대한 소개 글.
webpack의 chunk 분할, `webpackChunkName`의 chunk 파일명 지정 등에 대해서 소개.


----

## Just(js): On Javascript Performance
[just.billywhizz.io/blog/on-javascript-performance-01/](https://just.billywhizz.io/blog/on-javascript-performance-01/ "Just(js): On Javascript Performance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">C++</span></p>

Just(js)는 어떤 최적화 방식으로 Techempower의 벤치마크 스코어를 올렸는지에 대해서 설명한다.

- [Introduction - TechEmpower Framework Benchmarks](https://www.techempower.com/benchmarks/#section=intro "Introduction - TechEmpower Framework Benchmarks")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Write videos in React | Remotion
[www.remotion.dev/](https://www.remotion.dev/ "Write videos in React | Remotion")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span> <span class="jser-tag">library</span></p>

React를 사용해 동영상을 만들기 위한 환경 라이브러리.
JSX를 이용해 효과를 선언적으로 작성하고 실제 동작하는 애니메이션을 동영상 파일로 추출할 수 있다. 


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## tildeio/simple-html-tokenizer: A lightweight JavaScript library for tokenizing non-`<script>` HTML expected to be found in the `<body>` of a document
[github.com/tildeio/simple-html-tokenizer](https://github.com/tildeio/simple-html-tokenizer "tildeio/simple-html-tokenizer: A lightweight JavaScript library for tokenizing non-`<script>` HTML expected to be found in the `<body>` of a document")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">library</span></p>

HTML를 파싱하여 토크나이징하는 라이브러리.


----

## Ethan-Arrowood/undici-fetch: A WHATWG Fetch implementation based on @nodejs/undici
[github.com/Ethan-Arrowood/undici-fetch](https://github.com/Ethan-Arrowood/undici-fetch "Ethan-Arrowood/undici-fetch: A WHATWG Fetch implementation based on @nodejs/undici")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">library</span></p>

Node.js 용 Fetch API 구현 라이브러리.
undici을 기반으로 개발돼 있다.

- [nodejs/undici: An HTTP/1.1 client, written from scratch for Node.js](https://github.com/nodejs/undici "nodejs/undici: An HTTP/1.1 client, written from scratch for Node.js")

----

## vercel/nft: Node.js dependency tracing utility
[github.com/vercel/nft](https://github.com/vercel/nft "vercel/nft: Node.js dependency tracing utility")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">library</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">TypeScript</span></p>

JavaScript 파일의 의존 관계를 추적하는 라이브러리.
`node_modules` 등을 포함하여 특정 모듈이 의존하는 파일 경로를 가져올 수 있다.


----

## gzuidhof/sunder: A minimal framework for Service Workers (such as Cloudflare Workers).
[github.com/gzuidhof/sunder](https://github.com/gzuidhof/sunder "gzuidhof/sunder: A minimal framework for Service Workers (such as Cloudflare Workers).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Service Worker나 Cloudflare Worker 용 라우팅 라이브러리.


----

## zeroturnaround/sql-formatter: A whitespace formatter for different query languages
[github.com/zeroturnaround/sql-formatter](https://github.com/zeroturnaround/sql-formatter "zeroturnaround/sql-formatter: A whitespace formatter for different query languages")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SQL</span> <span class="jser-tag">library</span></p>

JavaScript로 작성한 SQL 포멧터.


----

## mizdra/eslint-interactive
[github.com/mizdra/eslint-interactive](https://github.com/mizdra/eslint-interactive "mizdra/eslint-interactive")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

ESLint를 규칙별로 체크하고, 규칙별로 `--fix`를 이용한 수정을 인터랙티브하게 할 수 있는 커맨드라인 도구.

- [rule 별로 빠르게 eslint --fix 할 수 있는 도구를 만들었다 - mizdra's blog](https://www.mizdra.net/entry/2021/02/11/211856 "rule 별로 빠르게 eslint --fix 할 수 있는 도구를 만들었다 - mizdra&#x27;s blog")(일본어)

----
