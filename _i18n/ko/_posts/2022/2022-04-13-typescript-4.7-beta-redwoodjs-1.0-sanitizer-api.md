---
title: "2022-04-13: TypeScript 4.7 Beta, RedwoodJS 1.0, Sanitizer API"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-04-12T22:59:47.573Z
category: JSer
tags:
- Tools
- TypeScript
- React
- testing
- book

---

JSer.info #587 - TypeScript 4.7 Beta가 릴리스 됐다.

- [Announcing TypeScript 4.7 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/)

TypeScript 4.5 Beta에 도입되어 Nightly에서 테스트 된 Node.js의 ECMAScript Module 지원이 다시 활성화 됐다.
이와 관련하여 `package.json`의 `exports` 필드, `"module": "nodenext"`, `.mts` / `cts` 확장자도 함께 지원한다.
또, Node.js에서는 파일이 모듈인지 여부는 `package.json`의 `module` 필드 등에 의해 암묵적으로 달라진다.
때문에, 파일이 모듈 판정 방법을 제어할 수 있는 `moduleDetection` 옵션을 추가하여 강제(`force`)로 모듈로 인식시킬 수 있도록 하는 방법도 제공한다.

- [Add moduleDetection compiler flag to allow for changing how modules are parsed by weswigham · Pull Request #47495 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/47495)

타입 추론 개선으로는 Computed 속성에 대한 조작 흐름 해석 개선, 객체 내의 함수 타입 추론 개선이 이뤄졌다.

Generics 타입을 지정하여 별칭(alias)을 정의할 수 있는 Instantiation Expressions을 지원한다.

```ts
const ErrorMap = Map<string, Error>;
```

- [Add moduleDetection compiler flag to allow for changing how modules are parsed by weswigham · Pull Request #47495 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/47495)

`infer`에 대한 `extends` 시의 추론 조건의 추가를 지원, 타입이 공변(`in`, covariant) / 반변(`out`, contravariant) / 불변(`in out`, invariant) 인지 지정할 수 있는 애너테이션이 추가 됐다.

- [Optional variance annotations by ahejlsberg · Pull Request #48240 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/pull/48240)

모듈 해결자 탐색 방법을 사용자 정의할 수 있는 `moduleSuffixes` 옵션 추가, `import type`과 Reference Comment로 `resolution-mode`를 지정할 수 있도록 개선됐다.

----

[Making of: The Sanitizer API (Nullcon 2022) - Google 슬라이드](https://docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM_ASFHH8Z5fMyfeoSbSH-k/view#slide=id.g82761e80df_0_1948)에서는 [HTML Sanitizer API](https://wicg.github.io/sanitizer-api/)라고 하는 책정 및 구현 중인 웹 표준을 소개하고 있다.

신뢰할 수 없는 HTML 문자열을 주입할 때에, 그 HTML 문자열을 정제(sanitize)하여 XSS를 방지하기 위한 API.
최초에는, 단순히 정제된 HTML 문자열을 반환하는 API로 진행됐으나, HTML의 파싱 모드 차이를 이용해 우회(bypass)하는 방법이 발견됐다(문자열 플래그먼트에 대한 정제는 안전하게 할 수 없다는 사실).

때문에, `innerHTML`와 비슷한 `setHTML`이라는 새로운 API가 책정 됐으며, 이 API에 HTML 문자열과 sanitizer 객체를 함께 전달하는 방식으로 변경된 일련의 과정이 정리돼 있다.

- [Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api](https://github.com/WICG/sanitizer-api/issues/42)
- [1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc](https://bugzilla.mozilla.org/show_bug.cgi?id=1669945)


----

<h1 class="site-genre">헤드라인</h1>

----

## Astro 1.0 Beta Release | Astro
[astro.build/blog/astro-1-beta-release/](https://astro.build/blog/astro-1-beta-release/ "Astro 1.0 Beta Release | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 1.0 beta 릴리스.
2022년 6월 8일에 정식 릴리스될 예정이다.


----

## Announcing Rome Formatter
[rome.tools/blog/2022/04/05/rome-formatter-release](https://rome.tools/blog/2022/04/05/rome-formatter-release "Announcing Rome Formatter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rust로 다시 작성한 Rome의 Formatter가 릴리스 됐다.
Prettier 동작을 기반으로 하고 있으며 opt-in으로 구문 에러에 대한 포메팅 기능도 지원한다.


----

## Release v8.0.0 · cucumber/cucumber-js
[github.com/cucumber/cucumber-js/releases/tag/v8.0.0](https://github.com/cucumber/cucumber-js/releases/tag/v8.0.0 "Release v8.0.0 · cucumber/cucumber-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Cucumber.js 8.0.0 릴리스.


----

## Announcing RedwoodJS 1.0 and $1M Funding
[tom.preston-werner.com/2022/04/04/redwood-v1-and-funding.html](https://tom.preston-werner.com/2022/04/04/redwood-v1-and-funding.html "Announcing RedwoodJS 1.0 and $1M Funding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">React</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">prisma</span> <span class="jser-tag">jest</span></p>

React / GraphQL / Prisma / Jest / Storybook를 조합한 애플리케이션 프레임워크 RedwoodJS 1.0 릴리스.

- [Redwood 1.0.0-rc.final is Available 🚀 - Announcements / Releases and Upgrade Guides - RedwoodJS Community](https://community.redwoodjs.com/t/redwood-1-0-0-rc-final-is-available/2902 "Redwood 1.0.0-rc.final is Available 🚀 - Announcements / Releases and Upgrade Guides - RedwoodJS Community")

----

## Announcing TypeScript 4.7 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-7-beta/ "Announcing TypeScript 4.7 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>


4.7 beta가  릴리스 됐다.

 * Node.js의 ECMAScript Module 지원을 다시 활성화
 * `moduleDetection` 옵션 추가
 * Compuated 프로퍼티에 대한 조작 흐름 분석 개선
 * 객체 내의 함수(메서드) 타입 추론 개선 
 * Generics의 타입을 지정하여 일종의 alias를 선언할 수 있는 Instantiation Expressions 지원.
 * `infer`에 대한 `extends` 시의 추론 조건 추가를 지원. 
 * 타입이 공변(`in`, covariant) / 반변(`out`, contravariant) / 불변(`in out`, invariant) 인지를 지정할 수 있는 애너테이션 추가. 
 * 모듈 해결자 탐색 방법을 사용자 정의할 수 있는 `moduleSuffixes` 옵션 추가.
 * `import type`과 Reference Comment로 `resolution-mode`를 지정할 수 있도록 개선.


----

## Release Notes for Safari Technology Preview 143 | WebKit
[webkit.org/blog/12563/release-notes-for-safari-technology-preview-143/](https://webkit.org/blog/12563/release-notes-for-safari-technology-preview-143/ "Release Notes for Safari Technology Preview 143 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 143 릴리스.
CSS Container Queries, CSS Cascade Layers, Web Animation API 각각 개선.
Permissions API를 기본 활성화, `inert` 속성을 기본 활성화.

- [HTMLElement.inert - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/HTMLElement/inert "HTMLElement.inert - Web API | MDN")

----

## Turborepo 1.2 | Turborepo
[turborepo.org/blog/turbo-1-2-0](https://turborepo.org/blog/turbo-1-2-0 "Turborepo 1.2 | Turborepo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepot 1.2 릴리스.
대상을 필터링 할 수 있는 `--filter` 플래그 추가, 실행 작업에 대한 정보 가시성(human readable)을 높일 수 있는 `--dry-run` 플래그 추가.
성능 개선, 캐시 적합성을 HMAC으로 검증할 수 있는 `signature` 옵션이 추가됐다.


----

## Release v8.0.0-rc.0 · reduxjs/react-redux
[github.com/reduxjs/react-redux/releases/tag/v8.0.0-rc.0](https://github.com/reduxjs/react-redux/releases/tag/v8.0.0-rc.0 "Release v8.0.0-rc.0 · reduxjs/react-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.0.0-rc.0 릴리스.
`@types/react-readux`에 존재했던 `DefaultRootState` 타입 정의를 삭제했다.


----

## goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript &amp; Node.js testing best practices (April 2022)
[github.com/goldbergyoni/javascript-testing-best-practices](https://github.com/goldbergyoni/javascript-testing-best-practices "goldbergyoni/javascript-testing-best-practices: 📗🌐 🚢 Comprehensive and exhaustive JavaScript &amp; Node.js testing best practices (April 2022)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">news</span></p>

자바스크립트 테스트에 대한 문서. 테스트 구조, 백엔드, 프런트엔드, CI 등 다양한 테스트 관련 주제를 다루고 있는 javascript-testing-best-practices가 업데이트 됐다.


----

## Release 2.0.0-beta.0 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-beta.0](https://github.com/vercel/swr/releases/tag/2.0.0-beta.0 "Release 2.0.0-beta.0 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-beta.0 릴리스.
수동으로 직접 수행해야하는 요청을 다룰 수 있는 `useSWRMutation` 추가(dedicated API for remote mutations).
비호환 변경 사항으로 Fetcher에서 여러개의 인수를 전개하지 않도록 변경됐다.


----
<h1 class="site-genre">아티클</h1>

----

## 04.01.2022 - TypeScript/How the compiler compiles
[www.huy.rocks/everyday/04-01-2022-typescript-how-the-compiler-compiles](https://www.huy.rocks/everyday/04-01-2022-typescript-how-the-compiler-compiles "04.01.2022 - TypeScript/How the compiler compiles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript Compiler가 어떻게 TypeScript 코드를 컴파일하고, 에러를 알려주는지 설명하는 글.


----

## ECMAScript proposal “Change Array by copy”: four new non-destructive Array methods
[2ality.com/2022/04/change-array-by-copy.html](https://2ality.com/2022/04/change-array-by-copy.html "ECMAScript proposal “Change Array by copy”: four new non-destructive Array methods")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

현재 ECMAScript Proposal Stage 3인 Change Array by copy를 다루고 있다.
Array 메서드에는 파괴적(destructive) 메서드가 포함돼 있는데 이에 상응하는 비파괴적(non-destructive) 메서드를 추가하는 제안이다(ex: `arr.sort()` => `arr.toSorted()`).


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Making of: The Sanitizer API (Nullcon 2022) - Google 슬라이드
[docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM\_ASFHH8Z5fMyfeoSbSH-k/view#slide&#x3D;id.g82761e80df\_0\_1948](https://docs.google.com/presentation/d/1eLmIZkY7auD8xT-Q6AzBKM_ASFHH8Z5fMyfeoSbSH-k/view#slide=id.g82761e80df_0_1948 "Making of: The Sanitizer API (Nullcon 2022) - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">API</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

Sanitizer API를 주제로 한 슬라이드 자료.
DOM XSS를 막는 Sanitizer API가 단순히 새니타이저한 HTML 문자열을 반환하는 API가 아닌 이유를 설명하며, `setHTML` API도 함께 다룬다.

- [Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api](https://github.com/WICG/sanitizer-api/issues/42 "Sanitizer API creating mock context-element can cause XSS when used in different context · Issue #42 · WICG/sanitizer-api")
- [1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc](https://bugzilla.mozilla.org/show_bug.cgi?id=1669945 "1669945 - Sanitizer bypass if the sanitized markup is assigned to srcdoc")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## antfu/vue-starport: 🛰 Shared component across routes with animations
[github.com/antfu/vue-starport](https://github.com/antfu/vue-starport "antfu/vue-starport: 🛰 Shared component across routes with animations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

페이지 전환 효과를 구현하는 Vue 컴포넌트.
공유 컴포넌트를 Root로 끌어올려서 페이지 간 동일한 컴포넌트 인스턴스를 유지할 수 있도록 설계돼 있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## AgnosticUI/agnosticui: AgnosticUI is a set of UI primitives that start their lives in clean HTML and CSS. These standards compliant components are then copied to our framework implementations in: React, Vue 3, Angular, and Svelte.
[github.com/agnosticui/agnosticui](https://github.com/agnosticui/agnosticui "AgnosticUI/agnosticui: AgnosticUI is a set of UI primitives that start their lives in clean HTML and CSS. These standards compliant components are then copied to our framework implementations in: React, Vue 3, Angular, and Svelte.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

UI 컴포넌트 프레임워크.
순수 자바스크립트로도 사용할 수 있으며 React / Angular / Svelte / Vue 등 각 프레임워크 용 패키지도 공개돼 있다.


----
<h1 class="site-genre">도서</h1>

----

## 프로를 지망하는 사람을 위한 TypeScript 입문. 안전한 코드를 작성하는 방법 부터 고급 타입 사용 방법까지 : 서적 안내 | 기술평론사(일본어)
[gihyo.jp/book/2022/978-4-297-12747-3](https://gihyo.jp/book/2022/978-4-297-12747-3 "프로를 지망하는 사람을 위한 TypeScript 입문. 안전한 코드를 작성하는 방법 부터 고급 타입 사용 방법까지 : 서적 안내 | 기술평론사")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2022년 4월 22일에 출간 예정인 타입스크립트 입문서


----
