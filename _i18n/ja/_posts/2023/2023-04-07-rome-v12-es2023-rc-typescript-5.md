---
title: "2023-04-07のJS: Rome v12、ES2023 RC、TypeScript 5で追加されたオプション"
author: "azu"
layout: post
date : 2023-04-06T15:01:39.093Z
category: JSer
tags:
- React
- Tools
- TypeScript
- node.js
- Next.js

---

JSer.info #638 - Rome v12がリリースされました。

- [Announcing Rome v12](https://rome.tools/blog/2023/03/28/rome12/)

JSONのサポート、TypeScript 5.0のサポート、フラグ付きでImportのソートに対応にしています。
また、エラー表示の改善や`--config-path`フラグの追加なども行われています。

----

ECMAScript 2023のリリース候補版(Candidate)が公開されました。

- [Release ES2023 Candidate April 2023 · tc39/ecma262](https://github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04)

6月に行われるEcma GA(総会)で承認を得ると正式にES2023としてリリースされます。
リリースされたかは次のニュースページに掲載されます。

- [News - Ecma International](https://www.ecma-international.org/news/)

また、ECMAScriptはLiving Standardなので、現在のmainブランチはES2024に入る内容がコミットされていきます。

- [Editorial: main is now ES2024 · tc39/ecma262@e356adc](https://github.com/tc39/ecma262/commit/e356adc0545a1a6409c69e41b9626ad3493f6bc8)

ECMAScriptの策定プロセスについては、次のページを参照してください。

- [The TC39 Process](https://tc39.es/process-document/)
- [ECMAScript · JavaScript Primer #jsprimer](https://jsprimer.net/basic/ecmascript/)

----

[TypeScript 5.0](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/)ではDecoratorのアップデートなど様々な変更が含まれています。
その中で、TypeScriptの`tsconfig.json`で設定できるオプションにも色々と追加されています。

次の記事は、新しく追加された`moduleResolution: Bundler`、`verbatimModuleSyntax`オプションについて解説しています。

- [TypeScript で"moduleResolution": "Node"は使わないほうがいい](https://blog.s2n.tech/articles/dont-use-moduleresolution-node)
- [TypeScript 5.0 で追加された verbatimModuleSyntax とは何か？](https://zenn.dev/teppeis/articles/2023-04-typescript-5_0-verbatim-module-syntax)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v16.20.0 (LTS) | Node.js
[nodejs.org/en/blog/release/v16.20.0](https://nodejs.org/en/blog/release/v16.20.0 "Node v16.20.0 (LTS) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v16.20.0リリース。
undici、npm、corepackのアップデート


----

## Announcing Rome v12
[rome.tools/blog/2023/03/28/rome12/](https://rome.tools/blog/2023/03/28/rome12/ "Announcing Rome v12")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Rome v12リリース。
JSONのサポート、TypeScript 5.0のサポート、フラグ付きでImportのソートに対応。
エラー表示の改善や`--config-path`フラグの追加など


----

## Release v1.7.0 - U Can&#039;t Type This · solidjs/solid
[github.com/solidjs/solid/releases/tag/v1.7.0](https://github.com/solidjs/solid/releases/tag/v1.7.0 "Release v1.7.0 - U Can&#039;t Type This · solidjs/solid")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">React</span> <span class="jser-tag">ReleaseNote</span></p>

Solid v1.7.0リリース。
TypeScriptのより厳密な型で書けるように改善、`onError`を置き換える`catchError`の追加など


----

## Release ES2023 Candidate April 2023 · tc39/ecma262
[github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04](https://github.com/tc39/ecma262/releases/tag/es2023-candidate-2023-04 "Release ES2023 Candidate April 2023 · tc39/ecma262")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">spec</span></p>

ECMAScript 2023 Candidateリリース。
6月のEcma GAで承認されたら正式にリリースされる。


----

## Bun v0.5.9 | Bun Blog
[bun.sh/blog/bun-v0.5.9](https://bun.sh/blog/bun-v0.5.9 "Bun v0.5.9 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun 0.5.9リリース。
ファイル変更を監視してプロセスを再起動する`bun --watch`のサポート、tarballの依存をサポート、バグ修正など。
0.6.0ではReact Server Componentsをサポートする予定。


----

## Electron 24.0.0 | Electron
[www.electronjs.org/blog/electron-24-0](https://www.electronjs.org/blog/electron-24-0 "Electron 24.0.0 | Electron")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Electron</span> <span class="jser-tag">ReleaseNote</span></p>

Electron 24.0.0リリース。
Chromium 112.0.5615.49、Node.js 18.12.1、V8 11.0へのアップデート。
`nativeImage.createThumbnailFromPath(path, size)`の`maxSize`オプションを`size`オプションへ変更など


----

## Release Notes for Safari Technology Preview 167 | WebKit
[webkit.org/blog/14100/release-notes-for-safari-technology-preview-167/](https://webkit.org/blog/14100/release-notes-for-safari-technology-preview-167/ "Release Notes for Safari Technology Preview 167 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 167リリース。
CSS NestingでのTop Level `&`をサポート、Priority Hintsのサポートなど


----
<h1 class="site-genre">アーティクル</h1>

----

## React Labs: What We&#039;ve Been Working On – March 2023 – React
[react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023 "React Labs: What We&#039;ve Been Working On – March 2023 – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Labsで進めているプロジェクトについて。
React Server Componentsで"use client"ディレクティブを使うようになり、サーバコンポーネントではasync/awaitを利用できるようになる予定。
SuspenseでのCSSやFontのロード、`<meta>`などのビルドインサポート、Reactの最適化コンパイラの開発状況などについて


----

## RailsアプリのフロントエンドをじわじわとNext.jsにリプレースした話と、その振り返り - High Link テックブログ
[tech.high-link.co.jp/entry/Rails-application-replace-Next.js](https://tech.high-link.co.jp/entry/Rails-application-replace-Next.js "RailsアプリのフロントエンドをじわじわとNext.jsにリプレースした話と、その振り返り - High Link テックブログ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">rails</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

NginxでパスごとにRailsからNext.jsへリクエストを切り替えながら、移行していったという話。
認証の問題、`<Link>`によるフロントエンドのルーティングとの齟齬の問題など移行時の対応について


----

## CSS text-wrap: balance - Chrome Developers
[developer.chrome.com/en/blog/css-text-wrap-balance/](https://developer.chrome.com/en/blog/css-text-wrap-balance/ "CSS text-wrap: balance - Chrome Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chromeにフラグ付きで実装されているCSS `text-wrap: balance`について。
テキストブロックの改行位置を調整するタイポグラフィ用のプロパティ


----

## What are source maps?
[web.dev/source-maps/](https://web.dev/source-maps/ "What are source maps?")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">sourcemap</span> <span class="jser-tag">article</span> <span class="jser-tag">debug</span></p>

Source Mapsとは何かについて。
Source Mapsのフォーマット、読み方、ツールでのサポート、`x_google_ignoreList`の独自拡張などについて

- [The \`x\_google\_ignoreList\` source map extension - Chrome Developers](https://developer.chrome.com/en/articles/x-google-ignore-list/ "The \&#x60;x\_google\_ignoreList\&#x60; source map extension - Chrome Developers")

----

## TypeScript 5.0 で追加された verbatimModuleSyntax とは何か？
[zenn.dev/teppeis/articles/2023-04-typescript-5\_0-verbatim-module-syntax](https://zenn.dev/teppeis/articles/2023-04-typescript-5_0-verbatim-module-syntax "TypeScript 5.0 で追加された verbatimModuleSyntax とは何か？")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 5.0で追加された`verbatimModuleSyntax`について。
`import type`をそのまま削除し、`import`は残すというシンプルな動作について


----

## TypeScript で&quot;moduleResolution&quot;: &quot;Node&quot;は使わないほうがいい
[blog.s2n.tech/articles/dont-use-moduleresolution-node](https://blog.s2n.tech/articles/dont-use-moduleresolution-node "TypeScript で\&quot;moduleResolution\&quot;: \&quot;Node\&quot;は使わないほうがいい")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの`moduleResolution`オプションに指定できる`Node`/`NodeNext`/`Bundler`の挙動の違いについて


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## lxsmnsyc/seroval: Stringify JS values
[github.com/lxsmnsyc/seroval](https://github.com/lxsmnsyc/seroval "lxsmnsyc/seroval: Stringify JS values")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JavaScriptのオブジェクトをJavaScriptのコードやJSONのシリアライズ/デシリアライズするライブラリ。
シリアライズするかを機能ごとの無効化するオプションを持っている


----

## wantedly/react-declassify: say goodbye to class components
[github.com/wantedly/react-declassify](https://github.com/wantedly/react-declassify "wantedly/react-declassify: say goodbye to class components")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

ReactのクラスコンポーネントをHooksを使うように変換するツール


----

## unjs/magicast: 🧀 Programmatically modify JavaScript and TypeScript source codes with a simplified, elegant and familiar syntax powered by recast and babel.
[github.com/unjs/magicast](https://github.com/unjs/magicast "unjs/magicast: 🧀 Programmatically modify JavaScript and TypeScript source codes with a simplified, elegant and familiar syntax powered by recast and babel.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">AST</span> <span class="jser-tag">library</span></p>

JavaScriptのAST操作を簡単に行うためのライブラリ。


----
