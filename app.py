import os

def create_empty_md_files(file_names: list[str], output_dir: str) -> None:
    """
    指定された名前の空のMarkdownファイルを出力先フォルダに作成します。

    Args:
        file_names (list[str]): 作成するファイル名のリスト。
        output_dir (str): ファイルを作成する出力先フォルダ。
    """
    os.makedirs(output_dir, exist_ok=True)

    for file_name in file_names:
        with open(os.path.join(output_dir, file_name), 'w') as f:
            pass

# ファイル名のリスト
file_names = [
    "01.First Steps.md",
    "02.PathParameters.md",
    "03.QueryParameters.md",
    "04.RequestBody.md",
    "05.QueryParametersの追加オプション.md",
    "06.PathParametersの追加オプション.md",
    "07.複数のRequestBody_ネストしたJSON_を受け付ける.md",
    "08.RequestBodyの追加オプション.md",
    "09.様々なRequestBody.md",
    "10.ResponceModel.md",
    "11.同期SQL_リレーショナル.md",
    "01.SQLAlchemyパーツを作成する.md",
    "02.データベースモデルを作成する.md",
    "03.Pydanticモデルを作成する.md",
    "04.CRUD処理を作成する.md",
    "05.FastAPIアプリ.md",
    "12.非同期SQL_リレーショナル.md",
    "01.FastAPIサーバ立ち上げ処理.md",
    "02.データベースとの接続情報.md",
    "03.データベーステーブル情報.md",
    "04.APIレスポンス作成_Json部.md",
    "05.APIレスポンス作成_html部.md",
    "06.ルーター.md",
    "01.datavolume.md",
    "02.link.md",
    "03.node.md",
    "13.同期NoSQL_DynamoDB.md",
    "01.FastAPIサーバ立ち上げ処理.md",
    "02.APIレスポンス作成_Json部.md",
    "03.DynamoDBアクセス_APIルータ.md",
    "14.非同期NoSQL_DynamoDB.md",
    "01.FastAPIサーバ立ち上げ処理.md",
    "02.APIレスポンス作成_Json部.md",
    "03.DynamoDBアクセス_APIルータ.md",
    "15.mangum-cliとSAMを利用したデプロイ.md",
    "16.Gunicornサーバでの起動（Docker）.md",
    "xx.CORSの設定.md"
]

# 現在のフォルダに出力
current_dir = os.getcwd()
create_empty_md_files(file_names, current_dir)
