---
title: "2015-09-02 JS 소식: MSEdge와 asm.js, 단방향 데이터 흐름 아키텍쳐, CSS 스펙문서 읽는법"
author: azu
translator: ChoEun
layout: post
date : 2015-09-02T21:38
category: JSer
tags:
    - Flux
    - MVC
    - MSEdge
    - CSS
    - Spec

---

JSer.info #243 - Windows 10 [Build 10532](https://blogs.windows.com/bloggingwindows/2015/08/27/windows-10-insider-preview-build-10532-for-pc/ "Build 10532") 업데이트를 공개하면서 MSEdge도 업데이트하였습니다.

Pointer Lock, Canvas [blend modes](http://blogs.adobe.com/webplatform/2014/02/24/using-blend-modes-in-html-canvas/ "blend modes") 추가, ES6 Classes, asm.js를 기본으로 사용할 수 있으며, Destructuring이나 ES.next [Async Functions](https://github.com/tc39/ecmascript-asyncawait "Async Functions")를 실험 플래그를 붙여 지원합니다.

- [Microsoft Edge 10532](http://dev.modern.ie/platform/changelog/10532-pc/ "Microsoft Edge 10532")
- [Windows 10 Insider Preview Build 10532 for PC | Blogging Windows](https://blogs.windows.com/bloggingwindows/2015/08/27/windows-10-insider-preview-build-10532-for-pc/ "Windows 10 Insider Preview Build 10532 for PC | Blogging Windows")

또한, 오픈 미디어 타입 포맷을 개발하는 [Alliance for Open Media](http://aomedia.org/ "Alliance for Open Media")에 Microsoft가 참여하고 있는 것과 관련 있을 거 같지만, MSEdge에서 WebM/Opus/VP9를 구현할 예정이라고 합니다.

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Oh, hai there open media formats! <a href="http://t.co/mdUgKyFvV0">http://t.co/mdUgKyFvV0</a> <a href="http://t.co/PT7srf6J4J">http://t.co/PT7srf6J4J</a> <a href="http://t.co/0tjhZipHaV">http://t.co/0tjhZipHaV</a></p>&mdash; Jacob Rossi (@jacobrossi) <a href="https://twitter.com/jacobrossi/status/638785221593288704">September 1, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

[André Staltz - Unidirectional User Interface Architectures](http://staltz.com/unidirectional-user-interface-architectures.html "André Staltz - Unidirectional User Interface Architectures") 기사에서, Flux, Redux, Famous, Elm, Cycle.js의 아키텍쳐에 대해 간결하게 설명하고 있습니다.

각 구성요소에서 어떻게 단방향 데이터 흐름을 돌리고 있는가에 대해 그림과 함께 설명하고 있어 추천하는 글입니다.

Backbone.js 등에 대해 작성한 아래 기사도 함께 보면 재미있습니다.

- [서버와 클라이언트 양쪽에서 동작하는 대규모 JavaScript개발을 하기 위해](https://gist.github.com/tily/1362110 "서버와 클라이언트 양쪽에서 동작하는 대규모 JavaScript 개발을 하기 위해")

----

[기본 이전의 기초지식 - Back to Basics CSS 2015-08-30](http://unformedbuilding.com/slide/back-to-basics-2015-08-30/#/ "기본 이전의 기초지식 - Back to Basics CSS 2015-08-30")([한국어문서](http://techhtml.github.io/TR/)) 슬라이드에서, CSS 스펙을 어떻게 읽어야 하는지 설명하고 있습니다.

스펙문서는 어디에 있는지, 스펙문서에 나오는 CSS 기본구문 읽는 법, 기호의 의미 등을 자세히 설명합니다.

CSS 스펙문서를 참조할 때 맞춰 읽으면 좋은 문서입니다.

----

## 공지

[JSer.info 로고 및 아이콘을 변경했습니다](http://jser.info/2015/08/26/update-logo/ "JSer.info 로고 및 아이콘을 변경했습니다 - JSer.info")

![jser.info](https://monosnap.com/file/h3VuimNtmUkbaIr4FO2GhRiooVGetE.png)

이미지는 [jser/media](https://github.com/jser/media "jser/media")에서 자유롭게 인용할 수 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## ESLint v1.3.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/08/eslint-v1.3.0-released](http://eslint.org/blog/2015/08/eslint-v1.3.0-released "ESLint v1.3.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.3.0 릴리즈
`SourceCode` 객체 API 추가, HTML 포매터 추가, 룰 수정 등

----

## V8 JavaScript Engine: V8 Release 4.6
[v8project.blogspot.com/2015/08/v8-release-46.html](http://v8project.blogspot.com/2015/08/v8-release-46.html "V8 JavaScript Engine: V8 Release 4.6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.6 릴리즈
ES6의 Spread operator, `new.target` 대응, TypedArray 개선 등

----

## Release v2.0.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v2.0.0](https://github.com/rackt/redux/releases/tag/v2.0.0 "Release v2.0.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Redux 2.0.0 릴리즈
Hot Reloading에서만 사용하던 `getReducer()` 제거, `compose()` 동작 수정 등

----

## mocha/HISTORY.md at master · mochajs/mocha
[github.com/mochajs/mocha/blob/master/HISTORY.md#230--2015-08-30](https://github.com/mochajs/mocha/blob/master/HISTORY.md#230--2015-08-30 "mocha/HISTORY.md at master · mochajs/mocha")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 2.3.0 릴리즈. 테스트 중 에러가 발생했을 때 자동으로 캐치하지 않고 넘길 수 있는 `--allowUncaught` 추가, 비동기 테스트만 허가하는 `--async-only`에서 Promise 동작 수정

- [Added option to allow unhandled exceptions to propagate in the browser by amsul · Pull Request #1659 · mochajs/mocha](https://github.com/mochajs/mocha/pull/1659 "Added option to allow unhandled exceptions to propagate in the browser by amsul · Pull Request #1659 · mochajs/mocha")

----

## Release version 10532 [PC] : Microsoft Edge Dev
[dev.modern.ie/platform/changelog/10532-pc/](http://dev.modern.ie/platform/changelog/10532-pc/ "Release version 10532 \[PC\] : Microsoft Edge Dev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

Microsoft Edge 10532 릴리즈
Pointer Lock, Canvas blending modes 지원, asm.js와 ES6 Classes를 기본지원
또한 Async Function, Destructuring이 플래그 지원 기능으로 추가

----

## jsdom/Changelog.md at 6.2.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/6.2.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/6.2.0/Changelog.md "jsdom/Changelog.md at 6.2.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 6.2.0 릴리즈
`Element.prototype.classList` 지원 및 버그 수정

----

## Release v1.0.0: The first stable release (2015-08-26) · power-assert-js/power-assert
[github.com/power-assert-js/power-assert/releases/tag/v1.0.0](https://github.com/power-assert-js/power-assert/releases/tag/v1.0.0 "Release v1.0.0: The first stable release (2015-08-26) · power-assert-js/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

assert를 실패했을 때 표시하는 정보량을 늘리는 power-assert 1.0.0 릴리즈

----
<h1 class="site-genre">아티클</h1>

----

## André Staltz - Unidirectional User Interface Architectures
[staltz.com/unidirectional-user-interface-architectures.html](http://staltz.com/unidirectional-user-interface-architectures.html "André Staltz - Unidirectional User Interface Architectures")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">설계</span></p>

Flux, Redux, Famous, Elm, Cycle.js의 아키텍쳐에 대해 간결하게 설명하고 있습니다.
구성요소, 데이터 흐름, 특징에 대해 간결하게 정리

----

## Using requestIdleCallback — Google Web Updates
[developers.google.com/web/updates/2015/08/27/using-requestidlecallback](https://developers.google.com/web/updates/2015/08/27/using-requestidlecallback "Using requestIdleCallback — Google Web Updates")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span></p>

requestIdleCallback에 대해 설명
Idle 같이 단기간 비동기 콜백을 호출하는 게 가능해, 두번째 인수로 일정 시간 내 반드시 호출하는 `timeout`을 지정할 수 있다.

----

## fizzbuzz
[ditam.github.io/posts/fizzbuzz.html](http://ditam.github.io/posts/fizzbuzz.html "fizzbuzz")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">알고리즘</span></p>

JavaScript에서 20종류의 FizzBuzz를 구현

----
<h1 class="site-genre">슬라이드 및 동영상</h1>

----

## 기본 이전의 기초지식 - Back to Basics CSS 2015-08-30
[unformedbuilding.com/slide/back-to-basics-2015-08-30/#/](http://unformedbuilding.com/slide/back-to-basics-2015-08-30/#/ "기본 이전의 기초지식 - Back to Basics CSS 2015-08-30") [한국어문서](http://techhtml.github.io/TR/)

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">spec</span> <span class="jser-tag">슬라이드</span></p>

CSS 스펙 읽는 법에 대한 슬라이드
스펙에 나오는 구문 읽는 법이나 단위에 대해 설명하고 있다.

----

## npm3 ❓ // Speaker Deck
[speakerdeck.com/watilde/npm3](https://speakerdeck.com/watilde/npm3 "npm3 ❓ // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">슬라이드</span></p>

npm3에 추가한 기능이나 변경점에 대한 슬라이드

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Thimble by Mozilla - An online code editor for learners &amp; educators.
[thimble.mozilla.org/](https://thimble.mozilla.org/ "Thimble by Mozilla - An online code editor for learners & educators.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Mozilla</span> <span class="jser-tag">webservice</span> <span class="jser-tag">editor</span></p>

온라인으로 웹사이트를 제작하는 서비스.
JSFiddle 같은 에디터와 프리뷰, 파일트리를 지원.
또한 임의의 파일을 업로드한 뒤 HTML로 표현 가능해 편리해보인다.

----

## mattdesl/promise-cookbook
[github.com/mattdesl/promise-cookbook](https://github.com/mattdesl/promise-cookbook "mattdesl/promise-cookbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">book</span></p>

Promise 기본 사용방법, 메소드에 대해 설명하고 있는 Cookbook

----

## JS.ORG | NEWS
[news.js.org/](http://news.js.org/ "JS.ORG | NEWS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

유저가 제보한 JavaScript 뉴스를 모아둔 사이트

----
<h1 class="site-genre">소프트웨어, 툴, 라이브러리</h1>

----

## Izzimach/react-pixi
[github.com/Izzimach/react-pixi](https://github.com/Izzimach/react-pixi "Izzimach/react-pixi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span></p>

React에서 Pixi.js의 Canvas를 조작할 수 있게하는 라이브러리

----

## mysticatea/npm-run-all
[github.com/mysticatea/npm-run-all](https://github.com/mysticatea/npm-run-all "mysticatea/npm-run-all")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm run-script에 정의한 스크립트의 병렬실행 및 순차실행 등을 보조하는 커맨드라인 도구
Node 모듈로도 사용 가능하다

- [npm-run-all과 concurrently 사용해보다 | アカベコマイリ](http://akabeko.me/blog/2015/08/npm-run-all-and-concurrently/ "npm-run-all 과 concurrently를 사용해보다 | アカベコマイリ")

----
<h1 class="site-genre">서적</h1>

----

## Amazon: Reactive Programming with Rxjs: Untangle Your Asynchronous JavaScript Code: Sergi Mansilla
[www.amazon.com/dp/1680501291?tag=amazon0abac-22](http://www.amazon.com/dp/1680501291?tag=amazon0abac-22 "Amazon: Reactive Programming with Rxjs: Untangle Your Asynchronous JavaScript Code: Sergi Mansilla")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span> <span class="jser-tag">book</span></p>

2016년 3월 25일 발매
RxJS에서 리액티브 프로그래밍에 대한 서적

----

## SurviveJS - Webpack and React
[survivejs.com/](http://survivejs.com/ "SurviveJS - Webpack and React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

Webpack과 React에 대한 서적

----
