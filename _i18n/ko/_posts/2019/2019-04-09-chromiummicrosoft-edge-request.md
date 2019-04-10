---
title: "2019-04-09: Chromium 기반 Microsoft Edge 버전 공개, `request` 모듈 메인터넌스 모드로 전환될 예정"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-04-09T00:14:01.804Z
category: JSer
tags:
- Chrome
- MSEdge
- Node.js
- HTTP

---

JSer.info #430 - [2018년 12월에 공지](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/) 한대로 Chromium을 이용한 Microsoft Edge(MSEdge) 프리뷰 버전이 공개됐습니다.

- [Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/ "Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog")
- [What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/)

현재 Windows 10 PC 용만 공개했으며 이후 Windows 7, Windows 8.1, macOS 등도 대응할 예정입니다.
[Microsoft Edge Insider](https://www.microsoftedgeinsider.com/en-us/download/)에서 Beta, Dev, Canary 세 가지 빌드 버전을 공개합니다.

[Microsoft Edge and Chromium Open Source: Our Intent](https://github.com/MicrosoftEdge/MSEdge/blob/master/README.md) 문서나 [What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/)에 Chromium의 어디를 어떻게 컨트리뷰션할 것인지 작성돼 있습니다.
웹 표준의 컨트리뷰션에 관한 계획은 [MSEdgeExplainers](https://github.com/MicrosoftEdge/MSEdgeExplainers)에 작성돼 있으며 이미 HTML Modules와 관련한 내용이 커밋돼 있습니다.

- [\[WIP\] Introduce HTML Modules by dandclark · Pull Request #4505 · whatwg/html](https://github.com/whatwg/html/pull/4505)
- [Intent to Implement: HTML Modules - Google 그룹스](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/ewfRSdqcOd8/w_Fr6rJ3DQAJ)

또, 릴리스 기사에는 새로운 Edge의 User Agent도 소개돼 있는데 호환성을 위해 `Edg`(Edge가 아닌) 문자열을 사용하고 있는 것 같습니다.

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.48 Safari/537.36 Edg/74.1.96.24
```

---

Node.js의 HTTP 라이브러리로 유명한 [request](https://github.com/request/request) 모듈의 메인터넌스 전환 계획이 공지됐습니다.

- [Request’s Past, Present and Future · Issue #3142 · request/request](https://github.com/request/request/issues/3142)

앞으로 새로운 기능이나 비호환적 변경 사항 없이 유지보수 차원의 수정만 합니다.
또, 비권장 공지와 다른 라이브러리로 이전하는 방법 게재에 대한 안건은 해당 이슈에서 계속 논의 중입니다.

request를 대체할 수 있는 라이브러리는 다음 이슈에서 논의되고 있습니다.

- [Alternative libraries to request · Issue #3143 · request/request](https://github.com/request/request/issues/3143)

`request` 모듈에 관심있는 분은 살펴보시길 바랍니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v2.6.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.6.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.6.0 "Release v2.6.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v2.6.0이 릴리스됐습니다.
core-js 2와 3을 지원하며 2.5에 적용된 `ready()`의 비호환적 변경 사항을 되돌렸(revert)습니다.


----

## Release 3.13.1 · nodeca/js-yaml
[github.com/nodeca/js-yaml/releases/tag/3.13.1](https://github.com/nodeca/js-yaml/releases/tag/3.13.1 "Release 3.13.1 · nodeca/js-yaml")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

js-yaml 3.13.1이 릴리스됐습니다.
`load()`로 yaml 파일을 읽어들일 때 파일 내 악의적으로 작성된 코드가 실행되는 취약점을 수정했습니다. 

- [Arbitrary Code Execution in js-yaml | Snyk](https://snyk.io/vuln/SNYK-JS-JSYAML-174129 "Arbitrary Code Execution in js-yaml | Snyk")
- [Fix possible code execution in (already unsafe) load() by rlidwka · Pull Request #480 · nodeca/js-yaml](https://github.com/nodeca/js-yaml/pull/480 "Fix possible code execution in (already unsafe) load() by rlidwka · Pull Request #480 · nodeca/js-yaml")

----

## Request’s Past, Present and Future · Issue #3142 · request/request
[github.com/request/request/issues/3142](https://github.com/request/request/issues/3142 "Request’s Past, Present and Future · Issue #3142 · request/request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span></p>

Node.js의 HTTP 라이브러리인 `request` 모듈이 메인터넌스 모드로 전환됩니다.
새로운 기능 추가나 비호환적 변경 사항 없이 유지보수 차원의 수정만 이뤄집니다.

- [Alternative libraries to request · Issue #3143 · request/request](https://github.com/request/request/issues/3143 "Alternative libraries to request · Issue #3143 · request/request")

----

## Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog
[blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/](https://blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/ "Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

Chromium을 사용한 Microsoft Edge 프리뷰 버전이 릴리스됐습니다. Beta, Dev, Canary 버전을 빌드해 제공하며 향후 macOS도 지원될 예정입니다.

- [What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/#veEezTt4cKDiSZ0P.97 "What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog")


----
<h1 class="site-genre">아티클</h1>

----

## 아메브로 2019: 목소리 블로그에서의 PWA(일본어)
[developers.cyberagent.co.jp/blog/archives/20506/](https://developers.cyberagent.co.jp/blog/archives/20506/ "アメブロ2019: こえのブログでのPWA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>


목소리 블로그에 적용한 프런트엔드 기술 소개 기사입니다.
Fastly CDN의 전체 URL 구조, Cloud Speech-to-Text를 사용한 입력, 사운드 파일을 vmsg를 사용해 클라이언트에서 인코딩 한 후 업로드 하는 방법과 웹 컴포넌트 등에 대해서 이야기합니다.
또, 첫방문과 재방문 시 최적화 방식과 performance budget 설정도 소개합니다.


----

## New WebKit Features in Safari 12.1 | WebKit
[webkit.org/blog/8718/new-webkit-features-in-safari-12-1/](https://webkit.org/blog/8718/new-webkit-features-in-safari-12-1/ "New WebKit Features in Safari 12.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 12.1의 WebKit 관련 변경 사항이 정리돼 있습니다.
다크 모드를 지원하며 ITP 2.1로 갱신됐습니다. Payment Request API와 WebRTC의 개선이 이뤄졌고 EME API/MSE 대응, Intersection Observer, Web Sharer API 대응, Web Inspect 개선 등이 이뤄졌습니다. 


----

## Scroll Anchoring in Firefox 66 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/03/scroll-anchoring-in-firefox-66/](https://hacks.mozilla.org/2019/03/scroll-anchoring-in-firefox-66/ "Scroll Anchoring in Firefox 66 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Scroll Anchoring에 관한 글이며 어떻게 작동하는지 소개합니다.


----

## Managing Z-Index In A Component-Based Web Application — Smashing Magazine
[www.smashingmagazine.com/2019/04/z-index-component-based-web-application/](https://www.smashingmagazine.com/2019/04/z-index-component-based-web-application/ "Managing Z-Index In A Component-Based Web Application — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

컴포넌트 기반 웹 애플리케이션에서 z-index를 관리하는 방법을 소개합니다.
Stacking Context, z-index 관리, 오버레이에 적용하는 요령을 설명합니다.


----

## docker-node/BestPractices.md at master · nodejs/docker-node
[github.com/nodejs/docker-node/blob/master/docs/BestPractices.md](https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md "docker-node/BestPractices.md at master · nodejs/docker-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Docker</span> <span class="jser-tag">node.js</span> <span class="jser-tag">document</span></p>

Docker에서의 Node.js 베스트 프랙티스를 정리한 문서입니다.
환경 변수, Ctrl + C 시그널이 보내지지 않는 문제, yarn 업데이트, root 관련 설정, `CMD`으로 npm run-script 경유하지 않고 직접 실행하는 방법 등을 소개합니다.

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## jeffijoe/typesync: Install missing TypeScript typings for dependencies in your package.json.
[github.com/jeffijoe/typesync](https://github.com/jeffijoe/typesync "jeffijoe/typesync: Install missing TypeScript typings for dependencies in your package.json.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">console</span> <span class="jser-tag">toll</span></p>

`package.json`에 등록된 패키지와 관련된 @types 패키지를 일괄 설치해주는 도구입니다.


----

## typeless-js/typeless: A complete toolkit for building scalable React apps with Typescript.
[github.com/typeless-js/typeless](https://github.com/typeless-js/typeless "typeless-js/typeless: A complete toolkit for building scalable React apps with Typescript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Redux의 전형적인 구조를 내재화 한 React + Redux + Rxjs를 기본 구조로 한 상태 관리 라이브러리입니다.
React Hooks를 지원하고 React에 맞춘 라이프사이클 액션을 제공합니다.


----

## codex-team/editor.js: A block-styled editor with clean JSON output
[github.com/codex-team/editor.js](https://github.com/codex-team/editor.js "codex-team/editor.js: A block-styled editor with clean JSON output")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

블록 스타일의 에디터 라이브러리입니다.
각 블록 단위를 알아보기 쉽게 JSON으로 출력할 수 있습니다.


----

## mgechev/codelyzer: Static analysis for Angular projects.
[github.com/mgechev/codelyzer](https://github.com/mgechev/codelyzer "mgechev/codelyzer: Static analysis for Angular projects.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TSLint를 사용한 Angular 컴포넌트 용 Lint 규칙 세트입니다.


----

## Home | PreVue
[prevue.io/](https://prevue.io/ "Home | PreVue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Tools</span> <span class="jser-tag">design</span></p>

Vue.js를 사용한 UI 프로토타이핑 도구입니다.


----

## kognise/water.css: A just-add-css collection of styles to make simple websites just a little nicer
[github.com/kognise/water.css](https://github.com/kognise/water.css "kognise/water.css: A just-add-css collection of styles to make simple websites just a little nicer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

HTML 요소의 기본 스타일을 정의한 라이브러리입니다.
요소에 스타일을 제공하기 위해서 특정한 CSS 클래스를 정의하지 않습니다. 


----

## leebyron/react-loops: React Loops works with React Hooks as part of the React Velcro Architecture
[github.com/leebyron/react-loops](https://github.com/leebyron/react-loops "leebyron/react-loops: React Loops works with React Hooks as part of the React Velcro Architecture")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

for 루프 제어를 제공하는 React 컴포넌트 라이브러리입니다.

