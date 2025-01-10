# RDBを利用したAPI設計例（非同期処理）  
- [BformatAPI](https://dev-growi.aw-connected.com/Status/API/MapData/Download)をFastAPIで非同期処理で実装した例


## ファイル構造
```
.
│  asgi.py             :FastAPIサーバ立ち上げ処理
│  database.py         :データベースとの接続情報
│  models.py           :データベーステーブル情報
│  response_html.py    :APIレスポンス作成（html部）
│  schemas.py          :APIレスポンス作成（Json部）
│  __init__.py
└─router
   │  datavolume.py    :data_volumeテーブルに対するCRUD処理
   │  link.py          :linkテーブルに対するCRUD処理
   └─ node.py          :nodeテーブルに対するCRUD処理
```