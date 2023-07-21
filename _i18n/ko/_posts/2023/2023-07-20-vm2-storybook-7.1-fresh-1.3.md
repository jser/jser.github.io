---
title: "2023-07-20: vm2 개발종료, Storybook 7.1, Fresh 1.3"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-07-20T12:49:40.487Z
category: JSer
tags:
- node.js
- security
- Tools
- ECMAScript
- proposal

---

JSer.info #652 - Node.js의 [node:vm](https://nodejs.org/api/vm.html) 모듈은 Sandbox(신용할 수 없는 코드 실행하는 환경)으로 [이용할 수 없습니다](https://snyk.io/blog/security-concerns-javascript-sandbox-node-js-vm-module/)만, [vm2](https://github.com/patriksimek/vm2)는 `node:vm`를 Wrap해서 Sandbox를 제공했던 모듈이었습니다.

 `vm2`이 구조적으로 수정할 수 없는 곳에서 Sandbox 취약성이 발견되었기에, 유지보수 종료 선언했습니다. 취약성에 대한 자세한 정보는 아직 공개되어있지 않습니다만, Sandbox를 깨트리는 취약성으로, [PoC는 8월즈음](https://github.com/patriksimek/vm2/issues/533#issuecomment-1632482080) 공개될 예정입니다.

- [Discontinued · Issue #533 · patriksimek/vm2](https://github.com/patriksimek/vm2/issues/533)
- [vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database](https://github.com/advisories/GHSA-cchq-frgv-rjh5)

Sandbox 기능이 필요하다면, QuickJS를 WebAssembly로 컴파일한 [quickjs-emscripten](https://github.com/justjake/quickjs-emscripten)이나 V8의 Isolate를 사용한[isolated-vm](https://github.com/laverdet/isolated-vm)로 이행하길 권장하고 있습니다.
[proxy-agents](https://github.com/TooTallNate/proxy-agents)(PAC파일을 평가하기 위해 vm2 이용했었습니다)는 `quickjs-emscripten`으로 이행했습니다.

- [Use `quickjs-emscripten` instead of `vm2` to execute PAC file code by TooTallNate · Pull Request #224 · TooTallNate/proxy-agents](https://github.com/TooTallNate/proxy-agents/pull/224)

`vm2`는 `node:vm` 상에서 실행하는 코드에서 호스트 환경을 참조하지 못하도록 패치로 막는 접근을 취하고 있어습니다.(📝 `node:vm`를 사용한 적이 있는 사람 대상 이야기. context로 넘겨 객체에 Proxy를 사용, 특정 프로퍼티를 참조하지 못하게 하기 등)
손쉽지만, 막지 못하는 구멍이 생기거나 빠지는 것이 있었던 접근법이었습니다.

이런 Sandbox에는 어떤 접근법이 있는가에 대해서는 다음 글이 흥미로울 것 입니다.

- [How to build a plugin system on the web and also sleep well at night | Figma Blog](https://www.figma.com/ja/blog/how-we-built-the-figma-plugin-system/)
- [Sandboxing and Workload Isolation · Fly](https://fly.io/blog/sandboxing-and-workload-isolation/)

---

Storybook 7.1가 출시되었습니다.

- [Storybook 7.1](https://storybook.js.org/blog/storybook-7-1/)

Storybook상에서 온보딩 추가, Emotion 등 스타일링 라이브러리 리셋 자동화, Vue 지원 개선이 포함되어있습니다.
또한 지금까지 커뮤니티에서 개발한 Figma design addon를 코어 Addon으로 관리하기 시작했습니다.

----

Deno의 웹 프레임워크니 Fresh 1.3가 출시되었습니다.

- [Fresh 1.3 – Simplified Route Components and More](https://deno.com/blog/fresh-1.3)

비동기 루트 컴포넌트 지원, 플러그인이 라우팅이나 미들웨어를 정의할 수 있도록, `_500.tsx` 에러페이지 지원, ErrorBoundary 지원이 추가되었습니다.
또한, 파일 하나에서 여러 islands를 export 할 수 있게끔 되었으며, `Deno.serve` 지원도 추가되었습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## ECMAScript proposal updates @ 2023-07 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2023/07/14/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2023/07/14/ecmascript-proposal-update "ECMAScript proposal updates @ 2023-07 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2023년 7월 TC39 Meeting에서 ECMAScript Proposal 스테이지 변경 정리


----

## Discontinued · Issue #533 · patriksimek/vm2
[github.com/patriksimek/vm2/issues/533](https://github.com/patriksimek/vm2/issues/533 "Discontinued · Issue #533 · patriksimek/vm2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span></p>

Node.js의 `vm` 모듈을 사용해서 Sandbox 실현했던 `vm2`가 구조적으로 Sandbox Escape 취약점이 있어, 유지보수가 종료되었다는 공지.
취약성 PoC는 2023년 8월즈음에 공개하기에, isolated-vm 같은 모듈로 이행하기 권하고 있다.

- [vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database](https://github.com/advisories/GHSA-cchq-frgv-rjh5 "vm2 Sandbox Escape vulnerability · CVE-2023-37466 · GitHub Advisory Database")
- [laverdet/isolated-vm: Secure &amp; isolated JS environments for nodejs](https://github.com/laverdet/isolated-vm "laverdet/isolated-vm: Secure &amp;amp; isolated JS environments for nodejs")

----

## Release v0.18.13 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.13](https://github.com/evanw/esbuild/releases/tag/v0.18.13 "Release v0.18.13 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.13 출시.
`DEV: doAnExpensiveCheck()` 같은 라벨 지정한 처리를, `--drop-label`으로 삭제할 수 있도록.


----

## Release Notes for Safari Technology Preview 174 | WebKit
[webkit.org/blog/14390/release-notes-for-safari-technology-preview-174/](https://webkit.org/blog/14390/release-notes-for-safari-technology-preview-174/ "Release Notes for Safari Technology Preview 174 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 174 출시.
Canvas 자체 설정된 합산 메모리 사용량 제한 삭제.

- [Total Canvas Memory Use Exceeds The Maximum Limit - PQINA](https://pqina.nl/blog/total-canvas-memory-use-exceeds-the-maximum-limit/ "Total Canvas Memory Use Exceeds The Maximum Limit - PQINA")

----

## Node v18.17.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v18.17.0](https://nodejs.org/en/blog/release/v18.17.0 "Node v18.17.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.17.0 출시.
URL 파서 Ada 2.0로 업데이트, `URL.canParse` 지원, Web Crypto API 사양과 호환성 향상


----

## Release 1.0.3 · kamranahmedse/driver.js
[github.com/kamranahmedse/driver.js/releases/tag/1.0.3](https://github.com/kamranahmedse/driver.js/releases/tag/1.0.3 "Release 1.0.3 · kamranahmedse/driver.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

사이트 투어해주는 Driver.js 1.0 출시.
TypeScript으로 재작성, SVG를 페이지 상 올려 하이라이트 표시할 수 있도록 구현 변경, 문서 갱신


----

## Storybook 7.1
[storybook.js.org/blog/storybook-7-1/](https://storybook.js.org/blog/storybook-7-1/ "Storybook 7.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 7.1 출시.
온보딩 추가, Emotion 등 스타일링 라이브러리 리셋 자동화, Vue 지원 개선.
Figma design addon 코어로 다룸


----

## Chrome 116 beta - Chrome Developers
[developer.chrome.com/en/blog/chrome-116-beta/](https://developer.chrome.com/en/blog/chrome-116-beta/ "Chrome 116 beta - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 116 beta 출시.
CSS Motion Path, `display`와 `content-visibility`에 키프레임 애니메이션 지원.
`AbortSignal.any()` 지원, Fetch API `getReader({mode: 'byob'})` 지원, Document Picture-in-Picture 지원.
Permissions Policy Origins에 `*` wildcard 지정 지원.
Origin Trial으로 COOP의 `restrict-properties` 지원, EditContext API 지원

- [Use a ReadableStream with byte source (formerly called ReadableByteStream) for .body · Issue #267 · whatwg/fetch](https://github.com/whatwg/fetch/issues/267 "Use a ReadableStream with byte source (formerly called ReadableByteStream) for .body · Issue #267 · whatwg/fetch")
- [ReadableStream.getReader() - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/ReadableStream/getReader "ReadableStream.getReader() - Web API | MDN")
- [Wildcards in Permissions Policy Origins by arichiv · Pull Request #516 · w3c/webappsec-permissions-policy](https://github.com/w3c/webappsec-permissions-policy/pull/516 "Wildcards in Permissions Policy Origins by arichiv · Pull Request #516 · w3c/webappsec-permissions-policy")
- [w3c/edit-context: EditContext API](https://github.com/w3c/edit-context "w3c/edit-context: EditContext API")

----

## Fresh 1.3 – Simplified Route Components and More
[deno.com/blog/fresh-1.3](https://deno.com/blog/fresh-1.3 "Fresh 1.3 – Simplified Route Components and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Fresh 1.3 출시.
비동기 루트 컴포넌트 지원, 플러그인이 라우팅이나 미들웨어 정의할 수 있도록, `_500.tsx`으로 에러페이지 지원, ErrorBoundary 지원.
파일 하나에서 여러 islands를 export 할 수 있도록, `Deno.serve` 지원

- [feat: support async route components by marvinhagemeister · Pull Request #1388 · denoland/fresh](https://github.com/denoland/fresh/pull/1388 "feat: support async route components by marvinhagemeister · Pull Request #1388 · denoland/fresh")
- [feat(server): plugins can add middlewares and routes by deer · Pull Request #1455 · denoland/fresh](https://github.com/denoland/fresh/pull/1455 "feat(server): plugins can add middlewares and routes by deer · Pull Request #1455 · denoland/fresh")

----

## Release v0.18.14 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.14](https://github.com/evanw/esbuild/releases/tag/v0.18.14 "Release v0.18.14 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">esbuild</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.14 출시.
CSS Modules 지원의 일환으로, `global-css` loader와 `local-css` loader 추가, CSS에서 `:local()`와 `:global()` 지원.


----
<h1 class="site-genre">읽을거리</h1>

----

## URL.canParse
[davidwalsh.name/url-canparse](https://davidwalsh.name/url-canparse "URL.canParse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">article</span></p>

URL이 paser할 수 있는가 판정하는 `URL.canParse` 메서드에 대하여

- [URL: canParse() static method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/URL/canParse_static "URL: canParse() static method - Web APIs | MDN")

----

## How React 18 Improves Application Performance – Vercel
[vercel.com/blog/how-react-18-improves-application-performance](https://vercel.com/blog/how-react-18-improves-application-performance "How React 18 Improves Application Performance – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18のTransitions, Suspense, Server Components 관련하여


----

## Security alert: social engineering campaign targets technology industry employees - The GitHub Blog
[github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/](https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/ "Security alert: social engineering campaign targets technology industry employees - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">security</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

채용담당자나 개발자 사칭, 비밀 레포지토리에 초대, 레포지토리 clone해 설치하면 감염시키는 멀웨어 삽입하는 공격이 증가하고 있다는 이야기.
マルウェア는 npm install할 때, 다운로드 및 실행되는 구조

- [Phylum Discovers Sophisticated Ongoing Attack on NPM](https://blog.phylum.io/sophisticated-ongoing-attack-discovered-on-npm/ "Phylum Discovers Sophisticated Ongoing Attack on NPM")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## coderaiser/putout: 🐊 Pluggable and configurable JavaScript Linter and code transformer with built-in ESLint and Babel support for js, jsx typescript, flow, markdown, yaml and json. Write declarative codemods in a simplest possible way 😏
[github.com/coderaiser/putout](https://github.com/coderaiser/putout "coderaiser/putout: 🐊 Pluggable and configurable JavaScript Linter and code transformer with built-in ESLint and Babel support for js, jsx typescript, flow, markdown, yaml and json. Write declarative codemods in a simplest possible way 😏")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">Tools</span></p>

Babel와 ESLint를 기반으로 한 codemod 툴킷.
빌트인 규칙으로 CommonJS to ESM 같은 다수 변환 규칙을 가지고 있으며, 이를 관리하는 구조와 플러그인을 제공한다.


----
