import os

# スクリプトと同じ場所にファイルを作成/読み込み
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "input.txt")
output_path = os.path.join(script_dir, "output.txt")

# input.txt がなければサンプルを書き込んで終了
if not os.path.exists(input_path):
    sample_data = """midriff 315k
?
nail polish 255k
?
navel 1.2M
?
piercing 118k
?
pink collar 2.9k
?
pink sleeves 4.7k
?
purple nails 27k
?
red wings 8.4k"""
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(sample_data)
    print("input.txt を作成しました！内容を確認して再実行してください。")
    exit()

# ファイル読み込み
with open(input_path, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

tags = []

# 各行を処理してタグ抽出
for line in raw_lines:
    line = line.strip()
    if not line or line == "?":
        continue  # 空行や「?」はスキップ
    parts = line.split()
    if len(parts) >= 2:
        tag = ' '.join(parts[:-1])  # 最後の数値以外をタグとして保持
        tags.append(tag)

# 出力用文字列（前後にカンマ）
output = ', ' + ', '.join(tags) + ','

# 書き出し
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output)

print("✅ 完了しました！ → output.txt に保存されました。")
