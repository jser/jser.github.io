---
title: "2017-07-03 JS: ECMAScript 2017, Prettier 1.5.0, UX의 성능 지표"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-07-03T05:14:08.123Z
category: JSer
tags:
- ECMAScript
- Prettier
- performance
- browser

---

JSer.info #338 - ECMAScript 2017가 정식 릴리즈됐습니다.

> ECMA-262 8th edition - ECMAScript® 2017 Language Specification
> -- [Ecma latest news](http://ecma-international.org/news/index.html "Ecma latest news")

- [Standard ECMA-262](http://ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")

ES2017에는 async/await, shared memory and atomic, `Object.entires` / `Object.values`, `String#padStart` / `String#padEnd`, `Object.getOwnPropertyDescriptors()`이나 함수 인자나 매개변수 끝에 콤마(Trailing commas) 허용 등이 추가됐습니다.

상세한 내용은 아래 웹사이트를 참고하시길 바랍니다.

- [III ECMAScript 2017](http://exploringjs.com/es2016-es2017/pt_es2017.html "III ECMAScript 2017")

책정 중인 향후 버전(ES2018~)에 대한Proposal은 아래 문서에 정리돼 있습니다.

- [tc39/proposals: Tracking ECMAScript Proposals](https://github.com/tc39/proposals "tc39/proposals: Tracking ECMAScript Proposals")
- [babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals](https://github.com/babel/proposals "babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals")
  - Babel의 대응 여부

----

코드 포맷팅 도구인 Prettier 1.5.0이 릴리즈됐습니다.

- [Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier](https://github.com/prettier/prettier/releases/tag/1.5.0 "Release 1.5.0: GraphQL, CSS-in-JS &amp; JSON · prettier/prettier")

GraphQL, CSS in JS, JSON을 대응하고 CSS나 TypeScript, JSX 관련 버그가 수정됐습니다.

----

[Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics)에는  사용자 경험에 영향을 주는 성능 지표에 관해 작성돼 있습니다.

단순히 `DOMContentLoaded`나 `load` 시간만으론 사용자 경험을 측정할 수 없는 문제가 있습니다.
때문에 First Paint / First Meaningful Paing / Time to Interactive(TTI) / Longtasks 등의 지표나 그 의미에 대해 소개합니다.

이 글과 관련한 Google I/O 발표 영상이 있으니 함께 보시길 바랍니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6Ljq-Jn-EgU?ecver=1" frameborder="0" allowfullscreen></iframe>

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier
[github.com/prettier/prettier/releases/tag/1.5.0](https://github.com/prettier/prettier/releases/tag/1.5.0 "Release 1.5.0: GraphQL, CSS-in-JS & JSON · prettier/prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

prettier 1.5.0이 릴리즈됐습니다.
GraphQL, CSS in JS, JSON을 대응하고 CSS나 TypeScript, JSX 관련 버그가 수정됐습니다.

- [Adding a new layout strategy to Prettier – Geckoboard: Under-the-Hood – Medium](https://medium.com/geckoboard-under-the-hood/adding-a-new-layout-strategy-to-prettier-8d33084c0f99 "Adding a new layout strategy to Prettier – Geckoboard: Under-the-Hood – Medium")

----

## Release v7.0.0-beta.16 · babel/babylon
[github.com/babel/babylon/releases/tag/v7.0.0-beta.16](https://github.com/babel/babylon/releases/tag/v7.0.0-beta.16 "Release v7.0.0-beta.16 · babel/babylon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">AST</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Babylon 7.0.0 beta16이 릴리즈됐습니다.
TypeScript 파서가 추가됐고 BigInt(Stage 2)을 지원합니다.

- [TypeScript parser by andy-ms · Pull Request #523 · babel/babylon](https://github.com/babel/babylon/pull/523 "TypeScript parser by andy-ms · Pull Request #523 · babel/babylon")

----

## Ecma latest news
[ecma-international.org/news/index.html](http://ecma-international.org/news/index.html "Ecma latest news")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

"ECMA-262 8th edition - ECMAScript® 2017 Language Specification" ES2017가 GA에서 승이되어 정식으로 릴리즈됐습니다.

- [Standard ECMA-262](http://ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")

----

## Release Notes for Safari Technology Preview 34 | WebKit
[webkit.org/blog/7760/release-notes-for-safari-technology-preview-34/](https://webkit.org/blog/7760/release-notes-for-safari-technology-preview-34/ "Release Notes for Safari Technology Preview 34 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 34가 릴리즈됐습니다.
`RTCRtpTransceiver#addTransceiver`을 지원하고 트랙 단위로 단방향 통신을 사용할 수 있도록 변경됐습니다. 또, W3C Secure Contexts을 구현했으며 SRI를 시험적으로 지원하는 등 다양한 변경 사항이 있습니다.

- [Safari TP 34에서는 새로운 단방향 WebRTC 순서를 사용할 수 있어서 시도해봤다 - Qiita](http://qiita.com/tomoyukilabs/items/59267f25c9dbd43d5ecb "Safari TP 34에서는 새로운 단방향 WebRTC 순서를 사용할 수 있어서 시도해봤다 - Qiita")(일본어)

----
<h1 class="site-genre">아티클</h1>

----

## Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/user-centric-performance-metrics](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics "Leveraging the Performance Metrics that Most Affect User Experience  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

사용자 경험에 대한 영향 판단할 수 있는 성능 지표에 관해 이야기합니다.
로드 시간만으로는 경험을 측정할 수 없기 없습니다. 때문에 First Paint / First Meaningful Paing / Time to Interactive / Longtasks 지표를 이용해 이것이 의미하는 바와 측정하는 방법에 대해 작성돼 있습니다.

- [You Need to know SSR // Speaker Deck](https://speakerdeck.com/yosuke_furukawa/you-need-to-know-ssr "You Need to know SSR // Speaker Deck")

----

## Chrome 60 DevTools의 새기능 / 변경사항 - Qiita(일본어)
[qiita.com/kyoshidajp/items/e3f9be02a7ccd00aa7d7](http://qiita.com/kyoshidajp/items/e3f9be02a7ccd00aa7d7 "Chrome 60 DevTools の新機能/変更点 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome 60의 개발자 도구를 소개합니다.

----

## NYTimes/kyt: Starting a new JS app? Build, test and run advanced apps with kyt 🔥
[github.com/nytimes/kyt](https://github.com/nytimes/kyt "NYTimes/kyt: Starting a new JS app? Build, test and run advanced apps with kyt 🔥")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScript 애플리케이션 툴 킷 kyt 입니다.
Babel/webpack / Jest / Stylelint / ESlint / proto 등의 셋업이 한번에 할 수 있는 도구입니다.

----

## Supercharged Live Stream Blog: Code Splitting  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/06/supercharged-codesplit](https://developers.google.com/web/updates/2017/06/supercharged-codesplit "Supercharged Live Stream Blog: Code Splitting  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span> <span class="jser-tag">plugin</span> <span class="jser-tag">video</span></p>

Code Splitting 개념과 이를 수행하는 Babel 플러그인을 만드는 과정을 소개하는 스크린 캐스트입니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Building m.uber: Engineering a High-Performance Web App for the Global Market - Uber Engineering Blog
[eng.uber.com/m-uber/](https://eng.uber.com/m-uber/ "Building m.uber: Engineering a High-Performance Web App for the Global Market - Uber Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">mobile</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

Uber의 모바일 최적화에 대해 작성돼 있습니다. 
기본적으로 React를 사용하지만 mobile에서는 Preact로 바꿔 적용하고 서버 사이드 렌더링이나 초기 bundle 크기를 줄이기 위해 Code split 이용합니다. 또 의존 라이브러리가 없는 작은 사이즈의 Just를 사용하고 SW나 IndexedDB를 이용해 캐시합니다. 또, 문제 조금 더 쉽게 찾아내기 위한 에러 핸들링 방법도 소개합니다.

- [angus-c/just: A library of dependency-free utilities that do just do one thing.](https://github.com/angus-c/just "angus-c/just: A library of dependency-free utilities that do just do one thing.")

----

## GraphQL Network Communication Framework
[graphql-io.com/](http://graphql-io.com/ "GraphQL Network Communication Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

클라이언트와 서버 간 커뮤니테이션이 가능한 GraphQL의 프레임워크입니다.
Apollo/WebSocket을 기반으로 개발됐습니다.

----

## HTML Standard
[html.spec.whatwg.org/dev/](https://html.spec.whatwg.org/dev/ "HTML Standard")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span></p>

WHATWG HTML 사양의 Developer's Edition 입니다.
브라우저 벤더를 위한 정보는 삭제하고 웹 개발자에 초점을 맞춰 정보를 정리한 HTML 사양서 입니다.

- [HTML Standard 일본어 버전](https://momdo.github.io/html/dev/ "HTML Standard 일본어 버전")
- [Review on utilization of \`w-nodev\` annotation · Issue #1488 · whatwg/html](https://github.com/whatwg/html/issues/1488#issuecomment-310450737 "Review on utilization of \&#x60;w-nodev\&#x60; annotation · Issue #1488 · whatwg/html")
- [WHATWG HTML Standard Developer Edition 이야기 - 물속의 피](http://momdo.hatenablog.jp/entry/20170702/1498999477 "WHATWG HTML Standard Developer Edition 이야기 - 물속의 피")
- [HTML5 for Web Developers | HTML5 Doctor](http://html5doctor.com/html5-for-web-developers/ "HTML5 for Web Developers | HTML5 Doctor")

----

## babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals
[github.com/babel/proposals](https://github.com/babel/proposals "babel/proposals: (WIP) Tracking the status of Babel's implementation of TC39 proposals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

ECMAScript proposal에 대한 Babel의 구현 현황에 대해 정리돼 있는 문서입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## roman01la/js-memory-usage: Data Structures Memory Usage in JavaScript
[github.com/roman01la/js-memory-usage](https://github.com/roman01la/js-memory-usage "roman01la/js-memory-usage: Data Structures Memory Usage in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">정리</span> <span class="jser-tag">performance</span></p>

JavaScript의 데이터 구조 별 / 라이브러리 별 메로리 사용량이 정리돼 있는 저장소 입니다. List / Array / Map / Set이 JavaScript / ImmutableJS / ClojureScript / GopherJS / Reason 등 여러가지 구현체와 비교돼 있습니다.

----

## pinterest/esprint: Fast eslint runner
[github.com/pinterest/esprint](https://github.com/pinterest/esprint "pinterest/esprint: Fast eslint runner")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">Tools</span></p>

ESLint를 parallel하게 수행할 수 있는 도구입니다.

----

## anvilresearch/webcrypto: W3C Web Cryptography API for Node.js
[github.com/anvilresearch/webcrypto](https://github.com/anvilresearch/webcrypto "anvilresearch/webcrypto: W3C Web Cryptography API for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

Web Cryptography API를 대응한 Node.js의 polyfill(ponyfill) 라이브러리입니다.

----

## coast-team/netflux: JavaScript client and server side transport API based on WebRTC & WebSocket
[github.com/coast-team/netflux](https://github.com/coast-team/netflux "coast-team/netflux: JavaScript client and server side transport API based on WebRTC & WebSocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">browser</span></p>

WebRTC, WebSocket을 기반으로 구현한 P2P 라이브러리입니다.
브라우저, Node.js로 데이터를 주고 받을 수 있습니다.

----

## OnetapInc/chromy: Chromy is a library for operating headless chrome. 🍺🍺🍺
[github.com/OnetapInc/chromy](https://github.com/OnetapInc/chromy "OnetapInc/chromy: Chromy is a library for operating headless chrome. 🍺🍺🍺")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Headless Chrome을 Nightmare.js 처럼 조작할 수 있는 API를 제공하는 라이브러리입니다.
Chrome DevTools Protocol을 사용해 테스트를 위한 처리를 주고받습니다.

----

## dollarshaveclub/study: A Simple, progressive, client/server AB testing library ⚡️
[github.com/dollarshaveclub/study](https://github.com/dollarshaveclub/study "dollarshaveclub/study: A Simple, progressive, client/server AB testing library ⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

A/B 테스팅 라이브러리입니다.
universal로 동작하고 storage driver로 데이터의 저장소를 지정할 수 있습니다.

----

## egoist/dom-dom: JSX to actual DOM.
[github.com/egoist/dom-dom](https://github.com/egoist/dom-dom "egoist/dom-dom: JSX to actual DOM.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jsx</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

`document` API를 사용해 JSX를 DOM 객체로 변환하는 라이브러리입니다.

----

## yahoo/mendel: Build toolchain for experimentation on isomorphic web applications with tree-inheritance and multivariate support.
[github.com/yahoo/mendel](https://github.com/yahoo/mendel "yahoo/mendel: Build toolchain for experimentation on isomorphic web applications with tree-inheritance and multivariate support.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">설계</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

코드의 플래그가 아닌 규칙 파일 기준으로 프로젝트 구조를 관리할 수 있는 도구입니다.
시험적인 기능을 A / B 테스트 하기 쉽게 하기 위한 프레임워크입니다.
플래그 기반은 기술적 부채가 쌓이기 쉽고 야후에서 지속가능성에 대한 조사 결과 디자인된 라이브러리입니다.

- [mendel/Design.md at master · yahoo/mendel](https://github.com/yahoo/mendel/blob/master/docs/Design.md "mendel/Design.md at master · yahoo/mendel")

----

## jaredpalmer/formik: Forms in React, without tears
[github.com/jaredpalmer/formik](https://github.com/jaredpalmer/formik "jaredpalmer/formik: Forms in React, without tears")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React 용의 폼 라이브러리입니다.

----
