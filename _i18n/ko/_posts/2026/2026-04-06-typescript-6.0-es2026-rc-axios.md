---
title: "2026-04-06: TypeScript 6.0, ES2026 RC, axios 공급망 공격"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-04-06T01:32:51.276Z
category: JSer
tags:
- TypeScript
- nodejs
- security
- Tools
- React

---

JSer.info #768 - TypeScript 6.0가 출시되었다.

- [Announcing TypeScript 6.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

현재 JavaScript 코드 기반 마지막 출시, Go로 재작성된 TypeScript 7.0 이행 준비를 위한 출시이다. `strict`가 기본적으로 `true`, `target` 기본값이 `es2025`, `module` 기본값이 `esnext`으로 변경됨. `target: es5`이나 `--moduleResolution node`(node10), `--outFile` 비권장이 되어 에러로 변경됨. 새로운 기능으로, `es2025` 타겟 추가, Temporal API 자료형 정의, Map/WeakMap의 `getOrInsert()`/`getOrInsertComputed()` 메서드 추가, TypeScript 7.0 자료형 순서 합치는 `--stableTypeOrdering` 플래그 추가 포함.

---

ECMAScript 2026의 Release Candidate가 공개되었다.

- [Release ES2026 Candidate March 31st 2026 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31)

TC39에 의해 2026년 3월에 승인, 2026년 6월 Ecma General Assembly에서 승인을 거쳐 정식 출시할 예정. ES2026에는, `Array.fromAsync`, JSON.parse source text access, Iterator Sequencing, `Uint8Array`의 Base64 변환, `Math.sumPrecise`, `Error.isError`, Upsert(`Map.prototype.getOrInsert`) 포함될 예정이다.

---

axios의 npm 패키지 공급망 공격이 발생했다.

- [axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)
- [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers)
- [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise)

소셜 엔지니어링으로 관리자 계정을 탈취, 악의있는 `axios@1.14.1`와 `axios@0.30.4`가 공개됨. 이 버전에는 `plain-crypto-js` 멀웨어가 의존관계로 추가되어, postinstall 훅을 통해 macOS/Windows/Linux 대상 Remote Access Trojan(RAT)을 설치하는 구조다.

영향을 받았는지 확인하는 방법은 다음 페이지에 정리되어 있다.

- [Am I affected? - StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan#am-i-affected)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 6.0 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-6-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/ "Announcing TypeScript 6.0 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 6.0 출시.
현재 JavaScript 코드 기반 마지막 출시, Go로 재작성된 TypeScript 7.0으로 이행 준비하는 출시이다.
`strict`가 기본 `true`, `target` 기본값이 `es2025`, `module` 기본값이 `esnext`으로 변경.
`target: es5`, `--moduleResolution node`(node10), `--outFile`, `--esModuleInterop false` 비권장이 되어 에러로 변경.
`es2025` 타겟 추가, Temporal API 자료형 정의 추가, Map/WeakMap의 `getOrInsert()`/`getOrInsertComputed()` 메서드 추가.
Node.js의 Subpath Imports의 `#/` 지원, `--moduleResolution bundler`와 `--module commonjs` 구조 조합 지원.
TypeScript 7.0 자료형 순서 합치는 `--stableTypeOrdering` 플래그 추가


----

## WebKit Features for Safari 26.4 | WebKit
[webkit.org/blog/17862/webkit-features-for-safari-26-4/](https://webkit.org/blog/17862/webkit-features-for-safari-26-4/ "WebKit Features for Safari 26.4 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">CSS</span> <span class="jser-tag">WebTransport</span> <span class="jser-tag">WebAuthentication</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 26.4 출시.
CSS Grid Lanes에 의한 masonry/워터폴 스타일 레이아웃 지원, 이름 뿐이었던 `@container` 쿼리 지원.
`font-size: math`와 `math-depth` 프로퍼티 지원.
CSS Zoom 수정, Scroll-driven Animations 성능 개선.
WebTransport 지원, Keyboard Lock API 지원, ReadableByteStream 지원.
Scoped Custom Element Registries 개선, `Iterator.concat()` 지원.
`<img>`의 `sizes` 속성에서 math 함수 (`min()`/`max()`/`clamp()`) 지원, SVG의 `lighter` 합성연산자 지원.
WebAuthn의 PRF 확장 지원.


----

## Release v20.0.0 · raineorshine/npm-check-updates
[github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0](https://github.com/raineorshine/npm-check-updates/releases/tag/v20.0.0 "Release v20.0.0 · raineorshine/npm-check-updates")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

npm-check-updates v20.0.0 출시.
npm/yarn/pnpm의 설정인 minimum release age 설정을 자동적으로 읽어, cooldown 옵션으로 적용할 수 있음.


----

## Release ES2026 Candidate March 31st 2026 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31](https://github.com/tc39/ecma262/releases/tag/es2026-candidate-2026-03-31 "Release ES2026 Candidate March 31st 2026 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2026のRelease Candidate가 공개됨.
TC39에 2026년 3월 승인되어, 2026년 6월 Ecma GA에서 승인을 거쳐 정식 출시될 예정.


----

## Release v15.0.0 · sindresorhus/got
[github.com/sindresorhus/got/releases/tag/v15.0.0](https://github.com/sindresorhus/got/releases/tag/v15.0.0 "Release v15.0.0 · sindresorhus/got")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Got v15.0.0 출시.
Node.js 22 미만 지원 삭제, 
`promise.cancel()` 삭제하고 AbortController의 `signal` 옵션으로 이행, `isStream` 옵션 삭제.
`responseType: 'buffer'`가 `Buffer` 대신에 `Uint8Array` 반환하도록 변경.
네이티브 FormData API 이용하도록 변경, `strictContentLength` 기본적으로 `true`으로 변경.
RFC 9110에 표준으로 300/304 리스폰스 자동 리다이렉트 폐지


----

## Release 4.18.0 · lodash/lodash
[github.com/lodash/lodash/releases/tag/4.18.0](https://github.com/lodash/lodash/releases/tag/4.18.0 "Release 4.18.0 · lodash/lodash")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">lodash</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

lodash 4.18.0 출시.
`_.unset`과 `_.omit`의 Prototype Pollution 취약성 수정, `_.template` 코드 인젝션 수정.
`lodash.unset`나 `lodash.template` 개별 패키지가 낡아서 수정하고 재공개.


----

## Node.js — Node.js 25.9.0 (Current)
[nodejs.org/en/blog/release/v25.9.0](https://nodejs.org/en/blog/release/v25.9.0 "Node.js — Node.js 25.9.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v25.9.0 출시.
테스너 런너 목 모듈 API에 `defaultExport`와 `namedExports` 옵션을 `exports` 옵션에 통합.
`--max-heap-size` 플래그, Web Crypto으로 TurboSHAKE와 KangarooTwelve 알고리즘 지원.
SEA(Single Executable Applications)에 ESM 엔트리포인트 코드 캐시 지원, 실험적 `stream/iter` 모듈 추가.
`AsyncLocalStorage`에 `using` 스코프 추가, REPL에서 커스텀 에러 번들링 지원.


----

## Release v5.0.0 · lerna-lite/lerna-lite
[github.com/lerna-lite/lerna-lite/releases/tag/v5.0.0](https://github.com/lerna-lite/lerna-lite/releases/tag/v5.0.0 "Release v5.0.0 · lerna-lite/lerna-lite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

lerna-lite v5.0.0 출시.
Node.js 20 지원 종료, Conventional Changelog 레거시 설정 파일 읽기 삭제, `--remove-package-fields` 옵션 삭제.
내부 의존을 자체 구현으로 크기 절감


----
<h1 class="site-genre">읽을거리</h1>

----

## Storybook MCP for React
[storybook.js.org/blog/storybook-mcp-for-react/](https://storybook.js.org/blog/storybook-mcp-for-react/ "Storybook MCP for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">storybook</span> <span class="jser-tag">MCP</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Storybook MCP 서버에 대하여.
AI 에이언트에 의존 UI 컴포넌트 메타데이터(스토리, API, 문서) 제공하는 MCP 서버.
복수 Storybook를 조합함으로 사용하는 Composition에도 대응.
MCP Apps에 대응해서, 챗의 리스폰스에 직접 Story를 포함.


----

## Node.js — Security Bug Bounty Program Paused Due to Loss of Funding
[nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties](https://nodejs.org/en/blog/announcements/discontinuing-security-bug-bounties "Node.js — Security Bug Bounty Program Paused Due to Loss of Funding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Node.js 시큐리티 버그 바운티 프로그램 일시정지에 대하여.
2016년부터 HackerOne의 Internet Bug Bounty(IBB) 프로그램을 운용하고 있었지만, IBB 프로그램이 종료 되어 자금 고갈로 인해 일시정지됨.
자금 80%을 발견, 20%을 수정에 부여했지만, AI에 의한 발견이 확대됨에 밸런스가 변경됨.
취약성 보고자체는 HackerOne 통해서 지속해서 받지만, 보고자에 금전적 제공은 없어짐. 전용 자금 확보될 경우 프로그램 재개가 검토될 예정


----

## Signals, the push-pull based algorithm — Willy Brauner
[willybrauner.com/journal/signal-the-push-pull-based-algorithm](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm "Signals, the push-pull based algorithm — Willy Brauner")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Signal에 의한 push-pull 기반 리엑티브 알고리즘 해설 글.
Signal 기본적인 구조를 보고, 값의 변경 시에 구독으로 알림하는 Push형과, 계신값을 실제로 접근할 때까지 지연평가하는 Pull형 구조에 대해 설명한다.


----

## Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA | The IntelliJ IDEA Blog
[blog.jetbrains.com/idea/2026/03/js-ts-free-support/](https://blog.jetbrains.com/idea/2026/03/js-ts-free-support/ "Core JavaScript and TypeScript Features Become Free in IntelliJ IDEA | The IntelliJ IDEA Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JetBrains</span> <span class="jser-tag">IDE</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span></p>

IntelliJ IDEA v2026.1로, JavaScript/TypeScript/HTML/CSS 코어 기능이 무료로 이용 가능.
지금까지는 Ultimate 버전에서는 제공하고 있던 Web 개발 대상 기능이, Community Edition에서도 이용 가능해짐.
JS/TS 코드 보완이나 리팩토링, ESLint/Prettier 통합, Vite로 프로젝트 구성, npm 스크립트 실행, 의존관계 취약성 검출도 함.


----

## axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity
[www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan "axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

axios의 npm 패키지에 공급망 공격 관련해서.
소셜 엔지니어링으로 관리자 계정 탈취당함, 악의있는 `axios@1.14.1`와 `axios@0.30.4`가 공개됨.
`plain-crypto-js` 멀웨어가 의존관계에 추가됨.
postinstall 훅을 통해 macOS/Windows/Linux 대상 Remote Access Trojan(RAT)을 설치하는 구조.

- [Attackers Are Hunting High-Impact Node.js Maintainers in a C...](https://socket.dev/blog/attackers-hunting-high-impact-nodejs-maintainers "Attackers Are Hunting High-Impact Node.js Maintainers in a C...")
- [The Hidden Blast Radius of the Axios Compromise - Socket](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise "The Hidden Blast Radius of the Axios Compromise - Socket")

----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Introducing EmDash — the spiritual successor to WordPress that solves plugin security
[blog.cloudflare.com/emdash-wordpress/](https://blog.cloudflare.com/emdash-wordpress/ "Introducing EmDash — the spiritual successor to WordPress that solves plugin security")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">CMS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">astro</span> <span class="jser-tag">security</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">wordpress</span></p>

Cloudflare의 서버리스 CMS.
TypeScript로 작성, Astro 6.0을 기반으로 한 오픈소스 (MIT 라이센스) CMS.
플러그인을 독립해 샌드박스 환경 (Dynamic Workers)으로 실행, 플러그인 기원의 보안 문제 해결하는 아키텍처 채용.
MCP이나 CLI에 의한 AI에이전트 연계, x402 프로토콜에 의한 결제 통합 기능도 있음.


----

## vercel-labs/emulate: Local API emulation for CI and no-network sandboxes
[github.com/vercel-labs/emulate](https://github.com/vercel-labs/emulate "vercel-labs/emulate: Local API emulation for CI and no-network sandboxes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vercel</span> <span class="jser-tag">API</span> <span class="jser-tag">testing</span> <span class="jser-tag">CI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">server</span></p>

Vercel/GitHub/Google/Slack/AWS(S3/SQS)의 API를 로컬에서 에뮬레이트하는 도구.
외부 API의 목 서버에서 이용 가능.
각 서비스는 스테이풀한 데이터를 저장하고, OAuth 2.0 플로우나 Webhook에도 대응하고 있음.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ArrowJS — The first UI framework for the agentic era
[arrow-js.com/](https://arrow-js.com/ "ArrowJS — The first UI framework for the agentic era")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">library</span></p>

빌드 단계없이 동작하는 경량 UI 프레임워크. `reactive`, `html`, `component` 3개 함수로 구성.
AI 대상 WebAssembly 샌드박스 안에서 컴포넌트 로직을 분리해 실행하는 기능 갖고 있음.


----
<h1 class="site-genre">도서</h1>

----

## React 본격 입문 | 기술평론사
[gihyo.jp/book/2026/978-4-297-15523-0](https://gihyo.jp/book/2026/978-4-297-15523-0 "React 본격 입문 | 기술평론사")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

2026년 4월 15일 발매.
React 19 기반 입문서.


----
