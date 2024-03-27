---
title: "2024-03-27: Firefox 124, Chrome 123, Node.js 다큐멘터리"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-03-27T02:56:05.492Z
category: JSer
tags:
- nodejs
- Tools
- Chrome
- document
- rspack

---

JSer.info #686 - Firefox 124가 출시되었어요.

- [Firefox 124.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/124.0/releasenotes/)
- [Firefox 124 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/124)

 `AbortSignal.any()` 지원, WebDriver BiDi 대응 개선했어요.
또한, 플래그 조건으로 `SharedArrayBuffer.prototype.grow()`와 ` ArrayBuffer.prototype.resize()` 지원도 있어요.


---

Chrome 123가 출시되었어요.

- [New in Chrome 123  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-123?hl=en)

CSS `light-dark()` 지원, Service worker Static Routing API 지원, Content-Encoding: zstd 지원이 있어요.
또한, BFCache 이용할 수 없던 이유를 확인할 수 있는 `notRestoredReasons` 지원, ES Proposal Stage 3 Import Attributes 지원도 있어요.

---

Node.js 다큐멘터리가 공개되었어요.

- [Node.js: The Documentary | An origin story - YouTube](https://www.youtube.com/watch?v=LB8KwiiUGy0)

Node.js 탄생부터 Ryan→Isaac→TJ으로 오너 이양, Joyent 정체, io.js의 Fork에서 통합, Node.js Foundation 설립까지 이야기를 정리한 영상이에요.

같은 타이밍에, Node.js 웹사이트가 Next.js으로 리디자인된다는 발표가 있었어요.

- [Node.js — Diving into the Node.js Website Redesign](https://nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign)

Node.js 제작자이기도하면서 Deno의 제작자이기도 한 Ryan Dahl이 [X](https://twitter.com/rough__sea)에 복귀, Podcast에서 [JSR: the JavaScript Registry](https://jsr.io/)에 대해 언급하고 있어요.

- [Why the creator of Node.js® created a new JavaScript runtime - Stack Overflow](https://stackoverflow.blog/2024/03/19/why-the-creator-of-node-js-r-created-a-new-javascript-runtime/)

또한, 두 번째 Node.js 오너 Isaac이, JavaScript 패키지 매니저 개발하는 [vlt](https://www.vlt.sh/)에 참가한 것도 발표되었어요.

- [Introducing our team, investors & more...](https://blog.vlt.sh/blog/the-team)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing Rsbuild v0.5 - Rsbuild
[rsbuild.dev/community/releases/v0-5](https://rsbuild.dev/community/releases/v0-5 "Announcing Rsbuild v0.5 - Rsbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">rspack</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rsbuild v0.5 출시.
Lightning CSS를 opt-in으로 지원, Custom Server 지원, SVGR 플러그인 개선


----

## Firefox 124.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/124.0/releasenotes/](https://www.mozilla.org/en-US/firefox/124.0/releasenotes/ "Firefox 124.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 124 출시.
`AbortSignal.any()` 지원, WebDriver BiDi 대응 개선.
플래그 조건으로 `SharedArrayBuffer.prototype.grow()`와 ` ArrayBuffer.prototype.resize()` 지원

- [Firefox 124 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/124 "Firefox 124 for developers - Mozilla | MDN")

----

## Announcing VitePress 1.0 | The Vue Point
[blog.vuejs.org/posts/vitepress-1.0](https://blog.vuejs.org/posts/vitepress-1.0 "Announcing VitePress 1.0 | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

VitePress 1.0 출시


----

## New in Chrome 123  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-123?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-123?hl=en "New in Chrome 123  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 123 출시.
CSS `light-dark()` 지원, 
Service worker Static Routing API 지원, Content-Encoding: zstd 지원.
BFCache 이용할 수 없는 이유를 얻을 수 있는 `notRestoredReasons` 지원, ES Proposal Stage 3 Import Attributes 지원


----

## Node.js — Node v18.20.0 (LTS)
[nodejs.org/en/blog/release/v18.20.0](https://nodejs.org/en/blog/release/v18.20.0 "Node.js — Node v18.20.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.20.0 출시.
Import Attributes 지원, `vm.Script`와 Dynamic Import 관련한 성능 개선 backport(Jest에서 메모리 누수 문제 개선)


----

## Node.js — Node v20.12.0 (LTS)
[nodejs.org/en/blog/release/v20.12.0](https://nodejs.org/en/blog/release/v20.12.0 "Node.js — Node v20.12.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.12.0 출시.
`crypto.hash()` 추가, `.env` 다루는 `process.loadEnvFile(path)`와 `util.parseEnv(content)` 추가.
`net.createConnection`에 접속 시행 관련 이벤트 추가, `util.styleText(format, text)` 추가


----

## Release v10.4.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v10.4.0](https://github.com/mochajs/mocha/releases/tag/v10.4.0 "Release v10.4.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">test</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha v10.4.0 출시.
Error Cause 표시 대응


----

## Release v9.0.0-beta.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v9.0.0-beta.0](https://github.com/pnpm/pnpm/releases/tag/v9.0.0-beta.0 "Release v9.0.0-beta.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v9.0.0-beta.0 출시.
Node.js 16 지원 종료, Lockfile 버전 v7로 변경, `dedupe-injected-deps`를 `true`로 변경, `link-workspace-packages`를 `false`로 변경.
pre/post-script 실행하는 `enable-pre-post-scripts`를 `true`로 변경


----
<h1 class="site-genre">읽을거리</h1>

----

## Optimizing Javascript for fun and for profit
[romgrk.com/posts/optimizing-javascript](https://romgrk.com/posts/optimizing-javascript "Optimizing Javascript for fun and for profit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span></p>

JavaScript 성능 최적화에 대하여. 성능과 가독성 트레이드오프.
문자열 비교 피할 것, 다른 형태 피할 것, 배열이나 객체 메서드 피해 실행시 비용을 감소시키는 방법에 대하여


----

## Performance tooling in 2024 and beyond  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/perf-tooling-2024](https://developer.chrome.com/blog/perf-tooling-2024 "Performance tooling in 2024 and beyond  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Chrome DevTools에 실험적으 구현된 "Performance Insights" 패널은 2024년 후반에 삭제될 예정.
"Performance Insights"은 정보밀도를 감소시킬 목적이었지만, "Performance" 패널이 더 사용되었다는 이야기


----

## Node.js — Diving into the Node.js Website Redesign
[nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign](https://nodejs.org/en/blog/announcements/diving-into-the-nodejs-website-redesign "Node.js — Diving into the Node.js Website Redesign")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js 웹사이트가 Next.js로 새로히 작성된 이야기.
nextra 정적사이트로 시작했지만 커스텀 설정이 많아져서, Next.js를 Vercel에서 동작하는 방법으로 변경하였음.
이 리뉴얼에서 기존 번역이 리셋되었기에, 현 시점에서는 404가 됨り, 앞으로 Crowdin 사용한 번역 구조 도입 예정.

- [Node.js — Run JavaScript Everywhere](https://nodejs.org/en "Node.js — Run JavaScript Everywhere")

----

## Flow Nodes: How Type Inference Is Implemented
[effectivetypescript.com/2024/03/24/flownodes/](https://effectivetypescript.com/2024/03/24/flownodes/ "Flow Nodes: How Type Inference Is Implemented")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript의 narrowing가 어떻게 동작하는가에 대하여.
위아래 아래로 타입을 추리는 것이 아니라, 심볼이 참조된 포인트에서 제어 흐름 그래프를 역으로 접근함에 타입을 추린다는 이야기.


----

## Chrome에서 text-spacing-trim 프로퍼티가 지원된다니!!
[zenn.dev/inaniwaudon/articles/3ff8761773178c](https://zenn.dev/inaniwaudon/articles/3ff8761773178c "Chrome에서 text-spacing-trim 프로퍼티가 지원된다니!!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chrome 123에서 지원된 CSS의 text-spacing-trim 프로퍼티에 대하여


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Node.js: The Documentary | An origin story - YouTube
[www.youtube.com/watch?v&#x3D;LB8KwiiUGy0](https://www.youtube.com/watch?v=LB8KwiiUGy0 "Node.js: The Documentary | An origin story - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">history</span> <span class="jser-tag">video</span></p>

Node.js에 대한 다큐멘터리.
Node.js가 작성된 이유와 초기 개발, Window 대응과 libuv.
Ryan→Isaac→TJ으로 오너 이양, Joyent에서의 io.js의 fork, io.js와 Node.js가 머지될 때까지 이야기


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Runtime compatibility across JavaScript runtimes
[runtime-compat.unjs.io/](https://runtime-compat.unjs.io/ "Runtime compatibility across JavaScript runtimes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

Bun/Deno/Vercel/LLRT/Node.js/wasmer/workerd 등에서 JavaScript Runtime의 WinterCG API 호환성 정리 테이블


----

## Rsdoctor
[rsdoctor.dev/](https://rsdoctor.dev/ "Rsdoctor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">rspack</span> <span class="jser-tag">Tools</span></p>

webpack이나 Rspack의 bundle 결과를 분석하는 도구.
bundle 결과 정리, 컴파일/minify 시간, loader 마다 처리 시간 및 타임라인, 모듈 의존 관계 분석


----
