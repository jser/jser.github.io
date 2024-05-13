---
title: "2024-05-12: Headless UI v2.0 for React, Astro v4.8, 외부패키지 의존 없이 Node.js만으로 이용할 수 있는 기능"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-05-12T06:47:28.714Z
category: JSer
tags:
- test
- nodejs
- bundler
- vite
- Hono

---

JSer.info #692 - Headless UI v2.0 for React가 출시되었어요.

- [Headless UI v2.0 for React - Tailwind CSS](https://tailwindcss.com/blog/headless-ui-v2)

Floating UI에서 anchor 지정 지원, Checkbox 컴포넌트, Fieldset 컴포넌트, Combobox가 `virtual` props 지원 변경이 포함되어요.

---

Astro 4.8가 출시되었어요.

- [Astro 4.8 | Astro](https://astro.build/blog/astro-480/)

실험적 기능으로 Astro Actions, Request Rewriting 추가가 있어요.
또한, 성능 개선과 `injectRoute` 버그 수정 변경도 있어요.

---

[Node.js 진화로 인해 필요없어질지도 모를 패키지들](https://zenn.dev/morinokami/articles/npm-uninstall)에서는, 외부 패키지로 이용했던 기능 일부가 Node.js에도 구현되어 있음을 소개하고 있어요.

- Fetch API
- `.env` 파일 읽기
- `util.styleText`
- `node:test`
- `--watch` 플래그
- `glob`
- `util.parseArgs`

등이 있어요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v0.21.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.21.0](https://github.com/evanw/esbuild/releases/tag/v0.21.0 "Release v0.21.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.21.0 출시.
Stage 3의 Decorator Proposal 지원, private 메서드 최적화, 버그 수정


----

## Release v1.6.0 · vitest-dev/vitest
[github.com/vitest-dev/vitest/releases/tag/v1.6.0](https://github.com/vitest-dev/vitest/releases/tag/v1.6.0 "Release v1.6.0 · vitest-dev/vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

vitest v1.6.0 출시.
`--standalone` 그래프 지원, Snapshot 커스터마이즈 가능한 `snapshotEnvironment` 옵션 추가.
`browser.testerScripts`와 `browser.indexScripts` 옵션 추가.


----

## Release v4.3.0 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.3.0](https://github.com/honojs/hono/releases/tag/v4.3.0 "Release v4.3.0 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">ReleaseNote</span></p>

Hono v4.3.0 출시.
Response 관련해 클라이언트 측에서 자료형 추론 개선, `hono/jsx`에서 React와의 호환성 개선, `createFactory` 추가


----

## Astro 4.8 | Astro
[astro.build/blog/astro-480/](https://astro.build/blog/astro-480/ "Astro 4.8 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 4.8 출시.
실험적 기능으로 Astro Action, Request Rewriting 추가.
성능 개선 및 `injectRoute` 버그 수정


----

## Node.js — Node v20.13.0 (LTS)
[nodejs.org/en/blog/release/v20.13.0](https://nodejs.org/en/blog/release/v20.13.0 "Node.js — Node v20.13.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.13.0 출시.
Buffer에서 `base64`와 `base64url` 성능 개선, `CustomEvent`와 `node --watch`를 Stable로 변경, `fs/promises` 스택 트레이스 추가


----

## Release v1.44.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.44.0](https://github.com/microsoft/playwright/releases/tag/v1.44.0 "Release v1.44.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.44.0 출시.
accessibility용 Assertion 추가, `page.addLocatorHandler`에 `noWaitAfter` 옵션 추가, `page.removeLocatorHandler` 메서드 추가.
직전에 실패한 테스트한 실행하는 `--last-failed` 플래그 추가


----

## Release v2.3.0 · mswjs/msw
[github.com/mswjs/msw/releases/tag/v2.3.0](https://github.com/mswjs/msw/releases/tag/v2.3.0 "Release v2.3.0 · mswjs/msw")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

msw 2.3.0 출시.
핸들러 내에 unhandled exception는 500 에러가 되도록 변경, `unhandledException` 이벤트 추가


----

## Release v9.0.0 · sindresorhus/execa
[github.com/sindresorhus/execa/releases/tag/v9.0.0](https://github.com/sindresorhus/execa/releases/tag/v9.0.0 "Release v9.0.0 · sindresorhus/execa")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

execa v9.0.0 출시.
zx처럼 Template Literal에서 커맨드 실행 지원, 행마다 출력 처리 가능하게끔, 입력이나 출력 필터, `verbose` 모드 개선

- [Execa 9: our biggest release. Execa runs commands in your scripts. | by ehmicky | Medium](https://medium.com/@ehmicky/execa-9-release-d0d5daaa097f "Execa 9: our biggest release. Execa runs commands in your scripts. | by ehmicky | Medium")

----

## Bun v1.1.8 | Bun Blog
[bun.sh/blog/bun-v1.1.8](https://bun.sh/blog/bun-v1.1.8 "Bun v1.1.8 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.8 출시.
`process.on("uncaughtException")`와 `process.on("unhandledRejection")` 지원.
`node:zlib`에서 Brotli API 지원, Bun APIがExplicit Resource Management 지원


----

## Headless UI v2.0 for React - Tailwind CSS
[tailwindcss.com/blog/headless-ui-v2](https://tailwindcss.com/blog/headless-ui-v2 "Headless UI v2.0 for React - Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Headless UI v2.0 출시.
Floating UI에서 anchor 지정 지원, Checkbox 컴포넌트, Fieldset 컴포넌트, Combobox가 `virtual` props 지원


----

## Release 7.0.0 · jasonkuhrt/graphql-request
[github.com/jasonkuhrt/graphql-request/releases/tag/7.0.0](https://github.com/jasonkuhrt/graphql-request/releases/tag/7.0.0 "Release 7.0.0 · jasonkuhrt/graphql-request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

graphql-request 7.0 출시.
cross-fetch에서 polyfill 삭제, Pure ESM으로 변경


----
<h1 class="site-genre">アーティクル</h1>

----

## Node.js 진화로 인해 필요없어질지도 모르는 패키지들
[zenn.dev/morinokami/articles/npm-uninstall](https://zenn.dev/morinokami/articles/npm-uninstall "Node.js 진화로 인해 필요없어질지도 모르는 패키지들")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js 코어 모듈에 구현 된 패키지 기능 소개.
Fetch API, `.env` 로드, `util.styleText`, `node:test`, `--watch` 플래그, `glob`, `util.parseArgs` 관련


----

## TypeScript 타입 검사 시간 단축한 이야기
[zenn.dev/knowledgework/articles/speedup-typecheck](https://zenn.dev/knowledgework/articles/speedup-typecheck "TypeScript 타입 검사 시간 단축한 이야기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 타입 체크 성능 체크와 개선에 대하여


----

## Misconceptions about CSS Specificity – Bram.us
[www.bram.us/2024/05/05/misconceptions-about-css-specificity/](https://www.bram.us/2024/05/05/misconceptions-about-css-specificity/ "Misconceptions about CSS Specificity – Bram.us")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS에서 Specificity 이야기


----

## Monitor Third-Party Resources that Impact UX with Playwright
[www.checklyhq.com/blog/how-playwright-can-monitor-third-party-resources/](https://www.checklyhq.com/blog/how-playwright-can-monitor-third-party-resources/ "Monitor Third-Party Resources that Impact UX with Playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Playwright에서 Request Block/Delay 사용해 유저에게 영향있는 서드파티 스크립트 모니터링하는 방법


----

## Why Patching Globals Is Harmful - kettanaito.com
[kettanaito.com/blog/why-patching-globals-is-harmful](https://kettanaito.com/blog/why-patching-globals-is-harmful "Why Patching Globals Is Harmful - kettanaito.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Fetch</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Global API에 monkey patch하는 폐해에 대하여.
Fetch API 사양을 다양한 방법으로 덮어쓰고 있는 React/Next.js/Bun


----
