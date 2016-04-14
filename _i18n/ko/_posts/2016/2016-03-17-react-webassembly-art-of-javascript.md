---
title: "2016-03-17 JS: React.js v15.0 RC, WebAssembly, 근래의 JavaScript 도구/라이브러리"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-03-17T22:03
category: JSer
tags:
    - React
    - WebAssembly
    - JavaScript


---

JSer.info #270 - [React v15.0 RC2](https://facebook.github.io/react/blog/2016/03/16/react-v15-rc2.html "React v15.0 Release Candidate 2")가 릴리즈됐습니다.
RC2에서는 [RC1에서 발견한 버그](https://github.com/facebook/react/issues/6246)를 대응하고 SVG에 관한 변경 사항을 revert 했습니다.

RC1을 포함한 변경 사항이 아래 글에 정리돼 있으므로, React를 사용하고 있는 사람은 한번 읽어보시면 좋을 것 같습니다.

- [React.js v15.0 changes - blog.koba04.com](http://blog.koba04.com/post/2016/03/09/react-js-v15-changes/ "React.js v15.0 changes - blog.koba04.com")(일본어)

----

MSEdge([ChakraCore](https://github.com/microsoft/chakracore "ChakraCore")), Firefox, Chrome(V8)에서 각각 [WebAssembly](http://webassembly.github.io/ "WebAssembly")를 시험적으로 지원한다는 발표가 있었습니다.

- [V8 JavaScript Engine: Experimental support for WebAssembly in V8](http://v8project.blogspot.jp/2016/03/experimental-support-for-webassembly.html)
- [A WebAssembly Milestone: Experimental Support in Multiple Browsers ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/03/a-webassembly-milestone/) ([翻訳](https://www.mozilla.jp/blog/entry/10539/))
- [Previewing WebAssembly experiments in Microsoft Edge | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/03/15/previewing-webassembly-experiments/)

WebKit은, 특별히 별다른 발표는 없습니다만, 현재 [개발 중인 상태](https://webkit.org/status/#specification-webassembly "WebKit Feature Status | WebKit")로 [테스트 구현](http://trac.webkit.org/browser/trunk/Source/JavaScriptCore/wasm)을 하고 있습니다.

----

[State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium](https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b "State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium")에는 근래의 라이브러리나 도구의 전반적인 내용에 관해 정리돼 있습니다.

> If you don’t need it, don’t use it

라는 한마디가 잘 나타내듯이 모든 사람이 이 모두를 필요로 하는 상황은 없을 것이라고도 이야기하고 있습니다.

최근엔, 이와 같은 도구를 사용하는 추세가 되면서 [JavaScript fatigue fatigue ](http://www.2ality.com/2016/02/js-fatigue-fatigue.html "JavaScript fatigue")라는 글이 화제가 되기도 했습니다.

> Don’t try to know everything

모든 것을 사용해 볼 필요는 없이, [도구를 사용하지 않고 React를 시작하는 방법](https://medium.com/javascript-inside/learn-the-concepts-part-1-418952d968cb)(일본어) 등 여러가지 방식이나 의견도 이야기되고 있습니다.

피곤하지 않을 나름의 방식을 찾아가는 것이 좋다고 생각합니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## V8 JavaScript Engine: V8 Release 5.0
[v8project.blogspot.com/2016/03/v8-release-50.html](http://v8project.blogspot.com/2016/03/v8-release-50.html "V8 JavaScript Engine: V8 Release 5.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 5.0이 릴리즈됐습니다.
RegExp Unicode flag를 지원하고 RegExp의 well-known symbols를 지원합니다. 또, `Object.keys()`나 rest parameter의 속도가 개선됐습니다.

----

## Release v6.7.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.7.0](https://github.com/babel/babel/releases/tag/v6.7.0 "Release v6.7.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v6.7.0가 릴리즈됐습니다.
async/await 관련 버그가 수정됐고, AST 상에 존재했던 캐쉬를 WeakMap 기반으로 관리하도록 내부가 변경됐습니다.

----

## node/CHANGELOG.md at v5.8.0 · nodejs/node
[github.com/nodejs/node/blob/v5.8.0/CHANGELOG.md](https://github.com/nodejs/node/blob/v5.8.0/CHANGELOG.md "node/CHANGELOG.md at v5.8.0 · nodejs/node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.8.0이 릴리즈됐습니다.
`path.normalize`의 리그레션(regression)을 수정했고, `util.format`의 성능이 개선됐습니다.

- [Node 5.7.1 path.normalize broken · Issue #5585 · nodejs/node](https://github.com/nodejs/node/issues/5585 "Node 5.7.1 path.normalize broken · Issue #5585 · nodejs/node")
- [util: improve util.format performance by evanlucas · Pull Request #5360 · nodejs/node](https://github.com/nodejs/node/pull/5360 "util: improve util.format performance by evanlucas · Pull Request #5360 · nodejs/node")

----

## Node v5.9.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.9.0/](https://nodejs.org/en/blog/release/v5.9.0/ "Node v5.9.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.9.0가 릴리즈됐습니다.
`vm` 모듈의 메모리 사용량 이슈를 해결했고, `zlib` 모듈이 concatenated archives를 지원합니다.

----

## Release v1.5.0 · testem/testem
[github.com/testem/testem/releases/tag/v1.5.0](https://github.com/testem/testem/releases/tag/v1.5.0 "Release v1.5.0 · testem/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

testem v1.5.0이 릴리즈됐습니다.
여러개의 Test Page를 지정하여 parallel 실행 가능하도록 변경됐고, Mocha 테스트에 걸린 시간을 출력할 수 있게 변경됐습니다.

----

## React.js v15.0 changes - blog.koba04.com(일본어)
[blog.koba04.com/post/2016/03/09/react-js-v15-changes/](http://blog.koba04.com/post/2016/03/09/react-js-v15-changes/ "React.js v15.0 changes - blog.koba04.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React.js v15.0 RC의 변경 사항이 정리돼 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## A WebAssembly Milestone: Experimental Support in Multiple Browsers ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/03/a-webassembly-milestone/](https://hacks.mozilla.org/2016/03/a-webassembly-milestone/ "A WebAssembly Milestone: Experimental Support in Multiple Browsers ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">status</span></p>

WebAssembly의 사양, 브라우저의 구현 현황에 관해 작성돼 있습니다.
최초의 binary format 드래프트 사양이 발표됐고 Firefox, Chrome, ChackraCore의 Nightly에서 시험적으로 지원하고 있습니다.

- [V8 JavaScript Engine: Experimental support for WebAssembly in V8](http://v8project.blogspot.jp/2016/03/experimental-support-for-webassembly.html "V8 JavaScript Engine: Experimental support for WebAssembly in V8")
- [Previewing WebAssembly experiments in Microsoft Edge | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/03/15/previewing-webassembly-experiments/ "Previewing WebAssembly experiments in Microsoft Edge | Microsoft Edge Dev Blog")

----

## Firefox 개발자 도구를 사용한 Service Workers와 Push 디버깅 | Mozilla Developer Street (modest)(일본어)
[dev.mozilla.jp/2016/03/debugging-service-workers-and-push-with-firefox-devtools/](https://dev.mozilla.jp/2016/03/debugging-service-workers-and-push-with-firefox-devtools/ "Firefox 개발자 도구를 사용한 Service Workers와 Push 디버깅 | Mozilla Developer Street (modest)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">ServiceWorker</span></p>

Firefox에서 Service Worker와 Push Notifications을 디버깅하는 방법에 관해 작성돼 있습니다.
`about:debugging`이라는 디버깅 대시보드에 관해서도 작성돼 있습니다.

----

## State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium
[medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b](https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b "State of the Art JavaScript in 2016 — JavaScript and Opinions — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

근래 JavaScript에서 주류가 된 라이브러리와 도구에 관해 작성돼 있습니다.
React, Redux, Babel, ESLint, npm, webpack, mocha 등 테스트 도구 뿐만 아니라 개인의 철학에 관해서도 이야기합니다.

> If you don’t need it, don’t use it

라고 이야기하는 것 처럼 모든 상황에 만능 키가 되는 것은 없다는 이야기도 하고 있습니다.

----

## Learning React Without Using React Part 1 — JavaScript Inside — Medium
[medium.com/javascript-inside/learn-the-concepts-part-1-418952d968cb](https://medium.com/javascript-inside/learn-the-concepts-part-1-418952d968cb "Learning React Without Using React Part 1 — JavaScript Inside — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

별다른 도구를 사용하지 않고 React를 개발하는 과정에 관한 연재 글입니다.

----

## Webpack FTW!!!!
[k94n.com/webpack-ftw](https://k94n.com/webpack-ftw "Webpack FTW!!!!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack의 기능을 알기 쉽게 간단하게 소개하는 글입니다.

- [Webpack FTW // Speaker Deck](https://speakerdeck.com/k9ordon/webpack-ftw "Webpack FTW // Speaker Deck")

----

## 특집：C#×JavaScript：ECMAScript의 최신 정보를 얻으려면 (1/2) - ＠IT(일본어)
[www.atmarkit.co.jp/ait/articles/1603/11/news042.html](http://www.atmarkit.co.jp/ait/articles/1603/11/news042.html "특집：C#×JavaScript：ECMAScript의 최신 정보를 얻으려면 (1/2) - ＠IT")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span></p>

ECMAScript의 사양 책정의 프로세스나 관련 리소스를 어디에서 찾아볼 수 있는지 정리돼 있습니다.

----

## Jest | &quot;JavaScript Unit Testing Performance&quot;
[facebook.github.io/jest/blog/2016/03/11/javascript-unit-testing-performance.html](http://facebook.github.io/jest/blog/2016/03/11/javascript-unit-testing-performance.html "Jest | "JavaScript Unit Testing Performance"")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

테스트 프레임워크 Jest가 실행 시간을 개선하기 위해 하고 있는 일에 관해서 작성돼 있습니다.

----

## JavaScript Proposal for weak references: WeakRef
[ponyfoo.com/articles/weakref](https://ponyfoo.com/articles/weakref "JavaScript Proposal for weak references: WeakRef")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">proposal</span></p>

`WeakRef` Proposal에 관해 설명합니다.
WeakMap과 마찬가지로 Weak한 용도지만, WeakMap과 다르게 GC에서 회수할 때 호출되는 `executor`를 지정할 수 있습니다(WeakMap/Set은 GC에서 회수하는 시점을 알 수 없습니다).

- [proposal-weakrefs/weakrefs.md at master · tc39/proposal-weakrefs](https://github.com/tc39/proposal-weakrefs/blob/master/specs/weakrefs.md "proposal-weakrefs/weakrefs.md at master · tc39/proposal-weakrefs")

----

## Node.js Buffer API Changes — Medium
[medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97](https://medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97 "Node.js Buffer API Changes — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span></p>

Node.js v6에서 예정돼 있는 Buffer API의 변경에 관해 설명합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Fluent Conference 2016 (San Francisco, CA) - YouTube
[www.youtube.com/watch?v=9UYoKyuFXrM&amp;list=PL055Epbe6d5bQubu5EWf\_kUNA3ef\_qbmL](https://www.youtube.com/watch?v=9UYoKyuFXrM&amp;list=PL055Epbe6d5bQubu5EWf_kUNA3ef_qbmL "Fluent Conference 2016 (San Francisco, CA) - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">영상</span></p>

Fluent Conference 2016의 영상이 공개돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## PostCSS.parts | A searchable catalog of PostCSS plugins
[postcss.parts/](http://postcss.parts/ "PostCSS.parts | A searchable catalog of PostCSS plugins")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span> <span class="jser-tag">검색</span></p>

PostCSS의 카탈로그 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Introducing InversifyJS 2.0
[blog.wolksoftware.com/introducing-inversify-2](http://blog.wolksoftware.com/introducing-inversify-2 "Introducing InversifyJS 2.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Inversion of control (IoC) 컨테이너의 TypeScript 용 라이브러리입니다.

----

## rajasegar/compack: An awesome bundler for Web Components
[github.com/rajasegar/compack](https://github.com/rajasegar/compack "rajasegar/compack: An awesome bundler for Web Components")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">Tools</span></p>

Web Components를 scaffolding 및 bundle을 할 수 있는 도구입니다.

----

## eanplatter/enclave: A simpler way to compile React applications http://enclave.js.org
[github.com/eanplatter/enclave](https://github.com/eanplatter/enclave "eanplatter/enclave: A simpler way to compile React applications http://enclave.js.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">Tools</span></p>

`npm install`로써 `npm start`하는 것으로, React + Babel 환경을 셋팅할 수 있는 부트스트랩 적인 도구입니다.

----
