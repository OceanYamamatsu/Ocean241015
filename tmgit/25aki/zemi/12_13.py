# 011001010110111101110111

text = """
にゃ にゃー にゃー にゃ にゃー にゃー にゃ にゃー
にゃ にゃー にゃー にゃ にゃ にゃー にゃ にゃー
にゃ にゃー にゃー にゃ にゃー にゃー にゃー にゃー
にゃ にゃー にゃー にゃー にゃ にゃー にゃー にゃー
"""

# 改行や余計なスペースを除去
words = text.strip().split()

# 「にゃ」= 0, 「にゃー」= 1 に変換
binary = ""
for w in words:
    if w == "にゃ":
        binary += "0"
    elif w == "にゃー":
        binary += "1"
    else:
        print(f"未知の単語あり: {w}")

print("[Binary]")
print(binary)

# 8bitに揃える
if len(binary) % 8 != 0:
    print("Warning: バイナリ長が8bitの倍数ではありません")
    # 必要なら padding もできるがここでは警告だけ

# 8bitずつASCIIデコード
decoded = ""
for i in range(0, len(binary), 8):
    byte = binary[i:i+8]
    print(byte)
    if len(byte) < 8:
        break
    decoded += chr(int(byte, 2))

print("\n[Decoded text]")
print(decoded)



print(len('011001010110111101110111'))