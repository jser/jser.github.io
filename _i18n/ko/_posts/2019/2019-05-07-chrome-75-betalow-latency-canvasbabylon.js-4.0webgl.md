---
title: "2019-05-07: Chrome 75 Beta(Low Latency Canvas), Babylon.js 4.0(WebGL)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-05-07T01:19:40.127Z
category: JSer
tags:
- Chrome
- WebGL
- gulp

---

JSer.info #434 - Chrome 75 베타 버전이 릴리스됐습니다.

- [Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators](https://blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html)
- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D75)

Canvas Context에 저지연(low latency) 렌더링을 위한 `desynchronized` 옵션이 추가됐습니다.
`desynchronized` 옵션은 아래 문서에 잘 소개돼 있으니 참고하시기 바랍니다.

- [Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/05/desynchronized) 
- [Add a low latency mode for OffscreenCanvas · Issue #2659 · whatwg/html](https://github.com/whatwg/html/issues/2659)

Web Share API에서 파일을 지원하며 ES Proposal의 [Numeric separators](https://github.com/tc39/proposal-numeric-separator)를 지원합니다.
또, CSP의 디렉티브 `script-src-attr`, `script-src-elem`, `style-src-attr`, `style-src-elem` 등 4개가 추가됐습니다.
[HTMLVideoElement.playsInline](https://www.chromestatus.com/feature/Discussion%20to%20add%20it%20to%20spec:%20https://github.com/whatwg/html/issues/1237)와 Cache-Control의 `stale-while-revalidate` 등도 지원합니다.

`stale-while-revalidate`에 대해서는 아래 문서를 참고하시기 바랍니다.

- [What stale-while-revalidate provides is a grace period (defined by us) in which the browser is permitted to use an out of date (stale) asset while we’re checking for a newer version.](https://csswizardry.com/2019/03/cache-control-for-civilians/)

----

WebGL 기반의 3D 게임 프레임워크인 Babylon.js 4.0이 릴리스됐습니다.

- [Babylon.js 4.0 Is Here! – Babylon.js – Medium](https://medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b)
- [Release 4.0.0 · BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js/releases/tag/v4.0.0)

Visual Scene Inspector가 추가돼 [inspector](https://doc.babylonjs.com/features/playground_debuglayer)의 디버깅 기능이 한층 강화됐습니다.
또, 번들 시 불필요한 모듈이 제거되도록 개선됐습니다.

- [ES6 - Babylon.js Documentation](https://doc.babylonjs.com/features/es6_support)

이어 성능 개선이 이뤄졌고 물리 엔진인 [ammo.js](https://github.com/kripken/ammo.js/)를 지원합니다.

- [Use a Physics Engine - Babylon.js Documentation](https://doc.babylonjs.com/how_to/using_the_physics_engine)

----

<h1 class="site-genre">헤드라인</h1>

----

## jQuery 3.4.1: triggering focus events in IE and finding root elements in iOS 10 | Official jQuery Blog
[blog.jquery.com/2019/05/01/jquery-3-4-1-triggering-focus-events-in-ie-and-finding-root-elements-in-ios-10/](http://blog.jquery.com/2019/05/01/jquery-3-4-1-triggering-focus-events-in-ie-and-finding-root-elements-in-ios-10/ "jQuery 3.4.1: triggering focus events in IE and finding root elements in iOS 10 | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.4.1이 릴리스됐습니다.
IE10-IE11에서의 `trigger` 문제, iOS 10.0-10.2에서의 click 문제, AMD로 jQuery를 불러올 때 발생하는 문제 등이 수정됐습니다.


----

## Release Notes for Safari Technology Preview 81 | WebKit
[webkit.org/blog/8834/release-notes-for-safari-technology-preview-81/](https://webkit.org/blog/8834/release-notes-for-safari-technology-preview-81/ "Release Notes for Safari Technology Preview 81 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 81 릴리스됐습니다.
인쇄 용 스타일로 `@page`에 의한 margin을 지원하며 `frame-ancestors` CSP를 `X-Frame-Options` 헤더 보다 더 우선하도록 변경됐고 `requestAnimationFrame`의 실행 시점 문제가 수정됐습니다.

- [177484 – requestAnimationFrame should execute before the next frame](https://bugs.webkit.org/show_bug.cgi?id=177484 "177484 – requestAnimationFrame should execute before the next frame")

----

## Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators
[blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html](https://blog.chromium.org/2019/05/chrome-75-beta-low-latency-canvas.html "Chromium Blog: Chrome 75 Beta: low latency canvas contexts, sharing files, and numeric separators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 75 베타가 릴리스됐습니다.
Canvas에 저지연 렌더링을 위한 `desynchronized` 옵션 추가, Web Share에서 파일 지원, ES Proposal의 Numeric separators를 지원합니다.
CSP의 `script-src-attr` 디렉티브와 Cache-Control의 `stale-while-revalidate`를 지원합니다.

- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D75 "Chrome Platform Status")
- [Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/05/desynchronized "Low-latency rendering with the desynchronized hint  |  Web  |  Google Developers")

----

## Release 7.0.0 · websockets/ws
[github.com/websockets/ws/releases/tag/7.0.0](https://github.com/websockets/ws/releases/tag/7.0.0 "Release 7.0.0 · websockets/ws")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebSocket 클라이언트 & 서버 `ws` 7.0.0이 릴리스됐습니다.
Node.js 6 지원을 종료했고 생성자에서 Node.js의 `url` 객체가 아닌 `URL` 객체를 전달받도록 변경됐습니다.
`readyState`가 `OPEN`이 아닌 경우의 `ping`, `pong` 동작이 변경됐습니다.


----

## Release v4.0.0 · facebook/relay
[github.com/facebook/relay/releases/tag/v4.0.0](https://github.com/facebook/relay/releases/tag/v4.0.0 "Release v4.0.0 · facebook/relay")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

GraphQL과 React 용 프레임워크인 Relay 4.0.0이 릴리스됐습니다.
Container의 인수로 `graphql` tag를 전달하는게 아닌 객체를 전달하도록 변경됐고 client schema extensions를 모두 지원합니다.

- [Building the New facebook.com with React, GraphQL and Relay](https://developers.facebook.com/videos/2019/building-the-new-facebookcom-with-react-graphql-and-relay/ "Building the New facebook.com with React, GraphQL and Relay")

----

## Microsoft Edge – All the news from Build 2019 - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/05/06/edge-chromium-build-2019-pwa-ie-mode-devtools/](https://blogs.windows.com/msedgedev/2019/05/06/edge-chromium-build-2019-pwa-ie-mode-devtools/ "Microsoft Edge – All the news from Build 2019 - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">IE</span> <span class="jser-tag">news</span></p>

Chromium 기반의 MSEdge에는 서드 파티 트레킹의 블록이 가능한 Privacy Tools와 방문한 사이트를 자동으로 IE 호환 모드로 실행하는 기능이 탑재될 예정입니다.


----

## Babylon.js 4.0 Is Here! – Babylon.js – Medium
[medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b](https://medium.com/@babylonjs/babylon-js-4-0-is-here-d725b5b02e9b "Babylon.js 4.0 Is Here! – Babylon.js – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebGL 기반 3D 게임 프레임워크 Babylon.js 4.0.0이 릴리스됐습니다. Visual Scene Inspector 도입, 파일 크기와 성능의 개선, 물리 엔진인 Ammo.js를 지원합니다.


----

## Hyper Blog
[hyper.is/blog](https://hyper.is/blog "Hyper Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">console</span> <span class="jser-tag">software</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 기반의 터미널 애플리케이션인 Hyper 3가 릴리스됐습니다. `hterm`에서 `xterm.js`으로 변경하여 WebGL Renderer를 사용하도록 개선됐으며 IPC의 배치 처리를 이용해 성능을 개선했습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Stub navigator API in end-to-end tests | Better world by better software
[glebbahmutov.com/blog/stub-navigator-api/](https://glebbahmutov.com/blog/stub-navigator-api/ "Stub navigator API in end-to-end tests | Better world by better software")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Cypress를 사용해 Battery status API을 Stub하여 테스트하는 방법을 소개하는 튜토리얼 글입니다.
`navigator`를 어떻게 stub해 테스트할 수 있는지 소개합니다.


----

## The CSS Handbook: a handy guide to CSS for developers
[medium.freecodecamp.org/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11](https://medium.freecodecamp.org/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11 "The CSS Handbook: a handy guide to CSS for developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS를 주제로한 가이드 문서입니다.
기본적인 CSS의 속성 소개부터 unit, 레이아웃, 애니메이션 등 CSS와 관련한 기술이 폭넓게 정리돼 있습니다.


----

## Revisiting prefers-reduced-motion, the reduced motion media query | CSS-Tricks
[css-tricks.com/revisiting-prefers-reduced-motion-the-reduced-motion-media-query/](https://css-tricks.com/revisiting-prefers-reduced-motion-the-reduced-motion-media-query/ "Revisiting prefers-reduced-motion, the reduced motion media query | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">animation</span> <span class="jser-tag">article</span> <span class="jser-tag">accessibility</span></p>

CSS의 `prefers-reduced-motion` 미디어쿼리에 대한 소개와 사용 방법이 작성돼 있습니다.
접근성, 프로그레시브/인핸스먼트(enhancement)에 대한 생각, CSS Variables을 조합한 구현 방법 등을 소개합니다.


----

## Optimizing Performance With Resource Hints — Smashing Magazine
[www.smashingmagazine.com/2019/04/optimization-performance-resource-hints/](https://www.smashingmagazine.com/2019/04/optimization-performance-resource-hints/ "Optimizing Performance With Resource Hints — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

Resource Hints에 관한 소개글입니다.
`dns-prefetch`, `preconnect`, `prefetch`, `prerender`를 각각 어떤 경우에 이용하는지 그리고 `as` 속성에 대해 작성돼 있습니다.


----

## gulp4 재입문 gulpfile의 분할과 node 모듈 이용 - Qiita(일본어)
[qiita.com/masato\_makino/items/ad11058e1a8a009abbdf](https://qiita.com/masato_makino/items/ad11058e1a8a009abbdf "gulp4 재입문 gulpfile의 분할과 node 모듈 이용 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">gulp</span> <span class="jser-tag">article</span></p>

gulp4 기반 입문 글입니다.
gulp task 정의 방법, 태스크 파일의 분리, gulp 플러그인과 Node 모듈에 대해서 이야기합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## oclif/cli-ux: CLI IO utilities
[github.com/oclif/cli-ux](https://github.com/oclif/cli-ux "oclif/cli-ux: CLI IO utilities")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

터미널 CLI 인터페이스를 만들 수 있는 Node.js 라이브러리입니다.
prompt나 confirm 등의 대화형 조작, URL 링크 출력, spinner, 애너테이션, table 출력 등을 지원합니다.


----

## Laconia · Create well-crafted serverless applications, effortlessly
[laconiajs.io/](https://laconiajs.io/ "Laconia · Create well-crafted serverless applications, effortlessly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Node.js의 serverlsss 프레임워크 입니다. Hexagonal Architecture 기반으로 의존을 외부에서 주입할 수 있는 구조로 테스트하기 쉽게 돼 있습니다.
Long Task 용 배치 처리하는 모듈도 지원합니다.


----

## microsoft/react-native-windows: A framework for building native Windows apps with React.
[github.com/Microsoft/react-native-windows](https://github.com/Microsoft/react-native-windows "microsoft/react-native-windows: A framework for building native Windows apps with React.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">windows</span> <span class="jser-tag">library</span></p>

React Native for Windows.
React Native로 네이티브 Windows 애플리케이션(UWP)를 개발할 수 있는 프레임워크입니다.


----
