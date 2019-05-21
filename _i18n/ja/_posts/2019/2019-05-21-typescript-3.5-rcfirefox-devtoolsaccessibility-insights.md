---
title: "2019-05-21のJS: TypeScript 3.5 RC、Firefox DevTools改善、Accessibility Insights(アクセシビリティテスト) "
author: "azu"
layout: post
date : 2019-05-21T02:19:30.305Z
category: JSer
tags:
- TypeScript
- Firefox
- Accessibility

---

JSer.info #436 - TypeScript 3.5 RCがリリースされました。

- [Announcing TypeScript 3.5 RC | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/)
- [TypeScript 3.5 Iteration Plan · Issue #30555 · microsoft/TypeScript](https://github.com/Microsoft/TypeScript/issues/30555)
- [Breaking Changes · microsoft/TypeScript Wiki](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-35)

型チェックと`--incremental`オプションを使ったビルドのパフォーマンス改善がされています。
また、`Omit`ヘルパー型が`lib.d.ts`に追加、Union型におけるプロパティチェックの改善なども行われています。

破壊的な変更としてGeneric type parameterのデフォルトが`{}`から`unknown`へと変更されています。

3.4までは次のようなコードにおける`T`は何も`extends`していない場合は`{}`として解決されていました。
3.5からは`T`が`unknown`型として解決されるようになります。

```ts
function foo<T>(x: T): [T, string] {
    return [x, x.toString()]
    //           ~~~~~~~~ error! Property 'toString' does not exist on type 'T'.
}
```

簡単なワークアラウンドとしては明示的に`T`のデフォルトを`{}`型にすることです。

```ts
function foo<T extends {}>(x: T): [T, string] {
    return [x, x.toString()]
}
```

また、`tsconfig.json`で`target:es5`の場合に`Object.keys`がプリミティブ型を受け入れないように修正されました。
これは、ES5までは`Object.keys(10)`のようなコードは例外が発生するのがECMAScriptの仕様だったため、それに合わせる修正です。
一方で、ES2015からは`Object.keys(10)`は例外が発生しないのがECMAScriptの仕様なので、TypeScriptもそれに合わせています。

- [Break the Web: Object staticメソッドがES6で仕様変更になった件について](https://gist.github.com/teppeis/c50743a60832560aa1df)

それ以外にも細かい破壊的な変更があるので詳しくは[Breaking Changes](https://github.com/Microsoft/TypeScript/wiki/Breaking-Changes#typescript-35)を参照してください。

----

[Accessibility Insights](https://accessibilityinsights.io/)というウェブサイトやWindowsアプリケーションのアクセシビリティテストツールが公開されています。
ウェブ向けではChromeや[macOS版も公開された](https://blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/)MSEdgeのInside Preview向けのブラウザ拡張が公開されています。

FastPassとAssessmentの2つのシナリオでのアクセシビリティのテストをサポートしていて、自動チェックとシナリオ元にした手動チェックを行えます。
また、Tabキーのフォーカス移動の可視化、カラーテスト、WAI-ARIAのLandmarks表示などアクセシビリティテストの補助機能も用意されています。

次のページで使い方などが解説されているので、興味がある人は見てみるとよさそうです。

- [Accessibility Insights for Web · Accessibility Insights](https://accessibilityinsights.io/docs/en/web/overview)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v3.14.0 · lerna/lerna
[github.com/lerna/lerna/releases/tag/v3.14.0](https://github.com/lerna/lerna/releases/tag/v3.14.0 "Release v3.14.0 · lerna/lerna")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

monorepo管理ツールのlerna 3.14.0リリース。
npm publish時の2要素認証(OTP)のサポート、`--conventional-prerelease`と`--conventional-graduate`のサポートなど


----

## Release v2.7.0 · nuxt/nuxt.js
[github.com/nuxt/nuxt.js/releases/tag/v2.7.0](https://github.com/nuxt/nuxt.js/releases/tag/v2.7.0 "Release v2.7.0 · nuxt/nuxt.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js 2.7.0リリース。
サーバサイドのログもブラウザコンソールに表示されるように、`store/`ディレクトリのファイル監視の改善など

- [Nuxt.js v2.7.0 の変更点と注目のポイントまとめ - Qiita](https://qiita.com/potato4d/items/43b4f17c73aebc7a2154 "Nuxt.js v2.7.0 の変更点と注目のポイントまとめ - Qiita")

----

## Announcing TypeScript 3.5 RC | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-3-5-rc/ "Announcing TypeScript 3.5 RC | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.5 RCリリース。
型チェックとビルドのパフォーマンス改善、`Omit`ヘルパー型を追加、Union型の改善など。
破壊的な変更としてGeneric type parameterのデフォルトが`{}`から`unknown`へと変更、`target:es5`時に`Object.keys`がプリミティブ型を受け取らないように変更など


----

## V8 release v7.5 · V8
[v8.dev/blog/v8-release-75](https://v8.dev/blog/v8-release-75 "V8 release v7.5 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 v7.5リリース。
WebAssemblyのコンパイル結果を暗黙的にキャッシュする変更、ECMAScript ProposalのNumeric separatorsを実装。
ネットワークからスクリプトを読み込みながらパースする際に、メインスレッドによってブロックされる問題を解消など


----

## Release Notes for Safari Technology Preview 82 | WebKit
[webkit.org/blog/8921/release-notes-for-safari-technology-preview-82/](https://webkit.org/blog/8921/release-notes-for-safari-technology-preview-82/ "Release Notes for Safari Technology Preview 82 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 82リリース。
Fetch APIの`keepAlive`オプションのサポート、Web GPU APIを`navigator.gpu`に移動など


----

## Introducing the first Microsoft Edge preview builds for macOS - Microsoft Edge Blog
[blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/](https://blogs.windows.com/msedgedev/2019/05/20/microsoft-edge-macos-canary-preview/ "Introducing the first Microsoft Edge preview builds for macOS - Microsoft Edge Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">mac </span> <span class="jser-tag">ReleaseNote</span></p>

MSEdgeのmacOS対応版がInsider Previewでリリースされた


----
<h1 class="site-genre">アーティクル</h1>

----

## TypeScript 3.0: The unknown Type — Marius Schulz
[mariusschulz.com/blog/typescript-3-0-the-unknown-type](https://mariusschulz.com/blog/typescript-3-0-the-unknown-type "TypeScript 3.0: The unknown Type — Marius Schulz")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 3.0で導入された`unknown` typeについての解説。
`any` typeとの違い、`unknown` typeに対して任意の操作ができない点、`unknown` typeは型を絞り込んでから使う点について


----

## Faster smarter JavaScript debugging in Firefox DevTools - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/05/faster-smarter-javascript-debugging-in-firefox/](https://hacks.mozilla.org/2019/05/faster-smarter-javascript-debugging-in-firefox/ "Faster smarter JavaScript debugging in Firefox DevTools - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">firefox</span> <span class="jser-tag">debug</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Firefox 67の開発者ツールの改善点について。
ロードパフォーマンスの改善、Break Pointの改善やLog Pointの対応、Web Workerスクリプトとの切り替えを改善、Source Mapを使った細かい表示の改善など


----

## const assertions are the killer new TypeScript feature
[blog.logrocket.com/const-assertions-are-the-killer-new-typescript-feature-b73451f35802](https://blog.logrocket.com/const-assertions-are-the-killer-new-typescript-feature-b73451f35802 "const assertions are the killer new TypeScript feature")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScript 3.4で導入されたconst assertionについて。
リテラルの型拡大を防いだり、オブジェクトのプロパティを`readonly`にできるなど


----

## Google Fonts is Adding font-display 🎉—zachleat.com
[www.zachleat.com/web/google-fonts-display/](https://www.zachleat.com/web/google-fonts-display/ "Google Fonts is Adding font-display 🎉—zachleat.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">google</span> <span class="jser-tag">fonts</span> <span class="jser-tag">article</span></p>

Google Fontsが`display`パラメータで`font-display`プロパティの指定をサポートしたことについて。

- [display=swapとはなにか - MOL](https://t32k.me/mol/log/font-display-swap/ "display&#x3D;swapとはなにか - MOL")

----

## \[Web フロントエンド\] 状態更新ロジックをフレームワークから独立させる | Kabuku Developers Blog
[www.kabuku.co.jp/developers/framework-agnostic-state-modification](https://www.kabuku.co.jp/developers/framework-agnostic-state-modification "\[Web フロントエンド\] 状態更新ロジックをフレームワークから独立させる | Kabuku Developers Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

immerを使ったステート更新ロジックに分け、Angular、Vue、Reactなどのフレームワーク内に組み込む方法について。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JSでDoSる/ Shibuya.XSS techtalk #11 - Speaker Deck
[speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-11?slide&#x3D;6](https://speakerdeck.com/masatokinugawa/shibuya-dot-xss-techtalk-number-11?slide=6 "JSでDoSる/ Shibuya.XSS techtalk #11 - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">slide</span> <span class="jser-tag">security</span></p>

JavaScriptで例外が発生するパターンやNode.jsでクラッシュするケーススタディについてのスライド


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## DasSur.ma – Raw WebAssembly
[dassur.ma/things/raw-wasm/](https://dassur.ma/things/raw-wasm/ "DasSur.ma – Raw WebAssembly")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span></p>

WebAssemblyがstack-based VMであるとはどういうことかを見ていく記事。
WebAssembly text形式であるwatを手書きして、WebAssemblyでのモジュールの定義、関数の定義と呼び出し、メモリの確保、wasmの読み込みについて。

- [Understanding WebAssembly text format - WebAssembly | MDN](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format "Understanding WebAssembly text format - WebAssembly | MDN")

----

## Accessibility Insights
[accessibilityinsights.io/](https://accessibilityinsights.io/ "Accessibility Insights")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">accessibility</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">windows</span> <span class="jser-tag">Extension</span></p>

アクセシビリティのチェックを補助するブラウザ拡張。
アクセシビリティのチェック項目を可視化したり、FastPassとAssessmentの2つのシナリオでのテストをサポートしている。

- [microsoft/accessibility-insights-web: Accessibility Insights for Web](https://github.com/Microsoft/accessibility-insights-web "microsoft/accessibility-insights-web: Accessibility Insights for Web")
- [Introduction to Accessibility Insights for Web - YouTube](https://www.youtube.com/watch?v=U6NY8Cxym5g "Introduction to Accessibility Insights for Web - YouTube")

----

## Inside Microsoft’s surprise decision to work with Google on its Edge browser - The Verge
[www.theverge.com/2019/5/6/18527550/microsoft-chromium-edge-google-history-collaboration](https://www.theverge.com/2019/5/6/18527550/microsoft-chromium-edge-google-history-collaboration "Inside Microsoft’s surprise decision to work with Google on its Edge browser - The Verge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">Chrome</span> <span class="jser-tag">インタビュー</span> <span class="jser-tag">OSS</span> <span class="jser-tag">google</span> <span class="jser-tag">MS</span></p>

MSEdgeがChromiumベースになった背景について。
最初はEdgeの利用率、最新の機能の実装遅れなどの問題を解決する選択肢の一つだったが、組織改編、Septagonというプロトタイプ、切り替えの公表から実際の作業に入った話など


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## Reakit
[reakit.io/](https://reakit.io/ "Reakit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">accessibility</span> <span class="jser-tag">library</span></p>

アクセシビリティを考慮したReactコンポーネントライブラリ。
React Hooksへの対応や基礎的なコンポーネントを提供し、コンポーネントを組み合わせ利用できるようにすることを目的にしている。


----

## esxjs/esx: Like JSX, but native and fast
[github.com/esxjs/esx](https://github.com/esxjs/esx "esxjs/esx: Like JSX, but native and fast")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">jsx</span> <span class="jser-tag">React</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span></p>

JSXライクな構文をサポートしたTagged Templateライブラリ。
またReactをesxの構文に変換するBabelプラグインもあり、ReactのSSRテンプレートエンジンとしても利用できる


----
