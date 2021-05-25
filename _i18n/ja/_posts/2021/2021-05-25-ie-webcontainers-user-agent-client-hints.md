---
title: "2021-05-25のJS: IEの単体アプリとしてのサポート終了、WebContainers、User-Agent Client Hints"
author: "azu"
layout: post
date : 2021-05-25T02:50:27.271Z
category: JSer
tags:
- node.js
- Chrome
- Tools
- CSS
- React

---

JSer.info #541 - Windows 10においてのInternet Explorer(IE)の単体のアプリとしてサポートが2022年6月15日で終了されることがアナウンスされました。

- [The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog](https://blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/)
- [Internet Explorer は Microsoft Edge へ – Windows 10 の Internet Explorer 11 デスクトップアプリは 2022 年 6 月 15 日にサポート終了 - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/)
- [「Internet Explorer 11 デスクトップ アプリケーションのサポート終了」の発表に関連する FAQ - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/internet-explorer-11-desktop-app-retirement-faq/)

2022年6月15日以降は、IEのデスクトップアプリケーション(`iexplore.exe`)を利用しようとするとMicrosoft Edge(MSEdge)が代わりに起動します。
MSEdgeにはIE モードが搭載されており、MSEdgeの設定を変更することでIEのレンダリングエンジンであるMSHTML (Trident)が使えるようになるようです。

- [Microsoft Edge の Internet Explorer モード - Office サポート](https://support.microsoft.com/ja-jp/office/microsoft-edge-%e3%81%ae-internet-explorer-%e3%83%a2%e3%83%bc%e3%83%89-6604162f-e38a-48b2-acd2-682dbac6f0de?ui=ja-JP&rs=ja-JP&ad=JP)

このIEモード(MSHTML)のサポート自体は今回のアナウンスとは関係なく、 2029 年までサポートされる予定となっています。

---

WebContainersというブラウザ上でNode.jsのランタイムを動かす仕組みがstackblitzで公開されています。

- [Introducing WebContainers: Run Node.js natively in your browser](https://blog.stackblitz.com/posts/introducing-webcontainers/)

Node.jsのランタイムをブラウザで動かし、ブラウザ自体をSandboxとしてNode.jsのコードをセキュアに実行するための仕組みとなっています。あくまでブラウザの中で動かす仕組みであるため、ネイティブアドオンは対応せずCORSなどブラウザの制約の中で動作します。

[stackblitz/webcontainer-core](https://github.com/stackblitz/webcontainer-core)ではキーコンセプトが解説されています。
Virtual FSとNetworkingを実装し、各プロセスをWorkerとして起動してメッセージングすることでマルチプロセスのサポートしています。POSIXなシェルとしてjshという実装と、npm/yarnクライアントとしてturboという実装を持っています。

現在はオープンソースではありませんが、将来的に[コア部分はオープンソースとして公開](https://news.ycombinator.com/item?id=27225150)する予定となっています。

---

ChromeにおけるUA文字列を扱う `navigator.userAgent`, `navigator.appVersion`, `navigator.platform` を非推奨とするロードマップが更新されています。

- [Chromium Blog: Update on User-Agent String Reduction in Chrome](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html)

Chrome 92で非推奨の警告をだすようになり、段階的にUA文字列から情報を削り、UA文字列化を固定化していく予定のロードマップが公開されています。

`navigator.userAgent`の代替となる仕組みとして、UA Client Hintsがありロードマップの記事とあわせて、UA Client Hintsへの移行方法についての記事も公開されています。

- [Migrate to User-Agent Client Hints](https://web.dev/migrate-to-ua-ch/)
- [GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.](https://github.com/GoogleChromeLabs/uach-retrofill)


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Recoil 0.3.0 | Recoil
[recoiljs.org/blog/2021/05/14/0.3.0-released/](https://recoiljs.org/blog/2021/05/14/0.3.0-released/ "Recoil 0.3.0 | Recoil")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Recoil 0.3.0リリース。
RecoilRootに`override`オプションの追加、selectorに`GetCallback`を追加。
次の0.4で`snapshot.retain()`していないsnapshotを使うと例外が発生するようになる


----

## The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog
[blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/](https://blogs.windows.com/windowsexperience/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/ "The future of Internet Explorer on Windows 10 is in Microsoft Edge | Windows Experience Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">IE</span> <span class="jser-tag">news</span> <span class="jser-tag">MSEdge</span></p>

IE11のデスクトップアプリケーションとしてのサポートは2022年6月15日で終了し、MSEdgeのIEモードで引き続き2029年までサポートする予定。

- [Internet Explorer は Microsoft Edge へ – Windows 10 の Internet Explorer 11 デスクトップアプリは 2022 年 6 月 15 日にサポート終了 - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/the-future-of-internet-explorer-on-windows-10-is-in-microsoft-edge/ "Internet Explorer は Microsoft Edge へ – Windows 10 の Internet Explorer 11 デスクトップアプリは 2022 年 6 月 15 日にサポート終了 - Windows Blog for Japan")
- [「Internet Explorer 11 デスクトップ アプリケーションのサポート終了」の発表に関連する FAQ - Windows Blog for Japan](https://blogs.windows.com/japan/2021/05/19/internet-explorer-11-desktop-app-retirement-faq/ "「Internet Explorer 11 デスクトップ アプリケーションのサポート終了」の発表に関連する FAQ - Windows Blog for Japan")

----

## Release v7.5.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v7.5.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v7.5.0 "Release v7.5.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 7.5.0リリース。
Source Mapベースのファイルツリーを可視化するTreemap表示の追加、新しいCLSへの対応を追加など


----

## Node v16.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v16.2.0/](https://nodejs.org/en/blog/release/v16.2.0/ "Node v16.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node v16.2.0リリース。
`import.meta.resolve`が`URL`オブジェクトをサポート、Workerが作成された際にtriggerされる`worker`イベントを`process`に追加など


----

## DOM Events
[domevents.dev/](https://domevents.dev/ "DOM Events")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">event</span> <span class="jser-tag">Tools</span></p>

DOMイベントの流れをBubbling、Capture、Passiveなどのオプションごとに動きを可視化できるツール


----

## Release v10.0.0 · TypeStrong/ts-node
[github.com/TypeStrong/ts-node/releases/tag/v10.0.0](https://github.com/TypeStrong/ts-node/releases/tag/v10.0.0 "Release v10.0.0 · TypeStrong/ts-node")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScriptのコンパイルをRuntime時に行うts-node 10.0.0リリース。
`--script-mode`の挙動をデフォルト化し、古い挙動を再現する`--cwd-mode`を追加。
Node.js 10のサポート終了、`--show-config`の追加、`--transpiler`オプションでSWCを使ったtrasnpileに対応など。
またウェブサイトが更新されている。

- [Third-party transpilers | ts-node](https://typestrong.org/ts-node/docs/transpilers/ "Third-party transpilers | ts-node")
- [ts-node | ts-node](https://typestrong.org/ts-node/ "ts-node | ts-node")

----
<h1 class="site-genre">アーティクル</h1>

----

## Chromium Blog: Update on User-Agent String Reduction in Chrome
[blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html "Chromium Blog: Update on User-Agent String Reduction in Chrome")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

ChromeのUser-Agent固定化のロードマップ。
Chrome 92で`navigator.userAgent`などのdeprecated化、reduced UA stringをオプトインで導入、デフォルト化など7段階でのマイグレーションフェーズについて

- [User-Agent Reduction - The Chromium Projects](https://www.chromium.org/updates/ua-reduction "User-Agent Reduction - The Chromium Projects")

----

## Introducing Firefox&#039;s new Site Isolation Security Architecture - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/](https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/ "Introducing Firefox&#039;s new Site Isolation Security Architecture - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

FirefoxのSite Isolationのアーキテクチャについての記事。
eTLDベースのSiteごとにプロセス分け、メモリを相互に分離した状態でリソースをロードすることで、Spectreなどのサイドチャネル攻撃を防止する。
また、サブフレームもトップレベルが異なるSiteなら、別プロセスで読むこむようになっている。


----

## The Humble &lt;img&gt; Element And Core Web Vitals — Smashing Magazine
[www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/](https://www.smashingmagazine.com/2021/04/humble-img-element-core-web-vitals/ "The Humble &lt;img&gt; Element And Core Web Vitals — Smashing Magazine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Image</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

`<img>`についてLCP、CLS、FIDのメトリクスに関する最適化の仕方についてのガイド


----

## Introducing WebContainers: Run Node.js natively in your browser
[blog.stackblitz.com/posts/introducing-webcontainers/](https://blog.stackblitz.com/posts/introducing-webcontainers/ "Introducing WebContainers: Run Node.js natively in your browser")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">browser</span> <span class="jser-tag">webworker</span> <span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span></p>

Node.jsをブラウザで動かすWebContainersについて。
Node.jsのランタイムをブラウザで動かし、ブラウザ自体をSandboxとしてNode.jsのコードをセキュアに実行するための仕組み。
Virtual FSとNetworkingを実装し、各プロセスをWorkerとして起動してメッセージングすることでマルチプロセスのサポートしている。
POSIXなシェルとしてjshという実装と、npm/yarnクライアントとしてturboという実装を持っている

- [stackblitz/webcontainer-core](https://github.com/stackblitz/webcontainer-core "stackblitz/webcontainer-core")
- [AngularAir - StackBlitz with Eric Simons and Dominic Elm - YouTube](https://www.youtube.com/watch?v=5F9qH-ea5Qk "AngularAir - StackBlitz with Eric Simons and Dominic Elm - YouTube")

----

## Migrate to User-Agent Client Hints
[web.dev/migrate-to-ua-ch/](https://web.dev/migrate-to-ua-ch/ "Migrate to User-Agent Client Hints")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span> <span class="jser-tag">privacy</span></p>

`navigator.userAgent`などがDeprecatedとなり固定化されるため、その代わりとなるUser-Agent Client Hintsについて。
JavaScriptのAPIとしての`navigator.userAgentData`と`navigator.userAgentData.getHighEntropyValues`。
HTTPヘッダUA Client Hintを扱う`Accept-CH`と`Sec-CH-UA-*`について。
また、Client HintからレガシーなUA文字列を作成するライブラリについてなど

- [Chromium Blog: Update on User-Agent String Reduction in Chrome](https://blog.chromium.org/2021/05/update-on-user-agent-string-reduction.html "Chromium Blog: Update on User-Agent String Reduction in Chrome")
- [GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.](https://github.com/GoogleChromeLabs/uach-retrofill "GoogleChromeLabs/uach-retrofill: This snippet illustrates how to reconstruct the legacy navigator.userAgent string value from the modern navigator.userAgentData values.")

----

## Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium
[nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8](https://nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8 "Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsのネイティブアドオン用のAPIの名前をN-APIをNode-APIへ変更するという話。
変更のモチベーションについて解説している

- [Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium](https://nodejs.medium.com/renaming-n-api-to-node-api-27aa8ca30ed8 "Renaming N-API to Node-API. This post was contributed by the… | by Node.js | May, 2021 | Medium")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## オリジナルのJavaScriptライブラリを公開しよう
[zenn.dev/yusuke99/books/fcd96342f5cb1b468799](https://zenn.dev/yusuke99/books/fcd96342f5cb1b468799 "オリジナルのJavaScriptライブラリを公開しよう")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">Github</span> <span class="jser-tag">Actions</span> <span class="jser-tag">tutorial</span></p>

JavaScriptのライブラリをnpmに公開するチュートリアル。
ライブラリの実装とテスト、npmへの公開、GitHub ActionsでのCIからpublish、Scoped Packagesについてなど


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## argyleink/transition.css: Drop-in CSS transitions
[github.com/argyleink/transition.css](https://github.com/argyleink/transition.css "argyleink/transition.css: Drop-in CSS transitions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">library</span></p>

いろいろなCSS transitionを集めたCSSライブラリ


----

## rtk-incubator/rtk-query: Experimental data fetching and caching addon for Redux Toolkit
[github.com/rtk-incubator/rtk-query](https://github.com/rtk-incubator/rtk-query "rtk-incubator/rtk-query: Experimental data fetching and caching addon for Redux Toolkit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">redux</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">React</span></p>

Redux Toolkitを使うデータ取得と状態管理をするQueryライブラリ。
宣言的なAPIの定義、データの取得、キャッシュやリトライ、Prefetching、React Hooks、Open APIから自動生成などに対応している。
将来的にはRedux Toolkitに同梱することを目標にしている。


----

## ngneat/variabless: JS &amp; CSS - A Match Made in Heaven 💎
[github.com/ngneat/variabless](https://github.com/ngneat/variabless "ngneat/variabless: JS &amp; CSS - A Match Made in Heaven 💎")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span></p>

JavaScriptからCSS Variablesの定義を含んだCSSを生成するツール


----

## Web worker meets worker threads - threads.js
[threads.js.org/](https://threads.js.org/ "Web worker meets worker threads - threads.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">webworker</span></p>

ブラウザのWeb WorkerとNode.jsの`worker_threads`を使ったWorker管理ライブラリ。
async functionとObservablesの対応、thread pools、webpack向けのpluginを持っている


----
