---
title: "2024-02-05のJS: TypeScript 5.4 Beta、Learn Testing/Performance、Interop 2024"
author: "azu"
layout: post
date: 2024-02-05T07:00:08.915Z
category: JSer
tags:
- browser
- tutorial
- WebPlatformAPI
- nodejs
- Tools

---

JSer.info #679 - - [Announcing TypeScript 5.4 Beta - TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/)
- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909)

---

- [Learn Testing  |  web.dev](https://web.dev/learn/testing)
- [Learn Performance  |  web.dev](https://web.dev/learn/performance?hl=en)

---

- [Interop 2024  |  Blog  |  web.dev](https://web.dev/blog/interop-2024?hl=en)
- [The web just gets better with Interop 2024 | WebKit](https://webkit.org/blog/14955/the-web-just-gets-better-with-interop/)
- [Interop 2024 Launch - Bocoup](https://bocoup.com/blog/interop-2024)
- [Interop 2024 Launches | Igalia](https://www.igalia.com/2024/interop-2024-launches.html)
- [Microsoft Edge and Interop 2024 - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2024/02/01/microsoft-edge-and-interop-2024/)
- [Announcing Interop 2024 - Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2024/02/announcing-interop-2024/)
- [Interop 2024がスタート | フロントエンドBlog | ミツエーリンクス](https://www.mitsue.co.jp/knowledge/blog/frontend/202402/02_1152.html)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Release v3.10.0 · nuxt/nuxt
[github.com/nuxt/nuxt/releases/tag/v3.10.0](https://github.com/nuxt/nuxt/releases/tag/v3.10.0 "Release v3.10.0 · nuxt/nuxt")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Nuxt.js v3.10.0リリース。
実験的なオプションとして`sharedPrerenderData`を追加、`useId()`がSSR時にuniqueなIDを返すことを保証するように、アンチパターンの検出の強化など


----

## Announcing TypeScript 5.4 Beta - TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-5-4-beta/ "Announcing TypeScript 5.4 Beta - TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 5.4 Betaリリース。
クロージャーにおけるNarrowing結果の改善、`NoInfer` Utility Typeの追加。
ES2024の`Object.groupBy`/`Map.groupBy`をサポート、Import Attributesのサポート。
`target: "ES3"`や`out`オプションなどを非推奨化など

- [Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript](https://github.com/microsoft/TypeScript/issues/51909 "Feedback: 5.0 deprecations · Issue #51909 · microsoft/TypeScript")

----

## Release v9.0.1 · typicode/husky
[github.com/typicode/husky/releases/tag/v9.0.1](https://github.com/typicode/husky/releases/tag/v9.0.1 "Release v9.0.1 · typicode/husky")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">GIt</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

husky v9.0.1リリース。
`husk init`でセットアップを簡略化、git hookの書き方を単純化など


----
<h1 class="site-genre">アーティクル</h1>

----

## CodeMirror v6によるZennのMarkdownエディタの作り方
[zenn.dev/team\_zenn/articles/zenn-markdown-editor-by-cm6](https://zenn.dev/team_zenn/articles/zenn-markdown-editor-by-cm6 "CodeMirror v6によるZennのMarkdownエディタの作り方")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">article</span> <span class="jser-tag">React</span></p>

CodeMirrot v6でのMarkdownエディタの実装方法について


----

## SameSite属性とCSRFとHSTS - Cookieの基礎知識からブラウザごとのエッジケースまでおさらいする - Flatt Security Blog
[blog.flatt.tech/entry/samesite\_csrf\_hsts](https://blog.flatt.tech/entry/samesite_csrf_hsts "SameSite属性とCSRFとHSTS - Cookieの基礎知識からブラウザごとのエッジケースまでおさらいする - Flatt Security Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTTP</span> <span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Cookieの属性について。
Secure/HttpOnly/Domain/Path/SameSite属性、`__Secure-`/`__Host-` prefix、SameSite属性の挙動やブラウザのデフォルトの動作について。


----

## Interop 2024がスタート | フロントエンドBlog | ミツエーリンクス
[www.mitsue.co.jp/knowledge/blog/frontend/202402/02\_1152.html](https://www.mitsue.co.jp/knowledge/blog/frontend/202402/02_1152.html "Interop 2024がスタート | フロントエンドBlog | ミツエーリンクス")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">article</span></p>

ブラウザベンダーが注力して相互運用性に取り組むInterop 2024について。


----

## Node.jsで機能やパッケージの非推奨メッセージを通知する方法 | Web Scratch
[efcl.info/2024/02/04/emitwarning/](https://efcl.info/2024/02/04/emitwarning/ "Node.jsで機能やパッケージの非推奨メッセージを通知する方法 | Web Scratch")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">nodejs</span> <span class="jser-tag">article</span></p>

npmやNode.jsで非推奨のメッセージを通知する方法について。
パッケージの非推奨化コードレベルの非推奨化、実行時の非推奨化について


----

## Import attributes · V8
[v8.dev/features/import-attributes](https://v8.dev/features/import-attributes "Import attributes · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">article</span></p>

ECMAScript Proposal Stage 3のImport attributesについて。
`import ... from .... assert { type } `はセマンティクス的に問題があったため、`import ... from .... with { type }`へと変更された。


----

## Learn Testing  |  web.dev
[web.dev/learn/testing](https://web.dev/learn/testing "Learn Testing  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">testing</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">browser</span> <span class="jser-tag">nodejs</span></p>

自動テストについて学ぶチュートリアル。
ブラウザやNode.jsでのテスト、テストの種類、コンポーネントテスト、静的解析ツールなどについて


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Learn Performance  |  web.dev
[web.dev/learn/performance?hl&#x3D;en](https://web.dev/learn/performance?hl=en "Learn Performance  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">tutorial</span> <span class="jser-tag">browser</span></p>

ブラウザのパフォーマンスについてのチュートリアル。
リソースロードの最適化、JavaScriptの最適化、プリロード、Web Workerについてなど


----

## Tappy - Yahoo!デベロッパーネットワーク
[tappy.yahoo.co.jp/](https://tappy.yahoo.co.jp/ "Tappy - Yahoo!デベロッパーネットワーク")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">Tools</span> <span class="jser-tag">mobile</span> <span class="jser-tag">accessibility</span></p>

ウェブサイトのボタンなどのタップ成功率を計算して表示してくれるツール。
タップミスが起きやすいボタンなのかの調査に利用できる。

- [スマホのタップ操作の成功率を算出するモデル ～ UIデザインにおけるユーザビリティの推定 - Yahoo! JAPAN Tech Blog](https://techblog.yahoo.co.jp/entry/2021120930233778/ "スマホのタップ操作の成功率を算出するモデル ～ UIデザインにおけるユーザビリティの推定 - Yahoo! JAPAN Tech Blog")

----

## Compression Streams are now supported on all browsers  |  Blog  |  web.dev
[web.dev/blog/compressionstreams?hl&#x3D;en](https://web.dev/blog/compressionstreams?hl=en "Compression Streams are now supported on all browsers  |  Blog  |  web.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">WebPlatformAPI</span></p>

gzipの圧縮/解凍するCompressionStreamが全てのブラウザで利用できるようになった。


----
