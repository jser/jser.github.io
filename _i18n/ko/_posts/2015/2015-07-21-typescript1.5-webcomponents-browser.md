---
title: "2015-07-21 JS: TypeScript 1.5, Web Components 개요, 브라우저 공식 사이트 모음"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-07-21T22:54
category: JSer
tags:
    - TypeScript
    - WebCompoents
    - Browser

---

JSer.info #237 -  [TypeScript 1.5](https://github.com/Microsoft/TypeScript/releases/tag/v1.5.3 "TypeScript 1.5")가 릴리즈 됐습니다.

- [Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs](http://blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx "Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs")

새로운 기능에 대한 소개는 [What's new in TypeScript](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-15 "What's new in TypeScript")에 정리돼 있습니다. 간단히 말해 이번 버전에서 ES6와 관련한 modules, destructuring, spread, for/of, symbols, computed properties, let, const 등의 구문을 지원합니다.

또 TypeScript의 기능으로는 `--module umd`나 `--module system`으로 지원하는 모듈의 종류 추가, `--inlineSourceMap`으로 인라인 SourceMap 지원, `--experimentalDecorators`의 플래그로 Decorator의 지원 등이 추가 됐습니다.

기존의 구문이나 Compiler API의 대대적인 변경 내용은 아래에 정리돼 있습니다.

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-15 "Breaking Changes · Microsoft/TypeScript Wiki")
- [API Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/API-Breaking-Changes#typescript-15 "API Breaking Changes · Microsoft/TypeScript Wiki")

[TypeScript 1.5.3 변경 사항 - Qiita](http://qiita.com/vvakame/items/9b9fde6c71aae6a824c0 "TypeScript 1.5.3 변경 사항 - Qiita")(일본어)에도 변경 사항이 자세히 작성돼 있으므로 함께 읽어보면 좋을 것 같습니다.

-----

[Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog](http://blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/ "Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog")에 Web Components에 의해 무엇이 달라지는지 자세히 작성돼 있습니다.

Web Components가 어떤 문제를 해결해주는지, 이미 있었던 유사한 구현 등 역사에 대해, 기존의 구현에서는 무엇을 해결 못했었는지, 현재 Web Components의 상황 등에 관해 작성돼 있습니다.

또, [Microsoft Edge and Web Components | Microsoft Edge Dev Blog](http://blogs.windows.com/msedgedev/2015/07/15/microsoft-edge-and-web-components/ "Microsoft Edge and Web Components | Microsoft Edge Dev Blog")에는 MSEdge에서의 Web Components 구현 방침에 관해서 작성돼 있습니다.

----

위의 MSEdge의 이야기가 그렇듯이 최근에 브라우저 벤더들이 다양한 정보를 공개하고 있습니다.

공식 정보만 취하려고 하더라도 여러 사이트에 작성돼 있기 때문에 정보를 찾아 보기가 꽤 어렵습니다.

그런 공식 사이트 정보를 [azu/browser-javascript-resource](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource")에 정리했습니다.

- [브라우저 별 릴리즈 노트나 구현 상황을 어디에서 보면 좋을지를 정리했습니다 | Web Scratch](http://efcl.info/2015/07/21/browser-javascript-resource/ "브라우저 별 릴리즈 노트나 구현 상황을 어디에서 보면 좋을지를 정리했습니다")(일본어)

[변화를 만드는 사람이 모이는 장소에는 자연스럽게 정보가 모이므로](http://azu.github.io/slide/jser200/javascript-2014.html) 브라우저 벤더가 공개하는 정보만 봐도 꽤 폭넓은 정보를 얻을 수 있다고 생각합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## V8 JavaScript Engine: V8 4.5 release
[v8project.blogspot.com/2015/07/v8-45-release.html](http://v8project.blogspot.com/2015/07/v8-45-release.html "V8 JavaScript Engine: V8 4.5 release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.5(Chrome 45)가 릴리즈 됐습니다.
Arrow Function, Array/TypedArray의 메소드 및 Object.assign가 추가됐고 새로운 최적화 컴파일러로 TurboFan을 도입했습니다. 또, V8 API 등이 변경됐습니다.

----

## ESLint 1.0.0-rc-1 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/07/eslint-1.0.0-rc-1-released](http://eslint.org/blog/2015/07/eslint-1.0.0-rc-1-released "ESLint 1.0.0-rc-1 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 1.0.0-rc-1이 릴리즈 됐습니다.
`--reset`이 기본(default)으로 변경됐으며, ES6의 지원을 개선, 새로운 규칙이 추가 되는 등 다양한 변경 사항이 있습니다.

- [Documentation - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/1.0.0/user-guide/migrating-to-1.0.0 "Documentation - ESLint - Pluggable JavaScript linter")

----

## Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx](http://blogs.msdn.com/b/typescript/archive/2015/07/20/announcing-typescript-1-5.aspx "Announcing TypeScript 1.5 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.5가 릴리즈 됐습니다.
modules나 destructuring 등 ES6 지원을 개선했고 tsconfig.json를 이용해 프로젝트를 설정할 수 있습니다. 또한 `--experimentalDecorators` 플러그로 Decorator를 시험적으로 지원합니다.

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#15 "Roadmap · Microsoft/TypeScript Wiki")
- [TypeScript 1.5.3 변경 사항 - Qiita](http://qiita.com/vvakame/items/9b9fde6c71aae6a824c0 "TypeScript 1.5.3 변경 사항 - Qiita")(일본어)

----

## node-browserify/changelog.markdown at master · substack/node-browserify
[github.com/substack/node-browserify/blob/master/changelog.markdown#1100](https://github.com/substack/node-browserify/blob/master/changelog.markdown#1100 "node-browserify/changelog.markdown at master · substack/node-browserify")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 11.0.0이 릴리즈됐습니다.
브라우저용 stream으로 사용하는 readable-stream을 업데이트하고 Stream3 기반으로 변경했습니다.
브라우저용 `http` 모듈을 Fetch API를 기반으로한 stream-http로 변경하고 stream을 지원할 수 있도록 했습니다.

- [nodejs/readable-stream](https://github.com/nodejs/readable-stream "nodejs/readable-stream")
- [jhiesey/stream-http](https://github.com/jhiesey/stream-http "jhiesey/stream-http")

----
<h1 class="site-genre">아티클</h1>

----

## Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/](http://blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/ "Bringing componentization to the web: An overview of Web Components | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">MSEdge</span> <span class="jser-tag">browser</span></p>

Web Components에 관해 자세히 설명하고 있습니다.
어떤 목적이 있는지, 관련된 컴포넌트 구현의 역사 등을 소개합니다.
CSS 스타일의 isolation, 스타일의 스코프, Global object isolation, iframe에 부족한 부분 등을 설명합니다.

----

## Socket.IO — Socket.IO P2P
[socket.io/blog/socket.io-p2p/#](http://socket.io/blog/socket.io-p2p/# "Socket.IO — Socket.IO P2P")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">p2p</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Socket.IO에서 WebRTC를 이용한 P2P 통신 방법이 작성돼 있습니다.

----

## Comprehensive Beginner&#x27;s Guide To ReactJS - AntJanus
[antjanus.com/blog/web-development-tutorials/front-end-development/comprehensive-beginners-guide-to-reactjs/](http://antjanus.com/blog/web-development-tutorials/front-end-development/comprehensive-beginners-guide-to-reactjs/ "Comprehensive Beginner's Guide To ReactJS - AntJanus")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">React</span></p>

AngularJS 사용자를 위한 React.js 입문 가이드입니다.

----

## How to Debug JavaScript Remotely With Vorlon.js - Tuts+ Code Tutorial
[code.tutsplus.com/tutorials/how-to-debug-javascript-remotely-with-vorlonjs--cms-24343](http://code.tutsplus.com/tutorials/how-to-debug-javascript-remotely-with-vorlonjs--cms-24343 "How to Debug JavaScript Remotely With Vorlon.js - Tuts+ Code Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">tutorial</span></p>

Vorlon.js를 사용한 JavaScript 원격 디버깅을 소개합니다.

----

## ES6 In Depth: Proxies ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/07/es6-in-depth-proxies-and-reflect/](https://hacks.mozilla.org/2015/07/es6-in-depth-proxies-and-reflect/ "ES6 In Depth: Proxies ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Proxy API에 관해 설명합니다.
Proxy로 다루는 14개의 인터널 메서드, Proxy를 사용하는 곳, Revocable proxyies 등이 작성돼 있습니다.
"객체는 프로퍼티의 집합이다"라고 말할 수 있는지 이야기합니다.

----

## StrongLoop | An Introduction to JavaScript ES6 Iterators
[strongloop.com/strongblog/introduction-to-es6-iterators/](https://strongloop.com/strongblog/introduction-to-es6-iterators/ "StrongLoop | An Introduction to JavaScript ES6 Iterators")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 Iterator에 관해 설명합니다.
for-of와 for-in의 차이, Symbol.iterator로 정의하고 사용하는 방법을 소개합니다.

----

## azu/browser-javascript-resource
[github.com/azu/browser-javascript-resource](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">blog</span> <span class="jser-tag">まとめ</span></p>

IE나 Firefox 등의 브라우저별 릴리즈 노트나 변경 몇 구현 상황, 버그 리포트의 방법 등을 어느 사이트에서 보면 좋은지 정리했습니다.

- [브라우저 별 릴리즈 노트나 구현 상황을 어디에서 보면 좋을지를 정리했습니다 | Web Scratch](http://efcl.info/2015/07/21/browser-javascript-resource/ "브라우저 별 릴리즈 노트나 구현 상황을 어디에서 보면 좋을지를 정리했습니다 | Web Scratch")(일본어)

----

## 모르면 손해보는 Sass의 내장 함수 완벽 해부 | Yuhiisk(일본어)
[blog.yuhiisk.com/archive/2015/07/14/sass-built-in-functions.html](http://blog.yuhiisk.com/archive/2015/07/14/sass-built-in-functions.html "모르면 손해보는 Sass의 내장 함수 완벽 해부 | Yuhiisk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">リファレンス</span></p>

Sass의 함수가 정리돼 있습니다.

----

## Flux in Depth. Store and Network Communication. – Minko Gechev&#x27;s blog
[blog.mgechev.com/2015/07/18/flux-in-depth-store-network-communication-services](http://blog.mgechev.com/2015/07/18/flux-in-depth-store-network-communication-services "Flux in Depth. Store and Network Communication. – Minko Gechev's blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

Flux 아키텍체에서의 객체 네트워크를 포함한 데이터 흐름에 관해 설명합니다.
Store -> View, View -> Store 까지의 흐름, 모델과 State의 분리, 
Network -> UI 또는 UI -> Network의 패턴에 관해 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## An Introduction to Browser Rendering - YouTube
[www.youtube.com/watch?v=n1cKlKM3jYI](https://www.youtube.com/watch?v=n1cKlKM3jYI "An Introduction to Browser Rendering - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">영상</span></p>

브라우저 랜더링 흐름을 설명하는 스크린 캐스트입니다.

----
<h1 class="site-genre">소프트웨어, 툴, 라이브러리</h1>

----

## nikgraf/belle
[github.com/nikgraf/belle/](https://github.com/nikgraf/belle/ "nikgraf/belle")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

React Component로 개발된 UI Kit
JavaScript 리터럴 객체를 이용해 스타일을 커스텀할 수 있습니다.

----

## ipselon/react-ui-builder
[github.com/ipselon/react-ui-builder](https://github.com/ipselon/react-ui-builder "ipselon/react-ui-builder")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span></p>

React Component를 GUI로 일정한 자리에 알맞게 두거나, 지정한 UI 형태로 React.js의 코드를 얻고 GUI에서 코드를 편집하고 프리뷰 등이 가능한 도구입니다.
도구 자체가 React.js와 Proxy로 개발돼 있어 재미있습니다.

----
<h1 class="site-genre">도서</h1>

----

## DrBoolean/mostly-adequate-guide
[github.com/DrBoolean/mostly-adequate-guide](https://github.com/DrBoolean/mostly-adequate-guide "DrBoolean/mostly-adequate-guide")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">함수형 프로그래밍</span></p>

JavaScript의 함수형 프로그래밍에 관한 무료 서적입니다.

----

## JavaScript Regular Expressions - O&#x27;Reilly Media
[shop.oreilly.com/product/9781783282258.do](http://shop.oreilly.com/product/9781783282258.do "JavaScript Regular Expressions - O'Reilly Media")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">정규표현식</span> <span class="jser-tag">book</span></p>

JavaScript의 정규표현식에 관한 도서입니다.

----
