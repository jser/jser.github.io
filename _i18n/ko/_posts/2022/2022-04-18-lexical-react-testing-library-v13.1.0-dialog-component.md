---
title: "2022-04-18のJS: Lexical、React Testing Library v13.1.0、Dialog component 작성"
author: "azu"
translator: Daewon Seo
layout: post
date: 2022-04-18T13:36:16.175Z
category: JSer
tags:
  - React
  - HTML
  - JSON
  - TypeScript
  - polyfill
---

JSer.info #588 - Lexical이라고 하는 텍스트 에디터를 만들기 위한 JavaScript 프레임워크가 공개되었다.

- [facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.](https://github.com/facebook/lexical)

에디터의 상태를 double-buffering으로 관리하고, 상태 변경을 diff/patch로 표시하여 반영하는 구조로 되어있다.
또한 contentEditable을 사용하지만, 외부에서 변경을 MutationObserver로 감시하여, 에디터의 상태를 갱신하고 있다.

Lexical은 동일하게 Facebook에서 만들고 있는[Draft.js](https://draftjs.org/)의 후속작인 라이브러리로, API의 호환은 되지않지만 앞으로 마이그레이션 가이드가 만들어질 예정이다.

- [Add Draft JS to Lexical migration documentation · Issue #1641 · facebook/lexical](https://github.com/facebook/lexical/issues/1641)

---

React DOM의 테스트 라이브러리인 React Testing Library v13.1.0이 릴리스 됐다.

- [Release v13.1.0 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0)

React Testing Library v13.1.0에서는 `renderHook`이라 하는 API가 추가되었다.
이 API는 React Hooks의 테스트를 하기 위한 것으로 [`@testing-library/react-hooks`](https://github.com/testing-library/react-hooks-testing-library)
을 바탕으로 구현되었다.

상세한 경위는 다음 PR에 쓰여있지만,[`@testing-library/react-hooks`](https://github.com/testing-library/react-hooks-testing-library)은 React 18의 대응을 어렵게 하는 부분이 있기 때문에 `renderHook`이라고 하는 심플한 API가
`@testing-library/react`에 구현되었다.

- [feat: Add `renderHook` by eps1lon · Pull Request #991 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/pull/991)

그렇기 때문에, 앞으로 `@testing-library/react-hooks`은 권장되지 않을 예정이다.

- https://github.com/testing-library/react-hooks-testing-library#a-note-about-react-18-support

---

[Building a dialog component](https://web.dev/building-a-dialog-component/)라는 기사에서는`<dialog>`요소를 사용한 다이얼로그 컴포넌트 작성에 대해 쓰여있다.

`inert`속성、`autofocus`속성、CSS의 `overscroll-behavior`프로퍼티 등、 관련있는 접근성 기능 등에 대해 쓰여 있으므로, 흥미 있는 분은 참고 바람.

---

<h1 class="site-genre">헤드라인</h1>

---

## Release 3.22.0 - 2022.04.15 · zloirock/core-js

[github.com/zloirock/core-js/releases/tag/v3.22.0](https://github.com/zloirock/core-js/releases/tag/v3.22.0 "Release 3.22.0 - 2022.04.15 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.22.0 릴리스.
Change Array by copy proposal의 사양에 따라、`atob`/`btoa`의 수정、compat data의 갱신 등

---

## Release v1.4.0 · remix-run/remix

[github.com/remix-run/remix/releases/tag/v1.4.0](https://github.com/remix-run/remix/releases/tag/v1.4.0 "Release v1.4.0 · remix-run/remix")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Remix</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Remix v1.4.0 릴리스.
`remix`라 하는 단독 패키지를 참조하는 "magic imports"라고 하는 방식을 위해`node_modules`를 직접 편집했지만 pnpm 등 움직이지 않는 문제가 있었다.
따라서, 각각의 패키지를 참조할 수 있도록 하기 위해 마이그레이션 스크립트의 공개 등 이에 관한 변경을 포함하고 있다.

---

## Release v8.0.0 · reduxjs/react-redux

[github.com/reduxjs/react-redux/releases/tag/v8.0.0](https://github.com/reduxjs/react-redux/releases/tag/v8.0.0 "Release v8.0.0 · reduxjs/react-redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React-Redux v8.0.0 릴리스.
코드베이스를 TypeScript로 변환하여、API의 호환성을 유지한다.
`useSyncExternalStore`를 사용한 React 18 대응、TypeScript 타입 정의 부터 `DefaultRootState`의 삭제、`connectAdvanced` 삭제 등

---

## util: add parseArgs module by bcoe · Pull Request #42675 · nodejs/node

[github.com/nodejs/node/pull/42675](https://github.com/nodejs/node/pull/42675 "util: add parseArgs module by bcoe · Pull Request #42675 · nodejs/node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proposal</span> <span class="jser-tag">issue</span></p>

Node.js의 커맨드라인 인수를 전달하는`util.parseArgs`을 추가하는 Proposal

- [pkgjs/parseargs: Polyfill of future proposal for \`util.parseArgs()\`](https://github.com/pkgjs/parseargs "pkgjs/parseargs: Polyfill of future proposal for `util.parseArgs()`")

---

## Release v13.1.0 · testing-library/react-testing-library

[github.com/testing-library/react-testing-library/releases/tag/v13.1.0](https://github.com/testing-library/react-testing-library/releases/tag/v13.1.0 "Release v13.1.0 · testing-library/react-testing-library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

react-testing-library 13.1.0 릴리스.
React 18의 Hooks를 테스트하기 위한 `renderHook` API를 추가.

- [feat: Add \`renderHook\` by eps1lon · Pull Request #991 · testing-library/react-testing-library](https://github.com/testing-library/react-testing-library/pull/991 "feat: Add `renderHook` by eps1lon · Pull Request #991 · testing-library/react-testing-library")
- [testing-library/react-hooks-testing-library: 🐏 Simple and complete React hooks testing utilities that encourage good testing practices.](https://github.com/testing-library/react-hooks-testing-library#a-note-about-react-18-support "testing-library/react-hooks-testing-library: 🐏 Simple and complete React hooks testing utilities that encourage good testing practices.")

---

## Release 2.0.0-beta.1 · vercel/swr

[github.com/vercel/swr/releases/tag/2.0.0-beta.1](https://github.com/vercel/swr/releases/tag/2.0.0-beta.1 "Release 2.0.0-beta.1 · vercel/swr")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-beta.1 릴리스.
`useSWR`이`isLoading`을 반환하도록、`keepPreviousData`옵션 추가 등

---

<h1 class="site-genre">아티클</h1>

---

## New React 18 features and changes - Xebia

[xebia.com/new-react-18-features-and-changes/](https://xebia.com/new-react-18-features-and-changes/ "New React 18 features and changes - Xebia")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18의 변경점에 관한 해설.
Concurrent renderer、createRoot/hydrateRoot과 onRecoverableError에 관해서.
Automatic batching과 flushSync。
새롭게 추가한 Hooks API인 useTransition/useDeferredValue、useId、useSyncExternalStore、useInsertionEffect에 관해서

---

## 왜 우리는 session.cookie를 변경해야만 했을까 - BASE 프로덕트 팀 블로그

[devblog.thebase.in/entry/2022/04/13/114714](https://devblog.thebase.in/entry/2022/04/13/114714 "なぜ我々はsession.cookieを変更しなければならなかったのか - BASEプロダクトチームブログ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">privacy</span> <span class="jser-tag">article</span></p>

Public Suffix List의 추가 신청 등、 브라우저에 번들되는 타이밍
브라우저 복원후 기능에 관해, 변경 전과 변경 후 같은 이름의 Cookie가 존재하는 문제와 브라우저째 동작이 다른 점에 관하여.

---

## Building a dialog component

[web.dev/building-a-dialog-component/](https://web.dev/building-a-dialog-component/ "Building a dialog component")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">accessibility</span></p>

`<dialog>`요소를 사용한 다이얼로그의 작성과 접근성에 관한 기사.
다이얼로그 표시와 유자 입력을 무시하는 `inert`속성、`autofocus`속성、ESC 키로 비표시.
`<dialog>`요소의 스타일, Header/Footer의 디자인,`overscroll-behavior`에서의 body scroll lock、JavaScript과의 연동 방법에 관하여

---

## Boost Resource Loading With fetchpriority, a New Priority Hint — Smashing Magazine

[www.smashingmagazine.com/2022/04/boost-resource-loading-new-priority-hint-fetchpriority/](https://www.smashingmagazine.com/2022/04/boost-resource-loading-new-priority-hint-fetchpriority/ "Boost Resource Loading With fetchpriority, a New Priority Hint — Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">performance</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

리소스 로드의 우선도를 정의하는 `fetchpriority` 속성에 관해.

- [WICG/priority-hints: A browser API to enable developers signal the priorities of the resources they need to download.](https://github.com/WICG/priority-hints "WICG/priority-hints: A browser API to enable developers signal the priorities of the resources they need to download.")
- [HTMLIFrameElement.fetchpriority - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/fetchpriority "HTMLIFrameElement.fetchpriority - Web APIs | MDN")

---

## Turborepo로 보는 Monorepo 도구의 작업 배열 능력 · Issue #13 · worldzhao/blog

[github.com/worldzhao/blog/issues/13](https://github.com/worldzhao/blog/issues/13 "从 Turborepo 看 Monorepo 工具的任务编排能力 · Issue #13 · worldzhao/blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

monorepo에 관한 의존관계의 관리, 태스크 스케쥴링, 버전 관리에 관해.
태스크의 병렬 실행, 토폴로지컬 소스, Turborepo와 Rush의 어프로치, 리모트 캐시에 관한 설명.

---

<h1 class="site-genre">사이트, 서비스, 문서</h1>

---

## facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.

[github.com/facebook/lexical](https://github.com/facebook/lexical "facebook/lexical: Lexical is an extensible text editor framework that provides excellent reliability, accessibility and performance.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

텍스트 에디터를 작성하기 위한 JavaScript 프레임워크.
에디터의 상태를 double-buffering로 관리한다.
상태의 변경을 diff/patch로 표시해 반영한다.
또한 contentEditable를 사용하고 있지만, 외부에서의 변경을 MutationObserver로 감시하여, 에디터의 상태를 갱신한다.

---

<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

---

## ThomasAribart/json-schema-to-ts: Infer TS types from JSON schemas 📝

[github.com/ThomasAribart/json-schema-to-ts](https://github.com/ThomasAribart/json-schema-to-ts "ThomasAribart/json-schema-to-ts: Infer TS types from JSON schemas 📝")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

JSON Schema에서 TypeScript 타입으로 변경하는 라이브러리

---

## Shopify/javy: JS to WebAssembly toolchain

[github.com/Shopify/javy](https://github.com/Shopify/javy "Shopify/javy: JS to WebAssembly toolchain")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">Tools</span></p>

JavaScript의 코드를 실행하는 WebAssembly.
JavaScript 엔진에서는 QuickJS를 이용한다.
Shopify에서 사용된다.

---

## ehmicky/wild-wild-path: 🤠 Object property paths with wildcards and regexps 🌵

[github.com/ehmicky/wild-wild-path](https://github.com/ehmicky/wild-wild-path "ehmicky/wild-wild-path: 🤠 Object property paths with wildcards and regexps 🌵")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`*`와 정규표현식으로 매치한 오브젝트 프로퍼티 취득과 설정이 가능한 라이브러리

---
