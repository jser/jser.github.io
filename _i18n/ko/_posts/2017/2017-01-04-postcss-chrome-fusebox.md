---
title: "2017-01-04 JS: PostCSS 개요, Chrome 개발자 도구, FuseBox"
author: azu
translator: U-Yeong Ju
layout: post
date : 2017-01-04T17:28
category: JSer
tags:
    - bundler
    - Tools
    - Chrome
    - PostCSS

---

JSer.info #312 - [PostCSS 정리 - Qiita](http://qiita.com/morishitter/items/4a04eb144abf49f41d7d "PostCSS 정리 - Qiita")(일본어)에는 [PostCSS](https://github.com/postcss/postcss "PostCSS")란 무엇인지에 관해 작성돼 있습니다.

PostCSS는 CSS의 기반 도구 또는 일종의 프레임워크로 CSS 파서나 제너레이터 등을 플러그인으로서 추가해 CSS 관련 여러가지 처리를 할 수 있는 기능을 제공합니다(파서 자체도 플러그인으로 확장할 수 있으므로 Sass도 포함할 수 있습니다).

이 글에서는 PostCSS의 정의 뿐 아니라 PostCSS 환경에서 사용할 수 있는 프리프로세스와 Linter 관련 도구 등도 함께 소개합니다.

----

[Optimise your web development workflow 2016](https://umaar.github.io/devtools-optimise-your-web-development-workflow-2016/#/ "Optimise your web development workflow 2016")에는 Chrome 개발자 도구의 다양한 기능을 GIF 사진과 함께 자세히 소개돼 있습니다.

Elements, Timeline, Networks, Audits 패널에 있는 기능과 이와 관련된 사양 및 도구 등도 함께 소개합니다.
한번 살펴보면 재미있을 것 같습니다.

또, 아래 사이트에서는 1Tips/1Page 형식으로 개발자 도구 관련 팁을 소개하고 있으므로 앞서 소개드린 슬라이드와 함께 읽으면 좋을 것 같습니다.

- [Dev Tips - Developer Tips by Umar Hansa](https://umaar.com/dev-tips/ "Dev Tips - Developer Tips by Umar Hansa")

----

bundler/module loader 도구 [Fusebox](http://fuse-box.org/ "Fusebox")가 공개됐습니다.
webpack 등과 같은 도구로 플러그인으로 변환 레이어를 추가할 수 있고, 그 결과를 단일 파일로 묶어주는 bundler 입니다.
또, webpack이나 SystemJS 등과 비슷한 기능을 제공하는 `FuseBox.import` 라는 Loader API도 함께 이용할 수 있습니다.

빠른 변환 속도가 장점 중 하나로 모듈의 의존 관계와 변환 후의 파일을 캐시하여 재변환 시의 처리 시간을 줄이도록 설계 돼 있습니다.

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">FuseBox cache and deps.json <a href="https://t.co/4EjS62HY28">pic.twitter.com/4EjS62HY28</a></p>&mdash; azu (@azu_re) <a href="https://twitter.com/azu_re/status/816568272736788480">January 4, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

이제 막 공개된 도구이므로 소스 코드를 살펴보는 것도 재미있을 것 같습니다. 소스 코드는 TypeScript로 작성돼 있습니다.

----

## 공지사항

- [jser/ping](https://github.com/jser/ping "jser/ping")에 Ping의 Issue를 등록하면 [@jser_info](https://twitter.com/jser_info "@jser_info")의 Twitter에 전달되도록 했습니다.
- 데이터 분석 용으로 [JSer.info Data Dashboard](https://jser.info/data-dashboard/ "JSer.info Data Dashboard")를 만들었습니다.
    - JSer.info에서 소개한 글이나 URL 등에 관한 데이터를 여러가지 분류로 살펴볼 목적으로 생성한 페이지입니다.
    - 데이터를 읽는 재미있는 분류 방법이 있다면 [jser/data-dashboard: JSer.info Data Dashboard.](https://github.com/jser/data-dashboard "jser/data-dashboard: JSer.info Data Dashboard.")에 Issue 또는 PR을 생성해 주시면 좋을 것 같습니다.
    
----
<h1 class="site-genre">헤드라인</h1>

----

## StealJS 1.0 Release
[www.bitovi.com/blog/stealjs-1.0-release](https://www.bitovi.com/blog/stealjs-1.0-release "StealJS 1.0 Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

개발 시엔 동적인 모듈 로더로 개발하고 배포 시엔 steal-tool를 이용해 production build 가능한 StealJS 1.0이 릴리즈됐습니다.

- [Easy ES6 with StealJS - YouTube](https://www.youtube.com/watch?v=VKydmxRm6w8 "Easy ES6 with StealJS - YouTube")

----
<h1 class="site-genre">아티클</h1>

----

## Optimizing Page Speeds With Lazyloading | Jscrambler Blog
[blog.jscrambler.com/optimizing-page-speeds-with-lazyloading/](https://blog.jscrambler.com/optimizing-page-speeds-with-lazyloading/ "Optimizing Page Speeds With Lazyloading | Jscrambler Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span></p>

Angular의 라우팅과 컴포넌트를 LazyLoad할 수 있는 방법 관해 작성돼 있습니다.

----

## Lazy Loading - React
[webpack.js.org/guides/lazy-load-react/](https://webpack.js.org/guides/lazy-load-react/ "Lazy Loading - React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">React</span></p>

webpack2를 사용해 React 컴포넌트를 LazyLoad 하는 방법에 관해 소개하고 있는 문서입니다.

----

## Flowtype으로 Flux 아키텍처에 타입 시스템을 적용하는 것에 관해 발표했다 - Please Drive Faster(일본어)
[joe-re.hatenablog.com/entry/2016/12/29/204917](http://joe-re.hatenablog.com/entry/2016/12/29/204917 "Flowtype으로 Flux 아키텍처에 타입 시스템을 적용하는 것에 관해 발표했다 - Please Drive Faster")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">Flux</span></p>

FlowType를 사용해 타입 시스템을 적용한 Flux 아키텍처 패턴에 관해 이야기합니다

- [flowtype으로 Flux에서의 타입 안전성을 손에 넣는다 - Qiita](http://qiita.com/joe-re/items/d6fd262a8c6017f41e22 "flowtype으로 Flux에서의 타입 안전성을 손에 넣는다 - Qiita")(일본어)

----

## Node.js Interview Questions and Answers (2017 Edition) | @RisingStack
[blog.risingstack.com/node-js-interview-questions-and-answers-2017/](http://blog.risingstack.com/node-js-interview-questions-and-answers-2017/ "Node.js Interview Questions and Answers (2017 Edition) | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span></p>

Node.js 관해 자주 있는 질문과 답변을 Q&A 형식으로 풀어낸 글입니다.
코딩 스타일, 자주하게 되는 작성 실수, 보안, 타이밍 공격 등에 관해 작성돼 있습니다.

----

## React Interview Questions
[tylermcginnis.com/react-interview-questions/](https://tylermcginnis.com/react-interview-questions/ "React Interview Questions")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span></p>

React에 관한 여러가지 의문을 Q&A 형식으로 풀어 작성한 글입니다.
Class로 작성한 컴포넌트와 함수로 작성한 컴포넌트의 차이, `refs`란 무엇인지, `key` 속성은 왜 중요한지 등 컴포넌트와 관련된 패턴에 관해 이야기합니다.

----

## Writing HTML with accessibility in mind – Medium
[medium.com/@matuzo/writing-html-with-accessibility-in-mind-a62026493412](https://medium.com/@matuzo/writing-html-with-accessibility-in-mind-a62026493412 "Writing HTML with accessibility in mind – Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span></p>

HTML와 접근성(스크린리더)에 관해 작성된 글입니다.
`lang` 속성, `alt` 속성, `<buton>` 속성, landmarks 등을 이야기합니다.

----

## PostCSS 정리 - Qiita(일본어)
[qiita.com/morishitter/items/4a04eb144abf49f41d7d](http://qiita.com/morishitter/items/4a04eb144abf49f41d7d "PostCSS まとめ - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span></p>

PostCSS의 개요와 특징 그리고 만든 동기 등을 소개합니다.

----

## Front-End Performance Checklist 2017 (PDF, Apple Pages) – Smashing Magazine
[www.smashingmagazine.com/2016/12/front-end-performance-checklist-2017-pdf-pages/](https://www.smashingmagazine.com/2016/12/front-end-performance-checklist-2017-pdf-pages/ "Front-End Performance Checklist 2017 (PDF, Apple Pages) – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

웹 프론트엔드의 성능과 관련된 체크 리스트가 정리돼 있습니다.
파일 사이즈, 전송 방법, 렌더링, 모니터링, 테스트 방법 등을 소개합니다.

----

## The Reflect API of ES6 – Zsolt Nagy
[www.zsoltnagy.eu/the-reflect-api-of-es6/](http://www.zsoltnagy.eu/the-reflect-api-of-es6/ "The Reflect API of ES6 – Zsolt Nagy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Reflect API를 소개하는 글입니다.

----

## MozAnime in 2016 | Nothing new
[birtles.wordpress.com/2016/12/27/mozanime-in-2016/](https://birtles.wordpress.com/2016/12/27/mozanime-in-2016/ "MozAnime in 2016 | Nothing new")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">animation</span></p>

2016년 시점에서 Firefox의 Web Animations 대응 수준과 새롭게 바뀐 디버깅 기능에 관해 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Optimise your web development workflow 2016
[umaar.github.io/devtools-optimise-your-web-development-workflow-2016/](https://umaar.github.io/devtools-optimise-your-web-development-workflow-2016/ "Optimise your web development workflow 2016")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">CSS</span> <span class="jser-tag">debug</span> <span class="jser-tag">slide</span> <span class="jser-tag">accessibility</span></p>

Chrome 개발자 도구의 기능과 활용법을 소개하는 슬라이드입니다.
주로 CSS, 접근성, 성능과 관련된 기능과 활용법을 GIF 애니메이션과 함께 소개하고 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Fuse-Box bundler / API Reference
[fuse-box.org/](http://fuse-box.org/ "Fuse-Box bundler / API Reference")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

webpack/Browserify와 같은 bundler 기능과 JSPM/SystemJS와 같은 loader 기능을 가지고 있는 도구입니다.
모듈의 의존 관계와 변환 후의 파일을 캐시하여 빠르게 변환됩니다.
플러그인으로 변환 방법을 확장할 수 있습니다.

- [FuseBox — bundle your project within a fraction of a second](https://medium.com/@ivanorlov/fusebox-bundle-your-project-within-a-fraction-of-a-second-f2360ba95727 "FuseBox — bundle your project within a fraction of a second")

----

## Gothdo/range: A JavaScript implementation of the Python&#x27;s range() function.
[github.com/Gothdo/range](https://github.com/Gothdo/range "Gothdo/range: A JavaScript implementation of the Python's range() function.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Python의 `range()`를 JavaScript 구현한 라이브러리입니다.

----

## andywer/leakage: 🐛 Memory leak testing for node.
[github.com/andywer/leakage](https://github.com/andywer/leakage "andywer/leakage: 🐛 Memory leak testing for node.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">test</span> <span class="jser-tag">libn</span></p>

Node.js에서 메모리 누수와 관련된 테스트 코드를 작성할 수 있는 라이브러리입니다.

----

## nolanlawson/marky: High-resolution JavaScript timer based on performance.mark() and measure()
[github.com/nolanlawson/marky](https://github.com/nolanlawson/marky "nolanlawson/marky: High-resolution JavaScript timer based on performance.mark() and measure()")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">libn</span></p>

User Timing API(`performance.mark`와 `performance.measure`) 기반으로 구현한 처리 시간 측정 라이브러리입니다.

----

## maniart/diffyjs: A dependency-free motion detection library for the browser
[github.com/maniart/diffyjs](https://github.com/maniart/diffyjs "maniart/diffyjs: A dependency-free motion detection library for the browser")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">画像</span></p>

`MediaDevices.getUserMedia()`를 사용해 얻은 사진 이용해 프레임별 움직임을 diif하여 취득할 수 있는 라이브러리입니다.
motion detection 라이브러리로 불립니다.

----
