---
title: "2022-03-08: TypeScript 4.6, Chrome 100 beta, 새로운 MDN"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-03-08T03:17:40.310Z
category: JSer
tags:
- TypeScript
- React
- node.js
- webpack
- bundler

---

JSer.info #582 - TypeScript 4.6가 릴리스 됐다.

- [Announcing TypeScript 4.6 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/)

TypeScript 4.6에서는 Destructuring과 Union의 조합, 재귀 타입, 인터페이스에 대한 인덱스 접근 등에 대한 타입 추론 기능이 개선됐다.
또, `--target es2022`를 지원하고 `checkJs` 유효할 때에 수행하는 자바스크립트 문법 에러 검사 기능이 개선됐다.

다음 4.7에서는 [TypeScript 4.5](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-rc/)에서 보류됐던 Node.js ESM 대응이 진행될 예정이다.

- [TypeScript 4.7 Iteration Plan · Issue #48027 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/48027)

---

Chrome 100 beta가 릴리스 됐다.

- [Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More](https://blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html)

버전이 `100` 즉, 세 자리가 됐기 때문에 Chrome과 Firefox에서 문제가 발생하는 사이트가 있을 것으로 예상되고 있다.

- [Version 100 in Chrome and Firefox - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/02/version-100-in-chrome-and-firefox/)

또, Chrome 100 beta에서 User-Agent에서 정보를 삭제하거나 고정시키는 과정(단계 3)에 들어간다.
Chrome 100이 본격적으로 UA 문자열을 정리하기 전의 마지막 버전이며 101부터 단계적으로 UA 문자열을 정리하는 단계에 돌입한다.

- [Chromium Blog: User-Agent Reduction Origin Trial and Dates](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html)
- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)

그 외로 멀티 스크린 시에 어디에 Window를 표시할지를 지정할 수 있는 Multi-Screen Window Placement API 등이 추가 됐다.

- [Managing several displays with the Multi-Screen Window Placement API](https://web.dev/multi-screen-window-placement/)

---

[MDN Web Docs](https://developer.mozilla.org)(MDN)의 디자인이나 로고 등이 개편됐다.
또, MDN Plus라고 하는 구독하여 알람이나 추가 컨텐츠를 받을 수 있는 유료 기능이 공개될 예정이라고 한다.
자세한 내용은 아래 문서를 참고하길 바란다.

- [A new year, a new MDN - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v5.70.0 · webpack/webpack
[github.com/webpack/webpack/releases/tag/v5.70.0](https://github.com/webpack/webpack/releases/tag/v5.70.0 "Release v5.70.0 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack v5.70.0 릴리스.
ESM의 `require.context`에 해당하는 기능으로 `import.meta.webpackContext` 추가.
ESM 지원 대상에 Node.js 12를 추가.

----

## Release v0.14.24 · evanw/esbuild
[github.com/evanw/esbuild/releases/v0.14.24](https://github.com/evanw/esbuild/releases/v0.14.24 "Release v0.14.24 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.14.24 릴리스.
target으로 `es2022` 지원, `define` 옵션으로 인덱스를 지정한 경우에도 치환 가능하도록 개선, `--mangle-quoted` 옵션 추가.


----

## Release Notes for Safari Technology Preview 141 | WebKit
[webkit.org/blog/12434/release-notes-for-safari-technology-preview-141/](https://webkit.org/blog/12434/release-notes-for-safari-technology-preview-141/ "Release Notes for Safari Technology Preview 141 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 141 릴리스.
CSS `overflow: clip` 활성화, import assertion 구문을 플래그 붙여 구현, CSP의 `wasm-unsafe-eval` 구현 등.


----

## Announcing TypeScript 4.6 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-6/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-6/ "Announcing TypeScript 4.6 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.6 릴리스.
Destructuring과 Union의 조합, 재귀 타입, 인터페이스에 대한 인덱스 접근 등에 대한 타입 추론 개선.
함수 매개 변수의 제어 흐름에 따른 타입 추론 개선.
`--target es2022` 지원, `checkJs`가 유효할 때에 수행하는 자바스크립트 문법 에러 검사 기능 개선.


----

## Release v28.0.0-alpha.7 · facebook/jest
[github.com/facebook/jest/releases/tag/v28.0.0-alpha.7](https://github.com/facebook/jest/releases/tag/v28.0.0-alpha.7 "Release v28.0.0-alpha.7 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">ReleaseNote</span></p>

Jest v28.0.0-alpha.7 릴리스.
여러개의 머신으로 테스트를 분할하여 실행할 수 있는 `--shared` 플래그 구현.

- [feat: implement \`--shard\` option by marionebl · Pull Request #12546 · facebook/jest](https://github.com/facebook/jest/pull/12546 "feat: implement \&#x60;--shard\&#x60; option by marionebl · Pull Request #12546 · facebook/jest")

----

## Release v6.0.0-alpha.0 · styled-components/styled-components
[github.com/styled-components/styled-components/releases/tag/v6.0.0-alpha.0](https://github.com/styled-components/styled-components/releases/tag/v6.0.0-alpha.0 "Release v6.0.0-alpha.0 · styled-components/styled-components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

styled-components v6.0.0-alpha.0 릴리스.
TypeScript로 재작성, stylis v4로 업데이트, Node.js 14 미만 지원 종료.

- [\[breaking\] stylis v4 by probablyup · Pull Request #3241 · styled-components/styled-components](https://github.com/styled-components/styled-components/pull/3241 "\[breaking\] stylis v4 by probablyup · Pull Request #3241 · styled-components/styled-components")

----

## Release v10.7.0 · TypeStrong/ts-node
[github.com/TypeStrong/ts-node/releases/tag/v10.7.0](https://github.com/TypeStrong/ts-node/releases/tag/v10.7.0 "Release v10.7.0 · TypeStrong/ts-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">node.js</span></p>

ts-node v10.7.0 릴리스.
`--esm` 플래그와 `ts-node-esm` 바이너리를 추가했다.


----

## Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More
[blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html](https://blog.chromium.org/2022/03/chrome-100-beta-reduced-user-agent.html "Chromium Blog: Chrome 100 Beta: Reduced User-Agent Strings, Multi-Screen Window Placement, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 100 베타 릴리스.
Chrome 100은 UA 문자열 포멧을 정리하기 전의 마지막 버전이다. 101 부터는 UA 문자열을 단계적으로 정리 및 고정해 나갈 예정이다.
Multi-Screen Window Placement API가 추가 됐고 Origin Trial로서 Media Source Extensions을 Worker에서 실행할 수 있도록 됐다.
또, `AbortSignal.prototype.throwIfAborted()`와 `HIDDevice forget()`가 추가됐다.

- [Chromium Blog: User-Agent Reduction Origin Trial and Dates](https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html "Chromium Blog: User-Agent Reduction Origin Trial and Dates")

----
<h1 class="site-genre">아티클</h1>

----

## A new year, a new MDN - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/ "A new year, a new MDN - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">article</span></p>

MDN 디자인과 로고 개편 건 소개.
또, 추가 기능과 추가 컨텐츠를 제공하는 MDN Plus 구독 서비스에 대해서 다루고 있다.

- [MDN Web Docs](https://developer.mozilla.org/ "MDN Web Docs")

----

## Working together on Interop 2022 | WebKit
[webkit.org/blog/12288/working-together-on-interop-2022/](https://webkit.org/blog/12288/working-together-on-interop-2022/ "Working together on Interop 2022 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span> <span class="jser-tag">testing</span> <span class="jser-tag">WebPlatformAPI</span></p>

브라우저의 상호 운용성을 목표로 하는 Interop 2022 프로젝트 소개.
Apple / Google / Microsoft / Mozilla / Bocoup / Igalia 등이 협력하여 프로젝트로 웹 플랫폼에서 주목하고 있는 영역(기술)을 선정, 상호 운용성을 대처한다.
WPT를 사용한 측정 방식이나 선정된 기술 영역을 간단하게 소개하고 있다.

- [web-platform-tests dashboard](https://wpt.fyi/interop-2022 "web-platform-tests dashboard")
- [Interop 2022: browsers working together to improve the web for developers](https://web.dev/interop-2022/ "Interop 2022: browsers working together to improve the web for developers")
- [Microsoft Edge and Interop 2022 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2022/03/03/microsoft-edge-and-interop-2022/ "Microsoft Edge and Interop 2022 - Microsoft Edge Blog")
- [Announcing Interop 2022 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2022/03/interop-2022/ "Announcing Interop 2022 - Mozilla Hacks - the Web developer blog")
- [Bocoup and Interop 2022 - web standards - Bocoup](https://bocoup.com/blog/interop-2022 "Bocoup and Interop 2022 - web standards - Bocoup")
- [Igalia and Interop 2022 | Igalia](https://www.igalia.com/news/interop2022.html "Igalia and Interop 2022 | Igalia")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## nodeshift/nodejs-reference-architecture: The Red Hat and IBM Node.js Reference architecture. The teams &#039;opinion&#039; on what components our customers and internal teams should use when building Node.js applications and guidance for how to be successful in production with those components.
[github.com/nodeshift/nodejs-reference-architecture](https://github.com/nodeshift/nodejs-reference-architecture "nodeshift/nodejs-reference-architecture: The Red Hat and IBM Node.js Reference architecture. The teams &#039;opinion&#039; on what components our customers and internal teams should use when building Node.js applications and guidance for how to be successful in production with those components.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">document</span> <span class="jser-tag">Docker</span></p>

자바스크립트 / Node.js에서 아키텍처, 라이브러리 등을 선정 할 때 참고할 수 있는 정보, 도입 방법 등이 정리돼 있는 일종의 가이드라인 저장소.
Docker와 npm과 관련한 설정, 기술 영역 별로 정리한 라이브러리와 프레임워크,  운용 관련한 로깅과 트레이스 등 꽤 넓은 범위를 나름의 명확한 기준으로 정리돼 있다.

- [Node.js Reference Architecture | Node.JS Reference Architecture](https://nodeshift.dev/nodejs-reference-architecture/ "Node.js Reference Architecture | Node.JS Reference Architecture")

----
<h1 class="site-genre">도서</h1>

----

## 프런트엔드 디자인 패턴(일본어)
[zenn.dev/morinokami/books/learning-patterns-1](https://zenn.dev/morinokami/books/learning-patterns-1 "프런트엔드 디자인 패턴")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">architecture</span> <span class="jser-tag">book</span> <span class="jser-tag">React</span></p>

patterns.dev의 일본어 번역판.
React와 JavaScript에서의 디자인 패턴을 다루고 있다.

- [Patterns.dev - Modern Web App Design Patterns](https://www.patterns.dev/ "Patterns.dev - Modern Web App Design Patterns")

----
