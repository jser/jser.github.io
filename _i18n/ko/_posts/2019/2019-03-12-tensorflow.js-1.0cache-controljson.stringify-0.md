---
title: "2019-03-12: TensorFlow.js 1.0, Cache-Control 설명, `JSON.stringify(-0)`"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-03-12T00:20:50.340Z
category: JSer
tags:
- TensorFlow
- HTTP
- JSON

---

JSer.info #426 - TensorFlow 모델을 브라우저와 Node.js에서도 사용할 수 있는 TensorFlow.js 1.0이 릴리스됐습니다.

- [Release 1.0.0 · tensorflow/tfjs](https://github.com/tensorflow/tfjs/releases/tag/v1.0.0)

1.0에 `Tensor.array()`와 `Tensor.arraySync()`가 추가됐고 API의 이름이 변경되는 등 비호환적 변경사항이 포함돼 있습니다.
또, 초기 릴리스한 버전에 비해 성능이 크게 개선 됐습니다.


----

[Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts](https://csswizardry.com/2019/03/cache-control-for-civilians/ "Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts")에는 `Cache-Control` HTTP 헤더에 관해 자세히 작성돼 있습니다.

`public`, `private`, `max-age`, `no-store`, `no-cache`, `immutable`, `stale-while-revalidate` 라는 각 프로퍼티의 동작 방식이나 유스케이를 설명합니다.
뿐만 아니라 Cache Busting 방법이나 `Clear-Site-Data` 헤더 그리고 라이브 전송 용 페이지 설정 등 다양한 내용을 다루고 있습니다.

----

## 이번주 이슈

ECMAScript 사양의 이슈로 `JSON.stringify(-0)`의 처리에 관한 이슈가 등록됐습니다.

- [Normative: Make `JSON.stringify(-0)` preserve the sign by mathiasbynens · Pull Request #1466 · tc39/ecma262](https://github.com/tc39/ecma262/pull/1466)

현재의 사양에서 `JSON.stringify(-0)`할 경우 `String(-0)`의 경우와 같은 로직으로 동작하므로 `-`를 무시하여 `"0"` 문자열이 반환됩니다.
한편,  `JSON.parse("-0")`을 할 경우엔 `-`를 고려하여 `-0`이 반환됩니다.

이로 인해 parse 한 후 stringify 한 결과를 본래의 값과 `Object.is`로 비교 시 일치하지 않는 경우가 있습니다.
이 사양은 JSON 포맷을 발견한 [douglascrockford/JSON-js](https://github.com/douglascrockford)에 근거한 것입니다.

```js
// 현재 사양
Object.is(JSON.parse(JSON.stringify(-0)), -0); // => false
```

`JSON.stringify(-0)`가 `"-0"`을 반환하도록 하는 사양을 수정한 PR이 등록됐습니다.

```js
// PR로 제안한 사양
Object.is(JSON.parse(JSON.stringify(-0)), -0); // => true
```

하지만 `===`로 비교할 때 `-0`과 `0` 차이를 무시하는 동작, `String()`의 동작 방식과 통일하는 문제 등이 제기 됐으며 `JSON.stringify(-0)`의 동작이 현업에서 그다지 문제될 일이 없다는 의견이 있어 일단은 PR이 취하됐습니다.

```js
// === 는 -0과 0의 차이를 무시함
JSON.parse(JSON.stringify(-0)) === -0; // => true
```

이 문제에 관심 있는 분들은 위 이슈를 살펴보면 좋을 것 같습니다. 
`===`와 `Object.is`의 비교 방식에 대해선 아래 문서를 통해 알 수 있습니다.

- [동치 비교 및 동일성 - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Equality_comparisons_and_sameness)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 1.0.0 · tensorflow/tfjs
[github.com/tensorflow/tfjs/releases/tag/v1.0.0](https://github.com/tensorflow/tfjs/releases/tag/v1.0.0 "Release 1.0.0 · tensorflow/tfjs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

TensorFlow.js 1.0이 릴리스됐습니다.
성능 개선이 이뤄졌고 `Tensor.array()`와 `Tensor.arraySync()`가 추가 됐습니다.


----

## Release: npm@6.9.0 - 📣 announcements - npm forum
[npm.community/t/release-npm-6-9-0/5911](https://npm.community/t/release-npm-6-9-0/5911 "Release: npm@6.9.0 - 📣 announcements - npm forum")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.9.0이 릴리스됐습니다.
지정한 날짜 보다 이전 버전을 설치하는 `--before` 옵션이 추가됐고 패키지의 이름을 alias 하여 설치할 수 있는 package alias를 지원합니다.


----

## rmdm/rmgr: Release resources gracefully
[github.com/rmdm/rmgr](https://github.com/rmdm/rmgr "rmdm/rmgr: Release resources gracefully")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

리소스를 관리하는 라이브러리 입니다.
리소스 별로 initialize와 dispose 시의 처리를 정의하고 리소스를 배포할 수 있는 라이브러리입니다.


----

## Marble.js 2.0 🔥 — reactive, better, functional, stronger
[medium.com/@jflakus/marble-2-reactive-better-functional-stronger-5924119d3098](https://medium.com/@jflakus/marble-2-reactive-better-functional-stronger-5924119d3098 "Marble.js 2.0 🔥 — reactive, better, functional, stronger")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

RxJS를 사용한 Node.js 용 HTTP 프레임워크인 Marble.js 2.0이 릴리스됐습니다. WebSockets 대응, Context를 사용한 DI 구조, io-ts를 사용한 검증(validation)을 지원합니다.


----

## jsdom/Changelog.md at master · jsdom/jsdom
[github.com/jsdom/jsdom/blob/master/Changelog.md#1400](https://github.com/jsdom/jsdom/blob/master/Changelog.md#1400 "jsdom/Changelog.md at master · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JSDOM 14.0.0이 릴리스됐습니다.
`JSDOM.fragment()`가 browsing context를 갖지 않는 framents를 생성하도록 변경됐으며 `element.blur()`가 회귀(regression) 수정됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts
[csswizardry.com/2019/03/cache-control-for-civilians/](https://csswizardry.com/2019/03/cache-control-for-civilians/ "Cache-Control for Civilians – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">article</span></p>

`Cache-Control` HTTP 헤더에 관한 설명 글입니다.
`public`, `private`, `max-age`, `no-store`, `no-cache`, `immutable`, `stale-while-revalidate` 등 각각 항목을 설명하고 Cache Busting 방법 등에 대해서 이야기합니다.


----

## JavaScript loose comparison (==) step by step
[felix-kling.de/js-loose-comparison/](https://felix-kling.de/js-loose-comparison/ "JavaScript loose comparison (==) step by step")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">spec</span></p>

`==`이 어떻게 값을 비교하는지 ECMAScript 사양에 정의된 알고리즘 단계에 따라 체크하는 도구입니다.


----

## What's New In DevTools (Chrome 74)  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/03/devtools](https://developers.google.com/web/updates/2019/03/devtools "What's New In DevTools (Chrome 74)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 74 개발자 도구 변경 사항을 정리한 글입니다. CSS property의 영향이 강조 표현되며 Lighthouse v4로 갱신됐습니다. 이어 WebSocket 바이너리 메시지 표현 기능이 추가됐으며 퍼포먼스 패널에서 Long task를 기록할 수 있게 됐습니다.


----

## A Complete Guide to useEffect — Overreacted
[overreacted.io/a-complete-guide-to-useeffect/](https://overreacted.io/a-complete-guide-to-useeffect/ "A Complete Guide to useEffect — Overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Hooks의 `useEffect` 동작과 사용 방법에 대해 설명하며 자주 있는 질문에 대해 이야기합니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Request Map Generator
[requestmap.webperf.tools/](http://requestmap.webperf.tools/ "Request Map Generator")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

지정한 URL의 요청 관계(흐름)을 맵으로 출력 / 시각화 하는 도구입니다.
WebPageTest 결과를 이용합니다.


----

## twbs/rfs: Automated responsive font sizes
[github.com/twbs/rfs](https://github.com/twbs/rfs "twbs/rfs: Automated responsive font sizes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">PostCSS</span></p>

반응형 폰트 사이즈를 지정하는 CSS 세트입니다. 
Sass, PostCSS, less, stylus 버전이 준비돼 있습니다.


----

## Feature policy
[featurepolicy.info/](https://featurepolicy.info/ "Feature policy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">example</span> <span class="jser-tag">document</span></p>

Feature Policy 데모 사이트입니다. 각각의 정책의 지원 상황과 문서, 샘플 등이 정리돼 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## dyatko/arkit: Visualises JavaScript, TypeScript and Flow codebases as meaningful and committable architecture diagrams
[github.com/dyatko/arkit](https://github.com/dyatko/arkit "dyatko/arkit: Visualises JavaScript, TypeScript and Flow codebases as meaningful and committable architecture diagrams")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">SVG</span> <span class="jser-tag">UML</span></p>

파일로 부터 아키텍처 다이어그램을 생성하는 도구입니다. 코드 베이스가 되는 파일을 지정해 그 구조를 Plant UML이나 SVG 등의 그림으로 변환해 줍니다.


----

## Introduction · AnyProxy
[anyproxy.io/en/](http://anyproxy.io/en/ "Introduction · AnyProxy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proxy</span> <span class="jser-tag">Tools</span></p>

HTTPS나 WebSocket 등에 대응한 로컬 프록시 도구입니다.
Proxy한 로그를 살펴볼 수 있는 GUI도 제공합니다.


----

## jaames/iro.js: 🎨 Color wheel widget for JavaScript - with zero dependencies and a lovely SVG-based UI
[github.com/jaames/iro.js](https://github.com/jaames/iro.js "jaames/iro.js: 🎨 Color wheel widget for JavaScript - with zero dependencies and a lovely SVG-based UI")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">color</span> <span class="jser-tag">library</span></p>

의존 모듈 없는 색상 추출 라이브러리입니다. SVG를 기반으로 한 색상 추출 UI를 제공합니다.


----

## vladocar/femtoJS: femtoJS - Really small JavaScript (ES6) library for DOM manipulation.
[github.com/vladocar/femtoJS](https://github.com/vladocar/femtoJS "vladocar/femtoJS: femtoJS - Really small JavaScript (ES6) library for DOM manipulation.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

jQuery와 비슷한 일부 DOM API를 제공하는 라이브러리입니다.
ES2015+를 지원하는 브라우저를 대상으로 개발됐습니다.

- [vladocar/nanoJS: Minimal standalone JS library for DOM manipulation](https://github.com/vladocar/nanoJS "vladocar/nanoJS: Minimal standalone JS library for DOM manipulation")

----
