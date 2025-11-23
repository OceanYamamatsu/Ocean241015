def hantei(A,E,R):
    total = E + R
    # 出席回数12回未満
    if A < 12:
        if (A == 10 or A == 11) and total >= 80:
            return "合格"
        else:
            return "不合格"
    # 出席回数12回以上
    else:
        if total >= 60:
            return "合格"
        elif max(E,R) >= 45:
            return "合格"
        else:
            return "不合格"
#数値入力
students = [
    ("2001", 12, 25, 40),
    ("2002",  9, 50, 50),
    ("2003", 15,  0, 40),
    ("2004", 13, 25, 25),
    ("2005", 14, 45, 10),
    ("2006", 10, 50, 20),
    ("2007", 11, 40, 40)
]
for name,A,E,R in students:
    result = hantei(A,E,R)
    print(f"{name}：出席{A}回 試験{E}点 レポート{R}点 → {result}")
