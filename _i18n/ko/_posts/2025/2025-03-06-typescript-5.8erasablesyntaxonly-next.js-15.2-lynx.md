---
title: "2025-03-06: TypeScript 5.8(erasableSyntaxOnly), Next.js 15.2, Lynx"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-03-06T02:01:38.698Z
category: JSer
tags:
- TypeScript
- React
- Native
- ESLint
- css

---

JSer.info #727 - TypeScript 5.8 출시되었습니다.

- [Announcing TypeScript 5.8 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/)

TypeScript 5.8에서는, conditional return type 개선, `require(esm)` 대응, `--module node18` 추가되었습니다
또한, Node.js의 `--experimental-strip-types`와 설정을 조합할 수 있는 `--erasableSyntaxOnly` 플래그 추가, `--libReplacement` 플래그 추가도 있습니다.

[erasableSyntaxOnly](https://www.typescriptlang.org/tsconfig/#erasableSyntaxOnly) 옵션은, 다음 기능 금지하면 자료형 제거만으로도, JavaScript로 실행 가능한 TypeScript 코드 작성할 수 있는 설정입니다.

- enum declarations
- namespaces and modules with runtime code
- parameter properties in classes
- Non-ECMAScript `import =` and `export =` assignments

Node.js의 Type Stripping 관련해서는, 다음 글 참조 부탁드립니다.

- [Node.js Type Stripping Explained](https://satanacchio.hashnode.dev/everything-you-need-to-know-about-nodejs-type-stripping)

----

Next.js 15.2 출시되었습니다.

- [Next.js 15.2 | Next.js](https://nextjs.org/blog/next-15-2)

Error Overlay 스택트레이스 게시 개선, Dev indicator 개선, `generateMetadata` 처리를 비동기 대응, Turbopack 성능 개선이 있습니다.
또한, 실험적 기능으로 View Transition API 대응, Node.js middleware 지원도 추가되었습니다.

----

[Lynx](https://lynxjs.org/) React/CSS/TypeScript 사용한 네이티브 애플리케이션 개발 툴킷을 ByteDance가 공개했습니다.

Lynx는 React 17의 API와 QuickJS 기반한 [PrimJS](https://github.com/lynx-family/primjs) JavaScript 엔진을 사용합니다.

- [Why is it based on compatibility with React 17?](https://lynxjs.org/api/react/index.html#react-apis)
- [JavaScript Runtime - Lynx](https://lynxjs.org/guide/scripting-runtime/index.html)

 출시 글에는, Instant First-Frame Rendering (IFR)나 Main Thread Script에 관련한 렌더링 최적화에 대해 다루고 있습니다.

- [Lynx: Unlock Native for More - Lynx](https://lynxjs.org/blog/lynx-unlock-native-for-more)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## ArkType Docs: Optimized runtime validation for TypeScript syntax
[arktype.io/docs/blog/2.1](https://arktype.io/docs/blog/2.1 "ArkType Docs: Optimized runtime validation for TypeScript syntax")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ArkType 2.1 출시.
패턴 매치 하는 `match`　API 추가, `configure`으로 키워드에 에러 메세지를 커스터마이즈 가능하도록 함


----

## Release 0.11.0 | StyleX
[stylexjs.com/blog/v0.11.0](https://stylexjs.com/blog/v0.11.0 "Release 0.11.0 | StyleX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

StyleX v0.11.0 출시.
디버그 정보 개선, CLI 캐시 개선


----

## Announcing TypeScript 5.8 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-8/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/ "Announcing TypeScript 5.8 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.8 출시.
conditional return type 개선, `require(esm)` 대응, `--module node18` 추가. Node.js `--experimental-strip-types` 같이 설정하는 `--erasableSyntaxOnly` 플래그 추가, `--libReplacement` 플래그 추가


----

## Release 3.41.0 - 2025.03.01 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.41.0](https://github.com/zloirock/core-js/releases/tag/v3.41.0 "Release 3.41.0 - 2025.03.01 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">ReleaseNote</span></p>

core-js v3.41.0 출시.
Stage 4가 된 `RegExp.escape`/Float16, Stage 1 `Math.clamp` 대응


----

## Next.js 15.2 | Next.js
[nextjs.org/blog/next-15-2](https://nextjs.org/blog/next-15-2 "Next.js 15.2 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 15.2 출시.
Error Overlay 스택트레이스 게시 개선, Dev indicator 개선, `generateMetadata` 처리를 비동기 대응, Turbopack 성능 개선.
실험적 기능으로 View Transition API 대응, Node.js middleware 지원


----

## Re.Pack 5: Mobile Microfrontends, 5x Faster, Less Configuration - Re.Pack
[re-pack.dev/blog/repack-5-release](https://re-pack.dev/blog/repack-5-release "Re.Pack 5: Mobile Microfrontends, 5x Faster, Less Configuration - Re.Pack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 대상 빌드 도구 Re.Pack 5 출시.
webpack 대신 Rspack 이용, Module Federation 대응


----

## Release pnpm 10.5 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.5.0](https://github.com/pnpm/pnpm/releases/tag/v10.5.0 "Release pnpm 10.5 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.5.0 출시.
`package.json`에 분산된 `pnpm.*` 설정을 `pnpm-workspace.yaml`에 얹도록 변경


----

## Chrome 134  |  Release notes  |  Chrome for Developers
[developer.chrome.com/release-notes/134](https://developer.chrome.com/release-notes/134 "Chrome 134  |  Release notes  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 134 출시.
`<select>` 커스터마이즈 지원, `<dialog>`의 `closedby` 속성 지원, Document-Policy에 `expect-no-linked-resources` 추가.
Shared Storage에서 Web Locks API 지원, Canvas에서 `imageSmoothingQuality` 옵션 지원.
`getUserMedia` 비표준 API 삭제

- [WICG/shared-storage: Explainer for proposed web platform Shared Storage API](https://github.com/WICG/shared-storage "WICG/shared-storage: Explainer for proposed web platform Shared Storage API")

----

## Lynx
[lynxjs.org/](https://lynxjs.org/ "Lynx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span></p>

React 17 기반 API와 JavaScript/TypeScript/CSS 사용한 네이티브 애플리케이션 개발 가능한 툴킷.


----

## Release v8.26.0 · typescript-eslint/typescript-eslint
[github.com/typescript-eslint/typescript-eslint/releases/tag/v8.26.0](https://github.com/typescript-eslint/typescript-eslint/releases/tag/v8.26.0 "Release v8.26.0 · typescript-eslint/typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint v8.26.0 출시.
TypeScript 5.8 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## What is TypeScript? An overview for JavaScript programmers
[2ality.com/2025/02/what-is-typescript.html](https://2ality.com/2025/02/what-is-typescript.html "What is TypeScript? An overview for JavaScript programmers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript가 무엇인가 알려주는 개요적 글.
TypeScript는 JavaScript에 자료형 구문을 더한 것이라는 점, TypeScript 빌드, type stripping 등의 `tsc` 외 컴파일 관련하여


----

## Migrating 160,000 Lines of Production Banking JavaScript to TypeScript with Zero Downtime - Ben Howdle - Software Consultant &amp; Advisor
[benhowdle.im/migrating-js-to-ts-zero-downtime.html](https://benhowdle.im/migrating-js-to-ts-zero-downtime.html "Migrating 160,000 Lines of Production Banking JavaScript to TypeScript with Zero Downtime - Ben Howdle - Software Consultant &amp; Advisor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

JavaScript에서 TypeScript으로 이행.
이행 브런치를 사용해 이행 접근


----

## Temporal로 변경될 JavaScript 시간 조작［JS Modern Features no.1］ | gihyo.jp
[gihyo.jp/article/2025/02/ride-modern-frontend-07](https://gihyo.jp/article/2025/02/ride-modern-frontend-07 "Temporal로 변경될 JavaScript 시간 조작［JS Modern Features no.1］ | gihyo.jp")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3 Temporal 관련해서


----

## Lynx: Unlock Native for More - Lynx
[lynxjs.org/blog/lynx-unlock-native-for-more.html](https://lynxjs.org/blog/lynx-unlock-native-for-more.html "Lynx: Unlock Native for More - Lynx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">article</span></p>

React 기반 API와 CSS 사용한 네이티브 애플리케이션 개발이 가능한 Lynx.
Instant First-Frame Rendering (IFR)나 Main Thread Script 관련해서


----

## oxlint으로 eslint 고속화시키기
[zenn.dev/hiruno\_tarte/articles/how-to-use-oxlint](https://zenn.dev/hiruno_tarte/articles/how-to-use-oxlint "oxlint으로 eslint 고속화시키기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

oxlint와 ESLint 조합해서 이용하는 설정.
oxlint와 ESLint 겹친 내용을 oxlint으로 옮겨서, ESLint 플러그인만 체크하는 설정임


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## lynx-family/primjs: JavaScript Engine Optimized for Lynx
[github.com/lynx-family/primjs](https://github.com/lynx-family/primjs "lynx-family/primjs: JavaScript Engine Optimized for Lynx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Native</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Lynx에 사용되는 JavaScript 엔진.
QuickJS 기반, GC 구현이나 Chrome DevTools Protocol (CDP) 구현도 추가되어 있음


----
