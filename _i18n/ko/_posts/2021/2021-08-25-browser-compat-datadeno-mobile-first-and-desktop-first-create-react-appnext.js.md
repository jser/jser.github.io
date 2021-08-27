---
title: "2021-08-25: browser-compat-data에 Deno를 추가, Mobile First and Desktop First, create-react-app에서 Next.js로 이전"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-08-25T02:44:57.250Z
category: JSer
tags:
- React
- testing
- DOM
- Next.js
- webservice

---

JSer.info #554 - MDN 등에서 이용하는 브라우저 구현 호환 데이터를 관리하고 있는 `@mdn/browser-compat-data` 4.0.0 릴리스.

- [Release v4.0.0 · mdn/browser-compat-data](https://github.com/mdn/browser-compat-data/releases/tag/v4.0.0)

호환 목록에 Deno 데이터가 추가됐다.

- [Deno on MDN | Deno Blog](https://deno.com/blog/deno-on-mdn)

스키마에 `preview`와 `accepts_flags` 추가, XPath와 XSLT의 데이터가 불완전하므로 삭제됐다.

----

[The State Of Mobile First and Desktop First - Ahmad Shadeed](https://ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/)에서 CSS를 작성할 때 Mobile 코드를 먼저 작성하느냐 Desktop 코드를 먼저 작성하느냐에 따른 차이를 이야기한다.

Mobile과 Desktop 중 하나를 먼저 작성하고 다른 쪽을 Media Query로 덮어쓸때의 코드 차이와 확장성 측면의 차이를 비교한다.
또, 베이스 코드를 두고 여기에 Mobile과 Desktop 대응 코드를 각각 작성할 경우의 어려움 점에 대해서도 이야기한다. 
나아가 Flexbox나 CSS Grid, Container Queries 등 새로운 CSS 기능을 사용하여 좀 더 간단하게 작성할 수 있게 된 부분도 다룬다.

----

[From Create-React-App to Next | Kitty Giraudel](https://kittygiraudel.com/2021/08/24/from-cra-to-next/)에는 [Create React App](https://github.com/facebook/create-react-app)(CRA)에서 [Next.js](https://nextjs.org/)로 이전을 어떤식으로 했는지 소개한다.

`<head>`나 스타일링 등의 항목 별로 CRA에서 Next.js로 어떻게 이식했는지 소개.
또, `<Link`> 외에는 두 시스템(react-scripts, Next.js)에서 모두 실행 할 수 있으므로 이전 간 동작 확인을 위해 `<Link>` 역시 두 시스템에 대응 가능하도록 정의하여 테스트 할 수 있는 방법도 다룬다.



----

<h1 class="site-genre">헤드라인</h1>

----

## Announcing React Native 0.65 · React Native
[reactnative.dev/blog/2021/08/17/version-065](https://reactnative.dev/blog/2021/08/17/version-065 "Announcing React Native 0.65 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span></p>

React Native 0.65 릴리스.
Hermes 0.8로 업그레이드 하고 Hades 라는 가비지 콜렉터 구현, ECMAScript i18n API 지원, Apple M1 지원 등.


----

## Release v9.1.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v9.1.0](https://github.com/mochajs/mocha/releases/tag/v9.1.0 "Release v9.1.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 9.1.0 릴리스.
`--fail-zero`, `--node-option` 지원, `JSON` 레포트 추가 등.


----

## Release Notes for Safari Technology Preview 130 | WebKit
[webkit.org/blog/11958/release-notes-for-safari-technology-preview-130/](https://webkit.org/blog/11958/release-notes-for-safari-technology-preview-130/ "Release Notes for Safari Technology Preview 130 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

플래그(`--useArrayFindLastMethod`)를 붙여서 `Array.prototype.findLast`와 `Array.prototype.findLastIndex` 지원, WebAudio에서 WebM / Opus 컨테이너 지원 등.


----

## Release v4.0.0 · mdn/browser-compat-data
[github.com/mdn/browser-compat-data/releases/tag/v4.0.0](https://github.com/mdn/browser-compat-data/releases/tag/v4.0.0 "Release v4.0.0 · mdn/browser-compat-data")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MDN등에서 사용하고 있는 웹 기술 호환성 목록 browser-compat-data 4.0.0 릴리즈.
스키마에 `preview`와 `accepts_flags` 추가, Deno란 추가, XPath와 XSLT 데이터가 불완전 하기 때문에 삭제됐다.

- [Deno on MDN | Deno Blog](https://deno.com/blog/deno-on-mdn "Deno on MDN | Deno Blog")

----

## The npm registry is deprecating TLS 1.0 and TLS 1.1 | The GitHub Blog
[github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/](https://github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/ "The npm registry is deprecating TLS 1.0 and TLS 1.1 | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Github</span> <span class="jser-tag">security</span> <span class="jser-tag">news</span></p>

npm registry에서 LS 1.0과 TLS 1.1을 비권장하고 2021년 9월 29일에 지원을 종료할 예정.
Node.js 0.10.0 미만 버전을 사용하고 있는 경우, 커스텀 바이너리를 사용하고 있는 경우가 대응 대상이 되지만 이미 99%는 TLS 1.2를 이용하고 있다고 한다.


----
<h1 class="site-genre">아티클</h1>

----

## The State Of Mobile First and Desktop First - Ahmad Shadeed
[ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/](https://ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/ "The State Of Mobile First and Desktop First - Ahmad Shadeed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS를 작성 할 때 Mobile과 Desktop 용 중 어느 것을 먼저 작성할 것인지.
Mobile과 Desktop 중 무엇을 먼저 쓰고, 다른 쪽을 Media Query로 덮어써서 대응 할 경우의 코드량이나 확장성의 차이 연구.
또, 기반 코드에 각 코드를 작성한 경우나 Flexbox, Container Query와 같은 최신 기능을 사용할 경우에 대해서도 다루고 있다.


----

## mouseover 중에 표시 되는 DOM 디버깅 하기 | blog.jxck.io(일본어)
[blog.jxck.io/entries/2021-08-20/how-to-debug-mouseover.html](https://blog.jxck.io/entries/2021-08-20/how-to-debug-mouseover.html "mouseover 中に表示される DOM のデバッグ | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

mouseover 중에 표시되는 DOM 요소를 개발자 도구에서 디버깅하는 방법 소개(소소한 디버깅 팁).


----

## &#039;return await promise&#039; vs &#039;return promise&#039; in JavaScript
[dmitripavlutin.com/return-await-promise-javascript/](https://dmitripavlutin.com/return-await-promise-javascript/ "&#039;return await promise&#039; vs &#039;return promise&#039; in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`return await promise`와 `return promise` 두 구문의 동작이 다를 수 있는 경우 소개.
`try...catch`로 둘러 쌓여 있는 경우에 `await`에 의해 throw 되면 결과가 다르다고 한다.


----

## 여러 저장소 간 에서의 eslint・prettier 설정 공통화 - LIVESENSE ENGINEER BLOG(일본어)
[made.livesense.co.jp/entry/2021/08/24/083000](https://made.livesense.co.jp/entry/2021/08/24/083000 "複数リポジトリ間におけるeslint・prettierの設定共通化 - LIVESENSE ENGINEER BLOG")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLint의 설정을 소속 그룹(회사) 내 에서 공유하고 관리하기 위해 scoped packages으로 공개 하고 이용하는 방법 소개.


----

## Why WASM is not the future of Babylon.js | by Babylon.js | Aug, 2021 | Medium
[babylonjs.medium.com/why-wasm-is-not-the-future-of-babylon-js-5832b09c9b10](https://babylonjs.medium.com/why-wasm-is-not-the-future-of-babylon-js-5832b09c9b10 "Why WASM is not the future of Babylon.js | by Babylon.js | Aug, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

WebAssembly는 C++ 등의 네이티브 언어를 컴파일하여 사용하는 데 목적이 있으므로 TypeScript로 작성한 Babylon.js를 WASM으로 전환할 합당한 이유가 아직 없다는 의견을 풀어내는 글.
WASM과 JS 간의 커뮤니케이션 비용, 어려운 디버깅, 메모리 관리 등도 포함하기 때문에 관리 범위가 커지는 문제점에 대해서 언급한다.
또, Babylon.js의 물리 엔진 등 WASM을 이미 이용하고 있는 일부 영역에 대해서도 소개한다.


----

## From Create-React-App to Next | Kitty Giraudel
[kittygiraudel.com/2021/08/24/from-cra-to-next/](https://kittygiraudel.com/2021/08/24/from-cra-to-next/ "From Create-React-App to Next | Kitty Giraudel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

create-react-app로 작성한 앱을 Next.js로 이전 한 이야기.
보일러 플레이트, `<head>`, 라우팅, 컴포넌트의 Dynamic Import, Styling, CSR/SSR, Lint 등에 대해.
또, `<Link>` 외에는 두 시스템(react-scripts, Next.js)에서 모두 실행 할 수 있으므로 `<Link>` 역시 두 시스템에 대응 가능하도록 정의하여 마이그레이션 하는 동안에는 여전히 react-scripts를 이용해 제품 빌드 및 배포할 수 있도록 구성했다고 한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## SpeedVitals - Optimize your Website for Web Vitals
[speedvitals.com/](https://speedvitals.com/ "SpeedVitals - Optimize your Website for Web Vitals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span></p>

특정 웹 사이트를 성능 측정 하여 Core Web Vitals 측면의 개선 방법을 제시하는 서비스.
측정 결과로 부터 LCP 스코어 개선 방법, 레이아웃 시프트 시각화 등 개선에 관한 정보를 제공한다.

- [Introducing SpeedVitals Alpha Version! - SpeedVitals](https://blog.speedvitals.com/introducing-speedvitals/#more-20 "Introducing SpeedVitals Alpha Version! - SpeedVitals")

----

## @open-wc/semantic-dom-diff - npm
[www.npmjs.com/package/@open-wc/semantic-dom-diff](https://www.npmjs.com/package/@open-wc/semantic-dom-diff "@open-wc/semantic-dom-diff - npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

DOM / HTML assertion 라이브러리.
HTML 문자열을 비교하여 테스트 할 수 있다.

----

## Testing | Next.js
[nextjs.org/docs/testing](https://nextjs.org/docs/testing "Testing | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

Next.js에서의 테스트를 주제로 한 문서.
Cypress를 사용한 E2E 테스트와 Jest + React Testing Library를 사용한 테스트 방법 소개.

- [Delba de Oliveira on Twitter: &amp;quot;We&#039;ve just released the first iteration of the Next.js Testing Docs: https://t.co/jhe7zSigt3 🧪 We wanted to provide a starting point for those looking to set up Next.js with 3 commonly used testing tools: @cypress\_io, @fbjest and React @TestingLib.&amp;quot; / Twitter](https://twitter.com/delba_oliveira/status/1427307677709967362 "Delba de Oliveira on Twitter: &amp;amp;quot;We&amp;#039;ve just released the first iteration of the Next.js Testing Docs: https://t.co/jhe7zSigt3 🧪 We wanted to provide a starting point for those looking to set up Next.js with 3 commonly used testing tools: @cypress\_io, @fbjest and React @TestingLib.&amp;amp;quot; / Twitter")


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## geist-org/react: Modern and minimalist React UI library.
[github.com/geist-org/react](https://github.com/geist-org/react "geist-org/react: Modern and minimalist React UI library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

Vercel의 디자인에 영감을 받아 개발한 React UI 프레임워크.


----

## johnsoncodehk/volar: ⚡ Fast Vue Language Support Extension
[github.com/johnsoncodehk/volar](https://github.com/johnsoncodehk/volar "johnsoncodehk/volar: ⚡ Fast Vue Language Support Extension")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">plugin</span></p>

Vue 3를 지원하는 VSCode 용 확장 기능.
`.vue` 파일의 TypeScript 타입 체크 및 템플릿의 language server를 제공한다.


----
