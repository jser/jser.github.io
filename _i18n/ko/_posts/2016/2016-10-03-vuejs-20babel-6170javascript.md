---
title: "2016-10-03 JS: Vue.js 2.0, Babel 6.17.0, 복잡한 JavaScript"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-10-03T09:49
category: JSer
tags:
    - Vue
    - Babel
    - JavaScript
    - DDD

---

JSer.info #299 Vue.js 2.0이 릴리즈됐습니다.

- [Vue 2.0 is Here! – The Vue Point – Medium](https://medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8)

2.0에는 [snabbdom](https://github.com/snabbdom/snabbdom "snabbdom")을 fork한 Virtual DOM을 도입하기 때문에 요소를 갱신하는 방법이나 라이프 사이클 등, Virtual DOM과 관련된 기능과 아키텍처가 주로 변경됐습니다.
(한편, cycle.js의 개발자는 [snabbdom](https://github.com/snabbdom/snabbdom "snabbdom")의 collaborator가 됐습니다 -[참고](https://github.com/snabbdom/snabbdom/issues/164#issuecomment-248549455)-)

- [2.0 Changes · Issue #2873 · vuejs/vue](https://github.com/vuejs/vue/issues/2873)
- [Vue.js 2.0의 Features를 번역해보다 - Qiita](http://qiita.com/prismrism/items/66a9dfc31139326911d8)(일본어)
- [Vue1.0과 Vue2.0의 달라진 점 - Qiita](http://qiita.com/tanshio/items/88e29877671d5d9f1067 "Vue1.0과 Vue2.0의 달라진 점 - Qiita")(일본어)

또, 1.x에서의 마이그레이션 헬퍼와 가이드도 공개돼 있습니다.

- [vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0](https://github.com/vuejs/vue-migration-helper "vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0")
- [Migration from Vue 1.x - vue.js](http://vuejs.org/guide/migration.html "Migration from Vue 1.x - vue.js")

----

Babel [6.17.0](https://github.com/babel/babel/releases/tag/v6.17.0 "6.17.0")이 릴리즈됐습니다.

[optimize-js](https://github.com/nolanlawson/optimize-js "optimize-js")와 관련된 변경이나 ECMAScript Proposal의 Stage 변경을 각 preset에 반영하는 등 여러가지 변경 사항이 있습니다.

9월에 이뤄진 TC39 MTG에서 논의된 Stage의 변경 사항은 아래 페이지에 잘 정리돼 있습니다.

- [ECMAScript proposal updates @ 2016-10 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

----

[복잡한 자바스크립트 애플리케이션을 염두하여 만들기](http://azu.github.io/slide/2016/react-meetup/large-scale-javascript.html)(일본어)라는 슬라이드에는 대규모 자바스크립트 애플리케이션의 설계에 관해 작성돼 있습니다.

Flux와 CQRS, 1개의 객체가 2가지 이상의 역할을 갖게 될 때 발생할 수 있는 복잡성을 회피할 수 있는 아키텍처 등 대규모 애플리케이션을 생각하면서 고민한 여러가지 내용이 작성돼 있습니다.

이러한 고민을 토대로 탄생한 구현체가 [Almin](https://github.com/almin/almin "Almin") 이며, 이를 활용한 개발 관련 내용은 아래 저장소(문서)에 정리돼 있습니다.

- [azu/large-scale-javascript: 복잡한 자바스크립트 애플리케이션을 개발하기 위해 생각할 것들](https://github.com/azu/large-scale-javascript)

----
<h1 class="site-genre">헤드라인</h1>

----

## Node v6.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.7.0/](https://nodejs.org/en/blog/release/v6.7.0/ "Node v6.7.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.7.0이 릴리즈됐습니다.
시큐리티 릴리즈가 포함된 버전입니다.

----

## Vue 2.0 is Here! – The Vue Point – Medium
[medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8](https://medium.com/the-vue-point/vue-2-0-is-here-ef1f26acf4b8 "Vue 2.0 is Here! – The Vue Point – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.0이 릴리즈됐습니다.
1.x에서의 마이그레이션 헬퍼도 공개돼있습니다.

- [vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0](https://github.com/vuejs/vue-migration-helper "vuejs/vue-migration-helper: CLI tool to aid in migration from Vue 1.x to 2.0")
- [Migration from Vue 1.x - vue.js](http://vuejs.org/guide/migration.html "Migration from Vue 1.x - vue.js")

----

## 6.16.0 Released · Babel
[babeljs.io/blog/2016/09/28/6.16.0](https://babeljs.io/blog/2016/09/28/6.16.0 "6.16.0 Released · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.16.0이 릴리즈됐습니다.
babel-core가 `parserOpts`와 `generatorOpts`을 지원하는 등 다양한 변경 사항이 있습니다.

----

## Release v6.17.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.17.0](https://github.com/babel/babel/releases/tag/v6.17.0 "Release v6.17.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.17.0이 릴리즈됐습니다.
async generator와 object rest-spread를 stage3으로 지정하는 등 Proposal의 Stage 변경을 반영했고, optimize-js과 관련된 사항이 변경됐습니다.

- [ECMAScript proposal updates @ 2016-10 | ECMAScript Daily](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

----

## ESLint v3.7.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/09/eslint-v3.7.0-released](http://eslint.org/blog/2016/09/eslint-v3.7.0-released "ESLint v3.7.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v3.7.0이 릴리즈됐습니다.
코드를 자동으로 수정하는 `--fix` 플래그에 새로운 규칙이 추가되는 등 다양한 변경 사항이 있습니다.

- [ESLint v3.7.0 - Qiita](http://qiita.com/mysticatea/items/dd90aff81eeb92683c5d "ESLint v3.7.0 - Qiita")(일본어)

----

## RE:DOM is now 1.0! – RE:DOM – Medium
[medium.com/re-dom/re-dom-is-now-1-0-58ec0328a59d](https://medium.com/re-dom/re-dom-is-now-1-0-58ec0328a59d "RE:DOM is now 1.0! – RE:DOM – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

RE:DOM 1.0이 릴리즈됐습니다.
RE:DOM용 Fake DOM인 NO:DOM도 함께 공개하고 있습니다.

- [pakastin/redom: Tiny, but super fast DOM library with 100 % test coverage!](https://github.com/pakastin/redom "pakastin/redom: Tiny, but super fast DOM library with 100 % test coverage!")
- [pakastin/nodom: fake DOM for RE:DOM](https://github.com/pakastin/nodom "pakastin/nodom: fake DOM for RE:DOM")

----

## Release v0.33.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.33.0](https://github.com/facebook/flow/releases/tag/v0.33.0 "Release v0.33.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.33.0이 릴리즈됐습니다.

----

## Release Notes for Safari Technology Preview Release 14 | WebKit
[webkit.org/blog/6969/release-notes-for-safari-technology-preview-release-14/](https://webkit.org/blog/6969/release-notes-for-safari-technology-preview-release-14/ "Release Notes for Safari Technology Preview Release 14 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 14가 릴리즈됐습니다.
`URLSearchParams` 구현, safaridriver를 포함하는 등 다양한 변경 사항이 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Node.js debugging with Chrome DevTools (in parallel with browser JavaScript)
[blog.hospodarets.com/nodejs-debugging-in-chrome-devtools](https://blog.hospodarets.com/nodejs-debugging-in-chrome-devtools "Node.js debugging with Chrome DevTools (in parallel with browser JavaScript)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">node.js</span></p>

Node.js를 Chrome의 개발자 도구로 디버깅하는 방법을 설정하는 것부터 순서대로 소개합니다.

----

## Master the DOM – Medium
[medium.com/@pakastin/master-the-dom-bc1a2a06089b](https://medium.com/@pakastin/master-the-dom-bc1a2a06089b "Master the DOM – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">tutorial</span></p>

DOM API를 이용해 DOM Tree의 기본적인 조작을 배워볼 수 있는 글입니다.

----

## Common CSS Mistakes (And How To Fix Them)
[blog.mariano.io/common-css-mistakes-and-how-to-fix-them-8ee0f5e88d64](https://blog.mariano.io/common-css-mistakes-and-how-to-fix-them-8ee0f5e88d64 "Common CSS Mistakes (And How To Fix Them)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSS 작성 시 흔히하는 실수와 수정하는 방법에 관해 작성돼 있습니다.

----

## requestAnimationFrame와 타이머의 새삼스러운 비교와 데모 :: 허브로그(일본어)
[havelog.ayumusato.com/develop/javascript/e725-timer\_vs\_raf.html](https://havelog.ayumusato.com/develop/javascript/e725-timer_vs_raf.html "requestAnimationFrame とタイマーの今更な比較とデモ ::ハブろぐ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

`requestAnimationFrame`과 `setTimeout`의 비교글 입니다.
`setTimeout`는 세심한 처리에도 영향을 받기 쉽다는 이야기가 작성돼 있습니다.

----

## hemanth/es-next: stage-0 to stage-4 ECMAscript proposals.
[github.com/hemanth/es-next](https://github.com/hemanth/es-next "hemanth/es-next: stage-0 to stage-4 ECMAscript proposals.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

ECMAScript proposals의 Stage 별 정리 글입니다.
각각 스펙 별 작은 샘플 코드가 작성돼 있습니다.

----

## Loading Polyfills Only When Needed — Philip Walton
[philipwalton.com/articles/loading-polyfills-only-when-needed/](https://philipwalton.com/articles/loading-polyfills-only-when-needed/ "Loading Polyfills Only When Needed — Philip Walton")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

polyfill을 필요할 때 동적으로 불러들이는 방법과 고민에 관해 작성돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 복잡한 자바스크립트 애플리케이션을 염두하여 만들기(일본어)
[azu.github.io/slide/2016/react-meetup/large-scale-javascript.html](http://azu.github.io/slide/2016/react-meetup/large-scale-javascript.html "複雑なJavaScriptアプリケーションを考えながら作る話")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">슬라이드</span> <span class="jser-tag">CQRS</span> <span class="jser-tag">DDD</span></p>

자바스크립트 환경에서 복잡한 애플리케이션을 만드는 경우에 어떻게 설계하는게 좋을지 고민한 내용이 작성돼 있습니다.
도메인 모델을 어떻게 염두해 만들어 나갈지, Babel, React, Almin, PostCSS 등을 베이스로 이야기를 풀어갑니다.

- [azu/large-scale-javascript: 複雑なJavaScriptアプリケーションを作るために考えること](https://github.com/azu/large-scale-javascript "azu/large-scale-javascript: 複雑なJavaScriptアプリケーションを作るために考えること")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## CodePen - React ES6 lifecycles
[codepen.io/netsi1964/full/NRgyZX/](http://codepen.io/netsi1964/full/NRgyZX/ "CodePen - React ES6 lifecycles")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span></p>

React의 라이프 사이클 API가 정리돼 있습니다.
실제로 동작하는 코드가 문서에 포함돼 있어 해당 코드를 동작시켜 보면서 라이프 사이클 메서드의 실행 순서를 이해할 수 있습니다. 

----

## Web Platform Feature Availability
[paulirish.github.io/web-feature-availability/](https://paulirish.github.io/web-feature-availability/ "Web Platform Feature Availability")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">browser</span></p>

CanIUse와 StarCounter를 사용해 개발된 사이트로, 특정 기능을 플랫폼에서 어느정도 비율로 사용할 수 있는 상태인지를 살펴볼 수 있습니다.

----

## React Status: A Free, Weekly Email Newsletter
[react.statuscode.com/](http://react.statuscode.com/ "React Status: A Free, Weekly Email Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">news</span> <span class="jser-tag">mail</span></p>

React를 다루는 Weekly 메일 매거진입니다.

----

## Fix and prevent known vulnerabilities in Node.js apps | Snyk
[snyk.io/](https://snyk.io/ "Fix and prevent known vulnerabilities in Node.js apps | Snyk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">webservice</span></p>

Node.js 모듈의 기존 취약성 등을 감지하여 알려주고 수정할 수 있는 서비스입니다.
CI를 이용해 자동적으로 체크할 수 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mkwtys/bundle-size: Show bundle file size of npm packages
[github.com/mkwtys/bundle-size](https://github.com/mkwtys/bundle-size "mkwtys/bundle-size: Show bundle file size of npm packages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

지정한 패키지의 파일 사이즈를 출력할 수 있는 CLI 도구입니다.
Environment를 지정할 수 있어서 development와 production의 파일 사이즈를 minify와 gzip이 끝난 상태로도 비교할 수 있습니다.

----

## krasimir/navigo: A simple vanilla JavaScript router with a fallback for older browsers
[github.com/krasimir/navigo](https://github.com/krasimir/navigo "krasimir/navigo: A simple vanilla JavaScript router with a fallback for older browsers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

심플한 라우터 라이브러리입니다.
URL 맵핑에 정규표현식도 사용할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## TypeScript Design Patterns - O&#x27;Reilly Media
[shop.oreilly.com/product/9781785280832.do](http://shop.oreilly.com/product/9781785280832.do "TypeScript Design Patterns - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">디자인패턴</span> <span class="jser-tag">book</span></p>

TypeScript의 디자인패턴에 관한 책입니다.

----
