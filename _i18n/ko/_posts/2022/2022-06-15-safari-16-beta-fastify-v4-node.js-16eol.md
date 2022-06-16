---
title: "2022-06-15: Safari 16 Beta, Fastify v4, Node.js 16의 EOL 예정일 변경"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-06-15T03:43:11.216Z
category: JSer
tags:
- Tools
- node.js
- npm
- browser
- React

---

JSer.info #596 - Safari 16 beta의 릴리스 노트와 변경 사항에 대해 정리한 문서가 공개 됐다.

- [Safari 16 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-16-release-notes)
- [News from WWDC22: WebKit Features in Safari 16 Beta | WebKit](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/)

푸쉬 알림을 위한 Push API가 지원된다.

- [Meet Web Push | WebKit](https://webkit.org/blog/12945/meet-web-push/)

CSS의 Container Queries, Subgrid, `overscroll-behavior` 속성 지원이 추가 됐다.
또, Shared Worker 지원, Form의 `requestSubmit()` 메서드도 지원한다.

----

Node.js 웹 애플리케이션 프레임워크인 Fastify v4가 릴리스 됐다.

- [Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium](https://medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e)
- [Release v4.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v4.0.0)

Fastify 4.0.0에서는 일관성 없던 동작이 수정됐는데 비호환적이므로 버전 갱신 시 대응이 필요하다.
이와 함께 Fastify 3.x는 2023년 6월 30일에 EOL(End Of Life) 될 것임을 발표했다.

----

Node.js 16 LTS의 EOL은 2024년 4월 예정이었으나 2023년 9월 11일로 앞당겨졌다.

- [Bringing forward the End-of-Life Date for Node.js 16 | Node.js](https://nodejs.org/en/blog/announcements/nodejs16-eol/)

이것은 Node.js 16가 이용하는 OpenSSL1.1.1의 EOL이 2023년 9월 11일로 결정된데 기인한다.
결과적으로 Node.js 16의 EOL이 7개월 정도 단축된 상황이다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v11.9.0 · sverweij/dependency-cruiser
[github.com/sverweij/dependency-cruiser/releases/tag/v11.9.0](https://github.com/sverweij/dependency-cruiser/releases/tag/v11.9.0 "Release v11.9.0 · sverweij/dependency-cruiser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

dependency-cruiser 11.9.0 릴리스.
Markdown 형식 보고서를 지원한다.


----

## News from WWDC22: WebKit Features in Safari 16 Beta | WebKit
[webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/ "News from WWDC22: WebKit Features in Safari 16 Beta | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 16 Beta의 변경점 정리 및 소개.
Container Queries, Push API, Subgrid 지원.
CSS의 `overscroll-behavior` 지원, Shared Worker 지원, Form의 `requestSubmit()` 메서드 지원 등.

- [Safari 16 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-16-release-notes "Safari 16 Beta Release Notes | Apple Developer Documentation")

----

## Release v1.5.0 · ghiscoding/lerna-lite
[github.com/ghiscoding/lerna-lite/releases/tag/v1.5.0](https://github.com/ghiscoding/lerna-lite/releases/tag/v1.5.0 "Release v1.5.0 · ghiscoding/lerna-lite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

lerna-lite 1.5.0 릴리스.
락파일을 갱신하는 `--sync-workspace-lock` 플래그 추가 등.


----

## Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium
[medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e](https://medium.com/@fastifyjs/fastify-v4-ga-59f2103b5f0e "Fastify v4 GA. After two years we are excited to… | by Fastify | Jun, 2022 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>


Fastify 4.0.0 릴리스.
`reply.send`를 필수로 호출하도록 변경, `setErrorHandler` 처리 순서의 일관성 개선, Pino v8로 갱신, `fastify.listen`의 가변 인수 사용을 비권장화 등.

- [Release v4.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v4.0.0 "Release v4.0.0 · fastify/fastify")

----

## Bringing forward the End-of-Life Date for Node.js 16 | Node.js
[nodejs.org/en/blog/announcements/nodejs16-eol/](https://nodejs.org/en/blog/announcements/nodejs16-eol/ "Bringing forward the End-of-Life Date for Node.js 16 | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

Node.js 16의 EOL이 OpenSSL 1.1.1의 EOL과 동일한 2023녀 9월 11일 까지로 당겨졌다.


----

## PlasmoHQ/plasmo: The browser extension framework
[github.com/PlasmoHQ/plasmo](https://github.com/PlasmoHQ/plasmo "PlasmoHQ/plasmo: The browser extension framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">library</span></p>

브라우저 확장용 프레임워크.
React와 TypeScript 지원, Manifest V3, Live Reloading, `.env` 지원, 각 확장 Store로 배포하는 기능도 제공한다.


----

## ECMAScript proposal updates @ 2022-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2022/06/13/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2022/06/13/ecmascript-proposal-update "ECMAScript proposal updates @ 2022-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2022년 3월 TC39 Meeting에서 변경된 ECMAScript Proposal Stage 정리.
Type Annotations이 Stage 1로, Decorator가 Stage 3이 됐다.


----

## Release 3.23.0 - 2022.06.14 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.23.0](https://github.com/zloirock/core-js/releases/tag/v3.23.0 "Release 3.23.0 - 2022.06.14 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.23.0 릴리스.
`Array.prototype.findLast`를 stable로 이동, `Array.prototype.groupBy`를 `Array.prototype.group`으로 이름 변경 등.


----

## Prettier 2.7: new --cache CLI option and TypeScript 4.7 syntax! · Prettier
[prettier.io/blog/2022/06/14/2.7.0.html](https://prettier.io/blog/2022/06/14/2.7.0.html "Prettier 2.7: new --cache CLI option and TypeScript 4.7 syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.7 릴리스.
`--cache` 플래그 추가, TypeScript 4.7 지원 등.


----

## Release 10.8.0 · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.8.0](https://github.com/preactjs/preact/releases/tag/10.8.0 "Release 10.8.0 · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.8.0 릴리스.
Vitest와의 호환성을 위해서 Subpackages에 `exports` 필드 추가, `createRoot` / `hydrateRoot` API의 React와의 호환성 개선 등.


----

## Release v1.6.0 · remix-run/remix
[github.com/remix-run/remix/releases/tag/v1.6.0](https://github.com/remix-run/remix/releases/tag/v1.6.0 "Release v1.6.0 · remix-run/remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Remix</span></p>

Remix v1.6.0 릴리스.
`remix` 패키지를 Deprecated로 하고 `@remix-run/*`와 같이 개별 패키지로 Import 하여 사용하는 것을 권장한다.


----

## Release 7.0.0 · google/zx
[github.com/google/zx/releases/tag/7.0.0](https://github.com/google/zx/releases/tag/7.0.0 "Release 7.0.0 · google/zx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">shell</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

zx 7.0.0 릴리스.
TypeScript로 재작성, `within()`, `echo()` API 추가.
`--eval` 플래그 지원, REPL 지원 등.


----

## Release 18.2.0 (June 14, 2022) · facebook/react
[github.com/facebook/react/releases/tag/v18.2.0](https://github.com/facebook/react/releases/tag/v18.2.0 "Release 18.2.0 (June 14, 2022) · facebook/react")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React v18.2.0 릴리스.
`onRecoverableError`의 두 번째 인수에 component stack의 정보를 전달할 수 있도록 변경.
Hydrate 시 브라우저의 확장 기능 등에 의해 HTML이 변경 되면 렌더링이 깨지는 문제 수정 등.


----
<h1 class="site-genre">아티클</h1>

----

## First-party cookie recipes
[web.dev/first-party-cookie-recipes/](https://web.dev/first-party-cookie-recipes/ "First-party cookie recipes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

First-Party Cookie를 설정할 때의 Cookie 속성 지정 방법 정리
보통의 First-Party Cookie와 서브 도메인을 갖는 사이트 패턴에 대해 각각 설명하고 있다.
`__Host` prefix, `Secure` 속성, `Domain` 속성을 지정하지 말 것, `Path` 속성, `HttpOnly` 속성, `SameSite` 속성 등의 개요와 활용 방법을 소개한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## fastify/fastify-dx: A Full Stack Framework based on Fastify and Vite. Built for great developer experience without compromising on performance and stability.
[github.com/fastify/fastify-dx](https://github.com/fastify/fastify-dx "fastify/fastify-dx: A Full Stack Framework based on Fastify and Vite. Built for great developer experience without compromising on performance and stability.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

Fastify와 Vite를 기반으로 개발된 프레임워크.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ranyitz/qnm: cli utility for querying the node\_modules directory
[github.com/ranyitz/qnm](https://github.com/ranyitz/qnm "ranyitz/qnm: cli utility for querying the node\_modules directory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

node_modules에 설치돼 있는 패키지의 버전과 최신 버전, 공개일 등의 정보를 표시하는 명령줄 도구.
또, 패키지의 크기와 의존하고 있는 모듈의 개수 등도 표시한다.


----
