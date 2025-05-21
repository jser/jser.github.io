---
title: '2025-05-20: Zod 4, "use client", Fresh 2 Roadmap'
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-05-20T14:11:55.779Z
category: JSer
tags:
- React
- Design
- video
- GraphQL
- jsx

---

JSer.info #735 - Zod 4가 출시되었습니다.

또한, zod@4자체는 공개되지 않았지만, `zod@3.25.0`가 출시되어, `zod/v4`로 참조할 수 있습니다.

- [Introducing Zod 4 | Zod](https://zod.dev/v4)
- [Migration guide | Zod](https://zod.dev/v4/changelog)

Zod 4에서는, 자료형 체크 성능과 번들 크기 개선이 있습니다.
또한, 스킴에 메타데이터를 연결할 `z.registry()`나 `toJSONSchema()` 추가, i18n 지원 추가됩니다. 파괴적 변경으로, 톱레벨 문자열 형식이나 메일 주소 정규표현 변경이 있습니다.

----

React의 `"use client"` Directives 역할에 대한 해설 글입니다.

- [What Does "use client" Do? — overreacted](https://overreacted.io/what-does-use-client-do/)

이 글에서는 `"use client"`나 `"use server"`는, 코드가 클라이언트 측 혹은 서버 측에서 실행되는가 마크하는 것이 아니라, `"use client"`는 클라이언트 컴포넌트의 코드를 서버 컴포넌트에서 참조 가능하도록 하기 위함이라 설명합니다.

----

Deno 웹 프레임워크 Fresh 버전2 관련 로드맵을 공개했습니다.

- [An Update on Fresh | Deno](https://deno.com/blog/an-update-on-fresh)

Fresh 2는 2025년 9월 출시를 목표로 하고, 현재 알파판이 공개되어 있습니다.
이 글에서는, Fresh 2 변경 예정 사항에 대해 설명하고 있습니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v19.0.0 · facebook/relay
[github.com/facebook/relay/releases/tag/v19.0.0](https://github.com/facebook/relay/releases/tag/v19.0.0 "Release v19.0.0 · facebook/relay")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Relay v19.0.0 출시.
`@alias`가 conditional fragments에 필수이도록 변경, 문서 개선, React 19 대응.


----

## Version v8.0.0 | Mantine
[mantine.dev/changelog/8-0-0/](https://mantine.dev/changelog/8-0-0/ "Version v8.0.0 | Mantine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mantine v8.0.0 출시.
DatePicker가 `Date`가 아니라 `string`으로 다뤄지도록 변경, CodeHighlight에 shiki를 사용하도록 변경.
Menu 컴포넌트가 submenus 지원, TimePicker 컴포넌트 추가


----

## WebKit Features in Safari 18.5 | WebKit
[webkit.org/blog/16923/webkit-features-in-safari-18-5/](https://webkit.org/blog/16923/webkit-features-in-safari-18-5/ "WebKit Features in Safari 18.5 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 18.5 변경점.
Declarative Web Push를 macOS에도 지원.


----

## Node.js — Wednesday, May 14, 2025 Security Releases
[nodejs.org/en/blog/vulnerability/may-2025-security-releases](https://nodejs.org/en/blog/vulnerability/may-2025-security-releases "Node.js — Wednesday, May 14, 2025 Security Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 24.x, 23.x, 22.x, 20.x에 대한 보안 업데이트가 각기 공개되었습니다.


----

## Release pnpm 10.11 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.11.0](https://github.com/pnpm/pnpm/releases/tag/v10.11.0 "Release pnpm 10.11 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.11.0 출시.
`pnpm init`에 `init-type=module` 옵션 추가, `pnpm audit`에 `--ignore`와 `--ignore-unfixable` 플래그 추가


----

## Introducing Zod 4 | Zod
[zod.dev/v4](https://zod.dev/v4 "Introducing Zod 4 | Zod")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

zod 4 출시.
zod 3.25.0가 출시되어 `zod/v4`으로 참조 가능.
자료형 체크 성능과 bundle size 개선, zod mini 패키지 추가. 스킴에 엮을 메타데이터 관리 `z.regisry()` 추가, `toJSONSchema()` 추가, i18n 지원.
톱레벨 문자열 형식 변경, 메일 주소 정규표현 변경 가능, 템플릿 리터럴 자료형 지원

- [Migration guide | Zod](https://zod.dev/v4/changelog "Migration guide | Zod")

----

## May 19, 2025 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2025-05-19.html](https://react-spectrum.adobe.com/releases/2025-05-19.html "May 19, 2025 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria May 19, 2025 출시.
`useTreeData`에 `moveBefore`와 `moveAfter` 메서드 추가, `shouldSelectOnPressUp` props를 collection components에 추가.
React 19의 ref cleanup callback 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## Converting values to strings in JavaScript has pitfalls
[2ality.com/2025/04/stringification-javascript.html](https://2ality.com/2025/04/stringification-javascript.html "Converting values to strings in JavaScript has pitfalls")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript으로 값을 문자열로 변경하는 방법 비교


----

## An Update on Fresh | Deno
[deno.com/blog/an-update-on-fresh](https://deno.com/blog/an-update-on-fresh "An Update on Fresh | Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">article</span></p>

Fresh 2 마일드 스톤.
2025년 9월에 출시할 예정, alpha판 공개중


----

## ESLint can now lint HTML using the html-eslint language plugin - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2025/05/eslint-html-plugin/](https://eslint.org/blog/2025/05/eslint-html-plugin/ "ESLint can now lint HTML using the html-eslint language plugin - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">HTML</span> <span class="jser-tag">article</span></p>

ESLint로 HTML를 Lint하기 위한 `html-eslint`가 출시


----

## What Does &quot;use client&quot; Do? — overreacted
[overreacted.io/what-does-use-client-do/](https://overreacted.io/what-does-use-client-do/ "What Does \&quot;use client\&quot; Do? — overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

`"use client"`와 `"use server"`는 무엇인가.
클라이언트 측 / 서버 측 마크하는 수단이 아닌, `"use client"`는 클라이언트 함수를 서버에 export하는 것으로 인식


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Design Tokens Course with Brad Frost and Ian Frost
[designtokenscourse.com/](https://designtokenscourse.com/ "Design Tokens Course with Brad Frost and Ian Frost")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Design</span> <span class="jser-tag">video</span></p>

Design Token 강좌


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ije/mono-jsx: \`&lt;html&gt;\` as a \`Response\`.
[github.com/ije/mono-jsx](https://github.com/ije/mono-jsx "ije/mono-jsx: \`&lt;html&gt;\` as a \`Response\`.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">jsx</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

JSX Runtime 라이브러리.
서버사이드 템플릿으로 JSX 이용, 컴포넌트 State나 Streaming Rendering 지원


----

## aidenybai/bippy: ⚠️ hack into react internals
[github.com/aidenybai/bippy](https://github.com/aidenybai/bippy "aidenybai/bippy: ⚠️ hack into react internals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

React 내부 상태 사용한 React 애플리케이션을 디버그하는 도구 / 라이브러리.
React DevTools 대상 처리를 사용해 내부 상태 관찰


----

## webdiscus/ansis: CJS/ESM ANSI color library for CI, terminals and Chromium-based browser consoles. Compatible with Bun, Deno, Next.JS.
[github.com/webdiscus/ansis](https://github.com/webdiscus/ansis "webdiscus/ansis: CJS/ESM ANSI color library for CI, terminals and Chromium-based browser consoles. Compatible with Bun, Deno, Next.JS.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">color</span></p>

ANSI color 라이브러리


----

## macieklamberski/feedsmith: Robust and fast parser and generator for RSS, Atom, JSON Feed, and RDF feeds, with support for Podcast, iTunes, Dublin Core, and OPML files.
[github.com/macieklamberski/feedsmith](https://github.com/macieklamberski/feedsmith "macieklamberski/feedsmith: Robust and fast parser and generator for RSS, Atom, JSON Feed, and RDF feeds, with support for Podcast, iTunes, Dublin Core, and OPML files.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rss</span> <span class="jser-tag">library</span></p>

RSS와 OPML 파서 / 제네레이터 라이브러리


----
<h1 class="site-genre">도서</h1>

----

## 하이퍼 메타 시스템 | 기술평론사
[gihyo.jp/book/2025/978-4-297-14945-1](https://gihyo.jp/book/2025/978-4-297-14945-1 "하이퍼 메타 시스템 | 기술평론사")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2025년 6월 11일 발매
htmx 관련 도서.


----
