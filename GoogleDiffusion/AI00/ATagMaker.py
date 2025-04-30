def extract_tags(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tags = []
    skip_words = {"characters", "general", "?", "artist name", "twitter username",
                  "copyright notice", "watermark", "meta", "commentary",
                  "english commentary", "character", "copyright", "artist", "original"}

    for line in lines:
        line = line.strip()
        if not line or line == "?":
            continue

        tag_candidate = ""
        if ' ' in line:
            parts = line.rsplit(' ', 1)
            tag_candidate = parts[0].strip()
        else:
            tag_candidate = line

        # フィルタ（小文字化して判定）
        if tag_candidate.lower() in skip_words:
            continue

        tags.append(tag_candidate)

    # 出力
    if tags:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(", ".join(tags))
        print(f"{len(tags)} 個のタグを出力しました: {output_file}")
    else:
        print("タグが抽出されませんでした。")


# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     tags = []
#     skip_words = {"Characters", "General", "?", "artist name", "twitter username",
#                   "copyright notice", "watermark", "Meta", "commentary",
#                   "english commentary", "Character", "Copyright", "Artist", "original"}

#     for line in lines:
#         line = line.strip()
#         if not line or line == "?":
#             continue
#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0].strip()
#             if tag.lower() in skip_words:  # 小文字化して判定
#                 continue
#             tags.append(tag)
#         else:
#             if line.lower() in skip_words:
#                 continue
#             tags.append(line)

#     # 出力
#     if tags:
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(", ".join(tags))
#         print(f"{len(tags)}個のタグを出力しました: {output_file}")
#     else:
#         print("抽出されたタグがありません。")

# # 実行
# extract_tags('C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/input.txt',
#              'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/output.txt')

# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     tags = []
#     skip_words = {"Characters", "General", "?", "artist name", "twitter username",
#                   "copyright notice", "watermark", "Meta", "commentary",
#                   "english commentary"}

#     for line in lines:
#         line = line.strip()
#         if not line:
#             continue

#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0].strip()
#             # tag が skip_words に含まれているかチェック
#             if tag in skip_words:
#                 continue
#             tags.append(tag)
#         else:
#             continue

#     # 結果を書き込み
#     if tags:
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(", ".join(tags))
#         print(f"書き込み完了: {output_file}")
#     else:
#         print("タグが抽出されませんでした。")

# # 実行
# extract_tags('C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/input.txt',
#              'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/output.txt')

# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     tags = []
#     skip_words = {"Characters", "General", "?", "artist_name", "twitter username",
#                   "copyright notice", "watermark", "Meta", "commentary",
#                   "english commentary"}

#     for line in lines:
#         line = line.strip()
#         if not line:
#             continue
#         if line in skip_words:
#             continue
#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0]
#             tags.append(tag)
#             #print(f"Extracted tag: {tag}")  # デバッグ用出力
#         else:
#             print(f"Skipped line (no space): {line}")  # デバッグ用

#     if tags:
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(", ".join(tags))
#         #print(f"Tags written to {output_file}")
#     else:
#         print("No tags extracted.")

# # 実行（ファイルパスを再確認）
# extract_tags('C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/input.txt',
#              'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/output.txt')

# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     tags = []
#     skip_words = {"Characters", "General", "?", "artist name",
# "twitter username", "copyright notice", "watermark","Meta","commentary",
#  "english commentary", }
#     for line in lines:
#         line = line.strip()
#         if not line or line in skip_words:
#             continue
#         # 数値が最後についてるので、末尾の数値部分を削除してタグ名のみに
#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0]
#             tags.append(tag)
#     # 結果をoutput.txtに書き込み
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write(", " + ", ".join(tags) + ",")

# extract_tags('C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/input.txt', 
#              'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/output.txt')
