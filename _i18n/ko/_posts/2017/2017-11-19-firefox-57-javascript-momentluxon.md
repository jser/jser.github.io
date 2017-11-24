---
title: "2017-11-19 JS: Firefox 57, JavaScript의 비용, moment와 Luxon"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-11-19T10:51:22.569Z
category: JSer
tags:
- Firefox
- Performance
- Date
- Moment
- i18n

---

JSer.info #358 - Firefox 57이 릴리즈 됐습니다.

- [Firefox — Notes (57.0) — Mozilla](https://www.mozilla.org/en-US/firefox/57.0/releasenotes/)
- [Introducing the New Firefox: Firefox Quantum - The Mozilla Blog](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/)

[Project Quantum](https://medium.com/mozilla-tech/a-quantum-leap-for-the-web-a3b7174b3c12 "Project Quantum")이라고 불리던 Firefox의 대규모 개선 프로젝트의 첫 릴리즈 버전입니다.
Quantum CSS(Stylo)라고 불리는 새롭게 개발된 CSS 엔진이 포함된 릴리즈이기 때문에 기존 CSS와 동작(버그 수정을 포함해)이 다른 부분이 있을 수 있습니다.

자세한 내용은 아래 글을 참고해주세요.

- [Inside a super fast CSS engine: Quantum CSS (aka Stylo) – Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2017/08/inside-a-super-fast-css-engine-quantum-css-aka-stylo/ "Inside a super fast CSS engine: Quantum CSS (aka Stylo) – Mozilla Hacks – the Web developer blog")
- [Firefox Quantum 57 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/57 "Firefox Quantum 57 for developers - Mozilla | MDN")

`PerformanceObserver`의 효율성이 개선됐고 Fetch를 abort할 수 있는 [AbortController](https://developer.mozilla.org/ja/docs/Web/API/AbortController "AbortController")가 대응됐습니다. 또, Windows Firefox의 기본 폰트가 변경됐습니다.

- [일본어의 기본 폰트가 변경됐습니다 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/docs/2017/japanese-default-fonts-have-been-changed/ "일본어의 기본 폰트가 변경됐습니다 | Firefox 사이트 호환성 정보")(일본어)

----

[The Cost Of JavaScript – Dev Channel – Medium](https://medium.com/dev-channel/the-cost-of-javascript-84009f51e99e "The Cost Of JavaScript – Dev Channel – Medium")에는 JavaScript 실행 비용에 대해에 대해 작성돼 있습니다.

JavaScript의 비용은 네트워크에서의 로드, 파싱, 컴파일, 실행 순 으로 측정 됩니다.

이때 파싱과 컴파일이 낮은 사양의 디바이스에서는 큰 비율을 차지할 수 있습니다.
때문에, 같은 사이즈의 JavaScript, 이미지 파일이라 하더라도 실행 또는 렌더링까지의 시간이 다를 수 있습니다.

이러한 측면에 대해 이야기하고 대책 방법 중 대표적인 PRPL 패턴과 Performance Budget에 대해 소개합니다.

----

날짜와 시간을 처리할 수 있는 라이브러리인 [moment/luxon: A library for working with dates and times in JS](https://github.com/moment/luxon "moment/luxon: A library for working with dates and times in JS")의 알파 버전이 릴리즈됐습니다.

본래 [moment](https://github.com/moment/moment "moment")-lab 프로젝트에서 시작된 라이브러리로 moment의 문제점 중 하나인 [mutable](https://github.com/moment/moment-rfcs/pull/2) 특징을 해결한 라이브러리입니다.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Wondering about the future of Moment, modularization, etc? We have what we&#39;ll call a &#39;moment-labs&#39; project here: <a href="https://t.co/tFxIq9lEjm">https://t.co/tFxIq9lEjm</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Want a smaller, immutable date library for modern browsers? Luxon has officially joined the family! <a href="https://t.co/HSjRuRuZG1">https://t.co/HSjRuRuZG1</a></p>&mdash; moment.js (@momentjs) <a href="https://twitter.com/momentjs/status/923982141704192000?ref_src=twsrc%5Etfw">October 27, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

[For Moment users](https://moment.github.io/luxon/docs/manual/faq/moment.html "For Moment users")에도 작성돼 있습니다만 Moment API 와의 호환성은 없습니다.

특징적인 부분은 날짜 / 시간 / 인터벌 조작 / 파싱 / 포맷을 등을 지원한다는 점이며 moment와 다르게 Immutable 한 API로 디자인돼 있다는 것입니다. 또, TimeZone과 Intl을 사용한 국제화에도 대응하고 있습니다.

그리고 Luxon은 네이티브 Date, Moment, Date-fns와 달리 month를 `1-indexed`한 값으로 다루고 있습니다.

```js
// 2017-01-01
const date20170101 = new Date("2017-01-01T00:00:00.000Z");
// Luxon - 1-index
const { DateTime }  = require('luxon');
console.log("Luxon:get:" + DateTime.fromJSDate(date20170101).month); // => 1
console.log("Luxon:set:" + DateTime.fromJSDate(date20170101).set({ month: 1 }).month); // => 1
// date-fns - 0-indexed
const {getMonth, setMonth} = require('date-fns');
console.log("date-fns:get:"+ getMonth(date20170101)); // => 0
console.log("date-fns:set:"+ getMonth(setMonth(new Date(2017, 1, 1), 0))); // => 0
// moment - 0-indexed
const moment = require('moment');
console.log("moment:get:"+ moment(date20170101).month()); // => 0
console.log("moment:set:"+ moment(date20170101).month(0).month()); // => 0
```

- [Luxon - data-fns - moment | RunKit](https://runkit.com/azu/5a117a65dcefad0012187983 "Luxon - data-fns - moment | RunKit")

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v0.59.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.59.0](https://github.com/facebook/flow/releases/tag/v0.59.0 "Release v0.59.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.59.0이 릴리즈 됐습니다.
`$ReadOnly<T>` utility type이 추가됐고 성능이 개선됐습니다. 또, `/* flowlint sketchy-null:error */`와 같이 코멘트로 Lint를 활성화할 수 있도록 변경됐습니다.

----

## Node v9.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v9.2.0/](https://nodejs.org/en/blog/release/v9.2.0/ "Node v9.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 9.2.0이 릴리즈 됐습니다.
`fs.realpathSync.native`와 `fs.realpath.native` 그리고 `process.ppid`가 expose 됐습니다.

----

## Release Notes for Safari Technology Preview 44 | WebKit
[webkit.org/blog/8035/release-notes-for-safari-technology-preview-44/](https://webkit.org/blog/8035/release-notes-for-safari-technology-preview-44/ "Release Notes for Safari Technology Preview 44 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 44가 릴리즈 됐습니다.
Payment Request가 기본적으로 활성화 됐고, `createImageBitmap()` 메서드가 구현됐습니다. 또, OffscreenCanvas의 IDL이 추가됐습니다.

----

## Introducing security alerts on GitHub
[github.com/blog/2470-introducing-security-alerts-on-github](https://github.com/blog/2470-introducing-security-alerts-on-github "Introducing security alerts on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">github</span> <span class="jser-tag">security</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ruby</span> <span class="jser-tag">news</span></p>

GitHub 저장소에 npm이나 gem의 보안 경보 기능이 추가됐습니다.

----

## Release v4.0.0-beta.1 · reactjs/redux
[github.com/reactjs/redux/releases/tag/v4.0.0-beta.1](https://github.com/reactjs/redux/releases/tag/v4.0.0-beta.1 "Release v4.0.0-beta.1 · reactjs/redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Redux v4.0.0-beta.1이 릴리즈 됐습니다.
TypeScript의 재작성이 이뤄졌고 `INIT`가 랜덤한 값으로 변경됐습니다. 또, IE11 미만 브라우저에 대한 지원이 종료됐으며 Dispatch의 성능이 개선 됐습니다.

- [Redux 4 breaking changes · Issue #1342 · reactjs/redux](https://github.com/reactjs/redux/issues/1342 "Redux 4 breaking changes · Issue #1342 · reactjs/redux")

----

## Firefox — Notes (57.0) — Mozilla
[www.mozilla.org/en-US/firefox/57.0/releasenotes/](https://www.mozilla.org/en-US/firefox/57.0/releasenotes/ "Firefox — Notes (57.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 57이 릴리즈 됐습니다.
CSS엔진의 교체가 이뤄져 일부 동작이 변경됐고 성능이 개선됐으며 `watch`/`unwatch` 메서드가 비권장 됐고 `PerformanceObserver`의 효율성이 개선됐습니다. 그리고 Fetch의 abort를 지원하며
WebRTC `RTCDataChannel`의 메시지 파일 크기를 지정할 수 있도록 변경됐습니다.

- [Introducing the New Firefox: Firefox Quantum - The Mozilla Blog](https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/ "Introducing the New Firefox: Firefox Quantum - The Mozilla Blog")
- [Firefox Quantum 57 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/57 "Firefox Quantum 57 for developers - Mozilla | MDN")
- [Firefox 57 사이트 호환성 정보 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/57/ "Firefox 57 사이트 호환성 정보 | Firefox 사이트 호환성 정보")
- [Using WebRTC data channels - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels#Understanding_message_size_limits "Using WebRTC data channels - Web APIs | MDN")

----

## Release 2.6.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v2.6.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v2.6.0 "Release 2.6.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">ReleaseNote</span></p>

lighthouse 2.6.0이 릴리즈됐습니다.
`redirects` 검사 도구 추가 됐으며 각 스크립트의 동작 시간을 측정하는 `bootup-time`, 페이지의 실행 시간을 측정하는 `mainthread-work-breakdown` 등의 Audit이 추가됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Refactoring React Components with Jest’s Snapshot – Michael Romani – Medium
[medium.com/@mr4227/refactoring-react-components-with-jests-snapshot-7ed1b9d332cc](https://medium.com/@mr4227/refactoring-react-components-with-jests-snapshot-7ed1b9d332cc "Refactoring React Components with Jest’s Snapshot – Michael Romani – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jest의 snapshot 테스트를 사용한 React 컴포넌트의 리팩터링에 대해 소개돼 있습니다.
스탭샷을 찍고 테스트를 진행하며 거대한 컴포넌트를 세분화하는 과정을 이야기 합니다.

----

## How Redux Works: A Counter-Example
[daveceddia.com/how-does-redux-work/](https://daveceddia.com/how-does-redux-work/ "How Redux Works: A Counter-Example")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

Redux로 카운터 앱을 만들어 가며 Redux의 사용법이나 구조에 대해 배울 수 있는 튜토리얼 입니다.

----

## The Cost Of JavaScript – Dev Channel – Medium
[medium.com/dev-channel/the-cost-of-javascript-84009f51e99e](https://medium.com/dev-channel/the-cost-of-javascript-84009f51e99e "The Cost Of JavaScript – Dev Channel – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScript의 실행까지의 비용에 대해 소개돼 있는 글입니다.
다운로드, 파싱, 실행 과정과 같은 사이즈의 JavaScript, 이미지 파일이라 하더라도 실행 또는 렌더링까지의 비용이 다를 수 있는 점에 대해 소개돼 있습니다. 또, PRPL 패턴, Performance Budget에 관해서 이야기합니다.

----

## JavaScript. The Core: 2nd Edition – ds.laboratory
[dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition/](http://dmitrysoshnikov.com/ecmascript/javascript-the-core-2nd-edition/ "JavaScript. The Core: 2nd Edition – ds.laboratory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript / JavaScript의 용어 정의와 각 개념에 대해 소개돼 있습니다.
ECMAScript의 사양에 가까운 코어한 내용이 작성돼 있습니다.

----

## Clean Code vs. Dirty Code: React Best Practices - American Express Engineering Blog
[americanexpress.io/clean-code-dirty-code/](http://americanexpress.io/clean-code-dirty-code/ "Clean Code vs. Dirty Code: React Best Practices - American Express Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

React를 소재로 클린한 코드에 관해 이야기합니다.
네이밍과 컴포넌트 분할, 기본 값의 취급 방법 등 좋지 않은 예와 그것을 개선한 예를 이용해 알기 쉽게 작성 돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## React Redux를 사용한 SPA 신규 서비스를 운용하며 얻은 식견과 구현 사례 - 랜서즈(Lancers) 엔지니어 블로그(일본어)

[engineer.blog.lancers.jp/2017/11/react-redux-spa-manage-tips/](https://engineer.blog.lancers.jp/2017/11/react-redux-spa-manage-tips/ "React Redux を用いた SPA 新規サービスを運用して得た知見と実装例 - ランサーズ（Lancers）エンジニアブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">slide</span> <span class="jser-tag">JavaScript</span></p>

React + Redux + Saga를 사용한 프로젝트를 진행하며 알게 된 여러가지 사실에 대해 소개하는 슬라이드 입니다.
디렉터리 구성이나 기본적인 처리 흐름, HOC를 사용한 컴포넌트 확장, 다이얼로그와 스토리지 등 유즈케이스 별 구현 방법에 관해 이야기합니다.
또, 테스트, Sentry를 사용한 에러 해석, SEO, API 관리에 대해서도 작성돼 있습니다.

----

## JS Kongress 2017 - YouTube
[www.youtube.com/playlist?list&#x3D;PL8ajgHZ7PoCt3l5RXoyqVu\_r7gYJU0dMx](http://www.youtube.com/playlist?list=PL8ajgHZ7PoCt3l5RXoyqVu_r7gYJU0dMx "JS Kongress 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">video</span></p>

JS Kongress 2017의 발표 영상이 공개 됐습니다.

- [JS Kongress 2017 💻 - The Future of JavaScript, Nov 13-14 2017, Munich](https://2017.js-kongress.de/ "JS Kongress 2017 💻 - The Future of JavaScript, Nov 13-14 2017, Munich")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## What Web Can Do Today
[whatwebcando.today/](https://whatwebcando.today/ "What Web Can Do Today")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">browser</span></p>

사용하고 있는 브라우저가 다양한 Web Platform API 중 무엇무엇을 지원하고 있는지 알려주는 사이트입니다.

----

## \`performance.mark\` with metadata is useful for Real user monitoring
[dev.to/ben/we-welcome-a-wonderful-influx-of-new-members-from-japan-1k0](https://dev.to/ben/we-welcome-a-wonderful-influx-of-new-members-from-japan-1k0 "\`performance.mark\` with metadata is useful for Real user monitoring")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

`performance.mark` 에 메타데이터로써 FPS를 전달하여 측정하고, 병목을 일으키는 동작을 로깅하여 해석 및 시각화하는 방법에 대해 이야기합니다.

- [azu/performance-mark-metadata: \`performance.mark\` with custom meta data.](https://github.com/azu/performance-mark-metadata "azu/performance-mark-metadata: \&#x60;performance.mark\&#x60; with custom meta data.")
- [performance.mark에 메타데이터를 결합시킬 수 있는 라이브러리를 만들었다 | Web Scratch](http://efcl.info/2017/11/15/performance.mark-metadata/ "performance.mark에 메타데이터를 결합시킬 수 있는 라이브러리를 만들었다 | Web Scratch")(일본어)

----

## stereobooster/react-snap: A zero-configuration static pre-renderer for Single Page Applications
[github.com/stereobooster/react-snap](https://github.com/stereobooster/react-snap "stereobooster/react-snap: A zero-configuration static pre-renderer for Single Page Applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

React 애플리케이션을 정적 HTML로 pre-render할 수 있는 라이브러리입니다.
특별한 설정 없이 create-react-app 구조에 동작하는 것을 목표로 개발됐으며 SSR에서 다루기가 힘든 3rd 파티 스크립트나 WebGL 등을 옵션으로 대처할 수 있도록 디자인돼 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## moment/luxon: A library for working with dates and times in JS
[github.com/moment/luxon](https://github.com/moment/luxon "moment/luxon: A library for working with dates and times in JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

날짜나 시간, 인터벌을 다루는 라이브러리입니다. 날짜 조작 뿐 아니라 파싱 또는 포맷을 지원합니다. Immutable 하며 TimeZone이나 Intl를 사용한 국제화에 대응하고 있습니다. Moment와의 차이를 정리한 문서도 공개돼 있으니 함께 살펴보시길 바랍니다.

----

## jaredpalmer/react-fns: Browser API's turned into declarative React components and HoC's
[github.com/jaredpalmer/react-fns](https://github.com/jaredpalmer/react-fns "jaredpalmer/react-fns: Browser API's turned into declarative React components and HoC's")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React의 High Order Component의 컬렉션 라이브러리입니다.
디바이스의 회전과 동작, 온라인/오프라인, Geo, 미디어 쿼리, 스크롤, 로케일을 다루는 컴포넌트 등이 준비돼 있습니다.

----

## goto-bus-stop/tinyify: a browserify plugin that runs various optimizations, so you don't have to install them all manually. makes your bundles tiny!
[github.com/goto-bus-stop/tinyify](https://github.com/goto-bus-stop/tinyify "goto-bus-stop/tinyify: a browserify plugin that runs various optimizations, so you don't have to install them all manually. makes your bundles tiny!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">plugin</span> <span class="jser-tag">Tools</span></p>

Browserify 환경에서 플랫 bundle, unassert, production 빌드, minify 등 다양한 최적화 작업을 한 데 수행하는 플러그인입니다.

----

## jaredpalmer/razzle: ✨ Create server-rendered universal JavaScript applications with no configuration
[github.com/jaredpalmer/razzle](https://github.com/jaredpalmer/razzle "jaredpalmer/razzle: ✨ Create server-rendered universal JavaScript applications with no configuration")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">isomorphic</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Universal한 JavaScript 애플리케이션을 설정 없이 개발을 시작할 수 있는 개발 환경 도구입니다.
`create-react-app`와 비슷한 도구지만 React 이 외의 환경에서도 사용할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## Pure React
[daveceddia.com/pure-react/](https://daveceddia.com/pure-react/ "Pure React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React를 스텝 바이 스텝으로 배울 수 있는 예제 코드를 중심으로 작성됀 도서입니다.

----

## Manning | Vue.js in Action
[www.manning.com/books/vue-js-in-action](https://www.manning.com/books/vue-js-in-action "Manning | Vue.js in Action")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">book</span></p>

2018년 5월 30일 출간 예정인 Vue를 주제로 한 도서입니다.

----

## 초단기! Web 페이지 속도 개선 가이드── 사용성은 「속도」에서 시작된다(WEB+DB PRESS plus 시리즈)｜gihyo.jp … 기술평론사(일본어)
[gihyo.jp/magazine/wdpress/plus/978-4-7741-9400-4](http://gihyo.jp/magazine/wdpress/plus/978-4-7741-9400-4 "超速！ Webページ速度改善ガイド ── 使いやすさは「速さ」から始まる（WEB+DB PRESS plusシリーズ）｜gihyo.jp … 技術評論社")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

2017년 11월 23일 출간 예정인 웹페이지의 성능 개선을 주제로 한 도서입니다. 네트워크, 렌더링, 스크립트 항목별 측정 방법과 개선 방법에 대해 작성돼 있습니다.

----

## Manning | React Native in Action
[www.manning.com/books/react-native-in-action](https://www.manning.com/books/react-native-in-action "Manning | React Native in Action")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2018년 4월 30일에 출간 예정인 React Native를 주제로한 도서입니다.

----
