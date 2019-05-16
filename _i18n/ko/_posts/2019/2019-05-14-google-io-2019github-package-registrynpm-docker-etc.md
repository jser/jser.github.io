---
title: "2019-05-14: Google I/O 2019、GitHub Package Registry(npm, Docker, etc)"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-05-14T01:14:26.660Z
category: JSer
tags:
- Google
- Chrome
- GitHub
- npm 

---

JSer.info #435 - [Google I/O 2019](https://events.google.com/io/)의 이벤트 영상 또는 관련한 정보가 공개되고 있습니다.

Google I/O의 웹과 관련한 세션 영상은 아래 유튜브를 통해 공개됐습니다.

- [Web at Google I/O 2019 - YouTube](https://www.youtube.com/watch?v=rUUazNIZW7I&list=PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i)

Google 검색 크롤링에 사용되고 있는 렌더링 엔진이 Chrome 41에서 최신 버전(현재 74)의 Chromium 기반으로 갱신됩니다.

- [Official Google Webmaster Central Blog: The new evergreen Googlebot](https://webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html)

lighthouse 5.0.0이 릴리스됐습니다. Wordpress 등 특정 스택에 대한 정보를 출력하는 Stack Packs가 추가됐고 Performance budgets을 대응했으며 Lighthouse plugins 구조가 추가됐습니다. 이어 Performance budgets 정의 파일을 생성하는 [Performance Budget Calculator](https://perf-budget-calculator.firebaseapp.com/) 도구도 공개됐습니다.

- [Release v5.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0)

또, 구글이 운영하고 있는 [web.dev](https://web.dev/)에 [Blog](https://web.dev/blog)나 [React](https://web.dev/react) 애플리케이션 최적화에 관한 튜토리얼 등이 추가됐습니다.

----

GitHub가 [GitHub Package Registry](https://github.com/features/package-registry)라는 패키지 등록 서비스의 베타 버전을 공개했습니다.

- [Introducing GitHub Package Registry - The GitHub Blog](https://github.blog/2019-05-10-introducing-github-package-registry/)
- [GitHub Package Registry: Your packages, at home with their code](https://github.com/features/package-registry)

GitHub Package Registry는 npm이나 RubyGems, Docker 등에 대응한 public / private registry 서비스입니다.
현재는 베타이며 [GitHub Package Registry의 signup](https://github.com/features/package-registry/signup)를 통해 가입하여 사용해 볼 수 있습니다(pre-release).
자세한 내용은 아래 문서를 참고하시길 바랍니다. npm 패키지를 GitHub의 User 또는 Organization 명을 붙여 scoped module로 공개할 수 있는 것 같습니다.

- [About GitHub Package Registry - GitHub Help](https://help.github.com/en/articles/about-github-package-registry)
- [Configuring NPM for use with GitHub Package Registry - GitHub Help](https://help.github.com/en/articles/configuring-npm-for-use-with-github-package-registry)

GitHub Package Registry로 배포하는 데모 영상도 있으니 관심 있는 분은 함께 살펴보면 될 거 같습니다.

- Video: [GitHub: "Introducing GitHub Package Registry"](https://www.pscp.tv/w/1jMKgvMEggwxL)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release v5.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0 "Release v5.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 5.0.0이 릴리스됐습니다.
Wordpress 등 특정 스택에 대한 정보를 출력하는 Stack Packs가 추가됐고, Performance budgets을 대응했으며 Lighthouse plugins 구조가 추가됐습니다.

- [GoogleChrome/lighthouse-stack-packs: Lighthouse Stack Packs](https://github.com/GoogleChrome/lighthouse-stack-packs "GoogleChrome/lighthouse-stack-packs: Lighthouse Stack Packs")
- [Performance Budgets (Keep Request Counts Low And File Sizes Small)  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/lighthouse/audits/budgets "Performance Budgets (Keep Request Counts Low And File Sizes Small)  |  Tools for Web Developers  |  Google Developers")
- [lighthouse/plugins.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/plugins.md#plugin-config "lighthouse/plugins.md at master · GoogleChrome/lighthouse")

----

## Official Google Webmaster Central Blog: The new evergreen Googlebot
[webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html](https://webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html "Official Google Webmaster Central Blog: The new evergreen Googlebot")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">search</span> <span class="jser-tag">news</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span></p>

Google 검색 bot이 최신 버전의 Chromium 렌더링 엔진 기반으로 갱신됐습니다.

- [Fix Search-related JavaScript problems  |  Search  |  Google Developers](https://developers.google.com/search/docs/guides/fix-search-javascript "Fix Search-related JavaScript problems  |  Search  |  Google Developers")

----

## Node v12.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.2.0/](https://nodejs.org/en/blog/release/v12.2.0/ "Node v12.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.2.0이 릴리스됐습니다.
`--trace-tls` 옵션이 추가됐으며 `Module.createRequireFromPath()`를 비권장화 했고 `URL` 객체나 URL 문자열 등으로 require 함수를 만들 수 있는 `module.createRequire`가 추가됐습니다.


----

## comlink/CHANGELOG.md at master · GoogleChromeLabs/comlink
[github.com/GoogleChromeLabs/comlink/blob/master/CHANGELOG.md#v3---v4](https://github.com/GoogleChromeLabs/comlink/blob/master/CHANGELOG.md#v3---v4 "comlink/CHANGELOG.md at master · GoogleChromeLabs/comlink")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ES Proxy를 사용한 Worker 라이브러리 Comlink 4.0.0이 릴리스됐습니다.
Node.js의 `worker_thread`를 지원하며 일부 API의 이름이 변경됐고 성능이 개선됐습니다.

- [Surma on Twitter: &quot;I sneakily released Comlink v4 just before #io19! ➡️Smaller than v3 (~1.1kb) 🗜 ➡️10x faster on low-end devices (we needed that for https://t.co/TQBh7GNv2g!) 🏎💨 ➡️Better API naming 💫 ➡️Better folder structure 🙏 ➡️Support for workers in Node 11+ 🤯 https://t.co/v4PNytvkfq… https://t.co/mksFf7uxPu&quot;](https://twitter.com/DasSurma/status/1127266398185484288 "Surma on Twitter: &amp;quot;I sneakily released Comlink v4 just before #io19! ➡️Smaller than v3 (~1.1kb) 🗜 ➡️10x faster on low-end devices (we needed that for https://t.co/TQBh7GNv2g!) 🏎💨 ➡️Better API naming 💫 ➡️Better folder structure 🙏 ➡️Support for workers in Node 11+ 🤯 https://t.co/v4PNytvkfq… https://t.co/mksFf7uxPu&amp;quot;")

----

## Release v1.16.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.16.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.16.0 "Release v1.16.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer 1.16.0이 릴리스됐습니다.
`browser.isConnected()`, `target.worker()`를 지원하며 `accessibility.snapshot()`에 `root` 옵션이 추가됐습니다.


----

## Introducing GitHub Package Registry - The GitHub Blog
[github.blog/2019-05-10-introducing-github-package-registry/](https://github.blog/2019-05-10-introducing-github-package-registry/ "Introducing GitHub Package Registry - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">github</span> <span class="jser-tag">news</span> <span class="jser-tag">npm</span></p>

GitHub의 패키지 등록 서비스 베타 버전이 공개됐습니다.
npm, gem, docker 등을 지원하며 GitHub의 Team 퍼미션에 따라 관리할 수 있는 private registry 입니다.
GitHub Package Registry에 등록한 모듈은 GitHub의 Release나 검색에도 표현됩니다.

- [GitHub Package Registry: Your packages, at home with their code](https://github.com/features/package-registry "GitHub Package Registry: Your packages, at home with their code")

----

## AWS Lambda adds support for Node.js v10
[aws.amazon.com/jp/about-aws/whats-new/2019/05/aws\_lambda\_adds\_support\_for\_node\_js\_v10/](https://aws.amazon.com/jp/about-aws/whats-new/2019/05/aws_lambda_adds_support_for_node_js_v10/ "AWS Lambda adds support for Node.js v10")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">Lambda</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

AWS Lambda가 Node.js 10을 지원합니다.


----
<h1 class="site-genre">아티클</h1>

----

## SameSite cookies explained  |  web.dev
[web.dev/samesite-cookies-explained/](https://web.dev/samesite-cookies-explained/ "SameSite cookies explained  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

`SameSite` Cookie에 대한 설명글입니다. `SameSite`의 설정 값인 `Strict`, `Lax`, `None`의 각 동작 방식을 소개합니다.
Chrome 76에서 `SameSite`를 미지정한 경우 `SameSite=Lax`를 기본으로하는 시범적 플래그가 추가돼 있습니다.

- [HTTP 쿠키를 모다 안전하게 하는 SameSite 속성에 관하여 (Same-site Cookies) | 라보라디언](https://laboradian.com/same-site-cookies/ "HTTP 쿠키를 모다 안전하게 하는 SameSite 속성에 관하여 (Same-site Cookies) | 라보라디언")(일본어)

----

## React  |  web.dev
[web.dev/react](https://web.dev/react "React  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

web.dev의 React 웹 애플리케이션 최적화에 관한 튜토리얼입니다.
Bundle size, 무한 리스트, Service Worker, 프리 렌더링, 접근성 등에 관해 작성돼 있습니다.


----

## A Guide to Node.js Logging - Twilio
[www.twilio.com/blog/guide-node-js-logging](https://www.twilio.com/blog/guide-node-js-logging "A Guide to Node.js Logging - Twilio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 환경에서 로그를 출력하는 방법에 대한 글입니다.
Console API, pino를 사용한 로그 출력, 라이브러리의 로그, chalk 등으로 꾸며진 로그를 평범하게 출력하는 방법 등에 대해 작성돼 있습니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Web at Google I/O 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i](https://www.youtube.com/playlist?list=PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i "Web at Google I/O 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Google I/O 2019 웹 세션 영상이 정리돼 있습니다.


----

## ng-conf 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLOETEcp3DkCpimylVKTDe968yNmNIajlR](https://www.youtube.com/playlist?list=PLOETEcp3DkCpimylVKTDe968yNmNIajlR "ng-conf 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Angular 컨퍼런스 ng-confg 2019의 영상이 정리돼 있습니다.

- [Angular - All Talks from ng-conf 2019](https://nitayneeman.com/posts/all-talks-from-ng-conf-2019/ "Angular - All Talks from ng-conf 2019")
- [ng-conf 2019 Note](https://www.notion.so/ng-conf-2019-Note-10b9443262a54fb9bd8586cc25a449c7 "ng-conf 2019 Note")

----

## Node.js v12의 신경 쓰이는 변경 사항 / #kng6 - Speaker Deck(일본어)
[speakerdeck.com/masashi/number-kng6](https://speakerdeck.com/masashi/number-kng6 "Node.js v12의 신경 쓰이는 변경 사항 / #kng6 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">slide</span></p>

Node.js 12의 변경 사항이 정리돼 있습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## wapm | WebAssembly Package Manager
[wapm.io/](https://wapm.io/ "wapm | WebAssembly Package Manager")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span></p>

WebAssembly의 패키지 매니저 또는 저장소입니다.


----

## microsoft/frontend-bootcamp: Frontend Workshop from HTML/CSS/JS to TypeScript/React/Redux
[github.com/Microsoft/frontend-bootcamp](https://github.com/Microsoft/frontend-bootcamp "microsoft/frontend-bootcamp: Frontend Workshop from HTML/CSS/JS to TypeScript/React/Redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Microsoft의 프런트엔드 워크샵 교재입니다.
HTML, CSS, JavaScript, TypeScript를 다루는 2일 분량의 컨텐츠입니다.


----

## Data | Third-Party Web
[www.thirdpartyweb.today/](https://www.thirdpartyweb.today/ "Data | Third-Party Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

HTTP Archive의 크롤링 데이터를 기반으로 서드 파티 스크립트의 영향도를 시각화한 사이트입니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## manzinello/mailgo: 💌 mailgo, a different mailto (WIP)
[github.com/manzinello/mailgo](https://github.com/manzinello/mailgo "manzinello/mailgo: 💌 mailgo, a different mailto (WIP)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">mail</span></p>

`mailto:` 링크를 클릭했을 때 메뉴를 출력하는 라이브러리입니다.
메뉴를 이용해 Gmail, Outlook으로 열거나 주소를 복사할 수 있습니다.


----

## victorvoid/dinoql: A customizable GraphQL style query language for interacting with JavaScript objects.
[github.com/victorvoid/dinoql](https://github.com/victorvoid/dinoql "victorvoid/dinoql: A customizable GraphQL style query language for interacting with JavaScript objects.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

GraphQL 구문으로 객체로부터 데이터를 가져올 수 있는 쿼리 라이브러리입니다.
Alias, Cache, Fragments 등을 지원합니다.


----

## msgpack/msgpack-javascript: MessagePack for JavaScript/ECMA-262
[github.com/msgpack/msgpack-javascript](https://github.com/msgpack/msgpack-javascript "msgpack/msgpack-javascript: MessagePack for JavaScript/ECMA-262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

MessagePack의 JavaScript 구현체입니다.
ブラウザ와 Node.js 모두 동작하며 Async Iterator를 사용해 스트림 처리를 할 수 있습니다.

- [TypeScript로 MessagePack encoder/decoder를 구현했다 - Islands in the byte stream](https://gfx.hatenablog.com/entry/2019/05/07/102341 "TypeScript로 MessagePack encoder/decoder를 구현했다 - Islands in the byte stream")(일본어)

----
