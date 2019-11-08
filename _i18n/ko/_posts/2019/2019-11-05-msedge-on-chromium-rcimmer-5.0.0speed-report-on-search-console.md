---
title: "2019-11-05: MSEdge on Chromium RC, Immer 5.0.0, Speed Report on Search Console"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-11-05T00:09:40.841Z
category: JSer
tags:
- MSEdge
- Google
- Library

---

JSer.info #460 - Chromium 기반의 Microsoft Edge RC 버전이 릴리스됐습니다.

- [Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/)

로고가 새롭게 디자인됐습니다. 그리고 Microsoft Edge on Chromium은 이미 공개된 Microsoft Edge Insider Channels의 Canary, Dev, Beta로 테스트할 수 있습니다.
RC 릴리스 소식을 전하는 글에는 자동 테스트에 사용할 수 있는 웹 드라이버, 퍼펫티어를 소개하고 IE 드라이버 서버를 사용한 IE 모드 실행 및 활용 방법에 대해 작성돼 있습니다.
향후 개발 될 기능과 상황에 대해서는 아래 스테이터스, 익스플레너 문서를 참고하시길 바랍니다. 

- [Microsoft Edge web platform features status and roadmap - Microsoft Edge Development](https://developer.microsoft.com/en-us/microsoft-edge/platform/status/crossdomainfontloading/)
- [MicrosoftEdge/MSEdgeExplainers: Home for explainer documents originated by the Microsoft Edge team](https://github.com/MicrosoftEdge/MSEdgeExplainers)

----

객체 상태를 불변(immutable)하게 변경하는 라이브러리인 Immer.js 5.0.0이 릴리스됐습니다.

- [Release v5.0.0 · immerjs/immer](https://github.com/immerjs/immer/releases/tag/v5.0.0)

5.0.0에서는 `Map`과 `Set` 객체를 지원합니다.
자세한 내용은 아래 문서를 참고하시길 바랍니다.

- [Working with classes · Immer](https://immerjs.github.io/immer/docs/complex-objects)
- [Support for Set and Map · Issue #146 · immerjs/immer](https://github.com/immerjs/immer/issues/146)

----

Google Search Console에 Speed Report가 시험적으로 추가됐습니다.

- [Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console](https://webmasters.googleblog.com/2019/11/search-console-speed-report.html)

[Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)의 데이터를 기반으로 속도에 관해 Low, Middle, Fast 세 가지 그룹으로 나눠 문제를 알려줍니다.
문제의 방법에 관한 자세한 내용은 [Lighthouse](https://github.com/GoogleChrome/lighthouse)의 기반이 되는 [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)로 이동하여 살펴볼 수 있는 형태로 돼 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## OpenJS Foundation launches new professional certification program to support the future of Node.js development - OpenJS Foundation
[openjsf.org/blog/2019/10/22/openjs-foundation-launches-new-professional-certification-program-to-support-the-future-of-node-js-development/](https://openjsf.org/blog/2019/10/22/openjs-foundation-launches-new-professional-certification-program-to-support-the-future-of-node-js-development/ "OpenJS Foundation launches new professional certification program to support the future of Node.js development - OpenJS Foundation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

OpenJS Foundation(Node.js Foundation)이 Node.js 애플리케이션 개발과 Node.js 서비스 개발에 대한 두 가지 인증 프로그램을 공개했습니다.


----

## Release v0.111.0 · facebook/flow
[github.com/facebook/flow/releases/tag/v0.111.0](https://github.com/facebook/flow/releases/tag/v0.111.0 "Release v0.111.0 · facebook/flow")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">ReleaseNote</span></p>

FlowType 0.111.0이 릴리스됐습니다.
Object spread 문법에 의한 객체 병합에 대한 타입 추론이 개선됐습니다.
재검사 시 성능을 높이는 시험적인 플래그로 `experimental.minimal_merge`가 추가됐습니다.

- [Now you can spread disjoint unions without getting errors!](https://medium.com/flow-type/spreads-common-errors-fixes-9701012e9d58 "Now you can spread disjoint unions without getting errors!")

----

## The npm Blog — Release: 6.12.1
[blog.npmjs.org/post/188679949625/release-6121](https://blog.npmjs.org/post/188679949625/release-6121 "The npm Blog — Release: 6.12.1")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.12.1이 릴리스됐습니다.
Node.js 13 지원과 관련한 버그가 수정됐습니다.


----

## Release v5.0.0 · immerjs/immer
[github.com/immerjs/immer/releases/tag/v5.0.0](https://github.com/immerjs/immer/releases/tag/v5.0.0 "Release v5.0.0 · immerjs/immer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Immer 5.0.0이 릴리스됐습니다.
Map과 Set을 지원합니다.


----

## Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/](https://blogs.windows.com/msedgedev/2019/11/04/edge-chromium-release-candidate-get-ready/ "Getting your sites ready for the new Microsoft Edge - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge on Chromium RC 버전이 릴리스됐습니다.
WebDriver 대응, Puppeteer 대응, IEDriverServer 사용한 MSEdge의 IE 모드 실행 등이 소개돼 있습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Hands-on guide: developing & deploying Node.js apps in Kubernetes
[learnk8s.io/nodejs-kubernetes-guide/](https://learnk8s.io/nodejs-kubernetes-guide/ "Hands-on guide: developing & deploying Node.js apps in Kubernetes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Docker</span> <span class="jser-tag">kubernetes</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

Express + Mongo 구조의 Node.js 애플리케이션을 Docker로 실행한 후 minikube를 사용해 로컬의 Kubernates로 클러스터 및 스케일링을 테스트하는 튜토리얼 글입니다.


----

## 5 TypeScript tips to improve your applications
[nehalist.io/5-typescript-tips-to-improve-your-architecture/](https://nehalist.io/5-typescript-tips-to-improve-your-architecture/ "5 TypeScript tips to improve your applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 타입과 관련한 팁을 소개하는 글입니다.
Utility types, `unknown` 타입 이용, Lookup Types, 라이브러리 타입 확장, 빌트인 타입에 대한 팁을 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## React Conf 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLPxbbTqCLbGHPxZpw4xj\_Wwg8-fdNxJRh](https://www.youtube.com/playlist?list=PLPxbbTqCLbGHPxZpw4xj_Wwg8-fdNxJRh "React Conf 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

React Conf 2019 영상이 공개됐습니다.

- [React Conf 2019 - Fall 2019 in Lake Las Vegas, Nevada](https://conf.reactjs.org/ "React Conf 2019 - Fall 2019 in Lake Las Vegas, Nevada")

----

## ReactHooks로゙video를 능숙하게 다루기 - Speaker Deck(일본어)
[speakerdeck.com/narirou/reacthookstevideowocheng-rikonasu](https://speakerdeck.com/narirou/reacthookstevideowocheng-rikonasu "ReactHooks로゙video를 능숙하게 다루기 - Speaker Deck(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">video</span> <span class="jser-tag">slide</span></p>

React Hooks를 사용해 Video 플레이어를 만드는 방법을 소개하는 슬라이드입니다.
`<video>` 요소가 갖는 복잡한 상태를 관리, 갱신 빈도에 맞춰 상태 분리, React Hooks 사용 방법 등에 대해서 이야기합니다.利用についてな


----

## Building (And Re-Building) the Airbnb Design System | Maja Wichrowska & Tae Kim - YouTube
[www.youtube.com/watch?v&#x3D;fHQ1WSx41CA&amp;list&#x3D;PLPxbbTqCLbGHPxZpw4xj\_Wwg8-fdNxJRh&amp;index&#x3D;10&amp;t&#x3D;0s](https://www.youtube.com/watch?v=fHQ1WSx41CA&list=PLPxbbTqCLbGHPxZpw4xj_Wwg8-fdNxJRh&index=10&t=0s "Building (And Re-Building) the Airbnb Design System | Maja Wichrowska & Tae Kim - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Design</span> <span class="jser-tag">React</span> <span class="jser-tag">video</span></p>

Airbnb 디자인 시스템의 과거와 현재 그리고 미래에 대한 발표 영상입니다.
처음엔 파편화(fragmentation) 문제가 있어 CSS-in-JS를 사용해 디자인을 DSL에 붙였더니 복잡해지고 성능 문제가 생겨서 유연성과 성능을 모두 만족하는 모듈 구조를 목표로 시스템을 재구축하고 있다는 이야기입니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## SameSite cookie recipes
[web.dev/samesite-cookie-recipes/](https://web.dev/samesite-cookie-recipes/ "SameSite cookie recipes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span></p>

SameSite Cookies으로의 대응 방법에 대해 작성돼 있습니다.
SameSite=None에 대응 하고있지 않은 UA를 위해서 레거시한 Cookie와 SameSite 속성을 붙인 쿠키를 모두 전달하는 패턴이 소개돼 있습니다.


----

## Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console
[webmasters.googleblog.com/2019/11/search-console-speed-report.html](https://webmasters.googleblog.com/2019/11/search-console-speed-report.html "Official Google Webmaster Central Blog \[EN\]: Get faster with the new Speed report in Search Console")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">performance</span></p>

Google Search Console에 Chrome UX Report를 사용한 속도에 관한 리포트가 일반 공개됐습니다.
PC, 모바일 별 속도를 Low, Middle, Fast으로 분류하고 문제의 원인과 개선 방법에 대한 정보를 제공하는 화면이 추가됐습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mciastek/sal: 🚀 Performance focused, lightweight scroll animation library 🚀
[github.com/mciastek/sal](https://github.com/mciastek/sal "mciastek/sal: 🚀 Performance focused, lightweight scroll animation library 🚀")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">animation</span></p>

Intersection Observer를 사용한 스크롤 기반 애니메이션 라이브러리입니다.


----

## mikro-orm/mikro-orm: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Supports MongoDB, MySQL, MariaDB, PostgreSQL and SQLite databases.
[github.com/mikro-orm/mikro-orm](https://github.com/mikro-orm/mikro-orm "mikro-orm/mikro-orm: TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Supports MongoDB, MySQL, MariaDB, PostgreSQL and SQLite databases.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">rnode</span> <span class="jser-tag">library</span> <span class="jser-tag">MySQL</span> <span class="jser-tag">MongoDB</span></p>

TypeScript로 작성한 MongoDB, MySQL, PostgreSQL 등을 지원하는 ORM 맵퍼 라이브러리입니다.


----

## kroitor/asciichart: Nice-looking lightweight console ASCII line charts ╭┈╯ for NodeJS, browsers and terminal, no dependencies
[github.com/kroitor/asciichart](https://github.com/kroitor/asciichart "kroitor/asciichart: Nice-looking lightweight console ASCII line charts ╭┈╯ for NodeJS, browsers and terminal, no dependencies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">graphic</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span></p>

콘솔 환경에 아스키(ascii) 꺾은선 그래프를 그릴 수 있는 라이브러리입니다.


----
