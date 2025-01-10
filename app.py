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
    "01.クラスの定義.md",
    "02.クラスの初期化とクラス変数.md",
    "03.コンストラクタとデストラクタ.md",
    "04.クラスの継承.md",
    "05.メッソドのオーバーライドとsuperによる親のメソッドの呼び出し.md",
    "06.プロパティとセッターとゲッター.md",
    "07.ダックタイピング.md",
    "08.抽象クラス.md",
    "09.多重継承.md",
    "10.クラス変数.md",
    "11.クラスメソッド.md",
    "12.スタティックメソッド.md"
]

# 現在のフォルダに出力
current_dir = os.getcwd()
create_empty_md_files(file_names, current_dir)