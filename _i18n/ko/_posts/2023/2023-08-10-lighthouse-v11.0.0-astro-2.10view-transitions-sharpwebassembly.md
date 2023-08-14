---
title: "2023-08-10: Lighthouse v11.0.0, Astro 2.10(View Transitions), Sharp의 WebAssembly 빌드"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-08-10T13:11:24.885Z
category: JSer
tags:
- Bun
- Tools
- Chrome
- performance
- deno

---

JSer.info #655 - Lighthouse v11.0.0가 출시되었습니다.

- [Release v11.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0)

Node.js 16 지원 종료, 기본적으로 사용되지 않은 `resource-summary`/`service-worker`/`first-contentful-paint-3g`의 Audit이 삭제되었습니다.
또한, [INP](https://web.dev/inp/)의 Audit가 Stable이 되었습니다.

---

Astro 2.10가 출시되었습니다.

- [Astro 2.10: Persistent State in View Transitions | Astro](https://astro.build/blog/astro-2100/)

[Astro 2.9에 실험적 지원한 View Transitions](https://astro.build/blog/astro-290/)에 추가하는 형태로, 지정한 요소를 영속적으로 만드는 `transition:persist` 명령어가 추가되었습니다.

또한, Astro 3.0가 베타 출시되었습니다.

- [astro/packages/astro/CHANGELOG.md at refs/heads/next · withastro/astro](https://github.com/withastro/astro/blob/refs/heads/next/packages/astro/CHANGELOG.md#300-beta0)

----

[Bringing Sharp to WebAssembly and WebContainers](https://blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/)에서는, Native Addon인 이미지 처리 라이브러리 [sharp](https://sharp.pixelplumbing.com/)를 WebAssembly으로 어떻게 빌드했는가 다룹니다.

emnapi를 사용해 Node API 이식, libvips를 Wasm으로 컴파일, 기동할 때 처리를 동기적으로 하기 위해 Emscripten를 어떻게 수정했는가에 대했는지도 다뤄집니다.

다음 Pull Request에 sharp 변경을 확인가능합니다.

- [WebAssembly build by RReverser · Pull Request #3522 · lovell/sharp](https://github.com/lovell/sharp/pull/3522)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Bun v0.7.2 | Bun Blog
[bun.sh/blog/bun-v0.7.2](https://bun.sh/blog/bun-v0.7.2 "Bun v0.7.2 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.7.2 출시.
`node:worker_threads`, `node:diagnostics_channel` 지원.
`BroadcastChannel` API 지원, `Error` 객체를 `structuredClone`에서 clone할 수 있도록 수정.
메모리누수 수정


----

## Release v11.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v11.0.0 "Release v11.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse v11.0.0 출시.
Node.js 16 지원 종료, `resource-summary`/`service-worker`/`first-contentful-paint-3g` Audit 삭제.
INP의 Audit를 Stable으로


----

## Deno 1.36: More flexible security and expanded testing APIs
[deno.com/blog/v1.36](https://deno.com/blog/v1.36 "Deno 1.36: More flexible security and expanded testing APIs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.36 출시.
`--deny-*` 거부 플러그 지원, `deno test`가 JUnit 레포터 지원, `node:test` 지원.
Node.js와 호환성개선, 모듈 다운로드에 재시도 추가


----

## Astro 2.10: Persistent State in View Transitions | Astro
[astro.build/blog/astro-2100/](https://astro.build/blog/astro-2100/ "Astro 2.10: Persistent State in View Transitions | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 2.10 출시.
View Transition API 사용해 지정한 요소를 영속적으로 하는 `transition:persist` 명령어 추가.
또한 Astro 3.0 베타 출시.


----

## Bun v0.7.3 | Bun Blog
[bun.sh/blog/bun-v0.7.3](https://bun.sh/blog/bun-v0.7.3 "Bun v0.7.3 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.7.3 출시.
`bun test --coverage` 지원, `bun test -t /pattern/` 지원.
`bun:sqlite`, `fs` 크래시 수정


----

## 1.0.0: Milestone for API stability · vanjs-org/van · Discussion #72
[github.com/vanjs-org/van/discussions/72](https://github.com/vanjs-org/van/discussions/72 "1.0.0: Milestone for API stability · vanjs-org/van · Discussion #72")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Reactive UI 프레임워크 VanJS 1.0 출시.

- [Release 1.0.0: Milestone for API stability · vanjs-org/van](https://github.com/vanjs-org/van/releases/tag/1.0.0 "Release 1.0.0: Milestone for API stability · vanjs-org/van")

----

## Release v0.19.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.19.0](https://github.com/evanw/esbuild/releases/tag/v0.19.0 "Release v0.19.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.19.0 출시.
엔드포인트에 와일드 카드 지정할 수 있도록, Dynamic Import으로 변수를 포함한 경로를 bundle 할 수 있도록.
`--packages=external`와 `tsconfig.json`의 `paths` 문제 수정, `.module.css` 기본 로더를 `local-css`으로 변경


----

## Wednesday August 9th 2023 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/august-2023-security-releases](https://nodejs.org/en/blog/vulnerability/august-2023-security-releases "Wednesday August 9th 2023 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.js의 Security Releases로 다음 버전이 공개됨.

- Node v20.5.1 (Current)
- Node v18.17.1 (LTS)
- Node v16.20.2 (LTS)

실험적 기능인 Permissions policies 수정과 OpenSSL 업데이트가 주요한 수정


----

## Announcing TypeScript 5.2 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-2-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-rc/ "Announcing TypeScript 5.2 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.2 RC 출시.
Stage 3 Proposal의 Explicit Resource Management(`using` 선언) 지원, Decorator Metadata 지원.
Tuple 라벨 유무에 따른 조합 제한 삭제, 배열 Union 타입 처리 개선.
`import type`에는 `.ts` 파일을 import 할 수 있도록, `module` 옵션과 `moduleResolution` 옵션의 잘못 된 조합 체크 기능 추가


----

## Release Notes for Safari Technology Preview 176 | WebKit
[webkit.org/blog/14401/release-notes-for-safari-technology-preview-176/](https://webkit.org/blog/14401/release-notes-for-safari-technology-preview-176/ "Release Notes for Safari Technology Preview 176 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 176 출시.
CSS의 `contain-intrinsic-size: inherit` 지원, `liner(...)` timing function 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## Bringing Sharp to WebAssembly and WebContainers
[blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/](https://blog.stackblitz.com/posts/bringing-sharp-to-wasm-and-webcontainers/ "Bringing Sharp to WebAssembly and WebContainers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">Image</span> <span class="jser-tag">article</span></p>

C++으로 작성된 Native Addon 이미지처리 라이브러리 sharp를 WebContainers에서 이용가능 하도록 WebAssembly으로 컴파일한 이야기.
emnapi를 사용해 Node API 이식, libvips를 Wasm으로 컴파일, 기동시 처리를 동기적으로 하기 위해 Emscripten를 어떻게 수정했는가에 대하여.


----

## A compilation of outstanding testing articles (with JavaScript) | Practica.js
[practica.dev/blog/a-compilation-of-outstanding-testing-articles-with-javaScript/](https://practica.dev/blog/a-compilation-of-outstanding-testing-articles-with-javaScript/ "A compilation of outstanding testing articles (with JavaScript) | Practica.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

테스트에 관련한 우수한 글/영상를 소개하는 글.


----

## Puppeteer in Node.js: Common Mistakes to Avoid | AppSignal Blog
[blog.appsignal.com/2023/02/08/puppeteer-in-nodejs-common-mistakes-to-avoid.html](https://blog.appsignal.com/2023/02/08/puppeteer-in-nodejs-common-mistakes-to-avoid.html "Puppeteer in Node.js: Common Mistakes to Avoid | AppSignal Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">article</span></p>

Puppeteer에서 자주 있는 시행착오에 대하여


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Vue.js 에코시스템 동향 2023 - Speaker Deck
[speakerdeck.com/kazupon/vue-dot-jsekosisutemudong-xiang-2023](https://speakerdeck.com/kazupon/vue-dot-jsekosisutemudong-xiang-2023 "Vue.js 에코시스템 동향 2023 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">slide</span></p>

Vue 에코 시스템에 대한 슬라이드.
Vue 3.3 개선 내용, Reactivity Transform이 비권장이 된 이유에 대하여.
Vue의 LSP, Nuxt 3와 Nitro에 대하여


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## npmgraph -
[npmgraph.js.org/](https://npmgraph.js.org/ "npmgraph -")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

npm 패키지 의존관계를 가시화하는 Web서비스.
지정한 패키지나 `package.json`에서 분석 가능


----
<h1 class="site-genre">도서</h1>

----

## 실전 Svelte 입문：도서안내｜기술평론사
[gihyo.jp/book/2023/978-4-297-13495-2](https://gihyo.jp/book/2023/978-4-297-13495-2 "실전 Svelte 입문：도서안내｜기술평론사")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">book</span></p>

Svelte 입문서


----
