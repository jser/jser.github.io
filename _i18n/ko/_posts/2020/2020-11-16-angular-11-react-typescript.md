---
title: "2020-11-16: Angular 11, React 앱 최적화, TypeScript를 채택(adopting)하고 배운것"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-11-16T00:28:55.656Z
category: JSer
tags:
- React
- Angular
- ESLint
- performance
- ECMAScript

---

JSer.info #514 -　Angular 11 릴리스.

- [Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog](https://blog.angular.io/version-11-of-angular-now-available-74721b7952f7)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#1100-2020-11-11)

Angular 11에서는 폰트 자동 인라인 화 대응, Component Test Harnesses 모든 컴포넌트 지원, Language Service 대응 개선, HMR을 CLI 인수로 활성화 할 수 있도록 변경됐다. 
그 외로 webpack5 실험적 지원, Angular CLI의 기본 Linter 변경에 대해 정리돼 있다. 

현재 Angular에는 TSLint를 기반의 Lint가 구현돼 있다. 하지만, [TSLint는 비권장되어 ESLint로 이전](https://medium.com/palantir/tslint-in-2019-1a144c2317a9)이 진행되고 있다.
Angular에서도 마찬가지로 TSLint에서 ESlint로 이전이 진행되고 있었으며, 이미 커뮤니티 기반으로 진행되고 있던 [Angular ESLint](https://github.com/angular-eslint/angular-eslint)로 이전하는 방침에 대해서도 정리돼 있다.

자세한 내용은 아래 문서를 참고.

- [Angular: ESLint 지원 현황 2020 Autumn | <output type=text>](https://blog.lacolaco.net/2020/11/angular-state-of-linting-2020/)


---

[Optimize React Apps PageSpeed Insights Score - thetuteur](https://thetuteur.com/optimize-react-apps-pagespeed-insights-score/)

리액트 기반 애플리케이션의 성능 개선을 주제로 정리돼 있다.

미사용 자바스크립트 삭제, 컴포넌트 Lazy Load, TTFB 단축을 위해 Node.js 응답을 In-Memory로 캐시하는 방법.

[`react-lazy-load-image-component`](https://github.com/Aljullu/react-lazy-load-image-component#readme)를 사용한 이미지 지연 로드, [`react-lazy-hydration`](https://github.com/hadeeb/react-lazy-hydration)을 사용한 초기 로드 시의 메인 스레드 처리를 줄이는 방법 등이 정리돼 있다.
또, 비동기 로드나 [`critical`](https://github.com/addyosmani/critical)을 사용한 UA 별 크리티컬 패스 CSS 생성 등에 대해서도 작성돼 있다.

----

[10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg](https://www.techatbloomberg.com/blog/10-insights-adopting-typescript-at-scale/)

타입스크립트를 채택해서 배운 것에 대해서 여러가지 작성돼 있다.

타입스크립트라는 언어, tsconfig 설정, 타입 정의 방법 등, 아래 원칙을 기준으로 다양하게 이야기한다.

- Scalability
- Ecosystem Coherence
- Standards Alignment


위 글에서 참조하고 있는 `type`과 `interface`의 차이점이나 컴파일 성능과 관련된 글도 꽤 흥미롭다.

- [TypeScript: Prefer Interfaces — @ncjamieson](https://ncjamieson.com/prefer-interfaces/)
- [Performance · microsoft/TypeScript Wiki](https://github.com/microsoft/TypeScript/wiki/Performance)

----

<h1 class="site-genre">헤드라인</h1>

----

## Node v15.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v15.2.0/](https://nodejs.org/en/blog/release/v15.2.0/ "Node v15.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v15.2.0 릴리스.
`events`에 이벤트를 지정해 리스너를 가져올 수 있는 `getEventListeners` 추가, `fs`의 `writeFile` / `readFile` AbortSignal에 대응.


----

## Bootstrap 5 Alpha 3 | Bootstrap Blog
[blog.getbootstrap.com/2020/11/11/bootstrap-5-alpha-3/](https://blog.getbootstrap.com/2020/11/11/bootstrap-5-alpha-3/ "Bootstrap 5 Alpha 3 | Bootstrap Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 5 Alpha 3 릴리스.
`.card` 기반의 아코디언 대신 `.accordion` 추가, `.btn-block` 삭제, Utilities 클래스 추가.


----

## Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog
[blog.angular.io/version-11-of-angular-now-available-74721b7952f7](https://blog.angular.io/version-11-of-angular-now-available-74721b7952f7 "Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 11 릴리스.
폰트 자동 인라인 화 대응, Component Test Harnesses 모든 컴포넌트 지원, Service 대응 개선, HMR을 CLI의 인수로 활성화 할 수 있다.
그 외로 Webpack5를 실험적으로 지원한다.

- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#1100-2020-11-11 "angular/CHANGELOG.md at master · angular/angular")

----

## Release v0.22.0 · ryansolid/solid
[github.com/ryansolid/solid/releases/tag/v0.22.0](https://github.com/ryansolid/solid/releases/tag/v0.22.0 "Release v0.22.0 · ryansolid/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

UI 개발 라이브러리 solid v0.22.0 릴리스.
`splid-js/dom`를 비권장하고 `solid-js/web`을 대신 사용하도록.
`dev`옵션 지원 , CDN을 통해서 사용할 수 있도록 `solid-js/html` 등을 패키지에 포함하고 `renderToWebStream`와 `createMutable` 추가.


----

## Lunuy/iterable-weak: Iterable WeakSet / WeakMap using ES2021 WeakRef
[github.com/Lunuy/iterable-weak](https://github.com/Lunuy/iterable-weak "Lunuy/iterable-weak: Iterable WeakSet / WeakMap using ES2021 WeakRef")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ECMAScript</span></p>

WeakRef 사용해 개발한 Iterable한 WeakMap/WeakSet 구현 라이브러리.
Iterate 가능하도록 요소를 참조하며 WeakRef의 FinalizationRegistry를 사용해 참조를 해제할 수도 있다.


----
<h1 class="site-genre">아티클</h1>

----

## What's New In DevTools (Chrome 88)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/11/devtools](https://developers.google.com/web/updates/2020/11/devtools "What's New In DevTools (Chrome 88)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 88 개발자 도구 변경 사항 정리.
CSS angle 시각적 도구, AVIF가 지원하지 않는 상태를 에뮬레이트 할 수 있도록 지원, storage quota size 애뮬레이터 지원.
Performance 패널에 Web Vitals 레인(lane) 추가, Application 패널에 Cross-Origin Isolated 상태 표시, network initiator 스택 트레이스 복사 지원.
실험적인 기능으로 CSS Flexbox 디버깅 기능, 키보드 단축키(shortcut) 커스터마이즈 기능이 추가 됐다.


----

## Optimize React Apps PageSpeed Insights Score - thetuteur
[thetuteur.com/optimize-react-apps-pagespeed-insights-score/](https://thetuteur.com/optimize-react-apps-pagespeed-insights-score/ "Optimize React Apps PageSpeed Insights Score - thetuteur")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React 앱 성능 개선.
사용하지 않는 자바스크립트 삭제, 컴포넌트 Lazy Load, TTFB를 단축하기 위해서 응답 캐시.
`react-lazy-load-image-component`를 이용한 이미지 지연 로드, `react-lazy-hydration`을 사용해 초기 로드 시점의 CPU 처리 줄이기.
또, CSS 비동기 로드, `critical`을 사용한 UA 별 크리티컬 패스 CSS 생성 등.


----

## TypeScript: Prefer Interfaces — @ncjamieson
[ncjamieson.com/prefer-interfaces/](https://ncjamieson.com/prefer-interfaces/ "TypeScript: Prefer Interfaces — @ncjamieson")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript우ㅏ `type`과 `interface`의 다른점.
`interface`는 이름으로 참조되는 것에 반해 `type`으로 정의한 형은 인라인 화 되는 경우가 있다. 때문에 `type`을 사용한 경우  `d.ts`가 필요 이상으로 커질 수 도 있다.

- [10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg](https://www.techatbloomberg.com/blog/10-insights-adopting-typescript-at-scale/ "10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg")

----

## Performance · microsoft/TypeScript Wiki
[github.com/microsoft/TypeScript/wiki/Performance](https://github.com/microsoft/TypeScript/wiki/Performance "Performance · microsoft/TypeScript Wiki")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

TypeScript 컴파일 성능과 관련된 내용이 정리 돼 있다.
`type`과 `interface`, Base Type과 Union Type, Project Reference, tsconfig.json 설정과 관련한 최적화.


----

## Angular: ESLint 지원 상황 2020 Autumn | <output type=text>(일본)
[blog.lacolaco.net/2020/11/angular-state-of-linting-2020/](https://blog.lacolaco.net/2020/11/angular-state-of-linting-2020/ "Angular: ESLintサポートの現状 2020 Autumn | <output type=text>")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

Agular에서의 Lint(TSLint / ESLint) 향후 방향.
TSLint는 Angular 12에서 비권장 될 예정으로 ESLint로의 이전은 커뮤니티 기반(angular-eslint 사용을 권장)으로 진행되고 있다.

- [angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular](https://github.com/angular-eslint/angular-eslint "angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular")

----

## Official Google Webmaster Central Blog: Timing for bringing page experience to Google Search
[webmasters.googleblog.com/2020/11/timing-for-page-experience.html](https://webmasters.googleblog.com/2020/11/timing-for-page-experience.html "Official Google Webmaster Central Blog: Timing for bringing page experience to Google Search")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">search</span></p>

2021년 5월 부터 Core Web Vitals(LCP, FID, CLS) 점수가 구글 검색 결과의 시그널로 사용된다.
웹 성능이 검색 결과 순위에 영향을 주게 된다.


----

## microsoft/Web-Dev-For-Beginners: 24 Lessons, 12 Weeks, Get Started as a Web Developer
[github.com/microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners "microsoft/Web-Dev-For-Beginners: 24 Lessons, 12 Weeks, Get Started as a Web Developer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

HTML / CSS / JS 및 애플리케이션 개발에 대해 학습할 수 있는 웹 개발 튜터리얼 모음 및 레슨.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Next.js Conf 2020 - YouTube
[www.youtube.com/playlist?list&#x3D;PLBnKlKpPeagnT2Cmv4giCbosfrbKnuYTD](https://www.youtube.com/playlist?list=PLBnKlKpPeagnT2Cmv4giCbosfrbKnuYTD "Next.js Conf 2020 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Next.js Conf 2020 발표 영상 목록


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## ESM
[esm.sh/](https://esm.sh/ "ESM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">deno</span> <span class="jser-tag">cdn</span> <span class="jser-tag">library</span></p>

esbuild로 의존을 포함해 bundle한 패키지를 배포하는 npm CDN 서비스.
npm 패키지를 deno에서 ES Modules로 불러올 수 있고 polyfill 구조도 준비돼 있다.


----

## open-source-labs/Recoilize: Recoil developer tool
[github.com/open-source-labs/Recoilize](https://github.com/open-source-labs/Recoilize "open-source-labs/Recoilize: Recoil developer tool")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

recoil 디버깅 도구.


----

## acot-a11y/acot: More accessible web, all over the world.
[github.com/acot-a11y/acot](https://github.com/acot-a11y/acot "acot-a11y/acot: More accessible web, all over the world.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">Tools</span></p>

ESLint와 비슷한 플러그인 시스템을 갖는 Accessibility 테스트 프레임워크.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## trivago/prettier-plugin-sort-imports: A prettier plugin to sort imports in typescript and javascript files by the provided RegEx order.
[github.com/trivago/prettier-plugin-sort-imports](https://github.com/trivago/prettier-plugin-sort-imports "trivago/prettier-plugin-sort-imports: A prettier plugin to sort imports in typescript and javascript files by the provided RegEx order.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">plugin</span></p>

import 문 순서를 정렬하는 prettier plugin


----

## vinissimus/next-translate: i18n tool for Next.js 10 🌍 - Load page translations and use them in an easy way!
[github.com/vinissimus/next-translate](https://github.com/vinissimus/next-translate "vinissimus/next-translate: i18n tool for Next.js 10 🌍 - Load page translations and use them in an easy way!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Next.js 용 i18n 도구.


----

## angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular
[github.com/angular-eslint/angular-eslint](https://github.com/angular-eslint/angular-eslint "angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ESLint</span></p>

Angular 용 ESLint 플러그인 세트.
Codelyzer / TSLint에서 이전 시 사용을 권장하고 있다.


----

## felixfbecker/dom-to-svg: Library to convert a given HTML DOM node into an accessible SVG "screenshot".
[github.com/felixfbecker/dom-to-svg](https://github.com/felixfbecker/dom-to-svg "felixfbecker/dom-to-svg: Library to convert a given HTML DOM node into an accessible SVG \"screenshot\".")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">SVG</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`<foreignObject>`를 사용하지 않고 DOM에서 SVG를 생성하는 라이브러리.
DOM 상의 WAI-ARIA나 링크 등도 포함하는 SVG를 생성한다.


----

## davnicwil/react-frontload: Async data loading for React components, on client & server
[github.com/davnicwil/react-frontload](https://github.com/davnicwil/react-frontload "davnicwil/react-frontload: Async data loading for React components, on client & server")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

React 용 Data Loader 라이브러리.
컴포넌트에서 API를 호출해 데이터를 가져오거나 호출 상태를 다룰 수 있다. 클라이언트와 서버에서 각각 대응하는 API를 준비해 hydration도 가능하다.


----

## alephjs/aleph.js: The React Framework in Deno.
[github.com/alephjs/aleph.js](https://github.com/alephjs/aleph.js "alephjs/aleph.js: The React Framework in Deno.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React를 기반으로 한 Next.js와 비슷한 Deno 용 프레임워크.


----
<h1 class="site-genre">도서</h1>

----

## JavaScript 모던 프로그래밍 완전 가이드 \[견고한 코드를 효율적으로 개발! \] (impress top gear 시리즈) | Cay S. Horstmann, 요시카와 쿠니오 | 책 | 통신판매 | Amazon
[www.amazon.co.jp/dp/4295010561/](https://www.amazon.co.jp/dp/4295010561/ "JavaScript 모던 프로그래밍 완전 가이드 \[견고한 코드를 효율적으로 개발! \] (impress top gear 시리즈) | Cay S. Horstmann, 요시카와 쿠니오 | 책 | 통신판매 | Amazon")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2020년 12월 21일 출간 예정인 Modern JavaScript for the Impatient의 번역서.

- [Amazon | Modern JavaScript for the Impatient (English Edition) \[Kindle edition\] by Horstmann, Cay S. | Languages & Tools | Kindle 스토어](https://www.amazon.co.jp/dp/B08F5HFWBH/ "Amazon | Modern JavaScript for the Impatient (English Edition) \[Kindle edition\] by Horstmann, Cay S. | Languages &amp; Tools | Kindle 스토어")

----
