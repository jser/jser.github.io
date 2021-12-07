---
title: "2021-03-16: Safari Technology Preview 122, React Native 0.64, SvelteKit"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-03-15T23:42:20.954Z
category: JSer
tags:
- Tools
- debug
- Chrome
- CSS
- React

---

JSer.info #531 - Safari Technology Preview 122 릴리스 됐다.

- [Release Notes for Safari Technology Preview 122 | WebKit](https://webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/)

Safari Technology Preview 122에서 여러가지 기능이 구현됐다.
실험 플래그가 붙어 CSS `:focus-visible`와 CSS Color 5의 `color-mix()` / `color-contrast()` / [Relative color syntax](https://drafts.csswg.org/css-color-5/#relative-colors)가 구현됐다.
ES Proposal Stage 3의 [Private method](https://github.com/tc39/proposal-private-methods), [Static private methods](https://github.com/tc39/proposal-static-class-features), [Top-Level await](https://github.com/tc39/proposal-top-level-await), [RegExp Match Indices](https://github.com/tc39/proposal-regexp-match-indices)를 지원한다.
Web Worker와 Service Worker에서 `type: module`를 지원하고 Paint Timing의 (재)유효화 등도 포함됐다.

- [Threading the web with module workers](https://web.dev/module-workers/)
- [Chrome 80부터 Web Worker (Dedicated Worker)에서 ES Modules를 쓸수 있어요](https://nhiroki.jp/2019/12/05/es-modules-for-dedicated-workers)(일본어)

Safari와 직접적인 관계는 없지만 2021년 6월 즈음 릴리스 예정인 ECMAScript 2021의 후보도 공개됐다.

- [Release ES2021 Candidate March 2021 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03)
- [ECMAScript 2021: the final feature set](https://2ality.com/2020/09/ecmascript-2021.html)

---

SvelteKit의 소스 코드가 공개됐다.
SvelteKit은 Svelte 기반의 Next.js와 같은 프레임워크였던 [Sapper](https://sapper.svelte.dev/)를 전환할 목적으로 만들어졌다.

- [sveltejs/kit: A monorepo for SvelteKit and friends](https://github.com/sveltejs/kit)

아직 소스 코드를 공개했을 뿐이며 아직 릴리스는 하지 않은 상태다.
[What is SvelteKit? | SK Incognito](https://sk-incognito.vercel.app/learn/what-is-sveltekit)라는 튜토리얼 사이트에 SvelteKit이 어떠한 프레임워크인지 소개 돼 있으므로 흥미가 있는 사람은 함께 살펴보길 바란다.

---

React Native 0.64가 릴리스 됐다.

- [Announcing React Native 0.64 with Hermes on iOS · React Native](https://reactnative.dev/blog/2021/03/12/version-0.64)

AOT를 활용한 사전 컴파일로 footprint를 최적화 하여 애플리케이션의 시작 속도 등을 개선하는데 목적을 둔 [Hermes JS Engine](https://github.com/facebook/hermes)가 iOS에서도 사용할 수 있도록 됐다.
또, Hermes에 ES2015의 [Proxy object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) 지원이 추가됐다.
그 외로 Metro에서 Inline Requires가 기본적으로 활성화, [React 17](https://reactjs.org/blog/2020/10/20/react-v17.html)로의 업데이트 등의 내용도 포함됐다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v0.9.0 · evanw/esbuild
[github.com/evanw/esbuild/releases/tag/v0.9.0](https://github.com/evanw/esbuild/releases/tag/v0.9.0 "Release v0.9.0 · evanw/esbuild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">relre</span></p>

esbuild 0.9.0 릴리스.
package.json의 `exports` 필드 지원, `esbuild.startService()` API 삭제, banner와 footer를 언어별로 지정할 수 있다.


----

## Release Notes for Safari Technology Preview 122 | WebKit
[webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/](https://webkit.org/blog/11577/release-notes-for-safari-technology-preview-122/ "Release Notes for Safari Technology Preview 122 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 122 릴리스.
실험 플래그가 붙어 CSS `:focus-visible`와 CSS Color 5가 구현, 추가됐다.
ES Proposal의 Private method, Top-Level await, RegExp Match Indices를 지원한다.
Worker에서 `type: module`를 지원하고 Paint Timing을 활성화 했다.


----

## Chromium Blog: Chrome 90 Beta: AV1 Encoder for WebRTC, New Origin Trials, and More
[blog.chromium.org/2021/03/chrome-90-beta-av1-encoder-for-webrtc.html](https://blog.chromium.org/2021/03/chrome-90-beta-av1-encoder-for-webrtc.html "Chromium Blog: Chrome 90 Beta: AV1 Encoder for WebRTC, New Origin Trials, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 90 Beta 릴리스.
AV1 Encoder 지원.
Origin Trial로 `getCurrentBrowsingContextMedia()`, Breakout Box, WebAssembly Exception Handling을 지원한다.
CSS로는 `aspect-ratio`를 사용했을 때 width 또는 height 중 하나가 지정돼 있을 경우 크기(dimension)가 자동으로 추론되도록 개선됐고, `:state` 의사 클래스와 `overflow: clip` 속성을 지원한다.
Feature-Policy를 대신하는 Permissions-Policy, `StaticRange` 지원하며 `navigator.plugins`와 `navigator.mimeTypes`가 빈 값을 반환하도록 변경됐다.


----

## Announcing React Native 0.64 with Hermes on iOS · React Native
[reactnative.dev/blog/2021/03/12/version-0.64](https://reactnative.dev/blog/2021/03/12/version-0.64 "Announcing React Native 0.64 with Hermes on iOS · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.64 릴리스.
iOS에서도 JS 엔진인 Hermes를 사용할 수 있으며 Metro에서 Inline Requires가 기본적으로 활성화 됐다. 
Hermes가 ES Proxy를 지원하고 기본 React 버전이 17로 업데이트 됐다.


----

## sveltejs/kit: A monorepo for SvelteKit and friends
[github.com/sveltejs/kit](https://github.com/sveltejs/kit "sveltejs/kit: A monorepo for SvelteKit and friends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">news</span></p>

SvelteKit의 소스 코드가 공개됐다.


----

## Release ES2021 Candidate March 2021 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03](https://github.com/tc39/ecma262/releases/tag/es2021-candidate-2021-03 "Release ES2021 Candidate March 2021 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2021의 릴리스 후보가 공개됐다. ECMAScript 2021에 들어갈 예정인 기능과 사양이 결정(동결) 됐으므로 master 브랜치는 이제 ES 2022를 다루게 된다.

- [ECMAScript 2021: the final feature set](https://2ality.com/2020/09/ecmascript-2021.html "ECMAScript 2021: the final feature set")
- [proposals/finished-proposals.md at master · tc39/proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md "proposals/finished-proposals.md at master · tc39/proposals")

----

## Socket.IO 4.0.0 | Socket.IO
[socket.io/blog/socket-io-4-release/](https://socket.io/blog/socket-io-4-release/ "Socket.IO 4.0.0 | Socket.IO")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebSocket</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Socket.IO 4.0.0 릴리스.
비호환 변경 사항으로 서버 측의 `io.to()`가 immutable하게 변경됐다. 다만, protocol은 호환성을 유지한다.
`pingTimeout`의 기본값이 5초 에서 20초로 변경 됐으며 Utility 메서드와 `autoUnref` 옵션이 추가됐다.

- [Migrating from 3.x to 4.0 | Socket.IO](https://socket.io/docs/v3/migrating-from-3-x-to-4-0/ "Migrating from 3.x to 4.0 | Socket.IO")
- [fix: set default protocol version to 3 to allow backward compatibilit… by simonemazzoni · Pull Request #616 · socketio/engine.io](https://github.com/socketio/engine.io/pull/616 "fix: set default protocol version to 3 to allow backward compatibilit… by simonemazzoni · Pull Request #616 · socketio/engine.io")

----
<h1 class="site-genre">아티클</h1>

----

## Debugging layout shifts
[web.dev/debugging-layout-shifts/](https://web.dev/debugging-layout-shifts/ "Debugging layout shifts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Layout Instability API를 통해 Cumulative Layout Shift (CLS)를 측정하는 방법과 특징, 디버깅 방식 소개.


----

## Digging Into CSS Logical Properties
[ishadeed.com/article/css-logical-properties/](https://ishadeed.com/article/css-logical-properties/ "Digging Into CSS Logical Properties")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

RTL(right to left)에 대응하여 CSS를 작성하는 방법과 `margin-inline-end` 속성 소개.


----

## 레시피 서비스의 프런트엔드에 CSS in JS를 채택한 이야기 - 쿡 패드 개발자 블로그
[techlife.cookpad.com/entry/2021/03/15/090000](https://techlife.cookpad.com/entry/2021/03/15/090000 "レシピサービスのフロントエンドに CSS in JS を採用した話 - クックパッド開発者ブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

emotion를 사용한 CSS-in-JS 시스템 소개.
styled-components의 기법이 아니라 String Styles를 채택한 이유, stylelint를 사용한 Lint, Jest를 사용한 스냅샷 테스트 등에 대해서 이야기한다.


----

## JavaScript: What is the meaning of this?
[web.dev/javascript-this/](https://web.dev/javascript-this/ "JavaScript: What is the meaning of this?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

여러가지 경우에 따른 `this`의 의미를 설명하는 글.

- [함수와 this · JavaScript Primer #jsprimer](https://jsprimer.net/basic/function-this/ "함수와 this · JavaScript Primer #jsprimer")(일본어)

----

## Beyond Console.log() – Level up Your Debugging Skills - SitePoint
[www.sitepoint.com/beyond-console-log-level-up-your-debugging-skills/](https://www.sitepoint.com/beyond-console-log-level-up-your-debugging-skills/ "Beyond Console.log() – Level up Your Debugging Skills - SitePoint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">console</span> <span class="jser-tag">debug</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">Chrome</span></p>

Console API와 Chrome DevTools를 사용한 디버깅 방법 소개.
로그 포멧, Console API 소개, Dev Tools 상에서 쓸 수 있는 함수, Overrides, VScode와의 연계 등에 대해서 다룬다.


----

## The Death of a Node.js Process - Thomas Hunter II
[thomashunter.name/posts/2021-03-08-the-death-of-a-nodejs-process](https://thomashunter.name/posts/2021-03-08-the-death-of-a-nodejs-process "The Death of a Node.js Process - Thomas Hunter II")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js에 의한 프로세스 종료와 에러를 주제로 한 글.
uncaughtException, unhandledRejection에서의 에러 캐치와 `process.exit`에서의 프로세스 종료 방법.
또, Signal과 이를 핸들링할 수 있는지에 대해 정리돼 있다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Post-Spectre Web Development
[w3c.github.io/webappsec-post-spectre-webdev/](https://w3c.github.io/webappsec-post-spectre-webdev/ "Post-Spectre Web Development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">document</span></p>

Spectre 이후의 웹 개발에서의 위협 모델과 전략를 주제로한 문서.
Isolation, 서브 리소스, 크로스 오리진을 의도한 조작 등에 대해서 정리돼 있다.


----

## What is SvelteKit? | SK Incognito
[sk-incognito.vercel.app/learn/what-is-sveltekit](https://sk-incognito.vercel.app/learn/what-is-sveltekit "What is SvelteKit? | SK Incognito")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">tutorial</span></p>

SvelteKit 튜토리얼 사이트.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Cloud9c/taro: A lightweight 3D game engine for the web.
[github.com/Cloud9c/taro](https://github.com/Cloud9c/taro "Cloud9c/taro: A lightweight 3D game engine for the web.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">3D</span> <span class="jser-tag">game</span> <span class="jser-tag">library</span></p>

three.js와 cannon-es를 사용한 3D 게임 엔진 라이브러리.


----

## rsms/estrella: Lightweight and versatile build tool based on the esbuild compiler
[github.com/rsms/estrella](https://github.com/rsms/estrella "rsms/estrella: Lightweight and versatile build tool based on the esbuild compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">bundler</span></p>

esbuild와 tsc를 래핑한 도구.
esbuild로 빌드 하면서 tsc으로의 타입 검사를 동시에 실행할 수 있는 도구.

- [Through the pipeline: An exploration of front-end bundlers - DEV Community 👩‍💻👨‍💻](https://dev.to/walpolea/through-the-pipeline-an-exploration-of-front-end-bundlers-ea1 "Through the pipeline: An exploration of front-end bundlers - DEV Community 👩‍💻👨‍💻")

----
