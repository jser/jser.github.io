---
title: "2016-06-07 JS: Shadow DOM v1, React의 요즈음 상황, JavaScript 플러그인 설계 관련 책"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-06-07T09:40
category: JSer
tags:
    - WebComponent
    - React
    - JavaScript
    - plguin
    - book

---

JSer.info #282 - [What's New in Shadow DOM v1 (by examples) — hayato.io](http://hayato.io/2016/shadowdomv1/ "What&#39;s New in Shadow DOM v1 (by examples) — hayato.io")에 Shadow DOM v0과 v1의 차이점에 관해 설명돼 있습니다. 글을 작성한 [@shadow_hayato](https://twitter.com/shadow_hayato "@shadow_hayato")는 Shadow DOM의 사양 책정자입니다.

v1에는 closed shadow root라는 개념의 추가됐고, `/deep/`나 `::shadow`를 사용할 수 없으며, slot(`::slotted`)이 추가되는 등 여러가지 변경 사항이 있습니다.

- [webcomponents/Shadow-DOM-Cascade-Order-in-v1.md at gh-pages · w3c/webcomponents](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/Shadow-DOM-Cascade-Order-in-v1.md "webcomponents/Shadow-DOM-Cascade-Order-in-v1.md at gh-pages · w3c/webcomponents")

예제 코드를 중심으로 설명하고 있어, Shadow DOM에 관심 있는 사람이 보면 좋을 것 같습니다. 

-----

[ReactEurope](https://www.react-europe.org/ "ReactEurope")가 개최됐으며, 해당 컨퍼런스의 발표 영상도 공개됐습니다.

- [ReactEurope - YouTube](https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A/feed "ReactEurope - YouTube")

또, [The state of React.js 2016 // Speaker Deck](https://speakerdeck.com/koba04/the-state-of-react-dot-js-2016 "The state of React.js 2016 // Speaker Deck")라는 슬라이드에는 약 반년 간의 리액트 변화 등에 관해 정리돼 있습니다.

React의 최근 동향을 파악하고자 한다면 React Core 팀의 미팅 노트를 함께 참고하면 좋을 것 같습니다.

- [reactjs/core-notes: Weekly meeting notes from the React core team](https://github.com/reactjs/core-notes "reactjs/core-notes: Weekly meeting notes from the React core team")

----

[JavaScript Plugin Architecture](https://github.com/azu/JavaScript-Plugin-Architecture "JavaScript Plugin Architecture")(일본어)에는 자바스크립트의 라이브러리나 도구의 플러그인 구조에 관해 작성돼 있습니다.

- [플러그인 구조에 관해 학습할 수 있는 JavaScript Plugin Architecture라는 무료 전자 서적을 작성했다 | Web Scratch](http://efcl.info/2016/06/06/JavaScript-Plugin-Architecture/ "플러그인 구조에 관해 학습할 수 있는 JavaScript Plugin Architecture라는 무료 전자 서적을 작성했다 | Web Scratch")

현재 [jQuery](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/jQuery/), [ESLint](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/ESLint/), [Connect](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/connect/), [gulp](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/gulp/), [Redux](https://azu.gitbooks.io/javascript-plugin-architecture/content/ja/Redux/)의 플러그인 구조를 구현해보면서 살펴보고 원리를 설명하는 과정을 담고 있습니다.

한꺼번에 읽는 것보다 궁금한 부분을 찾아서 볼 수 있는 레퍼런스 적인 느낌으로 정리돼 있습니다.

----
<h1 class="site-genre">ECMAScript 소식〆</h1>

5월에 개최된 [TC39 Meeting](https://github.com/rwaldron/tc39-notes "TC39 Meeting")의 기록이 공개되어, 중요한 사항 몇 가지를 간단하게 정리해 소개합니다.
보다 자세한 내용은 [미팅 노트](https://github.com/rwaldron/tc39-notes/tree/master/es7/2016-05 "tc39-notes/es7/2016-05 at master · rwaldron/tc39-notes")을 참고하시길 바랍니다.

- [tc39/proposals: Tracking ECMAScript Proposals | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/13/tc39-proposals-tracking-ecmascript-proposals)
  - 과거 Proposal은 [tc39/ecma262](https://github.com/tc39/ecma262 "tc39/ecma262")에 정리돼 있었지만, 현재는 별도의 저장소로 옮겨졌습니다.
- [Arrive TC39 meeting notes for 2016-05 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/06/07/arrive-tc39-meeting-notes-for-2016-05)
  - 2016년 5월의 미팅 노트가 공개됐습니다.
  - 6월 중순에는 ECMAScript 2016의 정식 릴리즈가 예정돼 있습니다.
- [[Stage 0] ljharb/proposal-promise-finally: ECMAScript Proposal, specs, and reference implementation for Promise.prototype.finally | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-0-ljharb-proposal-promise-finally-ecmascript-proposal-specs-and-reference-implementation-for-promise-prototype-finally)
  - `Promise#finally`의 Proposal이 Stage 0가 됐습니다.
- [[Stage 4] Per May 2016 TC39 consensus, String#{padStart,padEnd} is now stage 4! by ljharb · Pull Request #581 · tc39/ecma262 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-4-per-may-2016-tc39-consensus-string-padstart-padend-is-now-stage-4-by-ljharb-pull-request-581-tc39-ecma262)
- [[Stage 4] Per May 2016 TC39 consensus, Object.getOwnPropertyDescriptors is now stage 4! by ljharb · Pull Request #582 · tc39/ecma262 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/25/stage-4-per-may-2016-tc39-consensus-object-getownpropertydescriptors-is-now-stage-4-by-ljharb-pull-request-582-tc39-ecma262)
  - `String#{padStart,padEnd}`와 `Object.getOwnPropertyDescriptors`가 Stage 4가 됐고 ES2017에 들어갔습니다.
- [Cancelable promises | ECMAScript Daily](https://ecmascript-daily.github.io/2016/05/26/cancelable-promises)
  - Promise의 취소 방법으로 CancelToken과 `Promise#cancel` 두 가지 방법이 제안됐고, 의논이 시작됐습니다.
  - [zenparsing/es-cancel-token: Cancel Tokens for ECMAScript](https://github.com/zenparsing/es-cancel-token)
    - ES Observable과도 관계가 있다. [Remove forEach and add "subscribe" overload by zenparsing · Pull Request #97 · zenparsing/es-observable](https://github.com/zenparsing/es-observable/pull/97 "Remove forEach and add &#34;subscribe&#34; overload by zenparsing · Pull Request #97 · zenparsing/es-observable") 참고.
  - [domenic/cancelable-promise: Cancelable promises proposal for JavaScript](https://github.com/domenic/cancelable-promise)

----
<h1 class="site-genre">헤드라인</h1>

----

## V8 JavaScript Engine: Release 5.2
[v8project.blogspot.com/2016/06/release-52.html](http://v8project.blogspot.com/2016/06/release-52.html "V8 JavaScript Engine: Release 5.2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.2가 릴리즈됐습니다.
 Exponentiation operator `**` 지원, `Array.isArray`, `in` operator, `Function#bind`의 성능이 개선됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Getting Started with TDD in React - Semaphore
[semaphoreci.com/community/tutorials/getting-started-with-tdd-in-react](https://semaphoreci.com/community/tutorials/getting-started-with-tdd-in-react "Getting Started with TDD in React - Semaphore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

Enzyme를 사용한 React Component 테스트 방법에 관해 이야기합니다.

----

## What&#x27;s New in Shadow DOM v1 (by examples) — hayato.io
[hayato.io/2016/shadowdomv1/](http://hayato.io/2016/shadowdomv1/ "What's New in Shadow DOM v1 (by examples) — hayato.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Shadow DOM v0와 v1의 차이점에 관해 작성돼 있습니다.
[@shadow_hayato](https://twitter.com/shadow_hayato "@shadow_hayato")(사양책정자)가 작성한 글이며 예제 코드를 중심으로 설명합니다.

- [Shadow DOM v1: Status updates - Google 그룹스](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/BUGxw_Yx5Lo "Shadow DOM v1: Status updates - Google グループ")
- [Issues · w3c/webcomponents](https://github.com/w3c/webcomponents/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Av1+label%3Ashadow-dom "Issues · w3c/webcomponents")


----

## Chrome의 헤드리스 브라우저가 찾아온다 하여 설치해봤다. - Qiita(일본어)
[qiita.com/devneko/items/51f2e114a7e0b3389435](http://qiita.com/devneko/items/51f2e114a7e0b3389435 "Chromeのヘッドレスブラウザがやってくる。というわけで試してみた。 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chrome의 헤드리스 브라우저를 설치해본 내용이 정리돼 있습니다.

- [Issues - chromium - An open-source project to help move the web forward. - Monorail](https://bugs.chromium.org/p/chromium/issues/list?q=label:Proj-Headless "Issues - chromium - An open-source project to help move the web forward. - Monorail")

----

## Infinite collections with ES6 generators - Advanced Web Machinery
[advancedweb.hu/2016/05/31/infinite-collections-with-es6-generators/](https://advancedweb.hu/2016/05/31/infinite-collections-with-es6-generators/ "Infinite collections with ES6 generators - Advanced Web Machinery")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Iterator를 사용한 무한 리스트(Infinite collections)에 관해 작성돼 있습니다.

- [sashee/gentoo: Tools for ES6 generators](https://github.com/sashee/gentoo "sashee/gentoo: Tools for ES6 generators")

----

## Why we chose MobX over Redux for Spectacle Editor
[formidable.com/blog/2016/06/02/why-we-chose-mobx-over-redux-for-spectacle-editor/](http://formidable.com/blog/2016/06/02/why-we-chose-mobx-over-redux-for-spectacle-editor/ "Why we chose MobX over Redux for Spectacle Editor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span></p>

Redux 처럼 애플리케이션의 State를 관리하는 도구인 MobX의 특징을 소개합니다.

- [mobxjs/mobx: Simple, scalable state management.](https://github.com/mobxjs/mobx "mobxjs/mobx: Simple, scalable state management.")

----

## Creating A Living Style Guide: A Case Study – Smashing Magazine
[www.smashingmagazine.com/2016/05/creating-a-living-style-guide-case-study/](https://www.smashingmagazine.com/2016/05/creating-a-living-style-guide-case-study/ "Creating A Living Style Guide: A Case Study – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

스타일 가이드의 사례가 정리돼 있습니다.

----

## Improving Your CSS with Parker – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts
[csswizardry.com/2016/06/improving-your-css-with-parker/](http://csswizardry.com/2016/06/improving-your-css-with-parker/ "Improving Your CSS with Parker – CSS Wizardry – CSS, OOCSS, front-end architecture, performance and more, by Harry Roberts")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSS 코드를 분석하는 도구인 Parker를 소개합니다.

- [katiefenn/parker: Stylesheet analysis tool.](https://github.com/katiefenn/parker/ "katiefenn/parker: Stylesheet analysis tool.")

----

## webpack의 DLL 번들을 사용해 빌드 속도를 빠르게 개선한다 - Qiita(일본어)
[qiita.com/pirosikick/items/c77db84dbed4c447a6fe](http://qiita.com/pirosikick/items/c77db84dbed4c447a6fe "webpackのDLLバンドルを使ってビルドを速くする - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">performance</span></p>

webpack 빌드의 속도를 개선하는 방법에 관해 작성돼 있습니다.
DLL 번들은 vendar 라이브러리만 따로 빌드하고 그것을 다른 bundle에서 읽어드리는 순간에 빌드하는 방식, `cacheDirectory`, `externals`와의 차이점에 관해서도 이야기합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## The state of React.js 2016 // Speaker Deck
[speakerdeck.com/koba04/the-state-of-react-dot-js-2016](https://speakerdeck.com/koba04/the-state-of-react-dot-js-2016 "The state of React.js 2016 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">슬라이드</span></p>

React의 최근 변경 사항이나 향후 변경 및 비권장이 예정돼 있는 기능에 대해서 정리돼 있습니다.

- [제65회 HTML5 관련 공부 모임 ー React 최신 정보 - YouTube](https://www.youtube.com/watch?v=C8bMahvTkHA "제65회 HTML5 관련 공부 모임 ー React 최신 정보 - YouTube")(일본어)

----

## ReactEurope 2016 - Day 1 - YouTube
[www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A](https://www.youtube.com/channel/UCorlLn2oZfgOJ-FUcF2eZ1A "ReactEurope 2016 - Day 1 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">영상</span></p>

ReactEurope 2016의 영상이 정리돼 있습니다.

----

## Building React Applications with Idiomatic Redux - Course by @dan_abramov @eggheadio
[egghead.io/courses/building-react-applications-with-idiomatic-redux](https://egghead.io/courses/building-react-applications-with-idiomatic-redux "Building React Applications with Idiomatic Redux - Course by @dan\_abramov @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">영상</span> <span class="jser-tag">tutorial</span></p>

Redux 개발자가 공개한 Redux를 이용해 애플리케이션을 만드는 방법을 소개하는 스크린캐스트입니다.

- [Dan Abramov - The Redux Journey at react-europe 2016 - YouTube](https://www.youtube.com/watch?v=uvAXVMwHJXU "Dan Abramov - The Redux Journey at react-europe 2016 - YouTube")

----

## Next Vue.js 2.0 // Speaker Deck
[speakerdeck.com/kazupon/next-vue-dot-js-2-dot-0](https://speakerdeck.com/kazupon/next-vue-dot-js-2-dot-0 "Next Vue.js 2.0 // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">슬라이드</span></p>

Vue.js 2.0의 렌더링 흐름을 설명합니다.

----

## Flow vs TypeScript
[djcordhose.github.io/flow-vs-typescript/2016\_hhjs.html#/](http://djcordhose.github.io/flow-vs-typescript/2016_hhjs.html#/ "Flow vs TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">flowtype</span></p>

TypeScript와 FlowType의 타입 지정법에 관해 비교한 슬라이드입니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## HyperDev
[hyperdev.com/](https://hyperdev.com/ "HyperDev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span></p>

서버측 로직도 함게 작성할 수 있는 JSFiddle과 비슷한 서비스입니다.
Node.js로 서버측 예제를 작성하고, HTML/CSS/JS이나 프론트엔드 측 예제도 함께 작성할 수 있는 에디터 서비스입니다.

----

## Front-end Hyperpolyglot
[jeffcarp.github.io/frontend-hyperpolyglot/](http://jeffcarp.github.io/frontend-hyperpolyglot/ "Front-end Hyperpolyglot")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

React/Angular1,2/Ember/Polymer/Vue의 템플릿 작성 문법을 테이블로 정리해놓은 사이트입니다.

- [Programming Languages - Hyperpolyglot](http://hyperpolyglot.org/ "Programming Languages - Hyperpolyglot")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## epoberezkin/ajv: The fastest JSON schema Validator. Supports v5 proposals
[github.com/epoberezkin/ajv](https://github.com/epoberezkin/ajv "epoberezkin/ajv: The fastest JSON schema Validator. Supports v5 proposals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

JSON Schema validator 라이브러리입니다.

----

## MJB-code6/SkyPort: Add offline functionality to your web app
[github.com/MJB-code6/SkyPort](https://github.com/MJB-code6/SkyPort "MJB-code6/SkyPort: Add offline functionality to your web app")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">library</span></p>

Service Worker를 사용해 오프라인 모드를 대응할 수 있는 라이브러리입니다.

----

## Frend — A collection of accessible, modern front-end components.
[frend.co/](http://frend.co/ "Frend — A collection of accessible, modern front-end components.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">WAI-ARIA</span></p>

Accessible한 DOM UI를 구현하기 위한 JavaScript 라이브러리입니다. CSS 프레임워크 처럼 특정 클래스를 붙인 요소에 WAI-ARIA의 속성을 함께 부여합니다.

----

## GoogleChrome/lighthouse: auditing and performance metrics for Progressive Web Apps
[github.com/GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse "GoogleChrome/lighthouse: auditing and performance metrics for Progressive Web Apps")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Service Worker를 사용해 오프라인을 대응하고 있는지 검사, Speed Index 등을 이용해 페이지 로드 성능 테스트 등 Progressive Web Apps에 관한 측정 도구 입니다.

----
<h1 class="site-genre">도서</h1>

----

## 플러그인 구조에 관해 학습할 수 있는 JavaScript Plugin Architecture라는 무료 전자 서적을 작성했다 | Web Scratch(일본어)
[efcl.info/2016/06/06/JavaScript-Plugin-Architecture/](http://efcl.info/2016/06/06/JavaScript-Plugin-Architecture/ "JavaScript Plugin Architectureというプラグイン設計について学ぶ無料の電子書籍を書いた | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ebook</span></p>

자바스크립트의 라이브러리나 도구의 플러그인 구조에 관해 작성돼 있는 책입니다.
jQuery, ESLint, Connect, gulp, Redux 등 플러그인의 구조를 구현해보면서 학습할 수 있는 전자 서적입니다.

- [azu/JavaScript-Plugin-Architecture: JavaScript 플러그인 아키텍처 책](https://github.com/azu/JavaScript-Plugin-Architecture "azu/JavaScript-Plugin-Architecture: JavaScript 플러그인 아키텍처 책")

----
