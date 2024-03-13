---
title: "2024-03-12: Tailwind CSS v4.0 alpha, TypeScript 5.4, Speedometer 3.0"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-03-12T02:18:32.384Z
category: JSer
tags:
- nodejs
- TypeScript
- React
- browser
- game

---

JSer.info #684 - Tailwind CSS v4.0 alpha가 출시됐어요.

- [Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v4-alpha)

Rust로 작성된 Oxide 엔진 추가, Lightning CSS 삽입함으로 성능, 빌트인 지원하는 구문 개선되었어요. 또한 글에서는 v4 로드맵에 대해서도 다루고 있어요.

---

TypeScript 5.4가 출시됐어요.

- [Announcing TypeScript 5.4 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4/)

Beta나 RC에서 큰 기능 추가는 없어요.
클로저에 의한 Narrowing 결과 개선, `NoInfer` Utility Type 추가, 
`--module preserve` 추가가 있었어요.
또한, ES2024 `Object.groupBy`/`Map.groupBy` 지원, Import Attributes 지원이 추가되었어요.
5.4는 `target: "ES3"`나 `out` 옵션 같은 비권장 기능 지원되는 마지막 버전이 될 예정이에요.
이 옵션은 5.5에서 삭제될 예정이에요.

- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909)

---

브라우저 엔진 퍼포먼스 측정하는 벤치마크 도구 [Speedometer 3.0](https://browserbench.org/Speedometer3.0/)가 출시됐어요.

- [Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit](https://webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/)

Speedometer는 주로 브라우저 엔진 개발자가 브라우저 퍼포먼스 측정 벤치마크로 이용하고 있어요.
이번 업데이트에서 동기, 비동기 처리 실행 시간을 보다 더 정확히 측정, HTTP Archive나 npm 다운로드 수 기반으로 이용하고 있는 프레임워크 조절 등이 있어요.
또한, 지금까진 TodoMVC 이용했지만, Next.js/Nuxt 사용한 미디어 사이트나 그래피컬한 대시보드, CodeMirror나 TipTap 사용한 에디터도 테스트에 추가되었어요.

Speedometer 3.0 벤치마크에서는 다음 프레임워크가 테스트에 포함되어 있어요.

- [Angular](https://angular.io/)
- [Backbone](https://backbonejs.org/)
- [jQuery](https://jquery.com/)
- [Lit](https://lit.dev/)
- [Preact](https://preactjs.com/)
- [React](https://reactjs.org/)
- [React+Redux](https://react-redux.js.org/)
- [Svelte](https://svelte.dev/)
- [Vue](https://vuejs.org/)
- [Next.js](https://nextjs.org/)
- [Nuxt](https://nuxt.com/)
- [Observable Plot](https://observablehq.com/@observablehq/plot)
- [chart.js](https://www.chartjs.org/)
- [React stockcharts](https://github.com/rrag/react-stockcharts)
- [D3](https://d3js.org/)
- [CodeMirror](https://codemirror.net/)
- [TipTap](https://www.tiptap.dev/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v8.0.0 · pixijs/pixijs
[github.com/pixijs/pixijs/releases/tag/v8.0.0](https://github.com/pixijs/pixijs/releases/tag/v8.0.0 "Release v8.0.0 · pixijs/pixijs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

PixiJS v8.0.0 출시.
`pixi.js` 하나의 패키지에 통합, 초기화가 비동기로 변경, Graphiscs API 변경

- [v8 Migration Guide | PixiJS](https://pixijs.com/guides/migrations/v8 "v8 Migration Guide | PixiJS")

----

## Node.js — Node v21.7.0 (Current)
[nodejs.org/en/blog/release/v21.7.0](https://nodejs.org/en/blog/release/v21.7.0 "Node.js — Node v21.7.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v21.7.0 출시.
`util.styleText(format, text)` 함수 추가, `process.loadEnvFile(path)`와 `util.parseEnv(content)` 추가.
`.env` 복수행 값 지원, `node:sea`에 API 추가, `node:vm`에 `importModuleDynamically` 옵션 추가, `crypto.hash()` 추가


----

## Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS
[tailwindcss.com/blog/tailwindcss-v4-alpha](https://tailwindcss.com/blog/tailwindcss-v4-alpha "Open-sourcing our progress on Tailwind CSS v4.0 - Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS v4 alpha 출시.
Rust로 작성된 Oxide 엔진 추가, Lightning CSS 사용하도록 변경.
v4 로드맵 언급


----

## WebKit Features in Safari 17.4 | WebKit
[webkit.org/blog/15063/webkit-features-in-safari-17-4/](https://webkit.org/blog/15063/webkit-features-in-safari-17-4/ "WebKit Features in Safari 17.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17.4 변경점에 대해.
HTML, `<input type="checkbox" switch>` 지원, 폼 세로 표시에 대응, `<select>` 구분에 `<hr>` 사용 가능.
CSS, `@scope` 지원, `::spelling-error`와 `::grammar-error` 추상 요소 지원, `content: "foo" / "alt"` 대체 텍스트 지원.
Web API, `element.checkVisibility()` 지원, `AbortSignal.any()` 지원.
JS, ES2024 `Promise.withResolvers()`/`Object.groupBy()`/`Map.groupBy()` 지원.

- [Safari 17.4 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17_4-release-notes "Safari 17.4 Release Notes | Apple Developer Documentation")

----

## Biome v1.6 | Biome
[biomejs.dev/blog/biome-v1-6/](https://biomejs.dev/blog/biome-v1-6/ "Biome v1.6 | Biome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Biome v1.6 출시.
Astro/Svelte/Vue 파일 내 JS/TS 분석 지원, `biome.jsonc` 지원.
`atributePosition` 옵션 추가, 규칙 업데이트


----

## Announcing TypeScript 5.4 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-4/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4/ "Announcing TypeScript 5.4 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.4 출시.
클로저로 인한 Narrowing 결과 개선, `NoInfer` Utility Type 추가,
`--module preserve` 추가.
ES2024 `Object.groupBy`/`Map.groupBy` 지원, Import Attributes 지원.
`target: "ES3"`나 `out` 옵션 같은 비권장되어있는 옵션은 5.5에서 삭제 예정.


----

## WinterJS 1.0 · Blog · Wasmer
[wasmer.io/posts/winterjs-v1](https://wasmer.io/posts/winterjs-v1 "WinterJS 1.0 · Blog · Wasmer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span></p>

Spidermonkey 기반 WinterJS-compatible한 JavaScript Runtime인 WinterJS 1.0 출시.


----

## Release v4.1.0 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.1.0](https://github.com/honojs/hono/releases/tag/v4.1.0 "Release v4.1.0 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Hono v4.1.0 출시.
WebSocket Helper 추가, Body Limit Middleware 추가, 출력 타겟 ES2022으로 변경


----
<h1 class="site-genre">읽을거리</h1>

----

## 풀스크래치로 이해하는 OpenID Connect (1) 인가 엔드포인트 편 - 엠스리테크블로그
[www.m3tech.blog/entry/2024/03/05/150000](https://www.m3tech.blog/entry/2024/03/05/150000 "풀스크래치로 이해하는 OpenID Connect (1) 인가 엔드포인트 편 - 엠스리테크블로그")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">OpenID</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

OpenID Connect의 ID Provider를 TypeScript로 구현하며 연재


----

## &quot;react-strict-dom&quot;, why it&#039;s so great? | Szymon Rybczak
[szymonrybczak.dev/blog/react-strict-dom](https://szymonrybczak.dev/blog/react-strict-dom "\&quot;react-strict-dom\&quot;, why it&#039;s so great? | Szymon Rybczak")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">HTML</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">article</span></p>

react-strict-dom에 대해.
React Native for Web 접근에는 React Native의 primitive를 웹에 맞게 변환하는 호환 Shim이 상당히 큼.
react-strict-dom은 역으로 접근하는 것을 선택해し, DOM API 서브셋를 네이티브 츠겡서 다룸.

- [RFC: React DOM for Native (reduce API fragmentation) by necolas · Pull Request #496 · react-native-community/discussions-and-proposals](https://github.com/react-native-community/discussions-and-proposals/pull/496 "RFC: React DOM for Native (reduce API fragmentation) by necolas · Pull Request #496 · react-native-community/discussions-and-proposals")

----

## Why Should You Care About Package Metadata Interoperability? | OpenJS Foundation
[openjsf.org/blog/package-metadata-interoperability-collab-space-intro](https://openjsf.org/blog/package-metadata-interoperability-collab-space-intro "Why Should You Care About Package Metadata Interoperability? | OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

OpenJS에서 `package.json` 메타데이터 호환 운용성 향상하기 위한 워킹 그룹 발족.

- [openjs-foundation/package-metadata-interoperability-collab-space: The goal of the Package Metadata Interoperability Collab Space is to improve how JavaScript developers define their packages across the ecosystem. The group is currently working to better understand package.json and how developers use it to define their projects.](https://github.com/openjs-foundation/package-metadata-interoperability-collab-space "openjs-foundation/package-metadata-interoperability-collab-space: The goal of the Package Metadata Interoperability Collab Space is to improve how JavaScript developers define their packages across the ecosystem. The group is currently working to better understand package.json and how developers use it to define their projects.")
- [OpenJS Launches New Collaboration to Improve Interoperability of JavaScript Package Metadata  - Socket](https://socket.dev/blog/openjs-improve-interoperability-of-javascript-package-metadata "OpenJS Launches New Collaboration to Improve Interoperability of JavaScript Package Metadata  - Socket")

----

## Ultimate Guide to Visual Testing with Playwright
[www.browsercat.com/post/ultimate-guide-visual-testing-playwright](https://www.browsercat.com/post/ultimate-guide-visual-testing-playwright "Ultimate Guide to Visual Testing with Playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Playwright 사용한 Visual Regression Testing에 대하여


----

## Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit
[webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/](https://webkit.org/blog/15131/speedometer-3-0-the-best-way-yet-to-measure-browser-performance/ "Speedometer 3.0: The Best Way Yet to Measure Browser Performance | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

웹브라우저 엔진 벤치 마크 Speedometer 3.0 출시.
동기와 비동기처리 실행 시간을 보다 더 정확히 측정, HTTP Archive나 npm 다운로드 수 기반으로 이용되고 있는 프레임워크 조절.
또한, 지금까지는 TodoMVC 이용했지만, Next.js/Nuxt 사용한 미디어사이트나 그래피컬한 대시보드, CodeMirror와 TipTap 사용한 에디터도 테스트 가능


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## rolldown-rs/rolldown: Fast Rust bundler for JavaScript with Rollup-compatible API.
[github.com/rolldown-rs/rolldown](https://github.com/rolldown-rs/rolldown "rolldown-rs/rolldown: Fast Rust bundler for JavaScript with Rollup-compatible API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rollup</span> <span class="jser-tag">Rust</span> <span class="jser-tag">vite</span> <span class="jser-tag">library</span></p>

Rollup 호환을 목표로하는 JavaScript Bundler.


----

## edmundhung/conform: A type-safe form validation library utilizing web fundamentals to progressively enhance HTML Forms with full support for server frameworks like Remix and Next.js.
[github.com/edmundhung/conform](https://github.com/edmundhung/conform "edmundhung/conform: A type-safe form validation library utilizing web fundamentals to progressively enhance HTML Forms with full support for server frameworks like Remix and Next.js.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">Remix</span> <span class="jser-tag">library</span></p>

Remix나 Next.js에서 서버 처리 대응한 폼 라이브러리.
Zod 같은 것과 조합함으로 서버측에서 검증이나 React의 `useFormState`와 조합해 동작


----
<h1 class="site-genre">도서</h1>

----

## Eloquent JavaScript
[eloquentjavascript.net/](https://eloquentjavascript.net/ "Eloquent JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Eloquent JavaScrip 4판(2024) 공개


----
