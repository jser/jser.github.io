---
title: "2019-02-26: yarn v2 후보(berry), Fastify v2, TSLint의 향후 방향"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-02-26T02:02:23.716Z
category: JSer
tags:
- yarn
- node
- typescript
- eslint
- tslint

---

JSer.info #424 - [yarn](https://yarnpkg.com/) v2 저장소를 공개했습니다.

- [yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization](https://github.com/yarnpkg/berry)

아래 이슈에도 작성돼 있듯이 v1과 저장소를 분리한 이유는 이슈 분류를 좀 더 편하게 하기 위해서라고 합니다.

- [👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry](https://github.com/yarnpkg/berry/issues/1 "👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry")
- [Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn](https://github.com/yarnpkg/yarn/issues/6953#issuecomment-466589196 "Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn")

> The codename for these changes is Berry
> -- https://github.com/yarnpkg/yarn/issues/6953

"Berry"라는 이름은 v2 용으로 변경한 코드 네임입니다.


v2(berry)에는 [Yarn's Future - v2 and beyond](https://github.com/yarnpkg/yarn/issues/6953)에서 예고한 기능이 구현돼 있는 단계인 것 같습니다.

소스 코드는 타입스크립트로 작성돼 있으며 monorepo로 관리합니다.
yml 서브셋 격인 [syml](https://github.com/yarnpkg/berry/blob/master/packages/berry-parsers/sources/syml.ts)이라는 포맷을 만들어 lock 파일에 적용하고 있습니다. 또, 플러그인 구조가 추가돼 PnP나 npm(`package-lock.json`을 다루는 등) 등의 처리는 플러그인으로 대응합니다.
이어서 워크스페이스 개선 내용으로 [Constraints](https://github.com/yarnpkg/berry/blob/master/docs/workspaces-constraints.md) 라고 하는 Prolog(실제론 [tau-prolog](https://github.com/jariazavalverde/tau-prolog))를 사용한 제약을 다루는 [플러그인](https://github.com/yarnpkg/berry/tree/master/packages/plugin-constraints)을 추가했습니다. 워크스페이스 간 의존 규칙 등을 Prolog를 이용해 기술하여 보다 효율적으로 제약을 다룰 수 있도록 하는데 목적을 두고 있습니다.

흥미가 있는 분은 [Install](https://github.com/yarnpkg/berry#install)로 테스트해보거나 [Issue](https://github.com/yarnpkg/berry/issues)를 살펴보시면 좋을 것 같습니다.

----

[TypeScript의 2019 June 로드맵](https://github.com/Microsoft/TypeScript/issues/29288)에서 TSLint가 아니라 ESLint의 지원을 강화하겠다는 이야기가 했습니다. 이어서 [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)라는 프로젝트를 생성했고 [ESLint 팀과 협력](https://eslint.org/blog/2019/01/future-typescript-eslint)할 것이라고 발표했습니다.

이러한 배경 속에서 TSLint의 메인테이너가 TSLint의 향후 방향에 대한 글을 공개했습니다.

- [TSLint in 2019 – Palantir Blog – Medium](https://medium.com/palantir/tslint-in-2019-1a144c2317a9 "TSLint in 2019 – Palantir Blog – Medium")
- [Roadmap: TSLint -> ESLint · Issue #4534 · palantir/tslint](https://github.com/palantir/tslint/issues/4534 "Roadmap: TSLint -> ESLint · Issue #4534 · palantir/tslint")

TSLint는 2019년 중에 비권장(당장은 아닙니다) 되며 향후엔 ESLint로의 마이그레이션하는 과정을 갖는다고 합니다. [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)는 아직 개발중이기 때문에 TSLint와 연계되는 규칙이 없는 것도 있습니다. 때문에 TSLint 자체도 당분간은 유지보수를 계속 이어갑니다.

현재 [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)의 동작에 관해서는 다음 글을 참고해주세요.

- [@typescript-eslint 첫삽 - teppeis blog](https://teppeis.hatenablog.com/entry/2019/02/typescript-eslint)

----

<h1 class="site-genre">헤드라인</h1>

----

## Release Version 3.5.0 · knockout/knockout
[github.com/knockout/knockout/releases/tag/v3.5.0](https://github.com/knockout/knockout/releases/tag/v3.5.0 "Release Version 3.5.0 · knockout/knockout")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Knockout 3.5.0을 릴리스했습니다.
`foreach` 바인딩의 동작 변경, 성능 개선, `ko.when`이 Promise를 반환하도록 수정했습니다.


----

## Release: npm@6.9.0-next.0 - 📣 announcements - npm forum
[npm.community/t/release-npm-6-9-0-next-0/5553](https://npm.community/t/release-npm-6-9-0-next-0/5553 "Release: npm@6.9.0-next.0 - 📣 announcements - npm forum")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.9.0-next.0을 릴리스 했습니다.
페키지에 별명을 붙일 수 있는 package alias 기능과 `--before` 옵션을 지원합니다.

- [install: add support for package aliases by zkat · Pull Request #3 · npm/cli](https://github.com/npm/cli/pull/3 "install: add support for package aliases by zkat · Pull Request #3 · npm/cli")

----

## The npm Blog — Managing JavaScript in the Enterprise
[blog.npmjs.org/post/182958759735/managing-javascript-in-the-enterprise](https://blog.npmjs.org/post/182958759735/managing-javascript-in-the-enterprise "The npm Blog — Managing JavaScript in the Enterprise")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">news</span></p>

npm Enterprise를 정식으로 릴리스했습니다.
SSO 인증을 대응했고 private registry를 지원합니다.

- [npm | Enterprise](https://www.npmjs.com/products/enterprise "npm | Enterprise")

----

## dsherret/conditional-type-checks: Types for testing TypeScript types.
[github.com/dsherret/conditional-type-checks](https://github.com/dsherret/conditional-type-checks "dsherret/conditional-type-checks: Types for testing TypeScript types.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

Conditional Type를 사용해 TypeScript 타입을 Assertion 할 수 있는 라이브러리입니다.


----

## Fastify v2.0.0 is here – Fastify – Medium
[medium.com/@fastifyjs/fastify-v2-0-0-is-here-8275d613fba4](https://medium.com/@fastifyjs/fastify-v2-0-0-is-here-8275d613fba4 "Fastify v2.0.0 is here – Fastify – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">server</span></p>

Node.js 프레임워크 Fastify 2.0.0를 릴리스했습니다.
`onError`, `preParsing`, `preSerialization`, `preValidation` Hook API를 추가했습니다.
plugin 불러오기 타임아웃을 설정할 수 있고 일관성 없던 시그니처를 수정했습니다.

- [Release v2.0.0 · fastify/fastify](https://github.com/fastify/fastify/releases/tag/v2.0.0 "Release v2.0.0 · fastify/fastify")

----

## yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization
[github.com/yarnpkg/berry](https://github.com/yarnpkg/berry "yarnpkg/berry: 📦🐈 A modern, fast, reliable, package manager; part of the Yarn organization")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">news</span></p>

yarn v2이 될 소 스코드 저장소를 공개했습니다.
issue를 좀 더 편하게 분류하고 다루기 위해서 v1 저장소와 분리 했습니다.
현재 로드맵에서 예정한 기능은 어느정도 개발한 상태이지만 일부 기능과 문서가 아직 부족한 상황입니다.

- [Yarn's Future - v2 and beyond · Issue #6953 · yarnpkg/yarn](https://github.com/yarnpkg/yarn/issues/6953#issuecomment-466589196 "Yarn&#x27;s Future - v2 and beyond · Issue #6953 · yarnpkg/yarn")
- [👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry](https://github.com/yarnpkg/berry/issues/1 "👑 Say hello to Yarn v2 · Issue #1 · yarnpkg/berry")

----
<h1 class="site-genre">아티클</h1>

----

## AddyOsmani.com - JavaScript Loading Priorities in Chrome
[addyosmani.com/blog/script-priorities/](https://addyosmani.com/blog/script-priorities/ "AddyOsmani.com - JavaScript Loading Priorities in Chrome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

link rel=preload와 script 요소에 defer/async 속성을 조합할 때의 불러오기와 실행의 Priority에 관해 정리한 글입니다.


----

## How @supports Works | CSS-Tricks
[css-tricks.com/how-supports-works/](https://css-tricks.com/how-supports-works/ "How @supports Works | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS의 `@supports` 사용법과 유스케이스에 관해 작성한 글입니다.
또, JavaScript에서 CSS Supports를 사용한 Feature Detect 기법도 소개합니다.


----

## Intelligent Tracking Prevention 2.1 | WebKit
[webkit.org/blog/8613/intelligent-tracking-prevention-2-1/](https://webkit.org/blog/8613/intelligent-tracking-prevention-2-1/ "Intelligent Tracking Prevention 2.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Safari 12.1에 도입되는 ITP(Intelligent Tracking Prevention) 2.1을 소개합니다. Partitioned Cookies와 DNT(Do Not Track)의 지원을 종료하며 document.cookie로 생성한 쿠기는 만료 기간을 7일로 제한합니다.


----

## TSLint in 2019 – Palantir Blog – Medium
[medium.com/palantir/tslint-in-2019-1a144c2317a9](https://medium.com/palantir/tslint-in-2019-1a144c2317a9 "TSLint in 2019 – Palantir Blog – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span> <span class="jser-tag">Tools</span></p>

TSLint의 향후 방침에 대해 이야기합니다.
올해 내 TSLint는 비권장되며 TSLint에서 ESLint로 마이그레이션하는 과정을 갖습니다.


----
<h1 class="site-genre">서비스, 사이트, 문서</h1>

----

## React – A JavaScript library for building user interfaces(일본어)
[ja.reactjs.org/](https://ja.reactjs.org/ "React – A JavaScript library for building user interfaces")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">번역</span></p>

React 사이트의 일본어 버전입니다.

- [Is React Translated Yet? ¡Sí! Sim! はい！ – React Blog](https://reactjs.org/blog/2019/02/23/is-react-translated-yet.html "Is React Translated Yet? ¡Sí! Sim! はい！ – React Blog")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## patr0nus/DeskGap: A cross-platform desktop app framework based on Node.js and the system webview
[github.com/patr0nus/DeskGap/](https://github.com/patr0nus/DeskGap/ "patr0nus/DeskGap: A cross-platform desktop app framework based on Node.js and the system webview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">mac</span> <span class="jser-tag">windows</span> <span class="jser-tag">Electron</span></p>

OS의 웹뷰 구조를 이용해 개발한 Electron과 비슷한 데스크탑 애플리케이션 개발 프레임워크입니다.
Chromium을 bundle 하고 있진 않지만 Node.js을 bundle 하고 있습니다.
제한적으로 Electron와 비슷한 몇 가지 API와 Node.js의 기능을 사용할 수 있습니다.


----

## klaussinani/qoa: 💬 Minimal interactive command-line prompts
[github.com/klaussinani/qoa](https://github.com/klaussinani/qoa "klaussinani/qoa: 💬 Minimal interactive command-line prompts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">console</span> <span class="jser-tag">UI</span></p>

터미널 환경을 위한 대화형 인터페이스를 만들 수 있는 Node.js 라이브러리입니다.
Confirm, Quiz, Secure Prompt 등을 지원합니다.


----

## jariazavalverde/tau-prolog: An open source Prolog interpreter in JavaScript
[github.com/jariazavalverde/tau-prolog](https://github.com/jariazavalverde/tau-prolog "jariazavalverde/tau-prolog: An open source Prolog interpreter in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">program</span> <span class="jser-tag">library</span></p>

Prolog 인터프리터 JavaScript 구현체입니다.


----

## fagbokforlaget/simple-fs: Handles files on indexeddb like you would do in node.js (promise)
[github.com/fagbokforlaget/simple-fs](https://github.com/fagbokforlaget/simple-fs "fagbokforlaget/simple-fs: Handles files on indexeddb like you would do in node.js (promise)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

IndexedDB를 사용한 파일 시스템 스러운 API를 제공하는 브라우저 용 라이브러리입니다.


----

## namics/webpack-config-plugins: Provide best practices for webpack loader configurations
[github.com/namics/webpack-config-plugins](https://github.com/namics/webpack-config-plugins "namics/webpack-config-plugins: Provide best practices for webpack loader configurations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">設定</span></p>

webpack의 loader 설정을 단순하게 정리하여 제공하는 플러그인 입니다.
Babel, TypeScript, Sass, Font, Image 등의 빌드를 지원하는 플러그인이 준비돼 있습니다.


----
