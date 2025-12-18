
def caesar_cipher(text, shift):
    result = ""
    for c in text:
        # 小文字
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        # 大文字
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        # 記号・数字・空白など
        else:
            result += c
    return result



# n = 'oisfuhwierwuhgruwgiuhwiughbwuf'
n='<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->'

for i in range(26):
    print(f"shift {i:2d}: {caesar_cipher(n, i)}")



