---
title: "2022-11-09のJS: Safari Technology Preview 157、hapi v21.0.0、Rome v10(Stable)"
author: "azu"
layout: post
date : 2022-11-09T03:08:56.671Z
category: JSer
tags:
- React
- Remix
- node.js
- Vue
- vite

---

JSer.info #617 - Safari Technology Preview 157がリリースされました。

- [Release Notes for Safari Technology Preview 157 | WebKit](https://webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/)

CSSの`@font-feature-settings`のサポート、ES2022のclass static initialization blocksのサポート、[WebCodecs API](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API)のサポートが改善されています。
[`Sec-Fetch-Site` HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site)ヘッダのサポート、Aレコードを使ったthird-party CNAME Cloakingに対するCookieの7日間制限を実装なども含まれています。

- [Cap cookie lifetimes to 7 days for responses from third party IP addresses by whsieh · Pull Request #5347 · WebKit/WebKit](https://github.com/WebKit/WebKit/pull/5347)

---

Node.jsのウェブアプリケーションフレームワークであるhapi v21.0.0がリリースされました。

- [Release v21.0.0 · hapijs/hapi](https://github.com/hapijs/hapi/releases/tag/v21.0.0)
- [21.0.0 Release Notes · Issue #4386 · hapijs/hapi](https://github.com/hapijs/hapi/issues/4386)

Node.js 12のサポート終了、JSONPのサポート終了し、Node.js 18のサポートの追加など。
またhapiのプラグインなどはhapi v20+以上のみをサポートするようになる変更も含まれています。

---

Rome v10がリリースされました。

- [Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript](https://rome.tools/blog/2022/11/08/rome-10.html)

Rustに書き換えてからの初のStableリリースとなるバージョンで、0.10.0から10.0.0へとバージョンが上がっています。
Stableの機能としてPrettierライクなFormatterとESLintライクなルールを含むLinterが利用できるようになっています。

----

{% include inline-support.html %}

----

<h1 class="site-genre">ヘッドライン</h1>

----

## vuetifyjs/vuetify: 🐉 Material Component Framework for Vue
[github.com/vuetifyjs/vuetify/releases/tag/v3.0.0](https://github.com/vuetifyjs/vuetify/releases/tag/v3.0.0 "vuetifyjs/vuetify: 🐉 Material Component Framework for Vue")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Vue</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

Vuetify v3.0.0リリース。
現時点では`vuetify@next`でインストールできる。


----

## Release v4.0.0-alpha.0 · vitejs/vite
[github.com/vitejs/vite/releases/tag/v4.0.0-alpha.0](https://github.com/vitejs/vite/releases/tag/v4.0.0-alpha.0 "Release v4.0.0-alpha.0 · vitejs/vite")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">vite</span> <span class="jser-tag">ReleaseNote</span></p>

Vite v4.0.0-alpha.0リリース。
rollup 3にアップグレード


----

## Release Notes for Safari Technology Preview 157 | WebKit
[webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/](https://webkit.org/blog/13575/release-notes-for-safari-technology-preview-157/ "Release Notes for Safari Technology Preview 157 | WebKit")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">safari</span> <span class="jser-tag">webkit</span> <span class="jser-tag">ReleaseNote</span></p>

Safari Technology Preview 157リリース。
CSSの`@font-feature-settings`のサポート、ES2022のclass static initialization blocksのサポート、WebCodecs APIのサポート改善。
`Sec-Fetch-Site` HTTPヘッダのサポート、Aレコードを使ったthird-party CNAME Cloakingに対するCookieの7日間制限を実装など。


----

## Release v21.0.0 · hapijs/hapi
[github.com/hapijs/hapi/releases/tag/v21.0.0](https://github.com/hapijs/hapi/releases/tag/v21.0.0 "Release v21.0.0 · hapijs/hapi")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">server</span> <span class="jser-tag">library</span> <span class="jser-tag">ReleaseNote</span></p>

hapi 21.0.0リリース。
Node.js 12のサポート終了、JSONPのサポート終了し、Node.js 18のサポートの追加など。
またhapiのプラグインなどはhapi v20+以上のみをサポートするようになる変更も含まれている

- [21.0.0 Release Notes · Issue #4386 · hapijs/hapi](https://github.com/hapijs/hapi/issues/4386 "21.0.0 Release Notes · Issue #4386 · hapijs/hapi")

----

## Deprecate array prototype extensions
[rfcs.emberjs.com/id/0848-deprecate-array-prototype-extensions/](https://rfcs.emberjs.com/id/0848-deprecate-array-prototype-extensions/ "Deprecate array prototype extensions")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Ember</span> <span class="jser-tag">proposal</span></p>

Ember.jsでの配列のprototype拡張をしないようにするProposal。
Ember.js 4.9.0ではprototype拡張をデフォルトで無効とする変更を入れる予定となっている

- [Release Release 4.9.0-beta.0 · ember-cli/ember-cli](https://github.com/ember-cli/ember-cli/releases/tag/v4.9.0-beta.0 "Release Release 4.9.0-beta.0 · ember-cli/ember-cli")

----

## Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript
[rome.tools/blog/2022/11/08/rome-10.html](https://rome.tools/blog/2022/11/08/rome-10.html "Announcing Rome v10 — first stable release of our fast linter and formatter for JavaScript and TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">Rust</span> <span class="jser-tag">Tools</span> <span class="jser-tag">ReleaseNote</span></p>

Rome v10リリース。
Rustに書き換えてからの初のStableリリース。
PrettierライクなFormatterとESLintライクなルールを含むLinterが利用できる


----

## Changelog | Cypress Documentation
[docs.cypress.io/guides/references/changelog#11-0-0](https://docs.cypress.io/guides/references/changelog#11-0-0 "Changelog | Cypress Documentation")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">browser</span> <span class="jser-tag">testing</span> <span class="jser-tag">E2E</span> <span class="jser-tag">ReleaseNote</span></p>

Cypress 11.0.0リリース。
コンポーネントテストのStable化、V8スナップショットを使った起動パフォーマンスの改善、`cy.*Cookie()` APIでドメインを指定できるように。
破壊的な変更として、コンポーネントのテストに関連するAPIや設定の変更など


----

## Nov 3 2022 Security Releases | Node.js
[nodejs.org/en/blog/vulnerability/november-2022-security-releases/](https://nodejs.org/en/blog/vulnerability/november-2022-security-releases/ "Nov 3 2022 Security Releases | Node.js")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">node.js</span> <span class="jser-tag">seuc</span> <span class="jser-tag">ReleaseNote</span></p>

Node.jsのセキュリティアップデートとしてそれぞれのバージョンが更新された

- Node.js v14.21.1 (LTS)
- Node.js v16.18.1 (LTS)
- Node.js v18.12.1 (LTS)
- Node.js v19.0.1 (Current)


----
<h1 class="site-genre">アーティクル</h1>

----

## React Router-ing Remix | Remix
[remix.run/blog/react-routering-remix](https://remix.run/blog/react-routering-remix "React Router-ing Remix | Remix")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Remix</span> <span class="jser-tag">article</span></p>

React RouterにRemixのData APIを移動した話。
破壊的な変更なしにどのように処理を移動しているかについて。Feature Flagを使いビルド時に処理を削って互換性を担保しつつ、新しい機能を試せるようにしていることについてなど。

- [React Router 6.4 Release | Remix](https://remix.run/blog/react-router-v6.4 "React Router 6.4 Release | Remix")

----

## Full Stack Components | Epic Web Dev by Kent C. Dodds
[www.epicweb.dev/full-stack-components](https://www.epicweb.dev/full-stack-components "Full Stack Components | Epic Web Dev by Kent C. Dodds")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Remix</span> <span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Remixの`useFetcher`を使った保留状態をもつUIコンポーネントの実装について


----

## What is a realm in JavaScript? · Gal Weizman
[weizman.github.io/page-what-is-a-realm-in-js/](https://weizman.github.io/page-what-is-a-realm-in-js/ "What is a realm in JavaScript? · Gal Weizman")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">ECMAScript</span> <span class="jser-tag">security</span> <span class="jser-tag">article</span></p>

Realmとは何かという解説記事。


----

## 個人ブログの Next.js v13 移行でやったことまとめ
[zenn.dev/panda\_program/scraps/6c66f160636969](https://zenn.dev/panda_program/scraps/6c66f160636969 "個人ブログの Next.js v13 移行でやったことまとめ")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Next.js</span> <span class="jser-tag">JavaScript</span> <span class="jser-tag">article</span></p>

Next.js 13へのアップデートについての記事。
`pages/`から`app/`への移行をした場合のコンポーネントの変更、外部ツールの対応などについて


----
