---
title: "2019-01-01: WebdriverIO v5, Rollup 1.0, Rust + WebAssembly + WebWorker"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-12-31T13:38:01.421Z
category: JSer
tags:
- Selenium
- rollup
- WebAssembly
- Rust

---

JSer.info #416 - WebDriver를 사용하는 테스트 프레임워크 WebdriverIO v5가 릴리스됐습니다.

- [WebdriverIO v5 Released · WebdriverIO](https://webdriver.io/blog/2018/12/19/webdriverio-v5-released.html)
- [webdriverio/CHANGELOG.md at master · webdriverio/webdriverio](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20)


패키지 구조와 API와 관련한 부분을 변경했습니다.

기본 패키지를 [`@wdio`](https://www.npmjs.com/org/@wdio/)로 이동했고 원래 포함돼 있던 CLI를 `@wdio/cli`로 분리했습니다.

API 관련해서는 커맨드에 직접 selector를 전달 하지 못하도록 변경했고 메서드 체인이 아닌 async/await 기반으로 변경했습니다.

```js
// v4에서는 셀렉터를 전달함
browser.click('#elem');
// v5에서는 element를 가져온 후 조작함
const elem = $('#elem');
elem.click()
```

또한 `isVisible`을 `isDisplayed`으로 이름을 변경했으며 이 외에도 많은 커맨드의 이름을 변경했습니다.
자세한 내용은 [CHANGELOG.md](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20)에 정리돼 있으니 참고하시길 바랍니다.

----

모듈 번들러 Rollup v1.0.0가 릴리스됐습니다.

- [Release v1.0.0 · rollup/rollup](https://github.com/rollup/rollup/releases/tag/v1.0.0)

특정 옵션을 비권장하고 옵션의 이름을 변경하는 등 비호환 변경 사항을 포함한 릴리스입니다.   
`bundle.generate`와 `bundle.write` 반환 값의 포맷을 변경했으며 사용중인 파서를 `acorn@6`로 업데이트 했습니다.

- [1.0 changes by guybedford · Pull Request #2293 · rollup/rollup](https://github.com/rollup/rollup/pull/2293)

----

[Comlink + Rust로 언어와 스레드의 울타리를 넘은 WebAssembly 개발 - Qiita(일본어)](https://qiita.com/3846masa/items/92d24e16ebb5151b08ba)에는 Rust를 사용한 WebAssembly 개발에 대해 Zip 압축 해제 앱을 예로 소개하고 있습니다. 

Rust나 [wasm-pack](https://rustwasm.github.io/wasm-pack/book/)을 사용한 개발 환경 설정부터 [wasm-bindgen](https://rustwasm.github.io/wasm-bindgen/)로 Rust와 JavaScript 바인딩 작성, webpack으로 가져오기, 브라우저에서의 실행까지 작성돼 있습니다.
또, 메인스레드의 비용을 줄이기 위해 WebAssembly 처리를 WebWorker 상에서 실행하고, 메시지를 주고 받는데 [Comlink](https://github.com/GoogleChromeLabs/comlink)를 사용하는 방법에 대해서도 소개합니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## WebdriverIO v5 Released · WebdriverIO
[webdriver.io/blog/2018/12/19/webdriverio-v5-released.html](https://webdriver.io/blog/2018/12/19/webdriverio-v5-released.html "WebdriverIO v5 Released · WebdriverIO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Selenium</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

WebdriverIO v5가 릴리스됐습니다.
`wdio` CLI를 `@wdio/cli`로 분리했고 커맨드에 selector를 전달하지 못하도록 변경했습니다. 또, 메서드 체인 방식에서 async/await 기반으로 변경했습니다.
이 외에 일부 커맨드의 이름을 변경하는 등 비호환 변경 사항을 포함하고 있습니다.

- [webdriverio/CHANGELOG.md at master · webdriverio/webdriverio](https://github.com/webdriverio/webdriverio/blob/master/CHANGELOG.md#v500-2018-12-20 "webdriverio/CHANGELOG.md at master · webdriverio/webdriverio")

----

## Release v1.0.0 · rollup/rollup
[github.com/rollup/rollup/releases/tag/v1.0.0](https://github.com/rollup/rollup/releases/tag/v1.0.0 "Release v1.0.0 · rollup/rollup")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Rollup 1.0.0이 릴리스됐습니다.

비호환 변경 사항으로 옵션 이름을 변경했고 `bundle.generate`에서 반환하는 값의 포맷도 변경했습니다. 그리고 사용중인 파서를 `acorn@6`으로 업데이트 했습니다.


----
<h1 class="site-genre">アーティクル</h1>

----

## 「GraphQL」 완변 입문 ─ REST와의 비교, API / 프런트 구현을 통해 학습하기 - 엔지니어Hub｜젊은 Web 엔지니어의 커리어를 생각하다!
[employment.en-japan.com/engineerhub/entry/2018/12/26/103000](https://employment.en-japan.com/engineerhub/entry/2018/12/26/103000 "「GraphQL」 완변 입문 ─ REST와의 비교, API / 프런트 구현을 통해 학습하기 - 엔지니어Hub｜젊은 Web 엔지니어의 커리어를 생각하다!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">article</span></p>

GraphQL 입문 글입니다.
GraphQL의 이점, 결점, 스키마 / 쿼리 작성 방법, Variable과 Fragment 사용 방법에 대해 소개합니다.
또, Relay 확장과 실제 GraphQL를 사용한 구현 예에 대해서도 작성돼 있습니다.


----

## Understanding Throttling and Debouncing – Bits and Pieces
[blog.bitsrc.io/understanding-throttling-and-debouncing-973131c1ba07](https://blog.bitsrc.io/understanding-throttling-and-debouncing-973131c1ba07 "Understanding Throttling and Debouncing – Bits and Pieces")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Throttling과 Debouncing를 각각 구현해가면서 동작을 이해할 수 있도록 작성된 글입니다.


----

## Comlink + Rust로 언어와 스레드의 울타리를 넘은 WebAssembly 개발 - Qiita(일본어)
[qiita.com/3846masa/items/92d24e16ebb5151b08ba](https://qiita.com/3846masa/items/92d24e16ebb5151b08ba "Comlink + Rust로 언어와 스레드의 울타리를 넘은 WebAssembly 개발 - Qiita(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webworker</span> <span class="jser-tag">Rust</span> <span class="jser-tag">article</span></p>

Rust를 사용한 WebAssembly 라이브러리 개발에 관해 소개합니다.
wasm 바인딩 작성, webpack을 사용해 불러오는 방법, 메인스레드 이 외의 환경에서 WebAssembly 실행 시 Comlink를 사용해 메세지를 주고 받는 방법에 관해 이야기 합니다.


----

## Babel 7의 주요 변경 사항 정리 - Qiita(일본어)
[qiita.com/soarflat/items/21b8955f992bf7d38581](https://qiita.com/soarflat/items/21b8955f992bf7d38581 "Babel 7의 주요 변경 사항 정리 - Qiita(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">article</span></p>

Babel 7의 주된 변경 사항과 마이그레이션 방법을 소개합니다.


----

## 기초부터 시작하는 React Native 입문：CodeZine（코드진）(일본어)
[codezine.jp/article/corner/772](https://codezine.jp/article/corner/772 "기초부터 시작하는 React Native 입문：CodeZine（코드진）(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">tutorial</span></p>

React Native에 관한 연재 글입니다.


----

## ECMAScript modules in Node.js: the new plan
[2ality.com/2018/12/nodejs-esm-phases.html](http://2ality.com/2018/12/nodejs-esm-phases.html "ECMAScript modules in Node.js: the new plan")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span> <span class="jser-tag">module</span></p>

Node.js에서 ES Modules를 다루를 방법을 정리한 글입니다.
`.mjs` 지원과 CommonJS와의 상호운용성 문제, 향후 어떤 방침이 예정돼 있는지 소개합니다.

----

## JavaScript와 Web 개발에 관한 InfoQ 트렌드 보고서
[www.infoq.com/jp/articles/javascript-web-development-trends](https://www.infoq.com/jp/articles/javascript-web-development-trends "JavaScriptとWeb開発に関するInfoQトレンドレポート")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript에 관한 InfoQ의 트렌드 보고서.
이노베이터, 얼리어답터, 얼리 메이저리티, 레이트 메이저리티, 레거드로 나눠 관련한 라이브러리 / 프레임워크 / 도구의 현 위치를 살펴볼 수 있습니다.


----

## Angular를 예로하는 TypeScript로 실현하는 타입 안전한 다국어 대응 | 주식회사 카북(일본어)
[www.kabuku.co.jp/software\_engineer/typescript-angular-i18n/](https://www.kabuku.co.jp/software_engineer/typescript-angular-i18n/ "Angular를 예로하는 TypeScript로 실현하는 타입 안전한 다언어 대응 | 주식회사 카북(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">i18n</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

다국어 파일(i18n)을 타입스크립트 코드로 표현하여 타입 안전한 다국어를 정의하는 방법에 대해 소개합니다.
다국어 파일을 코드로 작성했을 때 장점과 단점에 대해서도 이야기합니다.


----

## takefumi-yoshii/react-hooks-ogiri: Advent calendar of 2018. This is a showreel using a reaction hook.
[github.com/takefumi-yoshii/react-hooks-ogiri](https://github.com/takefumi-yoshii/react-hooks-ogiri "takefumi-yoshii/react-hooks-ogiri: Advent calendar of 2018. This is a showreel using a reaction hook.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">example</span> <span class="jser-tag">document</span></p>

React Hooks API를 사용한 UI 컴포넌트 샘플 구현 모음 저장소 입니다.

- [React Hooks 大喜利 Advent Calendar 2018 - Qiita](https://qiita.com/advent-calendar/2018/react-hooks-ogiri "React Hooks 大喜利 Advent Calendar 2018 - Qiita")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## FontoXML/fontoxpath: A minimalistic XPath 3.1 implementation in pure JavaScript
[github.com/FontoXML/fontoxpath](https://github.com/FontoXML/fontoxpath "FontoXML/fontoxpath: A minimalistic XPath 3.1 implementation in pure JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">xpath</span> <span class="jser-tag">library</span></p>

XPath 3.1, XQuery 3.1을 구현한 라이브러리입니다.


----

## jsincss | A JS-in-CSS stylesheet loader
[jsincss.com/](https://jsincss.com/ "jsincss | A JS-in-CSS stylesheet loader")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

JavaScript에서 템플릿을 이용 CSS 생성할 수 있고 이벤트에 의해 리액티브하게 CSS를 변경할 수 있는 라이브러리입니다.
플러그인으로 확장할 수 있게 디자인돼 있습니다.

- [tomhodgins/jsincss: A JS-in-CSS stylesheet loader](https://github.com/tomhodgins/jsincss "tomhodgins/jsincss: A JS-in-CSS stylesheet loader")
- [What is a JIC Stylesheet? - Responsive Style](https://responsive.style/theory/what-is-a-jic-stylesheet.html "What is a JIC Stylesheet? - Responsive Style")

----

## BabelEdit - Editor for JSON translation files for Angular & React
[www.codeandweb.com/babeledit](https://www.codeandweb.com/babeledit "BabelEdit - Editor for JSON translation files for Angular & React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">i18n</span> <span class="jser-tag">React</span> <span class="jser-tag">Angular</span> <span class="jser-tag">software</span></p>

JSON 기반의 다국어 파일 에디터입니다.
Angular나 React와 연계한 워크플로우도 소개하고 있습니다.


----
