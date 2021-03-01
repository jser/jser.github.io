---
title: "2021-03-02のJS: Bundle Size以外のJavaScriptパフォーマンス、CORS 完全手冊"
author: "azu"
layout: post
date : 2021-03-01T21:33:41.685Z
category: JSer
tags:
- debug
- React
- Chrome
- CSS
- performance

---

JSer.info #529 - [JavaScript performance beyond bundle size | Read the Tea Leaves](https://nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/)という記事では、JavaScriptのパフォーマンス測定について書かれています。
最近では、Bundle Sizeについては[BundlePhobia](https://bundlephobia.com/)や[Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)など分かりやすく測定するツールがありますが、それ以外のJavaScriptのパフォーマンスのメトリクスについて書かれています。

ランタイムのCPUコスト、電力消費量、メモリ使用量、ディスクの使用量などのBundle Size以外のメトリクスをどのように見るのかについてまとめられています。

---

[CORS 完全手冊](https://blog.huli.tw/2021/02/19/cors-guide-1/)というCORSについての連載記事では、
CORSの概念、対応方法、よくある間違い、CORB/CORP/COEP/COOPなど最近のオリジン関連のルール、セキュリティ的な問題について書かれています。

- [CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？](https://blog.huli.tw/2021/02/19/cors-guide-1/)
  - クロスオリジンリクエストとは何か? CORSエラーはなぜおきるのかについて 
- [CORS 完全手冊（二）：如何解決 CORS 問題？](https://blog.huli.tw/2021/02/19/cors-guide-2/)
  - CORS対応の仕方(expressを例にしている)
- [CORS 完全手冊（三）：CORS 詳解](https://blog.huli.tw/2021/02/19/cors-guide-3/)
  - CORSの仕組み、それぞれのヘッダの意味をシナリオと合わせて解説している
- [CORS 完全手冊（四）：一起看規範](https://blog.huli.tw/2021/02/19/cors-guide-4/)
  - CORSの仕様を[Fetch Standard](https://fetch.spec.whatwg.org/)と共に解説。`Vary`ヘッダでのキャッシュの注意点についても書かれている
- [CORS 完全手冊（五）：跨來源的安全性問題](https://blog.huli.tw/2021/02/19/cors-guide-5/)
  - `res.headers['Access-Control-Allow-Origin'] = req.headers['Origin']` のようにOriginをオウム返しするよくある設定ミス(脆弱性)について
  - CORB/CORP/COEP/COOPとSite Isolationについて
- [CORS 完全手冊（六）：總結、後記與遺珠](https://blog.huli.tw/2021/02/19/cors-guide-6/)
  - CORSのエラーのパターン分類、Origin Policy、CORSの細かな話など

CORSについて必要な知識がほとんど書かれているため、おすすめです。

----

<h1 class="site-genre">アーティクル</h1>

----

## Introducing Env: a better way to read environment variables in JavaScript - Human Who Codes
[humanwhocodes.com/blog/2021/02/introducing-env-javascript-environment-variables/](https://humanwhocodes.com/blog/2021/02/introducing-env-javascript-environment-variables/ "Introducing Env: a better way to read environment variables in JavaScript - Human Who Codes")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span> <span class="jser-tag">article</span></p>

環境変数のよくある問題を回避するライブラリについて


----

## CSS-in-JS support in DevTools  |  Web  |  Google Developers
[developers.google.com/web/updates/2021/02/css-in-js](https://developers.google.com/web/updates/2021/02/css-in-js "CSS-in-JS support in DevTools  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

Chrome 85 DevToolsのCSS-in-JSの対応について。
今まではCSSOM APIで追加されたルールのスタイルは編集できなかったが、編集できるようになったという話


----

## JavaScript performance beyond bundle size | Read the Tea Leaves
[nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/](https://nolanlawson.com/2021/02/23/javascript-performance-beyond-bundle-size/ "JavaScript performance beyond bundle size | Read the Tea Leaves")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

JavaScriptのBundle sizeとランタイムのCPUコスト、メモリ使用量、電力使用量の調べ方について。
Bundle SizeについてはBundlePhobiaやWeb Vitalsなどで分かるようになってきているが、パフォーマンスはもっと多面的なものであるため、他のメトリクスをどのように見るかについて

- [BundlePhobia ❘ cost of adding a npm package](https://bundlephobia.com/ "BundlePhobia ❘ cost of adding a npm package")

----

## How Web Content Can Affect Power Usage | WebKit
[webkit.org/blog/8970/how-web-content-can-affect-power-usage/](https://webkit.org/blog/8970/how-web-content-can-affect-power-usage/ "How Web Content Can Affect Power Usage | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

CPU、GPU、ネットワークなどが電力消費に与える影響について。
バックグラウンド時にCPU消費をなくす方法、Web InspectorのEnergy Impactの表示について


----

## Why JavaScript Developers Should Prefer Axios Over Fetch | by Sabesan Sathananthan | Feb, 2021 | Better Programming
[betterprogramming.pub/why-javascript-developers-should-prefer-axios-over-fetch-294b28a96e2c](https://betterprogramming.pub/why-javascript-developers-should-prefer-axios-over-fetch-294b28a96e2c "Why JavaScript Developers Should Prefer Axios Over Fetch | by Sabesan Sathananthan | Feb, 2021 | Better Programming")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Fetch</span> <span class="jser-tag">article</span></p>

Fetch APIとaxiosの比較。
レスポンスデータの自動変換、エラー処理、ダウンロードのprogress処理、アップロードのprogress処理、HTTPのインターセプト、タイムアウト、並列リクエストについて比較している


----

## Use CSS Variables instead of React Context | Epic React by Kent C. Dodds
[epicreact.dev/css-variables/](https://epicreact.dev/css-variables/ "Use CSS Variables instead of React Context | Epic React by Kent C. Dodds")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span></p>

CSS-in-JSを使ったThemeコンポーネントのようなテーマの切り替えをCSS Custom Propertiesで実装してみる話。
実装の違い、レンダリングフローの違いについて


----

## React Context を export するのはアンチパターンではないかと考える | stin&#039;s blog
[blog.stin.ink/articles/do-not-export-react-context](https://blog.stin.ink/articles/do-not-export-react-context "React Context を export するのはアンチパターンではないかと考える | stin&#039;s blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React Contextをモジュールからexportするのではなく、Custom Hookとしてexportするという話。


----

## CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？ - Huli
[blog.huli.tw/2021/02/19/cors-guide-1/](https://blog.huli.tw/2021/02/19/cors-guide-1/ "CORS 完全手冊（一）：為什麼會發生 CORS 錯誤？ - Huli")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">CORS</span> <span class="jser-tag">security</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

CORSの概念、対応方法、よくある間違い、CORB/CORP/COEP/COOPなどオリジン関連のルール、セキュリティ的な問題についての連載記事。
クロスオリジンリクエストはなぜブロックされるのか、CORSの仕様解説、CORSのキャッシュ、CORSの設定ミスなどについて


----

## What&#039;s New In DevTools (Chrome 90)  |  Web  |  Google Developers
[developers.google.com/web/updates/2021/02/devtools](https://developers.google.com/web/updates/2021/02/devtools "What&#039;s New In DevTools (Chrome 90)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">debug</span> <span class="jser-tag">article</span></p>

Chrome 90のDev Toolsの変更点について。
CSS flexboxのデバッグツールの追加、Core Web Vitalsのオーバーレイ表示、
Issues tabの改善、CSS color-gamutのエミュレート機能の追加。
Dev Toolsを開いた状態でのデバッグのパフォーマンス改善、`fn.displayName`のサポートを非推奨化など


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## GoudekettingRM/link-overview-jsworld-2021
[github.com/GoudekettingRM/link-overview-jsworld-2021](https://github.com/GoudekettingRM/link-overview-jsworld-2021 "GoudekettingRM/link-overview-jsworld-2021")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span> <span class="jser-tag">slide</span></p>

JS World 2021のスライドや動画のまとめ

- [JS World - Online Conference by Frontend Love](https://frontenddeveloperlove.com/ "JS World - Online Conference by Frontend Love")

----
<h1 class="site-genre">ソフトウェア、ツール、ライブラリ関係</h1>

----

## jcubic/tagger: Zero Dependency, Vanilla JavaScript Tag Editor
[github.com/jcubic/tagger](https://github.com/jcubic/tagger "jcubic/tagger: Zero Dependency, Vanilla JavaScript Tag Editor")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

依存のないタグ入力UIライブラリ


----

## wynntee/joss: JOSS can serialize almost every JavaScript data type and data structure, so data can be seamlessly exchanged between browsers and servers (Deno or Node.js).
[github.com/wynntee/joss](https://github.com/wynntee/joss "wynntee/joss: JOSS can serialize almost every JavaScript data type and data structure, so data can be seamlessly exchanged between browsers and servers (Deno or Node.js).")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">library</span></p>

JOSSというJavaScriptオブジェクトのシリアライズ、デシアライズの仕様とそのリファレンス実装ライブラリ。
BigInt、循環参照、疎な配列、`-0`などJSONにはない部分もサポートしている。
ブラウザ、Node、Denoで動作する

- [JS Open Serialization Scheme](https://www.wynntee.com/projects/serialization/specification/index.html "JS Open Serialization Scheme")

----

## andrewcourtice/harlem: Simple, unopinionated, lightweight and extensible state management for Vue 3
[github.com/andrewcourtice/harlem](https://github.com/andrewcourtice/harlem "andrewcourtice/harlem: Simple, unopinionated, lightweight and extensible state management for Vue 3")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">library</span></p>

Vue 3向けのステート管理ライブラリ。
pluginでVue DevToolsへの対応や、SSR、Storage保存、トランザクション対応などができる。


----
<h1 class="site-genre">書籍関係</h1>

----

## React テスト応用、テストに悩む人へ
[zenn.dev/tkdn/books/react-testing-patterns](https://zenn.dev/tkdn/books/react-testing-patterns "React テスト応用、テストに悩む人へ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">testing</span> <span class="jser-tag">book</span></p>

ReactコンポーネントとHooksのテストについての書籍。


----
