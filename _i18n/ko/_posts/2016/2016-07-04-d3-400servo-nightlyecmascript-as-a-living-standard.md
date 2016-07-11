---
title: "2016-07-04 JS: D3 4.0.0, Servo Nightly, ECMAScript as a Living Standard"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-07-04T22:32
category: JSer
tags:
    - D3
    - SVG
    - Servo
    - browser
    - ECMAScript

---

JSer.info #286 - D3.js 4.0.0가 릴리즈됐습니다.

- [Release v4.0.0 · d3/d3](https://github.com/d3/d3/releases/tag/v4.0.0 "Release v4.0.0 · d3/d3")
- [d3/CHANGES.md at master · d3/d3](https://github.com/d3/d3/blob/master/CHANGES.md "d3/CHANGES.md at master · d3/d3")

많은 부분이 큰 폭으로 수정됐고, 각각의 기능이 개별 모듈로 나뉘어졌습니다.
자세한 내용은 [CHANGES.md](https://github.com/d3/d3/blob/master/CHANGES.md)를 참고하세요.

----

Mozilla가 개발하고 있는 렌더링 엔진인 [Servo](https://servo.org/ "Servo")를 기반으로한 Nightly 빌드 버전이 공개됐습니다.

- [Servo Nightly Builds Available](https://blog.servo.org/2016/06/30/servo-nightlies/ "Servo Nightly Builds Available")

브라우저의 UI는 HTML 기반으로, [browserhtml](https://github.com/browserhtml/browserhtml "browserhtml")으로 개발돼 있으며, 브라우저 애플리케이션으로써 실행하고 사용해 볼 수 있습니다.

----

[ECMAScript as a Living Standard](http://azu.github.io/slide/2016/node-es/ecmascript.html "ECMAScript as a Living Standard")(일본어)에는 ECMAScript의 사양 책정 프로세스가 일반적인 소프트웨어 개발 프로세스와 크게 다르지 않다는 이야기가 작성돼 있습니다.
ES2015부터는 많은 의제나 커밋이 Github 상에서 행해지고 있기 때문에, OSS(Open Source Software) 프로젝트와 익숙한 흐름으로 진행되고 있음을 알 수 있습니다.
또한, 왜 매년 릴리즈하는 프로세스를 프로젝트에 도입했는지 등에 관해서도 이야기합니다.

- [Node학교, 21교시에서 ECMAScript as a Living Standard 라는 주제로 발표했다 | Web Scratch](http://efcl.info/2016/06/29/node-ecmascript/ "Node학교, 21교시에서 ECMAScript as a Living Standard 라는 주제로 발표했다 | Web Scratch")(일본어)

이러한 프로세스로 인해 빠르게 변경하는 사양에 대응하는 JavaScript 입문서가 있으면 좋을 것 같아 현재 작성 중에 있습니다.

- [asciidwango/js-primer: JavaScript 입문서](https://github.com/asciidwango/js-primer "asciidwango/js-primer: JavaScript 입문서")(일본어)

----
<h1 class="site-genre">헤드라인</h1>

----

## Release Cycle Diversity · cyclejs/core
[github.com/cyclejs/core/releases/tag/v7.0.0](https://github.com/cyclejs/core/releases/tag/v7.0.0 "Release Cycle Diversity · cyclejs/core")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cycle.js 7.0.0가 릴리즈됐습니다.
xstream을 선택해 사용할 수 있도록 변경됐고, TypeScript를 완벽히 지원하고자 재작성했으며, V-DOM으로 snabbdom을 사용하도록 변경됐습니다.

- [snabbdom](https://github.com/paldepind/snabbdom/ "snabbdom")

----

## Release v15.2.0 · facebook/react
[github.com/facebook/react/releases/tag/v15.2.0](https://github.com/facebook/react/releases/tag/v15.2.0 "Release v15.2.0 · facebook/react")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 15.2.0이 릴리즈됐습니다.
에러 코드가 추가됐으며 로그로 제공되는 URL을 통해 자세한 내용을 볼 수 있습니다. 또, warning 메시지에 컴포넌트 스택 정보가 추가됐으며, 새로운 PropType인 `React.PropTypes.symbol`이 추가됐습니다.

----

## Release 2.0.0 · sweet-js/sweet.js
[github.com/sweet-js/sweet.js/releases/tag/v2.0.0](https://github.com/sweet-js/sweet.js/releases/tag/v2.0.0 "Release 2.0.0 · sweet-js/sweet.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript로 매크로를 다룰 수 있는 sweet.js 2.0.0이 릴리즈됐습니다.
context API가 변경됐습니다.

----

## Release v4.0.0 · d3/d3
[github.com/d3/d3/releases/tag/v4.0.0](https://github.com/d3/d3/releases/tag/v4.0.0 "Release v4.0.0 · d3/d3")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span></p>

D3.js 4.0.0이 릴리즈됐습니다.
`d3-scale`이나 `d3-time` 처럼 각각의 기능이 모듈로 분할 됐고, npm 패키지로 개별로 설치하여 사용할 수 있습니다.
대부분 기능 추가나 수정이 이뤄졌습니다.

- [d3/CHANGES.md at master · d3/d3](https://github.com/d3/d3/blob/master/CHANGES.md "d3/CHANGES.md at master · d3/d3")

----

## ESLint v3.0.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/07/eslint-v3.0.0-released](http://eslint.org/blog/2016/07/eslint-v3.0.0-released "ESLint v3.0.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 3.0.0이 릴리즈됐습니다.
`eslint:recommended`가 업데이트 됐고, 설정 파일 또는 설정을 지정하지 않은 경우엔 경고가 발생하도록 변경됐습니다. 또, Node.js 0.12의 지원을 종류하는 등 다양한 변경 사항이 있습니다.

- [ESLint v3.0.0 - Qiita](http://qiita.com/mysticatea/items/9c8a8b1219d5f94441e8 "ESLint v3.0.0 - Qiita")(일본어)

----
<h1 class="site-genre">아티클</h1>

----

## Servo Nightly Builds Available
[blog.servo.org/2016/06/30/servo-nightlies/](https://blog.servo.org/2016/06/30/servo-nightlies/ "Servo Nightly Builds Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Mozilla</span></p>

Mozilla가 개발하고 있는 렌더링 엔진 Servo의 Developer Preview 버전이 공개됐습니다.

----

## How to Upgrade a Node Module The Right Way - Jama Software
[www.jamasoftware.com/blog/upgrade-node-module-right-way/](http://www.jamasoftware.com/blog/upgrade-node-module-right-way/ "How to Upgrade a Node Module The Right Way - Jama Software")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">webpack</span></p>

의존 모듈의 비호환성 업데이트를 어떻게 대응하여 갱신하는지 react-router를 예로 소개합니다.
webpack의 alias를 사용해 Feature Flag를 만들고, 플래그를 전환하면서 신버전과 구버전을 모두 사용하는 방법이 작성돼 있습니다.

----

## Intersection Observer를 이용한 요소 출력 감지 최적화 | blog.jxck.io(일본어)
[blog.jxck.io/entries/2016-06-25/intersection-observer.html](https://blog.jxck.io/entries/2016-06-25/intersection-observer.html "Intersection Observer を用いた要素出現検出の最適化 | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span></p>

Intersection Observer의 사용법과 기존 방식과 다른 점을 소개합니다.
스크롤의 량이나 요소의 출력에 따른 처리 등을 이야기합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## ECMAScript as a Living Standard
[azu.github.io/slide/2016/node-es/ecmascript.html](http://azu.github.io/slide/2016/node-es/ecmascript.html "ECMAScript as a Living Standard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">슬라이드</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

ECMAScript 사양 책정의 프로세스를 이해하고 나아가 ECMAScirpt와 관련된 정보를 보는 방법을 소개합니다.
ES2015는 매년 릴리즈를 목표로 하는 사양이며 부족한 부분에 관해서는 의논을 진행해 결정해 나갑니다.

- [Node학교, 21교시에서 ECMAScript as a Living Standard 라는 주제로 발표했다 | Web Scratch](http://efcl.info/2016/06/29/node-ecmascript/ "Node학교, 21교시에서 ECMAScript as a Living Standard 라는 주제로 발표했다 | Web Scratch")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## holyjs/holyjs: HolyJS - NodeJS Server Project Starter
[github.com/holyjs/holyjs](https://github.com/holyjs/holyjs "holyjs/holyjs: HolyJS - NodeJS Server Project Starter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">서버</span> <span class="jser-tag">template</span></p>

Node.js의 서버사이드 프로젝트 템플릿입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## juliangarnier/anime: Javascript Animation Engine
[github.com/juliangarnier/anime](https://github.com/juliangarnier/anime "juliangarnier/anime: Javascript Animation Engine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

CSS 애니메이션을 조작하는 경량 라이브러리입니다.

----

## planttheidea/vidz: A zero-dependency, framework-agnostic video implementation
[github.com/planttheidea/vidz](https://github.com/planttheidea/vidz "planttheidea/vidz: A zero-dependency, framework-agnostic video implementation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">영상</span> <span class="jser-tag">library</span></p>

Video 요소에서 로드 시점이나 이벤트 핸들링 등을 다룰 수 있도록 하는 라이브러리입니다.

----

## planttheidea/crio: Immutable objects and arrays in a natural way
[github.com/planttheidea/crio](https://github.com/planttheidea/crio "planttheidea/crio: Immutable objects and arrays in a natural way")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable 버전의 Array와 Object를 제공하는 라이브러리입니다.
Mutable로 사용하고 싶은 경우엔 네이티브 구현체로 조작하고 랩핑하거나, `.mutable(array =>{})` 메서드를 사용할 수 있습니다.

----

## leebyron/iterall: Minimal zero-dependency utilities for using Iterables in all JavaScript environments.
[github.com/leebyron/iterall](https://github.com/leebyron/iterall "leebyron/iterall: Minimal zero-dependency utilities for using Iterables in all JavaScript environments.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Array나 Array-like한 데이터를 `forEach`로 iterable하게 처리하기 위한 라이브러리입니다.

----

## ejs - Readable JavaScript Errors
[i-break-codes.github.io/ejs/](https://i-break-codes.github.io/ejs/ "ejs - Readable JavaScript Errors")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">debug</span></p>

`window.onerror`를 이용해 JavaScript 에러의 출력 형태를 변경하고 콘솔에 출력해주는 라이브러리입니다.

----

## caiogondim/fast-memoize.js: Fastest possible memoization library
[github.com/caiogondim/fast-memoize.js](https://github.com/caiogondim/fast-memoize.js "caiogondim/fast-memoize.js: Fastest possible memoization library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

메모이제이션 라이브러리입니다.

----

## gcanti/babel-plugin-tcomb: Babel plugin for static and runtime type checking using Flow and tcomb
[github.com/gcanti/babel-plugin-tcomb](https://github.com/gcanti/babel-plugin-tcomb "gcanti/babel-plugin-tcomb: Babel plugin for static and runtime type checking using Flow and tcomb")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

FlowType의 타입을 런타임 상에서 동작하는 assert로 변환하는 Babel 플러그인입니다. tcomb를 사용해 구현돼 있습니다. 

----
<h1 class="site-genre">도서</h1>

----

## Modular JS: Practical ES6 - O&#x27;Reilly Media
[shop.oreilly.com/product/0636920047124.do](http://shop.oreilly.com/product/0636920047124.do "Modular JS: Practical ES6 - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

2016년 8월 발매 예정인 ES6에 관한 도서입니다.

----
