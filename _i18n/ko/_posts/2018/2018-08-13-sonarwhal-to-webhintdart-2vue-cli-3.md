---
title: "2018-08-13 JS: sonarwhal to webhint, Dart 2, Vue CLI 3"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2018-08-13T12:22:03.816Z
category: JSer
tags:
- webhint
- dart
- vue

---

JSer.info.396 - sonar는 ESLint와 같이 플러그인으로 확장할 수 있는 웹사이트 검증 도구였습니다.

- [sonar - JS Foundation Welcomes Newest Project - JS Foundation](https://js.foundation/announcements/2017/06/22/sonar-js-foundation-welcomes-newest-project)

[이름이 충돌하는 툴](https://code.fb.com/android/open-sourcing-sonar-a-new-extensible-debugging-tool-2/)과 [서비스](https://www.sonarsource.com/)가 있어 webhint로 이름을 변경하기로 결정했습니다. (지금도 웹 사이트에는 이름 변경이 진행 중이기 때문에 기존 이름이 남아 있습니다)

- [webhint: a hinting engine for the web – webhint – Medium](https://medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9)
- [webhintio/hint: 💡 A hinting engine for the web](https://github.com/webhintio/hint)

이름을 변경함과 동시에 webhint 3.0이 릴리스 됐으며 성능 개선 및 npm create hintrc로 설정 파일을 작성할 수 있도록 기능이 추가됐습니다.

----

Dart 2의 안정 버전이 공개됐습니다.

- [Dart 2 | Dart](https://www.dartlang.org/dart-2)
- [Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium](https://medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7)

이번 릴리스에 맞춰 [AngularDart 5.0](https://webdev.dartlang.org/angular)도 릴리스 됐으며 Dart기반의 [Flutter](https://flutter.io/)는 이미 Dart 2의 프리 릴리즈 버전을 사용하고 있어 큰 변경 사항은 없을 거 같습니다.

----

[Vue CLI](https://cli.vuejs.org/) 3.0이 릴리스 됐습니다.

- [Vue CLI 3.0 is here! – The Vue Point – Medium](https://medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb)

Vue CLI 3.0은 지금까지 스캐폴딩 도구였던 CLI를 재작성한 버전으로 다양한 기능을 갖고 있습니다. webpack을 사용한 빌드 및 [Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/) 대응, 플러그인 시스템, GUI로 조작할 수 있는 대시 보드, 개발 서버, ES2015 대응 브라우저 용으로 빌드 최적화하는 Modern Mode등의 기능을 지원합니다.

또 기본적으로 webpack이 설정돼 있지만 eject 없이 webpack 관련 설정을 변경할 수 있도록 [webpack-chain](https://github.com/mozilla-neutrino/webpack-chain) 시스템이 도입됐습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## webhint: a hinting engine for the web – webhint – Medium
[medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9](https://medium.com/webhint/webhint-a-hinting-engine-for-the-web-ef0d3fa32ea9 "webhint: a hinting engine for the web – webhint – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

webhint(sonarwhal)가 릴리스 됐습니다. 
sonarwhal에서 webhint로 이름이 변경됐으며 실행 시간이 개선됐고 `npm create hintrc`로 설정 파일을 작성할 수 있게 됐습니다.

----

## V8 JavaScript Engine: V8 release v6.9
[v8project.blogspot.com/2018/08/v8-release-69.html](https://v8project.blogspot.com/2018/08/v8-release-69.html "V8 JavaScript Engine: V8 release v6.9")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v6.9가 릴리스 됐습니다. 메모리 사용량을 최적화 했으며 WebAssembly 컴파일러 실행 속도와 DataView의 성능이 개선됐습니다.

----

## Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium
[medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7](https://medium.com/dartlang/dart-2-stable-and-the-dart-web-platform-3775d5f8eac7 "Announcing Dart 2 Stable and the Dart Web Platform – Dart – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">dart</span> <span class="jser-tag">ReleaseNote</span></p>

Dart 2가 릴리스 됐습니다.

- [Dart 2 | Dart](https://www.dartlang.org/dart-2 "Dart 2 | Dart")

----

## Release v3.0.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v3.0.0](https://github.com/lerna/lerna/releases/tag/v3.0.0 "Release v3.0.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

monorepo 관리 도구인 lerna 3.0.0이 릴리스 됐습니다.
`lerna publish`와 `lerna version`으로 명령이 분리됐고 `lerna changed`가 추가됐습니다. 또, `lerna publish`시 자동으로 Git에 `--no-verify`를 전달하지 않도록 하는 `--commit-hook` 옵션이 추가됐습니다.

----

## Release v3.0.0 · karma-runner/karma
[github.com/karma-runner/karma/releases/tag/v3.0.0](https://github.com/karma-runner/karma/releases/tag/v3.0.0 "Release v3.0.0 · karma-runner/karma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span></p>

Karma 3.0.0이 릴리스 됐습니다. 
타임아웃 기본 시간이 변경됐고 `karma init`으로 `ChromeHeadless`를 선택할 수 있게 됐습니다.

----

## Vue CLI 3.0 is here! – The Vue Point – Medium
[medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb](https://medium.com/the-vue-point/vue-cli-3-0-is-here-c42bebe28fbb "Vue CLI 3.0 is here! – The Vue Point – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Vue CLI 3.0이 릴리스 됐습니다. 
CLI가 재작성된 버전으로 다양한 기능을 갖고 있습니다.
eject 없이 webpack을 설정 할 수 있으며 플러그인 시스템, 대시보드 GUI, 개발 서버를 제공하며 빌드 및 Modern Mode와 관련한 기능이 추가됐습니다.

- [mozilla-neutrino/webpack-chain: A chaining API to generate and simplify the modification of Webpack configurations.](https://github.com/mozilla-neutrino/webpack-chain "mozilla-neutrino/webpack-chain: A chaining API to generate and simplify the modification of Webpack configurations.")

----

## Release v7.0.0-rc.0 · babel/babel
[github.com/babel/babel/releases/tag/v7.0.0-rc.0](https://github.com/babel/babel/releases/tag/v7.0.0-rc.0 "Release v7.0.0-rc.0 · babel/babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7 RC가 릴리스 됐습니다.

----
<h1 class="site-genre">아티클</h1>

----

## AngularJS 대체재로 Angular를 택한 이야기 - BizReach Tech Blog(일본어)
[tech.bizreach.co.jp/posts/51/angular-upgrade/](https://tech.bizreach.co.jp/posts/51/angular-upgrade/ "AngularJSのリプレースにAngularを選んだ話 - BizReach Tech Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">article</span></p>

AngularJS(1.x)로 개발한 페이지를 성능과 장래성의 문제로 인해 Angular(2 이후)로 이전한 내용이 작성돼 있습니다. 복수의 앱에 대응할 수 있도록 UI 컴포넌트를 라이브러리화 하고 Atomic Components, standard-version을 사용한 버전 관리에 관해 이야기합니다.

- [대규모 Angular SPA 개발을 위해 애플리케이션과 UI를 분리한 이야기 - BizReach Tech Blog](https://tech.bizreach.co.jp/posts/204/angular-upgrade-second/ "대규모 Angular SPA 개발을 위해 애플리케이션과 UI를 분리한 이야기 - BizReach Tech Blog")(일본어)

----

## Introducing Electron Fiddle – Felix Rieseberg – Medium
[medium.com/@felixrieseberg/introducing-electron-fiddle-1de2be1ba6e7](https://medium.com/@felixrieseberg/introducing-electron-fiddle-1de2be1ba6e7 "Introducing Electron Fiddle – Felix Rieseberg – Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">article</span> <span class="jser-tag">software</span> <span class="jser-tag">editor</span></p>

Electron 앱을 JSFiddle과 같은 플레이그라운드에서 개발할 수 있도록 제공하는 프로젝트(애플리케이션)에 대해 소개돼 있습니다. 
에디터에 코드를 작성해 Electron 앱을 실행하거나 코드를 gist에 공유하고 앱을 패키징할 수 있습니다.

- [electron/fiddle: 🚀 The easiest way to get started with Electron](https://github.com/electron/fiddle "electron/fiddle: 🚀 The easiest way to get started with Electron")

----

## Variable Scope in Modern JavaScript with var, let and const | Andy Carter
[andy-carter.com/blog/variable-scope-in-modern-javascript](https://andy-carter.com/blog/variable-scope-in-modern-javascript "Variable Scope in Modern JavaScript with var, let and const | Andy Carter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`var`, `let`, `const` 변수의 범위(Scope)에 관해 소개돼 있습니다.

- [함수와 스코프 · JavaScript 입문서 #jsprimer](https://asciidwango.github.io/js-primer/basic/function-scope/ "함수와 스코프 · JavaScript 입문서 #jsprimer")(일본어)

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## NaturalIntelligence/fast-xml-parser: Validate XML, Parse XML to JS/JSON and vise versa, or parse XML to Nimn rapidly without C/C++ based libraries and no callback
[github.com/NaturalIntelligence/fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser "NaturalIntelligence/fast-xml-parser: Validate XML, Parse XML to JS/JSON and vise versa, or parse XML to Nimn rapidly without C/C++ based libraries and no callback")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">XML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Pure JavaScript로 개발한 XML to JSON, JSON to XML 변환 라이브러리입니다.

----
<h1 class="site-genre">도서</h1>

----

## Introduction · Human Redux
[read.reduxbook.com/](https://read.reduxbook.com/ "Introduction · Human Redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">book</span></p>

Redux를 주제로 한 도서입니다. 
Redux 사용 방법, Selector, 루틴, 비동기 처리나 에러 처리, Redux Bundler 등에 관해 작성돼 있습니다.

----

## JavaScript for impatient programmers
[exploringjs.com/impatient-js/](http://exploringjs.com/impatient-js/ "JavaScript for impatient programmers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

JavaScript의 문법이나 기능을 주제로한 JavaScript 초심자 용 도서입니다. 
각 장마다 연습 문제가 준비돼 있고 ES2018를 포함해 주요한 기능을 훑어보면서 학습할 수 있습니다.

----

## React Native + Expo로 시작하는 스마트폰 애플리케이션 개발 ~ JavaScript에 의한 애플리케이션 구축 실전 ~ | 마츠자와 타로 | 책 | 통신 판매 | Amazon(일본어)
[www.amazon.co.jp/dp/4839966648/](https://www.amazon.co.jp/dp/4839966648/ "React Native+Expoではじめるスマホアプリ開発 ~JavaScriptによるアプリ構築の実際~ | 松澤 太郎 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">book</span> <span class="jser-tag">ios</span> <span class="jser-tag">Android</span></p>

2018년 8월 29일 출간 예정인 React Native를 이용한 애플리케이션 개발을 주제로한 도서입니다.

----
