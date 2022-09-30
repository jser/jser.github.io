---
title: "2022-09-29: TypeScript 4.9 Beta, workerd(Cloudflare Workers runtime), Web Almanac 2022"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-09-29T03:01:10.645Z
category: JSer
tags:
- node.js
- TypeScript
- security
- book
- browser

---

JSer.info #611 - TypeScript 4.9 beta가 릴리스 됐다.

- [Announcing TypeScript 4.9 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/)

타입 변환 없이 타입 일치 여부 체크할 수 있는 `satisfies` 연산자 추가, `in` 연산자 구문 내 타입 추론 영역 축소, `== NaN`을 컴파일 에러로 변경하는 등이 갱신이 이뤄졌다.

`satisfies` 연산자는 아래 글에서 자세히 설명하고 있으니 참고한다.

- [Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium](https://medium.com/@cefn/typescript-satisfies-6ba52e74cb2f)

또, `--watch`에서의 파일 감시 시스템 기본값을 `useFsEvents`(파일 시스템 이벤트)로 변경, `exports` 파일의 `typeVersions` 우선도를 조정했다.

----

Cloudflare Workers의 runtime인 workerd가 오픈소스로 공개됐다.

- [Introducing workerd: the Open Source Workers runtime](https://blog.cloudflare.com/workerd-open-source-workers-runtime/)
- [cloudflare/workerd](https://github.com/cloudflare/workerd)

이와 함게 Miniflare 3.0.0가 알파 릴리스 됐으며 자바스크립트로 구현됐던 부분도 workerd를 다루는 방식으로 변경됐다.

- [Release v3.0.0-next.1 · cloudflare/miniflare](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0-next.1)

이에 따라 로컬 개발 시와 실제 동작이 달랐던 경우가 크게 줄어들 것으로 기대된다.

----

HTTP Archive 데이터를 기반으로 웹 현황을 정리한 보고서 Web Almanac의 2022년 버전이 공개됐다.

- [The 2022 Web Almanac](https://almanac.httparchive.org/en/2022/)

HTML / CSS / JS 뿐 아니라 접근성 / 보안 / 서드파티 등 폭넓은 데이터를 다루고 있는 보고서다.

2021년 버전은 일본어로도 번역돼 있으니 관심있는 분은 함께 읽어보면 좋을 것 같다.

- [2021 Web Almanac](https://almanac.httparchive.org/ja/2021/)
- <https://cdn.httparchive.org/almanac/ebooks/web_almanac_2021_ja.pdf>

----
ㄴ
<h1 class="site-genre">헤드라인</h1>

----

## September 22nd 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/september-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/september-2022-security-releases/ "September 22nd 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Node.js의 보안 수정 버전 v14.20.1 (LTS), v16.17.1 (LTS), v18.9.1 (Current)가 각각 릴리스 됐다.
`--inspect`에 의한 DNS rebinding, HTTP Request Smuggling, WebCrypto의 Weak randomness 문제가 수정됐다.


----

## Announcing TypeScript 4.9 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-9-beta/ "Announcing TypeScript 4.9 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.9 beta가 릴리스 됐다.

* 타입 캐스트 없이 타입의 일치 여부를 체크할 수 있는 `satisfies` 연산자 추가
* `in` 연산자 구문 내 타입 추론 영역 축소
* `== NaN`을 컴파일 에러로 변경
* `--watch` 시의 파일 감시 방식의 기본 값을 `useFsEvents`(파일 시스템 이벤트)으로 변경
* `exports` 필드의 `typeVersions` 우선도 수정

- [Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium](https://medium.com/@cefn/typescript-satisfies-6ba52e74cb2f "Typescript’s new ‘satisfies’ operator | by Cefn Hoile | Aug, 2022 | Medium")

----

## Introducing workerd: the Open Source Workers runtime
[blog.cloudflare.com/workerd-open-source-workers-runtime/](https://blog.cloudflare.com/workerd-open-source-workers-runtime/ "Introducing workerd: the Open Source Workers runtime")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">C++</span></p>

Cloudflare Workers의 JavaScript / WebAssembly runtime 인 workerd가 공개 됐다.
Miniflare에서 자바스크립트로 구현 돼 있던 부분을 workerd를 다루는 방식으로 변경한 버전도 공개 됐다.
workerd 자체는 Sandbox가 아니지만 SSRF 방지를 위한 Binding과 Fetch 구조 등을 제공한다.

- [Release v3.0.0-next.1 · cloudflare/miniflare](https://github.com/cloudflare/miniflare/releases/tag/v3.0.0-next.1 "Release v3.0.0-next.1 · cloudflare/miniflare")
- [cloudflare/workerd](https://github.com/cloudflare/workerd "cloudflare/workerd")

----

## Release Add support for engines.node and Volta · actions/setup-node
[github.com/actions/setup-node/releases/tag/v3.5.0](https://github.com/actions/setup-node/releases/tag/v3.5.0 "Release Add support for engines.node and Volta · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Github</span></p>

GitHub Actions의 setup-node 3.5.0 릴리스.
`package.json`의 `engines.node`와 Volta에서 지정한 Node.js 버전을 인식한다.


----

## Release Notes for Safari Technology Preview 154 | WebKit
[webkit.org/blog/13207/release-notes-for-safari-technology-preview-154/](https://webkit.org/blog/13207/release-notes-for-safari-technology-preview-154/ "Release Notes for Safari Technology Preview 154 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">serverless</span></p>

Safari Technology Preview 154 릴리스.
CSS의 `:dir` 활성화, `InputEvent.isComposing` 지원, Scroll To Text Fragment 활성화 등.


----

## Release v0.5.0 · facebook/lexical
[github.com/facebook/lexical/releases/tag/v0.5.0](https://github.com/facebook/lexical/releases/tag/v0.5.0 "Release v0.5.0 · facebook/lexical")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

lexical v0.5.0 릴리스.
Notion과 같은 Draggable Blocks 지원, LexicalTablePlugin 안정환, Shadow Root에 대응.
일부 API는 비호환 변경 사항도 포함돼 있으니 확인한다.


----
<h1 class="site-genre">아티클</h1>

----

## Next.js Layouts RFC in 5 minutes – Vercel
[vercel.com/blog/next-js-layouts-rfc-in-5-minutes](https://vercel.com/blog/next-js-layouts-rfc-in-5-minutes "Next.js Layouts RFC in 5 minutes – Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Next.js의 Layouts RFC를 설명(소개)하는 글.


----

## The Anatomy of an Isolate Cloud
[deno.com/blog/anatomy-isolate-cloud](https://deno.com/blog/anatomy-isolate-cloud "The Anatomy of an Isolate Cloud")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">V8</span> <span class="jser-tag">article</span></p>

Deno Deploy의 Isolation 접근법 소개.
V8 프로세스가 독립적으로 동작, Runner가 요청에 대해 부팅 중인 프로세스(혹은 프로세스)를 기동한다.
기본적으로는 V8 Sandbox를 의존하고 있으며 fs나 net 접근에 제한을 둔다.


----

## Introducing Ezno
[kaleidawave.github.io/posts/introducing-ezno/](https://kaleidawave.github.io/posts/introducing-ezno/ "Introducing Ezno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Rust로 구현하고 있는 TypeScript 호환 타입 체커와 컴파일러 Ezno를 소개하는 글.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Zod Tutorial | Total TypeScript
[www.totaltypescript.com/tutorials/zod](https://www.totaltypescript.com/tutorials/zod "Zod Tutorial | Total TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">video</span></p>

TypeScript 기반의 스키마 검증 라이브러리 zod를 소개하는 튜토리얼 동영상.
각각의 연습 문제를 직접 풀어보면서 진행할 수 있도록 준비 돼 있다.


----

## SPA 보안 초입문 | 독스웰(일본어)
[www.docswell.com/s/ockeghem/K2PPNK-phpconf2022](https://www.docswell.com/s/ockeghem/K2PPNK-phpconf2022 "SPA 보안 초입문 | 독스웰")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">XSS</span> <span class="jser-tag">SQL</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

SPA에서 잘 발생하는 보안 문제를 정리한 슬라이드 자료.
클라이언트 사이드에서만 검증하는 인가 제어 미비, 임의의 HTML의 렌더링을 허용하여 발생하는 XSS, CSRF 등에 대해서 이야기한다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## gioboa/vite-module-federation: Module Federation with Vite now is possible
[github.com/gioboa/vite-module-federation](https://github.com/gioboa/vite-module-federation "gioboa/vite-module-federation: Module Federation with Vite now is possible")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">plugin</span></p>

Module Federation을 하는 Vite Plugin.


----

## Japa - A simple yet powerful testing framework for Node.js
[japa.dev/docs](https://japa.dev/docs "Japa - A simple yet powerful testing framework for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Node.js 용 테스트 프레임워크.
`node` 명령어로 테스트를 실행할 수 있다.
기본적인 테스트 기능에 더해 파라메터라이즈 테스트와 테스트에 대한 태그를 지정하고 필터링 할 수 있는 기능 제공.
또, 플러그인 구조를 지원하며 실패한 테스트 만 재실행 하거나 타입스크립트의 타입 검사 등을 할 수 있는 플러그인을 지원한다


----
<h1 class="site-genre">도서</h1>

----

## The 2022 Web Almanac
[almanac.httparchive.org/en/2022/](https://almanac.httparchive.org/en/2022/ "The 2022 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">book</span> <span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">HTML</span></p>

Web Almanac의 2022년 버전이 공개됐다.
HTTP Archive의 데이터를 기반으로 웹 현황(status)을 정리한 보고서.
HTML / CSS / JS를 시작으로 접근성 / 보안 / 서드 파티 등 폭넓은 데이터를 보여준다.


----

## Shell scripting with Node.js
[exploringjs.com/nodejs-shell-scripting/](https://exploringjs.com/nodejs-shell-scripting/ "Shell scripting with Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">book</span> <span class="jser-tag">ShellScript</span></p>

Node.js에서 shell scripting을 다루는 방법을 기술한 도서


----

