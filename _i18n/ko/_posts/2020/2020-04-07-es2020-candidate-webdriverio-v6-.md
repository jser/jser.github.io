---
title: "2020-04-07: ES2020 Candidate、, WebdriverIO v6, 브라우저의 릴리스 정보를 모니터링하는 방법"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-04-07T01:38:40.312Z
category: JSer
tags:
- ECMAScript
- WebDriver
- Browser

---

JSer.info #482 - ECMAScript 2020의 릴리스 후보가 공개됐습니다.

- [Release ES2020 Candidate · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2020)

[ES2020 Candidate](https://tc39.es/ecma262/2020/)는 TC39에서 승인된 형태로, 2020년 6월에 있을 Ecma의 [General Assembly](https://www.ecma-international.org/memento/ga.htm)에서 승인되면 정식으로 ECMAScript 2020으로서 릴리스됩니다.

또, 이번 3월 부터 4월에 걸쳐 행해진 TC39 미팅에서 `import.meta`가 Stage 4로 변경됐습니다.

- [ECMAScript proposal updates @ 2020-04 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update)

이로인해 `import.meta`도 아슬아슬하게 ES2020에 포함되게 됐습니다.
ES2020에 포함되는 Proposal은 아래 문서에 정리돼 있습니다.

- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md)
- [ECMAScript 2020: the final feature set](https://2ality.com/2019/12/ecmascript-2020.html)

----

WebdriverIO v6가 릴리스 됐습니다.

- [WebdriverIO v6 Released · WebdriverIO](https://webdriver.io/blog/2020/03/26/webdriverio-v6-released.html)

WebdriverIO v6에서는 `devtools`가 기본적으로 활성화 됩니다.
WebdriverIO는 Webdriver API를 사용하며, 현재의 Webdriver API에서는 접속한 브라우저의 개발자 도구를 사용할 수 없습니다.
때문에 `devtools`에서는 Puppeteer를 통합해 이 문제를 회피합니다.

- [Chrome DevTools as Automation Protocol · WebdriverIO](https://webdriver.io/blog/2019/09/16/devtools.html)

이와 관련해 Webdriver API 쪽에도 MSEdge Team에 의한 양방향 통신 제안이 공개돼 있습니다.

- [MSEdgeExplainers/WebDriverRPC at master · MicrosoftEdge/MSEdgeExplainers](https://github.com/MicrosoftEdge/MSEdgeExplainers/tree/master/WebDriverRPC)

이 외에 비권장된 [request](https://github.com/request/request) 대신 [got](https://github.com/sindresorhus/got)를 사용한 성능 개선이 이뤄졌으며 타입스크립트 지원이 추가됐습니다.

----

JSer.info에서도 브라우저 릴리스 정보를 모니터링하고 있으며 이와 관련해 브라우저 릴리스 정보 사이트를 모아봤습니다.

- [브라우저 / 보안 / 정보 보호 관련 1차 정보에 가까운 2차 정보의 정보원을 정리한 문서](https://gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511)(일본어)

실제로는 좀 더 많은 리소스를 살펴보고 있지만 이를 간추려 정보원에 가까운 곳을 정리했습니다.

공개한 글과 함께 브라우저 공식 블로그나 이슈, SNS 등을 정리한 browser-resources도 갱신하고 있으니 살펴봐주시길 바랍니다.

- [azu/browser-resources: A Collection of official Resources/Status/Issues for browsers.](https://github.com/azu/browser-resources)

이 외로 브라우저 관련 RSS 등을 정리한 다음 사이트가 도움이 될 것 같습니다.

- [Web Browser Eng](https://topicdeck.com/web-dev/browser-eng/chromium/)
- [PaulKinlan/topicdeck: An NPM module that hosts and aggregates collections of RSS feeds.](https://github.com/PaulKinlan/topicdeck)
    - Chrome 팀의 [Paul Kinlan](https://github.com/PaulKinlan)이 관리하고 있다

----

<h1 class="site-genre">헤드라인</h1>

----

## Release ES2020 Candidate · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2020](https://github.com/tc39/ecma262/releases/tag/es2020 "Release ES2020 Candidate · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ES2020 릴리스 후보가 공개됐습니다.
`import.meta`도 ES2020에 포함됐습니다.


----

## WebdriverIO v6 Released · WebdriverIO
[webdriver.io/blog/2020/03/26/webdriverio-v6-released.html](https://webdriver.io/blog/2020/03/26/webdriverio-v6-released.html "WebdriverIO v6 Released · WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

WebdriverIO v6가 릴리스됐습니다.
Node 8 지원이 종료됐으며 Puppeteer 통합과 `devtools` 패키지 기본 활성화 됐고, `request`에서 `got`으로 변경하여 성능 개선이 이뤄졌습니다. 또, 타입스크립트를 지원합니다.


----

## Chromium Blog: Temporarily rolling back SameSite Cookie Changes
[blog.chromium.org/2020/04/temporarily-rolling-back-samesite.html](https://blog.chromium.org/2020/04/temporarily-rolling-back-samesite.html "Chromium Blog: Temporarily rolling back SameSite Cookie Changes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">news</span> <span class="jser-tag">security</span></p>

Chrome 80에서 단계적으로 롤아웃 됐던 SameSite의 기본값을 Lax로 변경하는 계획을 롤백, 디폴트 변경을 일시적으로 하지 않겠다는 글입니다.
여름을 목표로 다시 시행한다고 합니다.

- [SameSite Updates - The Chromium Projects](https://www.chromium.org/updates/same-site "SameSite Updates - The Chromium Projects")

----

## New WebKit Features in Safari 13.1 | WebKit
[webkit.org/blog/10247/new-webkit-features-in-safari-13-1/](https://webkit.org/blog/10247/new-webkit-features-in-safari-13-1/ "New WebKit Features in Safari 13.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 13.1의 변경 사항이 정리돼 있습니다.
iPadOS 13.4에서 Pointer Events를 대응했고 Web Animations API, Async Clipboard API, ResizeObserver, Picture-in-Picture를 지원합니다. 또, ES Proposal의 Nullish coalesing operator(`??`), CSS Shadow Parts를 지원하며 ITP 갱신 등이 이뤄졌습니다.


----
<h1 class="site-genre">아티클</h1>

----

## 브라우저 / 보안 / 정보 보호 관련 1차 정보에 가까운 2차 정보의 정보원을 정리한 문서
[gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511](https://gist.github.com/azu/7e879fd0c4598476b93aecd4d8dbb511 "ブラウザ/セキュリティ/プライバシー周りの一次情報に近い二次情報の情報源をまとめたもの")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">article</span> <span class="jser-tag">MSEdge</span> <span class="jser-tag">Firefox</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">safari</span> <span class="jser-tag">webkit</span></p>

브라우저의 새로운 API나 릴리스 등을 모니터링 하는 방법과 참고 사이트를 정리 했습니다.


----

## ECMAScript proposal updates @ 2020-04 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2020/04/04/ecmascript-proposal-update "ECMAScript proposal updates @ 2020-04 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

2020-03에서 2020-04에 걸쳐 진행한 TC39MTG에서 변경된 Proposal이 정리돼 있습니다.
`import.meta`가 Stage 4로 변경돼 ECMAScript 2020에 포함됐습니다.

- [Release ES2020 Candidate · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2020 "Release ES2020 Candidate · tc39/ecma262")

----

## LCH colors in CSS: what, why, and how? | Lea Verou
[lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/](http://lea.verou.me/2020/04/lch-colors-in-css-what-why-and-how/ "LCH colors in CSS: what, why, and how? | Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Color Modules Level 4에 정의돼 있는 LCH 색상을 설명하는 글입니다.
LCH란 무엇인지 왜 도입되고 있는지에 대해 정리돼 있습니다. RGB에 비해 많은 색상을 사용할 수 있는 점 등에 대해서도 이야기합니다.


----

## 프런트엔드 x RTC와 관련한 최근과 다음 - console.lealog();(일본어)
[lealog.hateblo.jp/entry/2020/04/02/094225](https://lealog.hateblo.jp/entry/2020/04/02/094225 "フロントエンド x RTC界隈の最近とこれから - console.lealog();")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

WebRTC 관련 Web Platform API 스테이터스와 Proposal에 대해서 작성돼 있습니다.
WebTransport, WebRTC-QUIC, WebCodecs, WebSocketStream 등 관련한 API도 소개합니다.


----

## A QUIC Update for Node.js
[www.nearform.com/blog/a-quic-update-for-node-js/](https://www.nearform.com/blog/a-quic-update-for-node-js/ "A QUIC Update for Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span> <span class="jser-tag">QUIC</span></p>

Node.js에서 QUIC 프로토콜 구현에 대해 작성돼 있습니다.
QUIC의 개요, Node.js Core에 추가할 목적으로 구현하고 있는 `quic` 모듈을 소개합니다.

- [nodejs/quic: Exploring a QUIC implementation for Node.js core](https://github.com/nodejs/quic "nodejs/quic: Exploring a QUIC implementation for Node.js core")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## engine262/engine262: An implementation of ECMA-262 in JavaScript
[github.com/engine262/engine262](https://github.com/engine262/engine262 "engine262/engine262: An implementation of ECMA-262 in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

JavaScript로 개발된 ECMAScript-262 구현체입니다.
JavaScript 개발자가 새로운 언어 기능의 프로토타이핑을 쉽게 할 수 있도록 관련 기능을 제공하는데 목적을 두고 잇습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Lezer
[lezer.codemirror.net/](https://lezer.codemirror.net/ "Lezer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">AST</span></p>

인크리멘탈 파싱을 수행하는 파서 시스템 라이브러리입니다.
문법을 정의해 파싱을 인크리멘탈하게 수행하며 에러 복귀 등에도 대응한 AST를 생성하는 파서 제너레이터입니다.
에디터의 신텍스 하이라이트와 같은 기능에 이용할 수 있으며 Code Mirror 팀에서 개발하고 있습니다.


----

## lirantal/npq: 🎖safely\* install packages with npm or yarn by auditing them as part of your install process
[github.com/lirantal/npq](https://github.com/lirantal/npq "lirantal/npq: 🎖safely\* install packages with npm or yarn by auditing them as part of your install process")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm이나 yarn에서 패키지를 설치할 때에 패키지의 다운로드 수, README 유무, 설치 스크립트 등을 확인하고 Snyk로 검사를 수행하는 CLI 도구입니다.


----

## Keyboard Event Viewer
[w3c.github.io/uievents/tools/key-event-viewer.html](https://w3c.github.io/uievents/tools/key-event-viewer.html "Keyboard Event Viewer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Keyboard</span> <span class="jser-tag">Tools</span> <span class="jser-tag">DOM</span></p>

JavaScript의 Keyboard Event 뷰어입니다.


----

## caroso1222/notyf: 👻 A minimalistic, responsive, vanilla JavaScript library to show toast notifications.
[github.com/caroso1222/notyf](https://github.com/caroso1222/notyf "caroso1222/notyf: 👻 A minimalistic, responsive, vanilla JavaScript library to show toast notifications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

의존 모듈 없는 토스트 메시지를 제공하는 UI 라이브러리입니다.


----
