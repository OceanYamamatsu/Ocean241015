n=int(input())
grid=[[0]*n for _ in range(n)]
r, c, k = 0, (n-1)//2, 1
grid[r][c] = 1
for _ in range(n*n-1):
    k+=1
    if 0 == grid[((r-1)% n)][(c+1)%n]:
        r=(r-1)%n
        c=(c+1)%n
        grid[r][c] = k
    else:
        r=(r+1)% n
        grid[r][c] = k
for u in grid:
    print(*u)
# print([u for u in grid])

