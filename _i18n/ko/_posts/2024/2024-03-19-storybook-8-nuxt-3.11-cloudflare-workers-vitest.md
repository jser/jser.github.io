---
title: "2024-03-19: Storybook 8, Nuxt 3.11, Cloudflare Workers + Vitest"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-03-19T03:24:43.652Z
category: JSer
tags:
- React
- test
- CSS
- vite
- Tools

---

JSer.info #685 - Storybook 8.0가 출시되었어요.

- [Storybook 8](https://storybook.js.org/blog/storybook-8/)
- [Storybook: UI component explorer for frontend developers](https://storybook.js.org/releases/8.0)

파괴적 변경으로 `storiesOf` API 삭제, `*.stories.mdx` 삭제, StoryShots addon 삭제, Yarn v1 지원 종료가 있어요.
상세한 이행 가이드는 참조해주세요.

- [Migration guide for Storybook 8.0 • Storybook docs](https://storybook.js.org/docs/migration-guide?ref=storybookblog.ghost.io)

추가 기능으로, Chromatic와 연계 기능 구현, MSW 사용한 React Server Component(RSC) 지원.
그 외로는, SWC 사용함에 따라 빌드 성능 개선, `react-docgen`가 기본값이 되도록 변경, `react`를 peerDependencies에서 제외 변경이 있어요.

---

Nuxt 3.11가 출시되었어요.

- [Nuxt 3.11 · Nuxt Blog](https://nuxt.com/blog/v3-11)

로그 표시 개선, `usePreviewMode` 추가, `appMiddleware` 추가가 있었어요.
또한, 서버 전용 `.server.vue`와 클라이언트 전용 `.client.vue` 파일명 정의 지원이 있어요.

----

다음 글에서는, Vitest 사용한 Cloudflare Workers 테스트에 대해 소개해요.

- [Improved Cloudflare Workers testing via Vitest and workerd](https://blog.cloudflare.com/workers-vitest-integration/)
- [Vitest integration · Cloudflare Workers docs](https://developers.cloudflare.com/workers/testing/vitest-integration/)

Vitest는 테스트 분리한 Worker에서 실행 가능합니다만, [Custom Pool](https://vitest.dev/advanced/pool.html) 사용하면 테스트 실행 환경을 독자적 정의가 가능해졌어요.
[@cloudflare/vitest-pool-workers](https://www.npmjs.com/package/@cloudflare/vitest-pool-workers)에는, Miniflare에서 테스트 코드 실행 가능한 Custom Pool이 구현되었어요.
이에 따라, 로컬에서도 Cloudflre Workers 테스트가 가능해졌으므로 이를 소개하고 있어요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 5.11.0 · prisma/prisma
[github.com/prisma/prisma/releases/tag/5.11.0](https://github.com/prisma/prisma/releases/tag/5.11.0 "Release 5.11.0 · prisma/prisma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">prisma</span> <span class="jser-tag">ReleaseNote</span></p>

Prisma 5.11.0 출시.
Cloudflare Workers(Vercel Edge)에서 Edge function 프리뷰 지원.

- [Prisma ORM support for Edge functions is now in Preview](https://www.prisma.io/blog/prisma-orm-support-for-edge-functions-is-now-in-preview "Prisma ORM support for Edge functions is now in Preview")

----

## Storybook 8
[storybook.js.org/blog/storybook-8/](https://storybook.js.org/blog/storybook-8/ "Storybook 8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Design</span> <span class="jser-tag">debug</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 8 출시.
파괴적 변경으로, `storiesOf` API 삭제, `*.stories.mdx` 삭제, StoryShots addon 삭제, Yarn v1 지원 종료.
추가 기능으로, Chromatic와 연계 기능 구현, MSW 사용한 React Server Component(RSC) 지원.
그 외로는, SWC 사용한 빌드 성능 개선, `react-docgen`가 기본값으로 변경 변경, `react`를 peerDependencies에서 제외

- [Storybook: UI component explorer for frontend developers](https://storybook.js.org/releases/8.0 "Storybook: UI component explorer for frontend developers")
- [storybook/MIGRATION.md at next · storybookjs/storybook](https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#from-version-7x-to-800 "storybook/MIGRATION.md at next · storybookjs/storybook")

----

## Bun v1.0.31 | Bun Blog
[bun.sh/blog/bun-v1.0.31](https://bun.sh/blog/bun-v1.0.31 "Bun v1.0.31 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.31 출시.
`bun --print` 추가, Stdin에서 코드 실행 가능하도록, `bun add --trust <pkg>` 추가, `bun pm trust`/`bun pm untrusted` 추가.
`fetch()`에 `unix` 옵션 추가해 Unix Sockets 지원.
Node.js 21.7.0에 추가된 `util.styleText` 지원

- [Node.js — Node v21.7.0 (Current)](https://nodejs.org/en/blog/release/v21.7.0 "Node.js — Node v21.7.0 (Current)")

----

## Nuxt 3.11 · Nuxt Blog
[nuxt.com/blog/v3-11](https://nuxt.com/blog/v3-11 "Nuxt 3.11 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.11 출시.
로그 표시 개선, `usePreviewMode` 추가, `appMiddleware` 추가.
서버 전용 `.server.vue`, 클라이언트 전용 `.client.vue` 지원


----

## Elysia 1.0 - Lament of the Fallen | ElysiaJS
[elysiajs.com/blog/elysia-10](https://elysiajs.com/blog/elysia-10 "Elysia 1.0 - Lament of the Fallen | ElysiaJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">server</span> <span class="jser-tag">ReleaseNote</span></p>

Bun 대상 HTTP 서버 프레임워크 Elysia 1.0 출시.
기동 시간 개선, Type Check 성능 개선, `onBeforeHandle`같은 곳에서 `as` 옵션 추가


----
<h1 class="site-genre">읽을거리</h1>

----

## Server Actions 시대에서 form 라이브러리 conform
[zenn.dev/akfm/articles/server-actions-with-conform](https://zenn.dev/akfm/articles/server-actions-with-conform "Server Actions 시대에서 form 라이브러리 conform")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Server Actions 대응한 폼 라이브러리 Conform에 관련하여

- [Conform / Overview](https://conform.guide/ "Conform / Overview")

----

## Improved Cloudflare Workers testing via Vitest and workerd
[blog.cloudflare.com/workers-vitest-integration/](https://blog.cloudflare.com/workers-vitest-integration/ "Improved Cloudflare Workers testing via Vitest and workerd")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">vite</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Vitest에서 Cloudflare Workers 테스트하는 방법에 대하여.
`@cloudflare/vitest-pool-workers` 사용함에 따라, Worker에 Unit Test를 가능하게 하는 구조에 대해.
Vitest Custom Pool 사용함에 따라, 테스트를 workerd 프로세스 내에서 실행.

- [Vitest integration · Cloudflare Workers docs](https://developers.cloudflare.com/workers/testing/vitest-integration/ "Vitest integration · Cloudflare Workers docs")

----

## Best Practices for Writing Tests with React Testing Library | ClarityDev blog
[claritydev.net/blog/improving-react-testing-library-tests](https://claritydev.net/blog/improving-react-testing-library-tests "Best Practices for Writing Tests with React Testing Library | ClarityDev blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

React Testing Library에서 React 컴포넌트 테스트에 대하여.
컴포넌트를 Role로 select하는 방법이나 디버그하는 방법, `userEvent`, "not wrapped in act(...)" 경고에 대해


----

## Implementing Vertical Form Controls | WebKit
[www.webkit.org/blog/15190/implementing-vertical-form-controls/](https://www.webkit.org/blog/15190/implementing-vertical-form-controls/ "Implementing Vertical Form Controls | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">CSS</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

WebKit에서 CSS `writing-mode`로 세로쓰기 폼 지원.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 에디터 있는 React 개발 환경을 브라우저만으로 구현한 이야기 - Speaker Deck
[speakerdeck.com/steelydylan/edeitafu-kinoreactkai-fa-huan-jing-wo-burauzadakedeshi-zhuang-sitahua](https://speakerdeck.com/steelydylan/edeitafu-kinoreactkai-fa-huan-jing-wo-burauzadakedeshi-zhuang-sitahua "에디터 있는 React 개발 환경을 브라우저만으로 구현한 이야기 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">slide</span></p>

프리뷰 기능이 있는 에디터 구현에 대한 슬라이드.
에디터 상에서 무거운 처리를 Web Worker 상으로 보내는 방법, Service Worker내에 TypeScript 트랜스파일 구현 등


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## ECSS — Simple Rules for efficient CSS
[ecss.info/en/](https://ecss.info/en/ "ECSS — Simple Rules for efficient CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

예측 가능한 CSS 작성하기 위한 디자인 가이드 라인과 stylelint 규칙


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## guidepup/virtual-screen-reader: Virtual Screen Reader is a screen reader simulator for unit tests.
[github.com/guidepup/virtual-screen-reader](https://github.com/guidepup/virtual-screen-reader "guidepup/virtual-screen-reader: Virtual Screen Reader is a screen reader simulator for unit tests.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

Unit Test 이용 가능한 스크린 리더 시뮬레이터 라이브러리

- [Simple setup: Virtual Screen Reader in Storybook - DEV Community](https://dev.to/scottnath/simple-setup-virtual-screen-reader-in-storybook-2efo "Simple setup: Virtual Screen Reader in Storybook - DEV Community")

----

## MistCSS
[typicode.github.io/mistcss/](https://typicode.github.io/mistcss/ "MistCSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

CSS에서 React 컴포넌트 작성하는 도구.
CSS 작성해서, 그 CSS에서 Rect 컴포넌트 생성하는 구조.
data 속성을 Props로 다루고, `@scope`로 스코프 다룸

----

## devongovett/unplugin-parcel-macros
[github.com/devongovett/unplugin-parcel-macros](https://github.com/devongovett/unplugin-parcel-macros "devongovett/unplugin-parcel-macros")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">parcel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">webpack</span> <span class="jser-tag">rollup</span> <span class="jser-tag">vite</span> <span class="jser-tag">esbuild</span></p>

Parcel의 macro 같은 것을 webpack/rollup/Vite/esbuild에서 이용 가능하게끔 하는 플러그인.
import attributes 구문 사용해 빌드할 때 macro 같은 처리하는 구조
