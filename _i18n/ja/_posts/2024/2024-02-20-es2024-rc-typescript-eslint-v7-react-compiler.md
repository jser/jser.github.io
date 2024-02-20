---
title: "2024-02-20のJS: ES2024 RC、typescript-eslint v7、React Compiler"
author: "azu"
layout: post
date: 2024-02-20T06:11:26.320Z
category: JSer
tags:
- TypeScript
- ECMAScript
- React
- nodejs
- HTTP

---

JSer.info #681 - - [Release ES2024 Candidate February 2024 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02)
- [Editorial: Describe changes in ES2024 by bakkot · Pull Request #3282 · tc39/ecma262](https://github.com/tc39/ecma262/pull/3282)
- [ECMAScript proposal updates @ 2024-02 | ECMAScript Daily](https://ecmascript-daily.github.io/ecmascript/2024/02/15/ecmascript-proposal-update)

---

- [Announcing typescript-eslint v7 | typescript-eslint](https://typescript-eslint.io/blog/announcing-typescript-eslint-v7/)

----

- [React Labs: What We've Been Working On – February 2024 – React](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release Release v0.28.0 · axios/axios
[github.com/axios/axios/releases/tag/v0.28.0](https://github.com/axios/axios/releases/tag/v0.28.0 "Release Release v0.28.0 · axios/axios")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">HTTP</span> <span class="jser-tag">library</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Axios v0.28.0リリース。
Axios v1.6.0で修正されたCSRFトークンの問題をバックポート。その他にもv1.x系での修正をバックポートしている。


----

## Announcing typescript-eslint v7 | typescript-eslint
[typescript-eslint.io/blog/announcing-typescript-eslint-v7/](https://typescript-eslint.io/blog/announcing-typescript-eslint-v7/ "Announcing typescript-eslint v7 | typescript-eslint")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

typescript-eslint v7リリース。
Node.js 16のサポート終了、ESLint Flat Configをサポートする`typescript-eslint`パッケージを追加。


----

## ECMAScript proposal updates @ 2024-02 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2024/02/15/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2024/02/15/ecmascript-proposal-update "ECMAScript proposal updates @ 2024-02 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2024年2月のTC39ミーティングでのProposalの変更まとめ。
Stage 2.7というステージが新しく追加された。
`ArrayBuffer.prototype.transfer`はStage 4となりES2024に含まれることが決まった


----

## Release ES2024 Candidate February 2024 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02](https://github.com/tc39/ecma262/releases/tag/es2024-candidate-2024-02 "Release ES2024 Candidate February 2024 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">spec</span> <span class="jser-tag">ReleaseNote</span></p>

ECMAScript 2024候補のリリース。
`ArrayBuffer.prototype.resize`/`ArrayBuffer.prototype.transfer`、RegExpの`v`フラグの追加。
`Promise.withResolvers`、`Object.groupBy`/`Map.groupBy`の追加。
`Atomics.waitAsync`、`String.prototype.isWellFormed`/`String.prototype.toWellFormed`の追加など

- [Editorial: Describe changes in ES2024 by bakkot · Pull Request #3282 · tc39/ecma262](https://github.com/tc39/ecma262/pull/3282 "Editorial: Describe changes in ES2024 by bakkot · Pull Request #3282 · tc39/ecma262")

----

## Bun v1.0.27 | Bun Blog
[bun.sh/blog/bun-v1.0.27](https://bun.sh/blog/bun-v1.0.27 "Bun v1.0.27 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.27リリース。
`Response`がAsync generatorとNode.jsの`Readable`をサポート、Bun Shellの改善など。
また、Bun Shellのエラー時のexit codeはv1.1では`1`となる変更が入る予定。


----

## htmz - a low power tool for html
[leanrada.com/htmz/](http://leanrada.com/htmz/ "htmz - a low power tool for html")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

htmxのようにHTMLで宣言的にAjax的な表示を行う小さなスニペット。
`<form action="/default#my-target" target=htmz>`と指定しリクエスト結果を用意した`<iframe name=htmz>`に表示する。
iframeの描画結果を`#my-target`の要素と置換する仕組みなっている。


----

## Node.js — Wednesday February 14 2024 Security Releases
[nodejs.org/en/blog/vulnerability/february-2024-security-releases](https://nodejs.org/en/blog/vulnerability/february-2024-security-releases "Node.js — Wednesday February 14 2024 Security Releases")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">secu</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのセキュリティアップデートとしてNode.js 20.x, 18.x, 21.xをそれぞれ更新。
OpenSSLの更新、Linuxのcapabilitiesに関するバグの修正、細工したHTTPリクエストでのDosに関する問題、パーミッションモデルの問題の修正など


----

## Redwood v7.0.0 Upgrade Guide - Announcements / Releases and Upgrade Guides - RedwoodJS Community
[community.redwoodjs.com/t/redwood-v7-0-0-upgrade-guide/5713](https://community.redwoodjs.com/t/redwood-v7-0-0-upgrade-guide/5713 "Redwood v7.0.0 Upgrade Guide - Announcements / Releases and Upgrade Guides - RedwoodJS Community")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Redwood v7リリース。
Node.js 18のサポート終了、`prop-types`パッケージの依存を削除、dbAuthのセキュリティ改善に伴う破壊的な変更など

- [Release v7.0.0 · redwoodjs/redwood](https://github.com/redwoodjs/redwood/releases/tag/v7.0.0 "Release v7.0.0 · redwoodjs/redwood")

----
<h1 class="site-genre">アーティクル</h1>

----

## React Labs: What We&#039;ve Been Working On – February 2024 – React
[react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024](https://react.dev/blog/2024/02/15/react-labs-what-we-have-been-working-on-february-2024 "React Labs: What We&#039;ve Been Working On – February 2024 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Compiler(aka. React Forgot)がinstagramの本番環境で利用され、今後数ヶ月以内に公開される予定。
また、次のメジャーバージョンであるReact 19に必要な機能が揃ったため、公開の準備を進めていくという話


----

## A novel technique for creating ergonomic and tree-shakable TypeScript libraries
[softwaremill.com/a-novel-technique-for-creating-ergonomic-and-tree-shakable-typescript-libraries/](https://softwaremill.com/a-novel-technique-for-creating-ergonomic-and-tree-shakable-typescript-libraries/ "A novel technique for creating ergonomic and tree-shakable TypeScript libraries")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

必要なメソッドを集める初期化とProxyオブジェクトを使うことで、zodのようにメソッドチェーンが可能でかつTree Shakingも可能なライブラリを作る方法について。
小さなバリデーションライブラリを例に作り方や仕組みについてを解説してる。

- [mieszkosabo/correttore](https://github.com/mieszkosabo/correttore "mieszkosabo/correttore")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JollyUI
[www.jollyui.dev/](https://www.jollyui.dev/ "JollyUI")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

React Ariaを使ったshadcn/ui互換を目指すコンポーネント集


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Tempo • Dates by FormKit
[tempo.formkit.com/](https://tempo.formkit.com/ "Tempo • Dates by FormKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">i18n</span> <span class="jser-tag">library</span></p>

Intlオブジェクトベースの日付操作ライブラリ


----

## kolodny/safetest
[github.com/kolodny/safetest?tab&#x3D;readme-ov-file](https://github.com/kolodny/safetest?tab=readme-ov-file "kolodny/safetest")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">browser</span> <span class="jser-tag">E2E</span> <span class="jser-tag">library</span></p>

Netflixで利用しているコンポーネントフレームワーク。
Playwright、Vitest/Jestなどのテストフレームワーク、ReactやVueなどのUIフレームワークを組み合わたテストを行う。
アプリケーションレベルのDIコンテナやテストのセットアップをコードで柔軟にした状態でPlaywrightを使ったテストを行う。

- [Introducing SafeTest: A Novel Approach to Front End Testing | by Netflix Technology Blog | Feb, 2024 | Netflix TechBlog](https://netflixtechblog.com/introducing-safetest-a-novel-approach-to-front-end-testing-37f9f88c152d "Introducing SafeTest: A Novel Approach to Front End Testing | by Netflix Technology Blog | Feb, 2024 | Netflix TechBlog")

----

## pashak09/ts-expect-error-validator: Command-line tool to validate expected TypeScript errors
[github.com/pashak09/ts-expect-error-validator](https://github.com/pashak09/ts-expect-error-validator "pashak09/ts-expect-error-validator: Command-line tool to validate expected TypeScript errors")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">test</span> <span class="jser-tag">Tools</span></p>

`@ts-expect-error`には指定したエラーコードだけを無視する機能はないため、`@ts-expect-error [Code]`のコメントで指定したエラーが起きるかをチェックできるツール。


----
<h1 class="site-genre">書籍関係</h1>

----

## Next.js超入門 - 秀和システム あなたの学びをサポート！
[www.shuwasystem.co.jp/book/9784798071299.html](https://www.shuwasystem.co.jp/book/9784798071299.html "Next.js超入門 - 秀和システム あなたの学びをサポート！")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">ebook</span></p>

Next.jsの入門書


----
