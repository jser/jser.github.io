---
title: "2025-05-29: TypeScript Native Previews, Firefox 139, Angular 20, Chrome 137"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-05-29T01:31:32.863Z
category: JSer
tags:
- TypeScript
- Bun
- nodejs
- ESLint
- golang

---

JSer.info #736 - TypeScipt의 Go언어 네이티브 구현 `@typescript/native-preview`가 공개되었습니다.

- [Announcing TypeScript Native Previews - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/)

TypeScript를 Go언어로 이식 구현한 것으로, 컴파일러인 `tsgo`와 같이 VSCode 확장도 출시되었습니다.

- [TypeScript 네이티브 이식 관찰 레포트 TSKaigi 2025 - Speaker Deck](https://speakerdeck.com/berlysia/typescript-native-porting-observation-tskaigi-2025)


---

Firefox 139가 출시되었습니다.

- [Firefox 139.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/139.0/releasenotes/)
- [Firefox 139 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/139)

`hidden=until-found` 속성 지원과 Temporal API 구현 포함됩니다. 실험적 기능으로, Prioritized Task Scheduling API, View Transition API, HTML 속성에 의한 `<`과 `>` 자동 이스케이프 기능이 추가되었습니다.

---

Angular v20가 출시되었습니다.

- [Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301)

`effect`, `linkedSignal`, `toSignal`, Incremental hydration과 route-level render mode config가 Stable으로 변경되었습니다. Zoneless는 Developer Preview으로 이행, 실험적 기능으로 `httpResource`과 vitest 지원도 추가되었습니다. 또한, Chrome DevTools에서의 Angular 고유성능 정보를 다루는 `ng.enableProfiling()` API가 추가되었습니다.
또한, `*ngIf`/`*ngFor`/`*ngSwitch` 비권장도 포함되어 있습니다.

---

Chrome 137가 출시되었습니다.

- [New in Chrome 137  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-137)
- [Chrome 137  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/137)

CSS 관련으로는 조건이 있는 값을 표현 하는 `if()` 함수와, 포커스 네비게이션 순서를 제어하는 `reading-flow`/`reading-order` 프로퍼티가 추가되었습니다. Web API 관련으로는, Selection API `getComposedRanges()`와 `direction` 프로퍼티, Web Cryptography에서의 Ed25519 지원디 추가됩니다. WebAssembly에는, JavaScript Promise Integration（JSPI）정식 지원이 포함됩니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Node.js — Node v24.1.0 (Current)
[nodejs.org/en/blog/release/v24.1.0](https://nodejs.org/en/blog/release/v24.1.0 "Node.js — Node v24.1.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.1.0 출시.
`node:fs`의 `glob`가 Stable이 되고, experimental의 warning가 나오지 않습니다


----

## Announcing TypeScript Native Previews - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-native-previews/](https://devblogs.microsoft.com/typescript/announcing-typescript-native-previews/ "Announcing TypeScript Native Previews - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">golang</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript의 Go언어 네이티브 구현 `@typescript/native-preview`가 공개


----

## Bun v1.2.14 | Bun Blog
[bun.sh/blog/bun-v1.2.14](https://bun.sh/blog/bun-v1.2.14 "Bun v1.2.14 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.14 출시.
`bun install`가 `catalog:` 지원, Fetch API가 zstd 지원, `"module": "Preserve"` 기본으로 변경


----

## Release v9.0.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v9.0.0](https://github.com/storybookjs/storybook/releases/tag/v9.0.0 "Release v9.0.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook v9.0.0 출시.


----

## Firefox 139.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/139.0/releasenotes/](https://www.mozilla.org/en-US/firefox/139.0/releasenotes/ "Firefox 139.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 139 출시.
`hidden=until-found` 지원, Temporarl API 지원.
실험적 기능으로, Prioritized Task Scheduling API/View Transition API/속성에 의한 `<`과 `>`를 자동적 이스케이프

- [Firefox 139 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/139 "Firefox 139 for developers - Mozilla | MDN")

----

## Bun v1.2.15 | Bun Blog
[bun.sh/blog/bun-v1.2.15](https://bun.sh/blog/bun-v1.2.15 "Bun v1.2.15 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.15 출시.
`bun audit` 추가, `BUN_OPTIONS` 환경변수 추가, `vm.SourceTextModule` 지원, `perf_hooks.createHistogram()` 지원


----

## Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog
[blog.angular.dev/announcing-angular-v20-b5c9c06cf301](https://blog.angular.dev/announcing-angular-v20-b5c9c06cf301 "Announcing Angular v20. The past couple of years have been… | by Minko Gechev | May, 2025 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v20. 출시.
`effect`/`linkedSignal`/`toSignal`, Incremental hydration과 route-level render mode config가 Stable으로 변경
Zoneless가 Developer Preview으로 변경.
실험적 기능으로 `httpResource` 추가, vitest 지원.
Chrome DevTools에서 Angular 특유의 성능 정보를 다루는 `ng.enableProfiling()` API 추가.
template expression에서 `**`와 `in` 연산자.
`*ngIf`/`*ngFor`/`*ngSwitch` 비권장


----

## New in Chrome 137  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-137?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-137?hl=en "New in Chrome 137  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 137 출시.
CSS 관련에는, 조건 있는 값을 표현하는  `if()` 함수 추가.
포커스 네비게이션 순서를 제어하는 `reading-flow`/`reading-order` 프로퍼티 추가. 필기체에서 문자간격 무시하는 개선, `accent-color` 프로퍼티 시스템 accent 색 대응 구현. `offset-path: shape()`  지원.

Web API 관련으로는, Selection API에 `getComposedRanges()` 와 `direction` 프로퍼티 추가. Blob URL 파티셔닝 (fetch/navigation) 구현.
Web Cryptography에서 `Ed25519` 지원 추가. HSTS 캐시를 사용한 트래킹 방지하는 기능 구현. 응답하지 않는 Web 페이지 크러쉬 레포트를 Reporting API로 지원.

WebAssembly 방면에서는, JavaScript Promise Integration（JSPI）정식 지원.
branch hint 지원

- [Chrome 137  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/137 "Chrome 137  |  Release notes  |  Chrome for Developers")

----
<h1 class="site-genre">읽을거리</h1>

----

## ESLint v9.0.0: A retrospective - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/](https://eslint.org/blog/2025/05/eslint-v9.0.0-retrospective/ "ESLint v9.0.0: A retrospective - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint v9.0.0의 retrospective.
잘된 점과 잘 되지 않은 점 관련하여.
지원 버전 정책과 v8.x/v9.x 공존 백포트는 잘 됨.
한 편으로 파괴적인 변경이 많은 문제가 있어서, 도구가 부족해져 업데이트가 힘들어진 문제나 에코시스템과 협력성 부족이 있음


----

## TSKaigi 자료 정리
[zenn.dev/m\_n/articles/a1189e28e43313](https://zenn.dev/m_n/articles/a1189e28e43313 "TSKaigi 자료 정리")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">document</span></p>

TSKaigi 2025 슬라이드 정리

- [TSKaigi 2025](https://2025.tskaigi.org/ "TSKaigi 2025")

----

## Wake up, Remix! | Remix
[remix.run/blog/wake-up-remix](https://remix.run/blog/wake-up-remix "Wake up, Remix! | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

Remix 앞으로는 방향성.
Remix v2는 React Router 얇은 래퍼였음.
Remix v3는 DB나 내장 컴포넌트를 포함한 프레임워크가 되었고, 또한 React가 아닌 Preact의 fork를 기반으로 한 구현 예정.
Remix 기본적 방침 언급


----

## A brief history of JavaScript | Deno
[deno.com/blog/history-of-javascript](https://deno.com/blog/history-of-javascript "A brief history of JavaScript | Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">history</span></p>

브라우저 / JavaScript / 라이브러리 역사를 타임라인으로 정리


----

## Introducing \`jsr:\` Support
[blog.vlt.sh/blog/jsr-support](https://blog.vlt.sh/blog/jsr-support "Introducing \`jsr:\` Support")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

vlt가 `jsr:` prefix에서 JSR 패키지 설치 지원


----

## React, visualized – react.gg
[react.gg/visualized](https://react.gg/visualized "React, visualized – react.gg")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React 동작을 비주얼라이즈 소개


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 2025-05-23 Signal과 Observable ― 새로운 데이터 모델을 뜯어보기 (TSKaigi 2025) - Google 슬라이드
[docs.google.com/presentation/d/1c7fYqn7-v3hnbKtmwXHbvwuCs6cNq\_ThLKVDZ7rvbA0/preview#slide&#x3D;id.g260298bad6d\_0\_77](https://docs.google.com/presentation/d/1c7fYqn7-v3hnbKtmwXHbvwuCs6cNq_ThLKVDZ7rvbA0/preview#slide=id.g260298bad6d_0_77 "2025-05-23 Signal과 Observable ― 새로운 데이터 모델을 뜯어보기 (TSKaigi 2025) - Google 슬라이드")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

ECMAScript Stage 1의 Signals와 WCIG Observable 관련 슬라이드.
Pull/Push 기반 연속성 있는 값 다루기


----
