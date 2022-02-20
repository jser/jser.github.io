---
title: "2022-01-11: 글로벌 사이트 관점에서 Core Web Vitals, 2021 JavaScript Rising Stars, colors.js의 인시던트 대응"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-01-11T03:01:30.504Z
category: JSer
tags:
- performance
- browser
- CSS
- Tools
- debug

---

JSer.info #574 - [Improving Core Web Vitals, A Smashing Magazine Case Study](https://www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/)에는 Smashing Magazine의 Core Web Vitals(LCP/FID/CLS) 스코어를 개선했는지 소개돼 있다.

Core Web Vitals은 Google의 검색 지표로 사용되고 있다.
또, Google Search Console를 통해 글로벌한 크롬 사용자를 기반으로한 Core Web Vitals 스코어를 확인할 수 있으며 이 값은 [Chrome User Experience Report ](https://developers.google.com/web/tools/chrome-user-experience-report) 데이터를 근거로 하고 있다.

사이트의 LCP를 개선 했으나, 왜인지 Google Search Console을 통해서는 개선된 결과를 확인할 수 없었던 문제를 추적한 내용이 정리돼 있다.
원인 중 하나로 Smashing Magazine은 글로벌 사이트이며 Google Search Console 스코어는 글로벌한 데이터를 한데 정리한 것이기 때문에 사용자가 많은 특정 국가에서 스코어가 나쁘면 전체 점수에도 영향을 줄 수 있다는 점을 들고 있다.

----

GitHub Star 수를 기준으로 순위를 정리한 2021년도 JavaScript Rising Stars가 공개됐다.

- [2021 JavaScript Rising Stars](https://risingstars.js.org/2021/en)
- 한국어: [JavaScript 라이징스타 2021](https://risingstars.js.org/2021/ko)

GitHub Star는 실제 인기 및 이용수와 반드시 일치하진 않지만, 각각 항목 별로 간단한 코멘트도 붙어 있기 때문에 한번 살펴보기에 좋은 자료인 듯 하다.

----

[colors 등의 npm 패키지에 악의가 담긴 코드가 포함된 문제에 대해서](https://zenn.dev/azu/articles/d56615b2e11ad1)(일본어)에는 `colors`라는 npm 패키지에 DoS 공격 코드가 포함된 내용이 patch 버전으로 공개됐던 소동이 소개돼 있다.

npm은 [leftpad라고 불리는 문제](https://web.archive.org/web/20160323000303/https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c)를 계기로 패키지의 Owner라 하더라도 공개 후 24 시간 경과하게 되면 비공개 전환 시 문의 과정을 필수로 거치도록 개정됐다(관련한 조건이 2020년에 추가됐다).

- [npm Blog Archive: changes to npm’s unpublish policy](https://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy)
- [npm Blog Archive: Changes to npm Unpublish Policy - January 2020](https://blog.npmjs.org/post/190553543620/changes-to-npmunpublish-policy-january-2020.html)

또, npm이나 yarn 등에서는 패키지 잠금 파일(lock file)이 기본적으로 사용되기 때문에 프로젝트에서는 버전을 고정할 수 있어 관련한 영향 범위가 leftpad 사건에 비해 상대적으로 작아졌다.
한편, `colors`를 새로 설치하거나 업데이트를 할 경우 문제가 있는 patch 버전이 semver에 의해 선택 돼 버리는 문제가 발생한다.

이 글에는 npm 패키지의 직/간접적 의존 검사 방법과 Yarn의 `resolutions`, npm 8.3+의 `overrides`를 통한 명시적인 버전 고정 방법 등에 대해서 작성돼 있다.

현재(2022년 1월 11일)는 문제가 있던 `colors`의 버전은 npm에 의해 취소된 상황이다.
colors.js의 향후에 대해서는 다음 Issue를 살펴보길 바란다.

- [(Semi-Official) Status Update · Issue #317 · Marak/colors.js](https://github.com/Marak/colors.js/issues/317)

----

<h1 class="site-genre">헤드라인</h1>

----

## January 10th 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/jan-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/jan-2022-security-releases/ "January 10th 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js의 보안 내용이 수정된 12.x, 14.x, 16.x, 17.x가 각각 릴리스 됐다.
Subject Alternative Name (SAN) 관련 수정이 두 가지 포함돼 있으며 이 수정은 `--security-revert` 플래그를 이용해 되돌릴 수도 잇다.
또, Relative Distinguished Names 조작과 관려한 수정과 `console.table`의 Prototype Pollution 수정이 포함됐다.

- [Release 2022-01-10, Version 14.18.3 &#039;Fermium&#039; (LTS), @richardlau · nodejs/node](https://github.com/nodejs/node/releases/tag/v14.18.3 "Release 2022-01-10, Version 14.18.3 &amp;#039;Fermium&amp;#039; (LTS), @richardlau · nodejs/node")

----

## Chromium Blog: Chrome 98 Beta: Color Gradient Vector Fonts, Region Capture Origin Trial, and More
[blog.chromium.org/2022/01/chrome-98-beta-color-gradient-vector.html](https://blog.chromium.org/2022/01/chrome-98-beta-color-gradient-vector.html "Chromium Blog: Chrome 98 Beta: Color Gradient Vector Fonts, Region Capture Origin Trial, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 98 beta 릴리스.
COLRv1 Color Gradient Vector Fonts 지원, Chrome 버전 100에 대한 사용자 에이전트를 테스트할 수 있는 플래그 추가.
Origin Trial로서 Region Capture 추가.
그 외로는 `contains-intrinsic-size: auto` 지원, `AudioContext.outputLatency` 지원, `color-scheme`에서의 `only` 지원.
`structuredClone()` 지원, Subresources에서 Private Network로 접근할 때 Preflight Request가 요구되도록 변경.


----
<h1 class="site-genre">아티클</h1>

----

## Improving Core Web Vitals, A Smashing Magazine Case Study
[www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/](https://www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/ "Improving Core Web Vitals, A Smashing Magazine Case Study")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Core Web Vitals의 개선과 CrUX의 측정을 토대로 드러난 문제를 추적하여 정리한 글.
LCP 등을 개선했으나 CrUX의 데이터는 개선되지 않았음을 의아하게 여겨 파고들어 특정 지역의 데이터에 의해 통계 데이터가 왜곡됐음을 파악하게 된 흐름과 방법.
CDN이 커버하지 못하는 지역 등이 문제가 되고 있었기 때문에 `SaveData` 헤더와 `prefers-reduced-data`를 기반으로 Web Font 로드 부하를 줄였다고 한다.


----

## 2021 JavaScript Rising Stars
[risingstars.js.org/2021/en](https://risingstars.js.org/2021/en "2021 JavaScript Rising Stars")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">Github</span></p>

2021년 GitHub Star를 기준으로한 JavaScript 관련 도구나 라이브러리 등의 순위.
각 항목별 순위와 간단한 코멘트로 함께 소개하고 있어 간단히 살펴보기에 흥미로운 자료.

- [JavaScript 라이징 스타 2021](https://risingstars.js.org/2021/ko "JavaScript 라이징 스타 2021")

----

## Container Queries | 12 Days of Web
[12daysofweb.dev/2021/container-queries/](https://12daysofweb.dev/2021/container-queries/ "Container Queries | 12 Days of Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Container query 정의, 이용 방법, 유스케이스등 소개.


----

## Introducing fuite: a tool for finding memory leaks in web apps | Read the Tea Leaves
[nolanlawson.com/2021/12/17/introducing-fuite-a-tool-for-finding-memory-leaks-in-web-apps/](https://nolanlawson.com/2021/12/17/introducing-fuite-a-tool-for-finding-memory-leaks-in-web-apps/ "Introducing fuite: a tool for finding memory leaks in web apps | Read the Tea Leaves")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span> <span class="jser-tag">Tools</span></p>

메모리-릭 디버깅 도구 fuite 소개.
Puppeteer를 사용해 횟수를 지정하여 시나리오 기반 조작을 반복하고, 반환 결과를 토대로 메모리-릭을 확인할 수 있다.
실행 시 Break Point를 걸어 처리를 멈추고 크롬 개발자 도구와 연계하여 디버깅 할 수 있는 도구.

- [nolanlawson/fuite: A tool for finding memory leaks in web apps](https://github.com/nolanlawson/fuite "nolanlawson/fuite: A tool for finding memory leaks in web apps")
- [Fixing memory leaks in web applications | Read the Tea Leaves](https://nolanlawson.com/2020/02/19/fixing-memory-leaks-in-web-applications/ "Fixing memory leaks in web applications | Read the Tea Leaves")
- [Debugging a memory leak with fuite - YouTube](https://www.youtube.com/watch?v=H0BHL2lo89M "Debugging a memory leak with fuite - YouTube")

----

## Web Performance Calendar » JS Self-Profiling API In Practice
[calendar.perfplanet.com/2021/js-self-profiling-api-in-practice/](https://calendar.perfplanet.com/2021/js-self-profiling-api-in-practice/ "Web Performance Calendar » JS Self-Profiling API In Practice")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScript Self-Profiling API를 자세히 설명하는 글.
샘플링된 프로파일을 얻을 수 있는 API로, RUM과 같은 실사용자(end user)의 실행 결과를 취득할 수 있다.
Document Policy를 통한 활성화, API 사용 방법, 유스케이스, 프로파일의 데이터 형식과 취득할 수 있는 데이터의 제한 등.
CORS에 대응하고 있지 않은 Cross-Origin Scripts의 JavaScript 함수는 프로파일 상에서는 식별할 수 없다는 점과 JS 이외의 데이터는 프로파일에 포함되지 않는다는 점 등을 설명한다.

- [WICG/js-self-profiling: Proposal for a programmable JS profiling API for collecting JS profiles from real end-user environments](https://github.com/WICG/js-self-profiling "WICG/js-self-profiling: Proposal for a programmable JS profiling API for collecting JS profiles from real end-user environments")

----

## Frontend Web Performance: The Essentials \[0\] | by Matthew Costello | Dec, 2021 | Medium
[medium.com/@matthew.costello/frontend-web-performance-the-essentials-0-61fea500b180](https://medium.com/@matthew.costello/frontend-web-performance-the-essentials-0-61fea500b180 "Frontend Web Performance: The Essentials \[0\] | by Matthew Costello | Dec, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

웹 성능과 브라우저 렌더링을 주제로 한 글.
Chrome 개발자 도구에서 Layout, Paint, Composite는 어떤 렌더링 스텝으로 이뤄지는지 살펴볼 수 있다.
CSS Animation을 예로 Chrome 개발자 도구로 각각의 렌더링 스텝을 가시화 하는 방법이 작성돼 있다.


----

## colors 등의 npm 패키지에 악의가 담긴 코드가 포함된 문제에 대해서(일본어)
[zenn.dev/azu/articles/d56615b2e11ad1](https://zenn.dev/azu/articles/d56615b2e11ad1 "colorsなどのnpmパッケージに悪意あるコードが含まれている問題について")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

colors.js에 DoS 공격 코드를 넣은 버전이 publish 돼 버린 문제를 다루는 글.
npm 패키지의 적/간접적 의존 검사 방법과 Yarn의 `resolutions`, npm 8.3+의 `overrides`를 통한 패키지 고정 방법 소개.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## shiguredo/media-processors: Media Processors(일본어)
[github.com/shiguredo/media-processors](https://github.com/shiguredo/media-processors "shiguredo/media-processors: Media Processors")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">video</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

포커스 아웃이나 노이즈 억제(noise suppression) 등의 처리를 브라우저에서 수행하는 라이브러리 소개.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## mozilla/glean: Modern cross-platform telemetry
[github.com/mozilla/glean](https://github.com/mozilla/glean "mozilla/glean: Modern cross-platform telemetry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">kotlin</span> <span class="jser-tag">swift</span> <span class="jser-tag">python</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span> <span class="jser-tag">Mozilla</span> <span class="jser-tag">Rust</span></p>

Rust / Kotlin / Swift / Python / JavaScript(브라우저, 브라우저 확장, Node.js) / Qt를 지원하는 크로스 플랫폼 Telemetry SDK.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## AntoineW/luge: Luge
[github.com/AntoineW/luge](https://github.com/AntoineW/luge "AntoineW/luge: Luge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">animation</span></p>

HTML에 속성을 지정하는 방식으로 애니메이션을 설정할 수 있는 라이브러리.


----
<h1 class="site-genre">도서</h1>

----

## New JavaScript features • JavaScript for impatient programmers (ES2022 edition)
[exploringjs.com/impatient-js/ch\_new-javascript-features.html#new-in-es2022](https://exploringjs.com/impatient-js/ch_new-javascript-features.html#new-in-es2022 "New JavaScript features • JavaScript for impatient programmers (ES2022 edition)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

JavaScript for impatient programmers (ES2022 edition) 릴리스.
ES2022의 Private / Public Fields, Top-level await, Error Cause.
Array와 String의 `.at()` 메서드, RegExp match indices, `Object.hasOwn()` 메서드가 추가된 버전.


----
