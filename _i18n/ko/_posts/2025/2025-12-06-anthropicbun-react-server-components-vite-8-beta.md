---
title: "2025-12-06: Anthropic가 Bun 인수, React Server  Components 취약성, Vite 8 Beta 출시"
author: "azu"
translator: rewrite0w0
layout: post
date: 2025-12-06T06:35:24.158Z
category: JSer
tags:
- Tools
- Next.js
- TypeScript
- React
- Bun

---

JSer.info #757 - Anthropic가 Bun 인수 발표했다.

- [Bun is joining Anthropic | Bun Blog](https://bun.com/blog/bun-joins-anthropic)
- [Anthropic acquires Bun as Claude Code reaches $1B milestone \ Anthropic](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)

앞으로는 Claude Code 팀과 연계해서 개발을 진행할 예정이지만, Bun 자체는 Bun으로 독립 프로젝트 개발을 계속한다.

---

React Server Components에, 임의 코드 실행 가능한 RCE 취약성이 발견됐다.

- [Critical Security Vulnerability in React Server Components – React](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)

이 취약성은, Next.js 등에서 React Server Components 서버로 기동되는 경우 영향이 있다. React나 Next.js 보안 수정판이 출시되어, 이미 PoC도 공개 되었기에, 업데이트 권장한다.

Next.js는 React를 Bundle하고 있으므로, 개별 업데이트가 필요하다.
각각 minor 버전에 대응하는 보안 업데이트가 출시되어있다.

- [Security Advisory: CVE-2025-66478 | Next.js](https://nextjs.org/blog/CVE-2025-66478)

---

Vite 8 Beta가 출시되었다.

- [Vite 8 Beta: The Rolldown-powered Vite | VoidZero](https://voidzero.dev/posts/announcing-vite-8-beta)

이 버전에는, 번들러로 Rollup 대신 Rolldown 이용한다. Rolldown은 성능 향상 목적을 가진 Rollup 대체 구현이다.

----

{% include inline-support.html %}

----

<h1 class="site-genre">헤드라인</h1>

----

## Bun is joining Anthropic | Bun Blog
[bun.com/blog/bun-joins-anthropic](https://bun.com/blog/bun-joins-anthropic "Bun is joining Anthropic | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">news</span></p>

Anthropic가 Bun를 인수했다.
앞으로는 Claude Code 팀과 연계해서 개발하지만, Bun 자체는 Bun으로 개발 계속될 예정


----

## Oxfmt: Oxc Formatter Alpha | The JavaScript Oxidation Compiler
[oxc.rs/blog/2025-12-01-oxfmt-alpha.html](https://oxc.rs/blog/2025-12-01-oxfmt-alpha.html "Oxfmt: Oxc Formatter Alpha | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript Formtter인 Oxfmt의 α 출시.
Prettier 일부 옵션 지원 및 `printWidth: 100` 기본값 변경 등이 포함된다.


----

## Release v6.0.0 · tinylibs/tinybench
[github.com/tinylibs/tinybench/releases/tag/v6.0.0](https://github.com/tinylibs/tinybench/releases/tag/v6.0.0 "Release v6.0.0 · tinylibs/tinybench")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

tinybench v6.0.0 출시


----

## Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier
[prettier.io/blog/2025/11/27/3.7.0](https://prettier.io/blog/2025/11/27/3.7.0 "Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 3.7 출시.


----

## Release pnpm 10.24 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.24.0](https://github.com/pnpm/pnpm/releases/tag/v10.24.0 "Release pnpm 10.24 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.24.0 출시.
network-concurrency를 CPU 코어의 3배로 설정해서, 네트워크 병렬성 개선


----

## 🎉 Ant Design 6.0 is Here! 🎉 · Issue #55804 · ant-design/ant-design
[github.com/ant-design/ant-design/issues/55804](https://github.com/ant-design/ant-design/issues/55804 "🎉 Ant Design 6.0 is Here! 🎉 · Issue #55804 · ant-design/ant-design")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ant Design 6 출시.
React 18 이상으로 최저요건 변경, React Compiler 지원, IE 지원 종료.
Pure CSS Variables Style Architecture으로 이행, v4에서 비권장이 된 API 삭제.
Masonry 컴포넌트 추가, Drawer 리사이징 지원, 마스터 blur 배경 추가


----

## Critical Security Vulnerability in React Server Components – React
[react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components "Critical Security Vulnerability in React Server Components – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

React 보안 업데이트.
Next.js 등에서 React Server Components 서버 기동하는 경우, 임의 코드 실행 가능한 RCE 취약성이 존재했음.
React나 Next.js(Next.js는 React를 Bundle하고 있기에 따로 업데이트 필요) 보안 수정 출시.


----

## New in Chrome 143  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-143?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-143?hl=en "New in Chrome 143  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 143 출시.
CSS Anchor Fallback Container Query/`background-position-x`/`y` 변수 상대 구문/`font-language-override` 프로퍼티 지원.
ICU 77으로 업데이트, EditContext API 개선, WebTransport 애플리케이션 프로토콜 Negotiation 추가.
XSLT 비권장

- [Chrome 143  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/143 "Chrome 143  |  Release notes  |  Chrome for Developers")

----

## Vite 8 Beta: The Rolldown-powered Vite | VoidZero
[voidzero.dev/posts/announcing-vite-8-beta](https://voidzero.dev/posts/announcing-vite-8-beta "Vite 8 Beta: The Rolldown-powered Vite | VoidZero")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 8 Beta 출시.
Rollup 대신 Rolldown 이용하는 버전


----
<h1 class="site-genre">읽을거리</h1>

----

## Announcing Baseline in action  |  Blog  |  web.dev
[web.dev/blog/announcing-baseline-in-action?hl&#x3D;en](https://web.dev/blog/announcing-baseline-in-action?hl=en "Announcing Baseline in action  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

Baseline 관련한 연재


----

## Accelerate Next.js in Kubernetes
[blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes](https://blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes "Accelerate Next.js in Kubernetes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">kubernetes</span> <span class="jser-tag">performance</span> <span class="jser-tag">linux</span> <span class="jser-tag">article</span></p>

Node.js 애플리케이션를 Kubernetes 환경에서 스케일링 할 때 문제와, Watt를 사용해 93% 레이턴시 개선.
PM2이나 cluster 모듈은 IPC에 의해 약 30% 오버헤드가 있으므로, 단일 CPU 포트의 수평 스케일링은 부하 분산 불균형 발생.
Watt은 Linux 커널의 `SO_REUSEPORT` 사용해, 마스터 프로세스없이 각 워커가 직접 연결을 붙어서 오버헤드를 절감하는 접근법을 이용하고 있음.


----

## Progress on TypeScript 7 - December 2025 - TypeScript
[devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/ "Progress on TypeScript 7 - December 2025 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Go언어 구현한 TypeScript 7 진행 관련하여.
TypeScript 7에는 TypeScript 6에서 Deprecated가 될 예정인 기능이 삭제됨.
또한, TypeScript 6가 JavaScript 구현 최후 버전임.
그리고, API나 JSDoc 호환성 등 기존 알려진 문제가 있던 것들, 자료형 확인 관련해서 안정화하고 있다는 이야기


----
<h1 class="site-genre">소프트웨어, 도구, 라이브러리</h1>

----

## TSDiagram - Diagrams as code with TypeScript
[tsdiagram.com/](https://tsdiagram.com/ "TSDiagram - Diagrams as code with TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">diagram</span></p>

TypeScript 인터페이스에서 diagram를 작성하는 도구


----

## vercel/streamdown: A drop-in replacement for react-markdown, designed for AI-powered streaming.
[github.com/vercel/streamdown](https://github.com/vercel/streamdown "vercel/streamdown: A drop-in replacement for react-markdown, designed for AI-powered streaming.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">library</span></p>

Streaming 출력 등에서 붕괴되는 Markdown를 복구해서 Markdown으로 렌더링하기 위한 라이브러리

- [New npm package for automatic recovery of broken streaming markdown - Vercel](https://vercel.com/changelog/new-npm-package-for-automatic-recovery-of-broken-streaming-markdown "New npm package for automatic recovery of broken streaming markdown - Vercel")

----
