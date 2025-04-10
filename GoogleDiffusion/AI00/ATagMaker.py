def extract_tags(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tags = []
    skip_words = {"Characters", "General", "?"}

    for line in lines:
        line = line.strip()
        if not line or line in skip_words:
            continue
        # 数値が最後についてるので、末尾の数値部分を削除してタグ名だけにする
        if ' ' in line:
            parts = line.rsplit(' ', 1)
            tag = parts[0]
            tags.append(tag)

    # 結果をoutput.txtに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(", " + ", ".join(tags) + ",")

# 使用例
extract_tags('input.txt', 'output.txt')
