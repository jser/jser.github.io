---
title: "2024-08-25: WebdriverIO v9, Node v22.7.0(TS `enum`와 `namespace` 지원), Deno 1.46(Last 1.x)"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-08-25T01:34:12.084Z
category: JSer
tags:
- nodejs
- Vue
- TypeScript
- webdriver
- Bun

---

JSer.info #704 - WebdriverIO v9가 출시되었어요.

- [WebdriverIO v9 Released | WebdriverIO](https://webdriver.io/blog/2024/08/15/webdriverio-v9-release/)

새 기능으로, WebDriver BiDi 지원, `url` 명령어 추가, `addInitScript` 명령어 추가, `setViewport` 명령어 추가, ShadowRoot 지원이 있어요.

그리고, `emulate` 명령어으로 Clock 에뮬레이션 지원, 요소가 interactive가 되도록 자동적으로 대기하는 변경도 포함되어있어요.

---

Node.js v22.7.0가 출시되었어요.

- [Node.js — Node v22.7.0 (Current)](https://nodejs.org/en/blog/release/v22.7.0)

새 기능으로, `--experimental-transform-types` 플래그로 TypeScript의 `enum`과 `namespace` 변환을 지원해요.
그리고, 애매한 JS를 CommonJS인가 ES Modules인가 판정해 실행하는 `--experimental-detect-module` 플래그를 기본적으로 유효, Buffer 성능 개선도 있어요.

---

Deno v1.46가 출시되었어요.

- [Deno 1.46: The Last 1.x Release](https://deno.com/blog/v1.46)

Deno 1.x 최종 출시가 될 예정이에요.

`deno run main.ts`의 `run` 생략할 수 있어요, `deno task`를 `deno run`로도 호출 가능할 수 있어요, `--allow-*`/`--deny-*` 생략형 추가, `--env`를 `--env-file`으로 변경, `deno fmt`가 HTML/CSS/YAML 지원, `deno remove`/`deno clean` 명령어 추가, `deno compile`가 Code Sign에 대응했어요

그 외로는 std 패키지 대부분이 Stable이 되었어요.

- [The Road to Stabilizing the Standard Library · Issue #4600 · denoland/std](https://github.com/denoland/std/issues/4600)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v11.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v11.0.0](https://github.com/vueuse/vueuse/releases/tag/v11.0.0 "Release v11.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v11.0.0 출시.
의존 major 업데이트, 추가 추가


----

## WebdriverIO v9 Released | WebdriverIO
[webdriver.io/blog/2024/08/15/webdriverio-v9-release/](https://webdriver.io/blog/2024/08/15/webdriverio-v9-release/ "WebdriverIO v9 Released | WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v9. 출시.
WebDriver BiDi 지원, `url` 명령어 추가, `addInitScript` 명령어 추가, `setViewport` 명령어 추가, ShadowRoot 지원.
`emulate` 명령어로 Clock 에뮬레이션 지원, 요소가 interactive 될 때까지 자동적으로 대기하도록 변경.


----

## Node.js — Node v20.17.0 (LTS)
[nodejs.org/en/blog/release/v20.17.0](https://nodejs.org/en/blog/release/v20.17.0 "Node.js — Node v20.17.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.17.0 출시.
ESM를 `require()`로 로드가능한 `--experimental-require-module` 플래그 추가,
Glob 패턴 판정 가능한 `path.matchesGlob` 추가.
DuplexPair API 공개


----

## Bun v1.1.25 | Bun Blog
[bun.sh/blog/bun-v1.1.25](https://bun.sh/blog/bun-v1.1.25 "Bun v1.1.25 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.25 출시.
`node:cluster` 지원, V8의 interal API를 부분적 지원, `bun build --compile`으로 지정한 파일을 바이너리 내에 파일을 임베딩 가능


----

## stackblitz-labs/pkg.pr.new: Continuous (Preview) Releases for your libraries!
[github.com/stackblitz-labs/pkg.pr.new](https://github.com/stackblitz-labs/pkg.pr.new "stackblitz-labs/pkg.pr.new: Continuous (Preview) Releases for your libraries!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">github</span> <span class="jser-tag">CI</span></p>

CI에서 커밋째로 npm 패키지 공개 가능한 도구와 서비스.


----

## Release v15.0.0 · capricorn86/happy-dom
[github.com/capricorn86/happy-dom/releases/tag/v15.0.0](https://github.com/capricorn86/happy-dom/releases/tag/v15.0.0 "Release v15.0.0 · capricorn86/happy-dom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Happy DOM v15.0.0 출시.
Node.js 18 미만 지원 종료, `HTML*Element` 지원 추가


----

## Announcing TypeScript 5.6 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-rc/ "Announcing TypeScript 5.6 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.6 RC 출시.
ESLint의 `no-constant-binary-expression`와 닮은 항상 true/nullish가 되는 잘 못 된 방법을 에러로 하도록 변경, Iterator Helper 지원.
ES2022의 Arbitrary module namespace identifier names 지원, `--noUncheckedSideEffectImports` 플래그 추가.
자료형 체크하지 않고 파일 출력 가능한 `--noCheck` 플래그 추가, `--stopOnBuildErrors` 플래그 추가


----

## Node.js — Node v22.7.0 (Current)
[nodejs.org/en/blog/release/v22.7.0](https://nodejs.org/en/blog/release/v22.7.0 "Node.js — Node v22.7.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.7.0 출시.
TypeScript의 `enum`과 `namaspace` 변환하는 `--experimental-transform-types` 플래그 추가.
애매한 JS를 CommonJS인가 ES Modules인가 판정해서 실행하는 `--experimental-detect-module` 플래그를 기본 유효화, Buffer 성능 개선


----

## Release v1.0.0-rc.0 · web-infra-dev/rspack
[github.com/web-infra-dev/rspack/releases/tag/v1.0.0-rc.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0-rc.0 "Release v1.0.0-rc.0 · web-infra-dev/rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

rspack v1.0.0-rc.0 출시.
eval-source-map 성능 개선, `HtmlRspackPlugin`가 이스케이프 구문 지원


----

## Nuxt 3.13 · Nuxt Blog
[nuxt.com/blog/v3-13](https://nuxt.com/blog/v3-13 "Nuxt 3.13 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Nuxt</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.13 출시.
Route Groups 지원, `NuxtLink`에 `prefetchOn` 추가, `@vue/runtime-core` 자료형을 확장하지 않도록 변경


----

## Electron 32.0.0 | Electron
[www.electronjs.org/blog/electron-32-0](https://www.electronjs.org/blog/electron-32-0 "Electron 32.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 32 출시.
Chromium 128/Node.js 20.16.0/V8 12.8 업데이트, `webcontents.navigationHistory` API 추가, `zstd` 대응.
`File` 객체에서 비표준 `path` 프로퍼티 삭제한 파괴적 변경


----

## Deno 1.46: The Last 1.x Release
[deno.com/blog/v1.46](https://deno.com/blog/v1.46 "Deno 1.46: The Last 1.x Release")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.46 출시.
Denov 1.x 최종 출시.
`deno run`의 `run` 생략 가능, `deno task`를 `deno run`으로 호출 가능, `--allow-*`/`--deny-*` 생략형 추가.
`--env`를 `--env-file`으로 이름 변경, `deno fmt`가 HTML/CSS/YAML 지원, `deno remove`/`deno clean` 명령어 추가.
`deno compile`가 Code Sign 대응, std를 Stable로 변경


----
<h1 class="site-genre">읽을거리</h1>

----

## blocking=render: Why would you do that?! – Harry Roberts – Web Performance Consultant
[csswizardry.com/2024/08/blocking-render-why-whould-you-do-that/](https://csswizardry.com/2024/08/blocking-render-why-whould-you-do-that/ "blocking=render: Why would you do that?! – Harry Roberts – Web Performance Consultant")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

`blocking=render`에 관하여.
anti-flicker snippet 같이 의도적으로 페이지를 보이지 않게 하고 싶을 때 유스케이스


----

## Node.js에서 자료형 안전한 환경변수를 다루는 스니펫 | Web Scratch
[efcl.info/2024/08/24/type-safe-env/](https://efcl.info/2024/08/24/type-safe-env/ "Node.js에서 자료형 안전한 환경변수를 다루는 스니펫 | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.js에서 환경변수를 TypeScript 정의, 명령어에 따라 환경 변수 세트를 자료형 안전하게 전달하는 방법에 대하여


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## vitest-dev/eslint-plugin-vitest: eslint plugin for vitest
[github.com/vitest-dev/eslint-plugin-vitest?tab&#x3D;readme-ov-file](https://github.com/vitest-dev/eslint-plugin-vitest?tab=readme-ov-file "vitest-dev/eslint-plugin-vitest: eslint plugin for vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">plugin</span></p>

vitest 대상 ESLint 플러그인

- [Vitest 공식이 된 eslint-plugin-vitest 도입해서, 적절한 Vitest 작성법 배우기](https://zenn.dev/bs_kansai/articles/8ff70404804f60)

----
<h1 class="site-genre">書籍関係</h1>

----

## Tailwind CSS 프론트엔드 개발 교과서
[www.amazon.co.jp/dp/4798070971/](https://www.amazon.co.jp/dp/4798070971/ "Tailwind CSS 프론트엔드 개발 교과서")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css </span> <span class="jser-tag">book</span></p>

2024년 12월 31일 발매
Tailwind CSS에 대한 도서


----
