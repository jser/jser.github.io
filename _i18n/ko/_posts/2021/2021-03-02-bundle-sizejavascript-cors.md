---
title: "2021-03-02: Bundle Size 외의 JavaScript 성능, CORS 완벽 가이드"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-03-01T21:33:41.685Z
category: JSer
tags:
- debug
- React
- Chrome
- CSS
- performance

---

JSer.info #529 - [JavaScript performance beyond bundle size | Read the Tea Leaves](https://nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/)

자바스크립트의 성능 측정을 주제로 한 글.
Bundle Size 관련해서는 [BundlePhobia](https://bundlephobia.com/)나 [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) 등 쉽게 측정할 수 있는 도구를 소개하며 그 이외의 자바스크립트 성능 지표는 어떻게 살펴 볼 수 있는지 다룬다.
런타임 CPU 비용, 전력 소비량, 메모리 사용량, 디스크 사용량 등 Bundle Size 이외의 지표를 측정하고 살펴보는 방법 소개.

---

[CORS 完全手冊](https://blog.huli.tw/2021/02/19/cors-guide-1/)(중국어)

CORS를 주제로 한 연재 글.
CORS의 개념, 대응 방법, 자주 하는 실수, CORB / CORP / COEP / COOP 등 최근의 오리진 관련 규칙, 보안 문제 등을 다룬다.

- [CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？](https://blog.huli.tw/2021/02/19/cors-guide-1/)
  - 크로스 오리진 요청이란 무엇인가? CORS 에러는 왜 일어나는가. 
- [CORS 完全手冊（二）：如何解決 CORS 問題？](https://blog.huli.tw/2021/02/19/cors-guide-2/)
  - CORS 대응 수단(express를 예로 소개)
- [CORS 完全手冊（三）：CORS 詳解](https://blog.huli.tw/2021/02/19/cors-guide-3/)
  - CORS의 구조, 각 헤더의 의미를 시나리오와 함께 소개.
- [CORS 完全手冊（四）：一起看規範](https://blog.huli.tw/2021/02/19/cors-guide-4/)
  - CORS 사양을 [Fetch Standard](https://fetch.spec.whatwg.org/)와 함께 설명. `Vary` 헤더에서의 캐시 주의점도 소개.
- [CORS 完全手冊（五）：跨來源的安全性問題](https://blog.huli.tw/2021/02/19/cors-guide-5/)
  - `res.headers['Access-Control-Allow-Origin'] = req.headers['Origin']` 처럼 Origin을 별 생각없이 설정하는 실수(취약성)에 대해서.
  - CORB / CORP / COEP / COOP와 Site Isolation에 대해서.
- [CORS 完全手冊（六）：總結、後記與遺珠](https://blog.huli.tw/2021/02/19/cors-guide-6/)
  - CORS 에러의 패턴 분류, Origin Policy, CORS에 대한 자세한 이야기.

CORS에 대한 필요한 지식이 거의 소개돼 있어 추천.

----

<h1 class="site-genre">아티클</h1>

----

## Introducing Env: a better way to read environment variables in JavaScript - Human Who Codes
[humanwhocodes.com/blog/2021/02/introducing-env-javascript-environment-variables/](https://humanwhocodes.com/blog/2021/02/introducing-env-javascript-environment-variables/ "Introducing Env: a better way to read environment variables in JavaScript - Human Who Codes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

환경 변수를 읽어들일 때 자주 있는 문제를 회피할 수 있는 라이브러리 Env 소개.


----

## CSS-in-JS support in DevTools  |  Web  |  Google Developers
[developers.google.com/web/updates/2021/02/css-in-js](https://developers.google.com/web/updates/2021/02/css-in-js "CSS-in-JS support in DevTools  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chrome 85 DevTools의 CSS-in-JS 대응 기능 소개.
CSSOM API로 추가한 스타일 규칙도 개발자 도구에서 편집할 수 있게 된다.


----

## JavaScript performance beyond bundle size | Read the Tea Leaves
[nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/](https://nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/ "JavaScript performance beyond bundle size | Read the Tea Leaves")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScript의 Bundle size와 런타인 CPU 비용, 메모리 이용량, 전력 사용량을 알아볼 수 있는 방법 소개.
Bundle Size에 대해서는 BundlePhobia나 Web Vitals 등에서 알기 쉽게 볼 수 있다. 하지만 성능은 좀 더 폭넓은 개념으로, Bundle Size 외의 지표는 어떻게 볼 수 있는지 다룬다.


- [BundlePhobia ❘ cost of adding a npm package](https://bundlephobia.com/ "BundlePhobia ❘ cost of adding a npm package")

----

## How Web Content Can Affect Power Usage | WebKit
[webkit.org/blog/8970/how-web-content-can-affect-power-usage/](https://webkit.org/blog/8970/how-web-content-can-affect-power-usage/ "How Web Content Can Affect Power Usage | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

CPU, GPU, 네트워크 등이 전력 소비에 주는 영향 소개.
백그라운드 모드에서 CPU 소비를 줄이는 방법, Web Inspector Energy Impact 표시.


----

## Why JavaScript Developers Should Prefer Axios Over Fetch | by Sabesan Sathananthan | Feb, 2021 | Better Programming
[betterprogramming.pub/why-javascript-developers-should-prefer-axios-over-fetch-294b28a96e2c](https://betterprogramming.pub/why-javascript-developers-should-prefer-axios-over-fetch-294b28a96e2c "Why JavaScript Developers Should Prefer Axios Over Fetch | by Sabesan Sathananthan | Feb, 2021 | Better Programming")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

Fetch API와 axios 비교.
응답 데이터 자동 변환, 에러 처리, 다운로드의 프로그래스 처리, 업로드 프로그래스 처리, HTTP 인터셉트, 타임아웃, 병렬 요청 등을 주제로 비교한다.


----

## Use CSS Variables instead of React Context | Epic React by Kent C. Dodds
[epicreact.dev/css-variables/](https://epicreact.dev/css-variables/ "Use CSS Variables instead of React Context | Epic React by Kent C. Dodds")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS-in-JS를 사용한 Theme 컴포넌트와 같은 테마 변환 기능을 CSS Custom Properties로 구현한 이야기.
구현의 차이와 렌더링 플로우의 차이 소개.


----

## React Context를 export 하는 건 안티 패턴이 아닐까 생각한다 | stin&#039;s blog(일본어)
[blog.stin.ink/articles/do-not-export-react-context](https://blog.stin.ink/articles/do-not-export-react-context "React Context를 export 하는 건 안티 패턴이 아닐까 생각한다 | stin&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Context를 모듈로 export 하지 않고 Custom Hook으로서 export 하는 방법과 유용성 소개.


----

## CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？ - Huli(중국어)
[blog.huli.tw/2021/02/19/cors-guide-1/](https://blog.huli.tw/2021/02/19/cors-guide-1/ "CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？ - Huli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CORS</span> <span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

CORS 개념, 대응 방법, 자주 있는 문제, CORB / CORP / COEP / COOP 등 옵션 관련 규칙, 보안 측면의 문제 등에 대해 연재하는 글.
크로스 오리진은 왜 차단되는지, CORS 사양 소개, CORS 캐시, CORS 설정 실수에 대해 이야기한다.


----

## What&#039;s New In DevTools (Chrome 90)  |  Web  |  Google Developers
[developers.google.com/web/updates/2021/02/devtools](https://developers.google.com/web/updates/2021/02/devtools "What&#039;s New In DevTools (Chrome 90)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 90 Dev Tools 변경 사항 소개.
CSS flexbox 디버깅 도구 추가, Core Web Vitals 오버레이 표시.
Issues tab 개선, CSS color-gamut 에뮬레이터 기능 추가.
Dev Tools를 활성화한 상태에서의 디버깅 성능 개선, `fn.displayName` 지원 비권장.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## GoudekettingRM/link-overview-jsworld-2021
[github.com/GoudekettingRM/link-overview-jsworld-2021](https://github.com/GoudekettingRM/link-overview-jsworld-2021 "GoudekettingRM/link-overview-jsworld-2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span> <span class="jser-tag">slide</span></p>

JS World 2021의 슬라이드와 영상이 정리돼 있다.

- [JS World - Online Conference by Frontend Love](https://frontenddeveloperlove.com/ "JS World - Online Conference by Frontend Love")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## jcubic/tagger: Zero Dependency, Vanilla JavaScript Tag Editor
[github.com/jcubic/tagger](https://github.com/jcubic/tagger "jcubic/tagger: Zero Dependency, Vanilla JavaScript Tag Editor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

의존 하는 모듈 없는 태그 입력 UI 라이브러리.


----

## wynntee/joss: JOSS can serialize almost every JavaScript data type and data structure, so data can be seamlessly exchanged between browsers and servers (Deno or Node.js).
[github.com/wynntee/joss](https://github.com/wynntee/joss "wynntee/joss: JOSS can serialize almost every JavaScript data type and data structure, so data can be seamlessly exchanged between browsers and servers (Deno or Node.js).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JOSS라는 포멧으로 JavaScript 객체를 직렬화, 역직렬화 하는 사양과 그 레퍼런스를 구현한 라이브러리.
BigInt, 순환 참조, 희소배열(sparse arrays), `-0` 등 JSON에는 없는 데이터 형도 지원한다.
브라우저, Node, Deno에서 동작.

- [JS Open Serialization Scheme](https://www.wynntee.com/projects/serialization/specification/index.html "JS Open Serialization Scheme")

----

## andrewcourtice/harlem: Simple, unopinionated, lightweight and extensible state management for Vue 3
[github.com/andrewcourtice/harlem](https://github.com/andrewcourtice/harlem "andrewcourtice/harlem: Simple, unopinionated, lightweight and extensible state management for Vue 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Vue 3 용 상태 관리 라이브러리.
plugin으로 Vue DevTools 대응, SSR, Storage 기억, 트랜잭션 대응이 가능하다.


----
<h1 class="site-genre">도서</h1>

----

## React 테스트 응용, 테스트가 괴로운 사람에게(일본어)
[zenn.dev/tkdn/books/react-testing-patterns](https://zenn.dev/tkdn/books/react-testing-patterns "React 테스트 응용, 테스트가 괴로운 사람에게")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span></p>

React 컴포넌트와 Hooks 테스트를 주제로 한 도서.


----
