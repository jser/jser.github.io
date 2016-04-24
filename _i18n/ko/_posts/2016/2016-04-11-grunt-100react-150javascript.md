---
title: "2016-04-11 JS: Grunt 1.0.0, React 15.0, 도구를 이용해 학습할 수 있는JavaScript"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-04-11T20:00
category: JSer
tags:
    - Grunt
    - React
    - Tutorial

---

JSer.info #274 - Grunt 1.0.0이 정식으로 릴리즈됐습니다.

- [Grunt 1.0.0 released - Grunt: The JavaScript Task Runner](http://gruntjs.com/blog/2016-04-04-grunt-1.0.0-released "Grunt 1.0.0 released - Grunt: The JavaScript Task Runner")
- [JavaScript 태스크 자동화 도구 「Grunt 1.0.0」이 등장. 약 2년간의 개발 침체에서 부활 － Publickey](http://www.publickey1.jp/blog/16/javascriptgrunt_1002.html "JavaScript 태스크 자동화 도구 「Grunt 1.0.0」이 등장. 약 2년간의 개발 침체에서 부활 － Publickey")(일본어)

`grunt.util._`로 참조할 수 있는 lodash의 버전이 4.3.0으로 업데이트되는 등, 1.0.0 RC1에는 의존하고 있는 패키지의 업데이트가 시행됐습니다. 
`grunt.util._` 프로퍼티는 비권장이기 때문에 아래와 같이 직접 lodash를 설치하여 사용할 것을 권장하고 있습니다.


```js
var _ = require('lodash');
```

----

[React v15.0](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")이 릴리즈됐습니다.

하지만 15.0에는 몇 가지 문제가 있어 바로 [React v15.0.1](https://facebook.github.io/react/blog/2016/04/08/react-v15.0.1.html "React v15.0.1")을 릴리즈했습니다. 기본적으로 콘솔창에 0.14.x의 비권장 경고 메시지가 출력되지 않는 상태라면 바로 업데이트 가능한 것 같습니다.

0.14.x에서의 변경 사항은 아래의 잘 정리돼 있습니다.

- [React v15.0 | React](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")
- [React.js v15.0 changes - blog.koba04.com](http://blog.koba04.com/post/2016/03/09/react-js-v15-changes/ "React.js v15.0 changes - blog.koba04.com")(일본어)

또, React의 코어팀의 미팅 노트가 공개돼 있습니다. 해당 노트에는 향후 방침이나 로드맵 등이 작성돼 있으므로 참고하면 좋을 것 같습니다.

- [reactjs/core-notes: Weekly meeting notes from the React core team](https://github.com/reactjs/core-notes "reactjs/core-notes: Weekly meeting notes from the React core team")

----

[Tools to Learn JavaScript By Doing -Telerik Developer Network](http://developer.telerik.com/featured/tools-learn-javascript/ "Tools to Learn JavaScript By Doing -Telerik Developer Network")에는 도구를 이용해 학습할 수 있는 JavaScript에 관해 작성돼 있습니다.

[NodeSchool](http://nodeschool.io/ja/ "NodeSchool")이나 [js-assessment](https://github.com/rmurphey/js-assessment "js-assessment"), [Advent of Code](http://adventofcode.com/ "Advent of Code") 등 문제를 풀면서 학습할 수 있는 사이트나 도구를 소개합니다.

몇해 전에 [테스트로 학습할 수 있는 JavaScript에 관해](http://efcl.info/2012/0414/res3059/ "테스트로 학습할 수 있는 JavaScript에 관해 | Web Scratch")(일본어)라는 글을 작성한 적 있습니다. 실제로 문제를 풀어보면서 학습하면 여러가지 새로운 사실도 알 수 있어 재미있는 학습법인 것 같습니다.

이 글에서 소개하는 [NodeSchool](http://nodeschool.io/ja/ "NodeSchool")의 [workshopper](http://nodeschool.io/ja/#workshopper-list)을 보면 JavaScript 문법 외에도 여러가지 라이브러리나 도구도 학습할 수도 있으니 한번 살펴보길 바랍니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Grunt 1.0.0 released - Grunt: The JavaScript Task Runner
[gruntjs.com/blog/2016-04-04-grunt-1.0.0-released](http://gruntjs.com/blog/2016-04-04-grunt-1.0.0-released "Grunt 1.0.0 released - Grunt: The JavaScript Task Runner")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Grunt</span> <span class="jser-tag">ReleaseNote</span></p>

Grunt 1.0.0이 릴리즈됐습니다.
Grunt 플러그인의 `peerDependencies` 속성에 `"grunt": ">=0.4.0"`을 추가하길 권장합니다.

----

## Release v1.0.0 - Rosebud · SBoudrias/Inquirer.js
[github.com/SBoudrias/Inquirer.js/releases/tag/v1.0.0](https://github.com/SBoudrias/Inquirer.js/releases/tag/v1.0.0 "Release v1.0.0 - Rosebud · SBoudrias/Inquirer.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">library</span></p>

터미널에서 선택 사항 등을 인터렉티브하게 제공할 수 있는 도구 Inquirer.js 1.0.0이 릴리즈됐습니다.
Promise 기반의 API로 변경됐습니다.

----

## normalize.css/CHANGELOG.md at 4.0.0 · necolas/normalize.css
[github.com/necolas/normalize.css/blob/4.0.0/CHANGELOG.md](https://github.com/necolas/normalize.css/blob/4.0.0/CHANGELOG.md "normalize.css/CHANGELOG.md at 4.0.0 · necolas/normalize.css")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

normalize.css 4.0.0이 릴리즈됐습니다.

- [Normalize.scss v4 - Weblog - Hail2u.net](https://hail2u.net/blog/webdesign/modularized-normalize-scss-v4.0.0.html "Normalize.scss v4 - Weblog - Hail2u.net")

----

## AWS Lambda Supports Node.js 4.3
[aws.amazon.com/about-aws/whats-new/2016/04/aws-lambda-supports-node-js-4-3/](https://aws.amazon.com/about-aws/whats-new/2016/04/aws-lambda-supports-node-js-4-3/ "AWS Lambda Supports Node.js 4.3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

AWS Lambda에서 Node.js 4.3을 지원합니다.

----

## jsdom/Changelog.md at 8.3.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/8.3.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/8.3.0/Changelog.md "jsdom/Changelog.md at 8.3.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 8.3.0이 릴리즈됐습니다.
Node Canvas을 사용하여 외부 리소스 `img`를 처리할 수 있도록 추가됐습니다(optional).
`img.naturalWidth` 등에서 실제 데이터에 근거한 값을 가져올 수 있습니다.

또, Page Visibility API의 기본적인 부분을 구현하는 등 다양한 변경 사항이 있습니다.

----

## React v15.0 | React
[facebook.github.io/react/blog/2016/04/07/react-v15.html](https://facebook.github.io/react/blog/2016/04/07/react-v15.html "React v15.0 | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v15.0이 릴리즈됐습니다.
IE8의 지원을 종료했고, semver에 근거하여 업데이트하도록 정책을 변경했습니다.
0.14에서 비권장 경고 메시지가 출력되지 않는 상태라면 바로 업데이트해도 무방합니다.

----
<h1 class="site-genre">아티클</h1>


----

## Tools to Learn JavaScript By Doing -Telerik Developer Network
[developer.telerik.com/featured/tools-learn-javascript/](http://developer.telerik.com/featured/tools-learn-javascript/ "Tools to Learn JavaScript By Doing -Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">tutorial</span></p>

js-assessment, NodeSchool, Advent of Code 등 익터렉티브하게 JavaScript를 학습할 수 있는 도구를 소개합니다.

----

## Introducing the Microsoft Edge Platform Issue Tracker | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/04/06/edgehtml-issue-tracker/](https://blogs.windows.com/msedgedev/2016/04/06/edgehtml-issue-tracker/ "Introducing the Microsoft Edge Platform Issue Tracker | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">issue</span></p>

MS Edge의 Issue Tracker가 업데이트 됐습니다.

- [azu/browser-javascript-resource: Browser JavaScript Resource.](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource: Browser JavaScript Resource.")

----

## WebdriverIO로 시작하는 E2E 테스트와 PageObject - Qiita(일본어)
[qiita.com/derui@github/items/9ee72c7533c9a57aa8d2](http://qiita.com/derui@github/items/9ee72c7533c9a57aa8d2 "WebdriverIO로 시작하는 E2E 테스트와 PageObject - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span></p>

WebdriverIO로 시작하는 E2E 테스트를 PageObject 패턴으로 구현하는 과정을 소개합니다.

----

## React 컴포넌트를 npm 패키지로 개발 - Hatena Developer Blog(일본어)
[developer.hatenastaff.com/entry/2016/04/09/180000](http://developer.hatenastaff.com/entry/2016/04/09/180000 "React 컴포넌트를 npm 패키지로 개발 - Hatena Developer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

React 컴포넌트를 npm 라이브러리로 개발하는 방법과 장점 및 단점에 관해 작성돼 있습니다.

----

## Streaming template literals - JakeArchibald.com
[jakearchibald.com/2016/streaming-template-literals/](https://jakearchibald.com/2016/streaming-template-literals/ "Streaming template literals - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

Template Literal과 WHATWG Stream을 함께 사용하는 방법에 관해 작성돼 있습니다.

----

## Angular 2 — Unit Testing recipes — Google Developer Experts — Medium
[medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584](https://medium.com/google-developer-experts/angular-2-unit-testing-with-jasmine-defe20421584 "Angular 2 — Unit Testing recipes — Google Developer Experts — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AnguarJS2의 테스트 패턴을 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Introduction to flux-util // Speaker Deck
[speakerdeck.com/joere/introduction-to-flux-util](https://speakerdeck.com/joere/introduction-to-flux-util "Introduction to flux-util // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">library</span></p>

Facebook의 flux util을 소개하는 슬라이드입니다.
flux util의 기능이나 담당하는 역할에 관해 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## React.run - Beta
[www.react.run/](http://www.react.run/ "React.run - Beta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">webservice</span></p>

React Component의 코드를 실행 및 공유할 수 있는 JSFiddle과 같은 느낌의 서비스입니다.

----

## Microsoft Edge Developer Resources
[dev.windows.com/en-us/microsoft-edge/platform/data/](https://dev.windows.com/en-us/microsoft-edge/platform/data/ "Microsoft Edge Developer Resources")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">webservice</span> <span class="jser-tag">統計</span></p>

CSS 속성의 사용률이나 각 브라우저의 API 지원 현황 등을 알 수 있는 MSEdge의 서비스입니다.

- [Chrome Platform Status](https://www.chromestatus.com/features "Chrome Platform Status")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## jdonaghue/es-search: Search ECMAScript structurally
[github.com/jdonaghue/es-search](https://github.com/jdonaghue/es-search "jdonaghue/es-search: Search ECMAScript structurally")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AST</span> <span class="jser-tag">검색</span> <span class="jser-tag">JavaScript</span></p>

AST 기반으로 JavaScript의 코드에서 질의에 일치하는 부분(구조)을 검색할 수 있는 도구입니다.

----

## redfin/react-server: React server monorepo
[github.com/redfin/react-server](https://github.com/redfin/react-server "redfin/react-server: React server monorepo")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">서버</span></p>

React를 기반으로 구현한 express middleware 등의 서버 관련 구현체입니다.

----

## mohayonao/web-audio-engine: Pure JS implementation of the Web Audio API
[github.com/mohayonao/web-audio-engine](https://github.com/mohayonao/web-audio-engine "mohayonao/web-audio-engine: Pure JS implementation of the Web Audio API")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

순수 JavaScript 구현한 Web Audio API입니다.
PCM audio를 Node Stream에 출력할 수 있습니다.

----

## kenwheeler/cash: An absurdly small jQuery alternative for modern browsers
[github.com/kenwheeler/cash](https://github.com/kenwheeler/cash "kenwheeler/cash: An absurdly small jQuery alternative for modern browsers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">library</span></p>

jQuery 대체할 수 있는 라이브러리입니다.
jQuery의 DOM 위주의 메서드를 모아놓은 느낌입니다.

----

## brigand/babel-plugin-flow-react-proptypes: A babel plugin to generate React PropTypes definitions from Flow type declarations.
[github.com/brigand/babel-plugin-flow-react-proptypes](https://github.com/brigand/babel-plugin-flow-react-proptypes "brigand/babel-plugin-flow-react-proptypes: A babel plugin to generate React PropTypes definitions from Flow type declarations.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span> <span class="jser-tag">React</span></p>

FlowType으로 React의 propTypes을 작성하면 JavaScript의 propTypes으로 변환해주는 Babel 플러그인입니다.

----

## c58/marsdb: MarsDB is a Promise based lightweight database with MongoDB query syntax, written on ES6
[github.com/c58/marsdb](https://github.com/c58/marsdb "c58/marsdb: MarsDB is a Promise based lightweight database with MongoDB query syntax, written on ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

minimongo 같은 클라이언트 사이브 용의 데이터베이스 라이브러리입니다.
Adpter로 백엔드에 데이터를 보존하는 방법을 변경할 수 있고 Browser 뿐만아니라 Electron, Node.js 등에서도 사용할 수 있습니다.

----

## PlasmaPower/assert-request: Assert responses to HTTP requests in Node.JS
[github.com/PlasmaPower/assert-request](https://github.com/PlasmaPower/assert-request "PlasmaPower/assert-request: Assert responses to HTTP requests in Node.JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span></p>

Node.js에서 특정 request에 해당하는 response를 assert 할 수 있는 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## Amazon.com: Isomorphic Application Development with JavaScrip eBook: Konstantin Tarkus: Kindle Store
[www.amazon.com/Isomorphic-Application-Development-JavaScrip-Konstantin-ebook/dp/B01DWFRFVG](http://www.amazon.com/Isomorphic-Application-Development-JavaScrip-Konstantin-ebook/dp/B01DWFRFVG "Amazon.com: Isomorphic Application Development with JavaScrip eBook: Konstantin Tarkus: Kindle Store")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017년 2월 4일에 발매 예정인 Isomorphic JavaScript에 대해서 다루는 서적입니다.

----
