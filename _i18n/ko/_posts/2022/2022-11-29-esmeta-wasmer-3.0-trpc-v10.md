---
title: "2022-11-29のJS: ESMeta、Wasmer 3.0、tRPC v10"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2022-11-29T14:34:25.485Z
category: JSer
tags:
- TypeScript
- Tools
- node.js
- WebAssembly
- Rust

---

JSer.info #620 - [ESMeta](https://github.com/es-meta/esmeta) ECMAScript Specification Metalanguage 도구가 공개되었다.

- [es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage](https://github.com/es-meta/esmeta)

주로 [ECMAScript의 사양](https://tc39.es/ecma262/)을 다루는 엔지니어를 위한 도구다.
ECMAScript의 언어/사양서 파서와 인터프리터를 구현해, 사양서에서 자동적으로 ECMAScript의 처리 환경을 생성하는 메타적 도구다.
사양서 알고리즘을 단계별로 실행하거나, 디버거로 Break Point를 붙이거나, 사양서에 위한 내부 상태를 가시화할 수 있는 디버그 기능이 구현되어있다.

----

WebAssembly 처리 환경 Wasmer 3.0가 출시되었다.

- [Announcing Wasmer 3.0](https://wasmer.io/posts/announcing-wasmer-3.0)
- [wasmer/migration_to_3.0.0.md at master · wasmerio/wasmer · GitHub](https://github.com/wasmerio/wasmer/blob/master/docs/migration_to_3.0.0.md)

Wasmer 3.0에는 WAPM 패키지 실행이 가능한 `wasmer run` 명령어, `MemoryView` 추가.
Zig의 크로스컴파일 기능으로 사용해 Window/Linux/macOS 실행파일을 만들 수 있다.

----

TypeScript로 만들어진 API 레이어를 정의하는 tRPC v10가 출시되었다.

- [Announcing tRPC v10 | tRPC](https://trpc.io/blog/announcing-trpc-10)

주 내용은 자료형 이용방법을 개선하는 Router 정의 방법, `inferRouterInputs`와 `inferRouterOutputs` 자료형 추가, Middleware 시그니처 변경 등이다.

마이그레이션 가이드와 마이그레이션 도구도 같이 공개되었다.

- [Migrate from v9 to v10 | tRPC](https://trpc.io/docs/migrate-from-v9-to-v10)

----

<h1 class="site-genre">헤드라인</h1>

----

## Prettier 2.8: improve --cache CLI option and TypeScript 4.9 satisfies operator! · Prettier
[prettier.io/blog/2022/11/23/2.8.0.html](https://prettier.io/blog/2022/11/23/2.8.0.html "Prettier 2.8: improve --cache CLI option and TypeScript 4.9 satisfies operator! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.8 출시
TypeScript 4.9 `satisfies` operator 지원, `--cache-location` 옵션 추가 등


----

## es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage
[github.com/es-meta/esmeta](https://github.com/es-meta/esmeta "es-meta/esmeta: ECMAScript Specification (ECMA-262) Metalanguage")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ECMAScript 사양서 메타언어 도구.
ECMAScript 언어/사양서 파서와 인터프리터 구현이 된 메타 도구.
사양서 알고리즘을 단계별로 실행하거나, 디버거로 Break Point를 붙이거나, 사양서에 위한 내부 상태를 가시화할 수 있는 기능이 구현되어있다.


----

## Announcing Wasmer 3.0
[wasmer.io/posts/announcing-wasmer-3.0](https://wasmer.io/posts/announcing-wasmer-3.0 "Announcing Wasmer 3.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span></p>

Wasmer 3.0 출시.
WAPM 패키지 실행이 가능한 `wasmer run` 명령어, `MemoryView` 추가.
Zig의 크로스컴파일 기능으로 Window/Linux/macOS 실행파일을 만들 수 있다.

- [wasmer/migration\_to\_3.0.0.md at master · wasmerio/wasmer · GitHub](https://github.com/wasmerio/wasmer/blob/master/docs/migration_to_3.0.0.md "wasmer/migration\_to\_3.0.0.md at master · wasmerio/wasmer · GitHub")

----

## Announcing tRPC v10 | tRPC
[trpc.io/blog/announcing-trpc-10](https://trpc.io/blog/announcing-trpc-10 "Announcing tRPC v10 | tRPC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

tRPC v10 출시.
Router 정의방법, `inferRouterInputs`와 `inferRouterOutputs`의 자료형 정의 추가, Middleware 시그니처 변경 등

- [Migrate from v9 to v10 | tRPC](https://trpc.io/docs/migrate-from-v9-to-v10 "Migrate from v9 to v10 | tRPC")

----

## Node.js 18.x runtime now available in AWS Lambda | AWS Compute Blog
[aws.amazon.com/jp/blogs/compute/node-js-18-x-runtime-now-available-in-aws-lambda/](https://aws.amazon.com/jp/blogs/compute/node-js-18-x-runtime-now-available-in-aws-lambda/ "Node.js 18.x runtime now available in AWS Lambda | AWS Compute Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">Lambda</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

AWS Lambda, Node.js 18 지원.


----
<h1 class="site-genre">읽을거리</h1>

----

## Wasm는 왜 시큐어한가?
[zenn.dev/0kate/articles/83e48c177ff709](https://zenn.dev/0kate/articles/83e48c177ff709 "Wasm은 왜 시큐어한가?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

Wasmer 구현을 보며, WebAssembly 시큐리티 기능이 어떻게 실현되는가


----

## Prerender2 기능에 대해 | blog.bokken.io
[blog.bokken.io/articles/2022-11-24/about-prerender2.html](https://blog.bokken.io/articles/2022-11-24/about-prerender2.html "Prerender2 기능에 대해 | blog.bokken.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome에 구현중인 Prerender2에 대해
Speculation Rules에서 프리렌더링하는 대상을 지정하는 새 구조에 대해


----

## 디자인 시스템 개발 우선도의 [난해함]과 [대책] ｜hikaru-takase /Loglass｜note
[note.com/99997373/n/n7dcb9092a90b](https://note.com/99997373/n/n7dcb9092a90b "디자인 시스템 개발 우선도 [난해함]과 [대책] ｜hikaru-takase /Loglass｜note")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Design</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

제품 다각화 중 여러 제품에서 참조할 수 있는 디자인이 필요해졌기에, 이를 해결하기 위한 디자인 시스템을 어떻게 만들어 가는가에 대해
디자인 토큰 분리, 컴포넌트 집중관리, 자잘하게 만들어 키우기 등


----

## TypeScript and native ESM on Node.js
[2ality.com/2021/06/typescript-esm-nodejs.html](https://2ality.com/2021/06/typescript-esm-nodejs.html "TypeScript and native ESM on Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.js에서 ESM와 `exports` 필드에 대한 해설


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JSConf JP 2022 공개자료・Twitter 링크 정리
[zenn.dev/yumemi\_inc/articles/2022-11-27-jsconf-jp-2022](https://zenn.dev/yumemi_inc/articles/2022-11-27-jsconf-jp-2022 "JSConf JP 2022 공개자료・Twitter 링크 정리")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

JSConf JP 2022 영상과 슬라이드 정리

- [JSConf JP](https://jsconf.jp/2022/ "JSConf JP")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## 1Password/typeshare: Typeshare is the ultimate tool for synchronizing your type definitions between Rust and other languages for seamless FFI.
[github.com/1Password/typeshare](https://github.com/1Password/typeshare "1Password/typeshare: Typeshare is the ultimate tool for synchronizing your type definitions between Rust and other languages for seamless FFI.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">kotlin</span> <span class="jser-tag">swift</span> <span class="jser-tag">golang</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

어노테이션한 Rust 코드에서 TypeScript/Swift/Kotlin 자료형 정의를 생성하는 도구

----


## hyperstackjs · Hyperstack is a modern full-stack Node.js web framework for the pragmatic programmer
[hyperstackjs.io/](https://hyperstackjs.io/ "hyperstackjs · Hyperstack is a modern full-stack Node.js web framework for the pragmatic programmer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

Node.js 웹 프레임워크

----
<h1 class="site-genre">도서</h1>

----

## A Skeptic’s Guide to Functional Programming with JavaScript
[jrsinclair.com/skeptics-guide](https://jrsinclair.com/skeptics-guide "A Skeptic’s Guide to Functional Programming with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">functional</span> <span class="jser-tag">book</span></p>

JavaScript 함수형 프로그래밍에 대한 도서


----
