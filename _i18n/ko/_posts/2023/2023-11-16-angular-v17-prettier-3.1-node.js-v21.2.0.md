---
title: "2023-11-16: Angular v17, Prettier 3.1, Node.js v21.2.0"
author: "azu"
translator: rewrite0w0
layout: post
date: 2023-11-16T12:22:34.462Z
category: JSer
tags:
- Tools
- performance
- browser
- Angular
- astro

---

JSer.info #669 - Angular v17 출시되었습니다.

- [Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog](https://blog.angular.io/introducing-angular-v17-4d7033312e4b)
- [Release v17.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/17.0.0)

Node.js 16 지원 종료, [문서 사이트](https://angular.dev/) 업데이트, `@if`나 `@for`같은 built-in control flow 추가되었습니다.
새로운 프로젝트에서 SSR를 위한 hydration를 기본값으로 유효, `ng serve`와 `ng build`에 Vite와 esbuild 이용가능하도록 하는 변경도 포함되었습니다.

----

Prettier 3.1 출시되었습니다.

- [Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier](https://prettier.io/blog/2023/11/13/3.1.0.html)

`--experimental-ternaries`으로 삼항연산자의 새로운 규칙을 체험할 수 있으며, 피드백을 기다리고 있습니다.

- [A curious case of the ternaries · Prettier](https://prettier.io/blog/2023/11/13/curious-ternaries)

Babel 7.23.0에서 지원되고 있는 Source Phase Imports/Deferred Import Evaluation/Optional Chaining Assignments 구문 지원, Angular 17에서 추가된 control flow 구문 지원도 추가됩니다.

----

Node.js v21.2.0 출시되었습니다.

- [Node v21.2.0 (Current) | Node.js](https://nodejs.org/blog/release/v21.2.0)

`__dirname`와 `__filename`에 ESM 버전 `import.meta.dirname`와 `import.meta.filename`가 추가되었습니다. `import.meta`은 ECMAScript에는 정의되어 있지 않으며, 호스트 환경(브라우저/Node.js/Bun/Deno) 등이 각각 정의하고 있습니다.
이 정의를 [import.meta Registry](https://github.com/wintercg/import-meta-registry/tree/main)에서 정리했습니다.

- [wintercg/import-meta-registry: A registry for import.meta properties](https://github.com/wintercg/import-meta-registry/tree/main)

또한, `fs/promises` 스택스테리스 추가, `navigator.language`/`navigator.platform` 추가, `--no-experimental-global-navigator` 플래그 추가도 있습니다.


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog
[blog.angular.io/introducing-angular-v17-4d7033312e4b](https://blog.angular.io/introducing-angular-v17-4d7033312e4b "Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v17 출시.
Node.js 16 지원, 문서 사이트 업데이트, `@if`이나 `@for`등의 built-in control flow 지원.
새로운 프로젝트에서 SSR에 의한 hydration 기본적으로 유효, `ng serve`와 `ng build`에 Vite와 esbuild 이용 가능

- [Release v17.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/17.0.0 "Release v17.0.0 · angular/angular")

----

## Astro 3.5: i18n Routing | Astro
[astro.build/blog/astro-350/](https://astro.build/blog/astro-350/ "Astro 3.5: i18n Routing | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 3.5 출시.
prefetch 기능을 코어에 통합, `<ViewTransitions handleForms />` 추가, `addMiddleware` 추가, Qwik 지원.
실험적 기능 i18n Routing API 추가, `contentCollectionCache` 옵션 추가

- [Release astro@3.5.0 · withastro/astro](https://github.com/withastro/astro/releases/tag/astro%403.5.0 "Release astro@3.5.0 · withastro/astro")

----

## Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier
[prettier.io/blog/2023/11/13/3.1.0.html](https://prettier.io/blog/2023/11/13/3.1.0.html "Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 3.1 출시.
`--experimental-ternaries` 삼항연산자 새 규칙 체험 가능.
Babel 7.23.0에서 지원되는 구문 지원, Angular 17에서 추가 된 control flow 구문 지원


----

## Node v21.2.0 (Current) | Node.js
[nodejs.org/blog/release/v21.2.0](https://nodejs.org/blog/release/v21.2.0 "Node v21.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v21.2.0 출시.
`import.meta.dirname`와 `import.meta.filename` 추가, `fs/promises`에 스택트레이스 추가.
`navigator.language`/`navigator.platform` 추가, `--no-experimental-global-navigator` 플래그 추가.


----

## Project Status: Maintenance Reboot · Issue #5027 · mochajs/mocha
[github.com/mochajs/mocha/issues/5027](https://github.com/mochajs/mocha/issues/5027 "Project Status: Maintenance Reboot · Issue #5027 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mocha</span> <span class="jser-tag">news</span> <span class="jser-tag">issue</span></p>

Mocha 프로젝트를 리붓하고 유지보수 재개한다는 공지.


----

## Bun v1.0.12 | Bun Blog
[bun.sh/blog/bun-v1.0.12](https://bun.sh/blog/bun-v1.0.12 "Bun v1.0.12 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.12 출시.
`bun -e "<code>"` 지원, `bun --env-file <path>` 지원, `import.meta.env` 지원.
`expect.unreachable()` 추가, `mock.module(...)` 개선


----
<h1 class="site-genre">읽을거리</h1>

----

## HTML DOM — Phuoc Nguyen
[phuoc.ng/collection/html-dom/](https://phuoc.ng/collection/html-dom/ "HTML DOM — Phuoc Nguyen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">tutorial</span></p>

DOM API 색인 같은 사이트


----

## 사양과 구현에서 이해하는 HTML의 loading 속성 - dwango on GitHub
[dwango.github.io/articles/html-loading-attribute/](https://dwango.github.io/articles/html-loading-attribute/ "양과 구현에서 이해하는 HTML의 loading 속성 - dwango on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

브라우저 마다 `img`/`iframe`의 `loading=lazy` 동작 차이에 대하여


----

## The end of third-party cookies and its impact on Miro apps and integrations | by Darren | Miro Engineering | Nov, 2023 | Medium
[medium.com/miro-engineering/the-end-of-third-party-cookies-and-its-impact-on-miro-apps-and-integrations-ee73358cda1e](https://medium.com/miro-engineering/the-end-of-third-party-cookies-and-its-impact-on-miro-apps-and-integrations-ee73358cda1e "The end of third-party cookies and its impact on Miro apps and integrations | by Darren | Miro Engineering | Nov, 2023 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

서드파티 Cookie 삭제가 이를 사용하는 사이트에게 주는 영상와 대응에 대해.


----

## A faster web in 2024 - rviscomi.dev
[rviscomi.dev/2023/11/a-faster-web-in-2024/](https://rviscomi.dev/2023/11/a-faster-web-in-2024/ "A faster web in 2024 - rviscomi.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Google의 Web Vitals 지표로 FID(First Input Delay) 대신 INP(Interaction to Next Paint) 이용하도록 변경하는 것에 대하여.
INP를 개선하는 방법으로 태스트 분리, LCP와 lazy loading 문제, fetchprioty나 Speculation Rules API 등에 관하여.


----

## Moving back to React
[daily.dev/blog/moving-back-to-react](https://daily.dev/blog/moving-back-to-react "Moving back to React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">refactoring</span></p>

Next.js 호환성을 위해 Preact에서 React으로 마이그레이션 한 이야기.
Preact와 React 호환성 문제나 실제 만나는 문제에 대해


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JetBrains JavaScript Day 2023 - YouTube
[www.youtube.com/playlist?list&#x3D;PLQ176FUIyIUZmRHOyz\_n9iy2qfHo4\_GRT](https://www.youtube.com/playlist?list=PLQ176FUIyIUZmRHOyz_n9iy2qfHo4_GRT "JetBrains JavaScript Day 2023 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JetBrains JavaScript Day 2023 영상 정리


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## SpeedVitals - Website Speed Test &amp; Monitoring
[speedvitals.com/](https://speedvitals.com/ "SpeedVitals - Website Speed Test &amp; Monitoring")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

WebPageTest 같이 장소와 기기를 지정해 성능 테스트 가능한 서비스.
URL 지정해서 Lighthouse 사용한 계측 데이터 확인 가능


----
