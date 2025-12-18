n = int(input())

# n×n のマスを 0（空白）で初期化
grid = [[0]*n for _ in range(n)]


print(grid)
# 初期位置
r, c = 0, n//2
grid[r][c] = 1

# 2 から n^2 まで書き込む
for k in range(2, n*n + 1):
    nr = (r - 1) % n
    nc = (c + 1) % n
    if grid[nr][nc] == 0:
        r, c = nr, nc
    else:
        r = (r + 1) % n
    grid[r][c] = k

# 出力
for row in grid:
    print(*row)
