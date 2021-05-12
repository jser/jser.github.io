---
title: "2021-05-11: Bootstrap 5, Underscore.js 1.13.0(`_.template` 보안 수정), Prettier 2.3"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-05-11T02:01:52.181Z
category: JSer
tags:
- CSS
- Tools
- node.js
- book
- WebComponents

---

JSer.info #539 - CSS 프레임워크 Bootstrap 5 릴리스.

- [Bootstrap 5 | Bootstrap Blog](https://blog.getbootstrap.com/2021/05/05/bootstrap-5/)

Bootstrap 5에서는 IE 지원을 종료하고 jQuery를 의존하지 않도록 재작성됐다.
offcanvas 컴포넌트, card의 아코디언을 대체하는 새로운 accordion 컴포넌트가 추가됐다.
또, Form과 Layout 변경, RTL 지원, Sass의 Utility API도 추가됐다.

v4에서의 마이그레이션 방법은 다음 문서에 정리돼 있다.

- [Migrating to v5 · Bootstrap v5.0](https://getbootstrap.com/docs/5.0/migration/)

----

Underscore.js 1.13 릴리스.

- [Underscore.js 1.13.0](https://underscorejs.org/#1.13.0)

Underscore.js 1.13에서는 `package.json`의 [`exports` 필드](https://nodejs.org/api/packages.html#packages_exports)에 대응하며 ECMAScript Modules를 지원한다.

또, Underscore.js 1.12에서는 lodash [4.17.21](https://github.com/lodash/lodash/releases/tag/4.17.21)에서 수정된 `_.template`의 취약점도 수정됐다.

- [Command Injection in lodash | Snyk](https://app.snyk.io/vuln/SNYK-JS-LODASH-1040724)

이와 경우는 별로 없을 것이라고 생각하지만 Underscore와 Lodash 모두 `_.template`의 `variable` 옵션에 임의의 문자열을 전달할 경우에 전달한 문자열을 코드로 실행할 수 있는 취약점이 있었다.

```js
const _ = require('underscore');
const template = _.template('hello: <%= name %>', { variable: '여기에 임의 코드 문자열을 전달할 수 있다는 취약점' });
template({ name: 'Mustache' });
```

----

Prettier 2.3 릴리스.

- [Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier](https://prettier.io/blog/2021/05/09/2.3.0.html)

새로운 JavaScript 포메터(Ember / Handlebars) 추가, Handlebars 지원을 alpha에서 release로 변경, JSON5 / JSON 포멧이 수정됐다.
JavaScript의 변수 및 프로퍼티 대입 코드가 일관성 있게 정책이 수정됐으므로 업데이트 시 큰 Diif가 발생할 수 있다. 그 외에 GraphQL, MD, YAML 관련 프리티어 정책이 변경돼 Diff가 발생한다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Bootstrap 5 | Bootstrap Blog
[blog.getbootstrap.com/2021/05/05/bootstrap-5/](https://blog.getbootstrap.com/2021/05/05/bootstrap-5/ "Bootstrap 5 | Bootstrap Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

Bootstrap 5 릴리스.
IE 지원 종료, jQuery 삭제.
offcanvas 컴포넌트, card 대체 accordion 컴포넌트 추가.
Form와 Layout 변경, RTL 지원, Sass의 Utility API 추가.

- [Migrating to v5 · Bootstrap v5.0](https://getbootstrap.com/docs/5.0/migration/ "Migrating to v5 · Bootstrap v5.0")

----

## Underscore.js
[underscorejs.org/#1.13.0](https://underscorejs.org/#1.13.0 "Underscore.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

underscore 1.13.0 릴리스.
ECMAScript Modules 지원, 
1.12.1에서는 `_.template`의 `variable` 옵션을 경우해 Code Injection이 가능한 취약점이 수정됐다.


----

## Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier
[prettier.io/blog/2021/05/09/2.3.0.html](https://prettier.io/blog/2021/05/09/2.3.0.html "Prettier 2.3. In which assignments are consistent, short keys non-breaking, and Handlebars official · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.3 릴리스.
JavaScript 포메터 정책이 크게 변경됨.
Handlebars 지원을 alpha에서 release로 변경, JSON5 / JSON 포멧 수정.

----
<h1 class="site-genre">아티클</h1>

----

## How we use Web Components at GitHub - The GitHub Blog
[github.blog/2021-05-04-how-we-use-web-components-at-github/](https://github.blog/2021-05-04-how-we-use-web-components-at-github/ "How we use Web Components at GitHub - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">Github</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

GitHub의 Web Components를 주제로 한 글.
Rails ViewComponent와 Catalyst를 사용한 Web Components 구성, GitHub Elements 공개.

- [github/github-elements: GitHub&#039;s Web Component collection.](https://github.com/github/github-elements "github/github-elements: GitHub&amp;#039;s Web Component collection.")

----

## 리소스 로드를 돕는 웹 브라우저 API의 세계(일본어)
[nhiroki.jp/2021/05/06/resource-loading-apis](https://nhiroki.jp/2021/05/06/resource-loading-apis "리소스 로드를 돕는 웹 브라우저 API의 세계")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

미리 가져오기 및 로드 순서 등 웹 브라우저에서의 리소스 로드의 Hint API와 구조를 소개한다.


----

## Hello, Modules!. JavaScript Modules, also known as ESM… | by Sindre Sorhus | May, 2021 | 🦄 Sindre Sorhus’ blog
[blog.sindresorhus.com/hello-modules-d1010b4e777b](https://blog.sindresorhus.com/hello-modules-d1010b4e777b "Hello, Modules!. JavaScript Modules, also known as ESM… | by Sindre Sorhus | May, 2021 | 🦄 Sindre Sorhus’ blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 10 지원이 종료됨으로써 ESM으로의 이전을 어떻게 할지를 주제로 한 글
ESM의 장점, 패키지 유지보수 용 이전 가이드.


----

## A Guide To Newly Supported, Modern CSS Pseudo-Class Selectors — Smashing Magazine
[www.smashingmagazine.com/2021/04/guide-supported-modern-css-pseudo-class-selectors/](https://www.smashingmagazine.com/2021/04/guide-supported-modern-css-pseudo-class-selectors/ "A Guide To Newly Supported, Modern CSS Pseudo-Class Selectors — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS로 활용할 수 있는 최신 의사 클래스 소개.
임의의 `a`에 매치하는 `:any-link`, 포커스 돼 있는 요소를 다루는 `:focus-visible`과 `:focus-within`, 셀렉터를 다루는 `:is()`와 `where()`와 `:has()`, `:empty` 등.


----

## Chapter 8: CSS | CSS-Tricks
[css-tricks.com/chapter-8-css/](https://css-tricks.com/chapter-8-css/ "Chapter 8: CSS | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">history</span> <span class="jser-tag">article</span></p>

CSS 역사를 주제를 한 글.
Lie, IE3의 CSS 구현, W3C의 CSS WG, Netscape의 JSSS。
doctype 선언으로 보는 스위치와 하위호환성, fantasai, CSS3에서의 모듈 접근 방식 등.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Svelte Summit Spring 2021 간단 정리(일본어)
[zenn.dev/tomoam/articles/889618f2e6e62f](https://zenn.dev/tomoam/articles/889618f2e6e62f "Svelte Summit Spring 2021 간단 정리")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Svelte Summit Spring의 영상과 각 영상 별 개요 정리.

- [Svelte Summit is a FREE whole-day online event.](https://sveltesummit.com/ "Svelte Summit is a FREE whole-day online event.")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## sinclairzx81/hammer: Build Tool for Browser and Node Applications
[github.com/sinclairzx81/hammer](https://github.com/sinclairzx81/hammer "sinclairzx81/hammer: Build Tool for Browser and Node Applications")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTML</span> <span class="jser-tag">Tools</span></p>

esbuild를 기반으로한 parcel 처럼 HTML을 엔트리포인트로 한 빌드 / 개발 도구.


----

## jsxtools/cqfill: Polyfill for CSS Container Queries
[github.com/jsxtools/cqfill](https://github.com/jsxtools/cqfill "jsxtools/cqfill: Polyfill for CSS Container Queries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span></p>

CSS Container Queries의 polyfill.
PostCSS와 조합하여 사용할 수 있다.

----

## google/zx: A tool for writing better scripts
[github.com/google/zx](https://github.com/google/zx "google/zx: A tool for writing better scripts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ShellScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

쉘 스크립트와 같은 처리를 자바스크립트로 작성할 수 있는 Node.js 도구.
Top-Level await와 함께 쉘 명령어를 그대로 쓸 수 있는 `$`, HTTP 통신할 수 있는 fetch 등 제공.


----
<h1 class="site-genre">도서</h1>

----

## 프로페셔널 Web 프로그래밍　JavaScript | 야나이 마사카즈 | 공학 | Kindle 스토어 | Amazon(일본어)
[www.amazon.co.jp/dp/B092QQJQF4/](https://www.amazon.co.jp/dp/B092QQJQF4/ "プロフェッショナルWebプログラミング　JavaScript | 柳井 政和 | 工学 | Kindleストア | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

동작하는 웹 페이지에 초점을 맞춰 소개하는 자바스크립트 입문서.


----

## React와 Vue에 관한 XSS 안티패턴(일본어)
[zenn.dev/yuuhu04/books/xss-anti-pattern-of-react-and-vue](https://zenn.dev/yuuhu04/books/xss-anti-pattern-of-react-and-vue "React と Vue に関する XSS アンチパターン")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">XSS</span> <span class="jser-tag">document</span></p>

React와 Vue에 관한 XSS 안티 패턴을 주제로 작성한 글.
React와 Vue의 이스케이프 구조, 프레임워크가 보호하지 않는 경우, XSS가 발생하는 패턴 등을 소개한다.


----
