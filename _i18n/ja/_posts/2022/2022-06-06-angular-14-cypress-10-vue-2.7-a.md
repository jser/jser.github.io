---
title: "2022-06-06のJS: Angular 14、Cypress 10、Vue 2.7 α"
author: "azu"
layout: post
date : 2022-06-06T13:47:09.930Z
category: JSer
tags:
- npm
- node.js
- vite
- Vue
- Tools

---

JSer.info #595 - Angular 14がリリースされました。

- [Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog](https://blog.angular.io/angular-v14-is-now-available-391a6db736af)

プレビュー機能としてstandalone componentsの追加されています。

- [Angular - Getting started with standalone components](https://angular.io/guide/standalone-components)

また、Angular Formsの型付けの改善、エラーメッセージをproduction buildではエラーコードのみに変更しファイルサイズの削減など。
その他には、TypeScript 4.7のサポート、Angular CLIの改善などが含まれています。

---

Cypress 10がリリースされました。

- [Announcing Cypress 10 with Component Testing Beta!](https://cypress.io/blog/2022/06/01/cypress-10-release/)

Cypress 10ではCypress Appが刷新されています。
また、Component Testの仕組みが追加されています。

- [Writing Your First Component Test | Cypress Documentation](https://docs.cypress.io/guides/component-testing/writing-your-first-component-test#Component-vs-End-to-End-in-a-Nutshell)

---

Vue 2.xの最終minorリリースとなる予定の Vue.js 2.7αが公開されています。

- [vue/CHANGELOG.md at main · vuejs/vue](https://github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31)

Composition APIのフルサポート、ESMビルドに`ref`などのnamed exportを追加などが含まれています。

このVue 2.7が正式リリースされてから、18ヶ月後にVue 2.xはEOLとなる予定です。
現時点では、Vue 2.xは2023年末にEOLの予定となっています。

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Vue 2 end of life at the end of 2023 <a href="https://twitter.com/hashtag/vuejs?src=hash&amp;ref_src=twsrc%5Etfw">#vuejs</a> <a href="https://t.co/luvk1lt3U6">pic.twitter.com/luvk1lt3U6</a></p>&mdash; Filip Rakowski 🇺🇦 (@filrakowski) <a href="https://twitter.com/filrakowski/status/1532281407942365184?ref_src=twsrc%5Etfw">June 2, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


----

<h1 class="site-genre">ヘッドライン</h1>

----

## jridgewell/trace-mapping: Trace the original position through a source map
[github.com/jridgewell/trace-mapping](https://github.com/jridgewell/trace-mapping "jridgewell/trace-mapping: Trace the original position through a source map")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

source-mapパッケージと互換性のあるAPIを提供するライブラリ。
source-mapパッケージとは異なりWebAssemblyを利用せずに書かれている。


----

## Node v18.3.0 (Current) | Node.js
[nodejs.org/en/blog/release/v18.3.0/](https://nodejs.org/en/blog/release/v18.3.0/ "Node v18.3.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 18.3.0リリース。
`util`モジュールに`parseArgs`を追加、`http`モジュールに`uniqueHeaders`オプションを追加など

- [pkgjs/parseargs: Polyfill of proposal for \`util.parseArgs()\`](https://github.com/pkgjs/parseargs "pkgjs/parseargs: Polyfill of proposal for \&#x60;util.parseArgs()\&#x60;")

----

## Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog
[blog.angular.io/angular-v14-is-now-available-391a6db736af](https://blog.angular.io/angular-v14-is-now-available-391a6db736af "Angular v14 is now available!. We are excited to announce the release… | by Emma Twersky | Jun, 2022 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 14リリース。
プレビュー機能としてstandalone componentsの追加、Angular Formsの型付けの改善、エラーメッセージをproduction buildではエラーコードのみに変更。
TypeScript 4.7のサポート、Angular CLIの改善など


----

## Announcing Cypress 10 with Component Testing Beta!
[cypress.io/blog/2022/06/01/cypress-10-release/](https://cypress.io/blog/2022/06/01/cypress-10-release/ "Announcing Cypress 10 with Component Testing Beta!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Cypress 10リリース。
Cypress Appの刷新、Component Testingがベータになった。


----

## Release v3.16.0 · mishoo/UglifyJS
[github.com/mishoo/UglifyJS/releases/tag/v3.16.0](https://github.com/mishoo/UglifyJS/releases/tag/v3.16.0 "Release v3.16.0 · mishoo/UglifyJS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span></p>

UflifyJS 3.16.0リリース。
入力をES Modulesとして扱う`--module`フラグを追加など


----

## vue/CHANGELOG.md at main · vuejs/vue
[github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31](https://github.com/vuejs/vue/blob/main/CHANGELOG.md#270-alpha1-2022-05-31 "vue/CHANGELOG.md at main · vuejs/vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Vue.js 2.7αリリース。
Vue 2.xの最後のminorリリース候補となり、Vue 2.7の正式リリースから18ヶ月後の2023年末にはVue 2.xはEOLとなる予定。
Composition APIのフルサポート、ESMビルドに`ref`などのnamed exportを追加など

- [Filip Rakowski 🇺🇦 on Twitter: &amp;quot;Vue 2 end of life at the end of 2023 #vuejs https://t.co/luvk1lt3U6&amp;quot; / Twitter](https://twitter.com/filrakowski/status/1532281407942365184 "Filip Rakowski 🇺🇦 on Twitter: &amp;amp;quot;Vue 2 end of life at the end of 2023 #vuejs https://t.co/luvk1lt3U6&amp;amp;quot; / Twitter")

----

## npm security update: Attack campaign using stolen OAuth tokens | The GitHub Blog
[github.blog/2022-05-26-npm-security-update-oauth-tokens/](https://github.blog/2022-05-26-npm-security-update-oauth-tokens/ "npm security update: Attack campaign using stolen OAuth tokens | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">news</span></p>

HerokuとTravis CIからGitHub OAuth Tokenの流出に関連して、npmが管理していたプライベートリポジトリからAWSへのアクセスキーが盗まれ、npmの一部情報が漏洩した。
2015年のユーザー情報(ユーザー名/メールアドレス/パスワードハッシュ)、2021年のプライベートnpmパッケージのメタデータ、2022年の全てのプライベートパッケージの名前とバージョンが漏洩した。


----

## Release Add support for lts/-n aliases · actions/setup-node
[github.com/actions/setup-node/releases/tag/v3.3.0](https://github.com/actions/setup-node/releases/tag/v3.3.0 "Release Add support for lts/-n aliases · actions/setup-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">ReleaseNote</span></p>

GitHub ActionsでNode.js環境を設定するactions/setup-node 3.3.0リリース。
`node-version: lts/-1` のようにLTSの相対指定をサポート。
3.2.0では、`current`と`latest`のaliasをサポートしている。

- [Release Support caching dependencies and LTS aliases · actions/setup-node](https://github.com/actions/setup-node/releases/tag/v2.2.0 "Release Support caching dependencies and LTS aliases · actions/setup-node")
- [Release Add current, node, latest aliases · actions/setup-node](https://github.com/actions/setup-node/releases/tag/v3.2.0 "Release Add current, node, latest aliases · actions/setup-node")

----
<h1 class="site-genre">アーティクル</h1>

----

## Processing Arrays non-destructively: \`for-of\` vs. \`.reduce()\` vs. \`.flatMap()\`
[2ality.com/2022/05/processing-arrays-non-destructively.html](https://2ality.com/2022/05/processing-arrays-non-destructively.html "Processing Arrays non-destructively: \`for-of\` vs. \`.reduce()\` vs. \`.flatMap()\`")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Arrayのfilter/map/some/every/reduce/flatMapメソッドやfor ofなど、どれを使うべきかについて。
それぞれの機能の紹介といつ使うべきかについて


----

## JavaScript のメディアタイプと RFC 9239 | blog.jxck.io
[blog.jxck.io/entries/2022-05-31/text-javascript.html](https://blog.jxck.io/entries/2022-05-31/text-javascript.html "JavaScript のメディアタイプと RFC 9239 | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

JavaScriptのMIME Typesについて


----

## Introducing Opportunities &amp; Experiments: Taking the Guesswork out of Performance - WebPageTest Blog
[blog.webpagetest.org/posts/introducing-opportunities-and-experiments/](https://blog.webpagetest.org/posts/introducing-opportunities-and-experiments/ "Introducing Opportunities &amp; Experiments: Taking the Guesswork out of Performance - WebPageTest Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

WebPageTestにOpportunitiesとExperiments機能が追加された。
Opportunitiesはパフォーマンスやアクセシビリティを改善する項目をサジェストし実際に適用して結果がどうなるかを計測できる機能。
ExperimentsはEdgeのProxyを通して一時的にサイトを書き換えて再計測できる。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## pkg.land - find NPM alternative packages
[pkg.land/](https://pkg.land/ "pkg.land - find NPM alternative packages")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">search</span> <span class="jser-tag">webservice</span></p>

npmパッケージの代替パッケージを検索できるサービス


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Svelvet
[svelvet.io/](https://svelvet.io/ "Svelvet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">diagram</span> <span class="jser-tag">library</span></p>

フローチャートを描画するSvelte component


----

## histoire-dev/histoire: ⚡ Fast and beautiful interactive component playgrounds, powered by Vite
[github.com/histoire-dev/histoire](https://github.com/histoire-dev/histoire "histoire-dev/histoire: ⚡ Fast and beautiful interactive component playgrounds, powered by Vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">Vue</span> <span class="jser-tag">Tools</span></p>

Viteを使ったStorybook的なツール


----

## WebReflection/highlighted-code: A textarea builtin extend to automatically provide code highlights based on one of the languages available via highlight.js
[github.com/WebReflection/highlighted-code](https://github.com/WebReflection/highlighted-code "WebReflection/highlighted-code: A textarea builtin extend to automatically provide code highlights based on one of the languages available via highlight.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

textareaにシンタックスハイライトをオーバーレイできるライブラリ


----

## cyco130/vavite: Develop server-side applications with Vite
[github.com/cyco130/vavite](https://github.com/cyco130/vavite "cyco130/vavite: Develop server-side applications with Vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span></p>

Viteをサーバサイドに組み込むためのExpressなどに対応したMiddlewareやViteプラグイン。
Viteを使ってサーバサイドのコードのTranspile、Live Reload、SSRなどに対応するための仕組みをを提供する。
また、本番ビルド時には開発用のDevServerの参照を消すVite Pluginも提供している。


----
<h1 class="site-genre">書籍関係</h1>

----

## Web Browser Engineering
[browser.engineering/](https://browser.engineering/ "Web Browser Engineering")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">python</span> <span class="jser-tag">book</span></p>

Pythonでブラウザのレンダリングエンジンを作りながらWebページの仕組みについて学ぶ本。
HTMLのパース、レイアウト、CSSのパース、クリックの処理、Browser ChromeのUI実装、HTTPリクエストの処理、DOM APIの実装、CookieとSameSiteの実装。
Skiaを使ったレンダリングとブレンディング、スケジューリング、アニメーションなどについて扱う

- [Why Python? | Web Browser Engineering](https://browser.engineering/blog/why-python.html "Why Python? | Web Browser Engineering")

----

## スラスラわかるJavaScript 新版（桜庭 洋之 望月 幸太郎）｜翔泳社の本
[www.shoeisha.co.jp/book/detail/9784798173269](https://www.shoeisha.co.jp/book/detail/9784798173269 "スラスラわかるJavaScript 新版（桜庭 洋之 望月 幸太郎）｜翔泳社の本")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">bok</span></p>

2022年07月13日 発売
JavaScriptの入門書


----
