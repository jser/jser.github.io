---
title: "2016-10-10 JS: JavaScript와 Unicode, Web Components, npm-scripts"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-10-10T23:11
category: JSer
tags:
    - Unicode
    - WebComponents
    - npm

---

JSer.info #300 - JSer.info가 300회를 맞이했습니다.
아래 기사에 JSer.info에 최근 추가한 기능이나 변경 사항 등에 관해 정리돼 있습니다

- [JSer.info 300회째 && https 적용 && 사용자 투고 기능](https://jser.info/ko/2016/10/10/300posts/)

----

[What every JavaScript developer should know about Unicode](https://rainsoft.io/what-every-javascript-developer-should-know-about-unicode/ "What every JavaScript developer should know about Unicode")라는 글에는 JavaScript와 Unicode에 관해 전체적이고 구체적으로 설명돼 있습니다 

Unicode의 용어, Character, Code point, Plane, BMP, Code unit, 써로게이트 페어 Combing marks, 이스케이프 시퀀스, 문자열 비교, Normalize, length의 반환 값, 정규 표현식 등 폭넓게 다루고 있습니다.
또, ES2015에 `String#normalize`메서드나 `String.fromCodePoint`와 `String#codePointAt` 메서드가 추가됐고, Iterable로 Unicode를 다룰 수 있게 되는 등 관련 API도 많이 늘어나고 있는 추세 이므로 한번 살펴보면 좋을 것 같습니다.  

----

[Web Components 2016 & Polymer v2](https://1000ch.github.io/slide/webcomponents-2016/ "Web Components 2016 &amp; Polymer v2")라는 슬라이드에는 Chrome과 Safari 등에 구현돼 있는 Shadow DOM v1, Custom Elements v1에 관해 작성돼 있습니다. 
Web Components의 라이브러리로써 유명한 Polymer v2의 로드-맵이나 is 속성 등 최근 Web Components와 관련된 여러가지 정보가 정리돼 있습니다

----

[npm-scripts로 Web 프론트엔드 개발을 관리한다 – 아카베코마이리](http://akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/ "npm-scripts로 Web 프론트엔드 개발을 관리한다 – 아카베코마이리")(일본어)라는 글에는 npm scripts(npm run-scripts)를 사용해 태스크를 처리하는 방법에 관해 작성돼 있습니다.
grunt, gulp 등의 Task Runner로 할 수 있는 처리를 npm run-scripts로 처리하는 방법이나 CLI를 이용하는 방법, 크로스 플랫폼을 대응한 태스크 작성 법 등 폭넓게 작성돼 있습니다

또, 해당 웹사이트에는 npm run-scripts에서 문제가 되는 변수를 사용할 수 없는 문제를 [cross-conf-env](http://akabeko.me/blog/2016/05/cross-conf-env-1-0-release/ "cross-conf-env")(일본어)를 사용해 해결하는 과정도 소개돼 있습니다

----
<h1 class="site-genre">헤드라인</h1>

----

## ECMAScript proposal updates @ 2016-10 | ECMAScript Daily
[ecmascript-daily.github.io/2016/10/02/proposals-updates](https://ecmascript-daily.github.io/2016/10/02/proposals-updates "ECMAScript proposal updates @ 2016-10 | ECMAScript Daily")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2016년 10월 시점에서의 ECMAScript Proposal의 Status와 9월의 미팅에서 변경된 Stage가 정리돼 있습니다.

----

## jsdom/Changelog.md at 9.6.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.6.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.6.0/Changelog.md "jsdom/Changelog.md at 9.6.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.6.0이 릴리즈 됐습니다.
HTMLCollection이 iterable에 대응하는 등 다양한 변경 사항이 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## What every JavaScript developer should know about Unicode
[rainsoft.io/what-every-javascript-developer-should-know-about-unicode/](https://rainsoft.io/what-every-javascript-developer-should-know-about-unicode/ "What every JavaScript developer should know about Unicode")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Unicode</span></p>

JavaScript의 문자열과 Unicode에 관해 전체적이고 구체적으로 설명한 글입니다.
Unicode의 용어, Character, Code point, Plane, BMP, Code unit, 써로게이트 페어 Combing marks, 이스케이프 시퀀스, 문자열 비교, Normalize, length의 반환 값, 정규 표현식 등 폭넓게 다루고 있습니다.

----

## Progressive Web Apps with React.js: Part 2 — Page Load Performance – Medium
[medium.com/@addyosmani/progressive-web-apps-with-react-js-part-2-page-load-performance-33b932d97cf2](https://medium.com/@addyosmani/progressive-web-apps-with-react-js-part-2-page-load-performance-33b932d97cf2 "Progressive Web Apps with React.js: Part 2 — Page Load Performance – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span></p>

초기 출력을 빠르게 하기 위해 Routing 마다 파일로 나눠 동적으로 로드하는 기법에 관해 작성돼 있습니다.
webpack을 사용한 분할과 읽어들이는 방법, link preload를 사용해 먼저 읽어들이는 방법, 캐쉬 등에 관해 설명합니다. 

----

## JavaScript 라이브러리 / 프로젝트의 파일사이즈 문제점을 찾는 방법 - Qiita(일본어)
[qiita.com/azu/items/7b54d614dc816780034a](http://qiita.com/azu/items/7b54d614dc816780034a "JavaScript 라이브러리 / 프로젝트의 파일사이즈 문제점을 찾는 방법 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Browserify나 webpack등에서 bundle한 파일의 사이즈나 의존 모듈의 사이즈 등을 확인하는 방법에 관해 작성돼 있습니다.

----

## npm-scripts로 Web 프론트엔드 개발을 관리한다 – 아카베코마이리
[akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/](http://akabeko.me/blog/2016/10/npm-scripts-web-front-end-development/ "npm-scripts で Web フロントエンド開発を管理する – アカベコマイリ")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span></p>

npm run-script에 관해 자세히 소개하는 글입니다.
grunt, gulp 등의 Task Runner로 할 수 있는 전형적인 사용 패턴을 npm run-script로 처리할 경우 어떻게 되는지, 크로스플랫폼에서 동작할 수 있도록 작성하는 방법과 규칙에 관해 작성돼 있습니다.

----

## event.offsetX, Y의 덫...어디가 원점 좌표값인지를 이해한다 (currentTarget과 target) - Qiita(일본어)
[qiita.com/yukiB/items/cc533fbbf3bb8372a924](http://qiita.com/yukiB/items/cc533fbbf3bb8372a924 "event.offsetX, Y의 덫...어디가 원점 좌표값인지를 이해한다 (currentTarget과 target) - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

target과 currentTarget의 차이, offsetX/Y, screenX/Y, getBoundingClientRect() 등에 관해 설명합니다.

- [마우스 이벤트로 얻을 수 있는 커서 좌표 파라메터 정리(offset, page, screen, client) - Qiita](http://qiita.com/yukiB/items/31a9e9e600dfb1f34f76 "마우스 이벤트로 얻을 수 있는 커서 좌표 파라메터 정리(offset, page, screen, client) - Qiita")(일본어)

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Proper Error Handling // Speaker Deck
[speakerdeck.com/michelebertoli/proper-error-handling](https://speakerdeck.com/michelebertoli/proper-error-handling "Proper Error Handling // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">슬라이드</span></p>

에러 처리와 관련된 핸들링에 관해 소개하는 슬라이드입니다.
무엇 때문에 필요한지, 기법이나 React 등 에서의 에러 처리에 관해 작성돼 있습니다

----

## create-react-app-introduction // Speaker Deck(일본어)
[speakerdeck.com/adwd/create-react-app-introduction](https://speakerdeck.com/adwd/create-react-app-introduction "create-react-app-introduction // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">슬라이드</span></p>

React의 StarterKit과 같은 `create-react-app`를 소개합니다.

- [facebookincubator/create-react-app: Create React apps with no build configuration.](https://github.com/facebookincubator/create-react-app "facebookincubator/create-react-app: Create React apps with no build configuration.")

----

## Web Components 2016 &amp; Polymer v2
[1000ch.github.io/slide/webcomponents-2016/](https://1000ch.github.io/slide/webcomponents-2016/ "Web Components 2016 & Polymer v2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">スライド</span></p>

Web Components를 소개하는 슬라이드입니다.
Shadow DOM v1, Custom Elements v1 각각의 변경 사항과 Polymer v2와 `is` 속성 등에 관해 설명합니다.

----

## WebVR - virtual reality in your browsers // Speaker Deck
[speakerdeck.com/casarock/webvr-virtual-reality-in-your-browsers](https://speakerdeck.com/casarock/webvr-virtual-reality-in-your-browsers "WebVR - virtual reality in your browsers // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">VR</span></p>

VR의 역사와 WebVR API에 관해 소개하는 슬라이드 입니다.
또 WebVR API를 사용한 유즈케이스도 소개합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## 하테나 교과서 JavaScript 책 · GitBook(일본어)
[hatena.github.io/Hatena-Textbook-JavaScript/](https://hatena.github.io/Hatena-Textbook-JavaScript/ "하테나 교과서 JavaScript 책 · GitBook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ebook</span></p>

JavaScript의 기본 문법이나 DOM, Node.js, jQuery 등을 훑어볼 수 있는 웹 도서입니다.

- [하테나 여름 인턴 2015년을 마치며, 「하테나 교과서」를 업데이트했습니다 - Hatena Developer Blog](http://developer.hatenastaff.com/entry/2016/10/05/160000 "하테나 여름 인턴 2015년을 마치며, 「하테나 교과서」를 업데이트했습니다 - Hatena Developer Blog")(일본어)
- [hatena/Hatena-Textbook-JavaScript: 하테나 교육용 JavaScript 교과서](https://github.com/hatena/Hatena-Textbook-JavaScript "hatena/Hatena-Textbook-JavaScript: 하테나 교육용 JavaScript 교과서")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## babel/babel-preset-env: WIP: Autoprefixer for Babel: target specific environments (browser, node, etc)
[github.com/babel/babel-preset-env](https://github.com/babel/babel-preset-env "babel/babel-preset-env: WIP: Autoprefixer for Babel: target specific environments (browser, node, etc)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

target으로 브라우저나 Node.js의 버전을 지정하여 해당 버전에서 필요로하는 최소한의 변환을 실시하는 babel preset입니다.

----

## DeNADev/wahid: A CreateJS-compatible library for games
[github.com/DeNADev/wahid](https://github.com/DeNADev/wahid "DeNADev/wahid: A CreateJS-compatible library for games")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

CreateJS 호환 (모바일) 게임 용 라이브러리입니다.

- [CreateJS 호환 라이브러리 wahid 개발 — Mobage Developers Blog](http://developers.mobage.jp/blog/createjs-wahid "CreateJS 호환 라이브러리 wahid 개발 — Mobage Developers Blog")(일본어)

----

## UI-Router
[ui-router.github.io/](https://ui-router.github.io/ "UI-Router")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Angular와 React를 지원하는 라우터 라이브러리입니다.

----

## Office UI Fabric
[dev.office.com/fabric](http://dev.office.com/fabric "Office UI Fabric")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">UI</span> <span class="jser-tag">React</span> <span class="jser-tag">AngularJS</span></p>

Office 365 등의 스타일을 지원하는 UI 컴포넌트를 제공하는 라이브러리입니다.
VanillaJS, React, Angular, iOS 버전이 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## React Components - O&#x27;Reilly Media
[shop.oreilly.com/product/9781785889288.do](http://shop.oreilly.com/product/9781785889288.do "React Components - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React Component에 관한 도서입니다.

----

## Manning | Functional Programming in JavaScript
[www.manning.com/books/functional-programming-in-javascript](https://www.manning.com/books/functional-programming-in-javascript "Manning | Functional Programming in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">함수형 프로그래밍</span> <span class="jser-tag">book</span></p>

함수형 프로그래밍에 관한 도서입니다.
샘플 코드가 ES2015 기반으로 작성돼 있습니다.

----

## JavaScript : Functional Programming for JavaScript Developers | PACKT Books
[www.packtpub.com/web-development/javascript-functional-programming-javascript-developers](https://www.packtpub.com/web-development/javascript-functional-programming-javascript-developers "JavaScript : Functional Programming for JavaScript Developers | PACKT Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">함수형 프로그래밍</span></p>

JavaScript의 함수형 프로그래밍 패턴을 소개하는 서적입니다.

----
