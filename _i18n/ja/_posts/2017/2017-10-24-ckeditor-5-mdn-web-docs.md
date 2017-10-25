---
title: "2017-10-24のJS: CKEditor 5、MDN Web Docsへのドキュメント統合"
author: "azu"
layout: post
date : 2017-10-24T01:41:38.582Z
category: JSer
tags:
- MDN
- CKEditor
- CORS
- domain

---

JSer.info #354 - Mozilla、Microsoft、Google、W3Cが協調してウェブ開発のドキュメントを[MDN Web Docs](https://developer.mozilla.org/ "MDN Web Docs")に集約していくことを発表しました。

- [Mozilla brings Microsoft, Google, the W3C, Samsung together to create cross-browser documentation on MDN - The Mozilla Blog](https://blog.mozilla.org/blog/2017/10/18/mozilla-brings-microsoft-google-w3c-samsung-together-create-cross-browser-documentation-mdn/ "Mozilla brings Microsoft, Google, the W3C, Samsung together to create cross-browser documentation on MDN - The Mozilla Blog")

目に見える変化としては、MSDNのドキュメントがMDNにリダイレクトされていきます。
ブラウザ固有のドキュメントに関しては[Microsoft Edge documentation - Microsoft Edge Development | Microsoft Docs](https://docs.microsoft.com/ja-jp/microsoft-edge/ "Microsoft Edge documentation - Microsoft Edge Development | Microsoft Docs")などに残ります。

- [Documenting the Web together - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2017/10/18/documenting-web-together-mdn-web-docs/ "Documenting the Web together - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")

以前、Web Platform APIのドキュメントを統合しようという動きは[WebPlatform.org](https://webplatform.github.io/ "Your Web, documented. · WebPlatform.org")という試みが行われていましたが、2015年にdiscontinueとなっています。

-----

[CKEditor 5: A new era for rich text editing | CKEditor.com](https://ckeditor.com/blog/CKEditor-5-A-new-era-for-rich-text-editing/ "CKEditor 5: A new era for rich text editing | CKEditor.com")という記事ではリッチエディタライブラリであるCKEditor 5の変更点について書かれています。

- [ckeditor/ckeditor5: Development environment for CKEditor 5; the best browser-based rich text editor.](https://github.com/ckeditor/ckeditor5 "ckeditor/ckeditor5: Development environment for CKEditor 5; the best browser-based rich text editor.")

CKEditor 5では内部的にドキュメントモデルを持ち、エディタのインターフェースやAPI経由での変更はこのドキュメントモデルを操作するようになりました。
今まではContentEditable + プリプロセスで行っていたため、汚いHTMLが生成される場合もあります。ドキュメントモデルから一意なHTMLを出力できるようになっています。また、ドキュメントモデルからの出力先として[Markdownへの出力](https://docs.ckeditor.com/ckeditor5/latest/features/markdown.html "Markdown")などもできるようになっています。

このドキュメントモデルを内部的にもつアプローチは同様のリッチエディタでは採用されることが多くなっています。
[Draft.js](https://draftjs.org/ "Draft.js")、[ProseMirror](http://marijnhaverbeke.nl/blog/prosemirror-1.html "ProseMirror")、[Quill](https://github.com/quilljs/quill "Quill")の[Parchment](https://github.com/quilljs/parchment "Parchment")、[Trix](https://github.com/basecamp/trix#understanding-the-document-model "Trix")、[Slate](https://github.com/ianstormtaylor/slate "Slate")のdata modelなどが似たような仕組みを持っています。

興味がある人は合わせて見るとよいかもしれません。

----


<h1 class="site-genre">ヘッドライン</h1>

----

## What’s New in Microsoft Edge in the Windows 10 Fall Creators Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog
[blogs.windows.com/msedgedev/2017/10/17/edgehtml-16-fall-creators-update/](https://blogs.windows.com/msedgedev/2017/10/17/edgehtml-16-fall-creators-update/ "What’s New in Microsoft Edge in the Windows 10 Fall Creators Update - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">MSEdge</span> <span class="jser-tag">ReleaseNote</span></p>

MSEdge 16の変更点について。
CSS Grid Layout、object-fit、Payment Request APIのサポート。
Service Workerの試験的サポート、WebVR対応の改善など


----

## Release Notes for Safari Technology Preview 42 | WebKit
[webkit.org/blog/8001/release-notes-for-safari-technology-preview-42/](https://webkit.org/blog/8001/release-notes-for-safari-technology-preview-42/ "Release Notes for Safari Technology Preview 42 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 42リリース。
Payment Requestの機能実装、`font-display`の実装、`constant()`が`env()`にリネーム、`link rel=preconnect`、`import.meta`のサポート、Web InspectorにCanvasタブを追加など


----

## Mozilla brings Microsoft, Google, the W3C, Samsung together to create cross-browser documentation on MDN - The Mozilla Blog
[blog.mozilla.org/blog/2017/10/18/mozilla-brings-microsoft-google-w3c-samsung-together-create-cross-browser-documentation-mdn/](https://blog.mozilla.org/blog/2017/10/18/mozilla-brings-microsoft-google-w3c-samsung-together-create-cross-browser-documentation-mdn/ "Mozilla brings Microsoft, Google, the W3C, Samsung together to create cross-browser documentation on MDN - The Mozilla Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Mozilla</span> <span class="jser-tag">MS</span> <span class="jser-tag">google</span> <span class="jser-tag">W3C</span> <span class="jser-tag">document</span> <span class="jser-tag">news</span></p>

Mozilla、Microsoft、Googleなどがウェブ開発系のドキュメントをMDNへ集約することになった。

- [Documenting the Web together - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog](https://blogs.windows.com/msedgedev/2017/10/18/documenting-web-together-mdn-web-docs/ "Documenting the Web together - Microsoft Edge Dev BlogMicrosoft Edge Dev Blog")
- [Chromium Blog: Building unified documentation for the web](https://blog.chromium.org/2017/10/building-unified-documentation-for-web.html "Chromium Blog: Building unified documentation for the web")
- [W3C to work with MDN on Web Platform documentation | W3C Blog](https://www.w3.org/blog/2017/10/w3c-to-work-with-mdn-on-web-platform-documentation/ "W3C to work with MDN on Web Platform documentation | W3C Blog")

----

## CKEditor 5: A new era for rich text editing | CKEditor.com
[ckeditor.com/blog/CKEditor-5-A-new-era-for-rich-text-editing/](https://ckeditor.com/blog/CKEditor-5-A-new-era-for-rich-text-editing/ "CKEditor 5: A new era for rich text editing | CKEditor.com")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">editor</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

CKEditor 5の変更点について。
今までのアーキテクチャを一新し、編集するテキストをデータモデルとしてもつことでContentEditable特有の出力を回避できるように。
またエディタ共通の問題についてを扱うEditor Recommendationsサイトの公開など

- [Home | editor-recommendations](http://ckeditor.github.io/editor-recommendations/ "Home | editor-recommendations")

----
<h1 class="site-genre">アーティクル</h1>

----

## New in Chrome 62  |  Web  |  Google Developers
[developers.google.com/web/updates/2017/10/nic62](https://developers.google.com/web/updates/2017/10/nic62 "New in Chrome 62  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 62の変更点について。
 Network Information API、OpenType Variable Fonts、WebVRのorigin trialの開始など


----

## The 100% correct way to structure a React app (or why there’s no such thing)
[hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed "The 100% correct way to structure a React app (or why there’s no such thing)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">opinion</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Reactアプリケーションのディレクトリ構造について。
index.js or コンポーネント名.js、階層構造、exportするものについてなど


----

## Node.js Security Overview
[nemethgergely.com/nodejs-security-overview/](https://nemethgergely.com/nodejs-security-overview/ "Node.js Security Overview")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Node.jsと関連するエコスシステムのセキュリティについてをざっくりと。
Core、npm、express、security.txt、関連サービスやツールなどについて


----

## Introducing PayPal’s open-source cross-domain javascript suite
[medium.com/@bluepnume/introducing-paypals-open-source-cross-domain-javascript-suite-95f991b2731d](https://medium.com/@bluepnume/introducing-paypals-open-source-cross-domain-javascript-suite-95f991b2731d "Introducing PayPal’s open-source cross-domain javascript suite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

PayPalが使ってるクロスドメイン関係のライブラリまとめ。
`postMessage`を使ったやり取り、コンポーネント、Util、同期的なPromiseであるZalgoとsetTimeoutのブロックについて、CORSとiframeについてなど


----

## An imperative guide to forms in Vue.js – LogRocket
[blog.logrocket.com/an-imperative-guide-to-forms-in-vue-js-7536bfa374e0](https://blog.logrocket.com/an-imperative-guide-to-forms-in-vue-js-7536bfa374e0 "An imperative guide to forms in Vue.js – LogRocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Vueを使った各種フォーム要素の管理やバリデーションについての紹介記事


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## BlinkOn 8 - Tokyo, Japan - YouTube
[www.youtube.com/playlist?list&#x3D;PL9ioqAuyl6UK7Z0HHswBM5JgAp-izn\_3S](http://www.youtube.com/playlist?list=PL9ioqAuyl6UK7Z0HHswBM5JgAp-izn_3S "BlinkOn 8 - Tokyo, Japan - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">blink</span> <span class="jser-tag">video</span> <span class="jser-tag">イベント</span></p>

BlinkOn 8の動画一覧

- [BlinkOn 8 Information - Google ドキュメント](https://docs.google.com/document/d/11Y1MK-jVQl_xlhFS8dds_6FsC70jQ_9aOtcWALBiz5k/edit "BlinkOn 8 Information - Google ドキュメント")

----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## prantlf/nettime: Prints timings of a HTTP/S request, including DNS lookup, TLS handshake etc.
[github.com/prantlf/nettime](https://github.com/prantlf/nettime "prantlf/nettime: Prints timings of a HTTP/S request, including DNS lookup, TLS handshake etc.")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">Tools</span> <span class="jser-tag">network</span></p>

特定のURLに対するDNS LookupやTCPコネクションの時間などネットワークの接続や通信にかかった時間を計測するCLI


----

## Micro Frontends - extending the microservice idea to frontend development
[micro-frontends.org/](https://micro-frontends.org/ "Micro Frontends - extending the microservice idea to frontend development")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">architecture</span> <span class="jser-tag">組織</span></p>

Micro Frontendsについて。
マイクロサービスアーキテクチャ的な考えをフロントエンドの中にも適応していく話。
機能でのチーム分割、独立したコンポーネントとWeb Components、ナビゲーションなど各トピックごとの実現方法についてを書いていくとのこと

- [Micro frontends | Technology Radar | ThoughtWorks](https://www.thoughtworks.com/radar/techniques/micro-frontends "Micro frontends | Technology Radar | ThoughtWorks")

----

## Chrome User Experience Report  |  Tools for Web Developers  |  Google Developers
[developers.google.com/web/tools/chrome-user-experience-report/](https://developers.google.com/web/tools/chrome-user-experience-report/ "Chrome User Experience Report  |  Tools for Web Developers  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">統計</span></p>

Chromeの使用統計データを元にしたoriginごとのRUMを集めたBigQueryのデータセット。
origin、通信タイプ、デバイスの種類、first_paintのヒストグラムを扱うデータセット。

- [Chromium Blog: Introducing the Chrome User Experience Report](https://blog.chromium.org/2017/10/introducing-chrome-user-experience-report.html "Chromium Blog: Introducing the Chrome User Experience Report")

----

## HTTP Archive (beta)
[beta.httparchive.org/](http://beta.httparchive.org/ "HTTP Archive (beta)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">統計</span></p>

新しいHTTP Archiveのβ版が公開された。
lighthouseを使ったLoad Speed関連の統計データやDesktopとmobileの比較データなどをみることができる

- [HTTP Archive on Twitter: &#34;Excited to share the open beta for the new HTTP Archive. Check it out at https://t.co/MmiFOKXTrM and let us know what you think! 1/3… https://t.co/ycJ03nMkEj&#34;](https://twitter.com/HTTPArchive/status/922582514010488832 "HTTP Archive on Twitter: &amp;#34;Excited to share the open beta for the new HTTP Archive. Check it out at https://t.co/MmiFOKXTrM and let us know what you think! 1/3… https://t.co/ycJ03nMkEj&amp;#34;")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## dollarshaveclub/es-check: Checks the version of ES in JavaScript files with simple shell commands 🏆
[github.com/dollarshaveclub/es-check](https://github.com/dollarshaveclub/es-check "dollarshaveclub/es-check: Checks the version of ES in JavaScript files with simple shell commands 🏆")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span></p>

Acornを使って特定のECMAScriptバージョンでパースできるかをテストするツール。
コードが構文的にそのECMAScriptバージョンをサポートしてるかチェックできる


----

## kbrsh/wade: Blazing fast, 1kb search for Javascript
[github.com/kbrsh/wade](https://github.com/kbrsh/wade "kbrsh/wade: Blazing fast, 1kb search for Javascript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

深さ優先探索で文字列検索を行うライブラリ

- [Inside Wade | Kabir Shah](https://blog.kabir.ml/posts/inside-wade.html "Inside Wade | Kabir Shah")

----

## EyeJS - testing framework
[eye.js.org/](https://eye.js.org/ "EyeJS - testing framework")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">testing</span> <span class="jser-tag">library</span></p>

nodeとbrowserのモードを持ったテストフレームワーク。


----
