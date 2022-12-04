---
title: "2020-08-04のJS: Firefox 79、Babel 7.11.0、Speculation in JavaScriptCore"
author: "azu"
layout: post
date : 2020-08-04T02:14:59.068Z
category: JSer
tags:
- Firefox
- Babel
- WebKit
- JavaScriptCore

---

JSer.info #499 - Firefox 79がリリースされました。

- [Firefox 79: The safe return of shared memory, new tooling, and platform updates - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/07/firefox-79/)
- [Firefox 79 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/79)

非同期処理のスタックトレースのサポート、デバッガの改善が行われています。
`target=_blank`のリンクに対して暗黙的に`rel=noopener`と同じ扱いをするようになりました。
また、`crossOriginIsolated`が有効の場合に`SharedArrayBuffer`が利用可能になっています。

詳しくは次の記事で解説されています。

- [Safely reviving shared memory - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2020/07/safely-reviving-shared-memory/)
- [Why you need "cross-origin isolated" for powerful features](https://web.dev/why-coop-coep/)


JavaScriptではStage 4の`Promise.any`、Logical assignment、WeakRefのサポートしています。
WebAssemblyのBulk memory operations、Reference types、Threads のサポートなども含まれています。

----

Babel 7.11.0がリリースされました。

- [7.11.0 Released: ECMAScript 2021 support in preset-env, TypeScript 4.0 support, printing config and the future of `babel-eslint` · Babel](https://babeljs.io/blog/2020/07/30/7.11.0)

`@babel/preset-env`にStage 4となったProposalのLogical Assignment、Numeric Separatorのサポートが追加されています。
[TypeScript 4.0で追加される構文](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/)のサポートが追加されています。
また、Stage 1の[Decimal Literal](https://github.com/tc39/proposal-decimal)の構文パースをサポート、`BABEL_SHOW_CONFIG_FOR`での設定出力をサポートしています。

- [feat: add SHOW_CONFIG docs by JLHwung · Pull Request #2302 · babel/website](https://github.com/babel/website/pull/2302)

また[`babel-eslint`](https://github.com/babel/babel-eslint)がmonorepo内の[`@babel/eslint-parser`](https://github.com/babel/babel/tree/main/eslint/babel-eslint-parser)に移動しています。

----

[Speculation in JavaScriptCore | WebKit](https://webkit.org/blog/10308/speculation-in-javascriptcore/)という記事ではWebKitのJavaScriptCoreの投機的コンパイラでのJavaScriptの最適化について解説されています。

投機処理、JITコンパイラなどについてかなり詳しく解説されているので興味がある人は読んでみると良さそうです。
とても長い記事/スライドなので、一番下のRelated WorkとConclusionから読んでみるとどういう話をしているかがつかみやすいかもしれません。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 79: The safe return of shared memory, new tooling, and platform updates - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/07/firefox-79/](https://hacks.mozilla.org/2020/07/firefox-79/ "Firefox 79: The safe return of shared memory, new tooling, and platform updates - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">relre</span></p>

Firefox 79リリース。
非同期処理のスタックトレースのサポート、デバッガの改善。
`target=_blank`のリンクに対して暗黙的に`rel=noopener`を同じ処理をするように、`crossOriginIsolated`が有効の場合に`SharedArrayBuffer`が利用可能に。
Stage 4の`Promise.any`、Logical assignment、WeakRefのサポート。
WebAssemblyのBulk memory operations、Reference types、Threads のサポートなど

- [Firefox 79.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/79.0/releasenotes/)
- [Firefox 79 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/79)

----

## Safely reviving shared memory - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2020/07/safely-reviving-shared-memory/](https://hacks.mozilla.org/2020/07/safely-reviving-shared-memory/ "Safely reviving shared memory - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">JavaScript</span></p>

FirefoxでSpectreへの対応として無効になっていた`SharedArrayBuffer`が再度利用できるようになる話。
プロセス分離、`Cross-Origin-Opener-Policy`と`Cross-Origin-Embedder-Policy`でCross-origin isolationについて。

- [Why you need &quot;cross-origin isolated&quot; for powerful features](https://web.dev/why-coop-coep/ "Why you need &amp;quot;cross-origin isolated&amp;quot; for powerful features")

----

## 7.11.0 Released: ECMAScript 2021 support in preset-env, TypeScript 4.0 support, printing config and the future of \`babel-eslint\` · Babel
[babeljs.io/blog/2020/07/30/7.11.0](https://babeljs.io/blog/2020/07/30/7.11.0 "7.11.0 Released: ECMAScript 2021 support in preset-env, TypeScript 4.0 support, printing config and the future of \`babel-eslint\` · Babel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">babel</span> <span class="jser-tag">ReleaseNote</span></p>

Babel 7.11.0リリース。
`@babel/preset-env`がStage 4となったProposalのLogical Assignment、Numeric Separatorのサポート、TypeScript 4.0で追加される構文のサポート。
Stage 1のDecimal Literalをサポート、`BABEL_SHOW_CONFIG_FOR`での設定出力をサポート、`babel-eslint`が`@babel/eslint-parser`に移動など


----

## Snowpack 2.7
[www.snowpack.dev/posts/2020-07-30-snowpack-2-7-release/](https://www.snowpack.dev/posts/2020-07-30-snowpack-2-7-release/ "Snowpack 2.7")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bundler</span> <span class="jser-tag">ReleaseNote</span></p>

フロントエンドビルドツールのSnowpack 2.7リリース。
Plugin APIの変更、`snowpack.config.json`の書式の変更など。
どちらもv2の間は後方互換性があるが、新しい形式に移行を推奨している。


----

## Release v3.0.0 · ykzts/node-xmlhttprequest
[github.com/ykzts/node-xmlhttprequest/releases/tag/v3.0.0](https://github.com/ykzts/node-xmlhttprequest/releases/tag/v3.0.0 "Release v3.0.0 · ykzts/node-xmlhttprequest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">XHR</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsでのXMLHttpRequestの実装ライブラリであるnode-xmlhttprequest 3.0.0リリース


----

## Speculation in JavaScriptCore | WebKit
[webkit.org/blog/10308/speculation-in-javascriptcore/](https://webkit.org/blog/10308/speculation-in-javascriptcore/ "Speculation in JavaScriptCore | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">JIT</span> <span class="jser-tag">webkit</span></p>

Filip PizloによるJavaScriptCoreの投機的コンパイル、JITについて詳しい解説。
JavaScriptCoreにおける4層のコンパイル処理の解説、投機的コンパイル、再コンパイル、プロファイリング、インラインキャッシュなど。
投機的コンパイルは動的に型付けの言語においてどんな型を持っているかを推測して最適化する手法。その推測には、複数の実行層を使ったプロファイリングなどを基にして最適化を行う話


----

## Blog - Next.js 9.5 | Next.js
[nextjs.org/blog/next-9-5](https://nextjs.org/blog/next-9-5 "Blog - Next.js 9.5 | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Next.js 9.5リリース。
`revalidate`、`basePath`、`trailingSlash`のオプションの追加、`rewrites`と`redirects`の設定が可能になった。
Page Bundleのビルドキャッシュの有効化、ProductionでReactのプロファイルができるようになるなど


----

## Ink 3 - Vadim's Blog
[vadimdemedes.com/posts/ink-3](https://vadimdemedes.com/posts/ink-3 "Ink 3 - Vadim's Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">console</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

Reactを使ったコンソールUIライブラリであるInk 3リリース。
パフォーマンスの改善、`<Color>`は`<Text>`コンポーネントにマージ、`useInput`や`useFocus`などのHookの提供など

- [Release v3.0.0 · vadimdemedes/ink](https://github.com/vadimdemedes/ink/releases/tag/v3.0.0 "Release v3.0.0 · vadimdemedes/ink")

----
<h1 class="site-genre">アーティクル</h1>

----

## Performance monitoring with Lighthouse CI
[web.dev/lighthouse-ci/](https://web.dev/lighthouse-ci/ "Performance monitoring with Lighthouse CI")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

Lighthouse CIについての記事。
設定方法、CIでテストとして使う方法、GitHub Actionの連携について


----

## A new default Referrer-Policy for Chrome: strict-origin-when-cross-origin
[developers.google.com/web/updates/2020/07/referrer-policy-new-chrome-default](https://developers.google.com/web/updates/2020/07/referrer-policy-new-chrome-default "A new default Referrer-Policy for Chrome: strict-origin-when-cross-origin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

ChromeのReferrer-Policyのデフォルト値が`strict-origin-when-cross-origin`に変更されることによる影響について。
`Origin`や`Sec-Fetch-Site`での代替えなどについて

- [Referer and Referrer-Policy best practices](https://web.dev/referrer-best-practices/ "Referer and Referrer-Policy best practices")

----

## 【翻訳】Date and Times in JavaScript - from scratch
[yosuke-furukawa.hatenablog.com/entry/2020/07/28/102821](https://yosuke-furukawa.hatenablog.com/entry/2020/07/28/102821 "【翻訳】Date and Times in JavaScript - from scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">translate</span></p>

Dateを置き換えるProposalであるTemporalについての翻訳


----

## Different versions of your site can be running at the same time - JakeArchibald.com
[jakearchibald.com/2020/multiple-versions-same-time/](https://jakearchibald.com/2020/multiple-versions-same-time/ "Different versions of your site can be running at the same time - JakeArchibald.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

デプロイ中に複数のバージョンが同じサイトで動く問題についてどのように対処するかという話。
再ビルドによるchunkファイルの404、Storageスキーマの変更、APIレスポンスの変更に対してどのような対策を取るかについて書かれている


----

## Webブラウザ上で純粋なHTTPだけで単方向リアルタイム通信を可能にするHTTPのストリーミングアップロードが遂にやってくる - nwtgck / Ryo Ota
[scrapbox.io/nwtgck/Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E4%B8%8A%E3%81%A7%E7%B4%94%E7%B2%8B%E3%81%AAHTTP%E3%81%A0%E3%81%91%E3%81%A7%E5%8D%98%E6%96%B9%E5%90%91%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E9%80%9A%E4%BF%A1%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%99%E3%82%8BHTTP%E3%81%AE%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%8C%E9%81%82%E3%81%AB%E3%82%84%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8B](https://scrapbox.io/nwtgck/Web%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E4%B8%8A%E3%81%A7%E7%B4%94%E7%B2%8B%E3%81%AAHTTP%E3%81%A0%E3%81%91%E3%81%A7%E5%8D%98%E6%96%B9%E5%90%91%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E9%80%9A%E4%BF%A1%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%99%E3%82%8BHTTP%E3%81%AE%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%8C%E9%81%82%E3%81%AB%E3%82%84%E3%81%A3%E3%81%A6%E3%81%8F%E3%82%8B "Webブラウザ上で純粋なHTTPだけで単方向リアルタイム通信を可能にするHTTPのストリーミングアップロードが遂にやってくる - nwtgck / Ryo Ota")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

Chrome 85βで実装されているFetch upload streamingについての記事


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## lamplightdev/aeon: A lightweight date picker built with web components that can be used anywhere
[github.com/lamplightdev/aeon](https://github.com/lamplightdev/aeon "lamplightdev/aeon: A lightweight date picker built with web components that can be used anywhere")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span></p>

Date PickerのWeb Componentsライブラリ


----

## apoorv-mishra/moment-guess: A utility package for guessing date's format
[github.com/apoorv-mishra/moment-guess](https://github.com/apoorv-mishra/moment-guess "apoorv-mishra/moment-guess: A utility package for guessing date's format")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

多種多様な日付文字列をパースして、その日付にマッチするフォーマットを返すツール


----
