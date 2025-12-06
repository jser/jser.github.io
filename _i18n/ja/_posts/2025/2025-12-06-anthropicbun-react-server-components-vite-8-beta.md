---
title: "2025-12-06のJS: AnthropicがBunを買収、React Server  Componentsの脆弱性、Vite 8 Betaリリース"
author: "azu"
layout: post
date: 2025-12-06T06:31:04.955Z
category: JSer
tags:
- Tools
- Next.js
- TypeScript
- React
- Bun

---

JSer.info #757 - AnthropicがBunを買収することが発表されました。

- [Bun is joining Anthropic | Bun Blog](https://bun.com/blog/bun-joins-anthropic)
- [Anthropic acquires Bun as Claude Code reaches $1B milestone \ Anthropic](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)

今後はClaude Codeチームと連携して開発を進めていく予定ですが、Bun自体はBunとして独立したプロジェクトとして開発を継続するとのことです。

---

React Server Componentsにおいて、任意のコード実行が可能なRCEの脆弱性が発見されました。

- [Critical Security Vulnerability in React Server Components – React](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)

この脆弱性は、Next.jsなどのReact Server Componentsに対応したサーバとして起動している場合に影響があります。ReactやNext.jsなどのセキュリティ修正版がリリースされており、すでにPoCも公開されているため、アプデートが推奨されています。

Next.jsはReactをBundleしているため、個別にアップデートが必要です。
それぞれminorバージョンに対応するセキュリティアップデートがリリースされています。

- [Security Advisory: CVE-2025-66478 | Next.js](https://nextjs.org/blog/CVE-2025-66478)

---

Vite 8 Betaがリリースされました。

- [Vite 8 Beta: The Rolldown-powered Vite | VoidZero](https://voidzero.dev/posts/announcing-vite-8-beta)

このバージョンでは、バンドラとしてRollupの代わりにRolldownを利用するようになります。Rolldownはパフォーマンスの向上を目的としたRollupの代替実装です。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Bun is joining Anthropic | Bun Blog
[bun.com/blog/bun-joins-anthropic](https://bun.com/blog/bun-joins-anthropic "Bun is joining Anthropic | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">news</span></p>

AnthropicがBunを買収した。
今後はClaude Codeチームと連携して開発をしていくが、Bun自体はBunとして開発を継続する予定


----

## Oxfmt: Oxc Formatter Alpha | The JavaScript Oxidation Compiler
[oxc.rs/blog/2025-12-01-oxfmt-alpha.html](https://oxc.rs/blog/2025-12-01-oxfmt-alpha.html "Oxfmt: Oxc Formatter Alpha | The JavaScript Oxidation Compiler")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

JavaScript FormtterであるOxfmtのαリリース。
Prettierの一部オプションのサポートや`printWidth: 100`のデフォルト値の変更などが含まれている。


----

## Release v6.0.0 · tinylibs/tinybench
[github.com/tinylibs/tinybench/releases/tag/v6.0.0](https://github.com/tinylibs/tinybench/releases/tag/v6.0.0 "Release v6.0.0 · tinylibs/tinybench")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">benchmark</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

tinybench v6.0.0リリース


----

## Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier
[prettier.io/blog/2025/11/27/3.7.0](https://prettier.io/blog/2025/11/27/3.7.0 "Prettier 3.7: Improved formatting consistency and new plugin features! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 3.7リリース。


----

## Release pnpm 10.24 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v10.24.0](https://github.com/pnpm/pnpm/releases/tag/v10.24.0 "Release pnpm 10.24 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v10.24.0リリース。
network-concurrencyをCPUのコア数の3倍に設定することで、ネットワークの並列性を改善するなど


----

## 🎉 Ant Design 6.0 is Here! 🎉 · Issue #55804 · ant-design/ant-design
[github.com/ant-design/ant-design/issues/55804](https://github.com/ant-design/ant-design/issues/55804 "🎉 Ant Design 6.0 is Here! 🎉 · Issue #55804 · ant-design/ant-design")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Ant Design 6リリース。
React 18以上を最低要件に変更、React Compilerをサポート、IEサポートを終了。
Pure CSS Variables Style Architectureへの移行、v4で非推奨となったAPIを削除。
Masonryコンポーネントの追加、Drawerのリサイズサポート、マスクのブラー背景などの追加など


----

## Critical Security Vulnerability in React Server Components – React
[react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components "Critical Security Vulnerability in React Server Components – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Reactのセキュリティアップデート。
Next.jsなどのReact Server Componentsに対応したサーバとして起動している場合に、任意のコード実行ができるRCEの脆弱性が存在している。
ReactやNext.js(Next.jsはReactをBundleしているため個別にアップデートが必要)などのセキュリティ修正がリリースされている。


----

## New in Chrome 143  |  Blog  |  Chrome for Developers
[developer.chrome.com/blog/new-in-chrome-143?hl&#x3D;en](https://developer.chrome.com/blog/new-in-chrome-143?hl=en "New in Chrome 143  |  Blog  |  Chrome for Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 143リリース。
CSS Anchor Fallback Container Query/`background-position-x`/`y`の辺相対構文/`font-language-override`プロパティのサポート。
ICU 77へアップデート、EditContext APIの改善、WebTransportアプリケーションプロトコルネゴシエーションの追加。
XSLTの非推奨化など

- [Chrome 143  |  Release notes  |  Chrome for Developers](https://developer.chrome.com/release-notes/143 "Chrome 143  |  Release notes  |  Chrome for Developers")

----

## Vite 8 Beta: The Rolldown-powered Vite | VoidZero
[voidzero.dev/posts/announcing-vite-8-beta](https://voidzero.dev/posts/announcing-vite-8-beta "Vite 8 Beta: The Rolldown-powered Vite | VoidZero")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 8 Betaリリース。
Rollupの代わりにRolldownを利用するようになるバージョン


----
<h1 class="site-genre">アーティクル</h1>

----

## Announcing Baseline in action  |  Blog  |  web.dev
[web.dev/blog/announcing-baseline-in-action?hl&#x3D;en](https://web.dev/blog/announcing-baseline-in-action?hl=en "Announcing Baseline in action  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">browser</span></p>

Baselineについての連載


----

## Accelerate Next.js in Kubernetes
[blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes](https://blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes "Accelerate Next.js in Kubernetes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">kubernetes</span> <span class="jser-tag">performance</span> <span class="jser-tag">linux</span> <span class="jser-tag">article</span></p>

Node.jsアプリケーションをKubernetes環境でスケーリングする際の問題と、Wattを使った93%のレイテンシ改善について。
PM2やclusterモジュールはIPCによる約30%のオーバーヘッドがあり、単一CPUポッドの水平スケーリングでは負荷分散の不均衡が発生する。
WattはLinuxカーネルの`SO_REUSEPORT`を使い、マスタープロセスなしで各ワーカーが直接接続を受け付けることでオーバーヘッドを削減するアプローチを採用していることについて。


----

## Progress on TypeScript 7 - December 2025 - TypeScript
[devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/](https://devblogs.microsoft.com/typescript/progress-on-typescript-7-december-2025/ "Progress on TypeScript 7 - December 2025 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Go言語実装のTypeScript 7の進捗について。
TypeScript 7ではTypeScript 6でDeprecatedとなる予定の機能が削除される。
また、TypeScript 6がJavaScript実装の最後のバージョンとなる。
まだ、APIやJSDocの互換性など既知の問題はあるが、型チェックに関しては安定してきているという話


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## TSDiagram - Diagrams as code with TypeScript
[tsdiagram.com/](https://tsdiagram.com/ "TSDiagram - Diagrams as code with TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">diagram</span></p>

TypeScriptのインターフェースでdiagramを書くツール


----

## vercel/streamdown: A drop-in replacement for react-markdown, designed for AI-powered streaming.
[github.com/vercel/streamdown](https://github.com/vercel/streamdown "vercel/streamdown: A drop-in replacement for react-markdown, designed for AI-powered streaming.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Markdown</span> <span class="jser-tag">library</span></p>

Streaming出力などで壊れているMarkdownを修復してMarkdownとしてレンダリングするためのライブラリ

- [New npm package for automatic recovery of broken streaming markdown - Vercel](https://vercel.com/changelog/new-npm-package-for-automatic-recovery-of-broken-streaming-markdown "New npm package for automatic recovery of broken streaming markdown - Vercel")

----
