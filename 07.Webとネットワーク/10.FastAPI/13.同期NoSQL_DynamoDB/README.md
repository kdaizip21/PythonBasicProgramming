# DynamoDBを利用したAPI設計例（非同期処理）

- AWSリソースを非同期で扱うためには [Async AWS SDK for Python](https://aioboto3.readthedocs.io/en/latest/readme.html)(aioboto3) を利用する
- これはboto3と非同期boto3であるaiobotocoreのラッパーで、AWSリソースを非同期で扱いやすくされたライブラリ
- ただし、AWS公式ではないサーボパーティ製ライブラリのため、利用の際は動作確認等を行うことを勧める。


## aioboto3 のサポート状況（2020/10/06時点）
| **Services**              | **Status**         |
| :------------------------ | :----------------- |
| DynamoDB Service Resource | Tested and working |
| DynamoDB Table            | Tested and working |
| S3                        | Working            |
| Kinesis                   | Working            |
| SSM Parameter Store       | Working            |
| Athena                    | Working            |

- インストール方法
```sh
$ pip install aioboto3
```

- FastAPIでの実装は、同期処理（boto3）と基本的に変わらないが、AWSリソース呼び出し部分だけが異なる


```txt.
│  asgi.py             :FastAPIサーバ立ち上げ処理
│  schemas.py          :APIレスポンス作成（Json部）
└  router.py           :DynamoDBアクセス、APIルータ
```

$lsx()
