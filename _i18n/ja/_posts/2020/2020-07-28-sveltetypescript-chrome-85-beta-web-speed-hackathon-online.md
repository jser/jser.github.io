---
title: "2020-07-28のJS: SvelteのTypeScriptサポート、Chrome 85 beta、Web Speed Hackathon Online"
author: "azu"
layout: post
date : 2020-07-28T02:42:16.641Z
category: JSer
tags:
- TypeScript
- Chrome
- Performance

---

JSer.info #498 - UIフレームワークであるSvelteがTypeScriptをサポートしました。

- [Svelte <3 TypeScript](https://svelte.dev/blog/svelte-and-typescript)

記事ではSvelteのテンプレート内でTypScriptを使う方法とエディタでのLSP([Language Server Protocol](https://langserver.org/)))を使ったコード補完の方法について紹介しています。

----

Chrome 85 betaがリリースされました。

- [Chromium Blog: Chrome 85: Upload Streaming, Human Interface Devices, Custom Properties with Inheritance and More](https://blog.chromium.org/2020/07/chrome-85-upload-streaming-human.html)
- [Chrome Platform Status](https://www.chromestatus.com/features#milestone%3D85)
- [V8 release v8.5 · V8](https://v8.dev/blog/v8-release-85)

Origin Trialとして[Fetch upload streaming](https://web.dev/fetch-upload-streaming/)、[WebHID](https://github.com/WICG/webhid)、[Declarative Shadow DOM](https://www.chromestatus.com/feature/5191745052606464)、[Portals](https://web.dev/hands-on-portals/)がサポートされています。
また、Mixed Contentの画像に関するAutoupgradeの追加、AVIFフォーマットのサポート、CSSの`conetnt-visibility`、`counter-set`プロパティのサポートなども追加されています。
[非推奨、破壊的な変更](https://developers.google.com/web/updates/2020/07/chrome-85-deps-rems)としては、`color-scheme`プロパティの`only`を削除、Referrer Policyのデフォルト値を`strict-origin-when-cross-origin`に変更。Cookieで`Secure`属性がない`SameSite=None`のサポート終了などが含まれています。

Chrome 85に含まれるJavaScriptのアップデートはV8のブログの方にまとまっています。
[2020-07のTC39 ミーティング](https://ecmascript-daily.github.io/ecmascript/2020/07/26/ecmascript-proposal-update)で[Stage 4](https://github.com/tc39/proposals/blob/master/finished-proposals.md)となった`Promise.any`と`AggregateError`、Logical assignment operatorsが実装されています。
また、同様にStage 4でES2021に入る予定の`String#replaceAll`も実装されています。
その他には、WebAssemblyでMulti-valueのサポート、BigIntsの値を渡せるようになるといった変更も含まれています。

- [V8 release v8.5 · V8](https://v8.dev/blog/v8-release-85)

----

[WIC Speed Hackathon Online](https://github.com/CyberAgentHack/web-speed-hackathon-online)というウェブアプリケーションのパフォーマンス改善を競うハッカソンの課題と解説が公開されています。

- [Web Speed Hackathon Online 出題のねらいと解説 · CyberAgentHack/web-speed-hackathon-online Wiki](https://github.com/CyberAgentHack/web-speed-hackathon-online/wiki/Web-Speed-Hackathon-Online-%E5%87%BA%E9%A1%8C%E3%81%AE%E3%81%AD%E3%82%89%E3%81%84%E3%81%A8%E8%A7%A3%E8%AA%AC)

解説では、パフォーマンスのポイントやどのように改善していくのかについて解説しています。
ビルド(主にフロントエンド)、フロントエンド、バックエンドの項目に大きく分けて解説されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Node v14.6.0 (Current) | Node.js
[nodejs.org/en/blog/release/v14.6.0/](https://nodejs.org/en/blog/release/v14.6.0/ "Node v14.6.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js 14.6.0リリース。
`imports` fieldの実装、`vm`に`microtaskMode`オプションの追加、`fs`のfile descriptorに`trackUnmanagedFds`オプションの追加など

- [module: package &quot;imports&quot; field by guybedford · Pull Request #34117 · nodejs/node](https://github.com/nodejs/node/pull/34117 "module: package &amp;quot;imports&amp;quot; field by guybedford · Pull Request #34117 · nodejs/node")

----

## Svelte <3 TypeScript
[svelte.dev/blog/svelte-and-typescript](https://svelte.dev/blog/svelte-and-typescript "Svelte <3 TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Svelte</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

SvelteのTypeScriptサポート。
テンプレートにTypeScriptで書けるようになり、型チェックが行える。
エディタはLSPを使ったサポートを実装している


----

## wixplosives/pleb: a casual publisher
[github.com/wixplosives/pleb](https://github.com/wixplosives/pleb "wixplosives/pleb: a casual publisher")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">Tools</span></p>

monorepoのnpm publishで行うツール。
gitコミットハッシュベースのcanaryリリースを行うこともできる


----

## ECMAScript proposal updates @ 2020-07 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2020/07/26/ecmascript-proposal-update](https://ecmascript-daily.github.io/ecmascript/2020/07/26/ecmascript-proposal-update "ECMAScript proposal updates @ 2020-07 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span> <span class="jser-tag">news</span></p>

2020-07のTC39ミーティングでステータスが変わったECMAScript Proposalのまとめ。
`Promise.any`、WeakRefs、Logical Assignment Operators、Numeric separatorsがStage 4となりES2021に入る予定


----

## V8 release v8.5 · V8
[v8.dev/blog/v8-release-85](https://v8.dev/blog/v8-release-85 "V8 release v8.5 · V8")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">V8</span> <span class="jser-tag">ReleaseNote</span></p>

V8 8.5リリース。
Stage 4の`Promise.any`と`AggregateError`、String#replaceAll、Logical assignment operatorsの実装。
WebAssemblyでMulti-valueのサポート、BigIntsの値を渡せるようになるなど


----

## Chromium Blog: Chrome 85: Upload Streaming, Human Interface Devices, Custom Properties with Inheritance and More
[blog.chromium.org/2020/07/chrome-85-upload-streaming-human.html](https://blog.chromium.org/2020/07/chrome-85-upload-streaming-human.html "Chromium Blog: Chrome 85: Upload Streaming, Human Interface Devices, Custom Properties with Inheritance and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 85 beta リリース。
Origin TrialとしてFetch upload streaming、WebHID、Declarative Shadow DOM、Portalsのサポート。
Mixed Contentの画像に関するAutoupgradeの追加、AVIFフォーマットのサポート、CSSの`conetnt-visibility`、`counter-set`プロパティのサポート。
`color-scheme`プロパティの`only`を削除、Referrer Policyのデフォルト値を`strict-origin-when-cross-origin`に変更。Cookieで`Secure`属性がない`SameSite=None`のサポート終了など


----

## Release 3.11.0 · avajs/ava
[github.com/avajs/ava/releases/tag/v3.11.0](https://github.com/avajs/ava/releases/tag/v3.11.0 "Release 3.11.0 · avajs/ava")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">testing</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">library</span></p>

AVA 3.11.0リリース。
`t.like()` assertionの追加。


----

## Wiki.js
[wiki.js.org/](https://wiki.js.org/ "Wiki.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">wiki</span> <span class="jser-tag">node.js</span> <span class="jser-tag">webservice</span> <span class="jser-tag">library</span></p>

Node.js製のWikiエンジン


----
<h1 class="site-genre">アーティクル</h1>

----

## HTML5 Worker Test
[html5workertest.com/](https://html5workertest.com/ "HTML5 Worker Test")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">browser</span></p>

WebWorkerで利用できるAPIについてブラウザごとにまとめた対応表


----

## TypeScript Contribution Diary: // @ts-expect-error | Goldblog
[blog.joshuakgoldberg.com/ts-expect-error/](http://blog.joshuakgoldberg.com/ts-expect-error/ "TypeScript Contribution Diary: // @ts-expect-error | Goldblog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

`@ts-expect-error`をどのように実装したのかについて


----

## Web Speed Hackathon Online 出題のねらいと解説 · CyberAgentHack/web-speed-hackathon-online Wiki
[github.com/CyberAgentHack/web-speed-hackathon-online/wiki/Web-Speed-Hackathon-Online-%E5%87%BA%E9%A1%8C%E3%81%AE%E3%81%AD%E3%82%89%E3%81%84%E3%81%A8%E8%A7%A3%E8%AA%AC](https://github.com/CyberAgentHack/web-speed-hackathon-online/wiki/Web-Speed-Hackathon-Online-%E5%87%BA%E9%A1%8C%E3%81%AE%E3%81%AD%E3%82%89%E3%81%84%E3%81%A8%E8%A7%A3%E8%AA%AC "Web Speed Hackathon Online 出題のねらいと解説 · CyberAgentHack/web-speed-hackathon-online Wiki")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span> <span class="jser-tag">webpack</span> <span class="jser-tag">babel</span> <span class="jser-tag">CSS</span></p>

ウェブアプリケーションのパフォーマンス改善ハッカソンの解説。
フロントエンド、バックエンド、ビルド処理での最適化についてハッカソンのアプリを題材に解説している

- [CyberAgentHack/web-speed-hackathon-online](https://github.com/CyberAgentHack/web-speed-hackathon-online "CyberAgentHack/web-speed-hackathon-online")

----

## A Mental Model to think in Typescript
[leandrotk.github.io/tk/2020/07/a-mental-model-to-think-in-typescript/](https://leandrotk.github.io/tk/2020/07/a-mental-model-to-think-in-typescript/ "A Mental Model to think in Typescript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

TypeScriptの型システム、コンパイルエラーとランタイムエラーの違いについてなどについて解説している記事


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## Create App - your tool for starting a new webpack or Parcel project
[createapp.dev/](https://createapp.dev/ "Create App - your tool for starting a new webpack or Parcel project")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">webpack</span></p>

webpackやparcelの設定ジェネレータ。
使いたいJavaScriptやCSSのフレームワーク、Lintツールなどを選択するとそれを導入できるwebpackやparcelの設定ファイルを出力してくれるツール


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## returntocorp/semgrep: Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.
[github.com/returntocorp/semgrep](https://github.com/returntocorp/semgrep "returntocorp/semgrep: Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">console</span> <span class="jser-tag">Tools</span> <span class="jser-tag">search</span></p>

ASTベースのコード検索ツール。
Python/JavaScript/Go/Java/C/JSONなどに対してパターンマッチでの検索ができる


----

## hugojosefson/minimum-node-version: Figures out the lowest version of Node.js that satisfies engines.node in package.json.
[github.com/hugojosefson/minimum-node-version](https://github.com/hugojosefson/minimum-node-version "hugojosefson/minimum-node-version: Figures out the lowest version of Node.js that satisfies engines.node in package.json.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span></p>

依存してるライブラリの`engines`フィールドを満たす最小のNode.jsバージョンを検索するツール


----
