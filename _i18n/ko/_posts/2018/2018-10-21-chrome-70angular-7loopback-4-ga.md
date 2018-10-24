---
title: "2018-10-21 JS: Chrome 70, Angular 7, LoopBack 4 GA"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-10-21T14:10:58.305Z
category: JSer
tags:
- chrome
- angular
- LoopBack


---

JSer.info #406 - Chrome 70이 릴리스됐습니다.

- [New in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/10/nic70 "New in Chrome 70  |  Web  |  Google Developers")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D70 "Chrome Platform Status")
- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
- [Deprecations and removals in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/09/chrome-70-deps-rems "Deprecations and removals in Chrome 70  |  Web  |  Google Developers")

[Desktop PWA](https://developers.google.com/web/progressive-web-apps/desktop)에서 확인할 수 있듯 Windows와 Linux에서 지원합니다. macOS는 Chrome 72에서 지원할 예정입니다.

Credential Management API에서 지문 인증, TLS 1.3을 지원하며 Web Worker에 `name` 속성(Named workers)을 추가했고 Web Components v0를 비권장화 했습니다.
또, Chrome 70 부터 `http://` 사이트의 폼 등에 데이터를 입력 시 빨간색으로 "Not Secure" 경고를 출력합니다.

- [Chromium Blog: Evolving Chrome's security indicators](https://blog.chromium.org/2018/05/evolving-chromes-security-indicators.html)

----

Angular 7이 릴리스됐습니다.

- [Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more](https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#700-2018-10-18)

TypeScript 3.1, CDK에서 Drag and Drop 지원하며 Virtual Scrolling을 대응했습니다. 또, 개발할 때만 필요한 `reflect-metadata`를 production 빌드 시 자동으로 제거하도록 변경했습니다.

----

Node.js의 API 프레임워크 [LoopBack 4](https://v4.loopback.io/) GA (General Availability)가 릴리스됐습니다.

- [StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!](https://strongloop.com/strongblog/loopback-4-ga)

핵심 코드를 TypeScript로 재작성하고 있으며 따라서 타입과 관련한 부분을 전체적으로 개선하고 있습니다.

- [strongloop/loopback-next: LoopBack makes it easy to build modern API applications that require complex integrations.](https://github.com/strongloop/loopback-next)

`lb4 openapi` 커맨드를 이용해 OpenAPI 스펙에 따른 출력에 대응할 수 있으며 LTS 정책도 함께 갱신했습니다.
 이번 LoopBack 4는 2021년 4월까지 지원할 예정입니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## New in Chrome 70  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/10/nic70](https://developers.google.com/web/updates/2018/10/nic70 "New in Chrome 70  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 70이 릴리스됐습니다.
Desktop PWA(Windows)와 Credential Management API에서 지문 인증을 지원하며 Web Worker에 `name` 속성을 추가했습니다. 도, TLS 1.3을 지원하고 Web Components v0 비권장이 이뤄졌습니다.

- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D70 "Chrome Platform Status")
- [Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more](https://blog.chromium.org/2018/09/chrome-70-beta-shape-detection-web.html "Chromium Blog: Chrome 70 beta: shape detection, web authentication, and more")
- [Deprecations and removals in Chrome 70  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/09/chrome-70-deps-rems "Deprecations and removals in Chrome 70  |  Web  |  Google Developers")

----

## Release 7.0.2 · zeit/next.js
[github.com/zeit/next.js/releases/tag/7.0.2](https://github.com/zeit/next.js/releases/tag/7.0.2 "Release 7.0.2 · zeit/next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 7.0.2가 릴리스됐습니다.
7.0.0와 7.0.1의 에러 화면에 존재하는 XSS 취약점을 수정했습니다.


----

## Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more
[blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c](https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c "Version 7 of Angular — CLI Prompts, Virtual Scroll, Drag and Drop and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 7이 릴리스됐습니다.
TypeScript 3.1, CDK에서 Drag and Drop 지원하며 Virtual Scrolling을 대응했습니다. 또, `reflect-metadata`를 production 빌드에 잘못 포함하는 경우를 방지하기 위해 자동으로 제거하도록 변경했습니다.

- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#700-2018-10-18 "angular/CHANGELOG.md at master · angular/angular")
- [Angular 7 릴리스 노트 - Angular Blog 일본어 버전 | maesblog](https://mae.chab.in/archives/60226 "Angular 7 릴리스 노트 - Angular Blog 일본어 버전 | maesblog")(일본어)

----

## StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!
[strongloop.com/strongblog/loopback-4-ga](https://strongloop.com/strongblog/loopback-4-ga "StrongLoop - Announcing LoopBack 4 GA is Now Ready for Production Use!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js API 프레임워크 LoopBack 4GA가 릴리스됐습니다.
핵심 코드를 TypeScript로 재작성했고 OpenAPI 형식으로의 출력을 대응했으며 LTS 정책도 포함해 갱신했습니다.
LoopBack 4는 2021년 4월까지 지원할 예정입니다.

- [LoopBack 4](https://v4.loopback.io/ "LoopBack 4")

----
<h1 class="site-genre">아티클</h1>

----

## Node.js에 있어 프로토타입 오염 공격이란 무엇인가 - 한가한 일기(일본어)
[jovi0608.hatenablog.com/entry/2018/10/19/083725](https://jovi0608.hatenablog.com/entry/2018/10/19/083725 "Node.js에 있어 프로토타입 오염 공격이란 무엇인가 - 한가한 일기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Prototype pollution에 관해 작성돼 있습니다.
객체를 합칠 때 등  `__proto__` 프로퍼티를 의도치 않게 다시 쓰게되는 경우에 대해 이야기합니다.


----

## Angular 4 애플리케이션을 Angular 6에 마이그레이션 | 주식회사 카부쿠(일본어)
[www.kabuku.co.jp/developers/migration-from-ng4-to-ng6](https://www.kabuku.co.jp/developers/migration-from-ng4-to-ng6 "Angular 4 애플리케이션을 Angular 6에 마이그레이션 | 주식회사 카부쿠")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

Angular 4.x에서 6.x으로 마이크레이션하는 방법에 대해 작성돼 있습니다.
Angular 4의 LTS가 2018년 9월 종료되며 이에 맞춰 6.x으로 어떻게 마이그레이션하면 될 지 이야기합니다.
마이그레이션 결과, 빌드 시간, 파일 사이즈 등에 개선 효과가 있었는지 등에 대해 다룹니다.


----

## On the Roadmap: Exact Objects by Default – Flow – Medium
[medium.com/flow-type/on-the-roadmap-exact-objects-by-default-16b72933c5cf](https://medium.com/flow-type/on-the-roadmap-exact-objects-by-default-16b72933c5cf "On the Roadmap: Exact Objects by Default – Flow – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">flowtype</span></p>

Flow 0.84.0부터 예정된 Exact Objects(`{| |}` 유형)가 기본으로 변경되는 것 대해 작성돼 있습니다. 그 외 속성을 허용하는 새로운 구문으로서 `{foo: number, ...}`를 도입, 어떻게 마이그레이션 할 수 있는지 이야기합니다.


----

## Re-ducks 패턴 : React + Redux 의 디렉터리 구성 베스트 프랙티스(일본어)
[noah.plus/blog/021/](https://noah.plus/blog/021/ "Re-ducks 패턴 : React + Redux 의 디렉터리 구성 베스트 프랙티스")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">redux</span></p>

Redux의 문맥으로 보는 Ducks 패턴과 Re-ducks 패턴에 대해 이야기합니다. 파일 디렉터리 구조를 어떤 규칙으로 구성할지, 그리고 그렇게 구성함으로서 해결할 수 있는 것들에 대해 작성돼 있습니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 마크업을 파워업하는 WAI-ARIA(일본어)
[masup9.github.io/dist23/#/](https://masup9.github.io/dist23/#/ "마크업을 파워업하는 WAI-ARIA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">slide</span></p>

WAI-AIRA의 목적, 사용법, 유즈케이스에 관해 설명하는 슬라이드입니다.
role, 스테이트, 프로퍼티를 지정했을 때 웹 브라우저와 접근성 지원 기기에 어떻게 전해지는지에 대해 정리돼 있습니다. 


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Gridsome - Build blazing fast websites with Vue.js and GraphQL
[gridsome.org/](https://gridsome.org/ "Gridsome - Build blazing fast websites with Vue.js and GraphQL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Vue와 GraphQL을 사용한 정적 사이트 도구 / 프레임워크입니다.
Gatsby.js에서 영감을 받아 개발한 프레임워크로 GraphQL 경유 레이어를 통해 데이터 소스에 접근합니다.


----

## perf-tools/timekeeper at master · artifact-project/perf-tools
[github.com/artifact-project/perf-tools/tree/master/timekeeper](https://github.com/artifact-project/perf-tools/tree/master/timekeeper "perf-tools/timekeeper at master · artifact-project/perf-tools")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

지정 구간에 대한 시간 측정 결과를 콘솔이나 퍼포먼스 타이밍(Performance Timing API)에 출력 가능한 라이브러리입니다.


----

## nico3333fr/CSP-useful: Collection of scripts, thoughts about CSP (Content Security Policy)
[github.com/nico3333fr/CSP-useful](https://github.com/nico3333fr/CSP-useful "nico3333fr/CSP-useful: Collection of scripts, thoughts about CSP (Content Security Policy)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

CSP 보고서 샘플과 노이즈가 돼 있는 CSP 보고서 등에 대해 정리하고 있는 저장소. 또, CSP의 팁이나 유즈케이스에 관해서도 작성돼 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## terkelg/zet: Set() as it should be
[github.com/terkelg/zet](https://github.com/terkelg/zet "terkelg/zet: Set() as it should be")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`Set`를 사용한 합집합, 차집합 등의 연산을 지원하는 라이브러리입니다.
`Set` 간 집합 연산을 시행하는 `Set` 서브클래스 라이브러리입니다.


----

## f/graphql.js: A Simple and Isomorphic GraphQL Client for JavaScript
[github.com/f/graphql.js](https://github.com/f/graphql.js "f/graphql.js: A Simple and Isomorphic GraphQL Client for JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

동형(Isomorphic)의 GraphQL 클라이언트 라이브러리입니다.


----

## segmentio/evergreen: 🌲 Evergreen React UI Framework by Segment
[github.com/segmentio/evergreen/](https://github.com/segmentio/evergreen/ "segmentio/evergreen: 🌲 Evergreen React UI Framework by Segment")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Segment에 의한 React UI 프레임워크입니다.


----

## Tencent/omi: Next generation web framework in 4kb JavaScript (Web Components + JSX + Proxy + Store + Path Updating)
[github.com/Tencent/omi](https://github.com/Tencent/omi "Tencent/omi: Next generation web framework in 4kb JavaScript (Web Components + JSX + Proxy + Store + Path Updating)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Web Components를 기반으로한 프레임워크입니다.
JSX 지원, ES Proxy를 사용한 변경 감지, Shadow DOM을 사용한 Scoped CSS 활용 등이 특징입니다.


----
