---
title: "2025-04-17: Zod 4 beta, Next.js 15.3과 Rspack, LLM를 사용한 테스트 이행"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-04-17T14:41:52.073Z
category: JSer
tags:
- Next.js
- React
- TypeScript
- test
- css

---

JSer.info #732 - Zod 4 beta가 출시되었습니다.

- [Introducing Zod 4 beta | Zod Docs](https://v4.zod.dev/v4)

성능과 Bundle Size 개선이 있었고, Tree Shaking 가능한 API 제공하는 `@zod/mini`와 `@zod/core` 패키지가 공개되었습니다. 또한, 재귀도 가능한 객체 정의하는 `z.interface()` API, 메타데이터 관리하는 `z.registry()` API, JSON 스킴 변환을 위한 `toJSONSchema()` API가 추가되었습니다. 그 외로는 문자열 Top Level API 추가 및 변경, 에러 메세지를 `message`에서 `error` 파라메터 변경 같은 많은 변경도 포함됩니다.

----

Next.js 15.3 출시되어, Rspack를 빌드도구로 지원합니다.

- [Next.js 15.3 | Next.js](https://nextjs.org/blog/next-15-3)
- [Rspack joins the Next.js ecosystem - Rspack](https://rspack.dev/blog/rspack-next-partner)

Next.js 15.3에서는, Turbopack를 `next build`에도 이용 가능, Rspack 지원, 클라이언트 사이드 계측하는 `instrumentation-client.{js,ts}` 지원, Navigation Hooks 지원 추가도 있습니다. 또한, `useLinkStatus` 추가나 TypeScript LSP 성능 개선도 있습니다. 실험적 기능으로 `<Link unstable_dynamicOnHovertrue>` 지원도 포함됩니다.

----

Airbnb가 Enzyme에서 React Testing Library로 대규모 테스트 이행을 LLM를 활용한 사례에 대해 공개했습니다.

- [Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b)

이행 프로세스를 단계화하고, 재시행 루프 도입, 관련한 테스트나 이행 가이드라인을 컨텐스트로 추가함으로, 당초는 75% 테스트가 자동적으로 이행되었습니다. 여기에, 실패한 파일에 어떤 단계에서 잘 안되었는가 코멘트를 남기고, 그 파일로 학습하면서, 최종적으로 97%까지 자동적으로 이행되었습닌다.

----

{% include inline-support.html %}

----
    
<h1 class="site-genre">헤드라인</h1>

----

## Bun v1.2.9 | Bun Blog
[bun.sh/blog/bun-v1.2.9](https://bun.sh/blog/bun-v1.2.9 "Bun v1.2.9 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.2.9 출시.
Redis 클라이언트 `Bun.redis` 추가, `require.extensions` 지원, `require.resolve`의 `paths` 옵션 지원


----

## Introducing Zod 4 | Zod Docs
[v4.zod.dev/v4](https://v4.zod.dev/v4 "Introducing Zod 4 | Zod Docs")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Zod 4 beta 출시.
성능 개선, Bundle Size 개선, Tree Shaking 가능한 API 제공 `@zod/mini`와 `@zod/core` 패키지 공개.
재귀도 가능한 객체 정의하는 `z.interface()` API 추가, 메타데이터 관리 `z.registry()` API, `toJSONSchema()` API 추가.
문자열 Top Level API 추가 및 변경, 에러 메세지를 `message`에서 `error` 파라메터로 변경


----

## Next.js 15.3 | Next.js
[nextjs.org/blog/next-15-3](https://nextjs.org/blog/next-15-3 "Next.js 15.3 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 15.3 출시.
Turbopack를 `next build`에서도 이용 가능하도록, Rspack 지원, `instrumentation-client.{js,ts}` 지원, Navigation Hooks 지원.
`useLinkStatus` 추가, TypeScript LSP 성능 개선.
실험적 기능으로 `<Link unstable_dynamicOnHovertrue>` 지원


----

## Release 0.12.0 | StyleX
[stylexjs.com/blog/v0.12.0](https://stylexjs.com/blog/v0.12.0 "Release 0.12.0 | StyleX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">css</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

StyleX v0.12.0 출시.
성능 개선, ESLint 플러그인으로 `no-legacy-media-queries` 추가.
`@stylexjs/esbuild-plugin`/`@stylexjs/nextjs-plugin`/`@stylexjs/webpack-plugin` 비권장으로 변경


----

## Shipping Temporal | SpiderMonkey JavaScript/WebAssembly Engine
[spidermonkey.dev/blog/2025/04/11/shipping-temporal.html](https://spidermonkey.dev/blog/2025/04/11/shipping-temporal.html "Shipping Temporal | SpiderMonkey JavaScript/WebAssembly Engine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

SpinderMonkey가 ECMAScript Proposal Stage 3의 Temporal 구현을 Firefox 139에 출시.


----

## Astro 5.7 | Astro
[astro.build/blog/astro-570/](https://astro.build/blog/astro-570/ "Astro 5.7 | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 5.7 출시.
실험적인 Font API 추가, Sessions API가 Stable으로 변경, SVG 파일을 컴포넌트로 읽도록, `astro:config` Stable으로 변경


----
<h1 class="site-genre">읽을거리</h1>

----

## Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium
[medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b](https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b "Accelerating Large-Scale Test Migration with LLMs | by Charles Covey-Brandt | The Airbnb Tech Blog | Mar, 2025 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">test</span> <span class="jser-tag">LanguageModel</span> <span class="jser-tag">article</span></p>

Enzyme에서 React Testing Library으로 이행을 LLM을 활용해 이행한 이야기.
이행 프로레스 단계화, 재시행 루프, 컨텍스트 관련 테스트/이행 가이드라인 추가함으로 75%는 이행.
여기에 단계 별로 어떻게 잘 안되었는가 커멘트 남겨서, 그 파일을 학습함으로 97%까지 자동적으로 이행


----

## Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext
[blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/](https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/ "Deploy your Next.js app to Cloudflare Workers with the Cloudflare adapter for OpenNext")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">cloudflare</span> <span class="jser-tag">article</span></p>

Cloudflare Workers에서 Next.js를 동작하는 OpenNext 관련하여.


----

## WebAssembly 가는 길
[zenn.dev/canary\_techblog/articles/47af6331b4ecfb](https://zenn.dev/canary_techblog/articles/47af6331b4ecfb "WebAssembly 가는 길")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

WebAssembly가 무엇인가 대하여.
WebAssembly가 정의하고 있는 것, 바이트코드 표현과 텍스트 표현, 사양 구현인 Embedder 관련하여


----

## Rspack joins the Next.js ecosystem - Rspack
[rspack.dev/blog/rspack-next-partner](https://rspack.dev/blog/rspack-next-partner "Rspack joins the Next.js ecosystem - Rspack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">rspack</span> <span class="jser-tag">article</span></p>

Next.js의 Rspack 지원


----

## Advanced React in the Wild
[largeapps.dev/case-studies/advanced/](https://largeapps.dev/case-studies/advanced/ "Advanced React in the Wild")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

React으로 작성된 애플리케이션 성능 개선 사례집


----

## Default styles for h1 elements are changing | MDN Blog
[developer.mozilla.org/en-US/blog/h1-element-styles/](https://developer.mozilla.org/en-US/blog/h1-element-styles/ "Default styles for h1 elements are changing | MDN Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">article</span> <span class="jser-tag">browser</span> <span class="jser-tag">css</span></p>

세션 기반 암묵적인 `<h1>` 요소 기본 스타일 (UA 스타일)가 변경됨.
Firefox 138, Chrome 136 이후부터 변경 포함


----
<h1 class="site-genre">웹사이트, 서비스, 문서</h1>

----

## goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)
[github.com/goldbergyoni/nodejs-testing-best-practices](https://github.com/goldbergyoni/nodejs-testing-best-practices "goldbergyoni/nodejs-testing-best-practices: Beyond the basics of Node.js testing. Including a super-comprehensive best practices list and an example app (April 2025)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">test</span> <span class="jser-tag">document</span></p>

Node.js에서 테스트에 관련한 문서


----

## lightpanda-io/browser: Lightpanda: the headless browser designed for AI and automation
[github.com/lightpanda-io/browser](https://github.com/lightpanda-io/browser "lightpanda-io/browser: Lightpanda: the headless browser designed for AI and automation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">zig</span> <span class="jser-tag">browser</span> <span class="jser-tag">software</span></p>

Zig와 V8를 사용해 작성된 헤드리스 브라우저


----

## Ray-D-Song/lexe: Package your Node.js application into a single executable file, but only 10MB.🔥
[github.com/Ray-D-Song/lexe?tab&#x3D;readme-ov-file](https://github.com/Ray-D-Song/lexe?tab=readme-ov-file "Ray-D-Song/lexe: Package your Node.js application into a single executable file, but only 10MB.🔥")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

LLRT를 Runtime으로 사용해 Single Executable Binary를 작성하는 도구.
Node.js 일부에 호환 API 제공, 바이너리 크기가 작다는 특징이 있다


----
<h1 class="site-genre">도서</h1>

----

## 「자료형 시스템 구조」발매 안내 - 마메메모
[mametter.hatenablog.com/entry/2025/04/10/063009](https://mametter.hatenablog.com/entry/2025/04/10/063009 "「자료형 시스템 구조」발매 안내 - 마메메모")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span> <span class="jser-tag">program</span></p>

TypeScript 서브셋 자료형 체커를 구현하는 자료형 시스템에 대한 책


----
