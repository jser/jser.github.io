---
title: "2016-03-03 JS: Ember.js LTS, ECMA i18n API 3rd Edition RC, jQuery 3의 변경사항"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-03-03T21:53
category: JSer
tags:
    - Ember
    - i18n
    - ECMAScript
    - jQuery

---

JSer.info #268 - [Ember.js - Announcing Ember's First LTS Release](http://emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html "Ember.js - Announcing Ember&#39;s First LTS Release")에는 Ember.js의 LTS(Long Term Support)에 관해 작성돼 있습니다.

[Ember.js 2.4](http://emberjs.com/blog/2016/02/29/ember-2-4-released.html "Ember.js 2.4")가 최초의 LTS로 릴리즈됩니다.

![LTS](http://emberjs.com/images/blog/2016-02/Releases@3x.svg)

LTS는 36 주간 버그를 대응하며, 60 주간 보안을 개선하는 릴리즈 사이클입니다.
즉, Ember.js 2.4는 2016년 11월 까지 버그를 대응하고, 2017년 4월 까지 보안을 개선하는 배포가 진행됩니다.

----

ECMA-402에서 책정하는 ECMAScript i18n API의 3rd Edition RC 버전이 릴리즈됐습니다.

- [ECMAScript® 2016 Internationalization API Specification (3rd Edition)](http://tc39.github.io/ecma402/ "ECMAScript® 2016 Internationalization API Specification (3rd Edition)")
- [Release 3rd Edition - Release Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402")

[Intl 오브젝트](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Intl "Intl 오브젝트")(일본어)라고 부르는 국제화와 관련한 API를 책정하는 사양입니다.

사용하는 입장에서 2nd Edition과의 차이점은 [`Intl.getCanonicalLocales (locales)`](http://tc39.github.io/ecma402/#sec-intl.getcanonicallocales "Intl.getCanonicalLocales (locales)")의 API가 늘어난 정도 입니다.

- [tc39-notes/nov-19.md at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/blob/master/es7/2015-11/nov-19.md#abstract-locale-operations)
- [Exposing `CanonicalizeLocaleList()` abstract operation via `Intl.getCanonicalLocales()` by caridy · Pull Request #78 · tc39/ecma402](https://github.com/tc39/ecma402/pull/78)

ECMA-402도 ECMAScript(ECMA-262)와 동일하게 [The TC39 Process](https://tc39.github.io/process-document/ "The TC39 Process")를 채용하고 있습니다.
따라서 매년 릴리즈 하고, Stage의 Proposal 관리 역시 [tc39/ecma402: Status, process, and documents for ECMA 402](https://github.com/tc39/ecma402 "tc39/ecma402: Status, process, and documents for ECMA 402")를 따르고 있습니다.

- [Introduction | ECMAScript란 무엇인가?](http://azu.github.io/slide-what-is-ecmascript/ "Introduction | ECMAScript란 무엇인가?")(일본어)

----

[What's New in jQuery 3 - Telerik Developer Network](http://developer.telerik.com/featured/whats-new-in-jquery-3/ "What&#39;s New in jQuery 3 - Telerik Developer Network")에는 현재 [Beta](https://blog.jquery.com/2016/01/14/jquery-3-0-beta-released/ "Beta") 버전이 릴리즈돼 있는 jQuery 3에 관해 자세히 설명돼 있습니다.

변경 사항을 자세히 소개하고 있으므로 jQuery에 관심 있는 사람은 보면 좋을 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Release v6.6.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.6.0](https://github.com/babel/babel/releases/tag/v6.6.0 "Release v6.6.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.6.0이 릴리즈됐습니다.
transform-es3-member-expression-literals를 다시 조합하여 사용할 수 있도록 됐고, Babel6에서 삭제된 옵션을 사용할 때 발생하는 에러를 알기 쉽게 출력하는 등 여러가지 변경 사항이 있습니다.

----

## Ember.js - Announcing Ember&#x27;s First LTS Release
[emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html](http://emberjs.com/blog/2016/02/25/announcing-embers-first-lts.html "Ember.js - Announcing Ember's First LTS Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js가 LTS(Long Term Support) 버전을 릴리즈할 예정입니다.
Ember.js 2.4가 최초의 LTS 버전이 됩니다.

----

## Ember.js - Ember.js 2.4 and 2.5 Beta Released
[emberjs.com/blog/2016/02/29/ember-2-4-released.html](http://emberjs.com/blog/2016/02/29/ember-2-4-released.html "Ember.js - Ember.js 2.4 and 2.5 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 2.4와 2.5 Beta가 릴리즈됐습니다.
2.5에는 `Object.assign`의 polyfill인 `Ember.assign`과 이벤트의 테스트 헬퍼가 추가됐습니다.

----

## Release 3rd Edition - Release Candidate · tc39/ecma402 · GitHub
[github.com/tc39/ecma402/releases/tag/3.0-rc-1](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402 · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript Internationalization API 3rd Edition RC가 릴리즈됐습니다. i18n API의 사양을 책정하고 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## What&#x27;s New in jQuery 3 - Telerik Developer Network
[developer.telerik.com/featured/whats-new-in-jquery-3/](http://developer.telerik.com/featured/whats-new-in-jquery-3/ "What's New in jQuery 3 - Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span></p>

jQuery 3 관해 작성돼 있습니다.
for/of로 열거하는 방법, `$.get`/`$.post`의 시그니처 추가, requestAnimationFrame 대응, `data()`의 동작 방식 변경, Deferred가 Promise/A+ 호환되는 부분 그리고 SVG 지원에 관한 내용 등 다양한 변경 사항이 작성돼 있습니다.

----

## Step by Step Guide To Building React Redux Apps — Medium
[medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a "Step by Step Guide To Building React Redux Apps — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

React+Redux를 스텝 바이 스텝으로 배울 수 있는 튜토리얼입니다.

----

## Design by Contract with Flow, React, and ESLint · Jeff Winkler
[react.rocks/blog/post/propTypes\_React\_Flow/](https://react.rocks/blog/post/propTypes_React_Flow/ "Design by Contract with Flow, React, and ESLint · Jeff Winkler")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">flowtype</span></p>

React의 코드를 ESLint + FlowType으로 검사하는 구조에 관해 작성돼 있습니다.

----

## Preload: What Is It Good For? – Smashing Magazine
[www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "Preload: What Is It Good For? – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span></p>

`<link rel="preload">`의 preload 관해 자세히 설명돼 있습니다.
마크업 레벨에서 로드되는 우선순위를 지정할 수 있고, CSP(Content-Security-Policy)를 함께 적용할 수 있으며 `as` 속성으로 적절한 형태(js, css, image 등)로 리소스를 불러올 수 있는 방법 등 여러가지 특성 관해 작성돼 있습니다.

----

## Building command line tools with Node.js - Atlassian Developers
[developer.atlassian.com/blog/2015/11/scripting-with-node/?categories=node.js](https://developer.atlassian.com/blog/2015/11/scripting-with-node/?categories=node.js "Building command line tools with Node.js - Atlassian Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">tutorial</span></p>

Node.js로 CLI 도구를 만드는 방법을 소개하는 튜토리얼입니다.

----

## Falcor 입문 1일차 Falcor는 무엇인가 - Qiita(일본어)
[qiita.com/Quramy/items/5cf4f112d715c2e2d300](http://qiita.com/Quramy/items/5cf4f112d715c2e2d300 "Falcor 입문 1일차 Falcor는 무엇인가 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">API</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Falcor에 관해 소개돼 있습니다.
데이터의 투명성과 일관성에 관해 이야기합니다.

> Falcor를 이용할 때 느끼는 큰 장점의 1가지는 「데이터가 서버에 있는지, 클라이언트에 있는지 신경쓰지 않고 다룰 수 있다」는 것이다.

----

## TypeScript의 타입 정의 관리 도구인 Typings에 관해 - Qiita(일본어)
[qiita.com/literalice/items/d83249a5646abcb0bec6](http://qiita.com/literalice/items/d83249a5646abcb0bec6 "TypeScript의 타입 정의 관리 도구인 Typings에 관해 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

typings의 사용 방법에 관해 작성돼 있습니다.

----

## async/await: It’s Good and Bad — Medium
[medium.com/@benlesh/async-await-it-s-good-and-bad-15cf121ade40](https://medium.com/@benlesh/async-await-it-s-good-and-bad-15cf121ade40 "async/await: It’s Good and Bad — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

async/await의 장/단점에 관해 작성돼 있습니다.

----

## gaearon/react-makes-you-sad: Here’s a flowchart to make you happy again!
[github.com/gaearon/react-makes-you-sad](https://github.com/gaearon/react-makes-you-sad "gaearon/react-makes-you-sad: Here’s a flowchart to make you happy again!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">그림</span></p>

그림을 이용해 React를 학습하는 절차나 에코시스템에 관해 어드바이스 하는 아티클입니다.

- [한국어 버전](https://github.com/ehrudxo/react-makes-you-sad)
- [일본어 버전](http://qiita.com/kuy/items/bfe5975205c9237ebd26)

----

## Examples of name clashes in JavaScript’s standard library
[www.2ality.com/2016/02/js-name-clashes.html](http://www.2ality.com/2016/02/js-name-clashes.html "Examples of name clashes in JavaScript’s standard library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

새롭게 추가하는 메서드 명이 충돌하는 현상인 Break th web의 예와 Symbol에 관해 작성돼 있습니다.
또, `Symbol.unscopables`가 도입된 사정(경위)에 관해서도 작성돼 있습니다.

----

## Elmish: Functional Programming in Javascript — Medium
[medium.com/@chetcorcos/elmish-functional-programming-in-javascript-50995f1d4b9e](https://medium.com/@chetcorcos/elmish-functional-programming-in-javascript-50995f1d4b9e "Elmish: Functional Programming in Javascript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">設計</span></p>

Elm적인 아키텍처를 JavaScript로 구현하면서 배운것에 관해 작성돼 있습니다.

- [ccorcos/elmish: A Javascript UI library inspired by Elm](https://github.com/ccorcos/elmish "ccorcos/elmish: A Javascript UI library inspired by Elm")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## ConFoo: Measuring SPA Performance // Speaker Deck
[speakerdeck.com/bluesmoon/confoo-measuring-spa-performance](https://speakerdeck.com/bluesmoon/confoo-measuring-spa-performance "ConFoo: Measuring SPA Performance // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">슬라이드</span></p>

SPA에서 성능을 측정하는 방법이 작성돼 있는 슬라이드입니다.
XHR의 hook, MutationObserver, FetchObserver에 관해 이야기합니다.

----

## React.js Conf 2016 - YouTube
[www.youtube.com/playlist?list=PLb0IAmt7-GS0M8Q95RIc2lOM6nc77q1IY](https://www.youtube.com/playlist?list=PLb0IAmt7-GS0M8Q95RIc2lOM6nc77q1IY "React.js Conf 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">영상 </span></p>

React.js Conf 2016의 영상이 공개돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Doclets
[www.doclets.io/](https://www.doclets.io/ "Doclets")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">webservice</span></p>

JSDoc과 Markdown으로 문서를 포스팅할 수 있는 사이트입니다.
yml에 소스와 Markdown 파일을 지정하면 문서를 만들어줍니다.

----

## HTML Standard 일본어 버전(일본어)
[momdo.github.io/html/](https://momdo.github.io/html/ "HTML Standard 일본어 버전")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">HTML</span> <span class="jser-tag">翻訳</span></p>

WHATWG Living Standard 일본어 버전입니다.

- [HTML Living Standard 번역을 시작했습니다 - 물밑의 피](http://momdo.hatenablog.jp/entry/20160301/1456833788 "HTML Living Standard 번역을 시작했습니다 - 물밑의 피")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## rtsao/csjs: Modular, scoped CSS with ES6
[github.com/rtsao/csjs](https://github.com/rtsao/csjs "rtsao/csjs: Modular, scoped CSS with ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

Template Strings을 사용해 CSS를 캡슐화하는 라이브러리입니다.

----

## mohayonao/web-audio-mock-api: mock API which implements the Web Audio API&#x27;s interfaces only
[github.com/mohayonao/web-audio-mock-api](https://github.com/mohayonao/web-audio-mock-api "mohayonao/web-audio-mock-api: mock API which implements the Web Audio API's interfaces only")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Web Audio API의 Mock 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## Introduction | React Webpack cookbook
[christianalfoni.github.io/react-webpack-cookbook/](https://christianalfoni.github.io/react-webpack-cookbook/ "Introduction | React Webpack cookbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span> <span class="jser-tag">webpack</span></p>

webpack과 React의 빌드 환경 구축에 관해 작성돼 있는 GitBook입니다.

----

## Amazon.co.jp： 브라우저 핵, 웹 브러우저에서의 공격 수법과 방어 방법 총정리: Wade Alcorn, Christian Frichot, Michele Orru, 소노다 미치오, 하세가와 요스케, 니시무라 무네아키, 주식회사 프로시스템 LOC: 책(일본어 서적)
[www.amazon.co.jp/%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%8F%E3%83%83%E3%82%AF-Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%8B%E3%82%89%E3%81%AE%E6%94%BB%E6%92%83%E6%89%8B%E6%B3%95%E3%81%A8%E3%81%9D%E3%81%AE%E9%98%B2%E5%BE%A1%E6%B3%95%E7%B7%8F%E8%A6%A7-Wade-Alcorn/dp/479814343X](http://www.amazon.co.jp/%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%8F%E3%83%83%E3%82%AF-Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%8B%E3%82%89%E3%81%AE%E6%94%BB%E6%92%83%E6%89%8B%E6%B3%95%E3%81%A8%E3%81%9D%E3%81%AE%E9%98%B2%E5%BE%A1%E6%B3%95%E7%B7%8F%E8%A6%A7-Wade-Alcorn/dp/479814343X "Amazon.co.jp： ブラウザハック Webブラウザからの攻撃手法とその防御法総覧: Wade Alcorn, Christian Frichot, Michele Orru, 園田 道夫, はせがわ ようすけ, 西村 宗晃, 株式会社プロシステムエルオーシー: 本")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">book</span></p>

2016년 3월16일 출간 예정
공격자 관점에서 학습할 수 있는 브라우저/웹의 보안에 관한 서적입니다.

----
