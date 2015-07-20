---
title: "2015-06-23 JS: ECMAScript 6 공개、SVG 가이드、JSConf US 2015"
author: azu
layout: post
date : 2015-06-23T21:06
translator: ChoEun
category: JSer
tags:
    - ES6
    - Promise
    - SVG
    - 동영상

---

JSer.info #233 - ECMAScript 2015(aka. ES6)가 Ecma 표준으로 승인되었습니다! :tada:

- [ECMAScript 2015 is now an Ecma Standard](https://esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard "ECMAScript 2015 is now an Ecma Standard")

[Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")에서 PDF와 HTML로 ES6 스펙을 공개하고 있습니다.
정식 스펙으로 공개하였기 때문에 브라우저에서 지원작업을 진행하고, 배우기 위한 리소스도 늘거라 생각합니다.

지금으로서는、[WEB+DB PRESS Vol.87](http://teppeis.hatenablog.com/entry/2015/06/webdb-press-es6-and-yapc-asia "WEB+DB PRESS Vol.87")에서 대략적인 느낌을 파악하고、
[http://es6-features.org/](http://es6-features.org/)에서 간단히 어떤 기능이 추가되었는가 확인한 뒤, [tower-of-babel](https://github.com/yosuke-furukawa/tower-of-babel "tower-of-babel")에서 실제로 작성해보면서、더 깊숙히 알고싶은 경우에는 [Exploring ES6](http://exploringjs.com/ "Exploring ES6")를 읽어보는 게 좋다고 생각합니다.

이전에 쓴, Promise 책도 업데이트했으니, Promise에 대해서는 이 책을 보시는게 좋을 거라 생각합니다.

- [ES6가 릴리즈 되었으니 Promise에 대해 공부해봅시다 | Web Scratch](http://efcl.info/2015/06/23/promises-book-v1.5/ "ES6가 릴리즈 되었으니 Promise에 대해 공부해봅시다 | Web Scratch")

----

[A Practical Guide to SVGs on the web](https://svgontheweb.com/ "A Practical Guide to SVGs on the web") 사이트 에서는、현재[대부분의 브라우저에서 지원하고 있다](http://caniuse.com/#feat=svg)고 SVG에 대해 작성하였습니다.

파일사이즈 최소화나 표시 방법, JavaScript나 CSS와 연동하는 방법에 대해서도 알기 쉽게 정리하고 있습니다.

----

[JSConf US 2015](http://2015.jsconf.us/ "JSConf US 2015 - The best conference for JS and the Web. Period") 동영상 일부가 공개되었습니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq" frameborder="0" allowfullscreen></iframe>

각각의 동영상에 자막이 있으니, 보고싶던 발표를 찾아보시는건 어떨까요. (역주: 일본어 자막입니다)

----

<h1 class="site-genre">헤드라인</h1>

----

## ECMAScript 2015 is now an Ecma Standard
[esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard](https://esdiscuss.org/topic/ecmascript-2015-is-now-an-ecma-standard "ECMAScript 2015 is now an Ecma Standard")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2015(ES6) 정식 릴리즈

- [ECMAScript 2015 Language Specification – ECMA-262 6th Edition](http://www.ecma-international.org/ecma-262/6.0/ "ECMAScript 2015 Language Specification – ECMA-262 6th Edition")

----

## babel/CHANGELOG.md at master · babel/babel
[github.com/babel/babel/blob/master/CHANGELOG.md#560](https://github.com/babel/babel/blob/master/CHANGELOG.md#560 "babel/CHANGELOG.md at master · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 5.6.0 릴리즈。
`--watch` 명령어를 실행할 때 파싱 에러가 나더라도 CLI를 정지하지 않도록 변경, transformer 일부를 plugin으로 분리하는 등의 변경이 있었습니다.

- [transformers](https://github.com/babel/babel/commit/3247851019dd350504689ad57c42ef45eb2381c7 "transformers")
- [Babel Plugins](https://github.com/babel-plugins "Babel Plugins")

----

## qooxdoo 5.0 released | qooxdoo News
[news.qooxdoo.org/qooxdoo-5-0-released](http://news.qooxdoo.org/qooxdoo-5-0-released "qooxdoo 5.0 released | qooxdoo News")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

JavaScript 기반 RIA 프레임워크 qooxdoo 5.0 릴리즈
qx.Website widgets 추가, MSEdge 대응, pointer event 등 대응,SVG, 풀 스크린 API 대응, WebDriver를 사용한 테스트 도입 등

----

## Node v0.12.5 (Stable)
[blog.nodejs.org/2015/06/22/node-v0-12-5-stable/](http://blog.nodejs.org/2015/06/22/node-v0-12-5-stable/ "Node v0.12.5 (Stable)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">보안</span> <span class="jser-tag">ReleaseNote</span></p>

Node v0.12.5 릴리즈

----

## Release JSHint 2.8.0 · jshint/jshint
[github.com/jshint/jshint/releases/tag/2.8.0](https://github.com/jshint/jshint/releases/tag/2.8.0 "Release JSHint 2.8.0 · jshint/jshint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JSHint 2.8.0 릴리즈
`module`에서 코드를 ES6 module로 간주하여 체크 가능하도록 변경, 버그 수정 등

----

## Node.js Foundation Advances Community Collaboration, Announces New Members and Ratified Technical Governance | The Linux Foundation
[www.linuxfoundation.org/news-media/announcements/2015/06/nodejs-foundation-advances-community-collaboration-announces-new](http://www.linuxfoundation.org/news-media/announcements/2015/06/nodejs-foundation-advances-community-collaboration-announces-new "Node.js Foundation Advances Community Collaboration, Announces New Members and Ratified Technical Governance | The Linux Foundation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js Foundation에 대한 공식 발표
Node.js와 io.js 머지나 기구모델에 대한 동의가 진행되어, Linux Foundation의 콜라보레이션 프로젝트로 Node.js Foundation가 탄생하였다.

- [Node.js Foundation이 커뮤니티 콜라보레이션을 진화: 새로운 멤버와 운용지침이 되는 기술 기구를 발표 | The Linux Foundation](http://www.linuxfoundation.jp/news-media/announcements/2015/06/jp_nodejs-foundation-advances-community-collaboration-announces-new "Node.js Foundation이 커뮤니티 콜라보레이션을 진화: 새로운 멤버와 운용지침이 되는 기술 기구를 발표 | The Linux Foundation")

----
<h1 class="site-genre">아티클</h1>

----

## Brendan Eich » Blog Archive » From ASM.JS to WebAssembly
[brendaneich.com/2015/06/from-asm-js-to-webassembly/](https://brendaneich.com/2015/06/from-asm-js-to-webassembly/ "Brendan Eich » Blog Archive » From ASM.JS to WebAssembly")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">asm.js</span> <span class="jser-tag">JavaScript</span></p>

브라우저를 위한 바이너리 포맷 표준화 프로젝트로 WebAssembly가 공개되었다. 사이즈나 디코드의 효율화를 목적으로 한 바이너리 포맷으로, 1단계 목표로 asm.js 바이너리 버전 정도의 기능을 예상하고 있다.
JavaScript를 옮겨놓는 게 아닌, JavaScript가 약한 부분을 보완 가능한 위치라는 등의 이야기가 [FAQ](https://github.com/WebAssembly/design/blob/master/FAQ.md "FAQ")에 써져있다.

- [주요 브라우저에서 실행 가능한 바이너리 형식 「WebAssembly」 개발 시작. Chrome、WebKit、Firefox、Microsoft Edge、LLVM、Unity가 지원할 의사를 표명 － Publickey](http://www.publickey1.jp/blog/15/webassembly.html "주요 브라우저에서 실행 가능한 바이너리 형식 「WebAssembly」 개발 시작. Chrome、WebKit、Firefox、Microsoft Edge、LLVM、Unity가 지원할 의사를 표명 － Publickey")
- [design/HighLevelGoals.md at master · WebAssembly/design](https://github.com/WebAssembly/design/blob/master/HighLevelGoals.md "design/HighLevelGoals.md at master · WebAssembly/design")
- [design/FAQ.md at master · WebAssembly/design](https://github.com/WebAssembly/design/blob/master/FAQ.md "design/FAQ.md at master · WebAssembly/design")
- [Rebuild: 97: Minimum Viable Standard (omo)](http://rebuild.fm/97/ "Rebuild: 97: Minimum Viable Standard (omo)")

----

## WebAssembly: a binary format for the web
[www.2ality.com/2015/06/web-assembly.html](http://www.2ality.com/2015/06/web-assembly.html "WebAssembly: a binary format for the web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span></p>

WebAssembly 개요 설명

----

## ES6 In Depth: Collections ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/06/es6-in-depth-collections/](https://hacks.mozilla.org/2015/06/es6-in-depth-collections/ "ES6 In Depth: Collections ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

Set와 Map에 대해서
각각의 메서드 설명, JS와 다른 언어에서 Map 특성 차이, 나열 순서 문제, WeakSet, WeakMap이 왜 필요한가에 대해서

----

## A Practical Guide to SVGs on the web
[svgontheweb.com/](https://svgontheweb.com/ "A Practical Guide to SVGs on the web")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">browser</span></p>

SVG 사용방법 가이드라인
최적화, 사용법, 표기방법을 정리, CSS나 JavaScript로 조작방법, 반응형, 애니메이션 등 SVG에 대해서 정리되어 있다.

----

## MIDI,JavaScript - JavaScript로 MIDI 파일을 해석해보자 1 - Qiita
[qiita.com/PianoScoreJP/items/2f03ae61d91db0334d45](http://qiita.com/PianoScoreJP/items/2f03ae61d91db0334d45 "MIDI,JavaScript - JavaScript로 MIDI 파일을 해석해보자 1 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">audio</span></p>

JavaScript로 MIDI 파일을 해석해서 헤더 정보나 트랙을 꺼내는 튜토리얼

----
<h1 class="site-genre">슬라이드, 동영상</h1>

----

## JSConf US 2015 - YouTube
[www.youtube.com/playlist?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq](https://www.youtube.com/playlist?list=PL37ZVnwpeshEkVjFZlLm1krvx0mPYPOoq "JSConf US 2015 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">동영상</span></p>

JSConf US 2015 동영상이 공개되었다.
각 동영상의 대본 gist도 공개되어있다.

- [JSConf US 2015 - The best conference for JS and the Web. Period](http://2015.jsconf.us/ "JSConf US 2015 - The best conference for JS and the Web. Period")
- [una/js-conf-notes](https://github.com/una/js-conf-notes "una/js-conf-notes")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## JavaScript Live
[jslive.com/](https://jslive.com/ "JavaScript Live")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

RubyFlow 같은 JavaScript 커뮤니티 뉴스 스타트

----

## JavaScript.com
[www.javascript.com/](https://www.javascript.com/ "JavaScript.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

CodeSchool에서 JavaScript 초보자를 위한 학습 리소스 소개, 커뮤니티에서 작성한 아티클 등을 소개하는 사이트

----

## Custom Elements - Explore the world of Web Components
[customelements.io/](https://customelements.io/ "Custom Elements - Explore the world of Web Components")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">검색</span></p>

Bower나 npm 키워드에서 web-components가 붙어있는 것만 검색할 수 있는 사이트

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## oceanhouse21/dokker
[github.com/oceanhouse21/dokker](https://github.com/oceanhouse21/dokker "oceanhouse21/dokker")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span></p>

JSDoc 코멘트를 통해 lodash 같은 문서 페이지/Markdown를 생성해주는 도구

----

## trueadm/t7
[github.com/trueadm/t7](https://github.com/trueadm/t7 "trueadm/t7")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">VirtualDOM</span></p>

Template Strings를 사용한 템플릿 라이브러리
결과를 React나 다른 virtual-dom 라이브러리를 사용한 것 기반으로 출력 가능하다.

----

## sighjs/sigh
[github.com/sighjs/sigh](https://github.com/sighjs/sigh "sighjs/sigh")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">gulp</span> <span class="jser-tag">Tools</span></p>

JavaScript 빌드 도구
gulp plugin을 지원하며, 기본적으로 병렬 태스크, incremental rebuild, Source Map 대응 등 다른 빌드 도구의 특징도 가지고 있다.
http://sighjs.github.io/

----

## eorroe/NodeList-Prototype-Extension
[github.com/eorroe/NodeList-Prototype-Extension](https://github.com/eorroe/NodeList-Prototype-Extension "eorroe/NodeList-Prototype-Extension")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

DOM Node Collection을 조작 가능한 라이브러리

----
