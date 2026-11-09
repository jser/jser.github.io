---
title: "2026-11-09: TypeScript 7.1 Beta, Node.js 26 LTS/27 Alpha, Safari 27.1"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-11-09T00:33:58.440Z
category: JSer
tags:
- TypeScript
- nodejs
- safari
- browser
- css
- WebAPI

---

JSer.info #782 - TypeScript 7.1 Beta가 출시했다.

- [Announcing TypeScript 7.1 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/)

Ambient Modules에서 Import Attributes, `import source`/`import.source()`에 대응했다.
`--target es2026`/`--lib es2026`가 추가되어, `Promise.allKeyed` 자료형 정의도 추가된다.
또한, `typescript/sync`/`typescript/async` 새로운 API, 임베드를 다루는 Content Mappers가 추가된다.

---

Node.js 26.13.0가 출시되어, Node.js 26 계열이 코드네임 Lithium이며 LTS으로 이행됐다.

- [Node.js — Node.js 26.13.0 (LTS)](https://nodejs.org/en/blog/release/v26.13.0)

Node.js 26 계열은 2029년 4월말까지 지원.
Node.js 25 이후 Linux 공식 바이너리는 `libatomic`로 링크되어, 오래된 LTS에서 업데이트시에는 별도 설치 필요한 경우가 있다.

또한, Node.js 27 Alpha가 출시됐다.

- [Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0)

Node.js 27부터는, [출시 스케쥴](https://nodejs.org/en/blog/announcements/evolving-the-nodejs-release-schedule)가 변경된다.
메이저 출시는 연 2회에서 연1회가 되며, 홀수 짝수 구별없이 각 메이저 버전이 LTS로 이행된다.
6개월은 Alpha, 6개월은 Current를 거쳐, 30개월 LTS으로 지원된다.
Node.js 27는, 2027년 4월에 Current, 동년 10월에 LTS로 이행될 예정.

V8 15.6으로 업데이트 되어, `Math.sumPrecise()`/`Iterator.zip()`에 대응한다.
파괴적 변경으로, 힙 상한 기존 값 변경이 있다.
`Buffer`/`ArrayBuffer` 메모리와 힙 상한이 도입된다.
`v8.serialize()` 출력 형식이 변경되어, 구버전에서는 읽을 수 없다.
그 외로는, `node:vfs` 플래그가 필요없어져, 환경변수 접근제어하는 `--allow-env`, 실험적 `net/promises` API가 추가된다.

---

Safari 27.1가 출시됐다.

- [WebKit Features for Safari 27.1 | WebKit](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/)

iPhone Duo 대상으로 Device Posture API와 Viewport Segments API를, 기능 플래그 조건으로 실험적인 지원한다.
`device-posture` 미디어 쿼리나 `navigator.devicePosture`으로 접힌 상태를 얻는다.
또한, `window.viewport.segments`이나 CSS 환경 변수에서 화면 분할 영역을 얻는다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 7.1 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-1-beta/ "Announcing TypeScript 7.1 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 7.1 Beta 출시.
Ambient Modules로 Import Attributes를 지원, `import source`/`import.source()`에 대응.
`--target es2026`/`--lib es2026` 추가, `Promise.allKeyed` 자료형 정의 추가.
`typescript/sync`/`typescript/async` 새로운 API, 임베디드된 코드를 다루는 Content Mappers 추가


----

## Nuxt 4.6 · Nuxt Blog
[nuxt.com/blog/v4-6](https://nuxt.com/blog/v4-6 "Nuxt 4.6 · Nuxt Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt v4.6.0 출시.
동봉된 Nuxt CLI v4으로 `nuxt init` 삭제, `npm create nuxt@latest`으로 통일.
서버 처리 공통 API가 되는 `nuxt/server`, `runtimeConfig.appSecret`과 세션 관리 API 추가.
`experimental.routeTypedFetch`으로 `$fetch`/`useFetch` 자료형 추론을 갱신하며, 자료형 체크 성능을 개선.
Vue Vapor와 상호운용, `createUseFetch`/`createUseAsyncData`의 `addons`, 실험적인 `@nuxt/vite-server` 추가.
`my-bad`에 의한 개발 시의 에러 표시, `nuxt dev` 대화 판넬, `nuxt curl`/`nuxt task` 명령어 추가


----

## Node.js — 2026년 10월 21일（화） 보안 출시
[nodejs.org/en/blog/vulnerability/october-2026-security-releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases "Node.js — 2026년 10월 21일（화） 보안 출시")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 22.23.4/24.22.1/26.12.1 보안 출시.
중요도 High 포함한 10건 취약성 수정.
`dns.resolve`에서의 NUL 문자에 의한 이름 이름 단축, TLS 증명서 호스트명 검증 회피, Brotli 디코더 영역 외 작성을 수정.
`crypto.randomUUID()`와 `crypto.randomInt()` 난수캐시가 스냅숏으로 보존되는 문제 수정.
`fs.realpathSync`에 의한 Permission Model 회피 수정.
또한, c-ares/Undici/OpenSSL/SQLite 의존 관계 갱신.


----

## WebKit Features for Safari 27.1 | WebKit
[webkit.org/blog/18486/webkit-features-for-safari-27-1/](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/ "WebKit Features for Safari 27.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">css</span> <span class="jser-tag">WebAPI</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 27.1 출시.
iPhone Duo 대상 Device Posture API와 Viewport Segments API를 기능 플래그 조건으로 실험적 지원.
`device-posture` 미디어쿼리나 `navigator.devicePosture`에서 접힘 상태 얻음.
`window.viewport.segments`이나 CSS 환경 변수로 화면 분할 영역 얻음.


----

## Release v10.0.0-beta.0 · TypeStrong/ts-loader
[github.com/TypeStrong/ts-loader/releases/tag/v10.0.0-beta.0](https://github.com/TypeStrong/ts-loader/releases/tag/v10.0.0-beta.0 "Release v10.0.0-beta.0 · TypeStrong/ts-loader")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

ts-loader v10.0.0-beta.0 출시.
TypeScript 7.1 이상/Node.js 22 이상을 필수로, 컴파일 처리를 `typescript/sync` API으로 이행.
`compilerOptions`/`context`/`happyPackMode` 로더 옵션을 삭제.


----

## Release vite-plus v1.4.0 · voidzero-dev/vite-plus
[github.com/voidzero-dev/vite-plus/releases/tag/v1.4.0](https://github.com/voidzero-dev/vite-plus/releases/tag/v1.4.0 "Release vite-plus v1.4.0 · voidzero-dev/vite-plus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">CLI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vite+ 1.4.0 출시.
`vpx`으로 TypeScript/JavaScript 파일 실행과 `--watch`에 의한 감시 대응, `vp migrate`으로 tsx에서 이행을 지원.
`vp check --deny-warnings`, 레지스트리 팀을 관리하는 `vp pm team` 추가.
글로벌 CLI 의존 관계를 출시마다 lock 파일에서 설치하도록 변경


----

## Node.js — Node.js 26.13.0 (LTS)
[nodejs.org/en/blog/release/v26.13.0](https://nodejs.org/en/blog/release/v26.13.0 "Node.js — Node.js 26.13.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v26.13.0 출시.
Node.js 26 계열이 코드네임 Lithium으로 하고 LTS으로 이행, 2029년 4월말까지 지원.
Node.js 25 이후 Linux 공식 바이너리는 `libatomic` 링크되어, 오래된 LTS에서 갱신할 때 별도 설치를 필요로 하는 경우가 있음.


----

## Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)
[nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0](https://nodejs.org/en/blog/release/v27.0.0-alpha.0.0.0 "Node.js — Node.js 27.0.0-alpha.0.0.0 (Alpha)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v27.0.0-alpha.0.0.0 출시.
파괴적 변경으로, 힙상 상한 기존값을 변경, `Buffer`/`ArrayBuffer` 메모리 상한에 도입하도록 변경.
`v8.serialize()` 출력 형식을 변경, 구버전에서의 호출 비대응.
V8 15.6으로 업데이트와 `Math.sumPrecise()`/`Iterator.zip()` 지원.
`node:vfs` 플래그없도록 변경, 환경변수 접근제어하는 `--allow-env` 추가, 실험적인 `net/promises` API 추가


----

## Release v1.0.0 · dy/jz
[github.com/dy/jz/releases/tag/v1.0.0](https://github.com/dy/jz/releases/tag/v1.0.0 "Release v1.0.0 · dy/jz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">compiler</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript를 WebAssembly에 컴파일하는 JZ v1.0.0 출시.


----

## Release v1.65.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.65.0](https://github.com/microsoft/playwright/releases/tag/v1.65.0 "Release v1.65.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Playwright v1.65.0 출시.
파괴적 변경으로, TypeScript 클래스 필드가 `useDefineForClassFields`에 따르도록 변경, 클릭 조작으로 `inert` 해제를 갖도록 변경.
Cookie 조합을 RFC 6265으로 합쳐져, `APIRequestContext`의 `params`를 기존 쿼리에 기록하도록 변경.
`bunx --bun playwright test`으로 Bun 상에서 테스트 실행에 대응, `failures` 레포터와 `onlyFailures` 옵션 추가.
테스트를 단독으로 실행하는 `lock: '-exclusive-'`, `cdpSession.send()`의 `timeout`/`signal` 옵션을 추가


----
<h1 class="site-genre">읽을거리</h1>

----

## Unload event deprecated in Chrome  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/unload-deprecated-in-chrome](https://developer.chrome.com/blog/unload-deprecated-in-chrome "Unload event deprecated in Chrome  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Chrome 155에서 `unload` 이벤트 비권장화가 완료되고, 기본적으로 동작하지 않도록 됨.
이벤트 신뢰성이나 BFCache으로 영향, 계단적 적용 경위에 대해 해설.
Permissions Policy이나 Chrome Enterprise 설정에 의한 옵트아웃로 계속 이용 가능.


----

## Rebuilding the global town square from scratch
[blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch](https://blog.x.com/en/engineering/rebuilding-the-global-town-square-from-scratch "Rebuilding the global town square from scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">SSR</span> <span class="jser-tag">performance</span> <span class="jser-tag">AI</span> <span class="jser-tag">article</span></p>

X.com의 Web 애플리케이션을 재구축한 배경과 이행 방법에 대하여.
React/Relay/Fastify를 사용해, 이용자/검색 크롤러/링크 프리뷰 대상을 나눴던 3가지 서버를 통합.
Streaming HTML, GraphQL 리스폰스 재이용, JavaScript 분할이나 읽기 순서 조절하여 성능 개선.
AI 코딩 에이전트를 사용한 개발과, 기존 서버 사양으로 이용하는 테스트, 국가의 계단적인 이행에 대해서 해설.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Add streaming HTML insertion methods by noamr · Pull Request #12758 · whatwg/html
[github.com/whatwg/html/pull/12758?overview&#x3D;true](https://github.com/whatwg/html/pull/12758?overview=true "Add streaming HTML insertion methods by noamr · Pull Request #12758 · whatwg/html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebAPI</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span></p>

HTML를 스트리밍으로 해석, DOM으로 계단적으로 도입하는 API를 HTML 사양으로.
`Element.streamHTML()`/`streamAppendHTML()`가 `WritableStream`를 반환, Stream으로 작성된 HTM 문자열을 HTML으로 도입.
위험한 요소나 속성을 제거하는 메서드와, 소거를 하지않는 `Unsafe`판을 준비.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## vercel-labs/tsc-ts: TypeScript written in TypeScript
[github.com/vercel-labs/tsc-ts](https://github.com/vercel-labs/tsc-ts "vercel-labs/tsc-ts: TypeScript written in TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">compiler</span> <span class="jser-tag">Tools</span></p>

TypeScript-Go（tsgo）를 TypeScript으로 이식하는 실험적인 컴파일러.
scriptc를 사용한 네이티브 코드를 컴파일하여, npm 패키지를 배포.
`tsc-ts -p tsconfig.json`으로 프로젝트 컴파일하고, `--api`으로 표준 입력을 사용하는 API 서버로 동작.


----

## obsidianmd/pele: Renders Mermaid diagrams faster than you&#039;d run from a volcano! 🌋
[github.com/obsidianmd/pele](https://github.com/obsidianmd/pele "obsidianmd/pele: Renders Mermaid diagrams faster than you&#039;d run from a volcano! 🌋")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">diagram</span> <span class="jser-tag">SVG</span></p>

Mermaid 다이어그램을 SVG으로 변환하는 라이브러리. 의존이 없이, CSS 변수에 의한 색이나 폰트 변경, 그림 종류마다 읽기나 지연 읽기에 대응.
`mount()`으로 브라우저 요소를 렌더링, 컨테이너 폭에 맞춘 레이아웃을 조절 가능.


----
