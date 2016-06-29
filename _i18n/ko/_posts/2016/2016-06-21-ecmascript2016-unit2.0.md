---
title: "2016-06-21 JS: ECMAScript 2016 릴리즈, QUnit 2.0"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-06-21T09:26
category: JSer
tags:
    - ECMAScript
    - Spec
    - i18n
    - QUnit

---

JSer.info #284 - ECMAScript 2016이 정식으로 릴리즈됐습니다. :tada:

- [ECMAScript® 2016 Language Specification](http://www.ecma-international.org/ecma-262/7.0/ "ECMAScript® 2016 Language Specification")

ECMAScript 2016의 변경 사항은 예전에 간단히 소개해드린적이 있습니다.

- [ECMAScript 2016 features & changes - JSer.info](http://jser.info/ko/2016/02/01/es2016/ "ECMAScript 2016 features &amp; changes - JSer.info")
- [ECMAScript 2015 - 2016 diff points](https://gist.github.com/azu/3dc9295e97aee9a2706068caf65f0348 "ECMAScript 2015 - 2016 diff points")

추가된 기능은 `Array.prototype.includes`와 [`**` 연산자](https://github.com/rwaldron/exponentiation-operator) 정도로 큰 변경사항은 없습니다.
(Proxy의 `[[enumerate]]` trap과 `Reflect.enumerate`가 삭제되기도 했습니다.)

ECMAScript의 사양 책정 프로세스는 스냅샷을 찍듯이 매년 릴리즈하는 방법으로 진행되고 있습니다. 
조금 예전에 작성한 글이지만 아래 문서에 해당 프로세스에 관해 소개한 글이 있으니 참고하시길 바랍니다.

- [ECMAScript의 사양 책정에 관한 컨닝페이퍼 | Web Scratch](http://efcl.info/2015/10/18/ecmascript-paper/ "ECMAScript의 사양 책정에 관한 컨닝페이퍼 | Web Scratch")(일본어)

HTML의 사양과 마찬가지로 ECMAScript의 사양을 읽으려한다면 [스냅샷](http://www.ecma-international.org/publications/standards/Ecma-262.htm)보다는 Living Standard스러운 아래 문서를 참조하는 편이 더 좋다고 생각합니다.

- [ECMAScript® 2017 Language Specification](https://tc39.github.io/ecma262/ "ECMAScript® 2017 Language Specification")

또, ECMAScript 2016과 동시에 [ECMAScript® 2016 Internationalization API Specification](http://www.ecma-international.org/ecma-402/3.0/ "ECMAScript® 2016 Internationalization API Specification")도 함께 릴리즈됐습니다.
`Intl` 오브젝트 등 [ECMAScript의 국제화 API](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Intl "ECMAScript의 국제화 API")를 책정하는 사양입니다.
이 사양도 매년 릴리즈하는 책정 프로세스로 운영됩니다.

- [Release 3rd Edition - Release Candidate · tc39/ecma402](https://github.com/tc39/ecma402/releases/tag/3.0-rc-1 "Release 3rd Edition - Release Candidate · tc39/ecma402")

ECMAScript의 최신 정보는 [ECMAScript Daily](https://ecmascript-daily.github.io/ "ECMAScript Daily")(일본어)에 작성 및 소개하고 있으니 관심이 있는 분은 참고하시길 바랍니다.

- [ecmascript-daily.github.io](https://ecmascript-daily.github.io/ "ECMAScript Daily")

----

JavaScript의 프레임워크 Qunit 2.0이 릴리즈됐습니다.

- [Release 2.0.0 · jquery/qunit](https://github.com/jquery/qunit/releases/tag/2.0.0 "Release 2.0.0 · jquery/qunit")

비권장이었던 글로벌 함수를 삭제하고, 메서드의 이름을 변경하는 등 비호환적인 변경 사항이 주로 이뤄졌습니다.

- `module()`, `test()`는 각각 `QUnit.*` 하위로 이동
- `start()`, `stop()` 대신 `assert.async()` 이용
- `setup`/`teardown`은 `beforeEach`/`afterEach`로 이름 변경
- `QUnit.init`과 `QUnit.reset` 삭제

업그레이드 가이드와 마이그레이션 도구가 공개돼 있으니 함께 살펴보시길 바랍니다.

- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")
- [apsdehal/qunit-migrate: Migrate old QUnit tests to 2.x](https://github.com/apsdehal/qunit-migrate "apsdehal/qunit-migrate: Migrate old QUnit tests to 2.x")

----
<h1 class="site-genre">헤드라인</h1>

----

## ECMAScript® 2016 Language Specification
[www.ecma-international.org/ecma-262/7.0/](http://www.ecma-international.org/ecma-262/7.0/ "ECMAScript® 2016 Language Specification")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span></p>

ECMAScript 2016이 릴리즈됐습니다.
매년 릴리즈하는 형식으로 변경된 후의 첫 릴리즈입니다.

- [Standard ECMA-262](http://www.ecma-international.org/publications/standards/Ecma-262.htm "Standard ECMA-262")
- [tc39/ecma262: Status, process, and documents for ECMA262](https://github.com/tc39/ecma262 "tc39/ecma262: Status, process, and documents for ECMA262")
- [ECMAScript 2016 features &amp;amp; changes - JSer.info](http://jser.info/2016/02/01/es2016/ "ECMAScript 2016 features &amp;amp; changes - JSer.info")

----

## ECMAScript® 2016 Internationalization API Specification
[www.ecma-international.org/ecma-402/3.0/](http://www.ecma-international.org/ecma-402/3.0/ "ECMAScript® 2016 Internationalization API Specification")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">spec</span></p>

ECMAScript 2016 Internationalization API 사양이 릴리즈됐습니다.
Unicode 8.0을 필요로 하게 됐고, `Intl.getCanonicalLocales()`이 추가됐습니다.

----

## Release v1.9.0 · testem/testem
[github.com/testem/testem/releases/tag/v1.9.0](https://github.com/testem/testem/releases/tag/v1.9.0 "Release v1.9.0 · testem/testem")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

testem 1.9.0이 릴리즈됐습니다.
커스텀 리포터가 meta 태그를 전달받을 수 있도록 변경됐습니다.

----

## Release 2.0.0 · jquery/qunit
[github.com/jquery/qunit/releases/tag/2.0.0](https://github.com/jquery/qunit/releases/tag/2.0.0 "Release 2.0.0 · jquery/qunit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.0.0이 릴리즈됐습니다.
비권장이었던 글로벌 함수를 삭제하고, 메서드의 이름을 변경하는 등 비호환적인 변경이 이뤄졌습니다.

- `module()`, `test()`는 각각 `QUnit.*` 하위로 이동
- `start()`, `stop()` 대신 `assert.async()` 이용
- `setup`/`teardown`은 `beforeEach`/`afterEach`로 이름 변경
- `QUnit.init`과 `QUnit.reset` 삭제

아래 업그레이드 가이드를 참고하세요.

- [QUnit 2.x Upgrade Guide | QUnit](http://qunitjs.com/upgrade-guide-2.x/ "QUnit 2.x Upgrade Guide | QUnit")

----

## ESLint v2.13.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/06/eslint-v2.13.0-released](http://eslint.org/blog/2016/06/eslint-v2.13.0-released "ESLint v2.13.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.13.0이 릴리즈됐습니다.
2.x 계열의 마지막 버전이며, 다음 버전으로는 3.0.0이 예정돼 있습니다.

- [Proposal for 3.0.0 · Issue #6356 · eslint/eslint](https://github.com/eslint/eslint/issues/6356 "Proposal for 3.0.0 · Issue #6356 · eslint/eslint")

----

## RC2 Now Available
[angularjs.blogspot.com/2016/06/rc2-now-available.html](http://angularjs.blogspot.com/2016/06/rc2-now-available.html "RC2 Now Available")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">ReleaseNote</span></p>

Angular2 RC2가 릴리즈됐습니다.

- [Angular 2 RC.2가 릴리즈됐습니다. | Angular2 Info](http://ng2-info.github.io/2016/06/16/angular-2-rc-2/ "Angular 2 RC.2가 릴리즈됐습니다. | Angular2 Info")(일본어)

----

## Safari 10.0
[developer.apple.com/library/prerelease/content/releasenotes/General/WhatsNewInSafari/Articles/Safari\_10\_0.html](https://developer.apple.com/library/prerelease/content/releasenotes/General/WhatsNewInSafari/Articles/Safari_10_0.html "Safari 10.0")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 10의 릴리즈 노트가 공개됐습니다.
IndexedDB, CSP, Shadow DOM v1, ES6, ECMA i18n API 등을 지원합니다.

----
<h1 class="site-genre">아티클</h1>

----

## React에서 TDD(테스트주도개발)을 시작해보다 : 환경 구축에서 테스트 작성, 기능 구현까지 소개하는 가이드 | 프로그래밍 | POSTD(일본어)
[postd.cc/getting-started-with-tdd-in-react/](http://postd.cc/getting-started-with-tdd-in-react/ "React에서 TDD(테스트주도개발)을 시작해보다 : 환경 구축에서 테스트 작성, 기능 구현까지 소개하는 가이드 | 프로그래밍 | POSTD")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">번역</span></p>

React Component를 TDD로 개발하는 이야기입니다.

----

## A Quick Introduction To Polymer — WebComponents.org
[webcomponents.org/articles/a-quick-polymer-introduction/](http://webcomponents.org/articles/a-quick-polymer-introduction/ "A Quick Introduction To Polymer — WebComponents.org")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span></p>

Polymer 입문을 위한 개괄적인 개요를 설명한 글입니다.

----

## 실사례로 학습하는 ECMAScript 2015 〜Generator〜 – NET BIZ DIV. TECH BLOG(일본어)
[tech.recruit-mp.co.jp/front-end/post-10358/](https://tech.recruit-mp.co.jp/front-end/post-10358/ "実例とともに学ぶECMAScript 2015 〜Generator〜 – NET BIZ DIV. TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span></p>

Generator, Iterator 에 관해 소개합니다.
Iterable를 다루는 for of, `Array.from`, spread operator 관해 이야기합니다.
「Generator는 Iterator를 반환하는 함수」등 관련된 특징이나 원리를 친절하게 설명하는 글입니다.

----

## The SoundCloud Client in React + Redux - RWieruch
[www.robinwieruch.de/the-soundcloud-client-in-react-redux/](http://www.robinwieruch.de/the-soundcloud-client-in-react-redux/ "The SoundCloud Client in React + Redux - RWieruch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">tutorial</span></p>

React + Redux로 Soundcloud의 클라이언트 부분을 만드는 튜토리얼입니다.

----

## The Future of Declaration Files | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/](https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/ "The Future of Declaration Files | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">TypeScript</span></p>

npm에서 TypeScript의 타입 정의 파일을 추가할 수 있게 된다고 합니다.

`npm install --save @types/lodash` 와 같은 형태로 별도의 도구없이 설치할 수 있습니다.

- [TypeScript Types Search](http://microsoft.github.io/TypeSearch/ "TypeScript Types Search")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Tips &amp; Tricks in Front-End Development // Speaker Deck
[speakerdeck.com/forloop/tips-and-tricks-in-front-end-development](https://speakerdeck.com/forloop/tips-and-tricks-in-front-end-development "Tips & Tricks in Front-End Development // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">슬라이드</span> <span class="jser-tag">Tips</span></p>

`object-fit`, Viewport unit, 읽은 링크를 다루는 법, 깨진 `<img />`를 표현하는 법, 요소 내에 빈공간이 생길때 출력 방법, postMessage, SVG 등의 프론트엔드 관련 팁을 소개합니다.

----

## CSS Animations, Orchestrated by David Khourshid
[slides.com/davidkhourshid/deck-17#/](http://slides.com/davidkhourshid/deck-17#/ "CSS Animations, Orchestrated by David Khourshid")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">슬라이드</span></p>

복잡한 CSS 애니메이션을 다루는 방법에 관한 슬라이드입니다.

----

## Resource (pre)loading
[yoavweiss.github.io/link\_htmlspecial\_16/](http://yoavweiss.github.io/link_htmlspecial_16/ "Resource (pre)loading")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">슬라이드</span></p>

`<link rel>`를 소개하는 슬라이드입니다.
prefetch, resource loading, feature detection 등에 관해 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## mgiuca/web-share: Web API proposal for sharing data from a web page
[github.com/mgiuca/web-share](https://github.com/mgiuca/web-share "mgiuca/web-share: Web API proposal for sharing data from a web page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">spec</span></p>

`navigator.share` API에 관한 문서입니다.
Web Share API는 Android의 intents, iOS의 UIActivityViewController 처럼 공유를 위한 API입니다.
Chrome에서 구현을 검토하고 있습니다.

- [Web Share - Chrome Platform Status](https://www.chromestatus.com/feature/5668769141620736 "Web Share - Chrome Platform Status")
- [Web Share API for sharing content to arbitrary destination - APIs - WICG](https://discourse.wicg.io/t/web-share-api-for-sharing-content-to-arbitrary-destination/1561/4 "Web Share API for sharing content to arbitrary destination - APIs - WICG")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## fed135/Kalm: Node socket wrapper and optimizer
[github.com/fed135/Kalm](https://github.com/fed135/Kalm "fed135/Kalm: Node socket wrapper and optimizer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">WebRTC</span> <span class="jser-tag">library</span></p>

Kalm은 양방향 통신(WebSocket, WebRTC)을 위한 라이브러리입니다.
Nagle 알고리즘을 구현하는 등 효율적으로 패킷을 전송하는 구조를 갖고 있습니다.
Adapter를 이용하여 통신 프로토콜을 변경할 수 있도록 구현돼 있습니다.

----

## af/envalid: Environment variable validation for Node.js
[github.com/af/envalid](https://github.com/af/envalid "af/envalid: Environment variable validation for Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Node.js `process.env`의 값을 검사하는 라이브러리입니다.

----

## headless - chromium/src - Git at Google
[chromium.googlesource.com/chromium/src/+/master/headless/](https://chromium.googlesource.com/chromium/src/+/master/headless/ "headless - chromium/src - Git at Google")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span></p>

Chromium 헤드리스 브라우저 저장소입니다.

----

## alexreardon/raf-stub: Accurate and predictable testing of requestAnimationFrame and cancelAnimationFrame
[github.com/alexreardon/raf-stub](https://github.com/alexreardon/raf-stub "alexreardon/raf-stub: Accurate and predictable testing of requestAnimationFrame and cancelAnimationFrame")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">animation</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

`requestAnimationFrame`의 stub 라이브러리입니다.
단계별로 프레임을 진행할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## Manning | Angular 2 in Action
[www.manning.com/books/angular-2-in-action](https://www.manning.com/books/angular-2-in-action "Manning | Angular 2 in Action")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

Angular 2를 소개하는 도서입니다.

- [Angular 2 in Action](https://github.com/angular-in-action/ "Angular 2 in Action")

----
