---
title: "2019-04-09のJS: ChromiumベースのMicrosoft Edge プレビュー版公開、`request`モジュールがメンテンスモードに移行の予定"
author: "azu"
layout: post
date : 2019-04-09T00:14:01.804Z
category: JSer
tags:
- Chrome
- MSEdge
- Node.js
- HTTP

---

JSer.info #430 - [2018年12月にアナウンス](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/)されていたように、Chromiumを利用したMicrosoft Edge(MSEdge)のプレビュー版が公開されました。

- [Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/ "Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog")
- [What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/)

現在はWindows 10 PC向けのみですが、今後はWindows 7、Windows 8.1、macOSなども対応していく予定とのことです。
[Microsoft Edge Insider](https://www.microsoftedgeinsider.com/en-us/download/)ではBeta、Dev、Canaryビルドを公開していくようです。

[Microsoft Edge and Chromium Open Source: Our Intent](https://github.com/MicrosoftEdge/MSEdge/blob/master/README.md)のドキュメントや[What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/)ではChromiumのどこへコントリビュートしていくかについても書かれています。
また、ウェブ標準へのコントリビュートについては[MSEdgeExplainers](https://github.com/MicrosoftEdge/MSEdgeExplainers)で公開されているドキュメントに予定が書かれていたり、HTML Modules周りで既にコミットされています。

- [\[WIP\] Introduce HTML Modules by dandclark · Pull Request #4505 · whatwg/html](https://github.com/whatwg/html/pull/4505)
- [Intent to Implement: HTML Modules - Google グループ](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/ewfRSdqcOd8/w_Fr6rJ3DQAJ)

また、リリース記事では新しいEdgeのUser Agentについても書かれていて、ウェブ互換性の観点から`Edg`(Edgeではない)の文字列を使うようです。

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.48 Safari/537.36 Edg/74.1.96.24
```

----

Node.jsのHTTPライブラリとして著名な[request](https://github.com/request/request)モジュールがメンテンスモードとなる方針がアナウンスされました。

- [Request’s Past, Present and Future · Issue #3142 · request/request](https://github.com/request/request/issues/3142)

新しい機能の受け入れや破壊的な変更の受け入れはせずに、修正リリースのみを行う方針について書かれています。
まだ、非推奨にするかや別のライブラリへのマイグレーション方法については、さきほどのIssueで話し合われている段階です。

代替ライブラリについては、次のIssueで話し合われています。

- [Alternative libraries to request · Issue #3143 · request/request](https://github.com/request/request/issues/3143)

`request`モジュールに関心がある人は読んでおくと良さそうです。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v2.6.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.6.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.6.0 "Release v2.6.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v2.6.0リリース。
core-js 2と3の両方をサポート、2.5で入った`ready()`に関するBreaking Changeをrevertなど


----

## Release 3.13.1 · nodeca/js-yaml
[github.com/nodeca/js-yaml/releases/tag/3.13.1](https://github.com/nodeca/js-yaml/releases/tag/3.13.1 "Release 3.13.1 · nodeca/js-yaml")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

js-yaml 3.13.1リリース。
`load()`で悪意のあるyamlファイルを読むと任意のコードを実行できる脆弱性の修正。

- [Arbitrary Code Execution in js-yaml | Snyk](https://snyk.io/vuln/SNYK-JS-JSYAML-174129 "Arbitrary Code Execution in js-yaml | Snyk")
- [Fix possible code execution in (already unsafe) load() by rlidwka · Pull Request #480 · nodeca/js-yaml](https://github.com/nodeca/js-yaml/pull/480 "Fix possible code execution in (already unsafe) load() by rlidwka · Pull Request #480 · nodeca/js-yaml")

----

## Request’s Past, Present and Future · Issue #3142 · request/request
[github.com/request/request/issues/3142](https://github.com/request/request/issues/3142 "Request’s Past, Present and Future · Issue #3142 · request/request")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">issue</span> <span class="jser-tag">news</span></p>

Node.jsのHTTPライブラリである`request`モジュールがメンテンスモードとなる。
新しい機能追加やBreaking Changesを入れないメンテンスモードとなる予定について書かれている。

- [Alternative libraries to request · Issue #3143 · request/request](https://github.com/request/request/issues/3143 "Alternative libraries to request · Issue #3143 · request/request")

----

## Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog
[blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/](https://blogs.windows.com/windowsexperience/2019/04/08/microsoft-edge-preview-builds-the-next-step-in-our-oss-journey/ "Microsoft Edge preview builds: The next step in our OSS journey | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">ReleaseNote</span></p>

Chromiumを使ったMicrosoft Edgeのプレビュー版がリリースされた。 Beta、Dev、Canaryビルドを用意し、今後はmacOSの対応なども行う。

- [What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2019/04/08/microsoft-edge-preview-channel-details/#veEezTt4cKDiSZ0P.97 "What to expect in the new Microsoft Edge Insider Channels - Microsoft Edge Blog")


----
<h1 class="site-genre">アーティクル</h1>

----

## アメブロ2019: こえのブログでのPWA
[developers.cyberagent.co.jp/blog/archives/20506/](https://developers.cyberagent.co.jp/blog/archives/20506/ "アメブロ2019: こえのブログでのPWA")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">PWA</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">performance</span></p>

こえのブログでのフロント周りの設計について。
Fastly CDN前提のURL構造、Cloud Speech-to-Textを使った文字起こし、vmsgを使ったクライアントでエンコードしてからのアップロード、Web Componentsの利用。
初回訪問と再訪問の最適化、performance budgetの設定など


----

## New WebKit Features in Safari 12.1 | WebKit
[webkit.org/blog/8718/new-webkit-features-in-safari-12-1/](https://webkit.org/blog/8718/new-webkit-features-in-safari-12-1/ "New WebKit Features in Safari 12.1 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 12.1のWebKit周りの変更点について。
ダークモードの対応、ITP 2.1へのアップデート、Payment Request API、WebRTCの改善、EME API/MSEの対応。
Intersection Observer、Web Share APIの対応、Web Inspectorの改善など


----

## Scroll Anchoring in Firefox 66 - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/03/scroll-anchoring-in-firefox-66/](https://hacks.mozilla.org/2019/03/scroll-anchoring-in-firefox-66/ "Scroll Anchoring in Firefox 66 - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Scroll Anchoringについて。
どのように動作するかの解説


----

## Managing Z-Index In A Component-Based Web Application — Smashing Magazine
[www.smashingmagazine.com/2019/04/z-index-component-based-web-application/](https://www.smashingmagazine.com/2019/04/z-index-component-based-web-application/ "Managing Z-Index In A Component-Based Web Application — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

コンポーネントベースにおけるz-indexの管理方法について。
Stacking Context、z-indexの管理、オーバーレイについて


----

## docker-node/BestPractices.md at master · nodejs/docker-node
[github.com/nodejs/docker-node/blob/master/docs/BestPractices.md](https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md "docker-node/BestPractices.md at master · nodejs/docker-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Docker</span> <span class="jser-tag">node.js</span> <span class="jser-tag">document</span></p>

DockerにおけるNode.jsのベストプラクティスについて書かれたドキュメント。
環境変数、Ctrl + Cのシグナルが送れない問題、yarnのアップデート、root周りの設定、`CMD`でnpm run-script経由ではなく直接実行することについてなど

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jeffijoe/typesync: Install missing TypeScript typings for dependencies in your package.json.
[github.com/jeffijoe/typesync](https://github.com/jeffijoe/typesync "jeffijoe/typesync: Install missing TypeScript typings for dependencies in your package.json.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">console</span> <span class="jser-tag">toll</span></p>

`package.json`から関連する@typesのパッケージをインストールしてくれるツール


----

## typeless-js/typeless: A complete toolkit for building scalable React apps with Typescript.
[github.com/typeless-js/typeless](https://github.com/typeless-js/typeless "typeless-js/typeless: A complete toolkit for building scalable React apps with Typescript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Reduxの典型的なケースをビルトインで持つ、React+Redux+Rxjsを前提としたステート管理ライブラリ。
React Hooksに対応し、Reactに合わせたライフサイクルアクションをもつ。


----

## codex-team/editor.js: A block-styled editor with clean JSON output
[github.com/codex-team/editor.js](https://github.com/codex-team/editor.js "codex-team/editor.js: A block-styled editor with clean JSON output")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span></p>

ブロックスタイルのエディタライブラリ。
ブロックごとの記述をJSONとして出力できる。


----

## mgechev/codelyzer: Static analysis for Angular projects.
[github.com/mgechev/codelyzer](https://github.com/mgechev/codelyzer "mgechev/codelyzer: Static analysis for Angular projects.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span></p>

TSLintを使ったAngularコンポーネント向けのLintルールセット


----

## Home | PreVue
[prevue.io/](https://prevue.io/ "Home | PreVue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">Tools</span> <span class="jser-tag">design</span></p>

Vue.jsを使ったUIプロトタイピングツール


----

## kognise/water.css: A just-add-css collection of styles to make simple websites just a little nicer
[github.com/kognise/water.css](https://github.com/kognise/water.css "kognise/water.css: A just-add-css collection of styles to make simple websites just a little nicer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

HTML要素のベーススタイルを定義したライブラリ。
要素に対するスタイルを提供するため、特別なクラスを提供していない。



----

## leebyron/react-loops: React Loops works with React Hooks as part of the React Velcro Architecture
[github.com/leebyron/react-loops](https://github.com/leebyron/react-loops "leebyron/react-loops: React Loops works with React Hooks as part of the React Velcro Architecture")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span></p>

forループするReactコンポーネントライブラリ。

