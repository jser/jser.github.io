---
title: "2021-03-09: Gatsby 3, Electron 12, 브라우저의 라이프 사이클 변화"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-03-08T14:53:58.520Z
category: JSer
tags:
- React
- serverless
- aws
- GraphQL
- jQuery

---

JSer.info #530 - Gatsby v3 릴리스.

- [Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby](https://www.gatsbyjs.com/blog/gatsby-v3/)
- [Gatsby v3.0 (March 2021 #1)](https://www.gatsbyjs.com/docs/reference/release-notes/v3.0/)

로컬에서 실제 접근한 페이지만 빌드하는 등 전체를 재구축하지 않고 빌드하는 방식을 기본으로 적용. 따라서 필요한 페이지만 빌드하기 때문에 개발 시의 빌드 대기 시간이 줄었다.

비호환 변경으로는 Node.js 12 미만 지원 종료, React 17 / webpack 5 / ESLint 7으로 갱신, 전역 `graphql` 대신 import 하여 사용하도록 변경, API 변경이 있다.

마이그레이션 방법은 다음 문서를 통해 친절히 설명하고 있다.

- [Migrating from v2 to v3 | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/migrating-from-v2-to-v3/)

---

Electron 12.0.0리 릴리스 됐다.

- [Electron 12.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-12-0)


Chromium 89, V8 8.9, Node.js 14.16(12.x에서)으로 갱신.
`exposeInMainWorld`가 객체 이외의 형식을 지원, `webFrameMain` API 추가.

Electron 12.0.0에서는 `contextIsolation`와 `worldSafeExecuteJavaScript`가 기본적으로 `true`로 변경됐다.
[Context Isolation](https://www.electronjs.org/docs/tutorial/context-isolation)는 `preload` 스크립트와 `webContents` 스크립트의 실행 문맥을 분리하는 것으로 XSS 등의 피해 범위를 축소하는 구조다.

- [Electron: Context Isolation의 격리 기능을 이용한 임의 코드 실행 / Electron: Abusing the lack of context isolation - CureCon(ja) - Speaker Deck](https://speakerdeck.com/masatokinugawa/electron-abusing-the-lack-of-context-isolation-curecon-ja)(일본어)
- [Electron(v.12.0.0 현재)의 IPC 통신 입문 - 보다 안전한 방법으로의 변화 - Qiita](https://qiita.com/hibara/items/c59fb6924610fc22a9db)(일본어)

또, [단계적으로 폐지되고 있는 `remote` 모듈](https://github.com/electron/electron/issues/21408)이 비권장 됐고 [@electron/remote](https://github.com/electron/remote) 라는 외부 모듈로 이전 중이다.

- [electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.](https://github.com/electron/remote)

---

브라우저 라이프 사이클이 변화하고 있어 관련하여 몇 가지 소식을 정리해 소개.

현재 6주 마다 릴리스하고 있는 크롬이지만 2021년 Q3 즉, 크롬 94부터 릴리스 사이클을 4주로 단축한다고 발표했다.

- [Chromium Blog: Speeding up Chrome's release cycle](https://blog.chromium.org/2021/03/speeding-up-release-cycle.html)
- [Chromium Dash](https://chromiumdash.appspot.com/schedule)

Microsoft Edge Legacy의 폐지 일정이 공개됐다.
Microsoft Edge Legacy는 2021년 3월 9일로 지원 종료된다. 또, 2021년 4월 13일에 릴리스되는 보안 업데이트를 통해 삭제되고 동시에 새로운 크로미움 기반의 MS Edge가 설치된다(대체됨).

- [New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224)

Internet Explorer(IE) 폐지는 Edge와는 다른 라이프 사이클을 갖기 때문에 아직 남았지만,
IE에서 접속했을 경우 사이트의 호환 여부에 따라서 MSEdge로 리다이렉트하는 등의 이전이 이뤄지고 있다.

- [Moving users to Microsoft Edge from Internet Explorer - Microsoft Edge Development | Microsoft Docs](https://docs.microsoft.com/en-us/microsoft-edge/web-platform/ie-to-microsoft-edge-redirection)

이 [NeedEdge 호환 목록](https://edge.microsoft.com/neededge/v1)에 작성된 사이트를 IE로 접속하면 MS Edge를 사용할 것을 가이드하는 리다이렉트 팝업이 제공된다.
호환 목록에 [추가돼 있는 사이트](https://github.com/teppeis/history-of-ie-incompatible-sites-list/commits/master)는 점차 늘어나고 있다.
이와 별개로 IE 지원 종료를 선언한 사이트는 다음 문서에 정리돼 있으니 참고한다.

- [IE11 지원 종료 역사 - Google 문서](https://docs.google.com/document/d/1XP58gVMyp_UCP4FFsf5ATpvRVwqi7v_EpEF3sl_Sobk/edit)(일본어)

----

<h1 class="site-genre">헤드라인</h1>

----

## Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby
[www.gatsbyjs.com/blog/gatsby-v3/](https://www.gatsbyjs.com/blog/gatsby-v3/ "Gatsby v3 Incremental Builds in OSS, new Gatsby Image, and more | Gatsby")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">ReleaseNote</span></p>

Gatsby 3.0 릴리스.
비호환 변경으로는 Node.js 12 미만 지원 종료, webpack 5 / ESLint 7으로 갱신, 전역 `graphql` 대신 import 하여 사용하도록 변경, API 변경 등이 있다.
로컬 환경에서 전체를 재구축하지 않고 실제 접속한 페이지만 빌드하는 방식이 적용됐다.

- [Migrating from v2 to v3 | Gatsby](https://www.gatsbyjs.com/docs/reference/release-notes/migrating-from-v2-to-v3/ "Migrating from v2 to v3 | Gatsby")

----

## jQuery 3.6.0 Released! | Official jQuery Blog
[blog.jquery.com/2021/03/02/jquery-3-6-0-released/](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/ "jQuery 3.6.0 Released! | Official jQuery Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">JSON</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.6.0 릴리스.
JSONP 요청 시 에러 응답으로 JSON을 반환했을 경우의 동작 변경.
`.focus()`의 버그 수정.


----

## Deno 1.8 Release Notes
[deno.land/posts/v1.8](https://deno.land/posts/v1.8 "Deno 1.8 Release Notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.8.0 릴리스.
WebGPU API를 실험적으로 지원.
ICU를 대응하는 ECMA i18n API인 `Intl` 객체 등 지원, `DENO_AUTH_TOKENS`로 모듈을 가져올 때 인증 토큰 지원, Exit sanitier를 `Deno.test`에 추가, `deno fmt`가 JSON을 지원, TypeScript 4.2으로 갱신.
Import Map, `Deno.permissions`, `Deno.link`, `Deno.symlink` API가 각각 Stable API로 변경됐다.


----

## New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community
[techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224](https://techcommunity.microsoft.com/t5/microsoft-365-blog/new-microsoft-edge-to-replace-microsoft-edge-legacy-with-april-s/ba-p/2114224 "New Microsoft Edge to replace Microsoft Edge Legacy with April’s Windows 10 Update Tuesday release - Microsoft Tech Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">news</span></p>

Microsoft Edge Legacy는 2021년 3월 9일 지원 종료.
이어 2021년 4월 13에 Legacy를 삭제함과 동시에 새로운 크로미움 기반 MS Edge를 설치하는 보안 업데이트가 실행될 예정


----

## Chromium Blog: Speeding up Chrome&#039;s release cycle
[blog.chromium.org/2021/03/speeding-up-release-cycle.html](https://blog.chromium.org/2021/03/speeding-up-release-cycle.html "Chromium Blog: Speeding up Chrome&#039;s release cycle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">news</span></p>

Chrome의 릴리스 주기를 6 주에서 4주로 단축.


----

## Announcing the New TypeScript Handbook | TypeScript
[devblogs.microsoft.com/typescript/announcing-the-new-typescript-handbook/](https://devblogs.microsoft.com/typescript/announcing-the-new-typescript-handbook/ "Announcing the New TypeScript Handbook | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span></p>

TypeScript Handbook 개편.

- [TypeScript: The starting point for learning TypeScript](https://www.typescriptlang.org/docs/ "TypeScript: The starting point for learning TypeScript")

----

## Electron 12.0.0 | Electron Blog
[www.electronjs.org/blog/electron-12-0](https://www.electronjs.org/blog/electron-12-0 "Electron 12.0.0 | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 12.0.0 릴리스.
Chromium 89, V8 8.9, Node.js 14.16으로 갱신.

`exposeInMainWorld`가 객체 이외의 형식을 지원, `webFrameMain` API 추가.

Electron 12.0.0에서는 `contextIsolation`와 `worldSafeExecuteJavaScript`가 기본적으로 `true`로 변경, `remote` 모듈이 비권장 됐고 `@electron/remote` 라는 외부 모듈로 이전 중이다.

- [electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.](https://github.com/electron/remote "electron/remote: Bridge JavaScript objects from the main process to the renderer process in Electron.")

----

## Release v6.0.0 · pixijs/pixi.js
[github.com/pixijs/pixi.js/releases/tag/v6.0.0](https://github.com/pixijs/pixi.js/releases/tag/v6.0.0 "Release v6.0.0 · pixijs/pixi.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">canvas</span> <span class="jser-tag">WebGL</span></p>

pixi.js 6.0.0 릴리스.
TypeScript의 타입 개선, Deprecated 됐던 API 삭제, `alpha` 옵션의 기본값을 `true`로 변경, `FAIL_IF_MAJOR_PERFORMANCE_CAVEAT`의 기본 값을 `false`로 변경


----

## Google Developers Blog: Announcing Flutter 2
[developers.googleblog.com/2021/03/announcing-flutter-2.html](https://developers.googleblog.com/2021/03/announcing-flutter-2.html "Google Developers Blog: Announcing Flutter 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">ReleaseNote</span></p>

Flutter 2 릴리스.
Web 및 데스크탑 안정적(Stable) 지원, Dart 2.12 지원.
iOS에서 Autocomplete와 ScaffoldMessenger 지원 등.

- [Dart 2.12](https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87 "Dart 2.12")
- [Flutter web support hits the stable milestone | Flutter](https://medium.com/flutter/flutter-web-support-hits-the-stable-milestone-d6b84e83b425 "Flutter web support hits the stable milestone | Flutter")
- [What’s New in Flutter 2. by Chris Sells | Mar, 2021 | Medium | Flutter | Flutter](https://medium.com/flutter/whats-new-in-flutter-2-0-fe8e95ecc65 "What’s New in Flutter 2. by Chris Sells | Mar, 2021 | Medium | Flutter | Flutter")

----
<h1 class="site-genre">아티클</h1>

----

## Mini apps - web.dev
[web.dev/mini-apps/](https://web.dev/mini-apps/ "Mini apps - web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span></p>

Mini apps의 에코시스템에 대한 글


----

## Hiding Content Responsibly | Kitty Giraudel
[kittygiraudel.com/2021/02/17/hiding-content-responsibly/](https://kittygiraudel.com/2021/02/17/hiding-content-responsibly/ "Hiding Content Responsibly | Kitty Giraudel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

컨텐츠를 숨김 처리하는 CSS와 WAI-ARIA 속성이 각각 접근성 측면에서 어떻게 동작하는지 정리.
데이터, 비주얼, 레이아웃, 시멘틱스, 컨텐츠, 키보드, 포인터, 스타일 등의 상태 등을 소개.

- [removal techniques and implications](https://codepen.io/vincent-valentin/full/JjGmxzV "removal techniques and implications")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## serverless-stack/serverless-stack: Serverless Stack (SST) is a framework that makes it easy to build serverless apps.
[github.com/serverless-stack/serverless-stack](https://github.com/serverless-stack/serverless-stack "serverless-stack/serverless-stack: Serverless Stack (SST) is a framework that makes it easy to build serverless apps.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">serverless</span> <span class="jser-tag">aws</span></p>

AWS CDK를 사용한 serverless 관리 및 개발 도구.
Lambda 개발, 디플로이, 빌드나 Lint 설정. 각종 AWS 스택과의 연동을 포함한다.


----

## NightlyCommit/twing: First-class Twig engine for Node.js
[github.com/NightlyCommit/twing](https://github.com/NightlyCommit/twing "NightlyCommit/twing: First-class Twig engine for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">template</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

템플릿 엔진인 Twig의 자바스크립트 구현 라이브러리.


----

## JakePartusch/serverlessui: A command-line utility for deploying serverless applications to AWS. Complete with custom domains, deploy previews, TypeScript support, and more.
[github.com/JakePartusch/serverlessui](https://github.com/JakePartusch/serverlessui "JakePartusch/serverlessui: A command-line utility for deploying serverless applications to AWS. Complete with custom domains, deploy previews, TypeScript support, and more.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">serverless</span> <span class="jser-tag">Tools</span></p>

AWS에서 serverless 애플리케이션을 디플로이 하기 위한 도구.
CDK를 사용해 정적 사이트와 lambda 등의 디플로이을 일괄 처리.


----

## nanojsx/nano: 🎯 SSR first, lightweight 1kB JSX library.
[github.com/nanojsx/nano](https://github.com/nanojsx/nano "nanojsx/nano: 🎯 SSR first, lightweight 1kB JSX library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

JSX를 사용한 SSR first한 UI 라이브러리.
지정한 컴포넌트만을 Hydrate, Lazy Hydrate 할 수 있으며 Router나 Head 관련 컴포넌트를 내장으로 제공한다.
React 스러운 라이프 사이클 메서드와 Hooks 구조도 제공.

- [Nano JSX • Lightweight 1kB JSX library](https://nanojsx.github.io/ "Nano JSX • Lightweight 1kB JSX library")

----
