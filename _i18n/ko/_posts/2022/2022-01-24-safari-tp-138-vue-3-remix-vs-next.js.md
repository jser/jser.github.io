---
title: "2022-01-24: Safari TP 138, Vue 3를 기본 버전으로, Remix vs Next.js"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-01-24T11:20:56.215Z
category: JSer
tags:
- node.js
- React
- npm
- HTTP
- GraphQL

---

JSer.info #576 - Safari Technology Preview 138 릴리스.

- [Release Notes for Safari Technology Preview 138 | WebKit](https://webkit.org/blog/12176/release-notes-for-safari-technology-preview-138/)

사파리 개발자 도구 Web Inspector의 Element Tab에서 Cascade Layers를 지원하는 등 몇몇 기능이 개선됐다.
또, CSS의 `:focus-visible`, Media Query의 `resolution`, CSS Containment가 기본적으로 활성화 됐다.

- [No, Apple Did Not Crowdfund :focus-visible in Safari – Eric’s Archived Thoughts](https://meyerweb.com/eric/thoughts/2022/01/24/no-apple-did-not-crowdfund-focus-visible-in-safari/)
  - WebKit에 `:focus-visible`가 구현되어 온 과정

그 외로는 Service Worker의 `NavigationPreloadManager`가 활성화됐고 Service Worker를 경유한 파일을 다운로드할 수 없던 문제가 수정됐다.

----

2022년 2월 7일에 `vue`의 기본 버전이 Vue 3로 변경될 것이라고 발표했다.

- [Vue 3 as the New Default | The Vue Point](https://blog.vuejs.org/posts/vue-3-as-the-new-default.html)

현재(2022년 1월 24일) `vue` 버전의 `latest`는 2.x다.

```
$ npm info vue

vue@2.6.14 | MIT | deps: none | versions: 368
Reactive, component-oriented view layer for modern web interfaces.
https://github.com/vuejs/vue#readme

keywords: vue

dist
.tarball: https://registry.npmjs.org/vue/-/vue-2.6.14.tgz
.shasum: e51aa5250250d569a3fbad3a8a5a687d6036e235
.integrity: sha512-x2284lgYvjOMj3Za7kqzRcUSxBboHqtgRE2zlos1qWaOye5yUmHn42LB1250NJBLRwEcdrB0JRwyPTEPhfQjiQ==
.unpackedSize: 3.0 MB

maintainers:
- posva <posva13@gmail.com>
- yyx990803 <yyx990803@gmail.com>

dist-tags:
beta: 3.2.0-beta.8  csp: 1.0.28-csp     latest: 2.6.14      next: 3.2.29

published 7 months ago by posva <posva13@gmail.com>
```

2022년 2월 7일에 `vue`의 `latest`가 3.x로 변경된다.
따라서 `npm install vue` 와 같이 버전 지정 없이 설치하면 `vue@3`가 설치된다.

이 변경과 함께 웹 사이트도 개편하고 깃허브([github.com/vuejs](https://github.com/vuejs)) 저장소 이름도 변경할 예정이라고 한다.



----

<h1 class="site-genre">헤드라인</h1>

----

## Release v0.25.0 · axios/axios
[github.com/axios/axios/releases/tag/v0.25.0](https://github.com/axios/axios/releases/tag/v0.25.0 "Release v0.25.0 · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

axios 0.25.0 릴리스.


----

## Node v17.4.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.4.0/](https://nodejs.org/en/blog/release/v17.4.0/ "Node v17.4.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.4.0 릴리스.
EventEmitter와 AsyncResource를 통합하는 `EventEmitterAsyncResource`가 추가됐고 ReadableStream에 `map`과 `filter`가 추가됐다.

- [addaleax/eventemitter-asyncresource: AsyncResource integration for EventEmitter](https://github.com/addaleax/eventemitter-asyncresource "addaleax/eventemitter-asyncresource: AsyncResource integration for EventEmitter")

----

## Announcing React Native 0.67 · React Native
[reactnative.dev/blog/2022/01/19/version-067](https://reactnative.dev/blog/2022/01/19/version-067 "Announcing React Native 0.67 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.67 릴리스.
`DatePickerAndroid`가 삭제됐고 Hermes를 0.9.0으로 갱신했다.


----

## Deno 1.18 Release Notes
[deno.com/blog/v1.18](https://deno.com/blog/v1.18 "Deno 1.18 Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.18 릴리스.
Web Cryptography API 구현, `deno.json`을 자동으로 참조하도록 개선, Error Cause를 스택 트레이스에 반영.
`Deno.test`의 step API를 stable로 변경, FFI API 개선, V8 snapshots의 압축 방법을 V8 zlib에서 lz와 zstd로 변경하여 동작 속도 개선.


----

## Release Notes for Safari Technology Preview 138 | WebKit
[webkit.org/blog/12176/release-notes-for-safari-technology-preview-138/](https://webkit.org/blog/12176/release-notes-for-safari-technology-preview-138/ "Release Notes for Safari Technology Preview 138 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 138 릴리스.
`:focus-visible`, Media Query의 `resolution`, CSS Containment를 기본 활성화.
Service Worker의 `NavigationPreloadManager`를 활성화, Service Worker를 경유한 파일 다운로드 지원.


----

## Vue 3 as the New Default | The Vue Point
[blog.vuejs.org/posts/vue-3-as-the-new-default.html](https://blog.vuejs.org/posts/vue-3-as-the-new-default.html "Vue 3 as the New Default | The Vue Point")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

2022년 2월 7일에 Vue 3가 `vue@next`에서 `vue@latest`로 변경되어 `vue` 패키지의 안정(stable) 버전으로 배포된다.
이 변경과 더불어 CDN의 lastest 참조 버전, 문서(웹사이트), GitHub 저장소도 변경된다.


----

## Release v5.67.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.67.0](https://github.com/webpack/webpack/releases/tag/v5.67.0 "Release v5.67.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5.67.0 릴리스.
AssertModule에 `outputPath` 옵션 추가.
`output.trustedTypes: true`인 경우에는 `eval-source-map`이라도 Trusted Types에 대응하는 코드를 출력하도록 변경.


----

## Announcing TypeScript 4.6 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6-beta/ "Announcing TypeScript 4.6 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.6 Beta 릴리스.
주로 타입 추론과 관련한 내용이 개선됐다. 재귀 타입, 인터페이스에 대한 인덱스 참조, 함수의 인수에 대한 타입 추론 성능 개선.
`checkJs`를 활성화했을 경우 실행되는 자바스크립트의 구문 에러 검사 개선.
`--generateTrace`로 출력할 수 있는 빌드에 대한 트레이스 데이터를 분석할 수 있는 `@typescript/analyze-trace` 패키지 공개.

- [@typescript/analyze-trace - npm](https://www.npmjs.com/package/@typescript/analyze-trace "@typescript/analyze-trace - npm")

----
<h1 class="site-genre">아티클</h1>

----

## npm: A Free Guide for Beginners | CSS-Tricks - CSS-Tricks
[css-tricks.com/a-complete-beginners-guide-to-npm/](https://css-tricks.com/a-complete-beginners-guide-to-npm/ "npm: A Free Guide for Beginners | CSS-Tricks - CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">tutorial</span></p>

npm란 무엇인가. 기본적인 사용 방법을 다룬 소개 글.


----

## Remix vs Next.js | Remix
[remix.run/blog/remix-vs-next](https://remix.run/blog/remix-vs-next "Remix vs Next.js | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Next.js의 이커머스를 예제를 이용해 Remix와 Next.js를 비교한 글.
아키텍처의 다른점, CDN Edge에서의 실행, 데이터 갱신 방식에 대한 비교.


----

## Mocking With Undici Like a Pro
[fusebit.io/blog/undici-mocking/](https://fusebit.io/blog/undici-mocking/ "Mocking With Undici Like a Pro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 용 HTTP 클라이언트 Undici가 지원하는 목킹을 소개한 글.
`MockAgent`를 사용한 목킹에 대해서 다룬다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## WebAppPentestGuidelines/graphQLGuideLine(일본어)
[github.com/WebAppPentestGuidelines/graphQLGuideLine](https://github.com/WebAppPentestGuidelines/graphQLGuideLine "WebAppPentestGuidelines/graphQLGuideLine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

GraphQL에 대한 취약성을 진단하는 가이드.
자주 하는 실수인 Introspection Query가 활성돼 있는 경우, DoS로 악용될 수 있는 쿼리, 경합 조건 등에 대해서 다룬다.
함께 진단 혹은 조사에 사용할 수 있는 도구도 소개한다.


----

## Vanilla List • The Vanilla JavaScript Repository
[vanillalist.top/](https://vanillalist.top/ "Vanilla List • The Vanilla JavaScript Repository")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

의존성 없이 바닐라로 개발한 라이브러리를 정리한 사이트.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mo.js
[mojs.github.io/](https://mojs.github.io/ "mo.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

도형 묘화 및 애니메이션을 적용할 수 있는 라이브러리


----

## tinyplex/tinybase: A tiny, reactive JavaScript library for structured state and tabular data.
[github.com/tinyplex/tinybase](https://github.com/tinyplex/tinybase "tinyplex/tinybase: A tiny, reactive JavaScript library for structured state and tabular data.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">database</span> <span class="jser-tag">library</span></p>

테이블 구조로 데이터 및 상태를 관리할 수 있는 라이브러리


----
<h1 class="site-genre">도서</h1>

----

## Structure and Interpretation of Computer Programs | The MIT Press
[mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1](https://mitpress.mit.edu/books/structure-and-interpretation-computer-programs-1 "Structure and Interpretation of Computer Programs | The MIT Press")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">book</span></p>

2022년 4월 출간 예정인 자바스크립트로 쓴 SICP.

- [sicp.comp.nus.edu.sg/](https://sicp.comp.nus.edu.sg/ "sicp.comp.nus.edu.sg/")

----
