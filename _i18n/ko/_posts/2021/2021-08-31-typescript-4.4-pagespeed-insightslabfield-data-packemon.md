---
title: "2021-08-31: TypeScript 4.4, PageSpeed Insights의 Lab / Field data, Packemon(라이브러리 용 빌드 도구)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-08-30T22:46:59.689Z
category: JSer
tags:
- node.js
- Chrome
- TypeScript
- browser
- React

---

JSer.info #555 - TypeScript 4.4 정식 릴리스.

- [Announcing TypeScript 4.4 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/)

Control Flow Analysis 개선, Index Signatures로 Symbol과 Template String를 이용 할 수 있도록.
Catch 절의 기본 타입을 `unknown` 타입으로 하는 `useUnknownInCatchVariables` 옵션 추가.
optional과 `undefined` 값을 구별하는 `exactOptionalPropertyTypes` 옵션 추가.

`useUnknownInCatchVariables`는 `strict` 옵션이 켜진 경우 자동으로 활성화 된다.
하지만 `exactOptionalPropertyTypes`는 `strict` 옵션과는 별도로 설정해야 한다.

또, ES Proposal Stage 3의[class static block](https://github.com/tc39/proposal-class-static-block#ecmascript-class-static-initialization-blocks)를 지원한다.
그 외로는 `tsc --help` 출력 방식 개선, 빌드 성능이 개선됐다.

----

[Why lab and field data can be different (and what to do about it)](https://web.dev/lab-and-field-data-differences/)에서는 [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) 등에 표시되는 "lab data"와 "field data"의 차이점을 소개하고 있다.

Lab data는 네트워크와 실행 환경을 고정한 Synthetic 모니터링 데이터라고 한다.
한편, Field data는 [Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)로 수집된 Chrome 사용자의 RUM 데이터를 기반으로 하고 있다.

두 데이터의 차이, 어떤 경우에 값에 차이가 발생하는지 등을 이야기한다.
실제 사용자 경험에 가까운 것은 Field data 이므로 우선은 Field data를 살펴볼 것, 두 데이터에 차이가 있을 경우 최적화 여지가 있음을 나타내는 것 등에 대해서 작성돼 있다.

---

[Packemon](https://packemon.dev/)은 npm에 공개하는 패키지 용 빌드 도구다.

Node.js(mjs,cjs), 브라우저(ESM、UMD) 용 빌드를 한번에 할 수 있다.

ECMAScript Modules(ESM, Node.js 12+)에서는 사용할 수 없는 Node.js API도 있고 import 시 `mjs` 파일 확장자가 필요하는 등 CommonJS와 다소 차이가 있는데 Packemon은 빌드 시에 [Babel를 사용해 ESM 용 코드를 변환](https://github.com/milesj/packemon/tree/master/packages/babel-plugin-cjs-esm-interop)하거나 ESM에서 사용할 수 없는 기능을 빌드시에 감지하여 알려준다.

- [Node.js 라이브러리 / 도구를 ESM으로 이전하다[Node.js 12+]](https://zenn.dev/azu/scraps/8251dab75562c8)(일본어)
- [Pure ESM package](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c)

그 외로는 `packemon validate`라는 패키지 메타 데이터 벨리데이션이 가능한 명령어도 제공한다.
비슷한 도구로는 [Microbundle](https://github.com/developit/microbundle)가 있으나 packemon은 패키지 공개를 보조하는 도구도 제공하므로 약간의 차이는 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Node v16.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.8.0/](https://nodejs.org/en/blog/release/v16.8.0/ "Node v16.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 16.8.0 릴리스.
`stream.Duplex.from`, `stream.Readable.isDisturbed(stream)` 추가.
`util` 모듈에 `toUSVString` 추가.

----

## Announcing TypeScript 4.4 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-4/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-4/ "Announcing TypeScript 4.4 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.4 릴리스.
Control Flow Analysis 개선, Index Signatures로 Symbol과 Template String를 이용 할 수 있도록.
Catch 절의 기본 타입을 `unknown` 타입으로 하는 `useUnknownInCatchVariables` 옵션 추가.
optional과 `undefined` 값을 구별하는 `exactOptionalPropertyTypes` 옵션 추가.
또, ES Proposal Stage 3의 class static block 지원.
`tsc --help`의 출력 방식과 빌드 성능이 개선 됐다.


----

## Chromium Blog: Chrome 94 Beta: WebCodecs, WebGPU, Scheduling, and More
[blog.chromium.org/2021/08/chrome-94-beta-webcodecs-webgpu.html](https://blog.chromium.org/2021/08/chrome-94-beta-webcodecs-webgpu.html "Chromium Blog: Chrome 94 Beta: WebCodecs, WebGPU, Scheduling, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 94 Beta 릴리스.
Origin Trial로서 HTTP status code 103 Early Hints를 시험적으로 지원.
WebCodecs, `scheduler.postTask()`, `MediaStreamTrackGenerator` / `MediaStreamTrackProcessor` 지원.
Self Profiling API 지원.
또, WebSQL이 서드 파티 컨텍스트에서 비권장 됐고, `navigator.plugins` / `navigator.mimeTypes`는 고정된 값을 반환하도록 변경됐다.


----

## Announcing SWR 1.0 – SWR
[swr.vercel.app/blog/swr-v1](https://swr.vercel.app/blog/swr-v1 "Announcing SWR 1.0 – SWR")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

데이터 가져오기 용 React Hooks 라이브러리 SWR 1.0 릴리스.
`fallback` 옵션 추가, Immutable Mode 추가, `provider` 옵션 추가, `useSWRConfig` 추가.
또, Middleware 대응, 일부 API 변경,  디폴트 `fetcher`를 지정하지 않아도 되도록 개선.


----

## Release 27.1.0 · facebook/jest
[github.com/facebook/jest/releases/tag/v27.1.0](https://github.com/facebook/jest/releases/tag/v27.1.0 "Release 27.1.0 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 27.1.0 릴리스.
`snapshotFormat` 옵션 추가, Node.js 16에서 추가된 `node:` prefix 모듈 지원.

- [Modules: CommonJS modules | Node.js v16.8.0 Documentation](https://nodejs.org/api/modules.html#modules_core_modules "Modules: CommonJS modules | Node.js v16.8.0 Documentation")

----

## mongoose/CHANGELOG.md at master · Automattic/mongoose
[github.com/Automattic/mongoose/blob/master/CHANGELOG.md#600--2021-08-24](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#600--2021-08-24 "mongoose/CHANGELOG.md at master · Automattic/mongoose")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MongoDB</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

mongoose 6.0 릴리스.
MongoDB Driver 4.0 지원, `sanitizeFilter`와 `Trusted()` 메서드 추가, `default`로 함수를 전달할 수 있도록, Document의 변경을  Proxy로 감지할 수 있다.
비호환 변경 사항으로는 `createConnection(uri)`이 thenable하지 않도록 변경됐고 같은 Query를 재실행하면 에러 발생하며 `strictQuery` 옵션이 strict로 이름 변경 됐다.
또, 기본 동작 변경과 관련하여 불필요하게 된 옵션 삭제와 타입스크립트의 타입 정의 변경이 이뤄졌다.

- [Mongoose v6.0.2: Migrating to Mongoose 6](https://mongoosejs.com/docs/migrating_to_6.html "Mongoose v6.0.2: Migrating to Mongoose 6")
- [Introducing Mongoose 6.0.0 | www.thecodebarbarian.com](https://thecodebarbarian.com/introducing-mongoose-6.html "Introducing Mongoose 6.0.0 | www.thecodebarbarian.com")

----
<h1 class="site-genre">아티클</h1>

----

## Private Network Access update: Introducing a deprecation trial - Chrome Developers
[developer.chrome.com/blog/private-network-access-update/](https://developer.chrome.com/blog/private-network-access-update/ "Private Network Access update: Introducing a deprecation trial - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Chrome에서의 non-secure한 웹사이트에서 Private Network Access를 제한하는 로드맵 공개.
Chrome 94에서 non-secure한 Public 웹사이트에서 Private Network로의 요청을 보낼 수 없게 되는 역 Origin Trial(Deprecation trials - formerly known as reverse origin trials)을 개시한다.
이어 Chrome 102에서 역 Origin Trial을 종료하고 전면 제한할 예정.


----

## Introducing Portal Windows for Electron
[blog.tandem.chat/portal-windows/](https://blog.tandem.chat/portal-windows/ "Introducing Portal Windows for Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Electron</span> <span class="jser-tag">article</span></p>

Tandem에서 만들고 사용하고 있는 Portal Windows 라이브러리 소개.
Portal Windows는 Electron 에서 별도 윈도우를 미러링할 수 있게 도와주는 라이브러리다.
별도 앱 윈도우를 리액트 컴포넌트로 렌더링하고 스크린 쉐어 등에 이용할 수 있다.

- [cryptagon/portal-windows: Render and position native windows as simply as you render and position tooltips in your React app.](https://github.com/cryptagon/portal-windows "cryptagon/portal-windows: Render and position native windows as simply as you render and position tooltips in your React app.")

----

## Why lab and field data can be different (and what to do about it)
[web.dev/lab-and-field-data-differences/](https://web.dev/lab-and-field-data-differences/ "Why lab and field data can be different (and what to do about it)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

PageSpeed Insight 등에 보고되는 합성 환경(synthetic environment) 측정 데이터인 Lab data와 실 사용자 모니터링(Real User Monitoring - RUM)인 Field data 소개.
각 데이터의 차이점, 측정 방법, 캐시 상태, AMP / SXG, BFCache 등으로 데이터가 받는 영향에 대해 다룬다.
Lab와 Field 데이터 모두 보고된 경우에는 Field data가 보다 사용자 체험에 가깝다고 한다.


----

## Modern client-side routing: the App History API
[web.dev/app-history-api/](https://web.dev/app-history-api/ "Modern client-side routing: the App History API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

Chrome 95에서 구현된 App History API(Experimental Web Platform features 플래그를 활성화하여 사용)  소개.
App History API는 SPA 구현시 다소 문제가 있는 것으로 알려진 History API를 대체하는 API 다.
`navigation` 이벤트를 통해 네비게이션 감지, `transitionWhile(promise)`로 전환중 / 성공 / 실패 표현, 네비게이션 에러 시의 롤백 등의 구체적인 예제를 소개한다.
또, History 관리, 상태 관리 방법 뿐 아니라 Form의 Submit에 의한 네비게이션 방법도 다루고 있다.

- [WICG/app-history: The app history API provides a web application-focused way of managing same-origin same-frame history entries and navigations.](https://github.com/WICG/app-history "WICG/app-history: The app history API provides a web application-focused way of managing same-origin same-frame history entries and navigations.")

----

## NAN to Node-API Migration: A Short Story - NodeSource
[nodesource.com/blog/NAN-to-Node-API-migration-a-short-story](https://nodesource.com/blog/NAN-to-Node-API-migration-a-short-story "NAN to Node-API Migration: A Short Story - NodeSource")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">C++</span> <span class="jser-tag">article</span></p>

Node.js의 native addon 개발 시 사용하는 NAN과 Node-API(N-API) 소개.
Node-API는 V8에 의존하지 않는 native addon을 개발을 위해 추가된다. NAN에서 Node-API로 전환하면서 Node-API 사용 방법을 살펴볼 수 있도록 구성된 글.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## GoogleChromeLabs/ProjectVisBug: FireBug for designers › Edit any webpage, in any state https://a.nerdy.dev/gimme-visbug
[github.com/GoogleChromeLabs/ProjectVisBug](https://github.com/GoogleChromeLabs/ProjectVisBug "GoogleChromeLabs/ProjectVisBug: FireBug for designers › Edit any webpage, in any state https://a.nerdy.dev/gimme-visbug")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">debug</span> <span class="jser-tag">Design</span></p>

디자이너 용 DevTools

- [VisBug](https://visbug.web.app/ "VisBug")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Gotta pack &#039;em all! | Packemon
[packemon.dev/](https://packemon.dev/ "Gotta pack &#039;em all! | Packemon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">bundler</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>


Zero Configuration 라이브러리 용 빌드 도구.
Node.js(mjs,cjs), 브라우저(ESM, UMD) 용 빌드를 한번에 할 수 있다.
또, 설정에 따른 package.json 수정, Babel을 사용한 ESM 용 코드 변환, mjs로 사용할 수 없는 기능을 빌드 하려는지 체크,  패키지의 메타 데이터 벨리데이션을 지원한다.

- [azu/packemon-demo: Packemon demo package](https://github.com/azu/packemon-demo "azu/packemon-demo: Packemon demo package")

----

## 5alidz/tiny-schema-validator: JSON schema validator
[github.com/5alidz/tiny-schema-validator](https://github.com/5alidz/tiny-schema-validator "5alidz/tiny-schema-validator: JSON schema validator")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Schema를 정의하여 검증 할 수 있는 JSON 스카미 빌더 라이브러리.
작성한 Schema 객체는 TypeScript의 타입으로도 사용할 수 있다.

----

## unjs/unplugin: Unified plugin system for Vite, Rollup, and Webpack
[github.com/unjs/unplugin](https://github.com/unjs/unplugin "unjs/unplugin: Unified plugin system for Vite, Rollup, and Webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">rollup</span> <span class="jser-tag">webpack</span> <span class="jser-tag">plugin</span> <span class="jser-tag">library</span></p>

Vite / Rollup / webpack의 plugin을 동일한 코드로 생성하는 라이브러리.


----
