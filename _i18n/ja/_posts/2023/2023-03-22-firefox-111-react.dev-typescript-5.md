---
title: "2023-03-22のJS: Firefox 111、react.dev、TypeScript 5"
author: "azu"
layout: post
date : 2023-03-22T03:54:32.412Z
category: JSer
tags:
- TypeScript
- node.js
- React
- npm
- Firefox

---

JSer.info #636 - Firefox 111がリリースされました。

- [Firefox 111.0, See All New Features, Updates and Fixes](https://www.mozilla.org/en-US/firefox/111.0/releasenotes/)
- [Firefox 111 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/111)

HTMLの`translate`属性をサポート、CSS color functionsをフラグ付きでサポートされています。
また、Safariと同じくFile System Access APIのOrigin private file system (OPFS)をサポートしています。

- [The File System API with Origin Private File System | WebKit](https://webkit.org/blog/12257/the-file-system-access-api-with-origin-private-file-system/)

----

Reactの新しいドキュメントサイトである [react.dev](https://react.dev/) がリリースされました。

- [Introducing react.dev – React](https://react.dev/blog/2023/03/16/introducing-react-dev)

ドメインが react.dev となり、React Hooksがデフォルトとなり、チュートリアルやAPIガイドも大きく書き直されています。
また、古いドキュメントは<https://legacy.reactjs.org/>で公開されています。

----

TypeScript 5.0が正式リリースされました。

- [Announcing TypeScript 5.0 - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/)

TypeScriptはsemverではないですが、メジャーアップデートと言えるような大きな変更が含まれています。


今まではECMAScript Stage 1相当のDecoratorでしたが、Stage 3のDecoratorがサポートされるようになりました。
`const` type parameterの追加、`tsconfig.json`で複数の`extends`に対応、enumとunion型の改善も行われています。

また、`--moduleResolution bundler`の追加と関連するオプションの追加、`exports`フィールドのConditionを指定できる`--customConditions`の追加。
`import`時に`type`修飾子を削除しそれ以外を残す`--verbatimModuleSyntax`オプションの追加、JSDocで`@satisfies`をサポートなども含まれています。

TypeScriptの内部的な変更としてTypeScriptのコードベースをnamespaceからmoduleに移行し、パフォーマンス/メモリ/パッケージサイズの改善されています。
namespaceからの以降については記事も公開されています。

- [TypeScript's Migration to Modules - TypeScript](https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/)

古くなった`--target ES3`や`--out`などのオプションを非推奨に変更し、`--forceConsistentCasingInFileNames`をデフォルトで`true`に変更するといった変更も含まれています。



----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Firefox 111.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/111.0/releasenotes/](https://www.mozilla.org/en-US/firefox/111.0/releasenotes/ "Firefox 111.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 111リリース。
HTMLの`translate`属性をサポート、CSS color functionsをフラグ付きでサポート。
File System Access APIのOrigin private file system (OPFS)をサポートなど

- [Firefox 111 for developers - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/111 "Firefox 111 for developers - Mozilla | MDN")

----

## Node v19.8.0 (Current) | Node.js
[nodejs.org/en/blog/release/v19.8.0](https://nodejs.org/en/blog/release/v19.8.0 "Node v19.8.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v19.8.0リリース。
`Buffer.copyBytesFrom()`の追加、`AsyncLocalStorage.bind()`と`AsyncLocalStorage.snapshot()`の追加。
`fs.openAsBlob()`の追加、`URLSearchParams`に`size` getterの追加、WASIに`version`を追加など


----

## vite/CHANGELOG.md at main · vitejs/vite
[github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#420-2023-03-16](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#420-2023-03-16 "vite/CHANGELOG.md at main · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite 4.2.0リリース。
HTMLファイル内で`%ENV_NAME%`での環境変数の置換に対応、Source Mapsの改善、`exports`フィールドのSubpath importsに対応。
TypeScript 5のサポートとesbuild 0.17へのアップデートなど


----

## Introducing react.dev – React
[react.dev/blog/2023/03/16/introducing-react-dev](https://react.dev/blog/2023/03/16/introducing-react-dev "Introducing react.dev – React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">document</span> <span class="jser-tag">news</span></p>

Reactの新しいドキュメントサイトである react.dev が公開された。
ドメインが react.dev となり、React Hooksがデフォルトとなり、チュートリアルやAPIガイドも書き直されている。


----

## Announcing TypeScript 5.0 - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0/ "Announcing TypeScript 5.0 - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.0リリース。
ECMAScript Stage 3のDecoratorを実装、`const` type perameterの追加、`tsconfig.json`で複数の`extends`に対応、enumとunion型の改善。
`--moduleResolution bundler`の追加と関連するオプションの追加、`exports`フィールのConditionを指定できる`--customConditions`の追加。
`import`時に`type`修飾子を削除しそれ以外を残す`--verbatimModuleSyntax`オプションの追加、JSDocで`@satisfies`をサポートなど。
また、TypeScriptのコードベースをnamespaceからmoudleに移行し、パフォーマンス/メモリ/パッケージサイズの改善。
`--target ES3`や`--out`などのオプションを非推奨に変更し、`--forceConsistentCasingInFileNames`をデフォルトでtrueに変更するといった変更も含まれている


----

## styled-components/xstyled: A utility-first CSS-in-JS framework built for React. 💅👩‍🎤⚡️
[github.com/styled-components/xstyled](https://github.com/styled-components/xstyled "styled-components/xstyled: A utility-first CSS-in-JS framework built for React. 💅👩‍🎤⚡️")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">news</span></p>

xstyledがstyled-componentsのorganizationに移管された

- [Evan Jacobs on Twitter: &amp;quot;Excited to announce that xstyled is now part of the styled-components organization and we will begin to cross-pollinate improvements in the near future! Thank you so much @neoziro! https://t.co/uPk4sR9QsS&amp;quot; / Twitter](https://twitter.com/probablyup/status/1632385154814558210 "Evan Jacobs on Twitter: &amp;amp;quot;Excited to announce that xstyled is now part of the styled-components organization and we will begin to cross-pollinate improvements in the near future! Thank you so much @neoziro! https://t.co/uPk4sR9QsS&amp;amp;quot; / Twitter")

----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing &quot;safe npm&quot;, a Socket npm Wrapper - Socket
[socket.dev/blog/introducing-safe-npm](https://socket.dev/blog/introducing-safe-npm "Introducing \&quot;safe npm\&quot;, a Socket npm Wrapper - Socket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span> <span class="jser-tag">security</span></p>

`npm`と`npx`にaliasして利用できるコマンド。
インストール時にパッケージがマルウェアかインストール時にスクリプト実行するかなどをチェックしてからインストールできる

- [socket npm &amp;amp; socket npx](https://docs.socket.dev/docs/socket-npm-socket-npx "socket npm &amp;amp;amp; socket npx")

----

## npm installとnpm ciの動作確認を簡単にやっておいた - Mitsuyuki.Shiiba
[bufferings.hatenablog.com/entry/2023/03/21/145023](https://bufferings.hatenablog.com/entry/2023/03/21/145023 "npm installとnpm ciの動作確認を簡単にやっておいた - Mitsuyuki.Shiiba")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">article</span> <span class="jser-tag">CI</span></p>

npm installとnpm ciとキャッシュについて。
`npm install`は`node_modules/`を再利用できるが、安全ではないケースもある。
`npm ci`は`node_modules/`を削除するため`~/.npm`をキャッシュとして使う必要があることについて。

- [npm install と npm ci って結局どう使うの？2023年版 - Mitsuyuki.Shiiba](https://bufferings.hatenablog.com/entry/2023/03/15/215044 "npm install と npm ci って結局どう使うの？2023年版 - Mitsuyuki.Shiiba")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## lagonapp/lagon: Deploy Serverless Functions at the Edge. Current status: Dev
[github.com/lagonapp/lagon](https://github.com/lagonapp/lagon "lagonapp/lagon: Deploy Serverless Functions at the Edge. Current status: Dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">Rust</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">OpenSource</span></p>

V8とRustで書かれているJavaScriptランタイム。


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----


## total-typescript/ts-reset: A &#039;CSS reset&#039; for TypeScript, improving types for common JavaScript API&#039;s
[github.com/total-typescript/ts-reset](https://github.com/total-typescript/ts-reset "total-typescript/ts-reset: A &#039;CSS reset&#039; for TypeScript, improving types for common JavaScript API&#039;s")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

TypeScriptのlibsの型定義を上書きする型定義ライブラリ。
`JSON.parse`が`any`ではなく`unknown`を返すように変更したり、`.includes()`や`.has()`の型を厳密にするなどしている


----

## anymaniax/orval: orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺
[github.com/anymaniax/orval](https://github.com/anymaniax/orval "anymaniax/orval: orval is able to generate client with appropriate type-signatures (TypeScript) from any valid OpenAPI v3 or Swagger v2 specification, either in yaml or json formats. 🍺")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">OpenAPI</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">React</span> <span class="jser-tag">Tools</span> <span class="jser-tag">library</span></p>

OpenAPI SpecからAPIクライアントやモックサーバなどのコードを生成するツール。

- [OpenAPIからコードを自動生成！『Orval』のメリットと選定理由](https://zenn.dev/hrbrain/articles/3ca5d37dd0b80e "OpenAPIからコードを自動生成！『Orval』のメリットと選定理由")

----

## gajus/turbowatch: Extremely fast file change detector and task orchestrator for Node.js.
[github.com/gajus/turbowatch](https://github.com/gajus/turbowatch "gajus/turbowatch: Extremely fast file change detector and task orchestrator for Node.js.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

ファイルの変更を監視して、プロセスを再起動するライブラリ、ツール。


----

## Transformers.js
[xenova.github.io/transformers.js/](https://xenova.github.io/transformers.js/ "Transformers.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">MachineLearning</span></p>

ブラウザ上で動くTransformersライブラリ。
HuggingFace Hubからのモデルのダウンロードに対応していて、BERTなどさまざまモデルでタスクを実行できる


----
<h1 class="site-genre">書籍関係</h1>

----

## Practical WebAssembly \[Book\]
[www.oreilly.com/library/view/practical-webassembly/9781098142513/](https://www.oreilly.com/library/view/practical-webassembly/9781098142513/ "Practical WebAssembly \[Book\]")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">book</span></p>

2024年5月発売
WebAssemblyについての書籍。
RustとAssemblyScriptでWasmを作成して利用する方法について


----
