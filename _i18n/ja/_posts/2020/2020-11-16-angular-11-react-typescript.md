---
title: "2020-11-16のJS: Angular 11、Reactアプリの最適化、TypeScriptを採用して学んだこと"
author: "azu"
layout: post
date : 2020-11-16T00:28:55.656Z
category: JSer
tags:
- React
- Angular
- ESLint
- performance
- ECMAScript

---

JSer.info #512 -　Angular 11がリリースされました。

- [Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog](https://blog.angular.io/version-11-of-angular-now-available-74721b7952f7)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#1100-2020-11-11)

Angular 11ではフォントの自動インライン化の対応、Component Test Harnessesがすべてのコンポーネントに対応、Language Serviceの対応改善、HMRをCLIの引数で有効化できるようになっています。
その他には、webpack5の実験的サポート、Angular CLIのデフォルトLinterの今後について書かれています。

現在のAngularではTSLintを使ったLintが実装されていますが、[TSLintは非推奨となりESLintへの移行](https://medium.com/palantir/tslint-in-2019-1a144c2317a9)が進められています。
Angularでも同様のTSLintからESLintの移行が進められていましたが、すでにコミュニティベースで進んでいた[Angular ESLint](https://github.com/angular-eslint/angular-eslint)に移行していく方針についても書かれています。

詳しくは次の記事も参照してください。

- [Angular: ESLintサポートの現状 2020 Autumn | <output type=text>](https://blog.lacolaco.net/2020/11/angular-state-of-linting-2020/)


---

[Optimize React Apps PageSpeed Insights Score - thetuteur](https://thetuteur.com/optimize-react-apps-pagespeed-insights-score/)という記事では、Reactで書かれたアプリケーションのパフォーマンス改善ついて書かれています。

未使用のJavaScriptを削除、コンポーネントのLazy Load、TTFBを短縮するためにNode.jsでレスポンスのIn-Memoryでキャッシュする方法について。

[`react-lazy-load-image-component`](https://github.com/Aljullu/react-lazy-load-image-component#readme)を使って画像の遅延ロード、[`react-lazy-hydration`](https://github.com/hadeeb/react-lazy-hydration)を使って初期ロードでのメインスレッド処理を減らす方法などについて書かれています。
また、CSSの非同期ロードや[`critical`](https://github.com/addyosmani/critical)を使ってUAごとに対してクリティカルパスCSSの生成などについても書かれています。

----

[10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg](https://www.techatbloomberg.com/blog/10-insights-adopting-typescript-at-scale/)という記事では、TypeScriptを採用して学んだことについて色々と書かれています。

TypeScriptという言語、tsconfigの設定、型定義の扱い方などについて次のような判断軸で色々と書かれています。

- Scalability
- Ecosystem Coherence
- Standards Alignment

この記事から参照されている`type`と`interface`の違いやコンパイルパフォーマンスについての記事も興味深いです。

- [TypeScript: Prefer Interfaces — @ncjamieson](https://ncjamieson.com/prefer-interfaces/)
- [Performance · microsoft/TypeScript Wiki](https://github.com/microsoft/TypeScript/wiki/Performance)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v15.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v15.2.0/](https://nodejs.org/en/blog/release/v15.2.0/ "Node v15.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v15.2.0リリース。
`events`にイベント名を指定してリスナーを取得する`getEventListeners`の追加、`fs`の`writeFile`/`readFile`がAbortSignal対応など


----

## Bootstrap 5 Alpha 3 | Bootstrap Blog
[blog.getbootstrap.com/2020/11/11/bootstrap-5-alpha-3/](https://blog.getbootstrap.com/2020/11/11/bootstrap-5-alpha-3/ "Bootstrap 5 Alpha 3 | Bootstrap Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Bootstrap 5 Alpha 3リリース。
`.card`ベースのアコーディオンの代わりとなる`.accordion`の追加、`.btn-block`の削除、Utilitiesクラスの追加など


----

## Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog
[blog.angular.io/version-11-of-angular-now-available-74721b7952f7](https://blog.angular.io/version-11-of-angular-now-available-74721b7952f7 "Version 11 of Angular Now Available | by Mark Techson | Nov, 2020 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 11リリース。
フォントの自動インライン化の対応、Component Test Harnessesがすべてのコンポーネントに対応、Language Serviceの対応改善、HMRをCLIの引数で有効化できるように。
その他には、webpack5の実験的サポートなど

- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/blob/master/CHANGELOG.md#1100-2020-11-11 "angular/CHANGELOG.md at master · angular/angular")

----

## Release v0.22.0 · ryansolid/solid
[github.com/ryansolid/solid/releases/tag/v0.22.0](https://github.com/ryansolid/solid/releases/tag/v0.22.0 "Release v0.22.0 · ryansolid/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

UI作成ライブラリのsolid v0.22.0リリース。
`splid-js/dom`を非推奨化し、`solid-js/web`を代わりに利用。
`dev`オプションのサポート、CDNのJSだけで動かせるように`solid-js/html`などを同梱、`renderToWebStream`や`createMutable`の追加など


----

## Lunuy/iterable-weak: Iterable WeakSet / WeakMap using ES2021 WeakRef
[github.com/Lunuy/iterable-weak](https://github.com/Lunuy/iterable-weak "Lunuy/iterable-weak: Iterable WeakSet / WeakMap using ES2021 WeakRef")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ECMAScript</span></p>

WeakRefを使ったIterableなWeakMap/WeakSetの実装ライブラリ。
Iterateできるように要素を参照するが、WeakRefのFinalizationRegistryを使って参照を解放するようになっている


----
<h1 class="site-genre">アーティクル</h1>

----

## What's New In DevTools (Chrome 88)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/11/devtools](https://developers.google.com/web/updates/2020/11/devtools "What's New In DevTools (Chrome 88)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 88の開発者ツールの変更点について。
CSS angleのビジュアライズ、AVIFがサポートされていない状態をエミュレートできるように、storage quota sizeのエミュレートに対応。
PerformanceパネルにWeb Vitalsレーンを追加、ApplicationパネルにCross-Origin Isolatedの状態を表示、network initiatorのコピーに対応。
実験的な機能としてCSS Flexboxのデバッグ機能、ショートカットカスタマイズを追加など


----

## Optimize React Apps PageSpeed Insights Score - thetuteur
[thetuteur.com/optimize-react-apps-pagespeed-insights-score/](https://thetuteur.com/optimize-react-apps-pagespeed-insights-score/ "Optimize React Apps PageSpeed Insights Score - thetuteur")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Reactアプリのパフォーマンス改善。
未使用のJavaScriptを削除、コンポーネントのLazy Load、TTFBを短縮するためにレスポンスのキャッシュ。
`react-lazy-load-image-component`を使って画像の遅延ロード、`react-lazy-hydration`を使い初期ロードでのCPU処理を減らす方法。
また、CSSの非同期ロード、`critical`を使ってUAごとに対してクリティカルパスCSSの生成などについて


----

## TypeScript: Prefer Interfaces — @ncjamieson
[ncjamieson.com/prefer-interfaces/](https://ncjamieson.com/prefer-interfaces/ "TypeScript: Prefer Interfaces — @ncjamieson")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの`type`と`interface`の違いについて。
`interface`は名前で参照されるのに対して、`type`で定義した型はインライン化されることがある。そのため`type`を使った場合に`d.ts`が肥大化する問題について

- [10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg](https://www.techatbloomberg.com/blog/10-insights-adopting-typescript-at-scale/ "10 Insights from Adopting TypeScript at Scale | Tech At Bloomberg")

----

## Performance · microsoft/TypeScript Wiki
[github.com/microsoft/TypeScript/wiki/Performance](https://github.com/microsoft/TypeScript/wiki/Performance "Performance · microsoft/TypeScript Wiki")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

TypeScriptのコンパイルパフォーマンスについてまとめられているページ。
`type`と`interface`、Base TypeとUnion Type、Project Reference、tsconfig.jsonの設定による最適化について


----

## Angular: ESLintサポートの現状 2020 Autumn | <output type=text>
[blog.lacolaco.net/2020/11/angular-state-of-linting-2020/](https://blog.lacolaco.net/2020/11/angular-state-of-linting-2020/ "Angular: ESLintサポートの現状 2020 Autumn | <output type=text>")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

AgularにおけるTSLint/ESLintでのLintの今後について。
TSLintはAngular 12で非推奨となる予定で、ESLintへの対応はコミュニティベースで進んでいるという話

- [angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular](https://github.com/angular-eslint/angular-eslint "angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular")

----

## Official Google Webmaster Central Blog: Timing for bringing page experience to Google Search
[webmasters.googleblog.com/2020/11/timing-for-page-experience.html](https://webmasters.googleblog.com/2020/11/timing-for-page-experience.html "Official Google Webmaster Central Blog: Timing for bringing page experience to Google Search")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">SEO</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">search</span></p>

2021年5月からCore Web Vitals(LCP、FID、CLS)のスコアがGoogle検索結果のシグナルに使われる。
ウェブパフォーマンスが検索結果のランキングへ影響を与えるようになる


----

## microsoft/Web-Dev-For-Beginners: 24 Lessons, 12 Weeks, Get Started as a Web Developer
[github.com/microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners "microsoft/Web-Dev-For-Beginners: 24 Lessons, 12 Weeks, Get Started as a Web Developer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

ウェブ開発のチュートリアル集、レッスン。HTML/CSS/JSについてやアプリ開発についての学習コンテンツ


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Next.js Conf 2020 - YouTube
[www.youtube.com/playlist?list&#x3D;PLBnKlKpPeagnT2Cmv4giCbosfrbKnuYTD](https://www.youtube.com/playlist?list=PLBnKlKpPeagnT2Cmv4giCbosfrbKnuYTD "Next.js Conf 2020 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

Next.js Conf 2020の動画一覧


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## ESM
[esm.sh/](https://esm.sh/ "ESM")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">deno</span> <span class="jser-tag">cdn</span> <span class="jser-tag">library</span></p>

esbuildで依存を含めてbundleしたパッケージを配布するnpm CDNサービス。
npmパッケージをdenoからES Modulesとして読み込めるようにpolyfillの仕組みも用意されている


----

## open-source-labs/Recoilize: Recoil developer tool
[github.com/open-source-labs/Recoilize](https://github.com/open-source-labs/Recoilize "open-source-labs/Recoilize: Recoil developer tool")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">debug</span> <span class="jser-tag">Tools</span> <span class="jser-tag">React</span></p>

recoilのデバッグツール


----

## acot-a11y/acot: More accessible web, all over the world.
[github.com/acot-a11y/acot](https://github.com/acot-a11y/acot "acot-a11y/acot: More accessible web, all over the world.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">Tools</span></p>

ESLintライクなプラグインシステムをもったAccessibilityテストフレームワーク。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## trivago/prettier-plugin-sort-imports: A prettier plugin to sort imports in typescript and javascript files by the provided RegEx order.
[github.com/trivago/prettier-plugin-sort-imports](https://github.com/trivago/prettier-plugin-sort-imports "trivago/prettier-plugin-sort-imports: A prettier plugin to sort imports in typescript and javascript files by the provided RegEx order.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">plugin</span></p>

import文の順番をソートするprettier plugin


----

## vinissimus/next-translate: i18n tool for Next.js 10 🌍 - Load page translations and use them in an easy way!
[github.com/vinissimus/next-translate](https://github.com/vinissimus/next-translate "vinissimus/next-translate: i18n tool for Next.js 10 🌍 - Load page translations and use them in an easy way!")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Next.js向けのi18nツール


----

## angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular
[github.com/angular-eslint/angular-eslint](https://github.com/angular-eslint/angular-eslint "angular-eslint/angular-eslint: Monorepo for all the tooling related to using ESLint with Angular")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ESLint</span></p>

Angular向けのESLintプラグインセット。
Codelyzer/TSLintからのマイグレーションを目的にしている


----

## felixfbecker/dom-to-svg: Library to convert a given HTML DOM node into an accessible SVG "screenshot".
[github.com/felixfbecker/dom-to-svg](https://github.com/felixfbecker/dom-to-svg "felixfbecker/dom-to-svg: Library to convert a given HTML DOM node into an accessible SVG \"screenshot\".")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">SVG</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

`<foreignObject>`を使わずに、DOMからSVGを作成するライブラリ。
DOM上のWAI-ARIAやリンクなども維持した状態のSVGを作成する


----

## davnicwil/react-frontload: Async data loading for React components, on client & server
[github.com/davnicwil/react-frontload](https://github.com/davnicwil/react-frontload "davnicwil/react-frontload: Async data loading for React components, on client & server")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">server</span></p>

React向けのData Loaderライブラリ。
コンポーネントでAPIを叩いてデータの取得、取得中の表示を扱える。クライアントとサーバでそれぞれ対応するAPIを用意してhydrationも扱える


----

## alephjs/aleph.js: The React Framework in Deno.
[github.com/alephjs/aleph.js](https://github.com/alephjs/aleph.js "alephjs/aleph.js: The React Framework in Deno.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

Deno向けのReactを使ったNext.jsライクなフレームワーク


----
<h1 class="site-genre">書籍関係</h1>

----

## JavaScriptモダンプログラミング完全ガイド \[堅牢なコードを効率的に開発できる! \] (impress top gearシリーズ) | Cay S. Horstmann, 吉川 邦夫 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4295010561/](https://www.amazon.co.jp/dp/4295010561/ "JavaScriptモダンプログラミング完全ガイド \[堅牢なコードを効率的に開発できる! \] (impress top gearシリーズ) | Cay S. Horstmann, 吉川 邦夫 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

2020年12月21日発売
Modern JavaScript for the Impatientの翻訳本

- [Amazon | Modern JavaScript for the Impatient (English Edition) \[Kindle edition\] by Horstmann, Cay S. | Languages & Tools | Kindleストア](https://www.amazon.co.jp/dp/B08F5HFWBH/ "Amazon | Modern JavaScript for the Impatient (English Edition) \[Kindle edition\] by Horstmann, Cay S. | Languages &amp; Tools | Kindleストア")

----
