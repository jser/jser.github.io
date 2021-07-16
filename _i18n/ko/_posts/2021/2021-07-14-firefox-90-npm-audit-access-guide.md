---
title: "2021-07-14: Firefox 90, npm audit 문제, Access Guide"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-07-14T03:24:13.966Z
category: JSer
tags:
- node.js
- Next.js
- npm
- TypeScript
- Tools

---

JSer.info #548 - Firefox 90 릴리스.

- [Firefox 90.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/90.0/releasenotes/)
- [Firefox 90 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/90)

Firefox 90에서는 ECMAScript Proposal Stage 4의 Private class fields를 기본적으로 지원하고 Stage 3 String/Array의 `at()`를 지원한다. FTP 지원을 삭제했고 WheelEvent의 호환성을 개선했다.

또, Chrome에 구현 돼 있던 [Fetch metadata request headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#fetch_metadata_request_headers)도 구현됐다.
`Sec-Fetch-Site`, `Sec-Fetch-Mode`, `Sec-Fetch-User`, `Sec-Fetch-Dest` 요청 헤더가 각 요청에 추가돼 서버에서 요청을 검사 할 때 이용할 수 있다.

- [Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/)
- [Protect your resources from web attacks with Fetch Metadata](https://web.dev/fetch-metadata/)

Fetch metadata request headers는 Safari를 비롯한 IE 이외의 브라우저에도 구현돼 있다.

---

[npm audit: Broken by Design — Overreacted](https://overreacted.io/npm-audit-broken-by-design/)에서는 [create-react-app](https://github.com/facebook/create-react-app/issues/11174)을 예로 `npm audit`의 취약성 보고 방식에 문제가 있다고 전한다.

보고되는 취약성 대부분이 ReDOS(Regular expression Denial of Service)이며(대부분 문제가 되지 않는), `devDependencies`로 다루는 도구에 대한 보고는 오탐지(false positive)에 가까운 경우가 많고, 에코시스템으로서 대응이 어렵게 돼 있는 부분에 대해 우려를 나타내고 있다.

GitHub에서 공개한 GitHub’s Advisory Database 데이터를 보더라도 2021년에는 CWE-400인 DoS가 가장 많은 보고가 이뤄져 있고, ReDOS 보고가 증가하고 있다는 사실을 알 수 있다.

- [Our shared common weaknesses | GitHub Security Lab](https://securitylab.github.com/research/CWE-Overview/)

도구가 과잉 보고하는 문제 속에서 실제 중요한 문제가 뒤섞여 무시될 가능성에 대한 우려, 이 문제를 어떻게 회피해 볼 수 있을지, [npm audit and audit-resolve.json](https://github.com/npm/rfcs/pull/18) 등 RFC에 대해서도 이야기한다.

---

[Access Guide](https://accessguide.io/)에는 WCAG 2.1 접근성 가이드가 작성돼 있다.
각 토픽별 해설 및 구현 방법, 테스트 방법 등 리소스가 정리 돼 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## html2canvas/CHANGELOG.md at master · niklasvh/html2canvas
[github.com/niklasvh/html2canvas/blob/master/CHANGELOG.md#100-2021-07-04](https://github.com/niklasvh/html2canvas/blob/master/CHANGELOG.md#100-2021-07-04 "html2canvas/CHANGELOG.md at master · niklasvh/html2canvas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

HTML을 Canvas로 스크린샷을 찍는 html2canvas 1.0.0 릴리스


----

## Release v8.0.0 · nestjs/nest
[github.com/nestjs/nest/releases/tag/v8.0.0](https://github.com/nestjs/nest/releases/tag/v8.0.0 "Release v8.0.0 · nestjs/nest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nest.js 8.0.0 릴리스.
Logger 클래스 개선, API Versioning 지원


----

## Release 8.9.2 · mermaid-js/mermaid
[github.com/mermaid-js/mermaid/releases/tag/8.9.2](https://github.com/mermaid-js/mermaid/releases/tag/8.9.2 "Release 8.9.2 · mermaid-js/mermaid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">diagram</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

mermaid 8.9.2에서 `%%{init: {<JSON_OBJECT>}}%%` 설정 기법을 사용한 XSS 취약점과 프로토타입 오염(Prototype pollution) 취약점이 수정됐다.

- [#1106238 Client-Side DOS via Mermaid Prototype Pollution vulnerability](https://hackerone.com/reports/1106238 "#1106238 Client-Side DOS via Mermaid Prototype Pollution vulnerability")

----

## Firefox 90.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/90.0/releasenotes/](https://www.mozilla.org/en-US/firefox/90.0/releasenotes/ "Firefox 90.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 90 릴리스.
ES Proposal Stage 4의 Private class fields를 기본적으로 지원, Stage 3의 String / Array의 `at()` 지원.
FTP 지원 삭제, WheelEvent의 호환성 개선 등.

- [Firefox 90 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/90 "Firefox 90 for developers - Mozilla | MDN")
- [tc39/proposal-relative-indexing-method: A TC39 proposal to add an .at() method to all the basic indexable classes (Array, String, TypedArray)](https://github.com/tc39/proposal-relative-indexing-method "tc39/proposal-relative-indexing-method: A TC39 proposal to add an .at() method to all the basic indexable classes (Array, String, TypedArray)")

----

## Release 2.27.0 · prisma/prisma
[github.com/prisma/prisma/releases/tag/2.27.0](https://github.com/prisma/prisma/releases/tag/2.27.0 "Release 2.27.0 · prisma/prisma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">MongoDB</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 용 ORM 라이브러리 Prisma 2.27.0 릴리스.
MongoDB를 프리뷰 지원, M1 Mac 지원, pnpm으로 설치할 수 없던 문제 수정 등.

- [Start from scratch with MongoDB (15 min) | Prisma Docs](https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/mongodb-typescript-mongodb "Start from scratch with MongoDB (15 min) | Prisma Docs")

----
<h1 class="site-genre">아티클</h1>

----

## How does Node.js load its built-in/native modules? | Joyee Cheung&#039;s Blog
[joyeecheung.github.io/blog/2021/07/06/how-does-node-js-load-its-builtins-native-modules/](https://joyeecheung.github.io/blog/2021/07/06/how-does-node-js-load-its-builtins-native-modules/ "How does Node.js load its built-in/native modules? | Joyee Cheung&#039;s Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 내에 JavaScript로 작성된 빌트인 모듈은 Node.js 바이너리에 어떻게 올려지고 읽혀는지 소개.
바이너피 파일의 읽기 전용 데이터 섹션에 올려지며 bootstrap에서 V8을 사용해 컴파일 및 Snapshots를 다루는 구조로 돼 있다.


----

## Resource inlining in JavaScript frameworks
[web.dev/aurora-resource-inlining/](https://web.dev/aurora-resource-inlining/ "Resource inlining in JavaScript frameworks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">Angular</span> <span class="jser-tag">CSS</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Next.js와 Angular Google Fonts의 Critical CSS 인라인화.
Font를 가져오는 CSS를 인라인화 하는 것으로 CLS를 최적화 할 수 있다고 소개


----

## npm audit: Broken by Design — Overreacted
[overreacted.io/npm-audit-broken-by-design/](https://overreacted.io/npm-audit-broken-by-design/ "npm audit: Broken by Design — Overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>


devDependencies로 사용하는 도구에 대한 `npm audit` 보고 대부분이 ReDoS 취약성에 대한 것이라는 문제 제기.
이를 회피하기 위한 방법으로 제품에서 사용되는 `dependencies` 만 검사하는 `npm audit --production`, 공개하는 패키지를 인라인화 하는 방법과 또다른 문제를 소개하며 에코시스템에 대한 우려도 나타내고 있다.


----

## TypeScript and native ESM on Node.js
[2ality.com/2021/06/typescript-esm-nodejs.html](https://2ality.com/2021/06/typescript-esm-nodejs.html "TypeScript and native ESM on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

타입스크립트에서 ESM에 대응하는 방법.
package.json의 `"type": "module"` 설정, `exports` 필드와 `typesVersions` 필드, `import`하는 파일의 확장자 설정 등


----

## jQuery에서 TypeScript・React 까지 - Vite로 시작하는 모던 고속 개발 환경 구축 - ICS MEDIA(일본어)
[ics.media/entry/210708/](https://ics.media/entry/210708/ "jQuery에서 TypeScript・React 까지 - Vite로 시작하는 모던 고속 개발 환경 구축 - ICS MEDIA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Vite의 기본적인 사용 방법 소개 글.
라이브러리, TypeScript, 이미지 등 에셋 사용, 설정 파일, IE11 대응 등.


----

## Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog
[blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/](https://blog.mozilla.org/security/2021/07/12/firefox-90-supports-fetch-metadata-request-headers/ "Firefox 90 supports Fetch Metadata Request Headers - Mozilla Security Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox 90에서 Fetch Metadata Request Headers를 지원한다.
`Sec-Fetch-Site` 등 교차 사이트 공격으로 부터 보호할 수 있는 `Sec-Fetch-*` 요청 헤더를 지원한다는 것.

- [Protect your resources from web attacks with Fetch Metadata](https://web.dev/fetch-metadata/ "Protect your resources from web attacks with Fetch Metadata")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Access Guide
[accessguide.io/](https://accessguide.io/ "Access Guide")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">document</span></p>

WCAG 2.1 설명 사이트.
어떤게 구현할 수 있는지, 어떻게 테스트할 수 있는지, 실제 예 등을 소개한다.


----

## Javascript Decorators
[javascriptdecorators.org/](https://javascriptdecorators.org/ "Javascript Decorators")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">Tools</span> <span class="jser-tag">debug</span></p>

ECMAScript Proposal의 Decorators를 시험해 볼 수 있는 Playground 도구

- [tc39/proposal-decorators: Decorators for ES6 classes](https://github.com/tc39/proposal-decorators "tc39/proposal-decorators: Decorators for ES6 classes")


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## FrontLabsOfficial/vue-tiny-validate: 💯 Tiny (2.5KB minified) Vue Validate Composition
[github.com/FrontLabsOfficial/vue-tiny-validate](https://github.com/FrontLabsOfficial/vue-tiny-validate "FrontLabsOfficial/vue-tiny-validate: 💯 Tiny (2.5KB minified) Vue Validate Composition")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span></p>

Vue Composition API 용 벨리데이션 라이브러리


----

## lucacasonato/dext.ts: The Preact Framework for Deno
[github.com/lucacasonato/dext.ts](https://github.com/lucacasonato/dext.ts "lucacasonato/dext.ts: The Preact Framework for Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">Next.js</span></p>

Next.js에서 영감을 받아 개발한 Deno 용 Preact 기반 웹프레임워크


----
<h1 class="site-genre">도서</h1>

----

## O&#039;Reilly Japan - 처음 시작하는 WebGL 2 제 2판(일본어)
[www.oreilly.co.jp/books/9784873119373/](https://www.oreilly.co.jp/books/9784873119373/ "O&#039;Reilly Japan - 처음 시작하는 WebGL 2 제 2판")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2021년 07월 21일 출간 예정인 WebGL 입문서
원서는 Real-Time 3D Graphics with WebGL 2 - Second Edition


----
