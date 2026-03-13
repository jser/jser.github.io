---
title: "2026-03-12: TypeScript 6.0 RC, Solid v2.0.0 Beta, Node.js 출시スケジュールの変更"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-03-12T11:45:51.325Z
category: JSer
tags:
- npm
- nodejs
- TypeScript
- React
- Tools

---

JSer.info #766 - TypeScript 6.0 RC가 출시되었다.

- [Announcing TypeScript 6.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

TypeScript 7(Go 기반)으로 이행을 준비한 출시로, 많은 기본 설정 변경과 비권장이 포함되었다.
`strict`가 기본적으로 `true`가 되고, `module`이 기본적으로 `esnext`이 된다, `target`은 기본 `es2025`으로 변경, 기존 프로젝트에 영향이 큰 변경이 있다.
또한, `target: es5`/`--moduleResolution node10`/`--module amd|umd|system`/`--outFile` 비권장화 된다.

---

Solid v2.0.0 Beta가 출시되었다.

- [Release v2.0.0 Beta - The <Suspense> is Over · solidjs/solid](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0)

비동기처리가 일급클래스가 되어, computations가 Promise이나 async iterables를 반환한다.
`<Loading>` 컴포넌트나 `isPending` 에 의한 Pending 상태 추적, `action()`과 `createOptimistic`에 의한 Optimistic Update 구조가 추가됨.
`<Index>`를 `<For keyed={false}>`으로 변경, `createEffect`의 compute/apply 페이즈 분리, `use:` 디렉티브 삭제 같은 파괴적 변경이 있다.

---

Node.js 출시 모델이 2026년 10월부터 변경됨을 발표했다.

- [Node.js — Evolving the Node.js Release Schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)

현재 연 2회 메이저 출시에서 연 1회로 변경, 모든 메이저 출시가 LTS가 된다.
새로운 출시 사이클은, Alpha Phase(10월〜3월)에 Breaking Changes 허용하고, Current Phase(4월〜10월)로 안정화, 그 이후 30개월 LTS 페이즈가 된다.
홀수/짝수 버전 구별이 사라졌고, Node.js 26(2026년 4월)이 현행 모델 마지막 출시이다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v6.3.0 · actions/setup-node
[github.com/actions/setup-node/releases/tag/v6.3.0](https://github.com/actions/setup-node/releases/tag/v6.3.0 "Release v6.3.0 · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GitHub</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

setup-node v6.3.0 출시.
`devEngines` 필드 지원


----

## Release v2.0.0 Beta - The &lt;Suspense&gt; is Over · solidjs/solid
[github.com/solidjs/solid/releases/tag/v2.0.0-beta.0](https://github.com/solidjs/solid/releases/tag/v2.0.0-beta.0 "Release v2.0.0 Beta - The &lt;Suspense&gt; is Over · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Solid</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Solid v2.0.0 Beta 출시.
비동기는 일급클래스로, computations가 Promise나 async iterables를 반환한다.
`<Loading>` 컴포넌트나 `isPending`에 의한 Pending 상태 추적, `action()`과 `createOptimistic`에 의한 Optimistic Update 구조 추가.
`<Index>`를 `<For keyed={false}>` 으로 변경, `createEffect`의 compute/apply 페이즈 분리, `use:` 디렉티브 삭제.


----

## Announcing TypeScript 6.0 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/ "Announcing TypeScript 6.0 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 6.0 RC 출시.
TypeScript 7(Go 언어)로 이행하기 위한 사전 준비 출시로, 많은 기본 설정 변경 및 비권장화가 포함됨.
Beta에서 변경은 `import ... assert {...}` 폐지 연장됨.
`strict` 기본 `true`, `module` 기본 `esnext`, `target` 기본 `es2025`, `types` 기본 `[]`으로 변경.
`target: es5`/`--moduleResolution node10`/`--module amd|umd|system`/`--outFile` 비권장화.
ES2025의 `RegExp.escape`이나 Temporal 자료형 정의 추가, `lib.dom`에 `dom.iterable`와 `dom.asynciterable` 통합.
`this` 사용하지 않는 함수의 context sensitivity 개선, `#/`로 시작하는 subpath imports 지원 추가.
`--moduleResolution bundler`와 `--module commonjs` 조합할 수 있도록.
TypeScript 7으로 이행 보조하는 `--stableTypeOrdering` 플래그 추가.


----

## Astro 6.0 | Astro
[astro.build/blog/astro-6/](https://astro.build/blog/astro-6/ "Astro 6.0 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Vite</span></p>

Astro 6.0 출시.
Vite의 Environment API 사용한 개발 서버 업데이트에 의해, 개발할 때에도 Cloudflare Workers나 Bun/Deno 런타임 실행 가능.
폰트 관리를 자동화하는 Fonts API 추가, 리퀘스트할 때 CMS이나 API 데이터 얻는 Live Content Collections 추가.
CSP 지원이 안정판으로.
Node.js 22 이상 필수로 변경, Vite 7/Shiki 4/Zod 4으로 업그레이드.
Experimental으로, Go에서 Rust 기반으로 재작성한 컴파일러, Queued Rendering, Route Caching API 추가.


----

## Node.js — Evolving the Node.js Release Schedule
[nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule "Node.js — Evolving the Node.js Release Schedule")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">news</span></p>

Node.js 출시 모델을 2026년 10월부터 변경.
현재 연 2회 메이저 출시에서 연 1회로 변경, 모든 출시가 LTS가 됨.
새로운 출시 사이클에는, Alpha Phase(10월 〜 3월)에 Breaking Changes 허용, Current Phase(4년 〜 10월)에 안정화, 그 이후 30개월 LTS 페이즈가 됨.
홀수/짝수 버전 구별이 사라지고, 버전 번호가 연도에 대응(Node.js 27은 2027년).
Node.js 26(2026년 4월)이 현행 모델 최후 출시며, Node.js 27(2027년 4월)부터 새로운 스케쥴 적용.


----

## Chrome 146  |  Release notes  |  Chrome for Developers
[developer.chrome.com/release-notes/146](https://developer.chrome.com/release-notes/146 "Chrome 146  |  Release notes  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 146 출시.
CSS 스크롤 애니메이션, `trigger-scope` 프로퍼티 지원.
`meta name="text-scale"`에 의한 OS/브라우저 텍스트 스케일링 설정 반영, Scoped Custom Element Registry 지원.
`Iterator.concat()` 지원, Sanitizer API 추가, WebAudio의 Playback Statistics API 추가.
WebGPU의 Compatibility mode 지원.


----

## Get features faster with Chrome&#039;s two-week release cycle  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/chrome-two-week-release?hl&#x3D;en](https://developer.chrome.com/blog/chrome-two-week-release?hl=en "Get features faster with Chrome&#039;s two-week release cycle  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">news</span></p>

Chrome 출시 사이클을 2026년 9월 (Chrome 153)부터, 4주 사이클에서 2주 사이클로 변경.
데스크탑, Android, iOS가 대상, Dev 채널과 Canary 채널은 변경 없음.
Extended Stable 채널은 8주 사이클 유지.


----

## RedwoodSDK 1.0: Getting Out of the Weeds | Blog | RedwoodSDK
[rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds](https://rwsdk.com/blog/redwood-v1-getting-out-of-the-weeds "RedwoodSDK 1.0: Getting Out of the Weeds | Blog | RedwoodSDK")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cloudflare Workers 대상 React 프레임워크 RedwoodSDK 1.0 출시.
구 RedwoodJS에서 방침을 변경, 코드 생성이나 암묵적인 규약 의존하지 않은 설계.
Web표준 API(fetch, Request, Response)를 그대로 이용, 설정보다 합성(Composability)를 중시하는 아키텍처 채용.

- [Release v1.0.0 · redwoodjs/sdk](https://github.com/redwoodjs/sdk/releases/tag/v1.0.0 "Release v1.0.0 · redwoodjs/sdk")

----
<h1 class="site-genre">읽을거리</h1>

----

## Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog
[bloomberg.github.io/js-blog/post/temporal/](https://bloomberg.github.io/js-blog/post/temporal/ "Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TC39</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal의 Temporal가 Stage 4가 되어 ES2026에 포함되는 것이 결정되는 경위에 대한 글.
JavaScript의 `Date` 오브젝트가 안고 있는 뮤터블한 설계, 타임존 대응 부족, 애매한 경로 문제를 각 해결하기 위해 Temporal가 어떤 설계했는가 설명하고 있다.
Temporal는 이뮤터블한 설계, 타임존 설정, 달력 네이티브 지원, 나노초 정밀 특정이 갖고 있음.
`ZonedDateTime`/`Instant`/`PlainDate`/`PlainTime` 같은 자료형.`temporal_rs`이나 Bloomberg/Google/Microsoft/Igalia 등 복수 조직에 의한 협력도 소개되어 있음.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Announcing npmx: a fast, modern browser for the npm registry
[npmx.dev/blog/alpha-release](https://npmx.dev/blog/alpha-release "Announcing npmx: a fast, modern browser for the npm registry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">search</span></p>

npm 패키지 검색 사이트 npmx α 출시
패키지 다운로드 통계, 낡은 의존 관계 경고, ESM/CJS 모듈 형식 검출, 설치 크기 분석 기능을 갖고 있음.


----

## flatt-security/setup-takumi-guard-npm: GitHub Action to configure npm with Takumi Guard registry auth via OIDC
[github.com/flatt-security/setup-takumi-guard-npm](https://github.com/flatt-security/setup-takumi-guard-npm "flatt-security/setup-takumi-guard-npm: GitHub Action to configure npm with Takumi Guard registry auth via OIDC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Actions</span></p>

npm 패키지 설치를 시큐리티 프록시 경유해서, 악의있는 패키지를 블록하는 GitHub Action.
npm/pnpm/yarn 대응, 레지스트리를 `https://npm.flatt.tech/`으로 설정함으로 설치할 때 패키지를 체크.
GitHub OIDC 사용해 인증 대응하고, Bot ID를 설정해서 감시로그나 대시보드 가시성을 이용.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## aidenybai/react-grab: Select context for coding agents directly from your website
[github.com/aidenybai/react-grab/tree/main](https://github.com/aidenybai/react-grab/tree/main "aidenybai/react-grab: Select context for coding agents directly from your website")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">AI</span> <span class="jser-tag">library</span></p>

Web사이트 상에 UI 요소를 Inspect해서 React 컴포넌트 명이나 파일 경로, HTML 소스코드 등 컨텍스트 정보를 복사할 수 있는 도구.
복사한 정보를 Cursor나 Claude Code 같은 AI 코딩 에이전트에게 전달해서 이용.
Next.js/Vite/webpack 대응, 플러그인에 의한 커스터마이즈나 Primitives API 의한 독자 UI 구축에도 대응.


----

## dupontcyborg/numpy-ts: Full NumPy, in TypeScript/JavaScript (94% coverage)
[github.com/dupontcyborg/numpy-ts](https://github.com/dupontcyborg/numpy-ts "dupontcyborg/numpy-ts: Full NumPy, in TypeScript/JavaScript (94% coverage)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">math</span></p>

Python의 NumPy를 TypeScript/JavaScript로 재구축한 라이브러리.
NumPy의 507 함수 중 476 함수를 커버하는 .dtype 지정, 브로드캐스팅, 선형대수계산, NumPy 스타일의 슬라이스 기법 지원.
Tree-shakeable한 모듈 구성으로, Node.js와 브라우저 양쪽에서 동작.


----

## pbakaus/impeccable: The design language that makes your AI harness better at design.
[github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable "pbakaus/impeccable: The design language that makes your AI harness better at design.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">AI</span> <span class="jser-tag">Design</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

AI 코딩 에이전트 대상 프론트엔드 디자인 명령어 셋.
타이포그라피, 색채, 공간설계, 모션, 인터렉션, 반응형 디자인, UX 라이팅 스킬 정의.
AI가 생성하는 UI/UX 디자인에 의한 안티 패턴의 가이던스도 포함.
Claude Code, Cursor, Gemini CLI 같은 AI 도구에 대응.


----
