---
title: "2025-03-12: React Aria March 5, 2025, Firefox 136.0, TypeScript 컴포넌트를 Go로 이식"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-03-12T03:37:21.235Z
category: JSer
tags:
- React
- TypeScript
- Vue
- Electron
- pnpm

---

JSer.info #728 - React Aria March 5, 2025 출시되었다

- [March 5, 2025 Release – React Spectrum Releases](https://react-spectrum.adobe.com/releases/2025-03-05.html)

Toast/Tree/Virtualizer 컴포넌트를 추가, Autocomplete를 Menu/Select와 조합해서 이용할 수 있도록 되었다.
또한, `<Pressable>`/`<Focusable>` 추가, `usePress` 리팩터링이 포함되어있다.
그 외로는, 문서를 Tailwind v4에 대응

---

Firefox 136.0 출시되었다

- [Firefox 136.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/136.0/releasenotes/)
- [Firefox 136 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/136)

HTML의 `autocorrect` 속성을 지원, `Intl.DurationFormat` 지원, Data URLs 최대 크기를 32MB에서 Chrome과 같은 512MB로 변경되었다.
Cookie Storage API 지원, HTTPS-First로 변경되었다.
실험적 기능으로, `Error.captureStackTrace()` 지원, `Clear-Site-Data` 헤더 지원, SVG의 `<discard>` 요소 지원이 포함되었다.

----

TypeScript 컴파일러를 Go언어로 포팅하는 계획이 공개되었다.

- [A 10x Faster TypeScript - TypeScript](https://devblogs.microsoft.com/typescript/typescript-native-port/)

TypeScript 자료형 체크나 LSP 성능 개선하기 위해서, TypeScript 컴파일러를 Go언어로 포팅할 계획이 공개되었다.
이식한 native판을 TypeScript 7로 출시할 예정이며, native판이 안정될 떄까지는 JS 버전도 관리될 예정이다.
TypeScript 7가 출시된 이후도, 이행 문제가 없을때까지는 JS 버전을 관리하며, 99.99%는 그대로 이행할 수 있는 것을 목표로 하고 있다.

- https://github.com/microsoft/typescript-go

> "Why a port instead of a rewrite? What's the difference? · microsoft/typescript-go · Discussion #410"
> https://github.com/microsoft/typescript-go/discussions/411

왜 다시 작성하지 않고 이행을 선택했는가는, TypeScript 컴파일러 코드 기반 크기나, TypeScript 사양이 따로 있는 것이 아니라 레퍼런스 구현만이라는 이유도 들고 있다.

> Why Go? #411 
> https://github.com/microsoft/typescript-go/discussions/411

Go를 선택할 이유로, GC가 있다는 이유와 의미론적 코드 구조가 JS와 닮았고, 이식성 높은 것을 이유로 들고 있다.

- [TypeScript is being ported to Go | interview with Anders Hejlsberg - YouTube](https://www.youtube.com/watch?v=10qowKUW82U)

C#은 OOP 언어라서, 기존 TypeScript 컴파일러 코드를 이행하기에는, 구조 변경할 이유가 있었기에 선택하기에는 어려운 면이 있었다.
그리고, TypeScript 컴파일러는 GC에 의존하고 있어서, Rust 언어는 선택하기 어려운 면이 있었다.
다시 작성했다면, 처음부터 GC/순환참조 그래프에 의존하지 않는 구조로 하고 싶다는 이야기.

또한, 구체적인 출시 스케쥴은 미정이지만, 기본적으로는 이행이 부드럽게 이뤄지는 것을 목표로 하고 있다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## March 5, 2025 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2025-03-05.html](https://react-spectrum.adobe.com/releases/2025-03-05.html "March 5, 2025 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria March 5, 2025 출시.
Toast/Tree/Virtualizer 컴포넌트를 추가, Autocomplete를 Menu/Select와 조합해서 이용하도록.
`<Pressable>`/`<Focusable>` 추가, 
`usePress` 리팩터링.
문서를 Tailwind v4에 대응


----

## Electron 35.0.0 | Electron
[www.electronjs.org/blog/electron-35-0](https://www.electronjs.org/blog/electron-35-0 "Electron 35.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 35.0.0 출시.
Chromium 134/Node.js 22.14.0/V8 13.5으로 업데이트, Service Worker Preload Scripts 지원


----

## Release v3.16.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.16.0](https://github.com/nuxt/nuxt/releases/tag/v3.16.0 "Release v3.16.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v3.16.0 출시.
`create-nuxt` 패키지 추가, 성능 개선, delayed/lazy hydration 지원


----

## Release pnpm 10.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.6.0](https://github.com/pnpm/pnpm/releases/tag/v10.6.0 "Release pnpm 10.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.6.0 출시.
`.npmrc` 설정을 전부 `pnpm-workspace.yaml`에 입력하도록


----

## Release v1.51.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.51.0](https://github.com/microsoft/playwright/releases/tag/v1.51.0 "Release v1.51.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.51.0 출시.
`browserContext.storageState()`가 IndexedDB 지원, `filter({ visible })` 추가, `expect(page).toHaveURL(fn)` 지원.
LLM 대상 Copy prompt 레포트에 추가


----

## Release @ark-ui/react@5.0.0 · chakra-ui/ark
[github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%405.0.0](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%405.0.0 "Release @ark-ui/react@5.0.0 · chakra-ui/ark")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Solid</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ark UI v5 출시.
성능과 Bundle Size 개선, 컴포넌트에 기본값을 지정하는 옵션 추가


----

## Firefox 136.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/136.0/releasenotes/](https://www.mozilla.org/en-US/firefox/136.0/releasenotes/ "Firefox 136.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 136 출시.
HTML의 `autocorrect` 속성 지원, `Intl.DurationFormat` 지원, Data URLs 최대 크기를 32MB에서 Chrome와 같은 512MB로 변경.
Cookie Storage API 지원, HTTPS-First로 변경.
실험적 기능으로, `Error.captureStackTrace()` 지원, `Clear-Site-Data` 헤더 지원, SVG의 `<discard>` 요소 지원

- [Firefox 136 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/136 "Firefox 136 for developers - Mozilla | MDN")

----

## Bun v1.2.5 | Bun Blog
[bun.sh/blog/bun-v1.2.5](https://bun.sh/blog/bun-v1.2.5 "Bun v1.2.5 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.5 출시.
Node-API와 호환성 개선, `node:timers` 추가, `Bun.CSRF` 추가.
dev server가 svelte 지원, CSS modules 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## A 10x Faster TypeScript - TypeScript
[devblogs.microsoft.com/typescript/typescript-native-port/](https://devblogs.microsoft.com/typescript/typescript-native-port/ "A 10x Faster TypeScript - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

TypeScript의 자료형 체크나 LSP 퍼포먼스 개선하기 위해, TypeScript 컴파일러나 LSP 도구를 Go언어로 포팅하는 이야기.
이식된 native판을 TypeScript 7로 출시할 예정, native판이 안정될 때까지는 JS 버전도 관리될 예정.


----

## Split Route Modules | Remix
[remix.run/blog/split-route-modules](https://remix.run/blog/split-route-modules "Split Route Modules | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Router v7.2.0에 추가된 Split Route Modules 관련하여.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## microsoft/typescript-go: Staging repo for development of native port of TypeScript
[github.com/microsoft/typescript-go](https://github.com/microsoft/typescript-go "microsoft/typescript-go: Staging repo for development of native port of TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">golang</span> <span class="jser-tag">Tools</span></p>

TypeScript를 Go 언어로 포팅 구현.
자료형 체크 이외는 병렬로 처리 가능. 자료형 체크는 몇 몇 블록으로 나눠서 처리하도록 되어있음.

- [A 10x faster TypeScript - YouTube](https://www.youtube.com/embed/pNlq-EVld70?si=OaEgTg6ROtfYDYLt "A 10x faster TypeScript - YouTube")

----

## Pikku - A Function-First Framework for Node.js | Pikku
[pikku.dev/](https://pikku.dev/ "Pikku - A Function-First Framework for Node.js | Pikku")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

TypeScript로 작성된 웹 프레임워크.
단순 함수 핸들러를 정의. TypeScript 코드에서 JSON 스키마 생성해 검증하고, 클라이언트 코드도 자동적으로 생성


----
