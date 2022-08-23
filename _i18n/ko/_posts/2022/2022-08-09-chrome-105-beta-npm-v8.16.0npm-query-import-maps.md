---
title: "2022-08-09: Chrome 105 Beta, npm v8.16.0(npm query), Import Maps"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2022-08-09T04:04:13.003Z
category: JSer
tags:
- React
- mail
- performance
- DOM
- puppeteer

---

JSer.info #604 - Chrome 105 베타가 릴리스 됐다.

- [Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More](https://blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html)

Chrome 105 베타에서는 Custom Highlight API 구현, Container Query 구현, `:has` 의사 클래스 구현, Fetch Upload Streaming 구현 등이 이뤄졌다.
또, `navigator.mediaDevices.getDisplayMedia`에 `systemAudio` 옵션 추가, HTML Sanitizer API 추가, `import.meta.resolve()` 메서드 추가, `Response.json()` 메서드 추가도 진행됐다.

비권장 됐던 WebSQL을 Secure Context 이외의 환경에서는 이용할 수 없게 됐으며 Cookie의 도메인 속성에 아스키가 아닌 문자 사용을 비권장 했다.

----

npm 8.16.0가 릴리스 됐다.

- [Release v8.16.0 · npm/cli](https://github.com/npm/cli/releases/tag/v8.16.0)

npm 8.16.0에서는 `npm query`라는 CSS 셀렉터와 비슷한 쿼리 구문으로 의존 관꼐를 검색할 수 있는 명령이 추가 됐다.
 
예를 들어 아래 명렁어로 `license` 필드가 `MIT`인 패키지를 살펴볼 수 있다.

```
npm query "[license=MIT]"
```

자세한 내용은 아래 문서나 RFC를 참고한다.

- [Introducing the new npm Dependency Selector Syntax | GitHub Changelog](https://github.blog/changelog/2022-08-03-introducing-the-new-npm-dependency-selector-syntax/)
- [rfcs/0000-dependency-selector-syntax.md at 3d5b2130504139bdc8a3b599923aa07d2ff79c96 · npm/rfcs](https://github.com/npm/rfcs/blob/3d5b2130504139bdc8a3b599923aa07d2ff79c96/accepted/0000-dependency-selector-syntax.md)

----

[Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog](https://www.honeybadger.io/blog/import-maps/) 글에서는 Import Maps에 대해 다루고 있다.

Import Maps 사용 방법, 동적 Import Maps 만드는 방법, 필드명의 해쉬와 캐시, 동일 모듈의 복수 버전 이용 방법, CDN과 함께 이용하는 방법을 소개한다.
 

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v7.0.0 · riot/riot
[github.com/riot/riot/releases/tag/v7.0.0](https://github.com/riot/riot/releases/tag/v7.0.0 "Release v7.0.0 · riot/riot")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Riot.js v7.0.0 릴리스.
ESM bundle 개선, runtime `slots` 추가, bundle 크기 개선 등.


----

## Release Inferno v8.0.0 · infernojs/inferno
[github.com/infernojs/inferno/releases/tag/v8.0.0](https://github.com/infernojs/inferno/releases/tag/v8.0.0 "Release Inferno v8.0.0 · infernojs/inferno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Inferno v8.0.0 릴리스.
컴포넌트 라이브 사이클 메서드에 `componentWillMove` / `componentDidAppear` / `componentWillDisappear` 추가, `javascript:` 링크에 대한 경고 추가, 타입스크립트 타입 정의 개선 등.

----

## Release v16.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v16.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v16.0.0 "Release v16.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">puppeteer</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v16.0.0 릴리스.
CDP(Chrome DevTools Protocol)의 auto-attach 메커니즘을 사용하여 Page와 Frame에 대한 접속 안정성을 개선했다.


----

## Release v2.7.0 · parcel-bundler/parcel
[github.com/parcel-bundler/parcel/releases/tag/v2.7.0](https://github.com/parcel-bundler/parcel/releases/tag/v2.7.0 "Release v2.7.0 · parcel-bundler/parcel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

Parcel v2.7.0 릴리스.
플러그인 설정 파일의 확장자로 `.cjs`를 사용할 수 있도록 개선, React Fresh에서 `@emotion/react`를 지원하는 등 다양한 변경 사항이 있다.


----

## Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More
[blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html](https://blog.chromium.org/2022/08/chrome-105-beta-custom-highlighting.html "Chromium Blog: Chrome 105 Beta: Custom Highlighting, Fetch Upload Streaming, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 105 beta 릴리스.
* Custom Highlight API 구현
* Container Query 구현
* `:has` 의사 클래스 구현
* Fetch Upload Streaming 구현
* `navigator.mediaDevices.getDisplayMedia`에 `systemAudio` 옵션 추가
* HTML Sanitizer API 추가
* `import.meta.resolve()` 메서드 추가
* `Response.json()` 메서드 추가
* WebSQL를 Secure Context 이외 환경에서는 이용할 수 없게 됨
* Cookie의 도메인 속성에서 비Ascii 문자 지원을 폐지


----

## Release bun v0.1.7 · oven-sh/bun
[github.com/oven-sh/bun/releases/tag/bun-v0.1.7](https://github.com/oven-sh/bun/releases/tag/bun-v0.1.7 "Release bun v0.1.7 · oven-sh/bun")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Bun 0.1.7 릴리스.
`bun init` 명령어 추가, `bun install`에서 private npm registry 지원, `bun installl`에서 프로젝트 루트의 `prepare` 등 lifecycle hook에 대응.

----

## Release v8.16.0 · npm/cli
[github.com/npm/cli/releases/tag/v8.16.0](https://github.com/npm/cli/releases/tag/v8.16.0 "Release v8.16.0 · npm/cli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm v8.16.0 릴리스.
CSS 셀렉터와 같은 쿼리 구문으로 의존 관계를 검색할 수 있는 `npm query` 명령어가 추가 됐다.

- [Introducing the new npm Dependency Selector Syntax | GitHub Changelog](https://github.blog/changelog/2022-08-03-introducing-the-new-npm-dependency-selector-syntax/ "Introducing the new npm Dependency Selector Syntax | GitHub Changelog")

----
<h1 class="site-genre">아티클</h1>

----

## Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog
[www.honeybadger.io/blog/import-maps/](https://www.honeybadger.io/blog/import-maps/ "Everything You Need to Know About JavaScript Import Maps - Honeybadger Developer Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Import Maps을 소개하는 글.
Import Maps의 사용 방법, 동적인 Import Maps을 만드는 방법, 파일 명의 해시와 캐시, 동일 모듈의 복수 버전 이용 방법, CDN 이용 방법 등에 대해서 다루고 있다.


----

## 500ms to 1.7ms In React: A Journey And A Checklist | Orizens
[orizens.com/blog/500ms-to-1-7ms-in-react-a-journey-and-a%20checklist/](https://orizens.com/blog/500ms-to-1-7ms-in-react-a-journey-and-a%20checklist/ "500ms to 1.7ms In React: A Journey And A Checklist | Orizens")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React 애플리케이션의 성능을 개선 하는 과정을 단계적으로 설명한다.
컴포넌트 분할, 메모화, 프로파일을 사용한 Custom Hooks의 문제 추적 방법 등에 대해서 다룬다.


----

## Parsing command line arguments with \`util.parseArgs()\` in Node.js
[2ality.com/2022/08/node-util-parseargs.html](https://2ality.com/2022/08/node-util-parseargs.html "Parsing command line arguments with \`util.parseArgs()\` in Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 18.3.0에서 추가된 `utils` 모듈의 `parseArgs` 함수 소개.

- [Util | Node.js v18.7.0 Documentation](https://nodejs.org/api/util.html#utilparseargsconfig "Util | Node.js v18.7.0 Documentation")

----

## Checking if a JavaScript native function is monkey patched · mmazzarolo.com
[mmazzarolo.com/blog/2022-07-30-checking-if-a-javascript-native-function-was-monkey-patched/](https://mmazzarolo.com/blog/2022-07-30-checking-if-a-javascript-native-function-was-monkey-patched/ "Checking if a JavaScript native function is monkey patched · mmazzarolo.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScript에서 네이티브 함수가 일명 몽키패치에 의해 덮어써져 있는지를 판단하는 방법을 소개한다.


----

## LINE MUSIC의 성능을 향상시켜준 Vue3 마이그레이션(일본어)
[engineering.linecorp.com/ja/blog/vue3-migration-with-improved-line-music-performance/](https://engineering.linecorp.com/ja/blog/vue3-migration-with-improved-line-music-performance/ "LINE MUSIC のパフォーマンスを向上させた Vue3 マイグレーション")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">refactoring</span></p>

Vue 2.x에서 Vue 3로 이전하는 방법과 이로 인해 개선된 bundle size 등을 소개한다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## sofn-xyz/mailing: Build, test, send emails with React
[github.com/sofn-xyz/mailing](https://github.com/sofn-xyz/mailing "sofn-xyz/mailing: Build, test, send emails with React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">mail</span> <span class="jser-tag">library</span></p>

React 컴포넌트 기반으로 메일 콘텐츠 개발을 할 수 있는 툴킷
MJML을 기반으로 개발 돼 있으며 로컬에서 메일의 렌더링 결과를 보면서 컴포넌트 문법으로 메일 콘텐츠를 작성할 수 있다.

- [MJML - The Responsive Email Framework](https://mjml.io/ "MJML - The Responsive Email Framework")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## mjmlio/mjml: MJML: the only framework that makes responsive-email easy
[github.com/mjmlio/mjml](https://github.com/mjmlio/mjml "mjmlio/mjml: MJML: the only framework that makes responsive-email easy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mail</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

MJML 마크업 언어를 바탕으로 반응형 메일을 작성할 수 있는 프레임워크.


----

