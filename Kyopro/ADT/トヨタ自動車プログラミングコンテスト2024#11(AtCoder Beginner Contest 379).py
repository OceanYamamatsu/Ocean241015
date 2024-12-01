# トヨタ自動車プログラミングコンテスト2024#11(AtCoder Beginner Contest 379)

# https://atcoder.jp/contests/abc379/tasks

#c


n, m = map(int, input().split())
x=list(map(int,input().split()))
a=list(map(int,input().split()))
xa = list(zip(x, a))
xa.sort()
ans=0
if xa[0][0] != 0:
    kago=xa[0][1]-1
    for i in range(m-1):
        k=xa[i+1][0]-(xa[i][0]+1)

        if kago >= k:
            ans+=k*(k+1)//2
            ans+=(kago-k)*(k+1)
            kago-=k
            kago+=xa[i+1][1]-1
        else:
            print(-1)
            break
    else:
        k=n-xa[-1][0]
        if k==kago:
            ans+=k*(k+1)//2
            print(ans)
        else:
            print(-1)
else:
    print(-1)






