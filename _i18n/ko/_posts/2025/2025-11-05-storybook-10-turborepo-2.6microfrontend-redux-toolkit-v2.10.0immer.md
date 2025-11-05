---
title: "2025-11-05: Storybook 10, Turborepo 2.6(Microfrontend),  redux-toolkit v2.10.0과 Immer 성능 개선"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-11-04T23:58:24.027Z
category: JSer
tags:
- Tools
- rspack
- performance
- nodejs
- storybook

---

JSer.info #754 - Storybook v10.0.0가 출시되었다.

- [Release v10.0.0 · storybookjs/storybook](https://github.com/storybookjs/storybook/releases/tag/v10.0.0)

ESM-only로 변경해 설치 크기 29% 경감, dist 코드를 unminify화 했다. 새로운 기능으로, Module automocking 지원, Typesafe한 CSF factories, 탭 필터 기능 개선도 포함된다.
또한, Next 16, Vitest 4, Svelte 비동기 컴포넌트 대응도 추가된다.

---

Turborepo 2.6가 출시되었다.

- [Turborepo 2.6 | Turborepo](https://turborepo.com/blog/turbo-2-6)

Microfrontend 지원으로, 로컬 개발의 path 라우팅 정의 가능한 `microfrontends.json`가 추가되었다.
Vercel의 [Microfrontends](https://vercel.com/docs/microfrontends) 지원 일환으로 제공된 것. 또한, Bun 지원, TUI 개선도 포함되었다.

---

Redux Toolkit v2.10.0가 출시되었다.

- [Release v2.10.0 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0)

Redux 관리자가 Immer 성능 개선해서, Immer 10.2.0으로 업데이트 되었다.
다음 Issue에서 Immer 성능 문제에 대해 조사했다.

- [Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer](https://github.com/immerjs/immer/issues/1152)

이 업데이트인해, Immer 성능 문제가 개선되었다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v10.0.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v10.0.0](https://github.com/storybookjs/storybook/releases/tag/v10.0.0 "Release v10.0.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook v10.0.0 출시.
ESM-only으로 변경해서 설치 크기를 29% 경감, dist 코드를 unminify화.
Module automocking 지원, Typesafe한 CSF factories, 탭 필터 기능 개선.
Next 16/Vitest 4/Svelte 비동기 컴포넌트 대응


----

## Turborepo 2.6 | Turborepo
[turborepo.com/blog/turbo-2-6](https://turborepo.com/blog/turbo-2-6 "Turborepo 2.6 | Turborepo")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Turborepo 2.6 출시.
Microfrontend 지원으로, 로컬 개발용 path 라우팅 정의가 가능한 `microfrontends.json` 추가.
Bun 지원, TUI 개선の


----

## Electron 39.0.0 | Electron
[www.electronjs.org/blog/electron-39-0](https://www.electronjs.org/blog/electron-39-0 "Electron 39.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 39.0.0 출시.
Chromium 142/Node.js 22.20/V8 14.2 업그레이드.
ASAR integrity가 Stable에, `window.open` 팝업은 항상 크기가 변경 가능하도록


----

## New in Chrome 142  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-142?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-142?hl=en "New in Chrome 142  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 142 출시.
`:target-before`/`:target-after` 추상 클래스 추가, Style Container Queries와 `if()` 함수 범위 구문 지원.
`interestfor` 속성 추가, `document.activeViewTransition` 프로퍼티 추가.
WebGPU의 `primitive_index` 기능과 텍스쳐 형식 tier1/tier2 지원.
로컬 네트워크 리퀘스트 허용 프롬프트 표기 가능하도록

- [Chrome 142  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/142 "Chrome 142  |  Release notes  |  Chrome for Developers")

----

## Release v2.10.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.10.0 "Release v2.10.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v2.10.0 출시.
Immer의 성능 개선하는 Immer 10.2.0 업데이트

- [Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer](https://github.com/immerjs/immer/issues/1152 "Immer perf appears to have gotten worse over time, based on updated benchmarks · Issue #1152 · immerjs/immer")

----

## Announcing Rspack 1.6 - Rspack
[rspack.rs/blog/announcing-1-6](https://rspack.rs/blog/announcing-1-6 "Announcing Rspack 1.6 - Rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">ReleaseNote</span></p>

Rspack 1.6 출시.
Dynamic import의 Tree Shaking 개선, import defer 지원.
ESM 출력 개선하는 `EsmLibraryPlugin` 추가, Barrel 파일 최적화 기반적으로 유효화, layer 기능 안정화.
빌드할 때에 JSX 구문을 유지하는 옵션 추가, Source Map 추출하는 `extractSourceMap` 옵션 추가.
Rsbuild 1.6에는, 브라우저 에러 로그를 터미널 전송 가능하도록, Rslib 1.6에는 typescript-go 기반 자료형 선언 파일 생성 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## Introducing TanStack Start Middleware – Frontend Masters Blog
[frontendmasters.com/blog/introducing-tanstack-start-middleware/](https://frontendmasters.com/blog/introducing-tanstack-start-middleware/ "Introducing TanStack Start Middleware – Frontend Masters Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

TanStack Start의 middleware에 대하여


----

## I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance | Loren Stewart
[www.lorenstew.art/blog/10-kanban-boards/](https://www.lorenstew.art/blog/10-kanban-boards/ "I Built the Same App 10 Times: Evaluating Frameworks for Mobile Performance | Loren Stewart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

10개 프레임워크에서 같은 칸반 애플리케이션을 만들어 모바일 성능 비교한 글.
번들 크기. 모바일 환경에서 성능, MPA와 SPA, React 이외 선택지에 대하여


----

## Node.js — Node.js v22 to v24
[nodejs.org/en/blog/migrations/v22-to-v24](https://nodejs.org/en/blog/migrations/v22-to-v24 "Node.js — Node.js v22 to v24")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js v22에서 v24 변경과 마이그레이션 도구


----

## The Inner Workings of JavaScript Source Maps
[www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals](https://www.polarsignals.com/blog/posts/2025/11/04/javascript-source-maps-internals "The Inner Workings of JavaScript Source Maps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">article</span></p>

Source Mao 구조에 대하여.
Source Map 형식이나 VLQ 인코딩 구조에 대하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## TanCN - Form and Table Builder
[tancn.dev/](https://tancn.dev/ "TanCN - Form and Table Builder")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">UI</span></p>

TanStack 사용한 폼 빌더


----


## Triplex Goes Open Source and Moves to Poimandres • Triplex
[triplex.dev/blog/triplex-moves-to-pmndrs](https://triplex.dev/blog/triplex-moves-to-pmndrs "Triplex Goes Open Source and Moves to Poimandres • Triplex")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">3D</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

React에서 3D 컴포넌트 만드는 도구

- [pmndrs/triplex: The open source visual workspace for React / Three Fiber. Build the 2D and 3D web.](https://github.com/pmndrs/triplex "pmndrs/triplex: The open source visual workspace for React / Three Fiber. Build the 2D and 3D web.")

----

## @remix-run/node-fetch-server - npm
[www.npmjs.com/package/@remix-run/node-fetch-server](https://www.npmjs.com/package/@remix-run/node-fetch-server "@remix-run/node-fetch-server - npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Fetch API의 `Request`/`Response` 사용한 HTTP 서버 라이브러리.

