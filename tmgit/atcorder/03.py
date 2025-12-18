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

# ==========================================================
N, M = map(int, input().split())

# マス目の占有状態（False = 空）
grid = [[False]*N for _ in range(N)]

count = 0

for _ in range(M):
    R, C = map(int, input().split())
    R -= 1  # 0-indexed に変換
    C -= 1

    # 2×2 の範囲がすべて空か確認
    can_put = True
    for dr in (0, 1):
        for dc in (0, 1):
            if grid[R+dr][C+dc]:
                can_put = False

    # 置けるなら配置
    if can_put:
        for dr in (0, 1):
            for dc in (0, 1):
                grid[R+dr][C+dc] = True
        count += 1

print(count)

