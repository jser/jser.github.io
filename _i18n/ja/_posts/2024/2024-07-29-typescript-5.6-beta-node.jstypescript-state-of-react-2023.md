---
title: "2024-07-29のJS: TypeScript 5.6 Beta、Node.jsの実験的なTypeScriptサポート、State of React 2023"
author: "azu"
layout: post
date: 2024-07-29T01:18:59.277Z
category: JSer
tags:
- nodejs
- ECMAScript
- React
- TypeScript
- Conference

---

JSer.info #701 - TypeScript 5.6 Beta がリリースされました。

- [Announcing TypeScript 5.6 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/)

ESLintの`no-constant-binary-expression`と似たチェックを行い、常にtrue/nullishとなる間違った書き方をコンパイルエラーにする変更が含まれています。

- [Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2022/07/interesting-bugs-caught-by-no-constant-binary-expression/)

Iterator Helperのサポート、ES2022のArbitrary module namespace identifier namesをサポート、`--noUncheckedSideEffectImports`フラグの追加も行われています。
また、型チェックせずにファイルを出力できる`--noCheck`フラグの追加など

----

Node.jsに`--experimental-strip-types`という実験的なフラグが実装されています。

- [module: add --experimental-strip-types by marco-ippolito · Pull Request #53725 · nodejs/node](https://github.com/nodejs/node/pull/53725)

この`--experimental-strip-types`フラグを使うと、TypeScriptのコードから型情報を削除してJavaScriptファイルとして実行できるようになります。

[Node.jsのTypeScriptサポートについて](https://gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250)では、Node.jsのTypeScriptサポートがどのような経緯で進んできているかをまとめています。
まだ実験段階で課題となる点も多いため、正式にサポートされるかは分かりませんが、今後の方針は次のIssueで議論されています。

- [Roadmap for experimental TypeScript support · Issue #217 · nodejs/loaders](https://github.com/nodejs/loaders/issues/217)

----

[State of React 2023](https://2023.stateofreact.com/)が公開されました。
Reactに関する開発者アンケートの結果をまとめたレポートになっています。

Reactの機能、状態管理、データ取得、Meta-Framework、どのようなアプリケーションを作っているかについてなど色々な項目ごとの結果がまとめられています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node.js — Node v22.5.1 (Current)
[nodejs.org/en/blog/release/v22.5.1](https://nodejs.org/en/blog/release/v22.5.1 "Node.js — Node v22.5.1 (Current)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v22.5.1リリース。
Node.js v22.5.0に含まれていた`npm ci`などがクラッシュするリグレッションを修正

- [Fix the bug caused by fast api changes in v22.5.0 and have a post-mortem by anonrig · Pull Request #53934 · nodejs/node](https://github.com/nodejs/node/pull/53934?hss_channel=tw-91985735 "Fix the bug caused by fast api changes in v22.5.0 and have a post-mortem by anonrig · Pull Request #53934 · nodejs/node")

----

## Release pnpm 9.6 · pnpm/pnpm
[github.com/pnpm/pnpm/releases/tag/v9.6.0](https://github.com/pnpm/pnpm/releases/tag/v9.6.0 "Release pnpm 9.6 · pnpm/pnpm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">pnpm</span> <span class="jser-tag">ReleaseNote</span></p>

pnpm v9.6.0リリース。
`pnpm.executionEnv.nodeVersion`でNode.jsのバージョンを指定できるように。
`catalogs:`のサポートの改善や修正など


----

## It&#039;s official, Meteor 3.0 Official Release is out! - announce - Meteor.js forums
[forums.meteor.com/t/its-official-meteor-3-0-official-release-is-out/61860](https://forums.meteor.com/t/its-official-meteor-3-0-official-release-is-out/61860 "It&#039;s official, Meteor 3.0 Official Release is out! - announce - Meteor.js forums")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">nodejs</span></p>

Meteor.js 3.0リリース。
非同期の対応改善、Node.js 20のサポート、Expressのmiddlewareに対応など

- [Meteor 3.0 Migration Guide | Meteor 3.0 Migration Guide](https://v3-migration-docs.meteor.com/ "Meteor 3.0 Migration Guide | Meteor 3.0 Migration Guide")

----

## July 22, 2024 Release – React Spectrum Releases
[react-spectrum.adobe.com/releases/2024-07-22.html](https://react-spectrum.adobe.com/releases/2024-07-22.html "July 22, 2024 Release – React Spectrum Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

React Spectrum July 22, 2024リリース。
React 19 RCの対応、TableView/ListView/ListBoxのVirtualizationの改善、Toastのfocus managementの改善など。
アイコンをApache 2.0 Licenseに変更など


----

## A new path for Privacy Sandbox on the web
[privacysandbox.com/news/privacy-sandbox-update/](https://privacysandbox.com/news/privacy-sandbox-update/ "A new path for Privacy Sandbox on the web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">privacy</span> <span class="jser-tag">news</span></p>

Chromeの3rd Party Cookie廃止計画は撤回することになった。


----

## Sass: Node Sass is end-of-life
[sass-lang.com/blog/node-sass-is-end-of-life/](https://sass-lang.com/blog/node-sass-is-end-of-life/ "Sass: Node Sass is end-of-life")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">Sass</span> <span class="jser-tag">news</span></p>

LibSassのNode.jsラッパーであるNode Sassのサポートが終了された。
DartSassがアクティブメンテナンスされているため、そちらへの移行を推奨している


----

## Bun v1.1.21 | Bun Blog
[bun.sh/blog/bun-v1.1.21](https://bun.sh/blog/bun-v1.1.21 "Bun v1.1.21 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.1.21リリース。
`--fetch-preconnect=<url>`フラグの追加、Remixの対応改善、`bun build --packages=external`の追加など


----

## Node.js — Node v20.16.0 (LTS)
[nodejs.org/en/blog/release/v20.16.0](https://nodejs.org/en/blog/release/v20.16.0 "Node.js — Node v20.16.0 (LTS)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v20.16.0リリース。
`process.getBuiltinModule(id)`を追加、OpenSSLのカスタムエンジンサポートの廃止に伴い `clientCertEngine` オプションを非推奨に変更など


----

## Announcing TypeScript 5.6 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-6-beta/ "Announcing TypeScript 5.6 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.6 Betaリリース。
ESLintの`no-constant-binary-expression`と似た常にtrue/nullishとなる間違った書き方をエラーにする変更、Iterator Helperのサポート。
ES2022のArbitrary module namespace identifier namesをサポート、`--noUncheckedSideEffectImports`フラグの追加。
型チェックせずにファイルを出力できる`--noCheck`フラグの追加など

- [Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter](https://eslint.org/blog/2022/07/interesting-bugs-caught-by-no-constant-binary-expression/ "Interesting bugs caught by no-constant-binary-expression - ESLint - Pluggable JavaScript Linter")

----

## Astro 4.12: Server Islands | Astro
[astro.build/blog/astro-4120/](https://astro.build/blog/astro-4120/ "Astro 4.12: Server Islands | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 4.12リリース。
Next.jsのPartial Prerenderingに類似する機能としてServer Islandsを実験的に追加、`inferRemoteSize`の追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## CSS Grid Areas
[ishadeed.com/article/css-grid-area/](https://ishadeed.com/article/css-grid-area/ "CSS Grid Areas")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Gridについての解説。
grid-template-areasを使ったGridのレイアウト方法について色々な例とともに解説している


----

## State of React 2023
[2023.stateofreact.com/en-US](https://2023.stateofreact.com/en-US "State of React 2023")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Survey</span></p>

State of React 2023の結果が公開された。
Reactの機能、状態管理、データ取得、Meta-Framework、どのようなアプリケーションを作っているかについてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSConf Budapest 2024 - YouTube
[www.youtube.com/playlist?list&#x3D;PL37ZVnwpeshEczPCbFGVGd-hj1DR7\_SKy](https://www.youtube.com/playlist?list=PL37ZVnwpeshEczPCbFGVGd-hj1DR7_SKy "JSConf Budapest 2024 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JSConf Budapest 2024 の動画一覧

- [26-28 June, JSConfBP 2024](https://jsconfbp.com/ "26-28 June, JSConfBP 2024")

----

## Temporalを取り巻く仕様を整理する - Speaker Deck
[speakerdeck.com/sajikix/temporalwoqu-rijuan-kushi-yang-wozheng-li-suru](https://speakerdeck.com/sajikix/temporalwoqu-rijuan-kushi-yang-wozheng-li-suru "Temporalを取り巻く仕様を整理する - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">slide</span></p>

ECMAScript Proposal Stage 3のTemporalに関連する仕様についてのスライド。
ECMA-402、Unicode(CLDR)、IETF(BCP47/RFC3339/RFC9557)、IANA(Timezone)について


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Node.jsのTypeScriptサポートについて
[gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250](https://gist.github.com/azu/ac5dafbf211ef8b5ecf386930ac75250 "Node.jsのTypeScriptサポートについて")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">TypeScript</span></p>

Node.jsに実験的な機能としてTypeScriptのコードから型定義を取り除いてJavaScriptとして実行する`--experimental-strip-types`フラグが実装された経緯について


----
<h1 class="site-genre">書籍関係</h1>

----

## Exploring JavaScript (ES2024 Edition)
[exploringjs.com/js/index.html](https://exploringjs.com/js/index.html "Exploring JavaScript (ES2024 Edition)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

Exploring JavaScriptのES2024対応版が公開された


----
