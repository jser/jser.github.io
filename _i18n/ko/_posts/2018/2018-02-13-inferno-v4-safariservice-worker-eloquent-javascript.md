---
title: "2018-02-13 JS: Inferno v4, Safari의 Service Worker, Eloquent JavaScript 제3판"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-02-13T02:04:48.927Z
category: JSer
tags:
- React
- inferno
- Safari
- book

---

JSer.info #370 - React 스러운 API를 갖고 있는 Inferno v4가 릴리스 됐습니다.

- [Release Inferno v4 · infernojs/inferno](https://github.com/infernojs/inferno/releases/tag/v4.0.2 "Release Inferno v4 · infernojs/inferno")

`Inferno.createPortal`이 추가됐으며 [inferno-router](https://github.com/infernojs/inferno/tree/master/packages/inferno-router "inferno-router")가 React Router v4와 같도록 수정됐습니다. 또, 최신 버전의 Mobx, Redux와 연계가 가능하도록 갱신됐습니다.
비호환적인 모듈 인터페이스 변경이 있으니 자세한 내용은 아래 마이그레이션 가이드를 확인하시길 바랍니다.

- [inferno/v4-migration.md at master · infernojs/inferno](https://github.com/infernojs/inferno/blob/master/docs/v4-migration.md "inferno/v4-migration.md at master · infernojs/inferno")

----

[Workers at Your Service | WebKit](https://webkit.org/blog/8090/workers-at-your-service/ "Workers at Your Service | WebKit")에는 [Safari 11.1](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_11_1.html "Safari 11.1")(beta)에 구현된 Service Worker에 대해 소개돼 있습니다.

사양적인 측면과 Safari에서의 구현 정보, 캐시 보관 장소나 삭제 방법 등에 대해 이야기합니다.
몇 주간 사용하고 있지 않은 Service Worker와 캐시를 자동으로 삭제하는 것과 캐시 크기를 50MB/partition으로 제한하는 것 등, Safari 11.1에서의 특징에 대해서도 작성돼 있습니다.

그리고 [PWAs are coming to iOS 11.3: Cupertino, we have a problem](https://medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea "PWAs are coming to iOS 11.3: Cupertino, we have a problem")에 Safari와 다른 브라우저와의 구현이 다른 부분과 홈 스크린 앱을 위한 Web App Manifest 대응 그리고 몇 가지 주의 사항에 대해 작성돼 있으니 함께 읽으면 좋을 거 같습니다.

----

[Eloquent JavaScript](https://eloquentjavascript.net/3rd_edition/ "Eloquent JavaScript") 제3판의 초안이 공개 됐습니다.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">You&#39;re all invited to read the full draft of Eloquent JavaScript&#39;s 3rd edition: <a href="https://t.co/8M5hp5awU2">https://t.co/8M5hp5awU2</a><br><br>Finishing touches are still ongoing, but this should be a readable text.</p>&mdash; Marijn Haverbeke (@MarijnJH) <a href="https://twitter.com/MarijnJH/status/958665332448784384?ref_src=twsrc%5Etfw">January 31, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

JavaScript와 프로그래밍에 대해 학습하는 도서입니다.
잘못된 정보 혹은 오타를 발견한 경우엔 [Issue](https://github.com/marijnh/Eloquent-JavaScript/issues)를 통해 알릴 수 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## jest/CHANGELOG.md at v22.2.0 · facebook/jest
[github.com/facebook/jest/blob/v22.2.0/CHANGELOG.md](https://github.com/facebook/jest/blob/v22.2.0/CHANGELOG.md "jest/CHANGELOG.md at v22.2.0 · facebook/jest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Jest 22.2.0이 릴리스됐습니다.

----

## browserify/changelog.markdown at v16.0.0 · browserify/browserify
[github.com/browserify/browserify/blob/v16.0.0/changelog.markdown](https://github.com/browserify/browserify/blob/v16.0.0/changelog.markdown "browserify/changelog.markdown at v16.0.0 · browserify/browserify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">ReleaseNote</span></p>

Browserify 16.0.0이 릴리스됐습니다.
`--preserve-symlinks` 지원를 지원하며  `events`의 shim이 갱신됐습니다. 또, `--node` 옵션을 지정하면 `__dirname`와 `__filename`이 동적으로 설정되도록 변경됐습니다.

----

## Dev.Opera — What’s new in Chromium 64 and Opera 51
[dev.opera.com/blog/opera-51/](https://dev.opera.com/blog/opera-51/ "Dev.Opera — What’s new in Chromium 64 and Opera 51")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 51 (based on Chromium 64)이 릴리스됐습니다.
Resize Observer, `import.meta`, ES2018의 정규표현이 구현됐으며 AudioWorklet을 시험 지원합니다(플래그를 붙여 사용할 수 있습니다).

----

## Release Notes for Safari Technology Preview 49 | WebKit
[webkit.org/blog/8088/release-notes-for-safari-technology-preview-49/](https://webkit.org/blog/8088/release-notes-for-safari-technology-preview-49/ "Release Notes for Safari Technology Preview 49 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 49가 릴리스됐습니다.
Service Worker가 활성화 됐고 Fetch의 버그가 수정됐으며 ITP에 디버그 모드가 시험 추가됐습니다. 또, Media Query에서 `calc()`를 지원하며 `String#trimStart`와 json superset proposal 등이 구현됐습니다.

- [tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262](https://github.com/tc39/proposal-json-superset "tc39/proposal-json-superset: Proposal to make all JSON text valid ECMA-262")

----

## Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API
[blog.chromium.org/2018/02/chrome-65-beta-css-paint-api-and.html](https://blog.chromium.org/2018/02/chrome-65-beta-css-paint-api-and.html "Chromium Blog: Chrome 65 Beta: CSS Paint API and the ServerTiming API")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 65 Beta가 릴리스됐습니다.
CSS Paint API, Server Timing API, Feature-Policy의 `sync-xhr`, TLS 1.3(draft-23) 등을 지원합니다.

----

## Eloquent JavaScript
[eloquentjavascript.net/3rd\_edition/](https://eloquentjavascript.net/3rd_edition/ "Eloquent JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">news</span></p>

Eloquent JavaScrip 제3판이 공개됐습니다.

----

## CanJS 4.0
[www.bitovi.com/blog/canjs-4.0](https://www.bitovi.com/blog/canjs-4.0 "CanJS 4.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CanJS 4.0이 릴리스 됐습니다.
템플릿 문법이 단순화 되거나 일관성 있게 수정됐으며 디버깅 도구와 Proxy, 클래스 기반의 Observable 객체가 추가됐습니다.

----

## Release Inferno v4 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v4.0.2](https://github.com/infernojs/inferno/releases/tag/v4.0.2 "Release Inferno v4 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v4가 릴리스 됐습니다.
`Inferno.Component`는 `inferno` 패키지에 이동됐고 `findDOMNode`는 `inferno-compat` 패키지에 이동됐습니다.
`createPortal`을 지원하고, Router가 React Router v4와 같도록 수정됐으며 최신 버전의 Mobx、Redux 연동이 가능도록 수정됐습니다. Inferno v4는 브라우저 IE9 이상 지원합니다.

- [inferno/v4-migration.md at master · infernojs/inferno](https://github.com/infernojs/inferno/blob/master/docs/v4-migration.md "inferno/v4-migration.md at master · infernojs/inferno")

----

## Echo JS on Twitter: "Echo JS, 2011-2018 - https://t.co/vEiEFdntF8"
[twitter.com/echojs/status/962996800738258945](https://twitter.com/echojs/status/962996800738258945 "Echo JS on Twitter: \"Echo JS, 2011-2018 - https://t.co/vEiEFdntF8\"")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

echojs.com 가 폐쇄됐습니다.

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="pt" dir="ltr">Echo JS, 2011-2018 - <a href="https://t.co/vEiEFdntF8">https://t.co/vEiEFdntF8</a></p>&mdash; Echo JS (@echojs) <a href="https://twitter.com/echojs/status/962996800738258945?ref_src=twsrc%5Etfw">February 12, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

----
<h1 class="site-genre">아티클</h1>

----

## 왜 제품에 Vue.js를 채용했는가, 운영해보고 어땠는지 이야기 | Nagisa의 스스메(일본어)
[blog.nagisa-inc.jp/archives/2980](https://blog.nagisa-inc.jp/archives/2980 "なぜプロダクトに Vue.js を採用したのか? 運用してみてどうっだった? という話 | Nagisaのすゝめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Vue</span> <span class="jser-tag">opinion</span> <span class="jser-tag">article</span></p>

Riot을 이용해 만든 사이트를 Vue로 리뉴얼 한 경험을 바탕으로 Vue의 특징, 라우터, 상태 관리, 프레임워크의 장/단점 등을 이야기합니다.

----

## Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/](https://blogs.windows.com/msedgedev/2018/02/06/welcoming-progressive-web-apps-edge-windows-10/ "Welcoming Progressive Web Apps to Microsoft Edge and Windows 10 - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">MS</span></p>

Microsoft Store에 PWA 애플리케이션을 등록할 수 있게 됩니다.
또, Bing에서 PWA 애플리케이션을 크롤 시 인덱싱에 적합한 후보로 식별합니다.

- [PWABuilder](https://www.pwabuilder.com/generator "PWABuilder")

----

## PWAs are coming to iOS 11.3: Cupertino, we have a problem
[medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea](https://medium.com/@firt/pwas-are-coming-to-ios-11-3-cupertino-we-have-a-problem-2ff49fd7d6ea "PWAs are coming to iOS 11.3: Cupertino, we have a problem")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Safari 11.1에 구현된 Service Worker에 관해 작성돼 있습니다.

몇 주간 사용하고 있지 않은 Service Worker와 캐시는 자동으로 삭제되는 점이나 Web App Manifetst 지원 방법 그리고 홈 스크린 앱 동작 시 주의할 점 등에 대해 이야기합니다.

- [Workers at Your Service | WebKit](https://webkit.org/blog/8090/workers-at-your-service/ "Workers at Your Service | WebKit")

----

## Introduction  |  Web Fundamentals  |  Google Developers
[developers.google.com/web/fundamentals/performance/webpack/](https://developers.google.com/web/fundamentals/performance/webpack/ "Introduction  |  Web Fundamentals  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">tutorial</span></p>

webpack을 사용한 경우 할 수 있는 코드최적화 방법에 대한 글입니다.
코드 분할이나 캐시, 분석 및 측정 방법에 대해 작성돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Hygen
[www.hygen.io/](http://www.hygen.io/ "Hygen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

코드 제너레이터 도구입니다.
템플릿에서 코드를 생성할 수 있습니다.
YAML Frontmatter으로 메타 데이터를 정의하고 ejs로 템플릿을 작성합니다. 그 외 의존이 필요한 경우 hook을 이용한 처리 등을 지원합니다.

----

## Jake Archibald: In The Loop - JSConf.Asia 2018 - YouTube
[www.youtube.com/watch?v&#x3D;cCOL7MC4Pl0](https://www.youtube.com/watch?v=cCOL7MC4Pl0 "Jake Archibald: In The Loop - JSConf.Asia 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">slide</span> <span class="jser-tag">video</span></p>

브라우저의 이벤트 루프에 관한 발표 영상입니다.
이벤트 루트와 스타일 변경을 반영하는 타이밍을 `setTimeout`, `requestAnimationFrame` 각각을 시각화하면서 차이점에 대해 설명합니다. 또, Promise 등의 MicroTask의 처리 순서에 대해서도 이야기합니다.

----

## JSConf.Asia 2018 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshFqN5dcZ704lxI3F5iHDYkl](http://www.youtube.com/playlist?list=PL37ZVnwpeshFqN5dcZ704lxI3F5iHDYkl "JSConf.Asia 2018 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">video</span></p>

JSConf.Asia 2018의 영상이 공개됐습니다.

- [JSConf.Asia Singapore 2018](https://2018.jsconf.asia/ "JSConf.Asia Singapore 2018")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Web Assembly Studio
[webassembly.studio/](https://webassembly.studio/ "Web Assembly Studio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">editor</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

C, Rust 등으로 WebAssembly 용 코드를 작성해 컴파일하고 실행할 수 있는 에디터 도구입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## thejameskyle/unstated: State that goes without saying
[github.com/thejameskyle/unstated](https://github.com/thejameskyle/unstated "thejameskyle/unstated: State that goes without saying")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React의 새로운 Context API를 사용한 상태 관리 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## VimeoSmashing Magazine
[vimeo.com/smashingmagazine](https://vimeo.com/smashingmagazine "VimeoSmashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span></p>

SmashingConf London 2018의 영상이 공개됐습니다.

----
