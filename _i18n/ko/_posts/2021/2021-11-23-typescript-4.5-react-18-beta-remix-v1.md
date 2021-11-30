---
title: "2021-11-23: TypeScript 4.5, React 18 beta, Remix v1"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-11-23T14:07:26.950Z
category: JSer
tags:
- Tools
- TypeScript
- React
- Chrome
- debug

---

JSer.info #567 - TypeScript 4.5가 정식 릴리스 됐다.

- [Announcing TypeScript 4.5 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5/)

TypeScript가 빌트인으로 갖고 있는 `lib`의 타입 정의를 `package.json`의 `dependencies`를 사용해 지정할 수 있도록 개선 됐다.
`Awaited` 타입 추가, Top-Level await을 지원하는 `module: es2022` 지원, Condition Types에서 꼬리 재귀 최적화 되도록 하는 변경도 포함됐다.
import 명에 적용할 수 있는 `type` modifier 지원, ES Proposal의 Private Field Presence Checks, Import Assertions 지원 등도 추가됐다.

[TypeScript 4.5 Beta](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-beta/)에 추가됐던 Node.js의 ESM 지원 사항은 4.6 이후로 릴리스가 연기됐다.

----

React 18 beta가 릴리스됐다.

- [React 18 is now in beta · Discussion #112 · reactwg/react-18](https://github.com/reactwg/react-18/discussions/112)
- [The Plan for React 18 – React Blog](https://reactjs.org/blog/2021/06/08/the-plan-for-react-18.html)

[useSyncExternalStore](https://github.com/reactwg/react-18/discussions/86) / [useId](https://github.com/reactwg/react-18/discussions/111) / [useInsertionEffect](https://github.com/reactwg/react-18/discussions/110) API가 각각 추가됐다.
React 18의 기능 개발은 이것으로 마무리되며 정식 버전의 릴리스를 위해 문서나 에러 개선 등을 진행하고 있다.

----

React 기반 웹 프레임워크인 [Remix](https://github.com/remix-run/remix) v1이 릴리스됐다.

- [Remix v1 | Remix](https://remix.run/blog/remix-v1)

Next.js 등 처럼 React를 기반으로 한 프레임워크로 CLI, 라우팅, 라이프 사이클 메서드, React Hooks 등을 제공한다.
다른 프레임워크와 다른 점으로 SSG(Static Site Generator)가 아니라 클라이언트 서버 모델을 기본으로 채택하고 있다.
서버가 데이터를 반환할 때 필요한 데이터만 남도록 필터링 하여 클라이언트에 전송할 데이터를 최소화하는 데 목적을 둔 `loader` 함수를 갖고 있다.
어떠한 관점으로 만들고 있는지 다음 문서에 잘 정리돼 있으니 이해하는데 참고하길 바란다.

- [Remix | Philosophy](https://remix.run/docs/en/v1/guides/philosophy)

기본적으로 서버가 필요하기 때문에 [서버 측 코드](https://github.com/remix-run/remix/tree/main/packages/remix-server-runtime)도 함께 공개돼 있다.
이 서버는 공식 호스팅 서비스 이외에도 fly.io나 Cloudflare Workers 등의 Edge로 동작할 수 있도록 고려돼 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 4.5 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-5/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-5/ "Announcing TypeScript 4.5 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.5 릴리스.
TypeScript가 빌트인으로 제공하는 `lib`의 타입 정의를 `dependencies`로 지정할 수 있도록 개선.
`Awaited` 타입 추가, Top-Level await을 지원하는 `module: es2022` 지원, Condition Types에서 꼬리 재귀 최적화 되도록.
import 명에 적용할 수 있는 `type` modifier 지원, ES Proposal의 Private Field Presence Checks, Import Assertions 지원


----

## React 18 is now in beta · Discussion #112 · reactwg/react-18
[github.com/reactwg/react-18/discussions/112](https://github.com/reactwg/react-18/discussions/112 "React 18 is now in beta · Discussion #112 · reactwg/react-18")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 18 beta 릴리즈.
`useSyncExternalStore`(`useMutableSource`를 이름 변경한 것), `useId`, `useInsertionEffect` 추가


----

## Remix v1 | Remix
[remix.run/blog/remix-v1](https://remix.run/blog/remix-v1 "Remix v1 | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React 기반의 웹 프레임워크 Remix v1 릴리스.
CLI, 라우팅, 라이프 사이클 메서드, React Hooks 등을 제공한다.
클라이언트 서버 모델로, 서버가 반환하는 데이터를 필터링하여 최소한의 데이터를 이용할 수 있도록 하는 `loader` 함수를 갖고 있다.
서버 측을 fly.io나 Cloudflare Workers 등의 Edge로 실행하는데 목적을 두고 있다.


----

## Release v6.0.0 · sindresorhus/execa
[github.com/sindresorhus/execa/releases/tag/v6.0.0](https://github.com/sindresorhus/execa/releases/tag/v6.0.0 "Release v6.0.0 · sindresorhus/execa")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

execa 6.0.0 릴리스.
ESM 지원을 위한 변경, default export를 삭제하고 named export로 변경.


----

## Release v4.0.0 · emberjs/ember.js
[github.com/emberjs/ember.js/releases/tag/v4.0.0](https://github.com/emberjs/ember.js/releases/tag/v4.0.0 "Release v4.0.0 · emberjs/ember.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 4.0.0 릴리스.

- [Ember 3.28 and 4.0 Beta Released](https://blog.emberjs.com/ember-3-28-released "Ember 3.28 and 4.0 Beta Released")

----
<h1 class="site-genre">아티클</h1>

----

## Chrome Devtools를 이용한 프런트엔드 성능 측정(일본어)
[zenn.dev/koki\_tech/articles/9deb70d0a9befb](https://zenn.dev/koki_tech/articles/9deb70d0a9befb "Chrome Devtools による フロントエンドパフォーマンスの計測")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 개발자 도구의 퍼포먼스 탭을 읽는 방법과 그래프가 나타내는 수치를 설명하는 글


----

## Reimagine Atomic CSS
[antfu.me/posts/reimagine-atomic-css](https://antfu.me/posts/reimagine-atomic-css "Reimagine Atomic CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Atomic CSS를 주제로 한 글.
사전 생성 + Prune로 접근하는 Tailwind 방식, 온디멘드 생성 방식 TailwindCSS 소개.
또, 아직 실험(개발) 중인 Atomic CSS 엔진 UnoCSS도 소개하고 있다.


----

## What&#039;s New In DevTools (Chrome 96) - Chrome Developers
[developer.chrome.com/blog/new-in-devtools-96/](https://developer.chrome.com/blog/new-in-devtools-96/ "What&#039;s New In DevTools (Chrome 96) - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome96 개발자 도구의 변경 사항 정리.
CSS Overview 패널 추가, `prefers-contrast`와 Auto Dark Theme의 에뮬레이터 기능 추가.
Network 패널에 Payload 탭 추가, 시험적으로 Reporting API 패널이 추가 됐다.


----

## Migrating from Puppeteer to Playwright | Checkly
[www.checklyhq.com/guides/puppeteer-to-playwright/](https://www.checklyhq.com/guides/puppeteer-to-playwright/ "Migrating from Puppeteer to Playwright | Checkly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Puppeteer에서 Playwright로 이전하는 방법 소개.
API 대응표, 마이그레이션 방법, Playwright의 auto-waiting, 두 가지의 차이점에 대해서.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## divriots/browser-vite: Vite in the browser.
[github.com/divriots/browser-vite](https://github.com/divriots/browser-vite "divriots/browser-vite: Vite in the browser.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">Tools</span></p>

Vite를 브라우저의 Service Workers에서 실행시키고자 하는 프로젝트


----

## Bun - fast JavaScript &amp; CSS bundler
[bun.sh/](https://bun.sh/ "Bun - fast JavaScript &amp; CSS bundler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">webpack</span> <span class="jser-tag">Tools</span></p>

Zig로 작성된 JavaScript / TypeScript / CSS에 대응한 Transpiler / Bundler 도구.


----

## d-kimuson/type-predicates-generator: generating predicates and assertion function by type definitions.
[github.com/d-kimuson/type-predicates-generator](https://github.com/d-kimuson/type-predicates-generator "d-kimuson/type-predicates-generator: generating predicates and assertion function by type definitions.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

TypeScript 코드로 부터 type predicates을 하는 assertion 함수를 생성하는 도구.

- [TypeScript의 타입 정의에서 타입 가드를 자동 생성하는 type-predicates-generator 소개](https://zenn.dev/kimuson/articles/type_predicates_generator "TypeScript의 타입 정의에서 타입 가드를 자동 생성하는 type-predicates-generator 소개")(일본어)

----
<h1 class="site-genre">도서</h1>

----

## 크리에티브 코딩 교과서(일본어)
[zenn.dev/baroqueengine/books/a19140f2d9fc1a](https://zenn.dev/baroqueengine/books/a19140f2d9fc1a "クリエイティブコーディングの教科書")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">book</span></p>

JavaScript와 Canvas를 이용한 크리에티브 코딩을 주제로한 전자 서적.
Canvas에서의 묘화, 영상 처리, 탐색 알고리즘, 애니메이션 표현 등을 다루고 있다.


----
