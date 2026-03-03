---
title: "2026-02-26: Electrobun v1, Deno 2.7, Oxfmt Beta"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-02-26T14:48:54.395Z
category: JSer
tags:
- security
- Tools
- nodejs
- React
- AI

---

JSer.info #765 - Electrobun v1가 출시되었다.

- [Electrobun v1 - Blackboard Blog](https://blackboard.sh/blog/electrobun-v1/)

TypeScript으로 크로스플랫폼 데스크탑 애플리케이션을 만들 수 있는 프레임워크, 런타임은 Bun, Zig나 C/C++로 구현되었다.
윈도우 관리나 메뉴, 글로벌 단축키 같은 네이티브 기능 지원, 차분 배치에 의한 자동 업데이트 기능과 프로세스 분리된 webview 구조를 가지고 있다.


---

Deno v2.7가 출시되었다.

- [Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno](https://deno.com/blog/v2.7)

Temporal API가 stable으로 변경, Windows ARM(aarch64) 지원이 추가되었다. `package.json`의 `overrides` 필드 지원, `CompressionStream`/`DecompressionStream`에서 Brotli 지원, Web Crypto API에서 SHA3 알고리즘 지원이 포함.


---

Oxc의 JavaScript Formatter Oxfmt β가 출시되었다.

- [Oxfmt Beta | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2026-02-24-oxfmt-beta)

Prettier의 JavaScript/TypeScript 호환 테스트를 100% 패스. Tailwind CSS 클래스 정렬, import 정렬, `package.json` 필드 정렬이 포함된 지원이다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Electrobun v1 - Blackboard Blog
[blackboard.sh/blog/electrobun-v1/](https://blackboard.sh/blog/electrobun-v1/ "Electrobun v1 - Blackboard Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Bun</span> <span class="jser-tag">Zig</span> <span class="jser-tag">Electron</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript로 크로스플랫폼 데스크탑 애플리케이션을 만들 수 있는 프레임워크.
런타임 Bun, Zig와 C/C++로 구현.
윈도우 관리/메뉴/글로벌 단축키/클립보드/다이얼로그 같은 네이티브 기능 지원.
차분 배치로 자동 업데이트 기능, 프로레스 분리된 webview를 `<electrobun-webview>` 요소로 다루는 구조를 갖고 있다.
macOS/Windows/Ubuntu 대응.

- [blackboardsh/electrobun: Build ultra fast, tiny, and cross-platform desktop apps with Typescript.](https://github.com/blackboardsh/electrobun "blackboardsh/electrobun: Build ultra fast, tiny, and cross-platform desktop apps with Typescript.")
- [Electrobun Documentation - Build ultra fast, tiny, cross-platform desktop apps](https://blackboard.sh/electrobun/docs/ "Electrobun Documentation - Build ultra fast, tiny, cross-platform desktop apps")

----

## Release v4.12.0 · honojs/hono
[github.com/honojs/hono/releases/tag/v4.12.0](https://github.com/honojs/hono/releases/tag/v4.12.0 "Release v4.12.0 · honojs/hono")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Hono</span> <span class="jser-tag">ReleaseNote</span></p>

Hono v4.12.0 출시.
Hono Client에 `$path()` 메서드 추가, SSG 대상 redirect plugin 추가, Basic Auth의 `onAuthSuccess` 콜백 추가.
`getConnInfo`가 AWS Lambda/Cloudflare Pages/Netlify 대응.
TrieRouter 성능 개선, `c.json()`의 Fast Path 추가


----

## Oxfmt Beta | The JavaScript Oxidation Compiler
[oxc.rs/blog/2026-02-24-oxfmt-beta](https://oxc.rs/blog/2026-02-24-oxfmt-beta "Oxfmt Beta | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Oxc의 JavaScript Formatter Oxfmtβ 출시.
Prettier의 JavaScript/TypeScript 호환 테스트 100% 패스.
Tailwind CSS 클래스 정렬, import 정렬, `package.json` 필드 정렬 지원

- [Oxfmt | The JavaScript Oxidation Compiler](https://oxc.rs/docs/guide/usage/formatter "Oxfmt | The JavaScript Oxidation Compiler")

----

## Node.js — Node.js 25.7.0 (Current)
[nodejs.org/en/blog/release/v25.7.0](https://nodejs.org/en/blog/release/v25.7.0 "Node.js — Node.js 25.7.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node v25.7.0 출시.
`node:sqlite` 모듈이 Release Candidate(RC)으로 승격.
Single Executable Applications(SEA)로 ESM 엔트리포인트 지원, 
HTTP/2でHTTP/1으로 폴백 설정 `http1Options` 추가.
`Duplex.toWeb()`의 type 옵션을 `readableType`으로 재명명, `node:test`으로 SIGINT할 때 중단된 테스트 게시.
`fs.stat`으로 `throwIfNoEntry` 옵션 추가, `zlib`으로 Brotli 압축 딕셔너리 지원.


----

## Node.js — Node.js 24.14.0 (LTS)
[nodejs.org/en/blog/release/v24.14.0](https://nodejs.org/en/blog/release/v24.14.0 "Node.js — Node.js 24.14.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node v24.14.0 출시.
`async_hooks`의 `createHook()`에 `trackPromises` 옵션 추가, `fs.watch()`에 `ignore` 옵션 추가.
`http.setGlobalProxyFromEnv()` 추가, Subpath Imports로 `#/`부터 시작하는 경로 지원.
SQLite의 defensive mode를 기본적 유효화, Embedder API으로 ESM 초기 지원 추가.
`stream/consumers`에 `bytes()` 메서드 추가, `node:test`의 `run()`으로 `env` 옵션 추가과 `it.expectFailure` 지원.


----

## Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno
[deno.com/blog/v2.7](https://deno.com/blog/v2.7 "Deno 2.7: Temporal API, Windows ARM, and npm overrides | Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.7 출시.
Temporal API이 stable으로 변경, Windows ARM(aarch64) 지원.
`package.json`의 `overrides` 필드 지원, `deno install --compile` 추가.
`CompressionStream`/`DecompressionStream`가 Brotli 지원, Web Crypto API에서 SHA3 알고리즘 지원.
`deno task`에서 globstar(`**`)와 `pipefail` 지원, `deno compile --self-extracting` 옵션 추가.
Web Worker의 DevTools 디버그 대응, OpenTelemetry에서 Deno Cron 자동 계측 대응.
Node.js 호환성 개선으로 `node:worker_threads`/`node:child_process`/`node:zlib`(Zstd) 수정, V8 14.5으로 업데이트.


----


## npm bulk trusted publishing config and script security now generally available - GitHub Changelog
[github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/](https://github.blog/changelog/2026-02-18-npm-bulk-trusted-publishing-config-and-script-security-now-generally-available/ "npm bulk trusted publishing config and script security now generally available - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span></p>

npm CLI v11.10.0 출시.
`min-release-age`에서 패키지 공개에서 일정 시간 경과 지난 것만 설치하도록.
`npm trust` 명령어로 복수의 패키지 OIDC Trusted Publishing 설정을 일괄적으로 처리 가능.
`--allow-git` 플래그 추가로, git 의존 관계 설치할 때 보안 제어가 가능.`.npmrc`에서 git 실행 패스를 덮어써서 `--ignore-scripts` 사용할 때 코드 실행이 가능하도록한 문제 처리.
`--allow-git=none` 이용이 권장, npm CLI v12에서는 기본이 될 예정.

- [Release v11.11.0 · npm/cli](https://github.com/npm/cli/releases/tag/v11.11.0 "Release v11.11.0 · npm/cli")

----

## The React Foundation: A New Home for React Hosted by the Linux Foundation – React
[react.dev/blog/2026/02/24/the-react-foundation](https://react.dev/blog/2026/02/24/the-react-foundation "The React Foundation: A New Home for React Hosted by the Linux Foundation – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">community</span> <span class="jser-tag">organization</span> <span class="jser-tag">news</span></p>

React Foundation가 Linux Foundation 산하에 정식으로 설립됨.
React, React Native, JSX 프레젝트가 Meta에서 React Foundation으로 이관.
플래티넘 멤버로 Amazon, Callstack, Expo, Huawei, Meta, Microsoft, Software Mansion, Vercel 참가.
기술적인 거버넌스는 Foundation에서 독립되어 유지, 공헌자나 관리자가 기술적인 방향성 결정
지금부터 몇 개월간 레포지토리나 인프라 이관이 진행될 예정.


----

## Release styled-components@6.3.7 · styled-components/styled-components
[github.com/styled-components/styled-components/releases/tag/styled-components%406.3.7](https://github.com/styled-components/styled-components/releases/tag/styled-components%406.3.7 "Release styled-components@6.3.7 · styled-components/styled-components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

styled-components v6.3.7 출시.
`createGlobalStyle`가 React StrictMode나 RSC(React Server Components)으로 정상적으로 동작하지 않는 문제 수정.
package.json에서 `exports` 필드를 추가 ESM 대응 개선


----
<h1 class="site-genre">읽을거리</h1>

----

## Clinejection — Compromising Cline&#039;s Production Releases just by Prompting an Issue Triager | Adnan Khan - Security Research
[adnanthekhan.com/posts/clinejection/](https://adnanthekhan.com/posts/clinejection/ "Clinejection — Compromising Cline&#039;s Production Releases just by Prompting an Issue Triager | Adnan Khan - Security Research")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">AI</span> <span class="jser-tag">article</span></p>

Cline의 GitHub Actions 워크플로우 공격에 대한 글.
AI 사용해 Issue Triage에 Prompt Injection을 기점으로, GitHub Actions 캐시 포이즈닝을 조합한 공격 수법에 대해 정리.
공격이 성공한 경우, VSCode Marketplace/OpenVSX/npm 공개 토큰을 유출된 문제가 있음, 실제로 Cline CLI의 npm 패키지가 침해됨.


----

## Goodbye innerHTML, Hello setHTML: Stronger XSS Protection in Firefox 148 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/](https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/ "Goodbye innerHTML, Hello setHTML: Stronger XSS Protection in Firefox 148 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">XSS</span> <span class="jser-tag">security</span> <span class="jser-tag">DOM</span> <span class="jser-tag">article</span></p>

Firefox 148에서 구현된 Sanitizer API 관련해서.
`innerHTML`는 HTML를 필터링하지 않고 삽입함, `setHTML()`는 자동적으로 Sanitizer해서 XSS 원인이 될 위험한 요소나 속성을 제거함.
Sanitizer API 기본적 설정이나 커스텀 설정, Trusted Types와 조합에 대해서 다뤄짐.


----

## How we rebuilt Next.js with AI in one week
[blog.cloudflare.com/vinext/](https://blog.cloudflare.com/vinext/ "How we rebuilt Next.js with AI in one week")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">vite</span> <span class="jser-tag">article</span></p>

Cloudflare에 의한 Next.js 호환 프레임워크 vinext에 대하여.
Next.js 라우팅, React Server Components, Server Actions 기능을 Vite 기반으로 재구현.

- [cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere](https://github.com/cloudflare/vinext "cloudflare/vinext: Vite plugin that reimplements the Next.js API surface — deploy anywhere")

----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## millionco/react-doctor: Let coding agents diagnose and fix your React code
[github.com/millionco/react-doctor](https://github.com/millionco/react-doctor "millionco/react-doctor: Let coding agents diagnose and fix your React code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">performance</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">AI</span></p>

React 코드 기반 정적 해석으로, 헬스 스코어(0〜100) 검출하는 도구.
60 이상 규칙에서 state/effects, 성능, 아키텍처, 번들사이즈, 보안, 접근성등을 체크.
미사용 파일이나 export 검출, Next.js/Vite/Remix 같은 프레임워크 자동 검출에 대응.
CLI나 GitHub Actions, Node.js API로 이용 가능.


----

## vercel-labs/portless: Replace port numbers with stable, named .localhost URLs. For humans and agents.
[github.com/vercel-labs/portless](https://github.com/vercel-labs/portless "vercel-labs/portless: Replace port numbers with stable, named .localhost URLs. For humans and agents.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">server</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">debug</span></p>

포트번호 대신 `myapp.localhost` 같은 명명형 `.localhost` URL를 사용하는 개발용 프록시 도구.
`portless proxy start`로 데몬 기동, `portless myapp next dev` 같은 위험 서버를 기동.
`http://myapp.localhost:1355`같이 URL로 접근 가능.
HTTP/2나 HTTPS 증명서 자동생성 대응, Next.js/Express/Nuxt/Vite/Astro 프레임워크에서 이용 가능.


----
