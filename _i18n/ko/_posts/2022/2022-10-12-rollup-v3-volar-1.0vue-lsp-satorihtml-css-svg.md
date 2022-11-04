---
title: "2022-10-12: Rollup v3, Volar 1.0(Vue LSP), Satori(HTML + CSS = SVG)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-10-12T07:49:16.919Z
category: JSer
tags:
- React
- Ember
- audio
- ESLint
- ECMAScript

---

JSer.info #613 - Rollup 3.0.0이 릴리스 됐다.

- [Release v3.0.0 · rollup/rollup](https://github.com/rollup/rollup/releases/tag/v3.0.0)
- [rollup.js#migration](https://rollupjs.org/guide/en/#migration)

비호환 변경으로 플러그인 API 변경, 옵션 변경이 이뤄졌다.
또, 기본적으로 `import()`를 변환하지 않도록 변경됐고 chunk의 알고리즘도 변경됐다.
그 외로는, Node.js의 ESM 지원과 상호운용성을 개선하기 위해 `output.interop` / `output.exports` / `output.esModule` 옵션의 기본값이 변경 됐다. 주 개선 방식은 `__esModule`라는 Node.js가 지원하지 않는(ESM와 CJS 양쪽 지원을 위해 사용되는) 속성을 줄여나가는 방향이다. 자세한 변경 내용은 다음 PR을 참고한다.

- [[v3.0] Improve interop defaults by lukastaegert · Pull Request #4611 · rollup/rollup](https://github.com/rollup/rollup/pull/4611)

덧붙여, ECMAScript Proposal Stage 3 단계인 [Import Assertions](https://github.com/tc39/proposal-import-assertions)도 지원한다.

---

Vue 관련 기능(템플릿 등)의 IDE 지원 도구인 Volar 1.0이 릴리스 됐다.

- [Volar 1.0 "Nika" Released! | The Vue Point](https://blog.vuejs.org/posts/volar-1.0.html)

`<template lang="pug">`의 built-in 지원을 종료하고 플러그인으로 대체.
`vue-tsc`가 `--watch`와 `--declaration --emitDeclarationOnly`를 지원한다.
또, 코어 모듈이 Vue 등 프레임워크를 의존하지 않게 되며 샘플로 [Svelte Langauge Server Example](https://github.com/johnsoncodehk/volar/tree/master/examples)를 공개했다.

---

HTML과 CSS로 작성한 코드를 SVG 이미지로 변환하는 라이브러리 Satori가 공개됐다.

- [vercel/satori: Enlightened library to convert HTML and CSS to SVG](https://github.com/vercel/satori)

OGP(OG) 이미지를 위해 컨텐츠에 기반한 이미지를 생성해야 하는 경우가 증가하고 있다.
Puppeteer 등을 이용하면 HTML과 CSS로 작성한 디자인으로 부터 이미지(스크린샷)를 생성할 수는 있다.
하지만, 브라우저 프로세스를 구동하는 건 시간이 걸리며 리소스 소비도 큰 편이다.

때문에, Satori는 Flexbox 레이아웃 엔진 구현체로 알려진 [Yoga](https://yogalayout.com/)의 Wasm빌드 버전을 사용해 HTML과 CSS의 서브셋을 구현해 SVG를 생성한다.

다음 글을 통해 자세히 설명하고 있으니 참고한다.

- [Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 2.0.0-rc.0 · vercel/swr
[github.com/vercel/swr/releases/tag/2.0.0-rc.0](https://github.com/vercel/swr/releases/tag/2.0.0-rc.0 "Release 2.0.0-rc.0 · vercel/swr")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

SWR 2.0.0-rc.0 릴리스.
mutation에 의한 에러를 throw 하도록 변경하고 이 동작을 비활성화 할 수 있는 `throwOnError` 옵션이 추가 됐다.


----

## ESLint v8.25.0 released - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2022/10/eslint-v8.25.0-released/](https://eslint.org/blog/2022/10/eslint-v8.25.0-released/ "ESLint v8.25.0 released - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.25.0 릴리스.
새로운 설정 시스템에서는 `.eslintignore` 파일을 지원하지 않으며 설정 파일 내의 `ignores` 필드에서 무시할 파일을 지정하도록 변경됐다.


----

## Chrome 107 beta - Chrome Developers
[developer.chrome.com/blog/chrome-107-beta/](https://developer.chrome.com/blog/chrome-107-beta/ "Chrome 107 beta - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 107 beta 릴리스.

* `grid-template`에서 transition 지원
* Screen Capture API 개선
* Resource Timing에 `renderBlockingStatus` 추가
* Permissions policy의 origin 지정에 * 을 사용할 수 있도록 개선
* &lt;form&gt; 요소에서 `rel` 속성 지원
* Origin Trials로서 Declarative PendingBeacon API, Permissions policy의 unload 지원
* `Expect-CT` HTTP 헤더 삭제


- [resource-timing/Render\_Blocking\_Status.md at render-blocking-status-explainer · abinpaul1/resource-timing](https://github.com/abinpaul1/resource-timing/blob/render-blocking-status-explainer/Explainer/Render_Blocking_Status.md "resource-timing/Render\_Blocking\_Status.md at render-blocking-status-explainer · abinpaul1/resource-timing")

----

## Release v7.0.0 · capricorn86/happy-dom
[github.com/capricorn86/happy-dom/releases/tag/v7.0.0](https://github.com/capricorn86/happy-dom/releases/tag/v7.0.0 "Release v7.0.0 · capricorn86/happy-dom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Happy DOM v7.0.0 릴리스.
`CSSStyleDeclaration` 지원 개선, `Window.getComputedStyle()` 지원 개선, `CSSStyleSheet` 지원 개선 등.


----

## Release v3.0.0 · rollup/rollup
[github.com/rollup/rollup/releases/tag/v3.0.0](https://github.com/rollup/rollup/releases/tag/v3.0.0 "Release v3.0.0 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rollup</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup v3.0.0 릴리스.
플러그인 API 인터페이스 변경, 옵션이 삭제되거나 기본값 변경, 기본적으로 `import()`를 유지하도록 변경, chunk의 알고리즘을 변경하는 등 비호환 변경이 이뤄졌다.
또, 기본적으로 Node.js의 ESM을 지원하며 관련 호환성이 개선됐고 import assertions도 지원한다.

- [rollup.js migration](https://rollupjs.org/guide/en/#migration "rollup.js migration")

----
<h1 class="site-genre">아티클</h1>

----

## Evolving Ember’s Major Version Process
[blog.emberjs.com/evolving-embers-major-version-process/](https://blog.emberjs.com/evolving-embers-major-version-process/ "Evolving Ember’s Major Version Process")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">article</span></p>

Ember는 메이저 릴리스(비호환 변경)를 최대한 적게 한다는 방침이었기 때문에 메이저 릴리스 간격이 길었다. 이 간격이 길수록 비권장 기능이 제거되는 시점을 알기 어려워 사용자에게 혼란을 주는 등의 문제가 있었다.
따라서 예측 가능한 리듬을 위해 6주 마다 마이너 릴리스, 18개월 마다 메이저 릴리스를 하는 정책을 발표했다.
또, `X.10` 이후로는 비권장을 추가하지 않고 메이저 릴리스 시에는 비권장을 삭제하기만 하는 등의 규칙을 도입하여 개발자가 비권장에 언제 대응하면 되는지 명확히 알 수 있도록 한다.


----

## Intl.Segmenter로 일문 개행을 개선해 보자(일본어)
[zenn.dev/notfounds/articles/58c465d4029dc1](https://zenn.dev/notfounds/articles/58c465d4029dc1 "Intl.Segmenter로 일문 개행을 개선해 보자")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">article</span></p>

`Intl.Segmenter`를 사용한 띄워쓰기를 고려한 개행 구현 소개.
또, CSS / JS 엔진 구현에 따른 차이와 Hydration으로 인한 차이를 무시하는 방법도 소개한다.


----

## 10 best practices to containerize Node.js web applications with Docker | Snyk Blog
[snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/](https://snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/ "10 best practices to containerize Node.js web applications with Docker | Snyk Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Docker</span> <span class="jser-tag">article</span></p>

Docker 기반의 Node.js 웹 애플리케이션 사례(practice) 소개.
Docker Image 작성, Gracefull Shutdown 대응, 불필요한 정보를 삭제하는 등 Docker와 함께 Node.js 운영하는데 있어 고려해야 할 10가지 팁을 다루고 있다.


----

## Volar 1.0 &quot;Nika&quot; Released! | The Vue Point
[blog.vuejs.org/posts/volar-1.0.html](https://blog.vuejs.org/posts/volar-1.0.html "Volar 1.0 \&quot;Nika\&quot; Released! | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span></p>

Volar 1.0 릴리스.
<template lang=“pug”>의 built-in 지원을 종료하고 플러그인 화.
`vue-tsc`에서 `--watch`와 `--declaration --emitDeclarationOnly` 지원.
코어 모듈이 Vue 등의 특정 프레임워크를 의존하지 않도록 개선.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## slash9494/react-modern-audio-player: 🔊 Simple, accessible and flexible audio player
[github.com/slash9494/react-modern-audio-player](https://github.com/slash9494/react-modern-audio-player "slash9494/react-modern-audio-player: 🔊 Simple, accessible and flexible audio player")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

React 기반의 음악 플레이어 컴포넌트.


----

## leeoniya/uFuzzy: A tiny, efficient fuzzy search that doesn&#039;t suck
[github.com/leeoniya/uFuzzy](https://github.com/leeoniya/uFuzzy "leeoniya/uFuzzy: A tiny, efficient fuzzy search that doesn&#039;t suck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search </span> <span class="jser-tag">library</span></p>

파일 크기가 작은 퍼지 문자열 검색(fuzzy string search, 근사 / 근접 문자열 검색) 라이브러리. 특별한 의존 모듈 없이 퍼지 문자열 검색 알고리즘을 순수 자바스크립트로 가볍게 구현. 번들러로는 롤업을 사용하고 있다.


----

## vercel/satori: Enlightened library to convert HTML and CSS to SVG
[github.com/vercel/satori](https://github.com/vercel/satori "vercel/satori: Enlightened library to convert HTML and CSS to SVG")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">SVG</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HTML과 CSS로 부터 SVG를 생성하는 버셀의 라이브러리.
HTML과 CSS의 렌더링 결과를 SVG의 Path 요소로 변환하여 벡터 그래픽으로 활용할 수 있다.
yoga-layout을 사용해 CSS의 서브셋을 구현하고 있으며 브라우저의 렌더링을 사용하지 않고서 SVG로 변환한다.

- [Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images "Introducing OG Image Generation: Fast, dynamic social card images at the Edge – Vercel")

----

## fp-ts/core
[github.com/fp-ts/core](https://github.com/fp-ts/core "fp-ts/core")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">functional</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

함수형 프로그래밍을 위한 TypeScript 라이브러리.
함수형 프로그래밍을 위한 다양한 함수, 유틸리티 등을 타입스크립트로 작성하고 제공한다.


----

## stepci/stepci: API Testing and Monitoring made simple
[github.com/stepci/stepci](https://github.com/stepci/stepci "stepci/stepci: API Testing and Monitoring made simple")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

특정 언어에 의존하지 않는 Web API 테스트 도구.
yaml 으로 API 테스트를 정의하고 실행할 수 있다.


----

