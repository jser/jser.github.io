---
title: "2025-07-04: ECMAScript 2025, Rspack 1.4, Deno 2.4, Bundle Size 개선"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-07-04T02:54:31.532Z
category: JSer
tags:
 - React
 - css
 - rspack
 - Chrome
 - ECMAScript
---

JSer.info #740 - ECMAScript 2025 정식 출시했습니다.

- [Ecma International approves new standards - Ecma International](https://ecma-international.org/news/ecma-international-approves-new-standards-11/)
- [Release ES2025 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2025)

ECMAScript 2025가 Ecma International의 General Assembly에서 승인되어, 정식 출시했습니다.
ECMAScript 2025에서는, 다음과 같은 사양이 추가됩니다.

- Iterator helpers: iterator 대상 map, filter, reduce 메서드
- Set.prototype 메서드: Set 대상 집합 연산 메서드
- JSON modules import: JSON 모듈을 import 하는 기능과 import attributes 사양
- RegExp.escape 메서드: 정규표현 에스케이프 하기 위한 메서드
- 정규표현 첨자 플래그: 정규표현에서 인라인으로 modifier flags를 유효/무효하는 구문 추가
- Promise.try 메서드: Promise 반환할 지 어떨지 모를 함수를 호출하고, 결과를 늘 Promise으로 하는 메서드
- Float16Array: Float16 다루는 TypedArray 자료형

---

Rspack 1.4 출시했습니다.

- [Announcing Rspack 1.4 - Rspack](https://rspack.rs/blog/announcing-1-4)

Wasm 이용 가능한 브라우저 환경에서 실행 지원이 추가되어, bundle size 개선도 있습니다.
기본적으로 Incremental build가 유효화되어 있고, 실험적으로 CssChunkingPlugin 추가, MultiCompiler에서 lazy compilation 지원 기능 강화가 포함됩니다.
또한, Perfetto 기반 성능 분석 도구도 추가되었습니다.

---

Deno 2.4가 출시되어, `deno bundle` 명령어가 부활합니다.

- [Deno 2.4: deno bundle is back | Deno](https://deno.com/blog/v2.4)

이전에 삭제된 `deno bundle` 명령어가 부활, 텍스트 `byte` import 기능과 OpenTelemetry 안정화가 있습니다.
`--preload` 플래그 추가, `deno update` 명령어 추가, package.json의 conditional exports 지원, 개발 체험 향상을 위한 많은 기능 추가가 있습니다.

---

{% include inline-support.html %}

---

<h1 class="site-genre">헤드라인</h1>

---

## Announcing Rspack 1.4 - Rspack

[rspack.rs/blog/announcing-1-4](https://rspack.rs/blog/announcing-1-4 "Announcing Rspack 1.4 - Rspack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">ReleaseNote</span></p>

Rspack 1.4 출시.
Wasm 이용한 브라우저 환경에서 실행 지원, bundle size 개선.
기본적으로 Incremental build 유효화.
실험적인 CssChunkingPlugin 추가, MultiCompiler에서 lazy compilation 지원, `useInputFileSystem` 옵션 지원.
Perfetto 기반 성능 분석 도구, Zod v4으로 업데이트

---

## Chrome 139 beta  |  Blog  |  Chrome for Developers

[developer.chrome.com/blog/chrome-139-beta?hl&#x3D;en](https://developer.chrome.com/blog/chrome-139-beta?hl=en "Chrome 139 beta  |  Blog  |  Chrome for Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 139 beta 출시.
CSS에서, `var()`/`attr()` 단축 평가 지원, `caret-animation`/`corner-shape`/CSS Custom Functions 지원.
WHATWG 사양과 맞춰서 `+json`의 JSON MIME type 지원.
Origin trials에서 Prompt API, WebGPU Compatibility mode 추가.
macOS 11 지원 종료, ISO-2022-JP 자동 검출 삭제

- [Intent to Ship: Spec-compliant JSON MIME type detection](https://groups.google.com/a/chromium.org/g/blink-dev/c/-lZFLXH7_Y8/m/ZzgLXc91AQAJ "Intent to Ship: Spec-compliant JSON MIME type detection")

---

## Ecma International approves new standards - Ecma International

[ecma-international.org/news/ecma-international-approves-new-standards-11/](https://ecma-international.org/news/ecma-international-approves-new-standards-11/ "Ecma International approves new standards - Ecma International")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

ECMAScript 2025가 Ecma의 GA에서 승인되어 정식 출시.

- [Release ES2025 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2025 "Release ES2025 · tc39/ecma262")

---

## Release 0.14.0 | StyleX

[stylexjs.com/blog/v0.14.0](https://stylexjs.com/blog/v0.14.0 "Release 0.14.0 | StyleX")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">library</span></p>

StyleX v0.14.0 출시.
`viewTransitionClass` API 추가, lint에 `validImports` 옵션 추가.
파괴적 변경으로 스타일을 머지할 때 전략 설정하는 `styleResolution` 옵션 기본값을 `application-order`에서 `property-specificity` 으로 변경

---

## Electron 37.0.0 | Electron

[www.electronjs.org/blog/electron-37-0](https://www.electronjs.org/blog/electron-37-0 "Electron 37.0.0 | Electron")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 37.0 출시.
Chromium 138.0.7204.35/Node 22.16.0/V8 13.8 업데이트.
`window.open`에서 `innerWidth`와 `innerHeight` 옵션 지원, Node.js 의`--experimental-network-inspection` 지원.
unhandled rejection 동작 변경, WebUSB/WebSerial API blocklist 지원.

---

## Deno 2.4: deno bundle is back | Deno

[deno.com/blog/v2.4](https://deno.com/blog/v2.4 "Deno 2.4: deno bundle is back | Deno")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.4 출시.
`deno bundle` 명령어 부활/텍스트 `byte` import 기능/OpenTelemetry 안정화 
`--preload` 플래그 추가/`deno update` 명령어 추가/`DENO_COMPAT` 환경 변수 추가, package.json의 conditional exports 지원

---

## Release v3.0.0 · recharts/recharts

[github.com/recharts/recharts/releases/tag/v3.0.0](https://github.com/recharts/recharts/releases/tag/v3.0.0 "Release v3.0.0 · recharts/recharts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">graphic</span> <span class="jser-tag">library</span></p>

Recharts 3 출시.
Custom components 지원, 기본적으로 `accessibilityLayera11y` 유효로 변경

- [3.0 migration guide · recharts/recharts Wiki](https://github.com/recharts/recharts/wiki/3.0-migration-guide#breaking-code-changes "3.0 migration guide · recharts/recharts Wiki")

---

## dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions

[github.com/dahlia/logtape?tab&#x3D;readme-ov-file](https://github.com/dahlia/logtape?tab=readme-ov-file "dahlia/logtape: Simple logging library with zero dependencies for Deno, Node.js, Bun, browsers, and edge functions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

로그 라이브러리.
라이브러리와 애플리케이션 이용을 상정해서, Node.js/Deno/Browser으로 동작, 구조화 로그 지원.
또한, pino나 winston 로그 라이브러리와 Integration 하는 Adapter 제공

---

<h1 class="site-genre">읽을거리</h1>

---

## CSS conditionals with the new if() function  |  Blog  |  Chrome for Developers

[developer.chrome.com/blog/if-article?hl&#x3D;en](https://developer.chrome.com/blog/if-article?hl=en "CSS conditionals with the new if() function  |  Blog  |  Chrome for Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">article</span></p>

CSS에서 `if()` 함수에 대하여.
프로퍼티 값에 `if()`와 `style()`/`media()`/`suports()` 사용해 조건 분기를 작성하는 방법에 대하여

---

## How We Reduced CKEditor’s Bundle Size by 40% | CKEditor

[ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/](https://ckeditor.com/blog/how-we-reduced-ckeditor-bundle-size/ "How We Reduced CKEditor’s Bundle Size by 40% | CKEditor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">article</span></p>

CKEditor 5의 bundle size 최적화 관련하여.
버전 어긋남 대책으로 re-export 으로 패키지를 모은 패키지를 공개하고 있지만 tree-shaking가 먹지 않아 bundle 크기 문제가 일어남.
`/* #__PURE__ */` 주석을 활용해서, ES2022으로 target 변경, `sideEffects` 플러그 설정을 하는 tree shaking 문제 해결한 이야기.
또한, Sonda 사용해 bundle 분석

- [Sonda](https://sonda.dev/ "Sonda")

---

## \`useOptimistic\` to Make Your App Feel Instant | Epic React by Kent C. Dodds

[www.epicreact.dev/use-optimistic-to-make-your-app-feel-instant-zvyuv](https://www.epicreact.dev/use-optimistic-to-make-your-app-feel-instant-zvyuv "`useOptimistic` to Make Your App Feel Instant | Epic React by Kent C. Dodds")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React의 `useOptimistic` hooks 사용 방법이나 `setState`와 차이에 대하여

---

<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

---

## photostructure/tz-lookup: JavaScript Library for Timezone Lookup by Location

[github.com/photostructure/tz-lookup](https://github.com/photostructure/tz-lookup "photostructure/tz-lookup: JavaScript Library for Timezone Lookup by Location")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

위도 경도에서 지명을 검색하는 라이브러리

---
