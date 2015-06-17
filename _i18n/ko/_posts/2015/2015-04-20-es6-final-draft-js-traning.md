---
title: "2015-04-20のJS: ECMAScript6 최종 draft, JavaScript 트레이닝"
author: azu
layout: post
date : 2015-04-20T22:12
category: JSer
translator: devcken
tags:
    - ECMAScript
    - JavaScript
    - tutorial
    
---

JSer.info #224 - 차기 ECMAScript인 ES6 [Rev 38 Final Draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_14_2015_rev_38_final_draft "Rev 38 Final Draft")가 릴리즈되었습니다.

<blockquote class="twitter-tweet" lang="en"><p>Final Draft of the ECMAScript 2015 Language Specification (ES6) is now available at <a href="http://t.co/pcHkz1muWu">http://t.co/pcHkz1muWu</a> Next step: Ecma GA approval vote</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/588811606236106755">April 16, 2015</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ECMA에 제출되어 2015년 6월 ECMA 미팅에서 승인될 경우, ECMA 표준으로 공개될 예정입니다.

[2014-06-09のJS](http://jser.info/post/88276341744/2014-06-09-js-bluebird/ "2014-06-09のJS")에서 ES6의 차기 릴리즈 일정 변경을 알려드린 바 있는데, 그대로 진행될 것으로 보입니다.
(그림은 2014-06-09 시점에 대한 것)

<p><a href="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" title="ES6 timeline" target="_blank"><img width="100%" src="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" alt="ES6 Release Schedule"/></a></p>

<p><a href="http://monosnap.com/image/VdNAJQPs9B0Jynw6bG3BoDxceqAEzl.png" title="ES6 timeline" target="_blank">＊이미지를 크게 보시려면 클릭하세요.</a></p>

ECMA 표준으로 승인된 후에 ECMAScript는 [ISO/IEC 16262](http://www.iso.org/iso/home/store/catalogue_ics/catalogue_detail_ics.htm?csnumber=55755 "ISO/IEC 16262")으로도 표준화되고 있어, ISO/IEC에도 제출될 예정입니다.

ISO/IEC에서는 ECMAScript 5를 [ISO/IEC 16262:2011](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=55755 "ISO/IEC 16262:2011") 표준화하는데 연호를 사용하고 있습니다.

이와 같은 대응 관계로 인한 혼동 때문에, ES6의 사양서에서는 ECMAScript 2015라는 표기로 변경되고 있습니다.

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/rwaldron">@rwaldron</a> <a href="https://twitter.com/SlexAxton">@SlexAxton</a> RC4 replaced a lot of &quot;Edition 6&quot; with &quot;ECMAScript 2015&quot;. Will help with ISO version aka ISO/IEC-16262 Edition 4</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/584093254045413376">April 3, 2015</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

- [Web Reflection: JavaScript and the living ECMAScript Standard](http://webreflection.blogspot.jp/2015/01/javascript-and-living-ecmascript.html "Web Reflection: JavaScript and the living ECMAScript Standard")

----

[mixi-inc/JavaScriptTraining](https://github.com/mixi-inc/JavaScriptTraining "mixi-inc/JavaScriptTraining")라는 Github 저장소에는 JavaScript의 입문 훈련용 자료가 공개되어 있습니다.

- [이틀이면 된다! JavaScript 트레이닝 - mixi Engineers&#39; Blog](http://alpha.mixi.co.jp/entry/2015/04/17/155003 "이틀이면 된다! JavaScript 트레이닝 - mixi Engineers&#39; Blog")

![screenshot](http://monosnap.com/image/7wFTczUbicOXK4BuMYYz03sa5s1sbl.png)

[JS Assessment](http://efcl.info/2012/0414/res3059/ "JS Assessment")과 소위 [Koan](http://el.jibun.atmarkit.co.jp/rails/2011/01/koan-3c38.html "Koan")과 같은 형식으로 되어 있어서, 테스트를 통과하기 위해 문제를 푸는 방식으로 되어 있습니다.

DOM 작성, DOM 이벤트, 비동기 처리, Promise와 Fetch API, bower를 활용한 패키지 관리 등을 다루고 있어서, DOM native API를 배울 기회가 적어진 현재 상황에서 이러한 트레이닝을 해보는 것도 즐거울 거 같습니다. 

----

<h1 class="site-genre">헤드라인</h1>

----

## April 14, 2015 Rev 38 Final Draft - Draft Specification for ES.next (Ecma-262 Edition 6)
[wiki.ecmascript.org/doku.php?id=harmony:specification\_drafts#april\_14\_2015\_rev\_38\_final\_draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts#april_14_2015_rev_38_final_draft)

ECMAScript 2015(ES6)의 최종 draft 릴리즈

<blockquote class="twitter-tweet" lang="en"><p>Final Draft of the ECMAScript 2015 Language Specification (ES6) is now available at <a href="http://t.co/pcHkz1muWu">http://t.co/pcHkz1muWu</a> Next step: Ecma GA approval vote</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/588811606236106755">April 16, 2015</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

## React v0.13.2 | React
[facebook.github.io/react/blog/2015/04/18/react-v0.13.2.html](http://facebook.github.io/react/blog/2015/04/18/react-v0.13.2.html "React v0.13.2 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v0.13.2 릴리즈
React 툴에 '--es6module' 옵션이 추가되는 등의 소식

- [Document new es6module flag in react-tools README by TimeBomb · Pull Request #3618 · facebook/react](https://github.com/facebook/react/pull/3618 "Document new es6module flag in react-tools README by TimeBomb · Pull Request #3618 · facebook/react")

----

## Release electron v0.24.0 · atom/electron
[github.com/atom/electron/releases/tag/v0.24.0](https://github.com/atom/electron/releases/tag/v0.24.0 "Release electron v0.24.0 · atom/electron")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">atom</span> <span class="jser-tag">ReleaseNote</span></p>

Atom Shell 0.24.0 릴리즈
Atom Shell은 Electon이 리네임된 것

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md#500](https://github.com/tmpvar/jsdom/blob/master/Changelog.md#500 "jsdom/Changelog.md at master · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 5.0.0 릴리즈
`document.cookie`와 관련된 수정이 주요 소식

----

## Release v0.8.0 · airportyh/testem
[github.com/airportyh/testem/releases/tag/v0.8.0](https://github.com/airportyh/testem/releases/tag/v0.8.0 "Release v0.8.0 · airportyh/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Testem 0.8.0 릴리즈
Sauce Labs처럼 리모트 연결 실행에 대한 동작을 개선

----

## Release v0.11.0: ES6 support (2015-04-18) · twada/power-assert
[github.com/twada/power-assert/releases/tag/v0.11.0](https://github.com/twada/power-assert/releases/tag/v0.11.0 "Release v0.11.0: ES6 support (2015-04-18) · twada/power-assert")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 0.11.0 릴리즈
ES6 구문 지원

- [ES6 support by twada · Pull Request #17 · twada/power-assert](https://github.com/twada/power-assert/pull/17 "ES6 support by twada · Pull Request #17 · twada/power-assert")
- [twada/babel-plugin-espower](https://github.com/twada/babel-plugin-espower "twada/babel-plugin-espower")

----

## Chromium Blog: Chrome 43 Beta: Web MIDI and upgrading legacy sites to HTTPS
[blog.chromium.org/2015/04/chrome-43-beta-web-midi-and-upgrading.html](http://blog.chromium.org/2015/04/chrome-43-beta-web-midi-and-upgrading.html "Chromium Blog: Chrome 43 Beta: Web MIDI and upgrading legacy sites to HTTPS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 43 Beta 릴리즈
'Web MIDI API를 default 설정', 'Permissions API 지원', 'DOM 속성 prototype chian으로 이동', 'Flash 없이도 클립보드 복사 가능', 'Fetch를 통해 response 스트리밍 가능' 등의 소식  

- [Permissions API for the Web](http://updates.html5rocks.com/2015/04/permissions-api-for-the-web "Permissions API for the Web")
- [DOM Attributes now on the prototype chain](http://updates.html5rocks.com/2015/04/DOM-attributes-now-on-the-prototype "DOM Attributes now on the prototype chain")
- [Cut and Copy Commands](http://updates.html5rocks.com/2015/04/cut-and-copy-commands "Cut and Copy Commands")
- [yutakahirano/fetch-with-streams](https://github.com/yutakahirano/fetch-with-streams/ "yutakahirano/fetch-with-streams")

----
<h1 class="site-genre">기사</h1>

----

## Getting started with Node.js and Mocha - Semaphore
[semaphoreci.com/community/tutorials/getting-started-with-node-js-and-mocha](https://semaphoreci.com/community/tutorials/getting-started-with-node-js-and-mocha "Getting started with Node.js and Mocha - Semaphore")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Mocha를 사용한 테스트에 관한 내용
Mocha의 기본적인 사용법이나 express를 활용한 웹 서버 테스트에 대해 간결하게 정리했다.

----

## Fullscreen API의 어두운 면 - Browser
[browser.hatenablog.com/entry/2015/04/18/121248](http://browser.hatenablog.com/entry/2015/04/18/121248 "Fullscreen API의 어두운 면 - Browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

브라우저 간의 풀 스크린 API 실행 차이에 대한 내용

----

## Permissions API for the Web
[updates.html5rocks.com/2015/04/permissions-api-for-the-web](http://updates.html5rocks.com/2015/04/permissions-api-for-the-web "Permissions API for the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

퍼미션을 확인하는 API
`navigator.permissions`에 관한 내용

----

## JavaScript로 풀 스크래치 게임 개발하기, 제 1회 준비편 - Qiita
[qiita.com/zukkun/items/4ea9542a6dde45c6a9fd](http://qiita.com/zukkun/items/4ea9542a6dde45c6a9fd "JavaScript로 풀 스크래치 게임 개발하기, 제 1회 준비편 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">game</span> <span class="jser-tag">JavaScript</span></p>

JavaScript로 게임(게임 엔진)을 만드는 과정을 연재
프레임 단위 갱신, canvas를 사용한 애니메이션, 이미지 입력 등에 대해 게임 프레임워크를 사용하지 않고 구현하는 방법에 대한 이야기

----
<h1 class="site-genre">슬라이드、 동영상 관련</h1>

----

## Controllable React Components // Speaker Deck
[speakerdeck.com/lettertwo/controllable-react-components](https://speakerdeck.com/lettertwo/controllable-react-components "Controllable React Components // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">슬라이드</span></p>

React로 ES6 Classes를 활용하여 컴포넌트를 만드는 슬라이드
컴포넌트 내에서 항상 state가 아닌 props를 사용하는 것을 선호하여, Form의 Controlled Component에서도 props를 사용하기 위한 고계 함수에 대한 내용

- [Forms | React](http://facebook.github.io/react/docs/forms.html#controlled-components "Forms | React")
- [matthewwithanm/react-controllables](https://github.com/matthewwithanm/react-controllables "matthewwithanm/react-controllables")

----
<h1 class="site-genre">사이트, 서비스, 도큐먼트</h1>

----

## ES Weekly Newsletter
[esweekly.com/](http://esweekly.com/ "ES Weekly Newsletter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">mail</span></p>

ECMAScript에 대한 주간 메일 매거진

----

## mixi-inc/JavaScriptTraining
[github.com/mixi-inc/JavaScriptTraining](https://github.com/mixi-inc/JavaScriptTraining "mixi-inc/JavaScriptTraining")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

mixi사의 JavaScript 연수 자료
테스트를 통해 살펴볼 수 있는 내용이다.
DOM 작성, DOM 이벤트, 비동기 처리, Promise와 Fetch API, bower를 사용한 패키지 관리 등에 대한 내용

- [이틀이면 된다! JavaScript 트레이닝 - mixi Engineers&#39; Blog](http://alpha.mixi.co.jp/entry/2015/04/17/155003 "이틀이면 된다! JavaScript 트레이닝 - mixi Engineers&#39; Blog")

----

## ARIA in HTML 일본어 번역
[momdo.github.io/html-aria/](http://momdo.github.io/html-aria/ "ARIA in HTML 일본어 번역")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">spec</span></p>

HTML과 WAI-ARIA의 속성에 대한 요구사항을 정리한 문서
요소의 default ARIA 시멘틱스든지 사용해도 좋은 ARIA의 역할에 대해서 간결하게 잘 정리되고 있다.

- [ARIA in HTML 일본어 번역을 공개하다. - 水底の血](http://momdo.hatenablog.jp/entry/20150418/1429345964 "ARIA in HTML 일본어 번역을 공개하다. - 水底の血")

----

## Hacklone/private-bower
[github.com/Hacklone/private-bower](https://github.com/Hacklone/private-bower "Hacklone/private-bower")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">오픈소스</span></p>

Private bower registry

----

## HAR Resources | A community curated list of resources, tools, projects and applications that support HTTP Archive (HAR)
[ahmadnassri.github.io/har-resources](https://ahmadnassri.github.io/har-resources "HAR Resources | A community curated list of resources, tools, projects and applications that support HTTP Archive (HAR)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">정리</span></p>

HTTP Archive(HAR)을 다루는 도구와 자원에 대한 정리

----
<h1 class="site-genre">소프트웨어、툴、라이브러리 관련</h1>

----

## acornejo/jjv
[github.com/acornejo/jjv](https://github.com/acornejo/jjv "acornejo/jjv")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

JSON 스키마에 대한 정의 및 검증을 수행하는 라이브러리

----

## caiogondim/logdown
[github.com/caiogondim/logdown](https://github.com/caiogondim/logdown "caiogondim/logdown")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Logger + Markdown 라이브러리
브라우저, Node.js 양쪽에서 모두 동작

----

## T3 JavaScript Framework - T3 JavaScript Framework
[t3js.org/](http://t3js.org/ "T3 JavaScript Framework - T3 JavaScript Framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Box사의 JavaScript 프레임워크
AngularJS 1.x 계열과 비슷한 모듈 구조이지만, 기본 구조가 컴팩트하고 콜 스택 또한 꽤 심플하게 만들어졌다. 'debug' 옵션을 활성화시키면 에러 메시지를 쉽게 출력할 수 있도록 설계되어 있다. 

----

## vdemedes/interaptor
[github.com/vdemedes/interaptor](https://github.com/vdemedes/interaptor "vdemedes/interaptor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

mitm을 사용하여 만들어진 HTTP stub 라이브러리
특정한 request에 대해서 임의의 response를 정의하여 전달한다.

----
