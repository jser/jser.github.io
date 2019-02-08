---
title: "2019-02-05: Firefox 65(WebP), Safari 12.1(릴리스후보), ECMAScript 2019의 기능 결정"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-02-05T00:35:02.073Z
category: JSer
tags:
- firefox
- safari
- ECMAScript

---

JSer.info #421 - Firefox 65를 릴리스했습니다.

- [Firefox 65.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/65.0/releasenotes/ "Firefox 65.0, See All New Features, Updates and Fixes")
- [Firefox 65 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/65 "Firefox 65 for developers - Mozilla | MDN")
- [Firefox 65 사이트 호환성 정보 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/65/ "Firefox 65 사이트 호환성 정보 | Firefox 사이트 호환성 정보")(일본어)
- [Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/01/firefox-65-webp-flexbox-inspector-new-tooling/ "Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog")

Firefox 65에서는 개발자 도구의 한 기능인 [CSS Flexbox Inspector](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Examine_Flexbox_layouts)를 추가했고, CSS `env()`를 지원하며 `Intl.RelativeTimeFormat`와 `globalThis`를 구현했습니다.
또, 지금까지 플래그를 붙여 시범적으로 지원하던 Storage Access API와 Readable Streams을 기본적으로 활성화했습니다.

[RFC 8441 - Bootstrapping WebSockets with HTTP/2](https://tools.ietf.org/html/rfc8441)로 표준화된 WebSockets HTTP/2 대응, 이미지 타입 WebP 지원 등이 이뤄졌습니다.

----

iOS 12.2/macOS 10.14.4와 함께 공개할 예정인 Safari 12.1의 릴리스 노트를 공개했습니다(아직 정식 릴리스는 이뤄지지 않았습니다).

- [Safari 12.1 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari_release_notes/safari_12_1_release_notes)

Safari 12.1는 [Safari Technology Preview 62](https://webkit.org/blog/8384/release-notes-for-safari-technology-preview-62/)의 일부 변경 사항이 포함된 것 같습니다.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Safari Technology Preview 62 is out!<br><br>A small note: STP 62 bumps its Safari version number from 12.0 to 12.1. That is, STP is now tracking a release after Safari 12.<br><br>Release Notes: <a href="https://t.co/vt8myfz7NO">https://t.co/vt8myfz7NO</a> <a href="https://t.co/yrgHQyUpSa">pic.twitter.com/yrgHQyUpSa</a></p>&mdash; Ricky Mondello (@rmondello) <a href="https://twitter.com/rmondello/status/1024708391396995072?ref_src=twsrc%5Etfw">August 1, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Safari 12.1에서는 ITP(Intelligent Tracking Prevention)를 강화하고 다크 모드를 지원하기 위한 color scheme를 지원합니다. Intersection Observer API, Web Share API, `<datalist>`를 추가했습니다.
또, WebRTC Unified Plan과 VP8도 지원합니다.

- [Safari 12.1에서 VP8과 Unified Plan가 들어가다 – V – Medium](https://medium.com/@voluntas/safari-12-1-%E3%81%A7-vp8-%E3%81%A8-unified-plan-%E3%81%8C%E5%85%A5%E3%82%8B-47c3aa0cb9eb)(일본어)

----

2019년 1월에 TC39 미팅을 개최하고 ECMAScript 2019에 들어갈 기능을 결정했습니다.
ECMAScript 2019는 2019년 6월에 릴리스 할 예정이기 때문에 1월 미팅에서 Stage4로 정리한 기능까지 릴리스 대상이 됩니다.

- [agendas/11.md at master · tc39/agendas](https://github.com/tc39/agendas/blob/master/2018/11.md)
- [ECMAScript의 사양 책전에 관한 컨닝페이퍼 | Web Scratch](https://efcl.info/2015/10/18/ecmascript-paper/)

1월 미팅에서는 `Object.fromEntries`, Well-formed `JSON.stringify`, `String.prototype.{trimStart,trimEnd}`, `Array.prototype.{flat,flatMap}`를 Stage 4로 변경하여 ES 2019에 추가했습니다.

- [\[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates)

최종적으로 ES2019에 들어갈 기능은 다음 문서에 정리하고 있으니 참고하시길 바랍니다.

- [ECMAScript 2019: the final feature set](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")
- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

주로 메서드 추가가 이뤄졌으며 Decorator나 Private field 등 구문이 바뀌는 Proposal은 아직 Stage 4가 아니기 때문에 ES2019엔 들어가지 않았습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Firefox 65.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/65.0/releasenotes/](https://www.mozilla.org/en-US/firefox/65.0/releasenotes/ "Firefox 65.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 65.0을 릴리스했습니다.
CSS `env()` 지원하고 `Intl.RelativeTimeFormat`/`globalThis` 구현했으며 Storage Access API/Readable Streams를 기본적으로 활성화했습니다.
또, WebSockets HTTP/2 대응, WebP 이미지 타입도 지원합니다.

- [Firefox 65 for developers | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/65 "Firefox 65 for developers | MDN")
- [Firefox 65 사이트 호환성 정보 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/65/ "Firefox 65 사이트 호환성 정보 | Firefox 사이트 호환성 정보")(일본어)
- [Firefox 65: WebP support, Flexbox Inspector, new tooling & platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2019/01/firefox-65-webp-flexbox-inspector-new-tooling/ "Firefox 65: WebP support, Flexbox Inspector, new tooling &amp; platform updates - Mozilla Hacks - the Web developer blog")

----

## Release v2.0.0 · facebook/relay
[github.com/facebook/relay/releases/tag/v2.0.0](https://github.com/facebook/relay/releases/tag/v2.0.0 "Release v2.0.0 · facebook/relay")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

GraphQL + React 라이브러리인 Repay v2.0.0을 릴리스했습니다.
React의 새로운 Context API에 대응했고 의존 관계를 갱신했으며 `replay-compiler`에서 Persisted Queries를 지원합니다.

- [Persisted Queries · Relay](https://facebook.github.io/relay/docs/en/persisted-queries.html "Persisted Queries · Relay")

----

## New in Chrome 72  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/01/nic72](https://developers.google.com/web/updates/2019/01/nic72 "New in Chrome 72  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 72를 릴리스했습니다.
Public class fields, User Activation API, `Intl.format`을 지원합니다.
또, HPKP 삭제, TLS 1.0과 1.1을 비권장합니다.

- [Chromium Blog: Chrome 72 Beta: Public class fields, user activation and more](https://blog.chromium.org/2018/12/chrome-72-beta-public-class-fields-user.html "Chromium Blog: Chrome 72 Beta: Public class fields, user activation and more")
- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D72 "Chrome Platform Status")
- [Deprecations and removals in Chrome 72  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/12/chrome-72-deps-rems "Deprecations and removals in Chrome 72  |  Web  |  Google Developers")

----

## Safari 12.1 Release Notes | Apple Developer Documentation
[developer.apple.com/documentation/safari\_release\_notes/safari\_12\_1\_release\_notes](https://developer.apple.com/documentation/safari_release_notes/safari_12_1_release_notes "Safari 12.1 Release Notes | Apple Developer Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 12.1(iOS 12.2/macOS 10.14.4에 포함될 예정)의 릴리스 노트를 공개했습니다。
ITP를 강화하고 color scheme와 Intersection Observer API, Web Share API, `<datalist>`, WebRTC Unified Plan, VP8을 지원합니다.

- [Ricky Mondello의 릴리스 관련 트위터](https://twitter.com/rmondello/status/1091073294202269696 "Ricky Mondello의 릴리스 관련 트위터")

----

## Announcing TypeScript 3.3 | TypeScript
[blogs.msdn.microsoft.com/typescript/2019/01/31/announcing-typescript-3-3/](https://blogs.msdn.microsoft.com/typescript/2019/01/31/announcing-typescript-3-3/ "Announcing TypeScript 3.3 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.3을 릴리스했습니다.
함수 호출에서의 Union Types 행위 개선했으며 `--build --watch` 시 인크리멘탈 빌드 시스템을 활용해 빌드 시간을 최적화했습니다.

- [TypeScript v3.3.0-rc 변경사항 - Qiita](https://qiita.com/vvakame/items/dadc91f0be6fc00085ae "TypeScript v3.3.0-rc 변경사항 - Qiita")

----

## Type Safe JavaScript with JSDoc – TruckJS – Medium
[medium.com/@trukrs/type-safe-javascript-with-jsdoc-7a2a63209b76](https://medium.com/@trukrs/type-safe-javascript-with-jsdoc-7a2a63209b76 "Type Safe JavaScript with JSDoc – TruckJS – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JSDoc</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">VSCode</span></p>

JSDoc과 `jsconfig.json`를 이용해 자바스크립트 타입을 검사하는 방법을 소개합니다.
`tsc`의 `checkJS` 기능을 사용해 JSDoc 문법을 그대로 이용해 타입 체크를 할 수 있습니다.


----

## \[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2019/02/03/ecmascript-proposal-updates "\[ES2019\] ECMAScript proposal updates @ 2019-01 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2019년 1월 TC39 미팅에서 ECMAScript Proposal을 결정하고 정리했습니다.
이번 미팅에서 Stage 4로 변경한 기능을 포함해 ES2019로 릴리스합니다.

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")
- [ECMAScript 2019: the final feature set](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")

----
<h1 class="site-genre">아티클</h1>

----

## Code-splitting for libraries—bundling for npm with Rollup 1.0
[levelup.gitconnected.com/code-splitting-for-libraries-bundling-for-npm-with-rollup-1-0-2522c7437697](https://levelup.gitconnected.com/code-splitting-for-libraries-bundling-for-npm-with-rollup-1-0-2522c7437697 "Code-splitting for libraries—bundling for npm with Rollup 1.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

Rollup을 사용한 라이브러리 번들 방법과 npm에 배포하는 과정을 설명합니다.
umd, esm, cjs 형식을 모두 배포하는 방법을 소개합니다.


----

## ECMAScript 2019: the final feature set
[2ality.com/2018/02/ecmascript-2019.html](http://2ality.com/2018/02/ecmascript-2019.html "ECMAScript 2019: the final feature set")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

1월 TC39 미팅에서 ECMAScript 2019에 들어갈 기능을 최종 결정했습니다.

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

----

## RTCQuicTransport Coming to an Origin Trial Near You (Chrome 73)  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/01/rtcquictransport-api](https://developers.google.com/web/updates/2019/01/rtcquictransport-api "RTCQuicTransport Coming to an Origin Trial Near You (Chrome 73)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">QUIC</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 73에서 QUIC로 접속해 데이터를 주고 받을 수 있는 API 인 `RTCQuicTransport`의 Origin Trial을 공개했습니다.
WebRTC NV(Next Version)에 대한 대처로 UDP 상의 QUIC을 사용한 Low Level API를 책정하는 게 목적입니다.

- [shampson/RTCQuicTransport-Origin-Trial-Documentation: Documentation and demos for developers using the RTCQuicTransport in Chrome's origin trial.](https://github.com/shampson/RTCQuicTransport-Origin-Trial-Documentation "shampson/RTCQuicTransport-Origin-Trial-Documentation: Documentation and demos for developers using the RTCQuicTransport in Chrome&#x27;s origin trial.")
- [WebRTC over QUIC – V – Medium](https://medium.com/@voluntas/webrtc-over-quic-d65425230ef "WebRTC over QUIC – V – Medium")

----

## Severe Security Vulnerability in Bower’s Zip Archive Extraction | Snyk
[snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction/](https://snyk.io/blog/severe-security-vulnerability-in-bowers-zip-archive-extraction/ "Severe Security Vulnerability in Bower’s Zip Archive Extraction | Snyk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span> <span class="jser-tag">ReleaseNote</span></p>

Bower의 zip/tar 압축 해제 처리에 취약점이 있어 수정 버전인 Bower 1.8.8을 릴리스했습니다.

- [Release v1.8.8 · bower/bower](https://github.com/bower/bower/releases/tag/v1.8.8 "Release v1.8.8 · bower/bower")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Chrome University 2018 - YouTube
[www.youtube.com/playlist?list&#x3D;PL9ioqAuyl6UIFAdsM5KU6P-hRJdh-BPmm](https://www.youtube.com/playlist?list=PL9ioqAuyl6UIFAdsM5KU6P-hRJdh-BPmm "Chrome University 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">video</span></p>

Chrome과 Chrome OS의 아키텍처에 관한 발표 영상을 정리하고 잇습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ungap
[ungap.github.io/](https://ungap.github.io/ "ungap")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span></p>

ES5 호환하는 ECMAScript 및 DOM API에 관련한 Polyfill을 정리한 프로젝트 저장소입니다.
각각의 polyfill을 모듈로 이용할 수 있으며 단일 조직(organization)에서 관리하는 데 목적이 있습니다.


----

## nextapps-de/flexsearch: Next-Generation full text search library for Browser and Node.js
[github.com/nextapps-de/flexsearch](https://github.com/nextapps-de/flexsearch "nextapps-de/flexsearch: Next-Generation full text search library for Browser and Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">search </span> <span class="jser-tag">library</span></p>

브라우저와 Node.js에서 동작하는 전문(全文) 검색 엔진 라이브러리입니다.
WebWorker를 대응하고 검색 관련 다양한 옵션을 지원합니다.


----

## lukeed/httpie: A Node.js HTTP client as easy as pie! 🥧
[github.com/lukeed/httpie](https://github.com/lukeed/httpie "lukeed/httpie: A Node.js HTTP client as easy as pie! 🥧")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

단순한 Node.js 용 Promise HTTP 라이브러리입니다.
Node의 코어 모듈 만을 사용해 개발했습니다.


----
<h1 class="site-genre">도서</h1>

----

## Chrome Developer Tools 입문 | 전자책과 프린트 온 디멘드（POD） | NextPublishing（넥스트퍼블리싱）(일본어)
[nextpublishing.jp/book/10430.html](https://nextpublishing.jp/book/10430.html "Chrome Developer Tools 입문 | 전자책과 프린트 온 디멘드（POD） | NextPublishing（넥스트퍼블리싱）")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">book</span></p>

2019년 2월 1일에 출간한 Chrome Developer Tools를 주제로한 도서입니다.


----
