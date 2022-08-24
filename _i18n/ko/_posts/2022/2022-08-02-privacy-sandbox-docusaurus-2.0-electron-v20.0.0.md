---
title: "2022-08-02: Privacy Sandbox 로드맵 갱신, Docusaurus 2.0, Electron v20.0.0"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-08-02T00:23:15.529Z
category: JSer
tags:
- Tools
- CSS
- serverless
- TypeScript
- Vue

---

JSer.info #603 - Google Chrome의 서드 파티 쿠키를 폐지하고 이를 대체할 API로서 Privacy Sandbox라는 API가 제안돼 있다.
원래는 2023년 중반부터 서드 파티 쿠키 폐지를 단계적으로 진행할 예정이었으나 이번 이와 관련한 로드맵이 갱신 됐다.

- [Expanding testing for the Privacy Sandbox for the Web](https://blog.google/products/chrome/update-testing-privacy-sandbox-web/)

Privacy Sandbox API 릴리스는 2023년 Q3까지 연기되고, 서드 파티 쿠키의 단계적 폐지는 2024년 후반까지 연기된다.
새로운 로드맵에 대한 자세한 내용은 아래 문서를 참고한다.

- [How We’re Protecting Your Online Privacy - The Privacy Sandbox](https://privacysandbox.com/intl/en_us/open-web/)

---

정적 사이트 제너레이터 Docusaurus v2가 릴리스 됐다.

- [Announcing Docusaurus 2.0 | Docusaurus](https://docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0)

MDX 지원, 사이드바 자동 생성, 플러그인 시스템 개편, 테마 재구축 등의 변경이 이뤄졌다.

Docusaurus 1에서 2가 릴리스 되기 까지 4년 정도 지났으나, 이제부터는 메이저 업데이트를 몇 달 단위로 더 자주 시행해 나갈 방침으로 보인다.

---

Electron v20.0.0 릴리스.

- [Release electron v20.0.0 · electron/electron](https://github.com/electron/electron/releases/tag/v20.0.0)

Chromium 104, [Node v16.15.0](https://nodejs.org/en/blog/release/v16.15.0/), V8 v10.4으로 의존 버전이 각각 업데이트 됐다.
또, `nodeIntegration: true`와 `sandbox: false`를 조합해 설정하지 않는 한 Renderers가 기본적으로 Sandbox화 되도록 변경 됐다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v9.0.0 · vueuse/vueuse
[github.com/vueuse/vueuse/releases/tag/v9.0.0](https://github.com/vueuse/vueuse/releases/tag/v9.0.0 "Release v9.0.0 · vueuse/vueuse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

vueuse v9.0.0 릴리스.
`isSupported`를 `Ref<boolean>`로 변경, 타입 명을 `Use` prefix로 통일.
많은 Use 함수의 인수에 함수를 전달할 수 있도록 변경, `@vueuse/math` 패키지 추가 등.


----

## Node v18.7.0 (Current) | Node.js
[nodejs.org/en/blog/release/v18.7.0/](https://nodejs.org/en/blog/release/v18.7.0/ "Node v18.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">serverless</span></p>

Node.js 18.7.0 릴리스.
`process.exit(code)`의 `code`에  정수 이외의 값 전달을 비권장화, `CustomEvent` 구현, http server에 `dropRequest` 이벤트 구현.

----

## Release v1.2.0 · video-dev/hls.js
[github.com/video-dev/hls.js/releases/tag/v1.2.0](https://github.com/video-dev/hls.js/releases/tag/v1.2.0 "Release v1.2.0 · video-dev/hls.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HLS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hls.js v1.2.0 릴리스.
IE 11 지원 종료, CMAF CC 지원, 버그 수정 및 안정성이 향상됐다.


----

## Expanding testing for the Privacy Sandbox for the Web
[blog.google/products/chrome/update-testing-privacy-sandbox-web/](https://blog.google/products/chrome/update-testing-privacy-sandbox-web/ "Expanding testing for the Privacy Sandbox for the Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">news</span></p>

갱신된 Privacy Sandbox의 로드맵 소개.
Privacy Sandbox API 릴리스는 2023년 Q3까지로 연기 됐고, 서드 파키 쿠키의 단계적 폐지는 2024년 말까지 연기 됐다.


----

## losfair/blueboat: All-in-one, multi-tenant serverless JavaScript runtime.
[github.com/losfair/blueboat](https://github.com/losfair/blueboat "losfair/blueboat: All-in-one, multi-tenant serverless JavaScript runtime.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">serverless</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">Tools</span></p>

Cloudflare Workers와 같이 V8 Isolates에서 멀티 테넌트를 실행할 수 있는 자바스크립트 실행 환경.
엔진은 Rust로 작성 돼 있으며 실행할 자바스크립트 스크립트에서 Fetch API나 Request / Response 와 같은 웹 표준 호환 API를 일부 사용할 수 있다.


----

## Announcing Docusaurus 2.0 | Docusaurus
[docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0](https://docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0 "Announcing Docusaurus 2.0 | Docusaurus")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">ReleaseNote</span></p>

정적 사이트 제너레이터 Docusaurus v2 릴리스.
MDX 지원, 사이드 바 자동 생성, 플러그인 시스템 개편, 테마 재구축 등.


----

## Release electron v20.0.0 · electron/electron
[github.com/electron/electron/releases/tag/v20.0.0](https://github.com/electron/electron/releases/tag/v20.0.0 "Release electron v20.0.0 · electron/electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron v20.0.0 릴리스.
`nodeIntegration: true`와 `sandbox: false`을 조합해 설정하지 않는 한 Renderers가 기본적으로 Sandbox화 되도록 변경 됐다.

----
<h1 class="site-genre">아티클</h1>

----

## 새로운 뷰포트 단위(sv*、lv*、dv*) | 프런트엔드 Blog | 미츠에링크스(일본어)
[www.mitsue.co.jp/knowledge/blog/frontend/202207/28\_0755.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202207/28_0755.html "새로운 뷰포트 단위(sv*、lv*、dv*) | 프런트엔드 Blog | 미츠에링크스")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS의 새로운 뷰포트 단위를 소개하는 글.


----

    ## Help pick a syntax for CSS nesting - Chrome Developers
[developer.chrome.com/blog/help-css-nesting/](https://developer.chrome.com/blog/help-css-nesting/ "Help pick a syntax for CSS nesting - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">アンケート</span></p>

CSS의 들여쓰기 구문에 대한 설문 조사
SCSS / Less / Stylus 처럼 들여쓰기 하는 케이스, `@nest`를 사용하는 케이스, 브라켓을 사용하는 케이스 등 들여쓰기 구문 디자인과 관련한 의견을 모으고 있다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 🌕 moon의 monorepo 관리 방식과 packemon의 CJS / ESM dual package에 대해(일본어)
[azu.github.io/slide/2022/moa/moon-packemon.html](https://azu.github.io/slide/2022/moa/moon-packemon.html "🌕 moon의 monorepo 관리 방식과 packemon의 CJS / ESM dual package에 대해")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">slide</span> <span class="jser-tag">JavaScript</span></p>

monorepo 관리 도구 moon과 CJS / MJS 대응 라이브러리 빌드 시스템 packemon을 소개하는 슬라이드 자료.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ronami/HypeScript: 🐬 A simplified implementation of TypeScript&#039;s type system written in TypeScript&#039;s own type system
[github.com/ronami/HypeScript](https://github.com/ronami/HypeScript "ronami/HypeScript: 🐬 A simplified implementation of TypeScript&#039;s type system written in TypeScript&#039;s own type system")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TypeScript의 타입 시스템을 TypeScript의 타입 애너테이션만으로 개발한 구현체


----

## ehmicky/safe-json-value: ⛑️ JSON serialization should never fail
[github.com/ehmicky/safe-json-value](https://github.com/ehmicky/safe-json-value "ehmicky/safe-json-value: ⛑️ JSON serialization should never fail")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">JSON</span></p>

에러를 던지지 않는 JSON 직렬화 기능을 제공하는 라이브러리.
직렬화를 할 수 없을 때 예외를 던지는 대신 `error` 속성에 에러를 할당하고 예외가 되는 값을 제외하는 방식으로 구현돼 있다.


----

## Skeleton
[skeleton.brainandbonesllc.com/](https://skeleton.brainandbonesllc.com/ "Skeleton")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

Svelte와 Tailwind 기반의 UI 컴포넌트 라이브러리


----
<h1 class="site-genre">도서</h1>

----

## TypeScript와 React / Next.js로 만드는 실천 웹 애플리케이션 개발: 서적 안내|기술평론사(일본어)
[gihyo.jp/book/2022/978-4-297-12916-3](https://gihyo.jp/book/2022/978-4-297-12916-3 "TypeScript와 React / Next.js로 만드는 실천 웹 애플리케이션 개발: 서적 안내|기술평론사")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2022년 7월 22일에 출간된 Next.js 입문서.


----

