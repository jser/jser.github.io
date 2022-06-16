---
title: "2022-06-06: Angular 14, Cypress 10, Vue 2.7 α"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-06-06T13:47:09.930Z
category: JSer
tags:
- npm
- node.js
- vite
- Vue
- Tools

---

JSer.info #595 - Angular 14가 릴리스 됐다.

- [Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog](https://blog.angular.io/angular-v14-is-now-available-391a6db736af)

프리뷰 기능으로서 standalone components가 추가 됐다.

- [Angular - Getting started with standalone components](https://angular.io/guide/standalone-components)

또, Angular Forms의 타입 형식 개선, 에러 메시지를 production build에서는 오류 코드만 출력하도록 변경, 파일 크기 최적화 등이 이뤄졌다.
이 외에는 TypeScript 4.7 지원, Angular CLI 개선 등이 포함됐다.

---

Cypress 10가 릴리스 됐다.

- [Announcing Cypress 10 with Component Testing Beta!](https://cypress.io/blog/2022/06/01/cypress-10-release/)

Cypress 10에서는 Cypress App이 개편됐다.
또, Component Test 구조가 추가 됐다.

- [Writing Your First Component Test | Cypress Documentation](https://docs.cypress.io/guides/component-testing/writing-your-first-component-test#Component-vs-End-to-End-in-a-Nutshell)

---

Vue 2.x의 마지막 minor 릴리스가 될 예정인 Vue.js 2.7α가 공개 됐다.

- [vue/CHANGELOG.md at main · vuejs/vue](https://github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31)

Composition API의 전체 지원, ESM 빌드에 `ref` 등 named export 추가 등이 포함됐다.

이 Vue 2.7이 정식 릴리스 된 이후 약 18 개월 후에 Vue 2.x는 EOL이 될 예정이다.
현시점으로 볼 때 Vue 2.x는 2023년 말 즈음 EOL이 되지 않을까 예상한다.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Vue 2 end of life at the end of 2023 <a href="https://twitter.com/hashtag/vuejs?src=hash&amp;ref_src=twsrc%5Etfw">#vuejs</a> <a href="https://t.co/luvk1lt3U6">pic.twitter.com/luvk1lt3U6</a></p>&mdash; Filip Rakowski 🇺🇦 (@filrakowski) <a href="https://twitter.com/filrakowski/status/1532281407942365184?ref_src=twsrc%5Etfw">June 2, 2022</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


----

<h1 class="site-genre">헤드라인</h1>

----

## Node v18.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v18.3.0/](https://nodejs.org/en/blog/release/v18.3.0/ "Node v18.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 18.3.0 릴리스.
`util` 모듈에 `parseArgs` 추가, `http` 모듈에 `uniqueHeaders` 옵션 추가 등.

- [pkgjs/parseargs: Polyfill of proposal for \`util.parseArgs()\`](https://github.com/pkgjs/parseargs "pkgjs/parseargs: Polyfill of proposal for \&#x60;util.parseArgs()\&#x60;")

----

## Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog
[blog.angular.io/angular-v14-is-now-available-391a6db736af](https://blog.angular.io/angular-v14-is-now-available-391a6db736af "Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 14 릴리스.
프리뷰 기능으로 standalone components 추가, Angular Forms 타입 형식 개선, 에러 메시지를 production build 시에는 에러 코드만 출력하도록 변경.
TypeScript 4.7 지원, Angular CLI 개선 등.


----

## Announcing Cypress 10 with Component Testing Beta!
[cypress.io/blog/2022/06/01/cypress-10-release/](https://cypress.io/blog/2022/06/01/cypress-10-release/ "Announcing Cypress 10 with Component Testing Beta!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cypress 10 릴리스.
Cypress App이 개편됐고 Component Testing이 베타가 됐다.


----

## Release v3.16.0 · mishoo/UglifyJS
[github.com/mishoo/UglifyJS/releases/tag/v3.16.0](https://github.com/mishoo/UglifyJS/releases/tag/v3.16.0 "Release v3.16.0 · mishoo/UglifyJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

UflifyJS 3.16.0 릴리스.
입력된 데이터를 ES Modules로 다루는 `--module` 플래그가 추가됐다.


----

## vue/CHANGELOG.md at main · vuejs/vue
[github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31](https://github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31 "vue/CHANGELOG.md at main · vuejs/vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.7α 릴리스.
Vue 2.x의 마지막 마이너 릴리스 후보가 된다. Vue 2.7이 정식 릴리스 된 후로 18 개월 후인 2023년 말에 Vue 2.x는 EOL이 될 예정이다.
Composition API 풀 지원, ESM 빌드에 `ref` 등 named export 추가.

- [Filip Rakowski 🇺🇦 on Twitter: &amp;quot;Vue 2 end of life at the end of 2023 #vuejs https://t.co/luvk1lt3U6&amp;quot; / Twitter](https://twitter.com/filrakowski/status/1532281407942365184 "Filip Rakowski 🇺🇦 on Twitter: &amp;amp;quot;Vue 2 end of life at the end of 2023 #vuejs https://t.co/luvk1lt3U6&amp;amp;quot; / Twitter")

----

## npm security update: Attack campaign using stolen OAuth tokens | The GitHub Blog
[github.blog/2022-05-26-npm-security-update-oauth-tokens/](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/ "npm security update: Attack campaign using stolen OAuth tokens | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">news</span></p>

Heroku와 Travis CI에서 GitHub OAuth Token이 유출된 사건 정리.
npm이 관리하는 프라이빗 저장소를 통해 AWS 접근키가 탈취 당해 npm의 일부 정보가 유출됐다.
2015년 사용자 정보(사용자 명 / 메일 주소 / 패스워드 해시), 2021년 프라이빗 npm 패키지 메타 데이터, 2022년 모든 프라이빗 패키지 이름과 버전이 유출됐다.


----

## Release Add support for lts/-n aliases · actions/setup-node
[github.com/actions/setup-node/releases/tag/v3.3.0](https://github.com/actions/setup-node/releases/tag/v3.3.0 "Release Add support for lts/-n aliases · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">ReleaseNote</span></p>

GitHub Actions에서 Node.js 환경을 설정하는 actions/setup-node 3.3.0 릴리스.
`node-version: lts/-1` 처럼 LTS 상대 지정 방식 지원.
3.2.0에서는 `current`와 `latest`의 alias를 지원한다.

- [Release Support caching dependencies and LTS aliases · actions/setup-node](https://github.com/actions/setup-node/releases/tag/v2.2.0 "Release Support caching dependencies and LTS aliases · actions/setup-node")
- [Release Add current, node, latest aliases · actions/setup-node](https://github.com/actions/setup-node/releases/tag/v3.2.0 "Release Add current, node, latest aliases · actions/setup-node")

----
<h1 class="site-genre">아티클</h1>

----

## Processing Arrays non-destructively: \`for-of\` vs. \`.reduce()\` vs. \`.flatMap()\`
[2ality.com/2022/05/processing-arrays-non-destructively.html](https://2ality.com/2022/05/processing-arrays-non-destructively.html "Processing Arrays non-destructively: \`for-of\` vs. \`.reduce()\` vs. \`.flatMap()\`")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Array의 filter / map / some / every / reduce / flatMap 메서드나 for of 등, 각 메서드의 특징과 활용 방법 그리고 상황에 따라 무엇을 써야하는지 정리.


----

## JavaScript의 미디어타입과 RFC 9239 | blog.jxck.io(일본어)
[blog.jxck.io/entries/2022-05-31/text-javascript.html](https://blog.jxck.io/entries/2022-05-31/text-javascript.html "JavaScript のメディアタイプと RFC 9239 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript의 MIME Types을 정리 및 소개하고 있다.


----

## Introducing Opportunities &amp; Experiments: Taking the Guesswork out of Performance - WebPageTest Blog
[blog.webpagetest.org/posts/introducing-opportunities-and-experiments/](https://blog.webpagetest.org/posts/introducing-opportunities-and-experiments/ "Introducing Opportunities &amp; Experiments: Taking the Guesswork out of Performance - WebPageTest Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

WebPageTest에 Opportunities와 Experiments이라고 부르는 기능이 추가됐다.
Opportunities는 성능이나 접근성과 관련된 개선 항목을 추천하고 실제 적용하면 결과가 어떻게 나타나는지 측정할 수 있는 기능.
Experiments는 Edge의 Proxy를 통하여 일시적으로 사이트를 변경해 측정할 수 있는 기능.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## pkg.land - find NPM alternative packages
[pkg.land/](https://pkg.land/ "pkg.land - find NPM alternative packages")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">search</span> <span class="jser-tag">webservice</span></p>

특정 npm 패키지를 대체할 수 있는 다른 패키지를 탐색할 수 있는 서비스.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## jridgewell/trace-mapping: Trace the original position through a source map
[github.com/jridgewell/trace-mapping](https://github.com/jridgewell/trace-mapping "jridgewell/trace-mapping: Trace the original position through a source map")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

source-map 패키지와 호환성 있는 API를 제공하는 라이브러리.
source-map 패키지와는 다르게 WebAssembly를 이용하지 않는 방향으로 개발됐다.

----

## Svelvet
[svelvet.io/](https://svelvet.io/ "Svelvet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">diagram</span> <span class="jser-tag">library</span></p>

플로우 차트를 그리는(묘화) Svelte component.


----

## histoire-dev/histoire: ⚡ Fast and beautiful interactive component playgrounds, powered by Vite
[github.com/histoire-dev/histoire](https://github.com/histoire-dev/histoire "histoire-dev/histoire: ⚡ Fast and beautiful interactive component playgrounds, powered by Vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Tools</span></p>

Vite를 기반으로 한 Storybook과 같은 도구.


----

## WebReflection/highlighted-code: A textarea builtin extend to automatically provide code highlights based on one of the languages available via highlight.js
[github.com/WebReflection/highlighted-code](https://github.com/WebReflection/highlighted-code "WebReflection/highlighted-code: A textarea builtin extend to automatically provide code highlights based on one of the languages available via highlight.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

textarea에 신텍스 하이라이트를 오버레이 할 수 있는 라이브러리.


----

## cyco130/vavite: Develop server-side applications with Vite
[github.com/cyco130/vavite](https://github.com/cyco130/vavite "cyco130/vavite: Develop server-side applications with Vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Vite를 서버 사이드에 내장하기 위해 Express 등에 대응한 Middleware와 Vite 플러그인.
Vite를 사용해 서버 사이드의 코드 트랜스파일, Live Reload, SSR 등에 대응하기 위한 구조를 제공한다.
또, 제품 빌드 시 개발 용 DevServer 참조를 지울 수 있는 Vite 플러그인도 함께 제공한다.


----
<h1 class="site-genre">도서</h1>

----

## Web Browser Engineering
[browser.engineering/](https://browser.engineering/ "Web Browser Engineering")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">python</span> <span class="jser-tag">book</span></p>

Python으로 브라우저 렌더링 엔진을 만들어 보면서 웹 페이지의 구조를 학습 할 수 있는 전자 서적.
HTML 파서, 레이아웃, CSS 파서, 클릭 처리, Browser Chrome의 UI 구현, HTTP 요청 처리, DOM API 구현, Cookie와 SameSite 구현.
Skia를 사용한 렌더링과 블렌딩, 스케줄링, 애니메이션 처리 등을 다룬다.

- [Why Python? | Web Browser Engineering](https://browser.engineering/blog/why-python.html "Why Python? | Web Browser Engineering")

----

## 막힘없이 이해하는 자바스크립트 신판(사쿠라바 히로유키, 모치즈키 코타로) | 쇼에이사의 책(일본어)
[www.shoeisha.co.jp/book/detail/9784798173269](https://www.shoeisha.co.jp/book/detail/9784798173269 "スラスラわかるJavaScript 新版（桜庭 洋之 望月 幸太郎）｜翔泳社の本")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bok</span></p>

2022년 07월 13일 출간 예정인 자바스크립트 입문서


----


