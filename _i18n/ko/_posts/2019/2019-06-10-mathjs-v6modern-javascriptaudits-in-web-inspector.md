---
title: "2019-06-10: mathjs v6, Modern JavaScript 패키지 배포, Audits in Web Inspector"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-06-10T16:21:33.839Z
category: JSer
tags:
- mathjs
- Safari
- npm

---

JSer.info #439 - 수치 계산 라이브러리 [Math.js](https://mathjs.org/) v6가 릴리스됐습니다.

- [mathjs v6: a monolith turned modular - Jos de Jong](https://josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/)

Math.js는 200개 이상 기능을 제공하고 있으며 이에 따라 파일 크기가 137kB(gzip)에 달합니다.
따라서 v6에서는 필요한 기능만 모듈로 사용할 수 있도록 구조적인 변경이 이뤄졌습니다.
다음과 같이 작성할 경우 필요한 것 이외의 코드는 삭제되거나 트리쉐이킹 가능하도록 [`"module"`](https://github.com/rollup/rollup/wiki/pkg.module) 필드가 추가됐습니다.

```js
import { log } from "mathjs";

console.log(log(10))
``` 

또, 전역 설정이 아닌 `create` 함수를 이용해 독자적인 의존과 설정을 이용해 특정 기능을 생성할 수 있는 기능도 추가됐습니다.
이 외에도 BigNumber를 지원하지 않는 경량화 된 `mathjs/number`도 사용할 수 있습니다.

이와 함께 패키지 배포 방법에 대해 작성한 [Enabling Modern JavaScript on npm](https://jasonformat.com/enabling-modern-js-on-npm/)도 살펴보면 좋을 것 같습니다. Modern JavaScript는 ES2015 이후의 문법으로 작성된 코드 정도로 이해할 수 있습니다. 하지만 현재 npm에 배포되고 있는 많은 패키지는 ES5로 변환 된 것으로, 패키지 사용자는 현대적인 버전을 선택하지 못하고 ES5로 변환된 코드를 강제적으로 사용해야 하는 문제에 대해 작성돼 있습니다.

이 문제를 해결하기 위해서 웹팩이나 롤업에서는 `package.json`의 `"module"` 필드를 대응하고 패키지 이용자가 두 패키지 중 하나를 선택할 수 있도록 지원합니다. 
또, 해당 글에서는 [Microbundle](https://github.com/developit/microbundle)이나 [@pika/pack](https://www.pikapkg.com/blog/introducing-pika-pack/) 등 Modern JavaScript를 패키지로 배포할 수 있는 도구도 함께 소개하면서 이들 도구의 에코시스템이 아직 성숙하지 못한 부분에 대해서도 이야기하고 있습니다.

----

[Audits in Web Inspector | WebKit](https://webkit.org/blog/8935/audits-in-web-inspector/)에는 [Safari Technology Preview 75](https://webkit.org/blog/8594/release-notes-for-safari-technology-preview-75/)에 추가된 Safari의 Audit Tab에 대해 작성돼 있습니다.

접근성에 관한 기본적인 Audit 규칙이 정의돼 있으므로 접근성 검사가 가능합니다.
또, 이 Audit 탭에서는 Test Case Format에 맞춰 작성된 JSON을 읽어들여 임의의 검사 도구를 정의할 수도 있습니다.
[Creating Web Inspector Audits | WebKit](https://webkit.org/blog/8937/creating-web-inspector-audits/)에는 ESLint를 사용해 `*.js` 파일을 검사하는 규칙을 정의하고 이를 Audit 탭을 통해 실행하는 방법이 소개돼 있습니다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Node v12.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.4.0/](https://nodejs.org/en/blog/release/v12.4.0/ "Node v12.4.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.4.0이 릴리스 됐습니다.
`import` 문으로 JSON을 불러올 수 있는 `--experimental-json-modules` 플래그와 V8 heap profiler를 다루는 `--heap-prof` 플래그가 추가됐습니다.


----

## mathjs v6: a monolith turned modular - Jos de Jong
[josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/](https://josdejong.com/blog/2019/06/08/mathjs-v6-a-monolith-turned-modular/ "mathjs v6: a monolith turned modular - Jos de Jong")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

matchjs v6이 릴리스됐습니다.
각 기능을 모듈 단위로 가져와 사용할 수 있도록 구조를 변경했으며 전역 설정이 아닌 `create` 함수를 이용해 독자적인 의존과 설정을 이용해 특정 기능을 생성할 수 있도록 기능이 추가됐습니다. 또, BigNumber를 지원하지 않고 순수 `number` 처리만 지원하는 경량화 버전도 포함됐습니다.

- [mathjs/HISTORY.md at develop · josdejong/mathjs](https://github.com/josdejong/mathjs/blob/develop/HISTORY.md#2019-06-08-version-600 "mathjs/HISTORY.md at develop · josdejong/mathjs")

----

## Storybook 5.1
[medium.com/storybookjs/storybook-5-1-50afd02b5bbb](https://medium.com/storybookjs/storybook-5-1-50afd02b5bbb "Storybook 5.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">開発環境</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Stroybook 5.1이 릴리스됐습니다.
React Native를 다시 지원하며 A11y addon이 개선됐고 Context addon과 TypeScrip 용 preset이 추가됐습니다.

- [Real-time accessibility testing with Storybook](https://medium.com/storybookjs/instant-accessibility-qa-linting-in-storybook-4a474b0f5347 "Real-time accessibility testing with Storybook")
- [Intro to Presets](https://storybook.js.org/docs/presets/introduction/ "Intro to Presets")

----

## Release v3.0.0 · mqttjs/MQTT.js
[github.com/mqttjs/MQTT.js/releases/tag/v3.0.0](https://github.com/mqttjs/MQTT.js/releases/tag/v3.0.0 "Release v3.0.0 · mqttjs/MQTT.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MQTT.js 3.0.0이 릴리스 됐습니다.
MQTT 5.0을 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## Audits in Web Inspector | WebKit
[webkit.org/blog/8935/audits-in-web-inspector/](https://webkit.org/blog/8935/audits-in-web-inspector/ "Audits in Web Inspector | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Safari의 개발자 도구에 추가된 Audit 탭을 소개합니다.
접근성에 관한 기본적인 Audit 규칙이 정의돼 있어 접근성 검사가 가능하며 사용자가 직접 임의의 검사 도구를 정의할 수도 있습니다.
[Creating Web Inspector Audits | WebKit](https://webkit.org/blog/8937/creating-web-inspector-audits/ "Creating Web Inspector Audits | WebKit")에는 하나의 예로 `*.js` 파일을 ESLint 검사하는 Audit 규칙을 작성하는 방법이 소개돼 있습니다.

----

## An introduction to the MediaRecorder API - Twilio
[www.twilio.com/blog/mediastream-recording-api](https://www.twilio.com/blog/mediastream-recording-api "An introduction to the MediaRecorder API - Twilio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

MediaRecorder API를 이용한 음성 녹음과 다운로드 기능을 구현하는 튜토리얼입니다.


----

## ECMAScript proposal updates @ 2019-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2019/06/09/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2019/06/09/ecmascript-proposal-updates "ECMAScript proposal updates @ 2019-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2019년 6월 TC39 미팅에서 Stage가 변경된 ECMAScript Proposal이 정리돼 있습니다.
Dynamic Import가 드디어 Stage 4가 됐습니다.


----

## Dive into IndexedDB
[flaviocopes.com/indexeddb/](https://flaviocopes.com/indexeddb/ "Dive into IndexedDB")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Promise 기반 IndexedDB 랩퍼인 `idb`를 활용해 작성된 IndexedDB 튜토리얼 글입니다.
데이터 추가, 삭제, 마이그레이션 방법에 대해 작성돼 있습니다.

- [jakearchibald/idb: IndexedDB, but with promises](https://github.com/jakearchibald/idb "jakearchibald/idb: IndexedDB, but with promises")

----

## Enabling Modern JavaScript on npm
[jasonformat.com/enabling-modern-js-on-npm/](https://jasonformat.com/enabling-modern-js-on-npm/ "Enabling Modern JavaScript on npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">npm</span></p>

npm에 현대적인 자바스크립트를 패키지로 공개하는 방법을 소개합니다.
번들 도구의 변화에 의해, ES5로 변환된 파일만 배포하면 사용자가 최적화할 수 없는 문제와 `package.json`의 `"main"`, `"module"`, `"unpkg"` 필드와 패키지 개발자가 배포 시 주의할 점 등에 대해 작성돼 있습니다.
또, microbundle이나 `@pika/pack` 등의 패키지 배포 보조 도구도 함께 이야기합니다.


----

## CSS Grid Level 2 - subgrid is coming to Firefox - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/06/css-grid-level-2-subgrid-is-coming-to-firefox/](https://hacks.mozilla.org/2019/06/css-grid-level-2-subgrid-is-coming-to-firefox/ "CSS Grid Level 2 - subgrid is coming to Firefox - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Grid Level 2의 서브그리드를 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Inside Frontend #3 - YouTube
[www.youtube.com/playlist?list&#x3D;PLZFhK-XSlb82hef6Sxyqcc-6e8xVTbaIE&amp;app&#x3D;desktop](https://www.youtube.com/playlist?list=PLZFhK-XSlb82hef6Sxyqcc-6e8xVTbaIE&app=desktop "Inside Frontend #3 - YouTube")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">video</span> <span class="jser-tag">이벤트</span></p>

Inside Frontend #3의 영상이 공개됐습니다.

- [Inside Frontend | 2019년 5월 18일 Frontend 컨퍼런스를 시부야 Abema Towers에서 개최](https://inside-frontend.com/ "Inside Frontend | 2019년 5월 18일 Frontend 컨퍼런스를 시부야 Abema Towers에서 개최")(컨퍼런스 공식 사이트)

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## npmfs - home
[npmfs.com/](https://npmfs.com/ "npmfs - home")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span></p>

npm에 공개돼 있는 패키지의 소스 코드 뷰어 서비스입니다.
특정 버전의 코드를 살펴보거나 버전 간 코드의 차이를 비교해 볼 수 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## urql
[formidable.com/open-source/urql/](https://formidable.com/open-source/urql/ "urql")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React Hooks에 대응한 GraphQL React 라이브러리입니다.
리액트 컴포넌트를 이용해 쿼리의 실행 및 상태와 결과를 다룰 수 있습니다.

- [Urql, Grown Up](https://formidable.com/open-source/urql/ "Urql, Grown Up")

----

## lukeed/tinydate: A tiny (340B) reusable date formatter. Extremely fast!
[github.com/lukeed/tinydate](https://github.com/lukeed/tinydate "lukeed/tinydate: A tiny (340B) reusable date formatter. Extremely fast!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

파일 크기가 작은 Date Formatter 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## 실천 TypeScript ~ BFF와 Next.js&Nuxt.js의 타입 정의 ~ | 요시이 타케후미 | 책 | 통신 판매 | Amazon
[www.amazon.co.jp/dp/483996937X/](https://www.amazon.co.jp/dp/483996937X/ "실천 TypeScript ~ BFF와 Next.js&Nuxt.js의 타입 정의 ~ | 요시이 타케후미 | 책 | 통신 판매 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2019년 6월 26일에 출간 예정인 TypeSctipt와 Next.js, Nuxt.js를 주제로 한 도서입니다.


----
