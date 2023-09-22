---
title: "2023-09-22: Remix v2, Safari 17, TypeScript 다큐멘터리"
author: "azu"
translator: rewrite0w0
layout: post
date : 2023-09-22T11:20:43.678Z
category: JSer
tags:
- Tools
- nodejs
- UI
- Chrome
- debug

---

JSer.info #661 - Remix v2가 출시되었습니다.

- [Release v2.0.0 · remix-run/remix](https://github.com/remix-run/remix/releases/tag/remix%402.0.0)
- [Remix v2 | Remix](https://remix.run/blog/remix-v2)

React 17 지원 종료, Node.js 14/16 지원 종료되었습니다.

옵션이나 기본 동작 변경도 있으며,
V1에서 이행은 `v2_*` 플러그 사용함으로 기능을 하나씩 유효화하며 이행 가능합니다.

- [Upgrading to v2 | Remix](https://remix.run/docs/en/main/start/v2)

라우팅 디렉토리 구조 기본이 Flat Routes으로 되었습니다.

- [Flat Routes · remix-run/remix · Discussion #4482](https://github.com/remix-run/remix/discussions/4482)

2.0.0에는 `v2_*` 플러그 삭제, `remix.config.js` 설정 커맨드 변경이 있습니다.

---

Safari 17.0가 출시 되었습니다.

- [WebKit Features in Safari 17.0 | WebKit](https://webkit.org/blog/14445/webkit-features-in-safari-17-0/)
- [Safari 17 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes)

상당히 많은 변화가 있습니다.

- HTML, `<search>` 요소 대응, `popover` 대응
- CSS, `font-size-adjust`, `text-transform`, `@counter-style`, `image-set()` 대응
- JavaScript, Storage API, 정규표현 `v` 플러그(ES2024), Stage 3의 Set Operations 대응
- 이미지, JPEG XL/HEIC/AV1 코덱 지원

또한, 실험적인 플러그 관리 방법이나 개발자 도구 변경도 있습니다.

---

[TypeScript Origins: The Documentary - YouTube](https://www.youtube.com/watch?v=U6s2pdxebSo) TypeScript가 어떻게 만들어 졌는데 다큐멘터리가 공개되었습니다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/U6s2pdxebSo?si=X3RsrXXWRZQbyT9K" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

오픈소스, 다른 도구나 라이브러리를 위한 접근, TypeScript가 어떻게 퍼져가는가를 보여줍니다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Bun v1.0.2 | Bun Blog
[bun.sh/blog/bun-v1.0.2](https://bun.sh/blog/bun-v1.0.2 "Bun v1.0.2 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.2 출시.
`bunx <pkg>@latest` 최신 패키지 받을 수 없는 버그 수정, `bun --watch` 성능 개선.
Date 경로에 V8 구현, `URL.canParse`/`URLSearchParams.prototype.size` 구현.


----

## Release v2.0.0 · remix-run/remix
[github.com/remix-run/remix/releases/tag/remix%402.0.0](https://github.com/remix-run/remix/releases/tag/remix%402.0.0 "Release v2.0.0 · remix-run/remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">ReleaseNote</span></p>

Remix 2.0.0 출시.
React 17 지원 종료, Node.js 14/16 지원 종료.
V1 이행은 `v2_*` 플러그로 하나씩 유효화 하면서 이행 가능.
2.0.0에는 w`v2_*`플러그 삭제, `remix.config.js` 설정이나 명령어 변경 포함.

- [Remix v2 | Remix](https://remix.run/blog/remix-v2 "Remix v2 | Remix")
- [Upgrading to v2 | Remix](https://remix.run/docs/en/main/start/v2 "Upgrading to v2 | Remix")

----

## Node v18.18.0 (LTS) | Node.js
[nodejs.org/ja/blog/release/v18.18.0](https://nodejs.org/ja/blog/release/v18.18.0 "Node v18.18.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v18.18.0 출시.
`node --import` 플러그 추가, `node:fs`와 `node:stream`으로 Explicit Resource Management 지원


----

## Node v20.7.0 (Current) | Node.js
[nodejs.org/ja/blog/release/v20.7.0](https://nodejs.org/ja/blog/release/v20.7.0 "Node v20.7.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.7.0 출시.
복수의 `--env-file` 지정 지원, npm 10.x으로 업데이트, `process.sourceMapsEnabled` API 추가


----

## Next.js 13.5 | Next.js
[nextjs.org/blog/next-13-5](https://nextjs.org/blog/next-13-5 "Next.js 13.5 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 13.5 출시.
성능 개선, re-exports 하는 패키지 최적화 `optimizePackageImports` 옵션 추가.
실험적 기능으로, `next/image`에 `unstable_getImgProps` 추가, `next dev --experimental-https` 추가.
또한, `create-next-app`가 Bun 지원


----

## eslint-stylistic/eslint-stylistic: Monorepo for ESLint Stylistic plugins and configs
[github.com/eslint-stylistic/eslint-stylistic](https://github.com/eslint-stylistic/eslint-stylistic "eslint-stylistic/eslint-stylistic: Monorepo for ESLint Stylistic plugins and configs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">plugin</span></p>

ESLint 스타일 규칙 관리하는 프로젝트


----

## Ladle v3 | Ladle
[ladle.dev/blog/ladle-v3](https://ladle.dev/blog/ladle-v3 "Ladle v3 | Ladle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 대용 도구 Ladle v3 출시.
SWC 기본 Transpiler로 변경, Node.js 16 지원 종료, CSS in JS 라이브러리 추가 설정 없이 동작 가능


----

## WebKit Features in Safari 17.0 | WebKit
[webkit.org/blog/14445/webkit-features-in-safari-17-0/](https://webkit.org/blog/14445/webkit-features-in-safari-17-0/ "WebKit Features in Safari 17.0 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 17 출시.
HTML `<search>` 요소 대응, `popover` 속성 대응.
CSS, `font-size-adjust`, `text-transform`, `@counter-style`, `image-set()` 대응.
JavaScript, Storage API, 정규표현 `v` 플러그(ES2024), Stage 3의 Set Operations 대응.
이미지 JPEG XL/HEIC/AV1 코덱 지원.
실험적으로 플러그 관리 방법이나 개발자 도구 변경 포함

- [Safari 17 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-17-release-notes "Safari 17 Release Notes | Apple Developer Documentation")

----

## Deno 1.37: Modern JavaScript in Jupyter Notebooks
[deno.com/blog/v1.37](https://deno.com/blog/v1.37 "Deno 1.37: Modern JavaScript in Jupyter Notebooks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">denoe</span> <span class="jser-tag">ReleaseNote</span></p>

Deno v1.37 출시.
`deno jupyter --unstable` 추가, `deno test`에 `--reporter=tap` 레포터 추가, Node.js 호환성 개선.
Lockfile 형식을 version 3으로 업데이트, `std/url` 추가, `std/ulid` 추가


----
<h1 class="site-genre">읽을거리</h1>

----

## How to Find the Exact Line of an Infinite Loop Bug in the code | by Abdu Tawfik | Medium
[abduvik.medium.com/how-to-find-infinite-loops-in-javascript-using-devtools-ea5fc84aec73](https://abduvik.medium.com/how-to-find-infinite-loops-in-javascript-using-devtools-ea5fc84aec73 "How to Find the Exact Line of an Infinite Loop Bug in the code | by Abdu Tawfik | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome에서 무한 루프가 일어날 때 성능 프로파일을 얻는 방법에 대해.
무한 루프가 일어나면 Profile 자체도 완성되지 않기에, 기록을 시작하고 탭 프로세스를 강제적으로 정지하면 얻을 수 있는 방법에 대해서.
또한 동기적 무한 루프와 비동기 무한 루프에 대하여


----

## From WebGL to WebGPU - Chrome for Developers
[developer.chrome.com/en/blog/from-webgl-to-webgpu/](https://developer.chrome.com/en/blog/from-webgl-to-webgpu/ "From WebGL to WebGPU - Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebGL</span> <span class="jser-tag">WebGPU</span> <span class="jser-tag">article</span></p>

WebGL와 WebGPU 차이에 대하여


----

## Introducing runes
[svelte.dev/blog/runes](https://svelte.dev/blog/runes "Introducing runes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">article</span></p>

Svelte 5는 `$state`/`$derived`/`$effect` runes 매크로 사용해 reactive하게 상태 관리 실현.
`$:` 라벨대문에 Reactive 애플리케이션이 복잡해지면 어떤 것이 Reactive 인가 파악하기 어려운 문제가 있었기 때문.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## TypeScript Origins: The Documentary - YouTube
[www.youtube.com/watch?v&#x3D;U6s2pdxebSo](https://www.youtube.com/watch?v=U6s2pdxebSo "TypeScript Origins: The Documentary - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">video</span></p>

TypeScript 다큐멘터리


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## nuejs/nuejs: Build user interfaces with 10x less code. Alternative to React, Vue, and Svelte
[github.com/nuejs/nuejs/tree/master](https://github.com/nuejs/nuejs/tree/master "nuejs/nuejs: Build user interfaces with 10x less code. Alternative to React, Vue, and Svelte")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

적은 코드량으로 표현하는 것을 목표로 하는 Vue/Riot라이크 UI 프레임워크.


----
