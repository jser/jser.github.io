---
title: "2023-06-29: Svelte 4, Ember 5.0, The Cost Of JavaScript in 2023"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-06-29T00:45:08.079Z
category: JSer
tags:
- CSS
- Tools
- React
- TypeScript
- editor

---

JSer.info #649 - Svelte 4가 출시되었습니다.

- [Announcing Svelte 4](https://svelte.dev/blog/svelte-4)
- [Release svelte@4.0.0 · sveltejs/svelte](https://github.com/sveltejs/svelte/releases/tag/svelte%404.0.0)

Node.js 14 지원 종료, CJS 출력은 사라지고 ESM만 지원, Custom Elements 대응을 `tag` 옵션에서 `customElement` 옵션으로 변경이 포함되어있다.
또한, 생성한 파일 크기 경감, 웹사이트 문서 갱신 등도 있습니다.

마이그레이션 가이드와 `npx svelte-migrate@latest svelte-4` 마이그레이션 도구가 공개되어 있습니다.

- [Svelte 4 migration guide • Docs • Svelte](https://svelte.dev/docs/v4-migration-guide)

---

Ember 5.0 출시되었습니다.

- [Ember 5.0 Released](https://blog.emberjs.com/ember-5-0-released/)

메이저 업데이트로 기능추가없이, 파괴적변경만이 있습니다.
비권장이 된 `AutoLocation` 삭제, `@ember/error` 패키지 삭제, `Ember.String` 삭제 등도 있습니다.

---

The Cost Of JavaScript 2023년판 영상과 슬라이드가 공개되었습니다.

- [The Cost Of JavaScript - 2023 - YouTube](https://www.youtube.com/watch?v=ZKH3DLT4BKw)
- [The Cost Of JavaScript in 2023 - Speaker Deck](https://speakerdeck.com/addyosmani/the-cost-of-javascript-in-2023)

JavaScript 다운로드, 실행 코스트에 대한 이야기로, Code Splitting나 Dynamic Import 등 최적화에 대해서도 소개중입니다.
또한, 최근 발전하고 있는 Islands Architecture의 Partial Hydration, Qwik의 Resumalable Hydration, React의 Selective Hydation에 대해서도 다루고 있습니다.

과거 The Cost Of JavaScript는 다음 페이지를 참조해주시길 바랍니다.

- [The Cost Of JavaScript In 2018. Update: The Cost Of JavaScript In 2019… | by Addy Osmani | Medium](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4)
- [The cost of JavaScript in 2019 · V8](https://v8.dev/blog/cost-of-javascript-2019)

또한, 실제 웹사이트 데이터는 [Web Almanac](https://almanac.httparchive.org/ja/2022/)의 [JavaScript](https://almanac.httparchive.org/en/2022/javascript)를 참조하시면 좋을 듯 합니다.


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing Svelte 4
[svelte.dev/blog/svelte-4](https://svelte.dev/blog/svelte-4 "Announcing Svelte 4")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">ReleaseNote</span></p>

Svelte 4 출시.
Node.js 14 지원 종료, CJS 출력은 사라지고 ESM만 지원, Custom Elements를 `tag` 옵션에서 `customElement` 옵션으로 변경.
생성하는 파일 크기 삭감, 웹사이트 문서 갱신

- [Svelte 4 migration guide • Docs • Svelte](https://svelte.dev/docs/v4-migration-guide "Svelte 4 migration guide • Docs • Svelte")
- [Release svelte@4.0.0 · sveltejs/svelte](https://github.com/sveltejs/svelte/releases/tag/svelte%404.0.0 "Release svelte@4.0.0 · sveltejs/svelte")

----

## Ember 5.0 Released
[blog.emberjs.com/ember-5-0-released/](https://blog.emberjs.com/ember-5-0-released/ "Ember 5.0 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 5.0 출시.
메이저 업데이트이며 기능 추가 없이, 파괴적 변경만 있음.
`AutoLocation` 삭제, `@ember/error` 패키지 삭제, `Ember.String` 삭제


----

## Release v6.14.0 · remix-run/react-router
[github.com/remix-run/react-router/releases/tag/react-router%406.14.0](https://github.com/remix-run/react-router/releases/tag/react-router%406.14.0 "Release v6.14.0 · remix-run/react-router")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Router 6.14.0 출시.
`useSubmit`가 JSON와 Text를 지원.


----

## Release v0.18.9 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.18.9](https://github.com/evanw/esbuild/releases/tag/v0.18.9 "Release v0.18.9 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.18.9 출시.
`await using` 수정, autoprefixer 같이 CSS의 prefix 자동으로 추가되도록


----

## Bun v0.6.10 | Bun Blog
[bun.sh/blog/bun-v0.6.10](https://bun.sh/blog/bun-v0.6.10 "Bun v0.6.10 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v0.6.10 출시.
CommonJS 호환성 개선 webpack 동작되도록, `require.main` 지원, `__esModule` 플래그를 해석하도록.
`fs.watch` 구현, V8 `Error.captureStackTrace` 구현.
`bun install`할 때에 라이프사이클 스크립트 실행허가하는 패키지를 정의하는 `trustedDependencies` 필드 지원


----

## Release Notes for Safari Technology Preview 173 | WebKit
[webkit.org/blog/14378/release-notes-for-safari-technology-preview-173/](https://webkit.org/blog/14378/release-notes-for-safari-technology-preview-173/ "Release Notes for Safari Technology Preview 173 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 173 출시.
Safari 17에서 도입 예정 기능 이용 가능한 Technology Preview.
Web Inspector 재설계, 웹애플리케이션을 Dock 추가, JPEG XL 지원, HEIC 지원


----

## Release v3.0.0 · cloudflare/miniflare
[github.com/cloudflare/miniflare/releases/tag/v3.0.0](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0 "Release v3.0.0 · cloudflare/miniflare")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

miniflare v3.0.0 출시.
workerd 이용하도록 되었다.
CLI가 동봉되어 있지 않게되어 `wrangler` 경유해 CLI로 이용.
또한 몇몇 API가 삭제나 변경이 있다.

- [⬆️ Migrating from Version 2 · Miniflare](https://miniflare.dev/get-started/migrating "⬆️ Migrating from Version 2 · Miniflare")

----
<h1 class="site-genre">읽을거리</h1>

----

## Cyclic Dependency Space Toggles
[kizu.dev/cyclic-toggles/](https://kizu.dev/cyclic-toggles/ "Cyclic Dependency Space Toggles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Variables를 사용해서 로직게이트를 구현하는 방법에 대해서.
Cyclic Dependency하는 Variables는 무효로하는 사양을 이용해서, Variables에 if문스러운 표현 구현하는 방법에 대해서.
또한 왜 이런 사양과 구현이 되었는가에 대해서


----

## Next.js App Router Update | Next.js
[nextjs.org/blog/june-2023-update](https://nextjs.org/blog/june-2023-update "Next.js App Router Update | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.js 최신 동작에 대해.
App Router의 Stable화, 거대한 애프리케이션 성능 개선, 문서 개선.
React의 Server Side Component 대응과 Server Actions에 대해


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 2023-06-24 DOM 테스트를 점점 작성하고 싶어지는 Testing Library 세계로 초대 (#phpconfuk) - Google 슬라이드
[docs.google.com/presentation/d/1j6sEAs0LF5jPXs\_mHxvPreqK-lxEL3OxvQAFyXmxbZc/view#slide&#x3D;id.g24bcedd6665\_0\_0](https://docs.google.com/presentation/d/1j6sEAs0LF5jPXs_mHxvPreqK-lxEL3OxvQAFyXmxbZc/view#slide=id.g24bcedd6665_0_0 "2023-06-24 DOM 테스트를 점점 작성하고 싶어지는 Testing Library 세계로 초대 (#phpconfuk) - Google 슬라이드")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">slide</span></p>

DOM 테스트 라이브러리 Testing Library 철학에 대해
DOM를 생성, 테스트 대상을 쿼리로 검색, assertion로 테스트한다.
쿼리에는 WAI-ARIA Role이나 라벨, Test Id등 지정하는 메서드가 있는가 우선도에 대해.

- [About Queries | Testing Library](https://testing-library.com/docs/queries/about/ "About Queries | Testing Library")

----

## The Cost Of JavaScript - 2023 - YouTube
[www.youtube.com/watch?v&#x3D;ZKH3DLT4BKw](https://www.youtube.com/watch?v=ZKH3DLT4BKw "The Cost Of JavaScript - 2023 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">performance</span></p>

JavaScript 코스트에 대한 영상과 슬라이드.
JavaScript 다운로드, 실행 비용.
Code Splitting이나 Dynamic Import등 최적화.
Islands Architecture의 Partial Hydration, Qwik의 Resumalable Hydration, React의 Selective Hydation에 대해.

- [The Cost Of JavaScript in 2023 - Speaker Deck](https://speakerdeck.com/addyosmani/the-cost-of-javascript-in-2023 "The Cost Of JavaScript in 2023 - Speaker Deck")

----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Module Federation: streamline your microfrontends
[module-federation.io/](https://module-federation.io/ "Module Federation: streamline your microfrontends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MicroFrontend</span> <span class="jser-tag">document</span></p>

Microfrontends 개발을 보조하는 Module Federation에 대해 웹사이트가 공개되었다.
문서나 유스케이스, 사용 방법이나 샘플 프로젝트 등도 공개되어있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Panda CSS - Build modern websites using build time and type-safe CSS-in-JS
[panda-css.com/](https://panda-css.com/ "Panda CSS - Build modern websites using build time and type-safe CSS-in-JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

CSS in JS 프레임워크.
TypeScript으로 Type Safe 스타일로 작성도 가능, 도구를 통해 CSS 파일을 출력함으로, 실행할 때는 JS가 없어도 된다.


----

## Codux | Visual IDE for React
[www.codux.com/](https://www.codux.com/ "Codux | Visual IDE for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">editor</span> <span class="jser-tag">Tools</span></p>

React 비주얼 에디터.
GUI에서 컴포넌트 편접이 가능, 코드도 같이 편집할 수 있는 에디터.

- [Meet Codux: The React Visual Editor That Improves Developer Experience — Smashing Magazine](https://www.smashingmagazine.com/2023/06/codux-react-visual-editor-improves-developer-experience/ "Meet Codux: The React Visual Editor That Improves Developer Experience — Smashing Magazine")

----
