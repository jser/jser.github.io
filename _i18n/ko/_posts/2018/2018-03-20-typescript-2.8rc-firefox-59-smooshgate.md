---
title: "2018-03-20 JS: TypeScript 2.8RC, Firefox 59, #SmooshGate"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-03-20T01:23:07.818Z
category: JSer
tags:
- TypeScript
- firefox
- ECMAScript

---

JSer.info #375　- TypeScript 2.8 RC 버전이 릴리스 됐습니다.

- [Announcing TypeScript 2.8 RC | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/ "Announcing TypeScript 2.8 RC | TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-28 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

Conditional Types와 Mapped Type Modifier에서 `-`, `+` 연산자 지원하며 NonNullable으로의 변환을 다룰 수 있도록 변경 됐습니다.
또, JSX Pragmas를 주석으로 지정할 수 있으며 `.d.ts` 만 출력하는 `--emitDeclarationsOnly` 지원 등이 이뤄졌습니다.

Conditional Types으로 형의 표현이 보다 넓어졌습니다. 자세한 내용은 릴리스 노트와 아래 문서를 참고하세요.

- [TypeScript 2.8의 Conditional Types에 관해 - Qiita](https://qiita.com/Quramy/items/b45711789605ef9f96de)(일본어)
- [Strongly Typed Event Emitters with Conditional Types](https://medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8)

----

Firefox 59가 릴리스 됐습니다.

- [Firefox — Notes (59.0) — Mozilla](https://www.mozilla.org/en-US/firefox/59.0/releasenotes/ "Firefox — Notes (59.0) — Mozilla")
- [Firefox 59 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Releases/59 "Firefox 59 for developers - Mozilla | MDN")

[PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent "PointerEvent")가 기본적으로 활성화 됐고 [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior "overscroll-behavior")와 [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget) 생성자 클래스가 구현됐습니다.

[EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget "EventTarget")은 Node.js의 EventEmitter 처럼 상속하여 pub / sub 클래스로 사용할 수 있습니다.

- [EventTarget 상속 가능에 따른 EventEmitter 대체 | blog.jxck.io](https://blog.jxck.io/entries/2017-07-10/subclassible-eventtarget.html "EventTarget 상속 가능에 따른 EventEmitter 대체 | blog.jxck.io")(일본어)

----

[#SmooshGate FAQ | Web | Google Developers](https://developers.google.com/web/updates/2018/03/smooshgate "#SmooshGate FAQ | Web | Google Developers")에는 최근 화제가 된 [#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")에 관한 FAQ가 정리돼 있습니다.

[#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")는 사양 현재 Stage 3 Proposal 인 [Array.prototype.flatMap과 Array.prototype.flatten](https://tc39.github.io/proposal-flatMap/ "Array.prototype.flatMap &amp; Array.prototype.flatten")의 break the web 문제와 관련된 내용입니다.
Firefox Nightly에 `Array.prototype.flatten`이 실험적으로 구현되면서 MooTools의 `Array.prototype.flatten` 구현과 충돌해 일부 사이트가 동작하지 않는 문제가 알려졌습니다.
그 문제의 회피안 중 하나로 `Array.prototype.flatten`를 `Array.prototype.smoosh`으로 이름을 변경하는 PR이 요청된 일련의 사건 흐름을 [#smooshgate](https://twitter.com/hashtag/smooshgate "#smooshgate")라고 부르고 있습니다.

- [rename flatten to smoosh by michaelficarra · Pull Request #56 · tc39/proposal-flatMap](https://github.com/tc39/proposal-flatMap/pull/56 "rename flatten to smoosh by michaelficarra · Pull Request #56 · tc39/proposal-flatMap")
- [SmooshGate: The ongoing struggle between progress and stability in JavaScript](https://medium.com/@jacobdfriedmann/smooshgate-the-ongoing-struggle-between-progress-and-stability-in-javascript-2a971c1162dd "SmooshGate: The ongoing struggle between progress and stability in JavaScript")

실제 `Array.prototype.flatten`는 MooTools와 prototype.js, sugar.js 등에서 구현돼 있습니다. 특정 라이브러리에서 표준 API를 덮어쓰고 있는지 판정할 수 있는 서비스 [Can I Standardize?](https://azu.github.io/can-i-standardize/ "Can I Standardize?")를 공개있으니 참고하세요.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Can I Standardize?<a href="https://t.co/Q1hA7MnHqB">https://t.co/Q1hA7MnHqB</a><br><br>`Array.prototype.flatten`:<br>- prototype.js define: true<br>- MooTools define: true<br>- Suger.js define: true<br><br>`Array.prototype.smoosh`:<br>prototype.js define: false<br>MooTools define: false<br>Suger.js define: false<br><br> <a href="https://twitter.com/hashtag/smooshgate?src=hash&amp;ref_src=twsrc%5Etfw">#smooshgate</a> <a href="https://twitter.com/hashtag/ecmascript?src=hash&amp;ref_src=twsrc%5Etfw">#ecmascript</a> <a href="https://t.co/JQluGQLU4N">pic.twitter.com/JQluGQLU4N</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/971958777485312000?ref_src=twsrc%5Etfw">March 9, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

위 문서에서는 왜 prototype 확장으로 인해 break the web이 발생했는지, 왜 MooTools를 수정하는 것으로 해결되지 않는지 TC39는 앞으로 이 문제를 어떻게 수정해 날갈 것인지에 대해 작성돼 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 2.8 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/](https://blogs.msdn.microsoft.com/typescript/2018/03/15/announcing-typescript-2-8-rc/ "Announcing TypeScript 2.8 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.8 RC가 릴리스 됐습니다.
Conditional Types와 Mapped Type Modifier에서 `-`, `+` 연산자를 지원하며 JSX Pragmas를 주석으로 지정할 수 있도록 변경 됐습니다.

----

## Release v1.2.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.2.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.2.0 "Release v1.2.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

puppeteer 1.2.0 릴리스 됐습니다.
`elementHandle.contentFrame()`와 리다이렉트 횟수를 반환하는 `request.redirectChain()`이 추가됐습니다.

----

## Firefox — Notes (59.0) — Mozilla
[www.mozilla.org/en-US/firefox/59.0/releasenotes/](https://www.mozilla.org/en-US/firefox/59.0/releasenotes/ "Firefox — Notes (59.0) — Mozilla")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 59 릴리스 됐습니다.
개발자 도구 개선됐고 [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent "PointerEvent")가 기본적으로 활성화 됐습니다. 그리고 [`overscroll-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior "overscroll-behavior")와 [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/EventTarget) 생성자 클래스도 구현 됐습니다.

- [Firefox 59 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Releases/59 "Firefox 59 for developers - Mozilla | MDN")

----

## Release Inferno v5.0.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v5.0.0](https://github.com/infernojs/inferno/releases/tag/v5.0.0 "Release Inferno v5.0.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Inferno v5.0.0이 릴리스 됐습니다. `.mjs`로 배포한 것을 `.js`로 변경했고 IE9 지원을 종료했습니다. 그리고 TypeScript 지원에 대한 기능이 개선됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## 어떤 LP의 제작 현장 - Qiita(일본어)
[qiita.com/noplan1989/items/a52a957546ddb9efeca3](https://qiita.com/noplan1989/items/a52a957546ddb9efeca3 "とあるLPの制作現場 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">design</span></p>

실서비스 웹 사이트의 랜딩 페이지(LP)를 어떻게 개발했는지 소개돼 있습니다.

----

## How to Build Password Generator with Electron & React Pt.1 - Setting the Stage - Alex Devero Blog
[blog.alexdevero.com/password-generator-pt1/](https://blog.alexdevero.com/password-generator-pt1/ "How to Build Password Generator with Electron & React Pt.1 - Setting the Stage - Alex Devero Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">JavaScript</span></p>

일렉트론을 사용해 비밀번호 생성 애플리케이션을 튜토리얼 형식으로 만들어 보는 글입니다.

----

## Unblocking Clipboard Access  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/clipboardapi](https://developers.google.com/web/updates/2018/03/clipboardapi "Unblocking Clipboard Access  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">clipboard</span> <span class="jser-tag">WebPlatformAPI</span></p>

Async Clipboard API에 대해 소개하는 글입니다.
지금까지 `document.execCommand`로 구현한 기능을 제대로 된 Permission 모델과 함께 개발할 수 있는 API에 대해 소개합니다.

----

## Data visualization with react-vis – DailyJS – Medium
[medium.com/dailyjs/data-visualization-with-react-vis-bd2587fe1660](https://medium.com/dailyjs/data-visualization-with-react-vis-bd2587fe1660 "Data visualization with react-vis – DailyJS – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

react-vis를 사용해 데이터를 시각화하는 방법에 대해 작성돼 있습니다.

----

## webpack 4의 optimization.splitChunks(폐지된 CommonsChunkPlugin 대신)의 사용 방법과 사용 장소 - Qiita(일본어)
[qiita.com/soarflat/items/1b5aa7163c087a91877d](https://qiita.com/soarflat/items/1b5aa7163c087a91877d "webpack 4 の optimization.splitChunks（廃止されたCommonsChunkPluginの代わり） の使い方、使い所 - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">article</span></p>

webpack 4의 `optimization` 옵션에 관해 이야기합니다.
`optimization.*` 설정과 각 출력 결과에 대해 작성돼 있습니다.

----

## Say Hello to Houdini and the CSS Paint API / Coder's Block
[codersblock.com/blog/say-hello-to-houdini-and-the-css-paint-api/](https://codersblock.com/blog/say-hello-to-houdini-and-the-css-paint-api/ "Say Hello to Houdini and the CSS Paint API / Coder's Block")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Paint API 관해 작성돼 있습니다.
Paint Worklet를 사용한 스타일 확장 방법과 스타일의 적용 방법에 대해 소개합니다.
또, 현시점에서의 CSS Paint API를 포함한 Houdini에 관해서도 이야기합니다.

----

## Redruco: Truco para aprender Redux (Parte 1) – Javier Fernandes – Medium
[medium.com/@javierfernandes/redruco-truco-para-aprender-redux-parte-1-c72d052576b0](https://medium.com/@javierfernandes/redruco-truco-para-aprender-redux-parte-1-c72d052576b0 "Redruco: Truco para aprender Redux (Parte 1) – Javier Fernandes – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">redux</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

React/Redux를 사용한 애플리케이션 개발 연재 글입니다.
Redux가 필요한 상태는 어떤 경우인지 또, 개발에 있어 애플리케이션의 상태와 UI의 상세를 독립적으로 바라볼 수 있는지에 관해 이야기합니다.
Storybook로 컴포너트를 확인하면서 애플리케이션을 만들어가는 튜토리얼 형식의 글입니다.

----

## #SmooshGate FAQ  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/03/smooshgate](https://developers.google.com/web/updates/2018/03/smooshgate "#SmooshGate FAQ  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TC39</span></p>

ECMAScript에서 `Array.prototype.flatten` Proposal이 기존 MooTools 등의 라이브러리와 이름이 출동해 break the web 현상이 발생하는 문제에 관해 작성돼 있습니다.
표준화와 구현이 다른 점 뿐 아니라 prototype을 열거하고 있는 점도 문제가 있으며 또, 왜 라이브러리 측의 구현을 변경 해도 해결되지 않는지 또 향후 어떻게 대처할 것인지 이야기합니다.

----

## Strongly Typed Event Emitters – Brian Terlson – Medium
[medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8](https://medium.com/@bterlson/strongly-typed-event-emitters-2c2345801de8 "Strongly Typed Event Emitters – Brian Terlson – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 2.8(RC)의 Conditional Type를 사용한 EventEmitter 형에 대해 작성돼 있습니다.

- [bterlson/strict-event-emitter-types: A type-only library for strongly typing any event emitter](https://github.com/bterlson/strict-event-emitter-types "bterlson/strict-event-emitter-types: A type-only library for strongly typing any event emitter")

----
<h1 class="site-genre">슬라이드, 영상

----

## nucleartide/emberconf-2018: EmberConf 2018 notes.
[github.com/nucleartide/emberconf-2018](https://github.com/nucleartide/emberconf-2018 "nucleartide/emberconf-2018: EmberConf 2018 notes.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">이벤트</span> <span class="jser-tag">video</span></p>

EmberConf 2018의 영상과 발표 자료가 정리 및 공개됐습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Everyone can now run JavaScript on Cloudflare with Workers
[blog.cloudflare.com/cloudflare-workers-unleashed/](https://blog.cloudflare.com/cloudflare-workers-unleashed/ "Everyone can now run JavaScript on Cloudflare with Workers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cdn</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">webservice</span></p>

Cloudflare Workers가 퍼블릭 공개됐습니다.
CDN 상에서 Service Worker와 같은 API로 어떠한 처리를 작성할 수 있는 서비스입니다.

----

## FromJS - Understand JavaScript Apps
[www.fromjs.com/](http://www.fromjs.com/ "FromJS - Understand JavaScript Apps")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">DOM</span> <span class="jser-tag">Extension</span> <span class="jser-tag">babel</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

DOM을 인스펙트하여 출력되고 있는 문자열이 코드의 어디에서 생성 됐는지 찾아 낼 수 있는 크롬 확장 플러그인입니다. HTML을 생성하는 DOM API를 덮어써서 역 추적하는 원리로 개발돼 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## vuex-orm/vuex-orm: The Vuex plugin to enable Object-Relational Mapping access to the Vuex Store.
[github.com/vuex-orm/vuex-orm](https://github.com/vuex-orm/vuex-orm "vuex-orm/vuex-orm: The Vuex plugin to enable Object-Relational Mapping access to the Vuex Store.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Vuex</span> <span class="jser-tag">ORM</span></p>

복잡한 데이터 구조를 다루기 위한 Vuex 플러그인입니다. 관계를 갖는 데이터를 정규화하고 Rails나 Laravel과 같은 ORM 스러운 API로 데이터를 검색하고 가져올 수 있습니다. 복잡하게 중첩된 데이터 구조를 정규화함으로써 데이터를 다루는 비용을 일정하게 유지하고자 개발됐습니다.

- [Vuex에서 관게를 갖는 복잡한 데이터 구조를 잘 다루기 위해 - Qiita](https://qiita.com/kiaking/items/bcd5360fb3106cf22a81 "Vuex에서 관게를 갖는 복잡한 데이터 구조를 잘 다루기 위해 - Qiita")(일본어)
- [paularmstrong/normalizr: Normalizes nested JSON according to a schema](https://github.com/paularmstrong/normalizr "paularmstrong/normalizr: Normalizes nested JSON according to a schema")

----

## maticzav/emma-cli: 📦 Terminal assistant to find and install node packages.
[github.com/maticzav/emma-cli](https://github.com/maticzav/emma-cli "maticzav/emma-cli: 📦 Terminal assistant to find and install node packages.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">検索</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

npm 모듈을 검색해서 직접 선택해 설치할 수 있는 도구입니다.

----

## terkelg/prompts: Lightweight, beautiful and user-friendly interactive prompts
[github.com/terkelg/prompts](https://github.com/terkelg/prompts "terkelg/prompts: Lightweight, beautiful and user-friendly interactive prompts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span></p>

Node.js 환경에 인터렉티브한 프롬프트를 생성할 수 있는 라이브러리입니다.

----
