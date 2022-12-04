---
title: "2020-12-22のJS:  lighthouse 7.0.0、React Server Components、Micro Frontends Architecture Patterns"
author: "azu"
layout: post
date : 2020-12-22T05:12:45.397Z
category: JSer
tags:
- Tools
- performance
- webservice
- Chrome
- Java

---

JSer.info #519 - Lighthouse 7.0.0がリリースされました。

- [Release v7.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v7.0.0)

Node.js 10のサポート終了、PWAカテゴリの変更、アクセシビリティのテストに使う`axe-core`のアップデート、nightlyを`lighthouse@next`としてインストールできるようになるといった変更が含まれています。
また、スクリーンショットがフルページとなりレポートのファイルサイズが増加しています。

---

ReactからReact Server Componentsと呼ばれる実験的な実装とRFCが公開されています。

- [Introducing Zero-Bundle-Size React Server Components – React Blog](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html)
- [RFC: React Server Components by josephsavona · Pull Request #188 · reactjs/rfcs](https://github.com/reactjs/rfcs/pull/188)

React Server Componentsは、サーバサイドでReact Componentをレンダリングする仕組みですが、レンダリング結果はHTMLではなくJSONライクなデータ(SlotとコンポーネントのJSON表現を組み合わせた形式)です。

リクエストごとにサーバコンポーネントをレンダリングした結果をJSON(クライアント描画するコンポーネントを含む)のレスポンスとして返し、クライアントではそのレスポンス結果を使いレンダリングできる仕組みとなっています。
大まかにいえば、コンポーネントレベルでのSSRとHydrateを行える仕組みです。

サーバサイドでコンポーネントをレンダリングすることで、サーバでのレンダリング結果のみを扱うクライアントでは不要なライブラリを含めずに扱えます。
そのため、クライアントに必要なbundleサイズを減らせるのが主な目的となっています。
Facebookのproductionでテストした結果、bundleサイズが最大30%削減できているそうです。

詳しくは、次の動画とデモアプリで解説されています。

- [Data Fetching with React Server Components - YouTube](https://www.youtube.com/watch?v=TQQPAU21ZUw&feature=emb_title)
- [reactjs/server-components-demo: Demo app of React Server Components.](https://github.com/reactjs/server-components-demo)

現在はまだRFCが出たばかりの実験的な段階であるため、来年にもっと詳細を決めていくようです。

---

[Micro Frontends Architecture Patterns](https://zenn.dev/okmttdhr/books/8c977618755cb68ad2c0)という電子書籍では、 フロントエンドで見かけるアーキテクチャについて色々とまとめられています。
まだ決まりきったパターンがないMicro Frontendsについても色々なパターンについて紹介されています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v7.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v7.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v7.0.0 "Release v7.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 7.0.0リリース。
Node.js 10のサポート終了。
PWAカテゴリの変更、アクセシビリティのテストに使う`axe-core`のアップデート、nightlyを`lighthouse@next`としてインストールできるようになる。
また、スクリーンショットがフルページとなりレポートのファイルサイズが増加するなど


----

## Release v4.0.0 · less/less.js
[github.com/less/less.js/releases/tag/v4.0.0](https://github.com/less/less.js/releases/tag/v4.0.0 "Release v4.0.0 · less/less.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">ReleaseNote</span></p>

Less 4.0.0リリース。
破壊的な変更としてmixinの呼び出し方のチェックをより厳密に変更、`math`オプションの初期値を`parens-division`に変更など。
`min()`/`max()`のサポート改善、`isdefined()`の追加など


----

## Announcing Stimulus 2.0 - Announcements - Stimulus Discourse
[discourse.stimulusjs.org/t/announcing-stimulus-2-0/1482](https://discourse.stimulusjs.org/t/announcing-stimulus-2-0/1482 "Announcing Stimulus 2.0 - Announcements - Stimulus Discourse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">rails</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Basecampで使われているStimulus 2.0リリース。
Controllerで`values`と`classes`プロパティを追加、EventListnerの`once`と`passive`のサポートなど。
`data`属性に`identifier`を含めて使うように変更、`input`要素を`change`から`input`イベントで監視するように変更など

- [Release v2.0.0 · stimulusjs/stimulus](https://github.com/stimulusjs/stimulus/releases/tag/v2.0.0 "Release v2.0.0 · stimulusjs/stimulus")

----

## Release v6.0.0 · fb55/htmlparser2
[github.com/fb55/htmlparser2/releases/tag/v6.0.0](https://github.com/fb55/htmlparser2/releases/tag/v6.0.0 "Release v6.0.0 · fb55/htmlparser2")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

htmlparser2 6.0.0リリース


----

## Release v0.13.0 · developit/microbundle
[github.com/developit/microbundle/releases/tag/v0.13.0](https://github.com/developit/microbundle/releases/tag/v0.13.0 "Release v0.13.0 · developit/microbundle")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">Tools</span></p>

ライブラリを配布用にbundleするmicrobundle 0.13.0リリース。
`--css`フラグを追加し、CSSをデフォルトでは外部ファイル(`external`)として出力し、`inline`でインライン化できるように。


----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing Zero-Bundle-Size React Server Components – React Blog
[reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html](https://reactjs.org/blog/2020/12/21/data-fetching-with-react-server-components.html "Introducing Zero-Bundle-Size React Server Components – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Reactで試験的に実装されたReact Server Componentsについて。
リクエストごとにサーバコンポーネントをレンダリングした結果をJSONライクなデータ(SlotとコンポーネントのJSON表現を組み合わせた形式)として返し、クライアントではレンダリング結果を使いレンダリングできる仕組み。
サーバサイドでコンポーネントをレンダリングすることで、レンダリング結果のみを扱うクライアントでは不要なライブラリを含めずに扱えるためサイズを減らせる。
コンポーネントレベルでのSSRとHydrateを行える仕組み。

- [RFC: React Server Components by josephsavona · Pull Request #188 · reactjs/rfcs](https://github.com/reactjs/rfcs/pull/188 "RFC: React Server Components by josephsavona · Pull Request #188 · reactjs/rfcs")
- [Data Fetching with React Server Components - YouTube](https://www.youtube.com/watch?v=TQQPAU21ZUw&feature=emb_title "Data Fetching with React Server Components - YouTube")

----

## Conditional JavaScript - JavaScript - Dev Tips
[umaar.com/dev-tips/242-considerate-javascript/](https://umaar.com/dev-tips/242-considerate-javascript/ "Conditional JavaScript - JavaScript - Dev Tips")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

選択的にモジュールをダウンロードする際に利用できるウェブAPIとブラウザのサポートについて。
メモリ、CPU数、バッテリー、ストレージの空き容量、ネットワーク、saveDataなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Moiva.io - Measure and compare JavaScript libraries
[moiva.io/](https://moiva.io/ "Moiva.io - Measure and compare JavaScript libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

npmパッケージの同士を比較できるツール。
NPMダウンロード数、Bundlephobiaでのサイズ、ThoughWorks、Google　Trends、GitHubのStar/Pulseなどを並べて見れるツール


----

## Cloudflare Pages
[pages.cloudflare.com/](https://pages.cloudflare.com/ "Cloudflare Pages")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">webservice</span></p>

Cloudflareの静的サイトホスティングサービス。
NetlifyやVercelのようにコミット/PRごとのレプビューURLの生成、Cloudflare Workersを使ったFaaSの仕組みを持っている

- [Introducing Cloudflare Pages: the best way to build JAMstack websites](https://blog.cloudflare.com/cloudflare-pages/ "Introducing Cloudflare Pages: the best way to build JAMstack websites")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## cincheo/jsweet: A Java to JavaScript transpiler.
[github.com/cincheo/jsweet](https://github.com/cincheo/jsweet "cincheo/jsweet: A Java to JavaScript transpiler.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Java</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

JavaのコードからTypeScript/JavaScriptのコードに変換するTranspiler


----

## f/honst: Fixes your dataset according to your rules.
[github.com/f/honst](https://github.com/f/honst "f/honst: Fixes your dataset according to your rules.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

オブジェクトの配列に対してルールを元にデータを編集するライブラリ


----

## Agamnentzar/ag-psd: Javascript library for reading and writing PSD files
[github.com/Agamnentzar/ag-psd](https://github.com/Agamnentzar/ag-psd "Agamnentzar/ag-psd: Javascript library for reading and writing PSD files")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

PSDファイルの読み書きをするライブラリ


----

## asos-craigmorten/opine: Fast, minimalist web framework for Deno ported from ExpressJS.
[github.com/asos-craigmorten/opine](https://github.com/asos-craigmorten/opine "asos-craigmorten/opine: Fast, minimalist web framework for Deno ported from ExpressJS.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">deno</span> <span class="jser-tag">library</span> <span class="jser-tag">express</span></p>

expressをDeno向けのポートしたウェブサーバライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Micro Frontends Architecture Patterns
[zenn.dev/okmttdhr/books/8c977618755cb68ad2c0](https://zenn.dev/okmttdhr/books/8c977618755cb68ad2c0 "Micro Frontends Architecture Patterns")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MicroFrontend</span> <span class="jser-tag">architecture</span> <span class="jser-tag">book</span></p>

Micro Frontendsを始めとしたアーキテクチャパターンについての電子書籍


----
