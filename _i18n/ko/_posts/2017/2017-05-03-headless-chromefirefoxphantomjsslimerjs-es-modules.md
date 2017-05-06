---
title: "2017-05-03 JS: Headless Chrome/Firefox와 PhantomJS/SlimerJS, ES modules"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-05-03T02:03:59.837Z
category: JSer
tags:
- Firefox
- Chrome
- Headless
- PhantomJS
- SlimerJS
- modules
- ECMAScript

---

JSer.info #329 - Chrome 59 베타(β)가 릴리즈됐습니다.

- [Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload](https://blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html "Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload")

Service Worker의 [navigation preloads](https://developers.google.com/web/updates/2017/02/navigation-preload)와 `MediaError.message`를 지원합니다. 또, Image Capture API를 실험적으로 지원하는 등 다양한 변경 사항이 있습니다.

이어, [Headless Chromium](https://chromium.googlesource.com/chromium/src/+/master/headless/ "Headless Chromium")이 추가돼 있습니다.

간단히 소개하자면 PhantomJS 처럼 Xvfb등이 불필요한 Chorme을 실행시킬 수 있는 모드입니다. 자세한 건 아래 문서에 설명돼 있습니다.

- [Getting Started with Headless Chrome  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/04/headless-chrome "Getting Started with Headless Chrome  |  Web  |  Google Developers")

이 Headless Chrome의 릴리즈 소식에 이어 PhantomJS의 코어테이너(유일한 액티브 테이너)가 개발 종료를 선언했습니다.

- [[Announcement] Stepping down as maintainer - Google 그룹스](https://groups.google.com/forum/#!topic/phantomjs/9aI5d-LDuNE "[Announcement] Stepping down as maintainer - Google 그룹스")
- [[Release] PhantomJS 2.5.0 Beta - Google 그룹스](https://groups.google.com/forum/#!topic/phantomjs/AefOuwkgBh0 "[Release] PhantomJS 2.5.0 Beta - Google 그룹스")
  - 얼마전 공개된 알파(α) 버전(QtWebKit의 업데이트가 포함돼 있다)

PhantomJS는 QtWebKit을 사용했으며 QtWebKit은 한번 프로젝트가 멈췄다 최근 다시 부활하고 있습니다.
QtWebKit의 Alternative로써 Chromium 기반의 [QtWebEngine](https://wiki.qt.io/QtWebEngine "QtWebEngine")을 제공하고 있습니다.

- [New Features in Qt 5.6 - Qt Wiki](https://wiki.qt.io/New_Features_in_Qt_5.6 "New Features in Qt 5.6 - Qt Wiki")
- [QtWebKit Developer Journal: QtWebKit: I'm back!](http://qtwebkit.blogspot.jp/2016/08/qtwebkit-im-back.html "QtWebKit Developer Journal: QtWebKit: I&#39;m back!")

또 다른 방향으로 PhantomJS를 Headless Chrome 기반으로 변경하는 것에 대한 Issue가 있었습니다.

- [Support headless Chromium · Issue #14954 · ariya/phantomjs](https://github.com/ariya/phantomjs/issues/14954 "Support headless Chromium · Issue #14954 · ariya/phantomjs")

현재 어느쪽을 이용하더라도 PhantomJS에는 대규모 수정이 필요하고 지원 비용이 높기 때문에 메인테이너를 종료한다는 입장입니다.

PhantomJS와 Headless Chrome의 차이에 관해는 아래 기사에 간단히 소개돼 있습니다.
렌더링 엔진 이외에도 [PhantomJS의 API](http://phantomjs.org/api/ "API | PhantomJS")와 Headless Chrome을 조작할 수 있는 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/ "Chrome DevTools Protocol")의 차이가 있습니다.

> Headless Chrome is similar to tools like PhantomJS. Both can be used for automated testing in a headless environment. The main difference between the two is that Phantom uses an older version of WebKit as its rendering engine while Headless Chrome uses the latest version of Blink.
> -- <https://developers.google.com/web/updates/2017/04/headless-chrome>

----

[Headless SlimerJS with Firefox – Coding](https://adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/ "Headless SlimerJS with Firefox – Coding")에는 Firefox Nightly에서 Headless를 지원하기 위한 개발 관련 내용이 작성돼 있습니다.

또, Firefox 기반의 PhantomJS라고 볼 수 있는 [SlimerJS](http://slimerjs.org/ "SlimerJS")를 이용해 Headless Firefox를 지원하는 방향에 관해서도 작성돼 있습니다
([SlimerJS](http://slimerjs.org/ "SlimerJS")는 [PhantomJS의 API](http://phantomjs.org/api/ "API | PhantomJS")와 비슷한 API를 갖고 있습니다).

- [Turn SlimerJS into an headless browser · Issue #80 · laurentj/slimerjs](https://github.com/laurentj/slimerjs/issues/80#issuecomment-280813674 "Turn SlimerJS into an headless browser · Issue #80 · laurentj/slimerjs")

**표**: Headless Browser 정리

<script src="https://gist.github.com/azu/c4206d94f18f35f6fe2fe303f988e7d5.js"></script>

----

[ECMAScript modules in browsers - JakeArchibald.com](https://jakearchibald.com/2017/es-modules-in-browsers/ "ECMAScript modules in browsers - JakeArchibald.com")에는 브라우저의 ES modules 지원 현황과 동작 방식에 관해 작성돼 있습니다.

Node.js에서 다루는 모듈과 다른점이나 `<script type="module">`의 기본적인 동작 등에 관해 소개돼 있습니다.

아래 글도 함께 살펴보면 좋을 것 같습니다.

- [Native ECMAScript modules: the new features and differences from Webpack modules](https://blog.hospodarets.com/native-ecmascript-modules-new-features "Native ECMAScript modules: the new features and differences from Webpack modules")

----

<h1 class="site-genre">헤드라인</h1>

----

## Headless SlimerJS with Firefox – Coding
[adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/](https://adriftwith.me/coding/2017/04/21/headless-slimerjs-with-firefox/ "Headless SlimerJS with Firefox – Coding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">E2E</span> <span class="jser-tag">webdriver</span></p>

Firefox Nightly에서 headleass 지원이 이뤄졌으며 SlimerJS를 이용해 헤드리스 환경에서 테스트를 수행할 수 있습니다.


----

## TestCafe v0.15.0 Released | TestCafe
[devexpress.github.io/testcafe/blog/testcafe-v0-15-0-released.html](http://devexpress.github.io/testcafe/blog/testcafe-v0-15-0-released.html "TestCafe v0.15.0 Released | TestCafe")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

TestCafe 0.15.0이 릴리즈됐습니다.
`Selector()#withText`의 사양을 변경했고 React와 Vue 용 확장 Selector를 지원합니다. 또, 셋업돼 있는 Docker image도 제공합니다.
`--proxy`와 `--debug-mode`가 추가됐고 `Role`에 `preserveUrl` 옵션을 추가하는 등 다양한 변경 사항이 있습니다.


----

## Angular: Angular 4.1.0 Now Available
[angularjs.blogspot.com/2017/04/angular-410-now-available.html](http://angularjs.blogspot.com/2017/04/angular-410-now-available.html "Angular: Angular 4.1.0 Now Available")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 4.1.0이 릴리즈됐습니다.
StrictNullChecks를 활성화한 TypeScript 2.2/2.3을 지원합니다.


----

## Release v2.3.0 JoJo's Bizarre Adventure · vuejs/vue
[github.com/vuejs/vue/releases/tag/v2.3.0](https://github.com/vuejs/vue/releases/tag/v2.3.0 "Release v2.3.0 JoJo's Bizarre Adventure · vuejs/vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.3.0이 릴리즈됐습니다.
서버 사이드 렌더링과 컴포넌트 비동기 로딩 관련 사항을 개선했으며 passive event listener 지원하는 등 다양한 변경 사항이 있습니다.


----

## Release v0.45.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.45.0](https://github.com/facebook/flow/releases/tag/v0.45.0 "Release v0.45.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow 0.45.0이 릴리즈됐습니다.
Unicode와 Dynamic Import 지원하며 `export type * from ...`를 대응합니다.


----

## Announcing TypeScript 2.3 | TypeScript
[blogs.msdn.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/](https://blogs.msdn.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/ "Announcing TypeScript 2.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.3이 릴리즈됐습니다.
`--checkJs`로 `// @ts-check`라고 작성된 JavaScript의 JSDoc을 type check 할 수 있도록 변경 됐습니다.
Default type arguments 지원하며 `--downlevelIteration` 추가가 추가 됐습니다. 또, `tsc  --init`로 `tsconfig.json` 생성 시 명시적으로 코드가 생성되도록 정리됐습니다.

- [JSDoc support in JavaScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript "JSDoc support in JavaScript · Microsoft/TypeScript Wiki")

----

## Ember.js - Ember 2.13 and 2.14 Beta Released
[emberjs.com/blog/2017/04/29/ember-2-13-released.html](https://emberjs.com/blog/2017/04/29/ember-2-13-released.html "Ember.js - Ember 2.13 and 2.14 Beta Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 2.14가 릴리즈됐습니다.
Ember CLI에서 yarn을 지원하며 Babel이나 Autoprefixer에서 이용할 수 있도록 `targets`를 지정하는 `config/targets.js`가 생성되도록 변경 됐습니다.

- [Ember CLI Targets 🎯](http://rwjblue.com/2017/04/21/ember-cli-targets/ "Ember CLI Targets 🎯")

----

## Netflix/unleash: Professionally publish your JavaScript modules in one keystroke
[github.com/Netflix/unleash](https://github.com/Netflix/unleash "Netflix/unleash: Professionally publish your JavaScript modules in one keystroke")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span></p>

unleash는 Netflix에서 개발하고 공개한 npm publish 버전 관리 도구 입니다.
semver 기반으로 버전을 관리하며 테스트를 함께 실행해 배포 안전 여부를 검사할 수 있습니다. 또, CHANGELOG를 자동 생성하며 publish 시의 preview도 볼 수 있습니다. 그리고 gh-pages에 문서를 배포하는 기능도 지원하는 등 npm publish 관련 처리를 정리 및 지원하는 도구입니다.


----

## Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload
[blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html](https://blog.chromium.org/2017/05/chrome-59-beta-headless-chromium-native.html "Chromium Blog: Chrome 59 Beta: Headless Chromium, native notifications on macOS, and service worker navigation preload")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 59 Beta가 릴리즈됐습니다.
Headless Chrome과 SW의 navigation preloads, `MediaError.message`를 지원합니다. 또, Image Capture API를 실험적으로 지원하는 등 다양한 변경 사항이 있습니다.

- [mediacapture-image/implementation-status.md at gh-pages · w3c/mediacapture-image](https://github.com/w3c/mediacapture-image/blob/gh-pages/implementation-status.md "mediacapture-image/implementation-status.md at gh-pages · w3c/mediacapture-image")

----
<h1 class="site-genre">아티클</h1>

----

## Introducing a faster BBC News front page | Wildly Inaccurate
[wildlyinaccurate.com/introducing-a-faster-bbc-news-front-page](https://wildlyinaccurate.com/introducing-a-faster-bbc-news-front-page "Introducing a faster BBC News front page | Wildly Inaccurate")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

BBC News의 성능 개선에 관해 작성돼 있습니다. SpeedCurve를 사용해 성능을 모니터링하고 이미지를 지연 로드 하며 React를 서버 사이드 렌더링으로만 이용하고 있다고 합니다. 또 현재 개선 1단계로 React를 브라우저에서 동작시킬 때 모바일에서 특히 무거운 문제를 어떻게 해결할 지 고민중 이라고 합니다.


----

## Internationalize your keyboard controls ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/03/internationalize-your-keyboard-controls/](https://hacks.mozilla.org/2017/03/internationalize-your-keyboard-controls/ "Internationalize your keyboard controls ★ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">키보드</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

키보드 이벤트에 관해 소개돼 있습니다.
`keyCode`/`charCode`/`which`를 대신하는 `key`와 `code` 프로퍼티에 관해 이야기합니다.
또, 그 외 KeyboardEvent 관련 팁도 소개돼 있습니다.

- [KeyboardEvent.key mapping of each browser - Google 스프레드시트](https://docs.google.com/spreadsheets/d/1YB4M5Y5BWSn-7FX7pXFNbLtDDGzQ0noUTIo-YSqyRzc/edit#gid&#x3D;0 "KeyboardEvent.key mapping of each browser - Google 스프레드시트")
- [cvan/keyboardevent-key-polyfill: polyfill for \`KeyboardEvent.prototype.key\`](https://github.com/cvan/keyboardevent-key-polyfill "cvan/keyboardevent-key-polyfill: polyfill for \&#x60;KeyboardEvent.prototype.key\&#x60;")
- [UI Events](https://w3c.github.io/uievents/#code-examples "UI Events")

----

## Everything you need to know about BabelJS
[kleopetrov.me/2016/03/18/everything-about-babel/](http://kleopetrov.me/2016/03/18/everything-about-babel/ "Everything you need to know about BabelJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babel의 설정이나 CLI의 개요가 소개돼 있습니다.


----

## Functional pattern: flatMap
[2ality.com/2017/04/flatmap.html](http://2ality.com/2017/04/flatmap.html "Functional pattern: flatMap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

`flatMap`이라 불리는 것은 무엇을 뜻하는 것인지 소개합니다.
또 이와 관련된 ECMAScript의 Stage 1의 Proposal도 작성돼 있습니다.

- [bterlson/proposal-flatMap: Proposal for flatten and flatMap](https://github.com/bterlson/proposal-flatMap "bterlson/proposal-flatMap: Proposal for flatten and flatMap")

----

## Getting Started with Headless Chrome  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/04/headless-chrome](https://developers.google.com/web/updates/2017/04/headless-chrome "Getting Started with Headless Chrome  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Headless Chrome를 사용하는 방법에 관해 소개돼 있습니다.
커멘드라인으로 DOM을 덤프하는 방법과 PDF를 만드는 방법, 스크린샷을 찍는 방법이나 remote debugging 방법 등이 작성돼 있습니다.


----

## ECMAScript modules in browsers - JakeArchibald.com
[jakearchibald.com/2017/es-modules-in-browsers/](https://jakearchibald.com/2017/es-modules-in-browsers/ "ECMAScript modules in browsers - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span></p>

ES modules의 브라우저 지원 현황 및 Node.js의 모듈 시스템과의 차이점에 관해 작성돼 있습니다
또, 모듈을 미지원하는 환경에서 fallback으로써 `nomodule`을 선언하는 방법, 기본적으로 `defer`인 점과 실행 순서, CORS와 MIME type 등을 소개합니다.


----

## Node.js 8.0.0 has been delayed and will ship on or around May 30th
[medium.com/the-node-js-collection/node-js-8-0-0-has-been-delayed-and-will-ship-on-or-around-may-30th-cd38ba96980d](https://medium.com/the-node-js-collection/node-js-8-0-0-has-been-delayed-and-will-ship-on-or-around-may-30th-cd38ba96980d "Node.js 8.0.0 has been delayed and will ship on or around May 30th")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodev</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

Node.js 8.0.0의 릴리즈 날이 3월 30일로 변경된 이유에 관해 작성돼 있습니다. 
V8의 TurboFan + Ignition pipeline가 기본적으로 활성화되는 릴리즈를 기다렸다 진행할 예정이라고 합니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## bevacqua/prop-tc39: Scraping microservice for TC39 proposals 😸
[github.com/bevacqua/prop-tc39](https://github.com/bevacqua/prop-tc39 "bevacqua/prop-tc39: Scraping microservice for TC39 proposals 😸")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">API</span></p>

ECMAScript의 Proposals의 목록과 이를 JSON으로 취득 가능한 Web API와 패키지 API에 관해 소개돼 있습니다.


----

## Performance best practices for Firefox front-end engineers - Mozilla | MDN
[developer.mozilla.org/en-US/docs/Mozilla/Firefox/Performance\_best\_practices\_for\_Firefox\_fe\_engineers](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Performance_best_practices_for_Firefox_fe_engineers "Performance best practices for Firefox front-end engineers - Mozilla | MDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span></p>

Firefox의 프론트엔드에 맞춰 작성된 성능 가이드라인입니다.
requestIdleCallback, reflow, repaint, 성능 측정 등에 관해 작성돼 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Introduction · react-sketchapp
[airbnb.io/react-sketchapp/](http://airbnb.io/react-sketchapp/ "Introduction · react-sketchapp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Sketch</span> <span class="jser-tag">library</span></p>

React Component를 Sketch에 렌더링하는 renderer입니다.


----

## Create Next App
[open.segment.com/create-next-app](https://open.segment.com/create-next-app "Create Next App")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">React</span></p>

Next.js 버전의 create react app 입니다.


----

## ktsn/houl: Gulp compatible build tool for huge static sites
[github.com/ktsn/houl](https://github.com/ktsn/houl "ktsn/houl: Gulp compatible build tool for huge static sites")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">node.js</span> <span class="jser-tag">gulp</span> <span class="jser-tag">debug</span></p>

gulp plugin를 사용할 수 있는 빌드 / dev server 도구 입니다.

- [대규모 정적 사이드를 위한 빌드 도구 // Speaker Deck](https://speakerdeck.com/ktsn/da-gui-mo-jing-de-saitofalsetamefalsebirudoturu "대규모 정적 사이드를 위한 빌드 도구 // Speaker Deck")(일본어)

----
<h1 class="site-genre">도서</h1>

----

## 알다(알고 싶은) WebRTC 종이 + 전자 서적 셋트 - Route 312 - BOOTH（동인지 통신판매・다운로드）(일본어)
[booth.pm/ja/items/504677](https://booth.pm/ja/items/504677 "알다(알고 싶은) WebRTC 종이 + 전자 서적 셋트 - Route 312 - BOOTH（동인지 통신판매・다운로드）(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">book</span></p>

WebRTC의 입문 서적 입니다.


----

## Web 프론트엔드 하이 퍼포먼스 튜닝 | 쿠보타 미츠노리 | 책 | 통신판매 | Amazon(일본어)
[www.amazon.co.jp/Web%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9-%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E4%B9%85%E4%BF%9D%E7%94%B0-%E5%85%89%E5%89%87/dp/4774189677](https://www.amazon.co.jp/Web%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%82%A8%E3%83%B3%E3%83%89-%E3%83%8F%E3%82%A4%E3%83%91%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%B3%E3%82%B9-%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E4%B9%85%E4%BF%9D%E7%94%B0-%E5%85%89%E5%89%87/dp/4774189677 "Web 프론트엔드 하이 퍼포먼트 튜닝 | 쿠보타 미츠노리 | 책 | 통신판매 | Amazon(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

2017년 5월 26일에 출간 예정인 웹사이트의 프론트엔드 성능에 관해 설명하는 서적입니다.


----
