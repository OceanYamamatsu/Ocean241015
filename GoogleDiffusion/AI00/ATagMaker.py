
def extract_tags(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tags = []
    skip_words = {"Characters", "General", "?", "artist name",
                   "twitter username", "copyright notice", "watermark", }

    for line in lines:
        line = line.strip()
        if not line or line in skip_words:
            continue
        # 数値が最後についてるので、末尾の数値部分を削除してタグ名のみに
        if ' ' in line:
            parts = line.rsplit(' ', 1)
            tag = parts[0]
            tags.append(tag)

    # 結果をoutput.txtに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(", " + ", ".join(tags) + ",")

extract_tags('C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/input.txt', 
             'C:/Users/hekat/py/Ocean241015/GoogleDiffusion/AI00/output.txt')
