---
title: "2025-02-24: Create React App 비권장으로, Deno 2.2, Bun 1.2.3, ESLint의 CSS 지원"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-02-24T13:09:04.703Z
category: JSer
tags:
- vite
- browser
- WebPlatformAPI
- TypeScript
- pnpm

---

JSer.info #726 - Create React App가 비권장이 되었습니다.

- [Sunsetting Create React App – React](https://react.dev/blog/2025/02/14/sunsetting-create-react-app)

`create-react-app`는 비권장이 되어, React 사용한 프레임워크나 Vite/Parcel/Rsbuild 빌드 도구로의 이행이 권장됩니다.

---

Deno 2.2가 출시되었습니다.

- [Deno 2.2: OpenTelemetry, Lint Plugins, node:sqlite](https://deno.com/blog/v2.2)

lint 빌트인 규칙 추가, JavaScript으로 작성가능한 Lint Plugin API 추가, `deno task`가 wildcard(`*`) 지정에 대응합니다.
또한, `deno outdated`에 interactive mode 추가, `deno compile` 개선도 포함되고 있습니다.
unstable한 기능으로 OpenTelemetry 지원, `WebTransport` API 지원도 추가되었습니다.

---

Bun v1.2.3가 출시되었습니다.

- [Bun v1.2.3 | Bun Blog](https://bun.sh/blog/bun-v1.2.3)

`bun ./index.html`로 개발 서버 세울 수 있도록, `Bun.serve`의 `static` 옵션을 `routes` 옵션으로 변경했습니다.
`bun init`에서 React 프로젝트 작성할 수 있도록, `bun install --analyze`에 부족한 의존을 `pacakge.json`에 추가할 수 있도록 했습니다.
또한, Wasm의 interpreter로 LLInt가 아니라 IPINT를 사용하는 것을 기본으로 하고, `BUN_JSC_useWasmIPInt=0`으로 돌릴 수 있도록 했습니다.

---

ESLint가 CSS의 Lint 지원합니다.

- [ESLint now officially supports linting of CSS - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2025/02/eslint-css-support/)

CSSTree 사용한 CSS 파서와 몇몇 Lint 규칙이 구현되었습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 5.8 RC - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-8-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8-rc/ "Announcing TypeScript 5.8 RC - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.8 RC 출시.
conditional return type 개선, `require(esm)` 대응, `--module node18` 추가. Node.js의 `--experimental-strip-types`와 같이 설정하는 `--erasableSyntaxOnly`플래그 추가, `--libReplacement`플래그 추가


----

## Release pnpm 10.4 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.4.0](https://github.com/pnpm/pnpm/releases/tag/v10.4.0 "Release pnpm 10.4 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.4.0 출시.
`pnpm approve-builds --global` 추가, `pnpm --allow-build=<pkg> add` 추가, `pnpm approve-builds` 버그 수정


----

## Sunsetting Create React App – React
[react.dev/blog/2025/02/14/sunsetting-create-react-app](https://react.dev/blog/2025/02/14/sunsetting-create-react-app "Sunsetting Create React App – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">news</span></p>

`create-react-app` 비권장, React 사용하는 프레임워크로 이행 하는 문서 공개.


----

## vite/packages/vite/CHANGELOG.md at main · vitejs/vite
[github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#610-2025-02-05](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#610-2025-02-05 "vite/packages/vite/CHANGELOG.md at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 6.1.0 출시.


----

## Release v3.0.5 · vitest-dev/vitest
[github.com/vitest-dev/vitest/releases/tag/v3.0.5](https://github.com/vitest-dev/vitest/releases/tag/v3.0.5 "Release v3.0.5 · vitest-dev/vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

vitest v3.0.5 출시.
Vitest UI의 API 서버는 리퀘스트 Origin 체크하지 않았기에, 낚시 사이트로 접근할 때 호스트 머신에서 임의 코드 실행이 가능했던 RCE 취약성 수정 포함.


----

## Release v2.20.0 · codesandbox/sandpack
[github.com/codesandbox/sandpack/releases/tag/v2.20.0](https://github.com/codesandbox/sandpack/releases/tag/v2.20.0 "Release v2.20.0 · codesandbox/sandpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">editor</span> <span class="jser-tag">ReleaseNote</span></p>

sandpack 2.20.0 출시.
React 19 대응


----

## Deno 2.2: OpenTelemetry, Lint Plugins, node:sqlite
[deno.com/blog/v2.2](https://deno.com/blog/v2.2 "Deno 2.2: OpenTelemetry, Lint Plugins, node:sqlite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.2 출시.
lint 빌트인 설치 추가, JavaScript으로 작성하는 Lint Plugin API 추가, `deno task`가 wildcard(`*`) 지정에 대응.
`deno outdated`에 interactive mode 추가, `deno compile` 개선.
unstable한 기능으로 OpenTelemetry 지원, `WebTransport` API 지원


----

## Bun v1.2.3 | Bun Blog
[bun.sh/blog/bun-v1.2.3](https://bun.sh/blog/bun-v1.2.3 "Bun v1.2.3 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.3 출시.
`bun ./index.html`으로 개발 서버 세울 수 있음, `Bun.serve`의 `static` 옵션을 `routes` 옵션으로 변경.
`bun init`으로 React 프로젝트 작성하도록, `bun install --analyze`으로 부족한 의존을 `pacakge.json`에 추가.
Wasm의 interpreter로 LLInt가 아니라 IPINT 사용하는 것을 기본으로 하고, `BUN_JSC_useWasmIPInt=0`으로 본래대로 돌릴 수 있도록


----

## Release v2.6.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v2.6.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.6.0 "Release v2.6.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v2.6.0 출시.
Infinite Query 지원


----

## ECMAScript proposal updates @ 2025-02 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2025/02/24/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2025/02/24/ecmascript-proposal-update "ECMAScript proposal updates @ 2025-02 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2025년 2월 TC39 Meeting에서 ECMAScript Proposal 상태 변경 정리.
`RegExp.escape`과 Float16가 Stage 4가 되어, ECMAScript 2025에 도입 결정


----
<h1 class="site-genre">읽을거리</h1>

----

## ESLint now officially supports linting of CSS - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2025/02/eslint-css-support/](https://eslint.org/blog/2025/02/eslint-css-support/ "ESLint now officially supports linting of CSS - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">css</span> <span class="jser-tag">article</span></p>

ESLint가 CSS의 Lint 정식 지원.
`@eslint/css` 플러그인으로 CSS의 Lint 대응, `tolerant` 옵션으로 구문 에러 케이스에도 대응, `customSyntax`으로 독자 `@at-rule`에도 대응


----

## The Popover API is now Baseline Newly available  |  Blog  |  web.dev
[web.dev/blog/popover-baseline?hl&#x3D;en](https://web.dev/blog/popover-baseline?hl=en "The Popover API is now Baseline Newly available  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

Popover API가 Baseline가 되어 많은 브라우저에서 이용 가능.


----

## Interop 2025 스타트 | 프론트엔드Blog | 미츠에링크스
[www.mitsue.co.jp/knowledge/blog/frontend/202502/17\_0829.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202502/17_0829.html "Interop 2025 스타트 | 프론트엔드Blog | 미츠에링크스")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span> <span class="jser-tag">WebPlatformAPI</span></p>

브라우저 상호 운용성 향상을 위한 Interop 2025 발표.

- [Announcing Interop 2025 | WebKit](https://webkit.org/blog/16458/announcing-interop-2025/ "Announcing Interop 2025 | WebKit")
- [Interop 2025 Launch - Bocoup](https://www.bocoup.com/blog/interop-2025 "Interop 2025 Launch - Bocoup")
- [Interop 2025: another year of web platform improvements  |  Blog  |  web.dev](https://web.dev/blog/interop-2025 "Interop 2025: another year of web platform improvements  |  Blog  |  web.dev")
- [Interop 2025 | Igalia](https://www.igalia.com/2025/02/13/Interop-2025.html "Interop 2025 | Igalia")
- [Microsoft Edge and Interop 2025 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2025/02/13/microsoft-edge-and-interop-2025/ "Microsoft Edge and Interop 2025 - Microsoft Edge Blog")
- [Launching Interop 2025 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2025/02/interop-2025/ "Launching Interop 2025 - Mozilla Hacks - the Web developer blog")

----

## Web 기술 호환성을 파악하기 위한 Baseline와 Web Platform Status Dashboard
[zenn.dev/sakito/articles/26cba8397c4dbe](https://zenn.dev/sakito/articles/26cba8397c4dbe "Web 기술 호환성을 파악하기 위한 Baseline와 Web Platform Status Dashboard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

Baseline와 Web Platform Status Dashboard에 대하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## The Typescript AI framework - Mastra
[mastra.ai/](https://mastra.ai/ "The Typescript AI framework - Mastra")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">LanguageModel</span> <span class="jser-tag">API</span> <span class="jser-tag">library</span></p>

OpenAI/Anthropic/Google Gemini의 LLM Provider API를 사용해 Agent나 도구를 작성하는 AI 프레임워크.
Gatsby 제작자들이 작성


----

## le0pard/re2js: RE2JS is the JavaScript port of RE2, a regular expression engine that provides linear time matching
[github.com/le0pard/re2js](https://github.com/le0pard/re2js "le0pard/re2js: RE2JS is the JavaScript port of RE2, a regular expression engine that provides linear time matching")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">RegExp</span> <span class="jser-tag">library</span></p>

정규표현 엔진 RE2의 JavaScript Port


----
