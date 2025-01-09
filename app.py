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
    "03.for文とbreak文とcontinue文.md",
    "01.InとNotの使い所.md",
    "02.値が入ってないかを判定するテクニック.md",
    "04.for range文での_(アンダースコア).md",
    "05.enumerate関数.md",
    "06.zip関数.md",
    "07.辞書をforループする.md",
    "08.関数のキーワード引数とデフォルト引数.md",
    "09.位置引数のタプル化 ～＊argsって何？～.md",
    "10.キーワード引数の辞書化 ～＊＊kwargsって何？～.md",
    "11.Docstrings～関数の説明書～.md",
    "12.クロージャー.md",
    "13.デコレータ.md",
    "14.Lambda ラムダ式.md",
    "15.ジェネレータ.md",
    "16.内包表記.md",
    "17.名前空間～__name__～とか.md"
]

# 現在のフォルダに出力
current_dir = os.getcwd()
create_empty_md_files(file_names, current_dir)
