---
title: "2019-10-15のJS: webpack 5β、Next.js(create-next-app)、Same-Site Cookies"
author: "azu"
layout: post
date : 2019-10-15T00:48:55.247Z
category: JSer
tags:
- webpack
- Next.js
- Cookie

---

JSer.info #457 - webpack 5βがリリースされ、ベータフィードバックを求めるIssueが作られています。

- [webpack 5 beta feedback · Issue #9802 · webpack/webpack](https://github.com/webpack/webpack/issues/9802)
- [changelog-v5/README.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/README.md)

webpack 5βでは、破壊的な変更としてNode.jsコアモジュールの自動Polyfillの削除、Long TermキャッシュのためにChunkとModule Idのハッシュアルゴリズムの変更、オプション名の変更などが行われています。
その他の機能として、ファイルシステムキャッシュ設定の追加、Tree Shakingの改善、`output.ecmaVersion`オプションの追加なども行われています。
また試験的な機能として`asset` module typeの追加、Top Level `await`のサポートなども含まれています。

4.xから5.xへのマイグレーションガイドも次のページで公開されています。

- [changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/MIGRATION%20GUIDE.md)

ベータフィードバックでは、バグやパフォーマンスリグレッション、Breaking Changeに対するコメントなどが募集されています。

----

Next.js 9.1.0がリリースされました。

- [Blog - Next.js 9.1 | Next.js](https://nextjs.org/blog/next-9-1)
- [Release v9.1.0 · zeit/next.js](https://github.com/zeit/next.js/releases/tag/v9.1.0)

Next.js 9.1.0では、`src/pages`ディレクトリのサポート、`next export`で`public/`ディレクトリへ出力できるように設定が追加されています。
また、次の試験的な機能がフラグ付きで実装されています。

- Built-in CSS Support
- Static Error Pages
- Module / Nomoduleの出力

その他には、今までコミュニティが管理していた`create-next-app`が公式に移管されました。
[公式のExample](https://github.com/zeit/next.js/tree/canary/examples)でも`create-next-app`を使っていく形になるようです。

- [Blog - Introducing Create Next App | Next.js](https://nextjs.org/blog/create-next-app)

----

[Same-Site Cookies By Default | text/plain](https://textslashplain.com/2019/09/30/same-site-cookies-by-default/)という記事ではSame-Site Cookiesについて詳しく書かれています。

Chrome 80でCookieのデフォルト`SameSite=Lax`とする予定で、この記事ではSame-Site Cookiesの目的や実際の影響などについて書かれています。
Same-Site CookiesはCSRF攻撃からの保護に役立つごとや、CookiのHTTPOnly属性やSecure属性についても書かれています。
またSame-Siteがデフォルトとなった場合の実際の影響や他のブラウザの対応などについても書かれています。

Same-Site Cookiesは`SameSite=None`と設定することで無効化できますが、[Safari 12には`SameSite=None`を`SameSite=Strict`](https://bugs.webkit.org/show_bug.cgi?id=198181)として扱うバグがあることやデバッグ方法についてなど実際に扱う場合の問題についても触れています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## The new evergreen Bingbot simplifying SEO by leveraging Microsoft Edge | Webmaster Blog
[blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge](https://blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge "The new evergreen Bingbot simplifying SEO by leveraging Microsoft Edge | Webmaster Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">SEO</span> <span class="jser-tag">news</span></p>

BingがChromiumベースのMSEdgeを採用。
クロールするBingbotがChrome相当になり、定期的に最新のStableにアップデートされる。


----

## Release v9.1.0 · zeit/next.js
[github.com/zeit/next.js/releases/tag/v9.1.0](https://github.com/zeit/next.js/releases/tag/v9.1.0 "Release v9.1.0 · zeit/next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Next.js 9.1.0リリース。
`src/pages`ディレクトリのサポート、`next export`で`public/`ディレクトリへ出力できるように


----

## webpack 5 beta feedback · Issue #9802 · webpack/webpack
[github.com/webpack/webpack/issues/9802](https://github.com/webpack/webpack/issues/9802 "webpack 5 beta feedback · Issue #9802 · webpack/webpack")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">ReleaseNote</span></p>

webpack 5βリリース。
Node.jsコアモジュールの自動Polyfillの削除、Long TermキャッシュのためにChunkとModule Idのハッシュアルゴリズムの変更、オプション名の変更など。
ファイルシステムキャッシュ設定の追加、Tree Shakingの改善、`output.ecmaVersion`オプションの追加。
また試験的な機能として、`asset` module typeの追加、Top Level `await`のサポートなど

- [changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/MIGRATION%20GUIDE.md "changelog-v5/MIGRATION GUIDE.md at master · webpack/changelog-v5")
- [changelog-v5/README.md at master · webpack/changelog-v5](https://github.com/webpack/changelog-v5/blob/master/README.md "changelog-v5/README.md at master · webpack/changelog-v5")

----

## Node v12.12.0 (Current) | Node.js
[nodejs.org/en/blog/release/v12.12.0/](https://nodejs.org/en/blog/release/v12.12.0/ "Node v12.12.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 12.12.0リリース。
`fs.opendir()`、`fs.Dir`の追加、`--enable-source-maps`でのスタックトレースのSource Mapサポートなど


----

## Blog - Introducing Create Next App | Next.js
[nextjs.org/blog/create-next-app](https://nextjs.org/blog/create-next-app "Blog - Introducing Create Next App | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

`create-next-app`がNext.jsの公式プロジェクトになった。


----
<h1 class="site-genre">アーティクル</h1>

----

## Top-level await · V8
[v8.dev/features/top-level-await](https://v8.dev/features/top-level-await "Top-level await · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Top-level `await`について。
Top-level `await`のユースケースや実行順序などの挙動についてなど


----

## Same-Site Cookies By Default | text/plain
[textslashplain.com/2019/09/30/same-site-cookies-by-default/](https://textslashplain.com/2019/09/30/same-site-cookies-by-default/ "Same-Site Cookies By Default | text/plain")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Chrome 80でされるSameSite=Laxのデフォルト化について。
CookieのSecurityとPrivacyの問題、Same-Site Cookiesの目的、CSRF攻撃からの保護、HTTPOnly属性やSecure属性について。
またSame-Siteがデフォルトとなった場合の実際の影響や他のブラウザの対応、2分間の緩和についてなど


----

## What's new in Chrome 78 - LogRocket Blog
[blog.logrocket.com/whats-new-in-chrome-78/](https://blog.logrocket.com/whats-new-in-chrome-78/ "What's new in Chrome 78 - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 78の変更点について。
CSS opacityの`%`サポート、ES ProposalのOptional Chaining、`unload`時の制限、User Timing Lv3、WebSocketStreamのサポートなど。

Origin TrialとしてサポートされたNative File System APIやSMS Receiver APIについてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Vue.js Performance Tips / #v\_kansai 11 - Speaker Deck
[speakerdeck.com/masashi/number-v-kansai-11](https://speakerdeck.com/masashi/number-v-kansai-11 "Vue.js Performance Tips / #v\_kansai 11 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">performance</span> <span class="jser-tag">slide</span></p>

Vue.jsアプリのパフォーマンス改善についてのスライド。
IntersectionObserverを使った表示サれたことの検知、画像の遅延ロード、Hydrationの遅延実行などについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## lirantal/is-website-vulnerable: finds publicly known security vulnerabilities in a website's frontend JavaScript libraries
[github.com/lirantal/is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable "lirantal/is-website-vulnerable: finds publicly known security vulnerabilities in a website's frontend JavaScript libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">security</span> <span class="jser-tag">Tools</span></p>

指定したURLに脆弱性のあるライブラリが使われているかを判定するツール。
Synxベースの脆弱性判定をしている。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## leeoniya/uPlot: An exceptionally fast, tiny time series chart
[github.com/leeoniya/uPlot](https://github.com/leeoniya/uPlot "leeoniya/uPlot: An exceptionally fast, tiny time series chart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">chart</span> <span class="jser-tag">library</span></p>

ファイルサイズが小さな時系列グラフライブラリ


----

## devforth/painterro: Painterro - JavaScript painting plugin
[github.com/devforth/painterro](https://github.com/devforth/painterro "devforth/painterro: Painterro - JavaScript painting plugin")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Image</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

画像エディタライブラリ


----

## luwes/sinuous: Small, fast, reactive UI library
[github.com/luwes/sinuous](https://github.com/luwes/sinuous "luwes/sinuous: Small, fast, reactive UI library")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">UI</span> <span class="jser-tag">library</span> <span class="jser-tag">jsx</span></p>

`htm`構文、Hyperscript、JSXに対応したUIライブラリ。
observableな値監視の仕組みも提供し、小さなファイルサイズでUIを作成できるようにすることが目的

- [developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.](https://github.com/developit/htm "developit/htm: Hyperscript Tagged Markup: JSX alternative using standard tagged templates, with compiler support.")

----
