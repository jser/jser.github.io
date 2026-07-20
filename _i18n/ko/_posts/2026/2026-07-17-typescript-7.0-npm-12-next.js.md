---
title: "2026-07-17: TypeScript 7.0, npm 12, Next.js 보안 출시 방침"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-07-16T15:07:18.836Z
category: JSer
tags:
- TypeScript
- nodejs
- npm
- Next.js
- security

---

JSer.info #776 - TypeScript 7.0가 출시되었다.

- [Announcing TypeScript 7.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)

Go으로 이식된 네이티브 `tsc`가, npm의 `typescript` 패키지로 공개된다.
TypeScript 6.0에서는 비권장이 된 `target: es5`이나 `baseUrl` 같은 설정이 에러가 된다.
또한, 병렬처리 제어하는 `--checkers`/`--builders`/`--singleThreaded` 옵션, 재작성된 `--watch`, LSP를 사용한 데이터 대응도 포함된다.
한 편으로는, 프로그램 대상 API는 아직 공개되어 있지 않아, Vue 같은 TypeScript API 이용하는 도구는 TypeScript 7.0를 이용할 수 없는 경우도 있다.

---

npm 12가 출시되었다.

- [npm install-time security and GAT bypass2fa deprecation - GitHub Changelog](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/)
- [Release v12.0.0 · npm/cli](https://github.com/npm/cli/releases/tag/v12.0.0)

npm 12에는, 의존 패키지 라이프사이클 스크립트를 제어하는 `allowScripts`가 기본적으로 무효화된다.
또한, Git이나 리모트 URL에서 의존 패키지를 제어하는 `--allow-git`/`--allow-remote`도 기본적으로 `none`이 된다.
2026년 8월 초부터, 2FA를 회피하는 Granular Access Token은 계정이나 패키지 관리 조작에서 2FA를 생략할 수 없으며, 2027년 1월부터는 같은 토큰을 사용해 직접 publish도 할 수없게 할 예정.

---

Next.js가 보안 출시의 새로운 방침을 발표했다.

- [Next.js Security Release and Our Next Patch Release | Next.js](https://nextjs.org/blog/next-security-release-program)

앞으로는 월 1회 정도, 대상 버전과 취약성 최대심각도를 사전 고지하고, 보안 출시 공개할 방침이다.
시급성이 높거나 실제 악용되고 있는 취약성은, 이전처럼 임시 패치로 공개한다.
2026년 7월 20일 공개를 목표로하고, Next.js 16.2와 15.5 대상 패치가 될 예정이다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release pnpm 11.10 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v11.10.0](https://github.com/pnpm/pnpm/releases/tag/v11.10.0 "Release pnpm 11.10 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v11.10.0 출시.
`pnpm issues`/`pnpm prefix` 명령어 추가, `pnpm_config__auth` 환경 변수에서 `_auth` 설정 지원.
`pnpm self-update`의 pnpm v12 대응.
`pnpm up -r <pkg>`가 관계없는 패키지를 업데이트하는 문제, `pnpm pack-app` 경로 검증 수정.


----

## Chrome 150  |  Release notes  |  Chrome for Developers
[developer.chrome.com/release-notes/150](https://developer.chrome.com/release-notes/150 "Chrome 150  |  Release notes  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">css</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebGPU</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 150 출시.
CSS `AccentColor`/`AccentColorText`, `polygon()` 둥금 지정, `text-fit` 지원.
CSS `url()`의 `cross-origin()`/`integrity()`/`referrer-policy()` 수식자 지원.
DOM에는 `focusgroup` 속성, `popover=hint` 동작 변경.
`Element`/`Window` 스크롤 메서드가 Promise를 반환하도록 변경.
WebGPU의 `setImmediateData()`, PWA의 origin migration.
Origin Trial으로 `performance.getSpeculations()` 추가

- [New in Chrome 150  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/new-in-chrome-150?hl=en "New in Chrome 150  |  Blog  |  Chrome for Developers")

----

## Electron 43 | Electron
[www.electronjs.org/blog/electron-43-0](https://www.electronjs.org/blog/electron-43-0 "Electron 43 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 43 출시.
Chromium 150.0.7871.46, Node.js v24.17.0, V8 15.0으로 업데이트.
파일 다운로드할 때 파일 다이얼로그가, 기존에 Downloads 폴더를 열도록 변경.
`WebContents` 인스턴스의 `clone()`, macOS의 `Notification.remove()`/`Notification.removeAll()` 추가.
`globalShortcut.setSuspended()` 추가, startup snapshot이나 V8 bytecode cache에 의한 기동 성능 개선


----

## Announcing TypeScript 7.0 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-7-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/ "Announcing TypeScript 7.0 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 7.0 출시.
Go로 이식된 네이티브 `tsc`를 npm의 `typescript` 패키지로 공개.
TypeScript 6.0에서 비권장이 된 `target: es5`/`baseUrl`는 에러가 된다.
`--checkers`/`--builders`/`--singleThreaded`에 의한 병렬 처리 제어 추가.
`--watch`를 Parcel의 file watcher를 본래대로 돌림, LSP 대응 포함.
한 편으로 프로그램 대상 API는 공개되지 않아, Vue 같이 TypeScript API를 사용하는 도구로 아직 동작하지 경우도 있음.


----

## Better Auth is joining Vercel
[better-auth.com/blog/better-auth-joins-vercel](https://better-auth.com/blog/better-auth-joins-vercel "Better Auth is joining Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">vercel</span> <span class="jser-tag">news</span> <span class="jser-tag">nodejs</span></p>

Vercel가 Better Auth 매수 발표.
Better Auth는 TypeScript로 만든 인증 라이브러리, MIT 라이센스 개발 체제 유지할 예정.
Agent Auth Protocol 개발을 지속하고, Vercel Connect나 Eve으로 에이전트 ID 관리를 포함할 예정.

- [Vercel acquires Better Auth to accelerate open source auth - Vercel](https://vercel.com/blog/vercel-acquires-better-auth "Vercel acquires Better Auth to accelerate open source auth - Vercel")

----

## npm install-time security and GAT bypass2fa deprecation - GitHub Changelog
[github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/ "npm install-time security and GAT bypass2fa deprecation - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

npm v12 출시.
`allowScripts`가 기본적으로 무효화되어, `--allow-git`/`--allow-remote`은 기본적으로 `none`가 됨.
2FA를 회피하는 Granular Access Token은, 2026년 8월부터 계정이나 패키지 관리 조작에 2FA를 생략할 수 없음.
2027년 1월부터는 2FA를 회피하는 Granular Access Token를 사용해 직접 publish도 할 수없게 될 예정.
자동 공개에는 Trusted Publishing, 또한 사람에 의한 2FA 인증하는 Staged Publishing 으로 이행을 권장

- [Release v12.0.0 · npm/cli](https://github.com/npm/cli/releases/tag/v12.0.0 "Release v12.0.0 · npm/cli")

----

## Node.js — Node.js 26.5.0 (Current)
[nodejs.org/en/blog/release/v26.5.0](https://nodejs.org/en/blog/release/v26.5.0 "Node.js — Node.js 26.5.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v26.5.0 출시.
`Blob.prototype.textStream()`, `--experimental-import-text`, `ReadableStreamTee` 추가.
`perf_hooks.monitorEventLoopDelay`에 `samplePerIteration` 옵션 추가


----
<h1 class="site-genre">읽을거리</h1>

----

## Your Worker can now have its own cache in front of it
[blog.cloudflare.com/workers-cache/](https://blog.cloudflare.com/workers-cache/ "Your Worker can now have its own cache in front of it")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Cloudflare Workers Cache에 대하여.
Worker 사전 캐시를, `wrangler.jsonc`의 `cache.enabled`에서 유효화 가능.
`Cache-Control`/`Vary`에 대응, `ctx.cache.purge()`에서 태그나 경로에 의한 삭제가 가능.


----

## Next.js Security Release and Our Next Patch Release | Next.js
[nextjs.org/blog/next-security-release-program](https://nextjs.org/blog/next-security-release-program "Next.js Security Release and Our Next Patch Release | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Next.js 보안 출시 방침에 대하여.
앞으로는 월 1회 정도 사전 고지하고 출시를 공개, 긴급할 때는 기존처럼 임시 패치를 공개할 예정.
2026년 7월 20일 공개를 목표하고, Next.js 16.2와 15.5 대상 패치 예정됨.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Blume — fast, AI-ready, markdown-first docs
[useblume.dev/](https://useblume.dev/ "Blume — fast, AI-ready, markdown-first docs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">document</span> <span class="jser-tag">AI</span></p>

Markdown/MDX에서 문서 사이트를 생성하는 도구.
`blume init`/`blume dev`/`blume build` 같은 CLI 제공, Astro와 Vite를 사용해 정적 HTML를 생성.
검색, OpenAPI/AsyncAPI에서 생성된 API 레퍼런스, `llms.txt`, MCP 서버, Ask AI 기능을 갖음.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## samchon/ttsc: A \`typescript-go\` toolchain for compiler-powered plugins and type-safe execution + 500x faster lint integrated into compiler
[github.com/samchon/ttsc](https://github.com/samchon/ttsc "samchon/ttsc: A \`typescript-go\` toolchain for compiler-powered plugins and type-safe execution + 500x faster lint integrated into compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">lint</span></p>

`typescript-go`를 사용한 TypeScript 대상 툴체인.
빌드, 자료형 체크 실행, Lint, Format 도구를 제공.
Vite/Rollup/esbuild/webpack/Rspack/Next.js 대상 플러그인도 제공.


----

## theMackabu/ant: javascript for 🐜&#039;s, a tiny runtime with big ambitions
[github.com/theMackabu/ant](https://github.com/theMackabu/ant "theMackabu/ant: javascript for 🐜&#039;s, a tiny runtime with big ambitions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">C</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

C로 구현된 작은 JavaScript Runtime.
WinterTC Minimum Common API 호환 구현을 목표로 하고 있음.


----

## Wordgard
[wordgard.net/](https://wordgard.net/ "Wordgard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

리치 텍스트 에디터 대상 JavaScript 라이브러리.
ProseMirror/CodeMirror 제작자가 개발, 스키마 기반 문서 구조와, CodeMirror 스러운 확장 기능을 갖음.

- [Wordgard Release 0.1](https://marijnhaverbeke.nl/blog/wordgard-0.1.html "Wordgard Release 0.1")

----

## inokawa/virtua: A zero-config, fast and small (~3kB) virtual list (and grid) component for React, Vue, Solid and Svelte.
[github.com/inokawa/virtua/](https://github.com/inokawa/virtua/ "inokawa/virtua: A zero-config, fast and small (~3kB) virtual list (and grid) component for React, Vue, Solid and Svelte.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Solid</span> <span class="jser-tag">Svelte</span> <span class="jser-tag">library</span></p>

React/Vue/Solid/Svelte 대상 Virtual Scroll 컴포넌트 라이브러리.
`VList`/`Virtualizer`/`WindowVirtualizer`/`experimental_VGrid`를 제공, 가변 크기, 횡 스크롤, Window 스크롤, 그리드 게시에 대응.


----

## unjs/httpxy: 🔀 A Full-Featured HTTP and WebSocket Proxy for Node.js
[github.com/unjs/httpxy](https://github.com/unjs/httpxy "unjs/httpxy: 🔀 A Full-Featured HTTP and WebSocket Proxy for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">WebSocket</span> <span class="jser-tag">library</span></p>

Node.js 대상 HTTP/WebSocket 프록시 라이브러리.
Fetch API 호환 `proxyFetch`, WebSocket Upgrade 대상 `proxyUpgrade`, `createProxyServer` 제공.
Unix Socket, `changeOrigin`, `xfwd`, 리다이렉트나 Cookie 갈아 끼우기에도 대응.


----
