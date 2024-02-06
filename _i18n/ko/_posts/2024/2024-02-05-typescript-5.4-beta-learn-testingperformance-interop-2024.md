---
title: "2024-02-05: TypeScript 5.4 Beta, Learn Testing/Performance, Interop 2024"
author: "azu"
translator: rewrite0w0
layout: post
date: 2024-02-05T07:09:35.304Z
category: JSer
tags:
- browser
- tutorial
- WebPlatformAPI
- nodejs
- Tools

---

JSer.info #679 - TypeScript 5.4 Beta가 출시되었어요.

- [Announcing TypeScript 5.4 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/)

클로저에 의한 Narrowing 결과 개선, `NoInfer` Utility Type 추가되었어요.
또한, ES2024 `Object.groupBy`/`Map.groupBy`를 지원, Import Attributes 지원도 추가되었어요.
그 외로는, `target: "ES3"`이나 `out` 옵션 비권장화, TypeScript 5.5에서 삭제될 것이 공지 되었어요. TypeScript 5.5에서 삭제될 옵션은 다음 Issue에 정리되어 있구요.

- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909)

---

web.dev에 테스트 퍼포먼스 관련 컨텐츠가 추가되었어요.

- [Learn Testing  |  web.dev](https://web.dev/learn/testing)
- [Learn Performance  |  web.dev](https://web.dev/learn/performance)

여러가지 테스트와 퍼포먼스 관련한 일련의 글을 정리한 페이지에요.

---

브라우저 벤더 관계자가 협력해, 웹플랫폼 간에 상호운용성을 높힐 [Interop 2024](https://wpt.fyi/interop-2024)가 공지되었어요.

- [Interop 2024  |  Blog  |  web.dev](https://web.dev/blog/interop-2024)
- [The web just gets better with Interop 2024 | WebKit](https://webkit.org/blog/14955/the-web-just-gets-better-with-interop/)
- [Interop 2024 Launch - Bocoup](https://bocoup.com/blog/interop-2024)
- [Interop 2024 Launches | Igalia](https://www.igalia.com/2024/interop-2024-launches.html)
- [Microsoft Edge and Interop 2024 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2024/02/01/microsoft-edge-and-interop-2024/)
- [Announcing Interop 2024 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2024/02/announcing-interop-2024/)

매해 협력한 중요분야를 정하는데, 올해 추가된 것으로는 접근성, CSS Nesting, HTTP(S) URLs for WebSockek 등이 있어요.

- [Interop 2024 스타트 | 프론트엔드 Blog | mitsue links](https://www.mitsue.co.jp/knowledge/blog/frontend/202402/02_1152.html)


----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v3.10.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.10.0](https://github.com/nuxt/nuxt/releases/tag/v3.10.0 "Release v3.10.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v3.10.0 출시.
실험적 옵션으로 `sharedPrerenderData` 추가, `useId()`가 SSR할 때 unique한 ID를 반환함을 보증하도록, 안티패턴 검출 강화 등


----

## Announcing TypeScript 5.4 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/ "Announcing TypeScript 5.4 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.4 Beta 출시.
클로저에 의한 Narrowing 결과 개선, `NoInfer` Utility Type 추가.
ES2024 `Object.groupBy`/`Map.groupBy`를 지원, Import Attributes 지원.
`target: "ES3"`이나 `out` 옵션 등 비권장화

- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909 "Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript")

----

## Release v9.0.1 · typicode/husky
[github.com/typicode/husky/releases/tag/v9.0.1](https://github.com/typicode/husky/releases/tag/v9.0.1 "Release v9.0.1 · typicode/husky")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GIt</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

husky v9.0.1 출시.
`husky init`으로 셋업 간략화, git hook 작성 방법 단순화


----
<h1 class="site-genre">읽을거리</h1>

----

## CodeMirror v6로 Zenn Markdown 에디터 만드는 방법
[zenn.dev/team\_zenn/articles/zenn-markdown-editor-by-cm6](https://zenn.dev/team_zenn/articles/zenn-markdown-editor-by-cm6 "CodeMirror v6로 Zenn Markdown 에디터 만드는 방법")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">article</span> <span class="jser-tag">React</span></p>

CodeMirror v6로 Markdown 에디터 구현 방법에 대하여


----

## SameSite 속성과 CSRF와 HSTS - Cookie 기초 지식에서 브라우저 별 엣지 케이스까지 복습하기 - Flatt Security Blog
[blog.flatt.tech/entry/samesite\_csrf\_hsts](https://blog.flatt.tech/entry/samesite_csrf_hsts "SameSite 속성과 CSRF와 HSTS - Cookie 기초 지식에서 브라우저 별 엣지 케이스까지 복습하기 - Flatt Security Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Cookie 속서에 대하여.
Secure/HttpOnly/Domain/Path/SameSite 속성, `__Secure-`/`__Host-` prefix, SameSite 속성의 동작이나 브라우저 기본 동작에 대하여.


----

## Interop 2024 스타트 | 프론트엔드 Blog | mitsue links
[www.mitsue.co.jp/knowledge/blog/frontend/202402/02\_1152.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202402/02_1152.html "Interop 2024 스타트 | 프론트엔드 Blog | mitsue links")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

브라우저 벤더가 추력으로 상호호환성을 향상 시킬 Interop 2024에 대하여.


----

## Node.js 기능이나 패키지 비권장 메세지 알리는 방법 | Web Scratch
[efcl.info/2024/02/04/emitwarning/](https://efcl.info/2024/02/04/emitwarning/ "Node.js 기능이나 패키지 비권장 메세지 알리는 방법 | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

npm나 Node.js 비권장 메세지를 알리는 방법에 대하여.
패키지 비권장화, 코드레벨의 비권장화, 실행 시 비권장화에 관련하여


----

## Import attributes · V8
[v8.dev/features/import-attributes](https://v8.dev/features/import-attributes "Import attributes · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3 Import attributes에 대하여.
`import ... from .... assert { type } `는 의미론적으로 문제가 있기에, `import ... from .... with { type }`으로 변경.


----

## Learn Testing  |  web.dev
[web.dev/learn/testing](https://web.dev/learn/testing "Learn Testing  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">browser</span> <span class="jser-tag">nodejs</span></p>

자동 테스트에 대해 배우늩 튜토리얼.
브라우저나 Node.js 테스트, 테스트 종류, 컴포넌트 테스트, 정적분석 도구 등


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## Learn Performance  |  web.dev
[web.dev/learn/performance?hl&#x3D;en](https://web.dev/learn/performance?hl=en "Learn Performance  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">browser</span></p>

브라우저의 퍼포먼스에 대한 튜토리얼.
자원 불러오기 최적화, JavaScript 최적화, 선로딩, Web Worker에 관련하여


----

## Tappy - Yahoo! 개발자 네트워크
[tappy.yahoo.co.jp/](https://tappy.yahoo.co.jp/ "Tappy - Yahoo! 개발자 네트워크")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span> <span class="jser-tag">mobile</span> <span class="jser-tag">accessibility</span></p>

웹사이트 버튼 등 탭 성공률을 계산해 보여주는 도구.
탭 미스가 일어나기 쉬운 버튼인가 확인하는데 이용 가능.

- [스마트폰 탭 조작 성공률 검출하는 모델 ~ UI 디자인의 사용성 측정 - Yahoo! JAPAN Tech Blog](https://techblog.yahoo.co.jp/entry/2021120930233778/ "스마트폰 탭 조작 성공률 검출하는 모델 ~ UI 디자인의 사용성 측정 - Yahoo! JAPAN Tech Blog")

----

## Compression Streams are now supported on all browsers  |  Blog  |  web.dev
[web.dev/blog/compressionstreams?hl&#x3D;en](https://web.dev/blog/compressionstreams?hl=en "Compression Streams are now supported on all browsers  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

gzip 압축/해제하는 CompressionStream이 모든 브라우저에서 이용 가능.


----
