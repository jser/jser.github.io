---
title: "2017-05-22 JS: Safari TP 30, Polymer 2.0와 Bower, Create React App 1.0.0"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-05-22T10:59:03.315Z
category: JSer
tags:
- Safari
- Polymer
- Bower
- React

---

JSer.info #332 - [Safari Technology Preview Release 30](https://webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/ "Safari Technology Preview Release 30")이 릴리즈됐습니다.

[Subresource Integrity](https://www.w3.org/TR/SRI/ "Subresource Integrity")(SRI), `X-Content-Type-Options:nosniff`을 지원합니다.

- [How to implement SRI in your build process ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/04/how-to-implement-sri-into-your-build-process/ "How to implement SRI in your build process ★ Mozilla Hacks – the Web developer blog")
- [X-Content-Type-Options: nosniff · Issue #2758 · Fyrd/caniuse](https://github.com/Fyrd/caniuse/issues/2758 "X-Content-Type-Options: nosniff · Issue #2758 · Fyrd/caniuse")
  - Firefox도 버전 50부터 지원([참고](https://blog.mozilla.org/security/2016/08/26/mitigating-mime-confusion-attacks-in-firefox/))하고 있으며 이제 사파리도 지원하면서 주요 브라우저에서 모두 nosniff 지원하게 됐습니다.

또, Promise의 `rejectionhandled`와 `unhandledrejection` 이벤트도 지원합니다.

----

[Polymer 2.0.0](https://github.com/Polymer/polymer/releases/tag/v2.0.0 "2.0.0")과 [polymer-cli 1.0.0](https://github.com/Polymer/polymer-cli "polymer-cli")이 릴리즈됐습니다.
ES2015의 클래스 기반으로 쓸 수 있도록 됐고 Dirty checking을 opt-out할 수단과 1.x와의 호환 계층 등도 준비돼 있습니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tKvNeNGmOtU" frameborder="0" allowfullscreen></iframe>

- [Time for 2.0 - Polymer Project](https://www.polymer-project.org/blog/2017-05-15-time-for-two "Time for 2.0 - Polymer Project")
- [What's new in 2.0 - Polymer Project](https://www.polymer-project.org/2.0/docs/about_20 "What&#39;s new in 2.0 - Polymer Project")

아래 문서에 1.x에서의 마이그레이션에 대해 작성돼 있으니 참고하시길 바랍니다.

- [Polymer 2.0 upgrade guide - Polymer Project](https://www.polymer-project.org/2.0/docs/upgrade "Polymer 2.0 upgrade guide - Polymer Project")

또, [Bower](https://bower.io/ "Bower")를 사용해 Polymer를 설치하는게 공식 방법입니다([polymer-cli](https://github.com/Polymer/polymer-cli "polymer-cli")도 Bower를 기반으로 하고 있습니다).

- [Install Polymer 2.x - Polymer Project](https://www.polymer-project.org/2.0/start/install-2-0 "Install Polymer 2.x - Polymer Project")

하지만 며칠 전에 Bower는 정식으로 비권장이 됐습니다.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Bower is deprecated. <a href="https://t.co/XkIxOKhfBc">pic.twitter.com/XkIxOKhfBc</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/866085257052798976">May 21, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

- [Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower](https://github.com/bower/bower/pull/2458 "Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower")

때문에 Polymer도 npm/yarn을 지원하도록 변경 중입니다.

```
philipahlberg 5:52 PM
Hi everyone, with Bower being depreciated and pointing to Yarn now, should an issue be filed for the Polymer CLI to make the switch at some point in the future?

fresnizky 7:47 PM
@philipahlberg I think they're​ already working on it.
 https://github.com/Polymer/polymer/issues/3903#issuecomment-279180914
```

- Polymer의 slack에서 <https://polymer.slack.com/archives/C03PF4L4L/p1495270338490522>

다음 Issue에서 npm 지원에 관해 의논되고 있으며 현재 [@polymer/polymer](https://www.npmjs.com/package/@polymer/polymer "@polymer/polymer") 알파(α) 버전이 공개돼 있습니다.

- [Polymer on NPM stuck on version 1.2.5 · Issue #3903 · Polymer/polymer](https://github.com/Polymer/polymer/issues/3903#issuecomment-279180914 "Polymer on NPM stuck on version 1.2.5 · Issue #3903 · Polymer/polymer")

----

React의 Scafolding 도구인 Create React App 1.0이 릴리즈됐습니다.

webpack2로 업그레이드 됐고 런타임 상 에러가 웹페이지로 출력되며 Service Worker 대응하고 Jest20을 사용하도록 됐습니다. 또, Dynamic import를 사용한 코드가 분할 빌드 되도록 변경됐습니다.

- [What's New in Create React App - React Blog](https://facebook.github.io/react/blog/2017/05/18/whats-new-in-create-react-app.html "What&#39;s New in Create React App - React Blog")

아래 릴리즈 노트에 0.9.5에서의 마이그레이션 방법이 작성돼 있으니 참고하시길 바랍니다.

- [Release v1.0.0 · facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app/releases/tag/v1.0.0 "Release v1.0.0 · facebookincubator/create-react-app")

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Notes for Safari Technology Preview 30 | WebKit
[webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/](https://webkit.org/blog/7614/release-notes-for-safari-technology-preview-30/ "Release Notes for Safari Technology Preview 30 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 30이 릴리즈됐습니다. 
Subresource Integrity(SRI), `X-Content-Type-Options:nosniff`를 대응했고 Promise의 Unhandled rejection 이벤트를 지원합니다.
`document.cookie`의 동작 방식을 보다 정밀히 변경했고 WAI-ARIA와 관련 기능을 수정하는 등 다양한 변경 사항이 있습니다.


----

## Time for 2.0 - Polymer Project
[www.polymer-project.org/blog/2017-05-15-time-for-two](https://www.polymer-project.org/blog/2017-05-15-time-for-two "Time for 2.0 - Polymer Project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 2.0이 릴리즈됐습니다.
클래스 기반으로 작성할 수 있도록 변경됐고 Polymer CLI도 함께 업데이트 됐습니다.

- [Release Stable Release 2.0.0 · Polymer/polymer](https://github.com/Polymer/polymer/releases/tag/v2.0.0 "Release Stable Release 2.0.0 · Polymer/polymer")
- [What&#39;s new in 2.0 - Polymer Project](https://www.polymer-project.org/2.0/docs/about_20 "What&amp;#39;s new in 2.0 - Polymer Project")

----

## Release 7.0 “Coelestem adspicit lucem” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/7.0.0](https://github.com/postcss/autoprefixer/releases/tag/7.0.0 "Release 7.0 “Coelestem adspicit lucem” · postcss/autoprefixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Autoprefixer 7.0이 릴리즈됐습니다.
PostCSS 6.0, Browserslist 2.0, caniuse-lite를 이용하도록 변경됐습니다.
Node.js 0.12의 지원을 종료했고 기본적으로 Grid Layout의 접두사 기능을 비활성화 했고 코드 베이스가 CoffeeScript에서 Babel을 사용한 ECAMScript6로 변경됐습니다.

- [Autoprefixer 7.0 and Browserslist 2.0 — Martian Chronicles, Evil Martians’ team blog](https://evilmartians.com/chronicles/autoprefixer-7-browserslist-2-released "Autoprefixer 7.0 and Browserslist 2.0 — Martian Chronicles, Evil Martians’ team blog")

----

## ESLint v4.0.0-beta.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2017/05/eslint-v4.0.0-beta.0-released](http://eslint.org/blog/2017/05/eslint-v4.0.0-beta.0-released "ESLint v4.0.0-beta.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 4.0.0β가 릴리즈됐습니다.

- [ESLint v4.0.0의 변경사항 정리 - Qiita](http://qiita.com/mysticatea/items/3d01452d76ea6c943793 "ESLint v4.0.0의 변경사항 정리 - Qiita")(일본어)

----

## Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower
[github.com/bower/bower/pull/2458](https://github.com/bower/bower/pull/2458 "Add yarn and webpack recommendation from bower.io to readme Fixes #2298 by graingert · Pull Request #2458 · bower/bower")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span></p>

Bower가 `npm deprecate`가 되어 정식으로 비권장 됐습니다.
유지보수는 계속 할 예정이며 Bower의 미래(유지보수/개발)에 흥미가 있는 사람은 메일로 연락해 달라고 합니다.

- [Consider deprecating Bower. · Issue #2298 · bower/bower](https://github.com/bower/bower/issues/2298#issuecomment-302792690 "Consider deprecating Bower. · Issue #2298 · bower/bower")

----

## Release v1.0.0 · facebookincubator/create-react-app
[github.com/facebookincubator/create-react-app/releases/tag/v1.0.0](https://github.com/facebookincubator/create-react-app/releases/tag/v1.0.0 "Release v1.0.0 · facebookincubator/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app v1.0.0이 릴리즈됐습니다.
webpack2로 업그레이드 됐고 런타임 상 에러가 웹페이지로 출력되며 Service Worker 대응하고 Jest20을 사용하도록 됐습니다. 또, Dynamic import를 사용한 코드가 분할 빌드 되도록 변경됐습니다.

- [What&#39;s New in Create React App - React Blog](https://facebook.github.io/react/blog/2017/05/18/whats-new-in-create-react-app.html "What&amp;#39;s New in Create React App - React Blog")

----
<h1 class="site-genre">아티클</h1>

----

## ZEIT – Next 3.0 Preview
[zeit.co/blog/next3-preview](https://zeit.co/blog/next3-preview "ZEIT – Next 3.0 Preview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">서버</span> <span class="jser-tag">ReleaseNote</span></p>

Next 3.0 프리뷰 버전이 릴리즈됐습니다.
`next export`로 정적인 HTML로 출력할 수 있도록 변경됐고 컴포넌트의 dynamic import를 지원하는 등 다양한 변경 사항이 있습니다.


----

## Developer Edition 54: New inspector and debugger features, MDN help in the netmonitor, and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2017/03/developer-edition-54-new-inspector-and-debugger-features/](https://hacks.mozilla.org/2017/03/developer-edition-54-new-inspector-and-debugger-features/ "Developer Edition 54: New inspector and debugger features, MDN help in the netmonitor, and more ★ Mozilla Hacks – the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Firefox 54 개발자 도구의 변경 사항을 소개하는 글입니다.
CSS Inspect가 개선됐고 Debugger 패널에서 코드판이 별도의 탭으로 열리거나 현 상태의 변수 값이 툴팁으로 출력되도록 변경됐습니다. 또, Network 패널에서 [More Info]을 통해 도움말 페이지로 바로 갈 수 있으며 JSON Viewer가 추가됐습니다.


----

## JavaScript의 또 하나의 「함수명」 —— name 프로퍼티 - Qiita(일본어)
[qiita.com/8x9/items/34272b59b5aa68e33256](http://qiita.com/8x9/items/34272b59b5aa68e33256 "JavaScript의 또 하나의 「함수명」 —— name 프로퍼티 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript Function의 `name` 프로퍼티에 관한 설명 글입니다.
ES2015부터 익명 함수나 Arrow Function 등에 함수 이름이 없어도 선언된 변수의 이름이 `name` 프로퍼티로 참조된다는 것과 `writable` 속성의 사양에 관해 소개 돼 있습니다.


----

## The Many Faces of Functions in JavaScript - Bocoup
[bocoup.com/blog/the-many-faces-of-functions-in-javascript](https://bocoup.com/blog/the-many-faces-of-functions-in-javascript "The Many Faces of Functions in JavaScript - Bocoup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

JavaScript의 여러가지 "함수" 선언 및 표현 방식에 관해 정리돼 있습니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## A Modern Front-End Workflow – Umar Hansa | Render 2017 - YouTube
[www.youtube.com/watch?v&#x3D;v5r\_n6Tq0uk](https://www.youtube.com/watch?v=v5r_n6Tq0uk "A Modern Front-End Workflow – Umar Hansa | Render 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">video</span></p>

Chrome 개발자 도구의 팁이나 디버깅 워크 플로우에 대해 소개하는 발표 영상입니다.


----

## The Future of Audio and Video on the Web (Google I/O '17) - YouTube
[www.youtube.com/watch?v&#x3D;z9unKFzAj1w](https://www.youtube.com/watch?v=z9unKFzAj1w "The Future of Audio and Video on the Web (Google I/O '17) - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ProgressiveWebApp</span></p>

웹의 영상이나 음악을 PWA로 어떻게 대응할 수 있는지 소개하는 발표 영상입니다.
ServiceWorker를 사용한 오프라인 대응, 디바이스 회전 시 자동 풀스크린, Media Capabilities를 사용한 재생 판단, MediaSession API를 이용한 커버 디자인 등 다양한 API와 사용 방법에 대해 소개합니다.

- [GoogleChrome/sample-media-pwa: A sample video-on-demand media Progressive Web App](https://github.com/GoogleChrome/sample-media-pwa "GoogleChrome/sample-media-pwa: A sample video-on-demand media Progressive Web App")
- [Customize Media Notifications and Handle Playlists  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/02/media-session "Customize Media Notifications and Handle Playlists  |  Web  |  Google Developers")
- [google/shaka-player: JavaScript player library / DASH client / MSE-EME player](https://github.com/google/shaka-player "google/shaka-player: JavaScript player library / DASH client / MSE-EME player")

----

## Web Performance: Leveraging the Metrics that Most Affect User Experience (Google I/O '17) - YouTube
[www.youtube.com/watch?v&#x3D;6Ljq-Jn-EgU&amp;index&#x3D;71&amp;list&#x3D;PLOU2XLYxmsIKC8eODk\_RNCWv3fBcLvMMy](https://www.youtube.com/watch?v=6Ljq-Jn-EgU&index=71&list=PLOU2XLYxmsIKC8eODk_RNCWv3fBcLvMMy "Web Performance: Leveraging the Metrics that Most Affect User Experience (Google I/O '17) - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">video</span></p>

성능과 측정 항목(Metrics)에 관해 소개하는 발표 영상입니다.
로드 완료가 아닌 상호 작용(Interactive)된 시간(TTI)를 측정하는 방법과 Hero Elements, UX를 측정 항목에 기준하여 이야기하며 Long Tasks(50ms)를 PerformanceObserver로 감지하는 방법과 조작 지연 측정, 개선을 위한 패턴에 대해서도 소개합니다.

- [GoogleChrome/tti-polyfill: TTI polyfill](https://github.com/GoogleChrome/tti-polyfill "GoogleChrome/tti-polyfill: TTI polyfill")

----

## CSS Houdini- the bridge between CSS, JavaScript and the browser by Serg Hospodarets
[slides.com/malyw/houdini-codemotion#/](http://slides.com/malyw/houdini-codemotion#/ "CSS Houdini- the bridge between CSS, JavaScript and the browser by Serg Hospodarets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">slide</span></p>

CSS Houdini(DOM을 벗어나 조금 더 저수준 레벨에서 CSS를 제어할 수 있도록 하는 스펙)에 관해 소개하는 슬라이드입니다.
CSS / JavaScript / 브라우저의 연계와 각 Worklet에 관해 이야기합니다.


----

##  Google I/O 2017 - All Sessions - YouTube
[www.youtube.com/playlist?list&#x3D;PLOU2XLYxmsIKC8eODk\_RNCWv3fBcLvMMy](http://www.youtube.com/playlist?list=PLOU2XLYxmsIKC8eODk_RNCWv3fBcLvMMy " Google I/O 2017 - All Sessions - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">이벤트</span></p>

Google I/O 2017 발표 영상이 공개됐습니다.


----

##  JSConf EU 2017 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshFmAPr65sU2O5WMs7\_CGjs\_](https://www.youtube.com/playlist?list=PL37ZVnwpeshFmAPr65sU2O5WMs7_CGjs_ " JSConf EU 2017 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">video</span></p>

JSConf EU 2017의 영상이 공개됐습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Don't Overcomplicate Javascript – Bits from Nikola Ristic ∞ ƒront-end ∆eveloper
[bits.ristic.io/dont-overcomplicate-javascript-0](https://bits.ristic.io/dont-overcomplicate-javascript-0 "Don't Overcomplicate Javascript – Bits from Nikola Ristic ∞ ƒront-end ∆eveloper")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">opinion</span></p>

JavaScript에서의 카고 컬트 프로그래밍(Cargo cult programming)에 대해 이야기하는 연재 글입니다. 특정 패턴이나 기술의 원칙이나 배경 이해 없이 코드 습관을 갖고 기술을 적용하면 기술적 부채나 복잡성도 함께 뒤따라 가져올 가능성이 있다고 이야기를 시작하면서 Redux에서의 Action에 대한 상수 패턴과 `import * as Constans from './constants'`의 문제점 등에 관해 소개합니다.


----

## HN PWA - Hacker News readers as Progressive Web Apps
[hnpwa.com/](https://hnpwa.com/ "HN PWA - Hacker News readers as Progressive Web Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">example</span></p>

Hacker News를 여러가지 View 프레임워크로 구현한 결과를 정리하고 공개하는 사이트입니다.

- [Hacker News API가 TodoMVC적인 장소가 됐다 | Web Scratch](http://efcl.info/2014/10/11/hackernews-api/ "Hacker News API가 TodoMVC적인 장소가 됐다 | Web Scratch")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## diegomura/react-pdf: Create PDF files using React
[github.com/diegomura/react-pdf](https://github.com/diegomura/react-pdf "diegomura/react-pdf: Create PDF files using React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">PDF</span> <span class="jser-tag">library</span></p>

React 컴포넌트로 레이아웃 등을 작성하고 PDF로 생성하는 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## Complete Redux Book by Ilya Gelman et al. \[PDF/iPad/Kindle\]
[leanpub.com/redux-book](https://leanpub.com/redux-book "Complete Redux Book by Ilya Gelman et al. \[PDF/iPad/Kindle\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">book</span></p>

Redux를 다루는 전자 서적입니다.


----
