---
title: "2019-11-19: Front-End Tooling Survey 2019, React 만드는 법"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-11-19T02:08:57.501Z
category: JSer
tags:
- Survey
- React

---

JSer.info #462 - 프런트엔드 관련 도구에 대한 설문 조사 Front-End Tooling Survey 2019의 결과가 공개됐습니다.

- [Front-End Tooling Survey 2019](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2019-results)

3,005명 개발자 대상으로 CSS, JavaScript 등에 관한 설문 조사 결과를 지난해의 설문 결과와 함께 비교하여 게재했습니다. 

CSS 관련 프리프로세서, 프레임워크, 명명 규칙과 CSS-in-JS 그리고 JavaScript 관련 프레임워크, 라이브러리, Bundler, Transpiler, 테스트 관련 결과가 공개돼 있으며 성능 테스트, 접근성 등에 관한 항목도 있습니다.

흥미가 있는 분은 한번 살펴보면 좋을 것 같습니다.

----

[Build your own React](https://pomb.us/build-your-own-react/)는 스크래치로 React 같은 DOM 렌더링 구조를 구현하는 방법을 소개하고 있습니다.
`createElement`, `render`와 같은 함수를 단계적으로 구현하며 Hooks API 구조까지 구현해보는 튜토리얼 느낌의 글입니다.

해당 글은 [Code Surfer](https://github.com/pomber/code-surfer)를 사용해 코드와 문장이 동기화 돼 표현되는 형태로 작성돼 있습니다.

또, React 상의 구조를 직접 살펴보고 싶은 분은 React 커스텀 렌더러를 구현하는 아래 동영상을 보면 재미있을 거 같습니다.

- [Building a Custom React Renderer | Sophie Alpert - YouTube](https://www.youtube.com/watch?v=CGpMlWVcHok)

----


<h1 class="site-genre">헤드라인</h1>

----

## Bytecode Alliance
[bytecodealliance.org/articles/announcing-the-bytecode-alliance](https://bytecodealliance.org/articles/announcing-the-bytecode-alliance "Bytecode Alliance")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">news</span></p>

Mozilla, Fastly, Intel, Red Hat 중심으로 WebAssembly의 안전한 에코 시스템을 만드는 게 목표인 Bytecode Alliance이라는 단체가 결성됐습니다.
npm을 예로한 현재 에코 시스템에서의 공격 사례와 Nanoprocess라고 불리는 Sandbox 구조에 대해서도 소개돼 있습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Upcoming notification permission changes in Firefox 72 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/11/upcoming-notification-permission-changes-in-firefox-72/](https://hacks.mozilla.org/2019/11/upcoming-notification-permission-changes-in-firefox-72/ "Upcoming notification permission changes in Firefox 72 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox 72에서 알림 허가 팝업은 사용자 상호 작용이 없으면 표시되지 않게 됩니다. 이에 대해서 소개하고 있습니다.


----

## Build your own React
[pomb.us/build-your-own-react/](https://pomb.us/build-your-own-react/ "Build your own React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

React와 같은 컴포넌트 렌더링 구조, Hooks 구조를 단계적으로 구현해보면서 살펴보는 글입니다.


----

## Handling Errors in Express | Zell Liew
[zellwk.com/blog/express-errors/](https://zellwk.com/blog/express-errors/ "Handling Errors in Express | Zell Liew")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Express의 에러 핸들링에 대해 이야기하는 글입니다.
`express-async-handler`를 사용한 async 에러 핸들링, `http-errors`를 사용한 에러 객체 작성, 커스텀 에러 핸들링이나 Fallback 등에 대해서 작성돼 있습니다.


----

## The Front-End Tooling Survey 2019 - Results - AshleyNolan.co.uk - Blog and Portfolio for Ashley Watson-Nolan
[ashleynolan.co.uk/blog/frontend-tooling-survey-2019-results](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2019-results "The Front-End Tooling Survey 2019 - Results - AshleyNolan.co.uk - Blog and Portfolio for Ashley Watson-Nolan")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">アンケート</span> <span class="jser-tag">article</span></p>

JavaScript나 CSS 도구와 관련한 설문 조사 The Front-End Tooling Survey 2019 결과가 공새됐습니다.
프리프로세서, 프레임워크, Lint, Bundler, Testing, Performance, Accessiblity 등에 대해서 조사했습니다.


----

## Building a native add-on for Node.js in 2019 - Sqreen Blog
[blog.sqreen.com/building-a-native-add-on-for-node-js-in-2019/](https://blog.sqreen.com/building-a-native-add-on-for-node-js-in-2019/ "Building a native add-on for Node.js in 2019 - Sqreen Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js의 네이티브 에드온을 만드는 방법에 대해서 소개합니다.
N-API 버전과 Node.js의 대응표와 NAN을 사용한 네이티브 애드온 작성 방법에 대해서 이야기합니다.


----

## Publishing Typings to DefinitelyTyped - Level Up Coding
[levelup.gitconnected.com/publishing-typings-to-definitelytyped-d4e0777e40f5](https://levelup.gitconnected.com/publishing-typings-to-definitelytyped-d4e0777e40f5 "Publishing Typings to DefinitelyTyped - Level Up Coding")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">article</span></p>

`@types` 패키지 작성 방법, 삭제 방법, DefinitelyTyped로 Pull Request 하는 방법, 테스트 방법 등을 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Chrome Dev Summit 2019 - All Sessions - YouTube
[www.youtube.com/playlist?list&#x3D;PLNYkxOF6rcIDA1uGhqy45bqlul0VcvKMr](https://www.youtube.com/playlist?list=PLNYkxOF6rcIDA1uGhqy45bqlul0VcvKMr "Chrome Dev Summit 2019 - All Sessions - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Chrome Dev Summmit 2019 영상이 공새됐습니다.


----

## 프런트엔드 엔지니어를 위한 보안 대책 ~XSS편~ / #frontkansai 2019 - Speaker Deck(일본어)
[speakerdeck.com/masashi/number-frontkansai-2019](https://speakerdeck.com/masashi/number-frontkansai-2019 "프런트엔드 엔지니어를 위한 보안 대책 ~XSS편~ / #frontkansai 2019 - Speaker Deck(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">XSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span></p>

XSS를 주제로 한 슬라이드입니다.
XSS 종류(Reflected, Stored, DOM Based)를 소개하고 각각의 전형적인 대책 방법에 대해서 소개합니다.
또, CSP나 Truested Types 등 예방책에 대해서도 이야기합니다.

- [이제까지의 프런트엔드 보안 - Speaker Deck(일본어)](https://speakerdeck.com/hasegawayosuke/korekarafalsehurontoendosekiyuritei "이제까지의 프런트엔드 보안 - Speaker Deck(일본어)")

----
<h1 class="site-genre">서비스, 사이트, 문서</h1>

----

## Integrate your data, APIs, and cloud services in minutes - Pipedream
[pipedream.com/](https://pipedream.com/ "Integrate your data, APIs, and cloud services in minutes - Pipedream")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">webservice</span> <span class="jser-tag">API</span></p>

Node.js에서 코드로 작성할 수 있는 IFTTT적인 웹 서비스입니다.
Slack이나 GitHub 등에서 이벤트를 전달 받아 코드로 처리하고 다른 서비스에 데이터를 보낼 수 있습니다.


----

## Metrics
[web.dev/metrics/](https://web.dev/metrics/ "Metrics")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">browser</span></p>

웹 사이트의 성능 지표에 대해서 소개 및 설명하는 사이트입니다.
FCP, LCP, FID, TTI, TBT, CLS에 관해 각각 설명하고 측정 방법과 개선 방법이 작성돼 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## NodeBB/NodeBB: Node.js based forum software built for the modern web
[github.com/NodeBB/NodeBB](https://github.com/NodeBB/NodeBB "NodeBB/NodeBB: Node.js based forum software built for the modern web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">BBS</span></p>

Node.js 버전 포럼 웹 애플리케이션 입니다.


----

## NeekSandhu/onigasm: Oniguruma regex library on the web using WebAssembly
[github.com/NeekSandhu/onigasm](https://github.com/NeekSandhu/onigasm "NeekSandhu/onigasm: Oniguruma regex library on the web using WebAssembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">library</span></p>

정규표현 엔진인 Oniguruma의 웹 어셈블리 버전입니다.


----
