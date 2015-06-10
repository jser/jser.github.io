---
title: "2015-06-10 JS: 브라우저와 ES6 상황 、Web Audio API 튜토리얼"
author: azu
translator: ChoEun
layout: post
date : 2015-06-10T12:45
category: JSer
tags:
    - WebAudio
    - ES6
    - Safari
    - Chrome
    - MSEdge

---

JSer.info #231 - [Safari 9.0](https://developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html "Safari 9.0") 변경사항이 공개되어 있습니다.

JavaScript 방면에선 ES6 Classes、Template Strings、Symbol、Computed Properties 등을 추가로 지원합니다.
또 CSS 방면에선、`-webkit-` prefix가 제거된 것이 많지만、반대로 `-webkit-` prefix를 붙인`-webkit-scroll-snap-type` 등을 추가로 지원합니다.

Webkit의 ES6나 CSS 등에 관한 구현현황은 아래 스테이터스 페이지에 공개되어있어, 관심이 있는 분이라면 참고하시길 바랍니다.

- [The WebKit Open Source Project - Web Platform Status](http://www.webkit.org/status.html "The WebKit Open Source Project - Web Platform Status")

또, Microsoft의 새 브라우저인 MSEdge가 서포트하고있는 ES6 기능에 대해서는 [JavaScript의 신기능](https://msdn.microsoft.com/library/br212465(v=vs.94).aspx "JavaScript의 신기능")이라는 페이지에 레퍼런스가 공개되어있습니다.
구현현황을 정리해둔 스테이터스 페이지도 [Developer Resources : MSEdge Dev](http://dev.modern.ie/platform/status/ "Developer Resources : MSEdge Dev")에 공개되어 있습니다.

같은 시기에 [Chrome 44 Beta](http://blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html "Chrome 44 Beta")도 공개되어, 크롬에서도 Computed Properties과 유니코드 이스케이프 리터럴 등을 지원하고, 구현현황에 대해서는 [Chromium Dashboard](https://www.chromestatus.com/features "Chromium Dashboard")에 공개되어있습니다.

Firefox는 구현현황을 정리한 페이지는 없지만, [ECMAScript 6 compatibility table](http://kangax.github.io/compat-table/es6/ "ECMAScript 6 compatibility table")를 보면 각 브라우저에의 구현현황을 한번에 보는게 가능합니다.

----

[Web Audio School](http://mmckegg.github.io/web-audio-school/ "Web Audio School") 사이트에서는、[Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API "Web Audio API")에 대해서 공부할 수 있는 튜토리얼을 공개하고 있습니다.

예전에 [JavaScript와 Web Audio 시작하기](http://azu.github.io/slide/webaudioapi/web-audio.html "JavaScript와 Web Audio 시작하기") 슬라이드에서 간단히 Web Audio에 대해서 소개해드렸었는데, Web Audio API로 소리를 처리하는 경우는, 음량을 조정하는 GainNode를 만들어서 이어주고 AudioNode로 처리하여 필터를 붙입니다.

![AudioNode](http://monosnap.com/image/aFVeydGv2X32wTXrWCSpHfMYYBIOhd.png)

[Web Audio School](http://mmckegg.github.io/web-audio-school/ "Web Audio School") 사이트에서는, Web Audio API의 기본적인 사용법부터 다양한 AudioNode의 처리 방법에 대해 써져 있습니다.

Web Audio API 코드를 작성하여, 기대한대로 동작하도록 맞추어 나가는게 문제의 형식마냥 되어있지만, 적어둔 문제가 맞는지에 대해서는 시각적으로 표현하고 있는 점이 재미있습니다.

<div class="kwout" style="text-align: center;"><img src="http://kwout.com/cutout/6/j6/7q/s2u_bor.jpg" alt="http://mmckegg.github.io/web-audio-school/" title="Web Audio School" width="600" height="339" style="border: none;" usemap="#map_6j67qs2u" /><p><a href="http://mmckegg.github.io/web-audio-school/">Web Audio School</a></p></div>

----

## 알림

예전부터 @[UYEONG](https://github.com/UYEONG "UYEONG")님이 [JSer.info의 한글번역](http://wit.nts-corp.com/)을 진행하고 있었습니다만, 한글번역도 [http://jser.info/ko/](http://jser.info/ko/) 같은 느낌으로 같은 사이트 내에서 공개하기로 하였습니다.

![header](http://monosnap.com/image/whz0nvwzXYcZfhtIwxyhL0aowGyOZD.png) 

그로 인해, 사이트 헤더 부분에 언어 변경 링크를 추가하였습니다.

----


<h1 class="site-genre">헤드라인</h1>

----

## Node v0.12.4 (Stable)
[blog.nodejs.org/2015/05/22/node-v0-12-4-stable/](http://blog.nodejs.org/2015/05/22/node-v0-12-4-stable/ "Node v0.12.4 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.4 릴리즈

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#550](https://github.com/babel/babel/blob/master/CHANGELOG.md#550 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Babel 5.5.0 릴리즈.
버그 수정 중심

----

## What’s new in Babylon.js v2.1 - Eternal Coding - HTML5 / JavaScript / 3D development - Site Home - MSDN Blogs
[blogs.msdn.com/b/eternalcoding/archive/2015/06/08/what-s-new-in-babylon-js-v2-1.aspx](http://blogs.msdn.com/b/eternalcoding/archive/2015/06/08/what-s-new-in-babylon-js-v2-1.aspx "What’s new in Babylon.js v2.1 - Eternal Coding - HTML5 / JavaScript / 3D development - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">ReleaseNote</span></p>

Babylon.js v2.1 릴리즈

----

## Chromium Blog: Chrome 44 Beta: Improvements to Notifications API and promoted add to homescreen
[blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html](http://blog.chromium.org/2015/06/chrome-44-beta-improvements-to.html "Chromium Blog: Chrome 44 Beta: Improvements to Notifications API and promoted add to homescreen")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 44 Beta 릴리즈.
푸시 알림 개선、`\u{1F302}` 같은 [Unicode 이스케이프 문자열](https://googlechrome.github.io/samples/extended-unicode-escapes/index.html)、ES6 Computed Properties、`document.scrollingElement`를 지원

----

## Safari 9.0
[developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html](https://developer.apple.com/library/prerelease/mac/releasenotes/General/WhatsNewInSafari/Articles/Safari_9.html "Safari 9.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 9.0에서 변경점으로 Template strings、Classes、WeakSet、Symbol 등 ES6 지원、 개발자 툴의 디자인 개선 및 기능추가를 진행.

- [Safari 9.0의 신기능 개요 - console.lealog();](http://lealog.hateblo.jp/entry/2015/06/09/115905 "Safari 9.0의 신기능 개요 - console.lealog();")
- [iOS9_changes · uupaa/WebKitChangeLog Wiki](https://github.com/uupaa/WebKitChangeLog/wiki/iOS9_changes "iOS9_changes · uupaa/WebKitChangeLog Wiki")

----

## Changelog · winjs/winjs Wiki
[github.com/winjs/winjs/wiki/Changelog#v40](https://github.com/winjs/winjs/wiki/Changelog#v40 "Changelog · winjs/winjs Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WinJS 4.0 릴리즈

----
<h1 class="site-genre">아티클</h1>

----

## New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/](https://hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/ "New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

Firefox 40 개발자 툴에 대해서
퍼포먼스 툴의 개선, 네트워크 모니터에서 Post 데이터 복사, CSS 도큐먼트 표시 연계 등

----

## Polymer 엘리먼트 개발 툴과 CI - 시와 창작, 사색의 광장
[motemen.hatenablog.com/entry/2015/06/polymer-tools-and-ci](http://motemen.hatenablog.com/entry/2015/06/polymer-tools-and-ci "Polymer 엘리먼트 개발 툴과 CI - 시와 창작, 사색의 광장")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

Polymer에 관련있는 툴이나 라이브러리를 다루고 있습니다.
컴포넌트의 문서제작법, 개발 보조 도구, 배포를 위한 빌드 작성, CI에서 테스트하는 법 등

----

## React/deku 컴포넌트와 this 패턴 | Web Scratch
[efcl.info/2015/06/05/this-component/](http://efcl.info/2015/06/05/this-component/ "React/deku 컴포넌트와 this 패턴 | Web Scratch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span></p>

React 컴포넌트를 ES6 Classes로 작성하면`this`가 여러개인 문제와 이벤트 핸들러 등록/해제 예시.
또, 함수적 접근방법을 지닌 deku 컴포넌트 사이의 차이에 대해서

----

## React: 보수하기 쉬운 고성능 UI 컴포넌트를 작성하기
[www.ibm.com/developerworks/jp/web/library/wa-react-intro/index.html](http://www.ibm.com/developerworks/jp/web/library/wa-react-intro/index.html "React: 보수하기 쉬운 고성능 UI 컴포넌트를 작성하기")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React、Component、Flux、디버깅 툴、GraphQL와 ReactNative 등의 관련 프로젝트 등 React의 전반적인 내용에 대한 기사

----
<h1 class="site-genre">슬라이드, 동영상</h1>

----

## BlinkOn 4 One-Pager - http://bit.ly/blinkon4onepager - Google 도큐먼트
[docs.google.com/document/d/1ga5lPyCxQ0G7deJWDZPSbVvewG7cRdT6Qi-pHXUDgkg/edit#heading=h.rx77pwie3tnj](https://docs.google.com/document/d/1ga5lPyCxQ0G7deJWDZPSbVvewG7cRdT6Qi-pHXUDgkg/edit#heading=h.rx77pwie3tnj "BlinkOn 4 One-Pager - http://bit.ly/blinkon4onepager - Google 도큐먼트")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">blink</span> <span class="jser-tag">이벤트</span></p>

Blink에 대한 이벤트인 BlinkOn  4개의 동영상과 슬라이드 정리

----

## Integrity protection for third-party JavaScript // Speaker Deck
[speakerdeck.com/fmarier/integrity-protection-for-third-party-javascript-1](https://speakerdeck.com/fmarier/integrity-protection-for-third-party-javascript-1 "Integrity protection for third-party JavaScript // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">보안</span></p>

브라우저에 구현되어있는 서드파티 스크립트에 대응하는 보안에 대한 슬라이드 
CSP、HSTS、SRI에 대해서

----

## ▶ Asynchronous JavaScript at Netflix by Matthew Podwysowski at JSConf Budapest 2015 - YouTube
[www.youtube.com/watch?v=a8W5VVGO-jA](https://www.youtube.com/watch?v=a8W5VVGO-jA "▶ Asynchronous JavaScript at Netflix by Matthew Podwysowski at JSConf Budapest 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">동영상</span> <span class="jser-tag">슬라이드</span></p>

Rx나 Observable에 대한 발표.
비동기에 있어서는 Promise가 있지만 Cancel이 불가능한 문제가 있고, Node Stream은 최적하지 않기 때문에, 그 부분을 다루는 API 디자인으로써 Observable、Rx에 대해 소개하고 있다.

- [mattpodwysocki/jsconfbp-2015](https://github.com/mattpodwysocki/jsconfbp-2015 "mattpodwysocki/jsconfbp-2015")

----
<h1 class="site-genre">사이트, 서비스, 도큐먼트</h1>

----

## Web Audio School
[mmckegg.github.io/web-audio-school/](http://mmckegg.github.io/web-audio-school/ "Web Audio School")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span></p>

Web Audio API에 대한 튜토리얼 사이트
각각의 Audio Node에 대한 해설과 실행결과를 시각적으로 이해하기 쉽게 설명하고 있어 이해하기 쉽다.

----

## What&#x27;s New in JavaScript
[msdn.microsoft.com/en-us/library/ie/br212465(v=vs.94).aspx](https://msdn.microsoft.com/en-us/library/ie/br212465(v=vs.94).aspx "What&#x27;s New in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MSEdge</span></p>

MSEdge에서 작동하는 JavaScript의 새로운 기능에 대한 페이지

----

## The Accessibility Cheatsheet - bitsofco.de
[bitsofco.de/2015/the-accessibility-cheatsheet](http://bitsofco.de/2015/the-accessibility-cheatsheet "The Accessibility Cheatsheet - bitsofco.de")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">접근성</span> <span class="jser-tag">치트 시트</span></p>

웹 접근성 치트시트

----
<h1 class="site-genre">소프트웨어, 툴, 라이브러리 관련</h1>

----

## cssnext
[cssnext.io/](http://cssnext.io/ "cssnext")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSS의 새로운 구문을 현재의 CSS로 변환하는 Transpiler 툴。
일부 스펙에 없는 확장구문도 포함하고 있다

- [cssnext에서 보는 차세대 CSS와 PostCSS | Yucchiy&#x27;s blog](http://blog.yucchiy.com/2015/04/22/cssnext-postcss-for-nextgeneration-of-css/ "cssnext에서 보는 차세대 CSS와 PostCSS | Yucchiy&#x27;s blog")

----

## TechnologyAdvice/Vers
[github.com/TechnologyAdvice/Vers](https://github.com/TechnologyAdvice/Vers "TechnologyAdvice/Vers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

버져닝을 가지는 모델 라이브러리

----

## Verify.js - A powerful, customizable, asynchronous form validation library
[verifyjs.com/](http://verifyjs.com/ "Verify.js - A powerful, customizable, asynchronous form validation library")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

비동기로 밸리데이션이 가능한 라이브러리

----

## Performance Tools | CSS-Tricks
[css-tricks.com/performance-tools/](https://css-tricks.com/performance-tools/ "Performance Tools | CSS-Tricks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

웹 사이트 퍼포먼스 측정에 관한 툴이나 서비스 정리

----
<h1 class="site-genre">서적 관련</h1>

----

## ECMAScript 2015… by Maciej Rzepiński [Leanpub PDF/iPad/Kindle]
[leanpub.com/ecmascript2015es6guide](https://leanpub.com/ecmascript2015es6guide "ECMAScript 2015… by Maciej Rzepiński \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">전자책</span></p>

ES6에 대한 전자책

- [Maciej Rzepiński — Medium](https://medium.com/@mrzepinski "Maciej Rzepiński — Medium")

----
