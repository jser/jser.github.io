---
title: "2021-08-25のJS: browser-compat-dataにDenoを追加、Mobile First and Desktop First、create-react-appからNext.jsに移行"
author: "azu"
layout: post
date : 2021-08-25T02:44:57.250Z
category: JSer
tags:
- React
- testing
- DOM
- Next.js
- webservice

---

JSer.info #554 - MDNなどが利用するブラウザ実装の互換データを管理している `@mdn/browser-compat-data` 4.0.0がリリースされました。

- [Release v4.0.0 · mdn/browser-compat-data](https://github.com/mdn/browser-compat-data/releases/tag/v4.0.0)

互換リストにDenoのデータが追加されています。

- [Deno on MDN | Deno Blog](https://deno.com/blog/deno-on-mdn)

スキーマに`preview`と`accepts_flags`の追加、XPathとXSLTのデータが不完全であるため削除などの変更も含まれています・

----

[The State Of Mobile First and Desktop First - Ahmad Shadeed](https://ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/)という記事では、CSSを書くときにMobileとDesktop向けのどちらを先に書くかについて書かれています。

MobileとDesktopのどちらかを先に書いて、もう一方をMedia Queryで上書きしたときのコード量や拡張性の違いについて比較しています。
また、ベースに加えてMobileとDesktopの対応をそれぞれ書いた場合の難しい点についても書かれています。
発展としてFlexboxやCSS Grid、Container Queriesなどの新しいCSS機能を使うことでより簡単に書けるようになっている話なども含まれています。

----

[From Create-React-App to Next | Kitty Giraudel](https://kittygiraudel.com/2021/08/24/from-cra-to-next/)という記事では[Create React App](https://github.com/facebook/create-react-app)(CRA)から[Next.js](https://nextjs.org/)への移行をどのようにしたかについて書かれています。

`<head>`やスタイリングなどの項目ごとに、CRAからNext.jsにどのように移植したのかが書かれています。
また移行後に`<Link>`以外はどちらの環境でも実行できたため、移行の動作確認として両方の環境で動かしてテストする方法についても書かれています。



----

<h1 class="site-genre">ヘッドライン</h1>

----

## Announcing React Native 0.65 · React Native
[reactnative.dev/blog/2021/08/17/version-065](https://reactnative.dev/blog/2021/08/17/version-065 "Announcing React Native 0.65 · React Native")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">iOS</span> <span class="jser-tag">Android</span></p>

React Native 0.65リリース。
Hermes 0.8にアップグレードし、Hadesというガベージコレクタの実装、ECMAScript i18n APIのサポート、Apple M1のサポートなど。


----

## Release v9.1.0 · mochajs/mocha
[github.com/mochajs/mocha/releases/tag/v9.1.0](https://github.com/mochajs/mocha/releases/tag/v9.1.0 "Release v9.1.0 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Mocha 9.1.0リリース。
`--fail-zero`、`--node-option`のサポート、`JSON`レポーターの追加など


----

## Release Notes for Safari Technology Preview 130 | WebKit
[webkit.org/blog/11958/release-notes-for-safari-technology-preview-130/](https://webkit.org/blog/11958/release-notes-for-safari-technology-preview-130/ "Release Notes for Safari Technology Preview 130 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

フラグ付きで`Array.prototype.findLast`と`Array.prototype.findLastIndex`のサポート、WebAudioでWebM/Opusコンテナのサポートなど


----

## Release v4.0.0 · mdn/browser-compat-data
[github.com/mdn/browser-compat-data/releases/tag/v4.0.0](https://github.com/mdn/browser-compat-data/releases/tag/v4.0.0 "Release v4.0.0 · mdn/browser-compat-data")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mdn</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

MDNなどで使われるウェブ技術の互換性リストであるbrowser-compat-data 4.0.0リリース。
スキーマに`preview`と`accepts_flags`の追加、Denoを追加、XPathとXSLTのデータが不完全であるため削除など

- [Deno on MDN | Deno Blog](https://deno.com/blog/deno-on-mdn "Deno on MDN | Deno Blog")

----

## The npm registry is deprecating TLS 1.0 and TLS 1.1 | The GitHub Blog
[github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/](https://github.blog/2021-08-23-npm-registry-deprecating-tls-1-0-tls-1-1/ "The npm registry is deprecating TLS 1.0 and TLS 1.1 | The GitHub Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Github</span> <span class="jser-tag">security</span> <span class="jser-tag">news</span></p>

npm registryでTLS 1.0とTLS 1.1を非推奨化し、2021年9月29日でサポートを終了する予定。
Node.js 0.10.0未満のバージョンを使っているケースやカスタムしたバイナリを使っているケースが対象となるがすでに99%はTLS 1.2を利用しているとのこと。


----
<h1 class="site-genre">アーティクル</h1>

----

## The State Of Mobile First and Desktop First - Ahmad Shadeed
[ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/](https://ishadeed.com/article/the-state-of-mobile-first-and-desktop-first/ "The State Of Mobile First and Desktop First - Ahmad Shadeed")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSSを書くときにMobileとDesktop向けのどちらを先に書くかについて。
MobileとDesktopのどちらかを先に書いて、もう一方をMedia Queryで上書きしたときのコード量や拡張性の違いについて。
また、ベースとそれぞれを書いた場合やFlexboxやContainer Queryといった最近の機能を使って書いた場合についてなど


----

## mouseover 中に表示される DOM のデバッグ | blog.jxck.io
[blog.jxck.io/entries/2021-08-20/how-to-debug-mouseover.html](https://blog.jxck.io/entries/2021-08-20/how-to-debug-mouseover.html "mouseover 中に表示される DOM のデバッグ | blog.jxck.io")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

mouseover中に表示されるDOM要素を開発者ツールでデバッグする方法について


----

## &#039;return await promise&#039; vs &#039;return promise&#039; in JavaScript
[dmitripavlutin.com/return-await-promise-javascript/](https://dmitripavlutin.com/return-await-promise-javascript/ "&#039;return await promise&#039; vs &#039;return promise&#039; in JavaScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Promises</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

`return await promise`と`return promise`で動作が異なるケースについて。
`try...catch`で囲まれている場合には、`await`によってthrowされると結果が異なる


----

## 複数リポジトリ間におけるeslint・prettierの設定共通化 - LIVESENSE ENGINEER BLOG
[made.livesense.co.jp/entry/2021/08/24/083000](https://made.livesense.co.jp/entry/2021/08/24/083000 "複数リポジトリ間におけるeslint・prettierの設定共通化 - LIVESENSE ENGINEER BLOG")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLintの設定を社内で共有管理するために、scoped packagesとして公開して利用方法について


----

## Why WASM is not the future of Babylon.js | by Babylon.js | Aug, 2021 | Medium
[babylonjs.medium.com/why-wasm-is-not-the-future-of-babylon-js-5832b09c9b10](https://babylonjs.medium.com/why-wasm-is-not-the-future-of-babylon-js-5832b09c9b10 "Why WASM is not the future of Babylon.js | by Babylon.js | Aug, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">WebAssembly</span> <span class="jser-tag">article</span> <span class="jser-tag">JavaScript</span></p>

WebAssemblyはC++などのネイティブな言語をコンパイルして利用するのが目的であるため、TypeScriptで書かれたBabylon.jsをWasmにする正当な理由がまだないという話。
WasmとJS間のコミュニケーションコストやデバッグが難しい、メモリ管理なども含むためサイズが大きくなるなどの問題点について。
また、Babylon.jsの物理エンジンなどの一部領域ではWasmをすでに利用していることなどについても書かれている。


----

## From Create-React-App to Next | Kitty Giraudel
[kittygiraudel.com/2021/08/24/from-cra-to-next/](https://kittygiraudel.com/2021/08/24/from-cra-to-next/ "From Create-React-App to Next | Kitty Giraudel")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Next.js</span> <span class="jser-tag">article</span></p>

Create-React-Appで書かれていたアプリをNext.jsに移行した話。
ボイラープレート、`<head>`、ルーティング、コンポーネントのDynamic Import、Styling、CSR/SSR、Lintなどについて。
また`<Link>`以外はどちらの環境でも実行できたため、移行の動作確認として両方の環境で動かしてテストする方法について


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## SpeedVitals - Optimize your Website for Web Vitals
[speedvitals.com/](https://speedvitals.com/ "SpeedVitals - Optimize your Website for Web Vitals")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span></p>

ウェブサイトのパフォーマンス計測をしてCore Web Vitalsの改善方法を提示するウェブサービス。
計測結果からLCPのスコアの改善方法、レイアウトシフトの視覚化など改善に関する情報を提示する

- [Introducing SpeedVitals Alpha Version! - SpeedVitals](https://blog.speedvitals.com/introducing-speedvitals/#more-20 "Introducing SpeedVitals Alpha Version! - SpeedVitals")

----

## @open-wc/semantic-dom-diff - npm
[www.npmjs.com/package/@open-wc/semantic-dom-diff](https://www.npmjs.com/package/@open-wc/semantic-dom-diff "@open-wc/semantic-dom-diff - npm")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">HTML</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

DOM/HTMLのassertionライブラリ。
HTML文字列を比較したテストができる。

----

## Testing | Next.js
[nextjs.org/docs/testing](https://nextjs.org/docs/testing "Testing | Next.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">document</span></p>

Next.jsにおけるテストについてのドキュメント。
Cypressを使ったE2EテストとJest + React Testing Libraryを使ったテストの方法について紹介している。

- [Delba de Oliveira on Twitter: &amp;quot;We&#039;ve just released the first iteration of the Next.js Testing Docs: https://t.co/jhe7zSigt3 🧪 We wanted to provide a starting point for those looking to set up Next.js with 3 commonly used testing tools: @cypress\_io, @fbjest and React @TestingLib.&amp;quot; / Twitter](https://twitter.com/delba_oliveira/status/1427307677709967362 "Delba de Oliveira on Twitter: &amp;amp;quot;We&amp;#039;ve just released the first iteration of the Next.js Testing Docs: https://t.co/jhe7zSigt3 🧪 We wanted to provide a starting point for those looking to set up Next.js with 3 commonly used testing tools: @cypress\_io, @fbjest and React @TestingLib.&amp;amp;quot; / Twitter")


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## geist-org/react: Modern and minimalist React UI library.
[github.com/geist-org/react](https://github.com/geist-org/react "geist-org/react: Modern and minimalist React UI library.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span></p>

VercelのデザインをインスパイアしたReactのUIフレームワーク


----

## johnsoncodehk/volar: ⚡ Fast Vue Language Support Extension
[github.com/johnsoncodehk/volar](https://github.com/johnsoncodehk/volar "johnsoncodehk/volar: ⚡ Fast Vue Language Support Extension")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">VSCode</span> <span class="jser-tag">plugin</span></p>

Vue 3をサポートするVSCode向けの拡張機能。
`.vue`ファイルのTypeScriptの型チェックやテンプレートのlanguage serverを提供する


----
