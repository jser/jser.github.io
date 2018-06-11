---
title: "2018-06-05 JS: Safari 12 변경 예정 사항, Jest 23, sucrase"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-06-05T00:34:04.007Z
category: JSer
tags:
- safari
- jest
- babel
- transpiler

---

JSer.info #386 - iOS 12, macOS 10.14에 탑재 될 Safari 12의 변경 예정 사항 릴리스 노트가 공개됐습니다.

- [What’s New in Safari - Apple Developer](https://developer.apple.com/safari/whats-new/)

`font-display` 지원, [Intelligent Tracking Prevention 2.0](https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/), [Cross-Origin Read Blocking (CORB)](https://chromium.googlesource.com/chromium/src/+/master/services/network/cross_origin_read_blocking_explainer.md) 일부 지원, 또 Password AutoFill 관한 기능이 추가됐습니다.

얼마전 릴리스 된 [Safari Technology Preview 57](https://webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/)에도 `Cross-Origin-Options` HTTP response header라고 하는 크로스 오리진에 관한 시큐리티 헤더가 시험적으로 구현됐습니다.

- [Safari TP 57의 Cross-Origin-Options HTTP response header에 관해](https://gist.github.com/azu/842e5d8d9fe1767dfbbd4238e7a19fad)(일본어)

----

JavaScript 테스트 프레임워크 Jest 23이 릴리스 됐습니다.

- [Jest 23: 🔥 Blazing Fast Delightful Testing · Jest](https://facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html)

Interactive Snapshot Mode와 `toStrictEqual` 등의 matcher가 추가됐으며 비동기적 커스텀 matcher를 작성할 수 있도록 변경됐고 `jest-each`가 코어에 포함됐습니다.

또, 테스트가 행에 걸렸을때 디버깅을 보조하는 [--detectOpenHandles](https://facebook.github.io/jest/docs/en/cli.html#detectopenhandles) 옵션도 추가됐습니다.

----

[sucrase](https://github.com/alangpierce/sucrase)라는 TypeScript, Flow, JSX와 일부 ES.next 기능의 변환에 한정된 Transpiler가 공개됐습니다. Babel과 다르게 ES2015+를 ES5로 변한하는게 아닌, ES2015+를 그대로 실행할 수 있는 환경을 고려한 모듈이나 TypeScript, Flow, JSX 등을 빠르게 JavaScript로 변환하는 것을 목적으로 하고 있습니다.

- website: <https://sucrase.io/>

Babel 파서를 포크한 것을 사용하고 TypeScript 등도 [@babel/preset-typescript](https://github.com/babel/babel/tree/master/packages/babel-preset-typescript)와 같이 타입 정보를 제외하고 JavaScript로 변환합니다(타입 체크는 하지 않습니다).

[Motivation](https://github.com/alangpierce/sucrase#motivation)에도 써있듯 Babel과는 다르게 AST 까지는 생성하지 않고 token 레벨에서 코드를 변환합니다.
따라서, Babel 처럼 AST 플러그인은 지원하지 않지만 단계가 줄어 좀 더 빠르게 코드를 변환할 수 있습니다.

- Babel: Source -> Token -> AST -> Transform -> AST -> Source
- sucrase: Source -> Token -> Transform -> Source

----

<h1 class="site-genre">헤드라인</h1>

----

## New in Chrome 67  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/nic67](https://developers.google.com/web/updates/2018/05/nic67 "New in Chrome 67  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 67이 릴리스 됐습니다.
Desktop PWA, Generic Sensor API, `BigInt`를 지원하며 개발자 도구가 업데이트 됐습니다.

----

## Announcing TypeScript 2.9 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/05/31/announcing-typescript-2-9/](https://blogs.msdn.microsoft.com/typescript/2018/05/31/announcing-typescript-2-9/ "Announcing TypeScript 2.9 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.9가 릴리스 됐습니다.
`import()` type 추가됐고 JSON 파일을 import 한 경우에 타입 추론이 이루어 지도록 변경됐으며 Tagged Template String 타입 개선 등이 이뤄졌습니다.

- [TypeScript 2.9 변경 사항 - Qiita](https://qiita.com/utatti/items/9f6c60f11620f7df50c0 "TypeScript 2.9 변경 사항 - Qiita")(일본어)
- [TypeScript 2.9.1 변경 사항 - Qiita](https://qiita.com/vvakame/items/0b22e5e34023e4c5d074 "TypeScript 2.9.1 변경 사항 - Qiita")(일본어)

----

## Release 1.0.0-beta.5 · avajs/ava
[github.com/avajs/ava/releases/tag/v1.0.0-beta.5](https://github.com/avajs/ava/releases/tag/v1.0.0-beta.5 "Release 1.0.0-beta.5 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 1.0.0-beta.5가 릴리스 됐습니다.
`ava.config.js` 설정 파일과 `t.throws`에서 `code` 프로퍼티를 지원합니다.

----

## Release 8.6 “Follow Reason” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/8.6.0](https://github.com/postcss/autoprefixer/releases/tag/8.6.0 "Release 8.6 “Follow Reason” · postcss/autoprefixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Autoprefixer 8.6이 릴리스 됐습니다.
CSS Grid의 `gap` 등을 지원합니다.

----

## Release Notes for Safari Technology Preview 57 | WebKit
[webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/](https://webkit.org/blog/8307/release-notes-for-safari-technology-preview-57/ "Release Notes for Safari Technology Preview 57 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 57이 릴리스 됐습니다.
크로스 오리진 Window 간 접근을 제한할 수 있는 `Cross-Origin-Options` HTTP 헤더를 시험적으로 지원하며  modern EME(Encrypted Media Extensions) API가 기본적으로 활성화 됐습니다.

----

## Jest 23: 🔥 Blazing Fast Delightful Testing · Jest
[facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html](https://facebook.github.io/jest/blog/2018/05/29/jest-23-blazing-fast-delightful-testing.html "Jest 23: 🔥 Blazing Fast Delightful Testing · Jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 23이 릴리스 됐습니다.
Interactive Snapshot Mode와 `toStrictEqual` 등의 matcher가 추가됐으며 비동기적 커스텀 matcher를 작성할 수 있도록 변경됐고 `jest-each`가 코어에 포함됐습니다.

----

## What’s New in Safari - Apple Developer
[developer.apple.com/safari/whats-new/](https://developer.apple.com/safari/whats-new/ "What’s New in Safari - Apple Developer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 12의 변경 예정 사항이 정리돼 있습니다.
watchOS에서 동작할 수 있도록 개선되며 `font-display`를 지원하고 ITP 2.0, CORB의 일부 기능을 지원합니다. 또, `.safariextz` 스타일의 Safari 확장을 비권장하는 등 다양한 변경 사항이 예정돼 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Simplify Web Worker code with Comlink
[davidea.st/articles/comlink-simple-web-worker](https://davidea.st/articles/comlink-simple-web-worker "Simplify Web Worker code with Comlink")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">article</span></p>

Web Worker의 동작에 관한 설명과 Comlink를 활용한 Web Worker 사용 방법에 대해 작성돼 있습니다.

- [GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.](https://github.com/GoogleChromeLabs/comlink "GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.")

----

## Beyond SPAs: alternative architectures for your PWA  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/05/beyond-spa](https://developers.google.com/web/updates/2018/05/beyond-spa "Beyond SPAs: alternative architectures for your PWA  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">server</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

Service Worker와 Express를 사용한 페이지 단위(SPA가 아닌)의 웹 애플리케이션을 위한 아키텍처와 구현 샘플에 대해 소개돼 있습니다.
라우팅을 클라이언트와 서버에서 공유하고, 부분적인 View를 Stream API로 가져와 렌더링합니다. 또, 동적인 메타 정보의 전달 방법에 대해 소개돼 있습니다.

- [GoogleChromeLabs/so-pwa: A progressive web app to read Stack Overflow content.](https://github.com/GoogleChromeLabs/so-pwa "GoogleChromeLabs/so-pwa: A progressive web app to read Stack Overflow content.")

----

## Getting Started With CSS Layout — Smashing Magazine
[www.smashingmagazine.com/2018/05/guide-css-layout/](https://www.smashingmagazine.com/2018/05/guide-css-layout/ "Getting Started With CSS Layout — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS의 레이아웃에 관한 소개글입니다.
Float, Flex, Grid 등의 레이아웃 구조에 대해 작성돼 있습니다.
Box와 Contents, Alignment 등에 관해서도 이야기합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JavaScript engines: The Good Parts™ // slidr.io
[slidr.io/mathiasbynens/javascript-engines-the-good-parts#1](https://slidr.io/mathiasbynens/javascript-engines-the-good-parts#1 "JavaScript engines: The Good Parts™ // slidr.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

JavaScript 엔진의 최적화 패스에 대해 이야기하는 슬라이드입니다.
V8, Spidermonkey, Chackra, JavaScriptCore 각각 최적화 패스의 흐름이나 Shape와 최적화가 깨지는 패턴에 대해서 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## GoogleChromeLabs/critters: A Webpack plugin to inline your critical CSS and lazy-load the rest.
[github.com/GoogleChromeLabs/critters](https://github.com/GoogleChromeLabs/critters "GoogleChromeLabs/critters: 🦔 A Webpack plugin to inline your critical CSS and lazy-load the rest.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span> <span class="jser-tag">performance</span></p>

크리티컬 CSS 인라인화, 외부 파일의 lazy load와 prefetch를 담당하는 webpack plugin입니다.

----

## Reach Router - Overview
[reach.tech/router](https://reach.tech/router "Reach Router - Overview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span></p>

React 용 라우터 라이브러리입니다.
React Router의 본 개발자가 개발하고 있고 Focus Mangement 등의 접근성가 고려돼 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## alangpierce/sucrase: Super-fast alternative to Babel for when you can target modern JS runtimes
[github.com/alangpierce/sucrase](https://github.com/alangpierce/sucrase "alangpierce/sucrase: Super-fast alternative to Babel for when you can target modern JS runtimes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">jsx</span> <span class="jser-tag">flowtype</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

Babel Parser를 fork하여 개발한 JSX / Flow / TypeScript 등을 JS로 변환하는 도구입니다.
ES2015+를 실행할 수 있는 환경을 고려해 코드를 변환하거나 JSX / Flow / TypeScript의 변환을 빠르게 변환하는 것에 목적을 두고 있습니다.
Babel와는 다르게 플러그인 시스템을 생략하여 변환 속도를 향상시키고 있습니다.

----

## hybridsjs/hybrids: UI library for creating Web Components with simple and functional API
[github.com/hybridsjs/hybrids/](https://github.com/hybridsjs/hybrids/ "hybridsjs/hybrids: UI library for creating Web Components with simple and functional API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span></p>

`lit-html` 처럼 Custom Element를 만들 수 있는 `html`이나 `define` 등을 제공하는 라이브러리입니다.

----

## Alex1990/tiny-cookie: A tiny cookie manipulation plugin for the browser.
[github.com/Alex1990/tiny-cookie](https://github.com/Alex1990/tiny-cookie "Alex1990/tiny-cookie: A tiny cookie manipulation plugin for the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

작은 사이즈의 쿠키 조작 라이브러리입니다.

----

## GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.
[github.com/GoogleChromeLabs/comlink](https://github.com/GoogleChromeLabs/comlink "GoogleChromeLabs/comlink: Comlink makes WebWorkers enjoyable.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webworker</span></p>

Proxy를 사용한 Web Worker 라이브러리입니다.
Worker 내의 구현을 Proxy하여 `postMessage` 등의 메세지를 감춰줍니다.

----

## marblejs/marble: Marble.js - functional reactive HTTP middleware framework built on top of Node.js platform, TypeScript and RxJS library.
[github.com/marblejs/marble](https://github.com/marblejs/marble "marblejs/marble: Marble.js - functional reactive HTTP middleware framework built on top of Node.js platform, TypeScript and RxJS library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">server</span> <span class="jser-tag">HTTP</span></p>

Rxjs를 사용한 HTTP 미들웨어 프레임워크입니다.
Node.js 환경의 리퀘스트, 리스폰즈에 대한 처리를 작성할 수 있습니다.

----

## Keyframes.app
[keyframes.app/](https://keyframes.app/ "Keyframes.app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">editor</span></p>

CSS animation의 GUI 에디터입니다. CSS animation의 프로퍼티를 설정하여 실제 애니메이션을 재생해보면서 애니메이션에 필요한 CSS 속성을 만들 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books
[www.amazon.com/dp/1617295248/](https://www.amazon.com/dp/1617295248/ "Testing Vue.js Applications: Edd Yerburgh: 9781617295249: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span> <span class="jser-tag">JavaScript</span></p>

2018년 8월 31일 출간 예정인 Vue.js의 테스트를 주제로 한 도서입니다.

----
