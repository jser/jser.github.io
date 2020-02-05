---
title: "2020-02-05: npm unpublish policy, yarn v2(berry) RC 릴리스"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2020-02-05T03:42:06.633Z
category: JSer
tags:
- npm
- yarn

---

JSer.info #473 - npm에는 패키지를 공개한 사람이 해당 패키지를 철회하는 규칙에 대해 정의한 [npm Unpublish Policy](https://www.npmjs.com/policies/unpublish)가 있습니다.
이번에 이 [npm Unpublish Policy](https://www.npmjs.com/policies/unpublish)의 규칙이 갱신됐습니다.

- [The npm Blog — Changes to npm Unpublish Policy - January 2020](https://blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020)

본래 이 Unpublish Policy는 [left-pad가 unpublish 된 사건](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)을 계기로 정의 됐습니다. 이미 사용되고 있는 npm 패키지가 unpublish 되면 npm의 에코시스템이 깨지게 됩니다. 따라서 `npm unpublish`에 어떠한 제한을 걸기 위해 도입된 규칙입니다.

- [The npm Blog — changes to npm’s unpublish policy](https://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy)

이번에 `npm publish` 한 후 `npm unpublish` 가능한 시간 제한이 완화 됐으며 몇 가지 조건을 충족할 경우 시간 제한 없이 unpublish 가능하도록 변경됐습니다.

- publish 한 후 72 시간 이내(본래는 24시간 이내)
- 지난 주 다운로드 수가 300미만, 다른 공개 모듈에서 의존하고 있지 않음, 단독 소유(소유자/메인테이너)일 경우

이 변경 전에는 publish 한 후 24시간 이상 지나면 unpublish 하기 위해서 직접 지원 센터에 연락할 필요가 있었습니다. 
아무래도 불편하기 때문에 다른 모듈에서 의존하지 않는 등의 모듈은 `npm unpublish` 가능하도록 규칙을 변경한 것 같습니다.

----

Yarn의 메이저 업데이트 인 v2([yarnpkg/berry](https://github.com/yarnpkg/berry))의 RC 버전 진행과 함께 yarn 2의 변경 사항에 대해서 메인테이너인 [arcanis](https://github.com/arcanis)가 정리해 공개했습니다.

- [Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻](https://dev.to/arcanis/introducing-yarn-2-4eh1)

이 글에는 현재 Stable인 Yarn v1을 legacy로, 향후 v2(berry)를 Stable로 전환 할 계획 등이 소개돼 있습니다.
웹사이트도 이에 맞춰 리다렉트(next.yarnpkg.com) 되며 이 영향으로 [번역된 페이지에 접근시 404](https://github.com/yarnpkg/website/issues/1042)가 발생하기도 합니다.

- Yarn v2: https://next.yarnpkg.com
- Yarn v1: https://classic.yarnpkg.com

또한 기본적으로 캐시를 레파지토리에 배치하도록 변경, CLI의 출력 방식 변경, v1의 구조 차이 등 Yarn 2의 변경 사항에 대해서도 소개돼 있습니다.
새로운 기능으로는 `npx`와 같은 `yarn dlx` 추가, `patch:`/`portal:` 대응, Workspace 명령어 개선, Workspace를 검사하는 Constraints가 추가 됐습니다.
이 외에도 패키지 별 빌드 여부를 설정할 수 있으며 `yarn run`에서 OS간 쉘의 차이 정규화, Lock 파일의 포멧 변경, 의존 패키지를 수정할 수 없도록 Read-Only로 변경했습니다.

현재 v2와 관련된 문서나 이전 가이드도 공개돼 있기 때문에 관심 있는 분은 함께 살펴보시기 바랍니다.,

- [Migration | Yarn - Package Manager](https://next.yarnpkg.com/advanced/migration "Migration | Yarn - Package Manager")
- [Plug'n'Play | Yarn - Package Manager](https://next.yarnpkg.com/features/pnp "Plug&#x27;n&#x27;Play | Yarn - Package Manager")
- [Zero-Installs | Yarn - Package Manager](https://next.yarnpkg.com/features/zero-installs "Zero-Installs | Yarn - Package Manager")


----

<h1 class="site-genre">헤드라인</h1>

----

## Release v2.1.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v2.1.0](https://github.com/puppeteer/puppeteer/releases/tag/v2.1.0 "Release v2.1.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v2.1.0이 릴리스 됐습니다.
Chromium 80로 갱신됏으며 Firefox를 지원합니다.


----

## New PWABuilder release! - PWABuilder - Medium
[medium.com/pwabuilder/new-pwabuilder-release-b2932f4722a5](https://medium.com/pwabuilder/new-pwabuilder-release-b2932f4722a5 "New PWABuilder release! - PWABuilder - Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

PWABuilder가 갱신됐습니다.
Trusted Web Activity를 사용한 Android 용 패키징에 대응했으며 패키징 관련 가이드가 개편됐습니다.

- [PWABuilder](https://www.pwabuilder.com/ "PWABuilder")
- [GoogleChromeLabs/llama-pack: Llama Pack 🦙 is a Command Line Interface (CLI) that helps developers to create a Project for an Android application that launches an existing Progressive Web App (PWAs) using a Trusted Web Activity.](https://github.com/GoogleChromeLabs/llama-pack "GoogleChromeLabs/llama-pack: Llama Pack 🦙 is a Command Line Interface (CLI) that helps developers to create a Project for an Android application that launches an existing Progressive Web App (PWAs) using a Trusted Web Activity.")

----

## The npm Blog — Changes to npm Unpublish Policy - January 2020
[blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020](https://blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020 "The npm Blog — Changes to npm Unpublish Policy - January 2020")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">news</span></p>

npm의 unpublish policy가 변경됐습니다.
지금까지 24시간 이내에 가능했던 unpublish가 72시간 이내 할 수 있도록 변경됐습니다.
또, 다운로드 수가 300미만이면서 다른 공개 패키지에서 의존하고 있지 않고 단독 소유(소유자 / 메인테이너)일 경우에도 unpublish가 가능합니다.

- [policies/unpublish.md at master · npm/policies](https://github.com/npm/policies/blob/master/unpublish.md "policies/unpublish.md at master · npm/policies")

----

## Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻
[dev.to/arcanis/introducing-yarn-2-4eh1](https://dev.to/arcanis/introducing-yarn-2-4eh1 "Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

Yarn 2에 관한 글이 공개됐습니다.
Yarn v1은 legacy로 전환되며 향우 Stable은 v2(berry)로 바뀔 계획입니다.
기본적으로 캐시를 레파지토리에 배치하도록 변경됐으며 CLI의 출력 방식이 바뀌었습니다. 그리고 `npx`와 같은 `yarn dlx`가 추가됐고 `patch:`/`portal:`를 대응합니다. 이어 Workspace 명령어어 개선이 이뤄졌고 Workspace를 검사하는 Constraints가 추가됐습니다.
또, 패키지 별 빌드 여부를 설정할 수 있으며 `yarn run`에서 OS간 쉘의 차이 정규화, Lock 파일의 포멧 변경, 의존 패키지를 수정할 수 없도록 Read-Only로 변경했습니다. 

- [Migration | Yarn - Package Manager](https://next.yarnpkg.com/advanced/migration "Migration | Yarn - Package Manager")
- [Plug'n'Play | Yarn - Package Manager](https://next.yarnpkg.com/features/pnp "Plug&#x27;n&#x27;Play | Yarn - Package Manager")
- [Zero-Installs | Yarn - Package Manager](https://next.yarnpkg.com/features/zero-installs "Zero-Installs | Yarn - Package Manager")

----

## Meteor 1.9 (Node.js 12) and new Roadmaps - Meteor Blog
[blog.meteor.com/meteor-1-9-node-js-12-and-new-roadmaps-cb993277d444](https://blog.meteor.com/meteor-1-9-node-js-12-and-new-roadmaps-cb993277d444 "Meteor 1.9 (Node.js 12) and new Roadmaps - Meteor Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Meteor 1.9가 릴리스 됐습니다.
Node.js 12를 지원하며 Galaxy(Metor 호스팅 환경)의 로드맵이 공개됐습니다.


----

## Release Releaaaaaaaaaaaaaaaaaaase · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.3.0](https://github.com/preactjs/preact/releases/tag/10.3.0 "Release Releaaaaaaaaaaaaaaaaaaase · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.3.0이 릴리스 됐습니다.
Built-In 요소를 상속하는 Custom Element에 대응했으며 버그가 수정됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## What's New In DevTools (Chrome 81)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/01/devtools](https://developers.google.com/web/updates/2020/01/devtools "What's New In DevTools (Chrome 81)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 81 개발자 도구의 변경 사항이 정리돼 있습니다.
차단된 쿠키를 특정 색으로 나타내며 네트워크 패널에 `Copy as Node.js fetch` 추가됐고 Source Map의 에러가 콘솔에 표시됩니다.


----

## JavaScript Libraries Are Almost Never Updated Once Installed
[blog.cloudflare.com/javascript-libraries-are-almost-never-updated/](https://blog.cloudflare.com/javascript-libraries-are-almost-never-updated/ "JavaScript Libraries Are Almost Never Updated Once Installed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

CDN 경유로 사이트에 내장돼 있는 자바스크립트 라이브러리는 한번 설치된 뒤 갱신되는 경우가 거의 없다는 사실을 데이터를 기반으로 설명합니다. 


----
<h1 class="site-genre">슬라이드, 문서</h1>

----

## 곧 다가올 Vue.js 3 - Speaker Deck(일본어)
[speakerdeck.com/kazupon/mamonakuyatutekuru-vue-dot-js-3](https://speakerdeck.com/kazupon/mamonakuyatutekuru-vue-dot-js-3 "곧 다가올 Vue.js 3 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">slide</span></p>

Vue.js 3를 소개하는 슬라이드 자료입니다.
Composition API, 라이프 사이클 훅, DI(`provide`,`inject`), React스러운 Portal과 Suspense, 추가된 CSS 독자 의사 클래스에 대해서 소개합니다.
또, 필터 삭제 건과 글로벌 상태 정리에 대해서도 이야기합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Adapt · React for your infrastructure.
[adaptjs.org/](https://adaptjs.org/ "Adapt · React for your infrastructure.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Infrastructure</span> <span class="jser-tag">Tools</span></p>

React를 사용해 pulumi 등 처럼 인프라를 코드로 관리하는 도구입니다.
Hooks API, 컴포넌트, JSX로 설정을 작성할 수 있습니다.
환경이나 프로바이더 등의 분리는 Style 이라고 하는 타입을 이용하여 할 수 있습니다. 


----

## cutenode/mingine: A module to get the minimum usable engine(s)
[github.com/cutenode/mingine](https://github.com/cutenode/mingine "cutenode/mingine: A module to get the minimum usable engine(s)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag"> node</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

의존하고 있는 npm 패키지의 `engines` 필드에서 `engines` 별 minimum한 버전을 산출하는 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## Manning | Deep Learning with JavaScript
[www.manning.com/books/deep-learning-with-javascript](https://www.manning.com/books/deep-learning-with-javascript "Manning | Deep Learning with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MachineLearning</span> <span class="jser-tag">book</span></p>

TensorFlow.js를 사용한 Deep Learning를 주제로 한 도서입니다.


----

## 프로그래밍 TypeScript ― 스케일하는 JavaScript 애플리케이션 개발 | Boris Cherny, 이마무라 켄시, 하라 타카후미 | 책 | 통신판매 | Amazon(일본어)
[www.amazon.co.jp/dp/4873119049/](https://www.amazon.co.jp/dp/4873119049/ "프로그래밍 TypeScript ― 스케일하는 JavaScript 애플리케이션 개발 | Boris Cherny, 이마무라 켄시, 하라 타카후미 | 책 | 통신판매 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2020년 3월 16일에 출간 예정인 Programming TypeScript 일본어 역서입니다.


----
