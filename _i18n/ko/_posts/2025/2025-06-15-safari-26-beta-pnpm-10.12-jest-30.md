---
title: "2025-06-15: Safari 26 Beta, pnpm 10.12, Jest 30"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-06-15T11:38:12.338Z
category: JSer
tags:
- test
- Tools
- rspack
- ESLint
- polyfill

---

JSer.info #738 - Safari 26 beta가 출시되었습니다.

- [News from WWDC25: WebKit in Safari 26 beta | WebKit](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/)

이 버전부터 macOS와 같이, 서기 밑의 2자리가 Safari 버전이 됩니다.

CSS는, Anchor Positioning, Scroll-driven Animations, `text-wrap:pretty`, `contrast-color()`, `progress()` 지원됩니다.
Web API는, WebGPU, HDR Images, Digital Credentials API, Trusted Types API, URL Pattern가 새롭게 지원됩니다.
Web Inspector는 Service Worker이나 비동기처리 디버그 개선됩니다.
그 외로는, SVG 파비콘 대응이나 WebAssembly 인터프리터로 쓸 때 실행 속도 개선이 있습니다.

---

pnpm v10.12.1가 출시되었습니다.

- [Release pnpm 10.12.1 · pnpm/pnpm](https://github.com/pnpm/pnpm/releases/tag/v10.12.1)
- [pnpm 10.12 Introduces Global Virtual Store and Expanded Version Catalogs](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs)

실험적 기능으로 `enableGlobalVirtualStore` 옵션에서 글로벌 가상 스토어를 지원하고, 의존 관계 캐시가 있을 때 설치 속도가 빨라집니다. 또한, `pnpm update`가 catalog 지원하고, `catalogMode` 옵션이나 `--save-catalog` 플러그가 추가됩니다.

---

Jest 30가 출시되었습니다.

- [Jest 30: Faster, Leaner, Better · Jest](https://jestjs.io/blog/2025/06/04/jest-30)

Node.js 14/16/19/21 지원 종료, TypeScript 5.4+, jsdom 26으로 업데이트 했습니다.
[unrs-resolver](https://github.com/unrs/unrs-resolver) 사용한 성능과 메모리 개선, 설정 파일에서 TypeScript 지원, `import.meta` 지원, `using` 사용한 spy 자동 복구 추가가 있습니다.
또한, `expect.arrayOf`, `jest.advanceTimersToNextFrame()`, `jest.unstable_unmockModule()` 같은 새로운 API도 추가되었습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Oxlint v1.0 Stable | The JavaScript Oxidation Compiler
[oxc.rs/blog/2025-06-10-oxlint-stable](https://oxc.rs/blog/2025-06-10-oxlint-stable "Oxlint v1.0 Stable | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

Oxlint 1.0 출시.


----

## Release 3.43.0 - 2025.06.09 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.43.0](https://github.com/zloirock/core-js/releases/tag/v3.43.0 "Release 3.43.0 - 2025.06.09 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.43.0 출시.
Explicit Resource Management/Array.fromAsync/Error.isError가 Stable으로 이행.
Joint iteration/Iterator chunking의 Stage 2 proposal 추가, `Math.clamp`에서 `Number.prototype.clamp`으로 변경


----

## Node.js — Node v24.2.0 (Current)
[nodejs.org/en/blog/release/v24.2.0](https://nodejs.org/en/blog/release/v24.2.0 "Node.js — Node v24.2.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.2.0 출시.
HTTP/2 priority signaling 삭제, `import.meta.main` 지원


----

## Release pnpm 10.12.1 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.12.1](https://github.com/pnpm/pnpm/releases/tag/v10.12.1 "Release pnpm 10.12.1 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.12.1 출시.
실험적 기능으로 `enableGlobalVirtualStore` 옵션으로 글로벌 가상 스토어 지원.
의존 관계 그래프 해쉬를 이름으로 글로벌 스토어로 하드링크 해서 캐시가 있을 때 설치가 고속이 됨.
`pnpm update`가 catalog 지원, `catalogMode` 옵션 추가, `--save-catalog` 추가

- [pnpm 10.12 Introduces Global Virtual Store and Expanded Vers...](https://socket.dev/blog/pnpm-introduces-global-virtual-store-and-expanded-version-catalogs "pnpm 10.12 Introduces Global Virtual Store and Expanded Vers...")

----

## Jest 30: Faster, Leaner, Better · Jest
[jestjs.io/blog/2025/06/04/jest-30](https://jestjs.io/blog/2025/06/04/jest-30 "Jest 30: Faster, Leaner, Better · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 30 출시.
Node.js 14/16/19/21 지원 종료, TypeScript 5.4+, jsdom 26 업데이트.
`expect` 얼라이어스 삭제, `--testPathPattern`를 `--testPathPatterns` 으로 재명명. 
unrs-resolver 사용해 성능과 메모리 개선, 설정 파일에서 TS 지원, `import.meta` 지원, `using` 사용한 spy 자동복구.
`expect.arrayOf` 추가, `jest.advanceTimersToNextFrame()` 추가, `jest.unstable_unmockModule()` 추가


----

## News from WWDC25: WebKit in Safari 26 beta | WebKit
[webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/ "News from WWDC25: WebKit in Safari 26 beta | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 26 beta 변경점 관련.
CSS는, Anchor Positioning/Scroll-driven Animations/`text-wrap:pretty`/`contrast-color()`/`progress()` 지원.
Web API는, WebGPU/HDR Images/Digital Credentials API/Trusted Types API/URL Pattern 지원.
Web Inspector에서 Service Worker나 비동기 디버그 개선.
그 외로는, SVG 파비콘 대응, WebAssembly를 인터프리터에서 쓸 때 실행 속도 개선


----
<h1 class="site-genre">읽을거리</h1>

----

## State of CSS 2025
[survey.devographics.com/en-US/survey/state-of-css/2025](https://survey.devographics.com/en-US/survey/state-of-css/2025 "State of CSS 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">Survey</span></p>

CSS 개발자 앙케이트 State of CSS 2025 모집 시작


----

## WebStatus.dev: Now with more data, deeper insights, and a clearer path to Baseline  |  Blog  |  web.dev
[web.dev/blog/web-platform-dashboard-evolution?hl&#x3D;en](https://web.dev/blog/web-platform-dashboard-evolution?hl=en "WebStatus.dev: Now with more data, deeper insights, and a clearer path to Baseline  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

웹플랫폼에서 Baseline 구현 상태를 가시화하는 대시보드 WebStatus.dev 관련하여

- [Web Platform Status](https://webstatus.dev/ "Web Platform Status")

----

## We shipped FinalizationRegistry in Workers: why you should never use it
[blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/](https://blog.cloudflare.com/we-shipped-finalizationregistry-in-workers-why-you-should-never-use-it/ "We shipped FinalizationRegistry in Workers: why you should never use it")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Cloudflare Workers에서 `FinalizationRegistry` API 지원 관련.
WebAssembly와 연계할 때 메모리 관리로, JavaScript 객체가 가비지 콜렉션 되늘 때 콜백 실행하는 API.  
비결정적인 실행 타이밍을 위해 사용 권장하지 않고, 대신 Explicit Resource Management 사용을 추천. I/O 조작이 무효화하는 등 안전 대책을 구현해서 제공


----

## Storybook 9
[storybook.js.org/blog/storybook-9/](https://storybook.js.org/blog/storybook-9/ "Storybook 9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Storybook 9 변경점 관련하여.
파괴적인 변경으로, `@storybook/addon-essentials` 삭제하고 core에 통합, 패키지 구조 변경.
Vitest과 Playwright 사용해서 Storybook 테스트 기능을 Stable으로 변경, 패키지 크기를 48% 삭감.
Interaction/Accessibility/Visual 테스트 기능 통합, Story 생성 기능, Tags-based 관리 기능 추가.
Vite-powered Next.js, Svelte 5, React Native 개선

- [Migration guide for Storybook 9.0 | Storybook docs](https://storybook.js.org/docs/migration-guide?ref=storybookblog.ghost.io "Migration guide for Storybook 9.0 | Storybook docs")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## web-infra-dev/rstest: The testing framework powered by Rspack (WIP).
[github.com/web-infra-dev/rstest](https://github.com/web-infra-dev/rstest "web-infra-dev/rstest: The testing framework powered by Rspack (WIP).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">rspack</span></p>

Rspack 사용한 Vitest 같은 테스트 프레임워크


----

## aymericzip/intlayer: Internationalisation solution for JS application focusing on scalability. Make your JavaScript / TypeScript application multilingue.
[github.com/aymericzip/intlayer](https://github.com/aymericzip/intlayer "aymericzip/intlayer: Internationalisation solution for JS application focusing on scalability. Make your JavaScript / TypeScript application multilingue.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

React/Next.js/Vue 지원하는 i18n 프레임워크.
코드 생성과 로케일 파일을 사용한 번역, 비주얼 에디터, middleware 제공, Markdown 지원


----

## Nergie/no-barrel-file
[github.com/Nergie/no-barrel-file](https://github.com/Nergie/no-barrel-file "Nergie/no-barrel-file")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

barrel imports 검지하고 수정하는 도구


----
