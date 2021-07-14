---
title: "2021-07-06: TypeScript 4.4 Beta, immutable-js 4.0.0-rc.13, petite-vue"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-07-05T22:36:05.800Z
category: JSer
tags:
- node.js
- Chrome
- WebAssembly
- 설문
- Markdown

---

JSer.info #547 - TypeScript 4.4 beta 릴리스.

- [Announcing TypeScript 4.4 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/)

Control Flow Analysis 개선 되어 Type Gurde의 결과를 변수에 대입하여 다루는 등의 Alias 경우도 올바르게 추론된다.
또, Index Signatures에 Symbol이나 Template String를 사용할 수 있도록 됐다.
Catch 절의 기본 타입을 `unknown`으로 하는 `useUnknownInCatchVariables` 옵션과 optional과 `undefined` 값을 구별하는 `exactOptionalPropertyTypes` 옵션이 추가됐다.

그 외로 declaration의 생성 및 `strict` 모드에서의 빌드 성능이 개선됐다.

----

immutable-js 4.0.0-rc.13 릴리스.

- [Release 4.0.0-rc.13 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13)

immutable-js는 [v4.0.0-rc.12](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.12)에서 프로젝트 관리가 중단돼 [immutable-oss](https://github.com/immutable-js-oss) Organiztion으로 포크돼 관리되고 있었다.

이번 릴리스에서는 `immutable-js` Organization에 `immutable-oss` 메인테이너를 추가하고 `immutable-oss`의 변경 내용도 immutable-js 4.0.0-rc.13로 통합한다.
즉, `immutable-js`으로 프로젝트 관리를 재개하는 릴리스다.

- [Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/issues/1689)
- [Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/pull/1833)

----

Vue 서브셋으로 파일 크기가 작은 petite-vue 공개.

- [vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement](https://github.com/vuejs/petite-vue)

Vue 호환 템플릿 문법과 서브셋 API를 제공하는 라이브러리.
ES Modules으로 import하여 사용할 수 있으며 Vue에는 없는 `v-scope`나 `v-effect` 등의 속성도 갖고 있다.
[Alpine.js](https://alpinejs.dev/) 처럼 이미 렌더링된 HTML에 대해 동작을 추가하는 작은 크기의 라이브러리를 목적으로 하고 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Support caching dependencies and LTS aliases · actions/setup-node
[github.com/actions/setup-node/releases/tag/v2.2.0](https://github.com/actions/setup-node/releases/tag/v2.2.0 "Release Support caching dependencies and LTS aliases · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

actions/setup-node 2.2.0 릴리스.
`lts/*` 등 LTS 문법 지원, `cache` 옵션으로 `npm`와 `yarn`에서의 의존 캐시 지원.


----

## Announcing TypeScript 4.4 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4-beta/ "Announcing TypeScript 4.4 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Prototype.js</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.4 Beta 릴리스.
Control Flow Analysis 개선, Index Signatures에 Symbol이나 Template String를 사용할 수 있도록.
Catch 절의 기본 타입을 `unknown`으로 하는 `useUnknownInCatchVariables` 옵션 추가.
optional과 `undefined` 값을 구별하는 `exactOptionalPropertyTypes` 옵션 추가.
declaration의 생성 및 `strict` 모드에서의 빌드 성능 개선.


----

## Release 4.0.0-rc.13 · immutable-js/immutable-js
[github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13](https://github.com/immutable-js/immutable-js/releases/tag/v4.0.0-rc.13 "Release 4.0.0-rc.13 · immutable-js/immutable-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

imutable-js 4.0.0 RC12 릴리스.
fork로 진행했던 immutable-js-oss 변경 내용을 통합하고, 커뮤니티에 의한 메인터넌스를 재개하는 릴리스.

- [Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/issues/1689 "Immutable.js is essentially unmaintained · Issue #1689 · immutable-js/immutable-js")
- [Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js](https://github.com/immutable-js/immutable-js/pull/1833 "Integrate immutable-js-oss fork into main repository by jdeniau · Pull Request #1833 · immutable-js/immutable-js")

----

## vite/CHANGELOG.md at main · vitejs/vite
[github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#240-2021-07-05](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#240-2021-07-05 "vite/CHANGELOG.md at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 2.4.0 릴리스.
`new URL(url, import.meta.url)` 지원, `server.fsServe`를 `server.fs`로 이름 변경, `server.fs.strict` 옵션 추가.

- [Static Asset Handling | Vite](https://vitejs.dev/guide/assets.html#the-public-directory "Static Asset Handling | Vite")

----
<h1 class="site-genre">아티클</h1>

----

## The State of WebAssembly 2021
[blog.scottlogic.com/2021/06/21/state-of-wasm.html](https://blog.scottlogic.com/2021/06/21/state-of-wasm.html "The State of WebAssembly 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">アンケート</span></p>

WebAssembly에 관한 개발자 설문조사.
어떤 언어를 사용하고 있는지, 어떤 용도로 사용하고 있는지, 바라는 기능 등 다양한 문항으로 설문을 진행.


----

## RenderingNG - Chrome Developers
[developer.chrome.com/blog/renderingng/](https://developer.chrome.com/blog/renderingng/ "RenderingNG - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">blink</span> <span class="jser-tag">article</span></p>

Chrome의 렌더링 엔진인 Blink의 새로운 아키텍처 RenderingNG의 프로젝트 주요 내용 정리.
CompositeAfterPaint, LayoutNG, BlinkNG, Viz, OffscreenCanvas, VideoNG 등 소개.


----

## Migrating from Capybara to Puppeteer - Engineering Blog - Wealthfront
[eng.wealthfront.com/2021/06/25/migrating-from-capybara-to-puppeteer/](https://eng.wealthfront.com/2021/06/25/migrating-from-capybara-to-puppeteer/ "Migrating from Capybara to Puppeteer - Engineering Blog - Wealthfront")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

E2E 테스트를 Capybara에서 Puppeteer로 이전한 내용 소개.
E2E 테스트 프레임워크 선택과 이전의 목적이었던 실행 시간 단축에 대한 정리.


----

## Designing a Dataflow Editor With TypeScript and React | Protocol Labs Research
[research.protocol.ai/blog/2021/designing-a-dataflow-editor-with-typescript-and-react/](https://research.protocol.ai/blog/2021/designing-a-dataflow-editor-with-typescript-and-react/ "Designing a Dataflow Editor With TypeScript and React | Protocol Labs Research")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">ElasticSearch</span></p>

React와 TypeScript 기반으로 데이터 흐름 에디터의 설계를 어떻게 했는지 소개.
데이터 흐름 상태 설계, 스키마 객체로 부터 각 Node의 타입 정의를 추출하는 구조를 Generics를 사용해 다루는 방법 등.

- [joeltg/react-dataflow-editor](https://github.com/joeltg/react-dataflow-editor "joeltg/react-dataflow-editor")

----

## Encoding data for POST requests - JakeArchibald.com
[jakearchibald.com/2021/encoding-data-for-post-requests/](https://jakearchibald.com/2021/encoding-data-for-post-requests/ "Encoding data for POST requests - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Fetch의 body에 안전하게 인코딩하여 데이터를 전달하는 방법.
`URLSearchParams`, `FormData`, `blob`, JSON 등을 사용하는 방법 소개.


----

## Image To Text Conversion With React And Tesseract.js (OCR) — Smashing Magazine
[www.smashingmagazine.com/2021/06/image-text-conversion-react-tesseract-js-ocr/](https://www.smashingmagazine.com/2021/06/image-text-conversion-react-tesseract-js-ocr/ "Image To Text Conversion With React And Tesseract.js (OCR) — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Tesseract.js를 사용한 이미지 OCR과 Canvas와 이미지 프리프로세스 기법을 활용한 텍스트 추출 방법 소개.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement
[github.com/vuejs/petite-vue](https://github.com/vuejs/petite-vue "vuejs/petite-vue: 5kb subset of Vue optimized for progressive enhancement")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Vue 서브셋 API와 템플릿을 제공하는 라이브러리.
작은 파일 크기를 목적으로 개발됐다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Saul-Mirone/milkdown: 🍼 Plugin driven WYSIWYG markdown editor.
[github.com/saul-mirone/milkdown/](https://github.com/saul-mirone/milkdown/ "Saul-Mirone/milkdown: 🍼 Plugin driven WYSIWYG markdown editor.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

Prosemirror와 remark를 기반으로 개발한 WYSIWYG 에디터 라이브러리


----

## niksy/promise-any-ponyfill: \`Promise.any\` ponyfill.
[github.com/niksy/promise-any-ponyfill](https://github.com/niksy/promise-any-ponyfill "niksy/promise-any-ponyfill: \`Promise.any\` ponyfill.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">polyfill</span></p>

Promise.any의 polyfill 라이브러리


----

## tinyhttp/malibu: 🏄 Framework-agnostic CSRF middleware for modern Node.js
[github.com/tinyhttp/malibu](https://github.com/tinyhttp/malibu "tinyhttp/malibu: 🏄 Framework-agnostic CSRF middleware for modern Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

CSRF 공격 대책 express middleware.


----
