---
title: "2022-01-11のJS: グローバルなサイトにおけるCore Web Vitals、2021 JavaScript Rising Stars、colors.jsのインシデント対応"
author: "azu"
layout: post
date : 2022-01-11T03:01:30.504Z
category: JSer
tags:
- performance
- browser
- CSS
- Tools
- debug

---

JSer.info #574 - [Improving Core Web Vitals, A Smashing Magazine Case Study](https://www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/)という記事では、Smashing MagazineのCore Web Vitals(LCP/FID/CLS)のスコアをどのように改善していったかについて書かれています。

Core Web VitalsはGoogle検索の指標に使われています。
また、Google Search Consoleでは、グローバルなChromeユーザーからのCore Web Vitalsのスコアを確認でき、この値は[Chrome User Experience Report ](https://developers.google.com/web/tools/chrome-user-experience-report)のデータを元にしています。

サイトのLCPの改善をしたところ、なぜかGoogle Search Consoleの結果は改善されなかったという問題を掘り下げていったというないようになっています。
Smashing Magazineはグローバルなサイトであり、Google Search Consoleのスコアはグローバルなデータをまとめたものとなるため、ユーザーが多い特定の国でスコアが悪いと、全体のスコアにも影響がある点について書かれています。

----

2021年のGitHub Star数でのランキングをまとめたJavaScript Rising Starsが公開されています。

- [2021 JavaScript Rising Stars](https://risingstars.js.org/2021/en)
- 日本語訳: [JavaScript ライジングスター 2021](https://risingstars.js.org/2021/ja)

GitHub Starは実際の人気の利用数とは必ずしも一致はしませんが、
それぞれのカテゴリごとに解説も書かれているので読んでみるとよさそうです。

----

[colorsなどのnpmパッケージに悪意あるコードが含まれている問題について](https://zenn.dev/azu/articles/d56615b2e11ad1)という記事では、`colors`というnpmパッケージにDoS攻撃のコードが含まれたものがpatchバージョンとして公開された問題について書かれています。

npmでは[leftpadと呼ばれる問題](https://web.archive.org/web/20160323000303/https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c)をきっかけに、パッケージのOwnerであっても公開後24時間経過するとその公開を取り下げるには問い合わせが必要になっています。(細かな条件が2020年に追加されています)

- [npm Blog Archive: changes to npm’s unpublish policy](https://blog.npmjs.org/post/141905368000/changes-to-npms-unpublish-policy)
- [npm Blog Archive: Changes to npm Unpublish Policy - January 2020](https://blog.npmjs.org/post/190553543620/changes-to-npmunpublish-policy-january-2020.html)

また、npmやyarnなどでロックファイルがデフォルトとなっているため、既存のプロジェクトではバージョンが固定でき、影響範囲がleftpadの時に比べて小さくなっています。
一方で、`colors`を新規インストールした際やアップデートした際に、問題があるpatchバージョンがsemverによって選択されてしまう問題があります。

この記事では、npmパッケージの直接的/間接的依存のチェック方法やYarnの`resolutions`、npm 8.3+の`overrides`での明示的なバージョン固定方法について書かれています。

現時点(2022-01-11)では、問題のあった`colors`のバージョンはnpmによって取り消されています。
今後のcolors.jsについては、次のIssueを参照してください。

- [(Semi-Official) Status Update · Issue #317 · Marak/colors.js](https://github.com/Marak/colors.js/issues/317)

----

<h1 class="site-genre">ヘッドライン</h1>

----

## January 10th 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/jan-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/jan-2022-security-releases/ "January 10th 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">security</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのセキュリティ修正が12.x, 14.x, 16.x, 17.x それぞれでリリースされている。
Subject Alternative Name (SAN)に関する修正が2つ含まれていて、この修正は`--security-revert`フラグで戻すことができる。
また、Relative Distinguished Namesの扱いに関する修正や`console.table`のPrototype Pollutionの修正が含まれている

- [Release 2022-01-10, Version 14.18.3 &#039;Fermium&#039; (LTS), @richardlau · nodejs/node](https://github.com/nodejs/node/releases/tag/v14.18.3 "Release 2022-01-10, Version 14.18.3 &amp;#039;Fermium&amp;#039; (LTS), @richardlau · nodejs/node")

----

## Chromium Blog: Chrome 98 Beta: Color Gradient Vector Fonts, Region Capture Origin Trial, and More
[blog.chromium.org/2022/01/chrome-98-beta-color-gradient-vector.html](https://blog.chromium.org/2022/01/chrome-98-beta-color-gradient-vector.html "Chromium Blog: Chrome 98 Beta: Color Gradient Vector Fonts, Region Capture Origin Trial, and More")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">ReleaseNote</span></p>

Chrome 98 betaリリース。
COLRv1 Color Gradient Vector Fontsのサポート、Chromeのバージョン100をテストできるフラグの追加。
Origin Trialとして、Region Captureの追加。
その他では、`contains-intrinsic-size: auto`のサポート、`AudioContext.outputLatency`のサポート、`color-scheme`での`only`のサポート。
`structuredClone()`のサポート、SubresourcesからPrivate Networkへのアクセス時にPreflight Requestが求められるように変更など


----
<h1 class="site-genre">アーティクル</h1>

----

## Improving Core Web Vitals, A Smashing Magazine Case Study
[www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/](https://www.smashingmagazine.com/2021/12/core-web-vitals-case-study-smashing-magazine/ "Improving Core Web Vitals, A Smashing Magazine Case Study")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

Core Web Vitalsの改善とCrUXのメトリクスを掘り下げた記事。
LCPなどを改善したが、CrUXのデータが改善されなかった点を掘り下げていき、特定地域のデータによって統計データが歪んでいたことを特定した方法について。
CDNがカバーしきれてない地域などが問題となっていたため、`SaveData`ヘッダと`prefers-reduced-data`を元にWeb Fontのロードを減らした話。


----

## 2021 JavaScript Rising Stars
[risingstars.js.org/2021/en](https://risingstars.js.org/2021/en "2021 JavaScript Rising Stars")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">Tools</span> <span class="jser-tag">article</span> <span class="jser-tag">Github</span></p>

JavaScript関係のツールやライブラリなどの2021年のGitHub Starでのランキング。
各カテゴリごとのランキングやコメントも合わせて紹介されている。

- [JavaScript ライジングスター 2021](https://risingstars.js.org/2021/ja "JavaScript ライジングスター 2021")

----

## Container Queries | 12 Days of Web
[12daysofweb.dev/2021/container-queries/](https://12daysofweb.dev/2021/container-queries/ "Container Queries | 12 Days of Web")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS Container queryの定義、利用方法、ユースケースについて


----

## Introducing fuite: a tool for finding memory leaks in web apps | Read the Tea Leaves
[nolanlawson.com/2021/12/17/introducing-fuite-a-tool-for-finding-memory-leaks-in-web-apps/](https://nolanlawson.com/2021/12/17/introducing-fuite-a-tool-for-finding-memory-leaks-in-web-apps/ "Introducing fuite: a tool for finding memory leaks in web apps | Read the Tea Leaves")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span> <span class="jser-tag">Tools</span></p>

fuiteというメモリリークのデバッグツールについて。
Puppeteerを使ってシナリオベースの操作をし、指定回数繰り返した結果のメモリリークを確認できる。
実行時にBreak Pointを貼ってブラウザの処理を止め、Chrome DevToolsと接続して開発者ツールによってデバッグができる。

- [nolanlawson/fuite: A tool for finding memory leaks in web apps](https://github.com/nolanlawson/fuite "nolanlawson/fuite: A tool for finding memory leaks in web apps")
- [Fixing memory leaks in web applications | Read the Tea Leaves](https://nolanlawson.com/2020/02/19/fixing-memory-leaks-in-web-applications/ "Fixing memory leaks in web applications | Read the Tea Leaves")
- [Debugging a memory leak with fuite - YouTube](https://www.youtube.com/watch?v=H0BHL2lo89M "Debugging a memory leak with fuite - YouTube")

----

## Web Performance Calendar » JS Self-Profiling API In Practice
[calendar.perfplanet.com/2021/js-self-profiling-api-in-practice/](https://calendar.perfplanet.com/2021/js-self-profiling-api-in-practice/ "Web Performance Calendar » JS Self-Profiling API In Practice")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScript Self-Profiling APIについての解説記事。
サンプリングされたプロファイルを取るAPIとなっていて、RUMのような実際のエンドユーザーでの実行結果を取得できる。
Document Policyでの有効化、APIの使い方、ユースケース、プロファイルのデータ形式と取得データの制限などについて。
CORSに対応していないCross-Origin ScriptsのJavaScript関数は、プロファイル上では見えないことやJS以外のデータがプロファイルに入らない点などについて。

- [WICG/js-self-profiling: Proposal for a programmable JS profiling API for collecting JS profiles from real end-user environments](https://github.com/WICG/js-self-profiling "WICG/js-self-profiling: Proposal for a programmable JS profiling API for collecting JS profiles from real end-user environments")

----

## Frontend Web Performance: The Essentials \[0\] | by Matthew Costello | Dec, 2021 | Medium
[medium.com/@matthew.costello/frontend-web-performance-the-essentials-0-61fea500b180](https://medium.com/@matthew.costello/frontend-web-performance-the-essentials-0-61fea500b180 "Frontend Web Performance: The Essentials \[0\] | by Matthew Costello | Dec, 2021 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">performance</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

ウェブパフォーマンスやブラウザのレンダリングについての記事。
Chrome開発者ツールでLayout, Paint, Compositeとはどのようなレンダリングステップで行われているのかみていく記事。
CSS Animationを例に、Chrome開発者ツールでそれぞれのレンダリングステップを可視化する方法について書かれている


----

## colorsなどのnpmパッケージに悪意あるコードが含まれている問題について
[zenn.dev/azu/articles/d56615b2e11ad1](https://zenn.dev/azu/articles/d56615b2e11ad1 "colorsなどのnpmパッケージに悪意あるコードが含まれている問題について")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">npm</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

colors.jsにDoS攻撃のコードを入れたものがpublishされていた問題について。
npmパッケージの直接的/間接的依存のチェック方法やYarnの`resolutions`、npm 8.3+の`overrides`でのバージョン固定方法について。


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## shiguredo/media-processors: Media Processors
[github.com/shiguredo/media-processors](https://github.com/shiguredo/media-processors "shiguredo/media-processors: Media Processors")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">video</span> <span class="jser-tag">audio</span> <span class="jser-tag">library</span></p>

背景ぼかしやノイズ抑制など処理をブラウザで行うライブラリ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## mozilla/glean: Modern cross-platform telemetry
[github.com/mozilla/glean](https://github.com/mozilla/glean "mozilla/glean: Modern cross-platform telemetry")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">kotlin</span> <span class="jser-tag">swift</span> <span class="jser-tag">python</span> <span class="jser-tag">node.js</span> <span class="jser-tag">library</span> <span class="jser-tag">performance</span> <span class="jser-tag">Mozilla</span> <span class="jser-tag">Rust</span></p>

Rust/Kotlin/Swift/Python/JavaScript(ブラウザとブラウザ拡張とNode.js)/Qtに対応したクロスプラットフォームなTelemetry SDK


----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## AntoineW/luge: Luge
[github.com/AntoineW/luge](https://github.com/AntoineW/luge "AntoineW/luge: Luge")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CSS</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">animation</span></p>

HTMLに属性を指定することでアニメーションできるライブラリ


----
<h1 class="site-genre">書籍関係</h1>

----

## New JavaScript features • JavaScript for impatient programmers (ES2022 edition)
[exploringjs.com/impatient-js/ch\_new-javascript-features.html#new-in-es2022](https://exploringjs.com/impatient-js/ch_new-javascript-features.html#new-in-es2022 "New JavaScript features • JavaScript for impatient programmers (ES2022 edition)")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">book</span></p>

JavaScript for impatient programmers (ES2022 edition)リリース。
ES2022のPrivate/Public Fields、Top-level await、Error Cause。
ArrayとStringの`.at()`メソッド、RegExp match indices、`Object.hasOwn()`メソッドについて追加されている。


----
