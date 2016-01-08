---
title: "2016-01-06 JS: React 에코시스템 입문, 벤더 프리픽스와 웹 표준, Setting up ES6"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-01-06T18:22
category: JSer
tags:
    - React
    - WebKit
    - CSS
    - Babel
    - Book

---

JSer.info #260 - [petehunt/react-howto](https://github.com/petehunt/react-howto "petehunt/react-howto")에는 React와 관련된 에코시스템의 입문에 관해 작성돼 있습니다.

[npm](https://www.npmjs.com/ "npm")과 [Browserify](http://browserify.org/ "Browserify")이나 [webpack](https://webpack.github.io/ "webpack") 그리고 Flux 라이브러리 등을 학습하는 방법에 대해서도 소개합니다.

----

[Webkit! RESOLVED FIXED - otsukare](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")에는 Firefox 46부터 `layout.css.prefixes.webkit`의 옵션이 기본으로 활성화된 이유에 대해 작성돼 있습니다.

이름 그대로 파이어폭스에서 CSS의 `-webkit-` prefix를 기본으로 인식하도록 하는 옵션입니다.
WebKit 브라우저만 고려해 `-webkit-box`(현재의 Flexbox)등을 사용하여 코드를 작성한 사이트도 렌더링 가능하도록 하는데 목적을 두고 있습니다.

아시아(특히 [일본](http://www.otsukare.info/2015/04/17/web-compatibility-japan))의 모바일 사이트에서는 WebKit 브라우저만을 고려한 것이 많은데 이번부터 -webkit- prefix도 인식 가능하도록 됐습니다.

MSEdge에서도 이와 같이 대응하고 있습니다.

- [A break from the past, part 2: Saying goodbye to ActiveX, VBScript, attachEvent… | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2015/05/06/a-break-from-the-past-part-2-saying-goodbye-to-activex-vbscript-attachevent/ "A break from the past, part 2: Saying goodbye to ActiveX, VBScript, attachEvent… | Microsoft Edge Dev Blog")

아래의 글도 함께 읽어보면 좋을 것 같습니다.

- [총 57,000 행이나 되는 거대한 CSS 코드 집합을 Less로 재작성한 기록 - mixi Engineers' Blog](http://alpha.mixi.co.jp/entry/2015/12/20/000000 "총 57,000 행이나 되는 거대한 CSS 코드 집합을 Less로 재작성한 기록 - mixi Engineers' Blog")(일본어)
- [Well, I'm Back: innerText: Cleaning A Dark Corner Of the Web](http://robert.ocallahan.org/2016/01/innertext.html "Well, I'm Back: innerText: Cleaning A Dark Corner Of the Web")

----

[Setting up ES6 by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]](https://leanpub.com/setting-up-es6 "Setting up ES6 by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]")라는 전자 서적에는 Babel을 사용해 ES6의 코드를 다루는 방법 등에 관해서 작성돼 있습니다.

- [My new book: “Setting up ES6”](http://www.2ality.com/2016/01/book-setting-up-es6.html "My new book: “Setting up ES6”")

또 ES6에서 Module의 구문을 정의하고 있으나, [불러오는 방법](ttps://github.com/whatwg/loader/issues)에 관해서는 아직 의논 중입니다. 
따라서, CommonJS와의 상호운용성은 도구의 해석에 따라 다르다는 점에 관해서도 자세히 작성돼 있습니다.

- [ES6 in Practice](http://www.slideshare.net/teppeis/es6-in-practice "ES6 in Practice")

----
<h1 class="site-genre">아티클</h1>

----

## petehunt/react-howto
[github.com/petehunt/react-howto](https://github.com/petehunt/react-howto "petehunt/react-howto")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

React 개발자가 작성한 React의 에코시스템 입문을 위한 가이드라인

----

## Revisiting Firefox’s DevTools – Smashing Magazine
[www.smashingmagazine.com/2015/12/revisiting-firefox-devtools/](http://www.smashingmagazine.com/2015/12/revisiting-firefox-devtools/ "Revisiting Firefox’s DevTools – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span></p>

파이어폭스 개발자 도구를 새롭게 소개하는 글입니다.
최근 다양한 기능이 추가 됐습니다.

----

## Angular 2 versus React: There Will Be Blood — Medium
[medium.com/@housecor/angular-2-versus-react-there-will-be-blood-66595faafd51](https://medium.com/@housecor/angular-2-versus-react-there-will-be-blood-66595faafd51 "Angular 2 versus React: There Will Be Blood — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">React</span></p>

AngularJS와 React를 비교한 글 입니다.

> Angular 2 continues to put “JS” into HTML. React puts “HTML” into JS.

----

## Well, I&#x27;m Back: innerText: Cleaning A Dark Corner Of the Web
[robert.ocallahan.org/2016/01/innertext.html](http://robert.ocallahan.org/2016/01/innertext.html "Well, I'm Back: innerText: Cleaning A Dark Corner Of the Web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">DOM</span></p>

IE나 WebKit에도 존재하는 `innerText`는 사양과 상호운용성이 없었는데, WebKit만 고려한 모바일 사이트에서 자주 사용하는 기능이기 때문에 파이어폭스에서도 해당 기능을 구현하기로 했고 또, 동시에 사양과 테스트 케이스도 작성했다고 소개하는 글입니다.

- [The poor, misunderstood innerText — Perfection Kills](http://perfectionkills.com/the-poor-misunderstood-innerText/ "The poor, misunderstood innerText — Perfection Kills")
- [Webkit! RESOLVED FIXED - otsukare](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")

----

## Webkit! RESOLVED FIXED - otsukare
[www.otsukare.info/2016/01/04/webkit-resolved-fixed](http://www.otsukare.info/2016/01/04/webkit-resolved-fixed "Webkit! RESOLVED FIXED - otsukare")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">webkit</span></p>

Firefox 46에서 CSS의 `-webkit-` prefix를 인식하도록 하는 옵션이 기본적으로 활성화 됐습니다. 
`-webkit-` prefix 밖에 쓰지 않는 경우에도 렌더링할 수 있도록 하는 것에 목적이 있습니다.

- [1213126 – Enable layout.css.prefixes.webkit by default](https://bugzilla.mozilla.org/show_bug.cgi?id=1213126 "1213126 – Enable layout.css.prefixes.webkit by default")
- [총 57,000 행이나 되는 거대한 CSS 코드 집합을 Less로 재작성한 기록 - mixi Engineers&#x27; Blog](http://alpha.mixi.co.jp/entry/2015/12/20/000000 "총 57,000 행이나 되는 거대한 CSS 코드 집합을 Less로 재작성한 기록 - mixi Engineers' Blog")

----

## ChromeDevTool - Chrome Developer Tools로 성능 측정하고 개선하기 - Qiita(일본어)
[qiita.com/y\_fujieda/items/a0a69151cf7307039f74](http://qiita.com/y_fujieda/items/a0a69151cf7307039f74 "ChromeDevTool - Chrome Developer Tools로 성능 측정하고 개선하기 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

크롬 개발자 도구의 각각 패널을 해부합니다.
조작 방법이나 각 항목의 의미 등에 관해 작성돼 있습니다.

----

## JavaScript - AudioWorker를 시험해보다 - Qiita(일본어)
[qiita.com/mohayonao/items/ce357230946cfa2303c2](http://qiita.com/mohayonao/items/ce357230946cfa2303c2 "JavaScript - AudioWorker를 시험해보다 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">audo</span> <span class="jser-tag">JavaScript</span></p>

Web Audio API의 AudioWorker에 관해서 작성돼 있습니다.

- [mohayonao/audio-worker-shim](https://github.com/mohayonao/audio-worker-shim "mohayonao/audio-worker-shim")

----

## Managing the private data of ES6 classes
[www.2ality.com/2016/01/private-data-classes.html](http://www.2ality.com/2016/01/private-data-classes.html "Managing the private data of ES6 classes")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

ES6 Classes에서 private 적으로 데이터를 보유하는 패턴에 관해 소개합니다.

----

## Lerna를 사용하여 Babel이나 React가 채택하고 있는 monorepo를 시험해봤다 - Qiita
[qiita.com/kimamula/items/0b4dff363933bfe74506](http://qiita.com/kimamula/items/0b4dff363933bfe74506 "Lerna를 사용하여 Babel이나 React가 채택하고 있는 monorepo를 시험해봤다 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Babel 처럼 monorepo를 lerna를 사용하여 관리하는 방법에 관해 작성돼 있습니다.

----

## Flux explained for newbies – Part 1 | DevButze
[devbutze.com/p/216](https://devbutze.com/p/216 "Flux explained for newbies – Part 1 | DevButze")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">tutorial</span></p>

컴포넌트 관점으로 UI를 바라 볼 때, 왜 Flux 같은 아키텍처가 필요하게 되는지에 관해 연재하고 있습니다.

----

## Day 2: Testing React Applications – 12 Devs of Xmas
[12devsofxmas.co.uk/2015/12/day-2-testing-react-applications/](http://12devsofxmas.co.uk/2015/12/day-2-testing-react-applications/ "Day 2: Testing React Applications – 12 Devs of Xmas")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

React Component의 테스트에 관해 작성돼 있습니다.
jsdom, Enzyme를 사용한 테스트 방법 등을 소개합니다.

----

## AddyOsmani.com - Offline installation of npm packages
[addyosmani.com/blog/using-npm-offline/](https://addyosmani.com/blog/using-npm-offline/ "AddyOsmani.com - Offline installation of npm packages")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span></p>

npm install을 오프라인에서도 사용할 수 있도록 하기 위한 팁을 소개합니다.
`--cache-min`, local-npm, npm_lazy 등에 관해 작성돼 있습니다.

----

## the new code – Create Fullscreen HTML5 Page Background Video
[thenewcode.com/777/Create-Fullscreen-HTML5-Page-Background-Video](http://thenewcode.com/777/Create-Fullscreen-HTML5-Page-Background-Video "the new code – Create Fullscreen HTML5 Page Background Video")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">영상</span></p>

HTML5 Video를 배경으로 사용하는 방법과 주의할 점에 관해 작성돼 있습니다.

- [Should I use a video as a background? | CSS-Tricks](https://css-tricks.com/should-i-use-a-video-as-a-background/ "Should I use a video as a background? | CSS-Tricks")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Getting Started with Redux - Course by @dan_abramov @eggheadio
[egghead.io/series/getting-started-with-redux](https://egghead.io/series/getting-started-with-redux "Getting Started with Redux - Course by @dan_abramov @eggheadio")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span></p>

Redux 개발자가 발행한 Redux 입문 스크린 캐스트 입니다.

- [tayiorbeii/egghead.io\_redux\_course\_notes](https://github.com/tayiorbeii/egghead.io_redux_course_notes "tayiorbeii/egghead.io_redux_course_notes")

----

## Node.js Interactive 2015 - YouTube
[www.youtube.com/playlist?list=PLfMzBWSH11xYjL8oFumSfzOf6-kr8\_t-o](https://www.youtube.com/playlist?list=PLfMzBWSH11xYjL8oFumSfzOf6-kr8_t-o "Node.js Interactive 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">영상</span> <span class="jser-tag">정리</span></p>

Node.js Interactive 2015 발표 영상 목록입니다.

- [Node.js Interactive 2015 | Linux Conferences and Linux Events | The Linux Foundation](http://events.linuxfoundation.org/events/node-interactive "Node.js Interactive 2015 | Linux Conferences and Linux Events | The Linux Foundation")
- [duffn/nodeinteractive-2015](https://github.com/duffn/nodeinteractive-2015 "duffn/nodeinteractive-2015")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## orizens/angular-es2015-styleguide
[github.com/orizens/angular-es2015-styleguide](https://github.com/orizens/angular-es2015-styleguide "orizens/angular-es2015-styleguide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

AngularJS 1.x과 ES2015를 함께 고려한 스타일 가이드입니다.

----

## HTML 5 Canvas Cheat Sheet - WebsiteSetup.org
[websitesetup.org/html-5-canvas-cheat-sheet/](http://websitesetup.org/html-5-canvas-cheat-sheet/ "HTML 5 Canvas Cheat Sheet - WebsiteSetup.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML5</span> <span class="jser-tag">canvas</span> <span class="jser-tag">치트시트</span></p>

Canvas 치트시트 입니다.

----

## WPO Stats
[wpostats.com/](https://wpostats.com/ "WPO Stats")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">정리</span></p>

웹 성능 최적화를 주제로 작성된 글이 수집돼 있는 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Lucifier129/react-lite
[github.com/Lucifier129/react-lite](https://github.com/Lucifier129/react-lite "Lucifier129/react-lite")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React의 Core API와 호환성 있는 구현 라이브러리입니다.
서버 사이드 렌더링, `React.PropTypes`, addons 등을 제거하여 더 작은 파일 사이즈를 목표로 구현돼 있습니다.

----

## substack/hyperx
[github.com/substack/hyperx](https://github.com/substack/hyperx "substack/hyperx")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">library</span></p>

Template Strings를 사용하여 디자인하고 virtual-dom, React, hyperscript에 대응한 빌더 라이브러리입니다.

----

## narirou/jconv
[github.com/narirou/jconv](https://github.com/narirou/jconv "narirou/jconv")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">문자코드</span> <span class="jser-tag">library</span></p>

순수 자바스크립트로만 작성된 Shift_JIS(CP932), ISO-2022-JP(-1), EUC-JP, UTF-8, UNICODE를 상호 변환할 수 있는 라이브러리입니다.

----

## unit-coverage/unit-coverage
[github.com/unit-coverage/unit-coverage](https://github.com/unit-coverage/unit-coverage "unit-coverage/unit-coverage")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

코드 커버리지 도구입니다.
코드 간의 관계도 커버리지 리포트에 포함시킬 수 있습니다. 
이 도구는 JSCS 에서 사용하고 있습니다.

- [Coverage report](http://jscs.info/jscs/coverage.html "Coverage report")

----
<h1 class="site-genre">도서</h1>

----

## Setting up ES6 by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]
[leanpub.com/setting-up-es6](https://leanpub.com/setting-up-es6 "Setting up ES6 by Axel Rauschmayer [Leanpub PDF/iPad/Kindle]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ebook</span></p>

Dr.Axel의 Babel을 사용한 ES6의 도입에 관한 전자 서적입니다. 
loader의 방식이 transpiler나 CommonJS에 의존 하고 있는 가운데, 모듈 동작에 관련한 오해를 풀 수 있는 내용이 작성돼 있습니다.

----
