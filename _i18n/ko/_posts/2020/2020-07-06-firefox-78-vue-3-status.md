---
title: "2020-07-06: Firefox 78, Vue 3 Status와 릴리스 일정"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-07-06T13:25:56.945Z
category: JSer
tags:
- Firefox
- Vue

---

JSer.info #495 - Firefox 78이 릴리스됐습니다.

- [New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/06/new-in-firefox-78/)
- [Firefox 78.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/)
- [Firefox 78 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/78)

Firefox 78는 [Firefox Extended Support Release](https://support.mozilla.org/kb/choosing-firefox-update-channel)(ESR) 배포 버전입니다. 78이전 마지막 ESR 배포 버전은 Firefox 68 입니다. 이전엔 Service Worker가 비활성화 돼 있었지만 Firefox 78 ESR 부터 지원하게 됐습니다.

- <https://support.mozilla.org/ja/kb/firefox-enterprise-78-release-notes>

Firefox 78에서 개발자 도구가 개선됐습니다.
콘솔에 Promise 에러를 보다 자세하게 출력하며 네트워크 패널에서 리퀘스트 요청 실패의 원인을 표시합니다. 

CSS 관련 내용으로는 `:is`와 `:where`을 지원하며 `:read-only`와 `:read-write`를 prefix 없이 사용할 수 있습니다.
또, 정규 표현 엔진을 새롭게 개발해 ES2018의 Named Capture Groups 등을 지원합니다.

- [A New RegExp Engine in SpiderMonkey - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/06/a-new-regexp-engine-in-spidermonkey/)

이 외로 TLS 1.0과 1.1 지원이 기본적으로 비활성화 됩니다.

- [TLS 1.0/1.1 지원이 초기 설정에서 비활성화 됩니다(영향있음) | Firefox 사이트 호환성 정보](https://www.fxsitecompat.dev/ja/docs/2020/tls-1-0-1-1-support-has-been-disabled-by-default/)(일본어)

----

Vue 3의 릴리스 일정과 제안된 RFC 등의 상황(status)이 공개돼 있습니다.

- [Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs](https://github.com/vuejs/rfcs/issues/183)

본래는 2020년 전반기에 릴리스할 예정이었지만 이를 변경해 Vue 3 RC를 7월 중순에 릴리스하고 Vue 3를 8월 초에 릴리스 할 예정이라고 합니다.
로드맵은 아래 프로젝트 보드에도 자세히 정리돼 있으니 참고하시길 바랍니다.

- [Roadmap](https://github.com/vuejs/vue/projects/6)

이슈에는 개발 중인 패키지 및 상황과 [JSX 지원 관련 논의](https://github.com/vuejs/jsx/issues/141)에 대해서도 소개돼 있으니 참고하시길 바랍니다.

이와 관련하여 Vue 2 용 Vue3 Composition API를 제공하는 [@vue/composition-api](https://github.com/vuejs/composition-api)의 [v1.0.0-beta.1](https://github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1)이 릴리스 돼 있으며 Vue 2와 Vue3 모두를 지원하는 라이브러리를 만들 때 사용할 수 있는 툴킷인 vue-demi도 공개돼 있습니다.

- [antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3](https://github.com/antfu/vue-demi)
- [Make Libraries Working with Vue 2 and 3 - Anthony Fu](https://antfu.me/posts/make-libraries-working-with-vue-2-and-3/)

이 외에도 Vue 3 릴리스 이후에 들어갈지도 모를 RFC 등도 작성돼 있으니 아래 문서를 함께 살펴보시면 좋을 것 같습니다.

- [SFC Improvements by yyx990803 · Pull Request #182 · vuejs/rfcs](https://github.com/vuejs/rfcs/pull/182)
- [Weekly Vue 2020-07-05 - DEV Community 👩‍💻👨‍💻](https://dev.to/rabspice/weekly-vue-2020-07-05-4b12)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v1.0.0-beta.1 · vuejs/composition-api
[github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1](https://github.com/vuejs/composition-api/releases/tag/v1.0.0-beta.1 "Release v1.0.0-beta.1 · vuejs/composition-api")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 2 용 Composition API 구현체인 @vue/composition-api 1.0.0 beta 1이 릴리스 됐습니다.


----

## New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/06/new-in-firefox-78/](https://hacks.mozilla.org/2020/06/new-in-firefox-78/ "New in Firefox 78: DevTools improvements, new regex engine, and abundant web platform updates - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 78이 릴리스됐습니다. ESR 갱신 버전입니다.
콘솔에서 Promise 에러를 보다 자세히 출력하도록 본경됐으며 네트워크 패널에서 요청 실패 원인 표시하는 등 개발자 도구가 개선됐습니다.
CSS의 `:is`와 `:where`를 지원하고 `:read-only`와 `:read-write`를 프리픽스 없이 사용할 수 있습니다.
정규 표현의 Named Cature Groups와 `ParentNode.replaceChildren`를 지원합니다.
TLS 1.0과 1.1이 기본적으로 비성활화 됐습니다.

- [Firefox 78.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/78.0/releasenotes/ "Firefox 78.0, See All New Features, Updates and Fixes")
- [Firefox 78 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/78 "Firefox 78 for developers - Mozilla | MDN")

----

## Release v0.14.0 · video-dev/hls.js
[github.com/video-dev/hls.js/releases/tag/v0.14.0](https://github.com/video-dev/hls.js/releases/tag/v0.14.0 "Release v0.14.0 · video-dev/hls.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hls.js 0.14.0이 릴리스 됐습니다.


----

## Node v14.5.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.5.0/](https://nodejs.org/en/blog/release/v14.5.0/ "Node v14.5.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v14.5.0이 릴리스 됐습니다.
V8 8.3으로 갱신됐으며 `EventTarget`이 시험적으로 구현됐습니다.


----

## V8 release v8.4 · V8
[v8.dev/blog/v8-release-84](https://v8.dev/blog/v8-release-84 "V8 release v8.4 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 8.4(Chrome 84)가 릴리스됐습니다.
WebAssembly SIMD API를 Origin Trial로 이용할 수 있게 됐으며 `WeakRef`, Private methods와 accessors를 지원합니다.


----

## Release v5.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v5.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v5.0.0 "Release v5.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v5.0.0이 릴리스 됐습니다.
`page.emulateMedia`가 `page.emulateMediaType`으로 변경됐으며 Direct require를 삭제하고 객제에서 가져올 수 있도록 변경됐습니다.


----

## Release Version 6.0.0 · react-hook-form/react-hook-form
[github.com/react-hook-form/react-hook-form/releases/tag/v6.0.0](https://github.com/react-hook-form/react-hook-form/releases/tag/v6.0.0 "Release Version 6.0.0 · react-hook-form/react-hook-form")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Hook Form 6.0.0이 릴리스 됐습니다.


----

## Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs
[github.com/vuejs/rfcs/issues/183](https://github.com/vuejs/rfcs/issues/183 "Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

Vue 3의 상태(status)가 정리돼 있습니다.
7월에 RC가 릴리스되고 8월에 정식 버전이 릴리스될 예정입니다.


----

## Release 3.10.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.10.0](https://github.com/avajs/ava/releases/tag/v3.10.0 "Release 3.10.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3.10.0이 릴리스 됐습니다.
`.only()`를 사용하는 중에 스탭샷을 업데이트하지 않도록 개선됐고 `t.timeout`에 메시지 옵션이 추가됐습니다. 
`t.try()`나 `t.snapshot()`을 hook 내에서 실행할 수 없도록 수정됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Sign-in form best practices
[web.dev/sign-in-form-best-practices/](https://web.dev/sign-in-form-best-practices/ "Sign-in form best practices")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

`<form>` / `<input>` / `<label>` / `<button>`을 사용한 폼 작성 관련 체크리스트가 정리돼 있습니다.


----

## Creating an Application Performance Monitor Using Node 14 New and Experimental Features | Medium
[medium.com/@erickwendel/node-v14-x-is-up-deep-diving-into-new-features-ace6dd89ac0b](https://medium.com/@erickwendel/node-v14-x-is-up-deep-diving-into-new-features-ace6dd89ac0b "Creating an Application Performance Monitor Using Node 14 New and Experimental Features | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 14에서 사용할 수 있는 실험적(experimental)인 기능을 사용해 애플리케이션 모니터링 Agent를 만드는 방법을 소개합니다.
Async Local Storage, Diagnostic Reports 등을 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## web.dev LIVE
[web.dev/live/](https://web.dev/live/ "web.dev LIVE")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Conference</span> <span class="jser-tag">video</span> <span class="jser-tag">google</span> <span class="jser-tag">Chrome</span></p>

web.dev의 세션 영상이 공개됐습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Overview | Tooling.Report
[bundlers.tooling.report/](https://bundlers.tooling.report/ "Overview | Tooling.Report")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">document</span></p>

browserify, parcel, rollup, webpack 등, bundler의 기능을 비교 / 정리하는 사이트입니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## preactjs/compressed-size-action: GitHub Action that adds compressed size changes to your PRs.
[github.com/preactjs/compressed-size-action](https://github.com/preactjs/compressed-size-action "preactjs/compressed-size-action: GitHub Action that adds compressed size changes to your PRs.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">library</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

JavaScript 파일의 빌드 크기가 달라졌음을 알려주는 GitHub Actions 입니다.


----

## tom-sherman/immurl: 🔗 A tiny immutable URL library, backed by the native whatwg URL.
[github.com/tom-sherman/immurl](https://github.com/tom-sherman/immurl "tom-sherman/immurl: 🔗 A tiny immutable URL library, backed by the native whatwg URL.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">library</span></p>

`URL`의 immutable 버전입니다.


----

## antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3
[github.com/antfu/vue-demi](https://github.com/antfu/vue-demi "antfu/vue-demi: 🎩 Creates Universal Library for Vue 2 & 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Vue2와 3를 지원하는 라이브러리를 작성하기 위한 툴킷 라이브러리입니다.
Vue2와 3 사이에 호환성이 없기 때문에 두 버전을 모두 지원하는 라이브러리 개발을 도와줍니다.

- [Make Libraries Working with Vue 2 and 3 - Anthony Fu](https://antfu.me/posts/make-libraries-working-with-vue-2-and-3/ "Make Libraries Working with Vue 2 and 3 - Anthony Fu")
- [Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs](https://github.com/vuejs/rfcs/issues/183#issuecomment-651944231 "Vue 3: mid 2020 status update · Issue #183 · vuejs/rfcs")

----
<h1 class="site-genre">도서</h1>

----

## 시작하면서 - 서바이벌 TypeScript(일본어)
[book.yyts.org/](https://book.yyts.org/ "시작하면서 - 서바이벌 TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span> <span class="jser-tag">ebook</span></p>

프로그래밍 경험이 있는 사람을 대상으로 한 TypeScript 학습서입니다.


----
