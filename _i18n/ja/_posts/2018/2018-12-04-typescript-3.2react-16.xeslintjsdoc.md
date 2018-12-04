---
title: "2018-12-04のJS: TypeScript 3.2、React 16.xロードマップ、ESLintのビルトインJSDocサポート終了の予定"
author: "azu"
layout: post
date : 2018-12-04T00:33:24.889Z
category: JSer
tags:
- typescript
- react
- eslint
- JSDoc

---

JSer.info #412 - TypeScript 3.2が正式にリリースされました。

- [Announcing TypeScript 3.2 | TypeScript](https://blogs.msdn.microsoft.com/typescript/2018/11/29/announcing-typescript-3-2/)
- [TypeScript 3.2.0-RC 変更点 - Qiita](https://qiita.com/vvakame/items/79557e00cfe6d3c612cd)

`strictBindCallApply`オプションが追加され`bind`、`call`、`apply`の型付け改善、Object spread/restとGenericsの組み合わせを改善、BigIntサポート。

また`allowJs`の際に`Object.defineProperty`で宣言されたプロパティのチェック(`checkJs`)に対応しています。

`tsconfig.json`では既存の`tsconfig.json`を継承して拡張できますが、今まで`node_modules/`にある場合はそのままパスを書く必要がありました。

```json
{
    "extends": "../node_modules/@my-team/tsconfig-base/tsconfig.json",
    "include": ["./**/*"]
    "compilerOptions": {
        // Override certain options on a project-by-project basis.
        "strictBindCallApply": false,
    }
}
```

プロジェクトなどで`tsconfig.json`をnpmで配布して共有する場合には、少し不便でした。(たとえば、node_modulesがflatかどうかでパスが変わる可能性もあります)
そのため、3.2から`extends`が`node_modules/`以下を探索するようになったため、次のように書けます。

```json
{
    "extends": "@my-team/tsconfig-base",
    "include": ["./**/*"]
    "compilerOptions": {
        // Override certain options on a project-by-project basis.
        "strictBindCallApply": false,
    }
}
```

----

[React 16.x Roadmap – React Blog](https://reactjs.org/blog/2018/11/27/react-16-roadmap.html)ではReact 16.xのロードマップについて書かれています。

それぞれのminorアップデートや実装される予定の機能について書かれています。

- React 16.6 with Suspense for Code Splitting (already shipped)
- 16.7?: A minor 16.x release with React Hooks (~Q1 2019)
- 16.8?: A minor 16.x release with Concurrent Mode (~Q2 2019)
- 16.9?: A minor 16.x release with Suspense for Data Fetching (~mid 2019)

また合わせてReact DOMのリファクタリングやSuspenseのSSR対応なども勧めていく予定とのことです。

- [React Fire: Modernizing React DOM · Issue #13525 · facebook/react](https://github.com/facebook/react/issues/13525)

----

[End-of-Life for Built-in JSDoc Support in ESLint - ESLint - Pluggable JavaScript linter](https://eslint.org/blog/2018/11/jsdoc-end-of-life)という記事では、現在ESLintにビルトインで入っているJSDocサポートの今後について書かれています。

- [ESLint の組み込み JSDoc サポートが終了します - Qiita](https://qiita.com/mysticatea/items/09f9dd4ab2569cd4cd68)

ESLintコアで行っていたJSDoc周りのパーサやルールなどの開発を終了するという内容です。

これによりESLint本体から`require-jsdoc`などのJSDoc関係のサポートが終了され、次のメジャーアップデートで削除される可能性があります。
そのためコミュニティで開発されている[eslint-plugin-jsdoc](https://github.com/gajus/eslint-plugin-jsdoc)というプラグインへの移行が推奨されています。

- [Incorporating now deprecated ESLint jsdoc features · Issue #107 · gajus/eslint-plugin-jsdoc](https://github.com/gajus/eslint-plugin-jsdoc/issues/107)

ESLintが利用していたJSDocパーサである[doctrine](https://github.com/eslint/doctrine)も開発が終了され、現在アーカイブ化されています。
これはもともと[@constellation](https://github.com/Constellation)さんが開発し、ESLint/JS Foundationにtransferしたパッケージです。
JS Foundationでの開発を引き継ぐには手続きが煩雑になることから、Forkによる引き継ぎが推奨されています。

----

<h1 class="site-genre">ヘッドライン</h1>

----

## Dev.Opera — What’s new in Chromium 70 and Opera 57
[dev.opera.com/blog/opera-57/](https://dev.opera.com/blog/opera-57/ "Dev.Opera — What’s new in Chromium 70 and Opera 57")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Opera</span> <span class="jser-tag">ReleaseNote</span></p>

Opera 57 (based on Chromium 70)リリース。
Feature Detectionの混乱をさけるために`ontouch*`イベントの属性はデスクトップにおいてデフォルトで無効化、`postMessage`に`targetOrigin`オプションの追加。
Web Components V1を非推奨化など


----

## Announcing TypeScript 3.2 | TypeScript
[blogs.msdn.microsoft.com/typescript/2018/11/29/announcing-typescript-3-2/](https://blogs.msdn.microsoft.com/typescript/2018/11/29/announcing-typescript-3-2/ "Announcing TypeScript 3.2 | TypeScript")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">TypeScript</span> <span class="jser-tag">ReleaseNote</span></p>

TypeScript 3.2リリース。`strictBindCallApply`オプションが追加され`bind`、`call`、`apply`の型付け改善、Object spread/restとGenericsの組み合わせを改善、BigIntサポート。
`tsconfig.json`の`extends`がnode_modulesのパスに対応など


----
<h1 class="site-genre">アーティクル</h1>

----

## Lazy loading (and preloading) components in React 16.6
[medium.com/@pomber/lazy-loading-and-preloading-components-in-react-16-6-804de091c82d](https://medium.com/@pomber/lazy-loading-and-preloading-components-in-react-16-6-804de091c82d "Lazy loading (and preloading) components in React 16.6")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

`React.lazy()`を使ったコンポーネントの遅延ロードについて


----

## End-of-Life for Built-in JSDoc Support in ESLint - ESLint - Pluggable JavaScript linter
[eslint.org/blog/2018/11/jsdoc-end-of-life](https://eslint.org/blog/2018/11/jsdoc-end-of-life "End-of-Life for Built-in JSDoc Support in ESLint - ESLint - Pluggable JavaScript linter")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ESLint</span> <span class="jser-tag">article</span></p>

ESLintのJSDocサポートが4.0.0でビルトインではなくなることについて。
これにあわせてJSDocパーサのDoctrineも更新されなくなる。
既存のJSDoc関係のルールは別途プラグインとして切り出される。

- [eslint/doctrine: JSDoc parser](https://github.com/eslint/doctrine "eslint/doctrine: JSDoc parser")

----

## React 16.x Roadmap – React Blog
[reactjs.org/blog/2018/11/27/react-16-roadmap.html](https://reactjs.org/blog/2018/11/27/react-16-roadmap.html "React 16.x Roadmap – React Blog")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

React 16.xのロードマップについて。
16.7でReact Hooks、16.8でConcurrent Mode、16.9でSuspense for Data Fetchingをリリース予定。
また、React DOMのモダン化やSSRに対するSuspenseを検討中。


----

## What's New In DevTools (Chrome 72)  |  Web  |  Google Developers
[developers.google.com/web/updates/2018/11/devtools](https://developers.google.com/web/updates/2018/11/devtools "What's New In DevTools (Chrome 72)  |  Web  |  Google Developers")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">Chrome</span> <span class="jser-tag">article</span></p>

Chrome 72の開発者ツールの変更点。
Performance metricsのビジュアライズ、"Copy JS path"(セレクタを指定するコードのコピー)を追加、Lighthouseのアップデートなど


----

## Modern Frontend Testing with Cypress.io Framework - Snipcart
[snipcart.com/blog/frontend-testing-cypress](https://snipcart.com/blog/frontend-testing-cypress "Modern Frontend Testing with Cypress.io Framework - Snipcart")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">E2E</span> <span class="jser-tag">testing</span> <span class="jser-tag">article</span></p>

Cypressを使ったE2Eテストについてのチュートリアル


----

## Web workers vs Service workers vs Worklets
[bitsofco.de/web-workers-vs-service-workers-vs-worklets/](https://bitsofco.de/web-workers-vs-service-workers-vs-worklets/ "Web workers vs Service workers vs Worklets")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">webworker</span> <span class="jser-tag">webservice</span> <span class="jser-tag">article</span></p>

Web Worker、Service Worker、Workletsの役割や動作についてを簡単に紹介している記事。
ブラウザのメインスレッドとは異なるスレッドでコードを実行するWorkerについて


----

## ECMAScript proposal updates @ 2018-11 | ECMAScript Daily
[ecmascript-daily.github.io/ecmascript/2018/12/01/ecmascript-proposal-updates](https://ecmascript-daily.github.io/ecmascript/2018/12/01/ecmascript-proposal-updates "ECMAScript proposal updates @ 2018-11 | ECMAScript Daily")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">ECMAScript</span> <span class="jser-tag">proposal</span></p>

2018年11月のTC39ミーティングで変更があったECMAScript Proposalのステータスまとめ


----

## What’s new in Create React App 2 – LogRocket
[blog.logrocket.com/whats-new-in-create-react-app-2-fe8f4f448c75](https://blog.logrocket.com/whats-new-in-create-react-app-2-fe8f4f448c75 "What’s new in Create React App 2 – LogRocket")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Create React App 2.0での変更点について。
TypeScript対応、Service Workerがオプトインに変更、Babel macrosの対応、`src/setupProxy.js`の対応など


----

## How Does React Tell a Class from a Function? | Overreacted
[overreacted.io/how-does-react-tell-a-class-from-a-function/](https://overreacted.io/how-does-react-tell-a-class-from-a-function/ "How Does React Tell a Class from a Function? | Overreacted")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">article</span></p>

Reactが関数とクラスで書かれたコンポーネントを呼び分ける必要があるため、内部でどのように判別しているかについての解説


----

## CSS and Network Performance – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts
[csswizardry.com/2018/11/css-and-network-performance/](https://csswizardry.com/2018/11/css-and-network-performance/ "CSS and Network Performance – CSS Wizardry – CSS Architecture, Web Performance Optimisation, and more, by Harry Roberts")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">CSS</span> <span class="jser-tag">article</span> <span class="jser-tag">performance</span></p>

CSSのロードとパフォーマンスについての記事。
非同期ロード、`@import`を避ける、CSSとJSのロード順の問題などについて


----
<h1 class="site-genre">スライド、動画関係</h1>

----

## Scrimba
[scrimba.com/](https://scrimba.com/ "Scrimba")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">React</span> <span class="jser-tag">Angular</span> <span class="jser-tag">Vue</span> <span class="jser-tag">TypeScript</span> <span class="jser-tag">video</span> <span class="jser-tag">tutorial</span></p>

Angular、React、VueやTypeScriptなどのスクリーンキャストを公開しているサイト


----
<h1 class="site-genre">書籍関係</h1>

----

## The Second Edition of "Refactoring"
[martinfowler.com/articles/refactoring-2nd-ed.html](https://martinfowler.com/articles/refactoring-2nd-ed.html "The Second Edition of \"Refactoring\"")
<p class="jser-tags jser-tag-icon"><span class="jser-tag">JavaScript</span> <span class="jser-tag">book</span></p>

Refactoring 第二版がリリースされた


----
