---
title: "2024-10-08: WebPlatform 출시노트, Node v20.18.0(network의 inspect), StyleX 0.8.0"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-10-08T11:13:58.188Z
category: JSer
tags:
- webservice
- nodejs
- React
- WebPlatformAPI
- npm

---

JSer.info #710 - [Web features explorer - Web platform release notes](https://web-platform-dx.github.io/web-features-explorer/release-notes/)는, [web-features](https://github.com/web-platform-dx/web-features/)나 [@mdn/browser-compat-data](https://github.com/mdn/browser-compat-data/) 데이터를 기반으로, 매월 브라우저의 신기능을 정리해 출시 노트를 자동적으로 정리합니다.

[web-features](https://github.com/web-platform-dx/web-features/)는 [Baseline](https://github.com/web-platform-dx/web-features/blob/main/docs/baseline.md)라 하는 최대공약수 베이스라인이 되는 브라우저로 지원되는 지표가 되는 데이터를 생성합니다.

어떤 기능을 이용하고 있는가 알 수 있으므로, 새로운 기능을 알고 싶은 사람은 체크해두는 것도 좋을 것 입니다.

---

Node.js 20.18.0가 출시되었습니다.

- [Node.js — Node v20.18.0 (LTS)](https://nodejs.org/en/blog/release/v20.18.0)

`--experimental-network-inspection`으로 개발자 도구에서 Network Inspection 지원합니다.
`vm` 내에 `globalThis`를 freeze하는 `vm.constants.DONT_CONTEXTIFY` 추가되었습니다.

---

CSS in JS 라이브러리 StyleX 0.8.0가 출시되었습니다.

- [Release 0.8.0 | StyleX](https://stylexjs.com/blog/v0.8.0)

Lint로 shorthand 금지하는 `valid-shorthands` 규칙 추가, `enforce-extension` 규칙 추가가 있었습니다.
또한, lightningcss를 사용해 minify나 autoprefix의 post-process를 처리합니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Web features explorer - Web platform release notes
[web-platform-dx.github.io/web-features-explorer/release-notes/](https://web-platform-dx.github.io/web-features-explorer/release-notes/ "Web features explorer - Web platform release notes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">news</span> <span class="jser-tag">webservice</span></p>

web-features이나 browser-compat-data를 기반으로 브라우저 새로운 기능 출시 노트 형식을 정리한 웹사이트


----

## Release v10.9.0 · npm/cli
[github.com/npm/cli/releases/tag/v10.9.0](https://github.com/npm/cli/releases/tag/v10.9.0 "Release v10.9.0 · npm/cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm v10.9.0 출시.
개발 시 런타임 정보를 정의하는 `devEngines` 필드 지원


----

## Node.js — Node v20.18.0 (LTS)
[nodejs.org/en/blog/release/v20.18.0](https://nodejs.org/en/blog/release/v20.18.0 "Node.js — Node v20.18.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.18.0 출시.
`--experimental-network-inspection` 플래그로 Network Inspection 지원.
`vm` 내에 `globalThis`를 freeze하는 `vm.constants.DONT_CONTEXTIFY` 추가


----

## Tauri 2.0 Stable Release | Tauri
[v2.tauri.app/blog/tauri-20/](https://v2.tauri.app/blog/tauri-20/ "Tauri 2.0 Stable Release | Tauri")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">GUI</span> <span class="jser-tag">ReleaseNote</span></p>

Tauri 2.0 출시.
iOS/Android 지원, 모바일 애플리케이션 시뮬레이터도 HMR가 가능, 플러그인 시스템 업데이트, 접근 제어 구조 업데이트


----

## September 30, 2024 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2024-09-30.html](https://react-spectrum.adobe.com/releases/2024-09-30.html "September 30, 2024 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Aria September 30, 2024 출시.
ColorPicker/ColorArea/ColorField/ColorSlider/ColorSwatch/ColorSwatchPicker/ColorWheel 추가.
Button에 Pending의 state 추가.
실험적 컴포넌트로, `Tree`/`TreeView`와 `Disclosure`/`DisclosureGroup` 추가


----

## Release 20.0.0 · nrwl/nx
[github.com/nrwl/nx/releases/tag/20.0.0](https://github.com/nrwl/nx/releases/tag/20.0.0 "Release 20.0.0 · nrwl/nx")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Nx 20.0.0 출시.
rspack 플러그인 추가


----

## Release 0.8.0 | StyleX
[stylexjs.com/blog/v0.8.0](https://stylexjs.com/blog/v0.8.0 "Release 0.8.0 | StyleX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">css </span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

StyleX 0.8.0 출시.
shorthand 금지하는 `valid-shorthands` 규칙 추가, `enforce-extension` 규칙 추가.
lightningcss 사용해 minify나 autoprefix의 post-process 실행


----
<h1 class="site-genre">읽을거리</h1>

----

## ESLint now officially supports linting of JSON and Markdown - ESLint - Pluggable JavaScript Linter
[eslint.org/blog/2024/10/eslint-json-markdown-support/](https://eslint.org/blog/2024/10/eslint-json-markdown-support/ "ESLint now officially supports linting of JSON and Markdown - ESLint - Pluggable JavaScript Linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">JSON</span> <span class="jser-tag">Markdown</span> <span class="jser-tag">article</span></p>

ESLint의 JSON와 Markdown 지원에 대하여


----

## How Bun supports V8 APIs without using V8 (part 1) | Bun Blog
[bun.sh/blog/how-bun-supports-v8-apis-without-using-v8-part-1](https://bun.sh/blog/how-bun-supports-v8-apis-without-using-v8-part-1 "How Bun supports V8 APIs without using V8 (part 1) | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">V8</span> <span class="jser-tag">webkit</span> <span class="jser-tag">C++</span> <span class="jser-tag">article</span></p>

Bun가 어떤 식으로 V8 API를 JSC 상에 구현하는가.
C++ 포인터, 레이아웃 호환성 레이어, V8와 JSC 값 표현 차이, NaN 박싱, GC, 메모리 레이아웃 관련하여


----

## Web Components are not Framework Components — and That’s Okay • Lea Verou
[lea.verou.me/blog/2024/wcs-vs-frameworks/](https://lea.verou.me/blog/2024/wcs-vs-frameworks/ "Web Components are not Framework Components — and That’s Okay • Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">article</span> <span class="jser-tag">opinion</span></p>

Web Components은 HTML 확장과 리액티브 템플릿이라는 2가지 카테고리를 사용


----

## webpack to Rspack ~ Rspack 이행 결과와 주의점 ~
[zenn.dev/ryo\_kawamata/articles/b2df9989fe2c6e](https://zenn.dev/ryo_kawamata/articles/b2df9989fe2c6e "webpack to Rspack ~ Rspack 이행 결과와 주의점 ~")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

webpack에서 Rspack으로 이행하기.
production 빌드 문제 대응


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## ViteConf 2024 - YouTube
[www.youtube.com/playlist?list&#x3D;PLqGQbXn\_GDmnObDzgjUF4Krsfl6OUKxtp](https://www.youtube.com/playlist?list=PLqGQbXn_GDmnObDzgjUF4Krsfl6OUKxtp "ViteConf 2024 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

ViteConf 2024 영상 목록


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## CrUX Vis
[cruxvis.withgoogle.com/](https://cruxvis.withgoogle.com/ "CrUX Vis")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span></p>

CrUX 데이터를 사용해 지정한 사이트 Web Vital 성능 매트릭스의 경향을 비주얼라이즈 한 웹사이트


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## dimdenGD/ultimate-express: The Ultimate Express. Fastest http server with full Express compatibility, based on µWebSockets.
[github.com/dimdenGD/ultimate-express](https://github.com/dimdenGD/ultimate-express "dimdenGD/ultimate-express: The Ultimate Express. Fastest http server with full Express compatibility, based on µWebSockets.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">express</span> <span class="jser-tag">library</span></p>

µWebSockets 기반 express 호환 API 라이브러리


----
