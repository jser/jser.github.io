---
title: "2021-09-28: Lit 2, Gatsby 4 beta, Partytown(Third-Party Script into Worker)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-09-27T14:10:06.442Z
category: JSer
tags:
- React
- WebComponents
- node.js
- Tools
- Chrome

---

JSer.info #559 - Web Components를 다루는 라이브러리인 Lit 2가 릴리스 됐다.

- [Announcing Lit 2 stable release – Lit](https://lit.dev/blog/2021-09-21-announcing-lit-2/)
- [Lit 2.0 Release Livestream - YouTube](https://www.youtube.com/watch?v=nfb779XIhsU)

Lit 2는 지금까지 별도 패키지로 존재한 LitElement 2.x와 lit-html 1.x을 통합하고 `lit`이라는 새로운 패키지를 구성했다.

class 기반의 Directives API, 비동기 Directives, Reactive Controllers가 추가됐다.
요소 전체에 작용하는 기능을 표현할 수 있는 Element expressions, 변수를 이용해 태그 명 등으로 사용할 수 있는 Static expressions 등도 추가됐다.
또, SSR을 실험적으로 지원한다.

LitElement 2.x와 lit-html 1.x에서의 업그레이드 가이드도 공개돼 있으니 참고하길 바란다.

- [Upgrade guide – Lit](https://lit.dev/docs/releases/upgrade/)

----

Gatsby 4 베타 버전이 릴리스 됐다.

- [Introducing Gatsby 4 | Gatsby](https://www.gatsbyjs.com/gatsby-4/)

[rendering mode](https://v4.gatsbyjs.com/docs/conceptual/rendering-options/)를 통해 HTML 생성을 실제 접근할 때 까지 미루는 Deferred Static Generation(DSG)와 Server Side Rendering(SSR)을 지원한다.

[Deferred Static Generation](https://v4.gatsbyjs.com/docs/reference/rendering-options/deferred-static-generation/)(DSG)는 Next.js의 [Incremental Static Regeneration](https://nextjs.org/docs/basic-features/data-fetching#incremental-static-regeneration)(ISR)와 비슷하게 첫 요청이 온 시점에 최초 빌드하여 접근 빈도가 낮은 컨텐츠를 포함하는 사이트의 배포(deploy)에 걸리는 시간을 단축하는데 목적이 있는 구조다.
DSG에서는 배포 시에 데이터 스냅샷을 만들고 요청 시에 스냅샷을 토대로 HTML 컨텐츠를 생성하여 응답한다. 때문에 DSG는 ISR와는 요청 시 처리가 다르며 서버로 부터 외부 리소스를 다시 가져오는 게 아니라 어디까지나 배포 시 생성된 스냅샷을 참조하여 빌드하도록 돼 있다.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">While DSG may look similar on the surface, what Gatsby does is that it takes a snapshot of the data at initial build time and creates lightweight render engines that are capable of building a page on demand. However, all data was already sourced at initial build time!</p>&mdash; Sid (@chatsidhartha) <a href="https://twitter.com/chatsidhartha/status/1442352346441281540?ref_src=twsrc%5Etfw">September 27, 2021</a></blockquote>

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

그 외로는 parallel query에서의 빌드 시간 개선이 포함됐다.
이와 함께 v3에서의 마이그레이션 가이드도 공개됐다.

- [Migrating from v3 to v4 | Gatsby](https://v4.gatsbyjs.com/docs/reference/release-notes/migrating-from-v3-to-v4/)

----

Partytown은 서드 파티 스크립트를 WebWorker로 동작 시켜 서드 파티 스크립트에 의한 메인 스레드 블로킹을 피할 수 있도록 고안된 라이브러리다.

- [BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉](https://github.com/BuilderIO/partytown)

WebWorker에는 DOM API 등이 없기 때문에 특별한 처리 없이 서드 파티 라이브러리르 Worker로 동작 시키면 에러가 발생한다.
따라서 라이브러리는 다음과 같은 구조로 DOM API 등을 포함하는 서드 파티 라이브러리를 Worker 내에서 실행한다.

1. Worker 내에서 DOM 조작을 [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) 한다.
2. DOM 조작을 커맨드 표현하여 동기 XHR로 통신([Worker 내에서 동기 XHR을 이용](https://developer.mozilla.org/docs/Web/API/XMLHttpRequest/Synchronous_and_Asynchronous_Requests#example_synchronous_http_request_from_a_worker)할 수 있다)
3. 이 통신을 Service Worker에서 가로채(intercept) 명령어를 가져온다.
4. 가져온 명령어를 Service Worker와 메인스레드 간 비동기적으로 주고받아 DOM 조작 결과를 가져온다.
5. DOM 조작 결과를 요청의 시발점인 Worker에 반환한다.

위와 같은 구조로 Worker 내에서 동작하는 서드 파티 라이브러리 관점에서 동기적으로 DOM을 조작하는 것으로 보이기 때문에 코드 변경 없이 동작 가능하다.

구조에 대한 자세한 내용은 다음 글에 소개돼 있으니 참고하길 바란다.

- [Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻](https://dev.to/adamdbradley/introducing-partytown-run-third-party-scripts-from-a-web-worker-2cnp)



----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing Lit 2 stable release – Lit
[lit.dev/blog/2021-09-21-announcing-lit-2/](https://lit.dev/blog/2021-09-21-announcing-lit-2/ "Announcing Lit 2 stable release – Lit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Lit 2 릴리스.
class 기반 Directives API, 비동기 Directives, Reactive Controllers 추가.
요소 전체에 작용하는 기능을 표현할 수 있는 Element expressions, 태그 명 등에 변수를 사용할 수 있도록 하는 Static expressions 추가.
또, 실험적으로 SSR을 지원한다.

----

## Node v16.10.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.10.0/](https://nodejs.org/en/blog/release/v16.10.0/ "Node v16.10.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.10.0 릴리스.
커넥션 별 최대 요청수를 제한하는 `server.maxRequestsPerSocket` 옵션 추가.
`$HOME/.node_modules`등을 탐색하지 않는 `--no-global-search-paths` 플래그 추가.


----

## Electron 15.0.0 | Electron
[www.electronjs.org/blog/electron-15-0/](https://www.electronjs.org/blog/electron-15-0/ "Electron 15.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 15.0.0 릴리스.
Electron 15부터 8 주간 별 메이저 업데이트된다.
Chromium 94, Node.js 16.5.0, V8 9.4로 각각 갱신.
`nativeWindowOpen`의 기본값을 `true`로 변경, `safeStorage` API 추가.

- [Release electron v15.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v15.0.0 "Release electron v15.0.0 · electron/electron")
- [safeStorage | Electron](https://www.electronjs.org/docs/latest/api/safe-storage/ "safeStorage | Electron")

----

## Chromium Blog: Chrome 95 Beta: Secure Payment Confirmation, WebAssembly Exception Handling and More
[blog.chromium.org/2021/09/chrome-95-beta-secure-payment.html](https://blog.chromium.org/2021/09/chrome-95-beta-secure-payment.html "Chromium Blog: Chrome 95 Beta: Secure Payment Confirmation, WebAssembly Exception Handling and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 95 beta 릴리스.
Origin Trial로 Access Handle를 File System Access API에 추가.
Performance Observer에 `droppedEntriesCount` 추가, EyeDropper API 추가, `self.reportError()` 추가, `URLPattern` 추가.
또, FTP URL 지원 종료, 숫자로 끝나는 IPv4 주소가 아닌 호스트명 지원을 폐지했다.


----

## Miniflare is now an official part of the Workers ecosystem 🎉 · cloudflare/miniflare@e1cb97f
[github.com/cloudflare/miniflare/commit/e1cb97f9891b2818f4be5715ee467668a39f7f80](https://github.com/cloudflare/miniflare/commit/e1cb97f9891b2818f4be5715ee467668a39f7f80 "Miniflare is now an official part of the Workers ecosystem 🎉 · cloudflare/miniflare@e1cb97f")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span> <span class="jser-tag">testing</span></p>

Cloudflare Workers의 simulator인 Miniflare가 Cloudflare 공식 파트로 전환됐다.


----

## es-module-shims/CHANGELOG.md at 1.0.0 · guybedford/es-module-shims
[github.com/guybedford/es-module-shims/blob/1.0.0/CHANGELOG.md](https://github.com/guybedford/es-module-shims/blob/1.0.0/CHANGELOG.md "es-module-shims/CHANGELOG.md at 1.0.0 · guybedford/es-module-shims")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

ES Module Shims 1.0.0 릴리스.
lexer가 Wasm를 사용하고 있었기 때문에 `unsafe-eval`의 CSP 설정이 필요했으나 asm.js 빌드를 사용해 기본적으로 CSP에 대응했다.
성능 면에서는 크게 달라진 점은 없지만 Safari 환경에서는 asm.js 버전이 조금 더 빠르게 측정됐다.

- [feat: make the CSP asm.js build the main entry by guybedford · Pull Request #193 · guybedford/es-module-shims](https://github.com/guybedford/es-module-shims/pull/193 "feat: make the CSP asm.js build the main entry by guybedford · Pull Request #193 · guybedford/es-module-shims")
- [feat: asm.js build by guybedford · Pull Request #86 · guybedford/es-module-lexer](https://github.com/guybedford/es-module-lexer/pull/86 "feat: asm.js build by guybedford · Pull Request #86 · guybedford/es-module-lexer")
- [content-security-policy/CSP.md at master · WebAssembly/content-security-policy](https://github.com/WebAssembly/content-security-policy/blob/master/proposals/CSP.md "content-security-policy/CSP.md at master · WebAssembly/content-security-policy")

----

## Manifest V2 support timeline - Chrome Developers
[developer.chrome.com/docs/extensions/mv3/mv2-sunset/](https://developer.chrome.com/docs/extensions/mv3/mv2-sunset/ "Manifest V2 support timeline - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span> <span class="jser-tag">news</span></p>

Chrome 확장 manifest v3 로드맵.
2022년 1월 17일 부로 manifest v2 기반의 확장은 새롭게 등록 신청할 수 없다.
2023년 1월 부로 기존 v2 확장을 갱신할 수도 없게 된다.


----

## ESLint v8.0.0-rc.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2021/09/eslint-v8.0.0-rc.0-released](https://eslint.org/blog/2021/09/eslint-v8.0.0-rc.0-released "ESLint v8.0.0-rc.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.0.0-rc.0 릴리스.

- [Migrating to v8.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/docs/8.0.0/user-guide/migrating-to-8.0.0 "Migrating to v8.0.0 - ESLint - Pluggable JavaScript linter")

----

## Stimulus 3
[world.hey.com/hotwired/stimulus-3-c438d432](https://world.hey.com/hotwired/stimulus-3-c438d432 "Stimulus 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rails</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Stimulus 3 릴리스.
패키지 명이 `stimulus`에서 `@hotwired/stimulus`로 변경됐다.
Action Parameters 지원, 기본값 지원, `debug` 옵션 추가.

- [Comparing v2.0.0...v3.0.0 · hotwired/stimulus](https://github.com/hotwired/stimulus/compare/v2.0.0...v3.0.0 "Comparing v2.0.0...v3.0.0 · hotwired/stimulus")

----

## Introducing Gatsby 4 | Gatsby
[www.gatsbyjs.com/gatsby-4/](https://www.gatsbyjs.com/gatsby-4/ "Introducing Gatsby 4 | Gatsby")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Gatsby 4 베타 릴리스.
실제 요청이 있을 때 까지 HTML 생성을 지연시키는 Deferred Static Generation(DSG) 지원, Server Side Rendering(SSR) 지원, parallel query의 빌드 시간 개선

- [Matteo Frana on Twitter: &amp;quot;@chatsidhartha Can you explain me briefly the differences between Gatsby DSG and ISR? Thank you! I&#039;m looking forward to testing Gatsby 4.&amp;quot; / Twitter](https://twitter.com/matfrana/status/1442225069158248449 "Matteo Frana on Twitter: &amp;amp;quot;@chatsidhartha Can you explain me briefly the differences between Gatsby DSG and ISR? Thank you! I&amp;#039;m looking forward to testing Gatsby 4.&amp;amp;quot; / Twitter")
- [Run Gatsby 4 with DSG and SSR on Netlify today | Netlify](https://www.netlify.com/blog/2021/09/16/run-gatsby-4-with-dsg-and-ssr-on-netlify-today/ "Run Gatsby 4 with DSG and SSR on Netlify today | Netlify")

----
<h1 class="site-genre">아티클</h1>

----

## Blazor Developers Can Now Create Custom Elements, Render Components from JavaScript -- Visual Studio Magazine
[visualstudiomagazine.com/articles/2021/09/16/aspnet-core-updates.aspx](https://visualstudiomagazine.com/articles/2021/09/16/aspnet-core-updates.aspx "Blazor Developers Can Now Create Custom Elements, Render Components from JavaScript -- Visual Studio Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">.net</span> <span class="jser-tag">C#</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span></p>

.NET 6 RC1에서 Blazor가 Custom Element를 지원한다. 또, Blazor 컴포넌트를 Custom Element로도 사용할 수 있다.

- [Announcing .NET 6 Release Candidate 1 - .NET Blog](https://devblogs.microsoft.com/dotnet/announcing-net-6-release-candidate-1/ "Announcing .NET 6 Release Candidate 1 - .NET Blog")
- [AspLabs/src/BlazorCustomElements at main · aspnet/AspLabs](https://github.com/aspnet/AspLabs/tree/main/src/BlazorCustomElements "AspLabs/src/BlazorCustomElements at main · aspnet/AspLabs")

----

## Fullstack app with TypeScript, Next.js, Prisma &amp; GraphQL
[www.prisma.io/blog/fullstack-nextjs-graphql-prisma-oklidw1rhw](https://www.prisma.io/blog/fullstack-nextjs-graphql-prisma-oklidw1rhw "Fullstack app with TypeScript, Next.js, Prisma &amp; GraphQL")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span> <span class="jser-tag">prisma</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">GraphQL</span></p>

Next.js / Prisma / GraphQL 기반 애플리케이션 개발을 테마로 한 튜토리얼 글.


----

## What&#039;s new in React 18? | Yagmur Cetin Tas
[yagmurcetintas.com/journal/whats-new-in-react-18](https://yagmurcetintas.com/journal/whats-new-in-react-18 "What&#039;s new in React 18? | Yagmur Cetin Tas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 18에서 예정돼 있는 변경 사항의 개요를 정리한 글.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Get Your Head Straight - Speaker Deck
[speakerdeck.com/csswizardry/get-your-head-straight](https://speakerdeck.com/csswizardry/get-your-head-straight "Get Your Head Straight - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">slide</span> <span class="jser-tag">CSS</span></p>


`<head>`내 style이나 script를 작성할 때 발생할 수 있는 다양한 성능 문제와 해결 방법을 제시하고 이와 관련된 성능 문제를 쉽게 발견할 수 있도록 `<head>` 내용을 표시해 주는 ct.css를 소개한다.
ct.css는 `<head>` 내 작성돼 있는 `<script>`나 `<style>`이 3rd party 인지 또, 블록킹 하고 있진 않은지 알아보기 쉽게 표시해준다.

- [🧠 ct.css – Let’s take a look inside your &lt;head&gt;](https://csswizardry.com/ct/ "🧠 ct.css – Let’s take a look inside your &amp;lt;head&amp;gt;")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## vite/packages/plugin-react at main · vitejs/vite
[github.com/vitejs/vite/tree/main/packages/plugin-react](https://github.com/vitejs/vite/tree/main/packages/plugin-react "vite/packages/plugin-react at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">vite</span> <span class="jser-tag">plugin</span></p>

Vite의 React Plugin.
`@vitejs/plugin-react-refresh`를 대체하는 플러그인.

----

## BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉
[github.com/BuilderIO/partytown](https://github.com/BuilderIO/partytown "BuilderIO/partytown: Relocate resource intensive third-party scripts off of the main thread and into a web worker. 🎉")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

서드 파티 스크립트를 Worker 내에서 실행하여 메인스레드의 블록킹을 방지하는 라이브러리.
Worker 내에서 DOM 조작을 Proxy 하고 동기 XHR로 통신, Service Worker에서 이 통신을 가로채 메인스레드와 비동기로 작업을 수행하고 그 결과를 다시 Worker에 반환하는 방식.

- [Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻](https://dev.to/adamdbradley/introducing-partytown-run-third-party-scripts-from-a-web-worker-2cnp "Introducing Partytown 🎉: Run Third-Party Scripts From a Web Worker - DEV Community 👩‍💻👨‍💻")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## gvergnaud/ts-pattern: 🎨 The exhaustive Pattern Matching library for TypeScript, with smart type inference.
[github.com/gvergnaud/ts-pattern](https://github.com/gvergnaud/ts-pattern "gvergnaud/ts-pattern: 🎨 The exhaustive Pattern Matching library for TypeScript, with smart type inference.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScript 친화적으로 고안된 패턴 매칭 라이브러리.


----

## cesanta/elk: A low footprint JavaScript engine for embedded systems
[github.com/cesanta/elk](https://github.com/cesanta/elk "cesanta/elk: A low footprint JavaScript engine for embedded systems")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

임베디드 용 작은 크기의 JavaScript 엔진


----
