
# tl,vl=[],[]
# for _ in range(int(input())):
#     t,v=map(int,input().split())
#     tl.append(t)
#     vl.append(v)
# print(sum(vl)-(tl[-1]-tl[0]))

# import random
# x=2
# a=1
# b=10
# ans=[]
# for _ in range(x):
#     ans.append(random.randint(a, b))
#     # print(random.randint(a, b))
# print(ans)

#https://atcoder.jp/contests/abc383/submissions/60678230

h,w,d=map(int,input().split())
men=[]
seen=[]
for i in range(h):
    seen.append([])
    xx=list(input())
    men.append(xx)
    ct=-1
    for q in xx:
        ct+=1
        if q =='H':
            seen[0].append([i,ct])
            xx[ct]=0
ir,id,il,iu=0,1,2,3
idou=[[0,1],[1,0],[0,-1],[-1,0]]
if d > h:
    d=h
for ct in range(d):
    mirutoko = seen[ct]
    for iti in mirutoko:
        for i in idou:
            gyou=iti[0]
            retu=iti[1]
            if iti[0]+i[0] < h and iti[1]+i[1] < w and -1 < iti[0]+i[0] and -1 < iti[1]+i[1]:
                if men[gyou+i[0]][retu+i[1]] != '#':
                    if men[gyou+i[0]][retu+i[1]] == '.':
                        men[gyou+i[0]][retu+i[1]] = (ct+1)
                        seen[ct+1].append([gyou+i[0],retu+i[1]])
                    elif ct+1 < men[gyou+i[0]][retu+i[1]]:
                        men[gyou+i[0]][retu+i[1]] = (ct+1)
                        seen[ct+1].append([gyou+i[0],retu+i[1]])
                    
ans=0
for gyou in men:
    for i in gyou:
        if i != '#' and i != '.':
            ans+=1
print(ans)