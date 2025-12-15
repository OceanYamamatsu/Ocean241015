from urllib.parse import urlparse, parse_qs, unquote_plus

def decode_icon_array_from_url(url: str):
    qs = parse_qs(urlparse(url).query)
    encoded = qs.get("iconArray", [None])[0]
    if not encoded:
        raise ValueError("iconArray が URL にありません")
    
    decoded = unquote_plus(encoded)

    # 配列本体 "[ ... ]" を抽出
    start = decoded.find('[')
    end = decoded.rfind(']')
    content = decoded[start+1:end]

    # ------- 手作りパーサー（壊れた JSON に強い） -------
    items = []
    i = 0
    n = len(content)

    while i < n:
        c = content[i]

        # カンマ・空白をスキップ
        if c in ' \n\t,':
            i += 1
            continue

        # ---- ① 文字列の解析 ----
        if c == '"':
            i += 1
            s = []
            while i < n:
                if content[i] == '\\':   # エスケープ対応
                    if i + 1 < n:
                        s.append(content[i+1])
                        i += 2
                    else:
                        i += 1
                elif content[i] == '"':   # 文字列終端
                    i += 1
                    break
                else:
                    s.append(content[i])
                    i += 1
            items.append(''.join(s))
            continue

        # ---- ② 数字 or 生のトークン ----
        j = i
        while j < n and content[j] not in ', ':
            j += 1

        token = content[i:j].strip()

        # 数値判定
        try:
            if '.' in token:
                items.append(float(token))
            else:
                items.append(int(token))
        except:
            # 数値でなければ文字列として扱う
            items.append(token.strip('"'))

        i = j

    return items


# -------------------------
# 使い方
# -------------------------
# url = "<<<ここにあなたのURL>>>"
#url = "https://korobolitepp.web.app/korobo_B.html?iconArray=%5B%22icon_start%22%2C%22icon_const_num%22%2C1%2C%22icon_block_for_start%22%2C%22icon_const_num%22%2C2%2C%22icon_var_num_input%22%2C4%2C%22icon_var_num_output%22%2C4%2C%22icon_operation_equal%22%2C2%2C%22icon_const_num%22%2C2%2C%22icon_block_while_start%22%2C%22icon_set_masterSpeed_korobo%22%2C2%2C%22icon_forward_korobo%22%2C%22icon_eye_L_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_var_num_output%22%2C4%2C%22icon_operation_num%22%2C2%2C%22icon_const_num%22%2C-1%2C%22icon_var_num_input%22%2C4%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_invert_bool%22%2C%22icon_block_while_start%22%2C%22icon_forward_right_korobo%22%2C%22icon_block_while_end%22%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_block_while_start%22%2C%22icon_forward_left_korobo%22%2C%22icon_block_while_end%22%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_while_end%22%2C%22icon_block_infinit_start%22%2C%22icon_motor_brake_korobo%22%2C%22icon_block_infinit_end%22%2C%22icon_const_num%22%2C1%2C%22icon_block_for_start%22%2C%22icon_forward_korobo%22%2C%22icon_wait%22%2C1%2C%22icon_forward_right_korobo%22%2C%22icon_wait%22%2C0.5%2C%22icon_block_for_end%22%2C%22icon_const_num%22%2C0%2C%22icon_var_num_input%22%2C3%2C%22icon_var_num_output%22%2C3%2C%22icon_operation_equal%22%2C0%2C%22icon_const_num%22%2C4%2C%22icon_block_while_start%22%2C%22icon_forward_korobo%22%2C%22icon_eye_L_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_var_num_output%22%2C3%2C%22icon_operation_num%22%2C0%2C%22icon_const_num%22%2C1%2C%22icon_var_num_input%22%2C3%2C%22icon_wait%22%2C0.6%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_while_end%22%2C%22icon_block_for_end%22%2C%22icon_end%22%5D&title=DXG"
url = "https://korobolitepp.web.app/korobo_B.html?iconArray=%5B%22icon_start%22%2C%22icon_const_num%22%2C1%2C%22icon_block_for_start%22%2C%22icon_const_num%22%2C2%2C%22icon_var_num_input%22%2C4%2C%22icon_var_num_output%22%2C4%2C%22icon_operation_equal%22%2C2%2C%22icon_const_num%22%2C2%2C%22icon_block_while_start%22%2C%22icon_set_masterSpeed_korobo%22%2C2%2C%22icon_forward_korobo%22%2C%22icon_eye_L_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_var_num_output%22%2C4%2C%22icon_operation_num%22%2C2%2C%22icon_const_num%22%2C-1%2C%22icon_var_num_input%22%2C4%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_invert_bool%22%2C%22icon_block_while_start%22%2C%22icon_forward_right_korobo%22%2C%22icon_block_while_end%22%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_eye_R_korobo%22%2C%22icon_block_while_start%22%2C%22icon_forward_left_korobo%22%2C%22icon_block_while_end%22%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_while_end%22%2C%22icon_block_infinit_start%22%2C%22icon_motor_brake_korobo%22%2C%22icon_block_infinit_end%22%2C%22icon_const_num%22%2C1%2C%22icon_block_for_start%22%2C%22icon_forward_korobo%22%2C%22icon_wait%22%2C1%2C%22icon_forward_right_korobo%22%2C%22icon_wait%22%2C0.5%2C%22icon_block_for_end%22%2C%22icon_const_num%22%2C0%2C%22icon_var_num_input%22%2C3%2C%22icon_var_num_output%22%2C3%2C%22icon_operation_equal%22%2C0%2C%22icon_const_num%22%2C4%2C%22icon_block_while_start%22%2C%22icon_forward_korobo%22%2C%22icon_eye_L_korobo%22%2C%22icon_block_if_start%22%2C%22icon_block_upper_start%22%2C%22icon_block_upper_end%22%2C%22icon_block_lower_start%22%2C%22icon_var_num_output%22%2C3%2C%22icon_operation_num%22%2C0%2C%22icon_const_num%22%2C1%2C%22icon_var_num_input%22%2C3%2C%22icon_wait%22%2C0.6%2C%22icon_block_lower_end%22%2C%22icon_block_if_end%22%2C%22icon_block_while_end%22%2C%22icon_block_for_end%22%2C%22icon_end%22%5D&title=DXG"
result = decode_icon_array_from_url(url)

print("要素数:", len(result))
for i, v in enumerate(result):
    print(i, ":", v)
# ?