---
title: "2021-07-27: vscode-js-debug, Privacy Sandbox Timeline, 작은 브라우저를 만드는 방법"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-07-27T12:52:36.749Z
category: JSer
tags:
- node.js
- browser
- security
- Tools
- Chrome

---

JSer.info #550 - vscode-js-debug는 VSCode에서 브라우저의 디버거에 접속해 JavaScript를 디버깅하는 VSCode 확장이다.
이 vscode-js-debug가 VScode에 bundle 되도록 됐다.

- [Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/)
- [microsoft/vscode-js-debug: The VS Code JavaScript debugger](https://github.com/microsoft/vscode-js-debug)

vscode-js-debug는 Chrome 및 MSEdge 등의 브라우저 디버거에 접속할 수 있다.
구조로는 [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/)(DAP)라는 개발 도구(VScode 등)과 디버거(브라우저나 노드 등)를 중계하는 Adapter를 사용하고 있다.

DAP는 [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)(LSP)와 비슷하게 개발 도구와 각종 언어를 중계하는 프로토콜을 정하고 있다.
개발 도구 등은 DAP를 지원하는 것으로 각종 언어 용 디버깅 기능을 일일이 개발하지 않아도 대응할 수 있다.

----

[Privacy Sandbox Timeline](https://privacysandbox.com/timeline/)에는 Google의 Privacy Sandbox라고 불리는 third-party cookies를 폐지하기 위한 Proposal과 관련된 로드맵을 공개돼 있다.

Privacy Sandbox의 각 Proposal 별로 어떤 일정으로 구현 및 테스트 할지 정리돼 있다.

---

[작은 웹 브라우저를 만들어보자](https://browserbook.shift-js.info/)(일본어)에서 Rust로 웹 브라우저를 만들어가면서 브라우저의 렌더링 구조와 보안 등에 대해 학습할 수 있는 과정을 다루고 있다.

작은 브라우저를 만들면서 브라우저의 내부 구조에 대해 배우는 것을 목적으로 하고 있는 교재이며 현재는 WIP(Working In Progress) 상태인 장이 많지만 계속해서 작성될 것으로 보인다.

덧붙여 Rust로 브라우저를 만들어 보면서 학습할 수 있는 튜토리얼로는 "Let's build a browser engine!"이 유명하다.
관심이 있는 사람은 함께 읽어보면 좋을 것.

- [Let's build a browser engine! Part 1: Getting started](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
	- [브라우저를 만드는 방법 - Speaker Deck](https://speakerdeck.com/keiya01/burauzafalsezuo-rifang)(일본어)
	- [「Let's build a browser engine!」를 읽고 Rust로 간이 렌더링 엔진을 만들었다 - dackdive's blog](https://dackdive.hateblo.jp/entry/2021/02/23/113522)(일본어)


----

<h1 class="site-genre">헤드라인</h1>

----

## Version 2.0 released : Node-RED
[nodered.org/blog/2021/07/20/version-2-0-released](https://nodered.org/blog/2021/07/20/version-2-0-released "Version 2.0 released : Node-RED")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

IoT 디바이스 등을 다루는 비쥬얼 프로그래밍 환경 Node-RED 2.0.0 릴리스.
Node-RED는 IBM사에서 개발한 IoT 분야의 대표 front-end 개발용 미들웨어 도구([참고](https://www.koreascience.or.kr/article/JAKO201827750146296.pdf)).

- [Release 2.0.0: Milestone Release · node-red/node-red](https://github.com/node-red/node-red/releases/tag/2.0.0 "Release 2.0.0: Milestone Release · node-red/node-red")

----
<h1 class="site-genre">아티클</h1>

----

## URLPattern brings routing to the web platform
[web.dev/urlpattern/](https://web.dev/urlpattern/ "URLPattern brings routing to the web platform")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

npm 패키지 path-to-regexp 같이 URL의 패턴 매치를 다루는 `URLPattern` 자바스크립트 객체를 소개하는 글.
기본적인 사용법, 캡쳐, 브라우저 지원과 폴리필을 설명.
`URLPattern`의 목표는 브라우저 / 서버사이드에서 사용하는 라우팅 패턴 매칭을 최대한 표준화시키는 것.


----

## Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/](https://blogs.windows.com/msedgedev/2021/07/16/easier-debugging-developer-tools-in-visual-studio-code/ "Easier browser debugging with Developer Tools integration in Visual Studio Code - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

VSCode에서 Chrome와 MSEdge의 Debugger에 접속하는 vscode-js-debug 확장 소개.
DAP(Debug Adapter Protocol)의 Protocol Adapter를 사용하여 VScode에서 브라우저 디버깅에 접속한다.

- [microsoft/vscode-js-debug: The VS Code JavaScript debugger](https://github.com/microsoft/vscode-js-debug "microsoft/vscode-js-debug: The VS Code JavaScript debugger")

----

## Fastly Launches New Era of Highly-Secure Serverless JavaScript With Zero Cold Starts | Fastly
[www.fastly.com/press/press-releases/fastly-launches-new-era-of-highly-secure-serverless-javascript-with-zero](https://www.fastly.com/press/press-releases/fastly-launches-new-era-of-highly-secure-serverless-javascript-with-zero "Fastly Launches New Era of Highly-Secure Serverless JavaScript With Zero Cold Starts | Fastly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">cdn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Fastly의 Compute@Edge가 JavaScript를 지원한다.

- [JS on Wasm with Nick Fitzgerald (JS Party #183) |&gt; Changelog](https://changelog.com/jsparty/183 "JS on Wasm with Nick Fitzgerald (JS Party #183) |&amp;gt; Changelog")

----

## How to Eliminate Render-Blocking Resources: a Deep Dive
[sia.codes/posts/render-blocking-resources/](https://sia.codes/posts/render-blocking-resources/ "How to Eliminate Render-Blocking Resources: a Deep Dive")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

렌더링 블록킹 원인이 되는 자바스크립트와 CSS의 요소 소개.
렌더링이 블록되면 성능에 어떠한 영향을 주는지, WebPageTest를 사용한 확인 방법, 렌더링 블록킹 제거 방법 등을 다룬다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## Privacy Sandbox Timeline
[privacysandbox.com/timeline/](https://privacysandbox.com/timeline/ "Privacy Sandbox Timeline")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">document</span></p>

Privacy Sandbox의 로드맵과 타임라인.


----

## nicoespeon/abracadabra: Automated refactorings for VS Code (JS &amp; TS) ✨ It&#039;s magic ✨
[github.com/nicoespeon/abracadabra](https://github.com/nicoespeon/abracadabra "nicoespeon/abracadabra: Automated refactorings for VS Code (JS &amp; TS) ✨ It&#039;s magic ✨")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">VSCode</span> <span class="jser-tag">refacoring</span> <span class="jser-tag">plugin</span> <span class="jser-tag">JavaScript</span></p>

JavaScript와 TypeScript 리팩터링을 보조하는 VSCode 확장.
WebStorm와 같이 Quick Fix를 제공한다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Tak-Iwamoto/ptera: Ptera is DateTime library for Deno
[github.com/Tak-Iwamoto/ptera](https://github.com/Tak-Iwamoto/ptera "Tak-Iwamoto/ptera: Ptera is DateTime library for Deno")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Deno 용 날짜 조작 라이브러리.

- [Deno의 DateTime 라이브러리 Ptera를 릴리스했다](https://zenn.dev/tak_iwamoto/articles/8b32b27bd577b1 "Deno의 DateTime 라이브러리 Ptera를 릴리스했다")(일본어)

----

## ajitid/fzf-for-js: Do fuzzy matching using FZF algorithm in JavaScript
[github.com/ajitid/fzf-for-js](https://github.com/ajitid/fzf-for-js "ajitid/fzf-for-js: Do fuzzy matching using FZF algorithm in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">search</span></p>

커맨드라인 도구 용 유사어 검색(퍼지 검색) FZF 알고리즘을 JavaScript에 이식한 라이브러리.
퍼지란 검색하는 키워드와 완전히 일치하지 않아도 표기의 차이나 동의어 까지 포함해 유연하게 해석 및 검색하는 것.


----

## ES-Community/nsecure: Node.js security CLI / API that allow you to deeply analyze the dependency tree of a given package / directory
[github.com/ES-Community/nsecure](https://github.com/ES-Community/nsecure "ES-Community/nsecure: Node.js security CLI / API that allow you to deeply analyze the dependency tree of a given package / directory")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">Tools</span></p>

디렉터리나 특정 패키지의 npm 패키지 의존 정보를 분석하는 도구.
코드를 분석(파싱)하여 현재 사용하고 있는 npm 패키지의 메타데이터, 라이센스, 보안 정보 등의 데이터를 살펴 볼 수 있는 기능 제공.


----

## tangramxyz/tangram: Tangram is an all-in-one automated machine learning framework.
[github.com/tangramxyz/tangram](https://github.com/tangramxyz/tangram "tangramxyz/tangram: Tangram is an all-in-one automated machine learning framework.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MachineLearning</span> <span class="jser-tag">library</span> <span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ruby </span> <span class="jser-tag">python</span> <span class="jser-tag">golang</span></p>

기계 학습 프레임워크.
커맨드 라인으로 학습할 모델을 작성하고, 각종 언어의 FFI 라이브러리로 예측할 수 있다.
자바스크립트로는 와즘(Wasm) 빌드를 공개하고 있다.
또, 브라우저로 볼 수 있는 모델의 퍼포먼스 대시보드를 제공한다.


----

## udecode/plate: A plugin framework for building rich text editors with slate.
[github.com/udecode/plate](https://github.com/udecode/plate "udecode/plate: A plugin framework for building rich text editors with slate.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

slate 기반의 리치 텍스트 에디터 라이브러리.
플러그인으로 기능을 추가할 수 구조로 돼 있으며 다양한 플러그인이 준비돼 있다.


----

## actuallyakash/spacers: 🔳 when you need more \_\_space\_\_
[github.com/actuallyakash/spacers](https://github.com/actuallyakash/spacers "actuallyakash/spacers: 🔳 when you need more \_\_space\_\_")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

드래그엔드랍 으로 요소에 대한 padding이나 margin 등의 공간을 설정할 수 있는 라이브러리.


----

## davewasmer/devcert: Local HTTPS development made easy
[github.com/davewasmer/devcert](https://github.com/davewasmer/devcert "davewasmer/devcert: Local HTTPS development made easy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">SSL</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span></p>

로컬에서 개발용 HTTPS 서버 구축을 보조하는 라이브러리.
임의의 도메인에 대한 증명서 작성, 머신에 루트 증명서 설치 등 로컬에서의 HTTPS 서버 동작을 보조한다.


----
<h1 class="site-genre">도서</h1>

----

## 작은 웹 브라우저를 만들어보자(일본어)
[browserbook.shift-js.info/](https://browserbook.shift-js.info/ "작은 웹 브라우저를 만들어보자")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">book</span> <span class="jser-tag">Rust</span> <span class="jser-tag">security</span></p>

Rust로 웹 브라우저를 만들어보면서 브라우저의 렌더링 구조, 전체적인 흐름, 보안에 대해 학습할 수 있는 일본어 교재.


----
