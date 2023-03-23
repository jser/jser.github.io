---
title: "2023-03-22: Firefox 111, react.dev, TypeScript 5"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2023-03-22T03:54:32.412Z
category: JSer
tags:
- TypeScript
- node.js
- React
- npm
- Firefox

---

JSer.info #636 - Firefox 111가 출시되었습니다.

- [Firefox 111.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/111.0/releasenotes/)
- [Firefox 111 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/111)

HTML `translate` 속성 지원, CSS color functions를 플러그로 지원합니다.
또, Safari와 같이 File System Access API Origin private file system (OPFS)를 지원합니다.

- [The File System API with Origin Private File System | WebKit](https://webkit.org/blog/12257/the-file-system-access-api-with-origin-private-file-system/)

----

React 새로운 문서 사이트 [react.dev](https://react.dev/) 가 공개되었습니다.

- [Introducing react.dev – React](https://react.dev/blog/2023/03/16/introducing-react-dev)

도메인이 react.dev이 되었으며, React Hooks이 기본으로 되어, 튜토리얼이나 API 가이드도 새로 작성되었습니다.
또한, 이전 문서는 <https://legacy.reactjs.org/>에 공개되어 있습니다.

----

TypeScript 5.0가 정식 출시되었습니다.

- [Announcing TypeScript 5.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/)

TypeScript는 semver는 아니지만, 메이저 업데이트라 할 정도로 큰 변경이 포함되어 있습니다.


지금까지는 ECMAScript Stage 1 Decorator이었지만, Stage 3 Decorator으로 지원됩니다.
`const` type parameter 추가, `tsconfig.json`로 다수 `extends`에 대응, enum과 union 자료형 개선도 행해졌습니다.

또한, `--moduleResolution bundler` 추가와 관련한 옵션 추가, `exports` 필드 Condition를 지정할 수 있는 `--customConditions` 추가.
`import`할 때 `type` 수식자를 삭제하고 그 외를 남기는 `--verbatimModuleSyntax` 옵션 추가, JSDoc에서 `@satisfies`를 지원 등도 포함되어 있습니다.

TypeScript의 내부적 변경으로 TypeScript 코드베이스를 namespace에서 moudle로 이행, 또한, TypeScript의 코드베이스를 namespace에서 moudle로 이행, 퍼포먼스 / 메모리 / 패키지 크기 개선했습니다.
namespace 관련해서는 글도 공개되어 있습니다.

- [TypeScript's Migration to Modules - TypeScript](https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/)

낡아진 `--target ES3`이나 `--out` 등 옵션도 비권장으로 변경했으며, `--forceConsistentCasingInFileNames` 를 기본적으로 `true`로 변경하는 변경도 포함되어 있습니다.



----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Firefox 111.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/111.0/releasenotes/](https://www.mozilla.org/en-US/firefox/111.0/releasenotes/ "Firefox 111.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 111 출시.
HTML `translate` 속성 지원, CSS color functions를 플러그로 지원.
File System Access API Origin private file system (OPFS) 지원 등

- [Firefox 111 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/111 "Firefox 111 for developers - Mozilla | MDN")

----

## Node v19.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v19.8.0](https://nodejs.org/en/blog/release/v19.8.0 "Node v19.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v19.8.0 출시.
`Buffer.copyBytesFrom()` 추가, `AsyncLocalStorage.bind()`와 `AsyncLocalStorage.snapshot()` 추가.
`fs.openAsBlob()` 추가, `URLSearchParams`에 `size` getter 추가, WASI에 `version`를 추가 등


----

## vite/CHANGELOG.md at main · vitejs/vite
[github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#420-2023-03-16](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#420-2023-03-16 "vite/CHANGELOG.md at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 4.2.0 출시.
HTML 파일 내에서 `%ENV_NAME%`로 환경 변수 치환 가능, Source Maps 개선, `exports` 필드의 Subpath imports에 대응.
TypeScript 5 지원과 esbuild 0.17으로 업데이트 등


----

## Introducing react.dev – React
[react.dev/blog/2023/03/16/introducing-react-dev](https://react.dev/blog/2023/03/16/introducing-react-dev "Introducing react.dev – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">news</span></p>

React 새로운 문서 사이트 react.dev 가 공개되었다.
도메인이 react.dev가 되었으며, React Hooks가 기본이 되었다. 튜토리얼, API 가이드도 새로 작성되었다.


----

## Announcing TypeScript 5.0 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/ "Announcing TypeScript 5.0 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.0 출시.
ECMAScript Stage 3 Decorator 구현, `const` type perameter 추가, `tsconfig.json`으로 다수 `extends` 대응, enum과 union 자료형 개선.
`--moduleResolution bundler`의 추가와 관련한 옵션 추가, `exports` 필드 Condition를 지정할 수 있는 `--customConditions` 추가.
`import`할 땨 `type` 수식자 삭제하고 그 외를 남기는 `--verbatimModuleSyntax` 옵션 추가, JSDoc에서 `@satisfies`를 지원 등.
또한, TypeScript의 코드베이스를 namespace에서 moudle로 이행, 퍼포먼스 / 메모리 / 패키지 크기 개선.
`--target ES3`이나 `--out` 등 옵션을 비권장으로 변경, `--forceConsistentCasingInFileNames`를 기본값으로 true로 변경하는 변경 등이 포함되어있다.


----

## styled-components/xstyled: A utility-first CSS-in-JS framework built for React. 💅👩‍🎤⚡️
[github.com/styled-components/xstyled](https://github.com/styled-components/xstyled "styled-components/xstyled: A utility-first CSS-in-JS framework built for React. 💅👩‍🎤⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">news</span></p>

xstyled가 styled-components organization으로 이관되었다

- [Evan Jacobs on Twitter: &amp;quot;Excited to announce that xstyled is now part of the styled-components organization and we will begin to cross-pollinate improvements in the near future! Thank you so much @neoziro! https://t.co/uPk4sR9QsS&amp;quot; / Twitter](https://twitter.com/probablyup/status/1632385154814558210 "Evan Jacobs on Twitter: &amp;amp;quot;Excited to announce that xstyled is now part of the styled-components organization and we will begin to cross-pollinate improvements in the near future! Thank you so much @neoziro! https://t.co/uPk4sR9QsS&amp;amp;quot; / Twitter")

----
<h1 class="site-genre">읽을거리</h1>

----

## Introducing &quot;safe npm&quot;, a Socket npm Wrapper - Socket
[socket.dev/blog/introducing-safe-npm](https://socket.dev/blog/introducing-safe-npm "Introducing \&quot;safe npm\&quot;, a Socket npm Wrapper - Socket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

`npm`와 `npx`에 alias해서 이용할 수 있는 커맨드.
설치할 때 패키지가 멀웨어인가, 설치시점에 스크립트 실행하는가 등 확인하며 설치할 수 있다

- [socket npm &amp;amp; socket npx](https://docs.socket.dev/docs/socket-npm-socket-npx "socket npm &amp;amp;amp; socket npx")

----

## npm install와 npm ci 동작 확인을 간단히 해보았다. - Mitsuyuki.Shiiba
[bufferings.hatenablog.com/entry/2023/03/21/145023](https://bufferings.hatenablog.com/entry/2023/03/21/145023 "npm install와 npm ci 동작확인을 간단히 해봤다. - Mitsuyuki.Shiiba")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span> <span class="jser-tag">CI</span></p>

npm install와 npm ci와 캐시에 관련한 글.
`npm install`는 `node_modules/`를 재이용할 수 있지만, 안전하지 않은 경우도 있다.
`npm ci`는 `node_modules/`를 삭제하기 위해 `~/.npm`를 캐시로 사용할 필요가 있다는 내용.

- [npm install 랑 npm ci 그래서 어떻게 쓰는거야? 2023년판 - Mitsuyuki.Shiiba](https://bufferings.hatenablog.com/entry/2023/03/15/215044 "npm install 랑 npm ci 그래서 어떻게 쓰는거야? 2023년판 - Mitsuyuki.Shiiba")

----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## lagonapp/lagon: Deploy Serverless Functions at the Edge. Current status: Dev
[github.com/lagonapp/lagon](https://github.com/lagonapp/lagon "lagonapp/lagon: Deploy Serverless Functions at the Edge. Current status: Dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">OpenSource</span></p>

V8와 Rust로 작성된 JavaScript 런타임.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----


## total-typescript/ts-reset: A &#039;CSS reset&#039; for TypeScript, improving types for common JavaScript API&#039;s
[github.com/total-typescript/ts-reset](https://github.com/total-typescript/ts-reset "total-typescript/ts-reset: A &#039;CSS reset&#039; for TypeScript, improving types for common JavaScript API&#039;s")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScript의 libs의 자료형 정의를 덮어쓰는 자료형 정의 라이브러리.
`JSON.parse`가 `any`가 아니라 `unknown`를 반환하도록 변경되거나, `.includes()`나 `.has()`의 자료형을 엄밀하게 하는 등의 동작


----

## anymaniax/orval: orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺
[github.com/anymaniax/orval](https://github.com/anymaniax/orval "anymaniax/orval: orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">OpenAPI</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

OpenAPI Spec에서 API 클라이언트나 목 서버 등의 코드 생성하는 도구.

- [OpenAPI로 코드 자동생성! 『Orval』 장점과 선정 이유](https://zenn.dev/hrbrain/articles/3ca5d37dd0b80e "OpenAPI로 코드 자동생성! 『Orval』 장점과 선정 이유")

----

## gajus/turbowatch: Extremely fast file change detector and task orchestrator for Node.js.
[github.com/gajus/turbowatch](https://github.com/gajus/turbowatch "gajus/turbowatch: Extremely fast file change detector and task orchestrator for Node.js.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

파일 변경을 감시해서, 프로세스를 재기동하는 라이브러리, 도구


----

## Transformers.js
[xenova.github.io/transformers.js/](https://xenova.github.io/transformers.js/ "Transformers.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">MachineLearning</span></p>

브라우저에서 동작하는 Transformers 라이브러리.
HuggingFace Hub에서 모델 다운로드할 수 있도록 되어있어, BERT 같은 다양한 모델에서 태스크 실행 가능


----
<h1 class="site-genre">도서</h1>

----

## Practical WebAssembly \[Book\]
[www.oreilly.com/library/view/practical-webassembly/9781098142513/](https://www.oreilly.com/library/view/practical-webassembly/9781098142513/ "Practical WebAssembly \[Book\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">book</span></p>

2024년 5월 발매
WebAssembly 관련 도서.
Rust와 AssemblyScript으로 Wasm를 작성해 이용하는 방법을 다룬다


----
