---
title: "2016-03-29 JS: Safari 9.1, Backbone.js의 근황, Web Performance API"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-03-29T09:46
category: JSer
tags:
    - Safari
    - perf
    - backbone.js

---

JSer.info #272 - Backbone.js [1.3.2](http://backbonejs.org/#changelog "1.3.2")가 릴리즈됐습니다.
[The Sad State of the Backbone Ecosystem](http://benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/ "The Sad State of the Backbone Ecosystem")에는 근래의 Backbone.js 에코시스템(생태계)에 관해 작성돼 있습니다.

Backbone.js의 Pulse와 [Marionette.js](https://github.com/marionettejs/backbone.marionette/ "Marionette.js"), 기타 Backbone.js와 관련한 라이브러리의 상황에 관해 작성돼 있습니다.

[JavaScript 정보란 뭐지?](http://azu.github.io/slide/2016/jser5years/javascript-information.html "JavaScript 정보란 뭐지?")(일본어)에서도 GitHub 저장소의 Pulse를 보는 것으로 프로젝트 상황을 어느정도 파악할 수 있다는 이야기를 했었습니다.
Backbone.js의 경우는 더 이상 진행이 안되는 프로젝트도 있어 이 이상 발전하기 어려운 상황으로 판단됩니다.

Backbone.js를 사용하고 있는 분 뿐만 아니라 관련 개발자들이 현재의 상황을 파악하는데 읽어보면 좋을 것 같습니다.

----

[Safari 9.1](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")이 릴리즈됐습니다.

- [Safari 9.1](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")
- [CSS Variables in WebKit | WebKit](https://webkit.org/blog/5989/css-variables-in-webkit/)
- [Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web](http://www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se)

위 문서는 Safari 9.1에서 사용할 수 있게 된 기능을 잘 설명하고 있습니다.
CSS Custom Properties, CSS Will-Change, `<picture>` 요소, Fast Tap 삭제 뿐만 아니라 여러가지 새로운 기능도 다루고 있습니다.

----

[브라우저의 Performance API 이야기](http://www.slideshare.net/kawada_hiroshi/performance-api "브라우저의 Performance API 이야기")(일본어)라는 슬라이드에는 브라우저에서 사용할 수 있는 성능 측정 용 API에 관해 작성돼 있습니다.

슬라이드 내에서도 소개하고 있습니다만, Timing API 관해서는 [A Primer for Web Performance Timing APIs](https://w3c.github.io/perf-timing-primer/ "A Primer for Web Performance Timing APIs")라는 문서에 잘 정리돼 있습니다.

또, 성능과 관련해 Google 등이 주도하는 [Accelerated Mobile Pages (AMP)](https://www.ampproject.org/ "Accelerated Mobile Pages (AMP)")에 대응한, [Content Performance Policy (CPP)](https://discourse.wicg.io/t/content-performance-policy/1380/1 "Content Performance Policy") 제안도 있습니다.

CPP는 아직 아이디어에 수준이며, 이 아이디어에 함께 [@igrigorik](https://github.com/igrigorik "igrigorik")으로 부터 Sandbox Policy라는 사양도 제안 되고 있습니다.

- [Proposal: Sandbox Policy - HTML - WICG](https://discourse.wicg.io/t/proposal-sandbox-policy/1414 "Proposal: Sandbox Policy - HTML - WICG")

이것은 기존의 `<iframe sandbox>`를 확장한 개념(옵트-인, 옵트-아웃 정도의 차이점은 있음)으로, `document.write`를 금지하는 디렉티브의 추가 등이 포함돼 있습니다.

개발 측에게 일종의 서브셋과 같은 제한을 받아들이도록 하여 빠르게 렌더링을 할 수 있도록하는 규칙을 정하고 있는 형태입니다.

성능에 관심이 있는 사람이 이와 관련한 부분을 살펴보면 좋을 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Backbone.js
[backbonejs.org/](http://backbonejs.org/ "Backbone.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">ReleaseNote</span></p>

Backbone. 1.3.2가 릴리즈됐습니다.
`findIndex`와 `findLastIndex`를 추가했고, `component.json` 지원을 종료했습니다.

- [Remove component.json support? · Issue #2601 · marionettejs/backbone.marionette](https://github.com/marionettejs/backbone.marionette/issues/2601 "Remove component.json support? · Issue #2601 · marionettejs/backbone.marionette")

----

## Release v1.0.0 · mozilla/sweet.js
[github.com/mozilla/sweet.js/releases/tag/v1.0.0](https://github.com/mozilla/sweet.js/releases/tag/v1.0.0 "Release v1.0.0 · mozilla/sweet.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScript에서 hygienic macros을 실현하는 라이브러리인 sweet.js 1.0.0이 릴리즈됐습니다.

- [Redesign by disnet · Pull Request #485 · mozilla/sweet.js](https://github.com/mozilla/sweet.js/pull/485 "Redesign by disnet · Pull Request #485 · mozilla/sweet.js")

----

## ESLint v2.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/03/eslint-v2.5.0-released](http://eslint.org/blog/2016/03/eslint-v2.5.0-released "ESLint v2.5.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.5.0이 릴리즈됐습니다.
의존하고 있는 라이브러리도 ESLint의 패키지에 포함해 배포될 수 있도록 `bundledDependencies`를 이용하도록 변경됐고, 몇가지 규칙이 추가/수정 됐습니다.

- [ESLint v2.5.0 - Qiita](http://qiita.com/mysticatea/items/7018ca26abfa7701debc "ESLint v2.5.0 - Qiita")

----
<h1 class="site-genre">아티클</h1>

----

## Safari 9.1
[developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari\_9\_1.html](https://developer.apple.com/library/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9_1.html "Safari 9.1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 9.1의 변경 사항에 관해 작성돼 있습니다.
`<picture>` 요소 지원, Web Inspector 개선, Fast Tap 삭제, Canvas에 `imageSmoothingQuality` 프로퍼티 추가, CSS Custom Properties 지원 등 여러가지 변경 사항을 소개합니다.

----

## CSS Variables in WebKit | WebKit
[webkit.org/blog/5989/css-variables-in-webkit/](https://webkit.org/blog/5989/css-variables-in-webkit/ "CSS Variables in WebKit | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Safari 9.1에서 지원하는 CSS Custom Properties를 소개합니다.
`--name`으로 변수를 정의하고, CSS 내에서 `var(--name)`으로 참조 가능합니다.
JavaScript에서도 `getPropertyValue/setProperty`로 읽어들일 수 있습니다.

----

## Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web
[www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se](http://www.mobilexweb.com/blog/safari-on-ios-9-3-picture-shrink-fit-iphone-se "Safari on iOS 9.3, Responsive Images, iPhone SE, shrink-to-fit and other new APIs | Breaking the Mobile Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

iOS 9.3의 Safari에 관해 작성돼 있습니다.
`<picture>`, Fast Tap removed, CSS Custom Properties, 다이얼로그 변경, `shrink-to-fit`, Remote Inspector 등 여러가지 변경 사항에 관해 자세히 소개합니다.

----

## JSDoc을 런타임 assert로 변환하는 Babel 플러그인을 만들었다 | Web Scratch(일본어)
[efcl.info/2016/03/25/jsdoc-to-assert/](http://efcl.info/2016/03/25/jsdoc-to-assert/ "JSDoc을 런타임 assert로 변환하는 Babel 플러그인을 만들었다 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">babel</span></p>

JSDoc을 assert로 변환하는 Babel 플러그인을 소개합니다.
JSDoc의 타입 주석을 런타임 assert로 변환하여 정의한 변수와 실제 전달된 값이 일치하는지 검증할 수 있습니다.

----

## Shadow DOM CSS Cheat Sheet
[robdodson.me/shadow-dom-css-cheat-sheet/](http://robdodson.me/shadow-dom-css-cheat-sheet/ "Shadow DOM CSS Cheat Sheet")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Shadow DOM의 CSS(`:host` 등), CSS Custom Properties(`--var`)와 관련한 속성을 정리한 치트시트입니다.

----

## Status of Static Typing in ECMAScript | ECMAScript Daily
[ecmascript-daily.github.io/pages/status-of-static-typing-in-ecmascript/](https://ecmascript-daily.github.io/pages/status-of-static-typing-in-ecmascript/ "Status of Static Typing in ECMAScript | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">정리</span></p>

ECMAScript에서 진행하는 정적 타입과 관련한 Proposal의 상태가 정리돼 있습니다.

----

## Gordux.js - The redux pattern in vanilla.js
[k94n.com/gordux-js-the-redux-pattern-in-vanilla-js](https://k94n.com/gordux-js-the-redux-pattern-in-vanilla-js "Gordux.js - The redux pattern in vanilla.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span></p>

Redux와 같은 데이터 플로우를 순수 JavaScript로 구현하는 과정이 작성돼 있습니다.
Event로는 Custom Event를 사용해 Pub/Sub을 구현합니다.

----

## The Sad State of the Backbone Ecosystem
[benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/](http://benmccormick.org/2016/03/07/the-sad-state-of-the-backbone-ecosystem/ "The Sad State of the Backbone Ecosystem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span></p>

Backbone.js의 에코시스템의 상태에 관해 작성돼 있습니다.
Backbone.js와 Marionette, 관련 라이브러리의 상황이 잘 정리돼 있습니다.

----

## GitHub - benoitvallon/computer-science-in-javascript: Computer science reimplemented in JavaScript
[github.com/benoitvallon/computer-science-in-javascript](https://github.com/benoitvallon/computer-science-in-javascript "GitHub - benoitvallon/computer-science-in-javascript: Computer science reimplemented in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">algorithm</span></p>

JavaScript를 활용한 데이터 구조 및 정렬 알고리즘의 구현 예를 소개합니다.

- [Data Structures in JavaScript posts - Ben&#x27;s Blog](http://blog.benoitvallon.com/category/data-structures-in-javascript/ "Data Structures in JavaScript posts - Ben&#x27;s Blog")

----

## Sinon Tutorial: JavaScript Testing with Mocks, Spies &amp; Stubs
[www.sitepoint.com/sinon-tutorial-javascript-testing-mocks-spies-stubs/](http://www.sitepoint.com/sinon-tutorial-javascript-testing-mocks-spies-stubs/ "Sinon Tutorial: JavaScript Testing with Mocks, Spies & Stubs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Sinon.js를 사용한 테스트 방법에 관해 작성돼 있습니다.
Sinon.js의 mock, stub, spy 등을 소개합니다.

----

## Promise-based functions should not throw exceptions
[www.2ality.com/2016/03/promise-rejections-vs-exceptions.html](http://www.2ality.com/2016/03/promise-rejections-vs-exceptions.html "Promise-based functions should not throw exceptions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Promises</span></p>

Promise를 기반으로하는 async/await를 함께 살펴보면서 Promise를 반환하는 함수는 예외를 발생시키지 말고 `reject`한 Promise 객체를 반환해야한다는 규칙에 대해 이야기합니다.

- [JavaScript Promise 책](http://azu.github.io/promises-book/#not-throw-use-reject "JavaScript Promise 책")(일본어)
- [JavaScript Promise](http://www.hanbit.co.kr/ebook/look.html?isbn=9788968487293)의 5.3 throw 대신 reject 사용(한국어)

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## ng-japan 2016 세션 자료 정리 - Qiita(일본어)
[qiita.com/nyamogera/items/b83833d1e15a55d0bb66](http://qiita.com/nyamogera/items/b83833d1e15a55d0bb66 "ng-japan 2016 セッション資料まとめ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">이벤트</span></p>

ng-japan 2016의 발표 영상과 슬라이드가 정리돼 있습니다.

- [ng-japan - The Angular conference in Tokyo, Japan (2016/3/21)](http://ngjapan.org/ "ng-japan - The Angular conference in Tokyo, Japan (2016/3/21)")

----

## The Case for CSS Modules
[markdalgleish.github.io/presentation-the-case-for-css-modules/](http://markdalgleish.github.io/presentation-the-case-for-css-modules/ "The Case for CSS Modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">슬라이드</span></p>

CSS Modules에 관해 소개하는 슬라이드입니다.

- [css-modules/css-modules: Documentation about css-modules](https://github.com/css-modules/css-modules "css-modules/css-modules: Documentation about css-modules")

----

## Fluent Conf 2016: Jeremy Fairbank - The rise of async JavaScript - YouTube
[www.youtube.com/watch?v=QtgR94Q2pt4](https://www.youtube.com/watch?v=QtgR94Q2pt4 "Fluent Conf 2016: Jeremy Fairbank - The rise of async JavaScript - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">영상</span></p>

async/await가 동작하는 원리를 Promise 기반으로 설명합니다.
에러 헨들링의 동작과 async function이 어떻게 동작하는지 살펴볼 수 있습니다.

- [Fluent Conf: Rise of Async JavaScript // Speaker Deck](https://speakerdeck.com/jfairbank/fluent-conf-rise-of-async-javascript "Fluent Conf: Rise of Async JavaScript // Speaker Deck")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## A Primer for Web Performance Timing APIs
[w3c.github.io/perf-timing-primer/](https://w3c.github.io/perf-timing-primer/ "A Primer for Web Performance Timing APIs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">document</span></p>

Web Performance Timing API의 개요를 정리한 문서입니다.

- [브라우저의 Performance API 이야기](http://www.slideshare.net/kawada_hiroshi/performance-api "브라우저의 Performance API 이야기")(일본어)

----

## WebpackBin
[www.webpackbin.com/](http://www.webpackbin.com/ "WebpackBin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webpack</span> <span class="jser-tag">webservice</span></p>

http://requirebin.com/ 의 webpack 버전입니다.
HTML/CSS/JavaScript를 작성해 공개할 수 있는 서비스입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## GitHub - ozkxr/match: An JavaScript library to test JSON with some nice features.
[github.com/ozkxr/match](https://github.com/ozkxr/match "GitHub - ozkxr/match: An JavaScript library to test JSON with some nice features.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">JSON</span></p>

predicate 함수의 결과를 사용한 match 라이브러리입니다. JSON 등을 테스트할 수 있습니다.

----

## tusharmath/funjector: Dependency injection for functional paradigm
[github.com/tusharmath/funjector](https://github.com/tusharmath/funjector "tusharmath/funjector: Dependency injection for functional paradigm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

함수에 대응한 DI 라이브러리입니다.
부분으로 적용 가능한 함수를 만들고, 그것에 inject할 수 있는 구조를 제공합니다.

----

## pmdartus/snapline: Unleash your screenshots stored in Chrome Devtool timeline files
[github.com/pmdartus/snapline](https://github.com/pmdartus/snapline "pmdartus/snapline: Unleash your screenshots stored in Chrome Devtool timeline files")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">사진</span></p>

Chrome 개발자 도구의 타임라인을 GIF 애니메이션 사진으로 변환할 수 있는 도구입니다.
타임라인 결과 파일을 분석해 GIF 파일로 생성합니다.

----
<h1 class="site-genre">도서</h1>

----

## Majesty Of… by Alex Kyriakidis et al. [Leanpub PDF/iPad/Kindle]
[leanpub.com/vuejs/](https://leanpub.com/vuejs/ "Majesty Of… by Alex Kyriakidis et al. \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Vue.js를 다루는 전자 서적입니다.

- [hootlex/the-majesty-of-vuejs: educational](https://github.com/hootlex/the-majesty-of-vuejs "hootlex/the-majesty-of-vuejs: educational")

----
