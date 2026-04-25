# RSS to Bluesky workflow design

## 概要

JSer.info の RSS フィードを Bluesky (`@jser.info`) に自動投稿する GitHub Actions workflow を追加する。既存の Mastodon workflow (`rss-to-mastodon.yml`) と同じ構造で、`joschi/blueskyfeedbot` を使用する。

## 動機

- 既存の Mastodon (`@jser@mstdn.jp`) と Twitter への投稿に加え、Bluesky (`@jser.info`) でも更新を配信する
- Bluesky アカウントは既に存在: <https://bsky.app/profile/jser.info> (DID: `did:plc:fqprbc6qtifjv7cpx5vjhwgq`)

## 設計

### ファイル

`.github/workflows/rss-to-bluesky.yml` を新規追加する。

### Action

`joschi/blueskyfeedbot` を使用する。

- バージョン: v1 (`ded1962e3afb0d7283f49a037bf4d4fd9d7b86ad`)
- 既存の workflow と同じく commit SHA で pinning する
- 参照: <https://github.com/joschi/blueskyfeedbot>

### トリガー

- `schedule: '*/5 * * * *'` (5分毎)
- `workflow_dispatch` (手動実行用)

5分毎にする理由: Bluesky 投稿は public な情報のみで、Mastodon (15分毎) より低レイテンシで配信したい。`joschi/blueskyfeedbot` の README デフォルトも 5 分。

### 投稿対象

| Job | RSS フィード | テンプレート |
|---|---|---|
| `realtime` | `https://realtime.jser.info/feed.xml` | `{{item.title}}\n{{item.link}}\n\n{{item.description}}` |
| `jser` | `https://jser.info/rss/` | `今週のJSer.infoを更新しました！\n{{item.title}}\n{{item.link}}` |

テンプレートは Mastodon と揃える。ただし `joschi/blueskyfeedbot` は Handlebars + `{{item.*}}` プレフィックスで、`jser/mastofeedbot` は `{{title}}` 形式なので、フィールド参照は読み替える。

### 共通設定

```yaml
service-url: https://bsky.social
username: ${{ secrets.JSER_BLUESKY_USERNAME }}
password: ${{ secrets.JSER_BLUESKY_PASSWORD }}
cache-file: ${{ github.workspace }}/blueskyfeedbot/cache.json
initial-post-limit: 1
```

`initial-post-limit: 1` を設定する理由: 初回実行時にキャッシュが無いと過去の RSS 全件が一気に投稿される可能性があるため、最初の 1 件だけに絞る。

### キャッシュ

各ジョブで個別の cache key を使用する (Mastodon workflow と同じパターン)。

- `realtime` ジョブ: `feed-cache-realtime-jser-info-bluesky-${cache-key}`
- `jser` ジョブ: `feed-cache-jser-info-bluesky-${cache-key}`

`actions/cache` と `actions/github-script` のバージョンも既存 workflow に合わせて pinning する。

### 並列実行制御

`concurrency: group: feedbot-bluesky` を設定し、ジョブが重複実行されないようにする。

## ユーザー側で必要な作業

1. <https://bsky.app/settings/app-passwords> で App Password を作成
2. リポジトリの Secrets に以下を追加:
   - `JSER_BLUESKY_USERNAME`: `jser.info`
   - `JSER_BLUESKY_PASSWORD`: 上で作成した App Password

## 影響範囲

- 新規ファイル `.github/workflows/rss-to-bluesky.yml` の追加のみ
- 既存の Mastodon/Twitter workflow には影響しない

## 検証方法

1. Secrets 設定後、`workflow_dispatch` で手動実行して動作確認
2. 初回は `initial-post-limit: 1` により最新記事 1 件のみ投稿されることを確認
3. 以降は新しい記事が出たタイミングで自動投稿されることを確認
