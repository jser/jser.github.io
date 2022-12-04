---
title: "2020-06-30のJS: Angular 10、TypeScript 4.0 Beta、Safari 14の変更点(Tracking Prevention)"
author: "azu"
layout: post
date : 2020-06-29T15:29:41.875Z
category: JSer
tags:
- Angular
- TypeScript
- Safari

---

JSer.info #494 - Angular 10がリリースされました。

- [Version 10 of Angular Now Available - Angular Blog](https://blog.angular.io/tagged/release-notes)
- [angular/CHANGELOG.md at master · angular/angular](https://github.com/angular/angular/compare/10.0.0-rc.6...10.0.0)
- [What’s new in Angular 10 | InfoWorld](https://www.infoworld.com/article/3537449/whats-new-in-angular-10.html)

依存するTypeScriptがそれぞれ[TypeScript 3.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html)、[TSLib 2.0](https://github.com/microsoft/tslib/releases/tag/2.0.0)、[TSLint 6](https://github.com/palantir/tslint/releases/tag/6.0.0)にアップデートされています。

Angular MaterialにDate Range Pickerの追加されています。
CommonJSを取り込むと警告がでるようになりES Momodulesを使うことを推奨するようになりました。
`ng new`に`--strict`オプションの追加され、TypeScriptなどのビルド時の`strict`フラグをまとめて有効化できるようになっています。
また新しいプロジェクトでのデフォルトのbrowserslistsが更新され、ES5のビルドを生成しないようになっています。

----

TypeScript 4.0 Betaがリリースされました。

- [Announcing TypeScript 4.0 Beta | TypeScript](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/)

Variadic Tuple Types、Labeled Tuple Elements、コンストラクタからClass Propertyの推論ができるようになっています
また`catch`節の変数（識別子）の型として`unknown`を指定できるようになっています。
その他にはStage 3のlogical assignmentをサポート、`jsxFragmentFactory`オプションのサポート、VSCodeで起動速度を向上させるためのPartial Editing Modeのサポートなどが含まれています。

----

Safari 14のBetaが公開されていますが、同様の変更内容を含むSafari Technology Previewが公開されています。

- [Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit](https://webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/)
- [Safari 14 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes)

また、[Tracking Prevention in WebKit | WebKit](https://webkit.org/tracking-prevention/)というドキュメントでは、
Safariのトラッキング防止に関する用語の解説や具体的にブロックするものについて解説されています。
Fingerprintingが可能になる可能性があるため、次のAPIを実装する予定がないことについても書かれています。

- Web Bluetooth
- Web MIDI API
- Magnetometer API
- Web NFC API
- Device Memory API
- Network Information API
- Battery Status API
- Ambient Light Sensor
- HDCP Policy Check extension for EME
- Proximity Sensor
- WebHID
- Serial API
- Web USB
- Geolocation Sensor (background geolocation)
- User Idle Detection

FirefoxもこれらのAPIのうちいくつかに関しては`harmful`という立場を示しています。

- [Mozilla Specification Positions](https://mozilla.github.io/standards-positions/)

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Version 10 of Angular Now Available - Angular Blog
[blog.angular.io/version-10-of-angular-now-available-78960babd41](https://blog.angular.io/version-10-of-angular-now-available-78960babd41 "Version 10 of Angular Now Available - Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular 10.0.0リリース。
Angular MaterialにDate Range Pickerの追加。
CommonJSを取り込むと警告がでるように、`ng new`に`--strict`オプションの追加、TypeScript 3.9へのアップデート、デフォルトのbrowserslistsの更新など


----

## Announcing TypeScript 4.0 Beta | TypeScript
[devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/](https://devblogs.microsoft.com/typescript/announcing-typescript-4-0-beta/ "Announcing TypeScript 4.0 Beta | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 4.0 Betaリリース。
Variadic Tuple Types、Labeled Tuple Elements、コンストラクタからClass Propertyの推論ができるように。
`catch`節の変数が`any`から`unknown`に変更。
Stage 3のlogical assignmentをサポート、`jsxFragmentFactory`オプションのサポート、VSCodeでPartial Editing Modeのサポートなど。


----

## Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit
[webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/](https://webkit.org/blog/10875/release-notes-for-safari-technology-preview-109-with-safari-14-features/ "Release Notes for Safari Technology Preview 109 with Safari 14 Features | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology 109リリース。
Safari 14の変更も含まれる。
WebExtensions、Private report、Web Authentication、private class fieldsのサポート。
Flashのサポート終了など。

- [Safari 14 Beta Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes "Safari 14 Beta Release Notes | Apple Developer Documentation")

----

## hapi.js on Twitter: "Some un-hapi and joi-less news..." / Twitter
[twitter.com/hapijs/status/1275887984114413569](https://twitter.com/hapijs/status/1275887984114413569 "hapi.js on Twitter: \"Some un-hapi and joi-less news...\" / Twitter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">news</span></p>

Node.jsフレームワークであるhapiのコア開発者がhapiの開発を終了するという宣言をした。

- [Slack | end | hapi hour](https://app.slack.com/client/T6ATU7T16/C015JQPME23/thread/C015JQPME23-1593110366.302100 "Slack | end | hapi hour")
- [hapi.dev - The simple, secure framework developers trust](https://hapi.dev/ "hapi.dev - The simple, secure framework developers trust")

----
<h1 class="site-genre">アーティクル</h1>

----

## Async Clipboard API | WebKit
[webkit.org/blog/10855/async-clipboard-api/](https://webkit.org/blog/10855/async-clipboard-api/ "Async Clipboard API | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">article</span></p>

Safari 13.1でサポートされたAsync Clipboard APIについて。
クリップボードの読み書き、Security/Privacyにおける制限について


----

## What's New In DevTools (Chrome 85)  |  Web  |  Google Developers
[developers.google.com/web/updates/2020/06/devtools](https://developers.google.com/web/updates/2020/06/devtools "What's New In DevTools (Chrome 85)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 85の開発者ツールの変更点について。
CSSOM経由で追加されたCSSを編集に対応、Lighthouse 6にアップデート、App shortcutsについての警告に対応、`respondWith`がTimingタブに表示。
パフォーマンスパネルにJavaScriptのコンパイルキャッシュの情報を表示するようになるなど


----

## Refactoring optional chaining into a large codebase: lessons learned – Lea Verou
[lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/](https://lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/ "Refactoring optional chaining into a large codebase: lessons learned – Lea Verou")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span> <span class="jser-tag">refacoring</span></p>

ES2020で入ったOptional Chainingを使ったリファクタリングについて。
Optional Chainingに書き換えできるパターン、書き換えてはいけないパターンについてなど


----

## Reactのレンダリングに関する完全ガイド - Qiita
[qiita.com/hellokenta/items/6b795501a0a8921bb6b5](https://qiita.com/hellokenta/items/6b795501a0a8921bb6b5 "Reactのレンダリングに関する完全ガイド - Qiita")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">translate</span></p>

Complete Guide to React Rendering Behaviorの翻訳。
レンダリングとコミットのフェーズ、レンダリングの動作、パフォーマンスの測定、再レンダリングのタイミングについてなど

- [Blogged Answers: A (Mostly) Complete Guide to React Rendering Behavior · Mark's Dev Blog](https://blog.isquaredsoftware.com/2020/05/blogged-answers-a-mostly-complete-guide-to-react-rendering-behavior/ "Blogged Answers: A (Mostly) Complete Guide to React Rendering Behavior · Mark&#x27;s Dev Blog")

----

## Tracking Prevention in WebKit | WebKit
[webkit.org/tracking-prevention/](https://webkit.org/tracking-prevention/ "Tracking Prevention in WebKit | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">privacy</span> <span class="jser-tag">security</span></p>

Safariのトラッキング防止について解説しているドキュメント。
First-Party、Third-PartyでのCookie、Storageの制限、Fingerprintingに利用できるため実装しないWeb API、ITPについてなど

- [Tracking Prevention Policy | WebKit](https://webkit.org/tracking-prevention-policy/ "Tracking Prevention Policy | WebKit")

----
<h1 class="site-genre">スライド、動画関係</h1>

----

## webpack 5 Miniseries - Tobias Koppers, webpack - YouTube
[www.youtube.com/watch?v&#x3D;3c-RFpaiUT8&amp;list&#x3D;PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5&amp;index&#x3D;34&amp;t&#x3D;0s](https://www.youtube.com/watch?v=3c-RFpaiUT8&list=PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5&index=34&t=0s "webpack 5 Miniseries - Tobias Koppers, webpack - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webpack</span> <span class="jser-tag">video</span></p>

webpack 5の変更についての紹介動画。
自動的なNode.jsのpolyfillの削除、生成コードのESバージョンを選択、ビルドのパフォーマンスやキャッシュの改善、最適化の改善やログの改善、Module Federationについてなど


----

## OpenJS World 2020 - YouTube
[www.youtube.com/playlist?list&#x3D;PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5](https://www.youtube.com/playlist?list=PLyspMSh4XhLP-mqulUMcaqTbLo-ZJxSX5 "OpenJS World 2020 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">video</span> <span class="jser-tag">Conference</span></p>

OpenJS World 2020の動画一覧

- [OpenJS World | Linux Foundation Events](https://events.linuxfoundation.org/openjs-world/ "OpenJS World | Linux Foundation Events")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## ealush/vest: Vest - effortless validations
[github.com/ealush/vest](https://github.com/ealush/vest "ealush/vest: Vest - effortless validations")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

バリデーションライブラリ


----

## nastyox/Rando.js: The world's easiest, most powerful random function.
[github.com/nastyox/Rando.js](https://github.com/nastyox/Rando.js "nastyox/Rando.js: The world's easiest, most powerful random function.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

指定範囲のランダムな値を生成するライブラリ。


----
<h1 class="site-genre">書籍関係</h1>

----

## Talking TypeScript with the engineer who leads the team - Stack Overflow Blog
[stackoverflow.blog/2020/06/15/talking-typescript-with-ryan-cavanaugh/](https://stackoverflow.blog/2020/06/15/talking-typescript-with-ryan-cavanaugh/ "Talking TypeScript with the engineer who leads the team - Stack Overflow Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">Interview</span> <span class="jser-tag">Microsoft</span></p>

TypeScriptのプロジェクトリードであるRyan Cavanaughのインタビュー。
作られた理由、Angularでの採用がターニングポイント、チーム構成、エディタとコンパイラサービス、JavaScriptのエコシステムについて


----
