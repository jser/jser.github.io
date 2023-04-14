---
title: "2023-02-15: Lighthouse 10, core-js와 오픈소스 재정적 지원, WebContainers"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2023-02-15T04:33:33.465Z
category: JSer
tags:
- performance
- TypeScript
- browser
- Tools
- node.js

---

JSer.info #631 - LightHouse 10가 출시되었다.

- [What's new in Lighthouse 10 - Chrome Developers](https://developer.chrome.com/blog/lighthouse-10-0/)
- [Release v10.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v10.0.0)

LightHouse 10 에는, 스코어에서 TTI가 삭제되었으며, CLS로 스코어에 이동되었다.
또, Audit으로 BFCache 검증, 붙여넣기 금지 검증이 추가되었다.
그 외로는, LightHouse JSON 출력 구조 변경이 있다.

관련 정보로, [CrUX History API](https://developer.chrome.com/docs/crux/history-api/) Chrome User Experience Report (CrUX) 이력 데이터를 취득하는 API가 출시 되었다.
특정 페이지 Web Vitals 값 데이터를 일주일 단위로 얻을 수 있다.

- [Introducing historical web performance data via the CrUX History API - Chrome Developers](https://developer.chrome.com/en/blog/chrome-ux-report-history-api/)

---

core-js 3.28.0가 출시되었다.

- [Release 3.28.0 - 2023.02.14 · zloirock/core-js](https://github.com/zloirock/core-js/releases/tag/v3.28.0)

core-js 3.28.0은, [2023-01 TC 39 Meetings 결과](https://ecmascript-daily.github.io/ecmascript/2023/02/03/ecmascript-proposal-update)를 반영한 변경이 포함되었다.

- Stage4가 된 Change Array by copy proposal를 Stable으로 이동
- Stage3 `JSON.parse` source text access, `ArrayBuffer.prototype.transfer`, Explicit Resource Management 추가
- Stage 2 Symbol Predicates 구현
- Stage 1 `Number.range`를 `Iterator.range`로 변경

또한, core-js 역사, 재정적 지원 모집이나 앞으로의 방침에 대한 글도 공개되었다.

- [core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub](https://github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md)

오픈 소스 관리와 재정적 이야기에 대해서는 [Working in Public](https://press.stripe.com/working-in-public)에 잘 정리되어 있다.
Babel이나 core-js 같이 소수 관리자와 많은 유저 비율이 크게 어긋나는 프로젝트는 스타디움모델 형식이라 분류되어 있다.

또 소프트웨어는 거의 무료 배포하고 있어서, 이용자 수는 계속 지속하지만, 관리자에게 걸리는 부하는 커지는 문제가 있다.
(오픈소스) 소프트웨어를 구매하는 동기는 적어지는 반면, 그 사회적가치가 극적으로 상승하고 있어, 많은 사람이나 사이트는 오픈소스 소프트웨어에 의존하고 있다.（[모던한 웹 애플리케이션 코드 97%는 npm에서 나오고 있다](https://medium.com/npm-inc/this-year-in-javascript-2018-in-review-and-npms-predictions-for-2019-3a3d7e5298ef#49d6) 이런 이야기도 있다）.
이에, 오픈소스는 관리가 필요한 공공 인프라의 일종이라는 말도 있습니다.

오픈소스에 재정적 지원하는 개인이나 기업이 늘어나고 있다.
한편 소프트웨어 의존관계는 방대해지고 있기에, 어디에 어떻게 지원해야 하는가 알기어렵다는 문제도 지적된다.

📝 의존관계에 따라 자동적으로 분배하는 서비스도 있다

- [thanks.dev – open source funding platform](https://thanks.dev/home)
- [StackAid - Fund all your open source dependencies](https://www.stackaid.us/)

또 특정 사람에게 Sponsor는 "기부" 개념과 혼동되지만, 명확하게 말하면 창작자의 장래에 대한 기대, 관심에 이어지므로, 구독에 가깝다 써있다.
최근에는 특정 프로젝트에 대해 Sponsor가 아닌, 특정 사람에 대한 Sponsor도 문화 변경도 일어난다는 이야기도 소개되어있다.

（이는, 프로젝트가 성장단계에 들어가면 코드를 쓰는 개발자 외에도, moderator나 문서화 등을 중심으로 하는 사람의 중요도가 높아졌다는 이야기와도 관련된다.）

이 책의 출간 이후라 포함되어있지 않지만, Babel에도 같은 이야기가 있었기에, 흥미롭다면 읽기 권장.

- [Babel is used by millions, so why are we running out of money? · Babel](https://babeljs.io/blog/2021/05/10/funding-update)

이 사이트 [💚JSer.info Sponsor](https://github.com/sponsors/azu) 등 Sponsors로 재정적 지원을 할 수 있다.

---

Node.js을 Web 브라우저 상에 동작시킨 후에, Playground 등에 이용할 수 있는 WebContainers API와 패키지가 공개되었다.
[Svelte Tutorial](https://learn.svelte.dev/tutorial/welcome-to-svelte) 등에서 이용하고 있는 사례도 적혀있다.

- [WebContainers - Dev environments. In your web app. | WebContainers](https://webcontainers.io/)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Notes for Safari Technology Preview 163 | WebKit
[webkit.org/blog/13839/release-notes-for-safari-technology-preview-163/](https://webkit.org/blog/13839/release-notes-for-safari-technology-preview-163/ "Release Notes for Safari Technology Preview 163 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 163 출시.
CSS Grid의 Masonry layout를 기본 유효화, `StorageManager.estimate()` 지원, Web Crypto API가 Ed25519 지원.
비표준한 `HTMLHeadElement.profile`이나 `HTMLFrameElement.location` 등 삭제.


----

## Release v3.2.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.2.0](https://github.com/nuxt/nuxt/releases/tag/v3.2.0 "Release v3.2.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Nuxt.js v3.2.0 출시.
Nuxt DevTools 추가, `useFetch` 리퀘스트에 자동적으로 Cookie 붙을 수 있게.
서버에서 코드에서 client-only component 빼오는 `treeshakeClientOnly`를 기본값으로 `true`로 등의 변경


----

## What&#039;s new in Lighthouse 10 - Chrome Developers
[developer.chrome.com/blog/lighthouse-10-0/](https://developer.chrome.com/blog/lighthouse-10-0/ "What&#039;s new in Lighthouse 10 - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 10 출시.
스코어에서  TTI 삭제, CLS로 스코어 이동.
Audit으로 BFCache 검증, 붙여넣기 금지 검증 추가.
Lighthouse 결과를 보여주는 JSON 구조 변경 등

- [Release v10.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v10.0.0 "Release v10.0.0 · GoogleChrome/lighthouse")

----

## Electron 23.0.0 | Electron
[www.electronjs.org/blog/electron-23-0](https://www.electronjs.org/blog/electron-23-0 "Electron 23.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 23.0.0 출시.
Chromium 110, Node.js 18.12.1, V8 11.0 으로 업데이트.
Windows 7/8/8.1 지원 종료, `scroll-touch-*` 이벤트 삭제.
추가 기능으로 WebUSB API 지원


----

## Release v1 Because I finally got around to it · jquense/yup
[github.com/jquense/yup/releases/tag/v1.0.0](https://github.com/jquense/yup/releases/tag/v1.0.0 "Release v1 Because I finally got around to it · jquense/yup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

스키마를 만들어 검증할 수 있는 yup 1.0.0. 출시.
`tuple` 추가, bundle한 파일을 배포할 수 있도록, `when` API 변경, email 검증을 WHATWG 정의과 같도록 변경.
`cast`에 `ignore-optionality` 옵션 추가, 자료형 처리 성능 개선과 `Objectschema` 클래스는 추가 등

- [How do I migrate to v1 · Issue #1906 · jquense/yup](https://github.com/jquense/yup/issues/1906 "How do I migrate to v1 · Issue #1906 · jquense/yup")

----

## Release DOMPurify 3.0.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/3.0.0](https://github.com/cure53/DOMPurify/releases/tag/3.0.0 "Release DOMPurify 3.0.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

DOMpurify 3.0.0 출시.
IE 서포트 종료, `ALLOW_SELF_CLOSE_IN_ATTRP` 옵션 추가 등


----

## Release 3.28.0 - 2023.02.14 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.28.0](https://github.com/zloirock/core-js/releases/tag/v3.28.0 "Release 3.28.0 - 2023.02.14 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.28.0 출시.
Stage4가 된 Change Array by copy proposal를 Stable로 이동.
Stage3 `JSON.parse` source text access, `ArrayBuffer.prototype.transfer`, Explicit Resource Management를 추가.
Stage2 Symbol Predicates 구현, Stage 1 `Number.range`를 `Iterator.range`으로 변경 등


----

## Nextra 2 – Next.js Static Site Generator – The Guild
[the-guild.dev/blog/nextra-2](https://the-guild.dev/blog/nextra-2 "Nextra 2 – Next.js Static Site Generator – The Guild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 기반 정적 사이트 제네레이터 Nextra 2 출시.
MDX2 지원, Markdown 임포트, Next 13 대응, 원격으로 Markdown 파일을 읽어 렌더링할 수 있도록, FlexSearch를 사용한 전문 검색 지원 등


----
<h1 class="site-genre">읽을거리</h1>

----

## Bringing Javascript to WebAssembly for Shopify Functions (2023)
[shopify.engineering/javascript-in-webassembly-for-shopify-functions](https://shopify.engineering/javascript-in-webassembly-for-shopify-functions "Bringing Javascript to WebAssembly for Shopify Functions (2023)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript를 Wasm으로 실행하는 구조에 대해.
QuickJS를 사용해 JavaScript를 ByteCode로 한 `script.wasm`를 작성해, `QuickJS.wasm`와 동적으로 링크해서 대부분을 공유하고 있다.

Shopify Function에서 이용가능하지만, 비동기처리 제한이나 5ms 미만 실행 제한이 있다. 현재는 Rust로 작성한 Wasm보다 3배정도 느리지만, 앞으로 SpiderMonkey 이용이나 JIT에 연계해서 나아갈 것.

- [Shopify/javy: JS to WebAssembly toolchain](https://github.com/Shopify/javy "Shopify/javy: JS to WebAssembly toolchain")

----

## Speculation Rules API으로 프레렌더링 위한 매트릭스 설계
[nhiroki.jp/2023/02/13/metrics-for-prerendering](https://nhiroki.jp/2023/02/13/metrics-for-prerendering "Speculation Rules API Speculation Rules API으로 프레렌더링 위한 매트릭스 설계")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Speculation Rules API의 PreRendering에 대하여.
Prerender한 경우 `navigationStart`는 사전실행 타이밍이기 되기에,  `activationStart` 매트릭스가 추가된 점.
또, Predender가 실제 이용되는가 확인하는 방법에 대하여

----

## Improved type safety in Storybook 7
[storybook.js.org/blog/improved-type-safety-in-storybook-7/](https://storybook.js.org/blog/improved-type-safety-in-storybook-7/ "Improved type safety in Storybook 7")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Storybook 7의 TypeScript 자료형에 대해.
`StoryObj` 타입이나 `satisfies` 연산자를 사용해 export 하는 컴포넌트 정의에 자료형을 붙이는 글


----

## Understanding App Directory Architecture In Next.js — Smashing Magazine
[www.smashingmagazine.com/2023/02/understanding-app-directory-architecture-next-js/](https://www.smashingmagazine.com/2023/02/understanding-app-directory-architecture-next-js/ "Understanding App Directory Architecture In Next.js — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.js에서 `app` 폴더에 대한 글


----

## A Historical Reference of React Criticism—zachleat.com
[www.zachleat.com/web/react-criticism/](https://www.zachleat.com/web/react-criticism/ "A Historical Reference of React Criticism—zachleat.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">history</span></p>

React 비판하는 역사에 대해


----

## core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub
[github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md](https://github.com/zloirock/core-js/blob/master/docs/2023-02-14-so-whats-next.md "core-js/2023-02-14-so-whats-next.md at master · zloirock/core-js · GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">article</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">opinion</span></p>

core-js 역사, 재정적 문제, 로드맵 등.
또한, 많은 웹사이트가 여러 버전의 `core-js`를 같은 페이지에서 읽고 있는 패키지 의존관계 문제에 대해서


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## WebContainers - Dev environments. In your web app. | WebContainers
[webcontainers.io/](https://webcontainers.io/ "WebContainers - Dev environments. In your web app. | WebContainers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span></p>

Node.js를 Web 브라우저 상에서 동작시키고, Playground 등으로 이용할 수 있는 WebContainers API와 패키지 공개되었다.


----

## Introducing historical web performance data via the CrUX History API - Chrome Developers
[developer.chrome.com/en/blog/chrome-ux-report-history-api/](https://developer.chrome.com/en/blog/chrome-ux-report-history-api/ "Introducing historical web performance data via the CrUX History API - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

CrUX History API로 1주일 간격 데이터를 6개월 분 확인할 수 있게 되었다.
WebVitals의 데이터를 각 페이지 레벨에서 얻을 수 있도록 되었다


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## upgradejs/depngn: A CLI tool to find out if your dependencies support a given version of node.
[github.com/upgradejs/depngn](https://github.com/upgradejs/depngn "upgradejs/depngn: A CLI tool to find out if your dependencies support a given version of node.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

설치된 의존관계 `engines` 필드를 보고, 지정한 Node.js 버전이 조건에 맞는지를 한 눈에 볼 수 있는 도구


----

## slashd-analytics/run: Run user-provided code in a Web Worker
[github.com/slashd-analytics/run](https://github.com/slashd-analytics/run "slashd-analytics/run: Run user-provided code in a Web Worker")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span></p>

Web Worker의 일종으로 Sandbox로 사용하거나, 임의의 JS코드를 실행할 수 있도록 하는 라이브러리


----
<h1 class="site-genre">도서</h1>

----

## Design Patterns in TypeScript
[refactoring.guru/design-patterns/typescript](https://refactoring.guru/design-patterns/typescript "Design Patterns in TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span> <span class="jser-tag">book</span></p>

TypeScript에서의 디자인 패턴에 대해 정리


----
