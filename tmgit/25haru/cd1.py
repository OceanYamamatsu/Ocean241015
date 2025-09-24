# 6×14 の "*" 表をリストに格納
rows = 6
cols = 14
grid = [['*' for _ in range(cols)] for _ in range(rows)]

# # 任意の位置を 0 に置き換える（例：2行3列目 → grid[1][2]）
# row_to_change = 2  # 1から数える行番号
# col_to_change = 5  # 1から数える列番号
# # Pythonのインデックスは0から始まるので -1
# grid[row_to_change - 1][col_to_change - 1] = '0'
lt=[(0,0)]
c=0
for i in range(10):
    x,y=lt[i]
    grid[c][c]="x"
    lt.append([c+1][c+1])

    


# 表示
for row in grid:
    print(''.join(row))