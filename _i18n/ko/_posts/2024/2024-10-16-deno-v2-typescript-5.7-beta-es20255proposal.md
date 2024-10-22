---
title: "2024-10-16: Deno v2, TypeScript 5.7 Beta, ES2025에 들어 갈 Proposal 다섯가지"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-10-15T15:41:43.168Z
category: JSer
tags:
- deno
- Tools
- Bun
- css
- ESLint

---

JSer.info #711 - Deno v2.0.0가 출시되었습니다.

- [Announcing Deno 2](https://deno.com/blog/v2.0)
- [Deno 2.0 Release Candidate](https://deno.com/blog/v2.0-release-candidate)

Node.js와 호환성 개선, JSR 지원 개선, Workspace 지원이 행해졌습니다.
Deno 1.x부터 2.x으로 이행 가이드 공개되었습니다.

- [Deno 1.x to 2.x Migration Guide](https://docs.deno.com/runtime/reference/migration_guide/)

---

TypeScript 5.7 Beta가 출시되었습니다

- [Announcing TypeScript 5.7 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/)

초기화되어 있지 않은 변수 체크, 상대 경로 `.ts`를 출력할 때 `.js`으로 변경하는 `--rewriteRelativeImportExtensions` 플래그가 추가되었습니다.
또한, `--target es2024` 지원, Node.js 22의 V8 Compile Cache 지원해서 실행 속도 개선했습니다.

---

2024년 10월 TC39 미팅에서 5개 Proposal이 Stage 4가 되었습니다.

- [ECMAScript proposal updates @ 2024-10 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update)

[Promise.try](https://github.com/tc39/proposal-promise-try)/[Import Attributes](https://github.com/tc39/proposal-import-attributes)/[RegExp Modifiers](https://github.com/tc39/proposal-regexp-modifiers)/[Sync Iterator helpers](https://github.com/tc39/proposal-iterator-helpers)/[JSON Modules](https://github.com/tc39/proposal-json-modules)이 각각 Stage 4가 되었습니다.
이에, 앞으로 기능은 ES2025에 포함됩니다.

이 외로도 이미 Stage 4가 된 Proposal은 다음에서 확인 가능합니다.

- [proposals/finished-proposals.md at main · tc39/proposals](https://github.com/tc39/proposals/blob/main/finished-proposals.md)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Bun v1.1.30 | Bun Blog
[bun.sh/blog/bun-v1.1.30](https://bun.sh/blog/bun-v1.1.30 "Bun v1.1.30 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">css</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.30 출시.
CSS의 parse와 bundle 지원, `bun publish` 명령어 추가, `bun build --bytecode --compile` 성능 개선.
`--compile` 플래그 없는 `--bytecode` 플래그 지원, `bun build --format=cjs` 지원


----

## Announcing Deno 2
[deno.com/blog/v2.0](https://deno.com/blog/v2.0 "Announcing Deno 2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v2.0 출시.
글로벌한 `window` 삭제/`process` 추가, `deno add`으로 `jsr:`과 `npm:` 식별자 지정 추가, 권한 지정 관련 동작 변경, `deno bundle` 명령어 삭제

- [Deno 2.0 Release Candidate](https://deno.com/blog/v2.0-release-candidate "Deno 2.0 Release Candidate")
- [Deno 1.x to 2.x Migration Guide](https://docs.deno.com/runtime/reference/migration_guide/ "Deno 1.x to 2.x Migration Guide")

----

## Release eslint-plugin-react-hooks@5.0.0 (Oct 11, 2024) · facebook/react
[github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0](https://github.com/facebook/react/releases/tag/eslint-plugin-react-hooks%405.0.0 "Release eslint-plugin-react-hooks@5.0.0 (Oct 11, 2024) · facebook/react")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

eslint-plugin-react-hooks 5.0.0 출시.
ESLint v9 지원, 컴포넌트명은 다문자로 시작하는 규칙 추가, React 19 대응, `useEffect(fn, undefined)` 허용하도록 변경


----

## Release v1.48.0 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.48.0](https://github.com/microsoft/playwright/releases/tag/v1.48.0 "Release v1.48.0 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.48.0 출시.
`page.routeWebSocket()` API 추가, `page.requestGC()` 메서드 추가, `location` 옵션 추가


----

## Release Notes for Safari Technology Preview 205 | WebKit
[webkit.org/blog/15999/release-notes-for-safari-technology-preview-205/](https://webkit.org/blog/15999/release-notes-for-safari-technology-preview-205/ "Release Notes for Safari Technology Preview 205 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 205 출시.
`Math.sumPrecise`, `Iterator.prototype.reduce` 지원.
WebAssembly 예외 처리 지원


----

## Announcing TypeScript 5.7 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-7-beta/ "Announcing TypeScript 5.7 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.7 Beta 출시.
초기화되어 있지 않은 변수 체크, 상대 경로의 `.ts` 출력할 때에 `.js`으로 변경시키는 `--rewriteRelativeImportExtensions` 플래그 추가.
`--target es2024` 지원, Node.js 22의 V8 Compile Cache 지원해 실행 속도 개선


----

## Release v0.81.0 · facebook/metro
[github.com/facebook/metro/releases/tag/v0.81.0](https://github.com/facebook/metro/releases/tag/v0.81.0 "Release v0.81.0 · facebook/metro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">bundler</span></p>

metro 0.81.0 출시.
Node.js 18 미만 지원 종료, `#`으로 시작하는 경로는 장래에 subpath import 지원을 위해서 예약


----

## Release v2.3.0 · reduxjs/redux-toolkit
[github.com/reduxjs/redux-toolkit/releases/tag/v2.3.0](https://github.com/reduxjs/redux-toolkit/releases/tag/v2.3.0 "Release v2.3.0 · reduxjs/redux-toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux Toolkit v2.3.0 출시.
`upsertQueryEntries` 추가, `prepareHeaders` 옵션 개선


----

## ECMAScript proposal updates @ 2024-10 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/10/12/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-10 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2024년 10월 TC39 Meeting에서 ECMAScript Proposal Status 변경 모음.
`Promise.try`/Import attributes/RegExp Modifiers/Iterator helpers/JSON modules가 Stage 4가 되어 ES2025에 포함


----
<h1 class="site-genre">읽을거리</h1>

----

## The Popover API: Your New Best Friend for Tooltips
[www.voorhoede.nl/en/blog/the-popover-api-your-new-best-friend-for-tooltips/](https://www.voorhoede.nl/en/blog/the-popover-api-your-new-best-friend-for-tooltips/ "The Popover API: Your New Best Friend for Tooltips")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">PostCSS</span> <span class="jser-tag">article</span></p>

Popover API 사용해서 툴팁 보이기


----

## Deno v2 출시🎉 - Deno v1.0.0부터와 변화와 현황에 대하여
[zenn.dev/uki00a/articles/deno-v2-what-has-changed-from-v1](https://zenn.dev/uki00a/articles/deno-v2-what-has-changed-from-v1 "Deno v2 출시🎉 - Deno v1.0.0부터와 변화와 현황에 대하여")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">article</span></p>

Deno v1부터 v2까지 변화에 대하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## trynova/nova: JS engine lolz
[github.com/trynova/nova](https://github.com/trynova/nova "trynova/nova: JS engine lolz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span></p>

Rust로 작성한 JavaScript 엔진.
데이터 지향 디자인으로 구현


----
