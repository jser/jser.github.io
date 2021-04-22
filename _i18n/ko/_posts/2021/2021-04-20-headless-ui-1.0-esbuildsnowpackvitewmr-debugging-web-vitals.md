---
title: "2021-04-20:  Headless UI 1.0, esbuild/Snowpack/Vite/wmr 비교, debugging Web Vitals"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-04-20T02:45:24.600Z
category: JSer
tags:
- Tools
- performance
- Chrome
- browser
- TypeScript

---

JSer.info #536 - React와 Vue를 지원하는 스타일 없는 컴포넌트 라이브러리 Headless UI 1.0 릴리스됐다.

- [Headless UI v1.0 – Tailwind CSS](https://blog.tailwindcss.com/headless-ui-v1)
- [tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.](https://github.com/tailwindlabs/headlessui)

Headless UI는 Tailwind CSS와 함게 사용할 목적으로 개발됐기 때문에 컴포넌트 자체에 스타일이 포함돼 있지 않다.
Headless UI는 React와 Vue 구현이 각각 존재하며 이번 릴리스를 통해 각 패키지도 1.0 릴리스 됐다.

----

[Comparing the New Generation of Build Tools | CSS-Tricks](https://css-tricks.com/comparing-the-new-generation-of-build-tools/)

esbuild / Snowpack / Vite / wmr 빌드 도구 비교 글.

각 도구의 특징 및 사용법, 지원하는 파일 형식, production build 등을 비교한다.
esbuild는 조금 레이어가 다른 느낌이 있지만 어쨋든 각 도구의 특징이 잘 정리돼 있다.

----

Google 검색 결과 순위에 page experience라는 Web Vitals를 기반으로 한 지표가 6월 부터 포함될 예정.

- [Timing for bringing page experience to Google Search](https://developers.google.com/search/blog/2020/11/timing-for-page-experience)
- [More time, tools, and details on the page experience update](https://developers.google.com/search/blog/2021/04/more-details-page-experience)

이에 맞춰 Web Vitals 방법 및 도구 등이 함께 공개됐다.

- [Debug Web Vitals in the field](https://web.dev/debug-web-vitals-in-the-field/)
  - Web Vitals의 지표 디버깅 방법
- [An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine](https://www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/)
  - Web Vitals 전체적인 설명
- [Cumulative Layout Shift Debugger (CLS) - webvitals.dev](https://webvitals.dev/cls)
  - CLS 디버깅 도구
- [Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores](https://waterfaller.dev/)
  - 페이지 로드 단계를 워터폴로 표시하여 Web Vitals 지표 등을 어떻게 개선할지 제안하는 도구

----

<h1 class="site-genre">헤드라인</h1>

----

## Deno 1.9 Release Notes | Deno Blog
[deno.com/blog/v1.9](https://deno.com/blog/v1.9 "Deno 1.9 Release Notes | Deno Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.9 릴리스.
HTTP/2 웹 서버 구현, opcall 개선, Blob URL 지원.
`--allow-env`와 `--allow-run`으로 개별 지정이 가능하도록, `--prompt`로 인터렉티브하게 퍼미션 허가할 수 있도록.
`Deno.listenTls`에서 ALPN 지원, tsconfig.json의 `useDefineForClassFields`을 기본 타입 옵션으로 추가


----

## New in Chrome 90 - Chrome Developers
[developer.chrome.com/blog/new-in-chrome-90/](https://developer.chrome.com/blog/new-in-chrome-90/ "New in Chrome 90 - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 90 릴리스.
`overflow: clip` 지원, AV1 Encoder 지원, Declarative Shadow DOM 지원.
Feature Policy를 Permissions Policy로 이름 변경, 주소바의 기본 프로토콜을 `https`로 변경.


----

## Headless UI v1.0 – Tailwind CSS
[blog.tailwindcss.com/headless-ui-v1](https://blog.tailwindcss.com/headless-ui-v1 "Headless UI v1.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">lib</span></p>

Headless UI 1.0 릴리스.
React와 Vue를 지원하는 스타일 없는 UI 컴포넌트 구현으로 Tailwind CSS와 함께 사용할 목적으로 개발됐다.

- [tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.](https://github.com/tailwindlabs/headlessui "tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.")

----

## Release v6.0.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v6.0.0](https://github.com/pnpm/pnpm/releases/tag/v6.0.0 "Release v6.0.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 6.0.0 릴리스.
Node.js 10 지원 종료, `pre` / `post` script를 자동으로 실행하지 않도록, lockfil 포멧 변경, `pnpx`가 자동으로 패키지를 설치하지 않도록.
`pnpm link`가 `--global`를 붙인 경우 global modules과 링크하도록, `pnpm fetch` 명령어 추가.


----

## helmet/CHANGELOG.md at main · helmetjs/helmet
[github.com/helmetjs/helmet/blob/main/CHANGELOG.md#450---2021-04-17](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#450---2021-04-17 "helmet/CHANGELOG.md at main · helmetjs/helmet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">express</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Express의 보안 헤더를 다루는 helmet 4.5.0 릴리스.
Cross-Origin isolation와 관련한 COEP, COOP, CORP 헤더 대응.

- [Making your website &amp;quot;cross-origin isolated&amp;quot; using COOP and COEP](https://web.dev/coop-coep/ "Making your website &amp;amp;quot;cross-origin isolated&amp;amp;quot; using COOP and COEP")

----

## React-pdf - Announcing react-pdf v2.0
[react-pdf.org/blog/announcing-react-pdf-v2](https://react-pdf.org/blog/announcing-react-pdf-v2 "React-pdf - Announcing react-pdf v2.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">PDF</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React로 PDF를 작성할 수 있는 react-pdf v2.0 릴리스.
레이아웃과 렌더링 분리, SVG 지원, Hooks API 추가.


----

## Never too late for Firefox 88 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/04/never-too-late-for-firefox-88/](https://hacks.mozilla.org/2021/04/never-too-late-for-firefox-88/ "Never too late for Firefox 88 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 88 릴리스.
`:user-valid`와 `:user-invalid` 구현, `RegExp#indices` 구현, `AbortSignal.abort()` 구현, FTP 지원 무효화.

- [Firefox 88 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/88 "Firefox 88 for developers - Mozilla | MDN")
- [Firefox 88.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/88.0/releasenotes/ "Firefox 88.0, See All New Features, Updates and Fixes")

----
<h1 class="site-genre">아티클</h1>

----

## Comparing the New Generation of Build Tools | CSS-Tricks
[css-tricks.com/comparing-the-new-generation-of-build-tools/](https://css-tricks.com/comparing-the-new-generation-of-build-tools/ "Comparing the New Generation of Build Tools | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

esbuild, Snowpack, Vite, wmr를 비교한 글.
각 도구의 특징과 사용법, 지원하는 파일, production build 등에 대해서 비교한다.


----

## Introducing CSS Grid Inspector | WebKit
[webkit.org/blog/11588/introducing-css-grid-inspector/](https://webkit.org/blog/11588/introducing-css-grid-inspector/ "Introducing CSS Grid Inspector | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Safari Technology Preview 123에 도입된 CSS Grid Inspector 소개.


----

## Real-world CSS vs. CSS-in-JS performance comparison - Tomas Pustelnik&#039;s personal website
[pustelto.com/blog/css-vs-css-in-js-perf/](https://pustelto.com/blog/css-vs-css-in-js-perf/ "Real-world CSS vs. CSS-in-JS performance comparison - Tomas Pustelnik&#039;s personal website")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Styled Components를 사용한 CSS-in-JS와
linaria를 사용한 CSS 파일 추출(분리)한 경우의 성능을 비교한 글.
사이즈, Lighthouse 등을 사용한 Runtime 성능 측정.


----

## HTML Inputs and Labels: A Love Story | CSS-Tricks
[css-tricks.com/html-inputs-and-labels-a-love-story/](https://css-tricks.com/html-inputs-and-labels-a-love-story/ "HTML Inputs and Labels: A Love Story | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

Label과 Input을 주제로한 글.
접근성을 고려해서 라벨을 다루는 방법.


----

## Debug Web Vitals in the field
[web.dev/debug-web-vitals-in-the-field/](https://web.dev/debug-web-vitals-in-the-field/ "Debug Web Vitals in the field")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Web Vitals의 지표를 JavaScript로 가져와 실제로 어떤 요소가 스코어에 영향을 주고 있는지 디버깅 하는 방법 소개.

- [GoogleChromeLabs/web-vitals-report: Measure and report on your Web Vitals data in Google Analytics](https://github.com/GoogleChromeLabs/web-vitals-report "GoogleChromeLabs/web-vitals-report: Measure and report on your Web Vitals data in Google Analytics")

----

## An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine
[www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/](https://www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/ "An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Web Vitals를 주제로한 글.
Web Vitals의 LCP/FID/CLS 설명, Lighthouse / Google Search Console의 보고서 읽는법, CrUX 데이터 읽는법 및 분석 방법 등 소개.


----

## Slow and Steady: Converting Sentry’s Entire Frontend to TypeScript | Product Blog • Sentry
[blog.sentry.io/2021/04/12/slow-and-steady-converting-sentrys-entire-frontend-to-typescript](https://blog.sentry.io/2021/04/12/slow-and-steady-converting-sentrys-entire-frontend-to-typescript "Slow and Steady: Converting Sentry’s Entire Frontend to TypeScript | Product Blog • Sentry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">refacoring</span></p>

Sentry 코드를 TypeScript로 마이그레이션 한 것에 대해.
마이그레이션 전략으로 교육, 새로운 코드는 TS로 작성하기, 기존 코드를 점진적으로 TS로 변환해 나가기. 
천천히 변환해 나가는 것. 조금씩 복잡한 타입으로 변경해 나가기, TypeScript를 최신으로 유지하기 등 마이그레이션 진행 중 배운 교훈이나 느낌을 이야기한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores
[waterfaller.dev/](https://waterfaller.dev/ "Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Web Vitals 지표와 리소스 로드 과정을 폭포수 차트로 표시하여 왜 Slowdown 되는지 원인을 알아보고 개선 방법을 제시하는 도구.


----

## Cumulative Layout Shift Debugger (CLS) - webvitals.dev
[webvitals.dev/cls](https://webvitals.dev/cls "Cumulative Layout Shift Debugger (CLS) - webvitals.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">webservice</span></p>

Cumulative Layout Shift(CLS) 디버깅 도구.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ivanhofer/typesafe-i18n
[github.com/ivanhofer/typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n "ivanhofer/typesafe-i18n")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

의존 모듈 없는 i18n 라이브러리.
TypeScript를 사용한 번역 누락 검사, plural 등의 transformer 지원, rollup 및 CLI를 사용한 최적화 지원.

----

## lukejacksonn/servor: Dependency free file server for single page app development
[github.com/lukejacksonn/servor](https://github.com/lukejacksonn/servor "lukejacksonn/servor: Dependency free file server for single page app development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

의존 모듈 없는 로컬 서버 라이브러리.



----

## callstack/linaria: Zero-runtime CSS in JS library
[github.com/callstack/linaria](https://github.com/callstack/linaria "callstack/linaria: Zero-runtime CSS in JS library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span></p>

CSS-in-JS 방식으로 스타일을 작성하고 그 스타일을 CSS 파일로 추출(분리)하는 라이브러리 도구.


----
