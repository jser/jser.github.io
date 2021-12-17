---
title: "2021-12-15: Tailwind CSS v3.0, create-react-app v5.0.0, CLS 개선"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-12-15T00:08:41.159Z
category: JSer
tags:
- node.js
- CSS
- safari
- Tools
- DOM

---

JSer.info #570 - Tailwind CSS v3.0가 릴리스 됐다.

- [Tailwind CSS v3.0 – Tailwind CSS](https://tailwindcss.com/blog/tailwindcss-v3)

클래스 명으로 지정한 템플릿을 토대로 스타일 클래스를 생성하는 Just-in-Time Mode 엔진이 개편됐다.
또, Box Shadow Color가 추가됐고 CSS Scroll Snap, Multi-column layout 등을 지원한다.
그 외로는 시험적으로 RTL과 LTR modifiers를 지원하며 따로 빌드 없이 브라우저에서 바로 사용할 수 있는 개발용 CDN(Paly CDN) 스크립트를 지원한다.


- [Installation: Play CDN - Tailwind CSS](https://tailwindcss.com/docs/installation/play-cdn)

----

Create React App 5.0가 릴리스 됐다.

- [Release v5.0.0 · facebook/create-react-app](https://github.com/facebook/create-react-app/releases/tag/v5.0.0)

webpack 5, Jest 27, ESLint 8, PostCSS 8로 각각 갱신됐다.
또, tailwind.config.js를 지원하고 의존 버전 고정을 삭제했으며 Node 10, 12가 지원 종료됐다.

----

BuzzFeed에서 CLS 개선을 주제로 정리한 연재 글을 공개했다.

- [Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd)
- [Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-2-2a846adeb097)
- [Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-3-3a36240861e4)

RUM과 Synthetic Moniting에서의 CLS 스코어 모니터링, RUM 로그로 부터 CLS를 발생 시키고 있는 요소 검출과 수정, 서드 파티에서 삽입하는 컨텐츠에 의한 CLS 문제를 개선하는 방법 등 폭넓게 다루고 있다.


----

<h1 class="site-genre">헤드라인</h1>

----

## Tailwind CSS v3.0 – Tailwind CSS
[tailwindcss.com/blog/tailwindcss-v3](https://tailwindcss.com/blog/tailwindcss-v3 "Tailwind CSS v3.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Tailwind CSS v3.0 릴리스.
Just-in-Time Mode 엔진 개편, Box Shadow Color 추가, CSS Scroll Snap 지원, Multi-column layout 지원 등.


----

## Release 13.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v13.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v13.0.0 "Release 13.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 13.0.0 릴리스.
`already-handled`의 typo를 수정.


----

## Release Notes for Safari Technology Preview 136 | WebKit
[webkit.org/blog/12137/release-notes-for-safari-technology-preview-136/](https://webkit.org/blog/12137/release-notes-for-safari-technology-preview-136/ "Release Notes for Safari Technology Preview 136 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">WebExtension</span></p>

Safari Technology Preview 136 릴리스.
`contain: paint`, `revert-layer`, `flex-basis: content` 지원.
`Temporal.Instant` 구현, WebExtension의 Manigest V3를 지원.


----

## GitHub Actions: GitHub-hosted runners now run Node.js 16 by default | GitHub Changelog
[github.blog/changelog/2021-12-10-github-actions-github-hosted-runners-now-run-node-js-16-by-default/](https://github.blog/changelog/2021-12-10-github-actions-github-hosted-runners-now-run-node-js-16-by-default/ "GitHub Actions: GitHub-hosted runners now run Node.js 16 by default | GitHub Changelog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

GitHub Actions의 Node.js 기본 버전이 Node.js 16으로 변경됐다.


----

## Release v5.0.0 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v5.0.0](https://github.com/facebook/create-react-app/releases/tag/v5.0.0 "Release v5.0.0 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app v5.0.0 릴리스.
webpack 5, Jest 27, ESLint 8, PostCSS 8로 각각 업데이트.
tailwind.config.js 지원, 의존 버전 고정 삭제, Node 10와 12 지원 종료 등.


----

## New WebKit Features in Safari 15.2 | WebKit
[webkit.org/blog/12140/new-webkit-features-in-safari-15-2/](https://webkit.org/blog/12140/new-webkit-features-in-safari-15-2/ "New WebKit Features in Safari 15.2 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">WebAssembly</span></p>

Safari 15.2의 변경 사항 정리 및 소개.
Wasm에서 이용 가능한 메모리가 4GB로 확장, COOP / COEP HTTP 헤더를 지원하고 crossOriginIsolated 시 SharedArrayBuffer / Wasm 스레드를 이용할 수 있도록 변경.
Canvas에서 `colorSpace: "display-p3"`를 지원 등.


----

## Release 5.0.0 – ESM support, CSS Selectors Level 4 · css/csso
[github.com/css/csso/releases/tag/v5.0.0](https://github.com/css/csso/releases/tag/v5.0.0 "Release 5.0.0 – ESM support, CSS Selectors Level 4 · css/csso")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

CSS minify 도구 CSSO 5.0.0 릴리스.
CSS Selectors Level 4 지원, 모듈 시스템을 ESM으로 변경했지만 ESM to CJS으로 dual module을 지원한다.


----
<h1 class="site-genre">아티클</h1>

----

## Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech
[tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-1-8b7ead2381dd "Improving CLS at BuzzFeed — Part 1 | BuzzFeed Tech")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

BuzzFeed의 Web Vitals 측정과 이를 이용한 개선을 주제로한 연재 글.
RUM과 Synthetic Moniting을 이용한 CLS 스코어 모니터링, RUM 로그에서 CLS를 발생시키고 있는 요소 검출과 수정, 서드 파티의 삽입 컨텐츠에 의한 CLS 문제 개선 등.

- [Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-2-2a846adeb097 "Improving CLS at BuzzFeed — Part 2 | BuzzFeed Tech")
- [Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech](https://tech.buzzfeed.com/improving-cumulative-layout-shift-at-buzzfeed-part-3-3a36240861e4 "Improving CLS at BuzzFeed — Part 3 | BuzzFeed Tech")

----

## New in Node.js: \`node:\` protocol imports
[2ality.com/2021/12/node-protocol-imports.html](https://2ality.com/2021/12/node-protocol-imports.html "New in Node.js: \`node:\` protocol imports")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

`node:` protocol을 이용한 Node.js의 빌트인 모듈 참조 방법 소개.
`node:` 는 Node.js 내장 모듈을 참조할 때 쓰는 새로운 방식.

 * Node.js의 내장 모듈을 참조하고 있음을 바로 알 수 있다.
 * 몇 개의 내장 모듈을 참조하고 있는지 판단할 때 유용한 정보.
 * `node_modules` 내의 모듈이 내장 모듈을 재정의 할 위험이 없다.
 * Node.js가 새로운 내장 모듈을 추가할 때 특히 중요(기존 npm 모듈과의 충돌 방지).


----

## Debug memory leaks with the Microsoft Edge Detached Elements tool - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/](https://blogs.windows.com/msedgedev/2021/12/09/debug-memory-leaks-detached-elements-tool-devtools/ "Debug memory leaks with the Microsoft Edge Detached Elements tool - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

MSEdge 개발자 도구의 Detached Elements 기능 소개.
DOM 트리에서 분리된 요소를 나열해서 살펴볼 수 있으며 이 정보로 DOM 메모리 릭을 디버깅할 수 있다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## capricorn86/happy-dom: A jsdom alternative with support for server side rendering of web components.
[github.com/capricorn86/happy-dom](https://github.com/capricorn86/happy-dom "capricorn86/happy-dom: A jsdom alternative with support for server side rendering of web components.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

JSDOM 처럼 Node.js에서 DOM API를 사용할 수 있도록 하는데 목적을 둔 라이브러리.
서버 사이드 렌더링 용 패키지도 함께 공개돼 있다.


----

## Akryum/peeky: Test framework for curious minds 🐈️ Powered by Vite ⚡️
[github.com/Akryum/peeky](https://github.com/Akryum/peeky "Akryum/peeky: Test framework for curious minds 🐈️ Powered by Vite ⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

Vite를 사용한 테스트 프레임워크.
테스트 개발 용 GUI를 제공한다.


----
