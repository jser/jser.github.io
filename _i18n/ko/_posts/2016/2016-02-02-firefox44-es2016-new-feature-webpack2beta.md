---
title: "2016-02-02 JS: Firefox 44.0, ES2016의 추가 기능, webpack2β"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-02-02T19:57
category: JSer
tags:
    - Firefox
    - ECMAScript
    - webpack

---

JSer.info #264 - [Firefox 44.0](https://www.mozilla.jp/firefox/44.0/releasenotes/ "Firefox 44.0")가 릴리즈됐습니다.

`let`과 `const` 구현에 [Spidermonkey의 독자적인 동작](https://www.fxsitecompat.com/ja/docs/2015/variables-defined-with-const-and-let-are-no-longer-properties-on-window-redeclaration-with-let-will-throw/) 방식이 포함돼 있었지만, 이번에 ES6에 근거하여 변경됐습니다.

HTTP 통신에서 [Brotli](https://en.wikipedia.org/wiki/Brotli "Brotli") 압축 알고리즘을 지원합니다.

- [Content negotiation - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#The_Accept-Encoding_header "Content negotiation - HTTP | MDN")

Chrome 49에서도 동일한 기능이 구현돼 있습니다(HTTPS만 지원)

- [Intent to Ship: Brotli (Accept-encoding: br on HTTPS connection) - Google 그룹스](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/JufzX024oy0/WEOGbN43AwAJ "Intent to Ship: Brotli (Accept-encoding: br on HTTPS connection) - Google 그룹스")

----

ECMAScript 2016(ES2016)에 추가되는 기능이 확정됐습니다.

ES2016부터는 Proposal(≒기능)마다 사양을 검토하고, 최종적으로 합의를 얻은 Proposal만 ECMAScript 사양에 통합됩니다.
아래 2개의 Proposal이 새로운 책정 프로세스에 따라 ES2016 사양에 추가됐습니다.

- [Array.prototype.includes](https://github.com/tc39/Array.prototype.includes/ "Array.prototype.includes")
- [Exponentiation Operator](https://github.com/rwaldron/exponentiation-operator "Exponentiation Operator")

Proposal에서 사양으로 변경된 것이 2개 라는 의미입니다. 따라서 ES2016에는 새 사양 추가 외에도 다양한 변경 사항이 있습니다.

자세한 내용은 별도로 포스트했으니 참고해주세요.

- [ECMAScript 2016 features & changes - JSer.info](http://jser.info/ko/2016/02/01/es2016/ "ECMAScript 2016 features &amp; changes - JSer.info")

----

[What's new in webpack 2](https://gist.github.com/sokra/27b24881210b56bbaff7 "What&#39;s new in webpack 2")에는 webpack 2에 새롭게 추가되는 기능이나 변경 사항에 관해 작성돼 있습니다.

[Rollup](https://github.com/rollup/rollup "Rollup")과 마찬가지로 ES6 Modules를 해석하여, 사용하지 않는 코드를 삭제하는 기능이 추가됐습니다.

또, `System.import`를 모듈의 분할 포인트로써 다루는 것이 가능하게 됩니다.

이 외의 기타 변경 사항은 아래 issue를 참고하세요.

- [Scheduled small breaking changes for 2.0 · Issue #729 · webpack/webpack](https://github.com/webpack/webpack/issues/729 "Scheduled small breaking changes for 2.0 · Issue #729 · webpack/webpack")
- [Issues · webpack/webpack](https://github.com/webpack/webpack/labels/webpack-2 "Issues · webpack/webpack")

----
<h1 class="site-genre">헤드라인</h1>

----

## V8 JavaScript Engine: V8 Release 4.9
[v8project.blogspot.com/2016/01/v8-release-49.html](http://v8project.blogspot.com/2016/01/v8-release-49.html "V8 JavaScript Engine: V8 Release 4.9")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.9가 릴리즈됐습니다.
Destructuring, Proxy, Reflect, Default parameters 등이 ES6의 사양을 따르도록 변경됐습니다.
`Math.random()`의 알고리즘이 개선되는 등 다양한 변경 사항이 있습니다.

- [메이저 브라우저의 Math.random()의 알고리즘이 XorShify128+로 됐다 - JSer.info](http://jser.info/ko/2016/01/27/math.random-xsfhit/ "메이저 브라우저의 Math.random()의 알고리즘이 XorShify128+로 됐다 - JSer.info")

----

## jQuery UI 1.12.0 Beta 1 | jQuery UI Blog
[blog.jqueryui.com/2016/01/jquery-ui-1-12-0-beta-1/](http://blog.jqueryui.com/2016/01/jquery-ui-1-12-0-beta-1/ "jQuery UI 1.12.0 Beta 1 | jQuery UI Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery UI 1.12.0 Beta 1이 릴리즈됐습니다.
controlgroup과 checkboxradio의 추가, npm 지원, IE7 지원이 종료되는 등 다양한 변경 사항이 있습니다.

----

## jsdom/Changelog.md at master · tmpvar/jsdom
[github.com/tmpvar/jsdom/blob/master/Changelog.md](https://github.com/tmpvar/jsdom/blob/master/Changelog.md "jsdom/Changelog.md at master · tmpvar/jsdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 8.0.0이 릴리즈됐습니다.
IDL에서 코드를 생성하는 것으로 사양과의 호환성을 향상하고, `Element#insertAdjacentHTML`와 `Node#adoptNode`를 구현하는 등 다양한 변경 사항이 있습니다.

----

## Firefox 44.0 릴리즈 노트(일본어)
[www.mozilla.jp/firefox/44.0/releasenotes/](https://www.mozilla.jp/firefox/44.0/releasenotes/ "Firefox 44.0 릴리즈 노트")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 44.0이 릴리즈됐습니다.
`Symbol.toPrimitive`의 구현, let과 const가 ES6의 사양을 따르도록 수정, OffscreenCanvas API 플래그로 사용할 수 있도록(실험적) 추가, WebRTC에서 접두사를 삭제하는 등 다양한 변경 사항이 있습니다.

- [Firefox 44 for developers - Mozilla | MDN](https://developer.mozilla.org/Firefox/Releases/44 "Firefox 44 for developers - Mozilla | MDN")
- [Firefox 44 사이트 호환성 정보 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/44/ "Firefox 44 사이트 호환성 정보 | Firefox 사이트 호환성 정보")(일본어)
- [const나 let으로 정의된 변수는 window의 프로퍼티로 선언되지 않고, let으로 선언한 변수를 재선언하면 예외가 발생합니다 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/docs/2015/variables-defined-with-const-and-let-are-no-longer-properties-on-window-redeclaration-with-let-will-throw/ "const나 let으로 정의된 변수는 window의 프로퍼티로 선언되지 않고, let으로 선언한 변수를 재선언하면 예외가 발생합니다. | Firefox 사이트 호환성 정보")(일본어)

----

## Announcing TypeScript 1.8 Beta - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2016/01/28/announcing-typescript-1-8-beta.aspx](http://blogs.msdn.com/b/typescript/archive/2016/01/28/announcing-typescript-1-8-beta.aspx "Announcing TypeScript 1.8 Beta - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.8β가 릴리즈됐습니다.
tsc에 JavaScript 파일을 다룰 수 있는 `--allowJs`가 추가됐습니다.
ES6 to ES5를 TypeScript Compiler에서 변환하며, d.ts가 없이 라이브러리 등을 tsc가 직접 다루게 됩니다.
Unreachable code 검출, String literal types 추가, JSX를 대응한 개선 등 다양한 변경 사항이 있습니다.

- [What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-18-upcoming "What&#x27;s new in TypeScript · Microsoft/TypeScript Wiki")

----

## PhantomJS 2.1 Release Notes | PhantomJS
[phantomjs.org/release-2.1.html](http://phantomjs.org/release-2.1.html "PhantomJS 2.1 Release Notes | PhantomJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">software</span> <span class="jser-tag">ReleaseNote</span></p>

PhantomJS 2.1이 릴리즈됐습니다.
SSL Client Authentication, context menu 이벤트를 지원합니다.

----

## Release v3.1.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v3.1.0](https://github.com/rackt/redux/releases/tag/v3.1.0 "Release v3.1.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 3.1.0이 릴리즈됐습니다.
`createStore()`가 `applyMiddleware()`를 옵셔널하게 전달 받을 수 있도록 변경 됐습니다.

----

## Deprecate TSD · Issue #269 · DefinitelyTyped/tsd
[github.com/DefinitelyTyped/tsd/issues/269](https://github.com/DefinitelyTyped/tsd/issues/269 "Deprecate TSD · Issue #269 · DefinitelyTyped/tsd")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span></p>

TypeScript의 형 정의 파일을 관리하는 도구인 tsd 사용이 비권장 됐으며, 대신 typings를 사용하도록 권장합니다.

- [typings/typings - TypeScript](https://github.com/typings/typings "typings/typings - TypeScript")
- [vvakame/dtsm - TypeScript](https://github.com/vvakame/dtsm "vvakame/dtsm - TypeScript")

----
<h1 class="site-genre">아티클</h1>

----

## ECMAScript 2016 features &amp; changes - JSer.info
[jser.info/ko/2016/02/01/es2016/](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features & changes - JSer.info")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

이번에 확정된 ES2016에 추가되는 기능에 관해 정리돼 있습니다.
또 새로운 기능 이외의 변경 사항이나 어디를 살펴보면 사양의 변경을 알 수 있는지에 관해서도 작성돼 있습니다.

----

## What&#x27;s new in webpack 2
[gist.github.com/sokra/27b24881210b56bbaff7](https://gist.github.com/sokra/27b24881210b56bbaff7 "What's new in webpack 2")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack 2의 변경 사항을 소개합니다.
ES6 modules를 기반으로한 최적화, `System.import`를 사용한 동적 로드 용 모듈 분리에 대응하는 등 다양한 변경 사항이 있습니다.

----

## Front-end Application Libraries and Component Architectures - Telerik Developer Network
[developer.telerik.com/featured/front-end-application-frameworks-component-architectures/](http://developer.telerik.com/featured/front-end-application-frameworks-component-architectures/ "Front-end Application Libraries and Component Architectures - Telerik Developer Network")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">정리</span></p>

컴포넌트를 다루는 라이브러리의 구조나 구성, 라우터, 지원 브라우저 등을 비교한 결과가 정리돼 있습니다.
Polymer, React, Riot.js, Vue.js, Aurelia, Angular2에 관해 비교 작성돼 있습니다.

----

## Spencer Dixon - Test Driven React Tutorial
[spencerdixon.com/blog/test-driven-react-tutorial.html](http://spencerdixon.com/blog/test-driven-react-tutorial.html "Spencer Dixon - Test Driven React Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span></p>

React의 테스트에 관한 튜토리얼입니다.

----

## Adding ESLint to Your Project is Now Easier than Ever
[devnull.guru/adding-eslint-to-your-project-is-easier-than-ever/](http://devnull.guru/adding-eslint-to-your-project-is-easier-than-ever/ "Adding ESLint to Your Project is Now Easier than Ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Bluetooth</span></p>

ESLint 2.x에서 도입되는 `--init`에 의한 Automatic Configuration을 소개합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## CreateJS 입문 - ICS MEDIA(일본어)
[ics.media/tutorial-createjs/index.html](https://ics.media/tutorial-createjs/index.html "CreateJS入門 - ICS MEDIA")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span> <span class="jser-tag">tutorial</span></p>

CreateJS 입문을 위한 사이트입니다.

----

## Styleguide: Accessibility · edx/ux-pattern-library Wiki
[github.com/edx/ux-pattern-library/wiki/Styleguide:-Accessibility](https://github.com/edx/ux-pattern-library/wiki/Styleguide:-Accessibility "Styleguide: Accessibility · edx/ux-pattern-library Wiki")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">접근성</span> <span class="jser-tag">정리</span> <span class="jser-tag">WAI-ARIA</span></p>

접근성에 관한 스타일 가이드입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## naomiaro/waveform-playlist: Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Project inspired by Audacity.
[github.com/naomiaro/waveform-playlist](https://github.com/naomiaro/waveform-playlist "naomiaro/waveform-playlist: Multitrack Web Audio editor and player with canvas waveform preview. Set cues, fades and shift multiple tracks in time. Project inspired by Audacity.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span> <span class="jser-tag">audio</span> <span class="jser-tag">editor</span></p>

Audacity에 영감을 받아 개발된 Web Audio를 사용한 음성 에디터 입니다.

----

## sinsoku/clairvoyance
[github.com/sinsoku/clairvoyance](https://github.com/sinsoku/clairvoyance "sinsoku/clairvoyance")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span></p>

CSS의 커버리지 측정 도구입니다. CSS 파일에 작성된 스타일이 HTML 안에서 어느정도 사용되고 있는지 측정 가능합니다.

- [CSS의 커버리지를 측정하는 Clairvoyance라는 도구를 개발했습니다 - 애자일SE의 우울](http://sinsoku.hatenablog.com/entry/2016/01/31/174155 "CSS의 커버리지를 측정하는 Clairvoyance라는 도구를 개발했습니다 - 애자일SE의 우울")(일본어)

----

## juliankrispel/decaf: Coffeescript to ES.next transpiler
[github.com/juliankrispel/decaf](https://github.com/juliankrispel/decaf "juliankrispel/decaf: Coffeescript to ES.next transpiler")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

CoffeeScript의 코드를 JavaScript로 변환하는 도구입니다.

- [Issues · decaffeinate/decaffeinate](https://github.com/decaffeinate/decaffeinate "Issues · decaffeinate/decaffeinate")

----

## dfilatov/vidom: Library to build UI based on virtual DOM
[github.com/dfilatov/vidom](https://github.com/dfilatov/vidom "dfilatov/vidom: Library to build UI based on virtual DOM")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React에서 영감을 받아 Virtual DOM을 구현한 UI라이브러리 입니다.
React 처럼 작고, 빠른 것을 목적으로 하고 있습니다.

----

## developit/preact: Fast 3kb React alternative with the same ES6 API. Components &amp; Virtual DOM.
[github.com/developit/preact](https://github.com/developit/preact "developit/preact: Fast 3kb React alternative with the same ES6 API. Components & Virtual DOM.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React의 코어의 재구현을 목적으로 한 라이브러리로, Context나 PropTypes등이 삭제돼 있습니다.
preact-compat라는 React 호환 레이어를 별도의 모듈로 갖고 있습니다.

- [Differences to React · developit/preact Wiki](https://github.com/developit/preact/wiki/Differences-to-React "Differences to React · developit/preact Wiki")
- [developit/preact-compat - JavaScript](https://github.com/developit/preact-compat "developit/preact-compat - JavaScript")

----

## zeithq/micro: Micro — Async HTTP microservices
[github.com/zeithq/micro](https://github.com/zeithq/micro "zeithq/micro: Micro — Async HTTP microservices")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">node.js</span></p>

경량 HTTP 서버 라이브러리입니다.
단순히 리퀘스트를 전달받아 리스폰즈 하는 서버 구현체입니다.
async/await를 기본으로 사용할 수 있도록 돼 있습니다.

----

## sindresorhus/got: Simplified HTTP/HTTPS requests
[github.com/sindresorhus/got](https://github.com/sindresorhus/got "sindresorhus/got: Simplified HTTP/HTTPS requests")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">Promises</span></p>

Node.js 용의 HTTP 클라이언트 라이브러리입니다. `request`와 같은 관점의 라이브러리입니다.

----

## Viewer.js
[fengyuanchen.github.io/viewerjs/](http://fengyuanchen.github.io/viewerjs/ "Viewer.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">사진</span> <span class="jser-tag">library</span></p>

여러 가능이 있는 사진 뷰어 라이브러리입니다.

----

## stylelint/stylelint
[github.com/stylelint/stylelint](https://github.com/stylelint/stylelint "stylelint/stylelint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

규칙을 플러그인으로 확장할 수 있는 CSS의 스타일 검증 도구입니다.

----
