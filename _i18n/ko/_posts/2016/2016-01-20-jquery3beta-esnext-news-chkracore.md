---
title: "2016-01-20 JS: jQuery 3.0β, ES.next News, ChakraCore OSS"
author: azu
layout: post
translator: U-Yeong Ju
date : 2016-01-20T22:57
category: JSer
tags:
    - jQuery
    - ECMAScript
    - MSEdge
    - CHakraCore

---

JSer.info #262 - jQuery 3.0β가 릴리즈됐습니다.

- [jQuery 3.0 Beta Released | Official jQuery Blog](http://blog.jquery.com/2016/01/14/jquery-3-0-beta-released/ "jQuery 3.0 Beta Released | Official jQuery Blog")

[jQuery 10주년](http://blog.jquery.com/2016/01/14/ten-years-of-jquery-and-beyond/)에 맞춰 릴리즈 됐습니다.
3.0에 관한 변경 사항도 정리돼 있으니, 이용하고 있다면 읽어보면 좋을 것 같습니다.


----

[ES.next News](http://esnextnews.com/ "ES.next News")는, 주 마다 5개 정도의 ES.next 관련 링크를 소개하는 매거진 사이트 입니다.

[JavaScript Weekly](http://javascriptweekly.com/ "JavaScript Weekly")를 보완하는 정보를 다루는 것 같습니다.

> We see ES.next News as complementary to JavaScript Weekly

- [ES.next News: a weekly email newsletter](http://www.2ality.com/2016/01/esnext-news.html "ES.next News: a weekly email newsletter")

관련 사항:

전 주, [JSer.info 5주년 기념 이벤트](http://jser.info/2016/01/16/jser-5years/ "JSer.info 5周年記念イベント")에서도 [발표](http://azu.github.io/slide/2016/jser5years/jser.info.html) 했듯이
[ECMAScript Daily News](http://ecmascript-daily.github.io/ "ECMAScript Daily News")라는 ECMAScript에 관해 다루는 사이트를 만들었습니다.

ECMAScript Daily News는 JSer.info를 보완하는 느낌으로 운영할 생각입니다.
개인적인 ECMAScript에 관한 메모를 겸하고 있고, ECMAScript의 사양이나 Proposal 위주(새롭게 Proposal이 공개됐다든지, V8에서 어떤 사양이 구현됐다든지, TC39에서 이러한 논의가 있었다 등)로 다룰 생각입니다.

라이브러리나 도구 등의 이야기는 다소 적지만, 흥미 있는 사람에겐 좋은 사이트가 될 것 같습니다.

- [RSS](http://ecmascript-daily.github.io/atom.xml "ECMAScript Daily")에서 구독 가능합니다.
- [ECMAScript Daily (@EcmascriptDaily)](https://twitter.com/ecmascriptdaily "ECMAScript Daily (@EcmascriptDaily) | Twitter") Twitter에서도 볼 수 있습니다.
- [메일 매거진](http://jser.us11.list-manage.com/subscribe/post?u=3d2f10a0ac6ad6b41153b027c&id=b591184502 "ECMAScript Daily")을 통해 주 마다 정리된 정보를 구독할 수 있습니다.


----

MSEdge의 JavaScript 엔진인 [ChakraCore](https://github.com/Microsoft/ChakraCore "ChakraCore")가 OSS로써 공개됐습니다.

- [ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/01/13/chakracore-now-open/ "ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog")

관련하여 [Node.js에서 ChakraCore도 이용할 수 있도록 한다 Pull Request](https://github.com/nodejs/node/pull/4765 "Enable Node.js to run with Microsoft's ChakraCore engine by kunalspathak · Pull Request #4765 · nodejs/node")도 진행되고 있습니다.

- [Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/01/19/nodejs-chakracore-mainline/ "Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog")

ChakraCore의 로드맵엔 Linux 지원, ES2015 Modules의 구현 등이 예정돼 있습니다.

- [Roadmap · Microsoft/ChakraCore Wiki](https://github.com/Microsoft/ChakraCore/wiki/Roadmap "Roadmap · Microsoft/ChakraCore Wiki")

----
<h1 class="site-genre">헤드라인</h1>

----

## jQuery 3.0 Beta Released | Official jQuery Blog
[blog.jquery.com/2016/01/14/jquery-3-0-beta-released/](http://blog.jquery.com/2016/01/14/jquery-3-0-beta-released/ "jQuery 3.0 Beta Released | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.0β가 릴리즈됐습니다.
jQuery10주년을 기념한 릴리즈입니다.

----

## Ember.js - Ember.js 2.3 and 2.4 Beta Released
[emberjs.com/blog/2016/01/15/ember-2-3-released.html](http://emberjs.com/blog/2016/01/15/ember-2-3-released.html "Ember.js - Ember.js 2.3 and 2.4 Beta Released")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember.js 2.3이 릴리즈됐습니다.
FastBoot에 `visit`이 추가됐습니다.

----

## Release 6.3 “Pro rege et lege” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/6.3.0](https://github.com/postcss/autoprefixer/releases/tag/6.3.0 "Release 6.3 “Pro rege et lege” · postcss/autoprefixer")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

Autoprefixer 6.3이 릴리즈됐습니다.
Grid Layout의 지원, 개인이 준비한 UA 데이터를 기준으로 브라우저의 종류를 결정할 수 있는 기능이 추가됐습니다.

----

## axios/CHANGELOG.md at v0.9.0 · mzabriskie/axios
[github.com/mzabriskie/axios/blob/v0.9.0/CHANGELOG.md](https://github.com/mzabriskie/axios/blob/v0.9.0/CHANGELOG.md "axios/CHANGELOG.md at v0.9.0 · mzabriskie/axios")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">XHR</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

axios 0.9.0가 릴리즈됐습니다.
XDomainRequest를 대응한 개선, `adapter` 프로퍼티를 추가하는 등 다양한 변경 사항이 있습니다.

----

## MooTools Blog: 1.6.0 is out!
[mootools.net/blog/2016/01/14/mootools-1-6-0-release](http://mootools.net/blog/2016/01/14/mootools-1-6-0-release "MooTools Blog: 1.6.0 is out!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MooTools 1.6.0이 릴리즈됐습니다.
Promises/A+와 호환할 수 있는`Class.Thenable`을 추가했습니다.
구 버전 브라우저 지원은 이번 릴리즈가 마지막이며, 다음 메이저 업데이트부터는 IE11+ 만을 지원하게 됩니다.
또 `Array.from`는 ES6의 메서드 명과 이름이 같아 Array.convert으로 이름을 변경했습니다.

----

## ES.next News: The 5 best ECMAScript links of the week
[esnextnews.com/](http://esnextnews.com/ "ES.next News: The 5 best ECMAScript links of the week")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">mail</span></p>

ES.next에 관한 주간 메일 메거진입니다.
JavaScript Weekly를 보완 하는 느낌입니다.
by Dr.Axel Rauschmayer and Johannes Weber.

- [ES.next News: a weekly email newsletter](http://www.2ality.com/2016/01/esnext-news.html "ES.next News: a weekly email newsletter")

----

## ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2016/01/13/chakracore-now-open/](https://blogs.windows.com/msedgedev/2016/01/13/chakracore-now-open/ "ChakraCore GitHub repository is now open | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">JavaScript</span></p>

MSEdge의 JavaScript 엔진인 Chakra의 Core 부분이 오픈소스로 공개됐습니다.

- [Microsoft/ChakraCore](https://github.com/Microsoft/Chakracore "Microsoft/ChakraCore")

----

## Enable Node.js to run with Microsoft&#x27;s ChakraCore engine by kunalspathak · Pull Request #4765 · nodejs/node
[github.com/nodejs/node/pull/4765](https://github.com/nodejs/node/pull/4765 "Enable Node.js to run with Microsoft's ChakraCore engine by kunalspathak · Pull Request #4765 · nodejs/node")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">issue</span></p>

Node.js에 ChakraCore 빌드를 추가할 수 있도록 하는 풀 리퀘스트입니다.

- [Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2016/01/19/nodejs-chakracore-mainline/ "Submitting a Pull Request to Node.js with ChakraCore | Microsoft Edge Dev Blog")

----

## Renaming jade -&gt; pug · Issue #2184 · pugjs/jade
[github.com/pugjs/jade/issues/2184](https://github.com/pugjs/jade/issues/2184 "Renaming jade -> pug · Issue #2184 · pugjs/jade")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span> <span class="jser-tag">node.js</span></p>

Jade를 pug로 이름 변경합니다.

----
<h1 class="site-genre">아티클</h1>

----

## babel-plugin-typecheck을 사용해 flowtype 문법으로 작성된 JS를 런타임 체크 한다 - Qiita(일본어)
[qiita.com/mizchi/items/30a5f9560e86e0d5ab31](http://qiita.com/mizchi/items/30a5f9560e86e0d5ab31 "babel-plugin-typecheck을 사용해 flowtype 문법으로 작성된 JS를 런타임 체크 한다 - Qiita")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">flowtype</span> <span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span></p>

FlowType의 형 정의 구문을 사용해 런타임 체크를 하는 Babel 플러그인을 소개합니다.

----

## Browserify VS Webpack - JS Drama
[blog.namangoel.com/browserify-vs-webpack-js-drama](http://blog.namangoel.com/browserify-vs-webpack-js-drama "Browserify VS Webpack - JS Drama")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">webpack</span></p>

철학의 차이, 정적 리소스를 다루는 방법, 어떤 것을 어떤 이유로 선택할 것인지에 관해 작성돼 있습니다.

----

## React.js Best Practices for 2016 | @RisingStack
[blog.risingstack.com/react-js-best-practices-for-2016/](https://blog.risingstack.com/react-js-best-practices-for-2016/ "React.js Best Practices for 2016 | @RisingStack")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React를 사용하는 방법, 데이터를 다루는(Dealing) 방법, 테스트 플러그인 사용해 테스트를 작성하는 방법 등에 관해 작성돼 있습니다.

----

## JS 라고하면 jQuery라던 Web 디자이너가, React을 1년간 사용하면서 느낀 장점 | dwango creators&#x27; blog（드완고 크리에이터 블로그）
[creator.dwango.co.jp/3413.html](http://creator.dwango.co.jp/3413.html "JS 라고하면 jQuery라고 말하던 Web 디자이너가, React을 1년간 사용하면서 느낀 장점 | dwango creators&#x27; blog（드완고 크리에이터 블로그）")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">design</span></p>

디자이너 관점에서 바라본 React에 관해 작성돼 있습니다.

----

## Enumify: better enums for JavaScript
[www.2ality.com/2016/01/enumify.html](http://www.2ality.com/2016/01/enumify.html "Enumify: better enums for JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">library</span></p>

class을 사용한 Enum 라이브러리에 관해 작성돼 있습니다.

- [rauschma/enumify](https://github.com/rauschma/enumify "rauschma/enumify")


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## MicheleBertoli/css-in-js - JavaScript
[github.com/MicheleBertoli/css-in-js](https://github.com/MicheleBertoli/css-in-js "MicheleBertoli/css-in-js - JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span></p>

React 계열 CSS in JS 라이브러리가 각각 비교/정리돼 있습니다.

----

## cheeaun/javascript-error-logging
[github.com/cheeaun/javascript-error-logging](https://github.com/cheeaun/javascript-error-logging "cheeaun/javascript-error-logging")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webservice</span> <span class="jser-tag">debug</span></p>

JavaScript의 error logging 서비스가 정리돼 있습니다.

----

## Progressive Web Apps | Web Fundamentals - Google Developers
[developers.google.com/web/progressive-web-apps](https://developers.google.com/web/progressive-web-apps "Progressive Web Apps | Web Fundamentals - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web</span></p>

Progressive Web App에 관해 Google이 정리한 문서입니다.
Progressive Web App는 무엇인지 설명합니다.

----

## thejameskyle/babel-handbook
[github.com/thejameskyle/babel-handbook](https://github.com/thejameskyle/babel-handbook "thejameskyle/babel-handbook")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">babel</span> <span class="jser-tag">tutorial</span></p>

Babel을 설치하는 방법이나 플러그인 개발 방법에 관해 작성된 핸드 북입니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## ariporad/pirates
[github.com/ariporad/pirates](https://github.com/ariporad/pirates "ariporad/pirates")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">babel</span></p>

`require.extensions`의 hook을 다루는 라이브러리입니다.
하나의 확장에 복수의 hook을 시행할 부분을 관리합니다.

----

## kolodny/deact - JavaScript
[github.com/kolodny/deact](https://github.com/kolodny/deact "kolodny/deact - JavaScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

Template Strings을 사용해 JSX 같이 작성 가능한 템플릿 엔진입니다.

----

## Jotted — Showcase self-hosted HTML, CSS and JavaScript demos, with editable source
[ghinda.net/jotted/](https://ghinda.net/jotted/ "Jotted — Showcase self-hosted HTML, CSS and JavaScript demos, with editable source")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JS Bin이나 JSFiddle 같은 형식으로 HTML/CSS/JS를 넣고 출력 가능한 라이브러리입니다.

----
