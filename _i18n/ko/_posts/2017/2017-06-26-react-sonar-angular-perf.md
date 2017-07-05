---
title: "2017-06-26 JS: React 입문, sonar - linting for web, Angular 성능 개선"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-06-26T08:55:22.360Z
category: JSer
tags:
- React
- Lint
- ESLint
- Angular

---

JSer.info #337 - [React Express](http://www.react.express/ "React Express") 라는 사이트에는 React를 이용한 애플리케이션 개발에 관한 튜토리얼이 작성돼 있습니다.
React로 처음하는 개발이라는 컨셉으로 npm, ES2015 등 관련 도구나 환경에 대해서도 간단하게 소개돼 있습니다.
기본적으로 실행할 수 있는 샘플코드 / 예제와 함께 React가 소개돼 있어 직접 실행해 보며 이해할 수 있습니다.

-----

 ESLint와 비슷한 도구 [sonar, a linting tool for the web](https://sonarwhal.com/ "sonar, a linting tool for the web")가 JS Foundation 프로젝트로서 공개됐습니다.

- [sonar – JS Foundation Welcomes Newest Project – JS Foundation](https://js.foundation/announcements/2017/06/22/sonar-js-foundation-welcomes-newest-project "sonar – JS Foundation Welcomes Newest Project – JS Foundation")

본래 MSEdge의 팀에 의해 만들어진 것으로 ESLint 처럼 커스텀 규칙을 작성할 수 있습니다.

- [sonar/events.md at master · sonarwhal/sonar](https://github.com/sonarwhal/sonar/blob/master/docs/developer-guide/collectors/events.md "sonar/events.md at master · sonarwhal/sonar")
   - hook 할 수 있는 이벤트

웹사이트의 HTML 요소를 트래버어스(Traverse) 하면서 처리하거나 리소스에 대한 리퀘스트 처리를 규칙으로 작성할 수 있습니다.

[FAQ](https://sonarwhal.com/about/faq.html "FAQ")에 따르면 [aXe](https://www.deque.com/products/axe/ "Easy Accessibility Testing with aXe")나 [SSL Server Test](https://www.ssllabs.com/ssltest/ "SSL Server Test") 등 기존 도구나 서비스와 연동할 수 있는 Linting 도구를 목적으로 하고 있는 것 같습니다(이를 위해 규칙도 비동기 처리에 대응하고 있음).

> sonar doesn’t want to reinvent the wheel. For that reason it tries to integrate other tools and services that do a great job and contribute back where appropriate. For example, we are using axe for accessibility, SSL Server Test for checking the certificate configuration, etc.

----

[Improve SPA Performance with Angular App // Speaker Deck](https://speakerdeck.com/manakuro/improve-spa-performance-with-angular-app "Improve SPA Performance with Angular App // Speaker Deck")(일본어) 슬라이드에는 메모리 누수가 발생하기 쉬운 패턴이나 Chrome 개발자 도구를 사용한 측정 방법에 관해 소개합니다.
또, Angular에 의한 메모리 누수 패턴이나 Change Detection 처리를 주리는 방법 등에 대해서도 작성돼 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Dev.Opera — What’s new in Chromium 59 and Opera 46
[dev.opera.com/blog/opera-46/](https://dev.opera.com/blog/opera-46/ "Dev.Opera — What’s new in Chromium 59 and Opera 46")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 46 (based on Chromium 59)이 릴리즈됐습니다.
Animation PNG, SVG 파비콘, 백그라운드 탭의 처리 성능 지연(throttling), `MediaError.message`를 지원하는 등 다양한 변경 사항이 있습니다.

----

## New Release: 2.9.5
[jshint.com/blog/2017-06-22/release-2-9-5/](http://jshint.com/blog/2017-06-22/release-2-9-5/ "New Release: 2.9.5")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.9.5가 릴리즈됐습니다.
`trailingcomma` 옵션이 추가됐고 몇 가지 버그 수정이 이뤄졌습니다.

----

## ESLint v4.1.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/06/eslint-v4.1.0-released](http://eslint.org/blog/2017/06/eslint-v4.1.0-released "ESLint v4.1.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.1.0이 릴리즈됐습니다. glob 기반의 `overrides` 설정 방식이 추가 됐고 무시할 파일을 `package.json`에 정의할 수 있도록 변경됐습니다.

- [ESLint v4.1.0 - Qiita](http://qiita.com/mysticatea/items/e758c9a9a7dfb8b9cdb1 "ESLint v4.1.0 - Qiita")

----
<h1 class="site-genre">아티클</h1>

----

## JS scope: static, dynamic, and runtime-augmented – Dmitry Soshnikov – Medium
[medium.com/@DmitrySoshnikov/js-scope-static-dynamic-and-runtime-augmented-5abfee6223fe](https://medium.com/@DmitrySoshnikov/js-scope-static-dynamic-and-runtime-augmented-5abfee6223fe "JS scope: static, dynamic, and runtime-augmented – Dmitry Soshnikov – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

JavaScript의 스코프에 관해 소개돼 있는 글입니다.
생성 시 참조가 결정되는 Static scope, 호출 시 참조가 결정되는 Dynamic scope(Perl을 이용해 설명), `with`나 `eval`에 의해 Runtime-augmented scope에 관해 작성돼 있습니다.

----

## React Express
[www.react.express/](http://www.react.express/ "React Express")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

React 튜토리얼이 공개돼 있는 사이트입니다.
사이트 내에서 실행할 수 있는 샘플과 함께 React 사용법과 npm / webpack / ES2015 등 관련 도구나 지식이 소개돼 있습니다.

----

## Redux Architecture Guidelines | joeellis.la
[joeellis.la/redux-architecture/](http://joeellis.la/redux-architecture/ "Redux Architecture Guidelines | joeellis.la")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

개개별로 특이 사항은 있겠지만 작성자가 생각했을 때 고수하는 Redux 아키텍처 가이드라인이 작성돼 있습니다.
state의 중첩(Nest)을 피하기 위해 normalize 하고 state에는 resource가 되는 원시 데이터(raw data)만 넣어 사용하며 React의 state보다 Redux의 State를 선호하는 방안에 대해 이야기합니다. 
또, Standard Action, Container component에 관해서도 작성돼 있습니다.

----

## Aligned Input Events  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/aligning-input-events](https://developers.google.com/web/updates/2017/06/aligning-input-events "Aligned Input Events  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">event</span> <span class="jser-tag">article</span> <span class="jser-tag">Android</span></p>

Pointer Events의 `getCoalescedEvents`에 관해 설명하는 글입니다.
터치 입력은 보통 60-120Hz에 맞춰 발생하고 마우스 입력은 100Hz(최대 2000Hz)에 맞춰 발생하지만 모니터는 보통 60Hz 속도로 화면이 재생됩니다. 따라서 이벤트가 발행(dispatch)되는 시점과 모니터 재생율(refresh rate)이 상이해 비효율을 발생시킵니다.
이러한 비효율을 피하기 위해 `requestAnimationFrame`이 발생하기 직전에 이벤트를 모아 발행해주는 `getCoalescedEvents()`에 대해 소개돼 있습니다.

----

## Codemods: A Quick and Easy Way to Automate Code Refactoring — SitePoint
[www.sitepoint.com/getting-started-with-codemods/](https://www.sitepoint.com/getting-started-with-codemods/ "Codemods: A Quick and Easy Way to Automate Code Refactoring — SitePoint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">AST</span></p>

codemod를 사용해 리팩터링 도구를 만드는 방법이 소개돼 있습니다.

----

## ✨Locally Scoped CSS Variables: What, How, and Why | Una Kravets Online✨
[una.im/local-css-vars/](https://una.im/local-css-vars/ "✨Locally Scoped CSS Variables: What, How, and Why | Una Kravets Online✨")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

CSS Custom Properties에 대한 글입니다.
사용 방법, 로컬 스코프, 지원 상황 등에 대해 작성돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## High Performance JS in V8 - Google スライド
[docs.google.com/presentation/d/1KCcA-WAyhGs0SEOrfU21fjaTWTxvNxYLwmNlGIbuZFw/edit#slide&#x3D;id.p](https://docs.google.com/presentation/d/1KCcA-WAyhGs0SEOrfU21fjaTWTxvNxYLwmNlGIbuZFw/edit#slide=id.p "High Performance JS in V8 - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

V8의 ES2015+ 성능에 대한 슬라이드입니다.
Crankshaft는 ES2015를 최적화 하지 않기 때문에 느렸습니다. 또 try-catch 구문 등이 있으면 최적화를 할 수 없었습니다.
새로운 pipeline의 Ignition + Turbofan에서는 이러한 부분이 개선되고 있다고 합니다.

----

## Improve SPA Performance with Angular App // Speaker Deck(일본어)
[speakerdeck.com/manakuro/improve-spa-performance-with-angular-app](https://speakerdeck.com/manakuro/improve-spa-performance-with-angular-app "Improve SPA Performance with Angular App // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">performance</span> <span class="jser-tag">Angular</span> <span class="jser-tag">slide</span></p>

메모리 릭 패턴, Chrome 개발자 도구를 사용한 측정 방법에 관해 소개돼 있습니다.
Angular에 의한 의도하지 않은 메모리 릭을 피하는 방법이나 Chnage Detection의 비용을 줄이는 방법 등에 대해서도 이야기합니다.

- [mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.](https://github.com/mgechev/angular-performance-checklist "mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.
[github.com/mgechev/angular-performance-checklist](https://github.com/mgechev/angular-performance-checklist "mgechev/angular-performance-checklist: Cheatsheet for developing ⚡lightning⚡ fast progressive Angular applications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">performance</span> <span class="jser-tag">document</span></p>

Angular 성능 관련 체크 리스트를 작성해 놓은 문서입니다.

----

## faceyspacey/redux-first-router: 🎖 seamless redux-first routing -- just dispatch actions
[github.com/faceyspacey/redux-first-router](https://github.com/faceyspacey/redux-first-router "faceyspacey/redux-first-router: 🎖 seamless redux-first routing -- just dispatch actions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Redux 용의 라우터 라이브러리입니다.
URL 패턴에 매치해 Action을 발행하는 방식으로 라우팅이 이뤄집니다.

- [Pre Release: Redux-First Router — A Step Beyond Redux-Little-Router](https://medium.com/faceyspacey/pre-release-redux-first-router-a-step-beyond-redux-little-router-cd2716576aea "Pre Release: Redux-First Router — A Step Beyond Redux-Little-Router")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## sonar, a linting tool for the web
[sonarwhal.com/](https://sonarwhal.com/ "sonar, a linting tool for the web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

웹사이트(URL)에 대해 Lint할 수 있는 ESLint 같은 도구입니다.
커스텀 룰을 직접 정의할 수 있고 axe나 SSL Server Test 등 기존 도구를 간단하게 연동하여 사용할 수 있습니다.

----

## await-to-js - NMOTW
[https://nmotw.in/await-to-js/](https://nmotw.in/await-to-js/ "await-to-js - NMOTW")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

await와 조합해 사용하여 go 언어 처럼 `[error, value]` 형식으로 값을 반환받을 수 있도록 하는 라이브러리입니다.

----

## medikoo/date-from-timezone: Construct dates with timezone context
[github.com/medikoo/date-from-timezone](https://github.com/medikoo/date-from-timezone "medikoo/date-from-timezone: Construct dates with timezone context")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

`Intl.DateTimeFormat`을 사용하여 JavaScript에 타임존 정보를 부여해 `Date` 객체를 생성할 수 있는 라이브러리입니다.

- [Add timezone data to Date](https://esdiscuss.org/topic/add-timezone-data-to-date#content-6 "Add timezone data to Date")

----

## OptimalBits/redbird: A modern reverse proxy for node
[github.com/OptimalBits/redbird](https://github.com/OptimalBits/redbird "OptimalBits/redbird: A modern reverse proxy for node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">proxy</span></p>

HTTPS나 HTTP/2에 대응한 Node.js의 리버스 프록시 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## O'Reilly Japan - 아이소모픽 JavaScript
[www.oreilly.co.jp/books/9784873118079/](https://www.oreilly.co.jp/books/9784873118079/ "O'Reilly Japan - アイソモーフィックJavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">React</span> <span class="jser-tag">Angular</span></p>

2017년 7월 4일에 출간될 Isomorphic JavaScript에 관한 서적입니다.
실제 구현 방법과 React / Angular / Brisket 프레임워크을 사용한 방법 그리고 케이스 스터디에 대해 작성돼 있습니다.

----
