---
title: "2021-06-01: Jest 27, vanilla-extract 1.0.0, Learn CSS"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-05-31T14:26:57.997Z
category: JSer
tags:
- TypeScript
- CSS
- Tools
- testing
- node.js

---

JSer.info #542 - Jest 27.0.0 릴리스.

- [Release 27.0.0 · Facebook/jest](https://github.com/facebook/jest/releases/tag/v27.0.0)
- [Jest 27: New Defaults for Jest, 2021 edition ⏩ · Jest](https://jestjs.io/blog/2021/05/25/jest-27)

Jest 27.0.0는 지금까지의 디폴트(defaults)가 크게 바뀌는 릴리스.

`testEnvironment`의 기본을 `jsdom`에서 `node`로 변경, jest-circus를 디폴트로 전환, Fake Timers의 디폴트로 @sinonjs/fake-timer 기반으로 변경하여 최신화 했다.
추가된 기능으로는 실패한 테스트를 대화형 모드(interactive mode)로 단계별로 실행할 수 있도록 했고, Inline Snapshots를 Prettier 의존 없이 실행 할 수 있도록 개선했다.
또, done의 중복 호출을 에러로 취급하며, Promise 반환과 done을 혼용하여 사용하는 것을 금지했고 TypeScript의 타입을 정제했다.

----

CSS Variables를 사용할 수 없는 CSS Modules의 문제점을 해결하는 동시에 타입 안전한 CSS in JS를 목표로 하고 있는 vanilla-extract 1.0.0 릴리스.

- [vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.](https://vanilla-extract.style/)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🧁🎉 Announcing vanilla-extract v1.0!<br><br>💪 Locally scoped, type-safe styles, variables + themes.<br>🦄 Minimal abstraction over CSS.<br>🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack.<br>✅ Now stable + production ready.<br><br>🙇‍♂️ Enjoy!<a href="https://t.co/Ejaf4anfbj">https://t.co/Ejaf4anfbj</a></p>&mdash; 🧁🍨 Mark Dalgleish (@markdalgleish) <a href="https://twitter.com/markdalgleish/status/1398158090294292482?ref_src=twsrc%5Etfw">May 28, 2021</a></blockquote>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

vanilla-extract는 [CSS Modules](https://github.com/css-modules/css-modules)의 개발자 중 한 사람인 [Mark Dalgleish](https://twitter.com/markdalgleish)를 중심으로 개발하고 있는 CSS Modules-in-TypeScript한 CSS 프레임워크다.
TypeScript로 스타일을 `.css.ts`에 작성하며 컴파일 하면 class 속성에 지정한 내용을 CSS 파일로 생성해주는, 특정 프레임워크에 의존하지 않는 툴킷.

최근에 다양한 CSS in JS가 등장하고 있는데 아래 글에 CSS 관련 접근법이 정리돼 있으니 참고.

- [A Thorough Analysis of CSS-in-JS | CSS-Tricks](https://css-tricks.com/a-thorough-analysis-of-css-in-js/)
- [Libraries to look out for · Issue #8 · andreipfeiffer/css-in-js](https://github.com/andreipfeiffer/css-in-js/issues/8)

----

web.dev에서 CSS를 학습할 수 있는 [Learn CSS](https://web.dev/learn/css/) 튜토리얼 강좌 공개.
Box Model, Selector, Specificity, CSS 단위 등 기본 개념과 Grid, Flexbox 등 레이아웃 뿐 아니라 Color, margin 등 CSS 속성 설명, 의사 클래스 및 의사 요소 등 CSS를 주제별로 폭넓게 다루고 있다.


----

<h1 class="site-genre">헤드라인</h1>

----

## sinon/CHANGELOG.md at master · sinonjs/sinon
[github.com/sinonjs/sinon/blob/master/CHANGELOG.md#1110--2021-05-25](https://github.com/sinonjs/sinon/blob/master/CHANGELOG.md#1110--2021-05-25 "sinon/CHANGELOG.md at master · sinonjs/sinon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

sinon.js 11.1.0 릴리스.
Promise를 Fake하는 `sinon.promise()` 구현.


----

## Jest 27: New Defaults for Jest, 2021 edition ⏩ · Jest
[jestjs.io/blog/2021/05/25/jest-27](https://jestjs.io/blog/2021/05/25/jest-27 "Jest 27: New Defaults for Jest, 2021 edition ⏩ · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 27 릴리스. 

디폴트(defaults)가 크게 바뀌는 릴리스.
`testEnvironment`의 기본을 `jsdom`에서 `node`로 변경, jest-circus를 디폴트로 전환, Fake Timers의 디폴트로 @sinonjs/fake-timer 기반으로 변경하여 최신화.
추가된 기능으로는 실패한 테스트를 대화형 모드(interactive mode)로 단계별로 실행할 수 있도록 했고, Inline Snapshots를 Prettier 의존 없이 실행 할 수 있도록 개선.
또, done의 중복 호출을 에러로 취급하며, Promise 반환과 done을 혼용하여 사용하는 것을 금지했고 TypeScript의 타입을 정제.

- [Release 27.0.0 · facebook/jest](https://github.com/facebook/jest/releases/tag/v27.0.0 "Release 27.0.0 · facebook/jest")

----

## Announcing TypeScript 4.3 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-3/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-3/ "Announcing TypeScript 4.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.3 릴리스.

setter에 getter와 다른 타입을 지정할 수 있도록 변경, `override` 키워드 추가, Template String Type 개선.
Private Class Elements(fields/methods/accessors) 지원, `static` Index Signature 지원.
`ConstructorParameters`에서 Abstract class 지원, Generics에 의한 타입의 추론 범위 축소 개선, Promise 객체를 조건식에 넘겨버리는 실수 검사 추가.
그 외로 `.tsbuildinfo` 파일 크기 개선하고 watch 시의 첫 빌드 성능 개선.

----

## Announcing Vendure v1.0 | Vendure E-commerce
[www.vendure.io/blog/2021/05/announcing-vendure-v1.0/](https://www.vendure.io/blog/2021/05/announcing-vendure-v1.0/ "Announcing Vendure v1.0 | Vendure E-commerce")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">GraphQL</span></p>

GraphQL/TypeScript 기반의 이커머스 프레임워크 Vendure v1.0 릴리스.

- [vendure-ecommerce/vendure: A headless GraphQL ecommerce framework for the modern web](https://github.com/vendure-ecommerce/vendure "vendure-ecommerce/vendure: A headless GraphQL ecommerce framework for the modern web")

----

## Optimized images for Nuxt
[image.nuxtjs.org/](https://image.nuxtjs.org/ "Optimized images for Nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Nuxt.js 용 이미지 최적화 도구.


----

## ECMAScript proposal updates @ 2021-05 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2021/05/29/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2021/05/29/ecmascript-proposal-update "ECMAScript proposal updates @ 2021-05 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2021년 5월 TC39 미팅에서 Stage가 변경된 Proposal 정리.
Top-Level await와 RegExpo Match Indices가 Stage 4가 됐으며 ES2022에 포함.


----

## New Release: 2.13.0
[jshint.com/blog/2021-05-30/release-2-13-0/](https://jshint.com/blog/2021-05-30/release-2-13-0/ "New Release: 2.13.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.13.0 릴리스.
`export * as ns from`, `import.meta`, Dynamic `import()`, Optional Chaining, Nullish Coalescing 지원.

----

## vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.
[vanilla-extract.style/](https://vanilla-extract.style/ "vanilla-extract — Zero-runtime Stylesheets-in-TypeScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

vanilla-extract v1.0 릴리스.

TypeScript로 스타일을 `.css.ts`에 작성하며 컴파일 하면 class 속성에 지정한 내용을 CSS 파일로 생성해주는 특정 프레임워크에 의존하지 않는 툴킷.
빌드 시에 정적으로 펼쳐지는 API와 실행시 동작하는 Dynamic API, webpack이나 Vite 등의 각종 빌드 도구를 지원하는 플러그인 지원.

- [🧁🍨 Mark Dalgleish on Twitter: &amp;quot;🧁🎉 Announcing vanilla-extract v1.0! 💪 Locally scoped, type-safe styles, variables + themes. 🦄 Minimal abstraction over CSS. 🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack. ✅ Now stable + production ready. 🙇‍♂️ Enjoy! https://t.co/Ejaf4anfbj&amp;quot; / Twitter](https://twitter.com/markdalgleish/status/1398158090294292482 "🧁🍨 Mark Dalgleish on Twitter: &amp;amp;quot;🧁🎉 Announcing vanilla-extract v1.0! 💪 Locally scoped, type-safe styles, variables + themes. 🦄 Minimal abstraction over CSS. 🛠 Framework agnostic, w/ integrations for webpack, esbuild, Vite + Snowpack. ✅ Now stable + production ready. 🙇‍♂️ Enjoy! https://t.co/Ejaf4anfbj&amp;amp;quot; / Twitter")

----

## Lit 2.0: Meet Lit, all over again! – Lit
[lit.dev/blog/2021-04-21-lit-2.0-meet-lit-all-over-again/](https://lit.dev/blog/2021-04-21-lit-2.0-meet-lit-all-over-again/ "Lit 2.0: Meet Lit, all over again! – Lit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Lit 2.0 RC 릴리스.
lit-html과 LitElement를 하나로 정리하여 lit 패키지로 공개, 웹사이트도 함께 개편.
파일 크기 및 성능 개선하고 SSR도 대응.

- [Lit Launch Event - YouTube](https://www.youtube.com/watch?v=f1j7b696L-E "Lit Launch Event - YouTube")
- [Introducing &amp;quot;Lit&amp;quot; for Web Components](https://zenn.dev/takanorip/articles/640f9fe9c6c8ca "Introducing &amp;amp;quot;Lit&amp;amp;quot; for Web Components")

----
<h1 class="site-genre">아티클</h1>

----

## 5 steps to faster web fonts /// Iain Bean
[iainbean.com/posts/2021/5-steps-to-faster-web-fonts/](https://iainbean.com/posts/2021/5-steps-to-faster-web-fonts/ "5 steps to faster web fonts /// Iain Bean")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span> <span class="jser-tag">article</span></p>

웹 폰트 로딩을 주제로한 연재글.
`font-display`를 활용한 텍스트 표시와 전환 타이밍 등 정리.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Learn CSS
[web.dev/learn/css/](https://web.dev/learn/css/ "Learn CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span></p>

CSS를 학습할 수 있는 튜토리얼 강좌 공개.
Box Model, Selector, Specificity, CSS 단위 등 기본 개념과 Grid, Flexbox 등 레이아웃 뿐 아니라 Color, margin 등 CSS 속성 설명, 의사 클래스 및 의사 요소 등 CSS를 주제별로 폭넓게 다룸.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>


----

## xqq/mpegts.js: HTML5 MPEG2-TS Stream Player
[github.com/xqq/mpegts.js](https://github.com/xqq/mpegts.js "xqq/mpegts.js: HTML5 MPEG2-TS Stream Player")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">library</span></p>

fiv.js를 기반으로 한 MPEG-2 TS 스트림 플레이어 라이브러리.
HTTPS와 WebSocket을 사용한 MPEG-2 TS 스트림 재생 기능.
DVB / ISDB TV나 감시카메라 등 저지연(low-latency), 저사양 머신에서도 최적화된 스프리밍을 하는데 목적을 두고 있음. flv.js 기반이므로 FLV Container도 지원.

----

## wwwtyro/candygraph: Fast by default, flexible 2D plotting library.
[github.com/wwwtyro/candygraph](https://github.com/wwwtyro/candygraph "wwwtyro/candygraph: Fast by default, flexible 2D plotting library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">graphic</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

빠른 성능에 주 목적을 둔 캔버스 기반의 2D 그래프 렌더링 라이브러리.


----

## lume/autolayout: Apple&#039;s Auto Layout and Visual Format Language for JavaScript (using cassowary constraints)
[github.com/lume/autolayout](https://github.com/lume/autolayout "lume/autolayout: Apple&#039;s Auto Layout and Visual Format Language for JavaScript (using cassowary constraints)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Auto Layout과 Visual Format Language를 구현한 라이브러리.


----

## plantain-00/type-coverage: A CLI tool to check type coverage for typescript code
[github.com/plantain-00/type-coverage](https://github.com/plantain-00/type-coverage "plantain-00/type-coverage: A CLI tool to check type coverage for typescript code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

타입스크립트의 타입 커버지리를 측정, 출력하는 도구.

----
<h1 class="site-genre">도서</h1>

----

## WebAssembly: The Definitive Guide
[learning.oreilly.com/library/view/webassembly-the-definitive/9781492089834/](https://learning.oreilly.com/library/view/webassembly-the-definitive/9781492089834/ "WebAssembly: The Definitive Guide")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">book</span></p>

2021년 12월 출간 예정인 WebAssebly를 주제로한 도서.


----
