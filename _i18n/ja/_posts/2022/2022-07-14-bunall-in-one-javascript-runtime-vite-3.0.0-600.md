---
title: "2022-07-14のJS: Bun(all-in-one JavaScript runtime)、Vite 3.0.0、600回目の更新"
author: "azu"
layout: post
date : 2022-07-13T15:00:00.011Z
category: JSer
tags:
- Tools
- node.js
- CSS
- TypeScript
- HTML

---

JSer.info #600 - [Bun](https://bun.sh/)というZig言語とJavaScriptCore(WebKitのJavaScriptエンジン)を使って書かれたJavaScript Runtimeが公開されました。

- [oven-sh/bun: Incredibly fast JavaScript runtime, bundler, transpiler and package manager – all in one.](https://github.com/oven-sh/bun)

Bunは"all-in-one JavaScript runtime"とあるように、TypeScript/JSXのTranspiler/Bundler/Task Runerを同梱し、npm互換のパッケージマネージャーやNode-API(N-API)互換の実装、FetchなどのWeb APIの実装をもっています。

Denoと似ている立ち位置のRuntimeですが、Node.js互換のAPIや`package.json`を扱えるnpm互換の実装を持つことで、Node.jsを置き換えて利用できることが意識されています。

Bunのロードマップは次のIssueで公開されています。

- [Bun's Roadmap · Issue #159 · oven-sh/bun](https://github.com/oven-sh/bun/issues/159)

また、Bunをどのように作ったかについては、次の動画でインタビューに答えています。

- [NextJS Was Too Slow...So He Made Bun??! Jarred Sumner & The Story Of Bun - YouTube](https://www.youtube.com/watch?v=rL4qpniIR7o)

----

Vite 3.0.0がリリースされました。

- [Vite 3.0 is out! | Vite](https://vitejs.dev/blog/announcing-vite3.html#upgrades-to-vite-core)
- [vite/CHANGELOG.md at v3.0.0 · vitejs/vite](https://github.com/vitejs/vite/blob/v3.0.0/packages/vite/CHANGELOG.md)

デフォルトのビルドターゲットをESMとDynamic Import/`import.meta`をサポートしてるブラウザに変更、オプションの変更や削除、デフォルトportを`5173`に変更されています。
また、minifyに利用する`terser`パッケージへの依存をオプショナルへ変更、`import.meta.glob`の仕様変更、Wasmファイルのimport方法の変更などが含まれています。

----

## 600回目の更新

この投稿で、JSer.infoは600回目の更新となります。
500回目の更新からは大体2年でした。

- [JSer.info 500回目の更新 - Slackワークスペース作成、コラボレータ募集、10年に向けて - JSer.info](https://jser.info/2020/08/11/500/)

JSer.infoのslackワークスペースでは、気になるものを投稿したり、更新作業をやったりしています。
気になるものをメモ書きで投稿するぐらいの場所として扱うぐらいでいいと思います。
質問とかあったら調べて答える気もします。

JSer.infoのslackワークスペースは、次のリンクからだれでも自由に参加できます。

- [JSer.info slackに参加する](https://join.slack.com/t/jserinfo/shared_invite/zt-g2shzp7o-f_tj6OaphCAFw5Qlt2Jw0A)

また、[GitHub Sponsors](https://github.com/sponsors/azu)での支援も引き続き募集しています。

<iframe src="https://github.com/sponsors/azu/card" title="Sponsor azu" height="225" width="600" style="border: 0;"></iframe>

- 参考: [初めてでもわかる、GitHub Sponsorsでオープンソースを支援する方法](https://zenn.dev/azu/articles/c48ad63e20ad75)

JavaScript周りも新しいツールとかがまた続々と出てきている気がします(特に最近はEdgeを意識したものが多い印象)。
今回公開された[Bun](https://bun.sh/)も、作者が週80-90時間ぐらいを1年かけて作っているそうです。
こういう労力を結構かけて作られるものが増えている感じはします。

新しいツールが出てもウェブ標準互換やNode.js互換や[CDN Edgeでの互換性](https://wintercg.org/)などの互換性は強く意識されている感じはします。そのため、完全に全く新しい知識を必要とするものは意外と少なくて、既存のものに対して何かフラストレーションがあり、それを置き換えるために新しいツールとして作りながら既存との互換性を意識するといった形式が多い気がします(Bunの場合はフラストレーションが"速度"で、それを置き換える形で進化してきた)。

一方でGoogle Chromeが巨大となりウェブ標準のCentralization問題や、AppleはSafari以外のブラウザを許容しないこと対する反発の強まりといった問題なども起きています。

- [What willwould a Chromium-only Web look like?](https://www.mnot.net/blog/2022/06/22/chromium-only)
- [Open Web Advocacy](https://open-web-advocacy.org/)

色々な物事が大きくなっている感覚はありますが、それを小さな視点から見ていくのがJSer.infoなのかなと思いました。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## vite/CHANGELOG.md at v3.0.0 · vitejs/vite
[github.com/vitejs/vite/blob/v3.0.0/packages/vite/CHANGELOG.md](https://github.com/vitejs/vite/blob/v3.0.0/packages/vite/CHANGELOG.md "vite/CHANGELOG.md at v3.0.0 · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 3.0.0リリース。
デフォルトのビルドターゲットをESMとDynamic Import/`import.meta`をサポートしてるブラウザに変更、オプションの変更や削除、デフォルトportを5173に変更。
minifyに利用する`terser`パッケージへの依存をオプショナルへ変更、`import.meta.glob`の仕様変更、Wasmファイルのimport方法を変更など


----

## July 7th 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/july-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/july-2022-security-releases/ "July 7th 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 14/16/18のセキュリティリリース。


----
<h1 class="site-genre">アーティクル</h1>

----

## 応答性を示す新しい指標「INP」 | フロントエンドBlog | ミツエーリンクス
[www.mitsue.co.jp/knowledge/blog/frontend/202207/06\_1002.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202207/06_1002.html "応答性を示す新しい指標「INP」 | フロントエンドBlog | ミツエーリンクス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

ユーザー操作に対するインタラクションにかかった時間を計測するメトリクスであるINP(Interaction to Next Paint)について。
FIDとは異なりページのロード後に関する値を計測する。
CrUX、LighthouseのTimespanモード、Web Vitalsでの計測データの取り方についてなど

- [Interaction to Next Paint (INP)](https://web.dev/inp/ "Interaction to Next Paint (INP)")

----

## Announcing support for WASI on Cloudflare Workers
[blog.cloudflare.com/announcing-wasi-on-workers/](https://blog.cloudflare.com/announcing-wasi-on-workers/ "Announcing support for WASI on Cloudflare Workers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">cloudflare</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

Cloudflare WorkersでWASIに対応したWebAssemblyファイルを実行するライブラリがサポートされたことについて


----

## Blogged Answers: How I Estimate NPM Package Market Share (and how Redux usage compares to other libraries) · Mark&#039;s Dev Blog
[blog.isquaredsoftware.com/2022/07/npm-package-market-share-estimates/](https://blog.isquaredsoftware.com/2022/07/npm-package-market-share-estimates/ "Blogged Answers: How I Estimate NPM Package Market Share (and how Redux usage compares to other libraries) · Mark&#039;s Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">React</span> <span class="jser-tag">redux</span> <span class="jser-tag">article</span></p>

npmパッケージのシェアを読み取るかについて、Reactとステート管理ライブラリを例に解説している記事。
npmパッケージのダウンロード数、GitHubの依存数を絶対数として見た時の問題点や相対的に見る方法についてなど


----

## Flutter前史: ChromeがFlutterになるまで
[zenn.dev/mjhd/articles/680a19ae893c1e](https://zenn.dev/mjhd/articles/680a19ae893c1e "Flutter前史: ChromeがFlutterになるまで")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Flutter</span> <span class="jser-tag">history</span> <span class="jser-tag">article</span></p>

Flutterの歴史を振り返る動画について。
BlinkのForkから始まり、JavaScriptからDartへの切り替え、DOMからCanvasへの切り替えなどについて

- [Before Flutter | Rubber Duck Engineering | Episode #100 - YouTube](https://www.youtube.com/watch?v=xqGAC5QCYuQ&list=TLGGp4ABzxMuimsxMjA3MjAyMg "Before Flutter | Rubber Duck Engineering | Episode #100 - YouTube")
- [Before Flutter - Google スライド](https://docs.google.com/presentation/d/1Yhch7KkNC5wbkcsc9p5XkWouEha2hex65l6Pca_SqkM/edit#slide=id.g11cbab926eb_0_0 "Before Flutter - Google スライド")

----

## NestJS製GraphQLサーバの起動が遅かったので調査した話 - もうずっといなかぐらし
[katainaka0503.hatenablog.com/entry/2022/07/09/190340](https://katainaka0503.hatenablog.com/entry/2022/07/09/190340 "NestJS製GraphQLサーバの起動が遅かったので調査した話 - もうずっといなかぐらし")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span></p>

GraphQLのスキーマからTypeScriptのファイルを生成するツールのボトルネックを調べて修正した話。
`0x`を使ったボトルネック分析、`ts-morph`でのTypeScript ASTの変換のパフォーマンス問題の修正についてなど


----

## Executing shell commands from Node.js
[2ality.com/2022/07/nodejs-child-process.html](https://2ality.com/2022/07/nodejs-child-process.html "Executing shell commands from Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsの`node:child_process`モジュールでのコマンドの実行についての解説。
spawnとexecの解説、spawnとexecの違い、Streamでの出力の読み取り、AbortControllerを使ったプロセスの終了、同期と非同期についてなど


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## jcubic/wayne: Service Worker Routing library for in browser HTTP requests
[github.com/jcubic/wayne](https://github.com/jcubic/wayne "jcubic/wayne: Service Worker Routing library for in browser HTTP requests")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ServiceWorker</span> <span class="jser-tag">library</span></p>

Service Worker向けのルーティングライブラリ


----

## Tailwind DX
[gimli.app/tailwinddx.html](https://gimli.app/tailwinddx.html "Tailwind DX")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">Extension</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

Tailwind用のChrome拡張。
TailwindのクラスをChrome DevTools上で変更できる。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## samchon/typescript-json: Runtime type checkers and 5x faster JSON.stringify()
[github.com/samchon/typescript-json](https://github.com/samchon/typescript-json "samchon/typescript-json: Runtime type checkers and 5x faster JSON.stringify()")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">JSON</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

ttypescriptなどを使ったコード変換とRuntimeを合わせたJSONライブラリ。
TypeScriptの型を使ったRuntimeでの型チェック、`JSON.stringify`相当の処理を提供する


----

## oven-sh/bun: Incredibly fast JavaScript runtime, bundler, transpiler and package manager – all in one.
[github.com/oven-sh/bun](https://github.com/oven-sh/bun "oven-sh/bun: Incredibly fast JavaScript runtime, bundler, transpiler and package manager – all in one.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">Bun </span></p>

JavaScriptCoreとZig言語を使って書かれたJavaScriptのRuntime。
Bundler/TSのTranspiler/Task Runerを同梱し、npm互換のパッケージマネージャーやNode-API(N-API)互換の実装、FetchなどのWeb APIの実装をもつ。


----

## oguimbal/pg-mem: An in memory postgres DB instance for your unit tests
[github.com/oguimbal/pg-mem](https://github.com/oguimbal/pg-mem "oguimbal/pg-mem: An in memory postgres DB instance for your unit tests")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">PostgreSQL</span> <span class="jser-tag">library</span> <span class="jser-tag">testing</span> <span class="jser-tag">deno</span></p>

In-memoryのPostgresエミュレーターライブラリ。
Postgresを使ったテストで利用する目的


----
