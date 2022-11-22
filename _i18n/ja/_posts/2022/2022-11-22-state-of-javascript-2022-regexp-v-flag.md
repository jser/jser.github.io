---
title: "2022-11-22のJS:  State of JavaScript 2022のアンケートを実施中、RegExp `v` flag"
author: "azu"
layout: post
date : 2022-11-22T00:42:43.228Z
category: JSer
tags:
- React
- tutorial
- CSS
- TypeScript
- browser

---

JSer.info #619 - 毎年行われているJavaScript開発者向けのアンケートである State of JavaScript 2022 が開催されています。

- [State of JavaScript 2022](https://survey.devographics.com/survey/state-of-js/2022)

言語機能やフレームワークなどについてのアンケートをとっていて、2022年12月15日まで受付けています。

過去の結果については次のページで公開されています。

- [The State of JS 2021](https://2021.stateofjs.com/en-US/)
- [State of JS 2020](https://2020.stateofjs.com/en-US/)


---

[ECMAScript proposal: RegExp flag `/v` makes character classes and character class escapes more powerful](https://2ality.com/2022/11/regexp-v-flag.html)という記事では、現在ECMAScript Proposal Stage 3の[RegExp `v` flag](https://github.com/tc39/proposal-regexp-v-flag)について解説されています。

正規表現の`v`フラグは、正規表現に集合操作と構文を追加するProposalになっています。
記事では、`v`フラグを利用した際の文字クラスとUnicode Property Escape、文字クラスの集合操作、case-insensitiveマッチの改善について解説されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## AWS AppSync GraphQL APIs Supports JavaScript Resolvers | AWS News Blog
[aws.amazon.com/jp/blogs/aws/aws-appsync-graphql-apis-supports-javascript-resolvers/](https://aws.amazon.com/jp/blogs/aws/aws-appsync-graphql-apis-supports-javascript-resolvers/ "AWS AppSync GraphQL APIs Supports JavaScript Resolvers | AWS News Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">news</span></p>

AWS AppSync GraphQL APIsのResolverとしてVTLに加えてJavaScriptが利用できるようになる。


----

## Release v1.28 · microsoft/playwright
[github.com/microsoft/playwright/releases/tag/v1.28.0](https://github.com/microsoft/playwright/releases/tag/v1.28.0 "Release v1.28 · microsoft/playwright")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">playwright</span> <span class="jser-tag">ReleaseNote</span></p>

playwright v1.28.0リリース。
VSCodeからテストコードの生成を補助するPlaywright Toolsの追加、`test.describe.configure` APIの追加など


----

## Release v7.17.0 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v7.17.0](https://github.com/pnpm/pnpm/releases/tag/v7.17.0 "Release v7.17.0 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v7.17.0リリース。
`pnpm licenses list`コマンドの追加など


----

## State of JavaScript 2022
[survey.devographics.com/survey/state-of-js/2022](https://survey.devographics.com/survey/state-of-js/2022 "State of JavaScript 2022")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Survey</span> <span class="jser-tag">news</span></p>

2022年12月15日まで、JavaScript開発者向けのアンケートであるState Of JSが実施中。


----
<h1 class="site-genre">アーティクル</h1>

----

## The magical world of Particles with React Three Fiber and Shaders - Maxime Heckel&#039;s Blog
[blog.maximeheckel.com/posts/the-magical-world-of-particles-with-react-three-fiber-and-shaders/](https://blog.maximeheckel.com/posts/the-magical-world-of-particles-with-react-three-fiber-and-shaders/ "The magical world of Particles with React Three Fiber and Shaders - Maxime Heckel&#039;s Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">WebGL</span> <span class="jser-tag">article</span> <span class="jser-tag">tutorial</span></p>

React Three Fiberを使ったパーティクルのレンダリングについてのチュートリアル

- [The Study of Shaders with React Three Fiber - Maxime Heckel&#039;s Blog](https://blog.maximeheckel.com/posts/the-study-of-shaders-with-react-three-fiber/ "The Study of Shaders with React Three Fiber - Maxime Heckel&amp;#039;s Blog")

----

## ECMAScript proposal: RegExp flag \`/v\` makes character classes and character class escapes more powerful
[2ality.com/2022/11/regexp-v-flag.html](https://2ality.com/2022/11/regexp-v-flag.html "ECMAScript proposal: RegExp flag \`/v\` makes character classes and character class escapes more powerful")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3のRegExpの`v`フラグについての解説。
文字クラスとUnicode Property Escape、文字クラスの集合操作、case-insensitiveマッチの改善について


----

## コードジャンプ可能な CSS Modules を実現する happy-css-modules の紹介 - mizdra&#039;s blog
[www.mizdra.net/entry/2022/11/14/102506](https://www.mizdra.net/entry/2022/11/14/102506 "コードジャンプ可能な CSS Modules を実現する happy-css-modules の紹介 - mizdra&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

Typed CSS Modulesとコードジャンプの問題について。
TypeScriptのDeclaration Mapを使い、型定義ファイルではなくソースコードであるCSSそのものへジャンプする実装について


----

## Manifest v3 signing available November 21 on Firefox Nightly | Mozilla Add-ons Community Blog
[blog.mozilla.org/addons/2022/11/17/manifest-v3-signing-available-november-21-on-firefox-nightly/](https://blog.mozilla.org/addons/2022/11/17/manifest-v3-signing-available-november-21-on-firefox-nightly/ "Manifest v3 signing available November 21 on Firefox Nightly | Mozilla Add-ons Community Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">Extension</span> <span class="jser-tag">article</span></p>

2022年11月21日からFirefoxの拡張機能ストアであるAMOに対してManifest V3の拡張をアップロードして署名できるようになる


----

## Automate an isolated browser instance with just a few lines of code
[blog.cloudflare.com/introducing-workers-browser-rendering-api/](https://blog.cloudflare.com/introducing-workers-browser-rendering-api/ "Automate an isolated browser instance with just a few lines of code")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">puppeteer</span> <span class="jser-tag">article</span></p>

Cloudflare WorkersからPuppeteerが利用できるRendering APIを導入予定という話。
gVisorで管理されたBrowser Renderingを行うサンドボックス内でレンダリングを行いその結果を取得できる


----

## Expiration Cap Removed From JavaScript Cookies In WebKit Browsers | Simo Ahava&#039;s blog
[www.simoahava.com/privacy/first-party-cookies-webkit-revisited/](https://www.simoahava.com/privacy/first-party-cookies-webkit-revisited/ "Expiration Cap Removed From JavaScript Cookies In WebKit Browsers | Simo Ahava&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">safari</span> <span class="jser-tag">privacy</span></p>

SafariのCookieの有効期限について。
ブラウザを利用した日で7日間未使用の場合の削除、ITPでのトラッキング分類された場合に24時間で削除、CNAME Cloakingでの7日間制限などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## メタフロントエンド開発者 プロフェッショナル認定証 | Coursera
[www.coursera.org/professional-certificates/meta-front-end-developer](https://www.coursera.org/professional-certificates/meta-front-end-developer "メタフロントエンド開発者 プロフェッショナル認定証 | Coursera")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">video</span></p>

Metaのフロントエンド開発者入門むけのcoursera講座。
HTML/CSS/JavaScriptとReact、UI/UXなどについて学ぶ講座


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Permissions-Policy Research - Google ドキュメント
[docs.google.com/document/d/14xHANU3n43PfJR\_dCpEwVCiVYv12BAfGqOICNvd79R4/edit#](https://docs.google.com/document/d/14xHANU3n43PfJR_dCpEwVCiVYv12BAfGqOICNvd79R4/edit# "Permissions-Policy Research - Google ドキュメント")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">spec</span> <span class="jser-tag">document</span></p>

Feature-PolicyとPermissions-Policyの対応や標準化についての調査ドキュメント。
MDNのドキュメントのために調査されている。

- [Intent to document: Permissions-Policy · Issue #22347 · mdn/content](https://github.com/mdn/content/issues/22347 "Intent to document: Permissions-Policy · Issue #22347 · mdn/content")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## hadmean/hadmean: Generate powerful, fully functional, ready-to-be-deployed admin apps in seconds with just \`npx hadmean\`. No Javascript, no SQL, no components, no tutorials, and finally zero maintenance. Stop building and maintaining admin apps that you can auto-generate.
[github.com/hadmean/hadmean](https://github.com/hadmean/hadmean "hadmean/hadmean: Generate powerful, fully functional, ready-to-be-deployed admin apps in seconds with just \`npx hadmean\`. No Javascript, no SQL, no components, no tutorials, and finally zero maintenance. Stop building and maintaining admin apps that you can auto-generate.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

データベースのデータをみる管理画面を作成するジェネレータアプリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScript と比較しながら学ぶ TypeScript | Techpit
[www.techpit.jp/courses/248](https://www.techpit.jp/courses/248 "JavaScript と比較しながら学ぶ TypeScript | Techpit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

JavaScriptに型を付けながらTypeScriptについて学ぶ書籍

- [\[Techpit\] JavaScriptと比較しながら学ぶTypeScriptという書籍をリリースしました！](https://zenn.dev/ababup1192/articles/6873aa4b4109f2 "\[Techpit\] JavaScriptと比較しながら学ぶTypeScriptという書籍をリリースしました！")

----
