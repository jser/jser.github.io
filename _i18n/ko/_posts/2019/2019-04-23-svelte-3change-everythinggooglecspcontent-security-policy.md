---
title: "2019-04-23: Svelte 3(Change Everything), Google의 CSP(Content Security Policy) 도입 단계"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2019-04-23T01:35:41.198Z
category: JSer
tags:
- Svelte
- CSP
- security

---

JSer.info #432 - 컴파일을 전제로한 UI 컴포넌트 프레임워크인 Svelte 3가 릴리스됐습니다.

- [Svelte 3: Rethinking reactivity](https://svelte.dev/blog/svelte-3-rethinking-reactivity)

3.0.0의 [CHANGELOG의 "Everything"](https://github.com/sveltejs/svelte/blob/master/CHANGELOG.md#300)을 보면 알 수 있듯이 지금까지의 구조를 크게 변경해 재작성한 버전입니다.

템플릿 구문, 컴포넌트에서 사용할 수 있는 API, 상태 변경 시 UI 갱신을 위한 전파 구조(reactive)가 변경됐습니다. 

기존에는 컴포넌트의 상태를 `set` API 등을 사용해 변경하고 UI에 반영했습니다.

```html
<p>{count} doubled is {double}</p>
<button on:click="set({ count: count + 1 })">+1</button>

<script>
	export default {
		data() {
			return {
				count: 0
			};
		},
        computed: {
			doubled: ({ count }) => count * 2
		}
	};
</script>
```

Svelte 3부터는 다음과 같이 변경을 탐지하고자 하는 문을 `$` 라벨([JavaScript의 라벨](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label))로 애너테이션합니다. 이 라벨로 지정된 변수의 값이 변경 됐을 때 UI를 갱신하는 코드가 컴파일 시 생성됩니다(`$$invalidate`라는 변경을 전파하는 코드가 빌드 파일에 포함됩니다).

```html
<p>{count} doubled is {doubled}</p>
<button on:click="{() => count += 1}">+1</button>

<script>
	let count = 0;
	$: doubled = count * 2;

	function handleClick() {
		count += 1;
	}
</script>
```

위와 같은 선언적인 Reactivity에 대해서는 다음 문서나 RFC를 살펴보면 좋을 것 같습니다.

- [Reactivity / Declarations • Svelte Tutorial](https://svelte.dev/tutorial/reactive-declarations)
- [rfcs/0003-reactive-declarations.md at master · sveltejs/rfcs](https://github.com/sveltejs/rfcs/blob/master/text/0003-reactive-declarations.md)

아주 간단히 설명하자면 `@observable`과 같은 [​아직 책정 중의 Decorator 구문](https://github.com/tc39/proposal-decorators)을 사용하는게 아니라 이미 존재하는 [label 문](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)과 `$` 라벨을 사용해 컴파일 시 변수 등을 Observable하게 만드는 방식입니다.

이 외에도 [Write less code](https://svelte.dev/blog/write-less-code)에 따른 변경 사항이 많이 포함된 버전이므로 자세한 내용은 공식 사이트를 꼼꼼히 살펴보는게 좋을 것 같습니다.

- [Svelte • Cybernetically enhanced web apps](https://svelte.dev/)


----

[Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck](https://speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation) 슬라이드에는 구글 주요 도메인의 CSP(Content Security Policy) 도입 상황과 단계 등이 소개돼 있습니다.

구글 도메인의 CSP 도입 정도를 나타내는 커버리지와 CSP 상에서의 XSS 차단율과 원리를 소개합니다. 또, CSP의 4개 레벨과 도입 단계, 명시적 허가 목록(whitelist) 문제와 nonce-based CSP, CSP와 배포(deploy) 환경과의 절충점(trade off)에 대해서도 이야기 합니다.

CSP의 설정(directive)에 따라서 eval이나 inline code를 사용할 수 없을수도 있기 있으며 이에 따른 CSP 대응 리팩터링 방법과 도입을 위한 각 단계가 소개돼 있습니다.

이 슬라이드에서 언급하고 있는 화이트리스트 문제와 nonce-based CSP는 다음 글을 참고하면 도움이 될 거 같습니다.

- [Content Security Policy Level 3의 XSS 대책 - pixiv inside](https://inside.pixiv.blog/kobo/5137 "Content Security Policy Level 3의 XSS 대책 - pixiv inside")(일본어)

----

<h1 class="site-genre">헤드라인</h1>

----

## alibaba/rax: \[ v1.0 released\] The fastest way to build universal application.
[github.com/alibaba/rax](https://github.com/alibaba/rax "alibaba/rax: \[ v1.0 released\] The fastest way to build universal application.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

React와 같은 API를 갖는 Universal View 라이브러리인 Rax 1.0.0이 릴리스됐습니다.
Hooks API를 지원합니다.


----

## Release v5.0.0 · sindresorhus/np
[github.com/sindresorhus/np/releases/tag/v5.0.0](https://github.com/sindresorhus/np/releases/tag/v5.0.0 "Release v5.0.0 · sindresorhus/np")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm publish하는 np 5.0.0이 릴리스됐습니다.
새롭게 공개하는 패키지에 관해서는 이중 인중이 자동으로 활성화 되며 공개에 실패한 경우를 위한 롤백 처리가 개선됐습니다.


----

## Release Notes for Safari Technology Preview 80 | WebKit
[webkit.org/blog/8825/release-notes-for-safari-technology-preview-80/](https://webkit.org/blog/8825/release-notes-for-safari-technology-preview-80/ "Release Notes for Safari Technology Preview 80 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 80이 릴리스됐습니다.
ResizeObserver, `contentWindow`와 `window.open`의 두번째 인수에 `noreferrer`를 지원합니다.
또, Legacy Safari Extensions가 지원 종료 됐습니다.

----

## Blog - Next.js 8.1 | Next.js
[nextjs.org/blog/next-8-1](https://nextjs.org/blog/next-8-1 "Blog - Next.js 8.1 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">AMP</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 8.1이 릴리스됐습니다.
AMP를 지원합니다. 컴포넌트 내에서 AMP를 위한 처리를 분기할 수 있는 hybrid 방식을 지원하며 `next export`로 AMP로의 출력과 검증이 가능합니다.


----

## Release 10.0.0-beta.0 Reconcilertron · developit/preact
[github.com/developit/preact/releases/tag/10.0.0-beta.0](https://github.com/developit/preact/releases/tag/10.0.0-beta.0 "Release 10.0.0-beta.0 Reconcilertron · developit/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.0.0-beta.0이 릴리스됐습니다.
`Fragments`가 안정화 됐고 조건 분기를 포함하는 프리젠테이션 성능이 개선됐습니다. 이어 컴포넌트의 계층 관계를 고려해 갱신을 처리하도록 수정됐습니다.


----

## Svelte 3: Rethinking reactivity
[svelte.dev/blog/svelte-3-rethinking-reactivity](https://svelte.dev/blog/svelte-3-rethinking-reactivity "Svelte 3: Rethinking reactivity")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

컴파일을 전제로한 UI 프레임워크 Svelte 3가 릴리스됐습니다.
기존의 구조를 새롭게 재작성 했기 때문에 템플릿 구문, API 뿐 아니라 웹사이트도 함께 변경됐습니다.
변경을 전파, 탐지하는 방식이 크게 바뀌어 `set` API가 아니라 reactive 변수를 `$:` 선언하며 컴파일 시 변경을 전파하는 코드를 생성하는 방식으로 변경됐습니다.


----
<h1 class="site-genre">아티클</h1>

----

## TypeScript 재입문 「느슨한 TypeScript」를 이용해 JavaScript를 “유연한” 정적 타입 언어로（gfx집필） - 엔지니어 Hub｜젊은 웹 엔지니어의 경력을 생각하다！
[employment.en-japan.com/engineerhub/entry/2019/04/16/103000](https://employment.en-japan.com/engineerhub/entry/2019/04/16/103000 "TypeScript 재입문 「느슨한 TypeScript」를 이용해 JavaScript를 “유연한” 정적 타입 언어로（gfx집필） - 엔지니어 Hub｜젊은 웹 엔지니어의 경력을 생각하다！")(일본어)
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

느슨한 타입 환경으로 TypeScript를 시작하는 방법과 장점을 이야기합니다.


----

## A horrifying globalThis polyfill in universal JavaScript · Mathias Bynens
[mathiasbynens.be/notes/globalthis](https://mathiasbynens.be/notes/globalthis "A horrifying globalThis polyfill in universal JavaScript · Mathias Bynens")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">polyfill</span> <span class="jser-tag">article</span></p>

`globalThis`의 polyfill과 동작 원리를 설명합니다.


----

## Experimental Node.js: testing the new performance hooks
[blog.logrocket.com/experimental-node-js-testing-the-new-performance-hooks-31fcdd2a747e](https://blog.logrocket.com/experimental-node-js-testing-the-new-performance-hooks-31fcdd2a747e "Experimental Node.js: testing the new performance hooks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Node.js `perf_hooks`의 사용 방법에 대해 작성돼 있습니다.
모듈을 불러오는 시간이나 URL의 요청 시간을 측정하는 것을 예로 설명하고 있습니다.


----

## The perfect unit test
[javascriptplayground.com/the-perfect-javascript-unit-test/](https://javascriptplayground.com/the-perfect-javascript-unit-test/ "The perfect unit test")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Unit Test를 작성하는 방법에 대한 짧은 글입니다.
테스트 케이스의 이름을 작성하는 방법, 테스트 설정, 코드 실행, Assert를 세 가지 단계로 나눠 작성하는 방법을 소개합니다.


----

## A RealWorld Comparison of Front-End Frameworks with Benchmarks (2019 update)
[medium.freecodecamp.org/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075](https://medium.freecodecamp.org/a-realworld-comparison-of-front-end-frameworks-with-benchmarks-2019-update-4be0d3c78075 "A RealWorld Comparison of Front-End Frameworks with Benchmarks (2019 update)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span> <span class="jser-tag">benchmark</span></p>

"RealWorld" 벤치마크 앱을 기반으로 각 JavaScript 프레임워크 구현체의 성능을 비교한 글입니다.
성능, 빌드된 파일의 크기, Line of Code(LOC) 항목으로 나눠 각 프레임워크를 비교한 결과가 정리돼 있습니다.

- [gothinkster/realworld: &quot;The mother of all demo apps&quot; — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more 🏅](https://github.com/gothinkster/realworld "gothinkster/realworld: &amp;quot;The mother of all demo apps&amp;quot; — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more 🏅")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck
[speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation](https://speakerdeck.com/mikispag/content-security-policy-a-successful-mess-between-hardening-and-mitigation "Content Security Policy: A successful mess between hardening and mitigation - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSP</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">slide</span></p>

구글의 CSP에 관한 슬라이드입니다. Google 도메인의 CSP 도입 정도를 나타내는 커버리지와 CSP 상에서의 XSS 차단율과 원리를 소개합니다.
CSP의 4개 레벨과 도입 단계, 명시적 허가 목록(whitelist) 문제와 nonce-based CSP, CSP와 배포(deploy) 환경과의 절충점(trade off)에 대해서 작성돼 있으며 CSP 대응을 위한 리팩터링 방법과 도입을 위한 각 단계가 소개돼 있습니다.

- [Content Security Policy Level 3におけるXSS対策 - pixiv inside](https://inside.pixiv.blog/kobo/5137 "Content Security Policy Level 3におけるXSS対策 - pixiv inside")

----
<h1 class="site-genre">사이트, 서비스, 문서</h1>

----

## isInputPending: Facebook's first browser API contribution - Facebook Code
[code.fb.com/developer-tools/isinputpending-api/](https://code.fb.com/developer-tools/isinputpending-api/ "isInputPending: Facebook's first browser API contribution - Facebook Code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">browser</span></p>

`navigator.scheduling.isInputPending()`를 사용해 사용자 조작 중에 큐에 쌓인 작업을 처리하지 않도록 제어하는 방법에 대해 작성돼 있습니다.
불러오기가 완료될 때까지 사용자가 조작할수 없는 시간인 First Input Delay(FID)를 줄일 수 있는 방법에 대해 이야기합니다. 

- [First Input Delay  |  Web  |  Google Developers](https://developers.google.com/web/updates/2018/05/first-input-delay "First Input Delay  |  Web  |  Google Developers")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## Do you really know how a lockfile works for yarn and npm packages? | Snyk
[snyk.io/blog/making-sense-of-package-lock-files-in-the-npm-ecosystem/](https://snyk.io/blog/making-sense-of-package-lock-files-in-the-npm-ecosystem/ "Do you really know how a lockfile works for yarn and npm packages? | Snyk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">yarn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

yarn의 `yarn.lock`, npm의 `package-lock.json`가 실제로 어떻게 동작하는지, 애플리케이션과 라이브러리 록(lock) 파일에 대해 작성돼 있습니다.


----

## stryker-mutator/stryker: Mutation testing for JavaScript and friends
[github.com/stryker-mutator/stryker](https://github.com/stryker-mutator/stryker "stryker-mutator/stryker: Mutation testing for JavaScript and friends")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">C#</span> <span class="jser-tag">scala</span></p>

Mutation testing 라이브러리입니다.
테스트 코드를 테스트하기 위한 프레임워크 입니다. 
mocha나 jest 등의 여러 테스트 프레임워크와 연동해 동작합니다.

- [stryker-mutator/stryker-handbook: A comprehensive guide to the stryker ecosystem](https://github.com/stryker-mutator/stryker-handbook#readme "stryker-mutator/stryker-handbook: A comprehensive guide to the stryker ecosystem")
- [stryker/packages/core at master · stryker-mutator/stryker](https://github.com/stryker-mutator/stryker/tree/master/packages/core#readme "stryker/packages/core at master · stryker-mutator/stryker")
- [Blog - Stryker Mutator](https://stryker-mutator.io/blog/2017-01-17/introduction-to-mutation-testing "Blog - Stryker Mutator")

----

## lancedikson/bowser: a browser detector
[github.com/lancedikson/bowser](https://github.com/lancedikson/bowser "lancedikson/bowser: a browser detector")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span></p>

User-Agent를 이용해 브라우저 명과 버전 등을 구조적인 데이터로 가져올 수 있는 라이브러리입니다.


----

## sindresorhus/file-type: Detect the file type of a Buffer/Uint8Array/ArrayBuffer
[github.com/sindresorhus/file-type](https://github.com/sindresorhus/file-type "sindresorhus/file-type: Detect the file type of a Buffer/Uint8Array/ArrayBuffer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

Content sniffing 하여 파일의 종류를 판단하는 Node.js 라이브러리입니다.


----
<h1 class="site-genre">도서</h1>

----

## Front-end Developer Handbook 2019 - Learn the entire JavaScript, CSS and HTML development practice!
[frontendmasters.com/books/front-end-handbook/2019/](https://frontendmasters.com/books/front-end-handbook/2019/ "Front-end Developer Handbook 2019 - Learn the entire JavaScript, CSS and HTML development practice!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span> <span class="jser-tag">links</span></p>

프런트엔드 개발에 관한 개요 그리고 기술을 항목별 리소스를 정리한 전자 도서의 2019년 판입니다. 


----
