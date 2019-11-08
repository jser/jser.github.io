---
title: "2019-10-15: webpack 5β, Next.js(create-next-app), Same-Site Cookies"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-10-15T00:48:55.247Z
category: JSer
tags:
- webpack
- Next.js
- Cookie

---

JSer.info #457 - webpack 5β가 릴리스되어 베타 피드백을 받는 이슈가 함께 생성됐습니다.

- [webpack 5 beta feedback · Issue #9802 · webpack/webpack](https://github.com/webpack/webpack/issues/9802)
- [changelog-v5/README.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/README.md)

webpack 5β의 비호환적 변경사항으로 Node.js 코어 모듈 자동 폴리필(automatic Node.js polyfills)을 삭제했고 장기적(long term) 캐시를 위해서 Chunk와 Module Id 해쉬 알고리즘을 변경했습니다. 또, 몇 가지 옵션명이 변경됐습니다. 

그 외 기능적인 측면으로 파일 시스템 캐시 설정 추가, Tree Shaking 개선, `output.ecmaVersion` 옵션이 추가됐습니다.
또 실험적 기능으로서 `asset` module type이 추가됐고 Top Level `await`를 지원합니다.

4.x에서 5.x로의 마이그레이션 가이드도 함께 공개됐습니다.

- [changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/MIGRATION%20GUIDE.md)

베타 피드벡 이슈에서는 버그나 성능 회귀(performance regression), Breaking Change에 대한 의견을 모집하고 있습니다.

----

Next.js 9.1.0이 릴리스됐습니다.

- [Blog - Next.js 9.1 | Next.js](https://nextjs.org/blog/next-9-1)
- [Release v9.1.0 · zeit/next.js](https://github.com/zeit/next.js/releases/tag/v9.1.0)

Next.js 9.1.0에서는 `src/pages` 디렉터리 지원하며 `public/` 디렉터리를 이용해 정적 파일의 루트 서빙을 할 수 있게 됐습니다. 따라서 기존과 같이 `static/`을 사용하면 비권장 메시지가 출력됩니다.
또, 다음과 같은 실험적 기능이 플래그가 붙어 구현됐습니다.

- Built-in CSS Support
- Static Error Pages
- Module / Nomodule 출력

이 외로 지금까지 커뮤니티에서 관리하던 `create-next-app`를 공식적으로 이관했습니다.
[공식 예제](https://github.com/zeit/next.js/tree/canary/examples) 문서도 `create-next-app`을 사용하는 형태로 변경되는 것 같습니다.

- [Blog - Introducing Create Next App | Next.js](https://nextjs.org/blog/create-next-app)

----

[Same-Site Cookies By Default | text/plain](https://textslashplain.com/2019/09/30/same-site-cookies-by-default/)에는 Same-Site Cookie에 대해서 자세히 소개돼 있습니다.

Chrome 80에서 Cookie 기본 정책을 `SameSite=Lax`로 변경할 예정이라는 소식과 함께 Same-Site Cookies의 목적과 실제 영향에 대해서 이야기 합니다.
CSRF 공격으로부터 방어적으로 도움이 되는 부분과 Cookie의 HTTPOnly 속성과 Secure 속성에 대해서도 작성돼 있습니다.
또 Same-Site가 기본이 돼 있을 경우 발생할 수 있는 영향과 다른 브라우저의 대응 현황에 대해서도 소개합니다. 

Same-Site Cookies는 `SameSite=None`이라고 설정하는 것으로 기능을 끌 수 있으나 [Safari 12에서 `SameSite=None`을 `SameSite=Strict`](https://bugs.webkit.org/show_bug.cgi?id=198181)으로 취급하는 버그가 있다는 사실과 디버깅하는 방법을 소개하는 등 이를 다룰때 발생할 수 있는 문제에 대해서도 언급합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## The new evergreen Bingbot simplifying SEO by leveraging Microsoft Edge | Webmaster Blog
[blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge](https://blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge "The new evergreen Bingbot simplifying SEO by leveraging Microsoft Edge | Webmaster Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">SEO</span> <span class="jser-tag">news</span></p>

Bing 엔진으로 Chromium 기반의 MSEdge 채용했다는 소식입니다.
크롤링하는 Bingbot은 이제 Chrome과 상응하며 정기적으로 최신 안정버전으로 갱신됩니다.


----

## Release v9.1.0 · zeit/next.js
[github.com/zeit/next.js/releases/tag/v9.1.0](https://github.com/zeit/next.js/releases/tag/v9.1.0 "Release v9.1.0 · zeit/next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 9.1.0이 릴리스됐습니다.
`src/pages` 디렉터리를 지원하고 `public/` 디렉터리를 이용해 정적 파일의 루트 서빙을 할 수 있게 됐습니다.


----

## webpack 5 beta feedback · Issue #9802 · webpack/webpack
[github.com/webpack/webpack/issues/9802](https://github.com/webpack/webpack/issues/9802 "webpack 5 beta feedback · Issue #9802 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5β가 릴리스됐습니다.
Node.js 코어 모듈 자동 폴리필(automatic Node.js polyfills)을 삭제했고 장기적(long term) 캐시를 위해서 Chunk와 Module Id 해쉬 알고리즘과 몇 가지 옵션명이 변경됐습니다.
파일 시스템 캐시 설정 추가, Tree Shaking 개선, `output.ecmaVersion` 옵션이 추가됐습니다.
또 실험적 기능으로서 `asset` module type이 추가됐고 Top Level `await`를 지원합니다.

- [changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/MIGRATION%20GUIDE.md "changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5")
- [changelog-v5/README.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/README.md "changelog-v5/README.md at master · webpack/changelog-v5")

----

## Node v12.12.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.12.0/](https://nodejs.org/en/blog/release/v12.12.0/ "Node v12.12.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.12.0이 릴리스됐습니다.
`fs.opendir()`, `fs.Dir`이 추가됐고 `--enable-source-maps`로 스택 트레이스 Source Map을 지원합니다.


----

## Blog - Introducing Create Next App | Next.js
[nextjs.org/blog/create-next-app](https://nextjs.org/blog/create-next-app "Blog - Introducing Create Next App | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

`create-next-app`가 Next.js의 공식 프로젝트로 이관됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## Top-level await · V8
[v8.dev/features/top-level-await](https://v8.dev/features/top-level-await "Top-level await · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Top-level `await`을 주제로 한 글입니다.
Top-level `await`의 유스케이스와 실행 순서 등 동작과 관련한 내용이 정리돼 있습니다.


----

## Same-Site Cookies By Default | text/plain
[textslashplain.com/2019/09/30/same-site-cookies-by-default/](https://textslashplain.com/2019/09/30/same-site-cookies-by-default/ "Same-Site Cookies By Default | text/plain")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Chrome 80에서 기본 정책으로 적용되는 SameSite=Lax에 대해서 이야기합니다.
Cookie의 Security와 Privacy 문제, Same-Site Cookies의 목적, CSRF 공격으로부터의 보호, HTTPOnly 속성과 Secure 속성에 대해서 작성돼 있습니다.
또, Same-Site가 기본 적용될 경우 실제 영향과 다른 브라우저의 대응 현황에 대해서도 소개하며 2분 완화(two minute mitigation) 전략에 대해서도 이야기합니다.


----

## What's new in Chrome 78 - LogRocket Blog
[blog.logrocket.com/whats-new-in-chrome-78/](https://blog.logrocket.com/whats-new-in-chrome-78/ "What's new in Chrome 78 - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 78의 변경 사항이 정리돼 있습니다.
CSS opacity의 `%`, Proposal의 Optional Chaining, `unload` 시의 제한, User Timing Lv3, WebSocketStream 등을 지원합니다.
Origin Trial로써 지원되는 Native File System API와 SMS Receiver API도 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Vue.js Performance Tips / #v\_kansai 11 - Speaker Deck(일본어)
[speakerdeck.com/masashi/number-v-kansai-11](https://speakerdeck.com/masashi/number-v-kansai-11 "Vue.js Performance Tips / #v\_kansai 11 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

Vue.js 애플리케이션의 성능 개선을 주제로 한 슬라이드입니다.
IntersectionObserver를 사용해 표시가 제대로 이뤄지는지 감지하는 방법과 이미지 지연 로드, Hydration의 지연 실행 등에 대해서 이야기합니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## lirantal/is-website-vulnerable: finds publicly known security vulnerabilities in a website's frontend JavaScript libraries
[github.com/lirantal/is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable "lirantal/is-website-vulnerable: finds publicly known security vulnerabilities in a website's frontend JavaScript libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">Tools</span></p>

지정한 URL에서 취약성이 있는 라이브러리를 사용하고 있는지 검사하는 도구입니다.
Synx를 기반으로 취약성을 판정합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## leeoniya/uPlot: An exceptionally fast, tiny time series chart
[github.com/leeoniya/uPlot](https://github.com/leeoniya/uPlot "leeoniya/uPlot: An exceptionally fast, tiny time series chart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">chart</span> <span class="jser-tag">library</span></p>

파일 크기가 작은 시 계열 그래프 라이브러리입니다.


----

## devforth/painterro: Painterro - JavaScript painting plugin
[github.com/devforth/painterro](https://github.com/devforth/painterro "devforth/painterro: Painterro - JavaScript painting plugin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Image</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

간단한 이미지 편집 라이브러리입니다.


----

## luwes/sinuous: Small, fast, reactive UI library
[github.com/luwes/sinuous](https://github.com/luwes/sinuous "luwes/sinuous: Small, fast, reactive UI library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">jsx</span></p>

`htm` 문법, Hyperscript, JSX에 대응한 UI 라이브러리입니다.
observable한 값 감시 시스템을 제공하며 작은 파일 크기로 UI를 만들 수 있도록 하는 것에 목적을 두고 있습니다.

- [developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.](https://github.com/developit/htm "developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.")

----
