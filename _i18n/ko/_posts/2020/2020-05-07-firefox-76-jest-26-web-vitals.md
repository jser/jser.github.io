---
title: "2020-05-07: Firefox 76, Jest 26, Web Vitals"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-05-07T04:42:34.756Z
category: JSer
tags:
- Firefox
- Jest
- Chrome
- Performance

---

JSer.info #486 - Firefox 76이 릴리스됐습니다.

- [Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/)
- [Firefox 76 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/76)
- [Firefox 76 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/en-CA/releases/76/)
- [Firefox 76.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/76.0/releasenotes/)

Firefox 76에서는 개발자 도구가 많이 개선됐습니다.
특정 디렉터리를 디버거 대상에서 제외할 수 있으며 "Copy stack trace"가 추가됐고 WebSocket Inspection에서 Action Cable을 지원합니다.

추가된 기능으로는 Audio worklets, CSS System Colors를 지원합니다.
그 외로 알 수 없는 프로토콜로의 Navigation 이동이 차단되도록 변경 됐습니다.

----

JavaScript 테스트 프레임워크 Jest 26이 릴리스됐습니다.

- [Jest 26: Tick Tock · Jest](https://jestjs.io/blog/2020/05/05/jest-26)

[@sinonjs/fake-timers](https://github.com/sinonjs/fake-timers) 기반의 새로Fake Timer와 `it`이나 `describe` 등을 export 하는 `@jest/globals`가 추가됐고 Native ESM을 지원합니다.
비호환 변경 사항으로는 Node.js 8 미만을 지원 종료 했으며 몇 개의 코어 모듈에서 ES5 빌드를 제공하지 않도록 변경됐습니다.

향후 예정된 변경 사항으로 Jest 27에서 기본 testRunner가 ["jest-circus"](https://github.com/facebook/jest/tree/master/packages/jest-circus)으로 변경되며 environment도 "node"로 변경됩니다.
또, Jest 28에서는 "jest-jasmine2"와 "jest-environment-jsdom"이 코어에서 별도의 패키지로 분리될 예정입니다.

위 내용을 간단하게 정리하자면 다음과 변경될 예정입니다.

- [testRunner](https://jestjs.io/docs/ja/configuration#testrunner-string): [jasmine2](https://github.com/facebook/jest/tree/master/packages/jest-jasmine2) → [circus](https://github.com/facebook/jest/tree/master/packages/jest-circus)
- [testEnvironment](https://jestjs.io/docs/ja/configuration#testenvironment-string): [jsdom](https://github.com/facebook/jest/tree/master/packages/jest-environment-jsdom) → [node](https://github.com/facebook/jest/tree/master/packages/jest-environment-node)

----

[Web Vitals](https://web.dev/vitals/)에서는 웹사이트 성능과 관련한 중요한 지표를 Core Web Vitals라는 개념으로 정리하고 Google/Chrome 계열 제품에서 어떻게 측정할 수 있는지 소개합니다.

현재 Core Web Vitals은 다음 세 가지 지표로 구성돼 있습니다.

- [Largest Contentful Paint (LCP)](https://web.dev/lcp/): 로드 관련 지표
- [First Input Delay (FID)](https://web.dev/fid/): 인터랙션 관련 지표
- [Cumulative Layout Shift (CLS)](https://web.dev/cls/): 렌더링 관련 지표

관련 지표를 측정할 수 있는 [web-vitals](https://github.com/GoogleChrome/web-vitals)이라는 자바스크립트 라이브러리([Performance Observer](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)를 사용하기 때문에 [Chrome에서만 얻을 수 있는 지표](https://github.com/GoogleChrome/web-vitals#browser-support)도 있음)와 [브라우저 확장 기능](https://github.com/GoogleChrome/web-vitals-extension)을 소개합니다.

향후에는 [Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)(이미 지원함), [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/), Search Console 등의 도구에서도 이 지표를 이용할 수 있도록 개선한다고 합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/](https://hacks.mozilla.org/2020/05/firefox-76-audio-worklets-and-other-tricks/ "Firefox 76: Audio worklets and other tricks - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 76이 릴리스됐습니다.
개발자 도구가 개선됐고 Audio worklets과 CSS System Colors 지원하며 알 수 없는 프로토콜로의 Navigation 이동이 차단됩니다.

- [Firefox 76 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/76 "Firefox 76 for developers - Mozilla | MDN")
- [Firefox 76 Site Compatibility | Firefox Site Compatibility](https://www.fxsitecompat.dev/en-CA/releases/76/ "Firefox 76 Site Compatibility | Firefox Site Compatibility")
- [Firefox 76.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/76.0/releasenotes/ "Firefox 76.0, See All New Features, Updates and Fixes")

----

## Node v12.16.3 (LTS) | Node.js
[nodejs.org/en/blog/release/v12.16.3/](https://nodejs.org/en/blog/release/v12.16.3/ "Node v12.16.3 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.16.3이 릴리스 됐습니다.
Experimental로 구현돼 있는 conditional exports와 관련된 경고 메시지가 삭제됐습니다.


----

## Announcing TypeScript 3.9 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-9-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-9-rc/ "Announcing TypeScript 3.9 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.9 RC가 릴리스됐습니다.
`Promise.all` 타입이 개선됐고 빌드 성능이 개선됐으며 Type Error가 보고되지 않도록 하는 `// @ts-expect-error` 코멘트가 추가됐습니다. 또, ECMAScript 사양에 맞춰 Getter/Setter가 변환되도록 수정됐으며 이번 릴리스에 예정됐던 `awaited` type 추가가 연기됐습니다.


----

## jQuery 3.5.1 Released: Fixing a Regression | Official jQuery Blog
[blog.jquery.com/2020/05/04/jquery-3-5-1-released-fixing-a-regression/](http://blog.jquery.com/2020/05/04/jquery-3-5-1-released-fixing-a-regression/ "jQuery 3.5.1 Released: Fixing a Regression | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.5.1이 릴리스 됐습니다.
jQuery 3.5.0에 발생한 회귀 문제를 수정했습니다. 3.5에는 XSS 보안 문제를 해결하기 위해 하위 호환성 없는 부분이 포함됐습니다.


----

## Jest 26: Tick Tock · Jest
[jestjs.io/blog/2020/05/05/jest-26](https://jestjs.io/blog/2020/05/05/jest-26 "Jest 26: Tick Tock · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 26이 릴리스 됐습니다.
`@sinonjs/fake-timers` 기반의 새로운 Fake Timer와 `it`이나 `describe` 등을 などをexport하는 `@jest/globals`가 추가됐고 Native ESM을 지원합니다.
몇 가지 코어 모듈에서 ES5 빌드를 제공하지 않으며 Node.js 8 미만 지원이 종료됐습니다.
향후 예정된 변경 사항으로 Jest 27에서 기본 testRunner가 "jest-circus"으로 변경되며 environment도 "node"로 변경됩니다.
또, Jest 28에서는 "jest-jasmine2"와 "jest-environment-jsdom"이 코어에서 별도의 패키지로 분리될 예정입니다.


----

## Release v1.6.0 · mdx-js/mdx
[github.com/mdx-js/mdx/releases/tag/v1.6.0](https://github.com/mdx-js/mdx/releases/tag/v1.6.0 "Release v1.6.0 · mdx-js/mdx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">ReleaseNote</span></p>

Markdown에 JSX를 확장하는 MDX 1.6.0이 릴리스 됐습니다.
Vue를 베타로 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## What’s in that .wasm? Introducing: wasm-decompile · V8
[v8.dev/blog/wasm-decompile](https://v8.dev/blog/wasm-decompile "What’s in that .wasm? Introducing: wasm-decompile · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

`wasm-decompile`의 WebAssembly 디컴파일 원리를 소개합니다.

- [wabt/decompiler.md at master · WebAssembly/wabt](https://github.com/WebAssembly/wabt/blob/master/docs/decompiler.md "wabt/decompiler.md at master · WebAssembly/wabt")

----

## window.location Cheatsheet - DEV Community 👩‍💻👨‍💻
[dev.to/samanthaming/window-location-cheatsheet-4edl](https://dev.to/samanthaming/window-location-cheatsheet-4edl "window.location Cheatsheet - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">チートシート</span> <span class="jser-tag">article</span></p>

`window.location` 객체의 속성이나 메서드 동작이 알기 쉽게 정리돼 있습니다.


----

## Improved Next.js and Gatsby page load performance with granular chunking
[web.dev/granular-chunking-nextjs/](https://web.dev/granular-chunking-nextjs/ "Improved Next.js and Gatsby page load performance with granular chunking")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack의 `SplitChunksPlugin`을 이용해 Next.js 9.2나 Gatsby의 페이지 간 Common chunk를 분리하는 방법을 소개합니다.
HTTP/2 환경에서 `maxInitialRequests` 설정으로 요청 수가 증가하면 어떠한 영향이 있고, 라우팅에 분리한 청크를 적용하는 방법은 무엇인지 설명합니다.

- [feat(gatsby): enable granular chunks by wardpeet · Pull Request #22253 · gatsbyjs/gatsby](https://github.com/gatsbyjs/gatsby/pull/22253 "feat(gatsby): enable granular chunks by wardpeet · Pull Request #22253 · gatsbyjs/gatsby")

----

## Web Vitals
[web.dev/vitals/](https://web.dev/vitals/ "Web Vitals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

웹사이트 성능과 관련한 중요한 지표를 Core Web Vitals라는 개념으로 정리하고 Google/Chrome 계열 제품에서 어떻게 측정할 수 있는지 소개합니다.

Core Web Vitals로는 Largest Contentful Paint(LCP), First Input Delay(FID), Cumulative Layout Shift(CLS)가 있고, 이를 측정할 수 있는 도구 `web-vitals`를 함께 소개합니다. 또, 추후 PageSpeed Insights나 Search Console 등도 각각 대응할 예정이라고 합니다.

- [GoogleChrome/web-vitals: Essential metrics for a healthy site.](https://github.com/GoogleChrome/web-vitals "GoogleChrome/web-vitals: Essential metrics for a healthy site.")
- [GoogleChrome/web-vitals-extension: A Chrome extension to measure essential metrics for a healthy site](https://github.com/GoogleChrome/web-vitals-extension "GoogleChrome/web-vitals-extension: A Chrome extension to measure essential metrics for a healthy site")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## rinsuki/play-flv-in-browser: Play FLV in Browser!
[github.com/rinsuki/play-flv-in-browser](https://github.com/rinsuki/play-flv-in-browser "rinsuki/play-flv-in-browser: Play FLV in Browser!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flash</span> <span class="jser-tag">video</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

ffmepg를 WebAssembly로 컴파일 한 버전을 이용해 flv/mp4를 브라우저에서 재생하는 데모입니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## antfu/i18n-ally: 🌍 All in one i18n extension for VS Code
[github.com/antfu/i18n-ally](https://github.com/antfu/i18n-ally "antfu/i18n-ally: 🌍 All in one i18n extension for VS Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">i18n</span> <span class="jser-tag">Extension</span> <span class="jser-tag">EmEditor</span></p>

i18n 편집 시스템을 제공하는 VS Code 확장 플러그인입니다.
에디터 상에서 번역키 대신에 번역 텍스트를 표시하는 등 지역화를 위한 기능을 제공합니다.
Vue, React 등 다양한 프레임워크 환경을 지원합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## addaleax/gen-esm-wrapper: Generate ESM wrapper files for CommonJS modules
[github.com/addaleax/gen-esm-wrapper](https://github.com/addaleax/gen-esm-wrapper "addaleax/gen-esm-wrapper: Generate ESM wrapper files for CommonJS modules")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span></p>

CommonJS에서 ESM Wrapper를 생성하는 도구입니다.


----

## jesseduffield/lazynpm: terminal UI for npm
[github.com/jesseduffield/lazynpm](https://github.com/jesseduffield/lazynpm "jesseduffield/lazynpm: terminal UI for npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">UI</span></p>

lazygit, lazydocker와 비슷한 npm 터미널 UI 도구입니다.
패키지 정보 표시, 패키지 관리, 스크립트를 실행 등의 기능을 제공합니다.


----

## Quantum JavaScript (Q.js)
[quantumjavascript.app/](https://quantumjavascript.app/ "Quantum JavaScript (Q.js)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

양자 회로 시뮬레이터 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## Tackling TypeScript: Upgrading from JavaScript
[exploringjs.com/tackling-ts/](https://exploringjs.com/tackling-ts/ "Tackling TypeScript: Upgrading from JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

Dr. Axel가 집필한 TypeScript 입문서입니다.


----
