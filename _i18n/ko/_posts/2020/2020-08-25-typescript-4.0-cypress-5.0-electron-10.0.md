---
title: "2020-08-25: TypeScript 4.0, Cypress 5.0, Electron 10.0"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-08-25T02:59:14.022Z
category: JSer
tags:
- TypeScript
- Testing
- Electron

---

JSer.info #502 - TypeScript 4.0이 정식 릴리스 됐습니다.

- [Announcing TypeScript 4.0 | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/)

Variadic Tuple Types, Labeled Tuple Elements 등이 추가되고 Class Property 타입이 Constructor에서 추론될 수 있도록 개선됐습니다.
또, ES2021에 도입될 예정인 [Logical Operators and Assignment Expressions](https://github.com/tc39/proposal-logical-assignment)를 지원합니다.
그 외로 `catch` 절의 기본 타입이 `unknown`으로 변경됐으며 `jsxFragmentFactory` 옵션과 `--incremental`과 `--noEmit`을 함께 사용할 수 있도록 지원합니다.

이어서 TypeScript 4.0에 대응한 Babel, Preitter의 새 버전도 각각 릴리스 됐습니다.

- [7.11.0 Released: ECMAScript 2021 support in preset-env, TypeScript 4.0 support, printing config and the future of `babel-eslint` · Babel](https://babeljs.io/blog/2020/07/30/7.11.0)
- [Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier](https://prettier.io/blog/2020/08/24/2.1.0.html)

TypeScript-ESLint 관련해서는 아래 이슈를 참고해주시기 바랍니다.

- [TypeScript 4.0 Syntax Support · Issue #2260 · typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/issues/2260#issuecomment-677853883)

----

E2E 테스트 프레임워크인 Cypress 5.0이 릴리스 됐습니다.

- [Release 5.0.0 · cypress-io/cypress](https://github.com/cypress-io/cypress/releases/tag/v5.0.0)


`cypress-plugin-retries`가 비권장 되고 Cypress 자체에서 재시도를 설정할 수 있게 됐습니다.
자세한 내용은 아래 문서를 참고해주시기 바랍니다.

- [Introducing Test Retries in Cypress 5.0](https://www.cypress.io/blog/2020/08/19/introducing-test-retries-in-cypress-5-0/)

지원 대상이 TypeScript 3.4+, Node.js 10+로 변경했으며 테스트 파일 내에 작성된 `__dirname`과 `__filename` 경로에 `/`가 포함되지 않도록 수정됐습니다.

----

Electron 10.0이 릴리스 됐습니다.

[Release electron v10.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v10.0.0)

Chromium 85, V8 8.5, Node.js 12.16으로각각 갱신됐습니다.
또, `enableRemoteModule`가 `false`로 변경되고 `app.allowRendererProcessReuse`가 `true`로 변경됐습니다.

`remote` 모듈은 유저랜드(electron-userland)로 이전되기 때문에 이를 위해 단계적으로 `enableRemoteModule` 옵션이 도입됐으며 이번에 기본 값이 `false`(비활성)로 변경됐습니다.

자세한 내용은 아래 이슈나 예정돼 있는 비호환 변경 내용을 정리한 문서를 참고하시기 바랍니다.

- [Deprecate the 'remote' module and move it to userland · Issue #21408 · electron/electron](https://github.com/electron/electron/issues/21408)
- [Electron 9.0.0 | Electron Blog](https://www.electronjs.org/blog/electron-9-0)
- [electron/breaking-changes.md at master · electron/electron](https://github.com/electron/electron/blob/master/docs/breaking-changes.md)

그 외로 `contents.backgroundThrottling` 속성이 추가 됐고 `sameSite` 정보를 가져올 수 있도록 변경됐으며 `worldSafeExecuteJavaScript` 옵션이 추가 됐습니다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Release 2.8.0 · pikapkg/snowpack
[github.com/pikapkg/snowpack/releases/tag/snowpack%402.8.0](https://github.com/pikapkg/snowpack/releases/tag/snowpack%402.8.0 "Release 2.8.0 · pikapkg/snowpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

snowpack 2.8.0이 릴리스 됐습니다.
`snowpack build --watch` 인자가 추가됐고, `--polyfill-node`으로 Node 코어 모듈의 polyfill을 추가할 수 있도록 변경됐습니다.


----

## Release v1.3.0 · Polymer/lit-html
[github.com/Polymer/lit-html/releases/tag/v1.3.0](https://github.com/Polymer/lit-html/releases/tag/v1.3.0 "Release v1.3.0 · Polymer/lit-html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

lit-html 1.3.0이 릴리스 됐습니다.
Trusted Types를 지원합니다.


----

## Announcing TypeScript 4.0 | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0/ "Announcing TypeScript 4.0 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.0이 릴리드 됐습니다.
Variadic Tuple Types, Labeled Tuple Elements, Class Property 타입이 Constructor에서 추론될 수 있도록 개선됐습니다.
ES2021에서 도입될 예정인 Logical Operators and Assignment Expressions를 지원합니다.
`catch` 절의 기본 타입이 `unknown`으로 변경됐으며 `jsxFragmentFactory` 옵션 지원하고 `--incremental`과 `--noEmit`을 함께 사용할 수 있도록 지원합니다.


----

## axios/CHANGELOG.md at master · axios/axios
[github.com/axios/axios/blob/master/CHANGELOG.md#0200-august-20-2020](https://github.com/axios/axios/blob/master/CHANGELOG.md#0200-august-20-2020 "axios/CHANGELOG.md at master · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Axios 0.20.0이 릴리스 됐습니다.
BOM을 포함하는 JSON을 지원하며 `maxBodyLength` 옵션과 `decompress` 옵션이 추가 됐습니다.


----

## Release 5.0.0 · cypress-io/cypress
[github.com/cypress-io/cypress/releases/tag/v5.0.0](https://github.com/cypress-io/cypress/releases/tag/v5.0.0 "Release 5.0.0 · cypress-io/cypress")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">testing</span></p>

Cypress 5.0.0이 릴리스 됐습니다.
`cypress-plugin-retries`가 비권장 되고 Cypress 자체에서 재시도를 설정할 수 있게 됐습니다.
지원 대상이 TypeScript 3.4+, Node.js 10+로 변경됐고 `__dirname`과 `__filename` 경로에 `/`가 포함되지 않도록 수정됐습니다. 

- [Release 5.0.0 · cypress-io/cypress](https://github.com/cypress-io/cypress/releases/tag/v5.0.0 "Release 5.0.0 · cypress-io/cypress")

----

## Release electron v10.0.0 · electron/electron
[github.com/electron/electron/releases/tag/v10.0.0](https://github.com/electron/electron/releases/tag/v10.0.0 "Release electron v10.0.0 · electron/electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 10.0.0이 릴리스 됐습니다.
Chromium 85, V8 8.5, Node.js 12.16으로 각각 갱신됐습니다.
`enableRemoteModule`의 기본값이 `false`로, `app.allowRendererProcessReuse`의 기본값이 `true`로 변경됐습니다.
`sameSite` 정보를 가져올 수 있도록 개선됐고 `contents.backgroundThrottling` 속성과 `worldSafeExecuteJavaScript` 옵션이 추가됐습니다.


----

## Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier
[prettier.io/blog/2020/08/24/2.1.0.html](https://prettier.io/blog/2020/08/24/2.1.0.html "Prettier 2.1: new --embedded-language-formatting option and new JavaScript/TypeScript features! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.1이 릴리스 됐습니다.
`--embedded-language-formatting` 플러그와 `--ignore-unknown` 플러그가 추가됐고 TypeScript 4.0을 지원합니다.
ES Proposal의 Pipeline operator, Record and Tuple 구문을 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## ts-migrate: A Tool for Migrating to TypeScript at Scale | by Sergii Rudenko | Airbnb Engineering & Data Science | Aug, 2020 | Medium
[medium.com/airbnb-engineering/ts-migrate-a-tool-for-migrating-to-typescript-at-scale-cd23bfeb5cc](https://medium.com/airbnb-engineering/ts-migrate-a-tool-for-migrating-to-typescript-at-scale-cd23bfeb5cc "ts-migrate: A Tool for Migrating to TypeScript at Scale | by Sergii Rudenko | Airbnb Engineering & Data Science | Aug, 2020 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

JavaScript에서 TypeScript로의 이전을 보조하는 `ts-migrate`을 소개합니다.
`.js`를 `.ts`로 이름 변경, codemod 기반으로 `any`등의 타입 명시, 컴파일 에러가 나는 부분을 `// @ts-expect-error` 코멘트로 비활성화하여 점진적으로 마이그레이션 할 수 있도록 도와줍니다.

- [airbnb/ts-migrate: A tool to help migrate JavaScript code quickly and conveniently to TypeScript](https://github.com/airbnb/ts-migrate "airbnb/ts-migrate: A tool to help migrate JavaScript code quickly and conveniently to TypeScript")

----

## What's New In DevTools (Chrome 86)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/08/devtools](https://developers.google.com/web/updates/2020/08/devtools "What's New In DevTools (Chrome 86)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 86 DevTools의 변경 사항이 정리돼 있습니다.
Media 패널 추가, 컨텍스트 메뉴에서 특정 요소를 스크린샷 촬영할 수 있는 기능이 추가됐습니다.
WebFont에 `local()`이 없는 경우를 애뮬레이트, Idle Detection 애뮬레이트, `prefers-reduced-data` 애뮬레이트 기능이 추가됐습니다.
Lighthouse 6.2로 갱신됐고 Application 패널에 Frame 정보 추가, `X-Client-Data`의 디코드를 지원합니다.


----

## Protect your resources from web attacks with Fetch Metadata
[web.dev/fetch-metadata/](https://web.dev/fetch-metadata/ "Protect your resources from web attacks with Fetch Metadata")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

Fetch Metadata의 `Sec-Fetch-*` 헤더를 설명합니다.
Same-Origin과 Cross-Site의 구별, 각 `Sec-Fetch-*` 헤더 설명, 크로스 사이트 리퀘스트를사용한 공격과 판정 그리고 대책에 대해서 이야기합니다.


----
<h1 class="site-genre">서비스, 사이트, 문서</h1>

----

## HexEd.it - Browser-based Online and Offline Hex Editing
[hexed.it/](https://hexed.it/ "HexEd.it - Browser-based Online and Offline Hex Editing")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">editor</span> <span class="jser-tag">Tools</span></p>

브라우저 기반의 바이너리 에디터입니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## azu/kvs: Key-Value storage library for Browser, Node.js, and In-Memory.
[github.com/azu/kvs](https://github.com/azu/kvs "azu/kvs: Key-Value storage library for Browser, Node.js, and In-Memory.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

브라우저와 Node.js에서 동작하는 Universal한 Key-Value 기반 스토리지 라이브러리입니다.
IndexedDB와 동일한 인터페이스를 제공 하며 파일 기반 기능도 구현돼 있고 마이그레이션도 지원합니다.  
각 구현은 개별 패키지로 나뉘어져 있으며 각 패키지의 크기는 1kb(gzip) 정도입니다.


----

## Elderjs/elderjs: Elder.js is an opinionated static site generator and web framework for Svelte built with SEO in mind.
[github.com/elderjs/elderjs](https://github.com/elderjs/elderjs "Elderjs/elderjs: Elder.js is an opinionated static site generator and web framework for Svelte built with SEO in mind.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Svelte</span> <span class="jser-tag">library</span></p>

Svelte를 사용한 정적사이트 생성기입니다.
규약이 아닌 `route.js`에 의한 유연한 퍼머링크(permalink) 생성, `data.js`로 빌드에 필요한 데이터를 한꺼번에 가져와 정적 사이트를 생성하는 도구입니다.


----

## keiya01/react-performance-testing: A library to test runtime performance in React
[github.com/keiya01/react-performance-testing](https://github.com/keiya01/react-performance-testing "keiya01/react-performance-testing: A library to test runtime performance in React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

React 컴포넌트의 렌더링 수와 렌더링 시간을 측정할 수 있는 라이브러리입니다.
React를 몽키패치(monkey patch)하여 관련 데이터를 측정합니다.

- [React에서 렌더링 수 및 렌더링 시 걸리는 시간을 유닛 테스트로 작성할 수 있는 라이브러리를 개발했습니다 - Qiita](https://qiita.com/keiya01/items/93d83911fb44170717c2 "React에서 렌더링 수 및 렌더링 시 걸리는 시간을 유닛 테스트로 작성할 수 있는 라이브러리를 개발했습니다 - Qiita")(일본어)

----
