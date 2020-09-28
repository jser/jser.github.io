---
title: "2020-09-29のJS: 新しいJSXの変換、Content delivery networks (CDNs)、 Atomic CSS-in-JS"
author: "azu"
layout: post
date : 2020-09-28T22:45:55.623Z
category: JSer
tags:
- JSX
- CSS
- CDN
- CSS-in-JS

---

JSer.info #507 - 次の記事ではReact 17 RCからサポートされている新しいJSXの変換について紹介されています。

- [Introducing the New JSX Transform – React Blog](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)

新しいJSXの変換では、JSXを変換するツール(BabelやTypeScript)、JSXを扱うライブラリ(ReactやPreact)のアップデートが必要です。
一方で、JSXの構文は何も変わらないため、あくまで関係するのは変換ツールとライブラリ側の実装です。

[React 0.12の際に導入されたJSXの変換仕様](https://reactjs.org/blog/2014/10/16/react-v0.12-rc1.html#jsx-changes)の中には、ライブラリ側の実装を複雑化させる仕様や現在では不要な仕組みも含まれています。
新しいJSXの変換の仕組みでは、その仕様の単純化やそれにともなうパフォーマンスの改善が主な目的です。

新しい変換の仕様については次のRFCにまとめられています。

- [rfcs/0000-create-element-changes.md at createlement-rfc · reactjs/rfcs](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md)

また新しい変換方式では、JSX(React Component)を書く際に `import React from 'react';` のような Reactのimportが不要となります。
そのため、既に書かれた `import React from 'react';` を削除するマイグレーションツールも公開されています。

- [Removing Unused React Imports](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html#removing-unused-react-imports)

この新しいJSXの変換方式は、それぞれ次のライブラリとツールで対応しています。

ライブラリ

- [React v17.0(RC)](https://reactjs.org/blog/2020/08/10/react-v17-rc.html)
- [Preact v10.5.0](https://github.com/preactjs/preact/releases/tag/10.5.0)

ツール

- [Babel 7.9.0](https://babeljs.io/blog/2020/03/16/7.9.0)
- [TypeScript 4.1 Beta](https://devblogs.microsoft.com/typescript/announcing-typescript-4-1-beta/#jsx-factories)
- [Flow v0.126.0](https://github.com/facebook/flow/releases/tag/v0.126.0)

----

[Content delivery networks (CDNs)](https://web.dev/content-delivery-networks/)という記事では、CDNの概要について書かれています。

CDNの仕組み、キャッシュのEvictionとPurging、Private/PublicなリソースでのCache-Control設定、動的/静的なコンテンツにおける設定の考え方。
また、キャッシュヒット率(CHR)の計測と改善方法、CDNのパフォーマンス機能としての圧縮/TLS 1.3/minificationについてなどについて書かれています。

----

[Atomic CSS-in-JS](https://sebastienlorber.com/atomic-css-in-js)という記事では、Atomic CSSとCSS-in-JSの組み合わせについて書かれています。

Atomic CSSはutility-firstなCSSを示す言葉です。

```css
/* Atomic CSS */
.bw-2x {
  border-width: 2px;
}
.bss {
  border-style: solid;
}
.sans {
  font-style: sans-serif;
}
.p-1x {
  padding: 10px;
}

/* Not atomic, because the class contains 2 rules */
.p-1x-sans {
  padding: 10px;
  font-style: sans-serif;
}
```

このUtility/atomic CSSはgzip効率が良いコードとなりファイルサイズ的なメリットなどがあります。
一方でのUtility/atomic CSSを手書きする場合には命名が難しい問題、utility-firstなライブラリである[Tailwind](https://tailwindcss.com/)のようなCSSライブラリを使うと未使用のクラスが残る問題などの問題もあります。

この記事では、Atomic CSSの問題を解決するためにCSS-in-JSと組み合わせるAtomic CSS-in-JSについて書かれています。
Atomic CSS-in-JSの例としてFacebookのStylexを紹介しています。

- [Tech stack rebuild for a new Facebook.com - Facebook Engineering](https://engineering.fb.com/web/facebook-redesign/)
- [Building the New Facebook with React and Relay | Frank Yan - YouTube](https://www.youtube.com/watch?v=9JZHodNR184)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## V8 release v8.6 · V8
[v8.dev/blog/v8-release-86](https://v8.dev/blog/v8-release-86 "V8 release v8.6 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 8.6リリース。
JavaScriptエンジンのFuzzingツールであるJS-Fuzzerの公開、`Number.prototype.toString`のパフォーマンス改善。
`Atomics.notify`にリネームされたため`Atomics.wake`の削除、Wasmのパフォーマンス改善など


----

## Release 10.5.0 - JSX Reloaded · preactjs/preact
[github.com/preactjs/preact/releases/tag/10.5.0](https://github.com/preactjs/preact/releases/tag/10.5.0 "Release 10.5.0 - JSX Reloaded · preactjs/preact")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Preact 10.5.0リリース。
新しいJSXの変換に対応したRuntimeの追加、 hydrationにおけるSuspend & Resumeの改善など


----

## Release DOMPurify 2.1.0 · cure53/DOMPurify
[github.com/cure53/DOMPurify/releases/tag/2.1.0](https://github.com/cure53/DOMPurify/releases/tag/2.1.0 "Release DOMPurify 2.1.0 · cure53/DOMPurify")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">DOM</span> <span class="jser-tag">XSS</span> <span class="jser-tag">library</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">ReleaseNote</span></p>

DOMpurify 2.1.0リリース。
jQueryのメソッドはデフォルトで対応したため`SAFE_FOR_JQUERY`フラグを削除、mXSSの修正とコード整理など


----

## Firefox 81.0, See All New Features, Updates and Fixes
[www.mozilla.org/en-US/firefox/81.0/releasenotes/](https://www.mozilla.org/en-US/firefox/81.0/releasenotes/ "Firefox 81.0, See All New Features, Updates and Fixes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">ReleaseNote</span></p>

Firefox 81リリース。
iframe要素の`sandbox`属性が`allow-downloads`をサポート、`Content-Disposition` HTTPヘッダにおいてクオートで囲まれていないファイル名に対応。
JavaScriptのMIMEタイプではないWorkerスクリプトは`new Worker()`で読み込めないように変更など

- [Firefox 81 for developers - Mozilla | MDN](https://developer.mozilla.org/docs/Mozilla/Firefox/Releases/81 "Firefox 81 for developers - Mozilla | MDN")
- [Worker scripts with wrong MIME type will be blocked from loading with Worker() or SharedWorker() (Breaking) | Firefox Site Compatibility](https://www.fxsitecompat.dev/docs/2020/worker-scripts-with-wrong-mime-type-will-be-blocked-from-loading-with-worker-or-sharedworker/ "Worker scripts with wrong MIME type will be blocked from loading with Worker() or SharedWorker() (Breaking) | Firefox Site Compatibility")

----

## ESLint v7.10.0 released - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2020/09/eslint-v7.10.0-released](https://eslint.org/blog/2020/09/eslint-v7.10.0-released "ESLint v7.10.0 released - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">ReleaseNote</span></p>

ESLint 7.10.0リリース。
`no-inline-comments`に`ignorePattern`オプションの追加など


----
<h1 class="site-genre">アーティクル</h1>

----

## Introducing the New JSX Transform – React Blog
[reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html "Introducing the New JSX Transform – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">jsx</span> <span class="jser-tag">article</span></p>

新しいJSXの変換の仕組みについて。
React 17、Babel 7.9.0から対応している。
コンポーネント内で`import React from "react"`が不要となり、パフォーマンスの改善や仕様のシンプル化が目的

- [rfcs/0000-create-element-changes.md at createlement-rfc · reactjs/rfcs](https://github.com/reactjs/rfcs/blob/createlement-rfc/text/0000-create-element-changes.md "rfcs/0000-create-element-changes.md at createlement-rfc · reactjs/rfcs")

----

## Content delivery networks (CDNs)
[web.dev/content-delivery-networks/](https://web.dev/content-delivery-networks/ "Content delivery networks (CDNs)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">network</span> <span class="jser-tag">cdn</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

CDNについての記事。
CDNの仕組み、キャッシュのEvictionとPurging、Private/PublicなリソースでのCache-Control設定、動的/静的なコンテンツにおける設定の考え方。
キャッシュヒット率(CHR)の計測と改善方法、CDNのパフォーマンス機能としての圧縮/TLS 1.3/minificationについてなど


----

## Feature watch: ECMAScript 2021
[2ality.com/2020/09/ecmascript-2021.html](https://2ality.com/2020/09/ecmascript-2021.html "Feature watch: ECMAScript 2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript 2021に入る予定のProposalまとめ


----

## Detached window memory leaks
[web.dev/detached-window-memory-leaks/](https://web.dev/detached-window-memory-leaks/ "Detached window memory leaks")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">article</span></p>

`window.open`で開いたウィンドウにおけるメモリリークについて。
切り離したwindowでメモリリークが起きる原理、heap snapshotや`performance.memory` APIでのメモリの増減の見方。
またメモリリークを避ける方法としてリファレンスを消す方法、WeakRefを使う方法、直接のリファレンスを持たない方法についてなど


----

## ECMAScript proposal updates @ 2020-09 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/09/26/ecmascript-proposal-updat](https://ecmascript-daily.github.io/ecmascript/2020/09/26/ecmascript-proposal-updat "ECMAScript proposal updates @ 2020-09 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2020年9月のTC39ミーティングで更新されたECMAScript Proposalのまとめ。


----

## Publishing Node modules with TypeScript and ES modules - LogRocket Blog
[blog.logrocket.com/publishing-node-modules-typescript-es-modules/](https://blog.logrocket.com/publishing-node-modules-typescript-es-modules/ "Publishing Node modules with TypeScript and ES modules - LogRocket Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

TypeScriptで書いたライブラリをTree Shakingできるような設定で配布できるようにするチュートリアル。


----

## Atomic CSS-in-JS
[sebastienlorber.com/atomic-css-in-js](https://sebastienlorber.com/atomic-css-in-js "Atomic CSS-in-JS")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Atomic CSSについての記事。
utility-firstなCSSを示す言葉だが、命名が難しい問題やutility-firstなライブラリであるTailwindのようなライブラリを使うと未使用のクラスが残る問題などの問題がある。
CSS-in-JSと組み合わせることでこの問題を解決するatomic CSS-in-JSについて。
例としてFacebookのStylexについてを紹介している。

- [Tech stack rebuild for a new Facebook.com - Facebook Engineering](https://engineering.fb.com/web/facebook-redesign/ "Tech stack rebuild for a new Facebook.com - Facebook Engineering")
- [Building the New Facebook with React and Relay | Frank Yan - YouTube](https://www.youtube.com/watch?v=9JZHodNR184 "Building the New Facebook with React and Relay | Frank Yan - YouTube")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## balazsbotond/urlcat: A URL builder library for JavaScript.
[github.com/balazsbotond/urlcat](https://github.com/balazsbotond/urlcat "balazsbotond/urlcat: A URL builder library for JavaScript.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">URL</span> <span class="jser-tag">library</span></p>

URLの結合(join)、パラメータクエリの生成(query)、置換(subst)するライブラリ。


----

## codemix/ts-sql: A SQL database implemented purely in TypeScript type annotations.
[github.com/codemix/ts-sql](https://github.com/codemix/ts-sql "codemix/ts-sql: A SQL database implemented purely in TypeScript type annotations.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">SQL</span> <span class="jser-tag">library</span></p>

TypeScript 4.1のTemplate Literal Typeを使ってSQL構文からクエリ結果の型を返す型ライブラリ


----

## sumup-oss/performance-observer: Generic interface for PerformanceObserver API.
[github.com/sumup-oss/performance-observer](https://github.com/sumup-oss/performance-observer "sumup-oss/performance-observer: Generic interface for PerformanceObserver API.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">library</span></p>

Performance Observerのラッパーライブラリ。
指定したメトリクスを取得するAPIを提供する


----

## jtbennett/create-ts-project: Create Typescript monorepo projects with project references, jest, eslint and prettier configured and ready for development.
[github.com/jtbennett/create-ts-project](https://github.com/jtbennett/create-ts-project "jtbennett/create-ts-project: Create Typescript monorepo projects with project references, jest, eslint and prettier configured and ready for development.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">monorepo</span> <span class="jser-tag">Tools</span></p>

TypeScript monorepo向けの管理ツール。
TypeScript Project References、Yarn、Jest、ESLint、Pretitterなどが入ったCreact React Appのようなツールを目指している


----
