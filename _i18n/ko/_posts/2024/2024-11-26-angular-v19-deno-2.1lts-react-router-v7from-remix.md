---
title: "2024-11-26: Angular v19, Deno 2.1(LTS), React Router v7(from Remix)"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-11-26T02:04:02.199Z
category: JSer
tags:
- React
- nodejs
- playwright
- TypeScript
- tool

---

JSer.info #716 - Angular v19가 출시되었습니다.

- [Meet Angular v19. In the past two years we doubled down… | by Minko Gechev | Nov, 2024 | Angular Blog](https://blog.angular.dev/meet-angular-v19-7b29dfd05b84)
- [Release v19.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/19.0.0)
- [Angular v19 Developer Event - YouTube](https://www.youtube.com/watch?v=JvkX2_46gUY)

Developer preview로 새로운 Incremental Hydration 구조 추가, ServerRoute으로 렌더링 모드 지정 가능, HMR 지원이 추가 되었습니다.

Incremental Hydration은, `@defer`으로 Hydration를 지연 실행하며, Hydration 할 때까지는 `@placeholder`으로 플레이스 홀더 게시할 수 있습니다. Qwik의 [Resumable](https://qwik.dev/docs/concepts/resumable/)와 거의 닮은 개념이지만, `@defer`는 Hydration하는 타이밍도 지정 가능합니다.

- [Incremental Hydration • Angular](https://angular.dev/guide/incremental-hydration)
- [[Complete] RFC: Incremental Hydration · angular/angular · Discussion #57664](https://github.com/angular/angular/discussions/57664)

또한, Standalone component가 기본적으로 `true`로 변경, `linkedSignal` 추가, `resource()` API 추가되었습니다.


----

Deno v2.1가 출시되었습니다.

- [Deno 2.1: Wasm Imports and other enhancements](https://deno.com/blog/v2.1)

Deno 2.1는 LTS 출시로, 2025년 4월까지 지원될 예정입니다.

![Deno LTS](https://docs.deno.com/runtime/fundamentals/images/deno-lts-support.png)

- [Stability and releases](https://docs.deno.com/runtime/fundamentals/stability_and_releases/)

`.wasm` 임포트 대응, `deno init --npm` 추가, `deno outdated` 추가, `deno compile`가 Assets 담길 수 있도록.
`deno task`으로 description 볼 수 있도록, task 간 의존 관계를 정의할 수 있도록 변경되었습니다.

---

React Router v7가 출시되었습니다.

- [React Router v7 | Remix](https://remix.run/blog/react-router-v7)

React Router v7은, Remix v2 메이저 업데이트 버전이 되는 버전입니다.
이에, React Router v6와 Remix v2에서 업데이트 가이드도 공개되었습니다.

- [Upgrading from v6 | React Router](https://reactrouter.com/upgrading/v6)
- [Upgrading from Remix | React Router](https://reactrouter.com/upgrading/remix)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Bun v1.1.35 | Bun Blog
[bun.sh/blog/bun-v1.1.35](https://bun.sh/blog/bun-v1.1.35 "Bun v1.1.35 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.35 출시.
Musl과 Alpine Linux 네이티브 지원, `bun test` 결과를 JUnit XML 형식으로 출력 가능, `Worker`의 preload 지원


----

## Meet Angular v19. In the past two years we doubled down… | by Minko Gechev | Nov, 2024 | Angular Blog
[blog.angular.dev/meet-angular-v19-7b29dfd05b84](https://blog.angular.dev/meet-angular-v19-7b29dfd05b84 "Meet Angular v19. In the past two years we doubled down… | by Minko Gechev | Nov, 2024 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v19 출시.
Developer preview으로 새로운 Incremental Hydration 구조 추가, ServerRoute으로 렌더링 모드 지정 가능, HMR 지원.
Standalone component가 기본적으로 `true`로 변경, `linkedSignal` 추가, `resource()` API 추가

- [Release v19.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/19.0.0 "Release v19.0.0 · angular/angular")
- [Angular v19 Developer Event - YouTube](https://www.youtube.com/watch?v=JvkX2_46gUY "Angular v19 Developer Event - YouTube")

----

## Node.js — Node v23.3.0 (Current)
[nodejs.org/en/blog/release/v23.3.0](https://nodejs.org/en/blog/release/v23.3.0 "Node.js — Node v23.3.0 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v23.3.0 출시.
`util.getCallSite()`가 Source Map 지원.
Node.js 관한 변경으로 SEMVER-MAJOR 커밋이 main 브런치에 들어갈 시에 규칙 엄격화


----

## Deno 2.1: Wasm Imports and other enhancements
[deno.com/blog/v2.1](https://deno.com/blog/v2.1 "Deno 2.1: Wasm Imports and other enhancements")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">dneo</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.1 출시.
LTS가 출시로, 2025년 4월까지 지원됨.
`.wasm` 임포트 대응, `deno init --npm` 추가, `deno outdated` 추가, `deno compile`가 Assets 담을 수 있도록.
`deno task`로 description를 볼 수 있도록, task 간 의존관계를 정의 가능하도록

- [Stability and releases](https://docs.deno.com/runtime/fundamentals/stability_and_releases/ "Stability and releases")

----

## November 20, 2024 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2024-11-20.html](https://react-spectrum.adobe.com/releases/2024-11-20.html "November 20, 2024 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

react-aria-components 1.5.0  출시.
`ToggleButtonGroup` 추가, `MenuSection` 째로 설정을 갖을 수 있도록, TypeScript 설정을 Strict으로 변경, Accordion과 Disclosure를 GA으로 변경


----

## Node.js 22 runtime now available in AWS Lambda | AWS Compute Blog
[aws.amazon.com/jp/blogs/compute/node-js-22-runtime-now-available-in-aws-lambda/](https://aws.amazon.com/jp/blogs/compute/node-js-22-runtime-now-available-in-aws-lambda/ "Node.js 22 runtime now available in AWS Lambda | AWS Compute Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">Lambda</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">news</span></p>

AWS Lambda에서 Node.js 22 지원


----

## React Router v7 | Remix
[remix.run/blog/react-router-v7](https://remix.run/blog/react-router-v7 "React Router v7 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Remix</span> <span class="jser-tag">ReleaseNote</span></p>

React Router v7 출시.
React Router v7은 Remix v2 메이저 업데이트 버전임.
React Router v6와 Remix v2에서 업데이트 가이드도 공개.

- [Upgrading from v6 | React Router](https://reactrouter.com/upgrading/v6 "Upgrading from v6 | React Router")
- [Upgrading from Remix | React Router](https://reactrouter.com/upgrading/remix "Upgrading from Remix | React Router")

----

## Announcing TypeScript 5.7 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-7/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7/ "Announcing TypeScript 5.7 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.7 출시.
초기화되어 있지 않은 변수 체크, 상대 경로 `.ts` 출력 시에 `.js`으로 변환하는 `--rewriteRelativeImportExtensions` 플래그 추가.
`--target es2024` 지원, Node.js 22의 V8 Compile Cache 지원해서 실행 속도 개선


----

## Release v1.49.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.49.0](https://github.com/microsoft/playwright/releases/tag/v1.49.0 "Release v1.49.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.49.0 출시.
Aria Snapshot 추가, 오래된 헤드리스 모드(`chromium-headless-shell`)와 새로운 헤드리스 모드 모두 다운로드되도록 변경.
`--only-shell` 사용해서 오래된 헤드리스 모드만 다운로드 가능. 새로운 헤드리스 모드 전환은 `channel: 'chromium'`.

- [Changes in Chromium headless in Playwright v1.49 · Issue #33566 · microsoft/playwright](https://github.com/microsoft/playwright/issues/33566 "Changes in Chromium headless in Playwright v1.49 · Issue #33566 · microsoft/playwright")
- [Download old Headless Chrome as chrome-headless-shell  |  Blog  |  Chrome for Developers](https://developer.chrome.com/blog/chrome-headless-shell "Download old Headless Chrome as chrome-headless-shell  |  Blog  |  Chrome for Developers")

----

## State of HTML 2024
[2024.stateofhtml.com/en-US/](https://2024.stateofhtml.com/en-US/ "State of HTML 2024")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">Survey</span> <span class="jser-tag">news</span></p>

State of HTML 2024 결과 공개


----
<h1 class="site-genre">읽을거리</h1>

----

## 접근성 트리 비교하는 Playwright의 Aria snapshots가 좋아보여
[azukiazusa.dev/blog/playwright-aria-snapshot/](https://azukiazusa.dev/blog/playwright-aria-snapshot/ "접근성 트리 비교하는 Playwright의 Aria snapshots가 좋아보여")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">article</span> <span class="jser-tag">test</span> <span class="jser-tag">accessibility</span></p>

Playwright의 Aria snapshots에 대해


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JSConf JP 2024 공개 자료・X 계정 링크 모음
[zenn.dev/yumemi\_inc/articles/2024-11-24-jsconf-jp-2024](https://zenn.dev/yumemi_inc/articles/2024-11-24-jsconf-jp-2024 "JSConf JP 2024 공개 자료・X 계정 링크 모음")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">slide</span></p>

JSConf JP 2024 슬라이드 모음

- [JSConf JP](https://jsconf.jp/2024/ "JSConf JP")

----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## React Scan
[react-scan.million.dev/](https://react-scan.million.dev/ "React Scan")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">tool</span></p>

태그를 넣어서 React 애플리케이션 렌더링 프로파일을 얻거나, 어째서 렌더링되었는가 보거나, 렌더링 횟수 가시화하는 도구.
Million Lint가 개발하고 있음.

- [aidenybai/react-scan: Scan for React performance issues and eliminate slow renders in your app](https://github.com/aidenybai/react-scan "aidenybai/react-scan: Scan for React performance issues and eliminate slow renders in your app")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ysk8hori/typescript-graph: A CLI to visualize the dependencies between files in the TypeScript codebase.
[github.com/ysk8hori/typescript-graph](https://github.com/ysk8hori/typescript-graph "ysk8hori/typescript-graph: A CLI to visualize the dependencies between files in the TypeScript codebase.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tool</span></p>

TypeScript 코드 의존 관계를 Mermaid로 비주얼라이즈한 도구


----
