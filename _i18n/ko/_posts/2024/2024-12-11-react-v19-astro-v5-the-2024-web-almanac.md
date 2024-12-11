---
title: "2024-12-11: React v19, Astro v5, The 2024 Web Almanac"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-12-11T02:51:36.980Z
category: JSer
tags:
- React
- TypeScript
- Chrome
- document
- performance

---

JSer.info #718 - React v19가 출시되었습니다.

- [React v19 – React](https://react.dev/blog/2024/12/05/react-19)
- [Release 19.0.0 (December 5, 2024) · facebook/react](https://github.com/facebook/react/releases/tag/v19.0.0)

2년 반 만의 메이저 출시입니다.
비동기 전환을 다루는 액션 개념 추가와 `useActionState`/`useFormStatus`/`useOptimistic`/`use` API 추가되었습니다.
또한, react-dom에 prerender API 추가, Server Component와 Server Action 추가 있습니다.

그 외 개선으로, `ref`를 props으로 전달 할 때 `forwardRef`가 필요 없어졌으며, Hydration Error 개선, `ref` callback가 cleanup 함수 반환이 있습니다.
`<title>`/`<meta>`/`<link>` 등 메타태그 지원, `<link rel=stylesheet>`나 `<script async={true} src=...>` 지원도 추가되었습니다.
그리고, 자원의 preload API 지원, Custom Element 지원도 있습니다.

Next.js은 15.1에서 React v19 Stable 지원합니다.

- [Next.js 15.1 | Next.js](https://nextjs.org/blog/next-15-1)

---

Astro 5.0가 출시되었습니다.

- [Astro 5.0 | Astro](https://astro.build/blog/astro-5/)
- [astro/packages/astro/CHANGELOG.md at main · withastro/astro](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#500)

Content Layer 개선, Server Islands/astro:env를 Stable으로, Vite 6으로 업데이트가 있습니다.

---

HTTP Archive 데이터를 기반으로 한 웹 스테이터스 정리 레포트 The 2024 Web Almanac가 출시되었습니다.

- [The 2024 Web Almanac](https://almanac.httparchive.org/en/2024/)

HTML/CSS/JavaScript/Performance/Accessibility/SEO/Security 등 폭 넓은 항목을 조사해 레포트로 정리했습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## React v19 – React
[react.dev/blog/2024/12/05/react-19](https://react.dev/blog/2024/12/05/react-19 "React v19 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 19 출시.
비동기 전환 다루는 액션 개념 추가와 `useActionState`/`useFormStatus`/`useOptimistic`/`use` API 추가.
react-dom에서 prerender API 추가, Server Component와 Server Action 추가.
`ref`를 props으로 전달할 때 `forwardRef` 필요없도록, Hydration Error 개선, `ref` callback가 cleanup 함수 반환.
`<title>`/`<meta>`/`<link>` 등 메타태그 지원, `<link rel=stylesheet>`이나 `<script async={true} src=...>` 지원.
자원 preload API 지원, Custom Element 지원

- [Release 19.0.0 (December 5, 2024) · facebook/react](https://github.com/facebook/react/releases/tag/v19.0.0 "Release 19.0.0 (December 5, 2024) · facebook/react")
- [Release v15.0.4 · vercel/next.js](https://github.com/vercel/next.js/releases/tag/v15.0.4 "Release v15.0.4 · vercel/next.js")

----

## ECMAScript proposal updates @ 2024-12 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/12/08/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/12/08/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-12 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2024년 12월 TC39 미팅으로 인한 ECMAScript Proposal 상태 변경 모음.
Sync Imports 추가, `Error.isError`가 Stage 3으로, `Intl.DurationFormat`가 Stage 4로


----

## Astro 5.0 | Astro
[astro.build/blog/astro-5/](https://astro.build/blog/astro-5/ "Astro 5.0 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 5.0 출시.
Content Layer 개선, Server Islands/astro:env가 Stable, Vite 6으로 업데이트

- [astro/packages/astro/CHANGELOG.md at main · withastro/astro](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#500 "astro/packages/astro/CHANGELOG.md at main · withastro/astro")

----

## Next.js 15.1 | Next.js
[nextjs.org/blog/next-15-1](https://nextjs.org/blog/next-15-1 "Next.js 15.1 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 15.1 출시.
React 19 Stable 대응, Source Maps 개선, 에러 스택 트레이스 개선.
실험적 기능으로 `forbidden()`과 `unauthorized()` 추가, `<link>`와 `<style>` 인라인화 대응.


----
<h1 class="site-genre">읽을거리</h1>

----

## 다시 배우는 satisfies 연산자
[zenn.dev/okkun/articles/ed6f146e03c60a](https://zenn.dev/okkun/articles/ed6f146e03c60a "다시 배우는 satisfies 연산자")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript의 `satisfies` 연산자 사용 방법에 대하여


----

## 니코니코 생방송 애플리케이션에 Rspack 도입한 이야기
[zenn.dev/thiry/articles/0f671d086b2fb0](https://zenn.dev/thiry/articles/0f671d086b2fb0 "니코니코 생방송 애플리케이션에 Rspack 도입한 이야기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

webpack에서 rspack으로 이행한 것에 대하여.
css modules 일부 동작에 문제가 있지만, 대부분이 webpack와 호환성이 있는 상태로 bundle 퍼포먼스가 개선되었다는 이야기


----

## Introducing Nuxt Icon v1 · Nuxt Blog
[nuxt.com/blog/nuxt-icon-v1-0](https://nuxt.com/blog/nuxt-icon-v1-0 "Introducing Nuxt Icon v1 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Nuxt</span> <span class="jser-tag">article</span></p>

Nuxt Icon v1.0 출시.
아이콘 로드 방법 비교와 Nuxt Icon 구현 관련하여.
img 태그 / Web 폰트 / 인라인 SVG / 동적인 API / 컴포넌트 / CSS 아이콘 접근 비교.
Nuxt Icon일 때는CSS 모드와 SVG 모드 모두 지원하며, 아이콘째로 갈아끼워진다.


----

## What&#039;s new in DevTools, Chrome 132  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-devtools-132?hl&#x3D;en](https://developer.chrome.com/blog/new-in-devtools-132?hl=en "What&#039;s new in DevTools, Chrome 132  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 132에서 Chrome DevTools 변경점에 대하여.
AI assistance 개선, 퍼포먼스 탭의 Network 패널에 그 자원이 렌더링 블록되고 있는가 보여짐, `scheduler.postTask` 가시화


----

## How To Improve INP: Yield Patterns | Jacob &#039;Kurt&#039; Groß
[kurtextrem.de/posts/improve-inp](https://kurtextrem.de/posts/improve-inp "How To Improve INP: Yield Patterns | Jacob &#039;Kurt&#039; Groß")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React 애플리케이션 Interaction-to-Next-Paint(INP) 개선하는 접근에 대한 연재 기사


----

## State of JavaScript 2024
[survey.devographics.com/survey/state-of-js/2024](https://survey.devographics.com/survey/state-of-js/2024 "State of JavaScript 2024")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span></p>

JavaScript 관련 개발자 앙케이트 State of JavaScript 2024 모집 시작


----

## A leap in the evolution of Airtable’s codebase: Scaling TypeScript to thousands of projects | by Michael Mitchell | The Airtable Engineering Blog | Dec, 2024 | Medium
[medium.com/airtable-eng/a-leap-in-the-evolution-of-airtables-codebase-scaling-typescript-to-thousands-of-projects-734326c3a553](https://medium.com/airtable-eng/a-leap-in-the-evolution-of-airtables-codebase-scaling-typescript-to-thousands-of-projects-734326c3a553 "A leap in the evolution of Airtable’s codebase: Scaling TypeScript to thousands of projects | by Michael Mitchell | The Airtable Engineering Blog | Dec, 2024 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

Bazel 사용해서 TypeScript 병렬 빌드를 최적화한 이야기.
TypeScript 프로젝트끼리 순환참조한 것을 Copilot 사용해서 인터페이스 분리, Isolated Declarations 사용한 병렬 빌드 가능하도록 명시적으로 자료형 명명


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## CSS Wrapped 2024
[chrome.dev/css-wrapped-2024/](https://chrome.dev/css-wrapped-2024/ "CSS Wrapped 2024")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">css </span> <span class="jser-tag">document</span> <span class="jser-tag">example</span> <span class="jser-tag">Chrome</span></p>

2024년에 Chrome 추가된 CSS 기능을 체험 가능한 사이트.


----

## onlook-dev/onlook: The open source, local-first Figma for React. Design directly in your live React app and publish your changes to code.
[github.com/onlook-dev/onlook](https://github.com/onlook-dev/onlook "onlook-dev/onlook: The open source, local-first Figma for React. Design directly in your live React app and publish your changes to code.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">figma</span> <span class="jser-tag">editor</span> <span class="jser-tag">software</span></p>

Figma스러운 UI로 React애플리케이션 편집 가능한 에디터 애플리케이션


----

## The 2024 Web Almanac
[almanac.httparchive.org/en/2024/](https://almanac.httparchive.org/en/2024/ "The 2024 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">document</span> <span class="jser-tag">HTTP</span></p>

Web Almanac의 2024년판 공개.
HTTP Archive 데이터를 근거로 웹사이트 스테이터스 정리해서 레포트.


----
