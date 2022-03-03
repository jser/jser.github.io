---
title: "2022-03-01: Redux Toolkit 1.8.0, Node.js 17.6.0, CSS Cascade Layers"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-02-28T12:49:04.690Z
category: JSer
tags:
- node.js
- TypeScript
- Tools
- pnpm
- Chrome

---

JSer.info #581 - Redux Toolkit 1.8.0가 릴리스 됐다.

- [Release v1.8.0 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.8.0)

1.8.0에서 새로운 비동기 Middleware로 `createListenerMiddleware`가 추가됐다.

- [createListenerMiddleware | Redux Toolkit](https://redux-toolkit.js.org/api/createListenerMiddleware)

`createListenerMiddleware`는 [redux-saga](https://github.com/redux-saga/redux-saga)나 [redux-observable](https://redux-observable.js.org/) 등과 같이 비동기 처리를 다루기 위한 Middleware다.
단순한 작업을 다룰 수 있는 `dispatch`나 `getState` 등의 API 뿐 아니라 redux-saga에 영감받은 `take`, [Temporal](https://docs.temporal.io/docs/typescript/workflows#condition)에 영감받은`condition` 등의 API도 제공해 복잡한 작업도 다룰 수 있도록 개선됐다.

아래 영상을 통해 이 `createListenerMiddleware`가 어떻게 만들어졌는지 소개하고 있다.

- [Redux Insights: the Redux Toolkit &quot;action listener&quot; middleware - YouTube](https://www.youtube.com/watch?v=D5WOry6gw9c)
- [New experimental &quot;action listener middleware&quot; package available · Discussion #1648 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/discussions/1648)

---

Node.js 17.6.0가 릴리스 됐다.

- [Node v17.6.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v17.6.0/)

[Node v17.5.0](https://nodejs.org/en/blog/release/v17.5.0/)에서 Streaｍ과 관련된 ECMAScript Proposal Stage 2 단계인 [Iterator Helpers](https://github.com/tc39/proposal-iterator-helpers)가 구현됐다.
하지만, 사양에 근거해 구현할 경우에 [mongoose](https://github.com/Automattic/mongoose/issues/11377) 등의 모듈이 동작하지 않게 되는 회귀가 발생하여 [사양에 근거한 몇 가지 변경 내용을 되돌렸다(revert)](https://github.com/nodejs/node/pull/41931).

- [Regression in Node 17.5, Assigning a function to prototype of an Object results in a TypeError: Cannot assign to read only property 'x' of object 'y' at Object.<anonymous> · Issue #41926 · nodejs/node](https://github.com/nodejs/node/issues/41926)

구체적으로 Iterator Helper의 사양에서는 `map` 등의 메서드를 [`{ [[Writable]]: false, [[Enumerable]]: false, [[Configurable]]: false }`](https://tc39.es/proposal-iterator-helpers/#sec-iterator.prototype)로 구현하도록 돼 있다.

이 경우에 다음과 같이 Stream의 `prototype.map`을 덮어쓰게 되면 `Writable`가 `false`이기 때문에 예외가 발생하므로 불가능하다.

```js
// [Writable]]: false인 경우 덮어쓸 수 없다.
ReadableStream.prototype.map = function(fn) { // 예외가 발생한다.
  // ..
};
```

mongoose 등의 구현부에 이러한 대입이 존재하기 때문에 [`[[Writable]]: false`를 `[[Writable]]: true`로 변경(revert)](https://github.com/nodejs/node/pull/41931)하는 내용이 Node.js 17.6.0에 포함됐다(예상과 다르게 BREAKING CHANGE 사항이 됐기 때문)

mongoose 측에서 이 문제에 대응한 내용은 다음과 같다. 

- [fix Node.js 17.5 compatibility by benjamingr · Pull Request #11381 · Automattic/mongoose](https://github.com/Automattic/mongoose/pull/11381)

----

[A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks](https://css-tricks.com/css-cascade-layers/)에는 Chrome / Edge 99+, Firefox 97+, Safari Technology Preview 133에서 구현된 CSS Cascade Layers가 소개돼 있다.

CSS에는 UA, `!important`, [명시도](https://developer.mozilla.org/ko/docs/Web/CSS/Specificity) 등에 의해 어느 스타일을 적용하는 게 맞는지에 대한 [Cascading 사양](https://drafts.csswg.org/css-cascade/#cascading)이 정해져 있다.
이 사양에 [Cascade Layers](https://www.w3.org/TR/css-cascade-5/#layering)라는 내용이 추가돼 각 브라우저에서 구현이 진행되고 있다.

이 글에는 Cascade Layers의 기본적인 사용 방법, Important layers, Layer 우선도, sub layer 개념 등에 대해 작성돼 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v6.32.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v6.32.0](https://github.com/pnpm/pnpm/releases/tag/v6.32.0 "Release v6.32.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 6.32.0 릴리스.
설치 스크립트를 실행 할 수 있는 패키지를 지정하는 `onlyBuiltDependencies` 추가, `pnpm add` 시 `overrides` 필드 값을 고려하여 패키지 버전이 설정되도록 개선


----

## Astro 0.23 Release Notes | Astro
[astro.build/blog/astro-023/](https://astro.build/blog/astro-023/ "Astro 0.23 Release Notes | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>


주우영 ju uyeong  10:00 AM
Astro 0.23 Release Notes | Astro
Astro 0.23 릴리스.
HTML 이외의 빌드에 대응, `set:html`과 `set:text` 디렉티브 추가, `PUBLIC_` prefix 환경 변수를 프런트엔드에서도 참조할 수 있도록 변경.
다음 버전에서는 컴포넌트 내의 텍스트를 자동으로 HTML 이스케이프 하도록 변경할 예정이다.


----

## Node v17.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.6.0/](https://nodejs.org/en/blog/release/v17.6.0/ "Node v17.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.6.0 릴리스.
Stream 내 Iterator helper의 `map`을 사양을 근거해 변경하니 일부 동작하지 않는 모듈이 발생하여 일시적으로 되돌렸다.
`--experimental-https-modules` 플래그를 붙여서 HTTP URL을 ESM 모듈로 가져올 수 있다.
또, `process.on("multipleResolves", ...)`가 비권장 됐다.

- [stream: add map method to Readable: by benjamingr · Pull Request #40815 · nodejs/node](https://github.com/nodejs/node/pull/40815 "stream: add map method to Readable: by benjamingr · Pull Request #40815 · nodejs/node")

----

## Release v1.8.0 · reduxjs/redux-toolkit
[reduxjs/redux-toolkit/releases/tag/v1.8.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v1.8.0)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v1.8.0-rc.0 릴리스.
새로운 비동기 미들웨어로 `createListenerMiddleware` 추가, `configureStore`의 타입 정의 개선 등.

- [New experimental &amp;quot;action listener middleware&amp;quot; package available · Discussion #1648 · reduxjs/redux-toolkit](https://github.com/reduxjs/redux-toolkit/discussions/1648 "New experimental &amp;amp;quot;action listener middleware&amp;amp;quot; package available · Discussion #1648 · reduxjs/redux-toolkit")

----
<h1 class="site-genre">아티클</h1>

----

## What&#039;s New In DevTools (Chrome 99) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-99/](https://developer.chrome.com/blog/new-in-devtools-99/ "What&#039;s New In DevTools (Chrome 99) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Chrome 99 개발자 도구 변경 사항 정리
WebSockets의 Throttiling에 대응, Reporting API 패널 추가, ANSI escape code를 사용한 콘솔 로그 스타일링 지원 등.


----

## How to publish Deno modules to NPM
[deno.com/blog/dnt-oak](https://deno.com/blog/dnt-oak "How to publish Deno modules to NPM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

Deno로 작성된 라이브러리를 Node.js 용으로 npm에 공개하는 방법 소개.
HTTP 프레임워크인 oak과 dnt를 사용해 Node.js에서도 동작하도록 변환하여 공개하는 방법이 작성돼 있다.

- [denoland/dnt: Deno to npm package build tool.](https://github.com/denoland/dnt/ "denoland/dnt: Deno to npm package build tool.")
- [feat: add experimental support for Node.js by kitsonk · Pull Request #479 · oakserver/oak](https://github.com/oakserver/oak/pull/479 "feat: add experimental support for Node.js by kitsonk · Pull Request #479 · oakserver/oak")

----

## A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks
[css-tricks.com/css-cascade-layers/](https://css-tricks.com/css-cascade-layers/ "A Complete Guide to CSS Cascade Layers | CSS-Tricks - CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Cascade Layers를 소개하는 글.
Cascade Layers의 기본적인 사용 장법, Important layers, Layer의 우선도, sub layer 등에 대해서 소개한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## microsoft/TypeScript-Compiler-Notes: A repo containing notes about the TypeScript Compiler codebase
[github.com/microsoft/TypeScript-Compiler-Notes](https://github.com/microsoft/TypeScript-Compiler-Notes "microsoft/TypeScript-Compiler-Notes: A repo containing notes about the TypeScript Compiler codebase")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">document</span></p>

TypeScript의 컴파일러에 대한 메모를 정리한 저장소.
주요한 변경 사항을 담은 PR 정리, 콤파일러 프로세스 설명, Contribute 하는 방법 등을 다루고 있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## JoshuaKGoldberg/TypeStat: Converts JavaScript to TypeScript and TypeScript to better TypeScript.
[github.com/JoshuaKGoldberg/TypeStat](https://github.com/JoshuaKGoldberg/TypeStat "JoshuaKGoldberg/TypeStat: Converts JavaScript to TypeScript and TypeScript to better TypeScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

JavaScript 코드에 TypeScript의 타입을 부여하여 TypeScript 코드 베이스로 변환해주는 도구


----

## xataio/screenshot: A zero-dependency browser-native way to take screenshots powered by the native web MediaDevices API.
[github.com/xataio/screenshot](https://github.com/xataio/screenshot "xataio/screenshot: A zero-dependency browser-native way to take screenshots powered by the native web MediaDevices API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Image</span> <span class="jser-tag">browser</span></p>

`MediaDevices.getDisplayMedia`를 사용해 개발한 스크린샷 라이브러리.
출력된 화면을 이미지로 캡처해 얻을 수 있다.

- [Xata | New Open Source Library: Announcing @xata.io/screenshot](https://www.xata.io/blog/introducing-screenshot/ "Xata | New Open Source Library: Announcing @xata.io/screenshot")

----

## leafac/caxa: 📦 Package Node.js applications into executable binaries 📦
[github.com/leafac/caxa](https://github.com/leafac/caxa "leafac/caxa: 📦 Package Node.js applications into executable binaries 📦")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

Node.js 애플리케이션을 단일 실행 라이브러리로 패키징하는 도구.
Node.js와 애플리케이션을 담은 자기 풀림 타입 압축(SFX, self-extract format archive)로서 다뤄 `fs` 등의 patch 없이 패키징 하고 있다.


----
<h1 class="site-genre">도서</h1>

----

## vinodotdev/node-to-rust
[github.com/vinodotdev/node-to-rust/](https://github.com/vinodotdev/node-to-rust/ "vinodotdev/node-to-rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">book</span></p>

JavaScript 개발자를 위한 Rust 입문서


----
