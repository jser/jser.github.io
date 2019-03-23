---
title: "2019-03-18: TypeScript 3.4 RC(readonly), Node.js 11.12.0의 `--frozen-intrinsic`와 시험적 기능 정리"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-03-18T23:34:25.280Z
category: JSer
tags:
- TypeScript
- Node.js

---

JSer.info #427 - TypeScript 3.4 RC가 릴리스됐습니다.

- [TypeScript | Announcing TypeScript 3.4 RC](https://devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/)
- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#34-march-2019 "Roadmap · Microsoft/TypeScript Wiki")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-34 "Breaking Changes · Microsoft/TypeScript Wiki")
- [TypeScript v3.4.0-rc 변경 사항 - Qiita](https://qiita.com/vvakame/items/7f4a55fe15fc9bbe1a63 "TypeScript v3.4.0-rc 변경 사항 - Qiita")(일본어)

CLI에 빌드 정보를 파일에 저장하고 다음 빌드 시 그 정보를 기반으로 동작할 수 있도록 하는 `--incremental` 플래그가 추가 됐습니다.
`--watch`와는 다르게 프로세스가 종료 되더라도 다시 이어서 증분 빌드(incremental build)를 할 수 있습니다.

타입과 관련한 변경 사항으로 `readonly` 수식자를 배열과 tuple에 정의할 수 있도록 됐습니다. 그리고 리터럴에  `readyonly` 적용할 수 있는 `const` assertion과 `"문자열"`이 의도하지 않게 `string` 타입으로 확장되는 문제를 방지할 수 있는 구문이 추가됐습니다.

이 외에도 고차 함수의 타입 추론이 개선됐으며 `globalThis`(Stage 3)의 타입 정의가 추가 됐습니다.

----

Node.js 11.12.0이 릴리스됐습니다.

- [Node v11.12.0 (Current) | Node.js](https://nodejs.org/en/blog/release/v11.12.0/)

Node.js 11.12.0에 `--frozen-intrinsics`라는 시험적인 플래그가 추가됐습니다.
상세한 내용은 구현 PR 등에 작성돼 있습니다만 `--frozen-intrinsics`는 `Array` 등의 자바스크립트 빌트인 객체를 기본적으로 깊게 동결(deep freeze)시키는 플래그입니다.
이 플래그를 활성화하면 몽키 패치(monkey patch)라 부르는 빌트인 객체를 수정하거나 기능을 확장하는 기법을 사용할 수 없는 상태가 됩니다. 따라서 빌트인 객체가 수정되거나 확장돼 있지 않은 상태에서 코드를 살펴볼 수 있는 보안적인 이점을 얻을 수 있습니다.

- [Frozen intrinsics experimental flag by guybedford · Pull Request #25685 · nodejs/node](https://github.com/nodejs/node/pull/25685 "Frozen intrinsics experimental flag by guybedford · Pull Request #25685 · nodejs/node")
- [A Node.js Security Model](https://docs.google.com/document/d/1h__FmXsEWRuNrzAV_l3Iw9i_z8fCXSokGfBiW8-nDNg/edit?ts=5c1adaed#heading=h.xh66r8quma5i)

이와 관련된 사항으로 Secure EcmaScript(SES)와 Node.js 11.8.0에 실험적으로 구현된 Policy 기능을 함께 살펴보면 좋을 것 같습니다.

- [Agoric/SES: Secure EcmaScript](https://github.com/Agoric/SES "Agoric/SES: Secure EcmaScript")
- [2019-01-29のJS: Node.js 11.8.0(Policy機能)、Nuxt.js 2.4.0(TSサポート)、Yarn v2のロードマップ](https://jser.info/2019/01/29/node.js-11.8.0policynuxt.js-2.4.0tsyarn-v2/)

----

[Update on Experimental Features in Node.js - NodeSource](https://nodesource.com/blog/experimental-features-in-node.js)에서는 현재 구현돼 있는 Node.js의 시험적 기능을 소개하고 있습니다.

위에서 언급한 Policy 기능과 Worker Threads, Performance Hooks, Diagnostic Report, ECMAScript Modules에 대해 작성돼 있습니다.

Performance Hooks는 브라우저의 Performance Timing API와의 호환성 관련 내용 뿐 아니라 ECMAScript Module(`.mjs`)의 사용 방법 등에 대해서도 이야기합니다.

관심 있는 분은 해당 글을 참고해 한번 사용해보면 좋을 거 같습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## New in Chrome 73  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/03/nic73](https://developers.google.com/web/updates/2019/03/nic73 "New in Chrome 73  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 73이 릴리스 됐습니다.
데스크탑 크롬에서도 PWA 설치와 Signed HTTP Exchanges, Constructable style sheets, `String#matchAll`를 지원합니다.
`wheel` 이벤트가 기본적으로 Passive로 동작하도록 변경됐습니다.

- [Chrome Platform Status](https://www.chromestatus.com/features#browsers.chrome.desktop%3D73 "Chrome Platform Status")

----

## TypeScript | Announcing TypeScript 3.4 RC
[devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-4-rc/ "TypeScript | Announcing TypeScript 3.4 RC")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.4 RC가 릴리스 됐습니다.
빌드 정보를 파일에 저장하고 다음 동작 시 그 정보를 기반으로 빌드를 이어갈 수 있는 `--incremental`가 추가 됐습니다.
`readonly` 수식자를 배열과 tuple에 정의할 수 있으며 `const` assertion이 추가 됐고 고차 함수의 타입 추론이 개선됐습니다.

- [Roadmap · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Roadmap#34-march-2019 "Roadmap · Microsoft/TypeScript Wiki")
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-34 "Breaking Changes · Microsoft/TypeScript Wiki")
- [TypeScript v3.4.0-rc 변경 사항 - Qiita](https://qiita.com/vvakame/items/7f4a55fe15fc9bbe1a63 "TypeScript v3.4.0-rc 변경 사항 - Qiita")(일본어)

----

## Node v11.12.0 (Current) | Node.js
[nodejs.org/en/blog/release/v11.12.0/](https://nodejs.org/en/blog/release/v11.12.0/ "Node v11.12.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 11.12.0이 릴리스됐습니다.
`Array` 등 빌트인 객체를 기본적으로 동결하는 `--frozen-intrinsics` 플래그가 시험적으로 추가됐습니다.


----

## CKEditor 5 v12.0.0 with inline widgets and distraction free editor released
[ckeditor.com/blog/CKEditor-5-v12.0.0-with-inline-widgets-and-distraction-free-editor-released/](https://ckeditor.com/blog/CKEditor-5-v12.0.0-with-inline-widgets-and-distraction-free-editor-released/ "CKEditor 5 v12.0.0 with inline widgets and distraction free editor released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CKEditor 5 v12.0.0이 릴리스됐습니다.
Inline widgets과 placeholder를 지원하며 Table에 Media를 넣을 수 있도록 변경됐습니다. 또, 인스팩터 기능을 지원하는 디버깅 모듈을 공개했습니다.


----

## Releasing React Native 0.59 · React Native
[facebook.github.io/react-native/blog/2019/03/12/releasing-react-native-059](https://facebook.github.io/react-native/blog/2019/03/12/releasing-react-native-059 "Releasing React Native 0.59 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">ios</span> <span class="jser-tag">andoi</span> <span class="jser-tag">ReleaseNote</span></p>

React Native 0.59가 릴리스됐습니다.
Hooks를 대응하며 JavaScriptCore를 갱신하여 64 bit를 지원합니다. 그리고 일부 코어 컴포넌트를 별개의 라이브러리로 분리했습니다.


----
<h1 class="site-genre">아티클</h1>

----

## 손안의 코드를 성능 측정하는 performance.mark 스니펫 | Web Scratch
[efcl.info/2019/03/14/performance-snnipet/](https://efcl.info/2019/03/14/performance-snnipet/ "손안의 코드를 성능 측정하는 performance.mark 스니펫 | Web Scratch")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`performance.mark`를 사용한 특정 코드의 처리 시간이나 관련 데이터를 기록하는 스니펫을 소개합니다. 측정과 데이터 수집 그리고 어떻게 기록했는지 이야기합니다. 


----

## A Complete React Redux Tutorial for 2019
[daveceddia.com/redux-tutorial/](https://daveceddia.com/redux-tutorial/ "A Complete React Redux Tutorial for 2019")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Redux를 주제로 한 튜토리얼 입니다.
상태 관리 방법, Action의 Dispatch 방법과 동작, React와 같이 사용하는 방법에 대해 작성돼 있습니다.


----

## Node.js and Express Tutorial: Building and Securing RESTful APIs
[auth0.com/blog/node-js-and-express-tutorial-building-and-securing-restful-apis/](https://auth0.com/blog/node-js-and-express-tutorial-building-and-securing-restful-apis/ "Node.js and Express Tutorial: Building and Securing RESTful APIs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">API</span> <span class="jser-tag">article</span></p>

Node.js와 Express를 사용해 Rest API 개발을 주제로 한 튜토리얼 입니다.
Auth0를 사용한 jwt 대응 방법도 소개돼 있습니다.


----

## On the Road to WebRTC 1.0, Including VP8 | WebKit
[webkit.org/blog/8672/on-the-road-to-webrtc-1-0-including-vp8/](https://webkit.org/blog/8672/on-the-road-to-webrtc-1-0-including-vp8/ "On the Road to WebRTC 1.0, Including VP8 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebRTC</span> <span class="jser-tag">article</span> <span class="jser-tag">safari</span></p>

Safari 12.1에서 변경된 WebRTC에 대해 작성돼 있습니다.
VP8코덱, Simulcast, Unified Plan 대응 내용과 Screen capture API 시험적 지원, 비권장된 과거 WebRTC API에 대해 이야기합니다.


----

## Update on Experimental Features in Node.js - NodeSource
[nodesource.com/blog/experimental-features-in-node.js](https://nodesource.com/blog/experimental-features-in-node.js "Update on Experimental Features in Node.js - NodeSource")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js의 시험적 기능을 정리해 소개하는 글입니다.
Worker Threads, Performance Hooks, Diagnostic Report, Policy, ECMAScript Modules에 대해 작성돼 있습니다.


----

## 자사 운영 웹 애플리케이션을 PWA로 바꾸면서 알게된 것（OAuth 등） - APC 기술 블로그
[techblog.ap-com.co.jp/entry/2019/03/13/201027](https://techblog.ap-com.co.jp/entry/2019/03/13/201027 "자사 운영 웹 애플리케이션을 PWA로 바꿀 때 알게된 것（OAuth 등） - APC 기술 블로그")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span> <span class="jser-tag">PWA</span> <span class="jser-tag">Android</span> <span class="jser-tag">Chrome</span></p>

Android와 iOS의 PWA 대응 상황에 대해 정리돼 있는 글입니다.
홈 스크린 애플리케이션으로 실행하면 동작하지 않는 기능을 소개하고 해당 문제를 어떻게 대응했는지 작성돼 있습니다. 


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Yahoo! 뉴스의 BFF 성능 튜닝 사례
[www.slideshare.net/techblogyahoo/yahoobff](https://www.slideshare.net/techblogyahoo/yahoobff "Yahoo! 뉴스의 BFF 성능 튜닝 사례")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

Node.js 서버의 처리 병목 지점 조사 및 벤치마크 하는 방법과 튜닝을 위한 접근 방법 등에 대해 이야기합니다.


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## aruneko/WebUSB-MyNumberCard
[github.com/aruneko/WebUSB-MyNumberCard](https://github.com/aruneko/WebUSB-MyNumberCard "aruneko/WebUSB-MyNumberCard")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

WebUSB를 사용한 마이 넘버 카드 드라이버 모듈입니다.


----

## sindresorhus/type-fest: A collection of essential TypeScript types
[github.com/sindresorhus/type-fest](https://github.com/sindresorhus/type-fest "sindresorhus/type-fest: A collection of essential TypeScript types")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScript의 타입 컬렉션 라이브러리입니다.


----
