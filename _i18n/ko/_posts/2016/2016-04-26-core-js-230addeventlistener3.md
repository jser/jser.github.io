---
title: "2016-04-26 JS: core-js 2.3.0, addEventListener 세번째 인수, 웹과 관련된 사양 번역 글"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-04-26T20:25
category: JSer
tags:
    - ECMAScript
    - DOM
    - W3C
    - WHATWG
    - Spec
    - Translation

---

JSer.info #276 - [Babel의 runtime](https://babeljs.io/docs/plugins/transform-runtime/)에서 사용하고 있는 core-js 2.3.0이 릴리즈됐습니다.

- [Release 2.3.0 - 2016.04.24 · zloirock/core-js](https://github.com/zloirock/core-js/releases/tag/v2.3.0 "Release 2.3.0 - 2016.04.24 · zloirock/core-js")

대부분 Proposal의 Stage 이동이 주된 내용으로, 3월에 있었던 TC39의 미팅 내용을 반영한 것 입니다.

- [tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/tree/master/es7/2016-03 "tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes")

----

[DOM Listener: capture, passive, and once](https://www.webreflection.co.uk/blog/2016/04/17/new-dom4-standards "DOM Listener: capture, passive, and once")에는 최근 WHATWG HTML에 추가된 `node.addEventListener(type, handler, {capture: true}`의 세번째 인수 인 `EventListenerOptions`가 설명돼 있습니다.

구체적인 사양이나 구현 상황에 관해서는 아래를 문서를 참고하시길 바랍니다.

- [addEventListener/removeEventListener EventListenerOptions API - Chrome Platform Status](https://www.chromestatus.com/feature/5718574840676352 "addEventListener/removeEventListener EventListenerOptions API - Chrome Platform Status")
- [WICG/EventListenerOptions: An extension to the DOM event pattern to allow authors to disable support for preventDefault](https://github.com/WICG/EventListenerOptions "WICG/EventListenerOptions: An extension to the DOM event pattern to allow authors to disable support for preventDefault")

또, 아직 의논 중인 사양이지만 Chrome에서 일부 구현돼 있어 사용해 볼 수 있습니다.

- [Issue 543685 - chromium - Implement addEventListener(type, listener, EventListenerOptions); - Monorail](https://bugs.chromium.org/p/chromium/issues/detail?id=543685 "Issue 543685 - chromium - Implement addEventListener(type, listener, EventListenerOptions); - Monorail")

----

위 `addEventListener`와 같이 DOM과 관련한 API는 대개 WHATWG 측에 추가돼 있습니다.

- [WHATWG와 W3C에 있는 여러 사양 - Unreviewed](http://takenspc.hatenablog.com/entry/2015/12/03/235927 "WHATWG와 W3C에 있는 여러 사양 - Unreviewed")(일본어)
- 지금까지도 HTML의 사양에 관해서는 [여러가지 잡음이](http://momdo.hatenablog.jp/entry/20160415/1460722489) 있다.

그리하여 [WHATWG](https://github.com/whatwg/ "WHATWG")에 있는 Living Standard 사양을 GitHub에서 일본어로 번역하고 있습니다.

- [웹과 관련된 사양 일본어 번역](https://triple-underscore.github.io/ "웹과 관련된 사양 일본어 번역")(일본어)

또, WHATWG의 사양 원글에는 일본어 번역에 관한 링크가 일부 추가될 것으로 보입니다.

- [WHATWG translations · Issue #1 · triple-underscore/triple-underscore.github.io](https://github.com/triple-underscore/triple-underscore.github.io/issues/1 "WHATWG translations · Issue #1 · triple-underscore/triple-underscore.github.io")

위에서 소개한 번역 말고도 [@momdo_](https://twitter.com/momdo_ "@momdo_")가 진행하고 있는 [HTML Standard 일본어 버전](https://momdo.github.io/html/ "HTML Standard 일본어 버전")이라는 Living Standard 사양의 또다른 번역 문서도 있습니다.

- [HTML Standard 일본어 버전](https://momdo.github.io/html/ "HTML Standard 일본어 버전")
- [html · momdo/momdo.github.io Wiki](https://github.com/momdo/momdo.github.io/wiki/html "html · momdo/momdo.github.io Wiki")

WHATWG Living Standard라는 이름 처럼 [항상 갱신](https://github.com/whatwg/html/commits/master)되고 있기 때문에, 최신 정보를 원한다면 원글을 봐야하지만 정리하여 한번에 읽고 싶은 경우에는 번역글을 보면 좋을 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## New Release: 2.9.2
[jshint.com/blog/2016-04-19/release-2-9-2/](http://jshint.com/blog/2016-04-19/release-2-9-2/ "New Release: 2.9.2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.9.2가 릴리즈됐습니다.

----

## Release v3.5.0 · reactjs/redux
[github.com/reactjs/redux/releases/tag/v3.5.0](https://github.com/reactjs/redux/releases/tag/v3.5.0 "Release v3.5.0 · reactjs/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 3.5.0이 릴리즈됐습니다.
ES.next의 Stage 1 Proposal인 es obvervable을 대응했습니다.
`Symbol.observable` 구현체를 추가했습니다.

----

## Release 2.3.0 - 2016.04.24 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v2.3.0](https://github.com/zloirock/core-js/releases/tag/v2.3.0 "Release 2.3.0 - 2016.04.24 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 2.3.0이 릴리즈됐습니다.
`global.asap`, `Symbol.asyncIterator`, `Symbol.observable`을 추가하고 
`Map#toJSON`, `Set#toJSON`, `Error.isError`를 삭제하는 등 TC39의 미팅 내용이 중심적으로 반영됐습니다.

- [tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes](https://github.com/rwaldron/tc39-notes/tree/master/es7/2016-03 "tc39-notes/es7/2016-03 at master · rwaldron/tc39-notes")

----

## V8 JavaScript Engine: V8 Release 5.1
[v8project.blogspot.com/2016/04/v8-release-51.html](http://v8project.blogspot.com/2016/04/v8-release-51.html "V8 JavaScript Engine: V8 Release 5.1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.1이 릴리즈됐습니다.
`Symbol.species`, `Symbol.hasInstance`, Function name에 관한 사양이 반영됐고, 성능 및 메모리 사용량이 개선됐습니다.

----

## Release Version 2.0.0 · chartjs/Chart.js
[github.com/chartjs/Chart.js/releases/tag/v2.0.0](https://github.com/chartjs/Chart.js/releases/tag/v2.0.0 "Release Version 2.0.0 · chartjs/Chart.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">canvas</span> <span class="jser-tag">그래프</span> <span class="jser-tag">library</span></p>

Canvas를 사용한 그래프 라이브러리인 Chart.js 2.0.0이 릴리즈됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## DOM Listener: capture, passive, and once
[www.webreflection.co.uk/blog/2016/04/17/new-dom4-standards](https://www.webreflection.co.uk/blog/2016/04/17/new-dom4-standards "DOM Listener: capture, passive, and once")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span></p>

`node.addEventListener(type, handler, EventListenerOptions)`의 세번째 인수인 `EventListenerOptions`에 관해 작성돼 있습니다.
`passive`와 `capture`에 관해 설명합니다.

----

## How do I update to Gulp 4? - Liquid Light
[www.liquidlight.co.uk/blog/article/how-do-i-update-to-gulp-4/](https://www.liquidlight.co.uk/blog/article/how-do-i-update-to-gulp-4/ "How do I update to Gulp 4? - Liquid Light")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span></p>

아직 릴리즈 되진 않았지만, 해당 글에는 gulp 4로 업데이트하는 방법에 관해 작성돼 있습니다.

----

## Stylelint | CSS-Tricks
[css-tricks.com/stylelint/](https://css-tricks.com/stylelint/ "Stylelint | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSS의 Lint 도구인 Stylelint를 소개합니다.
에디터와의 연동, PostCSS, stylefmt 등을 설명합니다.

----

## emilbjorklund/svg-weirdness: A repository of bugs and plain weird behavior in SVG
[github.com/emilbjorklund/svg-weirdness](https://github.com/emilbjorklund/svg-weirdness "emilbjorklund/svg-weirdness: A repository of bugs and plain weird behavior in SVG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">browser</span> <span class="jser-tag">issue</span></p>

SVG의 버그를 이슈로 등록하여 모아놓는 저장소입니다.

----

## 중급자를 위한 Service Worker Tutorial | blog.jxck.io(일본어)
[blog.jxck.io/entries/2016-04-24/service-worker-tutorial.html](https://blog.jxck.io/entries/2016-04-24/service-worker-tutorial.html "中級者向け Service Worker Tutorial | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">영상</span></p>

ServiceWorker를 사용해 개발할 때 발생하는 문제나 동작 방식에 관해 설명하는 스크린캐스트입니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## EmberConf 2016 - YouTube
[www.youtube.com/playlist?list=PL4eq2DPpyBblc8aQAd516-jGMdAhEeUiW](https://www.youtube.com/playlist?list=PL4eq2DPpyBblc8aQAd516-jGMdAhEeUiW "EmberConf 2016 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">영상</span></p>

EmberConf 2016의 영상이 공개됐습니다.

- [EmberConf 2016 - March 29 &amp; 30, Portland, OR.](http://emberconf.com/ "EmberConf 2016 - March 29 &amp; 30, Portland, OR.")

----

## Dev.Opera — Front-End Performance: The Dark Side
[dev.opera.com/blog/timing-attacks/](https://dev.opera.com/blog/timing-attacks/ "Dev.Opera — Front-End Performance: The Dark Side")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">영상</span></p>

프론트엔드의 성능에 관해 설명하는 영상입니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Flexbox Patterns
[www.flexboxpatterns.com/home](http://www.flexboxpatterns.com/home "Flexbox Patterns")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

Flexbox 패턴 모음집입니다.

----

## 웹과 관련된 사양 일본어 버전(일본어)
[triple-underscore.github.io/](https://triple-underscore.github.io/ "웹과 관련된 사양 일본어 버전")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">spec</span> <span class="jser-tag">번역</span></p>

WHATWG나 W3C 등 사양 문서를 일본어로 번역해 공개하는 사이트입니다.

----

## 처음 시작하는 프로그레시브 웹 애플리케이션(일본어)
[codelabs.developers.google.com/codelabs/your-first-pwapp-ja/](https://codelabs.developers.google.com/codelabs/your-first-pwapp-ja/ "처음 시작하는 프로그레시브 웹 애플리케이션")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span></p>

프로그레시브 웹 애플리케이션을 배울 수 있는 튜토리얼 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## evcohen/eslint-plugin-jsx-a11y: Static AST checker for a11y rules on JSX elements.
[github.com/evcohen/eslint-plugin-jsx-a11y](https://github.com/evcohen/eslint-plugin-jsx-a11y "evcohen/eslint-plugin-jsx-a11y: Static AST checker for a11y rules on JSX elements.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">ESLint</span></p>

JSX 요소에서 접근성을 체크할 수 있는 ESLint의 규칙 플러그인입니다.

----

## VictorBjelkholm/autochecker: Test your JavaScript modules simultaneously in 32 different versions of NodeJS
[github.com/VictorBjelkholm/autochecker](https://github.com/VictorBjelkholm/autochecker "VictorBjelkholm/autochecker: Test your JavaScript modules simultaneously in 32 different versions of NodeJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span></p>

여러 Node.js 버전에서 테스트(matrix test)할 수 있는 도구입니다.

----

## staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript
[github.com/staltz/xstream](https://github.com/staltz/xstream "staltz/xstream: An extremely intuitive, small, and fast functional reactive stream library for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">library</span></p>

Hot only, RxJS 스러운 Stream 라이브러리입니다.

- [André Staltz - Why we built xstream](http://staltz.com/why-we-built-xstream.html "André Staltz - Why we built xstream")

----

## jonathanewerner/webpack-validator: Validates your webpack config with Joi
[github.com/jonathanewerner/webpack-validator](https://github.com/jonathanewerner/webpack-validator "jonathanewerner/webpack-validator: Validates your webpack config with Joi")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

webpack 설정 파일의 유효성을 검증하는 도구입니다.

----

## webpack/memory-fs: A simple in-memory filesystem. Holds data in a javascript object.
[github.com/webpack/memory-fs](https://github.com/webpack/memory-fs "webpack/memory-fs: A simple in-memory filesystem. Holds data in a javascript object.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

memory 위에서 읽고 쓸 수 있는 fs 모듈입니다.

----
