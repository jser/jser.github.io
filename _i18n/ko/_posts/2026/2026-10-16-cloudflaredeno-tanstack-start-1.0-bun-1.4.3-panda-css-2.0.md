---
title: "2026-10-16: Cloudflare가 Deno 인수, TanStack Start 1.0, Bun 1.4.3, Panda CSS 2.0"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-10-16T00:46:17.876Z
category: JSer
tags:
- deno
- cloudflare
- TanStack
- React
- Solid
- Bun
- TypeScript
- css

---

JSer.info #781 - Cloudflare가 Deno 인수를 발표했다.

- [Deno is joining Cloudflare | Deno](https://deno.com/blog/cloudflare)
- [The state of Deno after the Cloudflare announcement · Issue #37030 · denoland/deno](https://github.com/denoland/deno/issues/37030)

Deno 런타임은 1년간 버그 수정・보안 업데이트 진행한 이후, Deno 팀에 의한 개발이 종료된다.
Deno Deploy은 6개월 후에 종료, JSR은 Cloudflare로 이행되어 계승된다.
앞으로는 Workers과 Durable Objects 플랫폼에 주력, `rusty_v8`은 지속해서 지원하며 `workerd`으로 통합 진행이 예정되었다.

---

TanStack Start 1.0 출시되었다.

- [TanStack Start 1.0 is Stable | TanStack Blog](https://tanstack.com/blog/tanstack-start-1-0)

TanStack Start은, TanStack Router를 기반으로 하는 React/Solid 대상 풀스택 프레임워크이다.
SSR와 스트리밍, 자료형 있는 서버 함수 `createServerFn`, 실행 환경 째로 처리를 전환하는 `createIsomorphicFn`를 제공한다.

---

Bun 1.4.3 출시되었다.

- [Bun v1.4.3 | Bun Blog](https://bun.com/blog/bun-v1.4.3)

TypeScript 자료형 체크하는 `bun check`가 추가되어, `bun run --check`/`bun test --check`/`bun build --check`에 대응한다.
또한, `--disallow-code-generation-from-strings`으로 문자열에서 생성 금지, `bun build --compile --bytecode-order`에 대응한다.

---

Panda CSS 2.0 출시되었다.

- [Panda CSS 2.0 | Panda CSS Blog - Panda CSS](https://panda-css.com/blog/panda-css-v2)

Panda CSS 2.0에는, ESM만 가능해 Node.js 22 이상이 필요가 되었으며, `hooks`가 `plugins`으로 마이그레이션된다.
또한, 컴파일러가 Rust와 Oxc으로 재작성되어, `panda lib`와 `designSystem`으로 디자인 시스템 배포에 대응한다.
그 외로는, `viewTransition()`/`firstThatWorks()`/`keyframes()`/`positionTry()`, `panda doctor`/`panda analyze`/`panda debug`가 추가되었다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Preact 11 – Preact
[preactjs.com/blog/preact-11/](https://preactjs.com/blog/preact-11/ "Preact 11 – Preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">React</span></p>

Preact 11.0.0 출시.
파괴적 변경으로, `.mjs`의 ESM 배포만 하게 되어 CommonJS/UMD 핸들러 삭제, `render()`은 세 번째 인수 삭제.
`Hydration 2.0`, `Object.is`으로 Hook 인수 비교, ref를 기본적으로 전송하도록 변경`forwardRef`를 필요하지 않게 함, `createPortal`를 core에 추가.

- [Upgrading from Preact 10.x – Preact Guide v11](https://preactjs.com/guide/v11/upgrade-guide/ "Upgrading from Preact 10.x – Preact Guide v11")

----

## Next.js 16.4 | Next.js
[nextjs.org/blog/next-16-4](https://nextjs.org/blog/next-16-4 "Next.js 16.4 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 16.4 출시.
`create-next-app`으로 Cache Componentsが가 기본 유효화, `ensureStatic`/`navigation()`/`prefetch()` 추가.
`next upgrade --agent`と`experimental.agentUpgrade`, `experimental.agentFeedback` 추가.
Turbopack 디스크 캐시 삭제, Lazy server HMR, Turbopack 공유 Runtime.
CSS Modules으로 production 빌드에는 짧은 클래스명 생성되도록 변경, React 19.3으로 업데이트.


----

## Panda CSS 2.0 | Panda CSS Blog - Panda CSS
[panda-css.com/blog/panda-css-v2](https://panda-css.com/blog/panda-css-v2 "Panda CSS 2.0 | Panda CSS Blog - Panda CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Panda CSS 2.0 출시.
ESM만 지원하게되었으며 Node.js 22 이상 필요, `hooks`를 `plugins`으로 이행.
`createStyleContext`를 `createSlotRecipeContext`/`createRecipeContext`으로 분할分割.
Rust와 Oxc로 컴파일러 재작성, `panda lib`와 `designSystem`으로 디자인 시스템 배포에 대응.
`viewTransition()`/`firstThatWorks()`/`keyframes()`/`positionTry()` 추가.
`panda doctor`/`panda analyze`/`panda debug`, ESLint 플러그인 정식 지원


----

## Node.js — Node.js 26.11.0 (Current)
[nodejs.org/en/blog/release/v26.11.0](https://nodejs.org/en/blog/release/v26.11.0 "Node.js — Node.js 26.11.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v26.11.0 출시.
`isLatin1`/`Buffer.stringLength()`, `http.isValidHeaderName()`/`http.isValidHeaderValue()` 추가.
`http2`の`connectionWindowSize`, `histogram.diff()`/`histogram.snapshot()`, `--process-timeout=N` 추가.
`process.ref()`/`process.unref()`가 Stable, npm 11.20.0으로 업데이트.


----

## Release 3.0.0 · qunitjs/qunit
[github.com/qunitjs/qunit/releases/tag/3.0.0](https://github.com/qunitjs/qunit/releases/tag/3.0.0 "Release 3.0.0 · qunitjs/qunit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">test</span></p>

QUnit 3.0.0 출시.
Node.js 16 이하/PhantomJS/AMD 대상 빌트인 export/`QUnit.load()` 삭제.
네이티브 ESM 배포, `before`/`after` 훅 module context, `QUnit.config.reporters.html` 추가.
기본적 테스트 타임아웃을 3초로 변경, HTML Reporter 디자인 업데이트.

- [QUnit 3.0 Upgrade Guide | QUnit](https://qunitjs.com/upgrade-guide-3.x/ "QUnit 3.0 Upgrade Guide | QUnit")

----

## Bun v1.4.3 | Bun Blog
[bun.com/blog/bun-v1.4.3](https://bun.com/blog/bun-v1.4.3 "Bun v1.4.3 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.4.3 출시.
TypeScript 자료형 체크를 하는 `bun check` 추가, `bun run --check`/`bun test --check`/`bun build --check` 대응.
`--disallow-code-generation-from-strings`으로 문자열에서 코드 생성 금지 대응, `bun build --compile --bytecode-order` 지원


----

## Deno is joining Cloudflare | Deno
[deno.com/blog/cloudflare](https://deno.com/blog/cloudflare "Deno is joining Cloudflare | Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

Cloudflare가 Deno 매수.
Deno 런타임은 1년간 버그 수정・보안 업데이트한 이후, Deno팀의 개발은 종료, Deno Deploy은 6개월 후에 종료, JSR은 Cloudflare으로 이행해서 계승.
앞으로는 Workers와 Durable Objects 플랫폼에 주력, `rusty_v8`은 계속해서 지원하며 `workerd`으로 통합 진행 예정.

- [Deno is joining Cloudflare | Cloudflare Blog](https://blog.cloudflare.com/deno-joins-cloudflare "Deno is joining Cloudflare | Cloudflare Blog")

----

## TanStack Start 1.0 is Stable | TanStack Blog
[tanstack.com/blog/tanstack-start-1-0](https://tanstack.com/blog/tanstack-start-1-0 "TanStack Start 1.0 is Stable | TanStack Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TanStack</span> <span class="jser-tag">React</span> <span class="jser-tag">Solid</span> <span class="jser-tag">ReleaseNote</span></p>

TanStack Start 1.0 출시.
TanStack Router를 기반하는 React/Solid 대상 풀스택 프레임워크.
SSR/스트리밍, 자료형 대상 서버 함수 `createServerFn`, 실행 환경 째로 처리 전환하는 `createIsomorphicFn` 제공한다.


----

## Release v5.3.0 · expressjs/express
[github.com/expressjs/express/releases/tag/v5.3.0](https://github.com/expressjs/express/releases/tag/v5.3.0 "Release v5.3.0 · expressjs/express")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">express</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Express 5.3.0 출시.
`Content-Disposition` 파일명 인용부를 생략하는 조건을 변경, `res.send()`으로 기존 `Content-Type` 파라메터를 보유하도록 변경.
`req.fresh`가 `QUERY` 메서드에 대응, 기본적으로 에러 핸들러가 `Error.cause`를 포함하는 에러 전체 로그 출력.


----

## Release v1.0.0 · QwikDev/partytown
[github.com/QwikDev/partytown/releases/tag/v1.0.0](https://github.com/QwikDev/partytown/releases/tag/v1.0.0 "Release v1.0.0 · QwikDev/partytown")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webworker</span> <span class="jser-tag">ReleaseNote</span></p>

Partytown v1.0.0 출시.
서드파티 스크립트를 Web Worker에서 실행하는 라이브러리.


----
<h1 class="site-genre">읽을거리</h1>

----

## Responsive iframes in Chrome 154  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/responsive-iframes?hl&#x3D;en](https://developer.chrome.com/blog/responsive-iframes?hl=en "Responsive iframes in Chrome 154  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">HTML</span> <span class="jser-tag">css</span></p>

Chrome 154에서 추가된 response한 `iframe` 해설 글.
`frame-sizing: content-height`로, 임베디드된 내용에 맞춰 크기를 정리 가능.
임베디드된 측에서는 `responsive-embedded-sizing` 메타 태그, `window.requestResize()`, Cross-Origin 대응에 대한 해설도 있음.


----

## Scrolling is All You Need: Building a Swipeable Sheet | React Aria
[react-aria.adobe.com/blog/sheet](https://react-aria.adobe.com/blog/sheet "Scrolling is All You Need: Building a Swipeable Sheet | React Aria")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">UI</span> <span class="jser-tag">animation</span> <span class="jser-tag">article</span></p>

React Aria 스와이프 조작으로 닫을 수 있는 Sheet 컴포넌트 구현에 대하여.
CSS Scroll Snap와 `view-timeline`를 사용해, JavaScript에서 터치 이벤트 처리없이 스와이프 조작과 연동한 애니메이션 실현함.
중간에 정지하는 스냅포인트, 시트 겹침, 소프트웨어 키보드 대응에 대해서도 설명됨.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## tester-army/e2e: Next generation e2e testing framework for web and mobile apps.
[github.com/tester-army/e2e](https://github.com/tester-army/e2e "tester-army/e2e: Next generation e2e testing framework for web and mobile apps.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">web</span> <span class="jser-tag">mobile</span> <span class="jser-tag">AI</span></p>

Web와 모바일 애플리케이션 대상 E2E 테스트 프레임워크.
자연언어로 작성된 순서를 에이전트가 실행, LocatorとAssertion으로 결과를 검증 가능.
Web은 Playwright 경유로 Chromium/Firefox/WebKit, 모바일은 iOS/Android에 대응.


----

## tarwin/tinyjsapp: Build native apps in JS. Backend, frontend. ~5Mb.
[github.com/tarwin/tinyjsapp](https://github.com/tarwin/tinyjsapp "tarwin/tinyjsapp: Build native apps in JS. Backend, frontend. ~5Mb.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">app</span> <span class="jser-tag">Tools</span> <span class="jser-tag">webview</span> <span class="jser-tag">macOS</span> <span class="jser-tag">windows</span> <span class="jser-tag">linux</span></p>

txiki.js와 OS 네이티브 WebView를 사용한 데스크탑 애플리케이션 작성하는 도구.
백엔드는 JavaScript로 작성, 프론트엔드는 HTML/CSS/JS를 OS의 WebView로 보여줌.
`tinyjs new`/`tinyjs dev`/`tinyjs build`의 CLI, 메뉴/알람/트레이/드래그앤드롭 네이티브 기능 제공.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## rauchg/gdp-ts
[github.com/rauchg/gdp-ts/tree/main](https://github.com/rauchg/gdp-ts/tree/main "rauchg/gdp-ts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">lint</span></p>

TypeScript 대상 Ghosts of Departed Proofs 구현 라이브러리.
`name()`으로 값으로 컴파일할 때 이름을 붙이고, `defineProof()`으로 인허가 체크 결과를 자료형으로 다루며, 개발 측에서 `_proof` 인수를 받아 인허가 체크만 자료형 체크함.


----
