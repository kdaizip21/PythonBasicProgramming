# RDBを利用したAPI設計例（同期処理）
- FastAPIは非同期処理に対応しているが、ここでは同期処理を解説する。
- SQLAlchemyを利用した例


## ファイル構造
```tree
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```