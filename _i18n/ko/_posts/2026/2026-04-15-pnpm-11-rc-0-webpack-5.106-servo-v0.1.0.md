---
title: "2026-04-15: pnpm 11 RC 0, webpack 5.106, Servo v0.1.0"
author: "azu"
translator: rewrite0w0
layout: post
date: 2026-04-15T11:20:00.406Z
category: JSer
tags:
- React
- Rust
- search
- Next.js
- security

---

JSer.info #769 - pnpm v11.0.0 RC 0가 출시되었다.

- [Release pnpm 11 RC 0 · pnpm/pnpm](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

Pure ESM 패키지로 이행, Node.js 18부터 21까지 지원 종료했다.
`.npmrc`은 인증/레지스트리 설정만 한정했으며, 그 외 설정은 `pnpm-workspace.yaml`으로 이행, `pnpm server` 명령어 삭제 같은 많은 파괴적 변경이 포함된다.
또한, `pnpm ci` 명령어 추가, `pnpm sbom`으로 SBOM 생성 가능하다.
`minimumReleaseAge` 기본적으로 1일 설정, `blockExoticSubdeps` 기본값을 `true`로 변경, 공급망 보안 강화도 있다.
그 외로는, 스토어 인덱스에 SQLite 사용하도록 변경, `undici` 사용에 의한 HTTP 리퀘스트 개선도 있다.

----

webpack 5.106가 출시되었다.

- [Webpack 5.106 | webpack](https://webpack.js.org/blog/2026-04-08-webpack-5-106/)

Plugin Validation Hook(`compiler.hooks.validate`) 추가, CSS Modules 런타임 스타일 주입(`exportType: "style"`) 지원도 포함된다.
장차 css-loader/style-loader/mini-css-extract-plugin 폐지가 예정되어 있다.
그 외로도, CommonJS의 Tree Shaking 개선, `create-webpack-app` 도구 추가, 실험적 기능으로 ES Stage 3의 Source Phase Imports에 의한 WebAssembly 지원, oxc-parser 지원이 추가된다.
또한, webpack-cli 7.0.0에는 Node.js 20.9.0 이상이 필요하며, 네이티브 TypeScript 지원도 추가된다.

----

Rust로 작성된 임베디드에 사용 가능한 Web 렌더링 엔진 Servo의 `servo`가 crates.io에 공개되었다.

- [Servo is now available on crates.io](https://servo.org/blog/2026/04/13/servo-0.1.0-release/)

애플리케이션에 Web 렌더링 기능을 내장하기 위해 Embedding API를 제공한다.
또한, LTS 버전도 도입하여, 반 년마다 메이저 업그레이드와 보안 업데이트를 제공한다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v1.5.0 · Pagefind/pagefind
[github.com/Pagefind/pagefind/releases/tag/v1.5.0](https://github.com/Pagefind/pagefind/releases/tag/v1.5.0 "Release v1.5.0 · Pagefind/pagefind")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">search</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Pagefind v1.5.0 출시.
Web Components 기반 새로운 UI 시스템 추가, 메타데이터 필드의 기본 인덱스화에 의한 검색 정밀도 향상, 발음 구별 기호 대응을 추가.
CJK(중국어/일본어/한국어) 쿼리 자동 세그멘테이션, Web Worker에서 검색 실행, 인덱스 청크 크기 절감 같은 성능 개선.
Windows ARM64 지원 추가


----

## Webpack 5.106 | webpack
[webpack.js.org/blog/2026-04-08-webpack-5-106/](https://webpack.js.org/blog/2026-04-08-webpack-5-106/ "Webpack 5.106 | webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5.106 출시.
Plugin Validation Hook(`compiler.hooks.validate`) 추가.
CSS Modules 런타임 스타일 주입(`exportType: "style"`) 지원.
장차 css-loader/style-loader/mini-css-extract-plugin 폐지 예정.
CommonJS의 Tree Shaking 개선, `create-webpack-app` 도구 추가.
실험적 기능으로, ES Stage 3의 Source Phase Imports에 따른 실험적인 WebAssembly 지원, oxc-parser 지원.
webpack-cli 7.0.0에는 Node.js 20.9.0+가 필요하며, 네이티브 TypeScript 지원이 추가됨.


----

## Release pnpm 11 RC 0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0 "Release pnpm 11 RC 0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v11.0.0 rc.0 출시.
Pure ESM 패키지 이행, Node.js 18-21 지원 종료.
`.npmrc`는 인증/레지스트리 설정만 한정, 그 외 설정은 `pnpm-workspace.yaml`으로 이행, `pnpm server` 명령어 삭제 같은 많은 파괴적 변경 있음.
`pnpm ci` 명령어 추가, `pnpm sbom`으로 SBOM 생성.
`minimumReleaseAge` 기본적으로 1일 설정, `blockExoticSubdeps` 기본값을 `true`으로 변경 같은 공급망 보안 강화.
스토어 인덱스에 SQLite를 사용하도록 변경, `undici` 선택에 따른 HTTP 리퀘스트 개선.


----

## Bun v1.3.12 | Bun Blog
[bun.com/blog/bun-v1.3.12](https://bun.com/blog/bun-v1.3.12 "Bun v1.3.12 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.3.12 출시.
`Bun.WebView` 추가, Markdown 파일을 터미널에서 직접 실행 가능한 `bun ./file.md` 지원.
인프로세스로 동작하는 콜백 기반 cron 스케쥴러 `Bun.cron()` 추가.
JavaScriptCore 업그레이드로 인해, ES Proposal Stage 3의 Explicit Resource Management(`using`/`await using`) 지원.
cgroup의 CPU 제한을 고려하도록 변경


----

## Servo is now available on crates.io - Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.
[servo.org/blog/2026/04/13/servo-0.1.0-release/](https://servo.org/blog/2026/04/13/servo-0.1.0-release/ "Servo is now available on crates.io - Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">servo</span> <span class="jser-tag">Rust</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

Servo v0.1.0 출시.
Rust으로 작성된 임베디드 가능한 Web 렌더링 엔진 Servo의 `servo`가 crates.io에 공개됨.
애플리케이션에 Web 렌더링 기능을 내장하기 위해 Embedding API 제공.
LTS 버전도 도입되어, 반 년마다 메이저 업그레이드와 보안 업그레이드 제공.


----
<h1 class="site-genre">읽을거리</h1>

----

## Summary of CVE-2026-23869 - Vercel
[vercel.com/changelog/summary-of-cve-2026-23869](https://vercel.com/changelog/summary-of-cve-2026-23869 "Summary of CVE-2026-23869 - Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">security</span> <span class="jser-tag">vercel</span></p>

React Server Components(RSC)의 DoS 취약성 수정으로 Next.js 15.5.15/16.2.3과 React 19.2.5가 출시.
App Router의 Server Function 엔드포인트에 대해, 세공된 HTTP 리퀘스트를 보냄으로 과도한 CPU 비용을 일으키는 취약성.
Next.js 13.x〜16.x가 영향을 받음.

- [Release 19.2.5 (April 8th, 2026) · facebook/react](https://github.com/facebook/react/releases/tag/v19.2.5 "Release 19.2.5 (April 8th, 2026) · facebook/react")

----

## The uphill climb of making diff lines performant - The GitHub Blog
[github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/ "The uphill climb of making diff lines performant - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GitHub</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

GitHub의 Files changed 탭의 React 기반 구현 diff행 성능 최적화.
1행에 10〜15개 DOM 요소와 8〜13개 React 컴포넌트가 필요한 구조로 최적화.
컴포넌트 수를 2개로 삭제, 이벤트 핸들러를 data 속성을 활용해 단일 핸들러에 집약하도록 변경.
TanStack Virtual에 의한 가상화 도입, 무거운 CSS 셀렉터 삭제, 드래그/리사이즈 처리 재구현 등으로 성능 개선.


----

## React Server Components Your Way | TanStack Blog
[tanstack.com/blog/react-server-components](https://tanstack.com/blog/react-server-components "React Server Components Your Way | TanStack Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">RSC</span> <span class="jser-tag">TanStack</span> <span class="jser-tag">article</span></p>

TanStack으로 React Server Components(RSC) 어프로치하는 방법에 대하여.
RSC를 데이터 스트림으로 다루고, 단방향 데이터 흐름으로 클라이언트 측에 서버 렌더링 된 UI 얻기나 캐시 제어 가능한 설계.
서버가 슬롯을 준비해뒀다가 클라이언트가 채우는 Composite Components 구조, `createServerFn`에 의한 명시적 서버 함수 정의 기능을 제공.


----

## The Intl API: The best browser API you&#039;re not using | Polypane
[polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/ "The Intl API: The best browser API you&#039;re not using | Polypane")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">article</span></p>

Intl API에 대한 해설 글.
`Intl.DateTimeFormat`/`Intl.RelativeTimeFormat`/`Intl.NumberFormat` 날짜나 수치 포맷 API를 소개.
`Intl.ListFormat`/`Intl.PluralRules`/`Intl.Segmenter`/`Intl.Collator` 사용 방법


----

## Under the hood of MDN&#039;s new frontend
[developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/ "Under the hood of MDN&#039;s new frontend")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">architecture</span> <span class="jser-tag">article</span></p>

MDN 프론트엔드 아키텍처 업데이트 글.
옛 프론트엔드(Yari)는 Create React App 기반, eject 후에 webpack 설정 복잡 같은 기술부채가 있었음.
Sass와 최신 CSS 혼재, `dangerouslySetInnerHTML`에 의한 정적 컨텐츠 담기 문제도 있었음.
새 아키텍처에서는 Lit 기반 Web Components 선택, 독자 Server Components 구조에서 SPA 문제를 해결.
빌트인을 webpack에서 Rspack으로 이행, Declarative Shadow DOM나 Baseline 프로젝트를 활용한 브라우저 호환성 관리도 언급.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## yuku-toolchain/yuku: High-performance JavaScript/TypeScript compiler and toolchain in pure Zig 🦎
[github.com/yuku-toolchain/yuku](https://github.com/yuku-toolchain/yuku "yuku-toolchain/yuku: High-performance JavaScript/TypeScript compiler and toolchain in pure Zig 🦎")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Zig</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">compiler</span> <span class="jser-tag">Tools</span></p>

Zig로 작성된 JavaScript/TypeScript 컴파일 및 툴체인.
Test262에서 테스트되었고, Pure Zig 같은 곳에서 크로스 컴파일 가능.


----

## Diffs, from Pierre
[diffs.com/](https://diffs.com/ "Diffs, from Pierre")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">diff</span></p>

diff 렌더링 코드 게시 라이브러리.
CSS Grid와 Shadow DOM를 활용해 DOM 노트 수를 삭제하며 렌더링 고속화나 Virtualization에 대응.
Stack 형(통합게시)과 Split 형(좌우 병렬 게시) 2가지 레이아웃, Shiki 기반 구문 하이라이트/주석/머지 충돌 해결 UI 기능 갖음.


----
