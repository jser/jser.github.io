---
title: "2021-12-08: Rust + Node-API를 이용한 패키지 공개, #WebSpeedHackathon, The 2021 Web Almanac"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-12-08T03:54:12.200Z
category: JSer
tags:
- Svelte
- node.js
- Tools
- book
- HTTP

---

JSer.info #569 - [Rust + Node-API을 이용해 크로스 플랫폼 용 npm 패키지를 공개한다 - 별로 힘들지 않는 블로그(일본어)](https://shisama.hatenablog.com/entry/2021/12/03/054437)에는 Rust와 napi-rs를 사용해 작성한 코드를 Node.js에서 사용하는 방법이 소개 돼 있다.

패키지로 공개할 경우, Node.js의 Node-API를 사용하기 때문에 네이티브 모듈로서 설치할 필요가 있다.

그 경우, 설치 후에 `postinstall`에서 바이너리를 다운로드 & 빌드 하는 게 아니라 `optionalDependencies`를 사용해 아키텍처 별로 패키지를 설치할 수 있도록 하는 방법을 함께 소개하고 있다.

---

[#WebSpeedHackathon](https://twitter.com/search?f=realtime&q=%0A%23WebSpeedHackathon) 2021년 버전이 개최됐습니다.

- [무거운 사이트를 가볍게! 연말 연시는 #WebSpeedHackathon 2021에 도전하자. | CyberAgent Developers Blog](https://developers.cyberagent.co.jp/blog/archives/32747/)(일본어)
- [CyberAgentHack/web-speed-hackathon-2021](https://github.com/CyberAgentHack/web-speed-hackathon-2021)

무거운 웹 사이트 성능을 개선하는 해커톤의 소재로 활용하기 위해서 만들어진 애플리케이션. 참가자를 해당 앱의 성능을 개선 것이 과제다.
2022년 1월 3일 까지 개최하며 스코어는 GitHub Actions로 측정하는 구조도 공개돼 있다.
웹 사이트 성능 개선에 흥미가 있다면 한번 다뤄보길 바란다.

---

HTTP Archive 데이터를 기반으로 웹의 현황을 정리하는 Web Almanac의 2021년 버전이 공개됐다.

- [The 2021 Web Almanac](https://almanac.httparchive.org/en/2021/)

브라우저의 기술 현황이나 웹의 상태를 가늠할 수 있는 보고서로 총 24 장으로 구성돼 있다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Node v17.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v17.2.0/](https://nodejs.org/en/blog/release/v17.2.0/ "Node v17.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 17.2.0 릴리스.
`async_hooks` 모듈에 `asyncWrapProviders` 추가, AbortSignal에 `reason` 추가.


----
<h1 class="site-genre">아티클</h1>

----

## Rust + Node-API으로 크로스 플랫폼 용 npm 패키지를 공개한다 - 별로 힘들지 않는 블로그(일본어)
[shisama.hatenablog.com/entry/2021/12/03/054437](https://shisama.hatenablog.com/entry/2021/12/03/054437 "Rust + Node-API으로 크로스 플랫폼 용 npm 패키지를 공개한다 - 별로 힘들지 않는 블로그")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Rust로 작성된 코드를 napi-rs를 사용하여 Node.js의 native modules로 사용하는 방법 소개.
`postinstall` 대신 `optionalDependencies`를 활용하여 아키텍쳐 별 바이너리를 publish 하는 방법도 다루고 있다.

----

## react-router를 만드는 방법(일본어)
[zenn.dev/stin/articles/how-to-develop-react-router](https://zenn.dev/stin/articles/how-to-develop-react-router "react-router를 만드는 방법(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">history</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

react-router가 내부적으로 사용하고 있는 history 라이브러리를 사용해 라우터를 만드는 방법을 소개한다.


----

## 무거운 사이트를 가볍게! 연말 연시는 #WebSpeedHackathon 2021에 도전해보자 | CyberAgent Developers Blog(일본어)
[developers.cyberagent.co.jp/blog/archives/32747/](https://developers.cyberagent.co.jp/blog/archives/32747/ "무거운 사이트를 가볍게! 연말 연시는 #WebSpeedHackathon 2021에 도전해보자 | CyberAgent Developers Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">example</span> <span class="jser-tag">article</span></p>

웹 성능 개선을 주제로 한 해커톤 개요와 참가자 과제 공개.

- [CyberAgentHack/web-speed-hackathon-2021](https://github.com/CyberAgentHack/web-speed-hackathon-2021 "CyberAgentHack/web-speed-hackathon-2021")

----

## Web Performance Calendar » HTTP compression
[calendar.perfplanet.com/2021/http-compression/](https://calendar.perfplanet.com/2021/http-compression/ "Web Performance Calendar » HTTP compression")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

무손실 데이터 압축 시 압축 레벨과 속도와의 밸런스에 대해 작성돼 있다.
gzip, brotli, zstd 등의 압축 레벨에서 발생하는 트레이트 오프에 대해서 이야기하며 바이너리 콘텐츠의 이중 압축 문제 등도 다루고 있다.


----

## WebAssembly and Back Again: Fine-Grained Sandboxing in Firefox 95 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/](https://hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/ "WebAssembly and Back Again: Fine-Grained Sandboxing in Firefox 95 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox 95에 포함될 RLBox라는 WebAssembly를 이용한 Sandbox 구조를 소개한다.
프로세스 분리는 오버헤드가 발생하기 쉽다. 그래서 분리 하고싶은 코드를 Wasm으로 변환 한 후 Wasm을 wasm2c으로 C언어로 변환하여 네이티브 코드로 이용한다.
Wasm을 경유하는 방법으로 지정 외 메모리 공간에 접근할 수 없는 것을 보장할 수 있다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JSConf JP 2021 Track A - YouTube
[www.youtube.com/playlist?list&#x3D;PL42hYWKFRfN7cg6c3uM4\_tAxbybVzG3ao](https://www.youtube.com/playlist?list=PL42hYWKFRfN7cg6c3uM4_tAxbybVzG3ao "JSConf JP 2021 Track A - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JSConf JP 2021 영상 목록이 공개됐다.

- [JSConf JP 2021 Track B - YouTube](https://www.youtube.com/playlist?list=PL42hYWKFRfN7XWswj9wcC0j4191KNJuO3 "JSConf JP 2021 Track B - YouTube")
- [JSConf JP 2021 Track C - YouTube](https://www.youtube.com/playlist?list=PL42hYWKFRfN4l-KXE-2xzy95dRKPtCg0V "JSConf JP 2021 Track C - YouTube")
- [JSConf JP](https://jsconf.jp/2021/ "JSConf JP")

----

## Svelte Summit Fall 2021 - YouTube
[www.youtube.com/playlist?list&#x3D;PL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt](https://www.youtube.com/playlist?list=PL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt "Svelte Summit Fall 2021 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Svelte Summit Fall 2021의 발표 영상이 공개됐다.

- [Svelte Summit Fall 2021](https://card.zenn.dev/?url=https%3A%2F%2Fwww.youtube.com%2Fplaylist%3Flist%3DPL8bMgX1kyZTg2bI9IOMgfBc8lrU3v2itt "Svelte Summit Fall 2021")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## primo-af/primo: a simpler, all-in-one way to develop and manage websites
[github.com/primo-af/primo](https://github.com/primo-af/primo "primo-af/primo: a simpler, all-in-one way to develop and manage websites")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">CMS</span> <span class="jser-tag">OpenSource</span> <span class="jser-tag">software</span></p>

정적 사이트를 관리, 개발하기 위한 CMS 애플리케이션.
Svelte 기반으로 만들어져 있으며 데스크탑 애플리케이션으로 사이트를 편집할 수 있다. 또,  Supabase 기반의 백엔드 솔루션도 함께 공개돼 있다.


----

## Online CSS Analyzer - Project Wallace
[www.projectwallace.com/analyze-css](https://www.projectwallace.com/analyze-css "Online CSS Analyzer - Project Wallace")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">webservice</span></p>

URL을 지정하면 해당 사이트가  이용하고 있는 CSS를 해석해주는 도구.
사이즈, 셀렉터 수, 상세도(specificity), 색상, 폰트, 복잡도 등에 대한 분석 결과를 제공한다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## denoland/dnt: Deno to npm package build tool.
[github.com/denoland/dnt](https://github.com/denoland/dnt "denoland/dnt: Deno to npm package build tool.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

Deno 용으로 작성된 모듈을 Node.js로 사용할 수 있도록 변환하는 도구.

- [dnt 라는 도구에 대해서 - Qiita](https://qiita.com/kt3k/items/8947fddc9f580ba32307 "dnt 라는 도구에 대해서 - Qiita")(일본어)

----

## Open Props: sub-atomic styles
[open-props.style/](https://open-props.style/ "Open Props: sub-atomic styles")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

CSS custom properties를 전면적으로 사용해 설계한 라이브러리.


----

## BuilderIO/mitosis: Write components once, run everywhere. Compiles to Vue, React, Solid, Angular, Svelte, and more.
[github.com/BuilderIO/mitosis](https://github.com/BuilderIO/mitosis "BuilderIO/mitosis: Write components once, run everywhere. Compiles to Vue, React, Solid, Angular, Svelte, and more.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JSX 기반 컴포넌트를 정의하고 그것을 React / Angular / Vue / Solid / Svelte 등의 각 프레임워크에 적합한 코드로 변환할 수 있는 도구.
UI 프레임워크의 중간 언어 느낌.


----

## plentico/plenti: Static Site Generator with Go backend and Svelte frontend
[github.com/plentico/plenti](https://github.com/plentico/plenti "plentico/plenti: Static Site Generator with Go backend and Svelte frontend")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">Tools</span> <span class="jser-tag">golang</span></p>

Svelte와 Go 언어를 사용해 개발된 정적 사이트 제너레이터.


----
<h1 class="site-genre">도서</h1>

----

## The 2021 Web Almanac
[almanac.httparchive.org/en/2021/](https://almanac.httparchive.org/en/2021/ "The 2021 Web Almanac")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">book</span> <span class="jser-tag">browser</span> <span class="jser-tag">HTTP</span></p>

HTTP Archive의 데이터를 기반으로 정리한 보고서 Web Almanac의 2021년 버전.
브라우저의 기술 현황이나 웹의 상태를 확인할 수 있는 자료다.


----

## The Jamstack Book
[www.manning.com/books/the-jamstack-book](https://www.manning.com/books/the-jamstack-book "The Jamstack Book")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Jamstack</span> <span class="jser-tag">book</span></p>

2022년 4월 26일에 출간 예정인 Jamstack을 주제로한 도서


----
