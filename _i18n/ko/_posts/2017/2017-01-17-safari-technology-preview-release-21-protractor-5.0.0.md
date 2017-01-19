---
title: "2017-01-17 JS: Safari Technology Preview Release 21, Protractor 5.0.0"
author: azu
translator: U-Yeong Ju
layout: post
date : 2017-01-17T09:49
category: JSer
tags:
    - Safari
    - testing
    - E2E

---

JSer.info #314 - [Safari Technology Preview Release 21](https://webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/ "Safari Technology Preview Release 21")이 릴리즈됐습니다.

`<script type="module">`을 지원하며 ECMAScript modules를 이용할 수 있습니다.
 ECMAScript modules에 대한 것은 아래의 문서에 잘 정리돼 있으며 Safari 에서의 설정 방법도 소개돼 있으므로 함께 살펴보면 좋을 것 같습니다.

- [Native ECMAScript modules - the first overview](https://blog.hospodarets.com/native-ecmascript-modules-the-first-overview "Native ECMAScript modules - the first overview")

----

E2E 테스트 프레임워크 [Protractor](http://www.protractortest.org/ "Protractor") [5.0.0](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "5.0.0")이 릴리즈 됐습니다.

- [protractor/CHANGELOG.md at 5.0.0 · angular/protractor](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "protractor/CHANGELOG.md at 5.0.0 · angular/protractor")

[selenium-webdriver v3.x](https://github.com/SeleniumHQ/selenium/blob/master/javascript/node/selenium-webdriver/CHANGES.md#v300 "selenium-webdriver")로 업데이트 됐기 때문에 API 인터페이스도 함께 변경됐습니다.
또, 실행에 필요한 Node.js의 버전도 v6.9.x 이상으로 변경됐습니다.

----

## 공지

1월 15일에 JSer.info 6주년 기념 이벤트를 개최했습니다.
당일에 발표된 슬라이드 및 속기록 등은 아래 문서에 정리했으니 관심있는 분은 보시길 바랍니다.

- [JSer.info 6주년 기념 이벤트를 개최했습니다 - JSer.info](https://jser.info/2017/01/15/jser-info-6years/ "JSer.info 6주년 기념 이벤트를 개최했습니다 - JSer.info")(일본어)

----
<h1 class="site-genre">헤드라인</h1>

----

## Release v1.4.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v1.4.0](https://github.com/karma-runner/karma/releases/tag/v1.4.0 "Release v1.4.0 · karma-runner/karma")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma v1.4.0이 릴리즈됐습니다.
HTTP module을 설정하는 것으로 `node-http2` 등을 이용할 수 있고, 상수를 `karma.constants`로 export할 수 있게 되는 등 다양한 변경 사항이 있습니다.

----

## mobx/CHANGELOG.md at 3.0.0 · mobxjs/mobx
[github.com/mobxjs/mobx/blob/3.0.0/CHANGELOG.md](https://github.com/mobxjs/mobx/blob/3.0.0/CHANGELOG.md "mobx/CHANGELOG.md at 3.0.0 · mobxjs/mobx")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MobX 3이 릴리즈됐습니다.
각 타입에 대한 옵저버블을 생성할 수 있는 옵저버블 팩토리 메서드 추가, 전달 받은 객체를 clone 하도록 변경, 에러 핸들링의 개선 등이 이뤄졌습니다.

- [MobX 3.0.0의 변경 사항에 대해 - console.lealog();](http://lealog.hateblo.jp/entry/2017/01/11/140607 "MobX 3.0.0 MobX 3.0.0의 변경 사항에 대해 - console.lealog();")(일본어)
- [MobX 3 released: Unpeeling the onion – Medium](https://medium.com/@mweststrate/mobx-3-released-unpeeling-the-onion-ca877382f443 "MobX 3 released: Unpeeling the onion – Medium")

----

## Release Notes for Safari Technology Preview 21 | WebKit
[webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/](https://webkit.org/blog/7265/release-notes-for-safari-technology-preview-21/ "Release Notes for Safari Technology Preview 21 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">webkit</span> <span class="jser-tag">safari</span></p>

Safari Technology Preview Release 21이 릴리즈됐습니다.
Concurrent GC와 `<script type="module">` 활성화했고 `global`이 지원됐었지만 break the web으로 인해 backout 되는 등 다양한 변경 사항이 있습니다.

- [체인지 셋 210570 – WebKit](https://trac.webkit.org/changeset/210570 "체인지 셋 210570 – WebKit")
- [global breaks flickr.com · Issue #20 · tc39/proposal-global](https://github.com/tc39/proposal-global/issues/20 "global breaks flickr.com · Issue #20 · tc39/proposal-global")
- [Native ECMAScript modules - the first overview](https://blog.hospodarets.com/native-ecmascript-modules-the-first-overview "Native ECMAScript modules - the first overview")

----

## protractor/CHANGELOG.md at 5.0.0 · angular/protractor
[github.com/angular/protractor/blob/5.0.0/CHANGELOG.md](https://github.com/angular/protractor/blob/5.0.0/CHANGELOG.md "protractor/CHANGELOG.md at 5.0.0 · angular/protractor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

Protractor 5.0.0이 릴리즈됐습니다.
`selenium-webdriver` 3.0.x로 업데이트 하면서 API 인터페이스가 변경됐으며 알 수 없는 플러그는 에러를 발생 시키도록 변경 됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## TypeScript: the missing introduction
[toddmotto.com/typescript-the-missing-introduction](https://toddmotto.com/typescript-the-missing-introduction "TypeScript: the missing introduction")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

TypeScript라는 언어가 어떠한 구조로 동작하고 또 JavaScript와 비교해 어떠한 역할을 담당하고 있는지 등 개요 격의 이야기를 친절하게 설명하고 있습니다.

----

## Practical Redux · Mark&#x27;s Dev Blog
[blog.isquaredsoftware.com/series/practical-redux/](http://blog.isquaredsoftware.com/series/practical-redux/ "Practical Redux · Mark's Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

게임 관리 도구를 소재로 Redux에 관해 소개하는 연재 글입니다.
`Redux-ORM`을 사용한 모델 작성, Semantic-UI로 UI 작성, 디렉터리 구조, 디버깅 방법, 컴포넌트 리팩터링 방법 등을 다루고 있습니다.

----

## Side Effects in JS Promise chains – Medium
[medium.com/@gabrielcatalin/side-effects-in-js-promise-chains-7db50b6302f3](https://medium.com/@gabrielcatalin/side-effects-in-js-promise-chains-7db50b6302f3 "Side Effects in JS Promise chains – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Promise chain에서 사이드 이펙트가 있는 처리를 포함할 때 처리가 도중에 끊어져 버리는 문제에 관해 이야기합니다.
`passThrough()`와 같은 고차 함수를 준비하고 사이드 이펙트 관련 처리를 명시적으로 다뤄 버그를 줄일 수 있는 방법을 소개하고 있습니다

----

## TypedArray or DataView: Understanding byte order ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/01/typedarray-or-dataview-understanding-byte-order/](https://hacks.mozilla.org/2017/01/typedarray-or-dataview-understanding-byte-order/ "TypedArray or DataView: Understanding byte order ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

`ArrayBuffer`, `TypedArray`, `DataView`을 설명하는 글입니다.
`ArrayBuffer`가 바이너리 데이터 구조고 *view*로써 `TypedArray`와 `DataView`가 있다는 이야기입니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Web Components v1 - the next generation  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/01/webcomponents-org](https://developers.google.com/web/updates/2017/01/webcomponents-org "Web Components v1 - the next generation  |  Web  |  Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Web Components v1에 맞춰 webcomponents.org가 업데이트 됐습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## arqex/freezer: A tree data structure that emits events on updates, even if the modification is triggered by one of the leaves, making it easier to think in a reactive way.
[github.com/arqex/freezer](https://github.com/arqex/freezer "arqex/freezer: A tree data structure that emits events on updates, even if the modification is triggered by one of the leaves, making it easier to think in a reactive way.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable.js와 같은 Immutable한 데이터 구조를 다룰 수 있는 라이브러리입니다.
변경을 통지하는 이벤트 시스템을 제공하고 Immutable.js 보다 용량도 작습니다.

----

## Siema - Lightweight and simple carousel with no dependencies
[pawelgrzybek.com/siema/](https://pawelgrzybek.com/siema/ "Siema - Lightweight and simple carousel with no dependencies")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

의존 라이브러리 없이 구현한 카누젤(Carrousel) 라이브러리입니다.

----

## angus-c/just: A library of dependency-free utilities that do just do one thing.
[github.com/angus-c/just](https://github.com/angus-c/just "angus-c/just: A library of dependency-free utilities that do just do one thing.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

의존성 없는 작은 사이즈의 유틸리티 라이브러리 셋입니다
각각의 기능을 개별 모듈로써 설치해 사용할 수 있습니다.
각각의 `just-*` 모듈 간에서도 의존 관계가 없이 만들어져 있습니다.

- [Why I wrote Just. – Medium](https://medium.com/@angustweets/just-a12d54221f65 "Why I wrote Just. – Medium")
- [Just vs lodash · Issue #4 · angus-c/just](https://github.com/angus-c/just/issues/4 "Just vs lodash · Issue #4 · angus-c/just")

----

## yamafaktory/shrimpit: Shrimpit is a small CLI analysis tool for checking unused JavaScript, JSX &amp; Vue templates ES6 exports in your project.
[github.com/yamafaktory/shrimpit](https://github.com/yamafaktory/shrimpit "yamafaktory/shrimpit: Shrimpit is a small CLI analysis tool for checking unused JavaScript, JSX & Vue templates ES6 exports in your project.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

각 모듈의 import/export를 훑어 보면서 미사용 모듈을 출력해주는 CLI 도구입니다.

----

## katat/vbot: JSON based visual regression testing tool, particularly useful for SPA or complicated web app
[github.com/katat/vbot](https://github.com/katat/vbot "katat/vbot: JSON based visual regression testing tool, particularly useful for SPA or complicated web app")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span></p>

JSON 기반의 회귀(regression) 테스트 도구입니다.
JSON으로 시나리오를 작성하며 스크린샷으로 결과를 비교할 수 있습니다.

- [vbot - JSON based visual regression tester - Kata Tech Life](http://katat.github.io/2017/01/09/vbot/ "vbot - JSON based visual regression tester - Kata Tech Life")

----

## Landmarks browser extension
[matatk.agrip.org.uk/landmarks/](http://matatk.agrip.org.uk/landmarks/ "Landmarks browser extension")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">Extension</span></p>

WAI-ARIA의 landmark 네비게이션을 활성화하는 브라우저 확장 플러그인(extension)입니다.

----

## tsayen/dom-to-image: Generates an image from a DOM node using HTML5 canvas
[github.com/tsayen/dom-to-image](https://github.com/tsayen/dom-to-image "tsayen/dom-to-image: Generates an image from a DOM node using HTML5 canvas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">canvas</span> <span class="jser-tag">SVG</span> <span class="jser-tag">library</span></p>

SVG의 `<foreignObject>`를 사용해 HTML의 렌더링 결과를 Canvas를 경유해 사진으로 취득할 수 있는 라이브러리입니다.

- [Drawing DOM objects into a canvas - HTML | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Drawing_DOM_objects_into_a_canvas "Drawing DOM objects into a canvas - HTML | MDN")

----

## ModClean/modclean: Remove unwanted files and directories from your node_modules folder
[github.com/ModClean/modclean](https://github.com/ModClean/modclean "ModClean/modclean: Remove unwanted files and directories from your node\_modules folder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

node_modules에서 불필요한 파일을 삭제할 수 있는 도구입니다.

----
