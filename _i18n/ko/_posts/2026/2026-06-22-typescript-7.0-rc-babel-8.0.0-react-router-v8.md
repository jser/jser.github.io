---
title: "2026-06-22: TypeScript 7.0 RC, Babel 8.0.0, React Router v8"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-06-22T13:14:54.573Z
category: JSer
tags:
- TypeScript
- babel
- React
- ECMAScript
- nodejs

---

JSer.info #774 - TypeScript 7.0 RC가 출시되었다.

- [Announcing TypeScript 7.0 RC - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)

Go언어로 이식된 컴파일이 `typescript@rc`으로 공개되어, 기존 `@typescript/typescript6`와 병용할 수 있도록 되었다.
`--checkers`/`--builders`/`--singleThreaded` 옵션이나, `--watch` 개선 추가가 있다.
또한, `strict`/`module`/`target` 기본값 변경 및 `target: es5`이나 `baseUrl` 옵션 삭제도 있다.

---

Babel 8.0.0가 출시되었다.

- [Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel](https://babeljs.io/blog/2026/06/16/8.0.0/)
- [Upgrade to Babel 8 (API) · Babel](https://babeljs.io/docs/v8-migration-api/)

ESM만 배포하도록 되어, Node.js 24 이후 버전이 필수가 되는 파괴적 변경도 포함된다.
`@babel/preset-env`는 기본적으로 ES5으로 컴파일하지 않게 되었으며, Browserslist 기본 설정（ES2023）를 타겟하도록 변경되었다.
`loose`/`spec` 옵션은 삭제되고, `assumptions`으로 이행이 권장된다.
`corejs`/`useBuiltIns` 옵션도 삭제되어, 대신 `babel-plugin-polyfill-corejs3` 플러그인 이용이 권장된다.
Babel 7은 2027년 6월까지 보안 지원이 계속된다.

---

React Router v8가 출시되었다.

- [React Router v8 | Remix](https://remix.run/blog/react-router-v8)

Node.js 22.22.0 이상 / React 19.2.7 이상 / Vite 7 이상이 최소 지원 버전이 되어, ESM만 배포하도록 변경되었다.
`future.v8_middleware`/`future.v8_viteEnvironmentApi`의 Future Flag가 기본적으로 유효화되었다.
`react-router-dom`, meta API의 `data` 인수, `@react-router/dev/vite/cloudflare` 삭제되었다.
React Router v6와 Remix v2는 EOL가 되어, 이후는 React Router v7에 보안 업데이트 갱신만 제공된다.

----
{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Dependabot version updates now support the Deno ecosystem - GitHub Changelog
[github.blog/changelog/2026-06-09-dependabot-version-updates-now-support-the-deno-ecosystem/](https://github.blog/changelog/2026-06-09-dependabot-version-updates-now-support-the-deno-ecosystem/ "Dependabot version updates now support the Deno ecosystem - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GitHub</span> <span class="jser-tag">deno</span> <span class="jser-tag">npm</span> <span class="jser-tag">package</span> <span class="jser-tag">Actions</span> <span class="jser-tag">news</span></p>

Dependabot의 version updates가 Deno 에코시스템에 대응함.


----

## Bytecode Alliance — WASI 0.3 Launched
[bytecodealliance.org/articles/WASI-0.3](https://bytecodealliance.org/articles/WASI-0.3 "Bytecode Alliance — WASI 0.3 Launched")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span></p>

WASI 0.3 출시.
WebAssembly Component Model 네이티브 기능으로 비동기처리가 내장되어, `stream<T>`/`future<T>`/`async`가 Canonical ABI에 추가됨.
WASI 0.2에는 각 컴퓨넌트 독자 이벤트 루프를 갖을 필요가 있었지만, 호스트가 공유 이벤트 루프를 관리하는 설계로 변경했다.
앞으로 `start-foo`/`finish-foo`/`subscribe` 패턴이 `async func`으로 변환되고, 스트리밍 에러 핸들링도 독립된 `future`로 다루도록 되었다.


----

## Biome v2.5—500 Lint Rules, Plugin Code Fix, and Cross-File Linting | Biome
[biomejs.dev/blog/biome-v2-5/](https://biomejs.dev/blog/biome-v2-5/ "Biome v2.5—500 Lint Rules, Plugin Code Fix, and Cross-File Linting | Biome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">biome</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">css</span></p>

Biome v2.5 출시.
CSS 클래스를 파일 횡단으로 해석하는 Lint 규칙 `noUndeclaredClasses`/`noUnusedClasses` 추가.
GritQL 플러그인이 파일 경로째로 적용 및`=>`로 인한 코드픽스를 지원.
Formatter에 `delimiterSpacing` 옵션 추가, `lint`/`format`/`check`에서 `--watch` 지원.
Language Server의 go-to-definition 대응, AI Agent 대상 `concise` 레포트 추가.


----

## Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel
[babeljs.io/blog/2026/06/16/8.0.0/](https://babeljs.io/blog/2026/06/16/8.0.0/ "Releasing Babel 8 today: ESM-only, drop ES5 default, and a smooth migration path · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">polyfill</span></p>

Babel 8.0.0 출시.
ESM만 배포하도록 되어, Node.js 24 이후 버전이 필수가 되는 파괴적 변경도 포함.
`@babel/preset-env`가 기본적으로 ES5으로 컴파일하지 않게 되었고, Browserslist 기본적 설정이（ES2023）를 타겟하도록 변경.
`loose`/`spec` 옵션을 삭제, `assumptions`으로 이행을 권장.
`corejs`/`useBuiltIns` 옵션 삭제, `babel-plugin-polyfill-corejs3` 플러그인 이용을 권장.
모든 패키지에서 TypeScript 자료형 정의를 추가. 많은 AST 변경을 포함.
Babel 7은 2027년 6월까지 보안 지원를 지속.

- [Upgrade to Babel 8 (API) · Babel](https://babeljs.io/docs/v8-migration-api/ "Upgrade to Babel 8 (API) · Babel")

----

## pnpm 11.7 | pnpm
[pnpm.io/blog/releases/11.7](https://pnpm.io/blog/releases/11.7 "pnpm 11.7 | pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 11.7 출시.
읽기 전용 파일 시스템 상에 스토어에 대응하는 `frozenStore` 설정, 동일 레지스트리 URL 하에 스코프별 인증 토큰 지정에 대응.
의존 관계 해결을 Rust 구현 Pacquet 사용


----

## Release v1.61.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.61.0](https://github.com/microsoft/playwright/releases/tag/v1.61.0 "Release v1.61.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.61.0 출시.
`browserContext.credentials`에서 WebAuthn의 passkey 다루도록.
`page.localStorage`/`page.sessionStorage`으로 Web Storage를 읽는 API 추가.
`apiResponse.securityDetails()`/`apiResponse.serverAddr()`, `artifactsDir` 옵션, `-G` 옵션 추가.


----

## React Router v8 | Remix
[remix.run/blog/react-router-v8](https://remix.run/blog/react-router-v8 "React Router v8 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React Router v8 출시.
Node.js 22.22.0+/React 19.2.7+/Vite 7+가 최소 지원 버전이 되어, ESM으로만 배포하도록 변경.
`future.v8_middleware`/`future.v8_viteEnvironmentApi` Future Flag 기본값으로.
`react-router-dom`, meta API의 `data` 인수, `@react-router/dev/vite/cloudflare`를 삭제.
React Router v6와 Remix v2는 EOL가 되어, 앞으로는 React Router v7으로 보안 갱신만 제공.


----

## News from WWDC26: WebKit in Safari 27 beta | WebKit
[webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/ "News from WWDC26: WebKit in Safari 27 beta | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">css</span> <span class="jser-tag">JavaScript</span></p>

Safari 27 beta 출시.
CSS의 `appearance: base-select`로 `<select>` 커스터마이즈, Scroll Anchoring, `position-anchor: normal` 추가.
JavaScript는 Top-Level Await 문제를 수정, WebAssembly JSPI를 지원.
Web API는 Service Worker Static Routing API, `ReadableStream.from()`, Stream의 `postMessage()` 전송 지원.


----

## Announcing TypeScript 7.0 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/ "Announcing TypeScript 7.0 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">go</span></p>

TypeScript 7.0 RC 출시.
Go로 이식된 컴파일러 `typescript@rc` 공개, `@typescript/typescript6`와 병용에 대응.
`--checkers`/`--builders`/`--singleThreaded`, `--watch` 개선을 추가.
`strict`/`module`/`target` 기본값으로 변경, `target: es5`/`baseUrl` 삭제 포함


----
<h1 class="site-genre">읽을거리</h1>

----

## Upcoming breaking changes for npm v12 - GitHub Changelog
[github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/ "Upcoming breaking changes for npm v12 - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">CLI</span> <span class="jser-tag">article</span></p>

npm v12 예정된 파괴적 변경 해설. 2026년 7월 출시 예정 npm v12에는, 공급망 공격 대책으로, 라이프사이클 스크립트 실행이 변경됨.
preinstall/install/postinstall 스크립트가 기본적으로 실행되지 않으며, `npm approve-scripts`로 인증된 패키지만이 실행함.
`--allow-git`/`--allow-remote` 기본값이 `none`이 되어, Git 의존이나 원격 URL에서 의존 해결이 명시적으로 허용되지 않게 됨.


----

## Why pnpm no longer expands environment variables in a repository&#039;s .npmrc | pnpm
[pnpm.io/blog/2026/06/11/env-variables-in-repository-npmrc](https://pnpm.io/blog/2026/06/11/env-variables-in-repository-npmrc "Why pnpm no longer expands environment variables in a repository&#039;s .npmrc | pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">security</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

악의적인 레포지토리에서 `.npmrc`를 사용해 환경 변수를 훔치는 문제의 대책으로, pnpm가 레포지토리 관리 `.npmrc`으로 환경 변수 전개하지 않도록한 경위 해설.
v10.34.2/v11.5.3 이후, 레포지토리 내의 `.npmrc`나 `pnpm-workspace.yaml` 인증 정보 레포지토리 URL에 포함하는 `${...}`는 전개되지 않도록 됨.
유저 레벨 `~/.npmrc`이나  `PNPM_CONFIG_NPMRC_AUTH_FILE`으로 지정되는 `.npmrc`에는 계속해서 전개 가능.

- [CAND-PNPM-122: Repository config can expand victim environment secrets into registry requests before scripts run · Advisory · pnpm/pnpm](https://github.com/pnpm/pnpm/security/advisories/GHSA-3qhv-2rgh-x77r "CAND-PNPM-122: Repository config can expand victim environment secrets into registry requests before scripts run · Advisory · pnpm/pnpm")

----

## Introducing the MDN MCP server
[developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/ "Introducing the MDN MCP server")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">MCP</span> <span class="jser-tag">document</span> <span class="jser-tag">browser</span> <span class="jser-tag">AI</span> <span class="jser-tag">article</span></p>

MDN MCP server에 대하여
MCP 경유로 MDN 검색, 문서, 브라우저 호환성 데이터를 LLM이나 에디터에서 참조 가능.
실험적인 서버로, 이용할 떄 쿼리 데이터를 보존하는 것에 대해 해설됨.


----
<h1 class="site-genre">웹사아트, 서비스, 문서</h1>

----

## Introducing eve - Vercel
[vercel.com/blog/introducing-eve](https://vercel.com/blog/introducing-eve "Introducing eve - Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">AI</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Vercel에 의한 AI 에이전트 프레임워크 Eve에 대하여.
`instructions.md`/`agent.ts`/`tools/` 디렉토리 구성으로 에이전트를 정의하는 프레임워크.
Durable execution, Sandbox, Human-in-the-loop approvals, Subagents, Evals 다룸

- [vercel/eve: The Framework for Building Agents](https://github.com/vercel/eve "vercel/eve: The Framework for Building Agents")

----

## Rust Roadmap · Issue #11633 · pnpm/pnpm
[github.com/pnpm/pnpm/issues/11633](https://github.com/pnpm/pnpm/issues/11633 "Rust Roadmap · Issue #11633 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">Rust</span> <span class="jser-tag">issue</span></p>

pnpm의 Rust 구현 Pacquet 로드맵 Issue.
resolve를 필요로 하지않는 `pacquet install --frozen-lockfile`에서 대응, resolveの 대응 진행.
또한 `pnpm`에는 `install-backend=pacquet` 설정 통합해 갈 예정.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## nubjs/nub: The all-in-one Node.js toolkit
[github.com/nubjs/nub](https://github.com/nubjs/nub "nubjs/nub: The all-in-one Node.js toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span></p>

Node.js 대상 Rust제 툴킷.
TypeScript 파일이나 `package.json` 스크립트 실행, `nub install`로 의존관계 설치나 패키지 관리, `nub node`로 Node.js 버전 관리 가능.
Runtime으로 Polyfill 포함하는 Node.js를 이용, 내부적으로 Rust로 작성된 패키지 매니저 aube와 OXC를 이용.

- [Nub — an all-in-one toolkit for Node.js](https://nubjs.com/ "Nub — an all-in-one toolkit for Node.js")

----
