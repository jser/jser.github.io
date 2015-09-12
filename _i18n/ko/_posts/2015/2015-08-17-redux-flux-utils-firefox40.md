---
title: "2015-08-17의 JS: Redux 1.0.0、flux-utils、Firefox 40"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-08-17T20:21
category: JSer
tags:
    - flux
    - library
    - firefox

---

JSer.info #241 - Flux 처럼 단방향 데이터 플로우를 기반으로 하는 프레임워크인 [Redux](https://github.com/rackt/redux "Redux") 1.0.0이 릴리즈됐습니다.

- [Release v1.0.0 · rackt/redux](https://github.com/rackt/redux/releases/tag/v1.0.0 "Release v1.0.0 · rackt/redux")

Redux의 컨셉은 해당 개발자가 직접 작성한 [The Evolution of Flux Frameworks — Medium](https://medium.com/@dan_abramov/the-evolution-of-flux-frameworks-6c16ad26bb31 "The Evolution of Flux Frameworks — Medium")라는 문서에 잘 소개돼 있습니다.

짧게 설명 드리자면 State를 관리하는 컨테이너(redux 객체)를 제공하는 것으로 Flux의 ActionCreator와 Store에 해당하는 로직을 보통의 함수로 작성할 수 있도록 하고, 상태의 변화를 예측할 수 있는 환경으로 만드는 것에 목적을 두고 있습니다.

공식 문서나 [인기있는 Flux 프레임워크 Redux를 만져봤다 - 마루시테이아는 달위에](http://amagitakayosi.hatenablog.com/entry/2015/07/30/000000 "인기있는 Flux 프레임워크 Redux를 만져봤다 - 마루시테이아는 달위에")(일본어)등을 보면 특징이나 어떤 제약을 기반으로 만들어져 있는지 알 수 있습니다.

- [Read Me | Redux](http://rackt.github.io/redux/ "Read Me | Redux")
- [Three Principles | Redux](http://rackt.github.io/redux/docs/introduction/ThreePrinciples.html "Three Principles | Redux")

또, 지금까지 Flux는 Flux 아키텍처를 구현한 다른 프레임워크들 처럼 Store나 ActionCreator에 관한 구현체를 제공하지 않았지만, 이제는 [facebook/flux](https://github.com/facebook/flux "facebook/flux")에 [Flux Utils](https://github.com/facebook/flux/blob/master/docs/Flux-Utils.md "Flux Utils")를 추가하여 관련 기능을 제공합니다.

아래에 문서에 어떤 기능이 제공되고 있는지 간단히 정리돼 있습니다.

- [flux-utils에 관하여](https://gist.github.com/azu/e0274b703ef97226b0db "flux-utils에 관하여")(일본어)

[Immutable.js](https://facebook.github.io/immutable-js/ "Immutable.js")를 사용하고 있는 등의 여러가지 특징 중에서도 ReduceStore 객체의 reduce 메서드(state와 action을 전달 받아 적절하게 state를 변경한 후 반환하는 메서드)가 사이드-이펙트 없는 보통의 함수라는 글에서 Redux와 비슷한 개념을 제공하고 있음을 알 수 있습니다.

> This method should be pure and have no side-effects.

FluxUtils와 Reflux는 서로 영향을 받은 듯한 느낌이 들 수 있습니다. [Redux의 개발자](https://twitter.com/dan_abramov)와 [Flux의 개발자](https://twitter.com/fisherwebdev)의 대화를 한번 읽어보면 재미있을거 같습니다.

- [Combining Stateless Stores](https://gist.github.com/gaearon/d77ca812015c0356654f "Combining Stateless Stores")

<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/fisherwebdev">@fisherwebdev</a> <a href="https://twitter.com/goatslacker">@goatslacker</a> <a href="https://twitter.com/alexeyraspopov">@alexeyraspopov</a> Also, with Store-is-function pattern, you can easily keep modularity by delegating to &quot;substores&quot;</p>&mdash; Dan Abramov (@dan_abramov) <a href="https://twitter.com/dan_abramov/status/606155287024795648">June 3, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


----

[Firefox 40](http://www.mozilla.jp/firefox/40.0/releasenotes/ "Firefox 40")이 릴리즈됐습니다.

개발자 도구의 Perfomence 도구([Waterfall](https://developer.mozilla.org/en-US/docs/Tools/Performance/Waterfall) view, [Call Tree](https://developer.mozilla.org/en-US/docs/Tools/Performance/Call_Tree) view, [Flame Chart](https://developer.mozilla.org/en-US/docs/Tools/Performance/Flame_Chart) 등)가 개선됐습니다.

- [New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2015/06/new-performance-tools-in-firefox-developer-edition-40/ "New Performance Tools in Firefox Developer Edition 40 ✩ Mozilla Hacks – the Web developer blog")
- [Firefox 40 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/40 "Firefox 40 for developers - Mozilla | MDN")

또 동시에 [연장 지원 버전(ESR, Extended-support release)](https://www.mozilla.org/en-US/firefox/organizations/faq/) [Firefox 38.2.0](https://www.mozilla.org/en-US/firefox/38.2.0/releasenotes/)이 릴리즈됐습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v1.0.0 · rackt/redux
[github.com/rackt/redux/releases/tag/v1.0.0](https://github.com/rackt/redux/releases/tag/v1.0.0 "Release v1.0.0 · rackt/redux")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redux 1.0.0이 릴리즈됐습니다.
State를 관리하는 컨테이너(redux 객체)를 제공하는 것으로 Flux의 ActionCreator와 Store에 해당하는 로직을 보통의 함수로 작성할 수 있도록 하면서 단방향 데이터 플로우를 지원하는 라이브러리입니다.

----

## 1.1 Release
[blog.polymer-project.org/announcements/2015/08/13/1.1-release/](http://blog.polymer-project.org/announcements/2015/08/13/1.1-release/ "1.1 Release")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Polymer 1.1이 릴리즈 됐습니다.
컴포넌트와 글로벌 스코프에서 스타일을 공유하는 시스템을 추가했습니다.

- [Polymer 1.1 릴리즈 - Qiita](http://qiita.com/laco0416/items/51a3f7863602c1d35e8a "Polymer 1.1 릴리즈 - Qiita")(일본어)

----

## MozillaZine.jp » Blog Archive » Firefox 40이 릴리즈 됐다(일본어)
[mozillazine.jp/?p=4868](http://mozillazine.jp/?p=4868 "MozillaZine.jp » Blog Archive » Firefox 40이 릴리즈 됐다")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 40이 릴리즈 됐습니다.
`return` 구문 뒤에 작성해 실행되지 않는 코드를 경고하도록 개발자 도구가 개선됐고 Web Audio API와 Web Animations API의 사양을 따르는 등 여러가지 변경 사항이 있습니다.

- [Firefox 40의 도큐멘트 | Firefox 40 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/40/ "Firefox 40의 도큐멘트 | Firefox 40 사이트 호환성 정보")(일본어)
- [Firefox 40 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/40 "Firefox 40 for developers - Mozilla | MDN")(일본어)
- [Firefox 40 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Releases/40 "Firefox 40 for developers - Mozilla | MDN")(영어)

----
<h1 class="site-genre">아티클</h1>

----

## 4.0 is the new 1.0 — Node &amp; JavaScript — Medium
[medium.com/node-js-javascript/4-0-is-the-new-1-0-386597a3436d](https://medium.com/node-js-javascript/4-0-is-the-new-1-0-386597a3436d "4.0 is the new 1.0 — Node & JavaScript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">역사</span></p>

Node.js 4.0이 io.js와 병합이 완료된 버전으로 릴리즈될 예정입니다.

----

## Browserify dependencies in depth! | TEJI TECH BLOG(일본어)
[www.tejitak.com/blog/?p=1468](http://www.tejitak.com/blog/?p=1468 "Browserify dependencies in depth! | TEJI TECH BLOG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span></p>

Browserify의 의존 관계 해결 패턴에 관해 작성돼 있습니다.
의존하는 모듈의 버전이 복수인 경우에 발생하는 문제에 관한 여러가지 해결 방법을 소개합니다.

----

## ES6 In Depth: Modules ✩ Mozilla Hacks – the Web developer blog
[hacks.mozilla.org/2015/08/es6-in-depth-modules/](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/ "ES6 In Depth: Modules ✩ Mozilla Hacks – the Web developer blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 modules의 import/export의 다양한 구문과 각각의 동작에 관해 설명합니다.
Modules의 사양을 단계별로 나눠 볼 때 Loading에 관한 것은 아직 ECMAScript에 정의돼 있지 않다는 것과 구문적으로 정적(static)인 점 등에 관해 작성돼 있습니다.

----

## es6-coding-style/es6-coding-style-en.md at master · gf-web/es6-coding-style
[github.com/gf-web/es6-coding-style/blob/master/es6-coding-style-en.md](https://github.com/gf-web/es6-coding-style/blob/master/es6-coding-style-en.md "es6-coding-style/es6-coding-style-en.md at master · gf-web/es6-coding-style")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

ES6 코딩 스타일 가이드입니다. Destructuring의 과다 사용 주의, ES5 작성법을 ES6의 기능으로 깔끔하게 작성한 경우 비교, module의 '*'나 'as'에 관해 작성돼 있습니다.

----

## flux-utils에 관하여(일본어)
[gist.github.com/azu/e0274b703ef97226b0db](https://gist.github.com/azu/e0274b703ef97226b0db "flux-utils에 관하여")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">JavaScript</span></p>

Facebook의 flux 모듈에 추가된 utils에 관해 작성돼 있습니다. 
지금까지는 구현체가 Dispatcher 뿐이었지만 Store와 React Component를 연결하기 위한 Container 등 새롭게 제공하는 기능을 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 프론트엔드 MVC와 Flux // Speaker Deck(일본어)
[speakerdeck.com/sangotaro/hurontoendomvctoflux](https://speakerdeck.com/sangotaro/hurontoendomvctoflux "프론트엔드 MVC와Flux // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flux</span> <span class="jser-tag">슬라이드</span></p>

Flux란 무엇인지에 관한 슬라이드 입니다. 기존의 MVC와 무엇이 다르고 무엇이 같은지 알기 쉽게 작성돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## mdast - markdown processor powered by plug-ins
[mdast.js.org/](http://mdast.js.org/ "mdast - markdown processor powered by plug-ins")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Markdown 파서인 mdast의 사이트입니다. 플러그인을 사용해 Markdown을 HTML으로 변환할 수 있고, Lint 등 여러가지 기능이 생겼습니다.

----

## Perf.Rocks
[perf.rocks/](http://perf.rocks/ "Perf.Rocks")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">정리</span></p>

웹 성능에 관한 문서나 사람, 슬라이드, 영상, 도서 등이 요약 정리돼있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Relay | A JavaScript framework for building data-driven React applications
[facebook.github.io/relay/](https://facebook.github.io/relay/ "Relay | A JavaScript framework for building data-driven React applications")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">facebook</span></p>

GraphQL을 사용해 데이터를 주고 받는 프레임워크입니다. Relay.QL 등 ES6 Template literal을 전제로 개발돼 있어 재미있습니다.

- [Relay Technical Preview | React](https://facebook.github.io/react/blog/2015/08/11/relay-technical-preview.html "Relay Technical Preview | React")

----

## patrick-steele-idem/morphdom
[github.com/patrick-steele-idem/morphdom](https://github.com/patrick-steele-idem/morphdom "patrick-steele-idem/morphdom")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">library</span></p>

Virtual DOM이 아니라 DOM을 사용해 diff/patch를 하여 DOM Node를 변경하는 라이브러리입니다. `virtual-dom`과 비교한 벤치마크 결과도 소개하고 있습니다.

----

## jamesshore/quixote
[github.com/jamesshore/quixote](https://github.com/jamesshore/quixote "jamesshore/quixote")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

mocha 등 조합하여 사용할 수 있는 CSS 유닛 테스트 assertion 라이브러리입니다.

----

## scottcorgan/immu
[github.com/scottcorgan/immu](https://github.com/scottcorgan/immu "scottcorgan/immu")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Immutable Object를 다루는 라이브러리입니다. Object.defineProperty나 Object.freeze를 사용해 Array나 Object의 변경을 방지하는 객체를 생성합니다.

----
<h1 class="site-genre">도서</h1>

----

## Designing for Performance by Lara Callender Hogan
[designingforperformance.com/](http://designingforperformance.com/ "Designing for Performance by Lara Callender Hogan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">book</span></p>

브라우저의 성능에 관한 서적입니다.

----
