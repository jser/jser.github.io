---
title: "2019-10-09: Preact X(10), webhint browser extension v1, TypeScript 3.7β"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-10-09T00:17:09.603Z
category: JSer
tags:
- Preact
- webhint
- typescript

---

JSer.info #456 - React와 호환되는 API를 제공하는 Preact X(10.0.0)가 릴리스됐습니다.
Preact 9.x는 건너뛰고 Preact 10.x로 릴리스됐습니다.

- [Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact](https://github.com/preactjs/preact/releases/tag/10.0.0)
- [What's new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/whats-new/)

Preact X에서는 Fragments, componentDidCatch, Hooks(`preact/hooks`), createContext, CSS Custom Properties 대응 등이 포함됐습니다.
[Hooks](https://preactjs.com/guide/v10/hooks/)는 Preact의 코어에는 포함돼 있지 않으며 `preact/hooks`또는 `preact/compat`로 가져와 사용하는 방식으로 지원합니다.

또, 지금까지는 별개의 모듈로 돼 있던 `preact-compat`를 [`preact/compat`](https://preactjs.com/guide/v10/switching-to-preact)라는 형식으로 가져올 수 있도록 변경됐습니다.

```js
// Preact 8.x
import React from "preact-compat";

// Preact X
import React from "preact/compat";
```

이어서 이제 preact 내에서 default export를 이용하지 않기 때문에 named import로 가져와 사용해야 합니다.

```js
// Preact 8.x
import Preact from "preact";

// Preact X
import * as preact from "preact";

// Preferred: Named exports (works in 8.x and Preact X)
import { h, Component } from "preact";
```

Preact 8.x에서 10.x으로의 마이그레이션 가이드도 공개됐으니 함께 살펴보면 좋을 것 같습니다.

- [Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/upgrade-guide/)

----

웹 사이트 용 검사 도구인 [webhint](https://webhint.io/)의 브라우저 확장판이 v1이 됐습니다.

- [Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/#U2qsHqfdpdTkuKGc.97)

[beta 버전](https://medium.com/webhint/announcing-the-webhint-browser-extension-abb22f4cfeb)에 MDN browser compat data를 사용한 크로스 브라우저 호환 정보와 컬러 콘트라스트(color contrast)에 대한 힌트 정보가 추가됐습니다.

Chrome(lighthouse)의 Audit과의 차이점으로는 webhint는 크로스 브라우저와 관한 검사를 주로 다룬다고 이야기하고 있습니다.

> The webhint extension doesn’t replace the existing audits tab you’ll find in the developer tools for Chrome and the new Chromium-based Edge browser. While there is a little overlap in the information provided, webhint and Lighthouse serve different purposes, and you may find yourself using both. One distinguishing feature of webhint that it’s meant to provide cross-browser insights, including compatibility with Safari, IE, Opera, and so on.
> -- https://medium.com/webhint/announcing-the-webhint-browser-extension-abb22f4cfeb

----


TypeScript 3.7 Beta가 릴리스됐습니다.

- [Announcing TypeScript 3.7 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/)
- [TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352)

ECMAScript의 Stage 3 Proposal인 [Optional Chaining](https://github.com/tc39/proposal-optional-chaining)과 [Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing)가 지원됩니다.
또, `asserts`에 의해 조작 흐름 제어를 할 수 있는 Assertion Functions이 지원됩니다.
그 외로 `--declaration`와 `--allowJs`를 조합해 사용할 수 있도록 지원합니다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.0.0](https://github.com/preactjs/preact/releases/tag/10.0.0 "Release Preact X - Virtuous DOM and the Fragments of Suspense · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact X(10.0.0)가 릴리스됐습니다.
`Fragments`, `componentDidCatch`, `createContext`와 Hooks API를 지원합니다.

- [What's new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/whats-new/ "What&#x27;s new in Preact X | Preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.")
- [Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.](https://preactjs.com/guide/v10/upgrade-guide/ "Upgrading from Preact 8.x | Preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.")

----

## Release v3.2.0 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v3.2.0](https://github.com/facebook/create-react-app/releases/tag/v3.2.0 "Release v3.2.0 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 3.2.0이 릴리스됐습니다.
`yarn build --profile`로 production build에 대한 프로파일을 대응하고 `TSC_COMPILE_ON_ERROR`를 지원합니다.


----

## vuejs/vue-next
[github.com/vuejs/vue-next](https://github.com/vuejs/vue-next "vuejs/vue-next")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Github</span> <span class="jser-tag">news</span></p>

Vue v3 릴리스 후보의 소스 코드가 공개됐습니다.

----

## Announcing TypeScript 3.7 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7-beta/ "Announcing TypeScript 3.7 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.7 Beta이 릴리스됐습니다.
Optional Chaining, Nullish Coalescing, Assertion Functions을 지원하며 `--declaration`과 `--allowJs`를 조합할 수 있도록 지원합니다. 또,  TypeScript 파일 내에서 시맨틱 검사를 비활성화할 수 있는 `// @ts-nocheck` 주석이 추가됐습니다.

- [TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/33352 "TypeScript 3.7 Iteration Plan · Issue #33352 · microsoft/TypeScript")

----

## Release v5.5.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v5.5.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.5.0 "Release v5.5.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Chrome</span></p>

Lighthouse 5.5.0이 릴리스됐습니다.
Largest Contentful Paint(LCP)를 지원합니다.


----

## Version 1.0 released : Node-RED
[nodered.org/blog/2019/09/30/version-1-0-released](https://nodered.org/blog/2019/09/30/version-1-0-released "Version 1.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">IoT</span> <span class="jser-tag">ReleaseNote</span></p>

플로우 기반의 비쥬얼 데이터를 사용해 Node.js에서 동작하는 프로그램을 작성할 수 있는 툴킷인 Node-RED 1.0이 릴리스됐습니다.


----

## Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/](https://blogs.windows.com/msedgedev/2019/09/30/announcing-the-webhint-v1-browser-extension-for-microsoft-edge/ "Announcing the webhint v1 browser extension for Microsoft Edge - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Extension</span> <span class="jser-tag">accessibility</span></p>

webhint browser extension 1.0.0이 릴리스됐습니다.
플러그인으로 커스터마이즈 할 수 있는 웹 사이트 용 검사 도구의 브라우저 확장판입니다.
이번 버전에서 MDN browser compat data를 사용한 크로스 브라우저 호환성 정보와 컬러 콘트라스트(color contrast)에 대한 힌트가 추가됐습니다.

- [webhint, the hinting engine for web best practices](https://webhint.io/ "webhint, the hinting engine for web best practices")
- [webhint browser extension](https://medium.com/webhint/the-webhint-browser-extension-v1-release-df9044ddaf69)

----
<h1 class="site-genre">아티클</h1>

----

## I created the exact same app in React and Vue. Here are the differences. \[2019 Edition\]
[medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-2019-edition-42ba2cab9e56](https://medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-2019-edition-42ba2cab9e56 "I created the exact same app in React and Vue. Here are the differences. \[2019 Edition\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

React와 Vue를 Todo 애플리케이션으로 각 스타일을 비교 글입니다.
React Hooks에 대응해 수정된 버전입니다.


----

## Fixing layout instability  |  web.dev
[web.dev/fixing-layout-instability/](https://web.dev/fixing-layout-instability/ "Fixing layout instability  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`PerformanceObserver`로 Cumulative Layout Shift (CLS)를 측정해, 얼마나 레이아웃이 발생하는지 WebPageTest로 확인하는 방법이 소개돼 있습니다.
또, 플레이스홀더 데이터를 사용해 불안정한 레이아웃(layout instability)를 수정하는 실제 방법도 함께 다루고 있습니다.

- [Measuring Cumulative Layout Shift (CLS) in WebPageTest - DEV Community 👩‍💻👨‍💻](https://dev.to/chromiumdev/measuring-cumulative-layout-shift-cls-in-webpagetest-5cle "Measuring Cumulative Layout Shift (CLS) in WebPageTest - DEV Community 👩‍💻👨‍💻")

----

## How to read a Web Page Test waterfall chart - Frontend Web Developer, Oxfordshire, UK - Matt Hobbs
[nooshu.github.io/blog/2019/10/02/how-to-read-a-wpt-waterfall-chart/](https://nooshu.github.io/blog/2019/10/02/how-to-read-a-wpt-waterfall-chart/ "How to read a Web Page Test waterfall chart - Frontend Web Developer, Oxfordshire, UK - Matt Hobbs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

WebPageTest의 폭포수 차트를 읽는 방법이 소개돼 있습니다.
스크린샷을 이용해 각 요소를 설명하고 HTTP/1.1과 HTTP/2에서의 흐름 차이 등에 대해 작성돼 있습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Accessibility Support
[a11ysupport.io/](https://a11ysupport.io/ "Accessibility Support")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">webservice</span> <span class="jser-tag">WAI-ARIA</span></p>

스크린리더기 별 WAI-ARIA 등의 접근성 요소 지원 현황에 대해서 정리돼 있는 사이트입니다. 
Can I Use...의 접근성 버전이라고 볼 수 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## cevek/ttypescript: Over TypeScript tool to use custom transformers in the tsconfig.json
[github.com/cevek/ttypescript](https://github.com/cevek/ttypescript "cevek/ttypescript: Over TypeScript tool to use custom transformers in the tsconfig.json")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">plugin</span></p>

TypeScript 컴파일 간 플러그인으로 관련 변환 처리를 추가할 수 있도록 구현한 컴파일러입니다.

----

## algolia/shipjs: Take control of what is going to be your next release.
[github.com/algolia/shipjs](https://github.com/algolia/shipjs "algolia/shipjs: Take control of what is going to be your next release.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">CI </span></p>

릴리스 준비 및 시행하는 도구입니다.
semantic-release와는 다르게 모든것을 자동으로 시행하는게 아니라 Pull Request를 작성해 수동으로 확인하거나 CHANGELOG를 갱신하고 난 후에 릴리스를 시행하는 과정을 갖을 수 있습니다.

----

## fengyuanchen/cropperjs: JavaScript image cropper.
[github.com/fengyuanchen/cropperjs](https://github.com/fengyuanchen/cropperjs "fengyuanchen/cropperjs: JavaScript image cropper.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Image Cropper 라이브러리입니다.
이미지 오려내기, 회전, 이동이 가능한 이미지 가공 라이브러리입니다.


----

## Bin-Huang/prray: "Promisified" Array, comes with async method supports(such as mapAsync). And it is compatible with normal array.
[github.com/Bin-Huang/prray](https://github.com/Bin-Huang/prray "Bin-Huang/prray: \"Promisified\" Array, comes with async method supports(such as mapAsync). And it is compatible with normal array.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

콜백 함수로 비동기 함수를 전달할 수 있는 Array 구현 라이브러리입니다.  


----
