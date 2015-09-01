---
title: "2015-08-24의 JS: Bootstrap 4α、PostCSS 5.0、Node.js와 io.js"
author: azu
layout: post
date : 2015-08-24T22:00
translator: U-Yeong Ju
category: JSer
tags:
    - CSS
    - bootstrap
    - Node.js
    - io.js
    - community

---

JSer.info #242 - CSS 프레임워크인 Bootstrap 4 alpha 가 릴리즈됐습니다.

- [Bootstrap 4 alpha · Bootstrap Blog](http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/ "Bootstrap 4 alpha · Bootstrap Blog")

메이저 업데이트인 4의 알파 버전입니다. Bootstrap 기반 언어가 Less에서 Sass로 변경됐습니다.

IE8의 지원을 종료했고, `rem`을 기본 단위로 이용하도록 됐으며, flexbox를 옵션으로 이용 할 수 있습니다.
wells나 thumbnails, panels의 컴포넌트는 폐지되고 cards에 통합됩니다.

또 플러그인을 ES6로 재작성하여 UMD 모듈로 제공할 수 있도록 변경됐고, 노멀라이즈를 [Reboot](http://v4-alpha.getbootstrap.com/content/reboot/ "Reboot")로 정리하는 등 다양한 변경사항이 있습니다.

동시에 [Bootstrap Themes](http://themes.getbootstrap.com/ "Bootstrap Themes")라고 하는 Bootstrap의 테마를 다루는 공식 사이트도 공개됐습니다.

----

CSS의 포스트 프로세서를 빌드하는 기반 도구인 [PostCSS 5.0](https://github.com/postcss/postcss/releases/tag/5.0.0 "PostCSS 5.0")이 릴리즈 됐습니다. PostCSS는 Autoprefixer로 유명한 Andrey Sitnik가 개발하고 있습니다.

파서 부분을 옵셔널화 했으며 [SCSS parser](https://github.com/postcss/postcss-scss "SCSS parser")를 사용하여 CSS 뿐만 아니라 SCSS도 파서 가능하도록 변경됐습니다.

PostCSS에 관해서는 [PostCSS는 무엇인가 // Speaker Deck 슬라이드](https://speakerdeck.com/jmblog/postcss-tohahe-ka "PostCSS란 무엇인가 // Speaker Deck")(일본어)에 잘 정리돼 있습니다. CSS 중심적인 도구에 흥미가 있는 사람에게 좋은 자료가 될 것 같습니다.

----

[어떻게 이렇게 된 것일까? Node.js와 io.js의 분열과 통합의 미래, 이제부터 어떻게 진화할까? // Speaker Deck](https://speakerdeck.com/yosuke_furukawa/dousitekounatuta-node-dot-jstoio-dot-jsfalsefen-lie-totong-he-falsexing-fang-korekaradoujin-hua-siteikufalseka "어떻게 이렇게 된 것일까? Node.js와 io.js의 분열과 통합의 미래, 이제부터 어떻게 진화할까? // Speaker Deck")(일본어) 슬라이드에서 Node.js의 역사, io.js가 왜 생겨났는지, 커뮤니티와 개발 체제, Node.js v4.0에서의 통합 등, Node.js 프로젝트에 관계된 소동에 관해 정리돼 있습니다.

- [YAPC::ASIA 2015에서 「어떻게 이렇게 된 것일까? Node.js와 io.js의 분열과 통합의 미래, 이제부터 어떻게 진화할까?」라는 주제로 발표했다. - from scratch](http://yosuke-furukawa.hatenablog.com/entry/2015/08/24/152147 "YAPC::ASIA 2015에서 「어떻게 이렇게 된 것일까? Node.js와 io.js의 분열과 통합의 미래, 이제부터 어떻게 진화할까?」라는 주제로 발표했다. - from scratch")(일본어)

또, [4.0 is the new 1.0 — Node & JavaScript — Medium](https://medium.com/node-js-javascript/4-0-is-the-new-1-0-386597a3436d "4.0 is the new 1.0 — Node & JavaScript — Medium")에서 Node.js와 io.js의 통합 과정 등에 관해 작성돼 있으니 참고하면 좋을 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Bootstrap 4 alpha · Bootstrap Blog
[blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/](http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/ "Bootstrap 4 alpha · Bootstrap Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 4α가 릴리드됐습니다.
Less에서 Sass로 전환, IE8 지원 종료, `rem` 단위 이용, flexbox를 옵셔널하게 이요할 수 있도록 변경됐고, 플러그인을 ES6로 재작성 했으며 재정의 스타일을 Reboot로 정리하는 등 다양한 변경 사항이 있습니다.

- [Bootstrap 4 alpha · Bootstrap Blog](http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/ "Bootstrap 4 alpha · Bootstrap Blog")

----

## Release 5.0 “President Valac” · postcss/postcss
[github.com/postcss/postcss/releases/tag/5.0.0](https://github.com/postcss/postcss/releases/tag/5.0.0 "Release 5.0 “President Valac” · postcss/postcss")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CSS의 변환을 처리하는 PostCSS 5.0이 릴리즈 됐습니다.
`safe` 옵션이 별도의 프로젝트로 옮겨졌고, `parser`나 `stringifier` 등도 옵셔널화 했습니다.
SCSS의 파서에도 대응하는 등 다양한 변경 사항이 있습니다.

----

## Release RxJS Version 3.1 · Reactive-Extensions/RxJS
[github.com/Reactive-Extensions/RxJS/releases/tag/v3.1.0](https://github.com/Reactive-Extensions/RxJS/releases/tag/v3.1.0 "Release RxJS Version 3.1 · Reactive-Extensions/RxJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span></p>

RxJS 3.1이 릴리즈됐습니다.
`resultSelector`가 옵션널하게 변경됐으며 TypeScript 정의 파일이 재작성 됐습니다.

----

## Release 1.1.0 - 2015.08.17 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v1.1.0](https://github.com/zloirock/core-js/releases/tag/v1.1.0 "Release 1.1.0 - 2015.08.17 · zloirock/core-js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core-js 1.1.0가 릴리즈됐습니다.
string padding의 제안을  수용했으며 trimLeft/trimRight가 추가됐고 Reflect.enumerate는 캐쉬된 key를 iterate 하도록 변경됐습니다.

- [Question about \[\[Enumerate\]\] and property decision timing](https://esdiscuss.org/topic/question-about-enumerate-and-property-decision-timing "Question about [[Enumerate]] and property decision timing")

----

## ESLint 1.2.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/08/eslint-1.2.0-released/](http://eslint.org/blog/2015/08/eslint-1.2.0-released/ "ESLint 1.2.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 1.2.0가 릴리즈됐습니다.
문자열 결합에 Template String을 사용을 유도하는 규칙, 콜백에 Array Function을 사용을 우선하는 규칙 등이 추가됐습니다. `commonjs`의 environment 정의가 추가됐습니다.
文字列結合にTemplate Stringsを使うようにするルール、コールバックにArrow Functionを優先するルールなどの追加、のenvironment定義が追加された

----
<h1 class="site-genre">아티클</h1>

----

## 하테나 북마크 검색을 만들어보면서 Flux Utils를 익히다  | Web Scratch(일본어)
[efcl.info/2015/08/24/flux-utils/](http://efcl.info/2015/08/24/flux-utils/ "하테나 북마크 검색을 만들어보면서 Flux Utils를 익히다  | Web Scratch(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Flux</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

Flux Utils와 React를 사용해 앱을 만들어보면서 Flux Utils를 익히는 튜토리얼입니다.
Store의 state가 Immutable인 것과 Container 등의 동작 방식을 이해할 수 있습니다.

----

## JavaScript의 이터레이터를 누리다 - Qiita(일본어)
[qiita.com/kura07/items/cf168a7ea20e8c2554c6](http://qiita.com/kura07/items/cf168a7ea20e8c2554c6 "JavaScript의 이터레이터를 누리다 - Qiita(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span></p>

Iterator, Iterable, Generator 각각이 무엇인지, 어떤시긍로 사용하는지 설명하고 있습니다.

----

## Proper testing of Angular JS applications with ES6 modules — Medium
[medium.com/@tomastrajan/proper-testing-of-angular-js-applications-with-es6-modules-8cf31113873f](https://medium.com/@tomastrajan/proper-testing-of-angular-js-applications-with-es6-modules-8cf31113873f "Proper testing of Angular JS applications with ES6 modules — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AngularJS</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

ES6 modules와 AngularJS.
ES6 modules로 로드하여 테스트하기 위해서는 어떤식으로 코드를 작성해야하는지 이야기합니다.

----

## reactjs - ES6 버전 React.js 튜토리얼 - Qiita(일본어)
[qiita.com/nownabe/items/2d8b92d95186c3941de0](http://qiita.com/nownabe/items/2d8b92d95186c3941de0 "reactjs - ES6 버전 React.js 튜토리얼 - Qiita(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">tutorial</span></p>

React의 튜토리얼을 ES6 Classes 등을 사용하여 작성한 경우 어떤 모습이 되는지 알 수 있도록 튜토리얼 형식으로 작성한 문서입니다.

- [튜토리얼 | React](http://reactkr.github.io/react/docs/tutorial-ko-KR.html "튜토리얼 | React")

----

## Vue.js Tutorial - Vegibit
[vegibit.com/vue-js-tutorial/](http://vegibit.com/vue-js-tutorial/ "Vue.js Tutorial - Vegibit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">tutorial</span></p>

Vue.js에 관한 튜토리얼입니다.
기본적인 사용방법, Vue.js의 Event、Filter、Components 등에 관해 작성돼 있습니다.

----

## Windows 10 virtual machines now available on Microsoft Edge Dev | Microsoft Edge Dev Blog
[blogs.windows.com/msedgedev/2015/08/17/windows-10-virtual-machines-now-available-on-microsoft-edge-dev/](http://blogs.windows.com/msedgedev/2015/08/17/windows-10-virtual-machines-now-available-on-microsoft-edge-dev/ "Windows 10 virtual machines now available on Microsoft Edge Dev | Microsoft Edge Dev Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">MSEdge</span> <span class="jser-tag">가상화</span></p>

MSEdge를 사용할 수 있는 Windows 10의 Virtual Machine(VM)이 공개됐습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## PostCSS란 무엇인가? // Speaker Deck(일본어)
[speakerdeck.com/jmblog/postcss-tohahe-ka](https://speakerdeck.com/jmblog/postcss-tohahe-ka "PostCSS란 무엇인가? // Speaker Deck(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">슬라이드</span></p>

PostCSS에 관한 슬라이드입니다.
PostCSS를 사용한 변환 시스템, 각각의 플러그인은 하나의 기능을 담당하고 있으므로 조합하여 사용할 수 있다고 설명하고 있습니다.
csssnext, PreCSS, cssnano 등의 플러그인 팩과 Sass 대신 이용하는 방법도 소개합니다.

----

## 어떻게 이렇게 된 것일까? Node.js와 io.js의 분열과 통합의 미래, 이제부터 어떻게 진화할까? // Speaker Deck(일본어)
[speakerdeck.com/yosuke\_furukawa/dousitekounatuta-node-dot-jstoio-dot-jsfalsefen-lie-totong-he-falsexing-fang-korekaradoujin-hua-siteikufalseka](https://speakerdeck.com/yosuke_furukawa/dousitekounatuta-node-dot-jstoio-dot-jsfalsefen-lie-totong-he-falsexing-fang-korekaradoujin-hua-siteikufalseka "どうしてこうなった？ Node.jsとio.jsの分裂と統合の行方。これからどう進化していくのか？ // Speaker Deck")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">역사</span></p>

Node.js의 역사ㅡ io.js가 출범하게된 원인 그리고 Node.js와 io.js가 통합하게된 경위에 대해서 소개합니다.
또, 커뮤니티의 오픈-거버넌스 모델에 관해서도 설명합니다.

----

## Effective ES6(일본어)
[www.slideshare.net/teppeis/effective-es6](http://www.slideshare.net/teppeis/effective-es6 "Effective ES6(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">슬라이드</span></p>

ES6에 관해 폭넓게 소개하는 슬라이드입니다.
ES5 이하에서 최선의 방법으로 작성했던 코드를 ES6의 기능이나 구문을 이용해 세련되게 표현할 수 있는 점과 새롭게 추가된 기능에 관해 작성돼 있습니다.

----

## Ginza.rb에서 Quipper의 싱글 페이지 애플리케이션 개발에 관해 발표했습니다 - @kyanny&#x27;s blog(일본어)
[blog.kyanny.me/entry/2015/08/20/014509](http://blog.kyanny.me/entry/2015/08/20/014509 "Ginza.rb에서 Quipper의 싱글 페이지 애플리케이션 개발에 관해 발표했습니다 - @kyanny&#x27;s blog(일본어)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">슬라이드</span> <span class="jser-tag">backbone.js</span></p>

Backbone.js/Chaplin/Marionette/React 각각의 싱글 페이지 애플리케이션 개발에서의 이점과 문제점 그리고 Rails와의 궁합에 관해서 설명하고 있습니다.

----

## Functional programming in JavaScript - YouTube
[www.youtube.com/playlist?list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84](https://www.youtube.com/playlist?list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84 "Functional programming in JavaScript - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">함수형 프로그래밍</span> <span class="jser-tag">영상</span></p>

함수형 JavaScript를 다루는 스크린캐스트입니다.

----
<h1 class="site-genre">사이트, 서비스, 도큐멘트</h1>

----

## Dev Tips - Developer Tips by Umar Hansa
[umaar.com/dev-tips/](https://umaar.com/dev-tips/ "Dev Tips - Developer Tips by Umar Hansa")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tips</span></p>

Chrome 개발자 도구의 팁 모음집

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Falcor: One Model Everywhere
[netflix.github.io/falcor/](http://netflix.github.io/falcor/ "Falcor: One Model Everywhere")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Netflix의 모델 + data fetch 라이브러리입니다.
JSON Graph로 데이터를 하나의 도메인 모델로써 표현하고, 그 모델을 기반으로 서버는 라우팅, 클라이언트는 데이터를 요청합니다.
또 클라이언트에서는 캐쉬를 설정할 수도 있습니다.

- [The Netflix Tech Blog: Netflix Releases Falcor Developer Preview](http://techblog.netflix.com/2015/08/falcor-developer-preview.html "The Netflix Tech Blog: Netflix Releases Falcor Developer Preview")
- [▶ Netflix JavaScript Talks - Falcor - YouTube](https://www.youtube.com/watch?v=z8UgDZ4rXBU "▶ Netflix JavaScript Talks - Falcor - YouTube")

----

## stylelint
[stylelint.io/](http://stylelint.io/ "stylelint")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

CSS의 Lint도구입니다.
PostCSS의 플러그인으로도 사용할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## JavaScript Domain-Driven Design | PACKT Books
[www.packtpub.com/web-development/javascript-domain-driven-design](https://www.packtpub.com/web-development/javascript-domain-driven-design "JavaScript Domain-Driven Design | PACKT Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScript에서의 DDD에 관해 설명한 책입니다.

----

## Beautiful JavaScript — Medium
[medium.com/@valueof/beautiful-javascript-8aa69998add0](https://medium.com/@valueof/beautiful-javascript-8aa69998add0 "Beautiful JavaScript — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Beautiful JavaScript가 출시됐습니다.

- [Beautiful JavaScript - O&#x27;Reilly Media](http://shop.oreilly.com/product/0636920030706.do "Beautiful JavaScript - O'Reilly Media")

----

## Amazon: AngularJS　애플리케이션 프로그래밍: 山田 祥寛(일본서적)
[www.amazon.co.jp/dp/4774175684](http://www.amazon.co.jp/dp/4774175684 "Amazon: AngularJS　애플리케이션 프로그래밍: 山田 祥寛(일본서적)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">AngularJS</span> <span class="jser-tag">book</span></p>

AngularJS에 관한 책입니다.

----
