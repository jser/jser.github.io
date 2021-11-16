---
title: "2021-11-09: React Router v6, Angular v13, Chrome의 Record and Replay, TypeScript로의 단계적 이전"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-11-09T02:39:44.474Z
category: JSer
tags:
- React
- TypeScript
- Chrome
- performance
- node.js

---

JSer.info #565 - React Router v6가 릴리스 됐다.

- [React Router v6 | Remix](https://remix.run/blog/react-router-v6)

React Hooks 기반으로 재구현, `<Route>` 들여쓰기 개선, `<Link to>` 값의 상대 경로 해석이 `<Route path>`를 기준으로 이뤄지도록 변경됐다.

이와 함께 React Router v5에서의 마이그레이션 가이드도 공개됐다.

- [React Router | Upgrading from v5](https://reactrouter.com/docs/en/v6/upgrading/v5)

----

Angular 13이 릴리스됐다.

- [Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog](https://blog.angular.io/angular-v13-is-now-available-cce66f7bc296)

Ivy가 기본으로 채택돼 View Engine이 삭제됐다.
Angular Package Format(APF)가 `package.json`의 `exports` 필드를 지원한다.
또, IE 11 지원이 종료됐다.
Angular에서 IE 지원은 Angular 12까지만 이뤄지며 Angular 12는 2022년 11월 12일까지 관리된다.

- [Angular - Angular versioning and releases](https://angular.io/guide/releases#support-policy-and-schedule)

그 외로는 Angular CLI가 영속 빌드 캐시를 지원, 테스트 시 DOM 클린업 작업이 기본적으로 이뤄진다.

----

[Record, replay and measure user flows - Chrome Developers](https://developer.chrome.com/docs/devtools/recorder/)에서는 Chrome 97의 개발자 도구에 프리뷰로 구현된 Recorder panel을 소개한다.

사용자 조작을 기록하여 재생할 수 있고 사용자 흐름과 성능 측정을 조합하여 이용할 수 있다.
또, 기록한 내용을 편집하거나 Puppeteer 스크립트로 출력할 수 있다.

----


JavaScript에서 TypeScript로 단계적 이전을 주제로 한 두 글을 소개한다.

- [인크리멘탈하게 새로운 기술을 도입하는 방법. TypeScript로의 이전을 예로 한 프로세스](https://tech.plaid.co.jp/karte-blocks-incremental-development/)(일본어)
- [Etsy’s Journey to TypeScript - Code as Craft](https://codeascraft.com/2021/11/08/etsys-journey-to-typescript/)

느슨한 방식으로 접근하고 나서 단계적으로 엄격하게 변경하는 방법과 처음부터 엄격하게 타입을 작성하는 방법을 비교 및 소개하고 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v11.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v11.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v11.0.0 "Release v11.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 11.0.0 릴리스.
Out of Process한 iframe의 wait을 지원하는 `Page.waitForFrame()`와 `frame.isOOPFrame()` 추가.
HTTP Request의 initiator를 취득할 수 있도록 개선


----

## Recoil 0.5 | Recoil
[recoiljs.org/blog/2021/11/03/0.5.0-release](https://recoiljs.org/blog/2021/11/03/0.5.0-release "Recoil 0.5 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.5 릴리스.
캐시를 비울 수 있는 `useRecoilRefresher_UNSTABLE()` 추가.
onSet 콜백에 `isReset` 파라메터 추가, `getLoadable()` / `getPromise()` / `getInfo_UNSTABLE()` 추가.


----

## React Router v6 | Remix
[remix.run/blog/react-router-v6](https://remix.run/blog/react-router-v6 "React Router v6 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Router v6 릴리스.
React Hooks 기반으로 재작성, `<Route>`의 들여쓰기 개선, `<Link to>` 값의 상대 경로 해석이 `<Route path>`를 기준으로 이뤄지도록 변경.

- [React Router v6 | Remix](https://remix.run/blog/react-router-v6#upgrading-to-react-router-v6 "React Router v6 | Remix")
- [React Router | Upgrading from v5](https://reactrouter.com/docs/en/v6/upgrading/v5 "React Router | Upgrading from v5")

----

## Announcing TypeScript 4.5 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/ "Announcing TypeScript 4.5 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.5 RC 릴리스.
4.5 beta에서 도입 됐던 ESM 대응 시스템 `module: node12`는 릴리스 연기 됐다.


----

## Nightwatch v2 is Now in Beta | Nightwatch.js Blog
[nightwatchjs.org/blog/nightwatch-v2-beta-is-available.html](https://nightwatchjs.org/blog/nightwatch-v2-beta-is-available.html "Nightwatch v2 is Now in Beta | Nightwatch.js Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nightwatch v2 릴리스.
Chrome DevTools Protocol과 WebDriver BiDI 지원, CucumberJS 지원 등.


----

## V8 release v9.7 · V8
[v8.dev/blog/v8-release-97](https://v8.dev/blog/v8-release-97 "V8 release v9.7 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v9.7 릴리스.
Array와 TypedArray에 `findLast`와 `findLastIndex` 메서드 구현.


----

## Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog
[blog.angular.io/angular-v13-is-now-available-cce66f7bc296](https://blog.angular.io/angular-v13-is-now-available-cce66f7bc296 "Angular v13 is now Available. We’re back with the brand new release… | by Mark Thompson (@marktechson) | Nov, 2021 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 13 릴리스.
Ivy가 기본이 됐기 때문에 View Engine 삭제, Angular Package Format(APF)이 `exports` 필드를 지원, IE 11 지원 종료.
Angular CLI에서 영속 빌드 캐시 지원, 테스트 시 DOM의 클린업이 기본으로 진행된다.


----

## Release v4.0.0 · markedjs/marked
[github.com/markedjs/marked/releases/tag/v4.0.0](https://github.com/markedjs/marked/releases/tag/v4.0.0 "Release v4.0.0 · markedjs/marked")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

markded 4.0.0 릴리스.
ESM 대응, default export를 삭제하고 `import { markded } from "marked"`와 같이 named import를 사용하도록 변경.


----
<h1 class="site-genre">아티클</h1>

----

## What&#039;s new in PageSpeed Insights
[web.dev/whats-new-pagespeed-insights/](https://web.dev/whats-new-pagespeed-insights/ "What&#039;s new in PageSpeed Insights")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

PageSpeed Insights의 새로운 화면 디자인 소개.
기존에는 측정 데이터와 CrUX 데이터(Lab)가 혼재돼 있었으나 CrUX 데이터는 Origin Summary 탭으로 분리 됐다.
또, Core Web Vitals의 스코어 표시가 포함될 예정이다.


----

## Malware found in coa and rc, two npm packages with 23M weekly downloads - The Record by Recorded Future
[therecord.media/malware-found-in-coa-and-rc-two-npm-packages-with-23m-weekly-downloads/](https://therecord.media/malware-found-in-coa-and-rc-two-npm-packages-with-23m-weekly-downloads/ "Malware found in coa and rc, two npm packages with 23M weekly downloads - The Record by Recorded Future")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

`coa`와 `rc` 패키지에 멀웨어가 포함된 버전이 배포돼 있었던 문제에 대해서 다룬다.
현재는 해결된 상태이며, 아래 나열한 각 버전이 문제의 버전으로 참고하길 바란다.

- coa: 2.0.3, 2.0.4, 2.1.1, 2.1.3, 3.0.1, 3.1.3
- rc: 1.2.9, 1.3.9, 2.3.9

- [Embedded malware in coa · GHSA-73qr-pfmq-6rp8 · GitHub Advisory Database](https://github.com/advisories/GHSA-73qr-pfmq-6rp8 "Embedded malware in coa · GHSA-73qr-pfmq-6rp8 · GitHub Advisory Database")
- [Embedded malware in rc · GHSA-g2q5-5433-rhrf · GitHub Advisory Database](https://github.com/advisories/GHSA-g2q5-5433-rhrf "Embedded malware in rc · GHSA-g2q5-5433-rhrf · GitHub Advisory Database")

----

## Record, replay and measure user flows - Chrome Developers
[developer.chrome.com/docs/devtools/recorder/](https://developer.chrome.com/docs/devtools/recorder/ "Record, replay and measure user flows - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Chrome 97 개발자 도구에 프리뷰로 구현된 Recorder panel 소개.
사용자의 조작 흐름을 기록하고 재생할 수 있다. 또, 사용자 플로우와 성능 측정을 조합해 살펴볼 수 있다.
기록한 내용을 편집하거나 Puppeteer 스크립트로 추출할 수도 있다.


----

## TypeScript의 JSDoc 지원으로 가능해진 것과 가능하지 않은 것(일본어)
[zenn.dev/qnighy/articles/56917d9bf9077b](https://zenn.dev/qnighy/articles/56917d9bf9077b "TypeScript의 JSDoc 지원으로 가능해진 것과 가능하지 않은 것")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

TypeScript의 JSDoc에 의한 타입 애너테이션을 주제로 한 글.
TypeScript와 JSDoc의 타입 애너테이션 표현력 차이, JSDoc에서의 타입 애너테이션 작성 방법 등을 소개한다.


----

## A Comprehensive Guide To Error Handling In Node.js - Honeybadger Developer Blog
[www.honeybadger.io/blog/errors-nodejs/](https://www.honeybadger.io/blog/errors-nodejs/ "A Comprehensive Guide To Error Handling In Node.js - Honeybadger Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js의 에러 핸들링을 주제로 한 해설 글.
예외, 콜백, Promise, EventEmitter 각 케이스 별 에러 핸들링 방법.
커스텀 에러로  분리, Operational Error와 Programmer Error의 다른점.
또, Operation Error가 발생했을때 대응 방법과 Programmer Error의 방지책 등 소개.


----

## 인크리멘탈하게 새로운 기술을 도입하는 방법. TypeScript로의 이전을 예로 한 프로세스(일본어)
[tech.plaid.co.jp/karte-blocks-incremental-development/](https://tech.plaid.co.jp/karte-blocks-incremental-development/ "インクリメンタルに新しい技術を取り入れる方法。TypeScriptへの移行を例にしたプロセス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">article</span></p>

JavaScript를 TypeScript로 단계적으로 이전하는 방법 소개.
처음부터 엄격하게 타입을 작성하는 방법과 느슨한 방식으로 변경하고 나서 타입을 조금씩 추가하는 방법 비교.
마이그레이션 순서, 타입을 사용한 API 벨리데이션, Vue에서 React로의 단계적인 이전 방법과 인크리멘탈하게 이전할 경우 고려해야 할 포인트 등 정리.


----

## Etsy’s Journey to TypeScript - Code as Craft
[codeascraft.com/2021/11/08/etsys-journey-to-typescript/](https://codeascraft.com/2021/11/08/etsys-journey-to-typescript/ "Etsy’s Journey to TypeScript - Code as Craft")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

TypeScript의 채택 전략(strategies for adoption)을 주제로 한 글.
타입 검증을 엄격하게 만들고 점진적으로 이전하는 방법, typescript-eslint를 사용한 범용 타입과 일부 구문을 금지하는 방법. API에 타입을 추가하는 방법.
TypeScript 타입 체크 성능 문제 디버깅과 팀원의 온보딩 전략에 대해서도 이야기한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Web Performance Metrics Cheatsheet
[bitsofco.de/web-performance-metrics-cheatsheet/](https://bitsofco.de/web-performance-metrics-cheatsheet/ "Web Performance Metrics Cheatsheet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">cheatsheet</span></p>

웹 성능 지표 치트 시트.
네 개의 스테이지로 그룹핑 하고, 각 그룹과 관련된 지표가 정리돼 있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## urin/qrono: 🕥 Just right date time library
[github.com/urin/qrono](https://github.com/urin/qrono "urin/qrono: 🕥 Just right date time library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable하게 시간을 다룰 수 있는 라이브러리.
UTC와 로컬 시간 만으로 하절기의 모호한 시간(써머 타임)을 정확히 다룰 수 있다.
Time Zone과 locale 고려 없이 아주 경량으로 구현 했고 국제화 대응이 필요하면 표준인 Internationalization API을 사용하도록 가이드하고 있다.

- [이것으로도 충분해, JavaScript 날짜 시간 라이브러리 Qrono](https://zenn.dev/urin/articles/6ca9cf8174fd92 "이것으로도 충분해, JavaScript 날짜 시간 라이브러리 Qrono")(일본어)

----

## Shopify/hydrogen: React-based framework for building dynamic, Shopify-powered custom storefronts.
[github.com/Shopify/hydrogen](https://github.com/Shopify/hydrogen "Shopify/hydrogen: React-based framework for building dynamic, Shopify-powered custom storefronts.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">vite</span> <span class="jser-tag">library</span></p>

Shopify의 스토어 프론트 사용자 정의에 사용하는 React 기반 프레임워크.
Vite와 React를 기반으로 하고 있고 React ServerSide Components를 이용하고 있다.

- [Meet Hydrogen: A React Framework For Dynamic, Contextual And Personalized E-Commerce — Smashing Magazine](https://www.smashingmagazine.com/2021/11/hydrogen-react-framework-dynamic-contextual-personalized-ecommerce/ "Meet Hydrogen: A React Framework For Dynamic, Contextual And Personalized E-Commerce — Smashing Magazine")

----
<h1 class="site-genre">도서</h1>

----

## JavaScript(제 7 판) | Ohmsha(일본어)
[www.ohmsha.co.jp/book/9784873119700/](https://www.ohmsha.co.jp/book/9784873119700/ "JavaScript（第7版） | Ohmsha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2021년 12월 2일 출간 예정인 코뿔소 책 7판 일본어 번역서.
국내 도서는 6판까지 번역 돼 있다.


----
