# 入力ファイルを読み込む
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read()

# 「?」で分割してタグを抽出
tags = []
for item in data.strip().split('?'):
    if item:  # 空でない場合
        parts = item.strip().split()
        tag = ' '.join(parts[:-1])  # 数値を除いた部分をタグとする
        tags.append(tag)

# カンマ区切り + 前後にもカンマ追加
output = ', ' + ', '.join(tags) + ','

# 結果をファイルに書き出す
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("処理完了！ → output.txt に保存されました")
