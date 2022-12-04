---
title: "2021-04-20のJS:  Headless UI 1.0、esbuild/Snowpack/Vite/wmrの比較、debugging Web Vitals"
author: "azu"
layout: post
date : 2021-04-20T02:45:24.600Z
category: JSer
tags:
- Tools
- performance
- Chrome
- browser
- TypeScript

---

JSer.info #536 - ReactとVueに対応したスタイルなしコンポーネントライブラリであるHeadless UI 1.0がリリースされました。

- [Headless UI v1.0 – Tailwind CSS](https://blog.tailwindcss.com/headless-ui-v1)
- [tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.](https://github.com/tailwindlabs/headlessui)

Headless UIはTailwind CSSと一緒に使う目的で開発されているため、コンポーネント自体にはスタイルは含まれていません。
Headless UIにはReactとVueの実装がそれぞれあり、今回のリリースでそれぞれが1.0としてリリースされています。

----

[Comparing the New Generation of Build Tools | CSS-Tricks](https://css-tricks.com/comparing-the-new-generation-of-build-tools/)という記事では、esbuild/Snowpack/Vite/wmrのビルドツールについて比較しています。

それぞれのツールの特徴や使い方、サポートしているファイル形式、production buildなどについて比較しています。
esbuildは少しレイヤーが異なる気はしますが、それぞれのツールの特徴がまとめられいます。

----

Google検索結果のランキングにpage experienceというWeb Vitalsをベースとして指標が6月から含まれる予定です。

- [Timing for bringing page experience to Google Search](https://developers.google.com/search/blog/2020/11/timing-for-page-experience)
- [More time, tools, and details on the page experience update](https://developers.google.com/search/blog/2021/04/more-details-page-experience)

これにあわせて、Web Vitalsのデバッグ方法やツールなどが色々と公開されています。

- [Debug Web Vitals in the field](https://web.dev/debug-web-vitals-in-the-field/)
  - Web Vitalsのメトリクスのデバッグ方法
- [An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine](https://www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/)
  - Web Vitalsの全体的な解説
- [Cumulative Layout Shift Debugger (CLS) - webvitals.dev](https://webvitals.dev/cls)
  - CLSのデバッグツール
- [Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores](https://waterfaller.dev/)
  - ページロードをウォータフォール表示して、Web Vitalsのメトリクスなどをどのように改善するかを提示するツール

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Deno 1.9 Release Notes | Deno Blog
[deno.com/blog/v1.9](https://deno.com/blog/v1.9 "Deno 1.9 Release Notes | Deno Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">ReleaseNote</span></p>

Deno 1.9リリース。
HTTP/2なウェブサーバの実装、opcallの改善、Blob URLのサポート。
`--allow-env`と`--allow-run`で個別の指定ができるように、`--prompt`でインタラクティブにパーミッションの許可ができるように。
`Deno.listenTls`でALPNのサポート、tsconfig.jsonの`useDefineForClassFields`をデフォルト化など


----

## New in Chrome 90 - Chrome Developers
[developer.chrome.com/blog/new-in-chrome-90/](https://developer.chrome.com/blog/new-in-chrome-90/ "New in Chrome 90 - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 90リリース。
`overflow: clip`のサポート、AV1 Encoderサポート、Declarative Shadow DOMのサポートなど。
Feature PolicyがPermissions Policyにリネーム、アドレスバーのデフォルトプロトコルが`https`に変更など


----

## Headless UI v1.0 – Tailwind CSS
[blog.tailwindcss.com/headless-ui-v1](https://blog.tailwindcss.com/headless-ui-v1 "Headless UI v1.0 – Tailwind CSS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">lib</span></p>

Headless UI 1.0リリース。
ReactとVueのスタイルなしのUIコンポーネントの実装で、Tailwind CSSと組み合わせる目的で作られている。

- [tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.](https://github.com/tailwindlabs/headlessui "tailwindlabs/headlessui: Completely unstyled, fully accessible UI components, designed to integrate beautifully with Tailwind CSS.")

----

## Release v6.0.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v6.0.0](https://github.com/pnpm/pnpm/releases/tag/v6.0.0 "Release v6.0.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm 6.0.0リリース。
Node.js 10のサポート終了、`pre`/`post` scriptを自動で実行しないように、lockfileのフォーマットを変更、`pnpx`が自動的にパッケージをインストールはしないようになるなど。
`pnpm link`が`--global`をつけたときにglobal modulesとリンクするように、`pnpm fetch`コマンドの追加など


----

## helmet/CHANGELOG.md at main · helmetjs/helmet
[github.com/helmetjs/helmet/blob/main/CHANGELOG.md#450---2021-04-17](https://github.com/helmetjs/helmet/blob/main/CHANGELOG.md#450---2021-04-17 "helmet/CHANGELOG.md at main · helmetjs/helmet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">express</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Expressのセキュリティヘッダを扱うhelmet 4.5.0リリース。
Cross-Origin isolationを扱うCOEP、COOP、CORPヘッダに対応など

- [Making your website &amp;quot;cross-origin isolated&amp;quot; using COOP and COEP](https://web.dev/coop-coep/ "Making your website &amp;amp;quot;cross-origin isolated&amp;amp;quot; using COOP and COEP")

----

## React-pdf - Announcing react-pdf v2.0
[react-pdf.org/blog/announcing-react-pdf-v2](https://react-pdf.org/blog/announcing-react-pdf-v2 "React-pdf - Announcing react-pdf v2.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">PDF</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ReactでPDFを作成するreact-pdf v2.0リリース。
レイアウトとレンダリングの分離、SVGサポート、Hooks APIの追加など


----

## Never too late for Firefox 88 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/04/never-too-late-for-firefox-88/](https://hacks.mozilla.org/2021/04/never-too-late-for-firefox-88/ "Never too late for Firefox 88 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 88リリース。
`:user-valid`と`:user-invalid`の実装、`RegExp#indices`の実装、`AbortSignal.abort()`の実装、FTPサポートの無効化など

- [Firefox 88 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/88 "Firefox 88 for developers - Mozilla | MDN")
- [Firefox 88.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/88.0/releasenotes/ "Firefox 88.0, See All New Features, Updates and Fixes")

----
<h1 class="site-genre">アーティクル</h1>

----

## Comparing the New Generation of Build Tools | CSS-Tricks
[css-tricks.com/comparing-the-new-generation-of-build-tools/](https://css-tricks.com/comparing-the-new-generation-of-build-tools/ "Comparing the New Generation of Build Tools | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

esbuild, Snowpack, Vite, wmrを比較した記事。
それぞれのツールの特徴や使い方、サポートしているファイル、production buildなどについて比較している。


----

## Introducing CSS Grid Inspector | WebKit
[webkit.org/blog/11588/introducing-css-grid-inspector/](https://webkit.org/blog/11588/introducing-css-grid-inspector/ "Introducing CSS Grid Inspector | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Safari Technology Preview 123で導入されたCSS Grid Inspectorの紹介


----

## Real-world CSS vs. CSS-in-JS performance comparison - Tomas Pustelnik&#039;s personal website
[pustelto.com/blog/css-vs-css-in-js-perf/](https://pustelto.com/blog/css-vs-css-in-js-perf/ "Real-world CSS vs. CSS-in-JS performance comparison - Tomas Pustelnik&#039;s personal website")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Styled Componentsを使ったCSS-in-JSと
linaria を使ってCSSファイルに分離した場合のパフォーマンスを比較した記事。
サイズ、Lighthouseなどを使ったRuntimeのパフォーマンス計測


----

## HTML Inputs and Labels: A Love Story | CSS-Tricks
[css-tricks.com/html-inputs-and-labels-a-love-story/](https://css-tricks.com/html-inputs-and-labels-a-love-story/ "HTML Inputs and Labels: A Love Story | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">article</span></p>

LabelとInputについての記事。
アクセシビリティを考慮したラベルの扱い方について


----

## Debug Web Vitals in the field
[web.dev/debug-web-vitals-in-the-field/](https://web.dev/debug-web-vitals-in-the-field/ "Debug Web Vitals in the field")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Web VitalsのメトリクスをJavaScriptで取得して、実際にどの要素がスコアに影響してるのかをデバッグする方法について

- [GoogleChromeLabs/web-vitals-report: Measure and report on your Web Vitals data in Google Analytics](https://github.com/GoogleChromeLabs/web-vitals-report "GoogleChromeLabs/web-vitals-report: Measure and report on your Web Vitals data in Google Analytics")

----

## An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine
[www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/](https://www.smashingmagazine.com/2021/04/complete-guide-measure-core-web-vitals/ "An In-Depth Guide To Measuring Core Web Vitals — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Web Vitalsについての記事。
Web VitalsのLCP/FID/CLSの解説、Lighthouse/Google Search Consoleのレポート読み方、CrUXのデータの読み方や分析方法などについて。


----

## Slow and Steady: Converting Sentry’s Entire Frontend to TypeScript | Product Blog • Sentry
[blog.sentry.io/2021/04/12/slow-and-steady-converting-sentrys-entire-frontend-to-typescript](https://blog.sentry.io/2021/04/12/slow-and-steady-converting-sentrys-entire-frontend-to-typescript "Slow and Steady: Converting Sentry’s Entire Frontend to TypeScript | Product Blog • Sentry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">article</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">refacoring</span></p>

SentryのコードをベースをTypeScriptへマイグレーションした話。
戦略として教育、新しいコードをTSで書く、既存のコードをTSに変換をしていった。
徐々に変換していくこと、少しずつ複雑な型にしていくこと、TypeScriptを最新に保つことなどを教訓としてあげている。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores
[waterfaller.dev/](https://waterfaller.dev/ "Waterfaller - find and fix all the slowdowns on your web page to boost speed and core web vital scores")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

Web Vitalsの指標とリソースのロードをウォーターフォールチャートで表示し、なぜSlowdownしてるのかの解説と修正方法を提示してくれるツール。


----

## Cumulative Layout Shift Debugger (CLS) - webvitals.dev
[webvitals.dev/cls](https://webvitals.dev/cls "Cumulative Layout Shift Debugger (CLS) - webvitals.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Tools</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">webservice</span></p>

Cumulative Layout Shift(CLS)のデバッグツール


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ivanhofer/typesafe-i18n
[github.com/ivanhofer/typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n "ivanhofer/typesafe-i18n")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

依存のないi18nライブラリ。
TypeScriptを使った翻訳漏れのチェック、pluralなどのtransformerサポート、rollupやCLIを使った最適化などをサポートしている


----

## lukejacksonn/servor: Dependency free file server for single page app development
[github.com/lukejacksonn/servor](https://github.com/lukejacksonn/servor "lukejacksonn/servor: Dependency free file server for single page app development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">console</span> <span class="jser-tag">Tools</span></p>

依存のないローカルサーバライブラリ。
ファイル変更でリロード、起動時にブラウザやエディタで開く、httpsの対応のオレオレ証明生成などに対応している


----

## callstack/linaria: Zero-runtime CSS in JS library
[github.com/callstack/linaria](https://github.com/callstack/linaria "callstack/linaria: Zero-runtime CSS in JS library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span></p>

CSS-in-JSでスタイルを書いて、そのスタイルをCSSファイルに分離するライブラリとツールキット。


----
