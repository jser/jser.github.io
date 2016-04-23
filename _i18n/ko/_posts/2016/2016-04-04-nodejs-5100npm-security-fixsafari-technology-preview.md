---
title: "2016-04-04 JS: Node.js 5.10.0, npm security fix, Safari Technology Preview"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-04-04T19:46
category: JSer
tags:
    - Node.js
    - npm
    - security
    - safari

---

JSer.info #273 - [Node v5.10.0 (Stable)](https://nodejs.org/en/blog/release/v5.10.0/ "Node v5.10.0 (Stable)")이 릴리즈됐습니다.

다음 절에서 소개하는 [npm](https://www.npmjs.com/ "npm")의 보안 관련 문제를 수정한 버전도 포함돼 있습니다.

[2016-03-17 JS](http://jser.info/ko/2016/03/17/react-webassembly-art-of-javascript/ "2016-03-17のJS")에서도 소개했었지만, Node.js v6에서는 Buffer API가 변경될 예정입니다.

- [Node.js Buffer API Changes — Medium](https://medium.com/@jasnell/node-js-buffer-api-changes-3c21f1048f97#.qk7fmic6y "Node.js Buffer API Changes — Medium")

이 API의 변경과 `--zero-fill-buffers` 명령줄 옵션이, Node.js 5.10.0에 백포드됐습니다.

또, NW.js나 Electron의 환경에서 주로 사용되겠지만 `--no-browser-globals` 플래그로
아래와 같은 글로벌에서 접근할 수 있는 브라우저 호환 API를 노출시키지 않은 옵션도 추가됐습니다.

    setTimeout, clearTimeout, setInterval, clearInterval, setImmediate, clearImmediate
    console

----

[The npm Blog — fixing a bearer token vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")에서는 `npm < 2.15.1` 또는 `npm < 3.8.3`에 있었던 보안 취약점에 관해 소개하고 있스빈다.

npm의 CLI로 실행한 리퀘스트에서, registry 이외에도 token 정보를 송신하던 문제입니다. 기존의 토큰은 [토큰 설정 페이지](https://www.npmjs.com/settings/tokens)에서 취소할 수 있습니다.

- [npm security updates v2.15.1 and v3.8.3 | Node.js](http://nodejs.org/en/blog/vulnerability/npm-tokens-leak-march-2016/ "npm security updates v2.15.1 and v3.8.3 | Node.js")
- 해당 커밋: [config: only send token to registry hosts · npm/npm@f67ecad](https://github.com/npm/npm/commit/f67ecad59e99a03e5aad8e93cd1a086ae087cb29 "config: only send token to registry hosts · npm/npm@f67ecad")

npm 2.x와 3.x 각각 업데이트가 이뤄졌습니다.
이미 설치돼 있는 Node.js 경우는 Node.js 자체를 업데이트 하거나 `npm i -g npm`으로 npm을 업데이트할 필요가 있습니다.

Windows의 경우엔 [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade "npm-windows-upgrade")를 사용하여 `npm i -g npm`와 동일하게 업데이트할 수 있습니다.

npm은 [Azer의 Kik 문제](http://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm "Azer")를 겪고난 후, 여러가지 변경이나 개선을 진행하고 있습니다. 따라서 관련 사항을 모두 살펴보는게 좋을 것 같습니다.

간단히 정리하면

- [npm registry is now fully HTTPS!](http://blog.npmjs.org/post/142077474335/npm-registry-is-now-fully-https "The npm Blog — npm registry is now fully HTTPS!")
  - registry의 완전한 HTTPS화가 이뤄지고 있습니다.
- [changes to npm’s unpublish policy](http://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy "The npm Blog — changes to npm’s unpublish policy")
  - `npm unpublish`의 정책이 변경되고 있습니다.
  - publish하고 난 후 24 시간 이내에만, 지금처럼 `npm unpublish`할 수 있습니다.
  - 24시간이 지난 이후엔 `support@npmjs.com`로 연락해야 합니다.
- 완전히 unpublish(remove)된 모듈은 [Security holding package](https://github.com/npm/security-holder "Security holding package")로 대체되도록 변경됐습니다.
  - 패키지의 이름 공간의 탈취를 방지하기 위함이라고 합니다.
- [Package install scripts vulnerability](http://blog.npmjs.org/post/141702881055/package-install-scripts-vulnerability "The npm Blog — Package install scripts vulnerability")
  - `npm install <module>`한 시점에서 `postinstall`로 임의의 스크립트를 실행할 수 있는 문제와 대책에 대해서도 진행 중 입니다.
  - [npm install script의 취약성 그리고 오픈소스와 신뢰 - teppeis blog](http://teppeis.hatenablog.com/entry/2016/03/npm-vulnerability-and-open-source-trust "npm install script의 취약성 그리고 오픈소스와 신뢰")(일본어)

----

[Safari Technology Preview](https://developer.apple.com/safari/technology-preview/ "Safari Technology Preview")가 공개돼 있습니다.
2주간 마다 갱신되는 개발자 용 버전으로, [Firefox Developer Edition](https://www.mozilla.org/ja/firefox/developer/ "Firefox Developer Edition — Mozilla")이나 Chrome Dev Channel과 같은 느낌입니다.

- [Introducing Safari Technology Preview | WebKit](https://webkit.org/blog/6017/introducing-safari-technology-preview/ "Introducing Safari Technology Preview | WebKit")

Safari Technology Preview에서 문제를 발견하면, Bugzilla나 Bug Reporter를 사용해 알려줄 수 있습니다.

- [Fetch polyfill not working with Safari Technology Preview · Issue #303 · github/fetch](https://github.com/github/fetch/issues/303 "Fetch polyfill not working with Safari Technology Preview · Issue #303 · github/fetch")
- [azu/browser-javascript-resource: Browser JavaScript Resource.](https://github.com/azu/browser-javascript-resource "azu/browser-javascript-resource: Browser JavaScript Resource.")

----
<h1 class="site-genre">헤드라인</h1>

----

## Node v5.10.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.10.0/](https://nodejs.org/en/blog/release/v5.10.0/ "Node v5.10.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.10.0이 릴리즈됐습니다.
npm의 보안을 업데이트한 버전이 포함돼 있습니다.
또, `Buffer(size)`의 allocation 문제에 대응한 `Buffer.alloc`/`Buffer.allocUnsafe`/`Buffer.from`와 `--zero-fill-buffers` 커맨드 라인 옵션이 추가됐습니다.

- [The npm Blog — fixing a bearer token vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")
- [Node.js Buffer API Changes | Linux.com](https://www.linux.com/news/software/applications/893109-nodejs-buffer-api-changes "Node.js Buffer API Changes | Linux.com")

----

## Introducing Safari Technology Preview | WebKit
[webkit.org/blog/6017/introducing-safari-technology-preview/](https://webkit.org/blog/6017/introducing-safari-technology-preview/ "Introducing Safari Technology Preview | WebKit")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span></p>

Safari의 개발자 프리뷰 버전이 공개됐습니다.

----

## Pixi.JS v4 Arrives - Goodboy™ — Goodboy™
[www.goodboydigital.com/pixi-js-v4/](http://www.goodboydigital.com/pixi-js-v4/ "Pixi.JS v4 Arrives - Goodboy™ — Goodboy™")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">game</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">JavaScript</span></p>

PixiJS v4 RC가 릴리즈됐습니다.
WebGL의 코어 구현 부분을 pixi-gl-core으로 분리했고, 임의의 시점에서 RenderTexture를 GC 시킬 수 있도록 변경됐습니다.

- [pixijs/pixi-gl-core: A set of tidy little pixi objects that make working with webGL simpler (WIP, will be moved to pixi group when ready)](https://github.com/pixijs/pixi-gl-core "pixijs/pixi-gl-core: A set of tidy little pixi objects that make working with webGL simpler (WIP, will be moved to pixi group when ready)")

----
<h1 class="site-genre">아티클</h1>

----

## The npm Blog — fixing a bearer token vulnerability
[blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability](http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability "The npm Blog — fixing a bearer token vulnerability")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

npm에 MITM 가능한 취약점이 있어 2.x와 3.x 각각 보안 업데이트가 진행됐습니다.
`npm i -g npm`또는 `npm-windows-upgrade`을 사용하는 것으로 `npm`의 버전을 업데이트할 수 있습니다.

- [felixrieseberg/npm-windows-upgrade: Upgrade npm on Windows](https://github.com/felixrieseberg/npm-windows-upgrade "felixrieseberg/npm-windows-upgrade: Upgrade npm on Windows")

----

## Webpack 2 Tree Shaking Configuration — Modus Create: Front End Development — Medium
[medium.com/modus-create-front-end-development/webpack-2-tree-shaking-configuration-9f1de90f3233](https://medium.com/modus-create-front-end-development/webpack-2-tree-shaking-configuration-9f1de90f3233 "Webpack 2 Tree Shaking Configuration — Modus Create: Front End Development — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span></p>

webpack 1에서 2로의 마이그레이션 방법에 관해 작성돼 있습니다.

----

## React vs Angular2: The fight rages on – Evojam Technology Blog
[tech.evojam.com/2016/03/31/react-vs-angular2-the-fight-rages-on/](http://tech.evojam.com/2016/03/31/react-vs-angular2-the-fight-rages-on/ "React vs Angular2: The fight rages on – Evojam Technology Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">AngularJS</span></p>

React와 AngularJS 2를 비교한 글입니다.

----

## Houdini: Maybe The Most Exciting Development In CSS You&#x27;ve Never Heard Of – Smashing Magazine
[www.smashingmagazine.com/2016/03/houdini-maybe-the-most-exciting-development-in-css-youve-never-heard-of/](https://www.smashingmagazine.com/2016/03/houdini-maybe-the-most-exciting-development-in-css-youve-never-heard-of/ "Houdini: Maybe The Most Exciting Development In CSS You've Never Heard Of – Smashing Magazine")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span></p>

W3C task force의 Houdini는 무엇이며, 어떤 문제를 해결하는 것이 목적인지 설명돼 있습니다.

----

## The JavaScript Event Loop: Explained
[blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/](http://blog.carbonfive.com/2013/10/27/the-javascript-event-loop-explained/ "The JavaScript Event Loop: Explained")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

다이어그램과 함께 JavaScript의 이벤트 루프에 관해 설명합니다.
DOM Event나 WebWorker에 관해서 이해할 수 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## What&#x27;s New in TypeScript? | Build 2016 | Channel 9
[channel9.msdn.com/Events/Build/2016/B881](https://channel9.msdn.com/Events/Build/2016/B881 "What's New in TypeScript? | Build 2016 | Channel 9")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">영상</span></p>

금년에 릴리즈될 TypeScript 관해 소개합니다.
또, non-nullable type이나 npm과 d.ts 관해서도 이야기합니다.

----

## Let&#x27;s Learn ES6 - YouTube
[www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX](https://www.youtube.com/playlist?list=PL57atfCFqj2h5fpdZD-doGEIs0NZxeJTX "Let's Learn ES6 - YouTube")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">영상</span></p>

ES6를 학습할 있는 스크린캐스트가 연재되고 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## buzinas/tslint-eslint-rules: Improve your TSLint with the missing ESLint rules
[github.com/buzinas/tslint-eslint-rules](https://github.com/buzinas/tslint-eslint-rules "buzinas/tslint-eslint-rules: Improve your TSLint with the missing ESLint rules")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

TSLint 용으로 작성된 ESLint 규칙 셋입니다.

----

## aadsm/jschardet: Character encoding auto-detection in JavaScript (port of python&#x27;s chardet)
[github.com/aadsm/jschardet](https://github.com/aadsm/jschardet "aadsm/jschardet: Character encoding auto-detection in JavaScript (port of python's chardet)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">문자코드</span></p>

JavaScript에서 문자코드를 판단(detection)할 수 있는 라이브러리입니다.

----

## rbuckton/prex: Async coordination primitives and extensions on top of ES6 Promises
[github.com/rbuckton/prex](https://github.com/rbuckton/prex "rbuckton/prex: Async coordination primitives and extensions on top of ES6 Promises")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span> <span class="jser-tag">library</span></p>

Promise를 확장하는 보조 라이브러리입니다.
Cancellation, Semaphore, Scheduling API를 제공합니다.

----

## LiquidLabsGmbH/retractor: Expose react internals for E2E testing
[github.com/LiquidLabsGmbH/retractor](https://github.com/LiquidLabsGmbH/retractor "LiquidLabsGmbH/retractor: Expose react internals for E2E testing")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">webdriver</span> <span class="jser-tag">React</span></p>

selenium-webderiver에 React Element를 전달할 수 있도록 `findElement`를 확장한 라이브러리입니다.

----

## bfred-it/object-fit-images: Adds support to object-fit to images on IE9, IE10, IE11, Edge and other old browsers.
[github.com/bfred-it/object-fit-images](https://github.com/bfred-it/object-fit-images "bfred-it/object-fit-images: Adds support to object-fit to images on IE9, IE10, IE11, Edge and other old browsers.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

`object-fit` 속성을 IE에서도 동작할 수 있도록하는 JavaScript 라이브러리입니다.

----

## thejameskyle/the-super-tiny-compiler: Possibly the smallest compiler ever
[github.com/thejameskyle/the-super-tiny-compiler](https://github.com/thejameskyle/the-super-tiny-compiler "thejameskyle/the-super-tiny-compiler: Possibly the smallest compiler ever")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

JavaScript로 작성한 작은 사이즈의 Compiler/Transpiler 구현체 입니다.
주석이 잘 작성돼 있어 컴파일러를 만드는 방법에 관해 배울 수 있습니다.

----

## gajus/create-index: Creates ES6 ./index.js file in target directories that imports and exports all sibling files and directories.
[github.com/gajus/create-index](https://github.com/gajus/create-index "gajus/create-index: Creates ES6 ./index.js file in target directories that imports and exports all sibling files and directories.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

디렉터리를 지정하면, 해당 디렉터리에 있는 모듈을 읽어 `import`하는 `index.js`를 자동으로 생성하는 도구입니다.

----

## Babel Starter Kit ∙ A project template for authoring and publishing JavaScript libraries
[www.kriasoft.com/babel-starter-kit/](https://www.kriasoft.com/babel-starter-kit/ "Babel Starter Kit ∙ A project template for authoring and publishing JavaScript libraries")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Babel을 사용한 Starter Kit입니다.

----
<h1 class="site-genre">도서</h1>

----

## ECSS: Home Page
[ecss.io/](http://ecss.io/ "ECSS: Home Page")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">book</span></p>

ECSS(Enduring CSS)에 관한 서적입니다.
CSS의 설계와 설계 관점 등을 다룹니다.

- [Enduring CSS: writing style sheets for rapidly changing, long-lived projects – Ben Frain](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/ "Enduring CSS: writing style sheets for rapidly changing, long-lived projects – Ben Frain")

----
