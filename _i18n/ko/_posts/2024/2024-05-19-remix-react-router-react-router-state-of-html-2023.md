---
title: "2024-05-19: Remix + React Router = React Router, State of HTML 2023"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-05-19T14:15:49.809Z
category: JSer
tags:
- React
- Angular
- nodejs
- Next.js
- safari

---

JSer.info #693 - 다음 글에서, Remix v3는 React Router v7로 출시될 예정이라는 이야기를 다뤄요.

- [Merging Remix and React Router | Remix](https://remix.run/blog/merging-remix-and-react-router)

Remix와 React Router는, Vite와 서버 이외에서 거의 비슷한 기능이에요.
이에, React Router를 Remix로 마이그레이션할 필요 없이, React Router 업데이트하기만 하면 Remix 기능을 사용할 수 있다는 이야기구요.
기존 Remix 애플리케이션은, import할 때 패키지 `react-router` 변경하기만 해도 동작하게 할 예정이에요.

이런 결정 상세 사항은, X에 작성되어 있어요.

- https://x.com/ryanflorence/status/1791479313939976313

React Router 안정화 위해, Remix 자체 개발은 잠시 멈추지만, 
앞으로 Remix 프로젝트로 다뤄질 예정 같아요.

---

State of HTML 2023 결과가 공개되었어요.

- [State of HTML 2023](https://2023.stateofhtml.com/en-US/)

HTML 엘리먼트와 속성, Web Components, 접근성, 앞으로의 과제와 바라던 기능에 대한 앙케이트 결과에요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## WebKit Features in Safari 17.5 | WebKit
[webkit.org/blog/15383/webkit-features-in-safari-17-5/](https://webkit.org/blog/15383/webkit-features-in-safari-17-5/ "WebKit Features in Safari 17.5 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17.5 변경점.
CSS의 `text-wrap: balance`, `light-dark()`, `@starting-style`, `@import <url> supports(<feature>)` 지원.
AV1 for WebCodecs 지원


----

## Firefox 126.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/126.0/releasenotes/](https://www.mozilla.org/en-US/firefox/126.0/releasenotes/ "Firefox 126.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 126 출시.
zstd 지원, CSS `zoom` 프로퍼티 지원, `URL.parse()` 지원,  Screen Wake Lock API 지원.
Custom Element의 CustomStateSet과 `:state()` 추상클래스 지원

- [Firefox 126 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/126 "Firefox 126 for developers - Mozilla | MDN")

----

## Node.js — Node v22.2.0 (Current)
[nodejs.org/en/blog/release/v22.2.0](https://nodejs.org/en/blog/release/v22.2.0 "Node.js — Node v22.2.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.2.0 출시.
fs.glob가 `withFileTypes` 지원, `--inspect-wait=host:port` 지원, `--experimental-policy` 삭제.
`node:test`에 `test.plan` 메서드 추가


----

## Release 8.1.0 · google/zx
[github.com/google/zx/releases/tag/8.1.0](https://github.com/google/zx/releases/tag/8.1.0 "Release 8.1.0 · google/zx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ShellScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

zx 8.1.0 출시.
ESM와 CJS 모두 지원, Node.js 12에서 22까지 지원, Deno 1.x 호환성 지원.
`usePwsh()` 추가, `$.timeout` 지원, `--cwd` 플래그 추가


----

## Release v0.21.3 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.21.3](https://github.com/evanw/esbuild/releases/tag/v0.21.3 "Release v0.21.3 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.21.3 출시.
decorator metadata proposal 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## Merging Remix and React Router | Remix
[remix.run/blog/merging-remix-and-react-router](https://remix.run/blog/merging-remix-and-react-router "Merging Remix and React Router | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

Remix는 React Router v7로 출시 예정할 이야기.
Remix와 React Router는, Vite와 서버 이외는 거의 같은 기능.
이에, React Router를 Remix로 마이그레이션할 필요없이, React Router 업데이트하기만 하면 Remix 기능 사용 가능.
기존 Remix 애플리케이션은, import 패키지 `react-router`로 변경하기만 해도 동작할 예정.


----

## Angular 17 Update: Control Flow &amp; App Builder Migration - ANGULARarchitects
[www.angulararchitects.io/blog/angular-17-update-control-flow-app-builder-migration/](https://www.angulararchitects.io/blog/angular-17-update-control-flow-app-builder-migration/ "Angular 17 Update: Control Flow &amp; App Builder Migration - ANGULARarchitects")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 18가 2024-05-20에 출시되므로, 그 전에 Angular 17으로 업데이트 하자는 글.
Angular 17에는 새로운 제어 흐름과 Vite으로 변경도 포함, 업데이트 방법에 대해.


----

## Introducing Firebase App Hosting
[firebase.blog/posts/2024/05/introducing-app-hosting/](https://firebase.blog/posts/2024/05/introducing-app-hosting/ "Introducing Firebase App Hosting")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firebase</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Firebase App Hosting 관하여.
설정없이 Angular랑 Next.js 지원하는 Cloud Run 기반 호스팅 서비스


----

## State of HTML 2023
[2023.stateofhtml.com/en-US/](https://2023.stateofhtml.com/en-US/ "State of HTML 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">Survey</span></p>

State of HTML 2023 결과 공개.
HTML 엘리먼트나 속성, Web Components, 접근성, 앞으로의 과제나 필요한 기능에 대한 앙케이트


----

## Digging for SSRF in NextJS apps
[www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps](https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps "Digging for SSRF in NextJS apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Next.js 14.1.1에 수정된 SSRF 취약성에 대해.
Server Actions에서 `redirect()` 사용한 path 리다이렉트 하고 있는 API가 있는 경우에, Next.js에서 임의의 URL에 GET 리퀘스트한 내용을 얻을 수 있는 SSRF 취약성

- [Next.js Server-Side Request Forgery in Server Actions · CVE-2024-34351 · GitHub Advisory Database](https://github.com/advisories/GHSA-fr5h-rqp8-mj6g "Next.js Server-Side Request Forgery in Server Actions · CVE-2024-34351 · GitHub Advisory Database")
- [azu/nextjs-CVE-2024-34351: poc](https://github.com/azu/nextjs-CVE-2024-34351 "azu/nextjs-CVE-2024-34351: poc")

----

## Introducing the CSS anchor positioning API  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/anchor-positioning-api](https://developer.chrome.com/blog/anchor-positioning-api "Introducing the CSS anchor positioning API  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Anchor Positioning API에 대해.
컨셉, 기본적인 사용 방법, popover 속성과 `<dialog>`와 조합, `@position-try`에서 대체 위치 지정, 스크롤과 조합


----

## React Compiler – React
[react.dev/learn/react-compiler](https://react.dev/learn/react-compiler "React Compiler – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">babel</span> <span class="jser-tag">document</span></p>

React Compiler 실험적 공개.
Babel 플러그인으로 구현, opt-in 도입 방법이나 `react-compiler-healthcheck`로 호환성 체크, ESLint 플러그인에 대해서도 작성


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Web Platform Status
[webstatus.dev/](https://webstatus.dev/ "Web Platform Status")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">webservice</span></p>

웹 플랫폼 브라우저 상태 정리한 페이지.
기능 마다 브라우저 지원 표시, 검색 가능


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## farzher/fuzzysort: Fast SublimeText-like fuzzy search for JavaScript.
[github.com/farzher/fuzzysort](https://github.com/farzher/fuzzysort "farzher/fuzzysort: Fast SublimeText-like fuzzy search for JavaScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search</span> <span class="jser-tag">library</span></p>

fuzzy search 라이브러리


----
