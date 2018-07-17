---
title: "2018-07-17のJS: TypeScript 3.0.0、ウイルスとnpmパッケージ、Property based testing"
author: "azu"
layout: post
date : 2018-07-17T02:20:17.375Z
category: JSer
tags:
- TypeScript
- eslint
- npmjs
- testing

---

JSer.info #392 - TypeScript 3.0 RCが公開されています。
TypeScriptは[Semantic Versioning](https://semver.org/)ではないため、いわゆるメジャーアップデートとは違いますが、monorepoなど大きなリポジトリ向けの変更が入っています。

- [Announcing TypeScript 3.0 RC | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/07/12/announcing-typescript-3-0-rc/)
- [TypeScript 3.0.0-RC 変更点 - Qiita](https://qiita.com/vvakame/items/57a0559c45b88b2ae168)
- [Breaking Changes · Microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-30)

Project Referencesによりmonorepo内の別パッケージの型定義を参照できるようになり、Build modeによって関連するパッケージのインクリメンタルビルドできます。
今までも[`paths`](https://github.com/Quramy/lerna-yarn-workspaces-example)を使ってmonorepo内の別パッケージのソースコード(`.ts`)を直接参照できていましたが、[module resolution](https://github.com/textlint/textlint/issues/440)や`outDir`に必要ないものまで含まれるなどの問題がありました。

TypeScript 3.0ではこれらの問題を解決するメタIssueがあり、フィードバックを募集しています。

- [tsc --build / Project References Feedback & Discussion · Issue #25600 · Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/25600)

またTuple型の改善、`unknown`型の追加、Reactのdefault propsの型チェックのサポートなどが行われています。

----

2018年7月12日の18:00〜22:00（JST）に`eslint-scope@3.7.2`または`eslint-config-eslint@5.0.2`を含むパッケージをインストールすると`.npmrc`を盗み取られるウイルス入りのパッケージが公開されていたインシデントがありました。

`eslint-scope@3.x`に依存していたパッケージには`webpack`、`eslint@4`、`babel-eslint`などがあり影響範囲が広がりました。

より正確な時間や影響範囲については次の記事を参照してください。

- [Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes "Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter")
- [2018/07/12 に発生したセキュリティ インシデント (eslint-scope@3.7.2) について - Qiita](https://qiita.com/mysticatea/items/0141657e4478d9cf4614 "2018/07/12 に発生したセキュリティ インシデント (eslint-scope@3.7.2) について - Qiita")

npmによれば4,500のnpmアカウントがこの問題の影響を受けたと推測されており、またこの問題の後にすべてのユーザーのnpmのアクセストークンを無効化しています。そのため、ほとんどのユーザーはもう一度`npm login`などをしてアクセストークンを再発行する必要があります。

- [The npm Blog — Incident report: npm, Inc. operations incident of...](https://blog.npmjs.org/post/175824896885/incident-report-npm-inc-operations-incident-of)

現在は問題のパッケージ（`eslint-scope@3.7.2`と`eslint-config-eslint@5.0.2`）はunpublishされているため、インストールする可能性はほぼありません。しかし、npmのregistryには[Artifactory](https://www.jfrog.com/confluence/display/RTF/Npm+Registry)などのミラーを利用しているユーザーもいるため、ミラーのregistryには残っている可能性もあるので確認してください。仮に実行した場合でも[eslint-scope attack](https://gist.github.com/hzoo/51cb84afdc50b14bffa6c6dc49826b3e)で解説されているように、実際の攻撃スクリプトがすでに利用できないため影響はほぼありません。

[Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes)の記事では、パッケージのメンテナー側の対策として2要素認証をする、パスワードを使い回さないなどの対策などについて書かれています。
またパッケージの利用する側の対策として`pacakge-lock.json`や`yarn.lock`などでパッケージのバージョンをロックして今回の問題のようなパッケージは自動的には入らないようにするといったことについて書かれています。

今回の攻撃に使われたパッケージのインストール時に`postinstall`のhookで悪意あるコードを実行するという手法は以前も同様の問題が報告されていました。この問題の対策の一環として[read-only tokenや2要素認証](https://blog.npmjs.org/post/166039777883/protect-your-npm-account-with-two-factor)が導入されていました。

- [The npm Blog — Package install scripts vulnerability](https://blog.npmjs.org/post/141702881055/package-install-scripts-vulnerability)

npmの2要素認証はユーザー単位であるため、メンテナーが複数人いる場合は全員が2要素認証を有効化していないと、パッケージ自体は攻撃の影響を受ける可能性があります。
そのため今回の問題をうけてnpmでは、ユーザーではなくパッケージごとに2要素認証を設定可能にすることやTime-limited tokensについての提案などが行われています。

- [The npm Blog — Two-factor authentication protection for packages](https://blog.npmjs.org/post/175861857230/two-factor-authentication-protection-for-packages)
- [Time-limited tokens - 💡 ideas - npm forum](https://npm.community/t/time-limited-tokens/502)

----


<h1 class="site-genre">ヘッドライン</h1>

----

## The npm Blog — v6.2.0
[blog.npmjs.org/post/175871462900/v620](https://blog.npmjs.org/post/175871462900/v620 "The npm Blog — v6.2.0")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">ReleaseNote</span></p>

npm 6.2.0リリース。
`npm audit`にawkなどでパースしやすい`--parseable`オプションの追加、` sign-git-commit`の設定を追加など


----

## Announcing TypeScript 3.0 RC | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/07/12/announcing-typescript-3-0-rc/](https://blogs.msdn.microsoft.com/typescript/2018/07/12/announcing-typescript-3-0-rc/ "Announcing TypeScript 3.0 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.0 RCリリース。
monorepo向けのサポートがメイン。
Project Referencesによりmonorepo内の別パッケージの型定義を参照できるようになり、Build modeによって関連するパッケージのビルドをインクリメンタルに行える。
tuples型の改善、`unknown`型の追加、Reactのdefault propsのサポートなど

- [TypeScript 3.0.0-RC 変更点 - Qiita](https://qiita.com/vvakame/items/57a0559c45b88b2ae168 "TypeScript 3.0.0-RC 変更点 - Qiita")

----

## Release v1.6.0 · GoogleChrome/puppeteer
[github.com/GoogleChrome/puppeteer/releases/tag/v1.6.0](https://github.com/GoogleChrome/puppeteer/releases/tag/v1.6.0 "Release v1.6.0 · GoogleChrome/puppeteer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Puppeteer v1.6.0リリース。
`page.waitForRequest`と`page.waitForResponse`のサポート。
要素が現在のviewportに表示されているかを判定する`elementHandle.isIntersectingViewport`の追加など


----

## Release 9.0 “A Mari Usque Ad Mare” · postcss/autoprefixer
[github.com/postcss/autoprefixer/releases/tag/9.0.0](https://github.com/postcss/autoprefixer/releases/tag/9.0.0 "Release 9.0 “A Mari Usque Ad Mare” · postcss/autoprefixer")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Autoprefixer 9.0、Browserslist 4.0、PostCSS 7.0.0リリース。
Node.js 4のサポート終了など


----

## Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes "Postmortem for Malicious Packages Published on July 12th, 2018 - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">node.js</span></p>

`.npmrc`の内容を盗み取る`eslint-scope@3.7.2`と`eslint-config-eslint@5.0.2`が公開された問題についてのレポート。
パスワードリスト攻撃で取られてたアカウントのtokenから直接publishされ、その後npm incによって全ユーザーのtokenがリセットされた。
攻撃手法や対策について

- [The npm Blog — Incident report: npm, Inc. operations incident of...](https://blog.npmjs.org/post/175824896885/incident-report-npm-inc-operations-incident-of "The npm Blog — Incident report: npm, Inc. operations incident of...")
- [2018/07/12 に発生したセキュリティ インシデント (eslint-scope@3.7.2) について - Qiita](https://qiita.com/mysticatea/items/0141657e4478d9cf4614 "2018/07/12 に発生したセキュリティ インシデント (eslint-scope@3.7.2) について - Qiita")

----
<h1 class="site-genre">アーティクル</h1>

----

## Site Isolation for web developers  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/07/site-isolation](https://developers.google.com/web/updates/2018/07/site-isolation "Site Isolation for web developers  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span></p>

Chrome 67でデフォルト有効化されたSite Isolationについて。
レンダラープロセスを分離することで、サイドチャネル攻撃やオリジン超えの攻撃によって機密情報が盗まれるのを防止する。
CORB、iframeなどにおけるloadとunloadにおける挙動の違いなどについて

- [Google Online Security Blog: Mitigating Spectre with Site Isolation in Chrome](https://security.googleblog.com/2018/07/mitigating-spectre-with-site-isolation.html "Google Online Security Blog: Mitigating Spectre with Site Isolation in Chrome")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## The CSS Paint API | CSS-Tricks
[css-tricks.com/the-css-paint-api/](https://css-tricks.com/the-css-paint-api/ "The CSS Paint API | CSS-Tricks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span></p>

CSS Paint APIについての記事。
新しいShapeの追加、カスタムプロパティとの連携方法について


----

## Life of a Pixel 2018 - Google スライド
[docs.google.com/presentation/d/1boPxbgNrTU0ddsc144rcXayGA\_WF53k96imRH8Mp34Y/mobilepresent#slide&#x3D;id.p](https://docs.google.com/presentation/d/1boPxbgNrTU0ddsc144rcXayGA_WF53k96imRH8Mp34Y/mobilepresent#slide=id.p "Life of a Pixel 2018 - Google スライド")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">slide</span></p>

Chromeのレンダリングの仕組みについてのスライド。
DOM、Style、Layout、Paint、Rasterization。
変更があったときに再レンダリングやCompositingなどの処理の流れなどについて。


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Vue.js Cheat Sheet
[flaviocopes.com/vue-cheat-sheet/](https://flaviocopes.com/vue-cheat-sheet/ "Vue.js Cheat Sheet")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">チートシート</span></p>

Vueチートシート


----

## Browsh
[www.brow.sh/](https://www.brow.sh/ "Browsh")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">console</span> <span class="jser-tag">firefox</span></p>

Firefoxをバックエンド(WebExtensions)に使ったテキストブラウザ。
CSSやWebGL、画像や動画などの描画結果をテキストベースで閲覧できる。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## dubzzz/fast-check: Property based testing framework for JavaScript (like QuickCheck) written in TypeScript
[github.com/dubzzz/fast-check](https://github.com/dubzzz/fast-check "dubzzz/fast-check: Property based testing framework for JavaScript (like QuickCheck) written in TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">TypeScript</span></p>

Property based testingを行うテストライブラリ。
値のパターンや組み合わせを定義してランダムな値を生成してテストできる。
またテストが失敗した際には`seed`値を使って同じ組み合わせを再現してテストできる。


----

## joshwcomeau/guppy
[github.com/joshwcomeau/guppy](https://github.com/joshwcomeau/guppy "joshwcomeau/guppy")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">GUI</span> <span class="jser-tag">Tools</span> <span class="jser-tag">software</span></p>

React向けのアプリケーション管理、タスク実行を行えるGUIアプリ。


----

## teadjs/tead: Lighting the way to simpler testing
[github.com/teadjs/tead](https://github.com/teadjs/tead "teadjs/tead: Lighting the way to simpler testing")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

シンプルなテストフレームワーク。
`[actual, expected]`の組み合わせを返すだけでテストできる。


----
<h1 class="site-genre">書籍関係</h1>

----

## Programming TypeScript: Making Your JavaScript Applications Scale: Boris Cherny: 9781492037651: Amazon.com: Books
[www.amazon.com/dp/1492037656/](https://www.amazon.com/dp/1492037656/ "Programming TypeScript: Making Your JavaScript Applications Scale: Boris Cherny: 9781492037651: Amazon.com: Books")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">book</span></p>

2019年4月4日発売
TypeScriptでのアプリケーション開発についての書籍


----
