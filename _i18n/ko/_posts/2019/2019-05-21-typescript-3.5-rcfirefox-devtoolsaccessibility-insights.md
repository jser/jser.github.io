---
title: "2019-05-21: TypeScript 3.5 RC, Firefox DevTools 개선, Accessibility Insights(접근성 테스트)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-05-21T02:19:30.305Z
category: JSer
tags:
- TypeScript
- Firefox
- Accessibility

---

JSer.info #436 - TypeScript 3.5 RC가 릴리스됐습니다.

- [Announcing TypeScript 3.5 RC | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/)
- [TypeScript 3.5 Iteration Plan · Issue #30555 · microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/30555)
- [Breaking Changes · microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-35)

타입 검사와 `--incremental` 옵션을 사용한 빌드 성능이 개선됐습니다.
또, `Omit` 헬퍼 타입이 `lib.d.ts`에 추가됐고 Union 타입과 관련한 프로퍼티 검사도 함께 개선됐습니다.

비호환 변경사항으로 Generic type parameter의 기본이 `{}`에서 `unknown`으로 변경됐습니다.

버전 3.4 까지는 다음과 같이 아무것도 `extends`하지 않는 `T`일 경우 `{}`를 이용하여 오류를 피했습니다.
하지만 3.5부터는 `T`가 `unknown` 타입으로 취급돼 해당 문제가 해결됩니다.

```ts
function foo<T>(x: T): [T, string] {
    return [x, x.toString()]
    //           ~~~~~~~~ error! Property 'toString' does not exist on type 'T'.
}
```

여전히 명시적으로 `T`의 기본 타입을 `{}` 선언해 해결할 수도 있습니다.

```ts
function foo<T extends {}>(x: T): [T, string] {
    return [x, x.toString()]
}
```

또, `tsconfig.json`를 `target:es5`로 설정한 경우 `Object.keys`가 원시 타입 인수를 허용하지 않도록 수정됐습니다.
이는 ES5에서 `Object.keys(10)`와 같이 작성할 경우 예외가 발생해야 한다는 조건이 ECMAScript의 사양이기 때문에 이를 따른 것입니다.

- [Break the Web: Object staticメソッドがES6で仕様変更になった件について](https://gist.github.com/teppeis/c50743a60832560aa1df)

이 외에도 몇 가지 비호환 변경사항이 있으니 [Breaking Changes](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-35)을 살펴보시길 바랍니다.

----

[Accessibility Insights](https://accessibilityinsights.io/) 공식사이트와 함께 웹과 윈도우즈 애플리케이션을 위한 접근성 테스트 도구가 공개됐습니다.
웹 용으로는 크롬 확장 플러그인과 최근 [macOS 버전도 공개된](https://blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/) MSEdge의 Inside Preview 브라우저의 확장 플러그인도 함께 공개됐습니다.

FastPass와 Assessment, 두 가지 시나리오에 대한 접근성 테스트를 지원하며 자동으로 검사하거나 시나리오를 바탕으로 수동으로도 검사할 수 있습니다.
또, 탭 키를 이용한 포커스 이동 가시성, 색상 테스트, WAI-ARIA의 Landmarks 표시 등 접근성 테스트를 위한 보조 기능도 제공합니다. 

다음 페이지에 사용 방법이 설명돼 있으니 관심 있는 분은 함께 살펴보면 좋을 것 같습니다.

- [Accessibility Insights for Web · Accessibility Insights](https://accessibilityinsights.io/docs/en/web/overview)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v3.14.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v3.14.0](https://github.com/lerna/lerna/releases/tag/v3.14.0 "Release v3.14.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

monorepo 관리 도구 lerna 3.14.0이 릴리스됐습니다.
npm publish 시 이중 인증(OTP)과 `--conventional-prerelease`, `--conventional-graduate`를 지원합니다.


----

## Release v2.7.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.7.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.7.0 "Release v2.7.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js 2.7.0이 릴리스됐습니다.
서버 사이드의 로그도 브라우저 콘솔에 출력되며 `store/` 디렉티브 파일 감시 기능이 개선됐습니다.

- [Nuxt.js v2.7.0의 변경 사항과 주목할 지점 정리 - Qiita](https://qiita.com/potato4d/items/43b4f17c73aebc7a2154 "Nuxt.js v2.7.0 の変更点と注目のポイントまとめ - Qiita")(일본어)

----

## Announcing TypeScript 3.5 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/ "Announcing TypeScript 3.5 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.5 RC가 릴리스됐습니다.
타입 검사와 빌드 성능이 개선됐고 `Omit` 헬퍼 타입이 추가됐으며 Union 타입이 개선됐습니다.
비호환 변경사항으로 Generic type parameter의 기본이 `{}`에서 `unknown`으로 변경됐으며 `target:es5`으로 설정 시 `Object.keys`가 원시 타입을 허용하지 않도록 수정됐습니다.


----

## V8 release v7.5 · V8
[v8.dev/blog/v8-release-75](https://v8.dev/blog/v8-release-75 "V8 release v7.5 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v7.5가 릴리스됐습니다.
WebAssembly 컴파일 결과를 암묵적으로 캐시하도록 변경됐고 ECMAScript Proposal의 Numeric separators가 구현됐습니다.
네트워크에서 스크립트를 읽어드리며 파싱할 때 메인스레드에 의해 차단(block)되는 문제가 개선됐습니다.


----

## Release Notes for Safari Technology Preview 82 | WebKit
[webkit.org/blog/8921/release-notes-for-safari-technology-preview-82/](https://webkit.org/blog/8921/release-notes-for-safari-technology-preview-82/ "Release Notes for Safari Technology Preview 82 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 82가 릴리스됐습니다.
Fetch API의 `keepAlive` 지원하며 Web GPU API를 `navigator.gpu`로 옮겼습니다.


----

## Introducing the first Microsoft Edge preview builds for macOS - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/](https://blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/ "Introducing the first Microsoft Edge preview builds for macOS - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">mac</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge의 macOS 버전이 Insider Preview를 통해 릴리스됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## TypeScript 3.0: The unknown Type — Marius Schulz
[mariusschulz.com/blog/typescript-3-0-the-unknown-type](https://mariusschulz.com/blog/typescript-3-0-the-unknown-type "TypeScript 3.0: The unknown Type — Marius Schulz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 3.0에 도입된 `unknown` 타입을 소개합니다.
`any` 타입과의 차이점, `unknown`에 대해 임의로 조작이 불가능한 점, `unknown` 타입의 범위를 좁혀(narrowing) 사용하는 방법 등에 대해 작성돼 있습니다.


----

## Faster smarter JavaScript debugging in Firefox DevTools - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/05/faster-smarter-javascript-debugging-in-firefox/](https://hacks.mozilla.org/2019/05/faster-smarter-javascript-debugging-in-firefox/ "Faster smarter JavaScript debugging in Firefox DevTools - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Firefox 67의 개발자 도구의 변경 사항이 정리돼 있습니다.
불러오기(load) 성능과 중단점 기능이 개선됐습니다. 로그포인트(logpoints) 기능을 지원하며 웹 워커 스크립트로의 전환 시 성능 개선, 소스맵을 활용한 구체적인 내용 출력 개선 등이 이뤄졌습니다.


----

## const assertions are the killer new TypeScript feature
[blog.logrocket.com/const-assertions-are-the-killer-new-typescript-feature-b73451f35802](https://blog.logrocket.com/const-assertions-are-the-killer-new-typescript-feature-b73451f35802 "const assertions are the killer new TypeScript feature")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 3.4에서 도입된 const assertion을 소개합니다.
리터럴의 타입 확대를 방지하거나 객체 속성을 `readonly`로 선언할 수 있습니다.


----

## Google Fonts is Adding font-display 🎉—zachleat.com
[www.zachleat.com/web/google-fonts-display/](https://www.zachleat.com/web/google-fonts-display/ "Google Fonts is Adding font-display 🎉—zachleat.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">fonts</span> <span class="jser-tag">article</span></p>

Google Fonts의 `display` 파라메터를 이용한 `font-display` 프로퍼티 지정 기능에 대한 소개 글입니다.

- [display=swapとはなにか - MOL](https://t32k.me/mol/log/font-display-swap/ "display&#x3D;swapとはなにか - MOL")

----

## \[웹 프론트엔드\] 상태 갱신 로직을 프레임워크에서 떼어(독립)내다 | Kabuku Developers Blog
[www.kabuku.co.jp/developers/framework-agnostic-state-modification](https://www.kabuku.co.jp/developers/framework-agnostic-state-modification "\[웹 프론트엔드\] 상태 갱신 로직을 프레임워크에서 떼어(독립)내다 | Kabuku Developers Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

immer를 사용해 구현한 상태 갱신 로직을 Angular, Vue, React 등의 프레임워크 내에 위치시키는 방법을 소개합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## JS에서의 DoS/ Shibuya.XSS techtalk #11 - Speaker Deck
[speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-11](https://speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-11 "JS에서의 DoS/ Shibuya.XSS techtalk #11 - Speaker Deck")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">slide</span> <span class="jser-tag">security</span></p>

자바스크립트에서 예외가 발생하는 패턴이나 노드에서 크래시가 발생하는 경우에 대한 사례 연구 슬라이드 자료입니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## DasSur.ma – Raw WebAssembly
[dassur.ma/things/raw-wasm/](https://dassur.ma/things/raw-wasm/ "DasSur.ma – Raw WebAssembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

WebAssembly가 stack-based VM 형식으로 어떻게 동작하는지 살펴보는 글입니다.
WebAssembly text 형식인 wat를 직접 작성하며 WebAssembly에서의 모듈 정의, 함수의 정의와 호출, 메모리 확보, wasm 불러오기 등에 대해 설명합니다.

- [Understanding WebAssembly text format - WebAssembly | MDN](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format "Understanding WebAssembly text format - WebAssembly | MDN")

----

## Accessibility Insights
[accessibilityinsights.io/](https://accessibilityinsights.io/ "Accessibility Insights")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">windows</span> <span class="jser-tag">Extension</span></p>

접근성을 검사하는 브라우저 확장 도구입니다.
접근성 검사 항목을 일목요연하게 살펴볼 수 있고 FastPass와 Assessment 두 가지 시나리오 기반의 테스트를 지원합니다.

- [microsoft/accessibility-insights-web: Accessibility Insights for Web](https://github.com/Microsoft/accessibility-insights-web "microsoft/accessibility-insights-web: Accessibility Insights for Web")
- [Introduction to Accessibility Insights for Web - YouTube](https://www.youtube.com/watch?v=U6NY8Cxym5g "Introduction to Accessibility Insights for Web - YouTube")

----

## Inside Microsoft’s surprise decision to work with Google on its Edge browser - The Verge
[www.theverge.com/2019/5/6/18527550/microsoft-chromium-edge-google-history-collaboration](https://www.theverge.com/2019/5/6/18527550/microsoft-chromium-edge-google-history-collaboration "Inside Microsoft’s surprise decision to work with Google on its Edge browser - The Verge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">インタビュー</span> <span class="jser-tag">OSS</span> <span class="jser-tag">google</span> <span class="jser-tag">MS</span></p>

MSEdge가 Chromium 기반으로 변경된 배경이 작성돼 있습니다.
저조한 Edge의 이용률, 최신 기능 구현 지연 등의 문제를 해결하는 하나의 선택 사항이었으나 조직개편이 이뤄지고 Septagon라는 프로토타입과 전환에 대한 공표가 이뤄지면서 실제 작업이 시작된 배경이 자세히 정리돼 있습니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Reakit
[reakit.io/](https://reakit.io/ "Reakit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">library</span></p>

접근성을 고려한 리액트 컴포넌트 라이브러리입니다.
React Hooks를 대응하며 기반 컴포넌트를 제공합니다. 


----

## esxjs/esx: Like JSX, but native and fast
[github.com/esxjs/esx](https://github.com/esxjs/esx "esxjs/esx: Like JSX, but native and fast")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

JSX 스러운 문법을 지원하는 Tagged Template 라이브러리입니다.
또, 리액트를 esx 구문으로 변환하는 바벨 플러그인도 제공해 리액트의 SSR 템플릿 엔진으로도 이용할 수 있습니다.


----
