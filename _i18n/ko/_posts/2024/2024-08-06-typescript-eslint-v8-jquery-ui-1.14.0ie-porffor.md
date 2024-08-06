---
title: "2024-08-06: typescript-eslint v8, jQuery UI 1.14.0(IE 지원 종료), Porffor"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-08-06T00:30:13.575Z
category: JSer
tags:
- TypeScript
- browser
- ESLint
- React
- Extension

---

JSer.info #702 - typescript-eslint v8가 출시되었어요.

- [Announcing typescript-eslint v8 | typescript-eslint](https://typescript-eslint.io/blog/announcing-typescript-eslint-v8/)

ESLint 9 지원, `projectService`를 Stable으로 변경, preset 규칙 변경도 있어요.

---

jQuery UI 1.14.0가 출시되었어요.

- [jQuery UI 1.14.0 released | jQuery UI Blog](https://blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/)

jQuery UI는 이미 [관리 모드](https://blog.jqueryui.com/2021/10/jquery-maintainers-update-and-transition-jquery-ui-as-part-of-overall-modernization-efforts/)지만, 이번 출시에서는 앞으로 관리하기 쉬움을 지향한 변경이 있었어요.

- [Plans for jQuery UI 1.14, dropping support for UI <1.12 in the Download Builder | jQuery UI Blog](https://blog.jqueryui.com/2024/04/plans-for-jquery-ui-1-14-dropping-support-for-ui-1-12-in-the-download-builder/)

jQuery UI 1.14.0는 IE 지원 삭제되어, Chrome/Firefox/Safari/Edge 최신 버전만 지원해요.
또, jQuery UI 1.13 호환성 유지하기 위한 `jQuery.uiBackCompat` 옵션이 추가되었고, 기본적으로 `false` 상태에요.

그리고, jQuery UI 1.14.0으로 업그레이드 가이드도 공개되었어요.

- [jQuery UI 1.14 Upgrade Guide | jQuery UI](https://jqueryui.com/upgrade-guide/1.14/)

---

[Porffor](https://porffor.dev/)는, JavaScript/TypeScript 코드를 WebAssembly에 컴파일 하기 위한 JavaScript 엔진/컴파일러/런타임이에요.
porffor 자체도 JavaScript로 작성되어 있으며, AOT(Ahead-Of-Time)로 JS/TS를 WebAssembly로 컴파일해요.
이로써, [Javy](https://github.com/bytecodealliance/javy) 같은 기존 JavaScript 엔진 ([QuickJS](https://bellard.org/quickjs/))를 Wasm로 담아 실행할 때보다, 적은 파일 크기나 메모리 사용량을 목표로 하고 있어요.

- [CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS](https://github.com/CanadaHonk/porffor)

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing typescript-eslint v8 | typescript-eslint
[typescript-eslint.io/blog/announcing-typescript-eslint-v8/](https://typescript-eslint.io/blog/announcing-typescript-eslint-v8/ "Announcing typescript-eslint v8 | typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint v8 출시.
ESLint 9 지원, `projectService`를 Stable로 변경, preset 규칙 변경

----

## jQuery UI 1.14.0 released | jQuery UI Blog
[blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/](https://blog.jqueryui.com/2024/08/jquery-ui-1-14-0-released/ "jQuery UI 1.14.0 released | jQuery UI Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.14.0 출시.
IEの 지원 종료, 1.11의 API 호환성 유효로 하는 `jQuery.uiBackCompat` 옵션 추가


----

## Release 3.38.0 - 2024.08.05 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.38.0](https://github.com/zloirock/core-js/releases/tag/v3.38.0 "Release 3.38.0 - 2024.08.05 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">polyfill</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.38.0 출시.
`RegExp.escape`/`Promise.try`/Uint8Array to/from base64 and hex를 각각 Stage 3으로 이동.
Node.js 22.3.0에 추가된 `process.getBuiltinModule` 이용하도록


----

## ECMAScript proposal updates @ 2024-07 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/08/06/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/08/06/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-07 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2024년 7월 TC39 미팅에서 ECMAScript Proposal 상태 변경 정리.
`RegExp.escape`가 Stage 3가 됨


----
<h1 class="site-genre">읽을거리</h1>

----

## tsconfig.json의 include 옵션은 무엇을 지정해야하는가 - mizdra&#039;s blog
[www.mizdra.net/entry/2024/07/27/193815](https://www.mizdra.net/entry/2024/07/27/193815 "tsconfig.json의 include 옵션은 무엇을 지정해야하는가 - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

tsconfig.json `includes` 옵션에 대하여


----

## 【2024년 여름】브라우저 확장 기능 개발 가속시킬 프레임워크/도구 3선을 코드와 함께 소개!
[zenn.dev/cybozu\_frontend/articles/introduction-browser-extensions-tools](https://zenn.dev/cybozu_frontend/articles/introduction-browser-extensions-tools "【2024년 여름】브라우저 확장 기능 개발 가속시킬 프레임워크/도구 3선을 코드와 함께 소개!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span> <span class="jser-tag">library</span></p>

브라우저 확장 기능을 개발하는 도구 WXT/Plasmo/Extension.js에 관하여


----

## Patterns for Memory Efficient DOM Manipulation with Modern Vanilla JavaScript – Frontend Masters Boost
[frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/](https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/ "Patterns for Memory Efficient DOM Manipulation with Modern Vanilla JavaScript – Frontend Masters Boost")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

DOM API에서 DOM 변경을 효율적으로 하는 방법에 대하여.
`textContent`와 `innerText`, `insertAdjacentHTML`와 `innerHTML`, DOM Node 삭제와 GC, 이벤트 리너스 클린업에 대하여


----

## Migrate to ESLint 9.x • ~/Z
[tduyng.com/blog/migrating-to-eslint9x/](https://tduyng.com/blog/migrating-to-eslint9x/ "Migrate to ESLint 9.x • ~/Z")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint 9의 Flat Config으로 이행하는 방법.


----

## How Airbnb Smoothly Upgrades React | by Andre Wiggins | The Airbnb Tech Blog | Jul, 2024 | Medium
[medium.com/airbnb-engineering/how-airbnb-smoothly-upgrades-react-b1d772a565fd](https://medium.com/airbnb-engineering/how-airbnb-smoothly-upgrades-react-b1d772a565fd "How Airbnb Smoothly Upgrades React | by Andre Wiggins | The Airbnb Tech Blog | Jul, 2024 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Airbnb에서 React 업데이트에 관하여.
버전 alias 기능을 사용해 복수의 React 버전 이용, SSR 사용하는 서버도 있어서 환경변수를 사용해 버전 지정.
같은 코드에서 2개의 React 버전에서 동작할 수 있도록하면서, 테스트로 단계적으로 이행한 이야기.


----

## How Google handles JavaScript throughout the indexing process – Vercel
[vercel.com/blog/how-google-handles-javascript-throughout-the-indexing-process](https://vercel.com/blog/how-google-handles-javascript-throughout-the-indexing-process "How Google handles JavaScript throughout the indexing process – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Google Bots로 인한 인덱스와 JavaScript/CSS 렌더링 영향에 대한 조사


----

## 프론트엔드 개발에 도움되는 Datadog 활용법 - LegalOn Technologies Engineering Blog
[tech.legalforce.co.jp/entry/2024/08/05/154617](https://tech.legalforce.co.jp/entry/2024/08/05/154617 "프론트엔드 개발에 도움되는 Datadog 활용법 - LegalOn Technologies Engineering Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Datadog</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

Datadog RUM 사용한 프론트엔드 모니터링에 관하여.
유저 액션 트래킹 설정이나 가시화에 대하여

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Porffor
[porffor.dev/](https://porffor.dev/ "Porffor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">Tools</span></p>

Wasm에 컴파일 가능한 JavaScript 엔진/컴파일러/런타임.
JavaScript/TypeScript 코드를 AOT 컴파일해서 Wasm으로 만들 수 있어서, 파일 크기가 작고 효율적으로 동작 가능.
Wasm to C로 컴파일러도 구현하고 있음

- [CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS](https://github.com/CanadaHonk/porffor "CanadaHonk/porffor: A from-scratch experimental AOT JS engine, written in JS")


----
<h1 class="site-genre">슬라이드, 영상</h1>


----

## React Conf 2024 Talks
[conf.react.dev/talks](https://conf.react.dev/talks "React Conf 2024 Talks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Conf 2024 영상 모음


----
