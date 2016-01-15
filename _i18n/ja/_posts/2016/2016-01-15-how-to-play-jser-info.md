---
title: "JSer.infoの遊び方"
author: azu
layout: post
date : 2016-01-15T10:01
category: 雑記
tags:
    - JSer

---

JSer.infoに関連するリポジトリやサイトの案内です。
JSer.info自体はただの情報発信ブログというよりは、見ている人も情報を追加できるし、そのデータを使って遊べるみたいなものを目指しています。

この記事はその辺の仕組みとかツールの紹介です。

## 新しい情報を見たい

- [JSer.info](http://jser.info/)
	- JSer.infoサイトそのもの
	- 週一回程度で更新
- [Realtime JSer.info](http://realtime.jser.info/)
	- JSer.infoのリアルタイム版
	- 元データが追加された時点で更新


## コミュニケーションを取りたい

- [Issues · jser/jser.info](https://github.com/jser/jser.info/issues "Issues · jser/jser.info")
	- JSer.infoに関連する意見や要望などを管理するIssue
- [![Gitter chat](https://badges.gitter.im/jser/jser.info.png)](https://gitter.im/jser/jser.info)
	- Gitterを利用したチャット
	- Issueを立てるまでもない指摘や感想、疑問、オススメ記事など迷ったらチャットへ

[Support - JSer.info](http://jser.info/support/ "Support - JSer.info")に書いていますが、[![Gitter chat](https://badges.gitter.im/jser/jser.info.png)](https://gitter.im/jser/jser.info)へ"こんなの書いてみました"とかそういうのも気軽に投げてもらって問題ないです。

## データや記事を修正したい

- [jser/jser.info](https://github.com/jser/jser.info "jser/jser.info")
	- サイトデータを修正したい場合
	- 記事として掲載後に元データを修正しても、自動的には記事へ反映はされません
- [jser/jser.github.io](https://github.com/jser/jser.github.io "jser/jser.github.io")
	- JSer.infoの記事を修正したい場合

記事上部の **Edit on GitHub** 又は 下部の **この記事へ修正リクエストをする** から該当記事の編集画面が開けます。

![掲載済みの記事へのpull-request](http://take.ms/suw5I)


## 紹介して欲しい記事/サイト/ライブラリがある

JSer.infoに載せて欲しい記事は[jser.info](https://github.com/jser/jser.info)へPull Requestできます。

ただしやっぱり手順が面倒であるので、Gitterを使ってもらっても良いです。

- [CONTRIBUTING.md](https://github.com/jser/jser.info/blob/gh-pages/CONTRIBUTING.md)
	- Pull Requestする方法などの手順がまとめられている
- [JSer.info Pull Request Form](http://jser.info/contributing/ "JSer.info Pull Request Form")
	- 掲載したい記事がある場合はこちらのフォームからPull Request
	- [jser/contributing-preview](https://github.com/jser/contributing-preview "jser/contributing-preview")
	- データの表示をプレビューする補助ツール

関連: [JSer.infoに紹介してもらいたい記事のPull Requestが出来るようになりました - JSer.info](http://jser.info/post/75446735069/jser-info-pull-request/ "JSer.infoに紹介してもらいたい記事のPull Requestが出来るようになりました - JSer.info")


## データを分析したい

JSer.infoのデータを分析したい場合はJSON APIとライブラリが用意されています。

- [http://jser.info/source-data/items.json](http://jser.info/source-data/items.json) 掲載サイトデータ
- [http://jser.info/posts.json](http://jser.info/posts.json) 記事データ

の２つのJSONを上手く扱える[jser/stat-js](https://github.com/jser/stat-js "jser/stat-js")というライブラリが用意されています。

- [jser/stat-js](https://github.com/jser/stat-js "jser/stat-js")
	- JSer.infoの掲載データを利用出来る統計処理ライブラリ
	- 特定の期間で紹介した記事一覧の取得、関連記事の検索など
- [JSer.info トレンド](http://jser.info/trends/ "JSer.info トレンド")
	- [jser/stat-js](https://github.com/jser/stat-js "jser/stat-js")を使ったキーワードトレンド情報のビューア

## 素材が欲しい

- [jser/media](https://github.com/jser/media "jser/media")
	- JSer.infoのロゴやアイコンなどの素材


## ライセンス

JSer.infoの記事やデータはCC-BY [![CC-BY](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)で利用できます。

ソースコードなどはMITライセンスです。

-------

## データの自動更新の仕組み

どんな感じで掲載サイトデータなどが更新されているかの仕組みの話です。

サイトデータのマスターは[jser/jser.info](https://github.com/jser/jser.info/ "jser/jser.info")で管理されています。
(月ごとにJSONでまとめられています)

[jser/jser.info](https://github.com/jser/jser.info/ "jser/jser.info")のデータが更新されると、CIが自動的に以下のリポジトリも更新します。

- [jser/realtime.jser.info](https://github.com/jser/realtime.jser.info "jser/realtime.jser.info")
	- JSONからMarkdownに変換されてpushされます。
	- [Realtime JSer.info](http://realtime.jser.info/ "Realtime JSer.info")に反映されます。
- [jser/source-data](https://github.com/jser/source-data "jser/source-data")
	- 掲載サイトデータを[jser/stat-js](https://github.com/jser/stat-js "jser/stat-js")向けにまとめています。
	- 全てのJSONを一つのファイルにマージしたものを作成。

JSer.infoのマスターはJSONデータで管理されていますが、最近はMarkdown + Yaml Headerで管理しているサイトも増えています。

- [WASM.NEWS | HowTo](https://wasm.news/contributing.html "WASM.NEWS | HowTo")
	- Jekyllを利用
- [mozilla/platatus: Project Platform Status](https://github.com/mozilla/platatus/ "mozilla/platatus: Project Platform Status")

JSONに比べてMarkdown + Yaml Headerはヒトが見てもわかりやすいのでPull Requestがしやすいです。
(また必然的に1コンテンツ1ファイルとなるので対応がわかりやすい)

この辺のデータの扱い方は今後もっと良くしていくかもしれません。
