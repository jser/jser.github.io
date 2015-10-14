---
title: "2015-09-25의 JS: Firefox 41.0, npm 3.x stable 릴리즈, XRegExp 3.0.0"
author: azu
translator: U-Yeong Ju
layout: post
date : 2015-09-25T15:18
category: JSer
tags:
    - Firefox
    - npm
    - node
    - regexp
    - library

---


JSer.info #246 - Firefox 41.0가 릴리즈 됐습니다.

- [Firefox - Notes(41.0)](https://www.mozilla.org/en-US/firefox/41.0/releasenotes/ "Firefox - Notes(41.0)")
- [Firefox 41 for developers - Mozilla | MDN](https://developer.mozilla.org/en/Firefox/Releases/41 "Firefox 41 for developers - Mozilla | MDN")

CSS의 세로쓰기 문장에 관한 레이아웃 기능([writing-mode](https://developer.mozilla.org/en/docs/Web/CSS/writing-mode "writing-mode"))이 디폴트로 활성화 됐습니다.
ES6에 관한 변경 사항으로는 `Symbol.species`, `new.target`의 지원, destructuring이나 let 구문의 사양을 따르도록 변경됐습니다.

또, `Navigator.onLine`이 Windows와 Mac에서 온전하게 동작하고, Notifications API 등을 Web Worker 내에서 이용 가능하도록 변경됐습니다.


----
npm v3.x이 stable로 릴리즈 됐습니다.

- [The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...](http://blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the "The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...")

v3.3.2까지는 베타로 릴리즈 됐기 때문에, `npm install npm`으로 설치할 수 없었지만 v3.3.3부터 stable로 릴리즈됐기 때문에 설치할 수 있습니다.

Node.js 내에 포함(bundle) 되는 것은 다음 메이저 업데이트 때 겠지만 아래 문서를 읽고 npm v3.x의 변경 사항에 관해서 이해해 두는게 좋을 것 같습니다.

- [npm/CHANGELOG.md at master · npm/npm](https://github.com/npm/npm/blob/master/CHANGELOG.md "npm/CHANGELOG.md at master · npm/npm")
- [npm3 ? // Speaker Deck](https://speakerdeck.com/watilde/npm3)(일본어)
- [NPM 3 Beta엔 Windows 유저에게 좋은 소식이 있습니다](http://www.infoq.com/jp/news/2015/07/npm)(일본어)

의존 관계 디렉터리의 구조가 flat하게 변경 됐으며, peerDependencies가 기본으로 설치되지 않는 등 보다 안전한 설치가 가능하도록 변경됐습니다.

또, 현재 `npm link`에 관한 문제나 `npm install` 시 시간이 걸리는 등의 npm v3.x 관련한 이슈가 등록돼 있습니다.

- [EEXIST error: npm@3 link issues with .bin files · Issue #9702 · npm/npm](https://github.com/npm/npm/issues/9702 "EEXIST error: npm@3 link issues with .bin files · Issue #9702 · npm/npm")
- [npm@3 wants to be faster · Issue #8826 · npm/npm](https://github.com/npm/npm/issues/8826 "npm@3 wants to be faster · Issue #8826 · npm/npm")(현재 닫힌 상태)

-----

확장된 정규표현식을 제공하는 [XRegExp](http://xregexp.com/ "XRegExp") 3.0.0이 릴리즈됐습니다.

- [Flagrant Badassery » XRegExp 3.0.0!](http://blog.stevenlevithan.com/archives/xregexp-3-0-0 "Flagrant Badassery » XRegExp 3.0.0!")
- [Version history :: XRegExp](http://xregexp.com/history/ "Version history :: XRegExp")

3.0.0에서는 ES6를 따르는 변경됐고 Unicode 지원하며 속도 개선 등이 이루어 졌습니다.

----
<h1 class="site-genre">헤드라인</h1>

----

## Firefox - Notes(41.0)
[www.mozilla.jp/firefox/41.0/releasenotes/](http://www.mozilla.com/firefox/41.0/releasenotes/ "Firefox - Notes(41.0)")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 41.0가 릴리즈 됐습니다.
CSS의 세로쓰기 문장에 관한 레이아웃 기능이 디폴트로 활성화 됐으며 `Symbol.species`, `new.target`의 지원하고 Notifications API를 Web Worker 내에서 이용 가능하도록 변경되는 등 여러가지 변경 사항이 있습니다.

- [Firefox 41 for developers - Mozilla | MDN](https://developer.mozilla.org/en/Firefox/Releases/41 "Firefox 41 for developers - Mozilla | MDN")

----

## Node v4.1.0 (Stable) | Node.js
[nodejs.org/en/blog/release/v4.1.0/](https://nodejs.org/en/blog/release/v4.1.0/ "Node v4.1.0 (Stable) | Node.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v4.1.0이 릴리즈 됐습니다.
Buffer의 작성 방법과 fs.WriteStream의 기입(bulk writes) 속도가 개선 되는 등 다양한 변경 사항이 있습니다.

----

## The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...
[blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the](http://blog.npmjs.org/post/129378362260/npm-weekly-29-npm-3-out-of-beta-nick-out-of-the "The npm Blog — npm weekly #29: npm 3 out of beta, Nick out of the...")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 3.x가 latest로써 릴리즈됐습니다.
`npm install -g npm`으로 npm 3.x가 설치 가능하도록 변경됐습니다.

- [Release v3.0.0 · npm/npm](https://github.com/npm/npm/releases/tag/v3.0.0 "Release v3.0.0 · npm/npm")

----

## Announcing TypeScript 1.6 - TypeScript - Site Home - MSDN Blogs
[blogs.msdn.com/b/typescript/archive/2015/09/16/announcing-typescript-1-6.aspx](http://blogs.msdn.com/b/typescript/archive/2015/09/16/announcing-typescript-1-6.aspx "Announcing TypeScript 1.6 - TypeScript - Site Home - MSDN Blogs")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 1.6이 릴리즈됐습니다.
JSX(TSX), Class expressions, User defined type guards, Intersection types, Abstract classes 등이 추가됐고 module resolution logic 개선됐습니다.

- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-16 "Breaking Changes · Microsoft/TypeScript Wiki")

----

## Release 1.0 · bosonic/bosonic
[github.com/bosonic/bosonic/releases/tag/v1.0](https://github.com/bosonic/bosonic/releases/tag/v1.0 "Release 1.0 · bosonic/bosonic")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebComponents</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Web Components를 다루는 라이브러리인 Bosonic 1.0이 릴리즈됐습니다.

- [Bosonic Web Component](http://bosonic.github.io/ "Bosonic Web Component")

----

## Flagrant Badassery » XRegExp 3.0.0!
[blog.stevenlevithan.com/archives/xregexp-3-0-0](http://blog.stevenlevithan.com/archives/xregexp-3-0-0 "Flagrant Badassery » XRegExp 3.0.0!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">正規表現</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span></p>

확장된 정규표현식을 제공하는 라이브러리인 XRegExp 3.0.0이 릴리즈됐습니다.
Unicode에 관한 지원을 개선했으며 `A`(astral) 플래그를 추가했습니다. 또한 ES6에 사양에 맞춰 변경됐습니다.

----

## RxJS/CHANGELOG.md at 5.0.0-alpha.1 · ReactiveX/RxJS
[github.com/ReactiveX/RxJS/blob/5.0.0-alpha.1/CHANGELOG.md](https://github.com/ReactiveX/RxJS/blob/5.0.0-alpha.1/CHANGELOG.md "RxJS/CHANGELOG.md at 5.0.0-alpha.1 · ReactiveX/RxJS")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rx</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ReactiveX/RxJS 5.0.0α가 릴리즈됐습니다.

----

## 릴리즈 버전 10547 : Microsoft Edge Dev
[dev.modern.ie/platform/changelog/desktop/10547/](https://dev.modern.ie/platform/changelog/desktop/10547/ "リリース バージョン 10547 : Microsoft Edge Dev")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge Build 10547가 릴리즈됐습니다.
`<template>`、`<picture>`가 추가됐고, `<a download>`를 대응했습니다. SVG에서 외부 컨텐츠를 로드할 수 있고, 플래그를 설정하여 Async Function, `**` 연산자를 사용할 수 있습니다.

- [Microsoft Edge 변경 로그 - Windows 10 Insider Preview Build 10547 - Browser](http://browser.hatenablog.com/entry/2015/09/21/180947 "Microsoft Edge 변경 로그 - Windows 10 Insider Preview Build 10547 - Browser")(일본어)

----

## ESLint v1.5.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2015/09/eslint-v1.5.0-released/](http://eslint.org/blog/2015/09/eslint-v1.5.0-released/ "ESLint v1.5.0 released - ESLint - Pluggable JavaScript linter")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint v1.5.0이 릴리즈됐습니다.
`--fix` 명령줄 플래그, `--debug` 플래그 등이 추가됐습니다.

----

## Release ES2016 Draft 1 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2016-draft-1](https://github.com/tc39/ecma262/releases/tag/es2016-draft-1 "Release ES2016 Draft 1 · tc39/ecma262")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span></p>

ES2016 Draft 1이 릴리즈됐습니다.
사양을 Word에서 [Ecmarkup](http://bterlson.github.io/ecmarkup/)으로 작성할 수 있도록 변경됐으며 Github를 통해 릴리즈했습니다.

- [New in ECMAScript 2016, JavaScript&#x27;s First Yearly Release](http://www.infoq.com/presentations/ecmascript-2016 "New in ECMAScript 2016, JavaScript's First Yearly Release")

----
<h1 class="site-genre">아티클</h1>


----

## React.js v0.14 changes - blog.koba04.com(일본어)
[blog.koba04.com/post/2015/09/22/react-js-v014-changes/](http://blog.koba04.com/post/2015/09/22/react-js-v014-changes/ "React.js v0.14 changes - blog.koba04.com")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

React 0.14에서 변경된 사항이 정리돼 있습니다.

----

## Pointer Events Will Make Cross-Browser Touch Support Easy
[www.sitepoint.com/pointer-events-will-make-cross-browsers-touch-support-easy/](http://www.sitepoint.com/pointer-events-will-make-cross-browsers-touch-support-easy/ "Pointer Events Will Make Cross-Browser Touch Support Easy")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span></p>

Pointer Events의 컨셉과 실제 사용 방법에 관해 설명합니다.
feature detection을 하는 방법, 제스처를 다루는 MSGesture object에 관해서도 작성돼 있습니다.

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## ESDoc Hosting Service - hosts documentation for JavaScript(ES6) with ESDoc
[doc.esdoc.org/](https://doc.esdoc.org/ "ESDoc Hosting Service - hosts documentation for JavaScript(ES6) with ESDoc")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JSDoc</span> <span class="jser-tag">document</span></p>

[ESDoc](https://esdoc.org)로 작성한 문서를 호스팅하는 서비스입니다.
GitHub 저장소의 URL을 등록하면 ESDoc에 의해 문서가 생성됩니다. `esdoc.json` 설정 파일이 없는 경우에는 `src/`의 코드를 기초로 문서를 생성합니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mantoni/eslint_d.js
[github.com/mantoni/eslint\_d.js](https://github.com/mantoni/eslint_d.js "mantoni/eslint_d.js")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">서버</span></p>

ESLint를 서버로 실행하여 코드를 검증하는 도구입니다.
최초 실행 시 발생하는 오버 헤드를 줄일 수 있으므로 조금 더 빠르게 검증할 수 있습니다.

----

## ConquestArrow/dtsmake · GitHub
[github.com/ConquestArrow/dtsmake](https://github.com/ConquestArrow/dtsmake "ConquestArrow/dtsmake · GitHub")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaScript를 전달하여 d.ts를 생성하는 도구입니다.

- [TypeScript 타입 정의 파일의 형식과 생성 도구 dtsmake - Qiita](http://qiita.com/ConquestArrow/items/450f961c3d54bc932cf3 "타입 정의 파일의 형식과 생성 도구 dtsmake - Qiita")(일본어)

----

## fireball-x/editor-framework
[github.com/fireball-x/editor-framework](https://github.com/fireball-x/editor-framework "fireball-x/editor-framework")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">Electron</span></p>

Electron과 Polymer를 기반으로 만든 에디터 용 프레임워크입니다.

----

## Release the docs!
[sassdoc.com/](http://sassdoc.com/ "Release the docs!")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">Sass</span> <span class="jser-tag">document</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JSDoc</span></p>

Sass의 주석을 이용해 에너테이션을 작성하여 문서를 생성할 수 있는 도구입니다.

----
<h1 class="site-genre">도서</h1>

----

## Amazon: 속성 ECMAScript6: 차세대 표준 JavaScript를 지금 당장 마스터！ [Kindle용]: 山田祥寛(일본어)
[www.amazon.co.jp/dp/B014MS5XWK?tag=amazon0abac-22](http://www.amazon.co.jp/dp/B014MS5XWK?tag=amazon0abac-22 "Amazon: 속성 ECMAScript6: 차세대 표준 JavaScript를 지금 당장 마스터！ [Kindle용]: 山田祥寛")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

ES6에 관한 Kindle 용 도서입니다.

- [【신간소개】『속성 ECMAScript 6』 발매, 다음 버전 JavaScript사양을 단기간에 케치 업！：CodeZine（코드진）](http://codezine.jp/article/detail/8963 "【신간소개】『속성 ECMAScript 6』 발매, 다음 버전 JavaScript사양을 단기간에 케치 업！：CodeZine（코드진）")(일본어)

----

## Building Isomorphic JavaScript Apps: From Concept to Implementation to Real-World Solutions: Jason Strimpel, Maxime Najim: 9781491932933: Amazon.com: Books
[www.amazon.com/dp/1491932937/](http://www.amazon.com/dp/1491932937/ "Building Isomorphic JavaScript Apps: From Concept to Implementation to Real-World Solutions: Jason Strimpel, Maxime Najim: 9781491932933: Amazon.com: Books")

<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2016년 4월 30일 발매
Isomorphic에 관한 O'Reilly의 책입니다.

----
