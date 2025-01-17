---
title: "2025-01-16: WinterTC (TC55), Node.js에서 TypeScript 지원 배경, Angular 2025"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-01-16T13:42:36.358Z
category: JSer
tags:
- TypeScript
- nodejs
- React
- pnpm
- security

---

JSer.info #722 - Node.js/Deno/Cloudflare Workers 등에서 서버사이드 JavaScript 실행 환경 상호운영성에 대해 의논하는 WinterCG가, Ecma의 TC55([WinterTC](https://wintercg.org/))으로 표준화 작업이 되고 있다 발표되었습니다.

- [Collaborating across W3C and Ecma for web-interoperable server runtimes through WinterTC - Ecma International](https://ecma-international.org/news/collaborating-across-w3c-and-ecma-for-web-interoperable-server-runtimes-through-wintertc/)

ECMAScript이나 HTML 표준 사양에는 특허와 라이센스가 엮어있기에, 실제 API 표준을 만드는 것은 Ecma나 W3C 같은 표준화단체 프로세스를 따르는 것이 좋기도 합니다.
WinterCG은 본래 W3C 커뮤니케이션 그룹으로 시작했으며, W3C와 Ecma 어느 쪽에서 표준화를 진행할 지 의논해, 여러 멤버가 이미 Ecma에 참가하고 있으므로(TC39 ECMAScript 표준화에 관련되어 있으므로), Ecma의 TC55으로 표준화 진행합니다.

- [Dedicated standardization meeting 2024-08-29 · Issue #70 · wintercg/admin](https://github.com/wintercg/admin/issues/70)
- [Tracking issue: consider ECMA TC / W3C WG to publish standards · Issue #58 · wintercg/admin](https://github.com/wintercg/admin/issues/58)

---

[Node.js Type Stripping Explained](https://satanacchio.hashnode.dev/everything-you-need-to-know-about-nodejs-type-stripping)에서는, Node.js의 TypeScript 지원 접근인 Type Stripping에 대해 해설합니다.
왜 자료형을 제거한다는 접근을 하고 있는가, 코드 변환과 Source Map, 앞으로 TypeScript 지원 방향성 등이 언급되어 있습니다.

---

[Angular 2025 Strategy. For the past two and a half years… | by Minko Gechev | Jan, 2025 | Angular Blog](https://blog.angular.dev/angular-2025-strategy-9ca333dfc334)에서는, Angular의 2025년 전망에 대해 언급합니다.

Angular의 2024년 앙케이트 결과 분석, 2025년 이루고 싶은 점에 대해 다룹니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## ESLint v9.18.0 released - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2025/01/eslint-v9.18.0-released/](https://eslint.org/blog/2025/01/eslint-v9.18.0-released/ "ESLint v9.18.0 released - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">TypeScript</span></p>

ESLint v9.18.0 출시.
TypeScript에서 설정파일 작성하는 `eslint.config.ts` 지원


----

## Collaborating across W3C and Ecma for web-interoperable server runtimes through WinterTC - Ecma International
[ecma-international.org/news/collaborating-across-w3c-and-ecma-for-web-interoperable-server-runtimes-through-wintertc/](https://ecma-international.org/news/collaborating-across-w3c-and-ecma-for-web-interoperable-server-runtimes-through-wintertc/ "Collaborating across W3C and Ecma for web-interoperable server runtimes through WinterTC - Ecma International")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ecma</span> <span class="jser-tag">news</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">deno</span> <span class="jser-tag">cloudflare</span></p>

서버사이드 JavaScript API 상호운용성에 대해 의논하는 WinterCG는 Ecma의 TC55으로 표준화 진행하는 방침

- [WinterTC](https://wintercg.org/ "WinterTC")

----

## Release 3.40.0 - 2025.01.08 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.40.0](https://github.com/zloirock/core-js/releases/tag/v3.40.0 "Release 3.40.0 - 2025.01.08 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.40.0 출시.
Stage 3의 `Error.isError` 추가, 버그 수정


----

## Release v3.0.0 · Automattic/node-canvas
[github.com/Automattic/node-canvas/releases/tag/v3.0.0](https://github.com/Automattic/node-canvas/releases/tag/v3.0.0 "Release v3.0.0 · Automattic/node-canvas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

node-canvas 3.0.0 출시.
Node.js 16 지원 종료, N-API 이용하도록 하는 변경


----

## Release Version 26.0.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/26.0.0](https://github.com/jsdom/jsdom/releases/tag/26.0.0 "Release Version 26.0.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 26.0.0 출시.
node-canvas를 v3으로 업데이트, `AbortSignal.any()` 지원, `URL.parse()` 지원


----

## Release v136 · esm-dev/esm.sh
[github.com/esm-dev/esm.sh/releases/tag/v136](https://github.com/esm-dev/esm.sh/releases/tag/v136 "Release v136 · esm-dev/esm.sh")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">cdn</span> <span class="jser-tag">ReleaseNote</span></p>

esm.sh v136 출시.
jsr 지원, pkg.pr.new 지원.
빌드 성능 개선, `build` API/Deno CLI 스크립트 비권장으로


----

## 2024 JavaScript Rising Stars
[risingstars.js.org/2024/en](https://risingstars.js.org/2024/en "2024 JavaScript Rising Stars")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

GitHub 별 숫자 비교하는 JavaScript Rising Stars 2024 결과 공개


----

## January 15, 2025 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2025-01-15.html](https://react-spectrum.adobe.com/releases/2025-01-15.html "January 15, 2025 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria January 15, 2025 출시.
Autocomplete 컴포넌트 추가, Overlay 컴포넌트로 CSS Transitions 지원, `@react-aria/test-utils` 패키지 추가.
`usePress`으로 iOS 13 버그 대응 코드 삭제


----
<h1 class="site-genre">읽을거리</h1>

----

## pnpm 10.0.0 Blocks Lifecycle Scripts by Default - Socket
[socket.dev/blog/pnpm-10-0-0-blocks-lifecycle-scripts-by-default](https://socket.dev/blog/pnpm-10-0-0-blocks-lifecycle-scripts-by-default "pnpm 10.0.0 Blocks Lifecycle Scripts by Default - Socket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

pnpm 10에서는 설치할 패키지의 lifecycle script 실행 기본적으로 무효.


----

## Introducing TanStack Start – Frontend Masters Boost
[frontendmasters.com/blog/introducing-tanstack-start/](https://frontendmasters.com/blog/introducing-tanstack-start/ "Introducing TanStack Start – Frontend Masters Boost")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

TanStack Router 이용한 풀스택 React 프레임워크인 TanStack Start에 대하여


----

## Node.js Type Stripping Explained
[satanacchio.hashnode.dev/everything-you-need-to-know-about-nodejs-type-stripping](https://satanacchio.hashnode.dev/everything-you-need-to-know-about-nodejs-type-stripping "Node.js Type Stripping Explained")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.js의 TypeScript 지원하는 접근 방법에 대하여.
앞으로 TypeScript 팀을 구성하는 로드맵에 대하여


----

## Angular 2025 Strategy. For the past two and a half years… | by Minko Gechev | Jan, 2025 | Angular Blog
[blog.angular.dev/angular-2025-strategy-9ca333dfc334](https://blog.angular.dev/angular-2025-strategy-9ca333dfc334 "Angular 2025 Strategy. For the past two and a half years… | by Minko Gechev | Jan, 2025 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular의 2024년 앙케이트 결과 분석, 2025년 이룰 점에 대하여.
개발자 체험 관련해 zoneless, Signal forms, Karma 변경에 대하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## standard-schema/standard-schema: A standard interface for TypeScript schema validation libraries
[github.com/standard-schema/standard-schema](https://github.com/standard-schema/standard-schema "standard-schema/standard-schema: A standard interface for TypeScript schema validation libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">proposal</span></p>

zod 스키마 검증 라이브러리의 표준 인터페이스를 의논하는 레포지터리.
표준적 인터페이스를 결정함으로, UI 라이브러리가 특정 스키마 검증 라이브러리에 의존하지 않는 것이 목적


----
