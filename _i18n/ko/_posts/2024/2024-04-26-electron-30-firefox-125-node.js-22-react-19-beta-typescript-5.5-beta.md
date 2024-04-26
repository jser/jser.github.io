---
title: "2024-04-26: Electron 30, Firefox 125, Node.js 22, React 19 Beta, TypeScript 5.5 Beta"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-04-26T02:31:56.430Z
category: JSer
tags:
- React
- Electron
- Firefox
- JSON
- Tools

---

JSer.info #690 - Electron 30.0.0가 출시되어요.

- [Electron 30.0.0 | Electron](https://www.electronjs.org/blog/electron-30-0)

V8 12.4, Chromium 124, Node.js 20.11.1으로 업데이트.
File System API 지원, Cross Origin iframe에 Permission Policy 사용하도록 변경, `WebContentsView`/`BaseWindow` 폐기도 있어요.

---

Firefox 125가 출시되어요.

- [Firefox 125.0.1, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/125.0.1/releasenotes/)
- [Firefox 125 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/125)

`Intl.Segmenter` 지원, Popover API 지원, AV1 코덱 지원, Wasm의 Multi Memory 지원이 추가되어요.

---

Node.js 22가 출시되어요.

- [Node.js — Node.js 22 is now available!](https://nodejs.org/en/blog/announcements/v22-release-announce)

Node.js 22.x은 2024-10-29에 [LTS](https://github.com/nodejs/release#release-schedule)이 될 예정이 있는 메이저 버전이에요.

V8 12.4으로 업데이트, `require()`에서 ESM 모듈 로드 지원하는 `--experimental-require-module` 플래그 추가가 있어요.
또한 npm run-script 실행하는 `node --run <script>` 추가, `node --watch` 플래그 추가, WebSocket 기본적으로 유효, `node:fs`에 `glob` 추가가 있어요.
그 외로는, Stream의 High Water Mark 기본값을 16KiB에서 64KiB로 변경했어요.

---

React 19 Beta가 출시되어요.

- [React 19 Beta – React](https://react.dev/blog/2024/04/25/react-19)

Action 개념 도입과 `useActionState`/`useFormStatus` 추가가 있어요.
낙관적 갱신을 다루는 `useOptimistic`, Promise를 unwrap하는 `use` 추가되어요.
Server Component/Server Action 지원, `forwardRef`가 필요하지 않도록 변경되어요.

---

TypeScript 5.5 Beta가 출시되어요.

- [Announcing TypeScript 5.5 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/)

함수에서 type predicates 추론이 가능해져, `Array.prototype.filter` 필터링을 간결하게 쓸 수 있어요.

- [The Making of a TypeScript Feature: Inferring Type Predicates](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/)

JSDoc에서 `@import {foo} from "foo"` 지원, 정규표현 기본적 구문 체크 지원, `isolatedDeclarations` 지원이 추가되어요.
또한, `out`이나 `target: ES3` 등 비권장이 된 옵션 무효화되어, `ignoreDeprecations` 옵션 지정하지 않으면 이용할 수 없어요.



----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Electron 30.0.0 | Electron
[www.electronjs.org/blog/electron-30-0](https://www.electronjs.org/blog/electron-30-0 "Electron 30.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 30 출시.
V8 12.4, Chromium 124, Node.js 20.11.1으로 업데이트.
File System API 지원, Cross Origin iframe에 Permission Policy 사용하도록 변경, `WebContentsView`/`BaseWindow` 폐기


----

## Firefox 125.0.1, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/125.0.1/releasenotes/](https://www.mozilla.org/en-US/firefox/125.0.1/releasenotes/ "Firefox 125.0.1, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 125 출시.
`Intl.Segmenter` 지원, Popover API 지원, AV1コーデック 지원, Wasm의 Multi Memory 지원

- [Firefox 125 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/125 "Firefox 125 for developers - Mozilla | MDN")
- [WebAssembly/multi-memory: Multiple per-module memories for Wasm](https://github.com/WebAssembly/multi-memory "WebAssembly/multi-memory: Multiple per-module memories for Wasm")

----

## Node.js — Node.js 22 is now available!
[nodejs.org/en/blog/announcements/v22-release-announce](https://nodejs.org/en/blog/announcements/v22-release-announce "Node.js — Node.js 22 is now available!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 22 출시.
V8 12.4으로 업데이트, `require()`에서 ESM 모듈 로드 지원하는 `--experimental-require-module` 플래그 추가.
npm run-script 실행하는 `node --run <script>` 추가, `node --watch` 플래그 추가, WebSocket 기본적으로 유효, `node:fs`에 `glob` 추가.
Stream의 High Water Mark 기본값을 16KiB에서 64KiB로 변경.


----

## React Native 0.74 - Yoga 3.0, Bridgeless New Architecture, and more · React Native
[reactnative.dev/blog/2024/04/22/release-0.74](https://reactnative.dev/blog/2024/04/22/release-0.74 "React Native 0.74 - Yoga 3.0, Bridgeless New Architecture, and more · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.74 출시.
레이아웃 엔진 Yoga 3.0로 업그레이드, Bridgeless가 기본값으로 변경, `onLayout`에서 State 갱신 배치화되도록.
Android의 최소 SDK 버전 (Android 6.0)으로 변경, PropTypes 삭제


----

## React 19 Beta – React
[react.dev/blog/2024/04/25/react-19](https://react.dev/blog/2024/04/25/react-19 "React 19 Beta – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 19 Beta 출시.
Action 개념 도입 및 `useActionState`/`useFormStatus` 추가.
낙관적 갱신을 다루는 `useOptimistic`, Promise를 unwrap하는 `use` 추가.
Server Component/Server Action 지원, `forwardRef`가 필요하지 않게 변경.
Hydration 에러 표시 개선, `<Context>` 자체가 `<Context.Provider>`으로 기능을 갖도록 변경, `ref`의 cleanup 처리 정의 가능함.
`useDeferredValue`의 제2인수 초기화 지원, `<title>` 같은 메타 태그 지원, `<link ref=stylesheet>`에서 스타일시트 지원.
`<script async={true}>` 지원, `preload` 등에서 `<link rel=preload>` 다루는 함수 추가.
 React 18에서는 서드파티에 의해 HTML이 수정되면 Hydration 시 다시 렌더링하여 사라지던 것을 남아있도록 변경, Custom Element 지원 등으로 변경.


----

## Release Version 2.0.0 · quilljs/quill
[github.com/quilljs/quill/releases/tag/v2.0.0](https://github.com/quilljs/quill/releases/tag/v2.0.0 "Release Version 2.0.0 · quilljs/quill")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Quill 2.0 출시.
TypeScript 빌트인 지원, `registry` 추가, 도큐멘트 모델과 동기적으로 InputEvent 사용하도록 변경.

- [Announcing Quill 2.0 - Knock Down Silos by Slab](https://slab.com/blog/announcing-quill-2-0/ "Announcing Quill 2.0 - Knock Down Silos by Slab")

----

## What’s new in Apollo Client 3.10 | Apollo GraphQL Blog
[www.apollographql.com/blog/whats-new-in-apollo-client-3-10](https://www.apollographql.com/blog/whats-new-in-apollo-client-3-10 "What’s new in Apollo Client 3.10 | Apollo GraphQL Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Apollo Client 3.10 출시.
`@apollo/client/testing/experimental`에 MSW 연계해서 스키마 주도 테스트 하는 `createTestSchema` 추가, `client.watchFragment` 추가.
`createQueryPreloader`를 Stable으로 변경

- [Release v3.10.0 · apollographql/apollo-client](https://github.com/apollographql/apollo-client/releases/tag/v3.10.0 "Release v3.10.0 · apollographql/apollo-client")

----

## Announcing TypeScript 5.5 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5-beta/ "Announcing TypeScript 5.5 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.5 출시.
함수에서 type predicates 추론 가능하도록, `Array.prototype.filter` 등에서 필터링 간결하게 작성 가능.
JSDoc에서 `@import {foo} from "foo"` 지원, 정규표현 기본적 구문 체크 지원, `isolatedDeclarations` 지원.
설정 파일 내에 `${configDir}` 템플릿 값 지원.
`typescript` 패키지 크기 절감, Named Import 지원, `transpileDeclaration` API 추가.
`out`이나 `target: ES3` 같이 비권장 옵션 무효화, `ignoreDeprecations` 옵션 지정하지 않으면 사용할 수 없도록 변경

- [The Making of a TypeScript Feature: Inferring Type Predicates](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/ "The Making of a TypeScript Feature: Inferring Type Predicates")

----
<h1 class="site-genre">읽을거리</h1>

----

## Rspack v1.0 Release Plan · web-infra-dev/rspack · Discussion #6315
[github.com/web-infra-dev/rspack/discussions/6315](https://github.com/web-infra-dev/rspack/discussions/6315 "Rspack v1.0 Release Plan · web-infra-dev/rspack · Discussion #6315")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

Rspack 로드맵.
2024년 7월 Rspack 1.0 출시 예정


----

## HTML attributes vs DOM properties - JakeArchibald.com
[jakearchibald.com/2024/attributes-vs-properties/](https://jakearchibald.com/2024/attributes-vs-properties/ "HTML attributes vs DOM properties - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

HTML 속성과 DOM 프로퍼티 차이에 대하여.
속성과 프로퍼티 타입 차이, 대소문자 구별, Reflection에 대하여.
Preact/Vue이나 React 같은 UI 프레임워크에서의 취급 등


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## LavaMoat/LavaDome: Secure DOM trees isolation and encapsulation leveraging ShadowDOM
[github.com/LavaMoat/LavaDome](https://github.com/LavaMoat/LavaDome "LavaMoat/LavaDome: Secure DOM trees isolation and encapsulation leveraging ShadowDOM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

Shadow DOM 사용해 같은 Origin에서 실행되고 있는 JavaScript에서 접근 할 수 없는 DOM 다루는 라이브러리


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## React의 규칙 – React
[ja.react.dev/reference/rules](https://ja.react.dev/reference/rules "React의 규칙 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">docue</span> <span class="jser-tag">translate</span></p>

Rules of React 일본어 번역.
React 애플리케이션을 작성할 때 규칙에 대해 언급되어있음

- [Rules of React – React](https://react.dev/reference/rules "Rules of React – React")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## JSON Fixer
[jsonfixer.com/](https://jsonfixer.com/ "JSON Fixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">Tools</span></p>

JSON스러운 것을 JSON으로 수정해주는 도구


----
