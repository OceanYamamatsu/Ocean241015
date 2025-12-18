n=int(input())
grid=[[0]*n for _ in range(n)]
r, c = 0, n//2
grid[r][c] = 1
for _ in range(n**2-1):
    

print(grid)