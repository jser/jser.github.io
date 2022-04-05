---
title: "2022-03-29: ES2022 릴리스 후보, Safari Technology Preview 142, Storybook 대체 구현"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-03-29T03:02:54.858Z
category: JSer
tags:
- ECMAScript
- React
- debug
- Tools
- vite

---

JSer.info #585 - ECMAScript 2022 릴리스 후보 사양이 공개됐다.
아울러 ECMAScript Internationalization API의 ES2022 릴리스 후보도 공개됐다.

- [Release ES2022 Candidate March 2022 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03)
- [Release ES Intl 2022 Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/es2022-candidate)

6월 즈음 Ecma International GA(총회)에서 승인하는 시점에 맞춰 ES2022가 정식 릴리스 될 예정이다.
Normative(사양 변경, Proposal 병합)한 변경은 아래 페이지를 통해 살펴볼 수 있다.

- [ES2021...ES2022 Normative changes: https://github.com/tc39/ecma262/compare/es2021...es2022-candidate-2022-03](https://gist.github.com/azu/a33211926e3de8bff8de83d6783c55eb)

ES2022에 포함될 Proposal은 다음과 같다.

- Class Fields
    - [tc39/proposal-class-fields](https://github.com/tc39/proposal-class-fields) private/public
    - [Ergonomic brand checks for Private Fields](https://github.com/tc39/proposal-private-fields-in-in)
- [Class static initialization blocks](https://github.com/tc39/proposal-class-static-block)
- [Error Cause](https://github.com/tc39/proposal-error-cause)
- [RegExp Match Indices](https://github.com/tc39/proposal-regexp-match-indices)
- [Top-level `await` proposal](https://github.com/tc39/proposal-top-level-await)
- [Object.hasOwn](https://github.com/tc39/proposal-accessible-object-hasownproperty)
- [String/Array.at()](https://github.com/tc39/proposal-relative-indexing-method)


ES2022를 지원하는 브라우저는 [ECMAScript compatibility table](https://kangax.github.io/compat-table/es2016plus/)로 확인 할 수 있다. Node.js는 [node.green](https://node.green/#ES2022)로 확인한다.
ES2022를 지원하는 도구로는 [Babel](https://babeljs.io/docs/en/plugins-list#es2022)、[TypeScript 4.6](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/), [ESLint v8.9.0](https://eslint.org/blog/2022/02/eslint-v8.9.0-released), [esbuild v0.14.24](https://github.com/evanw/esbuild/releases/v0.14.24) 등이 있다.
ES2022를 다루는 도서로는 [JavaScript for impatient programmers](https://exploringjs.com/impatient-js/index.html)가 [이미 개정](https://exploringjs.com/impatient-js/ch_new-javascript-features.html#new-in-es2022) 했으며 [JavaScript Primer](https://jsprimer.net/)(일본어)는 [개정중](https://github.com/asciidwango/js-primer/issues/1337)이다.

---

Safari Technology Preview 142가 릴리스 됐다.

- [Release Notes for Safari Technology Preview 142 | WebKit](https://webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/)

CSS Subgrid / CSS Container Queries / CSS Motion Path가 기본 활성화 됐다.
ECMAScript Proposal Stage3의 [ShadowRealm](https://github.com/tc39/proposal-shadowrealm)도 기본 활성화 됐다.
또, 이전에 구현했으나 이전에 삭제한 [SharedWorker](https://developer.mozilla.org/ja/docs/Web/API/SharedWorker)를 다시 구현하고 있다.
그 외로는 WebKit이 제안하고 있는 3D 컨텐츠를 표시하기 위한 `<model>` 요소를 실험적으로 구현하고 있다.

- [explainers/README.md at main · WebKit/explainers](https://github.com/WebKit/explainers/blob/main/model/README.md)


----

<h1 class="site-genre">헤드라인</h1>

----

## Release ES2022 Candidate March 2022 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03](https://github.com/tc39/ecma262/releases/tag/es2022-candidate-2022-03 "Release ES2022 Candidate March 2022 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2022 릴리스 후보 버전 공개.


----

## Release ES Intl 2022 Candidate · tc39/ecma402
[github.com/tc39/ecma402/releases/tag/es2022-candidate](https://github.com/tc39/ecma402/releases/tag/es2022-candidate "Release ES Intl 2022 Candidate · tc39/ecma402")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2022 Internationalizatio API 릴리스 후보 버전 공개.


----

## Release Notes for Safari Technology Preview 142 | WebKit
[webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/](https://webkit.org/blog/12522/release-notes-for-safari-technology-preview-142/ "Release Notes for Safari Technology Preview 142 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 142 릴리스.
CSS Subgrid / CSS Container Queries / CSS Motion Path를 기본 활성화.
ES Proposal Stage3의 Shadow Realms를 기본 활성화, Shared Workers 구현.
`<model>` 요소를 시험적으로 구현(modal 아님. model임).

- [explainers/README.md at main · WebKit/explainers](https://github.com/WebKit/explainers/blob/main/model/README.md "explainers/README.md at main · WebKit/explainers")

----

## Decorators (sans metadata) to stage 3, per 2022.03.28 TC39 · tc39/proposals@eced71d
[github.com/tc39/proposals/commit/eced71d59d7c34e0f173fdec6b6fb477fc2e0371](https://github.com/tc39/proposals/commit/eced71d59d7c34e0f173fdec6b6fb477fc2e0371 "Decorators (sans metadata) to stage 3, per 2022.03.28 TC39 · tc39/proposals@eced71d")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

ECMAScript Proposal의 Decorator가 Stage 3가 됐다.


----
<h1 class="site-genre">아티클</h1>

----

## Introducing Ladle | Ladle
[www.ladle.dev/blog/introducing-ladle/](https://www.ladle.dev/blog/introducing-ladle/ "Introducing Ladle | Ladle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">debug</span> <span class="jser-tag">vite</span></p>

Vite 기반의 Storybook 대체 구현 프로젝트 Ladle 소개.
빌드 시간 최적화와 같은 성능 개선을 주목적으로 하여 개발되고 있다.

- [tajo/ladle: 🥄 Develop, test and document your React components faster.](https://github.com/tajo/ladle "tajo/ladle: 🥄 Develop, test and document your React components faster.")

----

## Introducing MDN Plus: Make MDN your own - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2022/03/introducing-mdn-plus-make-mdn-your-own/](https://hacks.mozilla.org/2022/03/introducing-mdn-plus-make-mdn-your-own/ "Introducing MDN Plus: Make MDN your own - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">article</span></p>

MDN Plus를 소개하는 글.
페이지 변경 알림, 페이지 즐겨찾기 기능, 오프라인 기능 등을 이용할 수 있는 구독 유료 기능.
현재는 US와 Canada에서 이용할 수 있다.


----

## Remixing React Router | Remix
[remix.run/blog/remixing-react-router](https://remix.run/blog/remixing-react-router "Remixing React Router | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

Remix와 React Router 저장소를 합칠 계획을 소개한다.
Remix를 React Router 저장소로 합치고 Remix라고 저장소 이름을 변경할 예정이라고 한다.


----

## npm-scripts 작성 패턴 - mizdra's blog(일본어)
[www.mizdra.net/entry/2022/03/24/093000](https://www.mizdra.net/entry/2022/03/24/093000 "npm-scripts を書く時の手癖 - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

npm-scripts의 기본적인 패턴, npm-run-all을 사용한 복수 명령 실행 패턴, 코드를 사용해 script를 다루는 패턴 등을 소개하는 글.


----

## Tao of Node - Design, Architecture &amp; Best Practices | Alex Kondov - Software Engineer
[alexkondov.com/tao-of-node/](https://alexkondov.com/tao-of-node/ "Tao of Node - Design, Architecture &amp; Best Practices | Alex Kondov - Software Engineer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 애플리케이션 개발의 설계 및 아키텍처 모범 사례 정리 및 소개.
꽤 다양한 팁이 상세하고 일목요연하게 정리돼 있어 도움이 된다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## ブ브라우저 자동 조작 기술 심층 분석, 직접 만져보며 배우는 WebDriver와 Chrome DevTools Protocol - Speaker Deck(일본어)
[speakerdeck.com/hgsgtk/webdriver-cdp-using-php](https://speakerdeck.com/hgsgtk/webdriver-cdp-using-php "ブラウザ自動操作技術の深層へ、直接触れて学ぶ WebDriver と Chrome DevTools Protocol - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">webdriver</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">slide</span> <span class="jser-tag">php</span></p>

WebDriver API와 Chrome DevTools Protocol(CDP)를 주제로 한 슬라이더 자료.
각각의 API를 사용해 브라우저 조작을 자동화하는 처리를 어떻게 작성하는지 소개한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## tajo/ladle: 🥄 Develop, test and document your React components faster.
[github.com/tajo/ladle](https://github.com/tajo/ladle "tajo/ladle: 🥄 Develop, test and document your React components faster.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">vite</span></p>

Vite 기반의 Storybook 대체 구현.

- [Introducing Ladle | Ladle](https://www.ladle.dev/blog/introducing-ladle/ "Introducing Ladle | Ladle")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## MattiasBuelens/web-streams-polyfill: Web Streams, based on the WHATWG spec reference implementation
[github.com/MattiasBuelens/web-streams-polyfill](https://github.com/MattiasBuelens/web-streams-polyfill "MattiasBuelens/web-streams-polyfill: Web Streams, based on the WHATWG spec reference implementation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">stream</span> <span class="jser-tag">polyfill</span></p>

Web Stream의 polyfill 라이브러리.


----
