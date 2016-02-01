---
title: "2016-01-26 JS: JavaScript와 OOP, Fetch with Stream, ES6 치트시트"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-01-26T18:18
category: JSer
tags:
    - OOP
    - Fetch
    - JavaScript
    - ES6

---

JSer.info #263 - [OO Relationships — Medium](https://medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162 "OO Relationships — Medium")에는 JavaScript와 객체 지향 프로그래밍에 관해 작성돼 있습니다.

[Allen Wirfs-Brock](https://twitter.com/awbjs "Allen Wirfs-Brock")의 아래의 발언으로 인해 글이 시작됐습니다(지금도 계속되고 있습니다)

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">JS devs: do you use abstraction? What word do you use for “an open set of objects that share a common interface and implementation”?</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/689506114807857152">January 19, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">JS Devs: What  do you call “an open set of objects that share a common interface and implementation”?</p>&mdash; Allen Wirfs-Brock (@awbjs) <a href="https://twitter.com/awbjs/status/689513929546928128">January 19, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

ES6에서 추가된 `class`를 기반으로, 프로토타입 기반인 JavaScript와 객체 간의 관계성에 관해 작성돼 있습니다.
실용적인 이야기라기보단 개념적인 이야기지만 흥미로운 내용이 많습니다.

----

[2016 - the year of web streams - JakeArchibald.com](https://jakearchibald.com/2016/streams-ftw/ "2016 - the year of web streams - JakeArchibald.com")에서는 Chrome에서 플래그를 활성화해 사용할 수 있는 [WHATWG Stream](https://streams.spec.whatwg.org/ "Streams")에 관해 소개하고 있습니다.

또, [Fetch API](https://fetch.spec.whatwg.org/ "Fetch")와 Stream API를 조합하여 사용하는 것으로,
데이터를 취득한 후, 처리 하고 출력하기 까지의 동작이 어떻게 이루어지는지 소개하고 있습니다.

----

[ECMAScript 2015 by David Leonard](http://slides.com/drksephy/ecmascript-2015#/ "ECMAScript 2015 by David Leonard")에서는 [DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")의 치트시트를 기반으로 ES6에 관해 소개하고 있습니다.

ES6와 ES5를 [비교](http://es6-features.org/)한 내용으로, 구체적으로 어떤 부분이 다른지에 관해 작성돼 있습니다.

----

:information_source:

Podcast나 사이트 등을 소개를 하고 있는 [The Changelog](https://changelog.com/ "The Changelog - Open source moves fast. Keep up.")에 [Ping](https://github.com/thechangelog/ping "Ping")이라고하는 저장소가 있는데, 이와 같은 것이 JSer.info에도 있다면 이용하고 싶은지 의견을 모집하고 있습니다.

Ping은 소개해 줬으면 하는 기사를 요청하거나, 의견을 작성하거나, Changelog라는 사람이 podcast에서 다뤄줬으면하는 것을 요청하는 Github Issue 입니다.
이에 관한 의견이 있거나 하면 Gitter에 작성해주세요.

[![Gitter chat](https://badges.gitter.im/jser/jser.info.png)](https://gitter.im/jser/jser.info)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v2.9.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v2.9.0](https://github.com/jscs-dev/node-jscs/releases/tag/v2.9.0 "Release v2.9.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS v2.9.0가 릴리즈 됐습니다.
`requireCapitalizedConstructors` 규칙이 추가됐고, 규칙이 갱신되거나 버그가 수정됐습니다.


----

## Node v5.5.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.5.0/](https://nodejs.org/en/blog/release/v5.5.0/ "Node v5.5.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v5.5.0가 릴리즈됐습니다.
REPL에서도 `--require`가 작동하도록 변경됐고, `fs.createWriteStream`에서 `autoClose` 옵션을 지원하는 등 다양한 변경 사항이 있습니다.

----

## Release ES2016 Draft 2016-01-20 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20160120](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20160120 "Release ES2016 Draft 2016-01-20 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2016-01-20가 릴리즈됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Simulating Website Thumbnails using Iframes — Medium
[medium.com/@jamesfuthey/simulating-the-creation-of-website-thumbnail-screenshots-using-iframes-7145269891db](https://medium.com/@jamesfuthey/simulating-the-creation-of-website-thumbnail-screenshots-using-iframes-7145269891db "Simulating Website Thumbnails using Iframes — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span></p>

아이프레임을 사용하여 사이트의 썸네일을 출력을 하는 방법에 관해 작성돼 있습니다.

----

## Understand promises before you start using async/await — Medium
[medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8](https://medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8 "Understand promises before you start using async/await — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

async/await를 사용하기 전에 Promise에 관해 이해해 보자는 취지의 글입니다.

----

## OO Relationships — Medium
[medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162](https://medium.com/@DmitrySoshnikov/oo-relationships-5020163ab162 "OO Relationships — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">OOP</span></p>

JavaScript와 객체 지향 프로그래밍에 관해 작성돼 있습니다.
static/dynamic dispatch, prototype 기반, 세로 또는 가로의 상속,
class, mixin, traits, 덕 타이핑, composition등에 관해 소개합니다.

----

## 2016 - the year of web streams - JakeArchibald.com
[jakearchibald.com/2016/streams-ftw/](https://jakearchibald.com/2016/streams-ftw/ "2016 - the year of web streams - JakeArchibald.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Fetch with Stream에 관해 작성돼 있습니다.
readable stream, transform stream을 사용해 MPEG을 GIF로 재생하는 예제가 소개돼 있습니다.

----

## JavaScript의 코드를 분해해 자주 사용되고 있는 구문을 분석한다 | Web Scratch(일본어)
[efcl.info/2016/01/22/es-usage-rate/](http://efcl.info/2016/01/22/es-usage-rate/ "JavaScript의 코드를 분해해 자주 사용되고 있는 구문을 분석한다 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">Tools</span></p>

코드를 파싱해 기능(구문) 별 출현 횟수를 계산하는 도구를 소개합니다.

----

## rollup.js - Rollup이 딱 좋은 느낌 - Qiita(일본어)
[qiita.com/cognitom/items/e3ac0da00241f427dad6](http://qiita.com/cognitom/items/e3ac0da00241f427dad6 "rollup.js - Rollup이 딱 좋은 느낌 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span></p>

Bundler인 rollup.js을 소개합니다.
일단 어떤 코드든지 ES6로 변환한 후 필요에 필요에 따라 babel을 이용해 ES5로 변환하는 원리를 소개하며, Tree Shaking, 기본적인 사용 및 설정 방법에 관해서도 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Cycle.js Fundamentals - Course by @andrestaltz @eggheadio
[egghead.io/series/cycle-js-fundamentals](https://egghead.io/series/cycle-js-fundamentals "Cycle.js Fundamentals - Course by @andrestaltz @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rx</span> <span class="jser-tag">영상</span></p>

Cycle.js 개발자의 Cycle.js와 RxJS에 관한 스크린캐스트입니다.

----

## ECMAScript 2015 by David Leonard
[slides.com/drksephy/ecmascript-2015#/](http://slides.com/drksephy/ecmascript-2015#/ "ECMAScript 2015 by David Leonard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">슬라이드</span></p>

ES5로 작성하기 힘든 문법을 ES6에서 작성하게 되는 경우 어떻게 표현 되는지 등에 관해 소개하는 슬라이드입니다.
어떤 부분이 어떻게 다른지를 알기 쉽게 주석이 친절하게 작성돼 있습니다.

- [DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## DrkSephy/es6-cheatsheet
[github.com/DrkSephy/es6-cheatsheet](https://github.com/DrkSephy/es6-cheatsheet "DrkSephy/es6-cheatsheet")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6의 치트시트입니다.
ES5에서의 작성법과 ES6에서의 작성법을 비교하는 형태로 작성돼 있습니다.

----

## Pa11y - Your automated accessibility testing pal
[pa11y.org/](http://pa11y.org/ "Pa11y - Your automated accessibility testing pal")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">접근성</span> <span class="jser-tag">Tools</span></p>

접근성 검사 as a Service, 매일 실행해 결과를 집계하고 대쉬보드로 볼 수 있는 도구입니다.
또 CLI로 검사 하는 것도 가능합니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Umbrella JS
[umbrellajs.com/](http://umbrellajs.com/ "Umbrella JS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

jQuery 처럼 DOM을 조작하거나 Ajax 관련 기능을 제공하는 경량 라이브러리입니다.

----

## stomita/clipboard-hook
[github.com/stomita/clipboard-hook](https://github.com/stomita/clipboard-hook "stomita/clipboard-hook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">클립보드</span></p>

요소의 이벤트를 해당 라이브러리에 전달하는 방식으로 `cut` / `copy` / `paste` 이벤트의 hook을 작성할 수 있는 라이브러리입니다.

----

## Jam3/devtool: runs Node.js programs through Chromium DevTools
[github.com/Jam3/devtool](https://github.com/Jam3/devtool "Jam3/devtool: runs Node.js programs through Chromium DevTools")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">Electron</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

Node.js를 실행하고 개발자 도구로 디버깅 가능한 Electron 기반의 도구입니다.
명령줄을 이용해 Node.js의 파일을 지정하여 실행할 수 있습니다.

----

## skerit/janeway: A curses-based console for node.js
[github.com/skerit/janeway](https://github.com/skerit/janeway "skerit/janeway: A curses-based console for node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">debug</span></p>

curses/blessed 기반의 JavaScript REPL입니다.
브라우저의 개발자 도구 처럼 인터렉티브한 동작을 목적으로 하고 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## JavaScript Master - O&#x27;Reilly Media
[shop.oreilly.com/product/9780994346933.do](http://shop.oreilly.com/product/9780994346933.do "JavaScript Master - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016년 3월 출간 예정인 JavaScript에 관한 서적입니다.

----
