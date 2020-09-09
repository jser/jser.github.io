---
title: "2020-09-08: Chrome 86 베타, Underscore 1.11.0(ESM), JavaScript Primer v2"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-09-08T03:28:31.282Z
category: JSer
tags:
- Chrome
- Underscore
- book

---

JSer.info #504 - Chrome 86 베타 릴리스

- [Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More](https://blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html)

CSS 의사 클래스 `:focus-visible`, 의사 요소 `::marker`를 지원하고 
Document Policy, `FetchEvent.handled`, Shadow DOM Distribution API, `ParentNode.replaceChildren()` 등도 지원한다.
또, Origin Trial로서 WebHID API, Window placement API, `<meta name="battery-savings">` 등을 시험적으로 사용할 수 있다.

그 외로 FTP 지원이 단계적인 폐지 단계에 있다. 
Chrome 86에서는 FTP가 비권장되고 87에서는 기본적으로 해당 기능이 비활성화되며 88에서는 코드베이스에서 삭제 될 예정

- [Deprecate FTP support - Chrome Platform Status](https://www.chromestatus.com/feature/6246151319715840)

----

Underscore 1.11.0 릴리스

- [Underscore.js 1.11.0](https://underscorejs.org/#1.11.0)

이번 릴리스에는 ECMAScript Modules(ESM)를 대응하는 번들 파일이 추가됐다. 이를 위해 Underscore의 코드베이스를 각 함수 별로 모듈화(ES Modules) 했다.

또, 이를 진행한 [Julian Gonggrijp](https://github.com/jgonggrijp)가 Undescore 모듈 버전 이용 방법에 대한 글도 공개했다.

- [Introducing Modular Underscore—Julian Gonggrijp](https://juliangonggrijp.com/article/introducing-modular-underscore.html)

위 글에는 기존(모노리틱) 사용 방법부터 ES Modules 사용 방법, 빌드 크기 최적화, Underscore 2.0 등에 대해 작성돼 있다.

----

JavaScript 입문서 [JavaScript Primer](https://jsprimer.net/)(일본어) 2.0이 릴리스 됐다.

- [Release 2.0.0: ECMAScript 2020対応 · asciidwango/js-primer](https://github.com/asciidwango/js-primer/releases/tag/v2.0.0)
- [JavaScript Primer 2.0 - ECMAScript 2020에 대응한 입문서를 공개했습니다 | Web Scratch](https://efcl.info/2020/09/01/jsprimer-2.0/)(일본어)

JavaScript Primer 2.0에는 ES2020에 추가된 `String.prototype.matchAll`, `globalThis`, BigInt, Nullish coalescing(`??`), Optional chainin（`?.`）에 대한 내용이 포함됐다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 13.7.0 · stylelint/stylelint
[github.com/stylelint/stylelint/releases/tag/13.7.0](https://github.com/stylelint/stylelint/releases/tag/13.7.0 "Release 13.7.0 · stylelint/stylelint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

stylelint 13.7.0 릴리스.
`*-blacklist`, `*-requirelist`,  `*-whitelist`가 비권장화 되고 ` *-disallowed-list`, `*-required-list`으로 이름이 변경됐다.
`stylelint-disable` 코멘트에 설명구를 작성할 수 있다.


----

## ESLint v7.8.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/08/eslint-v7.8.0-released](https://eslint.org/blog/2020/08/eslint-v7.8.0-released "ESLint v7.8.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 7.8.0 릴리스.
`ecmaScript` 옵션으로 `2021`를 사용할 수 있고 Logical assignment operators, numeric separators를 대응한다.


----

## Release v4.0.0 · typescript-eslint/typescript-eslint
[github.com/typescript-eslint/typescript-eslint/releases/tag/v4.0.0](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v4.0.0 "Release v4.0.0 · typescript-eslint/typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript-ESLint 4.0.0 릴리스.
Optional Chaining과 decorators의 AST 변경, Scope 해석을 개선하여 결과적으로 `no-unused-vars` 등의 규칙 개선, `ban-ts-comment`의 기본값이 변경 됐다.
또, TypeScript 4.0에는 TypeScript-ESLint 3.10.0으로 대응하고 있다.


----

## webpack 5 release plan · Issue #11406 · webpack/webpack
[github.com/webpack/webpack/issues/11406](https://github.com/webpack/webpack/issues/11406 "webpack 5 release plan · Issue #11406 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">news</span> <span class="jser-tag">issue</span></p>

webpack 5 릴리스 계획.
webpack 5는 2020년 10월 10일 릴리스 될 예정이며 RC는 9월에 릴리스.
사소한 버그는 webpack 5 릴리스 후에 수정할 예정.


----

## Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More
[blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html](https://blog.chromium.org/2020/09/chrome-86-improved-focus-highlighting.html "Chromium Blog: Chrome 86: Improved Focus Highlighting, WebHID, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 86 베타 릴리스.
CSS 의사 클래스 `:focus-visible`, 의사 요소의 `::marker` 지원.
Document Policy, `FetchEvent.handled`, Shadow DOM Distribution API, `ParentNode.replaceChildren()` 지원.
또, Origin Trial로서 WebHID API, Window placement API, `<meta name="battery-savings">` 등 지원.
그 외로 FTP 지원이 비권장 됐다.

- [window-placement/EXPLAINER.md at master · webscreens/window-placement](https://github.com/webscreens/window-placement/blob/master/EXPLAINER.md "window-placement/EXPLAINER.md at master · webscreens/window-placement")
- [battery-savings/explainer.md at master · chrishtr/battery-savings](https://github.com/chrishtr/battery-savings/blob/master/explainer.md "battery-savings/explainer.md at master · chrishtr/battery-savings")

----

## Underscore.js
[underscorejs.org/#1.11.0](https://underscorejs.org/#1.11.0 "Underscore.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

underscore 1.10.0 릴리스.
각 함수를 별도의 ES Modules로 작성하고 ES Modules의 엔트리포인트로 `underscore-esm.js`가 추가됐다.
`_.isArrayBuffer`, `_.isDataView`, `_.isTypedArray`가 추가됐고 `_.flatten`에서 깊이를 지정할 수 있는 두 번재 인수를 지원한다.


----

## Update on Adobe Flash Player End of Support - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2020/09/04/update-adobe-flash-end-support/](https://blogs.windows.com/msedgedev/2020/09/04/update-adobe-flash-end-support/ "Update on Adobe Flash Player End of Support - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">flash</span> <span class="jser-tag">news</span></p>

MSEdge는 Flash Player를 2021년 1월 Edge 88에서 삭제할 예정.
이 삭제 계획은 Chromium에 맞춘 것으로 보인다.

- [Flash Roadmap - The Chromium Projects](https://www.chromium.org/flash-roadmap#TOC-Flash-Support-Removed-from-Chromium-Target:-Chrome-88---Jan-2021- "Flash Roadmap - The Chromium Projects")

----
<h1 class="site-genre">아티클</h1>

----

## Minimal React: getting started with the frontend library
[2ality.com/2020/08/minimal-react.html](https://2ality.com/2020/08/minimal-react.html "Minimal React: getting started with the frontend library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

snowpack, react, htm, immer를 이용해 설명하는 React 튜토리얼.


----

## Introducing: Modern Web
[modern-web.dev/blog/introducing-modern-web/](https://modern-web.dev/blog/introducing-modern-web/ "Introducing: Modern Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span> <span class="jser-tag">testing</span></p>

웹 개발 범용 도구와 가이드를 개발하는 Modern Web 프로젝트 소개.
먼저 Web Test Runner라는 브라우저를 사용한 테스트 도구를 릴리스하고 있다.
향후 Web Dev Server와 같은 개발용 서버나 개발 가이드 등도 추가해 나갈 것으로 보인다.

- [modernweb-dev/web: Guides, tools and libraries for modern web development.](https://github.com/modernweb-dev/web "modernweb-dev/web: Guides, tools and libraries for modern web development.")

----

## Introducing Modular Underscore—Julian Gonggrijp
[juliangonggrijp.com/article/introducing-modular-underscore.html](https://juliangonggrijp.com/article/introducing-modular-underscore.html "Introducing Modular Underscore—Julian Gonggrijp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

underscore 1.11.0의 ES Modules 이전과 해당 모듈을 이용하는 방법 소개.
기존(모노리틱) 사용 방법과 ES Modules 사용 방법, 빌드 크기 최적화, Underscore 2.0에 대해서 이야기한다.


----

## Browsers may throttle requestAnimationFrame
[mattperry.is/writing-code/browsers-may-throttle-requestanimationframe-to-30fps](https://mattperry.is/writing-code/browsers-may-throttle-requestanimationframe-to-30fps "Browsers may throttle requestAnimationFrame")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">article</span></p>

`requestAnimationFrame`의 프레임 레이트가 브라우저에 의해 억제되는 경우를 소개.
iOS의 low-power mode, Safari의 cross-origin iframes 조건 아래에 억제되는 경우를 설명,
또, Firefox에서 `performance.now()`의 정밀도가 떨어지는 부분과 cross-origin isolate에 대해서도 언급하고 있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## andnp/SimplyTyped: yet another Typescript type library for advanced types
[github.com/andnp/SimplyTyped](https://github.com/andnp/SimplyTyped "andnp/SimplyTyped: yet another Typescript type library for advanced types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScript 타입 유틸리티 라이브러리.
타입 정의 보조와 런타임 보조 함수 등을 제공한다.


----

## mizchi/minlink: Minimum(> 1kb) and isomorphic worker wrapper with comlink like rpc.
[github.com/mizchi/minlink](https://github.com/mizchi/minlink "mizchi/minlink: Minimum(> 1kb) and isomorphic worker wrapper with comlink like rpc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Web Worker / Node.js의 `worker_thread`에서 RPC를 하기 위한 라이브러리.
comlink 처럼 함수를 호출해 `postMessage`를 주고받는다.

- [minlink - browser/node에서 사용할 수 있는 Worker 랩퍼 - mizdev](https://mizchi.dev/202009061729-minlink-and-minify-tech "minlink - browser/node에서 사용할 수 있는 Worker 랩퍼 - mizdev")(일본어)

----
<h1 class="site-genre">도서</h1>

----

## 이 책에 대해서 · JavaScript Plugin Architecture
[azu.github.io/JavaScript-Plugin-Architecture/](https://azu.github.io/JavaScript-Plugin-Architecture/ "이 책에 대해서 · JavaScript Plugin Architecture")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">plugin</span> <span class="jser-tag">book</span></p>

JavaScript의 플러그인 아키텍처를 주제로 한 작은 크기의 책.
jQuery, ESLint, Connect, gulp, Redux의 플러그인 구조를 구현하면서 이해할 수 있도록 소개.

- [Release v2.0.0 · azu/JavaScript-Plugin-Architecture](https://github.com/azu/JavaScript-Plugin-Architecture/releases/tag/v2.0.0 "Release v2.0.0 · azu/JavaScript-Plugin-Architecture")

----

## Release 2.0.0: ECMAScript 2020 대응 · asciidwango/js-primer
[github.com/asciidwango/js-primer/releases/tag/v2.0.0](https://github.com/asciidwango/js-primer/releases/tag/v2.0.0 "Release 2.0.0: ECMAScript 2020対応 · asciidwango/js-primer")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript 입문서 JavaScript Primer 2.0.0 릴리스.
ES2020의 `String.prototype.matchAll`, `globalThis`, BigInt, Nullish coalescing(`??`), Optional chainin（`?.`） 대응.

- [JavaScript Primer 2.0 - ECMAScript 2020에 대응한 입문서를 공개했습니다 | Web Scratch](https://efcl.info/2020/09/01/jsprimer-2.0/ "JavaScript Primer 2.0 - ECMAScript 2020에 대응한 입문서를 공개했습니다 | Web Scratch")(일본어)

----
