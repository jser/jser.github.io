---
title: "2024-02-20: ES2024 RC, typescript-eslint v7, React Compiler"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-02-20T06:26:06.640Z
category: JSer
tags:
- TypeScript
- ECMAScript
- React
- nodejs
- HTTP

---

JSer.info #681 - 2024년 6월 공개될 ES2024 출시 후보가 공개되었어요.

- [Release ES2024 Candidate February 2024 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02)

ES2024에는, 다음과 같은 변경도 있어요.

- [`ArrayBuffer.prototype.resize`](https://github.com/tc39/proposal-resizablearraybuffer)
- [`ArrayBuffer.prototype.transfer`](https://github.com/tc39/proposal-arraybuffer-transfer)
- [RegExp `v` flag](https://github.com/tc39/proposal-regexp-v-flag)
- [`Promise.withResolvers`](https://github.com/tc39/proposal-promise-with-resolvers)
- [`Object.groupBy`/`Map.groupBy`](https://github.com/tc39/proposal-array-grouping)
- [`Atomics.waitAsync`](https://github.com/tc39/proposal-atomics-wait-async)
- [`String.prototype.isWellFormed`/`String.prototype.toWellFormed`](https://github.com/tc39/proposal-is-usv-string)

매년 2월 경에 사양에 담을 Proposal가 정해지고, 6월 경 [GA 127th meeting](https://ecma-international.org/meeting-calendar/)에서 최종 승인될 예정이에요.

---

TypeScript 대상 ESLint 플러그인 typescript-eslint v7가 출시돼요.

- [Announcing typescript-eslint v7 | typescript-eslint](https://typescript-eslint.io/blog/announcing-typescript-eslint-v7/)

Node.js 16 지원 종료, ESLint Flat Config 지원하는 `typescript-eslint` 패키지 추가하는 변경도 있어요.
[ESLint v9.0.0](https://eslint.org/blog/2023/10/flat-config-rollout-plans/)에서 기본값이 될 예정인 ESLint Flat Config 이용하는 경우에는, `typescript-eslint` 패키지 이용할 필요가 있구요.

- [Getting Started | typescript-eslint](https://typescript-eslint.io/getting-started)

----

[React Labs: What We've Been Working On – February 2024 – React](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024)에서는 React Forget로 알려진 React Compiler 현재와 React 19으로 메이저 업데이트 다뤄요.
둘 다 어느 정도 개발이 진행되어 있어서,  출시까지 준비 과정에 대해서도 언급하고 있어요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Release v0.28.0 · axios/axios
[github.com/axios/axios/releases/tag/v0.28.0](https://github.com/axios/axios/releases/tag/v0.28.0 "Release Release v0.28.0 · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Axios v0.28.0 출시.
Axios v1.6.0에 수정된 CSRF 토큰 문제 백포트. 그 외 v1.x 계열에서 수정 백포트.


----

## Announcing typescript-eslint v7 | typescript-eslint
[typescript-eslint.io/blog/announcing-typescript-eslint-v7/](https://typescript-eslint.io/blog/announcing-typescript-eslint-v7/ "Announcing typescript-eslint v7 | typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint v7 출시.
Node.js 16 지원 종료, ESLint Flat Config 지원하는 `typescript-eslint` 패키지 추가.


----

## ECMAScript proposal updates @ 2024-02 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/02/15/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/02/15/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-02 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2024년 2월 TC39에서 Proposal 변경 정리.
Stage 2.7 스테이지가 새롭게 추가 됨.
`ArrayBuffer.prototype.transfer`은 Stage 4가 되서 ES2024에 포함


----

## Release ES2024 Candidate February 2024 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02](https://github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02 "Release ES2024 Candidate February 2024 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2024 후보 공개.
`ArrayBuffer.prototype.resize`/`ArrayBuffer.prototype.transfer`, RegExp `v` 플러그 추가.
`Promise.withResolvers`, `Object.groupBy`/`Map.groupBy` 추가.
`Atomics.waitAsync`, `String.prototype.isWellFormed`/`String.prototype.toWellFormed` 추가

- [Editorial: Describe changes in ES2024 by bakkot · Pull Request #3282 · tc39/ecma262](https://github.com/tc39/ecma262/pull/3282 "Editorial: Describe changes in ES2024 by bakkot · Pull Request #3282 · tc39/ecma262")

----

## Bun v1.0.27 | Bun Blog
[bun.sh/blog/bun-v1.0.27](https://bun.sh/blog/bun-v1.0.27 "Bun v1.0.27 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.27 출시.
`Response`가 Async generator와 Node.js `Readable` 지원, Bun Shell 개선.
또한, Bun Shell 에러일 때 exit code는 v1.1에서는 `1`로 변경될 예정.


----

## htmz - a low power tool for html
[leanrada.com/htmz/](http://leanrada.com/htmz/ "htmz - a low power tool for html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

htmx처럼 HTML에 선언적으로 Ajax같이 보이게하는 소소한 스니펫.
`<form action="/default#my-target" target=htmz>`과 지정한 리퀘스트 결과를 준비해 `<iframe name=htmz>`로 보여줌.
iframe 렌더링 결과를 `#my-target` 요소와 변경하는 구조.


----

## Node.js — Wednesday February 14 2024 Security Releases
[nodejs.org/en/blog/vulnerability/february-2024-security-releases](https://nodejs.org/en/blog/vulnerability/february-2024-security-releases "Node.js — Wednesday February 14 2024 Security Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">secu</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 보안 업데이트로 Node.js 20.x, 18.x, 21.x 각 업데이트.
OpenSSL 갱신, Linux에서 capabilities 관련 버그 수정, HTTP 리퀘스트에서 DoS 관련 문제, 권한 모델 문제 수정


----

## Redwood v7.0.0 Upgrade Guide - Announcements / Releases and Upgrade Guides - RedwoodJS Community
[community.redwoodjs.com/t/redwood-v7-0-0-upgrade-guide/5713](https://community.redwoodjs.com/t/redwood-v7-0-0-upgrade-guide/5713 "Redwood v7.0.0 Upgrade Guide - Announcements / Releases and Upgrade Guides - RedwoodJS Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redwood v7 출시.
Node.js 18 지원 종료, `prop-types` 패키지 의존 삭제, dbAuth 보안 개선에 따른 파괴적 변경

- [Release v7.0.0 · redwoodjs/redwood](https://github.com/redwoodjs/redwood/releases/tag/v7.0.0 "Release v7.0.0 · redwoodjs/redwood")

----
<h1 class="site-genre">읽을거리</h1>

----

## React Labs: What We&#039;ve Been Working On – February 2024 – React
[react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024 "React Labs: What We&#039;ve Been Working On – February 2024 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Compiler(aka. React Forgot)가 instagram에 이용되어, 몇 개월 안에 공개될 예정.
또한, 다음 메이저 버전 React 19에 필요한 기능이 완성되어, 공개 준비 진행하고 있다는 이야기


----

## A novel technique for creating ergonomic and tree-shakable TypeScript libraries
[softwaremill.com/a-novel-technique-for-creating-ergonomic-and-tree-shakable-typescript-libraries/](https://softwaremill.com/a-novel-technique-for-creating-ergonomic-and-tree-shakable-typescript-libraries/ "A novel technique for creating ergonomic and tree-shakable TypeScript libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

필요한 메서드 모으는 초기화와 Proxy 객체 사용함으로, zod 같은 메서드 체인 가능하면서 동시에 Tree Shaking도 가능한 라이브러리 만드는 방법에 대하여.
소소한 검증 라이브러리 예로 만드는 방법과 구조에 대해 해설.

- [mieszkosabo/correttore](https://github.com/mieszkosabo/correttore "mieszkosabo/correttore")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JollyUI
[www.jollyui.dev/](https://www.jollyui.dev/ "JollyUI")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React Aria 사용해서 shadcn/ui 호환하려는 컴포넌트 모음


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Tempo • Dates by FormKit
[tempo.formkit.com/](https://tempo.formkit.com/ "Tempo • Dates by FormKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Intl 객체 기반 날짜 관련 라이브러리


----

## kolodny/safetest
[github.com/kolodny/safetest?tab&#x3D;readme-ov-file](https://github.com/kolodny/safetest?tab=readme-ov-file "kolodny/safetest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">browser</span> <span class="jser-tag">E2E</span> <span class="jser-tag">library</span></p>

Netflix에서 이용하고 있는 컴포넌트 프레임워크.
Playwright, Vitest/Jest 등 테스트 프레임워크, React나 Vue 같은 UI 프레임워크 조합해서 테스트 진행.
애플리케이션 레벨 DI 컨테이너나 테스트 셋업을 코드로 유연하게 해서 조작해서 상태를 Playwright 테스트 진행.

- [Introducing SafeTest: A Novel Approach to Front End Testing | by Netflix Technology Blog | Feb, 2024 | Netflix TechBlog](https://netflixtechblog.com/introducing-safetest-a-novel-approach-to-front-end-testing-37f9f88c152d "Introducing SafeTest: A Novel Approach to Front End Testing | by Netflix Technology Blog | Feb, 2024 | Netflix TechBlog")

----

## pashak09/ts-expect-error-validator: Command-line tool to validate expected TypeScript errors
[github.com/pashak09/ts-expect-error-validator](https://github.com/pashak09/ts-expect-error-validator "pashak09/ts-expect-error-validator: Command-line tool to validate expected TypeScript errors")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">test</span> <span class="jser-tag">Tools</span></p>

`@ts-expect-error`에는 지정된 에러 코드만 무시하는 기능은 없기에, `@ts-expect-error [Code]` 코멘트로 지정한 에러 발생하고 있는가 체크하는 도구.


----
<h1 class="site-genre">도서</h1>

----

## Next.js 초입문 - 슈와시스템 당신의 배움 지원!
[www.shuwasystem.co.jp/book/9784798071299.html](https://www.shuwasystem.co.jp/book/9784798071299.html "Next.js 초입문 - 슈와시스템 당신의 배움 지원!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ebook</span></p>

Next.js 입문서


----
