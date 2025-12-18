
n,m=map(int, input().split())
grid=set()
G=set()
for u in range(m):
    G=set()
    x,y = map(int, input().split())
    xn=(x-1)*n+y
    yn=x*n+y
    G.update({xn,xn+1,yn,yn+1})
    if 0== len(grid & G):
        grid.update(G)
print(len(grid)//4)


