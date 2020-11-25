---
title: "2020-11-22: Tailwind CSS v2.0, Electron 11.0.0, TypeScript 4.1, playwright-test"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-11-22T02:57:36.494Z
category: JSer
tags:
- Chrome
- browser
- proposal
- security
- XSS

---

JSer.info #515 - [Utility-First](https://tailwindcss.com/docs/utility-first)한 CSS 프레임워크인 Tailwind CSS 2.0 릴리스.

- [Tailwind CSS v2.0 – Tailwind CSS](https://blog.tailwindcss.com/tailwindcss-v2)

비호환 변경 사항으로 IE11 지원 종료, Node 10 이하 지원 종료, 일부 클래스 명이 변경 됐다.
추가된 기능으로는 색상 팔레트, 다크 모드 지원, `2xl` breakpoint가 있다. 
또, 폼 전용 플러그인 `@tailwindcss/forms`와 `overflow-ellipsis`, `overflow-clip`이 추가됐고 `@apply` 대응이 개선됐다.

---

Electron 11.0.0 릴리스

- [Electron 11.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-11-0)
- [Release electron v11.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v11.0.0)

Electron 11.0.0에서 Apple Silicon을 대응한다.

- [Apple Silicon Support | Electron Blog](https://www.electronjs.org/blog/apple-silicon)

그 외로는 Chromium 87 / V8 8.7 / Node.js 12.18.3으로 각각 버전이 갱신됐다.

---

TypeScript 4.1 정식 릴리스

- [Announcing TypeScript 4.1 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/)

큰 변경 사항으로 Template Literal Types를 지원한다.
Template Literal Types는 템플릿 리터럴에 대한 타입 정의 표현을 위한 것으로 DSL 등의 타입 정의에 사용할 수 있다. 

- [ghoullier/awesome-template-literal-types: Curated list of awesome Template Literal Types examples](https://github.com/ghoullier/awesome-template-literal-types)

또, Mapped Types에서 Key의 Remapping을 지원, 재귀적인 Conditional Types 지원, `undefined`일 수 있는 인덱스에 접근하게 되는 경우를 검사하는 `noUncheckedIndexedAccess`가 추가됐다. 
그 외로는 `baseUrl` 없이 `paths`을 지정할 수 있도록 개선 됐고, 새로운 JSX에 대한 변환을 지원한다.
비호환 변경으로 `new Promise`의 `resolve` 함수에 대한 인수 타입을 Optional로 선언할 수 없도록 변경됐다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Tailwind CSS v2.0 – Tailwind CSS
[blog.tailwindcss.com/tailwindcss-v2](https://blog.tailwindcss.com/tailwindcss-v2 "Tailwind CSS v2.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS 2.0 릴리스.
비호환 변경으로 IE11 지원 종료, Node 10 이하 지원 종료, 일부 클래스 명이 변경됐다.
추가된 기능으로는 색상 팔레트 추가, 다크 모드 지원, `2xl` breakpoint 등이 있다.
그 외로 폼 용 플러그인으로 `@tailwindcss/forms`와 `overflow-ellipsis`, ` overflow-clip`이 추가됐고 `@apply` 대응이 개선됐다. 



----

## Firefox 83 is upon us - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/11/firefox-83-is-upon-us/](https://hacks.mozilla.org/2020/11/firefox-83-is-upon-us/ "Firefox 83 is upon us - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 83 릴리스.
개발자 도구에서 `scroll`에 대한 디버깅 기능이 개선됐고, CSS `conic-gradient` 함수를 지원하며 WebRender 아키텍처 지원 대상이 추가됐다.

- [Firefox 83 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/83 "Firefox 83 for developers - Mozilla | MDN")

----

## Electron 11.0.0 | Electron Blog
[www.electronjs.org/blog/electron-11-0](https://www.electronjs.org/blog/electron-11-0 "Electron 11.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 11.0.0 릴리스.
Chromium 87 / V8 8.7 / Node.js 12.18.3으로 각각 버전이 갱신됐다.
Apple M1 지원, `app.createThumbnailFromPath()`, `webContents.forcefullyCrashRenderer()`가 추가됐다.

- [Release electron v11.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v11.0.0 "Release electron v11.0.0 · electron/electron")

----

## New in Chrome 87  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/11/nic87](https://developers.google.com/web/updates/2020/11/nic87 "New in Chrome 87  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 87 릴리스.
DevTools에 WebAuthn 탭 추가, 카메라의 pan / tilt / zoom 지원, Service Worker에서 Range 요청 지원.
Cookie Store API, `Intl.Segmenter`, `isInputPending`을 지원하고 `postMessage`에 Streams을 전달 할 수 있도록 개선 됐다.
또 FTP가 기본적으로 비활성화 됐다.

- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D87 "Chrome Platform Status")

----

## Announcing TypeScript 4.1 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-1/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1/ "Announcing TypeScript 4.1 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.1 릴리스.
Template Literal Types, Mapped Types에서 Key의 Remapping 지원, 재귀적인 Conditional Types 지원. `undefined` 일 수 있는 인덱스에 접근을 검사하는 `noUncheckedIndexedAccess` 옵션 추가.
`baseUrl` 없이 `paths` 옵션을 지정할 수 있도록, 새로운 JSX 변환 지원.
비호환 변경으로는 `new Promise`의 `resolve` 함수에 대한 인수를 생략할 수 없도록 변경됐다.


----

## Prettier 2.2: new JavaScript parsers, TS 4.1 and ESM standalone bundles · Prettier
[prettier.io/blog/2020/11/20/2.2.0.html](https://prettier.io/blog/2020/11/20/2.2.0.html "Prettier 2.2: new JavaScript parsers, TS 4.1 and ESM standalone bundles · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.2 릴리스.
`espree`와 `meriyah` 자바스크립트 파서와 TypeScript 4.1을 지원하며 standalone 버전을 패키지에 포함하도록 변경됐다.


----

## Release Notes for Safari Technology Preview 116 | WebKit
[webkit.org/blog/11348/release-notes-for-safari-technology-preview-116/](https://webkit.org/blog/11348/release-notes-for-safari-technology-preview-116/ "Release Notes for Safari Technology Preview 116 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 116 릴리스.
AudioWorklet API를 기본적으로 활성화, MediaRecorder 개선, Storage Access API가 per frame에서 per page으로 변경됐다.


----

## ECMAScript proposal updates @ 2020-11 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/11/22/ecmascript-proposal-updat](https://ecmascript-daily.github.io/ecmascript/2020/11/22/ecmascript-proposal-updat "ECMAScript proposal updates @ 2020-11 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2020년 11월 TC39 Meeting에서 변경된 ECMAScript Proposal 상태 정리.


----
<h1 class="site-genre">아티클</h1>

----

## Back/forward cache
[web.dev/bfcache/](https://web.dev/bfcache/ "Back/forward cache")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 87(Android)부터 cross-site 탐색을 위한 BFCache가 활성화 된다.
위 글에서는 BFCache의 동작, BFCache로 표시됐는지 판정하는 방법, BFCache 되지 않는 조건과 BFCache 에서의 처리 재개 방법을 소개한다.
또, Google Analytics의 접근 해석과 BFCache의 관계, 성능 측정에 미치는 영향 등에 대해서도 작성돼 있다.


----

## Web 기술의 조사 방법 | blog.jxck.io(일본어)
[blog.jxck.io/entries/2020-11-19/how-to-track-web-standards.html](https://blog.jxck.io/entries/2020-11-19/how-to-track-web-standards.html "Web 기술의 조사 방법 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span> <span class="jser-tag">spec</span> <span class="jser-tag">proposal</span></p>

웹 기술과 관련한 사양, 상태(status), 기술에 대한 논의 내용을 어디서 살펴 볼 수 있는지 소개한다.
이와 함께 Browser, IETF, W3C/WHAWG, TC39에 대해서도 설명한다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## BlackFan/client-side-prototype-pollution: Prototype Pollution and useful Script Gadgets
[github.com/BlackFan/client-side-prototype-pollution](https://github.com/BlackFan/client-side-prototype-pollution "BlackFan/client-side-prototype-pollution: Prototype Pollution and useful Script Gadgets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">XSS</span></p>

Prototype Pollution 공격 사례를 모아 놓은 저장소.
여러가지 라이브러리에 대한 rototype Pollution 예제 코드가 정리돼 있다.


----

## PrimeFaces – Ultimate UI Framework
[www.primefaces.org/](https://www.primefaces.org/ "PrimeFaces – Ultimate UI Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span> <span class="jser-tag">Java</span></p>

Angular, React, Vue, JSF를 지원하는 UI 프레임워크


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## 101arrowz/fflate: High performance (de)compression in an 8kB package
[github.com/101arrowz/fflate](https://github.com/101arrowz/fflate "101arrowz/fflate: High performance (de)compression in an 8kB package")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

deflate, gzip, zlib의 compress / decompress를 지원하는 라이브러리.
작은 파일 크기와 안정적인 성능을 주 목적으로 개발하고 있으며 Worker에서의 비동기 처리에도 대응하고 있다.


----

## microsoft/playwright-test: Build a cross-browser end-to-end test suite with Playwright.
[github.com/microsoft/playwright-test](https://github.com/microsoft/playwright-test "microsoft/playwright-test: Build a cross-browser end-to-end test suite with Playwright.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">browser</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span></p>

Playwright를 기반으로 한 E2E 테스트 프레임워크.
Jest 스러운 Assertion, Playwright와 Folio를 사용한 테스트, Snapshot 테스트로서 시각 테스팅을 지원한다.

- [microsoft/folio: A customizable test framework to build your own test frameworks](https://github.com/microsoft/folio "microsoft/folio: A customizable test framework to build your own test frameworks")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mkay581/cookie-store: A polyfill for the Cookie Store API
[github.com/mkay581/cookie-store](https://github.com/mkay581/cookie-store "mkay581/cookie-store: A polyfill for the Cookie Store API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span></p>

Cookie Store API의 Polyfill 라이브러리


----

## microsoft/folio: A customizable test framework to build your own test frameworks
[github.com/microsoft/folio](https://github.com/microsoft/folio "microsoft/folio: A customizable test framework to build your own test frameworks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

테스트 프레임워크를 만들기 위한 테스트 프레임워크.
Test Fixture, Annotation API으로 Flaky Tests 선언과 재시도, 특정 환경을 위한 테스트를 생성할 수 있다.


----

## kuu/hls-parser: A simple library to read/write HLS playlists
[github.com/kuu/hls-parser](https://github.com/kuu/hls-parser "kuu/hls-parser: A simple library to read/write HLS playlists")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

HLS playlist 파서, 제너레이터 라이브러리
Apple Low-Latency HLS 형식도 지원한다.

----

## ceifa/wasmoon: A real lua VM with JS bindings made with webassembly
[github.com/ceifa/wasmoon](https://github.com/ceifa/wasmoon "ceifa/wasmoon: A real lua VM with JS bindings made with webassembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Lua</span></p>

Lua VM을 WebAssembly로 변환해 JavaScript에서 Lua의 코드를 실행할 수 있는 라이브러리.


----
