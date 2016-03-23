---
title: "2016-02-24 JS: TypeScript 1.8, React의 버저닝(Versioning), Draft.js"
author: azu
translator: U-Yeong Ju
layout: post
date : 2016-02-24T10:11
category: JSer
tags:
    - TypeScript
    - React

---

JSer.info #267 - [TypeScript 1.8](https://blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/ "TypeScript 1.8")이 정식 릴리즈됐습니다.

- [Release v1.8.2 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/releases/tag/v1.8.2 "Release v1.8.2 · Microsoft/TypeScript")
- [What's new in TypeScript · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript#typescript-18 "What&#39;s new in TypeScript · Microsoft/TypeScript Wiki")

JavaScript 파일을 TypeScript 프로젝트에 포함할 수 있도록하는 [--allowJs](https://github.com/Microsoft/TypeScript/wiki/What's-new-in-TypeScript#including-js-files-with---allowjs "--allowJs") 옵션이나 TypeScript 파일을 1개의 JavaScript로 번들링하는 기능이 추가됐습니다.

또, String Literal Types를 대응하고 실행 되지 않는 코드(Unreachable)를 검사하는 [Control flow analysis](https://github.com/Microsoft/TypeScript/wiki/What's-new-in-TypeScript#control-flow-analysis-errors) 등의 기능도 추가됐습니다.

----

[New Versioning Scheme | React](http://facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html "New Versioning Scheme | React")에는 React의 다음 버전인 v15.0.0의 버전 전략 관해 작성돼 있습니다.

소위 [Semantic Versioning](http://semver.org/ "Semantic Versioning")의 1.0.0 이후의 방식으로 버전을 관리하겠다는 방침에 관해 작성돼 있습니다.

또, React를 의존하는 라이브러리에서 React 버전을 지정하는 방법에 관해서도 작성돼 있습니다.
React Component의 라이브러리를 개발하고 있는 사람은 참고하시길 바랍니다.

![react versioning](http://facebook.github.io/react/img/blog/versioning-6.png)

----

Facebook의 Note나 Messenger에서 사용하고 있는 React 기반의 리치 텍스트 에디터 프레임워크인 [Draft.js](https://facebook.github.io/draft-js/ "Draft.js")가 공개돼 있습니다.

텍스트 에디터와 같은 구조를 React로 컴포넌트로 만들 때 여러가지 고민이 필요하게 되는데, 이 프레임워크의 구조를 살펴보면 도움이 될 것 같습니다.

- [Issues and Pitfalls](https://facebook.github.io/draft-js/docs/advanced-topics-issues-and-pitfalls.html#content "Issues and Pitfalls")

----
<h1 class="site-genre">헤드라인</h1>

----

## Node v5.7.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v5.7.0/](https://nodejs.org/en/blog/release/v5.7.0/ "Node v5.7.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 5.7.0이 릴리즈됐습니다.
`Buffer#fill`가 `encoding` 인수를 지원하고, `spawn()`이 `shell` 옵션을 지원하는 등 여러가지 변경사항이 있습니다.

----

## jQuery 1.12.1 and 2.2.1 Released | Official jQuery Blog
[blog.jquery.com/2016/02/22/jquery-1-12-1-and-2-2-1-released/](http://blog.jquery.com/2016/02/22/jquery-1-12-1-and-2-2-1-released/ "jQuery 1.12.1 and 2.2.1 Released | Official jQuery Blog")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">jQuery</span> <span class="jser-tag">ReleaseNote</span></p>

jQuery 1.12.1와 2.2.1이 릴리즈됐습니다.
`.position()`의 버그가 수정됐습니다.

----

## Announcing TypeScript 1.8 | TypeScript
[blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/](https://blogs.msdn.microsoft.com/typescript/2016/02/22/announcing-typescript-1-8-2/ "Announcing TypeScript 1.8 | TypeScript")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.8이 릴리즈됐습니다.
String Literal Types를 지원하고, Control flow를 해석하여 Unreachable한 코드를 검사하는 등의 기능이 추가됐습니다.

----

## ESLint v2.2.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2016/02/eslint-v2.2.0-released](http://eslint.org/blog/2016/02/eslint-v2.2.0-released "ESLint v2.2.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 2.2.0이 릴리즈됐습니다.
`// eslint-disable-next-line`를 지원합니다.

----

## Release ES2016 Draft 2016-02-15 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-20160215](https://github.com/tc39/ecma262/releases/tag/es2016-draft-20160215 "Release ES2016 Draft 2016-02-15 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 2016-02-15이 릴리즈됐습니다.
exponentiation operator 추가, `Object.prototype`를 immutable하게 변경, Unicode 8.0 업데이트, `[[Enumerate]]`과 `Reflect.enumerate`를 삭제하는 등의 변경 사항이 있습니다.

----

## Release v2.10.0 · jscs-dev/node-jscs
[github.com/jscs-dev/node-jscs/releases/tag/v2.10.0](https://github.com/jscs-dev/node-jscs/releases/tag/v2.10.0 "Release v2.10.0 · jscs-dev/node-jscs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

JSCS 2.10.0가 릴리즈됐습니다.
`disallowSpacesInsideTemplateStringPlaceholders`, `requireImportsAlphabetized`가 추가됐습니다.

----

## New Versioning Scheme | React
[facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html](http://facebook.github.io/react/blog/2016/02/19/new-versioning-scheme.html "New Versioning Scheme | React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span></p>

React의 다음 버전은 15.0.0로 릴리즈될 예정입니다.
Semver적 버저닝 방식에 맞추기 위해서 변경됐습니다. 또, React를 의존하는 라이브러리에서 React 버전을 지정하는 방법에 관해서도 작성돼 있습니다.

----
<h1 class="site-genre">아티클</h1>

----

## Why using &#x60;_.chain&#x60; is a mistake. — Making Internets — Medium
[medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba](https://medium.com/making-internets/why-using-chain-is-a-mistake-9bc1f80d51ba "Why using \`\_.chain\` is a mistake. — Making Internets — Medium")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

이 아티클에서는 lodash의 `_.chain`은 확장하기 어려우며 lodash에 포함돼 있어 bundle 사이즈가 커지는 문제가 있다고 작성돼 있습니다.
4.1부터 `lodash/fp`에 functional한 함수가 준비돼 있으므로, 이를 활용하여 같은 역할을 하는 코드를 더 작은 bundle 사이즈로 구현 가능하다고 이야기합니다.

----

## DevTools의 시큐리티 패널 도입에 관해 - Google Developers Japan(일본어)
[googledevjp.blogspot.com/2016/02/draft-devtools.html](http://googledevjp.blogspot.com/2016/02/draft-devtools.html "DevTools へのセキュリティ パネル導入について - Google Developers Japan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span></p>

Chrome 개발자 도구에 "Security" 패널이 추가됐습니다.
TLS 증명서, Mixed Content 등을 확인해볼 수 있습니다.

----

## JavaScript Safe Navigation
[gist.github.com/dakaraphi/6a87168db66fd8f032d2](https://gist.github.com/dakaraphi/6a87168db66fd8f032d2 "JavaScript Safe Navigation")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">proxy</span></p>

Proxy와 Symbol을 사용해 `?.`와 같이 프로퍼티를 체인할 수 있도록 하는 구현 방벙에 관해 작성돼 있습니다.
`safe(o).isNull.next.next.$`와 같이 표현할 수 있습니다.

----

## Aerotwist - The Hack is Back!
[aerotwist.com/blog/the-hack-is-back/](https://aerotwist.com/blog/the-hack-is-back/ "Aerotwist - The Hack is Back!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">canvas</span></p>

`createImageBitmap`와 WebWorker를 사용하는 것으로 이미지의 디코드 처리를 별도의 스레드에서 실행하는 방법에 관해 작성돼 있습니다.

----

## Delivering Octicons with SVG
[github.com/blog/2112-delivering-octicons-with-svg](https://github.com/blog/2112-delivering-octicons-with-svg "Delivering Octicons with SVG")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">fonts</span> <span class="jser-tag">SVG</span></p>

GitHub는 아이콘 폰트를 그만두고, SVG를 사용한 아이콘을 이용하는 방법으로 변경했습니다.
이 아티클에는 SVG를 아이콘으로 이용하는 방법, 성능, 단점과 주의할점에 관해 작성돼 있습니다.

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## talk/webtalk_2016-02-20.pdf at master · momdo/talk(일본어)
[github.com/momdo/talk/blob/master/webtalk\_2016-02-20.pdf](https://github.com/momdo/talk/blob/master/webtalk_2016-02-20.pdf "talk/webtalk\_2016-02-20.pdf at master · momdo/talk")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">W3C</span> <span class="jser-tag">WHATWG</span> <span class="jser-tag">spec</span> <span class="jser-tag">슬라이드</span></p>

웹의 사양은 지속적으로 갱신되고 있다고 이야기하고 있습니다.
WHATWG HTML에서 보는 W3C HTML, CSS WG가 안정됐다고 여기는 것을 CSS Snapshot으로 기술하고 있다는 사실에 관해 이야기합니다.

----

## Google과 Udacity의 JavaScript Promise 온라인 코스 소개 - Google Developers Japan(일본어)
[googledevjp.blogspot.com/2016/02/google-udacity-javascript-promise.html](http://googledevjp.blogspot.com/2016/02/google-udacity-javascript-promise.html "Google と Udacity による JavaScript Promise オンライン コースのご紹介 - Google Developers Japan")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Promises</span></p>

Google과 Udacity가 함께 개발하여 공개한 Promise 온라인 강의를 소개합니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## npm Discover · see what everyone else is using
[www.npmdiscover.com/](http://www.npmdiscover.com/ "npm Discover · see what everyone else is using")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">library</span> <span class="jser-tag">webservice</span> <span class="jser-tag">検索</span></p>

특정 npm 패키지와 함께 사용하는 라이브러리 목록을 알려주는 사이트입니다.
「사람들이 `react`와 함께 사용하고 있는 도구나 라이브러리는 무엇일까」라는 느낌으로 검색할 수 있습니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## trueadm/inferno: An extremely fast, isomorphic JavaScript library for building modern user interfaces
[github.com/trueadm/inferno](https://github.com/trueadm/inferno "trueadm/inferno: An extremely fast, isomorphic JavaScript library for building modern user interfaces")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">VirtualDOM</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React 스러운 Virtual DOM 라이브러리입니다.
템플렛에서 Virtual DOM Element를 만드는 단계에서 정적 컨텐츠인지 동적 컨텐츠인지 판단합니다.
그리고 정적 컨텐츠라면 diff/patch 하지 않는 플래그먼트를 생성하는 것으로 성능 향상을 이루고 있습니다.

- [What&#x27;s the difference from virtual dom libraries? · Issue #21 · trueadm/inferno](https://github.com/trueadm/inferno/issues/21 "What&#x27;s the difference from virtual dom libraries? · Issue #21 · trueadm/inferno")

----

## ziyasal/scientist.js: A JavaScript interpretation of the Ruby library Scientist, a library for carefully refactoring critical paths.
[github.com/ziyasal/scientist.js](https://github.com/ziyasal/scientist.js "ziyasal/scientist.js: A JavaScript interpretation of the Ruby library Scientist, a library for carefully refactoring critical paths.")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span></p>

리팩터링을 도와주는 Ruby 라이브러리인 science의 JavaScript 버전입니다.

- [trello/scientist: A Node.js library for carefully refactoring critical paths in production](https://github.com/trello/scientist "trello/scientist: A Node.js library for carefully refactoring critical paths in production")
- [github/scientist: A Ruby library for carefully refactoring critical paths.](https://github.com/github/scientist "github/scientist: A Ruby library for carefully refactoring critical paths.")

----

## dthree/cash: Cross-platform Linux commands in pure ES6
[github.com/dthree/cash](https://github.com/dthree/cash "dthree/cash: Cross-platform Linux commands in pure ES6")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

JavaScript로 작성한 Linux 커맨드 구현 모음집입니다.
크로스 플랫폼에서 동작하는 `mv`나 `cp` 등의 커맨드를 설치할 수 있습니다.

----

## Draft.js | Rich Text Editor Framework for React
[facebook.github.io/draft-js/](https://facebook.github.io/draft-js/ "Draft.js | Rich Text Editor Framework for React")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">editor</span> <span class="jser-tag">facebook</span> <span class="jser-tag">library</span></p>

Facebook Notes나 messenger에서 사용하고 있는 React의 리치 텍스트 에디터 프레임워크 입니다.
immutable-js를 사용하고 있습니다.

----

## ProjectSeptemberInc/gl-react: OpenGL / WebGL bindings for React to implement complex effects over images and content, in the descriptive VDOM paradigm
[github.com/ProjectSeptemberInc/gl-react](https://github.com/ProjectSeptemberInc/gl-react "ProjectSeptemberInc/gl-react: OpenGL / WebGL bindings for React to implement complex effects over images and content, in the descriptive VDOM paradigm")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

OpenGL / WebGL을 사용한 React Component 라이브러리 입니다.

----
<h1 class="site-genre">도서</h1>

----

## Happy Learn JavaScript Tutorial
[www.happylearnjavascripttutorial.com/](http://www.happylearnjavascripttutorial.com/ "Happy Learn JavaScript Tutorial")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

즐겁게 JavaScript를 배우는 것을 목적으로한 도서입니다.

----

## JavaScript-mancy by Jaime González García [PDF/iPad/Kindle]
[leanpub.com/javascriptmancy-mastering-arcane-art-of-writing-awesome-javascript-for-csharp-developers](https://leanpub.com/javascriptmancy-mastering-arcane-art-of-writing-awesome-javascript-for-csharp-developers "JavaScript-mancy by Jaime González García \[PDF/iPad/Kindle\]")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

C# 개발자를 위한 JavaScript 서적입니다.

----
