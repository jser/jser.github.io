---
title: "2016-04-18 JS: JSCS 3.0와 ESLint의 합병, SVG 아이콘"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-04-18T19:42
category: JSer
tags:
    - JSCS
    - ESLint
    - SVG
    - CSS

---

JSer.info #275 - JavaScript 코드 스타일 검증 도구인 JSCS 3.0이 릴리즈됐습니다.

- [Release 3.0.0 · jscs-dev/node-jscs](https://github.com/jscs-dev/node-jscs/releases/tag/v3.0.0 "Release 3.0.0 · jscs-dev/node-jscs")

플러그인 개발에 영향(비호환성)이 있는 변경 사항이 있고, 그 외에 `yandex` preset의 삭제, 규칙의 추가 등이 이뤄졌습니다.

또, JSCS는 3.x으로 신규 개발을 종료하고, JSCS 팀은 ESLint에 합류하게 됐습니다.

- [JSCS — end of the line — Medium](https://medium.com/@markelog/jscs-end-of-the-line-bc9bf0b3fdb2)
- [Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")

향후 삼개월을 목표로 JSCS의 버그 수정 등도 종료하고, 그 사이에 [ESLint에 JSCS 호환 및 이전 지원](https://github.com/eslint/eslint/milestones/JSCS%20Compatibility)을 준비해나갈 예정이라고 합니다.
(때문에, JSCS에서 ESLint로 이전이 어느정도 완료되는 시점은 천천히 기다리는 편이 좋을 것 같습니다)

JSCS 팀이 ESLint에 합류한 이유로는 커뮤니티/Issue의 관리 비용이나 [CST](https://github.com/cst/cst "CST") 개발에 좀더 집중하고 싶었다고 말하고 있습니다.

- [JSCS, CST и новое начало / Хабрахабр](https://habrahabr.ru/post/281635/ "JSCS, CST и новое начало / Хабрахабр")

또, 같은 문제를 해결하는 도구이기도 하고 ESLint가 향후 AutoFix 기능을 개선하고자 하는 것도 하나의 이유일 것 같습니다.

- [Fixing autofix · Issue #5329 · eslint/eslint](https://github.com/eslint/eslint/issues/5329 "Fixing autofix · Issue #5329 · eslint/eslint")


-----

[How to work with SVG icons](http://fvsch.com/code/svg-icons/how-to/ "How to work with SVG icons")에는 SVG 아이콘에 관해 꽤 자세하게 설명돼 있습니다.

SVG sprite의 구조와 만드는 법, 브라우저 간의 동작 차이, CSS에서 SVG의 스타일을 변경하는 방법 등 실용적인 내용이 작성돼 있어서 재미있습니다.
또, 인라인 SVG와 외부 리소스 SVG의 동작 차이나 브라우저의 동작 방식의 문제 등 실제로 사용하면 겪게되는 부분도 다루고 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Notes for Safari Technology Preview 2 | WebKit
[webkit.org/blog/6098/release-notes-for-safari-technology-preview-release-2/](https://webkit.org/blog/6098/release-notes-for-safari-technology-preview-release-2/ "Release Notes for Safari Technology Preview 2 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 2가 릴리즈됐습니다.
`String#padStart`/`String#padEnd`가 추가됐고, `for (var i = 20 in b){ }` 문법 사용 시 에러가 발생합니다.
CSS media query에서 `color-gamut`을 대응하고, TP1에서 잘못 공개한 Fetch API를 기본적으로 Disabled 시켰습니다. 또, Web Inspector도 개선됐습니다.

----

## ESLint v2.8.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/04/eslint-v2.8.0-released](http://eslint.org/blog/2016/04/eslint-v2.8.0-released "ESLint v2.8.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.8.0이 릴리즈됐습니다.

- [ESLint v2.8.0 - Qiita](http://qiita.com/mysticatea/items/8e7ca6f6ae402a494a6b "ESLint v2.8.0 - Qiita")

----

## Release 3.0.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v3.0.0](https://github.com/jscs-dev/node-jscs/releases/tag/v3.0.0 "Release 3.0.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS 3.0.0이 릴리즈됐습니다.

----

## Jest 11.0 · Jest
[facebook.github.io/jest/blog/2016/04/12/jest-11.html](http://facebook.github.io/jest/blog/2016/04/12/jest-11.html "Jest 11.0 · Jest")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 11.0이 릴리즈됐습니다.
0.10에서 11.0로의 메이저 업데이트입니다.

----

## Release v0.23.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.23.0](https://github.com/facebook/flow/releases/tag/v0.23.0 "Release v0.23.0 · facebook/flow")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

Flow v0.23.0이 릴리즈됐습니다.
`flow init`로`.flowconfig`을 만들때 사용할 수 있는 옵션이 추가됐, `.flowconfig` 파일에 주석을 작성할 수 있게 되는 등 여러가지 변경 사항이 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/04/welcoming-jscs-to-eslint](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ESLint</span></p>

JSCS 3.0.0로 신규 개발을 종료하고 3개월을 목표로 지원도 종료한다고 합니다.
JSCS팀은 ESLint에 합류하고 ESLint의 Autofix를 위해 필요한 CST 개발에 집중합니다.
ESLint 측은 JSCS를 이전/호환 지원을 예정하고 있습니다.

- [Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2016/04/welcoming-jscs-to-eslint "Welcoming JSCS To ESLint - ESLint - Pluggable JavaScript linter")
- [JSCS, CST и новое начало / Хабрахабр](https://habrahabr.ru/post/281635/ "JSCS, CST и новое начало / Хабрахабр")

----

## How to work with SVG icons
[fvsch.com/code/svg-icons/how-to/](http://fvsch.com/code/svg-icons/how-to/ "How to work with SVG icons")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">사진</span></p>

SVG 아이콘에 관해 실용적으로 소개하고 있습니다.
CSS 스프라이트 처럼 SVG 스프라이트를 만드는 방법, 인라인 SVG와 외부 SVG를 로드하는 차이와 대응 브라우저 및 polyfill 등에 관해 작성돼 있습니다.
또, CSS로 SVG 스타일을 변경하는 방법이나 Safari의 문제 등 꽤 자세하게 작성돼 있습니다.

----

## CSS @apply rule (native CSS mixins)
[blog.gospodarets.com/css\_apply\_rule](https://blog.gospodarets.com/css_apply_rule "CSS @apply rule (native CSS mixins)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

CSS의 `@aaply` Proposal 관한 소개 글입니다.

----

## power-assert + babel as a development tool | Web Scratch(일본어)
[efcl.info/2016/04/14/espower-babel-is-deprecated/](http://efcl.info/2016/04/14/espower-babel-is-deprecated/ "power-assert + babel as a development tool | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

power-assert+babel+mocha의 구성에 관해 이야기합니다.
디버깅을 위한 자세한 정보를 제공하는 assert, 프로덕프 빌드시 assert를 제거하는 방법, JSDoc에서 런타임으로 assert 하여 검증하는 방법 등에 관해 작성돼 있습니다.

----

## christianalfoni - RxJs the smartest dumbest tool ever
[www.christianalfoni.com/articles/2016\_03\_31\_RxJs-the-smartest-dumbest-tool-ever](http://www.christianalfoni.com/articles/2016_03_31_RxJs-the-smartest-dumbest-tool-ever "christianalfoni - RxJs the smartest dumbest tool ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">tutorial</span></p>

RxJS로 어떤 문제를 해결할 수 있는지 작성돼 있습니다.

----

## Scalable Single-Page Application Architecture – Minko Gechev&#x27;s blog
[blog.mgechev.com/2016/04/10/scalable-javascript-single-page-app-angular2-application-architecture/](http://blog.mgechev.com/2016/04/10/scalable-javascript-single-page-app-angular2-application-architecture/ "Scalable Single-Page Application Architecture – Minko Gechev's blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">설계</span></p>

AngularJS2 + RxJS로 시도한 CQRS + EventSourcing 적인 접근법. DI로 의존 해결, 레이어간 분리나 async service의 동작 방식이 흥미롭습니다.

----

## Immutability is not enough
[codewords.recurse.com/issues/six/immutability-is-not-enough](https://codewords.recurse.com/issues/six/immutability-is-not-enough "Immutability is not enough")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">설계</span></p>

Immutable.js를 사용한 State의 갱신에 관해 작성돼 있습니다.
단순히 State를 immutable로 해서 단순하게 함수를 순차적으로 적용할 때 발생하는 "이전 State를 참조하지 않는 문제"와 "lost update" 문제에 관해 이야기합니다.

----

## react-storybook을 이용한 React 컴포넌트 해설 - Hatena Developer Blog(일본어)
[developer.hatenastaff.com/entry/2016/04/14/150000](http://developer.hatenastaff.com/entry/2016/04/14/150000 "react-storybookを用いたReactコンポーネント開発 - Hatena Developer Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

React Component를 스토리로 작성해 확인하며 개발할 수 있는 도구인 react-storybook에 관해 소개합니다.

----

## Leveling Up with React: Redux | CSS-Tricks
[css-tricks.com/learning-react-redux/](https://css-tricks.com/learning-react-redux/ "Leveling Up with React: Redux | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Redux에 의한 데이터 플로우 등을 알기 쉽게 설명하는 튜토리얼입니다.

----

## CoffeeScript를 ES2015(ES6)로 실행해봤다 - 페파보테크블로그(일본어)
[tech.pepabo.com/2016/04/13/coffeescript-transpiled-es/](http://tech.pepabo.com/2016/04/13/coffeescript-transpiled-es/ "CoffeeScript를 ES2015(ES6)로 실행해봤다 - 페파보테크블로그")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

CoffeeScript를 decaf를 사용해 변환하고 JavaScript로 실행하는 방법을 소개합니다.

----

## 【의역】Webpack의 혼란스러운 부분 - Qiita(일본어)
[qiita.com/chuck0523/items/caacbf4137642cb175ec](http://qiita.com/chuck0523/items/caacbf4137642cb175ec "【意訳】Webpackの混乱ポイント - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">번역</span></p>

"Webpack — The Confusing Parts"의 일본어 번역 글입니다.
webpack의 설정에서 혼란에 빠지기 쉬운 부분에 관해 정리돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Let&#x27;s Learn ES6
[letslearnes6.com/](http://letslearnes6.com/ "Let's Learn ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">영상 </span></p>

ES6를 학습할 수있는 강의 영상 사이트

- [Let&#x27;s Learn ES6 - YouTube](https://www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX "Let&#x27;s Learn ES6 - YouTube")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Makeitopen.com - Open Source Learning
[makeitopen.com/](http://makeitopen.com/ "Makeitopen.com - Open Source Learning")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React Native로 F8 앱을 어떻게 만들었는지 소개합니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Rich Harris / buble · GitLab
[gitlab.com/Rich-Harris/buble](https://gitlab.com/Rich-Harris/buble "Rich Harris / buble · GitLab")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

Babel과 같은 ES2015 코드를 ES5로 변환하는 도구입니다.
Babel 처럼 확장성이나 사양을 중요시하는 것 보다 변환 속도를 중요시 하여 개발됐습니다.

----

## thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.
[github.com/thejameskyle/babel-react-optimize](https://github.com/thejameskyle/babel-react-optimize "thejameskyle/babel-react-optimize: A Babel preset and plugins for optimizing React code.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

React(JSX)를 최적화하는 Babel 플러그인입니다.

----

## Our Justified Layout Goes Open Source | code.flickr.com
[code.flickr.net/2016/04/05/our-justified-layout-goes-open-source/](http://code.flickr.net/2016/04/05/our-justified-layout-goes-open-source/ "Our Justified Layout Goes Open Source | code.flickr.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

Flicker의 사진을 타일 느낌으로 나열하는 UI 라이브러리입니다.

----
