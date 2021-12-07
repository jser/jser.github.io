---
title: "2021-11-30: Lighthouse 9.1.0, Storybook 6.4.0, Deno의 Node.js 호환 모드"
author: "azu"
translator: U-Yeong Ju
layout: post
date : 2021-11-30T03:18:08.366Z
category: JSer
tags:
- Tools
- node.js
- CSS
- Chrome
- performance

---

JSer.info #568 - Lighthouse 9.1.0이 릴리스 됐다.

- [Release v9.1.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0)

Next.js 용의 Stack Pack을 추가하여 Next.js 애플리케이션에 대한 Audit을 사용할 수 있다.

- [feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs](https://github.com/GoogleChrome/lighthouse-stack-packs/pull/66)

----

Storybook 6.4.0이 릴리스 됐다.

- [Release v6.4.0 · storybookjs/storybook](https://github.com/storybookjs/storybook/releases/tag/v6.4.0)

[Storybook Addon Interactions](https://github.com/storybookjs/storybook/tree/next/addons/interactions)을 이용하면 Interactions 탭이 추가되며 인터렉션 조작을 시뮬레이션하거나 디버깅이 기능하다.
또, Storybook 용 ESLint 플러그인 [storybookjs/eslint-plugin-storybook](https://github.com/storybookjs/eslint-plugin-storybook)이 함께 공대 됐다.

----

Deno에서는 현재 [Node.js compability mode](https://deno.land/manual@v1.16.3/npm_nodejs/compatibility_mode)을 개발하고 있으며 향후에도 지속적으로 호환성을 높여나갈 방침을 세우고 있다.

- [Improve Node Compat Mode · Issue #12577 · denoland/deno](https://github.com/denoland/deno/issues/12577)

[지금까지 그리고 앞으로의 Deno JSConf JP 2021](https://kt3k.github.io/talk_jsconfjp2021/#1)(일본어)라는 자료에는 이 Node.js 호환 모드 개발이 왜 진행됐는지에 대해서 다루고 있다. 관심 있는 사람은 함께 살펴보길 바란다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/fC4oZJmvfI0?start=9735" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


----

<h1 class="site-genre">헤드라인</h1>

----

## Release 3.0.0 · emscripten-core/emscripten
[github.com/emscripten-core/emscripten/releases/tag/3.0.0](https://github.com/emscripten-core/emscripten/releases/tag/3.0.0 "Release 3.0.0 · emscripten-core/emscripten")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">LLVM</span></p>

Emscripten 3.0.0 릴리스.


----

## Prettier 2.5: TypeScript 4.5 and MDX v2 comment syntax! · Prettier
[prettier.io/blog/2021/11/25/2.5.0.html](https://prettier.io/blog/2021/11/25/2.5.0.html "Prettier 2.5: TypeScript 4.5 and MDX v2 comment syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 2.5 릴리스.
TypeScript 4.5 지원, MDX v2의 주석 문법 지원, HTML의 `class` 속성을 복수행으로 포멧팅 하던 것을 한 줄로 하도록 변경.


----

## Release 8.4 “President Camio” · postcss/postcss
[github.com/postcss/postcss/releases/tag/8.4.0](https://github.com/postcss/postcss/releases/tag/8.4.0 "Release 8.4 “President Camio” · postcss/postcss")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

PostCSS 8.4 릴리스.
Warning과 Error에 Range를 지정할 수 있도록 개선, 플러그인이 지정돼 있지 않은 경우에 CSS 파싱 처리를 실제 접근할 때 까지 지연시키도록 변경(Lazy Parsing). 패키지 크기 개선


----

## Release v9.1.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v9.1.0 "Release v9.1.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse v9.1.0 릴리스.
Next.js 용 audit이 추가됐다.

- [feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs](https://github.com/GoogleChrome/lighthouse-stack-packs/pull/66 "feat: Add Stack Pack for Next.js by kyliau · Pull Request #66 · GoogleChrome/lighthouse-stack-packs")

----

## Release 12.0.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v12.0.0](https://github.com/puppeteer/puppeteer/releases/tag/v12.0.0 "Release 12.0.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Firefox</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer 12.0.0 릴리스.
Chromium 97.0.4692.0으로 업데이트, Firefox에서 `userDataDir`의 지정을 지원한다.


----

## Release v6.4.0 · storybookjs/storybook
[github.com/storybookjs/storybook/releases/tag/v6.4.0](https://github.com/storybookjs/storybook/releases/tag/v6.4.0 "Release v6.4.0 · storybookjs/storybook")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 6.4.0 릴리스.
Interaction stories, ESLint 플러그인이 추가됐다.

- [storybook/addons/interactions at next · storybookjs/storybook](https://github.com/storybookjs/storybook/tree/next/addons/interactions "storybook/addons/interactions at next · storybookjs/storybook")
- [storybookjs/eslint-plugin-storybook: Official ESLint plugin for Storybook](https://github.com/storybookjs/eslint-plugin-storybook "storybookjs/eslint-plugin-storybook: Official ESLint plugin for Storybook")

----

## Release v5.0.0 · chalk/chalk
[github.com/chalk/chalk/releases/tag/v5.0.0](https://github.com/chalk/chalk/releases/tag/v5.0.0 "Release v5.0.0 · chalk/chalk")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Chalk 5.0.0 릴리스.
pure ESM으로 변경, default export에서 named export으로 변경.
`keyword()` / `hsl()` / `hsv()` / `hwb()` / `ansi()` 삭제, Template Literal를 `chalk-template` 패키지로 전환.


----

## berstend/node-safe: 🤠 Make using Node.js safe again with Deno-like permissions
[github.com/berstend/node-safe](https://github.com/berstend/node-safe "berstend/node-safe: 🤠 Make using Node.js safe again with Deno-like permissions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">macOS</span> <span class="jser-tag">security</span> <span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

macOS의 sandbox 기능을 이용하여 Deno와 같은 Sandbox 구조를 구현한 Node 실행 도구.
`--allow-read`, `--allow-net` 등 허가 리스트를 지정하여 스크립트를 실행할 수 있고 npm / yarn / npx에도 대응하고 있다.


----
<h1 class="site-genre">아티클</h1>

----

## CI 환경 에서 유닛 테스트의 실행 시간을 두 배 빠르게 개선(Jest + Mongo DB + Circle CI) - 미츠모어 Tech blog(일본어)
[engineering.meetsmore.com/entry/2021/01/21/134930](https://engineering.meetsmore.com/entry/2021/01/21/134930 "CI 환경 에서 유닛 테스트의 실행 시간을 두 배 빠르게 개선(Jest + Mongo DB + Circle CI) - 미츠모어 Tech blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">jest</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Jest의 유닛 테스트 실행 시간 최적화를 주제로 한 글.
테스트 병렬화, 변경한 파일만 테스트, Worker 단위 DB 초기화, CI에서 캐시하는 방법 등 소개.


----

## Publish ESM and CJS in a single package
[antfu.me/posts/publish-esm-and-cjs](https://antfu.me/posts/publish-esm-and-cjs "Publish ESM and CJS in a single package")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">CommonJS</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">module</span> <span class="jser-tag">article</span></p>

CommonJS와 ESM, 듀얼 포멧으로 패키지를 공개하는 방법
`package.json`의 `exports` 필드 구분 사용법, tsup과 unbuild의 빌드 방식.
ESM에서는 이용할 수 없는 CommonJS의 `__dirname` 등을 보완하는 방법 소개.


----

## New – Real-User Monitoring for Amazon CloudWatch | AWS News Blog
[aws.amazon.com/jp/blogs/aws/cloudwatch-rum/](https://aws.amazon.com/jp/blogs/aws/cloudwatch-rum/ "New – Real-User Monitoring for Amazon CloudWatch | AWS News Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

CloudWatch에서 RUM(Real-User Monitoring)을 가져올 수 있는 서비스가 릴리스 됐다.
JavaScript 태그를 삽입하는 것으로 Web Vitals 등의 측정 지표 등을 살펴볼 수 있다.

- [aws-observability/aws-rum-web: Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web "aws-observability/aws-rum-web: Amazon CloudWatch RUM Web Client")

----
<h1 class="site-genre">슬라이드, 영상</h1>

----

## 지금까지 그리고 앞으로의 Deno JSConf JP 2021(일본어)
[kt3k.github.io/talk\_jsconfjp2021/#1](https://kt3k.github.io/talk_jsconfjp2021/#1 "지금까지 그리고 앞으로의 Deno JSConf JP 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">node.js</span> <span class="jser-tag">slide</span></p>

Deno의 설계와 채택 사례를 주제로 한 슬라이드 자료.
또, 현재 진행하고 있는 Node.js 호환 모드에 대해서도 정리돼 있다.

- [Improve Node Compat Mode · Issue #12577 · denoland/deno](https://github.com/denoland/deno/issues/12577 "Improve Node Compat Mode · Issue #12577 · denoland/deno")

----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## postcss-rs/postcss-rs: 🚀 Fast and 100% API compatible postcss replacer, built in Rust
[github.com/postcss-rs/postcss-rs](https://github.com/postcss-rs/postcss-rs "postcss-rs/postcss-rs: 🚀 Fast and 100% API compatible postcss replacer, built in Rust")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PostCSS</span> <span class="jser-tag">Rust</span></p>

Rust로 구현한 PostCSS.


----

## Tamagui — React Native + Web UI kit
[tamagui.dev/](https://tamagui.dev/ "Tamagui — React Native + Web UI kit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Design</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

React Native와 Web에 대응한 스타일링 라이브러리
Props로 스타일을 전달하는 방식을 채택. 컴파일 시에는 Atomic CSS가 생성되며 컴포넌트에는 클래스 명이 지정된다.


----
