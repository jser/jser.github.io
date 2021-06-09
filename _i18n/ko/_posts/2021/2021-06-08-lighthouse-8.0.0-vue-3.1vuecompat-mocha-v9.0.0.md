---
title: "2021-06-08: Lighthouse 8.0.0(스코어 계산 변경), Vue 3.1(@vue/compat), Mocha v9.0.0"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-06-08T02:48:58.962Z
category: JSer
tags:
- Chrome
- node.js
- TypeScript
- browser
- WebAssembly

---

JSer.info #543 - Lighthouse 8.0.0 릴리스.

- [Release v8.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0)

Lighthouse 8.0.0에서는 퍼포먼스 스코어 계산식이 변경됐다.
상세한 내용은 다음 문서에 작성돼 있으며 지금까지 실험적이었던 Cumulative Layouy Shift(CLS) 비중이 5%에서 15%로 변경됐다. 이에 맞춰 다른 스코어 비중도 조금씩 조정됐다.

- [lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/v8-perf-faq.md)

기능 추가로 레포트를 지표 별로 필터링 가능하도록 됐고 `csp-xss`의 Audit 추가가 이뤄졌다.

----

Vue 3.1.0 릴리스.

- [Release v3.1.0 Pluto · vuejs/vue-next](https://github.com/vuejs/vue-next/releases/tag/v3.1.0)

Vue 3.1.0에서는 `@vue/compat`이라는 Vue 2 호환 API를 제공하는 패키지가 함께 공개됐다.
기존 Vue 2.x로 작성한 애플리케이션을 Vue 3 상에서 동작할 수 있도록 죽, Migration Build를 위해 추가된 패키지다.

자세한 내용은 아래 문서에 소개돼 있는데 Vue 2.x의 시점의 공개 API 만을 구현한 호환 빌드이기 때문에,
일부 라이브러리는 동작하지 않을 수 있다고 한다.

- [Migration Build | Vue.js](https://v3.vuejs.org/guide/migration/migration-build.html)

또, 향후에는 Vue 3에 구현된 Composition API 등을 Vue 2.x로 백포트한 Vue 2.7이 릴리스 될 예정이다.

----

JavaScript 테스트 프레임워크 Mocha 9.0.0 릴리스.

- [Release v9.0.0 · mochajs/mocha](https://github.com/mochajs/mocha/releases/tag/v9.0.0)

Mocha 9에서는 Node.js 10 지원이 종료됐고, ESM(ECMAScript Modules)를 네이티브 지원한다.
ESM으로 우선적으로 불러오며 실패한 경우 CJS(CommonJS)로 다시 시도하는 fallback 구조로 돼 있다.

- [import-first loading of test files by giltayar · Pull Request #4635 · mochajs/mocha](https://github.com/mochajs/mocha/pull/4635)

그 외로는 `--dry-run` 옵션 지원, 비권장 됐던 `utils.lookupFiles()` 삭제가 이뤄졌다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v10.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v10.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v10.0.0 "Release v10.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

puppeteer 10.0.0 릴리스.
Node.js 10 지원 종료, 동작 후 첫 페이지 로드 때까지 기다릴지 결정하는 `waitForInitialPage` 옵션 추가.


----

## Release v8.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v8.0.0 "Release v8.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 8.0.0 릴리스.
성능 스코어 계산식 변경, 레포트를 지표 별로 필터링 가능하도록, csp-xss의 Audit 추가.

- [lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/v8-perf-faq.md "lighthouse/v8-perf-faq.md at master · GoogleChrome/lighthouse")

----

## Electron 13.0.0 | Electron Blog
[www.electronjs.org/blog/electron-13-0](https://www.electronjs.org/blog/electron-13-0 "Electron 13.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 13.0.0 릴리스.
Chrome 91, Node.js 14.16.0, V8 9.1로 업데이트.
`process.contextIsolated`, `session.storagePat`, `process.contextId` 추가.
WebContents의 `new-window` 이벤트가 비권장됐고 대신 `webContents.setWindowOpenHandler()`를 권장


----

## Looking fine with Firefox 89 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/06/looking-fine-with-firefox-89/](https://hacks.mozilla.org/2021/06/looking-fine-with-firefox-89/ "Looking fine with Firefox 89 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 89 릴리스.

Media Query의 `forced-colors` 추가, 폰트 로드 시의 시각차를 조정할 수 있는 `line-gap-override` / `ascent-override` / `descent-override` 추가.
Top-level `await`를 기본 활성화, 64비트 머신에서 ArrayBuffer를 2GB 이상의 크기로 다룰 수 있도록 변경, `PerformanceEventTiming` 지원.

- [Firefox 89 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/89 "Firefox 89 for developers - Mozilla | MDN")
- [Firefox 89.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/89.0/releasenotes/ "Firefox 89.0, See All New Features, Updates and Fixes")

----

## Chromium Blog: Chrome 92: Web Apps as File Handlers, New JavaScript Features, and More
[blog.chromium.org/2021/06/chrome-92-web-apps-as-file-handlers-new.html](https://blog.chromium.org/2021/06/chrome-92-web-apps-as-file-handlers-new.html "Chromium Blog: Chrome 92: Web Apps as File Handlers, New JavaScript Features, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 92 베타 릴리스.
Origin Trial로서 File Handling API, Shared Element Transitions 지원.
`@font-face`의 `size-adjust` 지원, V8 엔진 9.2 버전으로 업데이트, SharedArrayBuffers를 Cross Origin Isolate된 페이지 내에서만 사용할 수 있도록 한정.


----

## Release v9.0.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v9.0.0](https://github.com/mochajs/mocha/releases/tag/v9.0.0 "Release v9.0.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 9.0.0 릴리스.
Node.js 10 지원 종료, ESM 지원, `--dry-run` 옵션 지원.
비권장 됐던 `utils.lookupFiles()`가 삭제됐다.


----

## Node v16.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.3.0/](https://nodejs.org/en/blog/release/v16.3.0/ "Node v16.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.3.0 릴리스.
npm 7.15.1로 업데이트 됐다. 해당 버전에는 npm의 workspace 관련 명령어가 여러가지 추가됐다.


----

## Release v3.1.0 Pluto · vuejs/vue-next
[github.com/vuejs/vue-next/releases/tag/v3.1.0](https://github.com/vuejs/vue-next/releases/tag/v3.1.0 "Release v3.1.0 Pluto · vuejs/vue-next")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue 3.1.0 릴리스.
Vue 2에서의 Migration Build 용도로 `@vue/compat` 추가.
`app.config.isCustomElement`와 컴포넌트의 `delimiters` 옵션을 비권장하고 컴포넌트의 `compilerOptions` 옵션을 지원.
`v-is`를 비권장하고 `is="vue:xxx"`를 지원한다.


----
<h1 class="site-genre">아티클</h1>

----

## What&#039;s New In DevTools (Chrome 92) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-92/](https://developer.chrome.com/blog/new-in-devtools-92/ "What&#039;s New In DevTools (Chrome 92) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 92 개발자 도구 변경 사항 정리.
CSS Grid 에디터, REPL 내에서 `const` 재정의 가능하도록, Source order viewer 추가.
CORS 에러 메시지 개선, Network 필터에 Wasm type 추가, UA Client Hint 대응.
Experiments로 Chrome DevTools Protocol을 볼 수 있는 Protocol Monitor, Puppeteer Recorder 추가.


----

## UI Security - Thinking Outside the Viewport | Microsoft Browser Vulnerability Research
[microsoftedge.github.io/edgevr/posts/ui-security-thinking-outside-the-viewport/](https://microsoftedge.github.io/edgevr/posts/ui-security-thinking-outside-the-viewport/ "UI Security - Thinking Outside the Viewport | Microsoft Browser Vulnerability Research")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

브라우저 UI 보안을 주제로 UI 보안 체크리스트, UI 보안 버그 등을 소개하고 설명하는 글.


----

## Making JavaScript run fast on WebAssembly | Bytecode Alliance
[bytecodealliance.org/articles/making-javascript-run-fast-on-webassembly](https://bytecodealliance.org/articles/making-javascript-run-fast-on-webassembly "Making JavaScript run fast on WebAssembly | Bytecode Alliance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Wasm에서 동작하는 자바스크립트 엔진을 만들기.
Wasm을 샌드박스로서 자바스크립트를 실행 가능하다는 내용, 자바스크립트 엔진의 초기화 및 런타임 시의 고성능 처리 기법에 대해서 소개.

- [bytecodealliance/wizer: The WebAssembly Pre-Initializer](https://github.com/bytecodealliance/wizer "bytecodealliance/wizer: The WebAssembly Pre-Initializer")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## An introduction to WebAssembly for JavaScript Developers
[pascalpares.appspot.ovh/webassembly-for-javascript-developers/](https://pascalpares.appspot.ovh/webassembly-for-javascript-developers/ "An introduction to WebAssembly for JavaScript Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

WebAssembly 관련 JavaScript API 소개 문서.
Wasm 파일 가져오기, 컴파일, Wasm에서 JS의 콜백 함수 호출하기, Dynamic Link, 전역 변수, 문자열 전달 방법, Shared Memory Buffer 등에 대해서 알 수 있다.


----

## progfay/benefit-from-end-of-ie: List of APIs that will be available due to IE termination
[github.com/progfay/benefit-from-end-of-ie](https://github.com/progfay/benefit-from-end-of-ie "progfay/benefit-from-end-of-ie: List of APIs that will be available due to IE termination")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">document</span></p>

IE만 지원하지 않는 API를 정리해놓은 저장소.
MDN의 데이버를 기반으로 HTML, JS, CSS, SVG 등의 API 정보가 테이블로 정리돼 있어 한번에 훑어보기에 좋다.

----


## Node.js API Table
[nodejs-api-table.netlify.app/](https://nodejs-api-table.netlify.app/ "Node.js API Table")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">API</span> <span class="jser-tag">document</span></p>

Node.js의 모듈이나 API가 어느 버전에서 추가 됐는지 살펴볼 수 있는 사이트.

- [Next.js로 Node.js의 API가 어느 버전에 추가 됐는지 알 수 있는 표를 만들다](https://zenn.dev/sosukesuzuki/articles/f00bc24600f2d8 "Next.js로 Node.js의 API가 어느 버전에 추가 됐는지 알 수 있는 표를 만들다")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## devongovett/dprint-node: A node API for the dprint TypeScript and JavaScript code formatter
[github.com/devongovett/dprint-node](https://github.com/devongovett/dprint-node "devongovett/dprint-node: A node API for the dprint TypeScript and JavaScript code formatter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">library</span></p>

Rust로 작성한 dprint 기반의 코드 포메터.


----

## htmlplus/core: HTMLPLUS is a native, framework-less, and lightweight library that is purely developed with Javascript. All HTMLPLUS components are customizable and configurable.
[github.com/htmlplus/core](https://github.com/htmlplus/core "htmlplus/core: HTMLPLUS is a native, framework-less, and lightweight library that is purely developed with Javascript. All HTMLPLUS components are customizable and configurable.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Web Components으로 만든 UI 라이브러리.
React와 Vue 영 바인딩도 제공한다.


----

## kawmra/typist-json: A simple runtime JSON type checker.
[github.com/kawmra/typist-json](https://github.com/kawmra/typist-json "kawmra/typist-json: A simple runtime JSON type checker.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">library</span></p>

스키마를 정의할 수 있는 빌더 함수와 검증(check) 수단 제공하는 라이브러리.
정의한 스키마를 타입스크립트의 타입으로 사용할 수 있음.


- [TypeScript 용 경량 런타임 JSON 타입 체커를 만들다](https://zenn.dev/kawmra/articles/0aad8dca56f1da "TypeScript 용 경량 런타임 JSON 타입 체커를 만들다")(일본어)

----

## EvandroLG/ts-audio: ts-audio is an agnostic library that makes it easy to work with AudioContext and create audio playlists in the browser
[github.com/EvandroLG/ts-audio](https://github.com/EvandroLG/ts-audio "EvandroLG/ts-audio: ts-audio is an agnostic library that makes it easy to work with AudioContext and create audio playlists in the browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">audio</span> <span class="jser-tag">TypeScript</span></p>

AudioContext API를 사용한 음악 재생 라이브러리.
여러개의 음악 연속 재생 등 다양한 음악 관련 기능 제공.


----

## Testy/TestyTs: ✔️ Modern TypeScript testing framework.
[github.com/Testy/TestyTs](https://github.com/Testy/TestyTs "Testy/TestyTs: ✔️ Modern TypeScript testing framework.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

데코레이터를 사용하는 타입스트립트 테스트 프레임워크.


----
