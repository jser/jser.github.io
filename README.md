# JSer.info [![Actions Status: Deploy](https://github.com/jser/jser.github.io/workflows/Deploy/badge.svg)](https://github.com/jser/jser.github.io/actions?query=workflow%3A"Deploy")

JSer.info のブログリポジトリです。

* [Jekyll](http://jekyllrb.com/) + GitHub Actions + [GitHub Pages](https://pages.github.com/)で動いています
* 記事に対してtypo等の内容の修正をPull Requestできます
    * `develop` ブランチ(デフォルトブランチ)のMarkdownファイルに対して修正を送って下さい。
    * `master` ブランチのhtmlは自動的に生成されたファイルとなっています。
* 記事の元となるデータ等は[jser/jser.info](https://github.com/jser/jser.info "jser/jser.info")で管理しています。

### NOTE

JSer.info に関するIssueは以下のどちらに立てても問題ありません。

* [jser/jser.github.io](https://github.com/jser/jser.github.io "jser/jser.github.io") 
* [jser/jser.info](https://github.com/jser/jser.info "jser/jser.info")

しいて分けるなら、以下のような感じです。

* [jser/jser.github.io](https://github.com/jser/jser.github.io "jser/jser.github.io") はサイトそのものについて
* [jser/jser.info](https://github.com/jser/jser.info "jser/jser.info") はその他全般

JSer.infoのSlackワークスペースは次のURLから参加できます。
JSer.infoに関する質問を気軽にしていただいて大丈夫です。

[JSer.info Slack](https://join.slack.com/t/jserinfo/shared_invite/zt-g2shzp7o-f_tj6OaphCAFw5Qlt2Jw0A)

## Installation

``` sh
# テストやJavaScript関係
npm install
# Jekyllのインストールとビルド
bundle install
```

## Usage

### Jekyllのビルド

```
bundle exec jekyll build
```

### Tests

```
npm test
```

## Contributing

サイト記事上部の **Edit on GitHub** 又は 下部の **この記事へ修正リクエストをする** から修正を送れます。

記事からGitHubで直接編集してpull requestを送ることが出来ます。

ちょっとした誤字脱字でもご気軽に修正を送ってくださると助かります。
詳しくは[CONTRIBUTING.md](./CONTRIBUTING.md)を読んでみるといいです。

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

* `_post/*` : CC-BY
* Other: MIT

[![CC-BY](https://licensebuttons.net/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
