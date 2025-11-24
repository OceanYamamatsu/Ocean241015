import os
def extract_tags(input_file,output_file,entry_file):
    with open(input_file,'r',encoding='utf-8') as f:
        lines = f.readlines()
    tags = []
    skip_words = {
        "pubic hair","female pubic hair",
        "Character","Characters","General","original","?"," Meta","Artist","name tag",
        "artist name","circle name","character name","copyright name",
        "twitter username","fanbox_username","subscribestar username","pixiv username","facebook username",
        "logo","artist logo","pixiv logo","patreon logo","twitter x logo","bluesky logo","fanbox logo",
        "bad id","bad pixiv id","pixiv id","copyright notice","watermark","commentary",
        "character censor","novelty censor","heart censor","bar censor","censored",
        "english commentary","Copyright","english text","korean text","speech bubble",
        "mosaic censoring","pointless censoring","convenient censoring","signature",
        "mixed-language commentary","adversarial noise","watermark grid",
        "korean commentary","paid reward available","copyright request","translated",
        "variant set","large variant set","commission","pixiv commission","character request",
        "source request","third-party edit","cover","cover page","web_address",
        "hashtag-only commentary","web address"," chinese commentary"," dated",
        'second-party source',"odaibako","request inset",
        "request","commentary request","translation","translation request",
        "instagram logo","instagram username", 

        "bleeding","injury,","blood","bruise",
    }
    for line in lines:
        print(line)
        line = line.strip()
        if not line:
            continue
        if ' ' in line:
            parts = line.rsplit(' ', 1)
            tag = parts[0]
        else:
            tag = line
        if tag in skip_words:
            continue
        if ' ' in line:
            tags.append(tag)
    # --- output.txt に上書き ---
    output_text = ", " + ", ".join(tags) + ","
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)
        print("complethion1")
    # --- entry_file に追記（重複チェック付き） ---
    last_entry = ""
    if os.path.exists(entry_file):
        with open(entry_file, 'r', encoding='utf-8') as f:
            lines = f.read().strip().splitlines()
            if lines:
                last_entry = lines[-1]
    if output_text != last_entry:
        with open(entry_file, 'a', encoding='utf-8') as f:
            f.write(output_text + "\n\n")
            print("complethion2 (added)")
    else:
        print("complethion2 (skipped)")
    os.startfile(output_file)
# 実行部分
extract_tags(
    'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/input.txt',
    'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt',
    'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/z4/16.md'
)

# def extract_tags(input_file, output_file, entry_file,):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         tags = []
#         skip_words = {
#             "Character","Characters", "General","original", "?", "Meta",
#             "Artist","name tag", 
#             "artist name","circle name","character name","copyright name",
#             "twitter username","fanbox_username", "subscribestar username","pixiv username","facebook username",
#             "logo", "artist logo","pixiv logo", "patreon logo", "twitter x logo", "bluesky logo", "fanbox logo",
#             "bad id","bad pixiv id","pixiv id",
#             "copyright notice", "watermark", "commentary",
#             "character censor","novelty censor","heart censor","bar censor","censored",
#             "english commentary", "Copyright","english text","korean text","speech bubble",
#             "mosaic censoring","pointless censoring","convenient censoring", 
#             "signature","mixed-language commentary",
#             "adversarial noise","watermark grid",
#             "korean commentary","paid reward available","copyright request", "translated",
#             "variant set", "large variant set", "commission", "pixiv commission","character request",
#             "source request", "third-party edit",
#             "cover", "cover page",  "web_address",
#             "hashtag-only commentary","web address"," chinese commentary"," dated",
#             'second-party source',"odaibako","request inset", 
#         }
#     for line in lines:
#         print(line)
#         line = line.strip()
#         if not line:
#             continue
#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0]
#         else:
#             tag = line
#         if tag in skip_words:
#             continue
#         # スキップしないタグをリストに追加
#         if ' ' in line:
#             tags.append(tag)
#         # 結果をoutput.txtに書き込み
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(", " + ", ".join(tags) + ",")
#             print("complethion"+"1")
#         # 結果を任意の.txtに追加
#         with open(entry_file, 'a', encoding='utf-8') as f:
#             f.write("\n" + ", " + ", ".join(tags) + ",\n\n")
#             print("complethion"+"2")
#     import os
#     os.startfile(r"C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt")


# # 実行部分（ファイルパスは適宜変更） 
# extract_tags(
#             'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/input.txt',
#             'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt',
#             'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/z4/14.md'
#             )
# ==================================================================================================================
# import subprocess
# subprocess.Popen([r"C:/Users/hekat/AppData/Local/Programs/Microsoft VS Code/Code.exe", r"C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt"])
# import subprocess
# subprocess.Popen(["code", "--reuse-window", r"C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt"])

# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     tags = []
#     skip_words = {
#         "Character","Characters", "General","original", "?", "Meta",
#         "Artist","name tag", 
#         "artist name","circle name","character name","copyright name",
#         "twitter username","fanbox_username", "subscribestar username","pixiv username","facebook username",
#         "logo", "artist logo","pixiv logo", "patreon logo", "twitter x logo", "bluesky logo", "fanbox logo",
#         "bad id","bad pixiv id","pixiv id",
#         "copyright notice", "watermark", "commentary",
#         "character censor","novelty censor","heart censor","bar censor","censored",
#         "english commentary", "Copyright","english text","korean text","speech bubble",
#         "mosaic censoring","pointless censoring","convenient censoring", 
#         "signature","mixed-language commentary",
#         "adversarial noise","watermark grid",
#         "korean commentary","paid reward available","copyright request", "translated",
#         "variant set", "large variant set", "commission", "pixiv commission","character request",
#         "source request", "third-party edit",
#         "cover", "cover page",  "web_address",
#         "hashtag-only commentary","web address"," chinese commentary"," dated",
#         'second-party source',"odaibako","request inset", 
#     }

#     for line in lines:
#         print(line)
#         line = line.strip()
#         if not line:
#             continue

#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag = parts[0]
#         else:
#             tag = line

#         if tag in skip_words:
#             continue

#         # スキップしないタグをリストに追加
#         if ' ' in line:
#             tags.append(tag)

#     # 結果をoutput.txtに書き込み
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write(", " + ", ".join(tags) + ",")
#         print("complethion")

# # 実行部分（ファイルパスは適宜変更）
# extract_tags(
#     'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/input.txt',
#     'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt'
# )

# # ==========================================================================================
# import subprocess
# vscode_path = r"C:/Users/hekat/AppData/Local/Programs/Microsoft VS Code/Code.exe"
# output_path = r"C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt"
# subprocess.Popen([vscode_path, output_path])
# # ==========================================================================================
# import subprocess
# import os
# # 実行後に VSCode で output.txt を開く
# output_path = r"C:/Users/hekat/py/Ocean241015/GoogleDiffusion/aiTagmaker/output.txt"
# subprocess.Popen(["code", output_path])
# ==========================================================================================

# https://www.kia.or.jp/event/detail/?id=7504&utm_source=chatgpt.com

# def extract_tags(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()

#     tags = []
#     skip_words = {"characters", "general", "?", "artist name", "twitter username",
#                   "copyright notice", "watermark", "meta", "commentary",
#                   "english commentary", "character", "copyright", "artist", "original"}

#     for line in lines:
#         line = line.strip()
#         if not line or line == "?":
#             continue

#         tag_candidate = ""
#         if ' ' in line:
#             parts = line.rsplit(' ', 1)
#             tag_candidate = parts[0].strip()
#         else:
#             tag_candidate = line

#         # フィルタ（小文字化して判定）
#         if tag_candidate.lower() in skip_words:
#             continue

#         tags.append(tag_candidate)

#     # 出力
#     if tags:
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(", ".join(tags))
#         print(f"{len(tags)} 個のタグを出力しました: {output_file}")
#     else:
#         print("タグが抽出されませんでした。")


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


        # "Character","Characters", "General","original", "?", "Meta",
        # "Artist","artist name","circle name", "twitter username", "copyright name",
        # "copyright notice", "watermark", "commentary","character censor",
        # "english commentary", "Copyright","english text","korean text","speech bubble",
        # "commentary request", "translation request", "censored",
        #   "mosaic censoring","pointless censoring","convenient censoring", 
        # "bar censor","signature","heart censor","mixed-language commentary","novelty censor",
        # "adversarial noise","watermark grid","bad id","bad pixiv id",
        # "korean commentary","paid reward available","copyright request", "translated",
        # "variant set", "large variant set", "commission", "pixiv commission","character request",
        # "source request", "third-party edit","subscribestar username","pixiv username",
        # "character name", "logo", "artist logo","cover", "cover page",  "fanbox_username","web_address",
        # "hashtag-only commentary","facebook username","web address"," chinese commentary"," dated",
        # 'second-party source',"pixiv id","pixiv logo", "patreon logo", "twitter x logo", "bluesky logo", 
        # "fanbox logo", 

# "Character","Characters", "General","original", "?", "Meta",
# "Artist",
# "artist name","circle name","character name","copyright name",
# "twitter username","fanbox_username", "subscribestar username","pixiv username","facebook username",
# "logo", "artist logo","pixiv logo", "patreon logo", "twitter x logo", "bluesky logo", "fanbox logo",
# "bad id","bad pixiv id","pixiv id",
# "copyright notice", "watermark", "commentary",
# "character censor","novelty censor","heart censor","bar censor",
# "english commentary", "Copyright","english text","korean text","speech bubble",
# "mosaic censoring","pointless censoring","convenient censoring", 
# "signature","mixed-language commentary",
# "adversarial noise","watermark grid",
# "korean commentary","paid reward available","copyright request", "translated",
# "variant set", "large variant set", "commission", "pixiv commission","character request",
# "source request", "third-party edit",
# "cover", "cover page",  "web_address",
# "hashtag-only commentary","web address"," chinese commentary"," dated",
# 'second-party source',