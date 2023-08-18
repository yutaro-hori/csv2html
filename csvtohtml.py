import pandas as pd
import os

# 現在のディレクトリのCSVファイルをリストアップ
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# CSVファイルを結合
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# 'files'列が存在する場合、それを削除
if 'files' in combined_df.columns:
    combined_df = combined_df.drop('files', axis=1)

# 各セルの内容に対して\nを実際の改行に置換
combined_df = combined_df.applymap(lambda x: str(x).replace("\n", "<br>") if isinstance(x, str) else x)

# 結合されたデータをHTMLファイルに保存
combined_df.to_html("combined.html", encoding="utf-8", index=False, border=1, escape=False)

print("CSVの結合とHTMLへの変換が完了しました。")
