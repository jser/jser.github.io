---
title: "2020-09-15: playwright 1.4.0, snowpack 2.11.1, Migrating to JavaScript modules(Chrome Dev Tools)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-09-15T02:59:01.892Z
category: JSer
tags:
- playwright
- snowpack
- modules

---

JSer.info #505 - playwright 1.4.0 릴리스.

단일 API로 Chrome, Firefox, WebKit을 자동화할 수 있는 크로스 브라우저 웹 자동화 라이브러리 playwright 1.4.0 릴리스.

- [Release v1.4.0 · microsoft/playwright](https://github.com/microsoft/playwright/releases/tag/v1.4.0)

playwright 1.4에서는 의존하는 브라우저가 Chromium 86 / Firefox 80 / WebKit 14 기반으로 각각 갱신됐다.
API는 `elementHandle.waitForElementState()`와 `elementHandle.waitForSelector()` 등이 추가됐다.
그 외 실험적 기능으로 영상 녹화 기능이 추가됐다.

또, 함께 [Playwright CLI](https://github.com/microsoft/playwright-cli)가 정식 릴리스됐다.

[Playwright CLI](https://github.com/microsoft/playwright-cli)는 조작을 기록하고 재생하는 코드 생성, 요소 Inspect, 스크린샷, PDF 생성 등을 할 수 있는 커맨드 라인 도구다.

----

프런트엔드 용 빌드 도구인 Snowpack 2.11.1 릴리스.

- [Release snowpack@2.11.1 · pikapkg/snowpack](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1)

[@snowpack/plugin-optimize](https://github.com/pikapkg/snowpack/tree/master/plugins/plugin-optimize)라고 하는 최적화 플러그인이 추가됐다.
[@snowpack/plugin-optimize](https://github.com/pikapkg/snowpack/tree/master/plugins/plugin-optimize)는 [esbuild](https://github.com/evanw/esbuild)로 JavaScript를, [CSSO](https://github.com/css/csso)로 CSS를, [HTMLMinifier](https://github.com/kangax/html-minifier)로 HTML을 각각 압축한다. 이와 함께 [`<link rel="modulepreload">`](https://developers.google.com/web/updates/2017/12/modulepreload)를 사용한 미리 가져오기에 대응하고 있다.

그 외로 `build --watch`에서 HMR / Livereload를 대응하고 `@snowpack/plugin-webpack`에서도 HTML을 압축하는 변경이 포함됐다.

----

[DevTools architecture refresh: Migrating to JavaScript modules  |  Web](https://developers.google.com/web/updates/2020/09/migrating-to-js-modules)

위 글에는 Chrome Dev Tools의 기반 코드를 ES Modules로 이전한 배경과 과정이 정리돼 있다.

Chrome Dev Tools(원래는 WebKit)는 ES Modules가 책정되기 전부터 개발돼 왔기 때문에 독자적인 모듈 구조를 가지고 있었다.
표준화된 ES Modules의 장점 등을 고려하여 어떻게 자체 구조에서 ES Modules로 이전했는지 소개돼 있다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Node v14.10.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.10.0/](https://nodejs.org/en/blog/release/v14.10.0/ "Node v14.10.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 14.10.0 릴리스.
무작위 integer를 반환하는 `crypto.randomInt()` 추가, `performance.eventLoopUtilization()`가 추가됐다.


----

## Release 2.0.0 (2020-09-10) · serverless/serverless
[github.com/serverless/serverless/releases/tag/v2.0.0](https://github.com/serverless/serverless/releases/tag/v2.0.0 "Release 2.0.0 (2020-09-10) · serverless/serverless")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">serverless</span></p>

Serverless Framework인 serverless 2.0 릴리스.
Node.js 10 미만 지원 종료, `slss`의 alias 삭제, AWS `httoApi`의 `timeout` 설정 삭제.


----

## Release v1.4.0 · denoland/deno
[github.com/denoland/deno/releases/tag/v1.4.0](https://github.com/denoland/deno/releases/tag/v1.4.0 "Release v1.4.0 · denoland/deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.4.0 릴리스.
WebSocket API 구현, `Deno.systemMemoryInfo()`가 추가.
또, 불안정 기능으로 `deno run --watch`, `deno test --coverage`가 추가됐다.


----

## Release snowpack@2.11.1 · pikapkg/snowpack
[github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.11.1 "Release snowpack@2.11.1 · pikapkg/snowpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

snowpack 2.11.1 릴리스.
esbuild 등을 기반으로 한 `@snowpack/plugin-optimize` 추가, `build --watch`에서 HMR/Livereload 대응.
또, `@snowpack/plugin-webpack`에서도 HTML을 압축하도록 변경됐다.


----

## ten1seven/what-input: A global utility for tracking the current input method (mouse/pointer, keyboard or touch).
[github.com/ten1seven/what-input](https://github.com/ten1seven/what-input "ten1seven/what-input: A global utility for tracking the current input method (mouse/pointer, keyboard or touch).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">browser</span> <span class="jser-tag">DOM</span></p>

사용자의 입력 상태를 트래킹하는 라이브러리.
현재 입력 상태가 mouse, keyboard, touch 인지 판정한다.


----

## Release v1.4.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.4.0](https://github.com/microsoft/playwright/releases/tag/v1.4.0 "Release v1.4.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

playwright 1.4.0 릴리스.
playwright-cli 정식 릴리스, Chromium 86 / Firefox 80 / WebKit 14 으로 각각 갱신.
`elementHandle.waitForElementState()`와 `elementHandle.waitForSelector()`가 추가됐다.


----
<h1 class="site-genre">아티클</h1>

----

## AVIF has landed - JakeArchibald.com
[jakearchibald.com/2020/avif-has-landed/](https://jakearchibald.com/2020/avif-has-landed/ "AVIF has landed - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Image</span> <span class="jser-tag">article</span></p>

AV1 video에서 유래한 이미지 포맷인 AVIF 소개.
jpeg, WebP, AVIF의 크기와 화질 비교.
AVIF의 인코딩과 디코딩 시간, 프로그래시브하게 출력할 수 없는 특징 등이 소개 돼 있다.

- [How to Use AVIF: The New Next-Gen Image Compression Format — Lightspeed](https://reachlightspeed.com/blog/using-the-new-high-performance-avif-image-format-on-the-web-today/ "How to Use AVIF: The New Next-Gen Image Compression Format — Lightspeed")

----

## DevTools architecture refresh: Migrating to JavaScript modules  |  Web
[developers.google.com/web/updates/2020/09/migrating-to-js-modules](https://developers.google.com/web/updates/2020/09/migrating-to-js-modules "DevTools architecture refresh: Migrating to JavaScript modules  |  Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">refacoring</span></p>

Chrome Dev Tools의 기반 코드를 독자 모듈 시스템에서 ES Modules로 이전한 배경과 과정.
표준 ES Modules의 이점, 이전 전략, export / import 단계적 적용.
또, 기술적인 부채로 인해서 초기 예상한 몇 주 보다 시간이 더 많이 소요 된 점이 소개돼 있다. 


----

## Leading-Trim: The Future of Digital Typesetting | by Ethan Wang | Microsoft Design | Aug, 2020 | Medium
[medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202](https://medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202 "Leading-Trim: The Future of Digital Typesetting | by Ethan Wang | Microsoft Design | Aug, 2020 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS `leading-trim` 속성 소개.


----

## A Practical Guide to the Web Cryptography API - DEV Community 👩‍💻👨‍💻
[dev.to/voraciousdev/a-practical-guide-to-the-web-cryptography-api-4o8n](https://dev.to/voraciousdev/a-practical-guide-to-the-web-cryptography-api-4o8n "A Practical Guide to the Web Cryptography API - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Web Cryptography API의 기본적인 사용 방법 소개.
Encryption, Decryption, 전송과 저장에 대해 다루고 있다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## type-challenges/type-challenges: Collection of TypeScript type challenges with online judge
[github.com/type-challenges/type-challenges](https://github.com/type-challenges/type-challenges "type-challenges/type-challenges: Collection of TypeScript type challenges with online judge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tutorial</span></p>

TypeScript의 타입 정의 문제에 도전할 수 있는 문제 모음.


----

## microsoft/FluidFramework: Library for building distributed, real-time collaborative web applications
[github.com/microsoft/FluidFramework](https://github.com/microsoft/FluidFramework "microsoft/FluidFramework: Library for building distributed, real-time collaborative web applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

분산형 실시간 협업을 위한 웹 애플리케이션 프레임워크.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## brahmosjs/brahmos: Super charged JavaScript library with modern React API and native templates.
[github.com/brahmosjs/brahmos](https://github.com/brahmosjs/brahmos "brahmosjs/brahmos: Super charged JavaScript library with modern React API and native templates.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">jsx</span> <span class="jser-tag">library</span> <span class="jser-tag">babel</span></p>

React와 같은 API와 JSX로 코드를 작성할 수 있는 UI 라이브러리.
Babel plugin으로 JSX를 Tagged Template Literal로 변환하고 lit-html와 같은 형태로 렌더링한다.のような形でレンダリングする


----

## cookie-universal/packages/cookie-universal at master · microcipcip/cookie-universal
[github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal](https://github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal "cookie-universal/packages/cookie-universal at master · microcipcip/cookie-universal")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

브라우저와 Node.js에서 동작하는 Cookie 조작 라이브러리.


----

## microsoft/playwright-cli: CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots.
[github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli "microsoft/playwright-cli: CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">browser</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

Playwright의 CLI 도구.
조작을 기록하고 재생하는 코드 생성, 요소의 Inspect, 스크린샷, PDF 생성 등의 기능 제공.


----

## ngneat/edit-in-place: A flexible and unopinionated edit in place library for Angular applications
[github.com/ngneat/edit-in-place](https://github.com/ngneat/edit-in-place "ngneat/edit-in-place: A flexible and unopinionated edit in place library for Angular applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Angular</span></p>

클릭하면 즉시 편집 모드로 전환되는 즉, edit in place 기능을 제공하는 Angular 용 라이브러리.


----

## sabljakovich/mongoose-execution-time: Mongoose plugin for measuring and logging query execution time
[github.com/sabljakovich/mongoose-execution-time](https://github.com/sabljakovich/mongoose-execution-time "sabljakovich/mongoose-execution-time: Mongoose plugin for measuring and logging query execution time")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MongoDB</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

mongoose에서 질의(query) 실행 시간을 로그 출력하는 라이브러리.


----
<h1 class="site-genre">도서</h1>

----

## JavaScript for Data Science
[js4ds.org/](https://js4ds.org/ "JavaScript for Data Science")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

데이터 과학자를 대상으로 한 JavaScript 입문서.


----
