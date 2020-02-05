---
title: "2020-02-05のJS: npm unpublish policy、yarn v2(berry) RCリリース"
author: "azu"
layout: post
date : 2020-02-05T03:42:06.633Z
category: JSer
tags:
- npm
- yarn

---

JSer.info #473 - npmにはパッケージを公開した人がパッケージを取り下げるルールを決めた[npm Unpublish Policy](https://www.npmjs.com/policies/unpublish)があります。
今回、この[npm Unpublish Policy](https://www.npmjs.com/policies/unpublish)のルールが更新されています。

- [The npm Blog — Changes to npm Unpublish Policy - January 2020](https://blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020)

元々このUnpublish Policyは[left-padがunpublishされた件](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm)で、使われているnpmパッケージがunpublishされるとnpmのエコシステムが壊れるため、`npm unpublish`に対して制限を入れるために導入されたルールです。

- [The npm Blog — changes to npm’s unpublish policy](https://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy)

今回の変更では、`npm publish`してから`npm unpublish`できるまでの時間制限が緩める変更と、いくつかの条件を満たす場合は時間とは関係なくunpublishできるようになっています。

- publishしてから72時間以内(元々は24時間以内)
- また、ダウンロード数が300未満 かつ 別の公開モジュールから依存されていない かつ メンテナが単独

この変更以前では、publishしてから24時間以上経つと、unpublishするためにはサポートに連絡する必要がありました。
そのため、他から依存されていなそうなモジュールに関しては、`npm unpublish`できるようにするルール変更をしたという感じのようです。

----

Yarnのメジャーアップデートであるv2([yarnpkg/berry](https://github.com/yarnpkg/berry))のRC版が進んできたのにあわせて、Yarn 2での変更点などに関して書かれた記事がメンテナーの[arcanis](https://github.com/arcanis)によって公開されています。

- [Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻](https://dev.to/arcanis/introducing-yarn-2-4eh1)

この記事では、現在のStableであるYarn v1はlegacyになり、今後のStableはv2(berry)に切り替わる予定などについて書かれています。
ウェブサイトの方もそれに合わせてリダイレクトされてるようになっていて、この影響で[翻訳されたページが404](https://github.com/yarnpkg/website/issues/1042)になったりもしています。

- Yarn v2: https://next.yarnpkg.com
- Yarn v1: https://classic.yarnpkg.com

Yarn 2の変更点についても紹介されていて、デフォルトでCacheをリポジトリに配置するように変更、CLIの出力の変更などv1の仕組みの違いについて書かれています。
また新しい機能として、`npx`と同じような`yarn dlx`の追加、`patch:`/`portal:`の対応、Workspaceのコマンド改善、Workspaceの検証をするConstraintsの追加などもされています。
その他にもパッケージごとにビルドするかを設定可能に、`yarn run`でOS間のシェルの違いをノーマライズするように、Lockファイルのフォーマット変更、パッケージはRead-Onlyに変更なども含まれています。

すでにv2に関するドキュメントやマイグレーションガイドも公開されているため、興味がある人は読んでみるといいと思います。

- [Migration | Yarn - Package Manager](https://next.yarnpkg.com/advanced/migration "Migration | Yarn - Package Manager")
- [Plug'n'Play | Yarn - Package Manager](https://next.yarnpkg.com/features/pnp "Plug&#x27;n&#x27;Play | Yarn - Package Manager")
- [Zero-Installs | Yarn - Package Manager](https://next.yarnpkg.com/features/zero-installs "Zero-Installs | Yarn - Package Manager")


----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v2.1.0 · puppeteer/puppeteer
[github.com/puppeteer/puppeteer/releases/tag/v2.1.0](https://github.com/puppeteer/puppeteer/releases/tag/v2.1.0 "Release v2.1.0 · puppeteer/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v2.1.0 リリース。
Chromium 80へアップデート、Firefoxをサポートなど


----

## New PWABuilder release! - PWABuilder - Medium
[medium.com/pwabuilder/new-pwabuilder-release-b2932f4722a5](https://medium.com/pwabuilder/new-pwabuilder-release-b2932f4722a5 "New PWABuilder release! - PWABuilder - Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ProgressiveWebApp</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

PWABuilderのアップデート。
Trusted Web Activityを使ったAndroid向けのパッケージングに対応、パッケージングするためのガイドの刷新など

- [PWABuilder](https://www.pwabuilder.com/ "PWABuilder")
- [GoogleChromeLabs/llama-pack: Llama Pack 🦙 is a Command Line Interface (CLI) that helps developers to create a Project for an Android application that launches an existing Progressive Web App (PWAs) using a Trusted Web Activity.](https://github.com/GoogleChromeLabs/llama-pack "GoogleChromeLabs/llama-pack: Llama Pack 🦙 is a Command Line Interface (CLI) that helps developers to create a Project for an Android application that launches an existing Progressive Web App (PWAs) using a Trusted Web Activity.")

----

## The npm Blog — Changes to npm Unpublish Policy - January 2020
[blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020](https://blog.npmjs.org/post/190553543620/changes-to-npm-unpublish-policy-january-2020 "The npm Blog — Changes to npm Unpublish Policy - January 2020")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">news</span></p>

npmのunpublish policyの変更。
今まで24時間以内だったらunpublishできたのが、72時間以内ならunpublish出来るように変更された。
またダウンロード数が300未満、別の公開モジュールから依存されていない、メンテナが単独の条件を満たす場合もunpublishが可能となった。

- [policies/unpublish.md at master · npm/policies](https://github.com/npm/policies/blob/master/unpublish.md "policies/unpublish.md at master · npm/policies")

----

## Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻
[dev.to/arcanis/introducing-yarn-2-4eh1](https://dev.to/arcanis/introducing-yarn-2-4eh1 "Introducing Yarn 2 ! 🧶🌟 - DEV Community 👩‍💻👨‍💻")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">yarn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

Yarn 2について。
Yarn v1はlegacyになり、今後のStableはv2(berry)に切り替わる予定。
デフォルトでCacheをリポジトリに配置するように変更、CLIの出力の変更、`npx`と同じような`yarn dlx`の追加、`patch:`/`portal:`の対応。
Workspaceのコマンド改善、Workspaceの検証をするConstraintsの追加。
パッケージごとにビルドするかを設定可能に、`yarn run`でOS間のシェルの違いをノーマライズするように、Lockファイルのフォーマット変更、パッケージはRead-Onlyに変更など

- [Migration | Yarn - Package Manager](https://next.yarnpkg.com/advanced/migration "Migration | Yarn - Package Manager")
- [Plug'n'Play | Yarn - Package Manager](https://next.yarnpkg.com/features/pnp "Plug&#x27;n&#x27;Play | Yarn - Package Manager")
- [Zero-Installs | Yarn - Package Manager](https://next.yarnpkg.com/features/zero-installs "Zero-Installs | Yarn - Package Manager")

----

## Meteor 1.9 (Node.js 12) and new Roadmaps - Meteor Blog
[blog.meteor.com/meteor-1-9-node-js-12-and-new-roadmaps-cb993277d444](https://blog.meteor.com/meteor-1-9-node-js-12-and-new-roadmaps-cb993277d444 "Meteor 1.9 (Node.js 12) and new Roadmaps - Meteor Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag"> node</span> <span class="jser-tag">ReleaseNote</span></p>

Meteor 1.9リリース。
Node.js 12をサポート、Galaxy(Metorのホスティング環境)のロードマップについて


----

## Release Releaaaaaaaaaaaaaaaaaaase · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.3.0](https://github.com/preactjs/preact/releases/tag/10.3.0 "Release Releaaaaaaaaaaaaaaaaaaase · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.3.0リリース
Built-In要素を継承したCustom Elementに対応、バグ修正など


----
<h1 class="site-genre">アーティクル</h1>

----

## What's New In DevTools (Chrome 81)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/01/devtools](https://developers.google.com/web/updates/2020/01/devtools "What's New In DevTools (Chrome 81)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 81の開発者ツールの変更点について。
ブロックされたCookieに色をつけるように、ネットワークパネルで`Copy as Node.js fetch`の追加、Source Mapのエラーをコンソールに表示など


----

## JavaScript Libraries Are Almost Never Updated Once Installed
[blog.cloudflare.com/javascript-libraries-are-almost-never-updated/](https://blog.cloudflare.com/javascript-libraries-are-almost-never-updated/ "JavaScript Libraries Are Almost Never Updated Once Installed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

CDN経由でサイトに埋め込まれているJavaScriptライブラリは一度インストールされたあとにアップデートされることが殆どないというデータについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## まもなくやってくる Vue.js 3 - Speaker Deck
[speakerdeck.com/kazupon/mamonakuyatutekuru-vue-dot-js-3](https://speakerdeck.com/kazupon/mamonakuyatutekuru-vue-dot-js-3 "まもなくやってくる Vue.js 3 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">slide</span></p>

Vue.js 3についてのスライド。
Composition API、ライフサイクルフック、DI(`provide`,`inject`)、ReactライクなPortalとSuspense、CSSの独自擬似クラスの追加。
またフィルターの削除、グローバル状態の整理などについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Adapt · React for your infrastructure.
[adaptjs.org/](https://adaptjs.org/ "Adapt · React for your infrastructure.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Infrastructure</span> <span class="jser-tag">Tools</span></p>

Reactを使ってpulumiなどのようにインフラをコード管理するツール。
Hooks API、コンポーネント、JSXで設定を書ける。
環境やプロバイダーなどの分離はStyleという形で分離できるようにしている。


----

## cutenode/mingine: A module to get the minimum usable engine(s)
[github.com/cutenode/mingine](https://github.com/cutenode/mingine "cutenode/mingine: A module to get the minimum usable engine(s)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag"> node</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

依存してるnpmパッケージの`engines`フィールドから、`engines`ごとのminimumなバージョンを算出するライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## Manning | Deep Learning with JavaScript
[www.manning.com/books/deep-learning-with-javascript](https://www.manning.com/books/deep-learning-with-javascript "Manning | Deep Learning with JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">MachineLearning</span> <span class="jser-tag">book</span></p>

TensorFlow.jsを使ったDeep Learningについての書籍


----

## プログラミングTypeScript ―スケールするJavaScriptアプリケーション開発 | Boris Cherny, 今村 謙士, 原 隆文 |本 | 通販 | Amazon
[www.amazon.co.jp/dp/4873119049/](https://www.amazon.co.jp/dp/4873119049/ "プログラミングTypeScript ―スケールするJavaScriptアプリケーション開発 | Boris Cherny, 今村 謙士, 原 隆文 |本 | 通販 | Amazon")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2020年3月16日発売
Programming TypeScriptの翻訳本


----
