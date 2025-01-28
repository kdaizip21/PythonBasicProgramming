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
    "00.並列化とは.md",
    "01.バウンド別のメリデリ.md",
    "02.並列化の効果.md",
    "03.データフレーム加工の例.md",
    "01.マルチスレッド.md",
    "01.threadingの使い方.md",
    "02.スレッドへの引数の渡し方.md",
    "03.デーモンスレッド.md",
    "04.同じ処理のスレッドを同時に複数立ち上げる.md",
    "05.Timer.md",
    "06.スレッドのロック.md",
    "07.セマフォ.md",
    "08.キュー.md",
    "09.イベント.md",
    "10.コンディション.md",
    "02.マルチプロセス.md",
    "01.multiprocessingの使い方.md",
    "02.Poolで非同期処理.md",
    "03.同期処理.md",
    "04.map.md",
    "05.プロセス間通信.md",
    "01.Pipe.md",
    "02.ValueとArray.md",
    "03.Manager.md",
    "03.concurrent.futures.md"
]

# 現在のフォルダに出力
current_dir = os.getcwd()
create_empty_md_files(file_names, current_dir)
