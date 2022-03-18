---
title: "2021-05-25: IE 자체 앱으로서 지원 종료, WebContainers, User-Agent Client Hints"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-05-25T02:50:27.271Z
category: JSer
tags:
- node.js
- Chrome
- Tools
- CSS
- React

---

JSer.info #541 - Windows 10에서 Internet Explorer(IE) 단일 앱으로서의 지원을 2022년 6월 15일로 종료한다고 발표.

- [The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/)
- [Internet Explorer는 Microsoft Edge로 – Windows 10의 Internet Explorer 11 데스크탑 앱은 2022년 6월 15일에 지원 종료 - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/)(일본어)
- [「Internet Explorer 11 데스크탑 앱 지원 종료」 발표와 관련한 FAQ - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/internet-explorer-11-desktop-app-retirement-faq/)(일본어)

2022년 6월 15일 이후로 IE 데스크탑 애플리케이션 (`iexplore.exe`)를 사용하려고 하면 Microsoft Edge(MSEdge)가 대신 실행된다.
MSEdge에는 IE 모드가 탑재돼 있고, MSEdge의 설정을 변경하여 IE의 렌더링 엔진인MSHTML(Trident)를 사용할 수 있다.

- [Microsoft Edge의 Internet Explorer 모드 - Office 지원](https://support.microsoft.com/ja-jp/office/microsoft-edge-%e3%81%ae-internet-explorer-%e3%83%a2%e3%83%bc%e3%83%89-6604162f-e38a-48b2-acd2-682dbac6f0de?ui=ja-JP&rs=ja-JP&ad=JP)(일본어)

또, 이 IE 모드에서는 MSEdge의 F12 개발자 도구와 연동되지 않으며 디버깅이 필요할 시 `IEChooser.exe`를 대신 사용해야 한다.

- [IE 모드와 관련된 자주있는 질문 | Japan Developer Support Internet Team Blog](https://jpdsi.github.io/blog/internet-explorer-microsoft-edge/ie-mode-faq/)(일본어)

이 IE 모드(MSHTML) 자체는 발표 내용과 상관없이 2029년 까지 지원할 예정이다.

---

브라우저 상에서 Node.js의 런타임을 실행하는 구조 WebContainers가 stackblitz에서 공개됐다.

- [Introducing WebContainers: Run Node.js natively in your browser](https://blog.stackblitz.com/posts/introducing-webcontainers/)

Node.js 런타임을 브라우저에서 실행하며 브라우저 자체를 샌드박스로 활용 Node.js 코드를 안전하게 실행할 수 있는 구조를 제공한다. 어디까지나 브라우저 내에서 실행되는 시스템으로 네이티브 애드온을 지원하지 않으며 CORS 등 브라우저 제약 하에 동작한다.

[stackblitz/webcontainer-core](https://github.com/stackblitz/webcontainer-core)에 키 콘셉트가 소개돼 있다.
Virtual FS와 Networking을 구현하고 각 프로세스를 Worker로 실행, 메시징하여 멀티 쓰레드를 지원한다. POSIX를 따른 쉘로 jsh라는 구현과 npm/yarn 클라이언트로 turbo라는 구현을 갖고 있다.

현재는 오픈소스가 아니지만 장래에 [코어 부분은 오픈소스로 공개](https://news.ycombinator.com/item?id=27225150)할 예정이라고 한다.

---

Chrome에서 UA 문자열을 다루는 `navigator.userAgent`, `navigator.appVersion`, `navigator.platform`을 비권장하는 로드맵이 구체화 되고 있다.

- [Chromium Blog: Update on User-Agent String Reduction in Chrome](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html)

Chrome 92에서 사용시 비권장 경고를 노출하며 단계적으로 UA 문자열에서 정보를 삭제하고 UA 문자열을 고정 시키는 과정을 담은 로드맵 공개 됐다.

`navigator.userAgent` 대체할 구조로 UA Client Hints가 있으며, 로드맵과 함께 UA Client Hints으로 이전하는 방법을 소개하는 글도 함께 공개 됐다.

- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)
- [GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.](https://github.com/GoogleChromeLabs/uach-retrofill)


----

<h1 class="site-genre">헤드라인</h1>

----

## Recoil 0.3.0 | Recoil
[recoiljs.org/blog/2021/05/14/0.3.0-released/](https://recoiljs.org/blog/2021/05/14/0.3.0-released/ "Recoil 0.3.0 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.3.0 릴리스.
RecoilRoot에 `override` 옵션 추가, selector에 `GetCallback` 추가.
다음 0.4에서 `snapshot.retain()` 하지 않고 snapshot을 사용하면 예외가 발생하게 된다.


----

## The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog
[blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/](https://blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/ "The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">news</span> <span class="jser-tag">MSEdge</span></p>

IE11의 데스크탑 앱으로서 지원은 2022년 6월 15일에 종료되며 MSEdge의 IE 모드로 전환. IE 모드는 2029년 까지 지원할 예정.

- [Internet Explorer는 Microsoft Edge로 – Windows 10의 Internet Explorer 11 데스크탑 앱은 2022년 6월 15일에 지원 종료 - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/ "Internet Explorer는 Microsoft Edge로 – Windows 10의 Internet Explorer 11 데스크탑 앱은 2022년 6월 15일에 지원 종료 - Windows Blog for Japan")(일본어)
- [「Internet Explorer 11 데스크탑 앱 지원 종료」 발표와 관련된 FAQ - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/internet-explorer-11-desktop-app-retirement-faq/ "「Internet Explorer 11 데스크탑 앱 지원 종료」 발표와 관련된 FAQ - Windows Blog for Japan")(일본어)

----

## Release v7.5.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v7.5.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v7.5.0 "Release v7.5.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 7.5.0 릴리스.
Source Map 기반의 파일 트리를 보여주는 트리맵 기능 추가, 새로운 CLS 대응 추가.


----

## Node v16.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.2.0/](https://nodejs.org/en/blog/release/v16.2.0/ "Node v16.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.2.0 릴리스.
`import.meta.resolve`에서 `URL` 객체 지원, Worker가 작성됐을 때 트리가 되는 `worker` 이벤트를 `process`에 추가.


----


## Release v10.0.0 · TypeStrong/ts-node
[github.com/TypeStrong/ts-node/releases/tag/v10.0.0](https://github.com/TypeStrong/ts-node/releases/tag/v10.0.0 "Release v10.0.0 · TypeStrong/ts-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 컴파일을 Runtime 시에 실행하는 ts-node 10.0.0 릴리스.
`--script-mode` 동작을 기본으로 활성화하고 오래된 동작을 재현하는 `--cwd-mode` 추가.
Node.js 10 지원 종료, `--show-config` 추가, `--transpiler` 옵션으로 SWC를 사용한 trasnpile에 대응.
또, 웹 사이트가 개편됐다.

- [Third-party transpilers | ts-node](https://typestrong.org/ts-node/docs/transpilers/ "Third-party transpilers | ts-node")
- [ts-node | ts-node](https://typestrong.org/ts-node/ "ts-node | ts-node")

----
<h1 class="site-genre">아티클</h1>

----

## Chromium Blog: Update on User-Agent String Reduction in Chrome
[blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html "Chromium Blog: Update on User-Agent String Reduction in Chrome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome의 User-Agent를 고정해 나갈 과정을 담은 로드맵. 
Chrome 92에서 `navigator.userAgent` 등 비권장화, reduced UA string을 옵트인으로 도입하고 활성화하는 등 7 단계로 이뤄진 마이그레이션 전략에 대해.

- [User-Agent Reduction - The Chromium Projects](https://www.chromium.org/updates/ua-reduction "User-Agent Reduction - The Chromium Projects")

----

## Introducing Firefox&#039;s new Site Isolation Security Architecture - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/](https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/ "Introducing Firefox&#039;s new Site Isolation Security Architecture - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Firefox의 Site Isolation 아키텍처를 소개하는 글.
eTLD 기반의 Site 별로 프로세스를 나눠 메모리를 서로 분리한 상태에서 리소스를 불러오는 것으로 Spectre 등의 사이드 채널 공격을 방지.
또, 서브 프레임도 탑 레벨이 다른 사이트라면 별도 프로세스로 읽어 들이도록 돼 있다.


----

## The Humble &lt;img&gt; Element And Core Web Vitals — Smashing Magazine
[www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/](https://www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/ "The Humble &lt;img&gt; Element And Core Web Vitals — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Image</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`<img>` 관련한 LCP, CLS, FID 지표 최적화 방법 가이드.


----

## Introducing WebContainers: Run Node.js natively in your browser
[blog.stackblitz.com/posts/introducing-webcontainers/](https://blog.stackblitz.com/posts/introducing-webcontainers/ "Introducing WebContainers: Run Node.js natively in your browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">browser</span> <span class="jser-tag">webworker</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

Node.js를 브라우저에서 동작시키는 WebContainers 소개.
Node.js 런타임을 브라우저에서 실행하며 브라우저 자체를 샌드박스로 활용. Node.js 코드를 안전하게 실행하기 위한 구조 소개.
Virtual FS와 Networking를 구현하고 각 프로세스를 Worker로 실행, 메시징하여 멀티 스레드를 지원한다.
POSIX를 따르는 jsh라는 구현과 npm/yarn 클라이언트로 turbo라는 구현을 갖고 있다.

- [stackblitz/webcontainer-core](https://github.com/stackblitz/webcontainer-core "stackblitz/webcontainer-core")
- [AngularAir - StackBlitz with Eric Simons and Dominic Elm - YouTube](https://www.youtube.com/watch?v=5F9qH-ea5Qk "AngularAir - StackBlitz with Eric Simons and Dominic Elm - YouTube")

----

## Migrate to User-Agent Client Hints
[web.dev/migrate-to-ua-ch/](https://web.dev/migrate-to-ua-ch/ "Migrate to User-Agent Client Hints")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">privacy</span></p>

`navigator.userAgent` 등이 비권장되며 이후 고정되기 때문에 해당 속성 대신 사용할 수 있는 User-Agent Client Hints를 소개.
JavaScript API로 사용할 수 있는 `navigator.userAgentData`와 `navigator.userAgentData.getHighEntropyValues`.
HTTP 헤더 UA Client Hint를 다루는 `Accept-CH`와 `Sec-CH-UA-*` 설명.
또, Client Hint에서 레거시 UA 문자열을 만들어주는 라이브러리도 소개.

- [Chromium Blog: Update on User-Agent String Reduction in Chrome](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html "Chromium Blog: Update on User-Agent String Reduction in Chrome")
- [GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.](https://github.com/GoogleChromeLabs/uach-retrofill "GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.")

----

## Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium
[nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8](https://nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8 "Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 네이티브 애드온 용 API 이름을 N-API에서 Node-API로 변경.
변경하게 된 계기에 대해서 이야기한다.

- [Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium](https://nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8 "Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## 오리지널 JavaScript 라이브러리 공개하기(일본어)
[zenn.dev/yusuke99/books/fcd96342f5cb1b468799](https://zenn.dev/yusuke99/books/fcd96342f5cb1b468799 "오리지널 JavaScript 라이브러리 공개하기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">tutorial</span></p>

JavaScript 라이브러리를 npm에 공개하는 과정을 담은 튜토리얼.
라이브러리 구현과 테스트, npm에 공개, Githun 액션을 이용한 CI를 통한 배포, Scoped Packages 등.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## argyleink/transition.css: Drop-in CSS transitions
[github.com/argyleink/transition.css](https://github.com/argyleink/transition.css "argyleink/transition.css: Drop-in CSS transitions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

여러가지 CSS transition을 모아놓은 CSS 라이브러리.


----


## DOM Events
[domevents.dev/](https://domevents.dev/ "DOM Events")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">event</span> <span class="jser-tag">Tools</span></p>

DOM 이벤트의 흐름을 Bubbling, Capture, Passive 등의 옵션별로 어떻게 동작하는지 시각적으로 살펴볼 수 있는 도구. 


----

## rtk-incubator/rtk-query: Experimental data fetching and caching addon for Redux Toolkit
[github.com/rtk-incubator/rtk-query](https://github.com/rtk-incubator/rtk-query "rtk-incubator/rtk-query: Experimental data fetching and caching addon for Redux Toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span></p>

Redux Toolkit 기반의 데이터 취득과 상태를 관리할 수 있는 Query 라이브러리.
선언적 API 정의, 데이터 취득, 캐시 및 재시도, Prefetching, React Hooks, Open API를 통한 자동 생성 등을 지원한다.
향후 Redux Toolkit에 포함되는 것을 목표로 하고 있다.


----

## ngneat/variabless: JS &amp; CSS - A Match Made in Heaven 💎
[github.com/ngneat/variabless](https://github.com/ngneat/variabless "ngneat/variabless: JS &amp; CSS - A Match Made in Heaven 💎")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

JavaScript에서 CSS Variables 정의를 포함한 CSS를 생성하는 도구.


----

## Web worker meets worker threads - threads.js
[threads.js.org/](https://threads.js.org/ "Web worker meets worker threads - threads.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">webworker</span></p>

브라우저의 Web Worker와 Node.js의 `worker_threads`를 사용한 Worker 관리 라이브러리.
async function와 Observables 대응, thread pools, webpack 용 plugin을 제공한다.


----
