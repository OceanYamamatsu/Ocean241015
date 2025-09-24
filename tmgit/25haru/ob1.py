

import pandas as pd

# Excelファイルのパス
file_path = r"C:\Users\hekat\Downloads\二子玉川店2025年7月前半シフト-1.xlsx"

# 自分の名前を設定
my_name = "福地　雄介"  # ←ここを自分の名前に変更

# ファイル読み込み（ヘッダーなし）
df = pd.read_excel(file_path, header=None)

# 日付と時間帯の取得
dates = df.iloc[4, 2:]   # 行5（index=4）、列C以降
times = df.iloc[21, 2:]  # 行22（index=21）、列C以降

# 名前リスト（B列、23行目以降）
names = df.iloc[22:, 1]
my_row_index = names[names == my_name].index[0]

# 自分のシフト（○など）
shift_data = df.iloc[my_row_index, 2:]

# シフト抽出
my_shifts = []
for i, mark in shift_data.items():
    if pd.notna(mark) and str(mark).strip() != "":
        date = dates[i]
        time = times[i]
        my_shifts.append({"日付": date, "シフト時間": time})

# DataFrameに変換
result_df = pd.DataFrame(my_shifts)

# 出力ファイルパスを指定して保存
save_path = r"C:\Users\hekat\Downloads\my_shift.xlsx"
result_df.to_excel(save_path, index=False)

# 成功メッセージ
print(f"シフト一覧を保存しました: {save_path}")