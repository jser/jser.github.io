---
title: "2022-03-15:  React 18 RC, playwright v1.20.0, Safari 15.4 변경 사항"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-03-15T03:48:47.857Z
category: JSer
tags:
- React
- node.js
- TypeScript
- ECMAScript
- book

---

JSer.info #583 - React 18 RC가 릴리스 됐다.

- [How to Upgrade to the React 18 Release Candidate – React Blog](https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html)

React 18 RC에서는 IE 지원을 종료한다. IE를 지원해야하는 프로젝트라면 React 17 버전으로 고정해야 한다.

ReactDOM의 `render` API를 비권장하고 대신에 `createRoot` API가 권장된다.
SSR API의 `renderToNodeStream`을 비권장하고 Suspense를 지원하는 `renderToPipeableStream`과 `renderToReadableStream`가 추가됐다.

`setState` 등의 상태 갱신을 자동으로 배치(batching) 처리하도록 개선됐고 React 17의 동작을 재현하기 위한 `flushSync` API가 추가됐다.
또, Redux 등과 같이 React 바깥에서 상태를 관리하는 라이브러리를 위한 `userId` / `useSyncExternalStore` / `useInsertionEffect` API가 추가됐다.

이어, `<StrictMode>`의 새로운 개발 환경 검사로 다시 마운트 시 상태 복원을 시뮬레이션하는 동작이 추가됐다.
그리고 테스트 실행 환경임을 React에게 알릴 수 있는 `global.IS_REACT_ACT_ENVIRONMENT` 플래그가 추가됐다.

---

playwright 1.20.0이 릴리스 됐다.

- [Release v1.20.0 · microsoft/playwright](https://github.com/microsoft/playwright/releases/tag/v1.20.0)

스크린샷 API에 애니메이션을 비활성화하는 옵션과 특정 부분을 숨길 수 있는 `mask` 옵션이 추가됐다.
`expect().toMatchSnapshot()`에서 anomymouse snapshots을 지원하며 `maxDiffPixels`와 `maxDiffPixelRatio` 옵션이 추가 됐다.
또, 테스트 케이스 별로 병렬로 수행할 수 있는 `fullyParallel` 모드 옵션이 추가됐다.

----

[New WebKit Features in Safari 15.4 | WebKit](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/)에는 Safari 15.4의 변경 사항이 정리돼 있다.

꽤 다양한 기능이 추가 됐으며 주 내용을 다음과 같이 정리할 수 있다.

- `<dialog>` 요소 지원
- CSS의 `:has()` 의사 클래스 지원
- Cascade Layers 지원
- CSS Containment 지원
- 새로운 Viewport Units으로 `lvh`와 `svh` 등 지원
- `:focus-visible` 의사 클래스 지원
- `calc()`에서 math function 지원
- 비표준 `-webkit-` 접두사를 몇 개의 CSS 프로퍼티에서 제거
- BroadcastChannel 지원
- `window.scroll`의 `scroll-behavior` 프로퍼티 지원
- `structuredClone` API 지원
- File System Access API 지원
- ES2022의 `at()` 메서드와 `Object.hasOwn()` 메서드 지원
- ECMAScript Proposal Stage 3인 `findLast()` 메서드 지원
- `Intl` 구현을 사양에 맞춰 수정
- Web App Manifest 대응 개선
- `navigationPreload` 지원
- `requestVideoFrameCallback()` 지원
- CSP Lv3 지원 개선
- XSS Auditor 삭제


----

<h1 class="site-genre">헤드라인</h1>

----

## How to Upgrade to the React 18 Release Candidate – React Blog
[reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html](https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html "How to Upgrade to the React 18 Release Candidate – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>


React 18 RC 릴리스.
IE 지원 종료, ReactDOM의 `render` API를 비권장하고 `createRoot` API 사용을 권장한다.
SSR API의 `renderToNodeStream`를 비권장하고 Suspense를 지원하는 `renderToPipeableStream`과 `renderToReadableStream`이 추가됐다.
₩setState₩의 상태 갱신을 자동으로 배치(batching) 처리하도록 개선됐고 React 17의 동작을 재현하기 위한 `flushSync` API가 추가됐다.
또, Redux 등과 같이 React 바깥에서 상태를 관리하는 라이브러리를 위한 `userId` / `useSyncExternalStore` / `useInsertionEffect` API가 추가됐다.


----

## Node v17.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.7.0/](https://nodejs.org/en/blog/release/v17.7.0/ "Node v17.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v17.7.0 릴리스.
`net.Socket`과 `net.Server`에 `noDelay` / `keepAlive` / `keepAliveInitialDelay` 옵션이 추가 됐다.


----

## Release v8.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v8.0.0](https://github.com/vueuse/vueuse/releases/tag/v8.0.0 "Release v8.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v8.0.0 릴리스.
`@vueuse/core/nuxt`를 삭제하고 대신에 `@vueuse/nuxt`를 공개.
`useTimeoutPoll` / `useDateFormat` / `useGamepad` / `useFileSystemAccess` / `useChangeCase` 추가.


----

## Release v8.0.0 · breejs/bree
[github.com/breejs/bree/releases/tag/v8.0.0](https://github.com/breejs/bree/releases/tag/v8.0.0 "Release v8.0.0 · breejs/bree")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Job 스케줄러 Bree 8.0.0 릴리스.


----

## Release v1.20.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.20.0](https://github.com/microsoft/playwright/releases/tag/v1.20.0 "Release v1.20.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.20.0 릴리스.
스크린샷 API에 애니메이션을 비활성화하는 옵션과 특정 부분을 감추는 `mask` 옵션이 추가됐다.
`expect().toMatchSnapshot()`에서 anomymouse snapshots를 지원하며 `maxDiffPixels`과 `maxDiffPixelRatio` 옵션이 추가됐다.
테스트 케이스 별로 병렬로 수행할 수 있는 `fullyParallel` 모드 옵션이 추가됐다.


----

## New WebKit Features in Safari 15.4 | WebKit
[webkit.org/blog/12445/new-webkit-features-in-safari-15-4/](https://webkit.org/blog/12445/new-webkit-features-in-safari-15-4/ "New WebKit Features in Safari 15.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 15.4의 변경 사항 정리.
`<dialog>` 요소를 지원하고 CSS의 `:has()` 의사 클래스, Cascade Layers, CSS Containment 지원한다.
새로운 Viewport Units으로 `lvh`와 `svh` 등 지원, `:focus-visible` 클래스 지원, `calc()`에서 math function을 사용할 수 있다.
비표준 `-webkit` 접두어가 붙은 몇 개의 CSS 속성에서 접두어를 제거했다.
BroadcastChannel, `window.scroll`의 `scroll-behavior` 프로퍼티, `structuredClone`, File System Access API를 지원한다.
ES2022의 `at()` 메서드와 `Object.hasOwn()` 메서드, ECMAScript Proposal Stage 3인 `findLast()` 메서드를 지원한다.
`Intl` 구현을 사양에 맞춰 수정햇고 Web App Manifest 대응 개선, `navigationPreload`를 지원한다.
`requestVideoFrameCallback()` 지원, CSP Lv3 지원 개선, XSS Auditor가 삭제 됐다.


----
<h1 class="site-genre">아티클</h1>

----

## Learn PWA
[web.dev/learn/pwa/](https://web.dev/learn/pwa/ "Learn PWA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">tutorial</span></p>

PWA를 학습할 수 있는 튜토리얼 사이트.


----

## Typed Ember is now the Ember TypeScript Core Team!
[blog.emberjs.com/typed-ember-is-now-the-ember-type-script-core-team/](https://blog.emberjs.com/typed-ember-is-now-the-ember-type-script-core-team/ "Typed Ember is now the Ember TypeScript Core Team!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Ember의 TypeScript 지원을 코어의 서브팀에서 진행한다는 이야기.
Ember CLI로의 통합, Glint에서 템플릿과 타입 체크, Ember 자체 타입 정의 개선, RFC를 통한 TypeScript 지원 시의 영향 조사 등을 담당한다.

- [0724-road-to-typescript](https://emberjs.github.io/rfcs/0724-road-to-typescript.html "0724-road-to-typescript")
- [typed-ember/glint: TypeScript powered tooling for Glimmer templates](https://github.com/typed-ember/glint "typed-ember/glint: TypeScript powered tooling for Glimmer templates")

----

## A Proposal For Type Syntax in JavaScript - TypeScript
[devblogs.microsoft.com/typescript/a-proposal-for-type-syntax-in-javascript/](https://devblogs.microsoft.com/typescript/a-proposal-for-type-syntax-in-javascript/ "A Proposal For Type Syntax in JavaScript - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

TypeScript 팀이 실행 시에는 브라우저에서 무시(무효화)되는 방식의 타입 구문을 ECMAScript의 Proposal로 제안한다.
해당 문서에는 제안하게 된 계기, 향후 계획 등이 작성돼 있다.

- [giltayar/proposal-types-as-comments: ECMAScript proposal for type syntax that is erased - Stage 0](https://github.com/giltayar/proposal-types-as-comments "giltayar/proposal-types-as-comments: ECMAScript proposal for type syntax that is erased - Stage 0")

----

## JavaScript naming conflicts: How existing code can force proposed features to be renamed
[2ality.com/2022/03/naming-conflicts.html](https://2ality.com/2022/03/naming-conflicts.html "JavaScript naming conflicts: How existing code can force proposed features to be renamed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">issue</span></p>

ECMAScript의 새로운 Proposal로 인해 기존 Web을 고장나는 이른바 “break the web"이 어떤 경우에 일어나게 되는지 설명하는 글.
빌트인 프로토타입 변경, 프로퍼티 명 경합, with에 의한 충돌 등 문제가 발생할 수 있는 원인을 소개하고 회피하기 위한 몇가지 원칙을 소개한다.


----

## WebGPU — All of the cores, none of the canvas — surma.dev
[surma.dev/things/webgpu/](https://surma.dev/things/webgpu/ "WebGPU — All of the cores, none of the canvas — surma.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGPU</span> <span class="jser-tag">article</span></p>

WebGPU에 대한 소개 기사.
WebGL은 OpenGL의 래퍼지만 WebGPU는 독자적 추상화 레이어를 갖고 있다는 점과 WGSL이라는 WebGPU의 쉐이딩 언어를 함께 소개한다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## daisyUI — Tailwind CSS Components
[daisyui.com/](https://daisyui.com/ "daisyUI — Tailwind CSS Components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

UI 컴포넌트의 외형을 제공하는 Tailwind 플러그인.
사전에 정의된 컴포넌트 클래스명을 지정하여 UI를 정의하고 추가로 클래스명에 Tailwind의 Utility를 지정하여 사용자 정의하는 방식.


----
<h1 class="site-genre">도서</h1>

----

## Micro State Management with React Hooks | Packt
[www.packtpub.com/product/micro-state-management-with-react-hooks/9781801812375](https://www.packtpub.com/product/micro-state-management-with-react-hooks/9781801812375 "Micro State Management with React Hooks | Packt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

React에서의 상태 관리를 주제로 한 도서


----
