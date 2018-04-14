---
title: "2018-04-01のJS: TypeScript 2.8、React 16.3.0、TensorFlow.js"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-04-01T05:56:39.824Z
category: JSer
tags:
- TypeScript
- react
- ML

---

JSer.info #377 - TypeScript 2.8이 정식 릴리스 됐습니다.

- [Announcing TypeScript 2.8 | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/)
- [TypeScript 2.8.1 변경 사항 - Qiita](https://qiita.com/vvakame/items/2e32aeded05997f77dfa)(일본어)

Conditional Types를 지원하며 Conditional Types를 사용한 빌트인 타입으로 `Exclude<T, U>`, `Extract<T, U>`, `NonNullable<T>`, `ReturnType<T>`, `InstanceType<T>`가 추가됐습니다.
mapped type modifier의 `+`, `-` 지원, `.d.ts` 파일만 출력 할 수 있는 ` emitDeclarationOnly ` 옵션 추가, `@jsx` 프래그마 코멘트 지원 등이 이뤄졌습니다.

----

React 16.3.0이 릴리스 됐습니다.

- [React v16.3.0: New lifecycles and context API - React Blog](https://reactjs.org/blog/2018/03/29/react-v-16-3.html "React v16.3.0: New lifecycles and context API - React Blog")
- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")

향후 큰 기능 변경을 예고하고 있습니다.
새로운 [Context API](https://reactjs.org/docs/context.html "Context"), `createRef` 메서드, `forwardRef` 메서드, `StrictMode` 컴포넌트 등이 새롭게 추가됐습니다.

또, 비동기 렌더링 지원으로 인해 React 컴포넌트의 라이프 사이클 이벤트가 변경 됐습니다.
`componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` 는 앞으로 삭제되며 대신`getDerivedStateFromProps`와 `getSnapshotBeforeUpdate`가 추가됐습니다.

다음과 같은 절차로 위 라이플 사이클 API의 삭제가 이뤄지게 됩니다.

- 16.3: 각각 alias 메서드 `UNSAFE_componentWillMount, ` `UNSAFE_componentWillReceiveProps`,  ` UNSAFE_componentWillUpdate` 추가
  - `UNSAFE_` prefix를 위한 마이그레이션 스크립트 [rename-unsafe-lifecycles](https://github.com/reactjs/react-codemod#rename-unsafe-lifecycles "rename-unsafe-lifecycles") 공개 됨
- A future 16.x release: `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate`를 사용 시 비권장 경고 메시지 출력
- 17.0: `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` 삭제
  - 단, 원할한 마이그레이션을 위해 `UNSAFE_` 버전은 17.x에서도 유지함

이후, 버전 18.0에서 비권장 라이플 사이클 API가 완전히 삭제 될 예정입니다(`UNSAFE_` 버전은 17.x에서도 남음).
자세한 내용은 아래 글에 소개돼 있으니 참고하시길 바랍니다.

- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")

----

브라우저에서 TensorFlow 모델을 사용해 기계 학습을 할 수 있는 [TensorFlow.js](https://js.tensorflow.org/ "TensorFlow.js")가 공개됐습니다.
본래 Google이 개발 중이던 [deeplearn.js](https://deeplearnjs.org/index.html "deeplearn.js")의 차기 버전으로써 공개됐습니다.

JavaScript와 high-level layers API를 이용해 기계 학습을 할 수 있습니다. 처음으로 기계 학습을 배우는 JavaScript 개발자를 위한 관련 내용이 아래 문서에 정리돼 있으니 참고하시길 바랍니다.

- [Introducing TensorFlow.js: Machine Learning in JavaScript](https://medium.com/tensorflow/introducing-tensorflow-js-machine-learning-in-javascript-bf3eab376db "Introducing TensorFlow.js: Machine Learning in JavaScript")

또, 기존 TensorFlow나 Keras의 모델을 변환해 불러올 수 있으며 브라우저 상에서 재학습 등도 할 수 있습니다.
현재는 WebGL에 의존하고 있기 때문에 브라우저에서만 동작하며 Node.js 지원에 대해서는 검토 중인 것으로 FAQ를 통해 알 수 있습니다.

- [FAQ – TensorFlow.js](https://js.tensorflow.org/faq/)

----

<h1 class="site-genre">헤드라인</h1>

----

## React v16.3.0: New lifecycles and context API - React Blog
[reactjs.org/blog/2018/03/29/react-v-16-3.html](https://reactjs.org/blog/2018/03/29/react-v-16-3.html "React v16.3.0: New lifecycles and context API - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React v16.3.0이 릴리스 됐습니다.
새로운 Context API, `createRef` 메서드, `forwardRef` 메서드,  `StrictMode`  컴포넌트가 추가됐습니다.
컴포넌트 라이프 라이클 이벤트가 변경 됐습니다.

- [Update on Async Rendering - React Blog](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")
- [React v16.3.0: New lifecycles and context API【일본어 번역】 | maesblog](https://mae.chab.in/archives/60040 "React v16.3.0: New lifecycles and context API【日本語翻訳】 | maesblog")(일본어)

----

## March 2018 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/march-2018-security-releases/](https://nodejs.org/en/blog/vulnerability/march-2018-security-releases/ "March 2018 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.js의 보안 업데이트로써 각각 LTS와 개발 버전 업데이트가 공개됐습니다.

- Node.js 9.10.0
- Node.js 8.11.0 (LTS "Carbon")
- Node.js 6.14.0 (LTS "Boron")
- Node.js 4.9.0 (LTS "Argon")


----

## V8 JavaScript Engine: V8 release v6.6
[v8project.blogspot.com/2018/03/v8-release-66.html](https://v8project.blogspot.com/2018/03/v8-release-66.html "V8 JavaScript Engine: V8 release v6.6")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.6(Chrome 66)이 릴리스 됐습니다.
ECMAScript Proposal 대응을 위해 `Function#toString()`이 사양을 따르도록 수정됐고 JS가 JSON의 superset 되는 사양에 맞춰 변경됐습니다.
또, `catch` 구문의 파라메터 생략 가능하도록 변경됐고 `String#trimStart`나 `String#trimEnd`가 구현됐으며 Background compilation을 대응하고 Async, Array의 성능이 개선됐습니다.

- [Function.prototype.toString revision](https://tc39.github.io/Function-prototype-toString-revision/ "Function.prototype.toString revision")
- [tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262](https://github.com/tc39/proposal-json-superset "tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262")
- [tc39/proposal-string-left-right-trim: A proposal to the ECMAScript standard for including left and right trim of whitespace to strings](https://github.com/tc39/proposal-string-left-right-trim "tc39/proposal-string-left-right-trim: A proposal to the ECMAScript standard for including left and right trim of whitespace to strings")

----

## ZEIT – Next.js 5.1: Faster Page Resolution, Environment Config & More
[zeit.co/blog/next5-1](https://zeit.co/blog/next5-1 "ZEIT – Next.js 5.1: Faster Page Resolution, Environment Config & More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 5.1이 릴리스 됐습니다.
런타임 환경을 설정할 수 있는 `publicRuntimeConfig`와 `serverRuntimeConfig` 옵션 추가됐고 페이지 로딩 속도와 에러 핸들링 방식이 개선됐습니다. 

----

## Release v3.4.0 · storybooks/storybook
[github.com/storybooks/storybook/releases/tag/v3.4.0](https://github.com/storybooks/storybook/releases/tag/v3.4.0 "Release v3.4.0 · storybooks/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ui </span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

Storybook 3.4.0이 릴리스 됐습니다.
Polymer2를 지원하고 Angular와 Vue의 storyshot을 지원합니다.

----

## power-assert/CHANGELOG.md at v1.5.0 · power-assert-js/power-assert
[github.com/power-assert-js/power-assert/blob/v1.5.0/CHANGELOG.md](https://github.com/power-assert-js/power-assert/blob/v1.5.0/CHANGELOG.md "power-assert/CHANGELOG.md at v1.5.0 · power-assert-js/power-assert")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

power-assert 1.5.0이 릴리스 됐습니다.
Node.js 9.9.0에 추가된 `assert`의 strict mode를 지원합니다.

- [Node v9.9.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v9.9.0/ "Node v9.9.0 (Current) | Node.js")
- [Assert | Node.js v9.10.1 Documentation](https://nodejs.org/api/assert.html#assert_strict_mode "Assert | Node.js v9.10.1 Documentation")

----

## 📦 Parcel v1.7.0: – devongovett – Medium
[medium.com/@devongovett/parcel-v1-7-0-9aac0c505837](https://medium.com/@devongovett/parcel-v1-7-0-9aac0c505837 "📦 Parcel v1.7.0: – devongovett – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v1.7.0이 릴리스 됐습니다.
`.vue`와 Pug를 새롭게 지원하며 absolute path와 tilde(`~`) path도 지원합니다. 또, 출력한 파일에 해시 값을 부여하도록 개선됐으며 필요한 의존 모듈을 자동적으로 설치하도록 변경됐습니다.

----

## Dart Sass 1.0.0 is Released « Sass Blog
[sass.logdown.com/posts/7045860-dart-sass-100-is-released](http://sass.logdown.com/posts/7045860-dart-sass-100-is-released "Dart Sass 1.0.0 is Released « Sass Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart Sass 1.0이 릴리스 됐습니다.
Ruby Sass는 앞으로 유지보수만 합니다.

----

## ESLint v5.0.0-alpha.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/03/eslint-v5.0.0-alpha.0-released](https://eslint.org/blog/2018/03/eslint-v5.0.0-alpha.0-released "ESLint v5.0.0-alpha.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">serverless</span></p>

ESLint 5.0.0α가 릴리스 됐습니다.
예정됐던 비호환 변경에 대한 내용은 마이그레이션 가이드에 소개돼 있으니 참고하시길 바랍니다.

- [ESLint v5.0.0 변경 사항 정리(지속갱신) - Qiita](https://qiita.com/mysticatea/items/f34097961bf2827b675d "ESLint v5.0.0 변경 사항 정리(지속갱신) - Qiita")(일본어)
- [Migrating to v5.0.0 - ESLint - Pluggable JavaScript linter](https://eslint.org/docs/5.0.0/user-guide/migrating-to-5.0.0 "Migrating to v5.0.0 - ESLint - Pluggable JavaScript linter")

----

## Announcing TypeScript 2.8 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/](https://blogs.msdn.microsoft.com/typescript/2018/03/27/announcing-typescript-2-8/ "Announcing TypeScript 2.8 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ReleaseNote</span> <span class="jser-tag">TypeScript</span></p>

TypeScript 2.8이 릴리스 됐습니다.
Conditional Types, `@jsx` 프래그마 코멘트, mapped type modifier의 `+`, `-`를 지원하며 `d.ts`만 출력하는 옵션이 추가됐습니다.

- [TypeScript 2.8.1 변경 사항 - Qiita](https://qiita.com/vvakame/items/2e32aeded05997f77dfa "TypeScript 2.8.1 変更点 - Qiita")(일본어)

----
<h1 class="site-genre">아티클</h1>

----

## Server Timing API를 사용해 서버 사이드 벤치마킹을 편리하게 | 블로그 :: Web notes.log(일본어)
[blog.wnotes.net/blog/article/server-side-benchmark-using-server-timing-api](http://blog.wnotes.net/blog/article/server-side-benchmark-using-server-timing-api "Server Timing APIを使ってサーバーサイドのベンチマークを手軽にやる | ブログ :: Web notes.log")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span></p>

Server Timinig API를 사용해 서버 사이드의 리퀘스트 별 벤치마킹 데이터를 Chrome 개발자 도구에 출력하는 방법을 소개합니다.

----

## Update on Async Rendering - React Blog
[reactjs.org/blog/2018/03/27/update-on-async-rendering.html](https://reactjs.org/blog/2018/03/27/update-on-async-rendering.html "Update on Async Rendering - React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

비동기 렌더링을 위한 라이프 라이클 이벤트 추가와 변경 사항에 대해 작성돼 있습니다.
16.3에서 새로운 이벤트를 추가하고 16.x에서 구 이벤트 사용 시 경고 출력하며 17.0에서 구 이벤트 폐지를 진행합니다.
또 새롭게 추가한 `getDerivedStateFromProps`와 `getSnapshotBeforeUpdate`를 소개합니다.

----

## Working with the new CSS Typed Object Model  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/cssom](https://developers.google.com/web/updates/2018/03/cssom "Working with the new CSS Typed Object Model  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

CSS Typed OM에 대해 소개합니다.
이미 존재하는 `style` 프로퍼티와 새롭게 추가되는 `attributeStyleMap`의 차이나 CSS Typed OM에 추가된 API 메서드 리고 장점과 사용 방법이 작성돼 있습니다.

----

## WebAssembly/esm-integration: ECMAScript module integration
[github.com/WebAssembly/esm-integration](https://github.com/WebAssembly/esm-integration "WebAssembly/esm-integration: ECMAScript module integration")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">module</span> <span class="jser-tag">ECMAScript</span></p>

웹 어쎔블리를 위한 ES Module Integration Proposal 저장소 입니다.

----

## How display: contents; Works
[bitsofco.de/how-display-contents-works/](https://bitsofco.de/how-display-contents-works/ "How display: contents; Works")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

`display: contents;`에 대해 소개하는 글입니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## CondeNast/perf-timeline-cli: Generate Chrome Performance Timelines via a command line interface
[github.com/CondeNast/perf-timeline-cli](https://github.com/CondeNast/perf-timeline-cli "CondeNast/perf-timeline-cli: Generate Chrome Performance Timelines via a command line interface")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Chrome 개발자 도구의 Performance 패널 정보를 가져올 수 있는 CLI 도구입니다.
Puppeteer를 사용해 접근한 페이지에 대한 측정 결과를 가져올 수 있습니다.

----

## JavaScript in 14 minutes by Jeremy Thomas
[jgthms.com/javascript-in-14-minutes/](https://jgthms.com/javascript-in-14-minutes/ "JavaScript in 14 minutes by Jeremy Thomas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

브라우저의 개발자 도구에서 실행해 보면서 배울 수 있는 JavaScript 튜토리얼 글입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## cmseaton42/task-easy: A simple, customizable, and lightweight priority queue for promises.
[github.com/cmseaton42/task-easy](https://github.com/cmseaton42/task-easy "cmseaton42/task-easy: A simple, customizable, and lightweight priority queue for promises.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promise 스케줄 라이브러리입니다.

----

## asfktz/Awaity.js: A functional, lightweight alternative to bluebird.js, built with async / await in mind.
[github.com/asfktz/Awaity.js](https://github.com/asfktz/Awaity.js "asfktz/Awaity.js: A functional, lightweight alternative to bluebird.js, built with async / await in mind.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

async/await 기반의 컬렉션 라이브러리입니다.
Promise를 지원하는 map, filter, reduce 등의 컬렉션 조작을 제공합니다.

----

## jacobbogers/libRmath.js: Javascript Pure Implementation of Statistical R "core" numerical libRmath.so
[github.com/jacobbogers/libRmath.js](https://github.com/jacobbogers/libRmath.js "jacobbogers/libRmath.js: Javascript Pure Implementation of Statistical R \"core\" numerical libRmath.so")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">R </span> <span class="jser-tag">library</span></p>

R의 `math를 JavaScript에 포팅한 라이브러리입니다.

----

## TensorFlow.js
[js.tensorflow.org/](https://js.tensorflow.org/ "TensorFlow.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">WebGL</span></p>

tensorflow의 JavaScript 버전입니다.
WebGL을 사용해 기계 학습을 지원하며 기존 학습 모델을 converter로 변환하여 재사용할 수 있습니다.

- [tensorflow/tfjs-converter: Convert TensorFlow SavedModel and Keras models to TensorFlow.js](https://github.com/tensorflow/tfjs-converter "tensorflow/tfjs-converter: Convert TensorFlow SavedModel and Keras models to TensorFlow.js")

----

## jaywcjlove/hotkeys: ➷ A robust Javascript library for capturing keyboard input. It has no dependencies.
[github.com/jaywcjlove/hotkeys](https://github.com/jaywcjlove/hotkeys "jaywcjlove/hotkeys: ➷ A robust Javascript library for capturing keyboard input. It has no dependencies.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">키보드</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

단축키를 관리할 수 있는 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## React 개발 현장 교과서 | 마이나비북스(일본어)
[book.mynavi.jp/ec/products/detail/id&#x3D;88735](https://book.mynavi.jp/ec/products/detail/id=88735 "React開発　現場の教科書 | マイナビブックス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React와 Atomic Design을 주제로한 도서입니다.

----

## CSS Pocket Reference, 5th Edition - O'Reilly Media
[shop.oreilly.com/product/0636920146353.do](http://shop.oreilly.com/product/0636920146353.do "CSS Pocket Reference, 5th Edition - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2018년 4월 출간 예정인 CSS 레퍼런스 도서입니다.

----
