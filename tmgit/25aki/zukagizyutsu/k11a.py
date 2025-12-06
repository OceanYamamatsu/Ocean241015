# おやつの値段リスト（例）
snacks = [120, 170, 40, 200, 350, 80]

# 初期の所持金
limit = 500

# ★ ① おやつを降順（高い順）にソート
snacks_sorted = sorted(snacks, reverse=True)

bag = []  # 持ち物

# ★ ② 上から順に、買えるものを入れていく
ct=0
for price in snacks_sorted:
    ct+=1
    if price <= limit:
        bag.append(price)
        limit -= price  # 残りの金額を減らす

# 結果表示
print("合計",sum(bag))
print("持ち物:", bag)
print("残りの金額:", limit)
print("計算回数",ct)
