# shift_extract.py
import pandas as pd
from datetime import datetime, timedelta

# ①--- 設定 -------------------------------------------------------------
XLSX_FILE = "二子玉川店2025年7月前半シフト-1.xlsx"   # ←アップロード済みファイル名
PERSON    = "福地　雄介"                               # ←抽出したい人の氏名
# -----------------------------------------------------------------------

def _time_map(df):
    """「時間帯」が書かれている行と列座標 → 'HH:MM' の対応表を作る"""
    for r in range(len(df)):
        if df.iloc[r].astype(str).str.contains('時間帯').any():
            idx = r
            break
    else:
        return {}
    return {c: str(df.iat[idx, c]).strip()
            for c in df.columns
            if isinstance(df.iat[idx, c], str) and ':' in str(df.iat[idx, c])}

def _extract_one_day(df, person, ignore={'休憩', '指定'}):
    """1枚のシート（＝1日）から (開始, 終了, 担当) を抽出"""
    tmap = _time_map(df)
    if not tmap:
        return []

    # 氏名が入っている行（役割行）とその直下（休憩行）
    role_row = df.index[df[1] == person]
    if role_row.empty:
        return []
    role_row = role_row[0]
    brk_row  = role_row + 1 if role_row + 1 < len(df) else None

    shifts, current, start_col = [], None, None
    cols = sorted(tmap)

    for i, col in enumerate(cols):
        role_val  = str(df.iat[role_row, col]).strip() if pd.notna(df.iat[role_row, col]) else ''
        break_val = ''
        if brk_row is not None and pd.notna(df.iat[brk_row, col]):
            break_val = str(df.iat[brk_row, col]).strip()

        # 休憩セルにぶつかったら現在の勤務を終了
        if break_val in ignore:
            if current:
                end = datetime.strptime(tmap[cols[i-1]], '%H:%M') + timedelta(minutes=30)
                shifts.append((start_time, end.strftime('%H:%M'), current))
                current = start_col = None
            continue

        # 新しい担当が書かれているセル
        if role_val:
            if current:          # 直前の勤務をクローズ
                end = datetime.strptime(tmap[cols[i-1]], '%H:%M') + timedelta(minutes=30)
                shifts.append((start_time, end.strftime('%H:%M'), current))
            current    = role_val
            start_col  = col
            start_time = tmap[col]

    # 行末まで担当が続く場合
    if current:
        end = datetime.strptime(tmap[cols[-1]], '%H:%M') + timedelta(minutes=30)
        shifts.append((start_time, end.strftime('%H:%M'), current))

    return shifts

def collect_schedule(xlsx_path, person):
    """ブック内すべてのシートを回って (日付, 開始, 終了, 担当) をまとめる"""
    xl = pd.ExcelFile(xlsx_path)
    records = []
    for sheet in xl.sheet_names:            # シート名 = yyyymmdd 形式
        df = pd.read_excel(xlsx_path, sheet_name=sheet, header=None)
        date = datetime.strptime(sheet, '%Y%m%d').strftime('%Y-%m-%d')
        for start, end, role in _extract_one_day(df, person):
            records.append((date, start, end, role))
    return sorted(records)

if __name__ == "__main__":
    data = collect_schedule(XLSX_FILE, PERSON)
    out  = pd.DataFrame(data, columns=["日付", "開始", "終了", "担当"])
    print(out.to_string(index=False))
