---
title: "2019-05-14のJS: Google I/O 2019、GitHub Package Registry(npm, Docker, etc)"
author: "azu"
layout: post
date : 2019-05-14T01:14:26.660Z
category: JSer
tags:
- Google
- Chrome
- GitHub
- npm 

---

JSer.info #435 - [Google I/O 2019](https://events.google.com/io/)が開催されイベントの動画や関連するアップデートが多数公開されています。

Google I/Oのウェブ関連のセッションの動画は次のページにまとめられています。

- [Web at Google I/O 2019 - YouTube](https://www.youtube.com/watch?v=rUUazNIZW7I&list=PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i)

Google検索のクロールに使われているレンダリングエンジンがChrome 41相当から、最新版(現時点では74)のChromiumをベースとなるようにアップデートされています。

- [Official Google Webmaster Central Blog: The new evergreen Googlebot](https://webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html)

lighthouse 5.0.0がリリースされ、Wordpressなど特定のスタックに対するレポートを表示するStack Packsの追加、Performance budgetsの対応、Lighthouse pluginsの仕組みが追加されています。また、Performance budgetsの定義ファイルを生成する[Performance Budget Calculator](https://perf-budget-calculator.firebaseapp.com/)というツールも公開されています。

- [Release v5.0.0 · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0)

また、Googleが運営する[web.dev](https://web.dev/)も更新され[Blog](https://web.dev/blog)や[React](https://web.dev/react)アプリケーションの最適化についてのチュートリアルなどが追加されています。

----

GitHubが[GitHub Package Registry](https://github.com/features/package-registry)というパッケージレジストリサービスのベータ公開を発表しました。

- [Introducing GitHub Package Registry - The GitHub Blog](https://github.blog/2019-05-10-introducing-github-package-registry/)
- [GitHub Package Registry: Your packages, at home with their code](https://github.com/features/package-registry)

GitHub Package RegistryはnpmやRubyGems、Dockerなどに対応したpublic/private registryサービスです。
現在はベータなので、[GitHub Package Registryのsignup](https://github.com/features/package-registry/signup)から登録した人にプレリリースしている状態です。
詳細は次のドキュメントに書かれていますが、npmパッケージをGitHubのUserまたはOrgnization名に紐づいたscoped moduleとして公開できるようになるようです。

- [About GitHub Package Registry - GitHub Help](https://help.github.com/en/articles/about-github-package-registry)
- [Configuring NPM for use with GitHub Package Registry - GitHub Help](https://help.github.com/en/articles/configuring-npm-for-use-with-github-package-registry)

次の動画でGitHub Package Registryへpublishするデモなども行っているので、興味がある人は見てみると良さそうです。

- Video: [GitHub: "Introducing GitHub Package Registry"](https://www.pscp.tv/w/1jMKgvMEggwxL)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v5.0.0 · GoogleChrome/lighthouse
[github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0](https://github.com/GoogleChrome/lighthouse/releases/tag/v5.0.0 "Release v5.0.0 · GoogleChrome/lighthouse")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Lighthouse 5.0.0リリース。
Wordpressなど特定のスタックに対するレポートを表示するStack Packsの追加、Performance budgetsの対応、Lighthouse plugins

- [GoogleChrome/lighthouse-stack-packs: Lighthouse Stack Packs](https://github.com/GoogleChrome/lighthouse-stack-packs "GoogleChrome/lighthouse-stack-packs: Lighthouse Stack Packs")
- [Performance Budgets (Keep Request Counts Low And File Sizes Small)  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/lighthouse/audits/budgets "Performance Budgets (Keep Request Counts Low And File Sizes Small)  |  Tools for Web Developers  |  Google Developers")
- [lighthouse/plugins.md at master · GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/docs/plugins.md#plugin-config "lighthouse/plugins.md at master · GoogleChrome/lighthouse")

----

## Official Google Webmaster Central Blog: The new evergreen Googlebot
[webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html](https://webmasters.googleblog.com/2019/05/the-new-evergreen-googlebot.html "Official Google Webmaster Central Blog: The new evergreen Googlebot")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">search</span> <span class="jser-tag">news</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span></p>

Google検索botが最新版のChromiumレンダリングエンジンを使うように変更された

- [Fix Search-related JavaScript problems  |  Search  |  Google Developers](https://developers.google.com/search/docs/guides/fix-search-javascript "Fix Search-related JavaScript problems  |  Search  |  Google Developers")

----

## Node v12.2.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.2.0/](https://nodejs.org/en/blog/release/v12.2.0/ "Node v12.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.2.0リリース。
`--trace-tls`オプションの追加、`Module.createRequireFromPath()`を非推奨化し、`URL`でのパスも受け取れるようにした`module.createRequire`を追加など


----

## comlink/CHANGELOG.md at master · GoogleChromeLabs/comlink
[github.com/GoogleChromeLabs/comlink/blob/master/CHANGELOG.md#v3---v4](https://github.com/GoogleChromeLabs/comlink/blob/master/CHANGELOG.md#v3---v4 "comlink/CHANGELOG.md at master · GoogleChromeLabs/comlink")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">webworker</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

ES Proxyを使ったWorkerライブラリのComlink 4.0.0リリース。
Node.jsの`worker_thread`をサポート、APIのリネーム、パフォーマンスの改善など

- [Surma on Twitter: &quot;I sneakily released Comlink v4 just before #io19! ➡️Smaller than v3 (~1.1kb) 🗜 ➡️10x faster on low-end devices (we needed that for https://t.co/TQBh7GNv2g!) 🏎💨 ➡️Better API naming 💫 ➡️Better folder structure 🙏 ➡️Support for workers in Node 11+ 🤯 https://t.co/v4PNytvkfq… https://t.co/mksFf7uxPu&quot;](https://twitter.com/DasSurma/status/1127266398185484288 "Surma on Twitter: &amp;quot;I sneakily released Comlink v4 just before #io19! ➡️Smaller than v3 (~1.1kb) 🗜 ➡️10x faster on low-end devices (we needed that for https://t.co/TQBh7GNv2g!) 🏎💨 ➡️Better API naming 💫 ➡️Better folder structure 🙏 ➡️Support for workers in Node 11+ 🤯 https://t.co/v4PNytvkfq… https://t.co/mksFf7uxPu&amp;quot;")

----

## Release v1.16.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.16.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.16.0 "Release v1.16.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer 1.16.0リリース。
`browser.isConnected()`、`target.worker()`のサポート。
`accessibility.snapshot()`が`root`オプションをサポートなど


----

## Introducing GitHub Package Registry - The GitHub Blog
[github.blog/2019-05-10-introducing-github-package-registry/](https://github.blog/2019-05-10-introducing-github-package-registry/ "Introducing GitHub Package Registry - The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">github</span> <span class="jser-tag">news</span> <span class="jser-tag">npm</span></p>

GitHubのパッケージレジストリサービスのベータ公開がされた。
npm、gem、dockerなどに対応していて、GitHubのTeamパーミッションに紐付いて管理できるprivate registry。
GitHubのReleaseや検索にも表示されるようになる

- [GitHub Package Registry: Your packages, at home with their code](https://github.com/features/package-registry "GitHub Package Registry: Your packages, at home with their code")

----

## AWS Lambda adds support for Node.js v10
[aws.amazon.com/jp/about-aws/whats-new/2019/05/aws\_lambda\_adds\_support\_for\_node\_js\_v10/](https://aws.amazon.com/jp/about-aws/whats-new/2019/05/aws_lambda_adds_support_for_node_js_v10/ "AWS Lambda adds support for Node.js v10")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">aws</span> <span class="jser-tag">Lambda</span> <span class="jser-tag">node.js</span> <span class="jser-tag">news</span></p>

AWS LambdaがNode.js 10をサポート。


----
<h1 class="site-genre">アーティクル</h1>

----

## SameSite cookies explained  |  web.dev
[web.dev/samesite-cookies-explained/](https://web.dev/samesite-cookies-explained/ "SameSite cookies explained  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

`SameSite` Cookieについての解説。`SameSite`の設定値である`Strict`、`Lax`、`None`の動作の解説。
Chrome 76で`SameSite`が未指定の場合に`SameSite=Lax`をデフォルトとする試験的フラグが追加されるなど

- [HTTP クッキーをより安全にする SameSite 属性について (Same-site Cookies) | ラボラジアン](https://laboradian.com/same-site-cookies/ "HTTP クッキーをより安全にする SameSite 属性について (Same-site Cookies) | ラボラジアン")

----

## React  |  web.dev
[web.dev/react](https://web.dev/react "React  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">tutorial</span></p>

web.dev のReactウェブアプリの最適化についてのチュートリアル。
Bundle size、無限リスト、Service Worker、プリレンダリング、アクセシビリティについて


----

## A Guide to Node.js Logging - Twilio
[www.twilio.com/blog/guide-node-js-logging](https://www.twilio.com/blog/guide-node-js-logging "A Guide to Node.js Logging - Twilio")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">article</span></p>

Node.jsでログ出力についての記事。
Console API、pinoを使ったログ出力、ライブラリのログ、chalkなどで装飾されているログをプレーンな出力にする方法などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Web at Google I/O 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i](https://www.youtube.com/playlist?list=PLNYkxOF6rcIATmAmz7HcCzongGvQEtx8i "Web at Google I/O 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Google I/O 2019のウェブセッションの動画まとめ


----

## ng-conf 2019 - YouTube
[www.youtube.com/playlist?list&#x3D;PLOETEcp3DkCpimylVKTDe968yNmNIajlR](https://www.youtube.com/playlist?list=PLOETEcp3DkCpimylVKTDe968yNmNIajlR "ng-conf 2019 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

Angularのカンファレンスであるng-confg 2019の動画一覧。

- [Angular - All Talks from ng-conf 2019](https://nitayneeman.com/posts/all-talks-from-ng-conf-2019/ "Angular - All Talks from ng-conf 2019")
- [ng-conf 2019 Note](https://www.notion.so/ng-conf-2019-Note-10b9443262a54fb9bd8586cc25a449c7 "ng-conf 2019 Note")

----

## Node.js v12の気になる変更点 / #kng6 - Speaker Deck
[speakerdeck.com/masashi/number-kng6](https://speakerdeck.com/masashi/number-kng6 "Node.js v12の気になる変更点 / #kng6 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">slide</span></p>

Node.js 12の変更点についてまとめたスライド


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## wapm | WebAssembly Package Manager
[wapm.io/](https://wapm.io/ "wapm | WebAssembly Package Manager")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">webservice</span></p>

WebAssemblyのパッケージマネージャとレジストリ


----

## microsoft/frontend-bootcamp: Frontend Workshop from HTML/CSS/JS to TypeScript/React/Redux
[github.com/Microsoft/frontend-bootcamp](https://github.com/Microsoft/frontend-bootcamp "microsoft/frontend-bootcamp: Frontend Workshop from HTML/CSS/JS to TypeScript/React/Redux")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MS</span> <span class="jser-tag">HTML</span> <span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">tutorial</span></p>

Microsoftのフロントエンドワークショップ教材。
HTML、CSS、JavaScript、TypeScriptについて扱う2日分のコンテンツ


----

## Data | Third-Party Web
[www.thirdpartyweb.today/](https://www.thirdpartyweb.today/ "Data | Third-Party Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span></p>

HTTP Archiveのクロールデータを元にした、サードパーティスクリプトの影響度を可視化したサイト


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## manzinello/mailgo: 💌 mailgo, a different mailto (WIP)
[github.com/manzinello/mailgo](https://github.com/manzinello/mailgo "manzinello/mailgo: 💌 mailgo, a different mailto (WIP)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">mail</span></p>

`mailto:`なリンクをクリックした時にメニューを表示してくれるライブラリ。
GmailやOutlookで開くやコピーなどを選択できる


----

## victorvoid/dinoql: A customizable GraphQL style query language for interacting with JavaScript objects.
[github.com/victorvoid/dinoql](https://github.com/victorvoid/dinoql "victorvoid/dinoql: A customizable GraphQL style query language for interacting with JavaScript objects.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GraphQL</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

GraphQL構文でオブジェクトからデータを取得できるクエリライブラリ。
Alias、Cache、Fragmentsなどをサポートしている


----

## msgpack/msgpack-javascript: MessagePack for JavaScript/ECMA-262
[github.com/msgpack/msgpack-javascript](https://github.com/msgpack/msgpack-javascript "msgpack/msgpack-javascript: MessagePack for JavaScript/ECMA-262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

MessagePackのJavaScript実装。
ブラウザとNode.jsどちらでも動作し、Async Iteratorを使いストリーム処理ができるようになっている。

- [TypeScriptで MessagePack encoder/decoder を実装した - Islands in the byte stream](https://gfx.hatenablog.com/entry/2019/05/07/102341 "TypeScriptで MessagePack encoder/decoder を実装した - Islands in the byte stream")

----
