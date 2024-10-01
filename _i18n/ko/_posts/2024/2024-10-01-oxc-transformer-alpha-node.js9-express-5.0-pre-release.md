---
title: "2024-10-01: Oxc Transformer Alpha, Node.js 9개의 기둥, Express 5.0 pre-release"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-10-01T01:40:30.220Z
category: JSer
tags:
- nodejs
- TypeScript
- Tools
- Rust
- React

---

JSer.info #709 - TypeScript의 Transpiler인 oxc-transform α판이 출시되었어요.

- [Oxc Transformer Alpha | The JavaScript Oxidation Compiler](https://oxc.rs/blog/2024-09-29-transformer-alpha.html)

Rust 작성된 TypeScript to JavaScript의 transpiler으로, isolatedDeclarations 대응한 자료형 정의 파일 생성에도 대응하고 있어요.

---

[The Nine Node Pillars](https://www.platformatichq.com/node-principles)은, Node.js 애플리케이션의 9가지 모범사례에 대해 작성된 문서에요.

이하 항목에 관련해, Node.js 애플리케이션 개발에 관련해 작성되어 있어요.

- 이벤트 루프를 블록하지 않는다
- 매트릭스 감시해서 행동한다
- Node.js LTS 사용한다
- 테스트, 리뷰 자동화
- 의존 관계 관리, monorepo
- 의존 관계 위험과 업데이트
- 글로벌을 피한다
- 에러 핸들링, 의미 있는 로그 출력
- API Spec과 클라이언트 자동 생성

---

express v5.0.0의 pre-release가 출시되었어요.

- [Release 5.0.0 · expressjs/express](https://github.com/expressjs/express/releases/tag/v5.0.0)
- [Migrating to Express 5](https://expressjs.com/en/guide/migrating-5.html)


[What's New in Express.js v5.0](https://www.trevorlasn.com/blog/whats-new-in-express-5)에는, 
Express 5.0(pre-release) 변경점에 대해 정리되어 있어요.
`app.del()`/`app.param(fn)`/`req.param(name)` 삭제, Path Route 매칭이 정규표현으로 Strict하도록 변경되었어요.
또한, Router의 Handler가 async await 지원, Node.js 18 미만 지원 종료 변경도 있어요.


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v1.9.0 - LGTM! · solidjs/solid
[github.com/solidjs/solid/releases/tag/v1.9.0](https://github.com/solidjs/solid/releases/tag/v1.9.0 "Release v1.9.0 - LGTM! · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Solid</span> <span class="jser-tag">ReleaseNote</span></p>

Solid v1.9.0 출시.
JSX 검증 개선, Custom Element 지원 개선, `handleEvent` 지원


----

## Release v2.0.0 · unjs/jiti
[github.com/unjs/jiti/releases/tag/v2.0.0](https://github.com/unjs/jiti/releases/tag/v2.0.0 "Release v2.0.0 · unjs/jiti")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

jiti v2.0.0 출시.
JSX 지원, CJS/ESM의 dual pacakge로 공개, `jiti/native` 추가, `jiti/register` 추가.


----

## OpenNext - OpenNext
[opennext.js.org/](https://opennext.js.org/ "OpenNext - OpenNext")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">aws</span> <span class="jser-tag">library</span></p>

Next.js를 Vercel 외에서 셀프호스팅하기 위해, 아키텍처 설계나 어댑터 구현.
AWS와 Cloudflare 대상 어댑터가 개발되어 있음


----

## End of life for Actions Node16 - GitHub Changelog
[github.blog/changelog/2024-09-25-end-of-life-for-actions-node16/](https://github.blog/changelog/2024-09-25-end-of-life-for-actions-node16/ "End of life for Actions Node16 - GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">news</span></p>

2024년 10월 15일에 GitHub Actions에서 Node.js 16 지원 종료.


----

## helmet/CHANGELOG.md at main · helmetjs/helmet
[github.com/helmetjs/helmet/blob/main/CHANGELOG.md#800](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#800 "helmet/CHANGELOG.md at main · helmetjs/helmet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">security</span> <span class="jser-tag">library</span></p>

helmet v8.0.0 출시.
Node.js 18 미만 지원 종료, 
`Strict-Transport-Security`의 max-age가 기본적으로 365으로 변경


----

## Oxc Transformer Alpha | The JavaScript Oxidation Compiler
[oxc.rs/blog/2024-09-29-transformer-alpha.html](https://oxc.rs/blog/2024-09-29-transformer-alpha.html "Oxc Transformer Alpha | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Rust</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript의 Transpiler oxc-transform α판 출시.


----

## The Nine Node Pillars
[www.platformatichq.com/node-principles](https://www.platformatichq.com/node-principles "The Nine Node Pillars")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">document</span></p>

Node.js 애플리케이션 9개의 모범 사례에 관한 문서.
- 이벤트 루프를 블록하지 않는다
- 매트릭스 감시해서 행동한다
- Node.js LTS 사용한다
- 테스트, 리뷰 자동화
- 의존 관계 관리, monorepo
- 의존 관계 위험과 업데이트
- 글로벌을 피한다
- 에러 핸들링, 의미 있는 로그 출력
- API Spec과 클라이언트 자동 생성


----

## Release @ark-ui/react@4.0.0 · chakra-ui/ark
[github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%404.0.0](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Freact%404.0.0 "Release @ark-ui/react@4.0.0 · chakra-ui/ark")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Ark UI v4.0.0 출시.
ColorPicker/Select/Combobox/DatePicker 값 전달 방법 변경

- [Release @ark-ui/solid@4.0.0 · chakra-ui/ark](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Fsolid%404.0.0 "Release @ark-ui/solid@4.0.0 · chakra-ui/ark")
- [Release @ark-ui/vue@4.0.0 · chakra-ui/ark](https://github.com/chakra-ui/ark/releases/tag/%40ark-ui%2Fvue%404.0.0 "Release @ark-ui/vue@4.0.0 · chakra-ui/ark")

----

## Release Notes for Safari Technology Preview 204 | WebKit
[webkit.org/blog/15978/release-notes-for-safari-technology-preview-204/](https://webkit.org/blog/15978/release-notes-for-safari-technology-preview-204/ "Release Notes for Safari Technology Preview 204 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 204 출시.
CSS `line-clamp` preview 지원, Cookie Store API 지원


----
<h1 class="site-genre">읽을거리</h1>

----

## What&#039;s New in Express.js v5.0
[www.trevorlasn.com/blog/whats-new-in-express-5](https://www.trevorlasn.com/blog/whats-new-in-express-5 "What&#039;s New in Express.js v5.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">express</span> <span class="jser-tag">article</span></p>

Express 5.0(pre-release) 변경점에 대하여.
`app.del()`/`app.param(fn)`/`req.param(name)` 삭제, Path Route 매칭이 정규표현으로 Strict스럽게 변경.
Router의 Handler가 async await 지원, Node.js 18 미만 지원 종료

- [Migrating to Express 5](https://expressjs.com/en/guide/migrating-5.html "Migrating to Express 5")

----

## Jotai의 atom를 자유롭게 테스트하고 싶을 때 보는 글
[zenn.dev/yuneco/articles/jotai-atom-testing](https://zenn.dev/yuneco/articles/jotai-atom-testing "Jotai의 atom를 자유롭게 테스트하고 싶을 때 보는 글")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">test</span> <span class="jser-tag">article</span></p>

Jotai 테스트 방법에 관하여


----

## Node.js 20 upgrade: a journey through unexpected HEAP issues with Kubernetes | by Ztec | Sep, 2024 | Deezer I/O
[deezer.io/node-js-20-upgrade-a-journey-through-unexpected-heap-issues-with-kubernetes-27ae3d325646](https://deezer.io/node-js-20-upgrade-a-journey-through-unexpected-heap-issues-with-kubernetes-27ae3d325646 "Node.js 20 upgrade: a journey through unexpected HEAP issues with Kubernetes | by Ztec | Sep, 2024 | Deezer I/O")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

Node.js 18에서 20으로 업데이트 하면 평균응답 시간과 CPU 사용률이 살짝 증가하는데, 이 원인 찾는 글.
Heap과 GC 매트릭스를 보면, GC가 빈번하게 동작, 출시 노트를 찾아보니 V8의 Heap 스페이스 기본값이 변경을 발견하기까지의 이야기


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mieszkosabo/tartak: Tartak is a functional programming language that compiles to TypeScript types.
[github.com/mieszkosabo/tartak](https://github.com/mieszkosabo/tartak "mieszkosabo/tartak: Tartak is a functional programming language that compiles to TypeScript types.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">language</span> <span class="jser-tag">Tools</span></p>

TypeScript 자료형과 컴파일 가능한 함수형 언어


----
<h1 class="site-genre">도서</h1>

----

## ［만들면서 배우기］브라우저 구조──HTTP, HTML, CSS, JavaScript의 뒷면 | 토이 아사미 | 책 | 통판 | Amazon
[www.amazon.co.jp/dp/4297145464/](https://www.amazon.co.jp/dp/4297145464/ "［만들면서 배우기］브라우저 구조──HTTP, HTML, CSS, JavaScript의 뒷면 | 토이 아사미 | 책 | 통판 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">book</span> <span class="jser-tag">Rust</span></p>

2024년 11월 9일 발매
Rust로 심플한 브라우저를 만들며 구조에 대해 배우는 책


----
