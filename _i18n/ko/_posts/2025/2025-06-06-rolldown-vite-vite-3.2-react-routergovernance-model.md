---
title: "2025-06-06: Rolldown-Vite, Vite 3.2, React Router의 Governance Model"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-06-05T22:17:29.129Z
category: JSer
tags:
- vite
- Rust
- nodejs
- babel
- DOM

---

JSer.info #737 - Rust 기반 Rolldown 이용한 Rolldown-Vite가 출시되었습니다.

- [Announcing Rolldown-Vite | VoidZero](https://voidzero.dev/posts/announcing-rolldown-vite)

Rolldown-Vite는, Rust로 작성된 Rolldown 기반 Vite로, `rolldown-vite` 패키지로 공개됩니다.
Rolldown는 Rust로 만든 JavaScript 번들러인데, Rollup와 호환성을 갖으면서 성능 향상을 목표로 합니다.
앞으로 Vite에서 이행할 때 호환성이나 성능 피드백을 얻을 목적으로, `rolldown-vite` 패키지를 공개했습니다.

Rolldown-Vite가 안정되면 `vite` 패키지와 통합될 예정입니다.

---

Vitest 3.2가 출시되었습니다.

- [Vitest 3.2 is out! | Vitest](https://vitest.dev/blog/vitest-3-2.html)

`workspace` 옵션을 비권장으로하고, `projects` 옵션/`vitest.workspace` 파일을 권장하도록 변경되었습니다.
또한, `context.annotate` API 추가, `test.extends`에 `scope` 옵션 추가, `locators.extend` 추가, `context.signal` 추가 신기능도 포함되어 있습니다. `using`(Explicit Resource Management)으로 mock 함수 자동 클린업하도록 되었으며, `sequence.groupOrder` 옵션도 추가되었습니다.

---

React Router의 Governance Model 관련해 상세한 설명한 글을 공개했습니다.

- [React Router Open Governance | Remix](https://remix.run/blog/rr-governance)
- [react-router/GOVERNANCE.md at main · remix-run/react-router](https://github.com/remix-run/react-router/blob/main/GOVERNANCE.md#new-feature-process)

스테이지 제도를 포함한 개발 프로세스에 관련한 상세한 설명 및 React Router의 앞으로의 개발 방침이 작성되어 있습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v8.0.0-beta.0 · babel/babel
[github.com/babel/babel/releases/tag/v8.0.0-beta.0](https://github.com/babel/babel/releases/tag/v8.0.0-beta.0 "Release v8.0.0-beta.0 · babel/babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel v8.0.0-beta.0 출시.


----

## Vitest 3.2 is out! | Vitest
[vitest.dev/blog/vitest-3-2.html](https://vitest.dev/blog/vitest-3-2.html "Vitest 3.2 is out! | Vitest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">test</span> <span class="jser-tag">ReleaseNote</span></p>

Vitest 3.2 출시.
`workspace` 옵션 비권장 `vitest.workspace` 파일을 권장 하도록 변경.
`context.annotate` API 추가, `test.extends`에 `scope` 옵션을 추가, `locators.extend` 추가, `context.signal` 추가.
`using`으로 mock 함수르 자동 클린업할 수 있으며, `sequence.groupOrder` 옵션 추가


----

## Release astro@5.9.0 · withastro/astro
[github.com/withastro/astro/releases/tag/astro%405.9.0](https://github.com/withastro/astro/releases/tag/astro%405.9.0 "Release astro@5.9.0 · withastro/astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro v5.9.0 출시.
실험적 기능으로 Content Security Policy(CSP)지원 추가, content loader으로 Markdown 렌더러 제공.
어댑터 대상 `supportedAstroFeatures` 옵션 추가


----

## ECMAScript proposal updates @ 2025-05 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2025/06/05/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2025/06/05/ecmascript-proposal-update "ECMAScript proposal updates @ 2025-05 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">news</span></p>

2025년 5월 TC39 미팅에서 ECMAScript Proposal 상태 변경 정리.
Inspector/More Random Functions가 Stage 1으로 신규 추가.
SeededPRNG/`Math.clamp`가 Stage 2으로.
Error.isError가 Stage 4가 되어 ES2026에 추가.


----
<h1 class="site-genre">읽을거리</h1>

----

## Announcing Rolldown-Vite | VoidZero
[voidzero.dev/posts/announcing-rolldown-vite](https://voidzero.dev/posts/announcing-rolldown-vite "Announcing Rolldown-Vite | VoidZero")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">Rust</span> <span class="jser-tag">article</span></p>

Rolldown-Vite 출시.
Rolldown 기반 Vite로 `rolldown-vite` 패키지 공개


----

## Resilient Import Maps - Better Theme Development and Beyond (2025) - Shopify
[shopify.engineering/resilient-import-maps](https://shopify.engineering/resilient-import-maps "Resilient Import Maps - Better Theme Development and Beyond (2025) - Shopify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

Import Maps은 여럿을 정의하면 동작하지 않아서, 사양이랑 브라우저를 수정한 이야기


----

## Seamlessly Blend PHP with Node.js
[blog.platformatic.dev/seamlessly-blend-php-with-nodejs](https://blog.platformatic.dev/seamlessly-blend-php-with-nodejs "Seamlessly Blend PHP with Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">php</span> <span class="jser-tag">article</span> <span class="jser-tag">Rust</span></p>

Node.js에서 PHP 동작시키는 `@platformatic/php-node`에 대하여.

- [platformatic/php-node: PHP HTTP Request handler for Node.js](https://github.com/platformatic/php-node "platformatic/php-node: PHP HTTP Request handler for Node.js")

----

## minify 효과를 최대한으로 끌어내는 TypeScript 코드 작성
[zenn.dev/j\_sakamoto/articles/1b5e1d563b1c30](https://zenn.dev/j_sakamoto/articles/1b5e1d563b1c30 "minify 효과를 최대한으로 끌어내는 TypeScript 코드 작성")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

minify 되기 쉬운 코드에 대하여


----

## React Router Open Governance | Remix
[remix.run/blog/rr-governance](https://remix.run/blog/rr-governance "React Router Open Governance | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

React Router의 Governance Model 관련하여.
스테이지 제도를 포함한 개발 프로세스 다룸

- [react-router/GOVERNANCE.md at main · remix-run/react-router](https://github.com/remix-run/react-router/blob/main/GOVERNANCE.md#new-feature-process "react-router/GOVERNANCE.md at main · remix-run/react-router")

----

## Exploring the OKLCH ecosystem and its tools—Martian Chronicles, Evil Martians’ team blog
[evilmartians.com/chronicles/exploring-the-oklch-ecosystem-and-its-tools](https://evilmartians.com/chronicles/exploring-the-oklch-ecosystem-and-its-tools "Exploring the OKLCH ecosystem and its tools—Martian Chronicles, Evil Martians’ team blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css</span> <span class="jser-tag">color</span> <span class="jser-tag">article</span></p>

OKLCH 사용해 명도와 채도를 일정하게 유지하면서 테마를 다루는 방법


----

## 프로파일러를 이용해서 Node.js 서버의 리스폰스 시간을 200 초 → 20 초 단축한 이야기
[zenn.dev/dinii/articles/improve-latency-with-profiler](https://zenn.dev/dinii/articles/improve-latency-with-profiler "프로파일러를 이용해서 Node.js 서버의 리스폰스 시간을 200 초 → 20 초 단축한 이야기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`node:async_hooks` 사용해 로그에서, 블록킹 처리를 발견해 Cloud Profiler 사용한 처리를 개선한 이야기


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JavaScript 프레임워크가 DOM 렌더링하는 3가지 방법 - YouTube
[www.youtube.com/watch?v&#x3D;0C-y59betmY](https://www.youtube.com/watch?v=0C-y59betmY "JavaScript 프레임워크가 DOM 렌더링하는 3가지 방법 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">video</span></p>

프레임워크 DOM 렌더링 방법 해설 영상, Dirty Check, Virtual DOM, Fine-Grained Rendering 다룸


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## almadoro/react-just: React Server Components without a framework. Powered by Vite
[github.com/almadoro/react-just](https://github.com/almadoro/react-just "almadoro/react-just: React Server Components without a framework. Powered by Vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span></p>

Vite 기반 React Server Component 지원하는 프레임워크.


----
