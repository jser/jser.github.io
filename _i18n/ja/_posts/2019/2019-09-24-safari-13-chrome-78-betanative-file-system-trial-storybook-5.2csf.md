---
title: "2019-09-24のJS: Safari 13、Chrome 78 Beta(Native File System trial)、Storybook 5.2(CSF)"
author: "azu"
layout: post
date : 2019-09-24T00:15:41.639Z
category: JSer
tags:
- Safari
- Chrome
- Storybook

---

JSer.info #454 - iOS 13、macOS 10.14.5(Mojave)に搭載されるSafari 13のリリースノートが公開されています。

- [Safari 13 Release Notes | Apple Developer Documentation](https://developer.apple.com/documentation/safari_release_notes/safari_13_release_notes)

Web Authentication APIを使ったFIDO2のセキュリティキーに対応、`__Secure-`と`__Host-`のクッキーprefixのサポート、Pointer EventsやVisual Viewport APIのサポートなどが行われています。
iOS 13のSafariでWebDriverのサポート、ITP 2.3へのアップデート、WebSQLの削除なども含まれています。

- [WebDriver is Coming to Safari in iOS 13 | WebKit](https://webkit.org/blog/9395/webdriver-is-coming-to-safari-in-ios-13/)
- [Intelligent Tracking Prevention 2.3 | WebKit](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/)

----

Chrome 78 Betaがリリースされました。

- [Chromium Blog: Chrome 78 Beta: a new Houdini API, native file system access and more](https://blog.chromium.org/2019/09/chrome-78-beta-new-houdini-api-native.html)


CSS Custom Propertiesを使ったアニメーションのサポート、Native File System APIとSMS Receiver APIのorigin trialでのサポートが含まれています。

- [Smarter custom properties with Houdini’s new API  |  web.dev](https://web.dev/css-props-and-vals/ "Smarter custom properties with Houdini’s new API  |  web.dev")
- [The Native File System API: Simplifying access to local files  |  Web](https://developers.google.com/web/updates/2019/08/native-file-system)

WebSocketsにおけるArrayBufferのダウンロード速度の改善、`performance.mark`などに対してメタデータを付与できるUser Timing API Level 3のサポートもふくまれています。
また、unload時にはポップアップやSync HXRが禁止されるなどの制限の追加、MSEdgeに引き続いてXSS Auditorが廃止されています。

- [Google deprecates XSS Auditor for Chrome | The Daily Swig](https://portswigger.net/daily-swig/google-deprecates-xss-auditor-for-chrome)
- [What’s new in Microsoft Edge in the Windows 10 October 2018 Update - Microsoft Edge Blog](https://blogs.windows.com/msedgedev/2018/10/04/edgehtml-18-october-2018-update/)

----

デザインシステムツールであるStorybook 5.2がリリースされました。

- [Storybook 5.2 - Storybook - Medium](https://medium.com/storybookjs/storybook-5-2-794958b9b111)

UIコンポーネントに対してMDXを使ってドキュメントを書けるDocsPageという機能が追加されています。
詳しくは次の記事でも解説されています。

- [Storybook DocsPage - Storybook - Medium](https://medium.com/storybookjs/storybook-docspage-e185bc3622bf)

今までは、`Stroy#add`のようなAPIでストーリを記述する形式でした。

```js
storiesOf('atoms/Button', module)
  .add('text', () => <Button>Hello</Button>)
  .add('emoji', () => <Button>😀😎👍💯</Button>);
```

Storybook 5.2ではこれに加えてComponent Story Format (CSF)というストーリの形式がサポートされました。
CSFはストーリーをモジュールとしてexportすることで表現できるようになっています。

```js
export default { title: 'atoms/Button' };

export const text = () => <Button>Hello</Button>;
export const emoji = () => <Button>😀😎👍💯</Button>;
```

詳細は次の記事で書かれています。

- [Component Story Format - Storybook - Medium](https://medium.com/storybookjs/component-story-format-66f4c32366df)



----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Moving Firefox to a faster 4-week release cycle - Mozilla Hacks - the Web developer blog
[hacks.mozilla.org/2019/09/moving-firefox-to-a-faster-4-week-release-cycle/](https://hacks.mozilla.org/2019/09/moving-firefox-to-a-faster-4-week-release-cycle/ "Moving Firefox to a faster 4-week release cycle - Mozilla Hacks - the Web developer blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Firefox</span> <span class="jser-tag">news</span></p>

Firefoxのリリースサイクルが7週ごとから4週ごとへと変更される予定について。
一方でFirefox ESRのリリースサイクルは変更されない。


----

## Safari 13 Release Notes | Apple Developer Documentation
[developer.apple.com/documentation/safari\_release\_notes/safari\_13\_release\_notes](https://developer.apple.com/documentation/safari_release_notes/safari_13_release_notes "Safari 13 Release Notes | Apple Developer Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari 13の変更点について。
FIDO2のセキュリティキー、`__Secure-`と`__Host-`のクッキーprefix、Pointer Events、Visual Viewport APIのサポートなど。
iOS 13のSafariでWebDriverのサポート、WebSQLの削除など

- [WebDriver is Coming to Safari in iOS 13 | WebKit](https://webkit.org/blog/9395/webdriver-is-coming-to-safari-in-ios-13/ "WebDriver is Coming to Safari in iOS 13 | WebKit")

----

## jasmine/3.5.0.md at master · jasmine/jasmine
[github.com/jasmine/jasmine/blob/master/release\_notes/3.5.0.md](https://github.com/jasmine/jasmine/blob/master/release_notes/3.5.0.md "jasmine/3.5.0.md at master · jasmine/jasmine")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span> <span class="jser-tag">testing</span></p>

Jasmine 3.5リリース。
`toHaveBeenCalledWith`のエラー結果の出力の改善、`resolveTo`と`rejectWith`の追加、カスタム非同期Matcherを定義する`addAsyncMatchers`の追加など


----

## Chromium Blog: Chrome 78 Beta: a new Houdini API, native file system access and more
[blog.chromium.org/2019/09/chrome-78-beta-new-houdini-api-native.html](https://blog.chromium.org/2019/09/chrome-78-beta-new-houdini-api-native.html "Chromium Blog: Chrome 78 Beta: a new Houdini API, native file system access and more")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 78 Betaリリース。
CSS Custom Propertiesを使ったアニメーションのサポート、Native File System APIとSMS Receiver APIのorigin trialの開始など。
WebSocketsにおけるArrayBufferのダウンロード速度の改善、User Timing API Level 3のサポート。
また、Sync HXRがunload時などには禁止、XSS Auditorの削除など

- [Smarter custom properties with Houdini’s new API  |  web.dev](https://web.dev/css-props-and-vals/ "Smarter custom properties with Houdini’s new API  |  web.dev")

----

## Storybook 5.2 - Storybook - Medium
[medium.com/storybookjs/storybook-5-2-794958b9b111](https://medium.com/storybookjs/storybook-5-2-794958b9b111 "Storybook 5.2 - Storybook - Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Storybook 5.2リリース。
MDXを使ったドキュメントを書けるDocsPageの追加、Storyをモジュールとして作れるCSFのサポート。
TypeScriptのサポート、React Hooksのサポート、 Standalone modeなど

- [Storybook DocsPage - Storybook - Medium](https://medium.com/storybookjs/storybook-docspage-e185bc3622bf "Storybook DocsPage - Storybook - Medium")
- [Component Story Format - Storybook - Medium](https://medium.com/storybookjs/component-story-format-66f4c32366df "Component Story Format - Storybook - Medium")

----
<h1 class="site-genre">アーティクル</h1>

----

## Fresher service workers, by default  |  Web  |  Google Developers
[developers.google.com/web/updates/2019/09/fresher-sw](https://developers.google.com/web/updates/2019/09/fresher-sw "Fresher service workers, by default  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ServiceWorker</span> <span class="jser-tag">article</span></p>

Chrome 78では`importScript`で読み込むファイルも変更があればHTTP Cacheはデフォルトで無視されるようになった。
Chrome 68で追加された`updateViaCache`オプションを使ってHTTP Cache-Controlを見るかを制御できる。


----

## Practical Ways to Write Better JavaScript - Stack Overflow Blog
[stackoverflow.blog/2019/09/12/practical-ways-to-write-better-javascript/](https://stackoverflow.blog/2019/09/12/practical-ways-to-write-better-javascript/ "Practical Ways to Write Better JavaScript - Stack Overflow Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">article</span></p>

より良いJavaScriptを書くためにどうするかという記事。
TypeScriptを使う、ES2015+の機能を活用する、分散を考える。
Lint、テストを行うなどについて


----

## ✩ Wikipedia's JavaScript initialisation on a budget
[phabricator.wikimedia.org/phame/live/7/post/175/wikipedia\_s\_javascript\_initialisation\_on\_a\_budget/](https://phabricator.wikimedia.org/phame/live/7/post/175/wikipedia_s_javascript_initialisation_on_a_budget/ "✩ Wikipedia's JavaScript initialisation on a budget")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">refacoring</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Wikipediaの初期表示に読み込むJavaScriptのファイルサイズを削減した話。
目標のbudgeを28KBと設定してどのように初期ロードのJavaScriptサイズを減らしていったかについて


----

## Intelligent Tracking Prevention 2.3 | WebKit
[webkit.org/blog/9521/intelligent-tracking-prevention-2-3/](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/ "Intelligent Tracking Prevention 2.3 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">privacy</span> <span class="jser-tag">article</span></p>

Safari 13(iOS 13/macOS Catalina)に実装されたITP 2.3について。
CookieからLocalStorageに保存場所を移行したサードパーティトラッカーに対する制限の追加、`document.referrer`にもeTLD+1の制限を追加、デバッグモードの改善など


----

## Techniques to make a web app load fast, even on a feature phone
[web.dev/load-faster-like-proxx/](https://web.dev/load-faster-like-proxx/ "Techniques to make a web app load fast, even on a feature phone")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

PROXXのローディングパフォーマンスに利用したテクニックの紹介記事。
WebPageTestを使ったリソースロードのwaterfall分析、コネクション数の削減、preload、prerendering、CSSのインライン化、Code Splittingなどについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Backbone.Model に 型をつけて剥がす - Typing to destroy Backbone.Model - Speaker Deck
[speakerdeck.com/fsubal/backbone-dot-model-ni-xing-wotuketebo-gasu-typing-to-destroy-backbone-dot-model?slide&#x3D;34](https://speakerdeck.com/fsubal/backbone-dot-model-ni-xing-wotuketebo-gasu-typing-to-destroy-backbone-dot-model?slide=34 "Backbone.Model に 型をつけて剥がす - Typing to destroy Backbone.Model - Speaker Deck")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">backbone.js</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">slide</span> <span class="jser-tag">refacoring</span></p>

Backbone.Modelに型をつけてリファクタリングしていく話。
Backbone.ModelをただのJSONとして扱い、JSONのスナップショットに対してテスト行う


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## faboulaws/fakingoose: An automatic fixture generator for mongoose using the schema definition
[github.com/faboulaws/fakingoose](https://github.com/faboulaws/fakingoose "faboulaws/fakingoose: An automatic fixture generator for mongoose using the schema definition")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

データスキーマからダミデータを生成してくれるライブラリ


----
