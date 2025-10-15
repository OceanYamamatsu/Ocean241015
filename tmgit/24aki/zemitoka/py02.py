import math
# 1001 7
p = 7
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 7  # 公開鍵の指数
# gcd（最大公約数）を求める
g = math.gcd(e, phi)

print(f"gcd(e, φ(n)) = {g}")

# 判定
if g == 1:
    print("e と φ(n) は互いに素です。")
else:
    print("e と φ(n) は互いに素ではありません。")
