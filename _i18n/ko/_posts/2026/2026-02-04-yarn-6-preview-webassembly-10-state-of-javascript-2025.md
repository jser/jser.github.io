---
title: "2026-02-04: Yarn 6 Preview, WebAssembly 10년, State of JavaScript 2025 결과 공개"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-02-04T13:19:34.984Z
category: JSer
tags:
- Tools
- Bun
- security
- playwright
- WebAssembly

---

JSer.info #763 - Yarn 6 프리뷰가 공개되었다.

- [Yarn 6 Preview | Yarn](https://yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/)

Yarn 6는 Rust로 재작성되어, 성능 개선이 있다.
Corepack 대신에 Yarn 버전 관리를 하는 `yarn switch` 명령어 추가, package.json 변경할 때 자동으로 설치하는 Lazy Installs가 기본 유효화된다.
마이그레이션 스텝으로, JS 구현 Yarn 5가 수 개월 안에 출시 예정이며, Rust 구현한 Yarn 6는 2026년 Q3 이후에 출시 예정이다.

---

WebAssembly 탄생 10년을 돌아 보는 글이 공개되었다.

- [Bytecode Alliance — 10 Years of Wasm: A Retrospective](https://bytecodealliance.org/articles/ten-years-of-webassembly-a-retrospective)

2013년 asm.js으로 시작해, Mozilla의 Luke Wagner와 Google의 Ben Titzer 협력으로 WebAssembly가 탄생한 경위를 소개한다. 2015년에 주요 브라우저가 동시에 대응을 발표, 2017년에는 모든 브라우저 대응이 완료되었다. 그 이후, WASI나 Component Model의 개발로 인해서 브라우저 외에서 이용할 수 있도록 넓어졌다, WASI을 POSIX 카피로 하지 않은 점 등에 대해 다뤄진다.

---

State of JavaScript 2025 앙케이트 결과가 공개되었다.

- [State of JavaScript 2025](https://2025.stateofjs.com/en-US)

JavaScript 언어기능, 프레임워크, 라이브러리, 도구, 테스트, AI 활용 등에 대해 앙케이트 결과 정리되어있다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v8.0.0 · FullHuman/purgecss
[github.com/FullHuman/purgecss/releases/tag/v8.0.0](https://github.com/FullHuman/purgecss/releases/tag/v8.0.0 "Release v8.0.0 · FullHuman/purgecss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

PurgeCSS v8.0.0 출시.
PostCSS 플러그인 임포트 방법이 default import으로 변경.
CLI에 `--preserve-paths` 옵션 추가, CSS 변수에 참조된 애니메이션 유지 개선


----

## Bun v1.3.7 | Bun Blog
[bun.com/blog/bun-v1.3.7](https://bun.com/blog/bun-v1.3.7 "Bun v1.3.7 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.3.7 출시.
JSON5 파서 `Bun.JSON5`, JSON Lines 다루는 `Bun.JSONL`, ANSI 텍스트 랩을 하는 `Bun.wrapAnsi()` 추가.
Markdown 형식에서 Heap이나 CPU 프로파일을 출력하는 `--heap-prof-md`/`--cpu-prof-md` 플래그 추가.
`Buffer.from(array)`/async-await/`array.flat()` 성능 개선, HTTP/2 호환성 수정.


----

## Release v4.11.7 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.11.7](https://github.com/honojs/hono/releases/tag/v4.11.7 "Release v4.11.7 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Hono v4.11.7 출시.
다음 보안 문제를 수정하는 출시

- IP 제한 Middleware의 IPv4 주소 검증 바이패스
- Cache Middleware에서 private나 no-store한 response가 캐시되는 문제
- Serve Static 미들웨어 (Cloudflare Workers adapter)에서의 내부 에셋 접근 문제
- hono/jsx의 ErrorBoundary에서의 XSS


----

## Release v0.0.58 · microsoft/playwright-mcp
[github.com/microsoft/playwright-mcp/releases/tag/v0.0.58](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.58 "Release v0.0.58 · microsoft/playwright-mcp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">MCP</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

playwright-mcp v0.0.58 출시.
`playwright-cli` 명령어가 추가되어, 명령어로 Playwright를 조작 가능.


----

## Node.js — Node.js 25.5.0 (Current)
[nodejs.org/en/blog/release/v25.5.0](https://nodejs.org/en/blog/release/v25.5.0 "Node.js — Node.js 25.5.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node v25.5.0 출시.
Single Executable Applications(SEA) 작성을 간략화하는 `--build-sea` 플래그 추가.
`fs.watch()`에 `ignore` 옵션을 추가, SQLite의 defensive mode를 기본적으로 유효화.
`node:test`에 `expectedFailure` 옵션을 추가


----

## Yarn 6 Preview | Yarn
[yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/](https://yarn6.netlify.app/blog/2026-01-28-yarn-6-preview/ "Yarn 6 Preview | Yarn")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">Rust</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

Yarn 6 프리뷰 공개.
Yarn 6은 Rust으로 재작성되어, 성능 개선됨.
Corepack 대신에 Yarn 버전 관리하는 `yarn switch` 추가, package.json의 변경할 때 자동으로 설치하는 Lazy Installs가 기본.
JS 구조인 Yarn 5은 마이그레이션 스텝으로 수 개월 내에 출시 예정, Rust 구현 Yarn 6은 2026년 Q3 이후 예정.


----

## Lodash Rolls Out Major Security Overhaul | OpenJS Foundation
[openjsf.org/blog/lodash-security-overhaul](https://openjsf.org/blog/lodash-security-overhaul "Lodash Rolls Out Major Security Overhaul | OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">lodash</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Lodash 4.17.23 출시.
`_.unset`와 `_.omit` 함수 Prototype Pollution 취약성 수정.
프로젝트의 거버넌스 시큐리티 체제를 쇄신, Technical Steering Committee 설립.
CodeQL로 정적 해석, Renovate로 의존 관계 자동 갱신, OpenSSF Scorecard 감시 도입.
CI 재구축, Bun 지원, Playwright 사용한 브라우저 테스트 재도입도 있다.


----

## Release v1.58.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.58.0](https://github.com/microsoft/playwright/releases/tag/v1.58.0 "Release v1.58.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.58.0 출시.
`_react`/`_vue` 셀렉터, `:light` 셀렉터 엔진, `devtools` 옵션 삭제.
macOS 13에서 WebKit 지원 종료.
HTML 레포트 Speedboard 탭에 Timeline 추가, UI Mode와 Trace Viewer에 시스템 테마 옵션을 추가 및 검색 기능 추가


----

## Bun v1.3.8 | Bun Blog
[bun.com/blog/bun-v1.3.8](https://bun.com/blog/bun-v1.3.8 "Bun v1.3.8 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.3.8 출시.
Zig 작성된 내장 CommonMark 준거한 Markdown 파서 `Bun.markdown` 추가.
`bun build --metafile-md`으로 LLM 프렌들리한 모듈 그래프의 메타데이터 출력 가능.
Windows에서 `npm install -g bun` 리그레션 수정.


----

## Release Version 28.0.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/28.0.0](https://github.com/jsdom/jsdom/releases/tag/28.0.0 "Release Version 28.0.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 28.0.0 출시.
리소스 로딩 커스터마이즈 API 쇄신, `<iframe>`/`<frame>` 요소에서 MIME type sniffing 지원.
`XMLHttpRequest`이나 `WebSocket` 리퀘스트가 새로운 리소스 로등의 커스터마이즈해서 인터셉트 가능.
리다이렉트할 때 `document referrer` 수정, `XMLHttpRequest` 버그 수정


----
<h1 class="site-genre">읽을거리</h1>

----

## Bytecode Alliance — 10 Years of Wasm: A Retrospective
[bytecodealliance.org/articles/ten-years-of-webassembly-a-retrospective](https://bytecodealliance.org/articles/ten-years-of-webassembly-a-retrospective "Bytecode Alliance — 10 Years of Wasm: A Retrospective")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">history</span> <span class="jser-tag">article</span></p>

WebAssembly 탄생 10년 돌아보는 글.
2013년 asm.js으로 시작해, Mozilla의 Luke Wagner와 Google의 Ben Titzer 협력에 의해 WebAssembly가 탄생한 경위 소개.
2015년에 주요 브라우저가 동시에 대응 발표, 2017년에는 모든 브라우저 대응 완료.
그 이후, WASI나 Component Model의 개발로 인해 브라우저 외로도 이용이 넓혀짐.
WASI를 POSIX 카피하지 않은 점에 대해서도 다룸


----

## Custom DuckDB Wasm builds for Cloudflare Workers - tobilg.com
[tobilg.com/posts/custom-duckdb-wasm-builds-for-cloudflare-workers/](https://tobilg.com/posts/custom-duckdb-wasm-builds-for-cloudflare-workers/ "Custom DuckDB Wasm builds for Cloudflare Workers - tobilg.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">duckdb</span> <span class="jser-tag">article</span></p>

Cloudflare Workers 상에서 DuckDB WebAssembly를 동작하기 위한 커스텀 빌드.
DuckDB의 기존 Wasm 빌드는 브라우저 대상 설계며, Workers 비동기환경에서 동작하지 않기에, Emscripten의 Asyncify를 사용해 해결책을 소개함.
@ducklings/workers 패키지를 사용해서, Parquet/JSON/httpfs 확장 기능을 포함하는 DuckDB Wasm를 엣지에서 실행 가능.

- [tobilg/ducklings: A minimal DuckDB Wasm build for browsers and serverless environments like Cloudflare Workers](https://github.com/tobilg/ducklings "tobilg/ducklings: A minimal DuckDB Wasm build for browsers and serverless environments like Cloudflare Workers")

----

## State of JavaScript 2025
[2025.stateofjs.com/en-US](https://2025.stateofjs.com/en-US "State of JavaScript 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span></p>

State of JavaScript 2025의 앙케이트 결과가 공개됨.
JavaScript 언어 기능, 프레임워크, 라이브러리, 도구, 테스트, AI 활용 등에 대한 앙케이트 결과 정리.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## LibPDF-js/core: A modern PDF library for TypeScript. Parse, modify, and generate PDFs with a clean, intuitive API.
[github.com/libpdf-js/core](https://github.com/libpdf-js/core "LibPDF-js/core: A modern PDF library for TypeScript. Parse, modify, and generate PDFs with a clean, intuitive API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PDF</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

ブラウザ나 Node.js 등에서 동작하는 PDF 편집, 작성 라이브러리.
PDF 해석, 수정, 생성 지원하며, RC4/AES 암호화, 디지털 서명, 폼 입력, 페이지 머지/분리, 텍스트 추출 등 대응.


----
