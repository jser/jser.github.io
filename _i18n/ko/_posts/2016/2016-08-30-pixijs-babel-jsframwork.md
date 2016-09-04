---
title: "2016-08-30 JS: pixi.js 4.0.0, Babel 6.14.0, JS 프레임워크 앙케이트"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-08-30T09:40
category: JSer
tags:
    - Canvas
    - WebGL
    - game
    - Babel
    - framwork
    - survery

---

JSer.info #294 - WebGL과 Canvas를 사용한 2D 렌더링 엔진 pixi.js 4.0.0이 릴리즈됐습니다.

- [Release v4.0.0 · pixijs/pixi.js](https://github.com/pixijs/pixi.js/releases/tag/v4.0.0 "Release v4.0.0 · pixijs/pixi.js")

[PixiJS v4 Arrives](http://www.goodboydigital.com/pixi-js-v4/)에도 소개돼 있습니다만,
Multi texture renderering 지원, GPU GC 관리 기능 추가, WebGL 렌더 개선 등이 이뤄졌습니다.
또, 코어 부분을 [pixi-gl-core](https://github.com/pixijs/pixi-gl-core "pixi-gl-core")에 공개 했고, npm과 관련된 부분이 정리됐습니다.

현재 공개된 마이그레이션 가이드는 없지만 아래 이슈를 보아 곧 공개될 것으로 판단됩니다.

- [Migration guide v3->v4 · Issue #2867 · pixijs/pixi.js](https://github.com/pixijs/pixi.js/issues/2867 "Migration guide v3-&gt;v4 · Issue #2867 · pixijs/pixi.js")

이전 버그의 수정도 이뤄졌지만 아무래도 4.0 자체의 버그도 있을 것이므로 이러한 버그를 수정한 4.1 버전의 릴리즈가 예정돼 있습니다.

- [Issues · pixijs/pixi.js](https://github.com/pixijs/pixi.js/issues?q=is%3Aopen+is%3Aissue+milestone%3Av4.1 "Issues · pixijs/pixi.js")

----

Babel [6.14.0](https://github.com/babel/babel/releases/tag/v6.14.0 "6.14.0")이 릴리즈됐습니다.

- [6.14.0 Released · Babel](http://babeljs.io/blog/2016/08/24/6.14.0 "6.14.0 Released · Babel")

`latest`와 `es2017`라는 새로운 preset이 추가됐습니다.
`latest` preset은 ES2015+(ES2015, ES2016, ES2017)가 포함돼 있습니다. 즉, ECMAScript의 새로운 버전이 추가된 preset이라고 볼 수 있습니다.

----

[The State Of JavaScript: Front-End Frameworks – Medium](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")에는 자바스크립트의 프레임워크에 관한 앙케이트 결과가 공개돼 있습니다.
[The State Of JavaScript](http://stateofjs.com/ "The State Of JavaScript")에서 실시한 앙케이트로 것으로 유명한 프레임워크/라이브러리에 대해 흥미 및 만족도에 관해 조사한 내용입니다.


앙케이트 대상된 프레임워크/라이브러리는 아래 6개 입니다.

- React
- Angular
- Angular 2
- Ember
- Vue
- Backbone

해당 글에는 앙케이트의 결과도 공개돼있습니다.

조사 결과만 간단히 소개해 드리자면 다음과 같습니다(앙케이트 대상인 프레임워크/라이브러리는 Vue를 제외하면 대부분의 사람이 알고 있는 것입니다).

- 배우고 싶은 것: React -> Vue -> Angular2
- 만족도가 높은 것: React -> Vue -> Angular2

자세한 내용은 [The State Of JavaScript: Front-End Frameworks – Medium](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")을 참고해주세요.

----
<h1 class="site-genre">헤드라인</h1>

----

## Release v4.0.0 · pixijs/pixi.js
[github.com/pixijs/pixi.js/releases/tag/v4.0.0](https://github.com/pixijs/pixi.js/releases/tag/v4.0.0 "Release v4.0.0 · pixijs/pixi.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

pixi.js 4.0.0이 릴리즈됐습니다.
Multi texture renderering 지원, GPU GC 관리 기능 추가, WebGL 렌더 개선, npm 패키지 공개 등이 이뤄졌습니다.

- [PixiJS v4 Arrives - Goodboy™ — Goodboy™](http://www.goodboydigital.com/pixi-js-v4/ "PixiJS v4 Arrives - Goodboy™ — Goodboy™")

----

## Release v6.14.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.14.0](https://github.com/babel/babel/releases/tag/v6.14.0 "Release v6.14.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.14.0이 릴리즈됐습니다.
`es2017` preset과 ES2015+를 지원하는 `latest` preset이 추가됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## The State Of JavaScript: Front-End Frameworks – Medium
[medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510](https://medium.com/@sachagreif/the-state-of-javascript-front-end-frameworks-1a2d8a61510 "The State Of JavaScript: Front-End Frameworks – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

자바스크립트 프레임워크에 관한 앙케이트 결과가 공개됐습니다.
각 프레임워크에 대한 인지도는 Vue를 제외하면 거의 비슷합니다.
결과만 간단히 소개해 드리자면 다음과 같습니다.

배워보고 싶은 것: React -> Vue -> Angular2
만족도가 높은 것: React -> Vue -> Angular2

- [The State Of JavaScript](http://stateofjs.com/ "The State Of JavaScript")

----

## Enable Chrome Accessibility Experiment
[gist.github.com/marcysutton/0a42f815878c159517a55e6652e3b23a](https://gist.github.com/marcysutton/0a42f815878c159517a55e6652e3b23a "Enable Chrome Accessibility Experiment")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">debug</span></p>

크롬에서 시험적으로 지원하는 Accessibility inspector를 활성화하는 방법을 소개합니다.
특정 요소에 대응한 WAI-ARIA의 정보를 Elements 패널을 통해 볼 수 있습니다.

----

## Demythstifying Web Components – Back Alley Coder
[www.backalleycoder.com/2016/08/26/demythstifying-web-components/](http://www.backalleycoder.com/2016/08/26/demythstifying-web-components/ "Demythstifying Web Components – Back Alley Coder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Web Components에 대한 흔히 있는 오해에 관해 작성돼 있습니다.

----

## How To Use WebPageTest and its API | CSS-Tricks
[css-tricks.com/use-webpagetest-api/](https://css-tricks.com/use-webpagetest-api/ "How To Use WebPageTest and its API | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">performance</span> <span class="jser-tag">API</span></p>

WebPageTest API를 사용한 메트릭스에 관해 이야기합니다.

----

## Three Ways to Test Angular 2 Components – Angular 2
[vsavkin.com/three-ways-to-test-angular-2-components-dcea8e90bd8d](https://vsavkin.com/three-ways-to-test-angular-2-components-dcea8e90bd8d "Three Ways to Test Angular 2 Components – Angular 2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span></p>

AngularJS 2의 컴포넌트를 테스트하는 방법에 관해 작성돼 있습니다.

----

## You SHOULD Learn Vanilla JavaScript Before JS Frameworks - Snipcart
[snipcart.com/blog/learn-vanilla-javascript-before-using-js-frameworks](https://snipcart.com/blog/learn-vanilla-javascript-before-using-js-frameworks "You SHOULD Learn Vanilla JavaScript Before JS Frameworks - Snipcart")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">thought</span></p>

프레임워크를 배우기 전에 자바스크립트를 먼저 학습해야 한다고 주장하는 글입니다.

----

## jsdoc-to-assert를 사용해보다 - 아카베코마이루(일본어)
[akabeko.me/blog/2016/08/jsdoc-to-assert/](http://akabeko.me/blog/2016/08/jsdoc-to-assert/ "jsdoc-to-assert를 시험해보다 - 아카베코마이루(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

jsdoc-to-assert를 사용해 런타임 assert를 도입하는 것에 관해 작성돼 있습니다.

----

## 타입 정의 기반의 어썰션 라이브러리 types-assert를 만들다 - Qiita(일본어)
[qiita.com/KeitaMoromizato/items/e49185a0cd03c6cb8b3a](http://qiita.com/KeitaMoromizato/items/e49185a0cd03c6cb8b3a "型定義ベースのアサーションライブラリ types-assert を書いた - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

TypeScript의 타입 정의 파일을 사용한 assertion 라이브러리를 소개합니다.

- [KeitaMoromizato/types-assert: type-assert is dynamic type assertion library](https://github.com/KeitaMoromizato/types-assert "KeitaMoromizato/types-assert: type-assert is dynamic type assertion library")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## From MVC to Flux - JS Monthly London - YouTube
[www.youtube.com/watch?v=p8tqhf5qKOI](https://www.youtube.com/watch?v=p8tqhf5qKOI "From MVC to Flux - JS Monthly London - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span></p>

다시금 Flux는 어떤 컨셉인지 또, Flux와 동일한 코어 컨셉을 가진 Redux를 소개하는 영상입니다.

- [From MVC to Flux - Pusher Blog](https://blog.pusher.com/from-mvc-to-flux/ "From MVC to Flux - Pusher Blog")

----

## thejameskyle/itsy-bitsy-data-structures: All the things you didn&#x27;t know you wanted to know about data structures
[github.com/thejameskyle/itsy-bitsy-data-structures](https://github.com/thejameskyle/itsy-bitsy-data-structures "thejameskyle/itsy-bitsy-data-structures: All the things you didn't know you wanted to know about data structures")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">알고리즘</span> <span class="jser-tag">document</span></p>

리스트, 해쉬테이블, 스택 등의 데이터구조를 구현한 자바스크립트 코드와 해설을 포함하고 있는 저장소입니다.
각각의 탐색 비용이나 특징 등에 대한 해설이 주석으로 작성돼 있습니다.

- [React Rally Day 2 - YouTube](https://www.youtube.com/watch?v=nI0cQ-2YR1I "React Rally Day 2 - YouTube")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## SAM - State | Action | Model
[sam.js.org/](http://sam.js.org/ "SAM - State | Action | Model")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">설계</span> <span class="jser-tag">디자인패턴</span></p>

SAM(State-Action-Model)를 소개하는 문서 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## babel/babel-minify: Babel preset for minification (Alpha)
[github.com/babel/babel-minify](https://github.com/babel/babel-minify "babel/babel-minify: Babel preset for minification (Alpha)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

Babel의 minify plugin preset 입니다.

----

## google/closure-compiler-js: Package for the JS version of closure-compiler for use via npm
[github.com/google/closure-compiler-js](https://github.com/google/closure-compiler-js "google/closure-compiler-js: Package for the JS version of closure-compiler for use via npm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Closure Compiler의 일부 기능을 사용할 수 있는 도구입니다. 자바스크립트로 컴파일된 후의 파일을 포함(의존)하고 있어 자바를 필요로 하지 않습니다.

----

## reactjs/react-docgen: A CLI and toolbox to extract information from React component files for documentation generation purposes.
[github.com/reactjs/react-docgen](https://github.com/reactjs/react-docgen "reactjs/react-docgen: A CLI and toolbox to extract information from React component files for documentation generation purposes.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

React의 propTypes 등을 파싱하여 AST로 취득할 수 있는 라이브러리/CLI 도구입니다.

----

## pakastin/redom: Tiny DOM library
[github.com/pakastin/redom](https://github.com/pakastin/redom "pakastin/redom: Tiny DOM library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

DOM API를 사용한 작은 사이즈의 컴포넌트 라이브러리입니다.

----

## nolanlawson/slow-deps: 🐌 Measure which dependencies in a project are slowest to npm install
[github.com/nolanlawson/slow-deps](https://github.com/nolanlawson/slow-deps "nolanlawson/slow-deps: 🐌 Measure which dependencies in a project are slowest to npm install")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

의존하는 각 npm 모듈의 설치 시간과 파일 크기를 측정할 수 있는 도구 입니다.

----
<h1 class="site-genre">도서</h1>

----

## Fluent JavaScript | PACKT Books
[www.packtpub.com/web-development/fluent-javascript](https://www.packtpub.com/web-development/fluent-javascript "Fluent JavaScript | PACKT Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2017년 4월 6일 출간 예정인 자바스크립트 도서입니다.

- [Amazon | Fluent JavaScript \[Kindle edition\] by Callum Rimmer, Lucian Lature | Languages &amp;amp; Tools | Kindleストア](https://www.amazon.co.jp/dp/B01F7HCB0C/ "Amazon | Fluent JavaScript \[Kindle edition\] by Callum Rimmer, Lucian Lature | Languages &amp;amp; Tools | Kindleストア")

----
