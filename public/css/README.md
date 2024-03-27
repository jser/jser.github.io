# sass

## 要素

* **core**
    * 全体的に影響を与えるもの
    * ベースの色
    * ノーマライズ
* **component**
    * header,content,sidebar,footer等のコンポーネント
* **layout**
    * カラム等のレイアウト
    * component間のborderや空間
* **vendor**
    * sassライブラリ
    
## 空間の制御

* componentはそのcomponentの内部を管理する
* componentは基本的にpaddingを変更する
* marginについてはlayoutで考える
* component同士の境界(border)もlayoutが扱う

## 構造

```
content-wrapper 
    |- page-content
        |- post-content
       
```