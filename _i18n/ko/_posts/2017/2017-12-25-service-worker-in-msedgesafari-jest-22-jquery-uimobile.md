---
title: "2017-12-26 JS: Service Worker in MSEdge/Safari, Jest 22, jQuery UI와 Mobile 통합"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-12-26T09:55:06.473Z
category: JSer
tags:
- ServiceWorker
- jest
- jQuery

---

JSer.info #363 - MSEdge(Insider build)와 Safari(Technology Preview)의 Service Worker 구현 내용이 블로그를 통해 공개됐습니다.

- [Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/)
- [Release Notes for Safari Technology Preview 46 | WebKit](https://webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/)

이로써 모든 모던 브라우저에서 Service Worker를 지원하게 됐습니다.

<p class="ciu_embed" data-feature="serviceworkers" data-periods="future_1,current,past_1,past_2">
  <a href="http://caniuse.com/#feat=serviceworkers">Can I Use serviceworkers?</a> Data on support for the serviceworkers feature across the major browsers from caniuse.com.
</p>

MSEdge와 Safari 둘 다 아직 실험적 빌드 버전으로 공개한 것이므로 비정상적으로 동작하는 경우도 있는 것 같습니다.
그러한 경우를 발견했을 때는 각 Issue Tracker에 등록해주길 권장하고 있습니다.

- MSEdge: [Microsoft Edge issue tracker - Microsoft Edge Development](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/?page=1&q=Service%20Worker "Microsoft Edge issue tracker - Microsoft Edge Development")
- Safari: [Bug List](https://bugs.webkit.org/buglist.cgi?quicksearch=Service%20Worker "Bug List")

----

Jest 22이 릴리즈 됐습니다.

- [Jest 22: Refinements & Custom Runners · Jest](http://facebook.github.io/jest/blog/2017/12/18/jest-22.html "Jest 22: Refinements &amp; Custom Runners · Jest")


Node.js 4 지원이 종료됐고 Custom Runner의 코어인 [jest-worker](https://github.com/facebook/jest/tree/master/packages/jest-worker "jest-worker")가 공개됐습니다.
Jest는 테스트를 병렬 실행하는데 [node-worker-farm](https://github.com/rvagg/node-worker-farm "node-worker-farm")을 사용하고 있었으며 현재 해당 역할로 [jest-worker](https://github.com/facebook/jest/tree/master/packages/jest-worker "jest-worker")를 개발, 대체하고 있습니다. - [Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest](https://github.com/facebook/jest/pull/4497 "Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest")

- [Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest](https://github.com/facebook/jest/pull/4497 "Initial version of jest-worker by mjesun · Pull Request #4497 · facebook/jest")

그리고 Jest를 병렬 처리 기반으로 사용할 수 있는 Custom Runner가 Jest 22를 통해 정식으로 공개됐습니다.
의해 Jest 상에서 [jest-runner-mocha](https://github.com/rogeliog/jest-runner-mocha "jest-runner-mocha")나 [jest-runner-eslint](https://github.com/jest-community/jest-runner-eslint "jest-runner-eslint") 등의 Runner를 이용해 다른 테스트 프레임워크나 Lint 처리 등을 병렬로 실행할 수 있게 됐습니다.

자세한 내용은 아래 동영상을 참고해주세요.

<iframe width="560" height="315" src="https://www.youtube.com/embed/NtjyeojAOBs" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>

또 테스트 결과 포맷이 변경됐고 `--detectLeaks` 옵션이 실험적으로 추가됐으며 Babel 7 지원 등이 이뤄졌습니다.

----

[The Future of jQuery UI and jQuery Mobile | jQuery UI Blog](http://blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/ "The Future of jQuery UI and jQuery Mobile | jQuery UI Blog")에는 jQuery UI와 jQuery Mobile 프로젝트의 통합과 관련한 내용이 소개돼 있습니다.

[jquery-mobile](https://github.com/jquery/jquery-mobile "jquery-mobile")은 [jquery-ui](https://github.com/jquery/jquery-ui "jquery-ui")를 의존하고 있지만 지금까지 팀이나 저장소가 따로 분리돼 있었습니다.
이번에 [@scottgonzalez](https://github.com/scottgonzalez "scottgonzalez")가 Query UI 프로젝트 리더를 그만두게 돼 현재 jQuery Mobile 프로젝터 리더인 [@arschmitz](https://github.com/arschmitz "arschmitz")가 jQuery UI 프로젝트도 함께 담당하게 됐습니다.
jQuery Mobile는 UI에 의존하고 있기 때문에 별도의 프로젝트로 운영하여 발생하는 중복이나 낭비를 피하기 위해 2개의 프로젝트 팀을 하나로 통합해 진행할 방침에 대해 작성돼 있습니다.

또 이에 맞춰 협력자를 모집하기 위해 slack 팀 [jquery-dev](https://jqueryui-dev.slack.com/)을 만들어 의견을 모으고 있습니다(<http://bit.ly/2Btf6pu>을 통해 Slack 팀에 join할 수 있습니다).

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Notes for Safari Technology Preview 46 | WebKit
[webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/](https://webkit.org/blog/8042/release-notes-for-safari-technology-preview-46/ "Release Notes for Safari Technology Preview 46 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">ServiceWorker</span></p>

Safari Technology Preview Release 46이 릴리즈 됐습니다.
Service Worker가 기본적으로 활성화됐고 `--useBigInt` 플래그를 이용해 사용할 수 있는 BigInt가 구현됐습니다. 또, `img` 요소의 `decoding` 속성 등을 지원합니다.

----

## V8 JavaScript Engine: V8 release v6.4
[v8project.blogspot.com/2017/12/v8-release-64.html](https://v8project.blogspot.com/2017/12/v8-release-64.html "V8 JavaScript Engine: V8 release v6.4")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.4가 릴리즈됐습니다.
성능과 메모리 사용 효율성이 개선됐고 named capture 정규 표현 제안이 구현됐으며 `import.meta.url` 등을 지원합니다.

----

## Release Webpack-CLI V.2.0.0 · webpack/webpack-cli
[github.com/webpack/webpack-cli/releases/tag/v.2.0.0](https://github.com/webpack/webpack-cli/releases/tag/v.2.0.0 "Release Webpack-CLI V.2.0.0 · webpack/webpack-cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack-cli 2.0.0이 릴리즈됐습니다.
`add` 커맨드와 `serve` 커맨드가 추가됐습니다.

----

## Release v2.0.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v2.0.0](https://github.com/karma-runner/karma/releases/tag/v2.0.0 "Release v2.0.0 · karma-runner/karma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma v2.0.0이 릴리즈됐습니다.
Node.js 4 미만 지원이 종료됐으며 에러를 출력하는 방식이 개선됐습니다.

----

## ESLint v4.14.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/12/eslint-v4.14.0-released](https://eslint.org/blog/2017/12/eslint-v4.14.0-released "ESLint v4.14.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.14.0이 릴리즈됐습니다.
파서 용의 Scope 해석 hook 포인트가 추가됐습니다.

----

## Jest 22: Refinements & Custom Runners · Jest
[facebook.github.io/jest/blog/2017/12/18/jest-22.html](http://facebook.github.io/jest/blog/2017/12/18/jest-22.html "Jest 22: Refinements & Custom Runners · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 22가 릴리즈됐습니다.
Node.js 4에 대한 지원이 종료됐고 커스텀 Runner의 코어인 `jest-worker`가 공개됐습니다.
또, 결과 포맷팅이 변경됐고 `--detectLeaks` 옵션이 추가 됐습니다. 그리고 Babel 7을 지원하며 MIT 라이센스로 변경됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## 【연재글】JavaScript로 프로그래밍을 배우다 그 첫 편：기초와 문법(일본어)
[sbfl.net/blog/2017/12/14/javascript-programming-1/](https://sbfl.net/blog/2017/12/14/javascript-programming-1/ "【連載記事】JavaScriptでプログラミングを学ぶ　その1：基礎と文法")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

프로그래밍을 공부한 적 없는 사람을 위한 JavaScript 입문 연재 글입니다.

----

## Use a Render Prop! – componentDidBlog
[cdb.reacttraining.com/use-a-render-prop-50de598f11ce](https://cdb.reacttraining.com/use-a-render-prop-50de598f11ce "Use a Render Prop! – componentDidBlog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React의 자식 컴포넌트와 값이나 로직을 공유하는 패턴인 render props에 대한 글입니다.

- [Add doc about Render Props by mjackson · Pull Request #355 · reactjs/reactjs.org](https://github.com/reactjs/reactjs.org/pull/355 "Add doc about Render Props by mjackson · Pull Request #355 · reactjs/reactjs.org")

----

## React 🎄
[react.holiday/](https://react.holiday/ "React 🎄")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React 튜토리얼을 Advent Calendar로 정리한 곳입니다.

----

## Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/](https://blogs.windows.com/msedgedev/2017/12/19/service-workers-going-beyond-page/ "Service Workers: Going beyond the page - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

MSEdge에 Service Worker가 구현됐습니다.
Service Worker의 기본적인 사용 방법과 제한에 관해 작성돼 있습니다.

----

## The Future of jQuery UI and jQuery Mobile | jQuery UI Blog
[blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/](http://blog.jqueryui.com/2017/12/the-future-of-jquery-ui-and-jquery-mobile/ "The Future of jQuery UI and jQuery Mobile | jQuery UI Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">mobile</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

jQuery Mobile은 jQuery UI에 의존하고 있지만 지금까지는 다른 팀/저장소로 운영되고 있었습니다.
중복이나 비용 낭비가 있어 팀을 통합하고 정체중인 프로젝트를 개선하고자하는 지침이 공개됐습니다.
함께 Slack 채널을 개설하고 협력할 사람을 모집하고 있습니다.

----

## Preloading modules  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/12/modulepreload](https://developers.google.com/web/updates/2017/12/modulepreload "Preloading modules  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

`<link rel="modulepreload">`에 관해 소개한 글입니다.
`<link rel="preload">`와의 차이점, 모듈의 의존 관계를 수평적으로 모든 파일을 정의해야 하는지에 대해 작성돼 있습니다.

----

## Idiomatic Redux: Using Reselect Selectors for Encapsulation and Performance · Mark's Dev Blog
[blog.isquaredsoftware.com/2017/12/idiomatic-redux-using-reselect-selectors/](http://blog.isquaredsoftware.com/2017/12/idiomatic-redux-using-reselect-selectors/ "Idiomatic Redux: Using Reselect Selectors for Encapsulation and Performance · Mark's Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">React</span></p>

reselect를 사용한 성능 최적화에 관해 작성돼 있습니다.
reselect는 state에서 state를 만드는 라이브러리로 입력에 대해 메모이제이션이 이뤄져있습니다.
이를 사용해 Redux의 state에서 애플리케이션에 적절한 형태로 state를 변환하는 예제를 함께 소개하고 있습니다.

----

## ES6 Modules의 에러 처리를 결정적(deterministic)으로 한 이야기 - Google 문서(일본어)
[docs.google.com/document/d/1Wuc2LVLb2Ii-itnA4sKw\_KndJGvZ4mvdfw0POm5qcs4/edit#](https://docs.google.com/document/d/1Wuc2LVLb2Ii-itnA4sKw_KndJGvZ4mvdfw0POm5qcs4/edit# "ES6 Modules のエラー処理を決定的(deterministic)にした話 - Google ドキュメント")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">module</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">article</span> <span class="jser-tag">ECMAScript</span></p>

ES Modules(사양)의 에러가 네트워크에 의존한 것으로 돼 있어 매번 같지 않은 에러가 출력되는 문제가 있습니다.
에러의 결과가 항상 같도록 사양을 어떻게 수정하고 있는지에 대해 작성돼 있습니다.

----

## 브라우저의 구조: 데이터 구조와 알고리즘과 분위기로 이해한다, DOM과 Shadow DOM — hayato.io(일본어)
[hayato.io/2017/dom/](https://hayato.io/2017/dom/ "ブラウザのしくみ: データ構造とアルゴリズムと雰囲気で理解する DOM と Shadow DOM — hayato.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">WebComponents</span></p>

DOM과 Shadow DOM의 구조나 구현에 대해 설명돼 있습니다.
Shadow DOM의 등장으로 DOM은 트리의 트리(Super Tree)가 됐습니다.
그 경우에 있어 CSS 셀렉터의 맷칭이나 이벤트 패스 처리 등을 Chrome의 구현에 맞춰 소개합니다.

----

## Lint the Web Forward With Sonarwhal ◆ 24 ways
[24ways.org/2017/lint-the-web-forward-with-sonarwhal/](https://24ways.org/2017/lint-the-web-forward-with-sonarwhal/ "Lint the Web Forward With Sonarwhal ◆ 24 ways")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">web </span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Sonarwhal를 사용한 웹사이트 Lint에 대해 작성돼 있습니다.
Sonarwhal의 기본적인 사용 방법과 설정에 관해 소개합니다.

----

## Testing Angular 2 and Continuous Integration with Jest - Semaphore
[semaphoreci.com/community/tutorials/testing-angular-2-and-continuous-integration-with-jest](https://semaphoreci.com/community/tutorials/testing-angular-2-and-continuous-integration-with-jest "Testing Angular 2 and Continuous Integration with Jest - Semaphore")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Angular</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jest를 사용한 Angular 테스트 방법에 관해 소개돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 닛케이 전자 버전 사이트 고속화와 PWA 대응 / nikkei-high-performance-pwa // Speaker Deck(일본어)
[speakerdeck.com/sisidovski/nikkei-high-performance-pwa](https://speakerdeck.com/sisidovski/nikkei-high-performance-pwa "日経電子版 サイト高速化とPWA対応 / nikkei-high-performance-pwa // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">slide</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

웹 사이트의 성능 개선 사례에 대해 소개돼 있는 슬라이드입니다.
에셋 전송 최적화, Resource Hints로 preload, SpeedCurve를 사용한 모니터링이나 파일 사이즈 체크, Service Worker를 이용한 캐시나 디버깅 기법 등에 관해 소개합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## amsul/react-performance: Helpers to debug and record component render performance 🚀
[github.com/amsul/react-performance](https://github.com/amsul/react-performance "amsul/react-performance: Helpers to debug and record component render performance 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

React 16에서 동작하는 `react-addons-perf`와 비슷한 역할을 하는 구현체를 목표로 하는 라이브러리입니다.
React 컴포넌트의 프로파일을 취할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## Responsively Retrofitting: Retrofitting Web Sites with HTML5 and CSS3: Christopher Schmitt: 9781449364205: Amazon.com: Books
[www.amazon.com/Responsively-Retrofitting-Sites-HTML5-CSS3/dp/1449364209](https://www.amazon.com/Responsively-Retrofitting-Sites-HTML5-CSS3/dp/1449364209 "Responsively Retrofitting: Retrofitting Web Sites with HTML5 and CSS3: Christopher Schmitt: 9781449364205: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">book</span></p>

2018년 8월 25일 출간 예정인 레거시한 웹 사이트를 모바일 용으로 리뉴얼하는 방법을 주제로한 서적입니다.

----
