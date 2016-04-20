---
title: "2016-03-23 JS: Chrome 50β, React의 성능 측정 및 개선, Node.js compat table"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-03-23T23:26
category: JSer
tags:
    - Chrome
    - React
    - perf
    - Node.js

---

JSer.info #271 - [Chrome 50 Beta](http://blog.chromium.org/2016/03/chrome-50-beta-push-notification.html "Chrome 50 Beta")가 릴리즈됐습니다.

페이지를 완전하게 출력하기 위한 필요한 리소스를 먼저 불러오는 [link rel="preload"](https://w3c.github.io/preload/ "link rel=&#34;preload&#34;")를 지원합니다.

`<link rel="preload">`관한 자세한 내용은 아래에 잘 정리돼 있습니다.

- [Preload: What Is It Good For? – Smashing Magazine](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "Preload: What Is It Good For? – Smashing Magazine")

또, Firefox나 IE에는 구현돼 있는 [`HTMLCanvasElement.toBlob()](http://blog.chromium.org/2016/03/chrome-50-beta-push-notification.html "HTMLCanvasElement.toBlob()")을 Chrome에서도 지원합니다.

- [Chromium에서 Canvas.toBlob을 시험적으로 이용할 수 있습니다 - Qiita](http://qiita.com/uupaa/items/8bc48e904141be9224c4 "Chromium에서 Canvas.toBlob을 시험적으로 이용할 수 있습니다 - Qiita")(일본어)

----

[React를 사용한 제품의 성능을 개선한 이야기 | GMO 미디어 엔지니어 블로그](http://tech.gmo-media.jp/post/141458071484/react-perf-tuning)(일본어)에는 React를 사용한 웹 앱의 성능을 개선한 방법이 작성돼 있습니다.

`react-addons-perf`를 사용한 성능 측정, 어디에 문제가 있었고, 어떻게 해결했는지 이야기합니다.
이어서 아래의 문서나 공식 문서의 [Performance Tools](https://facebook.github.io/react/docs/perf.html) 문서를 함께 보면 좋을 것 같습니다.

- [A Deep Dive into React Perf Debugging](http://benchling.engineering/deep-dive-react-perf-debugging/ "A Deep Dive into React Perf Debugging")
- [Animating with React, Redux, and d3 | A geek with a hat](http://swizec.com/blog/animating-with-react-redux-and-d3/swizec/6775)

----

[Node.js ES2015/ES6 support](http://node.green/ "Node.js ES2015/ES6 support")라는 사이트에는 Node.js의 버전에 따른 ECMAScript 지원 현황이 정리돼 있습니다.

Node.js 버전의 [ECMAScript 6 compatibility table](http://kangax.github.io/compat-table/es6/ "ECMAScript 6 compatibility table")라고 말하면 이야기 쉬울 것 같습니다.

Node.js v6에서는 ES6의 대부분 지원될 예정이지만, v6는 [V8 5.0](http://v8project.blogspot.jp/2016/03/v8-release-50.html "V8 5.0")의 릴리즈를 기다렸다가 공개될 예정입니다.
때문에, Node.js v6는 4월 후반에 릴리즈될 것 같습니다.

- [Planning for v6 · Issue #5766 · nodejs/node](https://github.com/nodejs/node/issues/5766 "Planning for v6 · Issue #5766 · nodejs/node")

----
<h1 class="site-genre">헤드라인</h1>

----

## Announcing Marko v3: From HTML to HTML-JS | Marko
[markojs.com/blog/announcing-marko-v3/](http://markojs.com/blog/announcing-marko-v3/ "Announcing Marko v3: From HTML to HTML-JS | Marko")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">template</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

템플릿 엔진인 Marko v3가 릴리즈됐습니다.
HTML-JS syntax라는 JavaScript 처럼 작성한 템플릿 표현을 지원하고 컴파일 시의 최적화를 진행하는 등 다양한 변경 사항이 있습니다.

----

## Chromium Blog: Chrome 50 Beta: Push notification improvements and declarative preload
[blog.chromium.org/2016/03/chrome-50-beta-push-notification.html](http://blog.chromium.org/2016/03/chrome-50-beta-push-notification.html "Chromium Blog: Chrome 50 Beta: Push notification improvements and declarative preload")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 50 Beta가 릴리즈됐습니다.
`<link rel='preload'>`, `HTMLCanvasElement.toBlob()`의 지원, iframe의 sandbox 속성을 지원하고 있는지 판정할 수 있는 기능 추가, `Document.defaultCharset`을 삭제하는 등 다양한 변경 사항이 있습니다.

- [DOMTokenList Validation Added in Chrome 50 | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/03/domtokenlist-validation-added-in-chrome-50?hl=en "DOMTokenList Validation Added in Chrome 50 | Web Updates - Google Developers")
- [Preload: What Is It Good For? – Smashing Magazine](https://www.smashingmagazine.com/2016/02/preload-what-is-it-good-for/ "Preload: What Is It Good For? – Smashing Magazine")

----

## protractor/CHANGELOG.md at 3.2.0 · angular/protractor
[github.com/angular/protractor/blob/3.2.0/CHANGELOG.md](https://github.com/angular/protractor/blob/3.2.0/CHANGELOG.md "protractor/CHANGELOG.md at 3.2.0 · angular/protractor")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Protractor 3.2.0이 릴리즈됐습니다.
TypeScript 지원을 위한 기능이 추가됐고 임의의 버전의 WebDriver를 지정할 수 있도록 변경 됐습니다.

- [Typescript support · Issue #1203 · angular/protractor](https://github.com/angular/protractor/issues/1203#issuecomment-168777170 "Typescript support · Issue #1203 · angular/protractor")

----

## Google Cloud Platform Blog: Node.js on Google App Engine goes beta
[cloudplatform.googleblog.com/2016/03/Node.js-on-Google-App-Engine-goes-beta.html](https://cloudplatform.googleblog.com/2016/03/Node.js-on-Google-App-Engine-goes-beta.html "Google Cloud Platform Blog: Node.js on Google App Engine goes beta")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">google</span></p>

GAE에서 Node.js를 지원합니다(베타).

----
<h1 class="site-genre">아티클</h1>

----

## Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/](https://hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/ "Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span></p>

Firefox 47 개발자 도구의 새로운 기능에 관해 작성돼 있습니다.
어떤 관계로 객체가 유지되고 있는지 쉽게 알아볼 수 있도록 그래프를 제공하고, 콘솔에서 여러 줄을 입력할 수 있도록 변경됐습니다. 또, Storage Inspector에서 Cache API를 지원하는 등 여러가지 기능에 관해 작성돼 있습니다.

----

## Debugging with Node
[krasimirtsonev.com/blog/article/debugging-with-node](http://krasimirtsonev.com/blog/article/debugging-with-node "Debugging with Node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">debug</span> <span class="jser-tag">tutorial</span></p>

Node.js에서 예전부터 지원하는 `node debug` 명령어의 사용 방법에 관해 작성돼 있습니다.

----

## reBEM: React ♥ BEM — Medium
[medium.com/@mistadikay/rebem-react-bem-20d875157017](https://medium.com/@mistadikay/rebem-react-bem-20d875157017 "reBEM: React ♥ BEM — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">CSS</span></p>

React와 BEM의 조합에 관해 이야기합니다.
reBEM layers라는 관점에 관해서도 작성돼 있습니다.

----

## An Introduction to jQuery&#x27;s Deferred Objects
[www.sitepoint.com/introduction-jquery-deferred-objects/](http://www.sitepoint.com/introduction-jquery-deferred-objects/ "An Introduction to jQuery's Deferred Objects")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span></p>

jQuery Deferred의 역사와 사용방법에 관해 작성돼 있습니다.
각 1.x, 2.x, 3.x 에서의 차이점에 관해서도 이야기합니다.

----

## Animating with React, Redux, and d3 | A geek with a hat
[swizec.com/blog/animating-with-react-redux-and-d3/swizec/6775](http://swizec.com/blog/animating-with-react-redux-and-d3/swizec/6775 "Animating with React, Redux, and d3 | A geek with a hat")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">d3.js</span> <span class="jser-tag">SVG</span></p>

React와 D3.js를 조합하여 애니메이션 효과를 지원하는 컴포넌트를 만드는 방법에 관해 이야기합니다.
컨테이너 컴포넌트에서 State가 출발하는 구조이기 때문에 Redux에서 관리하는 점이 특이합니다.
대량의 파티클(particles)를 출력할 때 발생하는 병목 현상에 관해서도 작성돼 있습니다.

----

## React를 사용한 제품의 성능을 개선한 이야기 | GMO 미디어 엔지니어 블로그(일본어)
[tech.gmo-media.jp/post/141458071484/react-perf-tuning](http://tech.gmo-media.jp/post/141458071484/react-perf-tuning "React를 사용한 제품의 성능을 개선한 이야기 | GMO 미디어 엔지니어 블로그")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">debug</span></p>

React Component로 개발한 앱의 성능을 측정하는 방법과 개선하는 방법에 관해 작성돼 있습니다.
react-addons-perf를 사용해 프로파일링을 출력하고 분석해 나가는 과정을 자세히 이야기합니다.

----

## Redux Middleware in Depth - Qiita(일본어)
[qiita.com/kuy/items/c6784fe443f1d5c7bbdc](http://qiita.com/kuy/items/c6784fe443f1d5c7bbdc "Redux Middleware in Depth - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span></p>

Redux의 middleware에 관해 작성돼 있습니다.
middleware를 적용하는 순서나 실행되는 순서에 의해 일어나는 문제와 해결 방법에 관해 자세히 작성돼 있습니다.

----

## Why I Write Plain JavaScript Modules
[ponyfoo.com/articles/why-i-write-plain-javascript-modules](https://ponyfoo.com/articles/why-i-write-plain-javascript-modules "Why I Write Plain JavaScript Modules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

왜 DOM 라이브러리를 React/AngularJS 등 특정 프레임워크에 의존하지 않고 Pure한 DOM 라이브러리로써 개발하는지 이야기합니다.

----

## The State of Browser APIs - 1
[hwclass.in/2016/03/09/the-next-generation-of-browser-apis/](http://hwclass.in/2016/03/09/the-next-generation-of-browser-apis/ "The State of Browser APIs - 1")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">WebPlatformAPI</span></p>

현재 브라우저에서 사용할 수 있는 여러가지 새로운 API를 소개합니다.

- [AurelioDeRosa/HTML5-API-demos: A repository where you can find information about many JavaScript and HTML5 APIs.](https://github.com/AurelioDeRosa/HTML5-API-demos "AurelioDeRosa/HTML5-API-demos: A repository where you can find information about many JavaScript and HTML5 APIs.")

----

## JavaScript의 Promise 객체에 관해 리서치한 결과 | QUARTETCOM TECH BLOG(일본어)
[tech.quartetcom.co.jp/2016/03/22/javascript-promise/](http://tech.quartetcom.co.jp/2016/03/22/javascript-promise/ "JavaScriptのPromiseオブジェクトについて調べた事 | QUARTETCOM TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span></p>

Promise를 간결하게 정리한 글입니다.
AngularJS의 `$q` 관해서도 다루고있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Node.js ES2015/ES6 support
[node.green/](http://node.green/ "Node.js ES2015/ES6 support")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">まとめ</span></p>

Node.js 버전의 ECMAScript compat-table 입니다.

----

## Your first Progressive Web App
[codelabs.developers.google.com/codelabs/your-first-pwapp/](https://codelabs.developers.google.com/codelabs/your-first-pwapp/ "Your first Progressive Web App")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">tutorial</span></p>

Progressive Web App에 관해 배우는 워크숍 자료입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## gravmatt/force-js: The easy way to scroll and animate your page
[github.com/gravmatt/force-js](https://github.com/gravmatt/force-js "gravmatt/force-js: The easy way to scroll and animate your page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

별도 의존하는 라이브러리 없이 개발한 특정 요소를 애니메이션 처리하는 라이브러리입니다.

----

## danigb/tonal: Music tonal elements —pitches, chords, scales, keys— in Javascript
[github.com/danigb/tonal](https://github.com/danigb/tonal "danigb/tonal: Music tonal elements —pitches, chords, scales, keys— in Javascript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

Web MIDI, Web Audio API를 다루는 작은 사이즈의 라이브러리를 모아놓은 mono 저장소입니다.

----

## GoogleChrome/proxy-polyfill: Proxy object polyfill
[github.com/GoogleChrome/proxy-polyfill](https://github.com/GoogleChrome/proxy-polyfill "GoogleChrome/proxy-polyfill: Proxy object polyfill")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

ES6 Proxy의 polyfill 라이브러리입니다.
get/set/apply/construct 등 일부 trap 만을 지원하고 있습니다.

----
