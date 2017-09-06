---
title: "2017-09-05 JS: Headless Browser 대응, Browserify 재개"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2017-09-05T01:20:45.284Z
category: JSer
tags:
- browser
- firefox
- Chrome
- headless
- browserify

---

JSer.info #347 - Firefox Headless 모드에 관한 문서가 공개됐습니다.

- [Headless mode - Mozilla | MDN](https://developer.mozilla.org/en-US/Firefox/Headless_mode "Headless mode - Mozilla | MDN")

Firefox의 Headless 모드는 Linux 환경에서는 Firefox 55 부터 Mac/Windows 환경에서는 56(현재의 Nightly 버전)부터 동작합니다.

Chrome도 Mac/Linux는 Chrome 59 부터 Windows는 Chrome 60부터 Headless 모드를 사용할 수 있습니다.

과거 [2017-05-03 JS: Headless Chrome/Firefox와 PhantomJS/SlimerJS, ES modules - JSer.info](https://jser.info/ko/2017/05/03/headless-chromefirefoxphantomjsslimerjs-es-modules/ "2017-05-03のJS: Headless Chrome/FirefoxとPhantomJS/SlimerJS、ES modules - JSer.info")에서 정리한 Headless 대응 상황은 다음과 같습니다.

<script src="https://gist.github.com/azu/c4206d94f18f35f6fe2fe303f988e7d5.js"></script>

Firefox는 [selenium-webdriver](https://www.npmjs.com/package/selenium-webdriver "selenium-webdriver")를 사용한 예가 소개돼 있습니다.
Chrome은 Chrome 팀이 공개한 [Puppeteer](https://github.com/GoogleChrome/puppeteer "Puppeteer")을 시작으로 [Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD](https://medium.com/@kensoh/chromeless-chrominator-chromy-navalia-lambdium-ghostjs-autogcd-ef34bcd26907 "Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD") 등 다양한 라이브러리가 공개돼 있습니다.

[NickJS](https://nickjs.org/ "NickJS | The Modern Headless Browser Library") 처럼 PhantomJS에서 Headless Chrome으로 환경을 옮기는 도구도 나오고 있습니다.

- [Web Scraping in 2017: Advanced Headless Chrome Tips & Tricks](https://blog.phantombuster.com/web-scraping-in-2017-headless-chrome-tips-tricks-4d6521d695e8 "Web Scraping in 2017: Advanced Headless Chrome Tips &amp; Tricks")

----

Browserify가 `substack/node-browserify`에서 [browserify/browserify](https://github.com/browserify/browserify "browserify/browserify")의 organization로 옮겨짐과 동시에 다음과 같은 Issue를 생성하여 협력을 구하고 있습니다.

- [help wanted · Issue #5 · browserify/discuss](https://github.com/browserify/discuss/issues/5 "help wanted · Issue #5 · browserify/discuss")

[JSer레포트 #1 Bundler의 미래, 테스트 프레임워크의 현황 - JSer.info](https://jser.info/2017/01/31/bundler-testing-framework-report/ "JSer레포트 #1 Bundler의 미래, 테스트 프레임워크의 현황 - JSer.info")(일본어)에서 전해드린 것과 같이 Browserify의 개발은 정체돼 있었습니다.
현재 Browserify는 CommonJS를 기반으로한 Bundler 이기 때문에 향후 [.mjs](https://blog.jxck.io/entries/2017-08-15/universal-mjs-ecosystem.html ".mjs")(일본어) 등을 지원해야할 상황에 대비할 필요성을 근거로 현재의 에코시스템을 정리 하고 있습니다.

이 Issue를 시작으로 [browserify/admin: administrative procedures for the browserify org](https://github.com/browserify/admin "browserify/admin: administrative procedures for the browserify org")와 같은 커뮤니티용 문서를 공개하고 지금까지 각기 저장소에 있던 `*fy` 패키지를 <https://github.com/browserify>에 한데 모으고 있습니다.

Browserify에 의견이 있는 사람은 이 Issue 게시판에 이슈를 생성하면 좋을 것 같네요.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">if you want to help out the browserify ecosystem, there&#39;s a new help wanted thread <a href="https://t.co/nB98TS5Cls">https://t.co/nB98TS5Cls</a></p>&mdash; substack (@substack) <a href="https://twitter.com/substack/status/902644080445874177">August 29, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing TypeScript 2.5 | TypeScript
[blogs.msdn.microsoft.com/typescript/2017/08/31/announcing-typescript-2-5/](https://blogs.msdn.microsoft.com/typescript/2017/08/31/announcing-typescript-2-5/ "Announcing TypeScript 2.5 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 2.5가 릴리즈됐습니다.
Optinal-catch-binding과 `--preserveSymlinks`를 지원하고 에디터 연동 및 중복/alias 패키지의 취급 방식이 개선됐습니다.

- [Typescript 2.5 릴리즈 - abcdefGets](http://abcdef.gets.b6n.ch/entry/2017/09/01/143601 "Typescript 2.5 릴리즈 - abcdefGets")(일본어)

----

## Ember.js - Ember 2.15 and 2.16 Beta Released
[emberjs.com/blog/2017/09/01/ember-2-15-released.html](https://emberjs.com/blog/2017/09/01/ember-2-15-released.html "Ember.js - Ember 2.15 and 2.16 Beta Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 2.15가 릴리즈됐습니다.
`Ember.Router`의 슈퍼-셋인 `router` service를 공개가 공개됐습니다.

----

## Concurrent JavaScript: It can work! | WebKit
[webkit.org/blog/7846/concurrent-javascript-it-can-work/](https://webkit.org/blog/7846/concurrent-javascript-it-can-work/ "Concurrent JavaScript: It can work! | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webkit</span></p>

`SharedArrayBuffer`가 추가되며 이를 이용해 JavaScript에서 Thread를 지원할 경우에 어떤 형태가 될지 생각해볼 수 있는 글입니다.
현재의 JavaScript VM은 싱글 스레드 이용하고 있으며 멀티 스테드의 경우의 VM 성능 등에 관해 이야기합니다.

----

## 🏁 Release: Iteration 10 – 10th developer preview · Issue #177 · ckeditor/ckeditor5-design
[github.com/ckeditor/ckeditor5-design/issues/177](https://github.com/ckeditor/ckeditor5-design/issues/177 "🏁 Release: Iteration 10 – 10th developer preview · Issue #177 · ckeditor/ckeditor5-design")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CKEditor 5 v0.10.0이 릴리즈됐습니다.
MSEdge 지원, 툴-팁 메뉴 및 클립보드 기능 등이 개선됐습니다.

- [CKEditor 5 Developer Preview (v0.10.0)](https://ckeditor5.github.io/ "CKEditor 5 Developer Preview (v0.10.0)")
- [CKEditor 5 – Roadmap to 1.0.0 and beyond · Issue #172 · ckeditor/ckeditor5-design](https://github.com/ckeditor/ckeditor5-design/issues/172 "CKEditor 5 – Roadmap to 1.0.0 and beyond · Issue #172 · ckeditor/ckeditor5-design")

----
<h1 class="site-genre">아티클</h1>

----

## What's New In DevTools (Chrome 62)  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/08/devtools-release-notes](https://developers.google.com/web/updates/2017/08/devtools-release-notes "What's New In DevTools (Chrome 62)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 62의 개발자 도구의 변경 사항이 소개돼 있습니다.
Top-level `await`을 콘솔에서 이용 가능하며 특정 노드를 스크린샷으로 찍을 수 기능과 CSS Grid의 하일라이트를 지원하고 콘솔 필터가 개선됐습니다.
또 HAR을 import할 수 있도록 개선 됐고 캐쉬 데이터를 열어볼 수 있도록 변경됐습니다.

----

## Form Validation with Web Audio | CSS-Tricks
[css-tricks.com/form-validation-web-audio/](https://css-tricks.com/form-validation-web-audio/ "Form Validation with Web Audio | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

Web Audio API와 폼 벨리데이션의 조합에 대해 이야기합니다.

----

## Measuring performance gains — AngularJS to React (with Redux or Mobx)
[medium.com/@guptagaruda/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455](https://medium.com/@guptagaruda/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455 "Measuring performance gains — AngularJS to React (with Redux or Mobx)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Angular</span></p>

세 가지 벤치 마킹 앱을 이용해 Angular 1.x와 React/Redux/Mobx를 비교한 글입니다. 현재도 많은 엔터프라이즈 애플리케이션이 Angular 1.x로 동작하고 있으며 만약 React로 이전할 때 어떤 장점이 있는지 살펴보는 것을 목적으로 하고 있습니다.

----

## Decaffeinating a Large CoffeeScript Codebase Without Losing Sleep · DataFox Tech Blog
[eng.datafox.com/javascript/2017/07/18/decaffeinating-large-coffeescript-codebase/](http://eng.datafox.com/javascript/2017/07/18/decaffeinating-large-coffeescript-codebase/ "Decaffeinating a Large CoffeeScript Codebase Without Losing Sleep · DataFox Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CoffeeScript</span> <span class="jser-tag">JavaScript</span></p>

bulk-decaffeinate를 사용해 CoffeeScript에서 JavaScript로 이전하는 방법과 순서에 대해 작성돼 있습니다.

----

## React + RxJSで始める状態管理 - VOYAGE GROUP techlog
[techlog.voyagegroup.com/entry/2017/08/31/102915](http://techlog.voyagegroup.com/entry/2017/08/31/102915 "React + RxJSで始める状態管理 - VOYAGE GROUP techlog")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">almin</span> <span class="jser-tag">設計</span></p>

Write 레이어와 Read 레이어를 분리하여 얻을 수 있는 장점과 단점에 대해 작성돼 있습니다. 책임을 분리하여 복잡성을 낮추고 의존을 국소화하는 방안에 대해 이야기합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Headless mode - Mozilla | MDN
[developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless\_mode](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode "Headless mode - Mozilla | MDN")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">document</span></p>

Firefox의 headless mode에 대한 소개 글입니다.

----

## Rendering on Google Search  |  Search  |  Google Developers
[developers.google.com/search/docs/guides/rendering](https://developers.google.com/search/docs/guides/rendering "Rendering on Google Search  |  Search  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">browser</span></p>

Google Search Bot의 렌더링 서브 시스템에서 이용하고 있는 Chrome의 버전이나 지원하지 않는(Disable돼 있는) 기능에 관해 작성돼 있습니다.
현시점(2017년 9월 4일) 에서는 Chrome 4을 기반으로 하고 있습니다.

- [방일한 Google 게리에 마음껏 물어봤다 ―― 프로젝트 OWL, 검색 애널리틱스, PWA, etc. #inhouseseo | 해외 SEO 정보 블로그](https://www.suzukikenichi.com/blog/ama-with-gary/amp/ "방일한 Google 게리에 마음껏 물어봤다 ―― 프로젝트 OWL, 검색 애널리틱스, PWA, etc. #inhouseseo | 해외 SEO 정보 블로그")(일본어)

----

## Kea vs setState, Redux, Mobx, Dva, JumpState, Apollo, etc.
[medium.com/@mariusandra/kea-vs-setstate-redux-mobx-dva-jumpstate-apollo-etc-4aa26ea11d02](https://medium.com/@mariusandra/kea-vs-setstate-redux-mobx-dva-jumpstate-apollo-etc-4aa26ea11d02 "Kea vs setState, Redux, Mobx, Dva, JumpState, Apollo, etc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">redux</span></p>

React 용 상태 관리 라이브러리 Kea를 소개한 글입니다.

- [Kea](https://kea.js.org/ "Kea")

----

## help wanted · Issue #5 · browserify/discuss
[github.com/browserify/discuss/issues/5](https://github.com/browserify/discuss/issues/5 "help wanted · Issue #5 · browserify/discuss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browserify</span> <span class="jser-tag">issue</span></p>

browserify의 issue와 향후 로드맵(ES Module나 hmr 등)에 관해 이야기합니다.
이제 각각의 `*ify` 패키지를 browserify organization에 옮겨 한데 정리하여 관리합니다.

----

## phantombuster/nickjs: Web scraping library made by the Phantombuster team. Modern, simple & works on all websites.
[github.com/phantombuster/nickjs](https://github.com/phantombuster/nickjs "phantombuster/nickjs: Web scraping library made by the Phantombuster team. Modern, simple & works on all websites.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span></p>

Headless Chrome과 PhantomJS를 지원하는 웹 스크래핑 라이브러리입니다.

- [Phantombuster: API-fy the Web](https://phantombuster.com/ "Phantombuster: API-fy the Web")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## react-tools/react-move: React Move 🌀 Beautiful, data-driven animations for React
[github.com/react-tools/react-move](https://github.com/react-tools/react-move "react-tools/react-move: React Move 🌀 Beautiful, data-driven animations for React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">animation</span> <span class="jser-tag">library</span></p>

React에서 데이터 주도적으로 애니메이션을 처리 할 수 있도록 지원하는 라이브러립니다.

----

## lukechilds/keyv: Simple key-value store with support for multiple backends
[github.com/lukechilds/keyv](https://github.com/lukechilds/keyv "lukechilds/keyv: Simple key-value store with support for multiple backends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

Redis, MySQL 등 다양한 백엔드 환경을 지원하는 단순한 KVS 라이브러리입니다.
Map 적인 API를 구현한 adpter를 사용하여 백엔드 환경을 변경할 수 있습니다.

----
<h1 class="site-genre">도서</h1>

----

## React for Real - O'Reilly Media
[shop.oreilly.com/product/9781680502633.do](http://shop.oreilly.com/product/9781680502633.do "React for Real - O'Reilly Media")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span></p>

React를 다루는 도서입니다.

----

## New Javascript Books
[newjavascriptbooks.com/](https://newjavascriptbooks.com/ "New Javascript Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScript를 주제로한 신간 서적이 정리돼 있는 사이트입니다.

----
