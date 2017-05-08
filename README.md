# JSer.info [![Build Status](https://travis-ci.org/jser/jser.github.io.svg?branch=develop)](https://travis-ci.org/jser/jser.github.io) [![CircleCI](https://circleci.com/gh/jser/jser.github.io.svg?style=svg)](https://circleci.com/gh/jser/jser.github.io)

JSer.info のブログリポジトリです。

* [Jekyll](http://jekyllrb.com/ "Jekyll") + [Travis CI](https://travis-ci.org/jser/jser.github.io) + [GitHub Pages](https://pages.github.com/ "GitHub Pages")で動いています
* 記事に対してtypo等の内容の修正をPull Requestすることが出来ます
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

Gitterは共通で使用していますので、気になったことは以下に書き込んで下さい。

[![Gitter chat](https://badges.gitter.im/jser/jser.info.png)](https://gitter.im/jser/jser.info)

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
