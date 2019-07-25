---
title: "2019-07-23: TypeScript 3.6 Beta, postMessage와 성능, Node.js 12의 변경 사항"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-07-23T01:11:39.658Z
category: JSer
tags:
- TypeScript
- performance
- Node.js

---

JSer.info #445 - TypeScript 3.6 Beta가 릴리스 됐습니다.

- [Announcing TypeScript 3.6 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/)
- [Roadmap · microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/issues/202)

Generator / Iterator 타입 개선, 아래와 같은 Array Spread 변환의 엣지케이스에서 사양과 동작 차이가 있었는데 해당 문제가 수정됐습니다.

```ts
[...Array(5)]
```

또, Promise를 사용할 때 `await`을 누락한 경우 발생하는 타입 불일치에 대한 경고 메시지가 좀 더 친절하게 개선 됐습니다. 

----

[Is postMessage slow? — DasSur.ma](https://dassur.ma/things/is-postmessage-slow/)에서는 데이터를 `postMessage`로 전송할 경우의 성능에 관해 작성돼 있습니다.

`postMessage`의 사양에는 객체를 보내기 전 Structured Clone algorithm으로 직렬화하는 방식으로 정리돼 있습니다.
Structured Clone algorithm과 `JSON.stringify`/`JSON.parse`와의 성능을 비교하며, ImmerJS를 사용해 전송할 객체 자체를 부분으로 줄이는 방법도 소개합니다.

또, `ArrayBuffer` 등은 전송 가능한(transferable) 타입이기 때문에 직렬화 비용 없이 보낼 수 있어 데이터의 크기가 큰 경우 장점이 있다는 점과 WebAssembly, SharedArrayBuffer에 대해서도 다루고 있습니다.

`postMessage`로 보낼 페이로드로 객체와 바이너리 중 어느것을 택할지에 대한 기준이나 성능 측정한 데이터도 자세히 정리돼 있습니다.

----

<h1 class="site-genre">헤드라인</h1>

----

## Ember.js - Ember 3.11 Released
[blog.emberjs.com/2019/07/15/ember-3-11-released.html](https://blog.emberjs.com/2019/07/15/ember-3-11-released.html "Ember.js - Ember 3.11 Released")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Ember 3.11이 릴리스 됐습니다.
`...attributes` 문법을 지원하고 `{{fn}}` helper와 `{{on}}` modifier가 추가됐습니다.
그리고 `Function.prototype.observes`를 비권장 합니다.


----

## Recommended security update | Yarn Blog
[yarnpkg.com/blog/2019/07/12/recommended-security-update/](https://yarnpkg.com/blog/2019/07/12/recommended-security-update/ "Recommended security update | Yarn Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">security</span></p>

Yarn 1.17.3이 릴리스 됐습니다.
`*.yarnpkg.com`, `*.npmjs.org`, `*.npmjs.com` 등 3개의 레지스트리에 대한 통신은 자동으로 https로 하도록 수정됐습니다.


----

## Announcing TypeScript 3.6 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-6-beta/ "Announcing TypeScript 3.6 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.6 베타가 릴리스 됐습니다.
Generator/Iterator 타입 개선, Array Spread 변환 개선, Promise의 `await`을 잊었을 경우 등 에러 메시지 개선 등이 이뤄졌습니다>


----

## laverdet/isolated-vm: Secure & isolated JS environments for nodejs
[github.com/laverdet/isolated-vm](https://github.com/laverdet/isolated-vm "laverdet/isolated-vm: Secure & isolated JS environments for nodejs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">V8</span> <span class="jser-tag">JavaScript</span></p>

V8 Isolate 인터페이스를 이용해 Node.js에서 JavaScript를 격리(isolated)한 환경에서 코드를 실행할 수 있는 라이브러리입니다.


----
<h1 class="site-genre">아티클</h1>

----

## Use React.memo() wisely
[dmitripavlutin.com/use-react-memo-wisely/](https://dmitripavlutin.com/use-react-memo-wisely/ "Use React.memo() wisely")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`React.memo()`의 역할과 사용 방법에 대해 정리돼 있습니다.


----

## Google deprecates XSS Auditor for Chrome | The Daily Swig
[portswigger.net/daily-swig/google-deprecates-xss-auditor-for-chrome](https://portswigger.net/daily-swig/google-deprecates-xss-auditor-for-chrome "Google deprecates XSS Auditor for Chrome | The Daily Swig")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">XSS</span> <span class="jser-tag">article</span></p>

MSEdge에 이어서 Chrome의 XSS Auditor도 비권장 됩니다. 비권장 되는 이유와 보안 문제에 대해 정리돼 있습니다.


----

## ES proposal: private class fields
[2ality.com/2019/07/private-class-fields.html](https://2ality.com/2019/07/private-class-fields.html "ES proposal: private class fields")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal의 private class fields를 주제로 한 소개 글입니다.


----

## Is postMessage slow? — DasSur.ma
[dassur.ma/things/is-postmessage-slow/](https://dassur.ma/things/is-postmessage-slow/ "Is postMessage slow? — DasSur.ma")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`postMessage`의 성능에 관한 글입니다. Structured Clone algorithm과 JSON 직렬화의 성능을 비교합니다.
ImmerJS를 사용한 보낼 객체 최소화, ArrayBuffer 등 전송 가능한(transferable) 바이너리 포멧의 성능. 100kb 이내의 데이터는 객체, 그 이상의 데이터는 바이너리로 전송하는 방법 등을 소개합니다.


----

## Datadog와 Lighthouse를 이용한 WebPerf 지속적 측정 | mediba Creator × Engineer Blog(일본어)
[ceblog.mediba.jp/post/186341145447/webperf-measuring-with-lighthouse-and-datadog](https://ceblog.mediba.jp/post/186341145447/webperf-measuring-with-lighthouse-and-datadog "## Datadog와 Lighthouse를 이용한 WebPerf 지속적 측정 | mediba Creator × Engineer Blog(일본어)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Lighthouse로 측정한 값을 Datadog에 저장해 매트릭스를 시각화하는 방법을 소개합니다.


----

## Weak references and finalizers · V8
[v8.dev/features/weak-references](https://v8.dev/features/weak-references "Weak references and finalizers · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

`WeakMap`, `WeakSet`의 약한(weak) 동작에 대해서 이야기합니다.
또, ECMAScript Proposal인 `WeakRef`와 `FinalizationGroup`도 소개합니다.

- [tc39/proposal-weakrefs: WeakRefs](https://github.com/tc39/proposal-weakrefs "tc39/proposal-weakrefs: WeakRefs")

----

## Node.js 12: The future of server-side JavaScript - LogRocket Blog
[blog.logrocket.com/node-js-12/](https://blog.logrocket.com/node-js-12/ "Node.js 12: The future of server-side JavaScript - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.js 12의 주요 변경 사항이 정리돼 있습니다.
V8 갱신에 의한 성능 개선 효과와 TLS 1.3 대응, 힙 크기가 메모리 크기에 의해 결정되도록 변경되는 것과 HTTP 파서 개선 내용 그리고 Diagnostic reports나 heap dump 통합 등 다양한 사항이 소개돼 있습니다. 
또, `worker_thread`의 experimental 플래그가 제거됐고, 실험적으로 ES modules도 지원합니다.


----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Introduction - Content Security Policy
[csp.withgoogle.com/docs/index.html](https://csp.withgoogle.com/docs/index.html "Introduction - Content Security Policy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">XSS</span></p>

CSP(Content Security Policy)에 대해 자세히 소개돼 있는 사이트입니다.
CSP는 어떻게 XSS를 방지하는지, 사용하는 이유와 하지 않는 이유, CSP 설정 방법, FAQ 등이 정리돼 있습니다.


----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## IntrinsicLabs/osgood: Osgood is a secure, fast, and simple platform for running JavaScript HTTP servers.
[github.com/IntrinsicLabs/osgood](https://github.com/IntrinsicLabs/osgood "IntrinsicLabs/osgood: Osgood is a secure, fast, and simple platform for running JavaScript HTTP servers.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">server</span> <span class="jser-tag">Rust</span></p>

Rust로 작성된 V8 기반 HTTP 서버입니다. 루팅 핸들은 Worker로 실행돼 요청에 대한 응답을 반환합니다.

- [Introducing Osgood - DEV Community 👩‍💻👨‍💻](https://dev.to/tlhunter/introducing-osgood-4k1m "Introducing Osgood - DEV Community 👩‍💻👨‍💻")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## zerobias/effector: The state manager ☄️
[github.com/zerobias/effector](https://github.com/zerobias/effector "zerobias/effector: The state manager ☄️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

상태 관리 라이브러리 입니다.
Events와 Effects를 사용해 Store의 State를 갱신하는 일련의 흐름을 관장하는 이름 공간 도메인 API를 제공합니다.
Vue와 React 등 UI 프레임워크 용 어댑터도 제공합니다.


----

## gajus/lightship: Abstracts readiness/ liveness checks and graceful shutdown of Node.js services running in Kubernetes.
[github.com/gajus/lightship](https://github.com/gajus/lightship "gajus/lightship: Abstracts readiness/ liveness checks and graceful shutdown of Node.js services running in Kubernetes.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Kubernetes</span> <span class="jser-tag">node.js</span></p>

Kubernetes의 헬스 체크 등을 위한 추상 계층을 제공하는 Node.js 라이브러리입니다.


----

## ehmicky/test-each: 🤖 Repeat tests. Repeat tests. Repeat tests.
[github.com/ehmicky/test-each](https://github.com/ehmicky/test-each "ehmicky/test-each: 🤖 Repeat tests. Repeat tests. Repeat tests.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span></p>

Data Driven Testing을 수행하기 위한 헬퍼 라이브러리입니다.
데이터로 테스트 케이스를 작성하기 위해 이터레이터를 활용하고 Seed 값을 기초로 무작위 값을 생성하여 테스트할 수 있습니다.


----
