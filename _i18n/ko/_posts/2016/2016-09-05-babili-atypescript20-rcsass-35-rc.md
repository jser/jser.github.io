---
title: "2016-09-05 JS: Babili α, TypeScript 2.0 RC, Sass 3.5 RC"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-09-05T19:41
category: JSer
tags:
    - Sass
    - Babel
    - TypeScript

---

JSer.info #295 - TypeScript 2.0 RC가 릴리즈됐습니다.

- [Announcing TypeScript 2.0 RC | TypeScript](https://blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/ "Announcing TypeScript 2.0 RC | TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-20 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

더 강력한 null 체크 방법 [`--strictNullChecks`](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#--strictnullchecks) 지원, [Tagged union types](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#tagged-union-types "Tagged union types") 지원, [tsconfig.json에서 glob을 지원](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#glob-support-in-tsconfigjson)하는 등 여러가지 기능이 강화됐습니다.


----

Babel의 플러그인으로 minify를 할 수 있는 [babili](https://github.com/babel/babili "babili") 알파(α)가 릴리즈됐습니다.

- [Babili (babel-minify) · Babel](https://babeljs.io/blog/2016/08/30/babili "Babili (babel-minify) · Babel")

ES2015+ 코드를 대응하여 압축하거나 미사용 코드를 삭제하는 등의 작업을 담당하는 Babel 플러그인 입니다.
Rollup이나 webpack은 bundle 도구 이므로 조금 영역이 다르고, [UglifyJS2](https://github.com/mishoo/UglifyJS2)와 같은 압축 도구에 목표를 두고 있는 것 같습니다.

----
CSS 메타 언어 Sass 3.5RC가 릴리즈됐습니다.

- [Sass 3.5 Release Candidate « Sass Blog](http://blog.sass-lang.com/posts/809572-sass-35-release-candidate "Sass 3.5 Release Candidate « Sass Blog")

C++로 구현한 [LibSass](http://sass-lang.com/libsass "LibSass")는 Ruby 버전을 거의 100% 호환하는 것 같습니다.
또, 3.5에는 CSS Custom Property, First-Class Functions, Bracketed Lists 등을 지원합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## esprima/ChangeLog at 3.0.0 · jquery/esprima
[github.com/jquery/esprima/blob/3.0.0/ChangeLog](https://github.com/jquery/esprima/blob/3.0.0/ChangeLog "esprima/ChangeLog at 3.0.0 · jquery/esprima")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">ReleaseNote</span></p>

esprima 3.0.0이 릴리즈됐습니다.
ES2016의 `**`(Exponentiation expression)과 JSX를 지원하는 등 다양한 변경 사항이 있습니다.

----

## Sass 3.5 Release Candidate « Sass Blog
[blog.sass-lang.com/posts/809572-sass-35-release-candidate](http://blog.sass-lang.com/posts/809572-sass-35-release-candidate "Sass 3.5 Release Candidate « Sass Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">ReleaseNote</span></p>

Sass 3.5 RC이 릴리즈됐습니다.
libsass가 Ruby 버전과 거의 100％의 호환성을 갖습니다.
또, CSS Custom Property를 지원하는 등 여러가지 기능적 변경 사항이 있습니다.

----

## jsdom/Changelog.md at 9.5.0 · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/9.5.0/Changelog.md](https://github.com/tmpvar/jsdom/blob/9.5.0/Changelog.md "jsdom/Changelog.md at 9.5.0 · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 9.5.0이 릴리즈됐습니다.
`document.scripts`, `document.embeds`와 `document.plugins`이 추가됐습니다.
`document.getElementsByTagName`가 `HTMLCollection`을 반환하도록 변경됐습니다.

----

## Angular 2 RC6
[angularjs.blogspot.com/2016/09/angular-2-rc6\_1.html](http://angularjs.blogspot.com/2016/09/angular-2-rc6_1.html "Angular 2 RC6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 2 RC6가 릴리즈됐습니다.
RC5 이하에서 비권장 됐었던 API가 삭제됐고, npm 패키지에 ES6 modules 형식의 소스를 포함하도록 변경됐습니다. 또, TypeScript 2.0을 대응하는 등 다양한 변경 사항이 있습니다.

- [Angular 2 RC.6가 릴리즈됐습니다. · Angular2 Info](https://ng2-info.github.io/2016/09/angular-2-rc-6/ "Angular 2 RC.6가 릴리즈됐습니다. · Angular2 Info")(일본어)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-rc6-2016-08-31 "angular/CHANGELOG.md at master · angular/angular")

----

## Release Notes for Safari Technology Preview Release 12 | WebKit
[webkit.org/blog/6928/release-notes-for-safari-technology-preview-release-12/](https://webkit.org/blog/6928/release-notes-for-safari-technology-preview-release-12/ "Release Notes for Safari Technology Preview Release 12 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview Release 12가 릴리즈됐습니다.
Fetch API가 기본적으로 활성화되도록 변경됐고, Resource Timing을 사양을 반영해 변경하는 등 다양한 변경 사항이 있습니다.

----

## Node v6.5.0 (Current) | Node.js
[nodejs.org/en/blog/release/v6.5.0/](https://nodejs.org/en/blog/release/v6.5.0/ "Node v6.5.0 (Current) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v6.5.0이 릴리즈됐습니다.
inspector가 uncaught exception을 지원하는 등 다양한 변경 사항이 있습니다.

----

## Announcing TypeScript 2.0 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/](https://blogs.msdn.microsoft.com/typescript/2016/08/30/announcing-typescript-2-0-rc/ "Announcing TypeScript 2.0 RC | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.0 RC가 릴리즈됐습니다.
Tagged Unions 지원, number와 string의 Literal Type 강화, tsconfig.json에서 glob을 지원하는 등 다양한 변경 사항이 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Babili (babel-minify) · Babel
[babeljs.io/blog/2016/08/30/babili](https://babeljs.io/blog/2016/08/30/babili "Babili (babel-minify) · Babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

Babel의 minify 플러그인인 Babili 베타(β) 버전에 관해 작성돼 있습니다.
변환 후의 ES5 코드를 압축하는 Uglify와 달리 ES2015+ 코드를 그대로 압축합니다.
또, Flow, TypeScript 등의 형 정의 도구를 사용한 코드도 압축을 지원합니다.

----

## The Case for Custom Elements: Part 1 – Dev Channel – Medium
[medium.com/dev-channel/the-case-for-custom-elements-part-1-65d807b4b439](https://medium.com/dev-channel/the-case-for-custom-elements-part-1-65d807b4b439 "The Case for Custom Elements: Part 1 – Dev Channel – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span></p>

Custom Element의 여러가지 케이스에 대해서 스터디한 내용이 작성돼 있습니다.

----

## 15K 행의 앱을 TypeScript 1.8에서 2.0으로 변경해봤다 - 빨리 프로그래머가 되고싶다(일본어)
[rhysd.hatenablog.com/entry/2016/07/15/090000](http://rhysd.hatenablog.com/entry/2016/07/15/090000 "15K 행의 앱을 TypeScript 1.8에서 2.0으로 변경해봤다 - 빨리 프로그래머가 되고 싶다")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span></p>

TypeScript 2 계열로 변경한 내용과 여러가지 옵션에 관해 작성돼 있습니다.

----

## the new code – Web Developer Reading List: Maths in JavaScript
[thenewcode.com/1131/Web-Developer-Reading-List-Maths-in-JavaScript](http://thenewcode.com/1131/Web-Developer-Reading-List-Maths-in-JavaScript "the new code – Web Developer Reading List: Maths in JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

자바스크립트의 Math에 관해 학습할 수 있는 튜토리얼입니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## React의 최신 동향과 베스트 플랙티스 // Speaker Deck(일본어)
[speakerdeck.com/koba04/reactfalsezui-xin-dong-xiang-tobesutopurakuteisu](https://speakerdeck.com/koba04/reactfalsezui-xin-dong-xiang-tobesutopurakuteisu "Reactの最新動向とベストプラクティス // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">슬라이드</span></p>

React의 컴포넌트의 작성법과 테스트 방법을 이야기하고 React와 함께 사용할 수 있는 여러가지 도구에 관해 소개하는 슬라이드입니다.

----

## Service Worker Deep Dive - Google 슬라이드(일본어)
[docs.google.com/presentation/d/19x3yi7Jn-6In5igGYfEiK0tBfNI290BAclT0AiqDj4Q/pub#slide=id.p](https://docs.google.com/presentation/d/19x3yi7Jn-6In5igGYfEiK0tBfNI290BAclT0AiqDj4Q/pub#slide=id.p "Service Worker Deep Dive - Google スライド")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">슬라이드</span></p>

최근 약 1년간의 Service Worker와 그 주변 환경의 변경 사항에 관해 소개하는 슬라이드입니다.
Push Notification, Stream, Background, Foreign Fetch, Header-based Install, Origin Trial 등을 이야기합니다.

----

## Edge Web Technologies and Browser Vendors(일본어)
[www.slideshare.net/dynamis/edge-web-technologies-and-browser-vendors](http://www.slideshare.net/dynamis/edge-web-technologies-and-browser-vendors "Edge Web Technologies and Browser Vendors")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">browser</span> <span class="jser-tag">슬라이드</span></p>

최근 웹 브라우저의 변경 사항 및 동향에 관해 소개하는 슬라이드입니다.
웹 호환성에 관한 방침, 새로운 기능 등에 관해 개괄적으로 소개합니다.

----

## WAI-ARIA 진기명기(일본어)
[www.slideshare.net/mlca11y/waiaria-65618928](http://www.slideshare.net/mlca11y/waiaria-65618928 "WAI-ARIA 진기명기")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">WAI-ARIA</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">슬라이드</span></p>

> WAI-ARIA는 표현이나 인터렉션을 변경하지 않는다.

role="button"을 선언한 엘리먼트에 키보드에 의한 인터렉션을 처리를 하지 않는 등의 사례에 관해 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## html-best-practices/README.ja.md at master · hail2u/html-best-practices(일본어)
[github.com/hail2u/html-best-practices/blob/master/README.ja.md](https://github.com/hail2u/html-best-practices/blob/master/README.ja.md "html-best-practices/README.ja.md at master · hail2u/html-best-practices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">번역</span></p>

HTML Best Practices의 일본어 버전입니다.

- [보통의 HTML 작성법(또는 HTML Best Practices  일본어 버전) - Weblog - Hail2u.net](https://hail2u.net/blog/webdesign/html-best-practices-in-japanese.html "보통의 HTML 작성법(또는 HTML Best Practices  일본어 버전) - Weblog - Hail2u.net")(일본어)
- [HTML5의 SVG 요소에는 네임스페이스 선언이 생략될 수 있다 - 주간SVG](http://ssvvgg.net/post/147494232850/html5%E3%81%AEsvg%E8%A6%81%E7%B4%A0%E3%81%A7%E3%81%AF%E5%90%8D%E5%89%8D%E7%A9%BA%E9%96%93%E5%AE%A3%E8%A8%80%E3%81%8C%E7%9C%81%E7%95%A5%E3%81%A7%E3%81%8D%E3%82%8B "HTML5의 SVG 요소에는 네임스페이스 선언이 생략될 수 있다 - 주간SVG")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Top | Diff of HTMLs
[diffofhtmls.herokuapp.com/](https://diffofhtmls.herokuapp.com/ "Top | Diff of HTMLs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WHATWG</span> <span class="jser-tag">HTML</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

WHATWG와 W3C HTML의 diff를 볼 수 있는 도구입니다.

----

## Async Redux Actions With RxJS - React Rally 2016
[www.slideshare.net/benlesh1/async-redux-actions-with-rxjs-react-rally-2016](http://www.slideshare.net/benlesh1/async-redux-actions-with-rxjs-react-rally-2016 "Async Redux Actions With RxJS - React Rally 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">Rx</span> <span class="jser-tag">슬라이드</span></p>

_redux-observable_에 관한 슬라이드 입니다.
Redux에서 비동기를 처리하는 경우, 연속성이나 취소(Cancel) 등을 표현하기 쉬운 RxJS를 사용한다는 내용이 작성돼 있습니다.

- [redux-observable/redux-observable: RxJS middleware for action side effects in Redux using &amp;#34;Epics&amp;#34;](https://github.com/redux-observable/redux-observable "redux-observable/redux-observable: RxJS middleware for action side effects in Redux using &amp;#34;Epics&amp;#34;")

----

## camwiegert/in-view: Get notified when a DOM element enters or exits the viewport.
[github.com/camwiegert/in-view](https://github.com/camwiegert/in-view "camwiegert/in-view: Get notified when a DOM element enters or exits the viewport.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">UI</span></p>

어떤 요소가 viewport에 포함돼 있는지를 판정하고, viewport에 들어오거나 나갔을 때의 이벤트에 핸들러를 등록할 수 있는 라이브러리입니다.
장래에 IntersectionObserver에도 대응할 계획을 하고 있습니다.

----

## dollarshaveclub/postmate: A powerful, simple, promise-based postMessage library 📭 📨 📬 📫 🚚
[github.com/dollarshaveclub/postmate](https://github.com/dollarshaveclub/postmate "dollarshaveclub/postmate: A powerful, simple, promise-based postMessage library 📭 📨 📬 📫 🚚")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Promise기반의 postMessage 라이브러리입니다.

----

## sdkennedy/babel-preset-target: Babel preset that allows for target environments to be specified along with plugins and presets. If all environments have native support for a given plugin, it will be skipped.
[github.com/sdkennedy/babel-preset-target](https://github.com/sdkennedy/babel-preset-target "sdkennedy/babel-preset-target: Babel preset that allows for target environments to be specified along with plugins and presets. If all environments have native support for a given plugin, it will be skipped.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">plugin</span></p>

지원하는 브라우저를 지정하는 것으로 필요한 부분만 Babel plugin 변환을 해주는 babel preset 입니다.

----
<h1 class="site-genre">도서</h1>

----

## Angular 2 Router by Victor Savkin [Leanpub PDF/iPad/Kindle]
[leanpub.com/router](https://leanpub.com/router "Angular 2 Router by Victor Savkin \[Leanpub PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

AngularJS 2의 Router에 관한 전자 서적입니다.

----
