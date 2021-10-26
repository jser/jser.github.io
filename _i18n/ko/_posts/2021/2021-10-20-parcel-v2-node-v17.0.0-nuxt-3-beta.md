---
title: "2021-10-20: Parcel v2, Node v17.0.0, Nuxt 3 beta"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-10-20T03:47:20.958Z
category: JSer
tags:
- React
- node.js
- video
- bundler
- browser

---

JSer.info #562 - 빌드 도구 Parcel v2 릴리스.

- [Announcing Parcel v2!](https://parceljs.org/blog/v2/)

Parcel은 특별한 설정 없이(zero configuration) 실행하는 것을 목표로 했기 때문에 v1에서 플러그인 구조가 매우 얇은 형태로 돼 있었다.
Parcel v2에서는 플러그인 구조를 개편하고, 다양한 경우에 대응할 수 있도록 개선됐다.

- [Plugins](https://parceljs.org/features/plugins/)

또, Tree Shaking을 기본적으로 활성화, [SWC](https://github.com/swc-project/swc) 기반의 JavaScript 컴파일러 채택, Modern과 Legacy 분리 빌드, Image optimizer 등이 추가 됐다.
그 외에도 bundle 인라인화, 라이브러리 용 빌드 모드 지원, C++이나 Rust로 코어 모듈 일부를 수정하여 빌드 성능을 개선했다.

Parcel v1에서 마이그레이션 하는 방법은 공식 문서를 참고한다.

- [Migration](https://parceljs.org/getting-started/migration/)

----

Node.js 17.0.0 릴리스.

- [Node v17.0.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v17.0.0/)
- [Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium](https://medium.com/the-node-js-collection/node-js-17-is-here-8dba1e14e382)

Node의 홀수 버전은 LTS가 아니며 `Current` 버전이다.
현재 Node의 LTS는 12와 14 이며 2021년 10월 26일에 Node 16이 LTS로 추가된다.

- [Releases | Node.js](https://nodejs.org/en/about/releases/)

Node.js 17에서는 `readline` 모듈의 Promise 대응, OpenSSL 3.0으로 갱신, V8 9.5으로 갱신, npm 8.0.0으로 갱신 됐고, 스택 트레이스에 Node 버전을 포함하도록 변경됐다.
또 웹 표준의 `strcturedClone()`과 `DOMException`도 지원한다.

[structuredClone()](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone)은 `postMessage` 등에서 내부적으로 사용하고 있던 (DOM을 포함하여) 객체의 복제 메커니즘을 함수로 공개한 메서드다.
최근에 WHATWG HTML 사양에 추가되어 [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=1722576)와 [Deno](https://deno.com/blog/v1.13#support-for-self.structuredclone())에서 구현됐으며 [Chrome](https://bugs.chromium.org/p/chromium/issues/detail?id=1233571), [Safari](https://bugs.webkit.org/show_bug.cgi?id=228331), [core-js](https://github.com/zloirock/core-js/issues/969)에서는 구현이 진행되고 있다.

- [Expose structuredClone by surma · Pull Request #3414 · whatwg/html](https://github.com/whatwg/html/pull/3414)

`structuredClone()`는 `JSON.parse` / `JSON.strinfigy`가 지원하지 않는 객체(Map이나 RegExp 등)의 복제도 지원하므로 DOM 외를 다룰 때에도 유용하게 사용할 수 있다.

- [구조화 복제 알고리즘(the structured clone algorithm)을 사용한 객체 깊은 복사](https://zenn.dev/petamoriken/articles/ad1e943d8d113c)(일본어)

`structuredClone()`로 복제할 수 없는 경우에는 `DOMException` 예외가 발생해야 하므로 `DOMException`도 함께 구현됐다.

Node 17에는 Node 16의 변경 사항도 포함되는 버전으로 자세한 내용은 다음 문서를 참고하길 바란다.

- [2021-04-27: Node.js 16.0.0, Chrome 91 beta, Prisma(Ready for production) - JSer.info](https://jser.info/ko/2021/04/27/node.js-16.0.0-chrome-91-beta-prismaready-for-production/)
- [Node.js v17의 주요 변경 사항 - 별로 힘들지 않은 블로그](https://shisama.hatenablog.com/entry/2021/10/20/114721)


----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing Parcel v2!
[parceljs.org/blog/v2/](https://parceljs.org/blog/v2/ "Announcing Parcel v2!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v2 릴리스.
플러그인 구조 개편, Tree Shaking을 기본적으로 활성화, SWC 기반의 JavaScript 컴파일러로 변경, Modern과 Legacy 빌드 분리 출력, Image optimizer 추가.
bundle의 인라인화, 라이브러리 용 빌드 지원, 개발 시 요청 된 시점에 지연 빌드 할 수 있게 됐다.
그 외로도 Source Map 라이브러리를 Rust로 재작성하여 성능과 파일 감시 시스템을 개선했다.

- [Migration](https://parceljs.org/getting-started/migration/ "Migration")

----

## Deno 1.15 Release Notes | Deno Blog
[deno.com/blog/v1.15](https://deno.com/blog/v1.15 "Deno 1.15 Release Notes | Deno Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.15 릴리스.
Web Crypto API 갱신, FFI 개선, `deno uninstall` 커맨드 추가, `deno lint --watch` 추가.
`Deno.test`가 들여쓰기 한 중첩된 테스트 케이스를 지원, V8 9.5로 갱신, Node.js 호환 모듈을 이용할 수 있는 `--compat` 플러그 추가.

- [Deno v1.15에 도입된 Node.js 호환 모드 소개](https://zenn.dev/uki00a/articles/node-compat-mode-introduced-in-deno-v1-15 "Deno v1.15에 도입된 Node.js 호환 모드 소개")(일본어)

----

## Nuxt - Introducing Nuxt 3 Beta
[nuxtjs.org/announcements/nuxt3-beta/](https://nuxtjs.org/announcements/nuxt3-beta/ "Nuxt - Introducing Nuxt 3 Beta")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt 3 베타 릴리스.
Vue 3와 Vite 대응.
새로운 서버 엔진 Nitro Engine을 도입하여 Node.js 서버, Serverless, Service Worker 등 각각의 형태로 디플로이 가능하게 됐다.


----

## GitHub Advisory Database now powers npm audit | The GitHub Blog
[github.blog/2021-10-07-github-advisory-database-now-powers-npm-audit/](https://github.blog/2021-10-07-github-advisory-database-now-powers-npm-audit/ "GitHub Advisory Database now powers npm audit | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Github</span> <span class="jser-tag">news</span></p>

이제 `npm audit`은 GitHub Advisory Database를 기반으로 취약성 정보를 분석한다.

----

## Release v7.0.0 · pinojs/pino
[github.com/pinojs/pino/releases/tag/v7.0.0](https://github.com/pinojs/pino/releases/tag/v7.0.0 "Release v7.0.0 · pinojs/pino")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

pino 7.0.0 릴리스.
로그 처리를 별도의 Thread 등에 전달하는 `pino.transport()` 추가, `pino.multistream()` 추가, TypeScript의 타입 선언을 패키지에 포함하도록 변경

- [Welcome to pino@7.0.0 - and the era of worker\_thread transport - NearForm](https://www.nearform.com/blog/pino7-0-0-pino-transport-worker_thread-transport/ "Welcome to pino@7.0.0 - and the era of worker\_thread transport - NearForm")

----

## Node v17.0.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.0.0/](https://nodejs.org/en/blog/release/v17.0.0/ "Node v17.0.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v17.0.0 릴리스.
`readline` 모듈의 Promise 대응, OpenSSL 3.0으로 업데이트, V8 9.5로 업데이트, npm 8.0.0으로 업데이트, 스택 트레이스에 Node 버전을 표시한다.
또, 웹 표준인 `strcturedClone()`과 `DOMException`을 지원한다.

- [Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium](https://medium.com/the-node-js-collection/node-js-17-is-here-8dba1e14e382 "Node.js 17 is here!. This blog was written by Bethany… | by Node.js | Node.js Collection | Oct, 2021 | Medium")
- [Release v8.0.0 · npm/cli](https://github.com/npm/cli/releases/tag/v8.0.0 "Release v8.0.0 · npm/cli")

----
<h1 class="site-genre">아티클</h1>

----

## A Visual Guide to React Rendering - Cheat Sheet | Alex Sidorenko
[alexsidorenko.com/blog/react-render-cheat-sheet/](https://alexsidorenko.com/blog/react-render-cheat-sheet/ "A Visual Guide to React Rendering - Cheat Sheet | Alex Sidorenko")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">cheatsheet</span> <span class="jser-tag">article</span></p>

그림과 함께 React의 렌더링 케이스를 알기 쉽게 설명한 가이드 / 치트시트


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## RF21 – Naman Goel – Rethinking CSS - Introducing Stylex - YouTube
[www.youtube.com/watch?v&#x3D;ur-sGzUWId4](https://www.youtube.com/watch?v=ur-sGzUWId4 "RF21 – Naman Goel – Rethinking CSS - Introducing Stylex - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">facebook</span> <span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">video</span></p>

Facebook의 Atomic CSS 구현체인 Stylex 소개 영상.
Stylex는 React-Native와 같이 스타일을 작성할 수 있는 툴킷으로 Atomic CSS에 의해 선형적으로 증가하는 CSS 양을 비선형적으로 관리할 수 있다.
2021년 연말에 베타 버전을 릴리스 할 예정.

- [Facebook CSS-in-JS Solution Stylex Introduced at React Finland 2021](https://www.infoq.com/news/2021/10/facebook-css-js-stylex/ "Facebook CSS-in-JS Solution Stylex Introduced at React Finland 2021")

----

## React Finland 2021 - Talks - YouTube
[www.youtube.com/playlist?list&#x3D;PL-a9lBflNu2opNHeISTnlHgGVlI7oGLXi](https://www.youtube.com/playlist?list=PL-a9lBflNu2opNHeISTnlHgGVlI7oGLXi "React Finland 2021 - Talks - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Finland 2021의 발표 영상 공개

- [React Finland 2021 - Sessions - YouTube](https://www.youtube.com/playlist?list=PL-a9lBflNu2rhk1vr3yr4mdRzzUb_nj5P "React Finland 2021 - Sessions - YouTube")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## PrivacyTests.org: open-source tests of web browser privacy
[privacytests.org/](https://privacytests.org/ "PrivacyTests.org: open-source tests of web browser privacy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">privacy</span></p>

브라우저 별 Finger Printing이나 Tracking 관련 대책 등의 정책 기능을 정리한 사이트.


----

## oslabs-beta/sapling: Sapling - A convenient way to traverse your React app in VS Code
[github.com/oslabs-beta/sapling](https://github.com/oslabs-beta/sapling "oslabs-beta/sapling: Sapling - A convenient way to traverse your React app in VS Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">React</span> <span class="jser-tag">Extension</span></p>

React 컴포넌트 트리를 에디터의 사이드 패널에 표시하는 VSCode 확장.
Root가 되는 컴포넌트를 포함하는 파일을 선택하면 그 컴포넌트가 갖고 있는 컴포넌트를 트리로 표시해준다

- [Sapling - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=team-sapling.sapling "Sapling - Visual Studio Marketplace")
- [Introducing Sapling: a VS Code Extension for Traversing React Component Hierarchy | by Team Sapling | Oct, 2021 | JavaScript in Plain English](https://javascript.plainenglish.io/introducing-sapling-a-vs-code-extension-for-traversing-your-react-component-hierarchy-3ac94d95887e "Introducing Sapling: a VS Code Extension for Traversing React Component Hierarchy | by Team Sapling | Oct, 2021 | JavaScript in Plain English")

----
<h1 class="site-genre">도서</h1>

----

## Practical Svelte - Create Performant Applications with the Svelte Component Framework | Alex Libby | Apress
[www.apress.com/gp/book/9781484273739](https://www.apress.com/gp/book/9781484273739 "Practical Svelte - Create Performant Applications with the Svelte Component Framework | Alex Libby | Apress")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">book</span></p>

Svelte를 사용한 웹 애플리케이션 개발 입문서


----

## Sairyss/domain-driven-hexagon: Guide on Domain-Driven Design, Hexagonal architecture, best practices etc.
[github.com/Sairyss/domain-driven-hexagon](https://github.com/Sairyss/domain-driven-hexagon "Sairyss/domain-driven-hexagon: Guide on Domain-Driven Design, Hexagonal architecture, best practices etc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DDD</span> <span class="jser-tag">document</span> <span class="jser-tag">TypeScript</span></p>

도메인 주도 개발(DDD) 가이드.
DDD에 관한 용어, 설계 뿐 아니라 TypeScript 기반 예제를 이용한 기술적 전략에 대해서도 다룬다.


----
