---
title: "2020-02-25: TypeScript 3.8 정식 릴리스, ESLint 7.0.0 변경 예정 사항"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-02-25T02:30:48.221Z
category: JSer
tags:
- TypeScript
- ESLint

---

JSer.info #476 - TypeScript 3.8이 정식 릴리스 됐습니다.

- [Announcing TypeScript 3.8 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8/)

타입 정의만 가져오거나 내보낼 수 있는 `import type` / `export type`이 추가됐고 ECMAScript Proposal Stage 3의 [ECMAScript Private Fields](https://github.com/tc39/proposal-private-fields), [Top-Level `await`](https://github.com/tc39/proposal-top-level-await)을 지원합니다.

또, `tsconfig.json`의 `target`과 `module` 옵션에 `es2020`이 추가됐으며 `watchOptions`으로 `--watch` 시의 동작 방식을 설정할 수 있습니다. 이어 `assumeChangesOnlyAffectDirectDependencies` 컴파일 옵션을 활성화해 "Fast and Loose"한 인크리멘탈 빌드를 사용할 수 있도록 변경됐습니다. 이 옵션을 활성화하면 모든 파일을 확인하고 다시 빌드(rechecking/rebuilding) 하지 않고 변경된 파일만 확인하고 빌드 합니다.

----

ESLint 7(현재 [v7.0.0-alpha.1](https://github.com/eslint/eslint/releases/tag/v7.0.0-alpha.1)가 공개돼 있음)의 변경 예정 사항이 정리된 문서가 공개돼 있습니다.

- [What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0)

이 문서에는 주로 비호환적 변경 사항에 대해 다루고 있습니다.

Node.js 8.x의 지원을 종료하며 `CLIEngine` 클래스를 비권장 함과 동시에 `ESLint` 클래스가 도입될 예정입니다.
`ESLint` 클래스에 대해서는 RFC에 정리돼 있습니다. 간단하게 기존의 `CLIEngine` 클래스는 동기적으로 처리했던 것에 비해 `ESLint`는 비동기 처리에 대응합니다.

- [New: `ESLint` Class Replacing `CLIEngine` by mysticatea · Pull Request #40 · eslint/rfcs](https://github.com/eslint/rfcs/pull/40)

또, ESLint에 포함돼 있던 Node.js나 CommonJS 관련 규칙을 [`eslint-plugin-node`](https://github.com/mysticatea/eslint-plugin-node)로 옮길 예정입니다. 
이 외로는 directive comments에 코멘트를 작성할 수 있도록 변경되며 홈 디렉터리에 있는 `~/.eslintrc` 이용 시 경고가 출력됩니다. 이어 기본 ignore patterns가 갱신 됩니다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 3.8 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-8/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-8/ "Announcing TypeScript 3.8 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.8이 릴리스됐습니다.
`import type` / `export type`가 추가됐고 Stage 3의 ES Private Fields와 Top-Level `await`을 지원합니다.
이어 `target`과 `module` 옵션에 `es2020`이 추가됐으며 `watchOptions`로 `--watch` 시의 도악ㅈㅇ르 설정할 수 있도록 변경됐습니다.


----

## Node v13.9.0 (Current) | Node.js
[nodejs.org/en/blog/release/v13.9.0/](https://nodejs.org/en/blog/release/v13.9.0/ "Node v13.9.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Node v13.9.0이 릴리스 됐습니다.
`async_hooks` 모듈에 `executionAsyncResource`가 추가됐고 `crypto` 모듈에 `diffieHellman`가 추가됐습니다.
또, Diagnostic Report가 worker_threds를 지원합니다.

- [Diagnostic Report | Node.js v13.9.0 Documentation](https://nodejs.org/api/report.html "Diagnostic Report | Node.js v13.9.0 Documentation")

----

## Release Initial Release: 1.0.0 · reduxjs/cra-template-redux
[github.com/reduxjs/cra-template-redux/releases/tag/v1.0.0](https://github.com/reduxjs/cra-template-redux/releases/tag/v1.0.0 "Release Initial Release: 1.0.0 · reduxjs/cra-template-redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">Tools</span></p>

create-react-app 용 Redux 템플릿 1.0.0이 릴리스됐습니다.
`npx create-react-app my-app --template redux` 명령어로 설치할 수 있습니다.
Redux Toolkit을 이용하고 있습니다.

- [Redux Toolkit | Redux Toolkit](https://redux-toolkit.js.org/ "Redux Toolkit | Redux Toolkit")

----

## Release 3.4.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.4.0](https://github.com/avajs/ava/releases/tag/v3.4.0 "Release 3.4.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 3.4.0이 릴리스됐습니다.
테스트 실패없이 Assertion을 살펴볼 수 있는 `t.try()`를 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## Understanding the “Initial”, “Inherit” and “Unset” CSS Keywords
[medium.com/@elad/understanding-the-initial-inherit-and-unset-css-keywords-2d70b7121695](https://medium.com/@elad/understanding-the-initial-inherit-and-unset-css-keywords-2d70b7121695 "Understanding the “Initial”, “Inherit” and “Unset” CSS Keywords")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS의 `initial`, `inherit`, `unset`, `revert`에 대해서 설명합니다.
CSS 프로퍼티 초기값의 차이와 각 의미에 대해서 작성돼 있습니다.


----

## The Circuit Breaker Pattern
[blog.bearer.sh/circuit-breaker-design-pattern/](https://blog.bearer.sh/circuit-breaker-design-pattern/ "The Circuit Breaker Pattern")
<p class="jser-tags jser-tag-icon"><span class="jser-tag"> node</span> <span class="jser-tag">article</span></p>

Node.js로 Circuit Breaker 패턴을 살펴보면서 학습하는 튜토리얼입니다.

- [Building a Circuit Breaker in Node.js (Part 1)](https://blog.bearer.sh/build-a-circuit-breaker-in-node-js/ "Building a Circuit Breaker in Node.js (Part 1)")

----

## 가상 DOM은 정말 "빠른가?" DOM 조작의 새로운 사고를 프레임워크를 구현해 이해하자 - 엔지니어Hub｜젊은 Web 엔지니어의 커리어를 생각하다!(일본어)
[employment.en-japan.com/engineerhub/entry/2020/02/18/103000](https://employment.en-japan.com/engineerhub/entry/2020/02/18/103000 "가상 DOM은 정말 \"빠른가\" DOM 조작의 새로운 사고를 프레임워크를 구현해 이해하자 - 엔지니어Hub｜젊은 Web 엔지니어의 커리어를 생각하다!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VirtualDOM</span> <span class="jser-tag">article</span></p>

Virtual DOM란 무엇이며 어떻게 구현돼 있는지 소개합니다.
왜 Virtual DOM은 느리기 어려운지에 대해서도 이야기합니다.


----

## Aborting a fetch request
[meetguns.com/blog/aborting-a-fetch-request/](https://meetguns.com/blog/aborting-a-fetch-request/ "Aborting a fetch request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

`AbortController`를 사용해 Fetch의 취소 기능을 구현하는 방법을 소개합니다.


----

## Angular 9: What’s New?
[auth0.com/blog/angular-9-whats-new/](https://auth0.com/blog/angular-9-whats-new/ "Angular 9: What’s New?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 9의 변경 사항이 정리돼 있습니다.


----

## What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0](https://eslint.org/blog/2020/02/whats-coming-in-eslint-7.0.0 "What's coming in ESLint v7.0.0 - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint 7.0.0의 변경 예정 사항에 대해 소개돼 있습니다.
`CLIEngine` 클래스는 비권장 되며 새로운 `ESLint` 클래스가 도입됩니다. 그리고 Node.js나 CommonJS와 관계된 규칙은 `eslint-plugin-node`로 옮겨집니다.
또, directive comments에 코멘트를 작성할 수 있으며 `~/.eslintrc` 이용 시 경고가 출력되고 기본 ignore patterns이 갱신됩니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## benawad/destiny: Prettier for File Structures
[github.com/benawad/destiny](https://github.com/benawad/destiny "benawad/destiny: Prettier for File Structures")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

프로젝트의 파일 구조를 컴포넌트 별로 분리되도록 성형하는 도구입니다.


----

## suchipi/hex-engine: A modern 2D game engine for the browser.
[github.com/suchipi/hex-engine](https://github.com/suchipi/hex-engine "suchipi/hex-engine: A modern 2D game engine for the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">canvas</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

Canvas를 사용한 2D 게임 엔진 라이브러리입니다. React에서 영감 받아 설계된 API를 제공합니다.
음성 동기, 스프라이트 시트와 에니메이션, 물리 엔진 등을 지원합니다.
또 Aseprite, Tiled, BMFont 등 오쏘링 도구도 제공하고 있습니다.

- [Aseprite - Animated sprite editor & pixel art tool](https://www.aseprite.org/ "Aseprite - Animated sprite editor &amp; pixel art tool")
- [Tiled Map Editor | A flexible level editor](https://www.mapeditor.org/ "Tiled Map Editor | A flexible level editor")
- [BMFont - AngelCode.com](https://www.angelcode.com/products/bmfont/ "BMFont - AngelCode.com")

----
