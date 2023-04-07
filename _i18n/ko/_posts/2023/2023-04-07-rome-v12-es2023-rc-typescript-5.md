---
title: "2023-04-07: Rome v12, ES2023 RC, TypeScript 5에 추가된 옵션"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2023-04-06T15:01:39.093Z
category: JSer
tags:
- React
- Tools
- TypeScript
- node.js
- Next.js

---

JSer.info #638 - Rome v12가 출시되었다.

- [Announcing Rome v12](https://rome.tools/blog/2023/03/28/rome12/)

JSON 지원, TypeScript 5.0 지원, 플러그 조건으로 Import 정렬 가능합니다.
또한, 에러 표시의 개선이나 `--config-path` 플러그 추가등도 있습니다.

----

ECMAScript 2023 출시 후보판(Candidate)이 공개되었습니다.

- [Release ES2023 Candidate April 2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04)

6월에 행해진 Ecma GA(총회)에서 인증을 받으면 정식으로 ES2023가 되어 출시됩니다.
출시여부는 다음 뉴스에 게시됩니다.

- [News - Ecma International](https://www.ecma-international.org/news/)

또한, ECMAScript는 Living Standard이므로, 현재 main 브런치는 ES2024에 포함된 내용이 커밋되어있습니다.

- [Editorial: main is now ES2024 · tc39/ecma262@e356adc](https://github.com/tc39/ecma262/commit/e356adc0545a1a6409c69e41b9626ad3493f6bc8)

ECMAScript 책정 프로세스에 대해서는 다음 문서를 참조해주십시오.

- [The TC39 Process](https://tc39.es/process-document/)
- [ECMAScript · JavaScript Primer #jsprimer](https://jsprimer.net/basic/ecmascript/)

----

[TypeScript 5.0](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/)에는 Decorator 업데이트 등 다양한 변경이 포함되어 있습니다.
그 중에, TypeScript `tsconfig.json`에서 설정하는 옵션도 여럿 추가되었습니다.

다음 글은 새로히 추가된 `moduleResolution: Bundler`, `verbatimModuleSyntax` 옵션에 대한 설명입니다.

- [TypeScript 에서 "moduleResolution": "Node"는 사용하지 않는 편이 좋다](https://blog.s2n.tech/articles/dont-use-moduleresolution-node)
- [TypeScript 5.0에 추가된 verbatimModuleSyntax는 무엇인가?](https://zenn.dev/teppeis/articles/2023-04-typescript-5_0-verbatim-module-syntax)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Node v16.20.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v16.20.0](https://nodejs.org/en/blog/release/v16.20.0 "Node v16.20.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v16.20.0 출시.
undici, npm, corepack 업데이트


----

## Announcing Rome v12
[rome.tools/blog/2023/03/28/rome12/](https://rome.tools/blog/2023/03/28/rome12/ "Announcing Rome v12")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Rome v12 출시.
JSON 지원, TypeScript 5.0 지원, 플러그 조건으로 Import 정렬 대응.
에러 표시의 개선과 `--config-path` 플러그 추가 등


----

## Release v1.7.0 - U Can&#039;t Type This · solidjs/solid
[github.com/solidjs/solid/releases/tag/v1.7.0](https://github.com/solidjs/solid/releases/tag/v1.7.0 "Release v1.7.0 - U Can&#039;t Type This · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Solid v1.7.0 출시.
TypeScript 더 엄격한 자료형을 작성할 수 있도록 개선, `onError`를 대체할 `catchError` 추가 등


----

## Release ES2023 Candidate April 2023 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04](https://github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04 "Release ES2023 Candidate April 2023 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">spec</span></p>

ECMAScript 2023 Candidate 출시.
6월 Ecma GA에서 인증되면 정식으로 출시.


----

## Bun v0.5.9 | Bun Blog
[bun.sh/blog/bun-v0.5.9](https://bun.sh/blog/bun-v0.5.9 "Bun v0.5.9 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun 0.5.9 출시.
파일 변경을 감시해서 프로세스를 재기동하는 `bun --watch` 지원, tarball 의존 지원, 버그 수정 등.
0.6.0에서는 React Server Components를 지원할 예정.


----

## Electron 24.0.0 | Electron
[www.electronjs.org/blog/electron-24-0](https://www.electronjs.org/blog/electron-24-0 "Electron 24.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 24.0.0 출시.
Chromium 112.0.5615.49, Node.js 18.12.1, V8 11.0로 업데이트.
`nativeImage.createThumbnailFromPath(path, size)`의 `maxSize` 옵션을 `size` 옵션으로 변경 등


----

## Release Notes for Safari Technology Preview 167 | WebKit
[webkit.org/blog/14100/release-notes-for-safari-technology-preview-167/](https://webkit.org/blog/14100/release-notes-for-safari-technology-preview-167/ "Release Notes for Safari Technology Preview 167 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 167 출시.
CSS Nesting에서 Top Level `&` 지원, Priority Hints 지원 등


----
<h1 class="site-genre">읽을거리</h1>

----

## React Labs: What We&#039;ve Been Working On – March 2023 – React
[react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023 "React Labs: What We&#039;ve Been Working On – March 2023 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Labs에서 진행하고 있는 프로젝트에 대하여.
React Server Components에서 "use client" 디렉티브를 사용하도록 되어서 서버 컴포넌트에서 async/await를 이용 가능하도록 할 예정.
Suspense에서 CSS나 Font 로드, `<meta>` 등의 빌트인 지원, React 최적화 컴파일 개발상황 등에 대하여


----

## Rails 애플리케이션 프론트엔드를 차근차근 Next.js으로 재배치한 이야기와 그에 따른 회고록 - High Link 테크블로그
[tech.high-link.co.jp/entry/Rails-application-replace-Next.js](https://tech.high-link.co.jp/entry/Rails-application-replace-Next.js "Rails 애플리케이션 프론트엔드를 차근차근 Next.js으로 재배치한 이야기와 그에 따른 회고록 - High Link 테크블로그")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">rails</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

Nginx에서 경로째로 Rails에서 Next.js로 리퀘스트를 갈아끼우면서 이행한 이야기.
인증 문제, `<Link>`에 의한 프론트엔드 라우팅 문제 등 이행 대응에 대하여


----

## CSS text-wrap: balance - Chrome Developers
[developer.chrome.com/en/blog/css-text-wrap-balance/](https://developer.chrome.com/en/blog/css-text-wrap-balance/ "CSS text-wrap: balance - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chrome에 플러그 조건으로 구현된 CSS `text-wrap: balance`에 대하여.
텍스트 블록 개행 위치를 조절하는 타이포그래피 전용 프로퍼티


----

## What are source maps?
[web.dev/source-maps/](https://web.dev/source-maps/ "What are source maps?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Source Maps가 무엇인가에 대하여.
Source Maps 포맷, 읽는 방법, 도구 지원, `x_google_ignoreList` 독자 확장 등에 대하여

- [The \`x\_google\_ignoreList\` source map extension - Chrome Developers](https://developer.chrome.com/en/articles/x-google-ignore-list/ "The \&#x60;x\_google\_ignoreList\&#x60; source map extension - Chrome Developers")

----

## TypeScript 5.0 에 추가된 verbatimModuleSyntax는 무엇인가?
[zenn.dev/teppeis/articles/2023-04-typescript-5\_0-verbatim-module-syntax](https://zenn.dev/teppeis/articles/2023-04-typescript-5_0-verbatim-module-syntax "TypeScript 5.0 에 추가된 verbatimModuleSyntax는 무엇인가?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 5.0에 추가된 `verbatimModuleSyntax`에 대하여.
`import type`를 그째로 삭제, `import`는 남기는 동작에 대하여


----

## TypeScript で&quot;moduleResolution&quot;: &quot;Node&quot; 는 사용하지 않는 편이 좋다
[blog.s2n.tech/articles/dont-use-moduleresolution-node](https://blog.s2n.tech/articles/dont-use-moduleresolution-node "TypeScript で\&quot;moduleResolution\&quot;: \&quot;Node\&quot; 는 사용하지 않는 편이 좋다")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript의 `moduleResolution` 옵션 지정할 수 있는 `Node`/`NodeNext`/`Bundler` 동작차이에 대하여


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## lxsmnsyc/seroval: Stringify JS values
[github.com/lxsmnsyc/seroval](https://github.com/lxsmnsyc/seroval "lxsmnsyc/seroval: Stringify JS values")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScript 객체를 JavaScript 코드화, JSON 인코딩/디코딩하는 라이브러리.
인코딩할지를 기능째로 무효화하는 옵션도 가지고 있다


----

## wantedly/react-declassify: say goodbye to class components
[github.com/wantedly/react-declassify](https://github.com/wantedly/react-declassify "wantedly/react-declassify: say goodbye to class components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

React 클래스 컴포넌트를 Hooks를 사용하도록 하는 변환 도구


----

## unjs/magicast: 🧀 Programmatically modify JavaScript and TypeScript source codes with a simplified, elegant and familiar syntax powered by recast and babel.
[github.com/unjs/magicast](https://github.com/unjs/magicast "unjs/magicast: 🧀 Programmatically modify JavaScript and TypeScript source codes with a simplified, elegant and familiar syntax powered by recast and babel.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScript의 AST조작을 간단히 하기 위한 라이브러리


----
