---
title: "2019-09-17: Chrome 77, TypeScript 3.7 로드맵, Can I use and MDN"
author: "azu"
translator: U-Yeong Ju, Taihoon Kim
layout: post
date : 2019-09-17T00:03:38.654Z
category: JSer
tags:
- Chrome
- TypeScript
- MDN

---

JSer.info #453 - Chrome 77가 릴리스 됐습니다.

- [New in Chrome 77  |  Web  |  Google Developers](https://developers.google.com/web/updates/2019/09/nic77)

Chrome 77에서는 `PerformanceObserver` 내에서 페이지의 큰 변경을 감지할 수 있는 Largest Contentful Paint(LCP)을 지원합니다.

- [Largest Contentful Paint  |  web.dev](https://web.dev/largest-contentful-paint/)

외에도 `formdata` 이벤트, `formAssociated` 속성을 지원합니다.
또, 주소바에 표시되고 있던 EV 증명서 정보가 상세 패널 쪽으로 이동됐습니다.

- [Troy Hunt: Extended Validation Certificates are (Really, Really) Dead](https://www.troyhunt.com/extended-validation-certificates-are-really-really-dead/)
- [Upcoming Change to Chrome's Identity Indicators - Google 그룹스](https://groups.google.com/a/chromium.org/forum/#!msg/security-dev/h1bTcoTpfeI/jUTk1z7VAAAJ)

----

[TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352) 이슈에 TypeScript 3.7의 로드맵이 공개돼 있습니다.

ECMAScript Private Fields, Optional Chaining, Nullish Coalescing, Top-Level await 등 현재 Stage3인 제안을 대응할 예정입니다.
또, 지금까지 제한돼 있던 `--declaration`과 `--allowJs` 조합이나 `--declaration`과 `--isolatedModules`와의 조합도 지원할 예정이라고 합니다.
이 외로 `typescript` 패키지 크기 최적화, `@types` 패키지를 GitHub Package Registry에도 배포할 수 있도록 변경됩니다. 그리고 핸드북도 각 변경 사항에 맞춰 개정될 예정입니다.

----

[Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/)에는 [MDN compat data](https://github.com/mdn/browser-compat-data)와 [Can I use...](https://caniuse.com/)의 공동 작업에 대해서 정리돼 있습니다.

두 서비스 모두 기능 등에 대한 브라우저 지원 상황을 정리한 데이터지만 목적이 다르기 때문에 데이터의 특성이 조금씩 다릅니다. 
MDN은 모든 세세한 기능에 대한 호환성(compatibility) 데이터를, Can I use...는 큰 기능을 중점으로 브라우저 지원 여부를 정리합니다. 
따라서 Can I use...에는 포함되지 않는 데이터도 많이 있습니다.

이번 공동 작업으로 [Can I use...](https://caniuse.com/)가 [MDN compat data](https://github.com/mdn/browser-compat-data)의 데이터를 사용해 기능에 관한 브라우저 정보도 지원 상황을 표시할 수 있도록 됐습니다(현재 양쪽의 데이터를 검색한 결과가 각각 노출됨).
 
또, 비슷한 사이트로 각 메일 클라이언트 별 이용할 수 있는 HTML이나 CSS 지원 상황 정리한 Can i email...이라는 사이트도 다른 개발자에 의해 공개됐습니다.

- [Can I email… Support tables for HTML and CSS in emails](https://www.caniemail.com/)

----

<h1 class="site-genre">헤드라인</h1>

----

## TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript
[github.com/microsoft/TypeScript/issues/33352](https://github.com/microsoft/TypeScript/issues/33352 "TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span></p>

TypeScript 3.7의 로드맵이 공개됐습니다.
ECMAScript Private Fields, Optional Chaining, Nullish Coalescing 및 `--declaration`과 `--allowJs` 속성 조합 등에 대한 대응이 이뤄집니다.
또, `typescript` 패키지 크기 최적화, `@types` 패키지를 GitHub Package Registry에도 배포할 수 있도록 변경되며 여러 변경 사항에 맞춰 핸드북도 개정될 예정입니다.


----

## Release DOMPurify 2.0.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/2.0.0](https://github.com/cure53/DOMPurify/releases/tag/2.0.0 "Release DOMPurify 2.0.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

DOMpurify 2.0.0이 릴리스 됐습니다.
Trusted Types를 사용할 수 있는 경우에도 `RETURN_TRUSTED_TYPE` 옵션을 전달 했을 때만 Trusted Types을 사용하도록 변경됐습니다.


----

## Google Developers Blog: Flutter news from GDD China: uniting Flutter on web and mobile, and introducing Flutter 1.9
[developers.googleblog.com/2019/09/flutter-news-from-gdd-china-flutter1.9.html?m&#x3D;1](https://developers.googleblog.com/2019/09/flutter-news-from-gdd-china-flutter1.9.html?m=1 "Google Developers Blog: Flutter news from GDD China: uniting Flutter on web and mobile, and introducing Flutter 1.9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">ReleaseNote</span></p>

Flutter 1.9가 릴리스 됐습니다.
웹 지원이 메인 저장소에 합쳐(merge)졌습니다.


----

## ESLint v6.4.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2019/09/eslint-v6.4.0-released](https://eslint.org/blog/2019/09/eslint-v6.4.0-released "ESLint v6.4.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 6.4.0이 릴리스 됐습니다.
`no-import-assign`, `prefer-regex-literals`, `default-param-last` 규칙이 추가됐습니다.
`enforceForClassMembers` 옵션으로 일부 규칙을 클래스 구문에도 적용할 수 있도록 변경됐습니다.

- [ESLint v6.4.0 - Qiita](https://qiita.com/mysticatea/items/4164b162fb37dcc443a1 "ESLint v6.4.0 - Qiita")

----

## Release v4.0.0 · immerjs/immer
[github.com/immerjs/immer/releases/tag/v4.0.0](https://github.com/immerjs/immer/releases/tag/v4.0.0 "Release v4.0.0 · immerjs/immer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Immer 4.0.0이 릴리스 됐습니다.
development mode 일 때 모든 값이 deep frozen 된 상태로 저장되도록 변경됐습니다.
또, 웹 사이트의 문서가 개편됐습니다.

- [Introduction to Immer · Immer](https://immerjs.github.io/immer/docs/introduction "Introduction to Immer · Immer")

----

## Release 2.4.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v2.4.0](https://github.com/avajs/ava/releases/tag/v2.4.0 "Release 2.4.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

AVA 2.4.0이 릴리스 됐습니다.
`t.try()`를 플래그를 붙여 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## How to build a plugin system on the web and also sleep well at night
[www.figma.com/blog/how-we-built-the-figma-plugin-system/](https://www.figma.com/blog/how-we-built-the-figma-plugin-system/ "How to build a plugin system on the web and also sleep well at night")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">plugin</span></p>

플러그인으로 추가되는 서드파티 코드를 안전하게 웹 브라우저에서 실행할 수 있도록 하는 구조에 대해서 이야기합니다. 
`<inline-iframe>`과 자바스크립트 인터프리터 이용하는 방법, Proposal의 Realms(shim)을 사용한 샌드박스 등을 소개합니다.

- [tc39/proposal-realms: ECMAScript Proposal, specs, and reference implementation for Realms](https://github.com/tc39/proposal-realms "tc39/proposal-realms: ECMAScript Proposal, specs, and reference implementation for Realms")
- [Agoric/realms-shim: Spec-compliant shim for Realms TC39 Proposal](https://github.com/Agoric/realms-shim "Agoric/realms-shim: Spec-compliant shim for Realms TC39 Proposal")

----

## Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/](https://hacks.mozilla.org/2019/09/caniuse-and-mdn-compat-data-collaboration/ "Caniuse and MDN compatibility data collaboration - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

MDN Compat Data를 Can I Use의 웹 사이트에서 제공합니다.
이제 Can I Use에서 MDN의 데이터를 기반으로 기능 및 지원 브라우저 상황을 함께 볼 수 있습니다.


----

## A lighter V8 · V8
[v8.dev/blog/v8-lite](https://v8.dev/blog/v8-lite "A lighter V8 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

V8의 Lite mode를 소개합니다.
메모리가 적은 디바이스 용 모드로 메모리 소비를 크게 줄이는 것을 목표로 하고 있습니다.


----

## WebGPU and WSL in Safari | WebKit
[webkit.org/blog/9528/webgpu-and-wsl-in-safari/](https://webkit.org/blog/9528/webgpu-and-wsl-in-safari/ "WebGPU and WSL in Safari | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari Technology Preview 91부터 베타로 지원 되고있는 WebGPU API와 WSL에 대해 작성돼 있습니다.
WebGPU의 파이프라이느처리 최적화, 런타임 성능, Web Shading Language(WSL) 등을 소개합니다.


----

## X3D: Declarative 3D for the Modern Web
[blog.scottlogic.com/2019/08/27/declarative-3d-for-the-modern-web.html](https://blog.scottlogic.com/2019/08/27/declarative-3d-for-the-modern-web.html "X3D: Declarative 3D for the Modern Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">3D</span> <span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

선언적으로 3D를 표현하는 X3D라는 사양과 X3DOM 구현에 대해서 이야기합니다.
SVG 처럼 HTML 내에 태그를 작성하여 3D를 표현할 수 있습니다.


----

## New in Chrome 77  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/09/nic77](https://developers.google.com/web/updates/2019/09/nic77 "New in Chrome 77  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 77 릴리스 됐습니다.
Largest Contentful Paint(LCP), `formdata` 이벤트, `formAssociated` 프로퍼티를 지원합니다.

- [More capable form controls  |  web.dev](https://web.dev/more-capable-form-controls/ "More capable form controls  |  web.dev")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Can I email… Support tables for HTML and CSS in emails
[www.caniemail.com/](https://www.caniemail.com/ "Can I email… Support tables for HTML and CSS in emails")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mail</span> <span class="jser-tag">HTML</span> <span class="jser-tag">webservice</span></p>

메일 내에서 특정 HTML 태그와 CSS를 사용할 수 있는지, 메일 클라이언트 지원 상황을 검색할 수 있는 서비스입니다. 


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## nanoSQL 2
[nanosql.io/](https://nanosql.io/ "nanoSQL 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SQL</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

SQL builder 라이브러리입니다.
인메모리, 브라우저의 IndexedDB나 Localstorage, Node.js의 MySQL이나 Redix 등 다양한 데이터베이스를 지원합니다. 


----
<h1 class="site-genre">도서</h1>

----

## Web Development with Node and Express, 2nd Edition - O'Reilly Media
[shop.oreilly.com/product/0636920261216.do](http://shop.oreilly.com/product/0636920261216.do "Web Development with Node and Express, 2nd Edition - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">book</span></p>

2019년 10월 출간 예정인 Node.js와 Express를 주제로한 도서입니다.


----

## daumann/ECMAScript-new-features-list: A comprehensive list of new ES features, including ES2015 (ES6), ES2016 (ES7), ES2017 (ES8), ES2018 (ES9), ES2019 (ES10)
[github.com/daumann/ECMAScript-new-features-list](https://github.com/daumann/ECMAScript-new-features-list "daumann/ECMAScript-new-features-list: A comprehensive list of new ES features, including ES2015 (ES6), ES2016 (ES7), ES2017 (ES8), ES2018 (ES9), ES2019 (ES10)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">document</span></p>

ECMAScript 버전 별 추가된 기능 및 구문과 샘플 코드가 정리돼 있는 저장소입니다.


----
