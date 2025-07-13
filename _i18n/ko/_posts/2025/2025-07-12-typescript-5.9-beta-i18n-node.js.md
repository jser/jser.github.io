---
title: "2025-07-12: TypeScript 5.9 Beta, i18n와 로컬라이즈, Node.js 모던한 기능"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-07-12T07:52:38.994Z
category: JSer
tags:
- TypeScript
- nodejs
- MCP
- Vue
- vercel

---

JSer.info #741 - TypeScript 5.9 Beta가 출시되었다.

- [Announcing TypeScript 5.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/)

`tsc --init` 생성하는 설정을 변경, `import defer` 구문 지원, `--module node20` 옵션 추가가 포함. 또한, 자료형 체크 개선 및 성능 향상도 있음.

---

Patreon 국제화와 로컬라이즈 구현에 대한 글이 공개되었다.

- [4 Untranslatable Words Behind Patreon's Internationalization Overhaul](https://www.patreon.com/posts/133137028)

조건식으로 문장을 나눌 때 주의점, 수치표현에서 Intl API 활용, 복수형 표현 로컬라이즈, 로컬라이즈로 인한 주의점 정리.
또한, 로컬라이즈 시스템 이행할 때 일어난 문제와 해결 방법에 대해서도 작성.

---

다음 글에서는, 2025년 Node.js에서 모던한 기능과 패턴에 대해 정리됨.

- [Modern Node.js Patterns for 2025](https://kashw1n.com/blog/nodejs-2025/)

ESM, built-in fetch API, Worker threads에 의한 병렬처리, AbortController에 의한 취소처리, 최신 Node.js 기능 활용 방법이 설명되어 있음. Permission model이나 Single Executable Applications 신기능에 대해서도 다룸.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 5.9 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-9-beta/ "Announcing TypeScript 5.9 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.9 Beta 출시.
`tsc --init`으로 생성하는 설정을 변경, `import defer` 지원, `--module node20` 지원


----

## The future of Nuxt​ · nuxt/nuxt · Discussion #32559
[github.com/nuxt/nuxt/discussions/32559](https://github.com/nuxt/nuxt/discussions/32559 "The future of Nuxt​ · nuxt/nuxt · Discussion #32559")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">vercel</span> <span class="jser-tag">news</span></p>

Nuxt.js 개발하는 NuxtLabs가 Vercel에 인수

- [NuxtLabs joins Vercel - Vercel](https://vercel.com/blog/nuxtlabs-joins-vercel "NuxtLabs joins Vercel - Vercel")

----

## Node.js — Node v24.4.0 (Current)
[nodejs.org/en/blog/release/v24.4.0](https://nodejs.org/en/blog/release/v24.4.0 "Node.js — Node v24.4.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v24.4.0 출시.
`fs.mkdtempDisposableSync` 추가, `--watch-kill-signal`フラグ 추가


----

## Release v5.100.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.100.0](https://github.com/webpack/webpack/releases/tag/v5.100.0 "Release v5.100.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack v5.100.0 출시.
HMR의 ES Modules output 지원, `using` 지원, Defer Module Evaluation 지원.
`virtual:` 스키마 지원하는 VirtualUrlPlugin 추가


----

## Release v1.54.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.54.0](https://github.com/microsoft/playwright/releases/tag/v1.54.0 "Release v1.54.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.54.0 출시.
`partitionKey` 옵션 추가, html reporter에 `noSnippets` 옵션 추가.
`--user-data-dir` 플러그로 유저 데이터 디렉토리 지정 가능


----
<h1 class="site-genre">읽을거리</h1>

----

## Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog
[blog.nginx.org/blog/quickjs-engine-support-for-njs](https://blog.nginx.org/blog/quickjs-engine-support-for-njs "Modern JavaScript in NGINX: QuickJS Engine Support for njs – NGINX Community Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nginx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

NGINX의 njs은 QuickJS 엔진으로 선택해 이용 가능


----

## JavaScript scope hoisting is broken
[devongovett.me/blog/scope-hoisting.html](https://devongovett.me/blog/scope-hoisting.html "JavaScript scope hoisting is broken")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">article</span></p>

Rollup이 하는 Scope Hoisting은, Code splitting과 개념과 충돌해서 문제가 발생하는 것에 대한 글.
모듈 실행순서 문제나 모듈을 함수로 래퍼할 때 최적화 문제에 대하여


----

## 4 Untranslatable Words Behind Patreon's Internationalization Overhaul
[www.patreon.com/posts/133137028](https://www.patreon.com/posts/133137028 "4 Untranslatable Words Behind Patreon's Internationalization Overhaul")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">i18n</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

로컬라이즈 된 컨텐츠를 작성할 때 조심하는 것.

- 조건식에서 문장을 나눌 때는, 완전한 문장으로 나눈다
- 수치 표현은 늘 Intl 이용
- 조건 표현도 로컬라이즈한다

로컬라이즈 시스템 이행할 때 일어난 문제와 해결 방법도 다룬다


----

## Modern Node.js Patterns for 2025
[kashw1n.com/blog/nodejs-2025/](https://kashw1n.com/blog/nodejs-2025/ "Modern Node.js Patterns for 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

최신 Node.js에서 이용 가능한 기능 관련하여.
ESM, `node:` prefix, built-in fetch API이나 testing framework 이용, top-level await.
Worker threads에 의한 병렬처리, AbortController에 의한 취소 처리, async iterators에 의한 이벤트 처리.
Permission model, import maps에 의한 모듈 해결, Single Executable Applications에 의한 단일 실행 가능 파일 작성 관련


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## xmcp — The TypeScript MCP framework
[xmcp.dev/](https://xmcp.dev/ "xmcp — The TypeScript MCP framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">MCP</span> <span class="jser-tag">library</span></p>

TypeScript의 MCP 서버 프레임워크


----

## typescript-eslint/tsgolint: ✨ Experimental proof-of-concept typescript-go powered JS/TS linter written in Go
[github.com/typescript-eslint/tsgolint](https://github.com/typescript-eslint/tsgolint "typescript-eslint/tsgolint: ✨ Experimental proof-of-concept typescript-go powered JS/TS linter written in Go")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">library</span></p>

TSLint 규칙을 tsgo로 동작시키면 어느 정도 빨라지는가 실험적 구현.
ESLint의 AST으로 변환없이 TS AST를 그대로 다루는 변경도 있어서, 20-40배 정도 빨리 체크


----

## josdejong/jsonrepair: Repair invalid JSON documents
[github.com/josdejong/jsonrepair](https://github.com/josdejong/jsonrepair "josdejong/jsonrepair: Repair invalid JSON documents")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Invalid한 JSON 문자열을 JSON으로 고쳐주는 도구


----
