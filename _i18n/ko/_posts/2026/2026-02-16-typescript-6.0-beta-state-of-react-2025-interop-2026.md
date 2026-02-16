---
title: "2026-02-16: TypeScript 6.0 Beta, State of React 2025 결과, Interop 2026"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-02-16T10:52:55.838Z
category: JSer
tags:
- browser
- CSS
- TypeScript
- safari
- Fetch

---

JSer.info #764 - TypeScript 6.0 Beta가 출시되었다.

- [Announcing TypeScript 6.0 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)

TypeScript 7(Go언어 기반)으로 마이그레이션에 집중한 출시로, 많은 기본 설정 변경 및 비권장화가 포함되어있다. `strict`가 기본적으로 `true`로, `module` 기본이 `esnext`으로, `target` 기본이 `es2025`으로 등으로 변경되었다. 또한, `target: es5`이나 `--moduleResolution node10` 등이 비권장이 되어, ES2025의 `RegExp.escape`이나 Temporal의 자료형 정의 추가, TypeScript 7으로 마이그레이션을 보조하는 `--stableTypeOrdering` 플래그 추가도 포함되어있다.

---

State of React 2025 앙케이트 결과가 공개되었다.

- [State of React 2025](https://2025.stateofreact.com/en-US)

React 기능, 프레임워크, 상태 관리, 데이터 페칭, 메타 프레임워크, 도구, AI 활용에 대한 앙케이트 결과가 정리되어 있다.

---

브라우저 상호운용성 향상을 목표로하는 프로젝트 Interop 2026가 개시되었다.

- [Interop 2026가 시작되었다!](https://zenn.dev/yamanoku/articles/interop-2026-launched)
- [Launching Interop 2026 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2026/02/launching-interop-2026/)
- [Announcing Interop 2026 | WebKit](https://webkit.org/blog/17818/announcing-interop-2026/)
- [Interop 2026 Focus Areas Announced | Igalia](https://www.igalia.com/news/interop-2026.html)
- [Interop 2026: Continuing to improve the web for developers | web.dev](https://web.dev/blog/interop-2026)
- [Microsoft Edge and Interop 2026 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2026/02/12/microsoft-edge-and-interop-2026/)

Apple, Google, Microsoft, Mozilla 등의 브라우저 벤더가 참가, CSS Anchor Positioning, Container Style Queries, Navigation API, View Transitions 등이 포커스 에리어로 선택되었다. 그 외로는 Scroll-driven Animations, IndexedDB, WebRTC, WebTransport 등 합계 20분야가 대상이다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 6.0 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/ "Announcing TypeScript 6.0 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 6.0 Beta 출시.
TypeScript 7(Go언어 기반)으로 마이그레이션에 집중한 출시로, 많은 기본 설정 변경이나 비권장화 포함.
`strict`가 기본적으로 `true`으로 변경, `module` 기본이 `esnext`으로 변경, `target` 기본적으로 `es2025`으로 변경, `types` 기본이 `[]`으로 변경.
`target: es5`/`--moduleResolution node10`/`--module amd|umd|system`/`--outFile` 등을 비권장화.
ES2025의 `RegExp.escape`이나 Temporal 자료형 정의를 추가, `lib.dom`으로 `dom.iterable`와 `dom.asynciterable` 통합.
TypeScript 7으로 마이그레이션 보조하는 `--stableTypeOrdering` 플래그 추가.


----

## WebKit features for Safari 26.3 | WebKit
[webkit.org/blog/17798/webkit-features-for-safari-26-3/](https://webkit.org/blog/17798/webkit-features-for-safari-26-3/ "WebKit features for Safari 26.3 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 26.3 출시.
zstd 지원, Navigation API의 `NavigateEvent`으로 `AbortSignal` 공개, 네비게이션 중단할 때에 처리를 캔슬가능.
CSS의 `position-try`이나 `text-decoration`, 멀티 컬럼 레이아웃 관련한 버그 수정.


----

## Biome v2.4—Embedded Snippets, HTML Accessibility, and Better Framework Support | Biome
[biomejs.dev/blog/biome-v2-4/](https://biomejs.dev/blog/biome-v2-4/ "Biome v2.4—Embedded Snippets, HTML Accessibility, and Better Framework Support | Biome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">biome</span> <span class="jser-tag">ReleaseNote</span></p>

Biome v2.4 출시.
JavaScript내에 포함된 CSS이나 GraphQL 스니펫의 Formatter와 Lint를 지원.
HTML 접근성 대상 15개 Lint 규칙 추가.
Vue/Svelte/Astro 지원 개선, CSS 파서에서 Vue SFC의 `:slotted`이나 `:deep` 대응.
SARIF 레포트 추가, `--skip`/`--only` 플래그 지원.


----
<h1 class="site-genre">읽을거리</h1>

----

## Blog &gt; Writing Good Unit Tests
[eliocapella.com/blog/writing-good-unit-tests/](https://eliocapella.com/blog/writing-good-unit-tests/ "Blog &gt; Writing Good Unit Tests")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">test</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

유닛테스트 작성 방법에 대한 글.
함수가 아닌 동작을 테스트하는 것, 시스템 경계만 Mock화하는 것, 인메모리 데이터 베이스 활용, HTTP Mock에 대해서


----

## State of React 2025
[2025.stateofreact.com/en-US](https://2025.stateofreact.com/en-US "State of React 2025")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Survey</span></p>

State of React 2025 앙케이트 결과가 공개되었다.
React 기능, 프레임워크, 상태관리, 데이터페칭, 메타 프레임워크, 도구, AI 활용 등에 대한 앙케이트 결과 정리.


----

## The CSS Selection - 2026 Edition - Project Wallace
[www.projectwallace.com/the-css-selection/2026](https://www.projectwallace.com/the-css-selection/2026 "The CSS Selection - 2026 Edition - Project Wallace")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

10만 이상 웹사이트 대상으로 한 실제 CSS 이용 상황 조사 레포트.
Web Almanac의 CSS 대체로, CSS 파일 크기, 프로퍼티 이용률, 모던 CSS 기능 선택률 등 정리.
`:where()` 91%, `:has()` 41%, `@container` 10%, `@layer` 2.7% 선택률임.
벤더 prefix나 IE6 시대 브라우저 hack이 아직 남아있는 점에 대해 다뤄짐.


----

## Interop 2026가 시작되었다!
[zenn.dev/yamanoku/articles/interop-2026-launched](https://zenn.dev/yamanoku/articles/interop-2026-launched "Interop 2026가 시작되었다!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

브라우저 상호운용성 향상을 목표로한 프로젝트 Interop 2026에 대하여.
Apple, Google, Microsoft, Mozilla 같은 브라우저 벤더가 참가.
CSS Anchor Positioning, Container Style Queries, Navigation API, View Transitions가 포커스 에리어로 선정됨.
그 외로는 Scroll-driven Animations, IndexedDB, WebRTC, WebTransport 등 합계 20 분야가 대상이 됨.
조사 대상으로 접근성 테스트, JPEG XL, 모바일 테스트, WebVTT의 4분야가 포함.

- [Launching Interop 2026 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2026/02/launching-interop-2026/ "Launching Interop 2026 - Mozilla Hacks - the Web developer blog")
- [Announcing Interop 2026 | WebKit](https://webkit.org/blog/17818/announcing-interop-2026/ "Announcing Interop 2026 | WebKit")
- [Interop 2026 Focus Areas Announced | Igalia](https://www.igalia.com/news/interop-2026.html "Interop 2026 Focus Areas Announced | Igalia")
- [Interop 2026: Continuing to improve the web for developers | web.dev](https://web.dev/blog/interop-2026 "Interop 2026: Continuing to improve the web for developers | web.dev")
- [Microsoft Edge and Interop 2026 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2026/02/12/microsoft-edge-and-interop-2026/ "Microsoft Edge and Interop 2026 - Microsoft Edge Blog")

----

## Web 폰트를 사용한 contenteditable 에서 탈출
[techblog.lycorp.co.jp/ja/20260216c](https://techblog.lycorp.co.jp/ja/20260216c "Web 폰트 사용해 contenteditable 에서 탈출")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">fonts</span> <span class="jser-tag">article</span></p>

임의 크기의 변형 가능한 공백 문자를 갖고 있는 웹폰트와 텍스트 오버레이를 사용해 텍스트 에리어에 이모티콘 등을 보이는 방법에 대해


----

## Roadmap 2026 (2026-02-04) | webpack
[webpack.js.org/blog/2026-04-02-roadmap-2026/](https://webpack.js.org/blog/2026-04-02-roadmap-2026/ "Roadmap 2026 (2026-02-04) | webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack 2026년 로드맵.
CSS Modules 네이티브 지원, TypeScript 로더없이 빌드, HTML 엔트리 포인트 플래그인 없이 이용을 webpack 본체에 내장 예정.
Node.js/Deno/Bun 크로스 런타임 대응, Barrel File 지연 최적화, Minimizer 플러그인 통합도 계획.
webpack 6 출시 변경에 대해 소개.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## npmx - Package Browser for the npm Registry
[npmx.dev/](https://npmx.dev/ "npmx - Package Browser for the npm Registry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">search</span> <span class="jser-tag">webservice</span></p>

npm 레지스트리 인크리멘탈 검색 서비스.
Algolia에 의한 패키지 검색, 패키지 비교 기능, npm/pnpm/yarn/bun/deno/vlt 등의 패키지 매니저에 대응한 설치 명령어 표시 기능이 있음.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## hamzaydia/verifyfetch: Resumable, verified downloads for large browser files. Fail at 3.8GB, resume from 3.8GB.
[github.com/hamzaydia/verifyfetch](https://github.com/hamzaydia/verifyfetch "hamzaydia/verifyfetch: Resumable, verified downloads for large browser files. Fail at 3.8GB, resume from 3.8GB.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">WebAssembly</span></p>

브라우저에서 대용량 파일 다운로드에 대해, resume 대응과 정합성 검증하는 라이브러리.
WebAssembly에 의한 스트리밍 해쉬 계산, HTTP Range 리퀘스트에 의한 resume 다운로드, IndexedDB으로 Chunk 저장 지원.
사전에 파일을 일정 chunk으로 나눠진 해시 생성해두고, 매 Chunk 검증.


----

## bikeshaving/shovel: Run Service Workers anywhere
[github.com/bikeshaving/shovel](https://github.com/bikeshaving/shovel "bikeshaving/shovel: Run Service Workers anywhere")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">Bun</span> <span class="jser-tag">cloudflare</span></p>

Service Worker API나 Web 표준 API 인터페이스를 기반으로 한 서버 애플리케이션을 작성하는 메타 프레임워크.
Node.js/Bun/Cloudflare Workers에서 동작.
Service Worker의 `install`/`activate`/`fetch` 이벤트를 기반으로 한 서버 라이프 사이클을 갖음.
Fetch API, Cache API, FileSystem API, CookieStore API, URLPattern의 Web 표준API를 기반으로 함.


----

## ubugeeei/vize: Unofficial High-Performance Vue.js Toolchain in Rust
[github.com/ubugeeei/vize](https://github.com/ubugeeei/vize "ubugeeei/vize: Unofficial High-Performance Vue.js Toolchain in Rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">compiler</span></p>

Rust으로 작성된 Vue.js 도구 체인.
Vue SFC 컴파일러, Linter, Formatter, 자료형 체커, LSP를 포함.
CLI/Browser(WebAssembly)/Vite Plugin으로 이용 가능


----
