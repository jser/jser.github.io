---
title: "2018-04-10のJS: PWA on iOS & Windows Store、dom-testing-library"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-04-10T01:35:23.636Z
category: JSer
tags:
- PWA
- iOS
- windows
- dom
- tests

---

JSer.info #378 - [Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7)에는 iOS 11.3/Safari 11.1에서 지원하는 Service Worker 등 소위 [Progressive Web Apps ](https://developers.google.com/web/progressive-web-apps/)(PWA)와 관련한 내용이 정리돼 있습니다.

홈 스크린 앱으로써의 구동, [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/)를 사용한 Service Worker 디버깅 방법에 관해 소개돼 있으며 iOS의 네이티브 앱과의 차이점이나 Android/Chrome의 PWA와이 차이점 등에 관해서도 작성돼 있습니다.

이어, [First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Centra](https://www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here)에서 Windows 10 Spring Creators Update(Windows 10 build 1803)의 프리뷰 버전의 Windows Store에 PWA 앱이 등록된 소식을 전하고 있습니다.

Windows Store와 PWA에 관한 내용은 아래 글을 참고해주세요.

- [Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/#0eVsoxrHYlso6vcS.97)

----

 DOM 요소를 테스트하기 위한 라이브러리 [kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.](https://github.com/kentcdodds/dom-testing-library)가 공개됐습니다.
테스트 시 자주 필요로 하는 특정 텍스트를 포함하는 요소를 선택하는 `getByText` 함수나 `data-testid` 속성을 기반으로 요소를 선택하는 `getByTestId` 함수 등을 제공하는 라이브러리입니다.

React 용 바인딩 라이브러리[react-testing-library
](https://github.com/kentcdodds/react-testing-library)도 제공하며 Vue 용으로 [vue-testing-library
](https://github.com/dfcook/vue-testing-library)가 준비돼 있습니다.

자세한 내용은 라이브러리 개발자가 직접 공개한 아래 글을 참고해주세요.

- [Introducing the react-testing-library 🐐 – kentcdodds](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65)

----

<h1 class="site-genre">헤드라인</h1>

----

## Axe 3.0 has arrived — here’s what you need to know - Deque
[www.deque.com/blog/axe-3-0-has-arrived/](https://www.deque.com/blog/axe-3-0-has-arrived/ "Axe 3.0 has arrived — here’s what you need to know - Deque")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">ReleaseNote</span></p>

Axe 3.0이 릴리스 됐습니다.
Shadow DOM을 지원합니다.

- [Release 3.0.0 · dequelabs/axe-core](https://github.com/dequelabs/axe-core/releases/tag/v3.0.0 "Release 3.0.0 · dequelabs/axe-core")

----

## First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Central
[www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here](https://www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here "First Windows 10 Progressive Web Apps (PWA) published by Microsoft hit the Store | Windows Central")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">PWA</span> <span class="jser-tag">news</span></p>

Microsoft Store에 PWA 애플리케이션이 공개됐습니다.

----

## sails/CHANGELOG.md at v1.0.0 · balderdashy/sails
[github.com/balderdashy/sails/blob/v1.0.0/CHANGELOG.md](https://github.com/balderdashy/sails/blob/v1.0.0/CHANGELOG.md "sails/CHANGELOG.md at v1.0.0 · balderdashy/sails")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js의 웹 애플리케이션 프레임워크 Sails.js 1.0이 릴리스 됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## React v16.3 changes - blog.koba04.com(일본어)
[blog.koba04.com/post/2018/04/04/react-v163-changes/](http://blog.koba04.com/post/2018/04/04/react-v163-changes/ "React v16.3 changes - blog.koba04.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16.3의 변경 사항에 대해 정리돼 있습니다.

----

## Lazy Loading Images and Video  |  Web Fundamentals  |  Google Developers
[developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/ "Lazy Loading Images and Video  |  Web Fundamentals  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span></p>

이미지나 영상을 지연 로드하는 방법에 관해 작성돼 있습니다.
Intersection Observer 또는 CSS를 사용한 이미지 지연 로드 방법을 각각 소개하며 영상과 GIF를 지연 로드하는 방법과 지연 로드를 보조하는 라이브러리, 로드에 실패했을 때의 Fallback 처리 등에 관해 작성돼 있습니다.

----

## Headless Chrome: an answer to server-side rendering JS sites  |  Tools for Web Developers  |  Google Developers
[developers.google.com/web/tools/puppeteer/articles/ssr](https://developers.google.com/web/tools/puppeteer/articles/ssr "Headless Chrome: an answer to server-side rendering JS sites  |  Tools for Web Developers  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">server</span> <span class="jser-tag">article</span></p>

Headless Chrome을 사용해 서버 사이드 렌더링을 구현하는 튜토리얼입니다. 구현하는 방법 뿐 아니라 최적화 방법에 대해서도 정리돼 있습니다.

----

## GoDaddy Open Source Center - Isomorphic Asset System for React and React-Native
[godaddy.github.io/2018/04/04/isomorphic-asset-system-for-react-and-react-native/](https://godaddy.github.io/2018/04/04/isomorphic-asset-system-for-react-and-react-native/ "GoDaddy Open Source Center - Isomorphic Asset System for React and React-Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">SVG</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

SVG 파일(에셋)을 관리하는 도구로 React/React Native 컴포넌트, webpack loader 와의 연계에 대해 정리돼 있습니다.

----

## Strategies for Service Worker Caching for Progressive Web Apps
[blog.hasura.io/strategies-for-service-worker-caching-d66f3c828433](https://blog.hasura.io/strategies-for-service-worker-caching-d66f3c828433 "Strategies for Service Worker Caching for Progressive Web Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Service Worker의 캐시 구조 및 캐시와 관련한 문제에 대해 작성돼 있습니다.
문제가 있는(망가진) 배포 버전 패치 문제, `service-worker.js` 파일 자체를 캐시할 때의 문제, 캐시될 필요 없는 응답에 대한 조작 등을 소개하며 `create-react-app`의 사례와 `Clear-Site-Data` 헤더에 대해서도 이야기합니다.

----

## Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium
[medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7 "Progressive Web Apps on iOS are here 🚀 – Maximiliano Firtman – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ios</span> <span class="jser-tag">safari</span> <span class="jser-tag">article</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">PWA</span></p>

iOS 11.3에서 지원하는 Service Worker 등 PWA와 관련된 기능에 대해 작성돼 있습니다.
네이티브 앱과 비교했을 때의 제약과 Chrome/Android 와의 차이점에 대해 이야기합니다.

----

## Transform your codebase using codemods | nec.is
[nec.is/writing/transform-your-codebase-using-codemods/](https://nec.is/writing/transform-your-codebase-using-codemods/ "Transform your codebase using codemods | nec.is")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">AST</span></p>

jscodeshift를 사용한 JavaScript 코드 변환에 대해 소개합니다.
JavaScript 코드를 다루는 방법과 AST 그리고 jscodeshift의 API에 관해 작성돼 있습니다.

----

## Introducing the Payment Request API for Apple Pay | WebKit
[webkit.org/blog/8182/introducing-the-payment-request-api-for-apple-pay/](https://webkit.org/blog/8182/introducing-the-payment-request-api-for-apple-pay/ "Introducing the Payment Request API for Apple Pay | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 11.1에서 Payment Request API로 Apple Pay를 이용하는 방법에 대해 소개합니다.
`-webkit-appearance: -apple-pay-button;"` 스타일을 지정하여 Appley Pay 버튼을 표현하는 방법과 Payment Request API를 사용하는 방법에 관해 작성돼 있습니다.

----

## Understanding JavaScript Proxies by Examining on-change Library
[codeburst.io/understanding-javascript-proxies-by-examining-on-change-library-f252eddf76c2](https://codeburst.io/understanding-javascript-proxies-by-examining-on-change-library-f252eddf76c2 "Understanding JavaScript Proxies by Examining on-change Library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">proxy</span> <span class="jser-tag">article</span></p>

속성 변경 감지를 ES Proxy로 구현해보면서 Proxy에 대해 이해할 수 있는 글입니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Browser Automated Tests // Speaker Deck
[speakerdeck.com/derekb/browser-automated-tests](https://speakerdeck.com/derekb/browser-automated-tests "Browser Automated Tests // Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">slide</span></p>

puppeteer와 mocha를 사용한 자동 테스트 환경을 소개하는 슬라이드립니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## React lifecycle methods diagram
[projects.wojtekmaj.pl/react-lifecycle-methods-diagram/](http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/ "React lifecycle methods diagram")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span></p>

React 16.3 이후 환경의 React 라이프 사이클을 정리한 다이어그램.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.
[github.com/kentcdodds/dom-testing-library](https://github.com/kentcdodds/dom-testing-library "kentcdodds/dom-testing-library: 🐙 Simple and complete DOM testing utilities that encourage good testing practices.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

DOM 요소를 테스트하는 Matcher 라이브러리입니다.

- [Introducing the react-testing-library 🐐 – kentcdodds](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65 "Introducing the react-testing-library 🐐 – kentcdodds")

----

## kwolfy/webworker-promise: Promise based wrapper for webworkers
[github.com/kwolfy/webworker-promise](https://github.com/kwolfy/webworker-promise "kwolfy/webworker-promise: Promise based wrapper for webworkers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span></p>

WebWorker를 Promise 기반으로 다룰 수 있는 라이브러리입니다.
EventEmitter와 같은 이벤트 구조와 Promise를 사용한 비동기 처리, Worker pool 구조를 지원합니다.

----

## avwo/whistle: HTTP, HTTPS, WebSocket debugging proxy
[github.com/avwo/whistle](https://github.com/avwo/whistle "avwo/whistle: HTTP, HTTPS, WebSocket debugging proxy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">proxy</span> <span class="jser-tag">debug</span> <span class="jser-tag">node.js</span></p>

Node.js로 작성된 HTTP/HTTPS/WebSockets 디버깅 Proxy 라이브러리입니다.

----
