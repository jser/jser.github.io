---
title: "2023-01-06: Vue 2의 EOL은 2023년말, NextAuth는 Auth.js에, React Native에 First-class Support for TypeScript"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2023-01-06T03:37:03.041Z
category: JSer
tags:
- node.js
- React
- Tools
- browser
- book

---

JSer.info #625 - [2022 Year In Review | The Vue Point](https://blog.vuejs.org/posts/2022-year-in-review.html)에서는, Vue 2의 End of Life (EOL)에 대해 다시 한 번 공지되었다.

- [Vue.js - Vue 2 LTS, EOL & Extended Support](https://v2.vuejs.org/lts/)

Vue.js 2는 2023년 12월 31일에 EOL이 되며, 지원이 종료된다.
지원 종료 후에는 보안 업데이트도 행해지지 않을 예정이다.

---

[NextAuth.js](https://next-auth.js.org/)가 [Auth.js](https://authjs.dev/) 일부로 다뤄지는 변경했다.
이에, SvelteKit이나 SolidStart에서도 NextAuth이 구현된 인증, 인가를 이용할 수 있다.

---

React Native가 TypeScript를 First-class로 지원하도록 발표되었다.

- [First-class Support for TypeScript · React Native](https://reactnative.dev/blog/2023/01/03/typescript-first)

자료형 정의 파일 동봉이나 템플릿도 TypeScript가 기본값이 된다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Prototype Pollution in JSON5 via Parse Method · CVE-2022-46175 · GitHub Advisory Database
[github.com/advisories/GHSA-9c47-m6qq-7p4h](https://github.com/advisories/GHSA-9c47-m6qq-7p4h "Prototype Pollution in JSON5 via Parse Method · CVE-2022-46175 · GitHub Advisory Database")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSON</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

JSON5에 prototype pollution 취약성이 있어, 2.2.2와 1.0.2에서 수정되었다.

- [Release v2.2.2 · json5/json5](https://github.com/json5/json5/releases/tag/v2.2.2 "Release v2.2.2 · json5/json5")
- [Release v1.0.2 · json5/json5](https://github.com/json5/json5/releases/tag/v1.0.2 "Release v1.0.2 · json5/json5")

----

## Tamagui 1.0 🎉 — Tamagui
[tamagui.dev/blog/version-one](https://tamagui.dev/blog/version-one "Tamagui 1.0 🎉 — Tamagui")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React 대상 UI프레임워크인 Tamagui 1.0 출시.
React Native와 Web 어느쪽에서도 사용가능하며, 스타일링 라이브러리도 포함. 1.0에서는 Native와 Web 호환성 향상과 번들사이즈 개선 등을 했다.


----

## Vue.js
[v2.vuejs.org/lts/](https://v2.vuejs.org/lts/ "Vue.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">document</span></p>

Vue 2의 지원 종료는 2023년 12월 31일.
지원 종료 후는 보안 업데이트를 제공하지않으며, 확장 LTS는 AngularJS 처럼 외부 기업에 의뢰하는 형태가 될 예정

- [2022 Year In Review | The Vue Point](https://blog.vuejs.org/posts/2022-year-in-review.html "2022 Year In Review | The Vue Point")

----

## Release v0.16.13 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.16.13](https://github.com/evanw/esbuild/releases/tag/v0.16.13 "Release v0.16.13 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

esbuild v0.16.13 출시.
`--metafile`로 bundle 할 때 메타데이터 추출, 메타데이터 가시화 가능한 뷰사이트 구현 등


----

## First-class Support for TypeScript · React Native
[reactnative.dev/blog/2023/01/03/typescript-first](https://reactnative.dev/blog/2023/01/03/typescript-first "First-class Support for TypeScript · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Native</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.71에서 TypeScript 자료형 정의가 동봉되어, 새로운 템플릿도 기본값으로 TypeScript 이용할 수 있다.


----

## Node v18.13.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v18.13.0/](https://nodejs.org/en/blog/release/v18.13.0/ "Node v18.13.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.13.0 출시.
`File` API 구현, `node:test` 모듈에 `mock` API 추가, v8 snapshot compression를 무효화해서 기동속도 향상 등


----

## Release v6.4.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v6.4.0](https://github.com/lerna/lerna/releases/tag/v6.4.0 "Release v6.4.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span></p>

lerna v6.4.0 출시.
`lerna watch` 명령어 추가 등

----

## Auth.js
[authjs.dev/](https://authjs.dev/ "Auth.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAuthentication</span> <span class="jser-tag">OAuth</span> <span class="jser-tag">library</span></p>

NextAuth는 Auth.js가 되어, Next.js 외에도 SvelteKit나 SolidStart 등을 지원한다.


----

## Gluon
[gluonjs.org/](https://gluonjs.org/ "Gluon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">node.js</span> <span class="jser-tag">deno</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Chrome과 Firefox를 WebView 대신에 데스트탑 애플리케이션을 만드는 프레임워크.
데스크탑브라우저의 기동 옵션에서 단독 애플리케이션처럼 기동할 수 있다.
백엔드로는 Node.js와 Deno가 이용가능하며, 애플리케이션과 연계할 수 있는 API가 준비되어있다.


----
<h1 class="site-genre">읽을거리</h1>

----

## 슬슬 캐스케이드 레이어(@layer)를 마주하자
[zenn.dev/yend724/articles/20221227-fcz1jh70bhnqof2v](https://zenn.dev/yend724/articles/20221227-fcz1jh70bhnqof2v "슬슬 캐스케이드 레이어(@layer)를 마주하자")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS의 @layer에 대한 글


----

## Interop 2022: end of year update
[web.dev/interop-2022-wrapup/](https://web.dev/interop-2022-wrapup/ "Interop 2022: end of year update")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

웹브라우저 상호운용성 대처 상황를 알아보는 Interop 2022 결과 정리


----

## Miško Hevery의 Qwik 시리즈 | POSTD
[postd.cc/series-qwik/](https://postd.cc/series-qwik/ "Miško Hevery의 Qwik 시리즈 | POSTD")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Qwik 시리즈 번역 글


----
<h1 class="site-genre">도서</h1>

----

## 실전 Node.js 입문 | 이토 코우타 | 도서 | 통신판매 | Amazon
[www.amazon.co.jp/dp/4297129566/](https://www.amazon.co.jp/dp/4297129566/ "실전 Node.js 입문 | 이토 코우타 | 도서 | 통신판매 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">book</span></p>

2023년 1월 26일 발매.
Node.js의 CLI이나 애플리케이션 개발에 대한 도서


----
