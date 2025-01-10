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
    "01.ファイル操作.md",
    "02.withステートメントでのopen.md",
    "03.ファイルの読み込み.md",
    "04.seekで移動する.md",
    "05.書き込み読み込みモード.md",
    "06.テンプレート.md",
    "07.ファイル操作.md",
    "08.subprocessでコマンド実行.md",
    "09.datetime.md"
]

# 現在のフォルダに出力
current_dir = os.getcwd()
create_empty_md_files(file_names, current_dir)
