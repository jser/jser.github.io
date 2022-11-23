---
title: "2022-11-22:  State of JavaScript 2022 앙케이트 실시중, RegExp `v` flag"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2022-11-22T00:42:43.228Z
category: JSer
tags:
- React
- tutorial
- CSS
- TypeScript
- browser

---

JSer.info #619 - 매년 행해지고 있는 JavaScript 개발자 앙케이트 State of JavaScript 2022가 개최되었다.

- [State of JavaScript 2022](https://survey.devographics.com/survey/state-of-js/2022)

언어 기능이나 프레임워크 등에 대해 2022년 12월 15일까지 앙케이트를 받는다.

과거 결과는 다음 페이지에 공개되어있다.

- [The State of JS 2021](https://2021.stateofjs.com/en-US/)
- [State of JS 2020](https://2020.stateofjs.com/en-US/)


---

[ECMAScript proposal: RegExp flag `/v` makes character classes and character class escapes more powerful](https://2ality.com/2022/11/regexp-v-flag.html)에서는 현재 ECMAScript Proposal Stage 3에 있는 [RegExp `v` flag](https://github.com/tc39/proposal-regexp-v-flag)에 대해 해설합니다.

정규표현 `v` 플러그는 정규표현에 집합조작과 구문을 추가하는 Proposal입니다.
글에서는 `v` 플러그를 이용할 때 문자 클래스와 Unicode Property Escape, 문자 클래스의 집합조작, case-insensitive 매치 개선에 대해 해설합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## AWS AppSync GraphQL APIs Supports JavaScript Resolvers | AWS News Blog
[aws.amazon.com/jp/blogs/aws/aws-appsync-graphql-apis-supports-javascript-resolvers/](https://aws.amazon.com/jp/blogs/aws/aws-appsync-graphql-apis-supports-javascript-resolvers/ "AWS AppSync GraphQL APIs Supports JavaScript Resolvers | AWS News Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

AWS AppSync GraphQL APIs의 Resolver로 VTL를 더한 JavaScript이 이용 가능.

----

## Release v1.28 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.28.0](https://github.com/microsoft/playwright/releases/tag/v1.28.0 "Release v1.28 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.28.0 출시.
VSCode에서 테스트 코드 생성을 보조하는 Playwright Tools 추가, `test.describe.configure` API 추가 등


----

## Release v7.17.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v7.17.0](https://github.com/pnpm/pnpm/releases/tag/v7.17.0 "Release v7.17.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v7.17.0 출시.
`pnpm licenses list` 커맨드 추가 등


----

## State of JavaScript 2022
[survey.devographics.com/survey/state-of-js/2022](https://survey.devographics.com/survey/state-of-js/2022 "State of JavaScript 2022")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span> <span class="jser-tag">news</span></p>

2022년 12월 15일까지, JavaScript 개발자의 앙케이트를 받는다.

----
<h1 class="site-genre">읽을거리</h1>

----

## The magical world of Particles with React Three Fiber and Shaders - Maxime Heckel&#039;s Blog
[blog.maximeheckel.com/posts/the-magical-world-of-particles-with-react-three-fiber-and-shaders/](https://blog.maximeheckel.com/posts/the-magical-world-of-particles-with-react-three-fiber-and-shaders/ "The magical world of Particles with React Three Fiber and Shaders - Maxime Heckel&#039;s Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

React Three Fiber를 이용한 파티클 렌더링 튜토리얼


- [The Study of Shaders with React Three Fiber - Maxime Heckel&#039;s Blog](https://blog.maximeheckel.com/posts/the-study-of-shaders-with-react-three-fiber/ "The Study of Shaders with React Three Fiber - Maxime Heckel&amp;#039;s Blog")

----

## ECMAScript proposal: RegExp flag \`/v\` makes character classes and character class escapes more powerful
[2ality.com/2022/11/regexp-v-flag.html](https://2ality.com/2022/11/regexp-v-flag.html "ECMAScript proposal: RegExp flag \`/v\` makes character classes and character class escapes more powerful")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3 RegExp의 `v` 플러그에 대한 해설.
문자클래스와 Unicode Property Escape, 문자클래스 집합조작, case-insensitive 매치 개선에 대하여


----

## 코드 점프 가능한 CSS Modules 실현하는 happy-css-modules 소개 - mizdra&#039;s blog
[www.mizdra.net/entry/2022/11/14/102506](https://www.mizdra.net/entry/2022/11/14/102506 "코드 점프 가능한 CSS Modules 실현하는 happy-css-modules 소개 - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Typed CSS Modules와 코드점프 문제 관련.
TypeScript Declaration Map를 사용해, 자료형 정의 파일이 아니라, 소스코드인 CSS 그 자체로 점프하도록 구현


----

## Manifest v3 signing available November 21 on Firefox Nightly | Mozilla Add-ons Community Blog
[blog.mozilla.org/addons/2022/11/17/manifest-v3-signing-available-november-21-on-firefox-nightly/](https://blog.mozilla.org/addons/2022/11/17/manifest-v3-signing-available-november-21-on-firefox-nightly/ "Manifest v3 signing available November 21 on Firefox Nightly | Mozilla Add-ons Community Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span></p>

2022년 11월 21일부터 Firefox 확장기능 스토어 AMO에 Manifest V3 확장을 업로드하고 서명할 수 있게 함


----

## Automate an isolated browser instance with just a few lines of code
[blog.cloudflare.com/introducing-workers-browser-rendering-api/](https://blog.cloudflare.com/introducing-workers-browser-rendering-api/ "Automate an isolated browser instance with just a few lines of code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">puppeteer</span> <span class="jser-tag">article</span></p>

Cloudflare Workers에서 Puppeteer를 이용할 수 있는 Rendering API를 도입 예정.
gVisor로 관리되어 온 Browser Rendering를 샌드박스 내에서 렌더링하고 결과를 얻을 수 있다.


----

## Expiration Cap Removed From JavaScript Cookies In WebKit Browsers | Simo Ahava&#039;s blog
[www.simoahava.com/privacy/first-party-cookies-webkit-revisited/](https://www.simoahava.com/privacy/first-party-cookies-webkit-revisited/ "Expiration Cap Removed From JavaScript Cookies In WebKit Browsers | Simo Ahava&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">safari</span> <span class="jser-tag">privacy</span></p>

Safari Cookie 유효기간 관련.
브라우저 이용한 날에 7일간 사용하지 않는다면 삭제, ITP에서 트래킹 분류된 경우에는 24시간 후 삭제, CNAME Cloaking 이라면 7일간 제한 등


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 메타 프론트엔드 개발자 프로페셔널 인증서 | Coursera
[www.coursera.org/professional-certificates/meta-front-end-developer](https://www.coursera.org/professional-certificates/meta-front-end-developer "메타프론트엔드개발자 프로페셔널 인증서 | Coursera")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">video</span></p>

Meta의 프론트엔드 개발자 입문을 위한 coursera 강좌.
HTML/CSS/JavaSciprt, React, UI/UX 등을 배울 수 있는 강좌이다.


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Permissions-Policy Research - Google 문서
[docs.google.com/document/d/14xHANU3n43PfJR\_dCpEwVCiVYv12BAfGqOICNvd79R4/edit#](https://docs.google.com/document/d/14xHANU3n43PfJR_dCpEwVCiVYv12BAfGqOICNvd79R4/edit# "Permissions-Policy Research - Google 문서")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">spec</span> <span class="jser-tag">document</span></p>

Feature-Policy와 Permissions-Policy 대응이나 표준화등에 대해 조사 문서
MDN 문서를 위해 조사되었다.

- [Intent to document: Permissions-Policy · Issue #22347 · mdn/content](https://github.com/mdn/content/issues/22347 "Intent to document: Permissions-Policy · Issue #22347 · mdn/content")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## hadmean/hadmean: Generate powerful, fully functional, ready-to-be-deployed admin apps in seconds with just \`npx hadmean\`. No Javascript, no SQL, no components, no tutorials, and finally zero maintenance. Stop building and maintaining admin apps that you can auto-generate.
[github.com/hadmean/hadmean](https://github.com/hadmean/hadmean "hadmean/hadmean: Generate powerful, fully functional, ready-to-be-deployed admin apps in seconds with just \`npx hadmean\`. No Javascript, no SQL, no components, no tutorials, and finally zero maintenance. Stop building and maintaining admin apps that you can auto-generate.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

데이터베이스의 데이터를 보는 관리 화면을 만드는 제네레이터 애플리케이션


----
<h1 class="site-genre">도서</h1>

----

## JavaScript와 비교하며 배우는 TypeScript | Techpit
[www.techpit.jp/courses/248](https://www.techpit.jp/courses/248 "JavaScript와 비교하며 배우는 TypeScript | Techpit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

JavaScript에 자료형을 붙이며 TypeScript에 대해 배우는 도서

- [\[Techpit\] JavaScript와 비교하며 배우는 TypeScript를 출간했습니다!](https://zenn.dev/ababup1192/articles/6873aa4b4109f2 "\[Techpit\] JavaScript와 비교하며 배우는 TypeScript를 출간했습니다!")

----
