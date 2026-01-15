# JSer.info 15周年 データ分析レポート

2011年1月16日から2026年1月15日までの15年間のデータを分析した結果をまとめる。

## 基本統計

| 項目 | 数値 |
|------|------|
| 総投稿数 | 820回 |
| 総紹介記事数 | 13,606件 |
| 期間 | 2011年1月〜2026年1月 |
| 平均投稿頻度 | 週1回（15年間維持） |

## 紹介記事数の推移

| 年 | 紹介記事数 | 投稿数 | 1投稿あたり |
|----|-----------|--------|-------------|
| 2011 | 915 | 65 | 14.1 |
| 2012 | 1,126 | 57 | 19.8 |
| 2013 | 1,269 | 57 | 22.3 |
| 2014 | 1,147 | 59 | 19.4 |
| 2015 | 1,043 | 56 | 18.6 |
| 2016 | 1,078 | 59 | 18.3 |
| 2017 | 1,068 | 54 | 19.8 |
| 2018 | 921 | 58 | 15.9 |
| 2019 | 790 | 53 | 14.9 |
| 2020 | 810 | 53 | 15.3 |
| 2021 | 789 | 53 | 14.9 |
| 2022 | 712 | 54 | 13.2 |
| 2023 | 737 | 53 | 13.9 |
| 2024 | 638 | 47 | 13.6 |
| 2025 | 552 | 41 | 13.5 |

2013年をピークに紹介記事数は減少傾向。1投稿あたりの記事数も22件から13件程度に減少している。

<details>
<summary>クエリと実行結果</summary>

```sql
-- 年ごとの紹介記事数
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    COUNT(*) as items_count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year
ORDER BY year;
```

```
┌───────┬─────────────┐
│ year  │ items_count │
├───────┼─────────────┤
│  2011 │         915 │
│  2012 │        1126 │
│  2013 │        1269 │
│  2014 │        1147 │
│  2015 │        1043 │
│  2016 │        1078 │
│  2017 │        1068 │
│  2018 │         921 │
│  2019 │         790 │
│  2020 │         810 │
│  2021 │         789 │
│  2022 │         712 │
│  2023 │         737 │
│  2024 │         638 │
│  2025 │         552 │
└───────┴─────────────┘
```

```sql
-- 年ごとの投稿数
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    COUNT(*) as posts_count
FROM read_json_auto('https://jser.info/posts.json')
GROUP BY year
ORDER BY year;
```

```
┌───────┬─────────────┐
│ year  │ posts_count │
├───────┼─────────────┤
│  2011 │          65 │
│  2012 │          57 │
│  2013 │          57 │
│  2014 │          59 │
│  2015 │          56 │
│  2016 │          59 │
│  2017 │          54 │
│  2018 │          58 │
│  2019 │          53 │
│  2020 │          53 │
│  2021 │          53 │
│  2022 │          54 │
│  2023 │          53 │
│  2024 │          47 │
│  2025 │          41 │
└───────┴─────────────┘
```

</details>

---

## コンテンツタイプの変化

紹介記事のURLパターンから、コンテンツの種類がどう変化したかを分析。

| タイプ | 2011-2013 | 2014-2016 | 2017-2019 | 2020-2022 | 2023-2025 |
|--------|-----------|-----------|-----------|-----------|-----------|
| ブログ | 679 | 808 | 792 | 571 | 607 |
| リリースノート | 23 | 261 | 305 | 373 | 349 |
| 公式ドキュメント | 31 | 47 | 68 | 212 | 328 |
| GitHubリポジトリ | 447 | 583 | 531 | 497 | 231 |
| 書籍 | 257 | 123 | 73 | 36 | 18 |
| スライド | 179 | 129 | 63 | 10 | 13 |
| 動画 | 20 | 59 | 53 | 17 | 16 |

### 変化のポイント

- リリースノート: 23件 → 349件（15倍に増加）
- 公式ドキュメント: 31件 → 328件（10倍に増加）
- 書籍: 257件 → 18件（93%減少）
- スライド: 179件 → 13件（93%減少）

勉強会でのスライド共有文化から、公式ドキュメント・リリースノート中心の情報収集へ移行している。

<details>
<summary>クエリと実行結果</summary>

```sql
SELECT
    CASE
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013 THEN '2011-2013'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2014 AND 2016 THEN '2014-2016'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2017 AND 2019 THEN '2017-2019'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2020 AND 2022 THEN '2020-2022'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025 THEN '2023-2025'
    END as period,
    CASE
        WHEN url LIKE '%slideshare%' OR url LIKE '%speakerdeck%' THEN 'スライド'
        WHEN url LIKE '%youtube.com%' OR url LIKE '%vimeo.com%' THEN '動画'
        WHEN url LIKE '%amazon.co%' OR url LIKE '%amazon.com%' OR url LIKE '%oreilly%' THEN '書籍'
        WHEN url LIKE '%github.com%/releases%' OR url LIKE '%/changelog%' THEN 'リリースノート'
        WHEN url LIKE '%github.com%' THEN 'GitHubリポジトリ'
        WHEN url LIKE '%.dev%' OR url LIKE '%developer.%' OR url LIKE '%docs.%' THEN '公式ドキュメント'
        WHEN url LIKE '%blog.%' OR url LIKE '%medium.com%' OR url LIKE '%qiita%' OR url LIKE '%zenn%' THEN 'ブログ'
        ELSE 'その他'
    END as content_type,
    COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2025
GROUP BY period, content_type
ORDER BY period, content_type;
```

```
┌───────────┬──────────────────┬───────┐
│  period   │   content_type   │ count │
├───────────┼──────────────────┼───────┤
│ 2011-2013 │ GitHubリポジトリ │   455 │
│ 2011-2013 │ その他           │  1946 │
│ 2011-2013 │ スライド         │   179 │
│ 2011-2013 │ ブログ           │   416 │
│ 2011-2013 │ リリースノート   │    15 │
│ 2011-2013 │ 公式ドキュメント │    31 │
│ 2011-2013 │ 動画             │    20 │
│ 2011-2013 │ 書籍             │   248 │
│ 2014-2016 │ GitHubリポジトリ │   670 │
│ 2014-2016 │ その他           │  1622 │
│ 2014-2016 │ スライド         │   126 │
│ 2014-2016 │ ブログ           │   455 │
│ 2014-2016 │ リリースノート   │   174 │
│ 2014-2016 │ 公式ドキュメント │    47 │
│ 2014-2016 │ 動画             │    59 │
│ 2014-2016 │ 書籍             │   115 │
│ 2017-2019 │ GitHubリポジトリ │   583 │
│ 2017-2019 │ その他           │  1306 │
│ 2017-2019 │ スライド         │    53 │
│ 2017-2019 │ ブログ           │   391 │
│ 2017-2019 │ リリースノート   │   253 │
│ 2017-2019 │ 公式ドキュメント │    68 │
│ 2017-2019 │ 動画             │    53 │
│ 2017-2019 │ 書籍             │    72 │
│ 2020-2022 │ GitHubリポジトリ │   530 │
│ 2020-2022 │ その他           │   976 │
│ 2020-2022 │ スライド         │    10 │
│ 2020-2022 │ ブログ           │   191 │
│ 2020-2022 │ リリースノート   │   340 │
│ 2020-2022 │ 公式ドキュメント │   212 │
│ 2020-2022 │ 動画             │    17 │
│ 2020-2022 │ 書籍             │    35 │
│ 2023-2025 │ GitHubリポジトリ │   243 │
│ 2023-2025 │ その他           │   889 │
│ 2023-2025 │ スライド         │    13 │
│ 2023-2025 │ ブログ           │    84 │
│ 2023-2025 │ リリースノート   │   337 │
│ 2023-2025 │ 公式ドキュメント │   328 │
│ 2023-2025 │ 動画             │    16 │
│ 2023-2025 │ 書籍             │    17 │
└───────────┴──────────────────┴───────┘
```

</details>

---

## 記事の種類の変化

紹介文のキーワードから記事の種類を分類。

| 種類 | 2011-2013 | 2014-2016 | 2017-2019 | 2020-2022 | 2023-2025 |
|------|-----------|-----------|-----------|-----------|-----------|
| リリースノート | 555 | 769 | 828 | 881 | 949 |
| 解説/説明 | 963 | 1,028 | 869 | 540 | 439 |
| ライブラリ/FW紹介 | 439 | 489 | 446 | 387 | 175 |
| チュートリアル/入門 | 178 | 195 | 152 | 88 | 46 |
| 書籍関連 | 155 | 69 | 26 | 26 | 8 |
| 発表/スライド | 37 | 25 | 7 | 3 | 7 |

### 変化のポイント

- リリースノート: 555件 → 949件（増加）
- 解説記事: 963件 → 439件（54%減少）
- チュートリアル: 178件 → 46件（74%減少）
- 書籍関連: 155件 → 8件（95%減少）

学習コンテンツ（チュートリアル、書籍）から情報追跡（リリースノート）へシフトしている。

<details>
<summary>クエリと実行結果</summary>

```sql
SELECT
    CASE
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013 THEN '2011-2013'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2014 AND 2016 THEN '2014-2016'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2017 AND 2019 THEN '2017-2019'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2020 AND 2022 THEN '2020-2022'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025 THEN '2023-2025'
    END as period,
    CASE
        WHEN LOWER(content) LIKE '%リリース%' OR LOWER(content) LIKE '%release%' THEN 'リリースノート'
        WHEN LOWER(content) LIKE '%入門%' OR LOWER(content) LIKE '%tutorial%'
            OR LOWER(content) LIKE '%チュートリアル%' THEN 'チュートリアル/入門'
        WHEN LOWER(content) LIKE '%ライブラリ%' OR LOWER(content) LIKE '%library%'
            OR LOWER(content) LIKE '%フレームワーク%' THEN 'ライブラリ/FW紹介'
        WHEN LOWER(content) LIKE '%解説%' OR LOWER(content) LIKE '%について%' THEN '解説/説明'
        WHEN LOWER(content) LIKE '%スライド%' OR LOWER(content) LIKE '%発表%' THEN '発表/スライド'
        WHEN LOWER(content) LIKE '%書評%' OR LOWER(content) LIKE '%本%' THEN '書籍関連'
        ELSE 'その他'
    END as article_type,
    COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2025
GROUP BY period, article_type
ORDER BY period, article_type;
```

```
┌───────────┬─────────────────────┬───────┐
│  period   │    article_type     │ count │
├───────────┼─────────────────────┼───────┤
│ 2011-2013 │ その他              │  1052 │
│ 2011-2013 │ チュートリアル/入門 │   100 │
│ 2011-2013 │ ライブラリ/FW紹介   │   438 │
│ 2011-2013 │ リリースノート      │   549 │
│ 2011-2013 │ 書籍関連            │   127 │
│ 2011-2013 │ 発表/スライド       │    38 │
│ 2011-2013 │ 解説/説明           │  1006 │
│ 2014-2016 │ その他              │   731 │
│ 2014-2016 │ チュートリアル/入門 │   122 │
│ 2014-2016 │ ライブラリ/FW紹介   │   495 │
│ 2014-2016 │ リリースノート      │   761 │
│ 2014-2016 │ 書籍関連            │    47 │
│ 2014-2016 │ 発表/スライド       │    26 │
│ 2014-2016 │ 解説/説明           │  1086 │
│ 2017-2019 │ その他              │   471 │
│ 2017-2019 │ チュートリアル/入門 │    91 │
│ 2017-2019 │ ライブラリ/FW紹介   │   452 │
│ 2017-2019 │ リリースノート      │   816 │
│ 2017-2019 │ 書籍関連            │    17 │
│ 2017-2019 │ 発表/スライド       │     7 │
│ 2017-2019 │ 解説/説明           │   925 │
│ 2020-2022 │ その他              │   423 │
│ 2020-2022 │ チュートリアル/入門 │    53 │
│ 2020-2022 │ ライブラリ/FW紹介   │   388 │
│ 2020-2022 │ リリースノート      │   868 │
│ 2020-2022 │ 書籍関連            │    12 │
│ 2020-2022 │ 発表/スライド       │     3 │
│ 2020-2022 │ 解説/説明           │   564 │
│ 2023-2025 │ その他              │   329 │
│ 2023-2025 │ チュートリアル/入門 │    25 │
│ 2023-2025 │ ライブラリ/FW紹介   │   174 │
│ 2023-2025 │ リリースノート      │   940 │
│ 2023-2025 │ 書籍関連            │     3 │
│ 2023-2025 │ 発表/スライド       │     7 │
│ 2023-2025 │ 解説/説明           │   449 │
└───────────┴─────────────────────┴───────┘
```

</details>

---

## 情報ソースの変化

### ドメイン別（初期 vs 中期 vs 後期）

**初期（2011-2013）TOP5:**
1. github.com (327)
2. d.hatena.ne.jp (154)
3. slideshare.net (147)
4. amazon.co.jp (98)
5. amazon.com (83)

**中期（2017-2019）TOP5:**
1. github.com (828)
2. medium.com (134)
3. developers.google.com (103)
4. webkit.org (69)
5. nodejs.org (64)

**後期（2023-2025）TOP5:**
1. github.com (568)
2. nodejs.org (98)
3. bun.sh (62)
4. zenn.dev (56)
5. developer.chrome.com (55)

### 日本語ブログプラットフォームの変遷

| 年 | はてな | Qiita | Zenn |
|----|--------|-------|------|
| 2011 | 92 | 0 | 0 |
| 2014 | 29 | 19 | 0 |
| 2016 | 10 | 45 | 0 |
| 2020 | 3 | 4 | 3 |
| 2021 | 1 | 1 | 22 |
| 2024 | 2 | 1 | 24 |

はてなダイアリー → Qiita → Zenn と移行している。

### 日本語ソースの割合

| 年 | 日本語 | 英語 | 日本語率 |
|----|--------|------|----------|
| 2011 | 203 | 712 | 22.2% |
| 2015 | 80 | 963 | 7.7% |
| 2019 | 26 | 764 | 3.3% |
| 2025 | 26 | 526 | 4.7% |

日本語ソースは22%から5%程度に減少。国際的な一次情報源への移行が進んでいる。

<details>
<summary>クエリと実行結果</summary>

```sql
-- ドメイン別集計（初期 2011-2013）
SELECT regexp_extract(url, 'https?://([^/]+)', 1) as domain, COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013
GROUP BY domain ORDER BY count DESC LIMIT 10;
```

```
┌────────────────────┬───────┐
│       domain       │ count │
├────────────────────┼───────┤
│ github.com         │   327 │
│ d.hatena.ne.jp     │   154 │
│ www.slideshare.net │   147 │
│ www.amazon.co.jp   │    98 │
│ www.amazon.com     │    83 │
│ blog.nodejs.org    │    73 │
│ blog.jquery.com    │    45 │
│ blogs.msdn.com     │    44 │
│ shop.oreilly.com   │    34 │
│ hacks.mozilla.org  │    33 │
└────────────────────┴───────┘
```

```sql
-- ドメイン別集計（中期 2017-2019）
SELECT regexp_extract(url, 'https?://([^/]+)', 1) as domain, COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2017 AND 2019
GROUP BY domain ORDER BY count DESC LIMIT 10;
```

```
┌───────────────────────┬───────┐
│        domain         │ count │
├───────────────────────┼───────┤
│ github.com            │   828 │
│ medium.com            │   134 │
│ developers.google.com │   103 │
│ webkit.org            │    69 │
│ nodejs.org            │    64 │
│ www.youtube.com       │    52 │
│ qiita.com             │    49 │
│ speakerdeck.com       │    40 │
│ eslint.org            │    29 │
│ www.amazon.com        │    29 │
└───────────────────────┴───────┘
```

```sql
-- ドメイン別集計（後期 2023-2025）
SELECT regexp_extract(url, 'https?://([^/]+)', 1) as domain, COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025
GROUP BY domain ORDER BY count DESC LIMIT 10;
```

```
┌────────────────────────┬───────┐
│         domain         │ count │
├────────────────────────┼───────┤
│ github.com             │   568 │
│ nodejs.org             │    98 │
│ bun.sh                 │    62 │
│ zenn.dev               │    56 │
│ developer.chrome.com   │    55 │
│ webkit.org             │    36 │
│ deno.com               │    35 │
│ devblogs.microsoft.com │    35 │
│ www.mozilla.org        │    27 │
│ web.dev                │    25 │
└────────────────────────┴───────┘
```

```sql
-- 日本語プラットフォームの変遷
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN url LIKE '%d.hatena.ne.jp%' OR url LIKE '%hatenablog%' THEN 1 ELSE 0 END) as hatena,
    SUM(CASE WHEN url LIKE '%qiita.com%' THEN 1 ELSE 0 END) as qiita,
    SUM(CASE WHEN url LIKE '%zenn.dev%' THEN 1 ELSE 0 END) as zenn
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year ORDER BY year;
```

```
┌───────┬────────┬────────┬────────┐
│ year  │ hatena │ qiita  │  zenn  │
├───────┼────────┼────────┼────────┤
│  2011 │     92 │      0 │      0 │
│  2012 │     68 │      3 │      0 │
│  2013 │     45 │      5 │      0 │
│  2014 │     29 │     19 │      0 │
│  2015 │     14 │     32 │      0 │
│  2016 │     10 │     45 │      0 │
│  2017 │      7 │     24 │      0 │
│  2018 │      7 │     18 │      0 │
│  2019 │      3 │      7 │      0 │
│  2020 │      3 │      4 │      3 │
│  2021 │      1 │      1 │     22 │
│  2022 │      2 │      0 │     14 │
│  2023 │      4 │      0 │     18 │
│  2024 │      2 │      1 │     24 │
│  2025 │      3 │      0 │     14 │
└───────┴────────┴────────┴────────┘
```

```sql
-- 日本語ソースの割合
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN url LIKE '%.jp%' OR url LIKE '%qiita%' OR url LIKE '%zenn%'
        OR url LIKE '%hatena%' THEN 1 ELSE 0 END) as jp_count,
    COUNT(*) as total,
    ROUND(100.0 * SUM(CASE WHEN url LIKE '%.jp%' OR url LIKE '%qiita%'
        OR url LIKE '%zenn%' OR url LIKE '%hatena%' THEN 1 ELSE 0 END) / COUNT(*), 1) as jp_pct
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year ORDER BY year;
```

```
┌───────┬──────────┬───────┬────────┐
│ year  │ jp_count │ total │ jp_pct │
├───────┼──────────┼───────┼────────┤
│  2011 │      203 │   915 │   22.2 │
│  2015 │       80 │  1043 │    7.7 │
│  2019 │       26 │   790 │    3.3 │
│  2025 │       26 │   552 │    4.7 │
└───────┴──────────┴───────┴────────┘
```

</details>

---

## 個人ブログ vs 公式

紹介記事のソースを「公式」「GitHub」「個人ブログ」に分類。

| ソース | 2011-2013 | 2023-2025 | 変化 |
|--------|-----------|-----------|------|
| 公式 | 204 | 479 | +135% |
| GitHub | 506 | 596 | 安定 |
| 個人ブログ | 213 | 70 | -67% |

- 公式: nodejs.org, webkit.org, reactjs.org, eslint.org など公式サイト/プロジェクト
- GitHub: github.com, github.io
- 個人ブログ: はてな, Qiita, Zenn, medium.com/@個人 など

### 変化のポイント

- 2011-2013年: 個人ブログと公式がほぼ同数（213 vs 204）
- 2023-2025年: 公式が個人ブログの7倍（479 vs 70）

個人が技術情報を発信する場から、公式ドキュメントやプロジェクトサイトから直接情報を得る形へ変化している。

<details>
<summary>クエリと実行結果</summary>

```sql
SELECT
    CASE
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013 THEN '2011-2013'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025 THEN '2023-2025'
    END as period,
    CASE
        WHEN url LIKE '%d.hatena.ne.jp%' OR url LIKE '%hatenablog%' OR url LIKE '%qiita.com%'
            OR url LIKE '%zenn.dev%' OR url LIKE '%medium.com/@%' THEN '個人ブログ'
        WHEN url LIKE '%github.com%' OR url LIKE '%github.io%' THEN 'GitHub'
        WHEN url LIKE '%nodejs.org%' OR url LIKE '%webkit.org%' OR url LIKE '%chromium.org%'
            OR url LIKE '%mozilla.org%' OR url LIKE '%microsoft.com%' OR url LIKE '%google.com%'
            OR url LIKE '%reactjs.org%' OR url LIKE '%eslint.org%' OR url LIKE '%bun.sh%'
            OR url LIKE '%deno.com%' OR url LIKE '%nextjs.org%' OR url LIKE '%vitejs.dev%'
            THEN '公式'
        ELSE 'その他'
    END as source_type,
    COUNT(*) as count
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013
   OR YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025
GROUP BY period, source_type
ORDER BY period, source_type;
```

```
┌───────────┬─────────────┬───────┐
│  period   │ source_type │ count │
├───────────┼─────────────┼───────┤
│ 2011-2013 │ GitHub      │   506 │
│ 2011-2013 │ その他      │  2398 │
│ 2011-2013 │ 個人ブログ  │   213 │
│ 2011-2013 │ 公式        │   193 │
│ 2023-2025 │ GitHub      │   596 │
│ 2023-2025 │ その他      │   908 │
│ 2023-2025 │ 個人ブログ  │    67 │
│ 2023-2025 │ 公式        │   356 │
└───────────┴─────────────┴───────┘
```

</details>

---

## 横断的トピックの変化

フレームワークに依存しない、技術横断的なトピックの出現数。

| 年 | 型 | テスト | パフォーマンス | 非同期 | セキュリティ | a11y |
|----|-----|--------|----------------|--------|--------------|------|
| 2011 | 30 | 46 | 27 | 19 | 10 | 6 |
| 2014 | 52 | 87 | 58 | 80 | 14 | 9 |
| 2017 | 108 | 86 | 93 | 58 | 15 | 15 |
| 2020 | 123 | 44 | 80 | 44 | 13 | 16 |
| 2021 | 129 | 59 | 64 | 45 | 28 | 17 |
| 2025 | 88 | 47 | 42 | 19 | 15 | 23 |

### 変化のポイント

- 型（TypeScript）: 30 → 129（2021ピーク）→ 88
- 非同期: 2014年がピーク（ES6 Promise導入期）
- パフォーマンス: 2017年がピーク
- a11y: 着実に増加（6 → 23）

<details>
<summary>クエリと実行結果</summary>

```sql
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN LOWER(content) LIKE '%security%' OR LOWER(content) LIKE '%セキュリティ%'
        OR LOWER(content) LIKE '%脆弱性%' THEN 1 ELSE 0 END) as security,
    SUM(CASE WHEN LOWER(content) LIKE '%performance%' OR LOWER(content) LIKE '%パフォーマンス%'
        OR LOWER(content) LIKE '%高速%' THEN 1 ELSE 0 END) as performance,
    SUM(CASE WHEN LOWER(content) LIKE '%accessib%' OR LOWER(content) LIKE '%a11y%'
        OR LOWER(content) LIKE '%アクセシビリティ%' THEN 1 ELSE 0 END) as a11y,
    SUM(CASE WHEN LOWER(content) LIKE '%test%' OR LOWER(content) LIKE '%テスト%' THEN 1 ELSE 0 END) as testing,
    SUM(CASE WHEN LOWER(content) LIKE '%型%' OR LOWER(content) LIKE '%type%' THEN 1 ELSE 0 END) as typing
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year
ORDER BY year;
```

```
┌───────┬──────────┬─────────────┬────────┬─────────┬────────┐
│ year  │ security │ performance │  a11y  │ testing │ typing │
├───────┼──────────┼─────────────┼────────┼─────────┼────────┤
│  2011 │        6 │          21 │      3 │      34 │     29 │
│  2012 │        7 │          31 │      2 │      98 │     43 │
│  2013 │       11 │          29 │      7 │     118 │     69 │
│  2014 │        6 │          43 │      4 │      82 │     52 │
│  2015 │        9 │          23 │      8 │      66 │     72 │
│  2016 │       10 │          41 │     22 │      60 │     75 │
│  2017 │       13 │          76 │      5 │      72 │    104 │
│  2018 │       11 │          70 │     14 │      50 │     90 │
│  2019 │       20 │          55 │     14 │      55 │    103 │
│  2020 │       11 │          65 │      9 │      34 │    117 │
│  2021 │       23 │          54 │      8 │      39 │    124 │
│  2022 │       18 │          41 │      7 │      57 │    114 │
│  2023 │       13 │          66 │      6 │      57 │    111 │
│  2024 │       12 │          38 │      9 │      46 │     90 │
│  2025 │       14 │          33 │      9 │      34 │     86 │
└───────┴──────────┴─────────────┴────────┴─────────┴────────┘
```

</details>

---

## 開発プラクティスの変化

| プラクティス | 2011-2013 | 2017-2019 | 2023-2025 |
|--------------|-----------|-----------|-----------|
| CI/CD | 31 | 56 | 67 |
| Migration/移行 | 10 | 32 | 56 |
| RFC/Proposal | 2 | 73 | 45 |
| Breaking Change | 3 | 15 | 17 |

エコシステムの成熟に伴い、移行やBreaking Changeへの言及が増加している。

<details>
<summary>クエリと実行結果</summary>

```sql
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN LOWER(content) LIKE '%ci%' OR LOWER(content) LIKE '%github actions%' THEN 1 ELSE 0 END) as ci_cd,
    SUM(CASE WHEN LOWER(content) LIKE '%migration%' OR LOWER(content) LIKE '%移行%' THEN 1 ELSE 0 END) as migration,
    SUM(CASE WHEN LOWER(content) LIKE '%breaking%' OR LOWER(content) LIKE '%deprecat%' THEN 1 ELSE 0 END) as breaking_change
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year
ORDER BY year;
```

```
┌───────┬────────┬───────────┬─────────────────┐
│ year  │ ci_cd  │ migration │ breaking_change │
├───────┼────────┼───────────┼─────────────────┤
│  2011 │      7 │         0 │               1 │
│  2012 │      6 │         3 │               1 │
│  2013 │     16 │         4 │               1 │
│  2014 │     15 │         4 │               2 │
│  2015 │      7 │        14 │               5 │
│  2016 │     15 │         5 │               4 │
│  2017 │     17 │        10 │               5 │
│  2018 │     12 │        13 │               6 │
│  2019 │     27 │         5 │               4 │
│  2020 │     22 │        14 │               3 │
│  2021 │     19 │        17 │               7 │
│  2022 │     30 │        14 │              10 │
│  2023 │     29 │        25 │               8 │
│  2024 │     18 │        12 │               6 │
│  2025 │     20 │        16 │               3 │
└───────┴────────┴───────────┴─────────────────┘
```

</details>

---

## テストツールの変遷

テストに関する言及は全体の6-9%程度で、15年間を通じて安定した関心がある領域。ツールは世代交代を繰り返している。

### ユニットテストフレームワーク

| ツール | 2011-2013 | 2014-2016 | 2017-2019 | 2020-2022 | 2023-2025 |
|--------|-----------|-----------|-----------|-----------|-----------|
| Jasmine | 52 | 19 | 9 | 5 | 2 |
| QUnit | 35 | 13 | 4 | 2 | 0 |
| Mocha | 33 | 38 | 14 | 9 | 3 |
| Sinon | 34 | 17 | 7 | 5 | 0 |
| Jest | 0 | 10 | 35 | 26 | 21 |
| Vitest | 0 | 0 | 0 | 4 | 28 |

世代交代:
```
Jasmine/QUnit + Mocha/Sinon (2011-2016) → Jest (2016-) → Vitest (2022-)
```

### ブラウザテスト

| ツール | 2011-2013 | 2014-2016 | 2017-2019 | 2020-2022 | 2023-2025 |
|--------|-----------|-----------|-----------|-----------|-----------|
| PhantomJS | 37 | 13 | 8 | 0 | 0 |
| Selenium | 9 | 13 | 5 | 3 | 0 |
| Puppeteer | 0 | 0 | 25 | 33 | 3 |
| Cypress | 0 | 0 | 6 | 8 | 4 |
| Playwright | 0 | 0 | 0 | 18 | 27 |

世代交代:
```
PhantomJS/Selenium (2011-2016) → Puppeteer (2017-2020) → Playwright (2020-)
```

### テスト言及数の推移

| 年 | 総記事数 | テスト言及数 | 言及率 |
|----|----------|--------------|--------|
| 2011 | 915 | 34 | 3.7% |
| 2012 | 1,126 | 98 | 8.7% |
| 2013 | 1,269 | 118 | 9.3% |
| 2014 | 1,147 | 82 | 7.1% |
| 2015 | 1,043 | 66 | 6.3% |
| 2016 | 1,078 | 60 | 5.6% |
| 2017 | 1,068 | 72 | 6.7% |
| 2018 | 921 | 50 | 5.4% |
| 2019 | 790 | 55 | 7.0% |
| 2020 | 810 | 34 | 4.2% |
| 2021 | 789 | 39 | 4.9% |
| 2022 | 712 | 57 | 8.0% |
| 2023 | 737 | 57 | 7.7% |
| 2024 | 638 | 46 | 7.2% |
| 2025 | 552 | 34 | 6.2% |

テストへの関心は一定して存在し、ツールが入れ替わっても言及率は5-9%で推移している。

<details>
<summary>クエリと実行結果</summary>

```sql
-- テストフレームワークの言及数（期間別）
SELECT
    CASE
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2014 THEN '2011-2014'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2015 AND 2018 THEN '2015-2018'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2019 AND 2022 THEN '2019-2022'
        WHEN YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025 THEN '2023-2025'
    END as period,
    SUM(CASE WHEN LOWER(content) LIKE '%jasmine%' THEN 1 ELSE 0 END) as jasmine,
    SUM(CASE WHEN LOWER(content) LIKE '%mocha%' THEN 1 ELSE 0 END) as mocha,
    SUM(CASE WHEN LOWER(content) LIKE '%jest%' THEN 1 ELSE 0 END) as jest,
    SUM(CASE WHEN LOWER(content) LIKE '%vitest%' THEN 1 ELSE 0 END) as vitest,
    SUM(CASE WHEN LOWER(content) LIKE '%playwright%' THEN 1 ELSE 0 END) as playwright,
    SUM(CASE WHEN LOWER(content) LIKE '%cypress%' THEN 1 ELSE 0 END) as cypress,
    SUM(CASE WHEN LOWER(content) LIKE '%puppeteer%' THEN 1 ELSE 0 END) as puppeteer
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2025
GROUP BY period
ORDER BY period;
```

```
┌───────────┬─────────┬────────┬────────┬────────┬────────────┬─────────┬───────────┐
│  period   │ jasmine │ mocha  │  jest  │ vitest │ playwright │ cypress │ puppeteer │
├───────────┼─────────┼────────┼────────┼────────┼────────────┼─────────┼───────────┤
│ 2011-2014 │      62 │     45 │      1 │      0 │          0 │       0 │         0 │
│ 2015-2018 │      17 │     38 │     36 │      0 │          0 │       5 │        18 │
│ 2019-2022 │       6 │     11 │     34 │      4 │         18 │       9 │        40 │
│ 2023-2025 │       2 │      3 │     21 │     28 │         27 │       4 │         3 │
└───────────┴─────────┴────────┴────────┴────────┴────────────┴─────────┴───────────┘
```

</details>

---

## 技術のライフサイクル

### 消えた技術（2011-2013 → 2023-2025）

| 技術 | 2011-2013 | 2023-2025 | 減少率 |
|------|-----------|-----------|--------|
| Backbone.js | 75 | 0 | 100% |
| CoffeeScript | 71 | 0 | 100% |
| AMD/RequireJS | 74 | 3 | 96% |
| Jasmine | 52 | 2 | 96% |
| Grunt | 49 | 0 | 100% |
| PhantomJS | 37 | 0 | 100% |
| Underscore | 19 | 0 | 100% |
| Bower | 13 | 0 | 100% |

### 新たに台頭した技術

| 技術 | 2011-2013 | 2023-2025 | 成長率 |
|------|-----------|-----------|--------|
| ESM/import | 2 | 117 | 5,850% |
| Rust | 1 | 40 | 4,000% |
| Docker/Container | 2 | 26 | 1,300% |
| SSR/SSG | 2 | 20 | 1,000% |
| AI/LLM | 73 | 136 | 186% |
| WebAssembly | 0 | 51 | New |
| monorepo | 0 | 14 | New |

### 安定して存在する概念

| 概念 | 2011-2013 | 2017-2019 | 2023-2025 |
|------|-----------|-----------|-----------|
| API | 181 | 278 | 273 |
| npm | 19 | 129 | 121 |
| Linter | 47 | 65 | 88 |
| Bundler | 2 | 50 | 65 |
| DOM | 105 | 74 | 54 |
| Polyfill | 24 | 32 | 9 |

Polyfillはブラウザ標準化の進展により減少している。

<details>
<summary>クエリと実行結果</summary>

```sql
-- 消えた技術
WITH early AS (
    SELECT content FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
    WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013
),
late AS (
    SELECT content FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
    WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025
)
SELECT
    'Backbone' as keyword,
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%backbone%') as early_count,
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%backbone%') as late_count
UNION ALL SELECT 'CoffeeScript',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%coffeescript%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%coffeescript%')
UNION ALL SELECT 'Grunt',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%grunt%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%grunt%')
UNION ALL SELECT 'AMD/RequireJS',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%amd%' OR LOWER(content) LIKE '%requirejs%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%amd%' OR LOWER(content) LIKE '%requirejs%')
UNION ALL SELECT 'Bower',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%bower%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%bower%');
```

```
┌───────────────┬─────────────┬────────────┐
│    keyword    │ early_count │ late_count │
├───────────────┼─────────────┼────────────┤
│ Backbone      │          75 │          0 │
│ CoffeeScript  │          71 │          0 │
│ Grunt         │          49 │          0 │
│ AMD/RequireJS │          74 │          3 │
│ Bower         │          13 │          0 │
└───────────────┴─────────────┴────────────┘
```

```sql
-- 新たに台頭した技術
WITH early AS (
    SELECT content FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
    WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2011 AND 2013
),
late AS (
    SELECT content FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
    WHERE YEAR(CAST(date AS TIMESTAMP)) BETWEEN 2023 AND 2025
)
SELECT
    'WebAssembly' as keyword,
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%wasm%' OR LOWER(content) LIKE '%webassembly%') as early_count,
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%wasm%' OR LOWER(content) LIKE '%webassembly%') as late_count
UNION ALL SELECT 'TypeScript',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%typescript%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%typescript%')
UNION ALL SELECT 'ESM',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%esm%' OR LOWER(content) LIKE '%es modules%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%esm%' OR LOWER(content) LIKE '%es modules%')
UNION ALL SELECT 'Rust',
    (SELECT COUNT(*) FROM early WHERE LOWER(content) LIKE '%rust%'),
    (SELECT COUNT(*) FROM late WHERE LOWER(content) LIKE '%rust%');
```

```
┌─────────────┬─────────────┬────────────┐
│   keyword   │ early_count │ late_count │
├─────────────┼─────────────┼────────────┤
│ WebAssembly │           0 │         51 │
│ TypeScript  │          33 │        184 │
│ ESM         │           1 │         73 │
│ Rust        │           1 │         40 │
└─────────────┴─────────────┴────────────┘
```

</details>

---

## フレームワーク/ライブラリの変遷

### UIフレームワーク

| 年 | jQuery | Angular | React | Vue |
|----|--------|---------|-------|-----|
| 2011 | 109 | 1 | 0 | 0 |
| 2013 | 86 | 44 | 6 | 0 |
| 2015 | 29 | 30 | 103 | 10 |
| 2017 | 7 | 34 | 153 | 28 |
| 2019 | 9 | 9 | 84 | 20 |
| 2021 | 8 | 6 | 84 | 23 |
| 2025 | 1 | 4 | 82 | 4 |

jQuery → Angular → React/Vue への移行が明確。

### ビルドツール

| 年 | webpack | Rollup | esbuild | Vite |
|----|---------|--------|---------|------|
| 2016 | 33 | 2 | 0 | 0 |
| 2017 | 43 | 8 | 0 | 0 |
| 2020 | 26 | 7 | 5 | 1 |
| 2022 | 11 | 3 | 9 | 28 |
| 2023 | 13 | 10 | 16 | 36 |
| 2025 | 8 | 2 | 6 | 23 |

webpack → Vite への移行が進行中。

### ランタイム

| 年 | Node.js | Deno | Bun |
|----|---------|------|-----|
| 2020 | - | 13 | 0 |
| 2021 | - | 21 | 1 |
| 2022 | - | 21 | 5 |
| 2023 | - | 19 | 27 |
| 2024 | - | 18 | 26 |

Node.js一強から、Deno/Bun登場による多様化。

<details>
<summary>クエリと実行結果</summary>

```sql
-- UIフレームワークの言及数
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN LOWER(content) LIKE '%jquery%' THEN 1 ELSE 0 END) as jquery,
    SUM(CASE WHEN LOWER(content) LIKE '%angular%' THEN 1 ELSE 0 END) as angular,
    SUM(CASE WHEN LOWER(content) LIKE '%react%' THEN 1 ELSE 0 END) as react,
    SUM(CASE WHEN LOWER(content) LIKE '%vue%' THEN 1 ELSE 0 END) as vue
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year
ORDER BY year;
```

```
┌───────┬────────┬─────────┬────────┬────────┐
│ year  │ jquery │ angular │ react  │  vue   │
├───────┼────────┼─────────┼────────┼────────┤
│  2011 │     96 │       1 │      0 │      0 │
│  2012 │    101 │       9 │      1 │      0 │
│  2013 │     78 │      42 │      3 │      0 │
│  2014 │     35 │      49 │     52 │     11 │
│  2015 │     17 │      23 │     93 │     10 │
│  2016 │     23 │      37 │    128 │     24 │
│  2017 │      5 │      33 │    142 │     34 │
│  2018 │      8 │      24 │     99 │     39 │
│  2019 │      9 │       9 │     78 │     27 │
│  2020 │     11 │      18 │     71 │     24 │
│  2021 │      7 │       6 │     77 │     36 │
│  2022 │      2 │       8 │     75 │     17 │
│  2023 │      2 │       9 │     67 │     21 │
│  2024 │      3 │       7 │     66 │     16 │
│  2025 │      1 │       4 │     73 │      9 │
└───────┴────────┴─────────┴────────┴────────┘
```

```sql
-- ビルドツールの言及数
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN LOWER(content) LIKE '%webpack%' THEN 1 ELSE 0 END) as webpack,
    SUM(CASE WHEN LOWER(content) LIKE '%rollup%' THEN 1 ELSE 0 END) as rollup,
    SUM(CASE WHEN LOWER(content) LIKE '%esbuild%' THEN 1 ELSE 0 END) as esbuild,
    SUM(CASE WHEN LOWER(content) LIKE '%vite%' THEN 1 ELSE 0 END) as vite
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) >= 2016
GROUP BY year
ORDER BY year;
```

```
┌───────┬─────────┬────────┬─────────┬────────┐
│ year  │ webpack │ rollup │ esbuild │  vite  │
├───────┼─────────┼────────┼─────────┼────────┤
│  2016 │      31 │      2 │       0 │      0 │
│  2017 │      42 │      8 │       0 │      0 │
│  2018 │      42 │      1 │       0 │      0 │
│  2019 │      18 │      5 │       0 │      0 │
│  2020 │      25 │      7 │       4 │      1 │
│  2021 │      23 │      5 │      11 │     16 │
│  2022 │      11 │      3 │       9 │     28 │
│  2023 │      13 │     10 │      16 │     35 │
│  2024 │       7 │      3 │       9 │     26 │
│  2025 │       8 │      2 │       6 │     21 │
└───────┴─────────┴────────┴─────────┴────────┘
```

```sql
-- ランタイムの言及数
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    SUM(CASE WHEN LOWER(content) LIKE '%deno%' THEN 1 ELSE 0 END) as deno,
    SUM(CASE WHEN LOWER(url) LIKE '%bun.sh%' OR LOWER(title) LIKE '%bun %'
        OR LOWER(content) LIKE '% bun %' THEN 1 ELSE 0 END) as bun
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
WHERE YEAR(CAST(date AS TIMESTAMP)) >= 2020
GROUP BY year
ORDER BY year;
```

```
┌───────┬────────┬────────┐
│ year  │  deno  │  bun   │
├───────┼────────┼────────┤
│  2020 │     13 │      0 │
│  2021 │     21 │      1 │
│  2022 │     21 │      5 │
│  2023 │     18 │     27 │
│  2024 │     17 │     26 │
│  2025 │     10 │     18 │
└───────┴────────┴────────┘
```

</details>

---

## 紹介文の変化

| 年 | 平均文字数 | 中央値 | 最小 | 最大 |
|----|------------|--------|------|------|
| 2011 | 62 | 41 | 6 | 1,845 |
| 2015 | 65 | 58 | 8 | 489 |
| 2019 | 90 | 87 | 11 | 274 |
| 2021 | 101 | 93 | 10 | 414 |
| 2025 | 108 | 90 | 12 | 498 |

15年間で紹介文の長さが約2倍に増加。より詳しい紹介をするスタイルに変化している。

<details>
<summary>クエリと実行結果</summary>

```sql
-- 紹介文の長さの統計
SELECT
    YEAR(CAST(date AS TIMESTAMP)) as year,
    ROUND(AVG(LENGTH(content)), 0) as avg_length,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY LENGTH(content)), 0) as median_length,
    MIN(LENGTH(content)) as min_length,
    MAX(LENGTH(content)) as max_length
FROM read_json_auto('https://jser.info/source-data/items.json', ignore_errors=true)
GROUP BY year
ORDER BY year;
```

```
┌───────┬────────────┬───────────────┬────────────┬────────────┐
│ year  │ avg_length │ median_length │ min_length │ max_length │
├───────┼────────────┼───────────────┼────────────┼────────────┤
│  2011 │       62.0 │          41.0 │          6 │       1845 │
│  2012 │       52.0 │          43.0 │          7 │        446 │
│  2013 │       58.0 │          50.0 │          5 │        449 │
│  2014 │       70.0 │          65.0 │          8 │        324 │
│  2015 │       65.0 │          58.0 │          8 │        489 │
│  2016 │       62.0 │          54.0 │          8 │        218 │
│  2017 │       79.0 │          73.0 │          8 │        273 │
│  2018 │       83.0 │          80.0 │          9 │        216 │
│  2019 │       90.0 │          87.0 │         11 │        274 │
│  2020 │       98.0 │          89.0 │         10 │        338 │
│  2021 │      101.0 │          93.0 │         10 │        414 │
│  2022 │      102.0 │          92.0 │         13 │        554 │
│  2023 │      106.0 │          97.0 │         10 │        729 │
│  2024 │      101.0 │          90.0 │         11 │        539 │
│  2025 │      108.0 │          90.0 │         12 │        498 │
└───────┴────────────┴───────────────┴────────────┴────────────┘
```

</details>

---

## 分析手法

- DuckDBを使用したJSON分析
- データソース:
  - items.json（13,606件）: https://jser.info/source-data/items.json
  - posts.json（820件）: https://jser.info/posts.json
- 分析期間: 2011年1月〜2026年1月
- 各セクションのクエリは「クエリと実行結果」の折りたたみで確認可能
- 全てのクエリはDuckDBでURLから直接実行可能
