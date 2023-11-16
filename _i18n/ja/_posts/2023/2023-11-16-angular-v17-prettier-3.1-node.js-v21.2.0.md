---
title: "2023-11-16のJS: Angular v17、Prettier 3.1、Node.js v21.2.0"
author: "azu"
layout: post
date: 2023-11-16T12:14:04.892Z
category: JSer
tags:
- Tools
- performance
- browser
- Angular
- astro

---

JSer.info #669 - - [Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog](https://blog.angular.io/introducing-angular-v17-4d7033312e4b)
- [Release v17.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/17.0.0)

----

- [Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier](https://prettier.io/blog/2023/11/13/3.1.0.html)

----

- [Node v21.2.0 (Current) | Node.js](https://nodejs.org/blog/release/v21.2.0)


----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog
[blog.angular.io/introducing-angular-v17-4d7033312e4b](https://blog.angular.io/introducing-angular-v17-4d7033312e4b "Introducing Angular v17. Last month marked the 13th anniversary… | by Minko Gechev | Nov, 2023 | Angular Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Angular</span> <span class="jser-tag">ReleaseNote</span></p>

Angular v17リリース。
Node.js 16のサポート終了、ドキュメントサイトの刷新、`@if`や`@for`などのbuilt-in control flowのサポート。
新しいプロジェクトでのSSRにおけるhydrationがデフォルトで有効に、`ng serve`と`ng build`にViteとesbuildを利用するようになるなど

- [Release v17.0.0 · angular/angular](https://github.com/angular/angular/releases/tag/17.0.0 "Release v17.0.0 · angular/angular")

----

## Astro 3.5: i18n Routing | Astro
[astro.build/blog/astro-350/](https://astro.build/blog/astro-350/ "Astro 3.5: i18n Routing | Astro")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">astro</span> <span class="jser-tag">ReleaseNote</span></p>

Astro 3.5リリース。
prefetchの機能をコアに統合、`<ViewTransitions handleForms />`を追加、`addMiddleware`を追加、Qwikのサポート。
実験的な機能としてi18n Routing APIを追加、`contentCollectionCache`オプションを追加など

- [Release astro@3.5.0 · withastro/astro](https://github.com/withastro/astro/releases/tag/astro%403.5.0 "Release astro@3.5.0 · withastro/astro")

----

## Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier
[prettier.io/blog/2023/11/13/3.1.0.html](https://prettier.io/blog/2023/11/13/3.1.0.html "Prettier 3.1: New experimental ternaries formatting and Angular control flow syntax! · Prettier")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Prettier 3.1リリース。
`--experimental-ternaries`で三項演算子の新しい整形ルールを試せるように。
Babel 7.23.0でサポートされた構文をサポート、Angular 17で追加されたcontrol flow構文のサポートなど


----

## Node v21.2.0 (Current) | Node.js
[nodejs.org/blog/release/v21.2.0](https://nodejs.org/blog/release/v21.2.0 "Node v21.2.0 (Current) | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">nodejs</span> <span class="jser-tag">ReleaseNote</span></p>

Node.js v21.2.0リリース。
`import.meta.dirname`と`import.meta.filename`を追加、`fs/promises`にスタックトレースを追加。
`navigator.language`/`navigator.platform`を追加、`--no-experimental-global-navigator`フラグを追加など。


----

## Project Status: Maintenance Reboot · Issue #5027 · mochajs/mocha
[github.com/mochajs/mocha/issues/5027](https://github.com/mochajs/mocha/issues/5027 "Project Status: Maintenance Reboot · Issue #5027 · mochajs/mocha")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">mocha</span> <span class="jser-tag">news</span> <span class="jser-tag">issue</span></p>

Mochaのプロジェクトをリブートしメンテナンスを再開するというアナウンス。


----

## Bun v1.0.12 | Bun Blog
[bun.sh/blog/bun-v1.0.12](https://bun.sh/blog/bun-v1.0.12 "Bun v1.0.12 | Bun Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Bun</span> <span class="jser-tag">ReleaseNote</span></p>

Bun v1.0.12リリース。
`bun -e "<code>"`のサポート、`bun --env-file <path>`のサポート、`import.meta.env`のサポート。
`expect.unreachable()`の追加、`mock.module(...)`の改善など


----
<h1 class="site-genre">アーティクル</h1>

----

## HTML DOM — Phuoc Nguyen
[phuoc.ng/collection/html-dom/](https://phuoc.ng/collection/html-dom/ "HTML DOM — Phuoc Nguyen")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">DOM</span> <span class="jser-tag">WebPlatformAPI</span> <span class="jser-tag">tutorial</span></p>

DOM APIを使った逆引きリファレンス的なサイト


----

## 仕様と実装から読み解くHTMLのloading属性 - dwango on GitHub
[dwango.github.io/articles/html-loading-attribute/](https://dwango.github.io/articles/html-loading-attribute/ "仕様と実装から読み解くHTMLのloading属性 - dwango on GitHub")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">HTML</span> <span class="jser-tag">browser</span> <span class="jser-tag">article</span></p>

ブラウザごとの`img`/`iframe`の`loading=lazy`の挙動の違いについて


----

## The end of third-party cookies and its impact on Miro apps and integrations | by Darren | Miro Engineering | Nov, 2023 | Medium
[medium.com/miro-engineering/the-end-of-third-party-cookies-and-its-impact-on-miro-apps-and-integrations-ee73358cda1e](https://medium.com/miro-engineering/the-end-of-third-party-cookies-and-its-impact-on-miro-apps-and-integrations-ee73358cda1e "The end of third-party cookies and its impact on Miro apps and integrations | by Darren | Miro Engineering | Nov, 2023 | Medium")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">browser</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

サードパーティCookieの廃止が埋め込みサイトに与える影響と対応策について。


----

## A faster web in 2024 - rviscomi.dev
[rviscomi.dev/2023/11/a-faster-web-in-2024/](https://rviscomi.dev/2023/11/a-faster-web-in-2024/ "A faster web in 2024 - rviscomi.dev")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">performance</span> <span class="jser-tag">article</span></p>

GoogleのWeb Vitalsの指標としてFID(First Input Delay)の代わりにINP(Interaction to Next Paint)を利用するようになる変更について。
INPを改善する方法としてのタスク分割、LCPとlazy loadingの問題、fetchpriotyやSpeculation Rules APIなどについて。


----

## Moving back to React
[daily.dev/blog/moving-back-to-react](https://daily.dev/blog/moving-back-to-react "Moving back to React")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span> <span class="jser-tag">refactoring</span></p>

Next.jsとの互換性のためPreactからReactへ移行した話。
PreactとReactの互換性の問題や実際に遭遇した問題についてなど


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## JetBrains JavaScript Day 2023 - YouTube
[www.youtube.com/playlist?list&#x3D;PLQ176FUIyIUZmRHOyz\_n9iy2qfHo4\_GRT](https://www.youtube.com/playlist?list=PLQ176FUIyIUZmRHOyz_n9iy2qfHo4_GRT "JetBrains JavaScript Day 2023 - YouTube")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Conference</span> <span class="jser-tag">video</span></p>

JetBrains JavaScript Day 2023の動画まとめ


----
<h1 class="site-genre">サイト、サービス、ドキュメント</h1>

----

## SpeedVitals - Website Speed Test &amp; Monitoring
[speedvitals.com/](https://speedvitals.com/ "SpeedVitals - Website Speed Test &amp; Monitoring")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webservice</span> <span class="jser-tag">performance</span> <span class="jser-tag">Tools</span></p>

WebPageTestのように場所とデバイスを指定してパフォーマンステストができるサービス。
URLを指定してLighthouseを使った計測データを閲覧できる


----
