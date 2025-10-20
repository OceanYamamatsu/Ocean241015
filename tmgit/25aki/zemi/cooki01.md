import urllib.parse
import base64

# Cookieの値
cookie_value = "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ%3D%3D"

# ① URLデコード
url_decoded = urllib.parse.unquote(cookie_value)

# ② Base64デコード
decoded_bytes = base64.b64decode(url_decoded)

# ③ バイト列を文字列に変換
decoded_text = decoded_bytes.decode('utf-8')

print(decoded_text)
