---
title: "2015-05-27 JS: Promise의 있을법한 오류, AngularJS 2를 향해서、Plain JS"
author: azu
translator: ChoEun
layout: post
date : 2015-05-27T22:12
category: JSer
tags:
    - Promise
    - AngularJS
    - DOM
    - jQuery

---

JSer.info #229 - [We have a problem with promises](http://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html "We have a problem with promises") 글에서, Promise에서 있을법한 오류 등에 대해 정리해서 소개합니다.

Promise의 동작 흐름 해설, 이상한 작성 방법과 이를 수정한 작성 방법을 통틀어 소개하고 있어 잘 정리되어있다고 생각합니다.

[JavaScript Promise 책](http://azu.github.io/promises-book/ "JavaScript Promise 책")애서도 대부분 같은 이야기를 하고 있어서, 함께 봐도 좋으리라 생각합니다.

----

[JavaScript - AngularJS 모던 프랙티스 - Qiita](http://qiita.com/armorik83/items/5542daed0c408cb9f605 "JavaScript - AngularJS 프랙티스 - Qiita") 글에서, 이미 AngularJS 1.x를 사용하고 있는 사람이 [AngularJS 2](https://angular.io/ "Angular")를 대응하고자 할 때 어떻게 1.x에서 작성해두어야하는가에 대해 정리하고 있습니다.

[AngularJS 2](https://angular.io/ "Angular")에선 어떻게 작성하게 될것인가, 2.x에서는 폐지된 기능, 또 관련있는 라이버리나 툴에 대해서도 작성되어 있어, AngularJS를 사용하고 있는 분이라면 읽어보시면 좋을 거 같습니다.

----

[Plain JavaScript - Functions and Helpers](http://plainjs.com/javascript/ "Plain JavaScript - Functions and Helpers") 사이트에서는、jQuery 메소드를 Pure JavaScript로 작성하기 위해서는 어떤 식으로 작성해야 하는가에 대해 레퍼런스식으로 적어두었습니다.

[You Might Not Need jQuery](http://youmightnotneedjquery.com/ "You Might Not Need jQuery")와 비슷한 느낌이지만, DOM API 사용법의 확인책같은 느낌으로 사용합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## async/CHANGELOG.md at master · caolan/async
[github.com/caolan/async/blob/master/CHANGELOG.md#v100](https://github.com/caolan/async/blob/master/CHANGELOG.md#v100 "async/CHANGELOG.md at master · caolan/async")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

비동기처리를 관리하는 라이브러리 async 1.0.0 릴리즈

----
<h1 class="site-genre">아티클</h1>

----

## We have a problem with promises
[pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html](http://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html "We have a problem with promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">모음</span></p>

Promise의 여러 함정이나 안티패턴에 대해 잘 정리되어 있습니다.

- [JavaScript Promise 책](http://azu.github.io/promises-book/ "JavaScript Promise 책")

----

## JavaScript - AngularJS 모던 프랙티스 - Qiita
[qiita.com/armorik83/items/5542daed0c408cb9f605](http://qiita.com/armorik83/items/5542daed0c408cb9f605 "JavaScript - AngularJS 모던 프랙티스 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

AngularJS 2로 이동하기 쉽게 하기위해서는 어떻게 해야하는가에 대한 튜토리얼
1.x에서도 ES6 Classes를 사용한 작성법을 사용하기 위한 리팩토링 방법.
AngularJS 2에서의 directive、모듈、관련 라이브러리 및 툴、FAQ 등

----

## Moving to ES6 from CoffeeScript
[gist.github.com/danielgtaylor/0b60c2ed1f069f118562](https://gist.github.com/danielgtaylor/0b60c2ed1f069f118562 "Moving to ES6 from CoffeeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CoffeeScript</span></p>

CoffeeScript에서 ES6로 이동하기 위한 문법 비교와 ES6의 구문 및 기능 소개

----

## ES6 — classes and inheritance — Medium
[medium.com/@mrzepinski/es6-classes-and-inheritance-607804080906](https://medium.com/@mrzepinski/es6-classes-and-inheritance-607804080906 "ES6 — classes and inheritance — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Classes와 ES5 사이의 작성법 비교
getter나 setter、세세한 속기도 함께 소개하고 있습니다.

----

## Why Backbone.js? - Roost Austin
[roost.bocoup.com/2015/austin/blog/why-backbone/](https://roost.bocoup.com/2015/austin/blog/why-backbone/ "Why Backbone.js? - Roost Austin")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">MVC</span></p>

JavaScript 라이브러리를 어떤 기준으로 선택해야하는 가에 대한 글.
유명한 라이브러리 통계를 비교한 그림과 학습곡선,단점 등에 대해서 작성하고 있어, 어떤 관점으로 바라볼 수 있는가가 흥미롭습니다.

----

## Notifying you of Changes to Notifications
[updates.html5rocks.com/2015/05/Notifying-you-of-notificiation-changes](http://updates.html5rocks.com/2015/05/Notifying-you-of-notificiation-changes "Notifying you of Changes to Notifications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Chrome 44에서 Service Worker를 사용한 push알림에서 임의의 오브젝트를 넘겨줄 수 있게 되었으며, `getNotifications()`로 특정 태그가 연결된 Notification만 추출하는 것도 가능해졌습니다.

----

## graphite, grafana, sitespeed.io, diamond로 계속 Web 퍼포먼스 모니터링 - Qiita
[qiita.com/Jxck\_/items/abfa9f3dd15c5572cbfd](http://qiita.com/Jxck_/items/abfa9f3dd15c5572cbfd "graphite, grafana, sitespeed.io, diamond를 이용한 지속가능한 Web 퍼포먼스 모니터링 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

sitespeed.io를 사용해 실제 브라우저를 동작시켜 Timing API등의 클라이언트 사이드 매트릭스 정보를 지속적으로 취득한 데이터를 graphite로 보존하여 가시화하는 방법에 대한 글입니다.

----

## 최근 Web 지도의 주변 동향을 정리해보았습니다. | #GUNMAGISGEEK
[shimz.me/blog/map/4268](http://shimz.me/blog/map/4268 "최근 Web 지도의 주변 동향을 정리해보았습니다. | #GUNMAGISGEEK")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">GEO</span> <span class="jser-tag">정리</span></p>

GeoJSON을 시작해 웹의 지도 관련 기술에 대한 변화에 대해서

----

## Testing JavaScript — Medium
[medium.com/@nickheiner/testing-javascript-8c8efe8434e](https://medium.com/@nickheiner/testing-javascript-8c8efe8434e "Testing JavaScript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

proxyquire를 사용한 테스트、E2E와 목업、tape를 사용한 테스트에 대해서

----
<h1 class="site-genre">사이트, 서비스, 도큐멘트</h1>

----

## 웹 크리에이터를 위한 정보 사이트 | Web Programming Primer
[wp-p.info/](http://wp-p.info/ "웹 크리에이터를 위한 정보 사이트 | Web Programming Primer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">tutorial</span></p>

HTML/CSS/JavaScript 입문 튜토리얼 모음

----

## Plain JavaScript - Functions and Helpers
[plainjs.com/javascript/](http://plainjs.com/javascript/ "Plain JavaScript - Functions and Helpers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">레퍼런스</span></p>

Pure JavaScript를 사용하여 DOM 조작하는 법 등을 다루는 역레퍼런스

----

## EmberWeekend
[emberweekend.com/episodes](https://emberweekend.com/episodes "EmberWeekend")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">podcast</span></p>

Ember.js를 다루는 podcast

----
<h1 class="site-genre">소프트웨어, 툴, 라이브러리 관련</h1>

----

## sebastian-lenz/typedoc
[github.com/sebastian-lenz/typedoc](https://github.com/sebastian-lenz/typedoc "sebastian-lenz/typedoc")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">API</span> <span class="jser-tag">document</span></p>

TypeScript API 도큐멘트 생성 툴

----

## WebdriverIO - Selenium 2.0 javascript bindings for nodejs
[webdriver.io/](http://webdriver.io/ "WebdriverIO - Selenium 2.0 javascript bindings for nodejs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Selenium</span> <span class="jser-tag">webdriver</span></p>

Node.js의 Selenium/WebDriver API 바인딩.
모바일 플리킹이나 탭 전환등 여러가지 API가 준비되어 있습니다.

----

## symdiff
[symdiff.github.io/](https://symdiff.github.io/ "symdiff")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

HTML과 CSS를 넘겨서 사용하지 않은 CSS를 제거하는 툴

----

## padolsey/operative
[github.com/padolsey/operative](https://github.com/padolsey/operative "padolsey/operative")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

직접 함수를 넘겨서 그걸 Web Worker로 돌리는 라이브러리.
구버전 브라우저를 위한 fallback이나 promise 서포트 등, 하위호환성을 고려해 작성하고 있습니다.

- [operative에서 WebWorkers를 손쉽게 다루다 - 四角革命前夜](http://blog.sasaplus1.com/2015/05/23/01/ "operative에서 WebWorkers를 손쉽게 다루다 - 四角革命前夜")

----

## High-performance javascript library for animations &amp; interfaces | Famous.org
[famous.org/](http://famous.org/ "High-performance javascript library for animations & interfaces | Famous.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span></p>

애니메이션 라이브러리인 Famous가 리뉴얼 공개되었습니다.

----

## Easily testing React components with react-test-tree — Qubit Engineering — Medium
[medium.com/qubit-engineering/easily-testing-react-components-with-react-test-tree-f9e1668b1c2d](https://medium.com/qubit-engineering/easily-testing-react-components-with-react-test-tree-f9e1668b1c2d "Easily testing React components with react-test-tree — Qubit Engineering — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">DOM</span></p>

React component 맞춤 테스트 라이브러리
대상 React component의 `ref`속성을 추가해두는 걸로, click 등의 이벤트 시뮬레이트나 자식 component를 stub하는 것이 가능합니다

- [QubitProducts/react-test-tree](https://github.com/QubitProducts/react-test-tree "QubitProducts/react-test-tree")

----
