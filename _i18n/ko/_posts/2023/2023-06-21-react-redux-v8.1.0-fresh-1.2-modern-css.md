---
title: "2023-06-21: React-Redux v8.1.0, Fresh 1.2, Modern CSS"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-06-20T22:57:46.724Z
category: JSer
tags:
- React
- node.js
- WebAssembly
- webservice
- TypeScript

---

JSer.info #648 - React-Redux v8.1.0 출시되었습니다.
개발모드에는 `useSelector`가 같은 입력에 같은 결과 반환하는가 체크하는 기능이 추가되었습니다.
selector를 같은 입력 2번 호출, 다른 참조라면 경고 보이는 구조입니다.
[React v18.0](https://react.dev/blog/2022/03/29/react-v18#new-strict-mode-behaviors)에 추가된 Strict mode와 닮은 동작입니다.

- [Release v8.1.0 · reduxjs/react-redux](https://github.com/reduxjs/react-redux/releases/tag/v8.1.0)

---

Deno 대상 웹 프레임워크 Fresh 1.2가 출시되었습니다.

- [Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more](https://deno.com/blog/fresh-1.2)

주 관리자는 Preact의 [Marvin Hagemeister](https://github.com/marvinhagemeister)이며 풀타임으로 관리합니다.
Sigals를 hydrate할 수 있도록, `npm:` 식별자 대응, HEAD 핸들러 추가가 있습니다.
또한, `islands/` 서브 디렉토리 지원, 플러그인이 비동기처리 대응합니다.

---

[Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions](https://moderncss.dev/modern-css-for-dynamic-component-based-architecture/)에서는, 모던한 CSS를 사용한 컴포넌트 베이스 아키텍처에 대해 소개하고 있습니다.

`@layer`사용한 Layout, `:has()`이나 Custom Properties 사용한 Variants 구현, 
`@container style()` 사용한 스타일 조건분기, Container Query와 Media Query에 의한 브레이크 포인트로 디바이스 크기 구분할 수 있도록 합니다.


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 3.31.0 - 2023.06.12 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.31.0](https://github.com/zloirock/core-js/releases/tag/v3.31.0 "Release 3.31.0 - 2023.06.12 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.31.0 출시.
Proposal Stage 변경 대응.
Array Grouping는 Stage 2로 승격, 정적 메소드 `Object.groupBy` 추가.
`Promise.withResolvers` 추가


----

## Turborepo 1.10 – Turbo
[turbo.build/blog/turbo-1-10-0](https://turbo.build/blog/turbo-1-10-0 "Turborepo 1.10 – Turbo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepo 1.10 출시.
Plop 사용한 `turbo gen` 추가, `.env` 지원, `--env-mode` Stable 변경

- [Consistency Made Simple : PLOP](https://plopjs.com/ "Consistency Made Simple : PLOP")

----

## Release v8.1.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v8.1.0](https://github.com/reduxjs/react-redux/releases/tag/v8.1.0 "Release v8.1.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.1.0 출시.
개발모드에 `useSelector`가 같은 입력 같은 결과 반환하는가 체크하는 구조가 추가되었다.
selector를 같은 입력 2번 호출, 다른 참조라면 경고 보이는 구조


----

## Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more
[deno.com/blog/fresh-1.2](https://deno.com/blog/fresh-1.2 "Fresh 1.2 – welcoming a full-time maintainer, sharing state between islands, limited npm support, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">React</span></p>

Deno대상 Web Framework Fresh 1.2 출시.
주 관리자는 Preact의 Marvin Hagemeister으로 교대.
Sigals를 hydrate할 수 있도록, `npm:` 식별자 대응, HEAD 핸들러 추가.
`islands/` 서브 디렉토리 지원, 플러그인이 비동기처리 대응


----

## Release v10.0.0 · nestjs/nest
[github.com/nestjs/nest/releases/tag/v10.0.0](https://github.com/nestjs/nest/releases/tag/v10.0.0 "Release v10.0.0 · nestjs/nest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

NestJS v10.0.0 출시.
Node.js 12, 14 지원 종료, `@nestjs/common`에서 `CacheModule` 삭제

- [Migration guide - FAQ | NestJS - A progressive Node.js framework](https://docs.nestjs.com/migration-guide "Migration guide - FAQ | NestJS - A progressive Node.js framework")

----

## Release v5.0.0 ❤️ · gvergnaud/ts-pattern
[github.com/gvergnaud/ts-pattern/releases/tag/v5.0.0](https://github.com/gvergnaud/ts-pattern/releases/tag/v5.0.0 "Release v5.0.0 ❤️ · gvergnaud/ts-pattern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

TypeScript 대상 패턴 매칭 라이브러리 ts-pattern 5.0.0 출시.
`.with` 동작 변경, method chain 지원


----

## Tuesday June 20 2023 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/june-2023-security-releases](https://nodejs.org/en/blog/vulnerability/june-2023-security-releases "Tuesday June 20 2023 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.js 보안 업데이트, 16.x/18.x/20.x가 각각 공개됨.

- Node.js v16.20.1 (LTS)
- Node.js v18.16.1 (LTS)
- Node.js v20.3.1 (Current)


----
<h1 class="site-genre">읽을거리</h1>

----

## The Cloud is dead, long live the Cloud! Announcing Wasmer Edge
[wasmer.io/posts/announcing-wasmer-edge](https://wasmer.io/posts/announcing-wasmer-edge "The Cloud is dead, long live the Cloud! Announcing Wasmer Edge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span> <span class="jser-tag">article</span></p>

Wasmer Edge 출시.
WebAssembly 애플리케이션을 Wasmtime으로 움직이는 플랫폼.
Shared nothing 아키텍처로 분산 모노리스 접근.


----

## Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions
[moderncss.dev/modern-css-for-dynamic-component-based-architecture/](https://moderncss.dev/modern-css-for-dynamic-component-based-architecture/ "Modern CSS For Dynamic Component-Based Architecture | Modern CSS Solutions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

모던 CSS 사용한 컴포넌트 기반 아키텍처에 대하여.
`@layer` 사용한 Layout, `:has()`이나 Custom Properties를 사용한 Variants.
`@container style()` 사용한 스타일 조건분기, Container Query와 Media Query로 브레이크 포인트해서 디바이스 크기 구분


----

## TypeScript 5.2&#039;s New Keyword: &#039;using&#039; | Total TypeScript
[www.totaltypescript.com/typescript-5-2-new-keyword-using](https://www.totaltypescript.com/typescript-5-2-new-keyword-using "TypeScript 5.2&#039;s New Keyword: &#039;using&#039; | Total TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

TypeScript 5.2에서 구현 예정인 ECMAScript Proposal Stage 3 `using`에 대해.
리소스 처리 패턴을 `using` 구문으로 지원

- [tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management](https://github.com/tc39/proposal-explicit-resource-management "tc39/proposal-explicit-resource-management: ECMAScript Explicit Resource Management")
- [ECMAScript Explicit Resource Management &amp; \`using\` Declarations · Issue #52955 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/52955 "ECMAScript Explicit Resource Management &amp;amp; \&#x60;using\&#x60; Declarations · Issue #52955 · microsoft/TypeScript")

----

## Introducing HTTP/3 Prioritization
[blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/](https://blog.cloudflare.com/better-http-3-prioritization-for-a-faster-web/ "Introducing HTTP/3 Prioritization")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP3</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">cloudflare</span></p>

HTTP/3 Extensible Priorities 지원함에 따라, Web 페이지 읽기가 어느정도 개선되는가에 대하여


----

## Web Apps on macOS Sonoma 14 Beta
[blog.tomayac.com/2023/06/07/web-apps-on-macos-sonoma-14-beta/](https://blog.tomayac.com/2023/06/07/web-apps-on-macos-sonoma-14-beta/ "Web Apps on macOS Sonoma 14 Beta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">macOS</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

macOS Sonoma에서 설치 가능한 웹 애플리케이션에 대하여


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Fermyon • Experience the next wave of cloud computing. | Fermyon • Experience the next wave of cloud computing.
[www.fermyon.com/](https://www.fermyon.com/ "Fermyon • Experience the next wave of cloud computing. | Fermyon • Experience the next wave of cloud computing.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span></p>

Spin 툴킷으로 작성한 WebAssembly 애플리케이션 디플로이, 실행 가능한 서버레스플랫폼

- [The Next Generation of Serverless is Happening | Fermyon • Experience the next wave of cloud computing.](https://www.fermyon.com/blog/next-generation-of-serverless-is-happening "The Next Generation of Serverless is Happening | Fermyon • Experience the next wave of cloud computing.")

----
