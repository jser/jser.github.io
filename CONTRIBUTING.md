# Contributing

[JSer.info](http://jser.info/)記事上部の **Edit on GitHub**、又は、下部の **この記事へ修正リクエストをする** から修正を送れます。

![Pull Request](http://take.ms/suw5I)

記事からGitHubで直接編集してPull Requestを送ることが出来ます。

ちょっとした誤字脱字でもご気軽に修正を送ってくださると助かります。

## SpellCheck

[azu/technical-word-rules](https://github.com/azu/technical-word-rules "azu/technical-word-rules")の辞書を使った、用語統一のLintによるチェックがPull Requestに対して自動的に行われます。

![lint-image](http://monosnap.com/image/vE9DQn1451rGrWGSCQJrmth5cYzzIj.png)

### チェック対象となった場合の対応

Lint結果に対して以下のような対応を取ることが出来ます。

1. コメントに応じて修正する
2. [azu/technical-word-rules](https://github.com/azu/technical-word-rules "azu/technical-word-rules")の辞書を修正する
3. 例外的なので無視する(Lintの手法がおかしいなど)

辞書は完璧ではないので、辞書の方を直したほうが良い場合はコメントなどして下さい。

### ローカルでLintする方法

```
npm install
# 編集したファイルだけを対象にする場合
npm run textlint
# or ファイルを指定する場合
npm run lint -- /path/to/file.md
```

でLintをかけることが出来ます。
