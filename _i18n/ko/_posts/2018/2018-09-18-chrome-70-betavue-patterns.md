---
title: "2018-09-18 JS: Chrome 70 beta, 세로쓰기 구현, Vue Patterns"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-09-18T01:52:53.161Z
category: JSer
tags:
- chrome
- vue
- css

---

JSer.info #401 - Chrome 70β가 릴리스됐습니다.

- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html)


Shape Detection API을 [origin trial](https://blog.jxck.io/entries/2016-09-29/vender-prefix-to-origin-trials.html)로 공개했고 Credential Management API에서 지문 인증과 Web Worker에서의 `name` 옵션 그리고 TLS 1.3을 지원합니다.

Web Components v0(Custom Elements v0, HTML Imports, Shadow DOM v0)이 비권장(deprecated) 됐습니다.
비권장 이후 삭제까지의 일정은 아래 메일링리스트에 쓰여 있듯 Origin trials로 이용 범위를 줄여나가 최종적으로 2020년 Q2에서 삭제될 예정입니다.

- [Intent to Deprecate and Remove: Shadow DOM V0, Custom Elements V0, HTML Imports - Google 그룹](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/h-JwMiPUnuU/sl79aLoLBQAJ)

이 비권장 건을 위해 드물게 Origin Trial을 사용한 것에 대해서는 다음 Podcast에서 이야기하고 있으니 자세한 내용이 궁금한 분은 참고하시길 바랍니다.

- [ep40 Monthly Web 201807 | mozaic.fm](https://mozaic.fm/episodes/40/monthly-web-201807.html)(일본어) 0:29:00~

----

[카쿠요무(kakuyomu)에서의 세로 구조 출력 구현과 세로쓰기 웹의 미래를 향하여 (builderscon tokyo 2018) - Hatena Developer Blog](http://developer.hatenastaff.com/entry/2018/09/11/152905)(일본어)에서는 세로 구조 출력 사이트를 만들기 위한 웹표준과 현 구현 문제 그리고 회피 방법에 대해 작성돼 있습니다.
CSS를 사용한 세로 구조 구현에 관해 소개돼 있으며 브라우저 고유 문제가 있는데 이를 어떻게 대처했는지에 대해서도 다루고 있습니다.

또, 세로 구조와 관련된 CSS의 사양으로 [CSS3 module: text](https://www.w3.org/TR/2001/WD-css3-text-20010517/)와 [CSS Writing Modes Module Level 3](https://www.w3.org/TR/2010/WD-css3-writing-modes-20101202/)가 있으며 이 사양 책정과 관련된 [@fantasai](https://twitter.com/fantasai)의 인터뷰 글도 최근 공개됐으니 함께 살펴보면 좋을 거 같습니다.

- [저의 목표(Goal)는 세계의 언어로 CSS를 사용할 수 있도록 하는 것. EPUB3에서 세로쓰기를 구현한 fantasai（에리카 에테마드）에게 듣다](https://www.aplab.jp/fantasai)(일본어)

----

[Vue Patterns](https://learn-vuejs.github.io/vue-patterns/) 문서에는 Vue 컴포넌트와 관련된 패턴이 소개돼 있습니다.

기본적인 컴포넌트 선언 방식과 사용 방법, 에러 핸들링, Composition, HOC와 Render Props 패턴 등 주로 컴포넌트 작성 방법과 관련된 내용이 정리돼 있습니다.

----

## 공지사항

[JSer.info 400회 기념 이벤트](https://jser.connpass.com/event/100092/)는 이번주 토요일에 사이보즈(cybozu)주식회사(도쿄 사무실)에서 개최할 예정입니다.

- [2018년 9월 22일(토)에 JSer.info 400회째 기념 이벤트를 개최합니다 - JSer.info](https://jser.info/2018/08/31/jser-400-event-announce/)

참가 인원은 아슬하게 초과됐지만 행사 당일 취소하는 경우도 있으니 참가하고 싶은 분은 가능한한 미리 신청 부탁드립니다. 당일 입장에 필요한 **ID**를 connpass의 메시지로 보내기 때문에 보궐되더라도 사전에 등록해두는 편이 안전합니다.

당일 필요한 것은 다음과 같습니다.

- Connpass에서 메일로 전달된 ID(7F 출입 단말기에서 ID를 입력하여 출입증을 발행해 이용)
- JavaScript Discussion에서 묻고 싶은 것
  - 사전에 정리해두고 싶은 사람은 [사전 질문용 SpreadSheet](https://docs.google.com/spreadsheets/d/1pk1Nw4B5eo5mwOcQUo3ipVdwBOAeTkWCWbwW8I5e8Iw/edit#gid=0)에 작성해주세요.
- 참가하는 사람은 1000엔 준비
- 라이트닝톡을 하고 싶은 분은 라이트닝 톡 준비

이 외에 뭔가 묻고 싶은게 있는 사람은 [JSer.info 400회 기념 이벤트 · Issue #102 · jser/jser.info](https://github.com/jser/jser.info/issues/102)를 참고해 주세요.

그럼, 만날 날을 즐거운 마음으로 기다리고 있겠습니다. 

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 3.1 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/09/13/announcing-typescript-3-1-rc/](https://blogs.msdn.microsoft.com/typescript/2018/09/13/announcing-typescript-3-1-rc/ "Announcing TypeScript 3.1 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.1 RC가 릴리스됐습니다.
Mapped Type에서 Tuple과 Array를 다루는 방식이 개선됐으며 함수에 프로퍼티를 정의할 수 있도록 변경됐습니다.
또, 비호환적 변경 사항으로 3.1부터 `lib.d.ts`을 Web IDL을 기반으로 생성하기 때문에 벤더 독자적 타입이 삭제됐으며 `typeof foo === "function"` type gurde의 동작 방식이 변경됐습니다.

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes "Breaking Changes · Microsoft/TypeScript Wiki")

----

## Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more
[blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 70이 릴리스됐습니다.
Shape Detection API을 origin trial로 공개, Web Authentication에서 지문 인증 지원, Web Worker에서의 `name` 옵션, TLS 1.3 지원, Web Components v0 비권장 등이 이뤄졌습니다.


----

## Acorn 6.0.0 released - Acorn - discuss.Tern
[discuss.ternjs.net/t/acorn-6-0-0-released/230](https://discuss.ternjs.net/t/acorn-6-0-0-released/230 "Acorn 6.0.0 released - Acorn - discuss.Tern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript 파서 Acorn 6.0.0이 릴리스됐습니다.
TypeScript 타입 정의 파일이 포함됐고 `ecmaVersion`의 기본값이 `9`로 변경됐으며 몇 가지 내부 처리 로직이 별도 패키지로 분리됐습니다.


----

## neonious/lowjs: A port of Node.JS with far lower system requirements. Community version for POSIX systems such as Linux, uClinux or Mac OS X.
[github.com/neonious/lowjs](https://github.com/neonious/lowjs "neonious/lowjs: A port of Node.JS with far lower system requirements. Community version for POSIX systems such as Linux, uClinux or Mac OS X.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

파일사이즈가 2MB 정도인 임베디드용 Node.js 포트로 V8 대신 Duktape를 사용하고 있습니다.


----

## Release v3.0.0 · janl/mustache.js
[github.com/janl/mustache.js/releases/tag/v3.0.0](https://github.com/janl/mustache.js/releases/tag/v3.0.0 "Release v3.0.0 · janl/mustache.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

mustache.js 3.0.0이 릴리스됐습니다.
원시 타입의 프로퍼티 렌더링이 대응됐으며 `render`의 네번째 인수로 delimiter를 지정할 수 있도록 변경됐고 캐시 문제가 해결됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## 카쿠요무(kakuyomu)에서의 세로 구조 출력 구현과 세로쓰기 웹의 미래를 향하여 (builderscon tokyo 2018) - Hatena Developer Blog
[developer.hatenastaff.com/entry/2018/09/11/152905](http://developer.hatenastaff.com/entry/2018/09/11/152905 "카쿠요무(kakuyomu)에서의 세로 구조 출력 구현과 세로쓰기 웹의 미래를 향하여 (builderscon tokyo 2018) - Hatena Developer Blog")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

세로쓰기를 표현했을 때의 브라우저 버그나 문제를 대응하는 방법에 관해 정리돼 있습니다.


----

## Introducing the React Profiler – React Blog
[reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html](https://reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html "Introducing the React Profiler – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React 16.5에서 지원하는 프로파일과 개발자 도구에 관해 정리돼 있습니다.
개발자 도구에서의 측정 방법(dev/prod)와 사용 방법에 관해 작성돼 있습니다.


----

## Why React16 is a blessing to React developers – freeCodeCamp.org
[medium.freecodecamp.org/why-react16-is-a-blessing-to-react-developers-31433bfc210a](https://medium.freecodecamp.org/why-react16-is-a-blessing-to-react-developers-31433bfc210a "Why React16 is a blessing to React developers – freeCodeCamp.org")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16에 추가된 기능을 소개합니다.
`componentDidCatch` 에러 핸들링, Fragments, Portal, Custom DOM Attributes에 관해 정리돼 있습니다.
또, Ref 관련 API와 추가된 Context API, 라이프사이클 변경에 관해서도 다루고 있습니다.


----

## Operational Introduction to Algebraic Effects and Continuations
[gist.github.com/yelouafi/57825fdd223e5337ba0cd2b6ed757f53](https://gist.github.com/yelouafi/57825fdd223e5337ba0cd2b6ed757f53 "Operational Introduction to Algebraic Effects and Continuations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

redux-saga 개발자가 연재하는 JavaScript의 Algebraic Effects를 주제로 한 글입니다.
Continuation Passing Style(CPS)에 관해 정리돼 있습니다.


----

## Vue conference and meetup videos from 2018 (Q1 digest) - MeetupFeed
[blog.meetupfeed.com/vue-conference-and-meetup-videos-from-2018-q1-digest/](https://blog.meetupfeed.com/vue-conference-and-meetup-videos-from-2018-q1-digest/ "Vue conference and meetup videos from 2018 (Q1 digest) - MeetupFeed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">video</span> <span class="jser-tag">Vue</span></p>

Vue와 관련된 컨퍼런스나 이벤트 등의 발표 자료와 동영상을 정리한 글입니다.
각 발표에 대한 개요와 함께 발표를 볼 수 있는 링크가 정리돼 있습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Web 프런트엔드 성능 개선 핸드북을 공개했습니다 - dwango on GitHub
[dwango.github.io/articles/web-frontend-performance-handbook/](https://dwango.github.io/articles/web-frontend-performance-handbook/ "Web 프런트엔드 성능 개선 핸드북을 공개했습니다 - dwango on GitHub")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">performance</span></p>

웹 사이트의 성능 개선에 관한 문서입니다. 런타임과 페이지 로드 타임과 관련한 문제를 찾는 방법 및 개선 사례에 대해 정리돼 있습니다.

- [Introduction · Web 프런트엔드 성능 개선 핸드북](https://dwango-js.github.io/performance-handbook/ "Introduction · Web 프런트엔드 성능 개선 핸드북")

----

## Vue Patterns
[learn-vuejs.github.io/vue-patterns/](https://learn-vuejs.github.io/vue-patterns/ "Vue Patterns")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

Vue와 관련한 패턴이 정리돼 있는 문서입니다.
기본적인 컴포넌트 작성 방법과 사용법, 에러 핸들링, Composition, HOC나 Render Props 등의 패턴을 소개합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## UmiJS
[umijs.org/](https://umijs.org/ "UmiJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

Next.js와 비슷한 JavaScript 프레임워크입니다.
webpack을 사용한 빌드, 개발 서버, Nuxt.js와 같은 루틴을 제공하고 플러그인 확장 수단을 지원합니다


----

## axa-group/nlp.js: An NLP library built in node over Natural, with entity extraction, sentiment analysis, automatic language identify, and so more
[github.com/axa-group/nlp.js](https://github.com/axa-group/nlp.js "axa-group/nlp.js: An NLP library built in node over Natural, with entity extraction, sentiment analysis, automatic language identify, and so more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">nlp</span></p>

여러가지 자연 언어에 대응하고 있는 NLP 라이브러리입니다.
언어 추정, Classifier, levenshtein 거리 등 자연 언어 처리에서 사용하는 여러가지 기능이 구현돼 있습니다. 


----

## getgauge/taiko: A node.js library to automate chrome/chromium browser
[github.com/getgauge/taiko](https://github.com/getgauge/taiko "getgauge/taiko: A node.js library to automate chrome/chromium browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">console</span></p>

REPL로 Chrome을 조작할 수 있으며 조작에 사용한 코드를 일괄로 출력할 수 있는 도구입니다.


----

## intoli/user-agents: A JavaScript library for generating random user agents with data that's updated daily.
[github.com/intoli/user-agents](https://github.com/intoli/user-agents "intoli/user-agents: A JavaScript library for generating random user agents with data that's updated daily.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

임의의 UA(User Agent)를 생성할 수 있는 라이브러리입니다.
모바일이나 특정 범위의 UA 등을 지정하여 생성 할 수도 있습니다.


----

## SamVerschueren/tsd-check: Check TypeScript type definitions
[github.com/SamVerschueren/tsd-check](https://github.com/SamVerschueren/tsd-check "SamVerschueren/tsd-check: Check TypeScript type definitions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

TypeScript 형 정의 검증 라이브러리입니다. Generics를 이용해 assertion 처럼 사용할 수 있습니다.


----
