#!/usr/bin/env python3
# extract_lsb.py
# PNG (RGBA) の各チャンネルの LSB からバイト列を復元して表示する（picoCTF や { } を探索）

from PIL import Image
import sys, re

IMG = "red.png"

def bits_to_text(bits):
    # 8bit ごとに区切って文字に変換。末尾が8の倍数でない場合は切り捨て。
    n = (len(bits)//8) * 8
    chars = []
    for i in range(0, n, 8):
        byte = bits[i:i+8]
        val = int(byte, 2)
        if 32 <= val <= 126:  # printable
            chars.append(chr(val))
        else:
            chars.append(chr(val))  # 非表示もそのまま入れてみる
    return "".join(chars)

def find_flags(text):
    patterns = [r"picoCTF\{.*?\}", r"CTF\{.*?\}", r"\{.*?\}"]
    found = []
    for p in patterns:
        for m in re.finditer(p, text):
            found.append((p, m.group(0)))
    return found

def extract_from_channels(pixels, channel_idxs):
    bits = []
    for px in pixels:
        for idx in channel_idxs:
            v = px[idx]
            bits.append(str(v & 1))
    return "".join(bits)

def main():
    img = Image.open(IMG)
    pixels = list(img.getdata())  # each pixel is (R,G,B,A)
    print(f"Image: {IMG}, size={img.size}, mode={img.mode}")
    # チャンネル組合せを試す（R,G,B,A の単独、RGB、RGBA、R then G then B etc.）
    combos = {
        "R": [0], "G":[1], "B":[2], "A":[3],
        "RG":[0,1], "RB":[0,2], "GB":[1,2],
        "RGB":[0,1,2], "RGBA":[0,1,2,3],
        # 単一ピクセルごとにR,G,B,Aの順で取る (same as RGBA)、含めておく
    }

    for name, idxs in combos.items():
        bits = extract_from_channels(pixels, idxs)
        txt = bits_to_text(bits)
        # 見やすくするため先頭500文字だけ表示（必要なら増やす）
        head = txt[:500]
        found = find_flags(txt)
        print("="*60)
        print(f"Channels: {name} (indexes {idxs})")
        if found:
            print("== FLAG PATTERN(s) FOUND ==")
            for p, m in found:
                print(f"{p} => {m}")
        else:
            print("(no obvious flag pattern found)")
        print("Leading output (printable chars shown):")
        # 可視化：印刷可能文字だけを抜き出して表示
        printable = "".join(c if 32 <= ord(c) <= 126 else "." for c in head)
        print(printable)
        print()

    # 追加の解析：ビットを逆順で読む場合 (LSB をほかの順序で読む等)
    # 例として、各チャンネルの LSB を取ってから、8-bitブロックを逆順にしてみる
    bits_rgba = extract_from_channels(pixels, [0,1,2,3])
    reversed_bytes = "".join(chr(int(bits_rgba[i:i+8][::-1],2)) for i in range(0, (len(bits_rgba)//8)*8, 8))
    print("="*60)
    print("Additional try: RGBA bits with each byte bit-order reversed (for endian/bit-order issues)")
    preview = "".join(c if 32 <= ord(c) <= 126 else "." for c in reversed_bytes[:500])
    print(preview)
    found = find_flags(reversed_bytes)
    if found:
        for p,m in found:
            print("FOUND:", m)
    print("="*60)

if __name__ == "__main__":
    main()
                    