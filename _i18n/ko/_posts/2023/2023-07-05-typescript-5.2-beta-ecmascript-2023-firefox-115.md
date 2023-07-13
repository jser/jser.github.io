---
title: "2023-07-05: TypeScript 5.2 Beta, ECMAScript 2023, Firefox 115"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-07-05T06:01:57.428Z
category: JSer
tags:
- TypeScript
- ECMAScript
- browser
- node.js
- game

---

JSer.info #650 - TypeScript 5.2 Beta가 출시되었습니다.

- [Announcing TypeScript 5.2 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/)

Stage 3 Proposal의 Explicit Resource Management(`using` 선언) 지원, 그리고 같은 Stage 3의 Decorator Metadata 지원됩니다.
또, Tuple에 의한 라벨 유무 조합 제한 삭제, 배열 Union타입 개선도 있습니다.

---

ECMAScript 2023가 ecma GA으로 승인되어 정식 출시되었습니다.

- [Ecma International approves new standards - Ecma International](https://www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/)
- [Release ES2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023)

주 변경점은 이하와 같습니다.

- Proposal: [Hashbang Grammar](https://github.com/tc39/proposal-hashbang)
- 대응 브라우저: [모던 브라우저 전부](https://caniuse.com/mdn-javascript_grammar_hashbang_comments)

```js
#!test
// #! as single line commen터
```


- Proposal: [Change Array by copy](https://github.com/tc39/proposal-change-array-by-copy)
- 대응 브라우저: 모던 브라우저 전부
  - Firefox 115부터 지원

```js
const sequence = [1, 2, 3];
sequence.toReversed(); // => [3, 2, 1]
sequence; // => [1, 2, 3]

const outOfOrder = new Uint8Array([3, 1, 2]);
outOfOrder.toSorted(); // => Uint8Array [1, 2, 3]
outOfOrder; // => Uint8Array [3, 1, 2]

const correctionNeeded = [1, 1, 3];
correctionNeeded.with(1, 2); // => [1, 2, 3]
correctionNeeded; // => [1, 1, 3]
```

- Proposal: [Array.prototype.findLast and Array.prototype.findLastIndex](https://github.com/tc39/proposal-array-find-from-last)
- 대응 브라우저: [모던 브라우저 전부](https://caniuse.com/?search=Array.prototype.findLast)

```js
const array = [{ value: 1 }, { value: 2 }, { value: 3 }, { value: 4 }];
array.findLastIndex(n => n.value % 2 === 1); // => 2
array.findLast(n => n.value % 2 === 1); // => { value: 3 }
```

- Proposal: [Symbols as WeakMap keys](https://github.com/tc39/proposal-symbols-as-weakmap-keys)
- 대응 브라우저: [Firefox 이외](https://caniuse.com/mdn-javascript_builtins_weakmap_symbol_as_keys)


```js
const map = new WeakMap();
const s = Symbol("desc");
map.set(s, {})
map.get(s); // => {}
```

---

Firefox 115가 출시되었습니다.

- [Firefox 115.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/115.0/releasenotes/)
- [Firefox 115 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/115)

macOS 10.12/10.13/10.14, Windows7/8/8.1 지원되는 마지막 버전입니다.
`contenteditable`으로 노드 분석과 결합 동작이 다른 브라우저와 같도록 변경.
`Array.fromAsync()` 지원, ES2023 `Array.toReversed()`/`.toSorted()`/`.toSpliced()`/`.with()` 지원.
`Response.json()`, `URL.canParse()` 지원.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v8.0.0-alpha.0 · pixijs/pixijs
[github.com/pixijs/pixijs/releases/tag/v8.0.0-alpha.0](https://github.com/pixijs/pixijs/releases/tag/v8.0.0-alpha.0 "Release v8.0.0-alpha.0 · pixijs/pixijs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

PixiJS v8.0.0-alpha.0 출시.
WebGPU 렌더러와 WebGL 렌더러 재작성, 변경된 것만 갱신하는 리엑티브 렌더러, 수준 높은 Blend 모드 추가.
초기화 방법을 비동기로 변경, Graphics API 리뉴얼


----

## ESLint v8.44.0 released - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2023/06/eslint-v8.44.0-released/](https://eslint.org/blog/2023/06/eslint-v8.44.0-released/ "ESLint v8.44.0 released - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v8.44.0 출시.
`eslint.config.js`으로 Promise 허용하는 것으로 설정 파일(CJS)에서 ESM를 로드할 수 있도록, espree가 RegExp의 `v` 플러그 지원.
`context.parserServices` 프로퍼티 비권장화


----

## Announcing TypeScript 5.2 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-2-beta/ "Announcing TypeScript 5.2 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.2 Beta 출시.
Stage 3 Proposal Explicit Resource Management(`using` 선언) 지원, Decorator Metadata 지원.
Tuple에 의한 라벨 유무 조합 제한 삭제, 배열 Union 타입 개선


----

## Ecma International approves new standards - Ecma International
[www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/](https://www.ecma-international.org/news/ecma-international-approves-new-standards-at-the-125th-general-assembly-27-june-2023/ "Ecma International approves new standards - Ecma International")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2023가 ecma GA 승인되어 정식 출시.

- [Release ES2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023 "Release ES2023 · tc39/ecma262")

----

## Release v4.0.0 · lquixada/cross-fetch
[github.com/lquixada/cross-fetch/releases/tag/v4.0.0](https://github.com/lquixada/cross-fetch/releases/tag/v4.0.0 "Release v4.0.0 · lquixada/cross-fetch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

cross-fetch 4.0.0 출시.
Node.js 10랑 12 지원 종료, Node.js 18와 20 지원, Service Worker와 Cloudflare Workers 지원


----

## Release v8.6.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v8.6.6](https://github.com/pnpm/pnpm/releases/tag/v8.6.6 "Release v8.6.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">performance</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v8.6.6 출시.
성능 개선


----

## Release v29.6.0 · jestjs/jest
[github.com/jestjs/jest/releases/tag/v29.6.0](https://github.com/jestjs/jest/releases/tag/v29.6.0 "Release v29.6.0 · jestjs/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jest</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Jest 29.6.0 출시.
Current Test에서 snapshot테스트 지원, 비동기로 에러가 throw된 경우 문제를 `rejectionHandled` 이벤트로 사용으로 수정


----

## Release 0.2.5 · web-infra-dev/rspack
[github.com/web-infra-dev/rspack/releases/tag/0.2.5](https://github.com/web-infra-dev/rspack/releases/tag/0.2.5 "Release 0.2.5 · web-infra-dev/rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span></p>

rspack 0.2.5 출시.
Web Worker 지원, entry `filename` 옵션 지원, HMR으로 CJS와 ESM가 혼재된 경우에 warning 보이도록


----

## Firefox 115.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/115.0/releasenotes/](https://www.mozilla.org/en-US/firefox/115.0/releasenotes/ "Firefox 115.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 115 출시.
macOS 10.12/10.13/10.14, Windows7/8/8.1 지원하는 마지막 버전.
`contenteditable`으로 노드 분할과 결합 동작을 다른 브라우저와 같도록 변경.
` Array.fromAsync()` 지원, ES2023 `Array.toReversed()`/`.toSorted()`/`.toSpliced()`/`.with()` 지원.
`Response.json()`, `URL.canParse()` 지원.

- [Firefox users on macOS 10.12, 10.13 and 10.14 moving to Extended Support Release | Firefox 헬프](https://support.mozilla.org/ja/kb/firefox-users-macos-1012-1013-1014-moving-to-extended-support "Firefox users on macOS 10.12, 10.13 and 10.14 moving to Extended Support Release | Firefox 헬프")
- [Firefox users on Windows 7, 8 and 8.1 moving to Extended Support Release | Firefox 헬프](https://support.mozilla.org/ja/kb/firefox-users-windows-7-8-and-81-moving-extended-support "Firefox users on Windows 7, 8 and 8.1 moving to Extended Support Release | Firefox 헬프")
- [Firefox 115 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/115 "Firefox 115 for developers - Mozilla | MDN")
- [Intent to Ship: Compatible join and split node direction in HTML editor](https://groups.google.com/a/mozilla.org/g/dev-platform/c/Ob-T1HSe-4I?pli=1 "Intent to Ship: Compatible join and split node direction in HTML editor")

----
<h1 class="site-genre">읽을거리</h1>

----

## CommonJS is not going away | Bun Blog
[bun.sh/blog/commonjs-is-not-going-away](https://bun.sh/blog/commonjs-is-not-going-away "CommonJS is not going away | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">article</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span></p>

Bun가 CommonJS 지원하는 이유는 무엇인가.
CommonJS와 ECMAScript Module 비교해보면 동기와 비동기 차이가 있어서 기동할 때 로드 시간이 달라서, 이미 많은 CommonJS 모듈이 많아서

- [CommonJS is hurting JavaScript](https://deno.com/blog/commonjs-is-hurting-javascript "CommonJS is hurting JavaScript")

----

## Useful DevTools Tips and Tricks — Smashing Magazine
[www.smashingmagazine.com/2023/06/popular-devtools-tips/](https://www.smashingmagazine.com/2023/06/popular-devtools-tips/ "Useful DevTools Tips and Tricks — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">debug</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

브라우저 개발자 도구 Tips 모아둔 글


----

## Architecture of an early stage SAAS | Feelback Blog
[www.feelback.dev/blog/feelback-saas-launch-architecture/](https://www.feelback.dev/blog/feelback-saas-launch-architecture/ "Architecture of an early stage SAAS | Feelback Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">article</span> <span class="jser-tag">node.js</span></p>

fly.io와 Node.js를 사용한 SaaS 아키텍처 해설.
fly.io 사용한 낮은 비용 인프라 구성.
클라이언트와 서버 모두 Node.js, 타입 있는 RPC로써 httpc 이용.
관리화면은 Cloudflare Pages에 있으며 httpc 사용한 통신, 홈페이지나 문서에는 Astro 이용중이다.
또한 이용하고 있는 외부 서비스나 monorepo 구성 설명도 있다.

- [httpc: function-based API made easy](https://httpc.dev/ "httpc: function-based API made easy")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## giuseppelt/httpc: Build function-based API with minimal code and end-to-end type safety
[github.com/giuseppelt/httpc](https://github.com/giuseppelt/httpc "giuseppelt/httpc: Build function-based API with minimal code and end-to-end type safety")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

TypeScript로 작성된 서버 함수를 클라이언트에서도 똑같이 호출할 수 있는 RPC 툴킷.
서버에서 함수를 export한 코드에서 클라이언트 코드를 생성하는 구조로, 서버함수롸 같은 함수와 인수를 API  호출 가능하다.


----
