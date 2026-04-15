---
title: "2026-04-15のJS: pnpm 11 RC 0、webpack 5.106、Servo v0.1.0"
author: "azu"
layout: post
date: 2026-04-15T11:18:42.246Z
category: JSer
tags:
- React
- Rust
- search
- Next.js
- security

---

JSer.info #769 - pnpm v11.0.0 RC 0がリリースされました。

- [Release pnpm 11 RC 0 · pnpm/pnpm](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0)

Pure ESMパッケージへ移行し、Node.js 18から21のサポートを終了しています。
`.npmrc`は認証/レジストリ設定のみに限定し、その他の設定は`pnpm-workspace.yaml`へ移行、`pnpm server`コマンドの削除など多くの破壊的変更を含んでいます。
また、`pnpm ci`コマンドの追加、`pnpm sbom`でのSBOM生成に対応しています。
`minimumReleaseAge`のデフォルトを1日に設定、`blockExoticSubdeps`のデフォルトを`true`に変更するなど、サプライチェーンセキュリティの強化も行われています。
その他にも、ストアのインデックスにSQLiteを使用するように変更、`undici`の採用によるHTTPリクエストの改善なども含まれています。

----

webpack 5.106がリリースされました。

- [Webpack 5.106 | webpack](https://webpack.js.org/blog/2026-04-08-webpack-5-106/)

Plugin Validation Hook(`compiler.hooks.validate`)の追加、CSS Modulesのランタイムスタイル注入(`exportType: "style"`)のサポートが含まれています。
将来的にcss-loader/style-loader/mini-css-extract-pluginの廃止が予定されています。
その他にも、CommonJSのTree Shaking改善、`create-webpack-app`ツールの追加、実験的な機能としてES Stage 3のSource Phase ImportsによるWebAssemblyサポート、oxc-parserのサポートが追加されています。
また、webpack-cli 7.0.0ではNode.js 20.9.0以上が必要となり、ネイティブTypeScriptサポートが追加されています。

----

Rustで書かれた組み込み可能なWebレンダリングエンジンであるServoの`servo`クレートがcrates.ioで公開されました。

- [Servo is now available on crates.io](https://servo.org/blog/2026/04/13/servo-0.1.0-release/)

アプリケーションにWebレンダリング機能を組み込むためのEmbedding APIを提供しています。
また、LTSバージョンも導入され、半年ごとのメジャーアップグレードとセキュリティアップデートが提供されます。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v1.5.0 · Pagefind/pagefind
[github.com/Pagefind/pagefind/releases/tag/v1.5.0](https://github.com/Pagefind/pagefind/releases/tag/v1.5.0 "Release v1.5.0 · Pagefind/pagefind")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">search</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Pagefind v1.5.0リリース。
Web Componentsベースの新しいUIシステムの追加、メタデータフィールドのデフォルトインデックス化による検索精度の向上、ダイアクリティカルマーク(発音区別符号)の対応を追加。
CJK(中国語/日本語/韓国語)のクエリ自動セグメンテーション、Web Workerでの検索実行、インデックスチャンクのサイズ削減などパフォーマンスの改善。
Windows ARM64のサポートを追加など


----

## Webpack 5.106 | webpack
[webpack.js.org/blog/2026-04-08-webpack-5-106/](https://webpack.js.org/blog/2026-04-08-webpack-5-106/ "Webpack 5.106 | webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5.106リリース。
Plugin Validation Hook(`compiler.hooks.validate`)の追加。
CSS Modulesのランタイムスタイル注入(`exportType: "style"`)のサポート。
将来的にcss-loader/style-loader/mini-css-extract-pluginを廃止予定。
CommonJSのTree Shaking改善、`create-webpack-app`ツールの追加。
実験的な機能として、ES Stage 3のSource Phase Importsによる実験的なWebAssemblyサポート、oxc-parserのサポート。
webpack-cli 7.0.0ではNode.js 20.9.0+が必要となり、ネイティブTypeScriptサポートが追加されている。


----

## Release pnpm 11 RC 0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0](https://github.com/pnpm/pnpm/releases/tag/v11.0.0-rc.0 "Release pnpm 11 RC 0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v11.0.0 rc.0リリース。
Pure ESMパッケージへの移行、Node.js 18-21のサポートを終了。
`.npmrc`は認証/レジストリ設定のみに限定し、その他の設定は`pnpm-workspace.yaml`へ移行、`pnpm server`コマンドの削除など多くの破壊的変更を含む。
`pnpm ci`コマンドの追加、`pnpm sbom`でのSBOM生成に対応。
`minimumReleaseAge`のデフォルトを1日に設定、`blockExoticSubdeps`のデフォルトを`true`に変更などサプライチェーンセキュリティの強化。
ストアのインデックスにSQLiteを使用するように変更、`undici`の採用によるHTTPリクエストの改善など。


----

## Bun v1.3.12 | Bun Blog
[bun.com/blog/bun-v1.3.12](https://bun.com/blog/bun-v1.3.12 "Bun v1.3.12 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.3.12リリース。
`Bun.WebView`の追加、Markdownファイルをターミナルで直接実行できる`bun ./file.md`のサポート。
インプロセスで動作するコールバックベースのcronスケジューラ`Bun.cron()`の追加。
JavaScriptCoreのアップグレードにより、ES ProposalのStage 3のExplicit Resource Management(`using`/`await using`)のサポート。。
cgroupのCPU制限を考慮するように変更など


----

## Servo is now available on crates.io - Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.
[servo.org/blog/2026/04/13/servo-0.1.0-release/](https://servo.org/blog/2026/04/13/servo-0.1.0-release/ "Servo is now available on crates.io - Servo aims to empower developers with a lightweight, high-performance alternative for embedding web technologies in applications.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">servo</span> <span class="jser-tag">Rust</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

Servo v0.1.0リリース。
Rustで書かれた組み込み可能なWebレンダリングエンジンServoの`servo`クレートがcrates.ioで公開された。
アプリケーションにWebレンダリング機能を組み込むためのEmbedding APIを提供する。
LTSバージョンも導入され、半年ごとのメジャーアップグレードとセキュリティアップデートが提供される。


----
<h1 class="site-genre">アーティクル</h1>

----

## Summary of CVE-2026-23869 - Vercel
[vercel.com/changelog/summary-of-cve-2026-23869](https://vercel.com/changelog/summary-of-cve-2026-23869 "Summary of CVE-2026-23869 - Vercel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">security</span> <span class="jser-tag">vercel</span></p>

React Server Components(RSC)のDoS脆弱性の修正としてNext.js 15.5.15/16.2.3とReact 19.2.5がリリースされている。
App RouterのServer Functionエンドポイントに対して、細工されたHTTPリクエストを送ることで過剰なCPU消費を引き起こせる脆弱性。
Next.js 13.x〜16.xが影響を受けている。

- [Release 19.2.5 (April 8th, 2026) · facebook/react](https://github.com/facebook/react/releases/tag/v19.2.5 "Release 19.2.5 (April 8th, 2026) · facebook/react")

----

## The uphill climb of making diff lines performant - The GitHub Blog
[github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/](https://github.blog/engineering/architecture-optimization/the-uphill-climb-of-making-diff-lines-performant/ "The uphill climb of making diff lines performant - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GitHub</span> <span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

GitHubのFiles changedタブのReactベースの実装におけるdiff行のパフォーマンス最適化について。
1行あたり10〜15個のDOM要素と8〜13個のReactコンポーネントが必要だった構造を最適化している。
コンポーネント数を2個に削減し、イベントハンドラをdata属性を活用した単一のハンドラに集約するなどの変更をした。
TanStack Virtualによる仮想化の導入、重いCSSセレクタの削除、ドラッグ/リサイズ処理の再実装などでパフォーマンスを改善している。


----

## React Server Components Your Way | TanStack Blog
[tanstack.com/blog/react-server-components](https://tanstack.com/blog/react-server-components "React Server Components Your Way | TanStack Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">RSC</span> <span class="jser-tag">TanStack</span> <span class="jser-tag">article</span></p>

TanStackにおけるReact Server Components(RSC)のアプローチについて。
RSCをデータストリームとして扱い、一方向データフローとしてクライアント側でサーバーレンダリングされたUIの取得やキャッシュを制御できる設計になっている。
サーバーがスロットを用意しクライアントが埋めるComposite Componentsという仕組みや、`createServerFn`による明示的なサーバー関数定義などの機能を提供する。


----

## The Intl API: The best browser API you&#039;re not using | Polypane
[polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/](https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/ "The Intl API: The best browser API you&#039;re not using | Polypane")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">article</span></p>

Intl APIについての解説記事。
`Intl.DateTimeFormat`/`Intl.RelativeTimeFormat`/`Intl.NumberFormat`などの日付や数値のフォーマットAPIを紹介している。
`Intl.ListFormat`/`Intl.PluralRules`/`Intl.Segmenter`/`Intl.Collator`などの使い方について


----

## Under the hood of MDN&#039;s new frontend
[developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/ "Under the hood of MDN&#039;s new frontend")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">WebComponents</span> <span class="jser-tag">architecture</span> <span class="jser-tag">article</span></p>

MDNのフロントエンドアーキテクチャの刷新についての解説記事。
旧フロントエンド(Yari)はCreate React Appベースで、eject後のwebpack設定の複雑化などの技術的負債を抱えていた。
Sassと最新CSSの混在や、`dangerouslySetInnerHTML`による静的コンテンツの埋め込みなどの課題もあった。
新アーキテクチャではLitベースのWeb Componentsを採用し、独自のServer Components実装でSPAの課題を解決している。
ビルドツールをwebpackからRspackへ移行、Declarative Shadow DOMやBaselineプロジェクトを活用したブラウザ互換性の管理についても解説されている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## yuku-toolchain/yuku: High-performance JavaScript/TypeScript compiler and toolchain in pure Zig 🦎
[github.com/yuku-toolchain/yuku](https://github.com/yuku-toolchain/yuku "yuku-toolchain/yuku: High-performance JavaScript/TypeScript compiler and toolchain in pure Zig 🦎")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Zig</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">compiler</span> <span class="jser-tag">Tools</span></p>

Zigで書かれたJavaScript/TypeScriptコンパイラおよびツールチェーン。
Test262でテストされていて、Pure Zigなのでクロスコンパイルが可能となっている。


----

## Diffs, from Pierre
[diffs.com/](https://diffs.com/ "Diffs, from Pierre")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">diff</span></p>

diffレンダリングとコード表示のライブラリ。
CSS GridとShadow DOMを活用してDOMノード数を削減しレンダリングの高速化やVirtualizationに対応している。
Stack型(統合表示)とSplit型(左右並列表示)の2つのレイアウトに対応し、Shikiベースの構文ハイライト/コメント/マージコンフリクト解決UIなどの機能を持つ。


----
