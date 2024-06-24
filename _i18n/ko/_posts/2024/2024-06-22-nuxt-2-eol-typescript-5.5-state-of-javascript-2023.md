---
title: "2024-06-22: Nuxt 2 EOL, TypeScript 5.5, State of JavaScript 2023"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-06-22T06:30:30.339Z
category: JSer
tags:
- Vue
- ECMAScript
- nodejs
- Chrome
- proposal

---

JSer.info #697 - Nuxt 2가 2024년 6월 30일로 End-of-Life (EOL) 된다는 소식이에요.

- [Nuxt 2 End-of-Life (EOL) · Nuxt Blog](https://nuxt.com/blog/nuxt2-eol)

Nuxt 2.x 최종판 2.18.0가 6월 말에 출시될 예정이며, 이후로는 보안 업데이트 마저 공식적으로는 제공하지 않아요.

---

TypeScript 5.5 출시되었어요.

- [Announcing TypeScript 5.5 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/)

TypeScript 5.5에는, 함수에서 type predicates를 추론할 수 있어서, `Array.prototype.filter` 같은 필터링을 간결하게 작성할 수 있어요.
또한, Stage 3의 Set Methods 지원, JSDoc에서 `@import {foo} from "foo"` 지원, 정규표현 기본적으로 구문 체크 지원, `isolatedDeclarations` 지원되어요.

`isolatedDeclarations`는, 각각의 TS 파일에 명시적인 자료형 주석 작성을 강제함으로, 복잡한 자료형 추론할 필요없는 상태의 TS 파일을 다루기 위한 옵션이에요.
이에, `isolatedDeclarations`가 유의미한 프로젝트에는, 파일 단위로 자료형 체크가 가능함으로 병렬로 다룰 수 있어 되어, `tsc` 이 외 도구에서도 자료형을 다루기 쉬운 장점이 있어요.

- [Faster TypeScript builds with --isolatedDeclarations by Titian-Cornel Cernicova-Dragomir - Video recording - GitNation](https://portal.gitnation.org/contents/faster-typescript-builds-with-isolateddeclarations)
- [명시적인 자료형 주석으로 인한 추론 비용 절감하는 접근법](https://zenn.dev/cybozu_frontend/articles/ts-explicit-type-annotation)

이미 oxc나 swc는, 이 `isolatedDeclarations` 지원하고, 자료형 정의 파일 `d.ts` 출력에 대응을 진행하고 있어요.

- <https://x.com/kdy1dev/status/1804363859014357303>
- [feat(transformer-dts): `--isolatedDeclarations` dts transform by Dunqing · Pull Request #3664 · oxc-project/oxc](https://github.com/oxc-project/oxc/pull/3664)

그 외로는, 설정 파일 내에 `${configDir}` 템플릿 값 지원, `typescript` 패키지 크기 절감, Named Import 지원, `transpileDeclaration` API 추가도 있어요.
또한, `out`나 `target: ES3` 같은 비권장 옵션이 무효화되어, `ignoreDeprecations` 옵션 지정하지 않으면 이용할 수 없도록 변경되었어요.

---

State of JavaScript 2023 앙케이트 결과가 공개되었어요.

- [State of JavaScript 2023](https://2023.stateofjs.com/en-US/)

JavaScript 언어 기능, 프레임워크, 도구, 테스트, TypeScript 등에 관한 앙케이트 결과에요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Nuxt 2 End-of-Life (EOL) · Nuxt Blog
[nuxt.com/blog/nuxt2-eol](https://nuxt.com/blog/nuxt2-eol "Nuxt 2 End-of-Life (EOL) · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">news</span></p>

Nuxt 2는 2024년 6월 30일로 End-of-Life (EOL).
Nuxt 2.x 최종판 2.18.0이 6월말에 출시 예정


----

## Nuxt 3.12 · Nuxt Blog
[nuxt.com/blog/v3-12](https://nuxt.com/blog/v3-12 "Nuxt 3.12 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v3.12 출시.
Nuxt 4 동작을 opt-in해서 체험할 수 있는 `compatibilityVersion: 4` 옵션 추가, `multiApp` 옵션 추가, 필요하지 않은 exprimental 옵션 삭제

- [Upgrade Guide · Get Started with Nuxt](https://nuxt.com/docs/getting-started/upgrade#testing-nuxt-4 "Upgrade Guide · Get Started with Nuxt")

----

## New in Chrome 126  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-126?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-126?hl=en "New in Chrome 126  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 126 출시.
Cross-document view transitions 지원, CloseWatcher API 다시 유효화.
import assertion의 `assert` 구문 삭제

- [Chrome 126  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/126 "Chrome 126  |  Release notes  |  Chrome for Developers")

----

## Electron 31.0.0 | Electron
[www.electronjs.org/blog/electron-31-0](https://www.electronjs.org/blog/electron-31-0 "Electron 31.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 31 출시.
Chromium 125, Node.js 20.14, V8 12.6으로 업데이트.
WebSQL 삭제, File System API 지원


----

## Release Version 8.12.0 · acornjs/acorn
[github.com/acornjs/acorn/releases/tag/8.12.0](https://github.com/acornjs/acorn/releases/tag/8.12.0 "Release Version 8.12.0 · acornjs/acorn")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

acorn 8.12.0 출시.
ES2025의 duplicate capture group names in regular expressions 지원


----

## Bun v1.1.13 | Bun Blog
[bun.sh/blog/bun-v1.1.13](https://bun.sh/blog/bun-v1.1.13 "Bun v1.1.13 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.13 출시.
`worker_thread`의 `eval` 옵션 지원, `URL.createObjectURL` 지원, `expect` 커스텀 메세지 지원


----

## Version 4.0 released : Node-RED
[nodered.org/blog/2024/06/20/version-4-0-released](https://nodered.org/blog/2024/06/20/version-4-0-released "Version 4.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node-RED 4.0 출시.


----

## Announcing TypeScript 5.5 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-5/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-5/ "Announcing TypeScript 5.5 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.5 출시.
함수에서 type predicates 추론할 수 있게 되어, `Array.prototype.filter`에서 필터링이 간결히 작성 가능.
Stage 3의 Set Methods 지원.
JSDoc에서 `@import {foo} from "foo"` 지원, 정규표현을 기본적으로 구문 체크 지원, `isolatedDeclarations` 지원.
설정 파일 내에 `${configDir}` 템플릿 값 지원.
`typescript` 패키지 크기 절감, Named Import 지원, `transpileDeclaration` API 추가.
`transpileModule`와 `transpileDeclaration`에서의 빌드 시간 개선.
`out`나 `target: ES3` 비권장 옵션이 무효화로 되어, `ignoreDeprecations` 옵션 지정하지 않으면 사용할 수 없게 변경


----
<h1 class="site-genre">읽을거리</h1>

----

## ECMAScript proposal updates @ 2024-06 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/06/15/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/06/15/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-06 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2024년 6월 TC39 Meeting으로 인한 ECMAScript Proposal 상태 변경 모음.


----

## Codemod partnering with the React team
[codemod.com/blog/react-announcement](https://codemod.com/blog/react-announcement "Codemod partnering with the React team")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 19 관련 codemod

- [codemod/packages/codemods/react/19 at main · codemod-com/codemod](https://github.com/codemod-com/codemod/tree/main/packages/codemods/react/19 "codemod/packages/codemods/react/19 at main · codemod-com/codemod")

----

## Build Stunning Responsive Card Tables with CSS4 &amp; CSS5 - DEV Community
[dev.to/subu\_hunter/build-stunning-responsive-card-tables-with-css4-css5-1fai](https://dev.to/subu_hunter/build-stunning-responsive-card-tables-with-css4-css5-1fai "Build Stunning Responsive Card Tables with CSS4 &amp; CSS5 - DEV Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Table과 scroll-snap을 사용한 carousel 스러운 카드 타입 테이블 디자인에 대해


----

## Node.js Security Progress Report: Redefining Security Processes and Key Initiatives | OpenJS Foundation
[openjsf.org/blog/nodejs-security-progress-report-may-2024?utm\_content&#x3D;297186945&amp;utm\_medium&#x3D;social&amp;utm\_source&#x3D;twitter&amp;hss\_channel&#x3D;tw-91985735](https://openjsf.org/blog/nodejs-security-progress-report-may-2024?utm_content=297186945&utm_medium=social&utm_source=twitter&hss_channel=tw-91985735 "Node.js Security Progress Report: Redefining Security Processes and Key Initiatives | OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js 보안에 대한 보고서.
`--experimental-policy` 삭제, Permission Model의 Initiative phase 완료


----

## State of JavaScript 2023
[2023.stateofjs.com/en-US/](https://2023.stateofjs.com/en-US/ "State of JavaScript 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span></p>

State of JavaScript 2023 결과 공개.
JavaScript 언어 기능, 프레임워크, 도구, 테스트, TypeScript에 대한 앙케이트


----
