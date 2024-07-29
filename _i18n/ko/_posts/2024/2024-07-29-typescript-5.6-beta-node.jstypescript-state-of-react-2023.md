---
title: "2024-07-29: TypeScript 5.6 Beta, Node.js 실험적인 TypeScript 지원, State of React 2023"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-07-29T01:18:59.277Z
category: JSer
tags:
- nodejs
- ECMAScript
- React
- TypeScript
- Conference

---

JSer.info #701 - TypeScript 5.6 Beta가 출시되었어요.

- [Announcing TypeScript 5.6 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/)

ESLint의 `no-constant-binary-expression`과 닮은 체크를 하고, 늘 true/nullish가 되는 잘못된 작성 방법을 컴파일러 에러하는 변경이 있어요.

- [Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2022/07/interesting-bugs-caught-by-no-constant-binary-expression/)

Iterator Helper 지원, ES2022의 Arbitrary module namespace identifier names 지원, `--noUncheckedSideEffectImports` 플래그 추가도 있어요.
또한, 자료형 체크없이 파일 출력하는 `--noCheck`플래그 추가도 했어요

----

Node.js에 실험적인 플래그 `--experimental-strip-types`가 구현되었어요.

- [module: add --experimental-strip-types by marco-ippolito · Pull Request #53725 · nodejs/node](https://github.com/nodejs/node/pull/53725)

`--experimental-strip-types` 플래그 사용하면, TypeScript 코드에서 자료형 정보를 삭제해서 JavaScript 파일로 실행되어요.

[Node.js의TypeScript 지원에 관하여](https://gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250)에서는, Node.js의 TypeScript 지원이 어떤 경위로 진행되었는가 정리되어 있어요.
또한 실험 단계에서 문제점이 많기에, 정식으로 지원될 지 모르겠지만, 앞으로 방침에 대해 Issue에서 토론되었어요.

- [Roadmap for experimental TypeScript support · Issue #217 · nodejs/loaders](https://github.com/nodejs/loaders/issues/217)

----

[State of React 2023](https://2023.stateofreact.com/)가 공개되었어요.
React에 관련된 개발자 앙케이트 결과 레포트에요.

React의 기능, 상태 관리, 데이터 페치, Meta-Framework, 어떤 애플리케이션을 만들고 있는가 등에 대해 여러 항목마다 결과가 정리되어 있어요.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Node.js — Node v22.5.1 (Current)
[nodejs.org/en/blog/release/v22.5.1](https://nodejs.org/en/blog/release/v22.5.1 "Node.js — Node v22.5.1 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.5.1 출시.
Node.js v22.5.0 포함된 `npm ci` 등이 크래시하는 regression를 수정

- [Fix the bug caused by fast api changes in v22.5.0 and have a post-mortem by anonrig · Pull Request #53934 · nodejs/node](https://github.com/nodejs/node/pull/53934?hss_channel=tw-91985735 "Fix the bug caused by fast api changes in v22.5.0 and have a post-mortem by anonrig · Pull Request #53934 · nodejs/node")

----

## Release pnpm 9.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v9.6.0](https://github.com/pnpm/pnpm/releases/tag/v9.6.0 "Release pnpm 9.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v9.6.0 출시.
`pnpm.executionEnv.nodeVersion`에서 Node.js 버전 지정 가능.
`catalogs:` 지원 개선 및 수정


----

## It&#039;s official, Meteor 3.0 Official Release is out! - announce - Meteor.js forums
[forums.meteor.com/t/its-official-meteor-3-0-official-release-is-out/61860](https://forums.meteor.com/t/its-official-meteor-3-0-official-release-is-out/61860 "It&#039;s official, Meteor 3.0 Official Release is out! - announce - Meteor.js forums")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">nodejs</span></p>

Meteor.js 3.0 출시.
비동기 응답 개선, Node.js 20 지원, Express의 middleware에 대응

- [Meteor 3.0 Migration Guide | Meteor 3.0 Migration Guide](https://v3-migration-docs.meteor.com/ "Meteor 3.0 Migration Guide | Meteor 3.0 Migration Guide")

----

## July 22, 2024 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2024-07-22.html](https://react-spectrum.adobe.com/releases/2024-07-22.html "July 22, 2024 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Spectrum July 22, 2024 출시.
React 19 RC 대응, TableView/ListView/ListBoxのVirtualization 개선, Toast의 focus management 개선.
아이콘을 Apache 2.0 License으로 변경


----

## A new path for Privacy Sandbox on the web
[privacysandbox.com/news/privacy-sandbox-update/](https://privacysandbox.com/news/privacy-sandbox-update/ "A new path for Privacy Sandbox on the web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">news</span></p>

Chrome의 3rd Party Cookie 폐지 계획이 철회됨.


----

## Sass: Node Sass is end-of-life
[sass-lang.com/blog/node-sass-is-end-of-life/](https://sass-lang.com/blog/node-sass-is-end-of-life/ "Sass: Node Sass is end-of-life")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">Sass</span> <span class="jser-tag">news</span></p>

LibSass의 Node.js 래퍼인 Node Sass 지원이 종료.
DartSass가 관리되고 있으므로, 이쪽으로 이행을 권장


----

## Bun v1.1.21 | Bun Blog
[bun.sh/blog/bun-v1.1.21](https://bun.sh/blog/bun-v1.1.21 "Bun v1.1.21 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.21 출시.
`--fetch-preconnect=<url>` 플래그 추가, Remix 대응 개선, `bun build --packages=external` 추가


----

## Node.js — Node v20.16.0 (LTS)
[nodejs.org/en/blog/release/v20.16.0](https://nodejs.org/en/blog/release/v20.16.0 "Node.js — Node v20.16.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.16.0 출시.
`process.getBuiltinModule(id)` 추가, OpenSSL 커스텀 엔진 지원 폐지에 따른 `clientCertEngine` 옵션 비권장으로 변경


----

## Announcing TypeScript 5.6 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/ "Announcing TypeScript 5.6 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.6 Beta 출시.
ESLint의 `no-constant-binary-expression`처럼 늘 true/nullish가 되는 잘못된 작성 방법을 에러로 보이도록 변경, Iterator Helper 지원.
ES2022의 Arbitrary module namespace identifier names 지원, `--noUncheckedSideEffectImports`플래그 추가.
자료형 체크없이 파일 출력 가능한 `--noCheck`플래그 추가

- [Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2022/07/interesting-bugs-caught-by-no-constant-binary-expression/ "Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter")

----

## Astro 4.12: Server Islands | Astro
[astro.build/blog/astro-4120/](https://astro.build/blog/astro-4120/ "Astro 4.12: Server Islands | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 4.12 출시.
Next.js의 Partial Prerendering 비슷한 기능으로 Server Islands를 실험적 추가, `inferRemoteSize` 추가


----
<h1 class="site-genre">읽을거리</h1>

----

## CSS Grid Areas
[ishadeed.com/article/css-grid-area/](https://ishadeed.com/article/css-grid-area/ "CSS Grid Areas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Grid에 대해 해설.
grid-template-areas 사용해 Grid 레이아웃 방법에 대해 여러 예시를 가지고 해설


----

## State of React 2023
[2023.stateofreact.com/en-US](https://2023.stateofreact.com/en-US "State of React 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Survey</span></p>

State of React 2023 결과 공개.
React 기능, 상태관리, 데이터 페치, Meta-Framework, 어떤 애플리케이션을 만드는가


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JSConf Budapest 2024 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshEczPCbFGVGd-hj1DR7\_SKy](https://www.youtube.com/playlist?list=PL37ZVnwpeshEczPCbFGVGd-hj1DR7_SKy "JSConf Budapest 2024 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JSConf Budapest 2024 영상 목록

- [26-28 June, JSConfBP 2024](https://jsconfbp.com/ "26-28 June, JSConfBP 2024")

----

## Temporal를 둘러싼 사양 정리 - Speaker Deck
[speakerdeck.com/sajikix/temporalwoqu-rijuan-kushi-yang-wozheng-li-suru](https://speakerdeck.com/sajikix/temporalwoqu-rijuan-kushi-yang-wozheng-li-suru "Temporal를 둘러싼 사양 정리 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">slide</span></p>

ECMAScript Proposal Stage 3의 Temporal 관련한 사양 슬라이드.
ECMA-402, Unicode(CLDR), IETF(BCP47/RFC3339/RFC9557), IANA(Timezone)에 관하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Node.js의 TypeScript 지원에 대해
[gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250](https://gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250 "Node.js의 TypeScript 지원에 대해")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">TypeScript</span></p>

Node.js에 실험적 기능으로 TypeScript 코드에서 자료형 정의를 제외하고 JavaScript 실행하는 `--experimental-strip-types` 플래그가 구현된 경위에 대해


----
<h1 class="site-genre">도서</h1>

----

## Exploring JavaScript (ES2024 Edition)
[exploringjs.com/js/index.html](https://exploringjs.com/js/index.html "Exploring JavaScript (ES2024 Edition)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

Exploring JavaScript의 ES2024 대응판이 공개


----
