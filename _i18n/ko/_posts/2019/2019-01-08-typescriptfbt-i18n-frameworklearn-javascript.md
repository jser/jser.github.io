---
title: "2019-01-08: TypeScript 로드맵, FBT i18n Framework, Learn JavaScript"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-01-08T02:22:36.982Z
category: JSer
tags:
- TypeScript
- i18n
- JavaScript

---

JSer.info #417 - TypeScript의 2019년 로드맵을 아래 깃허브 이슈를 통해 공개했습니다.

- [TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/29288)

현재 `allowJs`나 `checkJS` 등으로 JavaScript도 함께 다룰 수 있으며 더 나아가 JS / JSDoc에 대한 기능을 개선하여 TypeScript로의 이전을 편리하게 할 수 있도록 제공할 계획입니다. 또, TSLint는 구조상 성능 문제가 있는데 이를 개선하면 기존 규칙에도 영향을 줍니다. 그래서 TSLint가 아닌 ESLint를 활용하여 TypeScript의 Lint 지원을 개선할 계획입니다.  

이어 TypeScript Compiler 성능 개선, CLI를 이용한 코드 자동 보정, 공식 문서 개선, 플레이그라운드에서 `tsconfig.json`를 설정할 수 있게 하는 등 앞으로의 개발 및 개선 방향에 대해서 다양하게 정리하고 있습니다.

기능에 대한 로드맵은 아래 문서에 공개하고 있으니 함께 살펴보면 좋을 것 같습니다.

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap)

이번 로드맵에 대한 다양한 의견도 모집하고 있습니다. 의견이 있는 분은 참고하세요.

----

JavaScript에 대해 공부할 수 있는 [Learn JavaScript](https://learnjavascript.online/)를 공개했습니다.

ES2015를 포함해 기본적인 JavaScript 문법 작성 방법에 대해 연습 문제를 풀어보면서 학습할 수 있는 사이트입니다.
모든 문제에 대한 테스트가 있고 그 테스트를 통과할 수 있도록 JavaScript를 작성해 나가는 [code kata](https://en.wikipedia.org/wiki/Kata_%28programming%29) 형식의 서비스입니다.

복습용 Flashcards도 제공하기 때문에 JavaScript에 대해서 알고 싶은 분에게 유용할 것 같습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release 2.9.0 · qunitjs/qunit
[github.com/qunitjs/qunit/releases/tag/2.9.0](https://github.com/qunitjs/qunit/releases/tag/2.9.0 "Release 2.9.0 · qunitjs/qunit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

QUnit 2.9.0을 릴리스했습니다.


----

## Release v2.1.3 · facebook/create-react-app
[github.com/facebook/create-react-app/releases/tag/v2.1.3](https://github.com/facebook/create-react-app/releases/tag/v2.1.3 "Release v2.1.3 · facebook/create-react-app")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">react</span> <span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

create-react-app 2.1.3을 릴리스했습니다.
`webpack-dev-server@3.1.10` 이하 버전에 있던 취약점을 수정한 버전을 도입했습니다.

- [Sniffing Codes in Hot Module Reloading Messages - crblog](https://blog.cal1.cn/post/Sniffing%20Codes%20in%20Hot%20Module%20Reloading%20Messages "Sniffing Codes in Hot Module Reloading Messages - crblog")
- [Release v3.1.11 · webpack/webpack-dev-server](https://github.com/webpack/webpack-dev-server/releases/tag/v3.1.11 "Release v3.1.11 · webpack/webpack-dev-server")
- [npm](https://www.npmjs.com/advisories/725 "npm")

----
<h1 class="site-genre">아티클</h1>

----

## Page Object pattern in JavaScript | LinkedIn
[www.linkedin.com/pulse/page-object-pattern-javascript-vladim%C3%ADr-gorej/](https://www.linkedin.com/pulse/page-object-pattern-javascript-vladim%C3%ADr-gorej/ "Page Object pattern in JavaScript | LinkedIn")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Selenium WebDriver를 사용한 페이지 오브젝트 패턴을 소개하는 글입니다.
페이지 객체란 무엇인지, 요소의 추상화, 지연 처리, Assert 없는 자유로운 페이지 오브젝트 등에 대해 이야기합니다. 


----

## Odi - server-side framework - DEV Community 👩‍💻👨‍💻
[dev.to/dantsk/odi---server-side-framework-2ep7](https://dev.to/dantsk/odi---server-side-framework-2ep7 "Odi - server-side framework - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Node.js 용 서버 사이드 프레임워크 Odi를 소개하는 글입니다. 
Decorator를 사용해 선언적으로 정의하고 TypeScript의 `emitDecoratorMetadata`를 이용한 DTO 시스템을 갖고 있는 프레임워크입니다. 또, 유사한 컨셉을 갖는 Nestjs와의 차이점에 대해서도 이야기합니다.

- [Odi-ts/odi: 🌪🌌 Opinionated, Declarative, Idiomatic framework for building scalable, supportable, enterprise applications and servers.](https://github.com/Odi-ts/odi "Odi-ts/odi: 🌪🌌 Opinionated, Declarative, Idiomatic framework for building scalable, supportable, enterprise applications and servers.")

----

## Neural networks in JavaScript | Scrimba.com
[scrimba.com/g/gneuralnetworks](https://scrimba.com/g/gneuralnetworks "Neural networks in JavaScript | Scrimba.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">library</span></p>

인공 신경망 라이브러리 Brain.js를 상호 작용하여 학습할 수 있는 튜토리얼입니다.

- [BrainJS/brain.js: 🤖 Neural networks in JavaScript](https://github.com/BrainJS/brain.js "BrainJS/brain.js: 🤖 Neural networks in JavaScript")

----

## TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript
[github.com/Microsoft/TypeScript/issues/29288](https://github.com/Microsoft/TypeScript/issues/29288 "TypeScript Roadmap: January - June 2019 · Issue #29288 · Microsoft/TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">issue</span> <span class="jser-tag">article</span></p>

TypeScript의 로드맵을 공개했습니다.
JS/JSDoc 대한 기능과 TSLint가 아니라 ESLint를 활용해 Lint를 좀 더 효율적으로 개선할 계획과 함께 성능, CLI, 공식 문서, Playground 등 다양한 개발 및 개선 계획에 대해 정리하고 있습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Learn JavaScript
[learnjavascript.online/](https://learnjavascript.online/ "Learn JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">webservice</span></p>

테스트를 통과하도록 코드를 작성하면서 JavaScript를 학습할 수 있는 사이트입니다.
각 챕터별로 다양한 연습 문제가 있고 복습을 위한 Flashcards도 준비하고 있습니다.


----

## GoogleChromeLabs/webm-wasm: webm-wasm lets you create webm videos in JavaScript via WebAssembly.
[github.com/GoogleChromeLabs/webm-wasm](https://github.com/GoogleChromeLabs/webm-wasm "GoogleChromeLabs/webm-wasm: webm-wasm lets you create webm videos in JavaScript via WebAssembly.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">C++</span></p>

webm를 인코딩하는 WebAssembly 라이브러리입니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## facebookincubator/fbt: A JavaScript Internationalization Framework
[github.com/facebookincubator/fbt](https://github.com/facebookincubator/fbt "facebookincubator/fbt: A JavaScript Internationalization Framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">u18</span> <span class="jser-tag">library</span> <span class="jser-tag">babel</span></p>

Facebook의 i18n JavaScript 프레임워크입니다.
소스 코드에서 텍스트 수집, 번역 파일 관리, 함수나 JSX에서 번역 표현 등을 지원하며 babel 플러그인을 지원합니다.


----

## RunJS - Write and run JavaScript instantly
[projects.lukehaas.me/runjs/](https://projects.lukehaas.me/runjs/ "RunJS - Write and run JavaScript instantly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mac</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">software</span> <span class="jser-tag">node.js</span></p>

JavaScript를 실행한 결과를 케이스 별로 출력할 수 잇는 macOS 용 어플리케이션입니다.


----
