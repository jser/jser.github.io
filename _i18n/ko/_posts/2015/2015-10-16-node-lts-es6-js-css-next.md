---
title: "2015-10-16のJS: Node.js 4.2.0 LTS、ES6、CSS.next"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-10-16T22:22
category: JSer
tags:
    - Node.js
    - ES6
    - CSS
    - JavaScript

---

JSer.info #249 - [Node.js 4.2.0](https://nodejs.org/en/blog/release/v4.2.0/ "Node v4.2.0")가 릴리즈됐습니다.

이 버전은 "Argon" 이라고 코드 명을 붙였으며 Node.js의 [LTS](https://github.com/nodejs/LTS "LTS")(Long-term Support) 버전으로써 릴리즈됐습니다.

- [Node.js 최초의 Long Term Support 대상이 된 「Node.js 4.2」, 코드명 "Argon"이 릴리즈됐다. 릴리즈 시점부터 2년 반은 메인터넌스 Publickey](http://www.publickey1.jp/blog/15/nodejs_long_term_support_argon.html "Node.js 최초의 Long Term Support 대상이 된 「Node.js 4.2」, 코드명 "Argon"이 릴리즈됐다. 릴리즈 시점부터 2년 반은 메인터넌스 Publickey")(일본어)

이름에서 알 수 있듯이 릴리즈 시점부터 액티브 18개월 + 메인터넌스 모드로 12개월, 총 30개월 동안 서포트가 이뤄질 예정의 버전입니다.

덧붙여, 현재 실행되고 있는 Node.js가 LTS 인지 여부를 반환하는 `process.release.lts` 등도 추가 됐습니다.

----

[ES6 Overview in 350 Bullet Points](https://ponyfoo.com/articles/es6 "ES6 Overview in 350 Bullet Points")에서는 동일한 저자가 작성한 [es6-in-depth](https://ponyfoo.com/articles/tagged/es6-in-depth "es6-in-depth")시리즈를 바탕으로 ES6의 기능을 조목 별로 정리해 소개하고 있습니다.

기능 별로 리스트화 돼 있으므로 평소 관심있었던 기능을 알기 위한 시작 점으로써 읽으면 좋을 것 같습니다.

----

[JavaScript/CSS 2015 Autumn](http://www.slideshare.net/t32k/javascriptcss-2015-autumn "JavaScript/CSS 2015 Autumn")슬라이드 에서는 자바스크립트와 CSS의 현 시점의 현황에 관해 작성돼 있습니다.

JavaScript 관해서는 ES6와 Babel을, CSS 관해서는 cssnext와 PostCSS 그리고 Sass를, 빌드 도구에 관해서는 Grunt/gulp와 npm을 소개합니다.

프론트엔드 개발 도구에 관해 폭넓게 정리돼 있으므로 전체적으로 살펴 본 다음, 관심있는 것 부터 하나씩 자세히 알아보면 좋을 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Node v4.2.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v4.2.0/](https://nodejs.org/en/blog/release/v4.2.0/ "Node v4.2.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 4.2.0가 릴리즈됐습니다.
"Argon"이라는 코드 명으로 LTS 버전(장기간 지원 버전)을 처음으로 릴리즈했습니다. 커멘드 라인 옵션에 신텍스만 체크하는 `--check` 인자를 추가했습니다.

- [add CLI option to syntax check script by bahamas10 · Pull Request #2411 · nodejs/node](https://github.com/nodejs/node/pull/2411 "add CLI option to syntax check script by bahamas10 · Pull Request #2411 · nodejs/node")

----

## Release 3.4.0 Release Candidate · knockout/knockout
[github.com/knockout/knockout/releases/tag/v3.4.0-rc](https://github.com/knockout/knockout/releases/tag/v3.4.0-rc "Release 3.4.0 Release Candidate · knockout/knockout")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout 3.4.0RC 버전이 릴리즈됐습니다.
`ko.isPureComputed`, `ko.onError`가 추가 됐으며 Observable의 성능을 개선했습니다.

----

## V8 JavaScript Engine: V8 Release 4.7
[v8project.blogspot.jp/2015/10/v8-release-47.html](http://v8project.blogspot.jp/2015/10/v8-release-47.html "V8 JavaScript Engine: V8 Release 4.7")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 4.7이 릴리즈 됐습니다.
Rest operator、Array#includes가 추가됐습니다.

- [V8 API changes - Google 문서](https://docs.google.com/document/d/1g8JFi8T_oAE_7uAri7Njtig7fKaPDfotU6huOa1alds/edit "V8 API changes - Google 문서")

----

## Release Fetch 0.10.0 · github/fetch
[github.com/github/fetch/releases/tag/v0.10.0](https://github.com/github/fetch/releases/tag/v0.10.0 "Release Fetch 0.10.0 · github/fetch")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Fetch API의 polyfill인 Fetch 0.10.0이 릴리즈됐습니다.
`Requst`/`Response` 객체에 몇 가지 메서드가 추가됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## 난독화된 자바스크립트 코드를 읽다 : document(일본어)
[imaya.blog.jp/archives/8183160.html](http://imaya.blog.jp/archives/8183160.html "난독화된 자바스크립트 코드를 읽다 : document")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

난독화된 코드를 읽기 위한 도구나 리팩터링 방법에 관해 소개합니다.

----

## ES2015 — Web Fundamentals
[developers.google.com/web/shows/ttt/series-2/es2015](https://developers.google.com/web/shows/ttt/series-2/es2015 "ES2015 — Web Fundamentals")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ES6를 학습하기 위한 리소스나 도구에 관해 소개합니다.

----

## ES6 Overview in 350 Bullet Points
[ponyfoo.com/articles/es6](https://ponyfoo.com/articles/es6 "ES6 Overview in 350 Bullet Points")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">정리</span></p>

eES6의 기능이나 포인트 에 관해 조목 별로 정리한 문서입니다.

----

## Surfin' Safari - Blog Archive » ES6 in WebKit
[www.webkit.org/blog/4054/es6-in-webkit/](https://www.webkit.org/blog/4054/es6-in-webkit/ "Surfin' Safari - Blog Archive » ES6 in WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">ECMAScript</span></p>

Safari 9과 WebKit nightly에 들어가는 ES6 기능에 대해 정리돼 있습니다.

----

## A Gentle Introduction to Ember 2.0 — Medium
[medium.com/@jamesfuthey/a-gentle-introduction-to-ember-2-0-8ef1f378ee4](https://medium.com/@jamesfuthey/a-gentle-introduction-to-ember-2-0-8ef1f378ee4 "A Gentle Introduction to Ember 2.0 — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Firebase와 Ember.js를 사용해 블로그를 만들어 가면서 Ember.js에 관해 학습할 수 있는 튜터리얼입니다.

----

## Lazy, composable, and modular JavaScript
[codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript](https://codewords.recurse.com/issues/four/lazy-composable-and-modular-javascript "Lazy, composable, and modular JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

자바스크립트에서의 고차원 함수, 함수 합성, 지연 평가에 관해 설명합니다. 또 Generator와 iterator를 사용한 함수의 조합 방법에 관해서도 이야기합니다.

----

##Not Angular한 환경에서 Protractor를 사용해 ES2015(ES6), ES7으로 E2E 테스트 코드를 작성해 봤다 - Qiita(일본어)
[qiita.com/nana4gonta/items/fabf1ab30ef16050c1e8](http://qiita.com/nana4gonta/items/fabf1ab30ef16050c1e8 "Not Angular한 환경에서 Protractor를 사용해 ES2015(ES6), ES7으로 E2E 테스트 코드를 작성해 봤다 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">protractor</span> <span class="jser-tag">Selenium</span></p>

async/await를 사용한 Protractor의 E2E테스트에 관해 소개합니다.
비동기 처리 부분을 async/await를 사용하여 직렬로 작성하는 방법을 이야기합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JavaScript/CSS 2015 Autumn
[www.slideshare.net/t32k/javascriptcss-2015-autumn](http://www.slideshare.net/t32k/javascriptcss-2015-autumn "JavaScript/CSS 2015 Autumn")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">슬라이드</span></p>

자바스크립트나 CSS, 빌드 도구 등에 관해 폭 넓게 정리돼 있는 슬라이드 입니다.

----

## AngularJS의 $watch 등록 수가 60,000이었다 - @yoshiko_pg(일본어)
[yoshiko-pg.github.io/slides/20151015-gp-meetup/](http://yoshiko-pg.github.io/slides/20151015-gp-meetup/ "AngularJS의 $watch 등록 수가 60,000이었다 - @yoshiko_pg")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">슬라이드</span></p>

AngularJS의 성능 개선에 관한 슬라이드 입니다.
$watch의 수를 알아내는 방법과 개선 방법에 관해 작성돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## All of the javascript features.
[jsfeatures.in/](http://jsfeatures.in/ "All of the javascript features.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">정리</span></p>

ES5, ES6나 ES.next의 기능별 샘플 코드가 정리돼 있는 사이트입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## gabrielbull/react-desktop
[github.com/gabrielbull/react-desktop](https://github.com/gabrielbull/react-desktop "gabrielbull/react-desktop")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">mac</span> <span class="jser-tag">windows</span></p>

OS X(혹은 Windows) 같은 느낌의 UI를 만들 수 있는 React Component 입니다.

----

## ryanbahniuk/sassaby
[github.com/ryanbahniuk/sassaby](https://github.com/ryanbahniuk/sassaby "ryanbahniuk/sassaby")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">testing</span> <span class="jser-tag">node.js</span></p>

Mocha나 Jasmine 등과 함께 Sass 코드를 테스트할 수 있도록 하는 Sass의 테스트 라이브러리입니다.
Sass의 함수나 mixin 등을 테스트 할 수 있습니다.

----

## Mancy NodeJs Repl
[www.mancy-re.pl/](http://www.mancy-re.pl/ "Mancy NodeJs Repl")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">software</span> <span class="jser-tag">Electron</span></p>

Electron을 사용해 개발한 JavaScript REPL 애플리케이션 입니다.

----
<h1 class="site-genre">도서</h1>

----

## Front-end Handbook - GitBook
[www.gitbook.com/book/frontendmasters/front-end-handbook/details](https://www.gitbook.com/book/frontendmasters/front-end-handbook/details "Front-end Handbook - GitBook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

프론트엔드 개발에 관한 전자 서적입니다.

----
