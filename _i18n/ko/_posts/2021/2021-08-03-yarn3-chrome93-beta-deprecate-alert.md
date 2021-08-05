---
title: "2021-08-03: Yarn 3.0, Chrome 93 beta, cross origin iframe에서 alert/prompt/confirm 삭제"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-08-03T03:38:52.177Z
category: JSer
tags:
- React
- node.js
- Chrome
- DOM
- browser

---

JSer.info #551 - Yarn 3.0 릴리스.

- [Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻](https://dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07)
- [berry/CHANGELOG.md at master · yarnpkg/berry](https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md#300)

Node.js 10 지원 종료, `.pnp.cjs`로 이름 변경, `@yarnpkg/pnpify`를 세 개의 패키지로 분할 하는 등의 변경 진행.

- `@yarnpkg/sdks`: [Editor SDKs](https://yarnpkg.com/getting-started/editor-sdks)
- `@yarnpkg/pnpify`: PnP와 호환성이 없는 도구를 실행하는 도구
- `@yarnpkg/nm`: `node_modules` linker

또, `exports` 필드 지원, [pnpm](https://pnpm.io/) 스러운 하드 링크 지원, 쉘 구문 지원 개선, ESBuild로 bundle을 지원하는 `@yarnpkg/esbuild-plugin-pnp`가 추가됐다.


----

Chrome 93 beta 릴리스.

- [Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More](https://blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html)

COEP를 보다 쉽게 도입할 수 있도록 하는 [`Cross-Origin-Embedder-Policy：credentialless`](https://github.com/WICG/credentiallessness), [URL Handlers](https://web.dev/pwa-url-handler/)가 Origin Trial로 추가됐다.
또, `AbortSignal.abort()` 메서드 지원, Stage 3의 Error cause와 `Object.hasOwn`를 지원한다.

다크 모드 대응과 관련해 CSS의 `prefers-color-scheme` media query를 사용해 사용자 에이전트가 어떤 color scheme를 우선하는지 판정했다. 하지만 이 속성은 페이지가 로드되고 난 후 알 수 있으므로 페이지 로드 시점에 해당 판정을 할 수 있도록 Client Hint Header로 `Sec-CH-Prefers-Color -Scheme`가 추가됐다.
또, `navigator.userAgent`나 `User-Agent` 헤더의 다음 모델인 User-Agent Client Hints의 API나 헤더 변경도 함께 이뤄졌다.

- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)

---

Chrome 92에서는 cross origin iframe 내에서 `window.{alert, prompt, confirm}`를 사용할 수 없다.

- [1065085 - Implement window.{alert, prompt, confirm} removal from cross-origin iframes - chromium](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085)

이 문제를 대응하는 방법으로 다음과 같은 수단이 이야기된다.

- <del>Chrome 96(12月)까지 사용할 수 있는</del> [Reverse Origin Trial](https://developer.chrome.com/origintrials/#/view_trial/2541156089743802369)를 활성화
- 다이얼로그 UI를 직접 작성하는 방법
- [postMessage를 사용해 부모 문서로 다이얼로그를 출력하는 방법](https://stackoverflow.com/questions/68492434/javascript-dialogs-alert-confirm-and-prompt-in-cross-origin-iframe-does-n)

이 영향으로 CodePen 등 iframe을 사용해 코드를 실행하는 환경, Google Apps Script를 웹 사이트로 공개하고 있는 경우, [Salesforce의 일부 기능](https://help.salesforce.com/articleView?id=000362676&language=en_US&mode=1&type=1) 등이 동작하지 않게 되는 영향이 나오고 있다.
몇몇 웹사이트에 영향을 끼치는 변경으로 Chrome은 해당 내용을 <del>[2021년 8월 15일 까지 연기](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085#c41) 했다(Reverse Origin Trial를 위한 유예 기간).</del> [2022년 1월까지 연기](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085#c72) 했다.

다른 브라우저도 역시 이 사양을 따를 예정이다.

- [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576)
- [Proposal: Disallow cross-origin iframes usage of window.{alert, confirm, prompt} · Issue #5407 · whatwg/html](https://github.com/whatwg/html/issues/5407)

자세한 내용은 다음 문서에도 정리돼 있으니 참고하길 바란다.

- [Cross Origin iframe에서 alert/confirm/prompt를 호출할 수 없다 | blog.jxck.io](https://blog.jxck.io/entries/2021-08-02/3rd-party-iframe-dialog.html)(일본어)


----

<h1 class="site-genre">헤드라인</h1>

----

## Headless UI v1.4: The One With Tabs – Tailwind CSS
[blog.tailwindcss.com/headless-ui-v1-4](https://blog.tailwindcss.com/headless-ui-v1-4 "Headless UI v1.4: The One With Tabs – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Headless UI 1.4 릴리스
Tag 컴포넌트 추가, `Disclosures`와 `Popover`의 Panel 내에 `Button`을 두면 해당 버튼으로 Panel을 닫을 수 있도록 변경


----

## Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻
[dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07](https://dev.to/arcanis/yarn-3-0-performances-esbuild-better-patches-e07 "Yarn 3.0 🚀🤖 Performances, ESBuild, Better Patches, ... - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">ReleaseNote</span></p>

Yarn 3.0 릴리즈.
Node.js 10 지원 종료, `.pnp.cjs`로 이름 변경, `@yarnpkg/pnpify`를 세 개의 패키지로 분해.
`exports` 필드 지원, pnp 스러운 하드 링크 지원, 쉘 구문 지원 개선, ESBuild 지원 등.

- [berry/CHANGELOG.md at master · yarnpkg/berry](https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md#300 "berry/CHANGELOG.md at master · yarnpkg/berry")

----

## Release 3.16.0 - 2021.07.30 · zloirock/core-js
[github.com/zloirock/core-js/releases/tag/v3.16.0](https://github.com/zloirock/core-js/releases/tag/v3.16.0 "Release 3.16.0 - 2021.07.30 · zloirock/core-js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

core.js 3.16.0 릴리스.
Stage 3의 `Array#findLast`, Stage 1의 `Array#filterOut`과 `Array#groupBy` 지원.
Deno도 지원한다.

----

## Node v16.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.6.0/](https://nodejs.org/en/blog/release/v16.6.0/ "Node v16.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 16.6.0 릴리스.
V8 9.2로 업데이트, `http2` 보안 수정 등.

- [V8 release v9.2 · V8](https://v8.dev/blog/v8-release-92 "V8 release v9.2 · V8")

----

## Recoil 0.4 | Recoil
[recoiljs.org/blog/2021/07/30/0.4.0-release/](https://recoiljs.org/blog/2021/07/30/0.4.0-release/ "Recoil 0.4 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.4 릴리스.
캐쉬 폴리쉬를 ₩cachePolicy_UNSTABLE₩로 설정할 수 있고, 트랜잭션을 ₩useRecoilTransaction_UNSTABLE₩으로 이용할 수 있다.
또, TypeScript의 타입 개선이 이뤄졌다.

----

## Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More
[blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html](https://blog.chromium.org/2021/07/chrome-93-multi-screen-window-placement.html "Chromium Blog: Chrome 93: Multi-Screen Window Placement, PWAs as URL Handlers, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 93 beta 릴리스.
`Cross-Origin-Embedder-Policy：credentialless`과 URL Handlers를 Origin Trial로 추가.
`AbortSignal.abort()` 메서드 지원, Stage 3의 Error cause와 `Object.hasOwn` 지원.
Client Hint Header의 `Sec-CH-Prefers-Color-Scheme` 추가, UA Client Hint 갱신 등.

----

## 1065085 - Implement window.\{alert, prompt, confirm\} removal from cross-origin iframes - chromium
[bugs.chromium.org/p/chromium/issues/detail?id&#x3D;1065085](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085 "1065085 - Implement window.\{alert, prompt, confirm\} removal from cross-origin iframes - chromium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">DOM</span> <span class="jser-tag">news</span></p>

Chrome 92에서 cross origin iframe에서의 alert / dialog / prompt가 동작하지 않는다.
회피 방법으로 opt-out Origin Trial(Chrome 95 까지만 유효한 방법), 직접 다이얼로그 UI를 만들기, postMessage를 사용해 부모 문서에서 다이얼 로그를 출력하는 방법 등에 대해서 이야기 나눈 스레드.

- [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576 "Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status")
- [Proposal: Disallow cross-origin iframes usage of window.\{alert, confirm, prompt\} · Issue #5407 · whatwg/html](https://github.com/whatwg/html/issues/5407 "Proposal: Disallow cross-origin iframes usage of window.\{alert, confirm, prompt\} · Issue #5407 · whatwg/html")
- [google chrome - JavaScript dialogs alert(), confirm() and prompt() in cross origin iframe does not work any longer - Stack Overflow](https://stackoverflow.com/questions/68492434/javascript-dialogs-alert-confirm-and-prompt-in-cross-origin-iframe-does-n "google chrome - JavaScript dialogs alert(), confirm() and prompt() in cross origin iframe does not work any longer - Stack Overflow")
- [Chrome Enterprise release notes - Google Chrome Enterprise Help](https://support.google.com/chrome/a/answer/7679408#92&zippy=%2Cchrome "Chrome Enterprise release notes - Google Chrome Enterprise Help")
- [Intent to Remove: Cross origin subframe JS Dialogs](https://groups.google.com/a/chromium.org/g/blink-dev/c/hTOXiBj3D6A/m/gFXmgIz9AwAJ "Intent to Remove: Cross origin subframe JS Dialogs")
- [Cross Origin iframe에서 alert/confirm/prompt를 호출할 수 없다 | blog.jxck.io](https://blog.jxck.io/entries/2021-08-02/3rd-party-iframe-dialog.html "Cross Origin iframe에서 alert/confirm/prompt를 호출할 수 없다 | blog.jxck.io")(일본어)

----

## Release Version 16.7.0 · jsdom/jsdom
[github.com/jsdom/jsdom/releases/tag/16.7.0](https://github.com/jsdom/jsdom/releases/tag/16.7.0 "Release Version 16.7.0 · jsdom/jsdom")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

jsdom 16.7.0 릴리스.
`AbortSignal.abort()` 지원, `getBoundingClientRect()`의 반환 값에 `x`, `y` 추가.
`<textarea>`의 개행 코드 노멀라이제이션을 사양에 맞춰서 변경.

- [The WHATWG Blog — Newline normalizations in form submission](https://blog.whatwg.org/newline-normalizations-in-form-submission "The WHATWG Blog — Newline normalizations in form submission")

----
<h1 class="site-genre">아티클</h1>

----

## How do Chrome extensions impact browser performance?
[www.debugbear.com/blog/chrome-extension-performance-2021](https://www.debugbear.com/blog/chrome-extension-performance-2021 "How do Chrome extensions impact browser performance?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Extension</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

브라우저의 확장이 웹 사이트 성능에 어떤 영향을 주고 있는지 정리 및 소개.
CPU 부하, 첫 회 최초 렌더링에 주는 영향, 백그라운드에서의 CPU 처리, 메모리 소비량.
또, AdBlocker 확장과 관련한 내용도 구체적으로 정리돼 있다.


----

## WebView2 and Electron | Electron Blog
[www.electronjs.org/blog/webview2](https://www.electronjs.org/blog/webview2 "WebView2 and Electron | Electron Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">windows</span> <span class="jser-tag">article</span></p>

Electron과 Windows의 WebView2 아키텍처의 차이를 설명한다.


----

## GraphQL 클라이언트로 urql를 추천하고 싶다(일본어)
[zenn.dev/adwd/articles/f4c5c5120467bb](https://zenn.dev/adwd/articles/f4c5c5120467bb "GraphQLクライアントにurqlをおすすめしたい")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">article</span></p>

GraphQL 클라리언트 라이브러리 urql 소개.
응답을 캐시하는 구조와 방법에 대해서.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## BlueBlazin/thislang: An implementation of a subset of javascript in that subset of javascript.
[github.com/BlueBlazin/thislang](https://github.com/BlueBlazin/thislang "BlueBlazin/thislang: An implementation of a subset of javascript in that subset of javascript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">language</span></p>

JavaScript에서 동작하는 JavaScript 서브셋 구현체.


----

## arcanis/clipanion: Type-safe CLI library with no runtime dependencies
[github.com/arcanis/clipanion](https://github.com/arcanis/clipanion "arcanis/clipanion: Type-safe CLI library with no runtime dependencies")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">console</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

CLI 용 커맨드 라인 인수 파서 라이브러리.
들여쓰기 된 커맨드 지원, typanion과 연계한 벨리데이션, help 지원 등.
Yarn에서 사용하고 있는 라이브러리 이기도 하다.


----

## crcn/sift.js: Use Mongodb queries in JavaScript
[github.com/crcn/sift.js](https://github.com/crcn/sift.js "crcn/sift.js: Use Mongodb queries in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScript 객체를 MongoDB Query 스러운 문법이나 연산자로 검색할 수 있는 라이브러리.


----
