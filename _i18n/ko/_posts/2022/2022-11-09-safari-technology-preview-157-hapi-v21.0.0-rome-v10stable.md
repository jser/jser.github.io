---
title: "2022-11-09: Safari Technology Preview 157, hapi v21.0.0, Rome v10(Stable)"
author: "azu"
translator: rewrite0w0(Oh TaeJun)
layout: post
date : 2022-11-09T03:08:56.671Z
category: JSer
tags:
- React
- Remix
- node.js
- Vue
- vite

---

JSer.info #617 - Safari Technology Preview 157가 출시됐다.

- [Release Notes for Safari Technology Preview 157 | WebKit](https://webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/)

CSS의 `@font-feature-settings` 지원, ES2022 class static initialization blocks 지원, [WebCodecs API](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) 지원이 개선됐다.
[`Sec-Fetch-Site` HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site)헤더 지원, A레코드를 사용한 third-party CNAME Cloaking의 Cookie 7일 제한 구현 등이 포함된다.

- [Cap cookie lifetimes to 7 days for responses from third party IP addresses by whsieh · Pull Request #5347 · WebKit/WebKit](https://github.com/WebKit/WebKit/pull/5347)

---

Node.js 웹 애플리케이션 프레임워크 hapi v21.0.0가 출시됐다.

- [Release v21.0.0 · hapijs/hapi](https://github.com/hapijs/hapi/releases/tag/v21.0.0)
- [21.0.0 Release Notes · Issue #4386 · hapijs/hapi](https://github.com/hapijs/hapi/issues/4386)

Node.js 12 지원 종료, JSONP 지원 종료 그리고 Node.js 18 지원 추가 등.
또한 hapi 플러그인 등은 hapi v20+ 이상만 지원하도록 하는 변경안이 포함되어있다.

---

Rome v10가 출시됐다.

- [Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript](https://rome.tools/blog/2022/11/08/rome-10.html)

Rust로 새로 쓴 이후의 첫 Stable 출시 버전으로, 0.10.0에서 10.0.0 으로 버전 상승했다.
Stable 기능으로 Prettier 같은 Formatter와 ESLint 같은 규칙을 포함하는 Linter가 이용 가능하다.

----

<h1 class="site-genre">헤드라인</h1>

----

## vuetifyjs/vuetify: 🐉 Material Component Framework for Vue
[github.com/vuetifyjs/vuetify/releases/tag/v3.0.0](https://github.com/vuetifyjs/vuetify/releases/tag/v3.0.0 "vuetifyjs/vuetify: 🐉 Material Component Framework for Vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vuetify v3.0.0 출시.
현시점에는 `vuetify@next`로 설치 가능.


----

## Release v4.0.0-alpha.0 · vitejs/vite
[github.com/vitejs/vite/releases/tag/v4.0.0-alpha.0](https://github.com/vitejs/vite/releases/tag/v4.0.0-alpha.0 "Release v4.0.0-alpha.0 · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite v4.0.0-alpha.0 출시.
rollup 3로 업그레이드


----

## Release Notes for Safari Technology Preview 157 | WebKit
[webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/](https://webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/ "Release Notes for Safari Technology Preview 157 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 157 출시.
CSS `@font-feature-settings` 지원, ES2022의 class static initialization blocks 지원, WebCodecs API 지원 개선.
`Sec-Fetch-Site` HTTP 헤더 지원, A레코드를 사용한 third-party CNAME Cloaking의 Cookie 7일 제한 구현 등.


----

## Release v21.0.0 · hapijs/hapi
[github.com/hapijs/hapi/releases/tag/v21.0.0](https://github.com/hapijs/hapi/releases/tag/v21.0.0 "Release v21.0.0 · hapijs/hapi")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hapi 21.0.0 출시.
Node.js 12 지원 종료, JSONP 지원 종료 및 Node.js 18 지원 추가 등.
또한 hapi 플러그인 등은 hapi v20+ 이상에서만 지원된다는 변경도 포함됐다.

- [21.0.0 Release Notes · Issue #4386 · hapijs/hapi](https://github.com/hapijs/hapi/issues/4386 "21.0.0 Release Notes · Issue #4386 · hapijs/hapi")

----

## Deprecate array prototype extensions
[rfcs.emberjs.com/id/0848-deprecate-array-prototype-extensions/](https://rfcs.emberjs.com/id/0848-deprecate-array-prototype-extensions/ "Deprecate array prototype extensions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">proposal</span></p>

Ember.js에서 prototype 확장하지 않도록 하는 Proposal.
Ember.js 4.9.0에는 prototype 확장을 기본으로 무효로 하는 변경이 예정되어 있다.

- [Release Release 4.9.0-beta.0 · ember-cli/ember-cli](https://github.com/ember-cli/ember-cli/releases/tag/v4.9.0-beta.0 "Release Release 4.9.0-beta.0 · ember-cli/ember-cli")

----

## Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript
[rome.tools/blog/2022/11/08/rome-10.html](https://rome.tools/blog/2022/11/08/rome-10.html "Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rome v10 출시.
Rust로 새로 쓴 이후의 첫 Stable 출시.
Prettier 같은 Formatter와 ESLint 같은 규칙을 포함하는 Linter가 이용 가능하다.


----

## Changelog | Cypress Documentation
[docs.cypress.io/guides/references/changelog#11-0-0](https://docs.cypress.io/guides/references/changelog#11-0-0 "Changelog | Cypress Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">ReleaseNote</span></p>

Cypress 11.0.0 출시.
컴포넌트 테스트 Stable화, V8 스냅샷 사용한 기동 성능 개선, `cy.*Cookie()` API로 도메인을 지정할 수 있도록 함.
파괴적 변경으로는 컴포넌트 테스트 관련 API나 설정 변경 등.


----

## Nov 3 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/november-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/november-2022-security-releases/ "Nov 3 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">seuc</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 보안 업데이트가 각 버전마다 갱신됐다.

- Node.js v14.21.1 (LTS)
- Node.js v16.18.1 (LTS)
- Node.js v18.12.1 (LTS)
- Node.js v19.0.1 (Current)


----
<h1 class="site-genre">읽을거리</h1>

----

## React Router-ing Remix | Remix
[remix.run/blog/react-routering-remix](https://remix.run/blog/react-routering-remix "React Router-ing Remix | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

React Router에 Remix의 Data API를 이행한 이야기
파괴적 변경 없이 어떻게 처리를 이행할 수 있는가에 대해. Feature Flag를 사용해 빌드 할 때 처리 감소하면서 호환성 담보, 새로운 기능을 어떻게 시도해 보는가에 대하여.

- [React Router 6.4 Release | Remix](https://remix.run/blog/react-router-v6.4 "React Router 6.4 Release | Remix")

----

## Full Stack Components | Epic Web Dev by Kent C. Dodds
[www.epicweb.dev/full-stack-components](https://www.epicweb.dev/full-stack-components "Full Stack Components | Epic Web Dev by Kent C. Dodds")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Remix의 `useFetcher`로 보류상태를 갖는 UI 컴포넌트 구현에 대해서.


----

## What is a realm in JavaScript? · Gal Weizman
[weizman.github.io/page-what-is-a-realm-in-js/](https://weizman.github.io/page-what-is-a-realm-in-js/ "What is a realm in JavaScript? · Gal Weizman")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Realm이란 무엇인가 해설 기사


----

## 개인 블로그 Next.js v13 이행기
[zenn.dev/panda\_program/scraps/6c66f160636969](https://zenn.dev/panda_program/scraps/6c66f160636969 "개인 블로그 Next.js v13 이행기")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Next.js 13로 업데이트를 다룬 기사.
`pages/`에서 `app/`로 이행한 경우에 컴포넌트 변경, 외부 도구 대응 등에 대하여


----
