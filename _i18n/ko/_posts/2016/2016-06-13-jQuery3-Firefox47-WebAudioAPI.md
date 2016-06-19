---
title: "2016-06-13 JS: jQuery 3.0, Firefox 47.0, Web Audio API 입문"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-06-13T15:30
category: JSer
tags:
    - Firefox
    - jQuery
    - WebAudioAPI

---

JSer.info #283 - [jQuery 3.0](http://blog.jquery.com/2016/06/09/jquery-3-0-final-released/ "jQuery 3.0")가 정식으로 릴리즈됐습니다.

3.0에는 몇가지 호환되지 않는 부분이 포함돼 있으며 jQuery 1.x이나 2.x에서 업데이트하는 경우 참고할 수 있는 문서도 공개됐습니다.
기본적으로 [jQuery Migrate](https://github.com/jquery/jquery-migrate "jQuery Migrate")라는 마이그레이션용 플러그인을 넣어 경고를 출력하고, 경고에 해당하는 코드를 수정하는 방법으로 업데이트해 나갑니다.

- [jQuery Core 3.0 Upgrade Guide | jQuery](http://jquery.com/upgrade-guide/3.0/ "jQuery Core 3.0 Upgrade Guide | jQuery")
- [【번역정리】jQuery 3.0 업그레이드 가이드 - Qiita](http://qiita.com/fmy/items/345a264a1cf2e2a73f62)(일본어)

또, jQuery 3 릴리즈와 동시에 `ajax`와 `effect`를 제거한 [slim 빌드 버전](https://code.jquery.com/jquery-3.0.0.slim.js)도 함께도 공개됐습니다.

----

[Firefox 47](https://www.mozilla.jp/firefox/47.0/releasenotes/ "Firefox 47")이 릴리즈됐습니다.

Widevine CDM(DRM스트리밍) 지원, Service Worker/Push API 기능 개선, `about:debugging` 추가, ES2017의 ` Object.values()`와 `Object.entries()`를 구현하는 등 다양한 변경 사항이 있습니다.

개발자 도구와 관련된 변경 사항은 아래 문서에 잘 정리돼 있습니다.

- [Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog](https://hacks.mozilla.org/2016/03/developer-edition-47-user-agent-emulation-popup-debugging-and-more/ "Developer Edition 47 – User agent emulation, popup debugging and more ★ Mozilla Hacks – the Web developer blog")

----

[web audio lesson](http://mohayonao.github.io/web-audio-lesson/ "web audio lesson")(일본어)에는 Web Audio API의 기본적인 개념부터 응용하는 방법까지를 레슨 방식으로 소개하고 있습니다.

- [web-audio-lesson : Web Audio API 초심자 용 문서를 작성했습니다 - 소리 나는 블로그](http://mohayonao.hatenablog.com/entry/2016/06/12/154735 "web-audio-lesson : Web Audio API 초심자 용 문서를 작성했습니다 - 소리가 나는 블로그")

작성돼 있는 예제 코드를 브라우저 내에서 바로 실행해 볼 수 있도록 돼 있으며, 각각의 레슨마다 과제가 부여돼 있습니다.
Web Audio API에 관심있는 사람에게 좋은 자료가 될 것 같습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## jQuery 3.0 Final Released! | Official jQuery Blog
[blog.jquery.com/2016/06/09/jquery-3-0-final-released/](http://blog.jquery.com/2016/06/09/jquery-3-0-final-released/ "jQuery 3.0 Final Released! | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 3.0이 릴리즈 됐습니다.
ajax와 effect를 제거한 slim 빌드 버전이 공개됐습니다.
`jQuery.Deferred`가 Promise A/+를 호환하도록 변경됐고, 비권장 이벤트가 삭제됐습니다. 또, 다시 `requestAnimationFrame`를 이용하도록 변경하는 등 다양한 변경 사항이 있습니다.

- [jQuery Core 3.0 Upgrade Guide | jQuery](http://jquery.com/upgrade-guide/3.0/ "jQuery Core 3.0 Upgrade Guide | jQuery")
- [jquery/jquery-migrate: APIs and features removed from jQuery core](https://github.com/jquery/jquery-migrate#migrate-older-jquery-code-to-jquery-30 "jquery/jquery-migrate: APIs and features removed from jQuery core")
- [【번역정리】jQuery 3.0 업데이트 가이드 - Qiita](http://qiita.com/fmy/items/345a264a1cf2e2a73f62 "【번역정리】jQuery 3.0 업데이트 가이드 - Qiita - Qiita")(일본어)

----

## Firefox 47.0 릴리즈 노트
[www.mozilla.jp/firefox/47.0/releasenotes/](https://www.mozilla.jp/firefox/47.0/releasenotes/ "Firefox 47.0 リリースノート")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 47이 릴리즈됐습니다.
Widevine CDM(DMR스트리밍) 지원, Service Worker/Push API의 디버깅 기능 개선, `about:debugging` 추가, ES2017의 ` Object.values()`와 `Object.entries()`를 구현하는 등 다양한 변경 사항이 있습니다.

- [Mozilla To Test Widevine CDM in Firefox Nightly | Future Releases](https://blog.mozilla.org/futurereleases/2016/04/08/mozilla-to-test-widevine-cdm-in-firefox-nightly/ "Mozilla To Test Widevine CDM in Firefox Nightly | Future Releases")
- [Firefox 47 for developers - Mozilla | MDN](https://developer.mozilla.org/ja/Firefox/Releases/47 "Firefox 47 for developers - Mozilla | MDN")
- [Firefox 47 사이트 호환성 정보 | Firefox 사이트 호환성 정보](https://www.fxsitecompat.com/ja/versions/47/ "Firefox 47 사이트 호환성 정보 | Firefox 사이트 호환성 정보")(일본어)
- [Firefox 47 릴리즈, CSS Mask Image 프로퍼티 대응 및 VP9 코덱 활성화 등 | WWW WATCH](https://hyper-text.org/archives/2016/06/firefox_47_release.shtml "Firefox 47 릴리즈, CSS Mask Image 프로퍼티 대응 및 VP9 코덱 활성화 등 | WWW WATCH")(일본어)

----

## Release v6.10.0 · babel/babel
[github.com/babel/babel/releases/tag/v6.10.0](https://github.com/babel/babel/releases/tag/v6.10.0 "Release v6.10.0 · babel/babel")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 6.10.0이 릴리즈됐습니다.
`--watch` 시, 최초엔 빌드하지 않는 `--skip-initial-build` 옵션이 추가됐고, 버그 수정 등이 이뤄졌습니다.

----

## ESLint v2.12.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/06/eslint-v2.12.0-released](http://eslint.org/blog/2016/06/eslint-v2.12.0-released "ESLint v2.12.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v2.12.0이 릴리즈 됐습니다.
JSCS 호환 규칙 추가, 모든 빌트인 규칙을 불러오는 `eslint:all` 설정 추가, 성능 개선이 이뤄졌습니다.

- [Utilize glob ignore option for massive perf win by samccone · Pull Request #6215 · eslint/eslint](https://github.com/eslint/eslint/pull/6215 "Utilize glob ignore option for massive perf win by samccone · Pull Request #6215 · eslint/eslint")
- [ESLint v2.12.0 - Qiita](http://qiita.com/mysticatea/items/7bf844b32f8295eeb061 "ESLint v2.12.0 - Qiita")(일본어)

----

## Release Notes for Safari Technology Preview 6 | WebKit
[webkit.org/blog/6531/release-notes-for-safari-technology-preview-6/](https://webkit.org/blog/6531/release-notes-for-safari-technology-preview-6/ "Release Notes for Safari Technology Preview 6 | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 6가 릴리즈됐습니다.
함수의 인수에 trailing commas 드래프트를 지원하고, CSS의 `normal` 속성 값을 지원합니다.

- [Trailing Commas in Function Param Lists](https://jeffmo.github.io/es-trailing-function-commas/ "Trailing Commas in Function Param Lists")

----

## Dev.Opera — What’s new in Chromium 51 and Opera 38
[dev.opera.com/blog/opera-38/](https://dev.opera.com/blog/opera-38/ "Dev.Opera — What’s new in Chromium 51 and Opera 38")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 38(based on Chromium 51)이 릴리즈됐습니다.
ES6 `Symbol.hasInstance`와 `Symbol.species` 지원, 함수식에 `fn.name` 속성 대응, `querySelector`의 반환 값이 iterable로 변경、`KeyboardEvent#key` 지원 등 다양한 변경 사항이 있습니다.

----

## Chromium Blog: Chrome 52 Beta: CSS containment, simpler performance measurement, streamable responses from service workers, and more options for web push
[blog.chromium.org/2016/06/chrome-52-beta-css-containment-simpler.html](http://blog.chromium.org/2016/06/chrome-52-beta-css-containment-simpler.html "Chromium Blog: Chrome 52 Beta: CSS containment, simpler performance measurement, streamable responses from service workers, and more options for web push")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 52 Beta가 릴리즈됐습니다.
CSS `contain` 프로퍼티와 `PerformanceObserver` 지원하며 Fetch API가 referrer policy를 지원하도록 변경됐고 meta 태그의 `X-Frame-Option`을 더이상 지원하지 않습니다.

- [CSS Containment in Chrome 52 | Web Updates - Google Developers](https://developers.google.com/web/updates/2016/06/css-containment "CSS Containment in Chrome 52 | Web Updates - Google Developers")
- [Fetch Referrer Policy Sample](https://googlechrome.github.io/samples/fetch-api/fetch-referrer-policy.html "Fetch Referrer Policy Sample")
- [CSS Containment Module Level 3 (일본어버전)](https://triple-underscore.github.io/css-containment-ja.html "CSS Containment Module Level 3 (일본어버전)")

----
<h1 class="site-genre">아티클</h1>

----

## Open Sourcing CloudFlare’s UI Framework
[blog.cloudflare.com/cf-ui/](http://blog.cloudflare.com/cf-ui/ "Open Sourcing CloudFlare’s UI Framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

작은 사이즈의 React Component를 monorepo로 관리하고 공개하는 방법을 이야기합니다.
컴포넌트의 크기(입도), 테스트 방법, 디버그, 접근성 등에 관해 작성돼 있습니다.

----

## DOM Features You Didn’t Know Existed (Video &amp; Slides) | Impressive Webs
[www.impressivewebs.com/dom-features-you-didnt-know-existed-video-slides/](https://www.impressivewebs.com/dom-features-you-didnt-know-existed-video-slides/ "DOM Features You Didn’t Know Existed (Video & Slides) | Impressive Webs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span></p>

여러가지 DOM API를 소개하는 문서입니다.

----

## Passive Event Listeners을 이용해 스크롤 개선 | blog.jxck.io(일본어)
[blog.jxck.io/entries/2016-06-09/passive-event-listeners.html](https://blog.jxck.io/entries/2016-06-09/passive-event-listeners.html "Passive Event Listeners을 이용해 스크롤 개선 | blog.jxck.io")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span></p>

`addEventListener(type, handler, options)`의 세번쨰 인수로 추가된 `passive` 옵션에 관해 이야기합니다.
`passive: true`로 설정한 경우의 효과, 세번째 인수를 Feature detect 방법 등을 소개합니다.

- [addEventListener()의 세번째 인수의 의미를 제대로 이해하기 위한 메모 - 오늘도 스미마셍](http://d.hatena.ne.jp/snaka72/20100925/1285404467 "addEventListener()의 세번째 인수의 의미를 제대로 이해하기 위한 메모 - 오늘도 스미마셍")
- [Add feature test for passive event listener support · Issue #1894 · Modernizr/Modernizr](https://github.com/Modernizr/Modernizr/issues/1894 "Add feature test for passive event listener support · Issue #1894 · Modernizr/Modernizr")

----

## Performance Observer - Efficient Access to Performance Data | Web Updates - Google Developers
[developers.google.com/web/updates/2016/06/performance-observer](https://developers.google.com/web/updates/2016/06/performance-observer "Performance Observer - Efficient Access to Performance Data | Web Updates - Google Developers")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">API</span> <span class="jser-tag">performance</span></p>

`PerformanceObserver`에 관해 설명하는 아티클입니다.
브라우저가 idle 일때 비동기로 Timing 정보를 얻을 수 있습니다.

----

## Memory Debugging with Web Inspector | WebKit
[webkit.org/blog/6425/memory-debugging-with-web-inspector/](https://webkit.org/blog/6425/memory-debugging-with-web-inspector/ "Memory Debugging with Web Inspector | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webkit</span> <span class="jser-tag">safari</span> <span class="jser-tag">debug</span></p>

Safari TP(Technology Preview) 버전에 공개된 새로운 메모리 프로퍼일러에 관해 소개합니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Practical React with MobX - YouTube
[www.youtube.com/watch?v=XGwuM\_u7UeQ](https://www.youtube.com/watch?v=XGwuM_u7UeQ "Practical React with MobX - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">영상</span> <span class="jser-tag">library</span></p>

MobX에 관한 스크린캐스트 입니다.
MobX를 사용해 어떻게 State를 관리하는지, 어떠 사이클로 상태 변화를 표현하는지에 관해 설명합니다.

- [mobxjs/mobx: Simple, scalable state management.](https://github.com/mobxjs/mobx "mobxjs/mobx: Simple, scalable state management.")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## web audio lesson
[mohayonao.github.io/web-audio-lesson/](http://mohayonao.github.io/web-audio-lesson/ "web audio lesson")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">web </span> <span class="jser-tag">audio</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">document</span></p>

Web Audio API의 기초부터 응용까지 과제와 함께 배울 수 있는 튜토리얼입니다.
예제 코드를 브라우저에서 바로 실행할 수 있도록 구성돼 있습니다.

- [web-audio-lesson : Web Audio API 초심자 용 문서를 작성했습니다 - 소리 나는 블로그](http://mohayonao.hatenablog.com/entry/2016/06/12/154735 "web-audio-lesson : Web Audio API 초심자 용 문서를 작성했습니다 - 소리 나는 블로그")(일본어)

----

## npms
[npms.io/](https://npms.io/ "npms")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">검색</span></p>

백엔드에 Elasticsearch를 사용한 npm 패키지 검색 서비스입니다.
검색 결과에 Quality, Maintenance, Popularity, Personalities(미구현) 지표도 함께 출력합니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## airbnb/hypernova: A service for server-side rendering your JavaScript views
[github.com/airbnb/hypernova](https://github.com/airbnb/hypernova "airbnb/hypernova: A service for server-side rendering your JavaScript views")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">rails</span></p>

Airbnb의 React 서버 사이드 렌더링 모듈입니다.
Rails 환경에서 사용할 수 있는 방법도 공개돼 있습니다.

----

## Kakapo.js
[devlucky.github.io/kakapo-js](http://devlucky.github.io/kakapo-js "Kakapo.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

HTTP 목(Mock) 라이브러리입니다.
목 데이터를 가지는 개발 서버를 만들 수 있는 라이브러리입니다.

----

## rill-js/rill: Isomorphic web application framework.
[github.com/rill-js/rill](https://github.com/rill-js/rill "rill-js/rill: Isomorphic web application framework.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">browser</span> <span class="jser-tag">node.js</span></p>

Browser, Node.js에서 동작하는 isomorphic한 HTTP 미들웨어 라이브러리입니다.

----

## benjamn/reify: Enable ECMAScript 2015 modules in Node today. No caveats. Full stop.
[github.com/benjamn/reify](https://github.com/benjamn/reify "benjamn/reify: Enable ECMAScript 2015 modules in Node today. No caveats. Full stop.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

ECMAScript module을 Node.js로 런타임 변환하는 도구입니다.

----
<h1 class="site-genre">도서</h1>

----

## CSS시크릿 - 웹디자이너가 알아야 할 47가지 키포인트 : Lea Verou, 마키노 사토시 : 책 : Amazon.co.jp(일본어)
[www.amazon.co.jp/CSS%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88-%E2%80%95%E3%82%A6%E3%82%A7%E3%83%96%E3%83%87%E3%82%B6%E3%82%A4%E3%83%8A%E3%83%BC%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D47%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-Lea-Verou/dp/4873117666](http://www.amazon.co.jp/CSS%E3%82%B7%E3%83%BC%E3%82%AF%E3%83%AC%E3%83%83%E3%83%88-%E2%80%95%E3%82%A6%E3%82%A7%E3%83%96%E3%83%87%E3%82%B6%E3%82%A4%E3%83%8A%E3%83%BC%E3%81%8C%E7%9F%A5%E3%82%8B%E3%81%B9%E3%81%8D47%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88-Lea-Verou/dp/4873117666 "CSSシークレット ―ウェブデザイナーが知るべき47のキーポイント : Lea Verou, 牧野 聡 : 本 : Amazon.co.jp")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

2016년 6월 25일 출간되는 CSS Secrets의 번역서입니다.

- [CSS Secrets - O&amp;#39;Reilly Media](http://shop.oreilly.com/product/0636920031123.do "CSS Secrets - O&amp;#39;Reilly Media")

----
